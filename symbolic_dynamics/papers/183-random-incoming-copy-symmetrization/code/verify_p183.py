#!/usr/bin/env python3
"""Exact author-side regression control for P183.

Only the Python standard library is used.  The program writes no files and
prints a deterministic transcript for bytewise comparison with CANONICAL.txt.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, got, expected, label: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{label}: got={got!r}, expected={expected!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def stirling2(t: int, r: int) -> int:
    if t == 0:
        return int(r == 0)
    if r == 0:
        return 0
    table = [[0] * (r + 1) for _ in range(t + 1)]
    table[0][0] = 1
    for i in range(1, t + 1):
        for j in range(1, min(i, r) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[t][r]


def onto_words(t: int, r: int) -> int:
    return factorial(r) * stirling2(t, r)


@lru_cache(maxsize=None)
def arc_index(n: int) -> dict[tuple[int, int], int]:
    return {
        arc: k
        for k, arc in enumerate((i, j) for i in range(n) for j in range(n) if i != j)
    }


def get_arc(state: int, n: int, i: int, j: int) -> int:
    return (state >> arc_index(n)[(i, j)]) & 1


def put_arc(state: int, n: int, i: int, j: int, value: int) -> int:
    bit = 1 << arc_index(n)[(i, j)]
    return state | bit if value else state & ~bit


def copy_incoming(state: int, n: int, vertex: int) -> int:
    out = state
    for other in range(n):
        if other != vertex:
            out = put_arc(out, n, vertex, other, get_arc(state, n, other, vertex))
    return out


def conflicts(state: int, n: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if get_arc(state, n, i, j) != get_arc(state, n, j, i)
    )


def representative(n: int, edges: frozenset[tuple[int, int]]) -> int:
    state = 0
    for i, j in edges:
        state = put_arc(state, n, i, j, 1)
    return state


def apply_word(state: int, n: int, word: tuple[int, ...]) -> int:
    for vertex in word:
        state = copy_incoming(state, n, vertex)
    return state


def independent(mask: int, edges: frozenset[tuple[int, int]]) -> bool:
    return all(not ((mask >> i) & 1 and (mask >> j) & 1) for i, j in edges)


def isolated_count(n: int, edges: frozenset[tuple[int, int]]) -> int:
    incident = {vertex for edge in edges for vertex in edge}
    return n - len(incident)


def endpoint_from_order(
    initial: int,
    n: int,
    edges: frozenset[tuple[int, int]],
    order: tuple[int, ...],
) -> int:
    rank = {vertex: position for position, vertex in enumerate(order)}
    infinity = n + 1
    out = initial
    for i, j in edges:
        rank_i = rank.get(i, infinity)
        rank_j = rank.get(j, infinity)
        if rank_i == rank_j == infinity:
            continue
        early, other = (i, j) if rank_i < rank_j else (j, i)
        value = get_arc(initial, n, other, early)
        out = put_arc(out, n, early, other, value)
        out = put_arc(out, n, other, early, value)
    return out


def order_distribution(initial: int, n: int, t: int) -> Counter:
    edges = conflicts(initial, n)
    result = Counter()
    for support_mask in range(1 << n):
        support = tuple(v for v in range(n) if (support_mask >> v) & 1)
        weight = stirling2(t, len(support))
        if weight:
            for order in permutations(support):
                result[endpoint_from_order(initial, n, edges, order)] += weight
    return result


def literal_distribution(initial: int, n: int, t: int) -> Counter:
    result = Counter()
    for word in product(range(n), repeat=t):
        result[apply_word(initial, n, word)] += 1
    return result


def absorption_prediction(n: int, t: int, edges: frozenset[tuple[int, int]]) -> int:
    return sum(
        onto_words(t, n - missing.bit_count())
        for missing in range(1 << n)
        if independent(missing, edges)
    )


def verify_statewise(n: int) -> tuple[int, int]:
    state_count = 1 << (n * (n - 1))
    recurrent = 0
    labelled = Counter()
    distinct: dict[int, set[int]] = {}
    for state in range(state_count):
        edge_set = conflicts(state, n)
        fixed = all(copy_incoming(state, n, v) == state for v in range(n))
        AUDIT.equal(fixed, not edge_set, f"fixed n={n} A={state}")
        recurrent += int(fixed)
        for vertex in range(n):
            target = copy_incoming(state, n, vertex)
            predicted_edges = frozenset(edge for edge in edge_set if vertex not in edge)
            AUDIT.equal(conflicts(target, n), predicted_edges, f"deletion n={n} A={state} v={vertex}")
            AUDIT.equal(copy_incoming(target, n, vertex), target, f"idempotent n={n} A={state} v={vertex}")
            labelled[target] += 1
            distinct.setdefault(target, set()).add(state)
    AUDIT.equal(recurrent, 1 << (n * (n - 1) // 2), f"recurrent census n={n}")
    max_distinct = 0
    for target in range(state_count):
        k = isolated_count(n, conflicts(target, n))
        AUDIT.equal(labelled[target], k * (1 << (n - 1)), f"labelled fibre n={n} B={target}")
        predicted = 1 + k * ((1 << (n - 1)) - 1) if k else 0
        got = len(distinct.get(target, set()))
        AUDIT.equal(got, predicted, f"distinct fibre n={n} B={target}")
        max_distinct = max(max_distinct, got)
    return recurrent, max_distinct


def verify_history_formulas(n: int) -> tuple[int, int]:
    pairs = tuple((i, j) for i in range(n) for j in range(i + 1, n))
    complete_mask = (1 << len(pairs)) - 1
    complete_absorbed = 0
    complete_endpoint_count = 0
    for edge_mask in range(1 << len(pairs)):
        edge_set = frozenset(edge for k, edge in enumerate(pairs) if (edge_mask >> k) & 1)
        initial = representative(n, edge_set)
        for t in range(n + 1):
            literal = literal_distribution(initial, n, t)
            ordered = order_distribution(initial, n, t)
            AUDIT.equal(sum(literal.values()), n**t, f"history total n={n} H={edge_mask} t={t}")
            AUDIT.equal(literal, ordered, f"endpoint kernel n={n} H={edge_mask} t={t}")
            absorbed = sum(count for target, count in literal.items() if not conflicts(target, n))
            predicted = absorption_prediction(n, t, edge_set)
            AUDIT.equal(absorbed, predicted, f"absorption n={n} H={edge_mask} t={t}")
            if edge_mask == complete_mask and t == n:
                complete_absorbed = absorbed
                complete_endpoint_count = len(literal)

    # Extra arbitrary-orientation pressure, not only one representative per H.
    if n <= 3:
        state_count = 1 << (n * (n - 1))
        for initial in range(state_count):
            for t in range(n + 1):
                AUDIT.equal(
                    literal_distribution(initial, n, t),
                    order_distribution(initial, n, t),
                    f"arbitrary endpoint n={n} A={initial} t={t}",
                )
    return complete_absorbed, complete_endpoint_count


def verify_noncommutation() -> None:
    for n in range(2, 5):
        pairs = tuple((i, j) for i in range(n) for j in range(i + 1, n))
        for edge in pairs:
            initial = representative(n, frozenset({edge}))
            u, v = edge
            left = copy_incoming(copy_incoming(initial, n, v), n, u)
            right = copy_incoming(copy_incoming(initial, n, u), n, v)
            AUDIT.true(left != right, f"noncommuting witness n={n} edge={edge}")


def main() -> None:
    print("P183_EXACT_AUTHOR_CONTROL")
    expected_rows = {
        1: (1, 1, 1, 1),
        2: (2, 3, 4, 2),
        3: (8, 10, 24, 9),
        4: (64, 29, 168, 40),
    }
    for n in range(1, 5):
        recurrent, max_distinct = verify_statewise(n)
        absorbed, endpoint_count = verify_history_formulas(n)
        AUDIT.equal(
            (recurrent, max_distinct, absorbed, endpoint_count),
            expected_rows[n],
            f"published control row n={n}",
        )
        print(
            f"n={n} states={1 << (n * (n - 1))} recurrent={recurrent} "
            f"max_distinct_fibre={max_distinct} "
            f"complete_H_absorbed_tn={absorbed} "
            f"complete_H_endpoint_support={endpoint_count}"
        )
    verify_noncommutation()
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()

