"""Cluster-aware analysis helpers for the frozen transport experiment.

The functions in this module operate only on per-trajectory sufficient
statistics.  In particular, they never treat return gaps within one chaotic
trajectory as independent observations.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import math

import numpy as np


@dataclass(frozen=True)
class ClusterBlock:
    """Sufficient statistics for one parameter arm and one rho value."""

    trajectory_id: np.ndarray
    exposure_steps: np.ndarray
    survived: np.ndarray
    even_gaps: np.ndarray
    odd_gaps: np.ndarray

    def __post_init__(self) -> None:
        arrays = (
            self.trajectory_id,
            self.exposure_steps,
            self.survived,
            self.even_gaps,
            self.odd_gaps,
        )
        n = len(self.trajectory_id)
        if n == 0 or any(array.shape != (n,) for array in arrays):
            raise ValueError("cluster arrays must be nonempty one-dimensional arrays")
        if len(np.unique(self.trajectory_id)) != n:
            raise ValueError("trajectory_id values must be unique within a block")
        if np.any(self.exposure_steps < 0):
            raise ValueError("exposure_steps must be nonnegative")
        if np.any(self.even_gaps < 0) or np.any(self.odd_gaps < 0):
            raise ValueError("gap counts must be nonnegative")

    @property
    def n_trajectories(self) -> int:
        return int(len(self.trajectory_id))


def polarity(even: np.ndarray | float, odd: np.ndarray | float):
    """Compute ``(even-odd)/(even+odd)`` with NaN for empty totals."""

    even_array = np.asarray(even, dtype=np.float64)
    odd_array = np.asarray(odd, dtype=np.float64)
    total = even_array + odd_array
    with np.errstate(divide="ignore", invalid="ignore"):
        value = (even_array - odd_array) / total
    if value.ndim == 0:
        return float(value) if total > 0 else float("nan")
    return np.where(total > 0, value, np.nan)


def odd_risk(even: np.ndarray | float, odd: np.ndarray | float):
    """Compute the fraction of return gaps with odd length."""

    even_array = np.asarray(even, dtype=np.float64)
    odd_array = np.asarray(odd, dtype=np.float64)
    total = even_array + odd_array
    with np.errstate(divide="ignore", invalid="ignore"):
        value = odd_array / total
    if value.ndim == 0:
        return float(value) if total > 0 else float("nan")
    return np.where(total > 0, value, np.nan)


def log_odd_gap_odds_ratio(
    primary_even: np.ndarray | float,
    primary_odd: np.ndarray | float,
    control_even: np.ndarray | float,
    control_odd: np.ndarray | float,
):
    """Log odd-gap odds ratio, using a fixed Haldane 0.5 correction.

    Negative values favor the primary arm because they indicate fewer odd
    return gaps.  The correction is fixed in advance and keeps boundary cases
    with zero odd gaps finite.
    """

    pe = np.asarray(primary_even, dtype=np.float64)
    po = np.asarray(primary_odd, dtype=np.float64)
    ce = np.asarray(control_even, dtype=np.float64)
    co = np.asarray(control_odd, dtype=np.float64)
    value = np.log((po + 0.5) / (pe + 0.5)) - np.log(
        (co + 0.5) / (ce + 0.5)
    )
    return float(value) if value.ndim == 0 else value


def _interval(values: np.ndarray, ci_level: float) -> tuple[float, float]:
    finite = np.asarray(values, dtype=np.float64)
    finite = finite[np.isfinite(finite)]
    if finite.size == 0:
        return float("nan"), float("nan")
    alpha = 1.0 - ci_level
    low, high = np.quantile(finite, [alpha / 2.0, 1.0 - alpha / 2.0])
    return float(low), float(high)


def _aggregate(block: ClusterBlock, horizon: int) -> dict[str, float]:
    even = float(np.sum(block.even_gaps))
    odd = float(np.sum(block.odd_gaps))
    return {
        "polarity": polarity(even, odd),
        "odd_risk": odd_risk(even, odd),
        "exposure": float(
            np.sum(block.exposure_steps) / (block.n_trajectories * horizon)
        ),
        "survival": float(np.mean(block.survived)),
        "even": even,
        "odd": odd,
    }


def align_pair(
    primary: ClusterBlock, control: ClusterBlock
) -> tuple[ClusterBlock, ClusterBlock]:
    """Return blocks sorted into exactly the same trajectory-id order."""

    primary_order = np.argsort(primary.trajectory_id)
    control_order = np.argsort(control.trajectory_id)
    primary_ids = primary.trajectory_id[primary_order]
    control_ids = control.trajectory_id[control_order]
    if not np.array_equal(primary_ids, control_ids):
        raise ValueError("paired arms must contain identical trajectory_id values")

    def sorted_block(block: ClusterBlock, order: np.ndarray) -> ClusterBlock:
        return ClusterBlock(
            trajectory_id=block.trajectory_id[order],
            exposure_steps=block.exposure_steps[order],
            survived=block.survived[order],
            even_gaps=block.even_gaps[order],
            odd_gaps=block.odd_gaps[order],
        )

    return sorted_block(primary, primary_order), sorted_block(control, control_order)


def paired_cluster_bootstrap(
    primary: ClusterBlock,
    control: ClusterBlock,
    *,
    horizon: int,
    n_replicates: int,
    seed: int,
    ci_level: float = 0.95,
    chunk_size: int = 128,
) -> dict[str, float | int]:
    """Estimate paired arm differences by whole-trajectory bootstrap.

    A single bootstrap index vector is applied to both arms, preserving the
    common-random-number pairing. The one-sided directional diagnostic is the
    bootstrap probability of a nonpositive paired contrast for the
    preregistered direction ``P(primary) > P(control)``. It is not an exact
    randomized-treatment p-value because the parameter arms were not randomized;
    Holm adjustment is retained as a conservative family-wise screen.
    """

    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if n_replicates <= 0:
        raise ValueError("n_replicates must be positive")
    if not 0.0 < ci_level < 1.0:
        raise ValueError("ci_level must lie strictly between zero and one")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    primary, control = align_pair(primary, control)
    n = primary.n_trajectories
    primary_point = _aggregate(primary, horizon)
    control_point = _aggregate(control, horizon)
    point = {
        "polarity_difference": primary_point["polarity"]
        - control_point["polarity"],
        "odd_risk_difference": primary_point["odd_risk"]
        - control_point["odd_risk"],
        "exposure_difference": primary_point["exposure"]
        - control_point["exposure"],
        "survival_difference": primary_point["survival"]
        - control_point["survival"],
        "log_odd_gap_odds_ratio": log_odd_gap_odds_ratio(
            primary_point["even"],
            primary_point["odd"],
            control_point["even"],
            control_point["odd"],
        ),
    }

    draws: dict[str, list[np.ndarray]] = {name: [] for name in point}
    rng = np.random.default_rng(seed)
    completed = 0
    while completed < n_replicates:
        batch_size = min(chunk_size, n_replicates - completed)
        indices = rng.integers(0, n, size=(batch_size, n))

        pe = primary.even_gaps[indices].sum(axis=1)
        po = primary.odd_gaps[indices].sum(axis=1)
        ce = control.even_gaps[indices].sum(axis=1)
        co = control.odd_gaps[indices].sum(axis=1)

        draws["polarity_difference"].append(
            polarity(pe, po) - polarity(ce, co)
        )
        draws["odd_risk_difference"].append(
            odd_risk(pe, po) - odd_risk(ce, co)
        )
        draws["exposure_difference"].append(
            (
                primary.exposure_steps[indices].sum(axis=1)
                - control.exposure_steps[indices].sum(axis=1)
            )
            / (n * horizon)
        )
        draws["survival_difference"].append(
            primary.survived[indices].mean(axis=1)
            - control.survived[indices].mean(axis=1)
        )
        draws["log_odd_gap_odds_ratio"].append(
            log_odd_gap_odds_ratio(pe, po, ce, co)
        )
        completed += batch_size

    output: dict[str, float | int] = {
        "bootstrap_replicates": int(n_replicates),
        "paired_trajectories": int(n),
    }
    arrays: dict[str, np.ndarray] = {}
    for name, batches in draws.items():
        values = np.concatenate(batches)
        arrays[name] = values
        low, high = _interval(values, ci_level)
        output[name] = float(point[name])
        output[f"{name}_ci_low"] = low
        output[f"{name}_ci_high"] = high

    delta = arrays["polarity_difference"]
    finite = delta[np.isfinite(delta)]
    observed = float(point["polarity_difference"])
    if finite.size == 0 or not math.isfinite(observed):
        one_sided_p = float("nan")
    else:
        one_sided_p = float(
            (1 + np.count_nonzero(finite <= 0.0))
            / (finite.size + 1)
        )
    output["polarity_one_sided_bootstrap_p"] = one_sided_p
    return output


def holm_adjust(p_values: Mapping[str, float]) -> dict[str, float]:
    """Return Holm family-wise adjusted p-values, preserving input keys."""

    if not p_values:
        return {}
    for value in p_values.values():
        if not math.isfinite(value) or not 0.0 <= value <= 1.0:
            raise ValueError("Holm inputs must be finite p-values in [0,1]")
    ordered = sorted(p_values.items(), key=lambda item: (item[1], item[0]))
    family_size = len(ordered)
    adjusted: dict[str, float] = {}
    running_max = 0.0
    for rank, (name, value) in enumerate(ordered):
        candidate = min(1.0, (family_size - rank) * value)
        running_max = max(running_max, candidate)
        adjusted[name] = running_max
    return {name: adjusted[name] for name in p_values}


def fixed_grid_transition(
    rows: Sequence[Mapping[str, float]], *, exposure_gate: float
) -> dict[str, object]:
    """Bracket a transition using only adjacent points on the frozen rho grid."""

    if len(rows) < 2:
        raise ValueError("at least two fixed-grid rows are required")
    ordered = sorted(rows, key=lambda row: float(row["rho"]))
    changes: list[dict[str, float]] = []
    for left, right in zip(ordered[:-1], ordered[1:], strict=True):
        changes.append(
            {
                "rho_left": float(left["rho"]),
                "rho_right": float(right["rho"]),
                "polarity_change": float(right["parity_polarity"])
                - float(left["parity_polarity"]),
                "exposure_change": float(right["exposure_fraction"])
                - float(left["exposure_fraction"]),
            }
        )
    polarity_largest = max(changes, key=lambda row: abs(row["polarity_change"]))
    exposure_largest = max(changes, key=lambda row: abs(row["exposure_change"]))
    crossings = [
        {
            "rho_left": change["rho_left"],
            "rho_right": change["rho_right"],
        }
        for change, left, right in zip(
            changes, ordered[:-1], ordered[1:], strict=True
        )
        if (float(left["exposure_fraction"]) >= exposure_gate)
        != (float(right["exposure_fraction"]) >= exposure_gate)
    ]
    return {
        "method": (
            "largest adjacent absolute change and exposure-gate crossings on "
            "the preregistered grid; no parameter or continuous change point fitted"
        ),
        "adjacent_changes": changes,
        "largest_polarity_change_interval": [
            polarity_largest["rho_left"],
            polarity_largest["rho_right"],
        ],
        "largest_exposure_change_interval": [
            exposure_largest["rho_left"],
            exposure_largest["rho_right"],
        ],
        "exposure_gate_crossing_intervals": crossings,
    }
