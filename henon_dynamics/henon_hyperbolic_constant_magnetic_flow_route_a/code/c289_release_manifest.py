#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C289 release."""
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

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C289_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c289_magnetic_evidence.json"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C289/2026-09-02.yaml"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "83a0f4b44909a88931ba20bff50019d6a6824b77aefc8a9e30406ab97d06eac0"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
ROUND_PATHS = [PAPER/"main_round0_original.pdf", PAPER/"main_round1.pdf", PAPER/"main_round2.pdf"]
ROUND_HASHES = [
    "989ee3a527d893e2ba2e8f0a7d17ab82629a3225b5c4fec1cb6ecadd1a1b64b4",
    "f63494f71de5b93efa02aed2b4a53785b47abba082adc25eb2bd26ef857a9f35",
    "c3361619fe4d967223415894bd712a772989827a0ebc2de5b0fd98872b328cd1",
]
ROUND_TEXT = [
    ("complete orbit atlas", "nonclosed horocycle", "primitive period"),
    ("independent geometric recovery", "completeness does and does not assert", "nilpotency index three"),
    ("finite evidence and hostile separation", "43/43", SCOPE.lower(), "route_a_rejected", "ai-use statement"),
]
EXPECTED = {
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md", "PAPER_IMPROVEMENT_LOG.md",
    "code/README.md", "code/c289_magnetic_producer.py", "code/c289_magnetic_checker.py",
    "code/c289_magnetic_sympy_crosscheck.py", "code/c289_magnetic_replay.py",
    "code/c289_magnetic_mutation.py", "code/c289_release_manifest.py",
    "evaluations/route_a/HCS-C289/2026-09-02.yaml",
    "results/c289_magnetic_evidence.json", "results/RESULTS.md", "results/TEST_REPORT.md", "results/HOSTILE_AUDIT.md",
    "paper/README.md", "paper/COMPILE_REPORT.md", "paper/main.tex", "paper/main.pdf",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
}
WARNING_RE = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined references|Rerun to get|Missing character")
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}
YAML_SEMANTIC_SHA = "0c1fb9d1e91cd69e18c2fa2ff074ce0f237341810a225d7c9798414307a31c86"


class UniqueYAMLLoader(yaml.SafeLoader):
    pass


def construct_unique_mapping(loader: UniqueYAMLLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_python(name: str) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT/"code"/name)], env=env, text=True)


def pages(path: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in out.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    out = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    return " ".join(subprocess.check_output(["pdftotext", str(path), "-"], text=True).lower().split())


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c289-r{round_number}-") as tmp:
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=tmp, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (Path(tmp)/"main.log").read_text(errors="replace")
        hit = WARNING_RE.search(log); assert hit is None, hit.group(0) if hit else ""
        return (Path(tmp)/"main.pdf").read_bytes(), log


def main() -> None:
    assert "C289_PRODUCER_PASS" in run_python("c289_magnetic_producer.py")
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c289-hyperbolic-magnetic-flow-v1"
    assert data["candidate_id"] == "HCS-C289" and data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-02" and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE and data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["model"]["frame_ode"].endswith("displayed right-action generator")
    assert data["theorem_contract"]["critical"].endswith("nonzero nilpotent")
    assert data["proof_contract"]["finite_role"].startswith("finite cells audit")
    assert data["proof_contract"]["critical_basepoint"].endswith("no nonzero time returns the base point")
    assert "returns iff sqrt(delta)t lies in 2 pi Z" in data["proof_contract"]["circle_primitivity"]
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(type(value) is bool and value is False for value in data["scope_flags"].values())
    assert data["enumeration"]["orbit_cells"] == 144 and data["enumeration"]["boundary_cells"] == 5
    assert [ref["identifier"] for ref in data["references"]] == ["10.1016/0003-4916(87)90098-4", "10.3836/tjm/1270043477"]

    route_yaml = yaml.load(YAML_PATH.read_text(), Loader=UniqueYAMLLoader)
    assert type(route_yaml) is dict and set(route_yaml) == YAML_KEYS
    assert route_yaml["schema"] == "route-a-evaluation-v0.2.0"
    assert route_yaml["candidate_id"] == "HCS-C289" and route_yaml["evaluation_date"] == "2026-09-02"
    assert route_yaml["source_commit"] == SOURCE and route_yaml["fixed_epoch"] == EPOCH and type(route_yaml["fixed_epoch"]) is int
    assert route_yaml["scope_literal"] == SCOPE and route_yaml["evaluator_authority_sha256"] == EVALUATOR
    assert route_yaml["obstruction_id"] == "HEN-O273" and route_yaml["orbit_cutoff"] == "not applicable"
    assert route_yaml["tuple"] == TUPLE and route_yaml["overall_verdict"] == "ROUTE_A_REJECTED"
    assert route_yaml["route_b_invocation_allowed"] is False
    assert route_yaml["a4"]["verdict"] == "A4_FORMAL_HINT" and route_yaml["a4"]["evidence_status"] == "BOUNDED_NONCLAIM"
    assert route_yaml["scope_flags"] == data["scope_flags"] and all(type(value) is bool for value in route_yaml["scope_flags"].values())
    yaml_semantic = json.dumps(route_yaml, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    assert hashlib.sha256(yaml_semantic.encode()).hexdigest() == YAML_SEMANTIC_SHA
    joined = " ".join((ROOT/"THEOREM_PACKAGE.md").read_text().split())
    for token in ("PROVABLE AS STATED", "right-action ODE", "A^2!=0", "Finite evidence is regression evidence only"):
        assert token in joined, token
    source_audit = (ROOT/"SOURCE_AUDIT.md").read_text()
    for token in ("10.1016/0003-4916(87)90098-4", "10.3836/tjm/1270043477", "not literature-level originality"):
        assert token in source_audit, token
    tex = " ".join(TEX.read_text().split())
    for token in ("right-action equation", "Complete orbit atlas", "A^2\\ne0", "finite grid; the all-parameter proof", "individual circle trajectories have intrinsic primitive periods", "no enumerable isolated primitive", "ledger or repetition census", "AI-use statement"):
        assert token in tex, token

    checker_source = (ROOT/"code/c289_magnetic_checker.py").read_text(); tree = ast.parse(checker_source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import): imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom): imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    for token in ("object_pairs_hook=reject_duplicates", "UniqueYAMLLoader", "YAML_SEMANTIC_SHA", "mp.expm", "A3 == scale(-delta, A)", "A2 != zero and A3 == zero", "basepoint return forces sin(theta)=0 and cos(theta)=1", "critical basepoint T-coordinate equals kappa*v*t"):
        assert token in checker_source, token

    compile_report = (PAPER/"COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "two isolated fresh directories", "byte-identical", "warning-free", *ROUND_HASHES):
        assert token in compile_report, token
    hostile = (ROOT/"results/HOSTILE_AUDIT.md").read_text()
    for token in ("duplicate JSON keys", "A^2!=0", "finite enumeration"):
        assert token in hostile, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED-set(files)), sorted(set(files)-EXPECTED))
    assert len(files) == 27
    archived = [digest(path) for path in ROUND_PATHS]
    assert archived == ROUND_HASHES and len(set(archived)) == 3
    assert digest(PAPER/"main.pdf") == ROUND_HASHES[2]
    page_counts = [pages(path) for path in ROUND_PATHS]; assert page_counts == [2, 3, 4]
    font_counts = []
    for path, terms in zip(ROUND_PATHS, ROUND_TEXT):
        rows = font_rows(path); assert rows
        assert all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows)); text = pdf_text(path)
        for term in terms: assert term in text, (path.name, term)
    assert font_counts == [23, 23, 24]
    fresh_hashes = []
    for number, (path, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, _ = fresh_build(number); second, _ = fresh_build(number)
        assert first == second == path.read_bytes()
        fresh_hashes.append([hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()])
        assert fresh_hashes[-1] == [expected, expected]

    checker = run_python("c289_magnetic_checker.py")
    symbolic = run_python("c289_magnetic_sympy_crosscheck.py")
    replay = run_python("c289_magnetic_replay.py")
    mutation = run_python("c289_magnetic_mutation.py")
    cm = re.search(r"PASS \((\d+) assertions", checker); sm = re.search(r"PASS \((\d+) symbolic", symbolic); mm = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert cm and int(cm.group(1)) == 4613
    assert sm and int(sm.group(1)) == 371
    assert "C289 byte replay: PASS" in replay
    assert mm and mm.group(1) == mm.group(2) == "43"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c289-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C289",
        "evaluation_date": "2026-09-02", "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "headline": "Complete hyperbolic constant-magnetic-flow orbit atlas with exact primitive period and critical nilpotency",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {"engine": "LuaLaTeX", "passes_per_build": 2, "fresh_builds_per_round": 2, "settled_warning_regex": WARNING_RE.pattern, "round_artifacts": [str(p.relative_to(ROOT)) for p in ROUND_PATHS], "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes, "round_pdf_pages": page_counts, "round_embedded_subset_font_rows": font_counts, "all_round_text_contracts": [list(t) for t in ROUND_TEXT], "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator": "PASS", "G1_strict_schema_and_full_grid": "PASS", "G2_lorentz_frame_cubic": "PASS", "G3_all_parameter_orbit_classification": "PASS", "G4_primitive_period_and_critical_nonclosure": "PASS", "G5_boundary_faces": "PASS", "G6_checker_sympy_replay_mutation": "PASS", "G7_two_substantive_revisions": "PASS", "G8_six_fresh_pdf_builds_fonts_logs_text": "PASS", "G9_manifest_hash_closure": "PASS", "G10_source_owner_and_originality_boundary": "PASS", "G11_route_b": "NOT_INVOKED"},
        "results": {"orbit_cells": 144, "boundary_cells": 5, "checker_assertions": int(cm.group(1)), "symbolic_checks": int(sm.group(1)), "hostile_rejections": int(mm.group(1)), "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PAPER/"main.pdf"), "pdf_pages": 4},
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C289_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C289_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PAPER/"main.pdf")}, sort_keys=True))


if __name__ == "__main__":
    main()
