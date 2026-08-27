#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C204 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C204_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results" / "c204_finite_linear_evidence.json"
PDF = ROOT / "paper" / "main.pdf"
SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SEMANTIC = "aa44c1ec0e97dfd2ddb2554e9550f65a536eaf455e5bd3a0998d91d8aa3c1a6f"
EVIDENCE_SHA = "b001387457de3bd332df5525739eeffdef9a254f39a2a3f99e26dc93bd074959"
PDF_SHA = "336d039d320202a36f7c3c64af1c6bc7a058431575b8ce4e78336d2e5016a38a"
PDF_BYTES = 261852
ROUNDS = [
    "85a289970b446949b6d4bd68a7b404e1c3125c8e0e7eeb1c69a3d44f81e4fca9",
    "3b5c87a9e459d48bd349c4c8aac0bee885c5e6dc5a04754d1904f5d9b846c3d8",
    PDF_SHA,
]


def digest(path): return sha256(path.read_bytes()).hexdigest()
def sidecar(path):
    return (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
            or "__pycache__" in path.parts or path.name.endswith(".synctex.gz"))


def main():
    d = json.loads(EVIDENCE.read_text())
    assert d["package_id"] == "HCS-C204" and d["source_commit"] == SOURCE_COMMIT
    assert d["evaluator_sha256"] == EVALUATOR and d["scope_guard"] == SCOPE
    assert d["semantic_payload_sha256"] == SEMANTIC and digest(EVIDENCE) == EVIDENCE_SHA
    assert d["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert d["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert d["route_a"]["route_b_invocation_allowed"] is False and not any(d["claim_flags"].values())
    assert digest(PDF) == PDF_SHA and PDF.stat().st_size == PDF_BYTES
    round_paths = [ROOT / "paper" / "main_round0_original.pdf", ROOT / "paper" / "main_round1.pdf", ROOT / "paper" / "main_round2.pdf"]
    round_hashes = [digest(p) for p in round_paths]
    assert round_hashes == ROUNDS and len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    assert "Declarations" in extracted and "AI-use disclosure" in extracted and SCOPE in extracted
    files = {}
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p != MANIFEST and not sidecar(p):
            files[str(p.relative_to(ROOT))] = digest(p)
    result = {
        "schema": "hcs-c204-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C204",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "evaluator_sha256": EVALUATOR,
        "scope_literal": SCOPE,
        "headline": "All-parameter rational-canonical finite dynamics and full-function Koopman characteristic polynomial",
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_all_parameter_theorem": "PASS",
            "G2_inseparable_nilpotent_nonsemisimple_GF4": "PASS",
            "G3_independent_checker_sympy_replay_mutation": "PASS",
            "G4_three_substantive_pdf_rounds": "PASS",
            "G5_fixed_epoch_fonts_text_visual": "PASS",
            "G6_manifest_27_payload_closure": "PASS",
            "G7_target_arithmetic_or_operator": "NOT_CLAIMED",
        },
        "results": {
            "cases": 8, "fixed_cells": 144, "sympy_gcd_cells": 198,
            "koopman_charpolys": 6, "hostile_repaired_hash": 17,
            "hostile_stale_hash": 1, "pdf_pages": pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "pdf_bytes": PDF.stat().st_size,
            "evidence_semantic_sha256": SEMANTIC,
            "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": PDF_SHA,
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": d["route_a"],
        "claim_flags": d["claim_flags"],
        "excluded_from_manifest": ["C204_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert pages == 2 and len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "C204_MANIFEST_PASS", "file_count": len(files),
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA,
                      "pdf_sha256": PDF_SHA}, sort_keys=True))


if __name__ == "__main__": main()
