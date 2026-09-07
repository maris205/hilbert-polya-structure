#!/usr/bin/env python3
"""P209 Review B: constructive carrier, monotone relation and local ports."""
import itertools
import json
import math
import sys

CHECKS = 0

def require(value, detail):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(detail)

def operation(f):
    n = len(f)
    return tuple(next((j for j in range(i + 1, n) if f[j] == f[i]), f[i])
                 for i in range(n))

def relation(f):
    n = len(f)
    result = set()
    for i in range(n):
        j = i
        for _ in range(n + 1):
            result.add((i, j))
            j = f[j]
    return result

def heights(f):
    n = len(f)
    present = set(range(n))
    h = [0] * n
    for k in range(1, n + 1):
        present = {f[i] for i in present}
        for v in present:
            h[v] = k
    return tuple(n + 1 if x == n else x for x in h)

def port_sources(g):
    n = len(g)
    possibilities = []
    factors = []
    for v in range(n):
        arrivals = tuple(i for i in range(n) if g[i] == v)
        local = []
        # Port value 0 = terminal, 1 = continuation.
        for labels in itertools.product((0, 1), repeat=len(arrivals)):
            if labels.count(0) > 1 or labels.count(1) > 1:
                continue
            if any(t and i >= v for i, t in zip(arrivals, labels)):
                continue
            local.append(tuple(zip(arrivals, labels)))
        possibilities.append(local)
        factors.append(len(local))
    result = []
    for local_choices in itertools.product(*possibilities):
        types = dict(pair for choice in local_choices for pair in choice)
        f = [-1] * n
        for i in range(n - 1, -1, -1):
            f[i] = f[g[i]] if types[i] else g[i]
        f = tuple(f)
        require(operation(f) == g, ('port_soundness', g, types, f))
        for i in range(n):
            # A terminal can be a loop; recover type by strictly-greater
            # target and equality, not equality alone.
            recovered = int(i < g[i] and f[i] == f[g[i]])
            require(recovered == types[i], ('type_injectivity', g, f, i))
        result.append(f)
    require(len(result) == len(set(result)), ('injectivity', g))
    require(len(result) == math.prod(factors), ('product', g))
    return result, factors

def constructed_carrier(n):
    result = {}
    if not n:
        return {(): {'period': 1, 'next': (), 'core': (), 'paths': ()}}
    labels = set(range(n))
    for k in range(1, n + 1):
        for core in itertools.combinations(range(n), k):
            outside = sorted(labels - set(core))
            for images in itertools.permutations(core):
                cycle_next = dict(zip(core, images))
                cycle_prev = {v: u for u, v in cycle_next.items()}
                cycle_info = {}
                for c in core:
                    cycle = [c]
                    j = cycle_next[c]
                    while j != c:
                        cycle.append(j)
                        j = cycle_next[j]
                    cycle_info[c] = (len(cycle), min(cycle))
                # Slot-length compositions, then permutations, construct
                # each family of labelled paths with no graph classifier.
                for lengths in itertools.product(range(len(outside) + 1), repeat=k):
                    if sum(lengths) != len(outside):
                        continue
                    for order in itertools.permutations(outside):
                        paths = []
                        pos = 0
                        for c, length in zip(core, lengths):
                            path = order[pos:pos + length]
                            pos += length
                            if path:
                                paths.append((c, path))
                        if any(path[-1] >= cycle_info[c][1] for c, path in paths):
                            continue
                        f = [-1] * n
                        new = [-1] * n
                        for c in core:
                            f[c] = new[c] = cycle_next[c]
                        period = 1
                        for c, path in paths:
                            for u, v in zip(path, path[1:]):
                                f[u] = new[u] = v
                            f[path[-1]] = c
                            new[path[-1]] = cycle_prev[c]
                            period = math.lcm(period, cycle_info[c][0])
                        f = tuple(f)
                        require(f not in result, ('carrier_descriptor_unique', f))
                        result[f] = {'period': period, 'next': tuple(new),
                                     'core': core, 'paths': tuple(paths)}
    return result

def run(n):
    states = list(itertools.product(range(n), repeat=n))
    rank = {f: i for i, f in enumerate(states)}
    successor = [rank[operation(f)] for f in states]
    inverse = [[] for _ in states]
    for i, j in enumerate(successor):
        inverse[j].append(i)
    stable = set(range(len(states)))
    while True:
        new = {successor[i] for i in stable}
        require(new <= stable, ('whole_map_image_filtration', n))
        if new == stable:
            break
        stable = new
    expected = constructed_carrier(n)
    require({rank[f] for f in expected} == stable, ('carrier_iff', n))
    rows = []
    for i, f in enumerate(states):
        g = states[successor[i]]
        require(relation(f) <= relation(g), ('reachability_monotonicity', f))
        hf, hg = heights(f), heights(g)
        require(all(a <= b for a, b in zip(hf, hg)), ('height_monotonicity', f))
        route = {}
        j = i
        while j not in route:
            route[j] = len(route)
            j = successor[j]
        entrance, period = route[j], len(route) - route[j]
        recurrent = i in stable
        require(recurrent == (entrance == 0), ('stable_iff_return', f))
        descriptor = expected.get(f)
        if recurrent:
            require(relation(f) == relation(g), ('frozen_relation', f))
            require(hf == hg, ('frozen_heights', f))
            require(descriptor['period'] == period, ('least_lcm', f))
            require(descriptor['next'] == g, ('attachment_rotation', f))
        decoded, factors = port_sources(f)
        decoded_ranks = sorted(rank[x] for x in decoded)
        require(decoded_ranks == inverse[i], ('inverse_iff_all_targets', f))
        q = sum(v == 2 for v in factors)
        require(not decoded or len(decoded) == 2 ** q, ('power_two', f))
        limit = 2 ** (n - 1) if n else 1
        require(len(decoded) <= limit, ('bound', f))
        extremizer = tuple((v + 1) % n for v in range(n))
        require((len(decoded) == limit) == (f == extremizer), ('unique_maximum', f))
        rows.append({'rank': i, 'f': f, 'T_rank': successor[i],
                     'entrance': entrance, 'period': period, 'recurrent': recurrent,
                     'carrier': descriptor, 'predecessors': inverse[i],
                     'port_predecessors': decoded_ranks, 'port_factors': factors,
                     'heights': hf, 'reachability_size': len(relation(f))})
    require(sum(len(x) for x in inverse) == len(states), ('inverse_mass', n))
    return {'n': n, 'states': len(states), 'recurrent': len(stable),
            'image_size': sum(bool(x) for x in inverse),
            'max_inverse': max(map(len, inverse)), 'rows': rows}

def main():
    require(sys.flags.optimize == 0, 'optimization must be zero')
    require(sys.argv[1:] in ([], ['--max-n', '5']), 'only original --max-n 5 box authorized')
    boxes = [run(n) for n in range(6)]
    require(sum(x['states'] for x in boxes) == 3414, 'original carrier census')
    print(json.dumps({'schema': 'p209-b-ports-constructive-carrier-v1',
                      'max_n': 5, 'states': 3414, 'checks': CHECKS,
                      'status': 'PASS', 'boxes': boxes}, sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    main()
