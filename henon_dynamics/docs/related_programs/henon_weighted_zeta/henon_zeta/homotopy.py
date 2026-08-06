"""Total-degree homotopy for the cyclic Hénon periodic-point equations."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

import mpmath as mp
import numpy as np
from numpy.typing import ArrayLike, NDArray

from .orbits import canonical_rotation, cyclic_distance, primitive_period


ComplexArray = NDArray[np.complex128]


@dataclass(frozen=True)
class PathResult:
    path_index: int
    success: bool
    endpoint: tuple[complex, ...]
    residual_inf: float
    accepted_steps: int
    rejected_steps: int
    minimum_step: float
    maximum_condition: float
    message: str


def total_degree_starts(period: int) -> list[ComplexArray]:
    """Return the 2^n roots of Q_i(x)=x_i^2-1."""

    if period < 1:
        raise ValueError("period must be positive")
    return [np.asarray(values, dtype=np.complex128) for values in product((-1.0, 1.0), repeat=period)]


def target_residual(sequence: ArrayLike, a: float) -> ComplexArray:
    coordinates = np.asarray(sequence, dtype=np.complex128)
    return np.roll(coordinates, -1) + np.roll(coordinates, 1) + float(a) * coordinates**2 - 1.0


def target_jacobian(sequence: ArrayLike, a: float) -> ComplexArray:
    coordinates = np.asarray(sequence, dtype=np.complex128)
    period = coordinates.size
    jacobian = np.zeros((period, period), dtype=np.complex128)
    for index in range(period):
        jacobian[index, index] += 2.0 * float(a) * coordinates[index]
        jacobian[index, (index - 1) % period] += 1.0
        jacobian[index, (index + 1) % period] += 1.0
    return jacobian


def start_residual(sequence: ArrayLike) -> ComplexArray:
    coordinates = np.asarray(sequence, dtype=np.complex128)
    return coordinates**2 - 1.0


def start_jacobian(sequence: ArrayLike) -> ComplexArray:
    coordinates = np.asarray(sequence, dtype=np.complex128)
    return np.diag(2.0 * coordinates).astype(np.complex128)


def homotopy_residual(sequence: ArrayLike, t: float, a: float, gamma: complex) -> ComplexArray:
    return (1.0 - t) * gamma * start_residual(sequence) + t * target_residual(sequence, a)


def homotopy_jacobian(sequence: ArrayLike, t: float, a: float, gamma: complex) -> ComplexArray:
    return (1.0 - t) * gamma * start_jacobian(sequence) + t * target_jacobian(sequence, a)


def homotopy_t_derivative(sequence: ArrayLike, a: float, gamma: complex) -> ComplexArray:
    return target_residual(sequence, a) - gamma * start_residual(sequence)


def _correct(
    prediction: ComplexArray,
    t: float,
    a: float,
    gamma: complex,
    tolerance: float,
    max_iterations: int,
) -> tuple[bool, ComplexArray, int, float]:
    coordinates = prediction.copy()
    largest_condition = 0.0
    for iteration in range(1, max_iterations + 1):
        residual = homotopy_residual(coordinates, t, a, gamma)
        residual_norm = float(np.linalg.norm(residual, ord=np.inf))
        if residual_norm <= tolerance:
            return True, coordinates, iteration - 1, largest_condition
        jacobian = homotopy_jacobian(coordinates, t, a, gamma)
        try:
            condition = float(np.linalg.cond(jacobian))
            correction = np.linalg.solve(jacobian, residual)
        except np.linalg.LinAlgError:
            return False, coordinates, iteration, float("inf")
        largest_condition = max(largest_condition, condition)
        coordinates -= correction
        if not np.all(np.isfinite(coordinates)):
            return False, coordinates, iteration, largest_condition
    residual_norm = float(np.linalg.norm(homotopy_residual(coordinates, t, a, gamma), ord=np.inf))
    return residual_norm <= tolerance, coordinates, max_iterations, largest_condition


def track_path(
    start: ArrayLike,
    a: float,
    gamma: complex,
    path_index: int = 0,
    initial_step: float = 0.01,
    maximum_step: float = 0.025,
    minimum_step: float = 1.0e-8,
    tolerance: float = 1.0e-11,
    max_newton_iterations: int = 10,
) -> PathResult:
    """Track one regular homotopy path with tangent prediction and Newton correction."""

    coordinates = np.asarray(start, dtype=np.complex128).copy()
    t = 0.0
    step = initial_step
    accepted_steps = 0
    rejected_steps = 0
    smallest_step = step
    largest_condition = 0.0
    while t < 1.0 - 1.0e-15:
        trial_step = min(step, 1.0 - t)
        jacobian = homotopy_jacobian(coordinates, t, a, gamma)
        try:
            tangent = np.linalg.solve(jacobian, -homotopy_t_derivative(coordinates, a, gamma))
            largest_condition = max(largest_condition, float(np.linalg.cond(jacobian)))
        except np.linalg.LinAlgError:
            return PathResult(path_index, False, tuple(coordinates), float("inf"), accepted_steps, rejected_steps, smallest_step, float("inf"), "singular_tangent_jacobian")

        predicted = coordinates + trial_step * tangent
        corrected, candidate, iterations, condition = _correct(
            predicted,
            t + trial_step,
            a,
            gamma,
            tolerance,
            max_newton_iterations,
        )
        largest_condition = max(largest_condition, condition)
        if corrected:
            coordinates = candidate
            t += trial_step
            accepted_steps += 1
            smallest_step = min(smallest_step, trial_step)
            if iterations <= 2:
                step = min(maximum_step, trial_step * 1.35)
            elif iterations >= 6:
                step = max(minimum_step, trial_step * 0.7)
            else:
                step = trial_step
            continue

        rejected_steps += 1
        step = trial_step * 0.5
        smallest_step = min(smallest_step, step)
        if step < minimum_step:
            residual = float(np.linalg.norm(target_residual(coordinates, a), ord=np.inf))
            return PathResult(path_index, False, tuple(coordinates), residual, accepted_steps, rejected_steps, smallest_step, largest_condition, "step_below_minimum")

    final_ok, coordinates, _, condition = _correct(
        coordinates,
        1.0,
        a,
        gamma,
        tolerance * 0.1,
        max_newton_iterations + 5,
    )
    largest_condition = max(largest_condition, condition)
    residual = float(np.linalg.norm(target_residual(coordinates, a), ord=np.inf))
    return PathResult(
        path_index,
        bool(final_ok and residual <= 10.0 * tolerance),
        tuple(complex(value) for value in coordinates),
        residual,
        accepted_steps,
        rejected_steps,
        smallest_step,
        largest_condition,
        "passed" if final_ok else "target_correction_failed",
    )


def cluster_endpoints(results: list[PathResult], tolerance: float = 1.0e-7) -> list[ComplexArray]:
    """Cluster successful raw endpoints without quotienting cyclic phase."""

    representatives: list[ComplexArray] = []
    for result in results:
        if not result.success:
            continue
        endpoint = np.asarray(result.endpoint, dtype=np.complex128)
        if not any(float(np.linalg.norm(endpoint - existing, ord=np.inf)) <= tolerance for existing in representatives):
            representatives.append(endpoint)
    return representatives


def refine_complex_endpoint(
    endpoint: ArrayLike,
    a: float,
    dps: int = 80,
    max_iterations: int = 20,
) -> dict[str, object]:
    """Refine a complex target root with arbitrary-precision Newton iteration."""

    endpoint_array = np.asarray(endpoint, dtype=np.complex128)
    with mp.workdps(dps):
        a_mp = mp.mpf(str(a))
        coordinates = [mp.mpc(str(value.real), str(value.imag)) for value in endpoint_array]
        target = mp.power(10, -(dps - 15))
        converged = False
        for iteration in range(1, max_iterations + 1):
            period = len(coordinates)
            residual_values = [
                coordinates[(index + 1) % period]
                + coordinates[(index - 1) % period]
                + a_mp * coordinates[index] ** 2
                - 1
                for index in range(period)
            ]
            jacobian = mp.matrix(period, period)
            for index in range(period):
                jacobian[index, index] += 2 * a_mp * coordinates[index]
                jacobian[index, (index - 1) % period] += 1
                jacobian[index, (index + 1) % period] += 1
            correction = mp.lu_solve(jacobian, mp.matrix(residual_values))
            coordinates = [coordinates[index] - correction[index] for index in range(period)]
            if max(abs(value) for value in correction) < target:
                converged = True
                break

        period = len(coordinates)
        residual_values = [
            coordinates[(index + 1) % period]
            + coordinates[(index - 1) % period]
            + a_mp * coordinates[index] ** 2
            - 1
            for index in range(period)
        ]
        residual_inf = max(abs(value) for value in residual_values)
        max_imaginary = max(abs(mp.im(value)) for value in coordinates)
        digits = max(25, dps - 5)
        return {
            "converged": converged,
            "iterations": iteration,
            "residual_inf": mp.nstr(residual_inf, digits),
            "max_imaginary": mp.nstr(max_imaginary, digits),
            "is_real": bool(max_imaginary < mp.power(10, -(dps - 25))),
            "sequence": [
                [mp.nstr(mp.re(value), digits), mp.nstr(mp.im(value), digits)]
                for value in coordinates
            ],
            "float_sequence": [complex(float(mp.re(value)), float(mp.im(value))) for value in coordinates],
        }


def real_primitive_orbits(
    refined_roots: list[dict[str, object]],
    requested_period: int,
    cluster_tolerance: float = 1.0e-8,
) -> list[NDArray[np.float64]]:
    """Extract distinct real primitive orbits from refined H^n fixed points."""

    representatives: list[NDArray[np.float64]] = []
    for root_record in refined_roots:
        if not root_record["is_real"]:
            continue
        complex_sequence = root_record["float_sequence"]
        sequence = np.asarray([value.real for value in complex_sequence], dtype=float)
        if primitive_period(sequence, tolerance=cluster_tolerance) != requested_period:
            continue
        canonical = canonical_rotation(sequence)
        if not any(cyclic_distance(canonical, existing) <= cluster_tolerance for existing in representatives):
            representatives.append(canonical)
    representatives.sort(key=lambda value: tuple(float(item) for item in value))
    return representatives
