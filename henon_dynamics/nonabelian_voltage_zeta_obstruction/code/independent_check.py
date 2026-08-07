#!/usr/bin/env python3
"""Independent checks for HCS-C15 without importing the producer."""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

import sympy as sp


def multiply(left: tuple[int, int, int], right: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    a, b, c = left
    aa, bb, cc = right
    return ((a + aa) % p, (b + bb) % p, (c + cc + a * bb) % p)


def inverse(element: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    for candidate in ((a, b, c) for a in range(p) for b in range(p) for c in range(p)):
        if multiply(element, candidate, p) == (0, 0, 0) and multiply(candidate, element, p) == (0, 0, 0):
            return candidate
    raise AssertionError("inverse not found")


def conjugacy_class(element: tuple[int, int, int], group: list[tuple[int, int, int]], p: int) -> set[tuple[int, int, int]]:
    return {
        multiply(multiply(h, element, p), inverse(h, p), p)
        for h in group
    }


def word_value(word: str, p: int) -> tuple[int, int, int]:
    generators = {
        "x": (1, 0, 0),
        "X": (p - 1, 0, 0),
        "y": (0, 1, 0),
        "Y": (0, p - 1, 0),
    }
    value = (0, 0, 0)
    for letter in word:
        value = multiply(value, generators[letter], p)
    return value


def regular_permutation_cycles(
    element: tuple[int, int, int], group: list[tuple[int, int, int]], p: int
) -> list[int]:
    index = {value: position for position, value in enumerate(group)}
    permutation = [0] * len(group)
    for value in group:
        permutation[index[value]] = index[multiply(value, element, p)]
    unseen = set(range(len(group)))
    lengths: list[int] = []
    while unseen:
        start = next(iter(unseen))
        current = start
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = permutation[current]
            length += 1
        lengths.append(length)
    return sorted(lengths)


def cyclic_bigrams(word: str) -> dict[str, int]:
    alphabet = "xXyY"
    return {
        a + b: sum(
            word[index] == a and word[(index + 1) % len(word)] == b
            for index in range(len(word))
        )
        for a in alphabet
        for b in alphabet
    }


def cyclically_reduced(word: str) -> bool:
    inverse_letter = {"x": "X", "X": "x", "y": "Y", "Y": "y"}
    return all(
        inverse_letter[word[index]] != word[(index + 1) % len(word)]
        for index in range(len(word))
    )


def primitive_word(word: str) -> bool:
    length = len(word)
    return all(
        word != word[:period] * (length // period)
        for period in range(1, length)
        if length % period == 0
    )


def cyclic_rotations(word: str) -> set[str]:
    return {word[index:] + word[:index] for index in range(len(word))}


def inverse_word(word: str) -> str:
    inverse_letter = {"x": "X", "X": "x", "y": "Y", "Y": "y"}
    return "".join(inverse_letter[letter] for letter in reversed(word))


def dihedrally_equivalent(left: str, right: str) -> bool:
    return right in cyclic_rotations(left) | cyclic_rotations(inverse_word(left))


def new_character_residual(modulus: int) -> tuple[float, float]:
    """Check A chi=lambda chi directly on H(Z/modulus), without matrices."""

    generators = (
        (1, 0, 0),
        (modulus - 1, 0, 0),
        (0, 1, 0),
        (0, modulus - 1, 0),
    )
    eigenvalue = 2.0 + 2.0 * math.cos(2.0 * math.pi / modulus)
    maximum = 0.0
    for element in (
        (a, b, c)
        for a in range(modulus)
        for b in range(modulus)
        for c in range(modulus)
    ):
        value = cmath.exp(2j * math.pi * element[0] / modulus)
        adjacency_value = sum(
            cmath.exp(2j * math.pi * multiply(element, generator, modulus)[0] / modulus)
            for generator in generators
        )
        maximum = max(maximum, abs(adjacency_value - eigenvalue * value))
    return eigenvalue, maximum


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=7)
    parser.add_argument("--output", type=Path, default=Path("results/independent_check.json"))
    arguments = parser.parse_args()
    p = arguments.prime
    if p != 7:
        raise ValueError("the independent order-collapse witness is frozen at p=7")

    group = [(a, b, c) for a in range(p) for b in range(p) for c in range(p)]
    left_word = "XXXyxxyxYY"
    right_word = "XXXyxyxxYY"
    left = word_value(left_word, p)
    right = word_value(right_word, p)
    left_class = conjugacy_class(left, group, p)
    right_class = conjugacy_class(right, group, p)
    if left_class == right_class:
        raise AssertionError("central witnesses should be distinct conjugacy classes")

    cyclic_reduction_checks = [cyclically_reduced(left_word), cyclically_reduced(right_word)]
    primitive_checks = [primitive_word(left_word), primitive_word(right_word)]
    dihedral_equivalence = dihedrally_equivalent(left_word, right_word)
    holonomies_are_noninverse = left != inverse(right, p)
    if not all(cyclic_reduction_checks):
        raise AssertionError("the independent witnesses must be cyclically reduced")
    if not all(primitive_checks):
        raise AssertionError("the independent witnesses must be primitive")
    if dihedral_equivalence:
        raise AssertionError("the independent witnesses must be non-dihedral")
    if not holonomies_are_noninverse:
        raise AssertionError("the independent holonomies must not be inverses")
    if cyclic_bigrams(left_word) != cyclic_bigrams(right_word):
        raise AssertionError("the independent bigram ledger does not match")
    left_cycles = regular_permutation_cycles(left, group, p)
    right_cycles = regular_permutation_cycles(right, group, p)
    expected_cycles = [p] * (p**2)
    passed = left_cycles == expected_cycles and right_cycles == expected_cycles
    if not passed:
        raise AssertionError("regular permutations did not collapse to the order formula")

    q = sp.symbols("q")
    expected = (1 - q**p) ** (p**2)
    eigenvalue_9, residual_9 = new_character_residual(9)
    if residual_9 > 1e-12:
        raise AssertionError("conductor-new character failed the direct adjacency check")

    payload = {
        "prime": p,
        "group_size": len(group),
        "left_holonomy": list(left),
        "right_holonomy": list(right),
        "left_conjugacy_class": [list(item) for item in sorted(left_class)],
        "right_conjugacy_class": [list(item) for item in sorted(right_class)],
        "words": [left_word, right_word],
        "cyclically_reduced": cyclic_reduction_checks,
        "primitive": primitive_checks,
        "dihedrally_equivalent": dihedral_equivalence,
        "holonomies_are_noninverse": holonomies_are_noninverse,
        "equal_cyclic_bigram_counts": True,
        "regular_cycle_lengths_left": {str(p): len(left_cycles)},
        "regular_cycle_lengths_right": {str(p): len(right_cycles)},
        "expected_order_only_determinant": str(sp.factor(expected)),
        "exact_match": passed,
        "tower_level_2_modulus": 9,
        "tower_level_2_new_character_eigenvalue": eigenvalue_9,
        "tower_level_2_direct_eigenvector_max_residual": residual_9,
        "implementation": (
            "independent word-period/dihedral checks, regular-permutation cycle "
            "decomposition, and direct H(Z/9) character check"
        ),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
