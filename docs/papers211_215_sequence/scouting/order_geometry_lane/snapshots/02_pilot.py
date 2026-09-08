#!/usr/bin/env python3
"""Fourth bounded intake: six full-carrier maps; author scout only."""

from collections import Counter
from hashlib import sha256
from itertools import product
from math import factorial
import json


def report(name, parameter, states, update, check=None):
    lookup = {a: i for i, a in enumerate(states)}
    successor = [lookup[update(a)] for a in states]
    depth = [-1] * len(states)
    period = [0] * len(states)
    cycles = Counter()
    for start in range(len(states)):
        if depth[start] >= 0:
            continue
        path, position = [], {}
        v = start
        while depth[v] < 0 and v not in position:
            position[v] = len(path)
            path.append(v)
            v = successor[v]
        if depth[v] < 0:
            cut = position[v]
            length = len(path) - cut
            cycles[length] += 1
            for w in path[cut:]:
                depth[w], period[w] = 0, length
            path = path[:cut]
        for w in reversed(path):
            depth[w] = depth[successor[w]] + 1
            period[w] = period[successor[w]]
    fibres = Counter(successor)
    assert sum(length * count for length, count in cycles.items()) == depth.count(0)
    if check:
        check(states, successor, fibres, lookup, depth)
    maximum = max(fibres.values())
    maxima = [states[i] for i in range(len(states)) if fibres.get(i, 0) == maximum]
    out = {
        "map": name, "parameters": parameter, "states": len(states),
        "image": len(fibres), "core": depth.count(0), "height": max(depth),
        "depth_histogram": sorted(Counter(depth).items()),
        "strict_cycle_histogram": sorted(cycles.items()),
        "one_step_fibre_histogram": sorted(Counter(fibres.get(i, 0) for i in range(len(states))).items()),
        "maximum_fibre": maximum, "maximum_targets": len(maxima),
        "lex_first_maximum_target": maxima[0],
        "successor_sha256": sha256(json.dumps(successor, separators=(",", ":")).encode()).hexdigest(),
        "structural_control": "PASS" if check else "not_claimed",
    }
    print(json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)


def eccentricity(n, bound):
    states = list(product(range(bound+1), repeat=n))
    def update(a):
        return tuple(max(abs(x-y) for y in a) for x in a)
    def check(states, successor, fibres, lookup, depth):
        assert depth.count(0) == 1
        expected_height = 0 if bound == 0 else min(n, bound.bit_length()+1)
        assert max(depth) == expected_height
        for target in states:
            r = max(target)
            if r == 0:
                expected = bound+1
            elif min(target)*2 < r:
                expected = 0
            else:
                ends = target.count(r)
                middle = sum(2*v == r for v in target)
                expected = ((bound-r+1) * (2**ends-2) * 2**(n-ends-middle)
                            if ends >= 2 else 0)
            assert fibres.get(lookup[target], 0) == expected
    report("EC", {"n": n, "bound": bound}, states, update, check)


def parking(n):
    states = list(product(range(n), repeat=n))
    def update(a):
        occupied = set()
        displacement = []
        for preference in a:
            location, distance = preference, 0
            while location in occupied:
                location = (location+1) % n
                distance += 1
            occupied.add(location)
            displacement.append(distance)
        return tuple(displacement)
    def check(states, successor, fibres, lookup, depth):
        image = set(successor)
        expected = {lookup[a] for a in states if all(a[i] <= i for i in range(n))}
        assert image == expected and len(image) == factorial(n)
        for i in image:
            assert update(states[i]) == tuple(j-states[i][j] for j in range(n))
        assert max(fibres.values()) == factorial(n)
        assert sum(count == factorial(n) for count in fibres.values()) == n
    report("CP", {"n": n}, states, update, check)


def occurrence_rank(n):
    states = list(product(range(n), repeat=n))
    def update(a):
        return tuple(sum(a[j] == a[i] for j in range(i)) for i in range(n))
    report("OR", {"n": n}, states, update)


def orbit_maps(n, kind):
    states = list(product(range(n), repeat=n))
    def update(f):
        output = []
        for v in range(n):
            orbit, w = set(), v
            while w not in orbit:
                orbit.add(w)
                w = f[w]
            if kind == "UO":
                output.append(next((u for u in range(n) if u not in orbit), v))
            else:
                output.append(len(orbit)-1)
        return tuple(output)
    report(kind, {"n": n}, states, update)


def midpoint(n):
    states = list(product(range(2), repeat=n))
    def update(a):
        support = [i for i in range(n) if a[i]]
        output = [0] * n
        for j, vertex in enumerate(support):
            following = support[(j+1) % len(support)]
            gap = (following-vertex) % n or n
            target = (vertex+gap//2) % n
            assert output[target] == 0
            output[target] = 1
        return tuple(output)
    def check(states, successor, fibres, lookup, depth):
        assert all(sum(states[i]) == sum(states[j]) for i, j in enumerate(successor))
    report("MG", {"circle_size": n}, states, update, check)


def main():
    for n in (1, 2, 3, 4):
        for bound in (1, 2, 4):
            eccentricity(n, bound)
    for n in (1, 3, 4):
        eccentricity(n, 0)
    for n in range(1, 6):
        parking(n)
    for n in range(1, 6):
        occurrence_rank(n)
    for kind in ("UO", "OS"):
        for n in range(1, 6):
            orbit_maps(n, kind)
    for n in range(3, 9):
        midpoint(n)


if __name__ == "__main__":
    main()
