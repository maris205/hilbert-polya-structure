#!/usr/bin/env python3
"""Clean-process replay for the C71 complement-geometry checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c71_complement_geometry_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c71_complement_geometry_checker.py"


def main() -> None:
    expected = json.loads(EVIDENCE.read_text())
    run = subprocess.run(
        [sys.executable, str(CHECKER)], cwd=PROJECT, capture_output=True, text=True
    )
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["status"] == "PASS"
    assert result["complement_count"] == expected["spectrum_total"]
    assert result["subgroup_poset_size"] == expected["target_subgroup_poset"]["subgroup_count"]
    assert result["generating_triple_count"] == expected["named_core_geometry"]["generating_triple_count"]
    assert result["full_image_count"] == expected["complement_span"]["surjective_difference_count"]
    assert result["universal_core"] == "Z/3 + Z/18"
    print(json.dumps({**result, "status": "REPLAY_PASS"}, sort_keys=True))


if __name__ == "__main__":
    main()
