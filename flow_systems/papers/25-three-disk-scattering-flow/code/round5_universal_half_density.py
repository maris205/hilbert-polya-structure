#!/usr/bin/env python3
"""Round-5 universal half-density theorem ledger for Paper 25.

For a real two-dimensional symplectic hyperbolic return map with eigenvalues
``sigma*Lambda`` and ``sigma/Lambda``, ``Lambda > 1`` and ``sigma in {+1,-1}``,
the exact repetition stability amplitude is

    |det(I-M^r)|^(-1/2)
      = Lambda^(-r/2) / |1-sigma^r Lambda^(-r)|.

Thus the project statistic ``Lambda^(-r/2)`` is the universal leading factor,
not an arithmetic discriminator.  This program replays that exact identity on
the frozen 2,241-row three-disk ledger for repetitions r=1,2,3.  It reads no
prime table, Riemann-zero table, or fitted target.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from typing import Iterable

import mpmath as mp


mp.mp.dps = 100

DATE = "2026-08-27"
REPETITIONS = (1, 2, 3)
EXPECTED_SOURCE_ROWS = 2241
EXPECTED_OUTPUT_ROWS = EXPECTED_SOURCE_ROWS * len(REPETITIONS)
ROUND2_SHA256 = "25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736"
ROUND3_SHA256 = "1b932a5ca3cf7123e9428b3eb2f26078d8e289eabb11dd828379ecf39eeb414e"
THEOREM_ID = "P25-UNIVERSAL-2D-HYPERBOLIC-STABILITY-AMPLITUDE"
STATISTIC_ID = "UNSTABLE_MULTIPLIER_HALF_DENSITY_V1"


LEDGER_FIELDS = [
    "branch_id",
    "primitive_owner_id",
    "d_over_a",
    "topological_word_length",
    "cyclic_word",
    "repetition_index",
    "branch_class",
    "physical_primitive_eigenvalue_sign",
    "physical_repetition_eigenvalue_sign",
    "direct_trace_magnitude",
    "unstable_multiplier_magnitude",
    "unstable_multiplier_power",
    "universal_half_density",
    "source_half_density_r1",
    "source_half_density_relative_residual_r1",
    "positive_convention_exact_stability_amplitude",
    "physical_sign_exact_stability_amplitude",
    "positive_amplitude_over_half_density",
    "physical_amplitude_over_half_density",
    "relative_leading_factor_error",
    "trace_reconstruction_relative_residual",
    "positive_formula_relative_residual",
    "physical_formula_relative_residual",
    "theorem_id",
    "theorem_evidence_status",
    "ledger_evidence_status",
    "arithmetic_owner_status",
    "half_density_arithmetic_verdict",
    "prime_or_zero_tables_used",
    "formal_route_a_tuple",
    "a2_evaluation",
    "route_b_invocation_allowed",
]


SUMMARY_FIELDS = [
    "repetition_index",
    "branch_count",
    "primitive_branch_count",
    "repetition_branch_count",
    "negative_eigenvalue_sign_branch_count",
    "max_relative_leading_factor_error",
    "median_relative_leading_factor_error",
    "min_relative_leading_factor_error",
    "max_positive_formula_relative_residual",
    "max_physical_formula_relative_residual",
]


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mp_text(value: mp.mpf, digits: int = 50) -> str:
    if value == 0:
        return "0"
    return mp.nstr(value, digits, min_fixed=-8, max_fixed=12)


def relative_residual(left: mp.mpf, right: mp.mpf) -> mp.mpf:
    return abs(left - right) / max(abs(right), mp.mpf("1e-90"))


def unstable_multiplier_from_trace_magnitude(trace_magnitude: mp.mpf) -> mp.mpf:
    if trace_magnitude <= 2:
        raise ValueError("return map is not hyperbolic")
    return (trace_magnitude + mp.sqrt(trace_magnitude**2 - 4)) / 2


def exact_stability_amplitude(
    unstable_multiplier: mp.mpf, eigenvalue_sign: int, repetition: int
) -> mp.mpf:
    """Return the exact two-dimensional hyperbolic repetition amplitude."""

    multiplier_power = unstable_multiplier**repetition
    repeated_sign = eigenvalue_sign**repetition
    return multiplier_power ** (-mp.mpf("0.5")) / abs(
        1 - repeated_sign / multiplier_power
    )


def determinant_amplitude_from_eigenvalues(
    unstable_multiplier: mp.mpf, eigenvalue_sign: int, repetition: int
) -> mp.mpf:
    multiplier_power = unstable_multiplier**repetition
    repeated_sign = eigenvalue_sign**repetition
    determinant = (1 - repeated_sign * multiplier_power) * (
        1 - repeated_sign / multiplier_power
    )
    return 1 / mp.sqrt(abs(determinant))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def source_paths(project_root: Path) -> tuple[Path, Path]:
    results = project_root / "results"
    return (
        results / "three_disk_primitive_ledger_round2.csv",
        results / "three_disk_return_map_validation_round3.csv",
    )


def median(values: Iterable[mp.mpf]) -> mp.mpf:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("median of empty sequence")
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def build_ledger(project_root: Path) -> tuple[list[dict[str, str]], dict[str, object]]:
    round2_path, round3_path = source_paths(project_root)
    round2_sha = sha256_path(round2_path)
    round3_sha = sha256_path(round3_path)
    if round2_sha != ROUND2_SHA256:
        raise ValueError(f"Round-2 input hash changed: {round2_sha}")
    if round3_sha != ROUND3_SHA256:
        raise ValueError(f"Round-3 input hash changed: {round3_sha}")

    round2_rows = read_csv(round2_path)
    round3_rows = read_csv(round3_path)
    if len(round2_rows) != EXPECTED_SOURCE_ROWS or len(round3_rows) != EXPECTED_SOURCE_ROWS:
        raise ValueError("frozen source row count changed")
    round2_by_id = {row["row_id"]: row for row in round2_rows}
    if len(round2_by_id) != EXPECTED_SOURCE_ROWS:
        raise ValueError("Round-2 row identifiers are not unique")

    rows: list[dict[str, str]] = []
    max_source_half_residual = mp.mpf(0)
    max_trace_reconstruction_residual = mp.mpf(0)
    max_positive_formula_residual = mp.mpf(0)
    max_physical_formula_residual = mp.mpf(0)
    negative_primitive_sign_owners = 0

    for direct in round3_rows:
        owner_id = direct["row_id"]
        source = round2_by_id.get(owner_id)
        if source is None:
            raise ValueError(f"Round-3 owner missing from Round 2: {owner_id}")
        if direct["validation_status"] != "NUMERICALLY_CERTIFIED":
            raise ValueError(f"Round-3 row is not certified: {owner_id}")
        if source["actual_billiard_orbit_status"] != "NUMERICALLY_CERTIFIED":
            raise ValueError(f"Round-2 orbit is not certified: {owner_id}")
        if direct["prime_or_zero_tables_used"] != "false":
            raise ValueError(f"target-data firewall changed: {owner_id}")

        direct_trace = mp.mpf(direct["direct_trace_h1e_36"])
        trace_magnitude = abs(direct_trace)
        unstable = unstable_multiplier_from_trace_magnitude(trace_magnitude)
        primitive_sign = 1 if int(direct["physical_trace_parity_factor"]) > 0 else -1
        if primitive_sign < 0:
            negative_primitive_sign_owners += 1
        reconstructed_trace = unstable + 1 / unstable
        trace_reconstruction_residual = relative_residual(
            reconstructed_trace, trace_magnitude
        )
        max_trace_reconstruction_residual = max(
            max_trace_reconstruction_residual, trace_reconstruction_residual
        )

        source_half = mp.mpf(source["half_density_value"])
        direct_half = unstable ** (-mp.mpf("0.5"))
        source_half_residual = relative_residual(direct_half, source_half)
        max_source_half_residual = max(max_source_half_residual, source_half_residual)

        for repetition in REPETITIONS:
            multiplier_power = unstable**repetition
            half_density = multiplier_power ** (-mp.mpf("0.5"))
            positive_amplitude = exact_stability_amplitude(unstable, 1, repetition)
            physical_amplitude = exact_stability_amplitude(
                unstable, primitive_sign, repetition
            )
            positive_from_determinant = determinant_amplitude_from_eigenvalues(
                unstable, 1, repetition
            )
            physical_from_determinant = determinant_amplitude_from_eigenvalues(
                unstable, primitive_sign, repetition
            )
            positive_formula_residual = relative_residual(
                positive_amplitude, positive_from_determinant
            )
            physical_formula_residual = relative_residual(
                physical_amplitude, physical_from_determinant
            )
            max_positive_formula_residual = max(
                max_positive_formula_residual, positive_formula_residual
            )
            max_physical_formula_residual = max(
                max_physical_formula_residual, physical_formula_residual
            )
            relative_leading_error = multiplier_power ** (-1)
            repeated_sign = primitive_sign**repetition
            rows.append(
                {
                    "branch_id": f"{owner_id}-R{repetition}",
                    "primitive_owner_id": owner_id,
                    "d_over_a": source["d_over_a"],
                    "topological_word_length": source["topological_word_length"],
                    "cyclic_word": source["cyclic_word"],
                    "repetition_index": str(repetition),
                    "branch_class": "PRIMITIVE" if repetition == 1 else "REPETITION",
                    "physical_primitive_eigenvalue_sign": str(primitive_sign),
                    "physical_repetition_eigenvalue_sign": str(repeated_sign),
                    "direct_trace_magnitude": mp_text(trace_magnitude),
                    "unstable_multiplier_magnitude": mp_text(unstable),
                    "unstable_multiplier_power": mp_text(multiplier_power),
                    "universal_half_density": mp_text(half_density),
                    "source_half_density_r1": source["half_density_value"] if repetition == 1 else "",
                    "source_half_density_relative_residual_r1": (
                        mp_text(source_half_residual) if repetition == 1 else ""
                    ),
                    "positive_convention_exact_stability_amplitude": mp_text(
                        positive_amplitude
                    ),
                    "physical_sign_exact_stability_amplitude": mp_text(
                        physical_amplitude
                    ),
                    "positive_amplitude_over_half_density": mp_text(
                        positive_amplitude / half_density
                    ),
                    "physical_amplitude_over_half_density": mp_text(
                        physical_amplitude / half_density
                    ),
                    "relative_leading_factor_error": mp_text(relative_leading_error),
                    "trace_reconstruction_relative_residual": mp_text(
                        trace_reconstruction_residual
                    ),
                    "positive_formula_relative_residual": mp_text(
                        positive_formula_residual
                    ),
                    "physical_formula_relative_residual": mp_text(
                        physical_formula_residual
                    ),
                    "theorem_id": THEOREM_ID,
                    "theorem_evidence_status": "PROVED",
                    "ledger_evidence_status": "NUMERICALLY_CERTIFIED",
                    "arithmetic_owner_status": "ABSENT_BY_CONSTRUCTION",
                    "half_density_arithmetic_verdict": "STOP_SCOPED / PROVES_TOO_MUCH",
                    "prime_or_zero_tables_used": "false",
                    "formal_route_a_tuple": "UNASSIGNED",
                    "a2_evaluation": "NOT_RUN",
                    "route_b_invocation_allowed": "false",
                }
            )

    if len(rows) != EXPECTED_OUTPUT_ROWS:
        raise ValueError("Round-5 output row count changed")

    metrics: dict[str, object] = {
        "schema": "p25_round5_universal_half_density_metrics/1.0",
        "date": DATE,
        "status": "PASS",
        "theorem_id": THEOREM_ID,
        "theorem_evidence_status": "PROVED",
        "theorem_statement": (
            "For a real 2x2 symplectic hyperbolic map with eigenvalues "
            "sigma*Lambda and sigma/Lambda, |det(I-M^r)|^(-1/2)="
            "Lambda^(-r/2)/|1-sigma^r*Lambda^(-r)|."
        ),
        "round2_input_sha256": round2_sha,
        "round3_input_sha256": round3_sha,
        "source_primitive_owner_rows": EXPECTED_SOURCE_ROWS,
        "repetition_indices": list(REPETITIONS),
        "round5_branch_rows": len(rows),
        "primitive_branch_rows": EXPECTED_SOURCE_ROWS,
        "repetition_branch_rows": EXPECTED_OUTPUT_ROWS - EXPECTED_SOURCE_ROWS,
        "negative_primitive_eigenvalue_sign_owners": negative_primitive_sign_owners,
        "max_source_half_density_relative_residual": mp_text(
            max_source_half_residual
        ),
        "max_trace_reconstruction_relative_residual": mp_text(
            max_trace_reconstruction_residual
        ),
        "max_positive_formula_relative_residual": mp_text(
            max_positive_formula_residual
        ),
        "max_physical_formula_relative_residual": mp_text(
            max_physical_formula_residual
        ),
        "paper_disposition": "RETAIN_AS_METHODS_NEGATIVE_CONTROL_PAPER",
        "scientific_consequence": (
            "The tested half-density is the universal leading magnitude of any "
            "two-dimensional symplectic hyperbolic return-map amplitude; its "
            "persistence cannot supply arithmetic specificity."
        ),
        "half_density_evidence_status": "NUMERICAL_OBSERVATION",
        "half_density_control_verdict": "STOP_SCOPED / PROVES_TOO_MUCH",
        "arithmetic_owner_status": "ABSENT_BY_CONSTRUCTION",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "gates_a_e": "NOT_REACHED",
        "prime_or_zero_tables_used": False,
        "manuscript_authorized": False,
    }
    return rows, metrics


def build_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summary: list[dict[str, str]] = []
    for repetition in REPETITIONS:
        selected = [row for row in rows if int(row["repetition_index"]) == repetition]
        errors = [mp.mpf(row["relative_leading_factor_error"]) for row in selected]
        positive_residuals = [
            mp.mpf(row["positive_formula_relative_residual"]) for row in selected
        ]
        physical_residuals = [
            mp.mpf(row["physical_formula_relative_residual"]) for row in selected
        ]
        summary.append(
            {
                "repetition_index": str(repetition),
                "branch_count": str(len(selected)),
                "primitive_branch_count": str(
                    sum(row["branch_class"] == "PRIMITIVE" for row in selected)
                ),
                "repetition_branch_count": str(
                    sum(row["branch_class"] == "REPETITION" for row in selected)
                ),
                "negative_eigenvalue_sign_branch_count": str(
                    sum(
                        row["physical_repetition_eigenvalue_sign"] == "-1"
                        for row in selected
                    )
                ),
                "max_relative_leading_factor_error": mp_text(max(errors)),
                "median_relative_leading_factor_error": mp_text(median(errors)),
                "min_relative_leading_factor_error": mp_text(min(errors)),
                "max_positive_formula_relative_residual": mp_text(
                    max(positive_residuals)
                ),
                "max_physical_formula_relative_residual": mp_text(
                    max(physical_residuals)
                ),
            }
        )
    return summary


def csv_bytes(rows: list[dict[str, str]], fields: list[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def combined_hash(outputs: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name, payload in sorted(outputs.items()):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(payload)
        digest.update(b"\0")
    return digest.hexdigest()


def build_outputs(project_root: Path) -> dict[str, bytes]:
    rows, metrics = build_ledger(project_root)
    summary = build_summary(rows)
    outputs = {
        "round5_universal_half_density_ledger.csv": csv_bytes(rows, LEDGER_FIELDS),
        "round5_universal_half_density_by_repetition.csv": csv_bytes(
            summary, SUMMARY_FIELDS
        ),
        "round5_universal_half_density_metrics.json": json_bytes(metrics),
    }
    return outputs


def write_outputs(output_dir: Path, outputs: dict[str, bytes]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in outputs.items():
        (output_dir / name).write_bytes(payload)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    outputs = build_outputs(args.project_root)
    write_outputs(args.output_dir, outputs)
    print(
        json.dumps(
            {
                "artifact_tree_sha256": combined_hash(outputs),
                "output_files": sorted(outputs),
                "status": "PASS",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
