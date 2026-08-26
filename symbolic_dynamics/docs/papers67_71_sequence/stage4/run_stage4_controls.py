#!/usr/bin/env python3
"""Replay and persist the five deterministic Stage-4 proof controls."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTROLS = {
    "67-multiplicative-plaquette-matroid-complexity": "verify_plaquette_matroid.py",
    "68-complete-bipartite-homshift-conjugacies": "verify_complete_bipartite.py",
    "69-orientation-sensitive-surface-flat-sft": "verify_surface_flat_sft.py",
    "70-weighted-heisenberg-congruence-nullities": "verify_weighted_heisenberg.py",
    "71-zip-shift-degree-pressure": "verify_degree_pressure.py",
}


def main() -> None:
    for slug, script_name in CONTROLS.items():
        paper = ROOT / "papers" / slug
        command = ["python3", str(paper / "code" / script_name)]
        result = subprocess.run(command, cwd=paper, capture_output=True, text=True)
        receipt = result.stdout
        if result.stderr:
            receipt += "\n[stderr]\n" + result.stderr
        receipt += f"\n[exit {result.returncode}]\n"
        out = paper / "stage4" / "FINAL_CONTROL_RUN.out"
        out.write_text(receipt, encoding="utf-8")
        if result.returncode != 0:
            raise SystemExit(f"{slug}: control failed; see {out}")
        print(f"{slug}: PASS")


if __name__ == "__main__":
    main()
