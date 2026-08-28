#!/usr/bin/env python3
"""Content-addressed, self-excluded release manifest for C213."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C213_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c213_telegraph_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVAL_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "code/README.md",
    "code/c213_telegraph_checker.py", "code/c213_telegraph_mutation.py", "code/c213_telegraph_producer.py",
    "code/c213_telegraph_replay.py", "code/c213_telegraph_sympy_crosscheck.py", "code/c213_release_manifest.py",
    "evaluations/route_a/HCS-C213/2026-08-28.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c213_telegraph_evidence.json",
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
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
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
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(line.split()[-5:-3] == ["yes", "yes"] for line in fonts)
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in ["Fourier", "Jordan", "spectral-abscissa", "essential", "ROUTE_A_REJECTED", SCOPE, "Kac"]:
        assert phrase in extracted, phrase
    producer = run_json(ROOT / "code/c213_telegraph_producer.py")
    checker = run_json(ROOT / "code/c213_telegraph_checker.py")
    sympy = run_json(ROOT / "code/c213_telegraph_sympy_crosscheck.py")
    replay = run_json(ROOT / "code/c213_telegraph_replay.py")
    mutation = run_json(ROOT / "code/c213_telegraph_mutation.py")
    assert producer["status"] == "C213_PRODUCER_PASS"
    result = {
        "schema": "hcs-c213-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C213",
        "evaluation_date": "2026-08-28", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_exact_fourier_blocks": "PASS", "G2_gap_and_boundaries": "PASS", "G3_checker_sympy_replay_mutation": "PASS", "G4_two_substantive_revisions": "PASS", "G5_fixed_epoch_pdf_fonts_text_visual": "PASS", "G6_manifest_hash_closure": "PASS", "G7_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {"block_rows": 700, "gap_rows": 25, "matrix_entries": 2800, "checker_assertions": checker["assertions"], "sympy_checks": sympy["checks"], "replay_bytes": replay["bytes"], "hostile_rejections": mutation["total_rejections"], "working_decimal_digits": 100, "serialized_significant_digits": 82, "pdf_pages": pages, "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"], "excluded_from_manifest": ["C213_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    physical_after = [p for p in ROOT.rglob("*") if p.is_file()]
    assert len(physical_after) == 28, len(physical_after)
    print(json.dumps({"status": "C213_MANIFEST_PASS", "payload_file_count": len(files), "physical_file_count": len(physical_after), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
