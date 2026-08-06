#!/usr/bin/env python3
"""Localize direct/common CSR discrepancy on the R061 source rows.

Samples are regenerated from the frozen R060 Sobol/Gauss rules.  For each
coarse source row, the script computes image-distance exposure to h-set and
internal target-cell boundaries, leakage, and
``E_i = 0.5 ||D_i-C_i||_1``.  Row arrays are persisted as compressed NPZ files;
the JSON output contains only hashes and seed-level summaries.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from scipy.sparse import load_npz
from scipy.stats import spearmanr
from scipy.stats import qmc


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R061_COMMON_CLOUD_PROTOCOL.json"
DEFAULT_COARSEN = PROJECT_ROOT / "results" / "common_coarsen_r061.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "boundary_localization_r061.json"
DEFAULT_ARRAY_DIR = PROJECT_ROOT / "results" / "boundary_localization_r061_arrays"

STATE_ORDER = ("--", "-+", "+-", "++")
BOUNDS = {
    "--": (-5.0 / 8.0, -1.0 / 3.0, -81.0 / 128.0, -5.0 / 16.0),
    "-+": (-5.0 / 8.0, -1.0 / 3.0, 5.0 / 16.0, 81.0 / 128.0),
    "+-": (1.0 / 3.0, 5.0 / 8.0, -81.0 / 128.0, -5.0 / 16.0),
    "++": (1.0 / 3.0, 5.0 / 8.0, 5.0 / 16.0, 81.0 / 128.0),
}
TAUS = (0.125, 0.25, 0.5, 1.0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--coarsen", type=Path, default=DEFAULT_COARSEN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--array-dir", type=Path, default=DEFAULT_ARRAY_DIR)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--chain", nargs="+")
    parser.add_argument("--seed", nargs="+", type=int)
    parser.add_argument("--sobol-samples", nargs="+", type=int)
    parser.add_argument("--gauss-order", nargs="+", type=int)
    parser.add_argument("--smoke", action="store_true")
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


def cell_geometry(m: int) -> tuple[np.ndarray, np.ndarray]:
    centers: list[np.ndarray] = []
    widths: list[np.ndarray] = []
    for state in STATE_ORDER:
        xl, xu, yl, yu = BOUNDS[state]
        wx = (xu - xl) / m
        wy = (yu - yl) / m
        xs = xl + (np.arange(m, dtype=float) + 0.5) * wx
        ys = yl + (np.arange(m, dtype=float) + 0.5) * wy
        xx, yy = np.meshgrid(xs, ys, indexing="xy")
        centers.append(np.column_stack((xx.ravel(), yy.ravel())))
        widths.append(np.tile(np.asarray([wx, wy]), (m * m, 1)))
    return np.concatenate(centers, axis=0), np.concatenate(widths, axis=0)


def sample_batches(m: int, method_family: str, samples: int, order: int, seed: int | None) -> Iterable[tuple[np.ndarray, float]]:
    centers, widths = cell_geometry(m)
    if method_family == "sobol":
        exponent = int(round(math.log2(samples)))
        if 2 ** exponent != samples:
            raise ValueError("Sobol sample count must be a power of two")
        base = qmc.Sobol(d=2, scramble=True, seed=int(seed)).random_base2(exponent)
        shifts = np.random.default_rng(int(seed) + 1_000_003).random((centers.shape[0], 2))
        for point in base:
            unit = np.mod(point + shifts, 1.0)
            yield centers + (unit - 0.5) * widths, 1.0 / float(samples)
        return
    nodes, weights = np.polynomial.legendre.leggauss(order)
    for xn, xw in zip(nodes, weights):
        for yn, yw in zip(nodes, weights):
            yield centers + 0.5 * widths * np.asarray([xn, yn]), float(xw * yw / 4.0)


def source_parent_map(m_fine: int, m_coarse: int) -> tuple[np.ndarray, int]:
    if m_fine % m_coarse:
        raise ValueError("non-integral source block ratio")
    ratio = m_fine // m_coarse
    local = np.arange(m_fine * m_fine, dtype=np.int64)
    y = local // m_fine
    x = local % m_fine
    coarse = (y // ratio) * m_coarse + (x // ratio)
    return np.concatenate([state * m_coarse * m_coarse + coarse for state in range(4)]), ratio


def image_exposure(points: np.ndarray, m: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, int]:
    image_x = 1.0 - 6.0 * points[:, 0] ** 2 - points[:, 1]
    image_y = points[:, 0]
    n = points.shape[0]
    signed = np.full(n, -np.inf, dtype=float)
    dcell = np.full(n, np.inf, dtype=float)
    inside_any = np.zeros(n, dtype=bool)
    boundary_hits = 0
    for state in STATE_ORDER:
        xl, xu, yl, yu = BOUNDS[state]
        norm = min((xu - xl) / m, (yu - yl) / m)
        closed = (image_x >= xl) & (image_x <= xu) & (image_y >= yl) & (image_y <= yu)
        interior = (image_x > xl) & (image_x < xu) & (image_y > yl) & (image_y < yu)
        boundary_hits += int(np.count_nonzero(closed & ~interior))
        margin = np.minimum.reduce((image_x - xl, xu - image_x, image_y - yl, yu - image_y)) / norm
        dx = np.maximum(np.maximum(xl - image_x, image_x - xu), 0.0)
        dy = np.maximum(np.maximum(yl - image_y, image_y - yu), 0.0)
        outside = -np.maximum(dx, dy) / norm
        candidate = np.where(interior, margin, outside)
        signed = np.maximum(signed, candidate)
        if np.any(interior):
            inside_any |= interior
            ux = (image_x[interior] - xl) / ((xu - xl) / m)
            uy = (image_y[interior] - yl) / ((yu - yl) / m)
            frac_x = np.mod(ux, 1.0)
            frac_y = np.mod(uy, 1.0)
            local_d = np.minimum.reduce((frac_x, 1.0 - frac_x, frac_y, 1.0 - frac_y))
            positions = np.flatnonzero(interior)
            dcell[positions] = np.minimum(dcell[positions], local_d)
            boundary_hits += int(np.count_nonzero((ux == np.floor(ux)) | (uy == np.floor(uy))))
    return signed, dcell, inside_any, boundary_hits


def spearman_safe(x: np.ndarray, y: np.ndarray) -> float | None:
    mask = np.isfinite(x) & np.isfinite(y)
    if np.count_nonzero(mask) < 3 or np.ptp(x[mask]) == 0.0 or np.ptp(y[mask]) == 0.0:
        return None
    value = spearmanr(x[mask], y[mask]).statistic
    return None if not np.isfinite(value) else float(value)


def top_quartile_concentration(energy: np.ndarray, exposure: np.ndarray) -> float | None:
    total = float(np.sum(energy))
    if total <= 0.0 or exposure.size == 0:
        return None
    count = max(1, int(math.ceil(exposure.size * 0.25)))
    # Use a rank-defined top quartile rather than a quantile threshold: the
    # exposure arrays contain many exact zeros, and threshold ties would
    # otherwise select nearly every row and inflate the concentration to one.
    order = np.argsort(-exposure, kind="mergesort")
    chosen = order[:count]
    return float(np.sum(energy[chosen]) / total)


def aggregate_exposure(m_fine: int, m_coarse: int, method_family: str, samples: int, order: int, seed: int | None) -> dict[str, Any]:
    parent_map, ratio = source_parent_map(m_fine, m_coarse)
    n_rows = 4 * m_coarse * m_coarse
    total = np.zeros(n_rows, dtype=float)
    inside_total = np.zeros(n_rows, dtype=float)
    h_counts = {str(tau): np.zeros(n_rows, dtype=float) for tau in TAUS}
    cell_counts = {str(tau): np.zeros(n_rows, dtype=float) for tau in TAUS}
    boundary_hits = 0
    point_count = 0
    for points, weight in sample_batches(m_fine, method_family, samples, order, seed):
        signed, dcell, inside, hits = image_exposure(points, m_coarse)
        boundary_hits += hits
        point_count += points.shape[0]
        weights = np.full(points.shape[0], weight, dtype=float)
        total += np.bincount(parent_map, weights=weights, minlength=n_rows)
        inside_total += np.bincount(parent_map, weights=weights * inside.astype(float), minlength=n_rows)
        for tau in TAUS:
            h_counts[str(tau)] += np.bincount(parent_map, weights=weights * (np.abs(signed) <= tau), minlength=n_rows)
            cell_counts[str(tau)] += np.bincount(parent_map, weights=weights * (inside & (dcell <= tau)), minlength=n_rows)
    h_exposure = {key: np.divide(value, total, out=np.zeros_like(value), where=total > 0.0) for key, value in h_counts.items()}
    cell_exposure = {key: np.divide(value, inside_total, out=np.zeros_like(value), where=inside_total > 0.0) for key, value in cell_counts.items()}
    return {"h_exposure": h_exposure, "cell_exposure": cell_exposure, "inside_fraction": np.divide(inside_total, total, out=np.zeros_like(total), where=total > 0.0), "sample_weight_total": total, "boundary_hits": boundary_hits, "point_count": point_count, "ratio": ratio}


def run_one(config: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    target = int(config["target_grid"])
    fine = int(config["fine_grid"])
    common_path = PROJECT_ROOT / str(config["common_matrix_path"])
    direct_path = PROJECT_ROOT / str(config["direct_matrix_path"])
    common = load_npz(common_path).tocsr()
    direct = load_npz(direct_path).tocsr()
    if common.shape != direct.shape:
        raise ValueError("direct/common shapes differ")
    diff = (common - direct).tocsr()
    row_energy = 0.5 * np.asarray(abs(diff).sum(axis=1)).ravel()
    common_rows = np.asarray(common.sum(axis=1)).ravel()
    direct_rows = np.asarray(direct.sum(axis=1)).ravel()
    exposure = aggregate_exposure(fine, target, str(config["method_family"]), int(config["samples_per_cell"]), int(config["quadrature_order"]), config.get("seed"))
    arrays_dir = Path(config["array_dir"])
    arrays_dir.mkdir(parents=True, exist_ok=True)
    identifier = str(config["config_id"])
    array_path = arrays_dir / f"{identifier}.npz"
    save_dict: dict[str, Any] = {"row_energy": row_energy, "common_leak": 1.0 - common_rows, "direct_leak": 1.0 - direct_rows, "inside_fraction": exposure["inside_fraction"]}
    for tau in TAUS:
        key = str(tau)
        save_dict[f"h_exposure_tau_{key}"] = exposure["h_exposure"][key]
        save_dict[f"cell_exposure_tau_{key}"] = exposure["cell_exposure"][key]
    np.savez_compressed(array_path, **save_dict)
    array_sha = sha256_file(array_path)
    tau_summary: dict[str, Any] = {}
    for tau in TAUS:
        key = str(tau)
        h = exposure["h_exposure"][key]
        c = exposure["cell_exposure"][key]
        tau_summary[key] = {"spearman_h": spearman_safe(row_energy, h), "spearman_cell": spearman_safe(row_energy, c), "top25_h": top_quartile_concentration(row_energy, h), "top25_cell": top_quartile_concentration(row_energy, c), "mean_h": float(np.mean(h)), "mean_cell": float(np.mean(c))}
    total_energy = float(np.sum(row_energy))
    return {"config_id": identifier, "chain": config["chain"], "fine_grid": fine, "target_grid": target, "ratio": int(config["ratio"]), "method_family": config["method_family"], "samples_per_cell": int(config["samples_per_cell"]), "effective_samples_per_cell": int(config["effective_samples_per_cell"]), "quadrature_order": int(config["quadrature_order"]), "seed": config.get("seed"), "common_matrix_path": config["common_matrix_path"], "common_matrix_sha256": config["common_matrix_sha256"], "direct_matrix_path": config["direct_matrix_path"], "direct_matrix_sha256": config["direct_matrix_sha256"], "array_path": portable(array_path), "array_sha256": array_sha, "row_count": int(row_energy.size), "total_row_energy": total_energy, "positive_energy_row_fraction": float(np.mean(row_energy > 0.0)), "common_mean_leak": float(np.mean(1.0 - common_rows)), "direct_mean_leak": float(np.mean(1.0 - direct_rows)), "boundary_hits": int(exposure["boundary_hits"]), "point_count": int(exposure["point_count"]), "tau_summary": tau_summary, "seconds": time.perf_counter() - started}


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    coarsen = json.loads(args.coarsen.read_text(encoding="utf-8"))
    protocol_sha = sha256_file(args.protocol)
    design = protocol["design"]
    chains = list(design["chains"])
    seeds = [int(x) for x in design["seeds"]]
    budgets = [int(x) for x in design["sobol_samples_per_cell"]]
    orders = [int(x) for x in design["gauss_orders"]]
    if args.chain:
        chains = [x for x in chains if str(x["name"]) in set(args.chain)]
    if args.seed:
        seeds = [int(x) for x in args.seed]
    if args.sobol_samples:
        budgets = [int(x) for x in args.sobol_samples]
    if args.gauss_order:
        orders = [int(x) for x in args.gauss_order]
    smoke = bool(args.smoke)
    if smoke:
        chains = chains[:1]
        seeds = seeds[:1]
        budgets = budgets[:1]
        orders = orders[:1]
        if args.output == DEFAULT_OUTPUT:
            args.output = PROJECT_ROOT / "results" / "boundary_localization_r061_smoke.json"
        if args.array_dir == DEFAULT_ARRAY_DIR:
            args.array_dir = PROJECT_ROOT / "results" / "boundary_localization_r061_smoke_arrays"
    coarsen_records = list(coarsen.get("records", []))
    configs: list[dict[str, Any]] = []
    for row in coarsen_records:
        chain = str(row["chain"])
        if chain not in {str(x["name"]) for x in chains}:
            continue
        if str(row["method_family"]) == "sobol":
            if int(row["samples_per_cell"]) not in budgets or int(row["seed"]) not in seeds:
                continue
        else:
            if int(row["quadrature_order"]) not in orders:
                continue
        configs.append({
            "config_id": row["config_id"], "chain": chain, "fine_grid": int(row["fine_grid"]), "target_grid": int(row["target_grid"]), "ratio": int(row["ratio"]), "method_family": row["method_family"], "samples_per_cell": int(row["samples_per_cell"]), "effective_samples_per_cell": int(row["effective_samples_per_cell"]), "quadrature_order": int(row["quadrature_order"]), "seed": row.get("seed"), "common_matrix_path": row["matrix_path"], "common_matrix_sha256": row["matrix_sha256"], "direct_matrix_path": row["direct_matrix_path"], "direct_matrix_sha256": row["direct_matrix_sha256"], "array_dir": str(args.array_dir.resolve())
        })
    expected_count = 6 if smoke else 136
    records: list[dict[str, Any]] = []
    workers = int(args.workers if args.workers is not None else design.get("workers", 8))
    if workers <= 1:
        for i, cfg in enumerate(configs, 1):
            rec = run_one(cfg); records.append(rec); print(f"[r061-localize] {i}/{len(configs)} {rec['config_id']}", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run_one, cfg) for cfg in configs]
            for i, future in enumerate(as_completed(futures), 1):
                rec = future.result(); records.append(rec); print(f"[r061-localize] {i}/{len(configs)} {rec['config_id']}", flush=True)
    records.sort(key=lambda x: str(x["config_id"]))
    output = {"run_id": "R061_BOUNDARY_LOCALIZATION", "created_utc": datetime.now(timezone.utc).isoformat(), "protocol_path": portable(args.protocol), "protocol_sha256": protocol_sha, "coarsen_path": portable(args.coarsen), "frozen_configuration": bool(not smoke and len(records) == expected_count), "record_count": len(records), "records": records, "scope": "Finite-resolution row localization; no continuous-operator claim."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": portable(args.output), "records": len(records), "expected": expected_count, "frozen_configuration": output["frozen_configuration"]}, indent=2))
    if output["frozen_configuration"] and len(records) != expected_count:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
