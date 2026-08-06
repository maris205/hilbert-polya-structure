#!/usr/bin/env python3
"""Frozen complex-root census for instability-roof cycle sections."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Sequence

import mpmath as mp
import numpy as np

from henon_roof import (
    CycleSection,
    OrbitRecord,
    Rectangle,
    WeightedOrbit,
    argument_principle_count,
    complex_pair,
    discover_roots,
    match_roots,
    mp_cycle_coefficients,
    mp_determinant,
    nearest_real_root,
    root_drift_summary,
    weighted_orbits,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = PROJECT_ROOT / "refine-logs" / "R000_FROZEN_PROTOCOL.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--label", type=str, required=True)
    parser.add_argument("--cutoffs", nargs="+", type=int, default=[7, 8, 10, 12, 14, 16, 18, 20])
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--real-step", type=float, default=0.01)
    parser.add_argument("--imag-step", type=float, default=0.025)
    return parser.parse_args()


def load_catalog(path: Path) -> tuple[dict[str, object], list[OrbitRecord]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = []
    for row in payload["orbits"]:
        row = dict(row)
        row["coordinates"] = tuple(row["coordinates"])
        records.append(OrbitRecord(**row))
    return payload, records


def refine_high_precision_root(
    orbits: Sequence[WeightedOrbit],
    cutoff: int,
    kappa: int,
    root: complex,
    dps: int,
) -> dict[str, object]:
    with mp.workdps(dps):
        initial = mp.mpc(root.real, root.imag)

        def determinant(value: mp.mpc) -> mp.mpc:
            return mp_determinant(orbits, cutoff, value, kappa, dps=dps, method="product")

        try:
            refined = mp.findroot(
                determinant,
                (initial, initial + mp.mpc("1e-10", "1e-10")),
                tol=mp.mpf(10) ** (-(dps - 15)),
                maxsteps=80,
            )
        except (ValueError, ZeroDivisionError):
            refined = initial
        product_coefficients = mp_cycle_coefficients(
            orbits, cutoff, refined, kappa, dps=dps, method="product"
        )
        trace_coefficients = mp_cycle_coefficients(
            orbits, cutoff, refined, kappa, dps=dps, method="trace"
        )
        product_value = sum(product_coefficients)
        trace_value = sum(trace_coefficients)
        coefficient_discrepancy = max(
            abs(left - right)
            for left, right in zip(product_coefficients, trace_coefficients, strict=True)
        )
        return {
            "real": mp.nstr(refined.real, dps),
            "imag": mp.nstr(refined.imag, dps),
            "product_residual": mp.nstr(abs(product_value), 20),
            "trace_residual": mp.nstr(abs(trace_value), 20),
            "coefficient_discrepancy": mp.nstr(coefficient_discrepancy, 20),
            "float_to_high_precision_shift": float(
                abs(refined - mp.mpc(root.real, root.imag))
            ),
        }


def conjugation_residual(roots: Sequence[complex]) -> float:
    if not roots:
        return 0.0
    return float(max(min(abs(root.conjugate() - other) for other in roots) for root in roots))


def cutoff_block(
    orbits: Sequence[WeightedOrbit],
    cutoff: int,
    kappa: int,
    rectangle: Rectangle,
    contour_samples: Sequence[int],
    dps: int,
    real_step: float,
    imag_step: float,
) -> dict[str, object]:
    section = CycleSection(orbits, cutoff=cutoff, kappa=kappa)
    roots = discover_roots(
        section,
        rectangle,
        real_step=real_step,
        imag_step=imag_step,
    )
    contour = [argument_principle_count(section, rectangle, samples) for samples in contour_samples]
    probes = [0.11 + 1.37j, -0.07 + 7.91j, 0.23 + 15.17j]
    implementation_discrepancies = [section.implementation_discrepancy(probe) for probe in probes]
    refined = [
        refine_high_precision_root(orbits, cutoff, kappa, root, dps=dps)
        for root in roots
    ]
    return {
        "cutoff": cutoff,
        "kappa": kappa,
        "orbit_count": len(section.orbits),
        "roots": [complex_pair(root) for root in roots],
        "root_count_discovered": len(roots),
        "argument_principle": contour,
        "argument_counts_agree": len({row["root_count"] for row in contour}) == 1,
        "root_count_discrepancy": int(contour[-1]["root_count"] - len(roots)),
        "conjugation_residual": conjugation_residual(roots),
        "real_roots_in_minus1_1": nearest_real_root(section),
        "float_implementation_discrepancy_max": max(implementation_discrepancies),
        "float_implementation_discrepancies": implementation_discrepancies,
        "high_precision_roots": refined,
        "high_precision_root_residual_max": max(
            (float(row["product_residual"]) for row in refined), default=0.0
        ),
        "high_precision_coefficient_discrepancy_max": max(
            (float(row["coefficient_discrepancy"]) for row in refined), default=0.0
        ),
        "precision_drift_max": max(
            (row["float_to_high_precision_shift"] for row in refined), default=0.0
        ),
    }


def roots(block: dict[str, object]) -> list[complex]:
    return [complex(float(row[0]), float(row[1])) for row in block["roots"]]


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    protocol_hash = sha256_file(args.protocol)
    catalog_payload, records = load_catalog(args.catalog)
    if catalog_payload["protocol_sha256"] != protocol_hash:
        raise SystemExit("catalog and root analysis do not share the frozen protocol hash")
    max_period = int(catalog_payload["max_period"])
    cutoffs = sorted(set(cutoff for cutoff in args.cutoffs if cutoff <= max_period))
    required = {7, 8}
    if not required.issubset(cutoffs):
        raise SystemExit("cutoffs 7 and 8 are required to define the frozen training root set")

    rectangle_payload = protocol["root_rectangle"]
    rectangle = Rectangle(
        real_min=float(rectangle_payload["real_min"]),
        real_max=float(rectangle_payload["real_max"]),
        imag_min=float(rectangle_payload["imag_min"]),
        imag_max=float(rectangle_payload["imag_max"]),
    )
    contour_samples = [int(value) for value in protocol["contour_samples"]]
    dps = int(protocol["root_check_precision_dps"])
    orbit_data = weighted_orbits(records)

    sectors: dict[str, object] = {}
    csv_rows: list[dict[str, object]] = []
    for kappa in (0, 1):
        blocks: dict[int, dict[str, object]] = {}
        for cutoff in cutoffs:
            block = cutoff_block(
                orbit_data,
                cutoff,
                kappa,
                rectangle,
                contour_samples,
                dps,
                args.real_step,
                args.imag_step,
            )
            blocks[cutoff] = block
            for index, value in enumerate(roots(block)):
                csv_rows.append(
                    {
                        "kappa": kappa,
                        "cutoff": cutoff,
                        "root_index": index,
                        "real": value.real,
                        "imag": value.imag,
                        "high_precision_real": block["high_precision_roots"][index]["real"],
                        "high_precision_imag": block["high_precision_roots"][index]["imag"],
                        "high_precision_residual": block["high_precision_roots"][index]["product_residual"],
                    }
                )

        roots7 = roots(blocks[7])
        roots8 = roots(blocks[8])
        training_match = match_roots(roots7, roots8, float(protocol["root_match_tolerance"]))
        retained_target_indices = {
            int(row["target_index"])
            for row in training_match["matches"]
            if rectangle.boundary_distance(roots8[int(row["target_index"])])
            >= float(protocol["training_boundary_margin"])
        }
        training_roots = [
            value for index, value in enumerate(roots8) if index in retained_target_indices
        ]

        stability: dict[str, object] = {
            "training_7_to_8": root_drift_summary(training_match, len(roots7)),
            "training_root_count": len(training_roots),
            "training_roots": [complex_pair(value) for value in training_roots],
        }

        validation_roots: list[complex] = []
        if 12 in blocks:
            validation_match = match_roots(
                training_roots,
                roots(blocks[12]),
                float(protocol["root_match_tolerance"]),
            )
            validation_summary = root_drift_summary(validation_match, len(training_roots))
            validation_roots = [
                roots(blocks[12])[int(row["target_index"])]
                for row in validation_match["matches"]
            ]
            gates = protocol["validation_gates"]
            validation_summary["gate_pass"] = bool(
                validation_summary["retained_fraction"] >= float(gates["retained_fraction_min"])
                and validation_summary["median_drift"] <= float(gates["median_drift_max"])
                and validation_summary["p90_drift"] <= float(gates["p90_drift_max"])
            )
            stability["validation_8_to_12"] = validation_summary

        if 16 in blocks and validation_roots:
            sealed_match = match_roots(
                validation_roots,
                roots(blocks[16]),
                float(protocol["root_match_tolerance"]),
            )
            sealed_summary = root_drift_summary(sealed_match, len(validation_roots))
            gates = protocol["sealed_test_gates"]
            sealed_summary["gate_pass"] = bool(
                sealed_summary["retained_fraction"] >= float(gates["retained_fraction_min"])
                and sealed_summary["median_drift"] <= float(gates["median_drift_max"])
                and sealed_summary["p90_drift"] <= float(gates["p90_drift_max"])
            )
            stability["sealed_12_to_16"] = sealed_summary

        if 20 in blocks and 16 in blocks:
            robustness_match = match_roots(
                roots(blocks[16]),
                roots(blocks[20]),
                float(protocol["root_match_tolerance"]),
            )
            stability["robustness_16_to_20"] = root_drift_summary(
                robustness_match, len(roots(blocks[16]))
            )

        leading_root_gate: dict[str, object] | None = None
        if kappa == 0 and 10 in blocks and 12 in blocks:
            positive10 = [value for value in blocks[10]["real_roots_in_minus1_1"] if value > 0]
            positive12 = [value for value in blocks[12]["real_roots_in_minus1_1"] if value > 0]
            if positive10 and positive12:
                validation_drift = abs(positive12[-1] - positive10[-1])
                leading_root_gate = {
                    "h10": positive10[-1],
                    "h12": positive12[-1],
                    "validation_drift": validation_drift,
                    "validation_pass": validation_drift
                    <= float(protocol["validation_gates"]["untwisted_leading_real_root_drift_max"]),
                }
                if 16 in blocks:
                    positive16 = [
                        value for value in blocks[16]["real_roots_in_minus1_1"] if value > 0
                    ]
                    if positive16:
                        test_drift = abs(positive16[-1] - positive12[-1])
                        leading_root_gate.update(
                            {
                                "h16": positive16[-1],
                                "sealed_test_drift": test_drift,
                                "sealed_test_pass": test_drift
                                <= float(
                                    protocol["sealed_test_gates"][
                                        "untwisted_leading_real_root_drift_max"
                                    ]
                                ),
                            }
                        )

        sectors[str(kappa)] = {
            "cutoffs": {str(cutoff): block for cutoff, block in blocks.items()},
            "stability": stability,
            "leading_real_root_gate": leading_root_gate,
        }

    payload = {
        "run_id": f"roots_{args.label}",
        "created_utc": protocol["created_utc"],
        "candidate_id": protocol["candidate_id"],
        "protocol_path": str(args.protocol.relative_to(PROJECT_ROOT)),
        "protocol_sha256": protocol_hash,
        "catalog_path": str(args.catalog),
        "catalog_sha256": sha256_file(args.catalog),
        "catalog_max_period": max_period,
        "cutoffs": cutoffs,
        "determinant_convention": protocol["determinant"],
        "root_rectangle": rectangle_payload,
        "scope": "finite degree-in-z cycle sections at z=1; stable roots are numerical observations, not a proved limiting divisor",
        "sectors": sectors,
    }
    output_json = PROJECT_ROOT / "results" / f"roots_{args.label}.json"
    output_csv = PROJECT_ROOT / "results" / f"roots_{args.label}.csv"
    output_json.write_text(
        json.dumps(payload, allow_nan=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0]))
        writer.writeheader()
        writer.writerows(csv_rows)
    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "cutoffs": cutoffs,
                "protocol_sha256": protocol_hash,
                "stability": {
                    sector: block["stability"] for sector, block in sectors.items()
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
