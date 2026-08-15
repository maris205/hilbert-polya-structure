"""Exact algebra for the frozen cubic field and quadratic maps."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.domains.algebraicfield import AlgebraicField


@dataclass(frozen=True)
class CandidateField:
    """The abstract field ``Q[u]/(u^3-2u^2+2u-2)``."""

    domain: AlgebraicField
    generator: sp.AlgebraicNumber
    minimal_polynomial: sp.Poly


def parameter_polynomial(symbol: sp.Symbol | None = None) -> sp.Poly:
    """Return the frozen monic cubic over the rationals."""

    variable = symbol if symbol is not None else sp.Symbol("U")
    return sp.Poly(
        variable**3 - 2 * variable**2 + 2 * variable - 2,
        variable,
        domain=QQ,
    )


def candidate_field() -> CandidateField:
    """Construct the frozen cubic field without choosing a floating embedding."""

    minimal = parameter_polynomial()
    domain = QQ.alg_field_from_poly(minimal, alias="u")
    generator = domain.to_sympy(domain.unit)
    return CandidateField(domain=domain, generator=generator, minimal_polynomial=minimal)


def candidate_map(field: CandidateField | None = None) -> tuple[CandidateField, sp.Poly]:
    """Return ``g(z)=z^2-u`` over the frozen exact field."""

    selected = field if field is not None else candidate_field()
    z = sp.Symbol("z")
    return selected, sp.Poly(z**2 - selected.generator, z, domain=selected.domain)


def quadratic_map(parameter: sp.Rational | int, variable: sp.Symbol | None = None) -> sp.Poly:
    """Return ``z^2+c`` over ``QQ`` for an exact rational parameter."""

    z = variable if variable is not None else sp.Symbol("z")
    return sp.Poly(z**2 + sp.Rational(parameter), z, domain=QQ)


def iterate_polynomial(base: sp.Poly, iterate: int) -> sp.Poly:
    """Return an exact polynomial iterate, with iterate zero equal to identity."""

    if type(iterate) is not int or iterate < 0:
        raise ValueError("iterate must be a nonnegative integer")
    variable = base.gens[0]
    current = sp.Poly(variable, variable, domain=base.domain)
    for _ in range(iterate):
        current = current.compose(base)
    return current


def product(values: Iterable[sp.Poly], *, identity: sp.Poly) -> sp.Poly:
    """Multiply exact polynomials in a fixed domain."""

    result = identity
    for value in values:
        result *= value
    return result


def algebraic_element_basis(element: Any, field: CandidateField) -> tuple[sp.Rational, ...]:
    """Return coefficients in the ascending basis ``1,u,u^2``."""

    converted = field.domain.convert(element)
    descending = list(converted.to_list())
    padded = [field.domain.dom.zero] * (3 - len(descending)) + descending
    return tuple(sp.Rational(item) for item in reversed(padded))


def algebraic_field_norm(element: Any, field: CandidateField) -> sp.Rational:
    """Compute ``N_{Q(u)/Q}(element)`` by an exact rational resultant."""

    coefficients = algebraic_element_basis(element, field)
    U = field.minimal_polynomial.gens[0]
    representative = sp.Poly(
        sum(coefficient * U**index for index, coefficient in enumerate(coefficients)),
        U,
        domain=QQ,
    )
    return sp.Rational(field.minimal_polynomial.resultant(representative))


def serialize_element(element: Any, field: CandidateField | None = None) -> dict[str, Any]:
    """Serialize an exact coefficient without decimal conversion."""

    if field is None:
        rational = sp.Rational(element)
        return {"domain": "QQ", "value": str(rational)}
    basis = algebraic_element_basis(element, field)
    return {
        "domain": "QQ<u>",
        "basis": "1,u,u^2",
        "coefficients_ascending": [str(value) for value in basis],
        "expression": sp.sstr(field.domain.to_sympy(field.domain.convert(element))),
    }


def serialize_polynomial(value: sp.Poly, field: CandidateField | None = None) -> dict[str, Any]:
    """Serialize all coefficients of an exact univariate polynomial."""

    payload: dict[str, Any] = {
        "variable": str(value.gens[0]),
        "domain": str(value.domain),
        "degree": int(value.degree()) if not value.is_zero else None,
        "coefficients_descending": [sp.sstr(item) for item in value.all_coeffs()],
    }
    if field is not None:
        payload["coefficient_basis"] = "1,u,u^2"
        payload["coefficients_basis_descending"] = [
            [str(item) for item in algebraic_element_basis(coefficient, field)]
            for coefficient in value.all_coeffs()
        ]
    return payload
