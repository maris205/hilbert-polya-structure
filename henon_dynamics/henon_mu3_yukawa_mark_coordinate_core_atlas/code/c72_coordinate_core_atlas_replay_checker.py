#!/usr/bin/env python3
"""Clean-process replay for the C72 independent checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c72_coordinate_core_atlas_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c72_coordinate_core_atlas_checker.py"


def main() -> None:
    expected = json.loads(EVIDENCE.read_text())
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["status"] == "PASS"
    assert result["subset_count"] == expected["support_atlas"]["subset_count"]
    assert result["core_subgroup_count"] == expected["subgroup_lattice_atlas"]["all_subgroup_count"]
    assert result["minimal_generating_support_count"] == expected["generation_complex"]["minimal_generating_support_count"]
    print(json.dumps({**result, "status": "REPLAY_PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
