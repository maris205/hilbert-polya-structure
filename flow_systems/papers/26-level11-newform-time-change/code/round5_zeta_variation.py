#!/usr/bin/env python3
"""Paper-26 Round-5 first-variation and Hecke-owner audit.

This module freezes an explicit reciprocal-product convention for two formal
finite-owner zeta functions.  It consumes only the source-locked Round-4
Hecke cycle/period ledgers and the Round-2 group definitions.  It never reads
prime-target tables or spectral-zero data.

The two conventions are

    log Z_R(s, eps) = sum_gamma# sum_r>=1
        exp(-s r T_eps(gamma)) / r,

and the frozen-stability Selberg-type convention

    log Z_S^fr(s, eps) = sum_gamma# sum_r>=1
        exp(-s r T_eps(gamma)) / (r (1-exp(-r ell(gamma)))).

Here gamma# is an oriented primitive flow orbit, r is its zeta repetition,
and ell is the base hyperbolic length.  Round 5 truncates only r, at r <= 4,
for its finite numerical ledger.  The analytic statements in the companion
note concern the convergent infinite series (or finite owner sets).

The Hecke permutation-cycle degree d is deliberately kept separate from r.
Each Round-4 output delta_O is primitive in Gamma_0(11), even though its base
length is d_O ell(M).  Treating d_O as a zeta repetition would mix owners.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Iterable, Sequence


PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_ROUND4_CYCLE_LEDGER = (
    PROJECT_DIR / "results" / "round4_hecke_cycle_ledger.csv"
)
DEFAULT_ROUND4_PERIOD_SUMMARY = (
    PROJECT_DIR / "results" / "round4_hecke_period_summary.csv"
)

FROZEN_S_VALUES = (0.125, 0.25, 0.5)
FROZEN_REPETITION_CUTOFF = 4
REPETITION_LEDGER_S = 0.25
NUMERICAL_TOLERANCE = 1.0e-10

REPETITION_FIELDS = (
    "primitive_owner_id",
    "word",
    "hecke_prime",
    "cycle_id",
    "hecke_cycle_degree_d",
    "primitive_in_gamma0_11_exact",
    "orientation_sign",
    "orientation_partner_id",
    "zeta_repetition_r",
    "frozen_s",
    "primitive_base_length",
    "repeated_base_length",
    "primitive_alpha_period",
    "repeated_alpha_period",
    "log_series_weight_one_over_r",
    "ruelle_log_term",
    "ruelle_direct_first_variation",
    "ruelle_cancelled_first_variation",
    "ruelle_formula_residual",
    "frozen_stability_denominator",
    "selberg_log_term",
    "selberg_direct_first_variation",
    "selberg_cancelled_first_variation",
    "selberg_formula_residual",
    "orientation_pair_cancellation_status",
    "owner_evidence_token",
    "period_evidence_token",
)

DEGREE_MOMENT_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "hecke_cycle_degree_d",
    "primitive_owner_count_at_degree",
    "base_alpha_period",
    "alpha_period_sum_at_degree",
    "complex_period_sum_real_at_degree",
    "complex_period_sum_imag_at_degree",
    "closed_control_period_sum_at_degree",
    "required_alpha_moment_for_all_s_recurrence",
    "alpha_moment_residual",
    "alpha_moment_status",
    "required_complex_moment_real_for_all_s_recurrence",
    "required_complex_moment_imag_for_all_s_recurrence",
    "complex_moment_residual",
    "complex_moment_status",
    "required_closed_control_moment_for_all_s_recurrence",
    "closed_control_moment_residual",
    "closed_control_moment_status",
    "moment_criterion_scope",
    "period_evidence_token",
)

HECKE_VARIATION_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "frozen_s",
    "zeta_repetition_cutoff_R",
    "source_primitive_base_length",
    "source_alpha_period",
    "source_closed_control_period",
    "output_primitive_owner_count",
    "hecke_cycle_degree_pattern",
    "degree_profile_type",
    "hecke_degree_is_zeta_repetition",
    "all_output_owners_primitive_exact",
    "unweighted_output_alpha_period_sum",
    "unweighted_expected_alpha_period_sum",
    "unweighted_alpha_residual",
    "ruelle_source_first_variation",
    "ruelle_hecke_output_first_variation_one_sided",
    "ruelle_naive_a_p_prediction",
    "ruelle_naive_recurrence_residual",
    "ruelle_naive_recurrence_status",
    "selberg_source_first_variation",
    "selberg_hecke_output_first_variation_one_sided",
    "selberg_naive_a_p_prediction",
    "selberg_naive_recurrence_residual",
    "selberg_naive_recurrence_status",
    "ruelle_closed_control_recurrence_residual",
    "selberg_closed_control_recurrence_residual",
    "canonical_inverse_paired_ruelle_first_variation",
    "canonical_inverse_paired_selberg_first_variation",
    "canonical_orientation_pairing_status",
    "formal_no_implication_witness",
    "analytic_evidence_token",
    "finite_period_evidence_token",
)


def _load_round2_module():
    module_path = Path(__file__).with_name("round2_experiment.py")
    spec = importlib.util.spec_from_file_location("p26_round2_for_round5", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load round2_experiment.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ROUND2 = _load_round2_module()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def grouped_cycle_rows(
    rows: Iterable[dict[str, str]],
) -> dict[tuple[str, int], list[dict[str, str]]]:
    grouped: dict[tuple[str, int], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["word"], int(row["hecke_prime"]))].append(row)
    for values in grouped.values():
        values.sort(key=lambda row: int(row["cycle_id"]))
    return dict(sorted(grouped.items()))


def period_summary_map(
    rows: Iterable[dict[str, str]],
) -> dict[tuple[str, int], dict[str, str]]:
    result: dict[tuple[str, int], dict[str, str]] = {}
    for row in rows:
        key = (row["word"], int(row["hecke_prime"]))
        if key in result:
            raise ValueError(f"duplicate Round-4 period-summary key: {key!r}")
        result[key] = row
    return result


def primitive_length(word: str) -> float:
    return ROUND2.geodesic_length(ROUND2.matrix_from_word(word))


def kernel(kind: str, s_value: float, length: float, repetition_cutoff: int) -> float:
    if kind not in {"ruelle", "selberg"}:
        raise ValueError(f"unknown kernel kind: {kind!r}")
    if s_value <= 0.0 or length <= 0.0 or repetition_cutoff <= 0:
        raise ValueError("kernel arguments must be positive")
    total = 0.0
    for repetition in range(1, repetition_cutoff + 1):
        exponential = math.exp(-s_value * repetition * length)
        if kind == "selberg":
            exponential /= 1.0 - math.exp(-repetition * length)
        total += exponential
    return total


def owner_first_variation(
    kind: str,
    s_value: float,
    length: float,
    alpha_period: float,
    repetition_cutoff: int,
) -> float:
    return -s_value * alpha_period * kernel(
        kind, s_value, length, repetition_cutoff
    )


def dirichlet_degree_coefficient(
    degree_moments: dict[int, complex | float], exponent: int
) -> complex:
    """Coefficient sum produced by q-expanding either infinite kernel.

    For an output owner of Hecke degree d, both the Ruelle kernel and the
    frozen-stability Selberg kernel contribute only powers q^(d*r).  At power
    q^n the period numerator is therefore sum_(d|n) P_d.  (The Selberg kernel
    has the additional common nonzero factor 1/(1-exp(-n*ell)).)
    """

    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return sum(
        (complex(value) for degree, value in degree_moments.items() if exponent % degree == 0),
        0.0j,
    )


def validate_round4_inputs(
    cycle_rows: Sequence[dict[str, str]],
    period_rows: Sequence[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    grouped = grouped_cycle_rows(cycle_rows)
    periods = period_summary_map(period_rows)
    if len(cycle_rows) != 138:
        errors.append(f"expected 138 cycle-owner rows, got {len(cycle_rows)}")
    if len(period_rows) != 55:
        errors.append(f"expected 55 period-summary rows, got {len(period_rows)}")
    if set(grouped) != set(periods):
        errors.append("cycle-owner and period-summary keys differ")
    for key, rows in grouped.items():
        word, prime = key
        if sum(int(row["cycle_degree"]) for row in rows) != prime + 1:
            errors.append(f"Hecke branches do not partition p+1 for {key!r}")
        if any(row["primitive_in_gamma0_11_exact"] != "true" for row in rows):
            errors.append(f"nonprimitive Round-4 output owner for {key!r}")
        if key not in periods:
            continue
        summary = periods[key]
        alpha_sum = sum(float(row["period_real"]) for row in rows)
        expected = float(summary["expected_period_real"])
        if abs(alpha_sum - expected) > NUMERICAL_TOLERANCE:
            errors.append(f"Round-4 alpha Hecke sum mismatch for {key!r}")
        length = primitive_length(word)
        for row in rows:
            degree = int(row["cycle_degree"])
            owner_trace = abs(int(row["cycle_owner_trace"]))
            owner_length = 2.0 * math.acosh(owner_trace / 2.0)
            if abs(owner_length - degree * length) > 5.0e-13:
                errors.append(
                    f"cycle degree/base-length identity failed for {key!r}, "
                    f"cycle {row['cycle_id']}"
                )
    return errors


def build_repetition_ledger(
    cycle_rows: Sequence[dict[str, str]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cycle in cycle_rows:
        word = cycle["word"]
        prime = int(cycle["hecke_prime"])
        cycle_id = int(cycle["cycle_id"])
        degree = int(cycle["cycle_degree"])
        length = degree * primitive_length(word)
        unsigned_period = float(cycle["period_real"])
        owner_id = f"{word}|p={prime}|O={cycle_id}"
        for orientation in (1, -1):
            signed_period = orientation * unsigned_period
            oriented_id = f"{owner_id}|orientation={orientation:+d}"
            partner_id = f"{owner_id}|orientation={-orientation:+d}"
            for repetition in range(1, FROZEN_REPETITION_CUTOFF + 1):
                repeated_length = repetition * length
                repeated_period = repetition * signed_period
                weight = 1.0 / repetition
                exponential = math.exp(
                    -REPETITION_LEDGER_S * repeated_length
                )
                direct_ruelle = (
                    weight
                    * exponential
                    * (-REPETITION_LEDGER_S * repeated_period)
                )
                cancelled_ruelle = (
                    -REPETITION_LEDGER_S * signed_period * exponential
                )
                stability_denominator = 1.0 - math.exp(-repeated_length)
                direct_selberg = direct_ruelle / stability_denominator
                cancelled_selberg = cancelled_ruelle / stability_denominator
                rows.append(
                    {
                        "primitive_owner_id": oriented_id,
                        "word": word,
                        "hecke_prime": prime,
                        "cycle_id": cycle_id,
                        "hecke_cycle_degree_d": degree,
                        "primitive_in_gamma0_11_exact": cycle[
                            "primitive_in_gamma0_11_exact"
                        ],
                        "orientation_sign": orientation,
                        "orientation_partner_id": partner_id,
                        "zeta_repetition_r": repetition,
                        "frozen_s": REPETITION_LEDGER_S,
                        "primitive_base_length": length,
                        "repeated_base_length": repeated_length,
                        "primitive_alpha_period": signed_period,
                        "repeated_alpha_period": repeated_period,
                        "log_series_weight_one_over_r": weight,
                        "ruelle_log_term": weight * exponential,
                        "ruelle_direct_first_variation": direct_ruelle,
                        "ruelle_cancelled_first_variation": cancelled_ruelle,
                        "ruelle_formula_residual": abs(
                            direct_ruelle - cancelled_ruelle
                        ),
                        "frozen_stability_denominator": stability_denominator,
                        "selberg_log_term": weight
                        * exponential
                        / stability_denominator,
                        "selberg_direct_first_variation": direct_selberg,
                        "selberg_cancelled_first_variation": cancelled_selberg,
                        "selberg_formula_residual": abs(
                            direct_selberg - cancelled_selberg
                        ),
                        "orientation_pair_cancellation_status": (
                            "PROVED_BY_SIGN_PAIRING"
                        ),
                        "owner_evidence_token": "NUMERICALLY_CERTIFIED",
                        "period_evidence_token": "NUMERICAL_OBSERVATION",
                    }
                )
    return rows


def degree_period_sums(
    rows: Sequence[dict[str, str]], field: str
) -> dict[int, float]:
    sums: dict[int, float] = defaultdict(float)
    for row in rows:
        sums[int(row["cycle_degree"])] += float(row[field])
    return dict(sorted(sums.items()))


def build_degree_moment_ledger(
    grouped: dict[tuple[str, int], list[dict[str, str]]],
    periods: dict[tuple[str, int], dict[str, str]],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for key, rows in grouped.items():
        word, prime = key
        summary = periods[key]
        eigenvalue = int(rows[0]["a_p"])
        base_alpha = float(summary["base_period_real"])
        base_complex = complex(
            float(summary["base_period_real"]),
            float(summary["base_period_imag"]),
        )
        base_control = float(summary["closed_control_base_period"])
        # Degree one carries the nonzero source-side obligation even when the
        # Hecke permutation has no degree-one output cycle.  Emit that absent
        # owner bin explicitly instead of hiding a failed condition.
        degrees = sorted({1, *(int(row["cycle_degree"]) for row in rows)})
        for degree in degrees:
            selected = [
                row for row in rows if int(row["cycle_degree"]) == degree
            ]
            alpha_sum = sum(float(row["period_real"]) for row in selected)
            complex_sum = sum(
                (
                    complex(float(row["period_real"]), float(row["period_imag"]))
                    for row in selected
                ),
                0.0j,
            )
            control_sum = sum(
                float(row["closed_control_period"]) for row in selected
            )
            required_alpha = eigenvalue * base_alpha if degree == 1 else 0.0
            required_complex = (
                eigenvalue * base_complex if degree == 1 else 0.0j
            )
            required_control = eigenvalue * base_control if degree == 1 else 0.0
            alpha_residual = abs(alpha_sum - required_alpha)
            complex_residual = abs(complex_sum - required_complex)
            control_residual = abs(control_sum - required_control)
            output.append(
                {
                    "word": word,
                    "hecke_prime": prime,
                    "a_p": eigenvalue,
                    "hecke_cycle_degree_d": degree,
                    "primitive_owner_count_at_degree": len(selected),
                    "base_alpha_period": base_alpha,
                    "alpha_period_sum_at_degree": alpha_sum,
                    "complex_period_sum_real_at_degree": complex_sum.real,
                    "complex_period_sum_imag_at_degree": complex_sum.imag,
                    "closed_control_period_sum_at_degree": control_sum,
                    "required_alpha_moment_for_all_s_recurrence": required_alpha,
                    "alpha_moment_residual": alpha_residual,
                    "alpha_moment_status": (
                        "PASS_NUMERICAL_OBSERVATION"
                        if alpha_residual <= NUMERICAL_TOLERANCE
                        else "FAILS_NAIVE_ALL_S_RECURRENCE"
                    ),
                    "required_complex_moment_real_for_all_s_recurrence": (
                        required_complex.real
                    ),
                    "required_complex_moment_imag_for_all_s_recurrence": (
                        required_complex.imag
                    ),
                    "complex_moment_residual": complex_residual,
                    "complex_moment_status": (
                        "PASS_NUMERICAL_OBSERVATION"
                        if complex_residual <= NUMERICAL_TOLERANCE
                        else "FAILS_NAIVE_ALL_S_RECURRENCE"
                    ),
                    "required_closed_control_moment_for_all_s_recurrence": (
                        required_control
                    ),
                    "closed_control_moment_residual": control_residual,
                    "closed_control_moment_status": (
                        "PASS_NUMERICAL_OBSERVATION"
                        if control_residual <= NUMERICAL_TOLERANCE
                        else "FAILS_NAIVE_ALL_S_RECURRENCE"
                    ),
                    "moment_criterion_scope": (
                        "NECESSARY_AND_SUFFICIENT_FOR_THE_NAIVE_ALL_S_IDENTITY_"
                        "ON_THIS_FINITE_HECKE_OWNER_MULTISET"
                    ),
                    "period_evidence_token": "NUMERICAL_OBSERVATION",
                }
            )
    return output


def build_hecke_variation_ledger(
    grouped: dict[tuple[str, int], list[dict[str, str]]],
    periods: dict[tuple[str, int], dict[str, str]],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for key, rows in grouped.items():
        word, prime = key
        summary = periods[key]
        eigenvalue = int(rows[0]["a_p"])
        length = primitive_length(word)
        base_alpha = float(summary["base_period_real"])
        base_control = float(summary["closed_control_base_period"])
        degrees = [int(row["cycle_degree"]) for row in rows]
        degree_pattern = "|".join(map(str, sorted(degrees)))
        profile = "MIXED_DEGREES" if len(set(degrees)) > 1 else "UNIFORM_NONUNIT"
        witness = (
            "UNWEIGHTED_RELATION_UNDERDETERMINES_LENGTH_KERNEL_MOMENTS"
            if profile == "MIXED_DEGREES"
            else "UNWEIGHTED_RELATION_FORCES_A_NONUNIT_LENGTH_KERNEL_SHIFT"
        )
        alpha_sum = sum(float(row["period_real"]) for row in rows)
        expected_alpha = eigenvalue * base_alpha
        for s_value in FROZEN_S_VALUES:
            ruelle_source = owner_first_variation(
                "ruelle",
                s_value,
                length,
                base_alpha,
                FROZEN_REPETITION_CUTOFF,
            )
            selberg_source = owner_first_variation(
                "selberg",
                s_value,
                length,
                base_alpha,
                FROZEN_REPETITION_CUTOFF,
            )
            ruelle_output = sum(
                owner_first_variation(
                    "ruelle",
                    s_value,
                    int(row["cycle_degree"]) * length,
                    float(row["period_real"]),
                    FROZEN_REPETITION_CUTOFF,
                )
                for row in rows
            )
            selberg_output = sum(
                owner_first_variation(
                    "selberg",
                    s_value,
                    int(row["cycle_degree"]) * length,
                    float(row["period_real"]),
                    FROZEN_REPETITION_CUTOFF,
                )
                for row in rows
            )
            ruelle_prediction = eigenvalue * ruelle_source
            selberg_prediction = eigenvalue * selberg_source
            ruelle_residual = abs(ruelle_output - ruelle_prediction)
            selberg_residual = abs(selberg_output - selberg_prediction)

            ruelle_control_source = owner_first_variation(
                "ruelle",
                s_value,
                length,
                base_control,
                FROZEN_REPETITION_CUTOFF,
            )
            selberg_control_source = owner_first_variation(
                "selberg",
                s_value,
                length,
                base_control,
                FROZEN_REPETITION_CUTOFF,
            )
            ruelle_control_output = sum(
                owner_first_variation(
                    "ruelle",
                    s_value,
                    int(row["cycle_degree"]) * length,
                    float(row["closed_control_period"]),
                    FROZEN_REPETITION_CUTOFF,
                )
                for row in rows
            )
            selberg_control_output = sum(
                owner_first_variation(
                    "selberg",
                    s_value,
                    int(row["cycle_degree"]) * length,
                    float(row["closed_control_period"]),
                    FROZEN_REPETITION_CUTOFF,
                )
                for row in rows
            )
            output.append(
                {
                    "word": word,
                    "hecke_prime": prime,
                    "a_p": eigenvalue,
                    "frozen_s": s_value,
                    "zeta_repetition_cutoff_R": FROZEN_REPETITION_CUTOFF,
                    "source_primitive_base_length": length,
                    "source_alpha_period": base_alpha,
                    "source_closed_control_period": base_control,
                    "output_primitive_owner_count": len(rows),
                    "hecke_cycle_degree_pattern": degree_pattern,
                    "degree_profile_type": profile,
                    "hecke_degree_is_zeta_repetition": "false",
                    "all_output_owners_primitive_exact": "true",
                    "unweighted_output_alpha_period_sum": alpha_sum,
                    "unweighted_expected_alpha_period_sum": expected_alpha,
                    "unweighted_alpha_residual": abs(alpha_sum - expected_alpha),
                    "ruelle_source_first_variation": ruelle_source,
                    "ruelle_hecke_output_first_variation_one_sided": ruelle_output,
                    "ruelle_naive_a_p_prediction": ruelle_prediction,
                    "ruelle_naive_recurrence_residual": ruelle_residual,
                    "ruelle_naive_recurrence_status": (
                        "PASS_NUMERICAL_OBSERVATION"
                        if ruelle_residual <= NUMERICAL_TOLERANCE
                        else "FAILS_NAIVE_HECKE_RECURRENCE"
                    ),
                    "selberg_source_first_variation": selberg_source,
                    "selberg_hecke_output_first_variation_one_sided": (
                        selberg_output
                    ),
                    "selberg_naive_a_p_prediction": selberg_prediction,
                    "selberg_naive_recurrence_residual": selberg_residual,
                    "selberg_naive_recurrence_status": (
                        "PASS_NUMERICAL_OBSERVATION"
                        if selberg_residual <= NUMERICAL_TOLERANCE
                        else "FAILS_NAIVE_HECKE_RECURRENCE"
                    ),
                    "ruelle_closed_control_recurrence_residual": abs(
                        ruelle_control_output - eigenvalue * ruelle_control_source
                    ),
                    "selberg_closed_control_recurrence_residual": abs(
                        selberg_control_output - eigenvalue * selberg_control_source
                    ),
                    "canonical_inverse_paired_ruelle_first_variation": 0.0,
                    "canonical_inverse_paired_selberg_first_variation": 0.0,
                    "canonical_orientation_pairing_status": (
                        "PROVED_EXACT_ZERO_BEFORE_TRUNCATION_LIMIT"
                    ),
                    "formal_no_implication_witness": witness,
                    "analytic_evidence_token": "PROVED",
                    "finite_period_evidence_token": "NUMERICAL_OBSERVATION",
                }
            )
    return output


def validate_generated_artifacts(
    repetition_rows: Sequence[dict[str, object]],
    moment_rows: Sequence[dict[str, object]],
    variation_rows: Sequence[dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    if len(repetition_rows) != 138 * 2 * FROZEN_REPETITION_CUTOFF:
        errors.append("unexpected repetition-ledger row count")
    if len(moment_rows) != 110:
        errors.append("unexpected degree-moment row count")
    if len(variation_rows) != 55 * len(FROZEN_S_VALUES):
        errors.append("unexpected Hecke-variation row count")
    if any(float(row["ruelle_formula_residual"]) > 1.0e-15 for row in repetition_rows):
        errors.append("Ruelle repetition cancellation formula failed")
    if any(float(row["selberg_formula_residual"]) > 1.0e-15 for row in repetition_rows):
        errors.append("Selberg repetition cancellation formula failed")
    if any(row["hecke_degree_is_zeta_repetition"] != "false" for row in variation_rows):
        errors.append("Hecke cycle degree was mixed with zeta repetition")
    return errors


def write_csv(
    path: Path, rows: Iterable[dict[str, object]], fields: Sequence[str]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def group_moment_status_counts(
    rows: Sequence[dict[str, object]], field: str
) -> tuple[int, int]:
    grouped: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["word"]), int(row["hecke_prime"]))].append(row)
    failures = sum(
        any(float(row[field]) > NUMERICAL_TOLERANCE for row in values)
        for values in grouped.values()
    )
    return failures, len(grouped) - failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--round4-cycle-ledger",
        type=Path,
        default=DEFAULT_ROUND4_CYCLE_LEDGER,
    )
    parser.add_argument(
        "--round4-period-summary",
        type=Path,
        default=DEFAULT_ROUND4_PERIOD_SUMMARY,
    )
    args = parser.parse_args()

    cycle_rows = read_csv(args.round4_cycle_ledger)
    period_rows = read_csv(args.round4_period_summary)
    errors = validate_round4_inputs(cycle_rows, period_rows)
    grouped = grouped_cycle_rows(cycle_rows)
    periods = period_summary_map(period_rows)
    repetition_rows = build_repetition_ledger(cycle_rows)
    moment_rows = build_degree_moment_ledger(grouped, periods)
    variation_rows = build_hecke_variation_ledger(grouped, periods)
    errors.extend(
        validate_generated_artifacts(repetition_rows, moment_rows, variation_rows)
    )

    args.output.mkdir(parents=True, exist_ok=True)
    repetition_path = args.output / "round5_zeta_repetition_ledger.csv"
    moment_path = args.output / "round5_degree_moment_ledger.csv"
    variation_path = args.output / "round5_hecke_zeta_variation_ledger.csv"
    summary_path = args.output / "round5_summary.json"
    manifest_path = args.output / "round5_artifact_manifest.json"
    write_csv(repetition_path, repetition_rows, REPETITION_FIELDS)
    write_csv(moment_path, moment_rows, DEGREE_MOMENT_FIELDS)
    write_csv(variation_path, variation_rows, HECKE_VARIATION_FIELDS)

    alpha_moment_failures, alpha_moment_passes = group_moment_status_counts(
        moment_rows, "alpha_moment_residual"
    )
    complex_moment_failures, complex_moment_passes = group_moment_status_counts(
        moment_rows, "complex_moment_residual"
    )
    control_moment_failures, control_moment_passes = group_moment_status_counts(
        moment_rows, "closed_control_moment_residual"
    )
    mixed_groups = sum(
        len({int(row["cycle_degree"]) for row in values}) > 1
        for values in grouped.values()
    )
    summary = {
        "schema": "p26_round5_zeta_variation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "zeta_convention": {
            "product": "RECIPROCAL_PRIMITIVE_ORBIT_PRODUCT",
            "owner": "ORIENTED_PRIMITIVE_GAMMA0_11_FLOW_ORBIT",
            "ruelle_log_term": "exp(-s*r*T_epsilon(gamma))/r",
            "selberg_frozen_stability_log_term": (
                "exp(-s*r*T_epsilon(gamma))/(r*(1-exp(-r*ell(gamma))))"
            ),
            "reciprocal_convention_effect": (
                "switching to the nonreciprocal product flips the derivative sign "
                "but not the zero or no-implication results"
            ),
        },
        "frozen_s_values": list(FROZEN_S_VALUES),
        "frozen_zeta_repetition_cutoff": FROZEN_REPETITION_CUTOFF,
        "selected_source_owners": len(ROUND2.gamma0_11_positive_necklaces(9)),
        "hecke_word_prime_groups": len(grouped),
        "round4_primitive_cycle_owners_consumed": len(cycle_rows),
        "orientation_repetition_rows": len(repetition_rows),
        "degree_moment_rows": len(moment_rows),
        "hecke_zeta_variation_rows": len(variation_rows),
        "mixed_degree_groups": mixed_groups,
        "uniform_nonunit_degree_groups": len(grouped) - mixed_groups,
        "unweighted_hecke_period_groups_passing": sum(
            float(row["unweighted_alpha_residual"]) <= NUMERICAL_TOLERANCE
            for row in variation_rows[:: len(FROZEN_S_VALUES)]
        ),
        "naive_ruelle_recurrence_failures": sum(
            row["ruelle_naive_recurrence_status"]
            == "FAILS_NAIVE_HECKE_RECURRENCE"
            for row in variation_rows
        ),
        "naive_selberg_recurrence_failures": sum(
            row["selberg_naive_recurrence_status"]
            == "FAILS_NAIVE_HECKE_RECURRENCE"
            for row in variation_rows
        ),
        "alpha_all_s_degree_moment_groups_failing": alpha_moment_failures,
        "alpha_all_s_degree_moment_groups_passing_numerically": alpha_moment_passes,
        "complex_all_s_degree_moment_groups_failing": complex_moment_failures,
        "complex_all_s_degree_moment_groups_passing_numerically": (
            complex_moment_passes
        ),
        "closed_control_all_s_degree_moment_groups_failing": (
            control_moment_failures
        ),
        "closed_control_all_s_degree_moment_groups_passing_numerically": (
            control_moment_passes
        ),
        "maximum_ruelle_naive_recurrence_residual": max(
            float(row["ruelle_naive_recurrence_residual"])
            for row in variation_rows
        ),
        "maximum_selberg_naive_recurrence_residual": max(
            float(row["selberg_naive_recurrence_residual"])
            for row in variation_rows
        ),
        "analytic_results": {
            "oriented_inverse_pair_first_variation": (
                "PROVED_EXACT_ZERO_FOR_INVERSE_CLOSED_OWNER_FAMILIES"
            ),
            "degree_moment_criterion": (
                "PROVED_NECESSARY_AND_SUFFICIENT_FOR_NAIVE_ALL_S_HECKE_"
                "RECURRENCE_ON_A_FINITE_OUTPUT_MULTISET"
            ),
            "hecke_period_relation_implies_zeta_recurrence": False,
            "primitive_euler_factorization": False,
            "discriminative_hecke_euler_evidence": "STOP_SCOPED",
        },
        "evidence_tokens": {
            "orientation_and_moment_theorems": "PROVED",
            "finite_owner_and_repetition_bookkeeping": "NUMERICALLY_CERTIFIED",
            "round4_period_weighted_residuals": "NUMERICAL_OBSERVATION",
        },
        "source_inputs": [
            {
                "path": args.round4_cycle_ledger.name,
                "sha256": sha256(args.round4_cycle_ledger),
            },
            {
                "path": args.round4_period_summary.name,
                "sha256": sha256(args.round4_period_summary),
            },
        ],
        "claim_boundary": {
            "finite_positive_orientation_half_ledger_is_canonical_global_zeta": False,
            "complete_gamma0_11_primitive_enumeration": False,
            "global_zeta_convergence_or_continuation_proved_here": False,
            "a2_dynamical_zeta_evaluation_run": False,
            "formal_route_a_tuple": "UNASSIGNED",
            "route_b_evaluation": "NOT_RUN",
            "route_b_invocation_allowed": False,
            "prime_target_table_used": False,
            "riemann_zero_data_used": False,
        },
        "errors": errors,
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    primary_paths = (repetition_path, moment_path, variation_path, summary_path)
    manifest = {
        "schema": "p26_round5_artifact_manifest/1.0",
        "artifacts": [
            {
                "path": path.name,
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
            for path in primary_paths
        ],
        "source_inputs": [
            {
                "path": args.round4_cycle_ledger.name,
                "sha256": sha256(args.round4_cycle_ledger),
                "bytes": args.round4_cycle_ledger.stat().st_size,
            },
            {
                "path": args.round4_period_summary.name,
                "sha256": sha256(args.round4_period_summary),
                "bytes": args.round4_period_summary.stat().st_size,
            },
        ],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
