#!/usr/bin/env python3
"""Independently replay the protected Paper 48 Integration State A.

The live authority and frozen Stage-0 input are read only.  The optional
record operation writes only two new support files below the writer root;
the portable protected manifest must already exist and match the replay.
"""

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
EXPECTED = {
    "live_nodes": 75,
    "live_regular": 57,
    "live_directories": 18,
    "stage0_nodes": 59,
    "stage0_regular": 44,
    "stage0_directories": 15,
    "output_nodes": 16,
    "output_regular": 13,
    "output_directories": 3,
}
ANCHORS = {
    "integration_contract_sha256":
        "dcbf0029c78362cd8a9ac1251873e16d34058a8b15d15533cabc1251d0d66157",
    "post_output_verdict_sha256":
        "6f69cddfd069d267e5a71f8ec342df71c31d456152a8ba910d93829daadcb5f9",
    "preauthority_manifest_sha256":
        "f5669e651c4c31ce860bad534d17e64956a8750412f74257d341810424252057",
    "preoutput_static_seal_sha256":
        "2726c5eac3ef0aed1e67158912b58ae1a8f98339573b683ba348bdf72171d02d",
    "state_a_tree_sha256":
        "c23b59034303af74f2a9433b92f9f5c1e1cce4510bd8032ef1214372390bda58",
    "static_tree_manifest_sha256":
        "663400efb19c6f4b31308de551a82e4f5ac12e78950e4309a20eaf26b7d188a0",
}
HEX64 = re.compile(r"[0-9a-f]{64}")


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


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_json(path: Path, label: str) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("ascii"))
    except Exception as error:
        raise SystemExit(f"{label}_JSON_INVALID:{type(error).__name__}") from error
    if type(value) is not dict or canonical(value) != raw:
        raise SystemExit(f"{label}_JSON_NONCANONICAL")
    return raw, value


def strict_root(path: Path, label: str) -> Path:
    if not path.is_absolute() or path.is_symlink():
        raise SystemExit(f"{label}_ROOT_INVALID")
    resolved = path.resolve(strict=True)
    metadata = os.lstat(path)
    if resolved != path or not stat.S_ISDIR(metadata.st_mode):
        raise SystemExit(f"{label}_ROOT_INVALID")
    return path


def inspect(path: Path) -> tuple[str, str, str, str]:
    metadata = os.lstat(path)
    mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
    if stat.S_ISDIR(metadata.st_mode):
        return "directory", mode, "-", "-"
    if stat.S_ISREG(metadata.st_mode):
        raw = path.read_bytes()
        return "regular", mode, str(len(raw)), sha(raw)
    raise SystemExit(f"NONREGULAR_NODE:{path}")


def capture(root: Path) -> list[tuple[str, str, str, str, str]]:
    rows = []
    for path in [root, *root.rglob("*")]:
        relative = "." if path == root else path.relative_to(root).as_posix()
        if "\\" in relative or "\x00" in relative:
            raise SystemExit("UNSAFE_RELATIVE_PATH")
        rows.append((relative, *inspect(path)))
    rows.sort(key=lambda row: os.fsencode(row[0]))
    if len(rows) != len({row[0] for row in rows}):
        raise SystemExit("DUPLICATE_PATH")
    return rows


def protected_bytes(rows: list[tuple[str, str, str, str, str]]) -> bytes:
    return (
        HEADER + "".join("\t".join(row) + "\n" for row in rows)
    ).encode("ascii")


def output_tree_sha256(authority: Path) -> str:
    output = authority / "outputs"
    rows: list[dict[str, Any]] = []
    for path in sorted(output.rglob("*"),
                       key=lambda item: os.fsencode(item.relative_to(output).as_posix())):
        relative = path.relative_to(output).as_posix()
        kind, mode, _size, digest = inspect(path)
        row: dict[str, Any] = {"kind": kind, "mode": mode, "path": relative}
        if kind == "regular":
            row["sha256"] = digest
        rows.append(row)
    return sha(canonical(rows))


def static_sums(rows: list[tuple[str, str, str, str, str]]) -> bytes:
    selected = [
        row for row in rows
        if row[1] == "regular"
        and row[0] != "outputs"
        and not row[0].startswith("outputs/")
    ]
    if len(selected) != EXPECTED["stage0_regular"]:
        raise SystemExit("STATIC_FILE_COUNT")
    return "".join(
        f"{row[4]}  {row[0]}\n" for row in selected
    ).encode("ascii")


def count(rows: list[tuple[str, str, str, str, str]], kind: str) -> int:
    return sum(row[1] == kind for row in rows)


def safe_new_output(path: Path, writer_root: Path, raw: bytes) -> None:
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


def build(
    authority: Path,
    stage0: Path,
    verdict_path: Path,
    manifest_path: Path,
) -> tuple[bytes, bytes, bytes]:
    first = capture(authority)
    second = capture(authority)
    if first != second:
        raise SystemExit("AUTHORITY_CHANGED_DURING_DOUBLE_CAPTURE")
    if (
        len(first) != EXPECTED["live_nodes"]
        or count(first, "regular") != EXPECTED["live_regular"]
        or count(first, "directory") != EXPECTED["live_directories"]
    ):
        raise SystemExit("LIVE_SCOPE_MISMATCH")

    stage0_live = [
        row for row in first
        if row[0] != "outputs" and not row[0].startswith("outputs/")
    ]
    frozen = capture(stage0)
    if stage0_live != frozen or (
        len(frozen) != EXPECTED["stage0_nodes"]
        or count(frozen, "regular") != EXPECTED["stage0_regular"]
        or count(frozen, "directory") != EXPECTED["stage0_directories"]
    ):
        raise SystemExit("FROZEN_STAGE0_MISMATCH")

    outputs = [
        row for row in first
        if row[0] == "outputs" or row[0].startswith("outputs/")
    ]
    if (
        len(outputs) != EXPECTED["output_nodes"]
        or count(outputs, "regular") != EXPECTED["output_regular"]
        or count(outputs, "directory") != EXPECTED["output_directories"]
    ):
        raise SystemExit("OUTPUT_SCOPE_MISMATCH")

    anchored_paths = {
        "PREOUTPUT_STATIC_SEAL.json": "preoutput_static_seal_sha256",
        "STATIC_TREE_MANIFEST.json": "static_tree_manifest_sha256",
        "contracts/INTEGRATION_CONTRACT.json": "integration_contract_sha256",
        "preauthority/SHA256SUMS.txt": "preauthority_manifest_sha256",
    }
    for relative, key in anchored_paths.items():
        if sha((authority / relative).read_bytes()) != ANCHORS[key]:
            raise SystemExit(f"ANCHOR_MISMATCH:{relative}")

    contract_raw, contract = canonical_json(
        authority / "contracts/INTEGRATION_CONTRACT.json", "INTEGRATION_CONTRACT"
    )
    if sha(contract_raw) != ANCHORS["integration_contract_sha256"]:
        raise SystemExit("INTEGRATION_CONTRACT_HASH")
    output_files = sorted(
        path.relative_to(authority / "outputs").as_posix()
        for path in (authority / "outputs").rglob("*") if path.is_file()
    )
    output_directories = sorted(
        path.relative_to(authority / "outputs").as_posix()
        for path in (authority / "outputs").rglob("*") if path.is_dir()
    )
    if output_files != sorted(contract.get("declared_state_a_files", [])) \
            or output_directories != sorted(contract.get("declared_output_directories", [])):
        raise SystemExit("DECLARED_OUTPUT_NAMESPACE_MISMATCH")
    canonical_mtime = contract.get("canonical_mtime_ns")
    if type(canonical_mtime) is not int or any(
        os.lstat(path).st_mtime_ns != canonical_mtime
        for path in [authority / "outputs", *(authority / "outputs").rglob("*")]
    ):
        raise SystemExit("OUTPUT_MTIME_MISMATCH")
    tree_sha256 = output_tree_sha256(authority)
    if tree_sha256 != ANCHORS["state_a_tree_sha256"]:
        raise SystemExit("STATE_A_TREE_MISMATCH")
    if (authority / "outputs/PAPER_MANIFEST.sha256").exists():
        raise SystemExit("STATE_A_PAPER_MANIFEST_FORBIDDEN")

    verdict_raw, verdict = canonical_json(verdict_path, "POST_OUTPUT_VERDICT")
    if sha(verdict_raw) != ANCHORS["post_output_verdict_sha256"] \
            or verdict.get("candidate_id") != "SD-C50" \
            or verdict.get("state") != "A" \
            or verdict.get("status") != "POST-OUTPUT CLEAN" \
            or verdict.get("anchors", {}).get("state_a_tree_sha256") != tree_sha256 \
            or verdict.get("no_drift", {}).get("git_tracked_changes") != 0:
        raise SystemExit("POST_OUTPUT_VERDICT_MISMATCH")

    manifest = protected_bytes(first)
    if manifest_path.read_bytes() != manifest:
        raise SystemExit("PROTECTED_MANIFEST_MISMATCH")
    sums = static_sums(first)
    replay = canonical({
        "anchors": {
            **ANCHORS,
            "protected_statea_manifest_sha256": sha(manifest),
            "static_input_sums_sha256": sha(sums),
        },
        "candidate_id": "SD-C50",
        "counts": EXPECTED,
        "evidence_boundary": (
            "Protected and finite replay checks validate bytes, metadata, and "
            "declared finite outputs; they are not proofs of infinite theorems."
        ),
        "replay": {
            "authority_double_capture_equal": True,
            "declared_output_namespace_exact": True,
            "frozen_stage0_exact": True,
            "live_manifest_exact": True,
            "output_canonical_mtime_exact": True,
            "post_output_verdict_exact": True,
            "state_a_tree_exact": True,
        },
        "schema": "paper48.writer-protected-statea-replay.v1",
        "status": "PASS",
    })
    return manifest, sums, replay


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--authority", required=True)
    parser.add_argument("--stage0", required=True)
    parser.add_argument("--post-output-verdict", required=True)
    parser.add_argument("--writer-root", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--record", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    authority = strict_root(Path(args.authority), "AUTHORITY")
    stage0 = strict_root(Path(args.stage0), "STAGE0")
    writer = strict_root(Path(args.writer_root), "WRITER")
    verdict = Path(args.post_output_verdict)
    if not verdict.is_absolute() or verdict.is_symlink() or not verdict.is_file():
        raise SystemExit("POST_OUTPUT_VERDICT_PATH_INVALID")
    manifest_path = writer / "PROTECTED_STATEA_TREE.tsv"
    _manifest, sums, replay = build(authority, stage0, verdict, manifest_path)
    targets = [
        (writer / "STATIC_INPUT_SHA256SUMS.txt", sums),
        (writer / "evidence/PROTECTED_STATEA_REPLAY.json", replay),
    ]
    if args.record:
        for path, raw in targets:
            safe_new_output(path, writer, raw)
        print(
            f"RECORDED protected_sha256={sha(manifest_path.read_bytes())} "
            f"replay_sha256={sha(replay)}"
        )
        return 0
    for path, expected in targets:
        if not path.is_file() or path.read_bytes() != expected:
            raise SystemExit(f"REPLAY_RECORD_MISMATCH:{path.name}")
    print(
        f"PASS protected_sha256={sha(manifest_path.read_bytes())} "
        f"replay_sha256={sha(replay)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
