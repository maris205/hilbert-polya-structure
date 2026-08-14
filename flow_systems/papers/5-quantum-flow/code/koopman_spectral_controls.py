#!/usr/bin/env python3
"""Deterministic controls for the Frobenius-suspension Koopman audit.

The infinite-dimensional results are proved in notes/proof_audit.md. This
program only regression-checks exact closed-point formulas, finite prefixes of
the rational-frequency multiplicity construction, and a finite Fourier-vector
instance of positive-component-weight unitary equivalence.

There is no Riemann-zero data, rational-prime table, fitting, optimization,
randomness, or network access.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


def integer_divisors(value: int) -> list[int]:
    """Return all positive divisors of a positive integer."""
    if value < 1:
        raise ValueError("value must be positive")
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def moebius(value: int) -> int:
    """Elementary integer Möbius function."""
    if value < 1:
        raise ValueError("value must be positive")
    remainder = value
    prime_count = 0
    candidate = 2
    while candidate * candidate <= remainder:
        if remainder % candidate == 0:
            remainder //= candidate
            prime_count += 1
            if remainder % candidate == 0:
                return 0
            while remainder % candidate == 0:
                remainder //= candidate
        candidate += 1
    if remainder > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def affine_irreducible_count_f2(degree: int) -> int:
    """Number of degree-degree monic irreducibles over F_2."""
    if degree < 1:
        raise ValueError("degree must be positive")
    numerator = sum(
        moebius(divisor) * 2 ** (degree // divisor)
        for divisor in integer_divisors(degree)
    )
    quotient, remainder = divmod(numerator, degree)
    if remainder:
        raise ArithmeticError("Möbius count is not integral")
    return quotient


def projective_closed_point_count(degree: int) -> int:
    """Closed points of P^1/F_2; infinity contributes only in degree one."""
    return affine_irreducible_count_f2(degree) + (1 if degree == 1 else 0)


def positivity_lower_bound_numerator(degree: int) -> int:
    """Lower bound used for d * I_2(d), valid for degree >= 2."""
    if degree < 2:
        raise ValueError("positivity bound is stated for degree at least two")
    geometric_sum = 2 ** (degree // 2 + 1) - 2
    return 2**degree - geometric_sum


def fixed_point_count_p1_f2(extension_degree: int) -> int:
    if extension_degree < 1:
        raise ValueError("extension degree must be positive")
    return 2**extension_degree + 1


def recovered_fixed_point_count(
    extension_degree: int, counts: dict[int, int]
) -> int:
    return sum(
        degree * counts[degree] for degree in integer_divisors(extension_degree)
    )


def fraction_label(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def frequency_witnesses(
    rational_frequency: Fraction, witness_count: int
) -> list[dict[str, object]]:
    """Finite prefix of degree k*b, mode k*a for q=a/b."""
    if witness_count < 1:
        raise ValueError("witness_count must be positive")
    numerator = rational_frequency.numerator
    denominator = rational_frequency.denominator
    rows: list[dict[str, object]] = []
    for index in range(1, witness_count + 1):
        degree = index * denominator
        mode = index * numerator
        observed = Fraction(mode, degree)
        closed_count = projective_closed_point_count(degree)
        rows.append(
            {
                "q": fraction_label(rational_frequency),
                "witness_index": index,
                "degree": degree,
                "fourier_mode": mode,
                "mode_over_degree": fraction_label(observed),
                "closed_point_count": closed_count,
                "closed_point_exists": closed_count > 0,
                "frequency_match": observed == rational_frequency,
                "actual_frequency_formula": f"(2*pi/log(2))*{fraction_label(observed)}",
            }
        )
    return rows


def weighted_unitary_control() -> tuple[list[dict[str, object]], dict[str, float]]:
    """Finite Fourier-vector regression for W_w U_t = U_t W_w.

    Each tuple is (degree, mode, weight, coefficient). Distinct tuples should
    be read as distinct components, even when a degree repeats.
    """
    samples: Sequence[tuple[int, int, float, complex]] = (
        (1, 0, 1.0 / 3.0, complex(1.0, -2.0)),
        (2, 1, 2.0, complex(-0.5, 0.75)),
        (3, -2, 5.0 / 7.0, complex(1.25, 0.5)),
        (6, 5, 11.0 / 5.0, complex(-0.2, -1.1)),
    )
    time = 0.371
    rows: list[dict[str, object]] = []
    weighted_norm_squared = 0.0
    mapped_norm_squared = 0.0
    max_intertwiner_error = 0.0

    for component_index, (degree, mode, weight, coefficient) in enumerate(
        samples, start=1
    ):
        angular_frequency = 2.0 * math.pi * mode / (degree * math.log(2.0))
        phase = cmath.exp(-1j * angular_frequency * time)
        source_after_translation = phase * coefficient
        map_after_translation = math.sqrt(weight) * source_after_translation
        mapped_coefficient = math.sqrt(weight) * coefficient
        translation_after_map = phase * mapped_coefficient
        error = abs(map_after_translation - translation_after_map)
        weighted_term = weight * abs(coefficient) ** 2
        mapped_term = abs(mapped_coefficient) ** 2
        weighted_norm_squared += weighted_term
        mapped_norm_squared += mapped_term
        max_intertwiner_error = max(max_intertwiner_error, error)
        rows.append(
            {
                "component_index": component_index,
                "degree": degree,
                "mode": mode,
                "weight": format(weight, ".17g"),
                "angular_frequency": format(angular_frequency, ".17g"),
                "weighted_norm_term": format(weighted_term, ".17g"),
                "mapped_norm_term": format(mapped_term, ".17g"),
                "norm_term_error": format(abs(weighted_term - mapped_term), ".17g"),
                "intertwiner_error": format(error, ".17g"),
            }
        )

    summary = {
        "weighted_norm_squared": weighted_norm_squared,
        "mapped_norm_squared": mapped_norm_squared,
        "norm_error": abs(weighted_norm_squared - mapped_norm_squared),
        "max_intertwiner_error": max_intertwiner_error,
    }
    return rows, summary


def write_csv(
    path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def run(
    output_dir: Path, max_degree: int = 24, witness_count: int = 12
) -> dict[str, object]:
    if max_degree < 2:
        raise ValueError("max_degree must be at least two")
    if witness_count < 2:
        raise ValueError("witness_count must be at least two")
    output_dir.mkdir(parents=True, exist_ok=True)

    counts = {
        degree: projective_closed_point_count(degree)
        for degree in range(1, max_degree + 1)
    }
    closed_rows: list[dict[str, object]] = []
    for degree in range(1, max_degree + 1):
        affine_count = affine_irreducible_count_f2(degree)
        projective_count = counts[degree]
        recovered = recovered_fixed_point_count(degree, counts)
        expected_fixed = fixed_point_count_p1_f2(degree)
        closed_rows.append(
            {
                "degree": degree,
                "affine_irreducible_count": affine_count,
                "projective_closed_point_count": projective_count,
                "positive": projective_count > 0,
                "positivity_lower_bound_numerator": (
                    "" if degree == 1 else positivity_lower_bound_numerator(degree)
                ),
                "recovered_fixed_points": recovered,
                "expected_fixed_points": expected_fixed,
                "fixed_point_match": recovered == expected_fixed,
            }
        )

    rational_controls = (
        Fraction(0, 1),
        Fraction(1, 2),
        Fraction(-2, 3),
        Fraction(5, 4),
        Fraction(1, 1),
        Fraction(-7, 5),
    )
    frequency_rows = [
        row
        for rational_frequency in rational_controls
        for row in frequency_witnesses(rational_frequency, witness_count)
    ]
    weight_rows, weight_summary = weighted_unitary_control()

    closed_path = output_dir / "closed_point_degree_controls.csv"
    frequency_path = output_dir / "frequency_multiplicity_witnesses.csv"
    weight_path = output_dir / "weight_unitary_controls.csv"

    write_csv(
        closed_path,
        [
            "degree",
            "affine_irreducible_count",
            "projective_closed_point_count",
            "positive",
            "positivity_lower_bound_numerator",
            "recovered_fixed_points",
            "expected_fixed_points",
            "fixed_point_match",
        ],
        closed_rows,
    )
    write_csv(
        frequency_path,
        [
            "q",
            "witness_index",
            "degree",
            "fourier_mode",
            "mode_over_degree",
            "closed_point_count",
            "closed_point_exists",
            "frequency_match",
            "actual_frequency_formula",
        ],
        frequency_rows,
    )
    write_csv(
        weight_path,
        [
            "component_index",
            "degree",
            "mode",
            "weight",
            "angular_frequency",
            "weighted_norm_term",
            "mapped_norm_term",
            "norm_term_error",
            "intertwiner_error",
        ],
        weight_rows,
    )

    artifact_paths = (closed_path, frequency_path, weight_path)
    manifest: dict[str, object] = {
        "schema": "koopman_spectral_controls/1",
        "candidate_id": "FF-FROB-SUSP-P1-F2-KOOPMAN-P1",
        "max_degree": max_degree,
        "witness_count_per_rational_frequency": witness_count,
        "rational_frequency_controls": [
            fraction_label(value) for value in rational_controls
        ],
        "all_closed_point_counts_positive": all(count > 0 for count in counts.values()),
        "all_positivity_bounds_positive": all(
            positivity_lower_bound_numerator(degree) > 0
            for degree in range(2, max_degree + 1)
        ),
        "all_fixed_point_ledgers_match": all(
            row["fixed_point_match"] for row in closed_rows
        ),
        "all_frequency_witnesses_match": all(
            row["frequency_match"] for row in frequency_rows
        ),
        "all_frequency_witness_degrees_exist": all(
            row["closed_point_exists"] for row in frequency_rows
        ),
        "nonzero_frequency_control_survives_kernel_deletion": all(
            row["frequency_match"] and row["closed_point_exists"]
            for row in frequency_rows
            if row["q"] == "1/2"
        ),
        "weight_unitary_control": {
            key: format(value, ".17g") for key, value in weight_summary.items()
        },
        "weight_unitary_control_pass": (
            weight_summary["norm_error"] < 1e-14
            and weight_summary["max_intertwiner_error"] < 1e-14
        ),
        "theorem_ledger": {
            "point_spectrum": "(2*pi/log(2))*Q",
            "point_multiplicity": "countably_infinite_at_every_point_eigenvalue",
            "spectrum": "R",
            "essential_spectrum": "R",
            "discrete_spectrum": "empty",
            "compact_resolvent": False,
            "positive_width_local_projection_rank": "infinite",
            "heat_trace_class": False,
            "orbit_zeta_is_generator_determinant": False,
        },
        "route_a_a4": {
            "verdict": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "evidence_status": "PROVED",
            "route_b_ready": False,
        },
        "limited_route_b": {
            "b1": "B1_COMPLETE_OPERATOR_DEFINITION",
            "b2": "B2_SELF_ADJOINT",
            "b3": "B3_FAIL",
            "scope": ["B1", "B2", "B3"],
            "overall": "ROUTE_B_REJECTED",
            "hilbert_polya_claim_allowed": False,
        },
        "b4_b5_invoked": False,
        "target_zero_data_used": False,
        "fitted_parameters": [],
        "artifacts": {path.name: sha256(path) for path in artifact_paths},
    }

    manifest_path = output_dir / "koopman_spectral_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--max-degree", type=int, default=24)
    parser.add_argument("--witness-count", type=int, default=12)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = run(
        args.output_dir,
        max_degree=args.max_degree,
        witness_count=args.witness_count,
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

