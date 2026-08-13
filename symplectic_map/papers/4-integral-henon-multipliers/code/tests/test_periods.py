import sympy as sp

from henon_audit.algebra import U, equal_mod_parameter
from henon_audit.periods import (
    L,
    T,
    candidate_period_record,
    exact_period_decomposition,
    multiplier_polynomial,
    rational_multiplier_polynomial,
    trace_polynomial,
)


def test_closed_trace_polynomials_match_frozen_formulas():
    assert trace_polynomial(1, U).as_expr() == T**2 - 4 * T - 4 * U
    assert trace_polynomial(2, U).as_expr() == T + 4 * U - 14
    expected = (T - (10 - 8 * U)) ** 2 - (6 - 8 * U) ** 2 * (U - 1)
    assert equal_mod_parameter(trace_polynomial(3, U).as_expr(), expected)


def test_exact_period_branch_decompositions_pass_at_integral_control():
    for period, point_count, cycle_count in ((1, 2, 2), (2, 2, 1), (3, 6, 2)):
        record = exact_period_decomposition(period, sp.Integer(0))
        assert record["exact_point_count"] == point_count
        assert record["exact_cycle_count"] == cycle_count
        assert record.get("period_separation_pass", True)


def test_candidate_multiplier_polynomials_are_reciprocal_units():
    for period in (1, 2, 3):
        over_k = multiplier_polynomial(period, U)
        over_q = rational_multiplier_polynomial(period)
        assert over_k.LC() == over_k.TC() == 1
        assert over_q.LC() == over_q.TC() == 1
        assert sp.expand(L ** over_q.degree() * over_q.as_expr().subs(L, 1 / L) - over_q.as_expr()) == 0


def test_candidate_period_records_have_no_rational_multiplier_roots():
    for period in (1, 2, 3):
        record = candidate_period_record(period)
        assert record["rational_multiplier_audit"]["exact_rational_roots"] == []

