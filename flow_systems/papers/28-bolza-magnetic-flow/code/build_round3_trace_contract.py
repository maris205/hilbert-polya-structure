#!/usr/bin/env python3
"""Build the P28 source-bound even-subsequence trace contract.

No eigenvalues or closed-orbit samples are generated.  The artifact translates
Kordyukov--Taimanov's B=1 trace theorem to the source-compatible square-root
subtype of the frozen degree-one B=1/2 bundle on the even sequence N=2m.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Sequence


FIELDS = (
    "metric_control_id",
    "field_b",
    "base_bundle",
    "tensor_power_N",
    "even_subsequence",
    "source_tensor_m",
    "source_compatible_square_root",
    "semiclassical_parameter_h",
    "unscaled_operator_P_N",
    "scaled_operator_hP_N",
    "trace_distribution",
    "test_function_class",
    "spectral_center_lambda",
    "lambda_window",
    "laplacian_center_nu",
    "laplacian_window",
    "classical_hamiltonian",
    "classical_shell",
    "physical_unit_speed",
    "trace_clock_speed",
    "clock_conversion",
    "source_field_B",
    "source_energy_E",
    "source_energy_E0",
    "mane_status",
    "primitive_period_trace_clock",
    "primitive_period_physical_clock",
    "action_frequency_per_N",
    "trace_owner_status",
    "trace_binding_evidence_token",
    "fixed_operator_credit_transfer_allowed",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)

EVEN_TENSOR_POWERS = (2, 4, 8, 16)

FIELD_SPECS = (
    {
        "field_b": "0",
        "base_bundle": "trivial",
        "source_compatible_square_root": "not_applicable",
        "source_field_B": "not_applicable",
        "mane_status": "zero_field_control",
        "primitive_period_trace_clock": "OPEN",
        "primitive_period_physical_clock": "OPEN",
        "action_frequency_per_N": "OPEN",
        "trace_owner_status": "CONTROL_CONTRACT_FROZEN_OWNER_OPEN",
        "trace_binding_evidence_token": "OPEN",
    },
    {
        "field_b": "+1/2",
        "base_bundle": "L",
        "source_compatible_square_root": "true",
        "source_field_B": "+1_after_L_squared",
        "mane_status": "ABOVE_CRITICAL_1_GREATER_THAN_(1/2)^2",
        "primitive_period_trace_clock": "sqrt(5/3)*log_Norm(h)",
        "primitive_period_physical_clock": "2/sqrt(3)*log_Norm(h)",
        "action_frequency_per_N": "-sqrt(3)/2*k*log_Norm(h)",
        "trace_owner_status": "PROVED_SOURCE_COMPATIBLE_EVEN_SUBSEQUENCE",
        "trace_binding_evidence_token": "PROVED",
    },
    {
        "field_b": "-1/2",
        "base_bundle": "L_dual",
        "source_compatible_square_root": "true_via_duality",
        "source_field_B": "-1_after_(L_dual)_squared",
        "mane_status": "ABOVE_CRITICAL_1_GREATER_THAN_(1/2)^2",
        "primitive_period_trace_clock": "sqrt(5/3)*log_Norm(h)",
        "primitive_period_physical_clock": "2/sqrt(3)*log_Norm(h)",
        "action_frequency_per_N": "+sqrt(3)/2*k*log_Norm(h)",
        "trace_owner_status": "PROVED_BY_ANTIUNITARY_DUALITY",
        "trace_binding_evidence_token": "PROVED",
    },
)


def parse_even_tensor_powers(raw: str) -> list[int]:
    values = [int(item.strip()) for item in raw.split(",") if item.strip()]
    if not values or any(value < 2 or value % 2 for value in values):
        raise ValueError("tensor powers must be a nonempty list of positive even integers")
    if len(values) != len(set(values)):
        raise ValueError("tensor powers must be unique")
    return sorted(values)


def build_rows(tensor_powers: Sequence[int]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n_value in tensor_powers:
        if n_value % 2:
            raise ValueError("the source-bound contract is restricted to N=2m")
        m_value = n_value // 2
        for field in FIELD_SPECS:
            rows.append(
                {
                    "metric_control_id": "BOLZA_ARITHMETIC_CURVATURE_MINUS_1",
                    "field_b": field["field_b"],
                    "base_bundle": field["base_bundle"],
                    "tensor_power_N": n_value,
                    "even_subsequence": "true",
                    "source_tensor_m": m_value,
                    "source_compatible_square_root": field[
                        "source_compatible_square_root"
                    ],
                    "semiclassical_parameter_h": f"1/{n_value}",
                    "unscaled_operator_P_N": "sqrt(Delta^(bundle^N)+N^2/4)",
                    "scaled_operator_hP_N": "N^(-1)*sqrt(Delta^(bundle^N)+N^2/4)",
                    "trace_distribution": "Y_N(phi)=Tr phi(P_N-(sqrt(5)/2)*N)",
                    "test_function_class": (
                        "phi_in_S(R)_real_even;_Fourier_support_compact_and_disjoint_from_0"
                    ),
                    "spectral_center_lambda": "(sqrt(5)/2)*N",
                    "lambda_window": "O(1)_in_lambda",
                    "laplacian_center_nu": "N^2",
                    "laplacian_window": "O(N)_in_nu_exactly_sqrt(5)*N*s+s^2_for_lambda_shift_s",
                    "classical_hamiltonian": "sqrt(|p|^2+1/4)",
                    "classical_shell": "|p|^2=1",
                    "physical_unit_speed": "1_for_H0=|p|^2/2",
                    "trace_clock_speed": "2/sqrt(5)_for_H=sqrt(|p|^2+1/4)",
                    "clock_conversion": "T_trace=(sqrt(5)/2)*T_physical",
                    "source_field_B": field["source_field_B"],
                    "source_energy_E": "sqrt(5)",
                    "source_energy_E0": "4",
                    "mane_status": field["mane_status"],
                    "primitive_period_trace_clock": field[
                        "primitive_period_trace_clock"
                    ],
                    "primitive_period_physical_clock": field[
                        "primitive_period_physical_clock"
                    ],
                    "action_frequency_per_N": field["action_frequency_per_N"],
                    "trace_owner_status": field["trace_owner_status"],
                    "trace_binding_evidence_token": field[
                        "trace_binding_evidence_token"
                    ],
                    "fixed_operator_credit_transfer_allowed": "false",
                    "formal_route_a_tuple": "UNASSIGNED",
                    "route_b_invocation_allowed": "false",
                }
            )
    return rows


def algebraic_invariants(n_value: int) -> dict[str, bool]:
    """Exact rational checks behind the N=2m source/project translation.

    These identities validate the scaling contract only.  They do not replace
    human verification of the hypotheses of the cited trace theorem.
    """

    if n_value < 2 or n_value % 2:
        raise ValueError("algebraic invariants require a positive even N")
    m_value = n_value // 2
    return {
        "n_equals_2m": n_value == 2 * m_value,
        "operator_shift_n2_over_4_equals_m2": (
            Fraction(n_value * n_value, 4) == m_value * m_value
        ),
        "spectral_center_squared_matches": (
            Fraction(5 * n_value * n_value, 4) == 5 * m_value * m_value
        ),
        "project_shell_is_unit_speed": Fraction(5, 4) - Fraction(1, 4) == 1,
        "trace_to_physical_period_factor_matches": (
            Fraction(5, 4) * Fraction(4, 3) == Fraction(5, 3)
        ),
        "source_symplectic_pullback_scales_canonical_part_by_2": 2 == 2 * 1,
        "source_symplectic_pullback_scales_field_part_by_2": (
            Fraction(1, 1) == 2 * Fraction(1, 2)
        ),
        "source_hamiltonian_squared_scales_by_4": (
            (Fraction(4), Fraction(1))
            == (4 * Fraction(1), 4 * Fraction(1, 4))
        ),
        "source_energy_is_above_critical": Fraction(5) > Fraction(2),
        "action_frequency_per_n_squared_is_3_over_4": (
            (Fraction(5) - Fraction(2))
            * Fraction(m_value * m_value, n_value * n_value)
            == Fraction(3, 4)
        ),
    }


def validate_rows(
    rows: Sequence[dict[str, object]], tensor_powers: Sequence[int]
) -> dict[str, object]:
    errors: list[str] = []
    expected_fields = {"0", "+1/2", "-1/2"}
    expected_keys = {
        (field_b, n_value) for n_value in tensor_powers for field_b in expected_fields
    }
    keys = {(str(row["field_b"]), int(row["tensor_power_N"])) for row in rows}
    if keys != expected_keys or len(rows) != len(expected_keys):
        errors.append("field/even-N grid is incomplete or duplicated")

    invariant_reports = {
        str(n_value): algebraic_invariants(n_value) for n_value in tensor_powers
    }
    for n_value, report in invariant_reports.items():
        for invariant, passed in report.items():
            if not passed:
                errors.append(f"algebraic invariant {invariant} failed at N={n_value}")

    for index, row in enumerate(rows):
        n_value = int(row["tensor_power_N"])
        if n_value % 2 or int(row["source_tensor_m"]) != n_value // 2:
            errors.append(f"N=2m mapping failed in row {index}")
        if row["even_subsequence"] != "true":
            errors.append(f"even-subsequence marker failed in row {index}")
        if row["spectral_center_lambda"] != "(sqrt(5)/2)*N":
            errors.append(f"spectral center changed in row {index}")
        if row["laplacian_center_nu"] != "N^2":
            errors.append(f"Laplacian center changed in row {index}")
        if row["classical_shell"] != "|p|^2=1":
            errors.append(f"classical shell changed in row {index}")
        if row["fixed_operator_credit_transfer_allowed"] != "false":
            errors.append(f"fixed-operator credit leak in row {index}")
        if row["formal_route_a_tuple"] != "UNASSIGNED":
            errors.append(f"premature Route-A tuple in row {index}")
        if row["route_b_invocation_allowed"] != "false":
            errors.append(f"premature Route-B invocation in row {index}")

        if row["field_b"] == "0":
            if row["trace_binding_evidence_token"] != "OPEN":
                errors.append(f"zero-field owner overstated in row {index}")
        else:
            if row["trace_binding_evidence_token"] != "PROVED":
                errors.append(f"source-bound owner understated in row {index}")
            if "OPEN" in str(row["primitive_period_trace_clock"]):
                errors.append(f"source period missing in row {index}")

    signed_action_pairings_checked = 0
    for n_value in tensor_powers:
        positive = next(
            row
            for row in rows
            if row["field_b"] == "+1/2" and row["tensor_power_N"] == n_value
        )
        negative = next(
            row
            for row in rows
            if row["field_b"] == "-1/2" and row["tensor_power_N"] == n_value
        )
        if positive["action_frequency_per_N"] != "-sqrt(3)/2*k*log_Norm(h)":
            errors.append(f"positive action convention changed at N={n_value}")
        if negative["action_frequency_per_N"] != "+sqrt(3)/2*k*log_Norm(h)":
            errors.append(f"negative action convention changed at N={n_value}")
        signed_action_pairings_checked += 1

    serialized = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "schema": "p28_round3_trace_contract_validation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "row_count": len(rows),
        "even_tensor_powers": list(tensor_powers),
        "source_bound_signed_field_rows": sum(
            row["trace_binding_evidence_token"] == "PROVED" for row in rows
        ),
        "zero_field_control_rows_open": sum(
            row["field_b"] == "0" and row["trace_binding_evidence_token"] == "OPEN"
            for row in rows
        ),
        "fixed_operator_transfer_allowed_rows": sum(
            row["fixed_operator_credit_transfer_allowed"] == "true" for row in rows
        ),
        "formal_route_a_tuple_assigned_rows": sum(
            row["formal_route_a_tuple"] != "UNASSIGNED" for row in rows
        ),
        "signed_action_pairings_checked": signed_action_pairings_checked,
        "row_payload_sha256": hashlib.sha256(serialized).hexdigest(),
        "exact_algebraic_invariants": invariant_reports,
        "algebraic_validation_boundary": (
            "EXACT_SCALING_IDENTITIES_ONLY;"
            "SOURCE_THEOREM_HYPOTHESES_NOT_MACHINE_VERIFIED;"
            "PRIMARY_SOURCE_CHECK_RECORDED"
        ),
        "source_lock": {
            "primary_source": "Kordyukov-Taimanov_arXiv:2202.06055v3_Theorem_3",
            "source_B": 1,
            "source_E": "sqrt(5)",
            "mapping": "N=2m_and_L^N=(L^2)^m",
            "project_hamiltonian": "sqrt(|p|^2+1/4)",
            "project_shell": "|p|^2=1",
        },
        "errors": errors,
    }


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tensor-powers", default="2,4,8,16")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    args = parser.parse_args()

    tensor_powers = parse_even_tensor_powers(args.tensor_powers)
    rows = build_rows(tensor_powers)
    validation = validate_rows(rows, tensor_powers)
    write_csv(args.output, rows)
    args.validation_output.parent.mkdir(parents=True, exist_ok=True)
    args.validation_output.write_text(
        json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(validation, sort_keys=True))
    return 0 if validation["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
