#!/usr/bin/env python3
"""Deterministic Stage-1 pressure tests for the P152--P156 combinatorial lane.

Enumeration is used only to falsify proposed statements in finite boxes.  The
script deliberately builds every literal map independently of the formulas it
checks.  No output of this program is a proof or an ownership statement.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: str = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()


@lru_cache(None)
def perms(n: int):
    return tuple(permutations(range(1, n + 1)))


def standardize(values):
    values = tuple(values)
    rank = {v: i + 1 for i, v in enumerate(sorted(values))}
    return tuple(rank[v] for v in values)


def identity(n: int):
    return tuple(range(1, n + 1))


# ---------------------------------------------------------------------------
# C01 / WEX: weak-excedance extraction


def wex(p):
    return standardize(v for i, v in enumerate(p, 1) if v >= i)


def maxdrop(p):
    return max((i - v for i, v in enumerate(p, 1)), default=0)


@lru_cache(None)
def wex_tail(p):
    if p == identity(len(p)):
        return 0
    return 1 + wex_tail(wex(p))


def fib(k: int):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def wex_section(sigma, n: int):
    m = len(sigma)
    h = n - m
    return tuple(v + h for v in sigma) + tuple(range(1, h + 1))


def deficient_completion_count(B, Q):
    """Bijections B->Q with assigned value b at q satisfying b<q."""
    total = 1
    for j, q in enumerate(Q, 1):
        total *= sum(b < q for b in B) - (j - 1)
        if total <= 0:
            return 0
    return total


def wex_fibre_formula(sigma, n: int):
    m = len(sigma)
    if m > n:
        return 0
    universe = tuple(range(1, n + 1))
    total = 0
    for Avals in combinations(universe, m):
        Aset = set(Avals)
        B = tuple(v for v in universe if v not in Aset)
        for Ppos in combinations(universe, m):
            if any(Ppos[i] > Avals[sigma[i] - 1] for i in range(m)):
                continue
            Pset = set(Ppos)
            Q = tuple(q for q in universe if q not in Pset)
            total += deficient_completion_count(B, Q)
    return total


def audit_wex():
    maxima = []
    tail_census = []
    image_counts = []
    fixed_counts = []
    literal_fibres = {}
    literal_images = {}

    # The literal functional graph and the proposed pointwise Fibonacci bounds.
    for n in range(1, 10):
        A.box()
        fibres = Counter()
        census = Counter()
        fixed = 0
        for p in perms(n):
            q = wex(p)
            A.check(1 <= len(q) <= n, f"WEX closure n={n}, p={p}")
            A.check(sorted(q) == list(range(1, len(q) + 1)))
            t = wex_tail(p)
            census[t] += 1
            fibres[q] += 1
            if q == p:
                fixed += 1
                A.check(p == identity(n), f"nonidentity WEX fixed point {p}")
            A.check(maxdrop(q) <= maxdrop(p), f"drop increased at {p}")
            if t:
                # Finite-box pressure on the all-rank certificate theorem.
                A.check(n >= fib(t + 2), f"size Fibonacci bound fails at {p}")
                A.check(maxdrop(p) >= fib(t + 1), f"drop Fibonacci bound fails at {p}")
        maxima.append(max(census))
        tail_census.append(dict(sorted(census.items())))
        image_counts.append(len(fibres))
        literal_images[n] = set(fibres)
        fixed_counts.append(fixed)
        if n <= 7:
            literal_fibres[n] = fibres

    A.check(maxima == [0, 1, 2, 2, 3, 3, 3, 4, 4])
    A.check(fixed_counts == [1] * 9)

    # Exact falsifier for the proof-gate compression lemma:
    # tail(W(p)) is no larger than the worst tail at rank maxdrop(p).
    for n in range(1, 10):
        for p in perms(n):
            D = maxdrop(p)
            rank_D_max = 0 if D == 0 else maxima[D - 1]
            A.check(wex_tail(wex(p)) <= rank_D_max, ("compression", p, D))

    # Exact one-step image theorem and its explicit high-shift/low-tail section.
    for m in range(1, 9):
        for sigma in perms(m):
            d = maxdrop(sigma)
            for n in range(m, 10):
                predicted = m + d <= n
                observed = sigma in literal_images[n]
                A.check(observed == predicted, (m, n, sigma, d))
            source = wex_section(sigma, m + d)
            A.check(wex(source) == sigma, f"section fails for {sigma}")
            A.check(maxdrop(source) == m if d else maxdrop(source) == 0)

    # Every-target Ferrers-board fibre formula, including zero fibres.
    fibre_checks = 0
    for n in range(1, 8):
        for m in range(1, n + 1):
            for sigma in perms(m):
                formula = wex_fibre_formula(sigma, n)
                literal = literal_fibres[n].get(sigma, 0)
                A.check(formula == literal, ("WEX fibre", n, sigma, formula, literal))
                fibre_checks += 1

    # Canonical sharp witnesses L(w_t).
    # The first lift of the identity must be chosen separately; thereafter L.
    witnesses = [(1,), (2, 1)]
    while len(witnesses) < 6:
        old = witnesses[-1]
        witnesses.append(wex_section(old, len(old) + maxdrop(old)))
    A.check([len(w) for w in witnesses] == [1, 2, 3, 5, 8, 13])
    A.check([maxdrop(w) for w in witnesses] == [0, 1, 2, 3, 5, 8])
    A.check([wex_tail(w) for w in witnesses] == [0, 1, 2, 3, 4, 5])

    return {
        "max_tail": maxima,
        "tail_census": tail_census,
        "image_counts": image_counts,
        "fibre_checks": fibre_checks,
        "witnesses": witnesses,
    }


# ---------------------------------------------------------------------------
# C02 / UHC: strict upper-hull extraction and rank compression


def upper_hull_extract(p):
    stack = []
    for x, y in enumerate(p, 1):
        while len(stack) >= 2:
            x1, y1 = stack[-2]
            x2, y2 = stack[-1]
            cross = (x2 - x1) * (y - y2) - (y2 - y1) * (x - x2)
            if cross >= 0:  # delete collinear middle points as well
                stack.pop()
            else:
                break
        stack.append((x, y))
    return standardize(y for _, y in stack)


@lru_cache(None)
def uhc_tail(p):
    q = upper_hull_extract(p)
    if q == p:
        return 0
    return 1 + uhc_tail(q)


def unimodal(p):
    if not p:
        return True
    peak = p.index(max(p))
    return all(p[i] < p[i + 1] for i in range(peak)) and all(
        p[i] > p[i + 1] for i in range(peak, len(p) - 1)
    )


def audit_uhc():
    maxima, images, fixed_counts, max_fibres = [], [], [], []
    fixed_lists = []
    for n in range(1, 10):
        A.box()
        fibres = Counter()
        fixed = []
        max_tail = 0
        for p in perms(n):
            q = upper_hull_extract(p)
            A.check(1 <= len(q) <= n)
            A.check(unimodal(q), ("non-unimodal hull image", p, q))
            fibres[q] += 1
            t = uhc_tail(p)
            max_tail = max(max_tail, t)
            if q == p:
                fixed.append(p)
            # A strict rank drop forbids a nontrivial cycle.
            if q != p:
                A.check(len(q) < len(p), ("same-rank UHC move", p, q))
        maxima.append(max_tail)
        images.append(len(fibres))
        fixed_counts.append(len(fixed))
        fixed_lists.append(tuple(fixed))
        max_fibres.append(max(fibres.values()))
    A.check(maxima == [0, 0, 1, 2, 2, 3, 3, 4, 4])
    A.check(images == [1, 2, 4, 8, 14, 22, 30, 50, 84])
    A.check(fixed_counts == [1, 2, 2, 2, 0, 0, 0, 0, 0])
    A.check(fixed_lists[2] == ((1, 3, 2), (2, 3, 1)))
    A.check(fixed_lists[3] == ((1, 3, 4, 2), (2, 4, 3, 1)))
    return {
        "max_tail": maxima,
        "image_counts": images,
        "fixed_counts": fixed_counts,
        "max_fibres": max_fibres,
    }


# ---------------------------------------------------------------------------
# Breadth controls C03--C14.  These are intentionally small owner-first boxes.


def edge(a, b):
    return tuple(sorted((a, b)))


def boundary_edge(a, b, n):
    return (a - b) % n in (1, n - 1)


@lru_cache(None)
def interval_triangulations(i, j):
    if j - i < 2:
        return (frozenset(),)
    ans = set()
    for k in range(i + 1, j):
        for left in interval_triangulations(i, k):
            for right in interval_triangulations(k, j):
                ds = set(left) | set(right)
                if k - i > 1:
                    ds.add(edge(i, k))
                if j - k > 1:
                    ds.add(edge(k, j))
                ans.add(frozenset(ds))
    return tuple(sorted(ans, key=lambda z: tuple(sorted(z))))


def triangulations(n):
    return interval_triangulations(0, n - 1)


def has_edge(T, a, b, n):
    return boundary_edge(a, b, n) or edge(a, b) in T


def frontier_fan_step(T, n):
    root_neighbors = [1] + [v for v in range(2, n - 1) if edge(0, v) in T] + [n - 1]
    candidates = []
    for a, b in zip(root_neighbors, root_neighbors[1:]):
        if b == a + 1:
            continue
        diag = edge(a, b)
        A.check(diag in T)
        thirds = [
            c
            for c in range(a + 1, b)
            if has_edge(T, a, c, n) and has_edge(T, b, c, n)
        ]
        A.check(len(thirds) == 1, (T, a, b, thirds))
        candidates.append((thirds[0], diag))
    if not candidates:
        return T
    c, diag = min(candidates)
    return frozenset((set(T) - {diag}) | {edge(0, c)})


def audit_frontier_fan():
    profiles = []
    for n in range(3, 11):
        A.box()
        depth = Counter()
        image = set()
        for T in triangulations(n):
            cur = T
            t = 0
            while True:
                nxt = frontier_fan_step(cur, n)
                if nxt == cur:
                    break
                A.check(len(nxt) == n - 3)
                cur = nxt
                t += 1
            missing = (n - 3) - sum(edge(0, v) in T for v in range(2, n - 1))
            A.check(t == missing)
            depth[t] += 1
            image.add(frontier_fan_step(T, n))
        A.check(len(triangulations(n)) == comb(2 * (n - 2), n - 2) // (n - 1))
        profiles.append((n, len(triangulations(n)), len(image), max(depth), dict(sorted(depth.items()))))
    return profiles


def dyck_words(n):
    ans = []

    def rec(prefix, up, down):
        if up == down == n:
            ans.append(prefix)
            return
        if up < n:
            rec(prefix + "U", up + 1, down)
        if down < up:
            rec(prefix + "D", up, down + 1)

    rec("", 0, 0)
    return tuple(ans)


def dyck_shell(w):
    pieces = []
    start = 0
    height = 0
    for i, ch in enumerate(w):
        height += 1 if ch == "U" else -1
        if height == 0:
            pieces.append(w[start + 1 : i])
            start = i + 1
    return "".join(pieces)


def dyck_height(w):
    h = best = 0
    for ch in w:
        h += 1 if ch == "U" else -1
        best = max(best, h)
    return best


def audit_dyck_shell():
    profile = []
    for n in range(0, 10):
        A.box()
        census = Counter()
        for w in dyck_words(n):
            cur, t = w, 0
            while cur:
                cur = dyck_shell(cur)
                t += 1
            A.check(t == dyck_height(w))
            census[t] += 1
        profile.append((n, len(dyck_words(n)), max(census), dict(sorted(census.items()))))
    return profile


def set_partitions(n):
    out = []

    def rec(i, blocks):
        if i > n:
            out.append(tuple(tuple(b) for b in blocks))
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            rec(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        rec(i + 1, blocks)
        blocks.pop()

    rec(1, [])
    return tuple(out)


def noncrossing(part):
    for x in range(len(part)):
        for y in range(x + 1, len(part)):
            Ablock, Bblock = part[x], part[y]
            for a, c in combinations(Ablock, 2):
                for b, d in combinations(Bblock, 2):
                    if a < b < c < d or b < a < d < c:
                        return False
    return True


def partition_perm(part, n):
    p = list(range(n + 1))
    for block in part:
        for a, b in zip(block, block[1:] + block[:1]):
            p[a] = b
    return tuple(p)


def perm_partition(p):
    seen = set()
    blocks = []
    for i in range(1, len(p)):
        if i in seen:
            continue
        cyc, x = [], i
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = p[x]
        blocks.append(tuple(sorted(cyc)))
    return tuple(sorted(blocks, key=lambda b: b[0]))


def kreweras(part, n):
    p = partition_perm(part, n)
    pinv = [0] * (n + 1)
    for i in range(1, n + 1):
        pinv[p[i]] = i
    q = [0] * (n + 1)
    for i in range(1, n + 1):
        c_i = i + 1 if i < n else 1
        q[i] = pinv[c_i]
    return perm_partition(tuple(q))


def audit_kreweras():
    profile = []
    for n in range(1, 8):
        A.box()
        states = tuple(p for p in set_partitions(n) if noncrossing(p))
        state_set = set(states)
        periods = Counter()
        for p in states:
            q = kreweras(p, n)
            A.check(q in state_set)
            cur, t = q, 1
            while cur != p:
                cur = kreweras(cur, n)
                t += 1
                A.check(t <= 2 * n)
            A.check((2 * n) % t == 0)
            periods[t] += 1
        A.check(len(states) == comb(2 * n, n) // (n + 1))
        profile.append((n, len(states), dict(sorted(periods.items()))))
    return profile


def rectangular_syt(rows, cols):
    N = rows * cols
    ans = []
    for t in permutations(range(1, N + 1)):
        ok = True
        for r in range(rows):
            for c in range(cols - 1):
                ok &= t[r * cols + c] < t[r * cols + c + 1]
        for r in range(rows - 1):
            for c in range(cols):
                ok &= t[r * cols + c] < t[(r + 1) * cols + c]
        if ok:
            ans.append(t)
    return tuple(ans)


def promotion(T, rows, cols):
    N = rows * cols
    tab = [list(T[r * cols : (r + 1) * cols]) for r in range(rows)]
    r = c = 0
    tab[0][0] = None
    while True:
        choices = []
        if r + 1 < rows:
            choices.append((tab[r + 1][c], r + 1, c))
        if c + 1 < cols:
            choices.append((tab[r][c + 1], r, c + 1))
        if not choices:
            break
        _, rr, cc = min(choices)
        tab[r][c] = tab[rr][cc]
        tab[rr][cc] = None
        r, c = rr, cc
    tab[r][c] = N + 1
    return tuple(tab[r][c] - 1 for r in range(rows) for c in range(cols))


def audit_promotion():
    profile = []
    for cols in range(1, 5):
        rows, N = 2, 2 * cols
        A.box()
        states = rectangular_syt(rows, cols)
        state_set = set(states)
        periods = Counter()
        for T in states:
            cur, t = promotion(T, rows, cols), 1
            A.check(cur in state_set)
            while cur != T:
                cur = promotion(cur, rows, cols)
                t += 1
                A.check(t <= N)
            A.check(N % t == 0)
            periods[t] += 1
        profile.append(((rows, cols), len(states), dict(sorted(periods.items()))))
    return profile


def plane_partitions(a, b, c):
    ans = []
    for vals in product(range(c + 1), repeat=a * b):
        ok = True
        for i in range(a):
            for j in range(b):
                if i + 1 < a:
                    ok &= vals[i * b + j] >= vals[(i + 1) * b + j]
                if j + 1 < b:
                    ok &= vals[i * b + j] >= vals[i * b + j + 1]
        if ok:
            ans.append(vals)
    return tuple(ans)


def pp_complement(P, a, b, c):
    return tuple(c - P[(a - 1 - i) * b + (b - 1 - j)] for i in range(a) for j in range(b))


def audit_plane_complement():
    profile = []
    for a, b, c in ((1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 2)):
        A.box()
        states = plane_partitions(a, b, c)
        fixed = 0
        for P in states:
            Q = pp_complement(P, a, b, c)
            A.check(Q in states)
            A.check(pp_complement(Q, a, b, c) == P)
            A.check(sum(P) + sum(Q) == a * b * c)
            fixed += Q == P
        profile.append(((a, b, c), len(states), fixed))
    return profile


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def incircle(a, b, c, d):
    # Translate d to the origin; positive for d inside a CCW circumcircle.
    ax, ay = a[0] - d[0], a[1] - d[1]
    bx, by = b[0] - d[0], b[1] - d[1]
    cx, cy = c[0] - d[0], c[1] - d[1]
    return (
        (ax * ax + ay * ay) * (bx * cy - by * cx)
        - (bx * bx + by * by) * (ax * cy - ay * cx)
        + (cx * cx + cy * cy) * (ax * by - ay * bx)
    )


def audit_delaunay_quad():
    # A generic integer convex quadrilateral; the carrier has its two triangulations.
    pts = ((0, 0), (4, 0), (5, 3), (0, 2))
    A.box()
    A.check(all(orient(pts[i], pts[(i + 1) % 4], pts[(i + 2) % 4]) > 0 for i in range(4)))
    illegal02 = incircle(pts[0], pts[1], pts[2], pts[3]) > 0
    illegal13 = incircle(pts[1], pts[2], pts[3], pts[0]) > 0
    A.check(illegal02 != illegal13)
    states = ("02", "13")
    legal = "13" if illegal02 else "02"
    step = {s: legal for s in states}
    A.check(step[legal] == legal)
    A.check(Counter(step.values()) == Counter({legal: 2}))
    return {"points": pts, "illegal": "02" if illegal02 else "13", "legal": legal, "tails": {legal: 0, (set(states) - {legal}).pop(): 1}}


def all_faces(facets):
    faces = {frozenset()}
    for F in facets:
        for r in range(1, len(F) + 1):
            faces.update(frozenset(x) for x in combinations(sorted(F), r))
    return faces


def maximal_facets(faces):
    nonempty = [f for f in faces if f]
    return tuple(sorted((f for f in nonempty if not any(f < g for g in nonempty)), key=lambda f: (len(f), tuple(f))))


def lex_collapse(facets):
    faces = all_faces(facets)
    maxes = maximal_facets(faces)
    pairs = []
    for sigma in maxes:
        if len(sigma) < 2:
            continue
        for tau in combinations(sorted(sigma), len(sigma) - 1):
            tau = frozenset(tau)
            owners = [F for F in maxes if tau <= F]
            if owners == [sigma]:
                pairs.append((tuple(sorted(tau)), tuple(sorted(sigma))))
    if not pairs:
        return tuple(tuple(sorted(f)) for f in maxes)
    tau_t, sigma_t = min(pairs)
    tau, sigma = frozenset(tau_t), frozenset(sigma_t)
    kept = {f for f in faces if not (tau <= f <= sigma)}
    return tuple(tuple(sorted(f)) for f in maximal_facets(kept))


def audit_lex_collapse():
    samples = (
        ((0, 1, 2),),
        ((0, 1, 2), (1, 2, 3)),
        ((0, 1), (1, 2), (2, 0)),
        ((0, 1, 2), (0, 2, 3)),
        ((0, 1, 2, 3),),
    )
    profile = []
    for facets in samples:
        A.box()
        cur = tuple(tuple(sorted(f)) for f in maximal_facets(all_faces(facets)))
        seen, t = set(), 0
        while cur not in seen:
            seen.add(cur)
            nxt = lex_collapse(cur)
            if nxt == cur:
                break
            A.check(len(all_faces(nxt)) < len(all_faces(cur)))
            cur, t = nxt, t + 1
        profile.append((facets, t, cur))
    return profile


def graph2core_step(state):
    n, edges = state
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    keep = [v for v in range(n) if degree[v] >= 2]
    rank = {v: i for i, v in enumerate(keep)}
    new_edges = frozenset(edge(rank[u], rank[v]) for u, v in edges if u in rank and v in rank)
    return len(keep), new_edges


def audit_graph2core():
    profile = []
    for n in range(0, 7):
        A.box()
        E = tuple(combinations(range(n), 2))
        census = Counter()
        for mask in range(1 << len(E)):
            state = (n, frozenset(E[i] for i in range(len(E)) if mask >> i & 1))
            cur, t = state, 0
            while True:
                nxt = graph2core_step(cur)
                if nxt == cur:
                    break
                A.check(nxt[0] < cur[0])
                cur, t = nxt, t + 1
            census[t] += 1
        profile.append((n, 1 << len(E), max(census), dict(sorted(census.items()))))
    return profile


def rectangle_ideals(a, b):
    elems = tuple((i, j) for i in range(a) for j in range(b))
    ans = []
    for mask in range(1 << len(elems)):
        I = frozenset(elems[k] for k in range(len(elems)) if mask >> k & 1)
        if all((ii, jj) in I for i, j in I for ii in range(i + 1) for jj in range(j + 1)):
            ans.append(I)
    return tuple(ans)


def rowmotion(I, a, b):
    comp = {(i, j) for i in range(a) for j in range(b)} - set(I)
    minima = {
        x
        for x in comp
        if not any(y != x and y[0] <= x[0] and y[1] <= x[1] for y in comp)
    }
    return frozenset((i, j) for x, y in minima for i in range(x + 1) for j in range(y + 1))


def audit_rowmotion():
    profile = []
    for a, b in ((1, 4), (2, 2), (2, 3), (3, 3)):
        A.box()
        states = rectangle_ideals(a, b)
        image = {rowmotion(I, a, b) for I in states}
        A.check(image == set(states))
        periods = Counter()
        for I in states:
            cur, t = rowmotion(I, a, b), 1
            while cur != I:
                cur = rowmotion(cur, a, b)
                t += 1
                A.check(t <= a + b)
            A.check((a + b) % t == 0)
            periods[t] += 1
        profile.append(((a, b), len(states), dict(sorted(periods.items()))))
    return profile


def audit_polygon_adjunction():
    # Exact subfamily: axis-parallel lattice rectangles, translated after each hull.
    profile = []
    for a in range(1, 11):
        for b in range(1, 11):
            A.box()
            x, y, t = a, b, 0
            while True:
                # Interior lattice points have a 2D convex hull iff x,y >= 3.
                if x < 3 or y < 3:
                    t += 1
                    break
                x, y, t = x - 2, y - 2, t + 1
            predicted = (min(a, b) + 1) // 2
            A.check(t == predicted, (a, b, t, predicted))
            profile.append((a, b, t))
    return {"boxes": len(profile), "max_tail": max(t for _, _, t in profile)}


def rsk_insert(word):
    rows = []
    for value in word:
        x = value
        r = 0
        while True:
            if r == len(rows):
                rows.append([x])
                break
            row = rows[r]
            j = next((j for j, y in enumerate(row) if y > x), len(row))
            if j == len(row):
                row.append(x)
                break
            row[j], x = x, row[j]
            r += 1
    return tuple(tuple(row) for row in rows)


def rsk_rowword(p):
    P = rsk_insert(p)
    return tuple(x for row in reversed(P) for x in row)


def audit_rsk_canonicalization():
    profile = []
    for n in range(1, 8):
        A.box()
        images = set()
        for p in perms(n):
            q = rsk_rowword(p)
            A.check(rsk_rowword(q) == q)
            A.check(rsk_insert(q) == rsk_insert(p))
            images.add(q)
        profile.append((n, len(images)))
    return profile


def tree_states(n):
    E = tuple(combinations(range(n), 2))
    ans = []
    for es in combinations(E, n - 1):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        good = True
        for u, v in es:
            ru, rv = find(u), find(v)
            if ru == rv:
                good = False
                break
            parent[ru] = rv
        if good:
            ans.append(frozenset(es))
    return tuple(ans)


def tree_path(T, s, t):
    adj = defaultdict(list)
    for u, v in T:
        adj[u].append(v)
        adj[v].append(u)
    stack = [(s, -1, [])]
    while stack:
        u, parent, path = stack.pop()
        if u == t:
            return path
        for v in adj[u]:
            if v != parent:
                stack.append((v, u, path + [edge(u, v)]))
    raise AssertionError("disconnected tree")


def matroid_greedy_step(T, n):
    target = frozenset(edge(0, v) for v in range(1, n))
    missing = sorted(target - T)
    if not missing:
        return T
    e = missing[0]
    cycle = tree_path(T, *e) + [e]
    removable = sorted((f for f in cycle if f not in target), reverse=True)
    A.check(bool(removable))
    return frozenset((set(T) | {e}) - {removable[0]})


def audit_matroid_greedy():
    profile = []
    for n in range(2, 7):
        A.box()
        states = tree_states(n)
        census = Counter()
        images = set()
        target = frozenset(edge(0, v) for v in range(1, n))
        for T in states:
            cur, t = T, 0
            while cur != target:
                nxt = matroid_greedy_step(cur, n)
                A.check(len(nxt & target) == len(cur & target) + 1)
                cur, t = nxt, t + 1
            A.check(t == len(target - T))
            census[t] += 1
            images.add(matroid_greedy_step(T, n))
        A.check(len(states) == n ** (n - 2))
        profile.append((n, len(states), len(images), dict(sorted(census.items()))))
    return profile


def main():
    wex_data = audit_wex()
    uhc_data = audit_uhc()
    fan_data = audit_frontier_fan()
    dyck_data = audit_dyck_shell()
    kreweras_data = audit_kreweras()
    promotion_data = audit_promotion()
    pp_data = audit_plane_complement()
    delaunay_data = audit_delaunay_quad()
    collapse_data = audit_lex_collapse()
    core_data = audit_graph2core()
    rowmotion_data = audit_rowmotion()
    adjunction_data = audit_polygon_adjunction()
    rsk_data = audit_rsk_canonicalization()
    matroid_data = audit_matroid_greedy()

    registry = (
        "WEX", "UHC", "TFE", "DSE", "NCK", "RSP", "BPC",
        "LDL", "LSC", "G2C", "OIR", "PLA", "RSK", "MGB",
    )
    A.check(len(registry) == 14 and len(set(registry)) == 14)

    print("P152-P156 COMBINATORIAL STAGE-1 EXACT SCOUT")
    print("external_status=HOLD_EXTERNAL")
    print("enumeration_role=counterexample_pressure_only")
    print(f"registry={','.join(registry)}")
    print(f"WEX max_tail n=1..9: {wex_data['max_tail']}")
    print(f"WEX image_count n=1..9: {wex_data['image_counts']}")
    print(f"WEX every-target fibre formula checks: {wex_data['fibre_checks']}")
    print(f"WEX sharp witnesses: {wex_data['witnesses']}")
    print(f"UHC max_tail n=1..9: {uhc_data['max_tail']}")
    print(f"UHC image_count n=1..9: {uhc_data['image_counts']}")
    print(f"UHC fixed_count n=1..9: {uhc_data['fixed_counts']}")
    print(f"TFE (n,states,image,max_tail): {[(n,s,i,t) for n,s,i,t,_ in fan_data]}")
    print(f"DSE (semilength,states,max_tail): {[(n,s,t) for n,s,t,_ in dyck_data]}")
    print(f"NCK (n,states,period-census): {kreweras_data}")
    print(f"RSP rectangle profiles: {promotion_data}")
    print(f"BPC box profiles: {pp_data}")
    print(f"LDL quadrilateral profile: {delaunay_data}")
    print(f"LSC sample tails: {[x[1] for x in collapse_data]}")
    print(f"G2C (n,graphs,max_tail): {[(n,s,t) for n,s,t,_ in core_data]}")
    print(f"OIR rectangle profiles: {rowmotion_data}")
    print(f"PLA rectangle boxes: {adjunction_data}")
    print(f"RSK (n,image-count): {rsk_data}")
    print(f"MGB (n,trees,image-count): {[(n,s,i) for n,s,i,_ in matroid_data]}")
    print(f"boxes={A.boxes}")
    print(f"assertions={A.assertions}")
    print("status=PASS")


if __name__ == "__main__":
    main()
