#!/usr/bin/env python3
"""Eight bounded literal-map probes. No theorem or owner verdict is inferred.

All carriers are complete, labelled, finite, and include their empty boundary.
This program imports only the standard library and no historical verifier.
"""

from collections import Counter
from itertools import combinations
import json


CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError("pilot consistency failure")


def members(bits):
    out = []
    while bits:
        bit = bits & -bits
        out.append(bit.bit_length() - 1)
        bits ^= bit
    return out


def family_update(state, mode):
    sets = members(state)
    result = 0
    if mode == "DI":
        for a, b in combinations(sets, 2):
            result |= 1 << (a & b)
    elif mode == "DR":
        for a in sets:
            for b in sets:
                if a != b:
                    result |= 1 << (a & ~b)
    elif mode == "SX":
        for a, b in combinations(sets, 2):
            result |= 1 << (a ^ b)
    elif mode == "M3":
        for a, b, c in combinations(sets, 3):
            result |= 1 << ((a & b) | (a & c) | (b & c))
    else:
        raise ValueError(mode)
    return result


def relation_update(state, n, mode):
    full = (1 << n) - 1
    rows = [(state >> (n * i)) & full for i in range(n)]
    result = 0
    for i in range(n):
        left = right = square = 0
        for k in range(n):
            if (rows[i] >> k) & 1:
                left |= full ^ rows[k]
                square |= rows[k]
            else:
                right |= rows[k]
        if mode == "BRC":
            row = left
        elif mode == "ECP":
            row = square ^ rows[i]
        elif mode == "DCR":
            row = left & ~right
        else:
            raise ValueError(mode)
        result |= row << (n * i)
    return result


def strict_neighborhood_graph(state, n):
    edges = list(combinations(range(n), 2))
    rows = [0] * n
    for bit, (u, v) in enumerate(edges):
        if (state >> bit) & 1:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    result = 0
    for bit, (u, v) in enumerate(edges):
        a, b = rows[u], rows[v]
        if a != b and ((a & b) == a or (a & b) == b):
            result |= 1 << bit
    return result


def profile(name, n, width, update):
    count = 1 << width
    successor = [update(x) for x in range(count)]
    indegree = [0] * count
    for y in successor:
        check(0 <= y < count)
        indegree[y] += 1
    depth = [-1] * count
    period = [0] * count
    cycles = Counter()
    for start in range(count):
        if depth[start] >= 0:
            continue
        path, pos = [], {}
        x = start
        while depth[x] < 0 and x not in pos:
            pos[x] = len(path)
            path.append(x)
            x = successor[x]
        if depth[x] < 0:
            cut = pos[x]
            cycle = path[cut:]
            cycles[len(cycle)] += 1
            for v in cycle:
                depth[v] = 0
                period[v] = len(cycle)
            path = path[:cut]
        for v in reversed(path):
            depth[v] = depth[successor[v]] + 1
            period[v] = period[successor[v]]
    for x, y in enumerate(successor):
        check(period[x] == period[y])
        check(depth[x] == 0 or depth[x] == depth[y] + 1)
        check((x == y) == (depth[x] == 0 and period[x] == 1))
    maximum = max(indegree)
    maximizers = [x for x, d in enumerate(indegree) if d == maximum]
    check(sum(indegree) == count)
    check(sum(k * v for k, v in cycles.items()) == depth.count(0))
    print(json.dumps({
        "id": name, "n": n, "states": count,
        "image": sum(d > 0 for d in indegree),
        "recurrent": depth.count(0), "H": max(depth),
        "cycle_lengths": dict(sorted(cycles.items())),
        "depths": dict(sorted(Counter(depth).items())),
        "max_fibre": maximum, "maximizer_count": len(maximizers),
        "maximizer_first": maximizers[:8],
        "deepest_first": depth.index(max(depth)),
    }, sort_keys=True), flush=True)


def main():
    print("scope=EIGHT_EXPLICIT_BOUNDED_PROBES_NOT_ADMITTED_SYSTEMS", flush=True)
    for mode in ("DI", "DR", "SX", "M3"):
        for n in range(5):
            profile(mode, n, 1 << n,
                    lambda x, mode=mode: family_update(x, mode))
    for mode in ("BRC", "ECP", "DCR"):
        for n in range(5):
            profile(mode, n, n * n,
                    lambda x, n=n, mode=mode: relation_update(x, n, mode))
    for n in range(7):
        profile("SND", n, n * (n - 1) // 2,
                lambda x, n=n: strict_neighborhood_graph(x, n))
    print(f"assertions={CHECKS}")
    print("status=PASS_BOUNDED_CONTROL_ONLY")
    print("theorems=NONE_CLAIMED; owner_gate=NOT_COMPLETED; HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
