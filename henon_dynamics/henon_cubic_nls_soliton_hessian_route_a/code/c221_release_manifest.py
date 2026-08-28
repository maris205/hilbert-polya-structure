#!/usr/bin/env python3
"""Content-addressed, self-excluded release manifest for C221."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C221_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c221_nls_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVAL_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c221_nls_checker.py", "code/c221_nls_mutation.py", "code/c221_nls_producer.py", "code/c221_nls_replay.py", "code/c221_nls_sympy_crosscheck.py", "code/c221_release_manifest.py",
    "evaluations/route_a/HCS-C221/2026-08-28.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c221_nls_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts


def run_json(script: Path) -> dict:
    out = subprocess.check_output([sys.executable, "-B", str(script)], text=True)
    return json.loads(out.strip().splitlines()[-1])


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVAL_SHA
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED" and evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(v is False for v in evidence["scope_flags"].values())

    physical = [p for p in ROOT.rglob("*") if p.is_file()]
    bad = [str(p.relative_to(ROOT)) for p in physical if sidecar(p)]
    assert not bad, f"sidecars present: {bad}"
    files = {str(p.relative_to(ROOT)): digest(p) for p in sorted(physical) if p != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(p) for p in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(x.split(":", 1)[1] for x in info.splitlines() if x.startswith("Pages:")))
    assert 2 <= pages <= 6
    font_lines = [line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:] if line.strip()]
    assert font_lines and all(" yes yes " in (" " + line + " ") for line in font_lines)
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in ["Hessian", "Pöschl", "Teller", "Morse", "VK", "A4_NATURAL_QUANTIZATION", "ROUTE_A_REJECTED", SCOPE, "Weinstein", "Zakharov"]:
        assert phrase in extracted, phrase

    producer = run_json(ROOT / "code/c221_nls_producer.py")
    checker = run_json(ROOT / "code/c221_nls_checker.py")
    sympy = run_json(ROOT / "code/c221_nls_sympy_crosscheck.py")
    replay = run_json(ROOT / "code/c221_nls_replay.py")
    mutation = run_json(ROOT / "code/c221_nls_mutation.py")
    assert producer["status"] == "C221_PRODUCER_PASS" and checker["status"] == "C221_CHECKER_PASS"
    assert sympy["status"] == "C221_SYMPY_PASS" and replay["status"] == "C221_REPLAY_PASS" and mutation["status"] == "C221_MUTATION_PASS"
    result = {
        "schema": "hcs-c221-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C221", "evaluation_date": "2026-08-28", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE, "headline": evidence["headline"],
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_profile_and_variational_identities": "PASS", "G2_hessian_spectrum_factorization_boundaries": "PASS", "G3_checker_sympy_replay_mutation": "PASS", "G4_two_substantive_revisions": "PASS", "G5_fixed_epoch_pdf_fonts_text_visual": "PASS", "G6_manifest_hash_closure": "PASS", "G7_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {"profile_rows": 15, "integral_rows": 3, "spectrum_rows": 15, "factorization_rows": 15, "boundary_rows": 4, "checker_assertions": checker["assertions"], "sympy_checks": sympy["checks"], "replay_bytes": replay["bytes"], "hostile_rejections": mutation["total_rejections"], "working_decimal_digits": 100, "serialized_significant_digits": 82, "pdf_pages": pages, "embedded_subset_fonts": len(font_lines), "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"], "excluded_from_manifest": ["C221_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    physical_after = [p for p in ROOT.rglob("*") if p.is_file()]
    assert len(physical_after) == 28, len(physical_after)
    print(json.dumps({"status": "C221_MANIFEST_PASS", "payload_file_count": len(files), "physical_file_count": len(physical_after), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
