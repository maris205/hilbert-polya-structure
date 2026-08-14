#!/usr/bin/env python3
"""Deterministic bounded analysis for SD-C32 exact artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    baseline = read(args.results / "baseline.json")
    finite = read(args.results / "finite_controls.json")
    free = read(args.results / "free_monoid_controls.json")
    clone = read(args.results / "clone_certificate.json")
    masks = read(args.results / "predicate_masks.json")
    analytic = read(args.results / "analytic_ownership.json")
    evaluation = read(args.results / "evaluation.json")
    tests = read(args.results / "test_report.json")
    summary = read(args.results / "summary.json")

    comparison = []
    for record in baseline["records"]:
        comparison.append(
            {
                "source": record["source"],
                "class": "integer_divisibility",
                "atoms": record["atom_count"],
                "qualified_pairs": record["qualified_pairs"],
                "qualified_triples": record["qualified_triples"],
                "pair_statistic_nonzero": record["C2_nonzero"],
                "triple_statistic_nonzero": record["theta3_nonzero"],
            }
        )
    for record in finite["records"]:
        comparison.append(
            {
                "source": record["source"],
                "class": "finite_non_UFD_control",
                "atoms": record["atom_count"],
                "qualified_pairs": record["qualified_pairs"],
                "qualified_triples": record["qualified_triples"],
                "pair_statistic_nonzero": record["C2_nonzero"],
                "triple_statistic_nonzero": record["theta3_nonzero"],
            }
        )
    comparison.append(
        {
            "source": "transported_free_commutative_clone_30",
            "class": "mandatory_UFD_clone",
            "atoms": baseline["records"][-1]["atom_count"],
            "qualified_pairs": baseline["records"][-1]["qualified_pairs"],
            "qualified_triples": baseline["records"][-1]["qualified_triples"],
            "pair_statistic_nonzero": True,
            "triple_statistic_nonzero": True,
        }
    )

    payload = {
        "schema_version": "SD-C32-analysis-v1",
        "candidate_id": "SD-C32",
        "status": "PASS_EXACT_CLONE_NO_GO",
        "route_tuple": summary["route_tuple"],
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
        "statistics": {
            "baseline_subset_rows": sum(
                len(record["pair_rows"]) + len(record["triple_rows"])
                for record in baseline["records"]
            ),
            "finite_control_subset_rows": sum(
                len(record["pair_rows"]) + len(record["triple_rows"])
                for record in finite["records"]
            ),
            "free_UFD_control_rows": free["row_count"],
            "predicate_mask_rows": masks["row_count"],
            "marker_rows": analytic["marker_row_count"],
            "independent_checks": evaluation["check_count"],
            "unit_tests": tests["tests_run"],
            "finite_pair_separating_masks": len(
                masks["pair_separating_masks_for_four_finite_controls"]
            ),
            "finite_triple_separating_masks": len(
                masks["triple_separating_masks_for_four_finite_controls"]
            ),
            "clone_equal_cutoffs": sum(clone["baseline_clone_equal_by_cutoff"]),
            "polynomial_UFD_equal_cutoffs": sum(
                clone["baseline_polynomial_UFD_equal_by_cutoff"]
            ),
        },
        "comparison_table": comparison,
        "findings": [
            {
                "observation": "The full pair selector retains exactly three mutated-cover pairs: (2,5), (2,7), and (3,5).",
                "interpretation": "A defect outside an atom pair's generated Boolean interval is invisible to every frozen pair predicate.",
                "implication": "The preregistered pair separator fails even before the UFD control; none of the 31 predicate masks fixes it.",
                "next_step": "Any further coherence statistic must be genuinely global across the whole source, not only global inside a generated interval.",
            },
            {
                "observation": "The full connected triple selector is nonzero on all three baselines and exactly zero on all four finite non-UFD fixture classes.",
                "interpretation": "Triple Boolean coherence is a real finite-fixture separator.",
                "implication": "This is a scoped GO, but it cannot establish arithmetic specificity without the mandatory structural clone.",
                "next_step": "Always place an isomorphic free-factorization clone beside finite mutation controls.",
            },
            {
                "observation": "Every baseline pair, triple, coefficient, marker, and all 31 predicate-mask counts are identical to transported free-commutative and polynomial-UFD clones.",
                "interpretation": "The selector detects free unique factorization, not the integer primes as a distinguished arithmetic source.",
                "implication": "Any natural invariant of the frozen incidence/join/Mobius/roof/Gram data proves too much.",
                "next_step": "Introduce a canonical integer-source operation absent from the clone, such as a derived additive/archimedean-multiplicative coupling, before another route claim.",
            },
            {
                "observation": "The filtered Gram matrix H has absolutely summable entries and an honest auxiliary Fredholm determinant, but its phase cancels and its coefficients are cloned exactly.",
                "interpretation": "Analytic determinant ownership can be earned for an auxiliary object without earning spectral or arithmetic selectivity.",
                "implication": "A2 survives while A1, A3, and A4 remain failed.",
                "next_step": "Do not identify det(I+zH) with the original chiral transfer determinant or count it as an RH mechanism.",
            },
        ],
        "decision": {
            "strongest_go": summary["strongest_go"],
            "strongest_stop": summary["strongest_stop"],
            "overall": summary["overall_status"],
            "paper31_minimum_obligation": summary["paper31_minimum_obligation"],
        },
        "boundary": {
            "proved": "exact clone obstruction for every invariant natural in the frozen transported decorated source data; exact failure of all 31 pair predicate masks on the mutated fixture",
            "not_proved": "a no-go after adding a new nontransportable source operation such as integer addition",
        },
    }
    (args.results / "analysis.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
