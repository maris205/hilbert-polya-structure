"""Finite weighted Euler products and cycle coefficients."""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
from numpy.typing import NDArray

from .orbits import OrbitRecord


ComplexArray = NDArray[np.complex128]


def orbit_weight(record: OrbitRecord, beta: float) -> float:
    """Return |Lambda_u|^{-beta} for a hyperbolic orbit."""

    if record.stability != "hyperbolic":
        raise ValueError(f"orbit {record.orbit_id} is not hyperbolic")
    unstable = max(abs(record.multiplier_large), abs(record.multiplier_small))
    if unstable <= 1.0:
        raise ValueError(f"orbit {record.orbit_id} lacks an unstable multiplier")
    return float(unstable ** (-float(beta)))


def determinant_coefficients(
    records: Iterable[OrbitRecord],
    max_degree: int,
    beta: float,
) -> ComplexArray:
    """Coefficients of product_p (1-w_p z^{n_p}) through max_degree."""

    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    coefficients = np.zeros(max_degree + 1, dtype=np.complex128)
    coefficients[0] = 1.0
    for record in records:
        if record.stability != "hyperbolic" or record.period > max_degree:
            continue
        weight = orbit_weight(record, beta)
        updated = coefficients.copy()
        updated[record.period:] -= weight * coefficients[:-record.period]
        coefficients = updated
    return coefficients


def zeta_coefficients(
    records: Iterable[OrbitRecord],
    max_degree: int,
    beta: float,
) -> ComplexArray:
    """Coefficients of product_p (1-w_p z^{n_p})^{-1}."""

    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    coefficients = np.zeros(max_degree + 1, dtype=np.complex128)
    coefficients[0] = 1.0
    for record in records:
        if record.stability != "hyperbolic" or record.period > max_degree:
            continue
        weight = orbit_weight(record, beta)
        updated = np.zeros_like(coefficients)
        for repetition in range(max_degree // record.period + 1):
            shift = repetition * record.period
            updated[shift:] += weight**repetition * coefficients[: max_degree + 1 - shift]
        coefficients = updated
    return coefficients


def log_zeta_coefficients(
    records: Iterable[OrbitRecord],
    max_degree: int,
    beta: float,
) -> ComplexArray:
    """Coefficients L_m in log Z(z)=sum_{m>=1} L_m z^m."""

    coefficients = np.zeros(max_degree + 1, dtype=np.complex128)
    for record in records:
        if record.stability != "hyperbolic" or record.period > max_degree:
            continue
        weight = orbit_weight(record, beta)
        for repetition in range(1, max_degree // record.period + 1):
            degree = repetition * record.period
            coefficients[degree] += weight**repetition / repetition
    return coefficients


def euler_log_derivative_coefficients(
    records: Iterable[OrbitRecord],
    max_degree: int,
    beta: float,
) -> ComplexArray:
    """Return m[z^m]log Z for the formal Euler product.

    These coefficients are not the flat traces of the smooth Perron--Frobenius
    operator; those require the |det(I-M_p^r)| denominator implemented below.
    """

    log_coefficients = log_zeta_coefficients(records, max_degree, beta)
    degrees = np.arange(max_degree + 1, dtype=float)
    return degrees * log_coefficients


def trace_coefficients(
    records: Iterable[OrbitRecord],
    max_degree: int,
    beta: float,
) -> ComplexArray:
    """Backward-compatible alias for Euler log-derivative coefficients."""

    return euler_log_derivative_coefficients(records, max_degree, beta)


def factor_poles(record: OrbitRecord, beta: float) -> tuple[complex, ...]:
    """Return poles contributed by one finite Euler factor."""

    weight = orbit_weight(record, beta)
    radius = weight ** (-1.0 / record.period)
    return tuple(
        radius * np.exp(2.0j * np.pi * branch / record.period)
        for branch in range(record.period)
    )


def leading_resonance_from_determinant(coefficients: ComplexArray) -> complex | None:
    """Return 1/z for the smallest-modulus nonzero root of a cycle polynomial."""

    trimmed = np.trim_zeros(np.asarray(coefficients, dtype=np.complex128), trim="b")
    if trimmed.size <= 1:
        return None
    roots = np.polynomial.polynomial.polyroots(trimmed)
    roots = roots[np.abs(roots) > 1.0e-12]
    if roots.size == 0:
        return None
    root = roots[int(np.argmin(np.abs(roots)))]
    return complex(1.0 / root)


def monodromy_trace_power(primitive_trace: float, repetition: int) -> float:
    """Return tr(M^r) for det(M)=1 using the Chebyshev recurrence."""

    if repetition < 0:
        raise ValueError("repetition must be nonnegative")
    if repetition == 0:
        return 2.0
    if repetition == 1:
        return float(primitive_trace)
    previous_previous = 2.0
    previous = float(primitive_trace)
    for _ in range(2, repetition + 1):
        current = float(primitive_trace) * previous - previous_previous
        previous_previous, previous = previous, current
    return previous


def perron_fixed_point_traces(
    records: Iterable[OrbitRecord],
    max_degree: int,
    singular_tolerance: float = 1.0e-12,
) -> FloatArray:
    """Return T_n=sum_{Fix f^n} 1/|det(I-Df^n)| from primitive orbits."""

    traces = np.zeros(max_degree + 1, dtype=float)
    for record in records:
        if record.period > max_degree or record.stability == "parabolic":
            continue
        for repetition in range(1, max_degree // record.period + 1):
            degree = repetition * record.period
            repeated_trace = monodromy_trace_power(record.trace, repetition)
            denominator = abs(2.0 - repeated_trace)
            if denominator <= singular_tolerance:
                raise ValueError(
                    f"orbit {record.orbit_id} has a near-singular repeated fixed point at degree {degree}"
                )
            traces[degree] += record.period / denominator
    return traces


def perron_fredholm_coefficients(
    records: Iterable[OrbitRecord],
    max_degree: int,
    singular_tolerance: float = 1.0e-12,
) -> ComplexArray:
    """Coefficients of exp(-sum_n T_n z^n/n) through max_degree."""

    traces = perron_fixed_point_traces(records, max_degree, singular_tolerance)
    coefficients = np.zeros(max_degree + 1, dtype=np.complex128)
    coefficients[0] = 1.0
    for degree in range(1, max_degree + 1):
        coefficients[degree] = -sum(
            traces[index] * coefficients[degree - index]
            for index in range(1, degree + 1)
        ) / degree
    return coefficients
