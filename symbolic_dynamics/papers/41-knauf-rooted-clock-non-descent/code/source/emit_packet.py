#!/usr/bin/env python3
"""Emit the canonical Paper 41 source packet to stdout."""

from __future__ import annotations

import os
import sys
if not sys.flags.isolated:
    clean_environment = os.environ.copy()
    clean_environment.pop("PYTHONPATH", None)
    clean_environment.pop("PYTHONHOME", None)
    clean_environment["PYTHONNOUSERSITE"] = "1"
    os.execve(
        sys.executable,
        [sys.executable, "-I", "-B", os.path.abspath(__file__), *sys.argv[1:]],
        clean_environment,
    )
sys.dont_write_bytecode = True

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from source_core import build_packet, canonical_bytes


def main() -> int:
    sys.stdout.buffer.write(canonical_bytes(build_packet()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
