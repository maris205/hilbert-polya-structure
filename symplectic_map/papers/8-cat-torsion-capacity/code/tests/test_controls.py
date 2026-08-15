from __future__ import annotations

from pathlib import Path

from cat_torsion.controls import (
    corruption_rejection_controls,
    input_scope_controls,
    run_all_controls,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def test_safe_controls_pass_without_registered_candidate():
    report = run_all_controls(PROJECT_ROOT)
    assert report["pass"] is True
    assert report["registered_candidate_accessed"] is False
    assert report["periods_above_twelve_computed"] is False
    assert report["external_data_accessed"] is False


def test_corrupted_period_factorization_and_jordan_inputs_fail():
    assert corruption_rejection_controls()["pass"] is True
    assert input_scope_controls()["pass"] is True
