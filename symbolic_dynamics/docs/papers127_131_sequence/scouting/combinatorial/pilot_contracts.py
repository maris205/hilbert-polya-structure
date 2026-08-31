#!/usr/bin/env python3
"""Exact theorem-contract pilots for the two surviving breadth candidates.

The first half verifies closed formulas for the frontier-parity boundary wave
on J([2] x [m]).  The second independently reconstructs the fibres of
crossing-component planarisation of chord matchings.  These computations are
finite falsification controls; the accompanying scouting report separates
them from the all-size proofs.
"""

from __future__ import annotations

from collections import Counter
from math import comb

from pilot_breadth import (
    chord_matchings,
    chords_cross,
    component_normalize,
    frontier_boundary_wave,
    grid_poset,
    ideals_of_poset,
    relation_components,
)


class Checks:
    def __init__(self):
        self.n = 0

    def that(self, condition, payload=None):
        self.n += 1
        if not condition:
            raise AssertionError(payload)


def triangular_states(m):
    return tuple((a, b) for a in range(m + 1) for b in range(a + 1))


def coordinate_wave(m, state):
    """The literal frontier-parity wave in row-length coordinates."""
    a, b = state
    if a == b == 0:
        return (1, 0)
    if b == 0:
        return (a - 1, 0)
    if a == b:
        return (a, a - 1)
    if a < m:
        return (a + 1, b + 1)
    return (m, b + 1)


def ideal_coordinates(mask, m):
    return (
        sum((mask >> j) & 1 for j in range(m)),
        sum((mask >> (m + j)) & 1 for j in range(m)),
    )


def recurrent_states(m):
    if m == 1:
        return {(0, 0), (1, 0)}
    return {(0, 0), (1, 0), (m, m - 1), (m, m)}


def predicted_depth(m, state):
    a, b = state
    if state in recurrent_states(m):
        return 0
    if b == 0:
        return a - 1
    if a == b:
        if a == 1:
            return 1
        return m - a + 1
    return m - b - 1


def run_po2():
    checks = Checks()

    # The coordinate rule is first checked against the literal order-ideal
    # definition, rather than assumed by the large-parameter control.
    literal_states = 0
    for m in range(1, 9):
        below = grid_poset(2, m)
        phi = frontier_boundary_wave(below)
        for ideal in ideals_of_poset(below):
            literal_states += 1
            state = ideal_coordinates(ideal, m)
            checks.that(0 <= state[1] <= state[0] <= m, (m, ideal, state))
            checks.that(
                ideal_coordinates(phi(ideal), m) == coordinate_wave(m, state),
                (m, ideal, state, ideal_coordinates(phi(ideal), m)),
            )

    # Formula stress test.  Checking that every positive depth falls by one
    # and every zero-depth state stays in the prescribed recurrent set is an
    # exact certificate of the pointwise clock once closure is also checked.
    tested_states = 0
    for m in range(1, 251):
        states = triangular_states(m)
        universe = set(states)
        recurrent = recurrent_states(m)
        layers = Counter()
        predecessors = Counter()
        for state in states:
            tested_states += 1
            image = coordinate_wave(m, state)
            checks.that(image in universe, (m, state, image, "closure"))
            depth = predicted_depth(m, state)
            checks.that(depth >= 0, (m, state, depth))
            layers[depth] += 1
            predecessors[image] += 1
            if depth == 0:
                checks.that(state in recurrent and image in recurrent,
                            (m, state, image, "recurrent"))
            else:
                checks.that(predicted_depth(m, image) == depth - 1,
                            (m, state, image, depth))

        checks.that(sum(layers.values()) == (m + 1) * (m + 2) // 2,
                    (m, layers))
        checks.that(set(state for state in states if predicted_depth(m, state) == 0)
                    == recurrent, (m, layers, recurrent))
        if m == 1:
            checks.that(layers == Counter({0: 2, 1: 1}), layers)
        elif m == 2:
            checks.that(layers == Counter({0: 4, 1: 2}), layers)
        else:
            expected = Counter({0: 4, 1: 4, m - 1: 2})
            if m == 3:
                expected[1] = 4
            for depth in range(2, m - 1):
                expected[depth] = depth + 3
            checks.that(layers == expected, (m, layers, expected))
            indegrees = Counter(predecessors.get(state, 0) for state in states)
            expected_indegrees = Counter({
                0: 2 * m - 2,
                1: (m * m - 5 * m + 14) // 2,
                2: 2 * m - 6,
                3: 2,
            })
            # Counter suppresses zero entries, notably the m=3 indegree-2 bin.
            expected_indegrees += Counter()
            checks.that(indegrees == expected_indegrees,
                        (m, indegrees, expected_indegrees))
            checks.that(len(predecessors) == (m * m - m + 6) // 2,
                        (m, len(predecessors)))
            checks.that(max(layers) == m - 1, (m, max(layers)))
            witnesses = {state for state in states
                         if predicted_depth(m, state) == m - 1}
            checks.that(witnesses == {(m, 0), (2, 2)}, (m, witnesses))

    print(
        "PO2_CONTRACT | literal_m<=8 | formula_m<=250 | "
        f"literal_states={literal_states} | tested_states={tested_states} | "
        "cycles=two_2cycles(m>=2) | sharp_depth=m-1(m>=3) | "
        "max_indegree=3 | assertions=" + str(checks.n)
    )
    return checks.n


def noncrossing(matching):
    return not any(
        chords_cross(matching[i], matching[j])
        for i in range(len(matching))
        for j in range(i + 1, len(matching))
    )


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def connected_chord_counts(max_n):
    counts = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        counts[n] = sum(
            len(relation_components(matching, chords_cross)) == 1
            for matching in chord_matchings(n)
        )
    return counts


def coefficient_power(coefficients, power, degree):
    out = [0] * (degree + 1)
    out[0] = 1
    for _ in range(power):
        nxt = [0] * (degree + 1)
        for i, left in enumerate(out):
            if not left:
                continue
            for j, right in enumerate(coefficients):
                if i + j > degree:
                    break
                nxt[i + j] += left * right
        out = nxt
    return out[degree]


def free_component_transform(connected):
    """Coefficients of A(z)=1+C(z A(z)), computed triangularly."""
    max_n = len(connected) - 1
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        a[n] = sum(
            connected[k] * coefficient_power(a, k, n - k)
            for k in range(1, n + 1)
        )
    return a


def child_counts(matching):
    """Numbers of immediate child chords, including the virtual root."""
    parents = []
    for i, (a, b) in enumerate(matching):
        containers = [
            (d - c, j)
            for j, (c, d) in enumerate(matching)
            if c < a < b < d
        ]
        parents.append(min(containers)[1] if containers else -1)
    counts = Counter(parents)
    return (counts.get(-1, 0),) + tuple(counts.get(i, 0)
                                        for i in range(len(matching)))


def run_mt2():
    checks = Checks()
    max_n = 7
    connected = connected_chord_counts(max_n)
    free = free_component_transform(connected)
    total_sources = 0
    total_targets = 0
    maximum_fibres = []

    for n in range(1, max_n + 1):
        states = chord_matchings(n)
        fibres = Counter()
        for matching in states:
            total_sources += 1
            image = component_normalize(matching, chords_cross, False)
            checks.that(noncrossing(image), (n, matching, image, "image"))
            checks.that(component_normalize(image, chords_cross, False) == image,
                        (n, image, "idempotence"))
            fibres[image] += 1

        targets = tuple(matching for matching in states if noncrossing(matching))
        total_targets += len(targets)
        checks.that(len(targets) == catalan(n), (n, len(targets), catalan(n)))
        checks.that(set(fibres) == set(targets), (n, "image equality"))
        for target in targets:
            predicted = 1
            for number_of_children in child_counts(target):
                predicted *= free[number_of_children]
            checks.that(fibres[target] == predicted,
                        (n, target, fibres[target], predicted, child_counts(target)))

        adjacent = tuple((2 * i, 2 * i + 1) for i in range(n))
        rainbow = tuple((i, 2 * n - 1 - i) for i in range(n))
        checks.that(fibres[adjacent] == free[n],
                    (n, fibres[adjacent], free[n]))
        checks.that(fibres[rainbow] == 1, (n, fibres[rainbow]))
        maximum = max(fibres.values())
        maximum_fibres.append(maximum)
        checks.that(maximum == free[n], (n, maximum, free[n]))
        checks.that(sum(value == maximum for value in fibres.values()) == 1,
                    (n, maximum, "unique pilot maximizer"))
        checks.that(sum(fibres.values()) == len(states), (n, sum(fibres.values())))

    print(
        "MT2_CONTRACT | chord_matchings_n<=7 | "
        f"sources={total_sources} | noncrossing_targets={total_targets} | "
        "connected=" + ",".join(map(str, connected[1:])) + " | "
        "free=" + ",".join(map(str, free)) + " | "
        "pilot_max=" + ",".join(map(str, maximum_fibres)) + " | "
        f"assertions={checks.n}"
    )
    return checks.n


def main():
    print("P127-P131 combinatorial theorem-contract exact pilots")
    po2 = run_po2()
    mt2 = run_mt2()
    print(f"TOTAL | assertions={po2 + mt2}")
    print("status: exact controls passed; all-size proof and owner subtraction live in SCOUT.md")


if __name__ == "__main__":
    main()
