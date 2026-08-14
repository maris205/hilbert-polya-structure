#!/usr/bin/env python3
"""Run, audit, freeze, and optionally double-run SD-C19 exact artifacts."""

from __future__ import annotations

import argparse
from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "results" / "SHA256SUMS.txt"


COMMANDS = (
    ("code/sdc19_fiber_cocycle_artin_experiment.py",),
    ("code/analyze_sdc19_fiber_cocycle_artin_results.py",),
    ("code/run_sdc19_fiber_cocycle_artin_tests.py",),
    ("code/audit_sdc19_artifact_integrity.py",),
    ("code/freeze_sdc19_fiber_cocycle_artin_artifacts.py",),
    ("code/freeze_sdc19_fiber_cocycle_artin_artifacts.py", "--check"),
)


def run_once() -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    for arguments in COMMANDS:
        subprocess.run(
            [sys.executable, *arguments],
            cwd=ROOT,
            env=environment,
            check=True,
        )
    return sha256(LEDGER.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify-byte-determinism",
        action="store_true",
        help="Run the entire suite twice and require an identical ledger hash.",
    )
    args = parser.parse_args()
    first = run_once()
    print(f"results_ledger_sha256={first}")
    if args.verify_byte_determinism:
        second = run_once()
        print(f"results_ledger_sha256_second_run={second}")
        if first != second:
            raise SystemExit("byte-determinism check failed")
        print("byte_determinism=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
