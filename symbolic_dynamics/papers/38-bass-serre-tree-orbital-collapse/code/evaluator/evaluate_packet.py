#!/usr/bin/env python3
"""Evaluate a Paper 38 source packet across a JSON-only boundary."""

from __future__ import annotations

import json
from pathlib import Path
import sys


EVALUATOR_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(EVALUATOR_DIR))

from independent_evaluator import evaluate  # noqa: E402


def canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=True) + "\n"
    ).encode("ascii")


def extract_fixtures(packet: object) -> dict[str, object]:
    if not isinstance(packet, dict):
        raise TypeError("source packet must be a JSON object")
    if "fixtures" not in packet:
        return packet
    allowed = {"fixtures", "transport_metadata"}
    unknown = set(packet) - allowed
    if unknown:
        raise ValueError(f"unknown transport envelope keys: {sorted(unknown)!r}")
    fixtures = packet["fixtures"]
    if not isinstance(fixtures, dict):
        raise TypeError("fixtures must be a JSON object")
    return fixtures


def main() -> int:
    packet = json.load(sys.stdin)
    sys.stdout.buffer.write(canonical_bytes(evaluate(extract_fixtures(packet))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
