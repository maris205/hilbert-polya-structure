#!/usr/bin/env python3
"""Exact spike for synchronous open-neighbourhood mex recolouring.

For a fixed graph G, a colouring c:V->{0,...,Delta(G)} is updated by
    c'(v) = mex { c(u) : uv in E(G) }.
On a complete multipartite graph, one round makes every part monochromatic.
The subsequent quotient map on k part-colours is exhaustively checked here.
"""

from itertools import product
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def mex(values):
    values = set(values)
    x = 0
    while x in values:
        x += 1
    return x


def quotient_step(state):
    """Part-colour map for a complete k-partite graph after round one."""
    return tuple(mex(state[j] for j in range(len(state)) if j != i) for i in range(len(state)))


def orbit_data(start):
    seen = {}
    path = []
    x = start
    while x not in seen:
        seen[x] = len(path)
        path.append(x)
        x = quotient_step(x)
    mu = seen[x]
    return mu, len(path) - mu, tuple(path[mu:])


def quotient_statistics(k):
    states = list(product(range(k), repeat=k)) if k else [()]
    fixed = 0
    cycles = set()
    max_depth = 0
    max_period = 1
    first_nonuniform_two_cycle = None
    first_depth_over_one = None

    for state in states:
        image = quotient_step(state)
        check(all(0 <= x < max(k, 1) for x in image), f"palette escaped at k={k}: {state}->{image}")
        is_fixed = image == state
        distinct = len(set(state)) == k
        check(is_fixed == distinct, f"fixed-point classification failed at k={k}: {state}")
        fixed += is_fixed
        depth, period, cycle = orbit_data(state)
        max_depth = max(max_depth, depth)
        max_period = max(max_period, period)
        canonical_cycle = min(tuple(cycle[i:] + cycle[:i]) for i in range(period))
        cycles.add(canonical_cycle)
        y = state
        for _ in range(depth):
            y = quotient_step(y)
        z = y
        for _ in range(period):
            z = quotient_step(z)
        check(z == y, f"orbit certificate failed at k={k}: {state}")
        if period == 2 and len(set(cycle[0])) > 1 and first_nonuniform_two_cycle is None:
            first_nonuniform_two_cycle = (state, cycle)
        if depth > 1 and first_depth_over_one is None:
            first_depth_over_one = (state, depth, cycle)

    check(fixed == factorial(k), f"expected k! fixed points at k={k}, got {fixed}")
    return {
        "k": k,
        "states": len(states),
        "fixed": fixed,
        "cycles": len(cycles),
        "periods": sorted({len(cycle) for cycle in cycles}),
        "max_depth": max_depth,
        "max_period": max_period,
        "first_nonuniform_two_cycle": first_nonuniform_two_cycle,
        "first_depth_over_one": first_depth_over_one,
    }


def complete_multipartite_neighbours(sizes):
    offsets = []
    total = 0
    for size in sizes:
        offsets.append(range(total, total + size))
        total += size
    part_of = {}
    for i, vertices in enumerate(offsets):
        for v in vertices:
            part_of[v] = i
    neighbours = []
    for v in range(total):
        neighbours.append(tuple(u for u in range(total) if part_of[u] != part_of[v]))
    return offsets, neighbours


def graph_step(colouring, neighbours):
    return tuple(mex(colouring[u] for u in neighbours[v]) for v in range(len(colouring)))


def check_one_round_collapse():
    """Exhaust all K_{a_1,...,a_k} with total order at most five."""
    for sizes in ((1, 1), (1, 2), (2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 2)):
        parts, neighbours = complete_multipartite_neighbours(sizes)
        delta = max(map(len, neighbours), default=0)
        for colouring in product(range(delta + 1), repeat=sum(sizes)):
            image = graph_step(colouring, neighbours)
            for part in parts:
                values = {image[v] for v in part}
                check(len(values) == 1, f"part did not collapse: sizes={sizes}, c={colouring}")
            second = graph_step(image, neighbours)
            part_state = tuple(image[part.start] for part in parts)
            expected = quotient_step(part_state)
            actual = tuple(second[part.start] for part in parts)
            check(actual == expected, f"quotient mismatch: sizes={sizes}, c={colouring}")


def main():
    check_one_round_collapse()
    stats = [quotient_statistics(k) for k in range(0, 7)]
    print("SYNCHRONOUS OPEN-NEIGHBOURHOOD MEX")
    for data in stats:
        print(
            "k={k} states={states} fixed={fixed} cycles={cycles} "
            "max_depth={max_depth} max_period={max_period} periods={periods}".format(**data)
        )

    first_nonuniform = next(
        (data["k"], data["first_nonuniform_two_cycle"])
        for data in stats
        if data["first_nonuniform_two_cycle"] is not None
    )
    first_long_transient = next(
        (data["k"], data["first_depth_over_one"])
        for data in stats
        if data["first_depth_over_one"] is not None
    )
    first_period_over_two = next(
        ((data["k"], data["max_period"]) for data in stats if data["max_period"] > 2),
        None,
    )
    print(f"first_nonuniform_two_cycle={first_nonuniform}")
    print(f"first_depth_over_one={first_long_transient}")
    print(f"first_period_over_two={first_period_over_two}")
    print(f"assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
