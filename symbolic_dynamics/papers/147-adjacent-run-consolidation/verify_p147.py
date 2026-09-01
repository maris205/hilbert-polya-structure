#!/usr/bin/env python3
"""Exact falsifier for P147 adjacent-run consolidation.

Enumeration is counterexample pressure only.  All arithmetic is exact and
uses only the Python standard library.
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
        check(current not in seen, "nontrivial cycle")
        seen.add(current)
        nxt = consolidate(current)
        if nxt == current:
            return current, depth
        check(len(nxt) < len(current), "no strict length descent")
        check(sum(nxt) == sum(current), "weight not preserved")
        current = nxt
        depth += 1


@lru_cache(maxsize=None)
def divisors(number: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, number + 1) if number % value == 0)


def fibre_polynomial(target: tuple[int, ...]) -> Counter[int]:
    frontier: dict[int, Counter[int]] = {}
    for base in divisors(target[0]):
        frontier[base] = Counter({target[0] // base: 1})
    for part in target[1:]:
        updated: dict[int, Counter[int]] = {}
        for base in divisors(part):
            polynomial = Counter()
            for previous, profile in frontier.items():
                if previous == base:
                    continue
                for degree, coefficient in profile.items():
                    polynomial[degree + part // base] += coefficient
            if polynomial:
                updated[base] = polynomial
        frontier = updated
    result = Counter()
    for polynomial in frontier.values():
        result.update(polynomial)
    return result


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
    expected_fixed = carlitz_counts(bound)
    total_states = 0
    total_targets = 0
    largest_fibre = 0
    profiles = []
    for total in range(1, bound + 1):
        incoming: dict[tuple[int, ...], Counter[int]] = {}
        depths = Counter()
        fixed = 0
        maximum = 0
        deepest = 0
        states = tuple(compositions(total))
        for state in states:
            target = consolidate(state)
            incoming.setdefault(target, Counter())[len(state)] += 1
            endpoint, depth = orbit(state)
            check(consolidate(endpoint) == endpoint, "endpoint not fixed")
            check(
                (target == state)
                == all(left != right for left, right in zip(state, state[1:])),
                "fixed criterion",
            )
            check(depth <= total.bit_length() - 1, "clock upper bound")
            depths[depth] += 1
            fixed += int(target == state)
            if depth > maximum:
                maximum, deepest = depth, 1
            elif depth == maximum:
                deepest += 1
        check(len(states) == 1 << max(0, total - 1), "composition census")
        check(fixed == expected_fixed[total], "Carlitz census")
        expected_maximum = total.bit_length() - 1
        check(maximum == expected_maximum, "sharp clock")
        witness = sharp_witness(total)
        check(sum(witness) == total, "witness weight")
        check(orbit(witness)[1] == expected_maximum, "witness depth")
        for target in compositions(total):
            observed = incoming.get(target, Counter())
            predicted = fibre_polynomial(target)
            check(observed == predicted, "target fibre polynomial")
            check(bool(observed) == bool(predicted), "image criterion")
            largest_fibre = max(largest_fibre, sum(observed.values()))
        total_states += len(states)
        total_targets += len(incoming)
        profile = "/".join(f"{d}:{c}" for d, c in sorted(depths.items()))
        profiles.append(
            f"n{total}:S{len(states)}:I{len(incoming)}:F{fixed}:"
            f"T{maximum}:D{profile}:W{deepest}"
        )
    check(total_states == (1 << bound) - 1, "aggregate state census")
    print("P147 ADJACENT-RUN CONSOLIDATION EXACT AUDIT")
    print(f"BOUND={bound}")
    print(f"STATES={total_states}")
    print(f"IMAGE_TARGETS_SUM={total_targets}")
    print(f"MAX_ONE_STEP_FIBRE={largest_fibre}")
    print("PROFILES=" + ";".join(profiles))
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
