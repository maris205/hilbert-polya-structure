#!/usr/bin/env python3
"""Exact spike for odd-degree synchronous local complementation.

The phase space is the set of labelled simple graphs on [n].  In one round,
an edge {u,v} is toggled when u and v have an odd number of common neighbours
whose current degree is odd.  This is the genuinely simultaneous adjacency
update A <- A + offdiag(A D A) over GF(2), where D records odd degrees.
"""

from itertools import combinations


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def edges_for(n):
    return tuple(combinations(range(n), 2))


def adjacency(mask, n):
    adj = [0] * n
    for bit, (u, v) in enumerate(edges_for(n)):
        if (mask >> bit) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def encode(adj, n):
    mask = 0
    for bit, (u, v) in enumerate(edges_for(n)):
        if (adj[u] >> v) & 1:
            mask |= 1 << bit
    return mask


def degree_parity(mask, n):
    return tuple(x.bit_count() & 1 for x in adjacency(mask, n))


def step(mask, n):
    adj = adjacency(mask, n)
    odd_vertices = 0
    for v in range(n):
        if adj[v].bit_count() & 1:
            odd_vertices |= 1 << v
    out = mask
    for bit, (u, v) in enumerate(edges_for(n)):
        if (adj[u] & adj[v] & odd_vertices).bit_count() & 1:
            out ^= 1 << bit
    return out


def decoded_edges(mask, n):
    return [edge for bit, edge in enumerate(edges_for(n)) if (mask >> bit) & 1]


def functional_statistics(n):
    size = 1 << (n * (n - 1) // 2)
    successor = [step(mask, n) for mask in range(size)]
    depth = [-1] * size
    period = [0] * size
    cycles = []

    for start in range(size):
        if depth[start] >= 0:
            continue
        path = []
        position = {}
        x = start
        while depth[x] < 0 and x not in position:
            position[x] = len(path)
            path.append(x)
            x = successor[x]
        if depth[x] >= 0:
            tail_depth = depth[x]
            tail_period = period[x]
            for y in reversed(path):
                tail_depth += 1
                depth[y] = tail_depth
                period[y] = tail_period
        else:
            cycle_start = position[x]
            cycle = path[cycle_start:]
            p = len(cycle)
            cycles.append(tuple(cycle))
            for y in cycle:
                depth[y] = 0
                period[y] = p
            tail_depth = 0
            for y in reversed(path[:cycle_start]):
                tail_depth += 1
                depth[y] = tail_depth
                period[y] = p

    for mask in range(size):
        d0 = degree_parity(mask, n)
        d1 = degree_parity(successor[mask], n)
        check(d0 == d1, f"degree parity changed at n={n}, mask={mask}")
        if not any(d0):
            check(successor[mask] == mask, f"Eulerian graph moved at n={n}, mask={mask}")
        y = mask
        for _ in range(depth[mask]):
            y = successor[y]
        z = y
        for _ in range(period[mask]):
            z = successor[z]
        check(z == y, f"functional-graph certificate failed at n={n}, mask={mask}")

    fixed = sum(successor[x] == x for x in range(size))
    return {
        "n": n,
        "states": size,
        "fixed": fixed,
        "cycles": len(cycles),
        "max_depth": max(depth, default=0),
        "max_period": max(period, default=1),
        "periods": sorted({len(cycle) for cycle in cycles}),
        "successor": successor,
        "depth": depth,
        "period": period,
    }


def first_counterexample(stats, predicate):
    for data in stats:
        n = data["n"]
        for mask in range(data["states"]):
            if not predicate(data, mask):
                return n, mask, decoded_edges(mask, n)
    return None


def deterministic_samples(n, sample_count=20000, orbit_cap=300):
    """Counterexample search beyond the exact n<=6 census.

    The power-of-two modulus makes this a reproducible LCG traversal of graph
    masks; it is a sample, not an exhaustive statement.
    """
    bits = n * (n - 1) // 2
    modulus_mask = (1 << bits) - 1
    seed = (1 << (bits - 1)) | 1
    max_depth = 0
    max_period = 1
    first_period_over_two = None
    first_non_power_two = None
    for _ in range(sample_count):
        seed = (6364136223846793005 * seed + 1442695040888963407) & modulus_mask
        start = seed
        seen = {}
        path = []
        x = start
        for time in range(orbit_cap):
            if x in seen:
                depth = seen[x]
                period = time - depth
                cycle_masks = tuple(path[depth:])
                max_depth = max(max_depth, depth)
                max_period = max(max_period, period)
                if period > 2 and first_period_over_two is None:
                    first_period_over_two = (
                        start,
                        decoded_edges(start, n),
                        depth,
                        period,
                        cycle_masks,
                    )
                if period & (period - 1) and first_non_power_two is None:
                    first_non_power_two = (
                        start,
                        decoded_edges(start, n),
                        depth,
                        period,
                        cycle_masks,
                    )
                break
            seen[x] = time
            path.append(x)
            y = step(x, n)
            check(
                degree_parity(x, n) == degree_parity(y, n),
                f"sampled degree parity changed at n={n}, mask={x}",
            )
            x = y
        else:
            raise AssertionError(f"sampled orbit exceeded cap at n={n}, mask={start}")
    return {
        "n": n,
        "samples": sample_count,
        "max_depth": max_depth,
        "max_period": max_period,
        "first_period_over_two": first_period_over_two,
        "first_non_power_two": first_non_power_two,
    }


def main():
    stats = [functional_statistics(n) for n in range(0, 7)]
    samples = [deterministic_samples(n) for n in range(7, 11)]
    print("ODD-DEGREE SYNCHRONOUS LOCAL COMPLEMENT")
    for data in stats:
        print(
            "n={n} states={states} fixed={fixed} cycles={cycles} "
            "max_depth={max_depth} max_period={max_period} periods={periods}".format(**data)
        )

    involution_cex = first_counterexample(
        stats,
        lambda data, mask: data["successor"][data["successor"][mask]] == mask,
    )
    fixed_attractor_cex = first_counterexample(
        stats, lambda data, mask: data["period"][mask] == 1
    )
    degree_sequence_cex = first_counterexample(
        stats,
        lambda data, mask: sorted(x.bit_count() for x in adjacency(mask, data["n"]))
        == sorted(
            x.bit_count()
            for x in adjacency(data["successor"][mask], data["n"])
        ),
    )
    non_power_two_cycle = next(
        (
            (data["n"], p)
            for data in stats
            for p in data["periods"]
            if p & (p - 1)
        ),
        None,
    )

    print(f"first_not_involution={involution_cex}")
    print(f"first_nonfixed_attractor={fixed_attractor_cex}")
    print(f"first_degree_sequence_change={degree_sequence_cex}")
    print(f"first_non_power_of_two_cycle={non_power_two_cycle}")
    for data in samples:
        print(
            "sample n={n} samples={samples} max_depth={max_depth} "
            "max_period={max_period} first_period_over_two={first_period_over_two} "
            "first_non_power_two={first_non_power_two}".format(**data)
        )
    print(f"assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
