#!/usr/bin/env python3
"""Exact breadth scout for stochastic/matrix/relation candidates P172--P176.

All calculations are finite, exhaustive, integer/rational, and deterministic.
The executable is falsification evidence only; it is not an all-parameter
proof or an ownership/novelty certificate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
import json


ASSERTIONS = 0


def check(condition, witness):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(witness)


def parity(x):
    return x.bit_count() & 1


def gf2_rank_rows(rows, width):
    rows = list(rows)
    rank = 0
    for col in range(width - 1, -1, -1):
        pivot = next((j for j in range(rank, len(rows)) if (rows[j] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for j in range(len(rows)):
            if j != rank and ((rows[j] >> col) & 1):
                rows[j] ^= rows[rank]
        rank += 1
    return rank


def matrix_rows(mask, r, c):
    return [(mask >> (i * c)) & ((1 << c) - 1) for i in range(r)]


def matrix_rank(mask, r, c):
    return gf2_rank_rows(matrix_rows(mask, r, c), c)


def outer_mask(u, v, r, c):
    ans = 0
    for i in range(r):
        if (u >> i) & 1:
            ans |= v << (i * c)
    return ans


def convolve_xor(left, right):
    out = Counter()
    for x, a in left.items():
        for y, b in right.items():
            out[x ^ y] += a * b
    return out


def walsh(counter, bits):
    return [sum(v * (-1 if parity(k & x) else 1) for x, v in counter.items())
            for k in range(1 << bits)]


def invert_walsh(power_values, bits):
    den = 1 << bits
    out = []
    for y in range(1 << bits):
        num = sum(v * (-1 if parity(k & y) else 1)
                  for k, v in enumerate(power_values))
        check(num % den == 0, ("walsh divisibility", bits, y, num))
        out.append(num // den)
    return out


def span_rank(vectors, width):
    return gf2_rank_rows(vectors, width)


def functional_stats(nexts):
    n = len(nexts)
    indeg = [0] * n
    for y in nexts:
        indeg[y] += 1
    tails = []
    periods = []
    for source in range(n):
        seen = {}
        x = source
        t = 0
        while x not in seen:
            seen[x] = t
            x = nexts[x]
            t += 1
        tails.append(seen[x])
        periods.append(t - seen[x])
    return {
        "states": n,
        "image": len(set(nexts)),
        "fixed": sum(i == nexts[i] for i in range(n)),
        "periods": sorted(set(periods)),
        "max_tail": max(tails, default=0),
        "max_fibre": max(indeg, default=0),
    }


def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return stirling2(n - 1, k - 1) + k * stirling2(n - 1, k)


stirling2 = lru_cache(None)(stirling2)


def factorial(n):
    ans = 1
    for k in range(2, n + 1):
        ans *= k
    return ans


def gaussian(n, k, q=2):
    if k < 0 or k > n:
        return 0
    num = den = 1
    for i in range(k):
        num *= q ** (n - i) - 1
        den *= q ** (k - i) - 1
    check(num % den == 0, ("gaussian", n, k, q))
    return num // den


def onto_linear(a, r, q=2):
    if r < 0 or r > a:
        return 0
    ans = 1
    for i in range(r):
        ans *= q ** a - q ** i
    return ans


def enumerate_subspaces(n):
    # Full exhaustive closure test is deliberately limited to n <= 4.
    vectors = range(1 << n)
    out = []
    for mask in range(1 << (1 << n)):
        if not (mask & 1):
            continue
        elems = [x for x in vectors if (mask >> x) & 1]
        if len(elems) & (len(elems) - 1):
            continue
        good = True
        for x in elems:
            for y in elems:
                if not ((mask >> (x ^ y)) & 1):
                    good = False
                    break
            if not good:
                break
        if good:
            out.append(frozenset(elems))
    expected = sum(gaussian(n, k, 2) for k in range(n + 1))
    check(len(out) == expected, ("subspace census", n, len(out), expected))
    return sorted(out, key=lambda s: (len(s), tuple(sorted(s))))


def enumerate_subspaces_rref(n):
    """Enumerate all binary subspaces via their unique reduced row echelon basis."""
    out = []
    for k in range(n + 1):
        for pivots in combinations(range(n), k):
            free_positions = []
            pivot_set = set(pivots)
            for i, p in enumerate(pivots):
                free_positions.extend((i, j) for j in range(p + 1, n)
                                      if j not in pivot_set)
            for assignment in range(1 << len(free_positions)):
                rows = [1 << p for p in pivots]
                for z, (i, j) in enumerate(free_positions):
                    if (assignment >> z) & 1:
                        rows[i] |= 1 << j
                out.append(span_vectors(rows))
    expected = sum(gaussian(n, k, 2) for k in range(n + 1))
    check(len(out) == expected, ("rref subspace census", n, len(out), expected))
    check(len(set(out)) == len(out), ("rref duplicate", n))
    return sorted(out, key=lambda s: (len(s), tuple(sorted(s))))


def subspace_dim(U):
    return len(U).bit_length() - 1


def span_vectors(gens):
    vals = {0}
    for g in gens:
        vals |= {x ^ g for x in tuple(vals)}
    return frozenset(vals)


def apply_linear(mask, x, n):
    ans = 0
    for i, row in enumerate(matrix_rows(mask, n, n)):
        ans |= parity(row & x) << i
    return ans


def matmul_transpose_gf2(mask, n):
    rows = matrix_rows(mask, n, n)
    out = 0
    for i in range(n):
        for j in range(n):
            if parity(rows[i] & rows[j]):
                out |= 1 << (i * n + j)
    return out


def symmetric_index(n):
    return [(i, j) for i in range(n) for j in range(i, n)]


def symmetric_outer(v, n):
    ans = 0
    for k, (i, j) in enumerate(symmetric_index(n)):
        if ((v >> i) & 1) and ((v >> j) & 1):
            ans |= 1 << k
    return ans


def alternating_index(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def alternating_outer(u, v, n):
    ans = 0
    for k, (i, j) in enumerate(alternating_index(n)):
        if (((u >> i) & 1) & ((v >> j) & 1)) ^ (((v >> i) & 1) & ((u >> j) & 1)):
            ans |= 1 << k
    return ans


def alternating_full(mask, n):
    rows = [0] * n
    for k, (i, j) in enumerate(alternating_index(n)):
        if (mask >> k) & 1:
            rows[i] |= 1 << j
            rows[j] |= 1 << i
    return rows


def candidate_m01():
    runs = []
    total_checks_before = ASSERTIONS
    for r, c in [(1, 1), (2, 2), (2, 3), (3, 3)]:
        bits = r * c
        inc = Counter(outer_mask(u, v, r, c)
                      for u in range(1 << r) for v in range(1 << c))
        ft = walsh(inc, bits)
        for B, val in enumerate(ft):
            expected = 1 << (r + c - matrix_rank(B, r, c))
            check(val == expected, ("M01 spectrum", r, c, B, val, expected))
        dist = Counter({0: 1})
        for t in range(1, 4):
            dist = convolve_xor(dist, inc)
            inv = invert_walsh([x ** t for x in ft], bits)
            for y in range(1 << bits):
                check(dist[y] == inv[y], ("M01 endpoint", r, c, t, y))
        hist = Counter(matrix_rank(B, r, c) for B in range(1 << bits))
        runs.append({"shape": [r, c], "increment_support": len(inc),
                     "rank_multiplicities": dict(sorted(hist.items())),
                     "three_step_support": len(dist)})
    return {"id": "M01", "name": "rectangular rank-one additive walk",
            "runs": runs, "assertions": ASSERTIONS - total_checks_before}


def candidate_m02():
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        bits = n * (n + 1) // 2
        inc = Counter(symmetric_outer(v, n) for v in range(1 << n))
        ft = walsh(inc, bits)
        dist = Counter({0: 1})
        for t in range(1, 4):
            dist = convolve_xor(dist, inc)
            inv = invert_walsh([x ** t for x in ft], bits)
            for y in range(1 << bits):
                check(dist[y] == inv[y], ("M02 endpoint", n, t, y))
        check(span_rank(list(inc), bits) == bits, ("M02 span", n))
        runs.append({"n": n, "states": 1 << bits,
                     "walsh_numerator_histogram": dict(sorted(Counter(ft).items())),
                     "three_step_support": len(dist)})
    return {"id": "M02", "name": "binary symmetric Gram-addition walk",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_m03():
    runs = []
    before = ASSERTIONS
    for n in range(2, 6):
        bits = n * (n - 1) // 2
        inc = Counter(alternating_outer(u, v, n)
                      for u in range(1 << n) for v in range(1 << n))
        ft = walsh(inc, bits)
        for B, val in enumerate(ft):
            rank = gf2_rank_rows(alternating_full(B, n), n)
            expected = 1 << (2 * n - rank)
            check(val == expected, ("M03 spectrum", n, B, val, expected))
        dist = convolve_xor(Counter({0: 1}), inc)
        dist = convolve_xor(dist, inc)
        inv = invert_walsh([x * x for x in ft], bits)
        for y in range(1 << bits):
            check(dist[y] == inv[y], ("M03 endpoint", n, y))
        runs.append({"n": n, "states": 1 << bits, "increment_support": len(inc),
                     "rank_histogram": dict(sorted(Counter(
                         gf2_rank_rows(alternating_full(B, n), n)
                         for B in range(1 << bits)).items()))})
    return {"id": "M03", "name": "alternating wedge-addition walk",
            "runs": runs, "assertions": ASSERTIONS - before}


def permutation_matrix(p):
    n = len(p)
    return sum(1 << (i * n + p[i]) for i in range(n))


def candidate_m04():
    runs = []
    before = ASSERTIONS
    for n in range(2, 5):
        bits = n * n
        inc = Counter(permutation_matrix(p) for p in permutations(range(n)))
        ft = walsh(inc, bits)
        check(sum(inc.values()) == factorial(n), ("M04 mass", n))
        # Direct character definition and the two-step Parseval return count.
        two_return = sum(v * v for v in inc.values())
        check(sum(x * x for x in ft) == (1 << bits) * two_return,
              ("M04 Parseval", n))
        runs.append({"n": n, "ambient_states": 1 << bits,
                     "increment_span_dimension": span_rank(list(inc), bits),
                     "eigen_numerator_histogram": dict(sorted(Counter(ft).items())),
                     "two_step_return_histories": two_return})
    return {"id": "M04", "name": "permutation-matrix XOR walk",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_m05():
    runs = []
    before = ASSERTIONS
    for r, c in [(2, 2), (2, 3), (3, 3)]:
        bits = r * c
        rectangles = [outer_mask(u, v, r, c)
                      for u in range(1, 1 << r) for v in range(1, 1 << c)]
        next_supports = []
        diag_hist = Counter()
        for A in range(1 << bits):
            succ = Counter(A | z for z in rectangles)
            next_supports.append(len(succ))
            contained = sum((A | z) == A for z in rectangles)
            diag_hist[contained] += 1
            check(sum(succ.values()) == len(rectangles), ("M05 mass", r, c, A))
        dist = Counter({0: 1})
        for _ in range(4):
            out = Counter()
            for A, mass in dist.items():
                for z in rectangles:
                    out[A | z] += mass
            dist = out
        check(sum(dist.values()) == len(rectangles) ** 4, ("M05 four mass", r, c))
        runs.append({"shape": [r, c], "states": 1 << bits,
                     "events": len(rectangles), "max_one_step_support": max(next_supports),
                     "diagonal_numerator_histogram": dict(sorted(diag_hist.items())),
                     "four_step_support_from_zero": len(dist)})
    return {"id": "M05", "name": "Boolean rectangle-OR growth",
            "runs": runs, "assertions": ASSERTIONS - before}


def cross_increment(i, j, n):
    ans = 0
    for c in range(n):
        ans ^= 1 << (i * n + c)
    for r in range(n):
        ans ^= 1 << (r * n + j)
    return ans


def candidate_m06():
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        bits = n * n
        inc = Counter(cross_increment(i, j, n) for i in range(n) for j in range(n))
        ft = walsh(inc, bits)
        check(sum(x * x for x in ft) == (1 << bits) * sum(v * v for v in inc.values()),
              ("M06 Parseval", n))
        runs.append({"n": n, "ambient_states": 1 << bits,
                     "increment_support": len(inc),
                     "span_dimension": span_rank(list(inc), bits),
                     "eigen_numerator_histogram": dict(sorted(Counter(ft).items()))})
    return {"id": "M06", "name": "binary row-column cross-toggle walk",
            "runs": runs, "assertions": ASSERTIONS - before}


def all_maps(n):
    return product(range(n), repeat=n)


def map_image_mask(f, A):
    ans = 0
    for i in range(len(f)):
        if (A >> i) & 1:
            ans |= 1 << f[i]
    return ans


def map_preimage_mask(f, A):
    return sum(1 << i for i, y in enumerate(f) if (A >> y) & 1)


def matrix_power(Q, t):
    n = len(Q)
    out = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    base = Q
    while t:
        if t & 1:
            out = [[sum(out[i][k] * base[k][j] for k in range(n))
                    for j in range(n)] for i in range(n)]
        base = [[sum(base[i][k] * base[k][j] for k in range(n))
                 for j in range(n)] for i in range(n)]
        t >>= 1
    return out


def rational_rank(matrix):
    A = [list(row) for row in matrix]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if A[i][col]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        value = A[rank][col]
        A[rank] = [x / value for x in A[rank]]
        for i in range(m):
            if i != rank and A[i][col]:
                value = A[i][col]
                A[i] = [x - value * y for x, y in zip(A[i], A[rank])]
        rank += 1
    return rank


def candidate_s01():
    runs = []
    before = ASSERTIONS
    for n in range(1, 8):
        Q = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
        for a in range(n + 1):
            for b in range(a + 1):
                count_one_target = 0
                marked = {}
                for r in range(0, min(n - a, a - b) + 1):
                    k = b + r
                    val = combinations_count(n - a, r) * factorial(k) * stirling2(a, k)
                    if val:
                        marked[k] = val
                        count_one_target += val
                Q[a][b] = Fraction(combinations_count(a, b) * count_one_target, n ** a if a else 1)
                check(sum(marked.values()) == count_one_target,
                      ("S01 marked", n, a, b))
            check(sum(Q[a]) == 1, ("S01 row", n, a, Q[a]))
        if n <= 4:
            maps = list(all_maps(n))
            for A in range(1 << n):
                a = A.bit_count()
                counter = Counter()
                marked_counter = Counter()
                for f in maps:
                    image = map_image_mask(f, A)
                    B = A & image
                    counter[B] += 1
                    marked_counter[(B, image.bit_count())] += 1
                extension = n ** (n - a)
                for B in range(1 << n):
                    if B & ~A:
                        check(counter[B] == 0, ("S01 support", n, A, B))
                        continue
                    b = B.bit_count()
                    expected = 0
                    for r in range(0, min(n - a, a - b) + 1):
                        k = b + r
                        val = combinations_count(n - a, r) * factorial(k) * stirling2(a, k)
                        expected += val
                        check(marked_counter[(B, k)] == extension * val,
                              ("S01 marked brute", n, A, B, k))
                    check(counter[B] == extension * expected,
                          ("S01 endpoint brute", n, A, B))
        power3 = matrix_power(Q, 3)
        resonance = None
        if n >= 2:
            lam = Q[n][n]
            check(lam == Q[n - 1][n - 1], ("S01 resonance", n, lam))
            check(Q[n][n - 1] > 0, ("S01 coupled resonance", n, Q[n][n - 1]))
            shifted = [[Q[i][j] - (lam if i == j else 0)
                        for j in range(n + 1)] for i in range(n + 1)]
            shifted2 = [[sum(shifted[i][k] * shifted[k][j] for k in range(n + 1))
                         for j in range(n + 1)] for i in range(n + 1)]
            nullity1 = n + 1 - rational_rank(shifted)
            nullity2 = n + 1 - rational_rank(shifted2)
            check((nullity1, nullity2) == (1, 2),
                  ("S01 Jordan", n, nullity1, nullity2))
            resonance = {"eigenvalue": str(lam), "jordan_block": 2,
                         "size_chain_nullities_N_N2": [nullity1, nullity2]}
        mean = "infinite (n=1 full state is fixed)" if n == 1 else str(
            absorption_mean(Q, n, {0}))
        runs.append({"n": n,
                     "diagonal": [str(Q[a][a] / combinations_count(a, a)) for a in range(n + 1)],
                     "three_step_absorption_full_start": str(power3[n][0]),
                     "full_start_mean_via_triangular_solve": mean,
                     "top_dimension_resonance": resonance})
    return {"id": "S01", "name": "fresh-map self-image erosion",
            "runs": runs, "assertions": ASSERTIONS - before}


def combinations_count(n, k):
    if k < 0 or k > n:
        return 0
    num = den = 1
    for i in range(1, k + 1):
        num *= n - k + i
        den *= i
    return num // den


def absorption_mean(Q, start, absorbing):
    # Lower-triangular chains used here only: solve increasing state index.
    E = [Fraction(0) for _ in Q]
    for a in range(len(Q)):
        if a in absorbing:
            continue
        rhs = Fraction(1) + sum(Q[a][b] * E[b] for b in range(a))
        E[a] = rhs / (1 - Q[a][a])
    return E[start]


def cycles_of_permutation(p):
    seen = set()
    c = 0
    for i in range(len(p)):
        if i not in seen:
            c += 1
            x = i
            while x not in seen:
                seen.add(x)
                x = p[x]
    return c


def candidate_s02():
    runs = []
    before = ASSERTIONS
    for n in range(1, 8):
        for a in range(n + 1):
            for b in range(a + 1):
                expected = combinations_count(n - a, a - b) * factorial(a) * factorial(n - a)
                if a - b > n - a:
                    expected = 0
                check(expected >= 0, ("S02 formula", n, a, b))
        if n <= 6:
            perms = list(permutations(range(n)))
            A = (1 << ((n + 1) // 2)) - 1
            a = A.bit_count()
            counter = Counter()
            cycle_mark = Counter()
            for p in perms:
                B = A & map_image_mask(p, A)
                counter[B] += 1
                cycle_mark[(B, cycles_of_permutation(p))] += 1
            for B in range(1 << n):
                if B & ~A:
                    check(counter[B] == 0, ("S02 support", n, B))
                    continue
                b = B.bit_count()
                expected = combinations_count(n - a, a - b) * factorial(a) * factorial(n - a)
                if a - b > n - a:
                    expected = 0
                check(counter[B] == expected, ("S02 endpoint", n, A, B))
                check(sum(v for (BB, _), v in cycle_mark.items() if BB == B) == expected,
                      ("S02 marked mass", n, B))
        runs.append({"n": n, "absorbing_sizes": [0, n],
                     "diagonal_per_exact_state": [str(Fraction(1, combinations_count(n, a)))
                                                  for a in range(n + 1)]})
    return {"id": "S02", "name": "fresh-permutation self-overlap erosion",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_s03():
    runs = []
    before = ASSERTIONS
    for n in range(1, 6):
        if n <= 4:
            maps = list(all_maps(n))
            for A in range(1 << n):
                a = A.bit_count()
                counter = Counter(map_preimage_mask(f, A) for f in maps)
                for B in range(1 << n):
                    b = B.bit_count()
                    expected = (a ** b) * ((n - a) ** (n - b))
                    check(counter[B] == expected, ("S03 Wright-Fisher", n, A, B))
        eigen = [Fraction(factorial(n), factorial(n-k) * (n ** k)) for k in range(n + 1)]
        runs.append({"n": n, "size_chain_eigenvalues": [str(x) for x in eigen],
                     "absorbing_sizes": [0, n]})
    return {"id": "S03", "name": "fresh-map inverse-image Wright-Fisher chain",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_s04():
    runs = []
    before = ASSERTIONS
    for n in range(1, 7):
        if n <= 4:
            maps = list(all_maps(n))
            for A in range(1 << n):
                a = A.bit_count()
                counter = Counter(map_image_mask(f, A) for f in maps)
                extension = n ** (n - a)
                for B in range(1 << n):
                    b = B.bit_count()
                    expected = extension * factorial(b) * stirling2(a, b)
                    check(counter[B] == expected, ("S04 occupancy", n, A, B))
        Q = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
        for a in range(n + 1):
            den = n ** a if a else 1
            for b in range(n + 1):
                Q[a][b] = Fraction(factorial(n), factorial(n-b)) * stirling2(a, b) / den
            check(sum(Q[a]) == 1, ("S04 row", n, a))
        runs.append({"n": n, "nonempty_recurrent_size": 1,
                     "size_diagonal": [str(Q[a][a]) for a in range(n + 1)]})
    return {"id": "S04", "name": "fresh-map subset-image occupancy chain",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_s05():
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        maps = list(all_maps(n))
        profiles = defaultdict(set)
        max_support = 0
        for A in range(1 << n):
            a = A.bit_count()
            counter = Counter()
            for f in maps:
                image = map_image_mask(f, A)
                preimage = map_preimage_mask(f, A)
                B = A & image & preimage
                counter[B] += 1
            max_support = max(max_support, len(counter))
            for B, count in counter.items():
                check((B & ~A) == 0, ("S05 support", n, A, B))
                profiles[(a, B.bit_count())].add(count)
        # Relabelling invariance forces a single exact count per (a,b).
        for key, vals in profiles.items():
            check(len(vals) == 1, ("S05 orbit invariance", n, key, vals))
        runs.append({"n": n, "states": 1 << n, "max_one_step_support": max_support,
                     "distinct_cardinality_kernel_entries": len(profiles)})
    return {"id": "S05", "name": "fresh-map mutual image/preimage core",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_s06():
    """Fresh-map two-sided image/preimage overlap, without current-set erosion."""
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        maps = list(all_maps(n))
        size_rows = {}
        profiles = defaultdict(set)
        max_support = 0
        for A in range(1 << n):
            a = A.bit_count()
            counter = Counter()
            for f in maps:
                B = map_image_mask(f, A) & map_preimage_mask(f, A)
                counter[B] += 1
            check(sum(counter.values()) == n ** n, ("S06 mass", n, A))
            max_support = max(max_support, len(counter))
            row = tuple(sum(value for B, value in counter.items() if B.bit_count() == b)
                        for b in range(n + 1))
            if a in size_rows:
                check(size_rows[a] == row, ("S06 size sufficiency", n, a, A))
            else:
                size_rows[a] = row
            for B, count in counter.items():
                profiles[(a, (A & B).bit_count(), B.bit_count())].add(count)
        check(all(len(values) == 1 for values in profiles.values()),
              ("S06 orbit kernel", n, profiles))
        Q = [[Fraction(value, n ** n) for value in size_rows[a]]
             for a in range(n + 1)]
        check(all(sum(row) == 1 for row in Q), ("S06 quotient rows", n, Q))
        power3 = matrix_power(Q, 3)
        runs.append({"n": n, "states": 1 << n,
                     "max_one_step_support": max_support,
                     "orbit_kernel_entries": len(profiles),
                     "size_diagonal": [str(Q[a][a]) for a in range(n + 1)],
                     "three_step_empty_probability_full_start": str(power3[n][0])})
    return {"id": "S06", "name": "fresh-map two-sided image/preimage overlap",
            "runs": runs, "assertions": ASSERTIONS - before}


def parity_image_mask(f, A):
    ans = 0
    for i in range(len(f)):
        if (A >> i) & 1:
            ans ^= 1 << f[i]
    return ans


def krawtchouk(n, b, k):
    return sum((-1) ** ell * combinations_count(b, ell)
               * combinations_count(n - b, k - ell)
               for ell in range(k + 1))


def parity_target_count(n, a, b):
    numerator = sum(krawtchouk(n, b, k) * (n - 2 * k) ** a
                    for k in range(n + 1))
    check(numerator % (1 << n) == 0, ("A01 Fourier integrality", n, a, b, numerator))
    return numerator // (1 << n)


def parity_onto_count(a, odd_boxes, positive_even_boxes):
    """Labelled-ball assignments with prescribed positive odd/even boxes."""
    dp = {0: 1}
    for odd in [True] * odd_boxes + [False] * positive_even_boxes:
        updated = defaultdict(int)
        for used, value in dp.items():
            start = 1 if odd else 2
            for take in range(start, a - used + 1, 2):
                updated[used + take] += value * combinations_count(a - used, take)
        dp = updated
    return dp.get(a, 0)


def candidate_a01():
    """Push a subset through a fresh random functional graph, modulo two."""
    runs = []
    before = ASSERTIONS
    for n in range(1, 6):
        fixed_counts = [[parity_target_count(n, a, b) for b in range(n + 1)]
                        for a in range(n + 1)]
        Q = [[Fraction(combinations_count(n, b) * fixed_counts[a][b],
                       n ** a if a else 1)
              for b in range(n + 1)] for a in range(n + 1)]
        for a in range(n + 1):
            check(sum(Q[a]) == 1, ("A01 quotient row", n, a, Q[a]))
            for b in range(n + 1):
                check((fixed_counts[a][b] == 0) == ((a - b) % 2 != 0 or b > a),
                      ("A01 parity support", n, a, b, fixed_counts[a][b]))
        check(Q[0][0] == Q[1][1] == 1, ("A01 recurrent sizes", n, Q))
        if n >= 2:
            check(all(Q[a][a] > Q[a + 1][a + 1] for a in range(1, n)),
                  ("A01 strict transient diagonal", n, Q))
        max_mark_width = 0
        if n <= 5:
            maps = list(all_maps(n))
            for A in range(1 << n):
                a = A.bit_count()
                counter = Counter()
                marked = Counter()
                for f in maps:
                    B = parity_image_mask(f, A)
                    occupied = len({f[i] for i in range(n) if (A >> i) & 1})
                    counter[B] += 1
                    marked[(B, occupied)] += 1
                extension = n ** (n - a)
                for B in range(1 << n):
                    b = B.bit_count()
                    expected = extension * fixed_counts[a][b]
                    check(counter[B] == expected, ("A01 endpoint", n, A, B, expected))
                    support = []
                    marked_mass = 0
                    for k in range(n + 1):
                        value = (combinations_count(n - b, k - b)
                                 * parity_onto_count(a, b, k - b))
                        check(marked[(B, k)] == extension * value,
                              ("A01 occupied mark", n, A, B, k, value))
                        marked_mass += value
                        if value:
                            support.append(k)
                    check(marked_mass == fixed_counts[a][b],
                          ("A01 marked mass", n, a, b, marked_mass))
                    max_mark_width = max(max_mark_width, len(support))
        power3 = matrix_power(Q, 3)
        terminal = n & 1
        runs.append({"n": n, "states": 1 << n,
                     "one_step_size_diagonal": [str(Q[a][a]) for a in range(n + 1)],
                     "three_step_terminal_probability_full_start": str(power3[n][terminal]),
                     "full_start_mean_to_parity_terminal": str(
                         absorption_mean(Q, n, {0, 1})),
                     "max_occupied_mark_support_width": max_mark_width})
    return {"id": "A01", "name": "fresh-map parity pushforward kernel",
            "runs": runs, "assertions": ASSERTIONS - before}


def set_partitions(n):
    if n == 0:
        return [tuple()]
    out = []

    def rec(word, maximum):
        if len(word) == n:
            out.append(tuple(word))
            return
        for x in range(maximum + 2):
            rec(word + [x], max(maximum, x))

    rec([0], 0)
    return out


def canonical_labels(items):
    names = {}
    return tuple(names.setdefault(x, len(names)) for x in items)


def partition_meet_coloring(pi, coloring):
    return canonical_labels(tuple(zip(pi, coloring)))


def refines(sigma, pi):
    return all(sigma[i] != sigma[j] or pi[i] == pi[j]
               for i in range(len(pi)) for j in range(len(pi)))


def falling(x, k):
    ans = 1
    for i in range(k):
        ans *= x - i
    return ans


def child_counts(sigma, pi):
    blocks = defaultdict(set)
    for p, s in zip(pi, sigma):
        blocks[p].add(s)
    return sorted(len(v) for v in blocks.values())


def marked_hash_count(Q, child_profile, r):
    onto = 0
    for j in range(r + 1):
        onto += (-1) ** j * combinations_count(r, j) * product_int(
            falling(r - j, c) for c in child_profile)
    return combinations_count(Q, r) * onto


def product_int(values):
    ans = 1
    for value in values:
        ans *= value
    return ans


def candidate_h01():
    runs = []
    before = ASSERTIONS
    for q, nmax, tmax in [(2, 5, 3), (3, 4, 2)]:
        for n in range(0, nmax + 1):
            parts = set_partitions(n)
            check(len(parts) == bell(n), ("H01 Bell census", q, n))
            max_mark_width = 0
            for t in range(1, tmax + 1):
                Q = q ** t
                assignments = list(product(range(Q), repeat=n))
                for pi in parts:
                    counter = Counter(partition_meet_coloring(pi, z) for z in assignments)
                    marked = Counter((partition_meet_coloring(pi, z), len(set(z)))
                                     for z in assignments)
                    check(sum(counter.values()) == Q ** n, ("H01 mass", q, n, t, pi))
                    for sigma in parts:
                        if not refines(sigma, pi):
                            check(counter[sigma] == 0, ("H01 support", q, n, t, pi, sigma))
                            continue
                        profile = child_counts(sigma, pi)
                        expected = product_int(falling(Q, c) for c in profile)
                        check(counter[sigma] == expected,
                              ("H01 endpoint", q, n, t, pi, sigma, profile))
                        marked_total = 0
                        support = []
                        for r in range(Q + 1):
                            value = marked_hash_count(Q, profile, r)
                            check(marked[(sigma, r)] == value,
                                  ("H01 marked", q, n, t, pi, sigma, r))
                            marked_total += value
                            if value:
                                support.append(r)
                        check(marked_total == expected, ("H01 marked mass", q, n, t, pi, sigma))
                        if support:
                            lower = max(profile) if profile else 0
                            expected_support = list(range(lower, min(sum(profile), Q) + 1))
                            check(support == expected_support,
                                  ("H01 marked support", q, n, t, profile, support))
                            max_mark_width = max(max_mark_width, len(support))
            pi_one_block = (0,) * n
            Q = q ** tmax
            absorption_num = falling(Q, n)
            runs.append({"q": q, "n": n, "partitions": len(parts),
                         "one_block_absorption_cdf_at_tmax": str(Fraction(
                             absorption_num, Q ** n if n else 1)),
                         "one_step_eigenvalues_by_block_count": [str(Fraction(
                             q ** k, q ** n if n else 1)) for k in range(n + 1)],
                         "max_marked_support_width": max_mark_width})
    return {"id": "H01", "name": "random hash-refinement chain on set partitions",
            "runs": runs, "assertions": ASSERTIONS - before}


def lse_restricted_count(n, a, b, q=2):
    terms = {}
    total = 0
    for r in range(b, min(a, n - a + b) + 1):
        val = (q ** ((a - b) * (r - b)) * gaussian(n - a, r - b, q)
               * onto_linear(a, r, q))
        if val:
            terms[r] = val
            total += val
    return total, terms


def candidate_g01():
    runs = []
    before = ASSERTIONS
    for q, nmax in [(2, 6), (3, 5), (5, 5)]:
        for n in range(1, nmax + 1):
            Q = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
            for a in range(n + 1):
                for b in range(a + 1):
                    count, terms = lse_restricted_count(n, a, b, q)
                    check(sum(terms.values()) == count, ("G01 marked", q, n, a, b))
                    Q[a][b] = Fraction(gaussian(a, b, q) * count, q ** (n * a))
                check(sum(Q[a]) == 1, ("G01 row", q, n, a, Q[a]))
            diagonals = [Fraction(onto_linear(a, a, q), q ** (n * a))
                         for a in range(n + 1)]
            check(len(set(diagonals)) == n + 1, ("G01 distinct spectrum", q, n, diagonals))
            check(max(diagonals[1:]) == diagonals[n], ("G01 top transient", q, n, diagonals))
            if q == 2 and n <= 3:
                subs = enumerate_subspaces(n)
                matrices = range(1 << (n * n))
                for U in subs:
                    a = subspace_dim(U)
                    counter = Counter()
                    marked = Counter()
                    for T in matrices:
                        W = frozenset(apply_linear(T, x, n) for x in U)
                        B = U & W
                        counter[B] += 1
                        marked[(B, subspace_dim(W))] += 1
                    extension = 2 ** (n * (n - a))
                    for B in subs:
                        if not B <= U:
                            check(counter[B] == 0, ("G01 support", n, U, B))
                            continue
                        b = subspace_dim(B)
                        expected, terms = lse_restricted_count(n, a, b, 2)
                        check(counter[B] == extension * expected,
                              ("G01 endpoint", n, a, b, U, B))
                        for r, val in terms.items():
                            check(marked[(B, r)] == extension * val,
                                  ("G01 rank mark", n, a, b, r))
            p4 = matrix_power(Q, 4)
            runs.append({"q": q, "n": n,
                         "subspace_states": sum(gaussian(n, a, q) for a in range(n + 1)),
                         "diagonal_per_exact_subspace": [str(x) for x in diagonals],
                         "four_step_absorption_full_start": str(p4[n][0]),
                         "full_start_mean": str(absorption_mean(Q, n, {0}))})
    return {"id": "G01", "name": "random-linear self-image erosion",
            "runs": runs, "assertions": ASSERTIONS - before}


def linear_leak_kernel_count(n, a, b, q=2):
    """Maps U -> V/U having one prescribed b-space as their kernel."""
    d = a - b
    return onto_linear(n - a, d, q) if 0 <= d <= n - a else 0


def candidate_g05():
    """Fresh T, with U replaced by U intersect T^{-1}(U).

    The update is the kernel of the uniformly random quotient-leakage map
    U -> V/U.  This lane was added after three entry-firewall controls were
    identified as literal historical duplicates.
    """
    runs = []
    before = ASSERTIONS
    for q, nmax in [(2, 8), (3, 7), (5, 7)]:
        for n in range(1, nmax + 1):
            Q = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
            for a in range(n + 1):
                den = q ** (a * (n - a))
                for b in range(a + 1):
                    Q[a][b] = Fraction(gaussian(a, b, q)
                                       * linear_leak_kernel_count(n, a, b, q), den)
                check(sum(Q[a]) == 1, ("G05 row", q, n, a, Q[a]))
            diagonals = [Q[a][a] for a in range(n + 1)]
            check(all(diagonals[a] == diagonals[n - a] for a in range(n + 1)),
                  ("G05 complementary spectrum", q, n, diagonals))
            paired_jordan = []
            for a in range((n // 2) + 1, n):
                b = n - a
                lam = diagonals[a]
                shifted = [[Q[i][j] - (lam if i == j else 0)
                            for j in range(n + 1)] for i in range(n + 1)]
                shifted2 = [[sum(shifted[i][k] * shifted[k][j]
                                 for k in range(n + 1))
                             for j in range(n + 1)] for i in range(n + 1)]
                nullity1 = n + 1 - rational_rank(shifted)
                nullity2 = n + 1 - rational_rank(shifted2)
                check((nullity1, nullity2) == (1, 2),
                      ("G05 paired Jordan", q, n, a, b, nullity1, nullity2))
                paired_jordan.append({"dimensions": [a, b],
                                      "eigenvalue": str(lam),
                                      "size_chain_nullities_N_N2": [nullity1, nullity2]})
            one_shifted = [[Q[i][j] - (1 if i == j else 0)
                            for j in range(n + 1)] for i in range(n + 1)]
            check(n + 1 - rational_rank(one_shifted) == 2,
                  ("G05 two absorbing eigenspaces", q, n))
            if q == 2 and n <= 3:
                subs = enumerate_subspaces(n)
                for U in subs:
                    a = subspace_dim(U)
                    counter = Counter()
                    for T in range(1 << (n * n)):
                        B = frozenset(x for x in U if apply_linear(T, x, n) in U)
                        counter[B] += 1
                    extension = 2 ** (n * n - a * (n - a))
                    for B in subs:
                        if not B <= U:
                            check(counter[B] == 0, ("G05 support", n, U, B))
                            continue
                        b = subspace_dim(B)
                        expected = extension * linear_leak_kernel_count(n, a, b, 2)
                        check(counter[B] == expected,
                              ("G05 endpoint", n, a, b, U, B))
            power4 = matrix_power(Q, 4)
            start = max(0, n - 1)
            runs.append({"q": q, "n": n,
                         "diagonal_per_exact_subspace": [str(x) for x in diagonals],
                         "paired_jordan_blocks_in_size_chain": paired_jordan,
                         "four_step_zero_absorption_from_hyperplane": str(power4[start][0]),
                         "hyperplane_start_mean": str(absorption_mean(Q, start, {0, n}))})
    return {"id": "G05", "name": "random-linear quotient-leakage erosion",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_g02():
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        subs = enumerate_subspaces(n)
        if n <= 3:
            matrices = range(1 << (n * n))
            for U in subs:
                a = subspace_dim(U)
                counter = Counter()
                for T in matrices:
                    W = frozenset(apply_linear(T, x, n) for x in U)
                    counter[W] += 1
                extension = 2 ** (n * (n - a))
                for W in subs:
                    b = subspace_dim(W)
                    expected = extension * onto_linear(a, b, 2)
                    check(counter[W] == expected, ("G02 endpoint", n, a, b))
        runs.append({"n": n, "subspace_states": len(subs),
                     "rank_retention_probability": [str(Fraction(
                         gaussian(n, a, 2) * onto_linear(a, a, 2), 2 ** (n * a)))
                         for a in range(n + 1)]})
    return {"id": "G02", "name": "fresh random-linear image chain",
            "runs": runs, "assertions": ASSERTIONS - before}


def functional_value(ell, x):
    return parity(ell & x)


def candidate_g03():
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        subs = enumerate_subspaces(n)
        for U in subs:
            a = subspace_dim(U)
            for t in range(1, n + 3):
                if n > 3:
                    total = 0
                    for b in range(a + 1):
                        d = a - b
                        expected = 1
                        for i in range(d):
                            expected *= 2 ** t - 2 ** i
                        expected *= 2 ** ((n - a) * t)
                        total += gaussian(a, b, 2) * expected
                    check(total == 2 ** (n * t), ("G03 formula mass", n, a, t))
                    continue
                counter = Counter()
                for history in product(range(1 << n), repeat=t):
                    B = frozenset(x for x in U if all(functional_value(e, x) == 0
                                                       for e in history))
                    counter[B] += 1
                for B in subs:
                    if not B <= U:
                        check(counter[B] == 0, ("G03 support", n, U, B))
                        continue
                    d = a - subspace_dim(B)
                    expected = 1
                    for i in range(d):
                        expected *= 2 ** t - 2 ** i
                    expected *= 2 ** ((n - a) * t)
                    check(counter[B] == expected, ("G03 endpoint", n, a, d, t))
        runs.append({"n": n, "subspace_states": len(subs),
                     "sharp_maximum_codimension_after_t": "min(t,a)",
                     "full_rank_history_count_t=n": str(onto_linear(n, n, 2))})
    return {"id": "G03", "name": "random hyperplane-cut chain",
            "runs": runs, "assertions": ASSERTIONS - before}


def affine_subspaces(n):
    subs = enumerate_subspaces(n)
    seen = set()
    out = []
    for U in subs:
        for x in range(1 << n):
            A = frozenset(x ^ u for u in U)
            if A not in seen:
                seen.add(A)
                out.append(A)
    return sorted(out, key=lambda A: (len(A), tuple(sorted(A))))


def candidate_g04():
    runs = []
    before = ASSERTIONS
    for n in range(1, 4):
        aff = affine_subspaces(n)
        maps = [(T, b) for T in range(1 << (n * n)) for b in range(1 << n)]
        for A in aff:
            a = len(A).bit_length() - 1
            counter = Counter()
            for T, shift in maps:
                W = frozenset(apply_linear(T, x, n) ^ shift for x in A)
                counter[W] += 1
            extension = 2 ** (n * (n - a))
            for W in aff:
                r = len(W).bit_length() - 1
                expected = extension * (2 ** r) * onto_linear(a, r, 2)
                check(counter[W] == expected, ("G04 endpoint", n, a, r, A, W))
        runs.append({"n": n, "affine_subspace_states": len(aff),
                     "recurrent_class": f"{2 ** n} points",
                     "dimension_retention": [str(Fraction(
                         gaussian(n, a, 2) * (2 ** a) * onto_linear(a, a, 2),
                         2 ** (n * (a + 1)))) for a in range(n + 1)]})
    return {"id": "G04", "name": "fresh random-affine image chain",
            "runs": runs, "assertions": ASSERTIONS - before}


def row_inclusion_map(A, n):
    rows = matrix_rows(A, n, n)
    out = 0
    for i in range(n):
        for j in range(n):
            if rows[i] & ~rows[j] == 0:
                out |= 1 << (i * n + j)
    return out


def is_preorder(A, n):
    rows = matrix_rows(A, n, n)
    if any(not ((rows[i] >> i) & 1) for i in range(n)):
        return False
    return all(not ((rows[i] >> j) & 1) or (rows[i] | rows[j]) == rows[i]
               for i in range(n) for j in range(n))


def transpose_matrix(A, n):
    return sum(((A >> (i * n + j)) & 1) << (j * n + i)
               for i in range(n) for j in range(n))


def candidate_r01():
    runs = []
    before = ASSERTIONS
    for n in range(1, 5):
        nexts = []
        preorders = 0
        for A in range(1 << (n * n)):
            P = row_inclusion_map(A, n)
            check(is_preorder(P, n), ("R01 output preorder", n, A, P))
            if is_preorder(A, n):
                preorders += 1
                check(P == transpose_matrix(A, n), ("R01 transpose", n, A, P))
            nexts.append(P)
        stats = functional_stats(nexts)
        check(stats["image"] == preorders, ("R01 image census", n, stats, preorders))
        runs.append({"n": n, "preorders": preorders, **stats})
    return {"id": "R01", "name": "row-inclusion residuation dynamics",
            "runs": runs, "assertions": ASSERTIONS - before}


def row_disjoint_map(A, n):
    rows = matrix_rows(A, n, n)
    return sum((not (rows[i] & rows[j])) << (i * n + j)
               for i in range(n) for j in range(n))


def candidate_r02():
    runs = []
    before = ASSERTIONS
    for n in range(1, 4):
        nexts = [row_disjoint_map(A, n) for A in range(1 << (n * n))]
        check(all(transpose_matrix(B, n) == B for B in nexts), ("R02 symmetric image", n))
        runs.append({"n": n, **functional_stats(nexts)})
    return {"id": "R02", "name": "row-disjointness feedback",
            "runs": runs, "assertions": ASSERTIONS - before}


def schur_square(U):
    return span_vectors(x & y for x in U for y in U)


def bell(n):
    return sum(stirling2(n, k) for k in range(n + 1))


def candidate_c01():
    runs = []
    before = ASSERTIONS
    for n in range(1, 8):
        one = (1 << n) - 1
        subs = [U for U in enumerate_subspaces_rref(n) if one in U]
        index = {U: i for i, U in enumerate(subs)}
        nexts = []
        for U in subs:
            V = schur_square(U)
            check(U <= V, ("C01 monotone", n, U, V))
            check(V in index, ("C01 closed carrier", n, U, V))
            nexts.append(index[V])
        stats = functional_stats(nexts)
        check(stats["fixed"] == bell(n), ("C01 Bell fixed", n, stats, bell(n)))
        check(stats["periods"] == [1], ("C01 fixed recurrence", n, stats))
        runs.append({"n": n, "unital_codes": len(subs), **stats})
    # The small complete census n <= 7 happens to see only one-step closure.
    # RM(1,3) supplies the first compact warning against extrapolating that
    # bounded observation: dimensions 4 -> 7 -> 8 under Schur squaring.
    n = 8
    coordinate_words = [sum(((x >> j) & 1) << x for x in range(n))
                        for j in range(3)]
    U = span_vectors([(1 << n) - 1, *coordinate_words])
    V = schur_square(U)
    W = schur_square(V)
    check((subspace_dim(U), subspace_dim(V), subspace_dim(W)) == (4, 7, 8),
          ("C01 Reed--Muller witness", tuple(map(subspace_dim, (U, V, W)))))
    check(V != W and schur_square(W) == W, "C01 Reed--Muller tail two")
    runs.append({"n": 8, "control": "RM(1,3)",
                 "dimension_orbit": [4, 7, 8, 8], "tail": 2})
    return {"id": "C01", "name": "unital binary Schur-square code dynamics",
            "runs": runs, "assertions": ASSERTIONS - before}


def candidate_c02():
    runs = []
    before = ASSERTIONS
    for n in range(1, 4):
        nexts = [matmul_transpose_gf2(A, n) for A in range(1 << (n * n))]
        # Output is symmetric over F_2.
        check(all(transpose_matrix(B, n) == B for B in nexts), ("C02 symmetric", n))
        runs.append({"n": n, **functional_stats(nexts)})
    return {"id": "C02", "name": "field-Gram feedback A -> A A^T over F2",
            "runs": runs, "assertions": ASSERTIONS - before}


def main():
    candidates = [
        candidate_m01(), candidate_m02(), candidate_m03(), candidate_m04(),
        candidate_m05(), candidate_m06(), candidate_s01(), candidate_s02(),
        candidate_s03(), candidate_s04(), candidate_s05(), candidate_s06(), candidate_a01(),
        candidate_h01(), candidate_g01(),
        candidate_g05(), candidate_g02(), candidate_g03(), candidate_g04(), candidate_r01(),
        candidate_r02(), candidate_c01(), candidate_c02(),
    ]
    check(len(candidates) == 23, ("candidate count", len(candidates)))
    check(len({x["id"] for x in candidates}) == 23, "duplicate handles")
    check(all(x["assertions"] > 0 for x in candidates), "empty audit")
    payload = {
        "schema": "p172-p176-stochastic-matrix-breadth-v1",
        "candidate_count": len(candidates),
        "candidates": candidates,
        "assertions": ASSERTIONS,
        "external_status": "HOLD_EXTERNAL",
        "interpretation": "finite exact falsification evidence; not proof or novelty",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
