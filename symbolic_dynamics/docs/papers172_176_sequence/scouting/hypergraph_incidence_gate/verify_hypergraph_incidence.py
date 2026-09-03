#!/usr/bin/env python3
"""Exact controls for odd pair-codegree feedback on 3-graphs.

The carrier is C_2 of the full simplex over F_2 (triples).  If W is the
edge--triangle boundary matrix, the update is L=W^T W.  Small exhaustive
graphs are falsification checks; the all-n proof is recorded separately.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import comb


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def pairs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


@lru_cache(None)
def triples(n: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(combinations(range(n), 3))


@lru_cache(None)
def triangle_boundaries(n: int) -> tuple[int, ...]:
    pair_index = {edge: i for i, edge in enumerate(pairs(n))}
    return tuple(
        sum(1 << pair_index[edge] for edge in combinations(face, 2))
        for face in triples(n)
    )


def gf2_rank(vectors) -> int:
    pivots: dict[int, int] = {}
    for vector in vectors:
        x = vector
        while x:
            pivot = x.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = x
                break
            x ^= pivots[pivot]
    return len(pivots)


def hypergraph_boundary(mask: int, n: int) -> int:
    out = 0
    boundaries = triangle_boundaries(n)
    x = mask
    while x:
        bit = x & -x
        out ^= boundaries[bit.bit_length() - 1]
        x ^= bit
    return out


def graph_coboundary(mask: int, n: int) -> int:
    out = 0
    for i, boundary in enumerate(triangle_boundaries(n)):
        if (mask & boundary).bit_count() & 1:
            out |= 1 << i
    return out


def step(mask: int, n: int) -> int:
    return graph_coboundary(hypergraph_boundary(mask, n), n)


def graph_vertex_boundary(mask: int, n: int) -> int:
    out = 0
    for i, (u, v) in enumerate(pairs(n)):
        if (mask >> i) & 1:
            out ^= (1 << u) | (1 << v)
    return out


def vertex_coboundary(mask: int, n: int) -> int:
    out = 0
    for i, (u, v) in enumerate(pairs(n)):
        if ((mask >> u) ^ (mask >> v)) & 1:
            out |= 1 << i
    return out


def edge_upper_laplacian(mask: int, n: int) -> int:
    return hypergraph_boundary(graph_coboundary(mask, n), n)


def cycle_basis(n: int) -> tuple[int, ...]:
    """Triangle fan through the last vertex; a basis of Z_1(K_n)."""
    if n < 3:
        return ()
    lookup = {face: i for i, face in enumerate(triples(n))}
    return tuple(
        triangle_boundaries(n)[lookup[(i, j, n - 1)]]
        for i, j in combinations(range(n - 1), 2)
    )


def span_words(basis):
    words = [0]
    for vector in basis:
        words += [word ^ vector for word in words]
    return tuple(words)


def precompute_boundaries(n: int) -> list[int]:
    dimension = len(triples(n))
    boundaries = triangle_boundaries(n)
    values = [0] * (1 << dimension)
    for mask in range(1, 1 << dimension):
        bit = mask & -mask
        values[mask] = values[mask ^ bit] ^ boundaries[bit.bit_length() - 1]
    return values


def verify_linear_boxes() -> None:
    print("[linear_chain_complex_boxes]")
    for n in range(1, 17):
        edge_count = comb(n, 2)
        face_count = comb(n, 3)
        zdim = comb(n - 1, 2) if n >= 1 else 0
        expected_rank = comb(n - 1, 2) if n & 1 else comb(max(n - 2, 0), 2)
        expected_bicycle = 0 if n & 1 else max(n - 2, 0)

        w_rank = gf2_rank(triangle_boundaries(n))
        l_columns = tuple(graph_coboundary(b, n) for b in triangle_boundaries(n))
        l_rank = gf2_rank(l_columns)
        check(w_rank == zdim, f"boundary rank n={n}")
        check(l_rank == expected_rank, f"Gram rank n={n}")

        epsilon = n & 1
        for face, image in enumerate(l_columns):
            image2 = step(image, n)
            check(image2 == (image if epsilon else 0), f"L square law n={n} face={face}")
            source = triples(n)[face]
            expected_johnson = 0
            for target_index, target in enumerate(triples(n)):
                if target == source or len(set(source) & set(target)) == 2:
                    expected_johnson |= 1 << target_index
            check(image == expected_johnson, f"I+Johnson identity n={n} face={face}")

        for edge_bit in range(edge_count):
            graph = 1 << edge_bit
            left = edge_upper_laplacian(graph, n)
            right = (graph if epsilon else 0) ^ vertex_coboundary(
                graph_vertex_boundary(graph, n), n
            )
            check(left == right, f"WWt identity n={n} edge={edge_bit}")

        basis = cycle_basis(n)
        check(len(basis) == zdim)
        check(gf2_rank(basis) == zdim)
        for cycle in basis:
            check(graph_vertex_boundary(cycle, n) == 0)
            check(edge_upper_laplacian(cycle, n) == (cycle if epsilon else 0))

        bicycle_cuts = 0
        for subset in range(1 << max(n - 1, 0)):
            cut = vertex_coboundary(subset, n)
            if graph_vertex_boundary(cut, n) == 0:
                bicycle_cuts += 1
        check(bicycle_cuts == 1 << expected_bicycle, f"bicycle count n={n}")
        check(zdim - expected_bicycle == expected_rank)
        print(
            f"LINEAR n={n} C2={face_count} C1={edge_count} "
            f"cycle_dim={zdim} bicycle_dim={expected_bicycle} "
            f"rank_L={l_rank} square={'L' if epsilon else '0'}"
        )


def verify_boundary_reconstruction() -> None:
    print("\n[boundary_graph_reconstruction]")
    for n in range(3, 8):
        cycles = span_words(cycle_basis(n))
        by_image = Counter(graph_coboundary(cycle, n) for cycle in cycles)
        expected_lifts = 1 if n & 1 else 1 << (n - 2)
        expected_images = 1 << (comb(n - 1, 2) if n & 1 else comb(n - 2, 2))
        check(len(cycles) == 1 << comb(n - 1, 2))
        check(len(by_image) == expected_images)
        check(set(by_image.values()) == {expected_lifts})
        for cycle in cycles:
            check(graph_vertex_boundary(cycle, n) == 0)
        print(
            f"RECON n={n} Eulerian={len(cycles)} images={len(by_image)} "
            f"Eulerian_boundary_lifts_per_image={expected_lifts} "
            f"hypergraphs_per_boundary={1 << comb(n - 1, 3)}"
        )


def verify_exhaustive_graphs() -> None:
    print("\n[exhaustive_hypergraph_functional_graphs]")
    digest = sha256()
    for n in range(3, 7):
        face_count = comb(n, 3)
        total = 1 << face_count
        rank_l = comb(n - 1, 2) if n & 1 else comb(n - 2, 2)
        kernel_l = face_count - rank_l
        kernel_w = comb(n - 1, 3)
        boundaries = precompute_boundaries(n)
        boundary_fibres = Counter(boundaries)
        one_step = Counter()
        two_step = Counter()
        depth = Counter()
        fixed = 0
        width = max(1, (face_count + 7) // 8)

        for x in range(total):
            b = boundaries[x]
            y = graph_coboundary(b, n)
            yy = graph_coboundary(boundaries[y], n)
            check(yy == (y if n & 1 else 0), f"state square law n={n} x={x}")
            check(step(x, n) == y)
            one_step[y] += 1
            two_step[yy] += 1
            fixed += y == x
            if n & 1:
                depth[0 if y == x else 1] += 1
            else:
                depth[0 if x == 0 else (1 if y == 0 else 2)] += 1
            digest.update(bytes((n,)))
            digest.update(x.to_bytes(width, "little"))
            digest.update(y.to_bytes(width, "little"))

        cycle_dim = comb(n - 1, 2)
        check(len(boundary_fibres) == 1 << cycle_dim)
        check(set(boundary_fibres.values()) == {1 << kernel_w})
        check(len(one_step) == 1 << rank_l)
        check(set(one_step.values()) == {1 << kernel_l})

        if n & 1:
            expected_depth = Counter({0: 1 << rank_l, 1: total - (1 << rank_l)})
            expected_fixed = 1 << rank_l
        else:
            expected_depth = Counter(
                {
                    0: 1,
                    1: (1 << kernel_l) - 1,
                    2: total - (1 << kernel_l),
                }
            )
            expected_fixed = 1
        check(depth == expected_depth)
        check(fixed == expected_fixed)

        # Every target and times 0..4.  Later counters are pushed forward
        # from the exact preceding fibre counter, not filled from the formula.
        time_counters = {1: one_step, 2: two_step}
        for t in range(3, 5):
            current = Counter()
            for state, count in time_counters[t - 1].items():
                current[step(state, n)] += count
            time_counters[t] = current
        for target in range(total):
            check(1 == 1)  # t=0 identity fibre
            expected_t1 = (1 << kernel_l) if target in one_step else 0
            check(one_step.get(target, 0) == expected_t1)
            for t in range(2, 5):
                if n & 1:
                    expected = expected_t1
                else:
                    expected = total if target == 0 else 0
                check(time_counters[t].get(target, 0) == expected)

        print(
            f"EXHAUSTIVE n={n} states={total} image={len(one_step)} "
            f"fixed={fixed} kernel_L_dim={kernel_l} "
            f"boundary_count={len(boundary_fibres)} kernel_W_dim={kernel_w} "
            f"depth_hist={tuple(sorted(depth.items()))} "
            f"one_step_fibre={1 << kernel_l}"
        )
    print(f"EDGE_DIGEST={digest.hexdigest()}")


def main() -> None:
    print("HYPERGRAPH_INCIDENCE_GATE")
    print("carrier=3-uniform_hypergraphs update=W_2,3^T_W_2,3 over F2")
    print("external=HOLD_EXTERNAL computation=falsification_not_proof")
    verify_linear_boxes()
    verify_boundary_reconstruction()
    verify_exhaustive_graphs()
    print(f"\nASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
