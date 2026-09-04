#!/usr/bin/env python3
"""Paper-local exact verifier for rank-compression support dynamics.

The code is standard-library only and imports no scouting or earlier-paper
module.  One assertion is one call to Audit.check.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from math import comb


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def subsets(n: int):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask >> i & 1)


def update(a):
    return tuple(sorted({value - rank for rank, value in enumerate(a)}))


def iterate(a, t: int):
    value = a
    for _ in range(t):
        value = update(value)
    return value


def gap_formula(a, t: int):
    if not a:
        return ()
    answer = [a[0]]
    for j in range(1, len(a)):
        gap = a[j] - a[j - 1]
        if gap > t:
            answer.append(answer[-1] + gap - t)
    return tuple(answer)


def tail(a) -> int:
    if len(a) < 2:
        return 0
    return max(a[j] - a[j - 1] for j in range(1, len(a)))


def fibonacci(k: int) -> int:
    x, y = 0, 1
    for _ in range(k):
        x, y = y, x + y
    return x


@lru_cache(maxsize=None)
def slot_series_prefix(t: int, slots: int, budget: int) -> int:
    """Sum of coefficients through budget in (1-z-...-z^t)^(-slots)."""
    if budget < 0:
        return 0
    one_slot = [0] * (budget + 1)
    one_slot[0] = 1
    for weight in range(1, budget + 1):
        one_slot[weight] = sum(
            one_slot[weight - part]
            for part in range(1, min(t, weight) + 1)
        )
    poly = [1] + [0] * budget
    for _ in range(slots):
        nxt = [0] * (budget + 1)
        for left, left_count in enumerate(poly):
            for right, right_count in enumerate(one_slot[: budget - left + 1]):
                nxt[left + right] += left_count * right_count
        poly = nxt
    return sum(poly)


def fibre_formula(b, t: int, n: int) -> int:
    if not b:
        return 1
    r = len(b) - 1
    forced_span = b[-1] - b[0] + t * r
    budget = n - 1 - b[0] - forced_span
    return slot_series_prefix(t, r + 1, budget)


def depth_cdf_formula(n: int, h: int) -> int:
    # Coefficients of 1/(1-(z+...+z^h)): bounded positive-gap words.
    words = [0] * n
    words[0] = 1
    for span in range(1, n):
        words[span] = sum(
            words[span - gap] for gap in range(1, min(h, span) + 1)
        )
    return 1 + sum((n - span) * words[span] for span in range(n))


def verify_rank(n: int):
    states = list(subsets(n))
    # Include one epoch beyond the sharp height, so the n=1 first image and
    # every stabilized carrier are checked without a boundary exception.
    time_fibres = [Counter() for _ in range(n + 1)]
    tails = Counter()
    endpoints = Counter()

    for a in states:
        AUDIT.check(update(a) == gap_formula(a, 1), "one-step gap formula")
        value = a
        trajectory = []
        for t in range(n + 1):
            if t:
                value = update(value)
            literal = value
            trajectory.append(literal)
            closed = gap_formula(a, t)
            AUDIT.check(literal == closed, "all-time pointwise formula")
            time_fibres[t][literal] += 1
        height = tail(a)
        tails[height] += 1
        endpoint = () if not a else (a[0],)
        endpoints[endpoint] += 1
        AUDIT.check(trajectory[height] == endpoint, "clock reaches endpoint")
        if height:
            AUDIT.check(trajectory[height - 1] != endpoint, "clock is least")
        AUDIT.check(update(endpoint) == endpoint, "endpoint fixed")

    for t in range(n + 1):
        observed = time_fibres[t]
        predicted = {
            b
            for b in states
            if not b or b[-1] + t * (len(b) - 1) < n
        }
        AUDIT.check(set(observed) == predicted, "all-time image criterion")
        predicted_image_size = 1 + sum(
            comb(n - t * r, r + 1)
            for r in range(n)
            if n - t * r >= r + 1
        )
        AUDIT.check(len(observed) == predicted_image_size, "all-time image size")
        for b in predicted:
            AUDIT.check(
                observed[b] == fibre_formula(b, t, n),
                "all-time every-target fibre",
            )
            if t == 1 and b:
                AUDIT.check(
                    observed[b] == comb(n - b[-1], len(b)),
                    "one-step binomial fibre",
                )
        AUDIT.check(sum(observed.values()) == 1 << n, "fibre mass")

    AUDIT.check(len(time_fibres[1]) == fibonacci(n + 2), "Fibonacci first image")
    AUDIT.check(endpoints[()] == 1, "empty basin")
    for minimum in range(n):
        AUDIT.check(
            endpoints[(minimum,)] == 1 << (n - minimum - 1),
            "singleton basin",
        )
    for h in range(n):
        actual = sum(count for depth, count in tails.items() if depth <= h)
        AUDIT.check(actual == depth_cdf_formula(n, h), "depth CDF")

    deepest = [a for a in states if tail(a) == n - 1]
    expected_deepest = [(0, n - 1)] if n > 1 else [(), (0,)]
    AUDIT.check(deepest == expected_deepest, "sharp deepest states")
    fixed = sum(update(a) == a for a in states)
    AUDIT.check(fixed == n + 1, "fixed set size")
    return (
        n,
        len(states),
        len(time_fibres[1]),
        fixed,
        max(tails),
        max(time_fibres[1].values()),
        tuple(sorted(tails.items())),
    )


def main() -> None:
    summaries = []
    for n in range(1, 19):
        before = AUDIT.count
        row = verify_rank(n)
        summaries.append(row)
        print(f"n={n} assertions={AUDIT.count-before} summary={row}")
    print(f"exact_assertions={AUDIT.count}")
    print("ranks=1..18")
    print("status=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
