"""Secondary attractor diagnostics for the Hénon homotopy.

This module is deliberately separate from the confirmatory symbolic-transport
code.  It uses a post-validation diagnostic seed and contains no access path
to the locked test split.  Its purpose is mechanistic: determine whether the
observed parity curve can be explained by ordinary dissipative attraction.

The map is

    H_{a,rho}(x,y) = (1 - a*x**2 - rho*y, x).

For ``0 <= rho < 1`` a stable periodic orbit can have an open basin.  At the
symplectic endpoint ``rho=1`` the monodromy determinant is one, so a periodic
sink is impossible.  A recurrence classifier can still label a trajectory
started exactly on a periodic orbit; such a label is not evidence of an
attractor, which is why the ensemble protocol and basin counts matter.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import numpy as np
from numpy.typing import ArrayLike, NDArray


FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]

DIAGNOSTIC_SEED = 20260815
EXPLORATORY_RHO_GRID = (
    0.0,
    0.02,
    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.35,
    0.38,
    0.40,
    0.41,
    0.42,
    0.43,
    0.44,
    0.45,
    0.46,
    0.48,
    0.50,
    0.60,
    0.75,
    0.90,
    0.99,
    1.00,
)

# This analysis intentionally has no import of primary split seeds.  The
# diagnostic value is frozen as a literal so changes in another module cannot
# accidentally turn it into access to a confirmatory split.
PRIMARY_SPLIT_SEEDS_FORBIDDEN = frozenset(
    {20260811, 20260812, 20260813, 20260814}
)


def positive_fixed_point(a: float, rho: float) -> float:
    """Return the positive fixed point of ``H_{a,rho}`` for ``a>0``.

    A fixed point has equal coordinates and solves

    ``a*x**2 + (1+rho)*x - 1 = 0``.

    The algebraically equivalent expression ``2/(1+rho+sqrt(...))`` is used
    to avoid cancellation in the positive root.
    """

    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    if not math.isfinite(rho):
        raise ValueError("rho must be finite")
    discriminant = (1.0 + rho) ** 2 + 4.0 * a
    if discriminant < 0.0:
        raise ValueError("the fixed-point discriminant is negative")
    return 2.0 / (1.0 + rho + math.sqrt(discriminant))


def negative_fixed_point(a: float, rho: float) -> float:
    """Return the negative fixed point of ``H_{a,rho}`` for ``a>0``."""

    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    if not math.isfinite(rho):
        raise ValueError("rho must be finite")
    discriminant = (1.0 + rho) ** 2 + 4.0 * a
    if discriminant < 0.0:
        raise ValueError("the fixed-point discriminant is negative")
    return (-(1.0 + rho) - math.sqrt(discriminant)) / (2.0 * a)


def positive_fixed_point_flip_threshold(a: float) -> float:
    """Return the analytic ``rho`` at which the positive fixed point flips.

    The value is ``sqrt(4*a/3)-1``.  It lies in the physical interval
    ``[0,1]`` exactly when ``3/4 <= a <= 3``.  Returning an out-of-interval
    value is intentional: callers can see that no such boundary occurs in
    their selected homotopy interval.
    """

    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    return math.sqrt(4.0 * a / 3.0) - 1.0


def positive_fixed_point_jury_margins(a: float, rho: float) -> dict[str, float]:
    """Return the three strict Jury margins for the positive fixed point.

    The characteristic polynomial is ``lambda**2 + b*lambda + rho`` with
    ``b=2*a*x_plus``.  Both multipliers are strictly inside the unit disk iff
    all returned margins are positive.
    """

    x_plus = positive_fixed_point(a, rho)
    coefficient = 2.0 * a * x_plus
    return {
        "one_plus_b_plus_rho": 1.0 + coefficient + rho,
        "one_minus_b_plus_rho": 1.0 - coefficient + rho,
        "one_minus_rho": 1.0 - rho,
    }


def positive_fixed_point_multipliers(a: float, rho: float) -> NDArray[np.complex128]:
    """Return the two fixed-point multipliers as complex numbers."""

    x_plus = positive_fixed_point(a, rho)
    return np.roots(np.array([1.0, 2.0 * a * x_plus, rho])).astype(
        np.complex128, copy=False
    )


def generate_diagnostic_parent_ensemble(
    *,
    a: float,
    n_trajectories: int = 256,
    parent_burn_in: int = 4096,
    seed: int = DIAGNOSTIC_SEED,
) -> FloatArray:
    """Return deterministic parent-derived states for secondary analysis.

    This seed is not any train/dev/validation/test seed used by the primary
    transport experiment.  The same pre-burn uniform draws are used for each
    ``a`` when the seed and ensemble size agree, aiding neighbor comparisons.
    """

    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    if n_trajectories <= 0:
        raise ValueError("n_trajectories must be positive")
    if parent_burn_in < 1:
        raise ValueError("parent_burn_in must be at least one")
    if seed in PRIMARY_SPLIT_SEEDS_FORBIDDEN:
        raise ValueError(
            "attractor diagnostics must use a seed distinct from every "
            "primary transport split"
        )
    rng = np.random.default_rng(seed)
    previous = rng.uniform(-1.0, 1.0, size=n_trajectories)
    current = 1.0 - a * previous**2
    for _ in range(parent_burn_in - 1):
        previous, current = current, 1.0 - a * current**2
    return np.column_stack((current, previous)).astype(np.float64, copy=False)


def _inside_escape_box(states: FloatArray, escape_bound: float) -> NDArray[np.bool_]:
    return np.all(np.isfinite(states), axis=1) & np.all(
        np.abs(states) <= escape_bound, axis=1
    )


def classify_periodic_tails(
    tails: FloatArray,
    *,
    candidate_periods: Iterable[int] = range(1, 33),
    absolute_tolerance: float = 1e-9,
    relative_tolerance: float = 1e-9,
) -> tuple[IntArray, FloatArray]:
    """Classify the least resolved period in a batch of finite orbit tails.

    Parameters
    ----------
    tails:
        Array with shape ``(time, trajectory, 2)``.  Every entry must be
        finite.  Escaped trajectories must be removed before calling.
    candidate_periods:
        Positive periods to test.  They are sorted internally, so the first
        accepted period is the least accepted period.

    Returns
    -------
    periods, residuals:
        ``periods[j]`` is zero if no candidate recurrence passed.  The
        residual is the maximum coordinate-wise recurrence error for the
        assigned period, or the smallest tested residual when unresolved.

    Notes
    -----
    This is a finite-window numerical classifier, not a proof of asymptotic
    convergence or a completeness certificate for attractors.
    """

    tail = np.asarray(tails, dtype=np.float64)
    if tail.ndim != 3 or tail.shape[2] != 2 or tail.shape[1] == 0:
        raise ValueError("tails must have nonempty shape (time, trajectory, 2)")
    if not np.all(np.isfinite(tail)):
        raise ValueError("tails must contain only finite values")
    if absolute_tolerance < 0.0 or relative_tolerance < 0.0:
        raise ValueError("recurrence tolerances must be nonnegative")
    periods = sorted({int(period) for period in candidate_periods})
    if not periods or periods[0] <= 0:
        raise ValueError("candidate_periods must contain positive integers")
    if periods[-1] >= tail.shape[0]:
        raise ValueError("every candidate period must be shorter than the tail")

    n_trajectories = tail.shape[1]
    assigned = np.zeros(n_trajectories, dtype=np.int64)
    assigned_residual = np.full(n_trajectories, np.inf, dtype=np.float64)
    smallest_residual = np.full(n_trajectories, np.inf, dtype=np.float64)
    scale = np.max(np.abs(tail), axis=(0, 2))
    thresholds = absolute_tolerance + relative_tolerance * np.maximum(1.0, scale)

    for period in periods:
        residual = np.max(np.abs(tail[period:] - tail[:-period]), axis=(0, 2))
        smallest_residual = np.minimum(smallest_residual, residual)
        accepted = (assigned == 0) & (residual <= thresholds)
        assigned[accepted] = period
        assigned_residual[accepted] = residual[accepted]

    unresolved = assigned == 0
    assigned_residual[unresolved] = smallest_residual[unresolved]
    return assigned, assigned_residual


@dataclass(frozen=True)
class AttractorRun:
    """One secondary ensemble run at fixed ``(a,rho)``."""

    a: float
    rho: float
    burn_in: int
    tail_length: int
    escape_bound: float
    absolute_tolerance: float
    relative_tolerance: float
    max_period: int
    labels: NDArray[np.str_]
    periods: IntArray
    recurrence_residuals: FloatArray
    escape_steps: IntArray
    final_states: FloatArray

    @property
    def n_trajectories(self) -> int:
        return int(self.labels.size)

    @property
    def counts(self) -> dict[str, int]:
        labels, counts = np.unique(self.labels, return_counts=True)
        return {
            str(label): int(count)
            for label, count in zip(labels.tolist(), counts.tolist(), strict=True)
        }

    @property
    def fractions(self) -> dict[str, float]:
        return {
            label: count / self.n_trajectories
            for label, count in self.counts.items()
        }


def simulate_and_classify_attractors(
    initial_states: ArrayLike,
    *,
    a: float,
    rho: float,
    burn_in: int = 16_384,
    tail_length: int = 2_048,
    escape_bound: float = 100.0,
    max_period: int = 32,
    absolute_tolerance: float = 1e-9,
    relative_tolerance: float = 1e-9,
) -> AttractorRun:
    """Burn an ensemble, retain a tail, and classify periodic attraction.

    The iteration is vectorized across live trajectories.  Escape is
    absorbing.  Surviving tails are tested for every period from one through
    ``max_period``; labels always use the least accepted period.
    """

    states = np.asarray(initial_states, dtype=np.float64).copy()
    if states.ndim != 2 or states.shape[1] != 2 or states.shape[0] == 0:
        raise ValueError("initial_states must have nonempty shape (n, 2)")
    if not math.isfinite(a) or a <= 0.0:
        raise ValueError("a must be finite and positive")
    if not math.isfinite(rho) or rho < 0.0:
        raise ValueError("rho must be finite and nonnegative")
    if burn_in < 0:
        raise ValueError("burn_in must be nonnegative")
    if tail_length <= 1:
        raise ValueError("tail_length must exceed one")
    if not math.isfinite(escape_bound) or escape_bound <= 0.0:
        raise ValueError("escape_bound must be finite and positive")
    if max_period <= 0 or max_period >= tail_length:
        raise ValueError("max_period must be positive and shorter than the tail")

    n_trajectories = states.shape[0]
    active = _inside_escape_box(states, escape_bound)
    escape_steps = np.full(n_trajectories, -1, dtype=np.int64)
    escape_steps[~active] = 0

    def advance(step_number: int) -> None:
        live_indices = np.flatnonzero(active)
        if live_indices.size == 0:
            return
        x = states[live_indices, 0]
        y = states[live_indices, 1]
        next_states = np.column_stack((1.0 - a * x**2 - rho * y, x))
        states[live_indices] = next_states
        remains_live = _inside_escape_box(next_states, escape_bound)
        newly_escaped = live_indices[~remains_live]
        if newly_escaped.size:
            active[newly_escaped] = False
            escape_steps[newly_escaped] = step_number

    for step in range(1, burn_in + 1):
        advance(step)

    tails = np.full((tail_length, n_trajectories, 2), np.nan, dtype=np.float64)
    for tail_index in range(tail_length):
        advance(burn_in + tail_index + 1)
        tails[tail_index, active] = states[active]

    labels = np.full(n_trajectories, "escape", dtype="<U24")
    periods = np.full(n_trajectories, -1, dtype=np.int64)
    recurrence_residuals = np.full(n_trajectories, np.nan, dtype=np.float64)
    survivor_indices = np.flatnonzero(active)
    if survivor_indices.size:
        detected, residuals = classify_periodic_tails(
            tails[:, survivor_indices, :],
            candidate_periods=range(1, max_period + 1),
            absolute_tolerance=absolute_tolerance,
            relative_tolerance=relative_tolerance,
        )
        periods[survivor_indices] = detected
        recurrence_residuals[survivor_indices] = residuals
        labels[survivor_indices] = "unresolved"
        for local_index, trajectory_index in enumerate(survivor_indices):
            period = int(detected[local_index])
            if period <= 0:
                continue
            if period == 1:
                final_x = float(states[trajectory_index, 0])
                distance_positive = abs(final_x - positive_fixed_point(a, rho))
                distance_negative = abs(final_x - negative_fixed_point(a, rho))
                labels[trajectory_index] = (
                    "fixed_positive"
                    if distance_positive <= distance_negative
                    else "fixed_negative"
                )
            else:
                labels[trajectory_index] = f"period_{period}"

    return AttractorRun(
        a=float(a),
        rho=float(rho),
        burn_in=int(burn_in),
        tail_length=int(tail_length),
        escape_bound=float(escape_bound),
        absolute_tolerance=float(absolute_tolerance),
        relative_tolerance=float(relative_tolerance),
        max_period=int(max_period),
        labels=labels,
        periods=periods,
        recurrence_residuals=recurrence_residuals,
        escape_steps=escape_steps,
        final_states=states.copy(),
    )


def summarize_attractor_run(run: AttractorRun) -> dict[str, object]:
    """Return a flat, JSON-safe summary of one run."""

    counts = run.counts
    summary: dict[str, object] = {
        "a": run.a,
        "rho": run.rho,
        "rho_flip": positive_fixed_point_flip_threshold(run.a),
        "fixed_point_jury_stable": all(
            margin > 0.0
            for margin in positive_fixed_point_jury_margins(run.a, run.rho).values()
        ),
        "n_trajectories": run.n_trajectories,
        "escaped": counts.get("escape", 0),
        "fixed_positive": counts.get("fixed_positive", 0),
        "fixed_negative": counts.get("fixed_negative", 0),
        "unresolved": counts.get("unresolved", 0),
    }
    for period in range(2, run.max_period + 1):
        summary[f"period_{period}"] = counts.get(f"period_{period}", 0)
    summary["resolved_periodic"] = int(
        run.n_trajectories
        - int(summary["escaped"])
        - int(summary["unresolved"])
    )
    return summary
