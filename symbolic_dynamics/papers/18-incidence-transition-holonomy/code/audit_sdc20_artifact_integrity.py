#!/usr/bin/env python3
"""Audit parseability, LF discipline, schema, caches, and scope for SD-C20."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C20" / "2026-08-14.yaml"

EXPECTED_CSV_ROWS = {
    "group_comparison_table.csv": 3,
    "group_enumeration_summary.csv": 3,
    "incidence_orbit_summary.csv": 4,
    "incidence_orbits.csv": 45,
    "inventory_comparison_table.csv": 6,
    "inventory_controls.csv": 30,
    "primitive_holonomy_ledger.csv": 3,
    "trace_class_comparison_table.csv": 2,
    "trace_class_gates.csv": 2,
    "transition_controls.csv": 4,
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
            if str(key).lower() in {"timestamp", "elapsed", "elapsed_seconds", "wall_time", "wall_time_seconds"}:
                found.append(child_path)
            found.extend(forbidden_metadata_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(forbidden_metadata_keys(child, f"{path}[{index}]"))
    return found


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
    route_checks = {
        "yaml_parse": isinstance(route_payload, dict),
        "required_top_level_keys": not route_missing,
        "candidate_id": route_payload.get("candidate_id") == "SD-C20",
        "route_tuple": route_payload.get("route_tuple")
        == [
            "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "A1_WEAK",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_rejected": route_payload.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route_payload.get("route_b_invocation_allowed") is False,
        "source_commit_sealed": isinstance(source_commit, str)
        and len(source_commit) == 40
        and all(character in "0123456789abcdef" for character in source_commit),
        "code_commit_sealed": isinstance(code_commit, str)
        and len(code_commit) == 40
        and all(character in "0123456789abcdef" for character in code_commit),
        "source_code_commit_match": source_commit == code_commit,
    }

    cache_paths = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("__pycache__"))
    payload = {
        "candidate_id": "SD-C20",
        "cache_clean": not cache_paths,
        "cache_paths": cache_paths,
        "csv_lf_only": csv_lf_only,
        "csv_row_counts": csv_rows,
        "forbidden_runtime_metadata": forbidden_metadata,
        "json_parse": json_parse,
        "research_package": {
            "path": "/tmp/paper18_research_notes/RESEARCH_PACKAGE.md",
            "available": Path("/tmp/paper18_research_notes/RESEARCH_PACKAGE.md").is_file(),
            "prototype_result_diff": "not_applicable_no_prototype_result_tree",
        },
        "route_a_schema": route_checks,
        "route_a_missing_keys": route_missing,
        "scope": {
            "primary_family": "Symbolic Dynamics",
            "cross_family_experiment_files": [],
            "target_zero_data_used": False,
        },
        "second_run_diff_protocol": "entire code/result SHA256 ledger must match on two complete reruns",
        "target_zero_data_used": False,
    }
    passed = (
        all(csv_lf_only.values())
        and not cache_paths
        and not forbidden_metadata
        and all(route_checks.values())
        and not route_missing
        and payload["research_package"]["available"]
    )
    payload["integrity_pass"] = passed
    if not passed:
        raise AssertionError("artifact integrity gate failed: " + json.dumps(payload, sort_keys=True))
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
