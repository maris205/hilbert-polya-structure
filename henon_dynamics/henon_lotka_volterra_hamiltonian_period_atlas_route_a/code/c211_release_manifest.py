#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C211 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C211_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c211_lv_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

EXPECTED_PAYLOADS = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c211_lv_checker.py", "code/c211_lv_mutation.py",
    "code/c211_lv_producer.py", "code/c211_lv_replay.py",
    "code/c211_lv_sympy_crosscheck.py", "code/c211_release_manifest.py",
    "evaluations/route_a/HCS-C211/2026-08-28.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c211_lv_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def run_text(script: Path) -> str:
    return subprocess.check_output([sys.executable, "-B", str(script)], text=True)


def sidecar(path: Path) -> bool:
    return (path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
            or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["regression"]["quadrature_level_count"] == 24
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)], "build sidecar present"
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED_PAYLOADS, (
        f"payload path mismatch; missing={sorted(EXPECTED_PAYLOADS-set(files))}; "
        f"extra={sorted(set(files)-EXPECTED_PAYLOADS)}"
    )

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert pages >= 2
    font_lines = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert font_lines and all(line.split()[-5:-3] == ["yes", "yes"] for line in font_lines)
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in ["Lambert", "cycle averages", "ROUTE_A_REJECTED", SCOPE, "center-period"]:
        assert phrase in extracted, phrase

    checker = run_text(ROOT / "code/c211_lv_checker.py")
    sympy = run_text(ROOT / "code/c211_lv_sympy_crosscheck.py")
    replay = run_text(ROOT / "code/c211_lv_replay.py")
    mutation = run_text(ROOT / "code/c211_lv_mutation.py")
    assert "732 assertions" in checker
    assert "12 symbolic identities" in sympy
    assert "byte replay: PASS" in replay
    assert "12/12" in mutation
    checker_count = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_count = int(re.search(r"PASS \((\d+) symbolic identities", sympy).group(1))
    hostile_count = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))

    result = {
        "schema": "hcs-c211-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C211",
        "evaluation_date": "2026-08-28", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_strict_convex_hamiltonian_period_annulus": "PASS",
            "G2_lambert_quadrature_action_center_averages": "PASS",
            "G3_checker_heterogeneous_ode_sympy_replay_mutation": "PASS",
            "G4_two_substantive_revisions": "PASS",
            "G5_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_cases": 6, "quadrature_levels": 24, "checker_assertions": checker_count,
            "sympy_checks": sympy_count, "hostile_rejections": hostile_count, "heterogeneous_ode_checks": 24,
            "pdf_pages": pages, "embedded_subset_fonts": len(font_lines),
            "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C211_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    physical_after = [path for path in ROOT.rglob("*") if path.is_file()]
    assert len(physical_after) == 28
    print(json.dumps({"status": "C211_MANIFEST_PASS", "payload_file_count": len(files),
                      "physical_file_count": len(physical_after), "manifest_sha256": digest(MANIFEST),
                      "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
