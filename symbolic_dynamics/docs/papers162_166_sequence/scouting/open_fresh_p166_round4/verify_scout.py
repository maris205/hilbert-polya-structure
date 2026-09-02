#!/usr/bin/env python3
"""Independent exact probes for the P166 Round-4 open scout.

The six literal maps here use six carrier types.  The program deliberately
checks small boxes only; it is evidence for theorem triage, not a novelty
claim.  It has no dependency on any paper-local verifier.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import reduce
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, gcd


ASSERTIONS = 0


def claim(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def digest_rows(rows) -> str:
    return sha256("\n".join(map(str, rows)).encode()).hexdigest()


def functional_shapes(states, step):
    """Return (tail, period) for every state of a finite endomap."""
    memo = {}
    for start in states:
        if start in memo:
            continue
        path = []
        pos = {}
        x = start
        while x not in memo and x not in pos:
            pos[x] = len(path)
            path.append(x)
            x = step(x)
        if x in memo:
            tail, period = memo[x]
            for y in reversed(path):
                tail += 1
                memo[y] = (tail, period)
        else:
            j = pos[x]
            period = len(path) - j
            for y in path[j:]:
                memo[y] = (0, period)
            tail = 0
            for y in reversed(path[:j]):
                tail += 1
                memo[y] = (tail, period)
    return memo


# ---------------------------------------------------------------------------
# GDI: x -> x + gcd(x,m) modulo m.


def additive_height(m: int) -> int:
    if m <= 1:
        return 0
    out, d, p = 0, m, 2
    while p * p <= d:
        while d % p == 0:
            out += p - 1
            d //= p
        p += 1
    if d > 1:
        out += d - 1
    return out


def divisors(m: int):
    return [d for d in range(1, m + 1) if m % d == 0]


def gdi_probe():
    rows, transitions = [], []
    for m in range(1, 181):
        def step(x):
            return (x + gcd(x, m)) % m

        depths = {}
        for x in range(m):
            seen, y = set(), x
            while y != 0:
                claim(y not in seen, f"GDI nonzero cycle m={m}, x={x}")
                seen.add(y)
                old_d = gcd(y, m)
                z = step(y)
                new_d = gcd(z, m)
                claim(new_d % old_d == 0, f"GDI gcd divisibility m={m}, y={y}")
                y = z
            depths[x] = len(seen)
            transitions.append((m, x, step(x)))
        claim(max(depths.values()) == additive_height(m), f"GDI height m={m}")
        claim(depths[1 % m] == additive_height(m), f"GDI sharp witness m={m}")
        claim([x for x in range(m) if step(x) == x] == [0], f"GDI fixed m={m}")

        actual = defaultdict(set)
        for x in range(m):
            actual[step(x)].add(x)
        for y in range(m):
            predicted = set()
            for d in divisors(m):
                if y % d == 0 and gcd(y // d - 1, m // d) == 1:
                    predicted.add((y - d) % m)
            claim(actual[y] == predicted, f"GDI fibre m={m}, y={y}")
        if m <= 20 or m in (30, 60, 90, 120, 150, 180):
            rows.append((m, additive_height(m), len(set(depths.values())),
                         max(map(len, actual.values())), len(actual[0])))
    return rows, digest_rows(transitions)


# ---------------------------------------------------------------------------
# CSP: pi -> pi^{|C_{S_n}(pi)|}.


def cycle_type(p):
    n, seen, lengths = len(p), set(), []
    for i in range(n):
        if i not in seen:
            x, ell = i, 0
            while x not in seen:
                seen.add(x)
                ell += 1
                x = p[x]
            lengths.append(ell)
    return tuple(sorted(lengths))


def centralizer_size(tp):
    mult = Counter(tp)
    z = 1
    for ell, count in mult.items():
        z *= (ell ** count) * factorial(count)
    return z


def perm_power(p, exponent):
    n, out, seen = len(p), list(range(len(p))), set()
    for i in range(n):
        if i in seen:
            continue
        cyc, x = [], i
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = p[x]
        ell = len(cyc)
        for j, v in enumerate(cyc):
            out[v] = cyc[(j + exponent) % ell]
    return tuple(out)


def powered_type(tp, exponent):
    out = []
    for ell in tp:
        g = gcd(ell, exponent)
        out.extend([ell // g] * g)
    return tuple(sorted(out))


def csp_probe():
    rows, transitions = [], []
    for n in range(1, 9):
        states = list(permutations(range(n)))
        state_set = set(states)

        def step(p):
            return perm_power(p, centralizer_size(cycle_type(p)))

        for p in states:
            q = step(p)
            claim(q in state_set, f"CSP closure n={n}")
            claim(cycle_type(q) == powered_type(cycle_type(p), centralizer_size(cycle_type(p))),
                  f"CSP powered type n={n}")
            transitions.append((n, p, q))
        shapes = functional_shapes(states, step)
        fibres = Counter(step(p) for p in states)
        rows.append((n, len(states), len(fibres),
                     tuple(sorted(Counter(shapes.values()).items())),
                     tuple(sorted(Counter(fibres.values()).items()))))
    return rows, digest_rows(transitions)


# ---------------------------------------------------------------------------
# POC: A -> A + r(A)c(A)^T over F_2.


def matrix_margins(a, m, n):
    rows = [0] * m
    cols = [0] * n
    for i in range(m):
        for j in range(n):
            bit = (a >> (i * n + j)) & 1
            rows[i] ^= bit
            cols[j] ^= bit
    return tuple(rows), tuple(cols)


def poc_step(a, m, n):
    r, c = matrix_margins(a, m, n)
    outer = 0
    for i in range(m):
        for j in range(n):
            if r[i] and c[j]:
                outer ^= 1 << (i * n + j)
    return a ^ outer


def poc_probe():
    boxes = [(1, 1), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (4, 4)]
    rows, transitions = [], []
    for m, n in boxes:
        states = list(range(1 << (m * n)))
        image1 = Counter(poc_step(a, m, n) for a in states)
        even_count = 1 << (m * n - 1)
        fixed_formula = ((1 << (m * (n - 1))) + (1 << ((m - 1) * n))
                         - (1 << ((m - 1) * (n - 1))))
        balanced_count = 1 << ((m - 1) * (n - 1))
        big_fibre = 1 + (1 << (m + n - 2))
        fixed = 0
        for a in states:
            b = poc_step(a, m, n)
            transitions.append((m, n, a, b))
            r, c = matrix_margins(a, m, n)
            rb, cb = matrix_margins(b, m, n)
            total = sum(r) & 1
            claim((sum(rb) & 1) == 0, f"POC even image {m}x{n}")
            if total:
                claim(not any(rb) and not any(cb), f"POC odd collapse {m}x{n}")
            else:
                claim(rb == r and cb == c, f"POC recurrent margins {m}x{n}")
                claim(poc_step(b, m, n) == a, f"POC involution {m}x{n}")
            fixed += (b == a)
        claim(len(image1) == even_count, f"POC image size {m}x{n}")
        claim(fixed == fixed_formula, f"POC fixed count {m}x{n}")

        for t in range(1, 5):
            counts = Counter()
            for a in states:
                b = a
                for _ in range(t):
                    b = poc_step(b, m, n)
                counts[b] += 1
            for b in states:
                r, c = matrix_margins(b, m, n)
                if sum(r) & 1:
                    expected = 0
                elif not any(r) and not any(c):
                    expected = big_fibre
                else:
                    expected = 1
                claim(counts[b] == expected, f"POC t-fibre {m}x{n}, t={t}, b={b}")
        claim(sum(1 for b in states if matrix_margins(b, m, n) == ((0,) * m, (0,) * n))
              == balanced_count, f"POC balanced count {m}x{n}")
        # The carrier and largest positive fibre recover mn and m+n.
        recovered_sum = (big_fibre - 1).bit_length() + 1
        claim(recovered_sum == m + n, f"POC parameter sum {m}x{n}")
        roots = sorted(k for k in range(1, recovered_sum) if k * (recovered_sum - k) == m * n)
        claim(roots == sorted(set((m, n))), f"POC unordered parameter recovery {m}x{n}")
        rows.append(((m, n), len(states), len(image1), fixed, balanced_count, big_fibre,
                     tuple(sorted(Counter(image1.values()).items()))))
    return rows, digest_rows(transitions)


# ---------------------------------------------------------------------------
# CTC: the self-commutator A A^T - A^T A on 2-by-2 matrices.


class TinyField:
    """The prime fields used below and the genuine field F_4."""

    def __init__(self, q):
        claim(q in (2, 3, 4, 5, 7), f"CTC supported exact field q={q}")
        self.q = q
        self.char = 2 if q in (2, 4) else q

    def add(self, x, y):
        return x ^ y if self.q == 4 else (x + y) % self.q

    def neg(self, x):
        return x if self.q == 4 else (-x) % self.q

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        if self.q != 4:
            return (x * y) % self.q
        raw = 0
        for i in range(2):
            if (y >> i) & 1:
                raw ^= x << i
        # alpha^2 = alpha + 1 for the modulus alpha^2+alpha+1.
        if raw & 4:
            raw ^= 0b111
        return raw

    def sq(self, x):
        return self.mul(x, x)


def ctc_step(a, field):
    x00, x01, x10, x11 = a
    f = field
    diag = f.sub(f.sq(x01), f.sq(x10))
    off = f.sub(f.add(f.mul(x00, x10), f.mul(x01, x11)),
                f.add(f.mul(x00, x01), f.mul(x10, x11)))
    return (diag, off, off, f.neg(diag))


def ctc_rank(b, field):
    if all(x == 0 for x in b):
        return 0
    det = field.sub(field.mul(b[0], b[3]), field.mul(b[1], b[2]))
    return 1 if det == 0 else 2


def ctc_probe():
    rows, transitions = [], []
    for q in (2, 3, 4, 5, 7):
        f = TinyField(q)
        states = list(product(range(q), repeat=4))
        fibres = Counter()
        for a in states:
            b = ctc_step(a, f)
            fibres[b] += 1
            transitions.append((q, a, b))
            claim(ctc_step(b, f) == (0, 0, 0, 0), f"CTC square-zero q={q}")
        image = set(fibres)
        zero_fibre = fibres[(0, 0, 0, 0)]
        nonzero_fibres = {fibres[b] for b in image if b != (0, 0, 0, 0)}
        if f.char != 2:
            predicted_image = {(x, y, y, f.neg(x)) for x in range(q) for y in range(q)}
            claim(image == predicted_image, f"CTC odd image q={q}")
            claim(zero_fibre == q ** 3 + q * (q - 1), f"CTC odd zero fibre q={q}")
            claim(nonzero_fibres == {q * (q - 1)}, f"CTC odd nonzero fibres q={q}")
        else:
            predicted_image = {(0, 0, 0, 0)}
            predicted_image |= {(x, y, y, x) for x in range(1, q) for y in range(q)}
            claim(image == predicted_image, f"CTC char2 image q={q}")
            claim(zero_fibre == q ** 3, f"CTC char2 zero fibre q={q}")
            claim(nonzero_fibres == {q ** 2}, f"CTC char2 nonzero fibres q={q}")
        shapes = functional_shapes(states, lambda a: ctc_step(a, f))
        expected_depth = Counter({0: 1, 1: zero_fibre - 1,
                                  2: q ** 4 - zero_fibre})
        claim(Counter(t for t, _ in shapes.values()) == expected_depth, f"CTC depth census q={q}")
        claim(set(period for _, period in shapes.values()) == {1}, f"CTC periods q={q}")
        rank_counts = Counter(ctc_rank(b, f) for b in image)
        if f.char != 2:
            roots_minus_one = sum(1 for z in range(q) if f.sq(z) == f.neg(1))
            predicted_rank1 = roots_minus_one * (q - 1)
            claim(rank_counts[1] == predicted_rank1, f"CTC odd rank-one spectrum q={q}")
            claim(rank_counts[2] == q * q - 1 - predicted_rank1,
                  f"CTC odd rank-two spectrum q={q}")
        else:
            claim(rank_counts == Counter({2: (q - 1) ** 2, 1: q - 1, 0: 1}),
                  f"CTC char2 rank spectrum q={q}")
        rows.append((q, len(states), len(image), zero_fibre,
                     tuple(sorted(nonzero_fibres)),
                     tuple(sorted(expected_depth.items())),
                     tuple(sorted(rank_counts.items()))))
    return rows, digest_rows(transitions)


# ---------------------------------------------------------------------------
# DPS: Seidel-switch a graph by its current odd-degree vertex set.


def graph_edges(n):
    return list(combinations(range(n), 2))


def odd_vertices(mask, n, edges):
    parity = [0] * n
    for k, (u, v) in enumerate(edges):
        if (mask >> k) & 1:
            parity[u] ^= 1
            parity[v] ^= 1
    return tuple(i for i, bit in enumerate(parity) if bit)


def switch_cut(mask, subset, n, edges):
    s = set(subset)
    out = mask
    for k, (u, v) in enumerate(edges):
        if (u in s) != (v in s):
            out ^= 1 << k
    return out


def dps_probe():
    rows, transitions = [], []
    for n in range(1, 7):
        edges = graph_edges(n)
        states = list(range(1 << len(edges)))

        def step(g):
            return switch_cut(g, odd_vertices(g, n, edges), n, edges)

        fixed = 0
        for g in states:
            h = step(g)
            transitions.append((n, g, h))
            fixed += (g == h)
            if n % 2:
                claim(not odd_vertices(h, n, edges), f"DPS odd-n Eulerian image n={n}")
                claim(step(h) == h, f"DPS odd-n idempotence n={n}")
            else:
                claim(odd_vertices(h, n, edges) == odd_vertices(g, n, edges),
                      f"DPS even-n invariant odd set n={n}")
                claim(step(h) == g, f"DPS even-n involution n={n}")
        shapes = functional_shapes(states, step)
        if n % 2:
            expected_fixed = 1 << (len(edges) - n + 1) if n > 1 else 1
            expected_fibre = 1 << (n - 1)
            for t in (1, 2, 3):
                counts = Counter()
                for g in states:
                    h = g
                    for _ in range(t):
                        h = step(h)
                    counts[h] += 1
                for h in states:
                    expected = expected_fibre if not odd_vertices(h, n, edges) else 0
                    claim(counts[h] == expected, f"DPS odd-n fibre n={n}, t={t}")
        else:
            expected_fixed = 2 * (1 << (len(edges) - n + 1))
            claim(len(set(step(g) for g in states)) == len(states), f"DPS bijective n={n}")
            claim(all(v == 1 for v in Counter(step(g) for g in states).values()),
                  f"DPS unit fibres n={n}")
        claim(fixed == expected_fixed, f"DPS fixed count n={n}")
        rows.append((n, len(states), fixed, tuple(sorted(Counter(shapes.values()).items()))))
    return rows, digest_rows(transitions)


# ---------------------------------------------------------------------------
# HOP: H -> all triangles of the pair-parity boundary graph of H.


def hop_data(n):
    edges = list(combinations(range(n), 2))
    triples = list(combinations(range(n), 3))
    edge_at = {e: i for i, e in enumerate(edges)}
    triangle_edges = []
    for a, b, c in triples:
        triangle_edges.append((1 << edge_at[(a, b)]) |
                              (1 << edge_at[(a, c)]) |
                              (1 << edge_at[(b, c)]))
    basis = []
    for i, j in combinations(range(1, n), 2):
        basis.append((1 << edge_at[(0, i)]) |
                     (1 << edge_at[(0, j)]) |
                     (1 << edge_at[(i, j)]))
    return edges, triples, triangle_edges, basis


def boundary(h, triangle_edges):
    g = 0
    for k, e_mask in enumerate(triangle_edges):
        if (h >> k) & 1:
            g ^= e_mask
    return g


def triangles_of(g, triangle_edges):
    h = 0
    for k, e_mask in enumerate(triangle_edges):
        if g & e_mask == e_mask:
            h |= 1 << k
    return h


def hop_probe():
    rows, transitions = [], []
    for n in range(3, 8):
        edges, triples, triangle_edges, basis = hop_data(n)
        eulerian = []
        for coeff in range(1 << len(basis)):
            g = 0
            for k, b in enumerate(basis):
                if (coeff >> k) & 1:
                    g ^= b
            eulerian.append(g)
        claim(len(set(eulerian)) == 1 << comb(n - 1, 2), f"HOP cycle-space basis n={n}")
        eulerian_set = set(eulerian)

        def quotient_step(g):
            return boundary(triangles_of(g, triangle_edges), triangle_edges)

        triangle_targets = Counter()
        for g in eulerian:
            h = triangles_of(g, triangle_edges)
            q = quotient_step(g)
            claim(q in eulerian_set, f"HOP quotient closure n={n}")
            triangle_targets[h] += 1
            transitions.append((n, g, h, q))
        shapes = functional_shapes(eulerian, quotient_step)
        claim(all(period == 1 for _, period in shapes.values()), f"HOP small-box cycles n={n}")

        kernel_size = 1 << comb(n - 1, 3)
        if n <= 5:
            actual = Counter()
            boundary_fibres = Counter()
            for h in range(1 << len(triples)):
                g = boundary(h, triangle_edges)
                boundary_fibres[g] += 1
                actual[triangles_of(g, triangle_edges)] += 1
            claim(set(boundary_fibres) == eulerian_set, f"HOP boundary image n={n}")
            claim(set(boundary_fibres.values()) == {kernel_size}, f"HOP uniform kernel n={n}")
            predicted = Counter({h: kernel_size * mult for h, mult in triangle_targets.items()})
            claim(actual == predicted, f"HOP first-target fibres n={n}")
        rows.append((n, len(eulerian), len(triangle_targets),
                     len(set(quotient_step(g) for g in eulerian)),
                     sum(quotient_step(g) == g for g in eulerian),
                     max(tail for tail, _ in shapes.values()),
                     tuple(sorted(Counter(shapes.values()).items())),
                     tuple(sorted(Counter(triangle_targets.values()).items()))))
    return rows, digest_rows(transitions)


# ---------------------------------------------------------------------------
# CTR: move a marked vertex toward the center of its fixed labelled tree.


def prufer_tree(seq, n):
    if n == 1:
        return tuple()
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = min(i for i in range(n) if degree[i] == 1)
        edges.append(tuple(sorted((leaf, x))))
        degree[leaf] -= 1
        degree[x] -= 1
    last = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(sorted(last)))
    return tuple(sorted(edges))


def tree_geometry(edges, n):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    dist = []
    for s in range(n):
        ds = [-1] * n
        ds[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if ds[v] < 0:
                    ds[v] = ds[u] + 1
                    q.append(v)
        dist.append(ds)
    ecc = [max(row) for row in dist]
    radius = min(ecc)
    centers = tuple(i for i, e in enumerate(ecc) if e == radius)
    claim(len(centers) in (1, 2), f"CTR center cardinality n={n}")
    if len(centers) == 2:
        claim(centers[1] in adj[centers[0]], f"CTR adjacent bicenter n={n}")
    depth = [min(dist[x][c] for c in centers) for x in range(n)]
    base = [min(centers, key=lambda c: dist[x][c]) for x in range(n)]
    parent = list(range(n))
    for x in range(n):
        if depth[x] > 0:
            choices = [v for v in adj[x] if min(dist[v][c] for c in centers) == depth[x] - 1]
            claim(len(choices) == 1, f"CTR unique inward edge n={n}, x={x}")
            parent[x] = choices[0]
        elif len(centers) == 2:
            parent[x] = centers[1] if x == centers[0] else centers[0]
    return adj, dist, centers, tuple(depth), tuple(base), tuple(parent)


def ctr_probe():
    rows, transitions = [], []
    for n in range(1, 8):
        seqs = [()] if n <= 2 else product(range(n), repeat=n - 2)
        tree_count = one_center = two_center = state_count = 0
        global_depth = 0
        fibre_max = 0
        seen_trees = set()
        for seq in seqs:
            edges = prufer_tree(seq, n)
            claim(edges not in seen_trees, f"CTR Prüfer injectivity n={n}")
            seen_trees.add(edges)
            tree_count += 1
            adj, dist, centers, depth, base, parent = tree_geometry(edges, n)
            one_center += len(centers) == 1
            two_center += len(centers) == 2
            state_count += n
            global_depth = max(global_depth, max(depth))

            def step(x):
                return parent[x]

            shapes = functional_shapes(range(n), step)
            for x in range(n):
                expected_period = 1 if len(centers) == 1 else 2
                claim(shapes[x] == (depth[x], expected_period), f"CTR point shape n={n}, x={x}")
                transitions.append((n, edges, x, step(x)))

            for t in range(0, n + 2):
                actual = defaultdict(set)
                for x in range(n):
                    y = x
                    for _ in range(t):
                        y = step(y)
                    actual[y].add(x)
                for y in range(n):
                    predicted = set()
                    if y not in centers:
                        for x in range(n):
                            if depth[x] == depth[y] + t:
                                z = x
                                for _ in range(t):
                                    z = parent[z]
                                if z == y:
                                    predicted.add(x)
                    elif len(centers) == 1:
                        predicted = {x for x in range(n) if depth[x] <= t}
                    else:
                        other = {centers[0]: centers[1], centers[1]: centers[0]}
                        for x in range(n):
                            if depth[x] <= t:
                                arrival = base[x]
                                if (t - depth[x]) & 1:
                                    arrival = other[arrival]
                                if arrival == y:
                                    predicted.add(x)
                    claim(actual[y] == predicted, f"CTR target fibre n={n}, t={t}, y={y}")
                    fibre_max = max(fibre_max, len(actual[y]))
        claim(tree_count == (1 if n == 1 else n ** (n - 2)), f"CTR Cayley count n={n}")
        claim(global_depth == (n - 1) // 2, f"CTR sharp global depth n={n}")
        rows.append((n, tree_count, state_count, one_center, two_center,
                     global_depth, fibre_max))
    return rows, digest_rows(transitions)


def main():
    print("P166 ROUND4 OPEN SCOUT — EXACT SMALL-BOX TRANSCRIPT")
    print("scope=7 literal maps / 7 carrier classes / HOLD_EXTERNAL")

    gdi_rows, gdi_hash = gdi_probe()
    print("\n[GDI] residue gcd-increment")
    for row in gdi_rows:
        print(row)
    print("transition_sha256=" + gdi_hash)

    csp_rows, csp_hash = csp_probe()
    print("\n[CSP] centralizer-size power on permutations")
    for row in csp_rows:
        print(row)
    print("transition_sha256=" + csp_hash)

    poc_rows, poc_hash = poc_probe()
    print("\n[POC] parity outer-product matrix feedback")
    for row in poc_rows:
        print(row)
    print("transition_sha256=" + poc_hash)

    ctc_rows, ctc_hash = ctc_probe()
    print("\n[CTC] 2-by-2 transpose self-commutator")
    for row in ctc_rows:
        print(row)
    print("transition_sha256=" + ctc_hash)

    dps_rows, dps_hash = dps_probe()
    print("\n[DPS] odd-set Seidel feedback")
    for row in dps_rows:
        print(row)
    print("transition_sha256=" + dps_hash)

    hop_rows, hop_hash = hop_probe()
    print("\n[HOP] hypergraph boundary-to-triangle operator")
    for row in hop_rows:
        print(row)
    print("transition_sha256=" + hop_hash)

    ctr_rows, ctr_hash = ctr_probe()
    print("\n[CTR] marked-root transport to tree center")
    for row in ctr_rows:
        print(row)
    print("transition_sha256=" + ctr_hash)

    print("\nDECISIONS")
    print("GDI=KILL_DIRECT_PUBLIC_LITERAL_OWNER")
    print("CSP=KILL_NO_ALL_PARAMETER_SPINE_PLUS_POWER_MAP_CROWDING")
    print("POC=KILL_INTERNAL_P127_PROOF_SILHOUETTE")
    print("CTC=KILL_CLASSICAL_SELF_COMMUTATOR_PLUS_SHALLOW_QUADRATIC_MATRIX_SILHOUETTE")
    print("DPS=KILL_CLASSICAL_SWITCHING_PLUS_INTERNAL_P127")
    print("HOP=KILL_NO_CLOSED_TEMPORAL_OR_TARGET_ATLAS")
    print("CTR=KILL_THIN_MARKER_NAVIGATION_ON_STATIC_TREE")
    print("ROUND4=KILL_ALL")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
