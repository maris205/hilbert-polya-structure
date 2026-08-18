#!/usr/bin/env python3
"""Read-only replay of the frozen P45 authority perimeter."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import stat
from pathlib import Path


EXPECTED_SNAPSHOT_SHA256 = (
    "40c0d921d993b7e3401c2bdbbbe6eee3431aa4dc2f8c7603bf490b128c2794c4"
)
EXPECTED_ROWS = 50
EXPECTED_STATIC = 42
EXPECTED_RESULTS = 8


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(code: str, **details: object) -> None:
    print(json.dumps({"status": "FAIL", "code": code, **details}, sort_keys=True))
    raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--authority", type=Path, required=True)
    args = parser.parse_args()

    snapshot = args.snapshot.resolve()
    authority = args.authority.resolve()
    observed_snapshot_sha = sha256(snapshot)
    if observed_snapshot_sha != EXPECTED_SNAPSHOT_SHA256:
        fail(
            "SNAPSHOT_HASH_MISMATCH",
            expected=EXPECTED_SNAPSHOT_SHA256,
            observed=observed_snapshot_sha,
        )

    with snapshot.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    required = {
        "relative_path",
        "type",
        "mode",
        "uid",
        "gid",
        "size",
        "mtime_ns",
        "inode",
        "nlink",
        "device",
        "sha256",
    }
    if set(rows[0]) != required:
        fail("SNAPSHOT_SCHEMA_MISMATCH", columns=sorted(rows[0]))
    if len(rows) != EXPECTED_ROWS:
        fail("SNAPSHOT_ROW_COUNT_MISMATCH", expected=EXPECTED_ROWS, observed=len(rows))

    expected_paths = [row["relative_path"] for row in rows]
    if expected_paths != sorted(expected_paths) or len(set(expected_paths)) != len(expected_paths):
        fail("SNAPSHOT_PATH_ORDER_OR_UNIQUENESS_MISMATCH")
    results_count = sum(path.startswith("results/") for path in expected_paths)
    static_count = len(rows) - results_count
    if (static_count, results_count) != (EXPECTED_STATIC, EXPECTED_RESULTS):
        fail(
            "SNAPSHOT_PARTITION_MISMATCH",
            expected_static=EXPECTED_STATIC,
            expected_results=EXPECTED_RESULTS,
            observed_static=static_count,
            observed_results=results_count,
        )

    observed_paths: list[str] = []
    nonregular: list[str] = []
    for base, dirs, files in os.walk(authority, followlinks=False):
        base_path = Path(base)
        for name in list(dirs):
            path = base_path / name
            if path.is_symlink():
                nonregular.append(path.relative_to(authority).as_posix())
        for name in files:
            path = base_path / name
            rel = path.relative_to(authority).as_posix()
            mode = path.lstat().st_mode
            if stat.S_ISREG(mode):
                observed_paths.append(rel)
            else:
                nonregular.append(rel)
    if nonregular:
        fail("AUTHORITY_NONREGULAR_ENTRY", paths=sorted(nonregular))
    if sorted(observed_paths) != expected_paths:
        fail(
            "AUTHORITY_PATH_SET_MISMATCH",
            missing=sorted(set(expected_paths) - set(observed_paths)),
            extra=sorted(set(observed_paths) - set(expected_paths)),
        )

    fields_checked = [
        "type",
        "mode",
        "uid",
        "gid",
        "size",
        "mtime_ns",
        "inode",
        "nlink",
        "device",
        "sha256",
    ]
    mismatches: list[dict[str, object]] = []
    for row in rows:
        path = authority / row["relative_path"]
        info = path.lstat()
        observed = {
            "type": "regular" if stat.S_ISREG(info.st_mode) else "nonregular",
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "uid": str(info.st_uid),
            "gid": str(info.st_gid),
            "size": str(info.st_size),
            "mtime_ns": str(info.st_mtime_ns),
            "inode": str(info.st_ino),
            "nlink": str(info.st_nlink),
            "device": str(info.st_dev),
            "sha256": sha256(path),
        }
        changed = {
            field: {"expected": row[field], "observed": observed[field]}
            for field in fields_checked
            if row[field] != observed[field]
        }
        if changed:
            mismatches.append({"path": row["relative_path"], "fields": changed})
    if mismatches:
        fail("PROTECTED_METADATA_OR_BYTES_MISMATCH", mismatches=mismatches)

    print(
        json.dumps(
            {
                "authority": str(authority),
                "fields_checked": fields_checked,
                "protected_rows": len(rows),
                "results_rows": results_count,
                "snapshot_sha256": observed_snapshot_sha,
                "static_rows": static_count,
                "status": "PASS",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
