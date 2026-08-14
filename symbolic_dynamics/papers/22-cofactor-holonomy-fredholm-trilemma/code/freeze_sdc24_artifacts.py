#!/usr/bin/env python3
"""Generate or verify the deterministic SD-C24 code/result SHA-256 ledger."""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "results" / "SHA256SUMS.txt"


def artifact_paths() -> list[Path]:
    paths = [path for path in (ROOT / "code").glob("*.py") if path.is_file()]
    paths.extend(
        path
        for path in (ROOT / "results").iterdir()
        if path.is_file() and path != LEDGER
    )
    return sorted(paths, key=lambda path: path.relative_to(ROOT).as_posix())


def ledger_lines() -> list[str]:
    return [
        f"{sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}"
        for path in artifact_paths()
    ]


def verify() -> bool:
    if not LEDGER.exists():
        return False
    expected = LEDGER.read_text(encoding="utf-8").splitlines()
    actual = ledger_lines()
    return expected == actual and all(
        sha256((ROOT / line.split("  ", 1)[1]).read_bytes()).hexdigest()
        == line.split("  ", 1)[0]
        for line in expected
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        passed = verify()
        print(f"sha256_ledger_check={'PASS' if passed else 'FAIL'}")
        return 0 if passed else 1
    LEDGER.write_text("\n".join(ledger_lines()) + "\n", encoding="utf-8")
    print(f"wrote {len(ledger_lines())} hashes to {LEDGER.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
