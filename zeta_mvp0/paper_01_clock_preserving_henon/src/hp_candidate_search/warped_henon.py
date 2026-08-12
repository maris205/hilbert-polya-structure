"""Classical diagnostics for Hénon-warped exponential Schrödinger operators.

The classical Hamiltonian is

    h(q, p) = |p|^2 / 2 + 2*pi*exp(pi*|Psi(q)|^2),

where ``Psi`` is a fixed iterate of the area-preserving Hénon map.  The
default map is centered at its positive fixed point.  Centering is an affine
area-preserving conjugacy, keeps the legacy parameter ``a`` unchanged, makes
``a=0`` an exactly radial control, and avoids an irrelevant translational
drift when the map is iterated.

The integrator is velocity Verlet.  Its tangent map is differentiated
analytically, so the reported FTLE does not depend on a finite satellite
separation.  These routines are diagnostics, not evidence for zeta zeros.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import ceil, log, pi, sqrt
from typing import Any

import numpy as np
from scipy.stats import qmc


TWO_PI = 2.0 * pi


def centered_fixed_point(a: float) -> float:
    """Return the positive fixed point of ``H_a`` with a stable ``a=0`` limit."""

    if a < -1.0:
        raise ValueError("the real positive branch requires a >= -1")
    if abs(a) < 1.0e-12:
        return 0.5
    # The rationalized form avoids cancellation close to a=0.
    return 1.0 / (1.0 + sqrt(1.0 + a))


def _map_coefficients(a: float, centered: bool) -> tuple[float, float]:
    if centered:
        return 0.0, -2.0 * a * centered_fixed_point(a)
    return 1.0, 0.0


def henon_step(q: np.ndarray, a: float, *, centered: bool = True) -> np.ndarray:
    """Apply one Hénon step to a two-vector."""

    x, y = np.asarray(q, dtype=float)
    constant, linear = _map_coefficients(a, centered)
    return np.array([constant + linear * x - a * x * x - y, x])


def henon_inverse_step(
    u: np.ndarray, a: float, *, centered: bool = True
) -> np.ndarray:
    """Apply the exact inverse of one Hénon step."""

    first, second = np.asarray(u, dtype=float)
    constant, linear = _map_coefficients(a, centered)
    return np.array([second, constant + linear * second - a * second**2 - first])


def henon_inverse_iterate(
    u: np.ndarray, a: float, n: int, *, centered: bool = True
) -> np.ndarray:
    """Apply ``H_a^{-n}``."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    q = np.asarray(u, dtype=float).copy()
    for _ in range(n):
        q = henon_inverse_step(q, a, centered=centered)
    return q


def henon_iterate_jet(
    q: np.ndarray, a: float, n: int, *, centered: bool = True
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return value, Jacobian, and component Hessians of ``H_a^n``.

    The Hessian array has layout ``hessian[component, input_i, input_j]``.
    """

    if n < 0:
        raise ValueError("n must be nonnegative")
    u = np.asarray(q, dtype=float).copy()
    jac = np.eye(2)
    hess = np.zeros((2, 2, 2), dtype=float)
    constant, linear = _map_coefficients(a, centered)

    for _ in range(n):
        x, y = u
        grad_x = jac[0].copy()
        grad_y = jac[1].copy()
        hess_x = hess[0].copy()
        hess_y = hess[1].copy()
        slope = linear - 2.0 * a * x

        new_u = np.array([constant + linear * x - a * x * x - y, x])
        new_jac = np.vstack((slope * grad_x - grad_y, grad_x))
        new_hess_0 = (
            slope * hess_x - hess_y - 2.0 * a * np.outer(grad_x, grad_x)
        )
        new_hess = np.stack((new_hess_0, hess_x))
        u, jac, hess = new_u, new_jac, new_hess

    return u, jac, hess


def potential_derivatives(
    q: np.ndarray,
    a: float,
    n: int,
    *,
    centered: bool = True,
    phi_cap: float | None = None,
) -> tuple[float, np.ndarray, np.ndarray]:
    """Return the warped potential, gradient, and Hessian.

    ``phi_cap`` is a numerical rejection guard for trial points far outside a
    specified energy surface.  Production trajectories are accepted only
    when their energy drift is small, so the guard must never be interpreted
    as a modification of the mathematical potential.
    """

    u, jac, component_hess = henon_iterate_jet(q, a, n, centered=centered)
    phi = pi * float(u @ u)
    exponent = phi if phi_cap is None else min(phi, phi_cap)
    value = TWO_PI * float(np.exp(exponent))
    grad_phi = TWO_PI * (jac.T @ u)
    hess_phi = TWO_PI * (
        jac.T @ jac
        + u[0] * component_hess[0]
        + u[1] * component_hess[1]
    )
    grad = value * grad_phi
    hess = value * (hess_phi + np.outer(grad_phi, grad_phi))
    return value, grad, hess


def hamiltonian_energy(
    q: np.ndarray, p: np.ndarray, a: float, n: int, *, centered: bool = True
) -> float:
    value, _, _ = potential_derivatives(q, a, n, centered=centered)
    return 0.5 * float(np.asarray(p) @ np.asarray(p)) + value


def microcanonical_initial_state(
    energy: float,
    a: float,
    n: int,
    seed_index: int,
    *,
    centered: bool = True,
    radial_fraction: float = 0.88,
) -> tuple[np.ndarray, np.ndarray, dict[str, float]]:
    """Generate a deterministic microcanonical state without zero data.

    In two configuration dimensions, microcanonical shell measure has uniform
    configuration density on the allowed domain and uniform momentum angle.
    A scrambled-free Sobol point is therefore mapped to uniform area in an
    interior disk in ``u=Psi(q)`` coordinates.
    """

    if energy <= TWO_PI:
        raise ValueError("energy must exceed the potential minimum 2*pi")
    if seed_index < 0:
        raise ValueError("seed_index must be nonnegative")
    sampler = qmc.Sobol(d=3, scramble=False)
    sample = sampler.random_base2(m=max(1, ceil(log(seed_index + 2, 2))))
    s0, s1, s2 = sample[seed_index + 1]
    radius = sqrt(log(energy / TWO_PI) / pi)
    rho = radial_fraction * radius * sqrt(s0)
    theta = TWO_PI * s1
    u = rho * np.array([np.cos(theta), np.sin(theta)])
    q = henon_inverse_iterate(u, a, n, centered=centered)
    potential, _, _ = potential_derivatives(q, a, n, centered=centered)
    kinetic_radius = sqrt(max(0.0, 2.0 * (energy - potential)))
    momentum_angle = TWO_PI * s2
    p = kinetic_radius * np.array(
        [np.cos(momentum_angle), np.sin(momentum_angle)]
    )
    meta = {
        "sobol_0": float(s0),
        "sobol_1": float(s1),
        "sobol_2": float(s2),
        "u_radius_fraction": float(rho / radius),
        "initial_potential_fraction": float(potential / energy),
    }
    return q, p, meta


def _configuration_scale(
    energy: float, a: float, n: int, *, centered: bool
) -> float:
    radius = sqrt(log(energy / TWO_PI) / pi)
    values = []
    for angle in np.linspace(0.0, TWO_PI, 65)[:-1]:
        u = radius * np.array([np.cos(angle), np.sin(angle)])
        values.append(np.linalg.norm(henon_inverse_iterate(u, a, n, centered=centered)))
    return max(1.0, float(max(values)))


@dataclass(frozen=True)
class FTLEConfig:
    """Frozen controls for one variational FTLE trajectory."""

    energy: float
    a: float
    n: int
    seed_index: int
    total_natural_time: float = 40.0
    steps_per_natural_time: int = 256
    renormalizations_per_natural_time: int = 8
    centered: bool = True
    radial_fraction: float = 0.88


def run_ftle_trajectory(config: FTLEConfig) -> dict[str, Any]:
    """Run one symplectic trajectory and return deterministic diagnostics."""

    if config.total_natural_time <= 0.0:
        raise ValueError("total_natural_time must be positive")
    if config.steps_per_natural_time < 8:
        raise ValueError("steps_per_natural_time is too small")
    if config.renormalizations_per_natural_time < 1:
        raise ValueError("renormalizations_per_natural_time must be positive")

    q, p, initial_meta = microcanonical_initial_state(
        config.energy,
        config.a,
        config.n,
        config.seed_index,
        centered=config.centered,
        radial_fraction=config.radial_fraction,
    )
    initial_q = q.copy()
    initial_p = p.copy()
    q_scale = _configuration_scale(
        config.energy, config.a, config.n, centered=config.centered
    )
    p_scale = sqrt(2.0 * config.energy)
    state_scales = np.array([q_scale, q_scale, p_scale, p_scale])

    # Two initially orthogonal scaled tangent directions for FTLE and SALI.
    tangent = np.zeros((4, 2), dtype=float)
    tangent[0, 0] = q_scale
    tangent[3, 1] = p_scale

    log_energy = log(config.energy / TWO_PI)
    natural_time_scale = sqrt(log_energy / config.energy)
    dt = natural_time_scale / config.steps_per_natural_time
    n_steps = int(round(config.total_natural_time * config.steps_per_natural_time))
    block_steps = max(
        1,
        config.steps_per_natural_time
        // config.renormalizations_per_natural_time,
    )
    phi_cap = log_energy + 30.0

    initial_energy = hamiltonian_energy(
        q, p, config.a, config.n, centered=config.centered
    )
    max_relative_energy_drift = 0.0
    accumulated_log_stretch = 0.0
    angular_momentum_min = float(q[0] * p[1] - q[1] * p[0])
    angular_momentum_max = angular_momentum_min
    poincare_points: list[tuple[float, float]] = []
    checkpoint_targets = tuple(
        target
        for target in (20.0, 40.0, 80.0, 160.0)
        if target <= config.total_natural_time + 1.0e-12
    )
    checkpoint_results: dict[str, float] = {}
    previous_q = q.copy()
    previous_p = p.copy()
    status = "ok"

    _, grad, hess = potential_derivatives(
        q,
        config.a,
        config.n,
        centered=config.centered,
        phi_cap=phi_cap,
    )

    for step in range(1, n_steps + 1):
        dq = tangent[:2]
        dp = tangent[2:]
        p_half = p - 0.5 * dt * grad
        dp_half = dp - 0.5 * dt * (hess @ dq)
        q_new = q + dt * p_half
        dq_new = dq + dt * dp_half

        value_new, grad_new, hess_new = potential_derivatives(
            q_new,
            config.a,
            config.n,
            centered=config.centered,
            phi_cap=phi_cap,
        )
        p_new = p_half - 0.5 * dt * grad_new
        dp_new = dp_half - 0.5 * dt * (hess_new @ dq_new)
        tangent = np.vstack((dq_new, dp_new))

        if not (
            np.all(np.isfinite(q_new))
            and np.all(np.isfinite(p_new))
            and np.all(np.isfinite(tangent))
        ):
            status = "nonfinite"
            break

        if previous_q[1] < 0.0 <= q_new[1] and p_new[1] > 0.0:
            denominator = q_new[1] - previous_q[1]
            fraction = 0.0 if denominator == 0.0 else -previous_q[1] / denominator
            cross_qx = previous_q[0] + fraction * (q_new[0] - previous_q[0])
            cross_px = previous_p[0] + fraction * (p_new[0] - previous_p[0])
            poincare_points.append((float(cross_qx / q_scale), float(cross_px / p_scale)))

        q, p = q_new, p_new
        previous_q, previous_p = q.copy(), p.copy()
        grad, hess = grad_new, hess_new

        angular_momentum = float(q[0] * p[1] - q[1] * p[0])
        angular_momentum_min = min(angular_momentum_min, angular_momentum)
        angular_momentum_max = max(angular_momentum_max, angular_momentum)

        if step % block_steps == 0 or step == n_steps:
            for column in range(2):
                scaled_norm = float(np.linalg.norm(tangent[:, column] / state_scales))
                if not np.isfinite(scaled_norm) or scaled_norm <= 0.0:
                    status = "tangent_failure"
                    break
                if column == 0:
                    accumulated_log_stretch += log(scaled_norm)
                tangent[:, column] /= scaled_norm
            if status != "ok":
                break

            completed_natural_at_block = step / config.steps_per_natural_time
            scaled_at_block = tangent / state_scales[:, None]
            for column in range(2):
                column_norm = np.linalg.norm(scaled_at_block[:, column])
                if column_norm > 0.0:
                    scaled_at_block[:, column] /= column_norm
            sali_at_block = float(
                min(
                    np.linalg.norm(scaled_at_block[:, 0] - scaled_at_block[:, 1]),
                    np.linalg.norm(scaled_at_block[:, 0] + scaled_at_block[:, 1]),
                )
            )
            for target in checkpoint_targets:
                label = int(target)
                if (
                    f"ftle_natural_t{label}" not in checkpoint_results
                    and completed_natural_at_block + 1.0e-12 >= target
                ):
                    checkpoint_results[f"ftle_natural_t{label}"] = float(
                        accumulated_log_stretch / completed_natural_at_block
                    )
                    checkpoint_results[f"sali_t{label}"] = sali_at_block

            current_energy = 0.5 * float(p @ p) + value_new
            relative_drift = abs(current_energy - initial_energy) / initial_energy
            max_relative_energy_drift = max(
                max_relative_energy_drift, float(relative_drift)
            )

    completed_steps = step if n_steps else 0
    physical_time = completed_steps * dt
    completed_natural_time = physical_time / natural_time_scale
    ftle_physical = (
        accumulated_log_stretch / physical_time if physical_time > 0.0 else float("nan")
    )
    ftle_natural = ftle_physical * natural_time_scale

    scaled_vectors = tangent / state_scales[:, None]
    for column in range(2):
        norm = np.linalg.norm(scaled_vectors[:, column])
        if norm > 0.0:
            scaled_vectors[:, column] /= norm
    sali = float(
        min(
            np.linalg.norm(scaled_vectors[:, 0] - scaled_vectors[:, 1]),
            np.linalg.norm(scaled_vectors[:, 0] + scaled_vectors[:, 1]),
        )
    )

    if poincare_points:
        point_array = np.asarray(poincare_points)
        clipped = np.clip((point_array + 1.5) / 3.0, 0.0, 1.0 - np.finfo(float).eps)
        bins = np.floor(24 * clipped).astype(int)
        occupancy = len({(int(i), int(j)) for i, j in bins}) / (24.0 * 24.0)
    else:
        occupancy = 0.0

    angular_scale = max(1.0, q_scale * p_scale)
    result: dict[str, Any] = {
        **asdict(config),
        **initial_meta,
        "status": status,
        "completed_steps": int(completed_steps),
        "completed_natural_time": float(completed_natural_time),
        "dt": float(dt),
        "natural_time_scale": float(natural_time_scale),
        "q_scale": float(q_scale),
        "p_scale": float(p_scale),
        "initial_q0": float(initial_q[0]),
        "initial_q1": float(initial_q[1]),
        "initial_p0": float(initial_p[0]),
        "initial_p1": float(initial_p[1]),
        "initial_energy": float(initial_energy),
        "max_relative_energy_drift": float(max_relative_energy_drift),
        "ftle_physical": float(ftle_physical),
        "ftle_natural": float(ftle_natural),
        "sali": sali,
        "angular_momentum_range_scaled": float(
            (angular_momentum_max - angular_momentum_min) / angular_scale
        ),
        "poincare_crossings": len(poincare_points),
        "poincare_occupancy_24": float(occupancy),
        **checkpoint_results,
    }
    return result
