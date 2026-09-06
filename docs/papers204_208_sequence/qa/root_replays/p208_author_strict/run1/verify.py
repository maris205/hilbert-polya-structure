#!/usr/bin/env python3
"""P208 author check, adapted from original author verify_ofs.py.
Tuple F/G/P/inverse and geometric sweep are reused with attribution.
Full graph/source-set stdout and parity checks are paper-local additions.
No candidate/review implementation or external data is imported.
"""
import hashlib
import itertools
import json
import math
import sys
from collections import Counter, defaultdict, deque
from functools import lru_cache

E = ()
C = (E, E)
CHECKS = 0


def check(test, detail=None):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError((CHECKS, detail))


@lru_cache(None)
def trees(m):
    if m == 0:
        return (E,)
    return tuple((a, b) for i in range(m)
                 for a in trees(i) for b in trees(m-1-i))


def size(t):
    return 1+size(t[0])+size(t[1]) if t else 0


def comb(n):
    t = E
    for _ in range(n-1):
        t = (t, E)
    return t


def right_comb(n):
    t = E
    for _ in range(n-1):
        t = (E, t)
    return t


def is_comb(t):
    while t:
        if t[1]:
            return False
        t = t[0]
    return True


def ls(t):
    rev = []
    while t:
        t, r = t
        rev.append(r)
    return tuple(reversed(rev))


def fold(branches):
    t = E
    for b in branches:
        t = (t, b)
    return t


def first(t, a):
    return (first(t[0], a), t[1]) if t else a


@lru_cache(None)
def prod(bs):
    if len(bs) == 2:
        return f((bs[0], bs[1]))
    return first(g(bs[-1]), prod(bs[:-1]))


@lru_cache(None)
def f(t):
    if not t or t == C:
        return t
    bs = ls(t)
    if len(bs) >= 2:
        return (E, prod(bs))
    cs = ls(bs[0])
    if len(cs) == 1:
        return first(g(cs[0]), C)
    return (C, prod(cs))


def g(t):
    return f((E, t))


def kmap(t):
    if not t:
        return E
    # Same-size form: no F/G call evaluates a tree larger than t.
    if t[0]:
        return g(prod(ls(t)))
    left, right = g(t[1])
    return first(g(right), comb(size(left)+1))


def canon(n):
    if n <= 2:
        return comb(n)
    return (C, canon(n-2))


def sharp(n):
    t = (E, C)
    for _ in range(n-3):
        t = (t, E)
    return t


def in_class(t):
    return size(t) <= 1 or bool(t[0]) and is_comb(t[0])


@lru_cache(None)
def h(t):
    if not t:
        return 1
    bs = ls(t)
    positions = [i for i, b in enumerate(bs) if b]
    if not positions:
        return 2**(len(bs)-1)
    gaps = [positions[0]]
    gaps += [b-a-1 for a, b in zip(positions, positions[1:])]
    gaps += [len(bs)-1-positions[-1]]
    if any(a == 0 for a in gaps[1:-1]):
        return 0
    exponent = max(gaps[0]-1, 0)+max(gaps[-1]-1, 0)
    exponent += sum(a-1 for a in gaps[1:-1])
    return 2**exponent * math.prod(h(bs[i]) for i in positions)


def fibre_count(t):
    if not t:
        return 1
    return h(t[1]) if is_comb(t[0]) else 0


@lru_cache(None)
def inverse_f(t):
    if not t:
        return (E,)
    left, right = t
    if not is_comb(left):
        return ()
    l = size(left)+1
    if not right:
        return (right_comb(size(t)+1),)
    sources = []
    for bs in inverse_product(right):
        source = fold(bs)
        for _ in range(l-1):
            source = (E, source)
        sources.append(source)
    return tuple(sources)


@lru_cache(None)
def inverse_g(t):
    if t == C:
        return (E,)
    if not t or not t[0]:
        return ()
    sources = inverse_f(t)
    check(all(not s[0] for s in sources), ("G extraction", t))
    return tuple(s[1] for s in sources)


@lru_cache(None)
def inverse_product(t):
    bs = ls(t)
    if not bs:
        return ()
    out = []
    for mask in range(1 << (len(bs)-1)):
        cut = [0]+[j+1 for j in range(len(bs)-1) if mask >> j & 1]+[len(bs)]
        blocks = [fold(bs[a:b]) for a, b in zip(cut, cut[1:])]
        seeds = inverse_f(blocks[0])
        tails = [inverse_g(b) for b in blocks[1:]]
        for seed in seeds:
            for rest in itertools.product(*tails):
                out.append((seed[0], seed[1])+rest)
    return tuple(out)


def diagonals(t):
    found = []
    def walk(s, a, top=False):
        if not s:
            return a+1
        b = walk(s[0], a)
        c = walk(s[1], b)
        if not top:
            found.append((a, c))
        return c
    walk(t, 0, True)
    return tuple(sorted(found))


def literal_sweep(ds, n):
    edges = set(ds) | {(j, j+1) for j in range(n-1)} | {(0, n-1)}
    for a, b in ds:
        check((a, b) in edges, ("unvisited old edge", n, ds, a, b))
        adjacent = [v for v in range(n) if v not in (a, b)
                    and tuple(sorted((a, v))) in edges
                    and tuple(sorted((b, v))) in edges]
        check(len(adjacent) == 2, ("incident triangles", n, ds, a, b, adjacent))
        new_edge = tuple(sorted(adjacent))
        check(new_edge not in edges, ("proper flip", n, ds, new_edge))
        edges.remove((a, b))
        edges.add(new_edge)
    return tuple(sorted((a, b) for a, b in edges if b-a > 1 and (a, b) != (0, n-1)))


def graph_analysis(states, nxt):
    indeg = Counter(nxt.values())
    degree = {t: indeg[t] for t in states}
    queue = deque(t for t in states if degree[t] == 0)
    removed = []
    while queue:
        t = queue.popleft()
        removed.append(t)
        degree[nxt[t]] -= 1
        if degree[nxt[t]] == 0:
            queue.append(nxt[t])
    core = {t for t in states if degree[t]}
    height = {t: 0 for t in core}
    for t in reversed(removed):
        height[t] = 1+height[nxt[t]]
    return indeg, core, height


def image_number(m):
    return sum(math.comb(2*j, j)//(j+1)*math.comb(m+j, 3*j+1)
               for j in range((m-1)//2+1))


def main():
    check(sys.flags.optimize == 0 and sys.flags.isolated == 1)
    check(sys.dont_write_bytecode)
    check(f(E) == E and g(E) == C and kmap(E) == E)
    check(kmap(C) == C)
    rows = []
    total_states = total_decoded = 0
    for n in range(3, 11):
        m, N = n-2, n-1
        states = trees(m)
        by_edges = {diagonals(t): t for t in states}
        check(len(by_edges) == len(states))
        check(len(states) == math.comb(2*m, m)//(m+1))
        nxt = {}
        reverse = defaultdict(set)
        for t in states:
            out = literal_sweep(diagonals(t), n)
            check(out in by_edges, ("carrier", n, out))
            nxt[t] = by_edges[out]
            reverse[nxt[t]].add(t)
            check(nxt[t] == f(t), ("dictionary", n, t))
        counts, core, height = graph_analysis(states, nxt)
        knext = {t: kmap(t) for t in states}
        check(all(y in knext for y in knext.values()), ("K size", n))
        _, kcore, kheight = graph_analysis(states, knext)
        expected_core = {C} if n == 3 else {canon(N), (E, canon(N-1))}
        check(core == expected_core, ("full core", n, core))
        check(kcore == {canon(N)}, ("K core", n))
        max_height = 0 if n <= 4 else n-2
        check(max(height.values()) == max_height, ("sharp clock", n))
        check(len(counts) == image_number(m), ("image count", n))
        for t in states:
            decoded = inverse_f(t)
            check(len(decoded) == len(set(decoded)), ("decoder duplicates", n, t))
            check(set(decoded) == reverse[t], ("whole inverse set", n, t))
            check(counts[t] == fibre_count(t), ("evaluated fibres", n, t))
            check(all(size(s) == m for s in decoded), ("decoder size", n, t))
            if counts[t]:
                check(counts[t] & (counts[t]-1) == 0, ("power two", n, t))
            if m <= 6:
                check(g(g(t)) == (C, kmap(t)), ("K defining equation", n, t))
                check(kmap((C, t)) == (C, kmap(t)), ("frozen prefix", n, t))
            if m <= 7:
                check(kmap(g(t)) == g(kmap(t)), ("KG", n, t))
            if t[0]:
                check(f(f(t)) == kmap(t), ("nonleaf-left square", n, t))
            else:
                check(f(f(t)) == (E, kmap(t[1])), ("leaf-left square", n, t))
            if N >= 3:
                check(in_class(kmap(t)), ("K image", n, t))
                check(kheight[t] <= N//2, ("K all clock", n, t))
                if in_class(t):
                    check(kmap(t)[0] == C and in_class(kmap(t)[1]), ("K C closure", n, t))
                    check(kheight[t] <= (N-2)//2, ("K C clock", n, t))
                if counts[t]:
                    check(height[t] <= N-2, ("image clock", n, t))
            total_decoded += len(decoded)
        maximum = max(counts.values())
        maximizers = {t for t in states if counts[t] == maximum}
        if n >= 5:
            check(maximum == 2**(n-4))
            check(maximizers == {(E, comb(m))}, ("all extremizers", n))
            witness = sharp(N)
            check(height[witness] == n-2, ("sharp witness", n))
            check(f(witness) == (E, sharp(N-1)))
            if N == 4:
                check(kmap(witness) == comb(4))
            else:
                check(kmap(witness) == (C, sharp(N-2)))
        else:
            check(maximum == 1 and maximizers == set(states))
        if n >= 5:
            z = witness
            orbit = [diagonals(z)]
            for _ in range(n-2):
                z = nxt[z]
                orbit.append(diagonals(z))
            tail = comb(4)
            for _ in range(N//2-2):
                tail = (C, tail)
            at_time = witness
            for _ in range(N-2):
                at_time = nxt[at_time]
            expected_tail = tail if N % 2 == 0 else (E, tail)
            check(at_time == expected_tail, ("both parity tails", n))
            check(at_time not in core and nxt[at_time] in core)
        else:
            orbit = None
        literal_table = [(diagonals(t), diagonals(nxt[t]), height[t], counts[t]) for t in states]
        full_records = [{"tree": t, "diagonals": diagonals(t),
                         "next_diagonals": diagonals(nxt[t]),
                         "height": height[t], "fibre": counts[t],
                         "source_diagonals": sorted(diagonals(s) for s in inverse_f(t)),
                         "K_next_diagonals": diagonals(knext[t]),
                         "K_height": kheight[t]} for t in states]
        digest = hashlib.sha256(json.dumps(literal_table, separators=(",", ":")).encode()).hexdigest()
        rows.append({"n": n, "states": len(states), "image": len(counts),
                     "core_diagonals": sorted(diagonals(t) for t in core),
                     "maximum_height": max_height, "maximum_fibre": maximum,
                     "all_maximum_targets": sorted(diagonals(t) for t in maximizers),
                     "fibre_histogram": sorted(Counter(counts[t] for t in states).items()),
                     "height_histogram": sorted(Counter(height.values()).items()),
                     "K_maximum_height": max(kheight.values()),
                     "sharp_witness_diagonals": diagonals(sharp(N)) if n >= 5 else None,
                     "literal_transition_depth_fibre_sha256": digest,
                     "sharp_witness_full_orbit": orbit,
                     "complete_graph_and_sources": full_records})
        total_states += len(states)
    check(total_states == total_decoded)
    print(json.dumps({"role": "standalone_author_check_not_independent_review",
                      "boxes": "original_complete_n3_through_n10",
                      "assertions": CHECKS, "total_states": total_states,
                      "total_decoded_predecessors": total_decoded, "rows": rows},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
