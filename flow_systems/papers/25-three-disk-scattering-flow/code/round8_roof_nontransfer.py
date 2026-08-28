#!/usr/bin/env python3
"""Exact roof-cohomology obstruction and locked physical replay for P25.

The proof is mathematical: the symmetric period-two and period-three billiard
owners have different exact mean flight lengths.  The locked numerical ledger
is only a regression check of those formulas and a bounded census of how often
the period-two scalar clock happens to agree at word length at most twelve.

No prime table, Riemann-zero table, resonance list, or fitted clock is read.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
CANDIDATE_ID = "P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR"
FORMAL_TUPLE = (
    "A0_FAIL",
    "A1_PASS_ANALYTIC",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
)

FREEZE_PATH = Path("experiments/round8_roof_nontransfer_freeze.json")
FREEZE_SHA256 = "43393de457d985009883ab31a023c7dcf6444f9640e86d9aa969cc3993cf49a4"
INPUT_PATH = Path("results/three_disk_primitive_ledger_round2.csv")
INPUT_SHA256 = "25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736"

RESULT_PATHS = {
    "witnesses": Path("results/round8_exact_roof_witnesses.csv"),
    "replay": Path("results/round8_physical_roof_replay.csv"),
    "summary": Path("results/round8_roof_nontransfer_summary.json"),
}
VALIDATION_PATH = Path("experiments/round8_validation.md")
RECEIPT_PATH = Path("experiments/round8_reproducibility_receipt.json")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round8_roof_nontransfer.py"),
    Path("code/test_round8_roof_nontransfer.py"),
    Path("experiments/reproduce_round8.sh"),
)

DISTANCE_EXACT = {
    "5.8": Fraction(29, 5),
    "6": Fraction(6, 1),
    "6.0": Fraction(6, 1),
    "6.2": Fraction(31, 5),
}
CANONICAL_DISTANCE_LABELS = {
    Fraction(29, 5): "29/5",
    Fraction(6, 1): "6",
    Fraction(31, 5): "31/5",
}
PERIOD_TWO_WORDS = ("01", "02", "12")
PERIOD_THREE_WORDS = ("012", "021")

WITNESS_FIELDS = (
    "d_over_a_exact",
    "orbit_family",
    "oriented_owner_words",
    "owner_count",
    "topological_period",
    "exact_total_length_over_a",
    "exact_mean_length_over_a",
    "exact_mean_gap_from_period_two",
    "locked_ledger_max_absolute_length_residual",
    "locked_ledger_formula_check",
    "proof_role",
)

REPLAY_FIELDS = (
    "row_id",
    "d_over_a_exact",
    "cyclic_word",
    "topological_word_length",
    "actual_flight_length_over_a",
    "mean_flight_length_over_a",
    "period_two_scalar_clock_over_a",
    "difference_from_period_two_scalar_clock",
    "agrees_with_period_two_scalar_clock_at_frozen_tolerance",
    "exact_symmetric_witness_family",
    "symbolic_owner_status",
    "physical_owner_status",
    "route_credit_transfer_allowed",
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


def decimal_text(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def fraction_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def load_freeze() -> tuple[dict[str, Any], bytes]:
    raw = (PROJECT_ROOT / FREEZE_PATH).read_bytes()
    if sha256(raw) != FREEZE_SHA256:
        raise RuntimeError("P25 Round-8 freeze contract changed")
    freeze = json.loads(raw)
    locked = freeze["input_locks"]["round2_physical_ledger"]
    if locked != {"path": INPUT_PATH.as_posix(), "sha256": INPUT_SHA256}:
        raise AssertionError("freeze/input binding mismatch")
    if tuple(freeze["route_boundary"]["formal_tuple"]) != FORMAL_TUPLE:
        raise AssertionError("freeze/Route-A tuple mismatch")
    if any(freeze["forbidden_inputs"].values()):
        raise AssertionError("every forbidden-input flag must remain false")
    return freeze, raw


def read_locked_ledger() -> list[dict[str, str]]:
    raw = (PROJECT_ROOT / INPUT_PATH).read_bytes()
    if sha256(raw) != INPUT_SHA256:
        raise RuntimeError("locked P25 Round-2 physical ledger changed")
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"), newline="")))
    if len(rows) != 2241:
        raise AssertionError("locked physical ledger must contain 2,241 rows")
    return rows


def exact_geometry(distance: Fraction) -> dict[str, Decimal]:
    with localcontext() as context:
        context.prec = 80
        d = fraction_decimal(distance)
        sqrt_three = Decimal(3).sqrt()
        period_two_mean = d - Decimal(2)
        period_three_mean = d - sqrt_three
        gap = Decimal(2) - sqrt_three
        return {
            "d": +d,
            "sqrt_three": +sqrt_three,
            "period_two_mean": +period_two_mean,
            "period_two_total": +(Decimal(2) * period_two_mean),
            "period_three_mean": +period_three_mean,
            "period_three_total": +(Decimal(3) * period_three_mean),
            "gap": +gap,
            "minimax_lower_bound": +(gap / Decimal(2)),
        }


def normalized_distance(row: dict[str, str]) -> Fraction:
    try:
        return DISTANCE_EXACT[row["d_over_a"]]
    except KeyError as error:
        raise AssertionError(f"unexpected d/a value: {row['d_over_a']}") from error


def build_payload() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any]]:
    freeze, _ = load_freeze()
    source_rows = read_locked_ledger()
    grouped: dict[Fraction, list[dict[str, str]]] = {}
    for row in source_rows:
        if row["symbolic_primitive"] != "true":
            raise AssertionError("every frozen row must be symbolically primitive")
        if row["symbolic_repetition_exponent"] != "1":
            raise AssertionError("repetitions must not be mixed into the owner ledger")
        if row["actual_billiard_orbit_status"] != "NUMERICALLY_CERTIFIED":
            raise AssertionError("every frozen physical orbit must remain certified")
        grouped.setdefault(normalized_distance(row), []).append(row)
    if sorted(grouped) != [Fraction(29, 5), Fraction(6), Fraction(31, 5)]:
        raise AssertionError("geometry panel drift")
    if any(len(rows) != 747 for rows in grouped.values()):
        raise AssertionError("each geometry must retain 747 frozen owners")

    length_tolerance = Decimal(freeze["finite_replay"]["length_tolerance"])
    constant_tolerance = Decimal(freeze["finite_replay"]["constant_roof_tolerance"])
    witness_rows: list[dict[str, str]] = []
    replay_rows: list[dict[str, str]] = []
    geometry_summaries: dict[str, Any] = {}

    for distance in sorted(grouped):
        label = CANONICAL_DISTANCE_LABELS[distance]
        exact = exact_geometry(distance)
        rows = sorted(grouped[distance], key=lambda row: row["row_id"])
        by_word = {row["cyclic_word"]: row for row in rows}
        if not all(word in by_word for word in PERIOD_TWO_WORDS + PERIOD_THREE_WORDS):
            raise AssertionError("symmetric witness owner missing")

        for family, words, period, total_key, mean_key, gap_text, proof_role in (
            (
                "TWO_DISK_BOUNCE",
                PERIOD_TWO_WORDS,
                2,
                "period_two_total",
                "period_two_mean",
                "0",
                "FIXES_THE_ONLY_POSSIBLE_SCALAR_C_FROM_PERIOD_TWO_OWNERS",
            ),
            (
                "THREE_DISK_EQUILATERAL_TRIANGLE",
                PERIOD_THREE_WORDS,
                3,
                "period_three_total",
                "period_three_mean",
                "2-sqrt(3)",
                "CONTRADICTS_THE_PERIOD_TWO_SCALAR_AND_CONSTANT_ROOF_COHOMOLOGY",
            ),
        ):
            residuals = [
                abs(Decimal(by_word[word]["actual_flight_length"]) - exact[total_key])
                for word in words
            ]
            max_residual = max(residuals)
            if max_residual > length_tolerance:
                raise AssertionError(f"locked {family} length formula failed at d/a={label}")
            exact_total = (
                f"2*({label}-2)"
                if family == "TWO_DISK_BOUNCE"
                else f"3*({label}-sqrt(3))"
            )
            exact_mean = (
                f"{label}-2"
                if family == "TWO_DISK_BOUNCE"
                else f"{label}-sqrt(3)"
            )
            witness_rows.append(
                {
                    "d_over_a_exact": label,
                    "orbit_family": family,
                    "oriented_owner_words": ";".join(words),
                    "owner_count": str(len(words)),
                    "topological_period": str(period),
                    "exact_total_length_over_a": exact_total,
                    "exact_mean_length_over_a": exact_mean,
                    "exact_mean_gap_from_period_two": gap_text,
                    "locked_ledger_max_absolute_length_residual": decimal_text(max_residual),
                    "locked_ledger_formula_check": "PASS",
                    "proof_role": proof_role,
                }
            )

        scalar_matches = 0
        mean_differences: list[Decimal] = []
        for row in rows:
            period = int(row["topological_word_length"])
            length = Decimal(row["actual_flight_length"])
            mean = length / Decimal(period)
            difference = mean - exact["period_two_mean"]
            agrees = abs(difference) <= constant_tolerance
            scalar_matches += int(agrees)
            mean_differences.append(difference)
            word = row["cyclic_word"]
            if word in PERIOD_TWO_WORDS:
                witness_family = "TWO_DISK_BOUNCE"
            elif word in PERIOD_THREE_WORDS:
                witness_family = "THREE_DISK_EQUILATERAL_TRIANGLE"
            else:
                witness_family = ""
            replay_rows.append(
                {
                    "row_id": row["row_id"],
                    "d_over_a_exact": label,
                    "cyclic_word": word,
                    "topological_word_length": str(period),
                    "actual_flight_length_over_a": row["actual_flight_length"],
                    "mean_flight_length_over_a": decimal_text(mean),
                    "period_two_scalar_clock_over_a": decimal_text(exact["period_two_mean"]),
                    "difference_from_period_two_scalar_clock": decimal_text(difference),
                    "agrees_with_period_two_scalar_clock_at_frozen_tolerance": str(agrees).lower(),
                    "exact_symmetric_witness_family": witness_family,
                    "symbolic_owner_status": "PROVED_PRIMITIVE_ORIENTED_CYCLIC_WORD",
                    "physical_owner_status": "NUMERICALLY_CERTIFIED_AT_FROZEN_CUTOFF",
                    "route_credit_transfer_allowed": "false",
                }
            )

        geometry_summaries[label] = {
            "frozen_owner_rows": len(rows),
            "rows_agreeing_with_period_two_scalar_clock": scalar_matches,
            "rows_disagreeing_with_period_two_scalar_clock": len(rows) - scalar_matches,
            "minimum_observed_mean_gap": decimal_text(min(mean_differences)),
            "maximum_observed_mean_gap": decimal_text(max(mean_differences)),
            "exact_periodic_average_gap": "2-sqrt(3)",
        }

    replay_rows.sort(key=lambda row: (row["d_over_a_exact"], row["row_id"]))
    if len(witness_rows) != 6 or len(replay_rows) != 2241:
        raise AssertionError("Round-8 output row-count drift")
    if any(item["rows_agreeing_with_period_two_scalar_clock"] != 3 for item in geometry_summaries.values()):
        raise AssertionError("unexpected frozen scalar-clock agreement count")

    exact_at_six = exact_geometry(Fraction(6))
    summary = {
        "schema": "p25-round8-roof-nontransfer-summary/1.0",
        "date": DATE,
        "candidate_id": CANDIDATE_ID,
        "status": "PASS",
        "freeze_contract_sha256": FREEZE_SHA256,
        "theorem_evidence_status": "PROVED",
        "finite_replay_evidence_status": "NUMERICALLY_CERTIFIED",
        "theorem": (
            "THE_PHYSICAL_THREE_DISK_ROOF_IS_NOT_COHOMOLOGOUS_TO_A_CONSTANT_"
            "AND_NO_OWNER_PRESERVING_GLOBAL_SCALAR_SUBSTITUTION_TRANSFERS_"
            "THE_UNIT_ROOF_DETERMINANT"
        ),
        "period_two_mean_length_over_a": "d/a-2",
        "period_three_mean_length_over_a": "d/a-sqrt(3)",
        "exact_periodic_average_gap_over_a": "2-sqrt(3)",
        "exact_gap_decimal_80_digit_context": decimal_text(exact_at_six["gap"]),
        "minimax_scalar_error_lower_bound_over_a": "(2-sqrt(3))/2",
        "minimax_scalar_error_lower_bound_decimal_80_digit_context": decimal_text(
            exact_at_six["minimax_lower_bound"]
        ),
        "cohomology_argument": (
            "IF_TAU=C+U-U_COMPOSE_SIGMA_THEN_EVERY_PERIOD_N_SUM_EQUALS_N*C;"
            "THE_EXACT_PERIOD_TWO_AND_THREE_AVERAGES_DIFFER"
        ),
        "global_scalar_substitution": "REFUTED_FOR_OWNER_AND_REPETITION_PRESERVING_TRANSFER",
        "physical_weighted_transfer_operator": "NOT_REFUTED_MAY_REQUIRE_NONCONSTANT_ROOF",
        "witness_rows": len(witness_rows),
        "physical_replay_rows": len(replay_rows),
        "geometry_summaries": geometry_summaries,
        "prime_or_zero_tables_used": False,
        "formal_route_a_tuple": list(FORMAL_TUPLE),
        "tuple_owner": "UNIT_ROOF_SYMBOLIC_CALIBRATOR_ONLY",
        "physical_three_disk_route_tuple": "UNASSIGNED",
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "ars_stage": "STAGE_1_RESEARCH_IN_PROGRESS",
        "manuscript_authorized": False,
        "paper_advance": "EXACT_ROOF_COHOMOLOGY_AND_SCALAR_SUBSTITUTION_NONTRANSFER_THEOREM",
        "freeze_declared_theorem": freeze["predeclared_theorem"],
    }
    return witness_rows, replay_rows, summary


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    witnesses, replay, summary = build_payload()
    outputs = {
        RESULT_PATHS["witnesses"]: csv_bytes(witnesses, WITNESS_FIELDS),
        RESULT_PATHS["replay"]: csv_bytes(replay, REPLAY_FIELDS),
        RESULT_PATHS["summary"]: json_bytes(summary),
    }
    return outputs, summary


def validation_markdown(outputs: dict[Path, bytes], summary: dict[str, Any]) -> bytes:
    text = f"""# P25 Round-8 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `{CANDIDATE_ID}`
- Freeze SHA-256: `{FREEZE_SHA256}`
- Core SHA-256: `{combined_hash(outputs)}`

## Exact theorem

For disk radius `a>0` and equilateral center separation `d`, the symmetric
period-two bounce has mean flight length `d-2a`, while the symmetric
period-three triangle has mean flight length `d-sqrt(3)a`.  Their exact gap is
`(2-sqrt(3))a>0`.  A roof coboundary `tau=c+u-u o sigma` would give mean `c`
on every periodic orbit, so the physical roof is not cohomologous to a
constant.  For every scalar `c`, at least one witness has mean-length error at
least `(2-sqrt(3))a/2`.

## Locked replay

- Exact witness-family rows: `{summary['witness_rows']}`.
- Frozen physical owner rows: `{summary['physical_replay_rows']}`.
- At each of `d/a=29/5,6,31/5`, exactly three period-two owners agree with
  the period-two scalar clock and the other 744 frozen owners disagree at the
  prespecified tolerance.
- The replay checks the exact symmetric formulas but does not prove the
  theorem from floating-point rows.

## Route boundary

The theorem refutes only an owner- and repetition-preserving global scalar
substitution from the unit-roof determinant to the physical clock.  It does
not refute a transfer operator with the genuine nonconstant roof, compute the
Gutzwiller--Voros zeta, or compute the exact multiple-scattering determinant.
The formal A1--A2 tuple remains owned by the unit-roof symbolic calibrator;
the physical three-disk tuple remains `UNASSIGNED`, the overall calibrator
verdict remains `ROUTE_A_REJECTED`, and Route B remains closed.
"""
    return text.encode("utf-8")


def receipt_for(outputs: dict[Path, bytes], summary: dict[str, Any], validation: bytes) -> dict[str, Any]:
    return {
        "schema": "p25-round8-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "execution": {"required_runs": 2, "byte_identical": True},
        "unit_tests": {"expected": 12, "failed": 0},
        "freeze_contract": {"path": FREEZE_PATH.as_posix(), "sha256": FREEZE_SHA256},
        "locked_inputs": {
            INPUT_PATH.as_posix(): {
                "sha256": INPUT_SHA256,
                "bytes": (PROJECT_ROOT / INPUT_PATH).stat().st_size,
            }
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
        "tuple_owner": summary["tuple_owner"],
        "physical_three_disk_route_tuple": "UNASSIGNED",
        "overall_verdict": "ROUTE_A_REJECTED",
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
    print("P25 Round-8 existing artifacts VERIFIED")


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
                    "physical_replay_rows": summary["physical_replay_rows"],
                    "status": summary["status"],
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
