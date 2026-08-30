#!/usr/bin/env python3
"""Validate and write the self-excluded C239 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C239_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c239_shuffle_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C239/2026-08-30.yaml"
SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c239_shuffle_checker.py", "code/c239_shuffle_mutation.py",
    "code/c239_shuffle_producer.py", "code/c239_shuffle_replay.py", "code/c239_shuffle_sympy_crosscheck.py",
    "code/c239_release_manifest.py", "evaluations/route_a/HCS-C239/2026-08-30.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c239_shuffle_evidence.json",
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
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script)], text=True, env=env)


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc", ".tmp"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED" and evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    evaluation_text = EVALUATION.read_text()
    for literal in (
        "candidate_id: HCS-C239", f"source_commit: {SOURCE_COMMIT}", f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVALUATOR_SHA256}", "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false", "A1_PASS_ANALYTIC", "EllisFanShallit2002",
        "10.46298/dmtcs.308", "Packard1994", "10.1080/00150517.1994.12429237", SCOPE,
    ):
        assert literal in evaluation_text, literal

    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={FIXED_EPOCH}" in compile_report and "pending" not in compile_report.lower()
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)], "build sidecar present"
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-set(EXPECTED))}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    hashes = [digest(path) for path in rounds]
    assert len(set(hashes)) == 3 and digest(PDF) == hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(len(line.split()) >= 7 and line.split()[4] == "yes" and line.split()[5] == "yes" for line in fonts)
    pdf_text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in ("perfect shuffle", "gcd", "möbius", "koopman", "a1_pass_analytic", "a2_fail", "route_a_rejected", SCOPE.lower(), "primitive"):
        assert phrase in pdf_text, phrase

    checker = run("c239_shuffle_checker.py")
    sympy = run("c239_shuffle_sympy_crosscheck.py")
    replay = run("c239_shuffle_replay.py")
    mutation = run("c239_shuffle_mutation.py")
    assert "independent checker: PASS" in checker
    assert "symbolic identities" in sympy
    assert "byte replay: PASS" in replay
    assert re.search(r"PASS \d+/\d+", mutation)
    checker_count = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_count = int(re.search(r"PASS \((\d+) symbolic identities", sympy).group(1))
    hostile = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))

    result = {
        "schema": "hcs-c239-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C239",
        "evaluation_date": "2026-08-30", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": FIXED_EPOCH, "passes_per_round": 2, "fresh_builds_per_round": 2, "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"], "final_equals": "paper/main_round2.pdf"},
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS", "G1_fixed_gcd_order_formula": "PASS",
            "G2_mobius_primitive_cycle_atlas": "PASS", "G3_packet_interleave_independence": "PASS",
            "G4_zeta_koopman_factorization": "PASS", "G5_checker_sympy_replay_mutation": "PASS",
            "G6_two_substantive_revisions": "PASS", "G7_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G8_manifest_hash_closure": "PASS", "G9_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "atlas_rows": len(evidence["regression"]["atlas_rows"]), "position_rows": len(evidence["regression"]["position_rows"]),
            "packet_interleave_checks": evidence["regression"]["row_counts"]["packet_interleave_checks"],
            "spectral_rows": len(evidence["regression"]["spectral_rows"]), "checker_assertions": checker_count,
            "sympy_checks": sympy_count, "hostile_rejections": hostile, "pdf_pages": pages,
            "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF), "round_pdf_sha256": hashes,
        },
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C239_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C239_MANIFEST_PASS", "payload_file_count": len(files), "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
