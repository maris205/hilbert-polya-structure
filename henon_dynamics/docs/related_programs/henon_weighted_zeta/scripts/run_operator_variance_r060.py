#!/usr/bin/env python3
"""Produce the frozen R060 finite-resolution variance/control ensemble.

R060 is deliberately separate from the frozen R059 production.  The producer
uses the R059 four-h-set assembly rules, but writes to an R060-only directory
and never edits an R059 artifact.  The 210 frozen configurations are

    6 grids * (16 Sobol seeds * 2 sample budgets + 3 Gauss orders).

The Sobol fingerprints make the fixed-(grid, seed) 64/256 prefix pairing
auditable without serialising the full point clouds.
"""

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
from scipy.stats import qmc


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


DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R060_OPERATOR_VARIANCE_PROTOCOL.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "operator_variance_r060.json"
DEFAULT_SUMMARY = PROJECT_ROOT / "results" / "operator_variance_r060_summary.json"
DEFAULT_CSV = PROJECT_ROOT / "results" / "operator_variance_r060.csv"
DEFAULT_MATRIX_DIR = PROJECT_ROOT / "results" / "operator_variance_r060_matrices"
DEFAULT_FREDHOLM = PROJECT_ROOT / "results" / "certified_domain_r059.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--grid", nargs="+", type=int)
    parser.add_argument("--seed", nargs="+", type=int)
    parser.add_argument("--sobol-samples", nargs="+", type=int)
    parser.add_argument("--gauss-order", nargs="+", type=int)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--matrix-dir", type=Path, default=DEFAULT_MATRIX_DIR)
    parser.add_argument("--fredholm", type=Path, default=DEFAULT_FREDHOLM)
    parser.add_argument("--smoke", action="store_true", help="run a tiny non-frozen smoke configuration")
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def relative_gap(first: float, second: float) -> float:
    return abs(float(first) - float(second)) / max(
        abs(float(first)), abs(float(second)), np.finfo(float).tiny
    )


def config_id(config: dict[str, Any]) -> str:
    grid = int(config["grid"])
    if config["method"] == "gauss":
        return f"r060_m{grid:03d}_gauss_q{int(config['quadrature_order'])}"
    return f"r060_m{grid:03d}_sobol{int(config['samples_per_cell'])}_seed{int(config['seed'])}"


def sampling_fingerprint(
    method: str,
    grid: int,
    seed: int | None,
    samples_per_cell: int,
    quadrature_order: int,
) -> dict[str, Any]:
    """Return hashes for the deterministic sampling rule used by a config."""

    if method == "sobol":
        if seed is None:
            raise ValueError("Sobol fingerprint requires a seed")
        if samples_per_cell < 1 or samples_per_cell & (samples_per_cell - 1):
            raise ValueError("Sobol samples must be a positive power of two")
        exponent = int(round(math.log2(samples_per_cell)))
        sampler = qmc.Sobol(d=2, scramble=True, seed=int(seed))
        base = np.ascontiguousarray(sampler.random_base2(exponent), dtype=np.float64)
        shifts = np.ascontiguousarray(
            np.random.default_rng(int(seed) + 1_000_003).random((4 * grid * grid, 2)),
            dtype=np.float64,
        )
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


def fredholm_reference(path: Path) -> tuple[float | None, str | None]:
    if not path.exists():
        return None, None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        cutoffs = payload.get("cycle_cutoffs", [])
        if not cutoffs:
            return None, portable(path)
        value = complex_modulus(cutoffs[-1].get("fredholm_resonance"))
        return value, portable(path)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return None, portable(path)


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
    matrix_sha = sha256_file(matrix_path)
    fingerprint = sampling_fingerprint(
        str(config["method"]),
        int(config["grid"]),
        None if config.get("seed") is None else int(config["seed"]),
        int(config["samples_per_cell"]),
        int(config["quadrature_order"]),
    )
    row_sums = np.asarray(assembly.row_sums, dtype=float)
    maximum_row_sum = float(np.max(row_sums)) if row_sums.size else 0.0
    minimum_row_sum = float(np.min(row_sums)) if row_sums.size else 0.0
    record = {
        "config_id": identifier,
        "run_id": "R060_OPERATOR_VARIANCE",
        "a": 6.0,
        "grid": int(config["grid"]),
        "state_count": int(assembly.matrix.shape[0]),
        "method": assembly.method,
        "method_key": "gauss" if config["method"] == "gauss" else f"sobol_seed{int(config['seed'])}",
        "method_family": str(config["method"]),
        "quadrature_order": int(assembly.quadrature_order),
        "samples_per_cell": int(assembly.samples_per_cell),
        "seed": assembly.seed,
        "matrix_path": portable(matrix_path),
        "matrix_sha256": matrix_sha,
        "schema_path": portable(schema_path),
        "matrix_shape": list(assembly.matrix.shape),
        "matrix_nnz": int(assembly.matrix.nnz),
        "minimum_row_sum": minimum_row_sum,
        "maximum_row_sum": maximum_row_sum,
        "mean_row_sum": float(np.mean(row_sums)) if row_sums.size else 0.0,
        "zero_row_fraction": float(np.mean(row_sums == 0.0)) if row_sums.size else 0.0,
        "leaky_row_fraction": float(np.mean(row_sums < 1.0 - 1.0e-12)) if row_sums.size else 0.0,
        "source_sample_count": int(assembly.source_sample_count),
        "target_hit_count": int(assembly.target_hit_count),
        "target_hit_fraction": float(assembly.target_hit_count / assembly.source_sample_count)
        if assembly.source_sample_count
        else 0.0,
        "target_boundary_hits": int(assembly.boundary_hits),
        "target_hset_boundary_hits": int(assembly.hset_boundary_hits),
        "target_cell_boundary_hits": int(assembly.cell_boundary_hits),
        "leading_eigenvalue": spectrum["leading_eigenvalue"],
        "leading_modulus": float(spectrum["leading_modulus"]),
        "maximum_eigenpair_residual": float(spectrum["maximum_residual"]),
        "eigenpairs": spectrum["eigenpairs"],
        "sampling_fingerprint": fingerprint,
        "assembly_seconds": assembly_seconds,
        "spectrum_seconds": spectrum_seconds,
        "nontrivial_pass": bool(assembly.matrix.nnz > 0 and maximum_row_sum > 0.0),
        "substochastic_pass": bool(maximum_row_sum <= 1.0 + float(config["row_sum_tolerance"])),
        "boundary_pass": bool(assembly.boundary_hits == 0),
        "residual_pass": bool(float(spectrum["maximum_residual"]) <= float(config["residual_tolerance"])),
    }
    record["g0_config_pass"] = bool(
        record["nontrivial_pass"]
        and record["substochastic_pass"]
        and record["boundary_pass"]
        and record["residual_pass"]
    )
    schema = {
        "schema_version": 1,
        "run_id": "R060_OPERATOR_VARIANCE",
        "config_id": identifier,
        "protocol_sha256": str(config["protocol_sha256"]),
        "map": "H_6(x,y)=(1-6*x^2-y,x)",
        "state_order": list(STATE_ORDER),
        "hset_bounds_rational": {state: list(HSET_BOUNDS_RATIONAL[state]) for state in STATE_ORDER},
        "indexing": "global=state_index*m^2 + y_index*m + x_index; state-major, x index fastest",
        "target_semantics": "strict h-set interior followed by half-open local cells; exact h-set/cell-boundary hits are counted and discarded",
        "matrix_path": portable(matrix_path),
        "matrix_sha256": matrix_sha,
        "matrix_format": "scipy_csr_npz",
        "shape": list(assembly.matrix.shape),
        "dtype": str(assembly.matrix.dtype),
        "grid": int(config["grid"]),
        "method": assembly.method,
        "method_family": str(config["method"]),
        "quadrature_order": int(config["quadrature_order"]),
        "samples_per_cell": int(config["samples_per_cell"]),
        "seed": assembly.seed,
        "sampling_fingerprint": fingerprint,
    }
    schema_path.write_text(json.dumps(schema, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    record["schema_sha256"] = sha256_file(schema_path)
    return record


def expected_configs(protocol: dict[str, Any]) -> list[dict[str, Any]]:
    design = protocol["design"]
    configs: list[dict[str, Any]] = []
    for grid in design["grids"]:
        for samples in design["sobol_samples_per_cell"]:
            for seed in design["fresh_sobol_seeds"]:
                configs.append({"grid": int(grid), "method": "sobol", "samples_per_cell": int(samples), "quadrature_order": 0, "seed": int(seed)})
        for order in design["gauss_orders"]:
            configs.append({"grid": int(grid), "method": "gauss", "samples_per_cell": int(order) ** 2, "quadrature_order": int(order), "seed": None})
    return configs


def percentile_bootstrap(values: list[float], seed: int, reps: int) -> list[float] | None:
    if not values:
        return None
    array = np.asarray(values, dtype=float)
    if array.size == 1:
        return [float(array[0]), float(array[0])]
    rng = np.random.default_rng(seed)
    sample = rng.choice(array, size=(int(reps), array.size), replace=True)
    means = np.mean(sample, axis=1)
    return [float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))]


def mean_mad_sd(values: list[float]) -> dict[str, Any]:
    if not values:
        return {"n": 0, "mean": None, "median": None, "sd": None, "mad": None}
    array = np.asarray(values, dtype=float)
    median = float(np.median(array))
    return {
        "n": int(array.size),
        "mean": float(np.mean(array)),
        "median": median,
        "sd": float(np.std(array, ddof=1)) if array.size > 1 else 0.0,
        "mad": float(np.median(np.abs(array - median))),
    }


def build_summary(records: list[dict[str, Any]], protocol: dict[str, Any], fredholm: Path) -> dict[str, Any]:
    by_key = {(str(row["method_family"]), int(row["grid"]), int(row["samples_per_cell"]), row.get("seed"), int(row["quadrature_order"])): row for row in records}
    sobol = [row for row in records if row["method_family"] == "sobol"]
    gauss = [row for row in records if row["method_family"] == "gauss"]
    bootstrap_seed = int(protocol["analysis"]["bootstrap_seed"])
    bootstrap_reps = int(protocol["analysis"]["bootstrap_replicates"])
    ensemble: list[dict[str, Any]] = []
    for grid in protocol["design"]["grids"]:
        for samples in protocol["design"]["sobol_samples_per_cell"]:
            values = [float(row["leading_modulus"]) for row in sobol if int(row["grid"]) == int(grid) and int(row["samples_per_cell"]) == int(samples)]
            stats = mean_mad_sd(values)
            stats.update({"method": "sobol", "grid": int(grid), "samples_per_cell": int(samples), "mean_bootstrap_ci": percentile_bootstrap(values, bootstrap_seed + int(grid) + int(samples), bootstrap_reps)})
            ensemble.append(stats)
    gauss_summary: list[dict[str, Any]] = []
    for grid in protocol["design"]["grids"]:
        for order in protocol["design"]["gauss_orders"]:
            values = [float(row["leading_modulus"]) for row in gauss if int(row["grid"]) == int(grid) and int(row["quadrature_order"]) == int(order)]
            stats = mean_mad_sd(values)
            stats.update({"method": "gauss", "grid": int(grid), "quadrature_order": int(order)})
            gauss_summary.append(stats)

    paired: list[dict[str, Any]] = []
    seeds = [int(value) for value in protocol["design"]["fresh_sobol_seeds"]]
    for grid in protocol["design"]["grids"]:
        shifts: list[float] = []
        for seed in seeds:
            r64 = next((r for r in sobol if int(r["grid"]) == int(grid) and int(r["samples_per_cell"]) == 64 and int(r["seed"]) == seed), None)
            r256 = next((r for r in sobol if int(r["grid"]) == int(grid) and int(r["samples_per_cell"]) == 256 and int(r["seed"]) == seed), None)
            if r64 is not None and r256 is not None:
                shifts.append(relative_gap(float(r64["leading_modulus"]), float(r256["leading_modulus"])))
        paired_stats = mean_mad_sd(shifts)
        paired_stats.update({"grid": int(grid), "relative_shift_256_vs_64": paired_stats.pop("mean"), "relative_shift_values": shifts})
        paired.append(paired_stats)

    dyadic: list[dict[str, Any]] = []
    for samples in protocol["design"]["sobol_samples_per_cell"]:
        for seed in seeds:
            for chain in protocol["design"]["dyadic_chains"]:
                values = []
                for grid in chain:
                    row = next((r for r in sobol if int(r["grid"]) == int(grid) and int(r["samples_per_cell"]) == int(samples) and int(r["seed"]) == seed), None)
                    if row is not None:
                        values.append(float(row["leading_modulus"]))
                first = relative_gap(values[0], values[1]) if len(values) == 3 else None
                final = relative_gap(values[1], values[2]) if len(values) == 3 else None
                dyadic.append({"samples_per_cell": int(samples), "seed": seed, "chain": list(chain), "values": values, "first_relative_change": first, "final_relative_change": final, "D": None if first is None or final is None else final - first, "pass_fraction_indicator": None if first is None or final is None else bool(final <= first)})

    reference, reference_source = fredholm_reference(fredholm)
    fredholm_rows: list[dict[str, Any]] = []
    if reference is not None:
        for row in sobol:
            if int(row["samples_per_cell"]) != 256 or int(row["grid"]) not in (96, 128):
                continue
            fredholm_rows.append({"grid": int(row["grid"]), "seed": int(row["seed"]), "leading_modulus": float(row["leading_modulus"]), "fredholm_reference": reference, "relative_gap": relative_gap(float(row["leading_modulus"]), reference)})
    sd_ratios: list[dict[str, Any]] = []
    for grid in protocol["design"]["grids"]:
        s64 = next((x for x in ensemble if x.get("method") == "sobol" and int(x["grid"]) == int(grid) and int(x["samples_per_cell"]) == 64), None)
        s256 = next((x for x in ensemble if x.get("method") == "sobol" and int(x["grid"]) == int(grid) and int(x["samples_per_cell"]) == 256), None)
        ratio = None if not s64 or not s256 or not s64.get("sd") or s64["sd"] == 0 else float(s256["sd"] / s64["sd"])
        sd_ratios.append({"grid": int(grid), "sd64": None if not s64 else s64.get("sd"), "sd256": None if not s256 else s256.get("sd"), "sd256_over_sd64": ratio})
    ratio_values = [float(x["sd256_over_sd64"]) for x in sd_ratios if x["sd256_over_sd64"] is not None]
    median_ratio = float(np.median(ratio_values)) if ratio_values else None
    expected = expected_configs(protocol)
    expected_ids = {
        config_id(config)
        for config in expected
    }
    observed_ids = [str(row.get("config_id")) for row in records]
    g0 = bool(
        len(records) == len(expected)
        and len(set(observed_ids)) == len(observed_ids)
        and set(observed_ids) == expected_ids
        and all(bool(row.get("g0_config_pass")) for row in records)
    )
    paired_mean_shifts = [
        float(x["relative_shift_256_vs_64"])
        for x in paired
        if x.get("relative_shift_256_vs_64") is not None
    ]
    g1 = bool(
        len(ratio_values) == 6
        and sum(r <= 1.0 for r in ratio_values) >= 5
        and median_ratio is not None
        and median_ratio <= 0.75
        and len(paired_mean_shifts) == 6
        and max(paired_mean_shifts) <= 0.01
    )
    gauss_gaps: list[dict[str, Any]] = []
    for grid in protocol["design"]["grids"]:
        q4 = next((x for x in gauss_summary if int(x["grid"]) == int(grid) and int(x["quadrature_order"]) == 4), None)
        q8 = next((x for x in gauss_summary if int(x["grid"]) == int(grid) and int(x["quadrature_order"]) == 8), None)
        q12 = next((x for x in gauss_summary if int(x["grid"]) == int(grid) and int(x["quadrature_order"]) == 12), None)
        gap48 = (
            None
            if not q4 or not q8 or q4.get("median") is None or q8.get("median") is None
            else relative_gap(q4["median"], q8["median"])
        )
        gap812 = (
            None
            if not q8 or not q12 or q8.get("median") is None or q12.get("median") is None
            else relative_gap(q8["median"], q12["median"])
        )
        gauss_gaps.append({"grid": int(grid), "q4_q8_gap": gap48, "q8_q12_gap": gap812})
    g2 = bool(len(gauss_gaps) == 6 and all(x["q8_q12_gap"] is not None and x["q8_q12_gap"] <= 0.005 for x in gauss_gaps) and sum(x["q8_q12_gap"] <= x["q4_q8_gap"] for x in gauss_gaps if x["q8_q12_gap"] is not None and x["q4_q8_gap"] is not None) >= 4)
    means = {(int(x["grid"]), int(x["samples_per_cell"])): x.get("mean") for x in ensemble}
    # G3 is frozen specifically for the 256-sample fresh-seed means.  Keep
    # the 64-sample trajectories in the per-seed table above, but do not let
    # them enter the G3 decision.
    trajectory_rows = []
    g3_samples = 256
    for chain in protocol["design"]["dyadic_chains"]:
        vals = [means.get((int(grid), g3_samples)) for grid in chain]
        first = None if any(v is None for v in vals) else relative_gap(vals[0], vals[1])
        final = None if any(v is None for v in vals) else relative_gap(vals[1], vals[2])
        trajectory_rows.append({"samples_per_cell": g3_samples, "chain": list(chain), "mean_values": vals, "first_relative_change": first, "final_relative_change": final, "D": None if first is None or final is None else final - first, "pass": None if first is None or final is None else final <= first})
    reference_ok = True
    if reference is not None:
        central = [
            float(row["mean"])
            for row in ensemble
            if row.get("method") == "sobol"
            and int(row["samples_per_cell"]) == 256
            and int(row["grid"]) in (96, 128)
            and row.get("mean") is not None
        ]
        reference_ok = len(central) == 2 and all(relative_gap(value, reference) <= 0.01 for value in central)
    g3 = bool(
        len(trajectory_rows) == len(protocol["design"]["dyadic_chains"])
        and all(row["pass"] for row in trajectory_rows if row["pass"] is not None)
        and reference_ok
    )
    return {
        "run_id": "R060_OPERATOR_VARIANCE_SUMMARY",
        "protocol_sha256": sha256_file(DEFAULT_PROTOCOL),
        "record_count": len(records),
        "expected_record_count_from_design": len(expected),
        "ensemble": ensemble,
        "gauss": gauss_summary,
        "paired_sample_budget": paired,
        "dyadic": dyadic,
        "dyadic_mean_trajectory": trajectory_rows,
        "sd_ratios": sd_ratios,
        "fredholm_reference": reference,
        "fredholm_source": reference_source,
        "fredholm_rows": fredholm_rows,
        "gates": {"G0_integrity": g0, "G1_sobol_variance": g1, "G2_gauss_order": g2, "G3_mean_trajectory": g3},
        "interpretation": "G1-G3 are descriptive finite-resolution diagnostics. A pass does not alter R059 G4=false and is not continuous operator convergence.",
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    design = protocol["design"]
    frozen_grids = [int(x) for x in design["grids"]]
    frozen_seeds = [int(x) for x in design["fresh_sobol_seeds"]]
    frozen_samples = [int(x) for x in design["sobol_samples_per_cell"]]
    frozen_orders = [int(x) for x in design["gauss_orders"]]
    protocol_sha = sha256_file(args.protocol)
    smoke = bool(args.smoke)
    grids = list(args.grid) if args.grid is not None else frozen_grids
    seeds = list(args.seed) if args.seed is not None else frozen_seeds
    samples = list(args.sobol_samples) if args.sobol_samples is not None else frozen_samples
    orders = list(args.gauss_order) if args.gauss_order is not None else frozen_orders
    workers = int(args.workers if args.workers is not None else design.get("workers", 8))
    if smoke:
        grids = list(args.grid) if args.grid is not None else [4]
        seeds = list(args.seed) if args.seed is not None else [frozen_seeds[0]]
        samples = list(args.sobol_samples) if args.sobol_samples is not None else [4, 8]
        orders = list(args.gauss_order) if args.gauss_order is not None else [2]
        if args.output == DEFAULT_OUTPUT:
            args.output = PROJECT_ROOT / "results" / "operator_variance_r060_smoke.json"
        if args.summary == DEFAULT_SUMMARY:
            args.summary = PROJECT_ROOT / "results" / "operator_variance_r060_smoke_summary.json"
        if args.csv == DEFAULT_CSV:
            args.csv = PROJECT_ROOT / "results" / "operator_variance_r060_smoke.csv"
        if args.matrix_dir == DEFAULT_MATRIX_DIR:
            args.matrix_dir = PROJECT_ROOT / "results" / "operator_variance_r060_smoke_matrices"
    configs: list[dict[str, Any]] = []
    common = {
        "matrix_dir": str(args.matrix_dir.resolve()),
        "protocol_sha256": protocol_sha,
        "eigenvalue_count": int(design["eigenvalue_count"]),
        "residual_tolerance": 1.0e-8,
        "row_sum_tolerance": 1.0e-12,
    }
    for grid in grids:
        for sample in samples:
            for seed in seeds:
                configs.append({**common, "grid": int(grid), "method": "sobol", "samples_per_cell": int(sample), "quadrature_order": 0, "seed": int(seed)})
        for order in orders:
            configs.append({**common, "grid": int(grid), "method": "gauss", "samples_per_cell": int(order) ** 2, "quadrature_order": int(order), "seed": None})
    frozen_configuration = bool(
        not smoke
        and grids == frozen_grids
        and seeds == frozen_seeds
        and samples == frozen_samples
        and orders == frozen_orders
        and len(configs) == 210
    )
    records: list[dict[str, Any]] = []
    if workers <= 1:
        for index, config in enumerate(configs, 1):
            record = run_config(config)
            records.append(record)
            print(f"[r060] {index}/{len(configs)} {record['config_id']} lambda={record['leading_modulus']:.12g}", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run_config, config) for config in configs]
            for index, future in enumerate(as_completed(futures), 1):
                record = future.result()
                records.append(record)
                print(f"[r060] {index}/{len(configs)} {record['config_id']} lambda={record['leading_modulus']:.12g}", flush=True)
    records.sort(key=lambda row: (int(row["grid"]), str(row["method_family"]), int(row["samples_per_cell"]), int(row["seed"] or -1), int(row["quadrature_order"])))
    fredholm, fredholm_source = fredholm_reference(args.fredholm)
    summary = build_summary(records, protocol, args.fredholm)
    summary["protocol_sha256"] = protocol_sha
    summary["frozen_configuration"] = frozen_configuration
    summary["fredholm_reference"] = fredholm
    summary["fredholm_source"] = fredholm_source
    payload = {
        "run_id": "R060_OPERATOR_VARIANCE",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable(args.protocol),
        "protocol_sha256": protocol_sha,
        "frozen_configuration": frozen_configuration,
        "records": records,
        "summary_path": portable(args.summary),
        "decisions": {
            "g0_integrity_pass": bool(summary["gates"]["G0_integrity"]),
            "g1_sobol_variance_descriptive_pass": bool(summary["gates"]["G1_sobol_variance"]),
            "g2_gauss_order_descriptive_pass": bool(summary["gates"]["G2_gauss_order"]),
            "g3_mean_trajectory_descriptive_pass": bool(summary["gates"]["G3_mean_trajectory"]),
            "r059_g4_remains_false": True,
        },
        "scope": "Finite-resolution variance and quadrature diagnostics on the explicit R059 four-h-set union; no continuous-operator claim.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    flat = [{key: value for key, value in row.items() if key != "eigenpairs" and key != "sampling_fingerprint"} for row in records]
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    if flat:
        with args.csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(flat[0]))
            writer.writeheader()
            writer.writerows(flat)
    print(json.dumps({"output": portable(args.output), "summary": portable(args.summary), "csv": portable(args.csv), "configurations": len(records), "frozen_configuration": frozen_configuration, "g0": summary["gates"]["G0_integrity"], "g1": summary["gates"]["G1_sobol_variance"], "g2": summary["gates"]["G2_gauss_order"], "g3": summary["gates"]["G3_mean_trajectory"]}, indent=2))
    if frozen_configuration and not summary["gates"]["G0_integrity"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
