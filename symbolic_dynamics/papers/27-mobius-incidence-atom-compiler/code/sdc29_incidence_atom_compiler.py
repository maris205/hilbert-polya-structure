#!/usr/bin/env python3
"""Exact candidate core for the SD-C29 incidence atom compiler.

The core receives only the finite divisibility relation.  It derives covers of
the bottom element and never calls a prime generator, factorization oracle,
prime table, target zeta routine, or target-zero routine.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp


def divisibility_relation(cutoff: int) -> tuple[tuple[bool, ...], ...]:
    """The relation on the downset {1,...,cutoff}, in its numeric extension."""
    return tuple(
        tuple((column + 1) % (row + 1) == 0 for column in range(cutoff))
        for row in range(cutoff)
    )


def zeta_matrix(relation: tuple[tuple[bool, ...], ...]) -> sp.Matrix:
    return sp.Matrix([[int(value) for value in row] for row in relation])


def incidence_inverse(
    relation: tuple[tuple[bool, ...], ...],
) -> sp.Matrix:
    """Compute the incidence inverse from the relation, not integer factors."""
    size = len(relation)
    inverse = sp.zeros(size)
    for left in range(size - 1, -1, -1):
        inverse[left, left] = 1
        for right in range(left + 1, size):
            if relation[left][right]:
                inverse[left, right] = -sum(
                    inverse[left, middle]
                    for middle in range(left, right)
                    if relation[left][middle] and relation[middle][right]
                )
    return inverse


def coordinate_idempotent(size: int, index: int) -> sp.Matrix:
    result = sp.zeros(size)
    result[index, index] = 1
    return result


def compiled_idempotents(
    relation: tuple[tuple[bool, ...], ...],
) -> tuple[sp.Matrix, sp.Matrix, list[sp.Matrix]]:
    zeta = zeta_matrix(relation)
    mobius = incidence_inverse(relation)
    compiled = [
        zeta * coordinate_idempotent(len(relation), index) * mobius
        for index in range(len(relation))
    ]
    return zeta, mobius, compiled


def covers_bottom(
    relation: tuple[tuple[bool, ...], ...],
) -> tuple[int, ...]:
    """Return zero-based indices of covers of the bottom source object."""
    atoms: list[int] = []
    for right in range(1, len(relation)):
        strict_middle = any(
            middle != right
            and relation[0][middle]
            and relation[middle][right]
            for middle in range(1, len(relation))
        )
        if relation[0][right] and not strict_middle:
            atoms.append(right)
    return tuple(atoms)


def atom_actions(
    relation: tuple[tuple[bool, ...], ...],
) -> tuple[list[sp.Matrix], tuple[int, ...]]:
    _, _, compiled = compiled_idempotents(relation)
    atoms = covers_bottom(relation)
    zero = sp.zeros(len(relation))
    actions = [compiled[index] if index in atoms else zero for index in range(len(relation))]
    return actions, atoms


def compiled_entry(
    zeta: sp.Matrix, mobius: sp.Matrix, source: int, left: int, right: int
) -> sp.Expr:
    """The explicit entry 1_{left|source|right} mu(source,right)."""
    return zeta[left, source] * mobius[source, right]


def matrix_product(matrices: list[sp.Matrix], word: tuple[int, ...]) -> sp.Matrix:
    result = sp.eye(matrices[0].rows)
    for letter in word:
        result = result * matrices[letter]
    return result


def selector_value(word: tuple[int, ...], atoms: tuple[int, ...]) -> int:
    return int(bool(word) and len(set(word)) == 1 and word[0] in atoms)


def gamma_code(label: int) -> str:
    binary = format(label, "b")
    return "0" * (len(binary) - 1) + binary


def gamma_length(label: int) -> int:
    return len(gamma_code(label))


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def necklace_representatives(
    alphabet: tuple[int, ...], max_length: int
) -> list[tuple[int, ...]]:
    representatives: list[tuple[int, ...]] = []
    for length in range(1, max_length + 1):
        seen: set[tuple[int, ...]] = set()
        for word in product(alphabet, repeat=length):
            representative = canonical_rotation(word)
            if representative not in seen:
                seen.add(representative)
                representatives.append(representative)
    return representatives


def cyclic_orbit_size(word: tuple[int, ...]) -> int:
    return len({word[index:] + word[:index] for index in range(len(word))})


def word_trace_via_pair_relations(
    word: tuple[int, ...], matrices: list[sp.Matrix]
) -> sp.Expr:
    """Exact cyclic trace, short-circuiting a mixed word at an adjacent change."""
    if len(word) == 1 or len(set(word)) == 1:
        return sp.trace(matrix_product(matrices, word))
    length = len(word)
    change = next(
        index for index in range(length) if word[index] != word[(index + 1) % length]
    )
    return sp.trace(matrices[word[change]] * matrices[word[(change + 1) % length]])


def gamma_affine_branch(label: int) -> tuple[Fraction, Fraction]:
    """Compose the two frozen affine digit maps along the gamma code."""
    translation = Fraction(0)
    contraction = Fraction(1)
    for bit in gamma_code(label):
        digit_translation = Fraction(-1 if bit == "0" else 1, 4)
        translation = digit_translation + Fraction(1, 2) * translation
        contraction *= Fraction(1, 2)
    return translation, contraction


def affine_zero_form(
    degree: int,
    translation: Fraction,
    contraction: Fraction,
) -> sp.Matrix:
    matrix = sp.zeros(degree + 1)
    a = sp.Rational(translation.numerator, translation.denominator)
    q = sp.Rational(contraction.numerator, contraction.denominator)
    for source_degree in range(degree + 1):
        for target_degree in range(source_degree + 1):
            matrix[target_degree, source_degree] = (
                sp.binomial(source_degree, target_degree)
                * a ** (source_degree - target_degree)
                * q**target_degree
            )
    return matrix


def affine_one_form(
    degree: int,
    translation: Fraction,
    contraction: Fraction,
) -> sp.Matrix:
    matrix = sp.zeros(degree)
    a = sp.Rational(translation.numerator, translation.denominator)
    q = sp.Rational(contraction.numerator, contraction.denominator)
    for source_degree in range(degree):
        for target_degree in range(source_degree + 1):
            matrix[target_degree, source_degree] = (
                q
                * sp.binomial(source_degree, target_degree)
                * a ** (source_degree - target_degree)
                * q**target_degree
            )
    return matrix


def derivative_matrix(degree: int) -> sp.Matrix:
    derivative = sp.zeros(degree, degree + 1)
    for source_degree in range(1, degree + 1):
        derivative[source_degree - 1, source_degree] = source_degree
    return derivative


def marked_weight(label: int, s: int, u: Fraction) -> sp.Rational:
    return (
        sp.Rational(u.numerator, u.denominator) ** gamma_length(label)
        * sp.Rational(1, label**s)
    )


def finite_transfer(
    compiled: list[sp.Matrix],
    atoms: tuple[int, ...],
    s: int,
    u: Fraction,
) -> tuple[sp.Matrix, dict[int, sp.Rational]]:
    transfer = sp.zeros(compiled[0].rows)
    weights: dict[int, sp.Rational] = {}
    for index in atoms:
        label = index + 1
        weight = marked_weight(label, s, u)
        transfer += weight * compiled[index]
        weights[label] = weight
    return transfer, weights


def de_rham_tensor_transfers(
    relation: tuple[tuple[bool, ...], ...],
    degree: int,
    s: int,
    u: Fraction,
) -> tuple[sp.Matrix, sp.Matrix, dict[int, sp.Rational]]:
    _, _, compiled = compiled_idempotents(relation)
    atoms = covers_bottom(relation)
    size = len(relation)
    zero_transfer = sp.zeros(size * (degree + 1))
    one_transfer = sp.zeros(size * degree)
    weights: dict[int, sp.Rational] = {}
    for index in atoms:
        label = index + 1
        weight = marked_weight(label, s, u)
        translation, contraction = gamma_affine_branch(label)
        zero = affine_zero_form(degree, translation, contraction)
        one = affine_one_form(degree, translation, contraction)
        zero_transfer += weight * sp.kronecker_product(compiled[index], zero)
        one_transfer += weight * sp.kronecker_product(compiled[index], one)
        weights[label] = weight
    return zero_transfer, one_transfer, weights


def permute_matrix(matrix: sp.Matrix, permutation: tuple[int, ...]) -> sp.Matrix:
    return sp.Matrix(
        len(permutation),
        len(permutation),
        lambda row, column: matrix[permutation[row], permutation[column]],
    )


def mutate_six_to_cover(
    relation: tuple[tuple[bool, ...], ...],
) -> tuple[tuple[bool, ...], ...]:
    if len(relation) < 6:
        raise ValueError("mutation requires cutoff at least 6")
    mutable = [list(row) for row in relation]
    mutable[1][5] = False
    mutable[2][5] = False
    return tuple(tuple(row) for row in mutable)


def fraction_text(value: sp.Expr) -> str:
    value = sp.cancel(value)
    return str(value)
