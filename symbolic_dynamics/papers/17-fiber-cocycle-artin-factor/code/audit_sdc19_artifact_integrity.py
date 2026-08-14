#!/usr/bin/env python3
"""Parse, LF, cache, and frozen-prototype diff audit for SD-C19 artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PROTOTYPE_RESULTS = Path("/tmp/paper17_fiber_cocycle_artin/results")
OUTPUT = RESULTS / "integrity_audit.json"

EXPECTED_CSV_ROWS = {
    "c2_transitivity.csv": 10,
    "cm_character_certificates.csv": 350,
    "cm_regular_local_determinants.csv": 7,
    "coboundary_controls.csv": 84,
    "formal_c2_factorization.csv": 10,
    "inventory_comparison_table.csv": 4,
    "inventory_controls.csv": 64,
    "naturality_summary.csv": 35,
    "naturality_tables.csv": 72079,
    "primitive_lift_census.csv": 350,
    "repetition_trace_ledger.csv": 300,
    "transition_comparison_table.csv": 4,
    "transition_countercontrols.csv": 4,
}


def main() -> int:
    csv_rows: dict[str, int] = {}
    csv_lf_only: dict[str, bool] = {}
    for name, expected in EXPECTED_CSV_ROWS.items():
        path = RESULTS / name
        raw = path.read_bytes()
        csv_lf_only[name] = b"\r" not in raw and raw.endswith(b"\n")
        with path.open(newline="", encoding="utf-8") as handle:
            csv_rows[name] = sum(1 for _ in csv.DictReader(handle))
        if csv_rows[name] != expected:
            raise AssertionError(f"{name}: {csv_rows[name]} rows, expected {expected}")

    json_names = sorted(
        path.name
        for path in RESULTS.glob("*.json")
        if path != OUTPUT
    )
    json_parse = {}
    for name in json_names:
        json.loads((RESULTS / name).read_text(encoding="utf-8"))
        json_parse[name] = True

    cache_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("__pycache__")
    )

    excluded_from_prototype_diff = {
        "SHA256SUMS.txt",
        "integrity_audit.json",
        "test_summary.json",
    }
    common_scientific_files = []
    prototype_differences = []
    if PROTOTYPE_RESULTS.is_dir():
        common_scientific_files = sorted(
            path.name
            for path in RESULTS.iterdir()
            if path.is_file()
            and path.name not in excluded_from_prototype_diff
            and (PROTOTYPE_RESULTS / path.name).is_file()
        )
        for name in common_scientific_files:
            authority_bytes = (RESULTS / name).read_bytes()
            prototype_bytes = (PROTOTYPE_RESULTS / name).read_bytes()
            if name.endswith(".csv"):
                authority_bytes = authority_bytes.replace(b"\r\n", b"\n")
                prototype_bytes = prototype_bytes.replace(b"\r\n", b"\n")
            if authority_bytes != prototype_bytes:
                prototype_differences.append(name)

    payload = {
        "candidate_id": "SD-C19",
        "cache_clean": not cache_paths,
        "cache_paths": cache_paths,
        "csv_lf_only": csv_lf_only,
        "csv_row_counts": csv_rows,
        "json_parse": json_parse,
        "prototype_diff": {
            "available": PROTOTYPE_RESULTS.is_dir(),
            "common_scientific_files": common_scientific_files,
            "differences": prototype_differences,
            "newline_normalized_exact_match": (
                PROTOTYPE_RESULTS.is_dir() and not prototype_differences
            ),
            "excluded": sorted(excluded_from_prototype_diff),
        },
        "target_zero_data_used": False,
    }
    if not all(csv_lf_only.values()) or cache_paths or prototype_differences:
        raise AssertionError("artifact integrity gate failed")
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
