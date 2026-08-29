#!/usr/bin/env python3
"""Exact finite controls for a Bernoulli signed-cat toral cocycle."""

from collections import defaultdict
from fractions import Fraction
from itertools import product


PLUS = ((2, 1), (1, 1))
MINUS = ((2, -1), (-1, 1))
GENERATORS = (PLUS, MINUS)
IDENTITY = ((1, 0), (0, 1))
ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def matmul(left, right):
    n = len(left)
    middle = len(right)
    m = len(right[0])
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(middle)) for j in range(m))
        for i in range(n)
    )


def matrix_power(matrix, n):
    size = len(matrix)
    result = tuple(tuple(Fraction(int(i == j)) for j in range(size)) for i in range(size))
    base = tuple(tuple(Fraction(x) for x in row) for row in matrix)
    while n:
        if n & 1:
            result = matmul(base, result)
        base = matmul(base, base)
        n //= 2
    return result


def product_matrix(word):
    matrix = IDENTITY
    for letter in word:
        matrix = matmul(GENERATORS[letter], matrix)
    return matrix


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def fixed_count(matrix):
    # det(M-I)=2-tr(M) because det(M)=1; all tested/contract words have tr>2.
    return abs((matrix[0][0] - 1) * (matrix[1][1] - 1) - matrix[0][1] * matrix[1][0])


def grid_fixed_count(matrix):
    modulus = fixed_count(matrix)
    count = 0
    for x in range(modulus):
        for y in range(modulus):
            if (
                ((matrix[0][0] - 1) * x + matrix[0][1] * y) % modulus == 0
                and (matrix[1][0] * x + (matrix[1][1] - 1) * y) % modulus == 0
            ):
                count += 1
    return count


def kronecker(left, right):
    return tuple(
        tuple(
            left[i // 2][j // 2] * right[i % 2][j % 2]
            for j in range(4)
        )
        for i in range(4)
    )


def average_matrix(p):
    q = 1 - p
    return tuple(
        tuple(p * PLUS[i][j] + q * MINUS[i][j] for j in range(2))
        for i in range(2)
    )


def average_tensor(p):
    q = 1 - p
    plus_tensor = kronecker(PLUS, PLUS)
    minus_tensor = kronecker(MINUS, MINUS)
    return tuple(
        tuple(p * plus_tensor[i][j] + q * minus_tensor[i][j] for j in range(4))
        for i in range(4)
    )


def run_exhaustive_lane():
    orientation_word = (0, 0, 1)
    check(product_matrix(orientation_word) != product_matrix(tuple(reversed(orientation_word))))
    check(trace(product_matrix(orientation_word)) == trace(product_matrix(tuple(reversed(orientation_word)))))

    for n in range(1, 17):
        histogram = defaultdict(int)
        traces = {}
        for word in product((0, 1), repeat=n):
            matrix = product_matrix(word)
            matrix_trace = trace(matrix)
            check(determinant(matrix) == 1)
            check(matrix_trace > 2)
            check(fixed_count(matrix) == matrix_trace - 2)
            histogram[matrix_trace - 2] += 1
            traces[word] = matrix_trace

            if n <= 5:
                check(grid_fixed_count(matrix) == fixed_count(matrix))

        check(sum(histogram.values()) == 2**n)
        maximum_trace = max(traces.values())
        minimum_trace = min(traces.values())
        check(maximum_trace == trace(matrix_power(PLUS, n)))
        check(sum(value == maximum_trace for value in traces.values()) == 2)
        alternating = tuple(i % 2 for i in range(n))
        check(minimum_trace == traces[alternating])
        check(sum(value == minimum_trace for value in traces.values()) == (2 if n % 2 == 0 else 2 * n))


def run_annealed_lane():
    for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
        q = 1 - p
        mean_matrix = average_matrix(p)
        tensor_matrix = average_tensor(p)
        sign_bias = 2 * p - 1
        check(mean_matrix == ((Fraction(2), sign_bias), (sign_bias, Fraction(1))))

        expected_trace_previous = Fraction(2)
        expected_trace_current = Fraction(3)
        for n in range(0, 15):
            mean_power = matrix_power(mean_matrix, n)
            tensor_power = matrix_power(tensor_matrix, n)
            exact_mean_trace = trace(mean_power)
            exact_second_trace = trace(tensor_power)

            enumerated_mean = Fraction(0)
            enumerated_second = Fraction(0)
            total_mass = Fraction(0)
            for word in product((0, 1), repeat=n):
                weight = p ** word.count(0) * q ** word.count(1)
                word_trace = trace(product_matrix(word))
                total_mass += weight
                enumerated_mean += weight * word_trace
                enumerated_second += weight * word_trace**2
            check(total_mass == 1)
            check(enumerated_mean == exact_mean_trace)
            check(enumerated_second == exact_second_trace)
            check(enumerated_mean - 2 == trace(mean_power) - 2)

            if n == 0:
                check(exact_mean_trace == expected_trace_previous)
            elif n == 1:
                check(exact_mean_trace == expected_trace_current)
            else:
                determinant_of_mean = 2 - sign_bias**2
                recurrence_value = 3 * expected_trace_current - determinant_of_mean * expected_trace_previous
                check(exact_mean_trace == recurrence_value)
                expected_trace_previous, expected_trace_current = expected_trace_current, exact_mean_trace

        # Exact deterministic endpoints are conjugate and have the same trace law.
        check(trace(matrix_power(PLUS, 12)) == trace(matrix_power(MINUS, 12)))

    # Multicone endpoint images: A_+ maps [-1,1] to [0,2/3],
    # A_- maps it to [-2/3,0].  This guards sign/orientation conventions.
    def slope_image(sign, slope):
        return (sign + slope) / (2 + sign * slope)

    check(slope_image(1, Fraction(-1)) == 0)
    check(slope_image(1, Fraction(1)) == Fraction(2, 3))
    check(slope_image(-1, Fraction(-1)) == Fraction(-2, 3))
    check(slope_image(-1, Fraction(1)) == 0)


if __name__ == "__main__":
    run_exhaustive_lane()
    run_annealed_lane()
    print("stochastic signed-cat spike: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal determinant/trace/extremizer horizon: n <= 16")
    print("annealed first/second moment horizon: n <= 14")
    print("orientation sentinel: reversal transposes but does not preserve the product")
    print("rare-event sentinel: constant words maximize and alternating words minimize trace for n >= 1")
