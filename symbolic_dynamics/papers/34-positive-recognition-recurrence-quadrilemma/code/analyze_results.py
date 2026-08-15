#!/usr/bin/env python3
"""Build exact comparison tables and scoped findings for Paper 34."""

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

    graph_rows = load_csv(results / "graph_census.csv")
    exhaustive = [row for row in graph_rows if row["graph_family"] == "exhaustive"]
    controls = [row for row in graph_rows if row["graph_family"] != "exhaustive"]
    evaluation = load_json(results / "evaluation.json")
    tests = load_json(results / "test_report.json")
    neutral = load_json(results / "neutral_recognizer.json")
    inventories = load_csv(results / "inventory_controls.csv")
    kraft = load_csv(results / "kraft_clock_summary.csv")
    markers = load_csv(results / "marker_ledger.csv")

    def total(rows: list[dict[str, str]], key: str) -> int:
        return sum(int(row[key]) for row in rows)

    raw_table: list[dict[str, object]] = [
        {
            "block": "complete_graph_enumeration",
            "evidence_class": "COMPLETE_FOR_FROZEN_N_LE_4",
            "population": total(exhaustive, "graphs"),
            "primary_metric": "mixed_primitive_roots",
            "value": total(exhaustive, "mixed_roots"),
            "failures": total(exhaustive, "failures"),
            "scope_note": "all loop-allowed simple directed graph masks on 1..4 vertices",
        },
        {
            "block": "complete_shared_state_pairs",
            "evidence_class": "COMPLETE_FOR_FROZEN_N_LE_4",
            "population": total(exhaustive, "shared_pairs"),
            "primary_metric": "mixed_primitive_roots",
            "value": total(exhaustive, "shared_pairs"),
            "failures": 0,
            "scope_note": "cyclically distinct primitive simple cycles sharing a state",
        },
        {
            "block": "complete_repaired_connectors",
            "evidence_class": "COMPLETE_FOR_FROZEN_N_LE_4",
            "population": total(exhaustive, "connector_pairs"),
            "primary_metric": "mixed_primitive_roots",
            "value": total(exhaustive, "connector_pairs"),
            "failures": 0,
            "scope_note": "disjoint primitive cycles in one SCC; SCC paths may traverse cycle vertices",
        },
        {
            "block": "preregistered_connector_normal_form",
            "evidence_class": "COUNTEREXAMPLE_CENSUS",
            "population": total(graph_rows, "connector_pairs"),
            "primary_metric": "strict_external_witness_failures",
            "value": total(graph_rows, "strict_external_connector_failures"),
            "failures": total(graph_rows, "strict_external_connector_failures"),
            "scope_note": "same endpoints plus both interiors outside both cycles was too strong",
        },
        {
            "block": "hash_seeded_graph_controls",
            "evidence_class": "FINITE_DETERMINISTIC_CONTROL_NOT_EXHAUSTIVE",
            "population": total(controls, "graphs"),
            "primary_metric": "mixed_primitive_roots",
            "value": total(controls, "mixed_roots"),
            "failures": total(controls, "failures"),
            "scope_note": "64 SHA-seeded strongly connected graphs on 5..8 vertices",
        },
        {
            "block": "terminal_recognizer",
            "evidence_class": "EXACT_FINITE_IDENTITY",
            "population": neutral["dimension"],
            "primary_metric": "determinant_equal",
            "value": int(neutral["terminal_extension_equal"]),
            "failures": int(not neutral["terminal_extension_equal"]),
            "scope_note": "acyclic decision tails versus recurrent product",
        },
        {
            "block": "arbitrary_inventory_pruning",
            "evidence_class": "EXACT_FINITE_CONTROLS",
            "population": len(inventories),
            "primary_metric": "proper_supports_change_determinant",
            "value": sum(row["pruning_differs_when_proper_nonempty"] == "True" for row in inventories),
            "failures": sum(row["pruning_differs_when_proper_nonempty"] == "False" for row in inventories),
            "scope_note": "trial atom, square, Fibonacci, modular, SHA, matched SHA, all, empty",
        },
        {
            "block": "kraft_clock_proxy",
            "evidence_class": "FINITE_WITNESS_NOT_INFINITE_PROOF",
            "population": len(kraft),
            "primary_metric": "exact_configuration_passes",
            "value": sum(
                row["kraft_at_most_one"] == "True"
                and int(row["prefix_collisions"]) == 0
                and int(row["roof_sum_failures"]) == 0
                and int(row["powered_clock_failures"]) == 0
                for row in kraft
            ),
            "failures": evaluation["kraft_failure_count"],
            "scope_note": "q=2,3,4 and cutoffs 31,127,511,2047",
        },
        {
            "block": "first_return_marker",
            "evidence_class": "EXACT_FORMAL_POLYNOMIAL",
            "population": len(markers),
            "primary_metric": "raw_differs_but_z1_equal",
            "value": sum(
                row["formal_equal"] == "False" and row["equal_at_z_one"] == "True"
                for row in markers
            ),
            "failures": evaluation["marker_item_formal_equal_count"]
            + evaluation["marker_item_z_one_mismatch_count"],
            "scope_note": "raw z^ell versus induced z",
        },
        {
            "block": "independent_evaluator",
            "evidence_class": "INDEPENDENT_RECONSTRUCTION",
            "population": len(graph_rows),
            "primary_metric": "aggregate_rows_equal",
            "value": sum(row["all_fields_equal"] for row in evaluation["graph_comparisons"]),
            "failures": sum(not row["all_fields_equal"] for row in evaluation["graph_comparisons"]),
            "scope_note": "different SCC, cycle, root, path, and determinant algorithms",
        },
    ]
    write_csv(results / "raw_data_table.csv", raw_table)

    complete_graphs = total(exhaustive, "graphs")
    complete_shared = total(exhaustive, "shared_pairs")
    complete_connectors = total(exhaustive, "connector_pairs")
    complete_mixed = total(exhaustive, "mixed_roots")
    strict_failures = total(graph_rows, "strict_external_connector_failures")
    control_mixed = total(controls, "mixed_roots")
    findings = [
        {
            "number": 1,
            "observation": f"The preregistered strict connector normal form failed on {strict_failures} cycle pairs (including controls).",
            "interpretation": "One pair of attachment points need not admit two paths whose interiors simultaneously avoid both cycles.",
            "implication": "C2 is false as written, but this does not refute same-SCC positive concatenation closure.",
            "next_step": "Use arbitrary SCC paths P:u->v and Q:v->u; permit cycle traversal or distinct attachment points.",
        },
        {
            "number": 2,
            "observation": f"The repaired audit exhaustively checked {complete_graphs} graphs, {complete_shared} shared-state pairs and {complete_connectors} connector pairs, producing {complete_mixed} mixed roots with zero failures.",
            "interpretation": "Within the frozen positive finite class, cyclically distinct recurrent branches in one SCC close under concatenation to an additional primitive root.",
            "implication": "A literal one-orbit-per-label ledger must separate its recurrent cycles; this is finite evidence aligned with the independent theorem proof.",
            "next_step": "Promote only the repaired hypothesis, not the rejected strict normal form.",
        },
        {
            "number": 3,
            "observation": f"The 64 deterministic 5..8 vertex controls added {control_mixed} mixed roots with zero repaired-C2 failures.",
            "interpretation": "The mechanism is graph recurrence, not arithmetic inventory.",
            "implication": "These are finite controls and must not be merged with the complete n<=4 census.",
            "next_step": "Keep the complete/control evidence classes separate in any paper table.",
        },
        {
            "number": 4,
            "observation": "A 160-state exact adjacency with 34 acyclic decision states had the same Newton determinant as its 126-state recurrent product for all eight post-freeze inventories; every proper nonempty pruning changed it.",
            "interpretation": "Terminal recognition is determinant-neutral until rejected recurrent blocks are deleted.",
            "implication": "The selected determinant belongs to a label-dependent pruned operator, not to the unclassified recurrent object.",
            "next_step": "Reject terminal orbitification/pruning as same-object arithmetic emergence.",
        },
        {
            "number": 5,
            "observation": "All 12 q-ary/cutoff configurations passed prefix, Kraft, roof-share, and powered clock inequalities exactly.",
            "interpretation": "The finite artifacts instantiate the premises of the Kraft-clock argument without floating-point approximation.",
            "implication": "They are regression witnesses only; noncompactness remains an infinite weak-null theorem.",
            "next_step": "Cite the analytic proof for noncompactness and label the cutoff table as a proxy.",
        },
        {
            "number": 6,
            "observation": "All 17 raw cycle factors differed formally from first-return factors and agreed after z=1.",
            "interpretation": "Induction replaces graph-step length by return count.",
            "implication": "First return is valid only as a changed-marker object.",
            "next_step": "Enforce the z^ell-to-z firewall in subsequent candidates.",
        },
        {
            "number": 7,
            "observation": "The signed three-state control had determinant one, and orthogonal matrix branches killed mixed products while pure products survived.",
            "interpretation": "Positivity is the coefficientwise no-cancellation hypothesis.",
            "implication": "The prototype does not close signed, matrix, supertrace, or nonlocal-weight programs.",
            "next_step": "Any such successor must prove source-natural cancellation and same-marker operator ownership independently.",
        },
    ]
    analysis = {
        "schema_version": "P34-analysis-v1",
        "raw_data_table": raw_table,
        "findings": findings,
        "statistical_note": "No stochastic estimator or multiple-seed mean is used; every reported value is an exact census or deterministic finite control.",
        "verdicts": [
            "FAIL_PREREGISTERED_C2_NORMAL_FORM",
            "GO_REPAIRED_POSITIVE_RECURRENCE_OBSTRUCTION_FINITE_CERTIFICATE",
            "STOP_TERMINAL_PRUNING_OWNERSHIP",
            "STOP_FIRST_RETURN_SAME_MARKER",
            "KRAFT_CLOCK_PROXY_ONLY",
            "BOUNDARY_SIGNED_MATRIX_OPEN",
        ],
        "test_status": tests["status"],
        "independent_evaluation_status": evaluation["status"],
        "status": "PASS" if tests["status"] == evaluation["status"] == "PASS" else "FAIL",
    }
    (results / "analysis.json").write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    table_lines = [
        "| Block | Evidence class | Population | Metric | Value | Failures |",
        "|---|---:|---:|---|---:|---:|",
    ]
    for row in raw_table:
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
                f"   Next step: {finding['next_step']}",
                "",
            ]
        )
    report = "\n".join(
        [
            "# Paper 34 exact analysis report",
            "",
            "## Raw data table",
            "",
            *table_lines,
            "",
            "Complete enumeration is restricted to all graph masks on at most four vertices. Hash-seeded graphs, Kraft cutoffs, inventories, and marker checks are finite deterministic evidence and are not part of that exhaustive claim.",
            "",
            "## Key findings",
            "",
            *finding_lines,
            "## Suggested next experiments",
            "",
            "1. Prove the repaired arbitrary-path connector lemma with formal edge variables.",
            "2. Treat any signed or matrix successor as a new source-locked cancellation problem.",
            "3. Do not reopen residue/Manin or terminal-decider families.",
            "",
        ]
    )
    (results / "ANALYSIS_REPORT.md").write_text(report, encoding="utf-8")
    if analysis["status"] != "PASS":
        raise SystemExit("analysis gates failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
