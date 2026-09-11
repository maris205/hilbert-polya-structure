#!/usr/bin/env python3
"""Fresh finite algebra intake; no promotion follows from these finite boxes."""
from collections import Counter
from itertools import combinations, product
from random import Random


def census(label, values, transform):
    values = list(values)
    index = {x: i for i, x in enumerate(values)}
    ff = [index[transform(x)] for x in values]
    indegree = Counter(ff)
    tails, periods = Counter(), Counter()
    for i in range(len(values)):
        seen, at = {}, i
        while at not in seen:
            seen[at] = len(seen)
            at = ff[at]
        tails[seen[at]] += 1
        periods[len(seen) - seen[at]] += 1
    fixed = sum(i == j for i, j in enumerate(ff))
    print(label, f"states={len(values)} image={len(indegree)} fixed={fixed}",
          f"max_tail={max(tails)} max_fibre={max(indegree.values())}",
          f"periods={sorted(periods)}", f"tail_hist={dict(sorted(tails.items()))}")


def unique_sums(d):
    n = 1 << d
    pair_classes = [[(a, a ^ z) for a in range(n) if a < (a ^ z)]
                    for z in range(1, n)]

    def update(mask):
        out = 0
        for z, pairs in enumerate(pair_classes, 1):
            count = sum(bool(mask & (1 << a)) and bool(mask & (1 << b)) for a, b in pairs)
            if count == 1:
                out |= 1 << z
        return out
    census(f"UPR d={d}", range(1 << n), update)


def collision_removal(p):
    def update(xy):
        x, y = xy
        return (x * (1 - y)) % p, (y * (1 - x)) % p
    for x, y in product(range(p), repeat=2):
        u, v = update((x, y))
        assert (u - v) % p == (x - y) % p
        d = (x - y) % p
        assert u == (x * (1 + d - x)) % p
        if p > 2:
            half = pow(2, -1, p)
            z = ((1 + d) * half - x) % p
            zz = ((1 + d) * half - u) % p
            assert zz == (z * z + (1 - d * d) * half * half) % p
    for u, v in product(range(p), repeat=2):
        d = (u - v) % p
        actual = {xy for xy in product(range(p), repeat=2) if update(xy) == (u, v)}
        inverse = {(x, (x - d) % p) for x in range(p)
                   if (x * x - (1 + d) * x + u) % p == 0}
        assert actual == inverse
    census(f"MCR p={p}", product(range(p), repeat=2), update)


def upr_stress(d, trials=3000):
    rng = Random(20260905 + d)
    n = 1 << d

    def update(mask):
        support = [i for i in range(n) if mask & (1 << i)]
        once, multiple = 0, 0
        for a, b in combinations(support, 2):
            bit = 1 << (a ^ b)
            multiple |= once & bit
            once |= bit
        return once & ~multiple

    max_tail, periods = 0, set()
    newcore = None
    for trial in range(trials):
        size = rng.randrange(n + 1)
        start = sum(1 << a for a in rng.sample(range(n), size))
        seen, at = {}, start
        while at not in seen:
            seen[at] = len(seen)
            at = update(at)
        tail, period = seen[at], len(seen) - seen[at]
        max_tail = max(max_tail, tail)
        periods.add(period)
        if period != 1 or at.bit_count() not in (0, 3):
            newcore = start, at, tail, period
            break
    print(f"UPR stress d={d} trials={trial + 1} limit={trials} max_tail={max_tail}",
          f"periods={sorted(periods)} unexpected_core={newcore}")


def upr_counterexample():
    # Separate ordinary Counter implementation, independent of both UPR loops.
    def update(mask):
        support = [i for i in range(64) if (mask >> i) & 1]
        counts = Counter(a ^ b for a, b in combinations(support, 2))
        return sum(1 << z for z, count in counts.items() if count == 1)
    a, b = 11253440500314867716, 11533932229067682872
    assert a != b and update(a) == b and update(b) == a
    print(f"UPR d=6 certified_2cycle=({a},{b}) sizes=({a.bit_count()},{b.bit_count()})")


def polynomial_advection(p):
    def update(coeff):
        out = [0] * p
        for i, a in enumerate(coeff):
            for j in range(1, p):
                degree = i + j - 1
                if degree >= p:
                    degree -= p - 1
                out[degree] += a * j * coeff[j]
        return tuple(z % p for z in out)
    census(f"CPA p={p}", product(range(p), repeat=p), update)


def main():
    for d in (1, 2, 3, 4):
        unique_sums(d)
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        collision_removal(p)
    for d in (5, 6, 7):
        upr_stress(d)
    upr_counterexample()
    for p in (2, 3, 5):
        polynomial_advection(p)


if __name__ == "__main__":
    main()
