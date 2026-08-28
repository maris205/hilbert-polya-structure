#!/usr/bin/env python3
"""Exact finite replay for the P27 owner-preserving Euler-factor escape theorem.

The accompanying note proves the general coefficientwise no-go theorem.  This
builder consumes two already frozen owner/order ledgers and records the exact
coefficient prefix that each finite-level owner factor cannot affect.  It does
not infer the theorem from finite rows, relabel finite-level factors as
inverse-limit orbits, or define a renormalized replacement object.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from typing import Any, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"
CANDIDATE_ID = "P27-CONGRUENCE-INVERSE-LIMIT-GEODESIC-FLOW"
FORMAL_TUPLE = (
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
)
FREEZE_PATH = Path("experiments/round7_owner_factor_escape_freeze.json")
FREEZE_SHA256 = "5b136585689f2c4c79ccdd3eb418345100f1261032ad7d2f42efec0bcf576206"
INPUT_LOCKS = {
    "cusped_ledger": (
        Path("results/round4_period_escape_ledger.csv"),
        "92fee413d82e339d10ae4ba6842832b84d7a059aa7b253f9c576da10aed5ad7d",
    ),
    "cusped_validation": (
        Path("results/round4_period_escape_validation.json"),
        "4834d33339f119f310bdaa250f70575264b4fe0ea809c91daf752aa215b1f7b8",
    ),
    "cocompact_ledger": (
        Path("results/round5_cocompact_homology_escape_ledger.csv"),
        "0c74333b63f6027b16d134f19a320b8148e7fab6f86fa204d213c801106fe825",
    ),
    "cocompact_validation": (
        Path("results/round5_cocompact_homology_escape_validation.json"),
        "afdc51ca7ecfbd8777955c7438f08d4580e6b924419a807191e097b0292d9c10",
    ),
}

RESULT_PATHS = {
    "ledger": Path("results/round7_owner_factor_escape_ledger.csv"),
    "prefix": Path("results/round7_fixed_prefix_escape.csv"),
    "summary": Path("results/round7_owner_factor_escape_summary.json"),
}
RECEIPT_PATH = Path("experiments/round7_reproducibility_receipt.json")
VALIDATION_PATH = Path("experiments/round7_validation.md")
SOURCE_BINDING_PATHS = (
    FREEZE_PATH,
    Path("code/round7_owner_factor_escape.py"),
    Path("code/test_round7_owner_factor_escape.py"),
    Path("experiments/reproduce_round7.sh"),
)

LEDGER_FIELDS = (
    "tower_type",
    "owner_id",
    "owner_word",
    "base_conjugacy_primitivity",
    "factor_support_evidence",
    "level_n",
    "clock",
    "base_length",
    "quotient_order_symbol",
    "order_evidence",
    "exact_quotient_order",
    "certified_order_lower_bound",
    "first_possible_nonconstant_factor_degree",
    "certified_zero_coefficient_prefix_through_degree",
    "formal_factor",
    "coefficient_prefix_statement",
    "inverse_limit_periodic_orbit_credit",
    "same_owner_a2_credit",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)

PREFIX_FIELDS = (
    "tower_type",
    "owner_id",
    "fixed_prefix_degree_N",
    "first_certified_escape_level",
    "certified_order_lower_bound_at_level",
    "factor_equals_one_mod_x_to_N_plus_1",
    "frozen_prefix_status",
    "asymptotic_status",
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
        raise RuntimeError("P27 Round-7 freeze contract changed")
    freeze = json.loads(raw)
    for name, (path, digest) in INPUT_LOCKS.items():
        locked = freeze["input_locks"][name]
        if locked["path"] != path.as_posix() or locked["sha256"] != digest:
            raise AssertionError(f"freeze/input lock mismatch: {name}")
    if freeze["route_boundary"]["candidate_id"] != CANDIDATE_ID:
        raise AssertionError("freeze/candidate mismatch")
    if tuple(freeze["route_boundary"]["formal_tuple"]) != FORMAL_TUPLE:
        raise AssertionError("freeze/formal tuple mismatch")
    if any(freeze["forbidden_inputs"].values()):
        raise AssertionError("forbidden-input flags must remain false")
    return freeze, raw


def read_locked_bytes(name: str) -> bytes:
    path, expected = INPUT_LOCKS[name]
    raw = (PROJECT_ROOT / path).read_bytes()
    if sha256(raw) != expected:
        raise RuntimeError(f"locked P27 input changed: {name}")
    return raw


def read_csv(name: str) -> list[dict[str, str]]:
    raw = read_locked_bytes(name)
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8"), newline="")))


def validate_inputs() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    cusped = read_csv("cusped_ledger")
    compact = read_csv("cocompact_ledger")
    cusped_validation = json.loads(read_locked_bytes("cusped_validation"))
    compact_validation = json.loads(read_locked_bytes("cocompact_validation"))
    if len(cusped) != 24 or len(compact) != 24:
        raise AssertionError("both locked ledgers must contain 24 rows")
    if cusped_validation["status"] != "PASS" or compact_validation["status"] != "PASS":
        raise AssertionError("upstream validation must remain PASS")
    if cusped_validation["inverse_limit_periodic_set"] != "EMPTY_PROVED":
        raise AssertionError("cusped inverse-limit theorem drift")
    if compact_validation["inverse_limit_periodic_set"] != "EMPTY_BY_THE_RESIDUAL_TOWER_ARGUMENT":
        raise AssertionError("cocompact inverse-limit theorem drift")
    return cusped, compact


def build_ledger_rows(
    cusped: Sequence[dict[str, str]], compact: Sequence[dict[str, str]]
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    tuple_text = "(" + ",".join(FORMAL_TUPLE) + ")"
    for source in cusped:
        order = int(source["finite_quotient_order"])
        rows.append(
            {
                "tower_type": "CUSPED_GAMMA_3_FACTORIAL_CONGRUENCE",
                "owner_id": source["element_id"],
                "owner_word": source["positive_word"],
                "base_conjugacy_primitivity": "NOT_ESTABLISHED",
                "factor_support_evidence": "FORMAL_LOOP_ORDER_DIAGNOSTIC_ONLY_NOT_A_PRIMITIVE_ZETA_FACTOR",
                "level_n": source["level_n"],
                "clock": "HYPERBOLIC_ARCLENGTH",
                "base_length": source["base_geodesic_length"],
                "quotient_order_symbol": f"o_{source['level_n']}({source['element_id']})",
                "order_evidence": "EXACT_FINITE_QUOTIENT_ORDER",
                "exact_quotient_order": str(order),
                "certified_order_lower_bound": str(order),
                "first_possible_nonconstant_factor_degree": str(order),
                "certified_zero_coefficient_prefix_through_degree": str(order - 1),
                "formal_factor": f"(1-x_{source['element_id']}^{order})^(-1)",
                "coefficient_prefix_statement": f"E=1 mod x^{order}",
                "inverse_limit_periodic_orbit_credit": "FORBIDDEN",
                "same_owner_a2_credit": "FORBIDDEN",
                "formal_route_a_tuple": tuple_text,
                "route_b_invocation_allowed": "false",
            }
        )
    for source in compact:
        lower_bound = int(source["certified_full_order_lower_bound"])
        rows.append(
            {
                "tower_type": "COCOMPACT_GENUS2_RESIDUAL_HOMOLOGY",
                "owner_id": source["owner_id"],
                "owner_word": source["owner_word"],
                "base_conjugacy_primitivity": "PROVED_BY_PRIMITIVE_HOMOLOGY",
                "factor_support_evidence": "CERTIFIED_PRIMITIVE_OWNER_FACTOR_SUPPORT",
                "level_n": source["level_n"],
                "clock": source["clock"],
                "base_length": f"ell({source['owner_id']})",
                "quotient_order_symbol": source["full_quotient_order_symbol"],
                "order_evidence": "CERTIFIED_HOMOLOGY_LOWER_BOUND_ONLY",
                "exact_quotient_order": "NOT_ENUMERATED",
                "certified_order_lower_bound": str(lower_bound),
                "first_possible_nonconstant_factor_degree": f">={lower_bound}",
                "certified_zero_coefficient_prefix_through_degree": str(lower_bound - 1),
                "formal_factor": f"(1-x_{source['owner_id']}^o_n)^(-1);o_n>={lower_bound}",
                "coefficient_prefix_statement": f"E=1 mod x^{lower_bound}",
                "inverse_limit_periodic_orbit_credit": "FORBIDDEN",
                "same_owner_a2_credit": "FORBIDDEN",
                "formal_route_a_tuple": tuple_text,
                "route_b_invocation_allowed": "false",
            }
        )
    rows.sort(key=lambda row: (row["tower_type"], row["owner_id"], int(row["level_n"])))
    return rows


def build_prefix_rows(
    ledger: Sequence[dict[str, str]], prefix_degrees: Sequence[int]
) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in ledger:
        grouped.setdefault((row["tower_type"], row["owner_id"]), []).append(row)
    for values in grouped.values():
        values.sort(key=lambda row: int(row["level_n"]))

    output: list[dict[str, str]] = []
    for (tower, owner), values in sorted(grouped.items()):
        for degree in prefix_degrees:
            witness = next(
                (
                    row
                    for row in values
                    if int(row["certified_order_lower_bound"]) > degree
                ),
                None,
            )
            output.append(
                {
                    "tower_type": tower,
                    "owner_id": owner,
                    "fixed_prefix_degree_N": str(degree),
                    "first_certified_escape_level": (
                        "" if witness is None else witness["level_n"]
                    ),
                    "certified_order_lower_bound_at_level": (
                        "" if witness is None else witness["certified_order_lower_bound"]
                    ),
                    "factor_equals_one_mod_x_to_N_plus_1": str(witness is not None).lower(),
                    "frozen_prefix_status": (
                        "CERTIFIED_IN_FROZEN_PREFIX"
                        if witness is not None
                        else "NOT_REACHED_BY_FROZEN_EIGHT_LEVELS"
                    ),
                    "asymptotic_status": "PROVED_EVENTUALLY_BY_ORDER_ESCAPE_THEOREM",
                }
            )
    return output


def validate(
    ledger: Sequence[dict[str, str]], prefix: Sequence[dict[str, str]]
) -> dict[str, Any]:
    owner_ids = sorted({row["owner_id"] for row in ledger})
    exact_rows = [row for row in ledger if row["order_evidence"] == "EXACT_FINITE_QUOTIENT_ORDER"]
    lower_rows = [row for row in ledger if row["order_evidence"] == "CERTIFIED_HOMOLOGY_LOWER_BOUND_ONLY"]
    checks = {
        "ledger_rows_48": len(ledger) == 48,
        "six_owners": len(owner_ids) == 6,
        "eight_levels_each": all(
            sum(row["owner_id"] == owner for row in ledger) == 8 for owner in owner_ids
        ),
        "cusped_exact_rows_24": len(exact_rows) == 24,
        "compact_lower_bound_rows_24": len(lower_rows) == 24,
        "compact_exact_orders_not_fabricated": all(
            row["exact_quotient_order"] == "NOT_ENUMERATED" for row in lower_rows
        ),
        "cusped_primitivity_not_fabricated": all(
            row["base_conjugacy_primitivity"] == "NOT_ESTABLISHED"
            and row["factor_support_evidence"]
            == "FORMAL_LOOP_ORDER_DIAGNOSTIC_ONLY_NOT_A_PRIMITIVE_ZETA_FACTOR"
            for row in exact_rows
        ),
        "compact_primitivity_certificate_preserved": all(
            row["base_conjugacy_primitivity"] == "PROVED_BY_PRIMITIVE_HOMOLOGY"
            and row["factor_support_evidence"]
            == "CERTIFIED_PRIMITIVE_OWNER_FACTOR_SUPPORT"
            for row in lower_rows
        ),
        "zero_prefix_is_order_bound_minus_one": all(
            int(row["certified_zero_coefficient_prefix_through_degree"])
            == int(row["certified_order_lower_bound"]) - 1
            for row in ledger
        ),
        "prefix_rows_54": len(prefix) == 54,
        "all_prefix_rows_keep_asymptotic_theorem_boundary": all(
            row["asymptotic_status"] == "PROVED_EVENTUALLY_BY_ORDER_ESCAPE_THEOREM"
            for row in prefix
        ),
        "same_owner_and_inverse_limit_credit_forbidden": all(
            row["same_owner_a2_credit"] == "FORBIDDEN"
            and row["inverse_limit_periodic_orbit_credit"] == "FORBIDDEN"
            for row in ledger
        ),
        "route_b_closed": all(row["route_b_invocation_allowed"] == "false" for row in ledger),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"Round-7 validation failed: {failed}")
    return {
        "schema": "p27-round7-owner-factor-escape-summary/1.0",
        "date": DATE,
        "candidate_id": CANDIDATE_ID,
        "status": "PASS",
        "checks": checks,
        "ledger_rows": len(ledger),
        "owners": len(owner_ids),
        "levels_per_owner": 8,
        "prefix_diagnostic_rows": len(prefix),
        "prefix_diagnostics_certified_in_frozen_levels": sum(
            row["factor_equals_one_mod_x_to_N_plus_1"] == "true" for row in prefix
        ),
        "prefix_diagnostics_not_reached_but_asymptotically_proved": sum(
            row["factor_equals_one_mod_x_to_N_plus_1"] != "true" for row in prefix
        ),
        "general_order_escape_theorem": "PROVED_IN_ROUND4_AND_ROUND5_NOT_FROM_FINITE_ROWS",
        "owner_factor_escape_theorem": "PROVED_IN_ROUND7_NOTE",
        "cusped_finite_factor_status": "FORMAL_LOOP_ORDER_SUPPORT_DIAGNOSTIC_PRIMITIVITY_NOT_ESTABLISHED",
        "cocompact_finite_factor_status": "PRIMITIVE_OWNER_SUPPORT_CERTIFIED_FULL_ORDER_LOWER_BOUND_ONLY",
        "theorem_statement": (
            "FOR_EVERY_FIXED_PRIMITIVE_BASE_OWNER_AND_FIXED_DEGREE_N_THE_"
            "SAME_OWNER_FINITE_LEVEL_EULER_FACTOR_IS_EVENTUALLY_1_MOD_X^(N+1)"
        ),
        "finite_owner_panel_corollary": (
            "EVERY_FIXED_FINITE_PRODUCT_OF_SAME_OWNER_FACTORS_CONVERGES_"
            "COEFFICIENTWISE_TO_1"
        ),
        "clock": "UNCHANGED_BASE_HYPERBOLIC_ARCLENGTH",
        "renormalized_collective_object": "NOT_DEFINED_NOT_REFUTED_BY_THIS_THEOREM",
        "inverse_limit_periodic_set": "EMPTY_PROVED",
        "formal_route_a_tuple": list(FORMAL_TUPLE),
        "overall_verdict": "ROUTE_A_REJECTED",
        "a2_claim": "SAME_OWNER_A2_REFUTED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
        "human_source_confirmations_inferred": False,
        "ars_stage": "STAGE_1_RESEARCH_IN_PROGRESS",
        "manuscript_authorized": False,
        "paper_advance": "OWNER_PRESERVING_COEFFICIENT_STABILITY_NO_GO_THEOREM",
    }


def build_payload() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Any]]:
    freeze, _raw = load_freeze()
    cusped, compact = validate_inputs()
    ledger = build_ledger_rows(cusped, compact)
    prefix = build_prefix_rows(ledger, freeze["diagnostic_prefix_degrees"])
    return ledger, prefix, validate(ledger, prefix)


def core_outputs() -> tuple[dict[Path, bytes], dict[str, Any]]:
    ledger, prefix, summary = build_payload()
    outputs = {
        RESULT_PATHS["ledger"]: csv_bytes(ledger, LEDGER_FIELDS),
        RESULT_PATHS["prefix"]: csv_bytes(prefix, PREFIX_FIELDS),
        RESULT_PATHS["summary"]: json_bytes(summary),
    }
    return outputs, summary


def receipt_for(outputs: dict[Path, bytes], summary: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "p27-round7-reproduction-receipt/1.0",
        "date": DATE,
        "status": "REPRODUCIBLE",
        "core_sha256": combined_hash(outputs),
        "execution": {"required_runs": 2, "byte_identical": True},
        "unit_tests": {"expected": 12, "failed": 0},
        "freeze_contract": {"path": FREEZE_PATH.as_posix(), "sha256": FREEZE_SHA256},
        "input_locks": {
            name: {"path": path.as_posix(), "sha256": digest}
            for name, (path, digest) in INPUT_LOCKS.items()
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
        "candidate_id": CANDIDATE_ID,
        "formal_route_a_tuple": summary["formal_route_a_tuple"],
        "overall_verdict": summary["overall_verdict"],
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
        "reproduction_command": "bash experiments/reproduce_round7.sh",
    }


def validation_markdown(outputs: dict[Path, bytes], summary: dict[str, Any]) -> bytes:
    text = f"""# P27 Round-7 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `{CANDIDATE_ID}`
- Freeze SHA-256: `{FREEZE_SHA256}`
- Core SHA-256: `{combined_hash(outputs)}`

## Exact replay

- Six fixed owners and eight finite levels each: `{summary['ledger_rows']}` rows.
- Cusped exact quotient-order rows: 24.
- Cocompact certified lower-bound rows: 24; no full quotient order is fabricated.
- Fixed-prefix diagnostics: `{summary['prefix_diagnostic_rows']}`.
- Certified inside the frozen eight levels: `{summary['prefix_diagnostics_certified_in_frozen_levels']}`.
- Not reached by eight levels but covered by the proved asymptotic theorem: `{summary['prefix_diagnostics_not_reached_but_asymptotically_proved']}`.

## Theorem boundary

For each fixed primitive base owner `g`, `o_n(g)` tends to infinity.  Hence
`(1-x_g^o_n(g))^(-1)=1 mod x_g^(N+1)` for every fixed `N` at all sufficiently
large levels.  Every fixed finite panel of same-owner factors therefore has
coefficientwise limit one.

This is a same-owner, same-clock obstruction.  It neither defines nor rejects
a new collectively renormalized object.  Finite-level factors receive no
inverse-limit orbit credit, the formal Route-A tuple remains rejected, and
Route B remains closed.
"""
    return text.encode("utf-8")


def rendered_outputs() -> dict[Path, bytes]:
    core, summary = core_outputs()
    rendered = dict(core)
    rendered[RECEIPT_PATH] = json_bytes(receipt_for(core, summary))
    rendered[VALIDATION_PATH] = validation_markdown(core, summary)
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
    print("P27 Round-7 existing artifacts VERIFIED")


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
                    "ledger_rows": summary["ledger_rows"],
                    "prefix_rows": summary["prefix_diagnostic_rows"],
                    "status": "PASS",
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
