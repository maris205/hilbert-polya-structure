#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C301 release."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C301_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c301_fragmentation_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C301/2026-09-02.yaml"
TEX = ROOT / "paper/main.tex"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "011f146e1fecfb88a6cc4a692d95a8267b9549cfefa43628083ab1aa21b06a03"
PAYLOAD_SHA = "1fcd7d727f3fd75ce99257c2ee69c6ecc7ff2332ad582628ad72ac9473043c10"
EVALUATION_SHA = "e9300587e9d7e4a84703caa6fdd8d40b7c54d158c3e03beebfc644fd25cecabb"
EVALUATION_SEMANTIC_SHA = "da2690a0a422319416c50563979d15835a2d940032e11f1c017f6c189c224f23"
TEX_SHA = "6b782832e2e47dbeb9582efbd5a6ecc302773a486000443306fbc6c771dc1930"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [
    ROOT / "paper/main_round0_original.pdf",
    ROOT / "paper/main_round1.pdf",
    ROOT / "paper/main_round2.pdf",
]
ROUND_HASHES = [
    "a11bf5746fc2a2056754139143d5abde3ee4f56b56c287c923ce6768a3d0669f",
    "8cd42fe5a6b46792c7a57b9e372a398a0806dd6a6931ec887a28ca99f84055c2",
    "f09a3fc6ee5f1a2c0954d7d4d7db11d98f01cfc7741e9c82a0a8fb98f92ce872",
]
ROUND_PAGES = [2, 3, 3]
ROUND_FONTS = [23, 26, 27]
ROUND_PRESENT = [
    ["all-parameter solution", "binary-word proof"],
    ["the spectral flag and its missing step", "birthday threshold and lattice boundary"],
    ["exact certificate and hostile boundary audit", "route_a_rejected", "no_bad_euler_or_root_number", "ai-use statement"],
]
ROUND_ABSENT = [
    ["the spectral flag and its missing step", "exact certificate and hostile boundary audit"],
    ["exact certificate and hostile boundary audit", "route_a_rejected"],
    [],
]
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c301_fragmentation_checker.py",
    "code/c301_fragmentation_mutation.py", "code/c301_fragmentation_producer.py",
    "code/c301_fragmentation_replay.py", "code/c301_fragmentation_sympy_crosscheck.py",
    "code/c301_release_manifest.py",
    "evaluations/route_a/HCS-C301/2026-09-02.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c301_fragmentation_evidence.json",
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character",
    re.IGNORECASE,
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="strict")
    value = json.loads(text, object_pairs_hook=reject_duplicate_keys, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON top level must be an object")
    canonical = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if text != canonical:
        raise ValueError(f"noncanonical JSON: {path}")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise TypeError("YAML keys must be strings")
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return value


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def run(command: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
    if result.returncode:
        raise RuntimeError("command failed: " + " ".join(command) + "\n" + result.stdout)
    return result.stdout.strip()


def fresh_pdf(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c301-r{round_number}-") as folder:
        work = Path(folder)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        tex_arg = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", tex_arg]
        run(command, cwd=work, env=env)
        run(command, cwd=work, env=env)
        return (work / "main.pdf").read_bytes(), (work / "main.log").read_text(errors="replace")


def pdf_pages(path: Path) -> int:
    output = run(["pdfinfo", str(path)])
    match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
    if not match:
        raise AssertionError("pdfinfo omitted page count")
    return int(match.group(1))


def font_count(path: Path) -> int:
    lines = run(["pdffonts", str(path)]).splitlines()[2:]
    if not lines:
        raise AssertionError("PDF has no fonts")
    for line in lines:
        if re.search(r"\byes\s+yes\s+(?:yes|no)\s+\d+\s+\d+\s*$", line) is None:
            raise AssertionError("non-embedded or non-subset font row: " + line)
    return len(lines)


def render_count(path: Path, pages: int) -> int:
    with tempfile.TemporaryDirectory(prefix="c301-render-") as folder:
        prefix = Path(folder) / "page"
        run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)])
        rendered = list(Path(folder).glob("page-*.png"))
        if any(item.stat().st_size == 0 for item in rendered):
            raise AssertionError("empty rendered page")
        if len(rendered) != pages:
            raise AssertionError("rendered page count mismatch")
        return len(rendered)


def pdf_text(path: Path) -> str:
    return run(["pdftotext", str(path), "-"]).lower()


def validate_metadata(evidence: dict, evaluation: dict) -> None:
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert evidence["payload_sha256"] == PAYLOAD_SHA == payload_hash(evidence)
    assert digest(EVALUATION) == EVALUATION_SHA
    assert semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA
    assert digest(TEX) == TEX_SHA
    assert evidence["candidate_id"] == evaluation["candidate_id"] == "HCS-C301"
    assert evidence["obstruction_id"] == evaluation["obstruction_id"] == "HEN-O285"
    assert evidence["source_commit"] == evaluation["source_commit"] == SOURCE
    assert evidence["fixed_epoch"] == evaluation["fixed_epoch"] == EPOCH
    assert evidence["scope_literal"] == evaluation["scope_literal"] == SCOPE
    assert evidence["evaluator_authority_sha256"] == evaluation["evaluator_authority_sha256"] == EVALUATOR
    assert evidence["route_a"]["tuple"] == evaluation["tuple"] == TUPLE
    assert evidence["route_a"]["overall_verdict"] == evaluation["overall_verdict"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evaluation["route_b_invocation_allowed"] is False
    assert evidence["scope_flags"] == evaluation["scope_flags"] == FLAGS
    assert all(value is False for value in FLAGS.values())


def main() -> None:
    producer_output = run([sys.executable, str(ROOT / "code/c301_fragmentation_producer.py")])
    checker_output = run([sys.executable, str(ROOT / "code/c301_fragmentation_checker.py")])
    sympy_output = run([sys.executable, str(ROOT / "code/c301_fragmentation_sympy_crosscheck.py")])
    replay_output = run([sys.executable, str(ROOT / "code/c301_fragmentation_replay.py")])
    mutation_output = run([sys.executable, str(ROOT / "code/c301_fragmentation_mutation.py")])

    evidence = strict_json(EVIDENCE)
    evaluation = strict_yaml(EVALUATION)
    validate_metadata(evidence, evaluation)

    round_rows = []
    for number, (archive, expected_sha, expected_pages, expected_fonts) in enumerate(
        zip(ROUND_PATHS, ROUND_HASHES, ROUND_PAGES, ROUND_FONTS)
    ):
        first, first_log = fresh_pdf(number)
        second, second_log = fresh_pdf(number)
        archived = archive.read_bytes()
        assert first == second == archived
        assert hashlib.sha256(archived).hexdigest() == expected_sha
        assert WARNING_RE.search(first_log) is None
        assert WARNING_RE.search(second_log) is None
        pages = pdf_pages(archive)
        fonts = font_count(archive)
        assert pages == expected_pages
        assert fonts == expected_fonts
        assert render_count(archive, pages) == pages
        text = pdf_text(archive)
        for marker in ROUND_PRESENT[number]:
            assert marker in text, f"round {number} missing {marker}"
        for marker in ROUND_ABSENT[number]:
            assert marker not in text, f"round {number} unexpectedly has {marker}"
        round_rows.append({
            "round": number,
            "path": archive.relative_to(ROOT).as_posix(),
            "sha256": expected_sha,
            "pages": pages,
            "embedded_subset_font_rows": fonts,
            "two_fresh_builds_identical": True,
            "archived_bytes_match": True,
            "warning_free_second_passes": True,
            "rendered_pages": pages,
        })

    assert len(set(ROUND_HASHES)) == 3
    final_pdf = ROOT / "paper/main.pdf"
    assert final_pdf.read_bytes() == ROUND_PATHS[2].read_bytes()
    assert digest(final_pdf) == ROUND_HASHES[2]

    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*") if path.is_file()
    }
    assert actual == EXPECTED | {MANIFEST.name}, (
        "physical tree mismatch", sorted(actual - (EXPECTED | {MANIFEST.name})),
        sorted((EXPECTED | {MANIFEST.name}) - actual),
    )

    files = [
        {"path": relative, "sha256": digest(ROOT / relative), "bytes": (ROOT / relative).stat().st_size}
        for relative in sorted(EXPECTED)
    ]
    manifest = {
        "schema": "hcs-c301-release-manifest-v1",
        "candidate_id": "HCS-C301",
        "obstruction_id": "HEN-O285",
        "title": "Parallel binary refinement of labelled set partitions",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "payload_file_count": len(EXPECTED),
        "physical_file_count": len(EXPECTED) + 1,
        "evidence": {
            "path": EVIDENCE.relative_to(ROOT).as_posix(),
            "file_sha256": EVIDENCE_SHA,
            "payload_sha256": PAYLOAD_SHA,
            "transition_state_rows": evidence["regression_summary"]["transition_state_rows"],
            "nonzero_transition_cells": evidence["regression_summary"]["transition_nonzero_probability_cells"],
            "time_rows": evidence["regression_summary"]["time_rows"],
            "block_count_coefficient_cells": evidence["regression_summary"]["block_count_coefficient_cells"],
            "absorption_mass_rows": evidence["regression_summary"]["absorption_mass_rows"],
        },
        "evaluation": {
            "path": EVALUATION.relative_to(ROOT).as_posix(),
            "file_sha256": EVALUATION_SHA,
            "semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "tuple": TUPLE,
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "scope_flags": FLAGS,
        },
        "paper": {
            "tex_sha256": TEX_SHA,
            "rounds": round_rows,
            "all_round_hashes_distinct": True,
            "final_path": "paper/main.pdf",
            "final_sha256": ROUND_HASHES[2],
            "final_equals_round2": True,
        },
        "verification": {
            "producer": producer_output.splitlines(),
            "independent_checker": checker_output.splitlines(),
            "sympy_crosscheck": sympy_output.splitlines(),
            "deterministic_replay": replay_output.splitlines(),
            "mutation_suite": mutation_output.splitlines(),
            "closed_world": True,
        },
        "files": files,
    }
    MANIFEST.write_text(json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    reread = strict_json(MANIFEST)
    assert reread == manifest
    assert len(files) == 27 and len(actual) == 28
    print("C301 release PASS")
    print(f"payload_files={len(files)} physical_files={len(actual)}")
    print(f"evidence_sha256={EVIDENCE_SHA}")
    print(f"payload_sha256={PAYLOAD_SHA}")
    print(f"final_pdf_sha256={ROUND_HASHES[2]}")
    print(f"manifest_sha256={digest(MANIFEST)}")


if __name__ == "__main__":
    main()
