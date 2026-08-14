#!/usr/bin/env python3
"""Rollback-safe group promotion for the three HCS-C51 frozen artifacts."""

from __future__ import annotations

import argparse
import os
import shutil
import uuid
from pathlib import Path


def promote(
    pairs: list[tuple[Path, Path]], inject_failure_after: int | None = None
) -> bool:
    if not pairs or len({target for _, target in pairs}) != len(pairs):
        raise ValueError("promotion targets must be nonempty and distinct")
    transaction = uuid.uuid4().hex
    staged: list[Path] = []
    backups: list[Path | None] = []
    promoted = 0
    try:
        for source, target in pairs:
            if not source.is_file():
                raise FileNotFoundError(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(f".{target.name}.{transaction}.new")
            shutil.copyfile(source, temporary)
            staged.append(temporary)
        for _, target in pairs:
            if target.exists():
                backup = target.with_name(f".{target.name}.{transaction}.bak")
                os.replace(target, backup)
                backups.append(backup)
            else:
                backups.append(None)
        for index, ((_, target), temporary) in enumerate(zip(pairs, staged), 1):
            os.replace(temporary, target)
            promoted = index
            if inject_failure_after == index:
                raise RuntimeError(f"injected promotion failure after move {index}")
    except Exception:
        for index, (_, target) in enumerate(pairs):
            if index < promoted and target.exists():
                target.unlink()
            backup = backups[index] if index < len(backups) else None
            if backup is not None and backup.exists():
                if target.exists():
                    target.unlink()
                os.replace(backup, target)
        for temporary in staged:
            if temporary.exists():
                temporary.unlink()
        for backup in backups:
            if backup is not None and backup.exists():
                backup.unlink()
        return False
    for backup in backups:
        if backup is not None and backup.exists():
            backup.unlink()
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", required=True, type=Path)
    parser.add_argument("--target", action="append", required=True, type=Path)
    parser.add_argument("--inject-failure-after", type=int)
    arguments = parser.parse_args()
    if len(arguments.source) != len(arguments.target):
        parser.error("--source and --target counts must match")
    injected = arguments.inject_failure_after
    if injected is None and os.environ.get("C51_INJECT_PROMOTION_FAILURE_AFTER"):
        injected = int(os.environ["C51_INJECT_PROMOTION_FAILURE_AFTER"])
    success = promote(list(zip(arguments.source, arguments.target)), injected)
    print("promotion=" + ("COMMITTED" if success else "ROLLED_BACK"))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
