#!/usr/bin/env python3
"""Exhaustive verifier for prefix-divisibility cut dynamics.

This file is deliberately self-contained and uses only the Python standard
library.  It does not import the scouting implementation.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from typing import Dict, Iterable, List, Sequence, Tuple


Composition = Tuple[int, ...]
MAX_N = 18


class Checks:
    """Count successful hard assertions and fail with a useful label."""

    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


def compositions(total: int) -> Tuple[Composition, ...]:
    """All positive compositions, ordered by their internal-cut bit mask."""

    result: List[Composition] = []
    for mask in range(1 << (total - 1)):
        previous = 0
        parts: List[int] = []
        for cut in range(1, total):
            if mask & (1 << (cut - 1)):
                parts.append(cut - previous)
                previous = cut
        parts.append(total - previous)
        result.append(tuple(parts))
    return tuple(result)


def internal_cuts(composition: Composition) -> Tuple[int, ...]:
    prefix = 0
    result: List[int] = []
    for part in composition[:-1]:
        prefix += part
        result.append(prefix)
    return tuple(result)


def composition_from_cuts(total: int, cuts: Iterable[int]) -> Composition:
    previous = 0
    result: List[int] = []
    for endpoint in cuts:
        result.append(endpoint - previous)
        previous = endpoint
    result.append(total - previous)
    return tuple(result)


def update(composition: Composition) -> Composition:
    """Literal simultaneous update: retain cut s_i exactly when a_i | s_i."""

    total = sum(composition)
    prefix = 0
    retained: List[int] = []
    for part in composition[:-1]:
        prefix += part
        if prefix % part == 0:
            retained.append(prefix)
    return composition_from_cuts(total, retained)


def fixed_criterion(composition: Composition) -> bool:
    """Independent statement of the proposed fixed-point criterion."""

    prefix = 0
    for part in composition[:-1]:
        prefix += part
        if prefix % part:
            return False
    return True


def fixed_count_recurrence(total: int) -> int:
    """Count stable prefix paths by the divisor-step recurrence.

    Let q[s] count stable paths ending at an internal prefix s.  Their last
    part d must divide s, so q[s] = sum_{d|s} q[s-d], with q[0] = 1.
    The final part is untested, hence f[N] = sum_{s=0}^{N-1} q[s].
    """

    stable_prefix_paths = [0] * total
    stable_prefix_paths[0] = 1
    for endpoint in range(1, total):
        stable_prefix_paths[endpoint] = sum(
            stable_prefix_paths[endpoint - step]
            for step in range(1, endpoint + 1)
            if endpoint % step == 0
        )
    return sum(stable_prefix_paths)


def tail_and_period(start: Composition, successor: Dict[Composition, Composition]) -> Tuple[int, int]:
    first_seen: Dict[Composition, int] = {}
    state = start
    while state not in first_seen:
        first_seen[state] = len(first_seen)
        state = successor[state]
    return first_seen[state], len(first_seen) - first_seen[state]


def global_no_skip_fibre(total: int, target: Composition) -> int:
    """One-step fibre DP on all possible source endpoints.

    A transition u -> v is forbidden if it skips a required target cut.  At
    an internal source endpoint v, its incoming part v-u must divide v iff v
    is a target cut.  The final endpoint N is never tested by the update.
    """

    target_cuts = internal_cuts(target)
    target_set = set(target_cuts)
    ways = [0] * (total + 1)
    ways[0] = 1
    last_required = 0
    target_index = 0
    for endpoint in range(1, total + 1):
        while target_index < len(target_cuts) and target_cuts[target_index] < endpoint:
            last_required = target_cuts[target_index]
            target_index += 1
        for previous in range(last_required, endpoint):
            if not ways[previous]:
                continue
            if endpoint < total:
                retained = endpoint % (endpoint - previous) == 0
                if retained != (endpoint in target_set):
                    continue
            ways[endpoint] += ways[previous]
    return ways[total]


def interval_path_count(left: int, right: int, terminal: bool) -> int:
    """Count admissible source paths inside one target interval."""

    ways = [0] * (right + 1)
    ways[left] = 1
    for endpoint in range(left + 1, right + 1):
        for previous in range(left, endpoint):
            if not ways[previous]:
                continue
            incoming = endpoint - previous
            if endpoint < right:
                # Strict intermediate endpoints are deleted source cuts.
                if endpoint % incoming == 0:
                    continue
            elif not terminal:
                # A nonterminal right endpoint is a retained target cut.
                if endpoint % incoming:
                    continue
            # At the terminal endpoint N the final source part is untested.
            ways[endpoint] += ways[previous]
    return ways[right]


def factorized_fibre(total: int, target: Composition) -> int:
    endpoints = internal_cuts(target) + (total,)
    product = 1
    left = 0
    for right in endpoints:
        product *= interval_path_count(left, right, terminal=(right == total))
        left = right
    return product


def witness_at_time(total: int, time: int) -> Composition:
    """Claimed trajectory of (1,2,1^(N-3)), including its fixed endpoint."""

    return (1, time + 2) + (1,) * (total - time - 3)


def encode(composition: Composition) -> str:
    return ".".join(str(part) for part in composition)


def main() -> None:
    checks = Checks()
    digest = sha256()
    transition_count = 0
    rows: List[str] = []

    for total in range(1, MAX_N + 1):
        states = compositions(total)
        state_set = set(states)
        successor = {state: update(state) for state in states}
        transition_count += len(states)

        checks.require(len(states) == 1 << (total - 1), f"composition count N={total}")
        checks.require(len(state_set) == len(states), f"unique enumeration N={total}")
        checks.require(len(successor) == len(states), f"total function N={total}")

        indegree: Counter[Composition] = Counter(successor.values())
        image = set(indegree)
        fixed: set[Composition] = set()
        recurrent: set[Composition] = set()
        tails: Dict[Composition, int] = {}

        for state in states:
            target = successor[state]
            digest.update(f"{total}:{encode(state)}->{encode(target)}\n".encode("ascii"))
            checks.require(all(part > 0 for part in state), f"positive source N={total} {state}")
            checks.require(sum(state) == total, f"source weight N={total} {state}")
            checks.require(all(part > 0 for part in target), f"positive target N={total} {state}")
            checks.require(sum(target) == total, f"target weight N={total} {state}")
            checks.require(target in state_set, f"closure N={total} {state}")
            checks.require(
                set(internal_cuts(target)).issubset(internal_cuts(state)),
                f"cut deletion N={total} {state}",
            )

            tail, period = tail_and_period(state, successor)
            tails[state] = tail
            checks.require(period >= 1, f"positive period N={total} {state}")
            checks.require(period == 1, f"all recurrence fixed N={total} {state}")
            checks.require(tail >= 0, f"nonnegative tail N={total} {state}")
            checks.require(
                (target == state) == fixed_criterion(state),
                f"fixed criterion N={total} {state}",
            )
            if target == state:
                fixed.add(state)
            if tail == 0:
                recurrent.add(state)

        checks.require(recurrent == fixed, f"recurrent equals fixed N={total}")
        checks.require(
            len(fixed) == fixed_count_recurrence(total),
            f"fixed recurrence N={total}",
        )

        maximum_tail = max(tails.values())
        expected_maximum = max(0, total - 3)
        deepest = {state for state, tail in tails.items() if tail == maximum_tail}
        checks.require(maximum_tail == expected_maximum, f"sharp maximum tail N={total}")

        if total <= 3:
            checks.require(fixed == state_set, f"small boundary all fixed N={total}")
            checks.require(deepest == state_set, f"small boundary deepest set N={total}")
        else:
            witness = (1, 2) + (1,) * (total - 3)
            checks.require(witness in state_set, f"witness closure N={total}")
            checks.require(tails[witness] == total - 3, f"witness tail N={total}")
            checks.require(deepest == {witness}, f"unique deepest N={total}")
            orbit_state = witness
            for time in range(total - 2):
                checks.require(
                    orbit_state == witness_at_time(total, time),
                    f"witness trajectory N={total} t={time}",
                )
                if time < total - 3:
                    orbit_state = successor[orbit_state]
            checks.require(successor[orbit_state] == orbit_state, f"witness endpoint fixed N={total}")

        formula_image: set[Composition] = set()
        global_fibre_mass = 0
        factorized_fibre_mass = 0
        fibre_maximum = 0
        for target in states:
            actual = indegree.get(target, 0)
            global_count = global_no_skip_fibre(total, target)
            product_count = factorized_fibre(total, target)
            checks.require(global_count == actual, f"global fibre DP N={total} {target}")
            checks.require(product_count == global_count, f"factorized fibre N={total} {target}")
            checks.require(
                (global_count > 0) == (target in image),
                f"pointwise image criterion N={total} {target}",
            )
            if global_count:
                formula_image.add(target)
            global_fibre_mass += global_count
            factorized_fibre_mass += product_count
            fibre_maximum = max(fibre_maximum, actual)

        checks.require(formula_image == image, f"image equality N={total}")
        checks.require(sum(indegree.values()) == len(states), f"true fibre mass N={total}")
        checks.require(global_fibre_mass == len(states), f"global DP fibre mass N={total}")
        checks.require(factorized_fibre_mass == len(states), f"factor fibre mass N={total}")

        rows.append(
            f"N={total:02d} states={len(states)} fixed={len(fixed)} "
            f"image={len(image)} max_tail={maximum_tail} "
            f"deepest={len(deepest)} fibre_max={fibre_maximum}"
        )

    print("P191 prefix-divisibility-cut verifier")
    print(f"range=N=1..{MAX_N}")
    print("\n".join(rows))
    print(f"transitions={transition_count}")
    print(f"assertions={checks.count}")
    print(f"transition_digest={digest.hexdigest()}")
    print("status=PASS")


if __name__ == "__main__":
    main()
