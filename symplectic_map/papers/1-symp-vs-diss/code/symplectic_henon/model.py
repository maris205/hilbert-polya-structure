"""The two-dimensional Hénon homotopy and exact differential identities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from numpy.typing import ArrayLike, NDArray


FloatArray = NDArray[np.float64]
OMEGA: FloatArray = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=float)


@dataclass(frozen=True)
class HenonHomotopy:
    """Map ``H(x,y)=(1-a*x**2-rho*y, x)``.

    ``rho=0`` is the singular one-dimensional endpoint, ``0<rho<1`` is
    conformally symplectic, and ``rho=1`` is area preserving/symplectic.
    """

    a: float
    rho: float

    def __post_init__(self) -> None:
        if not np.isfinite(self.a) or not np.isfinite(self.rho):
            raise ValueError("a and rho must be finite")

    def step(self, point: ArrayLike) -> FloatArray:
        x, y = np.asarray(point, dtype=float)
        return np.array([1.0 - self.a * x * x - self.rho * y, x])

    def jacobian(self, point: ArrayLike) -> FloatArray:
        x = float(np.asarray(point, dtype=float)[0])
        return np.array([[-2.0 * self.a * x, -self.rho], [1.0, 0.0]])

    def jacobian_determinant(self) -> float:
        """Return the analytic (point-independent) determinant ``rho``."""

        return float(self.rho)

    def monodromy_determinant(self, period: int) -> float:
        """Return the analytic determinant ``rho**period`` of ``D H^period``."""

        if period < 0:
            raise ValueError("period must be non-negative")
        return float(self.rho**period)

    def iterate(self, point: ArrayLike, steps: int) -> FloatArray:
        """Return the initial point followed by ``steps`` iterates."""

        if steps < 0:
            raise ValueError("steps must be non-negative")
        orbit = np.empty((steps + 1, 2), dtype=float)
        orbit[0] = np.asarray(point, dtype=float)
        for index in range(steps):
            orbit[index + 1] = self.step(orbit[index])
        return orbit

    def monodromy(self, periodic_points: Iterable[ArrayLike]) -> FloatArray:
        """Return ``D H^n = J_{n-1} ... J_0`` along an ordered orbit."""

        matrix = np.eye(2)
        used = False
        for point in periodic_points:
            matrix = self.jacobian(point) @ matrix
            used = True
        if not used:
            raise ValueError("periodic_points must contain at least one point")
        return matrix

    def conformal_symplectic_defect(self, point: ArrayLike) -> FloatArray:
        """Return ``J.T @ Omega @ J - rho*Omega`` (analytically zero)."""

        jac = self.jacobian(point)
        return jac.T @ OMEGA @ jac - self.rho * OMEGA

    def fixed_points(self) -> FloatArray:
        """Return all real fixed points, sorted increasingly by coordinate."""

        # a*x^2 + (1+rho)*x - 1 = 0.  Handle the affine limit a=0.
        if self.a == 0.0:
            denominator = 1.0 + self.rho
            if denominator == 0.0:
                return np.empty((0, 2), dtype=float)
            root = 1.0 / denominator
            return np.array([[root, root]], dtype=float)
        discriminant = (1.0 + self.rho) ** 2 + 4.0 * self.a
        if discriminant < 0.0:
            return np.empty((0, 2), dtype=float)
        square_root = np.sqrt(discriminant)
        roots = np.array(
            [
                (-(1.0 + self.rho) - square_root) / (2.0 * self.a),
                (-(1.0 + self.rho) + square_root) / (2.0 * self.a),
            ]
        )
        roots.sort()
        return np.column_stack([roots, roots])

    def generating_function(self, q: ArrayLike, Q: ArrayLike) -> FloatArray:
        """Type-1 generating function for the symplectic endpoint.

        For ``rho=1``, ``S(q,Q)=qQ-q+(a/3)q^3`` obeys
        ``p=-partial_q S`` and ``P=partial_Q S``.  No such type-1 generating
        function is claimed for the dissipative or singular members.
        """

        if not np.isclose(self.rho, 1.0, rtol=0.0, atol=1e-14):
            raise ValueError("the stated generating function is only for rho=1")
        q_array = np.asarray(q, dtype=float)
        Q_array = np.asarray(Q, dtype=float)
        return q_array * Q_array - q_array + (self.a / 3.0) * q_array**3

    def periodic_action(self, q_cycle: ArrayLike) -> float:
        """Return ``sum_i S(q_i,q_{i+1})`` for a periodic coordinate cycle."""

        q = np.asarray(q_cycle, dtype=float)
        if q.ndim != 1 or q.size == 0:
            raise ValueError("q_cycle must be a nonempty one-dimensional array")
        return float(np.sum(self.generating_function(q, np.roll(q, -1))))
