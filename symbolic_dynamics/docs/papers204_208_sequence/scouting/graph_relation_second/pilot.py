#!/usr/bin/env python3
"""Seven bounded, literal second-lane probes; no author/historical imports."""

from collections import Counter
from itertools import product
from functools import lru_cache
import hashlib
import json

CHECKS = Counter()


def require(value, label):
    CHECKS[label] += 1
    if not value:
        raise AssertionError(label)


def graphs(n):
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    for mask in range(1 << len(pairs)):
        edges = tuple(edge for k, edge in enumerate(pairs) if mask >> k & 1)
        neighbors = [set() for _ in range(n)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
        yield mask, edges, tuple(tuple(sorted(row)) for row in neighbors)


@lru_cache(maxsize=None)
def compositions(n, mass):
    if n == 0:
        return ((),) if mass == 0 else ()
    return tuple((first,)+tail for first in range(mass+1)
                 for tail in compositions(n-1, mass-first))


def spin(name, x, neighbors):
    if name == "ECD":
        return tuple(sum(x[u] == x[v] for u in row)
                     for v, row in enumerate(neighbors))
    if name == "LRC":
        return tuple(sum(x[u] < x[v] for u in row)
                     for v, row in enumerate(neighbors))
    if name == "CCI":
        return tuple((x[v]+1) % 3 if any(x[u] == x[v] for u in row) else x[v]
                     for v, row in enumerate(neighbors))
    raise ValueError(name)


def resource(name, x, edges, neighbors):
    y = list(x)
    if name == "MGE":
        # Each edge receives one globally consistent priority, so ties cannot
        # create a directed preference cycle. Accepted pairs are disjoint.
        def priority(u, v):
            return (abs(x[u]-x[v]), -min(u, v), -max(u, v))
        choice = [max(row, key=lambda u: priority(v, u)) if row else None
                  for v, row in enumerate(neighbors)]
        for u, v in edges:
            if choice[u] == v and choice[v] == u and abs(x[u]-x[v]) >= 2:
                high, low = (u, v) if x[u] > x[v] else (v, u)
                y[high] -= 1
                y[low] += 1
    elif name == "RMA":
        y = [0]*len(x)
        for v, row in enumerate(neighbors):
            destination = max((v,)+row, key=lambda u: (x[u], -u))
            y[destination] += x[v]
    elif name == "GLD":
        for v, row in enumerate(neighbors):
            lower = [u for u in row if x[u] < x[v]]
            if lower:
                destination = min(lower, key=lambda u: (x[u], u))
                y[v] -= 1
                y[destination] += 1
    else:
        raise ValueError(name)
    require(sum(y) == sum(x) and min(y, default=0) >= 0, "resource_carrier")
    if name == "MGE":
        require(tuple(y) == x or sum(a*a for a in y) < sum(a*a for a in x),
                "mge_strict_energy")
        require((tuple(y) == x) == all(abs(x[u]-x[v]) <= 1 for u, v in edges),
                "mge_fixed_local_lipschitz")
    if name == "RMA":
        require(tuple(y) == x or sum(a > 0 for a in y) < sum(a > 0 for a in x),
                "rma_strict_support")
        require((tuple(y) == x) == all(not (x[u] and x[v]) for u, v in edges),
                "rma_fixed_independent_support")
    return tuple(y)


def orientation(x, edges, n):
    degree = [0]*n
    for bit, (u, v) in zip(x, edges):
        degree[v if bit else u] += 1
    y = []
    for bit, (u, v) in zip(x, edges):
        tail, head = (v, u) if bit else (u, v)
        y.append(1-bit if degree[tail] > degree[head] else bit)
    return tuple(y)


def component(states, arrows, digest, label):
    state_set = set(states)
    require(all(y in state_set for y in arrows.values()), "finite_carrier")
    memo = {}
    for start in states:
        if start in memo:
            continue
        path, seen = [], {}
        x = start
        while x not in memo and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = arrows[x]
        if x in seen:
            begin = seen[x]
            period = len(path)-begin
            for y in path[begin:]:
                memo[y] = (0, period)
            path = path[:begin]
        for y in reversed(path):
            height, period = memo[arrows[y]]
            memo[y] = (height+1, period)
    fibres = Counter(arrows.values())
    for x in states:
        height, period = memo[x]
        next_height, next_period = memo[arrows[x]]
        require(next_height == max(0, height-1) and next_period == period,
                "functional_graph_consistency")
        digest.update(repr((label, x, arrows[x], height, period)).encode("ascii"))
    height = max(h for h, _ in memo.values())
    periods = sorted({p for _, p in memo.values()})
    return {"states": len(states), "image": len(fibres),
            "core": sum(h == 0 for h, _ in memo.values()),
            "fixed": sum(x == arrows[x] for x in states), "height": height,
            "periods": periods, "max_fibre": max(fibres.values()),
            "height_witness": next(x for x in states if memo[x][0] == height),
            "period_witness": next(x for x in states if memo[x][1] == max(periods))}


def summarize(name, n, pieces):
    records = [record for _, record in pieces]
    result = {"id": name, "n": n, "components": len(records)}
    for key in ("states", "image", "core", "fixed"):
        result[key] = sum(record[key] for record in records)
    for key in ("height", "max_fibre"):
        result[key] = max(record[key] for record in records)
    result["periods"] = sorted({p for record in records for p in record["periods"]})
    label, record = next((label, record) for label, record in pieces
                         if record["height"] == result["height"])
    result["height_witness"] = {"component": label, "state": record["height_witness"]}
    label, record = next((label, record) for label, record in pieces
                         if max(record["periods"]) == max(result["periods"]))
    result["largest_period_witness"] = {"component": label,
                                         "state": record["period_witness"]}
    return result


def main():
    digest = hashlib.sha256()
    rows = []
    for name in ("ECD", "LRC", "CCI", "MGE", "RMA", "GLD", "DGO"):
        for n in range(6 if name == "DGO" else 5):
            pieces = []
            for mask, edges, neighbors in graphs(n):
                if name in ("ECD", "LRC", "CCI"):
                    q = 3 if name == "CCI" else max(2, n)
                    states = tuple(product(range(q), repeat=n))
                    arrows = {x: spin(name, x, neighbors) for x in states}
                    label = (name, n, mask, q)
                    pieces.append((label, component(states, arrows, digest, label)))
                elif name == "DGO":
                    states = tuple(product((0, 1), repeat=len(edges)))
                    arrows = {x: orientation(x, edges, n) for x in states}
                    label = (name, n, mask)
                    pieces.append((label, component(states, arrows, digest, label)))
                else:
                    for mass in range(7 if n else 1):
                        states = compositions(n, mass)
                        arrows = {x: resource(name, x, edges, neighbors) for x in states}
                        label = (name, n, mask, mass)
                        pieces.append((label, component(states, arrows, digest, label)))
            rows.append(summarize(name, n, pieces))
    print(json.dumps({"scope": "SEVEN_BOUNDED_SCOUTS_NOT_THEOREMS",
                      "profiles": rows, "checks": dict(sorted(CHECKS.items())),
                      "total_checks": sum(CHECKS.values()),
                      "enumeration_sha256": digest.hexdigest(),
                      "external_status": "HOLD_EXTERNAL"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
