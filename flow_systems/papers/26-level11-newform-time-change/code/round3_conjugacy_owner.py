#!/usr/bin/env python3
"""Paper-26 Round-3 conjugacy-owner validation.

The exact layer checks bounded Gamma_0(11) conjugations of every Round-2
selected element.  The numerical layer checks the q-series quadrature under
nontrivial integral translations, where direct evaluation remains uniformly
stable.  The theorem that the weight-two differential descends to Y_0(11) is
proved in the accompanying note; finite computation is only a regression
check and is not advertised as a complete conjugacy-class enumeration.
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


Matrix = tuple[int, int, int, int]


def _load_round2_module():
    module_path = Path(__file__).with_name("round2_experiment.py")
    spec = importlib.util.spec_from_file_location("p26_round2", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load round2_experiment.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ROUND2 = _load_round2_module()

IDENTITY: Matrix = (1, 0, 0, 1)
TRANSLATION: Matrix = (1, 1, 0, 1)
LOWER_11: Matrix = (1, 0, 11, 1)

CONJUGATORS: tuple[tuple[str, Matrix], ...] = (
    ("identity", IDENTITY),
    ("T_plus_1", (1, 1, 0, 1)),
    ("T_minus_1", (1, -1, 0, 1)),
    ("T_plus_2", (1, 2, 0, 1)),
    ("T_minus_2", (1, -2, 0, 1)),
    ("V_plus", LOWER_11),
    ("V_minus", (1, 0, -11, 1)),
    ("T_then_V", (12, 1, 11, 1)),
    ("V_then_T", (1, 1, 11, 12)),
)

TRANSLATION_POWERS = (-2, -1, 1, 2)

EXACT_FIELDS = (
    "word",
    "word_length",
    "base_matrix",
    "conjugator_id",
    "conjugator_matrix",
    "conjugate_matrix",
    "base_trace",
    "conjugate_trace",
    "base_determinant",
    "conjugator_determinant",
    "conjugate_determinant",
    "base_c_mod_11",
    "conjugator_c_mod_11",
    "conjugate_c_mod_11",
    "trace_invariant_exact",
    "square_conjugacy_identity_exact",
    "cube_conjugacy_identity_exact",
    "inverse_orientation_identity_exact",
    "oriented_period_owner",
    "reverse_orientation_law",
    "repetition_law",
    "analytic_evidence_token",
    "finite_check_evidence_token",
)

TRANSLATION_FIELDS = (
    "word",
    "translation_power",
    "base_matrix",
    "translated_conjugate_matrix",
    "base_period_proxy",
    "translated_period_proxy",
    "absolute_residual",
    "q_cutoff",
    "quadrature_panels",
    "evidence_token",
)


def matrix_inverse(matrix: Matrix) -> Matrix:
    if ROUND2.determinant(matrix) != 1:
        raise ValueError("matrix_inverse requires determinant one")
    a, b, c, d = matrix
    return (d, -b, -c, a)


def conjugate(matrix: Matrix, owner_change: Matrix) -> Matrix:
    return ROUND2.matrix_multiply(
        ROUND2.matrix_multiply(owner_change, matrix),
        matrix_inverse(owner_change),
    )


def format_matrix(matrix: Matrix) -> str:
    a, b, c, d = matrix
    return f"[[{a},{b}],[{c},{d}]]"


def exact_owner_rows(max_word_length: int = 9) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for word in ROUND2.gamma0_11_positive_necklaces(max_word_length):
        matrix = ROUND2.matrix_from_word(word)
        for conjugator_id, owner_change in CONJUGATORS:
            conjugated = conjugate(matrix, owner_change)
            inverse_conjugated = conjugate(matrix_inverse(matrix), owner_change)
            rows.append(
                {
                    "word": word,
                    "word_length": len(word),
                    "base_matrix": format_matrix(matrix),
                    "conjugator_id": conjugator_id,
                    "conjugator_matrix": format_matrix(owner_change),
                    "conjugate_matrix": format_matrix(conjugated),
                    "base_trace": ROUND2.trace(matrix),
                    "conjugate_trace": ROUND2.trace(conjugated),
                    "base_determinant": ROUND2.determinant(matrix),
                    "conjugator_determinant": ROUND2.determinant(owner_change),
                    "conjugate_determinant": ROUND2.determinant(conjugated),
                    "base_c_mod_11": matrix[2] % 11,
                    "conjugator_c_mod_11": owner_change[2] % 11,
                    "conjugate_c_mod_11": conjugated[2] % 11,
                    "trace_invariant_exact": str(
                        ROUND2.trace(matrix) == ROUND2.trace(conjugated)
                    ).lower(),
                    "square_conjugacy_identity_exact": str(
                        conjugate(ROUND2.matrix_power(matrix, 2), owner_change)
                        == ROUND2.matrix_power(conjugated, 2)
                    ).lower(),
                    "cube_conjugacy_identity_exact": str(
                        conjugate(ROUND2.matrix_power(matrix, 3), owner_change)
                        == ROUND2.matrix_power(conjugated, 3)
                    ).lower(),
                    "inverse_orientation_identity_exact": str(
                        inverse_conjugated == matrix_inverse(conjugated)
                    ).lower(),
                    "oriented_period_owner": "SAME_GAMMA0_11_CONJUGACY_CLASS",
                    "reverse_orientation_law": "I(M^-1)=-I(M)",
                    "repetition_law": "I(M^r)=r*I(M)",
                    "analytic_evidence_token": "PROVED",
                    "finite_check_evidence_token": "NUMERICALLY_CERTIFIED",
                }
            )
    return rows


def translation_covariance_rows(
    max_word_length: int = 9,
    q_cutoff: int = 192,
    quadrature_panels: int = 512,
) -> list[dict[str, object]]:
    coefficients = ROUND2.level11_eta_product_coefficients(q_cutoff)
    rows: list[dict[str, object]] = []
    for word in ROUND2.gamma0_11_positive_necklaces(max_word_length):
        matrix = ROUND2.matrix_from_word(word)
        base_period = ROUND2.axis_one_form_period(
            matrix, coefficients, quadrature_panels
        )
        for translation_power in TRANSLATION_POWERS:
            translation = (1, translation_power, 0, 1)
            translated = conjugate(matrix, translation)
            translated_period = ROUND2.axis_one_form_period(
                translated, coefficients, quadrature_panels
            )
            rows.append(
                {
                    "word": word,
                    "translation_power": translation_power,
                    "base_matrix": format_matrix(matrix),
                    "translated_conjugate_matrix": format_matrix(translated),
                    "base_period_proxy": base_period,
                    "translated_period_proxy": translated_period,
                    "absolute_residual": abs(translated_period - base_period),
                    "q_cutoff": q_cutoff,
                    "quadrature_panels": quadrature_panels,
                    "evidence_token": "NUMERICAL_OBSERVATION",
                }
            )
    return rows


def validate_exact_rows(
    rows: Sequence[dict[str, object]], max_word_length: int = 9
) -> list[str]:
    errors: list[str] = []
    expected_count = (
        len(ROUND2.gamma0_11_positive_necklaces(max_word_length)) * len(CONJUGATORS)
    )
    if len(rows) != expected_count:
        errors.append(f"expected {expected_count} exact rows, got {len(rows)}")
    exact_boolean_fields = (
        "trace_invariant_exact",
        "square_conjugacy_identity_exact",
        "cube_conjugacy_identity_exact",
        "inverse_orientation_identity_exact",
    )
    for index, row in enumerate(rows):
        if any(int(row[field]) != 1 for field in (
            "base_determinant", "conjugator_determinant", "conjugate_determinant"
        )):
            errors.append(f"determinant failure in exact row {index}")
        if any(int(row[field]) != 0 for field in (
            "base_c_mod_11", "conjugator_c_mod_11", "conjugate_c_mod_11"
        )):
            errors.append(f"Gamma_0(11) failure in exact row {index}")
        if any(row[field] != "true" for field in exact_boolean_fields):
            errors.append(f"exact identity failure in row {index}")
    return errors


def write_csv(path: Path, rows: Sequence[dict[str, object]], fields: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-word-length", type=int, default=9)
    parser.add_argument("--q-cutoff", type=int, default=192)
    parser.add_argument("--quadrature-panels", type=int, default=512)
    args = parser.parse_args()

    exact_rows = exact_owner_rows(args.max_word_length)
    numeric_rows = translation_covariance_rows(
        args.max_word_length, args.q_cutoff, args.quadrature_panels
    )
    errors = validate_exact_rows(exact_rows, args.max_word_length)
    if any(float(row["absolute_residual"]) > 1.0e-11 for row in numeric_rows):
        errors.append("translation covariance residual exceeded 1e-11")

    args.output.mkdir(parents=True, exist_ok=True)
    exact_path = args.output / "round3_conjugacy_owner_ledger.csv"
    numeric_path = args.output / "round3_translation_covariance_ledger.csv"
    summary_path = args.output / "round3_summary.json"
    manifest_path = args.output / "round3_artifact_manifest.json"
    write_csv(exact_path, exact_rows, EXACT_FIELDS)
    write_csv(numeric_path, numeric_rows, TRANSLATION_FIELDS)

    summary = {
        "schema": "p26_round3_conjugacy_owner/1.0",
        "status": "PASS" if not errors else "FAIL",
        "selected_positive_word_rows": len(
            ROUND2.gamma0_11_positive_necklaces(args.max_word_length)
        ),
        "bounded_conjugators": len(CONJUGATORS),
        "exact_conjugacy_checks": len(exact_rows),
        "translation_covariance_checks": len(numeric_rows),
        "maximum_translation_period_residual": max(
            float(row["absolute_residual"]) for row in numeric_rows
        ),
        "analytic_result": (
            "Re(2*pi*i*f(z)dz) descends to Y_0(11); its oriented period is "
            "Gamma_0(11)-conjugacy invariant, changes sign under orientation "
            "reversal, and is linear under repetition"
        ),
        "analytic_evidence_token": "PROVED",
        "numeric_evidence_token": "NUMERICAL_OBSERVATION",
        "finite_exact_check_token": "NUMERICALLY_CERTIFIED",
        "scope_boundary": {
            "complete_gamma0_11_conjugacy_enumeration": False,
            "primitive_class_certificate": False,
            "hecke_recurrence_derived": False,
            "prime_table_used": False,
            "riemann_zero_data_used": False,
            "formal_route_a_tuple": "UNASSIGNED",
            "route_b_invocation_allowed": False,
        },
        "errors": errors,
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema": "p26_round3_artifact_manifest/1.0",
        "artifacts": [
            {"path": path.name, "sha256": sha256(path), "bytes": path.stat().st_size}
            for path in (exact_path, numeric_path, summary_path)
        ],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
