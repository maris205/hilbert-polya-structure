#!/usr/bin/env python3
"""One original complete-box SMV falsifier; not an all-field time proof."""
import collections
import itertools
import json
import sys

PRIMES = (3, 5, 7, 17)
CHECKS = 0


def check(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def update(point, p):
    x, y, z = point
    return ((y * z - x) % p, (z * x - y) % p, (x * y - z) % p)


def inverse(target, p):
    a, b, c = target
    found = []
    for z in range(p):
        denom = (z * z - 1) % p
        factored = ((z + c) * (z * z - 1) ** 2 - (b * z + a) * (a * z + b)) % p
        expanded = (z ** 5 + c * z ** 4 - 2 * z ** 3 - (2 * c + a * b) * z ** 2
                    + (1 - a * a - b * b) * z + c - a * b) % p
        check(expanded == factored, ('polynomial-expansion', p, target, z))
        if denom:
            if factored == 0:
                inv = pow(denom, p - 2, p)
                found.append((((b * z + a) * inv) % p, ((a * z + b) * inv) % p, z))
        elif (b + a * z) % p == 0:
            for y in range(p):
                if (z * y * y - a * y - c - z) % p == 0:
                    found.append(((z * y - a) % p, y, z))
    check(len(found) == len(set(found)), ('duplicate-inverse-branch', p, target))
    return set(found)


def histogram(values):
    return dict(sorted(collections.Counter(values).items()))


def graph(successor):
    n = len(successor)
    component = [-1] * n
    depth = [-1] * n
    cycles = []
    for initial in range(n):
        if component[initial] >= 0:
            continue
        path = []
        seen = {}
        node = initial
        while component[node] < 0 and node not in seen:
            seen[node] = len(path)
            path.append(node)
            node = successor[node]
        if component[node] < 0:
            prefix = seen[node]
            cycle = path[prefix:]
            start = cycle.index(min(cycle))
            cycle = cycle[start:] + cycle[:start]
            cid = len(cycles)
            cycles.append(cycle)
            for v in cycle:
                component[v] = cid
                depth[v] = 0
            path = path[:prefix]
        for v in reversed(path):
            component[v] = component[successor[v]]
            depth[v] = depth[successor[v]] + 1
    check(all(c >= 0 for c in component) and all(h >= 0 for h in depth), 'complete-functional-graph')
    for cid, cycle in enumerate(cycles):
        check(len(cycle) == len(set(cycle)), ('simple-cycle', cid))
        for i, v in enumerate(cycle):
            check(successor[v] == cycle[(i + 1) % len(cycle)] and depth[v] == 0, ('cycle-edge', cid, v))
    for v in range(n):
        if depth[v]:
            check(depth[v] == depth[successor[v]] + 1 and component[v] == component[successor[v]], ('tail-edge', v))
    return component, depth, cycles


def box(p):
    points = list(itertools.product(range(p), repeat=3))
    index = {point: i for i, point in enumerate(points)}
    successor = []
    fibres = [set() for _ in points]
    for i, point in enumerate(points):
        image = update(point, p)
        j = index[image]
        successor.append(j)
        fibres[j].add(point)
        x, y, z = point
        u, v, w = image
        check((u - v + (z + 1) * (x - y)) % p == 0, ('difference1', p, point))
        check((v - w + (x + 1) * (y - z)) % p == 0, ('difference2', p, point))
        check((w - u + (y + 1) * (z - x)) % p == 0, ('difference3', p, point))
    sizes = []
    for target, expected in zip(points, fibres):
        decoded = inverse(target, p)
        check(decoded == expected, ('all-target-exact-fibre', p, target, sorted(decoded), sorted(expected)))
        check(len(decoded) <= 5, ('five-bound', p, target))
        sizes.append(len(decoded))
    zero = {(0, 0, 0)}
    fixed = {(0, 0, 0)}
    for signs in itertools.product((-1, 1), repeat=3):
        if signs[0] * signs[1] * signs[2] == 1:
            zero.add(tuple(s % p for s in signs))
            fixed.add(tuple((2 * s) % p for s in signs))
    check(fibres[0] == zero and len(zero) == 5, ('sharp-zero-fibre', p))
    actual_fixed = {point for i, point in enumerate(points) if successor[i] == i}
    check(actual_fixed == fixed and len(fixed) == 5, ('all-fixed-points', p))
    check(sum(sizes) == len(points) and max(sizes) == 5, ('fibre-partition', p))
    for t in range(p):
        value = (t * t - t) % p
        check(update((t, t, t), p) == (value, value, value), ('diagonal', p, t))
    components, depths, cycles = graph(successor)
    basin = collections.Counter(components)
    peak = [0] * len(cycles)
    for c, h in zip(components, depths):
        peak[c] = max(peak[c], h)
    cycle_rows = [dict(nodes=[points[i] for i in cycle], length=len(cycle),
                       basin_states=basin[cid], max_depth=peak[cid]) for cid, cycle in enumerate(cycles)]
    check(sum(row['basin_states'] for row in cycle_rows) == len(points), ('all-basins', p))
    if p == 17:
        triple = [(3, 3, 3), (6, 6, 6), (13, 13, 13)]
        check(all(update(triple[i], p) == triple[(i + 1) % 3] for i in range(3)), 'explicit-diagonal-three-cycle')
    return dict(prime=p, state_count=len(points), coordinate_order='lexicographic (x,y,z), 0..p-1',
                successor_indices=successor, every_target_fibre_size=sizes, every_state_depth=depths,
                every_state_eventual_period=[len(cycles[c]) for c in components],
                image_size=sum(n > 0 for n in sizes), fibre_histogram=histogram(sizes),
                max_fibre=5, max_fibre_target_indices=[i for i, n in enumerate(sizes) if n == 5],
                fixed_points=sorted(fixed), maximum_depth=max(depths), depth_histogram=histogram(depths),
                cycle_length_histogram=histogram(len(c) for c in cycles), cycles=cycle_rows)


def main():
    check(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize,
          'required-isolated-no-site-no-bytecode-no-optimization')
    rows = [box(p) for p in PRIMES]
    check(sum(r['state_count'] for r in rows) == 5408, 'fixed-complete-box-size')
    print(json.dumps(dict(status='PASS_FIXED_BOX_PILOT_NOT_ALL_FIELD_TEMPORAL_PROOF',
                          candidate='SMV', literal_maps=1, original_pilots=1, primes=PRIMES,
                          total_states=5408, total_targets=5408, checks=CHECKS, boxes=rows),
                     sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
