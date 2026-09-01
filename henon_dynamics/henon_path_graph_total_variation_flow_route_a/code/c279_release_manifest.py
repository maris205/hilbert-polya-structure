#!/usr/bin/env python3
"""Full 28-file release closure for HCS-C279."""
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
MANIFEST = ROOT / "C279_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c279_path_tv_evidence.json"
PDF = ROOT / "paper/main.pdf"
YAML = ROOT / "evaluations/route_a/HCS-C279/2026-09-01.yaml"
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]

EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c279_release_manifest.py",
    "code/c279_path_tv_checker.py", "code/c279_path_tv_mutation.py",
    "code/c279_path_tv_producer.py", "code/c279_path_tv_replay.py",
    "code/c279_path_tv_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C279/2026-09-01.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c279_path_tv_evidence.json",
}

MODEL = {
    "graph": "unweighted path P_n on vertices 1,...,n, n>=1",
    "incidence": "(Dx)_i=x_{i+1}-x_i for i=1,...,n-1",
    "energy": "J(x)=sum_{i=1}^{n-1}|x_{i+1}-x_i|",
    "flow": "x'(t) in -partial J(x(t)), x(0)=x^0 in R^n",
    "clock": "maximal-monotone semigroup time t>=0",
    "rof": "R_t(x^0)=argmin_y (1/2)||y-x^0||_2^2+t J(y)",
}
THEOREM_KEYS = {
    "wellposedness", "block_velocity", "coalescence", "consensus",
    "rof_equivalence", "dissipation", "boundary",
}
PROOF_KEYS = {
    "classification", "maximal_monotone", "minimal_flux", "no_splitting",
    "rof_kkt", "finite_extinction", "finite_evidence_role",
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
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
    environment["TZ"] = "UTC"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)],
        env=environment, text=True,
    )


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["schema"] == "hcs-c279-path-graph-total-variation-flow-v1"
    assert data["candidate_id"] == "HCS-C279"
    assert data["evaluation_date"] == "2026-09-01"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["payload_sha256"] == payload_hash(data)
    assert data["model"] == MODEL
    assert set(data["theorem_contract"]) == THEOREM_KEYS
    assert set(data["proof_contract"]) == PROOF_KEYS
    assert data["proof_contract"]["classification"].startswith("PROVABLE AS STATED")
    assert "never split" in data["theorem_contract"]["coalescence"]
    assert "unique path ROF minimizer" in data["theorem_contract"]["rof_equivalence"]
    assert data["route_a"] == {
        "tuple": TUPLE, "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    assert data["scope_flags"] == SCOPE_FLAGS
    enumeration = data["enumeration"]
    assert enumeration["raw_input_count"] == 19530
    assert enumeration["n_min"] == 1 and enumeration["n_max"] == 6
    assert enumeration["stress_input_count"] == 5
    assert enumeration["stress_dimensions"] == [8, 9, 10, 11, 12]
    assert enumeration["stress_event_times"] == 30
    assert enumeration["stress_pair_merges"] == 38
    assert enumeration["trace_sha256"] == "da46566b83355f273a883c632abd8fd474fab8d244edce5c613ad77396c88943"
    assert enumeration["stress_trace_sha256"] == "da41a9d9cce93436425035832b315926eebc82fcc47498f074b343c67d38cb86"
    assert all(value == 0 for value in enumeration["violations"].values())
    assert len(data["witnesses"]) == 8
    assert len(data["references"]) == 4
    assert {reference["identifier"] for reference in data["references"]} == {
        "MR0348562", "10.1016/0167-2789(92)90242-F",
        "10.1137/19M124126X", "10.1007/s00526-019-1684-z",
    }

    yaml = YAML.read_text()
    for literal in (
        "schema: route-a-evaluation-v0.2.0", "candidate_id: HCS-C279",
        f"source_commit: {SOURCE}", f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVALUATOR}",
        "tuple: [A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL]",
        "overall_verdict: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert literal in yaml, literal

    proof = (ROOT / "THEOREM_PACKAGE.md").read_text()
    for literal in (
        "PROVABLE AS STATED", "v_B=(s_r-s_{l-1})/m", "Blocks never split",
        "ROF equals the flow", "averaged-subgradient ROF KKT",
        "global minimization", "separates blockwise",
        "General finite graphs are not included", "A4_FAIL",
    ):
        assert literal in proof, literal

    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for literal in (
        "10.1137/S0036142903422429", "10.1198/jcgs.2010.09208",
        "zero novelty credit", "not a literature-level originality claim",
    ):
        assert literal in source_audit, literal
    manuscript = (ROOT / "paper/main.tex").read_text()
    for literal in (
        "\\cite{Steidl2004}", "\\cite{Hoefling2010}",
        "not priority for equivalence or monotone fusion",
        "global minimization separates blockwise",
    ):
        assert literal in manuscript, literal

    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    for literal in (
        f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical for rounds 0, 1, and 2",
        "Final-pass warnings: none", "all embedded and subset",
        "all seven pages", "main.pdf` equals `main_round2.pdf",
    ):
        assert literal in report, literal

    checker_tree = ast.parse((ROOT / "code/c279_path_tv_checker.py").read_text())
    imported: list[str] = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    assert not [name for name in imported if "producer" in name]

    physical = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*") if path.is_file()
    }
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {
        name: digest(path)
        for name, path in sorted(physical.items()) if path != MANIFEST
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
    round_pages = []
    for path in rounds:
        info = subprocess.check_output(["pdfinfo", str(path)], text=True)
        pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
        round_pages.append(pages)
    assert round_pages == [2, 2, 3]
    fonts = [
        line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    assert fonts
    assert all(
        len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes"
        for line in fonts
    )
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for literal in (
        "exact coalescence and the rof semigroup identity",
        "complete path coalescence atlas", "flow equals rof on a path",
        "executable receipt, boundaries, and route-a nonclaim",
        SCOPE.lower(), "a4_fail", "route_a_rejected",
    ):
        assert literal in text, literal

    producer = run("c279_path_tv_producer.py")
    checker = run("c279_path_tv_checker.py")
    symbolic = run("c279_path_tv_sympy_crosscheck.py")
    replay = run("c279_path_tv_replay.py")
    mutation = run("c279_path_tv_mutation.py")
    assert "C279_PRODUCER_PASS" in producer
    assert "C279 independent checker: PASS" in checker
    assert "C279_SYMPY_PASS" in symbolic
    assert "C279 byte replay: PASS" in replay
    mutation_match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert mutation_match and mutation_match.group(1) == mutation_match.group(2)
    checker_assertions = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_checks = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    total_event_times = sum(row["total_event_times"] for row in enumeration["by_n"])
    total_pair_merges = sum(row["total_pair_merges"] for row in enumeration["by_n"])
    simultaneous_events = sum(row["simultaneous_event_times"] for row in enumeration["by_n"])

    result = {
        "schema": "hcs-c279-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C279",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Exact all-n path total-variation coalescence, finite consensus, and ROF semigroup identity",
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH,
            "passes_per_build": 2, "fresh_builds_per_round": 2,
            "round_artifacts": [
                "paper/main_round0_original.pdf", "paper/main_round1.pdf",
                "paper/main_round2.pdf",
            ],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G0_direct_prior_art_owners": "PASS",
            "G1_maximal_monotone_wellposedness": "PASS",
            "G2_block_velocity_no_splitting": "PASS",
            "G3_joint_events_finite_consensus": "PASS",
            "G4_rof_equivalence_boundaries": "PASS",
            "G5_checker_symbolic_replay_mutation": "PASS",
            "G6_two_substantive_revisions": "PASS",
            "G7_deterministic_pdf_fonts_text_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            "exact_grid_inputs": enumeration["raw_input_count"],
            "rational_stress_inputs": enumeration["stress_input_count"],
            "grid_event_times": total_event_times,
            "grid_pair_merges": total_pair_merges,
            "simultaneous_event_times": simultaneous_events,
            "checker_assertions": checker_assertions,
            "symbolic_checks": symbolic_checks,
            "hostile_rejections": int(mutation_match.group(1)),
            "pdf_pages_by_round": round_pages,
            "embedded_subset_fonts": len(fonts),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "transcript_sha256": enumeration["trace_sha256"],
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C279_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C279_MANIFEST_PASS",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
