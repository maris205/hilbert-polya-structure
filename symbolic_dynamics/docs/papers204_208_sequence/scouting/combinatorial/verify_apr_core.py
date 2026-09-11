#!/usr/bin/env python3
"""Falsification-only exact Catalan-core follow-up to C02_APR."""
from itertools import combinations, permutations
import json
from verify_breadth import alternating_prefix_rank as update, census


def in_core(w):
    n = len(w)
    a, b = w[::2], w[1::2]
    return (all(a[i] < a[i+1] for i in range(len(a)-1))
            and all(b[i] < b[i+1] for i in range(len(b)-1))
            and all(b[i] < a[i] for i in range(len(b)))
            and (n % 2 == 0 or a[-1] == n))


def core(m):
    labels = set(range(1, 2*m+1))
    for b in combinations(range(1, 2*m+1), m):
        a = tuple(sorted(labels-set(b)))
        if all(x < y for x, y in zip(b, a)):
            yield tuple(z for pair in zip(a, b) for z in pair)


def main():
    checked = 0
    for n in range(1, 9):
        for w in permutations(range(1, n+1)):
            assert in_core(update(update(w)))
            checked += 1
    rows = [census("C02_APR_CATALAN_CORE", 2*m, core(m), update) for m in range(1, 11)]
    odd_checks = 0
    for m in range(1, 9):
        for w in core(m):
            assert update(w+(2*m+1,)) == update(w)+(2*m+1,)
            odd_checks += 1
    print(json.dumps({"two_step_compression_checks": checked,
                      "odd_lift_checks": odd_checks,
                      "scope": "complete Catalan core only; ambient S_n not enumerated above n=8",
                      "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
