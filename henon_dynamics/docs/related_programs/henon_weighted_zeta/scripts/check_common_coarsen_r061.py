#!/usr/bin/env python3
"""Independent integrity checker for R061 common-cloud coarsenings.

The checker deliberately does not import the R061 producer or the restricted
operator assembly module.  It rebuilds the fine-to-coarse state-major block
map, verifies parent/direct bindings, and reconstructs selected derived CSR
rows directly from the frozen parent matrices.
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
from scipy.sparse import csr_matrix, load_npz


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R061_COMMON_CLOUD_PROTOCOL.json"
DEFAULT_INPUT = PROJECT_ROOT / "results" / "common_coarsen_r061.json"
DEFAULT_PARENT = PROJECT_ROOT / "results" / "operator_variance_r060.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "common_coarsen_r061_check.json"
RULE_VERSION = "R061_CSR_BLOCK_AVERAGE_V1"
EXPECTED_INDEXING = "global=state_index*m^2 + y_index*m + x_index; state-major, x index fastest"
EXPECTED_SEMANTICS = "strict h-set interior followed by half-open local cells; exact h-set/cell-boundary hits are counted and discarded"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--parent", type=Path, default=DEFAULT_PARENT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--row-tolerance", type=float, default=2.0e-12)
    parser.add_argument("--row-sum-tolerance", type=float, default=1.0e-12)
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


def project(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def block_maps(m_fine: int, m_coarse: int) -> tuple[np.ndarray, np.ndarray, int]:
    if m_fine < 2 or m_coarse < 2 or m_fine % m_coarse:
        raise ValueError("invalid integral grid ratio")
    ratio = m_fine // m_coarse
    local = np.arange(m_fine * m_fine, dtype=np.int64)
    y = local // m_fine
    x = local % m_fine
    coarse_local = (y // ratio) * m_coarse + (x // ratio)
    source = np.concatenate([state * m_coarse * m_coarse + coarse_local for state in range(4)])
    return source, source.copy(), ratio


def map_hash(m_fine: int, m_coarse: int) -> str:
    source, target, ratio = block_maps(m_fine, m_coarse)
    head = np.asarray([m_fine, m_coarse, ratio], dtype=np.int64).tobytes()
    return sha256_bytes(head + source.tobytes() + target.tobytes())


def expected_configs(protocol: dict[str, Any], parent: dict[str, Any]) -> dict[str, dict[str, Any]]:
    parent_by_id = {str(row["config_id"]): row for row in parent.get("records", [])}
    design = protocol["design"]
    result: dict[str, dict[str, Any]] = {}
    for chain in design["chains"]:
        name = str(chain["name"])
        fine = int(chain["fine_grid"])
        for budget in design["sobol_samples_per_cell"]:
            for seed in design["seeds"]:
                pid = f"r060_m{fine:03d}_sobol{int(budget)}_seed{int(seed)}"
                p = parent_by_id[pid]
                for target in chain["target_grids"]:
                    did = f"r061_{name}_m{int(target):03d}_from{fine:03d}_sobol{int(budget)}_seed{int(seed)}"
                    direct = next(row for row in parent["records"] if int(row["grid"]) == int(target) and row["method_family"] == "sobol" and int(row["samples_per_cell"]) == int(budget) and int(row["seed"]) == int(seed))
                    result[did] = {"chain": name, "fine_grid": fine, "target_grid": int(target), "parent_config_id": pid, "direct_config_id": direct["config_id"], "parent": p, "direct": direct, "samples_per_cell": int(budget), "seed": int(seed), "method_family": "sobol", "quadrature_order": 0}
        for order in design["gauss_orders"]:
            pid = f"r060_m{fine:03d}_gauss_q{int(order)}"
            p = parent_by_id[pid]
            for target in chain["target_grids"]:
                did = f"r061_{name}_m{int(target):03d}_from{fine:03d}_gauss_q{int(order)}"
                direct = next(row for row in parent["records"] if int(row["grid"]) == int(target) and row["method_family"] == "gauss" and int(row["quadrature_order"]) == int(order))
                result[did] = {"chain": name, "fine_grid": fine, "target_grid": int(target), "parent_config_id": pid, "direct_config_id": direct["config_id"], "parent": p, "direct": direct, "samples_per_cell": int(order) ** 2, "seed": None, "method_family": "gauss", "quadrature_order": int(order)}
    return result


def expected_row_from_parent(parent_matrix: csr_matrix, row: int, m_fine: int, m_coarse: int) -> dict[int, float]:
    _, _, ratio = block_maps(m_fine, m_coarse)
    state = int(row) // (m_coarse * m_coarse)
    local = int(row) % (m_coarse * m_coarse)
    cy, cx = divmod(local, m_coarse)
    expected: dict[int, float] = {}
    for dy in range(ratio):
        for dx in range(ratio):
            fine_row = state * m_fine * m_fine + (cy * ratio + dy) * m_fine + (cx * ratio + dx)
            sparse = parent_matrix.getrow(fine_row)
            for col, value in zip(sparse.indices, sparse.data):
                target_state = int(col) // (m_fine * m_fine)
                target_local = int(col) % (m_fine * m_fine)
                ty, tx = divmod(target_local, m_fine)
                coarse_col = target_state * m_coarse * m_coarse + (ty // ratio) * m_coarse + (tx // ratio)
                expected[coarse_col] = expected.get(coarse_col, 0.0) + float(value) / float(ratio * ratio)
    return expected


def compare_row(matrix: csr_matrix, row: int, expected: dict[int, float], tol: float) -> dict[str, Any]:
    sparse = matrix.getrow(int(row))
    actual = {int(col): float(value) for col, value in zip(sparse.indices, sparse.data)}
    keys = set(actual) == set(expected)
    vals = keys and all(math.isclose(actual[col], expected[col], rel_tol=tol, abs_tol=tol) for col in expected)
    return {"row": int(row), "expected_nnz": len(expected), "observed_nnz": len(actual), "keys_match": keys, "values_match": vals, "pass": bool(keys and vals)}


def selected_rows(m: int) -> list[int]:
    local = sorted({0, 1, m * m // 2, m * m - 2, m * m - 1, (m * m - 1) // 3, 2 * (m * m - 1) // 3})
    return [state * m * m + i for state in range(4) for i in local]


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    parent = json.loads(args.parent.read_text(encoding="utf-8"))
    protocol_sha = sha256_file(args.protocol)
    expected = expected_configs(protocol, parent)
    records = list(payload.get("records", []))
    seen: set[str] = set()
    record_checks: list[dict[str, Any]] = []
    for record in records:
        cid = str(record.get("config_id"))
        check: dict[str, Any] = {"config_id": cid, "unique": cid not in seen, "expected": cid in expected}
        seen.add(cid)
        if cid not in expected:
            check["pass"] = False
            record_checks.append(check)
            continue
        exp = expected[cid]
        matrix_path = PROJECT_ROOT / str(record.get("matrix_path", ""))
        schema_path = PROJECT_ROOT / str(record.get("schema_path", ""))
        check["matrix_exists"] = matrix_path.exists()
        check["schema_exists"] = schema_path.exists()
        check["matrix_hash"] = bool(matrix_path.exists() and sha256_file(matrix_path) == record.get("matrix_sha256"))
        check["schema_hash"] = bool(schema_path.exists() and sha256_file(schema_path) == record.get("schema_sha256"))
        p = exp["parent"]
        dp = exp["direct"]
        parent_path = PROJECT_ROOT / str(p["matrix_path"])
        direct_path = PROJECT_ROOT / str(dp["matrix_path"])
        check["parent_hash"] = bool(parent_path.exists() and sha256_file(parent_path) == record.get("parent_matrix_sha256") == p.get("matrix_sha256"))
        check["direct_hash"] = bool(direct_path.exists() and sha256_file(direct_path) == record.get("direct_matrix_sha256") == dp.get("matrix_sha256"))
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            matrix = load_npz(matrix_path).tocsr()
            parent_matrix = load_npz(parent_path).tocsr()
            check["protocol_binding"] = schema.get("protocol_sha256") == protocol_sha and payload.get("protocol_sha256") == protocol_sha
            check["schema_semantics"] = schema.get("coarsening_rule_version") == RULE_VERSION and schema.get("indexing") == EXPECTED_INDEXING and schema.get("target_semantics") == EXPECTED_SEMANTICS and schema.get("config_id") == cid
            check["metadata_match"] = all(record.get(key) == value for key, value in {"chain": exp["chain"], "fine_grid": exp["fine_grid"], "target_grid": exp["target_grid"], "parent_config_id": exp["parent_config_id"], "direct_config_id": exp["direct_config_id"], "method_family": exp["method_family"], "samples_per_cell": exp["samples_per_cell"], "quadrature_order": exp["quadrature_order"], "seed": exp["seed"]}.items())
            check["shape"] = list(matrix.shape) == [4 * exp["target_grid"] * exp["target_grid"]] * 2
            check["schema_shape"] = schema.get("shape") == list(matrix.shape)
            check["block_map_hash"] = record.get("block_map_sha256") == schema.get("block_map_sha256") == map_hash(exp["fine_grid"], exp["target_grid"])
            rows = np.asarray(matrix.sum(axis=1)).ravel()
            check["finite_nonnegative"] = bool(matrix.nnz == 0 or (np.all(np.isfinite(matrix.data)) and np.min(matrix.data) >= -1.0e-15))
            check["substochastic"] = bool(np.max(rows) <= 1.0 + args.row_sum_tolerance)
            check["nnz_match"] = int(matrix.nnz) == int(record.get("matrix_nnz", -1))
            check["residual_pass"] = float(record.get("maximum_eigenpair_residual", math.inf)) <= 1.0e-8
            check["boundary_pass"] = int(record.get("inherited_target_boundary_hits", -1)) == 0
            parent_rows = np.asarray(parent_matrix.sum(axis=1)).ravel().reshape((4, exp["fine_grid"], exp["fine_grid"]))
            ratio = exp["fine_grid"] // exp["target_grid"]
            expected_sums = parent_rows.reshape(4, exp["target_grid"], ratio, exp["target_grid"], ratio).mean(axis=(2, 4)).reshape(-1)
            check["row_sum_reconstruction"] = bool(np.max(np.abs(expected_sums - rows), initial=0.0) <= args.row_sum_tolerance)
            row_checks = []
            for row in selected_rows(exp["target_grid"]):
                row_checks.append(compare_row(matrix, row, expected_row_from_parent(parent_matrix, row, exp["fine_grid"], exp["target_grid"]), args.row_tolerance))
            check["source_row_reconstruction"] = bool(all(x["pass"] for x in row_checks))
            check["source_row_checks"] = row_checks
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            check["load_error"] = repr(exc)
        bool_keys = [key for key, value in check.items() if isinstance(value, bool) and key not in {"unique", "expected"}]
        check["pass"] = bool(check.get("unique") and check.get("expected") and bool_keys and all(bool(check[key]) for key in bool_keys))
        record_checks.append(check)
    parent_refs = list(payload.get("parent_references", []))
    links = list(payload.get("direct_links", []))
    parent_ref_pass = len(parent_refs) == (3 if args.smoke else 68) and len({str(x.get("config_id")) for x in parent_refs}) == len(parent_refs)
    direct_link_pass = len(links) == len(records) and len({str(x.get("derived_config_id")) for x in links}) == len(links)
    complete = len(records) == (6 if args.smoke else 136) and seen == (set(cid for cid in expected) if not args.smoke else seen)
    checks = {
        "protocol_binding": payload.get("protocol_sha256") == protocol_sha,
        "parent_payload_protocol_binding": parent.get("protocol_sha256") is not None,
        "parent_reference_count": len(parent_refs),
        "parent_reference_pass": parent_ref_pass,
        "direct_link_pass": direct_link_pass,
        "derived_record_complete": complete,
        "all_record_checks": bool(record_checks) and all(bool(x.get("pass")) for x in record_checks),
        "protocol_expected_parent_count": int(protocol["design"]["parent_reference_count"]),
        "protocol_expected_derived_count": int(protocol["design"]["derived_matrix_count"]),
    }
    all_pass = bool(checks["protocol_binding"] and checks["parent_reference_pass"] and checks["direct_link_pass"] and checks["derived_record_complete"] and checks["all_record_checks"])
    output = {
        "run_id": "R061_COMMON_CLOUD_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "input": project(args.input),
        "protocol": project(args.protocol),
        "protocol_sha256": protocol_sha,
        "checks": checks,
        "record_checks": record_checks,
        "all_checks_pass": all_pass,
        "scope": "Independent finite-resolution CSR coarsening integrity check; no continuous-operator claim."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": project(args.output), "records_checked": len(records), "all_checks_pass": all_pass, "parent_reference_count": len(parent_refs), "derived_record_count": len(records)}, indent=2))
    if not all_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
