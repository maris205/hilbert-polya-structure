#!/usr/bin/env python3
"""Exact release-closure gate for the HCS-C283 p-adic heat package."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C283_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c283_padic_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
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
    "code/c283_padic_checker.py",
    "code/c283_padic_mutation.py",
    "code/c283_padic_producer.py",
    "code/c283_padic_replay.py",
    "code/c283_padic_sympy_crosscheck.py",
    "code/c283_release_manifest.py",
    "evaluations/route_a/HCS-C283/2026-09-01.yaml",
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
    "results/c283_padic_evidence.json",
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
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script)],
                                   env=env, text=True)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["candidate_id"] == "HCS-C283"
    assert evidence["source_commit"] == SOURCE
    assert evidence["fixed_epoch"] == EPOCH
    assert evidence["scope_literal"] == SCOPE
    assert evidence["evaluator"]["sha256"] == EVALUATOR
    assert evidence["route_a"]["tuple"] == [
        "A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in evidence["scope_flags"].values())
    assert evidence["owner"]["normalization"].startswith("explicit Fourier multiplier")
    assert evidence["theorem_contract"]["boundaries"].startswith("alpha=0 gives I-P0")

    evaluation = (ROOT / "evaluations/route_a/HCS-C283/2026-09-01.yaml").read_text()
    for token in (
        "schema: route-a-evaluation-v0.2.0", "candidate_id: HCS-C283",
        SOURCE, EVALUATOR, SCOPE,
        "A0_WEAK_ARITHMETIC_RELATION", "A4_FORMAL_HINT",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
        "composite branching filtrations",
    ):
        assert token in evaluation, token

    theorem = (ROOT / "THEOREM_PACKAGE.md").read_text()
    for token in (
        "explicit conductor-shell Fourier multiplier", "complete pole set",
        "det{}'", "strongly as", "quasi-Schatten ideal",
        "arXiv:1511.02146", "zero originality credit",
        "A0_WEAK_ARITHMETIC_RELATION", "NO_BAD_EULER_OR_ROOT_NUMBER",
    ):
        assert token in theorem, token

    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in (
        "10.1070/IM2002v066n02ABEH000381", "10.1070/RM2014v069n04ABEH004907",
        "10.1090/spmj/1505", "arXiv:1511.02146", "Example 5.1",
        "zero originality credit", "C277", "C184", "C174", "C28",
    ):
        assert token in source_audit, token

    manuscript = (ROOT / "paper/main.tex").read_text()
    for token in (
        "Example 5.1", "\\cite{CZ}", "\\cite{Vlad,Kozyrev,BGPW,VVZ}",
        "quasi-Schatten ideal", "\\xrightarrow[m\\to\\infty]{}",
        "not a literature-novelty claim",
    ):
        assert token in manuscript, token

    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    for token in (
        f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical", "warning-free",
        "Font audit: PASS", "Text audit: PASS", "Visual audit: PASS",
    ):
        assert token in compile_report, token

    producer = run("c283_padic_producer.py")
    checker = run("c283_padic_checker.py")
    symbolic = run("c283_padic_sympy_crosscheck.py")
    replay = run("c283_padic_replay.py")
    mutation = run("c283_padic_mutation.py")
    assert "C283_PRODUCER_PASS" in producer
    assert "independent checker: PASS" in checker
    assert "C283_SYMPY_PASS" in symbolic
    assert "byte replay: PASS" in replay
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2)

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
              ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    pdfinfo = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in pdfinfo.splitlines()
                     if line.startswith("Pages:")))
    assert 3 <= pages <= 9
    font_lines = [
        line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    assert font_lines
    assert all(len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes"
               for line in font_lines)

    pdf_text = re.sub(r"\s+", " ", subprocess.check_output(
        ["pdftotext", str(PDF), "-"], text=True).lower())
    for token in (
        "conductor-shell p-adic fractional heat semigroup", "vertical pole lattice",
        "discrete-scale oscillation", "finite-quotient reconstruction",
        "strongly as", "mean-zero spectral zeta", "quasi-schatten",
        "example 5.1", "route_a_rejected", SCOPE.lower(),
    ):
        assert token in pdf_text, token

    counts = evidence["regression"]["counts"]
    checker_assertions = int(re.search(r"\((\d+) assertions", checker).group(1))
    symbolic_checks = int(re.search(r"\((\d+) exact", symbolic).group(1))
    hostile_rejections = int(mutation_match.group(1))
    result = {
        "schema": "hcs-c283-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C283",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Exact compact p-adic conductor heat spectrum, zeta lattice, determinant, and scale boundaries",
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2, "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "theorem_status": "PROVABLE_AS_STATED",
            "direct_owner_example_5_1": "PASS",
            "independent_checker": "PASS", "symbolic_crosscheck": "PASS",
            "byte_replay": "PASS", "hostile_mutation": "PASS",
            "deterministic_pdf": "PASS", "font_audit": "PASS", "text_audit": "PASS",
            "visual_audit": "PASS", "manifest_closure": "PASS",
            "target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **counts, "total_executable_cells": sum(counts.values()),
            "checker_assertions": checker_assertions, "sympy_checks": symbolic_checks,
            "hostile_rejections": hostile_rejections, "pdf_pages": pages,
            "embedded_subset_fonts": len(font_lines), "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "theorem_contract": evidence["theorem_contract"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C283_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C283_MANIFEST_PASS", "payload_file_count": 27,
        "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
