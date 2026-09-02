#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C297 release."""
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

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C297_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c297_pt_dimer_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C297/2026-09-02.yaml"
PAPER = ROOT / "paper"; TEX = PAPER / "main.tex"; PDF = PAPER / "main.pdf"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
OBSTRUCTION = "HEN-O281"
ROUTE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "e10307506e636527f3296fda541e627b6c17b704c059eb3c2845054beb87ccb2",
    "3208737429a4d28a18f399d038271a4b74ea2b7b9851887c627033dade1c337d",
    "a6122768fabaa99cfa3ab62ef28384a5360103c029ce4393fe94f16d4537fc82",
]
ROUND_TEXT = [
    ("complete three-chamber atlas", "rank-one nilpotent exceptional point", "least projective period"),
    ("projective flow and conserved metrics", "sharp metric boundary", "complex quadratic discriminant"),
    ("independent exact receipt", "hen-o281", "route_a_rejected", SCOPE.lower(), "52 hostile"),
]
EXPECTED = {
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md", "PAPER_IMPROVEMENT_LOG.md",
    "code/README.md", "code/c297_pt_dimer_producer.py", "code/c297_pt_dimer_checker.py", "code/c297_pt_dimer_sympy_crosscheck.py", "code/c297_pt_dimer_replay.py", "code/c297_pt_dimer_mutation.py", "code/c297_release_manifest.py",
    "evaluations/route_a/HCS-C297/2026-09-02.yaml",
    "results/c297_pt_dimer_evidence.json", "results/RESULTS.md", "results/TEST_REPORT.md", "results/HOSTILE_AUDIT.md",
    "paper/README.md", "paper/COMPILE_REPORT.md", "paper/main.tex", "paper/main.pdf", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
}
WARNING_RE = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_json(name: str) -> dict:
    env = dict(os.environ); env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    output = subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)
    return json.loads(output.strip().splitlines()[-1])


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def fonts(path: Path) -> list[str]:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    output = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(output.lower().split())


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c297-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ); env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING_RE.search(log); assert match is None, match.group(0) if match else ""
        rendered = work / "render"
        subprocess.run(["pdftoppm", "-png", "-r", "36", str(work / "main.pdf"), str(rendered)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert len(list(work.glob("render-*.png"))) == pages(work / "main.pdf")
        return (work / "main.pdf").read_bytes()


def main() -> None:
    producer = run_json("c297_pt_dimer_producer.py")
    checker = run_json("c297_pt_dimer_checker.py")
    symbolic = run_json("c297_pt_dimer_sympy_crosscheck.py")
    replay = run_json("c297_pt_dimer_replay.py")
    mutation = run_json("c297_pt_dimer_mutation.py")
    assert producer["status"] == "C297_PRODUCER_PASS"
    assert checker["status"] == "C297_CHECKER_PASS" and checker["assertions"] == 6475
    assert symbolic["status"] == "C297_SYMPY_PASS" and symbolic["checks"] == 516
    assert replay["status"] == "C297_REPLAY_PASS" and replay["paths"] == 2
    assert mutation["status"] == "C297_MUTATION_PASS" and mutation["total_rejections"] == 52

    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C297" and data["obstruction_id"] == OBSTRUCTION
    assert data["source_commit"] == SOURCE and data["fixed_epoch"] == EPOCH and data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"] == {"tuple": ROUTE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(type(value) is bool and value is False for value in data["scope_flags"].values())
    assert data["enumeration"]["phase_counts"] == {"unbroken": 64, "exceptional": 16, "broken": 88}
    assert checker["evaluation_semantic_sha256"] == "fcee5ce61bdedc783e4827d3800d43aadee5d9549a3f092ebfc8b29c62527ea1"

    checker_source = (ROOT / "code/c297_pt_dimer_checker.py").read_text()
    tree = ast.parse(checker_source); imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import): imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom): imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    for token in ("object_pairs_hook=reject_duplicate_keys", "AliasToken", "AnchorToken", "YAML merge keys are forbidden"):
        assert token in checker_source
    mutation_source = (ROOT / "code/c297_pt_dimer_mutation.py").read_text()
    for token in ("obstruction-id", "yaml-obstruction-id", "route-b-int", "boundary-text", "reference-title-int", "reference-ownership-list", "reference-identifier-fake-doi", "reference-url-fake-doi", "nonclaim-scope-escalation"):
        assert token in mutation_source
    for path, tokens in ((ROOT / "THEOREM_PACKAGE.md", ("PROVABLE AS STATED", "HEN-O281", "-4 delta", "The standard", "not a Hilbert--Pólya")), (ROOT / "SOURCE_AUDIT.md", ("10.1103/PhysRevLett.80.5243", "10.1063/1.1418246", "does not mean")), (ROOT / "results/HOSTILE_AUDIT.md", ("52 attacks", "HEN-O281", "False == 0", "fake DOI", "canonical nonclaim", "target Euler factors and root numbers", "forged Hermitian-axis", "sign error", "anchor, alias, merge"))):
        text = " ".join(path.read_text().split())
        for token in tokens: assert token in text, (path, token)

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    assert len(files) == 27
    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES and digest(PDF) == ROUND_HASHES[2] and len(set(ROUND_HASHES)) == 3
    page_counts = [pages(path) for path in ROUND_PATHS]; assert page_counts == [1, 2, 3]
    font_counts = []
    for path, required in zip(ROUND_PATHS, ROUND_TEXT):
        rows = fonts(path); assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows)); text = pdf_text(path)
        for token in required: assert token in text, (path, token)
    assert font_counts == [22, 21, 22]
    fresh_hashes = []
    for round_number, (archive, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first = fresh_build(round_number); second = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        fresh_hashes.append([hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()])
        assert fresh_hashes[-1] == [expected, expected]

    result = {
        "schema": "hcs-c297-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C297", "obstruction_id": OBSTRUCTION,
        "evaluation_date": "2026-09-02", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "exact PT-dimer propagator, projective phase transition, and sharp positive-metric boundary",
        "theorem_status": "PROVABLE AS STATED",
        "build_contract": {"engine": "LuaLaTeX", "passes_per_build": 2, "fresh_builds_per_round": 2, "fixed_epoch": EPOCH, "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes, "round_pdf_pages": page_counts, "round_embedded_subset_font_rows": font_counts, "all_pages_render": True, "final_equals": "paper/main_round2.pdf"},
        "evaluation_contract": {"path": str(EVALUATION.relative_to(ROOT)), "obstruction_id": OBSTRUCTION, "semantic_sha256": checker["evaluation_semantic_sha256"], "duplicate_keys_anchors_aliases_merges_rejected": True},
        "gates": {"G0_source_scope_evaluator": "PASS", "G0a_strict_bool_source_owner_boundary_nonclaim_trees": "PASS", "G1_scalar_square_and_propagator": "PASS", "G2_projective_period_and_fixed_rays": "PASS", "G3_metric_signature_boundary": "PASS", "G4_checker_sympy_replay_mutation": "PASS", "G5_two_substantive_revisions": "PASS", "G6_six_fresh_pdf_builds_fonts_logs_text": "PASS", "G7_manifest_hash_closure": "PASS", "G8_target_arithmetic_operator_route_b": "NOT_CLAIMED"},
        "results": {"grid_cells": 168, "boundary_cells": 8, "phase_counts": data["enumeration"]["phase_counts"], "checker_assertions": checker["assertions"], "symbolic_checks": symbolic["checks"], "hostile_rejections": mutation["total_rejections"], "evidence_json_hostile_rejections": mutation["json_rejections"], "evaluation_yaml_hostile_rejections": mutation["yaml_rejections"], "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "evaluation_semantic_sha256": checker["evaluation_semantic_sha256"], "pdf_sha256": digest(PDF), "pdf_pages": page_counts[-1]},
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C297_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C297_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
