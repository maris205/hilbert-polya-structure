#!/usr/bin/env python3
"""Independent control for the cross-colon basin theorem.

This verifier does not import the earlier C6 verifier.  On small rectangles it
builds the crossed-colon map from literal monomial multiplication and colon
operations, follows every orbit, and compares its attractor with the first
occupied diagonal.  Independently, it counts staircase boundary paths by a
four-mask contact transfer and compares those counts with the literal basins.
Larger rectangles test the transfer identities without enumerating ideals.
"""

from collections import Counter
from itertools import combinations_with_replacement
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def staircase_states(a, b):
    for increasing in combinations_with_replacement(range(b + 1), a):
        yield tuple(reversed(increasing))


def staircase_mask(h, a, b):
    result = 0
    for i in range(a):
        for j in range(h[i], b):
            result |= 1 << (i * b + j)
    return result


def multiply(mask, a, b, di, dj):
    result = 0
    for i in range(a):
        for j in range(b):
            if mask & (1 << (i * b + j)):
                if i + di < a and j + dj < b:
                    result |= 1 << ((i + di) * b + j + dj)
    return result


def colon(mask, a, b, di, dj):
    result = 0
    for i in range(a):
        for j in range(b):
            ni, nj = i + di, j + dj
            if ni >= a or nj >= b or mask & (1 << (ni * b + nj)):
                result |= 1 << (i * b + j)
    return result


def cross_colon_step(mask, a, b):
    first = multiply(colon(mask, a, b, 0, 1), a, b, 1, 0)
    second = multiply(colon(mask, a, b, 1, 0), a, b, 0, 1)
    return first | second


def degree_cut(a, b, r):
    result = 0
    for i in range(a):
        for j in range(b):
            if i + j >= r:
                result |= 1 << (i * b + j)
    return result


def checker_cut(a, b, r, parity):
    result = 0
    for i in range(a):
        for j in range(b):
            if i + j > r or (i + j == r and i % 2 == parity):
                result |= 1 << (i * b + j)
    return result


def attractor(start, transition):
    seen = {}
    path = []
    state = start
    while state not in seen:
        seen[state] = len(path)
        path.append(state)
        state = transition[state]
    return frozenset(path[seen[state] :])


def first_degree_and_mask(mask, a, b):
    occupied = [
        (i + j, i)
        for i in range(a)
        for j in range(b)
        if mask & (1 << (i * b + j))
    ]
    if not occupied:
        return None, 0
    r = min(degree for degree, _ in occupied)
    parity_mask = 0
    for degree, i in occupied:
        if degree == r:
            parity_mask |= 1 << (i % 2)
    return r, parity_mask


def predicted_attractor_label(mask, a, b):
    m = min(a, b)
    r, parity_mask = first_degree_and_mask(mask, a, b)
    if m == 1:
        return ("P", 1), r, parity_mask
    if r is None or r >= m:
        return ("P", m), r, parity_mask
    if r == 0:
        return ("P", 1), r, parity_mask
    if parity_mask == 3:
        return ("P", r), r, parity_mask
    check(parity_mask in (1, 2), (a, b, mask, r, parity_mask))
    return ("C", r), r, parity_mask


def contact_transfer(a, b, r):
    """Count boundary paths by parity mask of contacts with i+j=r.

    Mask 0 means no contact, 1 only even i, 2 only odd i, and 3 both.
    The routine is used only for 1 <= r < min(a,b), so neither endpoint is
    on the barrier.
    """
    check(1 <= r < min(a, b), (a, b, r))
    table = [[[0, 0, 0, 0] for _ in range(b + 1)] for _ in range(a + 1)]
    table[0][b][0] = 1
    for j in range(b, -1, -1):
        for i in range(a + 1):
            if (i, j) == (0, b) or i + j < r:
                continue
            incoming = [0, 0, 0, 0]
            if i > 0:
                for mask in range(4):
                    incoming[mask] += table[i - 1][j][mask]
            if j < b:
                for mask in range(4):
                    incoming[mask] += table[i][j + 1][mask]
            if i + j == r:
                bit = 1 << (i % 2)
                for mask, value in enumerate(incoming):
                    table[i][j][mask | bit] += value
            else:
                table[i][j] = incoming
    return tuple(table[a][0])


def predicted_basin_counts(a, b):
    m = min(a, b)
    total = comb(a + b, a)
    if m == 1:
        return {("P", 1): total}, {}

    orbit_counts = {("P", 1): 2}
    phase_counts = {}
    for r in range(1, m):
        no_contact, even, odd, mixed = contact_transfer(a, b, r)
        phase_counts[r] = (even, odd, mixed)
        orbit_counts[("C", r)] = even + odd
        if r >= 2:
            orbit_counts[("P", r)] = mixed
        else:
            check(mixed == 1, (a, b, r, mixed))
        check(no_contact == comb(a + b, a) - comb(a + b, r),
              (a, b, r, no_contact))
        check(even + odd + mixed == comb(a + b, r) - comb(a + b, r - 1),
              (a, b, r, even, odd, mixed))

    orbit_counts[("P", m)] = total - comb(a + b, m - 1)
    check(sum(orbit_counts.values()) == total, (a, b, orbit_counts, total))
    return orbit_counts, phase_counts


def check_small_rectangles():
    boxes = 0
    ideals = 0
    phase_hist = Counter()
    for a in range(1, 9):
        for b in range(1, 9):
            boxes += 1
            m = min(a, b)
            masks = tuple(staircase_mask(h, a, b) for h in staircase_states(a, b))
            mask_set = set(masks)
            transition = {mask: cross_colon_step(mask, a, b) for mask in masks}
            for image in transition.values():
                check(image in mask_set, (a, b, "closure", image))

            attractor_labels = {}
            for r in range(1, m + 1):
                attractor_labels[frozenset((degree_cut(a, b, r),))] = ("P", r)
            for r in range(1, m):
                orbit = frozenset(
                    (checker_cut(a, b, r, 0), checker_cut(a, b, r, 1))
                )
                attractor_labels[orbit] = ("C", r)

            actual_counts = Counter()
            trace_counts = {r: Counter() for r in range(1, m)}
            burn = 2 * (a + b) + 5
            for mask in masks:
                ideals += 1
                predicted, first_degree, parity_mask = predicted_attractor_label(mask, a, b)
                cycle = attractor(mask, transition)
                check(cycle in attractor_labels, (a, b, mask, cycle))
                actual = attractor_labels[cycle]
                check(actual == predicted,
                      (a, b, mask, first_degree, parity_mask, actual, predicted))
                actual_counts[actual] += 1

                if first_degree is not None and 1 <= first_degree < m:
                    trace_counts[first_degree][parity_mask] += 1

                state = mask
                for _ in range(burn):
                    state = transition[state]
                if predicted[0] == "P":
                    check(state == degree_cut(a, b, predicted[1]),
                          (a, b, mask, "fixed phase", predicted))
                else:
                    initial_parity = 0 if parity_mask == 1 else 1
                    expected = checker_cut(
                        a, b, predicted[1], (initial_parity + burn) % 2
                    )
                    check(state == expected,
                          (a, b, mask, "checker phase", predicted, parity_mask))

            expected_counts, transfer_phases = predicted_basin_counts(a, b)
            check(dict(actual_counts) == expected_counts,
                  (a, b, dict(actual_counts), expected_counts))
            for r, (even, odd, mixed) in transfer_phases.items():
                expected_trace = {1: even, 2: odd, 3: mixed}
                check(dict(trace_counts[r]) == {k: v for k, v in expected_trace.items() if v},
                      (a, b, r, dict(trace_counts[r]), expected_trace))
                phase_hist[(r, "even")] += even
                phase_hist[(r, "odd")] += odd
                phase_hist[(r, "mixed")] += mixed
    return boxes, ideals, phase_hist


def check_large_transfer_grid():
    triples = 0
    for a in range(1, 31):
        for b in range(1, 31):
            m = min(a, b)
            total = comb(a + b, a)
            if m == 1:
                counts, phases = predicted_basin_counts(a, b)
                check(counts == {("P", 1): total} and phases == {}, (a, b, counts))
                continue
            counts, phases = predicted_basin_counts(a, b)
            check(sum(counts.values()) == total, (a, b, counts))
            check(counts[("P", m)] == total - comb(a + b, m - 1),
                  (a, b, counts[("P", m)]))
            for r, (even, odd, mixed) in phases.items():
                triples += 1
                swapped = contact_transfer(b, a, r)
                if r % 2 == 0:
                    check((even, odd, mixed) == (swapped[1], swapped[2], swapped[3]),
                          (a, b, r, "swap-even"))
                else:
                    check((even, odd, mixed) == (swapped[2], swapped[1], swapped[3]),
                          (a, b, r, "swap-odd"))
    return triples


def main():
    boxes, ideals, phase_hist = check_small_rectangles()
    transfer_triples = check_large_transfer_grid()
    example_counts, example_phases = predicted_basin_counts(5, 7)
    ordered_counts = sorted(example_counts.items())
    ordered_phases = sorted(example_phases.items())

    print("cross-colon basin transfer independent control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_rectangles={boxes}; parameter_grid=a,b=1..8; ideals={ideals}")
    print("literal_attractors_vs_first_trace=PASS")
    print("contact_transfer_vs_exhaustive_basins=PASS")
    print("ballot_partition_and_swap_identities=PASS")
    print(f"large_transfer_grid=a,b=1..30; nontrivial_triples={transfer_triples}")
    print("example_a5_b7_orbit_basins=" + repr(ordered_counts))
    print("example_a5_b7_trace_phases=" + repr(ordered_phases))


if __name__ == "__main__":
    main()
