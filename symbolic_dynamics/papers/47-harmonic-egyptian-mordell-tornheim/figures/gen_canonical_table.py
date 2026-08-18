#!/usr/bin/env python3
"""Render exact P47 tables and a human-readable ledger from writer summary."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            indent=2,
            ensure_ascii=True,
            allow_nan=False,
            separators=(",", ": "),
        )
        + "\n"
    ).encode("ascii")


def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in items:
        if key in value:
            raise ValueError("duplicate")
        value[key] = item
    return value


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_summary(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=pairs)
    if raw != canonical(value) or value.get("status") != "PASS":
        raise SystemExit("SUMMARY_CANONICAL_STATUS")
    if value.get("schema") != "paper47.writer-canonical-summary.v1":
        raise SystemExit("SUMMARY_SCHEMA")
    return value, raw


def phase_table(payload: dict[str, Any]) -> bytes:
    phase = payload["operator_phase_certificate"]
    if (
        phase["bounded_compact"] != "Re_s_gt_0"
        or phase["hilbert_schmidt"] != "Re_s_gt_one_half"
        or phase["trace_class"] != "Re_s_gt_1"
    ):
        raise SystemExit("PHASE_VALUES")
    text = r"""% Generated mechanically by figures/gen_canonical_table.py.
\begin{table}[t]
\centering
\small
\begin{tabular}{lll}
\toprule
Property & Exact domain & Decisive boundary witness \\
\midrule
Bounded and compact & $\Re s>0$ & even loops / squarefree rows \\
Hilbert--Schmidt & $\Re s>\tfrac12$ & even-loop scale sum \\
Trace class & $\Re s>1$ & absolute even diagonal \\
$\det_2(I-zE_s)$ & $\Re s>\tfrac12$ & Hilbert--Schmidt wall \\
$\det(I-zE_s)$ & $\Re s>1$ & trace-class wall \\
\bottomrule
\end{tabular}
\caption{Sharp operator-ideal and determinant domains.  Every endpoint is
strict; the witnesses in the last column are analytic proof ingredients,
not finite-cutoff diagnostics.}
\label{tab:phase}
\end{table}
"""
    return text.encode("ascii")


def replay_table(payload: dict[str, Any]) -> bytes:
    checks = list(payload["comparison_checks"])
    if len(checks) != 12 or any(payload["comparison_checks"][key] != "PASS" for key in checks):
        raise SystemExit("CHECKS_EXACT12")
    cutoff_lines = "".join(
        f"{row['N']} & {row['ordered_edge_count']} & {row['loop_count']} \\\\\n"
        for row in payload["cutoffs"]
    )
    pairs_of_checks = list(zip(checks[:6], checks[6:], strict=True))
    check_lines = "".join(
        "\\texttt{\\detokenize{" + left + "}} & "
        "\\texttt{\\detokenize{" + right + "}} \\\\\n"
        for left, right in pairs_of_checks
    )
    text = (
        "% Generated mechanically by figures/gen_canonical_table.py.\n"
        "\\begin{table}[htbp]\n"
        "\\centering\n"
        "\\small\n"
        "\\begin{tabular}{rrr}\n"
        "\\toprule\n"
        "$N$ & Ordered edges & Loops \\\\\n"
        "\\midrule\n"
        + cutoff_lines
        + "\\bottomrule\n"
        "\\end{tabular}\n"
        "\\par\\vspace{0.45em}\n"
        "\\footnotesize\n"
        "\\begin{tabular}{p{0.47\\linewidth}p{0.47\\linewidth}}\n"
        "\\toprule\n"
        "\\multicolumn{2}{c}{Exact comparison keys (all PASS)} \\\\\n"
        "\\midrule\n"
        + check_lines
        + "\\bottomrule\n"
        "\\end{tabular}\n"
        "\\caption{Canonical State-A implementation replay.  The counts and\n"
        "comparison keys are extracted from two independent finite lanes.\n"
        "They validate implementation agreement and make no inference about\n"
        "an infinite endpoint.}\n"
        "\\label{tab:canonical-replay}\n"
        "\\end{table}\n"
    )
    return text.encode("ascii")


def ledger(
    payload: dict[str, Any], summary_sha: str, protected_sha: str,
) -> bytes:
    lines = [
        "# P47 canonical State-A writer ledger",
        "",
        "Status: `PASS / FINITE IMPLEMENTATION EVIDENCE ONLY`.",
        "",
        f"- protected 91-node manifest SHA-256: `{protected_sha}`;",
        f"- writer canonical summary SHA-256: `{summary_sha}`;",
        f"- State-A output tree SHA-256: `{payload['canonical_hashes']['state_a_output_tree_sha256']}`;",
        f"- State-A result-ledger SHA-256: `{payload['canonical_hashes']['result_ledger_sha256']}`;",
        f"- direct evaluator SHA-256: `{payload['canonical_hashes']['direct_sha256']}`;",
        f"- parameter evaluator SHA-256: `{payload['canonical_hashes']['parameter_sha256']}`;",
        f"- exact comparison SHA-256: `{payload['canonical_hashes']['comparison_sha256']}`.",
        "",
        "## Complete support cutoffs",
        "",
        "| N | Ordered edges | Loops |",
        "|---:|---:|---:|",
    ]
    for row in payload["cutoffs"]:
        lines.append(
            f"| {row['N']} | {row['ordered_edge_count']} | {row['loop_count']} |"
        )
    lines += ["", "## Exact comparison key set", ""]
    for key, value in payload["comparison_checks"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines += ["", "## N=128 exact rational trace controls", ""]
    for row in payload["finite_trace_controls"]:
        lines += [
            f"### s={row['s']}",
            "",
            f"- `Tr A_N`: `{row['trace_1']}`",
            f"- `Tr A_N^2`: `{row['trace_2']}`",
            "",
        ]
    mutation = payload["mutation_controls"]
    lines += [
        "## Adversarial and provenance controls",
        "",
        f"- theorem/governance: {mutation['theorem_instances']} instances, "
        f"{mutation['theorem_consumer_invocations']} consumer invocations;",
        f"- expanded nested: {mutation['expanded_instances']} instances, "
        f"{mutation['expanded_consumer_invocations']} consumer invocations;",
        f"- frozen external-auditor: {mutation['external_instances']} instances;",
        f"- survivors across these suites: {mutation['survivors']};",
        f"- Route: `{payload['route']['overall_verdict']}`, Route B invocation "
        f"allowed = `{str(payload['route']['route_b_invocation_allowed']).lower()}`.",
        "",
        "## Interpretation boundary",
        "",
        "These records establish finite exact agreement and artifact integrity.  "
        "They do not establish the infinite operator theorem, external novelty, "
        "or a spectral target.",
        "",
    ]
    return "\n".join(lines).encode("ascii")


def write_exclusive(path: Path, raw: bytes, root: Path) -> None:
    if not path.is_absolute() or root not in path.parents:
        raise SystemExit("OUTPUT_SCOPE")
    if path.parent.resolve(strict=True) != path.parent or os.path.lexists(path):
        raise SystemExit("OUTPUT_NOT_NEW")
    descriptor = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o644,
    )
    try:
        os.fchmod(descriptor, 0o644)
        offset = 0
        while offset < len(raw):
            offset += os.write(descriptor, raw[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--root", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    if not root.is_absolute() or root.is_symlink() or root.resolve(strict=True) != root:
        raise SystemExit("ROOT")
    summary, summary_raw = load_summary(root / "figures" / "data" / "canonical_summary.json")
    protected_raw = (root / "PROTECTED_STATEA_TREE.tsv").read_bytes()
    payload = summary["payload"]
    targets = [
        (root / "figures" / "generated" / "theorem_phase_table.tex", phase_table(payload)),
        (root / "figures" / "generated" / "canonical_replay_table.tex", replay_table(payload)),
        (root / "evidence" / "CANONICAL_RESULTS_LEDGER.md", ledger(payload, sha(summary_raw), sha(protected_raw))),
    ]
    if args.write:
        for path, raw in targets:
            write_exclusive(path, raw, root)
        print("WROTE " + " ".join(f"{path.name}={sha(raw)}" for path, raw in targets))
        return 0
    for path, raw in targets:
        if not path.is_file() or path.read_bytes() != raw:
            raise SystemExit(f"GENERATED_MISMATCH:{path.name}")
    print("PASS " + " ".join(f"{path.name}={sha(raw)}" for path, raw in targets))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
