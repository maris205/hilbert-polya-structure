#!/usr/bin/env python3
"""Exact falsifier for adjacent-run consolidation on integer compositions.

Enumeration is counterexample pressure only.  The accompanying scout gives
the proofs and treats classical Carlitz-composition enumeration as zero-credit
input.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def compositions(total: int):
    """All positive compositions of ``total`` in separator-mask order."""
    if total == 0:
        yield ()
        return
    for mask in range(1 << (total - 1)):
        parts = []
        current = 1
        for gap in range(total - 1):
            if mask & (1 << gap):
                parts.append(current)
                current = 1
            else:
                current += 1
        parts.append(current)
        yield tuple(parts)


def consolidate(state: tuple[int, ...]) -> tuple[int, ...]:
    """Replace every maximal equal run s^r by its sum rs."""
    result = []
    cursor = 0
    while cursor < len(state):
        end = cursor + 1
        while end < len(state) and state[end] == state[cursor]:
            end += 1
        result.append((end - cursor) * state[cursor])
        cursor = end
    return tuple(result)


def orbit(state: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    seen = set()
    depth = 0
    current = state
    while True:
        check(current not in seen, "ARC acquired a nontrivial cycle")
        seen.add(current)
        nxt = consolidate(current)
        if nxt == current:
            return current, depth
        check(len(nxt) < len(current), "ARC did not strictly shorten")
        check(sum(nxt) == sum(current), "ARC did not preserve total")
        current = nxt
        depth += 1


@lru_cache(maxsize=None)
def divisors(number: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, number + 1) if number % value == 0)


def fibre_polynomial(target: tuple[int, ...]) -> Counter[int]:
    """Coefficient of u^ell counts predecessors having ell input parts."""
    frontier: dict[int, Counter[int]] = {}
    first = target[0]
    for base in divisors(first):
        frontier[base] = Counter({first // base: 1})
    for part in target[1:]:
        updated: dict[int, Counter[int]] = {}
        for base in divisors(part):
            profile = Counter()
            added_length = part // base
            for previous, polynomial in frontier.items():
                if previous == base:
                    continue
                for degree, coefficient in polynomial.items():
                    profile[degree + added_length] += coefficient
            if profile:
                updated[base] = profile
        frontier = updated
    answer = Counter()
    for polynomial in frontier.values():
        answer.update(polynomial)
    return answer


def sharp_witness(total: int) -> tuple[int, ...]:
    if total == 1:
        return (1,)
    depth = total.bit_length() - 1
    cascade = (1, 1) + tuple(1 << power for power in range(1, depth))
    remainder = total - (1 << depth)
    if remainder == 0:
        return cascade
    if remainder == (1 << (depth - 1)):
        return (remainder,) + cascade
    return cascade + (remainder,)


def carlitz_counts(bound: int) -> list[int]:
    """DP for compositions with adjacent unequal parts."""
    totals = [0] * (bound + 1)
    totals[0] = 1
    ending = [[0] * (bound + 1) for _ in range(bound + 1)]
    for total in range(1, bound + 1):
        for last in range(1, total + 1):
            prefix = total - last
            ending[total][last] = totals[prefix] - ending[prefix][last]
        totals[total] = sum(ending[total])
    return totals


def main() -> None:
    bound = 18
    fixed_expected = carlitz_counts(bound)
    total_states = 0
    total_targets = 0
    largest_fibre = 0
    profiles = []

    for total in range(1, bound + 1):
        incoming: dict[tuple[int, ...], Counter[int]] = {}
        depth_census = Counter()
        fixed = 0
        maximum = 0
        deepest = 0
        states = tuple(compositions(total))
        for state in states:
            target = consolidate(state)
            incoming.setdefault(target, Counter())[len(state)] += 1
            endpoint, depth = orbit(state)
            check(consolidate(endpoint) == endpoint, "ARC endpoint not fixed")
            check(
                (target == state)
                == all(left != right for left, right in zip(state, state[1:])),
                "ARC fixed-point criterion",
            )
            check(depth <= total.bit_length() - 1, "ARC logarithmic bound")
            depth_census[depth] += 1
            fixed += int(target == state)
            if depth > maximum:
                maximum, deepest = depth, 1
            elif depth == maximum:
                deepest += 1

        expected_count = 1 << max(0, total - 1)
        check(len(states) == expected_count, "ARC composition census")
        check(fixed == fixed_expected[total], "ARC Carlitz fixed census")
        expected_maximum = total.bit_length() - 1
        check(maximum == expected_maximum, "ARC sharp clock")
        witness = sharp_witness(total)
        check(sum(witness) == total, "ARC witness total")
        check(orbit(witness)[1] == expected_maximum, "ARC witness depth")

        for target in compositions(total):
            observed = incoming.get(target, Counter())
            predicted = fibre_polynomial(target)
            check(observed == predicted, "ARC target-resolved fibre polynomial")
            check((sum(observed.values()) > 0) == bool(predicted), "ARC image gate")
            largest_fibre = max(largest_fibre, sum(observed.values()))

        total_states += len(states)
        total_targets += len(incoming)
        profile = "/".join(
            f"{depth}:{count}" for depth, count in sorted(depth_census.items())
        )
        profiles.append(
            f"n{total}:S{len(states)}:I{len(incoming)}:F{fixed}:"
            f"T{maximum}:D{profile}:W{deepest}"
        )

    check(total_states == (1 << bound) - 1, "ARC aggregate state census")
    print("P147-P151 ROOT REPLACEMENT SCOUT")
    print("SYSTEM=ARC adjacent-run consolidation on positive compositions")
    print(f"BOUND={bound}")
    print(f"STATES={total_states}")
    print(f"IMAGE_TARGETS_SUM={total_targets}")
    print(f"MAX_ONE_STEP_FIBRE={largest_fibre}")
    print("PROFILES=" + ";".join(profiles))
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
