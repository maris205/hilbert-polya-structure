#!/usr/bin/env python3
"""Exact closed-form engine for the complete cyclic phase-allocation family.

This module deliberately does not import prefix_engine.  Its finite-prefix
counts are obtained by grouping geometric progressions by residue class.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
from math import lcm
from typing import Dict, Iterable, Iterator, Sequence, Tuple

LogForm = Dict[int, Fraction]


def factor_integer(n: int) -> Dict[int, int]:
    if n < 1:
        raise ValueError("alphabet sizes must be positive")
    out: Dict[int, int] = {}
    q = n
    prime = 2
    while prime * prime <= q:
        while q % prime == 0:
            out[prime] = out.get(prime, 0) + 1
            q //= prime
        prime = 3 if prime == 2 else prime + 2
    if q > 1:
        out[q] = out.get(q, 0) + 1
    return out


def clean(form: LogForm) -> LogForm:
    return {prime: coeff for prime, coeff in form.items() if coeff}


def add(*forms: LogForm) -> LogForm:
    out: LogForm = {}
    for form in forms:
        for prime, coeff in form.items():
            out[prime] = out.get(prime, Fraction(0)) + coeff
    return clean(out)


def scale(form: LogForm, scalar: Fraction | int) -> LogForm:
    scalar = Fraction(scalar)
    return clean({prime: scalar * coeff for prime, coeff in form.items()})


def log_integer_form(n: int) -> LogForm:
    return {prime: Fraction(exponent) for prime, exponent in factor_integer(n).items()}


def canonical_form(form: LogForm) -> Tuple[Tuple[int, int, int], ...]:
    return tuple(
        (prime, coeff.numerator, coeff.denominator)
        for prime, coeff in sorted(clean(form).items())
    )


def form_from_canonical(items: Iterable[Sequence[int]]) -> LogForm:
    return clean({int(p): Fraction(int(n), int(d)) for p, n, d in items})


def evaluate(form: LogForm, precision: int = 70) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        total = Decimal(0)
        for prime, coeff in clean(form).items():
            total += (Decimal(coeff.numerator) / Decimal(coeff.denominator)) * Decimal(prime).ln()
        return +total


def compare_forms(left: LogForm, right: LogForm) -> int:
    """Compare rational prime-log forms exactly; return -1, 0, or 1.

    After clearing rational denominators, the sign of the difference is the
    sign of log(N/D), which is decided by the exact integer comparison N vs D.
    """
    difference = add(left, scale(right, -1))
    if not difference:
        return 0
    common_denominator = 1
    for coefficient in difference.values():
        common_denominator = lcm(common_denominator, coefficient.denominator)
    numerator = 1
    denominator = 1
    for prime, coefficient in difference.items():
        exponent = coefficient.numerator * (common_denominator // coefficient.denominator)
        if exponent > 0:
            numerator *= prime**exponent
        elif exponent < 0:
            denominator *= prime ** (-exponent)
    return (numerator > denominator) - (numerator < denominator)


def compositions(total: int, parts: int) -> Iterator[Tuple[int, ...]]:
    if total < 0 or parts < 1:
        raise ValueError("invalid weak-composition parameters")
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def h_forms(d: int, a: Sequence[int]) -> Tuple[LogForm, ...]:
    """Return H_j(log a), j in Z/p, using the frozen backward convention."""
    if d < 2 or not a or any(size < 1 for size in a):
        raise ValueError("require d>=2 and all phase sizes positive")
    p = len(a)
    denominator = d**p - 1
    result = []
    for j in range(p):
        form: LogForm = {}
        for t in range(p):
            weight = Fraction((d - 1) * d ** (p - 1 - t), denominator)
            form = add(form, scale(log_integer_form(a[(j - t) % p]), weight))
        result.append(form)
    return tuple(result)


def mean_c_form(a: Sequence[int]) -> LogForm:
    return scale(add(*(log_integer_form(size) for size in a)), Fraction(1, len(a)))


def feeder_forms_via_h(d: int, a: Sequence[int], m: Sequence[int]) -> Tuple[LogForm, ...]:
    p = len(a)
    if len(m) != p or any(x < 0 for x in m) or sum(m) != d:
        raise ValueError("m must be a weak p-composition of d")
    h = h_forms(d, a)
    return tuple(
        scale(add(*(scale(h[(s + j) % p], m[s]) for s in range(p))), Fraction(1, d))
        for j in range(p)
    )


def feeder_forms_via_b(d: int, a: Sequence[int], m: Sequence[int]) -> Tuple[LogForm, ...]:
    """Independently within the closed-form lane, compute H_j(b), b_k=sum m_s c_{s+k}/d."""
    p = len(a)
    if len(m) != p or any(x < 0 for x in m) or sum(m) != d:
        raise ValueError("m must be a weak p-composition of d")
    b = []
    for k in range(p):
        b.append(
            scale(
                add(*(scale(log_integer_form(a[(s + k) % p]), m[s]) for s in range(p))),
                Fraction(1, d),
            )
        )
    denominator = d**p - 1
    out = []
    for j in range(p):
        form: LogForm = {}
        for t in range(p):
            weight = Fraction((d - 1) * d ** (p - 1 - t), denominator)
            form = add(form, scale(b[(j - t) % p], weight))
        out.append(form)
    return tuple(out)


def feeder_forms_level_l(
    d: int, a: Sequence[int], m: Sequence[int], level: int
) -> Tuple[LogForm, ...]:
    p = len(a)
    leaves = d**level
    if level < 1 or len(m) != p or any(x < 0 for x in m) or sum(m) != leaves:
        raise ValueError("m must be a weak p-composition of d^level")
    h = h_forms(d, a)
    return tuple(
        scale(
            add(*(scale(h[(s + j) % p], m[s]) for s in range(p))),
            Fraction(1, leaves),
        )
        for j in range(p)
    )


def shifted_product_forms(a: Sequence[int], m: Sequence[int]) -> Tuple[LogForm, ...]:
    p = len(a)
    if len(m) != p:
        raise ValueError("length mismatch")
    return tuple(
        add(*(scale(log_integer_form(a[(s + k) % p]), m[s]) for s in range(p)))
        for k in range(p)
    )


def all_equal(forms: Sequence[LogForm]) -> bool:
    return bool(forms) and all(canonical_form(form) == canonical_form(forms[0]) for form in forms[1:])


def dimension_choice(forms: Sequence[LogForm]) -> Tuple[int, LogForm, Decimal]:
    if not forms:
        raise ValueError("at least one residue form is required")
    index = 0
    for candidate in range(1, len(forms)):
        if compare_forms(forms[candidate], forms[index]) < 0:
            index = candidate
    return index, forms[index], evaluate(forms[index])


def component_dimension(d: int, a: Sequence[int]) -> Tuple[int, LogForm, Decimal]:
    return dimension_choice(h_forms(d, a))


def feeder_dimension(d: int, a: Sequence[int], m: Sequence[int]) -> Tuple[int, LogForm, Decimal]:
    return dimension_choice(feeder_forms_via_h(d, a, m))


def closed_component_prefix_exponents(
    d: int, a: Sequence[int], root_phase: int, depth: int
) -> Dict[int, int]:
    """Group sum_{ell=0}^depth d^ell log(a_{h+ell}) by ell mod p."""
    if depth < 0:
        return {}
    p = len(a)
    out: Dict[int, int] = {}
    for residue in range(p):
        if residue > depth:
            continue
        terms = (depth - residue) // p + 1
        coefficient = d**residue * (d ** (p * terms) - 1) // (d**p - 1)
        for prime, exponent in factor_integer(a[(root_phase + residue) % p]).items():
            out[prime] = out.get(prime, 0) + coefficient * exponent
    return {prime: exponent for prime, exponent in out.items() if exponent}


def closed_feeder_prefix_exponents(
    d: int,
    a: Sequence[int],
    m: Sequence[int],
    total_depth: int,
    transient_levels: int = 1,
) -> Dict[int, int]:
    """Exact core-label exponents below a forced transient chain."""
    if transient_levels < 1 or total_depth < transient_levels:
        return {}
    p = len(a)
    leaves = d**transient_levels
    if len(m) != p or sum(m) != leaves:
        raise ValueError("composition has the wrong leaf total")
    core_depth = total_depth - transient_levels
    out: Dict[int, int] = {}
    for s, multiplicity in enumerate(m):
        for residue in range(p):
            if residue > core_depth:
                continue
            terms = (core_depth - residue) // p + 1
            coefficient = d**residue * (d ** (p * terms) - 1) // (d**p - 1)
            for prime, exponent in factor_integer(a[(s + residue) % p]).items():
                out[prime] = out.get(prime, 0) + multiplicity * coefficient * exponent
    return {prime: exponent for prime, exponent in out.items() if exponent}


def p2_expected_forms(d: int, a0: int, a1: int) -> Tuple[LogForm, LogForm]:
    """Return the closed component and optimized feeder forms for p=2."""
    c0 = log_integer_form(a0)
    c1 = log_integer_form(a1)
    mean = scale(add(c0, c1), Fraction(1, 2))
    high = max(a0, a1)
    low = min(a0, a1)
    absolute_difference = add(log_integer_form(high), scale(log_integer_form(low), -1))
    component_penalty = Fraction(d - 1, 2 * (d + 1))
    feeder_penalty = Fraction(0) if d % 2 == 0 else Fraction(d - 1, 2 * d * (d + 1))
    return (
        add(mean, scale(absolute_difference, -component_penalty)),
        add(mean, scale(absolute_difference, -feeder_penalty)),
    )


def balanced_composition(total: int, p: int) -> Tuple[int, ...]:
    quotient, remainder = divmod(total, p)
    return tuple(quotient + (1 if j < remainder else 0) for j in range(p))


def parameter_tuples(max_d: int, max_p: int, max_a: int) -> Iterator[Tuple[int, int, Tuple[int, ...]]]:
    for d in range(2, max_d + 1):
        for p in range(1, max_p + 1):
            for a in product(range(1, max_a + 1), repeat=p):
                yield d, p, a
