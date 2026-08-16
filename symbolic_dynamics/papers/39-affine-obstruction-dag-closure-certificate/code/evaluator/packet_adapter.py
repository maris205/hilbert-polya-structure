#!/usr/bin/env python3
"""Normalize raw or metadata-enveloped source packets without science logic."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def normalize(value: Any) -> dict[str, Any]:
    if isinstance(value, dict) and value.get("schema") == "paper39-source-packet-v1":
        return value
    if isinstance(value, dict) and set(value) == {"metadata", "payload"}:
        payload = value["payload"]
        if isinstance(payload, dict) and payload.get("schema") == "paper39-source-packet-v1":
            return payload
    raise ValueError("unsupported packet transport shape")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    value = json.loads(Path(args.input).read_text(encoding="utf-8"))
    Path(args.output).write_bytes(canonical_bytes(normalize(value)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
