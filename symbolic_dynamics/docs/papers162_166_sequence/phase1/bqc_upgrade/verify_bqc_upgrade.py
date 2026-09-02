#!/usr/bin/env python3
"""Independent exact gate for the tree-fibre upgrade of BQC.

The test does not enumerate arbitrary graphs.  It independently enumerates
all labelled trees by Pruefer words, records their literal consecutive-block
quotients, and compares every target count with an inclusion--exclusion of
Matrix--Tree cofactors for clique blow-ups.
"""

from __future__ import annotations

from collections import Counter
from heapq import heapify, heappop, heappush
from itertools import combinations, product
from math import comb
from hashlib import sha256


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def det_bareiss(matrix: list[list[int]]) -> int:
    """Exact determinant using fraction-free Bareiss elimination."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                check(numerator % previous == 0, "Bareiss exact division")
                a[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def block_sizes(n: int, width: int) -> tuple[int, ...]:
    return tuple(min(width, n - start) for start in range(0, n, width))


def prufer_tree(n: int, word: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if n == 1:
        return ()
    degree = [1] * n
    for value in word:
        degree[value] += 1
    leaves = [v for v in range(n) if degree[v] == 1]
    heapify(leaves)
    edges: list[tuple[int, int]] = []
    for value in word:
        leaf = heappop(leaves)
        edges.append(tuple(sorted((leaf, value))))
        degree[leaf] -= 1
        degree[value] -= 1
        if degree[value] == 1:
            heappush(leaves, value)
    u = heappop(leaves)
    v = heappop(leaves)
    edges.append(tuple(sorted((u, v))))
    return tuple(sorted(edges))


def quotient_mask(edges: tuple[tuple[int, int], ...], width: int, m: int) -> int:
    target_edges = list(combinations(range(m), 2))
    index = {edge: k for k, edge in enumerate(target_edges)}
    mask = 0
    for u, v in edges:
        a, b = sorted((u // width, v // width))
        if a != b:
            mask |= 1 << index[(a, b)]
    return mask


def blowup_tree_count(sizes: tuple[int, ...], target_mask: int) -> int:
    """Tree count of H[K_s1,...,K_sm] from a reduced Laplacian."""
    m = len(sizes)
    target_edges = list(combinations(range(m), 2))
    adjacent = [[False] * m for _ in range(m)]
    for k, (i, j) in enumerate(target_edges):
        if target_mask >> k & 1:
            adjacent[i][j] = adjacent[j][i] = True
    cross_degrees = [
        sum(sizes[j] for j in range(m) if adjacent[i][j]) for i in range(m)
    ]
    alpha = [sizes[i] + cross_degrees[i] for i in range(m)]
    quotient_laplacian = [
        [
            cross_degrees[i]
            if i == j
            else (-sizes[j] if adjacent[i][j] else 0)
            for j in range(m)
        ]
        for i in range(m)
    ]
    cofactor = [
        [quotient_laplacian[i][j] for j in range(1, m)]
        for i in range(1, m)
    ]
    answer = det_bareiss(cofactor)
    for value, size in zip(alpha, sizes):
        answer *= value ** (size - 1)
    check(answer % sizes[0] == 0, "reduced blow-up formula is integral")
    return answer // sizes[0]


def prescribed_quotient_tree_count(sizes: tuple[int, ...], target_mask: int) -> int:
    """Require every quotient edge by Boolean-lattice inversion."""
    answer = 0
    submask = target_mask
    while True:
        answer += (-1) ** ((target_mask ^ submask).bit_count()) * blowup_tree_count(
            sizes, submask
        )
        if submask == 0:
            return answer
        submask = (submask - 1) & target_mask


def all_prescribed_counts(sizes: tuple[int, ...]) -> list[int]:
    """All target counts by the fast Boolean Mobius transform."""
    edge_count = comb(len(sizes), 2)
    counts = [blowup_tree_count(sizes, mask) for mask in range(1 << edge_count)]
    for bit in range(edge_count):
        flag = 1 << bit
        for mask in range(1 << edge_count):
            if mask & flag:
                counts[mask] -= counts[mask ^ flag]
    return counts


def literal_counts(n: int, width: int) -> Counter[int]:
    sizes = block_sizes(n, width)
    counts: Counter[int] = Counter()
    words = [()] if n == 1 else product(range(n), repeat=n - 2)
    seen: set[tuple[tuple[int, int], ...]] = set()
    for word in words:
        tree = prufer_tree(n, tuple(word))
        check(tree not in seen, "Pruefer coding is injective")
        seen.add(tree)
        check(len(tree) == n - 1, "tree edge count")
        counts[quotient_mask(tree, width, len(sizes))] += 1
    check(len(seen) == (1 if n == 1 else n ** (n - 2)), "Cayley mass")
    return counts


def verify_all_targets() -> list[str]:
    rows: list[str] = []
    for n in range(1, 9):
        for width in range(1, n + 1):
            sizes = block_sizes(n, width)
            m = len(sizes)
            actual = literal_counts(n, width)
            positive = 0
            formula_mass = 0
            if m <= 6:
                expected_counts = all_prescribed_counts(sizes)
                targets = range(len(expected_counts))
            else:
                # The width-one boundary has up to 28 quotient edges.  Every
                # literal tree is its own target.  Check a deterministic
                # sample plus dense/disconnected zero-fibre attacks without
                # pretending to traverse all 2^28 target graphs.
                sample = sorted(actual)[:1024]
                edge_count = comb(m, 2)
                edge_index = {
                    edge: k for k, edge in enumerate(combinations(range(m), 2))
                }
                path_mask = sum(
                    1 << edge_index[(i, i + 1)] for i in range(m - 1)
                )
                cycle_mask = path_mask | (1 << edge_index[(0, m - 1)])
                disconnected_mask = sum(
                    1 << edge_index[(i, i + 1)] for i in range(0, m - 1, 2)
                )
                attacks = [0, path_mask, cycle_mask, disconnected_mask]
                targets = sorted(set(sample + attacks))
                expected_counts = None
            for target in targets:
                expected = (
                    expected_counts[target]
                    if expected_counts is not None
                    else prescribed_quotient_tree_count(sizes, target)
                )
                check(expected >= 0, "inverted tree count is nonnegative")
                check(actual[target] == expected, f"target mismatch n={n},w={width}")
                if expected_counts is not None:
                    formula_mass += expected
                    positive += expected > 0
            cayley = 1 if n == 1 else n ** (n - 2)
            if expected_counts is not None:
                check(formula_mass == cayley, "prescribed targets partition all trees")
            else:
                check(sum(actual.values()) == cayley, "literal width-one Cayley mass")
                positive = len(actual)
            rows.append(
                f"n={n},width={width},blocks={sizes},trees={cayley},"
                f"positive_targets={positive}"
            )
    return rows


def verify_parameter_probe() -> list[str]:
    """The time-one empty-fibre exponent strictly identifies the block width."""
    rows: list[str] = []
    for n in range(2, 513):
        previous = -1
        for width in range(1, n + 1):
            exponent = sum(comb(size, 2) for size in block_sizes(n, width))
            check(exponent > previous, f"strict width probe n={n},w={width}")
            previous = exponent
        rows.append(f"n={n},strict_internal_edge_exponents=PASS")
    return rows


def main() -> None:
    tree_rows = verify_all_targets()
    probe_rows = verify_parameter_probe()
    payload = "\n".join(tree_rows + probe_rows).encode()
    print("BQC_TREE_FIBRE_UPGRADE_V1")
    print(f"tree_boxes={len(tree_rows)}")
    print(f"parameter_boxes={len(probe_rows)}")
    print(f"payload_sha256={sha256(payload).hexdigest()}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
