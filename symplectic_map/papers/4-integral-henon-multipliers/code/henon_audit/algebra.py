"""Deterministic exact-algebra helpers for the frozen cubic parameter."""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Iterable

import sympy as sp

U = sp.Symbol("u")
PARAMETER_POLYNOMIAL = sp.Poly(U**3 - 2 * U**2 + 2 * U - 2, U, domain=sp.QQ)
ROOT_LOWER = sp.Rational(3859, 2500)
ROOT_UPPER = sp.Rational(15437, 10000)


def reduce_parameter(expression: sp.Expr) -> sp.Expr:
    """Reduce an expression in ``u`` to the frozen basis ``1,u,u^2``."""

    numerator, denominator = sp.cancel(expression).as_numer_denom()
    numerator_reduced = sp.rem(sp.Poly(numerator, U, domain=sp.QQ), PARAMETER_POLYNOMIAL).as_expr()
    denominator_reduced = sp.rem(
        sp.Poly(denominator, U, domain=sp.QQ), PARAMETER_POLYNOMIAL
    ).as_expr()
    if denominator_reduced == 1:
        return sp.expand(numerator_reduced)
    # All coefficient arithmetic in this project is polynomial in u.  Keep
    # the general branch exact, but fail if a denominator is zero in K.
    inverse = sp.invert(
        sp.Poly(denominator_reduced, U, domain=sp.QQ), PARAMETER_POLYNOMIAL
    )
    return sp.rem(
        sp.Poly(numerator_reduced * inverse.as_expr(), U, domain=sp.QQ),
        PARAMETER_POLYNOMIAL,
    ).as_expr()


def equal_mod_parameter(left: sp.Expr, right: sp.Expr = sp.Integer(0)) -> bool:
    """Return exact equality in ``Q[u]/(P(u))``."""

    return sp.expand(reduce_parameter(left - right)) == 0


def parameter_basis(expression: sp.Expr) -> list[str]:
    """Serialize a coefficient in the ascending basis ``1,u,u^2``."""

    reduced = sp.Poly(reduce_parameter(expression), U, domain=sp.QQ)
    return [str(reduced.nth(index)) for index in range(3)]


def polynomial_record(
    expression: sp.Expr | sp.Poly,
    variable: sp.Symbol,
    *,
    coefficient_field: str = "QQ",
) -> dict[str, Any]:
    """Create a deterministic JSON-compatible exact polynomial record."""

    expr = expression.as_expr() if isinstance(expression, sp.Poly) else expression
    if coefficient_field == "QQ[u]/P":
        poly = sp.Poly(expr, variable, domain=sp.QQ.frac_field(U))
        coefficient_basis = [parameter_basis(value) for value in poly.all_coeffs()]
    elif coefficient_field == "QQ":
        poly = sp.Poly(expr, variable, domain=sp.QQ)
        coefficient_basis = None
    else:
        raise ValueError(f"unsupported coefficient field: {coefficient_field}")

    payload: dict[str, Any] = {
        "variable": str(variable),
        "degree": int(poly.degree()) if not poly.is_zero else None,
        "domain": coefficient_field,
        "expression": sp.sstr(sp.expand(poly.as_expr())),
        "coefficients_descending": [sp.sstr(value) for value in poly.all_coeffs()],
    }
    if coefficient_basis is not None:
        payload["parameter_relation"] = sp.sstr(PARAMETER_POLYNOMIAL.as_expr())
        payload["coefficient_basis"] = "1,u,u^2"
        payload["coefficients_basis_descending"] = coefficient_basis
    return payload


def primitive_monic(poly: sp.Poly) -> sp.Poly:
    """Normalize a nonzero rational polynomial to its monic form."""

    if poly.is_zero:
        raise ValueError("zero polynomial has no monic normalization")
    return sp.Poly(poly.monic(), *poly.gens, domain=sp.QQ)


def norm_over_parameter(expression: sp.Expr, variable: sp.Symbol) -> sp.Poly:
    """Take the resultant norm from the cubic parameter algebra to ``QQ``."""

    resultant = sp.resultant(PARAMETER_POLYNOMIAL.as_expr(), expression, U)
    return primitive_monic(sp.Poly(resultant, variable, domain=sp.QQ))


def irreducible_factors(poly: sp.Poly) -> list[sp.Poly]:
    """Return distinct monic irreducible rational factors deterministically."""

    _, factors = sp.factor_list(poly)
    return [primitive_monic(factor) for factor, _multiplicity in factors]


def rational_interval(left: str | int | Fraction, right: str | int | Fraction) -> list[str]:
    """Serialize a strict rational interval."""

    lo = sp.Rational(Fraction(left))
    hi = sp.Rational(Fraction(right))
    if not lo < hi:
        raise ValueError("interval endpoints must be increasing")
    return [str(lo), str(hi)]


def product(items: Iterable[sp.Expr]) -> sp.Expr:
    value = sp.Integer(1)
    for item in items:
        value *= item
    return sp.expand(value)

