#!/usr/bin/env python3
"""Run the frozen R000 warped-Hénon chaos screen."""

from __future__ import annotations

import argparse
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


def _task(config_dict: dict) -> dict:
    return run_ftle_trajectory(FTLEConfig(**config_dict))


def _summarize(records: list[dict]) -> dict:
    groups: dict[str, list[dict]] = {}
    for record in records:
        key = f"a={record['a']}:n={record['n']}:E={record['energy']}:resolution={record['resolution']}"
        groups.setdefault(key, []).append(record)

    group_summary: dict[str, dict] = {}
    for key, group in sorted(groups.items()):
        valid = [
            row
            for row in group
            if row["status"] == "ok" and row["max_relative_energy_drift"] <= 1.0e-4
        ]
        ftles = np.array([row["ftle_natural"] for row in valid], dtype=float)
        salis = np.array([row["sali"] for row in valid], dtype=float)
        chaotic = [
            row
            for row in valid
            if row["ftle_natural"] > 0.05 and row["sali"] < 1.0e-4
        ]
        group_summary[key] = {
            "records": len(group),
            "valid_records": len(valid),
            "invalid_records": len(group) - len(valid),
            "median_ftle_natural": float(np.median(ftles)) if len(ftles) else None,
            "min_ftle_natural": float(np.min(ftles)) if len(ftles) else None,
            "max_ftle_natural": float(np.max(ftles)) if len(ftles) else None,
            "median_sali": float(np.median(salis)) if len(salis) else None,
            "chaotic_fraction_valid": len(chaotic) / len(valid) if valid else None,
            "chaotic_fraction_all": len(chaotic) / len(group) if group else None,
            "max_energy_drift": max(
                (row["max_relative_energy_drift"] for row in group), default=None
            ),
        }
    indexed = {
        (row["a"], row["n"], row["energy"], row["seed_index"], row["resolution"]): row
        for row in records
    }
    comparisons = []
    for key, primary in sorted(indexed.items()):
        a, n, energy, seed, resolution = key
        if resolution != "primary":
            continue
        refined = indexed.get((a, n, energy, seed, "refined"))
        if refined is None:
            continue
        both_valid = all(
            row["status"] == "ok" and row["max_relative_energy_drift"] <= 1.0e-4
            for row in (primary, refined)
        )
        difference = abs(primary["ftle_natural"] - refined["ftle_natural"])
        tolerance = max(0.02, 0.25 * abs(refined["ftle_natural"]))
        comparisons.append(
            {
                "a": a,
                "n": n,
                "energy": energy,
                "seed_index": seed,
                "both_valid": both_valid,
                "primary_ftle_natural": primary["ftle_natural"],
                "refined_ftle_natural": refined["ftle_natural"],
                "absolute_difference": difference,
                "tolerance": tolerance,
                "stable": bool(both_valid and difference <= tolerance),
            }
        )
    return {"groups": group_summary, "resolution_pairs": comparisons}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("smoke", "r000"), default="smoke")
    parser.add_argument("--workers", type=int, default=min(16, os.cpu_count() or 1))
    parser.add_argument("--output-root", type=Path, default=Path("results"))
    args = parser.parse_args()

    configs: list[dict] = []
    if args.mode == "smoke":
        for a in (0.0, 1.02, 6.0):
            for n in (1, 2, 3):
                for energy in (100.0, 1000.0):
                    for seed in range(2):
                        config = FTLEConfig(
                            energy=energy,
                            a=a,
                            n=n,
                            seed_index=seed,
                            total_natural_time=8.0,
                            steps_per_natural_time=128,
                        )
                        configs.append({**asdict(config), "resolution": "smoke"})
    else:
        # Frozen only after the smoke calibration.  The omitted high-distortion
        # branches remain in the smoke output as explicit failures.
        production_specs = (
            (0.0, 1, 2048),
            (1.02, 1, 4096),
            (6.0, 1, 8192),
            (1.02, 2, 8192),
        )
        for a, n, primary_steps in production_specs:
            for energy in (100.0, 1000.0):
                for seed in range(8):
                    config = FTLEConfig(
                        energy=energy,
                        a=a,
                        n=n,
                        seed_index=seed,
                        total_natural_time=80.0,
                        steps_per_natural_time=primary_steps,
                    )
                    configs.append({**asdict(config), "resolution": "primary"})
                    if seed < 2:
                        refined = FTLEConfig(
                            energy=energy,
                            a=a,
                            n=n,
                            seed_index=seed,
                            total_natural_time=80.0,
                            steps_per_natural_time=2 * primary_steps,
                        )
                        configs.append({**asdict(refined), "resolution": "refined"})

    output_dir = args.output_root / (
        "r000_warped_chaos" if args.mode == "r000" else "r000_warped_chaos_smoke"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict] = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        future_to_config = {}
        for config in configs:
            task_config = {key: value for key, value in config.items() if key != "resolution"}
            future = pool.submit(_task, task_config)
            future_to_config[future] = config
        for future in as_completed(future_to_config):
            config = future_to_config[future]
            try:
                record = future.result()
            except Exception as exc:  # persisted rather than silently dropped
                record = {
                    **config,
                    "status": "exception",
                    "exception": f"{type(exc).__name__}: {exc}",
                    "max_relative_energy_drift": float("inf"),
                    "ftle_natural": float("nan"),
                    "sali": float("nan"),
                }
            record["resolution"] = config["resolution"]
            records.append(record)

    records.sort(
        key=lambda row: (
            row["a"],
            row["n"],
            row["energy"],
            row["seed_index"],
            row["resolution"],
        )
    )
    fieldnames = sorted({key for record in records for key in record})
    with (output_dir / "records.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    summary = _summarize(records)
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, allow_nan=True) + "\n",
        encoding="utf-8",
    )
    metadata = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "mode": args.mode,
        "protocol": "research/R000_WARPED_HENON_CHAOS_PROTOCOL.md",
        "workers": args.workers,
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
    print(json.dumps({"output": str(output_dir), "summary": summary}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
