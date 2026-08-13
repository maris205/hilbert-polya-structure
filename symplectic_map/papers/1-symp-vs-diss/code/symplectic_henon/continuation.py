"""Small deterministic corrector for parameter-continuation diagnostics."""

from __future__ import annotations

from typing import Any, Iterable

import numpy as np
from numpy.typing import ArrayLike

from .cycles import cyclic_jacobian, cyclic_residual, numerical_minimal_period, solve_cycle


def continue_cycle(
    initial_q: ArrayLike,
    a: float,
    rho_values: Iterable[float],
    *,
    residual_tolerance: float = 1e-10,
) -> dict[str, Any]:
    """Correct a cycle sequentially on a caller-supplied ``rho`` grid.

    This routine is intentionally not advertised as pseudo-arclength
    continuation.  It stops at the first failed/singular corrector and records
    branch diagnostics, so a collision cannot silently be called survival.
    """

    q = np.asarray(initial_q, dtype=float).copy()
    points: list[dict[str, Any]] = []
    stopped_reason: str | None = None
    for rho in rho_values:
        corrected, solve = solve_cycle(q, a, float(rho), residual_tolerance=residual_tolerance)
        jacobian = cyclic_jacobian(corrected, a, float(rho))
        singular_values = np.linalg.svd(jacobian, compute_uv=False)
        smallest_singular_value = float(singular_values[-1])
        actual_period = numerical_minimal_period(corrected)
        accepted = bool(solve["accepted"] and actual_period == corrected.size)
        points.append(
            {
                "rho": float(rho),
                "accepted": accepted,
                "residual_inf": float(np.linalg.norm(cyclic_residual(corrected, a, float(rho)), ord=np.inf)),
                "minimal_period": int(actual_period),
                "smallest_corrector_singular_value": smallest_singular_value,
                "q": [float(value) for value in corrected],
            }
        )
        if not solve["accepted"]:
            stopped_reason = "corrector_failure"
            break
        if actual_period != corrected.size:
            stopped_reason = "branch_collapsed_to_lower_period"
            break
        if smallest_singular_value < 1e-9:
            stopped_reason = "near_singular_corrector"
            break
        q = corrected
    return {
        "method": "sequential_newton_corrector_not_pseudo_arclength",
        "period": int(np.asarray(initial_q).size),
        "points": points,
        "completed_grid": stopped_reason is None,
        "stopped_reason": stopped_reason,
    }
