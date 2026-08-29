#!/usr/bin/env python3
"""Exact controls for a Bernoulli max-plus switching-slowdown cocycle."""

from collections import defaultdict
from fractions import Fraction
from itertools import product


NEG_INF = None
C = ((1, 0), (0, 0))
D = ((0, 0), (0, 1))
GENERATORS = (C, D)
IDENTITY = ((0, NEG_INF), (NEG_INF, 0))
ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def add(x, y):
    if x is NEG_INF or y is NEG_INF:
        return NEG_INF
    return x + y


def max_finite(values):
    values = [x for x in values if x is not NEG_INF]
    return max(values) if values else NEG_INF


def multiply(left, right):
    return tuple(
        tuple(
            max_finite(add(left[i][k], right[k][j]) for k in range(2))
            for j in range(2)
        )
        for i in range(2)
    )


def literal_product(word):
    matrix = IDENTITY
    for letter in word:
        matrix = multiply(GENERATORS[letter], matrix)
    return matrix


def literal_height(word):
    return max_finite(x for row in literal_product(word) for x in row)


# Projective gaps -1, 0, 1 are denoted M, Z, P.
M, Z, P = range(3)
TRANSITION = {
    (M, 0): (Z, 0),
    (M, 1): (M, 1),
    (Z, 0): (P, 1),
    (Z, 1): (M, 1),
    (P, 0): (P, 1),
    (P, 1): (Z, 0),
}


def reduced_height(word):
    state, height = Z, 0
    for letter in word:
        state, increment = TRANSITION[state, letter]
        height += increment
    return state, height


def count_law(n):
    law = {(Z, 0): 1}
    for _ in range(n):
        new = defaultdict(int)
        for (state, height), count in law.items():
            for letter in (0, 1):
                next_state, increment = TRANSITION[state, letter]
                new[next_state, height + increment] += count
        law = dict(new)
    histogram = defaultdict(int)
    for (_, height), count in law.items():
        histogram[height] += count
    return dict(histogram)


def probability_law(n, p):
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


def direct_characteristic(r, z, p):
    q = 1 - p
    matrix = (
        (r - q * z, -p, 0),
        (-q * z, r, -p * z),
        (0, -q, r - p * z),
    )
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def closed_characteristic(r, z, p):
    a = p * (1 - p)
    return r**3 - z * r**2 + a * z * (z - 2) * r + a * z**2


def run_exhaustive_lane():
    orientation_word = (0, 0, 1)
    check(literal_product(orientation_word) != literal_product(tuple(reversed(orientation_word))))

    for n in range(0, 17):
        brute = defaultdict(int)
        max_count = 0
        for word in product((0, 1), repeat=n):
            _, height = reduced_height(word)
            check(height == literal_height(word))
            check((n + 1) // 2 <= height <= n if n else height == 0)
            brute[height] += 1
            max_count += height == n
        check(dict(brute) == count_law(n))
        check(sum(brute.values()) == 2**n)
        if n:
            check(literal_height((0,) * n) == n)
            check(literal_height((1,) * n) == n)
            check(max_count == 2)
            alternating = tuple(i % 2 for i in range(n))
            check(literal_height(alternating) == (n + 1) // 2)


def run_biased_lane():
    for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
        q = 1 - p
        a = p * q
        pi = (q * q / (1 - a), a / (1 - a), p * p / (1 - a))
        drift = (1 - 2 * a) / (1 - a)
        variance = a * (1 - 3 * a - 2 * a * a) / (1 - a) ** 3
        check(sum(pi) == 1)

        pushed = [Fraction(0) for _ in range(3)]
        mean_increment = Fraction(0)
        for state, mass in enumerate(pi):
            for letter, weight in ((0, p), (1, q)):
                next_state, increment = TRANSITION[state, letter]
                pushed[next_state] += mass * weight
                mean_increment += mass * weight * increment
        check(tuple(pushed) == pi)
        check(mean_increment == drift)
        check(variance > 0)

        for r in (Fraction(1, 3), Fraction(1), Fraction(5, 3)):
            for z in (Fraction(1, 2), Fraction(1), Fraction(7, 4)):
                check(direct_characteristic(r, z, p) == closed_characteristic(r, z, p))

        for n in range(0, 31):
            law = probability_law(n, p)
            check(sum(law.values()) == 1)
            if n <= 11:
                brute = defaultdict(Fraction)
                for word in product((0, 1), repeat=n):
                    weight = p ** word.count(0) * q ** word.count(1)
                    brute[literal_height(word)] += weight
                reduced = defaultdict(Fraction)
                for (_, height), mass in law.items():
                    reduced[height] += mass
                check(dict(brute) == dict(reduced))


if __name__ == "__main__":
    run_exhaustive_lane()
    run_biased_lane()
    print("stochastic tropical-slowdown spike: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal/three-state horizon: n <= 16")
    print("biased finite law: n <= 30 at p = 1/5, 1/2, 3/4")
    print("endpoint sentinel: deterministic growth rate 1")
    print("rare-event sentinel: alternating words attain ceil(n/2) for n >= 1")
