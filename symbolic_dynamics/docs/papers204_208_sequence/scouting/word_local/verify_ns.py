#!/usr/bin/env python3
"""Standalone author verification; no pilot/old-paper imports."""
from collections import Counter
from itertools import product, combinations
from math import comb, factorial
import json


checks = Counter()


def check(ok, tag, witness=None):
    checks[tag] += 1
    if not ok:
        raise AssertionError((tag, witness))


def step(x):
    y = []
    for i in range(len(x)):
        j = i-1
        while j >= 0 and x[j] >= x[i]:
            j -= 1
        y.append(0 if j < 0 else i-j)
    return tuple(y)


def blocks(x):
    i = 1
    ans = []
    while i < len(x):
        if x[i] == 0:
            i += 1
            continue
        start = i
        while i < len(x) and x[i] != 0:
            i += 1
        ans.append((start-1, i-start))
    return ans


def core(x):
    return all(x[r+j] in (1, j) for r, m in blocks(x) for j in range(1, m+1))


def involution(x):
    y = list(x)
    for r, m in blocks(x):
        for j in range(2, m+1):
            y[r+j] = j if x[r+j] == 1 else 1
    return tuple(y)


def endpoint(x):
    y = list(x)
    for r, m in blocks(x):
        y[r+1] = 1
        for j in range(2, m+1):
            y[r+j] = j if x[r+j-1] < x[r+j] else 1
    return tuple(y)


def block_count(r, m, ascents):
    total = 0
    for k in range(len(ascents)+1):
        for subset in combinations(ascents, k):
            cuts = (1,)+subset+(m+1,)
            term = 1
            for a, end in zip(cuts, cuts[1:]):
                term *= comb(r+end-1, end-a)
            total += (-1)**(len(ascents)-k)*term
    return total


def fibre(y, t):
    if not core(y):
        return 0
    answer = 1
    for r, m in blocks(y):
        ascents = tuple(j for j in range(2, m+1)
                        if (y[r+j] == j if t % 2 == 0 else y[r+j] == 1))
        answer *= block_count(r, m, ascents)
    return answer


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a+b
    return a


def main():
    reports = []
    for n in range(1, 9):
        states = list(product(*(range(i+1) for i in range(n))))
        arrows = {x: step(x) for x in states}
        counts = {t: Counter() for t in range(2, 6)}
        heights = Counter()
        fixed = recurrent = 0
        for x in states:
            y, z = arrows[x], arrows[arrows[x]]
            check([i for i, a in enumerate(x) if a == 0] ==
                  [i for i, a in enumerate(y) if a == 0], 'zero_barriers')
            check(z == endpoint(x), 'two_step_endpoint', x)
            check(core(z), 'two_step_core')
            for r, m in blocks(y):
                for j in range(2, m+1):
                    check(y[r+j] == 1 or y[r+j] > y[r+j-1], 'one_or_rise')
            if core(x):
                recurrent += 1
                check(y == involution(x), 'core_action')
                check(z == x, 'core_period')
            if y == x:
                fixed += 1
            heights[0 if core(x) else (1 if core(y) else 2)] += 1
            current = z
            for t in range(2, 6):
                counts[t][current] += 1
                current = arrows[current]
        check(recurrent == fib(2*n-1), 'recurrent_census')
        check(fixed == fib(n+1), 'fixed_census')
        check(max(heights) == (0 if n <= 2 else 1 if n == 3 else 2), 'sharp_height')
        for t in range(2, 6):
            for y in states:
                check(counts[t][y] == fibre(y, t), 'all_target_fibre', (n, t, y))
            check(sum(counts[t].values()) == factorial(n), 'fibre_mass')
        reports.append(dict(n=n, states=len(states), image=len(set(arrows.values())),
                            recurrent=recurrent, fixed=fixed, depths=dict(heights)))
    # Isolated source-count test, independent of the dynamical decoder.
    for r in range(5):
        for m in range(1, 7):
            actual = Counter()
            for x in product(*(range(1, r+j+1) for j in range(1, m+1))):
                actual[tuple(j for j in range(2, m+1) if x[j-2] < x[j-1])] += 1
            for bits in product(range(2), repeat=m-1):
                ascents = tuple(j for j in range(2, m+1) if bits[j-2])
                check(actual[ascents] == block_count(r, m, ascents), 'flagged_ascent_count')
    print(json.dumps(dict(audit='NS_author_v1', reports=reports,
                          checks=dict(sorted(checks.items())),
                          total_checks=sum(checks.values())), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
