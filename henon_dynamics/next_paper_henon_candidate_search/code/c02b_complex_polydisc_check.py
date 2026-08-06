#!/usr/bin/env python3
"""Independent exact and boundary-sampling checker for HCS-C02B."""

from __future__ import annotations

import argparse
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = PROJECT_ROOT / "results" / "c02_complex_base"


def display_path(path: Path) -> str:
    """Return a project-relative path when available, else an absolute path."""

    try:
        return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))
    except ValueError:
        return str(path.resolve())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--boundary-samples", type=int, default=16384)
    return parser.parse_args()


def cyclic_counts(max_length: int) -> list[dict[str, int]]:
    rows = []
    for length in range(1, max_length + 1):
        admissible = 0
        mixed = 0
        negative = 0
        forbidden = 0
        for mask in range(1 << length):
            signs = tuple(1 if mask & (1 << index) else -1
                          for index in range(length))
            if any(
                signs[(index - 1) % length] == 1
                and signs[(index + 1) % length] == 1
                for index in range(length)
            ):
                continue
            admissible += 1
            for index in range(length):
                pair = (signs[(index - 1) % length], signs[(index + 1) % length])
                if pair == (1, 1):
                    forbidden += 1
                elif pair == (-1, -1):
                    negative += 1
                else:
                    mixed += 1
        rows.append(
            {
                "length": length,
                "admissible": admissible,
                "mixed": mixed,
                "negative": negative,
                "forbidden": forbidden,
            }
        )
    return rows


def sampled_max_image_radius(center: Fraction, radius: Fraction,
                             target_center: Fraction, samples: int) -> float:
    maximum = 0.0
    for index in range(samples):
        angle = 2.0 * math.pi * index / samples
        z = float(center) + float(radius) * complex(math.cos(angle), math.sin(angle))
        root = cmath.sqrt(z)
        maximum = max(maximum, abs(root - float(target_center)))
    return maximum


def main() -> None:
    args = parse_args()
    if args.boundary_samples < 1024:
        raise SystemExit("require at least 1024 boundary samples")
    report_path = args.results_dir / "complex_polydisc.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))

    c = Fraction(23, 48)
    rho = Fraction(7, 48)
    rad_r = Fraction(7, 144)
    mixed_c = Fraction(1, 6)
    negative_c = Fraction(47, 144)

    mixed_margin = (math.sqrt(17.0) - 4.0) / 12.0
    negative_margin = 5.0 / 8.0 + (math.sqrt(10.0) - math.sqrt(47.0)) / 6.0
    contraction = 2.0 / math.sqrt(17.0)
    sampled_mixed = sampled_max_image_radius(
        mixed_c, rad_r, c, args.boundary_samples
    )
    sampled_negative = sampled_max_image_radius(
        negative_c, rad_r, c, args.boundary_samples
    )
    recomputed_cyclic = cyclic_counts(12)
    persisted_cyclic = report["cyclic_audit"]

    cyclic_match = (
        len(persisted_cyclic) == len(recomputed_cyclic) == 12
        and all(
            persisted["length"] == recomputed["length"]
            and persisted["admissible_cyclic_sign_words"] == recomputed["admissible"]
            and persisted["mixed_neighbor_occurrences"] == recomputed["mixed"]
            and persisted["two_negative_neighbor_occurrences"] == recomputed["negative"]
            and persisted["forbidden_two_positive_occurrences"] == recomputed["forbidden"]
            for persisted, recomputed in zip(persisted_cyclic, recomputed_cyclic)
        )
    )

    # Exact integer positivity tests for the two algebraic margins.
    exact_mixed_positive = 17 > 16
    exact_negative_positive = 470 * 1024 > 687 * 687

    checks = {
        "run_id": report["run_id"] == "HCS_C02B_COMPLEX_POLYDISC_V1",
        "canonical_domain": report["object"]["center"] == "23/48"
        and report["object"]["radius"] == "7/48",
        "mixed_disk_exact": (
            report["radicand_disks"]["mixed_neighbors"]["center"] == "1/6"
            and report["radicand_disks"]["mixed_neighbors"]["radius"] == "7/144"
            and report["radicand_disks"]["mixed_neighbors"]["real_part_lower"]
            == "17/144"
        ),
        "negative_disk_exact": (
            report["radicand_disks"]["two_negative_neighbors"]["center"]
            == "47/144"
            and report["radicand_disks"]["two_negative_neighbors"]["radius"]
            == "7/144"
            and report["radicand_disks"]["two_negative_neighbors"][
                "real_part_lower"
            ] == "5/18"
        ),
        "principal_branch_domain": Fraction(17, 144) > 0,
        "mixed_margin_positive_exact": exact_mixed_positive and mixed_margin > 0,
        "negative_margin_positive_exact": exact_negative_positive
        and negative_margin > 0,
        "uniform_contraction": contraction < 1,
        "sampled_mixed_image_inside": sampled_mixed < float(rho),
        "sampled_negative_image_inside": sampled_negative < float(rho),
        "cyclic_counts_match": cyclic_match,
        "n1_duplicate_chronology": recomputed_cyclic[0]
        == {"length": 1, "admissible": 1, "mixed": 0, "negative": 1,
            "forbidden": 0},
        "n2_duplicate_chronology": recomputed_cyclic[1]
        == {"length": 2, "admissible": 1, "mixed": 0, "negative": 2,
            "forbidden": 0},
        "complex_bridge_scoped": report["gate"]["complex_base_bridge"]
        == "PASS_FOR_SIGNED_ROOT_POLYDISC_ONLY",
        "no_schottky_claim": report["gate"]["finite_schottky_generators"]
        == "NOT_ESTABLISHED",
        "no_nuclearity_claim": report["gate"]["nuclearity"]
        == "NOT_ESTABLISHED",
        "no_fredholm_claim": report["gate"]["fredholm_determinant"]
        == "NOT_ESTABLISHED",
        "no_a2_promotion": report["gate"]["route_a_a2"] == "DO_NOT_PROMOTE",
    }

    output_report = {
        "run_id": "HCS_C02B_COMPLEX_POLYDISC_INDEPENDENT_CHECK_V1",
        "source": display_path(report_path),
        "exact_recomputations": {
            "mixed_real_gap": "17/144",
            "two_negative_real_gap": "5/18",
            "mixed_margin": "(sqrt(17)-4)/12",
            "two_negative_margin": "5/8+(sqrt(10)-sqrt(47))/6",
            "contraction": "2/sqrt(17)",
        },
        "display_values": {
            "mixed_margin": mixed_margin,
            "two_negative_margin": negative_margin,
            "contraction": contraction,
            "sampled_mixed_boundary_max": sampled_mixed,
            "sampled_negative_boundary_max": sampled_negative,
            "target_radius": float(rho),
            "boundary_samples_per_disk": args.boundary_samples,
        },
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scope": (
            "Exact recomputation plus non-probative boundary sampling. The "
            "checker certifies the signed-root polydisc gate only."
        ),
    }
    output_path = args.results_dir / "independent_check.json"
    output_path.write_text(
        json.dumps(output_report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output_report, indent=2, sort_keys=True))
    if not output_report["all_checks_pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
