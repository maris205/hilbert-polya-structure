#!/usr/bin/env python3
"""Audit SD-C27 exact artifacts, Route schema, source policy, and hygiene."""

from __future__ import annotations

import ast
import csv
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUTPUT = RESULTS / "integrity_audit.json"
ROUTE_A = ROOT / "evaluations" / "route_a" / "SD-C27" / "2026-08-14.yaml"
CORE = ROOT / "code" / "sdc27_holomorphic_lefschetz.py"
EVALUATOR = ROOT / "code" / "sdc27_evaluator.py"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"

EXPECTED_CSV_ROWS = {
    "arbitrary_inventory_controls.csv": 42,
    "code_registry.csv": 4095,
    "de_rham_chain_checks.csv": 40,
    "de_rham_power_supertraces.csv": 320,
    "local_determinant_telescoping.csv": 20,
    "marker_ownership_controls.csv": 4095,
    "nuclearity_domain_ledger.csv": 21,
    "ordinary_block_graded_firewall.csv": 20,
    "primitive_necklace_ledger.csv": 1183,
    "route_gate_summary.csv": 5,
    "scalar_power_rigidity.csv": 3066,
    "shared_disjoint_determinants.csv": 21,
    "shared_disjoint_power_ledger.csv": 168,
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

EXPECTED_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]


def csv_rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def true(row: dict[str, str], field: str) -> bool:
    return row.get(field) == "True"


def false(row: dict[str, str], field: str) -> bool:
    return row.get(field) == "False"


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


def text_control_characters() -> dict[str, list[int]]:
    suffixes = {".bib", ".csv", ".json", ".md", ".py", ".tex", ".txt", ".yaml", ".yml"}
    bad: dict[str, list[int]] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        positions = [
            index
            for index, byte in enumerate(path.read_bytes())
            if byte < 32 and byte not in {9, 10}
        ]
        if positions:
            bad[path.relative_to(ROOT).as_posix()] = positions[:20]
    return bad


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
    metrics = route.get("a2", {}).get("metrics", {})
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
        relative
        for relative in artifact_paths
        if relative not in future_artifacts and not (ROOT / relative).is_file()
    ]
    source_commit = route.get("source_commit")
    code_commit = route.get("code_commit")
    lock_commit = route.get("source_lock", {}).get("code_commit")
    paired_pending = source_commit == code_commit == lock_commit == PENDING
    paired_sealed = source_commit == code_commit == lock_commit and is_git_hash(source_commit)
    route_checks = {
        "yaml_parse": isinstance(route, dict),
        "required_top_level_keys": not route_missing,
        "candidate_id": route.get("candidate_id") == "SD-C27",
        "family": route.get("source_lock", {}).get("family") == "symbolic_dynamics",
        "route_tuple": route.get("route_tuple") == EXPECTED_TUPLE,
        "layer_verdicts": [
            route.get(key, {}).get("verdict") for key in ("a0", "a1", "a2", "a3", "a4")
        ]
        == EXPECTED_TUPLE,
        "overall_rejected": route.get("overall_verdict") == "ROUTE_A_REJECTED",
        "route_b_false": route.get("route_b_invocation_allowed") is False,
        "paired_provenance": paired_pending or paired_sealed,
        "two_stage_note": "two-stage" in route.get("freeze_note", "").lower(),
        "artifact_paths_exist": not missing_artifacts,
        "target_zero_root_fields_na": all(
            isinstance(metrics.get(field), str)
            and metrics[field].startswith("not_applicable;")
            for field in target_fields
        ),
        "target_zero_data_false": metrics.get("target_zero_data_used") is False,
        "a2_scoped_analytic_credit": route.get("a2", {}).get("verdict")
        == "A2_ANALYTIC_DETERMINANT",
        "proves_too_much": route.get("adversarial_controls", {}).get(
            "proves_too_much_risk"
        )
        is True,
        "a4_scoped": "this candidate"
        in route.get("a4", {}).get("strongest_failure", "").lower(),
    }

    source_tree = ast.parse(CORE.read_text(encoding="utf-8"))
    call_names = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    oracle = json.loads((RESULTS / "source_oracle_certificate.json").read_text())
    source_checks = {
        "candidate_evaluator_separation": oracle.get("candidate_evaluator_separated")
        is True,
        "evaluator_exists": EVALUATOR.is_file(),
        "no_forbidden_candidate_calls": oracle.get("forbidden_candidate_calls") == [],
        "static_call_audit": call_names.isdisjoint(
            {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
        ),
        "prime_table_false": oracle.get("prime_table_used_in_candidate") is False,
        "target_weight_false": oracle.get("target_weight_used_in_candidate") is False,
        "target_feedback_false": oracle.get("target_weight_used_in_candidate") is False,
        "zero_data_false": oracle.get("riemann_zero_data_used") is False,
        "cutoff_independent_code": oracle.get("cutoff_dependent_code") is False,
        "graded_not_mislabeled": oracle.get(
            "graded_ratio_called_ordinary_block_determinant"
        )
        is False,
        "fixed_digit_maps": oracle.get("digit_maps")
        == ["z/2-1/4", "z/2+1/4"],
    }

    code = csv_rows("code_registry.csv")
    prefix = json.loads((RESULTS / "prefix_free_certificate.json").read_text())
    scalar = csv_rows("scalar_power_rigidity.csv")
    ordinary = json.loads((RESULTS / "ordinary_matrix_firewall.json").read_text())
    chain = csv_rows("de_rham_chain_checks.csv")
    powers = csv_rows("de_rham_power_supertraces.csv")
    local = csv_rows("local_determinant_telescoping.csv")
    blocks = csv_rows("ordinary_block_graded_firewall.csv")
    determinants = csv_rows("shared_disjoint_determinants.csv")
    shared_powers = csv_rows("shared_disjoint_power_ledger.csv")
    necklaces = csv_rows("primitive_necklace_ledger.csv")
    arbitrary = csv_rows("arbitrary_inventory_controls.csv")
    marker = csv_rows("marker_ownership_controls.csv")
    nuclearity = csv_rows("nuclearity_domain_ledger.csv")
    route_rows = csv_rows("route_gate_summary.csv")
    tests = json.loads((RESULTS / "test_summary.json").read_text())
    double_run = json.loads((RESULTS / "double_run_certificate.json").read_text())
    summary = json.loads((RESULTS / "summary.json").read_text())

    ordinary_cases = ordinary.get("cases", {})
    mixed_necklaces = [row for row in necklaces if true(row, "mixed")]
    pure_necklaces = [row for row in necklaces if false(row, "mixed")]
    shared_controls = [row for row in arbitrary if row["architecture"] == "shared_renewal"]
    disjoint_controls = [row for row in arbitrary if row["architecture"] == "disjoint_components"]

    scientific_checks = {
        "gamma_code_registry_exact": all(
            true(row, "length_match")
            and true(row, "derivative_match")
            and true(row, "common_compact_containment")
            and true(row, "global_prefix_free")
            and row["inventory_filter_stage"] == "post_freeze_evaluator"
            and row["candidate_target_calls"] == "0"
            for row in code
        ),
        "prefix_registry_exact": prefix.get("prefix_free") is True
        and prefix.get("prefix_collision_pairs") == 0
        and prefix.get("range") == [1, 4096]
        and prefix.get("word_count") == 4096
        and prefix.get("code_fixed_before_inventory") is True,
        "scalar_r1_fit": all(
            (row["power"] != "1")
            or (true(row, "match") and true(row, "r1_fit") and false(row, "r2_plus_failure"))
            for row in scalar
        ),
        "scalar_r2_plus_failure": all(
            (row["power"] == "1")
            or (false(row, "match") and true(row, "r2_plus_failure") and row["residual"] != "0/1")
            for row in scalar
        ),
        "scalar_rank_one_boundary_excluded": all(
            false(row, "q_zero_rank_one_boundary") for row in scalar
        ),
        "ordinary_trace_class_pole_firewall": ordinary.get("theorem_firewall")
        == "entire_fredholm_determinant_cannot_equal_(1-t)/(1-q*t)"
        and ordinary.get("scope")
        == "ordinary finite-dimensional or trace-class tensor fiber"
        and len(ordinary_cases) == 5
        and all(
            case.get("ordinary_trace_class_determinant_entire") is True
            and case.get("genuine_pole_at_q_inverse") is True
            and case.get("ordinary_trace_class_fiber_exists") is False
            and case.get("first_two_moments_force_third_failure") is True
            and case.get("two_by_two_moment_control", {}).get("p3_residual") != "0/1"
            for case in ordinary_cases.values()
        ),
        "chain_maps_commute": all(true(row, "chain_residual_zero") for row in chain),
        "characteristic_quotients_exact": all(
            true(row, "characteristic_quotient_exact") for row in chain
        ),
        "ordinary_block_not_graded_chain": all(
            false(row, "ordinary_block_equals_graded_ratio") for row in chain
        ),
        "all_power_supertraces_exact": all(true(row, "exact_match") for row in powers),
        "local_determinants_telescope": all(true(row, "quotient_exact") for row in local),
        "ordinary_block_not_graded_ratio": all(
            false(row, "ordinary_equals_graded")
            and row["ordinary_object"] == "direct_sum_product"
            and row["graded_object"] == "degree_ratio"
            and row["ownership_gate"] == "STOP_ORDINARY_FREDHOLM_IDENTIFICATION"
            for row in blocks
        ),
        "shared_disjoint_determinants_differ": all(
            false(row, "shared_equals_disjoint")
            and row["difference"] != "0"
            and row["shared_cohomology_dimension"] == "1"
            and row["disjoint_cohomology_dimension"] == row["branch_count"]
            for row in determinants
        ),
        "shared_disjoint_power_one_agrees": all(
            row["power"] != "1"
            or (true(row, "equal") and false(row, "mixed_survives") and row["mixed_difference"] == "0/1")
            for row in shared_powers
        ),
        "shared_disjoint_higher_powers_split": all(
            row["power"] == "1"
            or (false(row, "equal") and true(row, "mixed_survives") and row["mixed_difference"] != "0/1")
            for row in shared_powers
        ),
        "primitive_necklace_census": len(mixed_necklaces) == 1174
        and len(pure_necklaces) == 9
        and all(true(row, "primitive") and true(row, "shared_included") for row in necklaces),
        "mixed_necklaces_survive": all(
            false(row, "disjoint_included") and false(row, "de_rham_cancels_word")
            for row in mixed_necklaces
        ),
        "pure_necklaces_are_disjoint_atoms": all(
            true(row, "disjoint_included") for row in pure_necklaces
        ),
        "arbitrary_inventory_post_freeze": all(
            row["compiler_target_calls"] == "0"
            and true(row, "inventory_loaded_post_freeze")
            and false(row, "selectivity_credit")
            and true(row, "proves_too_much")
            for row in arbitrary
        ),
        "shared_controls_collapse": len(shared_controls) == 21
        and all(
            row["cohomology_dimension"] == "1"
            and true(row, "mixed_primitives")
            and false(row, "atom_inventory_equivalent")
            for row in shared_controls
        ),
        "disjoint_controls_are_inventory": len(disjoint_controls) == 21
        and all(
            row["cohomology_dimension"] == row["atom_count"]
            and false(row, "mixed_primitives")
            and true(row, "atom_inventory_equivalent")
            for row in disjoint_controls
        ),
        "marker_ownership_firewall": all(
            int(row["gamma_code_length"]) > 1
            and false(row, "return_and_digit_markers_equal")
            and true(row, "u_equals_one_specialization")
            and true(row, "first_return_changes_object")
            and row["whole_codeword_alphabet"] == "countable_return_alphabet"
            and false(row, "original_digit_euler_marker_match")
            for row in marker
        ),
        "nuclearity_domain_scoped": all(
            row["shared_degreewise_trace_class_domain"] == "Re(s)>1_uniform_guarantee"
            and row["disjoint_degreewise_trace_class_domain"] == "Re(s)>1_uniform_guarantee"
            and row["graded_relative_determinant_domain"] == "Re(s)>1_uniform_guarantee"
            and row["prime_cohomology_barrier"]
            == (
                "Re(s)>1"
                if row["inventory"] == "prime_evaluator"
                else "control_inventory_not_used_for_prime_boundary"
            )
            and false(row, "finite_prefix_is_domain_proof")
            and row["remove_constant_cohomology_gives"] == "graded_determinant_one"
            and true(row, "retain_constant_cohomology")
            and false(row, "critical_strip_same_object_continuation")
            for row in nuclearity
        ),
        "route_rows_exact": [row["verdict"] for row in route_rows] == EXPECTED_TUPLE
        and [row["layer"] for row in route_rows] == ["A0", "A1", "A2", "A3", "A4"],
        "tests_exact": tests.get("status") == "PASS"
        and tests.get("collected") == tests.get("passed") == 53
        and tests.get("failed") == tests.get("skipped") == 0,
        "double_run_exact": double_run.get("status") == "PASS"
        and double_run.get("byte_identical") is True
        and double_run.get("mismatched_paths") == []
        and double_run.get("first_run_combined_sha256")
        == double_run.get("second_run_combined_sha256"),
        "summary_route_exact": summary.get("route_tuple") == EXPECTED_TUPLE
        and summary.get("overall_verdict") == "ROUTE_A_REJECTED"
        and summary.get("route_b_invocation_allowed") is False
        and summary.get("target_zero_data_used") is False,
    }

    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.name in {"__pycache__", ".pytest_cache"}
    )
    control_characters = text_control_characters()
    hygiene_checks = {
        "csv_lf_only": all(csv_lf_only.values()),
        "json_parse": all(json_parse.values()),
        "no_forbidden_runtime_metadata": not forbidden_metadata,
        "cache_clean": not cache_paths,
        "control_characters_clean": not control_characters,
    }

    all_checks = {**route_checks, **source_checks, **scientific_checks, **hygiene_checks}
    failed_checks = sorted(name for name, passed in all_checks.items() if not passed)
    payload = {
        "candidate_id": "SD-C27",
        "status": "PASS" if not failed_checks else "FAIL",
        "row_counts": row_counts,
        "expected_row_counts": EXPECTED_CSV_ROWS,
        "csv_lf_only": csv_lf_only,
        "json_parse": json_parse,
        "forbidden_runtime_metadata": forbidden_metadata,
        "route_checks": route_checks,
        "route_missing_keys": route_missing,
        "missing_artifact_paths": missing_artifacts,
        "source_checks": source_checks,
        "scientific_checks": scientific_checks,
        "hygiene_checks": hygiene_checks,
        "cache_paths": cache_paths,
        "control_characters": control_characters,
        "failed_checks": failed_checks,
        "route_tuple": EXPECTED_TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not failed_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
