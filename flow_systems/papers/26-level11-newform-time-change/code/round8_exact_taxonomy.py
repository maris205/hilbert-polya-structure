#!/usr/bin/env python3
"""P26 Round-8 exact taxonomy of all frozen Hecke cycle owners.

Round 6 used binary64 quadrature to audit quadratic degree moments.  Round 7
replaced numerical zero tests by exact Schreier homology for four p=5
survivors.  This module closes the finite-ledger gap: it classifies every one
of the 138 Round-4 cycle-owner instances and all 55 word/prime groups over
exact rational homology.

No target-prime table, Riemann-zero table, floating-point zero decision, global
primitive enumeration, dynamical determinant, or Route-B construction occurs
here.  The inherited numerical moments are used only as cross-checks.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Sequence


DATE = "2026-08-28"
FORMAL_TUPLE = (
    "(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)"
)
PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_ROUND4_CYCLE_LEDGER = (
    PROJECT_DIR / "results" / "round4_hecke_cycle_ledger.csv"
)
DEFAULT_ROUND6_MOMENT_LEDGER = (
    PROJECT_DIR / "results" / "round6_quadratic_degree_moment_ledger.csv"
)
EXPECTED_ROUND4_CYCLE_SHA256 = (
    "f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662"
)
EXPECTED_ROUND6_MOMENT_SHA256 = (
    "f95e1435c9293f8e008cebf80084ea2b522b76186dbd684b5e3997c5e588edea"
)
NUMERICAL_CROSSCHECK_TOLERANCE = 1.0e-10

SCALAR_LAWS = ("a_p", "a_p_squared", "a_p_squared_minus_p")
PRIMARY_LAWS = ("a_p", "a_p_squared")
SECONDARY_CONTROL_LAW = "a_p_squared_minus_p"

FULL_KERNEL = "FULL_COMPLEX_SOURCE_KERNEL"
PROJECTION_ONLY_KERNEL = "REAL_PROJECTION_ONLY_KERNEL"
TRUE_NONKERNEL = "TRUE_REAL_PROJECTION_NONKERNEL"
DEGENERATE_INSTANCE = "DEGENERATE_OR_OTHER"

FULL_GROUP_SURVIVOR = "EXACT_FULL_COMPLEX_KERNEL_SURVIVOR"
PROJECTION_GROUP_SURVIVOR = "EXACT_REAL_PROJECTION_ONLY_KERNEL_SURVIVOR"
TRUE_GROUP_FAILURE = "TRUE_QUADRATIC_MOMENT_FAILURE_NONKERNEL"
DEGENERATE_GROUP = "DEGENERATE_OR_OTHER"

FROZEN_SURVIVOR_GROUPS = {
    ("LRRLRRR", 5),
    ("LLRLLRLR", 5),
    ("LLLRLLRLR", 5),
    ("LLLRLRLLR", 5),
}

EXPECTED_INSTANCE_CLASS_COUNTS = {
    FULL_KERNEL: 2,
    PROJECTION_ONLY_KERNEL: 2,
    TRUE_NONKERNEL: 134,
    DEGENERATE_INSTANCE: 0,
}

INSTANCE_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "cycle_id",
    "cycle_degree",
    "cycle_branches",
    "cycle_owner_matrix",
    "owner_recomputed_equal_exact",
    "owner_determinant",
    "owner_c_mod_11",
    "primitive_in_gamma0_11_exact_recomputed",
    "primitive_root_exponent_recomputed",
    "homology_coordinates_y0_11",
    "compact_homology_coordinates_x0_11",
    "conjugate_homology_coordinates_y0_11",
    "real_symmetrized_coordinates_y0_11",
    "source_real_eigenspace_coordinate_k",
    "owner_real_eigenspace_coordinate_k",
    "normalized_real_period_ratio_exact",
    "normalized_real_period_square_exact",
    "compact_homology_zero_exact",
    "real_projection_zero_exact",
    "full_complex_period_zero_exact",
    "exact_instance_classification",
    "round4_period_real_crosscheck",
    "round4_period_imag_crosscheck",
    "proof_evidence_token",
    "quadrature_evidence_token",
    "target_data_used",
    "formal_a2_evaluation_run",
    "route_b_invocation_allowed",
)

GROUP_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "scalar_law",
    "scalar_lambda_p_exact",
    "source_real_eigenspace_coordinate_k",
    "cycle_owner_instances",
    "cycle_degree_profile",
    "normalized_quadratic_moments_by_degree_exact",
    "required_normalized_moments_by_degree_exact",
    "signed_residuals_by_degree_exact",
    "degree_one_residual_zero_exact",
    "all_nonunit_degree_moments_zero_exact",
    "all_degree_moment_residuals_zero_exact",
    "nonunit_full_complex_kernel_instances",
    "nonunit_real_projection_only_kernel_instances",
    "nonunit_true_nonkernel_instances",
    "exact_group_classification",
    "round6_numerical_group_pass",
    "exact_and_round6_numerical_verdict_agree",
    "max_round6_normalized_moment_crosscheck_residual",
    "criterion_scope",
    "proof_evidence_token",
    "quadrature_evidence_token",
    "target_data_used",
    "formal_a2_evaluation_run",
    "route_b_invocation_allowed",
)


def _load_module(filename: str, module_name: str):
    module_path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ROUND7 = _load_module("round7_exact_survivors.py", "p26_round7_for_round8")
ROUND2 = ROUND7.ROUND2
ROUND4 = ROUND7.ROUND4


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def fraction_text(value: Fraction) -> str:
    return ROUND7.fraction_text(value)


def coordinate_text(values: Sequence[Fraction]) -> str:
    return ROUND7.coordinate_text(values)


def degree_map_text(values: dict[int, Fraction]) -> str:
    return "|".join(
        f"{degree}:{fraction_text(values[degree])}" for degree in sorted(values)
    )


def scalar_value(law: str, eigenvalue: int, prime: int) -> int:
    if law == "a_p":
        return eigenvalue
    if law == "a_p_squared":
        return eigenvalue * eigenvalue
    if law == "a_p_squared_minus_p":
        return eigenvalue * eigenvalue - prime
    raise ValueError(f"unknown scalar law: {law!r}")


def real_symmetrized_coordinates(
    matrix: ROUND7.Matrix,
    arcs: Sequence[ROUND7.Arc],
    dual_basis: Sequence[Sequence[Fraction]],
) -> tuple[Fraction, ...]:
    coordinates = ROUND7.homology_coordinates(matrix, arcs, dual_basis)
    conjugate = ROUND7.homology_coordinates(
        ROUND7.conjugate_owner(matrix), arcs, dual_basis
    )
    return ROUND7.add_coordinates(coordinates, conjugate)


def real_eigenspace_coordinate(
    matrix: ROUND7.Matrix,
    arcs: Sequence[ROUND7.Arc],
    dual_basis: Sequence[Sequence[Fraction]],
) -> Fraction:
    symmetrized = real_symmetrized_coordinates(matrix, arcs, dual_basis)
    if symmetrized[0] != 0 or symmetrized[2] != 0:
        raise ValueError(
            "real symmetrization left the exact one-dimensional + eigenspace"
        )
    return symmetrized[1]


def recompute_cycle_owner(
    row: dict[str, str],
) -> tuple[list[str], ROUND7.Matrix, dict[str, object]]:
    word = row["word"]
    prime = int(row["hecke_prime"])
    source = ROUND2.matrix_from_word(word)
    representatives = ROUND4.hecke_representatives(prime)
    representative_map = dict(representatives)
    ordered_ids = [branch_id for branch_id, _ in representatives]
    cycles = ROUND4.permutation_cycles(
        ROUND4.right_action_permutation(source, prime), ordered_ids
    )
    cycle_index = int(row["cycle_id"])
    if cycle_index < 1 or cycle_index > len(cycles):
        raise ValueError(f"invalid cycle id for {word}|p={prime}: {cycle_index}")
    cycle = cycles[cycle_index - 1]
    branch = representative_map[cycle[0]]
    owner = ROUND4.integral_matrix(
        ROUND4.multiply(
            ROUND4.multiply(branch, ROUND2.matrix_power(source, len(cycle))),
            ROUND4.rational_inverse(branch),
        )
    )
    return cycle, owner, ROUND4.primitivity_certificate(owner)


def moment_source_map(
    rows: Sequence[dict[str, str]],
) -> dict[tuple[str, int, int], dict[str, str]]:
    output: dict[tuple[str, int, int], dict[str, str]] = {}
    for row in rows:
        key = (
            row["word"],
            int(row["hecke_prime"]),
            int(row["hecke_cycle_degree_d"]),
        )
        if key in output:
            raise ValueError(f"duplicate Round-6 moment key: {key!r}")
        output[key] = row
    return output


def numerical_status_field(law: str) -> str:
    return f"lambda_{law}_moment_status"


def build_taxonomy(
    cycle_rows: Sequence[dict[str, str]],
    moment_rows: Sequence[dict[str, str]],
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    arcs, relations = ROUND7.relation_matrix()
    _, pivots = ROUND7.rref(relations)
    dual_basis = ROUND7.nullspace_basis(relations)
    cusp = ROUND7.homology_coordinates(ROUND7.T_MATRIX, arcs, dual_basis)
    if (
        len(arcs),
        len(relations),
        len(pivots),
        len(dual_basis),
        cusp,
    ) != (24, 35, 21, 3, (Fraction(-1), Fraction(0), Fraction(0))):
        raise AssertionError("unexpected exact Gamma_0(11) homology model")

    grouped_cycles: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    source_coordinates: dict[str, Fraction] = {}
    instance_rows: list[dict[str, object]] = []

    for source_row in cycle_rows:
        word = source_row["word"]
        prime = int(source_row["hecke_prime"])
        source_matrix = ROUND2.matrix_from_word(word)
        source_k = source_coordinates.setdefault(
            word, real_eigenspace_coordinate(source_matrix, arcs, dual_basis)
        )
        cycle, owner, primitive_certificate = recompute_cycle_owner(source_row)
        locked_owner = ROUND7.parse_matrix(source_row["cycle_owner_matrix"])
        owner_equal = owner == locked_owner
        if not owner_equal:
            raise ValueError(f"Round-4 owner mismatch for {word}|p={prime}")
        if "|".join(cycle) != source_row["cycle_branches"]:
            raise ValueError(f"Round-4 cycle branch mismatch for {word}|p={prime}")

        coordinates = ROUND7.homology_coordinates(owner, arcs, dual_basis)
        conjugate_coordinates = ROUND7.homology_coordinates(
            ROUND7.conjugate_owner(owner), arcs, dual_basis
        )
        expected_conjugate_coordinates = (
            -coordinates[0],
            coordinates[1] + coordinates[2],
            -coordinates[2],
        )
        if conjugate_coordinates != expected_conjugate_coordinates:
            raise ValueError(
                f"exact real-involution matrix mismatch for {word}|p={prime}"
            )
        symmetrized = ROUND7.add_coordinates(coordinates, conjugate_coordinates)
        compact_zero = ROUND7.in_rational_span(coordinates, cusp)
        real_zero = ROUND7.in_rational_span(symmetrized, cusp)
        owner_k = real_eigenspace_coordinate(owner, arcs, dual_basis)

        if source_k == 0:
            ratio: Fraction | None = None
            category = DEGENERATE_INSTANCE
        else:
            ratio = owner_k / source_k
            if compact_zero:
                category = FULL_KERNEL
            elif real_zero:
                category = PROJECTION_ONLY_KERNEL
            else:
                category = TRUE_NONKERNEL

        row: dict[str, object] = {
            "word": word,
            "hecke_prime": prime,
            "a_p": int(source_row["a_p"]),
            "cycle_id": int(source_row["cycle_id"]),
            "cycle_degree": len(cycle),
            "cycle_branches": "|".join(cycle),
            "cycle_owner_matrix": ROUND7.format_matrix(owner),
            "owner_recomputed_equal_exact": str(owner_equal).lower(),
            "owner_determinant": ROUND7.determinant(owner),
            "owner_c_mod_11": owner[2] % ROUND7.LEVEL,
            "primitive_in_gamma0_11_exact_recomputed": str(
                primitive_certificate["primitive"]
            ).lower(),
            "primitive_root_exponent_recomputed": primitive_certificate[
                "primitive_root_exponent"
            ],
            "homology_coordinates_y0_11": coordinate_text(coordinates),
            "compact_homology_coordinates_x0_11": coordinate_text(coordinates[1:]),
            "conjugate_homology_coordinates_y0_11": coordinate_text(
                conjugate_coordinates
            ),
            "real_symmetrized_coordinates_y0_11": coordinate_text(symmetrized),
            "source_real_eigenspace_coordinate_k": fraction_text(source_k),
            "owner_real_eigenspace_coordinate_k": fraction_text(owner_k),
            "normalized_real_period_ratio_exact": (
                "UNDEFINED" if ratio is None else fraction_text(ratio)
            ),
            "normalized_real_period_square_exact": (
                "UNDEFINED" if ratio is None else fraction_text(ratio * ratio)
            ),
            "compact_homology_zero_exact": str(compact_zero).lower(),
            "real_projection_zero_exact": str(real_zero).lower(),
            "full_complex_period_zero_exact": str(compact_zero).lower(),
            "exact_instance_classification": category,
            "round4_period_real_crosscheck": source_row["period_real"],
            "round4_period_imag_crosscheck": source_row["period_imag"],
            "proof_evidence_token": "PROVED",
            "quadrature_evidence_token": "NUMERICAL_OBSERVATION",
            "target_data_used": "false",
            "formal_a2_evaluation_run": "false",
            "route_b_invocation_allowed": "false",
            "_ratio": ratio,
        }
        instance_rows.append(row)
        grouped_cycles[(word, prime)].append(row)

    moment_map = moment_source_map(moment_rows)
    group_rows: list[dict[str, object]] = []
    for (word, prime), instances in grouped_cycles.items():
        eigenvalue = int(instances[0]["a_p"])
        source_k = source_coordinates[word]
        degrees = sorted({1, *(int(row["cycle_degree"]) for row in instances)})
        exact_moments = {
            degree: sum(
                (
                    Fraction(row["_ratio"]) ** 2
                    for row in instances
                    if int(row["cycle_degree"]) == degree
                ),
                Fraction(0),
            )
            for degree in degrees
        }

        numerical_pass_by_law = {
            law: all(
                moment_map[(word, prime, degree)][numerical_status_field(law)]
                == "PASS_NUMERICAL_OBSERVATION"
                for degree in degrees
            )
            for law in SCALAR_LAWS
        }
        crosscheck_residuals: list[float] = []
        for degree in degrees:
            numerical_row = moment_map[(word, prime, degree)]
            base_square = float(numerical_row["base_alpha_period_squared"])
            numerical_normalized = (
                float(numerical_row["quadratic_alpha_moment_Q_d"]) / base_square
            )
            crosscheck_residuals.append(
                abs(numerical_normalized - float(exact_moments[degree]))
            )
        max_crosscheck = max(crosscheck_residuals, default=0.0)

        nonunit = [row for row in instances if int(row["cycle_degree"]) > 1]
        full_nonunit = sum(
            row["exact_instance_classification"] == FULL_KERNEL for row in nonunit
        )
        projection_nonunit = sum(
            row["exact_instance_classification"] == PROJECTION_ONLY_KERNEL
            for row in nonunit
        )
        true_nonunit = sum(
            row["exact_instance_classification"] == TRUE_NONKERNEL
            for row in nonunit
        )

        for law in SCALAR_LAWS:
            scalar = scalar_value(law, eigenvalue, prime)
            required = {
                degree: Fraction(scalar if degree == 1 else 0)
                for degree in degrees
            }
            residuals = {
                degree: exact_moments[degree] - required[degree]
                for degree in degrees
            }
            degree_one_zero = residuals[1] == 0
            nonunit_zero = all(
                exact_moments[degree] == 0 for degree in degrees if degree > 1
            )
            exact_pass = all(value == 0 for value in residuals.values())
            if source_k == 0:
                group_category = DEGENERATE_GROUP
            elif not exact_pass:
                group_category = TRUE_GROUP_FAILURE
            elif nonunit and full_nonunit == len(nonunit):
                group_category = FULL_GROUP_SURVIVOR
            elif (
                nonunit
                and true_nonunit == 0
                and projection_nonunit > 0
                and full_nonunit + projection_nonunit == len(nonunit)
            ):
                group_category = PROJECTION_GROUP_SURVIVOR
            else:
                group_category = DEGENERATE_GROUP

            group_rows.append(
                {
                    "word": word,
                    "hecke_prime": prime,
                    "a_p": eigenvalue,
                    "scalar_law": law,
                    "scalar_lambda_p_exact": scalar,
                    "source_real_eigenspace_coordinate_k": fraction_text(source_k),
                    "cycle_owner_instances": len(instances),
                    "cycle_degree_profile": "|".join(
                        str(int(row["cycle_degree"])) for row in instances
                    ),
                    "normalized_quadratic_moments_by_degree_exact": degree_map_text(
                        exact_moments
                    ),
                    "required_normalized_moments_by_degree_exact": degree_map_text(
                        required
                    ),
                    "signed_residuals_by_degree_exact": degree_map_text(residuals),
                    "degree_one_residual_zero_exact": str(degree_one_zero).lower(),
                    "all_nonunit_degree_moments_zero_exact": str(
                        nonunit_zero
                    ).lower(),
                    "all_degree_moment_residuals_zero_exact": str(exact_pass).lower(),
                    "nonunit_full_complex_kernel_instances": full_nonunit,
                    "nonunit_real_projection_only_kernel_instances": (
                        projection_nonunit
                    ),
                    "nonunit_true_nonkernel_instances": true_nonunit,
                    "exact_group_classification": group_category,
                    "round6_numerical_group_pass": str(
                        numerical_pass_by_law[law]
                    ).lower(),
                    "exact_and_round6_numerical_verdict_agree": str(
                        exact_pass == numerical_pass_by_law[law]
                    ).lower(),
                    "max_round6_normalized_moment_crosscheck_residual": (
                        max_crosscheck
                    ),
                    "criterion_scope": (
                        "EXACT_NECESSARY_AND_SUFFICIENT_FOR_THE_PREDECLARED_"
                        "P_ONLY_SCALAR_ALL_S_SECOND_VARIATION_IDENTITY_ON_"
                        "THIS_FINITE_HECKE_OUTPUT_MULTISET"
                    ),
                    "proof_evidence_token": "PROVED",
                    "quadrature_evidence_token": "NUMERICAL_OBSERVATION",
                    "target_data_used": "false",
                    "formal_a2_evaluation_run": "false",
                    "route_b_invocation_allowed": "false",
                }
            )

    for row in instance_rows:
        row.pop("_ratio")

    homology_model = {
        "presentation": "PSL(2,Z)=<s,r | s^2=r^3=1>",
        "right_coset_model": "Gamma_0(11)\\PSL(2,Z)=P^1(F_11)",
        "right_cosets": 12,
        "schreier_arcs": len(arcs),
        "relation_matrix_rows": len(relations),
        "relation_matrix_rank_over_q": len(pivots),
        "homology_dimension_y0_11_over_q": len(dual_basis),
        "cusp_direction": coordinate_text(cusp),
        "compact_homology_dimension_x0_11_over_q": 2,
        "real_involution_on_y0_coordinates": (
            "tau(x,y,z)=(-x,y+z,-z)"
        ),
        "real_involution_matrix": [[-1, 0, 0], [0, 1, 1], [0, 0, -1]],
        "compact_plus_eigenspace_dimension": 1,
        "real_symmetrization_rule": (
            "h+tau(h)=(0,2y+z,0); k(h)=2y+z"
        ),
        "normalized_real_period_rule": (
            "RePeriod(delta)/RePeriod(source)=k(delta)/k(source) when "
            "k(source)!=0"
        ),
        "quadratic_moment_rule": (
            "Q_d/RePeriod(source)^2=sum_{degree(delta)=d} "
            "(k(delta)/k(source))^2"
        ),
    }
    return instance_rows, group_rows, homology_model


def validate_outputs(
    instance_rows: Sequence[dict[str, object]],
    group_rows: Sequence[dict[str, object]],
    homology_model: dict[str, object],
) -> list[str]:
    errors: list[str] = []
    if len(instance_rows) != 138:
        errors.append("expected 138 exact instance rows")
    if len(group_rows) != 55 * len(SCALAR_LAWS):
        errors.append("expected 165 exact group/law rows")

    instance_counts = Counter(
        str(row["exact_instance_classification"]) for row in instance_rows
    )
    for category, expected in EXPECTED_INSTANCE_CLASS_COUNTS.items():
        if instance_counts[category] != expected:
            errors.append(
                f"unexpected instance count for {category}: "
                f"{instance_counts[category]} != {expected}"
            )
    if any(row["owner_recomputed_equal_exact"] != "true" for row in instance_rows):
        errors.append("a recomputed cycle owner differs from the locked ledger")
    if any(
        row["primitive_in_gamma0_11_exact_recomputed"] != "true"
        for row in instance_rows
    ):
        errors.append("a cycle-owner instance is not primitive on exact replay")
    if any(row["owner_determinant"] != 1 for row in instance_rows):
        errors.append("owner determinant failure")
    if any(row["owner_c_mod_11"] != 0 for row in instance_rows):
        errors.append("owner subgroup failure")
    if any(
        (row["real_projection_zero_exact"] == "true")
        != (row["normalized_real_period_ratio_exact"] == "0")
        for row in instance_rows
    ):
        errors.append("real-kernel and exact-ratio decisions disagree")

    expected_instance_by_prime = {
        2: {TRUE_NONKERNEL: 18},
        3: {TRUE_NONKERNEL: 22},
        5: {FULL_KERNEL: 2, PROJECTION_ONLY_KERNEL: 2, TRUE_NONKERNEL: 26},
        7: {TRUE_NONKERNEL: 30},
        13: {TRUE_NONKERNEL: 38},
    }
    for prime, expected in expected_instance_by_prime.items():
        actual = Counter(
            str(row["exact_instance_classification"])
            for row in instance_rows
            if int(row["hecke_prime"]) == prime
        )
        for category in EXPECTED_INSTANCE_CLASS_COUNTS:
            if actual[category] != expected.get(category, 0):
                errors.append(
                    f"unexpected p={prime} instance taxonomy for {category}"
                )

    expected_groups_by_law = {
        "a_p": {
            FULL_GROUP_SURVIVOR: 2,
            PROJECTION_GROUP_SURVIVOR: 2,
            TRUE_GROUP_FAILURE: 51,
            DEGENERATE_GROUP: 0,
        },
        "a_p_squared": {
            FULL_GROUP_SURVIVOR: 2,
            PROJECTION_GROUP_SURVIVOR: 2,
            TRUE_GROUP_FAILURE: 51,
            DEGENERATE_GROUP: 0,
        },
        "a_p_squared_minus_p": {
            FULL_GROUP_SURVIVOR: 0,
            PROJECTION_GROUP_SURVIVOR: 0,
            TRUE_GROUP_FAILURE: 55,
            DEGENERATE_GROUP: 0,
        },
    }
    for law, expected in expected_groups_by_law.items():
        actual = Counter(
            str(row["exact_group_classification"])
            for row in group_rows
            if row["scalar_law"] == law
        )
        for category, count in expected.items():
            if actual[category] != count:
                errors.append(
                    f"unexpected {law} group count for {category}: "
                    f"{actual[category]} != {count}"
                )

    if any(
        row["exact_and_round6_numerical_verdict_agree"] != "true"
        for row in group_rows
    ):
        errors.append("an exact group verdict disagrees with the Round-6 cross-check")
    if any(
        float(row["max_round6_normalized_moment_crosscheck_residual"])
        > NUMERICAL_CROSSCHECK_TOLERANCE
        for row in group_rows
    ):
        errors.append("a Round-6 numerical moment missed its exact rational value")
    if any(row["target_data_used"] != "false" for row in instance_rows):
        errors.append("target-data prohibition failed for instance ledger")
    if any(row["target_data_used"] != "false" for row in group_rows):
        errors.append("target-data prohibition failed for group ledger")
    if homology_model.get("compact_plus_eigenspace_dimension") != 1:
        errors.append("unexpected compact real-plus eigenspace dimension")
    return errors


def write_csv(
    path: Path, rows: Sequence[dict[str, object]], fields: Sequence[str]
) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def binding(path: Path) -> dict[str, object]:
    return {
        "path": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def nested_counter(
    rows: Sequence[dict[str, object]], key_field: str, category_field: str
) -> dict[str, dict[str, int]]:
    output: dict[str, dict[str, int]] = {}
    keys = sorted({str(row[key_field]) for row in rows}, key=lambda x: int(x))
    for key in keys:
        counts = Counter(
            str(row[category_field]) for row in rows if str(row[key_field]) == key
        )
        output[key] = dict(sorted(counts.items()))
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--round4-cycle-ledger", type=Path, default=DEFAULT_ROUND4_CYCLE_LEDGER
    )
    parser.add_argument(
        "--round6-moment-ledger", type=Path, default=DEFAULT_ROUND6_MOMENT_LEDGER
    )
    args = parser.parse_args()

    input_errors: list[str] = []
    if sha256(args.round4_cycle_ledger) != EXPECTED_ROUND4_CYCLE_SHA256:
        input_errors.append("Round-4 cycle-ledger SHA-256 mismatch")
    if sha256(args.round6_moment_ledger) != EXPECTED_ROUND6_MOMENT_SHA256:
        input_errors.append("Round-6 moment-ledger SHA-256 mismatch")
    cycle_rows = read_csv(args.round4_cycle_ledger)
    moment_rows = read_csv(args.round6_moment_ledger)
    instance_rows, group_rows, homology_model = build_taxonomy(
        cycle_rows, moment_rows
    )
    errors = input_errors + validate_outputs(instance_rows, group_rows, homology_model)
    if errors:
        raise SystemExit("; ".join(errors))

    args.output.mkdir(parents=True, exist_ok=True)
    instance_path = args.output / "round8_exact_instance_taxonomy_ledger.csv"
    group_path = args.output / "round8_exact_group_moment_taxonomy_ledger.csv"
    summary_path = args.output / "round8_summary.json"
    manifest_path = args.output / "round8_artifact_manifest.json"
    write_csv(instance_path, instance_rows, INSTANCE_FIELDS)
    write_csv(group_path, group_rows, GROUP_FIELDS)

    instance_class_counts = Counter(
        str(row["exact_instance_classification"]) for row in instance_rows
    )
    law_class_counts = {
        law: dict(
            sorted(
                Counter(
                    str(row["exact_group_classification"])
                    for row in group_rows
                    if row["scalar_law"] == law
                ).items()
            )
        )
        for law in SCALAR_LAWS
    }
    per_prime_law_counts = {
        str(prime): {
            law: dict(
                sorted(
                    Counter(
                        str(row["exact_group_classification"])
                        for row in group_rows
                        if int(row["hecke_prime"]) == prime
                        and row["scalar_law"] == law
                    ).items()
                )
            )
            for law in SCALAR_LAWS
        }
        for prime in sorted({int(row["hecke_prime"]) for row in group_rows})
    }

    failure_mechanisms: dict[str, dict[str, int]] = {}
    for law in SCALAR_LAWS:
        failed = [
            row
            for row in group_rows
            if row["scalar_law"] == law
            and row["exact_group_classification"] == TRUE_GROUP_FAILURE
        ]
        failure_mechanisms[law] = {
            "degree_one_only": sum(
                row["degree_one_residual_zero_exact"] == "false"
                and row["all_nonunit_degree_moments_zero_exact"] == "true"
                for row in failed
            ),
            "nonunit_only": sum(
                row["degree_one_residual_zero_exact"] == "true"
                and row["all_nonunit_degree_moments_zero_exact"] == "false"
                for row in failed
            ),
            "degree_one_and_nonunit": sum(
                row["degree_one_residual_zero_exact"] == "false"
                and row["all_nonunit_degree_moments_zero_exact"] == "false"
                for row in failed
            ),
        }

    primary_survivors = sorted(
        f"{row['word']}|p={row['hecke_prime']}|{row['exact_group_classification']}"
        for row in group_rows
        if row["scalar_law"] == "a_p_squared"
        and row["all_degree_moment_residuals_zero_exact"] == "true"
    )
    max_numerical_residual = max(
        float(row["max_round6_normalized_moment_crosscheck_residual"])
        for row in group_rows
    )
    summary = {
        "schema": "p26-round8-complete-exact-taxonomy-summary/1.0",
        "date": DATE,
        "status": "PASS",
        "classification": "COMPLETE_FROZEN_FINITE_EXACT_HOMOLOGY_TAXONOMY",
        "instances": {
            "total": len(instance_rows),
            "classification_counts": dict(sorted(instance_class_counts.items())),
            "classification_counts_by_prime": nested_counter(
                instance_rows, "hecke_prime", "exact_instance_classification"
            ),
            "unresolved": 0,
            "floating_point_zero_decisions": 0,
        },
        "groups": {
            "word_prime_groups": len(group_rows) // len(SCALAR_LAWS),
            "group_law_rows": len(group_rows),
            "law_classification_counts": law_class_counts,
            "per_prime_law_classification_counts": per_prime_law_counts,
            "failure_mechanisms": failure_mechanisms,
            "a_p_squared_exact_survivors": primary_survivors,
            "exact_round6_numerical_verdict_agreements": sum(
                row["exact_and_round6_numerical_verdict_agree"] == "true"
                for row in group_rows
            ),
            "max_round6_normalized_moment_crosscheck_residual": (
                max_numerical_residual
            ),
        },
        "homology_model": homology_model,
        "theorem": {
            "status": "PROVED",
            "statement": (
                "For every one of the 138 frozen Hecke cycle-owner instances, "
                "the real newform-period ratio is the exact rational number "
                "k(delta)/k(source), where k(x,y,z)=2y+z on the one-dimensional "
                "compact + eigenspace. Consequently each normalized quadratic "
                "degree moment is a rational sum of squares. Exactly two "
                "instances are full compact-homology kernels, two are nonzero "
                "real-projection-only kernels, and 134 are true nonkernels. "
                "The a_p and a_p^2 laws each have exactly four p=5 group "
                "survivors and 51 exact failures; the a_p^2-p control has "
                "55 exact failures."
            ),
            "quadratic_residual_equivalence": (
                "For d>1, Q_d=0 iff every degree-d owner is in the exact real-"
                "projection kernel; at d=1 the rational square sum must equal "
                "the predeclared scalar lambda_p."
            ),
            "numerical_smallness_used_as_proof": False,
        },
        "source_bindings": {
            "round4_cycle_ledger_sha256": sha256(args.round4_cycle_ledger),
            "round6_moment_ledger_sha256": sha256(args.round6_moment_ledger),
        },
        "claim_boundary": {
            "ars_stage": "STAGE_1_RESEARCH",
            "proposal_stage": "STAGE_1_ROUTE_A_A0_A1",
            "formal_route_a_tuple": FORMAL_TUPLE,
            "overall_route_a_status": "ROUTE_A_EXPLORATORY",
            "complete_frozen_138_instance_taxonomy": True,
            "complete_frozen_55_group_taxonomy": True,
            "complete_gamma0_11_primitive_enumeration": False,
            "global_cross_instance_conjugacy_deduplication": False,
            "primitive_euler_factorization": False,
            "global_zeta_convergence_or_continuation_proved_here": False,
            "a2_dynamical_zeta_evaluation_run": False,
            "root_count_or_zero_matching_run": False,
            "prime_target_table_used": False,
            "riemann_zero_data_used": False,
            "route_b_evaluation": "NOT_RUN",
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "perform exact cross-instance Gamma_0(11) conjugacy "
            "canonicalization/deduplication of the 138 frozen output instances "
            "and repeat the taxonomy on the resulting unique-owner ledger; "
            "this remains Stage 1 and cannot by itself promote A2"
        ),
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    source_paths = (
        Path(__file__),
        Path(__file__).with_name("test_round8_exact_taxonomy.py"),
        PROJECT_DIR / "experiments" / "reproduce_round8.sh",
        PROJECT_DIR / "notes" / "round8_taxonomy_freeze.md",
        args.round4_cycle_ledger,
        args.round6_moment_ledger,
    )
    artifact_paths = (instance_path, group_path, summary_path)
    manifest = {
        "schema": "p26-round8-artifact-manifest/1.0",
        "date": DATE,
        "classification": "COMPLETE_FROZEN_FINITE_EXACT_HOMOLOGY_TAXONOMY",
        "sources": [binding(path) for path in source_paths],
        "artifacts": [binding(path) for path in artifact_paths],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
