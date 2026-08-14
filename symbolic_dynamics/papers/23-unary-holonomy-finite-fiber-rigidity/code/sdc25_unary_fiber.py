#!/usr/bin/env python3
"""Exact source-side utilities for frozen candidate SD-C25.

This module contains only the successor--divisor source, its ordered
cofactor word, fixed finite-state/fixed-dimensional fibers, and exact
same-object operator calculations.  Target predicates and post-freeze
controls live in ``sdc25_evaluator.py``.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from itertools import product
from typing import Iterable, Sequence


CANDIDATE_ID = "SD-C25"
SOURCE_AUDIT_CUTOFF = 4096
STATE_SIZES = (1, 2, 3, 4)
RECURRENCE_DIMENSIONS = tuple(range(1, 9))
MEMORY_CUTOFFS = (32, 64, 128, 256)
BLOCK_CUTOFF = 9
BLOCK_MAX_POWER = 32
TRACE_SIGMAS = ("0.45", "0.49", "0.50", "0.51", "0.60", "1.00")
TRACE_CUTOFFS = (32, 64, 128, 256, 512, 1024, 2048, 4096)

Matrix = tuple[tuple[Fraction, ...], ...]


def edge_quotient(source: int, target: int) -> int:
    """Return the unique quotient on a frozen successor--divisor edge."""

    if source < 2 or target < 2 or (source + 1) % target:
        raise ValueError(f"not a frozen edge: {source}->{target}")
    return (source + 1) // target


def canonical_cycle(index: int) -> tuple[int, ...]:
    if index < 2:
        raise ValueError("index must be at least two")
    return tuple(range(index, 2 * index))


def ordered_quotient_word(cycle: Sequence[int]) -> tuple[int, ...]:
    vertices = tuple(cycle)
    if not vertices:
        return ()
    return tuple(
        edge_quotient(vertices[position], vertices[(position + 1) % len(vertices)])
        for position in range(len(vertices))
    )


def canonical_word_certificate(index: int) -> dict[str, int | bool]:
    """Audit every edge and the ordered word of the canonical cycle."""

    cycle = canonical_cycle(index)
    word = ordered_quotient_word(cycle)
    holonomy = 1
    for value in word:
        holonomy *= value
    return {
        "index": index,
        "length": len(cycle),
        "one_count": sum(value == 1 for value in word),
        "terminal_value": word[-1],
        "holonomy": holonomy,
        "all_edges_valid": all(
            (cycle[position] + 1) % cycle[(position + 1) % len(cycle)] == 0
            for position in range(len(cycle))
        ),
        "ordered_word_match": word == (1,) * (index - 1) + (2,),
        "unique_minimum_mark": cycle.count(min(cycle)) == 1 and cycle[0] == min(cycle),
        "primitive": len(set(cycle)) == len(cycle),
    }


def transformation_tail_period(
    mapping: Sequence[int], start: int = 0
) -> tuple[int, int]:
    """Return the exact exponent tail and period of one transformation orbit."""

    values = tuple(mapping)
    if not values or any(value < 0 or value >= len(values) for value in values):
        raise ValueError("mapping must be a total map on 0,...,q-1")
    if start < 0 or start >= len(values):
        raise ValueError("invalid start")
    seen: dict[int, int] = {}
    current = start
    exponent = 0
    while current not in seen:
        seen[current] = exponent
        current = values[current]
        exponent += 1
    return seen[current], exponent - seen[current]


def transformation_power_state(
    mapping: Sequence[int], exponent: int, start: int = 0
) -> int:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    current = start
    for _ in range(exponent):
        current = mapping[current]
    return current


def terminal_response_state(
    mapping: Sequence[int], terminal: Sequence[int], index: int, start: int = 0
) -> int:
    if index < 1:
        raise ValueError("index must be positive")
    return terminal[transformation_power_state(mapping, index - 1, start)]


def relation_identity(size: int) -> int:
    return sum(1 << (row * size + row) for row in range(size))


def relation_compose(left: int, right: int, size: int) -> int:
    """Return left after right for Boolean relations encoded as bit masks."""

    output = 0
    for source in range(size):
        for middle in range(size):
            if not (right >> (source * size + middle)) & 1:
                continue
            for target in range(size):
                if (left >> (middle * size + target)) & 1:
                    output |= 1 << (source * size + target)
    return output


def relation_tail_period(relation: int, size: int) -> tuple[int, int]:
    """Return the exact tail/period of R^e starting at exponent zero."""

    seen: dict[int, int] = {}
    current = relation_identity(size)
    exponent = 0
    while current not in seen:
        seen[current] = exponent
        current = relation_compose(relation, current, size)
        exponent += 1
    return seen[current], exponent - seen[current]


def relation_power(relation: int, exponent: int, size: int) -> int:
    current = relation_identity(size)
    for _ in range(exponent):
        current = relation_compose(relation, current, size)
    return current


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(size)) for _ in range(size))


def identity_matrix(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def matrix_from(values: Sequence[Sequence[int | Fraction]]) -> Matrix:
    matrix = tuple(tuple(Fraction(value) for value in row) for row in values)
    if matrix and any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be square")
    return matrix


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    if len(right) != size:
        raise ValueError("dimension mismatch")
    output = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for pivot in range(size):
            coefficient = left[row][pivot]
            if coefficient == 0:
                continue
            for column in range(size):
                if right[pivot][column]:
                    output[row][column] += coefficient * right[pivot][column]
    return tuple(tuple(row) for row in output)


def matrix_add_scalar_identity(matrix: Matrix, scalar: Fraction) -> Matrix:
    return tuple(
        tuple(
            matrix[row][column] + (scalar if row == column else Fraction(0))
            for column in range(len(matrix))
        )
        for row in range(len(matrix))
    )


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    result = identity_matrix(len(matrix))
    base = matrix
    value = exponent
    while value:
        if value & 1:
            result = matrix_multiply(result, base)
        value >>= 1
        if value:
            base = matrix_multiply(base, base)
    return result


def characteristic_coefficients(matrix: Matrix) -> tuple[Fraction, ...]:
    """Return c_1,...,c_d for det(tI-A)=t^d+c_1t^(d-1)+...+c_d."""

    size = len(matrix)
    auxiliary = identity_matrix(size)
    coefficients: list[Fraction] = []
    for order in range(1, size + 1):
        multiplied = matrix_multiply(matrix, auxiliary)
        coefficient = -matrix_trace(multiplied) / order
        coefficients.append(coefficient)
        auxiliary = matrix_add_scalar_identity(multiplied, coefficient)
    return tuple(coefficients)


def matrix_is_zero(matrix: Matrix) -> bool:
    return all(value == 0 for row in matrix for value in row)


def cayley_hamilton_matrix(matrix: Matrix) -> Matrix:
    coefficients = characteristic_coefficients(matrix)
    size = len(matrix)
    result = matrix_power(matrix, size)
    for offset, coefficient in enumerate(coefficients, start=1):
        term = matrix_power(matrix, size - offset)
        result = tuple(
            tuple(
                result[row][column] + coefficient * term[row][column]
                for column in range(size)
            )
            for row in range(size)
        )
    return result


def row_vector_times_matrix(vector: Sequence[Fraction], matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(
        sum((vector[row] * matrix[row][column] for row in range(len(matrix))), Fraction(0))
        for column in range(len(matrix))
    )


def matrix_times_vector(matrix: Matrix, vector: Sequence[Fraction]) -> tuple[Fraction, ...]:
    return tuple(
        sum((matrix[row][column] * vector[column] for column in range(len(matrix))), Fraction(0))
        for row in range(len(matrix))
    )


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def response_sequences(
    a_matrix: Matrix,
    b_matrix: Matrix,
    left_vector: Sequence[Fraction],
    right_vector: Sequence[Fraction],
    count: int,
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    power = identity_matrix(len(a_matrix))
    bilinear: list[Fraction] = []
    traces: list[Fraction] = []
    for _index in range(1, count + 1):
        product_matrix = matrix_multiply(power, b_matrix)
        bilinear.append(
            dot(row_vector_times_matrix(left_vector, product_matrix), right_vector)
        )
        traces.append(matrix_trace(product_matrix))
        power = matrix_multiply(power, a_matrix)
    return tuple(bilinear), tuple(traces)


def recurrence_residuals(
    sequence: Sequence[Fraction], coefficients: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    order = len(coefficients)
    residuals: list[Fraction] = []
    for start in range(len(sequence) - order):
        value = sequence[start + order]
        for offset, coefficient in enumerate(coefficients, start=1):
            value += coefficient * sequence[start + order - offset]
        residuals.append(value)
    return tuple(residuals)


def generating_numerator(
    sequence: Sequence[Fraction], coefficients: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    denominator = (Fraction(1), *coefficients)
    return tuple(
        sum(
            (denominator[offset] * sequence[degree - offset] for offset in range(degree + 1)),
            Fraction(0),
        )
        for degree in range(len(coefficients))
    )


def generating_series_from_rational(
    numerator: Sequence[Fraction],
    coefficients: Sequence[Fraction],
    count: int,
) -> tuple[Fraction, ...]:
    denominator = (Fraction(1), *coefficients)
    output: list[Fraction] = []
    for degree in range(count):
        value = numerator[degree] if degree < len(numerator) else Fraction(0)
        for offset in range(1, min(degree, len(coefficients)) + 1):
            value -= denominator[offset] * output[degree - offset]
        output.append(value)
    return tuple(output)


def _linear_system_consistent(rows: Sequence[Sequence[Fraction]], width: int) -> bool:
    matrix = [list(row) for row in rows]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or matrix[row][column] == 0:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                matrix[row][entry] - factor * matrix[pivot_row][entry]
                for entry in range(width + 1)
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return not any(
        all(row[column] == 0 for column in range(width)) and row[width] != 0
        for row in matrix
    )


def minimal_recurrence_order(sequence: Sequence[Fraction], maximum: int) -> int:
    if all(value == 0 for value in sequence):
        return 0
    for order in range(1, maximum + 1):
        rows = [
            [*sequence[start : start + order], -sequence[start + order]]
            for start in range(len(sequence) - order)
        ]
        if rows and _linear_system_consistent(rows, order):
            return order
    return maximum


def memorizer_response(target: Sequence[Fraction], index: int) -> Fraction:
    """Sparse value of either frozen nilpotent prefix memorizer."""

    return target[index - 1] if 1 <= index <= len(target) else Fraction(0)


def q12_edges(source: int, cutoff: int) -> tuple[tuple[int, int], ...]:
    output: list[tuple[int, int]] = []
    if source + 1 <= cutoff:
        output.append((source + 1, 1))
    if source % 2 == 1:
        target = (source + 1) // 2
        if 2 <= target <= cutoff:
            output.append((target, 2))
    return tuple(output)


def block_adjacency(
    cutoff: int, a_matrix: Matrix, b_matrix: Matrix, s_integer: int = 1
) -> Matrix:
    if len(a_matrix) != len(b_matrix):
        raise ValueError("fiber dimensions differ")
    fiber = len(a_matrix)
    size = (cutoff - 1) * fiber
    output = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for source in range(2, cutoff + 1):
        for target, quotient in q12_edges(source, cutoff):
            scalar = Fraction(1, (source * target) ** s_integer)
            block = a_matrix if quotient == 1 else b_matrix
            for row in range(fiber):
                for column in range(fiber):
                    output[(target - 2) * fiber + row][(source - 2) * fiber + column] += (
                        scalar * block[row][column]
                    )
    return tuple(tuple(row) for row in output)


def finite_power_traces(matrix: Matrix, max_power: int) -> tuple[Fraction, ...]:
    power = matrix
    traces: list[Fraction] = []
    for exponent in range(1, max_power + 1):
        traces.append(matrix_trace(power))
        if exponent != max_power:
            power = matrix_multiply(power, matrix)
    return tuple(traces)


def newton_determinant_coefficients(traces: Sequence[Fraction]) -> tuple[Fraction, ...]:
    coefficients = [Fraction(1)]
    for degree in range(1, len(traces) + 1):
        value = -sum(
            (traces[power - 1] * coefficients[degree - power] for power in range(1, degree + 1)),
            Fraction(0),
        ) / degree
        coefficients.append(value)
    return tuple(coefficients)


def polynomial_value(coefficients: Sequence[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def fraction_determinant(matrix: Matrix) -> Fraction:
    values = [list(row) for row in matrix]
    size = len(values)
    determinant = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if values[row][column]),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            values[column], values[pivot] = values[pivot], values[column]
            determinant = -determinant
        pivot_value = values[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            if values[row][column] == 0:
                continue
            factor = values[row][column] / pivot_value
            values[row][column] = Fraction(0)
            for inner in range(column + 1, size):
                values[row][inner] -= factor * values[column][inner]
    return determinant


def identity_minus_scaled(matrix: Matrix, value: Fraction) -> Matrix:
    return tuple(
        tuple(
            Fraction(int(row == column)) - value * matrix[row][column]
            for column in range(len(matrix))
        )
        for row in range(len(matrix))
    )


def canonical_fiber_trace(
    index: int, a_matrix: Matrix, b_matrix: Matrix
) -> tuple[Fraction, Fraction]:
    left = matrix_trace(matrix_multiply(matrix_power(a_matrix, index - 1), b_matrix))
    column_source = matrix_trace(matrix_multiply(b_matrix, matrix_power(a_matrix, index - 1)))
    return left, column_source


def canonical_mass(index: int) -> int:
    result = 1
    for value in range(index, 2 * index):
        result *= value
    return result


def decimal_edge_prefix_interval(
    cutoff: int, sigma_text: str, family: str
) -> tuple[Decimal, Decimal]:
    """Directed-rounding interval for one scalar edge nuclear prefix."""

    if family not in {"successor", "return"}:
        raise ValueError("unknown edge family")

    def compute(rounding: str) -> Decimal:
        with localcontext() as context:
            context.prec = 60
            context.rounding = rounding
            sigma = Decimal(sigma_text)
            total = Decimal(0)
            if family == "successor":
                bases: Iterable[int] = (source * (source + 1) for source in range(2, cutoff + 1))
            else:
                bases = (
                    (2 * target - 1) * target
                    for target in range(2, (cutoff + 1) // 2 + 1)
                )
            for base in bases:
                logarithm = Decimal(base).ln(context=context)
                term = (-sigma * logarithm).exp(context=context)
                total += term
            return +total

    return compute(ROUND_FLOOR), compute(ROUND_CEILING)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def vector_text(values: Sequence[Fraction]) -> str:
    return "[" + ",".join(fraction_text(value) for value in values) + "]"


def matrix_text(matrix: Matrix) -> str:
    return "[" + ";".join(",".join(fraction_text(value) for value in row) for row in matrix) + "]"


def all_transformations(size: int) -> Iterable[tuple[int, ...]]:
    return product(range(size), repeat=size)
