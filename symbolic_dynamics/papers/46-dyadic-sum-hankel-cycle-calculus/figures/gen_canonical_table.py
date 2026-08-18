#!/usr/bin/env python3
"""Render the P46 finite-replay LaTeX table from the sealed writer summary."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_SUMMARY_SHA256 = (
    "c86887d3e7e9602cfebaec3e0b03e534d243af576166115fd7825f130a8ec774"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    raw = Path(args.summary).read_bytes()
    if hashlib.sha256(raw).hexdigest() != EXPECTED_SUMMARY_SHA256:
        raise ValueError("canonical writer summary digest mismatch")
    value = json.loads(raw.decode("ascii"))
    if value.get("schema") != "paper46-writer-canonical-summary-v1" \
            or value.get("status") != "PASS":
        raise ValueError("canonical writer summary envelope")
    comparison = value["payload"]["comparison"]
    counts = comparison["case_counts"]
    rows = [
        ("Complete support cutoffs", counts["structural_cutoffs"],
         comparison["support_mismatch_count"]),
        ("Ordered dyadic label tuples", counts["cycle_ordered_label_tuples"],
         comparison["cycle_solution_mismatch_count"]),
        ("Exact rational finite traces", counts["finite_trace_cases"],
         comparison["finite_trace_mismatch_count"]),
    ]
    lines = [
        r"\begin{tabular}{@{}lrr@{}}",
        r"\toprule",
        r"Replay surface & Cases & Mismatches \\",
        r"\midrule",
    ]
    lines.extend(f"{name} & {count:,} & {mismatch} \\\\" for name, count, mismatch in rows)
    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    Path(args.output).write_text("\n".join(lines), encoding="ascii", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

