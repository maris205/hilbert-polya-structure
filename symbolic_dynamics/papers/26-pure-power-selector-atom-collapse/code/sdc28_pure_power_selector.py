#!/usr/bin/env python3
"""Exact algebra for the SD-C28 pure-power cyclic selector.

The candidate core is inventory-blind: colors are opaque integer labels and
no arithmetic predicate occurs here.  All matrices use exact SymPy entries.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp


def words(color_count: int, max_length: int):
    """Yield every nonempty word in length-lexicographic order."""
    for length in range(1, max_length + 1):
        yield from itertools.product(range(color_count), repeat=length)


def all_words_through(color_count: int, max_length: int):
    answer: list[tuple[int, ...]] = [()]
    for length in range(1, max_length + 1):
        answer.extend(itertools.product(range(color_count), repeat=length))
    return answer


def monochromatic_selector(word: tuple[int, ...]) -> int:
    return int(bool(word) and len(set(word)) == 1)


def completed_selector(
    word: tuple[int, ...], color_count: int, empty_value: int
) -> int:
    if not word:
        return empty_value
    return monochromatic_selector(word)


def matrix_product(
    matrices: list[sp.Matrix], word: tuple[int, ...]
) -> sp.Matrix:
    product = sp.eye(matrices[0].rows)
    for letter in word:
        product = product * matrices[letter]
    return product


def projector_matrices(color_count: int) -> list[sp.Matrix]:
    matrices: list[sp.Matrix] = []
    for color in range(color_count):
        matrix = sp.zeros(color_count)
        matrix[color, color] = 1
        matrices.append(matrix)
    return matrices


def radical_matrices(color_count: int) -> list[sp.Matrix]:
    """Noncommuting triangular extensions of color characters plus dormants."""
    dimension = color_count + 2
    matrices: list[sp.Matrix] = []
    for color in range(color_count):
        matrix = sp.zeros(dimension)
        matrix[color, color] = 1
        for row in range(dimension):
            for column in range(row + 1, dimension):
                raw = ((color + 1) * (row + 2) + 3 * (column + 1)) % 7 - 3
                matrix[row, column] = raw if raw != 0 else color + 1
        matrices.append(matrix)
    return matrices


def common_block(color: int) -> sp.Matrix:
    """A deterministic, generally noncommuting two-dimensional module."""
    return sp.Matrix(
        [[color + 2, 1 - color], [color + 1, 2 * color - 1]]
    )


def graded_extension_matrices(
    color_count: int,
) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    """Even = color characters plus a common block; odd = common block."""
    even: list[sp.Matrix] = []
    odd: list[sp.Matrix] = []
    for color in range(color_count):
        atomic = sp.zeros(color_count)
        atomic[color, color] = 1
        common = common_block(color)
        coupling = sp.Matrix(
            color_count,
            2,
            lambda row, column: (
                ((row + 1) * (color + 2) + column + 1) % 5 - 2
            ),
        )
        even_matrix = atomic.row_join(coupling).col_join(
            sp.zeros(2, color_count).row_join(common)
        )
        even.append(even_matrix)
        odd.append(common)
    return even, odd


def reversal_adversary_matrices(
) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    """Aggregate-exact graded pair with oriented mixed-word defects."""
    atomic = projector_matrices(3)
    common: list[sp.Matrix] = []
    for row, column in ((0, 1), (1, 2), (2, 0)):
        matrix = sp.zeros(3)
        matrix[row, column] = 1
        common.append(matrix)
    even = [sp.diag(atomic[i], common[i]) for i in range(3)]
    odd = [common[i].T for i in range(3)]
    return even, odd


def hankel_rank(
    color_count: int, depth: int, empty_value: int
) -> tuple[int, int]:
    index = all_words_through(color_count, depth)
    matrix = sp.Matrix(
        [
            [
                completed_selector(left + right, color_count, empty_value)
                for right in index
            ]
            for left in index
        ]
    )
    return int(matrix.rank()), len(index)


def support_exterior_certificate(support_size: int) -> dict[str, object]:
    dimensions = [
        int(sp.binomial(support_size - 1, degree))
        for degree in range(support_size)
    ]
    alternating_sum = sum(
        (-1) ** degree * dimension
        for degree, dimension in enumerate(dimensions)
    )
    return {
        "support_size": support_size,
        "reduced_dimension": support_size - 1,
        "exterior_dimensions": dimensions,
        "superdimension": alternating_sum,
        "expected": int(support_size == 1),
        "exact": alternating_sum == int(support_size == 1),
        "mixed_cohomology_nonzero": support_size > 1,
    }


def color_algebra_certificate(color_count: int) -> dict[str, object]:
    matrices = projector_matrices(color_count)
    multiplication_failures = 0
    centrality_failures = 0
    identity = sum(matrices, sp.zeros(color_count))
    for left in range(color_count):
        for right in range(color_count):
            expected = matrices[left] if left == right else sp.zeros(color_count)
            if matrices[left] * matrices[right] != expected:
                multiplication_failures += 1
        # The diagonal separability tensor sum e_i (x) e_i commutes with each
        # primitive idempotent on its two tensor legs.  This finite matrix
        # equality is the exact source of the standard Hochschild contraction.
        for index in range(color_count):
            lhs = sp.kronecker_product(matrices[left] * matrices[index], matrices[index])
            rhs = sp.kronecker_product(matrices[index], matrices[index] * matrices[left])
            if lhs != rhs:
                centrality_failures += 1
    return {
        "color_count": color_count,
        "algebra_dimension": color_count,
        "primitive_idempotents": color_count,
        "multiplication_checks": color_count**2,
        "multiplication_failures": multiplication_failures,
        "separability_centrality_checks": color_count**2,
        "separability_centrality_failures": centrality_failures,
        "separability_multiplication_is_identity": identity == sp.eye(color_count),
        "hh0_dimension": color_count,
        "positive_hh_dimension": 0,
        "surviving_sector": "direct_sum_of_color_lines",
    }


def affine_pullback_zero(
    degree: int, translation: Fraction, contraction: Fraction, weight: Fraction
) -> sp.Matrix:
    """Pullback by z -> translation + contraction*z on polynomials <= degree."""
    matrix = sp.zeros(degree + 1)
    a = sp.Rational(translation.numerator, translation.denominator)
    q = sp.Rational(contraction.numerator, contraction.denominator)
    w = sp.Rational(weight.numerator, weight.denominator)
    for source_degree in range(degree + 1):
        for target_degree in range(source_degree + 1):
            matrix[target_degree, source_degree] = (
                w
                * sp.binomial(source_degree, target_degree)
                * a ** (source_degree - target_degree)
                * q**target_degree
            )
    return matrix


def affine_pullback_one(
    degree: int, translation: Fraction, contraction: Fraction, weight: Fraction
) -> sp.Matrix:
    """Pullback on polynomial one-forms of coefficient degree <= degree-1."""
    if degree < 1:
        return sp.zeros(0)
    matrix = sp.zeros(degree)
    a = sp.Rational(translation.numerator, translation.denominator)
    q = sp.Rational(contraction.numerator, contraction.denominator)
    w = sp.Rational(weight.numerator, weight.denominator)
    for source_degree in range(degree):
        for target_degree in range(source_degree + 1):
            matrix[target_degree, source_degree] = (
                w
                * q
                * sp.binomial(source_degree, target_degree)
                * a ** (source_degree - target_degree)
                * q**target_degree
            )
    return matrix


def derivative_matrix(degree: int) -> sp.Matrix:
    matrix = sp.zeros(degree, degree + 1)
    for source_degree in range(1, degree + 1):
        matrix[source_degree - 1, source_degree] = source_degree
    return matrix


def de_rham_local_certificate(
    degree: int,
    translation: Fraction,
    contraction: Fraction,
    weight: Fraction,
    max_power: int,
) -> dict[str, object]:
    zero = affine_pullback_zero(degree, translation, contraction, weight)
    one = affine_pullback_one(degree, translation, contraction, weight)
    derivative = derivative_matrix(degree)
    power_rows: list[dict[str, object]] = []
    w = sp.Rational(weight.numerator, weight.denominator)
    for power in range(1, max_power + 1):
        actual = sp.trace(zero**power) - sp.trace(one**power)
        expected = w**power
        power_rows.append(
            {
                "power": power,
                "actual": str(actual),
                "expected": str(expected),
                "exact": sp.expand(actual - expected) == 0,
            }
        )
    z = sp.symbols("z")
    zero_det = sp.factor((sp.eye(zero.rows) - z * zero).det())
    one_det = sp.factor((sp.eye(one.rows) - z * one).det())
    quotient_residual = sp.factor(zero_det - (1 - z * w) * one_det)
    return {
        "degree": degree,
        "translation": fraction_text(translation),
        "contraction": fraction_text(contraction),
        "weight": fraction_text(weight),
        "chain_exact": derivative * zero == one * derivative,
        "zero_determinant": str(zero_det),
        "one_determinant": str(one_det),
        "quotient_factor": str(1 - z * w),
        "quotient_exact": quotient_residual == 0,
        "power_rows": power_rows,
    }


def tensor_de_rham_word_supertrace(
    word: tuple[int, ...],
    zero_matrices: list[sp.Matrix],
    one_matrices: list[sp.Matrix],
) -> sp.Expr:
    projectors = projector_matrices(len(zero_matrices))
    zero_tensor = [
        sp.kronecker_product(projectors[index], zero_matrices[index])
        for index in range(len(projectors))
    ]
    one_tensor = [
        sp.kronecker_product(projectors[index], one_matrices[index])
        for index in range(len(projectors))
    ]
    return sp.trace(matrix_product(zero_tensor, word)) - sp.trace(
        matrix_product(one_tensor, word)
    )


def gamma_length(integer: int) -> int:
    if integer < 1:
        raise ValueError("integer must be positive")
    return 2 * (integer.bit_length() - 1) + 1


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"
