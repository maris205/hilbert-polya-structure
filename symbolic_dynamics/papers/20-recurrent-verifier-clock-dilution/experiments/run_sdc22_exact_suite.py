#!/usr/bin/env python3
"""Run, audit, freeze, and optionally double-run all SD-C22 artifacts."""

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
    ("code/sdc22_clock_dilution.py", "--output", "results"),
    ("code/run_sdc22_clock_dilution_tests.py",),
    ("code/analyze_sdc22_clock_dilution_results.py",),
    ("code/audit_sdc22_artifact_integrity.py",),
    ("code/freeze_sdc22_clock_dilution_artifacts.py",),
    ("code/freeze_sdc22_clock_dilution_artifacts.py", "--check"),
)


def run_once() -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
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
    parser.add_argument("--verify-byte-determinism", action="store_true")
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
