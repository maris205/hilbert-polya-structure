#!/usr/bin/env python3
"""Refine a float64 orbit catalog and write an independent high-precision audit."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.precision import refine_and_audit


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results" / "periodic_orbits_baseline.json",
    )
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--output-stem", type=str, default="high_precision_audit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8"))
    rows = []
    for orbit in source["orbits"]:
        audit = refine_and_audit(orbit["sequence"], float(orbit["a"]), dps=args.dps)
        rows.append(
            {
                "orbit_id": orbit["orbit_id"],
                "a": orbit["a"],
                "period": orbit["period"],
                "float_trace": orbit["trace"],
                "float_determinant_error": orbit["determinant_error"],
                **audit,
            }
        )

    output_json = PROJECT_ROOT / "results" / f"{args.output_stem}.json"
    output_csv = PROJECT_ROOT / "results" / f"{args.output_stem}.csv"
    payload = {
        "run_id": "R012_high_precision_audit",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source": str(args.input),
        "source_run_id": source.get("run_id"),
        "dps": args.dps,
        "passed": all(row["passed"] for row in rows),
        "orbits": rows,
    }
    output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    csv_rows = []
    for row in rows:
        csv_rows.append(
            {
                key: ";".join(value) if key == "sequence" else value
                for key, value in row.items()
            }
        )
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0]))
        writer.writeheader()
        writer.writerows(csv_rows)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "orbits": len(rows), "passed": payload["passed"]}, indent=2))
    if not payload["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
