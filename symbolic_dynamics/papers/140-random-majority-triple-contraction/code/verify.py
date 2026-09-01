#!/usr/bin/env python3
"""Exact controls for P140.

The program is self-contained and deterministic.  It uses integers and
fractions.Fraction only: no floating point, sampling, seed, network access,
timestamp, or third-party package.  Its stdout is frozen byte-for-byte in
verification_output.txt.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product


ASSERTIONS = 0


def check(condition, payload=None):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(payload)


def odd_double_factorial(value):
    result = 1
    for factor in range(value, 0, -2):
        result *= factor
    return result


def int_poly_add(left, right):
    out = [0] * max(len(left), len(right))
    for degree, coefficient in enumerate(left):
        out[degree] += coefficient
    for degree, coefficient in enumerate(right):
        out[degree] += coefficient
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def int_poly_scale(poly, scalar, shift=0):
    return (0,) * shift + tuple(scalar * coefficient for coefficient in poly)


@lru_cache(maxsize=None)
def terminal_probability(word):
    if len(word) == 1:
        return Fraction(word[0])
    denominator = len(word) - 2
    answer = Fraction(0)
    for index in range(denominator):
        majority = int(sum(word[index:index + 3]) >= 2)
        successor = word[:index] + (majority,) + word[index + 3:]
        answer += terminal_probability(successor) / denominator
    return answer


@lru_cache(maxsize=None)
def terminal_history_counts(word):
    if len(word) == 1:
        return (int(word[0] == 0), int(word[0] == 1))
    zero_count = one_count = 0
    for index in range(len(word) - 2):
        majority = int(sum(word[index:index + 3]) >= 2)
        successor = word[:index] + (majority,) + word[index + 3:]
        zeros, ones = terminal_history_counts(successor)
        zero_count += zeros
        one_count += ones
    return zero_count, one_count


@lru_cache(maxsize=None)
def literal_cross_history_counts(word):
    """Return zero/one history polynomials marked by heterogeneous triples."""
    if len(word) == 1:
        return ((1,), (0,)) if word[0] == 0 else ((0,), (1,))
    zero_poly = (0,)
    one_poly = (0,)
    for index in range(len(word) - 2):
        window = word[index:index + 3]
        majority = int(sum(window) >= 2)
        successor = word[:index] + (majority,) + word[index + 3:]
        zeros, ones = literal_cross_history_counts(successor)
        shift = int(not (window[0] == window[1] == window[2]))
        zero_poly = int_poly_add(zero_poly, int_poly_scale(zeros, 1, shift))
        one_poly = int_poly_add(one_poly, int_poly_scale(ones, 1, shift))
    return zero_poly, one_poly


@lru_cache(maxsize=None)
def joint_laplace_one(word, s):
    """E[exp(-s tau) 1{terminal=1}] for rate-one current-window clocks."""
    if len(word) == 1:
        return Fraction(word[0])
    rate = len(word) - 2
    answer = Fraction(0)
    for index in range(rate):
        majority = int(sum(word[index:index + 3]) >= 2)
        successor = word[:index] + (majority,) + word[index + 3:]
        answer += joint_laplace_one(successor, s) / (rate + s)
    return answer


@lru_cache(maxsize=None)
def cross_history_one(a, b):
    if a == 0:
        return (odd_double_factorial(b - 2),)
    if b == 0:
        return (0,)
    answer = (0,)
    if a >= 3:
        answer = int_poly_add(
            answer, int_poly_scale(cross_history_one(a - 2, b), a - 2)
        )
    if b >= 3:
        answer = int_poly_add(
            answer, int_poly_scale(cross_history_one(a, b - 2), b - 2)
        )
    crossing = int(a >= 2) + int(b >= 2)
    if crossing:
        answer = int_poly_add(
            answer, int_poly_scale(cross_history_one(a - 1, b - 1), crossing, 1)
        )
    return answer


@lru_cache(maxsize=None)
def two_run_probability(a, b):
    if a == 0:
        return Fraction(1)
    if b == 0:
        return Fraction(0)
    n = a + b
    check(n >= 3 and n % 2 == 1, (a, b))
    denominator = n - 2
    answer = Fraction(0)
    if a >= 3:
        answer += Fraction(a - 2, denominator) * two_run_probability(a - 2, b)
    if b >= 3:
        answer += Fraction(b - 2, denominator) * two_run_probability(a, b - 2)
    crossing = int(a >= 2) + int(b >= 2)
    if crossing:
        answer += Fraction(crossing, denominator) * two_run_probability(a - 1, b - 1)
    check(max(a - 2, 0) + max(b - 2, 0) + crossing == denominator, (a, b))
    return answer


def verify():
    words = 0
    two_runs = 0
    transform_cells = 0
    cross_coefficients = 0

    for n in range(1, 16, 2):
        histories = odd_double_factorial(n - 2)
        for word in product((0, 1), repeat=n):
            word = tuple(word)
            probability = terminal_probability(word)
            zeros, ones = terminal_history_counts(word)
            check(zeros + ones == histories, (word, zeros, ones, histories))
            check(probability == Fraction(ones, histories), (word, probability))
            check(0 <= probability <= 1, (word, probability))
            if n <= 11:
                time_transform = Fraction(1)
                for rate in range(1, n - 1, 2):
                    time_transform *= Fraction(rate, rate + 3)
                joint = joint_laplace_one(word, 3)
                check(joint == probability * time_transform, (word, joint))
            words += 1

    for n in range(3, 202, 2):
        histories = odd_double_factorial(n - 2)
        for a in range(1, n):
            b = n - a
            formula = Fraction(b - 1, n - 2)
            check(two_run_probability(a, b) == formula, (a, b))
            check(
                (a - 1) * odd_double_factorial(n - 4)
                + (b - 1) * odd_double_factorial(n - 4)
                == histories,
                (a, b),
            )
            if n <= 101:
                one_poly = cross_history_one(a, b)
                zero_poly = cross_history_one(b, a)
                check(sum(one_poly) == (b - 1) * odd_double_factorial(n - 4))
                check(sum(zero_poly) == (a - 1) * odd_double_factorial(n - 4))
                one_support = ([] if b == 1 else [
                    c for c in range(1, min(a, b - 1) + 1)
                    if c % 2 == a % 2
                ])
                zero_support = ([] if a == 1 else [
                    c for c in range(1, min(b, a - 1) + 1)
                    if c % 2 == b % 2
                ])
                check([c for c, value in enumerate(one_poly) if value] == one_support)
                check([c for c, value in enumerate(zero_poly) if value] == zero_support)
                one_linear = one_poly[1] if len(one_poly) > 1 else 0
                zero_linear = zero_poly[1] if len(zero_poly) > 1 else 0
                check(one_linear == (histories // a if a % 2 else 0), (a, b))
                check(zero_linear == (histories // b if b % 2 else 0), (a, b))
                if n <= 13:
                    literal_zero, literal_one = literal_cross_history_counts(
                        (0,) * a + (1,) * b
                    )
                    check(literal_one == one_poly, (a, b))
                    check(literal_zero == zero_poly, (a, b))
                cross_coefficients += len(one_poly) + len(zero_poly)
            if n <= 15:
                check(terminal_probability((0,) * a + (1,) * b) == formula)
            two_runs += 1

        mean = sum((Fraction(1, k) for k in range(1, n - 1, 2)), Fraction(0))
        variance = sum(
            (Fraction(1, k * k) for k in range(1, n - 1, 2)), Fraction(0)
        )
        check(mean >= 0 and variance >= 0)
        for s in range(1, 11):
            forward = Fraction(1)
            backward = Fraction(1)
            for rate in range(1, n - 1, 2):
                forward *= Fraction(rate, rate + s)
            for rate in range(n - 2, 0, -2):
                backward *= Fraction(rate, rate + s)
            check(forward == backward, (n, s))
            transform_cells += 1

    return words, two_runs, cross_coefficients, transform_cells


if __name__ == "__main__":
    report = verify()
    print("P140_RANDOM_MAJORITY_TRIPLE_CONTRACTION")
    print("arithmetic=fractions.Fraction; sampling=none; third_party=none")
    print(f"binary_words={report[0]}")
    print(f"two_run_inputs={report[1]}")
    print(f"cross_polynomial_coefficients={report[2]}")
    print(f"clock_transform_cells={report[3]}")
    print(f"exact_assertions={ASSERTIONS}")
    print("checks=closure,endpoint,history_count,cross_pgf,cross_support,one_cross,clock_independence,laplace_product")
    print("status=PASS")
