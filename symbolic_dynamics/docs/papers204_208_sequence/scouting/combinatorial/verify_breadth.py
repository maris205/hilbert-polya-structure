#!/usr/bin/env python3
"""Original exact finite scouts; stdout is deterministic JSON, not a proof.

No dependencies.  Each box is a complete carrier, not a random sample.
Tree states use their preorder outdegree word; labelled trees use Prüfer codes.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations, product
import hashlib
import json


def census(name, size, states, update, identity=None):
    states = list(states)
    indices = {x: i for i, x in enumerate(states)}
    assert len(indices) == len(states)
    edges = [indices[update(x)] for x in states]
    depths = [-1] * len(states)
    periods = [0] * len(states)
    cycle_counts = Counter()
    for start in range(len(states)):
        if depths[start] >= 0:
            continue
        path, local = [], {}
        x = start
        while depths[x] < 0 and x not in local:
            local[x] = len(path)
            path.append(x)
            x = edges[x]
        if x in local:
            first = local[x]
            period = len(path) - first
            cycle_counts[period] += 1
            for y in path[first:]:
                depths[y], periods[y] = 0, period
            path = path[:first]
        for y in reversed(path):
            depths[y] = depths[edges[y]] + 1
            periods[y] = periods[edges[y]]
    fibres = Counter(edges)
    max_depth, max_fibre = max(depths), max(fibres.values())
    if identity is not None:
        for x in states:
            assert identity(x, update), (name, size, x)
    assert sum(fibres.values()) == len(states)
    assert sum(p * c for p, c in cycle_counts.items()) == depths.count(0)
    return {
        "candidate": name, "size": size, "states": len(states),
        "image": len(fibres), "recurrent": depths.count(0),
        "cycles": dict(sorted(cycle_counts.items())), "max_tail": max_depth,
        "depth_layers": dict(sorted(Counter(depths).items())),
        "deepest_count": depths.count(max_depth),
        "deepest_witness": states[depths.index(max_depth)],
        "max_fibre": max_fibre,
        "max_fibre_count": sum(c == max_fibre for c in fibres.values()),
        "max_fibre_target": states[next(i for i, c in fibres.items() if c == max_fibre)],
        "edges_sha256": hashlib.sha256(",".join(map(str, edges)).encode()).hexdigest(),
    }


def decreasing_run_front(w):
    result, i = [], 0
    while i < len(w):
        j = i + 1
        while j < len(w) and w[j-1] > w[j]:
            j += 1
        result.extend(w[j-1:j] + w[i:j-1])
        i = j
    return tuple(result)


def alternating_prefix_rank(w):
    total, scores = 0, []
    for i, value in enumerate(w):
        total += value if i % 2 == 0 else -value
        scores.append(total)
    order = sorted(range(len(w)), key=lambda i: (scores[i], i))
    result = [0] * len(w)
    for rank, i in enumerate(order, 1):
        result[i] = rank
    return tuple(result)


def insertion_tableau(w):
    rows = []
    for value in w:
        for row in rows:
            j = next((j for j, a in enumerate(row) if a > value), len(row))
            if j == len(row):
                row.append(value)
                break
            row[j], value = value, row[j]
        else:
            rows.append([value])
    return rows


def transpose_insertion_read(w):
    p = insertion_tableau(w)
    transpose = [[row[j] for row in p if len(row) > j] for j in range(len(p[0]))]
    return tuple(a for row in reversed(transpose) for a in row)


@lru_cache(None)
def plane_words(n):
    if n == 1:
        return ((0,),)
    result = []
    def compositions(total, k, prefix=()):
        if k == 0:
            if total == 0:
                yield prefix
            return
        for first in range(1, total-k+2):
            yield from compositions(total-first, k-1, prefix+(first,))
    for k in range(1, n):
        for sizes in compositions(n-1, k):
            for children in product(*(plane_words(s) for s in sizes)):
                result.append((k,) + sum(children, ()))
    return tuple(result)


def parse_tree(w):
    pos = 0
    def read():
        nonlocal pos
        degree = w[pos]
        pos += 1
        return tuple(read() for _ in range(degree))
    root = read()
    assert pos == len(w)
    return root


def breadth_preorder(w, degree_sort=False):
    queue = deque([parse_tree(w)])
    result = []
    while queue:
        children = queue.popleft()
        result.append(len(children))
        queue.extend(sorted(children, key=lambda c: -len(c)) if degree_sort else children)
    return tuple(result)


def depth_prufer(code):
    n = len(code) + 2
    degree = [1] * n
    for x in code:
        degree[x] += 1
    adj = [[] for _ in range(n)]
    for x in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        adj[leaf].append(x)
        adj[x].append(leaf)
        degree[leaf] -= 1
        degree[x] -= 1
    a, b = [i for i in range(n) if degree[i] == 1]
    adj[a].append(b)
    adj[b].append(a)
    depth, queue = [-1] * n, deque([0])
    depth[0] = 0
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if depth[y] < 0:
                depth[y] = depth[x] + 1
                queue.append(y)
    return tuple(depth[1:n-1])


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        for rest in matchings(vertices[1:j] + vertices[j+1:]):
            yield ((a, b),) + rest


def length_half_pair(matching):
    edges = sorted(matching, key=lambda e: (e[1]-e[0], e))
    word = [a for a, _ in edges] + [b for _, b in edges]
    return tuple(sorted(tuple(sorted(word[i:i+2])) for i in range(0, len(word), 2)))


def partitions(n):
    def rec(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            yield from rec(i+1, blocks[:j]+[blocks[j]+[i]]+blocks[j+1:])
        yield from rec(i+1, blocks+[[i]])
    yield from rec(0, [])


def median_transfer(blocks):
    k = len(blocks)
    if k <= 1:
        return blocks
    result = [set(b) for b in blocks]
    for j, block in enumerate(blocks):
        if len(block) > 1:
            a = block[(len(block)-1)//2]
            result[j].remove(a)
            result[(j+1) % k].add(a)
    return tuple(sorted((tuple(sorted(b)) for b in result), key=lambda b: b[0]))


def main():
    rows = []
    for n in range(1, 9):
        for name, update, identity in (
            ("C01_DRF", decreasing_run_front, None),
            ("C02_APR", alternating_prefix_rank, None),
            ("C08_TIR", transpose_insertion_read, lambda x, f: f(f(f(x))) == f(x)),
        ):
            rows.append(census(name, n, permutations(range(1, n+1)), update, identity))
    for n in range(1, 11):
        for name, flag in (("C03_BPC", False), ("C04_BDC", True)):
            rows.append(census(name, n, plane_words(n), lambda w, flag=flag: breadth_preorder(w, flag)))
    for n in range(2, 8):
        rows.append(census("C05_DPF", n, product(range(n), repeat=n-2), depth_prufer))
    for m in range(1, 7):
        rows.append(census("C06_LHP", m, matchings(tuple(range(2*m))), length_half_pair))
    for n in range(1, 9):
        rows.append(census("C07_SMT", n, partitions(n), median_transfer))
    print(json.dumps({"schema": 1, "scope": "complete finite carriers; no theorem/novelty certification", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
