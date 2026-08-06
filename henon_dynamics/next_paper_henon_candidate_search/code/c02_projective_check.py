#!/usr/bin/env python3
"""Independent checker for HCS-C02 projective-pilot artifacts."""

from __future__ import annotations

import argparse
import csv
import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = PROJECT_ROOT / "results" / "c02_projective"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def display_path(path: Path) -> str:
    """Use a project-relative path when possible, otherwise keep it absolute.

    External result directories are useful for clean-room reruns.  Requiring
    every artifact to live below ``PROJECT_ROOT`` made the checker fail only
    while formatting its report, after all mathematical checks had run.
    """

    try:
        return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))
    except ValueError:
        return str(path.resolve())


def main() -> None:
    args = parse_args()
    output = args.output or (args.results_dir / "independent_check.json")
    summary_path = args.results_dir / "pilot_summary.json"
    memory_path = args.results_dir / "memory_bounds.csv"
    edge_path = args.results_dir / "state_disk_bundle.csv"
    cycles_path = args.results_dir / "periodic_monodromy.csv"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    memories = read_csv(memory_path)
    edges = read_csv(edge_path)
    cycles = read_csv(cycles_path)

    # Recompute the exact constants independently of the producer's JSON.
    radius = (Fraction(41, 256) / Fraction(7, 48)) * Fraction(1, 2)
    denominator_min = Fraction(4, 1) - radius
    image_bound = Fraction(1, 1) / denominator_min
    derivative_bound = image_bound * image_bound
    center = (Fraction(2, 15) + Fraction(1, 4)) / 2
    child_radius = (
        (Fraction(1, 4) - Fraction(2, 15)) / 2
        + radius / (4 * (4 - radius))
    )

    memory_numbers = [int(row["memory"]) for row in memories]
    q_widths = [float(row["q_diameter_bound"]) for row in memories]
    map_widths = [float(row["map_family_sup_bound"]) for row in memories]
    cycle_periods = [int(row["period"]) for row in cycles]
    expected_q_widths = [
        float(Fraction(7, 24)) * (2.0 / math.sqrt(17.0)) ** memory
        for memory in range(1, 9)
    ]

    checks = {
        "run_id": summary.get("run_id") == "HCS_C02_PROJECTIVE_PILOT_V1",
        "projective_formula_frozen": summary.get("projective_map")
        == "phi_q(m)=1/(-12q-m)",
        "radius_exact": radius == Fraction(123, 224),
        "pole_clearance_exact": denominator_min == Fraction(773, 224),
        "image_bound_strict": image_bound < radius,
        "derivative_bound_strict": derivative_bound < 1,
        "child_disks_separated": center - child_radius > 0,
        "child_disks_inside_source": center + child_radius < radius,
        "memory_rows_1_to_8": memory_numbers == list(range(1, 9)),
        "memory_width_nonincreasing": all(
            q_widths[index] <= q_widths[index - 1]
            for index in range(1, len(q_widths))
        ),
        "published_memory_prefactor": all(
            abs(observed - expected) <= 5e-16
            for observed, expected in zip(q_widths, expected_q_widths)
        ),
        "map_uncertainty_strictly_decreases": all(
            map_widths[index] < map_widths[index - 1]
            for index in range(1, len(map_widths))
        ),
        "six_allowed_edges": len(edges) == 6,
        "edge_chronology": all(row["shift_consistency"] == "True" for row in edges),
        # This SFT has no primitive period-two orbit.  The exact counts agree
        # with the Möbius inversion of tr(A^n), n=1,...,8.
        "primitive_cycle_counts": {
            period: cycle_periods.count(period) for period in range(1, 9)
        } == {1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2, 7: 4, 8: 5},
        "cycle_matrix_error": max(
            float(row["projective_monodromy_matrix_error"]) for row in cycles
        ) <= 2e-11,
        "cycle_slope_residual": max(
            float(row["slope_fixed_point_residual"]) for row in cycles
        ) <= 2e-11,
        "cycle_disk_membership": min(
            float(row["slope_disk_clearance"]) for row in cycles
        ) > 0,
        "no_false_a2_promotion": summary["gate"]["route_a_promotion"]
        == "DO_NOT_PROMOTE_TO_A2",
        "complex_base_not_claimed": summary["gate"]["complexified_henon_base_domain"]
        == "NOT_TESTABLE_FROM_R058_R059",
        "schottky_not_claimed": summary["gate"]["finite_schottky_generators"]
        == "NOT_ESTABLISHED",
        "target_firewall": summary["data_firewall"]["forbidden_target_data_read"]
        is False,
    }

    report = {
        "run_id": "HCS_C02_PROJECTIVE_INDEPENDENT_CHECK_V1",
        "producer_summary": display_path(summary_path),
        "recomputed_exact_constants": {
            "source_radius": f"{radius.numerator}/{radius.denominator}",
            "pole_clearance": (
                f"{denominator_min.numerator}/{denominator_min.denominator}"
            ),
            "image_bound": f"{image_bound.numerator}/{image_bound.denominator}",
            "derivative_bound": (
                f"{derivative_bound.numerator}/{derivative_bound.denominator}"
            ),
            "child_center_abs": f"{center.numerator}/{center.denominator}",
            "child_radius": (
                f"{child_radius.numerator}/{child_radius.denominator}"
            ),
        },
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scope": (
            "Checks exact disk arithmetic, artifact consistency, finite-period "
            "sanity, and conservative gate language. It does not certify a "
            "complex Hénon base, Schottky group, or Fredholm determinant."
        ),
    }
    output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
