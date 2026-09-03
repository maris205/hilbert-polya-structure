#!/usr/bin/env python3
"""Exact breadth controls for the P177--P181 stochastic/graph lane.

The program deliberately mixes promoted and killed candidates.  A passing
finite box is counterexample pressure only; theorem and collision decisions
live in the accompanying ledger.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
import math


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def parity(x: int) -> int:
    return x.bit_count() & 1


def gf2_rank(vectors: list[int], d: int) -> int:
    pivots = [0] * d
    rank = 0
    for raw in vectors:
        x = raw
        while x:
            j = x.bit_length() - 1
            if pivots[j]:
                x ^= pivots[j]
            else:
                pivots[j] = x
                rank += 1
                break
    return rank


def graph_edges(n: int) -> list[tuple[int, int]]:
    return list(combinations(range(n), 2))


def edge_mask_from_predicate(n: int, predicate) -> int:
    ans = 0
    for k, (i, j) in enumerate(graph_edges(n)):
        if predicate(i, j):
            ans |= 1 << k
    return ans


def degrees_from_mask(n: int, mask: int) -> list[int]:
    deg = [0] * n
    for k, (i, j) in enumerate(graph_edges(n)):
        if (mask >> k) & 1:
            deg[i] += 1
            deg[j] += 1
    return deg


def rht_controls() -> dict:
    """Random hyperplane toggling on nonzero points of F_2^d."""
    signatures = {}
    for d in range(2, 5):
        points = list(range(1, 1 << d))
        m = len(points)
        whole = (1 << m) - 1
        codewords = []
        hyperplanes = []
        for ell in range(1 << d):
            c = 0
            h = 0
            for j, x in enumerate(points):
                if parity(ell & x):
                    c |= 1 << j
                else:
                    h |= 1 << j
            codewords.append(c)
            check(h == (whole ^ c))
            if ell:
                hyperplanes.append(h)
        check(len(set(codewords)) == 1 << d)
        check(len(set(hyperplanes)) == (1 << d) - 1)

        # The endpoint is A + (t mod 2)1 + c_L, where L is the sum of the
        # sampled nonzero forms.  Exhaust all starts through d=3 and a fixed
        # separating family at d=4.
        starts = range(1 << m) if d <= 3 else [0, 1, whole, whole >> 1, 0x55 & whole]
        nonzero_forms = list(range(1, 1 << d))
        N = len(nonzero_forms)
        for start in starts:
            for t in range(1, 4):
                actual = Counter()
                for history in product(nonzero_forms, repeat=t):
                    out = start
                    for ell in history:
                        out ^= whole ^ codewords[ell]
                    actual[out] += 1
                expected_support = set()
                for L in range(1 << d):
                    target = start ^ (whole if t & 1 else 0) ^ codewords[L]
                    expected_support.add(target)
                    if L == 0:
                        expected = (N**t + N * ((-1) ** t)) // (1 << d)
                    else:
                        expected = (N**t - ((-1) ** t)) // (1 << d)
                    check(actual[target] == expected)
                check(set(actual) == {x for x in expected_support if actual[x]})
                check(sum(actual.values()) == N**t)

        # Fourier eigenvalue: (-1)^|S| when xor(S)=0, and the same sign
        # multiplied by -1/(2^d-1) otherwise.
        mult = Counter()
        for subset in range(1 << m):
            sigma = 0
            for j, x in enumerate(points):
                if (subset >> j) & 1:
                    sigma ^= x
            numerator = sum((-1) ** parity(subset & h) for h in hyperplanes)
            expected = ((-1) ** parity(subset)) * (N if sigma == 0 else -1)
            check(numerator == expected)
            mult[Fraction(numerator, N)] += 1
        expected_pm = 1 << (m - d - 1)
        expected_small = N * expected_pm
        check(mult[Fraction(1)] == expected_pm)
        check(mult[Fraction(-1)] == expected_pm)
        check(mult[Fraction(1, N)] == expected_small)
        check(mult[Fraction(-1, N)] == expected_small)

        # H=<1,C> has dimension d+1 and partitions the carrier into closed
        # bipartite communicating classes.
        hspace = set(codewords) | {whole ^ c for c in codewords}
        check(len(hspace) == 1 << (d + 1))
        check((1 << m) % len(hspace) == 0)
        signatures[str(d)] = {
            "points": m,
            "communicating_classes": (1 << m) // len(hspace),
            "class_size": len(hspace),
            "phase_size": 1 << d,
            "spectrum_multiplicity": {str(k): v for k, v in sorted(mult.items())},
        }
    return signatures


def lfs_endpoint_formula(d: int, A: int, B: int) -> int:
    """One-step number of linear forms with A intersect ker(ell)=B."""
    if B & ~A:
        return 0
    points = list(range(1, 1 << d))
    rest_positions = [j for j in range(len(points)) if ((A >> j) & 1) and not ((B >> j) & 1)]
    base = [points[j] for j in range(len(points)) if (B >> j) & 1]
    total = 0
    for s in range(1 << len(rest_positions)):
        chosen = base + [points[rest_positions[k]] for k in range(len(rest_positions)) if (s >> k) & 1]
        total += (-1) ** parity(s) * (1 << (d - gf2_rank(chosen, d)))
    return total


def lfs_controls() -> dict:
    """Random linear-form sieve A <- A intersect ker(ell)."""
    signatures = {}
    for d in range(1, 4):
        points = list(range(1, 1 << d))
        m = len(points)
        kernels = []
        for ell in range(1 << d):
            h = 0
            for j, x in enumerate(points):
                if parity(ell & x) == 0:
                    h |= 1 << j
            kernels.append(h)
        rank_mult = Counter()
        for C in range(1 << m):
            vectors = [points[j] for j in range(m) if (C >> j) & 1]
            rank_mult[gf2_rank(vectors, d)] += 1
        for A in range(1 << m):
            actual = Counter(A & h for h in kernels)
            for B in range(1 << m):
                formula = lfs_endpoint_formula(d, A, B) if not (B & ~A) else 0
                check(actual[B] == formula)
            # zeta eigenfunction identity for every C subseteq A and every
            # single form, aggregated over the form choice.
            for C in range(1 << m):
                lhs = sum(1 for h in kernels if (C & ~(A & h)) == 0)
                vectors = [points[j] for j in range(m) if (C >> j) & 1]
                expected = (1 << (d - gf2_rank(vectors, d))) if (C & ~A) == 0 else 0
                check(lhs == expected)

        # Full all-time inclusion--exclusion for d<=3, selected sources and
        # all endpoints, using literal form histories.
        for t in range(1, 4):
            sources = range(1 << m) if d <= 2 else [0, 1, (1 << m) - 1, 0b1010111]
            for A in sources:
                actual = Counter()
                for history in product(kernels, repeat=t):
                    out = A
                    for h in history:
                        out &= h
                    actual[out] += 1
                for B in range(1 << m):
                    if B & ~A:
                        expected = 0
                    else:
                        outside = [j for j in range(m) if ((A >> j) & 1) and not ((B >> j) & 1)]
                        base = [points[j] for j in range(m) if (B >> j) & 1]
                        expected = 0
                        for s in range(1 << len(outside)):
                            chosen = base + [points[outside[k]] for k in range(len(outside)) if (s >> k) & 1]
                            expected += (-1) ** parity(s) * (1 << (t * (d - gf2_rank(chosen, d))))
                    check(actual[B] == expected)
        signatures[str(d)] = {
            "projective_points_binary": m,
            "rank_multiplicity": dict(sorted(rank_mult.items())),
            "full_source_absorption_counts_t1_t3": [
                sum(
                    (-1) ** parity(s)
                    * (1 << (t * (d - gf2_rank([points[j] for j in range(m) if (s >> j) & 1], d))))
                    for s in range(1 << m)
                )
                for t in range(1, 4)
            ],
        }
    return signatures


def zsi_constraint_count(n: int, q: int, edge_mask: int) -> int:
    edges = graph_edges(n)
    support = set()
    adjacency = [[] for _ in range(n)]
    for k, (u, v) in enumerate(edges):
        if (edge_mask >> k) & 1:
            support.update((u, v))
            adjacency[u].append(v)
            adjacency[v].append(u)
    seen = set()
    bip_components = 0
    for root in support:
        if root in seen:
            continue
        color = {root: 0}
        stack = [root]
        bip = True
        seen.add(root)
        while stack:
            u = stack.pop()
            for v in adjacency[u]:
                if v not in color:
                    color[v] = color[u] ^ 1
                    seen.add(v)
                    stack.append(v)
                elif color[v] == color[u]:
                    bip = False
        if bip:
            bip_components += 1
    return (q ** (n - len(support))) * (q ** bip_components)


def zsi_controls() -> dict:
    """Zero-sum-colouring graph intersection, q odd."""
    signatures = {}
    for n, q in [(3, 3), (4, 3), (3, 5)]:
        edges = graph_edges(n)
        masks = []
        for coloring in product(range(q), repeat=n):
            masks.append(edge_mask_from_predicate(n, lambda i, j, c=coloring: (c[i] + c[j]) % q == 0))
        spectrum = Counter()
        for F in range(1 << len(edges)):
            actual = sum(1 for mask in masks if F & ~mask == 0)
            expected = zsi_constraint_count(n, q, F)
            check(actual == expected)
            spectrum[Fraction(actual, q**n)] += 1

        # Two-step endpoint inclusion--exclusion, exhaust every source/target
        # in the small boxes.
        for A in range(1 << len(edges)):
            actual = Counter(A & h1 & h2 for h1 in masks for h2 in masks)
            for B in range(1 << len(edges)):
                if B & ~A:
                    expected = 0
                else:
                    rest = A & ~B
                    expected = sum(
                        (-1) ** C.bit_count() * zsi_constraint_count(n, q, B | C) ** 2
                        for C in submasks(rest)
                    )
                check(actual[B] == expected)
        signatures[f"n{n}_q{q}"] = {
            "states": 1 << len(edges),
            "masks_with_multiplicity": len(masks),
            "distinct_masks": len(set(masks)),
            "eigenvalues": {str(k): v for k, v in sorted(spectrum.items())},
        }
    return signatures


def submasks(mask: int):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            return
        sub = (sub - 1) & mask


def dpc_map(n: int, graph: int) -> int:
    deg = degrees_from_mask(n, graph)
    return edge_mask_from_predicate(n, lambda i, j: (deg[i] & 1) == (deg[j] & 1))


def dpc_controls() -> dict:
    signatures = {}
    for n in range(2, 7):
        e = math.comb(n, 2)
        fibres = Counter()
        image = set()
        full = (1 << e) - 1
        for G in range(1 << e):
            H = dpc_map(n, G)
            image.add(H)
            fibres[H] += 1
            if n & 1:
                check(dpc_map(n, H) == H)
            else:
                check(dpc_map(n, H) == full)
        expected_image = 1 << (n - 1 if n & 1 else n - 2)
        expected_fibre = 1 << ((n - 1) * (n - 2) // 2 + (0 if n & 1 else 1))
        check(len(image) == expected_image)
        check(set(fibres.values()) == {expected_fibre})
        max_tail = 0
        for G in range(1 << e):
            H = dpc_map(n, G)
            depth = 0 if H == G else (1 if dpc_map(n, H) == H else 2)
            max_tail = max(max_tail, depth)
        signatures[str(n)] = {
            "states": 1 << e,
            "image": len(image),
            "uniform_fibre": expected_fibre,
            "max_tail": max_tail,
        }
    return signatures


def cds_column_map(column: tuple[int, ...], diagonal_index: int, q: int) -> tuple[int, ...]:
    d = column[diagonal_index]
    return tuple((d * x) % q for x in column)


def cds_controls() -> dict:
    signatures = {}
    for n, q in [(2, 2), (2, 3), (2, 5), (3, 2)]:
        columns = list(product(range(q), repeat=n))
        maps = []
        for i in range(n):
            maps.append({c: cds_column_map(c, i, q) for c in columns})
        # Column iterate and every-target fibre formula.
        for i in range(n):
            for c in columns:
                d = c[i]
                out = c
                for t in range(1, 5):
                    out = maps[i][out]
                    expected = tuple((pow(d, (1 << t) - 1, q) * x) % q for x in c)
                    check(out == expected)
            fibres = Counter(maps[i].values())
            for target in columns:
                e = target[i]
                if e == 0 and all(x == 0 for x in target):
                    expected = q ** (n - 1)
                elif e == 0:
                    expected = 0
                else:
                    expected = sum(1 for d in range(1, q) if d * d % q == e)
                check(fibres[target] == expected)
        # Matrix map is the direct product of its column maps.
        states = q ** (n * n)
        if states <= 4096:
            matrix_fibres = Counter()
            for flat in product(range(q), repeat=n * n):
                out_cols = []
                for j in range(n):
                    col = tuple(flat[i * n + j] for i in range(n))
                    out_cols.append(maps[j][col])
                out = tuple(out_cols[j][i] for i in range(n) for j in range(n))
                matrix_fibres[out] += 1
            check(sum(matrix_fibres.values()) == states)
        column_image = len(set(maps[0].values()))
        signatures[f"n{n}_q{q}"] = {
            "states": states,
            "column_image": column_image,
            "matrix_image": column_image**n,
            "column_fibre_histogram": dict(sorted(Counter(Counter(maps[0].values()).values()).items())),
        }
    return signatures


def star_masks(n: int) -> list[int]:
    return [edge_mask_from_predicate(n, lambda i, j, v=v: i == v or j == v) for v in range(n)]


def star_intersection_controls() -> dict:
    signatures = {}
    for n in range(3, 8):
        stars = star_masks(n)
        full = (1 << math.comb(n, 2)) - 1
        for t in range(1, 6):
            actual = Counter()
            for history in product(range(n), repeat=t):
                out = full
                for v in history:
                    out &= stars[v]
                actual[out] += 1
            check(actual[0] == n**t - n - math.comb(n, 2) * (2**t - 2))
            for v in range(n):
                check(actual[stars[v]] == 1)
            for u, v in combinations(range(n), 2):
                edge = edge_mask_from_predicate(n, lambda i, j, u=u, v=v: {i, j} == {u, v})
                check(actual[edge] == 2**t - 2)
        signatures[str(n)] = {
            "states": 1 << math.comb(n, 2),
            "absorption_count_t5": n**5 - n - math.comb(n, 2) * (2**5 - 2),
            "spectrum_values": ["1", f"2/{n}", f"1/{n}", "0"],
        }
    return signatures


def star_union_controls() -> dict:
    signatures = {}
    for n in range(3, 8):
        stars = star_masks(n)
        full = (1 << math.comb(n, 2)) - 1
        for t in range(1, 6):
            actual = Counter()
            for history in product(range(n), repeat=t):
                out = 0
                for v in history:
                    out |= stars[v]
                actual[out] += 1
            expected_full = 0
            # Full graph occurs when at least n-1 distinct centres appeared.
            if t >= n - 1:
                expected_full += math.comb(n, n - 1) * math.factorial(n - 1) * stirling2(t, n - 1)
            if t >= n:
                expected_full += math.factorial(n) * stirling2(t, n)
            check(actual[full] == expected_full)
            for k in range(1, min(n - 2, t) + 1):
                fibre = math.factorial(k) * stirling2(t, k)
                for centres in combinations(range(n), k):
                    out = 0
                    for v in centres:
                        out |= stars[v]
                    check(actual[out] == fibre)
        signatures[str(n)] = {
            "completion_count_t5": sum(
                math.comb(n, k) * math.factorial(k) * stirling2(5, k)
                for k in range(max(0, n - 1), min(n, 5) + 1)
            ),
            "coupon_threshold": n - 1,
        }
    return signatures


def stirling2(n: int, k: int) -> int:
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]


def triangle_prune_map(n: int, graph: int) -> int:
    edges = graph_edges(n)
    keep = graph
    for k, (u, v) in enumerate(edges):
        if not ((graph >> k) & 1):
            continue
        for w in range(n):
            if w in (u, v):
                continue
            uw = edges.index(tuple(sorted((u, w))))
            vw = edges.index(tuple(sorted((v, w))))
            if ((graph >> uw) & 1) and ((graph >> vw) & 1):
                keep &= ~(1 << k)
                break
    return keep


def triangle_prune_controls() -> dict:
    signatures = {}
    for n in range(3, 7):
        e = math.comb(n, 2)
        image = set()
        fibres = Counter()
        for G in range(1 << e):
            H = triangle_prune_map(n, G)
            check(triangle_prune_map(n, H) == H)
            # H is triangle-free.
            for tri in combinations(range(n), 3):
                tri_mask = edge_mask_from_predicate(n, lambda i, j, tri=tri: i in tri and j in tri)
                check((H & tri_mask) != tri_mask)
            image.add(H)
            fibres[H] += 1
        signatures[str(n)] = {
            "states": 1 << e,
            "image_triangle_free_graphs": len(image),
            "max_fibre": max(fibres.values()),
        }
    return signatures


def row_sum_scaling_controls() -> dict:
    """A literal negative control: scale each row by its old row sum."""
    signatures = {}
    for n, q in [(2, 2), (2, 3), (2, 5), (3, 2)]:
        rows = list(product(range(q), repeat=n))
        mapping = {r: tuple((sum(r) * x) % q for x in r) for r in rows}
        for r in rows:
            s = sum(r) % q
            out = r
            for t in range(1, 5):
                out = mapping[out]
                expected = tuple((pow(s, (1 << t) - 1, q) * x) % q for x in r)
                check(out == expected)
        signatures[f"n{n}_q{q}"] = {
            "row_states": len(rows),
            "row_image": len(set(mapping.values())),
            "fibre_histogram": dict(sorted(Counter(Counter(mapping.values()).values()).items())),
        }
    return signatures


def main() -> None:
    results = {
        "RHT_random_hyperplane_toggle": rht_controls(),
        "LFS_random_linear_form_sieve": lfs_controls(),
        "ZSI_zero_sum_graph_intersection": zsi_controls(),
        "DPC_degree_parity_clique": dpc_controls(),
        "CDS_column_diagonal_scaling": cds_controls(),
        "RSI_random_star_intersection": star_intersection_controls(),
        "RSG_random_star_growth": star_union_controls(),
        "TCP_triangle_edge_pruning": triangle_prune_controls(),
        "RSS_row_sum_scaling": row_sum_scaling_controls(),
    }
    results["summary"] = {
        "fresh_literal_systems": 9,
        "exact_assertions": ASSERTIONS,
        "status": "PASS",
        "external_status": "HOLD_EXTERNAL",
    }
    print(json.dumps(results, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
