#!/usr/bin/env python3
"""Exact inverse-design and control experiments for SD-C03."""

from __future__ import annotations

import csv
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Sequence

import mpmath as mp
import numpy as np


SESSION_ID = "SD-S4-2026-08-12"
CANDIDATE_ID = "SD-C03"
MASTER_SEED = 20260812
ON_CIRCLE_SEED = 20260813
OFF_CIRCLE_SEED = 20260814
TARGET_DEGREE = 12
PAIR_COUNT = TARGET_DEGREE // 2
DECIMAL_PRECISION = 80


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def polynomial_multiply(left: Sequence[Fraction], right: Sequence[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def seeded_target_factors(seed: int, on_circle: bool) -> tuple[list[list[Fraction]], list[Fraction]]:
    rng = random.Random(seed)
    cosine_pool = [
        Fraction(-7, 8),
        Fraction(-3, 4),
        Fraction(-1, 2),
        Fraction(-1, 4),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(7, 8),
    ]
    cosines = rng.sample(cosine_pool, PAIR_COUNT)
    if on_circle:
        radii = [Fraction(1)] * PAIR_COUNT
    else:
        radii = [Fraction(2, 3), Fraction(3, 4), Fraction(4, 5), Fraction(5, 4), Fraction(4, 3), Fraction(3, 2)]
        rng.shuffle(radii)
    factors: list[list[Fraction]] = []
    coefficients = [Fraction(1)]
    for cosine, radius in zip(cosines, radii, strict=True):
        factor = [Fraction(1), -2 * cosine / radius, Fraction(1) / (radius * radius)]
        factors.append(factor)
        coefficients = polynomial_multiply(coefficients, factor)
    return factors, coefficients


def inverse_design(target_coefficients: Sequence[Fraction]) -> list[Fraction]:
    if not target_coefficients or target_coefficients[0] != 1:
        raise ValueError("inverse design requires H(0)=1")
    return [-coefficient for coefficient in target_coefficients[1:]]


def renewal_determinant_coefficients(loop_weights: Sequence[Fraction]) -> list[Fraction]:
    return [Fraction(1)] + [-weight for weight in loop_weights]


def evaluate_fraction_polynomial(coefficients: Sequence[Fraction], x: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    result: mp.mpf | mp.mpc = mp.mpf(0)
    for coefficient in reversed(coefficients):
        result = result * x + mp.mpf(coefficient.numerator) / coefficient.denominator
    return result


def evaluate_exact_fraction_polynomial(coefficients: Sequence[Fraction], x: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def positive_crossing_control(target_coefficients: Sequence[Fraction], precision: int) -> dict[str, object]:
    """Use degree- and magnitude-matched nonnegative renewal coefficients."""
    mp.mp.dps = precision
    positive_weights = [abs(coefficient) for coefficient in target_coefficients[1:]]
    assert any(weight > 0 for weight in positive_weights)

    first_return_coefficients = [Fraction(0)] + positive_weights

    def exact_first_return(x: Fraction) -> Fraction:
        return evaluate_exact_fraction_polynomial(first_return_coefficients, x)

    lower_exact = Fraction(0)
    upper_exact = Fraction(1)
    while exact_first_return(upper_exact) <= 1:
        upper_exact *= 2
    initial_upper_exact = upper_exact
    for _ in range(precision * 4):
        midpoint = (lower_exact + upper_exact) / 2
        if exact_first_return(midpoint) < 1:
            lower_exact = midpoint
        else:
            upper_exact = midpoint
    lower = mp.mpf(lower_exact.numerator) / lower_exact.denominator
    upper = mp.mpf(upper_exact.numerator) / upper_exact.denominator
    root = (lower + upper) / 2
    determinant_residual = abs(1 - evaluate_fraction_polynomial(first_return_coefficients, root))
    return {
        "evidence_status": "NUMERICALLY_CERTIFIED",
        "theorem_status": "PROVED",
        "theorem": "If a_n>=0, some a_n>0, and F(r_-)<1<F(r_+), continuity and strict increase give a unique positive real zero of D=1-F in (r_-,r_+).",
        "crossing_lower": "0",
        "F_at_lower": "0",
        "crossing_initial_upper": fraction_string(initial_upper_exact),
        "F_at_initial_upper": fraction_string(exact_first_return(initial_upper_exact)),
        "root_bracket": [mp.nstr(lower, precision), mp.nstr(upper, precision)],
        "root_bracket_exact_rational": [fraction_string(lower_exact), fraction_string(upper_exact)],
        "root_bracket_width_exact": fraction_string(upper_exact - lower_exact),
        "positive_root": mp.nstr(root, precision),
        "determinant_residual": mp.nstr(determinant_residual, 20),
        "loop_weights_exact": [fraction_string(value) for value in positive_weights],
        "precision_decimal_digits": precision,
    }


def numerical_root_summary(coefficients_ascending: Sequence[complex], expected_radii: Sequence[float] | None = None) -> dict[str, object]:
    roots = np.roots(np.asarray(list(reversed(coefficients_ascending)), dtype=np.complex128))
    radii = np.sort(np.abs(roots))
    result: dict[str, object] = {
        "precision": "numpy.complex128",
        "root_radii_sorted": [float(value) for value in radii],
        "inside_unit_disk": int(np.sum(radii < 1 - 1e-8)),
        "on_unit_circle_tolerance_1e-8": int(np.sum(np.abs(radii - 1) <= 1e-8)),
        "outside_unit_disk": int(np.sum(radii > 1 + 1e-8)),
    }
    if expected_radii is not None:
        expected = np.sort(np.asarray(expected_radii, dtype=float))
        result["max_radius_error_against_exact_factor_geometry"] = float(np.max(np.abs(radii - expected)))
    return result


def random_phase_control(target_coefficients: Sequence[Fraction], seed: int) -> dict[str, object]:
    rng = random.Random(seed)
    phases = [rng.uniform(-np.pi, np.pi) for _ in target_coefficients[1:]]
    loop_weights = [float(abs(value)) * np.exp(1j * phase) for value, phase in zip(target_coefficients[1:], phases, strict=True)]
    determinant = [1 + 0j] + [-value for value in loop_weights]
    target_complex = [complex(float(value), 0.0) for value in target_coefficients]
    coefficient_errors = [abs(left - right) for left, right in zip(determinant, target_complex, strict=True)]
    return {
        "evidence_status": "NUMERICAL_OBSERVATION",
        "seed": seed,
        "degree": len(target_coefficients) - 1,
        "magnitude_matched": True,
        "phases_radians": phases,
        "max_target_coefficient_error": float(max(coefficient_errors)),
        "target_reconstructed": bool(max(coefficient_errors) == 0),
        "determinant_coefficients": [[float(value.real), float(value.imag)] for value in determinant],
        "root_summary": numerical_root_summary(determinant),
    }


def matched_degree_generic_control(seed: int) -> dict[str, object]:
    rng = random.Random(seed)
    coefficients = [Fraction(1)]
    for index in range(1, TARGET_DEGREE + 1):
        numerator = rng.choice([value for value in range(-7, 8) if value != 0])
        coefficients.append(Fraction(numerator, index + 7))
    weights = inverse_design(coefficients)
    reconstructed = renewal_determinant_coefficients(weights)
    return {
        "evidence_status": "PROVED",
        "seed": seed,
        "degree": TARGET_DEGREE,
        "target_coefficients_exact": [fraction_string(value) for value in coefficients],
        "loop_weights_exact": [fraction_string(value) for value in weights],
        "reconstruction_exact": reconstructed == coefficients,
        "interpretation": "The coefficientwise inverse construction works for a generic matched-degree target too; it is not selective for a desired root geometry.",
    }


def target_result(name: str, seed: int, on_circle: bool, precision: int) -> dict[str, object]:
    factors, target = seeded_target_factors(seed, on_circle)
    weights = inverse_design(target)
    reconstructed = renewal_determinant_coefficients(weights)
    radii_exact = []
    for factor in factors:
        radius_squared_inverse = factor[2]
        radius = float(1 / np.sqrt(float(radius_squared_inverse)))
        radii_exact.extend([radius, radius])
    violating_indices = [index for index, coefficient in enumerate(target[1:], start=1) if coefficient > 0]
    return {
        "name": name,
        "evidence_status": "PROVED",
        "seed": seed,
        "degree_cutoff": TARGET_DEGREE,
        "factor_coefficients_exact": [[fraction_string(value) for value in factor] for factor in factors],
        "target_coefficients_exact": [fraction_string(value) for value in target],
        "inverse_designed_loop_weights_exact": [fraction_string(value) for value in weights],
        "reconstructed_coefficients_exact": [fraction_string(value) for value in reconstructed],
        "exact_reconstruction": reconstructed == target,
        "expected_root_radii_from_exact_factors": radii_exact,
        "numerical_root_check": numerical_root_summary([complex(float(value), 0) for value in target], radii_exact),
        "positive_renewal_obstruction": {
            "evidence_status": "PROVED",
            "criterion": "A positive renewal representation requires every nonconstant target coefficient h_n<=0 because a_n=-h_n>=0.",
            "positive_target_coefficient_indices": violating_indices,
            "violation_count": len(violating_indices),
            "positive_representation_possible": len(violating_indices) == 0,
        },
        "positive_crossing_control": positive_crossing_control(target, precision),
        "random_phase_control": random_phase_control(target, MASTER_SEED),
    }


def build_results(precision: int = DECIMAL_PRECISION) -> dict[str, object]:
    on_circle = target_result("on_circle", ON_CIRCLE_SEED, True, precision)
    off_circle = target_result("off_circle", OFF_CIRCLE_SEED, False, precision)
    generic = matched_degree_generic_control(MASTER_SEED)
    exact_reconstruction_all = bool(
        on_circle["exact_reconstruction"] and off_circle["exact_reconstruction"] and generic["reconstruction_exact"]
    )
    numerical_keys = {"numerical_root_check", "positive_crossing_control", "random_phase_control"}
    on_circle_exact = {key: value for key, value in on_circle.items() if key not in numerical_keys}
    off_circle_exact = {key: value for key, value in off_circle.items() if key not in numerical_keys}
    return {
        "schema_version": "1.0.0",
        "session_id": SESSION_ID,
        "candidate_id": CANDIDATE_ID,
        "run_id": "SD-C03-frozen-v1",
        "source_lock": {
            "family": "symbolic dynamics / weighted renewal shift",
            "first_return_series": "F(z)=sum_{n>=1} a_n z^n",
            "determinant_convention": "D_ren(z)=1-F(z)",
            "normalization": "D_ren(0)=1",
            "synthetic_targets_only": True,
            "forbidden_data_respected": True,
            "riemann_zero_data_used": False,
        },
        "reproducibility": {
            "master_seed": MASTER_SEED,
            "on_circle_seed": ON_CIRCLE_SEED,
            "off_circle_seed": OFF_CIRCLE_SEED,
            "random_phase_seed": MASTER_SEED,
            "precision": {"exact": "fractions.Fraction rational arithmetic", "numerical_decimal_digits": precision, "root_diagnostic": "numpy.complex128"},
            "cutoff": {"target_degree": TARGET_DEGREE, "conjugate_pair_count": PAIR_COUNT},
        },
        "exact": {
            "inverse_design_theorem": {
                "evidence_status": "PROVED",
                "statement": "For every holomorphic germ H(z)=1+sum_{n>=1}h_n z^n, choose a_n=-h_n. Then D_ren(z)=1-sum a_n z^n=H(z) coefficientwise throughout their common convergence disk.",
                "selectivity_consequence": "This is a tautological coefficient map unless the loop weights arise independently from the symbolic grammar.",
            },
            "positive_crossing_theorem": {
                "evidence_status": "PROVED",
                "statement": "For a_n>=0 with some a_n>0, F is continuous and strictly increasing on r>0. Under an explicit F(r_-)<1<F(r_+) crossing, D=1-F has exactly one positive root in (r_-,r_+).",
            },
            "on_circle_target": on_circle_exact,
            "off_circle_target": off_circle_exact,
            "matched_degree_generic_control": generic,
            "all_exact_reconstructions_pass": exact_reconstruction_all,
        },
        "numerical": {
            "evidence_status": "NUMERICAL_OBSERVATION",
            "on_circle_root_diagnostic": on_circle["numerical_root_check"],
            "off_circle_root_diagnostic": off_circle["numerical_root_check"],
            "positive_crossing_controls": {
                "on_circle": on_circle["positive_crossing_control"],
                "off_circle": off_circle["positive_crossing_control"],
            },
            "random_phase_controls": {
                "on_circle": on_circle["random_phase_control"],
                "off_circle": off_circle["random_phase_control"],
            },
        },
        "adversarial_verdict": {
            "status": "STOP_SCOPED / PROVES_TOO_MUCH",
            "evidence_status": "PROVED",
            "reason": "The identical inverse-design mechanism reconstructs on-circle, off-circle, and generic matched-degree synthetic targets exactly.",
            "no_riemann_target_fitted": True,
        },
        "claim_boundary": "Exact rational coefficient identities and positivity obstructions are separated from numerical root-radius and bisection diagnostics.",
        "route_b_invocation_allowed": False,
    }


def write_results(output_dir: Path, precision: int = DECIMAL_PRECISION) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = build_results(precision)
    (output_dir / "sd_c03_results.json").write_text(
        json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    csv_path = output_dir / "sd_c03_controls.csv"
    fields = [
        "candidate_id",
        "target",
        "seed",
        "precision",
        "cutoff_degree",
        "evidence_status",
        "exact_reconstruction",
        "positive_obstruction_count",
        "positive_crossing_root",
        "random_phase_max_coefficient_error",
        "adversarial_verdict",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for key in ("on_circle_target", "off_circle_target"):
            target = results["exact"][key]  # type: ignore[index]
            numerical_name = str(target["name"])
            crossing = results["numerical"]["positive_crossing_controls"][numerical_name]  # type: ignore[index]
            randomized = results["numerical"]["random_phase_controls"][numerical_name]  # type: ignore[index]
            writer.writerow(
                {
                    "candidate_id": CANDIDATE_ID,
                    "target": target["name"],
                    "seed": target["seed"],
                    "precision": f"exact_rational + {precision}_decimal_digit_bisection",
                    "cutoff_degree": TARGET_DEGREE,
                    "evidence_status": "PROVED",
                    "exact_reconstruction": target["exact_reconstruction"],
                    "positive_obstruction_count": target["positive_renewal_obstruction"]["violation_count"],
                    "positive_crossing_root": crossing["positive_root"],
                    "random_phase_max_coefficient_error": randomized["max_target_coefficient_error"],
                    "adversarial_verdict": results["adversarial_verdict"]["status"],
                }
            )
    return results


if __name__ == "__main__":
    default_output = Path(__file__).resolve().parents[1] / "results"
    built = write_results(default_output)
    print(json.dumps({"candidate_id": CANDIDATE_ID, "passed": built["exact"]["all_exact_reconstructions_pass"]}))
