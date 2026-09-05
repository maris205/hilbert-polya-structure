#!/usr/bin/env python3
"""Independent bounded ND1 pressure; no author/scout imports.

Neighborhood sets define the map. Kahn peeling finds recurrence.
The separate potential decoder is checked on every target for n<=4.
No larger graph box is used to replace an all-size proof.
"""
from collections import Counter, deque
from itertools import combinations, product

ASSERTIONS = 0


def check(value):
    global ASSERTIONS
    ASSERTIONS += 1
    if not value:
        raise AssertionError(ASSERTIONS)


def neighbors(n, code):
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(combinations(range(n), 2)):
        if code >> bit & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj


def encode(adj):
    return sum(1 << bit for bit, (u, v) in enumerate(combinations(range(len(adj)), 2))
               if v in adj[u])


def image(adj):
    out = [set() for _ in adj]
    for u, v in combinations(range(len(adj)), 2):
        if len(adj[u] ^ adj[v]) == 1:
            out[u].add(v)
            out[v].add(u)
    return out


def components(adj):
    unseen = set(range(len(adj)))
    result = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        group, todo = [root], [root]
        while todo:
            for v in sorted(adj[todo.pop()]):
                if v in unseen:
                    unseen.remove(v)
                    group.append(v)
                    todo.append(v)
        result.append(sorted(group))
    return result


def potential_inverse(n, target):
    """All singleton witness labels, then one bit per component pair.

    This is deliberately NOT claimed to solve all-size fibre enumeration.
    Empty target leaves every input edge bit unconstrained before exclusion.
    """
    h = neighbors(n, target)
    edges = [(u, v) for u, v in combinations(range(n), 2) if v in h[u]]
    groups = components(h)
    group_of = {v: i for i, c in enumerate(groups) for v in c}
    roots = [c[0] for c in groups]
    answers = []
    options = [[w for w in range(n) if w not in (u, v)] for u, v in edges]
    for labels in product(*options):
        edge_label = {e: 1 << w for e, w in zip(edges, labels)}
        p = [None] * n
        valid = True
        for root in roots:
            p[root] = 0
            todo = [root]
            while todo:
                u = todo.pop()
                for v in h[u]:
                    value = p[u] ^ edge_label[tuple(sorted((u, v))) ]
                    if p[v] is None:
                        p[v] = value
                        todo.append(v)
                    elif p[v] != value:
                        valid = False
        if not valid:
            continue
        for u, v in combinations(range(n), 2):
            c, d = group_of[u], group_of[v]
            if c == d:
                if (((p[v] >> v) ^ (p[u] >> v) ^
                     (p[u] >> u) ^ (p[v] >> u)) & 1):
                    valid = False
                if ((p[u] ^ p[v]).bit_count() == 1) != (v in h[u]):
                    valid = False
            else:
                r, s = roots[c], roots[d]
                if (((p[v] >> r) ^ (p[u] >> v) ^
                     (p[u] >> s) ^ (p[v] >> u)) & 1):
                    valid = False
        if not valid:
            continue
        component_pairs = list(combinations(range(len(groups)), 2))
        for bits in product((0, 1), repeat=len(component_pairs)):
            b = dict(zip(component_pairs, bits))
            a = [set() for _ in range(n)]
            for u, v in combinations(range(n), 2):
                c, d = group_of[u], group_of[v]
                if c == d:
                    val = ((p[v] >> v) ^ (p[u] >> v)) & 1
                else:
                    val = b[tuple(sorted((c, d)))] ^ (((p[v] >> roots[c]) ^ (p[u] >> v)) & 1)
                if val:
                    a[u].add(v)
                    a[v].add(u)
            if all(len(a[u] ^ a[v]) != 1 for u, v in combinations(range(n), 2)
                   if group_of[u] != group_of[v]):
                answers.append(encode(a))
    check(len(answers) == len(set(answers)))
    return set(answers)


def graph_census(f):
    indegree = Counter(f)
    queue = deque(v for v in range(len(f)) if indegree[v] == 0)
    peeled = []
    while queue:
        u = queue.popleft()
        peeled.append(u)
        indegree[f[u]] -= 1
        if indegree[f[u]] == 0:
            queue.append(f[u])
    depth = [0] * len(f)
    for u in reversed(peeled):
        depth[u] = 1 + depth[f[u]]
    core = {u for u in range(len(f)) if indegree[u] > 0}
    cycles = Counter()
    todo = set(core)
    while todo:
        u = start = min(todo)
        length = 0
        while True:
            todo.remove(u)
            length += 1
            u = f[u]
            if u == start:
                break
        cycles[length] += 1
    return core, max(depth), cycles


def main():
    print('ND1_INDEPENDENT_BOUNDED_PRESSURE / NO_PROMOTION')
    print('map=neighborhood_sets; graph=Kahn; inverse=component_XOR_potentials')
    print('scope=all_graphs_n0..6; full_target_decoder_n0..4; no_larger_box')
    for n in range(7):
        size = 1 << (n * (n - 1) // 2)
        f, fibres = [], {}
        for code in range(size):
            a = neighbors(n, code)
            h = image(a)
            y = encode(h)
            f.append(y)
            fibres.setdefault(y, set()).add(code)
            check((code & y) == 0)
            for u, v in combinations(range(n), 2):
                check(v not in h[u] or (len(a[u]) - len(a[v])) % 2 != 0)
                check(a[u] != a[v] or h[u] == h[v])
                if a[u] != a[v]:
                    common_types = {frozenset(a[w]) for w in h[u] & h[v]}
                    check(len(common_types) <= 2)
            if n <= 4:
                check(encode(image(a)) == y)
        core, height, cycles = graph_census(f)
        expected_core = {0}
        if n >= 4:
            for c, z in product(range(n), repeat=2):
                if c == z:
                    continue
                star = [set() for _ in range(n)]
                for v in range(n):
                    if v not in (c, z):
                        star[c].add(v)
                        star[v].add(c)
                expected_core.add(encode(star))
        check(core == expected_core)
        check([i for i in range(size) if f[i] == i] == [0])
        largest = max(map(len, fibres.values()))
        maximizers = sorted(y for y, sources in fibres.items() if len(sources) == largest)
        check(maximizers == [0])
        if n <= 4:
            for target in range(size):
                check(potential_inverse(n, target) == fibres.get(target, set()))
        print(f'n={n} states={size} image={len(fibres)} recurrent={len(core)} '
              f'height={height} cycles={sorted(cycles.items())} '
              f'empty_fibre={len(fibres[0])} maximum={largest} maximizers={maximizers}')
    print(f'assertions={ASSERTIONS}')
    print('status=PASS_BOUNDED_CONTROL')
    print('disposition=NO_PROMOTION; all_size_exhaustion=OPEN; max_fibre_theorem=OPEN')


if __name__ == '__main__':
    main()
