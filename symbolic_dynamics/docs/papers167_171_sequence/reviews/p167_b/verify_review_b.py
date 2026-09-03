#!/usr/bin/env python3
"""Reviewer-owned exact control for P167 Hostile Review B.

This standard-library program is deliberately self-contained.  It imports
neither the author verifier nor scouting code.  It reconstructs the literal
identity-default first-position map, exhausts complete carriers and all
target fibres through n=6, and attacks labelled path/cycle and species
boundaries through sizes beyond the full-carrier range.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.count += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()


def feedback(word: tuple[int, ...]) -> tuple[int, ...]:
    """First position of a present symbol; its own value when absent."""
    first: list[int | None] = [None] * len(word)
    for position, symbol in enumerate(word):
        if first[symbol] is None:
            first[symbol] = position
    return tuple(i if position is None else position
                 for i, position in enumerate(first))


def power(word: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    for _ in range(exponent):
        word = feedback(word)
    return word


def orbit_data(word: tuple[int, ...]) -> tuple[int, int]:
    first_time: dict[tuple[int, ...], int] = {}
    time = 0
    while word not in first_time:
        first_time[word] = time
        word = feedback(word)
        time += 1
    return first_time[word], time - first_time[word]


def off_diagonal_values_are_distinct(word: tuple[int, ...]) -> bool:
    values = [value for i, value in enumerate(word) if value != i]
    return len(values) == len(set(values))


def target_fibre_formula(target: tuple[int, ...]) -> int:
    """Evaluate the manuscript formula without using author code."""
    n = len(target)
    mandatory = [i for i, value in enumerate(target) if value != i]
    mandatory_positions = [target[i] for i in mandatory]
    if len(mandatory_positions) != len(set(mandatory_positions)):
        return 0

    optional = [i for i, value in enumerate(target)
                if value == i and i not in mandatory_positions]
    total = 0
    for mask in range(1 << len(optional)):
        present = mandatory + [optional[k] for k in range(len(optional))
                               if mask & (1 << k)]
        first = {i: (target[i] if i in mandatory else i) for i in present}
        forced_positions = set(first.values())
        ways = 1
        for position in range(n):
            if position not in forced_positions:
                ways *= sum(opening < position for opening in first.values())
                if ways == 0:
                    break
        total += ways
    return total


def bell_numbers(limit: int) -> list[int]:
    values = [1]
    for n in range(limit):
        values.append(sum(math.comb(n, k) * values[k]
                          for k in range(n + 1)))
    return values


def involution_numbers(limit: int) -> list[int]:
    values = [1]
    if limit:
        values.append(1)
    for n in range(2, limit + 1):
        values.append(values[n - 1] + (n - 1) * values[n - 2])
    return values


def connected_recurrent_count(size: int) -> int:
    if size <= 2:
        return 1
    if size == 3:
        return 4
    return math.factorial(size - 1) + math.factorial(size) // 4


def recurrent_numbers(limit: int) -> list[int]:
    """Labelled SET recurrence with the least label's component exposed."""
    values = [1]
    for n in range(1, limit + 1):
        values.append(sum(
            math.comb(n - 1, size - 1)
            * connected_recurrent_count(size)
            * values[n - size]
            for size in range(1, n + 1)
        ))
    return values


def exp_series(series: list[Fraction]) -> list[Fraction]:
    """Ordinary coefficients of exp(series), using (exp C)'=C'exp C."""
    out = [Fraction(0)] * len(series)
    out[0] = Fraction(1)
    for n in range(1, len(series)):
        out[n] = sum(Fraction(k) * series[k] * out[n - k]
                     for k in range(1, n + 1)) / n
    return out


def recurrent_numbers_from_displayed_egf(limit: int) -> list[int]:
    # log F = -log(1-x) + x^3/3 + x^4/(4(1-x)).
    logarithm = [Fraction(0)] * (limit + 1)
    for degree in range(1, limit + 1):
        logarithm[degree] += Fraction(1, degree)
    if limit >= 3:
        logarithm[3] += Fraction(1, 3)
    for degree in range(4, limit + 1):
        logarithm[degree] += Fraction(1, 4)
    ordinary = exp_series(logarithm)
    return [int(ordinary[n] * math.factorial(n))
            for n in range(limit + 1)]


def path_word(order: tuple[int, ...]) -> tuple[int, ...]:
    word = list(range(len(order)))
    for index in range(1, len(order)):
        word[order[index]] = order[index - 1]
    return tuple(word)


def predicted_path_step(order: tuple[int, ...]) -> tuple[int, ...]:
    if len(order) == 1:
        return path_word(order)
    components = ((tuple(reversed(order)),)
                  if order[0] > order[1]
                  else ((order[0],), tuple(reversed(order[1:]))))
    word = list(range(len(order)))
    for component in components:
        for index in range(1, len(component)):
            word[component[index]] = component[index - 1]
    return tuple(word)


def cycle_word(order: tuple[int, ...]) -> tuple[int, ...]:
    word = [0] * len(order)
    for index, vertex in enumerate(order):
        word[vertex] = order[(index + 1) % len(order)]
    return tuple(word)


def inverse_cycle_word(order: tuple[int, ...]) -> tuple[int, ...]:
    word = [0] * len(order)
    for index, vertex in enumerate(order):
        word[vertex] = order[(index - 1) % len(order)]
    return tuple(word)


def edge_digest(edges: dict[tuple[int, ...], tuple[int, ...]]) -> str:
    digest = hashlib.sha256()
    for source in sorted(edges):
        digest.update(bytes(source))
        digest.update(b">")
        digest.update(bytes(edges[source]))
        digest.update(b"\n")
    return digest.hexdigest()


def main() -> None:
    formula_limit = 16
    bells = bell_numbers(formula_limit)
    involutions = involution_numbers(formula_limit)
    recurrent = recurrent_numbers(formula_limit)
    recurrent_from_egf = recurrent_numbers_from_displayed_egf(formula_limit)
    A.equal(recurrent, recurrent_from_egf,
            "labelled recurrence versus displayed EGF")

    full_table: dict[str, object] = {}
    for n in range(1, 7):
        states = tuple(itertools.product(range(n), repeat=n))
        edges: dict[tuple[int, ...], tuple[int, ...]] = {}
        fibres: Counter[tuple[int, ...]] = Counter()
        orbit: dict[tuple[int, ...], tuple[int, int]] = {}

        for state in states:
            target = feedback(state)
            edges[state] = target
            fibres[target] += 1
            A.check(off_diagonal_values_are_distinct(target),
                    f"first-image injection n={n}")
            orbit[state] = orbit_data(state)
            tail, period = orbit[state]
            A.check(period in (1, 2), f"global terminal period n={n}")
            for exponent in range(1, 5):
                expected_fixed = (tail == 0 and
                                  (period == 1 or exponent % 2 == 0))
                A.equal(power(state, exponent) == state, expected_fixed,
                        f"pointwise iterate test n={n}, k={exponent}")

        formula_maximum = 0
        supported = 0
        off_diagonal_candidates = 0
        unsupported_candidates = 0
        for target in states:
            brute = fibres.get(target, 0)
            formula = target_fibre_formula(target)
            A.equal(formula, brute, f"every-target fibre n={n}")
            formula_maximum = max(formula_maximum, formula)
            supported += formula > 0
            if off_diagonal_values_are_distinct(target):
                off_diagonal_candidates += 1
                unsupported_candidates += formula == 0

        fixed = sum(edges[state] == state for state in states)
        recurrent_count = sum(tail == 0 for tail, _ in orbit.values())
        full_height = max(tail for tail, _ in orbit.values())
        image_height = max(orbit_data(target)[0] for target in fibres)
        periods = Counter(period for tail, period in orbit.values() if tail == 0)

        A.equal(len(fibres), supported, f"formula support equals image n={n}")
        A.equal(recurrent_count, recurrent[n], f"recurrent count n={n}")
        A.equal(fixed, involutions[n], f"involution fixed count n={n}")
        A.equal(periods[1], involutions[n], f"period-one point count n={n}")
        A.equal(periods[2], recurrent[n] - involutions[n],
                f"period-two point count n={n}")
        A.equal(full_height, 0 if n == 1 else 2 * n - 2,
                f"full sharp height n={n}")
        A.equal(image_height, 0 if n == 1 else 2 * n - 3,
                f"image sharp height n={n}")
        A.equal(formula_maximum, bells[n], f"Bell maximum n={n}")
        A.equal(target_fibre_formula(tuple(range(n))), bells[n],
                f"identity Bell fibre n={n}")

        if n >= 2:
            witness = tuple(range(1, n)) + (1,)
            increasing_path = path_word(tuple(range(n)))
            excluded_path = path_word(tuple(reversed(range(n))))
            A.equal(feedback(witness), increasing_path,
                    f"displayed witness image n={n}")
            A.equal(orbit_data(witness)[0], 2 * n - 2,
                    f"displayed full-height witness n={n}")
            A.equal(orbit_data(increasing_path)[0], 2 * n - 3,
                    f"displayed image-height witness n={n}")
            A.equal(fibres.get(excluded_path, 0), 0,
                    f"decreasing path excluded from image n={n}")

        fibre_histogram = Counter(fibres.values()) if n <= 3 else None
        full_table[str(n)] = {
            "states": len(states),
            "image": len(fibres),
            "recurrent": recurrent_count,
            "fixed": fixed,
            "two_orbits": (recurrent_count - fixed) // 2,
            "full_height": full_height,
            "image_height": image_height,
            "maximum_fibre": formula_maximum,
            "off_diagonal_candidates": off_diagonal_candidates,
            "unsupported_candidates": unsupported_candidates,
            "fibre_histogram": (dict(sorted(fibre_histogram.items()))
                                if fibre_histogram is not None else None),
            "edge_sha256": edge_digest(edges),
        }

    component_table: dict[str, object] = {}
    for size in range(1, 10):
        recurrent_paths = 0
        maximum_tail = -1
        maximizers: list[tuple[int, ...]] = []
        for order in itertools.permutations(range(size)):
            word = path_word(order)
            A.equal(feedback(word), predicted_path_step(order),
                    f"literal path step s={size}")
            tail, period = orbit_data(word)
            endpoint_test = (size == 1 or
                             (order[0] > order[1]
                              and order[-1] > order[-2]))
            A.equal(tail == 0, endpoint_test,
                    f"path recurrence endpoints s={size}")
            A.check(period in (1, 2), f"path terminal period s={size}")
            recurrent_paths += tail == 0
            if tail > maximum_tail:
                maximum_tail = tail
                maximizers = [order]
            elif tail == maximum_tail:
                maximizers.append(order)

        expected_paths = (1 if size == 1 else 0 if size == 2 else
                          2 if size == 3 else math.factorial(size) // 4)
        A.equal(recurrent_paths, expected_paths,
                f"recurrent path census s={size}")
        A.equal(maximum_tail, 0 if size == 1 else 2 * size - 2,
                f"path sharp height s={size}")
        expected_maximizers = ([(0,)] if size == 1 else
                               [tuple(reversed(range(size)))])
        A.equal(maximizers, expected_maximizers,
                f"unique decreasing path maximizer s={size}")

        cycles = 0
        if size >= 2:
            for rest in itertools.permutations(range(1, size)):
                order = (0,) + rest
                word = cycle_word(order)
                A.equal(feedback(word), inverse_cycle_word(order),
                        f"cycle inversion s={size}")
                A.equal(orbit_data(word), (0, 1 if size == 2 else 2),
                        f"cycle dynamical period s={size}")
                cycles += 1
            A.equal(cycles, math.factorial(size - 1),
                    f"directed cycle census s={size}")

        connected = 1 if size == 1 else cycles + recurrent_paths
        A.equal(connected, connected_recurrent_count(size),
                f"connected recurrent census s={size}")
        component_table[str(size)] = {
            "cycles": cycles,
            "recurrent_paths": recurrent_paths,
            "connected_recurrent": connected,
            "maximum_path_tail": maximum_tail,
            "maximum_path_orders": len(maximizers),
        }

    result = {
        "decision": "REVIEW_B_INDEPENDENT_CONTROL_PASS",
        "external_status": "HOLD_EXTERNAL",
        "assertions": A.count,
        "scope": {
            "complete_carriers_and_every_target_fibres": "n=1..6",
            "literal_paths_and_cycles": "sizes 1..9",
            "recurrent_egf": "orders 0..16",
            "positive_iterates": "k=1..4 pointwise",
        },
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "full_graph_n_1_to_6": full_table,
        "path_component_s_1_to_9": component_table,
        "formula_prefixes": {
            "recurrent_R_0_to_16": recurrent,
            "involutions_I_0_to_16": involutions,
            "Bell_B_0_to_16": bells,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True, separators=(",", ": ")))


if __name__ == "__main__":
    main()
