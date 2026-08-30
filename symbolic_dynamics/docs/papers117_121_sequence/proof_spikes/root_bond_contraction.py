#!/usr/bin/env python3
"""Bounded falsification spike for bond contraction on permutations."""

from collections import Counter
from itertools import permutations


def standardize(values):
    rank = {value: index for index, value in enumerate(sorted(values))}
    return tuple(rank[value] for value in values)


def update(permutation):
    if not permutation:
        return permutation
    representatives = []
    run = [permutation[0]]
    for value in permutation[1:]:
        if abs(value - run[-1]) == 1:
            run.append(value)
        else:
            representatives.append(min(run))
            run = [value]
    representatives.append(min(run))
    return standardize(representatives)


def depth(permutation):
    time = 0
    while update(permutation) != permutation:
        permutation = update(permutation)
        time += 1
    return time


def main():
    assertions = 0
    summary = {}
    for n in range(1, 10):
        counts = Counter()
        for permutation in permutations(range(n)):
            value = depth(permutation)
            assert 0 <= value <= n - 1
            assertions += 1
            counts[value] += 1
        assert max(counts) == n - 1 if n > 1 else max(counts) == 0
        assertions += 1
        if n > 1:
            assert counts[n - 1] == 1 << (n - 1)
            assertions += 1
        summary[n] = dict(sorted(counts.items()))
    print({"assertions": assertions, "depth_counts": summary})


if __name__ == "__main__":
    main()
