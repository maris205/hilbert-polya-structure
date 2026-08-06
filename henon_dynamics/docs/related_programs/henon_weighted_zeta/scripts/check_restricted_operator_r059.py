#!/usr/bin/env python3
"""Independent integrity checker for the R059 restricted operators.

This checker deliberately does not import ``henon_zeta.restricted_operator`` or
the producer.  It reloads every persisted CSR matrix and independently rebuilds
a tiny Gauss/Sobol grid as a semantics smoke test.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix, load_npz
from scipy.stats import qmc


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "results" / "restricted_operator_r059.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "restricted_operator_r059_check.json"
DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R059_CERTIFIED_DOMAIN_PROTOCOL.json"
STATE_ORDER = ("--", "-+", "+-", "++")
BOUNDS = {
    "--": (-5.0 / 8.0, -1.0 / 3.0, -81.0 / 128.0, -5.0 / 16.0),
    "-+": (-5.0 / 8.0, -1.0 / 3.0, 5.0 / 16.0, 81.0 / 128.0),
    "+-": (1.0 / 3.0, 5.0 / 8.0, -81.0 / 128.0, -5.0 / 16.0),
    "++": (1.0 / 3.0, 5.0 / 8.0, 5.0 / 16.0, 81.0 / 128.0),
}

# These rows are fixed before production and cover the first, middle, and last
# local cell in every state block.  Rebuilding them independently catches a
# transposed matrix, a state-block offset error, and a y/x-index swap without
# having to reassemble every production row in the checker.
SOURCE_ROW_LOCAL_FRACTIONS = (0.0, 0.5, 1.0)
SOURCE_ROW_TOLERANCE = 2.0e-12
EXPECTED_INDEXING = (
    "global=state_index*m^2 + y_index*m + x_index; "
    "state order --,-+,+-,++; x index varies fastest"
)
EXPECTED_TARGET_SEMANTICS = (
    "strict h-set interior followed by half-open local cells; exact "
    "h-set/cell-boundary hits are counted and discarded"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--microgrid", type=int, default=4)
    parser.add_argument("--row-sum-tolerance", type=float, default=1.0e-12)
    parser.add_argument("--residual-tolerance", type=float, default=1.0e-8)
    return parser.parse_args()


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
    x = xl + (np.arange(m) + 0.5) * wx
    y = yl + (np.arange(m) + 0.5) * wy
    xx, yy = np.meshgrid(x, y, indexing="xy")
    return np.column_stack((xx.ravel(), yy.ravel())), wx, wy


def frozen_source_rows(m: int) -> np.ndarray:
    """Return the predeclared source rows used by the independent checker."""

    local_indices = sorted(
        {
            min(m * m - 1, max(0, int(round(fraction * (m * m - 1)))) )
            for fraction in SOURCE_ROW_LOCAL_FRACTIONS
        }
    )
    return np.asarray(
        [state_index * m * m + local for state_index in range(4) for local in local_indices],
        dtype=np.int64,
    )


def target_cells_independent(
    points: np.ndarray,
    m: int,
) -> tuple[np.ndarray, np.ndarray, int]:
    """Map points to strict target cells without importing the producer."""

    image_x = 1.0 - 6.0 * points[:, 0] ** 2 - points[:, 1]
    image_y = points[:, 0]
    target = np.full(points.shape[0], -1, dtype=np.int64)
    valid = np.zeros(points.shape[0], dtype=bool)
    boundary_hits = 0
    for state_index, state in enumerate(STATE_ORDER):
        xl, xu, yl, yu = BOUNDS[state]
        closed = (
            (image_x >= xl)
            & (image_x <= xu)
            & (image_y >= yl)
            & (image_y <= yu)
        )
        interior = (
            (image_x > xl)
            & (image_x < xu)
            & (image_y > yl)
            & (image_y < yu)
        )
        boundary_hits += int(np.count_nonzero(closed & ~interior))
        if not np.any(interior):
            continue
        wx = (xu - xl) / m
        wy = (yu - yl) / m
        positions = np.flatnonzero(interior)
        ux = (image_x[interior] - xl) / wx
        uy = (image_y[interior] - yl) / wy
        ix = np.floor(ux).astype(np.int64)
        iy = np.floor(uy).astype(np.int64)
        on_cell = (ux == np.floor(ux)) | (uy == np.floor(uy))
        boundary_hits += int(np.count_nonzero(on_cell))
        accepted = (
            ~on_cell
            & (ix >= 0)
            & (ix < m)
            & (iy >= 0)
            & (iy < m)
        )
        accepted_positions = positions[accepted]
        target[accepted_positions] = (
            state_index * m * m + iy[accepted] * m + ix[accepted]
        )
        valid[accepted_positions] = True
    return target, valid, boundary_hits


def independent_source_rows(
    m: int,
    method: str,
    seed: int | None,
    rows: np.ndarray,
    quadrature_order: int = 8,
    samples_per_cell: int = 64,
) -> tuple[dict[int, dict[int, float]], int]:
    """Rebuild selected CSR rows using an independent sampling implementation."""

    all_centers: list[np.ndarray] = []
    all_widths: list[np.ndarray] = []
    for state in STATE_ORDER:
        centers, wx, wy = cell_centers(state, m)
        all_centers.append(centers)
        all_widths.append(np.tile(np.asarray([wx, wy]), (centers.shape[0], 1)))
    source = np.concatenate(all_centers, axis=0)[rows]
    widths = np.concatenate(all_widths, axis=0)[rows]
    expected: dict[int, dict[int, float]] = {int(row): {} for row in rows}
    boundary_hits = 0

    if method == "gauss":
        nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)
        batches = [
            (np.asarray([xn, yn]), float(xw * yw / 4.0))
            for xn, xw in zip(nodes, weights)
            for yn, yw in zip(nodes, weights)
        ]
    else:
        if seed is None:
            raise ValueError("Sobol source-row rebuild requires a seed")
        if samples_per_cell < 1 or samples_per_cell & (samples_per_cell - 1):
            raise ValueError("samples_per_cell must be a positive power of two")
        exponent = int(round(math.log2(samples_per_cell)))
        sampler = qmc.Sobol(d=2, scramble=True, seed=int(seed))
        base_points = sampler.random_base2(exponent)
        # Reproduce the producer's per-source-cell shifts, then select the
        # frozen rows.  The full draw is intentional: drawing only selected
        # rows would change the RNG stream and silently alter the rule.
        full_shifts = np.random.default_rng(int(seed) + 1_000_003).random(
            (4 * m * m, 2)
        )
        shifts = full_shifts[rows]
        batches = [
            (np.mod(point + shifts, 1.0), 1.0 / samples_per_cell)
            for point in base_points
        ]

    for local_unit, weight in batches:
        if method == "gauss":
            points = source + 0.5 * widths * local_unit
        else:
            points = source + (local_unit - 0.5) * widths
        target, valid, hits = target_cells_independent(points, m)
        boundary_hits += hits
        for row, column in zip(rows[valid], target[valid]):
            row_map = expected[int(row)]
            key = int(column)
            row_map[key] = row_map.get(key, 0.0) + weight
    return expected, boundary_hits


def compare_source_rows(
    matrix: csr_matrix,
    expected: dict[int, dict[int, float]],
    tolerance: float = SOURCE_ROW_TOLERANCE,
) -> tuple[bool, list[dict[str, object]]]:
    """Compare persisted CSR rows with independently rebuilt row maps."""

    checks: list[dict[str, object]] = []
    all_pass = True
    for row_index in sorted(expected):
        sparse_row = matrix.getrow(int(row_index))
        actual = {
            int(column): float(value)
            for column, value in zip(sparse_row.indices, sparse_row.data)
        }
        wanted = expected[row_index]
        keys_match = set(actual) == set(wanted)
        values_match = keys_match and all(
            math.isclose(actual[column], wanted[column], rel_tol=tolerance, abs_tol=tolerance)
            for column in wanted
        )
        passed = bool(keys_match and values_match)
        all_pass = all_pass and passed
        checks.append(
            {
                "row": int(row_index),
                "expected_nnz": len(wanted),
                "observed_nnz": len(actual),
                "keys_match": keys_match,
                "values_match": values_match,
                "pass": passed,
            }
        )
    return all_pass, checks


def independent_samples(m: int, method: str, seed: int | None) -> tuple[np.ndarray, int]:
    centers = []
    widths = []
    for state in STATE_ORDER:
        grid, wx, wy = cell_centers(state, m)
        centers.append(grid)
        widths.append(np.tile(np.asarray([wx, wy]), (grid.shape[0], 1)))
    source = np.concatenate(centers, axis=0)
    width = np.concatenate(widths, axis=0)
    if method == "gauss":
        nodes, weights = np.polynomial.legendre.leggauss(8)
        batches = []
        for xn, xw in zip(nodes, weights):
            for yn, yw in zip(nodes, weights):
                # Use per-state widths rather than assuming a square h-set.
                batches.append((source + 0.5 * width * np.asarray([xn, yn]), float(xw * yw / 4.0)))
        return batches, 64
    if seed is None:
        raise ValueError("Sobol smoke test requires a seed")
    sampler = qmc.Sobol(d=2, scramble=True, seed=int(seed))
    base = sampler.random_base2(6)
    shifts = np.random.default_rng(int(seed) + 1_000_003).random((source.shape[0], 2))
    return [(source + (np.mod(point + shifts, 1.0) - 0.5) * width, 1.0 / 64.0) for point in base], 64


def independent_microgrid(m: int, method: str, seed: int | None) -> dict[str, object]:
    batches, samples_per_cell = independent_samples(m, method, seed)
    centers = []
    for state in STATE_ORDER:
        centers.append(cell_centers(state, m)[0])
    source = np.concatenate(centers, axis=0)
    n = source.shape[0]
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    boundary_hits = 0
    target_hits = 0
    for points, weight in batches:
        image_x = 1.0 - 6.0 * points[:, 0] ** 2 - points[:, 1]
        image_y = points[:, 0]
        for state_index, state in enumerate(STATE_ORDER):
            xl, xu, yl, yu = BOUNDS[state]
            interior = (
                (image_x > xl)
                & (image_x < xu)
                & (image_y > yl)
                & (image_y < yu)
            )
            closed = (
                (image_x >= xl)
                & (image_x <= xu)
                & (image_y >= yl)
                & (image_y <= yu)
            )
            boundary_hits += int(np.count_nonzero(closed & ~interior))
            if not np.any(interior):
                continue
            wx = (xu - xl) / m
            wy = (yu - yl) / m
            ux = (image_x[interior] - xl) / wx
            uy = (image_y[interior] - yl) / wy
            ix = np.floor(ux).astype(int)
            iy = np.floor(uy).astype(int)
            on_cell = (ux == np.floor(ux)) | (uy == np.floor(uy))
            boundary_hits += int(np.count_nonzero(on_cell))
            good = ~on_cell & (ix >= 0) & (ix < m) & (iy >= 0) & (iy < m)
            positions = np.flatnonzero(interior)[good]
            target = state_index * m * m + iy[good] * m + ix[good]
            rows.extend(positions.tolist())
            cols.extend(target.tolist())
            vals.extend([weight] * target.size)
            target_hits += int(target.size)
    matrix = csr_matrix((vals, (rows, cols)), shape=(n, n))
    matrix.sum_duplicates()
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    return {
        "method": method,
        "seed": seed,
        "m": m,
        "shape": list(matrix.shape),
        "nnz": int(matrix.nnz),
        "source_sample_count": int(n * samples_per_cell),
        "target_hit_count": target_hits,
        "boundary_hits": boundary_hits,
        "maximum_row_sum": float(np.max(row_sums, initial=0.0)),
        "nontrivial": bool(matrix.nnz > 0),
    }


def main() -> None:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    protocol_sha256 = sha256_file(args.protocol)
    records = payload.get("records", [])
    checks: dict[str, bool] = {}
    checks["protocol_binding"] = payload.get("protocol_sha256") == protocol_sha256
    record_checks = []
    seen = set()
    for record in records:
        identifier = str(record["config_id"])
        path = PROJECT_ROOT / record["matrix_path"]
        schema_path = PROJECT_ROOT / record["schema_path"]
        row: dict[str, object] = {"config_id": identifier}
        row["unique_id"] = identifier not in seen
        seen.add(identifier)
        row["matrix_exists"] = path.exists()
        row["schema_exists"] = schema_path.exists()
        actual_matrix_sha = sha256_file(path) if path.exists() else None
        actual_schema_sha = sha256_file(schema_path) if schema_path.exists() else None
        row["matrix_sha256"] = actual_matrix_sha == record.get("matrix_sha256")
        row["schema_sha256"] = actual_schema_sha == record.get("schema_sha256")
        schema = json.loads(schema_path.read_text(encoding="utf-8")) if schema_path.exists() else {}
        row["schema_matrix_binding"] = (
            schema.get("matrix_sha256") == actual_matrix_sha
            and schema.get("shape") == [int(record["state_count"])] * 2
            and schema.get("state_order") == list(STATE_ORDER)
        )
        expected_bounds = {
            "--": ["-5/8", "-1/3", "-81/128", "-5/16"],
            "-+": ["-5/8", "-1/3", "5/16", "81/128"],
            "+-": ["1/3", "5/8", "-81/128", "-5/16"],
            "++": ["1/3", "5/8", "5/16", "81/128"],
        }
        row["schema_semantics"] = bool(
            schema.get("schema_version") == 1
            and schema.get("run_id") == "R059_RESTRICTED_OPERATOR"
            and schema.get("config_id") == identifier
            and schema.get("protocol_sha256") == payload.get("protocol_sha256")
            and schema.get("state_order") == list(STATE_ORDER)
            and schema.get("hset_bounds_rational") == expected_bounds
            and schema.get("indexing") == EXPECTED_INDEXING
            and schema.get("target_semantics") == EXPECTED_TARGET_SEMANTICS
            and schema.get("matrix_format") == "scipy_csr_npz"
            and schema.get("matrix_path") == record.get("matrix_path")
            and schema.get("matrix_sha256") == record.get("matrix_sha256")
            and schema.get("grid") == int(record["grid"])
            and schema.get("method") == record.get("method")
            and schema.get("quadrature_order") == int(record.get("quadrature_order") or 0)
            and schema.get("samples_per_cell") == int(record.get("samples_per_cell") or 0)
            and schema.get("seed") == record.get("seed")
        )
        matrix = load_npz(path).tocsr() if path.exists() else csr_matrix((0, 0))
        row["shape"] = list(matrix.shape)
        row["shape_matches"] = list(matrix.shape) == [int(record["state_count"])] * 2
        row_sums = np.asarray(matrix.sum(axis=1)).ravel()
        row["finite_nonnegative"] = bool(np.all(np.isfinite(matrix.data)) and np.all(matrix.data >= -1.0e-14))
        row["substochastic"] = bool(
            np.max(row_sums, initial=0.0) <= 1.0 + args.row_sum_tolerance
        )
        row["nnz_matches"] = int(matrix.nnz) == int(record["matrix_nnz"])
        row["boundary_zero"] = int(record.get("target_boundary_hits", -1)) == 0
        row["residual_pass"] = float(record.get("maximum_eigenpair_residual", math.inf)) <= args.residual_tolerance
        source_row_indices = frozen_source_rows(int(record["grid"]))
        source_row_checks: list[dict[str, object]] = []
        source_row_boundary_hits = -1
        source_rows_match = False
        if path.exists():
            method = (
                "gauss"
                if str(record.get("method")) == "tensor_gauss_legendre"
                else "sobol"
            )
            try:
                expected_rows, source_row_boundary_hits = independent_source_rows(
                    int(record["grid"]),
                    method,
                    None if method == "gauss" else int(record["seed"]),
                    source_row_indices,
                    quadrature_order=int(record.get("quadrature_order") or 8),
                    samples_per_cell=int(record.get("samples_per_cell") or 64),
                )
                source_rows_match, source_row_checks = compare_source_rows(
                    matrix, expected_rows
                )
            except (KeyError, TypeError, ValueError):
                source_row_checks = []
        row["source_row_indices"] = source_row_indices.tolist()
        row["source_row_boundary_hits"] = source_row_boundary_hits
        row["source_rows_match"] = source_rows_match
        row["source_row_checks"] = source_row_checks
        row["config_pass"] = all(
            bool(row[key])
            for key in (
                "unique_id",
                "matrix_exists",
                "schema_exists",
                "matrix_sha256",
                "schema_sha256",
                "schema_matrix_binding",
                "schema_semantics",
                "shape_matches",
                "finite_nonnegative",
                "substochastic",
                "nnz_matches",
                "boundary_zero",
                "source_rows_match",
                "residual_pass",
            )
        )
        row["config_pass"] = bool(
            row["config_pass"] and row["source_row_boundary_hits"] == 0
        )
        record_checks.append(row)

    microgrid = {
        "gauss": independent_microgrid(args.microgrid, "gauss", None),
        "sobol_seed20260801": independent_microgrid(args.microgrid, "sobol", 20260801),
        "sobol_seed20260802": independent_microgrid(args.microgrid, "sobol", 20260802),
    }
    microgrid_checks = {
        key: bool(
            value["nontrivial"]
            and value["boundary_hits"] == 0
            and value["maximum_row_sum"] <= 1.0 + args.row_sum_tolerance
        )
        for key, value in microgrid.items()
    }
    checks["record_count"] = len(records) == 18
    checks["all_record_checks"] = all(bool(row["config_pass"]) for row in record_checks)
    checks["microgrid_checks"] = all(microgrid_checks.values())
    checks["producer_g3"] = bool(payload.get("decisions", {}).get("g3_operator_integrity_pass", False))
    checks["all_checks_pass"] = all(checks.values())
    output = {
        "run_id": "R059_RESTRICTED_OPERATOR_INDEPENDENT_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "input": project(args.input),
        "input_sha256": sha256_file(args.input),
        "protocol": project(args.protocol),
        "protocol_sha256": protocol_sha256,
        "record_checks": record_checks,
        "frozen_source_row_rule": {
            "local_fractions": list(SOURCE_ROW_LOCAL_FRACTIONS),
            "value_tolerance": SOURCE_ROW_TOLERANCE,
            "description": "first, middle, and last local cell in each state block",
        },
        "microgrid": microgrid,
        "microgrid_checks": microgrid_checks,
        "checks": checks,
        "status": "PASS" if checks["all_checks_pass"] else "FAIL",
        "scope": "Sparse matrix/schema integrity and independent small-grid semantics smoke test; not operator convergence.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": project(args.output), "status": output["status"], "checks": checks}, indent=2))
    if not checks["all_checks_pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
