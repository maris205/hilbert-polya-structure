"""Exact finite-field period, kernel, and modulo-five Jordan certificates."""

from __future__ import annotations

from collections import Counter
from typing import Any

from .algebra import CAT_MATRIX, IDENTITY, LOCKED_SUPPORT, Matrix2, matrix_power


Vector2 = tuple[int, int]
EXPECTED_PERIOD_PROFILES = {
    2: {3: 3},
    3: {4: 8},
    5: {2: 4, 10: 20},
    7: {8: 48},
    11: {5: 120},
    19: {9: 360},
    29: {7: 840},
    199: {11: 39600},
}


def _field_modulus(value: int) -> int:
    if type(value) is not int or value not in LOCKED_SUPPORT:
        raise ValueError("field modulus must be one of the frozen support primes")
    return value


def matrix_mod(matrix: Matrix2, modulus: int) -> Matrix2:
    modulus = _field_modulus(modulus)
    return (
        (matrix[0][0] % modulus, matrix[0][1] % modulus),
        (matrix[1][0] % modulus, matrix[1][1] % modulus),
    )


def matrix_vector_mod(matrix: Matrix2, vector: Vector2, modulus: int) -> Vector2:
    modulus = _field_modulus(modulus)
    return (
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % modulus,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % modulus,
    )


def subtract_mod(left: Matrix2, right: Matrix2, modulus: int) -> Matrix2:
    modulus = _field_modulus(modulus)
    return (
        ((left[0][0] - right[0][0]) % modulus, (left[0][1] - right[0][1]) % modulus),
        ((left[1][0] - right[1][0]) % modulus, (left[1][1] - right[1][1]) % modulus),
    )


def rank_mod(matrix: Matrix2, modulus: int) -> int:
    modulus = _field_modulus(modulus)
    entries = [entry % modulus for row in matrix for entry in row]
    if not any(entries):
        return 0
    determinant = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % modulus
    return 2 if determinant else 1


def vector_period(
    matrix: Matrix2, modulus: int, vector: Vector2, *, maximum_period: int = 12
) -> int:
    modulus = _field_modulus(modulus)
    if type(maximum_period) is not int or maximum_period < 1 or maximum_period > 12:
        raise ValueError("finite-field period cutoff must lie in 1 through 12")
    normalized = (vector[0] % modulus, vector[1] % modulus)
    if normalized == (0, 0):
        raise ValueError("zero vector has no prime-order carrier role")
    current = normalized
    for period in range(1, maximum_period + 1):
        current = matrix_vector_mod(matrix, current, modulus)
        if current == normalized:
            return period
    raise RuntimeError("vector period exceeds the source-locked cutoff")


def enumerate_period_profile(modulus: int) -> dict[int, int]:
    """Enumerate nonzero vectors only for a frozen determinant-support prime."""

    modulus = _field_modulus(modulus)
    counts: Counter[int] = Counter()
    for first in range(modulus):
        for second in range(modulus):
            if first == 0 and second == 0:
                continue
            counts[vector_period(CAT_MATRIX, modulus, (first, second))] += 1
    return dict(sorted(counts.items()))


def kernel_vectors(period: int, modulus: int) -> list[Vector2]:
    modulus = _field_modulus(modulus)
    if type(period) is not int or period < 1 or period > 12:
        raise ValueError("kernel period must lie in 1 through 12")
    operator = subtract_mod(matrix_mod(matrix_power(CAT_MATRIX, period), modulus), IDENTITY, modulus)
    vectors: list[Vector2] = []
    for first in range(modulus):
        for second in range(modulus):
            vector = (first, second)
            if vector != (0, 0) and matrix_vector_mod(operator, vector, modulus) == (0, 0):
                vectors.append(vector)
    return vectors


def primitive_kernel_certificate(period: int, modulus: int) -> dict[str, Any]:
    """Cross-check the source-locked primitive-divisor-to-exact-period bridge."""

    vectors = kernel_vectors(period, modulus)
    exact = [vector_period(CAT_MATRIX, modulus, vector) for vector in vectors]
    operator = subtract_mod(matrix_mod(matrix_power(CAT_MATRIX, period), modulus), IDENTITY, modulus)
    dimension = 2 - rank_mod(operator, modulus)
    expected_count = modulus**dimension - 1
    return {
        "period": period,
        "prime": modulus,
        "kernel_dimension": dimension,
        "nonzero_kernel_count": len(vectors),
        "expected_nonzero_kernel_count": expected_count,
        "exact_periods": sorted(set(exact)),
        "cycle_count": len(vectors) // period,
        "pass": bool(vectors) and len(vectors) == expected_count and set(exact) == {period},
    }


def jordan_mod5_certificate() -> dict[str, Any]:
    modulus = 5
    reduced = matrix_mod(CAT_MATRIX, modulus)
    negative_identity = ((4, 0), (0, 4))
    nilpotent = subtract_mod(reduced, negative_identity, modulus)
    nilpotent_square = matrix_mod(
        (
            (
                nilpotent[0][0] * nilpotent[0][0] + nilpotent[0][1] * nilpotent[1][0],
                nilpotent[0][0] * nilpotent[0][1] + nilpotent[0][1] * nilpotent[1][1],
            ),
            (
                nilpotent[1][0] * nilpotent[0][0] + nilpotent[1][1] * nilpotent[1][0],
                nilpotent[1][0] * nilpotent[0][1] + nilpotent[1][1] * nilpotent[1][1],
            ),
        ),
        modulus,
    )
    profile = enumerate_period_profile(modulus)
    kernel_nonzero = sum(
        1
        for first in range(modulus)
        for second in range(modulus)
        if (first, second) != (0, 0)
        and matrix_vector_mod(nilpotent, (first, second), modulus) == (0, 0)
    )
    checks = {
        "A_equals_minus_I_plus_N": reduced == ((2, 1), (1, 1)),
        "N_nonzero": nilpotent != ((0, 0), (0, 0)),
        "N_square_zero": nilpotent_square == ((0, 0), (0, 0)),
        "N_rank_one": rank_mod(nilpotent, modulus) == 1,
        "four_nonzero_kernel_vectors": kernel_nonzero == 4,
        "period_profile_2_and_10": profile == EXPECTED_PERIOD_PROFILES[5],
        "twenty_period_ten_points": profile.get(10) == 20,
        "two_period_ten_cycles": profile.get(10, 0) // 10 == 2,
    }
    return {
        "prime": 5,
        "nilpotent": [list(row) for row in nilpotent],
        "period_profile": {str(key): value for key, value in profile.items()},
        "checks": checks,
        "pass": all(checks.values()),
    }


def boundary_profiles() -> dict[str, Any]:
    records = []
    for modulus in (2, 3, 5):
        profile = enumerate_period_profile(modulus)
        records.append(
            {
                "prime": modulus,
                "period_profile": {str(key): value for key, value in profile.items()},
                "expected": {
                    str(key): value for key, value in EXPECTED_PERIOD_PROFILES[modulus].items()
                },
                "pass": profile == EXPECTED_PERIOD_PROFILES[modulus],
            }
        )
    jordan = jordan_mod5_certificate()
    return {
        "records": records,
        "jordan_mod_5": jordan,
        "period_6_carriers": 0,
        "period_12_carriers": 0,
        "pass": all(record["pass"] for record in records) and jordan["pass"],
    }
