#!/usr/bin/env python3
"""Independent exact pilots for the P197--P201 replacement algebra lane.

Standard library only.  The script deliberately includes negative controls:
the strongest-looking sign-Laplacian candidate is checked against the exact
TCSD factor identity before any of its attractive census is credited.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import math
from collections import Counter


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def sgn(value: int) -> int:
    return (value > 0) - (value < 0)


def orbit_data(states, step):
    next_state = {x: step(x) for x in states}
    indegree = Counter(next_state.values())
    histogram = Counter()
    recurrent = 0
    for start in states:
        seen = {}
        x = start
        time = 0
        while x not in seen:
            seen[x] = time
            x = next_state[x]
            time += 1
        tail = seen[x]
        period = time - tail
        histogram[(tail, period)] += 1
        recurrent += tail == 0
    return next_state, indegree, histogram, recurrent


def left_shift(word):
    return word[1:] + word[:1]


def tcsd(word):
    n = len(word)
    return tuple(sgn(word[(i + 1) % n] - word[i]) for i in range(n))


def sign_laplacian(word):
    n = len(word)
    return tuple(
        sgn(word[i - 1] + word[(i + 1) % n] - 2 * word[i])
        for i in range(n)
    )


def audit_csl_factor():
    rows = []
    for n in range(1, 9):
        states = list(itertools.product((-1, 0, 1), repeat=n))
        for x in states:
            check(tcsd(tcsd(x)) == left_shift(sign_laplacian(x)), f"CSL factor n={n}")
        _, indegree, histogram, recurrent = orbit_data(states, sign_laplacian)
        check({p for (_, p) in histogram} <= {1, 2}, f"CSL periods n={n}")
        rows.append((n, len(states), max(t for (t, _) in histogram), recurrent, max(indegree.values())))
    return rows


def unique_sum_support(mask: int, n: int) -> int:
    counts = [0] * n
    for a in range(n):
        if (mask >> a) & 1:
            for b in range(n):
                if (mask >> b) & 1:
                    counts[(a + b) % n] += 1
    return sum((count == 1) << z for z, count in enumerate(counts))


def dilate(mask: int, multiplier: int, n: int) -> int:
    return sum(1 << ((multiplier * a) % n) for a in range(n) if (mask >> a) & 1)


def progression_free(mask: int, n: int) -> bool:
    inv2 = pow(2, -1, n)
    points = [a for a in range(n) if (mask >> a) & 1]
    point_set = set(points)
    for index, a in enumerate(points):
        for b in points[index + 1 :]:
            if ((a + b) * inv2) % n in point_set:
                return False
    return True


def audit_unique_sum():
    rows = []
    for n in (3, 5, 7, 9, 11, 13):
        states = list(range(1 << n))
        images = Counter()
        cap_count = 0
        for mask in states:
            image = unique_sum_support(mask, n)
            images[image] += 1
            check(unique_sum_support(image, n) == dilate(image, 2, n), f"U2S action n={n}")
            check(progression_free(image, n), f"U2S image cap n={n}")
            cap_count += progression_free(mask, n)
        check(len(images) == cap_count, f"U2S image equality n={n}")
        check(max(images.values()) == images[0], f"U2S zero maximum n={n}")
        rows.append((n, len(states), len(images), images[0], max(images.values())))
    return rows


def zqd_step(word, m):
    n = len(word)
    out = []
    for i, left in enumerate(word):
        right = word[(i + 1) % n]
        if left == 0 or right == 0:
            out.append(0)
        else:
            out.append(((right - left) % m) + 1)
    return tuple(out)


def unit_run(word):
    bits = tuple(value != 0 for value in word)
    n = len(bits)
    if all(bits):
        return n
    if not any(bits):
        return 0
    return max(
        next((length for length in range(1, n + 1) if not bits[(start + length) % n]), n)
        for start in range(n)
        if bits[start]
    )


def support_mask(word):
    return sum((value != 0) << i for i, value in enumerate(word))


def one_runs(mask: int, n: int) -> int:
    if mask == 0:
        return 0
    if mask == (1 << n) - 1:
        return 1
    return sum(((mask >> i) & 1) and not ((mask >> (i - 1)) & 1) for i in range(n))


def support_fibre(target, m):
    n = len(target)
    target_support = support_mask(target)
    full = (1 << n) - 1
    if target_support == full:
        exponent_sum = sum(value - 1 for value in target) % m
        return m if exponent_sum == 0 else 0
    total = 0
    for source_support in range(1 << n):
        image_support = 0
        for i in range(n):
            if ((source_support >> i) & 1) and ((source_support >> ((i + 1) % n)) & 1):
                image_support |= 1 << i
        if image_support == target_support:
            total += m ** one_runs(source_support, n)
    return total


def weighted_cycle_independent_sets(n, m):
    if n == 1:
        return 1
    return sum(
        (n * math.comb(n - k, k) // (n - k)) * (m**k)
        for k in range(n // 2 + 1)
    )


def audit_zqd():
    rows = []
    boxes = ((2, 3), (2, 5), (2, 7), (3, 2), (3, 4), (3, 5), (3, 7), (4, 3), (4, 5))
    for m, n in boxes:
        check(math.gcd(m, n) == 1, "ZQD registered coprime box")
        states = list(itertools.product(range(m + 1), repeat=n))
        step = lambda x, modulus=m: zqd_step(x, modulus)
        next_state, indegree, histogram, recurrent = orbit_data(states, step)
        full = (1 << n) - 1
        expected_recurrent = 1 + m ** (n - 1)
        check(recurrent == expected_recurrent, f"ZQD recurrent n={n},m={m}")
        check(histogram[(0, 1)] == 1 + math.gcd(m, 2**n - 1), f"ZQD fixed n={n},m={m}")
        for x in states:
            tail = None
            seen = {}
            y = x
            time = 0
            while y not in seen:
                seen[y] = time
                y = next_state[y]
                time += 1
            tail = seen[y]
            support = support_mask(x)
            if support == 0:
                expected_tail = 0
            elif support != full:
                expected_tail = unit_run(x)
            else:
                expected_tail = 0 if sum(value - 1 for value in x) % m == 0 else 1
            check(tail == expected_tail, f"ZQD point clock n={n},m={m}")
        for target, count in indegree.items():
            check(count == support_fibre(target, m), f"ZQD fibre n={n},m={m}")
        zero = (0,) * n
        check(indegree[zero] == weighted_cycle_independent_sets(n, m), f"ZQD Lucas n={n},m={m}")
        check(indegree[zero] == max(indegree.values()), f"ZQD max fibre n={n},m={m}")
        rows.append((m, n, len(states), max(t for (t, _) in histogram), recurrent, histogram[(0, 1)], indegree[zero]))
    return rows


def floor_reciprocal(x, N):
    return N // x


def audit_floor_reciprocal():
    rows = []
    for N in range(1, 201):
        states = list(range(1, N + 1))
        step = lambda x, bound=N: floor_reciprocal(x, bound)
        next_state, indegree, histogram, recurrent = orbit_data(states, step)
        for x in states:
            check(step(step(step(x))) == step(x), f"FRP polarity N={N}")
        k = math.isqrt(N)
        fixed = int(N < k * (k + 1))
        image_size = 2 * k - fixed
        check(recurrent == image_size, f"FRP image N={N}")
        check(histogram[(0, 1)] == fixed, f"FRP fixed N={N}")
        for y in states:
            expected = N // y - N // (y + 1)
            check(indegree[y] == expected, f"FRP fibre N={N},y={y}")
        if N in (1, 2, 5, 10, 25, 50, 100, 200):
            rows.append((N, image_size, fixed, max(t for (t, _) in histogram), max(indegree.values())))
    return rows


def projective_exact_one(rank):
    points = list(range(1, 1 << rank))
    rows = [[((u & v).bit_count() % 2) == 0 for u in points] for v in points]

    def step(mask):
        out = 0
        for i, row in enumerate(rows):
            if sum(flag and ((mask >> j) & 1) for j, flag in enumerate(row)) == 1:
                out |= 1 << i
        return out

    return points, step


def audit_exact_one_incidence():
    rows = []
    for rank in (2, 3, 4):
        points, step = projective_exact_one(rank)
        states = list(range(1 << len(points)))
        _, indegree, histogram, recurrent = orbit_data(states, step)
        rows.append((rank, len(points), len(states), len(indegree), max(t for (t, _) in histogram), tuple(sorted({p for (_, p) in histogram})), recurrent, max(indegree.values())))
    return rows


def exterior_pair_parity(mask, size):
    points = [x for x in range(size) if (mask >> x) & 1]
    out = 0
    for i, x in enumerate(points):
        for y in points[i + 1 :]:
            out ^= 1 << (x ^ y)
    return out


def audit_exterior_pair_parity():
    rows = []
    for rank in (1, 2, 3, 4):
        size = 1 << rank
        states = list(range(1 << size))
        step = lambda mask, order=size: exterior_pair_parity(mask, order)
        _, indegree, histogram, recurrent = orbit_data(states, step)
        rows.append((rank, size, len(states), len(indegree), max(t for (t, _) in histogram), tuple(sorted({p for (_, p) in histogram})), recurrent, max(indegree.values())))
    return rows


def graph_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def unique_triangle_step(mask, n):
    edges = graph_edges(n)
    index = {edge: i for i, edge in enumerate(edges)}
    out = 0
    for edge_index, (u, v) in enumerate(edges):
        common = 0
        for w in range(n):
            if w in (u, v):
                continue
            uw = index[tuple(sorted((u, w)))]
            vw = index[tuple(sorted((v, w)))]
            common += ((mask >> uw) & 1) and ((mask >> vw) & 1)
        if common == 1:
            out |= 1 << edge_index
    return out


def audit_unique_triangle():
    rows = []
    for n in range(2, 7):
        states = list(range(1 << len(graph_edges(n))))
        step = lambda mask, order=n: unique_triangle_step(mask, order)
        _, indegree, histogram, recurrent = orbit_data(states, step)
        rows.append((n, len(states), len(indegree), max(t for (t, _) in histogram), tuple(sorted({p for (_, p) in histogram})), recurrent, max(indegree.values())))
    return rows


def binary_subspaces(d):
    spaces = set()
    for k in range(d + 1):
        for pivots in itertools.combinations(range(d), k):
            free = [(row, col) for row, pivot in enumerate(pivots) for col in range(pivot + 1, d) if col not in pivots]
            for values in itertools.product((0, 1), repeat=len(free)):
                basis = [1 << pivot for pivot in pivots]
                for value, (row, col) in zip(values, free):
                    if value:
                        basis[row] |= 1 << col
                space = {0}
                for vector in basis:
                    space |= {x ^ vector for x in tuple(space)}
                spaces.add(frozenset(space))
    return sorted(spaces, key=lambda space: (len(space), tuple(space)))


def dual_even_step(space, d):
    dual = frozenset(
        x for x in range(1 << d)
        if all((x & y).bit_count() % 2 == 0 for y in space)
    )
    all_one = (1 << d) - 1
    return frozenset(set(dual) | {x ^ all_one for x in dual})


def audit_dual_even_codes():
    rows = []
    for d in range(1, 7):
        states = binary_subspaces(d)
        step = lambda space, dimension=d: dual_even_step(space, dimension)
        _, indegree, histogram, recurrent = orbit_data(states, step)
        rows.append((d, len(states), len(indegree), max(t for (t, _) in histogram), tuple(sorted({p for (_, p) in histogram})), recurrent, max(indegree.values())))
    return rows


def path_matchings(n):
    result = []

    def visit(vertex, mask):
        if vertex >= n:
            result.append(mask)
            return
        visit(vertex + 1, mask)
        if vertex + 1 < n:
            visit(vertex + 2, mask | (1 << vertex))

    visit(0, 0)
    return result


def isolated_plaquette_step(mask, n):
    if n < 2:
        return mask

    def flippable(edge):
        if (mask >> edge) & 1:
            return True
        left_busy = edge > 0 and ((mask >> (edge - 1)) & 1)
        right_busy = edge + 1 < n - 1 and ((mask >> (edge + 1)) & 1)
        return not left_busy and not right_busy

    flags = [flippable(edge) for edge in range(n - 1)]
    active = [
        flags[edge]
        and (edge == 0 or not flags[edge - 1])
        and (edge == n - 2 or not flags[edge + 1])
        for edge in range(n - 1)
    ]
    out = mask
    for edge, flag in enumerate(active):
        if flag:
            out ^= 1 << edge
    return out


def audit_isolated_plaquettes():
    rows = []
    for n in range(1, 21):
        states = path_matchings(n)
        step = lambda mask, width=n: isolated_plaquette_step(mask, width)
        _, indegree, histogram, recurrent = orbit_data(states, step)
        check(max(t for (t, _) in histogram) == (n - 1) // 2, f"IPF clock n={n}")
        if n in (1, 2, 3, 4, 8, 12, 16, 20):
            rows.append((n, len(states), max(t for (t, _) in histogram), tuple(sorted({p for (_, p) in histogram})), recurrent, max(indegree.values())))
    return rows


def digest(rows):
    return hashlib.sha256(repr(rows).encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="retained for a stable command line; all registered boxes are already cheap")
    parser.parse_args()

    results = {
        "CSL_EXACT_FACTOR": audit_csl_factor(),
        "U2S": audit_unique_sum(),
        "ZQD": audit_zqd(),
        "FRP": audit_floor_reciprocal(),
        "EOI": audit_exact_one_incidence(),
        "EPP": audit_exterior_pair_parity(),
        "UTE": audit_unique_triangle(),
        "DEC": audit_dual_even_codes(),
        "IPF": audit_isolated_plaquettes(),
    }
    print("P197-P201 REPLACEMENT ALGEBRA LANE")
    for name, rows in results.items():
        print(f"{name}: {rows}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"RESULT_SHA256={digest(results)}")
    print("VERDICT=NO_PROMOTION_FROM_THIS_LANE; THEOREM_CONTROLS_ZQD_FRP; HOLD_EXTERNAL")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
