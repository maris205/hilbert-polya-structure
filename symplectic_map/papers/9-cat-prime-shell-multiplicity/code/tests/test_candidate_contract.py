from __future__ import annotations

from prime_shell.candidate import run_registered_candidate
from prime_shell.constants import LOCKED_PRIMES, TERMINAL_LABELS


def test_registered_core_has_exact_closed_evidence_contract() -> None:
    result = run_registered_candidate()
    assert result["pass"] is True
    assert result["locked_primes"] == list(LOCKED_PRIMES)
    assert result["terminal_labels"] == list(TERMINAL_LABELS)
    assert all(result["controls"].values())
    assert result["candidate_numerical_runs"] == 0
    assert result["numeric_s_or_log_evaluations"] == 0
    assert result["composite_shells_enumerated"] == 0
    assert result["centralizer_computations_run"] == 0
    assert result["all_prime_inference_from_finite_audit"] is False
    assert result["global_convergence_inference_from_finite_audit"] is False
