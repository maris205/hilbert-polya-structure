#!/usr/bin/env python3
"""Build the self-excluded, content-addressed HCS-C256 release manifest."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

from hashlib import sha256
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C256_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c256_kdv_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVAL = ROOT / "evaluations/route_a/HCS-C256/2026-08-31.yaml"
SOURCE = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000

EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c256_kdv_checker.py",
    "code/c256_kdv_mutation.py", "code/c256_kdv_producer.py",
    "code/c256_kdv_replay.py", "code/c256_kdv_sympy_crosscheck.py",
    "code/c256_release_manifest.py",
    "evaluations/route_a/HCS-C256/2026-08-31.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf",
    "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md",
    "results/TEST_REPORT.md", "results/c256_kdv_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def is_sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc", ".tmp"} or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts


def run(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C256"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVALUATOR
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in data["scope_flags"].values())

    eval_text = EVAL.read_text()
    for literal in (
        "candidate_id: HCS-C256", f"source_commit: {SOURCE}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR}",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
        "A1_WEAK", "A4_FORMAL_HINT", "cn^2", "Galilean",
        "Bounded classical traveling profiles",
    ):
        assert literal in eval_text, literal

    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in compile_report
    assert "byte-identical" in compile_report
    assert "visual" in compile_report.lower()
    assert "pending" not in compile_report.lower()

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    pages_by_round = []
    for path in rounds:
        info = subprocess.check_output(["pdfinfo", str(path)], text=True)
        pages_by_round.append(int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:"))))
    assert all(2 <= pages <= 6 for pages in pages_by_round)
    pages = pages_by_round[-1]
    font_lines = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert font_lines and all(len(line.split()) >= 7 and line.split()[4] == "yes" and line.split()[5] == "yes" for line in font_lines)
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in ("korteweg", "cnoidal", "soliton", "galilean", "a1_weak", "route_a_rejected", SCOPE.lower(), "no arithmetic"):
        assert phrase in extracted, phrase

    producer = run("c256_kdv_producer.py")
    checker = run("c256_kdv_checker.py")
    sympy = run("c256_kdv_sympy_crosscheck.py")
    replay = run("c256_kdv_replay.py")
    mutation = run("c256_kdv_mutation.py")
    assert "C256_PRODUCER_PASS" in producer
    assert "C256 independent checker: PASS" in checker
    assert "C256_SYMPY_PASS" in sympy
    assert "C256 byte replay: PASS" in replay
    match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert match and match.group(1) == match.group(2) and int(match.group(1)) >= 20
    checker_assertions = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_checks = int(re.search(r"PASS \((\d+) symbolic", sympy).group(1))
    hostile = int(match.group(1))

    result = {
        "schema": "hcs-c256-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C256",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": data["headline"],
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_round": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_root_complete_bounded_profile_classification": "PASS",
            "G2_period_moments_degenerations_galilean_clock": "PASS",
            "G3_checker_sympy_replay_mutation": "PASS",
            "G4_two_substantive_revisions": "PASS",
            "G5_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "periodic_rows": data["receipts"]["periodic_row_count"],
            "boundary_rows": data["receipts"]["soliton_row_count"] + data["receipts"]["harmonic_row_count"] + data["receipts"]["galilean_row_count"],
            "checker_assertions": checker_assertions,
            "sympy_checks": sympy_checks,
            "hostile_rejections": hostile,
            "pdf_pages": pages,
            "round_pdf_pages": pages_by_round,
            "embedded_subset_fonts": len(font_lines),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C256_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C256_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
