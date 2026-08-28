#!/usr/bin/env python3
"""Build the P28 Round-5 bounded marked-cyclic Bolza census.

The census is complete only for the explicitly declared combinatorial scope:
freely and cyclically reduced words of marked length at most four, modulo
cyclic rotation and inversion.  Exact matrices are evaluated in

    Q(s,t,i),  s^2=2, t^2=1+s, i^2=-1,

which contains the source-locked Bolza matrices.  Matrix equality is checked
projectively and also modulo inversion.  This does *not* prove that distinct
marked-cyclic records are distinct Gamma-conjugacy classes.

Only marked-primitive records whose exact trace satisfies
``length < 2*Bolza_systole`` receive Gamma-primitivity and magnetic-owner
credit.  The other marked-primitive records stay candidate-only.  Signed-k
rows are emitted only for proved primitive owners, so no candidate or
orientation branch can mint owner credit.
"""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
from typing import Iterable, Sequence


DECIMAL_PRECISION = 120
DISPLAY_DIGITS = 70
WORD_CUTOFF = 4
SOURCE_K_ABSOLUTE_VALUES = (1, 2, 3, 4)
ALPHABET = (1, -1, 2, -2, 3, -3, 4, -4)

GROUP_SOURCE = (
    "Ebbens-Iordanov-Teillaud-Vegter_JoCG_2022_"
    "doi:10.20382/jocg.v13i1a5_equations_5-6_Theorem_2"
)
TRACE_SOURCE = (
    "Kordyukov-Taimanov_arXiv:2202.06055v3_"
    "Theorem_3_equations_19_and_22-23"
)

MODULE_PATH = Path(__file__).with_name("build_round4_bolza_owner_ledger.py")
SPEC = importlib.util.spec_from_file_location("p28_round4_for_round5", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load build_round4_bolza_owner_ledger.py")
ROUND4 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ROUND4
SPEC.loader.exec_module(ROUND4)


# Basis order: 1, i, t, ti, s, si, st, sti.
NF = tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]
ZERO: NF = (Fraction(0),) * 8


def nf_basis(s_power: int, t_power: int, i_power: int, coefficient: int = 1) -> NF:
    values = [Fraction(0)] * 8
    values[s_power * 4 + t_power * 2 + i_power] = Fraction(coefficient)
    return tuple(values)  # type: ignore[return-value]


ONE = nf_basis(0, 0, 0)
S = nf_basis(1, 0, 0)
T = nf_basis(0, 1, 0)
I_UNIT = nf_basis(0, 0, 1)


def nf_add(left: NF, right: NF) -> NF:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def nf_neg(value: NF) -> NF:
    return tuple(-entry for entry in value)  # type: ignore[return-value]


def nf_sub(left: NF, right: NF) -> NF:
    return nf_add(left, nf_neg(right))


def nf_mul(left: NF, right: NF) -> NF:
    """Multiply in Q(s,t,i) using the three defining relations exactly."""

    output = [Fraction(0)] * 8
    for left_index, left_coefficient in enumerate(left):
        if not left_coefficient:
            continue
        left_s = left_index // 4
        left_t = (left_index % 4) // 2
        left_i = left_index % 2
        for right_index, right_coefficient in enumerate(right):
            if not right_coefficient:
                continue
            right_s = right_index // 4
            right_t = (right_index % 4) // 2
            right_i = right_index % 2
            coefficient = left_coefficient * right_coefficient
            i_power = left_i + right_i
            if i_power == 2:
                coefficient = -coefficient
                i_power = 0
            s_power = left_s + right_s
            t_power = left_t + right_t
            branches = [(s_power, coefficient)]
            if t_power == 2:
                # t^2 = 1+s.
                branches = [(s_power, coefficient), (s_power + 1, coefficient)]
                t_power = 0
            for branch_s, branch_coefficient in branches:
                if branch_s >= 2:
                    branch_coefficient *= 2
                    branch_s -= 2
                output[branch_s * 4 + t_power * 2 + i_power] += branch_coefficient
    return tuple(output)  # type: ignore[return-value]


def nf_conjugate(value: NF) -> NF:
    return tuple(
        -coefficient if index % 2 else coefficient
        for index, coefficient in enumerate(value)
    )  # type: ignore[return-value]


def nf_scale(value: NF, coefficient: int) -> NF:
    return tuple(Fraction(coefficient) * entry for entry in value)  # type: ignore[return-value]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def nf_key(value: NF) -> tuple[str, ...]:
    return tuple(fraction_text(entry) for entry in value)


def nf_expression(value: NF) -> str:
    basis = ("1", "i", "t", "t*i", "s", "s*i", "s*t", "s*t*i")
    terms: list[str] = []
    for coefficient, symbol in zip(value, basis):
        if not coefficient:
            continue
        coefficient_text = fraction_text(coefficient)
        if symbol == "1":
            terms.append(coefficient_text)
        elif coefficient == 1:
            terms.append(symbol)
        elif coefficient == -1:
            terms.append(f"-{symbol}")
        else:
            terms.append(f"({coefficient_text})*{symbol}")
    return "+".join(terms).replace("+-", "-") if terms else "0"


def nf_decimal(value: NF) -> tuple[Decimal, Decimal]:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        sqrt2 = Decimal(2).sqrt()
        t_value = (Decimal(1) + sqrt2).sqrt()
        real = Decimal(0)
        imaginary = Decimal(0)
        for index, coefficient in enumerate(value):
            if not coefficient:
                continue
            s_power = index // 4
            t_power = (index % 4) // 2
            i_power = index % 2
            factor = (sqrt2**s_power) * (t_value**t_power)
            factor *= Decimal(coefficient.numerator) / Decimal(coefficient.denominator)
            if i_power:
                imaginary += factor
            else:
                real += factor
        return +real, +imaginary


MatrixNF = tuple[tuple[NF, NF], tuple[NF, NF]]


def matrix_identity() -> MatrixNF:
    return ((ONE, ZERO), (ZERO, ONE))


def matrix_multiply(left: MatrixNF, right: MatrixNF) -> MatrixNF:
    return tuple(
        tuple(
            nf_add(
                nf_mul(left[row][0], right[0][column]),
                nf_mul(left[row][1], right[1][column]),
            )
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_inverse_det_one(matrix: MatrixNF) -> MatrixNF:
    return (
        (matrix[1][1], nf_neg(matrix[0][1])),
        (nf_neg(matrix[1][0]), matrix[0][0]),
    )


def matrix_determinant(matrix: MatrixNF) -> NF:
    return nf_sub(nf_mul(matrix[0][0], matrix[1][1]), nf_mul(matrix[0][1], matrix[1][0]))


def matrix_trace(matrix: MatrixNF) -> NF:
    return nf_add(matrix[0][0], matrix[1][1])


def matrix_flat_key(matrix: MatrixNF) -> tuple[Fraction, ...]:
    return tuple(
        coefficient
        for row in matrix
        for entry in row
        for coefficient in entry
    )


def projective_matrix_key(matrix: MatrixNF) -> tuple[Fraction, ...]:
    direct = matrix_flat_key(matrix)
    negative = tuple(-entry for entry in direct)
    return min(direct, negative)


def inverse_paired_projective_key(matrix: MatrixNF) -> tuple[Fraction, ...]:
    return min(
        projective_matrix_key(matrix),
        projective_matrix_key(matrix_inverse_det_one(matrix)),
    )


def key_sha256(key: Iterable[Fraction]) -> str:
    payload = json.dumps([fraction_text(entry) for entry in key], separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def exact_generator_matrices() -> tuple[MatrixNF, ...]:
    a = nf_add(ONE, S)
    rho = nf_mul(S, T)
    upper_entries = (
        rho,
        nf_add(T, nf_mul(I_UNIT, T)),
        nf_mul(I_UNIT, rho),
        nf_add(nf_neg(T), nf_mul(I_UNIT, T)),
    )
    return tuple(
        ((a, upper), (nf_conjugate(upper), a))
        for upper in upper_entries
    )


EXACT_GENERATORS = exact_generator_matrices()


def letter_order(letter: int) -> int:
    return 2 * (abs(letter) - 1) + (1 if letter < 0 else 0)


def word_sort_key(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(letter_order(letter) for letter in word)


def inverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-letter for letter in reversed(word))


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_marked_inverse_pair(word: tuple[int, ...]) -> tuple[int, ...]:
    orbit = set(rotations(word)) | set(rotations(inverse_word(word)))
    return min(orbit, key=word_sort_key)


def is_freely_reduced(word: tuple[int, ...]) -> bool:
    return all(word[index] != -word[index + 1] for index in range(len(word) - 1))


def is_cyclically_reduced(word: tuple[int, ...]) -> bool:
    return is_freely_reduced(word) and word[0] != -word[-1]


def marked_root_decomposition(word: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    for root_length in range(1, len(word)):
        if len(word) % root_length:
            continue
        exponent = len(word) // root_length
        if word == word[:root_length] * exponent:
            return canonical_marked_inverse_pair(word[:root_length]), exponent
    return word, 1


def word_matrix(word: tuple[int, ...]) -> MatrixNF:
    value = matrix_identity()
    for letter in word:
        generator = EXACT_GENERATORS[abs(letter) - 1]
        if letter < 0:
            generator = matrix_inverse_det_one(generator)
        value = matrix_multiply(value, generator)
    return value


def matrix_power(matrix: MatrixNF, exponent: int) -> MatrixNF:
    if exponent < 0:
        return matrix_power(matrix_inverse_det_one(matrix), -exponent)
    value = matrix_identity()
    factor = matrix
    remaining = exponent
    while remaining:
        if remaining % 2:
            value = matrix_multiply(value, factor)
        factor = matrix_multiply(factor, factor)
        remaining //= 2
    return value


def word_text(word: tuple[int, ...]) -> str:
    return "*".join(
        f"f{abs(letter) - 1}" if letter > 0 else f"f{abs(letter) - 1}^-1"
        for letter in word
    )


def homology_vector(word: tuple[int, ...]) -> tuple[int, int, int, int]:
    values = [0, 0, 0, 0]
    for letter in word:
        values[abs(letter) - 1] += 1 if letter > 0 else -1
    return tuple(values)  # type: ignore[return-value]


def inverse_paired_homology_key(word: tuple[int, ...]) -> tuple[int, int, int, int]:
    vector = homology_vector(word)
    negative = tuple(-entry for entry in vector)
    return min(vector, negative)  # type: ignore[return-value]


def vector_text(vector: Sequence[int]) -> str:
    return "(" + ",".join(str(entry) for entry in vector) + ")"


def parse_word_text(text: str) -> tuple[int, ...]:
    letters: list[int] = []
    for token in text.split("*"):
        inverse = token.endswith("^-1")
        generator_text = token[:-3] if inverse else token
        if not generator_text.startswith("f"):
            raise ValueError(f"invalid marked-word token: {token}")
        letter = int(generator_text[1:]) + 1
        letters.append(-letter if inverse else letter)
    return tuple(letters)


def q_sqrt2_sign(value: NF) -> int:
    """Return the exact sign of a+b*sqrt(2), rejecting other basis terms."""

    if any(value[index] for index in (1, 2, 3, 5, 6, 7)):
        raise ValueError(f"not in Q(sqrt(2)): {nf_expression(value)}")
    rational = value[0]
    radical = value[4]
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if radical == 0:
        return (rational > 0) - (rational < 0)
    if rational > 0 and radical > 0:
        return 1
    if rational < 0 and radical < 0:
        return -1
    comparison = rational * rational - 2 * radical * radical
    if rational > 0:
        return 1 if comparison > 0 else -1
    return -1 if comparison > 0 else 1


def nf_abs_real_qsqrt2(value: NF) -> NF:
    return value if q_sqrt2_sign(value) >= 0 else nf_neg(value)


def decimal_string(value: Decimal, digits: int = DISPLAY_DIGITS) -> str:
    return format(value, f".{digits}g")


def translation_length_from_trace(trace: NF) -> Decimal:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        real, imaginary = nf_decimal(trace)
        if abs(imaginary) >= Decimal("1e-105"):
            raise ValueError("trace is not real at replay precision")
        x = abs(real) / Decimal(2)
        if x <= 1:
            raise ValueError("enumerated element is not hyperbolic")
        return +(Decimal(2) * (x + (x * x - Decimal(1)).sqrt()).ln())


def enumerate_marked_classes(cutoff: int = WORD_CUTOFF) -> tuple[list[dict[str, object]], dict[int, int]]:
    if cutoff != WORD_CUTOFF:
        raise ValueError(f"this source-locked artifact freezes cutoff={WORD_CUTOFF}")
    canonical_words: set[tuple[int, ...]] = set()
    raw_counts: dict[int, int] = {}
    for length in range(1, cutoff + 1):
        raw_count = 0
        for word in product(ALPHABET, repeat=length):
            if not is_cyclically_reduced(word):
                continue
            raw_count += 1
            canonical_words.add(canonical_marked_inverse_pair(word))
        raw_counts[length] = raw_count

    ordered_words = sorted(canonical_words, key=lambda word: (len(word), word_sort_key(word)))
    constants = ROUND4.bolza_constants()
    bolza_systole = constants["log_norm"]
    # 2*cosh(ell_B)=tr(f_j^2)=10+8*sqrt(2), exactly.
    primitive_trace_threshold = nf_add(nf_scale(ONE, 10), nf_scale(S, 8))

    provisional: list[dict[str, object]] = []
    direct_keys: dict[tuple[Fraction, ...], list[str]] = {}
    inverse_pair_keys: dict[tuple[Fraction, ...], list[str]] = {}
    trace_squared_keys: dict[tuple[str, ...], list[str]] = {}

    for ordinal, word in enumerate(ordered_words, start=1):
        census_id = f"B28R5-C{ordinal:04d}"
        root_word, repetition_exponent = marked_root_decomposition(word)
        matrix = word_matrix(word)
        trace = matrix_trace(matrix)
        trace_squared = nf_mul(trace, trace)
        direct_key = projective_matrix_key(matrix)
        inverse_pair_key = inverse_paired_projective_key(matrix)
        direct_keys.setdefault(direct_key, []).append(census_id)
        inverse_pair_keys.setdefault(inverse_pair_key, []).append(census_id)
        trace_squared_keys.setdefault(nf_key(trace_squared), []).append(census_id)
        geodesic_length = translation_length_from_trace(trace)
        trace_absolute_exact = nf_abs_real_qsqrt2(trace)

        homology = homology_vector(word)
        homology_axis_key = inverse_paired_homology_key(word)
        if repetition_exponent > 1:
            gamma_primitivity_status = "PROVED_GROUP_REPETITION_OF_MARKED_ROOT"
            owner_credit_status = "WITHHELD_MARKED_POWER"
            primitive_axis_owner_id = ""
            exact_primitivity_margin = "NOT_APPLICABLE"
            owner_distinctness_status = "NOT_APPLICABLE_MARKED_POWER"
        else:
            exact_margin = nf_sub(primitive_trace_threshold, trace_absolute_exact)
            if q_sqrt2_sign(exact_margin) > 0:
                gamma_primitivity_status = "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE"
                owner_credit_status = "PENDING_HOMOLOGY_AXIS_DEDUPLICATION"
                exact_primitivity_margin = nf_expression(exact_margin)
                primitive_axis_owner_id = ""
                owner_distinctness_status = "PENDING_HOMOLOGY_AXIS_DEDUPLICATION"
            else:
                gamma_primitivity_status = "NOT_ESTABLISHED_MARKED_PRIMITIVE_ONLY"
                owner_credit_status = "WITHHELD_GAMMA_PRIMITIVITY_OPEN"
                primitive_axis_owner_id = ""
                exact_primitivity_margin = nf_expression(exact_margin)
                owner_distinctness_status = "NOT_EVALUATED_GAMMA_PRIMITIVITY_OPEN"

        orbit = set(rotations(word)) | set(rotations(inverse_word(word)))
        provisional.append(
            {
                "census_id": census_id,
                "census_schema": "p28_round5_matched_marked_cyclic_census/1.0",
                "metric_control_id": "BOLZA_ARITHMETIC_CURVATURE_MINUS_1",
                "group_source_lock": GROUP_SOURCE,
                "marked_word_cutoff": cutoff,
                "alphabet_order": "f0,f0^-1,f1,f1^-1,f2,f2^-1,f3,f3^-1",
                "canonical_marked_word": word_text(word),
                "marked_length": len(word),
                "inverse_marked_word": word_text(inverse_word(word)),
                "marked_cyclic_inverse_orbit_size": len(orbit),
                "canonical_rule": "LEX_MIN_OVER_CYCLIC_ROTATIONS_AND_INVERSION",
                "marked_root_word": word_text(root_word),
                "marked_root_length": len(root_word),
                "marked_repetition_exponent": repetition_exponent,
                "marked_class_status": (
                    "MARKED_CYCLIC_PRIMITIVE_CANDIDATE"
                    if repetition_exponent == 1
                    else "MARKED_CYCLIC_POWER"
                ),
                "exact_number_field": "Q(s,t,i);s^2=2;t^2=1+s;i^2=-1",
                "exact_psl_matrix_key_sha256": key_sha256(direct_key),
                "exact_inverse_paired_psl_key_sha256": key_sha256(inverse_pair_key),
                "exact_trace": nf_expression(trace),
                "exact_trace_squared": nf_expression(trace_squared),
                "exact_trace_squared_key_sha256": hashlib.sha256(
                    json.dumps(nf_key(trace_squared), separators=(",", ":")).encode("utf-8")
                ).hexdigest(),
                "absolute_trace_decimal": decimal_string(abs(nf_decimal(trace)[0])),
                "geodesic_length_decimal": decimal_string(geodesic_length),
                "bolza_systole_ratio_decimal": decimal_string(geodesic_length / bolza_systole),
                "gamma_primitivity_status": gamma_primitivity_status,
                "gamma_primitivity_exact_margin_to_2sys": exact_primitivity_margin,
                "canonical_homology_vector": vector_text(homology),
                "inverse_paired_homology_axis_key": vector_text(homology_axis_key),
                "homology_axis_multiplicity_within_proved_set": 0,
                "owner_distinctness_status": owner_distinctness_status,
                "primitive_axis_owner_id": primitive_axis_owner_id,
                "owner_credit_status": owner_credit_status,
                "owner_counting_convention": "INVERSE_PAIRED_AXIS;NO_SIGNED_K_OR_ORIENTATION_OWNER_CREDIT",
                "marked_census_completeness": "COMPLETE_FOR_DECLARED_MARKED_CYCLIC_EQUIVALENCE_AT_LENGTH_LE_4",
                "full_gamma_conjugacy_completeness": "NOT_ESTABLISHED",
                "exact_matrix_collision_group_size": 0,
                "exact_inverse_pair_collision_group_size": 0,
                "trace_squared_isospectral_group_size": 0,
                "arithmetic_label": "NONE",
                "target_data_used": "false",
                "formal_route_a_tuple": "UNASSIGNED",
                "route_b_invocation_allowed": "false",
            }
        )

    by_id = {str(row["census_id"]): row for row in provisional}
    proved_homology_groups: dict[str, list[dict[str, object]]] = {}
    for row in provisional:
        if row["gamma_primitivity_status"] == "PROVED_BY_EXACT_LENGTH_LT_2_BOLZA_SYSTOLE":
            proved_homology_groups.setdefault(
                str(row["inverse_paired_homology_axis_key"]), []
            ).append(row)
    for group in proved_homology_groups.values():
        ordered_group = sorted(group, key=lambda row: str(row["census_id"]))
        for row in ordered_group:
            row["homology_axis_multiplicity_within_proved_set"] = len(ordered_group)
        credited = ordered_group[0]
        credited["owner_credit_status"] = "MINTED_INVERSE_PAIRED_AXIS_OWNER"
        credited["owner_distinctness_status"] = (
            "CERTIFIED_DISTINCT_FROM_OTHER_CREDITED_OWNERS_BY_HOMOLOGY_AXIS"
        )
        word = parse_word_text(str(credited["canonical_marked_word"]))
        if len(word) == 1 and word[0] > 0:
            credited["primitive_axis_owner_id"] = f"BOLZA_AXIS_INVERSE_PAIR_{word[0] - 1}"
        else:
            ordinal = int(str(credited["census_id"]).split("C")[-1])
            credited["primitive_axis_owner_id"] = f"BOLZA_MARKED_AXIS_INVPAIR_{ordinal:04d}"
        for withheld in ordered_group[1:]:
            withheld["owner_credit_status"] = (
                "WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED"
            )
            withheld["owner_distinctness_status"] = (
                "NOT_DISTINGUISHED_FROM_CREDITED_REPRESENTATIVE_BY_CURRENT_INVARIANTS"
            )
    for groups, field in (
        (direct_keys, "exact_matrix_collision_group_size"),
        (inverse_pair_keys, "exact_inverse_pair_collision_group_size"),
        (trace_squared_keys, "trace_squared_isospectral_group_size"),
    ):
        for identifiers in groups.values():
            for identifier in identifiers:
                by_id[identifier][field] = len(identifiers)
    return provisional, raw_counts


CENSUS_FIELDS = (
    "census_id",
    "census_schema",
    "metric_control_id",
    "group_source_lock",
    "marked_word_cutoff",
    "alphabet_order",
    "canonical_marked_word",
    "marked_length",
    "inverse_marked_word",
    "marked_cyclic_inverse_orbit_size",
    "canonical_rule",
    "marked_root_word",
    "marked_root_length",
    "marked_repetition_exponent",
    "marked_class_status",
    "exact_number_field",
    "exact_psl_matrix_key_sha256",
    "exact_inverse_paired_psl_key_sha256",
    "exact_trace",
    "exact_trace_squared",
    "exact_trace_squared_key_sha256",
    "absolute_trace_decimal",
    "geodesic_length_decimal",
    "bolza_systole_ratio_decimal",
    "gamma_primitivity_status",
    "gamma_primitivity_exact_margin_to_2sys",
    "canonical_homology_vector",
    "inverse_paired_homology_axis_key",
    "homology_axis_multiplicity_within_proved_set",
    "owner_distinctness_status",
    "primitive_axis_owner_id",
    "owner_credit_status",
    "owner_counting_convention",
    "marked_census_completeness",
    "full_gamma_conjugacy_completeness",
    "exact_matrix_collision_group_size",
    "exact_inverse_pair_collision_group_size",
    "trace_squared_isospectral_group_size",
    "arithmetic_label",
    "target_data_used",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)


BRANCH_FIELDS = (
    "row_id",
    "branch_schema",
    "census_id",
    "metric_control_id",
    "group_source_lock",
    "trace_source_lock",
    "field_b",
    "base_bundle",
    "tensor_regime",
    "primitive_axis_owner_id",
    "canonical_primitive_word",
    "inverse_pair_definition",
    "branch_primitive_word",
    "branch_group_element_word",
    "gamma_primitivity_status",
    "owner_credit_status",
    "owner_counting_convention",
    "source_k",
    "absolute_repetition_index",
    "source_k_class",
    "signed_k_partner_row_id",
    "field_sign_partner_row_id",
    "primitive_geodesic_length_decimal",
    "primitive_period_trace_clock_decimal",
    "absolute_total_trace_clock_period_decimal",
    "signed_trace_time_decimal",
    "primitive_period_physical_clock_decimal",
    "absolute_total_physical_period_decimal",
    "project_action_per_N_decimal",
    "poincare_multiplier_N_to_k_decimal",
    "poincare_multiplier_N_to_minus_k_decimal",
    "stability_determinant_sqrt_abs_decimal",
    "signed_trace_stability_denominator_decimal",
    "maslov_index",
    "connection_holonomy_status",
    "trace_owner_status",
    "enumeration_completeness",
    "full_gamma_conjugacy_completeness",
    "arithmetic_label",
    "target_data_used",
    "zero_field_status",
    "odd_N_status",
    "full_all_N_status",
    "fixed_operator_status",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)


def branch_row_id(field_b: str, census_id: str, source_k: int) -> str:
    field_code = "P" if field_b == "+1/2" else "M"
    k_code = f"KP{source_k}" if source_k > 0 else f"KN{abs(source_k)}"
    return f"B28R5-{field_code}-{census_id.split('-')[-1]}-{k_code}"


def build_branch_rows(census_rows: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    proved = [
        row
        for row in census_rows
        if row["owner_credit_status"] == "MINTED_INVERSE_PAIRED_AXIS_OWNER"
    ]
    signed_k_values = SOURCE_K_ABSOLUTE_VALUES + tuple(-value for value in SOURCE_K_ABSOLUTE_VALUES)
    rows: list[dict[str, object]] = []
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        sqrt3 = Decimal(3).sqrt()
        sqrt5_over_3 = (Decimal(5) / Decimal(3)).sqrt()
        for field_b, base_bundle in (("+1/2", "L"), ("-1/2", "L_dual")):
            partner_field = "-1/2" if field_b == "+1/2" else "+1/2"
            for census_row in proved:
                census_id = str(census_row["census_id"])
                owner_id = str(census_row["primitive_axis_owner_id"])
                canonical_word = parse_word_text(str(census_row["canonical_marked_word"]))
                ell = translation_length_from_trace(matrix_trace(word_matrix(canonical_word)))
                norm = ell.exp()
                trace_period = sqrt5_over_3 * ell
                physical_period = Decimal(2) / sqrt3 * ell
                action_unit = sqrt3 / Decimal(2) * ell
                for source_k in signed_k_values:
                    repetition = abs(source_k)
                    multiplier_k = norm**source_k if source_k > 0 else Decimal(1) / norm**repetition
                    multiplier_minus_k = Decimal(1) / multiplier_k
                    signed_denominator = multiplier_k.sqrt() - multiplier_minus_k.sqrt()
                    canonical_word_text = str(census_row["canonical_marked_word"])
                    canonical_word_tuple = parse_word_text(canonical_word_text)
                    inverse_word_text = word_text(inverse_word(canonical_word_tuple))
                    rows.append(
                        {
                            "row_id": branch_row_id(field_b, census_id, source_k),
                            "branch_schema": "p28_round5_proved_owner_signed_k_ledger/1.0",
                            "census_id": census_id,
                            "metric_control_id": "BOLZA_ARITHMETIC_CURVATURE_MINUS_1",
                            "group_source_lock": GROUP_SOURCE,
                            "trace_source_lock": TRACE_SOURCE,
                            "field_b": field_b,
                            "base_bundle": base_bundle,
                            "tensor_regime": "SOURCE_COMPATIBLE_EVEN_N_EQUALS_2m",
                            "primitive_axis_owner_id": owner_id,
                            "canonical_primitive_word": canonical_word_text,
                            "inverse_pair_definition": (
                                "{" + canonical_word_text + ";" + inverse_word_text + "}"
                            ),
                            "branch_primitive_word": (
                                canonical_word_text if source_k > 0 else inverse_word_text
                            ),
                            "branch_group_element_word": (
                                f"({canonical_word_text})^({source_k})"
                            ),
                            "gamma_primitivity_status": census_row["gamma_primitivity_status"],
                            "owner_credit_status": "MINTED_ONCE_PER_INVERSE_PAIRED_AXIS_PER_FIELD",
                            "owner_counting_convention": "INVERSE_PAIRED_AXIS_OWNER;EQ19_SIGNED_K_BRANCHES;NO_ORIENTATION_OWNER_CREDIT",
                            "source_k": source_k,
                            "absolute_repetition_index": repetition,
                            "source_k_class": (
                                "SIGNED_K_PRIMITIVE_BRANCH"
                                if repetition == 1
                                else "SIGNED_K_REPETITION_BRANCH"
                            ),
                            "signed_k_partner_row_id": branch_row_id(field_b, census_id, -source_k),
                            "field_sign_partner_row_id": branch_row_id(partner_field, census_id, -source_k),
                            "primitive_geodesic_length_decimal": decimal_string(ell),
                            "primitive_period_trace_clock_decimal": decimal_string(trace_period),
                            "absolute_total_trace_clock_period_decimal": decimal_string(Decimal(repetition) * trace_period),
                            "signed_trace_time_decimal": decimal_string(Decimal(source_k) * trace_period),
                            "primitive_period_physical_clock_decimal": decimal_string(physical_period),
                            "absolute_total_physical_period_decimal": decimal_string(Decimal(repetition) * physical_period),
                            "project_action_per_N_decimal": decimal_string(Decimal(source_k) * action_unit),
                            "poincare_multiplier_N_to_k_decimal": decimal_string(multiplier_k),
                            "poincare_multiplier_N_to_minus_k_decimal": decimal_string(multiplier_minus_k),
                            "stability_determinant_sqrt_abs_decimal": decimal_string(abs(signed_denominator)),
                            "signed_trace_stability_denominator_decimal": decimal_string(signed_denominator),
                            "maslov_index": 0,
                            "connection_holonomy_status": "NOT_SEPARATELY_LIFTED;EVEN_N_TOTAL_ACTION_SOURCE_BOUND",
                            "trace_owner_status": "PROVED_SOURCE_COMPATIBLE_INVERSE_PAIRED_AXIS_SIGNED_K_EVEN_SUBTYPE",
                            "enumeration_completeness": "ALL_EXACTLY_PRIMITIVITY_CERTIFIED_OWNERS_INSIDE_MARKED_LENGTH_LE_4_CENSUS",
                            "full_gamma_conjugacy_completeness": "NOT_ESTABLISHED",
                            "arithmetic_label": "NONE",
                            "target_data_used": "false",
                            "zero_field_status": "OPEN_NOT_IN_LEDGER",
                            "odd_N_status": "OPEN_NOT_ESTABLISHED",
                            "full_all_N_status": "OPEN_NOT_ESTABLISHED",
                            "fixed_operator_status": "OPEN_NOT_ESTABLISHED_NO_CREDIT_TRANSFER",
                            "formal_route_a_tuple": "UNASSIGNED",
                            "route_b_invocation_allowed": "false",
                        }
                    )
    return rows


def group_certificate(census_rows: Sequence[dict[str, object]], raw_counts: dict[int, int]) -> dict[str, object]:
    generators = EXACT_GENERATORS
    determinant_exact = [matrix_determinant(matrix) == ONE for matrix in generators]
    relator = ((1, 1), (2, -1), (3, 1), (4, -1), (1, -1), (2, 1), (3, -1), (4, 1))
    relator_matrix = word_matrix(tuple(letter * exponent for letter, exponent in relator))
    errors: list[str] = []
    if not all(determinant_exact):
        errors.append("an exact generator determinant is not one")
    if relator_matrix != matrix_identity():
        errors.append("the exact polygon relator failed")
    direct_collision_groups = [
        size for size in {str(row["exact_psl_matrix_key_sha256"]): int(row["exact_matrix_collision_group_size"]) for row in census_rows}.values() if size > 1
    ]
    inverse_collision_groups = [
        size for size in {str(row["exact_inverse_paired_psl_key_sha256"]): int(row["exact_inverse_pair_collision_group_size"]) for row in census_rows}.values() if size > 1
    ]
    if direct_collision_groups or inverse_collision_groups:
        errors.append("distinct marked records collided under exact PSL equality/inversion")
    length_counts = {
        str(length): sum(int(row["marked_length"]) == length for row in census_rows)
        for length in range(1, WORD_CUTOFF + 1)
    }
    trace_groups: dict[str, int] = {}
    for row in census_rows:
        trace_groups[str(row["exact_trace_squared_key_sha256"])] = int(row["trace_squared_isospectral_group_size"])
    return {
        "schema": "p28_round5_marked_cyclic_certificate/1.0",
        "status": "PASS" if not errors else "FAIL",
        "primary_source": {
            "citation": GROUP_SOURCE,
            "article_url": "https://doi.org/10.20382/jocg.v13i1a5",
            "arxiv_url": "https://arxiv.org/abs/2103.05960",
            "checked_date": "2026-08-27",
        },
        "exact_number_field": {
            "basis": ["1", "i", "t", "t*i", "s", "s*i", "s*t", "s*t*i"],
            "relations": ["s^2=2", "t^2=1+s", "i^2=-1"],
            "embedding": "s=positive_sqrt(2);t=positive_sqrt(1+s);i=positive_imaginary_unit",
            "generator_model": "diag=1+s;rho=s*t;upper phases 1,(1+i)/s,i,(-1+i)/s",
            "all_generator_determinants_exactly_one": all(determinant_exact),
            "polygon_relator_exactly_identity": relator_matrix == matrix_identity(),
        },
        "normal_form_rule": {
            "alphabet_order": "f0<f0^-1<f1<f1^-1<f2<f2^-1<f3<f3^-1",
            "input_scope": "all freely and cyclically reduced marked words with 1<=length<=4",
            "equivalence": "cyclic rotation plus word inversion",
            "representative": "lexicographically least word in the finite equivalence orbit",
            "proper_power_rule": "least periodic prefix among divisors of marked length",
        },
        "raw_cyclically_reduced_word_counts": {str(key): value for key, value in raw_counts.items()},
        "inverse_paired_marked_class_counts": length_counts,
        "inverse_paired_marked_class_total": len(census_rows),
        "marked_primitive_candidate_count": sum(row["marked_repetition_exponent"] == 1 for row in census_rows),
        "marked_power_count": sum(row["marked_repetition_exponent"] != 1 for row in census_rows),
        "gamma_primitivity_proved_count": sum(str(row["gamma_primitivity_status"]).startswith("PROVED_BY") for row in census_rows),
        "gamma_primitivity_open_count": sum(row["gamma_primitivity_status"] == "NOT_ESTABLISHED_MARKED_PRIMITIVE_ONLY" for row in census_rows),
        "distinct_inverse_paired_owner_credit_count": sum(
            row["owner_credit_status"] == "MINTED_INVERSE_PAIRED_AXIS_OWNER"
            for row in census_rows
        ),
        "proved_primitive_records_withheld_for_homology_axis_ambiguity": sum(
            row["owner_credit_status"]
            == "WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED"
            for row in census_rows
        ),
        "exact_primitivity_rule": "marked_primitive and abs(trace)<10+8*sqrt(2)=2*cosh(ell_B) implies length<2*ell_B and hence Gamma-primitive by systolic minimality",
        "owner_distinctness_rule": "credit at most one proved primitive per homology vector modulo sign; different credited homology axes cannot be Gamma-conjugate or inverse-conjugate; same-axis extras are withheld",
        "exact_projective_matrix_collision_groups": len(direct_collision_groups),
        "exact_projective_matrix_collision_extra_records": sum(size - 1 for size in direct_collision_groups),
        "exact_inverse_pair_collision_groups": len(inverse_collision_groups),
        "exact_inverse_pair_collision_extra_records": sum(size - 1 for size in inverse_collision_groups),
        "trace_squared_isospectral_group_count": len(trace_groups),
        "trace_squared_isospectral_nontrivial_group_count": sum(size > 1 for size in trace_groups.values()),
        "maximum_trace_squared_group_size": max(trace_groups.values()),
        "completeness_claim": "COMPLETE_MATCHED_MARKED_CYCLIC_CENSUS_AT_DECLARED_CUTOFF",
        "withheld_claim": "FULL_GAMMA_CONJUGACY_COMPLETENESS_NOT_ESTABLISHED",
        "errors": errors,
    }


def nonarithmetic_control_contract() -> dict[str, object]:
    return {
        "schema": "p28_round5_nonarithmetic_genus2_control_contract/1.0",
        "status": "DESIGN_ONLY_NOT_INSTANTIATED",
        "evidence_token": "OPEN",
        "required_geometry": {
            "surface": "closed_oriented_genus_2_constant_curvature_minus_1",
            "area": "4*pi_by_Gauss_Bonnet",
            "group_representation": "explicit_torsion_free_cocompact_Fuchsian_matrices_and_presentation_required",
            "source_lock": "peer_reviewed_or_primary_source_locator_required_before_execution",
            "nonarithmeticity": "independent_invariant_trace_field_or_quaternion_algebra_certificate_required",
            "systole": "source_or_rigorous_certificate_required_for_primitivity_gate",
        },
        "matched_physics": {
            "fields": ["+1/2", "-1/2"],
            "base_bundle_degrees": [1, -1],
            "tensor_regime": "N=2m with L^2=K and E=sqrt(5)",
            "trace_clock": "sqrt(5)/2 times physical clock",
            "source_k_values": [-4, -3, -2, -1, 1, 2, 3, 4],
            "owner_counting": "inverse_paired_axis_owner; signed k never mints owner credit",
        },
        "selection_contract": {
            "marked_word_layer": "same declared L=4 rule under an explicitly frozen control marking",
            "metric_comparison_layer": "freeze one common geodesic cutoff Lambda before inspecting branch outcomes",
            "primitive_safe_requirement": "Lambda < 2*min(sys_Bolza,sys_control) unless a stronger per-owner primitive certificate is supplied",
            "warning": "marked length is presentation-dependent and cannot alone support a cross-metric A0 comparison",
        },
        "execution": {
            "geometry_selected": False,
            "source_verified": False,
            "matrices_loaded": False,
            "census_run": False,
            "comparison_run": False,
        },
        "forbidden_inputs": ["rational_prime_targets", "prime_ideal_targets", "zeta_zero_targets", "fixed_operator_spectrum"],
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "claim_boundary": "PARAMETER_AND_SOURCE_CONTRACT_ONLY;NO_CONTROL_GEOMETRY_OR_RESULT_FABRICATED",
    }


def rows_by_id(rows: Sequence[dict[str, object]], field: str) -> dict[str, dict[str, object]]:
    return {str(row[field]): row for row in rows}


def validate(
    census_rows: Sequence[dict[str, object]],
    branch_rows: Sequence[dict[str, object]],
    certificate: dict[str, object],
    control_contract: dict[str, object],
) -> dict[str, object]:
    errors: list[str] = []
    expected_length_counts = {1: 4, 2: 16, 3: 60, 4: 310}
    actual_length_counts = {
        length: sum(int(row["marked_length"]) == length for row in census_rows)
        for length in expected_length_counts
    }
    if actual_length_counts != expected_length_counts:
        errors.append(f"marked length counts changed: {actual_length_counts}")
    if len(census_rows) != 390:
        errors.append(f"expected 390 census rows, found {len(census_rows)}")
    if certificate.get("status") != "PASS":
        errors.append("group/census certificate did not pass")
    if control_contract.get("status") != "DESIGN_ONLY_NOT_INSTANTIATED":
        errors.append("control contract was prematurely promoted")

    marked_primitive = [row for row in census_rows if row["marked_repetition_exponent"] == 1]
    marked_powers = [row for row in census_rows if row["marked_repetition_exponent"] != 1]
    proved = [row for row in census_rows if str(row["gamma_primitivity_status"]).startswith("PROVED_BY")]
    credited = [
        row
        for row in census_rows
        if row["owner_credit_status"] == "MINTED_INVERSE_PAIRED_AXIS_OWNER"
    ]
    homology_axis_withheld = [
        row
        for row in census_rows
        if row["owner_credit_status"]
        == "WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED"
    ]
    gamma_open = [row for row in census_rows if row["gamma_primitivity_status"] == "NOT_ESTABLISHED_MARKED_PRIMITIVE_ONLY"]
    if (
        len(marked_primitive),
        len(marked_powers),
        len(proved),
        len(credited),
        len(homology_axis_withheld),
        len(gamma_open),
    ) != (366, 24, 44, 36, 8, 322):
        errors.append("primitive/power/proved/credited/withheld/open counts changed")

    proved_by_length = {
        length: sum(int(row["marked_length"]) == length for row in proved)
        for length in expected_length_counts
    }
    if proved_by_length != {1: 4, 2: 12, 3: 16, 4: 12}:
        errors.append(f"proved-primitivity length distribution changed: {proved_by_length}")
    credited_by_length = {
        length: sum(int(row["marked_length"]) == length for row in credited)
        for length in expected_length_counts
    }
    if credited_by_length != {1: 4, 2: 12, 3: 12, 4: 8}:
        errors.append(f"credited-owner length distribution changed: {credited_by_length}")
    credited_homology_axes = {
        str(row["inverse_paired_homology_axis_key"]) for row in credited
    }
    if len(credited_homology_axes) != len(credited):
        errors.append("more than one owner credit was minted on a homology axis")

    direct_hashes = [str(row["exact_psl_matrix_key_sha256"]) for row in census_rows]
    inverse_hashes = [str(row["exact_inverse_paired_psl_key_sha256"]) for row in census_rows]
    if len(set(direct_hashes)) != len(census_rows):
        errors.append("an exact projective matrix collision remains")
    if len(set(inverse_hashes)) != len(census_rows):
        errors.append("an exact inverse-pair matrix collision remains")

    census_index = rows_by_id(census_rows, "census_id")
    power_checks = 0
    for row in marked_powers:
        word = next(
            candidate
            for candidate in (
                canonical_marked_inverse_pair(word)
                for length in range(1, WORD_CUTOFF + 1)
                for word in product(ALPHABET, repeat=length)
                if is_cyclically_reduced(word)
            )
            if word_text(candidate) == row["canonical_marked_word"]
        )
        root, exponent = marked_root_decomposition(word)
        if projective_matrix_key(word_matrix(word)) != projective_matrix_key(matrix_power(word_matrix(root), exponent)):
            errors.append(f"marked power matrix law failed for {row['census_id']}")
        power_checks += 1

    branch_index = rows_by_id(branch_rows, "row_id")
    expected_k = set(SOURCE_K_ABSOLUTE_VALUES) | {-value for value in SOURCE_K_ABSOLUTE_VALUES}
    if len(branch_rows) != 576:
        errors.append(f"expected 576 distinct-owner branch rows, found {len(branch_rows)}")
    owner_ids = {str(row["primitive_axis_owner_id"]) for row in credited}
    if len(owner_ids) != 36 or "" in owner_ids:
        errors.append("proved owner IDs are missing or duplicated")
    field_partner_checks = 0
    signed_k_partner_checks = 0
    law_checks = 0
    for row in branch_rows:
        row_id = str(row["row_id"])
        if set(row) != set(BRANCH_FIELDS):
            errors.append(f"branch schema changed for {row_id}")
        if row["primitive_axis_owner_id"] not in owner_ids:
            errors.append(f"unproved owner entered branch ledger: {row_id}")
        if row["full_gamma_conjugacy_completeness"] != "NOT_ESTABLISHED":
            errors.append(f"full Gamma completeness overclaimed: {row_id}")
        source_k = int(row["source_k"])
        if source_k not in expected_k:
            errors.append(f"source k outside frozen grid: {row_id}")
        partner = branch_index.get(str(row["signed_k_partner_row_id"]))
        if partner is None:
            errors.append(f"missing signed-k partner: {row_id}")
        else:
            if partner["signed_k_partner_row_id"] != row_id or int(partner["source_k"]) != -source_k:
                errors.append(f"signed-k partner failed: {row_id}")
            if partner["primitive_axis_owner_id"] != row["primitive_axis_owner_id"] or partner["field_b"] != row["field_b"]:
                errors.append(f"signed-k partner minted/changed owner: {row_id}")
            with localcontext() as context:
                context.prec = DECIMAL_PRECISION
                for field in (
                    "project_action_per_N_decimal",
                    "signed_trace_time_decimal",
                    "signed_trace_stability_denominator_decimal",
                ):
                    if abs(Decimal(str(partner[field])) + Decimal(str(row[field]))) >= Decimal("1e-65"):
                        errors.append(f"signed-k partner did not reverse {field}: {row_id}")
            signed_k_partner_checks += 1
        field_partner = branch_index.get(str(row["field_sign_partner_row_id"]))
        if field_partner is None:
            errors.append(f"missing field partner: {row_id}")
        else:
            if field_partner["field_sign_partner_row_id"] != row_id or int(field_partner["source_k"]) != -source_k:
                errors.append(f"field partner failed: {row_id}")
            if field_partner["primitive_axis_owner_id"] != row["primitive_axis_owner_id"] or field_partner["field_b"] == row["field_b"]:
                errors.append(f"field partner minted/changed owner: {row_id}")
            with localcontext() as context:
                context.prec = DECIMAL_PRECISION
                for field in (
                    "project_action_per_N_decimal",
                    "signed_trace_time_decimal",
                    "signed_trace_stability_denominator_decimal",
                ):
                    if abs(Decimal(str(field_partner[field])) + Decimal(str(row[field]))) >= Decimal("1e-65"):
                        errors.append(f"field partner did not reverse {field}: {row_id}")
            field_partner_checks += 1
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            multiplier = Decimal(str(row["poincare_multiplier_N_to_k_decimal"]))
            reciprocal = Decimal(str(row["poincare_multiplier_N_to_minus_k_decimal"]))
            signed_denominator = Decimal(str(row["signed_trace_stability_denominator_decimal"]))
            reciprocal_residual = abs(multiplier * reciprocal - Decimal(1))
            if reciprocal_residual >= Decimal("1e-64"):
                errors.append(f"multiplier reciprocity failed: {row_id}")
            expected_denominator = multiplier.sqrt() - reciprocal.sqrt()
            denominator_residual = abs(signed_denominator - expected_denominator)
            denominator_scale = max(abs(signed_denominator), abs(expected_denominator), Decimal(1))
            if denominator_residual / denominator_scale >= Decimal("1e-64"):
                errors.append(f"signed stability law failed: {row_id}")
        law_checks += 1
        if row["target_data_used"] != "false" or row["arithmetic_label"] != "NONE":
            errors.append(f"target/arithmetic data entered branch ledger: {row_id}")
        if row["formal_route_a_tuple"] != "UNASSIGNED" or row["route_b_invocation_allowed"] != "false":
            errors.append(f"route firewall failed: {row_id}")

    for field_b in ("+1/2", "-1/2"):
        field_rows = [row for row in branch_rows if row["field_b"] == field_b]
        if len(field_rows) != 288 or len({row["primitive_axis_owner_id"] for row in field_rows}) != 36:
            errors.append(f"field owner/branch count failed for {field_b}")
        for owner_id in owner_ids:
            grid = {int(row["source_k"]) for row in field_rows if row["primitive_axis_owner_id"] == owner_id}
            if grid != expected_k:
                errors.append(f"incomplete k grid for {field_b}/{owner_id}")

    # Round-4 seed rows at |k|<=3 must be recovered without changed owner IDs
    # or numerical formulas.  Round 5 adds k=+-4 but does not rewrite Round 4.
    round4_rows = ROUND4.build_rows()
    round4_compatibility_checks = 0
    for old in round4_rows:
        matches = [
            row for row in branch_rows
            if row["field_b"] == old["field_b"]
            and row["primitive_axis_owner_id"] == old["primitive_axis_owner_id"]
            and int(row["source_k"]) == int(old["source_k"])
        ]
        if len(matches) != 1:
            errors.append(f"Round-4 seed branch missing/duplicated: {old['row_id']}")
            continue
        new = matches[0]
        for field in (
            "primitive_geodesic_length_decimal",
            "primitive_period_trace_clock_decimal",
            "absolute_total_trace_clock_period_decimal",
            "signed_trace_time_decimal",
            "primitive_period_physical_clock_decimal",
            "absolute_total_physical_period_decimal",
            "project_action_per_N_decimal",
            "poincare_multiplier_N_to_k_decimal",
            "poincare_multiplier_N_to_minus_k_decimal",
            "stability_determinant_sqrt_abs_decimal",
            "signed_trace_stability_denominator_decimal",
        ):
            if Decimal(str(new[field])) != Decimal(str(old[field])):
                errors.append(f"Round-4 numerical compatibility failed for {old['row_id']}/{field}")
        round4_compatibility_checks += 1

    forbidden_fields = sum(
        any(key in {"oriented_primitive_owner_id", "orientation_sign"} for key in row)
        for row in list(census_rows) + list(branch_rows)
    )
    if forbidden_fields:
        errors.append("old oriented-owner credit fields reappeared")

    census_payload = json.dumps(census_rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    branch_payload = json.dumps(branch_rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "schema": "p28_round5_marked_cyclic_validation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "word_cutoff": WORD_CUTOFF,
        "census_row_count": len(census_rows),
        "marked_length_counts": {str(key): value for key, value in actual_length_counts.items()},
        "marked_primitive_candidate_count": len(marked_primitive),
        "marked_power_count": len(marked_powers),
        "gamma_primitivity_proved_count": len(proved),
        "gamma_primitivity_proved_by_marked_length": {str(key): value for key, value in proved_by_length.items()},
        "distinct_inverse_paired_owner_credit_count": len(credited),
        "distinct_owner_credit_by_marked_length": {
            str(key): value for key, value in credited_by_length.items()
        },
        "proved_primitive_records_withheld_for_homology_axis_ambiguity": len(
            homology_axis_withheld
        ),
        "gamma_primitivity_open_count": len(gamma_open),
        "primitive_axis_owners_per_field": len(owner_ids),
        "field_axis_owner_pairs": 2 * len(owner_ids),
        "branch_row_count": len(branch_rows),
        "signed_k_primitive_branch_rows": sum(abs(int(row["source_k"])) == 1 for row in branch_rows),
        "signed_k_repetition_branch_rows": sum(abs(int(row["source_k"])) > 1 for row in branch_rows),
        "source_k_values": sorted(expected_k),
        "maximum_absolute_repetition": max(SOURCE_K_ABSOLUTE_VALUES),
        "exact_projective_matrix_collision_groups": certificate["exact_projective_matrix_collision_groups"],
        "exact_inverse_pair_collision_groups": certificate["exact_inverse_pair_collision_groups"],
        "power_matrix_checks": power_checks,
        "signed_k_partner_checks": signed_k_partner_checks,
        "field_partner_checks": field_partner_checks,
        "period_action_stability_law_checks": law_checks,
        "round4_seed_compatibility_checks": round4_compatibility_checks,
        "forbidden_oriented_owner_field_rows": forbidden_fields,
        "target_data_rows": sum(row["target_data_used"] != "false" for row in list(census_rows) + list(branch_rows)),
        "arithmetic_label_rows": sum(row["arithmetic_label"] != "NONE" for row in list(census_rows) + list(branch_rows)),
        "census_payload_sha256": hashlib.sha256(census_payload).hexdigest(),
        "branch_payload_sha256": hashlib.sha256(branch_payload).hexdigest(),
        "marked_census_completeness": "COMPLETE_FOR_DECLARED_MARKED_CYCLIC_EQUIVALENCE_AT_LENGTH_LE_4",
        "full_gamma_conjugacy_completeness": "NOT_ESTABLISHED",
        "control_status": control_contract["status"],
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "errors": errors,
    }


def write_csv(path: Path, fields: Sequence[str], rows: Sequence[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--census-output", required=True, type=Path)
    parser.add_argument("--branch-output", required=True, type=Path)
    parser.add_argument("--certificate-output", required=True, type=Path)
    parser.add_argument("--control-contract-output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    arguments = parser.parse_args()

    census_rows, raw_counts = enumerate_marked_classes()
    branch_rows = build_branch_rows(census_rows)
    certificate = group_certificate(census_rows, raw_counts)
    control_contract = nonarithmetic_control_contract()
    validation = validate(census_rows, branch_rows, certificate, control_contract)
    write_csv(arguments.census_output, CENSUS_FIELDS, census_rows)
    write_csv(arguments.branch_output, BRANCH_FIELDS, branch_rows)
    write_json(arguments.certificate_output, certificate)
    write_json(arguments.control_contract_output, control_contract)
    write_json(arguments.validation_output, validation)
    print(json.dumps(validation, sort_keys=True))
    return 0 if certificate["status"] == "PASS" and validation["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
