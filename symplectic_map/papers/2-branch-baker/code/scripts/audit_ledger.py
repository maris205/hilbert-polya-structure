#!/usr/bin/env python3
"""Run the independent high-precision parent-factor/count audit."""

from __future__ import annotations

import argparse

from _common import add_output_argument, output_path, write_json_new
from branch_baker.audit import independent_parent_audit


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--digits",
        type=int,
        help="Decimal precision; defaults to the frozen 100-digit scale",
    )
    parser.add_argument(
        "--max-period",
        type=int,
        help="Maximum parent period; defaults to the frozen period 20",
    )
    parser.add_argument(
        "--allow-reduced-precision-test-mode",
        action="store_true",
        help="Explicitly label a sub-100-digit diagnostic as test-only",
    )
    add_output_argument(parser, "results/parent_audit.json")
    args = parser.parse_args()

    result = independent_parent_audit(
        digits=args.digits,
        max_period=args.max_period,
        allow_reduced_precision=args.allow_reduced_precision_test_mode,
    )
    target = output_path(args.output)
    write_json_new(target, result)
    print(target)
    if not result["passed"]:
        raise SystemExit("Independent parent audit failed")


if __name__ == "__main__":
    main()
