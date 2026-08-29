#!/usr/bin/env python3
"""Exact spike for cyclic nearest-neighbour gcd erosion on divisor words."""

from collections import Counter
from itertools import product
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def divisors(value):
    return [d for d in range(1, value + 1) if value % d == 0]


def factorization(value):
    out = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            out[prime] = out.get(prime, 0) + 1
            value //= prime
        prime += 1
    if value > 1:
        out[value] = out.get(value, 0) + 1
    return out


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def update(word):
    n = len(word)
    return tuple(gcd(word[i], word[(i + 1) % n]) for i in range(n))


def window_formula(word, time):
    n = len(word)
    return tuple(
        gcd(*(word[(i + shift) % n] for shift in range(time + 1)))
        for i in range(n)
    )


def longest_cyclic_run(bits):
    n = len(bits)
    check(not all(bits), "threshold above the global minimum has no zero")
    longest = current = 0
    for bit in bits + bits:
        current = current + 1 if bit else 0
        longest = max(longest, current)
    return min(longest, n)


def depth_formula(word, modulus):
    answer = 0
    for prime, exponent in factorization(modulus).items():
        values = [valuation(value, prime) for value in word]
        minimum = min(values)
        for level in range(minimum + 1, exponent + 1):
            bits = [value >= level for value in values]
            answer = max(answer, longest_cyclic_run(bits))
    return answer


def basin_formula(modulus, attractor, n):
    quotient = modulus // attractor
    answer = 1
    for exponent in factorization(quotient).values():
        answer *= (exponent + 1) ** n - exponent ** n
    return answer


def lane(modulus, n):
    alphabet = divisors(modulus)
    basins = Counter()
    depths = Counter()
    fixed = 0
    states = 0

    for word in product(alphabet, repeat=n):
        states += 1
        current = word
        time = 0
        while update(current) != current:
            check(current == window_formula(word, time),
                  "gcd-window iterate formula failed")
            following = update(current)
            check(all(current[i] % following[i] == 0 for i in range(n)),
                  "gcd update did not descend in the divisor lattice")
            current = following
            time += 1
            check(time <= n, "gcd erosion did not stabilize")
        check(current == window_formula(word, time),
              "terminal gcd-window formula failed")
        attractor = gcd(*word)
        check(current == (attractor,) * n, "wrong constant attractor")
        check(time == depth_formula(word, modulus),
              "longest-run pointwise depth formula failed")
        basins[attractor] += 1
        depths[time] += 1
        fixed += time == 0

    check(states == len(alphabet) ** n, "phase-size formula failed")
    check(fixed == len(alphabet), "constant fixed-point count failed")
    expected_depth = n - 1 if modulus > 1 and n > 1 else 0
    check(max(depths) == expected_depth, "sharp maximum depth failed")
    for attractor in alphabet:
        check(basins[attractor] == basin_formula(modulus, attractor, n),
              "factorized basin formula failed")
    check(sum(basins.values()) == states, "basins do not partition phase")

    return {
        "M": modulus,
        "n": n,
        "phase": states,
        "fixed": fixed,
        "max_depth": max(depths),
        "depths": dict(sorted(depths.items())),
        "basins": dict(sorted(basins.items())),
    }


def main():
    lanes = [(1, 5), (4, 5), (6, 6), (12, 5), (18, 5), (36, 4), (30, 6)]
    rows = [lane(modulus, n) for modulus, n in lanes]
    print("cyclic gcd erosion exact spike: PASS")
    print(f"assertions={ASSERTIONS}")
    for row in rows:
        print(
            "lane"
            f" M={row['M']} n={row['n']} phase={row['phase']}"
            f" fixed={row['fixed']} max_depth={row['max_depth']}"
            f" depths={row['depths']} basins={row['basins']}"
        )


if __name__ == "__main__":
    main()
