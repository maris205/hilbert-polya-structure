"""Foundational exact algebra for the frozen quadratic candidate."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable

import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.domains.algebraicfield import AlgebraicField


@dataclass(frozen=True)
class CandidateField:
    """The abstract cubic field with a display alias for its generator."""

    domain: AlgebraicField
    generator: sp.AlgebraicNumber
    minimal_polynomial: sp.Poly


def candidate_parameter_polynomial(symbol: sp.Symbol | None = None) -> sp.Poly:
    """Return the frozen monic parameter polynomial over ``QQ``."""

    variable = symbol if symbol is not None else sp.Symbol("U")
    return sp.Poly(variable**3 - 2 * variable**2 + 2 * variable - 2, variable, domain=QQ)


def candidate_field() -> CandidateField:
    """Construct ``QQ[u]/(u^3-2u^2+2u-2)`` exactly.

    No floating embedding is used in coefficient arithmetic.  Root selection
    is certified separately by rational isolation and monotonicity.
    """

    polynomial = candidate_parameter_polynomial()
    domain = QQ.alg_field_from_poly(polynomial, alias="u")
    generator = domain.to_sympy(domain.unit)
    return CandidateField(domain=domain, generator=generator, minimal_polynomial=polynomial)


def polynomial(
    expression: sp.Expr,
    variable: sp.Symbol,
    *,
    domain: Any | None = None,
) -> sp.Poly:
    """Coerce an expression to a univariate exact polynomial."""

    if domain is None:
        return sp.Poly(expression, variable)
    return sp.Poly(expression, variable, domain=domain)


def iterate_polynomial(base: sp.Poly, iterate: int) -> sp.Poly:
    """Return the exact ``iterate``-fold composition of a univariate map."""

    if iterate < 0:
        raise ValueError("iterate must be nonnegative")
    variable = base.gens[0]
    current = sp.Poly(variable, variable, domain=base.domain)
    for _ in range(iterate):
        current = current.compose(base)
    return current


def exact_equal(left: sp.Poly | sp.Expr, right: sp.Poly | sp.Expr) -> bool:
    """Test exact equality without numerical evaluation."""

    if isinstance(left, sp.Poly) and isinstance(right, sp.Poly):
        try:
            return left.unify(right)[0] == left.unify(right)[1]
        except Exception:
            return sp.expand(left.as_expr() - right.as_expr()) == 0
    left_expr = left.as_expr() if isinstance(left, sp.Poly) else left
    right_expr = right.as_expr() if isinstance(right, sp.Poly) else right
    return sp.simplify(left_expr - right_expr) == 0


def _rational_string(value: Any) -> str:
    rational = sp.Rational(value)
    return str(rational)


def algebraic_coefficient_basis(
    coefficient: sp.Expr,
    field: CandidateField,
) -> list[str]:
    """Serialize a cubic-field coefficient in the basis ``1,u,u^2``."""

    element = field.domain.from_sympy(coefficient)
    descending = list(element.to_list())
    padded = [field.domain.dom.zero] * (3 - len(descending)) + descending
    ascending = list(reversed(padded))
    return [_rational_string(item) for item in ascending]


def serialize_polynomial(
    value: sp.Poly,
    *,
    field: CandidateField | None = None,
) -> dict[str, Any]:
    """Return a deterministic JSON-compatible exact polynomial record."""

    coefficients = [sp.sstr(item) for item in value.all_coeffs()]
    payload: dict[str, Any] = {
        "variable": str(value.gens[0]),
        "degree": int(value.degree()) if not value.is_zero else None,
        "domain": str(value.domain),
        "expression": sp.sstr(value.as_expr()),
        "coefficients_descending": coefficients,
    }
    if field is not None:
        payload["coefficient_basis"] = "1,u,u^2"
        payload["coefficients_basis_descending"] = [
            algebraic_coefficient_basis(item, field) for item in value.all_coeffs()
        ]
        payload["parameter_relation"] = "u^3-2*u^2+2*u-2=0"
    return payload


def rational_from_string(value: str) -> sp.Rational:
    """Parse an internally serialized rational without accepting floats."""

    fraction = Fraction(value)
    return sp.Rational(fraction.numerator, fraction.denominator)


def product(values: Iterable[sp.Expr]) -> sp.Expr:
    """Exact multiplicative fold."""

    result = sp.Integer(1)
    for value in values:
        result *= value
    return sp.expand(result)

