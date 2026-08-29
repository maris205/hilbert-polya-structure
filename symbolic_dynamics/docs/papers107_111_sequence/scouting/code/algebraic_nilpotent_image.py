#!/usr/bin/env python3
"""Exact proof spike for U -> N(U) on a finite subspace lattice.

Here N is one regular nilpotent Jordan block.  This is intentionally distinct
from the previously falsified saturation map U -> U + N(U).
"""

from collections import Counter
from itertools import combinations, product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def vadd(u, v, q):
    return tuple((x + y) % q for x, y in zip(u, v))


def scale(c, u, q):
    return tuple(c * x % q for x in u)


def span(basis, q, d):
    out = {(0,) * d}
    for v in basis:
        out = {vadd(x, scale(c, v, q), q) for x in out for c in range(q)}
    return frozenset(out)


def all_subspaces(q, d):
    spaces = set()
    for r in range(d + 1):
        for pivots in combinations(range(d), r):
            pivot_set = set(pivots)
            free = [
                (i, j)
                for i, p in enumerate(pivots)
                for j in range(p + 1, d)
                if j not in pivot_set
            ]
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * d for _ in range(r)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), value in zip(free, values):
                    rows[i][j] = value
                spaces.add(span([tuple(row) for row in rows], q, d))
    return spaces


def qbinom(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    return numerator // denominator


def gauss_sum(d, q):
    return sum(qbinom(d, r, q) for r in range(d + 1))


def nilpotent_vector(v, t=1):
    if t >= len(v):
        return (0,) * len(v)
    return tuple(v[t:]) + (0,) * t


def image(space, t=1):
    return frozenset(nilpotent_vector(v, t) for v in space)


def dim(space, q):
    size = len(space)
    r = 0
    while q**r < size:
        r += 1
    AUDIT.check(q**r == size)
    return r


def transition_formula(d, q, t, r, s):
    # k = dim(U intersect ker N^t) = r-s.
    k = r - s
    if not (0 <= k <= min(r, t)):
        return 0
    if r - k > d - t:
        return 0
    return (
        qbinom(t, k, q)
        * qbinom(d - t, r - k, q)
        * q ** ((t - k) * (r - k))
    )


def run_lane(q, d):
    spaces = all_subspaces(q, d)
    zero = frozenset({(0,) * d})
    depths = Counter()
    transition = {t: Counter() for t in range(d + 1)}
    for u in spaces:
        r = dim(u, q)
        x = u
        tau = 0
        while x != zero:
            x = image(x)
            tau += 1
            AUDIT.check(tau <= d, "nilpotent image did not absorb")
        depths[tau] += 1
        for t in range(d + 1):
            literal = image(u, t)
            AUDIT.check(literal == (u if t == 0 else image(image(u, t - 1))), "iterate mismatch")
            transition[t][(r, dim(literal, q))] += 1

    AUDIT.check(len(spaces) == gauss_sum(d, q))
    for t in range(d + 1):
        cumulative = sum(count for depth, count in depths.items() if depth <= t)
        AUDIT.check(cumulative == gauss_sum(t, q), "absorption CDF mismatch")
        for r in range(d + 1):
            for s in range(r + 1):
                AUDIT.check(
                    transition[t][(r, s)] == transition_formula(d, q, t, r, s),
                    f"rank transition mismatch at {(q, d, t, r, s)}",
                )
    AUDIT.check(depths[d] > 0)
    expected_depths = {
        t: gauss_sum(t, q) - (gauss_sum(t - 1, q) if t else 0)
        for t in range(d + 1)
    }
    AUDIT.check(dict(depths) == expected_depths)
    print(
        f"q={q}, d={d}: subspaces={len(spaces)}, depths={dict(sorted(depths.items()))}"
    )


def main():
    for q, max_d in [(2, 6), (3, 5), (5, 4)]:
        for d in range(1, max_d + 1):
            run_lane(q, d)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
