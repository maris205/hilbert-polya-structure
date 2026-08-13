"""Exact rational-modulus certificates for the certified complex embedding.

Floating values in this module are used only to select a root already defined
by an irreducible rational polynomial and a rational isolating interval.  A
floating value is never tested for rationality and never enters a scientific
classification.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass
from itertools import product as cartesian_product
from typing import Any

import sympy as sp

from .algebra import (
    PARAMETER_POLYNOMIAL,
    ROOT_LOWER,
    ROOT_UPPER,
    U,
    norm_over_parameter,
    polynomial_record,
    primitive_monic,
)
from .periods import T, trace_polynomial

MU = sp.Symbol("M")


@dataclass(frozen=True)
class RationalBounds:
    lower: sp.Rational
    upper: sp.Rational

    def __post_init__(self) -> None:
        if not self.lower < self.upper:
            raise ValueError("bounds must be strictly increasing")

    def add(self, other: "RationalBounds") -> "RationalBounds":
        return RationalBounds(self.lower + other.lower, self.upper + other.upper)

    def multiply(self, other: "RationalBounds") -> "RationalBounds":
        candidates = [
            left * right
            for left, right in cartesian_product(
                (self.lower, self.upper), (other.lower, other.upper)
            )
        ]
        return RationalBounds(min(candidates), max(candidates))

    def negate(self) -> "RationalBounds":
        return RationalBounds(-self.upper, -self.lower)

    def serialize(self) -> list[str]:
        return [str(self.lower), str(self.upper)]


def rational_trace_polynomial(period: int) -> sp.Poly:
    return norm_over_parameter(trace_polynomial(period, U).as_expr(), T)


def hyperbolic_modulus_resultant(trace_minpoly: sp.Poly) -> sp.Poly:
    """Eliminate a real trace from ``mu=lambda^2`` and ``det=1``.

    For a real hyperbolic trace, conjugation fixes each real multiplier, so
    ``mu=lambda*conjugate(lambda)=lambda^2`` and
    ``mu + mu^-1 = trace^2-2``.
    """

    equation = MU**2 - (T**2 - 2) * MU + 1
    resultant = sp.resultant(trace_minpoly.as_expr(), equation, T)
    return primitive_monic(sp.Poly(resultant, MU, domain=sp.QQ))


def complex_trace_modulus_polynomial(real_trace: sp.Rational, imag_trace: sp.Rational) -> sp.Poly:
    """Return the exact polynomial for ``mu=|lambda|^2`` at ``t=A+iB``.

    Writing ``lambda=r*exp(i theta)`` and ``mu=r^2`` gives

    ``A^2*mu/(mu+1)^2 + B^2*mu/(mu-1)^2 = 1``.

    Clearing denominators yields the exact reciprocal polynomial below.
    Its roots at ``mu=1`` are checked separately when a denominator vanishes.
    """

    A = sp.Rational(real_trace)
    B = sp.Rational(imag_trace)
    expression = (
        A**2 * MU * (MU - 1) ** 2
        + B**2 * MU * (MU + 1) ** 2
        - (MU**2 - 1) ** 2
    )
    return primitive_monic(sp.Poly(expression, MU, domain=sp.QQ))


def _factor_intervals(poly: sp.Poly) -> list[tuple[sp.Poly, tuple[sp.Rational, sp.Rational]]]:
    records: list[tuple[sp.Poly, tuple[sp.Rational, sp.Rational]]] = []
    for factor, _multiplicity in sp.factor_list(poly)[1]:
        normalized = primitive_monic(factor)
        for interval, _root_multiplicity in normalized.intervals(eps=sp.Rational(1, 10**12)):
            left, right = map(sp.Rational, interval)
            records.append((normalized, (left, right)))
    return records


def _select_root(poly: sp.Poly, approximate: float) -> tuple[sp.Poly, tuple[sp.Rational, sp.Rational]]:
    """Select an exact isolated root using a display-only approximation."""

    target = sp.Rational(str(approximate))
    matches = [
        item for item in _factor_intervals(poly) if item[1][0] < target < item[1][1]
    ]
    if len(matches) != 1:
        # The interval routine can put a target on a rational endpoint after
        # decimal rounding.  Nearest-midpoint selection is deterministic and
        # is followed by the exact interval in the returned certificate.
        candidates = _factor_intervals(poly)
        candidates.sort(key=lambda item: abs(float((item[1][0] + item[1][1]) / 2) - approximate))
        if not candidates:
            raise RuntimeError("no real root interval found")
        matches = [candidates[0]]
    return matches[0]


def _mu_approximations_from_real_trace(trace_value: float) -> tuple[float, float]:
    discriminant = trace_value * trace_value - 4.0
    if discriminant <= 0:
        raise ValueError("real-hyperbolic modulus requested for a nonhyperbolic trace")
    root = discriminant**0.5
    multipliers = ((trace_value + root) / 2.0, (trace_value - root) / 2.0)
    squared = sorted(value * value for value in multipliers)
    return squared[0], squared[1]


def exact_positive_rational_square_root(value: sp.Rational) -> sp.Rational | None:
    """Return ``sqrt(value)`` iff it is a positive rational number."""

    rational = sp.Rational(value)
    if rational <= 0:
        return None
    numerator_root, numerator_exact = sp.integer_nthroot(int(rational.p), 2)
    denominator_root, denominator_exact = sp.integer_nthroot(int(rational.q), 2)
    if not (numerator_exact and denominator_exact):
        return None
    return sp.Rational(numerator_root, denominator_root)


def rational_prime_support(value: sp.Rational) -> list[int]:
    """Factor one internally derived exact rational value."""

    rational = abs(sp.Rational(value))
    support = set(sp.factorint(int(rational.p))) | set(sp.factorint(int(rational.q)))
    return sorted(int(prime) for prime in support)


def _rational_modulus_classification(
    modulus: sp.Rational, declared_bad_primes: tuple[int, ...]
) -> str:
    if modulus == 1:
        return "RATIONAL_MODULUS_UNIT"
    support = set(rational_prime_support(modulus))
    if support.issubset(declared_bad_primes):
        return "RATIONAL_MODULUS_S_UNIT"
    return "RATIONAL_MODULUS_OUTSIDE_DECLARED_SUPPORT"


def _exact_hyperbolic_record(
    *,
    label: str,
    trace_poly: sp.Poly,
    trace_interval: RationalBounds,
    declared_bad_primes: tuple[int, ...] = (),
) -> dict[str, Any]:
    if not (trace_interval.upper < -2 or trace_interval.lower > 2):
        raise ValueError("the rational trace interval does not certify hyperbolicity")
    trace_midpoint = float((trace_interval.lower + trace_interval.upper) / 2)
    modulus_poly = hyperbolic_modulus_resultant(trace_poly)
    approximations = _mu_approximations_from_real_trace(trace_midpoint)
    roots = []
    rational_moduli: list[sp.Rational] = []
    for role, approximation in zip(("contracting", "expanding"), approximations, strict=True):
        factor, interval = _select_root(modulus_poly, approximation)
        rational_mu = -factor.TC() if factor.degree() == 1 else None
        rational_modulus = (
            exact_positive_rational_square_root(sp.Rational(rational_mu))
            if rational_mu is not None
            else None
        )
        if rational_modulus is not None:
            rational_moduli.append(rational_modulus)
            classification = _rational_modulus_classification(
                rational_modulus, declared_bad_primes
            )
        elif rational_mu is not None:
            classification = "RATIONAL_MU_BUT_IRRATIONAL_MODULUS"
        else:
            classification = "ALGEBRAIC_UNIT_IRRATIONAL_MODULUS"
        record = {
            "role": role,
            "mu_definition": "mu=lambda*complex_conjugate(lambda)=lambda^2",
            "minimal_polynomial": polynomial_record(factor, MU),
            "minimal_polynomial_irreducible_over_Q": bool(factor.is_irreducible),
            "minimal_polynomial_degree": factor.degree(),
            "isolating_interval": [str(interval[0]), str(interval[1])],
            "display_approximation_only": f"{approximation:.12g}",
            "exact_rational_mu": factor.degree() == 1,
            "exact_rational_mu_value": str(rational_mu) if rational_mu is not None else None,
            "exact_positive_rational_modulus": (
                str(rational_modulus) if rational_modulus is not None else None
            ),
            "rational_modulus_classification": classification,
        }
        roots.append(
            record
        )
    return {
        "cycle_label": label,
        "trace_minimal_polynomial": polynomial_record(trace_poly, T),
        "trace_isolating_interval": trace_interval.serialize(),
        "trace_type": "REAL_HYPERBOLIC",
        "joint_exact_relation": "M^2-(T^2-2)*M+1=0",
        "modulus_squared_elimination_polynomial": polynomial_record(modulus_poly, MU),
        "multiplier_modulus_squared_records": roots,
        "declared_bad_prime_support": list(declared_bad_primes),
        "rational_modulus_values": [
            str(value) for value in sorted(set(rational_moduli))
        ],
    }


def candidate_trace_intervals() -> dict[str, RationalBounds]:
    """Certified rational bounds for every cycle at the chosen real root."""

    # sqrt(1+u) is strictly between 797/500 and 319/200 because the
    # corresponding squares bracket 1+[ROOT_LOWER,ROOT_UPPER].
    fixed_sqrt = RationalBounds(sp.Rational(797, 500), sp.Rational(319, 200))
    fixed_plus = RationalBounds(2 + 2 * fixed_sqrt.lower, 2 + 2 * fixed_sqrt.upper)
    fixed_minus = RationalBounds(2 - 2 * fixed_sqrt.upper, 2 - 2 * fixed_sqrt.lower)

    period_two = RationalBounds(14 - 4 * ROOT_UPPER, 14 - 4 * ROOT_LOWER)

    # sqrt(u-1) is bracketed by 737/1000 and 369/500.
    b_positive = RationalBounds(sp.Rational(737, 1000), sp.Rational(369, 500))
    center = RationalBounds(10 - 8 * ROOT_UPPER, 10 - 8 * ROOT_LOWER)
    slope = RationalBounds(6 - 8 * ROOT_UPPER, 6 - 8 * ROOT_LOWER)
    b_negative = b_positive.negate()
    period_three_b_positive = center.add(slope.multiply(b_positive))
    period_three_b_negative = center.add(slope.multiply(b_negative))

    return {
        "period_1_plus": fixed_plus,
        "period_1_minus": fixed_minus,
        "period_2": period_two,
        "period_3_b_positive": period_three_b_positive,
        "period_3_b_negative": period_three_b_negative,
    }


def candidate_modulus_audit() -> dict[str, Any]:
    """Audit every exact cycle through period three in the fixed embedding."""

    intervals = candidate_trace_intervals()
    trace_polys = {period: rational_trace_polynomial(period) for period in (1, 2, 3)}

    plus = _exact_hyperbolic_record(
        label="period_1_fixed_plus",
        trace_poly=trace_polys[1],
        trace_interval=intervals["period_1_plus"],
    )

    elliptic_interval = intervals["period_1_minus"]
    if not (-2 < elliptic_interval.lower < elliptic_interval.upper < 2):
        raise AssertionError("fixed-minus trace interval must certify ellipticity")
    minus = {
        "cycle_label": "period_1_fixed_minus",
        "trace_minimal_polynomial": polynomial_record(trace_polys[1], T),
        "trace_isolating_interval": elliptic_interval.serialize(),
        "trace_type": "REAL_ELLIPTIC",
        "conjugation_certificate": "nonreal roots of L^2-TL+1 are complex conjugates and have product 1",
        "multiplier_modulus_squared_records": [
            {
                "role": "both_conjugate_multipliers",
                "mu_definition": "mu=lambda*complex_conjugate(lambda)=1",
                "minimal_polynomial": polynomial_record(sp.Poly(MU - 1, MU), MU),
                "minimal_polynomial_irreducible_over_Q": True,
                "minimal_polynomial_degree": 1,
                "isolating_interval": ["1", "1"],
                "exact_rational_mu": True,
                "exact_positive_rational_modulus": "1",
                "rational_modulus_classification": "RATIONAL_MODULUS_UNIT",
            }
        ],
        "rational_modulus_values": ["1"],
    }

    records = [
        plus,
        minus,
        _exact_hyperbolic_record(
            label="period_2_unique_cycle",
            trace_poly=trace_polys[2],
            trace_interval=intervals["period_2"],
        ),
        _exact_hyperbolic_record(
            label="period_3_b_positive",
            trace_poly=trace_polys[3],
            trace_interval=intervals["period_3_b_positive"],
        ),
        _exact_hyperbolic_record(
            label="period_3_b_negative",
            trace_poly=trace_polys[3],
            trace_interval=intervals["period_3_b_negative"],
        ),
    ]
    rational_values = sorted(
        {sp.Rational(value) for record in records for value in record["rational_modulus_values"]}
    )
    unresolved = [
        root["rational_modulus_classification"]
        for record in records
        for root in record["multiplier_modulus_squared_records"]
        if "REQUIRES" in root["rational_modulus_classification"]
    ]
    raw_prime_moduli = [
        value
        for value in rational_values
        if value.q == 1 and value > 1 and bool(sp.isprime(int(value)))
    ]
    return {
        "embedding": "u is the unique real root in (3859/2500,15437/10000)",
        "cycle_count_audited": len(records),
        "periods": [1, 2, 3],
        "classification_rule": "mu is rational only when its exact irreducible minimal polynomial has degree one; q=sqrt(mu) is rational only after an exact rational-square test",
        "floating_policy": "display approximations select already isolated algebraic roots and never classify rationality",
        "cycles": records,
        "exact_rational_modulus_set": [str(value) for value in rational_values],
        "raw_rational_prime_moduli": [str(value) for value in raw_prime_moduli],
        "raw_rational_prime_modulus_count": len(raw_prime_moduli),
        "unresolved_square_test_classifications": unresolved,
        "all_period_conclusion_source": "PROOF_PACKAGE.md, not this finite audit",
    }


def complex_control_modulus_records(
    real_trace: int, imag_trace: int, *, declared_bad_primes: tuple[int, ...] = ()
) -> dict[str, Any]:
    """Exact modulus records for one nonreal trace and its conjugate."""

    poly = complex_trace_modulus_polynomial(sp.Rational(real_trace), sp.Rational(imag_trace))
    trace_value = complex(float(real_trace), float(imag_trace))
    discriminant = cmath.sqrt(trace_value * trace_value - 4)
    multipliers = ((trace_value + discriminant) / 2, (trace_value - discriminant) / 2)
    approximations = sorted(abs(value) ** 2 for value in multipliers)
    roots = []
    rational_moduli: list[sp.Rational] = []
    for role, approximation in zip(("contracting", "expanding"), approximations, strict=True):
        factor, interval = _select_root(poly, approximation)
        rational_mu = -factor.TC() if factor.degree() == 1 else None
        rational_modulus = (
            exact_positive_rational_square_root(sp.Rational(rational_mu))
            if rational_mu is not None
            else None
        )
        if rational_modulus is not None:
            rational_moduli.append(rational_modulus)
            classification = _rational_modulus_classification(
                rational_modulus, declared_bad_primes
            )
        elif rational_mu is not None:
            classification = "RATIONAL_MU_BUT_IRRATIONAL_MODULUS"
        else:
            classification = "ALGEBRAIC_UNIT_IRRATIONAL_MODULUS"
        roots.append(
            {
                "role": role,
                "minimal_polynomial": polynomial_record(factor, MU),
                "minimal_polynomial_degree": factor.degree(),
                "isolating_interval": [str(interval[0]), str(interval[1])],
                "display_approximation_only": f"{approximation:.12g}",
                "exact_rational_mu_value": str(rational_mu) if rational_mu is not None else None,
                "exact_positive_rational_modulus": (
                    str(rational_modulus) if rational_modulus is not None else None
                ),
                "classification": classification,
            }
        )
    return {
        "trace": f"{real_trace}+({imag_trace})*I",
        "conjugate_trace": f"{real_trace}-({imag_trace})*I",
        "derivation": "write lambda=x+i*y, impose lambda^2-t*lambda+1=0 and M=x^2+y^2; the displayed reciprocal equation is the exact elimination",
        "modulus_squared_polynomial": polynomial_record(poly, MU),
        "records": roots,
        "declared_bad_prime_support": list(declared_bad_primes),
        "rational_modulus_values": [
            str(value) for value in sorted(set(rational_moduli))
        ],
    }
