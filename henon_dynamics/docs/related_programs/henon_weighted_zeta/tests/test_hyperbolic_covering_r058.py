from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "scripts" / "audit_hyperbolic_covering_r058.py"


def run_certificate(output: Path) -> dict[str, object]:
    subprocess.run(
        [sys.executable, str(SCRIPT), "--output", str(output)],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(output.read_text(encoding="utf-8"))


def test_r058_exact_covering_and_cones_pass(tmp_path: Path) -> None:
    payload = run_certificate(tmp_path / "covering.json")
    decisions = payload["decisions"]
    assert decisions["b0_integrity_pass"] is True
    assert decisions["b1_exact_covering_pass"] is True
    assert decisions["b2_local_cone_pass"] is True
    assert decisions["local_exact_certificate_pass"] is True
    assert (
        decisions["bi_infinite_itinerary_realization_theorem_audit_pass"]
        is True
    )
    assert decisions["full_primary_claim_enabled"] is True
    assert decisions["entropy_claim_enabled"] is True


def test_r058_frozen_exact_values(tmp_path: Path) -> None:
    payload = run_certificate(tmp_path / "covering.json")
    assert len(payload["covering_records"]) == 6
    assert len(payload["forbidden_transition_records"]) == 10
    assert all(record["pass"] for record in payload["covering_records"])
    assert all(
        record["pass"] for record in payload["forbidden_transition_records"]
    )
    cone = payload["cone_certificate"]
    assert Fraction(
        cone["forward_unstable_slope_upper_bound"]["fraction"]
    ) == Fraction(25088, 95079)
    assert Fraction(
        cone["backward_stable_slope_upper_bound"]["fraction"]
    ) == Fraction(15129, 45388)
    assert Fraction(
        cone["forward_unstable_slope_upper_bound"]["fraction"]
    ) < Fraction(1, 2)
    assert Fraction(
        cone["backward_stable_slope_upper_bound"]["fraction"]
    ) < Fraction(1, 2)
    assert payload["symbolic_graph"]["characteristic_polynomial_match"] is True
