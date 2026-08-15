"""Schema-only guards for proof provenance, global bounds, and live escapes."""

from __future__ import annotations

from typing import Any

from .constants import OUTSIDE_SCOPE_ESCAPES, REQUIRED_ANALYTIC_CONTRACTS


def proof_only_contract() -> dict[str, Any]:
    return {
        "evidence_role": "PROOF_CONTRACT_NOT_FINITE_EXPERIMENT_EVIDENCE",
        "all_prime_theorem_source": "notes/PROOF_PACKAGE.md",
        "analytic_contracts": list(REQUIRED_ANALYTIC_CONTRACTS),
        "gap_2_lt_re_s_le_3": "NO_CLAIM",
        "exact_abscissa_claimed": False,
        "conditional_convergence_claimed": False,
        "analytic_continuation_claimed": False,
        "zero_statement_claimed": False,
        "outside_scope_escapes": {name: "OUTSIDE_SCOPE" for name in OUTSIDE_SCOPE_ESCAPES},
        "centralizer_computations_run": 0,
        "matrix_weight_computations_run": 0,
        "transfer_or_fredholm_computations_run": 0,
        "quantum_computations_run": 0,
        "prime_or_zero_correspondence_claimed": False,
        "route_b_status": "ROUTE_B_NOT_OPENED",
    }


def validate_proof_only_contract(record: Any) -> dict[str, Any]:
    expected = proof_only_contract()
    errors: list[str] = []
    if type(record) is not dict:
        errors.append("PROOF_CONTRACT_NOT_OBJECT")
    elif record != expected:
        errors.append("PROOF_CONTRACT_NOT_EXACT")
    return {"stage": "B5_PROOF_ONLY_SCOPE", "errors": errors, "pass": not errors}
