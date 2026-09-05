#!/usr/bin/env python3
"""Independent Stage1 P feedback checks; imports no candidate implementation."""
from array import array
from collections import Counter
from functools import lru_cache
from itertools import product, permutations
from math import comb, factorial, prod

CHECKS = 0


def require(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def feedback(f):
    # Composition powers put every vertex on its terminal cycle; no peeling.
    n = len(f)
    endpoint = list(range(n))
    jump = list(f)
    exponent = n
    while exponent:
        if exponent & 1:
            endpoint = [jump[x] for x in endpoint]
        jump = [jump[x] for x in jump]
        exponent >>= 1
    period = {}
    for x in endpoint:
        if x in period:
            continue
        orbit = [x]
        y = f[x]
        while y != x:
            orbit.append(y)
            y = f[y]
        for y in orbit:
            period[y] = len(orbit) - 1
    return tuple(period[x] for x in endpoint)


def direct_control(f):
    out = []
    for x in range(len(f)):
        for _ in range(len(f)):
            x = f[x]
        y, size = f[x], 1
        while y != x:
            y, size = f[y], size + 1
        out.append(size - 1)
    return tuple(out)


def encode(f):
    index = 0
    for x in f:
        index = index * len(f) + x
    return index


def decode(index, n):
    result = [0] * n
    for j in range(n - 1, -1, -1):
        index, result[j] = divmod(index, n)
    return tuple(result)


def bound(n):
    if n == 1:
        return 0
    h, size = 2, 2
    while size * (size + 1) // 2 <= n:
        h += 1
        size = size * (size + 1) // 2
    return h


def critical_size(h):
    n = 2
    for _ in range(h - 2):
        n = n * (n + 1) // 2
    return n


def component_count(d, size):
    if size < d:
        return 0
    if size == d:
        return factorial(d - 1)
    return comb(size, d) * factorial(d - 1) * d * size ** (size - d - 1)


@lru_cache(None)
def block_count(d, size):
    # Component containing the least label, rather than author cyclic-set sum.
    if size == 0:
        return 1
    return sum(comb(size - 1, k - 1) * component_count(d, k)
               * block_count(d, size - k) for k in range(d, size + 1))


def fibre(g):
    return prod(block_count(j + 1, k) for j, k in Counter(g).items())


def image_count(n):
    # Exhaust occupation vectors using decreasing remaining label slots.
    def count(j, left):
        if j == n:
            return int(left == 0)
        return count(j + 1, left) + sum(comb(left, k) * count(j + 1, left - k)
                                        for k in range(j + 1, left + 1))
    return count(0, n)


def height_literal(f):
    seen = set()
    height = 0
    while any(f):
        require(f not in seen)
        seen.add(f)
        f = feedback(f)
        height += 1
    return height


def critical_test(f, h):
    if h == 2:
        return f == (1, 0)
    n, k = len(f), critical_size(h - 1)
    if sorted(f) != list(range(n)):
        return False
    seen, lengths = set(), []
    for i in range(n):
        if i in seen:
            continue
        length, j = 0, i
        while j not in seen:
            seen.add(j)
            length += 1
            j = f[j]
        lengths.append(length)
    return sorted(lengths) == list(range(1, k + 1)) and critical_test(feedback(f)[:k], h - 1)


def witness(h):
    f = (1, 0)
    for _ in range(2, h):
        n = len(f)
        out = [None] * (n * (n + 1) // 2)
        fresh = n
        # Insert a decreasing fresh-label chain after each old labelled anchor.
        for anchor, value in enumerate(f):
            chain = [anchor] + list(range(fresh + value - 1, fresh - 1, -1))
            fresh += value
            for i in range(len(chain)):
                out[chain[i]] = chain[(i + 1) % len(chain)]
        f = tuple(out)
    return f


def main():
    for n in range(1, 8):
        count = n ** n
        arrows, ranks = array('I'), bytearray()
        fibres = Counter()
        for f in product(range(n), repeat=n):
            g = feedback(f)
            if n <= 5:
                require(g == direct_control(f))
            r, q = len(set(f)), len(set(g))
            require(r >= sum(j + 1 for j in set(g)))
            require(r >= q * (q + 1) // 2)
            arrows.append(encode(g))
            ranks.append(r)
            fibres[encode(g)] += 1
        require(arrows[0] == 0)
        depths, rankmax = Counter(), Counter()
        heights = bytearray(count)
        for state in range(count):
            path, at = [], state
            while at != 0 and heights[at] == 0:
                require(at not in path)
                path.append(at)
                at = arrows[at]
            depth = heights[at]
            for at in reversed(path):
                depth += 1
                heights[at] = depth
            h = heights[state]
            require(h <= bound(n))
            if h >= 2:
                require(ranks[state] >= critical_size(h))
            depths[h] += 1
            rankmax[ranks[state]] = max(rankmax[ranks[state]], h)
        for r in range(1, n + 1):
            require(rankmax[r] == (bound(r) if r > 1 else int(n > 1)))
        require(depths[0] == 1)
        require(len(fibres) == image_count(n))
        maximum = (n + 1) ** (n - 1)
        require(max(fibres.values()) == maximum)
        require([g for g, k in fibres.items() if k == maximum] == [0])
        for g in product(range(n), repeat=n):
            actual, predicted = fibres[encode(g)], fibre(g)
            require(actual == predicted)
            require(bool(actual) == all(k > j for j, k in Counter(g).items()))
        if n in (2, 3, 6):
            h = bound(n)
            for state in range(count):
                require((heights[state] == h) == critical_test(decode(state, n), h))
            claimed = prod(factorial(critical_size(t) - critical_size(t - 1))
                           for t in range(3, h + 1))
            require(depths[h] == claimed)
        print(f'n={n} states={count} image={len(fibres)} depths={dict(sorted(depths.items()))} '
              f'max_fibre={maximum} rank_heights={dict(sorted(rankmax.items()))}', flush=True)
    for h in range(2, 8):
        f = witness(h)
        require(len(f) == critical_size(h))
        require(sorted(f) == list(range(len(f))))
        require(height_literal(f) == h)
        if h <= 6:
            require(critical_test(f, h))
        for extra in (0, 1, 4):
            rank = len(f) + extra
            extended = f + tuple(range(len(f), rank))
            for outside in (0, 1, 5):
                test = extended + (0,) * outside
                require(height_literal(test) == h)
                require(len(set(test)) == rank)
        print(f'critical_witness h={h} n={len(f)} exact_height={h}', flush=True)
    a, b = (0, 1, 1), (1, 0, 1)
    require(Counter(a) == Counter(b))
    require(feedback(a) != feedback(b))
    require(height_literal(a) == 1 and height_literal(b) == 2)
    print(f'ASSERTIONS={CHECKS}')
    print('MATHEMATICAL_CHECKS_PASS / STAGE1_ONLY / HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
