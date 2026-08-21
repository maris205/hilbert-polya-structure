#!/usr/bin/env python3
"""Independent level-recursion and cylinder-count engine.

This implementation does not import formula_engine and never evaluates the
closed H_j formula.  It loops over levels or recurses over actual finite
trees, so comparisons in run_validation cross two independent code paths.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Sequence, Tuple


def _factor(n: int) -> Dict[int, int]:
    if n < 1:
        raise ValueError("positive integer required")
    factors: Dict[int, int] = {}
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        factors[divisor] = factors.get(divisor, 0) + 1
        remaining //= divisor
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def _accumulate(target: Dict[int, int], source: Dict[int, int], multiplier: int) -> None:
    for prime, exponent in source.items():
        target[prime] = target.get(prime, 0) + multiplier * exponent


def level_component_exponents(
    d: int, a: Sequence[int], root_phase: int, depth: int
) -> Dict[int, int]:
    if d < 2 or not a or depth < 0:
        raise ValueError("invalid component-prefix parameters")
    p = len(a)
    result: Dict[int, int] = {}
    vertices = 1
    phase = root_phase % p
    for _level in range(depth + 1):
        _accumulate(result, _factor(a[phase]), vertices)
        vertices *= d
        phase = (phase + 1) % p
    return {prime: exponent for prime, exponent in result.items() if exponent}


def level_feeder_exponents(
    d: int,
    a: Sequence[int],
    m: Sequence[int],
    total_depth: int,
    transient_levels: int = 1,
) -> Dict[int, int]:
    if transient_levels < 1 or total_depth < transient_levels:
        return {}
    p = len(a)
    if len(m) != p or sum(m) != d**transient_levels:
        raise ValueError("composition has the wrong leaf total")
    result: Dict[int, int] = {}
    core_depth = total_depth - transient_levels
    for start_phase, number_of_leaves in enumerate(m):
        vertices_per_leaf = 1
        phase = start_phase
        for _relative_level in range(core_depth + 1):
            _accumulate(
                result,
                _factor(a[phase]),
                number_of_leaves * vertices_per_leaf,
            )
            vertices_per_leaf *= d
            phase = (phase + 1) % p
    return {prime: exponent for prime, exponent in result.items() if exponent}


def recursive_component_count(d: int, a: Sequence[int], root_phase: int, depth: int) -> int:
    """Count actual labeled finite trees by the complete-bipartite recurrence."""
    if depth == 0:
        return a[root_phase % len(a)]
    child_count = recursive_component_count(d, a, root_phase + 1, depth - 1)
    return a[root_phase % len(a)] * child_count**d


def recursive_feeder_count(
    d: int, a: Sequence[int], ordered_leaf_phases: Sequence[int], total_depth: int
) -> int:
    """One transient root, followed by independently labeled core subtrees."""
    if len(ordered_leaf_phases) != d or total_depth < 1:
        raise ValueError("one-level feeder requires d phases and positive depth")
    subtree_depth = total_depth - 1
    count = 1
    for phase in ordered_leaf_phases:
        count *= recursive_component_count(d, a, phase, subtree_depth)
    return count


def integer_from_exponents(exponents: Dict[int, int]) -> int:
    result = 1
    for prime, exponent in exponents.items():
        result *= prime**exponent
    return result


def delta_size(d: int, depth: int) -> int:
    if d < 2 or depth < 0:
        raise ValueError("require d>=2 and depth>=0")
    return (d ** (depth + 1) - 1) // (d - 1)


def normalized_exponents(exponents: Dict[int, int], d: int, depth: int) -> Dict[int, Fraction]:
    denominator = delta_size(d, depth)
    return {
        prime: Fraction(exponent, denominator)
        for prime, exponent in exponents.items()
        if exponent
    }


def canonical_fraction_form(form: Dict[int, Fraction]) -> Tuple[Tuple[int, int, int], ...]:
    return tuple(
        (prime, coefficient.numerator, coefficient.denominator)
        for prime, coefficient in sorted(form.items())
        if coefficient
    )


def composition_from_ordered(phases: Sequence[int], p: int) -> Tuple[int, ...]:
    counts = [0] * p
    for phase in phases:
        counts[phase] += 1
    return tuple(counts)
