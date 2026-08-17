#!/usr/bin/env python3
"""Emit the canonical SD-C42 source packet to stdout."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


def load_source_core() -> object:
    path = Path(__file__).resolve().with_name("source_core.py")
    spec = importlib.util.spec_from_file_location("paper40_source_core", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the physical source-core module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    sys.stdout.buffer.write(load_source_core().packet_bytes())


if __name__ == "__main__":
    main()
