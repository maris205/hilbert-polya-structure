"""Periodic-orbit equations, smoke-test search, and local certification.

The multistart solver in this module is an exploratory real-root finder. It does not
claim global completeness. A total-degree homotopy or interval covering is required
before a finite catalog may be called complete.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from math import copysign, sqrt
from typing import Iterable

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import root
from scipy.stats import qmc

from .controls import analytic_period2, analytic_period3, real_periodic_coordinate_bound
from .geometry import classify_monodromy, fixed_points, monodromy_matrix, periodic_action


FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class FloatingPointKantorovichDiagnostic:
    passed: bool
    eta: float
    inverse_jacobian_inf: float
    gamma: float
    alpha: float
    radius: float
    condition_number: float
    reason: str


@dataclass
class OrbitRecord:
    orbit_id: str
    a: float
    period: int
    sequence: tuple[float, ...]
    scaled_residual_inf: float
    residual_inf: float
    solver_success: bool
    root_diagnostic: FloatingPointKantorovichDiagnostic
    trace: float
    determinant: float
    determinant_error: float
    greene_residue: float
    stability: str
    multiplier_large: complex
    multiplier_small: complex
    independent_eigenvalues: tuple[complex, complex]
    multiplier_product_error: float
    phase_trace_spread: float
    action: float
    reversor_partner_id: str | None = None
    reversor_partner_found: bool = False
    self_reversing: bool = False

    def to_dict(self) -> dict[str, object]:
        payload = asdict(self)
        payload["multiplier_large"] = [self.multiplier_large.real, self.multiplier_large.imag]
        payload["multiplier_small"] = [self.multiplier_small.real, self.multiplier_small.imag]
        payload["independent_eigenvalues"] = [
            [value.real, value.imag] for value in self.independent_eigenvalues
        ]
        return payload


@dataclass(frozen=True)
class PeriodSearchStats:
    a: float
    requested_period: int
    attempted: int
    optimizer_successes: int
    converged_real_roots: int
    within_bound: int
    lower_period_roots: int
    exact_period_candidates: int
    duplicates: int
    diagnostic_passed_orbits: int
    orbit_count: int


def cyclic_residual(sequence: ArrayLike, a: float) -> FloatArray:
    """Return G_i=x_{i+1}+x_{i-1}+a*x_i^2-1 for cyclic indices."""

    coordinates = np.asarray(sequence, dtype=float)
    if coordinates.ndim != 1 or coordinates.size == 0:
        raise ValueError("sequence must be a non-empty one-dimensional array")
    return np.roll(coordinates, -1) + np.roll(coordinates, 1) + float(a) * coordinates**2 - 1.0


def cyclic_jacobian(sequence: ArrayLike, a: float) -> FloatArray:
    """Return the Jacobian of the cyclic polynomial system.

    The additive assembly is essential for periods one and two, where neighbor
    indices coincide.
    """

    coordinates = np.asarray(sequence, dtype=float)
    if coordinates.ndim != 1 or coordinates.size == 0:
        raise ValueError("sequence must be a non-empty one-dimensional array")
    period = coordinates.size
    jacobian = np.zeros((period, period), dtype=float)
    for index in range(period):
        jacobian[index, index] += 2.0 * float(a) * coordinates[index]
        jacobian[index, (index - 1) % period] += 1.0
        jacobian[index, (index + 1) % period] += 1.0
    return jacobian


def scaled_residual_inf(sequence: ArrayLike, a: float) -> float:
    coordinates = np.asarray(sequence, dtype=float)
    norm = float(np.linalg.norm(coordinates, ord=np.inf))
    scale = 1.0 + 2.0 * norm + abs(float(a)) * norm * norm
    return float(np.linalg.norm(cyclic_residual(coordinates, a), ord=np.inf) / scale)


def canonical_rotation(sequence: ArrayLike, decimals: int = 12) -> FloatArray:
    """Return the lexicographically least cyclic rotation."""

    coordinates = np.asarray(sequence, dtype=float)
    if coordinates.ndim != 1 or coordinates.size == 0:
        raise ValueError("sequence must be a non-empty one-dimensional array")
    rotations = [np.roll(coordinates, -shift) for shift in range(coordinates.size)]

    def key(rotation: FloatArray) -> tuple[float, ...]:
        rounded = np.round(rotation, decimals=decimals)
        rounded[np.abs(rounded) < 0.5 * 10.0 ** (-decimals)] = 0.0
        return tuple(float(value) for value in rounded)

    best = min(range(len(rotations)), key=lambda index: key(rotations[index]))
    return rotations[best].copy()


def cyclic_distance(first: ArrayLike, second: ArrayLike) -> float:
    """Return the minimum infinity distance over cyclic shifts."""

    first_array = np.asarray(first, dtype=float)
    second_array = np.asarray(second, dtype=float)
    if first_array.shape != second_array.shape or first_array.ndim != 1:
        return float("inf")
    return min(
        float(np.linalg.norm(first_array - np.roll(second_array, shift), ord=np.inf))
        for shift in range(first_array.size)
    )


def primitive_period(sequence: ArrayLike, tolerance: float = 1.0e-8) -> int:
    """Return the least period dividing the supplied cyclic sequence length."""

    coordinates = np.asarray(sequence, dtype=float)
    period = coordinates.size
    for divisor in range(1, period):
        if period % divisor:
            continue
        if float(np.linalg.norm(coordinates - np.roll(coordinates, divisor), ord=np.inf)) <= tolerance:
            return divisor
    return period


def floating_point_kantorovich_diagnostic(
    sequence: ArrayLike, a: float
) -> FloatingPointKantorovichDiagnostic:
    """Apply a floating-point Newton--Kantorovich local diagnostic.

    For the cyclic quadratic system, the Jacobian has global Lipschitz constant
    2|a| in the infinity norm. Without outward-rounded interval arithmetic this is
    not a rigorous root certificate and does not prove global completeness.
    """

    coordinates = np.asarray(sequence, dtype=float)
    jacobian = cyclic_jacobian(coordinates, a)
    residual = cyclic_residual(coordinates, a)
    try:
        inverse = np.linalg.inv(jacobian)
    except np.linalg.LinAlgError:
        return FloatingPointKantorovichDiagnostic(
            False, float("inf"), float("inf"), float("inf"), float("inf"),
            float("inf"), float("inf"), "singular_jacobian"
        )

    correction = inverse @ residual
    eta = float(np.linalg.norm(correction, ord=np.inf))
    inverse_norm = float(np.linalg.norm(inverse, ord=np.inf))
    gamma = 2.0 * abs(float(a)) * inverse_norm
    alpha = gamma * eta
    condition = float(np.linalg.cond(jacobian, p=np.inf))
    if not np.isfinite(alpha) or alpha > 0.5:
        return FloatingPointKantorovichDiagnostic(
            False, eta, inverse_norm, gamma, alpha, float("inf"), condition,
            "alpha_exceeds_half"
        )
    if gamma == 0.0:
        radius = eta
    else:
        radius = (1.0 - sqrt(max(0.0, 1.0 - 2.0 * alpha))) / gamma
    return FloatingPointKantorovichDiagnostic(
        True, eta, inverse_norm, gamma, alpha, radius, condition,
        "floating_point_conditions_passed"
    )


def stable_multipliers(trace: float, stability: str) -> tuple[complex, complex]:
    """Return numerically stable reciprocal multipliers from the trace."""

    if stability == "hyperbolic":
        discriminant = sqrt(max(0.0, trace * trace - 4.0))
        large = (trace + copysign(discriminant, trace)) / 2.0
        small = 1.0 / large
        return complex(large), complex(small)
    if stability == "elliptic":
        imaginary = sqrt(max(0.0, 4.0 - trace * trace)) / 2.0
        real = trace / 2.0
        return complex(real, imaginary), complex(real, -imaginary)
    return complex(trace / 2.0), complex(trace / 2.0)


def build_orbit_record(a: float, sequence: ArrayLike, solver_success: bool) -> OrbitRecord:
    coordinates = canonical_rotation(sequence)
    period = coordinates.size
    matrix = monodromy_matrix(coordinates, a)
    trace = float(np.trace(matrix))
    determinant = float(np.linalg.det(matrix))
    stability = classify_monodromy(matrix)
    multiplier_large, multiplier_small = stable_multipliers(trace, stability)
    raw_eigenvalues = np.linalg.eigvals(matrix)
    independent_eigenvalues = (
        complex(raw_eigenvalues[0]),
        complex(raw_eigenvalues[1]),
    )
    phase_traces = [
        float(np.trace(monodromy_matrix(np.roll(coordinates, shift), a)))
        for shift in range(period)
    ]
    raw_residual = float(np.linalg.norm(cyclic_residual(coordinates, a), ord=np.inf))
    return OrbitRecord(
        orbit_id="",
        a=float(a),
        period=period,
        sequence=tuple(float(value) for value in coordinates),
        scaled_residual_inf=scaled_residual_inf(coordinates, a),
        residual_inf=raw_residual,
        solver_success=bool(solver_success),
        root_diagnostic=floating_point_kantorovich_diagnostic(coordinates, a),
        trace=trace,
        determinant=determinant,
        determinant_error=abs(determinant - 1.0),
        greene_residue=(2.0 - trace) / 4.0,
        stability=stability,
        multiplier_large=multiplier_large,
        multiplier_small=multiplier_small,
        independent_eigenvalues=independent_eigenvalues,
        multiplier_product_error=abs(
            independent_eigenvalues[0] * independent_eigenvalues[1] - 1.0
        ),
        phase_trace_spread=max(phase_traces) - min(phase_traces),
        action=periodic_action(coordinates, a),
    )


def initial_guesses(a: float, period: int, random_starts: int, seed: int) -> list[FloatArray]:
    """Build deterministic analytic/binary seeds plus scrambled Sobol seeds."""

    if period < 1:
        raise ValueError("period must be positive")
    bound = real_periodic_coordinate_bound(a)
    guesses: list[FloatArray] = []

    fixed_coordinates = [record.coordinate for record in fixed_points(a)]
    for coordinate in fixed_coordinates:
        guesses.append(np.full(period, coordinate, dtype=float))

    if period <= 12 and len(fixed_coordinates) >= 2:
        for code in product(fixed_coordinates[:2], repeat=period):
            guesses.append(np.asarray(code, dtype=float))

    if period == 2:
        guesses.extend(np.asarray(sequence, dtype=float) for sequence in analytic_period2(a))
    if period == 3:
        guesses.extend(np.asarray(sequence, dtype=float) for sequence in analytic_period3(a))

    if random_starts > 0 and np.isfinite(bound):
        sampler = qmc.Sobol(d=period, scramble=True, seed=seed)
        power = int(np.ceil(np.log2(random_starts)))
        unit = sampler.random_base2(power)[:random_starts]
        guesses.extend(-bound + 2.0 * bound * row for row in unit)

    # Exact duplicates are cheap to remove and otherwise overweight fixed seeds.
    unique: dict[tuple[float, ...], FloatArray] = {}
    for guess in guesses:
        unique.setdefault(tuple(float(value) for value in np.round(guess, 14)), guess)
    return list(unique.values())


def _solve_guess(guess: FloatArray, a: float, root_tolerance: float, max_evaluations: int) -> tuple[FloatArray, bool, float]:
    result = root(
        lambda coordinates: cyclic_residual(coordinates, a),
        guess,
        jac=lambda coordinates: cyclic_jacobian(coordinates, a),
        method="hybr",
        options={"xtol": root_tolerance, "maxfev": max_evaluations},
    )
    coordinates = np.asarray(result.x, dtype=float)
    return coordinates, bool(result.success), scaled_residual_inf(coordinates, a)


def search_period(
    a: float,
    period: int,
    random_starts: int = 256,
    seed: int = 20260731,
    root_tolerance: float = 1.0e-12,
    acceptance_tolerance: float = 1.0e-11,
    primitive_tolerance: float = 1.0e-8,
    cluster_tolerance: float = 1.0e-8,
    max_evaluations: int = 4000,
) -> tuple[list[OrbitRecord], PeriodSearchStats]:
    """Search real primitive orbits of one requested period.

    This routine is intentionally labeled a search. It provides local root
    diagnostics but not an interval certificate or all-roots completeness proof.
    """

    guesses = initial_guesses(a, period, random_starts, seed)
    bound = real_periodic_coordinate_bound(a)
    records: list[OrbitRecord] = []
    optimizer_successes = 0
    converged = 0
    within_bound = 0
    lower_period = 0
    exact_candidates = 0
    duplicates = 0

    for guess in guesses:
        coordinates, solver_success, scaled = _solve_guess(guess, a, root_tolerance, max_evaluations)
        optimizer_successes += int(solver_success)
        if not np.all(np.isfinite(coordinates)) or scaled > acceptance_tolerance:
            continue
        converged += 1
        if float(np.linalg.norm(coordinates, ord=np.inf)) > bound * (1.0 + 1.0e-9):
            continue
        within_bound += 1
        actual_period = primitive_period(coordinates, primitive_tolerance)
        if actual_period != period:
            lower_period += 1
            continue
        exact_candidates += 1
        canonical = canonical_rotation(coordinates)
        duplicate_index = next(
            (
                index
                for index, existing in enumerate(records)
                if cyclic_distance(canonical, existing.sequence) <= cluster_tolerance
            ),
            None,
        )
        candidate = build_orbit_record(a, canonical, solver_success)
        if duplicate_index is not None:
            duplicates += 1
            if candidate.scaled_residual_inf < records[duplicate_index].scaled_residual_inf:
                records[duplicate_index] = candidate
            continue
        records.append(candidate)

    records.sort(key=lambda record: record.sequence)
    prefix = f"a{a:.8g}_n{period:02d}"
    for index, record in enumerate(records):
        record.orbit_id = f"{prefix}_o{index:04d}"

    for record in records:
        reversed_sequence = canonical_rotation(np.asarray(record.sequence)[::-1])
        partner = next(
            (
                candidate
                for candidate in records
                if cyclic_distance(reversed_sequence, candidate.sequence) <= cluster_tolerance
            ),
            None,
        )
        if partner is not None:
            record.reversor_partner_found = True
            record.reversor_partner_id = partner.orbit_id
            record.self_reversing = partner.orbit_id == record.orbit_id

    stats = PeriodSearchStats(
        a=float(a),
        requested_period=period,
        attempted=len(guesses),
        optimizer_successes=optimizer_successes,
        converged_real_roots=converged,
        within_bound=within_bound,
        lower_period_roots=lower_period,
        exact_period_candidates=exact_candidates,
        duplicates=duplicates,
        diagnostic_passed_orbits=sum(
            record.root_diagnostic.passed for record in records
        ),
        orbit_count=len(records),
    )
    return records, stats


def search_periods(
    a: float,
    max_period: int,
    random_starts: int = 256,
    seed: int = 20260731,
    **kwargs: object,
) -> tuple[list[OrbitRecord], list[PeriodSearchStats]]:
    all_records: list[OrbitRecord] = []
    all_stats: list[PeriodSearchStats] = []
    for period in range(1, max_period + 1):
        records, stats = search_period(
            a=a,
            period=period,
            random_starts=random_starts,
            seed=seed + 1009 * period,
            **kwargs,
        )
        all_records.extend(records)
        all_stats.append(stats)
    return all_records, all_stats
