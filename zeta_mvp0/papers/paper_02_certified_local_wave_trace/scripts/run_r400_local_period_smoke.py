#!/usr/bin/env python3
"""Execute the frozen R400 near-well period/action smoke matrix."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import scipy

from hp_candidate_search.local_periodic_orbits import (
    OrbitSearchSpec,
    fast_normal_form_data,
    normal_mode_data,
    shoot_brake_orbit,
)


ENERGY_EXCESSES = (0.01, 0.02, 0.05, 0.10, 0.20, 0.40)
PERIOD_WINDOW = (0.60, 0.75)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _cell_name(excess: float) -> str:
    return f"delta_{excess:.2f}".replace(".", "p")


def _fit_intercept(x: np.ndarray, y: np.ndarray) -> tuple[float, list[float]]:
    coefficients = np.polyfit(x, y, deg=2)
    return float(coefficients[-1]), [float(value) for value in coefficients]


def _report(summary: dict[str, Any]) -> str:
    mode = summary["normal_mode"]
    fits = summary["asymptotic_fits"]
    normal_form = summary["fast_normal_form"]
    rows = []
    for cell in summary["cells"]:
        rows.append(
            "| {delta:.2f} | {period:.12f} | {action:.12f} | "
            "{determinant:.12f} | {closure:.2e} | {status} |".format(
                delta=cell["energy_excess"],
                period=cell["period"],
                action=cell["action"],
                determinant=cell["transverse_stability_determinant"]["real"],
                closure=cell["max_scaled_closure"],
                status="PASS" if cell["all_cell_gates_pass"] else "FAIL",
            )
        )
    status = "PASS" if summary["all_gates_pass"] else "FAIL"
    return rf"""# R400 Near-Well Period/Action Smoke Report

## Decision

\[
\boxed{{\text{{R400 numerical/asymptotic smoke {status}; arithmetic P not evaluated.}}}}
\]

The run used no prime table, von Mangoldt values, zeta zeros, or spectral
peak locations.  It certifies a reversible classical orbit family near the
bottom of the fixed \(a=1.02\) one-step Hénon-warped well.

## Analytic oracle

| Quantity | Value |
|---|---:|
| \(c_a\) | {mode['c']:.15f} |
| \(s_-\) | {mode['singular_values'][0]:.15f} |
| \(s_+\) | {mode['singular_values'][1]:.15f} |
| \(T_+^0\) | {mode['periods'][1]:.15f} |
| \(D_+^0\) | {mode['fast_stability_determinant']:.15f} |
| \(T_+^0/\sqrt{{D_+^0}}\) | {mode['fast_trace_amplitude']:.15f} |
| \(dT_+/dE\vert_{{2\pi}}\) | {normal_form['period_energy_slope']:.15f} |
| \(d(S_+/\delta)/d\delta\vert_0\) | {normal_form['action_ratio_energy_slope']:.15f} |

## Cells

| \(E-2\pi\) | Period | Action | \(\det(I-P)\) | Scaled closure | Gate |
|---:|---:|---:|---:|---:|:---:|
{chr(10).join(rows)}

Worst numerical diagnostics were:

- shooting residual: `{summary['worst_numerics']['max_abs_shooting_residual']:.3e}`;
- scaled closure: `{summary['worst_numerics']['max_scaled_closure']:.3e}`;
- energy drift/excess: `{summary['worst_numerics']['max_energy_drift_over_excess']:.3e}`;
- symplectic defect: `{summary['worst_numerics']['symplectic_defect_inf']:.3e}`.

## Small-energy extrapolation

Quadratic fits use only \(\delta=0.01,0.02,0.05\).

| Quantity | Fitted intercept | Exact intercept | Absolute error | Gate |
|---|---:|---:|---:|:---:|
| \(T_+(\delta)\) | {fits['period']['intercept']:.15f} | {fits['period']['oracle']:.15f} | {fits['period']['absolute_error']:.3e} | {'PASS' if fits['period']['pass'] else 'FAIL'} |
| \(S_+(\delta)/\delta\) | {fits['action_ratio']['intercept']:.15f} | {fits['action_ratio']['oracle']:.15f} | {fits['action_ratio']['absolute_error']:.3e} | {'PASS' if fits['action_ratio']['pass'] else 'FAIL'} |
| \(\det(I-P)\) | {fits['stability']['intercept']:.15f} | {fits['stability']['oracle']:.15f} | {fits['stability']['absolute_error']:.3e} | {'PASS' if fits['stability']['pass'] else 'FAIL'} |

The fitted first slopes are `{fits['period']['slope']:.15f}` for the period
and `{fits['action_ratio']['slope']:.15f}` for \(S/\delta\), versus the
Poincaré--Lindstedt oracles `{fits['period']['slope_oracle']:.15f}` and
`{fits['action_ratio']['slope_oracle']:.15f}`.

The entire computed branch remains in the preregistered physical-time window
\([0.60,0.75]\), separated from the radial harmonic return time \(1\).

## Claim boundary

A pass is a numerical certificate for the local period, action, monodromy,
and limiting Gutzwiller amplitude.  The analytic promotion still requires
the written Lyapunov-centre and microlocal trace arguments.  Even after that
promotion, the result is a **fixed-energy semiclassical local trace bridge**,
not the high-energy fixed-time prime-power bridge.  No Hilbert--Pólya,
zeta-zero, prime trace, or RH claim follows.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/r400_local_period_smoke"),
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = args.output if args.output.is_absolute() else root / args.output
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing result: {output}")
    cells_dir = output / "cells"
    cells_dir.mkdir(parents=True)

    mode = normal_mode_data(1.02)
    normal_form = fast_normal_form_data(1.02)
    cells: list[dict[str, Any]] = []
    for excess in ENERGY_EXCESSES:
        spec = OrbitSearchSpec(energy_excess=excess)
        cell, arrays = shoot_brake_orbit(spec)
        determinant = cell["transverse_stability_determinant"]
        gates = {
            "optimizer_success": bool(cell["optimizer_success"]),
            "shooting_residual": cell["max_abs_shooting_residual"] < 1.0e-9,
            "closure": cell["max_scaled_closure"] < 1.0e-9,
            "energy_drift": cell["max_energy_drift_over_excess"] < 1.0e-9,
            "symplectic_defect": cell["symplectic_defect_inf"] < 1.0e-8,
            "determinant_imaginary": abs(determinant["imag"]) < 1.0e-9,
            "transverse_nondegeneracy": determinant["real"] > 3.0,
            "period_window": PERIOD_WINDOW[0] <= cell["period"] <= PERIOD_WINDOW[1],
        }
        cell["energy_excess"] = excess
        cell["gates"] = gates
        cell["all_cell_gates_pass"] = all(gates.values())
        name = _cell_name(excess)
        npz_path = cells_dir / f"{name}.npz"
        np.savez_compressed(npz_path, **arrays)
        cell["npz_sha256"] = _sha256(npz_path)
        json_path = cells_dir / f"{name}.json"
        _write_json(json_path, cell)
        cells.append(cell)

    small = cells[:3]
    deltas = np.array([cell["energy_excess"] for cell in small])
    period_intercept, period_coefficients = _fit_intercept(
        deltas, np.array([cell["period"] for cell in small])
    )
    action_intercept, action_coefficients = _fit_intercept(
        deltas,
        np.array([cell["action"] / cell["energy_excess"] for cell in small]),
    )
    stability_intercept, stability_coefficients = _fit_intercept(
        deltas,
        np.array(
            [
                cell["transverse_stability_determinant"]["real"]
                for cell in small
            ]
        ),
    )

    def fit_record(
        intercept: float,
        coefficients: list[float],
        oracle: float,
        tolerance: float,
        *,
        slope_oracle: float | None = None,
        slope_tolerance: float | None = None,
    ) -> dict[str, Any]:
        error = abs(intercept - oracle)
        slope = coefficients[-2]
        slope_error = (
            None if slope_oracle is None else abs(slope - slope_oracle)
        )
        slope_pass = (
            True
            if slope_error is None or slope_tolerance is None
            else slope_error < slope_tolerance
        )
        return {
            "intercept": intercept,
            "coefficients_descending": coefficients,
            "oracle": oracle,
            "absolute_error": error,
            "tolerance": tolerance,
            "slope": slope,
            "slope_oracle": slope_oracle,
            "slope_absolute_error": slope_error,
            "slope_tolerance": slope_tolerance,
            "pass": error < tolerance and slope_pass,
        }

    fits = {
        "period": fit_record(
            period_intercept,
            period_coefficients,
            mode.periods[1],
            5.0e-6,
            slope_oracle=normal_form.period_energy_slope,
            slope_tolerance=5.0e-5,
        ),
        "action_ratio": fit_record(
            action_intercept,
            action_coefficients,
            mode.periods[1],
            5.0e-6,
            slope_oracle=normal_form.action_ratio_energy_slope,
            slope_tolerance=2.5e-5,
        ),
        "stability": fit_record(
            stability_intercept,
            stability_coefficients,
            mode.fast_stability_determinant,
            2.0e-5,
        ),
    }
    worst = {
        key: max(float(cell[key]) for cell in cells)
        for key in (
            "max_abs_shooting_residual",
            "max_scaled_closure",
            "max_energy_drift_over_excess",
            "symplectic_defect_inf",
        )
    }
    summary: dict[str, Any] = {
        "protocol": "R400_LOCAL_PERIOD_PROTOCOL.md",
        "status": "complete",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "normal_mode": mode.__dict__,
        "fast_normal_form": normal_form.__dict__,
        "energy_excesses": list(ENERGY_EXCESSES),
        "period_window": list(PERIOD_WINDOW),
        "cells": cells,
        "asymptotic_fits": fits,
        "worst_numerics": worst,
        "all_cell_gates_pass": all(cell["all_cell_gates_pass"] for cell in cells),
        "all_asymptotic_gates_pass": all(record["pass"] for record in fits.values()),
        "software": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "claim_boundary": {
            "classical_local_orbit_certificate": True,
            "semiclassical_trace_theorem": False,
            "high_energy_period_export": False,
            "prime_power_gate": False,
            "zeta_zero_test": False,
            "rh_claim": False,
        },
    }
    summary["all_gates_pass"] = bool(
        summary["all_cell_gates_pass"] and summary["all_asymptotic_gates_pass"]
    )
    _write_json(output / "summary.json", summary)
    (output / "R400_RESULT_REPORT.md").write_text(_report(summary))

    provenance_files = [
        root / "src/hp_candidate_search/local_periodic_orbits.py",
        root / "src/hp_candidate_search/warped_henon.py",
        root / "scripts/run_r400_local_period_smoke.py",
        root / "scripts/check_r400_local_period_independent.py",
        root / "research/route_a_wave_trace/R400_LOCAL_PERIOD_PROTOCOL.md",
    ]
    manifest = {
        "source_sha256": {
            str(path.relative_to(root)): _sha256(path) for path in provenance_files
        },
        "result_sha256": {
            str(path.relative_to(output)): _sha256(path)
            for path in sorted(output.rglob("*"))
            if path.is_file()
        },
    }
    _write_json(output / "manifest.json", manifest)
    print(json.dumps({"output": str(output), "all_gates_pass": summary["all_gates_pass"]}))
    return 0 if summary["all_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
