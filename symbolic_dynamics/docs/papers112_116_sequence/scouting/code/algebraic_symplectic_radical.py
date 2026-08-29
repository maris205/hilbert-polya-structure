#!/usr/bin/env python3
"""Exact spike for U -> U intersect U^perp in a finite symplectic space.

The update sends every subspace to the radical of its restricted alternating
form.  Literal RREF subspace enumeration is compared with independent
orbit-stabilizer formulas for every input dimension and radical dimension.
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


def add(u, v, q):
    return tuple((a + b) % q for a, b in zip(u, v))


def scale(c, u, q):
    return tuple((c * a) % q for a in u)


def span(basis, q, d):
    out = {(0,) * d}
    for vector in basis:
        out = {
            add(x, scale(c, vector, q), q)
            for x in out
            for c in range(q)
        }
    return frozenset(out)


def all_subspaces(q, d):
    spaces = set()
    for r in range(d + 1):
        for pivots in combinations(range(d), r):
            pivot_set = set(pivots)
            free = [
                (i, j)
                for i, pivot in enumerate(pivots)
                for j in range(pivot + 1, d)
                if j not in pivot_set
            ]
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * d for _ in range(r)]
                for i, pivot in enumerate(pivots):
                    rows[i][pivot] = 1
                for (i, j), value in zip(free, values):
                    rows[i][j] = value
                spaces.add(span([tuple(row) for row in rows], q, d))
    return spaces


def dimension(space, q):
    size = len(space)
    r = 0
    while q**r < size:
        r += 1
    AUDIT.check(q**r == size, "non-vector-space size")
    return r


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


def symplectic_pair(u, v, q):
    m = len(u) // 2
    return sum(
        u[i] * v[m + i] - u[m + i] * v[i] for i in range(m)
    ) % q


def radical(space, q):
    return frozenset(
        u
        for u in space
        if all(symplectic_pair(u, v, q) == 0 for v in space)
    )


def is_totally_isotropic(space, q):
    return all(symplectic_pair(u, v, q) == 0 for u in space for v in space)


def symplectic_order(rank_m, q):
    """Order of Sp(2*rank_m,q)."""
    return q ** (rank_m * rank_m) * product_int(
        q ** (2 * i) - 1 for i in range(1, rank_m + 1)
    )


def product_int(values):
    out = 1
    for value in values:
        out *= value
    return out


def isotropic_count(m, h, q):
    if h < 0 or h > m:
        return 0
    return qbinom(m, h, q) * product_int(q ** (m - i) + 1 for i in range(h))


def nondegenerate_count(m, j, q):
    """Nondegenerate 2j-subspaces in a symplectic 2m-space."""
    if j < 0 or j > m:
        return 0
    return symplectic_order(m, q) // (
        symplectic_order(j, q) * symplectic_order(m - j, q)
    )


def rank_radical_formula(m, input_dim, hull_dim, q):
    remainder = input_dim - hull_dim
    if remainder < 0 or remainder % 2:
        return 0
    j = remainder // 2
    if hull_dim > m or j > m - hull_dim:
        return 0
    return isotropic_count(m, hull_dim, q) * nondegenerate_count(
        m - hull_dim, j, q
    )


def run_lane(q, m):
    d = 2 * m
    spaces = all_subspaces(q, d)
    census = Counter()
    fibre_sizes = Counter()
    fixed = []

    for space in spaces:
        hull = radical(space, q)
        r = dimension(space, q)
        h = dimension(hull, q)
        census[(r, h)] += 1
        fibre_sizes[hull] += 1
        AUDIT.check(hull.issubset(space), "radical left its source subspace")
        AUDIT.check(is_totally_isotropic(hull, q), "radical is not isotropic")
        AUDIT.check(radical(hull, q) == hull, "radical map is not idempotent")
        if hull == space:
            fixed.append(space)

    AUDIT.check(len(spaces) == gauss_sum(d, q))
    for r in range(d + 1):
        AUDIT.check(sum(census[(r, h)] for h in range(d + 1)) == qbinom(d, r, q))
        for h in range(d + 1):
            expected = rank_radical_formula(m, r, h, q)
            AUDIT.check(
                census[(r, h)] == expected,
                f"rank/radical mismatch at q={q}, m={m}, r={r}, h={h}",
            )

    expected_fixed = sum(isotropic_count(m, h, q) for h in range(m + 1))
    AUDIT.check(len(fixed) == expected_fixed)

    # Fibres are uniform on each isotropic dimension.  Their size is the
    # number of all nondegenerate subspaces in the quotient W^perp/W.
    for hull in fixed:
        h = dimension(hull, q)
        expected_fibre = sum(
            nondegenerate_count(m - h, j, q) for j in range(m - h + 1)
        )
        AUDIT.check(fibre_sizes[hull] == expected_fibre)

    nonzero_cells = {
        key: value for key, value in sorted(census.items()) if value
    }
    print(
        f"q={q}, dim={d}: subspaces={len(spaces)}, fixed={len(fixed)}, "
        f"(input dim, radical dim) census={nonzero_cells}"
    )


def main():
    for lane in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1), (5, 2)]:
        run_lane(*lane)
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
