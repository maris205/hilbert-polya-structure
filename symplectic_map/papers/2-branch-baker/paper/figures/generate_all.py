#!/usr/bin/env python3
"""Regenerate every branch-baker paper figure and verify both output formats."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


FIGURE_DIR = Path(__file__).resolve().parent
SCRIPTS = (
    "gen_fig1_carrier_obstruction.py",
    "gen_fig2_orbit_lattice.py",
    "gen_fig3_audit_panel.py",
)


def main() -> None:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(FIGURE_DIR / script)], check=True,
                       cwd=FIGURE_DIR)
    for script in SCRIPTS:
        stem = script.removeprefix("gen_").removesuffix(".py")
        for suffix in ("pdf", "png"):
            output = FIGURE_DIR / f"{stem}.{suffix}"
            if not output.is_file() or output.stat().st_size == 0:
                raise RuntimeError(f"missing or empty figure output: {output}")
            print(f"verified {output.name} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
