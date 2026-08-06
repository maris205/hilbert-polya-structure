"""Exact geometry and orbit invariants for the Hénon map used in Paper 3."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from numpy.typing import ArrayLike, NDArray


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class FixedPoint:
    """A fixed point and its linear stability data."""

    coordinate: float
    trace: float
    determinant: float
    stability: str
    eigenvalues: tuple[complex, complex]


def _point(value: ArrayLike) -> FloatArray:
    point = np.asarray(value, dtype=float)
    if point.shape != (2,):
        raise ValueError(f"expected a two-dimensional point, got shape {point.shape}")
    return point


def henon_map(point: ArrayLike, a: float) -> FloatArray:
    """Return H_a(x,y) = (1-a*x^2-y, x)."""

    x, y = _point(point)
    return np.array([1.0 - float(a) * x * x - y, x], dtype=float)


def henon_inverse(point: ArrayLike, a: float) -> FloatArray:
    """Return the exact inverse H_a^{-1}(X,Y)."""

    X, Y = _point(point)
    return np.array([Y, 1.0 - float(a) * Y * Y - X], dtype=float)


def reversor(point: ArrayLike) -> FloatArray:
    """Return the involution R(x,y) = (y,x)."""

    x, y = _point(point)
    return np.array([y, x], dtype=float)


def henon_jacobian(point: ArrayLike, a: float) -> FloatArray:
    """Return D H_a at point."""

    x, _ = _point(point)
    return np.array([[-2.0 * float(a) * x, -1.0], [1.0, 0.0]], dtype=float)


def classify_monodromy(matrix: ArrayLike, tolerance: float = 1.0e-10) -> str:
    """Classify a real area-preserving 2x2 monodromy matrix by its trace."""

    matrix_array = np.asarray(matrix, dtype=float)
    if matrix_array.shape != (2, 2):
        raise ValueError("monodromy matrix must be 2x2")
    trace_abs = abs(float(np.trace(matrix_array)))
    if trace_abs > 2.0 + tolerance:
        return "hyperbolic"
    if trace_abs < 2.0 - tolerance:
        return "elliptic"
    return "parabolic"


def fixed_points(a: float) -> tuple[FixedPoint, ...]:
    """Return all finite real fixed points, including stability data."""

    a_float = float(a)
    if a_float <= -1.0:
        raise ValueError("real fixed-point pair requires a > -1")
    if abs(a_float) < np.finfo(float).eps:
        coordinate = 0.5
        matrix = henon_jacobian((coordinate, coordinate), a_float)
        eigenvalues = tuple(complex(value) for value in np.linalg.eigvals(matrix))
        point = FixedPoint(
            coordinate=coordinate,
            trace=float(np.trace(matrix)),
            determinant=float(np.linalg.det(matrix)),
            stability=classify_monodromy(matrix),
            eigenvalues=(eigenvalues[0], eigenvalues[1]),
        )
        return (point,)

    root = np.sqrt(1.0 + a_float)
    # The first form avoids cancellation as a approaches zero from either side.
    coordinates = (1.0 / (1.0 + root), -(1.0 + root) / a_float)
    records: list[FixedPoint] = []
    for coordinate in coordinates:
        matrix = henon_jacobian((coordinate, coordinate), a_float)
        eigenvalues = tuple(complex(value) for value in np.linalg.eigvals(matrix))
        records.append(
            FixedPoint(
                coordinate=float(coordinate),
                trace=float(np.trace(matrix)),
                determinant=float(np.linalg.det(matrix)),
                stability=classify_monodromy(matrix),
                eigenvalues=(eigenvalues[0], eigenvalues[1]),
            )
        )
    return records[0], records[1]


def generating_function(q: float, q_next: float, a: float) -> float:
    """Return S_a(q,q') = q*q' - q + a*q^3/3."""

    q_float = float(q)
    return q_float * float(q_next) - q_float + float(a) * q_float**3 / 3.0


def generating_momenta(q: float, q_next: float, a: float) -> tuple[float, float]:
    """Return p=-d_q S and p'=d_{q'} S."""

    q_float = float(q)
    q_next_float = float(q_next)
    p = 1.0 - float(a) * q_float**2 - q_next_float
    p_next = q_float
    return p, p_next


def sequence_points(sequence: Iterable[float]) -> FloatArray:
    """Convert cyclic coordinates x_i to points (x_i, x_{i-1})."""

    coordinates = np.asarray(tuple(sequence), dtype=float)
    if coordinates.ndim != 1 or coordinates.size == 0:
        raise ValueError("sequence must be a non-empty one-dimensional iterable")
    return np.column_stack((coordinates, np.roll(coordinates, 1)))


def monodromy_matrix(sequence: Iterable[float], a: float) -> FloatArray:
    """Return D H_a^n along a cyclic scalar sequence."""

    points = sequence_points(sequence)
    matrix = np.eye(2, dtype=float)
    for point in points:
        matrix = henon_jacobian(point, a) @ matrix
    return matrix


def periodic_action(sequence: Iterable[float], a: float) -> float:
    """Return the cyclic discrete action sum for a periodic sequence."""

    coordinates = np.asarray(tuple(sequence), dtype=float)
    if coordinates.ndim != 1 or coordinates.size == 0:
        raise ValueError("sequence must be a non-empty one-dimensional iterable")
    next_coordinates = np.roll(coordinates, -1)
    terms = coordinates * next_coordinates - coordinates + float(a) * coordinates**3 / 3.0
    return float(np.sum(terms))
