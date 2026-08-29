#!/usr/bin/env python3
"""Content-addressed, self-excluded release manifest for HCS-C230."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C230_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c230_open_toda_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C230/2026-08-29.yaml"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c230_open_toda_checker.py", "code/c230_open_toda_mutation.py",
    "code/c230_open_toda_producer.py", "code/c230_open_toda_replay.py",
    "code/c230_open_toda_sympy_crosscheck.py", "code/c230_release_manifest.py",
    "evaluations/route_a/HCS-C230/2026-08-29.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c230_open_toda_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts


def run(script: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script)], text=True, env=env)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    evaluation_text = EVALUATION.read_text()
    for literal in (
        "candidate_id: HCS-C230", f"source_commit: {SOURCE_COMMIT}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR_SHA256}",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
        "no arithmetic origin", "no primitive periodic-orbit repetition law",
    ):
        assert literal in evaluation_text, literal
    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={FIXED_EPOCH}" in compile_report

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    bad = [name for name, path in physical.items() if sidecar(path)]
    assert not bad, f"build sidecars present: {bad}"
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    hashes = [digest(path) for path in rounds]
    assert len(set(hashes)) == 3 and digest(PDF) == hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6, pages
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(len(line.split()) >= 7 and line.split()[4] == "yes" and line.split()[5] == "yes" for line in fonts)
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in ("Toda", "Lax", "sorting", "sech", "repeated root", "ROUTE_A_REJECTED", "A4_FORMAL_HINT", SCOPE, "not external peer review"):
        assert phrase.lower() in text.lower(), phrase

    producer = run("c230_open_toda_producer.py")
    checker = run("c230_open_toda_checker.py")
    sympy = run("c230_open_toda_sympy_crosscheck.py")
    replay = run("c230_open_toda_replay.py")
    mutation = run("c230_open_toda_mutation.py")
    assert "C230_PRODUCER_PASS" in producer
    assert "C230_CHECKER_PASS" in checker
    assert "C230_SYMPY_PASS" in sympy
    assert "C230_REPLAY_PASS" in replay
    assert "PASS 22/22" in mutation
    checker_count = int(re.search(r'"assertions":\s*(\d+)', checker).group(1))
    sympy_count = int(re.search(r'"checks":\s*(\d+)', sympy).group(1))
    hostile = 22

    result = {
        "schema": "hcs-c230-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C230",
        "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": FIXED_EPOCH, "passes_per_revision": 2,
                           "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"],
                           "final_equals": "paper/main_round2.pdf"},
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS", "G1_global_hamiltonian_lax": "PASS",
            "G2_simple_spectrum_scattering_norming": "PASS", "G3_checker_sympy_replay_mutation": "PASS",
            "G4_two_substantive_revisions": "PASS", "G5_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G6_manifest_hash_closure": "PASS", "G7_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_count": evidence["summary"]["parameter_count"], "lax_rows": evidence["summary"]["lax_row_count"],
            "n2_exact_rows": evidence["summary"]["n2_exact_row_count"], "scattering_rows": evidence["summary"]["scattering_row_count"],
            "action_angle_rows": evidence["summary"]["action_angle_row_count"], "boundary_rows": evidence["summary"]["boundary_row_count"],
            "checker_assertions": checker_count, "sympy_checks": sympy_count, "hostile_rejections": hostile,
            "pdf_pages": pages, "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF), "round_pdf_sha256": hashes,
        },
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C230_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    physical_after = [path for path in ROOT.rglob("*") if path.is_file()]
    assert len(physical_after) == 28, len(physical_after)
    print(json.dumps({"status": "C230_MANIFEST_PASS", "payload_file_count": len(files),
                      "physical_file_count": len(physical_after), "manifest_sha256": digest(MANIFEST),
                      "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
