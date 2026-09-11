#!/usr/bin/env python3
"""Independent tuple-edge trace pressure, n<=6 only; no author imports."""
from itertools import combinations
from collections import Counter


def choose(edges, triples):
    for tri in triples:
        bits = [edge in edges for edge in combinations(tri, 2)]
        if len(set(bits)) == 1:
            return tri, bits[0]
    return None, None


def trace(n, edges):
    triples = tuple(combinations(range(n), 3))
    result = []
    while True:
        tri, colour = choose(edges, triples)
        if tri is None:
            return result
        result.append((tri, colour))
        after = edges ^ set(combinations(tri, 2))
        nxt, _ = choose(after, triples)
        if nxt == tri:
            return result
        edges = after


def main():
    for n in range(7):
        pairs = tuple(combinations(range(n), 2))
        counts = Counter()
        examples = {}
        for code in range(1 << len(pairs)):
            edges = {e for i, e in enumerate(pairs) if code >> i & 1}
            path = trace(n, edges)
            tris = [set(t) for t, c in path]
            minima = [min(t) for t in tris]
            switches = tuple(i for i in range(len(minima)-1) if minima[i+1] < minima[i])
            common = set.intersection(*tris) if tris else set()
            counts[(len(switches), bool(common))] += 1
            key = (len(switches), bool(common))
            examples.setdefault(key, (code, path))
            if any(i > 0 for i in switches):
                examples.setdefault('late_anchor_change', (code, path))
            if len(switches) > 1:
                examples.setdefault('multiple_anchor_change', (code, path))
            retired = set()
            for a, b in zip(tris, tris[1:]):
                if b & retired:
                    raise AssertionError(('RETURN',n,code,path))
                retired |= a-b
        print(n, 'profiles', sorted(counts.items()), 'examples', examples)
    for n in range(3, 61):
        v = list(reversed(range(1, n)))
        s = [0, 0] + [(i-1) % 2 for i in range(2, n-1)]
        edges = {(0, v[i]) for i in range(n-1) if s[i]}
        for i, j in combinations(range(n-1), 2):
            colour = (i % 2 if j == i+1 else
                      1-s[i] if s[i] == s[j] else s[i])
            if colour:
                edges.add(tuple(sorted((v[i], v[j]))))
        observed = trace(n, edges)
        expected = [(tuple(sorted((0, v[t], v[t+1]))), bool(t % 2))
                    for t in range(n-2)]
        assert observed == expected, (n, observed, expected)
    print('sharp_family_n3..60=PASS; no_full_graph_boxes_above6')


if __name__ == '__main__':
    main()
