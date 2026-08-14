#!/usr/bin/env python3
"""Strict integrity, Route-A, source-separation, and hygiene audit for SD-C31."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C31" / "2026-08-14.yaml"
CORE = ROOT / "code" / "counterterm_core.py"
EVALUATOR = ROOT / "code" / "independent_evaluator.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_ROWS = {
    "analysis_comparison_table.csv": 7,
    "baseline_pair_ledger.csv": 76,
    "coefficient_grid_ledger.csv": 49,
    "control_pair_ledger.csv": 47,
    "determinant_power_ledger.csv": 4,
    "raw_counterterm_table.csv": 7,
    "route_gate_summary.csv": 5,
    "scheme_shift_ledger.csv": 15,
}
EXPECTED_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]
REQUIRED_ROUTE_KEYS = {
    "skill",
    "skill_version",
    "candidate_id",
    "source_commit",
    "code_commit",
    "evaluation_date",
    "artifact_path_base",
    "freeze_note",
    "source_lock",
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "adversarial_controls",
    "route_tuple",
    "overall_verdict",
    "claim_boundary",
    "blocking_conditions",
    "next_smallest_test",
    "round2_clues",
    "route_b_invocation_allowed",
}


def csv_rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def paired_provenance(source: object, code: object, lock: object) -> bool:
    values = (source, code, lock)
    if values == (PENDING, PENDING, PENDING):
        return True
    return (
        all(isinstance(value, str) for value in values)
        and source == code == lock
        and re.fullmatch(r"[0-9a-f]{40}", str(source)) is not None
    )


def main() -> int:
    row_counts: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_ROWS.items():
        raw = (RESULTS / name).read_bytes()
        rows = csv_rows(name)
        row_counts[name] = len(rows)
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        if len(rows) != expected:
            raise AssertionError(f"{name}: {len(rows)} != {expected}")

    baseline = json.loads((RESULTS / "baseline_cutoffs.json").read_text(encoding="utf-8"))
    controls = json.loads((RESULTS / "control_ledgers.json").read_text(encoding="utf-8"))
    coefficients = json.loads((RESULTS / "coefficient_search.json").read_text(encoding="utf-8"))
    determinant = json.loads((RESULTS / "determinant_ownership.json").read_text(encoding="utf-8"))
    incidence = json.loads((RESULTS / "incidence_checks.json").read_text(encoding="utf-8"))
    schemes = json.loads((RESULTS / "scheme_shifts.json").read_text(encoding="utf-8"))
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    analysis = json.loads((RESULTS / "analysis.json").read_text(encoding="utf-8"))
    evaluation = json.loads((RESULTS / "evaluation.json").read_text(encoding="utf-8"))
    tests = json.loads((RESULTS / "test_report.json").read_text(encoding="utf-8"))
    double = json.loads((RESULTS / "double_run_certificate.json").read_text(encoding="utf-8"))
    oracle = json.loads((RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8"))
    theorem = json.loads((RESULTS / "theorem_ledger.json").read_text(encoding="utf-8"))
    route = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))

    a2_metrics = route.get("a2", {}).get("metrics", {})
    zero_fields = (
        "zero_error_train",
        "zero_error_validation",
        "zero_error_test",
        "extra_zero_count",
        "missing_zero_count",
        "root_count_discrepancy",
        "cutoff_drift",
        "precision_drift",
        "control_margin",
    )
    route_checks = {
        "required_keys": not (REQUIRED_ROUTE_KEYS - set(route)),
        "candidate": route.get("candidate_id") == "SD-C31",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "tuple": route.get("route_tuple") == EXPECTED_TUPLE,
        "layer_verdicts": [route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")] == EXPECTED_TUPLE,
        "rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_provenance(
            route.get("source_commit"),
            route.get("code_commit"),
            route.get("source_lock", {}).get("code_commit"),
        ),
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "zero_fields_na": all(
            isinstance(a2_metrics.get(field), str)
            and a2_metrics[field].startswith("not_applicable;")
            for field in zero_fields
        ),
        "zero_data_false": a2_metrics.get("target_zero_data_used") is False,
        "regularization_order": route.get("source_lock", {}).get("regularization_order") == 3,
        "main_theorem_u": route.get("source_lock", {}).get("main_theorem_u") == 1,
    }

    tree = ast.parse(CORE.read_text(encoding="utf-8"))
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    evaluator_tree = ast.parse(EVALUATOR.read_text(encoding="utf-8"))
    evaluator_imports = {
        alias.name
        for node in ast.walk(evaluator_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(evaluator_tree)
        if isinstance(node, ast.ImportFrom)
    }
    forbidden_calls = {
        "factorint",
        "isprime",
        "primepi",
        "primerange",
        "sieve",
        "zeta",
        "zetazero",
        "siegelz",
        "mangoldt",
    }
    source_checks = {
        "evaluator_separated": oracle.get("candidate_evaluator_separated") is True
        and "counterterm_core" not in evaluator_imports
        and "generate_results" not in evaluator_imports,
        "forbidden_calls_empty": oracle.get("forbidden_candidate_calls") == [],
        "static_no_oracles": calls.isdisjoint(forbidden_calls),
        "prime_table_false": oracle.get("prime_table_used_in_candidate") is False,
        "zero_data_false": oracle.get("target_zero_data_used") is False,
        "source_cover_compiler": oracle.get("source_cover_compiler") is True,
        "numeric_marks_do_not_select": oracle.get("numeric_marks_select_atoms") is False,
        "det3_frozen": oracle.get("regularization_order") == 3,
        "route_b_false": oracle.get("route_b_invocation_allowed") is False,
    }

    control_counts = {row["name"]: int(row["nonzero_mixed_count"]) for row in controls["controls"]}
    scientific_checks = {
        "baseline_identites": baseline.get("all_diagonal_identities_pass") is True,
        "baseline_mixed": baseline.get("all_baseline_mixed_nonzero") is True,
        "incidence": incidence.get("all_pass") is True,
        "schemes": schemes.get("all_prefix_checks_pass") is True
        and schemes.get("classification", {}).get("finite_parts_distinct") is True,
        "controls": controls.get("all_have_nonzero_mixed_or_b4") is True
        and control_counts == {
            "mutated_cover_promote_6": 3,
            "composite_only": 2,
            "seeded_generic_dag_29031": 4,
            "seeded_random_inventory_29032": 9,
        },
        "coefficient_no_solution": coefficients.get("search", {}).get("solution_count") == 0
        and coefficients.get("search", {}).get("rows_tested") == 49,
        "determinant_ownership": determinant.get("b4_is_generic_pair_gram_ownership") is True
        and "new_scheme_dependent" in determinant.get("renormalized_functional", {}).get("ownership", ""),
        "summary": summary.get("route_tuple") == EXPECTED_TUPLE
        and summary.get("overall_status") == "REJECTED_AS_RH_COMPLETION"
        and all(summary.get("claims", {}).values()),
        "theorem_boundary": theorem.get("finite_part_nonuniqueness") is True
        and theorem.get("local_selectivity_no_go") is True
        and theorem.get("global_nonlocal_no_go_claimed") is False,
        "analysis": analysis.get("status") == "PASS_EXACT_NO_GO_WITHIN_FROZEN_CLASS"
        and analysis.get("route_tuple") == EXPECTED_TUPLE
        and analysis.get("statistics", {}).get("baseline_pair_rows") == 76
        and analysis.get("statistics", {}).get("control_pair_rows") == 47,
        "evaluation": evaluation.get("all_pass") is True
        and evaluation.get("check_count") == evaluation.get("pass_count") == 602,
        "tests": tests.get("all_pass") is True and tests.get("tests_run") == 23,
        "double_run": double.get("byte_identical") is True
        and double.get("first_hashes") == double.get("second_hashes"),
        "no_target_zeros": all(
            payload.get("target_zero_data_used") is False
            for payload in (analysis, evaluation, tests, oracle)
        ),
        "route_b_false": analysis.get("route_b_invocation_allowed") is False
        and evaluation.get("route_b_invocation_allowed") is False
        and tests.get("route_b_invocation_allowed") is False,
    }

    listed_paths = route.get("source_lock", {}).get("artifact_paths", [])
    self_generated = {"results/integrity_audit.json", "results/SHA256SUMS.txt"}
    missing_listed = sorted(
        path for path in listed_paths if path not in self_generated and not (ROOT / path).is_file()
    )
    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache"}
    )
    scanned_suffixes = {".py", ".json", ".csv", ".md", ".yaml", ".tex", ".bib"}
    control_byte_files = []
    crlf_files = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in scanned_suffixes:
            continue
        raw = path.read_bytes()
        if b"\r" in raw:
            crlf_files.append(path.relative_to(ROOT).as_posix())
        if any(byte < 32 and byte not in (9, 10) for byte in raw) or 127 in raw:
            control_byte_files.append(path.relative_to(ROOT).as_posix())

    artifact_checks = {
        "csv_rows": row_counts == EXPECTED_ROWS,
        "csv_lf_only": all(csv_lf_only.values()),
        "listed_paths_exist": not missing_listed,
        "no_caches": not cache_paths,
        "no_crlf": not crlf_files,
        "no_control_bytes": not control_byte_files,
    }
    all_checks = {**route_checks, **source_checks, **scientific_checks, **artifact_checks}
    payload = {
        "candidate_id": "SD-C31",
        "status": "PASS" if all(all_checks.values()) else "FAIL",
        "all_pass": all(all_checks.values()),
        "route_checks": route_checks,
        "source_checks": source_checks,
        "scientific_checks": scientific_checks,
        "artifact_checks": artifact_checks,
        "row_counts": row_counts,
        "csv_lf_only": csv_lf_only,
        "missing_listed_paths": missing_listed,
        "cache_paths": cache_paths,
        "crlf_files": crlf_files,
        "control_byte_files": control_byte_files,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not payload["all_pass"]:
        raise SystemExit(json.dumps(payload, indent=2, sort_keys=True))
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
