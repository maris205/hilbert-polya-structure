#!/usr/bin/env python3
"""Run the preregistered R401-SC eigenvalue-only trace audit."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
import time
from dataclasses import asdict
from math import pi
from pathlib import Path
from typing import Any

import numpy as np
import scipy

from hp_candidate_search.local_periodic_orbits import normal_mode_data
from hp_candidate_search.radial_laguerre import (
    RadialLaguerreSpec,
    solve_radial_laguerre,
)
from hp_candidate_search.semiclassical_trace import (
    filtered_spectral_density,
    ordered_spectrum_difference,
    predicted_fast_orbit_term,
    r401_window_delta_0p01,
    wrapped_phase,
)
from hp_candidate_search.transformed_galerkin import (
    TransformedGalerkinSpec,
    solve_transformed_galerkin,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "r401_fixed_energy_trace_smoke"
CLASSICAL_CELL = (
    ROOT / "results" / "r400_local_period_smoke" / "cells" / "delta_0p01.json"
)
EXPECTED_CLASSICAL_HASH = (
    "90184ec48d55986deb2b67ff6ac1fca3ae9f30b40e812181865f892a5920438b"
)
HBAR_LADDER = (4.0e-4, 3.0e-4, 2.0e-4, 1.5e-4, 1.0e-4, 7.5e-5, 5.0e-5, 4.0e-5)
TARGET_EXCESS = 0.01
EIGENVALUE_EXCESS_CEILING = 0.019
ACTIVE_UPPER_EXCESS = 0.018
TIME_MAX = 0.745


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _complex(value: complex) -> dict[str, float]:
    return {"real": float(value.real), "imag": float(value.imag)}


def _controls(hbar: float) -> dict[str, float | int]:
    if hbar >= 1.0e-4:
        return {
            "production_cutoff": 0.030,
            "fine_cutoff": 0.035,
            "production_quadrature": 96,
            "fine_quadrature": 112,
        }
    if hbar == 7.5e-5:
        return {
            "production_cutoff": 0.023,
            "fine_cutoff": 0.025,
            "production_quadrature": 104,
            "fine_quadrature": 120,
        }
    if hbar == 5.0e-5:
        return {
            "production_cutoff": 0.020,
            "fine_cutoff": 0.022,
            "production_quadrature": 120,
            "fine_quadrature": 136,
        }
    if hbar == 4.0e-5:
        return {
            "production_cutoff": 0.020,
            "fine_cutoff": 0.021,
            "production_quadrature": 136,
            "fine_quadrature": 152,
        }
    raise ValueError(f"unregistered hbar {hbar}")


def _harmonic_spectrum(
    frequencies: tuple[float, float], hbar: float
) -> np.ndarray:
    values: list[float] = []
    first = 0
    while (
        hbar * frequencies[0] * (first + 0.5)
        + 0.5 * hbar * frequencies[1]
        <= EIGENVALUE_EXCESS_CEILING
    ):
        second = 0
        while True:
            excess = hbar * (
                frequencies[0] * (first + 0.5)
                + frequencies[1] * (second + 0.5)
            )
            if excess > EIGENVALUE_EXCESS_CEILING:
                break
            values.append(2.0 * pi + excess)
            second += 1
        first += 1
    return np.sort(np.asarray(values, dtype=float))


def _solve_cell(
    hbar: float,
    classical: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    controls = _controls(hbar)
    retained_ceiling = 0.025 if hbar == HBAR_LADDER[0] else EIGENVALUE_EXCESS_CEILING
    controls["retained_excess_ceiling"] = retained_ceiling
    target_energy = 2.0 * pi + TARGET_EXCESS
    production_spec = TransformedGalerkinSpec(
        hbar=hbar,
        a=1.02,
        basis_excess_cutoff=float(controls["production_cutoff"]),
        eigenvalue_excess_ceiling=retained_ceiling,
        quadrature_order=int(controls["production_quadrature"]),
    )
    fine_spec = TransformedGalerkinSpec(
        hbar=hbar,
        a=1.02,
        basis_excess_cutoff=float(controls["fine_cutoff"]),
        eigenvalue_excess_ceiling=retained_ceiling,
        quadrature_order=int(controls["fine_quadrature"]),
    )

    started = time.perf_counter()
    warped_production, warped_production_meta = solve_transformed_galerkin(
        production_spec
    )
    warped_production_seconds = time.perf_counter() - started
    started = time.perf_counter()
    warped_fine, warped_fine_meta = solve_transformed_galerkin(fine_spec)
    warped_fine_seconds = time.perf_counter() - started

    radial_spec = RadialLaguerreSpec(
        hbar=hbar,
        basis_excess_cutoff=float(controls["fine_cutoff"]),
        eigenvalue_excess_ceiling=retained_ceiling,
        quadrature_order=int(controls["fine_quadrature"]),
    )
    started = time.perf_counter()
    radial_laguerre, radial_laguerre_meta = solve_radial_laguerre(radial_spec)
    radial_laguerre_seconds = time.perf_counter() - started
    radial_cartesian_spec = TransformedGalerkinSpec(
        hbar=hbar,
        a=0.0,
        basis_excess_cutoff=float(controls["fine_cutoff"]),
        eigenvalue_excess_ceiling=retained_ceiling,
        quadrature_order=int(controls["fine_quadrature"]),
    )
    started = time.perf_counter()
    radial_cartesian, radial_cartesian_meta = solve_transformed_galerkin(
        radial_cartesian_spec
    )
    radial_cartesian_seconds = time.perf_counter() - started

    window_512 = r401_window_delta_0p01(512)
    window_1024 = r401_window_delta_0p01(1024)
    warped_trace_production = filtered_spectral_density(
        warped_production,
        target_energy=target_energy,
        hbar=hbar,
        window=window_1024,
    )
    warped_trace_fine_512 = filtered_spectral_density(
        warped_fine,
        target_energy=target_energy,
        hbar=hbar,
        window=window_512,
    )
    warped_trace_fine = filtered_spectral_density(
        warped_fine,
        target_energy=target_energy,
        hbar=hbar,
        window=window_1024,
    )
    radial_trace_512 = filtered_spectral_density(
        radial_laguerre,
        target_energy=target_energy,
        hbar=hbar,
        window=window_512,
    )
    radial_trace = filtered_spectral_density(
        radial_laguerre,
        target_energy=target_energy,
        hbar=hbar,
        window=window_1024,
    )
    relative_production = warped_trace_production - radial_trace
    relative_fine_512 = warped_trace_fine_512 - radial_trace_512
    relative_fine = warped_trace_fine - radial_trace

    mode = normal_mode_data(1.02)
    harmonic_warped = _harmonic_spectrum(mode.angular_frequencies, hbar)
    harmonic_radial = _harmonic_spectrum((2.0 * pi, 2.0 * pi), hbar)
    harmonic_relative = filtered_spectral_density(
        harmonic_warped,
        target_energy=target_energy,
        hbar=hbar,
        window=window_1024,
    ) - filtered_spectral_density(
        harmonic_radial,
        target_energy=target_energy,
        hbar=hbar,
        window=window_1024,
    )

    determinant = float(classical["transverse_stability_determinant"]["real"])
    prediction = predicted_fast_orbit_term(
        hbar=hbar,
        action=float(classical["action"]),
        period=float(classical["period"]),
        stability_determinant=determinant,
    )
    harmonic_prediction = predicted_fast_orbit_term(
        hbar=hbar,
        action=mode.periods[1] * TARGET_EXCESS,
        period=mode.periods[1],
        stability_determinant=mode.fast_stability_determinant,
    )
    normalized = relative_fine / prediction
    normalized_harmonic = harmonic_relative / harmonic_prediction

    warped_comparison = ordered_spectrum_difference(
        warped_fine,
        warped_production,
        upper_energy=2.0 * pi + ACTIVE_UPPER_EXCESS,
    )
    radial_comparison = ordered_spectrum_difference(
        radial_cartesian,
        radial_laguerre,
        upper_energy=2.0 * pi + ACTIVE_UPPER_EXCESS,
    )
    nested_phase_budget = (
        TIME_MAX
        * float(warped_comparison["max_absolute_difference"])
        / hbar
    )
    radial_phase_budget = (
        TIME_MAX
        * float(radial_comparison["max_absolute_difference"])
        / hbar
    )
    trace_refinement_difference = abs(relative_fine - relative_production)
    fourier_difference = abs(relative_fine - relative_fine_512)
    trace_refinement_tolerance = max(0.05 * hbar, 1.0e-9)
    highest_guard = min(
        warped_production[-1],
        warped_fine[-1],
        radial_laguerre[-1],
        radial_cartesian[-1],
    )
    all_internal_residuals = (
        warped_production_meta["max_absolute_ritz_residual"],
        warped_fine_meta["max_absolute_ritz_residual"],
        radial_laguerre_meta["max_absolute_ritz_residual"],
        radial_cartesian_meta["max_absolute_ritz_residual"],
    )
    all_orthogonality = (
        warped_production_meta["quadrature_orthogonality_defect"],
        warped_fine_meta["quadrature_orthogonality_defect"],
        radial_laguerre_meta["maximum_quadrature_orthogonality_defect"],
        radial_cartesian_meta["quadrature_orthogonality_defect"],
    )
    gates = {
        "nested_phase_budget": bool(nested_phase_budget < 5.0e-3),
        "trace_refinement": bool(
            trace_refinement_difference <= trace_refinement_tolerance
        ),
        "radial_oracle_phase_budget": bool(radial_phase_budget < 1.0e-6),
        "internal_ritz_residual": bool(
            max(all_internal_residuals) < 1.0e-10
        ),
        "quadrature_orthogonality": bool(
            max(all_orthogonality) < 1.0e-10
        ),
        "guard_above_cutoff_support": bool(
            highest_guard > 2.0 * pi + ACTIVE_UPPER_EXCESS
        ),
        "inverse_fourier_order": bool(fourier_difference < 1.0e-10),
    }
    result: dict[str, Any] = {
        "hbar": hbar,
        "controls": controls,
        "warped_production_metadata": warped_production_meta,
        "warped_fine_metadata": warped_fine_meta,
        "radial_laguerre_metadata": radial_laguerre_meta,
        "radial_cartesian_metadata": radial_cartesian_meta,
        "wall_seconds": {
            "warped_production": warped_production_seconds,
            "warped_fine": warped_fine_seconds,
            "radial_laguerre": radial_laguerre_seconds,
            "radial_cartesian": radial_cartesian_seconds,
        },
        "ordered_spectrum_comparison": warped_comparison,
        "radial_oracle_comparison": radial_comparison,
        "nested_phase_budget_radians": nested_phase_budget,
        "radial_oracle_phase_budget_radians": radial_phase_budget,
        "trace_refinement_difference": trace_refinement_difference,
        "trace_refinement_tolerance": trace_refinement_tolerance,
        "inverse_fourier_order_difference": fourier_difference,
        "warped_trace_production": _complex(warped_trace_production),
        "warped_trace_fine": _complex(warped_trace_fine),
        "radial_trace": _complex(radial_trace),
        "relative_trace_production": _complex(relative_production),
        "relative_trace_fine": _complex(relative_fine),
        "prediction": _complex(prediction),
        "normalized_trace": _complex(normalized),
        "normalized_error": float(abs(normalized - 1.0)),
        "normalized_phase_error": wrapped_phase(normalized),
        "harmonic_relative_trace": _complex(harmonic_relative),
        "harmonic_prediction": _complex(harmonic_prediction),
        "normalized_harmonic_trace": _complex(normalized_harmonic),
        "normalized_harmonic_error": float(abs(normalized_harmonic - 1.0)),
        "nonlinear_harmonic_normalized_difference": float(
            abs(normalized - normalized_harmonic)
        ),
        "highest_common_guard_eigenvalue": float(highest_guard),
        "gates": gates,
        "all_integrity_gates_pass": bool(all(gates.values())),
    }
    arrays = {
        "warped_production": warped_production,
        "warped_fine": warped_fine,
        "radial_laguerre": radial_laguerre,
        "radial_cartesian": radial_cartesian,
        "harmonic_warped": harmonic_warped,
        "harmonic_radial": harmonic_radial,
    }
    return result, arrays


def _report(summary: dict[str, Any]) -> str:
    rows = []
    for cell in summary["cells"]:
        z = cell["normalized_trace"]
        zh = cell["normalized_harmonic_trace"]
        rows.append(
            "| {h:.2e} | {zr:.6f}{zi:+.6f}i | {e:.4f} | {p:+.4f} | "
            "{hr:.6f}{hi:+.6f}i | {nh:.4f} | {gate} |".format(
                h=cell["hbar"],
                zr=z["real"],
                zi=z["imag"],
                e=cell["normalized_error"],
                p=cell["normalized_phase_error"],
                hr=zh["real"],
                hi=zh["imag"],
                nh=cell["nonlinear_harmonic_normalized_difference"],
                gate="PASS" if cell["all_integrity_gates_pass"] else "FAIL",
            )
        )
    return r"""# R401-SC Result Report

## Outcome

Overall status: **{status}**.

This is an A4.9-guided fixed-energy numerical audit at delta=0.01.  The
analytic threshold delta_tr remains nonquantitative, so the result is not a
proof that this cell lies in the theorem's sufficiently-small interval.

| hbar | nonlinear Z | |Z-1| | arg Z | harmonic Z | |Z-Z_har| | integrity |
|---:|---:|---:|---:|---:|---:|:---:|
{rows}

The preregistered prediction used the absolute coefficient

\[
T/(2\pi\sqrt D)={amplitude:.17g}
\]

and phase +i, with no fitted constants.  The exact harmonic column uses the
same finite energy and time windows and exposes the pre-asymptotic window
oscillations in the coarser cells.

## Scientific gates

```json
{scientific}
```

Arithmetic P remains open and gate Z remains unauthorized.
""".format(
        status=summary["overall_status"],
        rows="\n".join(rows),
        amplitude=summary["classical_oracle"]["amplitude"],
        scientific=json.dumps(summary["scientific_gates"], indent=2),
    )


def main() -> int:
    if OUTPUT.exists():
        raise FileExistsError(f"refusing to overwrite immutable output {OUTPUT}")
    if _sha256(CLASSICAL_CELL) != EXPECTED_CLASSICAL_HASH:
        raise RuntimeError("the immutable R400 classical cell hash changed")
    classical = json.loads(CLASSICAL_CELL.read_text())
    OUTPUT.mkdir(parents=True)
    (OUTPUT / "cells").mkdir()

    cells: list[dict[str, Any]] = []
    for hbar in HBAR_LADDER:
        result, arrays = _solve_cell(hbar, classical)
        label = f"hbar_{hbar:.8f}".replace(".", "p")
        npz_path = OUTPUT / "cells" / f"{label}.npz"
        np.savez_compressed(npz_path, **arrays)
        result["npz_sha256"] = _sha256(npz_path)
        json_path = OUTPUT / "cells" / f"{label}.json"
        json_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        cells.append(result)

    finest = cells[-1]
    fine_tail_errors = [cells[-3]["normalized_error"], cells[-2]["normalized_error"]]
    scientific_gates = {
        "all_integrity_gates": all(
            cell["all_integrity_gates_pass"] for cell in cells
        ),
        "finest_complex_error_le_0p025": finest["normalized_error"] <= 0.025,
        "finest_phase_error_le_0p025": abs(finest["normalized_phase_error"])
        <= 0.025,
        "finest_matches_harmonic_baseline": finest[
            "nonlinear_harmonic_normalized_difference"
        ]
        <= 0.02,
        "finest_improves_on_two_preceding": finest["normalized_error"]
        < min(fine_tail_errors),
    }
    overall_status = "PASS" if all(scientific_gates.values()) else "FAIL"
    determinant = float(classical["transverse_stability_determinant"]["real"])
    summary: dict[str, Any] = {
        "experiment": "R401-SC",
        "overall_status": overall_status,
        "claim_scope": "A4.9-guided fixed-energy numerical audit only",
        "target_energy_excess": TARGET_EXCESS,
        "hbar_ladder": list(HBAR_LADDER),
        "classical_cell": str(CLASSICAL_CELL.relative_to(ROOT)),
        "classical_cell_sha256": EXPECTED_CLASSICAL_HASH,
        "classical_oracle": {
            "period": float(classical["period"]),
            "action": float(classical["action"]),
            "stability_determinant": determinant,
            "amplitude": float(
                classical["period"] / (2.0 * pi * np.sqrt(determinant))
            ),
            "positive_time_phase": "+i",
        },
        "window_order_1024": asdict(r401_window_delta_0p01(1024)),
        "scientific_gates": scientific_gates,
        "cells": cells,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "cpu_count": os.cpu_count(),
        },
    }
    summary_path = OUTPUT / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    report_path = OUTPUT / "R401_RESULT_REPORT.md"
    report_path.write_text(_report(summary))

    source_paths = (
        ROOT / "research" / "route_a_wave_trace" / "R401_FIXED_ENERGY_TRACE_PROTOCOL.md",
        ROOT / "src" / "hp_candidate_search" / "transformed_galerkin.py",
        ROOT / "src" / "hp_candidate_search" / "radial_laguerre.py",
        ROOT / "src" / "hp_candidate_search" / "semiclassical_trace.py",
        ROOT / "scripts" / "run_r401_fixed_energy_trace_smoke.py",
        ROOT / "scripts" / "check_r401_fixed_energy_trace_independent.py",
    )
    result_paths = sorted(
        path
        for path in OUTPUT.rglob("*")
        if path.is_file() and path.name != "manifest.json"
    )
    manifest = {
        "source_sha256": {
            str(path.relative_to(ROOT)): _sha256(path) for path in source_paths
        },
        "result_sha256": {
            str(path.relative_to(OUTPUT)): _sha256(path) for path in result_paths
        },
    }
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({"output": str(OUTPUT), "status": overall_status}, indent=2))
    return 0 if overall_status == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
