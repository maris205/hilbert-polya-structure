#!/usr/bin/env python3
"""Derive the compact deterministic SD-C27 analysis summary."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    scalar = rows("scalar_power_rigidity.csv")
    chain = rows("de_rham_chain_checks.csv")
    powers = rows("de_rham_power_supertraces.csv")
    necklaces = rows("primitive_necklace_ledger.csv")
    arbitrary = rows("arbitrary_inventory_controls.csv")
    marker = rows("marker_ownership_controls.csv")
    atom2_r2 = next(
        row for row in scalar if row["atom"] == "2" and row["power"] == "2"
    )
    mixed = [row for row in necklaces if row["mixed"] == "True"]
    payload = {
        "candidate_id": "SD-C27",
        "scalar_firewall": {
            "rows": len(scalar),
            "atom_2_r2_residual": atom2_r2["residual"],
            "all_r1_fit": all(row["match"] == "True" for row in scalar if row["power"] == "1"),
            "all_r2_plus_fail": all(row["match"] == "False" for row in scalar if int(row["power"]) >= 2),
        },
        "de_rham_escape": {
            "chain_rows": len(chain),
            "power_rows": len(powers),
            "all_characteristic_quotients_exact": all(
                row["characteristic_quotient_exact"] == "True" for row in chain
            ),
            "all_power_supertraces_exact": all(
                row["exact_match"] == "True" for row in powers
            ),
        },
        "mixed_primitive_survival": {
            "all_necklaces": len(necklaces),
            "mixed_necklaces": len(mixed),
            "all_mixed_survive_shared": all(
                row["shared_included"] == "True"
                and row["de_rham_cancels_word"] == "False"
                for row in mixed
            ),
        },
        "inventory_collapse": {
            "rows": len(arbitrary),
            "all_prove_too_much": all(row["proves_too_much"] == "True" for row in arbitrary),
        },
        "marker_firewall": {
            "rows": len(marker),
            "all_digit_return_mismatch": all(
                row["return_and_digit_markers_equal"] == "False" for row in marker
            ),
        },
        "strongest_advance": (
            "canonical de Rham 0|1 pullback cancels the affine fixed-point "
            "denominator at every power and gives an exact graded determinant"
        ),
        "strongest_ceiling": (
            "shared cohomology retains all mixed return words; disjoint "
            "cohomology is the supplied countable atom inventory"
        ),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

