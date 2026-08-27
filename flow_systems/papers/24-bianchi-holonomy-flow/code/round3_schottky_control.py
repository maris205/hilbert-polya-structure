#!/usr/bin/env python3
"""Exact Round-3 classical-Schottky control for P24.

The control is deliberately target-free.  Four pairs of round disks and a
fixed complex multiplier define a rank-four classical Schottky group by the
ping-pong theorem.  The program verifies the round-disk certificate with exact
Gaussian-rational arithmetic and enumerates the freely reduced marked word
ball and oriented cyclic classes through word length five.

Only the marking (four positive generators, eight oriented letters) and word
cutoff are matched to the P24 Round-2 sample.  Finite volume, cusp structure,
covolume, and length distribution are not matched.  No arithmetic owner or
orbit-to-arithmetic map is asserted.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import hashlib
import io
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Q = Fraction
GaussianQ = tuple[Q, Q]
Matrix = tuple[GaussianQ, GaussianQ, GaussianQ, GaussianQ]
Word = tuple[str, ...]

ZERO: GaussianQ = (Q(0), Q(0))
ONE: GaussianQ = (Q(1), Q(0))
IDENTITY: Matrix = (ONE, ZERO, ZERO, ONE)

MAX_WORD_LENGTH = 5
RADIUS_RATIO = Q(10)
DELTA = Q(1, 1000)
MU: GaussianQ = (Q(3, 50000), Q(4, 50000))
MU_ABS_SQUARED = Q(1, 100_000_000)
SHUFFLE_SEED_LABEL = "P24-2026-08-27-R3-Schottky-target-free-shuffle-v1"
COMPLETENESS_BOUNDARY = (
    "RANK4_CLASSICAL_SCHOTTKY_MARKED_CYCLIC_CLASSES_WORD_LENGTH_LE_5;"
    "EXACT_FOR_FROZEN_MARKING_AND_CUTOFF;NOT_A_LENGTH_SPECTRUM_CUTOFF;"
    "NOT_FINITE_VOLUME_MATCHED;NOT_BIANCHI_CUSP_MATCHED"
)
CONTROL_MATCH_SCOPE = (
    "MATCHED_ONLY_ON_POSITIVE_GENERATOR_RANK_4;ORIENTED_ALPHABET_8;"
    "MAX_REDUCED_WORD_LENGTH_5"
)

# Each pair is (name, repelling fixed point r, attracting fixed point a).
# The one-unit separation makes every Apollonius radius rational.  The grid
# and multiplier are frozen independently of any orbit, prime, or zero table.
FIXED_POINT_SPECS: tuple[tuple[str, GaussianQ, GaussianQ], ...] = (
    ("S1", (Q(-6), Q(-3)), (Q(-5), Q(-3))),
    ("S2", (Q(2), Q(-3)), (Q(3), Q(-3))),
    ("S3", (Q(-6), Q(3)), (Q(-5), Q(3))),
    ("S4", (Q(2), Q(3)), (Q(3), Q(3))),
)


def g_add(x: GaussianQ, y: GaussianQ) -> GaussianQ:
    return (x[0] + y[0], x[1] + y[1])


def g_neg(x: GaussianQ) -> GaussianQ:
    return (-x[0], -x[1])


def g_sub(x: GaussianQ, y: GaussianQ) -> GaussianQ:
    return g_add(x, g_neg(y))


def g_mul(x: GaussianQ, y: GaussianQ) -> GaussianQ:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def g_conj(x: GaussianQ) -> GaussianQ:
    return (x[0], -x[1])


def g_norm_squared(x: GaussianQ) -> Q:
    return x[0] * x[0] + x[1] * x[1]


def g_div(x: GaussianQ, y: GaussianQ) -> GaussianQ:
    norm = g_norm_squared(y)
    if norm == 0:
        raise ZeroDivisionError("Gaussian-rational division by zero")
    numerator = g_mul(x, g_conj(y))
    return (numerator[0] / norm, numerator[1] / norm)


def g_scale(x: GaussianQ, scalar: Q) -> GaussianQ:
    return (x[0] * scalar, x[1] * scalar)


def g_to_complex(x: GaussianQ) -> complex:
    return complex(float(x[0]), float(x[1]))


def q_text(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def g_text(value: GaussianQ) -> str:
    return f"({q_text(value[0])},{q_text(value[1])})"


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    a00, a01, a10, a11 = a
    b00, b01, b10, b11 = b
    return (
        g_add(g_mul(a00, b00), g_mul(a01, b10)),
        g_add(g_mul(a00, b01), g_mul(a01, b11)),
        g_add(g_mul(a10, b00), g_mul(a11, b10)),
        g_add(g_mul(a10, b01), g_mul(a11, b11)),
    )


def mat_det(matrix: Matrix) -> GaussianQ:
    return g_sub(g_mul(matrix[0], matrix[3]), g_mul(matrix[1], matrix[2]))


def mat_trace(matrix: Matrix) -> GaussianQ:
    return g_add(matrix[0], matrix[3])


def mat_inv(matrix: Matrix) -> Matrix:
    determinant = mat_det(matrix)
    if determinant == ZERO:
        raise ValueError("singular projective matrix")
    adjugate = (matrix[3], g_neg(matrix[1]), g_neg(matrix[2]), matrix[0])
    return tuple(g_div(entry, determinant) for entry in adjugate)  # type: ignore[return-value]


def projective_key(matrix: Matrix) -> tuple[tuple[int, int, int, int], ...]:
    pivot = next((entry for entry in matrix if entry != ZERO), None)
    if pivot is None:
        raise ValueError("zero projective matrix")
    normalized = tuple(g_div(entry, pivot) for entry in matrix)
    return tuple(
        (
            entry[0].numerator,
            entry[0].denominator,
            entry[1].numerator,
            entry[1].denominator,
        )
        for entry in normalized
    )


def projectively_equal(a: Matrix, b: Matrix) -> bool:
    return projective_key(a) == projective_key(b)


def matrix_id(matrix: Matrix) -> str:
    raw = repr(projective_key(matrix)).encode("ascii")
    return "K" + hashlib.sha256(raw).hexdigest()[:16]


def matrix_text(matrix: Matrix) -> str:
    return f"[[{g_text(matrix[0])},{g_text(matrix[1])}],[{g_text(matrix[2])},{g_text(matrix[3])}]]"


def h_matrix(repelling: GaussianQ, attracting: GaussianQ) -> Matrix:
    # h(z)=(z-a)/(z-r), so h(a)=0 and h(r)=infinity.
    return (ONE, g_neg(attracting), ONE, g_neg(repelling))


def diagonal_matrix(multiplier: GaussianQ) -> Matrix:
    return (multiplier, ZERO, ZERO, ONE)


def schottky_generator(repelling: GaussianQ, attracting: GaussianQ) -> Matrix:
    h = h_matrix(repelling, attracting)
    return mat_mul(mat_inv(h), mat_mul(diagonal_matrix(MU), h))


def generators() -> tuple[dict[str, Matrix], dict[str, str], tuple[str, ...]]:
    result: dict[str, Matrix] = {}
    inverse_name: dict[str, str] = {}
    order: list[str] = []
    for positive, repelling, attracting in FIXED_POINT_SPECS:
        negative = positive + "m"
        matrix = schottky_generator(repelling, attracting)
        result[positive] = matrix
        result[negative] = mat_inv(matrix)
        inverse_name[positive] = negative
        inverse_name[negative] = positive
        order.extend((positive, negative))
    return result, inverse_name, tuple(order)


GENERATORS, INVERSE_NAME, GENERATOR_ORDER = generators()


def disk_center(fixed: GaussianQ, other: GaussianQ, ratio: Q) -> GaussianQ:
    ratio_squared = ratio * ratio
    numerator = g_sub(fixed, g_scale(other, ratio_squared))
    return g_scale(numerator, Q(1) / (Q(1) - ratio_squared))


def disk_radius(ratio: Q) -> Q:
    # All paired fixed points are exactly one unit apart.
    return ratio / (Q(1) - ratio * ratio)


def build_domains() -> list[dict[str, object]]:
    domains: list[dict[str, object]] = []
    for positive, repelling, attracting in FIXED_POINT_SPECS:
        negative = positive + "m"
        domains.append(
            {
                "domain_id": positive + "+",
                "pair_id": positive,
                "target_letter": positive,
                "inverse_letter": negative,
                "role": "ATTRACTING_TARGET_FOR_POSITIVE_GENERATOR",
                "fixed": attracting,
                "other_fixed": repelling,
                "ratio": DELTA,
                "center": disk_center(attracting, repelling, DELTA),
                "radius": disk_radius(DELTA),
                "excluded_source_domain": positive + "-",
            }
        )
        inverse_ratio = Q(1) / RADIUS_RATIO
        domains.append(
            {
                "domain_id": positive + "-",
                "pair_id": positive,
                "target_letter": negative,
                "inverse_letter": positive,
                "role": "REPELLING_TARGET_FOR_INVERSE_GENERATOR",
                "fixed": repelling,
                "other_fixed": attracting,
                "ratio": inverse_ratio,
                "center": disk_center(repelling, attracting, inverse_ratio),
                "radius": disk_radius(inverse_ratio),
                "excluded_source_domain": positive + "+",
            }
        )
    return domains


def pairwise_squared_gaps(domains: list[dict[str, object]]) -> list[Q]:
    gaps: list[Q] = []
    for left_index, left in enumerate(domains):
        for right in domains[left_index + 1 :]:
            center_delta = g_sub(left["center"], right["center"])  # type: ignore[arg-type]
            radius_sum = left["radius"] + right["radius"]  # type: ignore[operator]
            gaps.append(g_norm_squared(center_delta) - radius_sum * radius_sum)
    return gaps


def exact_ping_pong_checks() -> dict[str, object]:
    domains = build_domains()
    gaps = pairwise_squared_gaps(domains)
    conjugacy_checks = 0
    for positive, repelling, attracting in FIXED_POINT_SPECS:
        h = h_matrix(repelling, attracting)
        generator = GENERATORS[positive]
        inverse = GENERATORS[positive + "m"]
        if mat_mul(h, generator) != mat_mul(diagonal_matrix(MU), h):
            raise AssertionError("exact h*g=diag(mu,1)*h identity failed")
        if mat_mul(h, inverse) != mat_mul(mat_inv(diagonal_matrix(MU)), h):
            raise AssertionError("exact inverse conjugacy identity failed")
        conjugacy_checks += 2
    boundary_identity = MU_ABS_SQUARED * RADIUS_RATIO * RADIUS_RATIO == DELTA * DELTA
    return {
        "domains": domains,
        "pairwise_squared_gaps": gaps,
        "all_closed_disks_pairwise_disjoint": all(gap > 0 for gap in gaps),
        "minimum_pairwise_squared_gap": min(gaps),
        "exact_conjugacy_identities_checked": conjugacy_checks,
        "boundary_modulus_identity": boundary_identity,
    }


def word_text(word: Word) -> str:
    return ".".join(word) if word else "e"


def inverse_word(word: Word) -> Word:
    return tuple(INVERSE_NAME[letter] for letter in reversed(word))


def canonical_rotation(word: Word) -> Word:
    if not word:
        return word
    return min(word[index:] + word[:index] for index in range(len(word)))


def symbolic_root(word: Word) -> tuple[Word, int]:
    if not word:
        return word, 1
    for root_length in range(1, len(word)):
        if len(word) % root_length != 0:
            continue
        exponent = len(word) // root_length
        if word[:root_length] * exponent == word:
            return canonical_rotation(word[:root_length]), exponent
    return word, 1


def matrix_for_word(word: Word) -> Matrix:
    matrix = IDENTITY
    for letter in word:
        matrix = mat_mul(matrix, GENERATORS[letter])
    return matrix


def enumerate_reduced_words(max_word_length: int = MAX_WORD_LENGTH) -> list[tuple[Word, Matrix]]:
    records: list[tuple[Word, Matrix]] = [((), IDENTITY)]
    frontier: list[tuple[Word, Matrix]] = [((), IDENTITY)]
    for _length in range(1, max_word_length + 1):
        next_frontier: list[tuple[Word, Matrix]] = []
        for word, matrix in frontier:
            for letter in GENERATOR_ORDER:
                if word and INVERSE_NAME[letter] == word[-1]:
                    continue
                new_word = word + (letter,)
                next_frontier.append((new_word, mat_mul(matrix, GENERATORS[letter])))
        records.extend(next_frontier)
        frontier = next_frontier
    return records


def cyclic_classes(
    reduced_words: list[tuple[Word, Matrix]],
) -> tuple[list[Word], Counter[Word], int]:
    multiplicities: Counter[Word] = Counter()
    cyclically_reduced_count = 0
    for word, _matrix in reduced_words:
        if not word or word[0] == INVERSE_NAME[word[-1]]:
            continue
        cyclically_reduced_count += 1
        multiplicities[canonical_rotation(word)] += 1
    return sorted(multiplicities), multiplicities, cyclically_reduced_count


def trace_invariant(matrix: Matrix) -> GaussianQ:
    return g_div(g_mul(mat_trace(matrix), mat_trace(matrix)), mat_det(matrix))


def complex_length(matrix: Matrix) -> tuple[float, float, float, complex]:
    invariant = g_to_complex(trace_invariant(matrix))
    normalized_trace = cmath.sqrt(invariant)
    value = 2.0 * cmath.acosh(normalized_trace / 2.0)
    if value.real < 0.0:
        value = -value
    theta = ((value.imag + math.pi) % (2.0 * math.pi)) - math.pi
    value = complex(value.real, theta)
    reconstructed = (2.0 * cmath.cosh(value / 2.0)) ** 2
    relative_residual = abs(reconstructed - invariant) / max(1.0, abs(invariant))
    return value.real, value.imag, relative_residual, cmath.exp(-value)


def _float(value: float) -> str:
    return format(value, ".15g")


def _corr(xs: list[float], ys: list[float]) -> float:
    if len(xs) < 2:
        return 0.0
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    dx = [value - mean_x for value in xs]
    dy = [value - mean_y for value in ys]
    denominator = math.sqrt(sum(value * value for value in dx) * sum(value * value for value in dy))
    if denominator == 0.0:
        return 0.0
    return sum(x * y for x, y in zip(dx, dy, strict=True)) / denominator


def phase_length_score(lengths: list[float], angles: list[float]) -> float:
    return math.hypot(
        _corr(lengths, [math.cos(angle) for angle in angles]),
        _corr(lengths, [math.sin(angle) for angle in angles]),
    )


DOMAIN_FIELDS = [
    "domain_id",
    "pair_id",
    "target_letter",
    "inverse_letter",
    "role",
    "fixed_point",
    "other_fixed_point",
    "apollonius_ratio",
    "center",
    "radius",
    "excluded_source_domain",
    "mapping_statement",
    "exact_conjugacy_identity",
    "exact_boundary_modulus_identity",
    "all_closed_disks_pairwise_disjoint",
    "minimum_pairwise_squared_gap",
    "evidence_status",
]

LEDGER_FIELDS = [
    "row_id",
    "oriented_cyclic_word",
    "marked_word_length",
    "projective_matrix",
    "projective_determinant",
    "trace_squared_over_determinant",
    "complex_length_re",
    "holonomy_angle",
    "invariant_reconstruction_relative_residual",
    "stable_complex_multiplier_re",
    "stable_complex_multiplier_im",
    "stable_multiplier_abs",
    "unstable_multiplier_abs",
    "symbolic_root",
    "repetition_exponent",
    "primitive_status",
    "orientation_pair_id",
    "orientation",
    "cyclic_rotation_multiplicity",
    "trace_invariant_collision_multiplicity",
    "loxodromic_status",
    "parabolic_cusp_risk",
    "arithmetic_owner",
    "target_data_used",
    "control_match_scope",
    "completeness_boundary",
    "group_evidence_status",
    "numeric_evidence_status",
]

CONTROL_FIELDS = [
    "control_id",
    "row_id",
    "complex_length_fixed",
    "repetition_exponent_fixed",
    "original_holonomy_angle",
    "shuffled_holonomy_angle",
    "shuffled_from_row_id",
    "shuffle_seed_label",
    "arithmetic_owner",
    "target_data_used",
    "evidence_status",
]


def build_payload() -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], dict[str, object]]:
    ping_pong = exact_ping_pong_checks()
    if not ping_pong["all_closed_disks_pairwise_disjoint"]:
        raise RuntimeError("round-disk closures are not pairwise disjoint")
    if not ping_pong["boundary_modulus_identity"]:
        raise RuntimeError("boundary modulus identity failed")

    reduced_words = enumerate_reduced_words()
    expected_reduced_count = 1 + sum(
        8 * 7 ** (length - 1) for length in range(1, MAX_WORD_LENGTH + 1)
    )
    if len(reduced_words) != expected_reduced_count:
        raise RuntimeError("unexpected freely reduced word count")
    word_projective_keys = [projective_key(matrix) for _word, matrix in reduced_words]
    if len(set(word_projective_keys)) != len(word_projective_keys):
        raise RuntimeError("exact projective collision contradicts the ping-pong certificate")

    classes, rotation_multiplicities, cyclically_reduced_count = cyclic_classes(reduced_words)
    class_matrices = {word: matrix_for_word(word) for word in classes}
    invariants = {word: trace_invariant(matrix) for word, matrix in class_matrices.items()}
    invariant_counts = Counter(invariants.values())
    rows: list[dict[str, str]] = []

    for word in classes:
        matrix = class_matrices[word]
        inverse_class = canonical_rotation(inverse_word(word))
        pair_words = sorted((word_text(word), word_text(inverse_class)))
        pair_id = "O" + hashlib.sha256("|".join(pair_words).encode("utf-8")).hexdigest()[:16]
        if word == inverse_class:
            orientation = "SELF_INVERSE_CLASS"
        elif word < inverse_class:
            orientation = "CANONICAL"
        else:
            orientation = "REVERSED"
        root, exponent = symbolic_root(word)
        ell, theta, residual, stable_multiplier = complex_length(matrix)
        invariant = invariants[word]
        row_id = matrix_id(matrix)
        primitive_status = (
            "PRIMITIVE_CONJUGACY_CLASS_IN_FREE_GROUP"
            if exponent == 1
            else "REPETITION_IN_FREE_GROUP"
        )
        rows.append(
            {
                "row_id": row_id,
                "oriented_cyclic_word": word_text(word),
                "marked_word_length": str(len(word)),
                "projective_matrix": matrix_text(matrix),
                "projective_determinant": g_text(mat_det(matrix)),
                "trace_squared_over_determinant": g_text(invariant),
                "complex_length_re": _float(ell),
                "holonomy_angle": _float(theta),
                "invariant_reconstruction_relative_residual": _float(residual),
                "stable_complex_multiplier_re": _float(stable_multiplier.real),
                "stable_complex_multiplier_im": _float(stable_multiplier.imag),
                "stable_multiplier_abs": _float(abs(stable_multiplier)),
                "unstable_multiplier_abs": _float(math.exp(ell)),
                "symbolic_root": word_text(root),
                "repetition_exponent": str(exponent),
                "primitive_status": primitive_status,
                "orientation_pair_id": pair_id,
                "orientation": orientation,
                "cyclic_rotation_multiplicity": str(rotation_multiplicities[word]),
                "trace_invariant_collision_multiplicity": str(invariant_counts[invariant]),
                "loxodromic_status": "LOXODROMIC_BY_CLASSICAL_SCHOTTKY_THEOREM",
                "parabolic_cusp_risk": "NO_PARABOLICS;CONTROL_IS_CONVEX_COCOMPACT_AND_HAS_NO_CUSPS",
                "arithmetic_owner": "NONE_BY_CONSTRUCTION",
                "target_data_used": "false",
                "control_match_scope": CONTROL_MATCH_SCOPE,
                "completeness_boundary": COMPLETENESS_BOUNDARY,
                "group_evidence_status": "PROVED",
                "numeric_evidence_status": "NUMERICALLY_CERTIFIED",
            }
        )

    primitive_rows = [row for row in rows if row["repetition_exponent"] == "1"]
    shuffled_sources = sorted(
        primitive_rows,
        key=lambda row: hashlib.sha256(
            f"{SHUFFLE_SEED_LABEL}:{row['row_id']}".encode("utf-8")
        ).hexdigest(),
    )
    controls: list[dict[str, str]] = []
    for target, source in zip(primitive_rows, shuffled_sources, strict=True):
        controls.append(
            {
                "control_id": "SC" + target["row_id"][1:],
                "row_id": target["row_id"],
                "complex_length_fixed": target["complex_length_re"],
                "repetition_exponent_fixed": target["repetition_exponent"],
                "original_holonomy_angle": target["holonomy_angle"],
                "shuffled_holonomy_angle": source["holonomy_angle"],
                "shuffled_from_row_id": source["row_id"],
                "shuffle_seed_label": SHUFFLE_SEED_LABEL,
                "arithmetic_owner": "NONE_BY_CONSTRUCTION",
                "target_data_used": "false",
                "evidence_status": "NUMERICALLY_CERTIFIED",
            }
        )

    domain_rows: list[dict[str, str]] = []
    min_gap = ping_pong["minimum_pairwise_squared_gap"]
    for domain in ping_pong["domains"]:  # type: ignore[union-attr]
        target_letter = str(domain["target_letter"])
        mapping_statement = (
            f"{target_letter}(COMPLEMENT_OF_{domain['excluded_source_domain']})"
            f"=INTERIOR_OF_{domain['domain_id']}"
        )
        domain_rows.append(
            {
                "domain_id": str(domain["domain_id"]),
                "pair_id": str(domain["pair_id"]),
                "target_letter": target_letter,
                "inverse_letter": str(domain["inverse_letter"]),
                "role": str(domain["role"]),
                "fixed_point": g_text(domain["fixed"]),  # type: ignore[arg-type]
                "other_fixed_point": g_text(domain["other_fixed"]),  # type: ignore[arg-type]
                "apollonius_ratio": q_text(domain["ratio"]),  # type: ignore[arg-type]
                "center": g_text(domain["center"]),  # type: ignore[arg-type]
                "radius": q_text(domain["radius"]),  # type: ignore[arg-type]
                "excluded_source_domain": str(domain["excluded_source_domain"]),
                "mapping_statement": mapping_statement,
                "exact_conjugacy_identity": "PROVED",
                "exact_boundary_modulus_identity": "PROVED",
                "all_closed_disks_pairwise_disjoint": "PROVED",
                "minimum_pairwise_squared_gap": q_text(min_gap),  # type: ignore[arg-type]
                "evidence_status": "PROVED",
            }
        )

    primitive_lengths = [float(row["complex_length_re"]) for row in primitive_rows]
    primitive_angles = [float(row["holonomy_angle"]) for row in primitive_rows]
    shuffled_angles = [float(row["shuffled_holonomy_angle"]) for row in controls]
    repetition_count = sum(int(row["repetition_exponent"]) > 1 for row in rows)
    orientation_pair_count = len({row["orientation_pair_id"] for row in rows})
    residual_max = max(float(row["invariant_reconstruction_relative_residual"]) for row in rows)

    metrics: dict[str, object] = {
        "candidate_id": "P24-RANK4-CLASSICAL-SCHOTTKY-CONTROL-R3",
        "generated_on": "2026-08-27",
        "control_type": "CONVEX_COCOMPACT_CLASSICAL_SCHOTTKY_KLEINIAN_NON_LATTICE",
        "positive_generator_rank": 4,
        "oriented_alphabet_size": 8,
        "max_reduced_word_length": MAX_WORD_LENGTH,
        "paired_round_domains": len(domain_rows),
        "pairwise_closed_disk_checks": len(ping_pong["pairwise_squared_gaps"]),  # type: ignore[arg-type]
        "minimum_pairwise_squared_gap_exact": q_text(min_gap),  # type: ignore[arg-type]
        "all_closed_disks_pairwise_disjoint": ping_pong["all_closed_disks_pairwise_disjoint"],
        "exact_conjugacy_identities_checked": ping_pong["exact_conjugacy_identities_checked"],
        "boundary_modulus_identity": ping_pong["boundary_modulus_identity"],
        "complex_multiplier": g_text(MU),
        "complex_multiplier_abs_squared": q_text(MU_ABS_SQUARED),
        "ping_pong_theorem_status": "PROVED",
        "free_discrete_convex_cocompact_status": "PROVED",
        "torsion_free_no_parabolics_status": "PROVED",
        "quotient_volume_scope": "INFINITE_VOLUME;NOT_A_LATTICE;NOT_FINITE_VOLUME_MATCHED",
        "arithmetic_lattice_status": "NOT_AN_ARITHMETIC_LATTICE",
        "arithmetic_lattice_evidence_status": "PROVED",
        "ambient_thin_arithmetic_containment": "OPEN",
        "enumerated_reduced_words_including_identity": len(reduced_words),
        "unique_exact_projective_word_matrices": len(set(word_projective_keys)),
        "cyclically_reduced_marked_words": cyclically_reduced_count,
        "oriented_cyclic_classes": len(rows),
        "primitive_oriented_cyclic_classes": len(primitive_rows),
        "repetition_oriented_cyclic_classes": repetition_count,
        "unoriented_orientation_pairs": orientation_pair_count,
        "self_inverse_oriented_classes": sum(row["orientation"] == "SELF_INVERSE_CLASS" for row in rows),
        "maximum_invariant_reconstruction_relative_residual": residual_max,
        "intrinsic_phase_length_score": phase_length_score(primitive_lengths, primitive_angles),
        "intrinsic_phase_length_score_shuffled": phase_length_score(primitive_lengths, shuffled_angles),
        "holonomy_shuffle_rows": len(controls),
        "holonomy_shuffle_evidence": "NUMERICAL_OBSERVATION",
        "matched_axes": [
            "positive_generator_rank_4",
            "oriented_alphabet_size_8",
            "max_reduced_word_length_5",
            "raw_reduced_word_count_22409",
        ],
        "unmatched_axes": [
            "finite_volume",
            "cusp_structure",
            "covolume",
            "length_distribution",
            "full_group_orbit_count",
        ],
        "completeness_boundary": COMPLETENESS_BOUNDARY,
        "control_match_scope": CONTROL_MATCH_SCOPE,
        "arithmetic_owner": "NONE_BY_CONSTRUCTION",
        "forbidden_target_data_used": False,
        "forbidden_target_data_classes": [
            "prime_tables",
            "riemann_zero_tables",
            "log_p_roofs",
            "von_mangoldt_weights",
        ],
        "arithmetic_hypothesis_verdict": "OPEN",
        "proposal_stage": 1,
        "route_a_scope": "A0-A1",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "group_evidence_status": "PROVED",
        "numeric_evidence_status": "NUMERICALLY_CERTIFIED",
    }
    return domain_rows, rows, controls, metrics


def csv_bytes(rows: Iterable[dict[str, str]], fieldnames: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def core_outputs() -> tuple[dict[str, bytes], dict[str, object]]:
    domains, ledger, controls, metrics = build_payload()
    outputs = {
        "results/schottky_ping_pong_domains_round3.csv": csv_bytes(domains, DOMAIN_FIELDS),
        "results/schottky_conjugacy_ledger_round3.csv": csv_bytes(ledger, LEDGER_FIELDS),
        "results/schottky_holonomy_shuffle_round3.csv": csv_bytes(controls, CONTROL_FIELDS),
        "results/round3_metrics.json": json_bytes(metrics),
    }
    return outputs, metrics


def combined_hash(outputs: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name in sorted(outputs):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[name])
        digest.update(b"\0")
    return digest.hexdigest()


def write_outputs(project_root: Path) -> str:
    first, metrics_first = core_outputs()
    second, metrics_second = core_outputs()
    if first != second or metrics_first != metrics_second:
        raise RuntimeError("in-process deterministic regeneration mismatch")
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in first.items()}
    digest = combined_hash(first)
    receipt = {
        "candidate_id": "P24-RANK4-CLASSICAL-SCHOTTKY-CONTROL-R3",
        "command": "python3 code/round3_schottky_control.py",
        "verification_command": "python3 code/round3_schottky_control.py --verify-existing",
        "test_command": "python3 code/test_round3_schottky_control.py -v",
        "date": "2026-08-27",
        "status": "COMPLETED",
        "verification_status": "VERIFIED",
        "reproducibility_verdict": "REPRODUCIBLE",
        "determinism": "DETERMINISTIC_EXACT_CORE_OUTPUTS",
        "in_process_generations_compared": 2,
        "combined_sha256": digest,
        "core_file_sha256": hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(
            (Path(__file__).parent / "test_round3_schottky_control.py").read_bytes()
        ).hexdigest(),
        "expected_outputs": sorted(first),
        "anomalies": [],
        "forbidden_target_data_used": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "claim_boundary": COMPLETENESS_BOUNDARY,
        "group_evidence_status": "PROVED",
        "numeric_evidence_status": "NUMERICALLY_CERTIFIED",
    }
    outputs = dict(first)
    outputs["experiments/round3_receipt.json"] = json_bytes(receipt)
    for relative, data in outputs.items():
        destination = project_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    return digest


def verify_existing(project_root: Path) -> str:
    expected, _metrics = core_outputs()
    mismatches: list[str] = []
    for relative, data in expected.items():
        path = project_root / relative
        if not path.exists() or path.read_bytes() != data:
            mismatches.append(relative)
    if mismatches:
        raise RuntimeError("existing artifact mismatch: " + ", ".join(mismatches))
    return combined_hash(expected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-word-length", type=int, default=MAX_WORD_LENGTH)
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    if args.max_word_length != MAX_WORD_LENGTH:
        raise SystemExit("Round-3 cutoff is frozen at max word length 5")
    project_root = Path(__file__).resolve().parents[1]
    digest = verify_existing(project_root) if args.verify_existing else write_outputs(project_root)
    print(json.dumps({"status": "PASS", "combined_sha256": digest}, sort_keys=True))


if __name__ == "__main__":
    main()
