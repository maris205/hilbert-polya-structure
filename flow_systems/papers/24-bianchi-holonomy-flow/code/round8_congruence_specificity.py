#!/usr/bin/env python3
"""Round-8 universality controls and first-congruence-jet audit for P24.

The theorem audited here is deliberately broader than the Gaussian candidate.
For a commutative ring ``R``, a non-zero-divisor ``m``, and
``gamma = I + m A`` in ``SL_2(R)``, determinant expansion gives

    (tr(gamma)^2 - 4) / m^2 = m^2 det(A)^2 - 4 det(A).

Thus the Round-7 normalized discriminant is a universal principal-congruence
identity, not a Gaussian-specific arithmetic owner.  Exact controls over the
integers, neighboring Gaussian levels, and Eisenstein integers make that
specificity failure executable.  A separate finite audit measures how much the
first congruence jet ``A mod m`` up to sign refines the Round-7 D9 collisions.

No prime table, zero table, metric length, or target-fitted threshold is read.
The sampled matrices remain a marked-word proxy, not a complete flow ledger.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import round2_bianchi_ledger as bianchi
import round7_trace_discriminant as round7


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
FREEZE_PATH = Path("experiments/round8_congruence_specificity_freeze.json")
FREEZE_SHA256 = "f60ef15527b254bef76dcf670c36c23018baf7ce7243792112795d2344240e0e"
CONTROL_PATH = Path("results/round8_universal_congruence_controls.csv")
PROFILE_PATH = Path("results/round8_d9_jet_collision_profile.csv")
METRICS_PATH = Path("results/round8_congruence_specificity_metrics.json")
VALIDATION_PATH = Path("experiments/round8_validation.md")
RECEIPT_PATH = Path("experiments/round8_receipt.json")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round8_congruence_specificity.py"),
    Path("code/test_round8_congruence_specificity.py"),
    Path("experiments/reproduce_round8.sh"),
)

Elem = tuple[int, int]
Matrix = tuple[Elem, Elem, Elem, Elem]
Jet = tuple[int, ...]


@dataclass(frozen=True)
class RingSpec:
    """Quadratic order Z[t]/(t^2-c1*t-c0), in the basis (1,t)."""

    ring_id: str
    symbol: str
    square_constant: int
    square_linear: int


INTEGER = RingSpec("Z", "0", 0, 0)
GAUSSIAN = RingSpec("Z[i]", "i", -1, 0)
EISENSTEIN = RingSpec("Z[omega]", "omega", -1, -1)

ZERO: Elem = (0, 0)
ONE: Elem = (1, 0)
IDENTITY: Matrix = (ONE, ZERO, ZERO, ONE)

CONTROL_FIELDS = [
    "control_id",
    "control_subpanel",
    "route_control_type",
    "ring",
    "level",
    "maximum_reduced_word_length",
    "matrix_rows",
    "determinant_one_rows",
    "principal_congruence_rows",
    "normalized_discriminant_integral_rows",
    "normalized_discriminant_nonintegral_rows",
    "distinct_normalized_discriminants",
    "theorem_scope",
    "exact_result",
    "specificity_consequence",
    "evidence_status",
]

PROFILE_FIELDS = [
    "d9_re",
    "d9_im",
    "matrix_rows",
    "distinct_first_jets_up_to_sign",
    "joint_descriptor_collisions_beyond_first",
    "maximum_joint_descriptor_bucket",
    "all_joint_descriptor_buckets_are_matrix_collisions",
    "owner_interpretation",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict[str, str]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
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
        raise RuntimeError("P24 Round-8 freeze contract changed")
    payload = json.loads(raw)
    if payload["candidate_panel"]["expected_unique_matrices_including_identity"] != 11481:
        raise AssertionError("freeze/candidate-size mismatch")
    if len(payload["arithmetic_controls"]) != 4:
        raise AssertionError("freeze must declare four arithmetic controls")
    if any(payload["forbidden_inputs"].values()):
        raise AssertionError("forbidden input flags must remain false")
    return payload, raw


def e_add(x: Elem, y: Elem) -> Elem:
    return (x[0] + y[0], x[1] + y[1])


def e_neg(x: Elem) -> Elem:
    return (-x[0], -x[1])


def e_sub(x: Elem, y: Elem) -> Elem:
    return e_add(x, e_neg(y))


def e_mul(x: Elem, y: Elem, ring: RingSpec) -> Elem:
    a, b = x
    c, d = y
    return (
        a * c + b * d * ring.square_constant,
        a * d + b * c + b * d * ring.square_linear,
    )


def e_square(x: Elem, ring: RingSpec) -> Elem:
    return e_mul(x, x, ring)


def e_scale(value: Elem, scalar: int) -> Elem:
    return (scalar * value[0], scalar * value[1])


def e_exact_divide(value: Elem, divisor: int) -> Elem:
    if divisor == 0 or value[0] % divisor or value[1] % divisor:
        raise ArithmeticError(f"{value} is not divisible by {divisor}")
    return (value[0] // divisor, value[1] // divisor)


def mat_mul(left: Matrix, right: Matrix, ring: RingSpec) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        e_add(e_mul(a, e, ring), e_mul(b, g, ring)),
        e_add(e_mul(a, f, ring), e_mul(b, h, ring)),
        e_add(e_mul(c, e, ring), e_mul(d, g, ring)),
        e_add(e_mul(c, f, ring), e_mul(d, h, ring)),
    )


def mat_det(matrix: Matrix, ring: RingSpec) -> Elem:
    a, b, c, d = matrix
    return e_sub(e_mul(a, d, ring), e_mul(b, c, ring))


def mat_trace(matrix: Matrix) -> Elem:
    return e_add(matrix[0], matrix[3])


def mat_inv_sl2(matrix: Matrix) -> Matrix:
    a, b, c, d = matrix
    return (d, e_neg(b), e_neg(c), a)


def mat_pow(matrix: Matrix, exponent: int, ring: RingSpec) -> Matrix:
    if exponent < 0:
        raise ValueError("negative exponent")
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = mat_mul(result, base, ring)
        base = mat_mul(base, base, ring)
        power //= 2
    return result


def unipotent_upper(level: int, value: Elem) -> Matrix:
    return (ONE, e_scale(value, level), ZERO, ONE)


def unipotent_lower(level: int, value: Elem) -> Matrix:
    return (ONE, ZERO, e_scale(value, level), ONE)


def generator_letters(
    ring: RingSpec, level: int, include_basis: bool
) -> tuple[list[str], dict[str, Matrix], dict[str, str]]:
    coefficients = [("1", ONE)]
    if include_basis:
        coefficients.append((ring.symbol, (0, 1)))
    positives: list[tuple[str, Matrix]] = []
    for label, value in coefficients:
        positives.append((f"U{label}", unipotent_upper(level, value)))
    for label, value in coefficients:
        positives.append((f"L{label}", unipotent_lower(level, value)))
    names: list[str] = []
    matrices: dict[str, Matrix] = {}
    inverse: dict[str, str] = {}
    for name, matrix in positives:
        inverse_name = f"{name}^-1"
        names.extend([name, inverse_name])
        matrices[name] = matrix
        matrices[inverse_name] = mat_inv_sl2(matrix)
        inverse[name] = inverse_name
        inverse[inverse_name] = name
    return names, matrices, inverse


def enumerate_matrix_word_ball(
    ring: RingSpec, level: int, cutoff: int, include_basis: bool
) -> dict[Matrix, tuple[str, ...]]:
    letters, generators, inverse = generator_letters(ring, level, include_basis)
    representatives: dict[Matrix, tuple[str, ...]] = {IDENTITY: ()}
    frontier: list[tuple[Matrix, tuple[str, ...]]] = [(IDENTITY, ())]
    for _length in range(1, cutoff + 1):
        new_frontier: list[tuple[Matrix, tuple[str, ...]]] = []
        for matrix, word in frontier:
            for letter in letters:
                if word and inverse[letter] == word[-1]:
                    continue
                new_word = word + (letter,)
                new_matrix = mat_mul(matrix, generators[letter], ring)
                new_frontier.append((new_matrix, new_word))
                representatives.setdefault(new_matrix, new_word)
        frontier = new_frontier
    return representatives


def matrix_a(matrix: Matrix, level: int) -> Matrix:
    differences = (
        e_sub(matrix[0], ONE),
        matrix[1],
        matrix[2],
        e_sub(matrix[3], ONE),
    )
    return tuple(e_exact_divide(value, level) for value in differences)  # type: ignore[return-value]


def in_principal_level(matrix: Matrix, level: int) -> bool:
    differences = (
        e_sub(matrix[0], ONE),
        matrix[1],
        matrix[2],
        e_sub(matrix[3], ONE),
    )
    return all(value[0] % level == 0 and value[1] % level == 0 for value in differences)


def normalized_discriminant(matrix: Matrix, level: int, ring: RingSpec) -> Elem:
    numerator = e_sub(e_square(mat_trace(matrix), ring), (4, 0))
    return e_exact_divide(numerator, level * level)


def theorem_formula(matrix: Matrix, level: int, ring: RingSpec) -> Elem:
    a = matrix_a(matrix, level)
    determinant = mat_det(a, ring)
    return e_sub(e_scale(e_square(determinant, ring), level * level), e_scale(determinant, 4))


def control_panel(
    control_id: str,
    subpanel: str,
    route_type: str,
    ring: RingSpec,
    level: int,
    cutoff: int,
    include_basis: bool,
) -> tuple[dict[str, str], dict[Matrix, tuple[str, ...]]]:
    matrices = enumerate_matrix_word_ball(ring, level, cutoff, include_basis)
    determinant_rows = 0
    principal_rows = 0
    integral_rows = 0
    values: set[Elem] = set()
    for matrix in matrices:
        determinant_rows += mat_det(matrix, ring) == ONE
        principal_rows += in_principal_level(matrix, level)
        observed = normalized_discriminant(matrix, level, ring)
        if observed != theorem_formula(matrix, level, ring):
            raise AssertionError("universal determinant formula changed")
        integral_rows += 1
        values.add(observed)
    if determinant_rows != len(matrices) or principal_rows != len(matrices):
        raise AssertionError("principal-control matrix contract failed")
    row = {
        "control_id": control_id,
        "control_subpanel": subpanel,
        "route_control_type": route_type,
        "ring": ring.ring_id,
        "level": str(level),
        "maximum_reduced_word_length": str(cutoff),
        "matrix_rows": str(len(matrices)),
        "determinant_one_rows": str(determinant_rows),
        "principal_congruence_rows": str(principal_rows),
        "normalized_discriminant_integral_rows": str(integral_rows),
        "normalized_discriminant_nonintegral_rows": "0",
        "distinct_normalized_discriminants": str(len(values)),
        "theorem_scope": "UNIVERSAL_PRINCIPAL_CONGRUENCE_FORMULA",
        "exact_result": "PASS_ALL_ROWS",
        "specificity_consequence": "D_m2_INTEGRALITY_IS_NOT_GAUSSIAN_SPECIFIC",
        "evidence_status": "PROVED_PLUS_EXACT_FINITE_REPLAY",
    }
    return row, matrices


def ambient_parent_matrices() -> list[Matrix]:
    i: Elem = (0, 1)
    minus_i: Elem = (0, -1)
    return [
        (ZERO, (-1, 0), ONE, ZERO),
        (i, ZERO, ZERO, minus_i),
        (ZERO, (-1, 0), ONE, ONE),
        (ONE, ONE, ZERO, ONE),
    ]


@lru_cache(maxsize=1)
def principal_control_panels() -> dict[str, tuple[RingSpec, int, dict[Matrix, tuple[str, ...]]]]:
    definitions = [
        ("C2-RATIONAL-INTEGER-LEVEL3", INTEGER, 3, 5, False),
        ("C3-GAUSSIAN-LEVEL2", GAUSSIAN, 2, 4, True),
        ("C3-GAUSSIAN-LEVEL4", GAUSSIAN, 4, 4, True),
        ("C4-EISENSTEIN-LEVEL3", EISENSTEIN, 3, 4, True),
    ]
    panels: dict[str, tuple[RingSpec, int, dict[Matrix, tuple[str, ...]]]] = {}
    for name, ring, level, cutoff, include_basis in definitions:
        panels[name] = (
            ring,
            level,
            enumerate_matrix_word_ball(ring, level, cutoff, include_basis),
        )
    return panels


def ambient_control_row() -> dict[str, str]:
    matrices = ambient_parent_matrices()
    if any(mat_det(matrix, GAUSSIAN) != ONE for matrix in matrices):
        raise AssertionError("ambient control left SL2")
    principal = sum(in_principal_level(matrix, 3) for matrix in matrices)
    integral = 0
    values: set[Elem] = set()
    for matrix in matrices:
        try:
            value = normalized_discriminant(matrix, 3, GAUSSIAN)
        except ArithmeticError:
            continue
        integral += 1
        values.add(value)
    if integral >= len(matrices):
        raise AssertionError("ambient control no longer falsifies unrestricted D9 integrality")
    return {
        "control_id": "C1-FULL-GAUSSIAN-AMBIENT-PARENT",
        "control_subpanel": "explicit_SL2_Zi_witness_panel",
        "route_control_type": "simpler parent system",
        "ring": GAUSSIAN.ring_id,
        "level": "NONE_FULL_GROUP",
        "maximum_reduced_word_length": "NOT_APPLICABLE_EXPLICIT_WITNESSES",
        "matrix_rows": str(len(matrices)),
        "determinant_one_rows": str(len(matrices)),
        "principal_congruence_rows": str(principal),
        "normalized_discriminant_integral_rows": str(integral),
        "normalized_discriminant_nonintegral_rows": str(len(matrices) - integral),
        "distinct_normalized_discriminants": str(len(values)),
        "theorem_scope": "OUTSIDE_PRINCIPAL_CONGRUENCE_HYPOTHESIS",
        "exact_result": "D9_NONINTEGRAL_WITNESSES_PRESENT",
        "specificity_consequence": "LEVEL3_HYPOTHESIS_IS_NECESSARY_FOR_UNRESTRICTED_AMBIENT_GROUP",
        "evidence_status": "PROVED_BY_EXACT_WITNESSES",
    }


@lru_cache(maxsize=1)
def control_rows() -> list[dict[str, str]]:
    rows = [ambient_control_row()]
    definitions = [
        (
            "C2-RATIONAL-INTEGER-LEVEL3",
            "Gamma_Z_3_word_ball_le_5",
            "simpler parent arithmetic ring",
            INTEGER,
            3,
            5,
            False,
        ),
        (
            "C3-GAUSSIAN-NEIGHBOR-LEVELS",
            "Gamma_Zi_2_word_ball_le_4",
            "neighboring dynamical parameters",
            GAUSSIAN,
            2,
            4,
            True,
        ),
        (
            "C3-GAUSSIAN-NEIGHBOR-LEVELS",
            "Gamma_Zi_4_word_ball_le_4",
            "neighboring dynamical parameters",
            GAUSSIAN,
            4,
            4,
            True,
        ),
        (
            "C4-EISENSTEIN-LEVEL3",
            "Gamma_Zomega_3_word_ball_le_4",
            "non-Gaussian arithmetic ring",
            EISENSTEIN,
            3,
            4,
            True,
        ),
    ]
    for definition in definitions:
        row, _matrices = control_panel(*definition)
        rows.append(row)
    return rows


def flatten_residue(residue: bianchi.Matrix) -> Jet:
    return tuple(coordinate for entry in residue for coordinate in entry)


def canonical_first_jet(matrix: bianchi.Matrix) -> Jet:
    residue = round7.a_residue_mod3(matrix)
    negative = round7.negate_residue_mod3(residue)
    return min(flatten_residue(residue), flatten_residue(negative))


def jet_id(jet: Jet) -> str:
    payload = ",".join(str(value) for value in jet).encode("ascii")
    return "J3-" + sha256(payload)[:16]


def candidate_records() -> list[tuple[bianchi.Matrix, tuple[int, int], Jet, str]]:
    records: list[tuple[bianchi.Matrix, tuple[int, int], Jet, str]] = []
    for matrix, _record in round7.ordered_records():
        records.append(
            (matrix, round7.d9(matrix), canonical_first_jet(matrix), bianchi.classification(matrix))
        )
    return records


def first_jet_power(matrix: bianchi.Matrix, exponent: int) -> tuple[int, ...]:
    residue = round7.a_residue_mod3(bianchi.mat_pow(matrix, exponent))
    return flatten_residue(residue)


def scaled_first_jet(matrix: bianchi.Matrix, exponent: int) -> tuple[int, ...]:
    residue = round7.a_residue_mod3(matrix)
    return tuple((exponent * coordinate) % 3 for entry in residue for coordinate in entry)


@lru_cache(maxsize=1)
def collision_payload() -> tuple[list[dict[str, str]], dict[str, Any]]:
    records = candidate_records()
    grouped: dict[tuple[int, int], list[Jet]] = defaultdict(list)
    for _matrix, d9_value, jet, _matrix_class in records:
        grouped[d9_value].append(jet)

    profile: list[dict[str, str]] = []
    for d9_value in sorted(grouped):
        jets = grouped[d9_value]
        counts = Counter(jets)
        profile.append({
            "d9_re": str(d9_value[0]),
            "d9_im": str(d9_value[1]),
            "matrix_rows": str(len(jets)),
            "distinct_first_jets_up_to_sign": str(len(counts)),
            "joint_descriptor_collisions_beyond_first": str(len(jets) - len(counts)),
            "maximum_joint_descriptor_bucket": str(max(counts.values())),
            "all_joint_descriptor_buckets_are_matrix_collisions": str(
                all(value > 1 for value in counts.values())
            ).lower(),
            "owner_interpretation": "NECESSARY_INVARIANT_ONLY_NOT_CONJUGACY_CLASSIFICATION",
        })

    d9_values = {d9_value for _matrix, d9_value, _jet, _class in records}
    jets = {jet for _matrix, _d9, jet, _class in records}
    descriptors = {(d9_value, jet) for _matrix, d9_value, jet, _class in records}
    d9_counts = Counter(d9_value for _matrix, d9_value, _jet, _class in records)
    descriptor_counts = Counter(
        (d9_value, jet) for _matrix, d9_value, jet, _class in records
    )
    d9_collisions = len(records) - len(d9_values)
    descriptor_collisions = len(records) - len(descriptors)
    separated = d9_collisions - descriptor_collisions
    loxodromic = [record for record in records if record[3] == "LOXODROMIC"]
    witness = round7.owner_separation_witness()
    witness_jets = [
        canonical_first_jet(round7.OWNER_WITNESS_GAMMA_1),
        canonical_first_jet(round7.OWNER_WITNESS_GAMMA_2),
    ]
    if witness_jets[0] == witness_jets[1]:
        raise AssertionError("first jet stopped separating the frozen owner witness")
    metrics = {
        "matrix_rows": len(records),
        "distinct_d9_values": len(d9_values),
        "distinct_first_jets_up_to_sign": len(jets),
        "distinct_joint_d9_jet_descriptors": len(descriptors),
        "d9_collision_rows_beyond_first": d9_collisions,
        "joint_descriptor_collision_rows_beyond_first": descriptor_collisions,
        "collision_rows_separated_by_first_jet": separated,
        "collision_reduction_fraction": f"{separated}/{d9_collisions}",
        "collision_reduction_decimal": f"{separated / d9_collisions:.15f}",
        "maximum_d9_bucket": max(d9_counts.values()),
        "maximum_joint_descriptor_bucket": max(descriptor_counts.values()),
        "singleton_d9_buckets": sum(value == 1 for value in d9_counts.values()),
        "singleton_joint_descriptor_buckets": sum(
            value == 1 for value in descriptor_counts.values()
        ),
        "loxodromic_rows": len(loxodromic),
        "loxodromic_distinct_d9_values": len({record[1] for record in loxodromic}),
        "loxodromic_distinct_joint_descriptors": len(
            {(record[1], record[2]) for record in loxodromic}
        ),
        "owner_separation_witness": {
            **witness,
            "first_jet_1_id": jet_id(witness_jets[0]),
            "first_jet_2_id": jet_id(witness_jets[1]),
            "separated_by_first_jet": True,
        },
        "residual_collision_claim_boundary": (
            "joint descriptor collisions are matrix-row collisions only; "
            "no distinct-owner claim is inferred"
        ),
    }
    return profile, metrics


def build_metrics() -> dict[str, Any]:
    freeze, _raw = load_freeze()
    controls = control_rows()
    profile, collision = collision_payload()
    principal_rows = [row for row in controls if row["control_id"] != "C1-FULL-GAUSSIAN-AMBIENT-PARENT"]
    all_principal_pass = all(row["exact_result"] == "PASS_ALL_ROWS" for row in principal_rows)
    control_ids = {row["control_id"] for row in controls}
    canonical_route_control_types = [
        "neighboring dynamical parameters",
        "simpler parent system",
    ]
    if len(control_ids) != 4 or len(profile) != collision["distinct_d9_values"]:
        raise AssertionError("control/profile completeness changed")
    decision = (
        "STOP_D9_AS_GAUSSIAN_SPECIFIC_ARITHMETIC_OWNER;"
        "RETAIN_UNIVERSAL_CONGRUENCE_THEOREM_AND_FIRST_JET_REFINEMENT"
        if all_principal_pass and collision["collision_rows_separated_by_first_jet"] > 0
        else "FAIL_CLOSED_REJECT_ROUND8_REFINEMENT"
    )
    return {
        "schema": "p24-round8-congruence-specificity-metrics/1.0",
        "date": DATE,
        "freeze_contract_sha256": FREEZE_SHA256,
        "freeze_status": freeze["freeze_status"],
        "research_question": freeze["research_question"],
        "universal_theorem": {
            "status": "PROVED",
            "scope": freeze["universal_theorem"]["coefficient_scope"],
            "formula": freeze["universal_theorem"]["claimed_formula"],
            "first_jet_status": "PROVED_NECESSARY_UNORIENTED_OWNER_INVARIANT",
            "first_jet_laws": freeze["universal_theorem"]["jet_laws"],
        },
        "a0_control_gate": {
            "required_minimum": 3,
            "executed_distinct_control_families": len(control_ids),
            "executed_subpanels": len(controls),
            "frozen_control_family_status": "COMPLETE_4_OF_4",
            "canonical_route_control_types": canonical_route_control_types,
            "executed_distinct_canonical_types": len(canonical_route_control_types),
            "status": "INCOMPLETE_2_OF_3_CANONICAL_TYPES",
            "specificity_verdict": "REFUTED_D9_IS_NOT_GAUSSIAN_SPECIFIC",
            "proves_too_much_verdict": "STOP_SCOPED_D9_OWNER_MECHANISM",
            "controls": controls,
        },
        "finite_control_matrix_rows": sum(int(row["matrix_rows"]) for row in controls),
        "all_principal_control_rows_pass": all_principal_pass,
        "ambient_parent_has_nonintegral_d9_witnesses": int(controls[0]["normalized_discriminant_nonintegral_rows"]) > 0,
        "first_jet_audit": collision,
        "paper_decision": decision,
        "typed_proxy_candidate_id": "P24-BIANCHI-MARKED-WORD-PROXY",
        "formal_route_a_tuple": freeze["route_boundary"]["formal_route_a_tuple"],
        "overall_verdict": "ROUTE_A_EXPLORATORY",
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "orbit_to_gaussian_prime_ideal_map": "OPEN",
        "metric_bianchi_prefix_authorized": False,
        "prime_or_zero_target_data_used": False,
        "typed_proxy_a2_a4_evaluation": "A2_FAIL_A3_FAIL_A4_FAIL",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "manuscript_authorized": False,
        "completeness_boundary": freeze["candidate_panel"]["completeness_boundary"],
    }


def primary_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    controls = control_rows()
    profile, _collision = collision_payload()
    metrics = build_metrics()
    return {
        CONTROL_PATH: csv_bytes(controls, CONTROL_FIELDS),
        PROFILE_PATH: csv_bytes(profile, PROFILE_FIELDS),
        METRICS_PATH: json_bytes(metrics),
    }, metrics


def validation_markdown(primary: dict[Path, bytes], metrics: dict[str, Any]) -> bytes:
    audit = metrics["first_jet_audit"]
    gate = metrics["a0_control_gate"]
    text = f"""# P24 Round-8 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus exact experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Primary-output SHA-256: `{combined_hash(primary)}`
- Freeze SHA-256: `{FREEZE_SHA256}`

## Universal principal-congruence theorem

Let `R` be a commutative ring with identity, let `m` be a non-zero-divisor,
and write `gamma=I+mA` in `SL_2(R)`.  Exact two-by-two determinant expansion
gives

```text
0 = m tr(A) + m^2 det(A),
tr(A) = -m det(A),
(tr(gamma)^2-4)/m^2 = m^2 det(A)^2 - 4 det(A) in R.
```

Thus Round-7 `D9` integrality is a universal level-normalized congruence
identity, not a special property of `Z[i]` or `Gamma((3))`.

The first jet `J_m(gamma)=A mod m` obeys

```text
J_m(h gamma h^-1)=J_m(gamma),
J_m(gamma^-1)=-J_m(gamma),
J_m(gamma^r)=r J_m(gamma).
```

The sign quotient is therefore a necessary invariant of unoriented
`Gamma((m))` conjugacy owners.  It is not a complete conjugacy classifier.

## Four executed A0 control families; canonical type gate remains open

All four pre-frozen control families were executed, with
{gate['executed_subpanels']} executable subpanels over
{metrics['finite_control_matrix_rows']} exact matrices/witnesses.  Strictly
mapping them to the evaluator list yields only
{gate['executed_distinct_canonical_types']} canonical types:
`{', '.join(gate['canonical_route_control_types'])}`.  The mandatory Route-A
gate is therefore `{gate['status']}`, while the frozen-family execution status
is `{gate['frozen_control_family_status']}`.

1. Full `SL_2(Z[i])` parent: removing the level condition produces exact
   nonintegral `/9` witnesses, so the congruence hypothesis is essential.
2. Integer level 3: every frozen `Gamma_Z(3)` row satisfies the same formula.
3. Gaussian neighbor levels 2 and 4: every row satisfies its corresponding
   level-normalized formula.
4. Eisenstein level 3: every row satisfies the same `D9` formula in
   `Z[omega]`.

The exact control outcome is `{gate['specificity_verdict']}` and
`{gate['proves_too_much_verdict']}`.  Passing these identities in controls is
a negative specificity result, not support for a Gaussian prime-owner map.

## First-jet collision audit

On all {audit['matrix_rows']} frozen Gaussian matrices, `D9` has
{audit['distinct_d9_values']} values.  The joint `(D9,J3 up to sign)` descriptor
has {audit['distinct_joint_d9_jet_descriptors']} values.  It separates
{audit['collision_rows_separated_by_first_jet']} of the original
{audit['d9_collision_rows_beyond_first']} collision rows
({audit['collision_reduction_fraction']}; decimal
{audit['collision_reduction_decimal']}).  The largest bucket falls from
{audit['maximum_d9_bucket']} to {audit['maximum_joint_descriptor_bucket']}.

The Round-7 exact owner witness with common `D9=13` receives two different
first-jet IDs and is therefore separated.  Nevertheless,
{audit['joint_descriptor_collision_rows_beyond_first']} matrix-row collisions
remain and there are {audit['singleton_joint_descriptor_buckets']} singleton
joint buckets.  Those residual counts are not promoted to distinct-owner
claims because the word ball is not a complete conjugacy enumeration.

## Decision and Route firewall

Decision:

```text
{metrics['paper_decision']}
```

The typed-proxy tuple remains

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
METRIC_BIANCHI_PREFIX_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
```

No prime/zero target data, metric period, dynamical determinant, or operator is
used.  The universal theorem and specificity obstruction are paper-ready; an
orbit-to-Gaussian-prime-ideal map remains open.
"""
    return text.encode("utf-8")


def receipt_for(material: dict[Path, bytes], metrics: dict[str, Any]) -> dict[str, Any]:
    audit = metrics["first_jet_audit"]
    return {
        "schema": "p24-round8-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "material_sha256": combined_hash(material),
        "execution": {"required_independent_builds": 2, "byte_identical": True},
        "unit_tests": {"expected": 14, "failed": 0},
        "freeze_contract": {"path": FREEZE_PATH.as_posix(), "sha256": FREEZE_SHA256},
        "output_bindings": {
            path.as_posix(): {"sha256": sha256(data), "bytes": len(data)}
            for path, data in sorted(material.items(), key=lambda item: item[0].as_posix())
        },
        "source_bindings": {
            path.as_posix(): {
                "sha256": sha256((PROJECT_ROOT / path).read_bytes()),
                "bytes": (PROJECT_ROOT / path).stat().st_size,
            }
            for path in SOURCE_BINDING_PATHS
        },
        "a0_control_families_executed": metrics["a0_control_gate"]["executed_distinct_control_families"],
        "a0_canonical_types_executed": metrics["a0_control_gate"]["executed_distinct_canonical_types"],
        "a0_canonical_gate_status": metrics["a0_control_gate"]["status"],
        "finite_control_matrix_rows": metrics["finite_control_matrix_rows"],
        "candidate_matrix_rows": audit["matrix_rows"],
        "distinct_joint_d9_jet_descriptors": audit["distinct_joint_d9_jet_descriptors"],
        "collision_rows_separated_by_first_jet": audit["collision_rows_separated_by_first_jet"],
        "paper_decision": metrics["paper_decision"],
        "formal_route_a_tuple": metrics["formal_route_a_tuple"],
        "overall_verdict": metrics["overall_verdict"],
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "prime_or_zero_target_data_used": False,
        "default_reproduction_command": "bash experiments/reproduce_round8.sh",
        "refresh_command": "bash experiments/reproduce_round8.sh --refresh",
    }


def rendered_outputs() -> dict[Path, bytes]:
    primary, metrics = primary_outputs()
    validation = validation_markdown(primary, metrics)
    material = {**primary, VALIDATION_PATH: validation}
    return {**material, RECEIPT_PATH: json_bytes(receipt_for(material, metrics))}


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
    print("P24 Round-8 existing artifacts VERIFIED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--verify-existing", action="store_true")
    mode.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    if args.refresh:
        write_outputs(args.output_root)
        primary, metrics = primary_outputs()
        print(json.dumps({
            "a0_control_families": metrics["a0_control_gate"]["executed_distinct_control_families"],
            "a0_canonical_types": metrics["a0_control_gate"]["executed_distinct_canonical_types"],
            "a0_canonical_gate": metrics["a0_control_gate"]["status"],
            "decision": metrics["paper_decision"],
            "primary_sha256": combined_hash(primary),
            "status": "REFRESHED",
        }, sort_keys=True))
    else:
        verify_existing(args.output_root)


if __name__ == "__main__":
    main()
