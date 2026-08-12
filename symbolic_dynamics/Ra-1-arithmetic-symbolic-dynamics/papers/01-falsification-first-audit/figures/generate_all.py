#!/usr/bin/env python3
"""Regenerate every data-driven figure and table in a deterministic order."""

from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
SCRIPTS = (
    "gen_fig1_route_a_matrix.py",
    "gen_fig2_finite_audits.py",
    "gen_table1_candidate_matrix.py",
)


def main() -> None:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(HERE / script)], cwd=HERE, check=True)


if __name__ == "__main__":
    main()
