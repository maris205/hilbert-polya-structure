#!/usr/bin/env python3
"""Exact falsifier for multiplicity-profile descent on integer partitions."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, defaultdict


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()


def partitions(n: int, least: int = 1):
    """Partitions in weakly increasing tuple notation."""
    if n == 0:
        yield ()
        return
    for first in range(least, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def profile(partition: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(Counter(partition).values()))


def lift(partition: tuple[int, ...]) -> tuple[int, ...]:
    """Canonical lift; input/output both use increasing notation."""
    out: list[int] = []
    for value, multiplicity in enumerate(sorted(partition, reverse=True), 1):
        out.extend([value] * multiplicity)
    return tuple(out)


def ferrers_contained(inner: tuple[int, ...], outer: tuple[int, ...]) -> bool:
    left = tuple(sorted(inner, reverse=True))
    right = tuple(sorted(outer, reverse=True))
    return len(left) <= len(right) and all(a <= b for a, b in zip(left, right))


def depth(partition: tuple[int, ...]) -> int:
    steps = 0
    seen = set()
    while partition != (1,):
        A.check(partition not in seen, "no nontrivial cycle")
        seen.add(partition)
        old_size = sum(partition)
        partition = profile(partition)
        A.check(sum(partition) <= old_size, "size does not increase")
        steps += 1
    return steps


def distinct_permutations(values: tuple[int, ...]):
    counter = Counter(values)
    keys = sorted(counter)
    word: list[int] = []

    def rec():
        if len(word) == len(values):
            yield tuple(word)
            return
        for key in keys:
            if counter[key]:
                counter[key] -= 1
                word.append(key)
                yield from rec()
                word.pop()
                counter[key] += 1

    yield from rec()


def fibre_coefficients(target: tuple[int, ...], cap: int) -> list[int]:
    """Coefficients of Phi_target(q) through q^cap."""
    answer = [0] * (cap + 1)
    for ordering in distinct_permutations(target):
        suffix = []
        running = 0
        for value in reversed(ordering):
            running += value
            suffix.append(running)
        suffix.reverse()
        dp = [0] * (cap + 1)
        dp[0] = 1
        for step in suffix:
            nxt = [0] * (cap + 1)
            for degree, count in enumerate(dp):
                if not count:
                    continue
                for gap in range(1, (cap - degree) // step + 1):
                    nxt[degree + gap * step] += count
            dp = nxt
        answer = [a + b for a, b in zip(answer, dp)]
    return answer


def canonical_thresholds(limit: int) -> tuple[list[int], list[tuple[int, ...]]]:
    state = (2,)
    sizes = []
    states = []
    for expected_depth in range(1, limit + 1):
        A.equal(depth(state), expected_depth, "canonical depth")
        sizes.append(sum(state))
        states.append(state)
        if expected_depth != limit:
            state = lift(state)
    return sizes, states


def main() -> None:
    thresholds, canonical_states = canonical_thresholds(10)
    expected = [2, 2, 3, 4, 7, 14, 42, 213, 2837, 175450]
    A.equal(thresholds, expected, "shifted Levine thresholds")

    exact_minimum: dict[int, tuple[int, list[tuple[int, ...]]]] = {}
    height_by_cap: dict[int, int] = {}
    running_height = 0
    state_count = 0
    for size in range(1, 43):
        for state in partitions(size):
            state_count += 1
            image = profile(state)
            A.equal(profile(lift(image)), image, "lift is a right inverse")
            A.check(ferrers_contained(lift(image), state), "canonical containment")
            d = depth(state)
            running_height = max(running_height, d)
            if d not in exact_minimum or size < exact_minimum[d][0]:
                exact_minimum[d] = (size, [state])
            elif size == exact_minimum[d][0]:
                exact_minimum[d][1].append(state)
        height_by_cap[size] = running_height
        predicted = max([0] + [d for d, value in enumerate(thresholds, 1)
                               if value <= size])
        A.equal(running_height, predicted, "sharp capped height")

    for d in range(1, 8):
        A.equal(exact_minimum[d],
                (thresholds[d - 1], [canonical_states[d - 1]]),
                "unique exact-depth minimum checked by enumeration")

    # Exhaustive source-to-target coefficients through source size 28.
    cap = 28
    actual: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    source_count = 0
    for size in range(1, cap + 1):
        for source in partitions(size):
            source_count += 1
            actual[profile(source)][size] += 1

    target_count = 0
    for target_size in range(1, 15):
        for target in partitions(target_size):
            target_count += 1
            coefficients = fibre_coefficients(target, cap)
            for source_size in range(1, cap + 1):
                A.equal(coefficients[source_size], actual[target][source_size],
                        "every-target source-size coefficient")
            least = sum(i * value for i, value in enumerate(
                sorted(target, reverse=True), 1))
            support = [i for i, value in enumerate(coefficients) if value]
            # The coefficient audit is truncated at ``cap``.  Targets whose
            # canonical least source lies above that cutoff must have empty
            # truncated support; right-invertibility itself was checked for
            # every target above.
            if least <= cap:
                A.check(bool(support), "target represented below cutoff")
                A.equal(min(support), least, "least source size")
                A.equal(coefficients[least], 1,
                        "unique canonical least source")
                A.equal(lift(target), next(
                    source for source in partitions(least)
                    if profile(source) == target),
                    "canonical least source identity")
            else:
                A.check(not support, "no source below canonical minimum")

    # Exhaustive containment-monotonicity on all partitions through size 12.
    small_states = [state for size in range(1, 13) for state in partitions(size)]
    comparable_pairs = 0
    for inner in small_states:
        for outer in small_states:
            if ferrers_contained(inner, outer):
                comparable_pairs += 1
                A.check(ferrers_contained(lift(inner), lift(outer)),
                        "lift preserves Ferrers containment")

    report = {
        "assertions": A.assertions,
        "canonical_states_1_to_8": {
            str(i): list(canonical_states[i - 1])
            for i in range(1, 9)
        },
        "comparable_pairs_checked": comparable_pairs,
        "decision": "AMBER_OWNER_DENSE_NEEDS_HOSTILE_GATE",
        "every_target_checked": target_count,
        "external_status": "HOLD_EXTERNAL",
        "height_by_cap_1_to_42": height_by_cap,
        "literal_map": "sorted positive multiplicities of distinct parts",
        "sources_checked_for_fibres": source_count,
        "states_checked_for_clock": state_count,
        "thresholds_1_to_10": thresholds,
    }
    encoded = json.dumps(report, indent=2, sort_keys=True)
    report["payload_sha256"] = hashlib.sha256(encoded.encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
