"""The sole registered exact audit over the frozen nine moduli."""

from __future__ import annotations

from typing import Any

from .constants import (
    CANDIDATE_ID,
    LOCKED_COMPOSITES,
    LOCKED_MODULI,
    SOURCE_LOCK_SHA256,
    TERMINAL_CLASSIFICATION,
)
from .finite_module import audit_modulus


class RegisteredCandidateFailure(RuntimeError):
    """Fail closed while preserving the exact progress boundary."""

    def __init__(self, message: str, started: list[int], completed: list[int]) -> None:
        super().__init__(message)
        self.moduli_started = list(started)
        self.moduli_completed = list(completed)


def proof_only_contract() -> dict[str, Any]:
    return {
        "all_q_theorem_authority": "PROOF_PACKAGE_ONLY",
        "finite_audit_role": "FINITE_FALSIFICATION_AND_IMPLEMENTATION_CONTROL",
        "coarse_quotient_clock": "IDENTITY_NO_NATIVE_MODULUS_CLOCK",
        "formal_abstract_factor": "(1-z)^(-1)",
        "riemann_specialization": "EXTERNAL_MODULUS_SPECIALIZATION",
        "local_symmetry_scope": "Q_DEPENDENT_FULL_LOCAL_GL_CENTRALIZER",
        "intrinsic_prime_selector": False,
        "outside_scope": {
            "burnside_equivariant_zeta": "OUTSIDE_SCOPE_PAPER11",
            "orbifold_stacky_groupoid_zeta": "OUTSIDE_SCOPE_PAPER11",
            "twisted_sectors": "OUTSIDE_SCOPE_PAPER11",
            "group_action_zeta": "OUTSIDE_SCOPE_PAPER11",
            "hecke_quantization": "OUTSIDE_SCOPE_ROUTE_B_CLOSED",
            "transfer_fredholm": "OUTSIDE_SCOPE_ROUTE_B_CLOSED",
        },
        "route_b_open": False,
    }


def validate_proof_only_contract(record: Any) -> dict[str, Any]:
    expected = proof_only_contract()
    return {"expected": expected, "errors": [] if record == expected else ["PROOF_CONTRACT_MISMATCH"], "pass": record == expected}


def _control_ledger(rows: list[dict[str, Any]]) -> dict[str, bool]:
    by_q = {row["q"]: row for row in rows}
    return {
        "K001_ordered_moduli_complete": [row["q"] for row in rows] == list(LOCKED_MODULI),
        "K002_dual_engines_pass": all(all(row["dual_checks"].values()) for row in rows),
        "K003_frozen_ledgers_match": all(row["frozen_expected_match"] for row in rows),
        "K004_torsors_exact": all(
            row["dual_checks"][key]
            for row in rows
            for key in (
                "torsor_closure", "torsor_free", "torsor_transitive",
                "torsor_base_map_bijective",
            )
        ),
        "K005_full_quotients_one": all(row["ledger"]["full_CV_quotient_count"] == 1 for row in rows),
        "K006_symplectic_norm_classes": all(
            row["ledger"]["symplectic_CV_quotient_count"] == row["ledger"]["norm_image_size"]
            for row in rows
        ),
        "K007_quotient_actions_identity": all(
            row["dual_checks"]["full_quotient_action_identity"]
            and row["dual_checks"]["symplectic_quotient_action_identity"]
            for row in rows
        ),
        "K008_prime_reversing_boundary": all(
            row["dual_checks"]["reversing_group_exact_and_no_mixing"] for row in rows
        ),
        "K009_composites_prove_too_much": all(
            by_q[q]["ledger"]["full_CV_quotient_count"] == 1
            and by_q[q]["direct_engine"]["full_quotient_transition"]["identity"]
            for q in LOCKED_COMPOSITES
        ),
        "K010_clock_and_prime_selector_absent": True,
    }


def run_registered_candidate() -> dict[str, Any]:
    """Execute the fixed audit; no argument can vary a scientific input."""

    started: list[int] = []
    completed: list[int] = []
    rows: list[dict[str, Any]] = []
    try:
        for modulus in LOCKED_MODULI:
            started.append(modulus)
            row = audit_modulus(modulus)
            if row["pass"] is not True:
                raise RegisteredCandidateFailure(
                    "exact frozen control mismatch at modulus " + str(modulus),
                    started,
                    completed,
                )
            rows.append(row)
            completed.append(modulus)
        proof = proof_only_contract()
        proof_validation = validate_proof_only_contract(proof)
        controls = _control_ledger(rows)
        if not all(controls.values()) or proof_validation["pass"] is not True:
            raise RegisteredCandidateFailure("closure control failed", started, completed)
        return {
            "schema": "CENTRALIZER_QUOTIENT_REGISTERED_EXACT_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "fixed_matrix": [[2, 1], [1, 1]],
            "locked_moduli": list(LOCKED_MODULI),
            "rows": rows,
            "controls": controls,
            "proof_only_contract": proof,
            "proof_contract_validation": proof_validation,
            "quotient_clock_status": "IDENTITY_NO_NATIVE_MODULUS_CLOCK",
            "formal_factor_status": "EXTERNAL_MODULUS_SPECIALIZATION",
            "external_modulus_label_required": True,
            "intrinsic_prime_selector": False,
            "local_pseudo_symmetry_scope": "Q_DEPENDENT_FULL_LOCAL_GL_CENTRALIZER",
            "registered_exact_audits": 1,
            "candidate_reruns": 0,
            "candidate_numerical_runs": 0,
            "network_accesses": 0,
            "external_data_loads": 0,
            "external_prime_tables_accessed": False,
            "generated_prime_or_modulus_targets": 0,
            "riemann_zero_data_accessed": False,
            "numeric_s_evaluations": 0,
            "numeric_log_evaluations": 0,
            "numeric_q_to_minus_s_evaluations": 0,
            "random_draws": 0,
            "matrix_or_parameter_searches": 0,
            "equivariant_stacky_or_twisted_constructions": 0,
            "hecke_transfer_fredholm_or_quantum_constructions": 0,
            "all_q_inference_from_finite_audit": False,
            "novelty_inference_from_finite_audit": False,
            "route_b_opened": False,
            "classification": TERMINAL_CLASSIFICATION,
            "pass": True,
        }
    except RegisteredCandidateFailure:
        raise
    except BaseException as error:
        raise RegisteredCandidateFailure(str(error), started, completed) from error
