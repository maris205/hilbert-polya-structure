from action_audit.controls import (
    identity_transcendental_constant_control,
    run_controls,
    target_injection_control,
)


def test_controls_first_suite_passes():
    record = run_controls()
    assert record["pass"]
    assert record["controls_executed_before_henon_static_audit"]


def test_identity_log_target_control_is_symbolic_only():
    record = identity_transcendental_constant_control()
    assert record["pass"]
    assert not record["numeric_logarithm_evaluated"]
    assert not record["external_target_table_accessed"]


def test_target_injection_control_is_forbidden_label():
    record = target_injection_control()
    assert record["classification"].startswith("FORBIDDEN_")
    assert not record["numeric_target_evaluated"]


def test_endpoint_mismatch_control_retains_seven():
    record = run_controls()["algebraic_endpoint_mismatch"]
    assert record["endpoint_mismatch"] == "7"
    assert record["pass"]


def test_log_abs_control_is_nonclaim():
    record = run_controls()["log_abs_nonclaim"]
    assert record["classification"] == "OUTSIDE_SOURCE_LOCK_NONCLAIM"


def test_multivalued_gauge_control_stops_absolute_action():
    record = run_controls()["multivalued_gauge_nonclaim"]
    assert not record["single_valued_qbar_rational"]
    assert "STOP" in record["classification"]


def test_candidate_counters_remain_zero_in_controls():
    record = run_controls()
    assert not record["candidate_parameter_substituted"]
    assert not record["candidate_periodic_point_computed"]
    assert not record["candidate_action_computed"]
