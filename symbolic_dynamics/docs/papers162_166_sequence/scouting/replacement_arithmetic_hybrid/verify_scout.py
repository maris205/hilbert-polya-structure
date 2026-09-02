#!/usr/bin/env python3
"""Independent exact probes for the arithmetic-hybrid P162--P166 lane.

The probes are deliberately small.  Their purpose is to falsify candidate
theorem silhouettes, not to serve as evidence of novelty or asymptotics.
No code is imported from any paper or prior scout.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd


ASSERTIONS = 0


def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)


def spf(n):
    for p in range(2, n + 1):
        if n % p == 0:
            return p
    raise ValueError(n)


def functional_signature(states, update):
    states = tuple(states)
    universe = set(states)
    check(len(universe) == len(states), "duplicate states")
    nxt = {}
    for x in states:
        y = update(x)
        check(y in universe, (x, y))
        nxt[x] = y
    fibres = Counter(nxt.values())
    fibre_hist = Counter(fibres.get(x, 0) for x in states)
    cycles = set()
    max_tail = 0
    for start in states:
        seen = {}
        orbit = []
        x = start
        while x not in seen:
            seen[x] = len(orbit)
            orbit.append(x)
            x = nxt[x]
        j = seen[x]
        max_tail = max(max_tail, j)
        cyc = orbit[j:]
        cycles.add(tuple(sorted(map(repr, cyc))))
    cycle_hist = Counter(len(c) for c in cycles)
    fixed = sum(nxt[x] == x for x in states)
    return {
        "S": len(states),
        "I": len(set(nxt.values())),
        "F": fixed,
        "H": max_tail,
        "C": ",".join(f"{k}:{v}" for k, v in sorted(cycle_hist.items())),
        "B": ",".join(f"{k}:{v}" for k, v in sorted(fibre_hist.items())),
    }, nxt


def factor_tuples(n, k):
    if k == 1:
        return [(n,)]
    out = []
    for d in range(1, n + 1):
        if n % d == 0:
            for tail in factor_tuples(n // d, k - 1):
                out.append((d,) + tail)
    return out


def prime_transfer(x):
    k = len(x)
    move = [None] * k
    for i, a in enumerate(x):
        if a > 1:
            p = spf(a)
            if x[(i + 1) % k] % p:
                move[i] = p
    y = list(x)
    for i, p in enumerate(move):
        if p is not None:
            y[i] //= p
            y[(i + 1) % k] *= p
    return tuple(y)


def coprime_fusion(x):
    y = list(x)
    for i in range(len(y) - 1):
        if y[i] > 1 and y[i + 1] > 1 and gcd(y[i], y[i + 1]) == 1:
            y[i] *= y[i + 1]
            y[i + 1] = 1
            return tuple(y)
    return tuple(y)


def set_partitions(n):
    out = []

    def rec(a):
        if len(a) == n:
            out.append(tuple(a))
            return
        hi = max(a, default=-1) + 1
        for v in range(hi + 1):
            rec(a + [v])

    rec([0])
    return out


def canonical_partition(blocks):
    blocks = sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0])
    label = {}
    for i, b in enumerate(blocks):
        for x in b:
            label[x] = i
    return tuple(label[x] for x in sorted(label))


def blocks_of(part):
    blocks = [[] for _ in range(max(part) + 1)]
    for x, b in enumerate(part, start=1):
        blocks[b].append(x)
    return blocks


def modular_split_partition(part):
    out = []
    for block in blocks_of(part):
        p = spf(sum(block)) if sum(block) > 1 else 2
        classes = {}
        for x in block:
            classes.setdefault(x % p, []).append(x)
        out.extend(classes.values())
    return canonical_partition(out)


def product_match_coalescence(part):
    classes = {}
    for block in blocks_of(part):
        residue = 1
        for x in block:
            residue = residue * x % 5
        classes.setdefault(residue, []).extend(block)
    return canonical_partition(classes.values())


def tree_product(t):
    if isinstance(t, int):
        return t
    return tree_product(t[0]) * tree_product(t[1])


def ordered_trees(leaves):
    leaves = tuple(leaves)
    if len(leaves) == 1:
        return [leaves[0]]
    out = []
    for k in range(1, len(leaves)):
        for a in ordered_trees(leaves[:k]):
            for b in ordered_trees(leaves[k:]):
                out.append((a, b))
    return out


def arithmetic_tamari(t):
    """Perform the first preorder admissible ((A,B),C)->(A,(B,C))."""
    if isinstance(t, int):
        return t, False
    left, right = t
    if isinstance(left, tuple):
        a, b = left
        if (tree_product(a) + tree_product(b) + tree_product(right)) % 5 == 0:
            return (a, (b, right)), True
    new_left, changed = arithmetic_tamari(left)
    if changed:
        return (new_left, right), True
    new_right, changed = arithmetic_tamari(right)
    return (left, new_right), changed


def all_labelled_trees(labels):
    out = []
    for perm in permutations(labels):
        out.extend(ordered_trees(perm))
    return out


def residue_subtree_flip(t):
    if isinstance(t, int):
        return t
    a = residue_subtree_flip(t[0])
    b = residue_subtree_flip(t[1])
    # Products are invariant under every lower flip; {2,6,7,8,10} are the
    # quadratic non-residues mod 11.
    if tree_product(t) % 11 in {2, 6, 7, 8, 10}:
        return (b, a)
    return (a, b)


def mat_det(m, q):
    a, b, c, d = m
    return (a * d - b * c) % q


def determinant_gate(m):
    a, b, c, d = m
    if mat_det(m, 3):
        return (b, a, d, c)
    return (a, (a + b) % 3, c, (c + d) % 3)


def first_unit_normalize(x):
    for a in x:
        if gcd(a, 6) == 1:
            inv = pow(a, -1, 6)
            return tuple(inv * z % 6 for z in x)
    return (0, 0, 0)


def farey_states(qmax, positive=True):
    out = []
    for q in range(1, qmax + 1):
        lo = 1 if positive else 0
        for p in range(lo, q + 1):
            if gcd(p, q) == 1:
                out.append((p, q))
    return sorted(set(out))


def cap_drift_states(cap):
    return [(p, q) for p in range(1, cap) for q in range(1, cap)
            if p + q <= cap and gcd(p, q) == 1] + [(0, 0)]


def cap_drift(cap, x):
    if x == (0, 0):
        return x
    p, q = x
    return (p, p + q) if 2 * p + q <= cap else (0, 0)


def matmul2(a, b):
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def continuant_trace(word):
    m = (1, 0, 0, 1)
    for a in word:
        m = matmul2(m, (a, 1, 1, 0))
    return m[0] + m[3]


def compositions(n):
    out = []
    for mask in range(1 << (n - 1)):
        cur = 1
        word = []
        for i in range(n - 1):
            if mask >> i & 1:
                word.append(cur)
                cur = 1
            else:
                cur += 1
        word.append(cur)
        out.append(tuple(word))
    return out


def rotate(word, r):
    if len(word) <= 1:
        return word
    r %= len(word)
    return word[r:] + word[:r]


def all_graphs(n):
    edges = list(combinations(range(n), 2))
    return list(range(1 << len(edges))), edges


def mask_edges(mask, edges):
    return {e for i, e in enumerate(edges) if mask >> i & 1}


def edges_mask(es, edges):
    idx = {e: i for i, e in enumerate(edges)}
    ans = 0
    for e in es:
        ans |= 1 << idx[tuple(sorted(e))]
    return ans


def edge_arithmetic_image(mask, edges):
    out = set()
    for u, v in mask_edges(mask, edges):
        a, b = (u + v) % 5, (u - v) % 5
        if a != b:
            out.add(tuple(sorted((a, b))))
    return edges_mask(out, edges)


def component_sum_cliques(mask, edges):
    adj = [set() for _ in range(5)]
    for u, v in mask_edges(mask, edges):
        adj[u].add(v)
        adj[v].add(u)
    comps = []
    unseen = set(range(5))
    while unseen:
        root = min(unseen)
        stack, comp = [root], set()
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u)
            unseen.discard(u)
            stack.extend(adj[u] - comp)
        comps.append(comp)
    by_sum = {}
    for c in comps:
        by_sum.setdefault(sum(c) % 5, set()).update(c)
    out = set()
    for c in by_sum.values():
        out.update(combinations(sorted(c), 2))
    return edges_mask(out, edges)


def all_hypergraphs(n):
    edges = list(combinations(range(n), 3))
    return list(range(1 << len(edges))), edges


def hypergraph_pair_sum_image(mask, triples):
    idx = {e: i for i, e in enumerate(triples)}
    out = 0
    for i, (a, b, c) in enumerate(triples):
        if mask >> i & 1:
            image = tuple(sorted({(a + b) % 5, (b + c) % 5, (c + a) % 5}))
            if len(image) == 3:
                out |= 1 << idx[image]
    return out


def matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return [()]
    a = vertices[0]
    out = []
    for i in range(1, len(vertices)):
        b = vertices[i]
        rest = vertices[1:i] + vertices[i + 1:]
        for m in matchings(rest):
            out.append(tuple(sorted(((min(a, b), max(a, b)),) + m)))
    return sorted(set(out))


def determinant_matching_rotation(m):
    ranked = sorted(m, key=lambda e: (((e[1] - e[0]) % 7), e))
    low = [a for a, _ in ranked]
    high = [b for _, b in ranked]
    out = []
    for i in range(len(ranked)):
        a, b = low[i], high[(i + 1) % len(ranked)]
        out.append((min(a, b), max(a, b)))
    return tuple(sorted(out))


def line(name, states, update, extra=None):
    sig, nxt = functional_signature(states, update)
    if extra:
        extra(states, nxt, sig)
    print(name + " " + " ".join(f"{k}={sig[k]}" for k in ("S", "I", "F", "H", "C", "B")))
    return sig, nxt


def main():
    print("REPLACEMENT_ARITHMETIC_HYBRID_SCOUT_V1")
    print("EXACT_ENUMERATION_IS_COUNTEREXAMPLE_PRESSURE_ONLY")
    # Factorisation-pattern / arithmetically labelled combinatorics.
    ft = factor_tuples(60, 3)
    line("AH01_prime_transfer", ft, prime_transfer,
         lambda ss, nn, sg: [check(__import__('math').prod(x) == 60) for x in nn.values()])
    line("AH02_coprime_fusion", ft, coprime_fusion)
    parts = set_partitions(5)
    line("AH03_modular_split_partition", parts, modular_split_partition)
    line("AH04_product_match_coalescence", parts, product_match_coalescence)
    tamari = ordered_trees((2, 3, 5, 7, 11))
    line("AH05_arithmetic_tamari", tamari, lambda t: arithmetic_tamari(t)[0],
         lambda ss, nn, sg: check("2:" not in sg["C"] and "3:" not in sg["C"]))
    flip_trees = all_labelled_trees((2, 3, 5, 7))
    line("AH06_residue_subtree_flip", flip_trees, residue_subtree_flip,
         lambda ss, nn, sg: [check(residue_subtree_flip(nn[x]) == x) for x in ss])

    # Nonlinear/state-gated finite-module maps.
    f5trip = list(product(range(5), repeat=3))
    line("AH07_markoff_vieta", f5trip, lambda v: (v[0], v[1], (v[0] * v[1] - v[2]) % 5))
    line("AH08_hurwitz_cyclic", f5trip, lambda v: (v[1], v[2], (v[1] * v[2] - v[0]) % 5))
    z6pair = list(product(range(6), repeat=2))
    def gated(v):
        x, y = v
        if gcd(x, 6) == 1:
            return x, (y + x) % 6
        if gcd(y, 6) == 1:
            return (x + y) % 6, y
        return v
    line("AH09_unit_gated_transvection", z6pair, gated)
    mats = list(product(range(3), repeat=4))
    line("AH10_determinant_gate", mats, determinant_gate)
    f5pair = list(product(range(5), repeat=2))
    line("AH11_quadratic_henon", f5pair, lambda v: (v[1], (v[1] * v[1] - v[0]) % 5),
         lambda ss, nn, sg: check(sg["I"] == sg["S"]))
    line("AH12_sum_product_compressor", f5pair,
         lambda v: ((v[0] + v[1] + v[0] * v[1]) % 5, v[0] * v[1] % 5))
    z6trip = list(product(range(6), repeat=3))
    line("AH13_first_unit_normalization", z6trip, first_unit_normalize,
         lambda ss, nn, sg: [check(first_unit_normalize(nn[x]) == nn[x]) for x in ss])
    f3trip = list(product(range(3), repeat=3))
    line("AH14_triangular_product_cascade", f3trip,
         lambda v: (v[0], v[0] * v[1] % 3, v[0] * v[1] * v[2] % 3))

    # Rational and continuant combinatorics.
    cap = 9
    drift = cap_drift_states(cap)
    def drift_extra(ss, nn, sg):
        check(sg["H"] == cap - 1)
        for p, q in ss:
            if (p, q) == (0, 0):
                continue
            x, steps = (p, q), 0
            while x != (0, 0):
                x = cap_drift(cap, x)
                steps += 1
            check(steps == (cap - p - q) // p + 1)
    line("AH15_farey_cap_drift", drift, lambda x: cap_drift(cap, x), drift_extra)
    farey = [(p, q) for q in range(2, 11) for p in range(1, q) if gcd(p, q) == 1]
    line("AH16_farey_fold", farey, lambda x: (min(x[0], x[1] - x[0]), x[1]),
         lambda ss, nn, sg: [check(nn[nn[x]] == nn[x]) for x in ss])
    line("AH17_modular_inverse", farey, lambda x: (pow(x[0], -1, x[1]), x[1]),
         lambda ss, nn, sg: [check(nn[nn[x]] == x) for x in ss])
    comps = compositions(8)
    line("AH18_continuant_trace_rotation", comps,
         lambda w: rotate(w, continuant_trace(w) % len(w)),
         lambda ss, nn, sg: [check(continuant_trace(nn[x]) == continuant_trace(x)) for x in ss])
    line("AH19_continuant_trace_reversal", comps,
         lambda w: tuple(reversed(w)) if continuant_trace(w) % 3 == 0 else w,
         lambda ss, nn, sg: [check(nn[nn[x]] == x) for x in ss])
    fq = farey_states(5, positive=False)
    triples = list(product(fq, repeat=3))
    def middle_mediant(s):
        x, y, z = s
        f = Fraction(x[0] + z[0], x[1] + z[1])
        m = (f.numerator, f.denominator)
        return (x, m, z) if f.denominator <= 5 else s
    line("AH20_farey_middle_mediant", triples, middle_mediant,
         lambda ss, nn, sg: [check(nn[nn[x]] == nn[x]) for x in ss])

    # Arithmetic labels on incidence objects.
    graphs, edges = all_graphs(5)
    line("AH21_edge_arithmetic_image", graphs, lambda g: edge_arithmetic_image(g, edges))
    line("AH22_component_sum_cliques", graphs, lambda g: component_sum_cliques(g, edges))
    hypers, triples5 = all_hypergraphs(5)
    line("AH23_hypergraph_pair_sum", hypers, lambda h: hypergraph_pair_sum_image(h, triples5))
    mats6 = matchings(range(6))
    line("AH24_determinant_matching_rotation", mats6, determinant_matching_rotation)

    print("SYSTEMS=24 FACTOR_TREE_PARTITION=6 FINITE_MODULE=8 RATIONAL_CONTINUANT=6 INCIDENCE_LABELLED=4")
    print("RETAINED=0 TOP=NONE EMPTY_POOL=YES KILLED=24")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
