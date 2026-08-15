"""Two independent exact engines for the five frozen prime shells."""

from __future__ import annotations

from collections import Counter
from typing import Any, Iterable

from .constants import CAT_MATRIX, EXPECTED_LEDGER, IDENTITY, LOCKED_PRIMES


Matrix2 = tuple[tuple[int, int], tuple[int, int]]
Vector2 = tuple[int, int]


def locked_prime(value: int) -> int:
    if type(value) is not int or value not in LOCKED_PRIMES:
        raise ValueError("prime must be one of the five source-locked controls")
    return value


def matrix_mod(matrix: Matrix2, prime: int) -> Matrix2:
    p = locked_prime(prime)
    return (
        (matrix[0][0] % p, matrix[0][1] % p),
        (matrix[1][0] % p, matrix[1][1] % p),
    )


def matrix_multiply(left: Matrix2, right: Matrix2, prime: int) -> Matrix2:
    p = locked_prime(prime)
    return (
        (
            (left[0][0] * right[0][0] + left[0][1] * right[1][0]) % p,
            (left[0][0] * right[0][1] + left[0][1] * right[1][1]) % p,
        ),
        (
            (left[1][0] * right[0][0] + left[1][1] * right[1][0]) % p,
            (left[1][0] * right[0][1] + left[1][1] * right[1][1]) % p,
        ),
    )


def matrix_power(matrix: Matrix2, exponent: int, prime: int) -> Matrix2:
    p = locked_prime(prime)
    if type(exponent) is not int or exponent < 0:
        raise ValueError("matrix exponent must be a nonnegative integer")
    result = matrix_mod(IDENTITY, p)
    base = matrix_mod(matrix, p)
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = matrix_multiply(result, base, p)
        base = matrix_multiply(base, base, p)
        remaining //= 2
    return result


def matrix_vector(matrix: Matrix2, vector: Vector2, prime: int) -> Vector2:
    p = locked_prime(prime)
    return (
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % p,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % p,
    )


def matrix_subtract(left: Matrix2, right: Matrix2, prime: int) -> Matrix2:
    p = locked_prime(prime)
    return (
        ((left[0][0] - right[0][0]) % p, (left[0][1] - right[0][1]) % p),
        ((left[1][0] - right[1][0]) % p, (left[1][1] - right[1][1]) % p),
    )


def determinant(matrix: Matrix2, prime: int) -> int:
    p = locked_prime(prime)
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % p


def rank(matrix: Matrix2, prime: int) -> int:
    p = locked_prime(prime)
    reduced = matrix_mod(matrix, p)
    if reduced == ((0, 0), (0, 0)):
        return 0
    return 2 if determinant(reduced, p) else 1


def nonzero_vectors(prime: int) -> tuple[Vector2, ...]:
    p = locked_prime(prime)
    return tuple(
        (first, second)
        for first in range(p)
        for second in range(p)
        if (first, second) != (0, 0)
    )


def canonical_cycle(cycle: Iterable[Vector2]) -> tuple[Vector2, ...]:
    values = tuple(cycle)
    if not values:
        raise ValueError("a primitive cycle may not be empty")
    rotations = tuple(values[index:] + values[:index] for index in range(len(values)))
    return min(rotations)


def direct_orbits(prime: int) -> tuple[tuple[Vector2, ...], ...]:
    """Enumerate the exact permutation cycles, without using case formulas."""

    p = locked_prime(prime)
    unseen = set(nonzero_vectors(p))
    cycles: list[tuple[Vector2, ...]] = []
    while unseen:
        start = min(unseen)
        orbit: list[Vector2] = []
        local: set[Vector2] = set()
        current = start
        while current not in local:
            if current == (0, 0) or current not in unseen:
                raise RuntimeError("matrix action failed to produce a disjoint shell cycle")
            local.add(current)
            orbit.append(current)
            current = matrix_vector(CAT_MATRIX, current, p)
        if current != start:
            raise RuntimeError("cycle did not close at its canonical starting point")
        for vector in local:
            unseen.remove(vector)
        cycles.append(canonical_cycle(tuple(orbit)))
    return tuple(sorted(cycles))


def is_eigenvector(vector: Vector2, prime: int) -> bool:
    p = locked_prime(prime)
    image = matrix_vector(CAT_MATRIX, vector, p)
    return (vector[0] * image[1] - vector[1] * image[0]) % p == 0


def direct_enumeration_certificate(prime: int) -> dict[str, Any]:
    p = locked_prime(prime)
    cycles = direct_orbits(p)
    cycle_counter = Counter(len(cycle) for cycle in cycles)
    point_counter = Counter()
    for length, count in cycle_counter.items():
        point_counter[length] = length * count
    eigenline_cycles: int | None = None
    off_eigenline_cycles: int | None = None
    if p == 11:
        eigenline_cycles = sum(is_eigenvector(cycle[0], p) for cycle in cycles)
        off_eigenline_cycles = len(cycles) - eigenline_cycles
    flattened = [vector for cycle in cycles for vector in cycle]
    return {
        "engine": "DIRECT_POINT_PERMUTATION",
        "prime": p,
        "shell_cardinality": p * p - 1,
        "point_period_profile": dict(sorted(point_counter.items())),
        "cycle_profile": dict(sorted(cycle_counter.items())),
        "m_p": len(cycles),
        "eigenline_cycles": eigenline_cycles,
        "off_eigenline_cycles": off_eigenline_cycles,
        "canonical_cycles": [[list(vector) for vector in cycle] for cycle in cycles],
        "partition_exact": len(flattened) == p * p - 1
        and len(set(flattened)) == p * p - 1,
    }


def matrix_order(prime: int, upper_bound: int) -> int:
    p = locked_prime(prime)
    if type(upper_bound) is not int or upper_bound < 1 or upper_bound > p * p - 1:
        raise ValueError("matrix-order bound is outside the frozen shell")
    reduced_identity = matrix_mod(IDENTITY, p)
    current = reduced_identity
    reduced_matrix = matrix_mod(CAT_MATRIX, p)
    for exponent in range(1, upper_bound + 1):
        current = matrix_multiply(current, reduced_matrix, p)
        if current == reduced_identity:
            return exponent
    raise RuntimeError("matrix order violates the source-locked case bound")


def legendre_five(prime: int) -> int:
    p = locked_prime(prime)
    if p in (2, 5):
        raise ValueError("Legendre classification is only for odd unramified rows")
    residue = pow(5, (p - 1) // 2, p)
    if residue == 1:
        return 1
    if residue == p - 1:
        return -1
    raise RuntimeError("Euler criterion returned neither split nor inert")


def analytic_case_certificate(prime: int) -> dict[str, Any]:
    """Derive the row from the finite-field case proof, never from point orbits."""

    p = locked_prime(prime)
    base: dict[str, Any] = {
        "engine": "ANALYTIC_CASE_CLASSIFICATION",
        "prime": p,
        "shell_cardinality": p * p - 1,
        "eigenline_cycles": None,
        "off_eigenline_cycles": None,
    }
    if p == 2:
        tau = matrix_order(p, 3)
        base.update(
            {
                "case": "binary_inert",
                "tau_p": tau,
                "tau_divides": "p+1",
                "divisibility_pass": (p + 1) % tau == 0,
                "point_period_profile": {tau: p * p - 1},
                "cycle_profile": {tau: (p * p - 1) // tau},
                "m_p": (p * p - 1) // tau,
                "case_checks": {"cayley_hamilton_order_three": tau == 3},
            }
        )
        return base
    if p == 5:
        negative_identity = ((p - 1, 0), (0, p - 1))
        nilpotent = matrix_subtract(matrix_mod(CAT_MATRIX, p), negative_identity, p)
        square = matrix_multiply(nilpotent, nilpotent, p)
        kernel_size = sum(
            matrix_vector(nilpotent, vector, p) == (0, 0)
            for vector in ((a, b) for a in range(p) for b in range(p))
        )
        checks = {
            "A_equals_minus_I_plus_N": matrix_mod(CAT_MATRIX, p)
            == matrix_mod(
                (
                    (negative_identity[0][0] + nilpotent[0][0], nilpotent[0][1]),
                    (nilpotent[1][0], negative_identity[1][1] + nilpotent[1][1]),
                ),
                p,
            ),
            "N_square_zero": square == ((0, 0), (0, 0)),
            "N_rank_one": rank(nilpotent, p) == 1,
            "kernel_size_five": kernel_size == 5,
        }
        short_period = 2
        long_period = 2 * p
        kernel_nonzero = kernel_size - 1
        outside_kernel = p * p - kernel_size
        point_profile = {short_period: kernel_nonzero, long_period: outside_kernel}
        cycle_profile = {
            short_period: kernel_nonzero // short_period,
            long_period: outside_kernel // long_period,
        }
        base.update(
            {
                "case": "ramified",
                "tau_p": None,
                "tau_divides": None,
                "divisibility_pass": None,
                "point_period_profile": point_profile,
                "cycle_profile": cycle_profile,
                "m_p": sum(cycle_profile.values()),
                "nilpotent": [list(row) for row in nilpotent],
                "case_checks": checks,
            }
        )
        return base
    symbol = legendre_five(p)
    case = "split" if symbol == 1 else "inert"
    divisor = p - 1 if case == "split" else p + 1
    tau = matrix_order(p, divisor)
    h_p = divisor // tau
    m_p = (p * p - 1) // tau
    if case == "split":
        eigenline_cycles = 2 * h_p
        off_eigenline_cycles = (p - 1) * h_p
    else:
        eigenline_cycles = None
        off_eigenline_cycles = None
    base.update(
        {
            "case": case,
            "legendre_five": symbol,
            "tau_p": tau,
            "tau_divides": "p-1" if case == "split" else "p+1",
            "divisibility_pass": divisor % tau == 0,
            "h_p": h_p,
            "point_period_profile": {tau: p * p - 1},
            "cycle_profile": {tau: m_p},
            "m_p": m_p,
            "eigenline_cycles": eigenline_cycles,
            "off_eigenline_cycles": off_eigenline_cycles,
            "case_checks": {
                "uniform_period_formula": m_p * tau == p * p - 1,
                "odd_lower_bound": m_p >= p - 1,
            },
        }
    )
    return base


def comparison_projection(record: dict[str, Any]) -> dict[str, Any]:
    return {
        key: record[key]
        for key in (
            "prime",
            "shell_cardinality",
            "point_period_profile",
            "cycle_profile",
            "m_p",
            "eigenline_cycles",
            "off_eigenline_cycles",
        )
    }


def expected_projection(prime: int) -> dict[str, Any]:
    p = locked_prime(prime)
    row = EXPECTED_LEDGER[p]
    return {
        "prime": p,
        "shell_cardinality": p * p - 1,
        "point_period_profile": row["point_period_profile"],
        "cycle_profile": row["cycle_profile"],
        "m_p": row["m_p"],
        "eigenline_cycles": row["eigenline_cycles"],
        "off_eigenline_cycles": row["off_eigenline_cycles"],
    }
