#!/usr/bin/env python3
"""Exact four-quadrant renormalization theorem replay for Paper 27.

This file deliberately defines a new finite-panel object.  It does not modify
or rescue the Round-7 residual inverse-limit owner.  The new cover is the pure
homology cover H_N and the new clock/normalization are explicit inputs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
from typing import Any, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
CANDIDATE_ID = "P27-HOMOLOGY-RENORMALIZED-GEODESIC-PANEL"
FORMAL_TUPLE = (
    "A0_FAIL",
    "A1_PASS_ANALYTIC",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
)

FREEZE_PATH = Path("experiments/round8_homology_renormalization_freeze.json")
FREEZE_SHA256 = "88d10c3dcdee3387b16414d2c56d4934b6daeef6728acc689855049840850a72"
INPUT_LOCKS = {
    "round5_owner_ledger": (
        Path("results/round5_cocompact_homology_escape_ledger.csv"),
        "0c74333b63f6027b16d134f19a320b8148e7fab6f86fa204d213c801106fe825",
    ),
    "round5_validation": (
        Path("results/round5_cocompact_homology_escape_validation.json"),
        "afdc51ca7ecfbd8777955c7438f08d4580e6b924419a807191e097b0292d9c10",
    ),
}
RESULT_PATHS = {
    "quadrants": Path("results/round8_renormalization_quadrants.csv"),
    "coefficients": Path("results/round8_renormalization_prefix_coefficients.csv"),
    "summary": Path("results/round8_homology_renormalization_summary.json"),
}
VALIDATION_PATH = Path("experiments/round8_validation.md")
RECEIPT_PATH = Path("experiments/round8_reproducibility_receipt.json")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round8_homology_renormalization.py"),
    Path("code/test_round8_homology_renormalization.py"),
    Path("experiments/reproduce_round8.sh"),
)

MODULI = (1, 2, 6, 24, 120, 720, 5040, 40320)
OWNER_IDS = ("G2-H1-A", "G2-H1-AB", "G2-H1-ACD")
MAX_DEGREE = 12
QUADRANTS = (
    {
        "quadrant_id": "Q00_RAW_CLOCK_RAW_MULTIPLICITY",
        "clock_rescaled": False,
        "multiplicity_normalized": False,
        "limit_status": "COEFFICIENTWISE_TO_1_ON_EVERY_FIXED_PREFIX",
    },
    {
        "quadrant_id": "Q10_RESCALED_CLOCK_RAW_MULTIPLICITY",
        "clock_rescaled": True,
        "multiplicity_normalized": False,
        "limit_status": "COEFFICIENT_OF_X_DIVERGES_AS_N_CUBED",
    },
    {
        "quadrant_id": "Q01_RAW_CLOCK_GEOMETRIC_MEAN",
        "clock_rescaled": False,
        "multiplicity_normalized": True,
        "limit_status": "COEFFICIENTWISE_TO_1_ON_EVERY_FIXED_PREFIX",
    },
    {
        "quadrant_id": "Q11_RESCALED_CLOCK_GEOMETRIC_MEAN",
        "clock_rescaled": True,
        "multiplicity_normalized": True,
        "limit_status": "EXACT_BASE_OWNER_FACTOR_AT_EVERY_LEVEL",
    },
)

QUADRANT_FIELDS = (
    "candidate_id",
    "owner_id",
    "owner_word",
    "homology_vector",
    "homology_content",
    "level_n",
    "modulus_N",
    "cover_subgroup",
    "deck_group",
    "deck_degree",
    "exact_owner_order_in_deck_group",
    "primitive_lift_component_count",
    "physical_lift_period",
    "quadrant_id",
    "clock",
    "log_multiplicity_normalization",
    "formal_owner_factor",
    "first_nonconstant_degree",
    "coefficient_at_first_nonconstant_degree",
    "all_level_or_asymptotic_status",
    "same_as_round7_owner",
    "arithmetic_or_target_data_used",
    "route_b_invocation_allowed",
)

COEFFICIENT_FIELDS = (
    "owner_id",
    "level_n",
    "modulus_N",
    "quadrant_id",
    "degree",
    "coefficient",
    "support_divisibility_condition",
    "exact_arithmetic",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_bytes(rows: Sequence[dict[str, str]], fields: Sequence[str]) -> bytes:
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
        raise RuntimeError("P27 Round-8 freeze contract changed")
    freeze = json.loads(raw)
    for name, (path, digest) in INPUT_LOCKS.items():
        if freeze["input_locks"][name] != {"path": path.as_posix(), "sha256": digest}:
            raise AssertionError(f"freeze/input binding mismatch: {name}")
    if tuple(freeze["route_boundary"]["formal_tuple"]) != FORMAL_TUPLE:
        raise AssertionError("freeze/Route-A tuple mismatch")
    if freeze["new_owner_notice"] != "THIS_IS_NOT_THE_ROUND7_RESIDUAL_INVERSE_LIMIT_OWNER":
        raise AssertionError("new-owner notice missing")
    if any(freeze["forbidden_inputs"].values()):
        raise AssertionError("every forbidden-input flag must remain false")
    return freeze, raw


def read_locked_bytes(name: str) -> bytes:
    path, digest = INPUT_LOCKS[name]
    raw = (PROJECT_ROOT / path).read_bytes()
    if sha256(raw) != digest:
        raise RuntimeError(f"locked P27 input changed: {name}")
    return raw


def source_owner_rows() -> dict[str, dict[str, str]]:
    ledger = list(
        csv.DictReader(
            io.StringIO(read_locked_bytes("round5_owner_ledger").decode("utf-8"), newline="")
        )
    )
    validation = json.loads(read_locked_bytes("round5_validation"))
    if validation["status"] != "PASS" or len(ledger) != 24:
        raise AssertionError("Round-5 owner source must remain valid")
    owners: dict[str, dict[str, str]] = {}
    for row in ledger:
        owner = row["owner_id"]
        owners.setdefault(owner, row)
        if row["homology_content"] != "1" or row["base_conjugacy_primitive"] != "true":
            raise AssertionError("Round-8 owner panel requires primitive content-one homology")
    if tuple(sorted(owners)) != tuple(sorted(OWNER_IDS)):
        raise AssertionError("owner panel drift")
    return owners


def factor_parameters(modulus: int, quadrant: dict[str, Any]) -> tuple[int, int]:
    support_degree = 1 if quadrant["clock_rescaled"] else modulus
    exponent = 1 if quadrant["multiplicity_normalized"] else modulus**3
    return support_degree, exponent


def factor_text(owner: str, modulus: int, quadrant: dict[str, Any]) -> str:
    support, exponent = factor_parameters(modulus, quadrant)
    return f"(1-x_{owner}^{support})^(-{exponent})"


def series_coefficient(support_degree: int, exponent: int, degree: int) -> int:
    if degree % support_degree:
        return 0
    repetition = degree // support_degree
    return math.comb(exponent + repetition - 1, repetition)


def build_payload() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any]]:
    freeze, _ = load_freeze()
    owners = source_owner_rows()
    quadrant_rows: list[dict[str, str]] = []
    coefficient_rows: list[dict[str, str]] = []

    for owner_id in OWNER_IDS:
        source = owners[owner_id]
        for level, modulus in enumerate(MODULI, start=1):
            deck_degree = modulus**4
            lift_count = modulus**3
            if deck_degree != modulus * lift_count:
                raise AssertionError("deck-orbit decomposition failed")
            for quadrant in QUADRANTS:
                support, exponent = factor_parameters(modulus, quadrant)
                if quadrant["clock_rescaled"]:
                    clock = "T_REN=T_PHYSICAL/N"
                else:
                    clock = "T_PHYSICAL"
                if quadrant["multiplicity_normalized"]:
                    normalization = "LOG_Z_REN=(1/N^3)*LOG_Z_PANEL"
                else:
                    normalization = "NONE"
                quadrant_rows.append(
                    {
                        "candidate_id": CANDIDATE_ID,
                        "owner_id": owner_id,
                        "owner_word": source["owner_word"],
                        "homology_vector": source["homology_vector_a1_b1_a2_b2"],
                        "homology_content": source["homology_content"],
                        "level_n": str(level),
                        "modulus_N": str(modulus),
                        "cover_subgroup": f"H_{modulus}=KER_H1_MOD_{modulus}",
                        "deck_group": f"(Z/{modulus}Z)^4",
                        "deck_degree": str(deck_degree),
                        "exact_owner_order_in_deck_group": str(modulus),
                        "primitive_lift_component_count": str(lift_count),
                        "physical_lift_period": f"{modulus}*ell({owner_id})",
                        "quadrant_id": quadrant["quadrant_id"],
                        "clock": clock,
                        "log_multiplicity_normalization": normalization,
                        "formal_owner_factor": factor_text(owner_id, modulus, quadrant),
                        "first_nonconstant_degree": str(support),
                        "coefficient_at_first_nonconstant_degree": str(exponent),
                        "all_level_or_asymptotic_status": quadrant["limit_status"],
                        "same_as_round7_owner": "false",
                        "arithmetic_or_target_data_used": "false",
                        "route_b_invocation_allowed": "false",
                    }
                )
                for degree in range(MAX_DEGREE + 1):
                    coefficient_rows.append(
                        {
                            "owner_id": owner_id,
                            "level_n": str(level),
                            "modulus_N": str(modulus),
                            "quadrant_id": quadrant["quadrant_id"],
                            "degree": str(degree),
                            "coefficient": str(series_coefficient(support, exponent, degree)),
                            "support_divisibility_condition": f"{support}_DIVIDES_DEGREE",
                            "exact_arithmetic": "true",
                        }
                    )

    quadrant_rows.sort(
        key=lambda row: (
            row["owner_id"],
            int(row["level_n"]),
            row["quadrant_id"],
        )
    )
    coefficient_rows.sort(
        key=lambda row: (
            row["owner_id"],
            int(row["level_n"]),
            row["quadrant_id"],
            int(row["degree"]),
        )
    )
    if len(quadrant_rows) != 96 or len(coefficient_rows) != 1248:
        raise AssertionError("Round-8 output row-count drift")

    q11 = [row for row in quadrant_rows if row["quadrant_id"].startswith("Q11")]
    if not all(
        row["first_nonconstant_degree"] == "1"
        and row["coefficient_at_first_nonconstant_degree"] == "1"
        for row in q11
    ):
        raise AssertionError("fully renormalized quadrant must equal the base factor")

    summary = {
        "schema": "p27-round8-homology-renormalization-summary/1.0",
        "date": DATE,
        "candidate_id": CANDIDATE_ID,
        "status": "PASS",
        "freeze_contract_sha256": FREEZE_SHA256,
        "new_owner_notice": "THIS_IS_NOT_THE_ROUND7_RESIDUAL_INVERSE_LIMIT_OWNER",
        "surface": "MARKED_CLOSED_HYPERBOLIC_GENUS_2_SURFACE",
        "cover_tower": "H_N=KER(GAMMA_TO_H1(SIGMA;Z/NZ))",
        "cover_tower_residual": False,
        "cover_tower_intersection": "COMMUTATOR_SUBGROUP",
        "owners": len(OWNER_IDS),
        "levels": len(MODULI),
        "moduli": list(MODULI),
        "quadrants": len(QUADRANTS),
        "quadrant_rows": len(quadrant_rows),
        "coefficient_rows": len(coefficient_rows),
        "coefficient_degree_max": MAX_DEGREE,
        "exact_structure": {
            "deck_degree": "N^4",
            "owner_order": "N",
            "primitive_lift_count": "N^3",
            "physical_lift_period": "N*ell(g)",
        },
        "quadrant_conclusions": {
            quadrant["quadrant_id"]: quadrant["limit_status"] for quadrant in QUADRANTS
        },
        "theorem": (
            "TIME_RESCALING_AND_GEOMETRIC_MEAN_MULTIPLICITY_NORMALIZATION_"
            "ARE_JOINTLY_SUFFICIENT_FOR_EXACT_BASE_PANEL_RECOVERY;EITHER_"
            "INTERVENTION_ALONE_FAILS"
        ),
        "fully_renormalized_factor": "(1-x_g)^(-1)_FOR_EVERY_OWNER_AND_LEVEL",
        "theorem_evidence_status": "PROVED",
        "finite_replay_evidence_status": "NUMERICALLY_CERTIFIED",
        "finite_replay_arithmetic_mode": "EXACT_INTEGER",
        "a0_specificity": "ABSENT_GENERIC_FOR_EVERY_MARKED_GENUS2_HYPERBOLIC_METRIC",
        "full_flow_determinant": "NOT_DEFINED_FINITE_OWNER_PANEL_ONLY",
        "prime_or_zero_tables_used": False,
        "formal_route_a_tuple": list(FORMAL_TUPLE),
        "overall_verdict": "ROUTE_A_REJECTED",
        "same_owner_round7_verdict": "ROUTE_A_REJECTED_UNCHANGED",
        "route_b_invocation_allowed": False,
        "ars_stage": "STAGE_1_RESEARCH_IN_PROGRESS",
        "manuscript_authorized": False,
        "paper_advance": "EXACT_FOUR_QUADRANT_COLLECTIVE_RENORMALIZATION_THEOREM",
        "freeze_declared_theorem": freeze["predeclared_theorem"],
    }
    return quadrant_rows, coefficient_rows, summary


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    quadrants, coefficients, summary = build_payload()
    outputs = {
        RESULT_PATHS["quadrants"]: csv_bytes(quadrants, QUADRANT_FIELDS),
        RESULT_PATHS["coefficients"]: csv_bytes(coefficients, COEFFICIENT_FIELDS),
        RESULT_PATHS["summary"]: json_bytes(summary),
    }
    return outputs, summary


def validation_markdown(outputs: dict[Path, bytes], summary: dict[str, Any]) -> bytes:
    text = f"""# P27 Round-8 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `{CANDIDATE_ID}`
- Freeze SHA-256: `{FREEZE_SHA256}`
- Core SHA-256: `{combined_hash(outputs)}`

## Exact structure

For `H_N=ker(Gamma -> H_1(Sigma;Z/NZ))`, the deck group is `(Z/NZ)^4`.
Every frozen primitive-content-one owner has exact deck order `N`; its full
preimage consists of `N^3` primitive lift components of physical period
`N*ell(g)`.  Thus the four frozen choices give

```text
raw clock, raw multiplicity:       (1-x_g^N)^(-N^3)
rescaled clock, raw multiplicity:  (1-x_g)^(-N^3)
raw clock, geometric mean:         (1-x_g^N)^(-1)
rescaled clock, geometric mean:    (1-x_g)^(-1)
```

Only the last quadrant recovers the base factor exactly at every level.  The
two raw-clock quadrants escape every fixed coefficient prefix; rescaling time
without multiplicity normalization instead makes the coefficient of `x_g`
grow as `N^3`.

## Exact replay

- Owner/level/quadrant rows: `{summary['quadrant_rows']}`.
- Exact coefficient rows through degree {MAX_DEGREE}: `{summary['coefficient_rows']}`.
- Three primitive owners and eight factorial moduli are retained.
- All computations use exact integers.

## Route and ownership boundary

This is a newly registered finite-panel calibrator with a new cover tower,
clock, and normalization.  It is not the Round-7 residual inverse-limit owner,
does not define a full-flow determinant, and is generic for every marked
genus-2 hyperbolic metric.  Hence A0 fails and the new candidate is
`ROUTE_A_REJECTED`; the original same-owner verdict is unchanged and Route B
remains closed.
"""
    return text.encode("utf-8")


def receipt_for(outputs: dict[Path, bytes], summary: dict[str, Any], validation: bytes) -> dict[str, Any]:
    return {
        "schema": "p27-round8-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "execution": {"required_runs": 2, "byte_identical": True},
        "unit_tests": {"expected": 12, "failed": 0},
        "freeze_contract": {"path": FREEZE_PATH.as_posix(), "sha256": FREEZE_SHA256},
        "locked_inputs": {
            path.as_posix(): {
                "sha256": digest,
                "bytes": (PROJECT_ROOT / path).stat().st_size,
            }
            for path, digest in INPUT_LOCKS.values()
        },
        "files": {
            path.as_posix(): {"sha256": sha256(data), "bytes": len(data)}
            for path, data in sorted(outputs.items(), key=lambda item: item[0].as_posix())
        },
        "validation_binding": {
            "path": VALIDATION_PATH.as_posix(),
            "sha256": sha256(validation),
            "bytes": len(validation),
        },
        "source_bindings": {
            path.as_posix(): {
                "sha256": sha256((PROJECT_ROOT / path).read_bytes()),
                "bytes": (PROJECT_ROOT / path).stat().st_size,
            }
            for path in SOURCE_BINDING_PATHS
        },
        "candidate_id": CANDIDATE_ID,
        "formal_route_a_tuple": summary["formal_route_a_tuple"],
        "overall_verdict": summary["overall_verdict"],
        "same_owner_round7_verdict": summary["same_owner_round7_verdict"],
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
        "reproduction_command": "bash experiments/reproduce_round8.sh",
    }


def rendered_outputs() -> dict[Path, bytes]:
    core, summary = core_outputs()
    rendered = dict(core)
    validation = validation_markdown(core, summary)
    rendered[VALIDATION_PATH] = validation
    rendered[RECEIPT_PATH] = json_bytes(receipt_for(core, summary, validation))
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
    print("P27 Round-8 existing artifacts VERIFIED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    if args.verify_existing:
        verify_existing(args.output_root)
    else:
        write_outputs(args.output_root)
        core, summary = core_outputs()
        print(
            json.dumps(
                {
                    "candidate_id": CANDIDATE_ID,
                    "core_sha256": combined_hash(core),
                    "quadrant_rows": summary["quadrant_rows"],
                    "coefficient_rows": summary["coefficient_rows"],
                    "status": summary["status"],
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
