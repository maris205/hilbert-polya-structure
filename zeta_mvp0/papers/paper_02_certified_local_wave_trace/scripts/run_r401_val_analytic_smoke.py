#!/usr/bin/env python3
"""Run the non-claiming Arb smoke preceding R401-VAL validated ODE work."""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path

from flint import __version__ as flint_version

from hp_candidate_search.validated_analytic import hash_files, run_analytic_smoke


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md"
RADIAL_PROOF = ROOT / "research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md"
WARPED_PROOF = ROOT / "research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md"
EXPECTED_HASHES = {
    str(PROTOCOL): "d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82",
    str(RADIAL_PROOF): "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    str(WARPED_PROOF): "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_analytic_smoke",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing result: {output}")
    output.mkdir(parents=True)

    actual_hashes = hash_files(EXPECTED_HASHES)
    hash_gates = {
        path: actual_hashes[path] == expected
        for path, expected in EXPECTED_HASHES.items()
    }
    runs = [
        run_analytic_smoke(precision=128),
        run_analytic_smoke(precision=256),
    ]
    overall = all(
        run["status"] == "PASS_IMPLEMENTATION_SMOKE" for run in runs
    ) and all(hash_gates.values())
    summary = {
        "status": "PASS_IMPLEMENTATION_SMOKE" if overall else "FAIL",
        "claim_level": "implementation only; no validated ODE or theorem-domain pass",
        "precision_runs": runs,
        "hash_gates": hash_gates,
        "actual_hashes": actual_hashes,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "python_flint": flint_version,
        },
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    report = f"""# R401-VAL Analytic Implementation Smoke

Overall status: **{summary['status']}**.

This run checks Arb-backed exact constants, zero-safe `exprel` and
`log1prel`, normal-coordinate reconstruction, analytic radial/warped period
bounds, and 60 parameterized shell-identity points at both 128-bit and
256-bit precision.

It is not a validated flow integration, does not close the global cover or
the local Krawczyk tree, and does not certify
`delta_tr > 0.01`.

- protocol hash gate: `{hash_gates[str(PROTOCOL)]}`
- radial proof hash gate: `{hash_gates[str(RADIAL_PROOF)]}`
- warped proof hash gate: `{hash_gates[str(WARPED_PROOF)]}`
- 128-bit status: `{runs[0]['status']}`
- 256-bit status: `{runs[1]['status']}`
"""
    (output / "R401_VAL_ANALYTIC_SMOKE_REPORT.md").write_text(
        report,
        encoding="utf-8",
    )
    print(json.dumps({"status": summary["status"], "output": str(output)}, indent=2))
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
