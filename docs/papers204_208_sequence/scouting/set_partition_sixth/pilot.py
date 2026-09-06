#!/usr/bin/env python3
"""Six bounded full-carrier scouts. See INTAKE.md for literal conventions."""
from collections import Counter
from functools import cmp_to_key
from hashlib import sha256
from math import gcd
import json

assertions = 0
state_digest = sha256()


def require(condition):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(assertions)


def analyze(rule, parameter, states, update):
    states = list(states)
    index = {x: i for i, x in enumerate(states)}
    require(len(index) == len(states))
    targets = [update(x) for x in states]
    require(all(y in index for y in targets))
    forward = [index[y] for y in targets]
    indegree = Counter(forward)
    tail = [-1] * len(states)
    period = [-1] * len(states)
    cycles = Counter()
    for start in range(len(states)):
        if tail[start] >= 0:
            continue
        path, seen, vertex = [], {}, start
        while tail[vertex] < 0 and vertex not in seen:
            seen[vertex] = len(path)
            path.append(vertex)
            vertex = forward[vertex]
        if tail[vertex] < 0:
            split = seen[vertex]
            loop = path[split:]
            cycles[len(loop)] += 1
            for point in loop:
                tail[point], period[point] = 0, len(loop)
            path = path[:split]
        for point in reversed(path):
            tail[point] = 1 + tail[forward[point]]
            period[point] = period[forward[point]]
    for i, y in enumerate(targets):
        require(period[i] == period[forward[i]])
        require(tail[i] == 0 or tail[i] == tail[forward[i]] + 1)
        state_digest.update(json.dumps([rule, parameter, states[i], y, tail[i], period[i]],
                                      separators=(",", ":"), sort_keys=True).encode())
        state_digest.update(b"\n")
    height = max(tail)
    biggest = max(indegree.values())
    maxima = [i for i in range(len(states)) if indegree[i] == biggest]
    return {"rule": rule, "parameter": parameter, "states": len(states),
            "image": len(indegree), "recurrent": sum(t == 0 for t in tail),
            "cycles_by_length": dict(sorted(cycles.items())), "height": height,
            "depth_counts": dict(sorted(Counter(tail).items())),
            "deepest_witness": states[tail.index(height)],
            "maximum_fibre": biggest, "maximizer_count": len(maxima),
            "maximizer_witness": states[maxima[0]],
            "nonempty_fibre_histogram": dict(sorted(Counter(indegree.values()).items()))}


def family_maps(n):
    cube = 1 << n
    full = cube - 1
    down = [sum(1 << b for b in range(cube) if b & a == b) for a in range(cube)]
    fibres, subcubes = [], []
    for a in range(cube):
        traces = [b for b in range(cube) if b & a == b]
        fibres.append([sum(1 << x for x in range(cube) if x & a == b) for b in traces])
        outside = [b for b in range(cube) if b & a == 0]
        subcubes.append([sum(1 << (b | x) for x in traces) for b in outside])

    def shd(family):
        return sum(1 << a for a in range(cube)
                   if all(family & f for f in fibres[a])
                   and not any(family & c == c for c in subcubes[a]))

    def uz(family):
        return sum(1 << a for a in range(cube) if (family & down[a]).bit_count() == 1)

    def ud(family):
        return sum(1 << a for a in range(cube)
                   if (family & down[full ^ a]).bit_count() == 1)

    return shd, uz, ud


def path_map(n):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    def update(mask):
        adjacency = [[0] * n for _ in range(n)]
        for bit, (i, j) in enumerate(edges):
            adjacency[i][j] = (mask >> bit) & 1
        paths = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                paths[i][j] = min(2, adjacency[i][j] +
                                 sum(adjacency[i][k] * paths[k][j] for k in range(i + 1, j)))
        return sum(1 << bit for bit, (i, j) in enumerate(edges) if paths[i][j] == 1)
    return 1 << len(edges), update


def partitions(n):
    if n == 0:
        yield ()
        return
    def extend(word, maximum):
        if len(word) == n:
            yield tuple(word)
            return
        for label in range(maximum + 2):
            yield from extend(word + [label], max(maximum, label))
    yield from extend([0], 0)


def all_partition_complement(word):
    n = len(word)
    if not n:
        return word
    blocks = [[i for i in range(n) if word[i] == label] for label in range(max(word) + 1)]
    inverse = [0] * n
    for block in blocks:
        for i, point in enumerate(block):
            inverse[block[(i + 1) % len(block)]] = point
    permutation = [inverse[(i + 1) % n] for i in range(n)]
    result, label = [-1] * n, 0
    for start in range(n):
        if result[start] >= 0:
            continue
        point = start
        while result[point] < 0:
            result[point] = label
            point = permutation[point]
        label += 1
    return tuple(result)


def angle_compare(a, b):
    half_a = 0 if a[1] > 0 or (a[1] == 0 and a[0] > 0) else 1
    half_b = 0 if b[1] > 0 or (b[1] == 0 and b[0] > 0) else 1
    if half_a != half_b:
        return -1 if half_a < half_b else 1
    cross = a[0] * b[1] - a[1] * b[0]
    return -1 if cross > 0 else (1 if cross < 0 else 0)


def tukey_map(rows, columns):
    points = [(x, y) for x in range(rows) for y in range(columns)]
    halfplanes = []
    for qx, qy in points:
        rays = set()
        for px, py in points:
            dx, dy = px - qx, py - qy
            if dx == dy == 0:
                continue
            divisor = gcd(abs(dx), abs(dy))
            ray = (-dy // divisor, dx // divisor)
            rays.add(ray)
            rays.add((-ray[0], -ray[1]))
        ordered = sorted(rays, key=cmp_to_key(angle_compare))
        normals = []
        if not ordered:
            normals = [(1, 0)]
        for i, a in enumerate(ordered):
            b = ordered[(i + 1) % len(ordered)]
            middle = (a[0] + b[0], a[1] + b[1])
            if middle == (0, 0):
                middle = (-a[1], a[0])
            normals.append(middle)
        masks = {sum(1 << i for i, (px, py) in enumerate(points)
                     if ax * (px - qx) + ay * (py - qy) >= 0)
                 for ax, ay in normals}
        require(bool(masks))
        halfplanes.append(sorted(masks))

    def update(subset):
        depths = [min((subset & h).bit_count() for h in masks) for masks in halfplanes]
        maximum = max(depths)
        return sum(1 << i for i, depth in enumerate(depths) if depth == maximum)
    return len(points), update


def main():
    profiles = []
    for n in range(5):
        shd, uz, ud = family_maps(n)
        states = range(1 << (1 << n))
        for name, update in (("SHD", shd), ("UZ", uz), ("UD", ud)):
            profiles.append(analyze(name, {"ground_size": n}, states, update))
    for n in range(7):
        count, update = path_map(n)
        profiles.append(analyze("UPC", {"vertices": n}, range(count), update))
    for n in range(9):
        profiles.append(analyze("AKC", {"labels": n}, partitions(n), all_partition_complement))
    grids = [(1, b) for b in range(1, 7)] + [(2, 2), (2, 3), (3, 3), (3, 4)]
    for rows, columns in grids:
        size, update = tukey_map(rows, columns)
        profiles.append(analyze("TDP", {"rows": rows, "columns": columns},
                                range(1 << size), update))
    print(json.dumps({"status": "BOUNDED_PILOT_NOT_ADMISSION", "literal_maps": 6,
                      "boxes": len(profiles), "states_across_boxes": sum(p["states"] for p in profiles),
                      "assertions": assertions, "all_state_sha256": state_digest.hexdigest(),
                      "profiles": profiles}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
