#!/usr/bin/env python3
"""Audit SD-C25 artifacts, local-factor firewall, Route schema, and scope."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C25" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc25_unary_fiber.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_CSV_ROWS = {
    "boolean_relation_periodicity.csv": 16,
    "canonical_block_traces.csv": 16,
    "canonical_word_certificates.csv": 4095,
    "composite_witnesses.csv": 11,
    "finite_block_determinants.csv": 12,
    "finite_block_power_traces.csv": 128,
    "finite_semigroup_controls.csv": 11,
    "finite_state_periodicity.csv": 288,
    "nilpotent_memorizer_controls.csv": 56,
    "recurrence_certificates.csv": 48,
    "recurrent_wrapper_controls.csv": 40,
    "roof_marker_mismatch.csv": 4095,
    "route_gate_summary.csv": 5,
    "trace_class_diagnostics.csv": 144,
    "transient_wrapper_structure.csv": 5,
    "transient_wrapper_traces.csv": 40,
}

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


def true(row: dict[str, str], field: str) -> bool:
    return row.get(field) == "True"


def is_git_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    )


def forbidden_metadata_keys(value: object, path: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            if str(key).lower() in {
                "timestamp",
                "elapsed",
                "elapsed_seconds",
                "wall_time",
                "wall_time_seconds",
                "hostname",
                "cwd",
            }:
                found.append(child_path)
            found.extend(forbidden_metadata_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(forbidden_metadata_keys(child, f"{path}[{index}]"))
    return found


def main() -> int:
    row_counts: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_CSV_ROWS.items():
        raw = (RESULTS / name).read_bytes()
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        data = csv_rows(name)
        row_counts[name] = len(data)
        if len(data) != expected:
            raise AssertionError(f"{name}: {len(data)} rows, expected {expected}")

    json_names = sorted(path.name for path in RESULTS.glob("*.json") if path != OUTPUT)
    json_parse: dict[str, bool] = {}
    forbidden_metadata: dict[str, list[str]] = {}
    for name in json_names:
        payload = json.loads((RESULTS / name).read_text(encoding="utf-8"))
        json_parse[name] = True
        forbidden = forbidden_metadata_keys(payload)
        if forbidden:
            forbidden_metadata[name] = forbidden

    route = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))
    route_missing = sorted(REQUIRED_ROUTE_KEYS - set(route))
    expected_tuple = [
        "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "A1_WEAK",
        "A2_ANALYTIC_DETERMINANT",
        "A3_FAIL",
        "A4_FAIL",
    ]
    a2_metrics = route.get("a2", {}).get("metrics", {})
    target_fields = (
        "zero_error_train",
        "zero_error_validation",
        "zero_error_test",
        "extra_zero_count",
        "missing_zero_count",
        "root_count_discrepancy",
    )
    artifact_paths = route.get("source_lock", {}).get("artifact_paths", [])
    future_artifacts = {"results/integrity_audit.json", "results/SHA256SUMS.txt"}
    missing_artifacts = [
        path for path in artifact_paths if path not in future_artifacts and not (ROOT / path).is_file()
    ]
    source_commit = route.get("source_commit")
    code_commit = route.get("code_commit")
    source_lock_commit = route.get("source_lock", {}).get("code_commit")
    paired_pending = source_commit == code_commit == PENDING
    paired_sealed = source_commit == code_commit and is_git_hash(source_commit)
    route_checks = {
        "yaml_parse": isinstance(route, dict),
        "required_top_level_keys": not route_missing,
        "candidate_id": route.get("candidate_id") == "SD-C25",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "route_tuple": route.get("route_tuple") == expected_tuple,
        "layer_verdicts": [route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")]
        == expected_tuple,
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_pending or paired_sealed,
        "source_lock_provenance_match": source_lock_commit == code_commit,
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "artifact_paths_exist": not missing_artifacts,
        "target_zero_fields_na": all(
            isinstance(a2_metrics.get(field), str) and a2_metrics[field].startswith("not_applicable;")
            for field in target_fields
        ),
        "target_zero_data_false": a2_metrics.get("target_zero_data_used") is False,
        "proves_too_much": route.get("adversarial_controls", {}).get("proves_too_much_risk") is True,
        "a4_scoped": "this candidate" in route.get("a4", {}).get("strongest_failure", "").lower(),
    }

    source_text = CORE.read_text(encoding="utf-8")
    source_tree = ast.parse(source_text)
    call_names = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Call) and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    oracle = json.loads((RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8"))
    source_checks = {
        "word_identity": oracle.get("word_mismatches") == 0,
        "edge_identity": oracle.get("edge_mismatches") == 0,
        "holonomy_identity": oracle.get("holonomy_mismatches") == 0,
        "mark_identity": oracle.get("mark_mismatches") == 0,
        "primitive_identity": oracle.get("primitive_mismatches") == 0,
        "candidate_evaluator_separation": oracle.get("candidate_evaluator_separated") is True,
        "no_forbidden_modules": oracle.get("forbidden_modules") == [],
        "no_forbidden_calls": oracle.get("forbidden_calls") == [],
        "constructor_oracle_free": oracle.get("forbidden_constructor_calls") == [],
        "static_call_audit": call_names.isdisjoint(
            {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
        ),
        "prime_table_false": oracle.get("prime_table_used") is False,
        "factorization_oracle_false": oracle.get("factorization_oracle_used") is False,
        "target_feedback_false": oracle.get("target_feedback_used") is False,
        "zero_data_false": oracle.get("riemann_zero_data_used") is False,
    }

    words = csv_rows("canonical_word_certificates.csv")
    finite = csv_rows("finite_state_periodicity.csv")
    relations = csv_rows("boolean_relation_periodicity.csv")
    witnesses = csv_rows("composite_witnesses.csv")
    recurrences = csv_rows("recurrence_certificates.csv")
    memorizers = csv_rows("nilpotent_memorizer_controls.csv")
    canonical = csv_rows("canonical_block_traces.csv")
    block_traces = csv_rows("finite_block_power_traces.csv")
    determinants = csv_rows("finite_block_determinants.csv")
    trace_class = csv_rows("trace_class_diagnostics.csv")
    transient_structure = csv_rows("transient_wrapper_structure.csv")
    transient_traces = csv_rows("transient_wrapper_traces.csv")
    recurrent = csv_rows("recurrent_wrapper_controls.csv")
    roof = csv_rows("roof_marker_mismatch.csv")
    imports = json.loads((RESULTS / "wrapper_import_certificates.json").read_text(encoding="utf-8"))
    tests = json.loads((RESULTS / "test_summary.json").read_text(encoding="utf-8"))
    double_run = json.loads((RESULTS / "double_run_certificate.json").read_text(encoding="utf-8"))
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))

    frozen_2x2 = [row for row in canonical if row["fiber"] == "trace_zero_repetition_leakage"]
    scientific_checks = {
        "canonical_words_exact": all(
            true(row, "all_edges_valid")
            and true(row, "ordered_word_match")
            and true(row, "unique_minimum_mark")
            and true(row, "primitive")
            and row["holonomy"] == "2"
            for row in words
        ),
        "finite_state_periodicity": all(true(row, "eventually_periodic") and row["periodicity_failures"] == "0" for row in finite),
        "million_configuration_census": summary["finite_state"]["transformation_totals"]["configurations"] == 1_054_474,
        "boolean_relation_periodicity": all(true(row, "eventually_periodic") and row["periodicity_failures"] == "0" for row in relations),
        "composite_witnesses": all(
            true(row, "same_residue") and true(row, "same_response") and true(row, "composite_verified")
            for row in witnesses
        ),
        "cayley_hamilton_and_lrs": all(
            true(row, "cayley_hamilton_zero")
            and row["bilinear_nonzero_residuals"] == "0"
            and row["trace_nonzero_residuals"] == "0"
            and true(row, "bilinear_series_match")
            and true(row, "trace_series_match")
            for row in recurrences
        ),
        "nilpotent_memorizer_controls": all(
            true(row, "exact_prefix_fit")
            and true(row, "proves_too_much")
            and row["label"] == "oracle-containing memorizer control"
            for row in memorizers
        ),
        "canonical_cyclic_trace": all(true(row, "cyclic_trace_match") for row in canonical),
        "matrix_local_factor_convention": all(row["local_factor_convention"].startswith("det(I-w_") for row in canonical),
        "trace_zero_2x2_firewall": len(frozen_2x2) == 4
        and all(
            row["local_factor_coefficients_in_w"] == "[1,0,-1]"
            and true(row, "first_trace_zero")
            and row["second_repetition_trace"] == "2"
            and true(row, "trace_zero_repetition_leakage")
            and not true(row, "scalar_trace_is_full_local_factor")
            for row in frozen_2x2
        ),
        "block_period_32": all(max(int(row["power"]) for row in block_traces if row["fiber"] == fiber) == 32 for fiber in {row["fiber"] for row in block_traces}),
        "finite_block_determinants": all(true(row, "match") for row in determinants),
        "trace_intervals_ordered": all(true(row, "interval_ordered") and not true(row, "finite_prefix_is_proof") for row in trace_class),
        "transient_pruning": all(
            true(row, "recurrent_core_exact")
            and not true(row, "computation_edges_on_closed_walk")
            and not true(row, "cemetery_edges_on_closed_walk")
            for row in transient_structure
        ),
        "transient_trace_determinant_match": all(true(row, "trace_match") and true(row, "determinant_coefficient_match") for row in transient_traces),
        "recurrent_clock_marker_firewall": all(
            true(row, "acceptance_independent_padding")
            and true(row, "bound_verified")
            and true(row, "disjoint_basis_witness")
            and true(row, "marker_changed")
            for row in recurrent
        ),
        "paper19_20_imports": imports.get("all_integrity_pass") is True and len(imports.get("imports", [])) == 2,
        "roof_marker_mismatch": all(
            true(row, "edge_monomial_identity")
            and not true(row, "marker_match")
            and not true(row, "roof_match")
            and row["filter_mode"] == "one-dimensional orbit-level oracle control"
            and not true(row, "finite_block_trace_filter")
            for row in roof
        ),
        "test_suite_32": tests.get("status") == "PASS" and tests.get("passed") == tests.get("collected") == 32,
        "double_run_byte_identical": double_run.get("status") == "PASS"
        and double_run.get("byte_identical") is True
        and double_run.get("mismatched_paths") == [],
    }

    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for pattern in ("__pycache__", ".pytest_cache")
        for path in ROOT.rglob(pattern)
    )
    result = {
        "candidate_id": "SD-C25",
        "cache_clean": not cache_paths,
        "cache_paths": cache_paths,
        "csv_lf_only": csv_lf_only,
        "csv_row_counts": row_counts,
        "json_parse": json_parse,
        "forbidden_runtime_metadata": forbidden_metadata,
        "missing_artifact_paths": missing_artifacts,
        "provenance_mode": (
            "pending_first_artifact_commit" if paired_pending else "sealed_git_commit"
        ),
        "route_a_missing_keys": route_missing,
        "route_a_schema": route_checks,
        "scientific_artifacts": scientific_checks,
        "source_policy": source_checks,
        "scope": {
            "primary_family": "Symbolic Dynamics",
            "countable_wrapper_claim": "Paper19/Paper20 licensed architectures only",
            "a4_claim": "this candidate constructs no Route-B mechanism",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
        "target_zero_data_used": False,
    }
    passed = (
        all(csv_lf_only.values())
        and not cache_paths
        and not forbidden_metadata
        and not missing_artifacts
        and not route_missing
        and all(route_checks.values())
        and all(source_checks.values())
        and all(scientific_checks.values())
    )
    result["integrity_pass"] = passed
    if not passed:
        raise AssertionError("artifact integrity gate failed: " + json.dumps(result, sort_keys=True))
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
