#!/usr/bin/env python3
"""Clean-process replay for the C70 orbit checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c70_direct_factor_orbit_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c70_direct_factor_orbit_checker.py"


def main() -> None:
    expected = json.loads(EVIDENCE.read_text())
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["status"] == "PASS"
    assert result["direct_factor_count"] == expected["direct_factor_count"]
    assert result["ordered_decomposition_count"] == expected["ordered_decomposition_count"]
    assert result["split_embedding_count"] == expected["split_embedding_count"]
    assert result["all_D_subgroup_count"] == expected["all_D_subgroup_count"]
    assert result["nondirect_D_subgroup_count"] == expected["nondirect_D_subgroup_count"]
    assert result["counterexample"] == "VERIFIED"
    print(json.dumps({**result, "status": "REPLAY_PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
