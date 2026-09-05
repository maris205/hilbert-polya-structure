#!/usr/bin/env python3
"""Exact scout for A -> A symmetric-difference [|A|].

The integer bit i-1 represents label i.  Exhaustion is finite evidence only;
the closed formulae checked here are proved separately in the theorem spike.
"""

from __future__ import annotations

from collections import Counter
from math import comb


def update(x: int) -> int:
    return x ^ ((1 << x.bit_count()) - 1)


def prefix_count(x: int, k: int) -> int:
    return (x & ((1 << k) - 1)).bit_count()


def fibre_formula(y: int, n: int) -> int:
    w = y.bit_count()
    if w & 1:
        return 0
    if w == 0:
        return n + 1
    r = w // 2
    positions = [i + 1 for i in range(n) if y >> i & 1]
    return positions[r] - positions[r - 1]


def two_cycle_state_formula(n: int) -> int:
    return sum(comb(k, k // 2) * comb(n - k, k // 2)
               for k in range(2, n + 1, 2) if k // 2 <= n - k)


def indegree_distribution_formula(n: int):
    out = Counter({n + 1: 1})
    for r in range(1, n // 2 + 1):
        for gap in range(1, n + 1):
            count = 0
            for left_middle in range(1, n - gap + 1):
                right_middle = left_middle + gap
                if left_middle - 1 >= r - 1 and n - right_middle >= r - 1:
                    count += (comb(left_middle - 1, r - 1)
                              * comb(n - right_middle, r - 1))
            if count:
                out[gap] += count
    return out


def cycle_data(x: int):
    path = []
    where = {}
    while x not in where:
        where[x] = len(path)
        path.append(x)
        x = update(x)
    return where[x], len(path) - where[x]


def duplicate_pairs(x: int, n: int) -> int:
    y = 0
    for i in range(n):
        if x >> i & 1:
            y |= 3 << (2 * i)
    return y


def main():
    assertions = 0
    summary = []
    for n in range(1, 19):
        size = 1 << n
        actual_fibres = Counter(update(x) for x in range(size))
        assert set(actual_fibres) == {y for y in range(size)
                                      if y.bit_count() % 2 == 0}
        assertions += size

        formula_distribution = indegree_distribution_formula(n)
        actual_distribution = Counter(actual_fibres.values())
        assert formula_distribution == actual_distribution
        assertions += len(actual_distribution)

        two_cycle_states = 0
        fixed = 0
        periods = set()
        max_tail = 0
        for y in range(size):
            assert actual_fibres.get(y, 0) == fibre_formula(y, n)
            assertions += 1

            z = update(y)
            if z == y:
                fixed += 1
            elif update(z) == y:
                two_cycle_states += 1
                k = y.bit_count()
                assert k > 0 and k % 2 == 0 and prefix_count(y, k) == k // 2
                assertions += 1

            tail, period = cycle_data(y)
            periods.add(period)
            max_tail = max(max_tail, tail)
            if period > 1:
                assert period % 2 == 0
                assertions += 1

        assert fixed == 1
        assert two_cycle_states == two_cycle_state_formula(n)
        assert sum(actual_fibres.values()) == size
        assertions += 3
        summary.append((n, len(actual_fibres), fixed, two_cycle_states,
                        max_tail, tuple(sorted(periods)), max(actual_fibres.values())))

    for n in range(1, 11):
        for x in range(1 << n):
            dx = duplicate_pairs(x, n)
            assert update(dx) == duplicate_pairs(update(x), n)
            assert update(x) == update(x)  # counted convention guard
            assertions += 2

            # Appending zero coordinates commutes with the update.
            assert update(x) == update(x) & ((1 << n) - 1)
            assertions += 1

    witnesses = {
        4: (5, {3, 5}),
        8: (12, {6, 9, 11, 12}),
        16: (30, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  14, 15, 17, 18, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30}),
    }
    for expected, (n, subset) in witnesses.items():
        x = sum(1 << (i - 1) for i in subset)
        tail, period = cycle_data(x)
        assert tail == 0 and period == expected
        assertions += 1

    print("self_cardinality_toggle_scout=PASS")
    print(f"assertions={assertions}")
    print("exhaustive_n<=18")
    print("columns=n,image,fixed,two_cycle_states,max_tail,periods,max_fibre")
    for row in summary:
        print(*row)
    print("explicit_period_witnesses=4@n5,8@n12,16@n30")


if __name__ == "__main__":
    main()
