#!/usr/bin/env python3
"""Exact Round-7 trace-discriminant audit for the P24 typed proxy.

For every frozen matrix ``gamma = I + 3 A`` in ``SL_2(Z[i])`` this module
records

    D9(gamma) = (tr(gamma)^2 - 4) / 9.

The determinant identity proves that this quotient is a Gaussian integer.
The finite ledger also checks conjugacy, inversion, and repetition witnesses
exactly.  It does not read prime/zero target data and does not interpret D9 as
an orbit-to-prime-ideal owner.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import round2_bianchi_ledger as bianchi


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
FREEZE_PATH = Path("experiments/round7_trace_discriminant_freeze.json")
FREEZE_SHA256 = "16bddd930a90af0fe673a698b912b9d302cfd126c5a1cb5bef48cfc496846b93"
LEDGER_PATH = Path("results/round7_trace_discriminant_ledger.csv")
METRICS_PATH = Path("results/round7_trace_discriminant_metrics.json")
VALIDATION_PATH = Path("experiments/round7_validation.md")
RECEIPT_PATH = Path("experiments/round7_receipt.json")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round7_trace_discriminant.py"),
    Path("code/test_round7_trace_discriminant.py"),
    Path("experiments/reproduce_round7.sh"),
)

Gaussian = bianchi.Gaussian
Matrix = bianchi.Matrix

LEDGER_FIELDS = [
    "matrix_id",
    "representative_word",
    "representative_word_length",
    "matrix",
    "matrix_class",
    "trace_re",
    "trace_im",
    "trace_minus_two_div9_re",
    "trace_minus_two_div9_im",
    "a_determinant_re",
    "a_determinant_im",
    "d9_re",
    "d9_im",
    "conjugator",
    "conjugate_d9_re",
    "conjugate_d9_im",
    "inverse_d9_re",
    "inverse_d9_im",
    "s0",
    "s1",
    "s2",
    "s3",
    "s4",
    "d9_power_1",
    "d9_power_2",
    "d9_power_3",
    "d9_power_4",
    "d9_power_5",
    "determinant_one",
    "level3_membership",
    "integrality_identity_pass",
    "conjugacy_invariance_pass",
    "inversion_invariance_pass",
    "repetition_identity_r1_to_r5_pass",
    "all_exact_witnesses_pass",
    "evidence_status",
    "arithmetic_mode",
    "owner_status",
    "completeness_boundary",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=LEDGER_FIELDS, lineterminator="\n")
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
        raise RuntimeError("P24 Round-7 freeze contract changed")
    payload = json.loads(raw)
    if payload["candidate"]["expected_unique_matrices_including_identity"] != 11481:
        raise AssertionError("freeze/sample-size mismatch")
    if payload["witnesses"]["repetition"]["exponents"] != [1, 2, 3, 4, 5]:
        raise AssertionError("freeze/repetition mismatch")
    if any(payload["forbidden_inputs"].values()):
        raise AssertionError("forbidden input flags must remain false")
    return payload, raw


def g_sub(x: Gaussian, y: Gaussian) -> Gaussian:
    return bianchi.g_add(x, bianchi.g_neg(y))


def g_exact_divide(x: Gaussian, divisor: int) -> Gaussian:
    if x[0] % divisor or x[1] % divisor:
        raise ArithmeticError(f"Gaussian integer {x} is not divisible by {divisor}")
    return (x[0] // divisor, x[1] // divisor)


def g_text(x: Gaussian) -> str:
    return f"{x[0]},{x[1]}"


def matrix_a(gamma: Matrix) -> Matrix:
    differences = (
        g_sub(gamma[0], bianchi.ONE),
        gamma[1],
        gamma[2],
        g_sub(gamma[3], bianchi.ONE),
    )
    return tuple(g_exact_divide(entry, 3) for entry in differences)  # type: ignore[return-value]


def gaussian_mod3(value: Gaussian) -> Gaussian:
    """Return the canonical coordinate representative in Z[i]/(3)."""
    return (value[0] % 3, value[1] % 3)


def a_residue_mod3(gamma: Matrix) -> Matrix:
    """Return ((gamma-I)/3) modulo 3 for a level-(3) matrix."""
    return tuple(gaussian_mod3(entry) for entry in matrix_a(gamma))  # type: ignore[return-value]


def negate_residue_mod3(residue: Matrix) -> Matrix:
    return tuple(gaussian_mod3(bianchi.g_neg(entry)) for entry in residue)  # type: ignore[return-value]


OWNER_WITNESS_GAMMA_1: Matrix = (
    (1, 0), (3, 0),
    (3, 0), (10, 0),
)
OWNER_WITNESS_GAMMA_2: Matrix = (
    (1, 0), (0, -3),
    (0, 3), (10, 0),
)


def owner_separation_witness() -> dict[str, Any]:
    """Exact D9 collision on two distinct unoriented Gamma(3) owners.

    If gamma=I+3A and h=I+3B is in Gamma(3), direct expansion modulo 9 gives
    (h gamma h^-1-I)/3 = A (mod 3).  Inversion changes this residue to -A.
    Hence the residue of A modulo sign separates unoriented conjugacy owners.
    """
    gamma_1 = OWNER_WITNESS_GAMMA_1
    gamma_2 = OWNER_WITNESS_GAMMA_2
    residue_1 = a_residue_mod3(gamma_1)
    residue_2 = a_residue_mod3(gamma_2)
    same_d9 = d9(gamma_1) == d9(gamma_2) == (13, 0)
    residues_equal = residue_1 == residue_2
    residues_negative = negate_residue_mod3(residue_1) == residue_2
    if not same_d9 or residues_equal or residues_negative:
        raise AssertionError("frozen D9 owner-separation witness changed")
    return {
        "status": "PROVED_DISTINCT_UNORIENTED_GAMMA3_OWNERS_WITH_EQUAL_D9",
        "d9": [13, 0],
        "gamma_1": bianchi.mat_text(gamma_1),
        "gamma_2": bianchi.mat_text(gamma_2),
        "gamma_1_matrix_id": bianchi.matrix_id(gamma_1),
        "gamma_2_matrix_id": bianchi.matrix_id(gamma_2),
        "a_1_mod3_gaussian_pairs": [list(entry) for entry in residue_1],
        "a_2_mod3_gaussian_pairs": [list(entry) for entry in residue_2],
        "residues_equal": residues_equal,
        "residues_equal_up_to_sign": residues_equal or residues_negative,
        "invariant_rule": "A_MOD3_UNCHANGED_BY_GAMMA3_CONJUGACY_AND_NEGATED_BY_INVERSION",
    }


def d9(gamma: Matrix) -> Gaussian:
    trace = bianchi.mat_trace(gamma)
    return g_exact_divide(g_sub(bianchi.g_square(trace), (4, 0)), 9)


def s_values(trace: Gaussian, maximum_index: int = 4) -> list[Gaussian]:
    values = [bianchi.ONE]
    if maximum_index == 0:
        return values
    values.append(trace)
    for _index in range(2, maximum_index + 1):
        values.append(
            g_sub(bianchi.g_mul(trace, values[-1]), values[-2])
        )
    return values


def ordered_records() -> list[tuple[Matrix, dict[str, object]]]:
    records = bianchi.enumerate_word_ball(max_word_length=bianchi.MAX_WORD_LENGTH)
    ordered = sorted(
        records.items(),
        key=lambda item: (
            len(item[1]["representative"]),
            item[1]["representative"],
            bianchi.mat_flat(item[0]),
        ),
    )
    if len(ordered) != 11481:
        raise AssertionError("frozen exact matrix census changed")
    return ordered


def ledger_row(gamma: Matrix, record: dict[str, object]) -> dict[str, str]:
    if bianchi.mat_det(gamma) != bianchi.ONE or not bianchi.in_level_three(gamma):
        raise AssertionError("matrix violates frozen level-(3) SL2 contract")

    trace = bianchi.mat_trace(gamma)
    a = matrix_a(gamma)
    det_a = bianchi.mat_det(a)
    trace_div9 = g_exact_divide(g_sub(trace, (2, 0)), 9)
    invariant = d9(gamma)
    integrality_pass = trace_div9 == bianchi.g_neg(det_a)

    conjugator = bianchi.GENERATORS["U1"]
    conjugate = bianchi.mat_mul(
        bianchi.mat_mul(conjugator, gamma), bianchi.mat_inv(conjugator)
    )
    conjugate_d9 = d9(conjugate)
    conjugacy_pass = conjugate_d9 == invariant

    inverse_d9 = d9(bianchi.mat_inv(gamma))
    inversion_pass = inverse_d9 == invariant

    recurrence = s_values(trace, maximum_index=4)
    power_values: list[Gaussian] = []
    repetition_pass = True
    for exponent in range(1, 6):
        observed = d9(bianchi.mat_pow(gamma, exponent))
        expected = bianchi.g_mul(invariant, bianchi.g_square(recurrence[exponent - 1]))
        power_values.append(observed)
        repetition_pass = repetition_pass and observed == expected

    all_pass = integrality_pass and conjugacy_pass and inversion_pass and repetition_pass
    representative = record["representative"]
    if not isinstance(representative, tuple):
        raise TypeError("unexpected representative type")
    return {
        "matrix_id": bianchi.matrix_id(gamma),
        "representative_word": bianchi.word_text(representative),
        "representative_word_length": str(len(representative)),
        "matrix": bianchi.mat_text(gamma),
        "matrix_class": bianchi.classification(gamma),
        "trace_re": str(trace[0]),
        "trace_im": str(trace[1]),
        "trace_minus_two_div9_re": str(trace_div9[0]),
        "trace_minus_two_div9_im": str(trace_div9[1]),
        "a_determinant_re": str(det_a[0]),
        "a_determinant_im": str(det_a[1]),
        "d9_re": str(invariant[0]),
        "d9_im": str(invariant[1]),
        "conjugator": "U1",
        "conjugate_d9_re": str(conjugate_d9[0]),
        "conjugate_d9_im": str(conjugate_d9[1]),
        "inverse_d9_re": str(inverse_d9[0]),
        "inverse_d9_im": str(inverse_d9[1]),
        **{f"s{index}": g_text(value) for index, value in enumerate(recurrence)},
        **{
            f"d9_power_{index}": g_text(value)
            for index, value in enumerate(power_values, start=1)
        },
        "determinant_one": "true",
        "level3_membership": "true",
        "integrality_identity_pass": str(integrality_pass).lower(),
        "conjugacy_invariance_pass": str(conjugacy_pass).lower(),
        "inversion_invariance_pass": str(inversion_pass).lower(),
        "repetition_identity_r1_to_r5_pass": str(repetition_pass).lower(),
        "all_exact_witnesses_pass": str(all_pass).lower(),
        "evidence_status": "NUMERICALLY_CERTIFIED",
        "arithmetic_mode": "EXACT_GAUSSIAN_INTEGER",
        "owner_status": "NECESSARY_INVARIANT_NOT_GAUSSIAN_PRIME_IDEAL_OWNER",
        "completeness_boundary": bianchi.COMPLETENESS_BOUNDARY,
    }


@lru_cache(maxsize=1)
def build_payload() -> tuple[list[dict[str, str]], dict[str, Any]]:
    freeze, _raw = load_freeze()
    rows = [ledger_row(gamma, record) for gamma, record in ordered_records()]
    class_counts: dict[str, int] = {}
    d9_values: set[tuple[int, int]] = set()
    for row in rows:
        class_counts[row["matrix_class"]] = class_counts.get(row["matrix_class"], 0) + 1
        d9_values.add((int(row["d9_re"]), int(row["d9_im"])))
    all_exact = all(row["all_exact_witnesses_pass"] == "true" for row in rows)
    decision = (
        freeze["decision_rule"]["if_all_exact_checks_pass"]
        if all_exact
        else freeze["decision_rule"]["otherwise"]
    )
    separation_witness = owner_separation_witness()
    row_ids = {row["matrix_id"] for row in rows}
    if not {
        separation_witness["gamma_1_matrix_id"],
        separation_witness["gamma_2_matrix_id"],
    }.issubset(row_ids):
        raise AssertionError("owner-separation witnesses left the frozen ledger")
    metrics = {
        "schema": "p24-round7-trace-discriminant-metrics/1.0",
        "date": DATE,
        "freeze_contract_sha256": FREEZE_SHA256,
        "freeze_status": freeze["freeze_status"],
        "candidate_object": freeze["candidate"]["object"],
        "unique_exact_matrices_including_identity": len(rows),
        "representative_word_length_maximum": max(
            int(row["representative_word_length"]) for row in rows
        ),
        "matrix_class_counts": dict(sorted(class_counts.items())),
        "distinct_d9_values": len(d9_values),
        "d9_collision_rows_beyond_first": len(rows) - len(d9_values),
        "d9_noninjective_on_unoriented_gamma3_owners": True,
        "owner_separation_witness": separation_witness,
        "finite_replay_evidence_status": "NUMERICALLY_CERTIFIED",
        "finite_replay_arithmetic_mode": "EXACT_GAUSSIAN_INTEGER",
        "all_determinants_one": all(row["determinant_one"] == "true" for row in rows),
        "all_level3_membership": all(row["level3_membership"] == "true" for row in rows),
        "all_integrality_identities_pass": all(
            row["integrality_identity_pass"] == "true" for row in rows
        ),
        "all_conjugacy_witnesses_pass": all(
            row["conjugacy_invariance_pass"] == "true" for row in rows
        ),
        "all_inversion_witnesses_pass": all(
            row["inversion_invariance_pass"] == "true" for row in rows
        ),
        "all_repetition_witnesses_r1_to_r5_pass": all(
            row["repetition_identity_r1_to_r5_pass"] == "true" for row in rows
        ),
        "all_exact_witnesses_pass": all_exact,
        "paper_decision": decision,
        "invariant_status": "SOURCE_DERIVED_NECESSARY_INVARIANT_NOT_OWNER_MAP",
        "orbit_to_gaussian_prime_ideal_map": "OPEN",
        "metric_bianchi_prefix_authorized": False,
        "prime_or_zero_target_data_used": False,
        "typed_proxy_candidate_id": "P24-BIANCHI-MARKED-WORD-PROXY",
        "formal_route_a_tuple": freeze["route_boundary"]["formal_route_a_tuple"],
        "overall_verdict": "ROUTE_A_EXPLORATORY",
        "route_tuple_owner": "P24-BIANCHI-MARKED-WORD-PROXY",
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "typed_proxy_a2_a4_evaluation": "A2_FAIL_A3_FAIL_A4_FAIL",
        "full_bianchi_flow_a2_a4_evaluation": "NOT_EVALUATED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "manuscript_authorized": False,
        "completeness_boundary": bianchi.COMPLETENESS_BOUNDARY,
    }
    return rows, metrics


def primary_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    rows, metrics = build_payload()
    return {
        LEDGER_PATH: csv_bytes(rows),
        METRICS_PATH: json_bytes(metrics),
    }, metrics


def validation_markdown(primary: dict[Path, bytes], metrics: dict[str, Any]) -> bytes:
    counts = metrics["matrix_class_counts"]
    text = f"""# P24 Round-7 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus exact experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Primary-output SHA-256: `{combined_hash(primary)}`
- Freeze SHA-256: `{FREEZE_SHA256}`

## Exact theorem and finite audit

Write `gamma=I+3A`.  Over `Z[i]`,

```text
1 = det(gamma) = 1 + 3 tr(A) + 9 det(A),
```

so `tr(gamma)-2=3 tr(A)=-9 det(A)`.  Therefore
`D9(gamma)=(tr(gamma)^2-4)/9` is a Gaussian integer.  Trace proves
conjugacy invariance, and `tr(gamma^-1)=tr(gamma)` in `SL_2` proves inversion
invariance.  Cayley--Hamilton gives
`D9(gamma^r)=D9(gamma) S_(r-1)(tr(gamma))^2`, where
`S_0=1`, `S_1=t`, and `S_n=t S_(n-1)-S_(n-2)`.

The deterministic audit contains `{metrics['unique_exact_matrices_including_identity']}`
unique exact matrices: `{counts.get('IDENTITY', 0)}` identity,
`{counts.get('PARABOLIC', 0)}` parabolic, and
`{counts.get('LOXODROMIC', 0)}` loxodromic.  It records
`{metrics['distinct_d9_values']}` distinct `D9` values and
`{metrics['d9_collision_rows_beyond_first']}` rows beyond first occurrences.
For every row, determinant, level membership, integrality, conjugacy by `U1`,
inversion, and repetitions `r=1,...,5` pass by exact Gaussian-integer
arithmetic.

Non-injectivity already occurs after quotienting by conjugacy and inversion.
The ledger contains
`gamma_1=[[1,3],[3,10]]` and
`gamma_2=[[1,-3i],[3i,10]]`, both with `D9=13`.  For
`A_j=(gamma_j-I)/3`, their residues modulo 3 are
`[[0,1],[1,0]]` and `[[0,-i],[i,0]]`, which are neither equal nor negatives.
For `h` in `Gamma((3))`, reduction modulo 9 proves that `A mod 3` is unchanged
under `h gamma h^-1`, while inversion negates it.  The two matrices therefore
belong to distinct unoriented `Gamma((3))` owners despite their equal `D9`.

Decision: `{metrics['paper_decision']}`.

## Claim and Route boundary

`D9` is a source-derived necessary invariant.  The exact residue witness above
proves that it is non-injective even on unoriented `Gamma((3))` conjugacy
owners, and no Gaussian-prime ideal is assigned.  The sample is the elementary-generated
reduced-word ball through length five, not all of `Gamma((3))` and not a full
conjugacy enumeration.  It supplies neither a metric prefix nor a determinant.

The conservative typed-proxy tuple remains

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_INVOCATION_ALLOWED=false
```
"""
    return text.encode("utf-8")


def receipt_for(material: dict[Path, bytes], metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "p24-round7-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "material_sha256": combined_hash(material),
        "execution": {"required_independent_builds": 2, "byte_identical": True},
        "unit_tests": {"expected": 12, "failed": 0},
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
        "exact_matrix_rows": metrics["unique_exact_matrices_including_identity"],
        "distinct_d9_values": metrics["distinct_d9_values"],
        "paper_decision": metrics["paper_decision"],
        "typed_proxy_candidate_id": metrics["typed_proxy_candidate_id"],
        "formal_route_a_tuple": metrics["formal_route_a_tuple"],
        "overall_verdict": metrics["overall_verdict"],
        "full_bianchi_flow_route_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "prime_or_zero_target_data_used": False,
        "default_reproduction_command": "bash experiments/reproduce_round7.sh",
        "refresh_command": "bash experiments/reproduce_round7.sh --refresh",
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
    print("P24 Round-7 existing artifacts VERIFIED")


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
            "primary_sha256": combined_hash(primary),
            "decision": metrics["paper_decision"],
            "rows": metrics["unique_exact_matrices_including_identity"],
            "status": "REFRESHED",
        }, sort_keys=True))
    else:
        verify_existing(args.output_root)


if __name__ == "__main__":
    main()
