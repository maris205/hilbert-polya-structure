#!/usr/bin/env python3
"""Deterministic replay and manifest audit for the algebra-lane scout."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
VERIFY = ROOT / "verify_algebra_lane.py"
CANONICAL = ROOT / "CANONICAL.txt"
MANIFEST = ROOT / "MANIFEST.json"
SUMS = ROOT / "SHA256SUMS"


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def run_fresh() -> subprocess.CompletedProcess[bytes]:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [sys.executable, str(VERIFY)],
        cwd=ROOT.parents[3],
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def main() -> None:
    audit = Audit()
    canonical = CANONICAL.read_bytes()
    first = run_fresh()
    second = run_fresh()
    audit.check(first.returncode == 0, "first verifier process failed")
    audit.check(second.returncode == 0, "second verifier process failed")
    audit.check(first.stderr == b"", "first verifier emitted stderr")
    audit.check(second.stderr == b"", "second verifier emitted stderr")
    audit.check(first.stdout == second.stdout, "fresh-process stdout mismatch")
    audit.check(first.stdout == canonical, "stdout did not match canonical")
    audit.check(canonical.endswith(b"RESULT=PASS\n"), "canonical lacks PASS terminator")
    audit.check(b"BOXES=15\n" in canonical, "wrong box count")
    audit.check(b"TRANSITIONS=334363\n" in canonical, "wrong transition count")
    audit.check(b"ASSERTIONS=1707811\n" in canonical, "wrong assertion count")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = manifest["files"]
    audit.check(manifest["schema"] == "p182-p186-algebra-lane-manifest-v1", "wrong schema")
    audit.check(len(entries) == manifest["file_count"], "manifest count mismatch")
    manifest_map = {entry["path"]: entry for entry in entries}
    audit.check(len(manifest_map) == len(entries), "duplicate manifest path")
    for relative, entry in sorted(manifest_map.items()):
        path = ROOT / relative
        audit.check(path.is_file(), f"missing manifest file: {relative}")
        audit.check(path.stat().st_size == entry["bytes"], f"size mismatch: {relative}")
        audit.check(sha256(path) == entry["sha256"], f"hash mismatch: {relative}")

    sum_lines = [line for line in SUMS.read_text(encoding="utf-8").splitlines() if line]
    audit.check(len(sum_lines) == len(entries), "SHA256SUMS count mismatch")
    parsed_sums = {}
    for line in sum_lines:
        digest, relative = line.split("  ", 1)
        parsed_sums[relative] = digest
    audit.check(parsed_sums == {path: entry["sha256"] for path, entry in manifest_map.items()}, "SHA256SUMS disagrees with manifest")

    print("P182_P186_ALGEBRA_LANE_SELF_CHECK_V1")
    print("PROCESS_REPLAYS=2")
    print(f"CANONICAL_BYTES={len(canonical)}")
    print(f"MANIFEST_ENTRIES={len(entries)}")
    print(f"CHECKS={audit.count}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
