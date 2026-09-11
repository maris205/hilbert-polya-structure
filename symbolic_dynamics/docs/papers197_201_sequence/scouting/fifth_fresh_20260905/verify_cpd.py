#!/usr/bin/env python3
"""Exact CPD counterexample pressure; bounded checks are not proofs."""

from collections import Counter
from functools import lru_cache
from itertools import product
from math import factorial

checks = 0


def check(condition):
    global checks
    checks += 1
    assert condition, checks


def forward(a):
    n = len(a)
    occupied = 0
    answer = []
    for preference in a:
        displacement = 0
        while occupied & (1 << ((preference + displacement) % n)):
            displacement += 1
        occupied |= 1 << ((preference + displacement) % n)
        answer.append(displacement)
    return tuple(answer)


def in_core(d):
    return all(0 <= x <= i for i, x in enumerate(d))


def complement(d):
    return tuple(i - x for i, x in enumerate(d))


def inverse_dp(d):
    n = len(d)
    if not in_core(d):
        return 0

    @lru_cache(None)
    def count(mask):
        if not mask:
            return 1
        m = mask.bit_length() - 1
        rest = mask ^ (1 << m)
        left = rest
        total = 0
        while True:
            if left.bit_count() >= d[m]:
                total += count(left) * count(rest ^ left)
            if not left:
                break
            left = (left - 1) & rest
        return total

    return n * count((1 << (n - 1)) - 1)


def main():
    for n in range(1, 8):
        fibres = Counter()
        depth_counts = Counter()
        for source in product(range(n), repeat=n):
            target = forward(source)
            check(in_core(target))
            second = forward(target)
            check(second == complement(target))
            check(forward(second) == target)
            depth_counts[int(not in_core(source))] += 1
            fibres[target] += 1
        check(len(fibres) == factorial(n))
        check(depth_counts[0] == factorial(n))
        check(depth_counts[1] == n**n - factorial(n))
        check(max(fibres.values()) == factorial(n))
        for target in product(*(range(i + 1) for i in range(n))):
            check(fibres[target] == inverse_dp(target))
            check((fibres[target] == factorial(n)) == (not any(target[:-1])))
            check((forward(target) == target) == (n == 1))
        # Audit every absent target through n=5, avoiding an unnecessary
        # repeated complete target pass at the two larger source cutoffs.
        if n <= 5:
            for target in product(range(n), repeat=n):
                if not in_core(target):
                    check(inverse_dp(target) == 0)
        print(f"n={n} states={n**n} image={len(fibres)} "
              f"depth0={depth_counts[0]} depth1={depth_counts[1]} "
              f"max_fibre={max(fibres.values())} "
              f"max_targets={sum(v == factorial(n) for v in fibres.values())}",
              flush=True)
    print(f"ASSERTIONS={checks}")
    print("PASS / THEOREM_SPIKE_ONLY / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
