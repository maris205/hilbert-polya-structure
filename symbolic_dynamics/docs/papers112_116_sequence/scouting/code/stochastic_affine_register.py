#!/usr/bin/env python3
"""Exact controls for an affine cyclic-register fixed-point cocycle.

On F_2^m, the two generators are x -> R x and x -> R x + e_0,
where R cyclically rotates coordinates.  The script checks literal maps,
the affine normal form, and the exact two-point fixed-count law.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd


ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def rotate(x, m, steps=1):
    steps %= m
    mask = (1 << m) - 1
    if steps == 0:
        return x & mask
    return ((x << steps) & mask) | (x >> (m - steps))


def generator(x, m, bit):
    return rotate(x, m) ^ bit


def literal_map(x, m, word):
    for bit in word:
        x = generator(x, m, bit)
    return x


def translation(m, word):
    value = 0
    for bit in word:
        value = rotate(value, m) ^ bit
    return value


def closed_map(x, m, word):
    return rotate(x, m, len(word)) ^ translation(m, word)


def cycle_parities_zero(value, m, n):
    d = gcd(m, n)
    seen = set()
    for start in range(m):
        if start in seen:
            continue
        parity = 0
        position = start
        while position not in seen:
            seen.add(position)
            parity ^= (value >> position) & 1
            position = (position + n) % m
        if parity:
            return False
    check(len(seen) == m)
    check(d == gcd(m, n))
    return True


def closed_fixed_count(m, n, affine_translation):
    if n == 0:
        return 1 << m
    d = gcd(m, n)
    return (1 << d) if cycle_parities_zero(affine_translation, m, n) else 0


def literal_fixed_count(m, word):
    return sum(literal_map(x, m, word) == x for x in range(1 << m))


def even_parity_probability(k, p):
    return (1 + (1 - 2 * p) ** k) / 2


def success_probability(m, n, p):
    if n == 0:
        return Fraction(1)
    d = gcd(m, n)
    return even_parity_probability(n // d, p) ** d


def word_satisfies_fixed_condition(m, word):
    return closed_fixed_count(m, len(word), translation(m, word)) != 0


def run_literal_lane():
    # Reversing generator order changes the affine translation.
    check(translation(3, (0, 1)) == 1)
    check(translation(3, (1, 0)) == 2)

    for m in range(1, 8):
        for n in range(0, 11):
            successful_words = 0
            for word in product((0, 1), repeat=n):
                affine_translation = translation(m, word)
                for x in range(1 << m):
                    check(literal_map(x, m, word) == closed_map(x, m, word))
                literal = literal_fixed_count(m, word)
                closed = closed_fixed_count(m, n, affine_translation)
                check(literal == closed)
                check(literal in (0, 1 << gcd(m, n)))
                successful_words += literal != 0
            check(successful_words == 2 ** (n - gcd(m, n)) if n else successful_words == 1)


def run_probability_lane():
    for p in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
        q = 1 - p
        for m in range(1, 11):
            for n in range(0, 14):
                exact_success = success_probability(m, n, p)
                if n <= 11:
                    enumerated = Fraction(0)
                    law = defaultdict(Fraction)
                    for word in product((0, 1), repeat=n):
                        weight = p ** sum(word) * q ** (n - sum(word))
                        fixed_count = closed_fixed_count(m, n, translation(m, word))
                        law[fixed_count] += weight
                        if fixed_count:
                            enumerated += weight
                    check(enumerated == exact_success)
                    check(sum(law.values()) == 1)
                    check(set(law).issubset({0, 1 << gcd(m, n)}))

                d = gcd(m, n)
                expected_fixed = (1 << d) * exact_success
                if n:
                    check(expected_fixed == (1 + (1 - 2 * p) ** (n // d)) ** d)
                else:
                    check(expected_fixed == 1 << m)

        # Resonant diagonal n=k m: an exact exponential-in-dimension moment.
        for k in range(1, 5):
            for m in range(1, 9):
                n = k * m
                expected = (1 << m) * success_probability(m, n, p)
                check(expected == (1 + (1 - 2 * p) ** k) ** m)

    # Deterministic endpoint p=1 retains a parity-of-resonance obstruction.
    for m in range(1, 11):
        for n in range(1, 21):
            d = gcd(m, n)
            expected_success = Fraction(int((n // d) % 2 == 0))
            check(success_probability(m, n, Fraction(1)) == expected_success)


if __name__ == "__main__":
    run_literal_lane()
    run_probability_lane()
    print("stochastic affine-register spike: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("literal full-map lane: 1 <= m <= 7, n <= 10")
    print("biased fixed-count lane: 1 <= m <= 10, n <= 13")
    print("orientation sentinel: translations of words 01 and 10 differ")
    print("endpoint sentinel: p=1 is controlled by parity of n/gcd(m,n)")
