#!/usr/bin/env python3
"""Exact scout for odd-component complementation on labelled simple graphs.

The graph is an edge bit mask in lexicographic edge order.  At one synchronous
step, the induced graph on every odd-order connected component is complemented;
even-order components are left unchanged.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def edge_list(n):
    return tuple(combinations(range(n), 2))


def adjacency(n, mask):
    adj = [0] * n
    for bit, (u, v) in enumerate(edge_list(n)):
        if mask >> bit & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def components(n, mask):
    adj = adjacency(n, mask)
    unseen = (1 << n) - 1
    answer = []
    while unseen:
        seed = unseen & -unseen
        reached = seed
        frontier = seed
        while frontier:
            vbit = frontier & -frontier
            frontier ^= vbit
            v = vbit.bit_length() - 1
            new = adj[v] & unseen & ~reached
            reached |= new
            frontier |= new
        unseen &= ~reached
        answer.append(tuple(v for v in range(n) if reached >> v & 1))
    return tuple(answer)


def induced_complement_connected(n, mask, vertices):
    if len(vertices) <= 1:
        return True
    vertex_mask = sum(1 << v for v in vertices)
    adj = adjacency(n, mask)
    start = 1 << vertices[0]
    reached = start
    frontier = start
    while frontier:
        vbit = frontier & -frontier
        frontier ^= vbit
        v = vbit.bit_length() - 1
        complement_neighbours = vertex_mask & ~(adj[v] | (1 << v))
        new = complement_neighbours & ~reached
        reached |= new
        frontier |= new
    return reached == vertex_mask


def phi(n, mask):
    result = mask
    edge_to_bit = {edge: bit for bit, edge in enumerate(edge_list(n))}
    for component in components(n, mask):
        if len(component) % 2:
            for u, v in combinations(component, 2):
                result ^= 1 << edge_to_bit[(u, v)]
    return result


def fixed_criterion(n, mask):
    return all(len(c) == 1 or len(c) % 2 == 0 for c in components(n, mask))


def recurrent_criterion(n, mask):
    for component in components(n, mask):
        if len(component) > 1 and len(component) % 2:
            if not induced_complement_connected(n, mask, component):
                return False
    return True


def orbit_data(n, mask):
    seen = {}
    state = mask
    while state not in seen:
        seen[state] = len(seen)
        state = phi(n, state)
    return seen[state], len(seen) - seen[state]


def assembly_count(n, allowed_connected):
    values = [0] * (n + 1)
    values[0] = 1
    for size in range(1, n + 1):
        values[size] = sum(
            comb(size - 1, block_size - 1)
            * allowed_connected[block_size]
            * values[size - block_size]
            for block_size in range(1, size + 1)
        )
    return values


EXPECTED = {
    0: (1, 1, 0),
    1: (1, 1, 0),
    2: (2, 2, 0),
    3: (4, 4, 1),
    4: (48, 48, 1),
    5: (216, 648, 2),
    6: (27920, 30512, 2),
}


def main():
    connected = [0] * 7
    rows = []
    for n in range(7):
        total = 1 << len(edge_list(n))
        fixed = 0
        recurrent = 0
        depth_histogram = Counter()
        period_histogram = Counter()
        indegrees = Counter()
        for mask in range(total):
            image = phi(n, mask)
            indegrees[image] += 1
            check(0 <= image < total, (n, mask, "range"))
            old_components = [frozenset(c) for c in components(n, mask)]
            for new_component in components(n, image):
                check(
                    any(set(new_component) <= old for old in old_components),
                    (n, mask, "components do not refine"),
                )
            depth, period = orbit_data(n, mask)
            check(period <= 2, (n, mask, "period", period))
            check(depth <= max(0, (n - 1) // 2), (n, mask, "depth", depth))
            is_fixed = image == mask
            is_recurrent = phi(n, image) == mask
            check(is_fixed == fixed_criterion(n, mask), (n, mask, "fixed criterion"))
            check(
                is_recurrent == recurrent_criterion(n, mask),
                (n, mask, "recurrent criterion"),
            )
            fixed += is_fixed
            recurrent += is_recurrent
            depth_histogram[depth] += 1
            period_histogram[period] += 1
            if n == 0 or len(components(n, mask)) == 1:
                connected[n] += 1
        expected_fixed, expected_recurrent, expected_depth = EXPECTED[n]
        check(fixed == expected_fixed, (n, "fixed", fixed))
        check(recurrent == expected_recurrent, (n, "recurrent", recurrent))
        check(max(depth_histogram) == expected_depth, (n, "max depth"))
        rows.append(
            (
                n,
                total,
                fixed,
                recurrent,
                dict(sorted(depth_histogram.items())),
                dict(sorted(period_histogram.items())),
                max(indegrees.values()),
            )
        )

    fixed_components = [0] * 7
    recurrent_components = [0] * 7
    fixed_components[1] = recurrent_components[1] = 1
    for n in range(2, 7):
        if n % 2 == 0:
            fixed_components[n] = connected[n]
            recurrent_components[n] = connected[n]
        else:
            recurrent_components[n] = 2 * connected[n] - (1 << len(edge_list(n)))
            check(recurrent_components[n] >= 0, (n, "co-connected count"))
    fixed_from_egf = assembly_count(6, fixed_components)
    recurrent_from_egf = assembly_count(6, recurrent_components)
    for n, (_, _, fixed, recurrent, *_rest) in enumerate(rows):
        check(fixed == fixed_from_egf[n], (n, "fixed EGF"))
        check(recurrent == recurrent_from_egf[n], (n, "recurrent EGF"))
        check((recurrent - fixed) % 2 == 0, (n, "two-cycle exponent"))

    print("odd-component complement: exhaustive labelled-graph census")
    print("n states fixed recurrent depth_hist period_hist max_indegree")
    for row in rows:
        print(*row)
    print("connected_counts", connected)
    print("fixed_EGF_coefficients", fixed_from_egf)
    print("recurrent_EGF_coefficients", recurrent_from_egf)
    print("ASSERTIONS", ASSERTIONS)


if __name__ == "__main__":
    main()
