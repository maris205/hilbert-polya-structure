"""Near-well periodic-orbit certificates for the one-step Hénon warp.

The routines here support the R400 theorem-engineering pilot.  They search
for the reversible (``p=0`` at both turning points) Lyapunov family born from
one normal mode of

    h_a(q,p) = |p|^2/2 + 2*pi*exp(pi*|H_tilde_a(q)|^2).

They do not use primes, zeta zeros, or fitted spectral targets.  The numerical
orbits are diagnostics for an analytic Lyapunov-centre/semiclassical trace
argument; they are not themselves a proof of a trace formula.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import pi, sqrt
from typing import Any, Literal

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

from .warped_henon import (
    TWO_PI,
    hamiltonian_energy,
    potential_derivatives,
)


Branch = Literal["slow", "fast"]


@dataclass(frozen=True)
class NormalModeData:
    """Exact linear data at the unique equilibrium of the one-step well."""

    a: float
    c: float
    singular_values: tuple[float, float]
    angular_frequencies: tuple[float, float]
    periods: tuple[float, float]
    frequency_ratio: float
    fast_transverse_angle: float
    fast_stability_determinant: float
    fast_trace_amplitude: float
    eigenvectors: tuple[tuple[float, float], tuple[float, float]]


@dataclass(frozen=True)
class FastNormalFormData:
    """First nonlinear period/action coefficients for the fast family."""

    cubic_frequency_coefficient: float
    period_energy_slope: float
    action_ratio_energy_slope: float
    third_derivatives_ffj: tuple[float, float]
    fourth_derivative_ffff: float


@dataclass(frozen=True)
class OrbitSearchSpec:
    """Frozen controls for one reversible near-well shooting problem."""

    energy_excess: float
    a: float = 1.02
    n: int = 1
    branch: Branch = "fast"
    rtol: float = 2.0e-12
    atol: float = 2.0e-14
    shooting_steps_per_half_period: int = 160
    certification_steps_per_period: int = 800
    max_nfev: int = 120


def normal_mode_data(a: float) -> NormalModeData:
    """Return closed-form normal-mode and limiting stability data.

    The tuple ordering is ``(slow, fast)`` for frequencies and ``(long,
    short)`` for the corresponding periods.  The columns of ``eigenvectors``
    use the same slow/fast ordering and have a deterministic sign.
    """

    if a <= -1.0:
        raise ValueError("the centered real branch requires a > -1")
    c = 2.0 * (sqrt(1.0 + a) - 1.0)
    linear_map = np.array([[-c, -1.0], [1.0, 0.0]])
    squared_singular_values, eigenvectors = np.linalg.eigh(
        linear_map.T @ linear_map
    )
    singular_values = np.sqrt(squared_singular_values)
    for column in range(2):
        pivot = int(np.argmax(np.abs(eigenvectors[:, column])))
        if eigenvectors[pivot, column] < 0.0:
            eigenvectors[:, column] *= -1.0

    slow, fast = (float(value) for value in singular_values)
    frequencies = (TWO_PI * slow, TWO_PI * fast)
    periods = (1.0 / slow, 1.0 / fast)
    ratio = fast / slow
    transverse_angle = TWO_PI * slow / fast
    stability_determinant = 4.0 * np.sin(0.5 * transverse_angle) ** 2
    trace_amplitude = periods[1] / sqrt(stability_determinant)
    return NormalModeData(
        a=float(a),
        c=float(c),
        singular_values=(slow, fast),
        angular_frequencies=(float(frequencies[0]), float(frequencies[1])),
        periods=(float(periods[0]), float(periods[1])),
        frequency_ratio=float(ratio),
        fast_transverse_angle=float(transverse_angle),
        fast_stability_determinant=float(stability_determinant),
        fast_trace_amplitude=float(trace_amplitude),
        eigenvectors=(
            (float(eigenvectors[0, 0]), float(eigenvectors[1, 0])),
            (float(eigenvectors[0, 1]), float(eigenvectors[1, 1])),
        ),
    )


def fast_normal_form_data(a: float) -> FastNormalFormData:
    """Return the Poincaré--Lindstedt coefficient at the well bottom.

    If ``delta = E - 2*pi`` and the fast Lyapunov branch is parameterized by
    energy, the coefficient gives

        T_fast(E) = T_fast(2*pi) + period_energy_slope * delta + o(delta),

    and integration of ``dS/dE = T`` gives the corresponding first slope of
    ``S(E)/delta``.  The calculation uses only the third and fourth
    derivatives of the analytic potential at the equilibrium.
    """

    mode = normal_mode_data(a)
    c = mode.c
    vectors = np.asarray(mode.eigenvectors, dtype=float).T
    linear_map = np.array([[-c, -1.0], [1.0, 0.0]])
    metric = linear_map.T @ linear_map

    phi2 = TWO_PI * metric
    phi3 = np.zeros((2, 2, 2))
    phi3[0, 0, 0] = 12.0 * pi * a * c
    for indices in ((0, 0, 1), (0, 1, 0), (1, 0, 0)):
        phi3[indices] = 4.0 * pi * a
    phi4 = np.zeros((2, 2, 2, 2))
    phi4[0, 0, 0, 0] = 24.0 * pi * a * a

    potential3 = TWO_PI * phi3
    potential4 = TWO_PI * (
        phi4
        + np.einsum("ij,kl->ijkl", phi2, phi2)
        + np.einsum("ik,jl->ijkl", phi2, phi2)
        + np.einsum("il,jk->ijkl", phi2, phi2)
    )
    normal3 = np.einsum(
        "ijk,ia,jb,kc->abc", potential3, vectors, vectors, vectors
    )
    normal4 = np.einsum(
        "ijkl,ia,jb,kc,ld->abcd",
        potential4,
        vectors,
        vectors,
        vectors,
        vectors,
    )

    fast = 1
    omega = np.asarray(mode.angular_frequencies)
    third_ffj = np.array([normal3[fast, fast, j] for j in range(2)])
    constant_corrections = -third_ffj / (4.0 * omega**2)
    second_harmonic_corrections = -third_ffj / (
        4.0 * (omega**2 - 4.0 * omega[fast] ** 2)
    )
    frequency_coefficient = (
        normal4[fast, fast, fast, fast] / 8.0
        + np.sum(
            third_ffj
            * (constant_corrections + 0.5 * second_harmonic_corrections)
        )
    ) / (2.0 * omega[fast])
    limiting_period = mode.periods[fast]
    period_slope = (
        -limiting_period * 2.0 * frequency_coefficient / omega[fast] ** 3
    )
    return FastNormalFormData(
        cubic_frequency_coefficient=float(frequency_coefficient),
        period_energy_slope=float(period_slope),
        action_ratio_energy_slope=float(0.5 * period_slope),
        third_derivatives_ffj=(float(third_ffj[0]), float(third_ffj[1])),
        fourth_derivative_ffff=float(normal4[fast, fast, fast, fast]),
    )


def _state_rhs(_time: float, state: np.ndarray, *, a: float, n: int) -> np.ndarray:
    _, gradient, _ = potential_derivatives(state[:2], a, n)
    return np.concatenate((state[2:], -gradient))


def _integrate_state(
    state0: np.ndarray,
    duration: float,
    *,
    a: float,
    n: int,
    rtol: float,
    atol: float,
    nominal_steps: int,
) -> np.ndarray:
    solution = solve_ivp(
        lambda time, state: _state_rhs(time, state, a=a, n=n),
        (0.0, duration),
        state0,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=duration / nominal_steps,
    )
    if not solution.success:
        raise RuntimeError(f"state integration failed: {solution.message}")
    return solution.y[:, -1]


def _augmented_rhs(
    _time: float,
    augmented: np.ndarray,
    *,
    a: float,
    n: int,
) -> np.ndarray:
    state = augmented[:4]
    _, gradient, hessian = potential_derivatives(state[:2], a, n)
    flow_jacobian = np.block(
        [
            [np.zeros((2, 2)), np.eye(2)],
            [-hessian, np.zeros((2, 2))],
        ]
    )
    monodromy = augmented[4:20].reshape(4, 4)
    action_rate = float(state[2:] @ state[2:])
    return np.concatenate(
        (
            state[2:],
            -gradient,
            (flow_jacobian @ monodromy).ravel(),
            np.array([action_rate]),
        )
    )


def shoot_brake_orbit(spec: OrbitSearchSpec) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    """Shoot and certify one reversible Lyapunov-family periodic orbit.

    Three dimensionless unknowns specify the initial displacement in the two
    linear normal-mode directions and the half-period.  The equations impose
    the requested energy and zero momentum at the opposite turning point.
    The returned monodromy and action are obtained from a separate full-period
    integration of the variational equations.
    """

    if spec.n != 1:
        raise ValueError("R400 currently certifies the one-step family only")
    if spec.energy_excess <= 0.0:
        raise ValueError("energy_excess must be positive")
    if spec.branch not in {"slow", "fast"}:
        raise ValueError("branch must be 'slow' or 'fast'")
    if spec.shooting_steps_per_half_period < 32:
        raise ValueError("shooting resolution is too small")
    if spec.certification_steps_per_period < 64:
        raise ValueError("certification resolution is too small")

    mode = normal_mode_data(spec.a)
    branch_index = 0 if spec.branch == "slow" else 1
    other_index = 1 - branch_index
    vectors = np.asarray(mode.eigenvectors, dtype=float).T
    branch_vector = vectors[:, branch_index]
    other_vector = vectors[:, other_index]
    basis = np.column_stack((branch_vector, other_vector))

    energy = TWO_PI + spec.energy_excess
    omega = mode.angular_frequencies[branch_index]
    amplitude_scale = sqrt(2.0 * spec.energy_excess) / omega
    momentum_scale = sqrt(2.0 * spec.energy_excess)
    half_period_scale = 0.5 * mode.periods[branch_index]

    def decode(unknowns: np.ndarray) -> tuple[np.ndarray, float]:
        q0 = amplitude_scale * (
            unknowns[0] * branch_vector + unknowns[1] * other_vector
        )
        half_period = half_period_scale * unknowns[2]
        return q0, float(half_period)

    def residual(unknowns: np.ndarray) -> np.ndarray:
        q0, half_period = decode(unknowns)
        state0 = np.concatenate((q0, np.zeros(2)))
        half_state = _integrate_state(
            state0,
            half_period,
            a=spec.a,
            n=spec.n,
            rtol=max(spec.rtol, 1.0e-11),
            atol=max(spec.atol, 1.0e-13),
            nominal_steps=spec.shooting_steps_per_half_period,
        )
        final_momentum = basis.T @ half_state[2:]
        initial_potential, _, _ = potential_derivatives(q0, spec.a, spec.n)
        return np.concatenate(
            (
                final_momentum / momentum_scale,
                np.array(
                    [(initial_potential - energy) / spec.energy_excess]
                ),
            )
        )

    solution = least_squares(
        residual,
        np.array([1.0, 0.0, 1.0]),
        bounds=(np.array([0.2, -1.0, 0.5]), np.array([2.0, 1.0, 1.5])),
        xtol=1.0e-13,
        ftol=1.0e-13,
        gtol=1.0e-13,
        max_nfev=spec.max_nfev,
    )
    q0, half_period = decode(solution.x)
    period = 2.0 * half_period
    state0 = np.concatenate((q0, np.zeros(2)))
    augmented0 = np.concatenate((state0, np.eye(4).ravel(), np.zeros(1)))
    sample_times = np.linspace(0.0, period, spec.certification_steps_per_period + 1)
    certified = solve_ivp(
        lambda time, state: _augmented_rhs(time, state, a=spec.a, n=spec.n),
        (0.0, period),
        augmented0,
        t_eval=sample_times,
        method="DOP853",
        rtol=spec.rtol,
        atol=spec.atol,
        max_step=period / spec.certification_steps_per_period,
    )
    if not certified.success:
        raise RuntimeError(f"certification integration failed: {certified.message}")

    final_state = certified.y[:4, -1]
    monodromy = certified.y[4:20, -1].reshape(4, 4)
    action = float(certified.y[20, -1])
    energies = np.array(
        [
            hamiltonian_energy(
                certified.y[:2, column],
                certified.y[2:4, column],
                spec.a,
                spec.n,
            )
            for column in range(certified.y.shape[1])
        ]
    )

    multipliers = np.linalg.eigvals(monodromy)
    unit_order = np.argsort(np.abs(multipliers - 1.0))
    trivial_multipliers = multipliers[unit_order[:2]]
    transverse_multipliers = multipliers[unit_order[2:]]
    transverse_determinant = np.prod(1.0 - transverse_multipliers)
    symplectic_form = np.block(
        [[np.zeros((2, 2)), np.eye(2)], [-np.eye(2), np.zeros((2, 2))]]
    )
    symplectic_defect = np.linalg.norm(
        monodromy.T @ symplectic_form @ monodromy - symplectic_form,
        ord=np.inf,
    )
    q_scale = max(amplitude_scale, np.finfo(float).eps)
    closure_scaled = max(
        float(np.max(np.abs(final_state[:2] - state0[:2])) / q_scale),
        float(np.max(np.abs(final_state[2:] - state0[2:])) / momentum_scale),
    )
    shooting_residual = residual(solution.x)
    limiting_period = mode.periods[branch_index]
    asymptotic_action = limiting_period * spec.energy_excess

    summary: dict[str, Any] = {
        "spec": asdict(spec),
        "energy": float(energy),
        "normal_mode": asdict(mode),
        "optimizer_success": bool(solution.success),
        "optimizer_status": int(solution.status),
        "optimizer_message": str(solution.message),
        "optimizer_nfev": int(solution.nfev),
        "dimensionless_unknowns": [float(value) for value in solution.x],
        "max_abs_shooting_residual": float(np.max(np.abs(shooting_residual))),
        "initial_state": [float(value) for value in state0],
        "period": float(period),
        "limiting_period": float(limiting_period),
        "relative_period_shift": float(period / limiting_period - 1.0),
        "action": action,
        "linear_asymptotic_action": float(asymptotic_action),
        "relative_action_ratio": float(action / asymptotic_action),
        "max_scaled_closure": closure_scaled,
        "max_energy_drift_over_excess": float(
            np.max(np.abs(energies - energy)) / spec.energy_excess
        ),
        "symplectic_defect_inf": float(symplectic_defect),
        "trivial_multiplier_max_distance_from_one": float(
            np.max(np.abs(trivial_multipliers - 1.0))
        ),
        "transverse_multipliers": [
            {"real": float(value.real), "imag": float(value.imag)}
            for value in transverse_multipliers
        ],
        "transverse_stability_determinant": {
            "real": float(transverse_determinant.real),
            "imag": float(transverse_determinant.imag),
        },
        "trace_amplitude_magnitude": float(
            period / sqrt(abs(transverse_determinant))
        ),
    }
    arrays = {
        "times": sample_times,
        "states": certified.y[:4].T,
        "energies": energies,
        "monodromy": monodromy,
        "multipliers_real": multipliers.real,
        "multipliers_imag": multipliers.imag,
        "shooting_residual": shooting_residual,
    }
    return summary, arrays
