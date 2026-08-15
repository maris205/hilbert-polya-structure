#!/usr/bin/env python3
"""Run exact authority integration tests for SD-C38."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def add(checks: list[dict[str, object]], name: str, passed: bool) -> None:
    checks.append({"name": name, "pass": bool(passed)})


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", required=True)
    arguments = parser.parse_args()
    result_dir = Path(arguments.result_dir)

    environment = read_json(result_dir / "environment_lock.json")
    dependencies = read_json(result_dir / "dependency_lock.json")
    parameters = read_json(result_dir / "run_parameters.json")
    source_summary = read_json(result_dir / "source_summary.json")
    source_tests = read_json(result_dir / "source_test_report.json")
    separation = read_json(result_dir / "source_separation_certificate.json")
    evaluation = read_json(result_dir / "evaluation.json")
    bridge = read_json(result_dir / "prototype_bridge_certificate.json")
    graded = read_json(result_dir / "graded_control.json")
    controls = read_json(result_dir / "control_summary.json")
    trace = read_csv(result_dir / "trace_audit.csv")
    markers = read_csv(result_dir / "marker_audit.csv")
    operator = read_csv(result_dir / "operator_cycle_audit.csv")
    finite = read_csv(result_dir / "finite_chain_audit.csv")

    checks: list[dict[str, object]] = []
    add(checks, "environment_schema", environment["schema"] == "SD-C38-environment-lock-v1")
    add(checks, "cpu_only", environment["cpu_only"])
    add(checks, "network_unused", not environment["network_used"])
    add(checks, "external_data_unused", not environment["external_data_used"])
    add(checks, "hash_seed_zero", environment["pythonhashseed"] == "0")
    add(checks, "scientific_dependencies_empty", dependencies["scientific_dependencies"] == [])
    add(checks, "seal_dependency_scoped", list(dependencies["seal_audit_dependencies"]) == ["PyYAML"])
    add(checks, "parameter_family_exact", parameters["main_r"] == [2, 3, 4, 5])
    add(checks, "baseline_exact", parameters["baseline_r"] == 4)
    add(checks, "word_cutoff_exact", parameters["max_word_length"] == 12)
    add(checks, "target_zero_none", parameters["target_zero_data"] == "none")
    add(checks, "source_checks_33", source_summary["source_checks_passed"] == source_summary["source_checks_total"] == 33)
    add(checks, "source_test_report_pass", source_tests["all_pass"])
    add(checks, "source_separation_pass", separation["pass"])
    add(checks, "source_evaluator_physically_distinct", separation["checks"]["process_files_physically_distinct"])
    add(checks, "source_no_banned_identifier", separation["checks"]["source_has_no_banned_identifier"])
    add(checks, "evaluator_no_source_import", separation["checks"]["evaluator_has_no_source_import"])
    add(checks, "prototype_bridge_pass", bridge["pass"])
    add(checks, "prototype_semantics_33", bridge["prototype_semantic_checks_passed"] == bridge["prototype_semantic_checks_total"] == 33)
    add(checks, "independent_evaluation_pass", evaluation["all_checks_pass"])
    add(checks, "integration_checks_35", evaluation["integration_passed"] == evaluation["integration_total"] == 35)
    add(checks, "trace_row_count", len(trace) == 52)
    add(checks, "marker_row_count", len(markers) == 5)
    add(checks, "operator_row_count", len(operator) == 5)
    add(checks, "finite_row_count", len(finite) == 6)

    expected_excess = {2: (5, 10), 3: (6, 12), 4: (7, 14), 5: (8, 32)}
    for r, (length, excess) in expected_excess.items():
        rows = [row for row in trace if int(row["r"]) == r]
        first = next(row for row in rows if int(row["relation_excess"]) != 0)
        add(checks, f"first_excess_length_r{r}", int(first["length"]) == length)
        add(checks, f"first_excess_count_r{r}", int(first["relation_excess"]) == excess)

    marker_map = {int(row["r"]): row for row in markers}
    add(checks, "balanced_marker_descends", marker_map[1]["unit_step_marker_descends"] == "true")
    add(checks, "main_markers_fail", all(marker_map[r]["unit_step_marker_descends"] == "false" for r in (2, 3, 4, 5)))
    add(checks, "relation_words_primitive", all(row["primitive"] == "true" for row in markers))
    add(checks, "relation_words_cyclically_nonbacktracking", all(row["cyclically_nonbacktracking"] == "true" for row in markers))

    operator_map = {int(row["r"]): row for row in operator}
    add(checks, "baseline_exponent_sum_23", int(operator_map[4]["origin_exponent_sum"]) == 23)
    add(checks, "baseline_weight_2_minus_46", operator_map[4]["one_cycle_weight"] == "1/70368744177664")
    add(checks, "operator_bounds_positive", all(row["strictly_positive"] == "true" for row in operator))

    expected_affine_h1 = [2, 1, 1, 1, 1, 1]
    add(checks, "finite_affine_h1_exact", [int(row["h1_after_affine_cells"]) for row in finite] == expected_affine_h1)
    add(checks, "finite_complete_h1_zero", all(int(row["h1_after_complete_presentation_cells"]) == 0 for row in finite))
    add(checks, "finite_boundary_affine_zero", all(row["boundary_squared_zero_affine"] == "True" for row in finite))
    add(checks, "finite_boundary_complete_zero", all(row["boundary_squared_zero_complete"] == "True" for row in finite))
    add(checks, "graded_samples_zero", graded["all_sampled_supertraces_zero"])
    add(checks, "graded_sample_count", len(graded["samples"]) == 48)
    add(checks, "generic_multiplier_zero", all(row["euler_multiplier"] == 0 for row in graded["matched_generic_controls"]))
    add(checks, "balanced_complete_control_zero", controls["balanced_control"]["complete_finite_h1"] == 0)
    add(checks, "all_mutated_markers_fail", all(not row["marker_descends"] for row in controls["exponent_mutations"]))
    add(checks, "route_tuple_exact", evaluation["route_tuple"] == ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
    add(checks, "overall_rejected", evaluation["overall_verdict"] == "ROUTE_A_REJECTED")
    add(checks, "route_b_false", evaluation["route_b_invocation_allowed"] is False)
    add(checks, "target_zero_false", evaluation["target_zero_data_used"] is False)

    passed = sum(bool(row["pass"]) for row in checks)
    payload = {
        "schema": "SD-C38-authority-test-report-v1",
        "candidate_id": "SD-C38",
        "tests": checks,
        "passed": passed,
        "total": len(checks),
        "all_pass": passed == len(checks),
    }
    write_json(result_dir / "test_report.json", payload)
    print(json.dumps({"candidate_id": "SD-C38", "passed": passed, "total": len(checks), "all_pass": payload["all_pass"]}, sort_keys=True))
    return 0 if payload["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
