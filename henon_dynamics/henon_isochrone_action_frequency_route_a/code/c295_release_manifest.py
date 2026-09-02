#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C295 release."""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml
from yaml.constructor import ConstructorError
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C295_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c295_isochrone_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C295/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "3eafe6ca64829ce4389efe8d11b89f556f018e67bdd59595e2330e28c702f472"
EVALUATION_RAW_SHA = "f7999ef49bf34162b0a9385ef6e26a52933081d200957030297cf8894738d134"
EVALUATION_SEMANTIC_SHA = "371a0e27dcd17ba950b06ab7ece415469ea998b244ba1eb6e208851182ec365d"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "959003cf32111953109f9a64875503805f120bf7bdd1310c62269db34a3fcd79",
    "d81c873e253e1505f316844fc27ad0cb6cd972e60736fe926d0de4f4c2cb691f",
    "e89f5fa8ba9d9b2148f7d15d2b1d48d6767681278ff6c123fd61f2e673b87f3b",
]
ROUND_TEXT = [
    ("exact circular-energy boundary", "quadratic turning-point reduction", "bound motion exists exactly"),
    ("noncircular closure criterion", "rationality test does not apply", "full cartesian period is 2tr"),
    ("87/87 hostile rejections", "duplicate-key-rejecting", "route_a_rejected", "no_bad_euler_or_root_number"),
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c295_isochrone_checker.py", "code/c295_isochrone_mutation.py",
    "code/c295_isochrone_producer.py", "code/c295_isochrone_replay.py",
    "code/c295_isochrone_sympy_crosscheck.py", "code/c295_release_manifest.py",
    "evaluations/route_a/HCS-C295/2026-09-02.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c295_isochrone_evidence.json",
}
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict[str, Any]) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe YAML with dates kept as strings and every duplicate rejected."""


UniqueYAMLLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader: UniqueYAMLLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge" or key_node.value == "<<":
            raise ConstructorError("mapping", node.start_mark, "YAML merge forbidden", key_node.start_mark)
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ConstructorError("mapping", node.start_mark, "duplicate/non-string YAML key", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict[str, Any]:
    text = path.read_text()
    if any(isinstance(token, (AnchorToken, AliasToken)) for token in yaml.scan(text)):
        raise ValueError("YAML anchor or alias forbidden")
    value = yaml.load(text, Loader=UniqueYAMLLoader)
    if type(value) is not dict:
        raise TypeError("YAML top-level object required")
    return value


def semantic_hash(value: dict[str, Any]) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    report = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in report.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    report = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in report.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    report = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(report.lower().split())


def render_count(path: Path) -> int:
    with tempfile.TemporaryDirectory(prefix="c295-render-") as temporary:
        prefix = Path(temporary) / "page"
        subprocess.run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return len(list(Path(temporary).glob("page-*.png")))


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c295-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING_RE.search(log)
        if match:
            raise AssertionError(f"round {round_number} settled warning: {match.group(0)}")
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    producer = run_python("c295_isochrone_producer.py")
    assert "C295_PRODUCER_PASS" in producer
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data) == "55c88124800ae58a683a1914b9ddb0dd40e54f514a36e8cf54bd00c32a39e82e"
    assert data["schema"] == "hcs-c295-henon-isochrone-action-frequency-v1"
    assert data["candidate_id"] == "HCS-C295" and data["obstruction_id"] == "HEN-O279"
    assert data["source_commit"] == SOURCE and data["evaluation_date"] == "2026-09-02"
    assert data["fixed_epoch"] == EPOCH and type(data["fixed_epoch"]) is int
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(type(value) is bool and value is False for value in data["scope_flags"].values())
    assert data["enumeration"] == {
        "mu_values": [1, 2, 3], "b_values": [1, 2, 3], "ell_values": [0, 1, 2, 3],
        "action_multipliers": [1, 2, 3], "orbit_cells": 108, "boundary_cells": 8,
        "closure_counts": {"closed_degenerate": 36, "closed_radial": 18, "closed_resonant": 14, "nonclosed_irrational": 40},
    }
    assert [ref["identifier"] for ref in data["references"]] == [
        "1959AnAp...22..126H", "1959AnAp...22..491H", "10.1063/5.0056957", "10.1093/mnras/stab3020"
    ]

    assert digest(EVALUATION) == EVALUATION_RAW_SHA
    evaluation = strict_yaml(EVALUATION)
    assert semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA
    assert evaluation["schema"] == "route-a-evaluation-v0.2.0"
    assert evaluation["candidate_id"] == "HCS-C295" and evaluation["obstruction_id"] == "HEN-O279"
    assert evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == EPOCH
    assert evaluation["scope_literal"] == SCOPE and evaluation["evaluator_authority_sha256"] == EVALUATOR
    assert evaluation["tuple"] == TUPLE and evaluation["overall_verdict"] == "ROUTE_A_REJECTED"
    assert evaluation["route_b_invocation_allowed"] is False
    assert evaluation["theorem_status"] == "PROVABLE_AS_STATED"
    assert evaluation["source_owner_tokens"] == [
        "1959AnAp...22..126H", "1959AnAp...22..491H", "10.1063/5.0056957", "10.1093/mnras/stab3020"
    ]

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in ("PROVABLE_AS_STATED", "Bound motion exists exactly", "full Cartesian phase point returns after \\(2T_r\\)", "bounded-perturbation theorem", "A1_WEAK"):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in ("1959AnAp...22..126H", "1959AnAp...22..491H", "10.1063/5.0056957", "10.1093/mnras/stab3020", "does **not** claim"):
        assert token in source_audit, token
    tex = TEX.read_text()
    for token in ("Complete bound action theorem", "Apsidal map and noncircular closure", "full Cartesian period is \\(2T_r\\)", "87/87 hostile rejections", "ROUTE\\_A\\_REJECTED"):
        assert token in tex, token

    checker_source = (ROOT / "code/c295_isochrone_checker.py").read_text()
    tree = ast.parse(checker_source)
    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    for token in ("object_pairs_hook=reject_duplicates", "AliasToken", "YAML_SEMANTIC_SHA", "direct period quadrature", "direct apsidal quadrature"):
        assert token in checker_source, token
    mutation_source = (ROOT / "code/c295_isochrone_mutation.py").read_text()
    for token in ("stale-payload-hash", "primitive-cycles-bool", "yaml-anchor", "yaml-merge"):
        assert token in mutation_source, token

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "six fresh builds total", "byte-identical", "embedded and subset", *ROUND_HASHES):
        assert token in compile_report, token
    hostile = (ROOT / "results/HOSTILE_AUDIT.md").read_text()
    for token in ("All 87 attacks", "62 evidence-JSON attacks", "25 evaluation-YAML attacks", "booleans for integers", "anchors, aliases, merge keys", "affirmative target Euler/root-number claim"):
        assert token in hostile, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == [2, 3, 4]
    font_counts: list[int] = []
    render_counts: list[int] = []
    for path, required, page_count in zip(ROUND_PATHS, ROUND_TEXT, pages):
        rows = font_rows(path)
        assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows))
        text = pdf_text(path)
        for token in required:
            assert token in text, (path.name, token)
        render_counts.append(render_count(path))
        assert render_counts[-1] == page_count
    assert font_counts == [16, 21, 22]

    fresh_hashes: list[list[str]] = []
    for round_number, (archive, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected, expected]
        fresh_hashes.append(pair)

    checker = run_python("c295_isochrone_checker.py")
    symbolic = run_python("c295_isochrone_sympy_crosscheck.py")
    replay = run_python("c295_isochrone_replay.py")
    mutation = run_python("c295_isochrone_mutation.py")
    assert "C295 independent checker: PASS" in checker and "strict duplicate-rejecting JSON/YAML" in checker
    assert "C295_SYMPY_PASS" in symbolic and "C295 fresh-path byte replay: PASS" in replay
    assert "C295_MUTATION_PASS 87/87" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    mutation_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, mutation_n) == (11254, 1099, 87)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c295-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C295",
        "obstruction_id": "HEN-O279",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "complete Hénon isochrone bound action-frequency, apsidal, closure, and degenerate-boundary atlas",
        "theorem_status": "PROVABLE_AS_STATED",
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2, "settled_warning_regex": WARNING_RE.pattern,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages, "round_embedded_subset_font_rows": font_counts,
            "round_rendered_page_counts": render_counts,
            "all_round_text_contracts": [list(tokens) for tokens in ROUND_TEXT],
            "visual_inspection": "PASS all final-round pages", "final_equals": "paper/main_round2.pdf",
        },
        "evaluation_contract": {
            "path": str(EVALUATION.relative_to(ROOT)), "raw_sha256": EVALUATION_RAW_SHA,
            "semantic_sha256": EVALUATION_SEMANTIC_SHA, "duplicate_keys_rejected": True,
            "anchors_aliases_merges_rejected": True, "exact_schema_types_values": True,
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G0a_strict_evaluation_yaml": "PASS",
            "G1_exact_duplicate_rejecting_json": "PASS",
            "G2_circular_minimum_and_energy_domain": "PASS",
            "G3_exact_action_period_and_frequency_map": "PASS",
            "G4_apsidal_integral_and_closure": "PASS",
            "G5_circular_radial_escape_signed_kepler_boundaries": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_revisions": "PASS",
            "G8_six_fresh_pdf_builds_fonts_logs_text_render": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_claim_source_traceability": "PASS",
            "G11_target_euler_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "orbit_cells": 108, "boundary_cells": 8, "audited_cells": 116,
            "closure_counts": data["enumeration"]["closure_counts"],
            "checker_assertions": checker_n, "symbolic_checks": symbolic_n,
            "hostile_rejections": mutation_n, "evidence_json_hostile_rejections": 62,
            "evaluation_yaml_hostile_rejections": 25, "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": EVIDENCE_SHA,
            "evaluation_raw_sha256": EVALUATION_RAW_SHA,
            "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "pdf_sha256": digest(PDF), "pdf_pages": pages[-1],
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C295_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C295_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA,
        "pdf_sha256": digest(PDF), "pdf_pages": pages[-1],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
