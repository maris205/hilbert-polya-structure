#!/usr/bin/env python3
"""Exact finite controls for a Bernoulli max-plus resonance cocycle.

The script is deliberately standard-library only.  It compares literal
max-plus matrix products with an independently coded three-state
Markov-additive reduction, checks biased exact laws, and verifies the
closed drift/CLT-variance/pressure-polynomial identities.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product


NEG_INF = None
A = ((-2, -1), (1, -1))
B = ((-1, 1), (-1, -2))
GENERATORS = (A, B)
IDENTITY = ((0, NEG_INF), (NEG_INF, 0))

ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def plus(x, y):
    if x is NEG_INF or y is NEG_INF:
        return NEG_INF
    return x + y


def maximum(values):
    finite = [x for x in values if x is not NEG_INF]
    return max(finite) if finite else NEG_INF


def tropical_matmul(left, right):
    return tuple(
        tuple(
            maximum(plus(left[i][k], right[k][j]) for k in range(2))
            for j in range(2)
        )
        for i in range(2)
    )


def literal_product(word):
    """Chronological convention: word[0] acts first."""
    matrix = IDENTITY
    for letter in word:
        matrix = tropical_matmul(GENERATORS[letter], matrix)
    return matrix


def literal_height(word):
    return maximum(x for row in literal_product(word) for x in row)


def vector_step(matrix, difference):
    """Apply a matrix to (difference, 0), returning new gap and height jump."""
    x, y = difference, 0
    new_x = max(matrix[0][0] + x, matrix[0][1] + y)
    new_y = max(matrix[1][0] + x, matrix[1][1] + y)
    return new_x - new_y, max(new_x, new_y) - max(x, y)


def vector_height(word):
    difference = 0
    height = 0
    for letter in word:
        difference, increment = vector_step(GENERATORS[letter], difference)
        height += increment
    return difference, height


# Lump labels for gaps {-3,-2}, {0}, and {2,3}.
N, Z, P = range(3)
TRANSITION = {
    (N, 0): (Z, -1),
    (N, 1): (P, 1),
    (Z, 0): (N, 1),
    (Z, 1): (P, 1),
    (P, 0): (N, 1),
    (P, 1): (Z, -1),
}


def lump_height(word):
    state = Z
    height = 0
    for letter in word:
        state, increment = TRANSITION[state, letter]
        height += increment
    return state, height


def count_dp(n):
    law = {(Z, 0): 1}
    for _ in range(n):
        new = defaultdict(int)
        for (state, height), multiplicity in law.items():
            for letter in (0, 1):
                next_state, increment = TRANSITION[state, letter]
                new[next_state, height + increment] += multiplicity
        law = dict(new)
    histogram = defaultdict(int)
    for (_, height), multiplicity in law.items():
        histogram[height] += multiplicity
    return dict(law), dict(histogram)


def probability_dp(n, p):
    q = 1 - p
    law = {(Z, 0): Fraction(1)}
    for _ in range(n):
        new = defaultdict(Fraction)
        for (state, height), mass in law.items():
            for letter, weight in ((0, p), (1, q)):
                next_state, increment = TRANSITION[state, letter]
                new[next_state, height + increment] += mass * weight
        law = dict(new)
    return law


def stationary_data(p):
    q = 1 - p
    a = p * q
    pi = (p / (1 + p), (1 - a) / (2 + a), q / (1 + q))
    drift = 3 * a / (2 + a)
    variance = 4 * a * (1 - a) * (5 - 2 * a) / (2 + a) ** 3
    return pi, drift, variance


def pressure_characteristic(r, y, p):
    """det(r I-Q(y)) for the three-state tilted kernel."""
    a = p * (1 - p)
    return r**3 + (2 * a - 1 - a * y**2) * r - a * y


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def direct_characteristic(r, y, p):
    q = 1 - p
    tilted = (
        (0, p / y, q * y),
        (p * y, 0, q * y),
        (p * y, q / y, 0),
    )
    matrix = tuple(
        tuple((r if i == j else 0) - tilted[i][j] for j in range(3))
        for i in range(3)
    )
    return determinant3(matrix)


def run_exhaustive_lane():
    # This word is an orientation sentinel: its global height happens to be
    # reversal invariant, but the chronological product matrix is not.
    word = (0, 0, 1)
    check(literal_product(word) != literal_product(tuple(reversed(word))))
    check(literal_product(word) == ((1, 1), (-1, -2)))

    for n in range(0, 16):
        brute_histogram = defaultdict(int)
        maximum_words = 0
        for word in product((0, 1), repeat=n):
            matrix = literal_product(word)
            difference, height = vector_height(word)
            state, reduced_height = lump_height(word)
            check(height == literal_height(word))
            check(height == reduced_height)
            if difference < 0:
                check(state == N)
            elif difference > 0:
                check(state == P)
            else:
                check(state == Z)
            check(height % 2 == n % 2)
            check((n % 2) <= height <= n)
            check(maximum(x for row in matrix for x in row) == height)
            brute_histogram[height] += 1
            maximum_words += height == n

        _, dp_histogram = count_dp(n)
        check(dict(brute_histogram) == dp_histogram)
        check(sum(dp_histogram.values()) == 2**n)
        if n:
            check(maximum_words == 2)
            check(literal_height((0,) * n) == n % 2)
            check(literal_height((1,) * n) == n % 2)


def run_biased_lane():
    for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
        q = 1 - p
        pi, drift, variance = stationary_data(p)
        check(sum(pi) == 1)

        # Exact stationarity of the un-tilted three-state kernel.
        pushed = [Fraction(0) for _ in range(3)]
        for state, mass in enumerate(pi):
            for letter, weight in ((0, p), (1, q)):
                next_state, _ = TRANSITION[state, letter]
                pushed[next_state] += mass * weight
        check(tuple(pushed) == pi)

        expected_increment = Fraction(0)
        for state, mass in enumerate(pi):
            for letter, weight in ((0, p), (1, q)):
                _, increment = TRANSITION[state, letter]
                expected_increment += mass * weight * increment
        check(expected_increment == drift)

        # The first two implicit derivatives of the Perron root at y=e^t=1.
        a = p * q
        r_tt = -(6 * drift**2 - 4 * a * drift - 5 * a) / (2 + a)
        check(r_tt - drift**2 == variance)
        check(variance > 0)

        for r in (Fraction(1, 3), Fraction(1), Fraction(7, 4)):
            for y in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
                check(direct_characteristic(r, y, p) == pressure_characteristic(r, y, p))

        for n in range(0, 29):
            law = probability_dp(n, p)
            check(sum(law.values()) == 1)
            # Independent weighted word enumeration on the smaller horizon.
            if n <= 11:
                brute = defaultdict(Fraction)
                for word in product((0, 1), repeat=n):
                    weight = p ** word.count(0) * q ** word.count(1)
                    brute[literal_height(word)] += weight
                reduced = defaultdict(Fraction)
                for (_, height), mass in law.items():
                    reduced[height] += mass
                check(dict(brute) == dict(reduced))

        # Endpoint and zero-temperature sentinels encoded in the cubic.
        check(pressure_characteristic(Fraction(1), Fraction(1), p) == 0)
        check(1 - 2 * a > 0)


if __name__ == "__main__":
    run_exhaustive_lane()
    run_biased_lane()
    print("stochastic tropical-resonance spike: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal/product/three-state horizon: n <= 15")
    print("biased law horizon: n <= 28 at p = 1/5, 1/2, 3/4")
    print("endpoint sentinel: A^n and B^n have height n mod 2")
    print("rare-event sentinel: max height n has exactly two alternating words for n >= 1")
