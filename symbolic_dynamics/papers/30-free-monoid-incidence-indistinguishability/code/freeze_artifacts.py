#!/usr/bin/env python3
"""Generate or verify the deterministic 31-entry SD-C32 SHA-256 ledger."""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "results" / "SHA256SUMS.txt"
EXPECTED_ENTRIES = 31


def artifact_paths() -> list[Path]:
    paths = [path for path in (ROOT / "code").glob("*.py") if path.is_file()]
    paths.extend(
        path
        for path in (ROOT / "results").iterdir()
        if path.is_file() and path != LEDGER
    )
    return sorted(paths, key=lambda path: path.relative_to(ROOT).as_posix())


def ledger_lines() -> list[str]:
    paths = artifact_paths()
    if len(paths) != EXPECTED_ENTRIES:
        raise RuntimeError(f"expected {EXPECTED_ENTRIES} artifacts, found {len(paths)}")
    return [
        f"{sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}"
        for path in paths
    ]


def verify() -> bool:
    return LEDGER.exists() and LEDGER.read_text(encoding="utf-8").splitlines() == ledger_lines()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        passed = verify()
        print(f"sha256_ledger_check={'PASS' if passed else 'FAIL'}")
        return 0 if passed else 1
    lines = ledger_lines()
    LEDGER.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} hashes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
