#!/usr/bin/env python3
"""Exact control for maximal permutation-bond-run contraction.

This is a Phase-2b theorem spike, not evidence of novelty.  A permutation is
cut into maximal contiguous runs whose successive values differ by one.  Each
run is replaced by its minimum and the resulting word is standardized.
"""

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def standardize(values):
    rank = {value: index for index, value in enumerate(sorted(values))}
    return tuple(rank[value] for value in values)


def step(permutation):
    if not permutation:
        return permutation
    minima = []
    run = [permutation[0]]
    for value in permutation[1:]:
        if abs(value - run[-1]) == 1:
            run.append(value)
        else:
            minima.append(min(run))
            run = [value]
    minima.append(min(run))
    return standardize(minima)


def bond_count(permutation):
    return sum(abs(a - b) == 1 for a, b in zip(permutation, permutation[1:]))


def depth(permutation):
    time = 0
    while step(permutation) != permutation:
        permutation = step(permutation)
        time += 1
    return time


def positions(permutation):
    answer = [0] * len(permutation)
    for index, value in enumerate(permutation):
        answer[value] = index
    return answer


def admissible(target, states):
    """States are 0 (singleton), + (increasing), or - (decreasing)."""
    pos = positions(target)
    for value in range(len(target) - 1):
        if abs(pos[value] - pos[value + 1]) != 1:
            continue
        if pos[value] < pos[value + 1]:
            if states[value] in "0+" and states[value + 1] in "0+":
                return False
        else:
            if states[value] in "0-" and states[value + 1] in "0-":
                return False
    return True


@lru_cache(maxsize=None)
def fibre_signature(target):
    """Number of admissible spin assignments by non-singleton blocks."""
    k = len(target)
    signature = Counter()
    for states in product("0+-", repeat=k):
        if not admissible(target, states):
            continue
        oriented = sum(state != "0" for state in states)
        signature[oriented] += 1
    return tuple(sorted(signature.items()))


def fibre_coefficient(target, source_length):
    """Coefficient of the signed three-state inflation partition function."""
    total = 0
    k = len(target)
    for oriented, multiplicity in fibre_signature(target):
        base = k + oriented
        excess = source_length - base
        if excess < 0:
            continue
        if oriented == 0:
            total += multiplicity * (excess == 0)
        else:
            total += multiplicity * comb(excess + oriented - 1, oriented - 1)
    return total


def run():
    # Every bond run is necessarily monotone and interval-valued.
    for n in range(1, 8):
        actual = Counter()
        depth_counts = Counter()
        for permutation in permutations(range(n)):
            image = step(permutation)
            actual[image] += 1
            depth_counts[depth(permutation)] += 1
            check(len(image) == n - bond_count(permutation), (permutation, image))
        check(max(depth_counts) == n - 1, (n, depth_counts))
        check(depth_counts[n - 1] == 1 << (n - 1), (n, depth_counts))

        for k in range(1, n + 1):
            for target in permutations(range(k)):
                expected = fibre_coefficient(target, n)
                check(actual[target] == expected, (n, target, actual[target], expected))

    # A target with exactly one bond has exactly two one-bond lifts.
    for k in range(2, 8):
        for target in permutations(range(k)):
            if bond_count(target) == 1:
                check(fibre_coefficient(target, k + 1) == 2, (k, target))

    print("r3_fibre_verify: PASS")
    print(f"assertions={ASSERTIONS}")
    print("max_depth(n)=n-1")
    print("deepest_count(n)=2^(n-1)")
    print("fibre=three_state_signed_bond_path_partition_function")


if __name__ == "__main__":
    run()
