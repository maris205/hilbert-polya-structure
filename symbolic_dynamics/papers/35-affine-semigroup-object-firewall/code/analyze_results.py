#!/usr/bin/env python3
"""Create deterministic scoped summaries from the exact Paper 35 audit."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    arguments = parser.parse_args()
    results = Path(arguments.results)

    parameters = load_json(results / "source_parameters.json")
    evaluation = load_json(results / "evaluation.json")
    tests = load_json(results / "test_report.json")
    counterexamples = load_json(results / "counterexamples.json")
    relations = load_json(results / "relation_witnesses.json")
    bc = load_json(results / "bc_firewall.json")
    fock = load_json(results / "fock_marker_firewall.json")
    boundaries = load_json(results / "boundary_controls.json")
    controls = load_json(results / "control_evaluation.json")
    census = load_csv(results / "admissible_word_census.csv")
    heights = load_csv(results / "height_dag_ledger.csv")
    backtracks = load_csv(results / "backtrack_ledger.csv")
    quotients = load_csv(results / "quotient_ledger.csv")

    total_words = sum(int(row["total_words"]) for row in census)
    total_admissible = sum(int(row["admissible_words"]) for row in census)
    total_nb_closed = sum(int(row["cyclic_nb_closed_words"]) for row in census)
    total_primitive_nb = sum(int(row["primitive_cyclic_nb_closed_words"]) for row in census)
    small_degenerate = sum(
        row["small_modulus"] == "True" and row["relation_polygon_vertex_simple"] == "False"
        for row in quotients
    )
    summary_rows: list[dict[str, object]] = [
        {
            "block": "positive_height_windows",
            "evidence_class": "EXACT_FINITE_LEDGER_PLUS_INDEPENDENT_DAG_CHECK",
            "population": len(heights),
            "primary_metric": "strict_height_edges",
            "value": sum(row["strict_increase"] == "True" for row in heights),
            "failures": sum(row["strict_increase"] != "True" for row in heights),
            "scope_note": "r=4 baseline; r=2,3,5 controls; infinite DAG conclusion owned by math lock",
        },
        {
            "block": "symmetric_two_step_backtracks",
            "evidence_class": "EXACT_EDGEWISE_CONSTRUCTION",
            "population": len(backtracks),
            "primary_metric": "hashimoto_rejected_backtracks",
            "value": sum(row["hashimoto_allowed"] == "False" for row in backtracks),
            "failures": sum(row["hashimoto_allowed"] != "False" for row in backtracks),
            "scope_note": "one reverse arc added for each frozen positive edge",
        },
        {
            "block": "hashimoto_word_census",
            "evidence_class": "EXHAUSTIVE_FOR_FROZEN_LENGTH_AND_BASES",
            "population": total_words,
            "primary_metric": "primitive_cyclic_nb_closed_words",
            "value": total_primitive_nb,
            "failures": int(not evaluation["gates"]["G3_hashimoto_affine_relation"]),
            "scope_note": f"{total_admissible} admissible and {total_nb_closed} cyclic nonbacktracking closed words through length 8",
        },
        {
            "block": "affine_relation_witnesses",
            "evidence_class": "EXACT_SYMBOLIC_WITNESSES",
            "population": len(relations["witnesses"]),
            "primary_metric": "closed_primitive_length_r_plus_3",
            "value": sum(
                row["closed"] and row["primitive"] and row["length"] == row["r"] + 3
                for row in relations["witnesses"]
            ),
            "failures": sum(
                not (row["closed"] and row["primitive"] and row["length"] == row["r"] + 3)
                for row in relations["witnesses"]
            ),
            "scope_note": "two bases for each r; authority U/V weights are one, so every relation witness has weight one",
        },
        {
            "block": "commutation_and_monoid_controls",
            "evidence_class": "EXACT_GENERIC_CONTROLS",
            "population": len(controls["commutation_controls"]) + len(controls["arbitrary_monoid_controls"]),
            "primary_metric": "generic_relation_cycles_survive",
            "value": int(controls["generic_relation_cycles_survive"]),
            "failures": int(not controls["generic_relation_cycles_survive"]),
            "scope_note": "generic dilation labels and arbitrary one-relator mutations; no arithmetic acceptance labels",
        },
        {
            "block": "operator_certificates",
            "evidence_class": "FINITE_WITNESS_SEQUENCES_NOT_NUMERICAL_PROOF",
            "population": len(parameters["r_values"]),
            "primary_metric": "exact_disjoint_support_certificates",
            "value": int(evaluation["gates"]["G5_operator_and_full_monoid_boundary"]),
            "failures": int(not evaluation["gates"]["G5_operator_and_full_monoid_boundary"]),
            "scope_note": "analytic boundedness/noncompactness and full-monoid boundary owned by math lock",
        },
        {
            "block": "finite_quotients",
            "evidence_class": "EXHAUSTIVE_FOR_Q_1_THROUGH_12",
            "population": len(quotients),
            "primary_metric": "relation_and_Uq_cycles_retained",
            "value": sum(row["relation_preserved"] == row["u_q_closed"] == "True" for row in quotients),
            "failures": int(not evaluation["gates"]["G6_finite_quotient_corrections"]),
            "scope_note": f"{small_degenerate} small-modulus rows have a non-simple relation polygon",
        },
        {
            "block": "bc_diagonal_firewall",
            "evidence_class": "EXACT_FINITE_RATIONAL_COEFFICIENT_IDENTITY",
            "population": len(bc["fixtures"]),
            "primary_metric": "Tr_Dm_over_m_log_coefficients",
            "value": sum(row["coefficient_identity_Tr_Dm_over_m"] for row in bc["fixtures"]),
            "failures": int(not evaluation["gates"]["G7_bc_trace_determinant_firewall"]),
            "scope_note": "beta=2,3 and cutoff 12; no infinite zeta identity inferred from cutoff",
        },
        {
            "block": "prime_fock_marker_firewall",
            "evidence_class": "EVALUATOR_ONLY_EXACT_CONTROL",
            "population": len(fock["prime_labels"]),
            "primary_metric": "occupation_series_methods_equal",
            "value": int(fock["coefficient_methods_equal"]),
            "failures": int(not evaluation["gates"]["G8_bosonic_marker_firewall"]),
            "scope_note": "prime-indexed basis is deliberately preloaded after source freeze; z counts occupation",
        },
        {
            "block": "signed_matrix_groupoid_boundary",
            "evidence_class": "EXACT_BOUNDARY_FIXTURES",
            "population": 3,
            "primary_metric": "boundary_gate_pass",
            "value": int(evaluation["gates"]["G9_signed_matrix_boundary"]),
            "failures": int(not evaluation["gates"]["G9_signed_matrix_boundary"]),
            "scope_note": "signed and matrix examples are exact; groupoid same-object question remains open",
        },
    ]
    write_csv(results / "exact_summary.csv", summary_rows)

    findings = [
        {
            "number": 1,
            "observation": "Every frozen positive P_r edge increased the authority height h_r(b,k)=b+r^k with the preregistered exact increment, and each induced finite window passed an independent Kahn DAG audit.",
            "interpretation": "The precise right-Cayley source is acyclic in the positive orientation; the result is not asserted for arbitrary ax+b action graphs.",
            "implication": "A nonzero positive primitive-cycle determinant cannot be extracted from this frozen graph without changing the source object.",
        },
        {
            "number": 2,
            "observation": "Symmetrization produced one primitive length-two immediate backtrack per frozen edge; Hashimoto exclusion removed all of these witnesses.",
            "interpretation": "The nonbacktracking repair solves the universal reverse-edge artifact only.",
            "implication": "It does not solve presentation-relation cycles.",
        },
        {
            "number": 3,
            "observation": "For r=2,3,4,5 at both bases, V U V^{-1} U^{-r} was admissible, primitive, cyclically nonbacktracking, and had length r+3; generic commutation and mutated monoid controls behaved the same way.",
            "interpretation": "Affine and commutation relations create generic reduced cycles independent of arithmetic acceptance labels.",
            "implication": "A Hashimoto ledger counts presentation geometry unless a further source-natural rule is proved.",
        },
        {
            "number": 4,
            "observation": "All 48 quotient rows preserved the labelled affine relation and also acquired U_q^q; small moduli retained polygon collapse, including r=2,q=2.",
            "interpretation": "Finite quotients reproduce relation words while adding quotient-clock cycles and geometric degeneracies.",
            "implication": "A quotient determinant cannot silently be identified with the infinite graph-step determinant.",
        },
        {
            "number": 5,
            "observation": "For both exact diagonal fixtures, [z^m](-log det(I-zD_beta))=Tr(D_beta^m)/m; the partition trace is only the linear coefficient, and det(I-D_beta)=0 at z=1 because n=1 contributes eigenvalue one.",
            "interpretation": "The diagonal trace, determinant germ, reciprocal determinant, and bosonic specialization are related but distinct objects.",
            "implication": "A same-source symbolic primitive interpretation requires a separate marker and whole-operator theorem.",
        },
        {
            "number": 6,
            "observation": "The evaluator-only prime-Fock product matched independent occupation enumeration through degree six; z counted particle number and z=1 gave a finite Euler specialization.",
            "interpretation": "The control deliberately preloads a prime-indexed one-particle basis after the neutral source was hashed.",
            "implication": "It is a marker firewall, not an advance of the affine source.",
        },
        {
            "number": 7,
            "observation": "Signed weights cancelled odd but not even power sums; a nonzero nilpotent matrix had determinant factor one; diag(1,-1) cancelled the first trace but not the second.",
            "interpretation": "Signed or matrix trace cancellation is weaker than literal deletion of primitive edge words.",
            "implication": "Groupoid, signed, and matrix successors remain open only with a source-natural all-orders and same-operator proof.",
        },
    ]
    status = "PASS" if evaluation["status"] == tests["status"] == "PASS" and counterexamples["unexpected_mismatches"] == [] else "FAIL"
    analysis = {
        "schema_version": "SD-C37-analysis-v1",
        "status": status,
        "summary_rows": summary_rows,
        "findings": findings,
        "counterexample_corrections_retained": counterexamples["all_expected_corrections_retained"],
        "statistical_note": "No stochastic estimate, floating-point tolerance, or multiple-seed mean is used; values are exact finite ledgers or deterministic controls.",
        "evidence_boundary": "Finite windows certify serialized formulas and witness families; infinite DAG, boundedness, noncompactness, and infinite-outdegree conclusions are theorem-owned by the mathematical lock.",
        "literature_boundary": "The primary literature contains genuine C*-partition and bosonic determinant constructions, but the source lock does not identify them with this graph-step primitive determinant.",
        "verdicts": [
            "GO_EXACT_AFFINE_BENCHMARK",
            "STOP_FULL_MONOID_FINITE_PRETENSE",
            "STOP_FINITE_QUOTIENT_LEDGER_DESCENT",
            "STOP_BC_TRACE_DETERMINANT_CONFLATION",
            "BOUNDARY_SIGNED_MATRIX_GROUPOID_OPEN",
            "ROUTE_A_NOT_ADVANCED"
        ],
        "route_tuple": evaluation["route_tuple"],
        "paper36_minimum_obligation": evaluation["paper36_minimum_obligation"],
    }
    (results / "analysis.json").write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    table_lines = [
        "| Block | Evidence class | Population | Metric | Value | Failures |",
        "|---|---|---:|---|---:|---:|",
    ]
    for row in summary_rows:
        table_lines.append(
            f"| {row['block']} | {row['evidence_class']} | {row['population']} | {row['primary_metric']} | {row['value']} | {row['failures']} |"
        )
    finding_lines: list[str] = []
    for finding in findings:
        finding_lines.extend(
            [
                f"{finding['number']}. Observation: {finding['observation']}",
                f"   Interpretation: {finding['interpretation']}",
                f"   Implication: {finding['implication']}",
                "",
            ]
        )
    report = "\n".join(
        [
            "# Paper 35 exact affine benchmark report",
            "",
            "## Exact evidence table",
            "",
            *table_lines,
            "",
            "The exhaustive claims are restricted to the frozen r/base/length and quotient ranges. Infinite operator conclusions remain theorem-owned by the mathematical lock.",
            "",
            "## Findings",
            "",
            *finding_lines,
            "## Route verdict",
            "",
            "The exact benchmark passes as a negative/correction benchmark. Route A is not advanced. The frozen route tuple is:",
            "",
            "```text",
            "(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL,",
            " A3_FAIL, A4_FAIL)",
            "```",
            "",
            "Paper 36 must exhibit source-natural cancellation or a quotient/induction with an explicit marker map and a same-whole-operator trace-log proof; otherwise this negative benchmark remains the conclusion.",
            "",
        ]
    )
    (results / "ANALYSIS_REPORT.md").write_text(report, encoding="utf-8")
    if status != "PASS":
        raise SystemExit("analysis gates failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
