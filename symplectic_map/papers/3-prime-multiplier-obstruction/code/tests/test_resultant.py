import sympy as sp

from prime_multiplier.algebra import candidate_field
from prime_multiplier.controls import quadratic_map
from prime_multiplier.resultant import (
    chain_rule_multiplier,
    classify_rational_multiplier,
    derivative_multiplier,
    multiplier_certificate,
    rational_roots_in_field_polynomial,
)


def test_chain_rule_and_full_iterate_derivative_agree():
    base = quadratic_map(sp.Rational(-2))
    assert chain_rule_multiplier(base, 4) == derivative_multiplier(base, 4)


def test_power_map_cycle_polynomial_groups_point_multiplicity():
    certificate = multiplier_certificate(quadratic_map(sp.Rational(0)), 3)
    L = certificate.cycle_polynomial.gens[0]
    assert certificate.point_resultant == sp.Poly((L - 8) ** 6, L, domain=sp.QQ)
    assert certificate.cycle_polynomial == sp.Poly((L - 8) ** 2, L, domain=sp.QQ)
    assert certificate.perfect_cycle_power_pass
    assert certificate.quotient_annihilation_pass


def test_rational_roots_require_simultaneous_cubic_basis_vanishing():
    field = candidate_field()
    u = field.generator
    L = sp.Symbol("L")
    value = sp.Poly((L - 3) * (L - u), L, domain=field.domain)
    roots, common = rational_roots_in_field_polynomial(value, field=field)
    assert roots == (sp.Rational(3),)
    assert common == sp.Poly(L - 3, L, domain=sp.QQ)


def test_exact_rational_multiplier_classifier():
    raw = classify_rational_multiplier(sp.Rational(3), 1)
    assert raw["raw_rational_prime"]
    assert raw["exponent_prime_kind"] == "EXPONENT_PRIME_ODD"
    exponent = classify_rational_multiplier(sp.Rational(16), 4)
    assert not exponent["raw_rational_prime"]
    assert exponent["exponent_prime_kind"] == "EXPONENT_PRIME_TWO"
    composite = classify_rational_multiplier(sp.Rational(12), 2)
    assert composite["exponent_prime_kind"] == "NONE"


def test_formal_collision_yields_vacuous_unit_resultant():
    certificate = multiplier_certificate(quadratic_map(sp.Rational(-3, 4)), 2)
    assert certificate.dynatomic.exact_degree == 0
    assert certificate.point_resultant.is_one
    assert certificate.cycle_polynomial.is_one
    assert certificate.rational_candidates == ()

