#!/usr/bin/env python3
"""Post-freeze independent arithmetic evaluator for SD-C29.

Nothing in this module is imported by the candidate core.  Trial division and
the scalar arithmetic Möbius function are used only to validate source-derived
cover and incidence outputs.
"""

from __future__ import annotations

import math


def trial_atom(label: int) -> bool:
    if label < 2:
        return False
    return all(label % divisor for divisor in range(2, math.isqrt(label) + 1))


def evaluator_atoms(cutoff: int) -> list[int]:
    return [label for label in range(2, cutoff + 1) if trial_atom(label)]


def arithmetic_mobius(label: int) -> int:
    if label == 1:
        return 1
    remainder = label
    factor_count = 0
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            remainder //= divisor
            factor_count += 1
            if remainder % divisor == 0:
                return 0
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factor_count += 1
    return -1 if factor_count % 2 else 1


def expected_incidence_entry(
    left_label: int, source_label: int, right_label: int
) -> int:
    if source_label % left_label or right_label % source_label:
        return 0
    return arithmetic_mobius(right_label // source_label)


def deterministic_permutation(size: int) -> tuple[int, ...]:
    """A fixed nontrivial permutation, independent of arithmetic labels."""
    return tuple(sorted(range(size), key=lambda index: ((7 * index + 5) % size, index)))
