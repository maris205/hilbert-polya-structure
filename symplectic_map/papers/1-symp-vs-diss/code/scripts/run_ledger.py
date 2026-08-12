#!/usr/bin/env python3
"""Generate deterministic periodic-orbit ledgers without arithmetic inputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


CODE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.cycles import build_orbit_ledger  # noqa: E402


UC = 1.5436890126920763


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--preset",
        choices=("positive-control", "uc-mixed", "both", "custom"),
        default="both",
    )
    parser.add_argument("--a", type=float, help="custom quadratic parameter")
    parser.add_argument("--rho", type=float, help="custom conformal factor")
    parser.add_argument("--max-period", type=int, default=None)
    parser.add_argument("--output", type=Path, help="write JSON here instead of stdout")
    return parser.parse_args()


def run(args: argparse.Namespace) -> dict[str, Any]:
    runs: list[dict[str, Any]] = []
    if args.preset in {"positive-control", "both"}:
        runs.append(
            build_orbit_ledger(
                a=6.0,
                rho=1.0,
                max_period=args.max_period or 8,
                regime="full_shift_positive_control",
            )
        )
    if args.preset in {"uc-mixed", "both"}:
        runs.append(
            build_orbit_ledger(
                a=UC,
                rho=1.0,
                max_period=args.max_period or 6,
                regime="exploratory_incomplete",
            )
        )
    if args.preset == "custom":
        if args.a is None or args.rho is None:
            raise SystemExit("--preset custom requires --a and --rho")
        runs.append(
            build_orbit_ledger(
                a=args.a,
                rho=args.rho,
                max_period=args.max_period or 6,
                regime="exploratory_incomplete",
            )
        )
    return {
        "experiment": "geometry_only_periodic_orbit_ledger",
        "source_lock": {
            "uses_prime_table": False,
            "uses_riemann_zeros": False,
            "tunes_parameters_to_external_arithmetic_targets": False,
        },
        "runs": runs,
    }


def main() -> None:
    args = parse_args()
    payload = run(args)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
