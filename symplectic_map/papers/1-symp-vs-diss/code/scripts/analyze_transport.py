#!/usr/bin/env python3
"""Cluster-aware comparison of a frozen transport run and neighbor controls."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any

import numpy as np


CODE_ROOT = Path(__file__).resolve().parents[1]
PAPER_ROOT = CODE_ROOT.parent
sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.analysis import (  # noqa: E402
    ClusterBlock,
    fixed_grid_transition,
    holm_adjust,
    paired_cluster_bootstrap,
)


CONTROL_TAGS = ("a150", "a152", "a156", "a158")
CONTROL_A = {"a150": 1.50, "a152": 1.52, "a156": 1.56, "a158": 1.58}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split", choices=("validation", "test"), required=True)
    parser.add_argument("--bootstrap-replicates", type=int, default=2000)
    parser.add_argument("--output-stem", default=None)
    return parser.parse_args()


def run_stems(split: str) -> tuple[str, dict[str, str]]:
    return (
        f"transport_{split}_frozen_v2",
        {tag: f"transport_{split}_neighbor_{tag}_v2" for tag in CONTROL_TAGS},
    )


def read_payload(stem: str) -> dict[str, Any]:
    path = PAPER_ROOT / "results" / "transport" / f"{stem}.json"
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def read_clusters(stem: str) -> dict[float, ClusterBlock]:
    path = PAPER_ROOT / "results" / "transport" / f"{stem}_clusters.csv"
    grouped: dict[float, list[dict[str, str]]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            grouped.setdefault(float(row["rho"]), []).append(row)
    return {
        rho: ClusterBlock(
            trajectory_id=np.array([int(row["trajectory_id"]) for row in rows]),
            exposure_steps=np.array([int(row["exposure_steps"]) for row in rows]),
            survived=np.array([bool(int(row["survived"])) for row in rows]),
            even_gaps=np.array([int(row["even_gaps"]) for row in rows]),
            odd_gaps=np.array([int(row["odd_gaps"]) for row in rows]),
        )
        for rho, rows in grouped.items()
    }


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ledger_summary(filename: str) -> dict[str, Any]:
    path = PAPER_ROOT / "results" / filename
    with path.open(encoding="utf-8") as handle:
        run = json.load(handle)["runs"][0]
    return {
        "path": str(path.relative_to(PAPER_ROOT)),
        "sha256": file_hash(path),
        "parameters": run["parameters"],
        "completeness_status": run["completeness_status"],
        "period_counts": [
            {
                "period": row["period"],
                "found": row["orbits_found"],
                "binary_necklaces": row["binary_primitive_necklaces"],
            }
            for row in run["periods"]
        ],
    }


def audit_summary(filename: str) -> dict[str, Any]:
    path = PAPER_ROOT / "results" / filename
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    orbits = [
        orbit
        for run in data["runs"]
        for period in run["periods"]
        for orbit in period.get("orbits", [])
    ]
    return {
        "path": str(path.relative_to(PAPER_ROOT)),
        "sha256": file_hash(path),
        "audit_kind": data["audit_kind"],
        "interval_certification": data["interval_certification"],
        "orbit_count": len(orbits),
        "all_refinements_converged": all(o["refinement_converged"] for o in orbits),
        "maximum_refined_residual": max(float(o["refined_residual_inf"]) for o in orbits),
        "maximum_determinant_absolute_error": max(float(o["determinant_absolute_error"]) for o in orbits),
    }


def json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, (np.floating, float)):
        number = float(value)
        return number if math.isfinite(number) else None
    return value


def write_table(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    if args.bootstrap_replicates <= 0:
        raise ValueError("--bootstrap-replicates must be positive")
    primary_stem, control_stems = run_stems(args.split)
    primary = read_payload(primary_stem)
    controls = {tag: read_payload(stem) for tag, stem in control_stems.items()}
    primary_clusters = read_clusters(primary_stem)
    control_clusters = {tag: read_clusters(stem) for tag, stem in control_stems.items()}
    horizon = int(primary["parameters"]["horizon"])

    raw_rows: list[dict[str, Any]] = []
    arms = [("frozen_uc", primary["parameters"]["a"], primary)] + [
        (tag, CONTROL_A[tag], controls[tag]) for tag in CONTROL_TAGS
    ]
    for arm, a, payload in arms:
        for row in payload["results"]:
            raw_rows.append(
                {
                    "split": args.split,
                    "arm": arm,
                    "a": a,
                    "rho": row["rho"],
                    "parity_polarity": row["parity_polarity"],
                    "parity_ci_low": row["parity_polarity_ci_low"],
                    "parity_ci_high": row["parity_polarity_ci_high"],
                    "markov_null_polarity": row["markov_null_polarity"],
                    "exposure_fraction": row["exposure_fraction"],
                    "survival_fraction": row["survival_fraction"],
                    "total_gaps": row["total_gaps"],
                }
            )

    comparisons: list[dict[str, Any]] = []
    for rho_index, rho in enumerate(sorted(primary_clusters)):
        for control_index, tag in enumerate(CONTROL_TAGS):
            result = paired_cluster_bootstrap(
                primary_clusters[rho],
                control_clusters[tag][rho],
                horizon=horizon,
                n_replicates=args.bootstrap_replicates,
                seed=2026081200 + 101 * rho_index + control_index,
            )
            comparisons.append(
                {
                    "split": args.split,
                    "rho": rho,
                    "control": tag,
                    "control_a": CONTROL_A[tag],
                    **result,
                }
            )

    endpoint_rows = [row for row in comparisons if row["rho"] == 1.0]
    raw_p = {
        row["control"]: row["polarity_one_sided_bootstrap_p"]
        for row in endpoint_rows
    }
    adjusted_p = holm_adjust(raw_p)
    for row in comparisons:
        row["holm_adjusted_p_endpoint"] = (
            adjusted_p[row["control"]] if row["rho"] == 1.0 else None
        )
    specificity_passed = all(
        row["polarity_difference"] > 0.0
        and row["polarity_difference_ci_low"] > 0.0
        and adjusted_p[row["control"]] < 0.05
        for row in endpoint_rows
    )

    endpoint = next(row for row in primary["results"] if row["rho"] == 1.0)
    availability_passed = (
        endpoint["exposure_fraction"] >= 0.8 and endpoint["total_gaps"] >= 10000
    )
    polarity_passed = endpoint["parity_polarity_ci_low"] >= 0.98
    if not availability_passed:
        decision = "A0_SHADOW_FAIL_CARRIER_UNAVAILABLE"
    elif not polarity_passed:
        decision = "A0_SHADOW_FAIL_POLARITY"
    elif not specificity_passed:
        decision = "A0_SHADOW_FAIL_NONSPECIFIC_PROVES_TOO_MUCH"
    else:
        decision = "ROBUST_WEAK_SHADOW"

    result_payload = {
        "schema_version": 1,
        "split": args.split,
        "primary_stem": primary_stem,
        "control_stems": control_stems,
        "bootstrap_replicates": args.bootstrap_replicates,
        "paired_unit": "common-random-number trajectory id",
        "directional_tail_warning": "bootstrap sign-tail diagnostic, not an exact randomized-treatment p-value",
        "holm_family": "four one-sided frozen-u_c minus neighbor polarity contrasts at rho=1",
        "endpoint": {
            "rho": 1.0,
            "exposure_fraction": endpoint["exposure_fraction"],
            "total_gaps": endpoint["total_gaps"],
            "parity_polarity": endpoint["parity_polarity"],
            "parity_ci": [endpoint["parity_polarity_ci_low"], endpoint["parity_polarity_ci_high"]],
            "availability_passed": availability_passed,
            "polarity_passed": polarity_passed,
            "neighbor_specificity_passed": specificity_passed,
            "holm_adjusted_p": adjusted_p,
            "formal_decision": decision,
        },
        "transition_on_frozen_grid": fixed_grid_transition(
            primary["results"], exposure_gate=0.8
        ),
        "small_rho_proves_too_much_observation": (
            "All four neighbors attain polarity above 0.997 at rho=0.1 and 0.2; the pattern is not u_c-specific."
        ),
        "ledgers": {
            "positive_control": ledger_summary("ledger_positive_a6_rho1_n10.json"),
            "frozen_exploratory": ledger_summary("ledger_uc_rho1_n8_exploratory.json"),
        },
        "high_precision_audits": {
            "positive_control": audit_summary("ledger_positive_a6_rho1_n10_audit80.json"),
            "frozen_exploratory": audit_summary("ledger_uc_rho1_n8_audit80.json"),
        },
        "raw_rows": raw_rows,
        "paired_comparisons": comparisons,
    }

    output_dir = PAPER_ROOT / "results" / "analysis"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_stem = args.output_stem or f"transport_{args.split}_analysis_v1"
    json_path = output_dir / f"{output_stem}.json"
    raw_path = output_dir / f"{output_stem}_raw.csv"
    paired_path = output_dir / f"{output_stem}_paired.csv"
    json_path.write_text(
        json.dumps(json_safe(result_payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_table(raw_path, raw_rows)
    write_table(paired_path, comparisons)
    print(json.dumps(result_payload["endpoint"], indent=2, sort_keys=True))
    print(f"wrote {json_path}")
    print(f"wrote {raw_path}")
    print(f"wrote {paired_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

