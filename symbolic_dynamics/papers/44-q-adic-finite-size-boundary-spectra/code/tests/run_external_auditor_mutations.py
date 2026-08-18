#!/usr/bin/env python3
"""Physical static-tree negative controls for the frozen external auditor."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise ValueError("duplicate key")
        out[key] = value
    return out


def invoke(auditor: Path, root: Path, cwd: Path) -> tuple[int, dict[str, Any]]:
    process = subprocess.run([sys.executable, "-I", "-B", str(auditor), "--root", str(root)],
                             cwd=cwd, env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                                           "PYTHONPATH": "", "PYTHONDONTWRITEBYTECODE": "1"},
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    value = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
    if process.stdout != canonical(value) or process.stderr \
            or set(value) != {"payload", "schema", "status"} \
            or value["schema"] != "paper44-frozen-external-audit-v2":
        raise ValueError("external auditor envelope")
    return process.returncode, value


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", required=True)
    parser.add_argument("--scratch", required=True)
    args = parser.parse_args()
    root, scratch = Path(args.root), Path(args.scratch)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() \
            or not scratch.is_absolute() or scratch.exists() or scratch.is_symlink():
        raise ValueError("unsafe roots")
    scratch.mkdir(parents=True, mode=0o755)
    cwd = scratch / "unrelated"; cwd.mkdir(mode=0o755)
    auditor = (root / "external_auditor/frozen_auditor.py").resolve(strict=True)
    baseline_code, baseline = invoke(auditor, root, cwd)
    if baseline_code != 0 or baseline["status"] != "PASS": raise ValueError("baseline rejected")

    def byte_flip(clone: Path) -> None:
        path = clone / "README.md"; raw = bytearray(path.read_bytes()); raw[0] ^= 1
        path.write_bytes(bytes(raw))

    def chmod_file(clone: Path) -> None:
        (clone / "README.md").chmod(0o600)

    def empty_directory(clone: Path) -> None:
        (clone / "rogue-empty").mkdir(mode=0o755)

    def fifo(clone: Path) -> None:
        os.mkfifo(clone / "rogue-fifo", 0o644)

    def symlink(clone: Path) -> None:
        (clone / "rogue-link").symlink_to("README.md")

    def missing(clone: Path) -> None:
        (clone / "contracts/RESULT_SCHEMA.json").unlink()

    def reorder_manifest(clone: Path) -> None:
        path = clone / "STATIC_TREE_MANIFEST.json"
        value = json.loads(path.read_text(encoding="ascii"), object_pairs_hook=unique)
        value["payload"]["rows"][0], value["payload"]["rows"][1] = \
            value["payload"]["rows"][1], value["payload"]["rows"][0]
        path.write_bytes(canonical(value))

    def seal_extra(clone: Path) -> None:
        path = clone / "PREOUTPUT_STATIC_SEAL.json"
        value = json.loads(path.read_text(encoding="ascii"), object_pairs_hook=unique)
        value["undeclared"] = True
        path.write_bytes(canonical(value))

    cases: list[tuple[str, str, Callable[[Path], None]]] = [
        ("static_byte_flip", "STATIC_BYTE_DRIFT", byte_flip),
        ("static_file_mode", "STATIC_TREE_MISMATCH", chmod_file),
        ("static_extra_empty_directory", "STATIC_TREE_MISMATCH", empty_directory),
        ("static_fifo", "STATIC_TREE_MISMATCH", fifo),
        ("static_symlink", "SYMLINK_FORBIDDEN", symlink),
        ("static_file_missing", "STATIC_TREE_MISMATCH", missing),
        ("static_manifest_reorder", "STATIC_MANIFEST_HASH_MISMATCH", reorder_manifest),
        ("seal_extra_key", "SEAL_EXACT_OBJECT_INVALID", seal_extra),
    ]
    records = []
    for index, (identifier, expected, mutate) in enumerate(cases):
        clone = scratch / f"mutated_{index:02d}"
        shutil.copytree(root, clone, ignore=shutil.ignore_patterns("outputs"), copy_function=shutil.copy2)
        mutate(clone)
        code, envelope = invoke(auditor, clone, cwd)
        observed = envelope.get("payload", {}).get("code")
        if code != 2 or envelope.get("status") != "REJECT" or observed != expected:
            raise ValueError(f"static mutation survived {identifier}: {observed}")
        records.append({"expected_code": expected, "id": identifier, "observed_code": observed,
                        "outcome": "REJECT", "returncode": code})
    sys.stdout.buffer.write(canonical({
        "payload": {"case_count": len(records), "records": records, "survivor_count": 0},
        "schema": "paper44-external-auditor-mutations-v2", "status": "PASS",
    }))
    return 0


if __name__ == "__main__": raise SystemExit(main())
