#!/usr/bin/env python3
"""Build the target-free P28 tensor-family ownership ledger.

This script records only exact bundle/duality bookkeeping.  It deliberately
does not synthesize magnetic closed orbits, spectral data, a trace regime, or
an energy window.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


FIELDS = (
    "metric_control_id",
    "field_b",
    "base_bundle",
    "base_bundle_degree",
    "tensor_power_N",
    "operator_bundle_degree",
    "semiclassical_parameter_h",
    "rescaled_operator_owner",
    "scaling_evidence_token",
    "hilbert_owner",
    "operator_owner",
    "operator_domain",
    "connection_owner",
    "antiunitary_partner_field",
    "classical_time_reversal_partner_field",
    "holonomy_tensor_rule",
    "operator_identity_at_N1",
    "trace_regime",
    "energy_window",
    "magnetic_orbit_trace_ownership",
    "fixed_operator_credit_transfer_allowed",
    "owner_evidence_token",
    "trace_binding_evidence_token",
)


FIELD_ROWS = (
    {
        "field_b": "0",
        "base_bundle": "trivial",
        "base_bundle_degree": 0,
        "antiunitary_partner_field": "0",
        "classical_time_reversal_partner_field": "0",
        "connection_owner": "trivial_connection",
    },
    {
        "field_b": "+1/2",
        "base_bundle": "L",
        "base_bundle_degree": 1,
        "antiunitary_partner_field": "-1/2",
        "classical_time_reversal_partner_field": "-1/2",
        "connection_owner": "tensor_connection_on_L^N",
    },
    {
        "field_b": "-1/2",
        "base_bundle": "L_dual",
        "base_bundle_degree": -1,
        "antiunitary_partner_field": "+1/2",
        "classical_time_reversal_partner_field": "+1/2",
        "connection_owner": "tensor_connection_on_(L_dual)^N",
    },
)


def parse_tensor_powers(raw: str) -> list[int]:
    values = [int(item.strip()) for item in raw.split(",") if item.strip()]
    if not values or any(value < 1 for value in values):
        raise ValueError("tensor powers must be a nonempty list of positive integers")
    if len(values) != len(set(values)):
        raise ValueError("tensor powers must be unique")
    return sorted(values)


def operator_labels(field_b: str, n_value: int) -> tuple[str, str]:
    if field_b == "0":
        return ("L2(Sigma_B,trivial)", "Delta_trivial")
    if field_b == "+1/2":
        return (f"L2(Sigma_B,L^{n_value})", f"Delta^(L^{n_value})")
    return (
        f"L2(Sigma_B,(L_dual)^{n_value})",
        f"Delta^((L_dual)^{n_value})",
    )


def build_rows(tensor_powers: list[int]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n_value in tensor_powers:
        for field in FIELD_ROWS:
            field_b = str(field["field_b"])
            base_degree = int(field["base_bundle_degree"])
            hilbert_owner, operator_owner = operator_labels(field_b, n_value)
            rows.append(
                {
                    "metric_control_id": "BOLZA_ARITHMETIC_CURVATURE_MINUS_1",
                    "field_b": field_b,
                    "base_bundle": field["base_bundle"],
                    "base_bundle_degree": base_degree,
                    "tensor_power_N": n_value,
                    "operator_bundle_degree": base_degree * n_value,
                    "semiclassical_parameter_h": f"1/{n_value}",
                    "rescaled_operator_owner": "UNASSIGNED",
                    "scaling_evidence_token": "MODELING_CHOICE",
                    "hilbert_owner": hilbert_owner,
                    "operator_owner": operator_owner,
                    "operator_domain": "H2_sections_of_named_bundle",
                    "connection_owner": field["connection_owner"],
                    "antiunitary_partner_field": field["antiunitary_partner_field"],
                    "classical_time_reversal_partner_field": field[
                        "classical_time_reversal_partner_field"
                    ],
                    "holonomy_tensor_rule": "Hol_tensor(gamma^r)=Hol_base(gamma)^(N*r)",
                    "operator_identity_at_N1": str(
                        field_b == "+1/2" and n_value == 1
                    ).lower(),
                    "trace_regime": "UNASSIGNED",
                    "energy_window": "OPEN",
                    "magnetic_orbit_trace_ownership": "NOT_ESTABLISHED",
                    "fixed_operator_credit_transfer_allowed": "false",
                    "owner_evidence_token": "PROVED",
                    "trace_binding_evidence_token": "OPEN",
                }
            )
    return rows


def validate_rows(rows: list[dict[str, object]], tensor_powers: list[int]) -> dict[str, object]:
    errors: list[str] = []
    expected_fields = {"0", "+1/2", "-1/2"}
    keys = {(str(row["field_b"]), int(row["tensor_power_N"])) for row in rows}
    expected_keys = {(field, n_value) for n_value in tensor_powers for field in expected_fields}
    if keys != expected_keys or len(rows) != len(expected_keys):
        errors.append("field/tensor-power grid is incomplete or duplicated")

    partner = {"0": "0", "+1/2": "-1/2", "-1/2": "+1/2"}
    base_degree = {"0": 0, "+1/2": 1, "-1/2": -1}
    for row in rows:
        field_b = str(row["field_b"])
        n_value = int(row["tensor_power_N"])
        if int(row["operator_bundle_degree"]) != base_degree[field_b] * n_value:
            errors.append(f"degree mismatch at {(field_b, n_value)}")
        if row["antiunitary_partner_field"] != partner[field_b]:
            errors.append(f"antiunitary partner mismatch at {(field_b, n_value)}")
        if row["classical_time_reversal_partner_field"] != partner[field_b]:
            errors.append(f"classical partner mismatch at {(field_b, n_value)}")
        if row["trace_regime"] != "UNASSIGNED" or row["energy_window"] != "OPEN":
            errors.append(f"premature trace freeze at {(field_b, n_value)}")
        if row["rescaled_operator_owner"] != "UNASSIGNED":
            errors.append(f"premature rescaled-operator freeze at {(field_b, n_value)}")
        if row["scaling_evidence_token"] != "MODELING_CHOICE":
            errors.append(f"scaling token mismatch at {(field_b, n_value)}")
        if row["magnetic_orbit_trace_ownership"] != "NOT_ESTABLISHED":
            errors.append(f"premature ownership credit at {(field_b, n_value)}")
        if row["fixed_operator_credit_transfer_allowed"] != "false":
            errors.append(f"illegal fixed-operator credit transfer at {(field_b, n_value)}")
        if row["owner_evidence_token"] != "PROVED":
            errors.append(f"owner token mismatch at {(field_b, n_value)}")
        if row["trace_binding_evidence_token"] != "OPEN":
            errors.append(f"trace token mismatch at {(field_b, n_value)}")

    n1_positive = [
        row
        for row in rows
        if row["field_b"] == "+1/2" and int(row["tensor_power_N"]) == 1
    ]
    expected_identity_count = 1 if 1 in tensor_powers else 0
    actual_identity_count = sum(
        row["operator_identity_at_N1"] == "true" for row in rows
    )
    if len(n1_positive) != expected_identity_count or actual_identity_count != expected_identity_count:
        errors.append("N=1 fixed-operator identity marker is incorrect")

    serialized = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "schema": "p28_tensor_family_owner_validation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "row_count": len(rows),
        "tensor_powers": tensor_powers,
        "field_values": ["0", "+1/2", "-1/2"],
        "owner_rows_proved": len(rows),
        "trace_binding_rows_open": sum(
            row["trace_binding_evidence_token"] == "OPEN" for row in rows
        ),
        "orbit_ownership_not_established": sum(
            row["magnetic_orbit_trace_ownership"] == "NOT_ESTABLISHED" for row in rows
        ),
        "fixed_operator_transfer_allowed_rows": sum(
            row["fixed_operator_credit_transfer_allowed"] == "true" for row in rows
        ),
        "row_payload_sha256": hashlib.sha256(serialized).hexdigest(),
        "errors": errors,
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tensor-powers", default="1,2,4,8")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    args = parser.parse_args()

    tensor_powers = parse_tensor_powers(args.tensor_powers)
    rows = build_rows(tensor_powers)
    validation = validate_rows(rows, tensor_powers)
    write_csv(args.output, rows)
    args.validation_output.parent.mkdir(parents=True, exist_ok=True)
    args.validation_output.write_text(
        json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0 if validation["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
