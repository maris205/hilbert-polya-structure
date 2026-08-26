#!/usr/bin/env python3
"""SymPy and independent finite identities for HCS-C175."""
from __future__ import annotations

from itertools import product
import json
from math import gcd

import sympy as sp


def move(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    out = list(word)
    movers = [i for i in range(n) if word[i] and not word[(i + 1) % n]]
    for i in movers:
        out[i] = 0
        out[(i + 1) % n] = 1
    return tuple(out)


def independent_enumeration(n: int, r: int) -> int:
    return sum(
        sum(word) == r and all(not (word[i] and word[(i + 1) % n]) for i in range(n))
        for word in product((0, 1), repeat=n)
    )


def independent_formula(n: int, r: int) -> sp.Integer:
    if r == 0:
        return sp.Integer(1)
    if r < 0 or r > n // 2:
        return sp.Integer(0)
    return sp.cancel(sp.Integer(n) * sp.binomial(n - r, r) / (n - r))


def fixed_formula(n_sites: int, particles: int, n: int) -> sp.Integer:
    m = min(particles, n_sites - particles)
    g = gcd(n_sites, n)
    q = n_sites // g
    return independent_formula(g, m // q) if m % q == 0 else sp.Integer(0)


def main() -> None:
    checks = 0

    # The closed cyclic-independent-set formula agrees with direct words.
    for n_sites in range(1, 17):
        for r in range(0, n_sites + 1):
            assert independent_formula(n_sites, r) == independent_enumeration(n_sites, r)
            checks += 1

    # Fixed counts, Möbius inversion and Euler-product logarithmic coefficients.
    for n_sites in range(1, 13):
        divisors = sp.divisors(n_sites)
        words_by_k = {
            k: [word for word in product((0, 1), repeat=n_sites) if sum(word) == k]
            for k in range(n_sites + 1)
        }
        for particles, words in words_by_k.items():
            fixed = {}
            current = {word: word for word in words}
            for n in range(1, 2 * n_sites + 3):
                current = {word: move(image) for word, image in current.items()}
                observed = sum(word == image for word, image in current.items())
                closed = fixed_formula(n_sites, particles, n)
                assert closed == observed
                checks += 1
                fixed[n] = sp.Integer(closed)

            cycles = {}
            for d in divisors:
                exact = sp.expand(sum(sp.mobius(d // e) * fixed[e] for e in sp.divisors(d)))
                assert exact.is_integer and exact >= 0 and exact % d == 0
                checks += 1
                cycles[d] = exact // d
            for n in range(1, 2 * n_sites + 3):
                from_product = sum(d * cycles[d] for d in divisors if n % d == 0)
                assert sp.expand(from_product - fixed[n]) == 0
                checks += 1

    # Gap update conserves the number of holes and realizes the zero-marker rule.
    for length in range(1, 7):
        for gaps in product(range(4), repeat=length):
            positive = [int(value > 0) for value in gaps]
            updated = tuple(
                gaps[i] - positive[i] + positive[(i + 1) % length]
                for i in range(length)
            )
            assert all(value >= 0 for value in updated)
            checks += 1
            assert sum(updated) == sum(gaps)
            checks += 1
            expected_zero_count = sum(
                gaps[(i + 1) % length] == 0 and gaps[i] <= 1
                for i in range(length)
            )
            assert sum(value == 0 for value in updated) == expected_zero_count
            checks += 1
            assert sum(value == 0 for value in updated) <= sum(value == 0 for value in gaps)
            checks += 1

    print(json.dumps({"status": "C175_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
