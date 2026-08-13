#!/usr/bin/env python3
"""Thin entry point for the source-locked exact audit."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from prime_multiplier.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
