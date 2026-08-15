"""Independent exact reconstruction of the nine regular centralizer torsors."""

from __future__ import annotations

from math import gcd
from typing import Any, Iterable

from .constants import BASE_VECTOR, CAT_MATRIX, EXPECTED_LEDGER, IDENTITY, LOCKED_MODULI


Matrix2 = tuple[tuple[int, int], tuple[int, int]]
Vector2 = tuple[int, int]


def locked_modulus(value: int) -> int:
    if type(value) is not int or value not in LOCKED_MODULI:
        raise ValueError("modulus is outside the frozen nine-element tuple")
    return value


def matrix_mod(matrix: Matrix2, modulus: int) -> Matrix2:
    q = locked_modulus(modulus)
    return tuple(tuple(value % q for value in row) for row in matrix)  # type: ignore[return-value]


def matrix_multiply(left: Matrix2, right: Matrix2, modulus: int) -> Matrix2:
    q = locked_modulus(modulus)
    return (
        (
            (left[0][0] * right[0][0] + left[0][1] * right[1][0]) % q,
            (left[0][0] * right[0][1] + left[0][1] * right[1][1]) % q,
        ),
        (
            (left[1][0] * right[0][0] + left[1][1] * right[1][0]) % q,
            (left[1][0] * right[0][1] + left[1][1] * right[1][1]) % q,
        ),
    )


def matrix_vector(matrix: Matrix2, vector: Vector2, modulus: int) -> Vector2:
    q = locked_modulus(modulus)
    return (
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % q,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % q,
    )


def determinant(matrix: Matrix2, modulus: int) -> int:
    q = locked_modulus(modulus)
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % q


def is_unit(value: int, modulus: int) -> bool:
    q = locked_modulus(modulus)
    return gcd(value % q, q) == 1


def all_matrices(modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    return tuple(
        ((a, b), (c, d))
        for a in range(q)
        for b in range(q)
        for c in range(q)
        for d in range(q)
    )


def algebra_matrix(a: int, b: int, modulus: int) -> Matrix2:
    q = locked_modulus(modulus)
    return (((a + 2 * b) % q, b % q), (b % q, (a + b) % q))


def algebra_norm(a: int, b: int, modulus: int) -> int:
    q = locked_modulus(modulus)
    return (a * a + 3 * a * b + b * b) % q


def brute_commutant(modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    matrix = matrix_mod(CAT_MATRIX, q)
    return tuple(
        item
        for item in all_matrices(q)
        if matrix_multiply(item, matrix, q) == matrix_multiply(matrix, item, q)
    )


def direct_centralizer(modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    return tuple(
        item for item in brute_commutant(q) if is_unit(determinant(item, q), q)
    )


def algebra_centralizer(modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    return tuple(
        sorted(
            algebra_matrix(a, b, q)
            for a in range(q)
            for b in range(q)
            if is_unit(algebra_norm(a, b, q), q)
        )
    )


def cyclic_delta(vector: Vector2, modulus: int) -> int:
    q = locked_modulus(modulus)
    image = matrix_vector(matrix_mod(CAT_MATRIX, q), vector, q)
    return (vector[0] * image[1] - vector[1] * image[0]) % q


def direct_cyclic_locus(modulus: int) -> tuple[Vector2, ...]:
    q = locked_modulus(modulus)
    return tuple(
        (x, y)
        for x in range(q)
        for y in range(q)
        if is_unit(cyclic_delta((x, y), q), q)
    )


def algebra_torsor_image(group: tuple[Matrix2, ...], modulus: int) -> tuple[Vector2, ...]:
    q = locked_modulus(modulus)
    return tuple(sorted(matrix_vector(item, BASE_VECTOR, q) for item in group))


def matrix_power(matrix: Matrix2, exponent: int, modulus: int) -> Matrix2:
    q = locked_modulus(modulus)
    if type(exponent) is not int or exponent < 0:
        raise ValueError("matrix exponent must be a nonnegative integer")
    result = matrix_mod(IDENTITY, q)
    factor = matrix_mod(matrix, q)
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = matrix_multiply(result, factor, q)
        factor = matrix_multiply(factor, factor, q)
        remaining //= 2
    return result


def matrix_order(matrix: Matrix2, modulus: int) -> int:
    q = locked_modulus(modulus)
    identity = matrix_mod(IDENTITY, q)
    current = identity
    for exponent in range(1, q ** 4 + 1):
        current = matrix_multiply(current, matrix, q)
        if current == identity:
            return exponent
    raise RuntimeError("matrix order exceeded the finite ambient bound")


def canonical_cycle(points: Iterable[Vector2]) -> tuple[Vector2, ...]:
    values = tuple(points)
    if not values:
        raise ValueError("empty cycle")
    rotations = tuple(values[index:] + values[:index] for index in range(len(values)))
    return min(rotations)


def permutation_cycles(
    matrix: Matrix2, points: tuple[Vector2, ...], modulus: int
) -> tuple[tuple[Vector2, ...], ...]:
    q = locked_modulus(modulus)
    point_set = set(points)
    unseen = set(points)
    cycles: list[tuple[Vector2, ...]] = []
    while unseen:
        start = min(unseen)
        current = start
        cycle: list[Vector2] = []
        while current not in cycle:
            if current not in point_set:
                raise RuntimeError("permutation left the declared point set")
            cycle.append(current)
            current = matrix_vector(matrix, current, q)
        if current != start:
            raise RuntimeError("permutation cycle did not close at its start")
        canonical = canonical_cycle(tuple(cycle))
        cycles.append(canonical)
        unseen.difference_update(canonical)
    return tuple(sorted(cycles))


def subgroup_generated_by(matrix: Matrix2, modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    order = matrix_order(matrix, q)
    return tuple(sorted(matrix_power(matrix, exponent, q) for exponent in range(order)))


def _group_axioms(group: tuple[Matrix2, ...], modulus: int) -> dict[str, bool]:
    q = locked_modulus(modulus)
    identity = matrix_mod(IDENTITY, q)
    group_set = set(group)
    closure = all(
        matrix_multiply(left, right, q) in group_set for left in group for right in group
    )
    inverse = all(
        any(matrix_multiply(left, right, q) == identity for right in group) for left in group
    )
    abelian = all(
        matrix_multiply(left, right, q) == matrix_multiply(right, left, q)
        for left in group
        for right in group
    )
    return {
        "identity": identity in group_set,
        "closure": closure,
        "inverses": inverse,
        "abelian": abelian,
    }


def _action_axioms(
    group: tuple[Matrix2, ...], points: tuple[Vector2, ...], modulus: int
) -> dict[str, Any]:
    q = locked_modulus(modulus)
    point_set = set(points)
    kernel = tuple(
        item
        for item in group
        if all(matrix_vector(item, point, q) == point for point in points)
    )
    stabilizer_sizes = tuple(
        sum(matrix_vector(item, point, q) == point for item in group) for point in points
    )
    base_orbit = tuple(sorted(matrix_vector(item, points[0], q) for item in group))
    return {
        "closed": all(
            matrix_vector(item, point, q) in point_set for item in group for point in points
        ),
        "kernel": kernel,
        "free": all(size == 1 for size in stabilizer_sizes),
        "transitive": base_orbit == points,
        "stabilizer_sizes": stabilizer_sizes,
    }


def reconstruct_regular_torsor(modulus: int) -> dict[str, Any]:
    q = locked_modulus(modulus)
    direct_group = direct_centralizer(q)
    algebra_group = algebra_centralizer(q)
    direct_points = direct_cyclic_locus(q)
    algebra_points = algebra_torsor_image(algebra_group, q)
    matrix = matrix_mod(CAT_MATRIX, q)
    order = matrix_order(matrix, q)
    inverse = matrix_power(matrix, order - 1, q)
    power_table = tuple(matrix_power(matrix, exponent, q) for exponent in range(order))
    inverse_power_table = tuple(
        matrix_power(inverse, exponent, q) for exponent in range(order)
    )
    cycles = permutation_cycles(matrix, direct_points, q)
    group_axioms = _group_axioms(direct_group, q)
    action_axioms = _action_axioms(direct_group, direct_points, q)
    expected_n, expected_r, expected_m = EXPECTED_LEDGER[q]
    n = len(direct_group)
    r = order
    m = len(cycles)
    checks = {
        "commutant_dimension_two": len(brute_commutant(q)) == q * q,
        "direct_group_equals_algebra_units": direct_group == algebra_group,
        "direct_cyclic_equals_algebra_torsor_image": direct_points == algebra_points,
        "group_identity": group_axioms["identity"],
        "group_closure": group_axioms["closure"],
        "group_inverses": group_axioms["inverses"],
        "group_abelian": group_axioms["abelian"],
        "action_closed": action_axioms["closed"],
        "action_free": action_axioms["free"],
        "action_transitive": action_axioms["transitive"],
        "action_effective": action_axioms["kernel"] == (matrix_mod(IDENTITY, q),),
        "uniform_source_cycle_length": all(len(cycle) == r for cycle in cycles),
        "expected_n": n == expected_n,
        "expected_r": r == expected_r,
        "expected_m": m == expected_m,
        "cycle_partition_size": sum(len(cycle) for cycle in cycles) == len(direct_points),
    }
    return {
        "q": q,
        "cat_matrix": matrix,
        "cat_matrix_inverse": inverse,
        "cat_power_table": power_table,
        "cat_inverse_power_table": inverse_power_table,
        "direct_commutant": brute_commutant(q),
        "direct_group": direct_group,
        "algebra_group": algebra_group,
        "direct_cyclic_locus": direct_points,
        "algebra_torsor_image": algebra_points,
        "action_kernel": action_axioms["kernel"],
        "source_cycles": cycles,
        "n": n,
        "r": r,
        "m": m,
        "checks": checks,
        "pass": all(checks.values()),
    }
