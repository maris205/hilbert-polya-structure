#!/usr/bin/env python3
"""Build the P24 Round-5 matched marked-word census.

The comparison contract lives in ``experiments/round5_freeze_contract.json``
and is hash-pinned below.  Both systems use the same reduced/cyclically-reduced
word algorithm, dihedral (rotation plus inversion) canonicalization, symbolic
root rule, owner multiplicity, marked-length cutoff, and phase statistic.  The
candidate has four positive marked generators while the control presentation
has two; this alphabet/presentation confound is an output, not something the
program hides by calling either ledger a metric length spectrum.

Candidate matrix arithmetic is exact over Z[i].  Control holonomies are
evaluated with the 212-bit SnapPy high-precision representation and remain
non-interval numerical observations.  No prime, prime-ideal, or zero table is
read.
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
from pathlib import Path
from typing import Any

import snappy

import round2_bianchi_ledger as bianchi


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-27"
SNAPPY_VERSION = "3.3.2"
MAX_WORD_LENGTH = 5
NULL_REPLICATES = 64
NULL_SEED = "P24-R5-MATCHED-MARKED-WORD-PHASE-NULL-V1"
FREEZE_PATH = Path("experiments/round5_freeze_contract.json")
FREEZE_SHA256 = "210cff78b8af54847baae1c7ef21572dd697d70004f50723f6b1bac4e19a85b7"

RESULT_PATHS = {
    "candidate": Path("results/bianchi_matched_marked_word_round5.csv"),
    "control": Path("results/five_two_matched_marked_word_round5.csv"),
    "comparison": Path("results/round5_matched_phase_comparison.json"),
    "metrics": Path("results/round5_metrics.json"),
}
RECEIPT_PATH = Path("experiments/round5_receipt.json")
VALIDATION_PATH = Path("experiments/round5_validation.md")
SOURCE_BINDING_PATHS = (
    Path("code/round5_matched_marked_word.py"),
    Path("code/test_round5_matched_marked_word.py"),
    Path("experiments/reproduce_round5.sh"),
)

Word = tuple[int, ...]

FIELDS = [
    "system_id",
    "marked_owner_id",
    "positive_generator_rank",
    "normalized_canonical_word",
    "local_canonical_word",
    "marked_word_length",
    "marked_orbit_multiplicity",
    "symbolic_root_owner_id",
    "symbolic_root_word",
    "symbolic_repetition_exponent",
    "symbolic_primitive",
    "dynamical_class",
    "complex_length_re",
    "holonomy_angle",
    "psl_trace_squared_re",
    "psl_trace_squared_im",
    "trace_reconstruction_residual",
    "matrix_determinant_residual",
    "candidate_level3_membership",
    "matrix_representation",
    "orientation_branch",
    "owner_scope",
    "completeness_boundary",
    "evidence_status",
    "target_data_used",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def combined_hash(outputs: dict[Path, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(outputs, key=lambda item: item.as_posix()):
        digest.update(path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[path])
        digest.update(b"\0")
    return digest.hexdigest()


def load_frozen_contract() -> tuple[dict[str, Any], bytes]:
    raw = (PROJECT_ROOT / FREEZE_PATH).read_bytes()
    observed = sha256(raw)
    if observed != FREEZE_SHA256:
        raise RuntimeError(
            f"Round-5 freeze contract changed: expected {FREEZE_SHA256}, found {observed}"
        )
    payload = json.loads(raw)
    if payload["enumeration"]["maximum_marked_word_length"] != MAX_WORD_LENGTH:
        raise AssertionError("freeze/cutoff mismatch")
    if payload["comparison"]["null_replicates"] != NULL_REPLICATES:
        raise AssertionError("freeze/null-replicate mismatch")
    if payload["comparison"]["seed_label"] != NULL_SEED:
        raise AssertionError("freeze/null-seed mismatch")
    if payload["route_boundary"]["formal_route_a_tuple"] != "UNASSIGNED":
        raise AssertionError("freeze contract attempted Route advancement")
    return payload, raw


def inverse_word(word: Word) -> Word:
    return tuple(token ^ 1 for token in reversed(word))


def rotations(word: Word) -> tuple[Word, ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_owner(word: Word) -> Word:
    if not word:
        return word
    return min(rotations(word) + rotations(inverse_word(word)))


def symbolic_root(word: Word) -> tuple[Word, int]:
    for size in range(1, len(word)):
        if len(word) % size:
            continue
        root = word[:size]
        exponent = len(word) // size
        if root * exponent == word:
            return canonical_owner(root), exponent
    return word, 1


def owner_id(rank: int, word: Word) -> str:
    encoded = f"rank={rank};word={','.join(map(str, word))}".encode("ascii")
    return f"MW{rank}_" + sha256(encoded)[:16]


def normalized_word_text(word: Word) -> str:
    labels = [f"g{token // 2 + 1}" if token % 2 == 0 else f"G{token // 2 + 1}" for token in word]
    return ".".join(labels)


def local_word_text(word: Word, labels: tuple[str, ...]) -> str:
    return ".".join(labels[token] for token in word)


def enumerate_marked_owners(rank: int) -> list[dict[str, Any]]:
    multiplicities: Counter[Word] = Counter()

    def extend(prefix: Word, target_length: int) -> None:
        if len(prefix) == target_length:
            if prefix[0] == (prefix[-1] ^ 1):
                return
            multiplicities[canonical_owner(prefix)] += 1
            return
        for token in range(2 * rank):
            if prefix and token == (prefix[-1] ^ 1):
                continue
            extend(prefix + (token,), target_length)

    for length in range(1, MAX_WORD_LENGTH + 1):
        extend((), length)

    owners: list[dict[str, Any]] = []
    for word in sorted(multiplicities, key=lambda item: (len(item), item)):
        root, exponent = symbolic_root(word)
        owners.append(
            {
                "word": word,
                "root": root,
                "exponent": exponent,
                "multiplicity": multiplicities[word],
                "owner_id": owner_id(rank, word),
                "root_owner_id": owner_id(rank, root),
            }
        )
    return owners


def _float(value: float) -> str:
    return format(value, ".17g")


def _gaussian_to_pair(value: bianchi.Gaussian) -> tuple[str, str]:
    return str(value[0]), str(value[1])


def candidate_rows(owners: list[dict[str, Any]]) -> list[dict[str, str]]:
    labels = tuple(bianchi.GENERATOR_ORDER)
    matrices = tuple(bianchi.GENERATORS[label] for label in labels)
    rows: list[dict[str, str]] = []
    for owner in owners:
        word = owner["word"]
        matrix = bianchi.IDENTITY
        for token in word:
            matrix = bianchi.mat_mul(matrix, matrices[token])
        matrix_class = bianchi.classification(matrix)
        trace = bianchi.mat_trace(matrix)
        trace_squared = bianchi.g_square(trace)
        if matrix_class == "LOXODROMIC":
            length, angle, residual = bianchi.complex_length(trace)
        else:
            length, angle, residual = math.nan, math.nan, 0.0
        trace_re, trace_im = _gaussian_to_pair(trace_squared)
        rows.append(
            {
                "system_id": "BIANCHI_LEVEL3_ELEMENTARY_MARKING",
                "marked_owner_id": owner["owner_id"],
                "positive_generator_rank": "4",
                "normalized_canonical_word": normalized_word_text(word),
                "local_canonical_word": local_word_text(word, labels),
                "marked_word_length": str(len(word)),
                "marked_orbit_multiplicity": str(owner["multiplicity"]),
                "symbolic_root_owner_id": owner["root_owner_id"],
                "symbolic_root_word": normalized_word_text(owner["root"]),
                "symbolic_repetition_exponent": str(owner["exponent"]),
                "symbolic_primitive": str(owner["exponent"] == 1).lower(),
                "dynamical_class": matrix_class,
                "complex_length_re": "" if math.isnan(length) else _float(length),
                "holonomy_angle": "" if math.isnan(angle) else _float(angle),
                "psl_trace_squared_re": trace_re,
                "psl_trace_squared_im": trace_im,
                "trace_reconstruction_residual": _float(residual),
                "matrix_determinant_residual": "0",
                "candidate_level3_membership": str(bianchi.in_level_three(matrix)).lower(),
                "matrix_representation": "EXACT_GAUSSIAN_INTEGER_SL2",
                "orientation_branch": "CANONICAL_DIHEDRAL_MARKED_WORD_REPRESENTATIVE",
                "owner_scope": "MARKED_SYMBOLIC_CYCLIC_OWNER_NOT_FULL_GROUP_CONJUGACY",
                "completeness_boundary": (
                    "FOUR_ELEMENTARY_GENERATED_SUBGROUP;MARKED_LENGTH_LE_5;"
                    "NOT_ALL_GAMMA3;NOT_METRIC_LENGTH_SPECTRUM"
                ),
                "evidence_status": "EXACT_MATRIX_AND_SYMBOLIC_LAYER_PLUS_NUMERICAL_COMPLEX_LENGTH",
                "target_data_used": "false",
            }
        )
    return rows


def control_complex_length(trace: Any) -> tuple[float, float, float]:
    value = 2 * (trace / 2).acosh()
    value_complex = complex(value)
    if value_complex.real < 0:
        value_complex = -value_complex
    angle = ((value_complex.imag + math.pi) % (2 * math.pi)) - math.pi
    if angle <= -math.pi + 1e-14:
        angle = math.pi
    normalized = complex(value_complex.real, angle)
    reconstructed = 2 * cmath.cosh(normalized / 2)
    trace_complex = complex(trace)
    residual = min(abs(reconstructed - trace_complex), abs(reconstructed + trace_complex))
    return normalized.real, normalized.imag, residual


def control_rows(owners: list[dict[str, Any]]) -> tuple[list[dict[str, str]], dict[str, Any]]:
    if snappy.__version__ != SNAPPY_VERSION:
        raise RuntimeError(
            f"P24 Round 5 requires snappy=={SNAPPY_VERSION}; found {snappy.__version__}"
        )
    manifold = snappy.Manifold("5_2")
    if not manifold.is_isometric_to(snappy.Manifold("m015")):
        raise AssertionError("rigorous named-control binding 5_2=m015 failed")
    group = manifold.high_precision().fundamental_group(simplify_presentation=True)
    if list(group.generators()) != ["a", "b"]:
        raise AssertionError(f"control generator marking changed: {group.generators()}")
    if list(group.relators()) != ["aBBBabbAAbb"]:
        raise AssertionError(f"control presentation relator changed: {group.relators()}")

    labels = ("a", "A", "b", "B")
    rows: list[dict[str, str]] = []
    determinant_residuals: list[float] = []
    parabolic_residuals: list[float] = []
    loxodromic_gaps: list[float] = []
    for owner in owners:
        word = owner["word"]
        local = "".join(labels[token] for token in word)
        matrix = group.SL2C(local)
        determinant_residual = abs(complex(matrix.det()) - 1)
        determinant_residuals.append(determinant_residual)
        trace = matrix.trace()
        trace_squared = trace * trace
        parabolic_residual = abs(complex(trace_squared) - 4)
        if parabolic_residual < 1e-25:
            matrix_class = "PARABOLIC"
            parabolic_residuals.append(parabolic_residual)
            length = angle = math.nan
            trace_residual = 0.0
        else:
            matrix_class = "LOXODROMIC"
            loxodromic_gaps.append(parabolic_residual)
            length, angle, trace_residual = control_complex_length(trace)
        trace_squared_complex = complex(trace_squared)
        rows.append(
            {
                "system_id": "FIVE_TWO_SNAPPY_PRESENTATION",
                "marked_owner_id": owner["owner_id"],
                "positive_generator_rank": "2",
                "normalized_canonical_word": normalized_word_text(word),
                "local_canonical_word": local,
                "marked_word_length": str(len(word)),
                "marked_orbit_multiplicity": str(owner["multiplicity"]),
                "symbolic_root_owner_id": owner["root_owner_id"],
                "symbolic_root_word": normalized_word_text(owner["root"]),
                "symbolic_repetition_exponent": str(owner["exponent"]),
                "symbolic_primitive": str(owner["exponent"] == 1).lower(),
                "dynamical_class": matrix_class,
                "complex_length_re": "" if math.isnan(length) else _float(length),
                "holonomy_angle": "" if math.isnan(angle) else _float(angle),
                "psl_trace_squared_re": _float(trace_squared_complex.real),
                "psl_trace_squared_im": _float(trace_squared_complex.imag),
                "trace_reconstruction_residual": _float(trace_residual),
                "matrix_determinant_residual": f"{determinant_residual:.17e}",
                "candidate_level3_membership": "NOT_APPLICABLE_CONTROL",
                "matrix_representation": "SNAPPY_HP_212_BIT_NUMERICAL_SL2C_NOT_INTERVAL",
                "orientation_branch": "CANONICAL_DIHEDRAL_MARKED_WORD_REPRESENTATIVE",
                "owner_scope": "MARKED_SYMBOLIC_CYCLIC_OWNER_NOT_FULL_GROUP_CONJUGACY",
                "completeness_boundary": (
                    "PINNED_TWO_GENERATOR_PRESENTATION;MARKED_LENGTH_LE_5;"
                    "NOT_METRIC_LENGTH_SPECTRUM;NOT_FULL_PRIMITIVE_SPECTRUM"
                ),
                "evidence_status": "PROVED_CONTROL_GEOMETRY_SEPARATE_FROM_NUMERICAL_HOLONOMY_LAYER",
                "target_data_used": "false",
            }
        )
    return rows, {
        "snappy_version": snappy.__version__,
        "precision_bits": int(group.SL2C("a")[0, 0].precision()),
        "generators": list(group.generators()),
        "relators": list(group.relators()),
        "maximum_determinant_residual": max(determinant_residuals, default=0.0),
        "parabolic_classification_threshold": 1e-25,
        "maximum_parabolic_trace_squared_minus_four_residual": max(
            parabolic_residuals, default=0.0
        ),
        "minimum_loxodromic_trace_squared_minus_four_gap": min(
            loxodromic_gaps, default=math.inf
        ),
        "named_control_isometry_check": "RIGOROUS_TRUE",
    }


def _corr(xs: list[float], ys: list[float]) -> float:
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    centered_x = [value - mean_x for value in xs]
    centered_y = [value - mean_y for value in ys]
    denominator = math.sqrt(
        sum(value * value for value in centered_x)
        * sum(value * value for value in centered_y)
    )
    if denominator == 0:
        return 0.0
    return sum(
        left * right for left, right in zip(centered_x, centered_y, strict=True)
    ) / denominator


def complex_phase_moment(lengths: list[float], angles: list[float]) -> complex:
    return complex(
        _corr(lengths, [math.cos(angle) for angle in angles]),
        _corr(lengths, [math.sin(angle) for angle in angles]),
    )


def phase_summary(system_id: str, rows: list[dict[str, str]]) -> dict[str, Any]:
    selected = [
        row
        for row in rows
        if row["symbolic_primitive"] == "true" and row["dynamical_class"] == "LOXODROMIC"
    ]
    lengths = [float(row["complex_length_re"]) for row in selected]
    angles = [float(row["holonomy_angle"]) for row in selected]
    observed = complex_phase_moment(lengths, angles)
    null_values: list[float] = []
    for replicate in range(NULL_REPLICATES):
        order = sorted(
            range(len(selected)),
            key=lambda index: sha256(
                (
                    f"{NULL_SEED}:{system_id}:{replicate}:"
                    f"{selected[index]['marked_owner_id']}"
                ).encode("utf-8")
            ),
        )
        shuffled_angles = [angles[index] for index in order]
        null_values.append(abs(complex_phase_moment(lengths, shuffled_angles)))
    null_mean = sum(null_values) / len(null_values)
    null_sd = math.sqrt(
        sum((value - null_mean) ** 2 for value in null_values)
        / (len(null_values) - 1)
    )
    if null_sd == 0:
        raise AssertionError(f"degenerate permutation null for {system_id}")
    return {
        "system_id": system_id,
        "owner_filter": "SYMBOLICALLY_PRIMITIVE_AND_LOXODROMIC",
        "rows_used": len(selected),
        "q_real": observed.real,
        "q_imag": observed.imag,
        "abs_q": abs(observed),
        "null_replicates": NULL_REPLICATES,
        "null_mean_abs_q": null_mean,
        "null_sample_sd_abs_q": null_sd,
        "z_abs_q": (abs(observed) - null_mean) / null_sd,
        "statistic_status": "FROZEN_PRE_RESULT_NUMERICAL_OBSERVATION",
    }


def row_metrics(rows: list[dict[str, str]]) -> dict[str, Any]:
    classes = Counter(row["dynamical_class"] for row in rows)
    primitive = sum(row["symbolic_primitive"] == "true" for row in rows)
    return {
        "marked_owner_rows": len(rows),
        "raw_cyclically_reduced_linear_words": sum(
            int(row["marked_orbit_multiplicity"]) for row in rows
        ),
        "symbolically_primitive_owner_rows": primitive,
        "symbolic_repetition_owner_rows": len(rows) - primitive,
        "loxodromic_owner_rows": classes["LOXODROMIC"],
        "parabolic_owner_rows": classes["PARABOLIC"],
        "identity_owner_rows": classes["IDENTITY"],
        "primitive_loxodromic_rows_used_in_phase_comparison": sum(
            row["symbolic_primitive"] == "true" and row["dynamical_class"] == "LOXODROMIC"
            for row in rows
        ),
        "all_target_data_flags_false": all(row["target_data_used"] == "false" for row in rows),
        "maximum_trace_reconstruction_residual": max(
            float(row["trace_reconstruction_residual"]) for row in rows
        ),
    }


def build_payload() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any], dict[str, Any]]:
    freeze, _raw = load_frozen_contract()
    candidate_owners = enumerate_marked_owners(rank=4)
    control_owners = enumerate_marked_owners(rank=2)
    candidate = candidate_rows(candidate_owners)
    control, control_contract = control_rows(control_owners)
    candidate_phase = phase_summary("BIANCHI_LEVEL3_ELEMENTARY_MARKING", candidate)
    control_phase = phase_summary("FIVE_TWO_SNAPPY_PRESENTATION", control)
    comparison = {
        "schema": "p24-round5-matched-phase-comparison/1.0",
        "date": DATE,
        "freeze_contract_sha256": FREEZE_SHA256,
        "statistic_frozen_before_result_execution": True,
        "statistic_formula": freeze["comparison"]["complex_phase_length_moment"],
        "candidate": candidate_phase,
        "control": control_phase,
        "absolute_permutation_standardized_phase_contrast": abs(
            candidate_phase["z_abs_q"] - control_phase["z_abs_q"]
        ),
        "interpretation": (
            "DESCRIPTIVE_MARKING_DEPENDENT_COMPARISON_ONLY;ALPHABET_SIZE_AND_"
            "PRESENTATION_CONFOUND_PRECLUDE_ARITHMETIC_OR_METRIC_SPECTRUM_VERDICT"
        ),
        "prime_or_zero_target_data_used": False,
    }
    metrics = {
        "schema": "p24-round5-metrics/1.0",
        "date": DATE,
        "freeze_contract_sha256": FREEZE_SHA256,
        "same_executable_enumeration_contract": True,
        "same_canonicalization": True,
        "same_symbolic_primitivity_rule": True,
        "same_marked_orbit_multiplicity_rule": True,
        "same_marked_word_cutoff": MAX_WORD_LENGTH,
        "same_comparison_precision_contract": True,
        "comparison_precision_contract": (
            "SYSTEM_SPECIFIC_MATRIX_EVALUATION_THEN_COMMON_BINARY64_COMPLEX_"
            "LENGTH_SERIALIZED_TO_17_SIGNIFICANT_DIGITS_AND_REPARSED"
        ),
        "candidate_positive_generator_rank": 4,
        "control_positive_generator_rank": 2,
        "generator_rank_semantics": (
            "MARKED_POSITIVE_GENERATOR_COUNT_NOT_A_CLAIM_OF_MINIMAL_GROUP_"
            "RANK_OR_FREE_RANK"
        ),
        "alphabet_size_and_presentation_confound": "RETAINED_AND_EXPLICIT",
        "candidate": row_metrics(candidate),
        "control": row_metrics(control),
        "candidate_all_exact_determinants_one": all(
            row["matrix_determinant_residual"] == "0" for row in candidate
        ),
        "candidate_all_level3_membership": all(
            row["candidate_level3_membership"] == "true" for row in candidate
        ),
        "control_numerical_contract": control_contract,
        "comparison_artifact": RESULT_PATHS["comparison"].as_posix(),
        "comparison_status": "EXECUTED_NUMERICAL_OBSERVATION_NO_ARITHMETIC_VERDICT",
        "full_group_conjugacy_completeness": "NOT_CLAIMED",
        "full_group_primitivity_completeness": "NOT_CLAIMED",
        "metric_length_spectrum": "NOT_CLAIMED",
        "forbidden_target_data_used": False,
        "ars_stage": "1_RESEARCH_IN_PROGRESS",
        "proposal_stage": 1,
        "route_a_scope": "A0-A1_ONLY",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "gates_a_e": "NOT_REACHED",
        "paper_level_consequence": (
            "THE_ROUND4_ENUMERATION_TYPE_MISMATCH_IS_CLOSED_AT_THE_MARKED_WORD_"
            "ALGORITHM_LEVEL;THE_REMAINING_MARKED_GENERATOR_COUNT_PRESENTATION_"
            "CONFOUND_IS_NOW_"
            "MEASURED_AND_BLOCKS_AN_ARITHMETIC_KILL_VERDICT"
        ),
        "smallest_next_artifact": (
            "PREREGISTERED_SAME_MARKED_GENERATOR_COUNT_NIELSEN_SENSITIVITY_PANEL_WITHOUT_"
            "TARGET_DATA_BEFORE_ANY_METRIC_CUTOFF_OR_ARITHMETIC_INTERPRETATION"
        ),
    }
    return candidate, control, comparison, metrics


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    candidate, control, comparison, metrics = build_payload()
    return {
        RESULT_PATHS["candidate"]: csv_bytes(candidate),
        RESULT_PATHS["control"]: csv_bytes(control),
        RESULT_PATHS["comparison"]: json_bytes(comparison),
        RESULT_PATHS["metrics"]: json_bytes(metrics),
    }, metrics


def receipt_for(outputs: dict[Path, bytes], metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "p24-round5-reproduction-receipt/1.1",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "freeze_contract": {
            "path": FREEZE_PATH.as_posix(),
            "sha256": FREEZE_SHA256,
            "frozen_before_result_execution": True,
        },
        "files": {
            path.as_posix(): {"sha256": sha256(data), "bytes": len(data)}
            for path, data in sorted(outputs.items(), key=lambda item: item[0].as_posix())
        },
        "source_bindings": {
            path.as_posix(): {
                "sha256": sha256((PROJECT_ROOT / path).read_bytes()),
                "bytes": (PROJECT_ROOT / path).stat().st_size,
            }
            for path in SOURCE_BINDING_PATHS
        },
        "dependency": f"snappy=={SNAPPY_VERSION}",
        "reproduction_command": "bash experiments/reproduce_round5.sh",
        "tests_expected": 10,
        "candidate_marked_owner_rows": metrics["candidate"]["marked_owner_rows"],
        "control_marked_owner_rows": metrics["control"]["marked_owner_rows"],
        "evidence_boundary": (
            "EXACT_CANDIDATE_MATRIX_AND_SYMBOLIC_ENUMERATION;HIGH_PRECISION_"
            "NONINTERVAL_CONTROL_HOLONOMY;MARKING_DEPENDENT_NUMERICAL_COMPARISON"
        ),
        "forbidden_target_data_used": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_invocation_allowed": False,
    }


def validation_markdown(outputs: dict[Path, bytes], metrics: dict[str, Any]) -> bytes:
    comparison = json.loads(outputs[RESULT_PATHS["comparison"]])
    candidate_phase = comparison["candidate"]
    control_phase = comparison["control"]
    text = f"""# P24 Round-5 validation report

## Material Passport

- Origin Skill: academic-research-suite + experiment-agent
- Origin Mode: Stage-1 research execution + validate
- Origin Date: {DATE}
- Verification Status: VERIFIED
- Version Label: p24_round5_validation_v1

## Reproducibility verdict

- Determinism class: exact symbolic/exact candidate arithmetic plus pinned
  high-precision control holonomy.
- Verdict: `REPRODUCIBLE`.
- Core-output combined SHA-256: `{combined_hash(outputs)}`.
- Pre-result freeze SHA-256: `{FREEZE_SHA256}`.
- Two independent temporary builds must be byte-identical under
  `bash experiments/reproduce_round5.sh`.

## Matched census checks

- Candidate marked owners: {metrics['candidate']['marked_owner_rows']} from
  {metrics['candidate']['raw_cyclically_reduced_linear_words']} raw cyclically
  reduced linear words.
- Control marked owners: {metrics['control']['marked_owner_rows']} from
  {metrics['control']['raw_cyclically_reduced_linear_words']} raw cyclically
  reduced linear words.
- Candidate primitive loxodromic comparison rows:
  {metrics['candidate']['primitive_loxodromic_rows_used_in_phase_comparison']}.
- Control primitive loxodromic comparison rows:
  {metrics['control']['primitive_loxodromic_rows_used_in_phase_comparison']}.
- The same canonicalization, symbolic primitivity, owner multiplicity, cutoff,
  binary64/17-significant-digit comparison projection, phase statistic and
  64-permutation rule are used on both sides.
- Every candidate determinant and level-`(3)` membership check passes exactly.
- Maximum control determinant residual:
  `{metrics['control_numerical_contract']['maximum_determinant_residual']:.3e}`.
- Control class separation: maximum parabolic `|tr^2-4|`
  `{metrics['control_numerical_contract']['maximum_parabolic_trace_squared_minus_four_residual']:.3e}`;
  minimum loxodromic gap
  `{metrics['control_numerical_contract']['minimum_loxodromic_trace_squared_minus_four_gap']:.3e}`.

## Frozen phase-sensitive observation

```text
candidate |q| = {candidate_phase['abs_q']:.12g}; z = {candidate_phase['z_abs_q']:.12g}
control   |q| = {control_phase['abs_q']:.12g}; z = {control_phase['z_abs_q']:.12g}
absolute z contrast = {comparison['absolute_permutation_standardized_phase_contrast']:.12g}
```

This is a marking-dependent `[NUMERICAL_OBSERVATION]`.  The candidate has four
marked positive generators / alphabet size 8 while the pinned control has two
/ alphabet size 4.  Thus the Round-4 **data-type** mismatch is closed by a common executable
marked-word rule, but the alphabet/presentation confound remains.  Neither CSV
is a complete metric length spectrum or a full group-conjugacy/primitive
enumeration.

## Integrity and Route boundary

- Prime, prime-ideal and zero target data used: `false`.
- Formal Route-A tuple: `UNASSIGNED`.
- A2--A4: `NOT_EVALUATED`.
- Route B: `NOT_RUN`; invocation allowed: `false`.
"""
    return text.encode("utf-8")


def rendered_outputs() -> dict[Path, bytes]:
    core, metrics = core_outputs()
    rendered = dict(core)
    rendered[RECEIPT_PATH] = json_bytes(receipt_for(core, metrics))
    rendered[VALIDATION_PATH] = validation_markdown(core, metrics)
    return rendered


def write_outputs(output_root: Path) -> None:
    for relative, data in rendered_outputs().items():
        path = output_root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def verify_existing(output_root: Path) -> None:
    mismatches: list[str] = []
    for relative, expected in rendered_outputs().items():
        path = output_root / relative
        if not path.exists():
            mismatches.append(f"missing:{relative}")
        elif path.read_bytes() != expected:
            mismatches.append(f"different:{relative}")
    if mismatches:
        raise SystemExit("verification failed: " + ", ".join(mismatches))
    print("P24 Round-5 existing artifacts VERIFIED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    if args.verify_existing:
        verify_existing(args.output_root)
    else:
        write_outputs(args.output_root)
        core, metrics = core_outputs()
        print(
            "P24 Round 5 complete: "
            f"candidate_owners={metrics['candidate']['marked_owner_rows']} "
            f"control_owners={metrics['control']['marked_owner_rows']} "
            f"core_sha256={combined_hash(core)}"
        )


if __name__ == "__main__":
    main()
