#!/usr/bin/env python3
"""Six exact bounded geometric literals; original boxes in INTAKE.md."""
from collections import Counter
from hashlib import sha256
from itertools import product
import json

checks = 0
all_digest = sha256()


def require(value):
    global checks
    checks += 1
    if not value:
        raise AssertionError(checks)


def analyze(name, parameter, states, update, extra=None):
    states = list(states)
    index = {state: i for i, state in enumerate(states)}
    require(len(index) == len(states))
    targets = [update(state) for state in states]
    require(all(target in index for target in targets))
    forward = [index[target] for target in targets]
    inverse = Counter(forward)
    tails = [-1] * len(states)
    periods = [-1] * len(states)
    cycles = Counter()
    for start in range(len(states)):
        if tails[start] >= 0:
            continue
        path, seen, point = [], {}, start
        while tails[point] < 0 and point not in seen:
            seen[point] = len(path)
            path.append(point)
            point = forward[point]
        if tails[point] < 0:
            split = seen[point]
            loop = path[split:]
            cycles[len(loop)] += 1
            for vertex in loop:
                tails[vertex], periods[vertex] = 0, len(loop)
            path = path[:split]
        for vertex in reversed(path):
            tails[vertex] = 1 + tails[forward[vertex]]
            periods[vertex] = periods[forward[vertex]]
    for i, state in enumerate(states):
        target = targets[i]
        require(periods[i] == periods[forward[i]])
        require(tails[i] == 0 or tails[i] == 1 + tails[forward[i]])
        if extra:
            extra(state, target)
        all_digest.update(json.dumps([name, parameter, state, target, tails[i], periods[i]],
                                     sort_keys=True, separators=(",", ":")).encode())
        all_digest.update(b"\n")
    maximum = max(inverse.values())
    maxima = [i for i in range(len(states)) if inverse[i] == maximum]
    height = max(tails)
    return {"rule": name, "parameter": parameter, "states": len(states),
            "image": len(inverse), "recurrent": sum(t == 0 for t in tails),
            "height": height, "cycles_by_length": dict(sorted(cycles.items())),
            "depth_counts": dict(sorted(Counter(tails).items())),
            "deepest_witness": states[tails.index(height)],
            "maximum_fibre": maximum, "maximizer_count": len(maxima),
            "maximizer_witness": states[maxima[0]],
            "nonempty_fibre_histogram": dict(sorted(Counter(inverse.values()).items()))}


def qhk(state):
    counts = Counter(state)
    targets = {}
    for x in counts:
        neighbours = sum(counts[y] for y in (x - 1, x, x + 1))
        total = sum(y * counts[y] for y in (x - 1, x, x + 1))
        targets[x] = (2 * total + neighbours - 1) // (2 * neighbours)
    return tuple(targets[x] for x in state)


def ols(a, b):
    points = [(x, y) for x in range(-a, a + 1) for y in range(-b, b + 1)]
    priority = sorted(range(len(points)), key=lambda i: (sum(v * v for v in points[i]),
                                                        points[i][0], points[i][1]))
    rank = {i: r for r, i in enumerate(priority)}
    stages = []
    for direction in (lambda p: p[1], lambda p: p[0] - p[1]):
        keys = sorted({direction(p) for p in points})
        groups = []
        for key in keys:
            members = [i for i in priority if direction(points[i]) == key]
            prefixes = [sum(1 << i for i in members[:k]) for k in range(len(members) + 1)]
            groups.append((prefixes[-1], prefixes))
        stages.append(groups)

    def update(mask):
        for groups in stages:
            mask = sum(prefixes[(mask & line).bit_count()] for line, prefixes in groups)
        return mask

    def potential(mask):
        return sum(rank[i] for i in range(len(points)) if mask & (1 << i))

    def extra(source, target):
        require(source.bit_count() == target.bit_count())
        require(potential(source) >= potential(target))
        require(source == target or potential(source) > potential(target))

    return len(points), update, extra


def rectangle_centres(a, b):
    points = [(x, y) for x in range(a) for y in range(b)]

    def encode(rect):
        lo_x, hi_x, lo_y, hi_y = rect
        return sum(1 << i for i, (x, y) in enumerate(points)
                   if lo_x <= x <= hi_x and lo_y <= y <= hi_y)

    data = []
    for lo_x in range(a):
        for hi_x in range(lo_x, a):
            for lo_y in range(b):
                for hi_y in range(lo_y, b):
                    rect = (lo_x, hi_x, lo_y, hi_y)
                    expansions = []
                    if lo_x:
                        expansions.append(encode((lo_x - 1, hi_x, lo_y, hi_y)))
                    if hi_x + 1 < a:
                        expansions.append(encode((lo_x, hi_x + 1, lo_y, hi_y)))
                    if lo_y:
                        expansions.append(encode((lo_x, hi_x, lo_y - 1, hi_y)))
                    if hi_y + 1 < b:
                        expansions.append(encode((lo_x, hi_x, lo_y, hi_y + 1)))
                    centre_x = {(lo_x + hi_x) // 2, (lo_x + hi_x + 1) // 2}
                    centre_y = {(lo_y + hi_y) // 2, (lo_y + hi_y + 1) // 2}
                    centres = sum(1 << i for i, (x, y) in enumerate(points)
                                  if x in centre_x and y in centre_y)
                    data.append((encode(rect), expansions, centres))

    def update(mask):
        target = 0
        for rect, expansions, centres in data:
            if not mask & rect and all(mask & extension for extension in expansions):
                target |= centres
        return target

    return len(points), update


def nearest_ties(a, b):
    points = [(x, y) for x in range(a) for y in range(b)]
    shells = []
    for q in points:
        layers = {}
        for i, p in enumerate(points):
            d = sum((p[j] - q[j]) ** 2 for j in range(2))
            layers[d] = layers.get(d, 0) | (1 << i)
        shells.append([layers[d] for d in sorted(layers)])

    def update(mask):
        target = 0
        for i, layers in enumerate(shells):
            for layer in layers:
                nearest = mask & layer
                if nearest:
                    if nearest.bit_count() >= 2:
                        target |= 1 << i
                    break
        return target

    return len(points), update


def singular_vertices(a, b):
    corners = []
    for x in range(a):
        for y in range(b):
            corners.append((x * b + y, ((x - 1) % a) * b + y,
                            x * b + (y - 1) % b, ((x - 1) % a) * b + (y - 1) % b))

    def update(mask):
        target = 0
        for i, corner in enumerate(corners):
            p, q, r, s = [(mask >> j) & 1 for j in corner]
            if p == s and q == r and p != q:
                target |= 1 << i
        return target

    return a * b, update


def laguerre(n, m):
    costs = [[(q - i) ** 2 for i in range(m)] for q in range(n)]

    def update(weights):
        counts = [0] * m
        for row in costs:
            best = min(range(m), key=lambda i: row[i] - weights[i])
            counts[best] += 1
        return tuple(counts)

    def twice_potential(weights):
        return (2 * sum(max(weights[i] - row[i] for i in range(m)) for row in costs)
                - sum(w * w for w in weights))

    def extra(source, target):
        require(sum(target) == n)
        require(twice_potential(target) - twice_potential(source) >=
                sum((target[i] - source[i]) ** 2 for i in range(m)))

    return update, extra


def main():
    profiles = []
    for length in range(1, 7):
        for population in range(1, 6):
            profiles.append(analyze("QHK", {"positions": length, "particles": population},
                                    product(range(length), repeat=population), qhk))
    for a, b in ((0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (1, 1), (1, 2), (2, 1)):
        size, update, extra = ols(a, b)
        profiles.append(analyze("OLS", {"half_width": a, "half_height": b},
                                range(1 << size), update, extra))
    grids = ((1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (3, 3), (3, 4))
    for a, b in grids:
        for name, factory in (("MER", rectangle_centres), ("NTL", nearest_ties)):
            size, update = factory(a, b)
            def disjoint(source, target):
                require(not source & target)
            profiles.append(analyze(name, {"rows": a, "columns": b},
                                    range(1 << size), update, disjoint))
    for a, b in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3)):
        size, update = singular_vertices(a, b)
        profiles.append(analyze("NSV", {"rows": a, "columns": b}, range(1 << size), update))
    for n in range(1, 8):
        for m in range(1, min(4, n) + 1):
            update, extra = laguerre(n, m)
            profiles.append(analyze("LVC", {"demand_points": n, "sites": m},
                                    product(range(n + 1), repeat=m), update, extra))
    print(json.dumps({"status": "BOUNDED_GEOMETRIC_PILOT_NOT_ADMISSION", "literal_maps": 6,
                      "boxes": len(profiles), "states_across_boxes": sum(p["states"] for p in profiles),
                      "assertions": checks, "all_state_sha256": all_digest.hexdigest(),
                      "profiles": profiles}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
