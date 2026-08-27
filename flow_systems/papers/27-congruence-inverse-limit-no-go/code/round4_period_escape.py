#!/usr/bin/env python3
"""Build the P27 Round-4 finite-level period-escape audit.

The asymptotic theorem is proved in the accompanying note.  This program only
validates its finite diagnostic on the already frozen three-element/eight-level
ledger.  It does not infer an asymptotic theorem from 24 rows and does not turn
finite-level closed lifts into periodic points of the inverse-limit flow.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import defaultdict
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Iterable, Sequence


getcontext().prec = 60

DATE = "2026-08-27"
CANDIDATE_ID = "P27-GAMMA-3-FACTORIAL-PERIOD-ESCAPE"
EXPECTED_INPUT_SHA256 = (
    "811c53a24e34def2b7fbb9353ccd568dd638a9c57706443626091bc4c23e09de"
)
EXPECTED_ROWS = 24
EXPECTED_LEVELS = (3, 6, 18, 72, 360, 2160, 15120, 120960)
EXPECTED_ORDERS = {
    "G3-A": (1, 3, 3, 6, 6, 36, 72, 288),
    "G3-B": (1, 1, 3, 12, 60, 360, 360, 2880),
    "G3-C": (1, 2, 6, 12, 12, 72, 72, 576),
}

OUTPUT_FIELDS = (
    "element_id",
    "positive_word",
    "level_n",
    "modulus_q",
    "base_geodesic_length",
    "finite_quotient_order",
    "previous_finite_quotient_order",
    "previous_order_divides",
    "order_non_decreasing",
    "strict_growth_at_transition",
    "closed_lift_period_from_frozen_base",
    "period_to_base_ratio",
    "normal_tower_conjugacy_independent",
    "finite_prefix_escape_observed",
    "asymptotic_escape_evidence",
    "finite_statistic_owner",
    "inverse_limit_periodic_orbit_credit",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def decimal_text(value: Decimal) -> str:
    return format(value, "f")


def read_input(project_root: Path) -> tuple[list[dict[str, str]], str]:
    path = project_root / "results/round2/congruence_reduction_order_ledger.csv"
    payload = path.read_bytes()
    digest = sha256_bytes(payload)
    if digest != EXPECTED_INPUT_SHA256:
        raise RuntimeError(f"Round-2 ledger drift: {digest}")
    rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8"))))
    if len(rows) != EXPECTED_ROWS:
        raise RuntimeError(f"expected {EXPECTED_ROWS} rows, found {len(rows)}")
    return rows, digest


def group_rows(rows: Sequence[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["element_id"]].append(row)
    for values in grouped.values():
        values.sort(key=lambda row: int(row["level_n"]))
    return dict(sorted(grouped.items()))


def build_escape_rows(rows: Sequence[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for element_id, group in group_rows(rows).items():
        first_order = int(group[0]["psl_order_sequential"])
        final_order = int(group[-1]["psl_order_sequential"])
        finite_prefix_escape = final_order > first_order
        previous: int | None = None
        for row in group:
            order = int(row["psl_order_sequential"])
            base_length = Decimal(row["base_geodesic_length"])
            closed_period = base_length * order
            divides = previous is None or order % previous == 0
            non_decreasing = previous is None or order >= previous
            output.append(
                {
                    "element_id": element_id,
                    "positive_word": row["positive_word"],
                    "level_n": row["level_n"],
                    "modulus_q": row["modulus_q"],
                    "base_geodesic_length": row["base_geodesic_length"],
                    "finite_quotient_order": str(order),
                    "previous_finite_quotient_order": "" if previous is None else str(previous),
                    "previous_order_divides": str(divides).lower(),
                    "order_non_decreasing": str(non_decreasing).lower(),
                    "strict_growth_at_transition": str(
                        previous is not None and order > previous
                    ).lower(),
                    "closed_lift_period_from_frozen_base": decimal_text(closed_period),
                    "period_to_base_ratio": str(order),
                    "normal_tower_conjugacy_independent": "true",
                    "finite_prefix_escape_observed": str(finite_prefix_escape).lower(),
                    "asymptotic_escape_evidence": "PROVED_IN_GENERAL_THEOREM_NOT_FROM_FINITE_ROWS",
                    "finite_statistic_owner": "FINITE_CONGRUENCE_TOWER_PLUS_FROZEN_ELEMENT",
                    "inverse_limit_periodic_orbit_credit": "FORBIDDEN",
                    "formal_route_a_tuple": "UNASSIGNED",
                    "route_b_invocation_allowed": "false",
                }
            )
            previous = order
    return output


def validate(rows: Sequence[dict[str, str]], input_sha: str) -> dict[str, object]:
    grouped = group_rows(rows)
    observed_moduli = tuple(int(row["modulus_q"]) for row in next(iter(grouped.values())))
    observed_orders = {
        key: tuple(int(row["psl_order_sequential"]) for row in values)
        for key, values in grouped.items()
    }
    nested_moduli = all(
        following % previous == 0
        for previous, following in zip(observed_moduli, observed_moduli[1:])
    )
    order_divisibility = all(
        following % previous == 0
        for values in observed_orders.values()
        for previous, following in zip(values, values[1:])
    )
    last_order_growth = {
        key: values[-1] // values[0] for key, values in observed_orders.items()
    }
    strict_growth_steps = {
        key: sum(following > previous for previous, following in zip(values, values[1:]))
        for key, values in observed_orders.items()
    }
    plateau_steps = {
        key: sum(following == previous for previous, following in zip(values, values[1:]))
        for key, values in observed_orders.items()
    }
    checks = {
        "row_count_24": len(rows) == 24,
        "three_elements": tuple(grouped) == tuple(EXPECTED_ORDERS),
        "eight_levels_each": all(len(values) == 8 for values in grouped.values()),
        "frozen_moduli_match": observed_moduli == EXPECTED_LEVELS,
        "nested_moduli": nested_moduli,
        "frozen_order_sequences_match": observed_orders == EXPECTED_ORDERS,
        "orders_divide_along_tower": order_divisibility,
        "every_frozen_element_shows_prefix_growth": all(
            values[-1] > values[0] for values in observed_orders.values()
        ),
        "finite_owner_firewall_intact": all(
            row["inverse_limit_flow_credit"] == "FORBIDDEN" for row in rows
        ),
        "order_crosschecks_pass": all(row["order_crosscheck"] == "true" for row in rows),
    }
    if not all(checks.values()):
        raise RuntimeError("Round-4 period-escape validation failed")
    return {
        "schema": "p27_round4_period_escape_validation/1.0",
        "candidate_id": CANDIDATE_ID,
        "date": DATE,
        "status": "PASS",
        "input_round2_ledger_sha256": input_sha,
        "checks": checks,
        "orders_by_element": {key: list(values) for key, values in observed_orders.items()},
        "last_to_first_order_growth_factor": last_order_growth,
        "strict_growth_transition_count": strict_growth_steps,
        "plateau_transition_count": plateau_steps,
        "max_observed_order": max(max(values) for values in observed_orders.values()),
        "finite_diagnostic_evidence": "NUMERICALLY_CERTIFIED",
        "general_period_escape_theorem": "PROVED",
        "general_theorem_statement": (
            "FOR_A_DESCENDING_NORMAL_FINITE_INDEX_TOWER_WITH_TRIVIAL_INTERSECTION,"
            "THE_ORDERS_OF_EVERY_INFINITE_ORDER_ELEMENT_IN_THE_FINITE_QUOTIENTS_"
            "DIVERGE;HENCE_ITS_CLOSED_LIFT_PERIODS_DIVERGE"
        ),
        "theorem_proof_location": "notes/round4_period_escape_theorem.md",
        "theorem_hypotheses_machine_proof_boundary": (
            "FINITE_PREFIX_AND_FROZEN_LEDGER_CHECKS_ONLY;GENERAL_PROOF_IS_HUMAN_READABLE"
        ),
        "novelty_boundary": (
            "EXPLICIT_FACTORIAL_TOWER_OWNER_CRITERION_CASE_STUDY;"
            "NO_GENERAL_APERIODICITY_PRIORITY_CLAIM"
        ),
        "inverse_limit_periodic_set": "EMPTY_PROVED",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_a4": "NOT_EVALUATED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
    }


def csv_payload(rows: Iterable[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_payload(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_outputs(project_root: Path) -> dict[str, bytes]:
    rows, input_sha = read_input(project_root)
    return {
        "round4_period_escape_ledger.csv": csv_payload(build_escape_rows(rows)),
        "round4_period_escape_validation.json": json_payload(validate(rows, input_sha)),
    }


def write_outputs(output_dir: Path, outputs: dict[str, bytes]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in outputs.items():
        (output_dir / name).write_bytes(payload)


def combined_hash(outputs: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name in sorted(outputs):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[name])
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    outputs = build_outputs(project_root)
    write_outputs(args.output_dir, outputs)
    print(
        json.dumps(
            {"status": "PASS", "combined_sha256": combined_hash(outputs)},
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
