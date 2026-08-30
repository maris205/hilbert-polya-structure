#!/usr/bin/env python3
"""Build the self-excluded, content-addressed C247 release manifest."""
from __future__ import annotations

import json
import os
from hashlib import sha256
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C247_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c247_billiard_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C247/2026-08-30.yaml"
SOURCE = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000

EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c247_billiard_checker.py", "code/c247_billiard_mutation.py",
    "code/c247_billiard_producer.py", "code/c247_billiard_replay.py",
    "code/c247_billiard_sympy_crosscheck.py", "code/c247_release_manifest.py",
    "evaluations/route_a/HCS-C247/2026-08-30.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c247_billiard_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return (path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc", ".tmp"}
            or path.name.endswith(".synctex.gz") or "__pycache__" in path.parts)


def run(script: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script)], text=True, env=env)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["candidate_id"] == "HCS-C247"
    assert evidence["source_commit"] == SOURCE and evidence["fixed_epoch"] == EPOCH
    assert evidence["evaluator"]["sha256"] == EVALUATOR and evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())

    evaluation_text = EVALUATION.read_text()
    for literal in (
        "candidate_id: HCS-C247", f"source_commit: {SOURCE}", f"fixed_epoch: {EPOCH}",
        f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVALUATOR}",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
        "A1_PASS_ANALYTIC", "A4_NATURAL_QUANTIZATION", "target_match",
    ):
        assert literal in evaluation_text, literal

    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report and "pending" not in report.lower()
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)], "build sidecars present"
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    for path, h in zip(rounds, round_hashes):
        assert h in report, f"hash absent from compile report: {path.name}"
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 8, pages
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(len(line.split()) >= 7 and line.split()[4] == "yes" and line.split()[5] == "yes" for line in fonts)
    pdf_text = " ".join(subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower().split())
    for phrase in (
        "circular billiard", "half-chord", "primitive", "caustic", "unipotent",
        "grazing", "dirichlet", "neumann", "a0_fail", "a1_pass_analytic",
        "a2_fail", "route_a_rejected", SCOPE.lower(), "no target",
    ):
        assert phrase in pdf_text, phrase

    producer = run("c247_billiard_producer.py")
    checker = run("c247_billiard_checker.py")
    sympy = run("c247_billiard_sympy_crosscheck.py")
    replay = run("c247_billiard_replay.py")
    mutation = run("c247_billiard_mutation.py")
    assert "C247_PRODUCER_PASS" in producer
    assert "C247 independent checker: PASS" in checker
    assert "C247_SYMPY_PASS" in sympy
    assert "C247 byte replay: PASS" in replay
    match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert match and match.group(1) == match.group(2) and int(match.group(1)) >= 24
    checker_count = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    sympy_count = int(re.search(r"PASS \((\d+) symbolic", sympy).group(1))
    hostile = int(match.group(1))

    result = {
        "schema": "hcs-c247-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C247",
        "evaluation_date": "2026-08-30", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "headline": evidence["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_round": 2,
                           "fresh_builds_per_round": 2,
                           "round_artifacts": [str(path.relative_to(ROOT)) for path in rounds],
                           "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_rigid_map_and_primitive_classification": "PASS",
                  "G2_length_caustic_action_repetition": "PASS", "G3_clean_kernel_and_boundaries": "PASS",
                  "G4_checker_sympy_replay_mutation": "PASS", "G5_two_substantive_revisions": "PASS",
                  "G6_fixed_epoch_pdf_fonts_text_visual": "PASS", "G7_manifest_hash_closure": "PASS",
                  "G8_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {"primitive_rows": evidence["regression"]["primitive_row_count"],
                    "repetition_rows": evidence["regression"]["repetition_row_count"],
                    "boundary_rows": evidence["regression"]["boundary_row_count"],
                    "n_max": evidence["regression"]["n_max"], "checker_assertions": checker_count,
                    "sympy_checks": sympy_count, "hostile_rejections": hostile, "pdf_pages": pages,
                    "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size,
                    "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
                    "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C247_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C247_MANIFEST_PASS", "payload_file_count": 27,
                      "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
                      "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
