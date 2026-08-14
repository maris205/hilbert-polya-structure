#!/usr/bin/env python3
"""Write the exact SFT and parent boundary-quotient periodic ledger."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone

import sympy as sp

from _common import add_output_argument, output_path, write_json_new
from branch_baker.algebra import ADJACENCY
from branch_baker.cycles import (
    boundary_quotient_ledger,
    direct_primitive_cycles,
    exact_candidate_cycle_audit,
    multiplier_moduli,
    periodic_point_counts,
)
from branch_baker.protocol import SOURCE_LOCK_PATH, sha256_file
from branch_baker.zeta import (
    S,
    Z,
    factor_orientation_determinant,
    factor_orientation_multiplier_product,
    interval_lefschetz_zeta,
    parent_core_zeta,
    parent_factor_orientation_object,
    unsigned_constant_slope_multiplier_product,
    unsigned_structural_determinant,
)


def expression(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(value))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=20)
    add_output_argument(parser, "results/ledger.json")
    args = parser.parse_args()
    if args.max_period != 20:
        raise SystemExit("The source-locked candidate ledger requires --max-period 20")

    audit = exact_candidate_cycle_audit(args.max_period)
    cycles = direct_primitive_cycles(ADJACENCY, args.max_period)
    boundary = boundary_quotient_ledger(args.max_period)
    cycle_rows = []
    for period in range(1, args.max_period + 1):
        unstable = stable = None
        if cycles[period]:
            unstable_expr, stable_expr = multiplier_moduli(period)
            unstable, stable = expression(unstable_expr), expression(stable_expr)
        cycle_rows.append(
            {
                "period": period,
                "fixed_points_symbolic": periodic_point_counts(
                    ADJACENCY, args.max_period
                )[period - 1],
                "primitive_count": len(cycles[period]),
                "representatives": [list(word) for word in cycles[period]],
                "unstable_multiplier_modulus": unstable,
                "stable_multiplier_modulus": stable,
            }
        )

    payload = {
        "candidate_id": "pcf_markov_baker_v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_lock_sha256": sha256_file(SOURCE_LOCK_PATH),
        "ledger_scope": "unquotiented constant-slope SFT/baker",
        "max_period": args.max_period,
        "cycle_rows": cycle_rows,
        "primitive_counts": list(audit.trace_mobius_counts),
        "primitive_total": sum(audit.trace_mobius_counts),
        "independent_direct_counts": list(audit.direct_enumeration_counts),
        "frozen_counts": list(audit.frozen_counts),
        "ledger_agreement": audit.passed,
        "parent_boundary_quotient": boundary.as_dict(),
        "determinant_conventions": {
            "unsigned_SFT_det": expression(unsigned_structural_determinant(Z)),
            "factor_orientation_det": expression(
                factor_orientation_determinant(Z)
            ),
            "parent_core_artin_mazur_zeta": expression(parent_core_zeta(Z)),
            "parent_factor_orientation_object": expression(
                parent_factor_orientation_object(Z)
            ),
            "interval_lefschetz_zeta": expression(interval_lefschetz_zeta(Z)),
            "unsigned_multiplier_product": expression(
                unsigned_constant_slope_multiplier_product(S)
            ),
            "factor_orientation_multiplier_product": expression(
                factor_orientation_multiplier_product(S)
            ),
        },
        "external_prime_or_zero_data_accessed": False,
        "passed": audit.passed and boundary.sole_declared_collapse_verified,
    }
    write_json_new(output_path(args.output), payload)


if __name__ == "__main__":
    main()
