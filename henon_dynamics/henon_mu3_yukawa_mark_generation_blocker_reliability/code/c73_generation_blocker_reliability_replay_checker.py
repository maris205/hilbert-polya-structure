#!/usr/bin/env python3
"""Clean-process replay for the C73 independent checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c73_generation_blocker_reliability_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c73_generation_blocker_reliability_checker.py"


def main() -> None:
    expected = json.loads(EVIDENCE.read_text())
    run = subprocess.run([sys.executable, str(CHECKER)], cwd=PROJECT,
                         capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["status"] == "PASS"
    assert result["minimal_edges"] == expected["generation_structure"]["base_graph_edge_count"]
    assert result["minimal_blockers"] == expected["blocker_geometry"]["minimal_blocker_count"]
    assert result["destructive_transversals"] == expected["blocker_geometry"]["destructive_transversal_count"]
    assert result["surviving_deletion_sets"] == expected["deletion_spectrum"]["surviving_total"]
    print(json.dumps({**result, "status": "REPLAY_PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
