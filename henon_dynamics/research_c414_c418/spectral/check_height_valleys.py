#!/usr/bin/env python3
"""Finite adversarial evidence, not the quantified height theorem.

Two paths: literal prime-field polynomial iteration until exact escape,
versus the proposed coefficient-free valley multiplicities. No file writes.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json


def trim(poly):
    p = list(poly)
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(x, y, p, scale=1):
    return trim(tuple(((x[i] if i < len(x) else 0)
                       + scale * (y[i] if i < len(y) else 0)) % p
                      for i in range(max(len(x), len(y)))))


def mul(x, y, p):
    if not x or not y:
        return ()
    z = [0] * (len(x) + len(y) - 1)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            z[i + j] = (z[i + j] + xi * yj) % p
    return trim(z)


def evaluate(f, x, p):
    z = ()
    for coefficient in reversed(f):
        z = add(mul(z, x, p), (coefficient,), p)
    return z


def iterate(point, f, a, p, backward=False):
    x, y = point
    if backward:
        z = add(evaluate(f, x, p), y, p, -1)
        inverse = pow(a, -1, p)
        return trim(tuple(inverse * c % p for c in z)), x
    return y, add(evaluate(f, y, p), x, p, -a)


def halfheight(point, f, a, p, backward=False):
    d = len(f) - 1
    for k in range(30):
        m, n = len(point[0]) - 1, len(point[1]) - 1
        if m <= 0 and n <= 0:
            return Fraction(0)
        escape = m if backward else n
        other = n if backward else m
        if escape > 0 and d * escape > other:
            return Fraction(escape, d ** k)
        point = iterate(point, f, a, p, backward)
    raise AssertionError("No certified escape within finite test limit")


def literal_distribution(p, f, a, bound):
    polynomials = [trim(cs) for cs in product(range(p), repeat=bound + 1)]
    counts = Counter()
    for point in product(polynomials, repeat=2):
        height = halfheight(point, f, a, p) + halfheight(point, f, a, p, True)
        assert height >= max(0, len(point[0]) - 1, len(point[1]) - 1)
        if height <= bound:
            counts[height] += 1
    return counts, len(polynomials) ** 2


def valley_distribution(q, d, bound):
    counts = Counter({Fraction(0): q ** 2})
    # The bound is on the canonical height, so each core degree is <= bound.
    # |k| <= bound+2 safely contains every contributing shift for d>=2.
    for m in range(1, bound + 1):
        for n in range(1, bound + 1):
            if m >= d * n or n >= d * m:
                continue
            weight = (q - 1) ** 2 * q ** (m + n)
            for k in range(-bound - 2, bound + 3):
                power = Fraction(d) ** k
                height = power * n + m / power
                if height <= bound:
                    counts[height] += weight
    for degree in range(1, bound + 1):
        quotient, residue = divmod(degree, d)
        if residue:
            weight = (q - 1) * q ** ((d + 1) * quotient + residue + 1)
        else:
            weight = (q - 1) ** 2 * q ** ((d + 1) * quotient)
        for k in range(-bound - 2, bound + 3):
            power = Fraction(d) ** k
            height = degree * (power / d + 1 / power)
            if height <= bound:
                counts[height] += weight
    return counts


def main():
    cases = [
        (2, (0, 0, 1), 1, 5),
        (2, (1, 1, 1), 1, 5),
        (2, (0, 0, 0, 1), 1, 5),
        (2, (1, 1, 1, 1), 1, 5),
        (2, (1, 1, 0, 0, 1), 1, 5),
        (3, (0, 0, 1), 1, 3),
        (3, (2, 1, 2), 2, 3),
        (3, (1, 0, 1, 1), 1, 3),
        (3, (2, 2, 0, 2), 2, 3),
        (5, (3, 2, 4), 3, 2),
        (5, (1, 4, 3, 2), 4, 2),
    ]
    rows = []
    for p, f, a, bound in cases:
        actual, tested = literal_distribution(p, f, a, bound)
        predicted = valley_distribution(p, len(f) - 1, bound)
        assert actual == predicted, (p, f, a, actual, predicted)
        rows.append({"prime": p, "coefficients_low_to_high": f,
                     "a": a, "height_bound": bound,
                     "polynomial_pairs_tested": tested,
                     "height_distribution": {str(h): actual[h] for h in sorted(actual)},
                     "exact_match": True})
    print(json.dumps({"scope": "finite prime-field checks; not a theorem",
                      "cases": rows,
                      "total_pairs_tested": sum(r["polynomial_pairs_tested"] for r in rows)},
                     indent=2))


if __name__ == "__main__":
    main()
