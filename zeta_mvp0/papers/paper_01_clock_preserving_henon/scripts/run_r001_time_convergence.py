#!/usr/bin/env python3
"""Run R001 time-length convergence from single long trajectories."""

from __future__ import annotations

import csv
import json
import os
import platform
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from hp_candidate_search.warped_henon import FTLEConfig, run_ftle_trajectory


def _run(config: FTLEConfig) -> dict:
    return run_ftle_trajectory(config)


def main() -> int:
    output_dir = Path("results/r001_time_convergence")
    output_dir.mkdir(parents=True, exist_ok=True)
    specs = (
        (0.0, 1, 4096),
        (1.02, 1, 8192),
        (1.02, 2, 16384),
        (6.0, 1, 16384),
    )
    configs = [
        FTLEConfig(
            energy=1000.0,
            a=a,
            n=n,
            seed_index=seed,
            total_natural_time=160.0,
            steps_per_natural_time=steps,
        )
        for a, n, steps in specs
        for seed in range(4)
    ]

    records = []
    with ProcessPoolExecutor(max_workers=min(16, os.cpu_count() or 1)) as pool:
        futures = {pool.submit(_run, config): config for config in configs}
        for future in as_completed(futures):
            config = futures[future]
            try:
                records.append(future.result())
            except Exception as exc:
                records.append(
                    {
                        **asdict(config),
                        "status": "exception",
                        "exception": f"{type(exc).__name__}: {exc}",
                        "max_relative_energy_drift": float("inf"),
                    }
                )
    records.sort(key=lambda row: (row["a"], row["n"], row["seed_index"]))
    fields = sorted({key for row in records for key in row})
    with (output_dir / "records.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    groups = {}
    for a, n, _ in specs:
        group = [row for row in records if row["a"] == a and row["n"] == n]
        medians = {}
        for target in (20, 40, 80, 160):
            medians[f"median_ftle_natural_t{target}"] = float(
                np.median([row[f"ftle_natural_t{target}"] for row in group])
            )
            medians[f"median_sali_t{target}"] = float(
                np.median([row[f"sali_t{target}"] for row in group])
            )
        chaotic_at_160 = sum(
            row["ftle_natural_t160"] > 0.05 and row["sali_t160"] < 1.0e-8
            for row in group
        )
        plateau_ratio = (
            medians["median_ftle_natural_t160"]
            / medians["median_ftle_natural_t80"]
        )
        groups[f"a={a}:n={n}"] = {
            "records": len(group),
            "valid_records": sum(
                row["status"] == "ok" and row["max_relative_energy_drift"] <= 1.0e-4
                for row in group
            ),
            **medians,
            "joint_chaotic_flags_t160": int(chaotic_at_160),
            "plateau_ratio_t160_over_t80": float(plateau_ratio),
            "max_energy_drift": max(row["max_relative_energy_drift"] for row in group),
        }

    nonlinear = [groups[key] for key in ("a=1.02:n=1", "a=1.02:n=2", "a=6.0:n=1")]
    radial = groups["a=0.0:n=1"]
    gates = {
        "all_records_valid": all(group["valid_records"] == 4 for group in groups.values()),
        "radial_sali_remains_large": radial["median_sali_t160"] > 1.0e-3,
        "radial_ftle_below_all_nonlinear": all(
            abs(radial["median_ftle_natural_t160"])
            < group["median_ftle_natural_t160"]
            for group in nonlinear
        ),
        "nonlinear_joint_flags_at_least_three_of_four": all(
            group["joint_chaotic_flags_t160"] >= 3 for group in nonlinear
        ),
        "nonlinear_plateau_ratios_in_range": all(
            0.6 <= group["plateau_ratio_t160_over_t80"] <= 1.4
            for group in nonlinear
        ),
    }
    summary = {"groups": groups, "gates": gates, "all_gates_pass": all(gates.values())}
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    metadata = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": "research/R001_TIME_CONVERGENCE_PROTOCOL.md",
        "record_count": len(records),
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "zero_data_loaded": False,
        "prime_data_loaded": False,
    }
    (output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["all_gates_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
