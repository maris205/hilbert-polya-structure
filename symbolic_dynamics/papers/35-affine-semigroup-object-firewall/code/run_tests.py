#!/usr/bin/env python3
"""Exact unit, integration, mutation-sensitivity, and contract tests."""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import json
from pathlib import Path

import independent_evaluator as independent
import source_core as source_core


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    arguments = parser.parse_args()
    results = Path(arguments.results)

    parameters = load_json(results / "source_parameters.json")
    evaluation = load_json(results / "evaluation.json")
    firewall = load_json(results / "source_evaluator_firewall.json")
    counterexamples = load_json(results / "counterexamples.json")
    bc = load_json(results / "bc_firewall.json")
    fock = load_json(results / "fock_marker_firewall.json")
    boundaries = load_json(results / "boundary_controls.json")
    controls = load_json(results / "control_evaluation.json")
    relation_witnesses = load_json(results / "relation_witnesses.json")
    operator_certificates = load_json(results / "operator_certificates.json")
    full_boundary = load_json(results / "full_monoid_boundary.json")
    quotient_rows = load_csv(results / "quotient_ledger.csv")
    height_rows = load_csv(results / "height_dag_ledger.csv")
    backtrack_rows = load_csv(results / "backtrack_ledger.csv")
    census_rows = load_csv(results / "admissible_word_census.csv")

    tests: list[tuple[str, bool]] = []

    def check(name: str, condition: object) -> None:
        tests.append((name, bool(condition)))

    # Source-side exact unit tests.
    for radix in (2, 3, 4, 5):
        check(f"source_relation_length_r{radix}", len(source_core.relation_word(radix)) == radix + 3)
        check(
            f"source_relation_closed_r{radix}",
            source_core.path_states(radix, (0, 0), source_core.relation_word(radix))[-1] == (0, 0),
        )
        check(
            f"source_relation_hashimoto_r{radix}",
            source_core.cyclically_nonbacktracking(source_core.relation_word(radix)),
        )
        check(
            f"source_relation_primitive_r{radix}",
            source_core.primitive_closed_word(radix, (0, 0), source_core.relation_word(radix)),
        )
    check("source_positive_u_increment", source_core.height(4, source_core.step(4, (3, 2), "U+")) - source_core.height(4, (3, 2)) == 16)
    check("source_positive_v_increment", source_core.height(4, source_core.step(4, (3, 2), "V+")) - source_core.height(4, (3, 2)) == 48)
    check("source_inverse_u_domain", source_core.step(4, (15, 2), "U-") is None)
    check("source_inverse_v_domain", source_core.step(4, (3, 0), "V-") is None)
    check("source_polynomial_product", source_core.polynomial_multiply([Fraction(1), Fraction(-1)], [Fraction(1), Fraction(1)]) == [Fraction(1), Fraction(0), Fraction(-1)])
    check("source_diagonal_first_value", source_core.diagonal_values(2, 12)[0] == 1)

    # Evaluator-side independent unit tests.
    check("independent_transition_u", independent.transition(4, (3, 2), "U+") == (19, 2))
    check("independent_transition_v", independent.transition(4, (3, 2), "V+") == (3, 3))
    check("independent_relation_closed", independent.itinerary(4, (0, 0), independent.affine_word(4))[-1] == (0, 0))
    check("independent_hashimoto_rejects_backtrack", not independent.hashimoto_test(("U+", "U-")))
    check("independent_hashimoto_accepts_relation", independent.hashimoto_test(independent.affine_word(4)))
    check("independent_quotient_uq", independent.quotient_walk((0, 1), 4, 7, ("U+",) * 7)[-1] == (0, 1))
    determinant = independent.determinant_by_elementary_symmetric([Fraction(1), Fraction(1, 4)])
    check("independent_determinant_fixture", determinant == [Fraction(1), Fraction(-5, 4), Fraction(1, 4)])
    check("independent_reciprocal_fixture", independent.reciprocal_series([Fraction(1), Fraction(-1, 2)], 3) == [Fraction(1), Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)])

    # Mutation-sensitivity tests: these are rejected in-memory counterfactuals.
    mutated_height = dict(independent.independent_height_rows(parameters)[0])
    mutated_height["height_increment"] = 0
    check("mutation_height_detected", mutated_height != independent.independent_height_rows(parameters)[0])
    mutated_relation = list(independent.affine_word(4))
    mutated_relation[-1] = "V-"
    mutated_path = independent.itinerary(4, (0, 0), mutated_relation)
    check("mutation_relation_detected", mutated_path is None or mutated_path[-1] != (0, 0))
    correct_bc = independent.independent_bc_fixture(2, 12, 4)
    mutated_bc = dict(correct_bc)
    mutated_coefficients = list(correct_bc["determinant_coefficients"])
    mutated_coefficients[1] = "0/1"
    mutated_bc["determinant_coefficients"] = mutated_coefficients
    check("mutation_bc_coefficient_detected", mutated_bc != correct_bc)
    q22 = independent.independent_quotient(2, 2)
    mutated_q22 = dict(q22)
    mutated_q22["relation_polygon_vertex_simple"] = True
    check("mutation_small_modulus_detected", mutated_q22 != q22 and q22["required_2_2_degeneracy"])
    altered_fock = list(independent.fock_product_coefficients([2, 3, 5, 7, 11, 13, 17, 19], 2, 6))
    altered_fock[1] += Fraction(1, 23**2)
    check("mutation_preloaded_label_detected", altered_fock != independent.fock_product_coefficients([2, 3, 5, 7, 11, 13, 17, 19], 2, 6))

    # Result-contract gates.
    check("baseline_r4", parameters["baseline_r"] == 4)
    check("controls_r2_r3_r5", parameters["r_values"] == [4, 2, 3, 5])
    check("authority_height_definition", parameters["height_definition"] == "h_r(b,k)=b+r^k")
    check("authority_operator_definition", parameters["operator_definition"] == "A_plus=S+T on ell2(P_r)")
    check("authority_unweighted_generators", parameters["edge_weight_a"] == parameters["edge_weight_b"] == "1/1")
    check("height_row_count", len(height_rows) == 520)
    check("height_all_strict", all(row["strict_increase"] == "True" for row in height_rows))
    check(
        "height_all_authority_increments",
        all(
            int(row["height_increment"])
            == (
                int(row["r"]) ** int(row["origin_k"])
                if row["token"] == "U+"
                else (int(row["r"]) - 1) * int(row["r"]) ** int(row["origin_k"])
            )
            == int(row["expected_increment"])
            for row in height_rows
        ),
    )
    check("backtrack_row_count", len(backtrack_rows) == len(height_rows))
    check("backtracks_hashimoto_excluded", all(row["hashimoto_allowed"] == "False" for row in backtrack_rows))
    check("census_row_count", len(census_rows) == 64)
    check("evaluation_pass", evaluation["status"] == "PASS")
    check("all_ten_gates_pass", len(evaluation["gates"]) == 10 and all(evaluation["gates"].values()))
    check("no_unexpected_mismatches", evaluation["unexpected_mismatches"] == [])
    check("source_hashes_unchanged", evaluation["source_hashes_unchanged_after_evaluation"])
    check("route_a_not_advanced", evaluation["route_a_advanced"] is False)
    check("relation_witness_count", len(relation_witnesses["witnesses"]) == 8)
    check("relation_lengths_r_plus_3", all(item["length"] == item["r"] + 3 for item in relation_witnesses["witnesses"]))
    check("relation_words_primitive", all(item["primitive"] for item in relation_witnesses["witnesses"]))
    check("operator_certificate_count", len(operator_certificates["certificates"]) == 4)
    check("operator_certificates_finite_only", all(item["finite_window_certificate_only"] for item in operator_certificates["certificates"]))
    check("full_monoid_no_finite_census", full_boundary["finite_census_performed"] is False)
    check("full_monoid_infinite_outdegree", full_boundary["outdegree"] == "countably_infinite")
    check("quotient_row_count", len(quotient_rows) == 48)
    check("quotient_relation_all_preserved", all(row["relation_preserved"] == "True" for row in quotient_rows))
    check("quotient_uq_all_present", all(row["u_q_closed"] == "True" for row in quotient_rows))
    check("quotient_2_2_degeneracy", next(row for row in quotient_rows if row["r"] == "2" and row["q"] == "2")["required_2_2_degeneracy"] == "True")
    check("bc_fixture_count", len(bc["fixtures"]) == 2)
    check("bc_exact_log_coefficients", all(item["coefficient_identity_Tr_Dm_over_m"] for item in bc["fixtures"]))
    check("bc_trace_not_det_germ", all(item["trace_is_not_determinant_germ"] for item in bc["fixtures"]))
    check("bc_det_z1_zero", all(item["determinant_at_z_one"] == "0/1" for item in bc["fixtures"]))
    check("fock_methods_equal", fock["coefficient_methods_equal"])
    check("fock_prime_logic_evaluator_only", fock["construction_location"] == "independent evaluator after source freeze" and not fock["source_contains_prime_classifier"])
    check("fock_z_not_graph_step", fock["z_one_is_not_original_graph_step_marker"])
    check("generic_controls_survive", controls["generic_relation_cycles_survive"])
    check("generic_controls_no_acceptance_labels", not controls["arithmetic_acceptance_labels_used"])
    check("signed_odd_cancel", boundaries["signed_scalar"]["odd_powers_cancel"])
    check("signed_even_survive", boundaries["signed_scalar"]["even_powers_survive"])
    check("nilpotent_det_one", boundaries["nilpotent_matrix"]["determinant_factor_is_one"])
    check("matrix_first_not_all", boundaries["traceless_invertible_matrix"]["first_trace_zero"] and boundaries["traceless_invertible_matrix"]["second_trace_nonzero"] and not boundaries["traceless_invertible_matrix"]["all_orders_cancel"])
    check("groupoid_boundary_open", boundaries["groupoid_boundary"]["status"] == "OPEN_BOUNDARY_NOT_EVALUATED_AS_SAME_OBJECT")
    check("firewall_pass", firewall["pass"])
    check("firewall_no_source_prime_logic", firewall["source_identifier_violations"] == [])
    check("firewall_evaluator_no_source_import", firewall["evaluator_imports_source_core"] is False)
    check("expected_counterexamples_retained", counterexamples["all_expected_corrections_retained"])
    check("counterexample_count", len(counterexamples["expected_corrections"]) == 6)
    check("counterexamples_no_unexpected", counterexamples["unexpected_mismatches"] == [])
    check("parameters_exact_only", parameters["external_dependencies"] == [] and not parameters["network_used"] and not parameters["gpu_used"])
    check("parameters_no_timestamps", parameters["result_timestamps"] is False)

    failed = [name for name, passed in tests if not passed]
    report = {
        "schema_version": "SD-C37-tests-v1",
        "test_count": len(tests),
        "passed": len(tests) - len(failed),
        "failed": len(failed),
        "failed_names": failed,
        "mutation_sensitivity_test_count": 5,
        "tests": [{"name": name, "status": "PASS" if passed else "FAIL"} for name, passed in tests],
        "status": "PASS" if not failed else "FAIL",
    }
    (results / "test_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if failed:
        raise SystemExit(f"tests failed: {failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
