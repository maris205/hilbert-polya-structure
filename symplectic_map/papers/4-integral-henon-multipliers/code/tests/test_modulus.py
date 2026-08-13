import sympy as sp

from henon_audit.modulus import (
    MU,
    candidate_modulus_audit,
    candidate_trace_intervals,
    complex_trace_modulus_polynomial,
    exact_positive_rational_square_root,
    hyperbolic_modulus_resultant,
    RationalBounds,
    _exact_hyperbolic_record,
)


def test_trace_intervals_certify_one_elliptic_and_four_hyperbolic_cycles():
    intervals = candidate_trace_intervals()
    assert -2 < intervals["period_1_minus"].lower < intervals["period_1_minus"].upper < 2
    for label in (
        "period_1_plus",
        "period_2",
        "period_3_b_positive",
        "period_3_b_negative",
    ):
        interval = intervals[label]
        assert interval.upper < -2 or interval.lower > 2


def test_real_hyperbolic_modulus_relation_is_reciprocal():
    T = sp.Symbol("T")
    poly = hyperbolic_modulus_resultant(sp.Poly(T - 4, T, domain=sp.QQ))
    assert poly == sp.Poly(MU**2 - 14 * MU + 1, MU, domain=sp.QQ)


def test_nonreal_trace_modulus_polynomial_is_exact():
    poly = complex_trace_modulus_polynomial(sp.Rational(10), sp.Rational(6))
    assert poly == sp.Poly(MU**4 - 136 * MU**3 + 126 * MU**2 - 136 * MU + 1, MU, domain=sp.QQ)
    assert poly.is_irreducible


def test_generic_hyperbolic_pipeline_performs_exact_rational_square_test():
    T = sp.Symbol("T")
    record = _exact_hyperbolic_record(
        label="trace_5_over_2_regression",
        trace_poly=sp.Poly(T - sp.Rational(5, 2), T, domain=sp.QQ),
        trace_interval=RationalBounds(sp.Rational(249, 100), sp.Rational(251, 100)),
        declared_bad_primes=(2,),
    )
    assert record["rational_modulus_values"] == ["1/2", "2"]
    assert all(
        item["rational_modulus_classification"] == "RATIONAL_MODULUS_S_UNIT"
        for item in record["multiplier_modulus_squared_records"]
    )
    assert exact_positive_rational_square_root(sp.Rational(4, 9)) == sp.Rational(2, 3)
    assert exact_positive_rational_square_root(sp.Rational(2)) is None


def test_candidate_exact_rational_modulus_set_is_only_one():
    result = candidate_modulus_audit()
    assert result["cycle_count_audited"] == 5
    assert result["exact_rational_modulus_set"] == ["1"]
    assert result["raw_rational_prime_modulus_count"] == 0
    assert result["unresolved_square_test_classifications"] == []
