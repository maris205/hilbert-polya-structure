#!/usr/bin/env python3
"""Thin entry point for the source-locked exact Hénon audit."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from henon_audit.cli import main


if __name__ == "__main__":
    raise SystemExit(main())

