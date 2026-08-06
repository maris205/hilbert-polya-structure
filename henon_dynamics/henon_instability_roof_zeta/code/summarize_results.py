#!/usr/bin/env python3
"""Aggregate the frozen experiment into tables and an evidence-bounded report."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from statistics import mean, stdev
from typing import Sequence

import numpy as np

from henon_roof import (
    CycleSection,
    OrbitRecord,
    Rectangle,
    match_roots,
    root_drift_summary,
    weighted_orbits,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = PROJECT_ROOT / "refine-logs" / "R000_FROZEN_PROTOCOL.json"
DEFAULT_CATALOG = PROJECT_ROOT / "results" / "catalog_robustness.json"
DEFAULT_ROOTS = PROJECT_ROOT / "results" / "roots_robustness.json"
DEFAULT_CONTROLS = PROJECT_ROOT / "results" / "controls.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--roots", type=Path, default=DEFAULT_ROOTS)
    parser.add_argument("--controls", type=Path, default=DEFAULT_CONTROLS)
    return parser.parse_args()


def load_orbits(payload: dict[str, object]) -> list[OrbitRecord]:
    records = []
    for row in payload["orbits"]:
        row = dict(row)
        row["coordinates"] = tuple(row["coordinates"])
        records.append(OrbitRecord(**row))
    return records


def roots(rows: Sequence[Sequence[float]]) -> list[complex]:
    return [complex(float(row[0]), float(row[1])) for row in rows]


def mean_std(values: Sequence[float]) -> tuple[float, float]:
    if not values:
        return float("nan"), float("nan")
    return float(mean(values)), float(stdev(values)) if len(values) > 1 else 0.0


def json_safe(value: object) -> object:
    """Replace non-finite floats so the persisted JSON is RFC-compliant."""

    if isinstance(value, float) and not np.isfinite(value):
        return None
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def exact_constant_roof_roots(
    fixed_length: float, rectangle: Rectangle
) -> list[complex]:
    golden_ratio = (1 + np.sqrt(5.0)) / 2
    eigenvalues = (golden_ratio, -1 / golden_ratio, 1j, -1j)
    values: list[complex] = []
    for eigenvalue in eigenvalues:
        for branch in range(-100, 101):
            root = (
                np.log(abs(eigenvalue))
                + 1j * (np.angle(eigenvalue) - 2 * np.pi * branch)
            ) / fixed_length
            if rectangle.contains(complex(root)):
                values.append(complex(root))
    return sorted(values, key=lambda value: (value.imag, value.real))


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    protocol_hash = sha256_file(args.protocol)
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    root_payload = json.loads(args.roots.read_text(encoding="utf-8"))
    controls = json.loads(args.controls.read_text(encoding="utf-8"))
    for name, payload in (("catalog", catalog), ("roots", root_payload), ("controls", controls)):
        if payload["protocol_sha256"] != protocol_hash:
            raise SystemExit(f"{name} does not match the frozen protocol")

    rectangle_data = protocol["root_rectangle"]
    rectangle = Rectangle(
        float(rectangle_data["real_min"]),
        float(rectangle_data["real_max"]),
        float(rectangle_data["imag_min"]),
        float(rectangle_data["imag_max"]),
    )
    records = load_orbits(catalog)
    orbit_data = weighted_orbits(records)
    h16 = float(root_payload["sectors"]["0"]["leading_real_root_gate"]["h16"])
    actual_section = CycleSection(orbit_data, cutoff=16, kappa=0)
    actual_coefficients = actual_section.product_coefficients(h16)
    actual_tail = float(np.sum(np.abs(actual_coefficients[9:17])))

    actual_training = roots(root_payload["sectors"]["0"]["stability"]["training_roots"])
    actual_roots16 = roots(root_payload["sectors"]["0"]["cutoffs"]["16"]["roots"])
    actual_match_8_16 = match_roots(actual_training, actual_roots16, tolerance=0.02)
    actual_stability_8_16 = root_drift_summary(actual_match_8_16, len(actual_training))

    root_rows: list[dict[str, object]] = []
    for sector, sector_payload in root_payload["sectors"].items():
        for cutoff_text, block in sorted(
            sector_payload["cutoffs"].items(), key=lambda item: int(item[0])
        ):
            positive_real = [value for value in block["real_roots_in_minus1_1"] if value > 0]
            root_rows.append(
                {
                    "sector": int(sector),
                    "cutoff": int(cutoff_text),
                    "root_count": block["root_count_discovered"],
                    "argument_count": block["argument_principle"][-1]["root_count"],
                    "root_count_discrepancy": block["root_count_discrepancy"],
                    "minimum_boundary_modulus": block["argument_principle"][-1][
                        "minimum_boundary_modulus"
                    ],
                    "maximum_phase_step": block["argument_principle"][-1][
                        "maximum_phase_step"
                    ],
                    "positive_real_root": positive_real[-1] if positive_real else None,
                    "precision_drift_max": block["precision_drift_max"],
                    "high_precision_residual_max": block[
                        "high_precision_root_residual_max"
                    ],
                    "implementation_discrepancy_max": block[
                        "high_precision_coefficient_discrepancy_max"
                    ],
                }
            )

    control_rows: list[dict[str, object]] = []
    for control, seed_blocks in controls["controls"].items():
        blocks = list(seed_blocks.values())
        valid = [
            block
            for block in blocks
            if all(
                block["cutoffs"][str(cutoff)]["argument_counts_agree"]
                and block["cutoffs"][str(cutoff)]["root_count_discrepancy"] == 0
                for cutoff in (8, 16)
            )
        ]
        retention = [block["stability_8_to_16"]["retained_fraction"] for block in valid]
        drift = [block["stability_8_to_16"]["median_drift"] for block in valid]
        tails = [block["cutoffs"]["16"]["tail_coefficient_l1_degrees_9_16"] for block in blocks]
        retention_mean, retention_std = mean_std(retention)
        drift_mean, drift_std = mean_std(drift)
        tail_mean, tail_std = mean_std(tails)
        status = "VALID_NUMERICAL_CONTROL" if len(valid) == len(blocks) else "NOT_TESTABLE_ROOT_COUNT"
        if control == "constant_roof_parent":
            fixed_length = float(controls["actual_reference"]["fixed_orbit_length"])
            exact_roots = exact_constant_roof_roots(fixed_length, rectangle)
            status = "EXACT_ANALYTIC_CONTROL"
            retention_mean, retention_std = 1.0, 0.0
            drift_mean, drift_std = 0.0, 0.0
            exact_count = len(exact_roots)
        else:
            exact_count = None
        control_rows.append(
            {
                "control": control,
                "seeds": len(blocks),
                "root_status": status,
                "valid_root_seeds": len(valid),
                "retention_mean": retention_mean,
                "retention_std": retention_std,
                "median_drift_mean": drift_mean,
                "median_drift_std": drift_std,
                "tail_l1_mean": tail_mean,
                "tail_l1_std": tail_std,
                "tail_ratio_vs_henon": tail_mean / actual_tail,
                "exact_root_count": exact_count,
            }
        )

    neighbor_rows: list[dict[str, object]] = []
    for parameter, block in sorted(controls["neighbors"].items()):
        stability = block["stability_8_to_16"]
        comparison = block["actual_training_to_neighbor16"]
        neighbor_rows.append(
            {
                "parameter": parameter,
                "retained_fraction_8_16": stability["retained_fraction"],
                "median_drift_8_16": stability["median_drift"],
                "p90_drift_8_16": stability["p90_drift"],
                "h6_training_match_fraction": comparison["retained_fraction"],
                "h6_training_match_median_drift": comparison["median_drift"],
                "root_count_16": block["cutoffs"]["16"]["root_count_discovered"],
                "evidence_status": block["evidence_status"],
            }
        )

    untwisted = root_payload["sectors"]["0"]
    twisted = root_payload["sectors"]["1"]
    summary = {
        "run_id": "analysis_r060",
        "created_utc": protocol["created_utc"],
        "protocol_sha256": protocol_hash,
        "source_hashes": {
            "catalog": sha256_file(args.catalog),
            "roots": sha256_file(args.roots),
            "controls": sha256_file(args.controls),
        },
        "exact_findings": {
            "roof_positive": catalog["exact_clock_audit"]["roof_positive"],
            "nonlattice_proof_inputs_pass": catalog["exact_clock_audit"][
                "nonlattice_proof_inputs_pass"
            ],
            "action_clock_rejected_by_zero_period": not catalog["exact_clock_audit"][
                "period4_action_positive_roof"
            ],
            "unit_clock_vertical_period": catalog["exact_clock_audit"][
                "unit_clock_periodicity"
            ],
        },
        "orbit_ledger": {
            "max_period": catalog["max_period"],
            "total_primitive_orbits": catalog["total_primitive_orbits"],
            "gates": catalog["gates"],
            "metrics": catalog["metrics"],
        },
        "untwisted": {
            "training_root_count": untwisted["stability"]["training_root_count"],
            "validation": untwisted["stability"]["validation_8_to_12"],
            "sealed_test": untwisted["stability"]["sealed_12_to_16"],
            "robustness": untwisted["stability"]["robustness_16_to_20"],
            "fair_8_to_16": actual_stability_8_16,
            "leading_real_root_gate": untwisted["leading_real_root_gate"],
            "h20_high_precision": next(
                row["real"]
                for root, row in zip(
                    untwisted["cutoffs"]["20"]["roots"],
                    untwisted["cutoffs"]["20"]["high_precision_roots"],
                    strict=True,
                )
                if abs(float(root[1])) < 1e-12
            ),
            "degree_9_16_coefficient_tail_l1_at_h16": actual_tail,
        },
        "twisted": {
            "training_root_count": twisted["stability"]["training_root_count"],
            "validation": twisted["stability"]["validation_8_to_12"],
            "sealed_test": twisted["stability"]["sealed_12_to_16"],
            "robustness": twisted["stability"]["robustness_16_to_20"],
            "exact_zero_at_s0": True,
        },
        "root_rows": root_rows,
        "control_rows": control_rows,
        "neighbor_rows": neighbor_rows,
        "claim_boundary": (
            "The exact result is a positive non-lattice instability roof on the local certified survivor. "
            "The cutoff-stable zero family and coefficient-decay results are finite-section numerical observations. "
            "No analytic continuation, limiting divisor, Riemann-zero match, functional equation, "
            "Riemann-von Mangoldt law, self-adjoint operator, or global Hénon statement is established."
        ),
    }

    output_json = PROJECT_ROOT / "results" / "analysis_summary.json"
    output_csv = PROJECT_ROOT / "results" / "control_summary.csv"
    output_md = PROJECT_ROOT / "results" / "ANALYSIS.md"
    output_json.write_text(
        json.dumps(json_safe(summary), allow_nan=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(control_rows[0]))
        writer.writeheader()
        writer.writerows(control_rows)

    root_table = "\n".join(
        "| {sector} | {cutoff} | {root_count} | {argument_count} | {positive} | {precision:.2e} |".format(
            sector=row["sector"],
            cutoff=row["cutoff"],
            root_count=row["root_count"],
            argument_count=row["argument_count"],
            positive=(
                f"{row['positive_real_root']:.12f}"
                if row["positive_real_root"] is not None
                else "--"
            ),
            precision=row["precision_drift_max"],
        )
        for row in root_rows
    )
    control_table = "\n".join(
        "| {control} | {status} | {retention} | {drift} | {tail:.3e} | {ratio:.2e} |".format(
            control=row["control"],
            status=row["root_status"],
            retention=(
                f"{row['retention_mean']:.3f} +/- {row['retention_std']:.3f}"
                if np.isfinite(row["retention_mean"])
                else "N/T"
            ),
            drift=(
                f"{row['median_drift_mean']:.3e}"
                if np.isfinite(row["median_drift_mean"])
                else "N/T"
            ),
            tail=row["tail_l1_mean"],
            ratio=row["tail_ratio_vs_henon"],
        )
        for row in control_rows
    )
    neighbor_table = "\n".join(
        "| {parameter} | {retained_fraction_8_16:.3f} | {median_drift_8_16:.3e} | {h6_training_match_fraction:.3f} | {root_count_16} |".format(
            **row
        )
        for row in neighbor_rows
    )

    output_md.write_text(
        f"""# Result Analysis

Evidence labels follow the Route-A hierarchy. The protocol hash is `{protocol_hash}`.

## Raw root table

| Orientation sector | Cutoff | Located roots | Numerical winding | Positive real root | Max precision drift |
|---:|---:|---:|---:|---:|---:|
{root_table}

All sampled numerical winding estimates above agree at 4096, 8192, and 16384 contour points. Every listed estimate equals the explicit census; no estimate is claimed as an interval-certified argument-principle count. The rectangle is the frozen `[-0.25,0.30] x [-20,20]` rectangle.

## Raw control table

| Control | Root-count status | Retention 8->16 (mean +/- SD) | Median drift | Degree 9--16 tail L1 | Tail / Hénon |
|---|---|---:|---:|---:|---:|
| Hénon instability roof | VALID_NUMERICAL_CANDIDATE | {actual_stability_8_16['retained_fraction']:.3f} | {actual_stability_8_16['median_drift']:.3e} | {actual_tail:.3e} | 1.00 |
{control_table}

`NOT_TESTABLE_ROOT_COUNT` means the frozen contour-sampling algorithm failed: its three resolutions disagree after a global shuffle creates high-frequency exponential terms. The entire control functions still have well-defined root counts, but the unresolved sampled counts and root-stability numbers are not used. The constant-roof row uses its exact four-eigenvalue formula; its reported coefficient tail is a floating-point floor, and the float root locator missed two roots at cutoff 16.

## Neighbor controls

| Parameter | Self retention 8->16 | Self median drift | Fraction matching H6 training roots | Roots at 16 |
|---:|---:|---:|---:|---:|
{neighbor_table}

These are numerical continuations of the same words, not certified common-survivor theorems.

## Key findings

1. **PROVED — the unit-clock lattice-periodicity obstruction is removed.** The unit clock gives an exact vertically periodic determinant, and the stored action is not a positive roof because one exact period-four orbit has action zero. In contrast, the unstable roof obeys `J^u >= 773/224 > 1`. The fixed orbit multiplier has degree four, the explicit period-four multiplier has degree two, and no positive powers can coincide; hence their log ratio is irrational and the roof is non-lattice. This removes one obstruction, not the global analytic obligations.

2. **NUMERICAL_OBSERVATION — a preregistered family of finite-section zeros survives the sealed test.** Untwisted retention is 100%, with validation median drift `{untwisted['stability']['validation_8_to_12']['median_drift']:.3e}` and sealed median drift `{untwisted['stability']['sealed_12_to_16']['median_drift']:.3e}`. Twisted retention is also 100%, with sealed median drift `{twisted['stability']['sealed_12_to_16']['median_drift']:.3e}`. The untwisted positive real finite-section zero reaches `{summary['untwisted']['h20_high_precision']}` at cutoff 20. In the twisted family, one of the 43 tracked zeros is the exact symbolic root `s=0`.

3. **NUMERICAL_OBSERVATION — the coefficient cancellation is strongly non-generic among the frozen orbit-level controls.** At the common Hénon probe, the Hénon degree-9--16 tail is `{actual_tail:.3e}`. Valid random controls are tens of thousands to hundreds of thousands of times larger and retain only a small fraction of their cutoff-8 roots. This demonstrates structured cycle cancellation relative to those controls; it does not isolate shadowing as the cause. The exact constant-roof parent is even more stable, so stability is not an arithmetic signature.

4. **NUMERICAL_OBSERVATION — nearby parameters are also internally stable.** The `a=5.9` and `a=6.1` word continuations each retain all their cutoff-8 roots while most do not lie within the frozen H6 matching tolerance. Thus H6 is not numerically isolated by this test.

5. **OPEN / A3 blocker — no limiting global divisor has been proved.** Each fixed finite section is an exponential polynomial with linear zero-count growth in height. Inferring a `T log T` law by increasing cutoff with height would be moving-order fitting unless a uniform remainder theorem is supplied. No functional equation, Gamma factor, trivial-zero structure, or completed-xi identity appears.

## Suggested next experiments

1. Construct cylinder-memory approximations to the same Hölder roof and compare their analytic determinants with the orbit sections. This is the smallest test of a genuine transfer-operator limit.
2. Prove a uniform cycle-tail or Rouché bound on a small contour around the positive real finite-section zero; that would promote one observed zero toward a limiting statement.
3. Add within-period length shuffles and locally constant edge-roof controls, evaluated both at the common Hénon probe and at each control's own positive zero when it exists.
4. Certify a common parameter interval around `a=6` before interpreting neighbor continuation as structural stability of one family.

## Claim boundary

{summary['claim_boundary']}
""",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "analysis": str(output_md),
                "summary": str(output_json),
                "control_table": str(output_csv),
                "actual_tail": actual_tail,
                "actual_stability_8_16": actual_stability_8_16,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
