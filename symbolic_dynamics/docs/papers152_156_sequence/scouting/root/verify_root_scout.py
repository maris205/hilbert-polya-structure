#!/usr/bin/env python3
"""Exact root negative controls for P152--P156.

The checks are falsification pressure, not deductive proofs or owner clearance.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product, permutations
from math import comb, floor, log2


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def parity_sieve(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(bit for i, bit in enumerate(word, 1) if bit == (i & 1))


def tail_and_terminal(word: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    current = word
    tail = 0
    while True:
        nxt = parity_sieve(current)
        if nxt == current:
            return tail, current
        check(len(nxt) < len(current), "R01 strict descent off the fixed set")
        current = nxt
        tail += 1


def alternating(length: int) -> tuple[int, ...]:
    return tuple(i & 1 for i in range(1, length + 1))


def fibre_recurrence(source_length: int, target: tuple[int, ...]) -> int:
    ways = [0] * (len(target) + 1)
    ways[0] = 1
    for i in range(1, source_length + 1):
        for j in range(min(i, len(target)), 0, -1):
            if (i & 1) == target[j - 1]:
                ways[j] += ways[j - 1]
    return ways[-1]


def minimal_source_length(target: tuple[int, ...]) -> int:
    position = 0
    for bit in target:
        position += 1
        if (position & 1) != bit:
            position += 1
    return position


def audit_parity_sieve() -> tuple[int, int, int]:
    words = 0
    max_tail_seen = 0
    terminal_classes = 0
    for n in range(1, 19):
        terminals = Counter()
        max_tail = 0
        for word in product((0, 1), repeat=n):
            words += 1
            tail, terminal = tail_and_terminal(word)
            check(terminal == alternating(len(terminal)), "R01 terminal form")
            terminals[len(terminal)] += 1
            max_tail = max(max_tail, tail)
        expected_tail = floor(log2(n)) + 1
        check(max_tail == expected_tail, "R01 sharp clock profile")
        zero_tail, _ = tail_and_terminal((0,) * n)
        check(zero_tail == expected_tail, "R01 all-zero sharp witness")
        for m in range(n + 1):
            check(
                terminals[m] == comb(n, (n - m) // 2),
                "R01 binomial terminal layer",
            )
            terminal_classes += 1
        max_tail_seen = max(max_tail_seen, max_tail)

    for n in range(0, 12):
        incoming: dict[tuple[int, ...], int] = defaultdict(int)
        for source in product((0, 1), repeat=n):
            incoming[parity_sieve(source)] += 1
        for m in range(n + 1):
            for target in product((0, 1), repeat=m):
                predicted = fibre_recurrence(n, target)
                check(incoming[target] == predicted, "R01 every-target fibre")
                check(
                    (predicted > 0) == (minimal_source_length(target) <= n),
                    "R01 greedy image criterion",
                )
    return words, terminal_classes, max_tail_seen


def erase_fixed_points(permutation: tuple[int, ...]) -> tuple[int, ...]:
    kept = [value for i, value in enumerate(permutation, 1) if value != i]
    ranks = {value: rank for rank, value in enumerate(sorted(kept), 1)}
    return tuple(ranks[value] for value in kept)


def audit_fixed_point_erasure() -> int:
    states = 0
    for n in range(0, 11):
        for permutation in permutations(range(1, n + 1)):
            states += 1
            first = erase_fixed_points(permutation)
            check(erase_fixed_points(first) == first, "R02 idempotence")
            check(
                all(value != i for i, value in enumerate(first, 1)),
                "R02 derangement image",
            )
    return states


def main() -> None:
    words, terminal_classes, max_tail = audit_parity_sieve()
    permutations_checked = audit_fixed_point_erasure()
    print("P152-P156 ROOT CROSS-CLASS SCOUT")
    print(
        "R01 "
        f"words={words} terminal_classes={terminal_classes} "
        f"max_tail={max_tail} status=KILL_OWNER_HEAVY_NEGATIVE_CONTROL"
    )
    print(
        "R02 "
        f"permutations={permutations_checked} "
        "status=KILL_IDEMPOTENT_BELOW_THRESHOLD"
    )
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()

