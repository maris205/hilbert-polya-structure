#!/usr/bin/env python3
"""Paper-26 Round-6 inverse-paired second-variation audit.

This builder consumes the frozen Round-4 Hecke cycle/period ledgers and reuses
the Round-5 source conventions.  It proves and replays a *local finite-product*
second-variation identity.  It does not enumerate all primitive Gamma_0(11)
classes, construct a global determinant, count roots, run Route-A A2, or use a
prime/zero target table.
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
from typing import Sequence


DATE = "2026-08-28"
FORMAL_TUPLE = (
    "(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)"
)
PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_ROUND4_CYCLE_LEDGER = (
    PROJECT_DIR / "results" / "round4_hecke_cycle_ledger.csv"
)
DEFAULT_ROUND4_PERIOD_SUMMARY = (
    PROJECT_DIR / "results" / "round4_hecke_period_summary.csv"
)
EXPECTED_CYCLE_SHA256 = (
    "f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662"
)
EXPECTED_PERIOD_SHA256 = (
    "c5de5c16c86d8db6ce7438c122deddb927d934bf0198fe3f72af4cbaf1233679"
)
FROZEN_S_VALUES = (0.125, 0.25, 0.5)
FROZEN_REPETITION_CUTOFF = 4
PAIR_LEDGER_S = 0.25
NUMERICAL_TOLERANCE = 1.0e-10


PAIR_FIELDS = (
    "primitive_axis_id",
    "word",
    "hecke_prime",
    "cycle_id",
    "hecke_cycle_degree_d",
    "primitive_in_gamma0_11_exact",
    "orientation_pair",
    "zeta_repetition_r",
    "frozen_s",
    "primitive_base_length",
    "repeated_base_length",
    "primitive_alpha_period_squared",
    "repeated_alpha_period_squared",
    "log_series_weight_one_over_r",
    "second_derivative_repetition_factor_r",
    "canonical_pair_first_variation",
    "ruelle_pair_second_variation_direct",
    "ruelle_pair_second_variation_formula",
    "ruelle_pair_formula_residual",
    "frozen_stability_denominator",
    "selberg_pair_second_variation_direct",
    "selberg_pair_second_variation_formula",
    "selberg_pair_formula_residual",
    "orientation_pair_second_variation_status",
    "owner_evidence_token",
    "period_evidence_token",
)

MOMENT_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "hecke_cycle_degree_d",
    "primitive_owner_count_at_degree",
    "base_alpha_period_squared",
    "quadratic_alpha_moment_Q_d",
    "required_Q_d_lambda_a_p",
    "lambda_a_p_moment_residual",
    "lambda_a_p_moment_status",
    "required_Q_d_lambda_a_p_squared",
    "lambda_a_p_squared_moment_residual",
    "lambda_a_p_squared_moment_status",
    "required_Q_d_lambda_a_p_squared_minus_p",
    "lambda_a_p_squared_minus_p_moment_residual",
    "lambda_a_p_squared_minus_p_moment_status",
    "secondary_control_role",
    "quadratic_moment_criterion_scope",
    "period_evidence_token",
)

VARIATION_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "frozen_s",
    "zeta_repetition_cutoff_R",
    "source_primitive_base_length",
    "source_alpha_period_squared",
    "output_primitive_owner_count",
    "hecke_cycle_degree_pattern",
    "degree_profile_type",
    "hecke_degree_is_zeta_repetition",
    "canonical_inverse_pair_first_variation",
    "ruelle_source_pair_second_variation",
    "ruelle_hecke_output_pair_second_variation",
    "ruelle_lambda_a_p_prediction",
    "ruelle_lambda_a_p_residual",
    "ruelle_lambda_a_p_status",
    "ruelle_lambda_a_p_squared_prediction",
    "ruelle_lambda_a_p_squared_residual",
    "ruelle_lambda_a_p_squared_status",
    "ruelle_secondary_a_p_squared_minus_p_prediction",
    "ruelle_secondary_a_p_squared_minus_p_residual",
    "ruelle_secondary_a_p_squared_minus_p_status",
    "selberg_source_pair_second_variation",
    "selberg_hecke_output_pair_second_variation",
    "selberg_lambda_a_p_prediction",
    "selberg_lambda_a_p_residual",
    "selberg_lambda_a_p_status",
    "selberg_lambda_a_p_squared_prediction",
    "selberg_lambda_a_p_squared_residual",
    "selberg_lambda_a_p_squared_status",
    "selberg_secondary_a_p_squared_minus_p_prediction",
    "selberg_secondary_a_p_squared_minus_p_residual",
    "selberg_secondary_a_p_squared_minus_p_status",
    "lambda_a_p_degree_moment_group_status",
    "lambda_a_p_squared_degree_moment_group_status",
    "secondary_a_p_squared_minus_p_degree_moment_group_status",
    "formal_a2_evaluation_run",
    "analytic_evidence_token",
    "finite_period_evidence_token",
)


def _load_round5_module():
    module_path = Path(__file__).with_name("round5_zeta_variation.py")
    spec = importlib.util.spec_from_file_location("p26_round5_for_round6", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load round5_zeta_variation.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROUND5 = _load_round5_module()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def second_kernel(
    kind: str, s_value: float, length: float, repetition_cutoff: int
) -> float:
    """Return sum_r r exp(-s r L), with the frozen Selberg denominator."""

    if kind not in {"ruelle", "selberg"}:
        raise ValueError(f"unknown kernel kind: {kind!r}")
    if s_value <= 0.0 or length <= 0.0 or repetition_cutoff <= 0:
        raise ValueError("kernel arguments must be positive")
    total = 0.0
    for repetition in range(1, repetition_cutoff + 1):
        term = repetition * math.exp(-s_value * repetition * length)
        if kind == "selberg":
            term /= 1.0 - math.exp(-repetition * length)
        total += term
    return total


def owner_pair_second_variation(
    kind: str,
    s_value: float,
    length: float,
    alpha_period: float,
    repetition_cutoff: int,
) -> float:
    """Canonical inverse-pair second derivative at epsilon=0."""

    return (
        2.0
        * s_value
        * s_value
        * alpha_period
        * alpha_period
        * second_kernel(kind, s_value, length, repetition_cutoff)
    )


def quadratic_dirichlet_coefficient(
    degree_moments: dict[int, float], exponent: int
) -> float:
    """Coefficient after removing the common factor n (and Selberg factor).

    The q^n coefficient of the Ruelle second-variation kernel is
    n * sum_(d|n) Q_d/d.  The frozen-stability Selberg kernel has the same
    numerator times the common nonzero factor (1-exp(-nL))^-1.
    """

    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return sum(
        value / degree
        for degree, value in degree_moments.items()
        if exponent % degree == 0
    )


def grouped_cycle_rows(
    rows: Sequence[dict[str, str]],
) -> dict[tuple[str, int], list[dict[str, str]]]:
    output: dict[tuple[str, int], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        output[(row["word"], int(row["hecke_prime"]))].append(row)
    return dict(output)


def period_summary_map(
    rows: Sequence[dict[str, str]],
) -> dict[tuple[str, int], dict[str, str]]:
    output: dict[tuple[str, int], dict[str, str]] = {}
    for row in rows:
        key = (row["word"], int(row["hecke_prime"]))
        if key in output:
            raise ValueError(f"duplicate period-summary key: {key!r}")
        output[key] = row
    return output


def validate_inputs(
    cycle_path: Path,
    period_path: Path,
    cycle_rows: Sequence[dict[str, str]],
    period_rows: Sequence[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    if sha256(cycle_path) != EXPECTED_CYCLE_SHA256:
        errors.append("Round-4 cycle-ledger SHA-256 mismatch")
    if sha256(period_path) != EXPECTED_PERIOD_SHA256:
        errors.append("Round-4 period-summary SHA-256 mismatch")
    errors.extend(ROUND5.validate_round4_inputs(cycle_rows, period_rows))
    return errors


def build_pair_ledger(
    cycle_rows: Sequence[dict[str, str]],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for row in cycle_rows:
        word = row["word"]
        prime = int(row["hecke_prime"])
        cycle_id = int(row["cycle_id"])
        degree = int(row["cycle_degree"])
        length = degree * ROUND5.primitive_length(word)
        period = float(row["period_real"])
        for repetition in range(1, FROZEN_REPETITION_CUTOFF + 1):
            repeated_length = repetition * length
            repeated_period_squared = repetition * repetition * period * period
            exponential = math.exp(-PAIR_LEDGER_S * repeated_length)
            weight = 1.0 / repetition
            single_orientation_direct = (
                weight
                * exponential
                * (PAIR_LEDGER_S * repetition * period) ** 2
            )
            pair_direct = 2.0 * single_orientation_direct
            pair_formula = (
                2.0
                * PAIR_LEDGER_S
                * PAIR_LEDGER_S
                * repetition
                * period
                * period
                * exponential
            )
            denominator = 1.0 - math.exp(-repeated_length)
            output.append(
                {
                    "primitive_axis_id": f"{word}|p={prime}|O={cycle_id}",
                    "word": word,
                    "hecke_prime": prime,
                    "cycle_id": cycle_id,
                    "hecke_cycle_degree_d": degree,
                    "primitive_in_gamma0_11_exact": row[
                        "primitive_in_gamma0_11_exact"
                    ],
                    "orientation_pair": "+1|-1",
                    "zeta_repetition_r": repetition,
                    "frozen_s": PAIR_LEDGER_S,
                    "primitive_base_length": length,
                    "repeated_base_length": repeated_length,
                    "primitive_alpha_period_squared": period * period,
                    "repeated_alpha_period_squared": repeated_period_squared,
                    "log_series_weight_one_over_r": weight,
                    "second_derivative_repetition_factor_r": repetition,
                    "canonical_pair_first_variation": 0.0,
                    "ruelle_pair_second_variation_direct": pair_direct,
                    "ruelle_pair_second_variation_formula": pair_formula,
                    "ruelle_pair_formula_residual": abs(pair_direct - pair_formula),
                    "frozen_stability_denominator": denominator,
                    "selberg_pair_second_variation_direct": pair_direct / denominator,
                    "selberg_pair_second_variation_formula": pair_formula / denominator,
                    "selberg_pair_formula_residual": abs(
                        pair_direct / denominator - pair_formula / denominator
                    ),
                    "orientation_pair_second_variation_status": (
                        "PROVED_ADDS_AND_IS_ORIENTATION_EVEN"
                    ),
                    "owner_evidence_token": "NUMERICALLY_CERTIFIED",
                    "period_evidence_token": "NUMERICAL_OBSERVATION",
                }
            )
    return output


def lambda_value(kind: str, eigenvalue: int, prime: int) -> int:
    if kind == "a_p":
        return eigenvalue
    if kind == "a_p_squared":
        return eigenvalue * eigenvalue
    if kind == "a_p_squared_minus_p":
        return eigenvalue * eigenvalue - prime
    raise ValueError(f"unknown lambda kind: {kind!r}")


def build_quadratic_moment_ledger(
    grouped: dict[tuple[str, int], list[dict[str, str]]],
    periods: dict[tuple[str, int], dict[str, str]],
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for key, rows in grouped.items():
        word, prime = key
        eigenvalue = int(rows[0]["a_p"])
        base_period = float(periods[key]["base_period_real"])
        base_square = base_period * base_period
        degrees = sorted({1, *(int(row["cycle_degree"]) for row in rows)})
        for degree in degrees:
            selected = [row for row in rows if int(row["cycle_degree"]) == degree]
            quadratic_moment = sum(float(row["period_real"]) ** 2 for row in selected)
            values: dict[str, object] = {}
            for kind in ("a_p", "a_p_squared", "a_p_squared_minus_p"):
                required = (
                    lambda_value(kind, eigenvalue, prime) * base_square
                    if degree == 1
                    else 0.0
                )
                residual = abs(quadratic_moment - required)
                values[f"required_Q_d_lambda_{kind}"] = required
                values[f"lambda_{kind}_moment_residual"] = residual
                values[f"lambda_{kind}_moment_status"] = (
                    "PASS_NUMERICAL_OBSERVATION"
                    if residual <= NUMERICAL_TOLERANCE
                    else "FAILS_NAIVE_ALL_S_SECOND_VARIATION_RECURRENCE"
                )
            output.append(
                {
                    "word": word,
                    "hecke_prime": prime,
                    "a_p": eigenvalue,
                    "hecke_cycle_degree_d": degree,
                    "primitive_owner_count_at_degree": len(selected),
                    "base_alpha_period_squared": base_square,
                    "quadratic_alpha_moment_Q_d": quadratic_moment,
                    **values,
                    "secondary_control_role": (
                        "A_P_SQUARED_MINUS_P_IS_AN_EXPLICIT_SECONDARY_NEGATIVE_"
                        "CONTROL_NOT_THE_THEORETICAL_TARGET"
                    ),
                    "quadratic_moment_criterion_scope": (
                        "NECESSARY_AND_SUFFICIENT_FOR_A_PREDECLARED_P_ONLY_SCALAR_"
                        "ALL_S_IDENTITY_ON_THIS_FINITE_HECKE_OWNER_MULTISET"
                    ),
                    "period_evidence_token": "NUMERICAL_OBSERVATION",
                }
            )
    return output


def group_moment_statuses(
    moment_rows: Sequence[dict[str, object]], kind: str
) -> dict[tuple[str, int], str]:
    grouped: dict[tuple[str, int], list[float]] = defaultdict(list)
    field = f"lambda_{kind}_moment_residual"
    for row in moment_rows:
        grouped[(str(row["word"]), int(row["hecke_prime"]))].append(
            float(row[field])
        )
    return {
        key: (
            "PASS_NUMERICAL_OBSERVATION"
            if max(residuals) <= NUMERICAL_TOLERANCE
            else "FAILS_NAIVE_ALL_S_SECOND_VARIATION_RECURRENCE"
        )
        for key, residuals in grouped.items()
    }


def recurrence_status(residual: float) -> str:
    return (
        "PASS_NUMERICAL_OBSERVATION"
        if residual <= NUMERICAL_TOLERANCE
        else "FAILS_NAIVE_HECKE_SECOND_VARIATION_RECURRENCE"
    )


def build_variation_ledger(
    grouped: dict[tuple[str, int], list[dict[str, str]]],
    periods: dict[tuple[str, int], dict[str, str]],
    moment_rows: Sequence[dict[str, object]],
) -> list[dict[str, object]]:
    moment_status = {
        kind: group_moment_statuses(moment_rows, kind)
        for kind in ("a_p", "a_p_squared", "a_p_squared_minus_p")
    }
    output: list[dict[str, object]] = []
    for key, rows in grouped.items():
        word, prime = key
        eigenvalue = int(rows[0]["a_p"])
        base_length = ROUND5.primitive_length(word)
        base_period = float(periods[key]["base_period_real"])
        degrees = [int(row["cycle_degree"]) for row in rows]
        degree_pattern = "|".join(map(str, sorted(degrees)))
        profile = "MIXED_DEGREES" if len(set(degrees)) > 1 else "UNIFORM_NONUNIT"
        for s_value in FROZEN_S_VALUES:
            kernel_values: dict[str, object] = {}
            for kernel_kind in ("ruelle", "selberg"):
                source = owner_pair_second_variation(
                    kernel_kind,
                    s_value,
                    base_length,
                    base_period,
                    FROZEN_REPETITION_CUTOFF,
                )
                hecke_output = sum(
                    owner_pair_second_variation(
                        kernel_kind,
                        s_value,
                        int(row["cycle_degree"]) * base_length,
                        float(row["period_real"]),
                        FROZEN_REPETITION_CUTOFF,
                    )
                    for row in rows
                )
                kernel_values[f"{kernel_kind}_source_pair_second_variation"] = source
                kernel_values[
                    f"{kernel_kind}_hecke_output_pair_second_variation"
                ] = hecke_output
                for lambda_kind, label in (
                    ("a_p", "lambda_a_p"),
                    ("a_p_squared", "lambda_a_p_squared"),
                    (
                        "a_p_squared_minus_p",
                        "secondary_a_p_squared_minus_p",
                    ),
                ):
                    prediction = lambda_value(lambda_kind, eigenvalue, prime) * source
                    residual = abs(hecke_output - prediction)
                    kernel_values[f"{kernel_kind}_{label}_prediction"] = prediction
                    kernel_values[f"{kernel_kind}_{label}_residual"] = residual
                    kernel_values[f"{kernel_kind}_{label}_status"] = recurrence_status(
                        residual
                    )
            output.append(
                {
                    "word": word,
                    "hecke_prime": prime,
                    "a_p": eigenvalue,
                    "frozen_s": s_value,
                    "zeta_repetition_cutoff_R": FROZEN_REPETITION_CUTOFF,
                    "source_primitive_base_length": base_length,
                    "source_alpha_period_squared": base_period * base_period,
                    "output_primitive_owner_count": len(rows),
                    "hecke_cycle_degree_pattern": degree_pattern,
                    "degree_profile_type": profile,
                    "hecke_degree_is_zeta_repetition": "false",
                    "canonical_inverse_pair_first_variation": 0.0,
                    **kernel_values,
                    "lambda_a_p_degree_moment_group_status": moment_status["a_p"][key],
                    "lambda_a_p_squared_degree_moment_group_status": moment_status[
                        "a_p_squared"
                    ][key],
                    "secondary_a_p_squared_minus_p_degree_moment_group_status": (
                        moment_status["a_p_squared_minus_p"][key]
                    ),
                    "formal_a2_evaluation_run": "false",
                    "analytic_evidence_token": "PROVED",
                    "finite_period_evidence_token": "NUMERICAL_OBSERVATION",
                }
            )
    return output


def write_csv(path: Path, rows: Sequence[dict[str, object]], fields: Sequence[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def count_failures(rows: Sequence[dict[str, object]], field: str) -> int:
    return sum(str(row[field]).startswith("FAILS_") for row in rows)


def count_group_statuses(
    moment_rows: Sequence[dict[str, object]], kind: str
) -> tuple[int, int]:
    statuses = group_moment_statuses(moment_rows, kind)
    failures = sum(value.startswith("FAILS_") for value in statuses.values())
    return failures, len(statuses) - failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--round4-cycle-ledger", type=Path, default=DEFAULT_ROUND4_CYCLE_LEDGER
    )
    parser.add_argument(
        "--round4-period-summary", type=Path, default=DEFAULT_ROUND4_PERIOD_SUMMARY
    )
    args = parser.parse_args()

    cycle_rows = read_csv(args.round4_cycle_ledger)
    period_rows = read_csv(args.round4_period_summary)
    input_errors = validate_inputs(
        args.round4_cycle_ledger,
        args.round4_period_summary,
        cycle_rows,
        period_rows,
    )
    grouped = grouped_cycle_rows(cycle_rows)
    periods = period_summary_map(period_rows)
    pair_rows = build_pair_ledger(cycle_rows)
    moment_rows = build_quadratic_moment_ledger(grouped, periods)
    variation_rows = build_variation_ledger(grouped, periods, moment_rows)

    errors = list(input_errors)
    if len(pair_rows) != 138 * FROZEN_REPETITION_CUTOFF:
        errors.append("unexpected inverse-pair ledger row count")
    if len(moment_rows) != 110:
        errors.append("unexpected quadratic degree-moment row count")
    if len(variation_rows) != 55 * len(FROZEN_S_VALUES):
        errors.append("unexpected second-variation ledger row count")
    if any(row["formal_a2_evaluation_run"] != "false" for row in variation_rows):
        errors.append("formal A2 boundary was not preserved")

    args.output.mkdir(parents=True, exist_ok=True)
    pair_path = args.output / "round6_inverse_pair_second_variation_ledger.csv"
    moment_path = args.output / "round6_quadratic_degree_moment_ledger.csv"
    variation_path = args.output / "round6_hecke_second_variation_ledger.csv"
    summary_path = args.output / "round6_summary.json"
    manifest_path = args.output / "round6_artifact_manifest.json"
    write_csv(pair_path, pair_rows, PAIR_FIELDS)
    write_csv(moment_path, moment_rows, MOMENT_FIELDS)
    write_csv(variation_path, variation_rows, VARIATION_FIELDS)

    group_counts = {
        kind: count_group_statuses(moment_rows, kind)
        for kind in ("a_p", "a_p_squared", "a_p_squared_minus_p")
    }
    nonunit_mass_by_group: dict[tuple[str, int], float] = defaultdict(float)
    for row in moment_rows:
        if int(row["hecke_cycle_degree_d"]) > 1:
            nonunit_mass_by_group[(str(row["word"]), int(row["hecke_prime"]))] += float(
                row["quadratic_alpha_moment_Q_d"]
            )
    survivors = sorted(
        f"{word}|p={prime}"
        for (word, prime), status in group_moment_statuses(
            moment_rows, "a_p_squared"
        ).items()
        if status == "PASS_NUMERICAL_OBSERVATION"
    )
    summary = {
        "schema": "p26_round6_inverse_pair_second_variation/1.0",
        "date": DATE,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "selected_source_owners": 11,
        "hecke_word_prime_groups": 55,
        "round4_primitive_cycle_owner_instances_consumed": 138,
        "inverse_pair_repetition_rows": len(pair_rows),
        "quadratic_degree_moment_rows": len(moment_rows),
        "hecke_second_variation_rows": len(variation_rows),
        "frozen_s_values": list(FROZEN_S_VALUES),
        "frozen_zeta_repetition_cutoff": FROZEN_REPETITION_CUTOFF,
        "groups_with_nonunit_quadratic_mass_above_tolerance": sum(
            value > NUMERICAL_TOLERANCE for value in nonunit_mass_by_group.values()
        ),
        "lambda_a_p_degree_moment_groups_failing": group_counts["a_p"][0],
        "lambda_a_p_degree_moment_groups_passing_numerically": group_counts["a_p"][1],
        "lambda_a_p_squared_degree_moment_groups_failing": group_counts[
            "a_p_squared"
        ][0],
        "lambda_a_p_squared_degree_moment_groups_passing_numerically": group_counts[
            "a_p_squared"
        ][1],
        "secondary_a_p_squared_minus_p_degree_moment_groups_failing": group_counts[
            "a_p_squared_minus_p"
        ][0],
        "secondary_a_p_squared_minus_p_degree_moment_groups_passing_numerically": (
            group_counts["a_p_squared_minus_p"][1]
        ),
        "lambda_a_p_ruelle_row_failures": count_failures(
            variation_rows, "ruelle_lambda_a_p_status"
        ),
        "lambda_a_p_selberg_row_failures": count_failures(
            variation_rows, "selberg_lambda_a_p_status"
        ),
        "lambda_a_p_squared_ruelle_row_failures": count_failures(
            variation_rows, "ruelle_lambda_a_p_squared_status"
        ),
        "lambda_a_p_squared_selberg_row_failures": count_failures(
            variation_rows, "selberg_lambda_a_p_squared_status"
        ),
        "secondary_a_p_squared_minus_p_ruelle_row_failures": count_failures(
            variation_rows, "ruelle_secondary_a_p_squared_minus_p_status"
        ),
        "secondary_a_p_squared_minus_p_selberg_row_failures": count_failures(
            variation_rows, "selberg_secondary_a_p_squared_minus_p_status"
        ),
        "lambda_a_p_squared_finite_numerical_survivors": survivors,
        "analytic_results": {
            "canonical_inverse_pair_first_variation": "PROVED_EXACT_ZERO",
            "canonical_inverse_pair_second_variation": (
                "PROVED_ORIENTATION_EVEN_AND_NONNEGATIVE_FOR_FINITE_OR_"
                "ABSOLUTELY_LOCALLY_UNIFORMLY_CONVERGENT_OWNER_FAMILIES"
            ),
            "quadratic_degree_moment_criterion": (
                "PROVED_NECESSARY_AND_SUFFICIENT_FOR_ANY_PREDECLARED_P_ONLY_"
                "SCALAR_ALL_S_RECURRENCE_ON_A_FINITE_OUTPUT_MULTISET"
            ),
            "hecke_linear_period_relation_implies_quadratic_recurrence": False,
            "a_p_squared_minus_p_role": "SECONDARY_NEGATIVE_CONTROL_ONLY",
        },
        "source_inputs": [
            {"path": args.round4_cycle_ledger.name, "sha256": sha256(args.round4_cycle_ledger)},
            {"path": args.round4_period_summary.name, "sha256": sha256(args.round4_period_summary)},
        ],
        "claim_boundary": {
            "ars_stage": "STAGE_1_RESEARCH",
            "proposal_stage": "STAGE_1_ROUTE_A_A0_A1",
            "formal_route_a_tuple": FORMAL_TUPLE,
            "formal_a0_verdict": "A0_WEAK_ARITHMETIC_RELATION",
            "formal_a1_verdict": "A1_WEAK",
            "formal_a2_a4_verdicts": "FAIL_NOT_TESTABLE",
            "overall_route_a_status": "ROUTE_A_EXPLORATORY",
            "a2_dynamical_zeta_evaluation_run": False,
            "finite_local_log_product_audit_only": True,
            "complete_gamma0_11_primitive_enumeration": False,
            "global_zeta_convergence_or_continuation_proved_here": False,
            "root_count_or_zero_matching_run": False,
            "primitive_euler_factorization": False,
            "route_b_evaluation": "NOT_RUN",
            "route_b_invocation_allowed": False,
            "prime_target_table_used": False,
            "riemann_zero_data_used": False,
        },
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    primary_paths = (pair_path, moment_path, variation_path, summary_path)
    manifest = {
        "schema": "p26_round6_artifact_manifest/1.0",
        "artifacts": [
            {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in primary_paths
        ],
        "source_inputs": summary["source_inputs"],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
