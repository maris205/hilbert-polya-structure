#!/usr/bin/env python3
"""Build the P28 Round-6 exact conjugacy-closure certificate.

Round 5 conservatively withheld eight proved primitive marked records because
each shared a homology axis with an already credited record.  This builder
binds the immutable Round-5 artifacts and verifies eight explicit witnesses

    x^{-1} g x = h

exactly in the source-locked SL(2) model over
Q(s,t,i), s^2=2, t^2=1+s, i^2=-1.  The witnesses prove that all eight
withheld records are conjugate duplicates, so no new primitive-axis owner is
minted.  The historical Round-5 census and 576-row branch ledger are never
rewritten.

The non-arithmetic genus-two control remains uninstantiated.  A separate
machine-readable gate records that the currently locked package lacks every
required control-geometry source; this builder never fabricates matrices,
systoles, or an arithmeticity verdict.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Sequence


ROUND5_MODULE_PATH = Path(__file__).with_name(
    "build_round5_bolza_marked_cyclic_census.py"
)
SPEC = importlib.util.spec_from_file_location(
    "p28_round5_for_round6", ROUND5_MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round5_bolza_marked_cyclic_census.py")
ROUND5 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ROUND5
SPEC.loader.exec_module(ROUND5)


ROUND4_MODULE_PATH = Path(__file__).with_name("build_round4_bolza_owner_ledger.py")

EXPECTED_SOURCE_SHA256 = {
    "round5_builder": "5af6bcf33aa3afafac5f51d68d0b02cb161cecfe1a1d2b797909ef5100168f3b",
    "round4_builder": "1e0b036e445461da656dac51b5c868dd9a7f9f92e25c8484852a1925556899c6",
    "round5_census": "d3d3fab9a62de100247d76141f0fb96cfe988c5fedb4bfe14dea262a64f88b27",
    "round5_branch_ledger": "5f9cc50dfba3bb257a8a4f32c8bc5bd322a683788da4c9b900e9f8a5a62ee493",
    "round5_certificate": "0af70bab2ec3e63a4bfb3270b44b8fcbc074206123d45b77dbdcd49d3fa45979",
    "round5_validation": "4ed53804a31605190d38dbe06894893e58fdab3d7b7bcfa44602538f090a02a0",
    "round5_control_contract": "a17e7090d9c1bcc80d994d01895b9a01a72246d1bd29cad09fa0049fc3e70fd4",
}


# A source package is not ready merely because its aggregate status says so.
# Every execution-bearing flag must remain false until the six-item source
# contract has been supplied and independently verified.
CONTROL_GATE_EXECUTION_FIELDS = (
    "source_package_supplied",
    "geometry_selected",
    "matrices_loaded",
    "nonarithmeticity_verified",
    "systole_verified",
    "common_geometric_cutoff_frozen",
    "census_run",
    "comparison_run",
    "control_instantiation_authorized",
)


# Each tuple is (credited representative, historically withheld duplicate,
# exact conjugator).  The convention checked below is x^{-1} g x = h.
CONJUGACY_SPECS = (
    ("B28R5-C0034", "B28R5-C0039", "f3^-1*f0^-1"),
    ("B28R5-C0036", "B28R5-C0049", "f3^-1*f2*f1^-1"),
    ("B28R5-C0046", "B28R5-C0051", "f0*f1^-1"),
    ("B28R5-C0067", "B28R5-C0070", "f0*f1^-1"),
    ("B28R5-C0168", "B28R5-C0267", "f3^-1*f2*f1^-1"),
    ("B28R5-C0143", "B28R5-C0271", "f0"),
    ("B28R5-C0173", "B28R5-C0272", "f0*f1^-1*f1^-1"),
    ("B28R5-C0169", "B28R5-C0293", "f0^-1"),
)


CONJUGACY_FIELDS = (
    "resolution_id",
    "schema",
    "source_census_id",
    "source_canonical_word",
    "historically_withheld_census_id",
    "historically_withheld_canonical_word",
    "conjugator_word",
    "conjugator_marked_length",
    "conjugator_exact_psl_key_sha256",
    "conjugacy_convention",
    "exact_sl2_direct_equality",
    "projective_sign",
    "inverse_fallback_used",
    "source_target_literal_projective_distinct",
    "gamma_primitivity_status",
    "inverse_paired_homology_axis_key",
    "exact_trace",
    "exact_trace_squared",
    "primitive_axis_owner_id",
    "historical_owner_status",
    "round6_owner_resolution",
    "owner_count_delta",
    "branch_ledger_action",
    "full_gamma_conjugacy_completeness",
    "arithmetic_label",
    "target_data_used",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_source_hash(label: str, path: Path) -> str:
    actual = sha256_file(path)
    expected = EXPECTED_SOURCE_SHA256[label]
    if actual != expected:
        raise ValueError(
            f"source-lock digest mismatch for {label}: expected {expected}, found {actual}"
        )
    return actual


def load_source_package(
    census_path: Path,
    branch_path: Path,
    certificate_path: Path,
    validation_path: Path,
    control_contract_path: Path,
) -> dict[str, object]:
    """Load and fail-closed validate the immutable Round-5 evidence package."""

    source_digests = {
        "round5_builder": assert_source_hash("round5_builder", ROUND5_MODULE_PATH),
        "round4_builder": assert_source_hash("round4_builder", ROUND4_MODULE_PATH),
        "round5_census": assert_source_hash("round5_census", census_path),
        "round5_branch_ledger": assert_source_hash("round5_branch_ledger", branch_path),
        "round5_certificate": assert_source_hash(
            "round5_certificate", certificate_path
        ),
        "round5_validation": assert_source_hash("round5_validation", validation_path),
        "round5_control_contract": assert_source_hash(
            "round5_control_contract", control_contract_path
        ),
    }
    census_rows = read_csv(census_path)
    branch_rows = read_csv(branch_path)
    certificate = read_json(certificate_path)
    validation = read_json(validation_path)
    control_contract = read_json(control_contract_path)

    if len(census_rows) != 390 or len(branch_rows) != 576:
        raise ValueError("Round-5 row counts changed")
    if certificate.get("status") != "PASS" or validation.get("status") != "PASS":
        raise ValueError("Round-5 certificate/validation is not PASS")
    if validation.get("distinct_inverse_paired_owner_credit_count") != 36:
        raise ValueError("Round-5 owner count changed")
    if (
        validation.get(
            "proved_primitive_records_withheld_for_homology_axis_ambiguity"
        )
        != 8
    ):
        raise ValueError("Round-5 withheld count changed")
    if control_contract.get("status") != "DESIGN_ONLY_NOT_INSTANTIATED":
        raise ValueError("non-arithmetic control contract was prematurely promoted")
    execution = control_contract.get("execution")
    if not isinstance(execution, dict) or any(bool(value) for value in execution.values()):
        raise ValueError("non-arithmetic control execution flags are not all false")

    return {
        "source_digests": source_digests,
        "census_rows": census_rows,
        "branch_rows": branch_rows,
        "certificate": certificate,
        "validation": validation,
        "control_contract": control_contract,
    }


def matrix_conjugate(matrix: object, conjugator: object) -> object:
    return ROUND5.matrix_multiply(
        ROUND5.matrix_multiply(
            ROUND5.matrix_inverse_det_one(conjugator), matrix
        ),
        conjugator,
    )


def build_conjugacy_rows(source_package: dict[str, object]) -> list[dict[str, object]]:
    census_rows = source_package["census_rows"]
    if not isinstance(census_rows, list):
        raise TypeError("census_rows must be a list")
    census_index = {str(row["census_id"]): row for row in census_rows}
    output: list[dict[str, object]] = []

    for ordinal, (source_id, duplicate_id, conjugator_text) in enumerate(
        CONJUGACY_SPECS, start=1
    ):
        source = census_index[source_id]
        duplicate = census_index[duplicate_id]
        source_word = ROUND5.parse_word_text(str(source["canonical_marked_word"]))
        duplicate_word = ROUND5.parse_word_text(
            str(duplicate["canonical_marked_word"])
        )
        conjugator_word = ROUND5.parse_word_text(conjugator_text)
        source_matrix = ROUND5.word_matrix(source_word)
        duplicate_matrix = ROUND5.word_matrix(duplicate_word)
        conjugator_matrix = ROUND5.word_matrix(conjugator_word)
        conjugated = matrix_conjugate(source_matrix, conjugator_matrix)

        direct_equal = conjugated == duplicate_matrix
        negative_duplicate_key = tuple(
            -entry for entry in ROUND5.matrix_flat_key(duplicate_matrix)
        )
        projective_sign = (
            "+"
            if direct_equal
            else "-"
            if ROUND5.matrix_flat_key(conjugated) == negative_duplicate_key
            else "NONE"
        )
        inverse_equal = ROUND5.projective_matrix_key(conjugated) == (
            ROUND5.projective_matrix_key(
                ROUND5.matrix_inverse_det_one(duplicate_matrix)
            )
        )
        literal_distinct = ROUND5.projective_matrix_key(source_matrix) != (
            ROUND5.projective_matrix_key(duplicate_matrix)
        )

        output.append(
            {
                "resolution_id": f"B28R6-Q{ordinal:02d}",
                "schema": "p28_round6_exact_gamma_conjugacy_resolution/1.0",
                "source_census_id": source_id,
                "source_canonical_word": source["canonical_marked_word"],
                "historically_withheld_census_id": duplicate_id,
                "historically_withheld_canonical_word": duplicate[
                    "canonical_marked_word"
                ],
                "conjugator_word": conjugator_text,
                "conjugator_marked_length": len(conjugator_word),
                "conjugator_exact_psl_key_sha256": ROUND5.key_sha256(
                    ROUND5.projective_matrix_key(conjugator_matrix)
                ),
                "conjugacy_convention": "x^-1*g*x=h",
                "exact_sl2_direct_equality": str(direct_equal).lower(),
                "projective_sign": projective_sign,
                "inverse_fallback_used": "false",
                "source_target_literal_projective_distinct": str(
                    literal_distinct
                ).lower(),
                "gamma_primitivity_status": source["gamma_primitivity_status"],
                "inverse_paired_homology_axis_key": source[
                    "inverse_paired_homology_axis_key"
                ],
                "exact_trace": source["exact_trace"],
                "exact_trace_squared": source["exact_trace_squared"],
                "primitive_axis_owner_id": source["primitive_axis_owner_id"],
                "historical_owner_status": duplicate["owner_credit_status"],
                "round6_owner_resolution": "CERTIFIED_CONJUGATE_DUPLICATE_NO_NEW_OWNER",
                "owner_count_delta": 0,
                "branch_ledger_action": "REUSE_ROUND5_576_ROWS_BYTE_FOR_BYTE",
                "full_gamma_conjugacy_completeness": "NOT_ESTABLISHED_OUTSIDE_FROZEN_EIGHT",
                "arithmetic_label": "NONE",
                "target_data_used": "false",
                "formal_route_a_tuple": "UNASSIGNED",
                "route_b_invocation_allowed": "false",
                "_inverse_equal_internal": inverse_equal,
                "_source_row_internal": source,
                "_duplicate_row_internal": duplicate,
                "_conjugator_word_internal": conjugator_word,
            }
        )
    return output


def public_conjugacy_rows(
    rows: Sequence[dict[str, object]],
) -> list[dict[str, object]]:
    return [{field: row[field] for field in CONJUGACY_FIELDS} for row in rows]


def nonarithmetic_source_package_gate(
    source_package: dict[str, object],
) -> dict[str, object]:
    control_contract = source_package["control_contract"]
    source_digests = source_package["source_digests"]
    if not isinstance(control_contract, dict) or not isinstance(source_digests, dict):
        raise TypeError("invalid source package")
    requirements = {
        "named_closed_genus2_constant_curvature_surface": "MISSING",
        "explicit_torsion_free_cocompact_fuchsian_matrices": "MISSING",
        "presentation_and_checked_group_relation": "MISSING",
        "primary_or_peer_reviewed_source_locator": "MISSING",
        "independent_nonarithmeticity_certificate": "MISSING",
        "rigorous_systole_or_per_owner_primitivity_certificate": "MISSING",
    }
    return {
        "schema": "p28_round6_nonarithmetic_source_package_gate/1.0",
        "status": "FAIL_CLOSED_NOT_READY",
        "evidence_token": "OPEN",
        "audit_scope": "CURRENT_SOURCE_LOCK_ONLY",
        "round5_control_contract_sha256": source_digests[
            "round5_control_contract"
        ],
        "round5_control_contract_status": control_contract["status"],
        "requirements": requirements,
        "requirements_satisfied": 0,
        "requirements_total": len(requirements),
        "source_package_supplied": False,
        "geometry_selected": False,
        "matrices_loaded": False,
        "nonarithmeticity_verified": False,
        "systole_verified": False,
        "common_geometric_cutoff_frozen": False,
        "census_run": False,
        "comparison_run": False,
        "control_instantiation_authorized": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "claim_boundary": (
            "MISSING_SOURCE_PACKAGE_RECORDED;NO_CONTROL_GEOMETRY_"
            "MATRICES_SYSTOLE_NONARITHMETICITY_OR_RESULT_FABRICATED"
        ),
    }


def validate(
    source_package: dict[str, object],
    rows: Sequence[dict[str, object]],
    control_gate: dict[str, object],
) -> dict[str, object]:
    errors: list[str] = []
    census_rows = source_package["census_rows"]
    branch_rows = source_package["branch_rows"]
    source_digests = source_package["source_digests"]
    if not isinstance(census_rows, list) or not isinstance(branch_rows, list):
        raise TypeError("invalid row package")
    if not isinstance(source_digests, dict):
        raise TypeError("invalid digest package")

    historical_withheld = {
        str(row["census_id"])
        for row in census_rows
        if row["owner_credit_status"]
        == "WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED"
    }
    certified_duplicates = {
        str(row["historically_withheld_census_id"]) for row in rows
    }
    if certified_duplicates != historical_withheld:
        errors.append("the exact eight historical withheld records were not resolved")
    if len(rows) != 8 or len(certified_duplicates) != 8:
        errors.append("expected eight unique conjugacy resolutions")

    exact_direct_count = 0
    inverse_fallback_count = 0
    literal_distinct_count = 0
    for row in rows:
        source = row["_source_row_internal"]
        duplicate = row["_duplicate_row_internal"]
        conjugator_word = row["_conjugator_word_internal"]
        if not isinstance(source, dict) or not isinstance(duplicate, dict):
            errors.append("internal source row binding failed")
            continue
        if row["exact_sl2_direct_equality"] != "true" or row["projective_sign"] != "+":
            errors.append(f"direct exact equality failed for {row['resolution_id']}")
        else:
            exact_direct_count += 1
        if row["inverse_fallback_used"] != "false":
            inverse_fallback_count += 1
        if row["source_target_literal_projective_distinct"] != "true":
            errors.append(f"source/duplicate literal distinction failed for {row['resolution_id']}")
        else:
            literal_distinct_count += 1
        if row["_inverse_equal_internal"]:
            errors.append(f"unexpected inverse equality for {row['resolution_id']}")
        if not ROUND5.is_freely_reduced(conjugator_word):
            errors.append(f"conjugator is not freely reduced for {row['resolution_id']}")
        if source["gamma_primitivity_status"] != (
            "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE"
        ) or duplicate["gamma_primitivity_status"] != (
            "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE"
        ):
            errors.append(f"non-proved primitive entered {row['resolution_id']}")
        for field in (
            "inverse_paired_homology_axis_key",
            "exact_trace",
            "exact_trace_squared",
            "geodesic_length_decimal",
        ):
            if source[field] != duplicate[field]:
                errors.append(f"frozen peer field {field} changed for {row['resolution_id']}")
        if row["owner_count_delta"] != 0 or row["round6_owner_resolution"] != (
            "CERTIFIED_CONJUGATE_DUPLICATE_NO_NEW_OWNER"
        ):
            errors.append(f"owner disposition failed for {row['resolution_id']}")

    credited = [
        row
        for row in census_rows
        if row["owner_credit_status"] == "MINTED_INVERSE_PAIRED_AXIS_OWNER"
    ]
    owner_ids = {str(row["primitive_axis_owner_id"]) for row in credited}
    branch_owner_ids = {str(row["primitive_axis_owner_id"]) for row in branch_rows}
    if len(credited) != 36 or len(owner_ids) != 36 or branch_owner_ids != owner_ids:
        errors.append("the 36-owner set changed")
    if len(branch_rows) != 576:
        errors.append("the Round-5 branch ledger row count changed")
    for field_b in ("+1/2", "-1/2"):
        field_rows = [row for row in branch_rows if row["field_b"] == field_b]
        if len(field_rows) != 288 or len(
            {row["primitive_axis_owner_id"] for row in field_rows}
        ) != 36:
            errors.append(f"owner/branch count changed for field {field_b}")

    proved_count = sum(
        row["gamma_primitivity_status"]
        == "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE"
        for row in census_rows
    )
    gamma_open_count = sum(
        row["gamma_primitivity_status"] == "NOT_ESTABLISHED_MARKED_PRIMITIVE_ONLY"
        for row in census_rows
    )
    marked_power_count = sum(
        row["marked_class_status"] == "MARKED_CYCLIC_POWER" for row in census_rows
    )
    if (proved_count, gamma_open_count, marked_power_count) != (44, 322, 24):
        errors.append("Round-5 primitivity/power populations changed")

    if control_gate.get("status") != "FAIL_CLOSED_NOT_READY":
        errors.append("non-arithmetic source-package gate did not fail closed")
    if control_gate.get("requirements_satisfied") != 0:
        errors.append("non-arithmetic control was fabricated or prematurely authorized")
    for field in CONTROL_GATE_EXECUTION_FIELDS:
        if control_gate.get(field) is not False:
            errors.append(
                f"non-arithmetic control gate field {field} did not fail closed"
            )

    public_rows = public_conjugacy_rows(rows)
    payload = json.dumps(public_rows, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return {
        "schema": "p28_round6_exact_gamma_conjugacy_validation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "round5_source_sha256": source_digests,
        "historically_withheld_record_count": len(historical_withheld),
        "conjugacy_resolution_count": len(rows),
        "exact_direct_sl2_conjugacy_count": exact_direct_count,
        "inverse_fallback_count": inverse_fallback_count,
        "literal_source_target_distinct_count": literal_distinct_count,
        "certified_conjugate_duplicate_count": len(certified_duplicates),
        "unresolved_count_within_frozen_eight": len(
            historical_withheld - certified_duplicates
        ),
        "new_owner_credit_count": sum(int(row["owner_count_delta"]) for row in rows),
        "gamma_primitivity_proved_record_count": proved_count,
        "primitive_axis_owner_count_per_field": len(owner_ids),
        "field_axis_owner_pair_count": 2 * len(owner_ids),
        "branch_row_count": len(branch_rows),
        "round5_branch_ledger_reused_byte_for_byte": True,
        "round5_branch_ledger_sha256": source_digests["round5_branch_ledger"],
        "gamma_primitivity_open_count": gamma_open_count,
        "marked_power_count": marked_power_count,
        "conjugacy_payload_sha256": hashlib.sha256(payload).hexdigest(),
        "full_gamma_conjugacy_completeness": "NOT_ESTABLISHED_OUTSIDE_FROZEN_EIGHT",
        "nonarithmetic_control_status": "DESIGN_ONLY_NOT_INSTANTIATED",
        "nonarithmetic_source_package_gate": control_gate["status"],
        "target_data_rows": sum(
            row["target_data_used"] != "false" for row in public_rows
        ),
        "arithmetic_label_rows": sum(
            row["arithmetic_label"] != "NONE" for row in public_rows
        ),
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "a4_credit": "NONE",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "errors": errors,
    }


def write_csv(
    path: Path, fields: Sequence[str], rows: Sequence[dict[str, object]]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round5-census", required=True, type=Path)
    parser.add_argument("--round5-branch-ledger", required=True, type=Path)
    parser.add_argument("--round5-certificate", required=True, type=Path)
    parser.add_argument("--round5-validation", required=True, type=Path)
    parser.add_argument("--round5-control-contract", required=True, type=Path)
    parser.add_argument("--conjugacy-output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    parser.add_argument("--control-gate-output", required=True, type=Path)
    arguments = parser.parse_args()

    source_package = load_source_package(
        arguments.round5_census,
        arguments.round5_branch_ledger,
        arguments.round5_certificate,
        arguments.round5_validation,
        arguments.round5_control_contract,
    )
    internal_rows = build_conjugacy_rows(source_package)
    public_rows = public_conjugacy_rows(internal_rows)
    control_gate = nonarithmetic_source_package_gate(source_package)
    validation = validate(source_package, internal_rows, control_gate)

    if validation["status"] != "PASS":
        raise RuntimeError("Round-6 conjugacy validation failed: " + "; ".join(validation["errors"]))
    write_csv(arguments.conjugacy_output, CONJUGACY_FIELDS, public_rows)
    write_json(arguments.validation_output, validation)
    write_json(arguments.control_gate_output, control_gate)
    print(
        json.dumps(
            {
                "status": validation["status"],
                "exact_direct_sl2_conjugacies": validation[
                    "exact_direct_sl2_conjugacy_count"
                ],
                "certified_conjugate_duplicates": validation[
                    "certified_conjugate_duplicate_count"
                ],
                "new_owner_credits": validation["new_owner_credit_count"],
                "owners_per_field": validation[
                    "primitive_axis_owner_count_per_field"
                ],
                "branch_rows_reused": validation["branch_row_count"],
                "nonarithmetic_control": validation[
                    "nonarithmetic_control_status"
                ],
                "formal_route_a_tuple": validation["formal_route_a_tuple"],
                "route_b_invocation_allowed": validation[
                    "route_b_invocation_allowed"
                ],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
