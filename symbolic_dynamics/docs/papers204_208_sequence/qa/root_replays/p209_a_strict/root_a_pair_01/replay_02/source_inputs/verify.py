"""Independent P209 A checker: incidence, reachability, and set partitions.

Written before reading any author/scout/gate numerical code or canonical.
Only standard-library imports; no input files or imported mathematical code.
The exhaustive domain is exactly n=0,...,5.
"""
import itertools
import json
import math
import sys


CHECKS = 0


def require(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def update(f):
    # Incoming incidence rows, traversed from largest source downwards.
    n = len(f)
    incoming = [[int(f[i] == v) for i in range(n)] for v in range(n)]
    result = [-1] * n
    for v, row in enumerate(incoming):
        destination = v
        for i in reversed(range(n)):
            if row[i]:
                result[i] = destination
                destination = i
    return tuple(result)


def partitions(n):
    # Canonical block creation order; no target-dependent subset search.
    blocks = []
    def visit(i):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(i)
            yield from visit(i + 1)
            b.pop()
        blocks.append([i])
        yield from visit(i + 1)
        blocks.pop()
    yield from visit(0)


def partition_inverse(g, all_partitions):
    result = {}
    for blocks in all_partitions:
        if any(g[a] != b for block in blocks for a, b in zip(block, block[1:])):
            continue
        values = [g[block[-1]] for block in blocks]
        if len(values) != len(set(values)):
            continue
        f = [-1] * len(g)
        mask = 0
        for block, value in zip(blocks, values):
            for i in block:
                f[i] = value
            for i in block[:-1]:
                mask |= 1 << i
        source = tuple(f)
        require(source not in result)
        result[source] = mask
    return result


def mask_inverse(g):
    result = {}
    n = len(g)
    for mask in range(1 << n):
        selected = [i for i in range(n) if mask & (1 << i)]
        ends = [i for i in range(n) if not mask & (1 << i)]
        if any(i >= g[i] for i in selected):
            continue
        if len({g[i] for i in selected}) != len(selected):
            continue
        if len({g[i] for i in ends}) != len(ends):
            continue
        source = []
        for i in range(n):
            while mask & (1 << i):
                i = g[i]
            source.append(g[i])
        source = tuple(source)
        require(source not in result)
        result[source] = mask
    return result


def graph_geometry(f):
    n = len(f)
    reach = [[f[i] == j for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    cyclic = {i for i in range(n) if reach[i][i]}
    sccs = []
    for i in sorted(cyclic):
        if not any(i in c for c in sccs):
            sccs.append(tuple(j for j in range(n) if reach[i][j] and reach[j][i]))
    indegree = [sum(f[i] == v for i in range(n)) for v in range(n)]
    carrier = all(indegree[i] <= 1 for i in range(n) if i not in cyclic)
    carrier = carrier and all(indegree[i] <= 2 for i in cyclic)
    period = 1
    for cycle in sccs:
        finals = [i for i in range(n) if i not in cyclic and f[i] in cycle]
        carrier = carrier and all(i < min(cycle) for i in finals)
        if finals:
            period = math.lcm(period, len(cycle))
    return carrier, period if carrier else None, cyclic, sccs


def image_chain(f):
    image = set(range(len(f)))
    chain = []
    for _ in range(len(f) + 1):
        chain.append(image)
        image = {f[i] for i in image}
    return chain


def main():
    require(sys.flags.optimize == 0)
    require('site' not in sys.modules)
    boxes = []
    for n in range(6):
        states = list(itertools.product(range(n), repeat=n))
        rank = {state: i for i, state in enumerate(states)}
        images = [update(f) for f in states]
        successors = [rank[g] for g in images]
        parents = [[] for _ in states]
        for i, j in enumerate(successors):
            parents[j].append(i)
        blocks = list(partitions(n))
        records = []
        for i, f in enumerate(states):
            seen = {}
            j = i
            while j not in seen:
                seen[j] = len(seen)
                j = successors[j]
            entrance = seen[j]
            period = len(seen) - entrance
            recurrent = entrance == 0
            carrier, expected_period, cyclic, sccs = graph_geometry(f)
            require(recurrent == carrier)
            if carrier:
                require(period == expected_period)
                for v in range(n):
                    if v in cyclic or f[v] not in cyclic:
                        require(images[i][v] == f[v])
                    else:
                        predecessor = next(u for u in cyclic if f[u] == f[v])
                        require(images[i][v] == predecessor)
            old_chain, new_chain = image_chain(f), image_chain(images[i])
            for old, new in zip(old_chain, new_chain):
                require(old <= new)
                if recurrent:
                    require(old == new)
            for a in range(n):
                for b in range(n):
                    # Weak component equivalence independently via common forward reach.
                    def basin_equal(h):
                        av, bv = {a}, {b}
                        for _ in range(n):
                            av |= {h[v] for v in tuple(av)}
                            bv |= {h[v] for v in tuple(bv)}
                        return bool(av & bv)
                    require(basin_equal(f) == basin_equal(images[i]))
            decoded = partition_inverse(f, blocks)
            from_masks = mask_inverse(f)
            require(decoded == from_masks)
            require(sorted(rank[g] for g in decoded) == parents[i])
            for source, mask in decoded.items():
                require(update(source) == f)
                actual_mask = sum(1 << a for a in range(n)
                                  if any(source[a] == source[b] for b in range(a + 1, n)))
                require(mask == actual_mask)
            records.append({'f': list(f), 'image_rank': successors[i],
                            'entrance': entrance, 'period': period,
                            'recurrent': recurrent, 'carrier_period': expected_period,
                            'cycle_sccs': [list(c) for c in sccs],
                            'inverse_ranks': parents[i],
                            'inverse_masks': sorted(from_masks.values())})
        maximum = max(map(len, parents))
        extremizers = [i for i, p in enumerate(parents) if len(p) == maximum]
        expected_target = tuple(range(1, n)) + (0,) if n else ()
        require(maximum == (1 << (n - 1) if n else 1))
        require(extremizers == [rank[expected_target]])
        boxes.append({'n': n, 'state_count': len(states), 'partition_count': len(blocks),
                      'maximum_fibre': maximum, 'extremizer_ranks': extremizers,
                      'records': records})
    require(sum(b['state_count'] for b in boxes) == 3414)
    print(json.dumps({'schema': 'p209-review-a-independent-v1', 'checks': CHECKS,
                      'boxes': boxes}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
