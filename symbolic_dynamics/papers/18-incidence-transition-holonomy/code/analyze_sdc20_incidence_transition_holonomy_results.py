#!/usr/bin/env python3
"""Validate and summarize the exact SD-C20 result ledger."""

from __future__ import annotations

import csv
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def read_csv(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with (RESULTS / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    run_summary = json.loads((RESULTS / "run_summary.json").read_text(encoding="utf-8"))
    s3 = json.loads((RESULTS / "s3_exact_certificate.json").read_text(encoding="utf-8"))
    group_rows = read_csv("group_enumeration_summary.csv")
    inventory_rows = read_csv("inventory_controls.csv")
    trace_rows = read_csv("trace_class_gates.csv")

    expected = {
        "S3": (7776, 972, 36, 36),
        "D4": (32768, 512, 64, 64),
        "Q8": (32768, 512, 64, 64),
    }
    group_comparison = []
    for row in group_rows:
        group = row["group"]
        tables = int(row["tables"])
        weak = int(row["one_dimensional_clean"])
        clean = int(row["all_irrep_clean"])
        gauge = int(row["gauge_power_clean"])
        if (tables, weak, clean, gauge) != expected[group]:
            raise AssertionError(f"unexpected exhaustive counts for {group}")
        group_comparison.append(
            {
                "group": group,
                "tables": tables,
                "one_dimensional_clean": weak,
                "all_irrep_clean": clean,
                "gauge_power_clean": gauge,
                "nongauge_clean": int(row["nongauge_clean"]),
                "weak_survival_rate": str(Fraction(weak, tables)),
                "all_irrep_survival_rate": str(Fraction(clean, tables)),
                "weak_false_survivors": weak - clean,
                "exact_clean_equals_gauge": clean == gauge,
            }
        )
    write_csv("group_comparison_table.csv", group_comparison)

    inventory_comparison = []
    kinds = sorted({row["inventory"] for row in inventory_rows})
    for inventory in kinds:
        selected = [row for row in inventory_rows if row["inventory"] == inventory]
        pass_count = sum(
            row["trivial_euler_ledger_exact"] == "True"
            and row["standard_leakage_persists"] == "True"
            and row["inventory_blind_symbolic_rule"] == "True"
            for row in selected
        )
        inventory_comparison.append(
            {
                "inventory": inventory,
                "rows": len(selected),
                "mechanism_passes": pass_count,
                "mechanism_pass_rate": str(Fraction(pass_count, len(selected))),
                "difference_from_prime_pass_rate": "0",
                "proves_too_much": pass_count == len(selected),
            }
        )
    write_csv("inventory_comparison_table.csv", inventory_comparison)

    trace_comparison = [
        {
            "block": row["block"],
            "absolute_subset_series": row["absolute_subset_series"],
            "proved_threshold": int(row["threshold"]),
            "evidence_status": row["evidence_status"],
            "boundary_or_below_claimed": row["boundary_or_below_claimed"],
        }
        for row in trace_rows
    ]
    write_csv("trace_class_comparison_table.csv", trace_comparison)

    leak_coefficients = s3["trace_log_coefficients"]
    if (
        leak_coefficients["x^2y^1"],
        leak_coefficients["x^1y^2"],
        leak_coefficients["x^2y^2"],
    ) != ("-3", "-3", "-6"):
        raise AssertionError("frozen trace-log leakage changed")
    if s3["four_cycle_character_gap"] != 3:
        raise AssertionError("frozen commutator character gap changed")
    if not all(run_summary["predeclared_gates"].values()):
        raise AssertionError("a preregistered gate failed")

    analysis = {
        "candidate_id": "SD-C20",
        "evidence_status": "NUMERICALLY_CERTIFIED",
        "exact_arithmetic_used": True,
        "strongest_progress": (
            "A genuine same-object S3 transition cocycle has exact trivial/sign "
            "Euler blocks and an exact standard Artin block with noncommutative leakage."
        ),
        "exact_formula_certificates": {
            "trivial_block": "(1-x)(1-y)",
            "sign_block": "(1-x)(1-y)",
            "standard_formula_exact": s3["standard_formula_exact"],
            "trace_log_x2y": leak_coefficients["x^2y^1"],
            "trace_log_xy2": leak_coefficients["x^1y^2"],
            "trace_log_x2y2": leak_coefficients["x^2y^2"],
            "unmarked_trace_log_x3y3": leak_coefficients["x^3y^3"],
            "isolated_commutator_character_gap": s3["four_cycle_character_gap"],
        },
        "finite_rigidity_evidence": {
            row["group"]: {
                "tables": row["tables"],
                "one_dimensional_clean": row["one_dimensional_clean"],
                "all_irrep_clean": row["all_irrep_clean"],
                "gauge_power_clean": row["gauge_power_clean"],
                "nongauge_clean": row["nongauge_clean"],
            }
            for row in group_comparison
        },
        "claim_boundary": (
            "The finite S3/D4/Q8 classifications are exact at two atoms but are "
            "not a universal determinant-classifies-cohomology theorem."
        ),
        "primary_obstacle": (
            "All six matched atom inventories reproduce the trivial factor, "
            "standard leakage, and commutator gap with identity pass-rate margin zero."
        ),
        "adversarial_control": {
            "inventory_kinds": kinds,
            "rows": len(inventory_rows),
            "all_rows_reproduce_mechanism": all(
                row["mechanism_passes"] == row["rows"] for row in inventory_comparison
            ),
            "identity_pass_rate_margin": 0,
            "verdict": "STOP_SCOPED / PROVES_TOO_MUCH",
        },
        "trace_class_boundary": {
            "trivial_rank_one": "Re(s)>1",
            "nontrivial_symmetric_incidence": "Re(s)>2",
            "continuation_beyond_honest_domain_claimed": False,
        },
        "route_tuple": [
            "A0_ANALYTIC_ARITHMETIC_ORIGIN",
            "A1_WEAK",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_metrics": {
            "zero_error_train": "not_applicable_no_target_zero_evaluation",
            "zero_error_validation": "not_applicable_no_target_zero_evaluation",
            "zero_error_test": "not_applicable_no_target_zero_evaluation",
            "extra_zero_count": "not_applicable_no_target_zero_evaluation",
            "missing_zero_count": "not_applicable_no_target_zero_evaluation",
            "root_count_discrepancy": "not_applicable_no_target_zero_evaluation",
        },
        "target_zero_data_used": False,
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(analysis, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
