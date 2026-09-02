#!/usr/bin/env python3
"""End-to-end deterministic release closure for HCS-C306."""
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

if sys.flags.optimize:
    raise RuntimeError("HCS-C306 release refuses python -O")

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C306_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c306_walkers_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C306/2026-09-03.yaml"
TEX = ROOT / "paper/main.tex"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
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
ROUND_PATHS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
PRESENT = [
    ["full killed semigroup atlas", "complete orthonormal basis"],
    ["entire absorption law and its leading edge", "immortal doob dynamics", "unique qsd"],
    ["faces, finite evidence, and claim boundary", "a4_formal_hint", "no_bad_euler_or_root_number", "ai-use statement"],
]
ABSENT = [
    ["entire absorption law and its leading edge", "faces, finite evidence, and claim boundary"],
    ["faces, finite evidence, and claim boundary", "no_bad_euler_or_root_number"],
    [],
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "code/README.md",
    "code/c306_walkers_checker.py", "code/c306_walkers_mutation.py", "code/c306_walkers_producer.py",
    "code/c306_walkers_replay.py", "code/c306_walkers_sympy_crosscheck.py", "code/c306_release_manifest.py",
    "evaluations/route_a/HCS-C306/2026-09-03.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c306_walkers_evidence.json",
}
WARNING_RE = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character", re.I)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def duplicate_guard(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path: Path) -> dict:
    text = path.read_bytes().decode("utf-8", errors="strict")
    value = json.loads(text, object_pairs_hook=duplicate_guard, parse_constant=reject_nonfinite)
    check(type(value) is dict, "JSON top level")
    check(text == json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n", "canonical JSON")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("non-string or duplicate YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    check(type(value) is dict, "YAML top level")
    return value


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def payload_hash(value: dict) -> str:
    body = dict(value)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def run(command: list[str], cwd: Path | None = None, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if result.returncode:
        raise RuntimeError("command failed: " + " ".join(command) + "\n" + result.stdout)
    return result.stdout.strip()


def fresh_pdf(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c306-r{round_number}-") as folder:
        work = Path(folder)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        argument = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", argument]
        run(command, cwd=work, env=env)
        run(command, cwd=work, env=env)
        return (work / "main.pdf").read_bytes(), (work / "main.log").read_text(errors="replace")


def pdf_pages(path: Path) -> int:
    match = re.search(r"^Pages:\s+(\d+)\s*$", run(["pdfinfo", str(path)]), re.M)
    check(match is not None, "page count")
    return int(match.group(1))


def font_count(path: Path) -> int:
    rows = run(["pdffonts", str(path)]).splitlines()[2:]
    check(bool(rows), "font rows")
    for row in rows:
        check(re.search(r"\byes\s+yes\s+(?:yes|no)\s+\d+\s+\d+\s*$", row) is not None,
              "font not embedded/subset: " + row)
    return len(rows)


def render_count(path: Path, pages: int) -> int:
    with tempfile.TemporaryDirectory(prefix="c306-render-") as folder:
        prefix = Path(folder) / "page"
        run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)])
        images = list(Path(folder).glob("page-*.png"))
        check(len(images) == pages and all(image.stat().st_size > 0 for image in images), "render")
        return len(images)


def validate_contract(evidence: dict, evaluation: dict) -> None:
    check(evidence["payload_sha256"] == payload_hash(evidence), "evidence payload hash")
    check(evidence["candidate_id"] == evaluation["candidate_id"] == "HCS-C306", "candidate")
    check(evidence["obstruction_id"] == evaluation["obstruction_id"] == "HEN-O290", "obstruction")
    check(evidence["source_commit"] == evaluation["source_commit"] == SOURCE, "source")
    check(type(evidence["fixed_epoch"]) is int and evidence["fixed_epoch"] == EPOCH, "evidence epoch")
    check(type(evaluation["fixed_epoch"]) is int and evaluation["fixed_epoch"] == EPOCH, "evaluation epoch")
    check(evidence["scope_literal"] == evaluation["scope_literal"] == SCOPE, "scope")
    check(evidence["evaluator_authority_sha256"] == evaluation["evaluator_authority_sha256"] == EVALUATOR, "evaluator")
    check(evidence["route_a"]["tuple"] == evaluation["tuple"] == TUPLE, "tuple")
    check(evidence["route_a"]["overall_verdict"] == evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "verdict")
    check(evidence["route_a"]["route_b_invocation_allowed"] is False and evaluation["route_b_invocation_allowed"] is False, "route B")
    check(evidence["scope_flags"] == evaluation["scope_flags"] == FLAGS, "flags")


def main() -> None:
    outputs = {
        "producer": run([sys.executable, str(ROOT / "code/c306_walkers_producer.py")]),
        "independent_checker": run([sys.executable, str(ROOT / "code/c306_walkers_checker.py")]),
        "sympy_crosscheck": run([sys.executable, str(ROOT / "code/c306_walkers_sympy_crosscheck.py")]),
        "deterministic_replay": run([sys.executable, str(ROOT / "code/c306_walkers_replay.py")]),
        "mutation_suite": run([sys.executable, str(ROOT / "code/c306_walkers_mutation.py")]),
    }
    evidence = strict_json(EVIDENCE)
    evaluation = strict_yaml(EVALUATION)
    validate_contract(evidence, evaluation)

    round_rows = []
    for number, archive in enumerate(ROUND_PATHS):
        first, log1 = fresh_pdf(number)
        second, log2 = fresh_pdf(number)
        archived = archive.read_bytes()
        check(first == second == archived, f"round {number} nondeterministic or stale")
        check(WARNING_RE.search(log1) is None and WARNING_RE.search(log2) is None, f"round {number} warning")
        pages = pdf_pages(archive)
        fonts = font_count(archive)
        text = run(["pdftotext", str(archive), "-"]).lower()
        check(all(marker in text for marker in PRESENT[number]), f"round {number} missing sentinel")
        check(all(marker not in text for marker in ABSENT[number]), f"round {number} leaked future content")
        rendered = render_count(archive, pages)
        round_rows.append({
            "round": number,
            "path": archive.relative_to(ROOT).as_posix(),
            "sha256": digest(archive),
            "pages": pages,
            "embedded_subset_font_rows": fonts,
            "two_fresh_builds_identical": True,
            "archived_bytes_match": True,
            "warning_free_second_passes": True,
            "rendered_pages": rendered,
        })
    round_hashes = [row["sha256"] for row in round_rows]
    check(len(set(round_hashes)) == 3, "round hashes not distinct")
    final = ROOT / "paper/main.pdf"
    check(final.read_bytes() == ROUND_PATHS[2].read_bytes(), "final is not round 2")

    actual = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_file()}
    check(actual in (EXPECTED, EXPECTED | {MANIFEST.name}), "closed-world tree mismatch")
    files = [{"path": name, "sha256": digest(ROOT / name), "bytes": (ROOT / name).stat().st_size}
             for name in sorted(EXPECTED)]
    manifest = {
        "schema": "hcs-c306-release-manifest-v1",
        "candidate_id": "HCS-C306",
        "obstruction_id": "HEN-O290",
        "title": "Killed noncolliding walkers: determinant, spectrum, absorption, and Q-process",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "payload_file_count": len(EXPECTED),
        "physical_file_count": len(EXPECTED) + 1,
        "evidence": {
            "path": EVIDENCE.relative_to(ROOT).as_posix(),
            "file_sha256": digest(EVIDENCE),
            "payload_sha256": evidence["payload_sha256"],
            **evidence["regression_summary"],
        },
        "evaluation": {
            "path": EVALUATION.relative_to(ROOT).as_posix(),
            "file_sha256": digest(EVALUATION),
            "semantic_sha256": semantic_hash(evaluation),
            "tuple": TUPLE,
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "scope_flags": FLAGS,
        },
        "paper": {
            "tex_sha256": digest(TEX),
            "rounds": round_rows,
            "all_round_hashes_distinct": True,
            "final_path": "paper/main.pdf",
            "final_sha256": digest(final),
            "final_equals_round2": True,
        },
        "verification": {key: value.splitlines() for key, value in outputs.items()} | {"closed_world": True},
        "files": files,
    }
    MANIFEST.write_text(json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    check(strict_json(MANIFEST) == manifest, "manifest parse")
    check(len(files) == 27, "payload count")
    final_actual = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_file()}
    check(final_actual == EXPECTED | {MANIFEST.name} and len(final_actual) == 28, "physical count")
    print("C306 release PASS")
    print(f"payload_files={len(files)} physical_files={len(final_actual)}")
    print(f"evidence_sha256={digest(EVIDENCE)}")
    print(f"payload_sha256={evidence['payload_sha256']}")
    print(f"final_pdf_sha256={digest(final)}")
    print(f"manifest_sha256={digest(MANIFEST)}")


if __name__ == "__main__":
    main()
