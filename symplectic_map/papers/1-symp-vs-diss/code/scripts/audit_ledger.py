#!/usr/bin/env python3
"""Independently audit a periodic-orbit ledger with 80-digit mpmath arithmetic."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


CODE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.audit import audit_ledger_payload  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON produced by run_ledger.py")
    parser.add_argument("--output", type=Path, help="write audit JSON here instead of stdout")
    parser.add_argument("--digits", type=int, default=80)
    parser.add_argument("--max-newton-iterations", type=int, default=12)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # parse_float=str preserves the exact decimal token written by the ledger.
    payload = json.loads(args.input.read_text(encoding="utf-8"), parse_float=str)
    audit = audit_ledger_payload(
        payload,
        digits=args.digits,
        max_iterations=args.max_newton_iterations,
    )
    rendered = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
