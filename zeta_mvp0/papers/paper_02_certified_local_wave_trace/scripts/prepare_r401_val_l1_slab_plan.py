#!/usr/bin/env python3
"""Prepare rational centers for the R401-VAL-L1 overlapping slab chain.

The centers are numerical accelerators only.  No scientific claim uses their
floating-point accuracy; every accepted slab must later pass a validated
parameterized Krawczyk inclusion.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from math import pi, sqrt
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root


ROOT = Path(__file__).resolve().parents[1]
A = 1.02
C = 2.0 * (sqrt(1.0 + A) - 1.0)
LINEAR = np.array([[-C, -1.0], [1.0, 0.0]])
METRIC = LINEAR.T @ LINEAR
LAMBDAS, NUMPY_VECTORS = np.linalg.eigh(METRIC)

# Protocol orientation, not NumPy's arbitrary sign convention.
SLOW_RAW = np.array([1.0 - LAMBDAS[0], -C])
FAST_RAW = np.array([LAMBDAS[1] - 1.0, C])
E_SLOW = SLOW_RAW / np.linalg.norm(SLOW_RAW)
E_FAST = FAST_RAW / np.linalg.norm(FAST_RAW)
O = np.column_stack((E_SLOW, E_FAST))
OMEGAS = 2.0 * pi * np.sqrt(LAMBDAS)


def vector_field(state: np.ndarray, epsilon: float) -> np.ndarray:
    q = state[:2]
    p = state[2:]
    w = np.array([-C * q[0] - q[1] - A * epsilon * q[0] ** 2, q[0]])
    jacobian = np.array(
        [[-C - 2.0 * A * epsilon * q[0], -1.0], [1.0, 0.0]]
    )
    exponential = np.exp(pi * epsilon**2 * float(w @ w))
    gradient = 4.0 * pi**2 * exponential * (jacobian.T @ w)
    return np.concatenate((p, -gradient))


def energy(state: np.ndarray, epsilon: float) -> float:
    q = state[:2]
    p = state[2:]
    w = np.array([-C * q[0] - q[1] - A * epsilon * q[0] ** 2, q[0]])
    squared_radius = float(w @ w)
    if epsilon == 0.0:
        potential = 2.0 * pi**2 * squared_radius
    else:
        potential = (
            2.0 * pi / epsilon**2
            * np.expm1(pi * epsilon**2 * squared_radius)
        )
    return 0.5 * float(p @ p) + potential


def residual(unknown: np.ndarray, epsilon: float) -> np.ndarray:
    q = O @ unknown[:2]
    p = O @ np.array([unknown[2], 0.0])
    state0 = np.concatenate((q, p))
    solution = solve_ivp(
        lambda _time, state: vector_field(state, epsilon),
        (0.0, float(unknown[3])),
        state0,
        method="DOP853",
        rtol=2.0e-12,
        atol=2.0e-14,
        max_step=float(unknown[3]) / 320.0,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    terminal = solution.y[:, -1]
    q_terminal = O.T @ terminal[:2]
    p_terminal = O.T @ terminal[2:]
    return np.array(
        [
            energy(state0, epsilon) - 1.0,
            q_terminal[0] - unknown[0],
            p_terminal[0] - unknown[2],
            p_terminal[1],
        ]
    )


def slab_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    seed = np.array(
        [0.0, sqrt(2.0) / OMEGAS[1], 0.0, 1.0 / sqrt(LAMBDAS[1])]
    )
    centers = [0.001 + 0.002 * index for index in range(50)] + [0.1005]
    for index, epsilon in enumerate(centers):
        solved = root(lambda value: residual(value, epsilon), seed, tol=1.0e-11)
        if not solved.success and np.max(np.abs(solved.fun)) > 1.0e-9:
            raise RuntimeError(f"root failure at epsilon={epsilon}: {solved.message}")
        seed = solved.x
        lower = max(0.0, epsilon - 0.0011)
        upper = min(0.101, epsilon + 0.0011)
        records.append(
            {
                "slab_id": f"S{index:03d}",
                "epsilon_lower": f"{lower:.4f}",
                "epsilon_upper": f"{upper:.4f}",
                "center": {
                    "q_slow": f"{seed[0]:.18g}",
                    "q_fast": f"{seed[1]:.18g}",
                    "p_slow": "0",
                    "period": f"{seed[3]:.18g}",
                },
                "root_radii": {
                    "q_slow": "0.00004",
                    "q_fast": "0.00002",
                    "p_slow": "0.00008",
                    "period": "0.00002",
                },
                "floating_residual_inf": float(np.max(np.abs(residual(seed, epsilon)))),
            }
        )
    return records


def bridge_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Build guarded decimal hull boxes on every adjacent epsilon overlap."""

    coordinate_keys = ("q_slow", "q_fast", "p_slow", "period")
    guard = Decimal("1e-18")
    bridges: list[dict[str, object]] = []
    with localcontext() as context:
        context.prec = 60
        for index, (left, right) in enumerate(zip(records, records[1:])):
            epsilon_lower = max(
                Decimal(str(left["epsilon_lower"])),
                Decimal(str(right["epsilon_lower"])),
            )
            epsilon_upper = min(
                Decimal(str(left["epsilon_upper"])),
                Decimal(str(right["epsilon_upper"])),
            )
            if not epsilon_lower < epsilon_upper:
                raise RuntimeError(f"nonpositive overlap at bridge {index}")
            center: dict[str, str] = {}
            radii: dict[str, str] = {}
            for key in coordinate_keys:
                left_center = Decimal(str(left["center"][key]))
                left_radius = Decimal(str(left["root_radii"][key]))
                right_center = Decimal(str(right["center"][key]))
                right_radius = Decimal(str(right["root_radii"][key]))
                lower = min(left_center - left_radius, right_center - right_radius)
                upper = max(left_center + left_radius, right_center + right_radius)
                center[key] = format((lower + upper) / 2, "f")
                radii[key] = format((upper - lower) / 2 + guard, "f")
            bridges.append(
                {
                    "bridge_id": f"B{index:03d}",
                    "left_slab_id": str(left["slab_id"]),
                    "right_slab_id": str(right["slab_id"]),
                    "epsilon_lower": format(epsilon_lower, "f"),
                    "epsilon_upper": format(epsilon_upper, "f"),
                    "center": center,
                    "root_radii": radii,
                    "construction": (
                        "coordinatewise hull of adjacent primary root boxes "
                        "with 1e-18 rational padding on every side"
                    ),
                    "hull_padding": "0.000000000000000001",
                }
            )
    return bridges


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "research/route_a_wave_trace/R401_VAL_L1_SLAB_PLAN.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite plan: {output}")
    records = slab_records()
    overlap_widths = [
        float(records[index]["epsilon_upper"])
        - float(records[index + 1]["epsilon_lower"])
        for index in range(len(records) - 1)
    ]
    bridges = bridge_records(records)
    plan = {
        "protocol_id": "R401-VAL-V2",
        "milestone_id": "R401-VAL-L1",
        "claim_boundary": (
            "prospective local-branch continuation only; centers are nonrigorous "
            "and every slab still requires validated Krawczyk inclusion"
        ),
        "coverage": ["0", "0.101"],
        "slab_count": len(records),
        "bridge_count": len(bridges),
        "bridge_hull_padding": "0.000000000000000001",
        "minimum_positive_overlap": min(overlap_widths),
        "all_floating_residuals_lt_1e-9": all(
            record["floating_residual_inf"] < 1.0e-9 for record in records
        ),
        "slabs": records,
        "bridges": bridges,
    }
    output.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(output),
                "slabs": len(records),
                "bridges": len(bridges),
                "max_float_residual": max(
                    record["floating_residual_inf"] for record in records
                ),
                "minimum_overlap": min(overlap_widths),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
