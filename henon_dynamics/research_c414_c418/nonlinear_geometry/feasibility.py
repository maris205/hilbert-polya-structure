"""Bounded, exact scouting checks; no all-degree claim is inferred here.

The finite rational-periodic box used for the discrete-sine maps is the
published Corollary 4.3 of arXiv:2412.01668v2, not a theorem proved by this
script. Only selected degrees are checked, not a parameter census.
"""

from collections import Counter
from fractions import Fraction
from math import comb, factorial


def discrete_sine(d, x):
    k = (d - 1) // 2
    product = x
    value = Fraction(0)
    for j in range(k + 1):
        if j:
            product *= x * x - j * j
        value += (-1) ** (k - j) * Fraction(product, factorial(2 * j + 1))
    assert value.denominator == 1
    positive_x = abs(x)
    independently = sum(
        (-1) ** (k - j) * comb(positive_x + j, 2 * j + 1)
        for j in range(k + 1) if positive_x + j >= 2 * j + 1
    )
    if x < 0:
        independently = -independently
    assert value == independently
    return value.numerator


def finite_cycles(points, step):
    remaining = set(points)
    cycles = []
    while remaining:
        point = min(remaining)
        chain, index = [], {}
        while point in remaining and point not in index:
            index[point] = len(chain)
            chain.append(point)
            point = step(point)
        if point in index:
            cycles.append(chain[index[point] :])
        remaining.difference_update(chain)
    return cycles


def check_discrete_sine(d):
    bound = (d + 5) // 2
    values = {y: discrete_sine(d, y) for y in range(-bound, bound + 1)}
    points = {(x, y) for x in values for y in values}
    cycles = finite_cycles(points, lambda p: (p[1], -p[0] + values[p[1]]))
    seen = set()
    for cycle in cycles:
        assert not seen.intersection(cycle)
        seen.update(cycle)
        for position, point in enumerate(cycle):
            assert (point[1], -point[0] + values[point[1]]) == cycle[(position + 1) % len(cycle)]
    periods = Counter(map(len, cycles))
    count = sum(period * multiplicity for period, multiplicity in periods.items())
    conjectured = {
        1: Fraction(d * d) - Fraction(8 * d, 3) + Fraction(56, 3),
        3: Fraction(d * d + 8),
        5: Fraction(d * d) - Fraction(8 * d, 3) + Fraction(40, 3),
    }[d % 6]
    print({"family": "discrete_sine", "d": d, "periodic_points_in_box": count,
           "primitive_multiplicities": dict(sorted(periods.items())),
           "published_count_conjecture_matches": count == conjectured})


if __name__ == "__main__":
    for degree in (3, 5, 7, 9, 11, 13, 19, 25, 31, 67):
        check_discrete_sine(degree)
