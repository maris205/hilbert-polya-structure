#!/usr/bin/env python3
"""Emit the frozen source fixture packet without making scientific decisions."""

from __future__ import annotations

import json
from pathlib import Path
import sys


SOURCE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SOURCE_DIR))

from source_core import build_source_fixtures  # noqa: E402


def canonical_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True) + "\n").encode("ascii")


def main() -> int:
    sys.stdout.buffer.write(canonical_bytes(build_source_fixtures()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
