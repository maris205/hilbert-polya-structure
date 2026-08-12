#!/usr/bin/env python3
"""Independent DOP853 variational audit for B=0 and B=1 dynamics."""

from __future__ import annotations

import csv
import json
import math
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


TWO_PI = 2.0 * math.pi


def potential_jet(q: np.ndarray, a: float, n: int) -> tuple[float, np.ndarray, np.ndarray]:
    """Independent centered-Hénon value/gradient/Hessian implementation."""

    fixed = 1.0 / (1.0 + math.sqrt(1.0 + a))
    linear = -2.0 * a * fixed
    u = np.asarray(q, dtype=float).copy()
    jac = np.eye(2)
    component_hess = np.zeros((2, 2, 2))
    for _ in range(n):
        x, y = u
        j0, j1 = jac[0].copy(), jac[1].copy()
        h0, h1 = component_hess[0].copy(), component_hess[1].copy()
        slope = linear - 2.0 * a * x
        u = np.array([linear * x - a * x * x - y, x])
        jac = np.vstack((slope * j0 - j1, j0))
        component_hess = np.stack(
            (slope * h0 - h1 - 2.0 * a * np.outer(j0, j0), h0)
        )
    phi = math.pi * float(u @ u)
    value = TWO_PI * math.exp(phi)
    grad_phi = TWO_PI * (jac.T @ u)
    hess_phi = TWO_PI * (
        jac.T @ jac
        + u[0] * component_hess[0]
        + u[1] * component_hess[1]
    )
    return value, value * grad_phi, value * (
        hess_phi + np.outer(grad_phi, grad_phi)
    )


def run_one(task: dict) -> dict:
    q = np.array([task["q0"], task["q1"]], dtype=float)
    velocity = np.array([task["v0"], task["v1"]], dtype=float)
    q_scale = task["q_scale"]
    v_scale = task["v_scale"]
    scales = np.array([q_scale, q_scale, v_scale, v_scale])
    tangents = np.zeros((4, 2))
    tangents[0, 0] = q_scale
    tangents[3, 1] = v_scale
    state = np.concatenate((q, velocity, tangents.ravel(order="F")))
    magnetic_matrix = np.array([[0.0, task["field"]], [-task["field"], 0.0]])
    natural_scale = math.sqrt(math.log(task["energy"] / TWO_PI) / task["energy"])
    segment = 0.5 * natural_scale
    segments = 160
    accumulated = 0.0
    initial_value, _, _ = potential_jet(q, task["a"], task["n"])
    initial_energy = 0.5 * float(velocity @ velocity) + initial_value
    max_drift = 0.0

    def rhs(_time: float, packed: np.ndarray) -> np.ndarray:
        local_q = packed[:2]
        local_v = packed[2:4]
        local_tangents = packed[4:].reshape((4, 2), order="F")
        value, gradient, hessian = potential_jet(local_q, task["a"], task["n"])
        del value
        dq = local_tangents[:2]
        dv = local_tangents[2:]
        tangent_derivative = np.vstack((dv, magnetic_matrix @ dv - hessian @ dq))
        return np.concatenate(
            (
                local_v,
                magnetic_matrix @ local_v - gradient,
                tangent_derivative.ravel(order="F"),
            )
        )

    for _ in range(segments):
        solution = solve_ivp(
            rhs,
            (0.0, segment),
            state,
            method="DOP853",
            rtol=1.0e-10,
            atol=1.0e-12,
            max_step=segment / 16.0,
        )
        if not solution.success or not np.all(np.isfinite(solution.y[:, -1])):
            return {**task, "status": "integration_failure", "message": solution.message}
        state = solution.y[:, -1]
        tangents = state[4:].reshape((4, 2), order="F")
        for column in range(2):
            norm = float(np.linalg.norm(tangents[:, column] / scales))
            if column == 0:
                accumulated += math.log(norm)
            tangents[:, column] /= norm
        state[4:] = tangents.ravel(order="F")
        value, _, _ = potential_jet(state[:2], task["a"], task["n"])
        energy = 0.5 * float(state[2:4] @ state[2:4]) + value
        max_drift = max(max_drift, abs(energy - initial_energy) / initial_energy)

    scaled = tangents / scales[:, None]
    scaled /= np.linalg.norm(scaled, axis=0)[None, :]
    sali = float(
        min(
            np.linalg.norm(scaled[:, 0] - scaled[:, 1]),
            np.linalg.norm(scaled[:, 0] + scaled[:, 1]),
        )
    )
    return {
        **task,
        "status": "ok",
        "ftle_natural": float(accumulated / 80.0),
        "sali": sali,
        "max_relative_energy_drift": float(max_drift),
        "initial_energy_error": float(abs(initial_energy - task["energy"]) / task["energy"]),
    }


def main() -> int:
    r001_path = Path("results/r001_time_convergence/records.csv")
    with r001_path.open(newline="", encoding="utf-8") as handle:
        source_rows = list(csv.DictReader(handle))
    source = {
        (float(row["a"]), int(row["seed_index"])): row
        for row in source_rows
        if int(row["n"]) == 1
    }
    tasks = []
    for a in (0.0, 1.02):
        for field in (0.0, 1.0):
            for seed in range(4):
                row = source[(a, seed)]
                tasks.append(
                    {
                        "a": a,
                        "n": 1,
                        "field": field,
                        "seed_index": seed,
                        "energy": 1000.0,
                        "q0": float(row["initial_q0"]),
                        "q1": float(row["initial_q1"]),
                        "v0": float(row["initial_p0"]),
                        "v1": float(row["initial_p1"]),
                        "q_scale": float(row["q_scale"]),
                        "v_scale": float(row["p_scale"]),
                        "verlet_ftle_t80": float(row["ftle_natural_t80"]),
                    }
                )
    records = []
    with ProcessPoolExecutor(max_workers=min(16, os.cpu_count() or 1)) as pool:
        futures = {pool.submit(run_one, task): task for task in tasks}
        for future in as_completed(futures):
            records.append(future.result())
    records.sort(key=lambda row: (row["a"], row["field"], row["seed_index"]))

    groups = {}
    for a in (0.0, 1.02):
        for field in (0.0, 1.0):
            group = [row for row in records if row["a"] == a and row["field"] == field]
            groups[f"a={a}:B={field}"] = {
                "records": len(group),
                "valid_records": sum(
                    row["status"] == "ok"
                    and row["max_relative_energy_drift"] < 1.0e-8
                    for row in group
                ),
                "median_ftle_natural": float(np.median([row["ftle_natural"] for row in group])),
                "median_sali": float(np.median([row["sali"] for row in group])),
                "joint_flags": sum(
                    row["ftle_natural"] > 0.05 and row["sali"] < 1.0e-8
                    for row in group
                ),
                "max_energy_drift": max(row["max_relative_energy_drift"] for row in group),
            }
    nonlinear_b0 = groups["a=1.02:B=0.0"]
    verlet_median = float(
        np.median(
            [row["verlet_ftle_t80"] for row in records if row["a"] == 1.02 and row["field"] == 0.0]
        )
    )
    ratio = nonlinear_b0["median_ftle_natural"] / verlet_median
    gates = {
        "all_records_energy_valid": all(group["valid_records"] == 4 for group in groups.values()),
        "radial_B0_B1_zero_joint_flags": all(
            groups[key]["joint_flags"] == 0 for key in ("a=0.0:B=0.0", "a=0.0:B=1.0")
        ),
        "nonlinear_B0_B1_at_least_three_flags": all(
            groups[key]["joint_flags"] >= 3
            for key in ("a=1.02:B=0.0", "a=1.02:B=1.0")
        ),
        "DOP853_Verlet_median_ratio_in_band": 0.7 <= ratio <= 1.3,
    }
    output = {
        "groups": groups,
        "records": records,
        "nonlinear_B0_DOP853_to_Verlet_median_ratio": ratio,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "zero_data_loaded": False,
        "prime_data_loaded": False,
    }
    output_dir = Path("results/r106_adaptive_magnetic_dynamics")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "summary.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({"groups": groups, "ratio": ratio, "gates": gates}, indent=2))
    return 0 if output["all_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
