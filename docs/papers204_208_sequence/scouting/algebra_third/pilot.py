#!/usr/bin/env python3
"""Bounded literal-map scout, not a proof or independent review.

Standard-library only. States are lexicographically enumerated in each full
carrier. A generic Kahn deletion/cycle traversal computes functional graphs.
No imported candidate, manuscript, or prior-scout code.
"""

from collections import Counter, deque
from hashlib import sha256
from itertools import permutations, product
import json


def graph_report(label, parameters, states, update, check=None):
    index = {state: i for i, state in enumerate(states)}
    successor = [index[update(state)] for state in states]
    n = len(states)
    fibres = Counter(successor)
    degree = [fibres.get(i, 0) for i in range(n)]
    queue = deque(i for i, d in enumerate(degree) if d == 0)
    peeled = []
    while queue:
        v = queue.popleft()
        peeled.append(v)
        w = successor[v]
        degree[w] -= 1
        if degree[w] == 0:
            queue.append(w)
    depth = [0] * n
    period = [0] * n
    cycle_histogram = Counter()
    for v in range(n):
        if degree[v] and not period[v]:
            cycle = [v]
            w = successor[v]
            while w != v:
                cycle.append(w)
                w = successor[w]
            for w in cycle:
                period[w] = len(cycle)
            cycle_histogram[len(cycle)] += 1
    for v in reversed(peeled):
        depth[v] = depth[successor[v]] + 1
        period[v] = period[successor[v]]
    assert all(period)
    assert sum(k * v for k, v in cycle_histogram.items()) == n - len(peeled)
    maximum = max(fibres.values())
    maximal_targets = [i for i in range(n) if fibres.get(i, 0) == maximum]
    if check is not None:
        check(states, successor, fibres, index)
    payload = {
        "map": label,
        "parameters": parameters,
        "states": n,
        "image": len(fibres),
        "core": n - len(peeled),
        "height": max(depth),
        "depth_histogram": sorted(Counter(depth).items()),
        "strict_cycle_histogram": sorted(cycle_histogram.items()),
        "one_step_fibre_histogram": sorted(Counter(fibres.get(i, 0) for i in range(n)).items()),
        "maximum_fibre": maximum,
        "maximum_targets": len(maximal_targets),
        "lex_first_maximum_target": states[maximal_targets[0]],
        "successor_sha256": sha256(json.dumps(successor, separators=(",", ":")).encode()).hexdigest(),
        "structural_control": "PASS" if check else "not_claimed",
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")), flush=True)


def st(n, p):
    states = list(product(range(p), repeat=n * n))
    def update(a):
        return tuple((sum(a[i*n+k] * a[k*n+j] for k in range(n)) + a[j*n+i]) % p
                     for i in range(n) for j in range(n))
    graph_report("ST", {"n": n, "p": p}, states, update)


def hn(p):
    states = list(product(range(p), repeat=2))
    def update(a):
        x, y = a
        return y, (y*y-x) % p
    def check(states, successor, fibres, index):
        assert len(fibres) == len(states) and set(fibres.values()) == {1}
        for u, v in states:
            assert update(((u*u-v) % p, u)) == (u, v)
    graph_report("HN", {"p": p}, states, update, check)


def group_tables(d):
    elements = list(permutations(range(d)))
    index = {g: i for i, g in enumerate(elements)}
    identity = index[tuple(range(d))]
    table = [[index[tuple(g[h[k]] for k in range(d))] for h in elements] for g in elements]
    inverse = [next(j for j in range(len(elements)) if table[i][j] == identity)
               for i in range(len(elements))]
    return elements, identity, table, inverse


def eg(d):
    elements, identity, mul, inv = group_tables(d)
    order = len(elements)
    states = list(product(range(order), repeat=2))
    def update(state):
        g, h = state
        return h, mul[mul[mul[g][h]][inv[g]]][inv[h]]
    def check(states, successor, fibres, index):
        for h, k in states:
            conjugacy_class = {mul[mul[g][h]][inv[g]] for g in range(order)}
            centralizer = sum(mul[g][h] == mul[h][g] for g in range(order))
            expected = centralizer if mul[k][h] in conjugacy_class else 0
            assert fibres.get(index[h, k], 0) == expected
    graph_report("EG", {"symmetric_degree": d}, states, update, check)


def rc(p):
    states = list(product(range(p), repeat=p))
    def update(a):
        return tuple(((j+1)*a[j+1] if j+1 < p else 0)
                     % p + sum(a[k] * a[j-k] for k in range(j+1))
                     for j in range(p))
    def reduced(a):
        return tuple(v % p for v in update(a))
    graph_report("RC", {"p": p, "ring": "Fp[X]/(X^p)"}, states, reduced)


def lv(n, p):
    states = list(product(range(p), repeat=n))
    def update(a):
        return tuple(a[i] * (a[(i+1) % n]-a[(i-1) % n]) % p for i in range(n))
    def check(states, successor, fibres, index):
        assert all(sum(states[j]) % p == 0 for j in successor)
        if n == 3 and p == 2:
            for a in states:
                b = update(a)
                assert update(b) == b
    graph_report("LV", {"n": n, "p": p}, states, update, check)


def nd(d, length):
    elements, identity, mul, inv = group_tables(d)
    order = len(elements)
    states = list(product(range(order), repeat=length))
    def update(a):
        return tuple(mul[inv[a[i]]][a[(i+1) % length]] for i in range(length))
    def check(states, successor, fibres, index):
        for a in states:
            total = identity
            for g in a:
                total = mul[total][g]
            expected = order if total == identity else 0
            assert fibres.get(index[a], 0) == expected
    graph_report("ND", {"symmetric_degree": d, "length": length}, states, update, check)


def main():
    for p, sizes in [(2, (1, 2, 3)), (3, (1, 2, 3)), (5, (1, 2))]:
        for n in sizes:
            st(n, p)
    for p in (2, 3, 5, 7, 11, 13):
        hn(p)
    for d in (2, 3, 4):
        eg(d)
    for p in (2, 3, 5):
        rc(p)
    for n, primes in [(3, (2, 3, 5, 7)), (4, (2, 3)), (5, (2, 3))]:
        for p in primes:
            lv(n, p)
    for d, lengths in [(2, (3, 4, 5)), (3, (3, 4)), (4, (3,))]:
        for length in lengths:
            nd(d, length)


if __name__ == "__main__":
    main()
