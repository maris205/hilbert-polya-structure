#!/usr/bin/env python3
"""Exact spike for synchronously flipping every odd cyclic run."""

from collections import Counter
from math import comb


def bits(mask, n):
    return [(mask >> i) & 1 for i in range(n)]


def run_lengths(mask, n):
    word = bits(mask, n)
    boundaries = [i for i in range(n) if word[i] != word[i - 1]]
    if not boundaries:
        return [n]
    return [
        (boundaries[(i + 1) % len(boundaries)] - boundaries[i]) % n
        for i in range(len(boundaries))
    ]


def update(mask, n):
    word = bits(mask, n)
    boundaries = [i for i in range(n) if word[i] != word[i - 1]]
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
    color = 0
    for length in lengths:
        for _ in range(length):
            mask |= color << position
            position += 1
        color ^= 1
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


def main():
    assertions = 0
    summary = {}
    for n in range(1, 17):
        data = Counter()
        fixed = period_two = 0
        for mask in range(1 << n):
            preperiod, period = orbit_data(mask, n)
            lengths = run_lengths(mask, n)
            recurrent = len({length & 1 for length in lengths}) == 1
            assert period in (1, 2)
            assert (preperiod == 0) == recurrent
            assertions += 2
            if preperiod == 0:
                if period == 1:
                    fixed += 1
                else:
                    period_two += 1
            data[(preperiod, period)] += 1
        expected_fixed, expected_two = recurrent_counts(n)
        assert (fixed, period_two) == (expected_fixed, expected_two)
        assert max(preperiod for preperiod, _ in data) == sharp_depth(n)
        assert orbit_data(extremal_witness(n), n)[0] == sharp_depth(n)
        assertions += 3
        summary[n] = {
            "max_preperiod": sharp_depth(n),
            "fixed_states": fixed,
            "period_two_states": period_two,
        }
    print({"assertions": assertions, "summary": summary})


if __name__ == "__main__":
    main()
