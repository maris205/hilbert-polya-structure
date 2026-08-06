#!/usr/bin/env python3
"""Build a hash manifest for repository handoff without requiring Git metadata."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT_ROOT / "results" / "manifest.json"
EXCLUDED_NAMES = {
    "manifest.json",
    "__pycache__",
    ".pytest_cache",
    "main.aux",
    "main.bbl",
    "main.blg",
    "main.log",
    "main.out",
    "compile.log",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def git_state() -> dict[str, object]:
    result = subprocess.run(
        ["git", "-C", str(PROJECT_ROOT), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        return {
            "available": False,
            "commit": None,
            "reason": "project workspace is not a Git worktree",
        }
    commit = subprocess.run(
        ["git", "-C", str(PROJECT_ROOT), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    return {"available": True, "commit": commit, "reason": None}


def main() -> None:
    files = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_NAMES for part in path.parts):
            continue
        relative = path.relative_to(PROJECT_ROOT)
        files.append(
            {
                "path": relative.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    protocol = PROJECT_ROOT / "refine-logs" / "R000_FROZEN_PROTOCOL.json"
    protocol_payload = json.loads(protocol.read_text(encoding="utf-8"))
    payload = {
        "artifact_epoch_utc": protocol_payload["created_utc"],
        "project": PROJECT_ROOT.name,
        "git": git_state(),
        "frozen_protocol_sha256": sha256(protocol),
        "file_count": len(files),
        "files": files,
    }
    OUTPUT.write_text(
        json.dumps(payload, allow_nan=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(OUTPUT)
    print(f"files={len(files)}")


if __name__ == "__main__":
    main()
