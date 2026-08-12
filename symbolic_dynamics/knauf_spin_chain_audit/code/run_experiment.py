#!/usr/bin/env python3
"""Run the locked Knauf spin-chain finite-k experiment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import mpmath
import mpmath as mp
import numpy as np

from knauf import (
    analytic_liouville,
    analytic_unsigned,
    arithmetic_sieves,
    coefficient_histogram,
    complete_totient_prefix,
    evaluate_dirichlet_complex128,
    evaluate_dirichlet_mpmath,
    iter_h_levels,
    parse_grid,
    splitmix64_state_signs,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--results-dir", type=Path, required=True)
    return parser.parse_args()


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def target_and_status(observable: str, s: complex) -> tuple[complex | None, str]:
    if observable == "unsigned":
        target = analytic_unsigned(s)
        if s.real > 2.0:
            return target, "PROVED_DIRICHLET_LIMIT_RE_GT_2"
        if s.real == 2.0 and s.imag == 0.0:
            return target, "PROVED_DIVERGENT_BOUNDARY_NO_FINITE_TARGET"
        return target, "MEROMORPHIC_BENCHMARK_ONLY_OUTSIDE_PROVED_DOMAIN"
    if observable == "liouville":
        target = analytic_liouville(s)
        if s.real > 2.0:
            return target, "PROVED_DIRICHLET_LIMIT_RE_GT_2"
        if s.real == 2.0 and s.imag == 0.0:
            return target, "BOUNDARY_VALUE_BENCHMARK_NO_CONVERGENCE_CLAIM"
        return target, "ANALYTIC_CONTINUATION_BENCHMARK_CONDITIONAL_REGION"
    return None, "CONTROL_NO_ANALYTIC_TARGET"


def summarize(
    rows: list[dict[str, Any]],
    diagnostics: list[dict[str, Any]],
    precision_rows: list[dict[str, Any]],
    final_k: int,
) -> dict[str, Any]:
    final = [row for row in rows if row["cutoff_k"] == final_k]

    def finite_numbers(items: list[Any]) -> list[float]:
        return [float(item) for item in items if item not in (None, "") and np.isfinite(float(item))]

    groups: dict[str, dict[str, Any]] = {}
    for observable in sorted({str(row["observable"]) for row in final}):
        subset = [row for row in final if row["observable"] == observable]
        proved = [
            row
            for row in subset
            if row["target_status"] == "PROVED_DIRICHLET_LIMIT_RE_GT_2"
        ]
        nonproved_benchmarks = [
            row
            for row in subset
            if "BENCHMARK" in str(row["target_status"])
            and row["target_abs_error"] not in (None, "")
        ]
        drift = finite_numbers([row["successive_k_drift"] for row in subset])
        proved_error = finite_numbers([row["target_abs_error"] for row in proved])
        nonproved_benchmark_error = finite_numbers(
            [row["target_abs_error"] for row in nonproved_benchmarks]
        )
        groups[observable] = {
            "row_count": len(subset),
            "proved_region_max_abs_error": max(proved_error) if proved_error else None,
            "proved_region_median_abs_error": float(np.median(proved_error)) if proved_error else None,
            "nonproved_benchmark_max_abs_error": max(nonproved_benchmark_error)
            if nonproved_benchmark_error
            else None,
            "max_successive_k_drift": max(drift) if drift else None,
            "median_successive_k_drift": float(np.median(drift)) if drift else None,
        }

    precision_diffs = finite_numbers(
        [row["abs_diff_vs_mpmath_100"] for row in precision_rows]
    )
    return {
        "final_cutoff_k": final_k,
        "final_state_count": 2**final_k,
        "observables": groups,
        "precision_audit_max_abs_diff_vs_mpmath_100": max(precision_diffs)
        if precision_diffs
        else None,
        "cutoff_diagnostics_final": diagnostics[-1],
        "claim_labels": {
            "exact_recurrence_and_zeta_ratios": "PROVED (source identity; implementation tested)",
            "finite_k_values": "NUMERICAL_OBSERVATION",
            "re_gt_2_approach": "NUMERICAL_OBSERVATION consistent with proved limit",
            "1p5_lt_re_le_2_approach": "NUMERICAL_OBSERVATION only; no convergence or RH claim",
            "random_control_behavior": "NUMERICAL_OBSERVATION over locked seeds only",
        },
    }


def main() -> int:
    args = parse_args()
    protocol_bytes = args.protocol.read_bytes()
    protocol = json.loads(protocol_bytes)
    protocol_hash = hashlib.sha256(protocol_bytes).hexdigest()
    output_dir = args.results_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    cutoffs = [int(value) for value in protocol["cutoffs_k"]]
    if cutoffs != sorted(set(cutoffs)):
        raise ValueError("cutoffs_k must be sorted and unique")
    grid = parse_grid(protocol["grid"])
    seeds = [int(seed) for seed in protocol["random_sign_control"]["base_seeds"]]
    max_k = max(cutoffs)
    audit_cutoffs = {int(k) for k in protocol["precision_audit"]["cutoffs_k"]}
    audit_dps = [int(value) for value in protocol["precision_audit"]["dps"]]
    if 100 not in audit_dps:
        raise ValueError("precision audit must include 100 dps as its reference")

    started = time.time()
    rows: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    seed_ledger: list[dict[str, Any]] = []
    audit_coefficients: dict[int, dict[str, np.ndarray]] = {}
    previous: dict[tuple[str, str, str], complex] = {}
    selected = set(cutoffs)

    for k, h, parity in iter_h_levels(max_k):
        if k not in selected:
            continue
        unsigned = coefficient_histogram(h)
        max_h = int(h.max())
        phi, liouville_values, mobius_values = arithmetic_sieves(max_h)
        liouville = unsigned * liouville_values.astype(np.int64)
        mobius = unsigned * mobius_values.astype(np.int64)
        parity_control = coefficient_histogram(h, parity)

        if np.any(unsigned > phi):
            bad = int(np.flatnonzero(unsigned > phi)[0])
            raise AssertionError(f"phi_k({bad}) exceeds Euler phi({bad})")
        prefix = complete_totient_prefix(unsigned, phi)
        diagnostics.append(
            {
                "cutoff_k": k,
                "state_count": int(h.size),
                "max_h": max_h,
                "support_size": int(np.count_nonzero(unsigned)),
                "complete_totient_prefix": prefix,
                "coefficient_mass_fraction_through_max_h": float(
                    h.size / np.sum(phi[1:], dtype=np.float64)
                ),
                "sum_liouville_coefficients": int(np.sum(liouville, dtype=np.int64)),
                "sum_mobius_coefficients": int(np.sum(mobius, dtype=np.int64)),
                "sum_parity_coefficients": int(np.sum(parity_control, dtype=np.int64)),
            }
        )

        coefficient_sets: list[tuple[str, str, np.ndarray]] = [
            ("unsigned", "none", unsigned),
            ("liouville", "none", liouville),
            ("mobius", "none", mobius),
            ("symbolic_parity", "none", parity_control),
        ]
        for seed in seeds:
            signs = splitmix64_state_signs(h.size, seed, k)
            random_coeff = coefficient_histogram(h, signs)
            seed_ledger.append(
                {
                    "base_seed": seed,
                    "cutoff_k": k,
                    "state_count": int(h.size),
                    "algorithm": "SplitMix64_counter_hash_v1",
                    "positive_count": int(np.count_nonzero(signs == 1)),
                    "negative_count": int(np.count_nonzero(signs == -1)),
                    "sign_sum": int(np.sum(signs, dtype=np.int64)),
                    "sign_field_sha256": hashlib.sha256(signs.tobytes()).hexdigest(),
                    "selection_status": "ALL_REPORTED_NO_BEST_SEED_SELECTION",
                }
            )
            coefficient_sets.append(("random_state_sign", str(seed), random_coeff))

        if k in audit_cutoffs:
            audit_coefficients[k] = {
                "unsigned": unsigned.copy(),
                "liouville": liouville.copy(),
            }

        for observable, seed, coefficients in coefficient_sets:
            for point in grid:
                s = complex(float(point["sigma"]), float(point["tau"]))
                value = evaluate_dirichlet_complex128(coefficients, s)
                target, target_status = target_and_status(observable, s)
                key = (observable, seed, str(point["id"]))
                predecessor = previous.get(key)
                drift = abs(value - predecessor) if predecessor is not None else None
                previous[key] = value
                rows.append(
                    {
                        "cutoff_k": k,
                        "state_count": int(h.size),
                        "max_h": max_h,
                        "grid_id": point["id"],
                        "sigma": s.real,
                        "tau": s.imag,
                        "observable": observable,
                        "seed": seed,
                        "value_re": value.real,
                        "value_im": value.imag,
                        "abs_value": abs(value),
                        "target_re": target.real if target is not None else None,
                        "target_im": target.imag if target is not None else None,
                        "target_abs_error": abs(value - target)
                        if target is not None
                        else None,
                        "target_status": target_status,
                        "successive_k_drift": drift,
                        "precision_mode": "numpy_complex128",
                    }
                )
        print(
            f"completed k={k:2d}, states={h.size:9d}, max_h={max_h:6d}, "
            f"complete_phi_prefix={prefix:5d}",
            flush=True,
        )

    raw_fields = [
        "cutoff_k",
        "state_count",
        "max_h",
        "grid_id",
        "sigma",
        "tau",
        "observable",
        "seed",
        "value_re",
        "value_im",
        "abs_value",
        "target_re",
        "target_im",
        "target_abs_error",
        "target_status",
        "successive_k_drift",
        "precision_mode",
    ]
    write_csv(output_dir / "raw_observables.csv", rows, raw_fields)
    final_grid_rows = [
        row
        for row in rows
        if row["cutoff_k"] == max_k
        and row["observable"] in ("unsigned", "liouville")
        and row["seed"] == "none"
    ]
    write_csv(
        output_dir / "final_grid_analytic_errors.csv", final_grid_rows, raw_fields
    )
    diagnostic_fields = list(diagnostics[0].keys())
    write_csv(output_dir / "cutoff_diagnostics.csv", diagnostics, diagnostic_fields)
    seed_fields = list(seed_ledger[0].keys())
    write_csv(output_dir / "seed_ledger.csv", seed_ledger, seed_fields)

    # Arbitrary-precision audit of the two objects with known zeta-ratio targets.
    lookup = {
        (int(row["cutoff_k"]), str(row["observable"]), str(row["grid_id"])): complex(
            float(row["value_re"]), float(row["value_im"])
        )
        for row in rows
        if row["seed"] == "none"
    }
    precision_rows: list[dict[str, Any]] = []
    for k in sorted(audit_coefficients):
        for observable, coefficients in audit_coefficients[k].items():
            for point in grid:
                s = complex(float(point["sigma"]), float(point["tau"]))
                values: dict[str, tuple[str, str]] = {
                    "numpy_complex128": (
                        repr(lookup[(k, observable, str(point["id"]))].real),
                        repr(lookup[(k, observable, str(point["id"]))].imag),
                    )
                }
                for dps in audit_dps:
                    values[f"mpmath_{dps}dps"] = evaluate_dirichlet_mpmath(
                        coefficients, s, dps
                    )
                reference_text = values["mpmath_100dps"]
                with mp.workdps(110):
                    reference = mp.mpc(
                        mp.mpf(reference_text[0]), mp.mpf(reference_text[1])
                    )
                    for method, (value_re, value_im) in values.items():
                        value = mp.mpc(mp.mpf(value_re), mp.mpf(value_im))
                        difference = abs(value - reference)
                        precision_rows.append(
                            {
                                "cutoff_k": k,
                                "grid_id": point["id"],
                                "sigma": s.real,
                                "tau": s.imag,
                                "observable": observable,
                                "method": method,
                                "value_re": value_re,
                                "value_im": value_im,
                                "abs_diff_vs_mpmath_100": mp.nstr(difference, n=40),
                            }
                        )
        print(f"completed precision audit k={k}", flush=True)

    precision_fields = [
        "cutoff_k",
        "grid_id",
        "sigma",
        "tau",
        "observable",
        "method",
        "value_re",
        "value_im",
        "abs_diff_vs_mpmath_100",
    ]
    write_csv(output_dir / "precision_audit.csv", precision_rows, precision_fields)

    summary = summarize(rows, diagnostics, precision_rows, max_k)
    summary["protocol_sha256"] = protocol_hash
    summary["elapsed_seconds"] = time.time() - started
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    metadata = {
        "protocol_path": str(args.protocol.resolve()),
        "protocol_sha256": protocol_hash,
        "results_dir": str(output_dir.resolve()),
        "started_unix_utc": started,
        "finished_unix_utc": time.time(),
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "mpmath": mpmath.__version__,
        "pid": os.getpid(),
        "argv": sys.argv,
    }
    (output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
