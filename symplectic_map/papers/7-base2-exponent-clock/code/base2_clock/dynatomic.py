"""Formal-period diagnostics and frozen set-theoretic exact-period engine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

import sympy as sp

from .algebra import (
    CandidateField,
    algebraic_field_norm,
    iterate_polynomial,
    serialize_element,
    serialize_polynomial,
)


@dataclass(frozen=True)
class ExactSetComponent:
    """Formal, scheme, and least-period set objects kept explicitly distinct."""

    period: int
    iterate_equation: sp.Poly
    iterate_radical: sp.Poly
    formal_dynatomic: sp.Poly
    formal_radical: sp.Poly
    lower_divisor_radical_product: sp.Poly
    lower_overlap: sp.Poly
    exact_set: sp.Poly


@dataclass(frozen=True)
class TargetCertificate:
    """Two exact target engines for one normalized multiplier value."""

    target: sp.Rational
    gcd: sp.Poly
    resultant: Any
    rational_field_norm: sp.Rational
    hit: bool
    engines_agree: bool


@dataclass(frozen=True)
class PeriodCertificate:
    """Complete exact certificate for one map and requested period."""

    component: ExactSetComponent
    normalized_cycle_product: sp.Poly
    invariant_mod_exact_set: bool
    exact_degree_divisible_by_period: bool
    exact_set_squarefree: bool
    targets: tuple[TargetCertificate, ...]


def _identity(base: sp.Poly) -> sp.Poly:
    variable = base.gens[0]
    return sp.Poly(variable, variable, domain=base.domain)


def iterate_minus_identity(base: sp.Poly, period: int) -> sp.Poly:
    """Return ``f^period-X`` exactly."""

    if type(period) is not int or period < 1:
        raise ValueError("period must be a positive integer")
    return iterate_polynomial(base, period) - _identity(base)


def radical(value: sp.Poly) -> sp.Poly:
    """Return the monic squarefree radical in characteristic zero."""

    if value.is_zero:
        raise ValueError("the radical of the zero polynomial is undefined")
    if value.degree() <= 0:
        return sp.Poly(1, value.gens[0], domain=value.domain)
    common = sp.gcd(value, value.diff())
    squarefree = value.exquo(common)
    return squarefree.monic()


def formal_dynatomic(base: sp.Poly, period: int) -> sp.Poly:
    """Compute the formal dynatomic polynomial by exact Mobius division."""

    variable = base.gens[0]
    numerator = sp.Poly(1, variable, domain=base.domain)
    denominator = sp.Poly(1, variable, domain=base.domain)
    for divisor in sp.divisors(period):
        mobius = int(sp.mobius(period // divisor))
        factor = iterate_minus_identity(base, int(divisor))
        if mobius == 1:
            numerator *= factor
        elif mobius == -1:
            denominator *= factor
    quotient, remainder = numerator.div(denominator)
    if not remainder.is_zero:
        raise ArithmeticError(f"formal dynatomic division failed at period {period}")
    return quotient.monic()


def exact_set_component(base: sp.Poly, period: int) -> ExactSetComponent:
    """Apply the source-locked radical/set-difference least-period formula.

    The definition is

    ``rad(F_n) / gcd(rad(F_n), product_{d|n,d<n} rad(F_d))``.

    Formal dynatomic polynomials and multiplicities are retained as separate
    diagnostics and never substitute for this set-theoretic object.
    """

    if type(period) is not int or period < 1:
        raise ValueError("period must be a positive integer")
    variable = base.gens[0]
    equation = iterate_minus_identity(base, period)
    equation_radical = radical(equation)
    proper_divisors = [int(item) for item in sp.divisors(period) if int(item) < period]
    lower_product = sp.Poly(1, variable, domain=base.domain)
    for divisor in proper_divisors:
        lower_product *= radical(iterate_minus_identity(base, divisor))
    overlap = sp.gcd(equation_radical, lower_product).monic()
    exact = equation_radical.exquo(overlap)
    exact = exact.monic() if exact.degree() > 0 else sp.Poly(1, variable, domain=base.domain)
    formal = formal_dynatomic(base, period)
    return ExactSetComponent(
        period=period,
        iterate_equation=equation,
        iterate_radical=equation_radical,
        formal_dynatomic=formal,
        formal_radical=radical(formal),
        lower_divisor_radical_product=lower_product,
        lower_overlap=overlap,
        exact_set=exact,
    )


def normalized_cycle_product(base: sp.Poly, period: int) -> sp.Poly:
    """Return ``B_n(X)=product_{j=0}^{n-1} f^j(X)``."""

    variable = base.gens[0]
    value = sp.Poly(1, variable, domain=base.domain)
    for step in range(period):
        value *= iterate_polynomial(base, step)
    return value


def target_certificate(
    exact: sp.Poly,
    normalized: sp.Poly,
    target: sp.Rational,
    *,
    field: CandidateField | None,
) -> TargetCertificate:
    variable = exact.gens[0]
    target_polynomial = sp.Poly(
        sp.Rational(target) - normalized.as_expr(),
        variable,
        domain=exact.domain,
    )
    common = sp.gcd(exact, target_polynomial)
    common = common.monic() if common.degree() > 0 else sp.Poly(1, variable, domain=exact.domain)
    if exact.degree() <= 0:
        resultant = exact.domain.one
    else:
        resultant = exact.resultant(target_polynomial)
    resultant = exact.domain.convert(resultant)
    if field is None:
        norm = sp.Rational(resultant)
    else:
        norm = algebraic_field_norm(resultant, field)
    hit = common.degree() > 0
    resultant_zero = resultant == exact.domain.zero
    norm_zero = norm == 0
    agreement = hit == resultant_zero == norm_zero
    return TargetCertificate(
        target=sp.Rational(target),
        gcd=common,
        resultant=resultant,
        rational_field_norm=norm,
        hit=hit,
        engines_agree=agreement,
    )


def audit_period(
    base: sp.Poly,
    period: int,
    *,
    targets: Iterable[sp.Rational | int] = (1, -1),
    field: CandidateField | None = None,
) -> PeriodCertificate:
    """Run the shared exact-set, cycle-product, gcd, resultant, and norm engines."""

    component = exact_set_component(base, period)
    normalized = normalized_cycle_product(base, period)
    exact = component.exact_set
    if exact.degree() <= 0:
        invariant = True
    else:
        transported = normalized.compose(base) - normalized
        invariant = transported.rem(exact).is_zero
    exact_degree = 0 if exact.degree() <= 0 else int(exact.degree())
    target_certificates = tuple(
        target_certificate(exact, normalized, sp.Rational(target), field=field)
        for target in targets
    )
    return PeriodCertificate(
        component=component,
        normalized_cycle_product=normalized,
        invariant_mod_exact_set=invariant,
        exact_degree_divisible_by_period=exact_degree % period == 0,
        exact_set_squarefree=exact.degree() <= 0 or sp.gcd(exact, exact.diff()).degree() == 0,
        targets=target_certificates,
    )


def certificate_passes(certificate: PeriodCertificate) -> bool:
    """Return whether all mandatory implementation checks agree."""

    return (
        certificate.invariant_mod_exact_set
        and certificate.exact_degree_divisible_by_period
        and certificate.exact_set_squarefree
        and all(target.engines_agree for target in certificate.targets)
    )


def certificate_record(
    certificate: PeriodCertificate,
    *,
    field: CandidateField | None = None,
    include_polynomials: bool = True,
) -> dict[str, Any]:
    """Serialize one certificate using exact strings and basis coefficients."""

    component = certificate.component
    exact_degree = 0 if component.exact_set.degree() <= 0 else int(component.exact_set.degree())
    record: dict[str, Any] = {
        "period": component.period,
        "iterate_equation_degree": int(component.iterate_equation.degree()),
        "iterate_radical_degree": int(component.iterate_radical.degree()),
        "iterate_scheme_repeated_degree": int(
            component.iterate_equation.degree() - component.iterate_radical.degree()
        ),
        "formal_dynatomic_degree": int(component.formal_dynatomic.degree()),
        "formal_radical_degree": int(component.formal_radical.degree()),
        "formal_scheme_repeated_degree": int(
            component.formal_dynatomic.degree() - component.formal_radical.degree()
        ),
        "lower_overlap_degree": int(component.lower_overlap.degree()),
        "exact_set_degree": exact_degree,
        "exact_cycle_count": exact_degree // component.period,
        "formal_radical_equals_exact_set": component.formal_radical == component.exact_set,
        "exact_set_squarefree": certificate.exact_set_squarefree,
        "exact_degree_divisible_by_period": certificate.exact_degree_divisible_by_period,
        "normalized_product_invariant": certificate.invariant_mod_exact_set,
        "targets": [],
        "status": "PASS" if certificate_passes(certificate) else "FAIL",
    }
    for target in certificate.targets:
        target_record = {
            "target": str(target.target),
            "gcd_degree": 0 if target.gcd.degree() <= 0 else int(target.gcd.degree()),
            "hit": target.hit,
            "target_resultant": serialize_element(target.resultant, field),
            "rational_field_norm": str(target.rational_field_norm),
            "field_norm_nonzero": target.rational_field_norm != 0,
            "gcd_resultant_norm_agree": target.engines_agree,
        }
        if include_polynomials:
            target_record["gcd_polynomial"] = serialize_polynomial(target.gcd, field)
        record["targets"].append(target_record)
    if include_polynomials:
        record["iterate_equation"] = serialize_polynomial(component.iterate_equation, field)
        record["iterate_radical"] = serialize_polynomial(component.iterate_radical, field)
        record["formal_dynatomic"] = serialize_polynomial(component.formal_dynatomic, field)
        record["formal_radical"] = serialize_polynomial(component.formal_radical, field)
        record["lower_overlap"] = serialize_polynomial(component.lower_overlap, field)
        record["exact_set_component"] = serialize_polynomial(component.exact_set, field)
        record["normalized_cycle_product"] = serialize_polynomial(
            certificate.normalized_cycle_product,
            field,
        )
    return record
