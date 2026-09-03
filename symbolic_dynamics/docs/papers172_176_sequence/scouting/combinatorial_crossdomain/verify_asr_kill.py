#!/usr/bin/env python3
"""Exact kill certificate for cyclic adjacent-sum reranking.

The map has an explicit 2n recurrent orbit, but the complete recurrent atlas
already branches at n=6 and again at n=9.  This script preserves that useful
negative evidence; it is not a paper contract.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def step(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    scores = tuple(word[index] + word[(index + 1) % n] for index in range(n))
    order = sorted(range(n), key=lambda index: (scores[index], index))
    ranks = [0] * n
    for rank, index in enumerate(order, 1):
        ranks[index] = rank
    return tuple(ranks)


def rotate(word: tuple[int, ...]) -> tuple[int, ...]:
    return word[1:] + word[:1]


def principal_cycle_seed(n: int) -> tuple[int, ...]:
    if n <= 2:
        return tuple(range(1, n + 1))
    evens = tuple(range(2, n + 1, 2))
    if n % 2:
        middle = (n,)
        descending_odds = tuple(range(n - 2, 2, -2))
    else:
        middle = ()
        descending_odds = tuple(range(n - 1, 2, -2))
    return (1,) + evens + middle + descending_odds


def audit_rank(n: int) -> None:
    states = tuple(permutations(range(1, n + 1)))
    state_set = set(states)
    successor = {}
    fibres = Counter()
    for state in states:
        target = step(state)
        check(target in state_set, "permutation closure")
        successor[state] = target
        fibres[target] += 1

    data = {}
    cycles = Counter()
    for start in states:
        if start in data:
            continue
        path = []
        position = {}
        point = start
        while point not in data and point not in position:
            position[point] = len(path)
            path.append(point)
            point = successor[point]
        if point in position:
            cycle_start = position[point]
            period = len(path) - cycle_start
            cycles[period] += 1
            for state in path[cycle_start:]:
                data[state] = (0, period)
            path = path[:cycle_start]
        for state in reversed(path):
            tail, period = data[successor[state]]
            data[state] = (tail + 1, period)
    check(len(data) == len(states), "complete functional graph")

    seed = principal_cycle_seed(n)
    check(len(set(seed)) == n, "principal seed permutation")
    if n >= 3:
        check(step(step(seed)) == rotate(seed), "principal orbit two-step rotation")
    point = seed
    orbit = []
    while point not in orbit:
        orbit.append(point)
        point = successor[point]
    if n >= 3:
        check(point == seed and len(orbit) == 2 * n, "principal 2n cycle")

    maximum_tail = max(tail for tail, _ in data.values())
    period_states = Counter(period for _, period in data.values())
    print(
        f"n={n} states={len(states)} image={len(fibres)} max_tail={maximum_tail} "
        f"cycles={dict(sorted(cycles.items()))} "
        f"period_states={dict(sorted(period_states.items()))} "
        f"max_fibre={max(fibres.values())}"
    )


def main() -> None:
    print("Adjacent-sum reranking exact kill certificate")
    print("STATUS HOLD_EXTERNAL")
    for n in range(1, 10):
        audit_rank(n)
    for n in range(3, 101):
        seed = principal_cycle_seed(n)
        check(step(step(seed)) == rotate(seed), "symbolic-family regression")
    print("KILL reason=recurrent atlas branches by n=9 and no target inverse axis")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
