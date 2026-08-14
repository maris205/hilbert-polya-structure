"""Exact multiplier resultants, cycle polynomials, and rational roots."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp
from sympy.ntheory.primetest import isprime

from .algebra import CandidateField, iterate_polynomial, serialize_polynomial
from .dynatomic import DynatomicComponent, dynatomic_summary, exact_period_component


@dataclass(frozen=True)
class MultiplierCertificate:
    """All exact certificates for one map and requested period."""

    period: int
    dynatomic: DynatomicComponent
    derivative_multiplier: sp.Poly
    chain_multiplier: sp.Poly
    chain_rule_pass: bool
    point_resultant: sp.Poly
    cycle_polynomial: sp.Poly
    perfect_cycle_power_pass: bool
    quotient_annihilation_pass: bool
    rational_candidates: tuple[sp.Rational, ...]
    rational_component_gcd: sp.Poly

    @property
    def exact_cycle_count(self) -> int:
        if self.dynatomic.exact_degree == 0:
            return 0
        return self.dynatomic.exact_degree // self.period


def chain_rule_multiplier(base: sp.Poly, period: int) -> sp.Poly:
    """Compute the return multiplier as a product of one-step derivatives."""

    variable = base.gens[0]
    derivative = base.diff()
    result = sp.Poly(1, variable, domain=base.domain)
    for step in range(period):
        position = iterate_polynomial(base, step)
        result *= derivative.compose(position)
    return result


def derivative_multiplier(base: sp.Poly, period: int) -> sp.Poly:
    """Compute the return multiplier by differentiating the full iterate."""

    return iterate_polynomial(base, period).diff()


def multiplier_resultant(
    exact_component: sp.Poly,
    multiplier: sp.Poly,
    multiplier_variable: sp.Symbol | None = None,
) -> sp.Poly:
    """Return the monic per-point multiplier resultant."""

    lam = multiplier_variable if multiplier_variable is not None else sp.Symbol("L")
    if exact_component.degree() <= 0:
        return sp.Poly(1, lam, domain=exact_component.domain)
    orbit_variable = exact_component.gens[0]
    coefficient_ring = exact_component.domain.poly_ring(lam)
    left = sp.Poly(exact_component.as_expr(), orbit_variable, domain=coefficient_ring)
    right = sp.Poly(lam - multiplier.as_expr(), orbit_variable, domain=coefficient_ring)
    resultant_expression = left.resultant(right)
    return sp.Poly(resultant_expression, lam, domain=exact_component.domain).monic()


def verified_cycle_root(point_resultant: sp.Poly, period: int) -> tuple[sp.Poly, bool]:
    """Extract and verify the monic period-th root induced by cycle grouping."""

    variable = point_resultant.gens[0]
    if point_resultant.degree() <= 0:
        return sp.Poly(1, variable, domain=point_resultant.domain), True
    coefficient, squarefree_factors = point_resultant.sqf_list()
    if point_resultant.domain.convert(coefficient) != point_resultant.domain.one:
        return sp.Poly(1, variable, domain=point_resultant.domain), False
    if any(multiplicity % period != 0 for _, multiplicity in squarefree_factors):
        return sp.Poly(1, variable, domain=point_resultant.domain), False
    root = sp.Poly(1, variable, domain=point_resultant.domain)
    for factor, multiplicity in squarefree_factors:
        root *= factor ** (multiplicity // period)
    root = root.monic()
    return root, root**period == point_resultant


def _coefficient_components(
    value: sp.Poly,
    field: CandidateField | None,
) -> tuple[sp.Poly, ...]:
    """Expand a multiplier polynomial into rational parameter-basis parts."""

    variable = value.gens[0]
    degree = int(value.degree())
    if field is None:
        return (sp.Poly(value.as_expr(), variable, domain=sp.QQ),)

    component_expressions = [sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    for index, coefficient in enumerate(value.all_coeffs()):
        power = degree - index
        element = field.domain.from_sympy(coefficient)
        descending = list(element.to_list())
        padded = [field.domain.dom.zero] * (3 - len(descending)) + descending
        ascending = list(reversed(padded))
        for basis_index, rational in enumerate(ascending):
            component_expressions[basis_index] += sp.Rational(rational) * variable**power
    return tuple(sp.Poly(expression, variable, domain=sp.QQ) for expression in component_expressions)


def rational_roots_in_field_polynomial(
    value: sp.Poly,
    *,
    field: CandidateField | None = None,
) -> tuple[tuple[sp.Rational, ...], sp.Poly]:
    """Certify rational roots by simultaneous vanishing of basis components."""

    variable = value.gens[0]
    components = [component for component in _coefficient_components(value, field) if not component.is_zero]
    if not components:
        raise ArithmeticError("zero polynomial has no finite rational-root certificate")
    common = components[0]
    for component in components[1:]:
        common = sp.gcd(common, component)
    common = common.monic()
    roots = tuple(sorted(sp.Rational(root) for root in common.ground_roots()))
    for root in roots:
        if sp.simplify(value.eval(root)) != 0:
            raise ArithmeticError("basis-component rational-root certificate failed")
    return roots, common


def quotient_annihilation(
    exact_component: sp.Poly,
    multiplier: sp.Poly,
    cycle_polynomial: sp.Poly,
) -> bool:
    """Check the cycle polynomial on the multiplier in the orbit quotient."""

    if exact_component.degree() <= 0:
        return True
    lam = cycle_polynomial.gens[0]
    expression = sp.expand(cycle_polynomial.as_expr().subs(lam, multiplier.as_expr()))
    evaluated = sp.Poly(expression, exact_component.gens[0], domain=exact_component.domain)
    return evaluated.rem(exact_component).is_zero


def multiplier_certificate(
    base: sp.Poly,
    period: int,
    *,
    field: CandidateField | None = None,
) -> MultiplierCertificate:
    """Build the complete exact multiplier certificate for one period."""

    component = exact_period_component(base, period)
    via_derivative = derivative_multiplier(base, period)
    via_chain = chain_rule_multiplier(base, period)
    chain_pass = via_derivative == via_chain
    point_resultant = multiplier_resultant(component.exact, via_derivative)
    cycle_polynomial, power_pass = verified_cycle_root(point_resultant, period)
    rational_candidates, common = rational_roots_in_field_polynomial(
        cycle_polynomial,
        field=field,
    )
    annihilation_pass = quotient_annihilation(component.exact, via_chain, cycle_polynomial)
    return MultiplierCertificate(
        period=period,
        dynatomic=component,
        derivative_multiplier=via_derivative,
        chain_multiplier=via_chain,
        chain_rule_pass=chain_pass,
        point_resultant=point_resultant,
        cycle_polynomial=cycle_polynomial,
        perfect_cycle_power_pass=power_pass,
        quotient_annihilation_pass=annihilation_pass,
        rational_candidates=rational_candidates,
        rational_component_gcd=common,
    )


def classify_rational_multiplier(value: sp.Rational, period: int) -> dict[str, Any]:
    """Classify one internally derived exact rational multiplier."""

    rational = sp.Rational(value)
    absolute = abs(rational)
    is_integer = rational.q == 1
    raw_prime = bool(is_integer and isprime(int(absolute)))
    exponent_base: int | None = None
    exponent_prime = False
    if is_integer:
        root, exact = sp.integer_nthroot(int(absolute), period)
        if exact and isprime(root):
            exponent_base = int(root)
            exponent_prime = True
    return {
        "multiplier": str(rational),
        "is_rational_integer": is_integer,
        "raw_rational_prime": raw_prime,
        "rational_exponent_prime": exponent_prime,
        "exponent_prime_base": exponent_base,
        "exponent_prime_kind": (
            "EXPONENT_PRIME_TWO"
            if exponent_prime and exponent_base == 2
            else "EXPONENT_PRIME_ODD"
            if exponent_prime
            else "NONE"
        ),
    }


def certificate_record(
    certificate: MultiplierCertificate,
    *,
    field: CandidateField | None = None,
    derivative_content: int | None = None,
) -> dict[str, Any]:
    """Serialize a certificate, including exact divisibility diagnostics."""

    record: dict[str, Any] = dynatomic_summary(certificate.dynatomic)
    candidate_records: list[dict[str, Any]] = []
    for candidate in certificate.rational_candidates:
        item = classify_rational_multiplier(candidate, certificate.period)
        if derivative_content is not None:
            quotient = candidate / (derivative_content**certificate.period)
            item["derivative_content_power"] = derivative_content**certificate.period
            item["content_divisibility_pass"] = bool(quotient.q == 1)
            item["content_quotient"] = str(quotient)
        candidate_records.append(item)
    record.update(
        {
            "exact_cycle_count": certificate.exact_cycle_count,
            "resultant_degree": int(certificate.point_resultant.degree()),
            "cycle_polynomial_degree": int(certificate.cycle_polynomial.degree()),
            "chain_rule_identity": "PASS" if certificate.chain_rule_pass else "FAIL",
            "perfect_cycle_power": "PASS" if certificate.perfect_cycle_power_pass else "FAIL",
            "quotient_annihilation": "PASS" if certificate.quotient_annihilation_pass else "FAIL",
            "rational_candidates": [str(item) for item in certificate.rational_candidates],
            "rational_candidate_records": candidate_records,
            "formal_dynatomic_polynomial": serialize_polynomial(certificate.dynatomic.formal, field=field),
            "exact_period_polynomial": serialize_polynomial(certificate.dynatomic.exact, field=field),
            "derivative_multiplier_polynomial": serialize_polynomial(
                certificate.derivative_multiplier,
                field=field,
            ),
            "point_resultant": serialize_polynomial(certificate.point_resultant, field=field),
            "cycle_multiplier_polynomial": serialize_polynomial(certificate.cycle_polynomial, field=field),
            "rational_component_gcd": serialize_polynomial(certificate.rational_component_gcd),
        }
    )
    return record
