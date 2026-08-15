from pathlib import Path

from base2_clock.controls import (
    chebyshev_control,
    formal_period_pollution_control,
    power_map_control,
    run_all_controls,
    upstream_regression_control,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def test_all_dynamic_controls_pass_shared_engine():
    assert power_map_control()["pass"] is True
    assert chebyshev_control()["pass"] is True
    assert formal_period_pollution_control()["pass"] is True


def test_upstream_regression_checks_semantics_not_only_hash():
    record = upstream_regression_control(PROJECT_ROOT)
    assert record["pass"] is True
    assert record["checks"]["formal_degrees_2_2_6_12"] is True
    assert record["checks"]["frozen_cycle_polynomials_equal"] is True
    assert record["checks"]["f_u_g_multiplier_invariants_equal"] is True


def test_controls_bundle_never_accesses_registered_candidate():
    record = run_all_controls(PROJECT_ROOT)
    assert record["pass"] is True
    assert record["registered_candidate_accessed"] is False
