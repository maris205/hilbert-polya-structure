#!/usr/bin/env python3
"""Independent exact checks for bracket-matching-support dynamics.

This reserve is intentionally not promoted: the script verifies the static
image/fibre theorem and the strict two-coordinate convergence potential, but
no sharp all-n maximum clock is claimed.
"""

from __future__ import annotations

from collections import Counter
from math import comb


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def literal_support(word: tuple[int, ...]) -> tuple[int, ...]:
    """Delete adjacent 10 pairs in the current residual word to exhaustion."""
    active = list(range(len(word)))
    matched = set()
    while True:
        next_active = []
        index = 0
        changed = False
        while index < len(active):
            if index + 1 < len(active):
                left, right = active[index], active[index + 1]
                if word[left] == 1 and word[right] == 0:
                    matched.add(left)
                    matched.add(right)
                    index += 2
                    changed = True
                    continue
            next_active.append(active[index])
            index += 1
        active = next_active
        if not changed:
            break
    return tuple(int(position in matched) for position in range(len(word)))


def words(n: int):
    for mask in range(1 << n):
        yield tuple((mask >> (n - 1 - index)) & 1 for index in range(n))


def runs(word: tuple[int, ...]) -> tuple[int, ...]:
    answer = []
    index = 0
    while index < len(word):
        if word[index] == 0:
            index += 1
            continue
        end = index
        while end < len(word) and word[end] == 1:
            end += 1
        answer.append(end - index)
        index = end
    return tuple(answer)


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def fibre_formula(target: tuple[int, ...]) -> int:
    lengths = runs(target)
    if any(length % 2 for length in lengths):
        return 0
    zeros = target.count(0)
    answer = zeros + 1
    for length in lengths:
        answer *= catalan(length // 2)
    return answer


def first_run_coordinates(word: tuple[int, ...]):
    try:
        left = word.index(1)
    except ValueError:
        return None
    right = left
    while right + 1 < len(word) and word[right + 1] == 1:
        right += 1
    return left, right


def fibonacci_image_count(n: int) -> int:
    # Binary words whose 1-runs all have even length.  State 0 is outside a
    # run, state 1 is inside an odd run, and state 2 is inside an even run.
    dp = (1, 0, 0)
    for _ in range(n):
        outside, odd, even = dp
        dp = (outside + even, outside + even, odd)
    return dp[0] + dp[2]


def audit(n: int) -> None:
    states = tuple(words(n))
    zero = (0,) * n
    successor = {}
    fibres = Counter()
    max_tail = 0
    for source in states:
        target = literal_support(source)
        successor[source] = target
        fibres[target] += 1
        check(all(length % 2 == 0 for length in runs(target)), "even image runs")
    check(len(fibres) == fibonacci_image_count(n), "three-state image DP")
    for target in states:
        check(fibres.get(target, 0) == fibre_formula(target), "every-target formula")
        if target in fibres and target != zero:
            nxt = successor[target]
            old_coordinates = first_run_coordinates(target)
            new_coordinates = first_run_coordinates(nxt)
            check(
                new_coordinates is None
                or new_coordinates[0] > old_coordinates[0]
                or (
                    new_coordinates[0] == old_coordinates[0]
                    and new_coordinates[1] > old_coordinates[1]
                ),
                "strict lexicographic first-run potential",
            )
    for source in states:
        point = source
        tail = 0
        while point != zero:
            point = successor[point]
            tail += 1
            check(tail <= 1 + n * (n + 1) // 2, "potential-derived convergence bound")
        max_tail = max(max_tail, tail)
    check(sum(fibres.values()) == 1 << n, "fibre mass")
    print(
        f"n={n} states={len(states)} image={len(fibres)} "
        f"height={max_tail} max_fibre={max(fibres.values())}"
    )


def main() -> None:
    print("Bracket-matching-support independent verifier")
    print("STATUS HOLD_EXTERNAL")
    for n in range(1, 17):
        audit(n)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
