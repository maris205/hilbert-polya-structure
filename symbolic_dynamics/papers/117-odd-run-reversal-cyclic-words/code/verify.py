#!/usr/bin/env python3
"""Exact control for parallel reversal of odd cyclic binary runs."""

from collections import Counter
from math import comb


def bits(mask, n):
    return [(mask >> i) & 1 for i in range(n)]


def boundary_positions(mask, n):
    word = bits(mask, n)
    return [i for i in range(n) if word[i] != word[i - 1]]


def run_lengths(mask, n):
    boundaries = boundary_positions(mask, n)
    if not boundaries:
        return [n]
    return [
        (boundaries[(i + 1) % len(boundaries)] - boundaries[i]) % n
        for i in range(len(boundaries))
    ]


def update(mask, n):
    word = bits(mask, n)
    boundaries = boundary_positions(mask, n)
    if not boundaries:
        return mask ^ ((1 << n) - 1) if n & 1 else mask
    flip = [0] * n
    for index, start in enumerate(boundaries):
        length = (boundaries[(index + 1) % len(boundaries)] - start) % n
        if length & 1:
            for offset in range(length):
                flip[(start + offset) % n] = 1
    return sum((word[i] ^ flip[i]) << i for i in range(n))


def orbit_data(mask, n):
    seen = {}
    time = 0
    while mask not in seen:
        seen[mask] = time
        mask = update(mask, n)
        time += 1
    return seen[mask], time - seen[mask]


def recurrent_counts(n):
    if n & 1:
        return 0, 2
    half = n // 2
    fixed = (1 << (half + 1)) - 2
    period_two = 0
    for runs in range(2, n + 1, 2):
        boundary_sets = n * comb((n + runs) // 2 - 1, runs - 1) // runs
        period_two += 2 * boundary_sets
    return fixed, period_two


def sharp_depth(n):
    return (n - 1) // 2 if n & 1 else (n - 2) // 4


def mask_from_runs(lengths):
    mask = 0
    position = 0
    colour = 0
    for length in lengths:
        for _ in range(length):
            mask |= colour << position
            position += 1
        colour ^= 1
    return mask


def extremal_witness(n):
    if n & 1:
        return mask_from_runs([1] * (n - 2) + [2]) if n > 1 else 0
    if n < 6:
        return 0
    k = n // 4
    if n % 4 == 2:
        ones = 2 * k - 1
        return mask_from_runs([1] * ones + [2] + [1] * ones + [2])
    ones = 2 * k - 3
    return mask_from_runs([1] * ones + [2] + [1] * ones + [4])


def predicted_boundaries(mask, n):
    """Old boundaries surviving the run-parity rule, in site order."""
    boundaries = boundary_positions(mask, n)
    if not boundaries:
        return []
    lengths = [
        (boundaries[(i + 1) % len(boundaries)] - boundaries[i]) % n
        for i in range(len(boundaries))
    ]
    return [
        boundaries[i]
        for i in range(len(boundaries))
        if (lengths[i - 1] - lengths[i]) % 2 == 0
    ]


def erode(q):
    if not q:
        return []
    return [q[i] for i in range(len(q)) if q[i - 1] == q[(i + 1) % len(q)]]


def cost(q):
    if not q:
        return 0
    return len(q) + sum(q[i] == q[(i + 1) % len(q)] for i in range(len(q)))


def alternating(q):
    return bool(q) and all(q[i] != q[(i + 1) % len(q)] for i in range(len(q)))


def minimal_realization(q):
    """Return a word whose boundary-site parities are q up to cyclic rotation."""
    assert q and len(q) % 2 == 0
    if 0 in q:
        pivot = q.index(0)
        q = q[pivot:] + q[:pivot]
    gaps = [1 if q[i] != q[(i + 1) % len(q)] else 2 for i in range(len(q))]
    n = sum(gaps)
    positions = [q[0]]
    for gap in gaps[:-1]:
        positions.append(positions[-1] + gap)
    boundary_set = set(positions)
    word = [0] * n
    for i in range(1, n):
        word[i] = word[i - 1] ^ (i in boundary_set)
    mask = sum(value << i for i, value in enumerate(word))
    return q, mask, n


def main():
    assertions = 0
    summaries = []
    for n in range(1, 17):
        orbit_types = Counter()
        fixed = period_two = 0
        for mask in range(1 << n):
            preperiod, period = orbit_data(mask, n)
            parities = {length & 1 for length in run_lengths(mask, n)}
            recurrent = len(parities) == 1
            next_mask = update(mask, n)
            expected_boundaries = predicted_boundaries(mask, n)
            assert period in (1, 2)
            assert (preperiod == 0) == recurrent
            assert boundary_positions(next_mask, n) == expected_boundaries
            assertions += 3
            if n % 2 == 0 and boundary_positions(mask, n):
                q = [i % 2 for i in boundary_positions(mask, n)]
                assert [i % 2 for i in expected_boundaries] == erode(q)
                assertions += 1
            if preperiod == 0:
                if period == 1:
                    fixed += 1
                else:
                    period_two += 1
            orbit_types[(preperiod, period)] += 1
        expected = recurrent_counts(n)
        assert (fixed, period_two) == expected
        assert max(depth for depth, _ in orbit_types) == sharp_depth(n)
        assert orbit_data(extremal_witness(n), n)[0] == sharp_depth(n)
        assertions += 3
        summaries.append((n, sharp_depth(n), fixed, period_two))

    parity_words = 0
    mixed_parity_words = 0
    for length in range(2, 19, 2):
        for mask in range(1 << length):
            q = bits(mask, length)
            rotated, realized_mask, circumference = minimal_realization(q)
            actual = [i % 2 for i in boundary_positions(realized_mask, circumference)]
            assert circumference == cost(q)
            assert actual == rotated
            assertions += 2
            parity_words += 1
            if len(set(q)) > 1 and not alternating(q):
                assert cost(erode(q)) <= cost(q) - 4
                assertions += 1
                mixed_parity_words += 1

    print("odd_run_reversal_verify: PASS")
    print(f"assertions={assertions}")
    print("exhaustive_orders=1..16")
    print("n,max_preperiod,fixed_states,period_two_states")
    for row in summaries:
        print(",".join(map(str, row)))
    print(f"even_parity_words={parity_words}")
    print(f"mixed_cost_drop_words={mixed_parity_words}")
    print("theorem_control=boundary_survival,parity_eroder,realization,cost_drop,recurrence,census,sharp_clocks")


if __name__ == "__main__":
    main()
