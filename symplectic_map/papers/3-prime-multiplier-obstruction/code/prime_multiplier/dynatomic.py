"""Formal dynatomic polynomials and exact-period saturation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp

from .algebra import iterate_polynomial


@dataclass(frozen=True)
class DynatomicComponent:
    """Formal and exact-period pieces for one requested period."""

    period: int
    formal: sp.Poly
    exact: sp.Poly
    lower_period_product: sp.Poly
    removed_factors: tuple[sp.Poly, ...]

    @property
    def formal_degree(self) -> int:
        return int(self.formal.degree())

    @property
    def exact_degree(self) -> int:
        return 0 if self.exact.degree() <= 0 else int(self.exact.degree())

    @property
    def contamination_degree(self) -> int:
        return self.formal_degree - self.exact_degree

    @property
    def has_formal_period_contamination(self) -> bool:
        return self.contamination_degree > 0


def _iterate_minus_identity(base: sp.Poly, period: int) -> sp.Poly:
    variable = base.gens[0]
    identity = sp.Poly(variable, variable, domain=base.domain)
    return iterate_polynomial(base, period) - identity


def formal_dynatomic(base: sp.Poly, period: int) -> sp.Poly:
    """Compute the formal dynatomic polynomial exactly by Möbius division."""

    if period < 1:
        raise ValueError("period must be positive")
    variable = base.gens[0]
    numerator = sp.Poly(1, variable, domain=base.domain)
    denominator = sp.Poly(1, variable, domain=base.domain)
    for divisor in sp.divisors(period):
        mobius = int(sp.mobius(period // divisor))
        factor = _iterate_minus_identity(base, divisor)
        if mobius == 1:
            numerator *= factor
        elif mobius == -1:
            denominator *= factor
    quotient, remainder = numerator.div(denominator)
    if not remainder.is_zero:
        raise ArithmeticError(f"dynatomic division failed exactly for period {period}")
    return quotient.monic()


def exact_period_component(base: sp.Poly, period: int) -> DynatomicComponent:
    """Remove every lower-period root from the formal dynatomic polynomial.

    Repeated saturation is essential at root-of-unity collisions: a lower
    period root can occur in the formal dynatomic polynomial with higher
    multiplicity than in a single lower iterate equation.
    """

    formal = formal_dynatomic(base, period)
    variable = base.gens[0]
    lower_product = sp.Poly(1, variable, domain=base.domain)
    for lower_period in range(1, period):
        lower_product *= _iterate_minus_identity(base, lower_period)

    exact = formal
    removed: list[sp.Poly] = []
    while exact.degree() > 0 and lower_product.degree() > 0:
        common = sp.gcd(exact, lower_product).monic()
        if common.degree() <= 0:
            break
        exact = exact.exquo(common)
        removed.append(common)

    if exact.degree() > 0:
        exact = exact.monic()
    else:
        exact = sp.Poly(1, variable, domain=base.domain)

    return DynatomicComponent(
        period=period,
        formal=formal,
        exact=exact,
        lower_period_product=lower_product,
        removed_factors=tuple(removed),
    )


def expected_formal_degree_quadratic(period: int) -> int:
    """Generic formal dynatomic degree for a monic quadratic."""

    return int(sum(int(sp.mobius(period // divisor)) * (2**divisor) for divisor in sp.divisors(period)))


def dynatomic_summary(component: DynatomicComponent) -> dict[str, Any]:
    """Create a compact JSON-compatible degree/contamination record."""

    return {
        "period": component.period,
        "formal_degree": component.formal_degree,
        "exact_period_degree": component.exact_degree,
        "formal_contamination_degree": component.contamination_degree,
        "formal_period_contamination": component.has_formal_period_contamination,
        "removed_factor_degrees": [int(item.degree()) for item in component.removed_factors],
    }

