#!/usr/bin/env python3
"""Replay the portable 83-node P46 State-A snapshot without authority writes."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
from pathlib import Path
from typing import Any


HEADER = "relative_path\tkind\tmode\tsize\tsha256\n"
HEX64 = re.compile(r"[0-9a-f]{64}\Z")


def canonical(value: Any) -> bytes:
    return (
        json.dumps(
            value, sort_keys=True, indent=2, ensure_ascii=True,
            allow_nan=False, separators=(",", ": "),
        )
        + "\n"
    ).encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe_relative(value: str, allow_root: bool = False) -> bool:
    if not value or "\\" in value or "\0" in value \
            or any(ord(character) < 0x20 or ord(character) == 0x7f
                   for character in value):
        return False
    if allow_root and value == ".":
        return True
    path = Path(value)
    return not path.is_absolute() and value == path.as_posix() \
        and all(part not in {"", ".", ".."} for part in path.parts)


def parse_manifest(raw: bytes) -> list[dict[str, str]]:
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise SystemExit("MANIFEST_NONASCII") from error
    if not text.startswith(HEADER) or "\r" in text or not text.endswith("\n"):
        raise SystemExit("MANIFEST_FRAMING")
    rows = []
    for line in text.splitlines()[1:]:
        fields = line.split("\t")
        if len(fields) != 5:
            raise SystemExit("MANIFEST_FIELD_COUNT")
        relative, kind, mode, size, digest = fields
        if not safe_relative(relative, allow_root=True):
            raise SystemExit("MANIFEST_PATH")
        if kind == "regular":
            if mode not in {"0444", "0644"} or not size.isdigit() \
                    or not HEX64.fullmatch(digest):
                raise SystemExit("MANIFEST_REGULAR_ROW")
        elif kind == "directory":
            if mode not in {"0555", "0755"} or size != "-" or digest != "-":
                raise SystemExit("MANIFEST_DIRECTORY_ROW")
        else:
            raise SystemExit("MANIFEST_KIND")
        rows.append({"path": relative, "kind": kind, "mode": mode,
                     "size": size, "sha256": digest})
    paths = [row["path"] for row in rows]
    if len(rows) != 83 or paths != sorted(paths) or len(set(paths)) != len(paths) \
            or not paths or paths[0] != ".":
        raise SystemExit("MANIFEST_EXACT83")
    if sum(row["kind"] == "regular" for row in rows) != 60 \
            or sum(row["kind"] == "directory" for row in rows) != 23:
        raise SystemExit("MANIFEST_KIND_COUNTS")
    return rows


def observed(path: Path) -> tuple[str, str, str, str]:
    info = os.lstat(path)
    mode = f"{stat.S_IMODE(info.st_mode):04o}"
    if stat.S_ISREG(info.st_mode):
        raw = path.read_bytes()
        return "regular", mode, str(len(raw)), sha(raw)
    if stat.S_ISDIR(info.st_mode):
        return "directory", mode, "-", "-"
    return "other", mode, "-", "-"


def capture(root: Path, rows: list[dict[str, str]]) -> list[tuple[str, str, str, str, str]]:
    result = []
    for row in rows:
        relative = row["path"]
        path = root if relative == "." else root / relative
        result.append((relative, *observed(path)))
    return result


def exact_nodes(root: Path) -> set[Path]:
    return {root, *root.rglob("*")}


def write_exclusive(path: Path, raw: bytes) -> None:
    if not path.is_absolute() or Path("/tmp") not in path.parents \
            or path.parent.resolve(strict=True) != path.parent \
            or os.path.lexists(path):
        raise SystemExit("UNSAFE_OUTPUT")
    descriptor = os.open(
        path,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o644,
    )
    try:
        os.fchmod(descriptor, 0o644)
        offset = 0
        while offset < len(raw):
            offset += os.write(descriptor, raw[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--authority", required=True)
    parser.add_argument("--stage0-snapshot", required=True)
    parser.add_argument("--statea-snapshot", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--assert-output-new", action="store_true")
    args = parser.parse_args()
    if not args.assert_output_new:
        raise SystemExit("EXCLUSIVE_OUTPUT_ASSERTION_REQUIRED")
    manifest = Path(args.manifest).resolve(strict=True)
    authority = Path(args.authority).resolve(strict=True)
    stage0 = Path(args.stage0_snapshot).resolve(strict=True)
    statea = Path(args.statea_snapshot).resolve(strict=True)
    for label, root, expected_mode in [
        ("authority", authority, 0o755),
        ("stage0", stage0, 0o555),
        ("statea", statea, 0o555),
    ]:
        info = os.lstat(root)
        if not stat.S_ISDIR(info.st_mode) or stat.S_IMODE(info.st_mode) != expected_mode:
            raise SystemExit(f"ROOT_MODE:{label}")
    raw = manifest.read_bytes()
    if not HEX64.fullmatch(args.expected_manifest_sha256) \
            or sha(raw) != args.expected_manifest_sha256:
        raise SystemExit("MANIFEST_SHA256")
    rows = parse_manifest(raw)
    first = capture(authority, rows)
    expected = [
        (row["path"], row["kind"], row["mode"], row["size"], row["sha256"])
        for row in rows
    ]
    if first != expected:
        raise SystemExit("LIVE_AUTHORITY_MISMATCH")
    mapped: set[Path] = set()
    for row in rows:
        relative = row["path"]
        if relative == "outputs" or relative.startswith("outputs/"):
            snapshot = statea / relative
        else:
            snapshot = stage0 if relative == "." else stage0 / relative
        mapped.add(snapshot)
        kind, mode, _size, digest = observed(snapshot)
        expected_mode = "0444" if row["kind"] == "regular" else "0555"
        if kind != row["kind"] or mode != expected_mode \
                or (kind == "regular" and digest != row["sha256"]):
            raise SystemExit("SEALED_SNAPSHOT_MISMATCH:" + relative)
    stage_nodes = exact_nodes(stage0)
    output_root = statea / "outputs"
    output_nodes = exact_nodes(output_root)
    if len(stage_nodes) != 58 or len(output_nodes) != 25 \
            or stage_nodes | output_nodes != mapped:
        raise SystemExit("SEALED_SNAPSHOT_SCOPE")
    second = capture(authority, rows)
    if second != first:
        raise SystemExit("AUTHORITY_CHANGED_DURING_REPLAY")
    payload = {
        "authority_capture_repetitions_equal": True,
        "authority_mutations": 0,
        "live_directory_count": 23,
        "live_mismatch_count": 0,
        "live_node_count": 83,
        "live_regular_count": 60,
        "manifest_sha256": sha(raw),
        "snapshot_extra_count": 0,
        "snapshot_mismatch_count": 0,
        "snapshot_output_node_count": 25,
        "snapshot_stage0_node_count": 58,
        "snapshot_union_node_count": 83,
    }
    result = canonical({
        "payload": payload,
        "schema": "paper46.protected-statea-replay.v1",
        "status": "PASS",
    })
    write_exclusive(Path(args.output), result)
    print(
        "PASS nodes=83 regular=60 directories=23 "
        f"manifest_sha256={sha(raw)} replay_sha256={sha(result)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
