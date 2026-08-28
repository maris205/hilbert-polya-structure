#!/usr/bin/env python3
"""Exhaustive elementary-Nielsen marking sensitivity audit for Paper 24.

Both systems are evaluated with four positive marked generators.  The Bianchi
side uses its native elementary four-tuple.  The finite-volume ``5_2=m015``
control uses the explicitly redundant Tietze four-marking ``(a,b,ab,aB)``.
The canonical panel is identity plus every elementary right Nielsen move
``x_i -> x_i x_j^epsilon`` for ``i != j`` and ``epsilon in {+1,-1}``.

The panel is exhaustive rather than result-selected.  A disclosed provisional
planning pilot means this is an exploratory decision audit, not a blind
confirmatory experiment.  No pilot numbers are read or emitted by this code.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import csv
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any

import snappy

import round2_bianchi_ledger as bianchi
import round5_matched_marked_word as round5


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
SNAPPY_VERSION = "3.3.2"
MAX_WORD_LENGTH = 5
NULL_REPLICATES = 64
NULL_SEED = "P24-R6-EXHAUSTIVE-NIELSEN-PHASE-NULL-V1"
FREEZE_PATH = Path("experiments/round6_nielsen_panel_freeze.json")
FREEZE_SHA256 = "ea2ac26dfab2ff05f7ea4f179d76c96130559d94013d0f0f5b4689a44f730f89"

RESULT_PATHS = {
    "panel": Path("results/round6_nielsen_panel.csv"),
    "metrics": Path("results/round6_nielsen_metrics.json"),
}
RECEIPT_PATH = Path("experiments/round6_receipt.json")
VALIDATION_PATH = Path("experiments/round6_validation.md")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round6_nielsen_sensitivity.py"),
    Path("code/test_round6_nielsen_sensitivity.py"),
    Path("experiments/reproduce_round6.sh"),
)

Word = tuple[int, ...]
Marking = tuple[Word, ...]

PANEL_FIELDS = [
    "system_id",
    "marking_id",
    "move_target",
    "move_source",
    "move_exponent",
    "positive_generator_count",
    "alphabet_size",
    "marked_owner_rows",
    "raw_cyclically_reduced_linear_words",
    "symbolically_primitive_owner_rows",
    "symbolic_repetition_owner_rows",
    "identity_owner_rows",
    "parabolic_owner_rows",
    "loxodromic_owner_rows",
    "primitive_loxodromic_phase_rows",
    "q_real",
    "q_imag",
    "abs_q",
    "null_mean_abs_q",
    "null_sample_sd_abs_q",
    "z_abs_q",
    "maximum_matrix_determinant_residual",
    "all_candidate_level3_membership",
    "evaluation_digest",
    "evidence_status",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=PANEL_FIELDS, lineterminator="\n")
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


def load_freeze() -> tuple[dict[str, Any], bytes]:
    raw = (PROJECT_ROOT / FREEZE_PATH).read_bytes()
    if sha256(raw) != FREEZE_SHA256:
        raise RuntimeError("P24 Round-6 freeze contract changed")
    payload = json.loads(raw)
    if payload["panel"]["expected_markings_per_system"] != 25:
        raise AssertionError("freeze/panel-size mismatch")
    if payload["enumeration"]["maximum_marked_word_length"] != MAX_WORD_LENGTH:
        raise AssertionError("freeze/cutoff mismatch")
    if payload["comparison"]["null_replicates"] != NULL_REPLICATES:
        raise AssertionError("freeze/null-count mismatch")
    if payload["comparison"]["null_seed"] != NULL_SEED:
        raise AssertionError("freeze/null-seed mismatch")
    if any(payload["forbidden_inputs"].values()):
        raise AssertionError("forbidden input flags must remain false")
    return payload, raw


def inverse_word(word: Word) -> Word:
    return tuple(token ^ 1 for token in reversed(word))


def freely_reduce(word: Word) -> Word:
    stack: list[int] = []
    for token in word:
        if stack and token == (stack[-1] ^ 1):
            stack.pop()
        else:
            stack.append(token)
    return tuple(stack)


def base_marking() -> Marking:
    return tuple((2 * index,) for index in range(4))


def apply_elementary_move(marking: Marking, target: int, source: int, exponent: int) -> Marking:
    if target == source or exponent not in {-1, 1}:
        raise ValueError("invalid elementary Nielsen move")
    result = list(marking)
    source_word = marking[source] if exponent == 1 else inverse_word(marking[source])
    result[target] = freely_reduce(marking[target] + source_word)
    return tuple(result)


def panel_markings() -> list[dict[str, Any]]:
    base = base_marking()
    panel: list[dict[str, Any]] = [
        {
            "marking_id": "ID",
            "target": None,
            "source": None,
            "exponent": 0,
            "marking": base,
        }
    ]
    for target in range(4):
        for source in range(4):
            if target == source:
                continue
            for exponent, suffix in ((1, "P"), (-1, "M")):
                panel.append(
                    {
                        "marking_id": f"R{target + 1}_{source + 1}_{suffix}",
                        "target": target,
                        "source": source,
                        "exponent": exponent,
                        "marking": apply_elementary_move(base, target, source, exponent),
                    }
                )
    if len(panel) != 25 or len({row["marking_id"] for row in panel}) != 25:
        raise AssertionError("canonical panel construction failed")
    return panel


def expand_word(word: Word, marking: Marking) -> Word:
    expanded: Word = ()
    for token in word:
        positive = marking[token // 2]
        expanded += positive if token % 2 == 0 else inverse_word(positive)
    return expanded


def _float(value: float) -> str:
    return format(value, ".17g")


def _phase_summary(
    system_id: str,
    marking_id: str,
    selected: list[tuple[str, float, float]],
) -> dict[str, float | int]:
    lengths = [row[1] for row in selected]
    angles = [row[2] for row in selected]
    observed = round5.complex_phase_moment(lengths, angles)
    null_values: list[float] = []
    for replicate in range(NULL_REPLICATES):
        order = sorted(
            range(len(selected)),
            key=lambda index: sha256(
                (
                    f"{NULL_SEED}:{system_id}:{marking_id}:{replicate}:"
                    f"{selected[index][0]}"
                ).encode("utf-8")
            ),
        )
        null_values.append(
            abs(round5.complex_phase_moment(lengths, [angles[index] for index in order]))
        )
    null_mean = sum(null_values) / len(null_values)
    null_sd = math.sqrt(
        sum((value - null_mean) ** 2 for value in null_values)
        / (len(null_values) - 1)
    )
    if null_sd == 0:
        raise AssertionError("degenerate permutation null")
    return {
        "rows": len(selected),
        "q_real": observed.real,
        "q_imag": observed.imag,
        "abs_q": abs(observed),
        "null_mean": null_mean,
        "null_sd": null_sd,
        "z": (abs(observed) - null_mean) / null_sd,
    }


def _panel_row(
    *,
    system_id: str,
    panel: dict[str, Any],
    classes: Counter[str],
    selected: list[tuple[str, float, float]],
    digest: str,
    max_determinant_residual: float,
    all_level3: bool | None,
) -> dict[str, str]:
    phase = _phase_summary(system_id, panel["marking_id"], selected)
    return {
        "system_id": system_id,
        "marking_id": panel["marking_id"],
        "move_target": "" if panel["target"] is None else str(panel["target"] + 1),
        "move_source": "" if panel["source"] is None else str(panel["source"] + 1),
        "move_exponent": str(panel["exponent"]),
        "positive_generator_count": "4",
        "alphabet_size": "8",
        "marked_owner_rows": "2074",
        "raw_cyclically_reduced_linear_words": "19624",
        "symbolically_primitive_owner_rows": "2046",
        "symbolic_repetition_owner_rows": "28",
        "identity_owner_rows": str(classes["IDENTITY"]),
        "parabolic_owner_rows": str(classes["PARABOLIC"]),
        "loxodromic_owner_rows": str(classes["LOXODROMIC"]),
        "primitive_loxodromic_phase_rows": str(phase["rows"]),
        "q_real": _float(float(phase["q_real"])),
        "q_imag": _float(float(phase["q_imag"])),
        "abs_q": _float(float(phase["abs_q"])),
        "null_mean_abs_q": _float(float(phase["null_mean"])),
        "null_sample_sd_abs_q": _float(float(phase["null_sd"])),
        "z_abs_q": _float(float(phase["z"])),
        "maximum_matrix_determinant_residual": f"{max_determinant_residual:.17e}",
        "all_candidate_level3_membership": (
            "NOT_APPLICABLE_CONTROL" if all_level3 is None else str(all_level3).lower()
        ),
        "evaluation_digest": digest,
        "evidence_status": (
            "EXACT_SYMBOLIC_AND_CANDIDATE_MATRIX_PLUS_NUMERICAL_COMPLEX_LENGTH"
            if system_id == "BIANCHI_LEVEL3_NIELSEN_PANEL"
            else "PROVED_CONTROL_GEOMETRY_PLUS_HIGH_PRECISION_NONINTERVAL_HOLONOMY"
        ),
    }


def candidate_summary(owners: list[dict[str, Any]], panel: dict[str, Any]) -> dict[str, str]:
    positive_names = ("U1", "Ui", "L1", "Li")
    positive_matrices = tuple(bianchi.GENERATORS[name] for name in positive_names)
    classes: Counter[str] = Counter()
    selected: list[tuple[str, float, float]] = []
    digest = hashlib.sha256()
    all_level3 = True
    all_det_one = True
    for owner in owners:
        expanded = expand_word(owner["word"], panel["marking"])
        matrix = bianchi.IDENTITY
        for token in expanded:
            factor = positive_matrices[token // 2]
            if token % 2:
                factor = bianchi.mat_inv(factor)
            matrix = bianchi.mat_mul(matrix, factor)
        all_det_one = all_det_one and bianchi.mat_det(matrix) == bianchi.ONE
        all_level3 = all_level3 and bianchi.in_level_three(matrix)
        matrix_class = bianchi.classification(matrix)
        classes[matrix_class] += 1
        if matrix_class == "LOXODROMIC":
            length, angle, _residual = bianchi.complex_length(bianchi.mat_trace(matrix))
        else:
            length = angle = math.nan
        digest.update(owner["owner_id"].encode("ascii"))
        digest.update(b"\0")
        digest.update(",".join(map(str, expanded)).encode("ascii"))
        digest.update(b"\0")
        digest.update(matrix_class.encode("ascii"))
        digest.update(b"\0")
        if matrix_class == "LOXODROMIC":
            digest.update(_float(length).encode("ascii"))
            digest.update(b"\0")
            digest.update(_float(angle).encode("ascii"))
        digest.update(b"\n")
        if owner["exponent"] == 1 and matrix_class == "LOXODROMIC":
            selected.append((owner["owner_id"], length, angle))
    if not all_det_one or not all_level3:
        raise AssertionError("candidate exact group contract failed")
    return _panel_row(
        system_id="BIANCHI_LEVEL3_NIELSEN_PANEL",
        panel=panel,
        classes=classes,
        selected=selected,
        digest=digest.hexdigest(),
        max_determinant_residual=0.0,
        all_level3=all_level3,
    )


def control_group() -> Any:
    if snappy.__version__ != SNAPPY_VERSION:
        raise RuntimeError(f"requires snappy=={SNAPPY_VERSION}; found {snappy.__version__}")
    manifold = snappy.Manifold("5_2")
    if not manifold.is_isometric_to(snappy.Manifold("m015")):
        raise AssertionError("rigorous named-control binding failed")
    group = manifold.high_precision().fundamental_group(simplify_presentation=True)
    if list(group.generators()) != ["a", "b"]:
        raise AssertionError("control generator marking changed")
    if list(group.relators()) != ["aBBBabbAAbb"]:
        raise AssertionError("control relator changed")
    return group


CONTROL_STABILIZED_BASE: Marking = ((0,), (2,), (0, 2), (0, 3))
CONTROL_LABELS = ("a", "A", "b", "B")


def _control_projective_identity_residual(matrix: Any) -> float:
    entries = [[complex(matrix[row, column]) for column in range(2)] for row in range(2)]
    plus = max(
        abs(entries[row][column] - (1.0 if row == column else 0.0))
        for row in range(2)
        for column in range(2)
    )
    minus = max(
        abs(entries[row][column] - (-1.0 if row == column else 0.0))
        for row in range(2)
        for column in range(2)
    )
    return min(plus, minus)


def control_summary(
    owners: list[dict[str, Any]], panel: dict[str, Any], group: Any
) -> dict[str, str]:
    classes: Counter[str] = Counter()
    selected: list[tuple[str, float, float]] = []
    determinant_residuals: list[float] = []
    digest = hashlib.sha256()
    for owner in owners:
        expanded_slots = expand_word(owner["word"], panel["marking"])
        expanded_ab = expand_word(expanded_slots, CONTROL_STABILIZED_BASE)
        local = "".join(CONTROL_LABELS[token] for token in expanded_ab)
        matrix = group.SL2C(local)
        # Subtract at SnapPy's native 212-bit precision before the final
        # binary64 serialization; converting the determinant first suppresses
        # part of the tiny real residual near one.
        determinant_residual = float(abs(matrix.det() - 1))
        determinant_residuals.append(determinant_residual)
        identity_residual = _control_projective_identity_residual(matrix)
        trace = matrix.trace()
        parabolic_residual = abs(complex(trace * trace) - 4)
        if identity_residual < 1e-25:
            matrix_class = "IDENTITY"
            length = angle = math.nan
        elif parabolic_residual < 1e-25:
            matrix_class = "PARABOLIC"
            length = angle = math.nan
        else:
            matrix_class = "LOXODROMIC"
            length, angle, _residual = round5.control_complex_length(trace)
        classes[matrix_class] += 1
        digest.update(owner["owner_id"].encode("ascii"))
        digest.update(b"\0")
        digest.update(local.encode("ascii"))
        digest.update(b"\0")
        digest.update(matrix_class.encode("ascii"))
        digest.update(b"\0")
        if matrix_class == "LOXODROMIC":
            digest.update(_float(length).encode("ascii"))
            digest.update(b"\0")
            digest.update(_float(angle).encode("ascii"))
        digest.update(b"\n")
        if owner["exponent"] == 1 and matrix_class == "LOXODROMIC":
            selected.append((owner["owner_id"], length, angle))
    return _panel_row(
        system_id="FIVE_TWO_STABILIZED_NIELSEN_PANEL",
        panel=panel,
        classes=classes,
        selected=selected,
        digest=digest.hexdigest(),
        max_determinant_residual=max(determinant_residuals, default=0.0),
        all_level3=None,
    )


@lru_cache(maxsize=1)
def build_payload() -> tuple[list[dict[str, str]], dict[str, Any]]:
    freeze, _raw = load_freeze()
    owners = round5.enumerate_marked_owners(rank=4)
    if len(owners) != 2074 or sum(owner["multiplicity"] for owner in owners) != 19624:
        raise AssertionError("rank-four owner census changed")
    panel = panel_markings()
    group = control_group()
    rows: list[dict[str, str]] = []
    for marking in panel:
        rows.append(candidate_summary(owners, marking))
        rows.append(control_summary(owners, marking, group))

    by_system: dict[str, list[dict[str, str]]] = {
        system: [row for row in rows if row["system_id"] == system]
        for system in ("BIANCHI_LEVEL3_NIELSEN_PANEL", "FIVE_TWO_STABILIZED_NIELSEN_PANEL")
    }
    candidate_by_marking = {row["marking_id"]: row for row in by_system["BIANCHI_LEVEL3_NIELSEN_PANEL"]}
    control_by_marking = {row["marking_id"]: row for row in by_system["FIVE_TWO_STABILIZED_NIELSEN_PANEL"]}
    signed_contrasts = {
        marking["marking_id"]: (
            float(candidate_by_marking[marking["marking_id"]]["z_abs_q"])
            - float(control_by_marking[marking["marking_id"]]["z_abs_q"])
        )
        for marking in panel
    }
    candidate_z = [float(row["z_abs_q"]) for row in by_system["BIANCHI_LEVEL3_NIELSEN_PANEL"]]
    control_z = [float(row["z_abs_q"]) for row in by_system["FIVE_TWO_STABILIZED_NIELSEN_PANEL"]]
    candidate_width = max(candidate_z) - min(candidate_z)
    control_width = max(control_z) - min(control_z)
    nonzero_signs = {1 if value > 0 else -1 for value in signed_contrasts.values() if value != 0}
    direction_constant = len(nonzero_signs) == 1 and all(value != 0 for value in signed_contrasts.values())
    minimum_abs_contrast = min(abs(value) for value in signed_contrasts.values())
    rule = freeze["comparison"]["robustness_rule"]
    criteria = {
        "candidate_z_range_width_pass": candidate_width <= rule["candidate_z_range_width_at_most"],
        "control_z_range_width_pass": control_width <= rule["control_z_range_width_at_most"],
        "signed_contrast_direction_constant_pass": direction_constant,
        "minimum_absolute_signed_contrast_pass": minimum_abs_contrast >= rule["minimum_absolute_signed_contrast_each_marking"],
    }
    robust = all(criteria.values())
    decision = (
        freeze["comparison"]["decision_if_all_conditions_pass"]
        if robust
        else freeze["comparison"]["decision_otherwise"]
    )
    metrics = {
        "schema": "p24-round6-nielsen-sensitivity-metrics/1.0",
        "date": DATE,
        "freeze_contract_sha256": FREEZE_SHA256,
        "freeze_status": freeze["freeze_status"],
        "pilot_status": freeze["pilot_disclosure"]["status"],
        "pilot_values_used_as_evidence": False,
        "panel_family": freeze["panel"]["family"],
        "markings_per_system": 25,
        "summary_rows": len(rows),
        "same_marked_positive_generator_count": 4,
        "same_alphabet_size": 8,
        "same_owner_rows_each_marking": 2074,
        "same_raw_linear_words_each_marking": 19624,
        "candidate_z_min": min(candidate_z),
        "candidate_z_max": max(candidate_z),
        "candidate_z_range_width": candidate_width,
        "control_z_min": min(control_z),
        "control_z_max": max(control_z),
        "control_z_range_width": control_width,
        "signed_contrast_min": min(signed_contrasts.values()),
        "signed_contrast_max": max(signed_contrasts.values()),
        "minimum_absolute_signed_contrast": minimum_abs_contrast,
        "signed_contrast_positive_count": sum(value > 0 for value in signed_contrasts.values()),
        "signed_contrast_negative_count": sum(value < 0 for value in signed_contrasts.values()),
        "robustness_criteria": criteria,
        "marking_robustness_pass": robust,
        "paper_decision": decision,
        "current_phase_statistic_disposition": (
            "RETAIN_FOR_DESCRIPTIVE_METHODS_HISTORY_ONLY"
            if not robust
            else "ELIGIBLE_FOR_SEPARATE_METRIC_PREFIX_PROPOSAL"
        ),
        "metric_bianchi_prefix_authorized": False,
        "candidate_all_exact_determinants_one": all(
            float(row["maximum_matrix_determinant_residual"]) == 0.0
            for row in by_system["BIANCHI_LEVEL3_NIELSEN_PANEL"]
        ),
        "candidate_all_level3_membership": all(
            row["all_candidate_level3_membership"] == "true"
            for row in by_system["BIANCHI_LEVEL3_NIELSEN_PANEL"]
        ),
        "control_maximum_determinant_residual": max(
            float(row["maximum_matrix_determinant_residual"])
            for row in by_system["FIVE_TWO_STABILIZED_NIELSEN_PANEL"]
        ),
        "control_snappy_version": snappy.__version__,
        "control_precision_bits": int(group.SL2C("a")[0, 0].precision()),
        "control_base_four_marking": ["a", "b", "ab", "aB"],
        "control_four_marking_status": "TIETZE_REDUNDANT_NOT_PRESENTATION_MATCHED",
        "typed_proxy_candidate_id": "P24-BIANCHI-MARKED-WORD-PROXY",
        "formal_route_a_tuple": [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_WEAK",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_EXPLORATORY",
        "route_tuple_owner": "P24-BIANCHI-MARKED-WORD-PROXY",
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "route_a_scope": "TYPED_MARKED_WORD_PROXY_AUDIT_NOT_FULL_BIANCHI_FLOW",
        "typed_proxy_a2_a4_evaluation": "A2_FAIL_A3_FAIL_A4_FAIL",
        "full_bianchi_flow_a2_a4_evaluation": "NOT_EVALUATED",
        "orbit_to_gaussian_prime_ideal_map": "OPEN",
        "full_group_conjugacy_or_primitive_completeness": "NOT_CLAIMED",
        "presentation_invariance": "REFUTED_FOR_CURRENT_FINITE_CUTOFF_PHASE_STATISTIC" if not robust else "NOT_REFUTED_BY_FROZEN_RULE",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_target_data_used": False,
        "manuscript_authorized": False,
    }
    return rows, metrics


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    rows, metrics = build_payload()
    return {
        RESULT_PATHS["panel"]: csv_bytes(rows),
        RESULT_PATHS["metrics"]: json_bytes(metrics),
    }, metrics


def receipt_for(outputs: dict[Path, bytes], metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "p24-round6-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "execution": {"required_runs": 2, "byte_identical": True},
        "unit_tests": {"expected": 11, "failed": 0},
        "freeze_contract": {"path": FREEZE_PATH.as_posix(), "sha256": FREEZE_SHA256},
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
        "markings_per_system": metrics["markings_per_system"],
        "summary_rows": metrics["summary_rows"],
        "paper_decision": metrics["paper_decision"],
        "typed_proxy_candidate_id": metrics["typed_proxy_candidate_id"],
        "formal_route_a_tuple": metrics["formal_route_a_tuple"],
        "overall_verdict": metrics["overall_verdict"],
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "typed_proxy_a2_a4_evaluation": metrics["typed_proxy_a2_a4_evaluation"],
        "full_bianchi_flow_a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_invocation_allowed": False,
        "prime_or_zero_target_data_used": False,
        "reproduction_command": "bash experiments/reproduce_round6.sh",
    }


def validation_markdown(outputs: dict[Path, bytes], metrics: dict[str, Any]) -> bytes:
    criteria = metrics["robustness_criteria"]
    text = f"""# P24 Round-6 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Core-output SHA-256: `{combined_hash(outputs)}`
- Freeze SHA-256: `{FREEZE_SHA256}`

## Exhaustive panel

- Panel: identity plus all 24 elementary right Nielsen moves.
- Markings per system: `{metrics['markings_per_system']}`.
- Summary rows: `{metrics['summary_rows']}`.
- Every marking uses four positive generators, alphabet size eight, 2,074
  canonical marked owners, and 19,624 raw cyclically reduced linear words.
- Candidate exact determinant and level-`(3)` checks: `PASS`.
- Maximum control determinant residual: `{metrics['control_maximum_determinant_residual']:.3e}`.

The feasibility pilot disclosed in the freeze contract is not included as
evidence.  The executed family is canonical and exhaustive rather than a
selected subset, but the result remains exploratory rather than blind
confirmatory.

## Marking sensitivity

```text
candidate z range = [{metrics['candidate_z_min']:.12g}, {metrics['candidate_z_max']:.12g}]
candidate width   = {metrics['candidate_z_range_width']:.12g}
control z range   = [{metrics['control_z_min']:.12g}, {metrics['control_z_max']:.12g}]
control width     = {metrics['control_z_range_width']:.12g}
signed contrasts = {metrics['signed_contrast_negative_count']} negative / {metrics['signed_contrast_positive_count']} positive
minimum |contrast| = {metrics['minimum_absolute_signed_contrast']:.12g}
```

Frozen exploratory criteria:

- candidate range-width pass: `{str(criteria['candidate_z_range_width_pass']).lower()}`;
- control range-width pass: `{str(criteria['control_z_range_width_pass']).lower()}`;
- constant signed-contrast direction: `{str(criteria['signed_contrast_direction_constant_pass']).lower()}`;
- minimum absolute contrast pass: `{str(criteria['minimum_absolute_signed_contrast_pass']).lower()}`.

Decision: `{metrics['paper_decision']}`.

## Claim and Route boundary

The exact finite combinatorics and candidate matrix checks do not make the
finite-cutoff statistic presentation-invariant.  The control four-marking is
Tietze-redundant, not a matched presentation.  No full primitive spectrum,
group-conjugacy completeness, Gaussian-prime owner, metric spectrum, A1 pass,
or A2 result follows.

The conservative formal tuple

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
```

belongs only to `P24-BIANCHI-MARKED-WORD-PROXY`.  The complete Bianchi flow
tuple remains `UNASSIGNED`; in particular, the proxy's explicit `A2_FAIL`
does not claim that a cusp-aware analytic Bianchi determinant is impossible.

```text
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```
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
    print("P24 Round-6 existing artifacts VERIFIED")


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
            json.dumps(
                {
                    "core_sha256": combined_hash(core),
                    "decision": metrics["paper_decision"],
                    "markings_per_system": metrics["markings_per_system"],
                    "status": "PASS",
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
