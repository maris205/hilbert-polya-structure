#!/usr/bin/env python3
"""Paper-local exact verifier for prefix-diversity delay dynamics.

Standard library only; no scouting or earlier-paper code is imported.  One
assertion means one call to Audit.check.
"""

from __future__ import annotations

from collections import Counter
from itertools import product


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def update(word):
    seen = set()
    answer = []
    for letter in word:
        answer.append(len(seen))
        seen.add(letter)
    return tuple(answer)


def closed_iterate(word, t: int):
    if t == 0:
        return tuple(word)
    d = update(word)
    shift = t - 1
    return tuple(
        i if i < shift else shift + d[i - shift]
        for i in range(len(word))
    )


def falling(n: int, k: int) -> int:
    answer = 1
    for value in range(n - k + 1, n + 1):
        answer *= value
    return answer


def distinct_prefix_length(word) -> int:
    seen = set()
    for i, letter in enumerate(word):
        if letter in seen:
            return i
        seen.add(letter)
    return len(word)


def clock(word) -> int:
    identity = tuple(range(len(word)))
    if word == identity:
        return 0
    return max(1, len(word) - distinct_prefix_length(word))


def image_condition(target, t: int) -> bool:
    n = len(target)
    if not 1 <= t <= n - 1:
        return target == tuple(range(n))
    if any(target[i] != i for i in range(t + 1)):
        return False
    return all(target[i] - target[i - 1] in (0, 1) for i in range(t + 1, n))


def fibre_formula(target, t: int, n: int) -> int:
    if t >= n - 1:
        return n**n if target == tuple(range(n)) else 0
    shift = t - 1
    d = tuple(target[j + shift] - shift for j in range(n - shift))
    choices = n ** (t + 1)  # first letter and the t invisible final letters
    for q in range(1, n - t):
        novelty = d[q + 1] - d[q]
        AUDIT.check(novelty in (0, 1), "visible novelty bit")
        choices *= n - d[q] if novelty else d[q]
    return choices


def verify_rank(n: int):
    states = list(product(range(n), repeat=n))
    identity = tuple(range(n))
    fibres = {t: Counter() for t in range(1, n)}
    tails = Counter()
    fixed = []

    for word in states:
        first = update(word)
        AUDIT.check(first[0] == 0, "first coordinate")
        if n > 1:
            AUDIT.check(first[1] == 1, "second coordinate")
        AUDIT.check(all(
            first[i] - first[i - 1] in (0, 1) for i in range(1, n)
        ), "novelty path")
        value = word
        trajectory = [word]
        for t in range(1, n):
            value = update(value)
            trajectory.append(value)
            AUDIT.check(value == closed_iterate(word, t), "all-time point formula")
            fibres[t][value] += 1
        if update(word) == word:
            fixed.append(word)
        tau = clock(word)
        tails[tau] += 1
        AUDIT.check(trajectory[tau] == identity, "clock reaches identity")
        if tau:
            AUDIT.check(trajectory[tau - 1] != identity, "clock is least")
        AUDIT.check(update(identity) == identity, "identity fixed")

    AUDIT.check(fixed == [identity], "unique fixed point")
    if n == 1:
        AUDIT.check(tails == Counter({0: 1}), "singleton carrier")
        return (1, 1, 1, 0, ((0, 1),))

    for t in range(1, n):
        observed = fibres[t]
        predicted = {target for target in states if image_condition(target, t)}
        AUDIT.check(set(observed) == predicted, "all-time image language")
        AUDIT.check(len(observed) == 2 ** (n - t - 1), "all-time image size")
        for target in predicted:
            AUDIT.check(
                observed[target] == fibre_formula(target, t, n),
                "all-time every-target fibre",
            )
        AUDIT.check(sum(observed.values()) == n**n, "fibre mass")
        actual_cdf = sum(count for depth, count in tails.items() if depth <= t)
        predicted_cdf = falling(n, n - t) * n**t
        AUDIT.check(actual_cdf == predicted_cdf, "depth CDF")
        AUDIT.check(observed[identity] == predicted_cdf, "identity fibre equals CDF")

    AUDIT.check(max(tails) == n - 1, "sharp global height")
    expected_deepest = 3 if n == 2 else n ** (n - 1)
    AUDIT.check(tails[n - 1] == expected_deepest, "deepest-state population")
    return (n, n**n, len(fibres[1]), max(tails), tuple(sorted(tails.items())))


def main() -> None:
    rows = []
    for n in range(1, 8):
        before = AUDIT.count
        row = verify_rank(n)
        rows.append(row)
        print(f"n={n} assertions={AUDIT.count-before} summary={row}")
    print(f"exact_assertions={AUDIT.count}")
    print("ranks=1..7")
    print("status=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
