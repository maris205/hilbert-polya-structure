#!/usr/bin/env python3
"""Run a source-seeded, split-gated floating carrier stress audit."""

from __future__ import annotations

import argparse

from _common import output_path, write_json_new
from branch_baker.audit import run_float_stress


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--split",
        choices=("development", "validation", "test"),
        default="development",
    )
    parser.add_argument(
        "--points",
        type=int,
        help="Number of points; defaults to the frozen 2^16",
    )
    parser.add_argument(
        "--steps",
        type=int,
        help="Per-point one-step checks; defaults to the frozen 256",
    )
    parser.add_argument(
        "--output",
        help="New JSON path; default is results/float_stress_<split>.json",
    )
    args = parser.parse_args()

    result = run_float_stress(
        split=args.split,
        points=args.points,
        steps=args.steps,
    )
    output = args.output or f"results/float_stress_{args.split}.json"
    target = output_path(output)
    write_json_new(target, result)
    print(target)
    if not result["passed"]:
        raise SystemExit("Floating stress audit failed")


if __name__ == "__main__":
    main()
