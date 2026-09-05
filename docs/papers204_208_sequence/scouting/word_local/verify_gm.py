#!/usr/bin/env python3
"""Self-contained author audit of the bounded GM proof contract."""
from collections import Counter
from itertools import combinations, product
from math import comb
import hashlib
import json


checks = Counter()


def require(value, label, evidence=None):
    checks[label] += 1
    if not value:
        raise AssertionError((label, evidence))


def adjacency(n, edges):
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    return neighbors


def update(c, neighbors):
    result = []
    for nb in neighbors:
        present = 0
        for u in nb:
            present |= 1 << c[u]
        k = 0
        while (present >> k) & 1:
            k += 1
        result.append(k)
    return tuple(result)


def sharp_graph(d):
    colors = list(range(1, d+1)) + [0, 0]
    edges = [(k, k+1) for k in range(d-1)] + [(0, d), (d, d+1)]
    for k in range(2, d+1):
        for j in range(k-1):
            first = len(colors)
            colors.extend(range(j+1))
            edges.extend(combinations(range(first, first+j+1), 2))
            edges.append((k-1, first+j))
    return tuple(colors), adjacency(len(colors), edges)


def main():
    graph_count = source_count = 0
    digest = hashlib.sha256()
    for n in range(5):
        universe = list(combinations(range(n), 2))
        for mask in range(1 << len(universe)):
            edges = [e for k, e in enumerate(universe) if mask >> k & 1]
            neighbors = adjacency(n, edges)
            degrees = list(map(len, neighbors))
            degree = max(degrees, default=0)
            isolated = degrees.count(0)
            graph_count += 1
            for q in (max(3, degree+1), max(3, degree+1)+1):
                states = list(product(range(q), repeat=n))
                arrows = {c: update(c, neighbors) for c in states}
                counts = Counter(arrows.values())
                require(sum(counts.values()) == q**n, 'mass')
                bound = q**isolated * (q-1)**(n-isolated)
                require(max(counts.values()) == bound, 'max_fibre')
                require([y for y in counts if counts[y] == bound] == [(0,)*n],
                        'unique_maximizer', (n, edges, q))
                for c in states:
                    source_count += 1
                    path = [c, arrows[c]]
                    for t in range(max(1, degree)+1):
                        path.append(arrows[path[-1]])
                        now, later = path[t], path[t+2]
                        require(all(b <= a for a, b in zip(now, later)),
                                'two_step_descent')
                        for v, (a, b) in enumerate(zip(now, later)):
                            require(b == a or a >= t+1, 'strict_drop_colour')
                            if t >= max(1, degrees[v]):
                                require(a == b, 'local_deadline')
                    require(path[max(1, degree)] == path[max(1, degree)+2],
                            'global_deadline')
                    digest.update(bytes(c))
                    digest.update(bytes(arrows[c]))
                for y, count in counts.items():
                    palette_product = 1
                    for nb in neighbors:
                        palette_product *= q-len({y[v] for v in nb})
                    require(count <= palette_product <= bound, 'fibre_bounds')
    witnesses = []
    for d in range(2, 25):
        initial, neighbors = sharp_graph(d)
        require(len(initial) == d+2+comb(d+1, 3), 'sharp_size')
        require(max(map(len, neighbors)) == d, 'sharp_degree')
        c, history = initial, []
        for t in range(2*d+4):
            expected = list(initial)
            for k in range(1, d+1):
                expected[k-1] = k-int(t >= k+1 and (t-k-1) % 2 == 0)
            expected[d] = 0 if t % 2 == 0 else (2 if t == 1 else 1)
            expected[d+1] = t % 2
            require(c == tuple(expected), 'sharp_complete_orbit', (d, t, c))
            history.append(c)
            c = update(c, neighbors)
        require(history[d-1] != history[d+1], 'sharp_not_early')
        require(history[d] == history[d+2], 'sharp_entrance')
        witnesses.append(dict(degree=d, vertices=len(initial), height=d))
    require(update((0, 2), [[1], [0]]) == (0, 1), 'degree_one_witness')
    require(update((0, 1), [[1], [0]]) == (0, 1), 'degree_one_fixed')
    print(json.dumps(dict(audit='GM_author_v1', graphs=graph_count,
                          graph_palette_sources=source_count,
                          enumeration_sha256=digest.hexdigest(),
                          checks=dict(sorted(checks.items())),
                          total_checks=sum(checks.values()),
                          sharp_witnesses=witnesses), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
