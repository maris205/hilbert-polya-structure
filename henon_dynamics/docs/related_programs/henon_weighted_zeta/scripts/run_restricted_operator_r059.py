#!/usr/bin/env python3
"""Produce the frozen R059 finite-volume operators on four separate h-sets."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from scipy.sparse import save_npz


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.restricted_operator import (  # noqa: E402
    HSET_BOUNDS_RATIONAL,
    STATE_ORDER,
    assemble_restricted_gauss,
    assemble_restricted_sobol,
    restricted_spectrum,
)


DEFAULT_PROTOCOL = (
    PROJECT_ROOT / "research" / "refine-logs" / "R059_CERTIFIED_DOMAIN_PROTOCOL.json"
)
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "restricted_operator_r059.json"
DEFAULT_CSV = PROJECT_ROOT / "results" / "restricted_operator_r059.csv"
DEFAULT_MATRIX_DIR = PROJECT_ROOT / "results" / "restricted_operator_r059_matrices"
DEFAULT_CYCLE_RESULT = PROJECT_ROOT / "results" / "certified_domain_r059.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--grid", nargs="+", type=int, default=[24, 32, 48, 64, 96, 128])
    parser.add_argument(
        "--method",
        nargs="+",
        choices=["gauss", "sobol"],
        default=["gauss", "sobol"],
    )
    parser.add_argument("--quadrature-order", type=int, default=8)
    parser.add_argument("--samples-per-cell", type=int, default=64)
    parser.add_argument("--seed", nargs="+", type=int, default=[20260801, 20260802])
    parser.add_argument("--eigenvalue-count", type=int, default=8)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--matrix-dir", type=Path, default=DEFAULT_MATRIX_DIR)
    parser.add_argument("--cycle-result", type=Path, default=DEFAULT_CYCLE_RESULT)
    parser.add_argument("--fredholm-reference", type=float)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def portable(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def complex_modulus(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return abs(float(value))
    if isinstance(value, list) and len(value) == 2:
        return abs(complex(float(value[0]), float(value[1])))
    return None


def load_fredholm_reference(args: argparse.Namespace) -> tuple[float | None, str | None]:
    if args.fredholm_reference is not None:
        return abs(float(args.fredholm_reference)), "command_line"
    if not args.cycle_result.exists():
        return None, None
    payload = json.loads(args.cycle_result.read_text(encoding="utf-8"))
    cutoffs = payload.get("cycle_cutoffs", [])
    if not cutoffs:
        return None, portable(args.cycle_result)
    return complex_modulus(cutoffs[-1].get("fredholm_resonance")), portable(args.cycle_result)


def config_id(config: dict[str, Any]) -> str:
    m = int(config["grid"])
    if config["method"] == "gauss":
        return f"r059_m{m:03d}_gauss_q{int(config['quadrature_order'])}"
    return (
        f"r059_m{m:03d}_sobol{int(config['samples_per_cell'])}"
        f"_seed{int(config['seed'])}"
    )


def run_config(config: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    if config["method"] == "gauss":
        assembly = assemble_restricted_gauss(
            a=6.0,
            cells_per_axis=int(config["grid"]),
            quadrature_order=int(config["quadrature_order"]),
        )
    else:
        assembly = assemble_restricted_sobol(
            a=6.0,
            cells_per_axis=int(config["grid"]),
            samples_per_cell=int(config["samples_per_cell"]),
            seed=int(config["seed"]),
        )
    assembly_seconds = time.perf_counter() - started
    started = time.perf_counter()
    spectrum = restricted_spectrum(
        assembly.matrix, eigenvalue_count=int(config["eigenvalue_count"])
    )
    spectrum_seconds = time.perf_counter() - started

    matrix_dir = Path(config["matrix_dir"])
    matrix_dir.mkdir(parents=True, exist_ok=True)
    identifier = config_id(config)
    matrix_path = matrix_dir / f"{identifier}.npz"
    schema_path = matrix_dir / f"{identifier}.schema.json"
    save_npz(matrix_path, assembly.matrix, compressed=True)
    matrix_sha256 = sha256_file(matrix_path)

    row_sums = assembly.row_sums
    maximum_row_sum = float(np.max(row_sums, initial=0.0))
    # ``initial=0`` would be treated as an additional candidate by NumPy and
    # would therefore force this diagnostic to zero for every nonnegative
    # substochastic matrix.  The matrix always has one row per h-set cell, so
    # the ordinary reduction is the intended minimum.
    minimum_row_sum = float(np.min(row_sums)) if row_sums.size else 0.0
    nontrivial = bool(assembly.matrix.nnz > 0 and maximum_row_sum > 0.0)
    substochastic = maximum_row_sum <= 1.0 + float(config["row_sum_tolerance"])
    residual_pass = float(spectrum["maximum_residual"]) <= float(
        config["maximum_eigenpair_residual"]
    )
    boundary_pass = assembly.boundary_hits == 0
    schema = {
        "schema_version": 1,
        "run_id": "R059_RESTRICTED_OPERATOR",
        "config_id": identifier,
        "protocol_sha256": config["protocol_sha256"],
        "map": "H_6(x,y)=(1-6*x^2-y,x)",
        "state_order": list(STATE_ORDER),
        "hset_bounds_rational": {
            state: list(HSET_BOUNDS_RATIONAL[state]) for state in STATE_ORDER
        },
        "indexing": (
            "global=state_index*m^2 + y_index*m + x_index; "
            "state order --,-+,+-,++; x index varies fastest"
        ),
        "target_semantics": (
            "strict h-set interior followed by half-open local cells; exact "
            "h-set/cell-boundary hits are counted and discarded"
        ),
        "matrix_path": portable(matrix_path),
        "matrix_sha256": matrix_sha256,
        "matrix_format": "scipy_csr_npz",
        "shape": list(assembly.matrix.shape),
        "dtype": str(assembly.matrix.dtype),
        "nnz": int(assembly.matrix.nnz),
        "grid": int(config["grid"]),
        "method": assembly.method,
        "quadrature_order": assembly.quadrature_order,
        "samples_per_cell": assembly.samples_per_cell,
        "seed": assembly.seed,
    }
    schema_path.write_text(
        json.dumps(schema, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    schema_sha256 = sha256_file(schema_path)
    return {
        "config_id": identifier,
        "a": 6.0,
        "grid": int(config["grid"]),
        "state_count": int(assembly.matrix.shape[0]),
        "method": assembly.method,
        "method_key": (
            "gauss"
            if assembly.method == "tensor_gauss_legendre"
            else f"sobol_seed{assembly.seed}"
        ),
        "quadrature_order": assembly.quadrature_order,
        "samples_per_cell": assembly.samples_per_cell,
        "seed": assembly.seed,
        "matrix_path": portable(matrix_path),
        "matrix_sha256": matrix_sha256,
        "schema_path": portable(schema_path),
        "schema_sha256": schema_sha256,
        "matrix_nnz": int(assembly.matrix.nnz),
        "minimum_row_sum": minimum_row_sum,
        "maximum_row_sum": maximum_row_sum,
        "mean_row_sum": float(np.mean(row_sums)),
        "zero_row_fraction": float(np.mean(row_sums == 0.0)),
        "leaky_row_fraction": float(np.mean(row_sums < 1.0 - 1.0e-12)),
        "source_sample_count": assembly.source_sample_count,
        "target_hit_count": assembly.target_hit_count,
        "target_hit_fraction": assembly.target_hit_count / assembly.source_sample_count,
        "target_boundary_hits": assembly.boundary_hits,
        "target_hset_boundary_hits": assembly.hset_boundary_hits,
        "target_cell_boundary_hits": assembly.cell_boundary_hits,
        "leading_eigenvalue": spectrum["leading_eigenvalue"],
        "leading_modulus": spectrum["leading_modulus"],
        "maximum_eigenpair_residual": spectrum["maximum_residual"],
        "eigenpairs": spectrum["eigenpairs"],
        "assembly_seconds": assembly_seconds,
        "spectrum_seconds": spectrum_seconds,
        "nontrivial_pass": nontrivial,
        "substochastic_pass": substochastic,
        "boundary_pass": boundary_pass,
        "residual_pass": residual_pass,
        "g3_config_pass": bool(nontrivial and substochastic and boundary_pass and residual_pass),
    }


def relative_gap(first: float, second: float) -> float:
    return abs(first - second) / max(abs(first), abs(second), np.finfo(float).tiny)


def finite_resolution_audit(
    records: list[dict[str, Any]],
    protocol: dict[str, Any],
    fredholm_reference: float | None,
    fredholm_source: str | None,
) -> dict[str, Any]:
    by_key = {(row["method_key"], int(row["grid"])): row for row in records}
    # The production gate is about the frozen Cartesian product, not merely
    # the number of rows.  A duplicated seed/configuration must not count as a
    # complete 18-configuration run.
    expected_grids = tuple(
        int(value) for value in protocol["operator_block"]["cells_per_hset_axis"]
    )
    expected_method_keys = ["gauss"]
    for method in protocol["operator_block"]["methods"]:
        if method["name"] == "random_shift_sobol":
            expected_method_keys.append(f"sobol_seed{int(method['seed'])}")
    method_keys = expected_method_keys
    expected_keys = {
        (method, grid) for method in method_keys for grid in expected_grids
    }
    actual_keys = set(by_key)
    cross_method_rows = []
    spread_limit = float(
        protocol["operator_block"]["finest_cross_method_relative_spread_max"]
    )
    for grid in (96, 128):
        values = [
            float(by_key[(method, grid)]["leading_modulus"])
            for method in method_keys
            if (method, grid) in by_key
        ]
        spread = (
            None
            if len(values) != len(method_keys)
            else (max(values) - min(values))
            / max(float(np.median(values)), np.finfo(float).tiny)
        )
        cross_method_rows.append(
            {
                "grid": grid,
                "values": values,
                "relative_spread": spread,
                "pass": spread is not None and spread <= spread_limit,
            }
        )

    cross_chain_rows = []
    cross_chain_limit = float(
        protocol["operator_block"]["finest_cross_chain_relative_gap_max"]
    )
    for method in method_keys:
        if (method, 96) in by_key and (method, 128) in by_key:
            value96 = float(by_key[(method, 96)]["leading_modulus"])
            value128 = float(by_key[(method, 128)]["leading_modulus"])
            gap = relative_gap(value96, value128)
        else:
            value96 = value128 = gap = None
        cross_chain_rows.append(
            {
                "method_key": method,
                "m96": value96,
                "m128": value128,
                "relative_gap": gap,
                "pass": gap is not None and gap <= cross_chain_limit,
            }
        )

    dyadic_rows = []
    for method in method_keys:
        for chain in ((24, 48, 96), (32, 64, 128)):
            if all((method, grid) in by_key for grid in chain):
                values = [float(by_key[(method, grid)]["leading_modulus"]) for grid in chain]
                first_change = relative_gap(values[0], values[1])
                final_change = relative_gap(values[1], values[2])
            else:
                values = []
                first_change = final_change = None
            dyadic_rows.append(
                {
                    "method_key": method,
                    "chain": list(chain),
                    "values": values,
                    "first_relative_change": first_change,
                    "final_relative_change": final_change,
                    "pass": (
                        first_change is not None
                        and final_change is not None
                        and final_change <= first_change
                    ),
                }
            )

    cycle_rows = []
    if fredholm_reference is not None:
        for method in method_keys:
            for grid in (96, 128):
                if (method, grid) not in by_key:
                    continue
                value = float(by_key[(method, grid)]["leading_modulus"])
                cycle_rows.append(
                    {
                        "method_key": method,
                        "grid": grid,
                        "leading_modulus": value,
                        "fredholm_reference": fredholm_reference,
                        "relative_gap": abs(value - fredholm_reference)
                        / max(abs(fredholm_reference), np.finfo(float).tiny),
                    }
                )
    gaps = [float(row["relative_gap"]) for row in cycle_rows]
    median_gap = None if not gaps else float(np.median(gaps))
    maximum_gap = None if not gaps else float(np.max(gaps))
    median_limit = float(
        protocol["operator_block"]["finest_cycle_operator_median_relative_gap_max"]
    )
    maximum_limit = float(
        protocol["operator_block"]["finest_cycle_operator_max_relative_gap_max"]
    )
    cycle_pass = bool(
        len(gaps) == 6
        and median_gap is not None
        and maximum_gap is not None
        and median_gap <= median_limit
        and maximum_gap <= maximum_limit
    )
    complete = len(records) == len(expected_keys) and actual_keys == expected_keys
    return {
        "definitions": {
            "relative_gap": "abs(a-b)/max(abs(a),abs(b))",
            "cross_method_relative_spread": "(max-min)/median",
            "cycle_relative_gap": "abs(lambda-rho_F)/abs(rho_F)",
        },
        "fredholm_reference": fredholm_reference,
        "fredholm_source": fredholm_source,
        "cross_method": cross_method_rows,
        "cross_chain": cross_chain_rows,
        "dyadic_change": dyadic_rows,
        "cycle_operator": {
            "rows": cycle_rows,
            "median_relative_gap": median_gap,
            "maximum_relative_gap": maximum_gap,
            "pass": cycle_pass,
        },
        "all_18_configs_present": complete,
        "expected_config_keys": sorted(
            [[method, grid] for method, grid in expected_keys]
        ),
        "observed_config_keys": sorted(
            [[method, grid] for method, grid in actual_keys]
        ),
        "cross_method_pass": all(row["pass"] for row in cross_method_rows),
        "cross_chain_pass": all(row["pass"] for row in cross_chain_rows),
        "dyadic_change_pass": all(row["pass"] for row in dyadic_rows),
        "cycle_operator_pass": cycle_pass,
        "g4_pass": bool(
            complete
            and all(row["pass"] for row in cross_method_rows)
            and all(row["pass"] for row in cross_chain_rows)
            and all(row["pass"] for row in dyadic_rows)
            and cycle_pass
        ),
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    operator_block = protocol["operator_block"]
    expected_grids = [int(value) for value in operator_block["cells_per_hset_axis"]]
    expected_gauss_order = next(
        int(method["quadrature_order"])
        for method in operator_block["methods"]
        if method["name"] == "tensor_gauss_legendre"
    )
    expected_sobol_samples = next(
        int(method["samples_per_cell"])
        for method in operator_block["methods"]
        if method["name"] == "random_shift_sobol"
    )
    expected_seeds = sorted(
        int(method["seed"])
        for method in operator_block["methods"]
        if method["name"] == "random_shift_sobol"
    )
    frozen_configuration = bool(
        sorted(args.grid) == sorted(expected_grids)
        and set(args.method) == {"gauss", "sobol"}
        and int(args.quadrature_order) == expected_gauss_order
        and int(args.samples_per_cell) == expected_sobol_samples
        and sorted(int(seed) for seed in args.seed) == expected_seeds
        and int(args.eigenvalue_count)
        == int(operator_block["eigenvalue_count"])
    )
    protocol_sha256 = sha256_file(args.protocol)
    configs: list[dict[str, Any]] = []
    common = {
        "quadrature_order": args.quadrature_order,
        "samples_per_cell": args.samples_per_cell,
        "eigenvalue_count": args.eigenvalue_count,
        "matrix_dir": str(args.matrix_dir.resolve()),
        "protocol_sha256": protocol_sha256,
        "maximum_eigenpair_residual": operator_block["maximum_eigenpair_residual"],
        "row_sum_tolerance": operator_block["maximum_row_sum_tolerance"],
    }
    for grid in args.grid:
        if "gauss" in args.method:
            configs.append({**common, "grid": grid, "method": "gauss", "seed": None})
        if "sobol" in args.method:
            for seed in args.seed:
                configs.append({**common, "grid": grid, "method": "sobol", "seed": seed})

    records: list[dict[str, Any]] = []
    if args.workers <= 1:
        for index, config in enumerate(configs, start=1):
            record = run_config(config)
            records.append(record)
            print(
                f"[restricted-operator] {index}/{len(configs)} {record['config_id']} "
                f"lambda={record['leading_modulus']:.12g}",
                flush=True,
            )
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(run_config, config): config for config in configs}
            complete = 0
            for future in as_completed(futures):
                record = future.result()
                records.append(record)
                complete += 1
                print(
                    f"[restricted-operator] {complete}/{len(configs)} "
                    f"{record['config_id']} lambda={record['leading_modulus']:.12g}",
                    flush=True,
                )
    records.sort(key=lambda row: (int(row["grid"]), str(row["method_key"])))
    fredholm_reference, fredholm_source = load_fredholm_reference(args)
    finite_resolution = finite_resolution_audit(
        records, protocol, fredholm_reference, fredholm_source
    )
    g3 = bool(
        frozen_configuration
        and len(records) == 18
        and finite_resolution["all_18_configs_present"]
        and all(row["g3_config_pass"] for row in records)
    )
    payload = {
        "run_id": "R059_RESTRICTED_OPERATOR",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable(args.protocol),
        "protocol_sha256": protocol_sha256,
        "frozen_configuration": frozen_configuration,
        "state_order": list(STATE_ORDER),
        "hset_bounds_rational": {
            state: list(HSET_BOUNDS_RATIONAL[state]) for state in STATE_ORDER
        },
        "indexing": (
            "global=state_index*m^2 + y_index*m + x_index; state-major, "
            "x index fastest"
        ),
        "records": records,
        "finite_resolution_audit": finite_resolution,
        "decisions": {
            "g3_operator_integrity_pass": g3,
            "g4_finite_resolution_consistency_pass": finite_resolution["g4_pass"],
            "all_operator_gates_pass": bool(g3 and finite_resolution["g4_pass"]),
        },
        "scope": (
            "Finite-volume open operator on the explicit four-h-set union. "
            "A pass is finite-resolution consistency, not continuous operator convergence."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    flat_rows = [
        {key: value for key, value in row.items() if key != "eigenpairs"}
        for row in records
    ]
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(flat_rows[0]))
        writer.writeheader()
        writer.writerows(flat_rows)
    print(
        json.dumps(
            {
                "output": portable(args.output),
                "csv": portable(args.csv),
                "configurations": len(records),
                "g3": g3,
                "g4": finite_resolution["g4_pass"],
            },
            indent=2,
        )
    )
    if not g3:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
