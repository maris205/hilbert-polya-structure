#!/usr/bin/env python3
"""Deterministic checks for the R1 sparse-period theorem.

The state is the adjacency matrix over F_2 of an ordered DAG, represented by
row bitsets.  The update is A |-> A + A^2.  This script is intentionally
standard-library only and uses exhaustive search only in bounded lanes.
"""

from collections import defaultdict
from itertools import combinations
import json
import math


class Checker:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def arc_positions(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def from_edges(n, edges):
    rows = [0] * n
    for i, j in edges:
        rows[i] |= 1 << j
    return tuple(rows)


def matrices(n):
    positions = arc_positions(n)
    for mask in range(1 << len(positions)):
        rows = [0] * n
        for bit, (i, j) in enumerate(positions):
            if (mask >> bit) & 1:
                rows[i] |= 1 << j
        yield tuple(rows)


def matrices_with_arc_count(n, edge_count):
    positions = arc_positions(n)
    for chosen in combinations(positions, edge_count):
        yield from_edges(n, chosen)


def multiply(a, b):
    out = []
    for row in a:
        value = 0
        todo = row
        while todo:
            low = todo & -todo
            value ^= b[low.bit_length() - 1]
            todo -= low
        out.append(value)
    return tuple(out)


def add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def zero(n):
    return (0,) * n


def update(a):
    return add(a, multiply(a, a))


def actual_period(a):
    start = a
    current = a
    for time in range(1, 257):
        current = update(current)
        if current == start:
            return time
    raise AssertionError("period exceeded deterministic safety bound")


def nilpotence_index(a):
    """Return the least positive r with A^r=0."""
    n = len(a)
    current = a
    for r in range(1, n + 1):
        if current == zero(n):
            return r
        current = multiply(current, a)
    raise AssertionError("strict upper triangular matrix was not nilpotent")


def period_from_index(r):
    s = 0
    while (1 << (1 << s)) < r:
        s += 1
    return 1 << s


def arc_count(a):
    return sum(row.bit_count() for row in a)


def edge_set(a):
    return {
        (i, j)
        for i, row in enumerate(a)
        for j in range(i + 1, len(a))
        if (row >> j) & 1
    }


def is_increasing_path_plus_isolates(a, length):
    edges = edge_set(a)
    active = sorted({vertex for edge in edges for vertex in edge})
    if len(active) != length + 1:
        return False
    expected = {(active[k], active[k + 1]) for k in range(length)}
    return edges == expected


def path_state(n, vertices):
    return from_edges(n, zip(vertices, vertices[1:]))


def arc_budget_witness(n, edge_count):
    """Achieve nilpotence index min(edge_count+1,n) with exactly e arcs."""
    positions = arc_positions(n)
    if edge_count < n - 1:
        edges = [(i, i + 1) for i in range(edge_count)]
    else:
        edges = [(i, i + 1) for i in range(n - 1)]
        present = set(edges)
        for edge in positions:
            if len(edges) == edge_count:
                break
            if edge not in present:
                edges.append(edge)
                present.add(edge)
    return from_edges(n, edges)


def longest_path_length(a):
    """Combinatorial longest directed-path length, ignoring parity cancellation."""
    n = len(a)
    best_to = [0] * n
    for j in range(n):
        for i in range(j):
            if (a[i] >> j) & 1:
                best_to[j] = max(best_to[j], best_to[i] + 1)
    return max(best_to, default=0)


def exhaustive_lane(checker):
    summaries = {}
    for n in range(1, 7):
        by_period_and_edges = defaultdict(int)
        max_index_by_edges = defaultdict(int)
        max_period_by_edges = defaultdict(int)
        for a in matrices(n):
            edges = arc_count(a)
            index = nilpotence_index(a)
            period = actual_period(a)
            checker.check(
                period == period_from_index(index),
                f"period/index mismatch at n={n}",
            )
            checker.check(
                index <= min(edges + 1, n),
                f"arc/index bound failed at n={n}, e={edges}",
            )
            by_period_and_edges[(period, edges)] += 1
            max_index_by_edges[edges] = max(max_index_by_edges[edges], index)
            max_period_by_edges[edges] = max(max_period_by_edges[edges], period)

        for edges in range(n * (n - 1) // 2 + 1):
            target_index = min(edges + 1, n)
            checker.check(
                max_index_by_edges[edges] == target_index,
                f"fixed-budget index envelope failed at n={n}, e={edges}",
            )
            checker.check(
                max_period_by_edges[edges] == period_from_index(target_index),
                f"fixed-budget period envelope failed at n={n}, e={edges}",
            )

        equality_counts = {}
        for s in (1, 2):
            m = 1 << (1 << (s - 1))
            if n <= m:
                continue
            equality = 0
            for a in matrices_with_arc_count(n, m):
                index = nilpotence_index(a)
                if period_from_index(index) == (1 << s):
                    equality += 1
                    checker.check(
                        is_increasing_path_plus_isolates(a, m),
                        f"equality classification failed at n={n}, s={s}",
                    )
            checker.check(
                equality == math.comb(n, m + 1),
                f"equality count failed at n={n}, s={s}",
            )
            equality_counts[str(1 << s)] = equality

        summaries[str(n)] = {
            "states": 1 << (n * (n - 1) // 2),
            "equality_counts": equality_counts,
        }
    return summaries


def sparse_layer_lane(checker):
    summaries = {}
    ranges = ((1, 2, range(3, 13)), (2, 4, range(5, 10)))
    for s, m, n_values in ranges:
        counts = {}
        for n in n_values:
            equality = 0
            for a in matrices_with_arc_count(n, m):
                index = nilpotence_index(a)
                if period_from_index(index) == (1 << s):
                    equality += 1
                    checker.check(
                        is_increasing_path_plus_isolates(a, m),
                        f"sparse-layer classification failed at n={n}, s={s}",
                    )
            expected = math.comb(n, m + 1)
            checker.check(
                equality == expected,
                f"sparse-layer count failed at n={n}, s={s}",
            )
            counts[str(n)] = equality
        summaries[f"period_{1 << s}"] = counts

    # The next threshold m=16 is too large for edge-layer enumeration, but all
    # equality candidates for n=17,...,20 can still be constructed and checked.
    # The strengthened range n>m^2 is already tested above for m=2, n=5,...,12.
    s = 3
    m = 16
    counts = {}
    for n in range(17, 21):
        equality = 0
        for vertices in combinations(range(n), m + 1):
            a = path_state(n, vertices)
            checker.check(arc_count(a) == m, "constructed path has wrong arc count")
            checker.check(nilpotence_index(a) == m + 1, "constructed path has wrong index")
            checker.check(actual_period(a) == (1 << s), "constructed path has wrong period")
            checker.check(
                is_increasing_path_plus_isolates(a, m),
                "constructed equality state failed path recognition",
            )
            equality += 1
        checker.check(equality == math.comb(n, m + 1), "constructed count failed")
        counts[str(n)] = equality
    summaries["period_8_constructed"] = counts
    return summaries


def budget_witness_lane(checker):
    summaries = {}
    for n in range(1, 13):
        maximum_edges = n * (n - 1) // 2
        for edges in range(maximum_edges + 1):
            a = arc_budget_witness(n, edges)
            target_index = min(edges + 1, n)
            checker.check(arc_count(a) == edges, f"witness arc count failed at n={n}, e={edges}")
            checker.check(
                nilpotence_index(a) == target_index,
                f"witness index failed at n={n}, e={edges}",
            )
            checker.check(
                actual_period(a) == period_from_index(target_index),
                f"witness period failed at n={n}, e={edges}",
            )
        summaries[str(n)] = {
            "edge_budgets": maximum_edges + 1,
            "max_index": n,
            "max_period": period_from_index(n),
        }
    return summaries


def cancellation_counterexample_lane(checker):
    # Two length-two paths 0-1-3 and 0-2-3 cancel in A^2 over F_2.
    diamond = from_edges(4, ((0, 1), (0, 2), (1, 3), (2, 3)))
    checker.check(longest_path_length(diamond) == 2, "diamond path length changed")
    checker.check(multiply(diamond, diamond) == zero(4), "diamond paths did not cancel")
    checker.check(nilpotence_index(diamond) == 2, "diamond index should be two")
    checker.check(actual_period(diamond) == 1, "diamond should be fixed")
    return {
        "arcs": arc_count(diamond),
        "longest_path_length": longest_path_length(diamond),
        "nilpotence_index": nilpotence_index(diamond),
        "period": actual_period(diamond),
    }


def main():
    checker = Checker()
    result = {
        "exhaustive_n_le_6": exhaustive_lane(checker),
        "sparse_equality_layers": sparse_layer_lane(checker),
        "arc_budget_witnesses_n_le_12": budget_witness_lane(checker),
        "parity_cancellation_counterexample": cancellation_counterexample_lane(checker),
    }
    result["assertions"] = checker.assertions
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
