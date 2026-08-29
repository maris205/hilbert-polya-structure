#!/usr/bin/env python3
"""Exact spike for synchronous score-upset reversal on labelled tournaments.

For every pair of vertices with unequal current outdegrees, the next
tournament directs the edge from the higher-score vertex to the lower-score
vertex.  Ties retain their old orientation.
"""

from collections import Counter
from itertools import combinations
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def edge_table(n):
    return list(combinations(range(n), 2))


def scores(tournament, n, edges):
    out = [0] * n
    for bit, (left, right) in enumerate(edges):
        winner = left if (tournament >> bit) & 1 else right
        out[winner] += 1
    return tuple(out)


def update(tournament, n, edges):
    old_scores = scores(tournament, n, edges)
    out = 0
    for bit, (left, right) in enumerate(edges):
        if old_scores[left] > old_scores[right]:
            orientation = 1
        elif old_scores[left] < old_scores[right]:
            orientation = 0
        else:
            orientation = (tournament >> bit) & 1
        out |= orientation << bit
    return out


def quadratic_score(tournament, n, edges):
    return sum(value * value for value in scores(tournament, n, edges))


def is_regular(tournament, vertices, edges):
    vertex_set = set(vertices)
    internal = {vertex: 0 for vertex in vertices}
    for bit, (left, right) in enumerate(edges):
        if left in vertex_set and right in vertex_set:
            winner = left if (tournament >> bit) & 1 else right
            internal[winner] += 1
    return len(set(internal.values())) <= 1


def has_fixed_structure(tournament, n, edges):
    score = scores(tournament, n, edges)
    classes = {}
    for vertex, value in enumerate(score):
        classes.setdefault(value, []).append(vertex)
    if not all(is_regular(tournament, block, edges) for block in classes.values()):
        return False
    for bit, (left, right) in enumerate(edges):
        if score[left] == score[right]:
            continue
        higher_wins = ((tournament >> bit) & 1) == (score[left] > score[right])
        if not higher_wins:
            return False
    return True


def regular_counts(limit):
    counts = [0] * (limit + 1)
    counts[0] = 0
    for n in range(1, limit + 1, 2):
        edges = edge_table(n)
        target = (n - 1) // 2
        counts[n] = sum(
            scores(state, n, edges) == (target,) * n
            for state in range(1 << len(edges))
        )
    return counts


def expected_fixed_counts(limit, regular):
    # A fixed tournament is a unique ordered sum of regular tournaments.
    fixed = [0] * (limit + 1)
    fixed[0] = 1
    for n in range(1, limit + 1):
        fixed[n] = sum(
            comb(n, block) * regular[block] * fixed[n - block]
            for block in range(1, n + 1, 2)
        )
    return fixed


def lane(n, expected_fixed):
    edges = edge_table(n)
    phase = 1 << len(edges)
    depth_histogram = Counter()
    fixed = 0

    for start in range(phase):
        current = start
        depth = 0
        seen = set()
        while True:
            check(current not in seen, "nontrivial score-reversal cycle found")
            seen.add(current)
            nxt = update(current, n, edges)
            old_score = scores(current, n, edges)
            new_score = scores(nxt, n, edges)
            check(
                all(
                    old_score[left] <= old_score[right]
                    or new_score[left] > new_score[right]
                    for left in range(n)
                    for right in range(n)
                ),
                "strict score-class order was not preserved",
            )
            if nxt == current:
                break
            check(
                quadratic_score(nxt, n, edges)
                > quadratic_score(current, n, edges),
                "quadratic score was not a strict Lyapunov function",
            )
            current = nxt
            depth += 1
            check(depth <= n - 1, "score refinement exceeded the structural n-1 cap")

        check(has_fixed_structure(current, n, edges), "terminal form is not an ordered regular sum")
        depth_histogram[depth] += 1
        fixed += depth == 0

    check(fixed == expected_fixed[n], "ordered-regular-sum fixed count failed")
    return {
        "n": n,
        "phase": phase,
        "fixed": fixed,
        "max_depth": max(depth_histogram),
        "depths": dict(sorted(depth_histogram.items())),
    }


def first_nonidempotent(limit):
    for n in range(1, limit + 1):
        edges = edge_table(n)
        for state in range(1 << len(edges)):
            first = update(state, n, edges)
            if update(first, n, edges) != first:
                return n, state, scores(state, n, edges)
    return None


def main():
    regular = regular_counts(5)
    expected_fixed = expected_fixed_counts(6, regular)
    rows = [lane(n, expected_fixed) for n in range(1, 7)]
    counterexample = first_nonidempotent(6)
    check(counterexample == (6, 148, (2, 2, 2, 2, 3, 4)), "unexpected first idempotence counterexample")

    print("synchronous tournament score-upset reversal spike: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"regular_counts={regular}")
    print(f"first_nonidempotent={counterexample}")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} phase={row['phase']} fixed={row['fixed']}"
            f" max_depth={row['max_depth']} depths={row['depths']}"
        )


if __name__ == "__main__":
    main()
