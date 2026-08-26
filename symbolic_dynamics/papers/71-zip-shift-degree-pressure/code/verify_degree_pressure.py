#!/usr/bin/env python3
"""Deterministic controls for the P71 degree-pressure identities."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import exp, log


def symbols(profile):
    return [(z, j) for z, k in enumerate(profile) for j in range(k)]


def q_exact(profile, t):
    if t + 1 >= 0:
        return Fraction(sum(k ** (t + 1) for k in profile), 1)
    return sum((Fraction(1, k ** (-(t + 1))) for k in profile), Fraction(0, 1))


def periodic_sum(profile, n, t):
    total = Fraction(0, 1)
    for word in product(symbols(profile), repeat=n):
        weight = Fraction(1, 1)
        for z, _ in word:
            k = profile[z]
            weight *= Fraction(k**t, 1) if t >= 0 else Fraction(1, k ** (-t))
        total += weight
    return total


def pressure(profile, t):
    return log(sum(k ** (t + 1.0) for k in profile))


def mean_var(profile, t):
    weights = [k ** (t + 1.0) for k in profile]
    normalizer = sum(weights)
    values = [log(k) for k in profile]
    mean = sum(w * a for w, a in zip(weights, values)) / normalizer
    variance = sum(w * (a - mean) ** 2 for w, a in zip(weights, values)) / normalizer
    return mean, variance


def shannon_binary(theta):
    if theta in (0.0, 1.0):
        return 0.0
    return -theta * log(theta) - (1.0 - theta) * log(1.0 - theta)


def main():
    for profile in ((1, 3), (1, 2, 3)):
        for n in range(1, 6):
            for t in (-1, 0, 1, 2):
                lhs = periodic_sum(profile, n, t)
                rhs = q_exact(profile, t) ** n
                assert lhs == rhs
    print("degree-weighted periodic identities: PASS (two profiles, n<=5, four weights)")

    for profile in ((1, 3), (1, 2, 3), (2, 2)):
        for t in (-2.0, -0.5, 0.0, 1.25, 3.0):
            mean, variance = mean_var(profile, t)
            eps = 1e-4
            d1 = (pressure(profile, t + eps) - pressure(profile, t - eps)) / (2 * eps)
            d2 = (
                pressure(profile, t + eps)
                - 2 * pressure(profile, t)
                + pressure(profile, t - eps)
            ) / (eps * eps)
            assert abs(d1 - mean) < 1e-7
            assert abs(d2 - variance) < 2e-7
    print("pressure derivative/variance identities: PASS")

    for profile in ((1, 3), (1, 1, 2, 4), (2, 2)):
        multiplicity = Counter(profile)
        fixed_histogram = {k: k * count for k, count in multiplicity.items()}
        recovered = {k: total // k for k, total in fixed_histogram.items()}
        assert recovered == dict(multiplicity)
    print("fixed-point local-degree profile recovery: PASS")

    # Same |S|=4, different profile: ordinary entropy agrees, pressure does not.
    assert sum((1, 3)) == sum((2, 2)) == 4
    assert abs(pressure((1, 3), 0.0) - log(4.0)) < 1e-14
    assert abs(pressure((2, 2), 0.0) - log(4.0)) < 1e-14
    assert abs(pressure((1, 3), 1.0) - pressure((2, 2), 1.0)) > 1e-3
    print("equal ordinary entropy / unequal degree pressure control: PASS")

    for theta in (0.1, 0.25, 0.5, 0.75, 0.9):
        alpha = theta * log(3.0)
        t = log(theta / (1.0 - theta)) / log(3.0) - 1.0
        legendre = pressure((1, 3), t) - t * alpha
        direct = shannon_binary(theta) + alpha
        assert abs(legendre - direct) < 1e-12
    theta = 0.75
    assert abs(shannon_binary(theta) + theta * log(3.0) - log(4.0)) < 1e-12
    print("binary multifractal/Legendre identity and maximum: PASS")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
