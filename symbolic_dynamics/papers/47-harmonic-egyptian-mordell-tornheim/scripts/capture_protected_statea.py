#!/usr/bin/env python3
"""Capture and replay the immutable P47 Stage0 + State-A authority tree.

The script is read-only with respect to the authority and integration
candidate.  It writes only caller-declared new files under the writer root.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


HEADER = "relative_path\tkind\tmode\tsize\tsha256\n"
EXPECTED_NODE_COUNT = 91
EXPECTED_REGULAR_COUNT = 67
EXPECTED_DIRECTORY_COUNT = 24
EXPECTED_STAGE0_NODE_COUNT = 62
EXPECTED_OUTPUT_NODE_COUNT = 29
EXPECTED_STATEA_OUTPUT_FILES = 20
EXPECTED_STATIC_FILES = 47


def canonical(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            indent=2,
            ensure_ascii=True,
            allow_nan=False,
            separators=(",", ": "),
        )
        + "\n"
    ).encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def inspect(path: Path) -> tuple[str, str, str, str]:
    info = os.lstat(path)
    mode = f"{stat.S_IMODE(info.st_mode):04o}"
    if stat.S_ISREG(info.st_mode):
        raw = path.read_bytes()
        return "regular", mode, str(len(raw)), digest(raw)
    if stat.S_ISDIR(info.st_mode):
        return "directory", mode, "-", "-"
    raise SystemExit(f"NONREGULAR_NODE:{path}")


def capture(root: Path) -> list[tuple[str, str, str, str, str]]:
    nodes = [root, *root.rglob("*")]
    rows: list[tuple[str, str, str, str, str]] = []
    for path in nodes:
        relative = "." if path == root else path.relative_to(root).as_posix()
        if "\\" in relative or "\0" in relative:
            raise SystemExit("UNSAFE_RELATIVE_PATH")
        rows.append((relative, *inspect(path)))
    rows.sort(key=lambda row: row[0])
    if len({row[0] for row in rows}) != len(rows):
        raise SystemExit("DUPLICATE_PATH")
    return rows


def without_root_rows(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        kind, mode, _size, sha256 = inspect(path)
        row: dict[str, Any] = {"kind": kind, "mode": mode, "path": relative}
        if kind == "regular":
            row["sha256"] = sha256
        rows.append(row)
    return sorted(rows, key=lambda row: row["path"])


def manifest_bytes(rows: list[tuple[str, str, str, str, str]]) -> bytes:
    return (
        HEADER
        + "".join("\t".join(row) + "\n" for row in rows)
    ).encode("ascii")


def static_sums_bytes(
    rows: list[tuple[str, str, str, str, str]],
) -> bytes:
    selected = [
        row for row in rows
        if row[1] == "regular"
        and row[0] != "."
        and row[0] != "outputs"
        and not row[0].startswith("outputs/")
    ]
    if len(selected) != EXPECTED_STATIC_FILES:
        raise SystemExit("STATIC_FILE_COUNT")
    return "".join(f"{row[4]}  {row[0]}\n" for row in selected).encode("ascii")


def write_exclusive(path: Path, raw: bytes, writer_root: Path) -> None:
    if not path.is_absolute() or writer_root not in path.parents:
        raise SystemExit("OUTPUT_OUTSIDE_WRITER_ROOT")
    if path.parent.resolve(strict=True) != path.parent or os.path.lexists(path):
        raise SystemExit("OUTPUT_NOT_NEW")
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


def check_root(path: Path, label: str) -> Path:
    if not path.is_absolute() or path.is_symlink():
        raise SystemExit(f"UNSAFE_{label}_ROOT")
    resolved = path.resolve(strict=True)
    if resolved != path or not path.is_dir():
        raise SystemExit(f"UNSAFE_{label}_ROOT")
    return path


def build(
    authority: Path,
    stage0: Path,
) -> tuple[bytes, bytes, bytes]:
    first = capture(authority)
    regular_count = sum(row[1] == "regular" for row in first)
    directory_count = sum(row[1] == "directory" for row in first)
    if (
        len(first) != EXPECTED_NODE_COUNT
        or regular_count != EXPECTED_REGULAR_COUNT
        or directory_count != EXPECTED_DIRECTORY_COUNT
    ):
        raise SystemExit("AUTHORITY_EXACT91")

    stage0_live = [
        row for row in first
        if row[0] == "."
        or (row[0] != "outputs" and not row[0].startswith("outputs/"))
    ]
    stage0_snapshot = capture(stage0)
    if len(stage0_live) != EXPECTED_STAGE0_NODE_COUNT:
        raise SystemExit("LIVE_STAGE0_SCOPE")
    if stage0_snapshot != stage0_live:
        raise SystemExit("SEALED_STAGE0_MISMATCH")

    output_live = [
        row for row in first
        if row[0] == "outputs" or row[0].startswith("outputs/")
    ]
    if len(output_live) != EXPECTED_OUTPUT_NODE_COUNT:
        raise SystemExit("STATEA_OUTPUT_SCOPE")
    output_files = sum(row[1] == "regular" for row in output_live)
    if output_files != EXPECTED_STATEA_OUTPUT_FILES:
        raise SystemExit("STATEA_OUTPUT_FILE_COUNT")

    seal_path = authority / "PREOUTPUT_STATIC_SEAL.json"
    seal_raw = seal_path.read_bytes()
    seal = json.loads(seal_raw.decode("ascii"))
    if canonical(seal) != seal_raw:
        raise SystemExit("NONCANONICAL_SEAL")
    expected_tree_sha256 = seal["smoke"]["state_A_final_tree_sha256"]
    observed_output_rows = without_root_rows(authority / "outputs")
    observed_tree_sha256 = digest(canonical(observed_output_rows))
    if observed_tree_sha256 != expected_tree_sha256:
        raise SystemExit("STATEA_TREE_SEAL_MISMATCH")

    ledger_path = authority / "outputs" / "RESULT_LEDGER.json"
    ledger_raw = ledger_path.read_bytes()
    ledger = json.loads(ledger_raw.decode("ascii"))
    if canonical(ledger) != ledger_raw or ledger.get("status") != "PASS":
        raise SystemExit("LEDGER_CANONICAL_STATUS")
    if ledger.get("payload", {}).get("state") != "A":
        raise SystemExit("LEDGER_NOT_STATE_A")

    second = capture(authority)
    if second != first:
        raise SystemExit("AUTHORITY_CHANGED_DURING_CAPTURE")

    manifest = manifest_bytes(first)
    static_sums = static_sums_bytes(first)
    replay = canonical({
        "payload": {
            "authority_capture_repetitions_equal": True,
            "authority_mutations": 0,
            "live_directory_count": directory_count,
            "live_mismatch_count": 0,
            "live_node_count": len(first),
            "live_regular_count": regular_count,
            "manifest_sha256": digest(manifest),
            "sealed_stage0_mismatch_count": 0,
            "sealed_stage0_node_count": len(stage0_snapshot),
            "state_a_output_directory_count_including_root": (
                len(output_live) - output_files
            ),
            "state_a_output_file_count": output_files,
            "state_a_output_node_count": len(output_live),
            "state_a_output_tree_sha256": observed_tree_sha256,
            "state_a_result_ledger_sha256": digest(ledger_raw),
            "static_file_count": EXPECTED_STATIC_FILES,
            "static_sums_sha256": digest(static_sums),
        },
        "schema": "paper47.protected-statea-replay.v1",
        "status": "PASS",
    })
    return manifest, static_sums, replay


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--authority", required=True)
    parser.add_argument("--stage0", required=True)
    parser.add_argument("--writer-root", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()

    authority = check_root(Path(args.authority), "AUTHORITY")
    stage0 = check_root(Path(args.stage0), "STAGE0")
    writer_root = check_root(Path(args.writer_root), "WRITER")
    manifest, static_sums, replay = build(authority, stage0)
    targets = [
        (writer_root / "PROTECTED_STATEA_TREE.tsv", manifest),
        (writer_root / "STATIC_INPUT_SHA256SUMS.txt", static_sums),
        (writer_root / "evidence" / "PROTECTED_STATEA_REPLAY.json", replay),
    ]
    if args.write:
        for path, raw in targets:
            write_exclusive(path, raw, writer_root)
        print(
            "WROTE "
            f"nodes={EXPECTED_NODE_COUNT} "
            f"manifest_sha256={digest(manifest)} "
            f"replay_sha256={digest(replay)}"
        )
        return 0
    for path, expected in targets:
        if not path.is_file() or path.read_bytes() != expected:
            raise SystemExit(f"CAPTURE_MISMATCH:{path.name}")
    print(
        "PASS "
        f"nodes={EXPECTED_NODE_COUNT} "
        f"manifest_sha256={digest(manifest)} "
        f"replay_sha256={digest(replay)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
