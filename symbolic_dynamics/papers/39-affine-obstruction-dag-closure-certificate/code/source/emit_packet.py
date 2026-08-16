#!/usr/bin/env python3
"""Emit one canonical Paper 39 source packet."""

from __future__ import annotations

import argparse
from pathlib import Path

from source_core import build_packet, canonical_bytes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-lock", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = build_packet(Path(args.input_lock))
    Path(args.output).write_bytes(canonical_bytes(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
