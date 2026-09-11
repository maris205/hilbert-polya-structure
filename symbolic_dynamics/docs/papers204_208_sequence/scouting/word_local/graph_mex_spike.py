#!/usr/bin/env python3
"""Pressure a general-graph mex clock; graphs are undirected and loopless."""
from itertools import combinations, product
from random import Random
import json
from pilot import mex, profile


def step(w, adj):
    return tuple(mex({w[j] for j in neighbors}) for neighbors in adj)


def make_adj(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def orbit(w, adj):
    seen = {}
    while w not in seen:
        seen[w] = len(seen)
        w = step(w, adj)
    return seen[w], len(seen)-seen[w]


def main():
    for n in range(1, 6):
        universe = list(combinations(range(n), 2))
        best, total = {}, 0
        for mask in range(1 << len(universe)):
            edges = [e for k, e in enumerate(universe) if mask >> k & 1]
            adj = make_adj(n, edges)
            degree = max(map(len, adj))
            q = max(3, degree+1)
            report = profile(product(range(q), repeat=n), lambda w: step(w, adj))
            total += report['states']
            assert max(map(int, report['cycles'])) <= 2
            assert report['height'] <= max(1, degree), (edges, report)
            if degree not in best or report['height'] > best[degree]['height']:
                best[degree] = dict(height=report['height'], edges=edges,
                                    witness=report['witness'])
        print(json.dumps(dict(test='all_graphs_full_colours', n=n,
                              states=total, best=best), sort_keys=True))
    rng = Random(205)
    for n in (6, 8, 12, 20):
        best = {}
        for trial in range(5000):
            edges = [e for e in combinations(range(n), 2) if rng.randrange(2)]
            adj = make_adj(n, edges)
            degree = max(map(len, adj))
            q = max(3, degree+1)
            w = tuple(rng.randrange(q) for _ in range(n))
            h, p = orbit(w, adj)
            assert p <= 2
            assert h <= max(1, degree)
            if degree not in best or h > best[degree]['height']:
                best[degree] = dict(height=h, edges=edges, witness=w)
        print(json.dumps(dict(test='random_graph_sources', n=n, trials=5000,
                              seed=205, best=best), sort_keys=True))


if __name__ == '__main__':
    main()
