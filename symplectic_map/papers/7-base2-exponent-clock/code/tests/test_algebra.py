import sympy as sp

from base2_clock.algebra import (
    algebraic_element_basis,
    algebraic_field_norm,
    candidate_field,
    iterate_polynomial,
    parameter_polynomial,
    quadratic_map,
)


def test_frozen_cubic_relation_and_norm_of_uniformizer():
    field = candidate_field()
    u = field.generator
    assert field.domain.from_sympy(parameter_polynomial().as_expr().subs({sp.Symbol("U"): u})) == field.domain.zero
    assert algebraic_element_basis(u, field) == (0, 1, 0)
    assert algebraic_field_norm(field.domain.from_sympy(u), field) == 2


def test_iterate_polynomial_is_exact_and_zero_iterate_is_identity():
    base = quadratic_map(sp.Rational(-3, 4))
    z = base.gens[0]
    assert iterate_polynomial(base, 0) == sp.Poly(z, z, domain=sp.QQ)
    assert iterate_polynomial(base, 2) == base.compose(base)


def test_iterate_rejects_noninteger_or_negative_count():
    base = quadratic_map(0)
    for bad in (-1, sp.Rational(1, 2)):
        try:
            iterate_polynomial(base, bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid iterate was accepted")
