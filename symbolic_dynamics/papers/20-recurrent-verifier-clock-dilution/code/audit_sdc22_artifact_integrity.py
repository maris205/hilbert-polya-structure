#!/usr/bin/env python3
"""Audit deterministic artifacts, Route schema, source policy, and scope."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C22" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc22_clock_dilution.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_CSV_ROWS = {
    "cutoff_compactness_witnesses.csv": 5,
    "cycle_clock_ledger.csv": 564,
    "marker_firewall.csv": 2,
    "padded_decider_controls.csv": 4,
    "power_trace_certificates.csv": 44,
    "route_gate_summary.csv": 5,
}

REQUIRED_ROUTE_KEYS = {
    "skill",
    "skill_version",
    "candidate_id",
    "source_commit",
    "code_commit",
    "evaluation_date",
    "artifact_path_base",
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


def main() -> int:
    csv_rows: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_CSV_ROWS.items():
        path = RESULTS / name
        raw = path.read_bytes()
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        with path.open(newline="", encoding="utf-8") as handle:
            csv_rows[name] = sum(1 for _ in csv.DictReader(handle))
        if csv_rows[name] != expected:
            raise AssertionError(f"{name}: {csv_rows[name]} rows, expected {expected}")

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
    source_lock_provenance_match = source_lock_commit == code_commit
    expected_tuple = [
        "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "A1_PASS_ANALYTIC",
        "A2_FAIL",
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
        "candidate_id": route_payload.get("candidate_id") == "SD-C22",
        "route_tuple": route_payload.get("route_tuple") == expected_tuple,
        "layer_verdicts": [
            route_payload.get("a0", {}).get("verdict"),
            route_payload.get("a1", {}).get("verdict"),
            route_payload.get("a2", {}).get("verdict"),
            route_payload.get("a3", {}).get("verdict"),
            route_payload.get("a4", {}).get("verdict"),
        ] == expected_tuple,
        "overall_rejected": route_payload.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route_payload.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_pending or paired_sealed,
        "source_lock_provenance_match": source_lock_provenance_match,
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

    oracle = json.loads(
        (RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    core_source = CORE.read_text(encoding="utf-8")
    forbidden_identifiers = (
        "tensor_divides",
        "exists_factor",
        "factor_exists",
        "has_factor",
    )
    source_checks = {
        "certificate_pass": oracle.get("no_oracle_pass") is True,
        "q_states_materialized": oracle.get("q_state_count", 0) > 0,
        "contracted_boundary": oracle.get("contracted_acceptance_boundary") is True,
        "forbidden_tokens_absent": all(
            token not in core_source for token in forbidden_identifiers
        ),
        "formula_convention": summary.get("cycle_formula")
        == "ell(p)=2+sum_{d=2}^{floor(sqrt(p))}ceil(p/d)",
        "max_length_convention": summary.get("max_cycle_length") == 15293,
        "whole_operator_noncompact": summary.get("whole_operator", {}).get("compact")
        is False,
        "z_one_collapse": summary.get("z_one_exact_collapse") is True,
        "marked_firewall": summary.get("small_marked_determinants_differ") is True,
    }

    cache_paths = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("__pycache__"))
    result = {
        "candidate_id": "SD-C22",
        "cache_clean": not cache_paths,
        "cache_paths": cache_paths,
        "csv_lf_only": csv_lf_only,
        "csv_row_counts": csv_rows,
        "forbidden_runtime_metadata": forbidden_metadata,
        "json_parse": json_parse,
        "missing_artifact_paths": missing_artifacts,
        "source_policy": source_checks,
        "provenance_mode": (
            "pending_first_artifact_commit" if paired_pending else "sealed_git_commit"
        ),
        "route_a_schema": route_checks,
        "route_a_missing_keys": route_missing,
        "scope": {
            "primary_family": "Symbolic Dynamics",
            "cross_family_experiment_files": [],
            "target_zero_data_used": False,
        },
        "second_run_diff_protocol": (
            "entire code/result SHA256 ledger must match on two complete reruns"
        ),
        "target_zero_data_used": False,
    }
    passed = (
        all(csv_lf_only.values())
        and not cache_paths
        and not forbidden_metadata
        and all(route_checks.values())
        and all(source_checks.values())
        and not route_missing
        and not missing_artifacts
    )
    result["integrity_pass"] = passed
    if not passed:
        raise AssertionError("artifact integrity gate failed: " + json.dumps(result, sort_keys=True))
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
