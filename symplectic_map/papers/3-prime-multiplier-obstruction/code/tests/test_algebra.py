import sympy as sp

from prime_multiplier.algebra import (
    algebraic_coefficient_basis,
    candidate_field,
    candidate_parameter_polynomial,
    iterate_polynomial,
    serialize_polynomial,
)


def test_parameter_polynomial_is_monic_irreducible_cubic():
    polynomial = candidate_parameter_polynomial()
    assert polynomial.degree() == 3
    assert polynomial.LC() == 1
    assert polynomial.is_irreducible


def test_candidate_generator_satisfies_parameter_relation():
    field = candidate_field()
    u = field.generator
    assert field.domain.from_sympy(u**3 - 2 * u**2 + 2 * u - 2) == field.domain.zero


def test_iterate_polynomial_zero_and_three_steps():
    z = sp.Symbol("z")
    base = sp.Poly(z**2 - 2, z, domain=sp.QQ)
    assert iterate_polynomial(base, 0) == sp.Poly(z, z, domain=sp.QQ)
    third = iterate_polynomial(base, 3)
    assert third.degree() == 8
    assert third == base.compose(base).compose(base)


def test_iterate_rejects_negative_count():
    z = sp.Symbol("z")
    base = sp.Poly(z**2, z, domain=sp.QQ)
    try:
        iterate_polynomial(base, -1)
    except ValueError as error:
        assert "nonnegative" in str(error)
    else:
        raise AssertionError("negative iterate was accepted")


def test_cubic_basis_serialization_is_ascending():
    field = candidate_field()
    u = field.generator
    assert algebraic_coefficient_basis(1 + 2 * u + 3 * u**2, field) == ["1", "2", "3"]


def test_polynomial_serialization_includes_parameter_relation():
    field = candidate_field()
    L = sp.Symbol("L")
    value = sp.Poly(L**2 + field.generator * L + 1, L, domain=field.domain)
    record = serialize_polynomial(value, field=field)
    assert record["degree"] == 2
    assert record["coefficient_basis"] == "1,u,u^2"
    assert record["coefficients_basis_descending"] == [["1", "0", "0"], ["0", "1", "0"], ["1", "0", "0"]]

