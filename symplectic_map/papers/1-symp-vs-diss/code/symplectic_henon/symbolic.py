"""Frozen-seed symbolic transport diagnostics for the Hénon homotopy.

The experiment starts from states sampled from the parent quadratic map

    f_a(x) = 1 - a x**2

and evolves the matched two-dimensional family

    H_{a,rho}(x, y) = (1 - a x**2 - rho*y, x).

The singular endpoint ``rho=0`` exactly reproduces the parent scalar
dynamics in its first coordinate.  It is a reference, not an ordinary
symplectic continuation point.  The preregistered arithmetic shadow is the
parity of return gaps to the symbol ``L := {x < 0}``:

    P = (number of even gaps - number of odd gaps) / number of gaps.

All uncertainty intervals resample entire trajectories (cluster bootstrap),
so the strongly dependent observations inside a trajectory are never treated
as independent samples.

Split seeds are deliberately fixed here, independently of the results:

    train      20260811
    dev        20260812
    validation 20260813
    test       20260814

The confirmatory test split is locked by default.  Callers must pass
``allow_confirmatory_test=True`` explicitly to obtain it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

import numpy as np


FROZEN_A = 1.5436890126920763
RHO_GRID = (0.0, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0)
SPLIT_SEEDS: Mapping[str, int] = {
    "train": 20260811,
    "dev": 20260812,
    "validation": 20260813,
    "test": 20260814,
}
CONFIRMATORY_RHO = 1.0
CONFIRMATORY_EXPOSURE_GATE = 0.8
CONFIRMATORY_MIN_GAPS = 10_000
CONFIRMATORY_POLARITY_LOWER_BOUND = 0.98


def quadratic_step(x: np.ndarray | float, a: float = FROZEN_A):
    """One step of the scalar parent map ``f_a(x)=1-a*x^2``."""

    return 1.0 - a * np.asarray(x) ** 2


def henon_step(
    x: np.ndarray | float,
    y: np.ndarray | float,
    *,
    a: float = FROZEN_A,
    rho: float,
) -> tuple[np.ndarray, np.ndarray]:
    """One vectorized step of ``H_{a,rho}``."""

    x_array = np.asarray(x)
    y_array = np.asarray(y)
    return 1.0 - a * x_array**2 - rho * y_array, x_array.copy()


def split_seed(split: str, *, allow_confirmatory_test: bool = False) -> int:
    """Return the frozen seed for a split, enforcing the test-set lock."""

    try:
        seed = SPLIT_SEEDS[split]
    except KeyError as exc:
        choices = ", ".join(SPLIT_SEEDS)
        raise ValueError(f"unknown split {split!r}; choose one of {choices}") from exc
    if split == "test" and not allow_confirmatory_test:
        raise PermissionError(
            "the confirmatory test split is locked; explicitly set "
            "allow_confirmatory_test=True after the analysis is frozen"
        )
    return seed


def generate_parent_ensemble(
    *,
    split: str = "dev",
    n_trajectories: int = 2048,
    burn_in: int = 4096,
    a: float = FROZEN_A,
    allow_confirmatory_test: bool = False,
) -> np.ndarray:
    """Generate deterministic parent-map states ``(x_t, x_{t-1})``.

    Independent starting values are drawn uniformly from ``[-1, 1]`` with the
    frozen split seed and then burned in under the parent map.  Randomness is
    used only to sample initial conditions; the dynamics and all later
    statistics are deterministic conditional on the seed.
    """

    if n_trajectories <= 0:
        raise ValueError("n_trajectories must be positive")
    if burn_in < 1:
        raise ValueError("burn_in must be at least one")
    if not np.isfinite(a) or a <= 0:
        raise ValueError("a must be finite and positive")

    seed = split_seed(split, allow_confirmatory_test=allow_confirmatory_test)
    rng = np.random.default_rng(seed)
    previous = rng.uniform(-1.0, 1.0, size=n_trajectories)
    current = quadratic_step(previous, a)
    for _ in range(burn_in - 1):
        previous, current = current, quadratic_step(current, a)
    return np.column_stack((current, previous)).astype(np.float64, copy=False)


@dataclass(frozen=True)
class ClusterStatistics:
    """Per-trajectory sufficient statistics for clustered inference."""

    exposure_steps: np.ndarray
    survived: np.ndarray
    left_visits: np.ndarray
    even_gaps: np.ndarray
    odd_gaps: np.ndarray
    transitions: np.ndarray

    def __post_init__(self) -> None:
        n = len(self.exposure_steps)
        one_dimensional = (
            self.survived,
            self.left_visits,
            self.even_gaps,
            self.odd_gaps,
        )
        if any(array.shape != (n,) for array in one_dimensional):
            raise ValueError("all scalar cluster arrays must have shape (n,)")
        if self.transitions.shape != (n, 2, 2):
            raise ValueError("transitions must have shape (n, 2, 2)")

    @property
    def n_trajectories(self) -> int:
        return int(len(self.exposure_steps))

    @property
    def gap_counts(self) -> np.ndarray:
        return self.even_gaps + self.odd_gaps


@dataclass(frozen=True)
class TransportResult:
    """Complete output of one ``rho`` experiment."""

    a: float
    rho: float
    horizon: int
    escape_bound: float
    clusters: ClusterStatistics
    gap_histogram: np.ndarray
    escape_times: np.ndarray

    @property
    def exposure_fraction(self) -> float:
        denominator = self.clusters.n_trajectories * self.horizon
        return float(np.sum(self.clusters.exposure_steps) / denominator)

    @property
    def survival_fraction(self) -> float:
        return float(np.mean(self.clusters.survived))

    @property
    def even_gaps(self) -> int:
        return int(np.sum(self.clusters.even_gaps))

    @property
    def odd_gaps(self) -> int:
        return int(np.sum(self.clusters.odd_gaps))

    @property
    def total_gaps(self) -> int:
        return self.even_gaps + self.odd_gaps

    @property
    def parity_polarity(self) -> float:
        return parity_polarity(self.even_gaps, self.odd_gaps)

    @property
    def aggregate_transitions(self) -> np.ndarray:
        return np.sum(self.clusters.transitions, axis=0)

    @property
    def markov_null_polarity(self) -> float:
        return markov_return_polarity(self.aggregate_transitions)


def parity_polarity(even_gaps: int | float, odd_gaps: int | float) -> float:
    """Return ``(even-odd)/(even+odd)``, or NaN when there are no gaps."""

    total = even_gaps + odd_gaps
    if total <= 0:
        return float("nan")
    return float((even_gaps - odd_gaps) / total)


def markov_return_polarity(transitions: np.ndarray) -> float:
    """Parity polarity under the matched two-state first-order Markov null.

    ``transitions[i,j]`` counts observed transitions from symbol ``i`` to
    symbol ``j``, where ``0=R`` and ``1=L``.  The null preserves the empirical
    one-step transition probabilities but discards all longer memory.
    """

    counts = np.asarray(transitions, dtype=np.float64)
    if counts.shape != (2, 2):
        raise ValueError("transitions must have shape (2, 2)")
    row_sums = counts.sum(axis=1)
    if np.any(row_sums <= 0):
        return float("nan")
    probability = counts / row_sums[:, None]
    p_rr = probability[0, 0]
    p_rl = probability[0, 1]
    p_lr = probability[1, 0]
    p_ll = probability[1, 1]
    denominator = 1.0 - p_rr**2
    if denominator <= np.finfo(float).eps or p_rl <= 0:
        return float("nan")
    even_probability = p_lr * p_rl / denominator
    odd_probability = p_ll + p_lr * p_rl * p_rr / denominator
    normalizer = even_probability + odd_probability
    if normalizer <= 0:
        return float("nan")
    return float((even_probability - odd_probability) / normalizer)


def simulate_transport(
    initial_states: np.ndarray,
    *,
    rho: float,
    a: float = FROZEN_A,
    horizon: int = 1024,
    escape_bound: float = 100.0,
) -> TransportResult:
    """Simulate the Hénon homotopy and collect clustered symbol statistics.

    A state contributes one exposure at each scheduled observation for which
    both coordinates are finite and inside the escape box.  Once it leaves the
    box, the trajectory is permanently censored.  Return gaps and transitions
    are counted only inside the exposed prefix.
    """

    states = np.asarray(initial_states, dtype=np.float64)
    if states.ndim != 2 or states.shape[1] != 2 or states.shape[0] == 0:
        raise ValueError("initial_states must have nonempty shape (n, 2)")
    if not np.all(np.isfinite(states)):
        raise ValueError("initial_states must be finite")
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if not np.isfinite(escape_bound) or escape_bound <= 0:
        raise ValueError("escape_bound must be finite and positive")
    if not np.isfinite(rho) or rho < 0:
        raise ValueError("rho must be finite and nonnegative")

    n = states.shape[0]
    x = states[:, 0].copy()
    y = states[:, 1].copy()
    active = (np.abs(x) <= escape_bound) & (np.abs(y) <= escape_bound)

    exposure_steps = np.zeros(n, dtype=np.int64)
    left_visits = np.zeros(n, dtype=np.int64)
    even_gaps = np.zeros(n, dtype=np.int64)
    odd_gaps = np.zeros(n, dtype=np.int64)
    transitions = np.zeros((n, 2, 2), dtype=np.int64)
    gap_histogram = np.zeros(horizon + 1, dtype=np.int64)
    escape_times = np.full(n, horizon, dtype=np.int64)
    escape_times[~active] = 0

    last_left = np.full(n, -1, dtype=np.int64)
    previous_symbol = np.full(n, -1, dtype=np.int8)
    indices = np.arange(n)

    for time_index in range(horizon):
        active_indices = indices[active]
        if active_indices.size == 0:
            break

        exposure_steps[active_indices] += 1
        current_symbol = (x[active_indices] < 0.0).astype(np.int8)

        has_previous = previous_symbol[active_indices] >= 0
        transition_indices = active_indices[has_previous]
        if transition_indices.size:
            old_symbol = previous_symbol[transition_indices]
            new_symbol = current_symbol[has_previous]
            np.add.at(
                transitions,
                (transition_indices, old_symbol, new_symbol),
                1,
            )
        previous_symbol[active_indices] = current_symbol

        local_left = current_symbol == 1
        left_indices = active_indices[local_left]
        if left_indices.size:
            left_visits[left_indices] += 1
            has_last_left = last_left[left_indices] >= 0
            gap_indices = left_indices[has_last_left]
            if gap_indices.size:
                gaps = time_index - last_left[gap_indices]
                gap_is_even = (gaps % 2) == 0
                even_gaps[gap_indices[gap_is_even]] += 1
                odd_gaps[gap_indices[~gap_is_even]] += 1
                gap_histogram += np.bincount(gaps, minlength=horizon + 1)
            last_left[left_indices] = time_index

        with np.errstate(over="ignore", invalid="ignore"):
            next_x = 1.0 - a * x[active_indices] ** 2 - rho * y[active_indices]
        next_y = x[active_indices]
        next_finite = np.isfinite(next_x) & np.isfinite(next_y)
        next_inside = (
            next_finite
            & (np.abs(next_x) <= escape_bound)
            & (np.abs(next_y) <= escape_bound)
        )
        x[active_indices] = next_x
        y[active_indices] = next_y

        escaped_indices = active_indices[~next_inside]
        if escaped_indices.size:
            escape_times[escaped_indices] = time_index + 1
            active[escaped_indices] = False

    clusters = ClusterStatistics(
        exposure_steps=exposure_steps,
        survived=active,
        left_visits=left_visits,
        even_gaps=even_gaps,
        odd_gaps=odd_gaps,
        transitions=transitions,
    )
    return TransportResult(
        a=float(a),
        rho=float(rho),
        horizon=int(horizon),
        escape_bound=float(escape_bound),
        clusters=clusters,
        gap_histogram=gap_histogram,
        escape_times=escape_times,
    )


def _percentile_interval(
    values: Iterable[float], *, ci_level: float
) -> tuple[float, float]:
    array = np.asarray(tuple(values), dtype=np.float64)
    array = array[np.isfinite(array)]
    if array.size == 0:
        return float("nan"), float("nan")
    alpha = 1.0 - ci_level
    lower, upper = np.quantile(array, [alpha / 2.0, 1.0 - alpha / 2.0])
    return float(lower), float(upper)


def cluster_bootstrap(
    result: TransportResult,
    *,
    n_replicates: int = 2000,
    seed: int = 0,
    ci_level: float = 0.95,
    chunk_size: int = 128,
) -> dict[str, tuple[float, float]]:
    """Cluster-bootstrap intervals for the main and censoring statistics."""

    if n_replicates <= 0:
        raise ValueError("n_replicates must be positive")
    if not 0.0 < ci_level < 1.0:
        raise ValueError("ci_level must lie strictly between zero and one")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    clusters = result.clusters
    n = clusters.n_trajectories
    rng = np.random.default_rng(seed)
    parity_values: list[float] = []
    exposure_values: list[float] = []
    survival_values: list[float] = []
    markov_values: list[float] = []

    completed = 0
    while completed < n_replicates:
        batch_size = min(chunk_size, n_replicates - completed)
        samples = rng.integers(0, n, size=(batch_size, n))
        even = clusters.even_gaps[samples].sum(axis=1)
        odd = clusters.odd_gaps[samples].sum(axis=1)
        total = even + odd
        with np.errstate(divide="ignore", invalid="ignore"):
            parity = (even - odd) / total
        parity_values.extend(parity.tolist())
        exposure_values.extend(
            (
                clusters.exposure_steps[samples].sum(axis=1)
                / (n * result.horizon)
            ).tolist()
        )
        survival_values.extend(clusters.survived[samples].mean(axis=1).tolist())
        batch_transitions = clusters.transitions[samples].sum(axis=1)
        markov_values.extend(
            markov_return_polarity(counts) for counts in batch_transitions
        )
        completed += batch_size

    return {
        "parity_polarity": _percentile_interval(
            parity_values, ci_level=ci_level
        ),
        "exposure_fraction": _percentile_interval(
            exposure_values, ci_level=ci_level
        ),
        "survival_fraction": _percentile_interval(
            survival_values, ci_level=ci_level
        ),
        "markov_null_polarity": _percentile_interval(
            markov_values, ci_level=ci_level
        ),
    }


def summarize_result(
    result: TransportResult,
    *,
    intervals: Mapping[str, tuple[float, float]] | None = None,
    exposure_gate: float = CONFIRMATORY_EXPOSURE_GATE,
) -> dict[str, object]:
    """Produce a JSON/CSV-friendly summary for one ``rho`` value."""

    markov_null = result.markov_null_polarity
    observed = result.parity_polarity
    exposure = result.exposure_fraction
    summary: dict[str, object] = {
        "a": result.a,
        "rho": result.rho,
        "horizon": result.horizon,
        "n_trajectories": result.clusters.n_trajectories,
        "escape_bound": result.escape_bound,
        "exposure_fraction": exposure,
        "survival_fraction": result.survival_fraction,
        "left_visits": int(np.sum(result.clusters.left_visits)),
        "even_gaps": result.even_gaps,
        "odd_gaps": result.odd_gaps,
        "total_gaps": result.total_gaps,
        "parity_polarity": observed,
        "markov_null_polarity": markov_null,
        "parity_excess_over_markov": observed - markov_null,
        "exposure_gate": exposure_gate,
        "exposure_gate_passed": bool(exposure >= exposure_gate),
        "gap_histogram": {
            str(index): int(count)
            for index, count in enumerate(result.gap_histogram)
            if index > 0 and count > 0
        },
    }
    if intervals is not None:
        for name, interval in intervals.items():
            summary[f"{name}_ci_low"] = float(interval[0])
            summary[f"{name}_ci_high"] = float(interval[1])
    return summary


def evaluate_confirmatory_endpoint(
    summary: Mapping[str, object],
    *,
    split: str,
    neighbor_specificity_passed: bool | None = None,
    exposure_gate: float = CONFIRMATORY_EXPOSURE_GATE,
    minimum_gaps: int = CONFIRMATORY_MIN_GAPS,
    polarity_lower_bound: float = CONFIRMATORY_POLARITY_LOWER_BOUND,
    protocol_deviations: Iterable[str] = (),
) -> dict[str, object]:
    """Evaluate each preregistered constituent of the endpoint decision.

    Neighbor specificity is supplied by the across-parameter analysis and is
    therefore ``None`` in a single-parameter run.  A final pass is possible
    only on the explicitly unlocked test split, with no protocol deviations,
    after that Holm-corrected comparison is available.
    """

    deviations = tuple(protocol_deviations)
    exposure = float(summary["exposure_fraction"])
    total_gaps = int(summary["total_gaps"])
    lower_ci_raw = summary.get("parity_polarity_ci_low")
    lower_ci = (
        float(lower_ci_raw) if lower_ci_raw is not None else float("nan")
    )
    exposure_passed = exposure >= exposure_gate
    gap_count_passed = total_gaps >= minimum_gaps
    lower_ci_passed = bool(
        np.isfinite(lower_ci) and lower_ci >= polarity_lower_bound
    )
    availability_passed = exposure_passed and gap_count_passed
    constituents_complete = neighbor_specificity_passed is not None
    all_scientific_gates_passed = bool(
        availability_passed
        and lower_ci_passed
        and neighbor_specificity_passed is True
    )
    confirmatory_passed = bool(
        split == "test"
        and not deviations
        and constituents_complete
        and all_scientific_gates_passed
    )

    if deviations:
        status = "protocol_deviation"
    elif split != "test":
        status = "exploratory_only"
    elif not availability_passed:
        status = "a0_shadow_fail_carrier_unavailable"
    elif not lower_ci_passed:
        status = "a0_shadow_fail_polarity"
    elif neighbor_specificity_passed is None:
        status = "pending_neighbor_specificity"
    elif neighbor_specificity_passed is False:
        status = "a0_shadow_fail_nonspecific"
    else:
        status = "confirmatory_pass"

    return {
        "rho": CONFIRMATORY_RHO,
        "metric": "parity_polarity",
        "value": summary.get("parity_polarity"),
        "ci_low": summary.get("parity_polarity_ci_low"),
        "ci_high": summary.get("parity_polarity_ci_high"),
        "exposure_fraction": exposure,
        "exposure_gate": exposure_gate,
        "exposure_gate_passed": exposure_passed,
        "total_gaps": total_gaps,
        "minimum_gaps": minimum_gaps,
        "gap_count_gate_passed": gap_count_passed,
        "availability_gate_passed": availability_passed,
        "polarity_ci_lower_bound": polarity_lower_bound,
        "polarity_ci_gate_passed": lower_ci_passed,
        "neighbor_specificity_gate_passed": neighbor_specificity_passed,
        "protocol_deviations": list(deviations),
        "confirmatory_passed": confirmatory_passed,
        "status": status,
    }
