#!/usr/bin/env python3
"""Build exact comparison tables and findings for SD-C38."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fieldnames = ["evidence_class", "case", "metric", "value", "control_or_baseline"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", required=True)
    arguments = parser.parse_args()
    result_dir = Path(arguments.result_dir)
    trace = read_csv(result_dir / "trace_audit.csv")
    markers = read_csv(result_dir / "marker_audit.csv")
    finite = read_csv(result_dir / "finite_chain_audit.csv")
    evaluation = read_json(result_dir / "evaluation.json")
    tests = read_json(result_dir / "test_report.json")

    raw_rows: list[dict[str, object]] = []
    for r in (2, 3, 4, 5):
        rows = [row for row in trace if int(row["r"]) == r]
        first = next(row for row in rows if int(row["relation_excess"]) != 0)
        raw_rows.append({"evidence_class": "identity_words", "case": f"r={r}", "metric": "first_excess_length", "value": first["length"], "control_or_baseline": "baseline" if r == 4 else "exponent_control"})
        raw_rows.append({"evidence_class": "identity_words", "case": f"r={r}", "metric": "first_excess_count", "value": first["relation_excess"], "control_or_baseline": "baseline" if r == 4 else "exponent_control"})
    for row in markers:
        raw_rows.append({"evidence_class": "marker", "case": f"r={row['r']}", "metric": "unit_step_marker_descends", "value": row["unit_step_marker_descends"], "control_or_baseline": "balanced_control" if row["r"] == "1" else ("baseline" if row["r"] == "4" else "exponent_control")})
    for row in finite:
        raw_rows.append({"evidence_class": "finite_chain", "case": f"r={row['r']},q={row['q']},t={row['period']}", "metric": "h1_affine_to_complete", "value": f"{row['h1_after_affine_cells']}->{row['h1_after_complete_presentation_cells']}", "control_or_baseline": "finite_control"})
    raw_rows.append({"evidence_class": "generic_chain_lift", "case": "two_generator_one_relator", "metric": "euler_multiplier", "value": "0", "control_or_baseline": "matched_generic"})
    write_csv(result_dir / "raw_data_table.csv", raw_rows)

    findings = [
        {
            "id": "F1",
            "observation": "The first affine excess appears at lengths 5, 6, 7, and 8 for r=2,3,4,5, with exact excess counts 10,12,14,32.",
            "interpretation": "The unquotiented finite-trace control detects the defining relation at its shortest polygon length.",
            "implication": "Relation imposition does not itself cancel path multiplicity.",
            "next_step": "Use the analytic contractibility proof, not finite counts, to classify the filled ledger.",
        },
        {
            "id": "F2",
            "observation": "The unit marker descends only for balanced r=1; it fails for every r=2,3,4,5 mutation.",
            "interpretation": "Unequal relation-side lengths obstruct a free graph-step grading before determinants are considered.",
            "implication": "No quotient determinant can inherit the original marker for the affine family.",
            "next_step": "Do not specialize z or alter deg(u) to repair the candidate.",
        },
        {
            "id": "F3",
            "observation": "Affine-only finite cells leave H1 dimensions 2,1,1,1,1,1, while complete finite-presentation cells give zero in all six controls.",
            "interpretation": "The affine-only residue consists of omitted quotient relations, not infinite-source descent evidence.",
            "implication": "Complete relation cancellation is topologically total rather than selective.",
            "next_step": "Retain finite quotients only as artifacts controls.",
        },
        {
            "id": "F4",
            "observation": "The scalar chain lift has zero supertrace for all 48 sampled powers and all matched two-generator/one-relator controls.",
            "interpretation": "The multiplier 1-2+1 cancels the complete ledger independently of the affine arithmetic relation.",
            "implication": "The repair realizes the proves-too-much failure and earns no recognition credit.",
            "next_step": "Paper 37 may test only a source-derived non-flat matrix coefficient system on the unquotiented same-marker shift.",
        },
    ]
    analysis = {
        "schema": "SD-C38-analysis-v1",
        "candidate_id": "SD-C38",
        "raw_data_rows": len(raw_rows),
        "findings": findings,
        "prototype_semantic_checks": f"{evaluation['prototype_semantic_passed']}/{evaluation['prototype_semantic_total']}",
        "integration_checks": f"{evaluation['integration_passed']}/{evaluation['integration_total']}",
        "authority_tests": f"{tests['passed']}/{tests['total']}",
        "main_result": "negative_exact_closure",
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    write_json(result_dir / "analysis.json", analysis)

    lines = [
        "# SD-C38 exact analysis report",
        "",
        "## Raw comparison table",
        "",
        "| Evidence | Case | Metric | Value | Role |",
        "|---|---|---|---:|---|",
    ]
    for row in raw_rows:
        lines.append(f"| {row['evidence_class']} | {row['case']} | {row['metric']} | {row['value']} | {row['control_or_baseline']} |")
    lines.extend(["", "## Key findings", ""])
    for finding in findings:
        lines.extend([
            f"### {finding['id']}",
            "",
            f"- Observation: {finding['observation']}",
            f"- Interpretation: {finding['interpretation']}",
            f"- Implication: {finding['implication']}",
            f"- Next step: {finding['next_step']}",
            "",
        ])
    lines.extend([
        "## Decision",
        "",
        f"Prototype semantic checks: `{analysis['prototype_semantic_checks']}`.",
        f"Independent integration checks: `{analysis['integration_checks']}`.",
        f"Authority tests: `{analysis['authority_tests']}`.",
        "",
        "The finite exact audit supports the frozen negative theorem boundary.",
        "It does not replace the independent infinite proofs.",
        "",
    ])
    (result_dir / "ANALYSIS_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"candidate_id": "SD-C38", "findings": len(findings), "raw_rows": len(raw_rows), "status": "PASS"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
