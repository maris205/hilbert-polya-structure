#!/usr/bin/env python3
"""Exact exhaustive and labelled-assembly verifier for graph complement layers."""

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


ASSERTIONS = 0


def check(statement, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(context)


@lru_cache(None)
def edges(n):
    return tuple(combinations(range(n), 2))


def complement(n, mask, vertices=None):
    vertices = tuple(range(n)) if vertices is None else tuple(vertices)
    result = mask
    lookup = {edge: bit for bit, edge in enumerate(edges(n))}
    for u, v in combinations(vertices, 2):
        result ^= 1 << lookup[(u, v)]
    return result


def components(n, mask):
    adjacency = [0] * n
    for bit, (u, v) in enumerate(edges(n)):
        if mask >> bit & 1:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    unseen = (1 << n) - 1
    answer = []
    while unseen:
        seed = unseen & -unseen
        reached = seed
        frontier = seed
        while frontier:
            vertex_bit = frontier & -frontier
            frontier ^= vertex_bit
            vertex = vertex_bit.bit_length() - 1
            new = adjacency[vertex] & unseen & ~reached
            reached |= new
            frontier |= new
        unseen &= ~reached
        answer.append(tuple(i for i in range(n) if reached >> i & 1))
    return tuple(answer)


def step(n, mask):
    result = mask
    for component in components(n, mask):
        if len(component) % 2:
            result = complement(n, result, component)
    return result


def orbit(n, mask):
    seen = {}
    state = mask
    while state not in seen:
        seen[state] = len(seen)
        state = step(n, state)
    return seen[state], len(seen) - seen[state]


def assemblies(maximum, allowed):
    values = [0] * (maximum + 1)
    values[0] = 1
    for n in range(1, maximum + 1):
        values[n] = sum(
            comb(n - 1, k - 1) * allowed[k] * values[n - k]
            for k in range(1, n + 1)
        )
    return values


def main():
    maximum = 6
    connected = [0] * (maximum + 1)
    coconnected = [0] * (maximum + 1)
    exhaustive_cumulative = []
    rows = []
    for n in range(maximum + 1):
        depth_hist = Counter()
        period_hist = Counter()
        total = 1 << len(edges(n))
        for mask in range(total):
            comps = components(n, mask)
            if n == 0 or len(comps) == 1:
                connected[n] += 1
            if n == 1 or (
                n > 1
                and len(comps) == 1
                and len(components(n, complement(n, mask))) == 1
            ):
                coconnected[n] += 1
            depth, period = orbit(n, mask)
            check(period in (1, 2), (n, mask, "period"))
            check(depth <= max(0, (n - 1) // 2), (n, mask, "depth"))
            depth_hist[depth] += 1
            period_hist[period] += 1
        cumulative = []
        running = 0
        for t in range(max(depth_hist) + 1):
            running += depth_hist[t]
            cumulative.append(running)
        exhaustive_cumulative.append(cumulative)
        rows.append((n, total, dict(sorted(depth_hist.items())), dict(sorted(period_hist.items()))))

    for n in range(3, maximum + 1, 2):
        check(coconnected[n] == 2 * connected[n] - (1 << len(edges(n))), (n, "co-connected"))

    odd_depth = []
    base = [0] * (maximum + 1)
    for n in range(1, maximum + 1, 2):
        base[n] = coconnected[n]
    odd_depth.append(base)
    all_cumulative = []
    for t in range(maximum // 2 + 1):
        if t:
            allowed_previous = [0] * (maximum + 1)
            for n in range(1, maximum + 1):
                allowed_previous[n] = connected[n] if n % 2 == 0 else odd_depth[-1][n]
            assembled = assemblies(maximum, allowed_previous)
            current = [0] * (maximum + 1)
            for n in range(1, maximum + 1, 2):
                current[n] = coconnected[n] + assembled[n] - allowed_previous[n]
            odd_depth.append(current)
        allowed = [0] * (maximum + 1)
        for n in range(1, maximum + 1):
            allowed[n] = connected[n] if n % 2 == 0 else odd_depth[t][n]
        all_cumulative.append(assemblies(maximum, allowed))

    fixed_allowed = [0] * (maximum + 1)
    fixed_allowed[1] = 1
    for n in range(2, maximum + 1, 2):
        fixed_allowed[n] = connected[n]
    fixed = assemblies(maximum, fixed_allowed)

    for n in range(maximum + 1):
        for t, observed in enumerate(exhaustive_cumulative[n]):
            check(all_cumulative[t][n] == observed, (n, t, all_cumulative[t][n], observed))
        check(fixed[n] <= all_cumulative[0][n], (n, "fixed subset recurrent"))

    print("odd-component complement layer verifier: PASS")
    print(f"assertions={ASSERTIONS}")
    print("connected", connected)
    print("coconnected_odd", [coconnected[n] if n % 2 else 0 for n in range(maximum + 1)])
    print("fixed", fixed)
    print("n states depth_hist period_hist")
    for row in rows:
        print(*row)
    print("cumulative_by_t")
    for t, values in enumerate(all_cumulative):
        print(t, values)


if __name__ == "__main__":
    main()
