#!/usr/bin/env python3
"""Summarize the frozen SD-C25 exact experiment artifacts."""

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
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    source = json.loads((RESULTS / "source_oracle_certificate.json").read_text(encoding="utf-8"))
    recurrence = rows("recurrence_certificates.csv")
    memorizer = rows("nilpotent_memorizer_controls.csv")
    canonical = rows("canonical_block_traces.csv")
    transient = rows("transient_wrapper_structure.csv")
    recurrent = rows("recurrent_wrapper_controls.csv")
    roof = rows("roof_marker_mismatch.csv")
    leakage = [row for row in canonical if row["trace_zero_repetition_leakage"] == "True"]
    frozen_counterexample = [
        row for row in leakage if row["fiber"] == "trace_zero_repetition_leakage"
    ]
    analysis = {
        "candidate_id": "SD-C25",
        "source_audit": {
            "cutoff": source["cutoff"],
            "cycles_checked": source["cycles_checked"],
            "edges_checked": source["edges_checked"],
            "candidate_evaluator_separated": source["candidate_evaluator_separated"],
            "source_policy_pass": source["source_policy_pass"],
            "target_zero_data_used": False,
        },
        "exact_census": {
            "finite_transformation_maps": summary["finite_state"]["transformation_totals"]["unary_maps"],
            "finite_state_configurations": summary["finite_state"]["transformation_totals"]["configurations"],
            "finite_state_period_comparisons": summary["finite_state"]["transformation_totals"]["period_comparisons"],
            "finite_state_periodicity_failures": summary["finite_state"]["transformation_totals"]["periodicity_failures"],
            "boolean_relation_configurations": summary["finite_state"]["relation_totals"]["configurations"],
            "composite_witnesses": summary["finite_state"]["composite_witness_rows"],
            "recurrence_cases": len(recurrence),
            "recurrence_residuals_checked": summary["recurrence"]["residuals_checked"],
            "nonzero_recurrence_residuals": summary["recurrence"]["nonzero_residuals"],
            "memorizer_controls": len(memorizer),
            "memorizer_failures": summary["memorizer_prefix_failures"],
        },
        "block_local_factor_firewall": {
            "convention": "det(I-w_k B A^(k-1))",
            "canonical_rows": len(canonical),
            "trace_zero_leakage_rows": len(leakage),
            "frozen_2x2_rows": len(frozen_counterexample),
            "frozen_2x2_factor": "1-w_k^2",
            "frozen_2x2_first_trace": "0",
            "frozen_2x2_second_repetition_trace": "2",
            "all_frozen_2x2_rows_exact": all(
                row["local_factor_coefficients_in_w"] == "[1,0,-1]"
                and row["first_trace_zero"] == "True"
                and row["second_repetition_trace"] == "2"
                for row in frozen_counterexample
            ),
            "warning": "vanishing first trace does not delete higher repetitions or the matrix local factor",
        },
        "countable_wrapper_scope": {
            "licensed_architectures_only": [
                "Paper19 transient total-decider wrapper",
                "Paper20 recurrent closure with short total roof",
            ],
            "transient_supports": len(transient),
            "transient_core_failures": sum(row["recurrent_core_exact"] != "True" for row in transient),
            "recurrent_rows": len(recurrent),
            "marker_firewall_failures": sum(row["marker_changed"] != "True" for row in recurrent),
            "universal_countable_impossibility_claimed": False,
        },
        "roof_firewall": {
            "rows": len(roof),
            "exact_identity_failures": sum(row["edge_monomial_identity"] != "True" for row in roof),
            "first_mismatch": summary["first_marker_or_roof_mismatch"],
            "post_freeze_selected_count": summary["post_freeze_selected_count"],
            "filter_mode": "one-dimensional orbit-level oracle control",
            "finite_block_trace_filter": False,
        },
        "observations": [
            "The source-derived canonical word is exactly 1^(k-1)2 through k=4096 without target predicates in the candidate constructor.",
            "All exhausted finite transformations and Boolean-relation controls are eventually periodic, and every constructive accepted-prime witness propagates to a composite with the same response.",
            "Every rational matrix fixture obeys its exact Cayley-Hamilton recurrence and rational generating function.",
            "Growing nilpotent bilinear and trace fibers memorize all seven matched target families with the same architecture.",
            "The full finite-block primitive factor is matrix-valued; a zero first trace can retain nonzero repetition terms.",
            "The licensed Paper19/Paper20 wrappers prune or clock-dilute, while the original canonical roof remains factorial and the marker remains z^k.",
        ],
        "interpretation": [
            "Fixed finite memory cannot provide an infinite prime-only exact support on this ordered unary spine.",
            "Finite-cutoff success with dimension growing as the cutoff is storage, not arithmetic selection.",
            "A scalar trace mask cannot stand in for a higher-dimensional local determinant factor.",
            "The countable-wrapper conclusion is scoped to the two imported architectures, not all countable symbolic extensions.",
        ],
        "implication": [
            "Further finite character, automaton, or fixed matrix tests on 1^(k-1)2 repeat a proved obstruction.",
            "Any successor must leave the unary spine and derive logarithmic graph length and roof before target comparison.",
        ],
        "route_tuple": summary["route_tuple"],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "a4_claim": "this candidate constructs no self-adjoint or critical-line mechanism",
        "target_zero_metrics": "not_applicable; no_target_zero_evaluation",
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(analysis, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
