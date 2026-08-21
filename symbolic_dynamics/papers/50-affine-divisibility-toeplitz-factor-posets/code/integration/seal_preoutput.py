#!/usr/bin/env python3
"""Write the raw payload-self-verifying PREOUTPUT seal."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path


ANCHORS = ("STATIC_MANIFEST.json", "PREOUTPUT_SEAL.txt")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_root_and_anchors(root: Path) -> None:
    if not root.is_absolute():
        raise ValueError("unsafe root path")
    metadata = os.lstat(root)
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise ValueError("unsafe root node")
    if root.resolve(strict=True) != root:
        raise ValueError("unsafe root resolution")
    for name in ANCHORS:
        metadata = os.lstat(root / name)
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError("unsafe excluded anchor")


def overwrite_regular(path: Path, payload: bytes) -> None:
    if not hasattr(os, "O_NOFOLLOW"):
        raise ValueError("O_NOFOLLOW unavailable")
    descriptor = os.open(path, os.O_WRONLY | os.O_NOFOLLOW)
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError("unsafe seal target")
        os.ftruncate(descriptor, 0)
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = -1
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    require_root_and_anchors(root)
    try:
        os.lstat(root / "outputs")
    except FileNotFoundError:
        pass
    else:
        raise ValueError("candidate is not output-free")
    contract = json.loads((root / "contracts" / "PROJECT_CONTRACT.json").read_text(encoding="utf-8"))
    manifest = json.loads((root / "STATIC_MANIFEST.json").read_text(encoding="ascii"))
    if manifest["payload"]["project_slug"] != contract["project_slug"]:
        raise ValueError("slug mismatch")
    lines = [
        "PREOUTPUT_SEAL_V1",
        f"project_slug={contract['project_slug']}",
        "state=A",
        "status=HOLD_FOR_FRESH_INDEPENDENT_PRE_RUN_REAUDIT",
        f"manifest_sha256={sha256(root / 'STATIC_MANIFEST.json')}",
        f"manifest_entry_count={manifest['payload']['entry_count']}",
        f"input_lock_sha256={sha256(root / 'contracts' / 'INPUT_LOCK.json')}",
        "candidate_output_count=0",
        "route_id=UNASSIGNED",
    ]
    payload = ("\n".join(lines) + "\n").encode("ascii")
    final = payload + f"payload_sha256={hashlib.sha256(payload).hexdigest()}\n".encode("ascii")
    if args.write:
        target = root / "PREOUTPUT_SEAL.txt"
        overwrite_regular(target, final)
    else:
        print(final.decode("ascii"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
