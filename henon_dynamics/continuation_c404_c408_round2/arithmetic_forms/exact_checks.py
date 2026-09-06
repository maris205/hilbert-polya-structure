#!/usr/bin/env python3
"""Finite rational sentinels, not a certificate of infinite-limit claims.

Represent x(m)=b(m)*sqrt(m), b rational. Then the critical GCD form
is sum b(m)b(n)gcd(m,n), so every check below is exact over Q.
The rowwise Gram evaluation and pairwise kernel evaluation are distinct
finite formulas; neither numerically proves a strong-resolvent limit.
"""

from fractions import Fraction as Q
from math import gcd, lcm
import json
import platform


def hilbert_norm_squared(b):
    return sum((m * v * v for m, v in b.items()), Q(0))


def form_pair(b, c):
    return sum((v * w * gcd(m, n) for m, v in b.items()
                for n, w in c.items()), Q(0))


def subtract(b, c):
    return {m: b.get(m, Q(0)) - c.get(m, Q(0)) for m in b.keys() | c.keys()}


def tail_vector(b, primes):
    s = sum((Q(1, p) for p in primes), Q(0))
    h = {}
    for p in primes:
        for m, v in b.items():
            h[p*m] = h.get(p*m, Q(0)) + v / (s*p)
    return s, h


def harmonic(n):
    return sum((Q(1, k) for k in range(1, n+1)), Q(0))


def gram_rows(b, size):
    return sum((sum((m*v for m, v in b.items() if r % m == 0), Q(0))**2 / r
                for r in range(1, size+1)), Q(0)) / harmonic(size)


def gram_pairs(b, size):
    return sum((v*w*gcd(m, n)*harmonic(size//lcm(m, n))
                for m, v in b.items() for n, w in b.items()), Q(0)) / harmonic(size)


def main():
    b = {1: Q(1), 2: Q(-1), 3: Q(1, 2), 6: Q(1, 3)}
    qb = form_pair(b, b)
    records = []
    for primes in ([5, 7, 11], [5, 7, 11, 13, 17, 19]):
        s, h = tail_vector(b, primes)
        residual = form_pair(subtract(h, b), subtract(h, b))
        prediction = qb * sum((Q(1, p)*(1-Q(1, p)) for p in primes), Q(0)) / s**2
        assert hilbert_norm_squared(h) == hilbert_norm_squared(b)/s
        assert form_pair(b, h) == qb
        assert residual == prediction
        records.append({"primes": primes, "s": str(s), "hilbert_norm_squared": str(hilbert_norm_squared(h)),
                        "form_residual": str(residual), "all_three_identities": True})
    # The tail hypotheses are substantive: including a support prime invalidates
    # the disjointness calculation. This is a deliberate failing-hypothesis control.
    bad_s, bad_h = tail_vector(b, [2, 3, 5])
    assert hilbert_norm_squared(bad_h) != hilbert_norm_squared(b)/bad_s
    assert form_pair(b, bad_h) != qb
    grams = []
    for size in (12, 31, 100):
        rows, pairs = gram_rows(b, size), gram_pairs(b, size)
        assert rows == pairs
        grams.append({"N": size, "row_value": str(rows), "pair_value": str(pairs), "equal": True})
    print(json.dumps({"method": "exact rational arithmetic, real finite test vector",
                      "python": platform.python_version(), "tail_checks": records,
                      "overlap_control_rejects_identities": True, "gram_checks": grams,
                      "infinite_limits_numerically_tested": False}, indent=2))


if __name__ == "__main__":
    main()
