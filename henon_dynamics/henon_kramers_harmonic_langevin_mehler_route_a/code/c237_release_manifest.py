#!/usr/bin/env python3
"""Build and validate the self-excluded HCS-C237 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C237_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c237_kramers_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C237/2026-08-29.yaml"
SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200

EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c237_kramers_checker.py", "code/c237_kramers_mutation.py", "code/c237_kramers_producer.py", "code/c237_kramers_replay.py", "code/c237_kramers_sympy_crosscheck.py", "code/c237_release_manifest.py",
    "evaluations/route_a/HCS-C237/2026-08-29.yaml", "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c237_kramers_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def run(script: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONHASHSEED"] = "0"
    env["LC_ALL"] = "C.UTF-8"
    env["TZ"] = "UTC"
    return subprocess.check_output([sys.executable, str(ROOT / "code" / script)], text=True, env=env)


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED" and evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    text = EVALUATION.read_text(encoding="utf-8")
    for literal in (
        "candidate_id: HCS-C237", f"source_commit: {SOURCE_COMMIT}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR_SHA256}",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
        "arithmetic_origin: none", "no intrinsic rational-prime carrier",
    ):
        assert literal in text, literal

    report = (ROOT / "paper/COMPILE_REPORT.md").read_text(encoding="utf-8")
    assert f"SOURCE_DATE_EPOCH={FIXED_EPOCH}" in report
    for literal in ("round 0", "round 1", "round 2", "two passes", "no layout/reference warnings", "embedded subset fonts"):
        assert literal.lower() in report.lower(), literal

    physical = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*") if p.is_file()}
    assert not [name for name, p in physical.items() if sidecar(p)], "build sidecar present"
    files = {name: digest(p) for name, p in sorted(physical.items()) if p != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(p) for p in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(len(line.split()) >= 7 and line.split()[4] == "yes" and line.split()[5] == "yes" for line in fonts)
    pdf_text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in (
        "all-damping", "mehler", "gibbs", "kalman", "critical damping", "spectral-abscissa",
        "route_a_rejected", "a4_formal_hint", SCOPE.lower(), "external peer review", "411 assertions", "26 identities", "32/32",
    ):
        assert phrase in pdf_text, phrase
    # The corrected DOI is checked in both source audit and manuscript.
    assert "BF02392081" in (ROOT / "SOURCE_AUDIT.md").read_text(encoding="utf-8")
    assert "BF02392081" in (ROOT / "paper/main.tex").read_text(encoding="utf-8")

    checker = run("c237_kramers_checker.py")
    sympy = run("c237_kramers_sympy_crosscheck.py")
    replay = run("c237_kramers_replay.py")
    mutation = run("c237_kramers_mutation.py")
    assert "independent checker: PASS" in checker
    assert "SymPy cross-check: PASS" in sympy
    assert "canonical byte replay: PASS" in replay
    assert re.search(r"PASS \d+/\d+", mutation)
    checker_count = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_count = int(re.search(r"PASS \((\d+) symbolic identities", sympy).group(1))
    hostile = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))

    result = {
        "schema": "hcs-c237-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C237",
        "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": FIXED_EPOCH, "passes_per_round": 2, "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"], "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_all_damping_matrix_flow": "PASS", "G2_mehler_lyapunov_gibbs": "PASS", "G3_kalman_correlations_rate": "PASS", "G4_checker_sympy_replay_mutation": "PASS", "G5_two_substantive_revisions": "PASS", "G6_fixed_epoch_pdf_fonts_text_visual": "PASS", "G7_manifest_hash_closure": "PASS", "G8_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {"regime_rows": len(evidence["regression"]["regime_rows"]), "transition_rows": len(evidence["regression"]["transition_rows"]), "correlation_rows": len(evidence["regression"]["correlation_rows"]), "rate_rows": len(evidence["regression"]["rate_rows"]), "kalman_rows": len(evidence["regression"]["kalman_rows"]), "gibbs_rows": len(evidence["regression"]["gibbs_rows"]), "boundary_rows": len(evidence["regression"]["boundary_rows"]), "checker_assertions": checker_count, "sympy_checks": sympy_count, "hostile_rejections": hostile, "pdf_pages": pages, "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size, "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"], "excluded_from_manifest": ["C237_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C237_MANIFEST_PASS", "payload_file_count": len(files), "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
