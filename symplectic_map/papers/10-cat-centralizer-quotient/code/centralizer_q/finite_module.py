"""Independent exact engines for the nine frozen residue modules."""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Any, Iterable

from .constants import (
    BASE_VECTOR,
    CAT_MATRIX,
    EXPECTED_LEDGER,
    IDENTITY,
    LEDGER_FIELDS,
    LOCKED_MODULI,
    LOCKED_PRIMES,
    REVERSOR,
)


Matrix2 = tuple[tuple[int, int], tuple[int, int]]
Vector2 = tuple[int, int]


def locked_modulus(value: int) -> int:
    if type(value) is not int or value not in LOCKED_MODULI:
        raise ValueError("modulus is outside the frozen nine-element tuple")
    return value


def expected_record(modulus: int) -> dict[str, Any]:
    q = locked_modulus(modulus)
    return dict(zip(LEDGER_FIELDS, EXPECTED_LEDGER[q], strict=True))


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


def algebra_ring(modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    return tuple(sorted(algebra_matrix(a, b, q) for a in range(q) for b in range(q)))


def brute_commutant(modulus: int) -> tuple[Matrix2, ...]:
    q = locked_modulus(modulus)
    matrix = matrix_mod(CAT_MATRIX, q)
    return tuple(
        item
        for item in all_matrices(q)
        if matrix_multiply(item, matrix, q) == matrix_multiply(matrix, item, q)
    )


def exact_additive_order(vector: Vector2, modulus: int) -> int:
    q = locked_modulus(modulus)
    return q // gcd(q, vector[0], vector[1])


def exact_order_shell(modulus: int) -> tuple[Vector2, ...]:
    q = locked_modulus(modulus)
    return tuple(
        (x, y)
        for x in range(q)
        for y in range(q)
        if exact_additive_order((x, y), q) == q
    )


def cyclic_delta(vector: Vector2, modulus: int) -> int:
    q = locked_modulus(modulus)
    image = matrix_vector(matrix_mod(CAT_MATRIX, q), vector, q)
    return (vector[0] * image[1] - vector[1] * image[0]) % q


def cyclic_locus(modulus: int) -> tuple[Vector2, ...]:
    q = locked_modulus(modulus)
    return tuple(
        (x, y)
        for x in range(q)
        for y in range(q)
        if is_unit(cyclic_delta((x, y), q), q)
    )


def canonical_orbit(points: Iterable[Vector2]) -> tuple[Vector2, ...]:
    return tuple(sorted(set(points)))


def group_orbits(
    group: tuple[Matrix2, ...], points: tuple[Vector2, ...], modulus: int
) -> tuple[tuple[Vector2, ...], ...]:
    q = locked_modulus(modulus)
    point_set = set(points)
    unseen = set(points)
    records: list[tuple[Vector2, ...]] = []
    while unseen:
        base = min(unseen)
        orbit = canonical_orbit(matrix_vector(matrix, base, q) for matrix in group)
        if not set(orbit).issubset(point_set):
            raise RuntimeError("group action left the declared point set")
        records.append(orbit)
        unseen.difference_update(orbit)
    return tuple(sorted(records, key=lambda orbit: orbit[0]))


def cyclic_map_orbits(points: tuple[Vector2, ...], modulus: int) -> tuple[tuple[Vector2, ...], ...]:
    q = locked_modulus(modulus)
    matrix = matrix_mod(CAT_MATRIX, q)
    point_set = set(points)
    unseen = set(points)
    records: list[tuple[Vector2, ...]] = []
    while unseen:
        start = min(unseen)
        current = start
        orbit: list[Vector2] = []
        while current not in orbit:
            if current not in point_set:
                raise RuntimeError("cat map left the declared point set")
            orbit.append(current)
            current = matrix_vector(matrix, current, q)
        if current != start:
            raise RuntimeError("finite permutation orbit failed to close at its start")
        canonical = canonical_orbit(orbit)
        records.append(canonical)
        unseen.difference_update(canonical)
    return tuple(sorted(records, key=lambda orbit: orbit[0]))


def matrix_order(modulus: int) -> int:
    q = locked_modulus(modulus)
    matrix = matrix_mod(CAT_MATRIX, q)
    current = matrix_mod(IDENTITY, q)
    for exponent in range(1, q ** 4 + 1):
        current = matrix_multiply(current, matrix, q)
        if current == matrix_mod(IDENTITY, q):
            return exponent
    raise RuntimeError("matrix order exceeded frozen finite ambient bound")


def quotient_transition(
    orbits: tuple[tuple[Vector2, ...], ...], modulus: int
) -> dict[str, Any]:
    q = locked_modulus(modulus)
    matrix = matrix_mod(CAT_MATRIX, q)
    index = {point: position for position, orbit in enumerate(orbits) for point in orbit}
    transition = [index[matrix_vector(matrix, orbit[0], q)] for orbit in orbits]
    identity = transition == list(range(len(orbits)))
    return {"class_count": len(orbits), "transition": transition, "identity": identity}


def delta_fibers(points: tuple[Vector2, ...], modulus: int) -> tuple[dict[str, Any], ...]:
    q = locked_modulus(modulus)
    fibers: dict[int, list[Vector2]] = {}
    for point in points:
        fibers.setdefault(cyclic_delta(point, q), []).append(point)
    return tuple(
        {"delta": value, "points": canonical_orbit(fibers[value])}
        for value in sorted(fibers)
    )


def rational_record(numerator: int, denominator: int) -> dict[str, Any]:
    value = Fraction(numerator, denominator)
    text = str(value.numerator) if value.denominator == 1 else (
        str(value.numerator) + "/" + str(value.denominator)
    )
    return {"numerator": value.numerator, "denominator": value.denominator, "text": text}


def _group_closed(group: tuple[Matrix2, ...], modulus: int) -> bool:
    q = locked_modulus(modulus)
    group_set = set(group)
    return matrix_mod(IDENTITY, q) in group_set and all(
        matrix_multiply(left, right, q) in group_set
        for left in group
        for right in group
    )


def reversing_certificate(
    modulus: int,
    full_centralizer: tuple[Matrix2, ...],
    shell: tuple[Vector2, ...],
    cyclic: tuple[Vector2, ...],
) -> dict[str, Any] | None:
    q = locked_modulus(modulus)
    if q not in LOCKED_PRIMES:
        return None
    matrix = matrix_mod(CAT_MATRIX, q)
    inverse = matrix_mod(((1, -1), (-1, 2)), q)
    reversor = matrix_mod(REVERSOR, q)
    coset = tuple(matrix_multiply(reversor, item, q) for item in full_centralizer)
    constructed = tuple(sorted(set(full_centralizer).union(coset)))
    brute = tuple(
        item
        for item in all_matrices(q)
        if is_unit(determinant(item, q), q)
        and (
            matrix_multiply(item, matrix, q) == matrix_multiply(matrix, item, q)
            or matrix_multiply(item, matrix, q) == matrix_multiply(inverse, item, q)
        )
    )
    orbits = group_orbits(constructed, shell, q)
    cyclic_set = set(cyclic)
    mixing = any(
        bool(cyclic_set.intersection(orbit)) and bool(set(orbit).difference(cyclic_set))
        for orbit in orbits
    )
    return {
        "constructed_group": constructed,
        "brute_reversing_group": brute,
        "constructed_equals_brute": constructed == brute,
        "group_closed": _group_closed(constructed, q),
        "reversor_relation": matrix_multiply(reversor, matrix, q)
        == matrix_multiply(inverse, reversor, q),
        "shell_orbits": orbits,
        "shell_orbit_count": len(orbits),
        "cyclic_noncyclic_mixing": mixing,
    }


def direct_engine(modulus: int) -> dict[str, Any]:
    q = locked_modulus(modulus)
    commutant = brute_commutant(q)
    full = tuple(item for item in commutant if is_unit(determinant(item, q), q))
    symplectic = tuple(item for item in full if determinant(item, q) == 1 % q)
    shell = exact_order_shell(q)
    cyclic = cyclic_locus(q)
    discard = tuple(sorted(set(shell).difference(cyclic)))
    a_orbits = cyclic_map_orbits(cyclic, q)
    full_cv_orbits = group_orbits(full, cyclic, q)
    symplectic_cv_orbits = group_orbits(symplectic, cyclic, q)
    full_shell_orbits = group_orbits(full, shell, q)
    symplectic_shell_orbits = group_orbits(symplectic, shell, q)
    reversing = reversing_certificate(q, full, shell, cyclic)
    return {
        "engine": "DIRECT_MATRIX_VECTOR_ENUMERATION",
        "q": q,
        "commutant": commutant,
        "full_centralizer": full,
        "symplectic_centralizer": symplectic,
        "exact_order_shell": shell,
        "cyclic_locus": cyclic,
        "discarded_shell": discard,
        "cyclic_additive_orders": tuple(exact_additive_order(point, q) for point in cyclic),
        "A_order": matrix_order(q),
        "cyclic_A_orbits": a_orbits,
        "full_CV_orbits": full_cv_orbits,
        "symplectic_CV_orbits": symplectic_cv_orbits,
        "full_shell_orbits": full_shell_orbits,
        "symplectic_shell_orbits": symplectic_shell_orbits,
        "full_quotient_transition": quotient_transition(full_cv_orbits, q),
        "symplectic_quotient_transition": quotient_transition(symplectic_cv_orbits, q),
        "delta_fibers": delta_fibers(cyclic, q),
        "norm_image_from_determinants": tuple(sorted({determinant(item, q) for item in full})),
        "reversing": reversing,
    }


def torsor_axioms(
    full: tuple[Matrix2, ...], cyclic: tuple[Vector2, ...], modulus: int
) -> dict[str, bool]:
    q = locked_modulus(modulus)
    cyclic_set = set(cyclic)
    orbit_sets = [
        {matrix_vector(matrix, point, q) for matrix in full}
        for point in cyclic
    ]
    stabilizer_sizes = [
        sum(matrix_vector(matrix, point, q) == point for matrix in full)
        for point in cyclic
    ]
    image = tuple(sorted(matrix_vector(matrix, BASE_VECTOR, q) for matrix in full))
    return {
        "closure": all(orbit.issubset(cyclic_set) for orbit in orbit_sets),
        "free": all(size == 1 for size in stabilizer_sizes),
        "transitive": all(orbit == cyclic_set for orbit in orbit_sets),
        "base_map_bijective": image == cyclic and len(image) == len(set(image)),
    }


def algebra_engine(modulus: int) -> dict[str, Any]:
    q = locked_modulus(modulus)
    entries = tuple((a, b) for a in range(q) for b in range(q))
    norm_table = tuple(
        {
            "a": a,
            "b": b,
            "matrix": algebra_matrix(a, b, q),
            "matrix_determinant": determinant(algebra_matrix(a, b, q), q),
            "algebra_norm": algebra_norm(a, b, q),
        }
        for a, b in entries
    )
    ring = tuple(sorted(record["matrix"] for record in norm_table))
    units = tuple(
        sorted(record["matrix"] for record in norm_table if is_unit(record["algebra_norm"], q))
    )
    norm_one = tuple(item for item in units if determinant(item, q) == 1 % q)
    torsor_image = tuple(sorted(matrix_vector(item, BASE_VECTOR, q) for item in units))
    cyclic = cyclic_locus(q)
    axioms = torsor_axioms(units, cyclic, q)
    norm_image = tuple(sorted({determinant(item, q) for item in units}))
    fiber_orbits = group_orbits(norm_one, cyclic, q)
    fiber_sets = tuple(sorted(canonical_orbit(record["points"]) for record in delta_fibers(cyclic, q)))
    return {
        "engine": "QUADRATIC_ALGEBRA_TORSOR",
        "q": q,
        "algebra_entries": entries,
        "norm_table": norm_table,
        "ring_matrices": ring,
        "unit_matrices": units,
        "norm_one_matrices": norm_one,
        "torsor_image": torsor_image,
        "torsor_axioms": axioms,
        "matrix_det_equals_norm": all(
            record["matrix_determinant"] == record["algebra_norm"] for record in norm_table
        ),
        "norm_image": norm_image,
        "norm_fiber_orbits": fiber_orbits,
        "delta_fibers_equal_norm_one_orbits": tuple(sorted(fiber_orbits)) == fiber_sets,
    }


def ledger_projection(
    direct: dict[str, Any], algebra: dict[str, Any], modulus: int
) -> dict[str, Any]:
    q = locked_modulus(modulus)
    expected = expected_record(q)
    reversing = direct["reversing"]
    shell_size = len(direct["exact_order_shell"])
    cyclic_size = len(direct["cyclic_locus"])
    return {
        "case": expected["case"],
        "exact_shell_size": shell_size,
        "cyclic_locus_size": cyclic_size,
        "discard_size": len(direct["discarded_shell"]),
        "full_centralizer_size": len(direct["full_centralizer"]),
        "symplectic_centralizer_size": len(direct["symplectic_centralizer"]),
        "A_order": direct["A_order"],
        "cyclic_A_orbit_count": len(direct["cyclic_A_orbits"]),
        "full_CV_quotient_count": len(direct["full_CV_orbits"]),
        "symplectic_CV_quotient_count": len(direct["symplectic_CV_orbits"]),
        "full_centralizer_shell_orbits": len(direct["full_shell_orbits"]),
        "symplectic_centralizer_shell_orbits": len(direct["symplectic_shell_orbits"]),
        "prime_reversing_group_shell_orbits": (
            None if reversing is None else reversing["shell_orbit_count"]
        ),
        "retained_fraction": rational_record(cyclic_size, shell_size),
        "discarded_fraction": rational_record(shell_size - cyclic_size, shell_size),
        "norm_image_size": len(algebra["norm_image"]),
    }


def audit_modulus(modulus: int) -> dict[str, Any]:
    q = locked_modulus(modulus)
    direct = direct_engine(q)
    algebra = algebra_engine(q)
    projection = ledger_projection(direct, algebra, q)
    expected = expected_record(q)
    exact_projection = {key: projection[key] for key in LEDGER_FIELDS}
    dual_checks = {
        "commutant_equals_algebra_ring": direct["commutant"] == algebra["ring_matrices"],
        "full_centralizer_equals_algebra_units": direct["full_centralizer"]
        == algebra["unit_matrices"],
        "symplectic_equals_norm_one": direct["symplectic_centralizer"]
        == algebra["norm_one_matrices"],
        "cyclic_locus_equals_torsor_image": direct["cyclic_locus"] == algebra["torsor_image"],
        "matrix_det_equals_norm": algebra["matrix_det_equals_norm"],
        "norm_images_match": direct["norm_image_from_determinants"] == algebra["norm_image"],
        "delta_fibers_equal_symplectic_orbits": algebra["delta_fibers_equal_norm_one_orbits"],
        "every_cyclic_vector_has_exact_order_q": all(
            value == q for value in direct["cyclic_additive_orders"]
        ),
        "torsor_closure": algebra["torsor_axioms"]["closure"],
        "torsor_free": algebra["torsor_axioms"]["free"],
        "torsor_transitive": algebra["torsor_axioms"]["transitive"],
        "torsor_base_map_bijective": algebra["torsor_axioms"]["base_map_bijective"],
        "full_quotient_action_identity": direct["full_quotient_transition"]["identity"],
        "symplectic_quotient_action_identity": direct["symplectic_quotient_transition"]["identity"],
        "reversing_group_exact_and_no_mixing": direct["reversing"] is None or (
            direct["reversing"]["constructed_equals_brute"]
            and direct["reversing"]["group_closed"]
            and direct["reversing"]["reversor_relation"]
            and not direct["reversing"]["cyclic_noncyclic_mixing"]
        ),
    }
    return {
        "q": q,
        "expected": expected,
        "ledger": projection,
        "frozen_expected_match": exact_projection == expected,
        "dual_checks": dual_checks,
        "direct_engine": direct,
        "algebra_engine": algebra,
        "pass": exact_projection == expected and all(dual_checks.values()),
    }
