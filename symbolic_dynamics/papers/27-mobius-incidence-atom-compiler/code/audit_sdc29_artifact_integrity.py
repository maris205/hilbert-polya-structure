#!/usr/bin/env python3
"""Audit SD-C29 exact artifacts, route schema, provenance, and hygiene."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C29" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc29_incidence_atom_compiler.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_ROWS = {
    "incidence_inverse_ledger.csv": 4,
    "primitive_idempotent_ledger.csv": 30,
    "pair_relation_ledger.csv": 900,
    "cover_atom_ledger.csv": 256,
    "necklace_ledger.csv": 1016,
    "digit_marker_ledger.csv": 80,
    "power_trace_ledger.csv": 8,
    "fredholm_de_rham_ledger.csv": 4,
    "weighted_hilbert_ledger.csv": 24,
    "bounded_similarity_ledger.csv": 3,
    "source_mutation_controls.csv": 2,
    "stability_equivariance_ledger.csv": 30,
    "ablation_controls.csv": 13,
    "route_gate_summary.csv": 5,
    "analysis_comparison_table.csv": 9,
}
EXPECTED_TUPLE = [
    "A0_ANALYTIC_ARITHMETIC_ORIGIN",
    "A1_PASS_ANALYTIC",
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


def main() -> int:
    row_counts: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_ROWS.items():
        raw = (RESULTS / name).read_bytes()
        data = csv_rows(name)
        row_counts[name] = len(data)
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        if len(data) != expected:
            raise AssertionError(f"{name}: {len(data)} != {expected}")

    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    analysis = json.loads(
        (RESULTS / "analysis_summary.json").read_text(encoding="utf-8")
    )
    tests = json.loads(
        (RESULTS / "test_summary.json").read_text(encoding="utf-8")
    )
    double = json.loads(
        (RESULTS / "double_run_certificate.json").read_text(encoding="utf-8")
    )
    oracle = json.loads(
        (RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    route = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))
    metrics = route.get("a2", {}).get("metrics", {})
    zero_fields = (
        "zero_error_train",
        "zero_error_validation",
        "zero_error_test",
        "extra_zero_count",
        "missing_zero_count",
        "root_count_discrepancy",
    )
    source_commit = route.get("source_commit")
    code_commit = route.get("code_commit")
    lock_commit = route.get("source_lock", {}).get("code_commit")
    commit_values = (source_commit, code_commit, lock_commit)
    paired_provenance = all(value == PENDING for value in commit_values) or (
        source_commit == code_commit == lock_commit
        and isinstance(source_commit, str)
        and len(source_commit) == 40
        and all(character in "0123456789abcdef" for character in source_commit)
    )
    route_checks = {
        "required_keys": not (REQUIRED_ROUTE_KEYS - set(route)),
        "candidate": route.get("candidate_id") == "SD-C29",
        "family": route.get("source_lock", {}).get("family")
        == "symbolic_dynamics",
        "tuple": route.get("route_tuple") == EXPECTED_TUPLE,
        "layer_verdicts": [
            route.get(key, {}).get("verdict")
            for key in ("a0", "a1", "a2", "a3", "a4")
        ]
        == EXPECTED_TUPLE,
        "rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_provenance,
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "zero_fields_na": all(
            isinstance(metrics.get(field), str)
            and metrics[field].startswith("not_applicable;")
            for field in zero_fields
        ),
        "zero_data_false": metrics.get("target_zero_data_used") is False,
    }

    tree = ast.parse(CORE.read_text(encoding="utf-8"))
    calls = {
        (
            node.func.id
            if isinstance(node.func, ast.Name)
            else node.func.attr
        ).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    source_checks = {
        "evaluator_separated": oracle.get("candidate_evaluator_separated") is True,
        "forbidden_calls_empty": oracle.get("forbidden_candidate_calls") == [],
        "static_no_oracles": calls.isdisjoint(
            {
                "factorint",
                "isprime",
                "primepi",
                "primerange",
                "sieve",
                "zeta",
                "zetazero",
                "mangoldt",
            }
        ),
        "prime_table_false": oracle.get("prime_table_used_in_candidate") is False,
        "zero_data_false": oracle.get("riemann_zero_data_used") is False,
        "wordwise": oracle.get("wordwise_not_aggregate_only") is True,
        "marker": oracle.get("digit_marker_retained") is True,
    }

    scientific_keys = [
        "all_incidence_inverse_exact",
        "all_primitive_exact",
        "all_pair_relations_exact",
        "all_cover_atoms_exact",
        "all_necklaces_exact",
        "all_markers_exact",
        "all_power_traces_exact",
        "all_fredholm_de_rham_exact",
        "all_hilbert_formulas_certified",
        "all_bounded_similarity_certified",
        "all_stability_equivariance_exact",
        "mutated_source_proves_too_much",
        "all_ablations_fail_as_expected",
    ]
    scientific_checks = {
        "summary_pass": summary.get("status") == "PASS",
        "summary_claims": all(summary.get(key) is True for key in scientific_keys),
        "summary_tuple": summary.get("route_tuple") == EXPECTED_TUPLE,
        "analysis_pass": analysis.get("status") == "PASS",
        "analysis_tuple": analysis.get("route_tuple") == EXPECTED_TUPLE,
        "tests": tests.get("status") == "PASS"
        and tests.get("passed") == tests.get("collected") == 61,
        "double_run": double.get("byte_identical") is True
        and double.get("first_hashes") == double.get("second_hashes"),
        "no_target_zeros": summary.get("target_zero_data_used") is False
        and analysis.get("target_zero_data_used") is False
        and tests.get("target_zero_data_used") is False,
    }

    listed_paths = route.get("source_lock", {}).get("artifact_paths", [])
    self_generated = {
        "results/integrity_audit.json",
        "results/SHA256SUMS.txt",
    }
    missing_listed = sorted(
        path
        for path in listed_paths
        if path not in self_generated and not (ROOT / path).is_file()
    )
    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache"}
    )
    checks = {
        "row_counts": row_counts == EXPECTED_ROWS,
        "csv_lf": all(csv_lf_only.values()),
        "route": all(route_checks.values()),
        "source": all(source_checks.values()),
        "scientific": all(scientific_checks.values()),
        "listed_artifacts_exist": not missing_listed,
        "no_caches": not cache_paths,
    }
    payload = {
        "candidate_id": "SD-C29",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "row_counts": row_counts,
        "csv_lf_only": csv_lf_only,
        "route_checks": route_checks,
        "source_checks": source_checks,
        "scientific_checks": scientific_checks,
        "missing_listed_artifacts": missing_listed,
        "cache_paths": cache_paths,
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
