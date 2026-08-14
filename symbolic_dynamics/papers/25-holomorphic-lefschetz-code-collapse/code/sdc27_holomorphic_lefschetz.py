#!/usr/bin/env python3
"""Target-blind exact algebra for the SD-C27 holomorphic Lefschetz audit."""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import product
from typing import Iterable, Sequence

import sympy as sp


def elias_gamma_code(n: int) -> str:
    if n < 1:
        raise ValueError("n must be positive")
    bits = format(n, "b")
    return "0" * (len(bits) - 1) + bits


def gamma_length(n: int) -> int:
    return 2 * n.bit_length() - 1


def prefix_collision_pairs(words: Sequence[str]) -> int:
    word_set = set(words)
    if len(word_set) != len(words):
        raise ValueError("codes must be unique")
    return sum(
        1
        for word in words
        for stop in range(1, len(word))
        if word[:stop] in word_set
    )


def compose_code_branch(code: str) -> tuple[Fraction, Fraction]:
    """Apply digit maps in reading order: current map, then psi_bit."""
    translation = Fraction(0)
    derivative = Fraction(1)
    for bit in code:
        digit_translation = Fraction(-1, 4) if bit == "0" else Fraction(1, 4)
        translation = translation / 2 + digit_translation
        derivative /= 2
    return translation, derivative


def branch_for_integer(n: int) -> tuple[str, Fraction, Fraction]:
    code = elias_gamma_code(n)
    translation, derivative = compose_code_branch(code)
    return code, translation, derivative


def zero_form_matrix(
    translation: Fraction, derivative: Fraction, degree: int
) -> sp.Matrix:
    a = sp.Rational(translation.numerator, translation.denominator)
    q = sp.Rational(derivative.numerator, derivative.denominator)
    matrix = sp.zeros(degree + 1, degree + 1)
    for column in range(degree + 1):
        for row in range(column + 1):
            matrix[row, column] = sp.binomial(column, row) * a ** (
                column - row
            ) * q**row
    return matrix


def one_form_matrix(
    translation: Fraction, derivative: Fraction, degree: int
) -> sp.Matrix:
    """One-forms with polynomial coefficient degree at most degree-1."""
    if degree < 1:
        return sp.zeros(0, 0)
    q = sp.Rational(derivative.numerator, derivative.denominator)
    return q * zero_form_matrix(translation, derivative, degree - 1)


def differential_matrix(degree: int) -> sp.Matrix:
    matrix = sp.zeros(degree, degree + 1)
    for column in range(1, degree + 1):
        matrix[column - 1, column] = column
    return matrix


def weighted_sum_matrices(
    branches: Sequence[tuple[Fraction, Fraction, Fraction]], degree: int
) -> tuple[sp.Matrix, sp.Matrix, Fraction]:
    zero = sp.zeros(degree + 1, degree + 1)
    one = sp.zeros(degree, degree)
    total = Fraction(0)
    for weight, translation, derivative in branches:
        scalar = sp.Rational(weight.numerator, weight.denominator)
        zero += scalar * zero_form_matrix(translation, derivative, degree)
        one += scalar * one_form_matrix(translation, derivative, degree)
        total += weight
    return zero, one, total


def chain_certificate(
    branches: Sequence[tuple[Fraction, Fraction, Fraction]], degree: int
) -> dict[str, object]:
    zero, one, total = weighted_sum_matrices(branches, degree)
    differential = differential_matrix(degree)
    chain_residual = differential * zero - one * differential
    z = sp.symbols("z")
    zero_det = sp.factor((sp.eye(degree + 1) - z * zero).det())
    one_det = sp.factor((sp.eye(degree) - z * one).det())
    cohomology_factor = 1 - z * sp.Rational(total.numerator, total.denominator)
    determinant_residual = sp.expand(zero_det - cohomology_factor * one_det)
    return {
        "degree": degree,
        "branch_count": len(branches),
        "weight_sum": total,
        "chain_residual_zero": chain_residual == sp.zeros(degree, degree + 1),
        "zero_determinant": str(zero_det),
        "one_determinant": str(one_det),
        "cohomology_factor": str(cohomology_factor),
        "characteristic_quotient_exact": determinant_residual == 0,
        "ordinary_block_determinant": str(sp.factor(zero_det * one_det)),
        "ordinary_block_equals_graded_ratio": sp.expand(
            zero_det * one_det - cohomology_factor
        )
        == 0,
    }


def power_supertrace(
    branches: Sequence[tuple[Fraction, Fraction, Fraction]],
    degree: int,
    power: int,
) -> tuple[sp.Expr, sp.Expr]:
    zero, one, total = weighted_sum_matrices(branches, degree)
    actual = sp.trace(zero**power) - sp.trace(one**power)
    expected = sp.Rational(total.numerator, total.denominator) ** power
    return sp.factor(actual), sp.factor(expected)


def scalar_rigidity(q: Fraction, power: int) -> tuple[Fraction, Fraction]:
    alpha = 1 - q
    normalized = alpha**power / (1 - q**power)
    return normalized, normalized - 1


def desired_ordinary_fiber_determinant(q: Fraction) -> tuple[str, bool]:
    t = sp.symbols("t")
    q_sp = sp.Rational(q.numerator, q.denominator)
    value = sp.factor((1 - t) / (1 - q_sp * t))
    return str(value), q != 0


def two_by_two_moment_control(q: Fraction) -> dict[str, Fraction]:
    p1 = 1 - q
    p2 = 1 - q**2
    elementary_2 = (p1**2 - p2) / 2
    predicted_p3 = p1 * p2 - elementary_2 * p1
    desired_p3 = 1 - q**3
    return {
        "p1": p1,
        "p2": p2,
        "e2": elementary_2,
        "predicted_p3": predicted_p3,
        "desired_p3": desired_p3,
        "p3_residual": predicted_p3 - desired_p3,
    }


def centered_local_determinants(
    weight: Fraction, q: Fraction, degree: int
) -> dict[str, object]:
    z = sp.symbols("z")
    w_sp = sp.Rational(weight.numerator, weight.denominator)
    q_sp = sp.Rational(q.numerator, q.denominator)
    zero = sp.factor(sp.prod(1 - z * w_sp * q_sp**mode for mode in range(degree + 1)))
    one = sp.factor(sp.prod(1 - z * w_sp * q_sp**mode for mode in range(1, degree + 1)))
    quotient = sp.cancel(zero / one)
    expected = 1 - z * w_sp
    ordinary = sp.factor(zero * one)
    return {
        "zero": str(zero),
        "one": str(one),
        "quotient": str(quotient),
        "expected": str(expected),
        "quotient_exact": sp.expand(quotient - expected) == 0,
        "ordinary_block": str(ordinary),
        "ordinary_equals_graded": sp.expand(ordinary - expected) == 0,
    }


def shared_disjoint_polynomials(weights: Sequence[Fraction]) -> dict[str, object]:
    z = sp.symbols("z")
    values = [sp.Rational(weight.numerator, weight.denominator) for weight in weights]
    shared = sp.factor(1 - z * sum(values))
    disjoint = sp.factor(sp.prod(1 - z * value for value in values))
    return {
        "shared": str(shared),
        "disjoint": str(disjoint),
        "difference": str(sp.factor(shared - disjoint)),
        "equal": sp.expand(shared - disjoint) == 0,
    }


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def is_primitive(word: tuple[int, ...]) -> bool:
    length = len(word)
    return not any(
        word == word[:period] * (length // period)
        for period in range(1, length)
        if length % period == 0
    )


def primitive_necklaces(alphabet_size: int, max_length: int) -> list[tuple[int, ...]]:
    necklaces: set[tuple[int, ...]] = set()
    for length in range(1, max_length + 1):
        for word in product(range(alphabet_size), repeat=length):
            if is_primitive(word):
                necklaces.add(canonical_rotation(word))
    return sorted(necklaces, key=lambda word: (len(word), word))


def necklace_weight(word: Sequence[int], weights: Sequence[Fraction]) -> Fraction:
    value = Fraction(1)
    for label in word:
        value *= weights[label]
    return value


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def polynomial_text(value: sp.Expr) -> str:
    return str(sp.factor(value))

