#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C261 release manifest."""
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
MANIFEST = ROOT / "C261_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c261_airy_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVAL = ROOT / "evaluations/route_a/HCS-C261/2026-08-31.yaml"
SOURCE = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c261_airy_checker.py", "code/c261_airy_mutation.py", "code/c261_airy_producer.py", "code/c261_airy_replay.py", "code/c261_airy_sympy_crosscheck.py", "code/c261_release_manifest.py",
    "evaluations/route_a/HCS-C261/2026-08-31.yaml", "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c261_airy_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc", ".tmp"} or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts


def run(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C261" and data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH and data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVALUATOR and data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in data["scope_flags"].values())
    eval_text = EVAL.read_text()
    for literal in ("candidate_id: HCS-C261", f"source_commit: {SOURCE}", f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR}", "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false", "A4_NATURAL_QUANTIZATION", "cubic-Talbot"):
        assert literal in eval_text, literal
    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report and "byte-identical" in report and "visual" in report.lower() and "pending" not in report.lower()
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    hashes = [digest(path) for path in rounds]
    assert len(set(hashes)) == 3 and digest(PDF) == hashes[2]
    pages_by_round = []
    for path in rounds:
        info = subprocess.check_output(["pdfinfo", str(path)], text=True)
        pages_by_round.append(int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:"))))
    assert all(2 <= pages <= 6 for pages in pages_by_round)
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(len(line.split()) >= 7 and line.split()[4] == "yes" and line.split()[5] == "yes" for line in fonts)
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in ("airy", "talbot", "fixed space", "noncompact", "a4_natural_quantization", "route_a_rejected", SCOPE.lower(), "no arithmetic"):
        assert phrase in extracted, phrase
    producer, checker = run("c261_airy_producer.py"), run("c261_airy_checker.py")
    sympy, replay, mutation = run("c261_airy_sympy_crosscheck.py"), run("c261_airy_replay.py"), run("c261_airy_mutation.py")
    assert "C261_PRODUCER_PASS" in producer and "C261 independent checker: PASS" in checker
    assert "C261_SYMPY_PASS" in sympy and "C261 byte replay: PASS" in replay
    match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert match and match.group(1) == match.group(2) and int(match.group(1)) >= 20
    checker_assertions = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_checks = int(re.search(r"PASS \((\d+) exact", sympy).group(1))
    result = {
        "schema": "hcs-c261-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C261", "evaluation_date": "2026-08-31", "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE, "headline": data["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_round": 2, "fresh_builds_per_round": 2, "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"], "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_all_time_and_rational_revival_theorem": "PASS", "G2_order_fixed_modes_state_periods": "PASS", "G3_checker_sympy_replay_mutation": "PASS", "G4_two_substantive_revisions": "PASS", "G5_fixed_epoch_pdf_fonts_text_visual": "PASS", "G6_manifest_hash_closure": "PASS", "G7_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {"modular_rows": data["receipts"]["modular_row_count"], "dft_rows": data["receipts"]["dft_row_count"], "support_rows": data["receipts"]["support_row_count"], "checker_assertions": checker_assertions, "sympy_checks": sympy_checks, "hostile_rejections": int(match.group(1)), "pdf_pages": pages_by_round[-1], "round_pdf_pages": pages_by_round, "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": hashes},
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C261_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C261_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
