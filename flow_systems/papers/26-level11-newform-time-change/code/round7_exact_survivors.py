#!/usr/bin/env python3
"""P26 Round-7 exact classification of the four p=5 survivors.

The Round-6 audit squared the *real* part of a level-11 newform period.  Four
degree-five Hecke cycles were numerically near its kernel.  This module decides
that question over exact rational homology, without evaluating target data and
without treating small binary64 values as zeros.

The exact model uses

    PSL(2,Z) = <s,r | s^2=r^3=1>

and the twelve right cosets of Gamma_0(11), identified with P^1(F_11).
Schreier rewriting gives 24 arcs, a relation matrix of rank 21, and the
three-dimensional rational homology of Y_0(11).  Quotienting the cusp-loop
direction gives the two-dimensional homology of X_0(11).  Complex conjugation
then detects the exact real-period kernel.
"""

from __future__ import annotations

import argparse
from collections import deque
import csv
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


Matrix = tuple[int, int, int, int]
Coset = tuple[int, int]
Arc = tuple[Coset, str]

DATE = "2026-08-28"
LEVEL = 11
HECKE_PRIME = 5
FROZEN_WORDS = (
    "LRRLRRR",
    "LLRLLRLR",
    "LLLRLLRLR",
    "LLLRLRLLR",
)
FORMAL_TUPLE = (
    "(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)"
)
NUMERICAL_TOLERANCE = 1.0e-10

IDENTITY: Matrix = (1, 0, 0, 1)
S_MATRIX: Matrix = (0, -1, 1, 0)
R_MATRIX: Matrix = (0, -1, 1, 1)
T_MATRIX: Matrix = (1, 1, 0, 1)

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

CLASSIFICATION_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "cycle_id",
    "cycle_degree",
    "cycle_branches",
    "source_word_matrix",
    "source_plus_homology_coordinates",
    "degree_one_cycle_branches",
    "degree_one_owner_matrix",
    "degree_one_plus_homology_coordinates",
    "degree_one_real_projection_equal_exact",
    "cycle_owner_matrix",
    "owner_determinant",
    "owner_c_mod_11",
    "psl_word_length",
    "homology_coordinates_y0_11",
    "cusp_parabolic_coordinates",
    "compact_homology_zero_exact",
    "conjugate_owner_matrix",
    "conjugate_homology_coordinates_y0_11",
    "conjugation_is_negative_mod_cusp_exact",
    "real_projection_zero_exact",
    "full_complex_period_zero_exact",
    "exact_period_character",
    "round4_period_real",
    "round4_period_imag",
    "round6_degree5_quadratic_real_moment",
    "round6_numerical_survivor",
    "exact_lambda_a_p_squared_group_moment_survivor",
    "exact_classification",
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


ROUND2 = _load_module("round2_experiment.py", "p26_round2_for_round7")
ROUND4 = _load_module("round4_hecke_correspondence.py", "p26_round4_for_round7")


def multiply(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def inverse(matrix: Matrix) -> Matrix:
    if determinant(matrix) != 1:
        raise ValueError("inverse requires determinant one")
    a, b, c, d = matrix
    return (d, -b, -c, a)


def power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        return power(inverse(matrix), -exponent)
    result = IDENTITY
    base = matrix
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        remaining //= 2
    return result


def format_matrix(matrix: Matrix) -> str:
    a, b, c, d = matrix
    return f"[[{a},{b}],[{c},{d}]]"


def parse_matrix(text: str) -> Matrix:
    values = tuple(int(value) for value in re.findall(r"-?\d+", text))
    if len(values) != 4:
        raise ValueError(f"could not parse matrix: {text!r}")
    return values  # type: ignore[return-value]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def canonical_coset(pair: tuple[int, int]) -> Coset:
    c, d = (pair[0] % LEVEL, pair[1] % LEVEL)
    if c == 0:
        return (0, 1)
    scale = pow(c, -1, LEVEL)
    return (1, d * scale % LEVEL)


def coset_action(coset: Coset, generator: str) -> Coset:
    c, d = coset
    if generator == "s":
        return canonical_coset((d, -c))
    if generator == "r":
        return canonical_coset((d, -c + d))
    raise ValueError(f"unknown PSL generator: {generator!r}")


def schreier_transversal() -> tuple[dict[Coset, tuple[str, ...]], tuple[Arc, ...]]:
    """Return a deterministic BFS transversal and its eleven tree arcs."""

    root: Coset = (0, 1)
    words: dict[Coset, tuple[str, ...]] = {root: ()}
    tree_arcs: list[Arc] = []
    queue: deque[Coset] = deque([root])
    while queue:
        coset = queue.popleft()
        for generator in ("s", "r"):
            target = coset_action(coset, generator)
            if target in words:
                continue
            words[target] = words[coset] + (generator,)
            tree_arcs.append((coset, generator))
            queue.append(target)
    if len(words) != LEVEL + 1 or len(tree_arcs) != LEVEL:
        raise AssertionError("unexpected P1(F_11) Schreier-tree size")
    return words, tuple(tree_arcs)


def relation_matrix() -> tuple[tuple[Arc, ...], list[list[Fraction]]]:
    transversal, tree_arcs = schreier_transversal()
    cosets = tuple(sorted(transversal))
    arcs = tuple((coset, generator) for coset in cosets for generator in ("s", "r"))
    arc_index = {arc: index for index, arc in enumerate(arcs)}

    def relation(terms: Iterable[Arc]) -> list[Fraction]:
        row = [Fraction(0) for _ in arcs]
        for term in terms:
            row[arc_index[term]] += 1
        return row

    rows: list[list[Fraction]] = []
    for coset in cosets:
        rows.append(
            relation(((coset, "s"), (coset_action(coset, "s"), "s")))
        )
    for coset in cosets:
        first = coset_action(coset, "r")
        second = coset_action(first, "r")
        rows.append(
            relation(((coset, "r"), (first, "r"), (second, "r")))
        )
    for arc in tree_arcs:
        rows.append(relation((arc,)))
    return arcs, rows


def rref(
    rows: Sequence[Sequence[Fraction]],
) -> tuple[list[list[Fraction]], tuple[int, ...]]:
    matrix = [list(map(Fraction, row)) for row in rows]
    if not matrix:
        return matrix, ()
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    pivot_columns: list[int] = []
    for column in range(column_count):
        selected = next(
            (index for index in range(pivot_row, row_count) if matrix[index][column]),
            None,
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [value / pivot for value in matrix[pivot_row]]
        for index in range(row_count):
            if index == pivot_row or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(matrix[index], matrix[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return matrix, tuple(pivot_columns)


def nullspace_basis(rows: Sequence[Sequence[Fraction]]) -> tuple[tuple[Fraction, ...], ...]:
    reduced, pivots = rref(rows)
    column_count = len(rows[0])
    free_columns = [column for column in range(column_count) if column not in pivots]
    basis: list[tuple[Fraction, ...]] = []
    for free_column in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free_column] = 1
        for pivot_row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[pivot_row][free_column]
        basis.append(tuple(vector))
    return tuple(basis)


def t_word(exponent: int) -> tuple[str, ...]:
    if exponent >= 0:
        return ("s", "r") * exponent
    return ("r", "r", "s") * (-exponent)


def decompose_sl2(matrix: Matrix) -> tuple[str, ...]:
    """Euclidean decomposition into s and r, modulo the central sign."""

    if determinant(matrix) != 1:
        raise ValueError("decomposition requires SL(2,Z)")
    a, b, c, d = matrix
    if c == 0:
        if a != d or abs(a) != 1 or b % a:
            raise ValueError("invalid upper-triangular SL(2,Z) matrix")
        return t_word(b // a)
    quotient = a // c
    reduced = multiply(S_MATRIX, multiply(power(T_MATRIX, -quotient), matrix))
    return t_word(quotient) + ("s",) + decompose_sl2(reduced)


def word_product(word: Sequence[str]) -> Matrix:
    matrix = IDENTITY
    for generator in word:
        matrix = multiply(matrix, S_MATRIX if generator == "s" else R_MATRIX)
    return matrix


def schreier_chain(matrix: Matrix, arcs: Sequence[Arc]) -> tuple[int, ...]:
    word = decompose_sl2(matrix)
    product = word_product(word)
    if product not in (matrix, tuple(-value for value in matrix)):
        raise AssertionError("PSL decomposition did not reconstruct the matrix")
    arc_index = {arc: index for index, arc in enumerate(arcs)}
    chain = [0 for _ in arcs]
    coset: Coset = (0, 1)
    for generator in word:
        chain[arc_index[(coset, generator)]] += 1
        coset = coset_action(coset, generator)
    if coset != (0, 1):
        raise ValueError("matrix is not in Gamma_0(11)")
    return tuple(chain)


def homology_coordinates(
    matrix: Matrix,
    arcs: Sequence[Arc],
    dual_basis: Sequence[Sequence[Fraction]],
) -> tuple[Fraction, ...]:
    chain = schreier_chain(matrix, arcs)
    return tuple(
        sum(Fraction(value) * coefficient for value, coefficient in zip(chain, dual))
        for dual in dual_basis
    )


def in_rational_span(
    vector: Sequence[Fraction], direction: Sequence[Fraction]
) -> bool:
    nonzero = next((index for index, value in enumerate(direction) if value), None)
    if nonzero is None:
        raise ValueError("span direction must be nonzero")
    scale = vector[nonzero] / direction[nonzero]
    return all(left == scale * right for left, right in zip(vector, direction))


def add_coordinates(
    left: Sequence[Fraction], right: Sequence[Fraction]
) -> tuple[Fraction, ...]:
    return tuple(a + b for a, b in zip(left, right))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def coordinate_text(values: Sequence[Fraction]) -> str:
    return "|".join(fraction_text(value) for value in values)


def conjugate_owner(matrix: Matrix) -> Matrix:
    """Matrix action induced by the real structure z -> -conjugate(z)."""

    a, b, c, d = matrix
    return (a, -b, -c, d)


def exact_cycle_of_degree(word: str, degree: int) -> tuple[list[str], Matrix]:
    source = ROUND2.matrix_from_word(word)
    representatives = ROUND4.hecke_representatives(HECKE_PRIME)
    representative_map = dict(representatives)
    ordered_ids = [branch_id for branch_id, _ in representatives]
    cycles = ROUND4.permutation_cycles(
        ROUND4.right_action_permutation(source, HECKE_PRIME), ordered_ids
    )
    selected = [cycle for cycle in cycles if len(cycle) == degree]
    if len(selected) != 1:
        raise ValueError(f"expected one degree-{degree} cycle for {word}")
    cycle = selected[0]
    branch = representative_map[cycle[0]]
    owner = ROUND4.integral_matrix(
        ROUND4.multiply(
            ROUND4.multiply(branch, ROUND2.matrix_power(source, len(cycle))),
            ROUND4.rational_inverse(branch),
        )
    )
    return cycle, owner


def exact_degree_five_cycle(word: str) -> tuple[list[str], Matrix]:
    return exact_cycle_of_degree(word, HECKE_PRIME)


def source_maps(
    cycle_rows: Sequence[dict[str, str]], moment_rows: Sequence[dict[str, str]]
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    cycles = {
        row["word"]: row
        for row in cycle_rows
        if row["word"] in FROZEN_WORDS
        and int(row["hecke_prime"]) == HECKE_PRIME
        and int(row["cycle_degree"]) == HECKE_PRIME
    }
    moments = {
        row["word"]: row
        for row in moment_rows
        if row["word"] in FROZEN_WORDS
        and int(row["hecke_prime"]) == HECKE_PRIME
        and int(row["hecke_cycle_degree_d"]) == HECKE_PRIME
    }
    if set(cycles) != set(FROZEN_WORDS) or set(moments) != set(FROZEN_WORDS):
        raise ValueError("frozen survivor rows are incomplete")
    return cycles, moments


def build_classification_rows(
    cycle_rows: Sequence[dict[str, str]], moment_rows: Sequence[dict[str, str]]
) -> tuple[list[dict[str, object]], dict[str, object]]:
    arcs, relations = relation_matrix()
    _, pivots = rref(relations)
    dual_basis = nullspace_basis(relations)
    if len(arcs) != 24 or len(pivots) != 21 or len(dual_basis) != 3:
        raise AssertionError("unexpected Gamma_0(11) Schreier homology dimensions")

    cusp_coordinates = homology_coordinates(T_MATRIX, arcs, dual_basis)
    cycles, moments = source_maps(cycle_rows, moment_rows)
    coefficients = ROUND2.level11_eta_product_coefficients(HECKE_PRIME)
    if coefficients[HECKE_PRIME] != 1:
        raise AssertionError("frozen eta-product has unexpected a_5")

    output: list[dict[str, object]] = []
    for word in FROZEN_WORDS:
        cycle, owner = exact_degree_five_cycle(word)
        degree_one_cycle, degree_one_owner = exact_cycle_of_degree(word, 1)
        source_owner = ROUND2.matrix_from_word(word)
        source_row = cycles[word]
        moment_row = moments[word]
        if parse_matrix(source_row["cycle_owner_matrix"]) != owner:
            raise ValueError(f"Round-4 owner mismatch for {word}")

        coordinates = homology_coordinates(owner, arcs, dual_basis)
        star_owner = conjugate_owner(owner)
        star_coordinates = homology_coordinates(star_owner, arcs, dual_basis)
        compact_zero = in_rational_span(coordinates, cusp_coordinates)
        star_is_negative = in_rational_span(
            add_coordinates(star_coordinates, coordinates), cusp_coordinates
        )
        real_projection_zero = compact_zero or star_is_negative
        source_plus = add_coordinates(
            homology_coordinates(source_owner, arcs, dual_basis),
            homology_coordinates(conjugate_owner(source_owner), arcs, dual_basis),
        )
        degree_one_plus = add_coordinates(
            homology_coordinates(degree_one_owner, arcs, dual_basis),
            homology_coordinates(
                conjugate_owner(degree_one_owner), arcs, dual_basis
            ),
        )
        degree_one_real_equal = in_rational_span(
            tuple(
                output_value - source_value
                for output_value, source_value in zip(degree_one_plus, source_plus)
            ),
            cusp_coordinates,
        )
        exact_group_survivor = real_projection_zero and degree_one_real_equal

        if compact_zero:
            classification = "EXACT_SOURCE_KERNEL"
            period_character = "EXACT_ZERO_IN_COMPACT_HOMOLOGY"
        elif star_is_negative:
            classification = "EXACT_REAL_PROJECTION_KERNEL_NONZERO_FULL_PERIOD"
            period_character = "PURELY_IMAGINARY_AND_NONZERO"
        else:
            classification = "FLOATING_QUADRATURE_ARTIFACT"
            period_character = "REAL_PROJECTION_EXACTLY_NONZERO"

        numerical_survivor = (
            abs(float(source_row["period_real"])) <= NUMERICAL_TOLERANCE
            and float(moment_row["quadratic_alpha_moment_Q_d"])
            <= NUMERICAL_TOLERANCE
        )
        output.append(
            {
                "word": word,
                "hecke_prime": HECKE_PRIME,
                "a_p": coefficients[HECKE_PRIME],
                "cycle_id": source_row["cycle_id"],
                "cycle_degree": len(cycle),
                "cycle_branches": "|".join(cycle),
                "source_word_matrix": format_matrix(source_owner),
                "source_plus_homology_coordinates": coordinate_text(source_plus),
                "degree_one_cycle_branches": "|".join(degree_one_cycle),
                "degree_one_owner_matrix": format_matrix(degree_one_owner),
                "degree_one_plus_homology_coordinates": coordinate_text(
                    degree_one_plus
                ),
                "degree_one_real_projection_equal_exact": str(
                    degree_one_real_equal
                ).lower(),
                "cycle_owner_matrix": format_matrix(owner),
                "owner_determinant": determinant(owner),
                "owner_c_mod_11": owner[2] % LEVEL,
                "psl_word_length": len(decompose_sl2(owner)),
                "homology_coordinates_y0_11": coordinate_text(coordinates),
                "cusp_parabolic_coordinates": coordinate_text(cusp_coordinates),
                "compact_homology_zero_exact": str(compact_zero).lower(),
                "conjugate_owner_matrix": format_matrix(star_owner),
                "conjugate_homology_coordinates_y0_11": coordinate_text(
                    star_coordinates
                ),
                "conjugation_is_negative_mod_cusp_exact": str(
                    star_is_negative
                ).lower(),
                "real_projection_zero_exact": str(real_projection_zero).lower(),
                "full_complex_period_zero_exact": str(compact_zero).lower(),
                "exact_period_character": period_character,
                "round4_period_real": source_row["period_real"],
                "round4_period_imag": source_row["period_imag"],
                "round6_degree5_quadratic_real_moment": moment_row[
                    "quadratic_alpha_moment_Q_d"
                ],
                "round6_numerical_survivor": str(numerical_survivor).lower(),
                "exact_lambda_a_p_squared_group_moment_survivor": str(
                    exact_group_survivor
                ).lower(),
                "exact_classification": classification,
                "proof_evidence_token": "PROVED",
                "quadrature_evidence_token": "NUMERICAL_OBSERVATION",
                "target_data_used": "false",
                "formal_a2_evaluation_run": "false",
                "route_b_invocation_allowed": "false",
            }
        )

    model = {
        "presentation": "PSL(2,Z)=<s,r | s^2=r^3=1>",
        "right_coset_model": "Gamma_0(11)\\PSL(2,Z)=P^1(F_11)",
        "right_cosets": len(schreier_transversal()[0]),
        "schreier_arcs": len(arcs),
        "schreier_tree_arcs": len(schreier_transversal()[1]),
        "relation_matrix_rows": len(relations),
        "relation_matrix_rank_over_q": len(pivots),
        "homology_dimension_y0_11_over_q": len(dual_basis),
        "cusp_parabolic_coordinates": coordinate_text(cusp_coordinates),
        "compact_homology_dimension_x0_11_over_q": 2,
        "real_structure": "z -> -conjugate(z)",
        "real_period_rule": (
            "star[class]=-[class] modulo the cusp direction implies the "
            "2*pi*i*f(z)dz period is purely imaginary"
        ),
        "full_kernel_rule": (
            "the period is zero iff the class is zero in H_1(X_0(11),Q); "
            "injectivity uses genus one"
        ),
    }
    return output, model


def validate_rows(rows: Sequence[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    if len(rows) != len(FROZEN_WORDS):
        errors.append("expected four classification rows")
    if tuple(row["word"] for row in rows) != FROZEN_WORDS:
        errors.append("frozen survivor order changed")
    if any(row["owner_determinant"] != 1 for row in rows):
        errors.append("owner determinant failure")
    if any(row["owner_c_mod_11"] != 0 for row in rows):
        errors.append("owner subgroup failure")
    if any(row["round6_numerical_survivor"] != "true" for row in rows):
        errors.append("a frozen Round-6 survivor no longer passes its numerical audit")
    if any(row["real_projection_zero_exact"] != "true" for row in rows):
        errors.append("a frozen real-projection kernel was not certified exactly")
    if any(
        row["degree_one_real_projection_equal_exact"] != "true" for row in rows
    ):
        errors.append("a degree-one real-period identity was not certified exactly")
    if any(
        row["exact_lambda_a_p_squared_group_moment_survivor"] != "true"
        for row in rows
    ):
        errors.append("a full finite a_p-squared moment survivor was not exact")
    classifications = [str(row["exact_classification"]) for row in rows]
    if classifications.count("EXACT_SOURCE_KERNEL") != 2:
        errors.append("expected two full source kernels")
    if classifications.count(
        "EXACT_REAL_PROJECTION_KERNEL_NONZERO_FULL_PERIOD"
    ) != 2:
        errors.append("expected two nonzero purely imaginary periods")
    if any(row["target_data_used"] != "false" for row in rows):
        errors.append("target-data prohibition failed")
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

    errors: list[str] = []
    if sha256(args.round4_cycle_ledger) != EXPECTED_ROUND4_CYCLE_SHA256:
        errors.append("Round-4 cycle-ledger SHA-256 mismatch")
    if sha256(args.round6_moment_ledger) != EXPECTED_ROUND6_MOMENT_SHA256:
        errors.append("Round-6 moment-ledger SHA-256 mismatch")
    cycle_rows = read_csv(args.round4_cycle_ledger)
    moment_rows = read_csv(args.round6_moment_ledger)
    rows, homology_model = build_classification_rows(cycle_rows, moment_rows)
    errors.extend(validate_rows(rows))
    if errors:
        raise SystemExit("; ".join(errors))

    args.output.mkdir(parents=True, exist_ok=True)
    ledger_path = args.output / "round7_exact_survivor_classification_ledger.csv"
    model_path = args.output / "round7_exact_homology_model.json"
    summary_path = args.output / "round7_summary.json"
    manifest_path = args.output / "round7_artifact_manifest.json"

    write_csv(ledger_path, rows, CLASSIFICATION_FIELDS)
    model_path.write_text(
        json.dumps(homology_model, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    full_kernels = [
        str(row["word"])
        for row in rows
        if row["exact_classification"] == "EXACT_SOURCE_KERNEL"
    ]
    projection_only = [
        str(row["word"])
        for row in rows
        if row["exact_classification"]
        == "EXACT_REAL_PROJECTION_KERNEL_NONZERO_FULL_PERIOD"
    ]
    summary = {
        "schema": "p26-round7-exact-survivor-summary/1.0",
        "date": DATE,
        "classification": "EXACT_TARGET_FREE_GAMMA0_11_HOMOLOGY_AUDIT",
        "frozen_survivors": len(rows),
        "exactly_classified": len(rows),
        "exact_lambda_a_p_squared_group_moment_survivors": len(rows),
        "exact_full_source_kernels": len(full_kernels),
        "exact_full_source_kernel_words": full_kernels,
        "exact_real_projection_only_kernels": len(projection_only),
        "exact_real_projection_only_kernel_words": projection_only,
        "floating_quadrature_artifacts": 0,
        "unresolved_fail_closed": 0,
        "theorem": {
            "status": "PROVED",
            "statement": (
                "All four Round-6 p=5 survivors are exact kernels of the "
                "real-period projection, and their degree-one output real "
                "period equals the base real period: two degree-five classes "
                "vanish in compact homology and two are nonzero anti-invariant "
                "classes with purely imaginary newform periods."
            ),
            "numerical_smallness_used_as_proof": False,
        },
        "homology_model": homology_model,
        "source_bindings": {
            "round4_cycle_ledger_sha256": sha256(args.round4_cycle_ledger),
            "round6_moment_ledger_sha256": sha256(args.round6_moment_ledger),
        },
        "claim_boundary": {
            "ars_stage": "STAGE_1_RESEARCH",
            "proposal_stage": "STAGE_1_ROUTE_A_A0_A1",
            "formal_route_a_tuple": FORMAL_TUPLE,
            "overall_route_a_status": "ROUTE_A_EXPLORATORY",
            "local_four_survivor_classification_only": True,
            "complete_gamma0_11_primitive_enumeration": False,
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
            "extend the exact Schreier-homology/real-structure classifier from "
            "the four survivors to all 138 Round-4 cycle-owner instances and "
            "replace the 55-group numerical real-moment verdicts by exact "
            "integer-coefficient moment identities"
        ),
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    source_paths = (
        Path(__file__),
        Path(__file__).with_name("test_round7_exact_survivors.py"),
        PROJECT_DIR / "experiments" / "reproduce_round7.sh",
        PROJECT_DIR / "notes" / "round7_survivor_classification_freeze.md",
        args.round4_cycle_ledger,
        args.round6_moment_ledger,
    )
    artifact_paths = (ledger_path, model_path, summary_path)
    manifest = {
        "schema": "p26-round7-artifact-manifest/1.0",
        "date": DATE,
        "classification": "EXACT_TARGET_FREE_GAMMA0_11_HOMOLOGY_AUDIT",
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
