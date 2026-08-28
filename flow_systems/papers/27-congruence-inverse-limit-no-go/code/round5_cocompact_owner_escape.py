#!/usr/bin/env python3
"""Build the P27 Round-5 cocompact residual-tower control.

The human-readable note proves the group-theoretic and geodesic statements.
This executable performs only exact integer replay of the frozen three-owner,
eight-level homology lower-bound ledger.  In particular, it does not enumerate
the canonical residual cores R_n and does not report their full quotient
orders as computed values.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from functools import reduce
from pathlib import Path
from typing import Iterable, Sequence


DATE = "2026-08-27"
CANDIDATE_ID = "P27-CLOSED-GENUS2-RESIDUAL-HOMOLOGY-PERIOD-ESCAPE"
SURFACE_ID = "CLOSED_ORIENTED_HYPERBOLIC_SURFACE_GENUS_2"
PRESENTATION = "<a1,b1,a2,b2 | [a1,b1][a2,b2]=1>"
LEVELS = tuple(range(1, 9))
MODULI = tuple(math.factorial(level) for level in LEVELS)
OWNERS = (
    {
        "owner_id": "G2-H1-A",
        "word": "a1",
        "homology_vector": (1, 0, 0, 0),
    },
    {
        "owner_id": "G2-H1-AB",
        "word": "a1*b1",
        "homology_vector": (1, 1, 0, 0),
    },
    {
        "owner_id": "G2-H1-ACD",
        "word": "a1*a2*b2",
        "homology_vector": (1, 0, 1, 1),
    },
)

OUTPUT_FIELDS = (
    "owner_id",
    "surface_id",
    "surface_group_presentation",
    "continuous_time_system",
    "clock",
    "owner_word",
    "homology_vector_a1_b1_a2_b2",
    "homology_content",
    "base_conjugacy_primitive",
    "base_primitivity_certificate",
    "level_n",
    "factorial_modulus_m_n",
    "canonical_residual_core",
    "tower_subgroup",
    "exact_homology_image_order",
    "full_quotient_order_status",
    "full_quotient_order_symbol",
    "proved_order_divisibility",
    "certified_full_order_lower_bound",
    "previous_lower_bound",
    "previous_bound_divides",
    "minimal_lift_period_symbol",
    "certified_minimal_period_lower_bound",
    "theorem_evidence",
    "finite_ledger_evidence",
    "finite_statistic_owner",
    "arithmetic_or_prime_target_used",
    "formal_route_a_tuple",
    "route_b_invocation_allowed",
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def vector_text(vector: Sequence[int]) -> str:
    return "(" + ",".join(str(value) for value in vector) + ")"


def homology_content(vector: Sequence[int]) -> int:
    """Return gcd of the coordinates, with content zero for the zero vector."""

    return reduce(math.gcd, (abs(value) for value in vector), 0)


def lcm(left: int, right: int) -> int:
    return abs(left * right) // math.gcd(left, right)


def order_in_modular_homology(vector: Sequence[int], modulus: int) -> int:
    """Exact additive order of ``vector`` in (Z/modulus Z)^d."""

    if modulus < 1:
        raise ValueError("modulus must be positive")
    coordinate_orders = (
        modulus // math.gcd(modulus, abs(value)) for value in vector
    )
    return reduce(lcm, coordinate_orders, 1)


def owner_primitivity_certificate(vector: Sequence[int]) -> str:
    if homology_content(vector) != 1:
        return "NOT_CERTIFIED_BY_PRIMITIVE_HOMOLOGY"
    return "PRIMITIVE_HOMOLOGY_VECTOR_FORBIDS_A_PROPER_GROUP_POWER"


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for owner in OWNERS:
        vector = owner["homology_vector"]
        if not isinstance(vector, tuple):
            raise TypeError("frozen homology vector must be a tuple")
        content = homology_content(vector)
        previous: int | None = None
        for level, modulus in zip(LEVELS, MODULI):
            homology_order = order_in_modular_homology(vector, modulus)
            rows.append(
                {
                    "owner_id": str(owner["owner_id"]),
                    "surface_id": SURFACE_ID,
                    "surface_group_presentation": PRESENTATION,
                    "continuous_time_system": "UNIT_SPEED_GEODESIC_FLOW",
                    "clock": "HYPERBOLIC_ARCLENGTH",
                    "owner_word": str(owner["word"]),
                    "homology_vector_a1_b1_a2_b2": vector_text(vector),
                    "homology_content": str(content),
                    "base_conjugacy_primitive": str(content == 1).lower(),
                    "base_primitivity_certificate": owner_primitivity_certificate(vector),
                    "level_n": str(level),
                    "factorial_modulus_m_n": str(modulus),
                    "canonical_residual_core": f"R_{level}=INTERSECTION_NORMAL_INDEX_LE_{level}",
                    "tower_subgroup": f"Gamma_{level}=R_{level}_INTERSECT_KERNEL_H1_MOD_{modulus}",
                    "exact_homology_image_order": str(homology_order),
                    "full_quotient_order_status": "NOT_ENUMERATED_LOWER_BOUND_ONLY",
                    "full_quotient_order_symbol": f"o_{level}({owner['owner_id']})",
                    "proved_order_divisibility": f"{homology_order}_DIVIDES_o_{level}",
                    "certified_full_order_lower_bound": str(homology_order),
                    "previous_lower_bound": "" if previous is None else str(previous),
                    "previous_bound_divides": str(
                        previous is None or homology_order % previous == 0
                    ).lower(),
                    "minimal_lift_period_symbol": (
                        f"o_{level}({owner['owner_id']})*ell({owner['owner_id']})"
                    ),
                    "certified_minimal_period_lower_bound": (
                        f">={homology_order}*ell({owner['owner_id']})"
                    ),
                    "theorem_evidence": "PROVED",
                    "finite_ledger_evidence": "NUMERICALLY_CERTIFIED",
                    "finite_statistic_owner": (
                        "COCOMPACT_RESIDUAL_HOMOLOGY_TOWER_PLUS_MARKED_GEODESIC"
                    ),
                    "arithmetic_or_prime_target_used": "false",
                    "formal_route_a_tuple": "UNASSIGNED",
                    "route_b_invocation_allowed": "false",
                }
            )
            previous = homology_order
    return rows


def validate(rows: Sequence[dict[str, str]]) -> dict[str, object]:
    owner_rows = {
        owner["owner_id"]: [
            row for row in rows if row["owner_id"] == owner["owner_id"]
        ]
        for owner in OWNERS
    }
    bound_sequences = {
        owner_id: [int(row["certified_full_order_lower_bound"]) for row in values]
        for owner_id, values in owner_rows.items()
    }
    checks = {
        "row_count_24": len(rows) == 24,
        "three_frozen_owners": tuple(owner_rows) == tuple(
            owner["owner_id"] for owner in OWNERS
        ),
        "eight_levels_per_owner": all(len(values) == 8 for values in owner_rows.values()),
        "factorial_schedule": all(
            tuple(int(row["factorial_modulus_m_n"]) for row in values) == MODULI
            for values in owner_rows.values()
        ),
        "factorial_schedule_nested": all(
            following % previous == 0
            for previous, following in zip(MODULI, MODULI[1:])
        ),
        "all_homology_vectors_primitive": all(
            row["homology_content"] == "1" for row in rows
        ),
        "homology_orders_equal_factorials": all(
            int(row["exact_homology_image_order"])
            == int(row["factorial_modulus_m_n"])
            for row in rows
        ),
        "all_lower_bounds_divide_forward": all(
            following % previous == 0
            for values in bound_sequences.values()
            for previous, following in zip(values, values[1:])
        ),
        "full_quotient_orders_not_claimed_computed": all(
            row["full_quotient_order_status"] == "NOT_ENUMERATED_LOWER_BOUND_ONLY"
            for row in rows
        ),
        "base_primitivity_certified": all(
            row["base_conjugacy_primitive"] == "true" for row in rows
        ),
        "owner_firewall_intact": all(
            row["finite_statistic_owner"]
            == "COCOMPACT_RESIDUAL_HOMOLOGY_TOWER_PLUS_MARKED_GEODESIC"
            for row in rows
        ),
        "route_and_target_firewalls_intact": all(
            row["arithmetic_or_prime_target_used"] == "false"
            and row["formal_route_a_tuple"] == "UNASSIGNED"
            and row["route_b_invocation_allowed"] == "false"
            for row in rows
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise RuntimeError(f"Round-5 cocompact validation failed: {failed}")
    return {
        "schema": "p27_round5_cocompact_owner_escape_validation/1.0",
        "candidate_id": CANDIDATE_ID,
        "date": DATE,
        "status": "PASS",
        "checks": checks,
        "surface": {
            "type": SURFACE_ID,
            "compact": True,
            "cusps": 0,
            "fundamental_group": PRESENTATION,
            "flow": "UNIT_SPEED_GEODESIC_FLOW",
            "clock": "HYPERBOLIC_ARCLENGTH",
        },
        "tower_definition": {
            "residual_core": "R_n=intersection of all normal N with [Gamma:N]<=n",
            "homology_kernel": "H_n=ker(Gamma -> H_1(Sigma;Z/n!Z))",
            "tower": "Gamma_n=R_n intersection H_n",
            "nested_normal_finite_index": "PROVED_IN_NOTE",
            "trivial_intersection": "PROVED_IN_NOTE",
            "residual_core_enumerated": False,
        },
        "owners": len(OWNERS),
        "levels": len(LEVELS),
        "rows": len(rows),
        "moduli": list(MODULI),
        "lower_bounds_by_owner": bound_sequences,
        "largest_certified_order_lower_bound": max(MODULI),
        "largest_certified_period_lower_bound": "40320*ell(owner)",
        "base_conjugacy_primitivity": "PROVED_FROM_PRIMITIVE_HOMOLOGY",
        "minimal_lift_period_statement": (
            "EXACT_PERIOD_IS_o_n_TIMES_BASE_LENGTH;CERTIFIED_LOWER_BOUND_IS_n!_TIMES_BASE_LENGTH"
        ),
        "general_cocompact_control_theorem": "PROVED",
        "finite_ledger_evidence": "NUMERICALLY_CERTIFIED",
        "control_conclusion": (
            "PERIOD_ESCAPE_AND_INVERSE_LIMIT_APERIODICITY_ARE_NOT_CUSP_"
            "PRINCIPAL_CONGRUENCE_OR_ARITHMETIC_SPECIFIC"
        ),
        "machine_proof_boundary": (
            "EXACT_INTEGER_HOMOLOGY_REPLAY_ONLY;RESIDUAL_FINITENESS_TOWER_"
            "AND_GEODESIC_PRIMITIVITY_ARGUMENTS_ARE_HUMAN_READABLE_PROOFS"
        ),
        "inverse_limit_periodic_set": "EMPTY_BY_THE_RESIDUAL_TOWER_ARGUMENT",
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


def build_outputs() -> dict[str, bytes]:
    rows = build_rows()
    return {
        "round5_cocompact_homology_escape_ledger.csv": csv_payload(rows),
        "round5_cocompact_homology_escape_validation.json": json_payload(
            validate(rows)
        ),
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
    outputs = build_outputs()
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
