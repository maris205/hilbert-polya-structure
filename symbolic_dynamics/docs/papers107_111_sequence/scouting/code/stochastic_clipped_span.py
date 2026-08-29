#!/usr/bin/env python3
"""Exact discovery spike for clipped left/right maps on a finite path.

On {0,...,m}, let L(x)=max(x-1,0) and R(x)=min(x+1,m).  The
chronological random composition uses fair iid choices.  This script checks
that its image diameter is the positive part of m minus the span of the
driving simple random walk, then independently matches the first-span-time
law to a product of gambler's-ruin PGFs written with Chebyshev polynomials.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product

import sympy as sp


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def compose_word(m, word):
    image = list(range(m + 1))
    for step in word:
        image = [max(0, min(m, x + step)) for x in image]
    return tuple(image)


def walk_data(word):
    position = 0
    low = high = 0
    for step in word:
        position += step
        low = min(low, position)
        high = max(high, position)
    return position, low, high


def chebyshev_stage_pgf(r, z):
    # Exit from {-1,0,...,r,r+1}, starting at the boundary point 0.
    return sp.cancel(
        (1 + sp.chebyshevu(r, 1 / z)) / sp.chebyshevu(r + 1, 1 / z)
    )


def total_pgf(m, z):
    return sp.cancel(sp.prod(chebyshev_stage_pgf(r, z)
                             for r in range(m)))


def first_span_counts(m, horizon):
    """DP counts paths whose walk span first reaches m at each time."""
    states = {(0, 0, 0): 1}
    first = [0] * (horizon + 1)
    for time in range(horizon):
        nxt = defaultdict(int)
        for (position, low, high), count in states.items():
            for step in (-1, 1):
                new_position = position + step
                new_low = min(low, new_position)
                new_high = max(high, new_position)
                if new_high - new_low >= m:
                    first[time + 1] += count
                else:
                    nxt[(new_position, new_low, new_high)] += count
        states = dict(nxt)
    return first


def run():
    # Route 1: literal finite-map composition versus walk extrema.
    for m in range(1, 9):
        for n in range(13):
            for word in product((-1, 1), repeat=n):
                image = compose_word(m, word)
                position, low, high = walk_data(word)
                span = high - low
                check(tuple(sorted(set(image)))
                      == tuple(range(min(image), max(image) + 1)),
                      ("image interval", m, n, word, image))
                check(max(image) - min(image) == max(0, m - span),
                      ("diameter/span", m, n, word, image, low, high))
                if span < m:
                    check(image[0] == position - low,
                          ("lower endpoint", m, n, word, image))
                    check(image[-1] == m + position - high,
                          ("upper endpoint", m, n, word, image))
                else:
                    check(len(set(image)) == 1,
                          ("synchronization", m, n, word, image))

    # Route 2: gambler's-ruin difference equation and exact PGF product.
    z = sp.symbols("z")
    for r in range(12):
        stage = chebyshev_stage_pgf(r, z)
        n_boundary = r + 2
        denominator = sp.chebyshevu(n_boundary - 1, 1 / z)
        values = []
        for i in range(n_boundary + 1):
            numerator = (sp.chebyshevu(n_boundary - i - 1, 1 / z)
                         + sp.chebyshevu(i - 1, 1 / z))
            values.append(sp.cancel(numerator / denominator))
        check(sp.simplify(values[0] - 1) == 0,
              ("left boundary", r))
        check(sp.simplify(values[-1] - 1) == 0,
              ("right boundary", r))
        for i in range(1, n_boundary):
            check(sp.simplify(values[i]
                              - z * (values[i - 1] + values[i + 1]) / 2)
                  == 0, ("difference equation", r, i))
        check(sp.simplify(stage - values[1]) == 0,
              ("stage PGF", r))
        mean = sp.simplify(sp.diff(stage, z).subs(z, 1))
        variance = sp.simplify(
            sp.diff(stage, z, 2).subs(z, 1) + mean - mean * mean
        )
        check(mean == r + 1, ("stage mean", r, mean))
        check(variance == sp.Rational(r * (r + 1) * (r + 2), 3),
              ("stage variance", r, variance))

    horizon = 28
    for m in range(1, 8):
        pgf = total_pgf(m, z)
        series = sp.series(pgf, z, 0, horizon + 1).removeO().expand()
        counts = first_span_counts(m, horizon)
        for n in range(horizon + 1):
            coefficient = sp.Rational(counts[n], 2**n)
            check(series.coeff(z, n) == coefficient,
                  ("first-span distribution", m, n,
                   series.coeff(z, n), coefficient))
        mean = sp.simplify(sp.diff(pgf, z).subs(z, 1))
        variance = sp.simplify(
            sp.diff(pgf, z, 2).subs(z, 1) + mean - mean * mean
        )
        check(mean == sp.Rational(m * (m + 1), 2),
              ("total mean", m, mean))
        check(variance == sp.Rational(
            m * (m - 1) * (m + 1) * (m + 2), 12),
            ("total variance", m, variance))

    print("stochastic clipped-span spike: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal cocycle lane: 1 <= m <= 8, n <= 12")
    print("PGF/first-hit lane: 1 <= m <= 7, coefficients through n=28")
    print("stage lane: Chebyshev difference equations for 0 <= r <= 11")


if __name__ == "__main__":
    run()
