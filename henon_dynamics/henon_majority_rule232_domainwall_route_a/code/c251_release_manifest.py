#!/usr/bin/env python3
"""Run C251 release gates and write the self-excluded manifest."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C251_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c251_majority_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C251/2026-08-30.yaml"
SOURCE_COMMIT = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000

EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c251_release_manifest.py", "code/c251_majority_checker.py",
    "code/c251_majority_mutation.py", "code/c251_majority_producer.py", "code/c251_majority_replay.py",
    "code/c251_majority_sympy_crosscheck.py", "evaluations/route_a/HCS-C251/2026-08-30.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c251_majority_evidence.json",
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
    assert evidence["fixed_epoch"] == FIXED_EPOCH
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED" and evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    evaluation_text = EVALUATION.read_text()
    for literal in (
        "candidate_id: HCS-C251", "evaluation_date: 2026-08-30", f"fixed_epoch: {FIXED_EPOCH}",
        f"source_commit: {SOURCE_COMMIT}", f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVALUATOR_SHA256}", "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false", "A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT", SCOPE,
    ):
        assert literal in evaluation_text, literal

    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={FIXED_EPOCH}" in compile_report and "pending" not in compile_report.lower()
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)], "build sidecar present"
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    font_lines = [line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:] if line.strip()]
    assert font_lines and all("yes" in line.split() and line.split().count("yes") >= 2 for line in font_lines)
    pdf_text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in ("majority", "domain-wall", "erosion", "fixed counts", "a1_pass_analytic", "a2_fail", "route_a_rejected", SCOPE.lower(), "alternating", "transient"):
        assert phrase in pdf_text, phrase

    checker = run("c251_majority_checker.py")
    sympy = run("c251_majority_sympy_crosscheck.py")
    replay = run("c251_majority_replay.py")
    mutation = run("c251_majority_mutation.py")
    assert "independent checker: PASS" in checker
    assert "symbolic identities" in sympy
    assert "byte replay: PASS" in replay
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2) and int(mutation_match.group(1)) >= 24
    checker_count = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_count = int(re.search(r"PASS \((\d+) symbolic identities", sympy).group(1))
    hostile = int(mutation_match.group(1))

    result = {
        "schema": "hcs-c251-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C251",
        "evaluation_date": "2026-08-30", "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": FIXED_EPOCH, "passes_per_round": 2, "fresh_builds_per_round": 2, "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"], "final_equals": "paper/main_round2.pdf"},
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS", "G1_wall_erosion_periodic_classification": "PASS",
            "G2_fixed_count_transfer": "PASS", "G3_transient_parity_transfer": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS", "G5_two_substantive_revisions": "PASS",
            "G6_fixed_epoch_pdf_fonts_text_visual": "PASS", "G7_manifest_hash_closure": "PASS",
            "G8_target_orbit_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "fixed_formula_rows": len(evidence["regression"]["fixed_formula_rows"]), "wall_run_rows": len(evidence["regression"]["wall_run_rows"]),
            "finite_state_rows": len(evidence["regression"]["finite_state_rows"]), "sample_trajectories": len(evidence["regression"]["sample_trajectories"]),
            "checker_assertions": checker_count, "sympy_checks": sympy_count, "hostile_rejections": hostile, "pdf_pages": pages,
            "embedded_subset_fonts": len(font_lines), "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C251_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C251_MANIFEST_PASS", "payload_file_count": len(files), "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
