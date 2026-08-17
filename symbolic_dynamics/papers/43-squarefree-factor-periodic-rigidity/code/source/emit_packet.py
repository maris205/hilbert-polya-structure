#!/usr/bin/env python3
"""Emit the canonical raw-only Paper 43 packet to stdout."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from source_core import build_packet, canonical


def main() -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("emit_packet.py requires python3 -I -B")
    sys.stdout.buffer.write(canonical(build_packet()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
