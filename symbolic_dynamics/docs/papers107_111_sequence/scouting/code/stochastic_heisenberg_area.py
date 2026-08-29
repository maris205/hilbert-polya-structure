#!/usr/bin/env python3
"""Exact discovery spike for a Bernoulli positive-Heisenberg cocycle.

The chronological product is M_n=A_n...A_1, with

    X = I + E_12,   Y = I + E_23.

The script deliberately compares literal 3-by-3 multiplication with a
separately computed binary-word inversion statistic.  It also reconstructs
the conditional law from the Gaussian-binomial recurrence and checks the
closed first two moments and the Hoeffding-type decomposition used by the
proposed CLT proof.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


X = ((1, 1, 0), (0, 1, 0), (0, 0, 1))
Y = ((1, 0, 0), (0, 1, 1), (0, 0, 1))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3))
              for j in range(3))
        for i in range(3)
    )


def literal_product(word):
    matrix = I
    for letter in word:
        matrix = matmul(X if letter else Y, matrix)
    return matrix


def inversion_area(word):
    """Number of ordered pairs Y before X (encode Y=0 and X=1)."""
    y_seen = 0
    area = 0
    for letter in word:
        if letter:
            area += y_seen
        else:
            y_seen += 1
    return area


def poly_add(left, right, shift=0):
    out = list(left)
    needed = len(right) + shift
    if len(out) < needed:
        out.extend([0] * (needed - len(out)))
    for degree, coefficient in enumerate(right):
        out[degree + shift] += coefficient
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def gaussian_binomial_rows(max_n):
    """Q[n,j]=Q[n-1,j]+z^(n-j)Q[n-1,j-1]."""
    rows = [[(1,)]]
    for n in range(1, max_n + 1):
        row = []
        for j in range(n + 1):
            no_final_x = rows[n - 1][j] if j < n else (0,)
            final_x = rows[n - 1][j - 1] if j else (0,)
            row.append(poly_add(no_final_x, final_x, n - j))
        rows.append(row)
    return rows


def histogram_polynomial(histogram):
    if not histogram:
        return (0,)
    return tuple(histogram.get(k, 0) for k in range(max(histogram) + 1))


def weighted_moments(histograms, n, p):
    q = 1 - p
    first = Fraction(0)
    second = Fraction(0)
    mass = Fraction(0)
    for j, histogram in histograms.items():
        weight = p**j * q**(n - j)
        for area, count in histogram.items():
            probability = count * weight
            mass += probability
            first += probability * area
            second += probability * area * area
    return mass, first, second - first * first


def run():
    max_n = 15
    qbinom = gaussian_binomial_rows(max_n)

    for n in range(max_n + 1):
        histograms = {j: Counter() for j in range(n + 1)}
        for word in product((0, 1), repeat=n):
            matrix = literal_product(word)
            j = sum(word)
            k = n - j
            area = inversion_area(word)
            expected = ((1, j, area), (0, 1, k), (0, 0, 1))
            check(matrix == expected, ("normal form", n, word, matrix,
                                       expected))
            histograms[j][area] += 1

        for j, histogram in histograms.items():
            check(histogram_polynomial(histogram) == qbinom[n][j],
                  ("q-binomial", n, j, histogram, qbinom[n][j]))
            check(sum(histogram.values()) == comb(n, j),
                  ("slice mass", n, j))
            if 0 < j < n:
                total = comb(n, j)
                mean = Fraction(sum(a * c for a, c in histogram.items()),
                                total)
                variance = (
                    Fraction(sum(a * a * c for a, c in histogram.items()),
                             total) - mean * mean
                )
                check(mean == Fraction(j * (n - j), 2),
                      ("conditional mean", n, j, mean))
                check(variance == Fraction(j * (n - j) * (n + 1), 12),
                      ("conditional variance", n, j, variance))

        maximum = max((max(h) for h in histograms.values()), default=0)
        zero_count = sum(h.get(0, 0) for h in histograms.values())
        check(maximum == (n * n) // 4, ("maximum area", n, maximum))
        check(zero_count == n + 1, ("zero-area paths", n, zero_count))

        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
            mass, mean, variance = weighted_moments(histograms, n, p)
            q = 1 - p
            expected_mean = Fraction(n * (n - 1), 2) * p * q
            expected_variance = (
                Fraction(n * (n - 1), 6) * p * q
                * (6 * n * p * p - 6 * n * p + 2 * n
                   - 9 * p * p + 9 * p - 1)
            )
            check(mass == 1, ("probability mass", n, p, mass))
            check(mean == expected_mean,
                  ("unconditional mean", n, p, mean, expected_mean))
            check(variance == expected_variance,
                  ("unconditional variance", n, p, variance,
                   expected_variance))

    # A wordwise identity isolates the independent weighted sum that drives
    # the n^(3/2) CLT from a quadratic remainder of smaller variance order.
    for n in range(1, 11):
        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
            q = 1 - p
            weights = [Fraction(k) - p * (n - 1) for k in range(n)]
            leading_variance = p * q * sum(a * a for a in weights)
            asymptotic_polynomial = (
                p * q * n * (n - 1)
                * (2 * n - 1 - 6 * p * (n - 1) + 6 * p * p * (n - 1))
                / 6
            )
            check(leading_variance == asymptotic_polynomial,
                  ("linear variance", n, p))
            for word in product((0, 1), repeat=n):
                eta = [Fraction(letter) - p for letter in word]
                centered = (Fraction(inversion_area(word))
                            - Fraction(n * (n - 1), 2) * p * q)
                linear = sum(a * e for a, e in zip(weights, eta))
                remainder = -sum(eta[i] * eta[j]
                                 for i in range(n) for j in range(i + 1, n))
                check(centered == linear + remainder,
                      ("Hoeffding decomposition", n, p, word))

    print("stochastic Heisenberg-area spike: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print(f"exhaustive matrix/q-binomial horizon: n <= {max_n}")
    print("moment lanes: p = 1/5, 1/2, 3/4")
    print("max-area pressure sentinel: max C_n=floor(n^2/4), "
          "zero-area paths=n+1")


if __name__ == "__main__":
    run()
