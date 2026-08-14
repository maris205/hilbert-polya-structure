#!/usr/bin/env python3
"""Audit SD-C23 artifacts, Route schema, source policy, scope, and provenance."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C23" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc23_successor_divisor.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_CSV_ROWS = {
    "confinement_certificates.csv": 32,
    "determinant_coefficients.csv": 51,
    "graph_controls.csv": 20,
    "primitive_orbit_inventory.csv": 667,
    "quotient_cycle_families.csv": 225,
    "route_gate_summary.csv": 5,
    "trace_class_diagnostics.csv": 56,
    "trace_cutoff_flags.csv": 128,
    "unweighted_trace_primitive.csv": 32,
    "weight_inventory_controls.csv": 64,
    "weighted_trace_ledger.csv": 48,
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
            }:
                found.append(child_path)
            found.extend(forbidden_metadata_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(forbidden_metadata_keys(child, f"{path}[{index}]"))
    return found


def is_git_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    )


def csv_rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    row_counts: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_CSV_ROWS.items():
        path = RESULTS / name
        raw = path.read_bytes()
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        rows = csv_rows(name)
        row_counts[name] = len(rows)
        if len(rows) != expected:
            raise AssertionError(f"{name}: {len(rows)} rows, expected {expected}")

    json_names = sorted(path.name for path in RESULTS.glob("*.json") if path != OUTPUT)
    json_parse: dict[str, bool] = {}
    forbidden_metadata: dict[str, list[str]] = {}
    for name in json_names:
        payload = json.loads((RESULTS / name).read_text(encoding="utf-8"))
        json_parse[name] = True
        keys = forbidden_metadata_keys(payload)
        if keys:
            forbidden_metadata[name] = keys

    route_payload = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))
    route_missing = sorted(REQUIRED_ROUTE_KEYS - set(route_payload))
    source_commit = route_payload.get("source_commit")
    code_commit = route_payload.get("code_commit")
    paired_pending = source_commit == PENDING and code_commit == PENDING
    paired_sealed = source_commit == code_commit and is_git_hash(source_commit)
    source_lock_commit = route_payload.get("source_lock", {}).get("code_commit")
    expected_tuple = [
        "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "A1_WEAK",
        "A2_ANALYTIC_DETERMINANT",
        "A3_FAIL",
        "A4_FAIL",
    ]
    a2_metrics = route_payload.get("a2", {}).get("metrics", {})
    target_fields = (
        "zero_error_train",
        "zero_error_validation",
        "zero_error_test",
        "extra_zero_count",
        "missing_zero_count",
        "root_count_discrepancy",
    )
    artifact_paths = route_payload.get("source_lock", {}).get("artifact_paths", [])
    generated_after_or_by_audit = {
        "results/integrity_audit.json",
        "results/SHA256SUMS.txt",
    }
    missing_artifacts = [
        path
        for path in artifact_paths
        if path not in generated_after_or_by_audit and not (ROOT / path).is_file()
    ]
    route_checks = {
        "yaml_parse": isinstance(route_payload, dict),
        "required_top_level_keys": not route_missing,
        "candidate_id": route_payload.get("candidate_id") == "SD-C23",
        "route_tuple": route_payload.get("route_tuple") == expected_tuple,
        "layer_verdicts": [
            route_payload.get("a0", {}).get("verdict"),
            route_payload.get("a1", {}).get("verdict"),
            route_payload.get("a2", {}).get("verdict"),
            route_payload.get("a3", {}).get("verdict"),
            route_payload.get("a4", {}).get("verdict"),
        ]
        == expected_tuple,
        "overall_rejected": route_payload.get("overall_verdict")
        == "ROUTE_A_REJECTED",
        "route_b_false": route_payload.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_pending or paired_sealed,
        "source_lock_provenance_match": source_lock_commit == code_commit,
        "artifact_paths_exist": not missing_artifacts,
        "target_zero_fields_na": all(
            isinstance(a2_metrics.get(field), str)
            and a2_metrics[field].startswith("not_applicable;")
            for field in target_fields
        ),
        "target_zero_data_false": a2_metrics.get("target_zero_data_used") is False,
        "proves_too_much": route_payload.get("adversarial_controls", {}).get(
            "proves_too_much_risk"
        )
        is True,
    }

    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    oracle = json.loads(
        (RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    cutoff_rows = csv_rows("trace_cutoff_flags.csv")
    determinant_rows = csv_rows("determinant_coefficients.csv")
    unweighted_rows = csv_rows("unweighted_trace_primitive.csv")
    controls = csv_rows("graph_controls.csv")
    spine = next(row for row in controls if row["variant"] == "q_1_2_spine")
    successor = next(row for row in controls if row["variant"] == "successor_only")

    core_source = CORE.read_text(encoding="utf-8")
    tree = ast.parse(core_source)
    imported_modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    call_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    source_checks = {
        "edge_identity": oracle.get("quotient_identity_mismatches") == 0,
        "no_loops": oracle.get("loop_count") == 0,
        "successor_edges_complete": oracle.get("successor_edge_count") == 4095,
        "prime_table_false": oracle.get("prime_table_used") is False,
        "target_feedback_false": oracle.get("target_feedback_used") is False,
        "zero_data_false": oracle.get("riemann_zero_data_used") is False,
        "forbidden_modules_absent": imported_modules.isdisjoint(
            {"sympy", "mpmath", "primesieve"}
        ),
        "forbidden_calls_absent": call_names.isdisjoint(
            {"primepi", "primerange", "zetazero", "sieve_primes"}
        ),
    }
    scientific_checks = {
        "trace_orders_32": summary.get("unweighted_trace_orders") == 32,
        "weighted_orders_16": summary.get("weighted_trace_max_power") == 16,
        "weighted_s_1_2_3": summary.get("weighted_integer_s_values") == [1, 2, 3],
        "primitive_inventory_667": summary.get(
            "primitive_orbit_inventory_through_length_16"
        )
        == 667,
        "cutoff_flags": all(
            (row["exact_infinite_trace"] == "True")
            == (int(row["cutoff"]) >= int(row["certified_cutoff"]))
            for row in cutoff_rows
        ),
        "necklace_exact": all(
            row["rooted_closed_walks"] == row["necklace_reconstruction"]
            for row in unweighted_rows
        ),
        "determinant_cross_method": all(
            row["exact_match"] == "True" for row in determinant_rows
        ),
        "first_trace_zero": summary.get("first_trace_zero") is True,
        "sharp_s1_domain": summary.get("trace_class_iff") == "Re(s)>1/2",
        "spine_zero_margin": (
            spine["all_lengths_2_to_32"] == "True"
            and spine["control_margin_against_full_flood"] == "0"
        ),
        "successor_acyclic": successor["first_positive_length"] == "",
        "route_tuple": summary.get("route_tuple") == expected_tuple,
    }

    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("__pycache__")
    )
    cache_paths.extend(
        sorted(
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob(".pytest_cache")
        )
    )
    result = {
        "cache_clean": not cache_paths,
        "cache_paths": cache_paths,
        "candidate_id": "SD-C23",
        "csv_lf_only": csv_lf_only,
        "csv_row_counts": row_counts,
        "forbidden_runtime_metadata": forbidden_metadata,
        "json_parse": json_parse,
        "missing_artifact_paths": missing_artifacts,
        "provenance_mode": (
            "pending_first_artifact_commit" if paired_pending else "sealed_git_commit"
        ),
        "route_a_missing_keys": route_missing,
        "route_a_schema": route_checks,
        "scientific_artifacts": scientific_checks,
        "scope": {
            "cross_family_experiment_files": [],
            "primary_family": "Symbolic Dynamics",
            "target_zero_data_used": False,
        },
        "second_run_diff_protocol": (
            "entire code/result SHA256 ledger must match on two complete reruns"
        ),
        "source_policy": source_checks,
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
        raise AssertionError(
            "artifact integrity gate failed: " + json.dumps(result, sort_keys=True)
        )
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
