#!/usr/bin/env python3
"""Audit the interpretation of the frozen R061 localization arrays.

This script is read-only with respect to the R061 producer outputs.  It checks
whether the preregistered tau=1 cell-exposure variable is distinct from a
target-occupancy indicator and recomputes lower-threshold associations after
conditioning on rows with nonzero target occupancy.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from scipy.stats import spearmanr


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "results" / "boundary_localization_r061.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "localization_interpretation_audit_r061.json"
LOW_TAUS = ("0.125", "0.25")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_project_path(path: str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else PROJECT_ROOT / candidate


def spearman_safe(x: np.ndarray, y: np.ndarray) -> float | None:
    mask = np.isfinite(x) & np.isfinite(y)
    if np.count_nonzero(mask) < 3:
        return None
    x_use = x[mask]
    y_use = y[mask]
    if np.ptp(x_use) == 0.0 or np.ptp(y_use) == 0.0:
        return None
    value = spearmanr(x_use, y_use).statistic
    return None if not np.isfinite(value) else float(value)


def top_quartile_concentration(energy: np.ndarray, exposure: np.ndarray) -> float | None:
    total = float(np.sum(energy))
    if total <= 0.0 or exposure.size == 0:
        return None
    count = max(1, int(math.ceil(exposure.size * 0.25)))
    order = np.argsort(-exposure, kind="mergesort")
    return float(np.sum(energy[order[:count]]) / total)


def stats(values: list[float]) -> dict[str, float | int | None]:
    finite = np.asarray([value for value in values if np.isfinite(value)], dtype=float)
    if finite.size == 0:
        return {"count": 0, "mean": None, "median": None, "min": None, "max": None}
    return {
        "count": int(finite.size),
        "mean": float(np.mean(finite)),
        "median": float(np.median(finite)),
        "min": float(np.min(finite)),
        "max": float(np.max(finite)),
    }


def main() -> None:
    args = parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    records = source.get("records", [])
    if not records:
        raise ValueError("no localization records found")

    hash_failures: list[str] = []
    tau_one_failures: list[str] = []
    tau_half_failures: list[str] = []
    occupied_energy: list[float] = []
    grouped: dict[tuple[str, int, int], dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for record in records:
        array_path = resolve_project_path(str(record["array_path"]))
        if sha256_file(array_path) != str(record["array_sha256"]):
            hash_failures.append(str(record["config_id"]))
        with np.load(array_path, allow_pickle=False) as arrays:
            energy = np.asarray(arrays["row_energy"], dtype=float)
            inside_fraction = np.asarray(arrays["inside_fraction"], dtype=float)
            occupied = inside_fraction > 0.0
            occupancy_indicator = occupied.astype(float)
            tau_one = np.asarray(arrays["cell_exposure_tau_1.0"], dtype=float)
            tau_half = np.asarray(arrays["cell_exposure_tau_0.5"], dtype=float)
            if not np.array_equal(tau_one, occupancy_indicator):
                tau_one_failures.append(str(record["config_id"]))
            if not np.array_equal(tau_half, occupancy_indicator):
                tau_half_failures.append(str(record["config_id"]))
            total_energy = float(np.sum(energy))
            if total_energy > 0.0:
                fraction = float(np.sum(energy[occupied]) / total_energy)
                occupied_energy.append(float(np.clip(fraction, 0.0, 1.0)))

            if str(record["method_family"]) != "sobol":
                continue
            key = (
                str(record["chain"]),
                int(record["samples_per_cell"]),
                int(record["target_grid"]),
            )
            energy_occupied = energy[occupied]
            for tau in LOW_TAUS:
                exposure = np.asarray(arrays[f"cell_exposure_tau_{tau}"], dtype=float)[occupied]
                rho = spearman_safe(exposure, energy_occupied)
                concentration = top_quartile_concentration(energy_occupied, exposure)
                if rho is not None:
                    grouped[key][f"rho_tau_{tau}"].append(rho)
                if concentration is not None:
                    grouped[key][f"top25_tau_{tau}"].append(concentration)

    group_summaries: list[dict[str, Any]] = []
    for (chain, samples, target), values in sorted(grouped.items()):
        group_summaries.append(
            {
                "chain": chain,
                "samples_per_cell": samples,
                "target_grid": target,
                "conditional_on_inside_positive": True,
                **{key: stats(value) for key, value in sorted(values.items())},
            }
        )

    output = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "scope": (
            "Read-only post-freeze interpretation audit of persisted R061 localization arrays; "
            "no producer, protocol, matrix, or localization array is modified."
        ),
        "input_path": str(args.input.resolve().relative_to(PROJECT_ROOT)),
        "input_sha256": sha256_file(args.input),
        "record_count": len(records),
        "sobol_record_count": sum(str(record["method_family"]) == "sobol" for record in records),
        "array_hashes_all_match": not hash_failures,
        "array_hash_failures": hash_failures,
        "tau_1_equals_inside_positive_indicator_all": not tau_one_failures,
        "tau_1_failures": tau_one_failures,
        "tau_0_5_equals_inside_positive_indicator_all": not tau_half_failures,
        "tau_0_5_failures": tau_half_failures,
        "occupied_row_energy_fraction": stats(occupied_energy),
        "group_summaries": group_summaries,
        "interpretation": {
            "formal_gate": (
                "The frozen tau=1 G2 bookkeeping result remains reproducible, but its cell-exposure "
                "variable is exactly a target-occupancy/support indicator."
            ),
            "mechanism": (
                "The frozen G2 result does not identify internal target-cell boundary phase. "
                "Conditional lower-threshold associations are reported as exploratory sensitivity only."
            ),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "record_count": len(records),
        "array_hashes_all_match": not hash_failures,
        "tau_1_degenerate_all": not tau_one_failures,
        "tau_0_5_degenerate_all": not tau_half_failures,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
