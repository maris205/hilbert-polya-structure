#!/usr/bin/env python3
"""Exact CSPD negative-control verifier; no candidate promotion implied."""
from collections import Counter
from itertools import product
from math import factorial, prod

checks = 0


def check(condition):
    global checks
    checks += 1
    assert condition, checks


def forward(a):
    n = len(a)
    answer = [-1] * n
    for preference in a:
        distance = 0
        while answer[(preference + distance) % n] >= 0:
            distance += 1
        answer[(preference + distance) % n] = distance
    return tuple(answer)


def core(a):
    return all(x <= i for i, x in enumerate(a))


def classical(a):
    return core(sorted(a))


def rotated_core(a):
    n = len(a)
    return any(all(a[(s + j) % n] <= j for j in range(n))
               for s in range(n))


def atlas(d):
    n = len(d)
    below = [sum(1 << ((i - j) % n) for j in range(1, x + 1))
             for i, x in enumerate(d)]
    for k in range(n):
        for i in range(n):
            if below[i] & (1 << k):
                below[i] |= below[k]
    if any(below[i] & (1 << i) for i in range(n)):
        return 0, ()
    ideals = [b | (1 << i) for i, b in enumerate(below)]
    for i in range(n):
        for j in range(i):
            intersection = ideals[i] & ideals[j]
            check(not intersection or intersection in (ideals[i], ideals[j]))
    hooks = tuple(b.bit_count() for b in ideals)
    denominator = prod(hooks)
    check(factorial(n) % denominator == 0)
    return factorial(n) // denominator, hooks


def indecomposable(n):
    a = [0] * (n + 1)
    for m in range(1, n + 1):
        a[m] = factorial(m) - sum(a[j] * factorial(m - j)
                                   for j in range(1, m))
    return a[n]


def main():
    for n in range(1, 8):
        fibres = Counter()
        depths = Counter()
        for source in product(range(n), repeat=n):
            target = forward(source)
            second = forward(target)
            check(classical(target))
            check(core(second))
            check(core(target) == classical(source))
            if core(source):
                check(target == tuple(i - x for i, x in enumerate(source)))
            depth = 0 if core(source) else 1 if classical(source) else 2
            depths[depth] += 1
            fibres[target] += 1
        check(len(fibres) == indecomposable(n + 1))
        check(depths[0] == factorial(n))
        check(depths[1] == (n + 1) ** (n - 1) - factorial(n))
        check(depths[2] == n**n - (n + 1) ** (n - 1))
        for target, mass in fibres.items():
            predicted, hooks = atlas(target)
            check(mass == predicted)
            check(rotated_core(target))
            check((mass == factorial(n)) == (not any(target)))
            check((mass == 1) == (sorted(hooks) == list(range(1, n + 1))))
        check(sum(m == 1 for m in fibres.values()) == factorial(n))
        # Whole codomain rejection check, bounded separately from source pass.
        if n <= 6:
            for target in product(range(n), repeat=n):
                if target not in fibres:
                    check(atlas(target)[0] == 0)
                    check(not rotated_core(target))
        print(f"n={n} states={n**n} image={len(fibres)} "
              f"depths={depths[0]},{depths[1]},{depths[2]} "
              f"max_fibre={max(fibres.values())} "
              f"min_targets={sum(v == 1 for v in fibres.values())}", flush=True)
    print(f"ASSERTIONS={checks}")
    print("PASS / KILL_OWNER_TRANSFER / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
