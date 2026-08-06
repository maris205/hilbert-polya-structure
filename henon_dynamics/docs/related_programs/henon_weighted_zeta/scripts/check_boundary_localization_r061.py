#!/usr/bin/env python3
"""Independent integrity checker for the R061 boundary-localization ledger.

This checker intentionally does not import the R061 producer/localizer (or
the finite-volume assembly code).  It validates the persisted JSON ledger,
the protocol/coarsening bindings, and each compact NPZ row-array artifact.
The checks are finite-resolution integrity checks only; they do not recompute
the geometric exposure values or make an operator-convergence claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R061_COMMON_CLOUD_PROTOCOL.json"
DEFAULT_INPUT = PROJECT_ROOT / "results" / "boundary_localization_r061.json"
DEFAULT_COARSEN = PROJECT_ROOT / "results" / "common_coarsen_r061.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "boundary_localization_r061_check.json"
DEFAULT_ARRAY_DIR = PROJECT_ROOT / "results" / "boundary_localization_r061_arrays"

ARRAY_KEYS = (
    "row_energy",
    "common_leak",
    "direct_leak",
    "inside_fraction",
    "h_exposure_tau_0.125",
    "cell_exposure_tau_0.125",
    "h_exposure_tau_0.25",
    "cell_exposure_tau_0.25",
    "h_exposure_tau_0.5",
    "cell_exposure_tau_0.5",
    "h_exposure_tau_1.0",
    "cell_exposure_tau_1.0",
)
EXPOSURE_KEYS = tuple(key for key in ARRAY_KEYS if "exposure" in key or key == "inside_fraction")
LEAK_KEYS = ("common_leak", "direct_leak")
ENERGY_TOL = 1.0e-12
RANGE_TOL = 1.0e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--coarsen", type=Path, default=DEFAULT_COARSEN)
    parser.add_argument("--array-dir", type=Path, default=DEFAULT_ARRAY_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--smoke", action="store_true", help="check a smoke ledger (six records)")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def portable(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def resolve_project_path(value: Any) -> Path:
    """Resolve a persisted project-relative path without importing producers."""

    raw = Path(str(value))
    return raw if raw.is_absolute() else PROJECT_ROOT / raw


def finite_number(value: Any) -> bool:
    try:
        return bool(np.isfinite(float(value)))
    except (TypeError, ValueError):
        return False


def in_unit_interval(value: Any, tol: float = RANGE_TOL) -> bool:
    return finite_number(value) and -tol <= float(value) <= 1.0 + tol


def expected_row_count(record: dict[str, Any]) -> int | None:
    try:
        target = int(record["target_grid"])
    except (KeyError, TypeError, ValueError):
        return None
    if target < 2:
        return None
    return 4 * target * target


def link_fields(record: dict[str, Any]) -> tuple[str, ...]:
    return (
        "chain",
        "fine_grid",
        "target_grid",
        "ratio",
        "method_family",
        "samples_per_cell",
        "effective_samples_per_cell",
        "quadrature_order",
        "seed",
    )


def scalar_equal(left: Any, right: Any) -> bool:
    """JSON scalar equality with integer/None normalization."""

    if left is None or right is None:
        return left is None and right is None
    if isinstance(left, (int, np.integer)) and isinstance(right, (int, np.integer)):
        return int(left) == int(right)
    if isinstance(left, (float, np.floating)) and isinstance(right, (float, np.floating)):
        return bool(math.isclose(float(left), float(right), rel_tol=0.0, abs_tol=0.0))
    return left == right


def validate_array(
    path: Path,
    record: dict[str, Any],
    expected_array_dir: Path,
) -> dict[str, Any]:
    checks: dict[str, Any] = {
        "exists": path.exists(),
        "is_file": path.is_file(),
        "path_under_array_dir": False,
        "sha256": False,
        "loadable": False,
        "keys_exact": False,
        "arrays_1d": False,
        "row_lengths": False,
        "finite": False,
        "energy_nonnegative": False,
        "leak_range": False,
        "exposure_range": False,
    }
    try:
        checks["path_under_array_dir"] = path.resolve().parent == expected_array_dir.resolve()
    except OSError:
        checks["path_under_array_dir"] = False
    if not checks["exists"] or not checks["is_file"]:
        return checks
    try:
        checks["sha256"] = sha256_file(path) == str(record.get("array_sha256"))
    except OSError:
        checks["sha256"] = False
    try:
        with np.load(path, allow_pickle=False) as data:
            keys = tuple(sorted(str(x) for x in data.files))
            checks["keys_exact"] = keys == tuple(sorted(ARRAY_KEYS))
            row_count = int(record.get("row_count", -1))
            arrays: dict[str, np.ndarray] = {}
            one_d = True
            lengths = True
            finite = True
            for key in ARRAY_KEYS:
                if key not in data.files:
                    one_d = False
                    lengths = False
                    continue
                array = np.asarray(data[key])
                arrays[key] = array
                one_d = one_d and array.ndim == 1
                lengths = lengths and array.ndim == 1 and array.size == row_count
                finite = finite and bool(np.all(np.isfinite(array)))
            checks["arrays_1d"] = one_d
            checks["row_lengths"] = lengths
            checks["finite"] = finite
            if "row_energy" in arrays:
                checks["energy_nonnegative"] = bool(np.min(arrays["row_energy"], initial=0.0) >= -ENERGY_TOL)
            if all(key in arrays for key in LEAK_KEYS):
                checks["leak_range"] = bool(
                    all(
                        np.min(arrays[key], initial=0.0) >= -RANGE_TOL
                        and np.max(arrays[key], initial=0.0) <= 1.0 + RANGE_TOL
                        for key in LEAK_KEYS
                    )
                )
            if all(key in arrays for key in EXPOSURE_KEYS):
                checks["exposure_range"] = bool(
                    all(
                        np.min(arrays[key], initial=0.0) >= -RANGE_TOL
                        and np.max(arrays[key], initial=0.0) <= 1.0 + RANGE_TOL
                        for key in EXPOSURE_KEYS
                    )
                )
            checks["loadable"] = True
    except (OSError, ValueError, EOFError, TypeError):
        checks["loadable"] = False
    return checks


def validate_record(
    record: dict[str, Any],
    coarsen_by_id: dict[str, dict[str, Any]],
    array_dir: Path,
) -> dict[str, Any]:
    cid = str(record.get("config_id"))
    check: dict[str, Any] = {
        "config_id": cid,
        "unique": True,
        "coarsen_record": cid in coarsen_by_id,
    }
    coarsen = coarsen_by_id.get(cid)
    if coarsen is None:
        check["pass"] = False
        return check

    check["run_id"] = record.get("config_id") is not None and record.get("chain") is not None
    # The localizer's metadata must agree exactly with the common-coarsen
    # record it describes, including matrix paths and hashes.
    metadata_ok = True
    for key in link_fields(record):
        if key in coarsen:
            metadata_ok = metadata_ok and scalar_equal(record.get(key), coarsen.get(key))
    check["metadata_link"] = metadata_ok
    check["common_matrix_link"] = (
        record.get("common_matrix_path") == coarsen.get("matrix_path")
        and record.get("common_matrix_sha256") == coarsen.get("matrix_sha256")
    )
    check["direct_matrix_link"] = (
        record.get("direct_matrix_path") == coarsen.get("direct_matrix_path")
        and record.get("direct_matrix_sha256") == coarsen.get("direct_matrix_sha256")
    )
    check["matrix_link_fields"] = all(
        key in record and finite_number(record[key])
        for key in ("fine_grid", "target_grid", "ratio", "effective_samples_per_cell")
    )
    expected_rows = expected_row_count(record)
    check["expected_row_count"] = expected_rows is not None and int(record.get("row_count", -1)) == expected_rows
    check["positive_point_count"] = isinstance(record.get("point_count"), (int, np.integer)) and int(record["point_count"]) > 0
    check["boundary_hits_zero"] = int(record.get("boundary_hits", -1)) == 0
    check["record_scalars_finite"] = all(
        finite_number(record.get(key))
        for key in ("total_row_energy", "positive_energy_row_fraction", "common_mean_leak", "direct_mean_leak")
    )
    check["record_ranges"] = (
        float(record.get("total_row_energy", -1.0)) >= -ENERGY_TOL
        and in_unit_interval(record.get("positive_energy_row_fraction"))
        and in_unit_interval(record.get("common_mean_leak"))
        and in_unit_interval(record.get("direct_mean_leak"))
    )
    tau_summary = record.get("tau_summary")
    tau_ok = isinstance(tau_summary, dict) and set(tau_summary) == {"0.125", "0.25", "0.5", "1.0"}
    if tau_ok:
        for row in tau_summary.values():
            if not isinstance(row, dict):
                tau_ok = False
                break
            for key in ("spearman_h", "spearman_cell"):
                value = row.get(key)
                if value is not None and (not finite_number(value) or not -1.0 - RANGE_TOL <= float(value) <= 1.0 + RANGE_TOL):
                    tau_ok = False
            for key in ("top25_h", "top25_cell", "mean_h", "mean_cell"):
                if not in_unit_interval(row.get(key)):
                    tau_ok = False
    check["tau_summary"] = tau_ok

    array_value = record.get("array_path")
    array_path = resolve_project_path(array_value)
    check["array_path_recorded"] = isinstance(array_value, str) and bool(array_value)
    array_checks = validate_array(array_path, record, array_dir)
    check["array"] = array_checks
    scalar_checks = [
        value
        for key, value in check.items()
        if key not in {"config_id", "array"} and isinstance(value, bool)
    ]
    array_bool_checks = [value for value in array_checks.values() if isinstance(value, bool)]
    check["pass"] = bool(scalar_checks and all(scalar_checks) and array_bool_checks and all(array_bool_checks))
    return check


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    coarsen = json.loads(args.coarsen.read_text(encoding="utf-8"))

    protocol_sha = sha256_file(args.protocol)
    records = list(payload.get("records", []))
    coarsen_records = list(coarsen.get("records", []))
    coarsen_by_id = {str(row.get("config_id")): row for row in coarsen_records}
    expected_count = 6 if args.smoke else int(protocol.get("design", {}).get("derived_matrix_count", 136))

    ids = [str(row.get("config_id")) for row in records]
    seen: set[str] = set()
    duplicate_ids: list[str] = []
    for cid in ids:
        if cid in seen:
            duplicate_ids.append(cid)
        seen.add(cid)
    record_checks = [validate_record(row, coarsen_by_id, args.array_dir) for row in records]

    protocol_outputs = protocol.get("outputs", {})
    checks: dict[str, Any] = {
        "run_id": payload.get("run_id") == "R061_BOUNDARY_LOCALIZATION",
        "protocol_exists": args.protocol.exists(),
        "protocol_sha256": payload.get("protocol_sha256") == protocol_sha,
        "protocol_output_link": payload.get("protocol_path") == portable(args.protocol),
        "protocol_localization_output": protocol_outputs.get("localization") == portable(args.input),
        "coarsen_exists": args.coarsen.exists(),
        "coarsen_output_link": payload.get("coarsen_path") == portable(args.coarsen),
        "coarsen_protocol_link": coarsen.get("protocol_sha256") == protocol_sha,
        "coarsen_run_id": coarsen.get("run_id") == "R061_COMMON_CLOUD",
        "record_count": len(records) == expected_count and int(payload.get("record_count", -1)) == len(records),
        "unique_record_ids": len(seen) == len(records) and not duplicate_ids,
        "coarsen_record_count": len(coarsen_records) == expected_count,
        "record_id_set_matches_coarsen": set(ids) == set(coarsen_by_id) and len(coarsen_by_id) == expected_count,
        "frozen_configuration": bool(payload.get("frozen_configuration")) if not args.smoke else True,
        "array_directory_exists": args.array_dir.is_dir(),
        "all_record_checks": bool(record_checks) and all(bool(row.get("pass")) for row in record_checks),
    }
    all_pass = bool(all(value for value in checks.values() if isinstance(value, bool)))
    output = {
        "run_id": "R061_BOUNDARY_LOCALIZATION_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "input": portable(args.input),
        "protocol": portable(args.protocol),
        "coarsen": portable(args.coarsen),
        "array_dir": portable(args.array_dir),
        "protocol_sha256": protocol_sha,
        "expected_record_count": expected_count,
        "record_count": len(records),
        "duplicate_ids": duplicate_ids,
        "checks": checks,
        "record_checks": record_checks,
        "all_checks_pass": all_pass,
        "scope": "Independent finite-resolution boundary-array integrity check; no continuous-operator claim.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": portable(args.output), "records_checked": len(records), "all_checks_pass": all_pass, "expected": expected_count}, indent=2))
    if not all_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
