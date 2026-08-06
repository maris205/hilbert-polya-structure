#!/usr/bin/env python3
"""Independent checker for the R060 operator-variance production.

This file intentionally does not import the R060 producer or
``henon_zeta.restricted_operator``.  It independently reconstructs frozen
source rows, sampling fingerprints, matrix/schema hashes, and the paired
Sobol-prefix invariant.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from scipy.sparse import csr_matrix, load_npz
from scipy.stats import qmc


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATE_ORDER = ("--", "-+", "+-", "++")
BOUNDS = {
    "--": (-5.0 / 8.0, -1.0 / 3.0, -81.0 / 128.0, -5.0 / 16.0),
    "-+": (-5.0 / 8.0, -1.0 / 3.0, 5.0 / 16.0, 81.0 / 128.0),
    "+-": (1.0 / 3.0, 5.0 / 8.0, -81.0 / 128.0, -5.0 / 16.0),
    "++": (1.0 / 3.0, 5.0 / 8.0, 5.0 / 16.0, 81.0 / 128.0),
}
EXPECTED_INDEXING = "global=state_index*m^2 + y_index*m + x_index; state-major, x index fastest"
EXPECTED_TARGET_SEMANTICS = "strict h-set interior followed by half-open local cells; exact h-set/cell-boundary hits are counted and discarded"
SOURCE_ROW_LOCAL_FRACTIONS = (0.0, 0.5, 1.0)
SOURCE_ROW_TOLERANCE = 2.0e-12


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=PROJECT_ROOT / "results" / "operator_variance_r060.json")
    parser.add_argument("--output", type=Path, default=PROJECT_ROOT / "results" / "operator_variance_r060_check.json")
    parser.add_argument("--protocol", type=Path, default=PROJECT_ROOT / "research" / "refine-logs" / "R060_OPERATOR_VARIANCE_PROTOCOL.json")
    parser.add_argument("--row-sum-tolerance", type=float, default=1.0e-12)
    parser.add_argument("--row-value-tolerance", type=float, default=SOURCE_ROW_TOLERANCE)
    parser.add_argument("--max-records", type=int)
    parser.add_argument("--smoke", action="store_true", help="allow an intentionally incomplete smoke payload")
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def project(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def cell_centers(state: str, m: int) -> tuple[np.ndarray, float, float]:
    xl, xu, yl, yu = BOUNDS[state]
    wx = (xu - xl) / m
    wy = (yu - yl) / m
    x = xl + (np.arange(m, dtype=float) + 0.5) * wx
    y = yl + (np.arange(m, dtype=float) + 0.5) * wy
    xx, yy = np.meshgrid(x, y, indexing="xy")
    return np.column_stack((xx.ravel(), yy.ravel())), wx, wy


def source_rows(m: int) -> np.ndarray:
    local_indices = sorted({min(m * m - 1, max(0, int(round(frac * (m * m - 1))))) for frac in SOURCE_ROW_LOCAL_FRACTIONS})
    return np.asarray([state_index * m * m + local for state_index in range(4) for local in local_indices], dtype=np.int64)


def target_lookup(points: np.ndarray, m: int) -> tuple[np.ndarray, np.ndarray, int]:
    image_x = 1.0 - 6.0 * points[:, 0] ** 2 - points[:, 1]
    image_y = points[:, 0]
    target = np.full(points.shape[0], -1, dtype=np.int64)
    valid = np.zeros(points.shape[0], dtype=bool)
    boundary_hits = 0
    for state_index, state in enumerate(STATE_ORDER):
        xl, xu, yl, yu = BOUNDS[state]
        closed = (image_x >= xl) & (image_x <= xu) & (image_y >= yl) & (image_y <= yu)
        interior = (image_x > xl) & (image_x < xu) & (image_y > yl) & (image_y < yu)
        boundary_hits += int(np.count_nonzero(closed & ~interior))
        if not np.any(interior):
            continue
        positions = np.flatnonzero(interior)
        wx = (xu - xl) / m
        wy = (yu - yl) / m
        ux = (image_x[interior] - xl) / wx
        uy = (image_y[interior] - yl) / wy
        ix = np.floor(ux).astype(np.int64)
        iy = np.floor(uy).astype(np.int64)
        on_cell = (ux == np.floor(ux)) | (uy == np.floor(uy))
        boundary_hits += int(np.count_nonzero(on_cell))
        accepted = ~on_cell & (ix >= 0) & (ix < m) & (iy >= 0) & (iy < m)
        chosen = positions[accepted]
        target[chosen] = state_index * m * m + iy[accepted] * m + ix[accepted]
        valid[chosen] = True
    return target, valid, boundary_hits


def independent_sampling_fingerprint(
    method_family: str,
    grid: int,
    seed: int | None,
    samples_per_cell: int,
    quadrature_order: int,
) -> dict[str, Any]:
    if method_family == "sobol":
        if seed is None:
            raise ValueError("missing Sobol seed")
        exponent = int(round(math.log2(samples_per_cell)))
        if 2**exponent != samples_per_cell:
            raise ValueError("Sobol sample count is not a power of two")
        base = np.ascontiguousarray(qmc.Sobol(d=2, scramble=True, seed=int(seed)).random_base2(exponent), dtype=np.float64)
        shifts = np.ascontiguousarray(np.random.default_rng(int(seed) + 1_000_003).random((4 * grid * grid, 2)), dtype=np.float64)
        prefix = base[:64] if samples_per_cell >= 64 else base
        return {
            "rule": "scipy.stats.qmc.Sobol(d=2,scramble=True,seed), random_base2; per-cell PCG64 seed+1000003",
            "base_point_count": int(base.shape[0]),
            "base_sha256": sha256_bytes(base.tobytes(order="C")),
            "base_prefix64_sha256": sha256_bytes(prefix.tobytes(order="C")),
            "shift_shape": list(shifts.shape),
            "shift_sha256": sha256_bytes(shifts.tobytes(order="C")),
            "paired_prefix_rule": "At fixed grid and seed, samples=64 is the first 64 scrambled points and uses the identical shift array as samples=256.",
        }
    nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)
    nodes = np.ascontiguousarray(nodes, dtype=np.float64)
    weights = np.ascontiguousarray(weights, dtype=np.float64)
    return {
        "rule": "numpy.polynomial.legendre.leggauss",
        "node_count": int(nodes.size),
        "nodes_sha256": sha256_bytes(nodes.tobytes(order="C")),
        "weights_sha256": sha256_bytes(weights.tobytes(order="C")),
    }


def independent_rows(
    m: int,
    method_family: str,
    seed: int | None,
    samples_per_cell: int,
    quadrature_order: int,
) -> tuple[dict[int, dict[int, float]], int]:
    centers: list[np.ndarray] = []
    widths: list[np.ndarray] = []
    for state in STATE_ORDER:
        grid, wx, wy = cell_centers(state, m)
        centers.append(grid)
        widths.append(np.tile(np.asarray([wx, wy]), (grid.shape[0], 1)))
    all_centers = np.concatenate(centers, axis=0)
    all_widths = np.concatenate(widths, axis=0)
    rows = source_rows(m)
    source = all_centers[rows]
    source_widths = all_widths[rows]
    expected: dict[int, dict[int, float]] = {int(row): {} for row in rows}
    boundary_hits = 0
    if method_family == "gauss":
        nodes, weights_legendre = np.polynomial.legendre.leggauss(quadrature_order)
        batches = [(np.asarray([xn, yn], dtype=float), float(xw * yw / 4.0)) for xn, xw in zip(nodes, weights_legendre) for yn, yw in zip(nodes, weights_legendre)]
        for local_unit, weight in batches:
            points = source + 0.5 * source_widths * local_unit
            target, valid, hits = target_lookup(points, m)
            boundary_hits += hits
            for row, column in zip(rows[valid], target[valid]):
                row_map = expected[int(row)]
                row_map[int(column)] = row_map.get(int(column), 0.0) + weight
        return expected, boundary_hits
    if seed is None:
        raise ValueError("Sobol rows require a seed")
    exponent = int(round(math.log2(samples_per_cell)))
    base = qmc.Sobol(d=2, scramble=True, seed=int(seed)).random_base2(exponent)
    full_shifts = np.random.default_rng(int(seed) + 1_000_003).random((4 * m * m, 2))
    shifts = full_shifts[rows]
    for point in base:
        local_unit = np.mod(point + shifts, 1.0)
        points = source + (local_unit - 0.5) * source_widths
        target, valid, hits = target_lookup(points, m)
        boundary_hits += hits
        weight = 1.0 / samples_per_cell
        for row, column in zip(rows[valid], target[valid]):
            row_map = expected[int(row)]
            row_map[int(column)] = row_map.get(int(column), 0.0) + weight
    return expected, boundary_hits


def compare_rows(matrix: csr_matrix, expected: dict[int, dict[int, float]], tolerance: float) -> tuple[bool, list[dict[str, Any]]]:
    checks: list[dict[str, Any]] = []
    all_pass = True
    for row in sorted(expected):
        actual_row = matrix.getrow(int(row))
        actual = {int(col): float(value) for col, value in zip(actual_row.indices, actual_row.data)}
        wanted = expected[row]
        keys_match = set(actual) == set(wanted)
        values_match = keys_match and all(math.isclose(actual[col], wanted[col], rel_tol=tolerance, abs_tol=tolerance) for col in wanted)
        passed = bool(keys_match and values_match)
        all_pass = all_pass and passed
        checks.append({"row": int(row), "expected_nnz": len(wanted), "observed_nnz": len(actual), "keys_match": keys_match, "values_match": values_match, "pass": passed})
    return all_pass, checks


def expected_configs(protocol: dict[str, Any]) -> dict[str, dict[str, Any]]:
    design = protocol["design"]
    expected: dict[str, dict[str, Any]] = {}
    for grid in design["grids"]:
        for samples in design["sobol_samples_per_cell"]:
            for seed in design["fresh_sobol_seeds"]:
                key = f"r060_m{int(grid):03d}_sobol{int(samples)}_seed{int(seed)}"
                expected[key] = {"grid": int(grid), "method_family": "sobol", "samples_per_cell": int(samples), "quadrature_order": 0, "seed": int(seed)}
        for order in design["gauss_orders"]:
            key = f"r060_m{int(grid):03d}_gauss_q{int(order)}"
            expected[key] = {"grid": int(grid), "method_family": "gauss", "samples_per_cell": int(order) ** 2, "quadrature_order": int(order), "seed": None}
    return expected


def check_record(record: dict[str, Any], protocol_sha: str, row_tolerance: float, row_sum_tolerance: float) -> dict[str, Any]:
    config_id = str(record.get("config_id"))
    result: dict[str, Any] = {"config_id": config_id}
    matrix_path = PROJECT_ROOT / str(record.get("matrix_path", ""))
    schema_path = PROJECT_ROOT / str(record.get("schema_path", ""))
    result["matrix_exists"] = matrix_path.exists()
    result["schema_exists"] = schema_path.exists()
    if not matrix_path.exists() or not schema_path.exists():
        result["pass"] = False
        return result
    actual_matrix_sha = sha256_file(matrix_path)
    actual_schema_sha = sha256_file(schema_path)
    result["matrix_sha_match"] = actual_matrix_sha == record.get("matrix_sha256")
    result["schema_sha_match"] = actual_schema_sha == record.get("schema_sha256")
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        matrix = load_npz(matrix_path).tocsr()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result["load_error"] = repr(exc)
        result["pass"] = False
        return result
    result["schema_protocol_match"] = schema.get("protocol_sha256") == protocol_sha
    result["schema_indexing_match"] = schema.get("indexing") == EXPECTED_INDEXING
    result["schema_semantics_match"] = schema.get("target_semantics") == EXPECTED_TARGET_SEMANTICS
    result["shape_match"] = list(matrix.shape) == list(record.get("matrix_shape", [])) == list(schema.get("shape", []))
    result["dtype_match"] = str(matrix.dtype) == str(schema.get("dtype"))
    result["nonnegative"] = bool(matrix.nnz == 0 or float(np.min(matrix.data)) >= -1.0e-15)
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    result["row_sum_max"] = float(np.max(row_sums)) if row_sums.size else 0.0
    result["substochastic"] = bool(result["row_sum_max"] <= 1.0 + row_sum_tolerance)
    result["nnz_match"] = int(matrix.nnz) == int(record.get("matrix_nnz", -1))
    result["reported_residual_pass"] = float(record.get("maximum_eigenpair_residual", float("inf"))) <= 1.0e-8
    try:
        grid = int(record["grid"])
        method_family = str(record["method_family"])
        seed = None if record.get("seed") is None else int(record["seed"])
        samples = int(record["samples_per_cell"])
        order = int(record["quadrature_order"])
        fingerprint = independent_sampling_fingerprint(method_family, grid, seed, samples, order)
        result["sampling_fingerprint_match"] = fingerprint == record.get("sampling_fingerprint") == schema.get("sampling_fingerprint")
        expected_rows, row_hits = independent_rows(grid, method_family, seed, samples, order)
        row_pass, row_checks = compare_rows(matrix, expected_rows, row_tolerance)
        result["source_row_boundary_hits"] = int(row_hits)
        result["source_rows_pass"] = row_pass
        result["source_row_checks"] = row_checks
    except (KeyError, ValueError, OverflowError, TypeError) as exc:
        result["rebuild_error"] = repr(exc)
        result["sampling_fingerprint_match"] = False
        result["source_rows_pass"] = False
    result["pass"] = bool(all(value for key, value in result.items() if key.endswith("_match") or key in {"matrix_exists", "schema_exists", "nonnegative", "substochastic", "nnz_match", "reported_residual_pass", "source_rows_pass"} if isinstance(value, bool)))
    return result


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    protocol_sha = sha256_file(args.protocol)
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    records = list(payload.get("records", []))
    if args.max_records is not None:
        records = records[: int(args.max_records)]
    expected = expected_configs(protocol)
    seen: set[str] = set()
    record_checks: list[dict[str, Any]] = []
    for record in records:
        identifier = str(record.get("config_id"))
        check = check_record(record, protocol_sha, float(args.row_value_tolerance), float(args.row_sum_tolerance))
        check["unique_id"] = identifier not in seen
        check["expected_config"] = identifier in expected or bool(args.smoke and identifier.startswith("r060_m"))
        if identifier in expected:
            exp = expected[identifier]
            check["metadata_match"] = all(record.get(key) == value for key, value in exp.items())
        elif args.smoke:
            check["metadata_match"] = (
                identifier.startswith("r060_m")
                and int(record.get("grid", 0)) > 1
                and str(record.get("method_family")) in {"sobol", "gauss"}
            )
        else:
            check["metadata_match"] = False
        seen.add(identifier)
        check["pass"] = bool(check.get("pass") and check["unique_id"] and check["expected_config"] and check["metadata_match"])
        record_checks.append(check)
    complete = len(records) == len(expected) and seen == set(expected)
    protocol_binding = payload.get("protocol_sha256") == protocol_sha
    frozen_config = bool(payload.get("frozen_configuration"))
    design_count = len(expected)
    stale_gate_text = "162" in " ".join(str(x) for x in protocol.get("gates", {}).get("G0_integrity", []))
    checks = {
        "protocol_binding": protocol_binding,
        "record_count_complete": complete,
        "design_expected_count": design_count,
        "design_count_is_210": design_count == 210,
        "protocol_gate_text_count_inconsistency": stale_gate_text and design_count == 210,
        "frozen_configuration_flag": frozen_config,
        "all_record_checks": all(bool(row.get("pass")) for row in record_checks) if record_checks else False,
    }
    pair_checks: list[dict[str, Any]] = []
    sobol_records: dict[tuple[int, int], dict[int, dict[str, Any]]] = {}
    for record in records:
        if str(record.get("method_family")) != "sobol":
            continue
        key = (int(record.get("grid", -1)), int(record.get("seed", -1)))
        sobol_records.setdefault(key, {})[int(record.get("samples_per_cell", -1))] = record
    for (grid, seed), pair in sorted(sobol_records.items()):
        r64 = pair.get(64)
        r256 = pair.get(256)
        if r64 is None or r256 is None:
            pair_checks.append({"grid": grid, "seed": seed, "present": False, "pass": bool(args.smoke)})
            continue
        f64 = r64.get("sampling_fingerprint", {})
        f256 = r256.get("sampling_fingerprint", {})
        passed = bool(
            f64.get("base_sha256") == f256.get("base_prefix64_sha256")
            and f64.get("base_prefix64_sha256") == f256.get("base_prefix64_sha256")
            and f64.get("shift_sha256") == f256.get("shift_sha256")
            and f64.get("shift_shape") == f256.get("shift_shape")
        )
        pair_checks.append({"grid": grid, "seed": seed, "present": True, "pass": passed})
    checks["sobol_pair_invariants"] = pair_checks
    checks["sobol_pair_invariants_pass"] = all(bool(row["pass"]) for row in pair_checks) if pair_checks else bool(args.smoke)
    all_pass = bool(protocol_binding and (complete or args.smoke) and checks["all_record_checks"] and checks["sobol_pair_invariants_pass"] and (frozen_config or args.smoke))
    output = {
        "run_id": "R060_OPERATOR_VARIANCE_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "input": project(args.input),
        "protocol": project(args.protocol),
        "protocol_sha256": protocol_sha,
        "checks": checks,
        "record_checks": record_checks,
        "all_checks_pass": all_pass,
        "scope": "Independent finite-resolution integrity check; does not alter R059 and does not test continuous-operator convergence.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": project(args.output), "records_checked": len(records), "design_expected_count": design_count, "all_checks_pass": all_pass, "protocol_gate_text_count_inconsistency": checks["protocol_gate_text_count_inconsistency"]}, indent=2))
    if not all_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
