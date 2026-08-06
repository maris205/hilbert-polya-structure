"""Known-truth controls used before interpreting Hénon computations."""

from __future__ import annotations

from math import isqrt

import numpy as np
from numpy.typing import NDArray


def cat_matrix() -> NDArray[np.int64]:
    """Return the standard hyperbolic cat-map matrix in SL(2,Z)."""

    return np.array([[2, 1], [1, 1]], dtype=np.int64)


def divisors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    values: set[int] = set()
    for candidate in range(1, isqrt(n) + 1):
        if n % candidate == 0:
            values.add(candidate)
            values.add(n // candidate)
    return tuple(sorted(values))


def mobius(n: int) -> int:
    """Return the Möbius function for a positive integer."""

    if n < 1:
        raise ValueError("n must be positive")
    remaining = n
    prime_count = 0
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            prime_count += 1
            if remaining % factor == 0:
                return 0
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def cat_fixed_point_count(period: int) -> int:
    """Return |det(A^period-I)| for the standard cat map."""

    if period < 1:
        raise ValueError("period must be positive")
    matrix_power = np.linalg.matrix_power(cat_matrix().astype(object), period)
    shifted = matrix_power - np.eye(2, dtype=object)
    determinant = shifted[0, 0] * shifted[1, 1] - shifted[0, 1] * shifted[1, 0]
    return abs(int(determinant))


def cat_primitive_orbit_count(period: int) -> int:
    """Return the number of primitive cat-map orbits of exact period n."""

    numerator = sum(
        mobius(period // divisor) * cat_fixed_point_count(divisor)
        for divisor in divisors(period)
    )
    quotient, remainder = divmod(numerator, period)
    if remainder:
        raise ArithmeticError("primitive orbit count failed integrality check")
    return quotient


def pcf_w2_zeta_coefficients(max_degree: int) -> tuple[int, ...]:
    """Coefficients of (1+z)/(1-2z^2) through max_degree."""

    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    return tuple(2 ** (degree // 2) for degree in range(max_degree + 1))


def real_periodic_coordinate_bound(a: float) -> float:
    """Return the a-priori coordinate bound for a real periodic orbit."""

    a_abs = abs(float(a))
    if a_abs == 0.0:
        return float("inf")
    return (1.0 + np.sqrt(1.0 + a_abs)) / a_abs


def analytic_period2(a: float) -> tuple[tuple[float, float], ...]:
    """Return the unique real primitive period-2 orbit when a > 3."""

    a_float = float(a)
    if a_float <= 3.0:
        return ()
    root = np.sqrt(a_float - 3.0)
    p = (1.0 + root) / a_float
    q = (1.0 - root) / a_float
    return ((float(p), float(q)),)


def analytic_period2_trace(a: float) -> float:
    """Return the primitive period-2 monodromy trace 14-4a."""

    return 14.0 - 4.0 * float(a)


def analytic_period3(a: float) -> tuple[tuple[float, float, float], ...]:
    """Return the two real primitive period-3 orbits when a > 1."""

    a_float = float(a)
    if a_float <= 1.0:
        return ()
    root = np.sqrt(a_float - 1.0)
    records = []
    for sign in (1.0, -1.0):
        p = sign * root / a_float
        q = (1.0 - sign * root) / a_float
        records.append((float(p), float(p), float(q)))
    return tuple(records)


def analytic_period3_traces(a: float) -> tuple[float, ...]:
    """Return the two primitive period-3 monodromy traces when a > 1."""

    a_float = float(a)
    if a_float <= 1.0:
        return ()
    root = np.sqrt(a_float - 1.0)
    return tuple(
        10.0 - 8.0 * a_float + sign * (8.0 * a_float - 6.0) * root
        for sign in (1.0, -1.0)
    )


def control_certificate(max_period: int = 12) -> dict[str, object]:
    """Return exact cat-map and PCF control tables."""

    cat_rows = [
        {
            "period": period,
            "fixed_points": cat_fixed_point_count(period),
            "primitive_orbits": cat_primitive_orbit_count(period),
        }
        for period in range(1, max_period + 1)
    ]
    return {
        "cat_map_matrix": cat_matrix().tolist(),
        "cat_map_determinant": int(round(np.linalg.det(cat_matrix()))),
        "cat_map_periods": cat_rows,
        "pcf_w2_zeta": "(1+z)/(1-2*z^2)",
        "pcf_w2_coefficients": list(pcf_w2_zeta_coefficients(max_period)),
        "henon_analytic_checks": {
            "period2_exists_for": "a > 3",
            "period2_trace": "14-4*a",
            "period3_exists_for": "a > 1",
            "period3_traces": "10-8*a +/- (8*a-6)*sqrt(a-1)",
            "generic_complex_fixed_points_of_Hn": "2^n counted with multiplicity",
        },
    }
