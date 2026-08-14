#!/usr/bin/env python3
"""Independent result evaluator for Paper 33 / SD-C35.

The evaluator reads frozen CSV/JSON payloads only.  It does not import the
candidate core, does not consult target-zero data, and treats arithmetic
classes as post-census labels.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    census = rows("modulus_homology_census.csv")
    matched = rows("matched_clone.csv")
    random_controls = rows("random_action_controls.csv")
    twists = rows("twist_census.csv")
    cross = json.loads((RESULTS / "cross_square_complex.json").read_text(encoding="utf-8"))
    source_scan = json.loads((RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8"))

    classes = ("prime", "prime_power", "mixed_composite")
    class_counts = {
        label: {
            "blocks": sum(row["evaluator_class"] == label for row in census),
            "relative_nonzero": sum(row["evaluator_class"] == label and int(row["relative_betti"]) > 0 for row in census),
            "cuspidal_nonzero": sum(row["evaluator_class"] == label and int(row["cuspidal_betti"]) > 0 for row in census),
        }
        for label in classes
    }
    composite_rows = [row for row in census if row["evaluator_class"] != "prime"]
    checks = {
        "all_191_relative_nonzero": all(int(row["relative_betti"]) > 0 for row in census),
        "all_148_composite_relative_nonzero": all(int(row["relative_betti"]) > 0 for row in composite_rows),
        "all_191_cusp_witnesses_return": all(int(row["cusp_rs_middle_distinct"]) and int(row["cusp_rs_returns"]) for row in census),
        "all_191_adjacencies_fail_to_descend": all(int(row["adjacency_descends"]) == 0 for row in census),
        "matched_clone_exact": sum(int(row["transport_exact"]) for row in matched) == len(matched) == 191,
        "random_controls_nonzero": sum(int(row["residual_nonzero"]) for row in random_controls) == len(random_controls) == 64,
        "diamond_fills_all_cross_h1": cross["graph_betti_before_filling"] == cross["diamond_boundary_rank"] and cross["homology_after_filling"] == 0,
        "honest_characters_do_not_kill_identity_cycle_words": sum(row["kind"] == "honest_character" and int(row["kills_identity_cycle_words"]) for row in twists) == 0,
        "two_honest_characters_kill_both_chain_norms": sum(row["kind"] == "honest_character" and int(row["kills_both_chain_norms"]) for row in twists) == 2,
        "zero_superdimension_identity_words_cancel": sum(row["kind"] == "zero_superdimension_difference" and int(row["kills_identity_cycle_words"]) for row in twists) == 15,
        "two_zero_superdimension_differences_kill_both_chain_norms": sum(row["kind"] == "zero_superdimension_difference" and int(row["kills_both_chain_norms"]) for row in twists) == 2,
        "zero_superdimension_cusp_survives": sum(row["kind"] == "zero_superdimension_difference" and int(row["cusp_sr_nonzero"]) for row in twists) == 15,
        "source_oracle_clean": source_scan["pass"] is True and not source_scan["hits"],
    }
    payload = {
        "candidate_id": "SD-C35",
        "evaluation_type": "independent_payload_evaluator",
        "class_counts": class_counts,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b": "LOCKED",
        "branch_action": "CLOSE_SEMIRING_RESIDUE_FAMILY",
    }
    (RESULTS / "evaluation.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "SD-C35", "checks": f'{payload["checks_passed"]}/{payload["checks_total"]}'}))


if __name__ == "__main__":
    main()
