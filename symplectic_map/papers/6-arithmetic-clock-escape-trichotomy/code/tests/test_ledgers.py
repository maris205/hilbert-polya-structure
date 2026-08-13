from pathlib import Path

from capacity_audit.ledger import (
    REQUIRED_ADMITTED_SCOPE_IDS,
    REQUIRED_EXCLUDED_SCOPE_IDS,
    REQUIRED_PROOF_IDS,
    audit_proof_ledger,
    audit_scope_ledger,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_proof_ledger_has_exact_structured_dependency_ids():
    record = audit_proof_ledger(PROJECT_ROOT)
    assert record["pass"]
    assert set(record["observed_ids"]) == REQUIRED_PROOF_IDS
    assert record["dependency_cycles"] == []
    assert record["phrase_based_proof_acceptance"] is False


def test_scope_ledger_has_exact_allowed_and_excluded_ids():
    record = audit_scope_ledger(PROJECT_ROOT)
    assert record["pass"]
    assert set(record["admitted_ids"]) == REQUIRED_ADMITTED_SCOPE_IDS
    assert set(record["excluded_ids"]) == REQUIRED_EXCLUDED_SCOPE_IDS
    assert record["escape_semantics_safe"]
    assert record["forbidden_output_ids_exact"]
