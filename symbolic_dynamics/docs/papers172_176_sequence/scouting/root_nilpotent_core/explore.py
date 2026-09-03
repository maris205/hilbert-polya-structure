#!/usr/bin/env python3
"""Exact exploratory pilot for U -> U cap N^{-1}U over F_2."""

from collections import Counter, defaultdict
from itertools import combinations


def span(basis):
    out = {0}
    for v in basis:
        out |= {x ^ v for x in tuple(out)}
    return frozenset(out)


def subspaces(n):
    # Generate RREF row spaces over F_2, then deduplicate defensively.
    ans = set()
    vectors = range(1, 1 << n)
    for r in range(n + 1):
        if r == 0:
            ans.add(frozenset({0}))
            continue
        for pivots in combinations(range(n), r):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, n) if j not in pivots]
            for mask in range(1 << len(free)):
                rows = [1 << p for p in pivots]
                for k, (i, j) in enumerate(free):
                    if mask >> k & 1:
                        rows[i] |= 1 << j
                # RREF also forbids nonpivot entries in later pivot columns.
                if any((rows[i] >> pivots[j]) & 1
                       for i in range(r) for j in range(i + 1, r)):
                    continue
                ans.add(span(rows))
    return sorted(ans, key=lambda u: (len(u), tuple(u)))


def N(v):
    return v >> 1


def step(u):
    return frozenset(v for v in u if N(v) in u)


def dim(u):
    return (len(u)).bit_length() - 1


def main():
    for n in range(1, 7):
        ss = subspaces(n)
        assert len(ss) == [0, 2, 5, 16, 67, 374, 2825][n]
        f = {u: step(u) for u in ss}
        fixed = [u for u in ss if f[u] == u]
        tails = Counter()
        layers = defaultdict(list)
        for u in ss:
            v, t, seen = u, 0, set()
            while f[v] != v:
                assert v not in seen
                seen.add(v)
                v, t = f[v], t + 1
            tails[t] += 1
            layers[t].append(u)
        indeg = Counter(f.values())
        fixed_fibres = [(dim(w), indeg[w]) for w in fixed]
        print("n", n, "states", len(ss), "fixed", len(fixed),
              "tails", dict(sorted(tails.items())),
              "fixed_fibres", fixed_fibres)
        deepest = layers[max(tails)]
        print(" deepest_dims", Counter(dim(u) for u in deepest),
              "deepest", len(deepest))


if __name__ == "__main__":
    main()
