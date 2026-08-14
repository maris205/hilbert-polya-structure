#!/usr/bin/env python3
"""Audit SD-C30 artifacts, route schema, provenance, and text hygiene."""

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
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C30" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc30_chiral_incidence.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_ROWS = {
    "source_compiler_ledger.csv": 4,
    "native_gram_ledger.csv": 43,
    "infinite_gram_formula_ledger.csv": 9,
    "schatten_strip_ledger.csv": 8,
    "finite_b2_diagnostic.csv": 4,
    "infinite_s2_firewall.csv": 4,
    "b4_frequency_ledger.csv": 7,
    "det3_deletion_ledger.csv": 8,
    "metric_rigidity_ledger.csv": 8,
    "orthogonalized_det3_ledger.csv": 4,
    "adversary_control_ledger.csv": 4,
    "marker_ownership_ledger.csv": 24,
    "t_sample_ledger.csv": 12,
    "route_gate_summary.csv": 5,
    "analysis_comparison_table.csv": 10,
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


def paired_provenance(source: object, code: object, lock: object) -> bool:
    """Accept the first-stage placeholder or one sealed lowercase commit."""
    values = (source, code, lock)
    if values == (PENDING, PENDING, PENDING):
        return True
    return (
        all(isinstance(value, str) for value in values)
        and source == code == lock
        and re.fullmatch(r"[0-9a-f]{40}", source) is not None
    )


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
    tests = json.loads((RESULTS / "test_summary.json").read_text(encoding="utf-8"))
    double = json.loads(
        (RESULTS / "double_run_certificate.json").read_text(encoding="utf-8")
    )
    oracle = json.loads(
        (RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8")
    )
    route = yaml.safe_load(ROUTE_A.read_text(encoding="utf-8"))
    a2_metrics = route.get("a2", {}).get("metrics", {})
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
    route_checks = {
        "required_keys": not (REQUIRED_ROUTE_KEYS - set(route)),
        "candidate": route.get("candidate_id") == "SD-C30",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "tuple": route.get("route_tuple") == EXPECTED_TUPLE,
        "layer_verdicts": [
            route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")
        ]
        == EXPECTED_TUPLE,
        "rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_provenance(
            source_commit, code_commit, lock_commit
        ),
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "zero_fields_na": all(
            isinstance(a2_metrics.get(field), str)
            and a2_metrics[field].startswith("not_applicable;")
            for field in zero_fields
        ),
        "zero_data_false": a2_metrics.get("target_zero_data_used") is False,
        "marker_u1": route.get("source_lock", {}).get("main_theorem_u") == 1,
        "det3_order": route.get("source_lock", {}).get("regularization_order") == 3,
    }

    tree = ast.parse(CORE.read_text(encoding="utf-8"))
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
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
                "siegelz",
                "mangoldt",
            }
        ),
        "prime_table_false": oracle.get("prime_table_used_in_candidate") is False,
        "zero_data_false": oracle.get("target_zero_data_used") is False,
        "source_compiler": oracle.get("source_poset_compiler") is True,
        "det3_frozen": oracle.get("regularization_order_frozen_before_run") == 3,
        "marker_owned": oracle.get("marker_u1_ownership_explicit") is True,
    }

    scientific_keys = [
        "all_source_compilers_exact",
        "all_native_gram_exact",
        "all_infinite_gram_formulas_positive",
        "schatten3_minimal",
        "finite_B2_exact_and_phase_dependent",
        "infinite_non_S2_firewall",
        "unique_positive_B4_frequencies",
        "det3_deletes_1_2_first_visible_4",
        "full_active_metric_rigidity",
        "orthogonalized_det3_phase_free",
        "all_adversaries_prove_too_much",
        "marker_u1_ownership_exact",
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
        "route_b_false": summary.get("route_b_invocation_allowed") is False
        and analysis.get("route_b_invocation_allowed") is False,
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
    control_bytes: dict[str, list[int]] = {}
    for folder in (ROOT / "code", ROOT / "docs", ROOT / "experiments", ROOT / "evaluations"):
        for path in sorted(folder.rglob("*")):
            if not path.is_file():
                continue
            found = sorted(
                {byte for byte in path.read_bytes() if byte < 32 and byte not in {9, 10}}
            )
            if found:
                control_bytes[path.relative_to(ROOT).as_posix()] = found
    checks = {
        "row_counts": row_counts == EXPECTED_ROWS,
        "csv_lf": all(csv_lf_only.values()),
        "route": all(route_checks.values()),
        "source": all(source_checks.values()),
        "scientific": all(scientific_checks.values()),
        "listed_artifacts_exist": not missing_listed,
        "no_caches": not cache_paths,
        "no_control_bytes": not control_bytes,
    }
    payload = {
        "candidate_id": "SD-C30",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "row_counts": row_counts,
        "csv_lf_only": csv_lf_only,
        "route_checks": route_checks,
        "source_checks": source_checks,
        "scientific_checks": scientific_checks,
        "missing_listed_artifacts": missing_listed,
        "cache_paths": cache_paths,
        "control_bytes": control_bytes,
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
