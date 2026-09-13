"""Exact m=2 route tests; no registered coefficient evaluator is invoked."""

from __future__ import annotations

import copy

import pytest

from bootstrap.protocol import load_exact_json
from bootstrap.runner import _validate_private_quartic
from conftest import CANDIDATE_ROOT


def test_q_complete_quotient_route(q_engine):
    witness = q_engine.quartic_quotient_witness()
    assert witness["route"] == "STANDARD_MONOMIAL_MULTIPLICATION_TRACE"
    assert witness["standard_basis_count"] == 64
    assert witness["trace_polynomial"] == [
        {"exponent": 0, "coefficient": -1296000},
        {"exponent": 3, "coefficient": -1572864},
    ]
    elimination = witness["general_quartic_trace_elimination"]
    assert elimination["classification_condition"] == "p_divides_derivative_squared"
    assert elimination["first_eliminated_variable"] == "c"
    assert elimination["first_pivot_coefficient"] == -8
    assert elimination["derivative_square_remainder"] == [
        [{"b_exponent": 0, "c_exponent": 2, "d_exponent": 0, "coefficient": 1}],
        [{"b_exponent": 1, "c_exponent": 1, "d_exponent": 0, "coefficient": 4}],
        [
            {"b_exponent": 0, "c_exponent": 0, "d_exponent": 1, "coefficient": -16},
            {"b_exponent": 2, "c_exponent": 0, "d_exponent": 0, "coefficient": 4},
        ],
        [{"b_exponent": 0, "c_exponent": 1, "d_exponent": 0, "coefficient": -8}],
    ]
    low = witness["low_period_and_fixed_moment"]
    assert low["fixed_basis_count"] == 4
    assert low["period_two_ambient_basis_count"] == 16
    assert low["period_two_exact_basis_count"] == 12
    assert low["fixed_trace_square_remainder"] == []
    assert [(row["root_multiplicity"], row["remaining_order"]) for row in witness["local_fixed_series"]] == [
        (2, 2),
        (4, 4),
    ]


def test_r_complete_residue_route(r_engine):
    witness = r_engine.quartic_residue_witness()
    assert witness["route"] == "NORMALIZED_GLOBAL_RESIDUE_AND_ROOT_PARTITIONS"
    assert witness["tensor_laurent_components"] == [
        {"component_index": 0, "coefficient": -6},
        {"component_index": 1, "coefficient": 0},
        {"component_index": 2, "coefficient": 0},
    ]
    assert witness["constant_top_coefficient"] == -1296000
    assert witness["direct_slope"] == -1572864
    low = witness["low_period"]
    assert low["p_minus_h_square_remainder"] == []
    assert low["q_minus_4x_h_remainder"] == []
    assert [case["root_partition"] for case in low["partition_cases"]] == [[2, 2], [4]]
    assert all(
        all(remainder == [] for remainder in case["support_q_remainders"])
        for case in low["partition_cases"]
    )
    assert low["fixed_length"] == 4
    assert low["period_two_ambient_length"] == 16
    assert low["period_two_exact_length"] == 12
    assert witness["fixed_moment"]["trace_square_factorization_remainder"] == []
    assert [(row["root_multiplicity"], row["remaining_order"]) for row in witness["local_fixed_orders"]] == [
        (2, 2),
        (4, 4),
    ]


def test_step10_and_step13_are_separate_records(q_engine, r_engine):
    q = q_engine.quartic_quotient_witness()
    r = r_engine.quartic_residue_witness()
    assert "fixed_trace_square_remainder" in q["low_period_and_fixed_moment"]
    assert "remaining_order" not in q["low_period_and_fixed_moment"]
    assert all("fixed_trace_square_remainder" not in row for row in q["local_fixed_series"])
    assert "fixed_moment" in r and "local_fixed_orders" in r
    assert "remaining_order" not in r["fixed_moment"]
    assert all("fixed_moment" not in row for row in r["local_fixed_orders"])


def test_unilateral_quartic_mutation_breaks_private_ledger_agreement(q_engine, r_engine):
    expected = load_exact_json(
        CANDIDATE_ROOT / "adjudicator/acceptance_ledger.json"
    )["quartic_expected"]
    q_witness = q_engine.quartic_quotient_witness()
    q_public = q_engine._q_public_quartic_record(q_witness["trace_polynomial"], q_witness)
    r_witness = r_engine.quartic_residue_witness()
    r_public = r_engine._r_public_quartic_record(
        r_witness["constant_top_coefficient"], r_witness["direct_slope"], r_witness
    )
    assert q_public == expected
    assert r_public == expected
    mutated_q = copy.deepcopy(q_public)
    mutated_q["pointwise_moment"]["terms"][1]["coefficient"] += 1
    assert mutated_q != expected
    assert r_public == expected
    mutated_r = copy.deepcopy(r_public)
    mutated_r["fixed_length"] += 1
    assert mutated_r != expected
    assert q_public == expected


def test_step10_step13_and_normalization_negative_mutations_reject(q_engine, r_engine):
    q = q_engine.quartic_quotient_witness()
    missing_local = copy.deepcopy(q)
    missing_local["local_fixed_series"] = []
    with pytest.raises(RuntimeError, match="Step13"):
        _validate_private_quartic(missing_local, "Q")
    wrong_order = copy.deepcopy(q)
    wrong_order["local_fixed_series"][0]["remaining_order"] = 3
    with pytest.raises(RuntimeError, match="Step13"):
        _validate_private_quartic(wrong_order, "Q")
    r = r_engine.quartic_residue_witness()
    reduced_support_only = copy.deepcopy(r)
    reduced_support_only["low_period"]["period_two_exact_length"] = 16
    with pytest.raises(RuntimeError, match="low-period"):
        _validate_private_quartic(reduced_support_only, "R")
    expected = load_exact_json(
        CANDIDATE_ROOT / "adjudicator/acceptance_ledger.json"
    )["quartic_expected"]
    premature_division = copy.deepcopy(expected)
    premature_division["pointwise_moment"] = copy.deepcopy(expected["cyclewise_moment"])
    assert premature_division != expected
