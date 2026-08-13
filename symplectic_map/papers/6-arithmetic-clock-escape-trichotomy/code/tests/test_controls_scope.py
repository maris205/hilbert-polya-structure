from capacity_audit.controls import (
    henon_bad_support_control,
    identity_action_injection_control,
    run_all_controls,
    set_selection_control,
    unit_edge_case_control,
)
from capacity_audit.scope import audit_escape_semantics, audit_output_scope


def test_exact_henon_boundary_control():
    record = henon_bad_support_control()
    assert record["pass"]
    assert record["fixed_point_identity"]
    assert record["spectral_identity"]
    assert record["denominator_supported_at_frozen_two"]
    assert record["boundary_control_not_candidate_search"]


def test_positive_dimensional_action_injection_is_symbolic_and_forbidden():
    record = identity_action_injection_control()
    assert record["pass"]
    assert record["phase_space"] == "AFFINE_PLANE_A2"
    assert record["potential_is_qbar_rational"] is False
    assert record["numeric_logarithm_evaluated"] is False
    assert record["target_injection"]


def test_set_and_unit_edge_controls():
    assert set_selection_control()["pass"]
    unit = unit_edge_case_control()
    assert unit["pass"]
    assert unit["canonical_audit"]["multiplier_closure"]["negative_powers_present"]
    assert unit["canonical_audit"]["multiplier_closure"]["rational_roots_required"]


def test_all_controls_have_no_target_data_or_numeric_matches():
    record = run_all_controls()
    assert record["pass"]
    assert record["external_prime_tables_accessed"] is False
    assert record["prime_target_arrays_generated"] is False
    assert record["riemann_zero_data_accessed"] is False
    assert record["candidate_matches_computed"] == 0


def test_only_scoped_escape_semantics_passes():
    safe = audit_escape_semantics(
        necessary=True,
        mutually_exclusive=False,
        exhaustive_for_all_dynamics=False,
        sufficient=False,
    )
    assert safe["pass"]
    assert not audit_escape_semantics(
        necessary=True,
        mutually_exclusive=True,
        exhaustive_for_all_dynamics=False,
        sufficient=False,
    )["pass"]
    assert not audit_escape_semantics(
        necessary=True,
        mutually_exclusive=False,
        exhaustive_for_all_dynamics=True,
        sufficient=False,
    )["pass"]


def test_forbidden_broad_output_claim_fails():
    assert audit_output_scope("CAPACITY_BOUND_CERTIFIED")["pass"]
    record = audit_output_scope(
        "CAPACITY_BOUND_CERTIFIED",
        ["UNIVERSAL_SYMPLECTIC_NO_GO"],
    )
    assert not record["pass"]
    assert record["forbidden_asserted"] == ["UNIVERSAL_SYMPLECTIC_NO_GO"]
