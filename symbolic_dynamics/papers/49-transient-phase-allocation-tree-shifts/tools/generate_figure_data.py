#!/usr/bin/env python3
"""Generate the deterministic numeric data used by Figures 2 and 3.

The Stage-2 evidence tree is immutable.  This script refuses to run if its
source evidence does not have the frozen hash recorded at writer intake.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "data"
SOURCE = ROOT / "inputs" / "level_l.json"
EXPECTED_SOURCE_SHA256 = (
    "cf8ae3ee10fd798d937bed725b6a55ad0635e5dcdfdb29fb0c1070f2290a63f9"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def profile_id(d: int, p: int, a: list[int]) -> str:
    return f"d{d}_p{p}_a" + "-".join(str(value) for value in a)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    actual_source_hash = sha256(SOURCE)
    if actual_source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit(
            f"frozen source hash mismatch: {actual_source_hash} != "
            f"{EXPECTED_SOURCE_SHA256}"
        )

    evidence = json.loads(SOURCE.read_text(encoding="utf-8"))

    exact_keys = {
        (2, 3, (1, 2, 3)): (0, "binary, three phases"),
        (2, 4, (1, 2, 3, 1)): (1, "binary, four phases"),
        (3, 2, (1, 2)): (2, "ternary, two phases"),
    }
    exact_rows: list[dict[str, object]] = []
    exact_receipts: list[dict[str, object]] = []
    for record in evidence["selected_optimizers"]:
        key = (record["d"], record["p"], tuple(record["a"]))
        if key not in exact_keys:
            continue
        mean = sum(math.log(value) for value in record["a"]) / record["p"]
        dimension = float(record["dimension_decimal"])
        series, label = exact_keys[key]
        row = {
            "profile": profile_id(record["d"], record["p"], record["a"]),
            "series": series,
            "label": label,
            "level": record["level"],
            "dimension": f"{dimension:.16f}",
            "spectral_mean": f"{mean:.16f}",
            "gap": f"{mean - dimension:.16f}",
        }
        exact_rows.append(row)
        exact_receipts.append(
            {
                **row,
                "a": record["a"],
                "d": record["d"],
                "p": record["p"],
                "optimizer": record["m"],
                "exact_dimension": record["dimension"],
                "composition_count": record["composition_count"],
            }
        )
    exact_rows.sort(key=lambda row: (str(row["profile"]), int(row["level"])))
    exact_receipts.sort(key=lambda row: (str(row["profile"]), int(row["level"])))
    if len(exact_rows) != 9:
        raise SystemExit(f"expected 9 exact optimizer rows, found {len(exact_rows)}")

    balanced_keys = {
        (2, 3, (2, 3, 4)): (0, "binary, three phases"),
        (3, 4, (2, 3, 4, 2)): (1, "ternary, four phases"),
    }
    balanced_rows: list[dict[str, object]] = []
    balanced_receipts: list[dict[str, object]] = []
    for profile in evidence["convergence_records"]:
        key = (profile["d"], profile["p"], tuple(profile["a"]))
        if key not in balanced_keys:
            continue
        series, label = balanced_keys[key]
        for record in profile["rows"]:
            gap = float(record["gap"])
            bound = float(record["upper_bound"])
            if not (gap > 0.0 and bound >= gap):
                raise SystemExit(f"invalid nonzero balanced gap/bound for {key}: {record}")
            row = {
                "profile": profile_id(profile["d"], profile["p"], profile["a"]),
                "series": series,
                "label": label,
                "level": record["level"],
                "balanced_gap": f"{gap:.18g}",
                "certificate": f"{bound:.18g}",
            }
            balanced_rows.append(row)
            balanced_receipts.append(
                {
                    **row,
                    "a": profile["a"],
                    "d": profile["d"],
                    "p": profile["p"],
                    "balanced_composition": record["m"],
                    "source_gap": record["gap"],
                    "source_certificate": record["upper_bound"],
                }
            )
    balanced_rows.sort(key=lambda row: (str(row["profile"]), int(row["level"])))
    balanced_receipts.sort(key=lambda row: (str(row["profile"]), int(row["level"])))
    if len(balanced_rows) != 16:
        raise SystemExit(f"expected 16 balanced rows, found {len(balanced_rows)}")

    p2_rows: list[dict[str, object]] = []
    log_two = math.log(2.0)
    for d in range(2, 13):
        component = log_two / (d + 1)
        mean = log_two / 2.0
        if d % 2 == 0:
            feeder = mean
        else:
            feeder = mean - (d - 1) * log_two / (2 * d * (d + 1))
        p2_rows.append(
            {
                "d": d,
                "component": f"{component:.16f}",
                "feeder": f"{feeder:.16f}",
                "spectral_mean": f"{mean:.16f}",
                "parity": "even" if d % 2 == 0 else "odd",
            }
        )

    write_csv(
        OUT / "fig2_exact.csv",
        ["series", "level", "dimension", "spectral_mean", "gap"],
        exact_rows,
    )
    write_csv(
        OUT / "fig2_balanced.csv",
        ["series", "level", "balanced_gap", "certificate"],
        balanced_rows,
    )
    write_csv(
        OUT / "fig3_p2.csv",
        ["d", "component", "feeder", "spectral_mean", "parity"],
        p2_rows,
    )

    provenance = {
        "schema": "p49-writer-figure-data-v1",
        "source": {
            "path": "inputs/level_l.json",
            "sha256": actual_source_hash,
        },
        "figure_3": {
            "exact_optimizer_rows": exact_receipts,
            "balanced_certificate_rows": balanced_receipts,
            "interpretation": (
                "Exact optimizers are copied from the frozen exhaustive sweep; "
                "balanced gaps and certificates are copied from its deterministic "
                "convergence controls."
            ),
        },
        "figure_2": {
            "a": [1, 2],
            "d_range": [2, 12],
            "formula": (
                "component=log(2)/(d+1); feeder=log(2)/2 for even d, "
                "otherwise log(2)/2-(d-1)log(2)/(2d(d+1))"
            ),
            "rows": p2_rows,
        },
    }
    provenance_path = OUT / "figure_provenance.json"
    provenance_path.write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    output_hashes = {
        path.name: sha256(path)
        for path in sorted(OUT.glob("*"))
        if path.is_file() and path.name != "figure_data_hashes.json"
    }
    (OUT / "figure_data_hashes.json").write_text(
        json.dumps(output_hashes, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
