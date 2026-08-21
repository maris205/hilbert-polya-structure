#!/usr/bin/env python3
"""Verify the static manifest, raw PREOUTPUT seal, modes, and hygiene."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
from pathlib import Path
from typing import Any


EXCLUDED = {"PREOUTPUT_SEAL.txt", "STATIC_MANIFEST.json"}
CACHES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
ANCHORS = ("STATIC_MANIFEST.json", "PREOUTPUT_SEAL.txt")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_root(root: Path) -> None:
    if not root.is_absolute():
        raise AssertionError("root path")
    metadata = os.lstat(root)
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise AssertionError("root node")
    if root.resolve(strict=True) != root:
        raise AssertionError("root resolution")


def require_anchor_nodes(root: Path) -> None:
    for name in ANCHORS:
        metadata = os.lstat(root / name)
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise AssertionError("excluded anchor node")


def manifest_rows(root: Path) -> list[dict[str, Any]]:
    rows = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        if rel in EXCLUDED or rel == "outputs" or rel.startswith("outputs/"):
            continue
        metadata = os.lstat(path)
        if path.name in CACHES or path.name.endswith((".pyc", ".pyo")) or path.name == ".git":
            raise AssertionError("cache or Git metadata")
        upper_name = path.name.upper()
        if path.name in {"README", "README.md", "README.txt"} or path.suffix.lower() in {".pdf", ".tex"} or upper_name.startswith("PAPER_MANIFEST") or ("PUBLICATION" in upper_name and "SEAL" in upper_name):
            raise AssertionError("forbidden static artifact")
        if stat.S_ISLNK(metadata.st_mode):
            raise AssertionError("symlink")
        mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode):
            if mode != "0755":
                raise AssertionError("directory mode")
            rows.append({"kind": "directory", "mode": mode, "path": rel})
        elif stat.S_ISREG(metadata.st_mode):
            if mode != "0644":
                raise AssertionError("file mode")
            rows.append({"kind": "regular", "mode": mode, "path": rel, "sha256": sha(path), "size": metadata.st_size})
        else:
            raise AssertionError("nonregular")
    return rows


def verify_outputs(root: Path) -> None:
    output = root / "outputs"
    try:
        metadata = os.lstat(output)
    except FileNotFoundError:
        return
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise AssertionError("outputs type")
    if sorted(path.name for path in output.iterdir()) != ["state_A"]:
        raise AssertionError("outputs namespace")
    for path in output.rglob("*"):
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode) or (not stat.S_ISDIR(metadata.st_mode) and not stat.S_ISREG(metadata.st_mode)) or path.name in CACHES or path.name.endswith((".pyc", ".pyo")):
            raise AssertionError("outputs hygiene")
        expected = 0o755 if stat.S_ISDIR(metadata.st_mode) else 0o644
        if stat.S_IMODE(metadata.st_mode) != expected:
            raise AssertionError("outputs mode")


def verify_seal(root: Path, manifest: dict[str, Any]) -> None:
    raw = (root / "PREOUTPUT_SEAL.txt").read_bytes()
    if not raw.endswith(b"\n") or any(byte > 127 for byte in raw):
        raise AssertionError("seal encoding")
    lines = raw.decode("ascii").splitlines()
    if len(lines) != 10 or lines[0] != "PREOUTPUT_SEAL_V1" or not lines[-1].startswith("payload_sha256="):
        raise AssertionError("seal shape")
    payload = ("\n".join(lines[:-1]) + "\n").encode("ascii")
    if lines[-1] != "payload_sha256=" + hashlib.sha256(payload).hexdigest():
        raise AssertionError("seal payload digest")
    fields = dict(line.split("=", 1) for line in lines[1:-1])
    if fields != {
        "candidate_output_count": "0",
        "input_lock_sha256": sha(root / "contracts" / "INPUT_LOCK.json"),
        "manifest_entry_count": str(manifest["payload"]["entry_count"]),
        "manifest_sha256": sha(root / "STATIC_MANIFEST.json"),
        "project_slug": manifest["payload"]["project_slug"],
        "route_id": "UNASSIGNED",
        "state": "A",
        "status": "HOLD_FOR_FRESH_INDEPENDENT_PRE_RUN_REAUDIT",
    }:
        raise AssertionError("seal fields")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--phase", choices=("PREOUTPUT", "RERUN"), required=True)
    args = parser.parse_args()
    root = Path(args.root)
    try:
        require_root(root)
        require_anchor_nodes(root)
        verify_outputs(root)
        if args.phase == "PREOUTPUT" and (root / "outputs").exists():
            raise AssertionError("outputs present")
        if args.phase == "RERUN" and not (root / "outputs" / "state_A").is_dir():
            raise AssertionError("missing installed output")
        manifest = json.loads((root / "STATIC_MANIFEST.json").read_text(encoding="ascii"))
        contract = json.loads((root / "contracts" / "PROJECT_CONTRACT.json").read_text(encoding="ascii"))
        if manifest["payload"]["project_slug"] != contract["project_slug"]:
            raise AssertionError("manifest/contract slug")
        rows = manifest_rows(root)
        if manifest != {"payload": {"entry_count": len(rows), "excluded": ["PREOUTPUT_SEAL.txt", "STATIC_MANIFEST.json", "outputs"], "project_slug": manifest["payload"]["project_slug"], "rows": rows}, "schema": "stage0-static-manifest-v1", "status": "SEALED"}:
            raise AssertionError("manifest")
        verify_seal(root, manifest)
        output = {"payload": {"manifest_entry_count": len(rows), "manifest_sha256": sha(root / "STATIC_MANIFEST.json"), "preoutput_seal_sha256": sha(root / "PREOUTPUT_SEAL.txt"), "project_slug": manifest["payload"]["project_slug"]}, "schema": "stage0-static-audit-v1", "status": "PASS"}
        sys.stdout.buffer.write(canonical(output))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
        sys.stdout.buffer.write(canonical({"payload": {"code": "REJECT_STATIC_TREE"}, "schema": "stage0-static-audit-v1", "status": "REJECT"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
