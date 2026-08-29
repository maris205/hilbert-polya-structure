#!/usr/bin/env python3
"""Build and validate the self-excluded HCS-C229 release manifest."""
from __future__ import annotations
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C229_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c229_cir_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C229/2026-08-29.yaml"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c229_cir_checker.py", "code/c229_cir_mutation.py", "code/c229_cir_producer.py", "code/c229_cir_replay.py", "code/c229_cir_sympy_crosscheck.py", "code/c229_release_manifest.py",
    "evaluations/route_a/HCS-C229/2026-08-29.yaml", "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c229_cir_evidence.json",
}


def digest(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def run(script: str) -> str:
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, str(ROOT / "code" / script)], text=True, env=env)


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED" and evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())
    text = EVALUATION.read_text()
    for literal in ("candidate_id: HCS-C229", f"source_commit: {SOURCE_COMMIT}", f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR_SHA256}", "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false", "no arithmetic, target determinant or Hilbert-Polya claim"):
        assert literal in text, literal
    report = (ROOT / "paper/COMPILE_REPORT.md").read_text(); assert f"SOURCE_DATE_EPOCH={FIXED_EPOCH}" in report
    physical = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*") if p.is_file()}
    assert not [name for name, p in physical.items() if sidecar(p)], "build sidecar present"
    files = {name: digest(p) for name, p in sorted(physical.items()) if p != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    hashes = [digest(p) for p in rounds]; assert len(set(hashes)) == 3 and digest(PDF) == hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True); pages = int(next(l.split(":",1)[1] for l in info.splitlines() if l.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(len(l.split()) >= 7 and l.split()[4] == "yes" and l.split()[5] == "yes" for l in fonts)
    pdf_text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in ("all-face affine", "feller", "noncentral", "gamma", "laguerre", "sharp mixing", "235 assertions", "18", "20/20", "route_a_rejected", "a4_formal_hint", SCOPE.lower(), "external peer"):
        assert phrase.lower() in pdf_text, phrase
    checker = run("c229_cir_checker.py"); sympy = run("c229_cir_sympy_crosscheck.py"); replay = run("c229_cir_replay.py"); mutation = run("c229_cir_mutation.py")
    assert "independent checker: PASS" in checker and "SymPy cross-check: PASS" in sympy and "canonical byte replay: PASS" in replay and re.search(r"PASS \d+/\d+", mutation)
    checker_count = int(re.search(r"\((\d+) assertions", checker).group(1)); sympy_count = int(re.search(r"PASS \((\d+) symbolic identities", sympy).group(1)); hostile = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    result = {
        "schema": "hcs-c229-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C229", "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE, "headline": evidence["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": FIXED_EPOCH, "passes_per_round": 2, "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"], "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_feller_boundary_atlas": "PASS", "G2_affine_transform_and_chisquare": "PASS", "G3_gamma_laguerre_gap": "PASS", "G4_checker_sympy_replay_mutation": "PASS", "G5_two_substantive_revisions": "PASS", "G6_fixed_epoch_pdf_fonts_text_visual": "PASS", "G7_manifest_hash_closure": "PASS", "G8_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {"boundary_rows": len(evidence["regression"]["boundary_rows"]), "transform_rows": len(evidence["regression"]["transform_rows"]), "stationary_rows": len(evidence["regression"]["stationary_rows"]), "laguerre_rows": len(evidence["regression"]["laguerre_rows"]), "gap_rows": len(evidence["regression"]["gap_rows"]), "atom_rows": len(evidence["regression"]["atom_rows"]), "checker_assertions": checker_count, "sympy_checks": sympy_count, "hostile_rejections": hostile, "pdf_pages": pages, "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": hashes},
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"], "excluded_from_manifest": ["C229_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C229_MANIFEST_PASS", "payload_file_count": len(files), "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__": main()
