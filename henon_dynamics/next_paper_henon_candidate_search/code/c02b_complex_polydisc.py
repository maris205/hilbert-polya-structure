#!/usr/bin/env python3
"""Exact/certified audit of the C02B complex signed-root polydiscs.

All algebraic signs are certified using rational arithmetic and dyadic
enclosures for square roots.  Floating values are display-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = PROJECT_ROOT / "results" / "c02_complex_base"

CENTER = Fraction(23, 48)
RADIUS = Fraction(7, 48)
RADICAND_RADIUS = Fraction(7, 144)
MIXED_CENTER = Fraction(1, 6)
NEGATIVE_CENTER = Fraction(47, 144)
DYADIC_BITS = 192


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def sqrt_dyadic_interval(value: Fraction,
                         bits: int = DYADIC_BITS) -> tuple[Fraction, Fraction]:
    """Return exact dyadic lower/strict-upper bounds for sqrt(value)."""

    if value < 0:
        raise ValueError("square-root input must be nonnegative")
    scale = 1 << bits
    scaled_floor = (value.numerator * scale * scale) // value.denominator
    lower_integer = math.isqrt(scaled_floor)
    lower = Fraction(lower_integer, scale)
    upper = Fraction(lower_integer + 1, scale)
    if not lower * lower <= value < upper * upper:
        raise AssertionError("invalid dyadic square-root enclosure")
    return lower, upper


def interval_record(value: Fraction) -> dict[str, object]:
    lower, upper = sqrt_dyadic_interval(value)
    return {
        "radicand": frac_text(value),
        "lower": frac_text(lower),
        "upper": frac_text(upper),
        "lower_float": float(lower),
        "upper_float": float(upper),
        "bits": DYADIC_BITS,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--max-cyclic-length", type=int, default=12)
    return parser.parse_args()


def cyclic_admissible(signs: tuple[int, ...]) -> bool:
    n = len(signs)
    return all(
        not (signs[(index - 1) % n] == 1 and signs[(index + 1) % n] == 1)
        for index in range(n)
    )


def cyclic_audit(max_length: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in range(1, max_length + 1):
        admissible_count = 0
        mixed_occurrences = 0
        negative_occurrences = 0
        duplicate_neighbor_words = 0
        plus_plus_occurrences = 0
        for mask in range(1 << length):
            signs = tuple(1 if mask & (1 << index) else -1
                          for index in range(length))
            if not cyclic_admissible(signs):
                continue
            admissible_count += 1
            if length in (1, 2):
                duplicate_neighbor_words += 1
            for index in range(length):
                left = signs[(index - 1) % length]
                right = signs[(index + 1) % length]
                if left == 1 and right == 1:
                    plus_plus_occurrences += 1
                elif left == -1 and right == -1:
                    negative_occurrences += 1
                else:
                    mixed_occurrences += 1
        rows.append(
            {
                "length": length,
                "admissible_cyclic_sign_words": admissible_count,
                "mixed_neighbor_occurrences": mixed_occurrences,
                "two_negative_neighbor_occurrences": negative_occurrences,
                "forbidden_two_positive_occurrences": plus_plus_occurrences,
                "duplicate_neighbor_words": duplicate_neighbor_words,
            }
        )
    return rows


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    args = parse_args()
    if not 2 <= args.max_cyclic_length <= 20:
        raise SystemExit("require 2 <= max-cyclic-length <= 20")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    mixed_left = MIXED_CENTER - RADICAND_RADIUS
    mixed_right = MIXED_CENTER + RADICAND_RADIUS
    negative_left = NEGATIVE_CENTER - RADICAND_RADIUS
    negative_right = NEGATIVE_CENTER + RADICAND_RADIUS

    sqrt17_lower, sqrt17_upper = sqrt_dyadic_interval(Fraction(17, 1))
    sqrt10_lower, sqrt10_upper = sqrt_dyadic_interval(Fraction(10, 1))
    sqrt47_lower, sqrt47_upper = sqrt_dyadic_interval(Fraction(47, 1))

    # Rigorous upper bounds for |sqrt(z)-c| on each radicand disk.
    # Mixed: c-sqrt(17)/12.  For an upper bound, use sqrt17_lower.
    mixed_image_radius_upper = CENTER - sqrt17_lower / 12
    mixed_margin_lower = RADIUS - mixed_image_radius_upper

    # Two-negative: sqrt(47)/6-c-sqrt(10)/6.  Use upper/lower bounds in
    # the directions that make the image-radius bound larger.
    negative_image_radius_upper = (
        sqrt47_upper / 6 - CENTER - sqrt10_lower / 6
    )
    negative_margin_lower = RADIUS - negative_image_radius_upper

    contraction_upper = Fraction(2, 1) / sqrt17_lower

    # Exact positivity certificates, independent of decimal approximations.
    mixed_margin_exact_positive = 17 > 16
    # (sqrt(47)-sqrt(10)) < 15/4 follows after squaring from
    # sqrt(470)>687/32, whose square is the integer comparison below.
    negative_margin_exact_positive = 470 * 32 * 32 > 687 * 687

    cyclic_rows = cyclic_audit(args.max_cyclic_length)
    n1 = cyclic_rows[0]
    n2 = cyclic_rows[1]

    checks = {
        "canonical_center": CENTER == Fraction(23, 48),
        "canonical_radius": RADIUS == Fraction(7, 48),
        "mixed_radicand_disk": (
            MIXED_CENTER == Fraction(1, 6)
            and RADICAND_RADIUS == Fraction(7, 144)
        ),
        "two_negative_radicand_disk": NEGATIVE_CENTER == Fraction(47, 144),
        "mixed_disk_in_right_half_plane": mixed_left == Fraction(17, 144)
        and mixed_left > 0,
        "negative_disk_in_right_half_plane": negative_left == Fraction(5, 18)
        and negative_left > 0,
        "mixed_radical_margin_positive_exact": mixed_margin_exact_positive
        and mixed_margin_lower > 0,
        "negative_radical_margin_positive_exact": negative_margin_exact_positive
        and negative_margin_lower > 0,
        "strict_complex_self_map": min(mixed_margin_lower, negative_margin_lower)
        > 0,
        "uniform_contraction": contraction_upper < 1,
        "no_forbidden_neighbor_occurrence": all(
            row["forbidden_two_positive_occurrences"] == 0 for row in cyclic_rows
        ),
        "cyclic_n1_only_negative": n1["admissible_cyclic_sign_words"] == 1
        and n1["two_negative_neighbor_occurrences"] == 1,
        "cyclic_n2_only_double_negative": n2["admissible_cyclic_sign_words"] == 1
        and n2["two_negative_neighbor_occurrences"] == 2,
        "cyclic_n1_n2_duplicate_occurrences_retained": (
            n1["duplicate_neighbor_words"] == 1
            and n2["duplicate_neighbor_words"] == 1
        ),
    }

    report = {
        "run_id": "HCS_C02B_COMPLEX_POLYDISC_V1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "object": {
            "map": "(T_epsilon q)_i=epsilon_i*sqrt((1-q_{i-1}-q_{i+1})/6)",
            "square_root_branch": "principal",
            "center": frac_text(CENTER),
            "radius": frac_text(RADIUS),
            "admissibility": "the two chronological neighbors are not both +",
        },
        "radicand_disks": {
            "mixed_neighbors": {
                "center": frac_text(MIXED_CENTER),
                "radius": frac_text(RADICAND_RADIUS),
                "real_part_lower": frac_text(mixed_left),
                "real_part_upper": frac_text(mixed_right),
            },
            "two_negative_neighbors": {
                "center": frac_text(NEGATIVE_CENTER),
                "radius": frac_text(RADICAND_RADIUS),
                "real_part_lower": frac_text(negative_left),
                "real_part_upper": frac_text(negative_right),
            },
        },
        "certified_square_root_enclosures": {
            "sqrt_10": interval_record(Fraction(10, 1)),
            "sqrt_17": interval_record(Fraction(17, 1)),
            "sqrt_47": interval_record(Fraction(47, 1)),
        },
        "image_bounds": {
            "mixed_neighbors": {
                "radius_bound_exact": "23/48-sqrt(17)/12",
                "radius_upper_dyadic": frac_text(mixed_image_radius_upper),
                "radius_upper_float": float(mixed_image_radius_upper),
                "strict_margin_exact": "(sqrt(17)-4)/12",
                "strict_margin_lower_dyadic": frac_text(mixed_margin_lower),
                "strict_margin_lower_float": float(mixed_margin_lower),
            },
            "two_negative_neighbors": {
                "radius_bound_exact": "sqrt(47)/6-23/48-sqrt(10)/6",
                "radius_upper_dyadic": frac_text(negative_image_radius_upper),
                "radius_upper_float": float(negative_image_radius_upper),
                "strict_margin_exact": "5/8+(sqrt(10)-sqrt(47))/6",
                "strict_margin_lower_dyadic": frac_text(negative_margin_lower),
                "strict_margin_lower_float": float(negative_margin_lower),
            },
            "uniform_strict_margin_lower_float": float(
                min(mixed_margin_lower, negative_margin_lower)
            ),
        },
        "contraction": {
            "exact_bound": "2/sqrt(17)",
            "certified_upper_dyadic": frac_text(contraction_upper),
            "certified_upper_float": float(contraction_upper),
            "cyclic_duplicate_rule": (
                "For n=1,2 the left and right chronological occurrences may "
                "refer to one coordinate; both derivative contributions are "
                "retained, so the same 2/sqrt(17) bound applies."
            ),
        },
        "cyclic_audit": cyclic_rows,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "gate": {
            "complex_signed_root_self_map": "PASS",
            "complex_base_bridge": "PASS_FOR_SIGNED_ROOT_POLYDISC_ONLY",
            "finite_schottky_generators": "NOT_ESTABLISHED",
            "finite_dimensional_holomorphic_markov_branches": "NOT_ESTABLISHED",
            "nuclearity": "NOT_ESTABLISHED",
            "fredholm_determinant": "NOT_ESTABLISHED",
            "route_a_a2": "DO_NOT_PROMOTE",
        },
        "next_theorem": (
            "First audit the theorem delta against analytic pinning-coordinate "
            "theory. If explicit H6 content survives, use full frozen endpoint "
            "disks to prove Neumann-path localization, finite-dimensional "
            "crossed/pinning composition, cyclic-diagonal equivalence, a "
            "matching-Jacobian/monodromy identity, and a frozen signed flat-trace "
            "weight. Operators and nuclearity are later gates."
        ),
        "scope": (
            "Closes analytic self-mapping and contraction of the complexified "
            "signed-root orbit-coordinate solver. It does not construct a "
            "Schottky group, nuclear operator, determinant, or HP structure."
        ),
    }

    output_path = args.output_dir / "complex_polydisc.json"
    output_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(output_path),
                "sha256": sha256_file(output_path),
                "all_checks_pass": report["all_checks_pass"],
                "gate": report["gate"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not report["all_checks_pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
