#!/usr/bin/env python3
"""Build R061 common-finest-grid CSR coarsenings from frozen R060 parents.

No R060 matrix is reassembled or overwritten.  For a finest grid ``M`` and a
target grid ``m`` with ``r=M/m``, the derived row/column block average is

    C[I,J] = r**(-2) * sum(P[i,j] for i in block(I), j in block(J)).

The effective samples per coarse source cell are recorded as ``s*r**2``;
derived common-cloud matrices are never silently pooled with direct R060
estimators at the same nominal ``s``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from scipy.sparse import coo_matrix, load_npz, save_npz


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.restricted_operator import restricted_spectrum  # noqa: E402


DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R061_COMMON_CLOUD_PROTOCOL.json"
DEFAULT_PARENT = PROJECT_ROOT / "results" / "operator_variance_r060.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "common_coarsen_r061.json"
DEFAULT_CSV = PROJECT_ROOT / "results" / "common_coarsen_r061.csv"
DEFAULT_MATRIX_DIR = PROJECT_ROOT / "results" / "common_coarsen_r061_matrices"

RULE_VERSION = "R061_CSR_BLOCK_AVERAGE_V1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--parent", type=Path, default=DEFAULT_PARENT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--matrix-dir", type=Path, default=DEFAULT_MATRIX_DIR)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--chain", nargs="+")
    parser.add_argument("--seed", nargs="+", type=int)
    parser.add_argument("--sobol-samples", nargs="+", type=int)
    parser.add_argument("--gauss-order", nargs="+", type=int)
    parser.add_argument("--smoke", action="store_true")
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
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def relative_gap(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), np.finfo(float).tiny)


def block_map(m_fine: int, m_coarse: int) -> tuple[np.ndarray, np.ndarray, int]:
    if m_fine % m_coarse:
        raise ValueError(f"grid ratio is not integral: {m_fine}/{m_coarse}")
    ratio = m_fine // m_coarse
    fine_local = np.arange(m_fine * m_fine, dtype=np.int64)
    fine_y = fine_local // m_fine
    fine_x = fine_local % m_fine
    coarse_local = (fine_y // ratio) * m_coarse + (fine_x // ratio)
    source_map = np.concatenate(
        [state * (m_coarse * m_coarse) + coarse_local for state in range(4)]
    ).astype(np.int64, copy=False)
    target_map = source_map.copy()
    return source_map, target_map, ratio


def block_map_hash(m_fine: int, m_coarse: int) -> str:
    source_map, target_map, ratio = block_map(m_fine, m_coarse)
    payload = np.asarray([m_fine, m_coarse, ratio], dtype=np.int64).tobytes()
    return sha256_bytes(payload + source_map.tobytes() + target_map.tobytes())


def coarsen_matrix(matrix, m_fine: int, m_coarse: int):
    source_map, target_map, ratio = block_map(m_fine, m_coarse)
    coo = matrix.tocoo()
    rows = source_map[coo.row]
    cols = target_map[coo.col]
    values = np.asarray(coo.data, dtype=float) / float(ratio * ratio)
    shape = (4 * m_coarse * m_coarse, 4 * m_coarse * m_coarse)
    result = coo_matrix((values, (rows, cols)), shape=shape).tocsr()
    result.sum_duplicates()
    return result, ratio


def config_id(parent: dict[str, Any], target_grid: int, chain_name: str) -> str:
    method = str(parent["method_family"])
    if method == "sobol":
        suffix = f"sobol{int(parent['samples_per_cell'])}_seed{int(parent['seed'])}"
    else:
        suffix = f"gauss_q{int(parent['quadrature_order'])}"
    return f"r061_{chain_name}_m{int(target_grid):03d}_from{int(parent['grid']):03d}_{suffix}"


def expected_parent_records(protocol: dict[str, Any], payload: dict[str, Any],
                            chains: list[dict[str, Any]], seeds: list[int],
                            budgets: list[int], orders: list[int]) -> list[dict[str, Any]]:
    by_id = {str(row["config_id"]): row for row in payload.get("records", [])}
    out: list[dict[str, Any]] = []
    for chain in chains:
        fine = int(chain["fine_grid"])
        for budget in budgets:
            for seed in seeds:
                cid = f"r060_m{fine:03d}_sobol{budget}_seed{seed}"
                if cid not in by_id:
                    raise KeyError(f"missing R060 parent {cid}")
                out.append(by_id[cid])
        for order in orders:
            cid = f"r060_m{fine:03d}_gauss_q{order}"
            if cid not in by_id:
                raise KeyError(f"missing R060 parent {cid}")
            out.append(by_id[cid])
    return out


def run_one(config: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    parent_path = PROJECT_ROOT / str(config["parent_matrix_path"])
    matrix = load_npz(parent_path).tocsr()
    parent_sha = sha256_file(parent_path)
    if parent_sha != config["parent_matrix_sha256"]:
        raise RuntimeError(f"parent hash mismatch: {config['parent_config_id']}")
    derived, ratio = coarsen_matrix(matrix, int(config["fine_grid"]), int(config["target_grid"]))
    assembly_seconds = time.perf_counter() - started
    spectrum = restricted_spectrum(derived, eigenvalue_count=int(config["eigenvalue_count"]))
    matrix_dir = Path(config["matrix_dir"])
    matrix_dir.mkdir(parents=True, exist_ok=True)
    identifier = str(config["config_id"])
    matrix_path = matrix_dir / f"{identifier}.npz"
    schema_path = matrix_dir / f"{identifier}.schema.json"
    save_npz(matrix_path, derived, compressed=True)
    matrix_sha = sha256_file(matrix_path)
    row_sums = np.asarray(derived.sum(axis=1)).ravel()
    max_row = float(np.max(row_sums)) if row_sums.size else 0.0
    min_row = float(np.min(row_sums)) if row_sums.size else 0.0
    residual = float(spectrum["maximum_residual"])
    schema = {
        "schema_version": 1,
        "run_id": "R061_COMMON_CLOUD",
        "config_id": identifier,
        "protocol_sha256": str(config["protocol_sha256"]),
        "coarsening_rule_version": RULE_VERSION,
        "parent_config_id": str(config["parent_config_id"]),
        "parent_matrix_path": str(config["parent_matrix_path"]),
        "parent_matrix_sha256": str(config["parent_matrix_sha256"]),
        "direct_config_id": str(config["direct_config_id"]),
        "fine_grid": int(config["fine_grid"]),
        "target_grid": int(config["target_grid"]),
        "ratio": int(ratio),
        "state_order": ["--", "-+", "+-", "++"],
        "indexing": "global=state_index*m^2 + y_index*m + x_index; state-major, x index fastest",
        "target_semantics": "strict h-set interior followed by half-open local cells; exact h-set/cell-boundary hits are counted and discarded",
        "block_map_sha256": block_map_hash(int(config["fine_grid"]), int(config["target_grid"])),
        "matrix_path": portable(matrix_path),
        "matrix_sha256": matrix_sha,
        "matrix_format": "scipy_csr_npz",
        "shape": list(derived.shape),
        "dtype": str(derived.dtype),
        "nnz": int(derived.nnz),
        "method_family": str(config["method_family"]),
        "method": str(config["method"]),
        "samples_per_cell_parent": int(config["samples_per_cell"]),
        "effective_samples_per_cell": int(config["samples_per_cell"]) * int(ratio) ** 2,
        "quadrature_order": int(config["quadrature_order"]),
        "seed": config.get("seed"),
    }
    schema_path.write_text(json.dumps(schema, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    schema_sha = sha256_file(schema_path)
    return {
        "config_id": identifier,
        "run_id": "R061_COMMON_CLOUD",
        "chain": str(config["chain"]),
        "fine_grid": int(config["fine_grid"]),
        "target_grid": int(config["target_grid"]),
        "ratio": int(ratio),
        "parent_config_id": str(config["parent_config_id"]),
        "parent_matrix_path": str(config["parent_matrix_path"]),
        "parent_matrix_sha256": str(config["parent_matrix_sha256"]),
        "direct_config_id": str(config["direct_config_id"]),
        "direct_matrix_path": str(config["direct_matrix_path"]),
        "direct_matrix_sha256": str(config["direct_matrix_sha256"]),
        "method_family": str(config["method_family"]),
        "method": str(config["method"]),
        "samples_per_cell": int(config["samples_per_cell"]),
        "effective_samples_per_cell": int(config["samples_per_cell"]) * int(ratio) ** 2,
        "quadrature_order": int(config["quadrature_order"]),
        "seed": config.get("seed"),
        "matrix_path": portable(matrix_path),
        "matrix_sha256": matrix_sha,
        "schema_path": portable(schema_path),
        "schema_sha256": schema_sha,
        "matrix_shape": list(derived.shape),
        "matrix_nnz": int(derived.nnz),
        "minimum_row_sum": min_row,
        "maximum_row_sum": max_row,
        "mean_row_sum": float(np.mean(row_sums)) if row_sums.size else 0.0,
        "zero_row_fraction": float(np.mean(row_sums == 0.0)) if row_sums.size else 0.0,
        "leaky_row_fraction": float(np.mean(row_sums < 1.0 - 1.0e-12)) if row_sums.size else 0.0,
        "inherited_target_boundary_hits": int(config["parent_boundary_hits"]),
        "leading_eigenvalue": spectrum["leading_eigenvalue"],
        "leading_modulus": float(spectrum["leading_modulus"]),
        "maximum_eigenpair_residual": residual,
        "eigenpairs": spectrum["eigenpairs"],
        "block_map_sha256": block_map_hash(int(config["fine_grid"]), int(config["target_grid"])),
        "assembly_seconds": assembly_seconds,
        "nonnegative_pass": bool(derived.nnz == 0 or float(np.min(derived.data)) >= -1.0e-15),
        "substochastic_pass": bool(max_row <= 1.0 + float(config["row_sum_tolerance"])),
        "boundary_pass": bool(int(config["parent_boundary_hits"]) == 0),
        "residual_pass": bool(residual <= float(config["residual_tolerance"])),
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    parent_payload = json.loads(args.parent.read_text(encoding="utf-8"))
    protocol_sha = sha256_file(args.protocol)
    design = protocol["design"]
    chains = list(design["chains"])
    seeds = [int(x) for x in design["seeds"]]
    budgets = [int(x) for x in design["sobol_samples_per_cell"]]
    orders = [int(x) for x in design["gauss_orders"]]
    if args.chain:
        wanted = set(args.chain)
        chains = [x for x in chains if str(x["name"]) in wanted]
    if args.seed:
        seeds = [int(x) for x in args.seed]
    if args.sobol_samples:
        budgets = [int(x) for x in args.sobol_samples]
    if args.gauss_order:
        orders = [int(x) for x in args.gauss_order]
    smoke = bool(args.smoke)
    if smoke:
        chains = chains[:1]
        seeds = seeds[:2]
        budgets = budgets[:1]
        orders = orders[:1]
        if args.output == DEFAULT_OUTPUT:
            args.output = PROJECT_ROOT / "results" / "common_coarsen_r061_smoke.json"
        if args.csv == DEFAULT_CSV:
            args.csv = PROJECT_ROOT / "results" / "common_coarsen_r061_smoke.csv"
        if args.matrix_dir == DEFAULT_MATRIX_DIR:
            args.matrix_dir = PROJECT_ROOT / "results" / "common_coarsen_r061_smoke_matrices"
    records_by_id = {str(row["config_id"]): row for row in parent_payload.get("records", [])}
    parent_refs = expected_parent_records(protocol, parent_payload, chains, seeds, budgets, orders)
    configs: list[dict[str, Any]] = []
    for chain in chains:
        chain_name = str(chain["name"])
        fine = int(chain["fine_grid"])
        for parent in parent_refs:
            if int(parent["grid"]) != fine:
                continue
            for target in [int(x) for x in chain["target_grids"]]:
                direct_id = str(next(
                    row["config_id"] for row in parent_payload["records"]
                    if int(row["grid"]) == target
                    and str(row["method_family"]) == str(parent["method_family"])
                    and int(row["samples_per_cell"]) == int(parent["samples_per_cell"])
                    and (row.get("seed") == parent.get("seed"))
                    and int(row["quadrature_order"]) == int(parent["quadrature_order"])
                ))
                direct = records_by_id[direct_id]
                identifier = config_id(parent, target, chain_name)
                configs.append({
                    "config_id": identifier,
                    "chain": chain_name,
                    "fine_grid": fine,
                    "target_grid": target,
                    "parent_config_id": str(parent["config_id"]),
                    "parent_matrix_path": str(parent["matrix_path"]),
                    "parent_matrix_sha256": str(parent["matrix_sha256"]),
                    "parent_boundary_hits": int(parent.get("target_boundary_hits", 0)),
                    "direct_config_id": direct_id,
                    "direct_matrix_path": str(direct["matrix_path"]),
                    "direct_matrix_sha256": str(direct["matrix_sha256"]),
                    "method_family": str(parent["method_family"]),
                    "method": str(parent["method"]),
                    "samples_per_cell": int(parent["samples_per_cell"]),
                    "quadrature_order": int(parent["quadrature_order"]),
                    "seed": parent.get("seed"),
                    "matrix_dir": str(args.matrix_dir.resolve()),
                    "protocol_sha256": protocol_sha,
                    "eigenvalue_count": int(design["eigenvalue_count"]),
                    "row_sum_tolerance": 1.0e-12,
                    "residual_tolerance": 1.0e-8,
                })
    frozen = bool(
        not smoke
        and len(parent_refs) == 68
        and len(configs) == 136
        and len(chains) == 2
        and seeds == [int(x) for x in design["seeds"]]
        and budgets == [int(x) for x in design["sobol_samples_per_cell"]]
        and orders == [int(x) for x in design["gauss_orders"]]
    )
    records: list[dict[str, Any]] = []
    workers = int(args.workers if args.workers is not None else design.get("workers", 8))
    if workers <= 1:
        for i, config in enumerate(configs, 1):
            row = run_one(config)
            records.append(row)
            print(f"[r061] {i}/{len(configs)} {row['config_id']} lambda={row['leading_modulus']:.12g}", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run_one, config) for config in configs]
            for i, future in enumerate(as_completed(futures), 1):
                row = future.result()
                records.append(row)
                print(f"[r061] {i}/{len(configs)} {row['config_id']} lambda={row['leading_modulus']:.12g}", flush=True)
    records.sort(key=lambda row: (str(row["chain"]), int(row["fine_grid"]), str(row["method_family"]), int(row["samples_per_cell"]), int(row["seed"] or -1), int(row["quadrature_order"]), int(row["target_grid"])))
    parent_summary = []
    for row in parent_refs:
        parent_summary.append({
            "config_id": row["config_id"], "grid": row["grid"], "method_family": row["method_family"],
            "samples_per_cell": row["samples_per_cell"], "quadrature_order": row["quadrature_order"],
            "seed": row.get("seed"), "matrix_path": row["matrix_path"], "matrix_sha256": row["matrix_sha256"],
        })
    direct_links = [{"derived_config_id": row["config_id"], "direct_config_id": row["direct_config_id"], "direct_matrix_path": row["direct_matrix_path"], "direct_matrix_sha256": row["direct_matrix_sha256"]} for row in records]
    payload = {
        "run_id": "R061_COMMON_CLOUD",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable(args.protocol),
        "protocol_sha256": protocol_sha,
        "parent_path": portable(args.parent),
        "frozen_configuration": frozen,
        "parent_reference_count": len(parent_summary),
        "derived_record_count": len(records),
        "direct_link_count": len(direct_links),
        "parent_references": parent_summary,
        "direct_links": direct_links,
        "records": records,
        "scope": "CSR common-finest-grid block projection on frozen R060 matrices; no continuous-operator claim.",
        "r059_g4_remains_false": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    flat = [{key: value for key, value in row.items() if key != "eigenpairs"} for row in records]
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    if flat:
        fields = list(flat[0])
        with args.csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(flat)
    print(json.dumps({"output": portable(args.output), "csv": portable(args.csv), "parent_references": len(parent_summary), "derived_records": len(records), "direct_links": len(direct_links), "frozen_configuration": frozen}, indent=2))
    if frozen and (len(records) != 136 or len(parent_summary) != 68):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
