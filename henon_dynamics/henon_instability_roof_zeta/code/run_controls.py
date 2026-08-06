#!/usr/bin/env python3
"""Run the frozen adversarial and neighboring-parameter control panel."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Sequence

import numpy as np

from henon_roof import (
    CycleSection,
    OrbitRecord,
    Rectangle,
    WeightedOrbit,
    argument_principle_count,
    complex_pair,
    discover_roots,
    make_control_orbits,
    match_roots,
    pressure_root_constant_roof,
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
    parser.add_argument("--root-results", type=Path, required=True)
    parser.add_argument("--neighbor-catalogs", nargs="*", type=Path, default=[])
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


def root_values(rows: Sequence[Sequence[float]]) -> list[complex]:
    return [complex(float(row[0]), float(row[1])) for row in rows]


def json_safe(value: object) -> object:
    """Map unmatched-root infinities to null for RFC 8259 JSON."""

    if isinstance(value, float) and not np.isfinite(value):
        return None
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def conjugation_residual(roots: Sequence[complex]) -> float:
    if not roots:
        return 0.0
    return float(max(min(abs(root.conjugate() - other) for other in roots) for root in roots))


def analyze_pair(
    orbits: Sequence[WeightedOrbit],
    rectangle: Rectangle,
    contour_samples: Sequence[int],
    real_step: float,
    imag_step: float,
    kappa: int = 0,
    coefficient_probe: float | complex = 0.27798298167628965,
) -> dict[str, object]:
    blocks: dict[int, dict[str, object]] = {}
    root_sets: dict[int, list[complex]] = {}
    for cutoff in (8, 16):
        section = CycleSection(orbits, cutoff=cutoff, kappa=kappa)
        roots = discover_roots(section, rectangle, real_step=real_step, imag_step=imag_step)
        contour = [
            argument_principle_count(section, rectangle, samples)
            for samples in contour_samples
        ]
        coefficients = section.product_coefficients(complex(coefficient_probe))
        trace_coefficients = section.trace_coefficients(complex(coefficient_probe))
        root_sets[cutoff] = roots
        blocks[cutoff] = {
            "cutoff": cutoff,
            "root_count_discovered": len(roots),
            "roots": [complex_pair(root) for root in roots],
            "argument_principle": contour,
            "argument_counts_agree": len({row["root_count"] for row in contour}) == 1,
            "root_count_discrepancy": int(contour[-1]["root_count"] - len(roots)),
            "conjugation_residual": conjugation_residual(roots),
            "coefficient_probe": [float(np.real(coefficient_probe)), float(np.imag(coefficient_probe))],
            "coefficient_abs": [float(abs(value)) for value in coefficients],
            "tail_coefficient_l1_degrees_9_16": float(np.sum(np.abs(coefficients[9:17]))),
            "coefficient_implementation_discrepancy": float(
                np.max(np.abs(coefficients - trace_coefficients))
            ),
        }
    match = match_roots(root_sets[8], root_sets[16], tolerance=0.02)
    return {
        "cutoffs": {str(key): value for key, value in blocks.items()},
        "stability_8_to_16": root_drift_summary(match, len(root_sets[8])),
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    protocol_hash = sha256_file(args.protocol)
    catalog_payload, records = load_catalog(args.catalog)
    if catalog_payload["protocol_sha256"] != protocol_hash:
        raise SystemExit("source catalogue does not match frozen protocol")
    if int(catalog_payload["max_period"]) < 16:
        raise SystemExit("control catalogue must include periods through 16")

    roots_payload = json.loads(args.root_results.read_text(encoding="utf-8"))
    if roots_payload["protocol_sha256"] != protocol_hash:
        raise SystemExit("root results do not match frozen protocol")
    actual_training_roots = root_values(
        roots_payload["sectors"]["0"]["stability"]["training_roots"]
    )
    actual_sealed = roots_payload["sectors"]["0"]["stability"]["sealed_12_to_16"]
    actual_h16 = float(
        roots_payload["sectors"]["0"]["leading_real_root_gate"]["h16"]
    )

    rectangle_data = protocol["root_rectangle"]
    rectangle = Rectangle(
        float(rectangle_data["real_min"]),
        float(rectangle_data["real_max"]),
        float(rectangle_data["imag_min"]),
        float(rectangle_data["imag_max"]),
    )
    contour_samples = [int(value) for value in protocol["contour_samples"]]
    seeds = [int(value) for value in protocol["control_seeds"]]
    source_orbits = weighted_orbits(records)
    fixed_length = next(
        orbit.length for orbit in source_orbits if orbit.period == 1
    )

    controls: dict[str, object] = {}
    for control in protocol["random_controls"]:
        control_seeds = [seeds[0]] if control == "constant_roof_parent" else seeds
        seed_blocks: dict[str, object] = {}
        for seed in control_seeds:
            control_orbits = make_control_orbits(
                source_orbits,
                control=control,
                seed=seed,
                fixed_length=fixed_length,
            )
            analysis = analyze_pair(
                control_orbits,
                rectangle,
                contour_samples,
                args.real_step,
                args.imag_step,
                kappa=0,
                coefficient_probe=actual_h16,
            )
            control_roots16 = root_values(analysis["cutoffs"]["16"]["roots"])
            actual_match = match_roots(actual_training_roots, control_roots16, tolerance=0.02)
            analysis["actual_training_to_control16"] = root_drift_summary(
                actual_match, len(actual_training_roots)
            )
            analysis["median_stability_margin_vs_actual_sealed"] = float(
                analysis["stability_8_to_16"]["median_drift"]
                - actual_sealed["median_drift"]
            )
            if control == "constant_roof_parent":
                analysis["exact_expected_pressure_root"] = pressure_root_constant_roof(
                    fixed_length
                )
                analysis["exact_imaginary_period"] = float(2 * np.pi / fixed_length)
            seed_blocks[str(seed)] = analysis
        controls[control] = seed_blocks

    neighbors: dict[str, object] = {}
    for path in args.neighbor_catalogs:
        payload, neighbor_records = load_catalog(path)
        if payload["protocol_sha256"] != protocol_hash:
            raise SystemExit(f"neighbor catalogue {path} does not match frozen protocol")
        parameter = str(payload["parameter"])
        analysis = analyze_pair(
            weighted_orbits(neighbor_records),
            rectangle,
            contour_samples,
            args.real_step,
            args.imag_step,
            kappa=0,
            coefficient_probe=actual_h16,
        )
        neighbor_roots16 = root_values(analysis["cutoffs"]["16"]["roots"])
        actual_match = match_roots(actual_training_roots, neighbor_roots16, tolerance=0.02)
        analysis["actual_training_to_neighbor16"] = root_drift_summary(
            actual_match, len(actual_training_roots)
        )
        analysis["catalog_path"] = str(path)
        analysis["catalog_sha256"] = sha256_file(path)
        analysis["catalog_gates"] = payload["gates"]
        analysis["evidence_status"] = "NUMERICAL_OBSERVATION; common survivor not certified"
        neighbors[parameter] = analysis

    payload = {
        "run_id": "controls_r041_r042",
        "created_utc": protocol["created_utc"],
        "candidate_id": protocol["candidate_id"],
        "protocol_path": str(args.protocol.relative_to(PROJECT_ROOT)),
        "protocol_sha256": protocol_hash,
        "catalog_path": str(args.catalog),
        "catalog_sha256": sha256_file(args.catalog),
        "root_results_path": str(args.root_results),
        "root_results_sha256": sha256_file(args.root_results),
        "scope": "adversarial finite-section controls; no control defines a Riemann target",
        "actual_reference": {
            "training_root_count": len(actual_training_roots),
            "sealed_stability": actual_sealed,
            "h16": actual_h16,
            "fixed_orbit_length": fixed_length,
        },
        "controls": controls,
        "neighbors": neighbors,
    }
    output = PROJECT_ROOT / "results" / "controls.json"
    output.write_text(
        json.dumps(json_safe(payload), allow_nan=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(output),
                "controls": list(controls),
                "neighbors": list(neighbors),
                "protocol_sha256": protocol_hash,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
