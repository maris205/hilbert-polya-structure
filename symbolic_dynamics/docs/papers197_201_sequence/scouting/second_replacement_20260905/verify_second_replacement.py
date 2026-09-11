#!/usr/bin/env python3
"""Bounded exact scouting. No imports from existing author/gate verifiers."""
from collections import Counter
from itertools import combinations, product
import json


CHECKS = 0


def require(test):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(CHECKS)


def functional_census(f, expected_depth=None):
    depth = [-1] * len(f)
    period = [0] * len(f)
    cycles = Counter()
    for start in range(len(f)):
        if depth[start] != -1:
            continue
        walk, seen = [], {}
        v = start
        while depth[v] == -1 and v not in seen:
            seen[v] = len(walk)
            walk.append(v)
            v = f[v]
        if depth[v] == -1:
            k = seen[v]
            cyc = walk[k:]
            cycles[len(cyc)] += 1
            for z in cyc:
                depth[z], period[z] = 0, len(cyc)
            walk = walk[:k]
        for z in reversed(walk):
            depth[z], period[z] = depth[f[z]] + 1, period[f[z]]
    fibres = Counter(f)
    if expected_depth is not None:
        require(depth == expected_depth)
    return {
        "states": len(f), "image": len(fibres),
        "depth_hist": sorted(Counter(depth).items()),
        "cycles": sorted(cycles.items()), "max_tail": max(depth),
        "max_fibre": max(fibres.values()),
        "max_targets": sorted(x for x in fibres if fibres[x] == max(fibres.values())),
        "fibre_hist_with_empty": sorted(Counter(fibres.get(x, 0) for x in range(len(f))).items()),
    }


def graph_rows(n, pairs, word):
    rows = [0] * n
    for k, (u, v) in enumerate(pairs):
        if word >> k & 1:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    return rows


def graph_boxes():
    bell = [1]
    for n in range(1, 7):
        from math import comb
        bell.append(sum(comb(n - 1, j) * bell[j] for j in range(n)))
    for n in range(7):
        pairs = tuple(combinations(range(n), 2))
        transitions = {"ND1": [], "D2G": []}
        for word in range(1 << len(pairs)):
            rows = graph_rows(n, pairs, word)
            sets = [{j for j in range(n) if rows[i] >> j & 1} for i in range(n)]
            nd = sum(1 << k for k, (u, v) in enumerate(pairs)
                     if (rows[u] ^ rows[v]).bit_count() == 1)
            nd_control = sum(1 << k for k, (u, v) in enumerate(pairs)
                             if len(sets[u] ^ sets[v]) == 1)
            require(nd == nd_control)
            require(not (nd & word))
            require(all((len(sets[u]) ^ len(sets[v])) & 1
                        for k, (u, v) in enumerate(pairs) if nd >> k & 1))
            nd_rows = graph_rows(n, pairs, nd)
            require(all(nd_rows[u] == nd_rows[v] for u, v in pairs
                        if rows[u] == rows[v]))
            d2 = sum(1 << k for k, (u, v) in enumerate(pairs)
                     if not (word >> k & 1) and rows[u] & rows[v])
            distances = []
            for u in range(n):
                dist, frontier, t = {u: 0}, {u}, 0
                while frontier:
                    t += 1
                    nxt = set().union(*(sets[z] for z in frontier)) - set(dist)
                    dist.update((z, t) for z in nxt)
                    frontier = nxt
                distances.append(dist)
            d2_control = sum(1 << k for k, (u, v) in enumerate(pairs)
                             if distances[u].get(v) == 2)
            require(d2 == d2_control)
            transitions["ND1"].append(nd)
            transitions["D2G"].append(d2)
        for name, f in transitions.items():
            require([x for x in range(len(f)) if f[x] == x] == [0])
            if name == "D2G":
                require(f.count(0) == bell[n])
            else:
                expected = {0}
                if n >= 4:
                    for center in range(n):
                        for isolated in range(n):
                            if center != isolated:
                                expected.add(sum(1 << k for k, (u, v) in enumerate(pairs)
                                                 if center in (u, v) and isolated not in (u, v)))
                require({x for x in range(len(f)) if f[f[x]] == x} == expected)
                # This proves only a bounded census, never all-n exhaustion.
            result = functional_census(f)
            result["n"] = n
            print(name, json.dumps(result, sort_keys=True, separators=(",", ":")))
        if n == 5:
            f = transitions["ND1"]
            require((f[21], f[21 | f[21]]) == (802, 72))
            print("ND1_REJECTED_INJECTION", json.dumps({"n": 5, "source": 21,
                  "target": 802, "ND1_of_source_union_target": 72}, sort_keys=True))


def sub(x, y, p):
    return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)


def dot(x, y, p):
    return (x[0] * y[0] + x[1] * y[1]) % p


def det(x, y, p):
    return (x[0] * y[1] - x[1] * y[0]) % p


def ccw_step(state, p):
    a, b, c = state
    u, v = sub(b, a, p), sub(c, a, p)
    d = det(u, v, p)
    if d == 0:
        return state
    bu = (dot(b, b, p) - dot(a, a, p)) % p
    cv = (dot(c, c, p) - dot(a, a, p)) % p
    inv = pow(2 * d, -1, p)
    o = (((bu * v[1] - cv * u[1]) * inv) % p,
         ((u[0] * cv - v[0] * bu) * inv) % p)
    require(dot(sub(a, o, p), sub(a, o, p), p)
            == dot(sub(b, o, p), sub(b, o, p), p)
            == dot(sub(c, o, p), sub(c, o, p), p))
    return (b, c, o)


def ccw_inverse(target, points, p):
    b, c, o = target
    sources = set()
    if det(sub(c, b, p), sub(o, b, p), p) == 0:
        sources.add(target)  # the whole-triple hold branch
    radius = dot(sub(b, o, p), sub(b, o, p), p)
    if radius == dot(sub(c, o, p), sub(c, o, p), p):
        for a in points:
            if det(sub(b, a, p), sub(c, a, p), p) != 0:
                if dot(sub(a, o, p), sub(a, o, p), p) == radius:
                    sources.add((a, b, c))
    return sources


def ccw_fibre_formula(target, p):
    b, c, o = target
    hold = int(det(sub(c, b, p), sub(o, b, p), p) == 0)
    radius = dot(sub(b, o, p), sub(b, o, p), p)
    if b == c or radius != dot(sub(c, o, p), sub(c, o, p), p):
        return hold
    epsilon = 1 if p % 4 == 1 else -1
    if radius != 0:
        return hold + p - epsilon - 2
    require(epsilon == 1)
    if dot(sub(c, b, p), sub(c, b, p), p) == 0:
        return hold + p - 1
    return hold + 2 * p - 3


def ccw_core(state, p):
    a, b, c = state
    if det(sub(b, a, p), sub(c, a, p), p) == 0:
        return True
    r = dot(sub(a, c, p), sub(a, c, p), p)
    return r != 0 and r == dot(sub(b, c, p), sub(b, c, p), p)


def ccw_boxes():
    for p in (3, 5):
        points = tuple(product(range(p), repeat=2))
        states = tuple(product(points, repeat=3))
        index = {x: i for i, x in enumerate(states)}
        actual = [set() for _ in states]
        f = []
        for i, state in enumerate(states):
            target = ccw_step(state, p)
            j = index[target]
            f.append(j)
            actual[j].add(state)
        for j, state in enumerate(states):
            require(ccw_inverse(state, points, p) == actual[j])
            require(ccw_fibre_formula(state, p) == len(actual[j]))
            b, c, o = state
            if ccw_core(state, p) and det(sub(c, b, p), sub(o, b, p), p) != 0:
                u, v = sub(b, o, p), sub(c, o, p)
                k = 2 * dot(u, v, p) * pow(dot(v, v, p), -1, p) % p
                a = ((o[0] + k * v[0] - u[0]) % p,
                     (o[1] + k * v[1] - u[1]) % p)
                pred = (a, b, c)
                require(ccw_core(pred, p))
                require({x for x in actual[j] if ccw_core(x, p)} == {pred})
        expected_depth = [0 if ccw_core(x, p) else
                          1 if ccw_core(states[f[i]], p) else 2
                          for i, x in enumerate(states)]
        require(all(ccw_core(states[f[f[i]]], p) for i in range(len(f))))
        result = functional_census(f, expected_depth)
        require(sum(f[i] == i for i in range(len(f))) == p**5 + p**4 - p**3)
        epsilon = 1 if p % 4 == 1 else -1
        fixed_count = p**5 + p**4 - p**3
        special_count = p**2 * (p - 1) * (p - epsilon) * (p - epsilon - 2)
        null_special_count = 2 * p**2 * (p - 1)**2 if epsilon == 1 else 0
        depth_two = null_special_count * (2 * p - 3)
        depth_one = p**6 - fixed_count - special_count - depth_two
        predicted_hist = [(0, fixed_count + special_count), (1, depth_one)]
        if depth_two:
            predicted_hist.append((2, depth_two))
        require(result["depth_hist"] == predicted_hist)
        require(result["image"] == fixed_count + special_count + null_special_count)
        require(result["max_fibre"] == (p if p % 4 == 3 else 2 * p - 3))
        maximum = set(result["max_targets"])
        predicted = set()
        for j, (b, c, o) in enumerate(states):
            u, v = sub(b, o, p), sub(c, o, p)
            if p % 4 == 3:
                is_max = b != o and c == ((2 * o[0] - b[0]) % p, (2 * o[1] - b[1]) % p)
            else:
                is_max = u != (0, 0) and v != (0, 0) and dot(u, u, p) == dot(v, v, p) == 0 and det(u, v, p) != 0
            if is_max:
                predicted.add(j)
        require(predicted == maximum)
        require(len(maximum) == (p**2 * (p**2 - 1) if p % 4 == 3 else 2 * p**2 * (p - 1)**2))
        result["p"] = p
        result["max_targets_count"] = len(result.pop("max_targets"))
        print("CCW", json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    graph_boxes()
    ccw_boxes()
    print("ASSERTIONS", CHECKS)
    print("STATUS SCOUTING_ONLY_NO_ADMISSION")
