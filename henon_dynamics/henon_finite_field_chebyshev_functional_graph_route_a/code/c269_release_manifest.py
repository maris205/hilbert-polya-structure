#!/usr/bin/env python3
"""Full 27-payload plus self-manifest release closure for HCS-C269."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C269_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c269_chebyshev_evidence.json"
PDF = ROOT / "paper/main.pdf"
TEX = ROOT / "paper/main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C269/2026-09-01.yaml"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788134400
TUPLE = [
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_PASS_ANALYTIC",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FORMAL_HINT",
]
ROUND_HASHES = [
    "81b38a2277a4e593a89082ea9a4161d14eeafceea39c3be764b7a33c6ed7432e",
    "cee059de35dfb9e0d98f298a08aee59c780343d5228d6f995c6711cf7835e8eb",
    "c966e31fe276300869a18ff7460952f850b7810e1cc0d4df3481d62da0fd5e0a",
]
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
    "code/c269_chebyshev_checker.py",
    "code/c269_chebyshev_mutation.py",
    "code/c269_chebyshev_producer.py",
    "code/c269_chebyshev_replay.py",
    "code/c269_chebyshev_sympy_crosscheck.py",
    "code/c269_release_manifest.py",
    "evaluations/route_a/HCS-C269/2026-09-01.yaml",
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
    "results/c269_chebyshev_evidence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def is_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_script(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True
    )


def fresh_round2_build() -> bytes:
    env = dict(os.environ)
    env["SOURCE_DATE_EPOCH"] = str(EPOCH)
    with tempfile.TemporaryDirectory(prefix="c269_pdf_") as tmp:
        directory = Path(tmp)
        command = [
            "lualatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-jobname=main",
            rf"\def\CRevisionRound{{2}}\input{{{TEX}}}",
        ]
        for _ in range(2):
            subprocess.run(
                command,
                cwd=directory,
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
                check=True,
            )
        log = (directory / "main.log").read_text(errors="replace")
        forbidden = re.compile(
            r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
            r"undefined references|Rerun to get"
        )
        assert not forbidden.search(log), "settled LuaLaTeX log contains a warning"
        return (directory / "main.pdf").read_bytes()


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C269"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVAL
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == TUPLE
    assert data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in data["scope_flags"].values())

    yaml_text = YAML.read_text()
    for literal in (
        "candidate_id: HCS-C269",
        f"source_commit: {SOURCE}",
        f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVAL}",
        "A0_WEAK_ARITHMETIC_RELATION",
        "A1_PASS_ANALYTIC",
        "A4_FORMAL_HINT",
        "overall_verdict: ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed: false",
    ):
        assert literal in yaml_text, literal

    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report
    assert "byte-identical" in report and "warning-free" in report

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
        sorted(EXPECTED - set(files)),
        sorted(set(files) - EXPECTED),
    )

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_HASHES
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    first_build = fresh_round2_build()
    second_build = fresh_round2_build()
    frozen_pdf = PDF.read_bytes()
    assert first_build == second_build == frozen_pdf

    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert pages == 3
    font_rows = [
        row
        for row in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
        if row.strip() and not row.lstrip().startswith("-")
    ]
    assert font_rows
    assert all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in font_rows)

    pdf_text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in (
        "two cyclic covers and ramified gluing",
        "complete labeled graph and all cycles",
        "tail, image, and koopman jordan atlases",
        "zero jordan blocks",
        "characteristic two",
        "route_a_exploratory",
        "a0_weak_arithmetic_relation",
        "a4_formal_hint",
        SCOPE.lower(),
        "10.1007/s10623-018-0545-7",
        "10.1016/j.disc.2013.10.014",
    ):
        assert phrase in pdf_text, phrase

    producer = run_script("c269_chebyshev_producer.py")
    checker = run_script("c269_chebyshev_checker.py")
    symbolic = run_script("c269_chebyshev_sympy_crosscheck.py")
    replay = run_script("c269_chebyshev_replay.py")
    mutation = run_script("c269_chebyshev_mutation.py")
    assert "C269_PRODUCER_PASS" in producer
    assert "C269 independent checker: PASS" in checker
    assert "C269_SYMPY_PASS" in symbolic
    assert "C269 byte replay: PASS" in replay
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2)
    checker_assertions = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_checks = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    hostile_rejections = int(mutation_match.group(1))
    counts = data["regression"]["counts"]

    result = {
        "schema": "hcs-c269-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C269",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "All-prime-power ramified functional-graph and Koopman classification of finite-field Chebyshev maps",
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_build": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": [
                "paper/main_round0_original.pdf",
                "paper/main_round1.pdf",
                "paper/main_round2.pdf",
            ],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G1_all_prime_power_field_models": "PASS",
            "G2_inversion_quotient_branch_gluing": "PASS",
            "G3_fixed_primitive_zeta": "PASS",
            "G4_tail_image_tree_atlas": "PASS",
            "G5_koopman_zero_jordan_characteristic": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_two_substantive_revisions": "PASS",
            "G8_deterministic_pdf_fonts_log": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **counts,
            "checker_assertions": checker_assertions,
            "sympy_checks": symbolic_checks,
            "hostile_rejections": hostile_rejections,
            "pdf_pages": pages,
            "embedded_subset_fonts": len(font_rows),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C269_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(
        json.dumps(
            {
                "status": "C269_MANIFEST_PASS",
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
