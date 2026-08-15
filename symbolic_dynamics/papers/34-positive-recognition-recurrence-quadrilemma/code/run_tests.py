#!/usr/bin/env python3
"""Exact unit, integration, and result-contract tests for Paper 34."""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import json
from pathlib import Path

import source_core as core


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

    graph_rows = load_csv(results / "graph_census.csv")
    graph_summary = load_json(results / "graph_witness_summary.json")
    kraft_rows = load_csv(results / "kraft_clock_summary.csv")
    clock_rows = load_csv(results / "code_clock_ledger.csv")
    neutral = load_json(results / "neutral_recognizer.json")
    marker_rows = load_csv(results / "marker_ledger.csv")
    evaluation = load_json(results / "evaluation.json")
    inventories = load_csv(results / "inventory_controls.csv")
    boundaries = load_json(results / "boundary_controls.json")
    firewall = load_json(results / "source_evaluator_firewall.json")
    counterexamples = load_json(results / "counterexamples.json")
    parameters = load_json(results / "parameters.json")
    construction_rows = load_csv(results / "connector_construction_counterexamples.csv")

    tests: list[tuple[str, bool]] = []

    def check(name: str, condition: object) -> None:
        tests.append((name, bool(condition)))

    check("edge_mask_roundtrip", core.edge_list(2, core.edge_mask(2, [(0, 1), (1, 0)])) == ((0, 1), (1, 0)))
    check("scc_empty_graph", core.strongly_connected_components(3, []) == ((0,), (1,), (2,)))
    check("scc_directed_cycle", core.strongly_connected_components(3, [(0, 1), (1, 2), (2, 0)]) == ((0, 1, 2),))
    check("simple_loop_cycle", core.all_simple_cycles(1, [(0, 0)]) == (((0, 0),),))
    check("simple_two_cycle", ((0, 1), (1, 0)) in core.all_simple_cycles(2, [(0, 1), (1, 0)]))
    cycle = ((0, 1), (1, 2), (2, 0))
    check("canonical_rotation", core.canonical_cycle(((1, 2), (2, 0), (0, 1))) == cycle)
    check("legal_closed_word", core.legal_closed_word(cycle))
    check("illegal_open_word", not core.legal_closed_word(((0, 1), (1, 2))))
    root, exponent = core.primitive_root(cycle + cycle)
    check("primitive_root_word", root == cycle)
    check("primitive_root_exponent", exponent == 2)
    check("positive_word_weight", core.word_weight(3, cycle) > 0)
    check("weight_power_identity", core.word_weight(3, cycle + cycle) == core.word_weight(3, cycle) ** 2)
    check("base_q_digits", core.base_q_digits(17, 4) == (1, 0, 1))
    check("binary_gamma_payload", core.gamma_payload(5, 2) == (0, 0, 1, 0, 1))
    check("ternary_gamma_payload", core.gamma_payload(5, 3) == (0, 1, 2))
    words = [core.gamma_payload(value, 2) for value in range(1, 128)]
    check("gamma_prefix_free", core.prefix_collision_count(words) == 0)
    check("polynomial_multiply", core.polynomial_multiply([Fraction(1), Fraction(-1)], [Fraction(1), Fraction(1)]) == [Fraction(1), Fraction(0), Fraction(-1)])
    check("polynomial_evaluate", core.polynomial_evaluate([Fraction(1), Fraction(-1)], Fraction(1)) == 0)
    loop_traces = core.trace_powers(1, [(0, 0, Fraction(1, 2))], 1)
    check("trace_one_loop", loop_traces == [Fraction(1, 2)])
    check("determinant_one_loop", core.determinant_from_traces(loop_traces) == [Fraction(1), Fraction(-1, 2)])

    check("graph_row_count", len(graph_rows) == 5)
    check("exhaustive_graph_total", sum(int(row["graphs"]) for row in graph_rows if row["graph_family"] == "exhaustive") == 66066)
    check("hash_graph_total", int(graph_rows[-1]["graphs"]) == 64)
    check("graph_true_failure_zero", sum(int(row["failures"]) for row in graph_rows) == 0)
    check("shared_pair_total", sum(int(row["shared_pairs"]) for row in graph_rows) == 680208)
    check("connector_pair_total", sum(int(row["connector_pairs"]) for row in graph_rows) == 164336)
    check("mixed_root_total", sum(int(row["mixed_roots"]) for row in graph_rows) == 844544)
    check("mixed_root_partition", sum(int(row["mixed_roots"]) for row in graph_rows) == sum(int(row["shared_pairs"]) + int(row["connector_pairs"]) for row in graph_rows))
    check("strict_normal_form_failure_total", sum(int(row["strict_external_connector_failures"]) for row in graph_rows) == 18272)
    check("construction_ledger_complete", len(construction_rows) == 18272)
    check("graph_summary_failure_zero", graph_summary["failure_count"] == 0)
    check("graph_summary_strict_failures", graph_summary["strict_external_connector_failure_count"] == 18272)
    check("graph_witness_digest_shape", len(graph_summary["witness_sha256"]) == 64)

    check("kraft_summary_rows", len(kraft_rows) == 12)
    check("clock_ledger_rows", len(clock_rows) == 6141)
    check("kraft_bounds", all(row["kraft_at_most_one"] == "True" for row in kraft_rows))
    check("prefix_collision_zero", sum(int(row["prefix_collisions"]) for row in kraft_rows) == 0)
    check("roof_sum_failure_zero", sum(int(row["roof_sum_failures"]) for row in kraft_rows) == 0)
    check("powered_clock_failure_zero", sum(int(row["powered_clock_failures"]) for row in kraft_rows) == 0)
    check("clock_roof_sums_one", all(row["roof_share_sum"] == "1/1" for row in clock_rows))
    check("clock_powered_certificates", all(row["powered_clock_certificate"] == "True" for row in clock_rows))

    check("neutral_dimension", neutral["dimension"] == 160)
    check("neutral_recurrent_dimension", neutral["recurrent_dimension"] == 126)
    check("neutral_cycle_count", len(neutral["cycles"]) == 17)
    check("terminal_extension_equal", neutral["terminal_extension_equal"])
    check("newton_product_equal", neutral["determinant_newton"] == neutral["recurrent_product"])
    check("determinant_constant_one", neutral["determinant_newton"][0] == "1/1")
    check("marker_item_count", len(marker_rows) == 17)
    check("marker_formal_all_different", all(row["formal_equal"] == "False" for row in marker_rows))
    check("marker_z_one_all_equal", all(row["equal_at_z_one"] == "True" for row in marker_rows))

    check("independent_evaluation_pass", evaluation["status"] == "PASS")
    check("independent_graph_equal", evaluation["graph_all_equal"])
    check("independent_graph_failures_zero", evaluation["graph_failure_count"] == 0)
    check("preregistered_C2_fails", evaluation["preregistered_C2_status"] == "FAIL_AS_WRITTEN")
    check("repaired_C2_passes", evaluation["repaired_C2_status"] == "PASS")
    check("terminal_tail_acyclic", evaluation["terminal_tail_acyclic_certificate"])
    check("source_firewall_pass", firewall["status"] == "PASS" and firewall["forbidden_identifier_count"] == 0)

    check("inventory_control_count", len(inventories) == 8)
    check("inventory_terminal_invariance", all(row["terminal_equals_unclassified"] == "True" for row in inventories))
    check("proper_pruning_changes", all(row["pruning_differs_when_proper_nonempty"] in {"True", "NA"} for row in inventories))
    check("inventory_marker_z_one", all(row["raw_equals_induced_at_z_one"] == "True" for row in inventories))
    check("nonempty_inventory_marker_differs", all(row["raw_equals_induced_formally"] == "False" for row in inventories if int(row["support_count"]) > 0))
    check("matched_inventory_cardinality", next(int(row["support_count"]) for row in inventories if row["inventory"] == "matched_sha") == next(int(row["support_count"]) for row in inventories if row["inventory"] == "trial_atom"))

    signed = boundaries["signed_scalar"]
    matrix = boundaries["matrix_branches"]
    check("signed_nilpotent", signed["nilpotent_order_at_most_3"])
    check("signed_trace_cancellation", signed["trace_orders_1_to_8"] == [0] * 8)
    check("absolute_trace_survives", any(signed["absolute_trace_orders_1_to_8"]))
    check("signed_determinant_one", signed["determinant_I_minus_zA"] == ["1/1"])
    check("matrix_cross_products_zero", matrix["left_times_right_zero"] and matrix["right_times_left_zero"])
    check("matrix_pure_products_survive", matrix["pure_left_survives"] and matrix["pure_right_survives"])
    check("matrix_determinant_product", matrix["sum_determinant"] == matrix["product_of_pure_determinants"])

    check("counterexample_C2_count", counterexamples["preregistered_C2_witness_normal_form_counterexample_count"] == 18272)
    check("positive_class_counterexample_zero", counterexamples["positive_class_counterexample_count"] == 0)
    check("counterexample_theorem_action", counterexamples["theorem_action"] == "REVISE_LOOSE_WORDING_AND_RETAIN_POSITIVE_SAME_SCC_STATEMENT")
    check("parameters_no_timestamps", parameters["result_timestamps"] is False)
    check("parameters_no_external_data", parameters["external_data"] is False)
    check("parameters_no_dependencies", parameters["external_dependencies"] == [])

    failed = [name for name, passed in tests if not passed]
    report = {
        "schema_version": "P34-tests-v1",
        "test_count": len(tests),
        "passed": len(tests) - len(failed),
        "failed": len(failed),
        "failed_names": failed,
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
