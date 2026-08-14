import sympy as sp

from henon_audit.algebra import (
    PARAMETER_POLYNOMIAL,
    U,
    equal_mod_parameter,
    norm_over_parameter,
    parameter_basis,
    reduce_parameter,
)


def test_frozen_parameter_polynomial_is_monic_irreducible_cubic():
    assert PARAMETER_POLYNOMIAL.degree() == 3
    assert PARAMETER_POLYNOMIAL.LC() == 1
    assert PARAMETER_POLYNOMIAL.is_irreducible


def test_parameter_reduction_uses_basis_one_u_u_squared():
    assert reduce_parameter(U**3) == 2 * U**2 - 2 * U + 2
    assert parameter_basis(U**3) == ["2", "-2", "2"]
    assert equal_mod_parameter(PARAMETER_POLYNOMIAL.as_expr())


def test_resultant_norm_is_exact_and_monic():
    z = sp.Symbol("z")
    norm = norm_over_parameter(z - U, z)
    assert norm == sp.Poly(z**3 - 2 * z**2 + 2 * z - 2, z, domain=sp.QQ)

