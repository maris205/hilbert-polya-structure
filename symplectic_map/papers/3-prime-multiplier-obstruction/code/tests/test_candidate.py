import json

import pytest

from prime_multiplier.algebra import candidate_field
from prime_multiplier.candidate import (
    audit_candidate,
    audit_conjugacy,
    parameter_and_conjugacy_preflight,
)


@pytest.fixture(scope="module")
def candidate_bundle():
    field = candidate_field()
    audit, certificates = audit_candidate(field=field)
    return field, audit, certificates


def test_parameter_and_conjugacy_preflight_passes():
    record = parameter_and_conjugacy_preflight(candidate_field())
    assert record["status"] == "PASS"
    assert record["candidate_multiplier_polynomials_computed"] is False
    assert all(record["checks"].values())
    assert json.loads(json.dumps(record))["status"] == "PASS"


def test_candidate_exact_audit_passes(candidate_bundle):
    _, record, _ = candidate_bundle
    assert record["status"] == "PASS"
    assert [item["formal_degree"] for item in record["periods"]] == [2, 2, 6, 12]
    assert [item["exact_cycle_count"] for item in record["periods"]] == [2, 1, 2, 3]
    assert [item["rational_candidates"] for item in record["periods"]] == [[], [], [], []]


def test_candidate_exact_cycle_multiplier_polynomials(candidate_bundle):
    _, record, _ = candidate_bundle
    expressions = [item["cycle_multiplier_polynomial"]["expression"] for item in record["periods"]]
    assert expressions == [
        "L**2 - 2*L - 4*u",
        "L - 4 + 4*u",
        "L**2 + L*(-16 + 8*u) - 64 + 64*u",
        "L**3 + L**2*(-48 + 16*u**2) + L*(256 + 256*u**2) + 4096",
    ]


def test_p2_exponent_boundary_remains_open(candidate_bundle):
    _, record, _ = candidate_bundle
    assert record["p2_exponent_prime_period_ge_2"] == "OPEN"
    assert record["raw_rational_prime_all_periods"] == "ABSENT_BY_THEOREM"


def test_conjugate_coordinate_pipeline_agrees(candidate_bundle):
    field, _, certificates = candidate_bundle
    record = audit_conjugacy(certificates, field=field)
    assert record["status"] == "PASS"
    assert all(all(item["checks"].values()) for item in record["periods"])


def test_candidate_cutoff_cannot_be_changed():
    with pytest.raises(ValueError, match="source-locked"):
        audit_candidate(max_period=5)
