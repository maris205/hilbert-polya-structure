#!/usr/bin/env python3
"""Deterministic exact controls for P100.

No floating-point comparisons and no external packages are used.  The orbit
lane and the coefficient lane implement the same claims independently.
"""

from collections import Counter
from fractions import Fraction
from math import comb


def digits(x: int, p: int, r: int) -> tuple[int, ...]:
    out = []
    for _ in range(r):
        out.append(x % p)
        x //= p
    return tuple(out)


def digit_sum(x: int, p: int, r: int) -> int:
    return sum(digits(x, p, r))


def erase(x: int, p: int) -> int:
    if x == 0:
        return 0
    original = x
    place = 1
    while x % p == 0:
        x //= p
        place *= p
    return original - place


def orbit_depth(x: int, p: int, r: int) -> tuple[int, int]:
    steps = 0
    transition_checks = 0
    while x:
        before = digit_sum(x, p, r)
        y = erase(x, p)
        after = digit_sum(y, p, r)
        assert after == before - 1
        assert 0 <= y < x
        transition_checks += 2
        x = y
        steps += 1
    return steps, transition_checks


def convolution_profile(p: int, r: int) -> list[int]:
    coeff = [1]
    for _ in range(r):
        nxt = [0] * (len(coeff) + p - 1)
        for i, a in enumerate(coeff):
            for j in range(p):
                nxt[i + j] += a
        coeff = nxt
    return coeff


def inclusion_exclusion(p: int, r: int, k: int) -> int:
    total = 0
    for j in range(0, min(r, k // p) + 1):
        total += (-1) ** j * comb(r, j) * comb(k - p * j + r - 1, r - 1)
    return total


def main() -> None:
    lanes = [(2, 12), (3, 9), (5, 7), (7, 7), (11, 5)]
    state_checks = 0
    transition_checks = 0
    profile_checks = 0

    for p, r in lanes:
        modulus = p**r
        observed = Counter()
        for x in range(modulus):
            depth, local_checks = orbit_depth(x, p, r)
            assert depth == digit_sum(x, p, r)
            observed[depth] += 1
            state_checks += 1
            transition_checks += local_checks

        profile = convolution_profile(p, r)
        assert len(profile) == (p - 1) * r + 1
        assert sum(profile) == modulus
        assert profile[0] == profile[-1] == 1
        assert profile[1] == r
        profile_checks += 4

        for k, count in enumerate(profile):
            assert observed[k] == count
            assert inclusion_exclusion(p, r, k) == count
            assert profile[k] == profile[-1 - k]
            profile_checks += 3

        middle = len(profile) // 2
        for k in range(middle):
            assert profile[k] <= profile[k + 1]
            profile_checks += 1

        first = sum(Fraction(k * c, modulus) for k, c in enumerate(profile))
        second = sum(Fraction(k * k * c, modulus) for k, c in enumerate(profile))
        mean = Fraction(r * (p - 1), 2)
        variance = Fraction(r * (p * p - 1), 12)
        assert first == mean
        assert second - first * first == variance
        assert 1 + (len(profile) - 1) // profile[1] == p
        profile_checks += 3

        deepest = modulus - 1
        y = deepest
        for _ in range((p - 1) * r - 1):
            y = erase(y, p)
        assert y != 0
        assert erase(y, p) == 0
        profile_checks += 2

        for n in range(1, 8):
            fixed = 0
            for x in range(modulus):
                y = x
                for _ in range(n):
                    y = erase(y, p)
                fixed += y == x
            assert fixed == 1
            profile_checks += 1

        print(
            f"lane p={p}, r={r}: states={modulus}, "
            f"max_depth={(p - 1) * r}, profile_terms={len(profile)} PASS"
        )

    total = state_checks + transition_checks + profile_checks
    print(f"orbit states checked: {state_checks}")
    print(f"single-step exact assertions: {transition_checks}")
    print(f"profile/fixed-data assertions: {profile_checks}")
    print(f"TOTAL EXACT ASSERTIONS: {total}")
    print("ALL P100 CONTROLS PASS")


if __name__ == "__main__":
    main()
