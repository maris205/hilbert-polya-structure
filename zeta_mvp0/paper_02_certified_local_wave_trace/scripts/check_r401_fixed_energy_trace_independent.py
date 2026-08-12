#!/usr/bin/env python3
"""Independent, no-production-import checker for the R401-SC archive."""

from __future__ import annotations

import hashlib
import json
from math import pi
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "r401_fixed_energy_trace_smoke"
TARGET = 2.0 * pi + 0.01
TIME_SUPPORT = (0.05, 0.15, 0.68, 0.745)
ENERGY_SUPPORT = (2.0 * pi + 0.002, 2.0 * pi + 0.004, 2.0 * pi + 0.016, 2.0 * pi + 0.018)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def complex_value(record: dict[str, float]) -> complex:
    return complex(record["real"], record["imag"])


def eta(values: np.ndarray) -> np.ndarray:
    x = np.asarray(values, dtype=float)
    result = np.zeros_like(x)
    result[x >= 1.0] = 1.0
    active = (x > 0.0) & (x < 1.0)
    left = np.exp(-1.0 / x[active])
    right = np.exp(-1.0 / (1.0 - x[active]))
    result[active] = left / (left + right)
    return result


def chi(values: np.ndarray) -> np.ndarray:
    lower_support, lower_plateau, upper_plateau, upper_support = ENERGY_SUPPORT
    return eta(
        (values - lower_support) / (lower_plateau - lower_support)
    ) * eta(
        (upper_support - values) / (upper_support - upper_plateau)
    )


def g_values(scaled: np.ndarray, order: int = 1536) -> np.ndarray:
    lower_support, lower_plateau, upper_plateau, upper_support = TIME_SUPPORT
    nodes, weights = np.polynomial.legendre.leggauss(order)
    midpoint = 0.5 * (lower_support + upper_support)
    half_width = 0.5 * (upper_support - lower_support)
    times = midpoint + half_width * nodes
    hat = eta(
        (times - lower_support) / (lower_plateau - lower_support)
    ) * eta(
        (upper_support - times) / (upper_support - upper_plateau)
    )
    return (
        half_width
        * (weights * hat)
        @ np.exp(1.0j * np.outer(times, np.asarray(scaled, dtype=float)))
        / (2.0 * pi)
    )


def trace(values: np.ndarray, hbar: float) -> complex:
    cutoff = chi(values)
    active = cutoff > 0.0
    return complex(
        np.sum(
            cutoff[active] ** 2
            * g_values((TARGET - values[active]) / hbar)
        )
    )


def harmonic_spectrum(
    frequencies: tuple[float, float], hbar: float, ceiling: float = 0.019
) -> np.ndarray:
    values: list[float] = []
    first = 0
    while hbar * frequencies[0] * (first + 0.5) + hbar * frequencies[1] * 0.5 <= ceiling:
        second = 0
        while True:
            excess = hbar * (
                frequencies[0] * (first + 0.5)
                + frequencies[1] * (second + 0.5)
            )
            if excess > ceiling:
                break
            values.append(2.0 * pi + excess)
            second += 1
        first += 1
    return np.sort(np.asarray(values))


def prediction(
    hbar: float, action: float, period: float, determinant: float
) -> complex:
    return complex(
        1.0j
        * period
        / (2.0 * pi * np.sqrt(determinant))
        * np.exp(1.0j * action / hbar)
    )


def main() -> int:
    summary = json.loads((OUTPUT / "summary.json").read_text())
    manifest = json.loads((OUTPUT / "manifest.json").read_text())
    checks: dict[str, bool] = {}
    for relative, expected in manifest["source_sha256"].items():
        checks[f"source_hash:{relative}"] = sha256(ROOT / relative) == expected
    for relative, expected in manifest["result_sha256"].items():
        checks[f"result_hash:{relative}"] = sha256(OUTPUT / relative) == expected

    classical = summary["classical_oracle"]
    mode = summary["cells"][0]["warped_fine_metadata"]
    frequencies = tuple(float(value) for value in mode["frequencies"])
    singular_values = tuple(float(value) for value in mode["singular_values"])
    harmonic_period = 1.0 / singular_values[1]
    harmonic_determinant = 4.0 * np.sin(
        pi / (singular_values[1] / singular_values[0])
    ) ** 2
    recomputed_cells: list[dict[str, Any]] = []

    for stored in summary["cells"]:
        hbar = float(stored["hbar"])
        label = f"hbar_{hbar:.8f}".replace(".", "p")
        arrays = np.load(OUTPUT / "cells" / f"{label}.npz")
        relative = trace(arrays["warped_fine"], hbar) - trace(
            arrays["radial_laguerre"], hbar
        )
        predicted = prediction(
            hbar,
            float(classical["action"]),
            float(classical["period"]),
            float(classical["stability_determinant"]),
        )
        normalized = relative / predicted
        harmonic_warped = harmonic_spectrum(frequencies, hbar)
        harmonic_radial = harmonic_spectrum((2.0 * pi, 2.0 * pi), hbar)
        harmonic_relative = trace(harmonic_warped, hbar) - trace(
            harmonic_radial, hbar
        )
        harmonic_predicted = prediction(
            hbar,
            harmonic_period * 0.01,
            harmonic_period,
            harmonic_determinant,
        )
        normalized_harmonic = harmonic_relative / harmonic_predicted
        checks[f"relative_trace:{label}"] = abs(
            relative - complex_value(stored["relative_trace_fine"])
        ) < 2.0e-10
        checks[f"prediction:{label}"] = abs(
            predicted - complex_value(stored["prediction"])
        ) < 2.0e-13
        checks[f"normalized:{label}"] = abs(
            normalized - complex_value(stored["normalized_trace"])
        ) < 5.0e-9
        checks[f"harmonic:{label}"] = abs(
            normalized_harmonic
            - complex_value(stored["normalized_harmonic_trace"])
        ) < 5.0e-9
        recomputed_cells.append(
            {
                "hbar": hbar,
                "relative_trace": {
                    "real": float(relative.real),
                    "imag": float(relative.imag),
                },
                "normalized_trace": {
                    "real": float(normalized.real),
                    "imag": float(normalized.imag),
                },
                "normalized_error": float(abs(normalized - 1.0)),
                "normalized_phase": float(np.angle(normalized)),
                "normalized_harmonic": {
                    "real": float(normalized_harmonic.real),
                    "imag": float(normalized_harmonic.imag),
                },
            }
        )

    finest = recomputed_cells[-1]
    scientific = {
        "all_stored_integrity_gates": all(
            cell["all_integrity_gates_pass"] for cell in summary["cells"]
        ),
        "finest_complex_error_le_0p025": finest["normalized_error"] <= 0.025,
        "finest_phase_error_le_0p025": abs(finest["normalized_phase"]) <= 0.025,
        "finest_matches_harmonic_baseline": abs(
            complex_value(finest["normalized_trace"])
            - complex_value(finest["normalized_harmonic"])
        )
        <= 0.02,
        "finest_improves_on_two_preceding": finest["normalized_error"]
        < min(
            recomputed_cells[-2]["normalized_error"],
            recomputed_cells[-3]["normalized_error"],
        ),
    }
    checks["summary_status_pass"] = summary["overall_status"] == "PASS"
    checks["scientific_gates"] = all(scientific.values())
    passed = all(checks.values())
    result = {
        "checker": "independent no-production-import R401 checker",
        "status": "PASS" if passed else "FAIL",
        "checks": checks,
        "scientific_gates": scientific,
        "cells": recomputed_cells,
    }
    (OUTPUT / "independent_checker.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({"status": result["status"], "checks": len(checks)}, indent=2))
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
