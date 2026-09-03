#!/usr/bin/env python3
"""Deterministic exact breadth pilots for the P167--P171 cross-domain lane.

This file is deliberately self-contained.  It prints small complete-carrier
signatures.  The signatures are falsification pressure, never proofs or
novelty evidence.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product


ASSERTIONS = 0


def check(condition: bool) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError


def functional_signature(states, step):
    states = tuple(states)
    state_set = set(states)
    image = {step(x) for x in states}
    check(image <= state_set)
    fixed = sum(step(x) == x for x in states)
    max_tail = 0
    periods = Counter()
    depth_hist = Counter()
    for x in states:
        seen = {}
        y = x
        t = 0
        while y not in seen:
            seen[y] = t
            y = step(y)
            check(y in state_set)
            t += 1
        tail = seen[y]
        period = t - seen[y]
        max_tail = max(max_tail, tail)
        depth_hist[tail] += 1
        if tail == 0:
            periods[period] += 1
    cycles = {p: periods[p] // p for p in sorted(periods)}
    return {
        "states": len(states),
        "image": len(image),
        "fixed": fixed,
        "tail": max_tail,
        "cycles": cycles,
        "depth": dict(sorted(depth_hist.items())),
    }


def support_signature(states, successors):
    states = tuple(states)
    state_set = set(states)
    arcs = set()
    outdegrees = []
    absorbing = 0
    for x in states:
        ys = set(successors(x))
        check(bool(ys))
        check(ys <= state_set)
        outdegrees.append(len(ys))
        absorbing += ys == {x}
        arcs.update((x, y) for y in ys)
    return {
        "states": len(states),
        "arcs": len(arcs),
        "absorbing": absorbing,
        "out": (min(outdegrees), max(outdegrees)),
    }


def reduced_word(v):
    """A reduced right-simple-reflection word building v from identity."""
    a = list(v)
    reducing = []
    n = len(a)
    while True:
        hit = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                reducing.append(i)
                hit = True
        if not hit:
            break
    check(tuple(a) == tuple(range(n)))
    return tuple(reversed(reducing))


def demazure(u, v):
    a = list(u)
    for i in reduced_word(v):
        if a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return tuple(a)


def reverse_descending_runs(p):
    ans = []
    i = 0
    while i < len(p):
        j = i + 1
        while j < len(p) and p[j - 1] > p[j]:
            j += 1
        ans.extend(reversed(p[i:j]))
        i = j
    return tuple(ans)


def lehmer_encode(p):
    return tuple(sum(p[j] < p[i] for j in range(i + 1, len(p))) for i in range(len(p)))


def lehmer_decode(code):
    pool = list(range(len(code)))
    out = []
    for c in code:
        out.append(pool.pop(c))
    return tuple(out)


def odd_lehmer_fold(p):
    code = lehmer_encode(p)
    return lehmer_decode(tuple((len(p) - i - 1 - c) if c % 2 else c for i, c in enumerate(code)))


def rgs_partitions(n):
    if n == 0:
        return ((),)
    out = []

    def rec(prefix, maximum):
        if len(prefix) == n:
            blocks = [[] for _ in range(maximum + 1)]
            for x, b in enumerate(prefix):
                blocks[b].append(x)
            out.append(tuple(tuple(b) for b in blocks))
            return
        for b in range(maximum + 2):
            rec(prefix + (b,), max(maximum, b))

    rec((0,), 0)
    return tuple(out)


def normalize_partition(blocks):
    clean = [tuple(sorted(b)) for b in blocks if b]
    return tuple(sorted(clean, key=lambda b: b[0]))


def alternating_rank_split(pi):
    out = []
    for block in pi:
        out.append(block[::2])
        if len(block) >= 2:
            out.append(block[1::2])
    return normalize_partition(out)


def midpoint_gap_split(pi):
    out = []
    for block in pi:
        if len(block) <= 1:
            out.append(block)
            continue
        lo, hi = block[0], block[-1]
        left = tuple(x for x in block if 2 * x <= lo + hi)
        right = tuple(x for x in block if 2 * x > lo + hi)
        out.extend((left, right))
    return normalize_partition(out)


def successor_transfer(pi):
    k = len(pi)
    if k <= 1:
        return pi
    keep = [set(b) for b in pi]
    send = [[] for _ in pi]
    for i, block in enumerate(pi):
        if len(block) > 1:
            x = block[-1]
            keep[i].remove(x)
            send[(i + 1) % k].append(x)
    return normalize_partition(keep[i] | set(send[i]) for i in range(k))


def adjacent_size_merge(pi):
    k = len(pi)
    parent = list(range(k))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for i in range(k):
        for j in range(i + 1, k):
            if abs(len(pi[i]) - len(pi[j])) == 1:
                union(i, j)
    groups = defaultdict(set)
    for i, block in enumerate(pi):
        groups[find(i)].update(block)
    return normalize_partition(groups.values())


def block_successor_join(pi):
    """Join blocks linked by a cyclic label successor, but only from maxima."""
    n = sum(map(len, pi))
    owner = {}
    for i, block in enumerate(pi):
        for x in block:
            owner[x] = i
    parent = list(range(len(pi)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, block in enumerate(pi):
        j = owner[(block[-1] + 1) % n]
        a, b = find(i), find(j)
        if a != b:
            parent[b] = a
    groups = defaultdict(set)
    for i, block in enumerate(pi):
        groups[find(i)].update(block)
    return normalize_partition(groups.values())


def binary_words(n):
    return tuple(product((0, 1), repeat=n))


def variable_words(q, nmax):
    return tuple(w for n in range(nmax + 1) for w in product(range(q), repeat=n))


def occurrence_rank_parity(w):
    seen = Counter()
    out = []
    for x in w:
        out.append(seen[x] & 1)
        seen[x] += 1
    return tuple(out)


def run_start_mask(w):
    return tuple(1 if i == 0 or w[i] != w[i - 1] else 0 for i in range(len(w)))


def prefix_minority_mask(w):
    counts = [0, 0]
    out = []
    for x in w:
        counts[x] += 1
        out.append(int(counts[x] <= counts[1 - x]))
    return tuple(out)


def parallel_01_cancel(w):
    delete = set()
    for i in range(len(w) - 1):
        if w[i : i + 2] == (0, 1):
            delete.update((i, i + 1))
    return tuple(x for i, x in enumerate(w) if i not in delete)


def first_last_delete(w):
    positions = defaultdict(list)
    for i, x in enumerate(w):
        positions[x].append(i)
    delete = set()
    for ps in positions.values():
        delete.add(ps[0])
        delete.add(ps[-1])
    return tuple(x for i, x in enumerate(w) if i not in delete)


def perfect_unshuffle(w):
    return tuple(w[::2] + w[1::2])


def functions(n):
    return tuple(product(range(n), repeat=n))


def iterate_function(f, x, k):
    for _ in range(k):
        x = f[x]
    return x


def indegree_routing(f):
    n = len(f)
    deg = Counter(f)
    return tuple(deg[i] % n for i in range(n))


def heavy_jump(f):
    deg = Counter(f)
    return tuple(iterate_function(f, i, 1 + deg[f[i]]) for i in range(len(f)))


def reverse_preimage_jump(f):
    deg = Counter(f)
    return tuple(iterate_function(f, i, 1 + deg[i]) for i in range(len(f)))


def cycle_entry_projection(f):
    out = []
    for x in range(len(f)):
        seen = {}
        y = x
        while y not in seen:
            seen[y] = len(seen)
            y = f[y]
        cycle = []
        z = y
        while True:
            cycle.append(z)
            z = f[z]
            if z == y:
                break
        out.append(min(cycle))
    return tuple(out)


def graph_setup(n):
    edges = tuple(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}

    def edge_set(mask):
        return {e for i, e in enumerate(edges) if mask >> i & 1}

    def mask_of(es):
        return sum(1 << index[tuple(sorted(e))] for e in es)

    return edges, edge_set, mask_of


def graph_degrees(n, es):
    d = [0] * n
    for u, v in es:
        d[u] += 1
        d[v] += 1
    return d


def degree_disagreement_prune(n, mask):
    _, edge_set, mask_of = graph_setup(n)
    es = edge_set(mask)
    d = graph_degrees(n, es)
    return mask_of(e for e in es if d[e[0]] != d[e[1]])


def odd_triangle_prune(n, mask):
    _, edge_set, mask_of = graph_setup(n)
    es = edge_set(mask)
    out = []
    for u, v in es:
        c = sum(tuple(sorted((u, w))) in es and tuple(sorted((v, w))) in es for w in range(n) if w not in (u, v))
        if c & 1:
            out.append((u, v))
    return mask_of(out)


def common_neighbor_toggle(n, mask):
    edges, edge_set, mask_of = graph_setup(n)
    es = edge_set(mask)
    out = set(es)
    for u, v in edges:
        c = sum(tuple(sorted((u, w))) in es and tuple(sorted((v, w))) in es for w in range(n) if w not in (u, v))
        if c & 1:
            if (u, v) in out:
                out.remove((u, v))
            else:
                out.add((u, v))
    return mask_of(out)


def equal_degree_completion(n, mask):
    edges, edge_set, mask_of = graph_setup(n)
    d = graph_degrees(n, edge_set(mask))
    return mask_of((u, v) for u, v in edges if d[u] == d[v])


def closed_common_majority(n, mask):
    edges, edge_set, mask_of = graph_setup(n)
    es = edge_set(mask)
    nbr = [{i} for i in range(n)]
    for u, v in es:
        nbr[u].add(v)
        nbr[v].add(u)
    return mask_of((u, v) for u, v in edges if 2 * len(nbr[u] & nbr[v]) > min(len(nbr[u]), len(nbr[v])))


def local_complement_successors(n, mask):
    edges, edge_set, mask_of = graph_setup(n)
    es = edge_set(mask)
    out = []
    for pivot in range(n):
        nbr = [v for v in range(n) if v != pivot and tuple(sorted((pivot, v))) in es]
        nxt = set(es)
        for e in combinations(nbr, 2):
            e = tuple(sorted(e))
            if e in nxt:
                nxt.remove(e)
            else:
                nxt.add(e)
        out.append(mask_of(nxt))
    return out


def triples(n, k):
    return tuple(combinations(range(n), k))


def private_vertex_prune(n, mask):
    es = triples(n, 3)
    fam = [e for i, e in enumerate(es) if mask >> i & 1]
    deg = Counter(x for e in fam for x in e)
    return sum(1 << i for i, e in enumerate(es) if e in fam and any(deg[x] == 1 for x in e))


def odd_intersection_transform(n, mask):
    es = triples(n, 3)
    fam = [e for i, e in enumerate(es) if mask >> i & 1]
    return sum(1 << i for i, e in enumerate(es) if sum(bool(set(e) & set(f)) for f in fam) & 1)


def medial_triangle(p, state):
    inv2 = pow(2, -1, p)
    a, b, c = state
    return ((a + b) * inv2 % p, (b + c) * inv2 % p, (c + a) * inv2 % p)


def reciprocal_window(p, state):
    a, b = state
    d = (b - a) % p
    return (b, 0 if d == 0 else pow(d, -1, p))


def pivot_split_successors(pi):
    n = sum(map(len, pi))
    outs = []
    for x in range(n):
        blocks = []
        for b in pi:
            if x not in b or len(b) == 1:
                blocks.append(b)
            else:
                blocks.extend((tuple(y for y in b if y <= x), tuple(y for y in b if y > x)))
        outs.append(normalize_partition(blocks))
    return outs


def run_delete_successors(w):
    if not w:
        return (w,)
    outs = []
    for i in range(len(w)):
        a = i
        b = i + 1
        while a and w[a - 1] == w[i]:
            a -= 1
        while b < len(w) and w[b] == w[i]:
            b += 1
        outs.append(w[:a] + w[b:])
    return outs


def main():
    print("P167_171_COMBINATORIAL_CROSSDOMAIN_BREADTH_V1")

    perm_states = tuple(permutations(range(6)))
    deterministic = []
    deterministic.append(("C01_HDQS", perm_states, lambda p: demazure(p, p)))
    deterministic.append(("C02_PDR", perm_states, reverse_descending_runs))
    deterministic.append(("C03_OLF", perm_states, odd_lehmer_fold))

    part_states = rgs_partitions(7)
    deterministic.append(("C04_ARS", part_states, alternating_rank_split))
    deterministic.append(("C05_MGS", part_states, midpoint_gap_split))
    deterministic.append(("C06_STF", part_states, successor_transfer))
    deterministic.append(("C07_ASM", part_states, adjacent_size_merge))
    deterministic.append(("C08_BSJ", part_states, block_successor_join))

    word8 = binary_words(8)
    deterministic.append(("C09_ORP", word8, occurrence_rank_parity))
    deterministic.append(("C10_RSM", word8, run_start_mask))
    deterministic.append(("C11_PMM", word8, prefix_minority_mask))
    deterministic.append(("C12_UNS", word8, perfect_unshuffle))
    variable_binary = variable_words(2, 10)
    deterministic.append(("C13_PAC", variable_binary, parallel_01_cancel))
    variable_ternary = variable_words(3, 7)
    deterministic.append(("C14_FLD", variable_ternary, first_last_delete))

    fun_states = functions(4)
    deterministic.append(("C15_IDR", fun_states, indegree_routing))
    deterministic.append(("C16_HJP", fun_states, heavy_jump))
    deterministic.append(("C17_RPJ", fun_states, reverse_preimage_jump))
    deterministic.append(("C18_CEP", fun_states, cycle_entry_projection))

    ngraph = 5
    graph_states = tuple(range(1 << len(tuple(combinations(range(ngraph), 2)))))
    deterministic.append(("C19_DDP", graph_states, lambda g: degree_disagreement_prune(ngraph, g)))
    deterministic.append(("C20_OTP", graph_states, lambda g: odd_triangle_prune(ngraph, g)))
    deterministic.append(("C21_CNT", graph_states, lambda g: common_neighbor_toggle(ngraph, g)))
    deterministic.append(("C22_EDC", graph_states, lambda g: equal_degree_completion(ngraph, g)))
    deterministic.append(("C23_CCM", graph_states, lambda g: closed_common_majority(ngraph, g)))

    nhyp = 5
    hyp_states = tuple(range(1 << len(triples(nhyp, 3))))
    deterministic.append(("C24_PVP", hyp_states, lambda h: private_vertex_prune(nhyp, h)))
    deterministic.append(("C25_OIT", hyp_states, lambda h: odd_intersection_transform(nhyp, h)))

    p = 5
    deterministic.append(("C26_MED", tuple(product(range(p), repeat=3)), lambda x: medial_triangle(p, x)))
    deterministic.append(("C27_RCW", tuple(product(range(p), repeat=2)), lambda x: reciprocal_window(p, x)))

    for name, states, step in deterministic:
        print(name, functional_signature(states, step))

    print("K01_RLC", support_signature(graph_states, lambda g: local_complement_successors(ngraph, g)))
    print("K02_RPS", support_signature(part_states, pivot_split_successors))
    print("K03_RRD", support_signature(variable_binary, run_delete_successors))

    # Definition-level sentinels for the strongest transparent claims.
    for p in permutations(range(5)):
        y = demazure(p, p)
        check(demazure(y, y) == demazure(p, demazure(p, demazure(p, p))))
    for pi in rgs_partitions(8):
        y = alternating_rank_split(pi)
        check(max(map(len, y)) <= (max(map(len, pi)) + 1) // 2)
    print("ASSERTIONS", ASSERTIONS)
    print("STATUS PASS")


if __name__ == "__main__":
    main()
