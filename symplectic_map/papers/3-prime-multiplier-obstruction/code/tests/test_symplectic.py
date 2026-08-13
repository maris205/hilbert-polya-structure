import pytest

from prime_multiplier.symplectic import audit_symplectic_bridge


def test_branchwise_exact_symplectic_identities_pass():
    record = audit_symplectic_bridge()
    assert record["status"] == "PASS"
    assert record["canonical_one_form_residual"] == "0"
    assert record["jacobian_determinant_residual"] == "0"
    assert all(item["reciprocal_pair_identity"] == "PASS" for item in record["return_products"])


def test_global_negative_checks_are_explicit():
    record = audit_symplectic_bridge()
    assert record["checks"]["critical_line_q_zero_rejected"]
    assert record["critical_denominator_at_q_zero"] == "0"
    assert record["checks"]["two_branch_images_overlap"]
    assert record["checks"]["global_inverse_rejected"]
    assert record["checks"]["regular_domain_unbounded"]
    assert "not a global symplectomorphism" in record["mandatory_limitations"]


def test_bridge_cutoff_is_frozen():
    with pytest.raises(ValueError):
        audit_symplectic_bridge(max_period=5)
