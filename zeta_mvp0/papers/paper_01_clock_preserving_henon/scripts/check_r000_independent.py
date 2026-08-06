#!/usr/bin/env python3
"""Independent R000 checker that does not import the production package."""

from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import median


ROOT = Path("results/r000_warped_chaos")


def centered_henon(x: float, y: float, a: float) -> tuple[float, float]:
    fixed = 1.0 / (1.0 + math.sqrt(1.0 + a))
    return -2.0 * a * fixed * x - a * x * x - y, x


def independent_initial_energy(row: dict[str, str]) -> float:
    x = float(row["initial_q0"])
    y = float(row["initial_q1"])
    a = float(row["a"])
    for _ in range(int(row["n"])):
        x, y = centered_henon(x, y, a)
    potential = 2.0 * math.pi * math.exp(math.pi * (x * x + y * y))
    p0 = float(row["initial_p0"])
    p1 = float(row["initial_p1"])
    return 0.5 * (p0 * p0 + p1 * p1) + potential


def main() -> int:
    with (ROOT / "records.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    summary = json.loads((ROOT / "summary.json").read_text(encoding="utf-8"))
    metadata = json.loads((ROOT / "metadata.json").read_text(encoding="utf-8"))

    checks: dict[str, object] = {}
    checks["record_count_80"] = len(rows) == 80
    checks["all_completed"] = all(row["status"] == "ok" for row in rows)
    checks["all_energy_drift_valid"] = all(
        float(row["max_relative_energy_drift"]) <= 1.0e-4 for row in rows
    )
    relative_initial_errors = []
    for row in rows:
        independently_computed = independent_initial_energy(row)
        requested = float(row["energy"])
        relative_initial_errors.append(abs(independently_computed - requested) / requested)
    checks["max_independent_initial_energy_error"] = max(relative_initial_errors)
    checks["initial_energy_identity"] = max(relative_initial_errors) <= 2.0e-11
    checks["zero_and_prime_data_absent"] = (
        metadata.get("zero_data_loaded") is False
        and metadata.get("prime_data_loaded") is False
    )

    groups: dict[tuple[float, int, float, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[
            (
                float(row["a"]),
                int(row["n"]),
                float(row["energy"]),
                row["resolution"],
            )
        ].append(row)

    recomputed = {}
    summary_matches = True
    for key, group in sorted(groups.items()):
        a, n, energy, resolution = key
        ftles = [float(row["ftle_natural"]) for row in group]
        salis = [float(row["sali"]) for row in group]
        chaotic = [
            row
            for row in group
            if float(row["ftle_natural"]) > 0.05 and float(row["sali"]) < 1.0e-4
        ]
        label = f"a={a}:n={n}:E={energy}:resolution={resolution}"
        recomputed[label] = {
            "records": len(group),
            "median_ftle_natural": median(ftles),
            "median_sali": median(salis),
            "chaotic_fraction": len(chaotic) / len(group),
        }
        stored = summary["groups"][label]
        summary_matches &= stored["records"] == len(group)
        summary_matches &= math.isclose(
            stored["median_ftle_natural"], median(ftles), rel_tol=1e-13, abs_tol=1e-13
        )
        summary_matches &= math.isclose(
            stored["median_sali"], median(salis), rel_tol=1e-13, abs_tol=1e-13
        )
        summary_matches &= math.isclose(
            stored["chaotic_fraction_all"],
            len(chaotic) / len(group),
            rel_tol=1e-13,
            abs_tol=1e-13,
        )
    checks["stored_summary_reproduced"] = bool(summary_matches)

    primary_groups = {
        key: value for key, value in recomputed.items() if key.endswith("resolution=primary")
    }
    radial_fractions = [
        value["chaotic_fraction"]
        for key, value in primary_groups.items()
        if key.startswith("a=0.0:")
    ]
    nonlinear_fractions = [
        value["chaotic_fraction"]
        for key, value in primary_groups.items()
        if not key.startswith("a=0.0:")
    ]
    checks["radial_primary_has_zero_joint_flags"] = radial_fractions == [0.0, 0.0]
    checks["all_nonlinear_primary_groups_pass_retention_gate"] = all(
        fraction >= 0.10 for fraction in nonlinear_fractions
    )

    pairs = summary["resolution_pairs"]
    checks["resolution_pair_count_16"] = len(pairs) == 16
    checks["stable_resolution_pairs"] = sum(bool(pair["stable"]) for pair in pairs)
    checks["unstable_resolution_pairs"] = [
        {
            "a": pair["a"],
            "n": pair["n"],
            "energy": pair["energy"],
            "seed_index": pair["seed_index"],
        }
        for pair in pairs
        if not pair["stable"]
    ]

    boolean_checks = [value for value in checks.values() if isinstance(value, bool)]
    output = {
        "independent_implementation": True,
        "imports_production_package": False,
        "checks": checks,
        "all_boolean_checks_pass": all(boolean_checks),
        "recomputed_groups": recomputed,
    }
    (ROOT / "independent_checker.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_boolean_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
