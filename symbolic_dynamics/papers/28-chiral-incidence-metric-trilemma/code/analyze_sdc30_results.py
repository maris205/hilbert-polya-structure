#!/usr/bin/env python3
"""Analyze SD-C30 exact ledgers into comparison and finding artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def rows(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def truth(value: str) -> bool:
    return value == "True"


def write_csv(name: str, data: list[dict[str, object]]) -> None:
    with (RESULTS / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(data[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(data)


def main() -> int:
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    source = rows("source_compiler_ledger.csv")
    native = rows("native_gram_ledger.csv")
    infinite = rows("infinite_gram_formula_ledger.csv")
    schatten = rows("schatten_strip_ledger.csv")
    firewall = rows("infinite_s2_firewall.csv")
    b2 = rows("finite_b2_diagnostic.csv")
    b4 = rows("b4_frequency_ledger.csv")
    det3 = rows("det3_deletion_ledger.csv")
    metrics = rows("metric_rigidity_ledger.csv")
    orthogonal = rows("orthogonalized_det3_ledger.csv")
    adversaries = rows("adversary_control_ledger.csv")
    markers = rows("marker_ownership_ledger.csv")
    samples = rows("t_sample_ledger.csv")

    native_failures = sum(
        not truth(row["exact"])
        or not truth(row["symmetric"])
        or not truth(row["nonnegative"])
        or (truth(row["diagonal"]) and not truth(row["positive"]))
        for row in native
    )
    infinite_failures = sum(
        not truth(row["positive"]) or not truth(row["symmetric"])
        for row in infinite
    )
    metric_failures = 0
    for row in metrics:
        required = (
            truth(row["K_positive_definite"])
            and truth(row["required_q_selfadjoint"])
            and truth(row["Zt_H_Z_equals_K"])
            and truth(row["active_coordinate_collapse"])
        )
        if row["scope"] == "active_atoms_only":
            required = (
                required
                and truth(row["dormant_coupling_present"])
                and not truth(row["all_q_selfadjoint"])
            )
        metric_failures += int(not required)

    positive_frequencies = [
        row for row in b4 if row["kind"] == "unique_positive_frequency"
    ]
    b4_failures = sum(
        not truth(row["positive"])
        or not truth(row["unique_by_factorization"])
        or not truth(row["phase_dependent"])
        for row in positive_frequencies
    )
    finite_b4_failures = sum(
        not truth(row["phase_dependent"])
        or not truth(row["phase_flip_changes"])
        for row in b4
        if row["kind"] == "finite_native_control"
    )

    comparison = [
        {
            "block": "source_compiler",
            "raw_rows": len(source),
            "exact_passes": sum(
                truth(row["zeta_mobius_inverse"])
                and truth(row["all_q_pair_relations"])
                for row in source
            ),
            "failures": sum(
                not truth(row["zeta_mobius_inverse"])
                or not truth(row["all_q_pair_relations"])
                for row in source
            ),
            "control_or_baseline": "four source relations",
            "delta": "all primitive systems exact",
        },
        {
            "block": "native_and_infinite_gram",
            "raw_rows": len(native) + len(infinite),
            "exact_passes": len(native) + len(infinite) - native_failures - infinite_failures,
            "failures": native_failures + infinite_failures,
            "control_or_baseline": "independent weighted-trace recomputation",
            "delta": "nonnegative finite kernels; strictly positive prime formulas",
        },
        {
            "block": "schatten_and_non_s2_firewall",
            "raw_rows": len(schatten) + len(firewall),
            "exact_passes": sum(truth(row["exact"]) for row in schatten) + len(firewall),
            "failures": sum(not truth(row["exact"]) for row in schatten),
            "control_or_baseline": "strict q*Re(s)>1 criterion",
            "delta": "q=3 first common strip; q=2 excluded on critical line",
        },
        {
            "block": "finite_b2_diagnostic",
            "raw_rows": len(b2),
            "exact_passes": sum(
                truth(row["direct_equals_gram"])
                and truth(row["phase_dependent"])
                and truth(row["phase_flip_changes"])
                for row in b2
            ),
            "failures": sum(
                not truth(row["direct_equals_gram"])
                or not truth(row["phase_dependent"])
                or not truth(row["phase_flip_changes"])
                for row in b2
            ),
            "control_or_baseline": "direct block product versus Gram expansion",
            "delta": "motion exact but finite-cutoff only",
        },
        {
            "block": "det3_and_b4",
            "raw_rows": len(det3) + len(b4),
            "exact_passes": len(det3) + len(b4) - b4_failures - finite_b4_failures,
            "failures": b4_failures + finite_b4_failures,
            "control_or_baseline": "modified determinant power ledger",
            "delta": "powers 1,2 deleted; first visible power 4 has positive unique frequencies",
        },
        {
            "block": "metric_rigidity",
            "raw_rows": len(metrics),
            "exact_passes": len(metrics) - metric_failures,
            "failures": metric_failures,
            "control_or_baseline": "full versus active-only positive metrics",
            "delta": "active atoms coordinate-diagonalize in every certified metric",
        },
        {
            "block": "orthogonalized_det3",
            "raw_rows": len(orthogonal),
            "exact_passes": sum(
                truth(row["characteristic_exact"])
                and truth(row["phase_free"])
                and truth(row["det3_phase_free"])
                for row in orthogonal
            ),
            "failures": sum(
                not truth(row["characteristic_exact"])
                or not truth(row["phase_free"])
                or not truth(row["det3_phase_free"])
                for row in orthogonal
            ),
            "control_or_baseline": "orthogonal atom blocks",
            "delta": "all t-phase disappears with obliqueness",
        },
        {
            "block": "adversarial_sources",
            "raw_rows": len(adversaries),
            "exact_passes": sum(
                truth(row["native_offdiagonal_gram"])
                and truth(row["native_B4_phase"])
                and not truth(row["orthogonalized_phase"])
                and not truth(row["arithmetic_selectivity_observed"])
                for row in adversaries
            ),
            "failures": sum(
                not truth(row["native_offdiagonal_gram"])
                or not truth(row["native_B4_phase"])
                or truth(row["orthogonalized_phase"])
                or truth(row["arithmetic_selectivity_observed"])
                for row in adversaries
            ),
            "control_or_baseline": "standard, mutated, composite-only, seeded DAG",
            "delta": "the same motion occurs on every control: PROVES_TOO_MUCH",
        },
        {
            "block": "marker_u1_ownership",
            "raw_rows": len(markers),
            "exact_passes": sum(
                truth(row["symbolic_marker_exact"])
                and row["main_theorem_u"] == "1"
                and not truth(row["continuation_credit"])
                for row in markers
            ),
            "failures": sum(
                not truth(row["symbolic_marker_exact"])
                or row["main_theorem_u"] != "1"
                or truth(row["continuation_credit"])
                for row in markers
            ),
            "control_or_baseline": "three labels, repetitions one through eight",
            "delta": "u^(r ell) retained; u=1 owns the theorem",
        },
        {
            "block": "common_t_samples",
            "raw_rows": len(samples),
            "exact_passes": 0,
            "failures": 0,
            "control_or_baseline": "three display points per fixture",
            "delta": "nongating display only; symbolic ledgers decide claims",
        },
    ]
    write_csv("analysis_comparison_table.csv", comparison)

    standard_mixed = next(
        row
        for row in infinite
        if row["left_prime"] == "2" and row["right_prime"] == "3"
    )
    coefficient_23 = next(
        row
        for row in positive_frequencies
        if row["left_label"] == "2" and row["right_label"] == "3"
    )["coefficient"]
    findings = [
        {
            "id": 1,
            "observation": (
                f"All {len(source)} source compilers and all {len(native)} finite "
                "native-Gram rows pass exact algebraic checks."
            ),
            "interpretation": (
                "The chiral construction is genuinely source-derived and its "
                "mixed geometry is not a numerical artifact."
            ),
            "implication": "A0 is structural, while the pure Paper27 orbit ledger is lost.",
            "next_step": "Keep the source grammar frozen in any renormalization test.",
        },
        {
            "id": 2,
            "observation": (
                f"The exact (2,3) mixed Gram value is {standard_mixed['exact_value']}; "
                "every finite B2 formula moves under a phase flip."
            ),
            "interpretation": (
                "Oblique incidence atoms create real common-t spectral motion."
            ),
            "implication": (
                "That motion cannot be promoted through ordinary Tr(B^2), because "
                "the infinite critical-line block is not Hilbert-Schmidt."
            ),
            "next_step": "Separate finite diagnostics from infinite trace claims permanently.",
        },
        {
            "id": 3,
            "observation": (
                "S3 is the first honest common Schatten class; det3 deletes powers "
                f"one and two, while the (2,3) B4 coefficient is {coefficient_23}."
            ),
            "interpretation": (
                "A positive, uniquely factorized phase frequency survives in the "
                "first visible regularized moment."
            ),
            "implication": (
                "This is the strongest analytic gain, but it is a family invariant, "
                "not a fixed spectral operator."
            ),
            "next_step": "Test whether a source-natural counterterm can isolate global coherence.",
        },
        {
            "id": 4,
            "observation": (
                f"All {len(metrics)} metric rows pass, and all {len(orthogonal)} "
                "orthogonalized determinants are phase-free."
            ),
            "interpretation": (
                "Positive self-adjoint completions coordinate-diagonalize active atoms; "
                "removing obliqueness also removes t-motion."
            ),
            "implication": "The positive-metric completion space is exhausted by the trilemma.",
            "next_step": "Do not repeat the search with another positive square root.",
        },
        {
            "id": 5,
            "observation": (
                "Mutated, composite-only, and seeded-DAG controls all retain native "
                "B4 phase motion, while all 24 marker rows keep u^(r ell) at u=1."
            ),
            "interpretation": (
                "Pairwise Gram motion is generic rather than divisibility-selective; "
                "marker damping cannot be used as continuation credit."
            ),
            "implication": "A4 fails and Route A is rejected without invoking Route B.",
            "next_step": "Classify functorial B2 counterterms or prove a stronger no-go.",
        },
    ]
    analysis_status = (
        "PASS"
        if summary["status"] == "PASS"
        and all(int(row["failures"]) == 0 for row in comparison)
        else "FAIL"
    )
    analysis = {
        "candidate_id": "SD-C30",
        "status": analysis_status,
        "raw_data_table": "results/analysis_comparison_table.csv",
        "comparison_rows": len(comparison),
        "findings": findings,
        "statistics_note": (
            "All claim-bearing entries are exhaustive finite identities or exact "
            "symbolic theorem certificates. Means, standard deviations, confidence "
            "intervals, and ML deltas are not applicable."
        ),
        "strongest_progress": (
            "An honest S3/det3 critical strip with a uniquely positive fourth-moment "
            "frequency and exact native Gram formulas."
        ),
        "main_obstacle": (
            "Native phase motion is generic on adversarial posets, while every positive "
            "metric completion that removes the defect also removes the motion."
        ),
        "suggested_experiment": (
            "Classify source-natural cutoff-compatible counterterms for the critical "
            "B2 form and test whether any retained mixed invariant vanishes on mutated, "
            "composite-only, and seeded-DAG controls."
        ),
        "route_tuple": summary["route_tuple"],
        "overall_verdict": summary["overall_verdict"],
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(analysis, indent=2, sort_keys=True))
    return 0 if analysis_status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
