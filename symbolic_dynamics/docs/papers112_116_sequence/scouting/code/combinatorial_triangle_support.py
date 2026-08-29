#!/usr/bin/env python3
"""Exact spike for reversing every tournament arc in a directed triangle."""

from collections import Counter
from itertools import combinations
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def edge_data(n):
    edges = list(combinations(range(n), 2))
    return edges, {edge: index for index, edge in enumerate(edges)}


def cyclic_support(tournament, n, edge_index):
    triangles = set()
    support = 0
    for left, middle, right in combinations(range(n), 3):
        lm = (tournament >> edge_index[(left, middle)]) & 1
        lr = (tournament >> edge_index[(left, right)]) & 1
        mr = (tournament >> edge_index[(middle, right)]) & 1
        cyclic = (lm and mr and not lr) or (not lm and not mr and lr)
        if cyclic:
            triangle = (left, middle, right)
            triangles.add(triangle)
            for edge in combinations(triangle, 2):
                support |= 1 << edge_index[edge]
    return frozenset(triangles), support


def update(tournament, n, edge_index):
    _, support = cyclic_support(tournament, n, edge_index)
    return tournament ^ support


def lane(n):
    edges, edge_index = edge_data(n)
    phase = 1 << len(edges)
    depth_histogram = Counter()
    fixed = recurrent = 0

    for start in range(phase):
        current = start
        seen = {}
        while current not in seen:
            seen[current] = len(seen)
            triangles, _ = cyclic_support(current, n, edge_index)
            nxt = update(current, n, edge_index)
            next_triangles, _ = cyclic_support(nxt, n, edge_index)
            check(triangles <= next_triangles, "directed-triangle set was not monotone")
            current = nxt
        depth = seen[current]
        period = len(seen) - depth
        check(period in (1, 2), "period larger than two survived triangle monotonicity")
        depth_histogram[depth] += 1

        first = update(start, n, edge_index)
        second = update(first, n, edge_index)
        fixed += first == start
        recurrent += second == start

    check(fixed == factorial(n), "fixed tournaments are not exactly the transitive tournaments")
    return {
        "n": n,
        "phase": phase,
        "fixed": fixed,
        "recurrent": recurrent,
        "two_cycles": (recurrent - fixed) // 2,
        "max_depth": max(depth_histogram),
        "depths": dict(sorted(depth_histogram.items())),
    }


def first_noninvolution(limit):
    for n in range(1, limit + 1):
        edges, edge_index = edge_data(n)
        for state in range(1 << len(edges)):
            first = update(state, n, edge_index)
            if update(first, n, edge_index) != state:
                before = len(cyclic_support(state, n, edge_index)[0])
                after = len(cyclic_support(first, n, edge_index)[0])
                return n, state, before, after
    return None


def main():
    rows = [lane(n) for n in range(1, 7)]
    counterexample = first_noninvolution(6)
    check(counterexample == (5, 10, 3, 4), "unexpected first involution counterexample")

    print("directed-triangle-support reversal spike: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"first_noninvolution={counterexample}")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} phase={row['phase']} fixed={row['fixed']}"
            f" recurrent={row['recurrent']} two_cycles={row['two_cycles']}"
            f" max_depth={row['max_depth']} depths={row['depths']}"
        )


if __name__ == "__main__":
    main()
