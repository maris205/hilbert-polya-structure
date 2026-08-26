#!/usr/bin/env python3
"""Deterministic regression controls for P67.

The program checks finite linear-algebra and counting consequences of the
manuscript.  It does not replace the global product-homeomorphism proof, the
all-finite-shape theorem, or the literature audit.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import product


def rank_mod(rows: list[list[int]], prime: int) -> int:
    """Return row rank over F_prime."""
    if not rows:
        return 0
    matrix = [[entry % prime for entry in row] for row in rows]
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0
    for column in range(ncols):
        pivot = next(
            (row for row in range(pivot_row, nrows) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, prime)
        matrix[pivot_row] = [
            (inverse * entry) % prime for entry in matrix[pivot_row]
        ]
        for row in range(nrows):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def f4_add(left: int, right: int) -> int:
    """Add in F_4 = F_2[u]/(u^2+u+1), encoded as a0 + a1*u."""
    return left ^ right


def f4_mul(left: int, right: int) -> int:
    """Multiply encoded elements of F_4 exactly."""
    left_constant, left_linear = left & 1, (left >> 1) & 1
    right_constant, right_linear = right & 1, (right >> 1) & 1
    constant = (left_constant * right_constant) ^ (
        left_linear * right_linear
    )
    linear = (
        (left_constant * right_linear)
        ^ (left_linear * right_constant)
        ^ (left_linear * right_linear)
    )
    return constant | (linear << 1)


def f4_inverse(value: int) -> int:
    """Return the multiplicative inverse of a nonzero encoded element."""
    if value == 0:
        raise ZeroDivisionError("zero has no inverse in F_4")
    return next(candidate for candidate in range(1, 4) if f4_mul(value, candidate) == 1)


def rank_f4(rows: list[list[int]]) -> int:
    """Return row rank over the nonprime extension field F_4."""
    if not rows:
        return 0
    matrix = [row.copy() for row in rows]
    nrows = len(matrix)
    ncols = len(matrix[0])
    pivot_row = 0
    for column in range(ncols):
        pivot = next(
            (row for row in range(pivot_row, nrows) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = f4_inverse(matrix[pivot_row][column])
        matrix[pivot_row] = [
            f4_mul(inverse, entry) for entry in matrix[pivot_row]
        ]
        for row in range(nrows):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                f4_add(left, f4_mul(factor, right))
                for left, right in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def root_coordinates(index: int, a: int, b: int) -> tuple[int, int, int]:
    """Return the unique (r,i,j) with index=r*a**i*b**j."""
    remainder = index
    exponent_a = 0
    exponent_b = 0
    while remainder % a == 0:
        remainder //= a
        exponent_a += 1
    while remainder % b == 0:
        remainder //= b
        exponent_b += 1
    return remainder, exponent_a, exponent_b


def prefix_constraint_matrix(
    a: int, b: int, cutoff: int, prime: int
) -> list[list[int]]:
    """Constraint matrix for the projection to [1,cutoff]."""
    rows: list[list[int]] = []
    for index in range(1, cutoff // (a * b) + 1):
        row = [0] * cutoff
        for coordinate, coefficient in (
            (index, 1),
            (a * index, -1),
            (b * index, -1),
            (a * b * index, 1),
        ):
            row[coordinate - 1] = (row[coordinate - 1] + coefficient) % prime
        rows.append(row)
    return rows


def direct_projection_dimension(
    a: int,
    b: int,
    cutoff: int,
    selected: tuple[int, ...],
    prime: int,
) -> int:
    """Project the kernel of the prefix constraint matrix onto selected.

    If A=[A_F A_C], the realizable selected vectors have codimension
    rank(A)-rank(A_C).
    """
    constraints = prefix_constraint_matrix(a, b, cutoff, prime)
    selected_zero = {coordinate - 1 for coordinate in selected}
    complement = [
        column for column in range(cutoff) if column not in selected_zero
    ]
    complement_matrix = [
        [row[column] for column in complement] for row in constraints
    ]
    return (
        len(selected)
        - rank_mod(constraints, prime)
        + rank_mod(complement_matrix, prime)
    )


def direct_projection_dimension_f4(
    a: int, b: int, cutoff: int, selected: tuple[int, ...]
) -> int:
    """Project the finite prefix kernel over F_4 onto selected coordinates."""
    # In characteristic two, the plaquette coefficients +1 and -1 coincide.
    constraints = prefix_constraint_matrix(a, b, cutoff, 2)
    selected_zero = {coordinate - 1 for coordinate in selected}
    complement = [
        column for column in range(cutoff) if column not in selected_zero
    ]
    complement_matrix = [
        [row[column] for column in complement] for row in constraints
    ]
    return len(selected) - rank_f4(constraints) + rank_f4(complement_matrix)


def edge_graph_statistics(
    edges: set[tuple[int, int]],
) -> tuple[int, int, int, int]:
    """Return (rank, cycle rank, components, vertices) for a bipartite graph."""
    if not edges:
        return 0, 0, 0, 0
    adjacency: dict[tuple[str, int], set[tuple[str, int]]] = defaultdict(set)
    for row, column in edges:
        left = ("L", row)
        right = ("R", column)
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(adjacency)
    components = 0
    while unseen:
        components += 1
        start = unseen.pop()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
    vertices = len(adjacency)
    rank = vertices - components
    cycle_rank = len(edges) - rank
    return rank, cycle_rank, components, vertices


def arithmetic_graph_statistics(
    selected: tuple[int, ...], a: int, b: int
) -> tuple[int, int]:
    """Return the manuscript rank and total cycle defect for selected indices."""
    root_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)
    for coordinate in selected:
        root, exponent_a, exponent_b = root_coordinates(coordinate, a, b)
        root_edges[root].add((exponent_a, exponent_b))
    dimension = 0
    cycle_rank = 0
    for edges in root_edges.values():
        component_dimension, component_cycle_rank, _, _ = edge_graph_statistics(
            edges
        )
        dimension += component_dimension
        cycle_rank += component_cycle_rank
    assert dimension + cycle_rank == len(selected)
    return dimension, cycle_rank


def check_root_coordinates_and_global_axes() -> tuple[int, int]:
    coordinate_cases = 0
    global_instances = 0
    for a, b in ((2, 3), (2, 5), (3, 4), (4, 9), (6, 35)):
        for index in range(1, 2001):
            root, exponent_a, exponent_b = root_coordinates(index, a, b)
            assert index == root * a**exponent_a * b**exponent_b
            assert root % a != 0 and root % b != 0
            assert (index % (a * b) != 0) == (
                exponent_a == 0 or exponent_b == 0
            )
            coordinate_cases += 1

        for prime in (2, 3, 5):
            cutoff = 600
            free_values = {
                index: (index * index + 3 * index + 1) % prime
                for index in range(1, cutoff + 1)
                if index % (a * b) != 0
            }

            def reconstructed(index: int) -> int:
                root, exponent_a, exponent_b = root_coordinates(index, a, b)
                axis_a = root * a**exponent_a
                axis_b = root * b**exponent_b
                return (
                    free_values[axis_a]
                    + free_values[axis_b]
                    - free_values[root]
                ) % prime

            for index, value in free_values.items():
                assert reconstructed(index) == value
            for index in range(1, cutoff // (a * b) + 1):
                assert (
                    reconstructed(index)
                    - reconstructed(a * index)
                    - reconstructed(b * index)
                    + reconstructed(a * b * index)
                ) % prime == 0
            global_instances += 1
    return coordinate_cases, global_instances


def check_prefixes() -> int:
    cases = 0
    for a, b, prime in ((2, 3, 2), (2, 5, 3), (3, 4, 5), (4, 9, 2)):
        for cutoff in range(1, 81):
            constraints = prefix_constraint_matrix(a, b, cutoff, prime)
            expected_constraint_rank = cutoff // (a * b)
            assert rank_mod(constraints, prime) == expected_constraint_rank
            selected = tuple(range(1, cutoff + 1))
            graph_dimension, graph_cycles = arithmetic_graph_statistics(
                selected, a, b
            )
            expected_dimension = cutoff - expected_constraint_rank
            assert graph_dimension == expected_dimension
            assert graph_cycles == expected_constraint_rank
            cases += 1
    return cases


def check_all_small_finite_projections() -> int:
    cases = 0
    cutoff = 12
    for a, b, prime in ((2, 3, 2), (2, 5, 3), (3, 4, 5)):
        for mask in range(1 << cutoff):
            selected = tuple(
                coordinate
                for coordinate in range(1, cutoff + 1)
                if mask & (1 << (coordinate - 1))
            )
            direct = direct_projection_dimension(
                a, b, cutoff, selected, prime
            )
            graph_dimension, _ = arithmetic_graph_statistics(selected, a, b)
            assert direct == graph_dimension, (
                a,
                b,
                prime,
                selected,
                direct,
                graph_dimension,
            )
            cases += 1
    return cases


def rectangular_constraint_rank(
    rows_count: int, columns_count: int, prime: int
) -> int:
    constraints: list[list[int]] = []
    for row in range(rows_count - 1):
        for column in range(columns_count - 1):
            equation = [0] * (rows_count * columns_count)
            for delta_row, delta_column, coefficient in (
                (0, 0, 1),
                (1, 0, -1),
                (0, 1, -1),
                (1, 1, 1),
            ):
                position = (row + delta_row) * columns_count + column + delta_column
                equation[position] = (equation[position] + coefficient) % prime
            constraints.append(equation)
    return rank_mod(constraints, prime)


def check_rectangles() -> int:
    cases = 0
    for prime in (2, 3, 5):
        for rows_count in range(1, 7):
            for columns_count in range(1, 7):
                constraint_rank = rectangular_constraint_rank(
                    rows_count, columns_count, prime
                )
                expected_cycle_rank = (rows_count - 1) * (columns_count - 1)
                expected_dimension = rows_count + columns_count - 1
                assert constraint_rank == expected_cycle_rank
                assert (
                    rows_count * columns_count - constraint_rank
                    == expected_dimension
                )
                edges = {
                    (row, column)
                    for row in range(rows_count)
                    for column in range(columns_count)
                }
                graph_dimension, graph_cycles, components, _ = (
                    edge_graph_statistics(edges)
                )
                assert components == 1
                assert graph_dimension == expected_dimension
                assert graph_cycles == expected_cycle_rank
                cases += 1
    return cases


def check_edge_update_laws() -> int:
    """Check the rank/nullity dichotomy under one-edge deletion or addition."""
    cases = 0

    cycle = {(0, 0), (0, 1), (1, 0), (1, 1)}
    cycle_rank, cycle_nullity, _, _ = edge_graph_statistics(cycle)
    for edge in cycle:
        reduced_rank, reduced_nullity, _, _ = edge_graph_statistics(
            cycle - {edge}
        )
        assert reduced_rank == cycle_rank
        assert reduced_nullity == cycle_nullity - 1
        cases += 1

    tree = {(0, 0), (0, 1), (1, 1)}
    tree_rank, tree_nullity, _, _ = edge_graph_statistics(tree)
    for edge in tree:
        reduced_rank, reduced_nullity, _, _ = edge_graph_statistics(
            tree - {edge}
        )
        assert reduced_rank == tree_rank - 1
        assert reduced_nullity == tree_nullity
        cases += 1

    additions = (
        ({(0, 0)}, (1, 0), 1, 0),
        ({(0, 0)}, (1, 1), 1, 0),
        ({(0, 0), (1, 1)}, (0, 1), 1, 0),
        (tree, (1, 0), 0, 1),
    )
    for edges, new_edge, rank_delta, nullity_delta in additions:
        old_rank, old_nullity, _, _ = edge_graph_statistics(edges)
        new_rank, new_nullity, _, _ = edge_graph_statistics(edges | {new_edge})
        assert new_rank == old_rank + rank_delta
        assert new_nullity == old_nullity + nullity_delta
        cases += 1

    return cases


def potential_pattern_counts(
    edges: tuple[tuple[int, int], ...], prime: int
) -> tuple[Counter[tuple[int, ...]], int, int]:
    row_vertices = sorted({row for row, _ in edges})
    column_vertices = sorted({column for _, column in edges})
    row_position = {vertex: index for index, vertex in enumerate(row_vertices)}
    column_position = {
        vertex: index for index, vertex in enumerate(column_vertices)
    }
    counts: Counter[tuple[int, ...]] = Counter()
    for assignment in product(
        range(prime), repeat=len(row_vertices) + len(column_vertices)
    ):
        row_values = assignment[: len(row_vertices)]
        column_values = assignment[len(row_vertices) :]
        pattern = tuple(
            (
                row_values[row_position[row]]
                + column_values[column_position[column]]
            )
            % prime
            for row, column in edges
        )
        counts[pattern] += 1
    rank, _, components, _ = edge_graph_statistics(set(edges))
    return counts, rank, components


def check_haar_and_forest_independence() -> int:
    shapes = (
        ((0, 0), (0, 1), (1, 1)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 1)),
    )
    cases = 0
    for prime in (2, 3, 5):
        for edges in shapes:
            counts, rank, components = potential_pattern_counts(edges, prime)
            total_assignments = sum(counts.values())
            assert len(counts) == prime**rank
            assert set(counts.values()) == {prime**components}

            for coordinate in range(len(edges)):
                marginal = Counter()
                for pattern, multiplicity in counts.items():
                    marginal[pattern[coordinate]] += multiplicity
                assert set(marginal) == set(range(prime))
                assert set(marginal.values()) == {total_assignments // prime}

            for first in range(len(edges)):
                for second in range(first + 1, len(edges)):
                    marginal_pair = Counter()
                    for pattern, multiplicity in counts.items():
                        marginal_pair[(pattern[first], pattern[second])] += multiplicity
                    assert len(marginal_pair) == prime**2
                    assert set(marginal_pair.values()) == {
                        total_assignments // (prime**2)
                    }

            _, cycle_rank, _, _ = edge_graph_statistics(set(edges))
            assert len(edges) - rank == cycle_rank
            if cycle_rank == 0:
                assert len(counts) == prime ** len(edges)
            else:
                assert edges == shapes[1]
                for pattern in counts:
                    assert (
                        pattern[0] - pattern[1] - pattern[2] + pattern[3]
                    ) % prime == 0
            cases += 1
    return cases


def potential_pattern_counts_f4(
    edges: tuple[tuple[int, int], ...],
) -> tuple[Counter[tuple[int, ...]], int, int]:
    """Enumerate a potential map over F_4 using exact polynomial arithmetic."""
    row_vertices = sorted({row for row, _ in edges})
    column_vertices = sorted({column for _, column in edges})
    row_position = {vertex: index for index, vertex in enumerate(row_vertices)}
    column_position = {
        vertex: index for index, vertex in enumerate(column_vertices)
    }
    counts: Counter[tuple[int, ...]] = Counter()
    for assignment in product(
        range(4), repeat=len(row_vertices) + len(column_vertices)
    ):
        row_values = assignment[: len(row_vertices)]
        column_values = assignment[len(row_vertices) :]
        pattern = tuple(
            f4_add(
                row_values[row_position[row]],
                column_values[column_position[column]],
            )
            for row, column in edges
        )
        counts[pattern] += 1
    rank, _, components, _ = edge_graph_statistics(set(edges))
    return counts, rank, components


def check_extension_field_f4() -> tuple[int, int, int, int]:
    """Exercise ranks, projections, rectangles, and Haar laws over F_4."""
    assert all(f4_mul(value, f4_inverse(value)) == 1 for value in range(1, 4))

    prefix_cases = 0
    for cutoff in range(1, 81):
        constraints = prefix_constraint_matrix(2, 3, cutoff, 2)
        assert rank_f4(constraints) == cutoff // 6
        prefix_cases += 1

    projection_cases = 0
    cutoff = 12
    for mask in range(1 << cutoff):
        selected = tuple(
            coordinate
            for coordinate in range(1, cutoff + 1)
            if mask & (1 << (coordinate - 1))
        )
        direct = direct_projection_dimension_f4(2, 3, cutoff, selected)
        graph_dimension, _ = arithmetic_graph_statistics(selected, 2, 3)
        assert direct == graph_dimension
        projection_cases += 1

    rectangle_cases = 0
    for rows_count in range(1, 7):
        for columns_count in range(1, 7):
            constraints: list[list[int]] = []
            for row in range(rows_count - 1):
                for column in range(columns_count - 1):
                    equation = [0] * (rows_count * columns_count)
                    for delta_row, delta_column in (
                        (0, 0),
                        (1, 0),
                        (0, 1),
                        (1, 1),
                    ):
                        position = (
                            (row + delta_row) * columns_count
                            + column
                            + delta_column
                        )
                        equation[position] = f4_add(equation[position], 1)
                    constraints.append(equation)
            assert rank_f4(constraints) == (rows_count - 1) * (
                columns_count - 1
            )
            rectangle_cases += 1

    shapes = (
        ((0, 0), (0, 1), (1, 1)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 1)),
    )
    haar_cases = 0
    for edges in shapes:
        counts, rank, components = potential_pattern_counts_f4(edges)
        total_assignments = sum(counts.values())
        assert len(counts) == 4**rank
        assert set(counts.values()) == {4**components}
        for first in range(len(edges)):
            for second in range(first + 1, len(edges)):
                marginal_pair = Counter()
                for pattern, multiplicity in counts.items():
                    marginal_pair[(pattern[first], pattern[second])] += multiplicity
                assert len(marginal_pair) == 16
                assert set(marginal_pair.values()) == {total_assignments // 16}
        _, cycle_rank, _, _ = edge_graph_statistics(set(edges))
        if cycle_rank:
            assert all(
                f4_add(f4_add(pattern[0], pattern[1]), f4_add(pattern[2], pattern[3]))
                == 0
                for pattern in counts
            )
        haar_cases += 1
    return prefix_cases, projection_cases, rectangle_cases, haar_cases


def main() -> None:
    coordinate_cases, global_instances = check_root_coordinates_and_global_axes()
    prefix_cases = check_prefixes()
    finite_projection_cases = check_all_small_finite_projections()
    rectangle_cases = check_rectangles()
    edge_update_cases = check_edge_update_laws()
    haar_cases = check_haar_and_forest_independence()
    f4_prefixes, f4_projections, f4_rectangles, f4_haar = (
        check_extension_field_f4()
    )

    print("multiplicative root and global-axis checks")
    print(f"  root coordinates checked:       {coordinate_cases}")
    print(f"  reconstructed global instances: {global_instances}")
    print("arithmetic-prefix checks")
    print(f"  prefix ranks/count exponents:   {prefix_cases}")
    print("arbitrary finite-projection checks")
    print(f"  all subsets of [1,12] checked:  {finite_projection_cases}")
    print("exponent-rectangle checks")
    print(f"  fields 2,3,5; sides 1,...,6:   {rectangle_cases}")
    print("edge deletion/addition checks")
    print(f"  rank/cycle-rank transitions:   {edge_update_cases}")
    print("Haar/forest/cycle checks")
    print(f"  exact potential enumerations:   {haar_cases}")
    print("  all distinct coordinate pairs are independent: PASS")
    print("  four-corner alternating cycle relation: PASS")
    print("rank theorem exercised in characteristics 2, 3, and 5")
    print("nonprime extension-field checks: F_4 = F_2[u]/(u^2+u+1)")
    print(f"  prefix ranks through 80:        {f4_prefixes}")
    print(f"  all subsets of [1,12]:         {f4_projections}")
    print(f"  rectangles through side 6:     {f4_rectangles}")
    print(f"  exact Haar enumerations:        {f4_haar}")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
