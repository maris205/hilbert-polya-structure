#!/usr/bin/env python3
"""Supplementary exact checks for PROOF_PACKAGE.md; no floating-point data."""

from collections import Counter
from itertools import product
from math import isqrt

import sympy as sp


def transform(point):
    x, y, z = point
    return (y, z, y * z - x)


def inverse(point):
    x, y, z = point
    return (x * y - z, x, y)


def invariant(point):
    x, y, z = point
    return x * x + y * y + z * z - x * y * z


def iterate(point, number, operation=transform):
    for _ in range(number):
        point = operation(point)
    return point


def cycle(point, expected_period):
    result = []
    for _ in range(expected_period):
        assert point not in result
        result.append(point)
        point = transform(point)
    assert point == result[0]
    return tuple(result)


def expected_cycles(bound):
    result = [cycle((0, 0, 0), 1)]
    if bound >= 2:
        result += [cycle((2, 2, 2), 1), cycle((-2, -2, 2), 3)]
    for parameter in range(1, bound + 1):
        result += [
            cycle((parameter, 0, 0), 6),
            cycle((-1, parameter, -1), 4),
            cycle((1, parameter, 1), 12),
        ]
    return result


def finite_partial_permutation_cycles(bound):
    """Independent finite-graph extraction, not a bounded-time orbit guess."""
    universe = set(product(range(-bound, bound + 1), repeat=3))
    remaining = universe.copy()
    found = []
    while remaining:
        point = next(iter(remaining))
        path, position = [], {}
        while point in remaining and point not in position:
            position[point] = len(path)
            path.append(point)
            point = transform(point)
        if point in position:
            found.append(tuple(path[position[point] :]))
        remaining.difference_update(path)
    return found


def polynomial_checks():
    x, y, z, parameter, u = sp.symbols("x y z m u")
    point = (x, y, z)
    assert all(sp.expand(a - b) == 0 for a, b in zip(inverse(transform(point)), point))
    assert sp.expand(invariant(transform(point)) - invariant(point)) == 0
    for seed, period, level in [
        ((parameter, 0, 0), 6, parameter ** 2),
        ((-1, parameter, -1), 4, parameter ** 2 - parameter + 2),
        ((1, parameter, 1), 12, parameter ** 2 - parameter + 2),
    ]:
        actual = seed
        for _ in range(period):
            actual = tuple(sp.expand(entry) for entry in transform(actual))
        assert all(sp.expand(a - b) == 0 for a, b in zip(actual, seed))
        assert sp.expand(invariant(seed) - level) == 0
    for sign in (-1, 1):
        point = (0, u, sign)  # coordinates x_{-1}, x_0, x_1
        for _ in range(6):
            point = tuple(sp.expand(entry) for entry in transform(point))
        assert sp.expand(point[2] - sign * (1 - u ** 2)) == 0  # x_7
    assert iterate((sp.Rational(3), sp.Rational(3, 2), sp.Rational(3)), 2) == (
        3, sp.Rational(3, 2), 3
    )
    assert transform((3, sp.Rational(3, 2), 3)) != (3, sp.Rational(3, 2), 3)
    print("PASS symbolic inverse, invariant, three infinite itineraries, signed zero-neighbour obstruction, rational 2-cycle")


def small_cube_checks():
    expected = {point for orbit in expected_cycles(2) for point in orbit}
    assert len(expected) == 49
    all_points = set(product(range(-2, 3), repeat=3))
    nonperiodic = all_points - expected
    assert len(nonperiodic) == 76
    exit_histograms = []
    for operation in (transform, inverse):
        histogram = Counter()
        for start in sorted(nonperiodic):
            point = start
            for elapsed in range(1, 126):
                point = operation(point)
                if max(map(abs, point)) > 2:
                    histogram[elapsed] += 1
                    break
            else:
                raise AssertionError(("small-cube escape failure", start, operation.__name__))
        assert sum(histogram.values()) == 76
        exit_histograms.append(dict(sorted(histogram.items())))
    actual = {frozenset(orbit) for orbit in finite_partial_permutation_cycles(2)}
    expected_set = {frozenset(orbit) for orbit in expected_cycles(2)}
    assert actual == expected_set
    print(f"PASS all 125 states in [-2,2]^3: 49 periodic, 76 exit; forward/backward exit histograms={exit_histograms}")


def graph_checks(bound):
    observed = {frozenset(orbit) for orbit in finite_partial_permutation_cycles(bound)}
    predicted = {frozenset(orbit) for orbit in expected_cycles(bound)}
    assert observed == predicted
    counts = Counter(map(len, observed))
    number_points = sum(map(len, observed))
    assert number_points == 22 * bound + 5
    print(f"PASS full partial-permutation graph [-{bound},{bound}]^3: cycle counts={dict(sorted(counts.items()))}, {number_points} periodic points")


def level_return_checks():
    maximum_level = 200
    bound = isqrt(maximum_level) + 2
    cycles = expected_cycles(bound)
    observed = {}
    for orbit in cycles:
        level = invariant(orbit[0])
        assert all(invariant(point) == level for point in orbit)
        observed.setdefault(level, []).append(orbit)
    for level in range(-10, maximum_level + 1):
        square = int(level > 0 and isqrt(level) ** 2 == level)
        discriminant = 4 * level - 7
        quadratic = int(discriminant > 0 and isqrt(discriminant) ** 2 == discriminant)
        exact_counts = Counter(len(orbit) for orbit in observed.get(level, []))
        predicted = {
            1: int(level == 0) + int(level == 4),
            3: int(level == 4),
            4: quadratic,
            6: square,
            12: quadratic,
        }
        assert exact_counts == Counter({key: value for key, value in predicted.items() if value})
        for time in range(1, 61):
            actual = sum(len(orbit) for orbit in observed.get(level, []) if time % len(orbit) == 0)
            formula = (
                int(level == 0)
                + int(level == 4) * (1 + 3 * int(time % 3 == 0))
                + 6 * square * int(time % 6 == 0)
                + quadratic * (4 * int(time % 4 == 0) + 12 * int(time % 12 == 0))
            )
            assert actual == formula
    print("PASS exact source return formulas for integer levels -10 through 200 and ordinary times 1 through 60")


if __name__ == "__main__":
    polynomial_checks()
    small_cube_checks()
    graph_checks(20)
    level_return_checks()
    print("ALL SUPPLEMENTARY CHECKS PASS; global completeness is proved in PROOF_PACKAGE.md, not inferred from these finite tests")
