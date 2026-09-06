#!/usr/bin/env python3
"""Immutable author pilot: exactly the three INTAKE boxes, no input files."""
import collections
import hashlib
import itertools
import json
import sys

assert sys.flags.optimize == 0
CHECKS = 0


def check(value):
    global CHECKS
    CHECKS += 1
    assert value


def rot(w, k):
    return w[k:] + w[:k]


def cnl(w):
    m = min(rot(w, k) for k in range(len(w)))
    return tuple(a ^ b for a, b in zip(w, m))


def bits(x, n):
    return tuple((x >> (n - 1 - i)) & 1 for i in range(n))


def number(w):
    z = 0
    for b in w:
        z = 2 * z + b
    return z


def cnl_integer(x, n):
    mask = (1 << n) - 1
    rotations = [((x << k) & mask) | (x >> (n - k)) for k in range(n)]
    return x ^ min(rotations)


def graph_data(mask, n, edges):
    adjacent = [set() for _ in range(n)]
    for j, (a, b) in enumerate(edges):
        if mask & (1 << j):
            adjacent[a].add(b)
            adjacent[b].add(a)
    active = [v for v in range(n) if len(adjacent[v]) == 2]
    return adjacent, active


def d2lc(mask, n, edges, edge_indices):
    adjacent, active = graph_data(mask, n, edges)
    if not active:
        return mask
    a, b = sorted(adjacent[active[0]])
    return mask ^ (1 << edge_indices[(a, b)])


def lrg(w, r, c):
    rows = [w[i*c:(i+1)*c] for i in range(r)]
    rows = [min(rot(row, k) for k in range(c)) for row in rows]
    columns = [tuple(rows[i][j] for i in range(r)) for j in range(c)]
    columns = [max(rot(col, k) for k in range(r)) for col in columns]
    return tuple(columns[j][i] for i in range(r) for j in range(c))


def lrg_lists(w, r, c):
    grid = [list(w[i*c:(i+1)*c]) for i in range(r)]
    for i in range(r):
        candidates = []
        for start in range(c):
            candidates.append([grid[i][(start+j) % c] for j in range(c)])
        grid[i] = min(candidates)
    for j in range(c):
        old = [grid[i][j] for i in range(r)]
        chosen = max([old[(start+i) % r] for i in range(r)] for start in range(r))
        for i in range(r):
            grid[i][j] = chosen[i]
    return tuple(value for row in grid for value in row)


def histogram(values):
    return [[key, count] for key, count in sorted(collections.Counter(values).items())]


def functional_graph(images):
    n = len(images)
    depth = [-1] * n
    period = [0] * n
    cycles = []
    for start in range(n):
        if depth[start] >= 0:
            continue
        path = []
        seen = {}
        at = start
        while depth[at] < 0 and at not in seen:
            seen[at] = len(path)
            path.append(at)
            at = images[at]
        if at in seen:
            split = seen[at]
            cycle = path[split:]
            smallest = cycle.index(min(cycle))
            cycles.append(cycle[smallest:] + cycle[:smallest])
            for item in cycle:
                depth[item] = 0
                period[item] = len(cycle)
            prefix = path[:split]
        else:
            prefix = path
        for item in reversed(prefix):
            depth[item] = depth[images[item]] + 1
            period[item] = period[images[item]]
    for x, y in enumerate(images):
        check(0 <= y < n)
        check(period[x] == period[y])
        check(depth[x] == depth[y] + 1 if depth[x] else depth[y] == 0)
    check(sum(len(cycle) for cycle in cycles) == depth.count(0))
    return depth, period, cycles


def census(label, parameters, images, decode):
    before = CHECKS
    n = len(images)
    predecessors = [[] for _ in range(n)]
    for x, y in enumerate(images):
        predecessors[y].append(x)
    indegrees = [len(p) for p in predecessors]
    check(sum(indegrees) == n)
    depth, period, cycles = functional_graph(images)
    longest = min((cycle for cycle in cycles if len(cycle) == max(period)), key=lambda c: c[0])
    tail_source = depth.index(max(depth))
    orbit = []
    at = tail_source
    for _ in range(depth[at] + period[at]):
        orbit.append(decode(at))
        at = images[at]
    max_target = indegrees.index(max(indegrees))
    answer = {
        'map': label, 'parameters': parameters, 'states': n,
        'image_size': sum(d > 0 for d in indegrees),
        'fixed_points': sum(x == y for x, y in enumerate(images)),
        'max_tail': max(depth), 'max_period': max(period),
        'max_fibre': max(indegrees), 'max_fibre_target_count': indegrees.count(max(indegrees)),
        'depth_histogram': histogram(depth),
        'cycle_count_by_period': histogram(len(cycle) for cycle in cycles),
        'fibre_histogram_including_zero': histogram(indegrees),
        'longest_cycle': [decode(v) for v in longest],
        'longest_tail_orbit': orbit,
        'first_max_fibre_target': decode(max_target),
        'first_max_fibre_sources': [decode(v) for v in predecessors[max_target]],
        'integer_arrow_sha256': hashlib.sha256(json.dumps(images, separators=(',', ':')).encode()).hexdigest(),
        'graph_checks': CHECKS - before,
    }
    return answer, depth, period, predecessors


def main():
    rows = []
    for n in range(1, 13):
        images = []
        for x in range(1 << n):
            w = bits(x, n)
            y = cnl(w)
            check(len(y) == n and set(y) <= {0, 1})
            check(sum(y) % 2 == 0)
            check(number(y) == cnl_integer(x, n))
            images.append(number(y))
        out, depth, period, pred = census('CNL', [n], images, lambda x: ''.join(map(str, bits(x, n))))
        check(out['fixed_points'] == 1 and images[0] == 0)
        if n & (n - 1) == 0:
            check(max(period) == 1 and max(depth) <= n)
        rows.append(out)
    for n in range(1, 7):
        edges = list(itertools.combinations(range(n), 2))
        edge_indices = {edge: j for j, edge in enumerate(edges)}
        images = [d2lc(x, n, edges, edge_indices) for x in range(1 << len(edges))]
        decode = lambda x: [list(e) for j, e in enumerate(edges) if x & (1 << j)]
        out, depth, period, pred = census('D2LC', [n], images, decode)
        check(max(period) <= 2 and max(depth) <= n - 1)
        for y in range(len(images)):
            adj, active = graph_data(y, n, edges)
            proposed = {y} if not active else set()
            for v in active:
                a, b = sorted(adj[v])
                x = y ^ (1 << edge_indices[(a, b)])
                source_adj, source_active = graph_data(x, n, edges)
                if source_active[0] == v:
                    proposed.add(x)
            check(proposed == set(pred[y]))
            if active:
                next_adj, next_active = graph_data(images[y], n, edges)
                check(bool(next_active) and next_active[0] <= active[0])
                check((depth[y] == 0) == (next_active[0] == active[0]))
            else:
                check(pred[y] == [y])
        rows.append(out)
    for r, c in ((1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3), (3,4)):
        images = []
        for x in range(1 << (r*c)):
            w = bits(x, r*c)
            y = lrg(w, r, c)
            check(len(y) == r*c and set(y) <= {0, 1})
            check(y == lrg_lists(w, r, c))
            check(sum(y) == sum(w))
            images.append(number(y))
        decode = lambda x: [''.join(map(str, bits(x, r*c)[i*c:(i+1)*c])) for i in range(r)]
        out, depth, period, pred = census('LRG', [r,c], images, decode)
        if min(r,c) == 1:
            check(max(depth) <= 1 and max(period) == 1)
        rows.append(out)
    output = {'role': 'AUTHOR_SCOUT_NOT_INDEPENDENT_REVIEW', 'schema': 1,
              'literal_maps_executed': 3, 'complete_boxes': len(rows),
              'state_map_pairs': sum(row['states'] for row in rows),
              'assertions': CHECKS, 'rows': rows}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
