#!/usr/bin/env python3
"""Replay the exact combinatorial pilot twice and verify the sealed manifest."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_FILES = {
    "CANONICAL.txt",
    "COLLISION_FIREWALL.md",
    "OWNER_SEARCH_LOG.md",
    "PDD_THEOREM_SPIKE.md",
    "RCS_THEOREM_SPIKE.md",
    "README.md",
    "SCOUT_AND_KILL_LEDGER.md",
    "SELF_CHECK.md",
    "TITLE_COLLISION_INVENTORY.md",
    "self_check.py",
    "verify_combinatorial_lane.py",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fresh_run() -> bytes:
    result = subprocess.run(
        [sys.executable, "-B", str(ROOT / "verify_combinatorial_lane.py")],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.stderr:
        raise AssertionError(f"verifier wrote stderr: {result.stderr!r}")
    return result.stdout


def read_manifest() -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if name in entries:
            raise AssertionError(f"duplicate manifest entry: {name}")
        entries[name] = digest
    return entries


def main() -> None:
    checks = 0
    canonical = (ROOT / "CANONICAL.txt").read_bytes()
    first = fresh_run()
    checks += 1
    if first != canonical:
        raise AssertionError("fresh verifier run 1 differs from CANONICAL.txt")
    second = fresh_run()
    checks += 1
    if second != canonical:
        raise AssertionError("fresh verifier run 2 differs from CANONICAL.txt")
    checks += 1
    if first != second:
        raise AssertionError("fresh verifier runs are not byte-identical")

    entries = read_manifest()
    checks += 1
    if set(entries) != EXPECTED_FILES:
        raise AssertionError(
            f"manifest names differ: got={sorted(entries)} expected={sorted(EXPECTED_FILES)}"
        )
    checks += 1
    if "SHA256SUMS" in entries:
        raise AssertionError("SHA256SUMS must exclude itself")
    for name, expected in sorted(entries.items()):
        actual = sha256((ROOT / name).read_bytes())
        checks += 1
        if actual != expected:
            raise AssertionError(f"manifest mismatch {name}: {actual} != {expected}")

    print("P182_186_COMBINATORIAL_SELF_CHECK")
    print("fresh_runs=2")
    print(f"canonical_bytes={len(canonical)}")
    print(f"canonical_sha256={sha256(canonical)}")
    print(f"manifest_entries={len(entries)}")
    print(f"checks={checks}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()

