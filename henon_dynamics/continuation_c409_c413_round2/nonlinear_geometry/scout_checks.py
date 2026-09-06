#!/usr/bin/env python3
"""Exact finite-scope scouts; not an assertion of global completeness."""

from collections import Counter
from itertools import product
from math import isqrt


def cycles_in_box(points, transform):
    """Find cycles of the partial permutation induced on the exact finite set."""
    remaining = set(points)
    cycles = []
    while remaining:
        start = next(iter(remaining))
        path, offsets = [], {}
        point = start
        while point in remaining and point not in offsets:
            offsets[point] = len(path)
            path.append(point)
            point = transform(point)
        if point in offsets:
            cycle = path[offsets[point] :]
            least = min(range(len(cycle)), key=cycle.__getitem__)
            cycles.append(cycle[least:] + cycle[:least])
        remaining.difference_update(path)
    return sorted(cycles, key=lambda cycle: (len(cycle), cycle))


def trace_scout(bound):
    transform = lambda point: (point[1], point[2], point[1] * point[2] - point[0])
    cycles = cycles_in_box(product(range(-bound, bound + 1), repeat=3), transform)
    counts = Counter(len(cycle) for cycle in cycles)
    print(f"TRACE complete cycles wholly inside [-{bound},{bound}]^3: {dict(sorted(counts.items()))}")
    off_axes = [cycle for cycle in cycles if sum(x != 0 for x in cycle[0]) > 1]
    for cycle in off_axes:
        x, y, z = cycle[0]
        invariant = x * x + y * y + z * z - x * y * z
        print(f"  invariant={invariant}, period={len(cycle)}, cycle={cycle}")
    assert all(transform(cycle[-1]) == cycle[0] for cycle in cycles)
    assert all(transform(cycle[i]) == cycle[i + 1] for cycle in cycles for i in range(len(cycle) - 1))
    assert all(transform(transform(transform(transform(transform(transform((a, 0, 0))))))) == (a, 0, 0) for a in range(-bound, bound + 1))


def cubic_scout(lower, upper):
    print(f"CUBIC complete integral cycles for H_a(x,y)=(y,y^3-a*y-x), {lower} <= a <= {upper}")
    shapes = Counter()
    examples = {}
    for parameter in range(lower, upper + 1):
        bound = isqrt(max(0, parameter + 2))
        transform = lambda point: (point[1], point[1] ** 3 - parameter * point[1] - point[0])
        cycles = cycles_in_box(product(range(-bound, bound + 1), repeat=2), transform)
        shape = tuple(sorted(Counter(len(cycle) for cycle in cycles).items()))
        shapes[shape] += 1
        examples.setdefault(shape, (parameter, cycles))
    for shape in sorted(shapes):
        print(f"  cycle signature={shape}, parameter count={shapes[shape]}, first example={examples[shape]}")


if __name__ == "__main__":
    trace_scout(12)
    cubic_scout(-12, 400)
