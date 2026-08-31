#!/usr/bin/env python3
"""Content-addressed release gate for HCS-C265."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C265_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c265_hawkes_evidence.json"
PDF = ROOT / "paper/main.pdf"
YAML = ROOT / "evaluations/route_a/HCS-C265/2026-08-31.yaml"
SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
EXPECTED = {
    "EXPERIMENT_PLAN.md",
    "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md",
    "README.md",
    "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md",
    "code/README.md",
    "code/c265_hawkes_checker.py",
    "code/c265_hawkes_mutation.py",
    "code/c265_hawkes_producer.py",
    "code/c265_hawkes_replay.py",
    "code/c265_hawkes_sympy_crosscheck.py",
    "code/c265_release_manifest.py",
    "evaluations/route_a/HCS-C265/2026-08-31.yaml",
    "paper/COMPILE_REPORT.md",
    "paper/README.md",
    "paper/main.pdf",
    "paper/main.tex",
    "paper/main_round0_original.pdf",
    "paper/main_round1.pdf",
    "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    "results/c265_hawkes_evidence.json",
}
EXPECTED_TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def is_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def run(script: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script)], env=env, text=True
    )


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C265"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVAL
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == EXPECTED_TUPLE
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in data["scope_flags"].values())

    evaluation = YAML.read_text()
    for literal in (
        "candidate_id: HCS-C265",
        f"source_commit: {SOURCE}",
        f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVAL}",
        "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
        "A0_FAIL",
        "A4_FORMAL_HINT",
        "exponential univariate Hawkes",
    ):
        assert literal in evaluation, literal

    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report
    assert "byte-identical" in report
    assert "no LaTeX/package warnings" in report

    physical = {
        str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()
    }
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {
        name: digest(path)
        for name, path in sorted(physical.items())
        if path != MANIFEST
    }
    assert set(files) == EXPECTED, (
        f"payload mismatch missing={sorted(EXPECTED-set(files))} "
        f"extra={sorted(set(files)-EXPECTED)}"
    )

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(
        next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:"))
    )
    assert 2 <= pages <= 6
    font_lines = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    fonts = [line for line in font_lines if line.strip() and not line.lstrip().startswith("-")]
    assert fonts
    assert all(
        len(line.split()) >= 7
        and line.split()[-5] == "yes"
        and line.split()[-4] == "yes"
        for line in fonts
    )
    pdf_text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in (
        "joint affine transform",
        "dirac atom",
        "bartlett spectrum",
        "borel genealogy",
        "a4_formal_hint",
        "route_a_rejected",
        SCOPE.lower(),
        "10.1093/biomet/58.1.83",
    ):
        assert phrase in pdf_text, phrase

    producer = run("c265_hawkes_producer.py")
    checker = run("c265_hawkes_checker.py")
    symbolic = run("c265_hawkes_sympy_crosscheck.py")
    replay = run("c265_hawkes_replay.py")
    mutation = run("c265_hawkes_mutation.py")
    assert "C265_PRODUCER_PASS" in producer
    assert "C265 independent checker: PASS" in checker
    assert "C265_SYMPY_PASS" in symbolic
    assert "C265 byte replay: PASS" in replay
    hostile_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert hostile_match and hostile_match.group(1) == hostile_match.group(2)
    checker_count = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_count = int(re.search(r"PASS \((\d+) exact symbolic", symbolic).group(1))
    hostile_count = int(hostile_match.group(1))
    regression = data["regression"]
    stable_cases = regression["stable_cases"]
    moment_cells = sum(len(row["moments_m0_to_m10"]) for row in stable_cases)
    window_cells = sum(
        len(row["window_variance_maclaurin_T1_to_T10"]) for row in stable_cases
    )
    assert moment_cells == 3520
    assert window_cells == 3200

    result = {
        "schema": "hcs-c265-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C265",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": data["headline"],
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_round": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": [
                "paper/main_round0_original.pdf",
                "paper/main_round1.pdf",
                "paper/main_round2.pdf",
            ],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_joint_affine_transform": "PASS",
            "G2_stationary_laplace_and_all_moments": "PASS",
            "G3_three_covariances_and_bartlett_convention": "PASS",
            "G4_window_variance_borel_and_boundaries": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_two_substantive_revisions": "PASS",
            "G7_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "stable_cases": regression["stable_case_count"],
            "moment_cells": moment_cells,
            "window_cells": window_cells,
            "cluster_rows": regression["cluster_row_count"],
            "boundary_rows": regression["boundary_row_count"],
            "checker_assertions": checker_count,
            "sympy_checks": symbolic_count,
            "hostile_rejections": hostile_count,
            "pdf_pages": pages,
            "embedded_subset_fonts": len(fonts),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C265_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(
        json.dumps(
            {
                "status": "C265_MANIFEST_PASS",
                "payload_file_count": 27,
                "physical_file_count": 28,
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(EVIDENCE),
                "pdf_sha256": digest(PDF),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
