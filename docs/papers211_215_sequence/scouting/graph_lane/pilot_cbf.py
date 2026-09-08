#!/usr/bin/env python3
"""Author-only CBF census, fixed all-graph boxes n=0,...,6; JSONL stdout."""
import itertools
import json
import sys

CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def bridge_data(n, edges, mask):
    adj = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        if mask >> j & 1:
            adj[u].append((v, j))
            adj[v].append((u, j))
    times = [-1] * n
    lows = [0] * n
    tick = 0
    bridges = 0
    components = 0

    def visit(u, parent):
        nonlocal tick, bridges
        times[u] = lows[u] = tick
        tick += 1
        for v, j in adj[u]:
            if j == parent:
                continue
            if times[v] < 0:
                visit(v, j)
                lows[u] = min(lows[u], lows[v])
                if lows[v] > times[u]:
                    bridges |= 1 << j
            else:
                lows[u] = min(lows[u], times[v])

    for u in range(n):
        if times[u] < 0:
            components += 1
            visit(u, -1)
    return bridges, components


def forest(n, edges, mask):
    roots = list(range(n))

    def root(u):
        while roots[u] != u:
            u = roots[u]
        return u

    for j, (u, v) in enumerate(edges):
        if mask >> j & 1:
            a, b = root(u), root(v)
            if a == b:
                return False
            roots[a] = b
    return True


def rgs(n):
    if n == 0:
        yield ()
        return

    def extend(a, maximum):
        if len(a) == n:
            yield tuple(a)
        else:
            for k in range(maximum + 2):
                yield from extend(a + [k], max(k, maximum))

    yield from extend([0], 0)


def profiles(nexts):
    depths = [-1] * len(nexts)
    periods = [0] * len(nexts)
    cycles = []
    for start in range(len(nexts)):
        if depths[start] >= 0:
            continue
        walk = []
        pos = {}
        v = start
        while depths[v] < 0 and v not in pos:
            pos[v] = len(walk)
            walk.append(v)
            v = nexts[v]
        if v in pos:
            cut = pos[v]
            cycle = walk[cut:]
            least = cycle.index(min(cycle))
            cycles.append(cycle[least:] + cycle[:least])
            for u in cycle:
                depths[u] = 0
                periods[u] = len(cycle)
            walk = walk[:cut]
        for u in reversed(walk):
            depths[u] = depths[nexts[u]] + 1
            periods[u] = periods[nexts[u]]
    return depths, periods, sorted(cycles)


def partition_count(n, edges, mask, parts):
    total = 0
    fedges = [(u, v) for j, (u, v) in enumerate(edges) if mask >> j & 1]
    for labels, weight in parts:
        roots = list(range(max(labels, default=-1) + 1))

        def root(a):
            while roots[a] != a:
                a = roots[a]
            return a

        for u, v in fedges:
            a, b = root(labels[u]), root(labels[v])
            if a == b:
                break
            roots[a] = b
        else:
            total += weight
    return total


def emit(item):
    print(json.dumps(item, sort_keys=True, separators=(",", ":")))


def main():
    bcounts = []
    total_states = 0
    for n in range(7):
        edges = list(itertools.combinations(range(n), 2))
        size = 1 << len(edges)
        full = size - 1
        bdata = [bridge_data(n, edges, g) for g in range(size)]
        bridges = [a for a, _ in bdata]
        bcounts.append(sum(a == 0 and c == 1 for a, c in bdata))
        nexts = [full ^ a for a in bridges]
        indegrees = [0] * size
        for h in nexts:
            indegrees[h] += 1
        depths, periods, cycles = profiles(nexts)
        parts = []
        for labels in rgs(n):
            sizes = [labels.count(i) for i in range(max(labels, default=-1) + 1)]
            weight = 1
            for k in sizes:
                weight *= bcounts[k]
            if weight:
                parts.append((labels, weight))
        for g in range(size):
            check(bridges[g] & g == bridges[g])
            check(forest(n, edges, bridges[g]))
            check((indegrees[full ^ g] > 0) == forest(n, edges, g))
            check(indegrees[full ^ g] == partition_count(n, edges, g, parts))
            check(periods[g] in (1, 2))
            if n >= 5:
                check(bridges[nexts[g]].bit_count() <= 1)
                check(nexts[nexts[nexts[g]]] == full)
                predicted = 0 if g == full else (1 if not bridges[g] else (2 if not bridges[nexts[g]] else 3))
                check(depths[g] == predicted)
            emit({"kind": "state", "n": n, "source": g, "next": nexts[g], "depth": depths[g], "period": periods[g], "indegree": indegrees[g]})
        expected_height = 0 if n <= 2 else (1 if n == 3 else 3)
        check(max(depths) == expected_height)
        maxima = [g for g, a in enumerate(indegrees) if a == max(indegrees)]
        if n >= 3:
            check(maxima == [full])
        if n >= 5:
            check(cycles == [[full]])
        if n == 4:
            check(sum(len(c) for c in cycles) == 13)
            check(sum(len(c) == 2 for c in cycles) == 6)
        total_states += size
        emit({"kind": "box", "n": n, "states": size, "image": sum(a > 0 for a in indegrees), "height": max(depths), "max_fibre": max(indegrees), "max_targets": maxima, "cycles": cycles, "connected_bridgeless": bcounts[n]})
    emit({"kind": "complete", "states": total_states, "checks": CHECKS, "scope": "CBF only, all n=0,...,6; author finite evidence"})


if __name__ == "__main__":
    main()
