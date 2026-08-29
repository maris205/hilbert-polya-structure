#!/usr/bin/env python3
"""Exact proof spike for the meet/join comparator sweep on subspace tuples."""

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
    zero = (0,) * d
    out = {zero}
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
                for (i, j), x in zip(free, values):
                    rows[i][j] = x
                spaces.add(span([tuple(row) for row in rows], q, d))
    return sorted(spaces, key=lambda x: (len(x), sorted(x)))


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


def lattice_tables(q, d):
    spaces = all_subspaces(q, d)
    locate = {u: i for i, u in enumerate(spaces)}
    n = len(spaces)
    meet = [[0] * n for _ in range(n)]
    join = [[0] * n for _ in range(n)]
    for i, u in enumerate(spaces):
        for j, v in enumerate(spaces):
            meet[i][j] = locate[u & v]
            summed = frozenset(vadd(x, y, q) for x in u for y in v)
            join[i][j] = locate[summed]
    dims = []
    for u in spaces:
        size = len(u)
        r = 0
        while q**r < size:
            r += 1
        AUDIT.check(q**r == size)
        dims.append(r)
    return spaces, dims, meet, join


def sweep(state, meet, join):
    state = list(state)
    for i in range(len(state) - 1):
        a, b = state[i], state[i + 1]
        state[i], state[i + 1] = meet[a][b], join[a][b]
    return tuple(state)


def is_flag(state, meet):
    return all(meet[a][b] == a for a, b in zip(state, state[1:]))


def gauss_sum(d, q):
    return sum(qbinom(d, r, q) for r in range(d + 1))


def flag_formula(d, q):
    return sum(
        qbinom(d, c, q) * qbinom(c, b, q) * qbinom(b, a, q)
        for a in range(d + 1)
        for b in range(a, d + 1)
        for c in range(b, d + 1)
    )


def depth_le_one_formula(d, q):
    ans = 0
    for a in range(d + 1):
        for b in range(d + 1):
            for k in range(min(a, b) + 1):
                if a + b - k > d:
                    continue
                pairs = (
                    qbinom(d, k, q)
                    * qbinom(d - k, a - k, q)
                    * qbinom(d - a, b - k, q)
                    * q ** ((a - k) * (b - k))
                )
                ans += pairs * gauss_sum(d - k, q)
    return ans


def run_triples(q, d):
    spaces, dims, meet, join = lattice_tables(q, d)
    n = len(spaces)
    hist = Counter()
    fixed = 0
    for state in product(range(n), repeat=3):
        s1 = sweep(state, meet, join)
        s2 = sweep(s1, meet, join)
        s3 = sweep(s2, meet, join)
        AUDIT.check(s3 == s2, "S^3 != S^2")
        AUDIT.check(is_flag(s2, meet), "second sweep did not sort")

        u, v, w = state
        triple_meet = meet[meet[u][v]][w]
        middle = join[meet[u][v]][meet[join[u][v]][w]]
        total = join[join[u][v]][w]
        AUDIT.check(s2 == (triple_meet, middle, total), "closed S^2 mismatch")

        condition = meet[meet[u][v]][w] == meet[u][v]
        AUDIT.check(is_flag(s1, meet) == condition, "depth-one criterion mismatch")
        if is_flag(state, meet):
            depth = 0
        elif is_flag(s1, meet):
            depth = 1
        else:
            depth = 2
        hist[depth] += 1
        fixed += depth == 0

    closed_fixed = flag_formula(d, q)
    closed_h = depth_le_one_formula(d, q)
    AUDIT.check(n == gauss_sum(d, q))
    AUDIT.check(fixed == closed_fixed)
    AUDIT.check(hist[0] + hist[1] == closed_h)
    AUDIT.check(hist[2] == n**3 - closed_h)
    print(
        f"triple q={q}, d={d}: subspaces={n}, states={n**3}, "
        f"depths={dict(sorted(hist.items()))}"
    )


def run_general(q, d, m):
    spaces, _, meet, join = lattice_tables(q, d)
    n = len(spaces)
    hist = Counter()
    for state in product(range(n), repeat=m):
        x = state
        depth = 0
        while not is_flag(x, meet):
            x = sweep(x, meet, join)
            depth += 1
            AUDIT.check(depth <= m - 1, "sorting bound failed")
        hist[depth] += 1
    zero = 0
    whole = n - 1
    # all_subspaces is sorted by cardinality, so these are {0} and V.
    sharp = (whole,) * (m - 1) + (zero,)
    x = sharp
    for t in range(m - 1):
        AUDIT.check(not is_flag(x, meet), "sharp witness sorted too early")
        x = sweep(x, meet, join)
    AUDIT.check(is_flag(x, meet), "sharp witness did not sort")
    print(
        f"general q={q}, d={d}, m={m}: states={n**m}, "
        f"max-depth={max(hist)}, depths={dict(sorted(hist.items()))}"
    )


def main():
    for q, d in [(2, 1), (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (5, 2)]:
        run_triples(q, d)
    for q, d, m in [(2, 1, 4), (2, 2, 4), (2, 3, 4), (2, 2, 5)]:
        run_general(q, d, m)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
