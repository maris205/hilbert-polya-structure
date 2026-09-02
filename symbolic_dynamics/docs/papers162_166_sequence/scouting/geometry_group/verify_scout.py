#!/usr/bin/env python3
"""Deterministic exact probes for the P162--P166 geometry/group lane.

No random choices, third-party modules, or network access are used.  The
program intentionally verifies both attractive signals and decisive negative
controls; it is a scout verifier, not evidence of novelty.
"""

from collections import Counter, deque
from itertools import combinations, product
from math import log2


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def dim(U):
    return (len(U)).bit_length() - 1


def span(vectors):
    U = {0}
    for v in vectors:
        U |= {x ^ v for x in tuple(U)}
    return frozenset(U)


def subspaces(n):
    ans = {frozenset({0})}
    for v in range(1, 1 << n):
        ans |= {span(tuple(U) + (v,)) for U in tuple(ans)}
    return tuple(sorted(ans, key=lambda U: (len(U), tuple(U))))


SUBSPACES = {n: subspaces(n) for n in range(6)}


def gaussian(n, r, q=2):
    if not 0 <= r <= n:
        return 0
    num = den = 1
    for i in range(r):
        num *= q ** (n - i) - 1
        den *= q ** (r - i) - 1
    return num // den


def flag_trace(U, t):
    return frozenset(x for x in U if x < (1 << (max(0, (max(U).bit_length() if U else 0) - t))))


def trace_to_prefix(U, k):
    return frozenset(x for x in U if x < (1 << k))


def probe_ftr():
    expected = (1, 2, 5, 16, 67, 374)
    for n, c in enumerate(expected):
        check(len(SUBSPACES[n]) == c, f"FTR subspace census n={n}")
    fibre_samples = []
    for k in range(4):
        for t in (1, 2):
            sources = SUBSPACES[k + t]
            counts = Counter(trace_to_prefix(U, k) for U in sources)
            for W in SUBSPACES[k]:
                d = dim(W)
                formula = sum(gaussian(t, r) * 2 ** (r * (k - d)) for r in range(t + 1))
                check(counts[W] == formula, f"FTR fibre k={k},t={t},d={d}")
            fibre_samples.append((k, t, tuple(sorted(set(counts.values())))))
    for n in range(1, 6):
        for U in SUBSPACES[n]:
            ranks = [dim(trace_to_prefix(U, k)) for k in range(n, -1, -1)]
            check(all(a - b in (0, 1) for a, b in zip(ranks, ranks[1:])), "FTR Schubert word")
            check(ranks[-1] == 0, "FTR terminal")
    return f"subspaces={expected}; fibre-levels={fibre_samples}"


def symp(x, y, m):
    z = 0
    for i in range(m):
        z ^= ((x >> (2 * i)) & 1) & ((y >> (2 * i + 1)) & 1)
        z ^= ((x >> (2 * i + 1)) & 1) & ((y >> (2 * i)) & 1)
    return z


def symp_radical(U, m):
    perp = frozenset(y for y in range(1 << (2 * m)) if all(symp(x, y, m) == 0 for x in U))
    return U & perp


def probe_sre():
    rows = []
    for m in (1, 2):
        S = SUBSPACES[2 * m]
        indeg = Counter()
        fixed = 0
        for U in S:
            R = symp_radical(U, m)
            check(symp_radical(R, m) == R, "SRE idempotence")
            isotropic = all(symp(x, y, m) == 0 for x in U for y in U)
            check((R == U) == isotropic, "SRE fixed iff totally isotropic")
            fixed += R == U
            indeg[R] += 1
        formula = sum(gaussian(m, r) * __import__('math').prod(2 ** (m - i) + 1 for i in range(r)) for r in range(m + 1))
        check(fixed == formula, "SRE fixed census")
        rows.append((m, len(S), fixed, len(indeg), max(indeg.values())))
    return f"(m,states,fixed,image,max-fibre)={rows}"


def subspace_sum(U, V):
    return span(tuple(U) + tuple(V))


def modular_erosion(x):
    U, V, W = x
    return (U & subspace_sum(V, W), V & subspace_sum(W, U), W & subspace_sum(U, V))


def probe_mte():
    rows = []
    for n in (1, 2, 3):
        S = SUBSPACES[n]
        indeg = Counter()
        fixed = 0
        for x in product(S, repeat=3):
            y = modular_erosion(x)
            check(modular_erosion(y) == y, "MTE observed retraction")
            criterion = all(A <= subspace_sum(B, C) for A, B, C in ((x[0], x[1], x[2]), (x[1], x[2], x[0]), (x[2], x[0], x[1])))
            check((y == x) == criterion, "MTE fixed criterion")
            fixed += y == x
            indeg[y] += 1
        rows.append((n, len(S) ** 3, fixed, len(indeg), max(indeg.values())))
    check(rows == [(1, 8, 5, 5, 4), (2, 125, 50, 50, 31), (3, 4096, 1090, 1090, 508)], "MTE frozen census")
    return f"(n,states,fixed,image,max-fibre)={rows}"


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    z = [0] * len(a)
    for i, x in enumerate(a):
        z[x] = i
    return tuple(z)


def generated(gens, n):
    H = {tuple(range(n))}
    gens = tuple(set(gens) | {inverse(g) for g in gens})
    changed = True
    while changed:
        changed = False
        for a in tuple(H):
            for b in gens:
                c = compose(a, b)
                if c not in H:
                    H.add(c)
                    changed = True
    return frozenset(H)


def symmetric_group(n):
    import itertools
    return frozenset(itertools.permutations(range(n)))


def all_subgroups(G, n):
    one = frozenset({tuple(range(n))})
    known = {one}
    queue = deque([one])
    while queue:
        H = queue.popleft()
        for g in G - H:
            K = generated(tuple(H) + (g,), n)
            if K not in known:
                known.add(K)
                queue.append(K)
    return tuple(sorted(known, key=lambda H: (len(H), tuple(sorted(H)))))


def conjugate_subgroup(H, g):
    gi = inverse(g)
    return frozenset(compose(compose(g, h), gi) for h in H)


def is_p_power(x, p):
    while x > 1 and x % p == 0:
        x //= p
    return x == 1


def p_radical_step(P, G, subgroups, n, p):
    N = frozenset(g for g in G if conjugate_subgroup(P, g) == P)
    normal_ps = [Q for Q in subgroups if Q <= N and is_p_power(len(Q), p) and all(conjugate_subgroup(Q, g) == Q for g in N)]
    return generated(tuple(g for Q in normal_ps for g in Q), n)


def probe_prc():
    rows = []
    for n in (3, 4):
        G = symmetric_group(n)
        subs = all_subgroups(G, n)
        check(len(subs) == (6 if n == 3 else 30), "PRC subgroup census")
        for p in (2, 3):
            ps = [P for P in subs if is_p_power(len(P), p)]
            indeg = Counter()
            max_depth = 0
            for P in ps:
                Q = p_radical_step(P, G, subs, n, p)
                check(P <= Q, "PRC inflationary")
                check(Q in ps, "PRC closed on p-subgroups")
                indeg[Q] += 1
                x, depth = P, 0
                while True:
                    y = p_radical_step(x, G, subs, n, p)
                    if y == x:
                        break
                    check(len(y) >= p * len(x), "PRC strict p-growth")
                    x, depth = y, depth + 1
                check(depth <= int(log2(len(G))) + 1, "PRC finite bound")
                max_depth = max(max_depth, depth)
            rows.append((n, p, len(ps), len(indeg), max_depth, max(indeg.values())))
    return f"(n,p,p-subgroups,image,height,max-fibre)={rows}"


def binary_rank(columns, mask):
    return dim(span(columns[i] for i in range(len(columns)) if mask >> i & 1))


def rank_table(columns):
    return tuple(binary_rank(columns, s) for s in range(1 << len(columns)))


def contract_first(table):
    m = (len(table)).bit_length() - 1
    e_rank = table[1]
    return tuple(table[(s << 1) | 1] - e_rank for s in range(1 << (m - 1)))


def probe_omc():
    rows = []
    for m in range(1, 5):
        mats = set()
        for r in range(0, 4):
            for cols in product(range(1 << r), repeat=m):
                mats.add(rank_table(cols))
        targets = Counter(contract_first(M) for M in mats)
        for M in mats:
            x = M
            drops = []
            for _ in range(m):
                drops.append(x[-1] - contract_first(x)[-1])
                x = contract_first(x)
            check(len(x) == 1 and x[0] == 0, "OMC terminal")
            check(all(z in (0, 1) for z in drops), "OMC greedy bits")
            check(sum(drops) == M[-1], "OMC rank recovery")
        rows.append((m, len(mats), len(targets), max(targets.values())))
    return f"(m,binary-matroids,image,max-fibre)={rows}"


def labelled_posets(n):
    ans = []
    for bits in range(1 << (n * n)):
        le = {(i, j) for i in range(n) for j in range(n) if bits >> (i * n + j) & 1}
        if any((i, i) not in le for i in range(n)):
            continue
        if any(i != j and (i, j) in le and (j, i) in le for i in range(n) for j in range(n)):
            continue
        if any((i, k) not in le for i in range(n) for j in range(n) for k in range(n) if (i, j) in le and (j, k) in le):
            continue
        ans.append(frozenset(le))
    return ans


def regular_closed_step(S, le, n):
    interior = {x for x in range(n) if all(y in S for y in range(n) if (x, y) in le)}
    return frozenset(x for x in range(n) if any((x, y) in le for y in interior))


def probe_rcr():
    posets = labelled_posets(3)
    check(len(posets) == 19, "RCR labelled posets")
    fixed_hist = Counter()
    max_fibre = 0
    for le in posets:
        indeg = Counter()
        for mask in range(8):
            S = frozenset(i for i in range(3) if mask >> i & 1)
            T = regular_closed_step(S, le, 3)
            check(regular_closed_step(T, le, 3) == T, "RCR idempotence")
            indeg[T] += 1
        fixed_hist[len(indeg)] += 1
        max_fibre = max(max_fibre, max(indeg.values()))
    return f"posets=19; regular-closed-count-hist={sorted(fixed_hist.items())}; max-fibre={max_fibre}"


def graph_distances(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    D = [[n + 1] * n for _ in range(n)]
    for s in range(n):
        D[s][s] = 0
        q = deque([s])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if D[s][y] > D[s][x] + 1:
                    D[s][y] = D[s][x] + 1; q.append(y)
    return D


def center_set(S, D):
    vals = [max(D[x][s] for s in S) for x in range(len(D))]
    z = min(vals)
    return frozenset(i for i, v in enumerate(vals) if v == z)


def farthest_hole_set(S, D):
    vals = [min(D[x][s] for s in S) for x in range(len(D))]
    z = max(vals)
    return frozenset(i for i, v in enumerate(vals) if v == z)


def functional_signature(states, step):
    indeg = Counter(step(S) for S in states)
    cycles = Counter(); max_tail = 0
    for S in states:
        seen = {}; x = S; t = 0
        while x not in seen:
            seen[x] = t; x = step(x); t += 1
        tail, cyc = seen[x], t - seen[x]
        max_tail = max(max_tail, tail); cycles[cyc] += 1
    return len(indeg), max(indeg.values()), max_tail, tuple(sorted(cycles.items()))


def probe_mcs():
    rows = []
    for kind, n in (("P", 6), ("C", 5), ("C", 6)):
        edges = [(i, i + 1) for i in range(n - 1)] + ([(n - 1, 0)] if kind == "C" else [])
        D = graph_distances(n, edges)
        states = [frozenset(i for i in range(n) if mask >> i & 1) for mask in range(1, 1 << n)]
        sig = functional_signature(states, lambda S: center_set(S, D))
        if kind == "P":
            for S in states:
                check(center_set(center_set(S, D), D) == center_set(S, D), "MCS path retraction")
        rows.append((kind, n, sig))
    check(rows == [('P', 6, (11, 21, 1, ((1, 63),))), ('C', 5, (11, 11, 1, ((1, 31),))), ('C', 6, (39, 4, 2, ((1, 45), (2, 18))))], "MCS frozen signatures")
    return str(rows)


def probe_mfs():
    rows = []
    for kind, n in (("P", 6), ("C", 5), ("C", 6)):
        edges = [(i, i + 1) for i in range(n - 1)] + ([(n - 1, 0)] if kind == "C" else [])
        D = graph_distances(n, edges)
        states = [frozenset(i for i in range(n) if mask >> i & 1) for mask in range(1, 1 << n)]
        for S in states:
            check(bool(farthest_hole_set(S, D)), "MFS nonempty")
        rows.append((kind, n, functional_signature(states, lambda S: farthest_hole_set(S, D))))
    return str(rows)


def essential_core(S):
    r = dim(span(S))
    return frozenset(x for x in S if dim(span(S - {x})) < r)


def probe_epc():
    pts = frozenset(range(1, 8))
    states = [frozenset(x for x in pts if mask >> (x - 1) & 1) for mask in range(128)]
    indeg = Counter()
    for S in states:
        T = essential_core(S)
        independent = dim(span(S)) == len(S)
        check(essential_core(T) == T, "EPC idempotence")
        check((T == S) == independent, "EPC fixed independent")
        indeg[T] += 1
    check(len(indeg) == 57, "EPC Fano independent-set count")
    return f"states=128; image=fixed=57; fibre-hist={sorted(Counter(indeg.values()).items())}"


def parallel_unique_step(mask, q):
    out = 0
    for d in range(q + 1):
        block = [d * q + b for b in range(q)]
        chosen = [i for i in block if mask >> i & 1]
        if len(chosen) == 1:
            out |= 1 << chosen[0]
    return out


def probe_lpu():
    rows = []
    for q in (2, 3):
        N = q * (q + 1)
        indeg = Counter(parallel_unique_step(S, q) for S in range(1 << N))
        check(len(indeg) == (q + 1) ** (q + 1), "LPU image census")
        for T, c in indeg.items():
            check(parallel_unique_step(T, q) == T, "LPU fixed image")
            b = T.bit_count()
            check(c == (2 ** q - q) ** (q + 1 - b), "LPU every-target fibre")
        rows.append((q, 1 << N, len(indeg), max(indeg.values())))
    return f"(q,states,image,max-fibre)={rows}"


def complexes(n):
    nonempty = tuple(range(1, 1 << n))
    ans = []
    for pick in range(1 << len(nonempty)):
        facets = tuple(nonempty[i] for i in range(len(nonempty)) if pick >> i & 1)
        if all(not (a != b and a & b == a) for a in facets for b in facets):
            ans.append(tuple(sorted(facets)))
    return ans


def faces_of(facets):
    faces = {0}
    for F in facets:
        s = F
        while True:
            faces.add(s)
            if s == 0: break
            s = (s - 1) & F
    return faces


def maximal_faces(faces):
    nz = [F for F in faces if F]
    return tuple(sorted(F for F in nz if not any(F != G and F & G == F for G in nz)))


def euler_link_prune(facets, n):
    faces = faces_of(facets)
    keep = 0
    for v in range(n):
        bit = 1 << v
        link = {F for F in range(1 << n) if not F & bit and (F | bit) in faces}
        chi = sum((-1) ** (F.bit_count() - 1) for F in link if F)
        if chi % 2:
            keep |= bit
    induced = {F for F in faces if F & ~keep == 0}
    return maximal_faces(induced)


def boundary_derivative(facets):
    if not facets:
        return ()
    dsize = max(F.bit_count() for F in facets)
    top = [F for F in facets if F.bit_count() == dsize]
    if dsize == 0:
        return ()
    ridges = Counter(F & ~(1 << v) for F in top for v in range(F.bit_length()) if F >> v & 1)
    return maximal_faces({R for R, c in ridges.items() if c == 1})


def probe_elp():
    C = complexes(4)
    # 167 labelled complexes when the void complex and {empty face} are
    # represented by the same empty facet tuple (Dedekind M(4)-1).
    check(len(C) == 167, "ELP complex census")
    indeg = Counter(); depths = Counter()
    for K in C:
        T = euler_link_prune(K, 4)
        check(set(faces_of(T)) <= set(faces_of(K)), "ELP decreasing")
        indeg[T] += 1
        x, d = K, 0
        while True:
            y = euler_link_prune(x, 4)
            if y == x: break
            x, d = y, d + 1
            check(d <= 4, "ELP vertex-height bound")
        depths[d] += 1
    return f"complexes=167; image={len(indeg)}; depth-hist={sorted(depths.items())}; max-fibre={max(indeg.values())}"


def probe_bpd():
    C = complexes(4)
    indeg = Counter(); depths = Counter()
    for K in C:
        T = boundary_derivative(K)
        indeg[T] += 1
        x, d = K, 0
        prev_dim = max((F.bit_count() for F in x), default=0)
        while x:
            y = boundary_derivative(x)
            new_dim = max((F.bit_count() for F in y), default=0)
            check(not y or new_dim < prev_dim, "BPD strict dimension drop")
            x, prev_dim, d = y, new_dim, d + 1
            check(d <= 4, "BPD dimension-height bound")
        depths[d] += 1
    return f"complexes=167; image={len(indeg)}; depth-hist={sorted(depths.items())}; max-fibre={max(indeg.values())}"


def main():
    probes = [
        ("GG01/FTR", probe_ftr),
        ("GG02/SRE", probe_sre),
        ("GG03/MTE", probe_mte),
        ("GG04/PRC", probe_prc),
        ("GG05/OMC", probe_omc),
        ("GG06/RCR", probe_rcr),
        ("GG07/MCS", probe_mcs),
        ("GG08/MFS", probe_mfs),
        ("GG09/EPC", probe_epc),
        ("GG10/LPU", probe_lpu),
        ("GG11/ELP", probe_elp),
        ("GG12/BPD", probe_bpd),
    ]
    print("P162--P166 geometry/group/topology deterministic scout")
    for name, probe in probes:
        print(f"{name}: {probe()}")
    print(f"PASS assertions={ASSERTIONS} systems={len(probes)} shortlist=0 status=EMPTY_POOL HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
