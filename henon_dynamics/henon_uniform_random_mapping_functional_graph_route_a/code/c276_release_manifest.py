#!/usr/bin/env python3
"""Full 28-file release closure for HCS-C276."""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C276_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c276_random_mapping_evidence.json"
PDF = ROOT / "paper/main.pdf"
YAML = ROOT / "evaluations/route_a/HCS-C276/2026-09-01.yaml"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
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
    "code/c276_random_mapping_checker.py",
    "code/c276_random_mapping_mutation.py",
    "code/c276_random_mapping_producer.py",
    "code/c276_random_mapping_replay.py",
    "code/c276_random_mapping_sympy_crosscheck.py",
    "code/c276_release_manifest.py",
    "evaluations/route_a/HCS-C276/2026-09-01.yaml",
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
    "results/c276_random_mapping_evidence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run(name: str) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)],
        env=environment,
        text=True,
    )


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["schema"] == "hcs-c276-uniform-random-mapping-v1"
    assert data["candidate_id"] == "HCS-C276"
    assert data["evaluation_date"] == "2026-09-01"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVALUATOR
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == TUPLE
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in data["scope_flags"].values())

    yaml = YAML.read_text()
    for literal in (
        "candidate_id: HCS-C276",
        f"source_commit: {SOURCE}",
        f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVALUATOR}",
        "tuple: [A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL]",
        "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert literal in yaml, literal
    assert "A4_FORMAL_HINT" not in yaml

    proof = (ROOT / "THEOREM_PACKAGE.md").read_text()
    for literal in (
        "PROVABLE AS STATED",
        "Cycle–forest decomposition",
        "Marked-orbit law",
        "One-dimensional limit",
        "Joint limit",
        "The proof owners are the bijection",
    ):
        assert literal in proof, literal

    checker_tree = ast.parse((ROOT / "code/c276_random_mapping_checker.py").read_text())
    imported = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    assert not [name for name in imported if "producer" in name]

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in compile_report
    assert "byte-identical within every round" in compile_report
    assert "Final-pass warnings: none" in compile_report
    for value in round_hashes:
        assert value in compile_report

    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = [
        line
        for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    assert fonts
    assert all(len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes" for line in fonts)
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for literal in (
        "uniform random mapping functional-graph closure",
        "rooted forest",
        "marked orbit",
        "rayleigh",
        "a4_fail",
        "route_a_rejected",
        SCOPE.lower(),
    ):
        assert literal in text, literal

    producer = run("c276_random_mapping_producer.py")
    checker = run("c276_random_mapping_checker.py")
    sympy = run("c276_random_mapping_sympy_crosscheck.py")
    replay = run("c276_random_mapping_replay.py")
    mutation = run("c276_random_mapping_mutation.py")
    assert "C276_PRODUCER_PASS" in producer
    assert "C276 independent checker: PASS" in checker
    assert "C276_SYMPY_PASS" in sympy
    assert "C276 byte replay: PASS" in replay
    match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert match and match.group(1) == match.group(2)
    checker_assertions = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    sympy_checks = int(re.search(r"PASS \((\d+) symbolic", sympy).group(1))
    hostile_rejections = int(match.group(1))
    counts = data["regression"]["counts"]
    formula_cells = (
        counts["cyclic_formula_cells"]
        + counts["collision_survival_cells"]
        + counts["cycle_expectation_formula_cells"]
    )

    result = {
        "schema": "hcs-c276-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C276",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Exact cycle-component, marked-orbit, and square-root limits for uniform random mappings",
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
            "G1_cycle_component_forest_count": "PASS",
            "G2_cyclic_marginal_and_cycle_means": "PASS",
            "G3_marked_tail_cycle_and_distribution_identity": "PASS",
            "G4_rayleigh_and_joint_square_root_limits": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_two_substantive_revisions": "PASS",
            "G7_deterministic_pdf_fonts_log": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "enumerated_sizes": counts["enumerated_sizes"],
            "enumerated_maps": counts["enumerated_maps"],
            "joint_enumeration_cells": counts["joint_enumeration_cells"],
            "tail_cycle_enumeration_cells": counts["tail_cycle_enumeration_cells"],
            "cycle_length_enumeration_cells": counts["cycle_length_enumeration_cells"],
            "formula_atlas_cells": formula_cells,
            "scaling_receipts": counts["cyclic_scaling_receipts"] + counts["joint_scaling_receipts"],
            "checker_assertions": checker_assertions,
            "sympy_checks": sympy_checks,
            "hostile_rejections": hostile_rejections,
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
            "C276_RELEASE_MANIFEST.json",
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
                "status": "C276_MANIFEST_PASS",
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
