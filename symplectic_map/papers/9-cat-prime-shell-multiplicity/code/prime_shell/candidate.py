"""The sole registered exact audit over the five inherited shell controls."""

from __future__ import annotations

from typing import Any

from .constants import (
    CANDIDATE_ID,
    EXPECTED_LEDGER,
    EXPECTED_RAW_FACTORS,
    LOCKED_PRIMES,
    SOURCE_LOCK_SHA256,
    TERMINAL_LABELS,
)
from .finite_field import (
    analytic_case_certificate,
    comparison_projection,
    direct_enumeration_certificate,
    expected_projection,
)
from .mechanisms import mechanism_audit, symbolic_composite_control
from .proof_contract import proof_only_contract, validate_proof_only_contract
from .protocol import canonical_json_bytes
from .symbolic import symbolic_product_audit


class RegisteredCandidateFailure(RuntimeError):
    """Fail closed with an exact record of the fixed-prime progress boundary."""

    def __init__(self, message: str, started: list[int], completed: list[int]) -> None:
        super().__init__(message)
        self.primes_started = list(started)
        self.primes_completed = list(completed)


def raw_factor_text(prime: int, cycle_profile: dict[int, int]) -> str:
    factors = []
    for length, count in sorted(cycle_profile.items()):
        factors.append(f"(1-{prime}^(-{length}s))^(-{count})")
    return "*".join(factors)


def _control_ledger(rows: list[dict[str, Any]], proof: dict[str, Any]) -> dict[str, bool]:
    by_prime = {row["prime"]: row for row in rows}
    return {
        "K001_shell_partition": all(row["direct_engine"]["partition_exact"] for row in rows),
        "K002_binary_exception": by_prime[2]["m_p"] == 1
        and by_prime[2]["cycle_profile"] == {3: 1},
        "K003_ramified_mixture": by_prime[5]["cycle_profile"] == {2: 2, 10: 2},
        "K004_odd_bound": all(by_prime[p]["m_p"] >= p - 1 for p in LOCKED_PRIMES if p != 2),
        "K005_split_strata": by_prime[11]["eigenline_cycles"] == 4
        and by_prime[11]["off_eigenline_cycles"] == 20,
        "K006_product_separation": all(row["product_audit"]["semantics_separated"] for row in rows)
        and len(by_prime[5]["product_audit"]["raw_return"]["factors"]) == 2
        and by_prime[5]["product_audit"]["orbit_label"]["denominator_degree"] == 4,
        "K007_repetition": all(
            len(row["product_audit"]["formal_repeats"]) == 3 for row in rows
        ),
        "K008_equal_weight_failure": all(
            row["mechanism_audit"]["equal_weight_control"][
                "repairs_only_first_repeat_when_m_gt_one"
            ]
            for row in rows
        ),
        "K009_fractional_identity": all(
            row["mechanism_audit"]["fractional_shell_normalization"]["equals_one"]
            for row in rows
        ),
        "K010_selector_cost": all(
            row["mechanism_audit"]["one_orbit_selector"]["discarded_cycle_count"]
            == row["m_p"] - 1
            for row in rows
        ),
        "K011_analytic_boundary": proof["gap_2_lt_re_s_le_3"] == "NO_CLAIM"
        and proof["zero_statement_claimed"] is False,
        "K012_escape_boundary": proof["centralizer_computations_run"] == 0
        and all(value == "OUTSIDE_SCOPE" for value in proof["outside_scope_escapes"].values()),
    }


def run_registered_candidate() -> dict[str, Any]:
    """Run exactly one deterministic audit; no parameter accepts scientific inputs."""

    started: list[int] = []
    completed: list[int] = []
    rows: list[dict[str, Any]] = []
    try:
        for prime in LOCKED_PRIMES:
            started.append(prime)
            analytic = analytic_case_certificate(prime)
            direct = direct_enumeration_certificate(prime)
            analytic_projection = comparison_projection(analytic)
            direct_projection = comparison_projection(direct)
            expected = expected_projection(prime)
            dual_match = canonical_json_bytes(analytic_projection) == canonical_json_bytes(
                direct_projection
            )
            expected_match = canonical_json_bytes(direct_projection) == canonical_json_bytes(expected)
            expected_case_match = analytic["case"] == EXPECTED_LEDGER[prime]["case"]
            raw_factor = raw_factor_text(prime, direct["cycle_profile"])
            raw_factor_match = raw_factor == EXPECTED_RAW_FACTORS[prime]
            case_checks_pass = all(analytic["case_checks"].values())
            if not (
                dual_match
                and expected_match
                and expected_case_match
                and raw_factor_match
                and case_checks_pass
                and direct["partition_exact"]
            ):
                raise RegisteredCandidateFailure(
                    f"exact theorem/control mismatch at frozen prime {prime}",
                    started,
                    completed,
                )
            product = symbolic_product_audit(direct)
            mechanisms = mechanism_audit(direct)
            rows.append(
                {
                    "prime": prime,
                    "case": analytic["case"],
                    "shell_cardinality": direct["shell_cardinality"],
                    "point_period_profile": direct["point_period_profile"],
                    "cycle_profile": direct["cycle_profile"],
                    "m_p": direct["m_p"],
                    "eigenline_cycles": direct["eigenline_cycles"],
                    "off_eigenline_cycles": direct["off_eigenline_cycles"],
                    "analytic_engine": analytic,
                    "direct_engine": direct,
                    "dual_engine_match": dual_match,
                    "frozen_expected_match": expected_match and expected_case_match,
                    "raw_factor": raw_factor,
                    "raw_factor_frozen_match": raw_factor_match,
                    "product_audit": product,
                    "mechanism_audit": mechanisms,
                    "evidence_role": "FINITE_FALSIFICATION_CONTROL",
                    "pass": True,
                }
            )
            completed.append(prime)
        proof = proof_only_contract()
        proof_validation = validate_proof_only_contract(proof)
        composite = symbolic_composite_control()
        controls = _control_ledger(rows, proof)
        passed = (
            completed == list(LOCKED_PRIMES)
            and all(row["pass"] for row in rows)
            and all(controls.values())
            and proof_validation["pass"] is True
            and composite["composite_shells_enumerated"] == 0
        )
        if not passed:
            raise RegisteredCandidateFailure(
                "fixed audit failed a closure control", started, completed
            )
        return {
            "schema": "PRIME_SHELL_REGISTERED_EXACT_AUDIT_V1",
            "candidate_id": CANDIDATE_ID,
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "fixed_matrix": [[2, 1], [1, 1]],
            "locked_primes": list(LOCKED_PRIMES),
            "development_seen_controls": True,
            "rows": rows,
            "controls": controls,
            "symbolic_composite_control": composite,
            "proof_only_contract": proof,
            "proof_contract_validation": proof_validation,
            "terminal_labels": list(TERMINAL_LABELS),
            "registered_exact_audits": 1,
            "candidate_numerical_runs": 0,
            "external_prime_tables_accessed": False,
            "generated_prime_target_arrays": 0,
            "riemann_zero_data_accessed": False,
            "numeric_s_or_log_evaluations": 0,
            "composite_shells_enumerated": 0,
            "centralizer_computations_run": 0,
            "parameter_or_matrix_searches": 0,
            "normalization_or_selector_searches": 0,
            "all_prime_inference_from_finite_audit": False,
            "global_convergence_inference_from_finite_audit": False,
            "classification": (
                "PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED / "
                "A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED"
            ),
            "pass": True,
        }
    except RegisteredCandidateFailure:
        raise
    except BaseException as error:
        raise RegisteredCandidateFailure(str(error), started, completed) from error
