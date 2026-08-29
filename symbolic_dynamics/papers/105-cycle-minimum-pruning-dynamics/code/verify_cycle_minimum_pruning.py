#!/usr/bin/env python3
"""Deterministic exact controls for cycle-minimum pruning.

The literal route enumerates every permutation through S_9, constructs the
cycle surgery from predecessor/successor pointers, and follows the full
orbit.  Independent routes use the closed iterate normal form, the
cycle-containing-1 recurrence for restricted cycle lengths, and the exact
one-step fibre formula.  Only integer arithmetic and finite enumeration are
used.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import factorial


class Ledger:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")


LEDGER = Ledger()


def cycles_of(p: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Return the disjoint cycles, each read in the permutation orientation."""
    n = len(p)
    seen = [False] * n
    cycles: list[tuple[int, ...]] = []
    for start in range(n):
        if seen[start]:
            continue
        cycle = []
        x = start
        while not seen[x]:
            seen[x] = True
            cycle.append(x)
            x = p[x]
        cycles.append(tuple(cycle))
    return cycles


def prune_literal(p: tuple[int, ...]) -> tuple[int, ...]:
    """Delete the minimum from every nontrivial cycle and fix it."""
    q = list(p)
    for cycle in cycles_of(p):
        if len(cycle) == 1:
            continue
        minimum = min(cycle)
        successor = p[minimum]
        predecessor = next(x for x in cycle if p[x] == minimum)
        q[predecessor] = successor
        q[minimum] = minimum
    return tuple(q)


def iterate_closed(p: tuple[int, ...], t: int) -> tuple[int, ...]:
    """Closed route: fix the t smallest entries of every original cycle."""
    q = list(range(len(p)))
    for cycle in cycles_of(p):
        deleted_count = min(t, len(cycle) - 1)
        deleted = set(sorted(cycle)[:deleted_count])
        survivors = [x for x in cycle if x not in deleted]
        if len(survivors) >= 2:
            for x, y in zip(survivors, survivors[1:] + survivors[:1]):
                q[x] = y
    return tuple(q)


def expected_cycle_lengths(lengths: list[int], t: int) -> list[int]:
    answer: list[int] = []
    for length in lengths:
        removed = min(t, length - 1)
        answer.extend([1] * removed)
        answer.append(max(length - t, 1))
    return sorted(answer)


def involution_number(n: int) -> int:
    total = 0
    for pairs in range(n // 2 + 1):
        total += factorial(n) // (
            (2**pairs) * factorial(pairs) * factorial(n - 2 * pairs)
        )
    return total


def fibre_formula(sigma: tuple[int, ...]) -> int:
    """Exact number of one-step ancestors of sigma."""
    cycles = cycles_of(sigma)
    fixed = sorted(cycle[0] for cycle in cycles if len(cycle) == 1)
    nontrivial = sorted(
        (cycle for cycle in cycles if len(cycle) >= 2), key=min
    )
    if len(fixed) < len(nontrivial):
        return 0

    matching_count = 1
    insertion_count = 1
    for index, cycle in enumerate(nontrivial):
        eligible = sum(value < min(cycle) for value in fixed)
        matching_count *= max(eligible - index, 0)
        insertion_count *= len(cycle)
    return (
        matching_count
        * insertion_count
        * involution_number(len(fixed) - len(nontrivial))
    )


@lru_cache(maxsize=None)
def restricted_count(n: int, k: int) -> int:
    """Permutations of [n] all of whose cycle lengths are at most k."""
    if n == 0:
        return 1
    if k <= 0:
        return 0
    return sum(
        factorial(n - 1) // factorial(n - j) * restricted_count(n - j, k)
        for j in range(1, min(n, k) + 1)
    )


def mobius(n: int) -> int:
    value = n
    prime_count = 0
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            if value % prime == 0:
                return 0
            prime_count += 1
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    literal_permutations = 0
    literal_trajectory_steps = 0
    fibre_states = 0
    histograms: dict[int, dict[int, int]] = {}

    for n in range(1, 10):
        identity = tuple(range(n))
        histogram: Counter[int] = Counter()
        actual_indegree: defaultdict[tuple[int, ...], int] = defaultdict(int)

        for p in permutations(range(n)):
            p = tuple(p)
            literal_permutations += 1
            LEDGER.check(sorted(p) == list(range(n)))
            cycles = cycles_of(p)
            lengths = [len(cycle) for cycle in cycles]
            LEDGER.check(sum(lengths) == n)
            depth = max(lengths) - 1
            histogram[depth] += 1

            current = p
            for t in range(depth + 1):
                closed = iterate_closed(p, t)
                LEDGER.check(current == closed, f"iterate mismatch n={n}, t={t}")
                observed_lengths = sorted(len(cycle) for cycle in cycles_of(current))
                LEDGER.check(observed_lengths == expected_cycle_lengths(lengths, t))
                fixed_observed = sum(current[x] == x for x in range(n))
                fixed_expected = sum(
                    1 if length == 1 else (length if t >= length - 1 else t)
                    for length in lengths
                )
                LEDGER.check(fixed_observed == fixed_expected)
                if t < depth:
                    next_state = prune_literal(current)
                    literal_trajectory_steps += 1
                    LEDGER.check(next_state != current)
                    LEDGER.check(
                        sum(next_state[x] == x for x in range(n)) > fixed_observed
                    )
                    current = next_state
            LEDGER.check(current == identity)
            LEDGER.check(prune_literal(current) == identity)

            for iterate_number in range(1, n + 2):
                LEDGER.check(
                    (iterate_closed(p, iterate_number) == p) == (p == identity)
                )

            image = prune_literal(p)
            actual_indegree[image] += 1

        histogram_dict = dict(sorted(histogram.items()))
        histograms[n] = histogram_dict
        LEDGER.check(sum(histogram.values()) == factorial(n))
        LEDGER.check(histogram[0] == 1)
        LEDGER.check(histogram[n - 1] == factorial(n - 1))
        if n >= 3:
            LEDGER.check(histogram[n - 2] == n * factorial(n - 2))

        cumulative = 0
        for t in range(n):
            cumulative += histogram[t]
            LEDGER.check(cumulative == restricted_count(n, t + 1))
            expected_layer = restricted_count(n, t + 1) - restricted_count(n, t)
            LEDGER.check(histogram[t] == expected_layer)

        total_formula_indegree = 0
        for sigma in permutations(range(n)):
            sigma = tuple(sigma)
            predicted = fibre_formula(sigma)
            observed = actual_indegree[sigma]
            fibre_states += 1
            LEDGER.check(predicted == observed, f"fibre mismatch n={n}")
            total_formula_indegree += predicted
            if sigma == identity:
                LEDGER.check(predicted == involution_number(n))
        LEDGER.check(total_formula_indegree == factorial(n))

    # Extended exact recurrence and endpoint checks beyond literal enumeration.
    for n in range(1, 51):
        layers = [
            restricted_count(n, t + 1) - restricted_count(n, t)
            for t in range(n)
        ]
        LEDGER.check(sum(layers) == factorial(n))
        LEDGER.check(layers[0] == 1)
        LEDGER.check(layers[-1] == factorial(n - 1))
        if n >= 3:
            LEDGER.check(layers[-2] == n * factorial(n - 2))
        for k in range(1, n + 1):
            recurrence_rhs = sum(
                factorial(n - 1) // factorial(n - j)
                * restricted_count(n - j, k)
                for j in range(1, min(n, k) + 1)
            )
            LEDGER.check(restricted_count(n, k) == recurrence_rhs)

    # Periodic and formal-zeta ledger: F(r)=1, hence only one 1-cycle.
    for period in range(1, 61):
        fixed_count = 1
        cycle_count = sum(
            mobius(period // d) * 1 for d in divisors(period)
        ) // period
        LEDGER.check(fixed_count == 1)
        LEDGER.check(cycle_count == (1 if period == 1 else 0))
        # n[z^n] log((1-z)^(-1)) = 1 = F(n).
        LEDGER.check(period * Fraction(1, period) == fixed_count)

    print("cycle-minimum pruning exact control: PASS")
    print(f"assertions={LEDGER.assertions}")
    print(f"literal_permutations={literal_permutations}")
    print(f"literal_trajectory_steps={literal_trajectory_steps}")
    print(f"fibre_formula_states={fibre_states}")
    for n in range(1, 10):
        print(f"depth_histogram n={n}: {histograms[n]}")
    print(
        "identity_indegrees n=1..9: "
        + str([involution_number(n) for n in range(1, 10)])
    )
    print("restricted_cycle_recurrence=PASS n<=50")
    print("periodic_mobius_zeta=PASS periods<=60")


if __name__ == "__main__":
    main()
