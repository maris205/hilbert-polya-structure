#!/usr/bin/env python3
"""Six literal fourth-lane pilots, bounded full carriers and raw JSON.

No all-parameter theorem is inferred from these functional graphs.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from math import prod

checks = 0
digest = sha256()


def require(statement):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(checks)


def analyze(tag, parameter, states, update):
    states = list(states)
    index = {state: i for i, state in enumerate(states)}
    require(len(index) == len(states))
    targets = [update(state) for state in states]
    require(all(target in index for target in targets))
    forward = [index[target] for target in targets]
    indegree = Counter(forward)
    tail = [-1] * len(states)
    period = [-1] * len(states)
    cycles = Counter()
    for start in range(len(states)):
        if tail[start] >= 0:
            continue
        path = []
        seen = {}
        current = start
        while tail[current] < 0 and current not in seen:
            seen[current] = len(path)
            path.append(current)
            current = forward[current]
        if tail[current] < 0:
            beginning = seen[current]
            cyc = path[beginning:]
            cycles[len(cyc)] += 1
            for vertex in cyc:
                tail[vertex] = 0
                period[vertex] = len(cyc)
            path = path[:beginning]
        for vertex in reversed(path):
            tail[vertex] = tail[forward[vertex]] + 1
            period[vertex] = period[forward[vertex]]
    for i, nxt in enumerate(forward):
        require((tail[i] == 0 and tail[nxt] == 0) or tail[nxt] == tail[i] - 1)
        require(period[nxt] == period[i])
        digest.update(json.dumps([tag, parameter, states[i], targets[i], tail[i], period[i]],
                                 separators=(",", ":")).encode())
        digest.update(b"\n")
    maximum_fibre = max(indegree.values())
    height = max(tail)
    maximizing = [states[i] for i in range(len(states)) if indegree[i] == maximum_fibre]
    if tag == "DPF":
        n = parameter["nonroot_vertices"]
        for state, target in zip(states, targets):
            require(all(b <= a for a, b in zip(state, target)))
        for i, profile in enumerate(states):
            choices = prod(1 if value == 0 else sum(previous == value - 1
                           for previous in profile[:position])
                           for position, value in enumerate(profile))
            require(indegree[i] == choices)
        expected_fixed = 1 if n == 0 else sum((k + 1) ** (n - k) - k ** (n - k)
                                               for k in range(n))
        require(cycles == Counter({1: expected_fixed}))
    elif tag == "CRS":
        p = parameter["prime"]
        full = (1 << p) - 1
        for state, target in zip(states, targets):
            require(not (state & target))
            if state not in (0, full):
                require(target.bit_count() < state.bit_count())
        require(cycles == Counter({2: 1}) and height <= p - 1)
    elif tag == "SEN":
        full = (1 << (1 << parameter["dimension"])) - 1
        for state, target in zip(states, targets):
            require(target == targets[index[state ^ full]])
    elif tag == "UEX" and parameter["k"] == 2:
        n = parameter["n"]
        edges = list(combinations(range(n), 2))
        for state, target in zip(states, targets):
            degrees = [sum(bool((state >> i) & 1) and vertex in edge
                           for i, edge in enumerate(edges)) for vertex in range(n)]
            direct = sum(1 << i for i, (a, b) in enumerate(edges)
                         if degrees[a] + degrees[b] - 2 * ((state >> i) & 1) == 1)
            require(direct == target)
    elif tag == "IDR":
        n = parameter["n"]
        require(cycles == Counter({1: 1}))
        require(height <= (n - 1).bit_length() if n else height == 0)
    return {"rule": tag, "parameter": parameter, "states": len(states),
            "image": len(indegree), "recurrent": sum(t == 0 for t in tail),
            "cycles_by_length": dict(sorted(cycles.items())),
            "height": height, "deepest_count": sum(t == height for t in tail),
            "deepest_witness": states[tail.index(height)],
            "maximum_fibre": maximum_fibre, "maximizer_count": len(maximizing),
            "maximizer_witness": maximizing[0]}


def depth_parent(parent):
    depth = [0]
    for predecessor in parent:
        depth.append(depth[predecessor] + 1)
    return tuple(value - 1 for value in depth[1:])


def exchange_graph(n, k):
    vertices = list(combinations(range(n), k))
    neighbourhoods = []
    for vertex in vertices:
        neighbours = sum(1 << j for j, other in enumerate(vertices)
                         if len(set(vertex).intersection(other)) == k - 1)
        neighbourhoods.append(neighbours)
    return neighbourhoods


def critical_roots(subset, p):
    coefficients = [1]
    for root in range(p):
        if (subset >> root) & 1:
            following = [0] * (len(coefficients) + 1)
            for degree, value in enumerate(coefficients):
                following[degree] = (following[degree] - root * value) % p
                following[degree + 1] = (following[degree + 1] + value) % p
            coefficients = following
    derivative = [(degree * coefficients[degree]) % p
                  for degree in range(1, len(coefficients))]
    # The derivative of the empty product is identically zero: every field
    # point is a root. This is part of the literal rule, not a hold guard.
    target = 0
    for point in range(p):
        value = 0
        for coefficient in reversed(derivative):
            value = (value * point + coefficient) % p
        if value == 0:
            target |= 1 << point
    return target


def circumcenter_table(p):
    points = list(product(range(p), repeat=2))
    triples = []
    for i, j, k in combinations(range(len(points)), 3):
        a, b, c = points[i], points[j], points[k]
        row1 = tuple((2 * (b[d] - a[d])) % p for d in range(2))
        row2 = tuple((2 * (c[d] - a[d])) % p for d in range(2))
        det = (row1[0] * row2[1] - row1[1] * row2[0]) % p
        if not det:
            continue
        norm = lambda point: sum(value * value for value in point) % p
        rhs1, rhs2 = (norm(b) - norm(a)) % p, (norm(c) - norm(a)) % p
        inv = pow(det, -1, p)
        centre = (((rhs1 * row2[1] - row1[1] * rhs2) * inv) % p,
                  ((row1[0] * rhs2 - rhs1 * row2[0]) * inv) % p)
        require(all(sum((point[d] - centre[d]) ** 2 for d in range(2)) % p ==
                    sum((a[d] - centre[d]) ** 2 for d in range(2)) % p
                    for point in (b, c)))
        triples.append(((1 << i) | (1 << j) | (1 << k), 1 << points.index(centre)))
    return triples


def circumcenter_image(subset, table):
    target = 0
    for triple, centre in table:
        if subset & triple == triple:
            target |= centre
    return target


def sensitivity_one(function, dimension):
    target = 0
    for point in range(1 << dimension):
        value = (function >> point) & 1
        sensitivity = sum(((function >> (point ^ (1 << direction))) & 1) != value
                          for direction in range(dimension))
        if sensitivity == 1:
            target |= 1 << point
    return target


def poset_data(n):
    pairs = list(combinations(range(n), 2))
    locations = {pair: i for i, pair in enumerate(pairs)}
    implications = [(1 << locations[(i, j)], 1 << locations[(j, k)],
                     1 << locations[(i, k)]) for i, j, k in combinations(range(n), 3)]
    states = [mask for mask in range(1 << len(pairs))
              if all(not (mask & a and mask & b) or mask & c for a, b, c in implications)]
    return pairs, locations, states


def diamond_interval(relation, pairs, locations):
    target = 0
    def comparable(a, b):
        return bool(relation & (1 << locations[(min(a, b), max(a, b))]))
    for slot, (left, right) in enumerate(pairs):
        if not (relation >> slot) & 1:
            continue
        interior = [vertex for vertex in range(left + 1, right)
                    if comparable(left, vertex) and comparable(vertex, right)]
        if any(not comparable(a, b) for a, b in combinations(interior, 2)):
            target |= 1 << slot
    require(target & relation == target)
    return target


def main():
    rows = []
    for n in range(0, 9):
        rows.append(analyze("DPF", {"nonroot_vertices": n},
                            product(*(range(i) for i in range(1, n + 1))), depth_parent))
    for n in range(0, 6):
        for k in range(n + 1):
            graph = exchange_graph(n, k)
            def update(family):
                return sum(1 << i for i, neighbours in enumerate(graph)
                           if (family & neighbours).bit_count() == 1)
            rows.append(analyze("UEX", {"n": n, "k": k}, range(1 << len(graph)), update))
    for p in (2, 3, 5, 7, 11, 13):
        rows.append(analyze("CRS", {"prime": p}, range(1 << p),
                            lambda subset: critical_roots(subset, p)))
    for p in (3,):
        table = circumcenter_table(p)
        rows.append(analyze("CCS", {"prime": p, "dimension": 2}, range(1 << (p * p)),
                            lambda subset: circumcenter_image(subset, table)))
    for dimension in range(0, 5):
        rows.append(analyze("SEN", {"dimension": dimension}, range(1 << (1 << dimension)),
                            lambda function: sensitivity_one(function, dimension)))
    for n in range(0, 7):
        pairs, locations, states = poset_data(n)
        rows.append(analyze("IDR", {"n": n, "labelling": "natural"}, states,
                            lambda relation: diamond_interval(relation, pairs, locations)))
    print(json.dumps({"status": "PILOT_COMPLETE_NOT_THEOREM", "literal_rules": 6,
                      "boxes": len(rows), "states_across_boxes": sum(row["states"] for row in rows),
                      "assertions": checks, "enumeration_sha256": digest.hexdigest(),
                      "profiles": rows}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
