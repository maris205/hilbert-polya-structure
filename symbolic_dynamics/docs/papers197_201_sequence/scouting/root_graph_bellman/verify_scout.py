#!/usr/bin/env python3
"""Exact scout for synchronous graph Bellman-envelope dynamics.

This is deliberately dependency-free.  It checks every labelled simple graph
through four vertices, heights through three, every state, every time through
stabilisation, and the all-time every-target inclusion--exclusion formula.
Finite checks are counterexample pressure, not proofs.
"""

from __future__ import annotations

from itertools import combinations, product


def graphs(n: int):
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        adj = [set() for _ in range(n)]
        for j, (u, v) in enumerate(edges):
            if mask >> j & 1:
                adj[u].add(v)
                adj[v].add(u)
        yield tuple(tuple(sorted(a)) for a in adj)


def distances(adj):
    n = len(adj)
    inf = n + 1
    out = [[inf] * n for _ in range(n)]
    for s in range(n):
        out[s][s] = 0
        queue = [s]
        for u in queue:
            for v in adj[u]:
                if out[s][v] == inf:
                    out[s][v] = out[s][u] + 1
                    queue.append(v)
    return out


def update(x, adj):
    return tuple(min([x[v]] + [x[u] + 1 for u in adj[v]]) for v in range(len(x)))


def iterate_formula(x, dist, t):
    n = len(x)
    return tuple(min(x[u] + dist[v][u] for u in range(n) if dist[v][u] <= t)
                 for v in range(n))


def fibre_formula(y, dist, h, t):
    n = len(y)
    lower = []
    for u in range(n):
        lower.append(max([0] + [y[v] - dist[v][u]
                                for v in range(n) if dist[v][u] <= t]))
    total = 0
    for mask in range(1 << n):
        sign = -1 if mask.bit_count() & 1 else 1
        ways = 1
        for u in range(n):
            threshold = lower[u]
            for v in range(n):
                if mask >> v & 1 and dist[v][u] <= t:
                    threshold = max(threshold, y[v] - dist[v][u] + 1)
            ways *= max(0, h - threshold + 1)
        total += sign * ways
    return total


def tail(x, adj):
    t = 0
    while True:
        z = update(x, adj)
        if z == x:
            return t
        x = z
        t += 1


def diameter(dist):
    n = len(dist)
    return max([0] + [dist[u][v] for u in range(n) for v in range(n)
                      if dist[u][v] <= n])


def main():
    assertions = 0
    boxes = 0
    for n in range(1, 5):
        for adj in graphs(n):
            dist = distances(adj)
            diam = diameter(dist)
            for h in range(4):
                states = list(product(range(h + 1), repeat=n))
                actual = {}
                for x in states:
                    orbit = [x]
                    for t in range(diam + 2):
                        if t:
                            orbit.append(update(orbit[-1], adj))
                        assert orbit[t] == iterate_formula(x, dist, t)
                        assertions += 1
                    assert orbit[-1] == orbit[-2]
                    assertions += 1
                    actual[x] = orbit

                    fixed = update(x, adj) == x
                    lipschitz = all(abs(x[u] - x[v]) <= 1
                                    for u in range(n) for v in adj[u])
                    assert fixed == lipschitz
                    assertions += 1

                observed_height = max(tail(x, adj) for x in states)
                assert observed_height == min(diam, max(0, h - 1))
                assertions += 1

                for t in range(diam + 2):
                    counts = {y: 0 for y in states}
                    for x in states:
                        counts[actual[x][t]] += 1
                    for y in states:
                        assert fibre_formula(y, dist, h, t) == counts[y]
                        assertions += 1
                    assert sum(counts.values()) == len(states)
                    assertions += 1
                boxes += 1

    print("graph_bellman_scout=PASS")
    print(f"boxes={boxes}")
    print(f"assertions={assertions}")
    print("n<=4; all labelled simple graphs; 0<=h<=3")
    print("checks=all-time_formula,fixed_lipschitz,sharp_height,all-time_every-target_fibres,mass")


if __name__ == "__main__":
    main()
