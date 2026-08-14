#!/usr/bin/env python3
"""Deterministic controls for the Frobenius operator-ownership audit.

The program uses exact integer and rational arithmetic only.  It neither reads
Riemann zeros nor approximates a spectral determinant.  Finite frequency
tables illustrate theorem-level multiplicity statements; they are not used as
evidence for a limiting spectral claim.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


CANDIDATE_ID = "FF-FROB-OPERATOR-OWNERSHIP-P1-F2"


def divisors(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n must be positive")
    small: list[int] = []
    large: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    remaining = n
    prime_count = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            prime_count += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def affine_irreducible_count(degree: int) -> int:
    """Number of monic irreducibles of degree ``degree`` over F_2."""
    if degree < 1:
        raise ValueError("degree must be positive")
    numerator = sum(mobius(e) * 2 ** (degree // e) for e in divisors(degree))
    quotient, remainder = divmod(numerator, degree)
    if remainder:
        raise ArithmeticError("Mobius numerator was not divisible by degree")
    return quotient


def p1_closed_point_count(degree: int) -> int:
    count = affine_irreducible_count(degree)
    return count + (1 if degree == 1 else 0)


def reconstructed_fixed_points(n: int) -> int:
    return sum(d * p1_closed_point_count(d) for d in divisors(n))


def p1_point_count(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return 2**n + 1


def cohomological_supertrace(n: int) -> int:
    """tr(F^n|H^0) - tr(F^n|H^1) + tr(F^n|H^2)."""
    return 1 + 2**n


def multiplicity_through_degree(frequency_units: Fraction, max_degree: int) -> int:
    """Multiplicity in components of degree at most ``max_degree``.

    Frequencies are measured in units of 2*pi/log(2).  A degree-d component
    contains q exactly when q*d is an integer, and then it contains one Fourier
    mode for each such component.
    """
    if max_degree < 1:
        raise ValueError("max_degree must be positive")
    return sum(
        p1_closed_point_count(d)
        for d in range(1, max_degree + 1)
        if (frequency_units * d).denominator == 1
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def degree_rows(max_degree: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for d in range(1, max_degree + 1):
        closed = p1_closed_point_count(d)
        reconstructed = reconstructed_fixed_points(d)
        expected = p1_point_count(d)
        rows.append(
            {
                "degree": d,
                "affine_irreducibles": affine_irreducible_count(d),
                "projective_closed_points": closed,
                "closed_point_count_positive": str(closed > 0).lower(),
                "fixed_points_from_cycles": reconstructed,
                "p1_f2n_point_count": expected,
                "cohomological_supertrace": cohomological_supertrace(d),
                "all_three_match": str(reconstructed == expected == cohomological_supertrace(d)).lower(),
            }
        )
    return rows


def trace_rows(max_power: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(1, max_power + 1):
        point_count = p1_point_count(n)
        log_coefficient = Fraction(point_count, n)
        rows.append(
            {
                "power": n,
                "trace_h0": 1,
                "trace_h1": 0,
                "trace_h2": 2**n,
                "graded_trace": cohomological_supertrace(n),
                "point_count": point_count,
                "log_zeta_coefficient": str(log_coefficient),
                "trace_equals_point_count": str(cohomological_supertrace(n) == point_count).lower(),
            }
        )
    return rows


def frequency_rows(max_degree: int) -> list[dict[str, object]]:
    targets = [Fraction(0), Fraction(1, 2), Fraction(2, 3), Fraction(-3, 4), Fraction(5, 7)]
    cutoffs = sorted({4, 8, 12, 16, 20, max_degree})
    rows: list[dict[str, object]] = []
    for target in targets:
        previous = -1
        for cutoff in (c for c in cutoffs if c <= max_degree):
            multiplicity = multiplicity_through_degree(target, cutoff)
            rows.append(
                {
                    "frequency_units_2pi_over_log2": str(target),
                    "reduced_denominator": target.denominator,
                    "max_degree": cutoff,
                    "multiplicity": multiplicity,
                    "nondecreasing": str(multiplicity >= previous).lower(),
                }
            )
            previous = multiplicity
    return rows


def divisor_rows(k_radius: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for eigenvalue, real_part in ((1, 0), (2, 1)):
        for k in range(-k_radius, k_radius + 1):
            rows.append(
                {
                    "frobenius_eigenvalue": eigenvalue,
                    "s_real_part": real_part,
                    "imaginary_lattice_index": k,
                    "imaginary_unit": "2*pi/log(2)",
                    "divisor_type": "pole",
                }
            )
    return rows


def run(output_dir: Path, max_degree: int = 24, max_power: int = 24) -> dict[str, object]:
    if max_degree < 8 or max_power < 8:
        raise ValueError("cutoffs must be at least eight")
    output_dir.mkdir(parents=True, exist_ok=True)

    degree_path = output_dir / "degree_trace_ledger.csv"
    trace_path = output_dir / "cohomological_trace_ledger.csv"
    frequency_path = output_dir / "koopman_multiplicity_controls.csv"
    divisor_path = output_dir / "frobenius_divisor_lift.csv"
    certificate_path = output_dir / "operator_ownership_certificate.json"

    degrees = degree_rows(max_degree)
    traces = trace_rows(max_power)
    frequencies = frequency_rows(max_degree)
    divisor = divisor_rows(4)

    write_csv(
        degree_path,
        [
            "degree",
            "affine_irreducibles",
            "projective_closed_points",
            "closed_point_count_positive",
            "fixed_points_from_cycles",
            "p1_f2n_point_count",
            "cohomological_supertrace",
            "all_three_match",
        ],
        degrees,
    )
    write_csv(
        trace_path,
        [
            "power",
            "trace_h0",
            "trace_h1",
            "trace_h2",
            "graded_trace",
            "point_count",
            "log_zeta_coefficient",
            "trace_equals_point_count",
        ],
        traces,
    )
    write_csv(
        frequency_path,
        [
            "frequency_units_2pi_over_log2",
            "reduced_denominator",
            "max_degree",
            "multiplicity",
            "nondecreasing",
        ],
        frequencies,
    )
    write_csv(
        divisor_path,
        [
            "frobenius_eigenvalue",
            "s_real_part",
            "imaginary_lattice_index",
            "imaginary_unit",
            "divisor_type",
        ],
        divisor,
    )

    certificate: dict[str, object] = {
        "schema": "cohomological-operator-ownership/1",
        "candidate_id": CANDIDATE_ID,
        "cutoffs": {"max_degree": max_degree, "max_power": max_power},
        "exact_identities": {
            "all_degrees_positive_through_cutoff": all(
                int(row["projective_closed_points"]) > 0 for row in degrees
            ),
            "cycle_point_cohomology_ledgers_match": all(
                row["all_three_match"] == "true" for row in degrees
            ),
            "cohomological_trace_matches": all(
                row["trace_equals_point_count"] == "true" for row in traces
            ),
            "graded_determinant_denominator_coefficients": [1, -3, 2],
            "graded_determinant": "1/((1-t)*(1-2*t))",
            "koopman_point_spectrum_units": "Q",
            "koopman_spectrum": "R",
            "koopman_essential_spectrum": "R",
            "zero_eigenspace_infinite_dimensional": True,
            "heat_operator_trace_class": False,
            "compact_resolvent": False,
        },
        "operator_ownership": {
            "koopman": {
                "space": "weighted Hilbert direct sum of L2 periodic circles",
                "operator": "-i*d/du on the direct-sum periodic H1 domain",
                "self_adjoint": True,
                "owns_native_hasse_weil_determinant": False,
            },
            "cohomology": {
                "space": "graded etale cohomology over Q_l",
                "operator": "Deligne-convention Frobenius action",
                "eigenvalues_for_p1_f2": [1, 2],
                "owns_native_hasse_weil_determinant": True,
                "canonical_complex_hilbert_polya_host": False,
            },
            "coordinatewise_route_b_merge_allowed": False,
        },
        "route_a_riemann_target": {
            "overall": "ROUTE_A_REJECTED",
            "reason": "one-characteristic clock and lattice-periodic divisor",
        },
        "limited_route_b_koopman": {
            "b1": "B1_COMPLETE_OPERATOR_DEFINITION",
            "b2": "B2_SELF_ADJOINT",
            "b3": "B3_FAIL",
            "b4": "B4_FAIL",
            "b5": "B5_FAIL",
            "overall": "ROUTE_B_REJECTED",
            "hilbert_polya_claim_allowed": False,
        },
        "forbidden_data": [
            "Riemann zeros",
            "fitted boundary conditions",
            "fitted scales or phases",
            "floating-point root finding",
            "network data",
        ],
        "interpretation_boundary": (
            "Finite exact regression controls illustrate proved identities; they do not prove "
            "the infinite spectral statements or a Hilbert--Polya realization."
        ),
    }
    certificate_path.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    artifacts = [degree_path, trace_path, frequency_path, divisor_path, certificate_path]
    manifest = {
        "schema": "cohomological-operator-ownership-manifest/1",
        "candidate_id": CANDIDATE_ID,
        "artifacts": {path.name: sha256(path) for path in artifacts},
    }
    manifest_path = output_dir / "manifest.sha256.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return certificate


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1] / "results")
    parser.add_argument("--max-degree", type=int, default=24)
    parser.add_argument("--max-power", type=int, default=24)
    args = parser.parse_args()
    certificate = run(args.output_dir, args.max_degree, args.max_power)
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

