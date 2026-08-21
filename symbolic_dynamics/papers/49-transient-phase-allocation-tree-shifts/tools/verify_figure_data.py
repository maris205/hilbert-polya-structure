#!/usr/bin/env python3
"""Independent checks for the writer's deterministic figure data."""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "figures" / "data"
SOURCE = ROOT / "inputs" / "level_l.json"
SOURCE_SHA256 = "cf8ae3ee10fd798d937bed725b6a55ad0635e5dcdfdb29fb0c1070f2290a63f9"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 5e-15) -> bool:
    return abs(left - right) <= tolerance


def main() -> None:
    assertions = 0
    assert sha256(SOURCE) == SOURCE_SHA256
    assertions += 1
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    provenance = json.loads((DATA / "figure_provenance.json").read_text(encoding="utf-8"))
    assertions += provenance["source"]["sha256"] == SOURCE_SHA256

    exact_source = {}
    for row in source["selected_optimizers"]:
        key = (row["d"], row["p"], tuple(row["a"]), row["level"])
        exact_source[key] = row
    with (DATA / "fig2_exact.csv").open(encoding="utf-8", newline="") as handle:
        exact_rows = list(csv.DictReader(handle))
    assert len(exact_rows) == 9
    assertions += 1
    for row in provenance["figure_3"]["exact_optimizer_rows"]:
        key = (row["d"], row["p"], tuple(row["a"]), row["level"])
        source_row = exact_source[key]
        assert source_row["m"] == row["optimizer"]
        assert source_row["dimension"] == row["exact_dimension"]
        dimension = float(row["dimension"])
        mean = sum(math.log(value) for value in row["a"]) / row["p"]
        assert close(float(row["spectral_mean"]), mean)
        assert close(float(row["gap"]), mean - dimension)
        assertions += 4

    convergence_source = {}
    for profile in source["convergence_records"]:
        for row in profile["rows"]:
            key = (profile["d"], profile["p"], tuple(profile["a"]), row["level"])
            convergence_source[key] = row
    with (DATA / "fig2_balanced.csv").open(encoding="utf-8", newline="") as handle:
        balanced_rows = list(csv.DictReader(handle))
    assert len(balanced_rows) == 16
    assertions += 1
    for row in provenance["figure_3"]["balanced_certificate_rows"]:
        key = (row["d"], row["p"], tuple(row["a"]), row["level"])
        source_row = convergence_source[key]
        assert source_row["m"] == row["balanced_composition"]
        assert source_row["gap"] == row["source_gap"]
        assert source_row["upper_bound"] == row["source_certificate"]
        assert float(row["certificate"]) >= float(row["balanced_gap"]) > 0.0
        assertions += 4

    with (DATA / "fig3_p2.csv").open(encoding="utf-8", newline="") as handle:
        p2_rows = list(csv.DictReader(handle))
    assert len(p2_rows) == 11
    assertions += 1
    log_two = math.log(2.0)
    for row in p2_rows:
        d = int(row["d"])
        expected_core = log_two / (d + 1)
        expected_mean = log_two / 2
        expected_feeder = (
            expected_mean
            if d % 2 == 0
            else expected_mean - (d - 1) * log_two / (2 * d * (d + 1))
        )
        assert close(float(row["component"]), expected_core)
        assert close(float(row["spectral_mean"]), expected_mean)
        assert close(float(row["feeder"]), expected_feeder)
        assert row["parity"] == ("even" if d % 2 == 0 else "odd")
        assertions += 4

    hash_receipt = json.loads((DATA / "figure_data_hashes.json").read_text(encoding="utf-8"))
    for name, expected in hash_receipt.items():
        assert sha256(DATA / name) == expected
        assertions += 1
    print(f"FIGURE_DATA_OK assertions={assertions}")


if __name__ == "__main__":
    main()
