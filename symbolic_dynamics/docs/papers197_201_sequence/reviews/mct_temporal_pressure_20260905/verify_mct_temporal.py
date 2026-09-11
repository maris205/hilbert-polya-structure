#!/usr/bin/env python3
"""Temporal pressure only. Own tuple-edge probe extended with graph peeling.

No candidate-author imports, no full graph box above n=6, no inverse claims.
This is the proof contributor's verifier, not a separate manuscript review.
"""
from collections import Counter, deque
from itertools import combinations


ASSERTIONS = 0


def check(statement, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(context)


def choose(edges, triples):
    for tri in triples:
        values = [edge in edges for edge in combinations(tri, 2)]
        if values[0] == values[1] == values[2]:
            return tri, int(values[0])
    return None, None


def sharp_edges(n):
    vertices = list(reversed(range(1, n)))
    s = [0, 0] + [(i-1) % 2 for i in range(2, n-1)]
    edges = {(0, vertices[i]) for i in range(n-1) if s[i]}
    for i, j in combinations(range(n-1), 2):
        colour = (i % 2 if j == i+1 else
                  1-s[i] if s[i] == s[j] else s[i])
        if colour:
            edges.add(tuple(sorted((vertices[i], vertices[j]))))
    return edges, vertices


def box(n):
    pairs = tuple(combinations(range(n), 2))
    triples = tuple(combinations(range(n), 3))
    position = {e: i for i, e in enumerate(pairs)}
    total = 1 << len(pairs)
    selected, colours, forward = [], [], []
    for state in range(total):
        edges = {e for i, e in enumerate(pairs) if state >> i & 1}
        tri, colour = choose(edges, triples)
        selected.append(tri)
        colours.append(colour)
        mask = sum(1 << position[e] for e in combinations(tri, 2)) if tri else 0
        forward.append(state ^ mask)
    indegree = [0]*total
    for target in forward:
        indegree[target] += 1
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    peeled = []
    while queue:
        state = queue.popleft()
        peeled.append(state)
        target = forward[state]
        indegree[target] -= 1
        if not indegree[target]:
            queue.append(target)
    depth = [0]*total
    for state in reversed(peeled):
        depth[state] = depth[forward[state]] + 1
    cycles, seen = Counter(), set()
    for state in range(total):
        if not indegree[state] or state in seen:
            continue
        point, size = state, 0
        while point not in seen:
            seen.add(point)
            size += 1
            point = forward[point]
        cycles[size] += 1
        check(size in (1, 2), ('cycle length', n, state, size))
        check((size == 1) == (selected[state] is None), ('fixed selector', n, state))
    for initial in range(total):
        state, path, path_colours = initial, [], []
        while selected[state] is not None:
            tri = selected[state]
            path.append(tri)
            path_colours.append(colours[state])
            target = forward[state]
            if selected[target] == tri:
                check(forward[target] == state, ('reciprocal', n, initial))
                break
            check(selected[target] < tri, ('strict decrease', n, initial))
            state = target
        strict = max(0, len(path)-1)
        check(strict == depth[initial], ('peeling versus trace', n, initial))
        check(strict <= max(0, n-3), ('sharp upper', n, initial))
        visited = set(path[0]) if path else set()
        for index, (a, b) in enumerate(zip(path, path[1:])):
            old, new = set(a), set(b)
            check(len(old & new) == 2, ('shared edge', n, initial, index))
            check(max(new-old) < max(old-new), ('replacement order', n, initial, index))
            check(not ((new-old) & visited), ('global no return', n, initial, index))
            check(path_colours[index] != path_colours[index+1], ('alternation', n, initial))
            if index >= 1:
                check(min(a) == min(b), ('no late minimum drop', n, initial))
                check(set(path[index-1]) & old != old & new, ('no repeated shared edge', n, initial))
            visited |= new
        if len(path) > 1:
            anchor = min(path[1])
            check(all(min(t) == anchor for t in path[1:]), ('stable anchor', n, initial))
    check(max(depth) == max(0, n-3), ('exact maximum', n))
    print(f'n={n} states={total} fixed={cycles[1]} two_cycles={cycles[2]} H={max(depth)}')


def family():
    for n in range(3, 61):
        edges, vertices = sharp_edges(n)
        triples = tuple(combinations(range(n), 3))
        for t in range(n-2):
            tri, colour = choose(edges, triples)
            expected = tuple(sorted((0, vertices[t], vertices[t+1])))
            check((tri, colour) == (expected, t % 2), ('uniform witness', n, t))
            edges ^= set(combinations(tri, 2))
        tri, colour = choose(edges, triples)
        check(tri == (0, 1, 2), ('last reciprocal selector', n))
        check(colour == (n-2) % 2, ('last reciprocal colour', n))
    print('symbolic_family=3..60; full_graph_boxes=0..6')


def main():
    for n in range(7):
        box(n)
    family()
    print('scope=temporal_pressure_only; independent_stage1=NOT_CLAIMED')
    print(f'assertions={ASSERTIONS}')
    print('status=PASS')


if __name__ == '__main__':
    main()
