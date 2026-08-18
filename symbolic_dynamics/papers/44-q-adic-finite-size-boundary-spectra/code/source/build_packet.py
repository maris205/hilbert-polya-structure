#!/usr/bin/env python3
"""Build a result-free source binding packet; never expands fixtures."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


RAW_HASH = "2421795bb1d341805f185fd9941db6ba31d9c521e0cbe1ff28fb24a0617dba10"
PREAUTH_HASH = "1952daeee561e4b0e1d11795a9638803a288a1eecddab0702ebcfec95816a7fd"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate JSON key")
        output[key] = value
    return output


def checked(root: Path, relative: str) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe root")
    cursor = root
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe path")
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink")
    result = cursor.resolve(strict=True)
    if root.resolve(strict=True) not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    arguments = parser.parse_args()
    root = Path(arguments.root)
    raw_path = checked(root, "preauthority/RAW_INPUT_MANIFEST.json")
    manifest_path = checked(root, "preauthority/SHA256SUMS.txt")
    raw_bytes, manifest_bytes = raw_path.read_bytes(), manifest_path.read_bytes()
    if hashlib.sha256(raw_bytes).hexdigest() != RAW_HASH \
            or hashlib.sha256(manifest_bytes).hexdigest() != PREAUTH_HASH:
        raise ValueError("source binding drift")
    raw = json.loads(raw_bytes.decode("ascii"), object_pairs_hook=unique)
    if raw["contains_expected_outputs"] is not False:
        raise ValueError("raw source contains expected outputs")
    value = {
        "payload": {
            "contains_expanded_fixtures": False,
            "contains_expected_outputs": False,
            "evaluator_access": [
                "A_independent_parse_and_expand",
                "B_independent_parse_and_expand"
            ],
            "frozen_manifest_sha256": PREAUTH_HASH,
            "neutral_raw_manifest_sha256": RAW_HASH,
            "raw_schema": raw["schema_version"],
            "source_configuration_count": len(raw["source_configurations"]),
        },
        "schema": "paper44-result-free-source-packet-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
