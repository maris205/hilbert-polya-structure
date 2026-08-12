#!/usr/bin/env python3
"""Generate the compact candidate table from the six Route-A YAML records."""

from pathlib import Path

import yaml


PAPER_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(__file__).resolve().parent / "table1_candidate_matrix.tex"
GATES = ("a0", "a1", "a2", "a3", "a4")

SUPPORTED = {
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A0_ANALYTIC_ARITHMETIC_ORIGIN",
    "A1_PASS_ANALYTIC",
    "A2_ANALYTIC_DETERMINANT",
}
PARTIAL = {
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_WEAK",
    "A3_PARTIAL_ANALYTIC_STRUCTURE",
    "A4_FORMAL_HINT",
}
FAILED = {"A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"}
EVIDENCE_LABELS = {
    "PROVED": "Proved",
    "MODELING_CHOICE": "Modeling choice",
    "NOT_TESTABLE": "Not testable",
}


def category(verdict: str) -> str:
    if verdict in FAILED:
        return "F"
    if verdict in PARTIAL:
        return "P"
    if verdict in SUPPORTED:
        return "S"
    raise ValueError(f"unrecognized evaluator verdict: {verdict!r}")


def tex_escape(value: str) -> str:
    return value.replace("_", r"\_")


def evidence_label(value: str) -> str:
    try:
        return EVIDENCE_LABELS[value]
    except KeyError as exc:
        raise ValueError(f"unrecognized evidence status: {value!r}") from exc


def main() -> None:
    records = []
    for path in sorted((PAPER_ROOT / "evaluations/route_a").glob("SD-C*/*.yaml")):
        with path.open(encoding="utf-8") as handle:
            records.append(yaml.safe_load(handle))
    if len(records) != 6:
        raise RuntimeError(f"expected six records, found {len(records)}")

    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Frozen same-object gate outcomes. S denotes local structural support, P denotes weak/partial/formal evidence, and F denotes failure. Route eligibility is the sequential conjunction on one row; all six Route-B flags are locked.}",
        r"\label{tab:candidate-matrix}",
        r"\small",
        r"\setlength{\tabcolsep}{4.2pt}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lcccccccl}",
        r"\toprule",
        r"Candidate & A0 & A1 & A2 & A3 & A4 & First block & Evidence & Status \\",
        r"\midrule",
    ]
    for record in records:
        gate_values = [category(record[gate]["verdict"]) for gate in GATES]
        if record["route_b_invocation_allowed"]:
            raise RuntimeError("Stage-01 table assumes the frozen Route-B lock")
        block_index = next(index for index, value in enumerate(gate_values) if value != "S")
        block_gate = GATES[block_index]
        status = {
            "ROUTE_A_REJECTED": "Rejected",
            "ROUTE_A_EXPLORATORY": "Exploratory",
        }.get(record["overall_verdict"])
        if status is None:
            raise ValueError(f"unrecognized overall verdict: {record['overall_verdict']!r}")
        fields = [
            tex_escape(record["candidate_id"]),
            *gate_values,
            block_gate.upper(),
            evidence_label(record[block_gate]["evidence_status"]),
            status,
        ]
        lines.append(" & ".join(fields) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}", ""])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
