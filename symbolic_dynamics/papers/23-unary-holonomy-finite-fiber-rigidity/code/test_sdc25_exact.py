#!/usr/bin/env python3
"""Exact and scoped regression tests for SD-C25 experiments E1--E10."""

from __future__ import annotations

import ast
from fractions import Fraction
import json
from pathlib import Path

from sdc25_evaluator import (
    TARGET_NAMES,
    algebraic_control_rows,
    block_fiber_fixtures,
    constructive_composite_witnesses,
    deterministic_matrix_fixtures,
    exhaustive_boolean_relation_rows,
    exhaustive_transformation_rows,
    imported_wrapper_certificates,
    recurrent_wrapper_rows,
    roof_marker_rows,
    target_digest,
    target_vector,
    transient_wrapper_rows,
)
from sdc25_unary_fiber import (
    BLOCK_MAX_POWER,
    MEMORY_CUTOFFS,
    TRACE_SIGMAS,
    block_adjacency,
    canonical_fiber_trace,
    canonical_word_certificate,
    cayley_hamilton_matrix,
    characteristic_coefficients,
    decimal_edge_prefix_interval,
    finite_power_traces,
    fraction_determinant,
    generating_numerator,
    generating_series_from_rational,
    identity_minus_scaled,
    matrix_is_zero,
    matrix_multiply,
    matrix_power,
    matrix_trace,
    memorizer_response,
    minimal_recurrence_order,
    newton_determinant_coefficients,
    polynomial_value,
    recurrence_residuals,
    response_sequences,
    transformation_tail_period,
)


ROOT = Path(__file__).resolve().parents[1]
SYMBOLIC_ROOT = ROOT.parents[1]


def test_e1_canonical_word_examples() -> None:
    for index in (2, 3, 5, 17, 101, 256):
        row = canonical_word_certificate(index)
        assert row["length"] == index
        assert row["one_count"] == index - 1
        assert row["terminal_value"] == 2
        assert row["holonomy"] == 2
        assert row["all_edges_valid"]
        assert row["ordered_word_match"]
        assert row["unique_minimum_mark"]
        assert row["primitive"]


def test_e1_candidate_core_has_no_forbidden_oracle_calls() -> None:
    source = (ROOT / "code" / "sdc25_unary_fiber.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    calls = {
        (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, (ast.Name, ast.Attribute))
    }
    assert calls.isdisjoint(
        {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
    )


def test_e1_candidate_and_evaluator_are_separate_files() -> None:
    assert (ROOT / "code" / "sdc25_unary_fiber.py").is_file()
    assert (ROOT / "code" / "sdc25_evaluator.py").is_file()
    assert (ROOT / "code" / "sdc25_unary_fiber.py") != (ROOT / "code" / "sdc25_evaluator.py")


def test_e2_known_transformation_tail_period() -> None:
    assert transformation_tail_period((1, 2, 2), 0) == (2, 1)
    assert transformation_tail_period((1, 2, 0), 0) == (0, 3)
    assert transformation_tail_period((0, 1, 2), 0) == (0, 1)


def test_e2_exhaustive_unary_maps_periodic() -> None:
    rows, totals = exhaustive_transformation_rows()
    assert len(rows) == 288
    assert totals["unary_maps"] == 288
    assert totals["configurations"] == 1_054_474
    assert totals["periodicity_failures"] == 0
    assert all(row["eventually_periodic"] for row in rows)


def test_e2_boolean_relation_semigroup_periodic() -> None:
    rows, totals = exhaustive_boolean_relation_rows(2)
    assert len(rows) == 16
    assert totals["configurations"] == 1024
    assert totals["periodicity_failures"] == 0
    assert all(row["eventually_periodic"] for row in rows)


def test_e2_group_and_non_group_controls_present() -> None:
    rows = algebraic_control_rows()
    assert sum(row["family"] == "cyclic_group" for row in rows) == 7
    assert sum(row["family"] == "non_group_semigroup" for row in rows) == 4
    assert all(row["eventually_periodic"] for row in rows)


def test_e3_constructive_composites_share_response() -> None:
    rows = constructive_composite_witnesses()
    assert len(rows) == 11
    assert all(row["same_residue"] and row["same_response"] for row in rows)
    assert all(row["composite_verified"] for row in rows)
    assert all(not row["candidate_used_target_predicate"] for row in rows)


def test_e4_all_fixture_dimensions_and_cases() -> None:
    fixtures = deterministic_matrix_fixtures()
    assert len(fixtures) == 48
    assert {fixture["dimension"] for fixture in fixtures} == set(range(1, 9))
    assert len({fixture["case"] for fixture in fixtures}) == 6


def test_e4_cayley_hamilton_exact() -> None:
    for fixture in deterministic_matrix_fixtures():
        assert matrix_is_zero(cayley_hamilton_matrix(fixture["A"]))


def test_e4_bilinear_and_trace_residuals_exact() -> None:
    for fixture in deterministic_matrix_fixtures():
        dimension = fixture["dimension"]
        coefficients = characteristic_coefficients(fixture["A"])
        bilinear, traces = response_sequences(
            fixture["A"], fixture["B"], fixture["u"], fixture["v"], 4 * dimension + 16
        )
        assert set(recurrence_residuals(bilinear, coefficients)) <= {Fraction(0)}
        assert set(recurrence_residuals(traces, coefficients)) <= {Fraction(0)}


def test_e4_rational_generating_functions_exact() -> None:
    for fixture in deterministic_matrix_fixtures():
        dimension = fixture["dimension"]
        coefficients = characteristic_coefficients(fixture["A"])
        bilinear, traces = response_sequences(
            fixture["A"], fixture["B"], fixture["u"], fixture["v"], 4 * dimension + 16
        )
        for sequence in (bilinear, traces):
            numerator = generating_numerator(sequence, coefficients)
            assert generating_series_from_rational(numerator, coefficients, len(sequence)) == sequence


def test_e4_minimal_orders_do_not_exceed_dimension() -> None:
    for fixture in deterministic_matrix_fixtures():
        dimension = fixture["dimension"]
        bilinear, traces = response_sequences(
            fixture["A"], fixture["B"], fixture["u"], fixture["v"], 4 * dimension + 16
        )
        assert 0 <= minimal_recurrence_order(bilinear, dimension) <= dimension
        assert 0 <= minimal_recurrence_order(traces, dimension) <= dimension


def test_e5_all_memorizer_targets_exact() -> None:
    for cutoff in MEMORY_CUTOFFS:
        for name in TARGET_NAMES:
            target = target_vector(name, cutoff)
            assert all(memorizer_response(target, index) == target[index - 1] for index in range(1, cutoff + 1))
            assert all(memorizer_response(target, index) == 0 for index in range(cutoff + 1, cutoff + 5))


def test_e5_target_digests_are_deterministic_and_separating() -> None:
    digests = [target_digest(target_vector(name, 64)) for name in TARGET_NAMES]
    assert digests == [target_digest(target_vector(name, 64)) for name in TARGET_NAMES]
    assert len(set(digests)) == len(digests)


def test_e5_dimension_changes_with_cutoff() -> None:
    assert tuple(MEMORY_CUTOFFS) == (32, 64, 128, 256)
    assert len(set(MEMORY_CUTOFFS)) == 4


def test_e6_canonical_trace_is_cyclic() -> None:
    for fixture in block_fiber_fixtures():
        for index in range(2, 6):
            left, column = canonical_fiber_trace(index, fixture["A"], fixture["B"])
            assert left == column


def test_e6_block_power_traces_reach_period_32() -> None:
    fixture = block_fiber_fixtures()[1]
    adjacency = block_adjacency(7, fixture["A"], fixture["B"], 1)
    assert len(finite_power_traces(adjacency, BLOCK_MAX_POWER)) == 32


def test_e6_finite_block_determinant_matches_newton() -> None:
    for fixture in block_fiber_fixtures():
        adjacency = block_adjacency(7, fixture["A"], fixture["B"], 1)
        traces = finite_power_traces(adjacency, len(adjacency))
        coefficients = newton_determinant_coefficients(traces)
        for value in (Fraction(1, 7), Fraction(2, 13)):
            assert polynomial_value(coefficients, value) == fraction_determinant(
                identity_minus_scaled(adjacency, value)
            )


def test_e6_trace_zero_does_not_delete_matrix_local_factor() -> None:
    fixture = next(
        item for item in block_fiber_fixtures() if item["name"] == "trace_zero_repetition_leakage"
    )
    product_matrix = matrix_multiply(fixture["B"], matrix_power(fixture["A"], 4))
    assert matrix_trace(product_matrix) == 0
    assert matrix_trace(matrix_power(product_matrix, 2)) == 2
    coefficients = newton_determinant_coefficients(finite_power_traces(product_matrix, 2))
    assert coefficients == (Fraction(1), Fraction(0), Fraction(-1))


def test_e6_scalar_local_factor_is_linear() -> None:
    fixture = block_fiber_fixtures()[0]
    product_matrix = matrix_multiply(fixture["B"], matrix_power(fixture["A"], 3))
    coefficients = newton_determinant_coefficients(finite_power_traces(product_matrix, 1))
    assert len(coefficients) == 2
    assert coefficients[1] == -matrix_trace(product_matrix)


def test_e7_directed_intervals_are_ordered() -> None:
    for sigma in TRACE_SIGMAS:
        for family in ("successor", "return"):
            lower, upper = decimal_edge_prefix_interval(128, sigma, family)
            assert lower <= upper
            assert lower > 0


def test_e7_prefixes_increase_with_cutoff() -> None:
    for sigma in ("0.49", "0.51", "1.00"):
        for family in ("successor", "return"):
            small = decimal_edge_prefix_interval(64, sigma, family)
            large = decimal_edge_prefix_interval(128, sigma, family)
            assert large[0] >= small[0]
            assert large[1] >= small[1]


def test_e8_transient_recurrent_core_is_only_accept_loops() -> None:
    structures, _traces = transient_wrapper_rows()
    assert len(structures) == 5
    assert all(row["recurrent_core_exact"] for row in structures)
    assert all(not row["computation_edges_on_closed_walk"] for row in structures)
    assert all(not row["cemetery_edges_on_closed_walk"] for row in structures)


def test_e8_transient_full_and_pruned_traces_match() -> None:
    _structures, traces = transient_wrapper_rows()
    assert len(traces) == 40
    assert all(row["trace_match"] and row["determinant_coefficient_match"] for row in traces)


def test_e8_recurrent_padding_bound_and_marker_firewall() -> None:
    rows = recurrent_wrapper_rows()
    assert len(rows) == 40
    assert all(row["acceptance_independent_padding"] for row in rows)
    assert all(row["bound_verified"] for row in rows)
    assert all(row["disjoint_basis_witness"] for row in rows)
    assert all(row["marker_changed"] for row in rows)
    assert all(not row["candidate_used_support"] for row in rows)


def test_e8_paper19_and_20_certificates_import_cleanly() -> None:
    payload = imported_wrapper_certificates(SYMBOLIC_ROOT)
    assert payload["all_integrity_pass"]
    assert [row["candidate_id"] for row in payload["imports"]] == ["SD-C21", "SD-C22"]
    assert all(len(row["core_sha256"]) == 64 for row in payload["imports"])


def test_e9_roof_and_marker_exact_small_prefix() -> None:
    rows = roof_marker_rows(128)
    assert len(rows) == 127
    assert all(row["product_equals_factorial_ratio"] for row in rows)
    assert all(row["target_multiset_matches_sources"] for row in rows)
    assert all(row["edge_monomial_identity"] for row in rows)
    assert all(not row["marker_match"] and not row["roof_match"] for row in rows)


def test_e9_oracle_filter_is_one_dimensional_control() -> None:
    rows = roof_marker_rows(32)
    assert all(row["filter_mode"] == "one-dimensional orbit-level oracle control" for row in rows)
    assert all(not row["finite_block_trace_filter"] for row in rows)
    assert all(not row["candidate_used_target_predicate"] for row in rows)


def test_e10_route_tuple_is_frozen_in_source_lock() -> None:
    text = (ROOT / "SOURCE_LOCK.md").read_text(encoding="utf-8")
    for label in (
        "A0\\_STRUCTURAL\\_ARITHMETIC\\_RELATION",
        "A1\\_WEAK",
        "A2\\_ANALYTIC\\_DETERMINANT",
        "A3\\_FAIL",
        "A4\\_FAIL",
        "ROUTE\\_A\\_REJECTED",
    ):
        assert label in text


def test_e10_target_zero_firewall_is_frozen() -> None:
    source_lock = (ROOT / "SOURCE_LOCK.md").read_text(encoding="utf-8")
    preregistration = (ROOT / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "Target-zero data:** forbidden and unused" in source_lock
    assert "Zero-data firewall:** active" in preregistration


def test_generated_summary_contract_when_present() -> None:
    path = ROOT / "results" / "summary.json"
    if not path.exists():
        return
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["candidate_id"] == "SD-C25"
    assert payload["overall_verdict"] == "ROUTE_A_REJECTED"
    assert payload["route_b_invocation_allowed"] is False
