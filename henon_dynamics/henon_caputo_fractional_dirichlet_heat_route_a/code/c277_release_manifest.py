#!/usr/bin/env python3
"""Release-closure gate for the HCS-C277 Caputo heat package."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C277_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c277_caputo_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800

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
    "code/c277_caputo_checker.py",
    "code/c277_caputo_mutation.py",
    "code/c277_caputo_producer.py",
    "code/c277_caputo_replay.py",
    "code/c277_caputo_sympy_crosscheck.py",
    "code/c277_release_manifest.py",
    "evaluations/route_a/HCS-C277/2026-09-01.yaml",
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
    "results/c277_caputo_evidence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run(script: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script)], env=env, text=True
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["candidate_id"] == "HCS-C277"
    assert evidence["source_commit"] == SOURCE
    assert evidence["fixed_epoch"] == EPOCH
    assert evidence["scope_literal"] == SCOPE
    assert evidence["evaluator"]["sha256"] == EVALUATOR
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert not evidence["route_a"]["route_b_invocation_allowed"]
    assert all(value is False for value in evidence["scope_flags"].values())
    assert evidence["theorem_contract"]["sharp_smoothing"] == (
        "for beta<1, t>0, and theta>=0, A^theta*S_beta(t) is bounded iff theta<=1"
    )
    assert evidence["theorem_contract"]["negative_theta_context"] == (
        "theta<0 also gives a bounded operator because A>=I, but it is outside "
        "the declared theta>=0 smoothing domain"
    )

    evaluation = (ROOT / "evaluations/route_a/HCS-C277/2026-09-01.yaml").read_text()
    for token in (
        "candidate_id: HCS-C277",
        SOURCE,
        EVALUATOR,
        SCOPE,
        "A0_FAIL",
        "A4_FORMAL_HINT",
        "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert token in evaluation, token

    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report
    assert "byte-identical" in report
    assert "warning-free" in report
    assert "22 fonts" in report

    producer = run("c277_caputo_producer.py")
    checker = run("c277_caputo_checker.py")
    symbolic = run("c277_caputo_sympy_crosscheck.py")
    replay = run("c277_caputo_replay.py")
    mutation = run("c277_caputo_mutation.py")
    assert "C277_PRODUCER_PASS" in producer
    assert "independent checker: PASS" in checker
    assert "C277_SYMPY_PASS" in symbolic
    assert "byte replay: PASS" in replay
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2)

    physical = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {
        name: digest(path)
        for name, path in sorted(physical.items())
        if path != MANIFEST
    }
    assert set(files) == EXPECTED, (
        sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED)
    )

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    pdfinfo = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in pdfinfo.splitlines()
                     if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    font_lines = [
        line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    assert font_lines
    assert all(
        len(line.split()) >= 7
        and line.split()[-5] == "yes"
        and line.split()[-4] == "yes"
        for line in font_lines
    )

    pdf_text = re.sub(
        r"\s+", " ",
        subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower(),
    )
    for token in (
        "caputo dirichlet heat flow",
        "sharp memory theorem",
        "operator-norm resolvent limit",
        "declared domain",
        "schatten",
        "route_a_rejected",
        SCOPE.lower(),
    ):
        assert token in pdf_text, token

    counts = evidence["regression"]["counts"]
    checker_assertions = int(re.search(r"\((\d+) assertions", checker).group(1))
    symbolic_checks = int(re.search(r"\((\d+) symbolic", symbolic).group(1))
    hostile_rejections = int(mutation_match.group(1))
    result = {
        "schema": "hcs-c277-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C277",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": (
            "Exact Caputo spectral flow, sharp two-derivative and Schatten "
            "thresholds, and an operator-norm resolvent limit"
        ),
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "theorem_status": "PROVABLE_AS_STATED",
            "independent_checker": "PASS",
            "symbolic_crosscheck": "PASS",
            "byte_replay": "PASS",
            "hostile_mutation": "PASS",
            "deterministic_pdf": "PASS",
            "manifest_closure": "PASS",
            "target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **counts,
            "total_executable_cells": sum(counts.values()),
            "checker_assertions": checker_assertions,
            "sympy_checks": symbolic_checks,
            "hostile_rejections": hostile_rejections,
            "pdf_pages": pages,
            "embedded_subset_fonts": len(font_lines),
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "theorem_contract": evidence["theorem_contract"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C277_RELEASE_MANIFEST.json",
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
    print(json.dumps({
        "status": "C277_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
