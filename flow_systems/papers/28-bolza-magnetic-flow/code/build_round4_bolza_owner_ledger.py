#!/usr/bin/env python3
"""Build the first source-locked Bolza magnetic-orbit owner ledger.

The target-free ledger uses four inverse-paired primitive axes per field and
the signed repetition index ``k`` from Kordyukov--Taimanov equation (19).  The
``k`` and ``-k`` rows are trace branches of the same axis owner, not two owner
credits.  Repetitions have absolute value 1--3.  This is deliberately not a
complete length-spectrum enumeration.
"""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path
from typing import Iterable, Sequence


DECIMAL_PRECISION = 120
DISPLAY_DIGITS = 70
REPETITIONS = (1, 2, 3)
SIDE_PAIRING_INDICES = (0, 1, 2, 3)

GROUP_SOURCE = (
    "Ebbens-Iordanov-Teillaud-Vegter_JoCG_2022_"
    "doi:10.20382/jocg.v13i1a5_equations_5-6_Theorem_2"
)
TRACE_SOURCE = (
    "Kordyukov-Taimanov_arXiv:2202.06055v3_"
    "Theorem_3_equations_19_and_22-23"
)

FIELDS = (
    "row_id",
    "ledger_schema",
    "metric_control_id",
    "group_source_lock",
    "trace_source_lock",
    "field_b",
    "base_bundle",
    "tensor_regime",
    "primitive_axis_owner_id",
    "inverse_pair_definition",
    "owner_counting_convention",
    "side_pairing_index",
    "canonical_primitive_word",
    "branch_primitive_word",
    "source_k",
    "absolute_repetition_index",
    "branch_group_element_word",
    "source_k_class",
    "primitive_root_status",
    "primitive_root_proof",
    "canonical_primitive_homology_vector",
    "signed_branch_homology_vector",
    "signed_k_partner_row_id",
    "field_sign_partner_row_id",
    "field_sign_partner_rule",
    "generator_trace_exact",
    "generator_trace_decimal",
    "primitive_geodesic_length_exact",
    "primitive_geodesic_length_decimal",
    "norm_exact",
    "norm_decimal",
    "primitive_period_trace_clock_exact",
    "primitive_period_trace_clock_decimal",
    "absolute_total_trace_clock_period_exact",
    "absolute_total_trace_clock_period_decimal",
    "signed_trace_time_exact",
    "signed_trace_time_decimal",
    "fourier_factor_exact",
    "primitive_period_physical_clock_exact",
    "primitive_period_physical_clock_decimal",
    "absolute_total_physical_period_exact",
    "absolute_total_physical_period_decimal",
    "project_action_per_N_exact",
    "project_action_per_N_decimal",
    "phase_exponent_exact",
    "maslov_index",
    "poincare_multiplier_N_to_k_exact",
    "poincare_multiplier_N_to_k_decimal",
    "poincare_multiplier_N_to_minus_k_exact",
    "poincare_multiplier_N_to_minus_k_decimal",
    "stability_determinant_sqrt_abs_exact",
    "stability_determinant_sqrt_abs_decimal",
    "signed_trace_stability_denominator_exact",
    "signed_trace_stability_denominator_decimal",
    "connection_holonomy_status",
    "trace_owner_status",
    "enumeration_completeness",
    "arithmetic_label",
    "target_data_used",
    "zero_field_status",
    "odd_N_status",
    "full_all_N_status",
    "fixed_operator_status",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)


ComplexDecimal = tuple[Decimal, Decimal]
Matrix2 = tuple[
    tuple[ComplexDecimal, ComplexDecimal],
    tuple[ComplexDecimal, ComplexDecimal],
]


def decimal_string(value: Decimal, digits: int = DISPLAY_DIGITS) -> str:
    """Return a deterministic significant-digit decimal string."""

    return format(value, f".{digits}g")


def c_add(left: ComplexDecimal, right: ComplexDecimal) -> ComplexDecimal:
    return left[0] + right[0], left[1] + right[1]


def c_mul(left: ComplexDecimal, right: ComplexDecimal) -> ComplexDecimal:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def c_neg(value: ComplexDecimal) -> ComplexDecimal:
    return -value[0], -value[1]


def c_abs(value: ComplexDecimal) -> Decimal:
    return (value[0] * value[0] + value[1] * value[1]).sqrt()


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            c_add(c_mul(left[i][0], right[0][j]), c_mul(left[i][1], right[1][j]))
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_inverse_det_one(matrix: Matrix2) -> Matrix2:
    return (
        (matrix[1][1], c_neg(matrix[0][1])),
        (c_neg(matrix[1][0]), matrix[0][0]),
    )


def identity_matrix() -> Matrix2:
    zero = (Decimal(0), Decimal(0))
    one = (Decimal(1), Decimal(0))
    return ((one, zero), (zero, one))


def bolza_constants() -> dict[str, Decimal]:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        sqrt2 = Decimal(2).sqrt()
        a = Decimal(1) + sqrt2
        rho = (a * a - Decimal(1)).sqrt()
        eigenvalue_plus = a + rho
        norm = eigenvalue_plus * eigenvalue_plus
        log_norm = norm.ln()
        sqrt3 = Decimal(3).sqrt()
        sqrt5_over_3 = (Decimal(5) / Decimal(3)).sqrt()
        return {
            "sqrt2": +sqrt2,
            "a": +a,
            "rho": +rho,
            "eigenvalue_plus": +eigenvalue_plus,
            "norm": +norm,
            "log_norm": +log_norm,
            "sqrt3": +sqrt3,
            "sqrt5_over_3": +sqrt5_over_3,
        }


def source_generator_matrices() -> list[Matrix2]:
    """Return the four JoCG equation-(5) matrices at genus two."""

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        constants = bolza_constants()
        a = constants["a"]
        rho = constants["rho"]
        inv_sqrt2 = Decimal(1) / constants["sqrt2"]
        unit_roots: tuple[ComplexDecimal, ...] = (
            (Decimal(1), Decimal(0)),
            (inv_sqrt2, inv_sqrt2),
            (Decimal(0), Decimal(1)),
            (-inv_sqrt2, inv_sqrt2),
        )
        matrices: list[Matrix2] = []
        for real, imag in unit_roots:
            upper = (rho * real, rho * imag)
            lower = (upper[0], -upper[1])
            diagonal = (a, Decimal(0))
            matrices.append(((diagonal, upper), (lower, diagonal)))
        return matrices


def determinant(matrix: Matrix2) -> ComplexDecimal:
    return c_add(c_mul(matrix[0][0], matrix[1][1]), c_neg(c_mul(matrix[0][1], matrix[1][0])))


def max_identity_residual(matrix: Matrix2) -> Decimal:
    residuals: list[Decimal] = []
    for i in range(2):
        for j in range(2):
            target = Decimal(1) if i == j else Decimal(0)
            residuals.append(c_abs((matrix[i][j][0] - target, matrix[i][j][1])))
    return max(residuals)


def group_certificate() -> dict[str, object]:
    """Validate the source-transcribed matrices without claiming a new proof."""

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        matrices = source_generator_matrices()
        determinant_residuals = [c_abs(c_add(determinant(matrix), (Decimal(-1), Decimal(0)))) for matrix in matrices]
        trace_values = [matrix[0][0][0] + matrix[1][1][0] for matrix in matrices]

        # Source equation (6), specialized to g=2:
        # f0 f1^-1 f2 f3^-1 f0^-1 f1 f2^-1 f3 = identity.
        relator = (
            (0, 1),
            (1, -1),
            (2, 1),
            (3, -1),
            (0, -1),
            (1, 1),
            (2, -1),
            (3, 1),
        )
        product = identity_matrix()
        for index, exponent in relator:
            factor = matrices[index]
            if exponent == -1:
                factor = matrix_inverse_det_one(factor)
            product = matrix_multiply(product, factor)
        relator_residual = max_identity_residual(product)

        constants = bolza_constants()
        expected_trace = Decimal(2) * constants["a"]
        trace_residuals = [abs(trace - expected_trace) for trace in trace_values]
        systole_from_norm_residual = abs(constants["norm"].ln() - constants["log_norm"])
        systole_from_eigenvalue_residual = abs(
            Decimal(2) * constants["eigenvalue_plus"].ln() - constants["log_norm"]
        )
        tolerance = Decimal("1e-100")
        errors: list[str] = []
        if max(determinant_residuals) >= tolerance:
            errors.append("generator determinant residual exceeds tolerance")
        if max(trace_residuals) >= tolerance:
            errors.append("generator trace residual exceeds tolerance")
        if relator_residual >= tolerance:
            errors.append("polygon relator residual exceeds tolerance")
        if systole_from_norm_residual >= tolerance:
            errors.append("log norm/systole identity failed")
        if systole_from_eigenvalue_residual >= tolerance:
            errors.append("eigenvalue/systole identity failed")

        return {
            "schema": "p28_round4_bolza_group_certificate/1.1",
            "status": "PASS" if not errors else "FAIL",
            "primary_source": {
                "citation": GROUP_SOURCE,
                "article_url": "https://doi.org/10.20382/jocg.v13i1a5",
                "arxiv_url": "https://arxiv.org/abs/2103.05960",
                "checked_date": "2026-08-27",
                "source_claims": [
                    "equation_5_opposite_side_pairing_matrices",
                    "equation_6_polygon_relator",
                    "poincare_theorem_fuchsian_group_and_fundamental_domain",
                    "theorem_2_bolza_systole",
                ],
            },
            "genus": 2,
            "generator_count": 4,
            "matrix_model": (
                "A_j=[[cot(pi/8),exp(i*j*pi/4)*sqrt(cot(pi/8)^2-1)],"
                "[exp(-i*j*pi/4)*sqrt(cot(pi/8)^2-1),cot(pi/8)]],j=0..3"
            ),
            "polygon_relator": "f0*f1^-1*f2*f3^-1*f0^-1*f1*f2^-1*f3=identity",
            "decimal_precision": DECIMAL_PRECISION,
            "numeric_tolerance": decimal_string(tolerance),
            "maximum_determinant_residual": decimal_string(max(determinant_residuals)),
            "maximum_trace_residual": decimal_string(max(trace_residuals)),
            "polygon_relator_residual": decimal_string(relator_residual),
            "generator_trace_exact": "2*(1+sqrt(2))",
            "generator_trace_decimal": decimal_string(expected_trace),
            "primitive_geodesic_length_exact": "ell_B=2*acosh(1+sqrt(2))",
            "primitive_geodesic_length_decimal": decimal_string(constants["log_norm"]),
            "norm_exact": "N_B=(1+sqrt(2)+sqrt(2+2*sqrt(2)))^2=exp(ell_B)",
            "norm_decimal": decimal_string(constants["norm"]),
            "systole_identity_residual": decimal_string(
                max(systole_from_norm_residual, systole_from_eigenvalue_residual)
            ),
            "primitive_owner_certificate": (
                "PROVED_FROM_SOURCE_SYSTOLE: each f_j has translation length ell_B=sys(Bolza); "
                "if f_j=u^r with r>=2 then ell(u)=ell_B/r<sys(Bolza), impossible"
            ),
            "inverse_nonconjugacy_certificate": (
                "PROVED_FROM_POLYGON_PRESENTATION_ABELIANIZATION: the single relator has "
                "zero exponent sum in every f_j, so f_j^+/- have distinct +/- standard-basis "
                "homology vectors and cannot be conjugate"
            ),
            "inverse_pair_counting_boundary": (
                "f_j and f_j^-1 are not conjugate in Gamma, but this trace ledger assigns "
                "one inverse-paired primitive axis owner and represents the two equation-(19) "
                "branches only by signed k; no oriented-owner credit is minted"
            ),
            "certificate_boundary": (
                "SOURCE_BACKED_EXPLICIT_BOLZA_REPRESENTATION; NUMERIC_REPLAY_CHECKS_TRANSCRIPTION; "
                "POINCARE_THEOREM_AND_PRIMITIVITY_ARGUMENT_ARE_HUMAN_MATHEMATICS; "
                "NOT_A_COMPLETE_PRIMITIVE_CONJUGACY_ENUMERATION"
            ),
            "errors": errors,
        }


def row_id(field_b: str, side_index: int, source_k: int) -> str:
    field_code = "P" if field_b == "+1/2" else "M"
    k_code = f"KP{source_k}" if source_k > 0 else f"KN{abs(source_k)}"
    return f"B28R4-{field_code}-A{side_index}-{k_code}"


def homology_vector(side_index: int, coefficient: int) -> str:
    values = [0, 0, 0, 0]
    values[side_index] = coefficient
    return "(" + ",".join(str(value) for value in values) + ")"


def signed_symbol(sign: int, positive_expression: str) -> str:
    return positive_expression if sign == 1 else f"-({positive_expression})"


def build_rows(repetitions: Sequence[int] = REPETITIONS) -> list[dict[str, object]]:
    if not repetitions or any(value < 1 for value in repetitions):
        raise ValueError("repetitions must be positive integers")
    if len(repetitions) != len(set(repetitions)):
        raise ValueError("repetitions must be unique")

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        constants = bolza_constants()
        ell = constants["log_norm"]
        norm = constants["norm"]
        trace = Decimal(2) * constants["a"]
        primitive_trace_period = constants["sqrt5_over_3"] * ell
        primitive_physical_period = (Decimal(2) / constants["sqrt3"]) * ell
        action_unit = (constants["sqrt3"] / Decimal(2)) * ell

        signed_source_values = tuple(repetitions) + tuple(
            -value for value in repetitions
        )
        rows: list[dict[str, object]] = []
        for field_b, base_bundle in (("+1/2", "L"), ("-1/2", "L_dual")):
            partner_field = "-1/2" if field_b == "+1/2" else "+1/2"
            for side_index in SIDE_PAIRING_INDICES:
                canonical_word = f"f{side_index}"
                owner_id = f"BOLZA_AXIS_INVERSE_PAIR_{side_index}"
                inverse_pair = f"{{f{side_index},f{side_index}^-1}}"
                for source_k in signed_source_values:
                    absolute_repetition = abs(source_k)
                    branch_sign = 1 if source_k > 0 else -1
                    branch_primitive_word = (
                        canonical_word if source_k > 0 else f"f{side_index}^-1"
                    )
                    branch_group_element_word = f"f{side_index}^{source_k}"
                    absolute_trace_period = (
                        Decimal(absolute_repetition) * primitive_trace_period
                    )
                    signed_trace_time = Decimal(source_k) * primitive_trace_period
                    absolute_physical_period = (
                        Decimal(absolute_repetition) * primitive_physical_period
                    )
                    action_per_n = Decimal(source_k) * action_unit
                    if source_k > 0:
                        multiplier_k = norm**source_k
                        multiplier_minus_k = Decimal(1) / multiplier_k
                    else:
                        multiplier_minus_k = norm ** abs(source_k)
                        multiplier_k = Decimal(1) / multiplier_minus_k
                    signed_stability_denominator = (
                        multiplier_k.sqrt() - multiplier_minus_k.sqrt()
                    )
                    stability_determinant_sqrt_abs = abs(
                        signed_stability_denominator
                    )
                    action_expression = signed_symbol(
                        branch_sign,
                        f"{absolute_repetition}*sqrt(3)/2*ell_B",
                    )
                    signed_time_expression = signed_symbol(
                        branch_sign,
                        f"{absolute_repetition}*sqrt(5/3)*ell_B",
                    )
                    signed_stability_expression = signed_symbol(
                        branch_sign,
                        (
                            f"N_B^({absolute_repetition}/2)"
                            f"-N_B^(-{absolute_repetition}/2)"
                        ),
                    )
                    rows.append(
                        {
                            "row_id": row_id(field_b, side_index, source_k),
                            "ledger_schema": (
                                "p28_round4_bolza_axis_signed_k_ledger/2.0"
                            ),
                            "metric_control_id": "BOLZA_ARITHMETIC_CURVATURE_MINUS_1",
                            "group_source_lock": GROUP_SOURCE,
                            "trace_source_lock": TRACE_SOURCE,
                            "field_b": field_b,
                            "base_bundle": base_bundle,
                            "tensor_regime": "SOURCE_COMPATIBLE_EVEN_N_EQUALS_2m",
                            "primitive_axis_owner_id": owner_id,
                            "inverse_pair_definition": inverse_pair,
                            "owner_counting_convention": (
                                "INVERSE_PAIRED_AXIS_OWNER;EQ19_SIGNED_K_BRANCHES;"
                                "NO_ORIENTED_OWNER_CREDIT"
                            ),
                            "side_pairing_index": side_index,
                            "canonical_primitive_word": canonical_word,
                            "branch_primitive_word": branch_primitive_word,
                            "source_k": source_k,
                            "absolute_repetition_index": absolute_repetition,
                            "branch_group_element_word": branch_group_element_word,
                            "source_k_class": (
                                "SIGNED_K_PRIMITIVE_BRANCH"
                                if absolute_repetition == 1
                                else "SIGNED_K_REPETITION_BRANCH"
                            ),
                            "primitive_root_status": "PROVED_SYSTOLIC_SIDE_PAIRING",
                            "primitive_root_proof": (
                                "CANONICAL_f_j_LENGTH_EQUALS_BOLZA_SYSTOLE;"
                                "OWNER_IS_INVERSE_PAIR"
                            ),
                            "canonical_primitive_homology_vector": homology_vector(
                                side_index, 1
                            ),
                            "signed_branch_homology_vector": homology_vector(
                                side_index, source_k
                            ),
                            "signed_k_partner_row_id": row_id(
                                field_b, side_index, -source_k
                            ),
                            "field_sign_partner_row_id": row_id(
                                partner_field, side_index, -source_k
                            ),
                            "field_sign_partner_rule": (
                                "(field_b,primitive_axis_owner_id,k)->"
                                "(-field_b,same_primitive_axis_owner_id,-k)"
                            ),
                            "generator_trace_exact": "2*(1+sqrt(2))",
                            "generator_trace_decimal": decimal_string(trace),
                            "primitive_geodesic_length_exact": (
                                "ell_B=2*acosh(1+sqrt(2))"
                            ),
                            "primitive_geodesic_length_decimal": decimal_string(ell),
                            "norm_exact": "N_B=exp(ell_B)",
                            "norm_decimal": decimal_string(norm),
                            "primitive_period_trace_clock_exact": "sqrt(5/3)*ell_B",
                            "primitive_period_trace_clock_decimal": decimal_string(
                                primitive_trace_period
                            ),
                            "absolute_total_trace_clock_period_exact": (
                                f"{absolute_repetition}*sqrt(5/3)*ell_B"
                            ),
                            "absolute_total_trace_clock_period_decimal": decimal_string(
                                absolute_trace_period
                            ),
                            "signed_trace_time_exact": signed_time_expression,
                            "signed_trace_time_decimal": decimal_string(
                                signed_trace_time
                            ),
                            "fourier_factor_exact": (
                                f"hat_phi({signed_time_expression})"
                            ),
                            "primitive_period_physical_clock_exact": (
                                "2/sqrt(3)*ell_B"
                            ),
                            "primitive_period_physical_clock_decimal": decimal_string(
                                primitive_physical_period
                            ),
                            "absolute_total_physical_period_exact": (
                                f"{absolute_repetition}*2/sqrt(3)*ell_B"
                            ),
                            "absolute_total_physical_period_decimal": decimal_string(
                                absolute_physical_period
                            ),
                            "project_action_per_N_exact": action_expression,
                            "project_action_per_N_decimal": decimal_string(action_per_n),
                            "phase_exponent_exact": f"exp(-i*N*({action_expression}))",
                            "maslov_index": 0,
                            "poincare_multiplier_N_to_k_exact": f"N_B^({source_k})",
                            "poincare_multiplier_N_to_k_decimal": decimal_string(
                                multiplier_k
                            ),
                            "poincare_multiplier_N_to_minus_k_exact": (
                                f"N_B^({-source_k})"
                            ),
                            "poincare_multiplier_N_to_minus_k_decimal": decimal_string(
                                multiplier_minus_k
                            ),
                            "stability_determinant_sqrt_abs_exact": (
                                f"N_B^({absolute_repetition}/2)"
                                f"-N_B^(-{absolute_repetition}/2)"
                            ),
                            "stability_determinant_sqrt_abs_decimal": decimal_string(
                                stability_determinant_sqrt_abs
                            ),
                            "signed_trace_stability_denominator_exact": (
                                signed_stability_expression
                            ),
                            "signed_trace_stability_denominator_decimal": decimal_string(
                                signed_stability_denominator
                            ),
                            "connection_holonomy_status": (
                                "NOT_SEPARATELY_LIFTED; EVEN_N_TOTAL_ACTION_SOURCE_BOUND"
                            ),
                            "trace_owner_status": (
                                "PROVED_SOURCE_COMPATIBLE_INVERSE_PAIRED_AXIS_"
                                "SIGNED_K_EVEN_SUBTYPE"
                            ),
                            "enumeration_completeness": (
                                "FOUR_INVERSE_PAIRED_SIDE_PAIRING_AXIS_OWNERS_ONLY; "
                                "NOT_COMPLETE_BOLZA_PRIMITIVE_SPECTRUM"
                            ),
                            "arithmetic_label": "NONE",
                            "target_data_used": "false",
                            "zero_field_status": "OPEN_NOT_IN_LEDGER",
                            "odd_N_status": "OPEN_NOT_ESTABLISHED",
                            "full_all_N_status": "OPEN_NOT_ESTABLISHED",
                            "fixed_operator_status": (
                                "OPEN_NOT_ESTABLISHED_NO_CREDIT_TRANSFER"
                            ),
                            "formal_route_a_tuple": "UNASSIGNED",
                            "route_b_invocation_allowed": "false",
                        }
                    )
        return rows


def rows_by_id(rows: Iterable[dict[str, object]]) -> dict[str, dict[str, object]]:
    return {str(row["row_id"]): row for row in rows}


def validate_rows(
    rows: Sequence[dict[str, object]], certificate: dict[str, object]
) -> dict[str, object]:
    errors: list[str] = []
    expected_count = 2 * len(SIDE_PAIRING_INDICES) * 2 * len(REPETITIONS)
    if len(rows) != expected_count:
        errors.append(f"expected {expected_count} rows, found {len(rows)}")
    indexed = rows_by_id(rows)
    if len(indexed) != len(rows):
        errors.append("row identifiers are not unique")
    if certificate.get("status") != "PASS":
        errors.append("group certificate did not pass")

    field_partner_checks = 0
    signed_k_partner_checks = 0
    signed_k_law_checks = 0
    stability_checks = 0
    expected_signed_k = set(REPETITIONS) | {-value for value in REPETITIONS}
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        tolerance = Decimal("1e-65")
        constants = bolza_constants()
        norm = constants["norm"]
        primitive_trace_period = constants["sqrt5_over_3"] * constants["log_norm"]
        primitive_physical_period = (
            Decimal(2) / constants["sqrt3"]
        ) * constants["log_norm"]
        action_unit = (
            constants["sqrt3"] / Decimal(2)
        ) * constants["log_norm"]

        for row in rows:
            row_identifier = str(row["row_id"])
            source_k = int(row["source_k"])
            absolute_repetition = int(row["absolute_repetition_index"])
            signed_k_partner_id = str(row["signed_k_partner_row_id"])
            field_partner_id = str(row["field_sign_partner_row_id"])

            if set(row) != set(FIELDS):
                errors.append(f"schema fields changed for {row_identifier}")
            if source_k not in expected_signed_k:
                errors.append(f"source k outside declared grid for {row_identifier}")
            if absolute_repetition != abs(source_k):
                errors.append(f"absolute repetition does not equal |k| for {row_identifier}")
            if row["primitive_axis_owner_id"] != (
                f"BOLZA_AXIS_INVERSE_PAIR_{row['side_pairing_index']}"
            ):
                errors.append(f"axis owner id changed for {row_identifier}")
            if row["canonical_primitive_word"] != f"f{row['side_pairing_index']}":
                errors.append(f"canonical primitive word changed for {row_identifier}")

            if signed_k_partner_id not in indexed:
                errors.append(f"missing signed-k partner for {row_identifier}")
            else:
                partner = indexed[signed_k_partner_id]
                if partner["signed_k_partner_row_id"] != row_identifier:
                    errors.append(f"signed-k partner is not involutive for {row_identifier}")
                if int(partner["source_k"]) != -source_k:
                    errors.append(f"signed-k partner did not reverse k for {row_identifier}")
                if partner["field_b"] != row["field_b"]:
                    errors.append(f"signed-k partner changed field for {row_identifier}")
                if partner["primitive_axis_owner_id"] != row["primitive_axis_owner_id"]:
                    errors.append(f"signed-k partner changed axis owner for {row_identifier}")
                if abs(
                    Decimal(str(partner["project_action_per_N_decimal"]))
                    + Decimal(str(row["project_action_per_N_decimal"]))
                ) >= tolerance:
                    errors.append(f"signed-k partner action did not reverse for {row_identifier}")
                if abs(
                    Decimal(str(partner["signed_trace_time_decimal"]))
                    + Decimal(str(row["signed_trace_time_decimal"]))
                ) >= tolerance:
                    errors.append(f"signed-k partner trace time did not reverse for {row_identifier}")
                if abs(
                    Decimal(
                        str(partner["signed_trace_stability_denominator_decimal"])
                    )
                    + Decimal(str(row["signed_trace_stability_denominator_decimal"]))
                ) >= tolerance:
                    errors.append(
                        f"signed-k partner trace denominator did not reverse for {row_identifier}"
                    )
                signed_k_partner_checks += 1

            if field_partner_id not in indexed:
                errors.append(f"missing field-sign partner for {row_identifier}")
            else:
                partner = indexed[field_partner_id]
                if partner["field_sign_partner_row_id"] != row_identifier:
                    errors.append(f"field-sign partner is not involutive for {row_identifier}")
                if partner["field_b"] == row["field_b"]:
                    errors.append(f"field-sign partner did not change field for {row_identifier}")
                if int(partner["source_k"]) != -source_k:
                    errors.append(f"field-sign partner did not reverse k for {row_identifier}")
                if partner["primitive_axis_owner_id"] != row["primitive_axis_owner_id"]:
                    errors.append(f"field-sign partner changed axis owner for {row_identifier}")
                if abs(
                    Decimal(str(partner["project_action_per_N_decimal"]))
                    + Decimal(str(row["project_action_per_N_decimal"]))
                ) >= tolerance:
                    errors.append(f"field-sign partner action did not change sign for {row_identifier}")
                field_partner_checks += 1

            expected_trace_period = Decimal(absolute_repetition) * primitive_trace_period
            expected_signed_trace_time = Decimal(source_k) * primitive_trace_period
            expected_physical_period = (
                Decimal(absolute_repetition) * primitive_physical_period
            )
            expected_action = Decimal(source_k) * action_unit
            if abs(
                Decimal(str(row["absolute_total_trace_clock_period_decimal"]))
                - expected_trace_period
            ) >= tolerance:
                errors.append(f"trace-period repetition law failed for {row_identifier}")
            if abs(
                Decimal(str(row["signed_trace_time_decimal"]))
                - expected_signed_trace_time
            ) >= tolerance:
                errors.append(f"signed trace-time law failed for {row_identifier}")
            if abs(
                Decimal(str(row["absolute_total_physical_period_decimal"]))
                - expected_physical_period
            ) >= tolerance:
                errors.append(f"physical-period repetition law failed for {row_identifier}")
            if abs(
                Decimal(str(row["project_action_per_N_decimal"])) - expected_action
            ) >= tolerance:
                errors.append(f"signed-k action law failed for {row_identifier}")
            signed_k_law_checks += 1

            multiplier_k = Decimal(str(row["poincare_multiplier_N_to_k_decimal"]))
            multiplier_minus_k = Decimal(
                str(row["poincare_multiplier_N_to_minus_k_decimal"])
            )
            signed_denominator = Decimal(
                str(row["signed_trace_stability_denominator_decimal"])
            )
            absolute_denominator = Decimal(
                str(row["stability_determinant_sqrt_abs_decimal"])
            )
            if source_k > 0:
                expected_multiplier_k = norm**source_k
                expected_multiplier_minus_k = Decimal(1) / expected_multiplier_k
            else:
                expected_multiplier_minus_k = norm ** abs(source_k)
                expected_multiplier_k = Decimal(1) / expected_multiplier_minus_k
            expected_signed_denominator = (
                expected_multiplier_k.sqrt() - expected_multiplier_minus_k.sqrt()
            )
            if abs(multiplier_k - expected_multiplier_k) >= tolerance:
                errors.append(f"N^k multiplier failed for {row_identifier}")
            if abs(multiplier_minus_k - expected_multiplier_minus_k) >= tolerance:
                errors.append(f"N^-k multiplier failed for {row_identifier}")
            if abs(multiplier_k * multiplier_minus_k - Decimal(1)) >= tolerance:
                errors.append(f"Poincare reciprocal law failed for {row_identifier}")
            if abs(signed_denominator - expected_signed_denominator) >= tolerance:
                errors.append(f"signed trace denominator failed for {row_identifier}")
            if abs(absolute_denominator - abs(expected_signed_denominator)) >= tolerance:
                errors.append(f"absolute stability root failed for {row_identifier}")
            stability_checks += 1

            if row["maslov_index"] != 0:
                errors.append(f"Maslov index changed for {row_identifier}")
            if row["formal_route_a_tuple"] != "UNASSIGNED":
                errors.append(f"premature Route-A tuple in {row_identifier}")
            if row["route_b_invocation_allowed"] != "false":
                errors.append(f"premature Route-B invocation in {row_identifier}")
            if row["target_data_used"] != "false" or row["arithmetic_label"] != "NONE":
                errors.append(f"target-data or arithmetic-label leak in {row_identifier}")

    primitive_branch_rows = [
        row
        for row in rows
        if row["source_k_class"] == "SIGNED_K_PRIMITIVE_BRANCH"
    ]
    repetition_branch_rows = [
        row
        for row in rows
        if row["source_k_class"] == "SIGNED_K_REPETITION_BRANCH"
    ]
    field_owner_pairs: set[tuple[object, object]] = set()
    for field_b in ("+1/2", "-1/2"):
        field_rows = [row for row in rows if row["field_b"] == field_b]
        owner_ids = {row["primitive_axis_owner_id"] for row in field_rows}
        if len(owner_ids) != 4:
            errors.append(f"expected four inverse-paired axis owners for {field_b}")
        if len(field_rows) != 24:
            errors.append(f"expected 24 signed trace branches for {field_b}")
        primitive_field_rows = [
            row for row in field_rows if abs(int(row["source_k"])) == 1
        ]
        if len(primitive_field_rows) != 8:
            errors.append(f"expected eight |k|=1 trace branches for {field_b}")
        for owner_id in owner_ids:
            owner_k_grid = {
                int(row["source_k"])
                for row in field_rows
                if row["primitive_axis_owner_id"] == owner_id
            }
            if owner_k_grid != expected_signed_k:
                errors.append(f"incomplete signed-k grid for {field_b}/{owner_id}")
            field_owner_pairs.add((field_b, owner_id))

    oriented_owner_credit_rows = sum(
        any(
            key.startswith("oriented_") and key.endswith("_owner_id")
            for key in row
        )
        for row in rows
    )
    if oriented_owner_credit_rows:
        errors.append("oriented-owner credit field reappeared")
    owner_conventions = {row["owner_counting_convention"] for row in rows}
    if owner_conventions != {
        "INVERSE_PAIRED_AXIS_OWNER;EQ19_SIGNED_K_BRANCHES;NO_ORIENTED_OWNER_CREDIT"
    }:
        errors.append("inverse-paired owner counting convention changed")

    serialized = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "schema": "p28_round4_bolza_owner_validation/2.0",
        "status": "PASS" if not errors else "FAIL",
        "row_count": len(rows),
        "field_values": ["+1/2", "-1/2"],
        "explicit_inverse_paired_axis_owners_per_field": len(
            SIDE_PAIRING_INDICES
        ),
        "field_axis_owner_pairs": len(field_owner_pairs),
        "signed_trace_branches_per_field": len(rows) // 2,
        "signed_k_primitive_branches_per_field": len(primitive_branch_rows) // 2,
        "signed_k_primitive_branch_rows": len(primitive_branch_rows),
        "signed_k_repetition_branch_rows": len(repetition_branch_rows),
        "oriented_owner_credit_rows": oriented_owner_credit_rows,
        "source_k_values": sorted(expected_signed_k),
        "maximum_absolute_repetition": max(REPETITIONS),
        "field_partner_checks": field_partner_checks,
        "signed_k_partner_checks": signed_k_partner_checks,
        "signed_k_law_checks": signed_k_law_checks,
        "stability_checks": stability_checks,
        "maslov_zero_rows": sum(row["maslov_index"] == 0 for row in rows),
        "target_data_rows": sum(row["target_data_used"] != "false" for row in rows),
        "arithmetic_label_rows": sum(row["arithmetic_label"] != "NONE" for row in rows),
        "formal_route_a_tuple_assigned_rows": sum(
            row["formal_route_a_tuple"] != "UNASSIGNED" for row in rows
        ),
        "route_b_allowed_rows": sum(
            row["route_b_invocation_allowed"] != "false" for row in rows
        ),
        "row_payload_sha256": hashlib.sha256(serialized).hexdigest(),
        "group_certificate_status": certificate.get("status"),
        "group_certificate_relator_residual": certificate.get(
            "polygon_relator_residual"
        ),
        "trace_source_lock": TRACE_SOURCE,
        "owner_counting_convention": (
            "FOUR_INVERSE_PAIRED_AXIS_OWNERS_PER_FIELD_WITH_EQ19_SIGNED_K_BRANCHES"
        ),
        "claim_boundary": (
            "PROVED_FOUR_INVERSE_PAIRED_AXIS_OWNERS_PER_FIELD_WITH_SIGNED_K_"
            "TRACE_BRANCHES_UNDER_FROZEN_EVEN_SUBTYPE;NO_ORIENTED_OWNER_CREDIT;"
            "NOT_COMPLETE_BOLZA_SPECTRUM;NO_ARITHMETIC_PRIME_LABEL;"
            "ZERO_ODD_FULL_FIXED_REGIMES_OPEN"
        ),
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "errors": errors,
    }


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger-output", required=True, type=Path)
    parser.add_argument("--certificate-output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    args = parser.parse_args()

    certificate = group_certificate()
    rows = build_rows()
    validation = validate_rows(rows, certificate)
    write_csv(args.ledger_output, rows)
    write_json(args.certificate_output, certificate)
    write_json(args.validation_output, validation)
    print(json.dumps(validation, sort_keys=True))
    return 0 if certificate["status"] == "PASS" and validation["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
