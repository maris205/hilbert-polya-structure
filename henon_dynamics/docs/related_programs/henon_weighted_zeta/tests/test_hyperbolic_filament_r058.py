from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "scripts" / "audit_hyperbolic_filament_r058.py"
PREFLIGHT = PROJECT_ROOT / "results" / "hyperbolic_filament_preflight_r058.json"


def test_r058_locked_preflight() -> None:
    subprocess.run(
        [sys.executable, str(SCRIPT), "--preflight-only"],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(PREFLIGHT.read_text(encoding="utf-8"))
    assert payload["pass"] is True
    assert len(payload["configurations"]) == 9
    assert len(payload["refinements"]) == 6
    assert all(row["k_match"] for row in payload["configurations"])
    assert all(row["below_cap"] for row in payload["configurations"])
    assert all(row["exact_nested"] for row in payload["refinements"])


def test_r058_shifted_k_schedule() -> None:
    payload = json.loads(PREFLIGHT.read_text(encoding="utf-8"))
    observed = {
        row["configuration"]: row["uncapped_k_max"]
        for row in payload["configurations"]
    }
    assert observed["n113_dp1_12"] == 37
    assert observed["n226_dp1_6"] == 43
    assert observed["n452_dp1_3"] == 62
    assert observed["n113_dm1_12"] == 37
    assert observed["n226_dm1_6"] == 43
    assert observed["n452_dm1_3"] == 62
