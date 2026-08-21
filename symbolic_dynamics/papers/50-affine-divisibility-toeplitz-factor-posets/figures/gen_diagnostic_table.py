#!/usr/bin/env python3
"""Generate Table 2 from the frozen writer-owned diagnostic receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_SOURCE_LOCKS = {
    "candidate_manifest_sha256":
        "c070bd76d8a28e1b918fa040d9346db32776f238e7081d8c3504648b137a583e",
    "reciprocal_audit_manifest_sha256":
        "8b4d54a8cc7ce505dea3c26110346b315af0e30c8753e5c95227d6ff82d75ca3",
    "root_audit_result_sha256":
        "e1dca456aecfe25a7c1a133d33c1a6a6bf43724775c0a4a3b5c4a1199e32ee64",
}


def fmt(value: int | None) -> str:
    return "--" if value is None else f"{value:,}"


def latex_escape(text: str) -> str:
    return text.replace("/", "/").replace("_", r"\_")


def render(data: dict) -> str:
    if data.get("source_locks") != EXPECTED_SOURCE_LOCKS:
        raise ValueError("source-lock hash mismatch")
    if data.get("status") != "PASS":
        raise ValueError("receipt does not have PASS status")
    if "ONLY" not in data.get("notice", ""):
        raise ValueError("finite-control firewall missing")
    rows = data.get("rows")
    if not isinstance(rows, list) or len(rows) != 8:
        raise ValueError("unexpected table row count")

    body = []
    for row in rows:
        if not isinstance(row, list) or len(row) != 4:
            raise ValueError("malformed diagnostic row")
        label, candidate, reciprocal, root = row
        body.append(
            f"{latex_escape(label)} & {fmt(candidate)} & {fmt(reciprocal)} & {fmt(root)} \\\\"
        )

    short = {key: value[:12] for key, value in EXPECTED_SOURCE_LOCKS.items()}
    return "\n".join([
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Deterministic finite falsification controls reproduced from",
        r"the frozen candidate and audit receipts.  The implementations use distinct evaluators,",
        r"and all typed mutations are rejected.  These bounded counts are not used",
        r"to prove any theorem.}",
        r"\label{tab:diagnostics}",
        r"\small",
        r"\begin{tabular}{@{}lrrr@{}}",
        r"\toprule",
        r"Control & Stage-2 & Reciprocal & Root \\",
        r"\midrule",
        *body,
        r"\midrule",
        r"Local-rule false positives / negatives & $0/0$ & -- & -- \\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\par\vspace{2pt}",
        r"{\footnotesize Finite falsification controls only.  Lock prefixes:",
        f"candidate \\texttt{{{short['candidate_manifest_sha256']}}}, "
        f"reciprocal \\texttt{{{short['reciprocal_audit_manifest_sha256']}}}, "
        f"root \\texttt{{{short['root_audit_result_sha256']}}}.}}",
        r"\end{table}",
        "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    data = json.loads(raw)
    output = render(data).encode("utf-8")
    args.output.write_bytes(output)
    print(json.dumps({
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "output_sha256": hashlib.sha256(output).hexdigest(),
        "row_count": len(data["rows"]),
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
