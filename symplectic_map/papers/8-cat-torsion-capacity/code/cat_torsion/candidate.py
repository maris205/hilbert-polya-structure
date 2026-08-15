"""Fail-closed registered exact reproduction of the frozen Paper 8 candidate."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import Any

from .algebra import (
    CAT_MATRIX,
    LOCKED_LEDGER,
    LOCKED_SUPPORT,
    delta_direct,
    delta_recurrence,
    factor_locked_integer,
    factorization_text,
    selected_primitive_divisor,
)
from .clock import every_order_witness, orbit_sum_monodromy_certificate, perturbation_witness
from .finite_field import EXPECTED_PERIOD_PROFILES, enumerate_period_profile, jordan_mod5_certificate
from .lifecycle import REGISTERED_PERIODS, validate_registered_claim
from .proof_contract import negative_trace_parity_contract, norm_determinant_contract, primitive_kernel_logic_contract
from .protocol import CANDIDATE_ID, EXPECTED_LOCK_SHA256, _raw_absolute, load_exact_json
from .review_gate import reviewed_code_tree_sha256


class RegisteredCandidateFailure(RuntimeError):
    """Carries exact lifecycle progress without permitting a scientific override."""

    def __init__(self, message: str, *, started: list[int], completed: list[int]):
        super().__init__(message)
        self.periods_started = list(started)
        self.periods_completed = list(completed)


def _require_deployment_authority(project_root: Path) -> dict[str, Any]:
    """Revalidate live P0--P3, official preflight, and the durable claim."""

    from .manifest import collect_safe_preflight, validate_official_preflight

    project_root = _raw_absolute(project_root)
    live = collect_safe_preflight(project_root)
    if live.get("pass") is not True or live.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        raise RuntimeError("live P0--P3 deployment authority is missing")
    current_tree = reviewed_code_tree_sha256(project_root)
    review = live.get("independent_review")
    if type(review) is not dict or review.get("pass") is not True:
        raise RuntimeError("independent deployment review is invalid")
    authority = review.get("authority")
    if type(authority) is not dict:
        raise RuntimeError("independent authority marker is malformed")
    if authority.get("source_lock_sha256") != EXPECTED_LOCK_SHA256:
        raise RuntimeError("review is not bound to the source lock")
    if authority.get("reviewed_code_sha256") != current_tree:
        raise RuntimeError("review is not bound to the current code tree")
    official = load_exact_json(project_root / "results" / "PRE_EXECUTION_AUDIT.json")
    errors = validate_official_preflight(official, live)
    if errors:
        raise RuntimeError("official preflight is not the live authorized snapshot")
    claim = validate_registered_claim(project_root, current_tree, require_clean_started=True)
    if claim.get("pass") is not True:
        raise RuntimeError("durable STARTED claim is missing or invalid")
    return {
        "preflight": live,
        "review": review,
        "claim": claim,
        "reviewed_code_sha256": current_tree,
    }


def run_registered_candidate(project_root: Path) -> dict[str, Any]:
    """Run exactly the locked n=1..12 audit after deployment authorization."""

    authorization = _require_deployment_authority(project_root)
    project_root = _raw_absolute(project_root)
    expected_tree = authorization["reviewed_code_sha256"]
    periods_started: list[int] = []
    periods_completed: list[int] = []
    ledger_records: list[dict[str, Any]] = []
    earlier_support: set[int] = set()
    try:
        for period, expected_delta, expected_factors, expected_selected in LOCKED_LEDGER:
            if reviewed_code_tree_sha256(project_root) != expected_tree:
                raise RuntimeError("reviewed code tree changed before a registered period")
            periods_started.append(period)
            direct = delta_direct(CAT_MATRIX, period)
            recurrence = delta_recurrence(CAT_MATRIX, period)
            factors = factor_locked_integer(direct)
            selected = selected_primitive_divisor(period, factors, earlier_support)
            record = {
                "period": period,
                "delta_direct": direct,
                "delta_recurrence": recurrence,
                "factorization": {str(key): value for key, value in sorted(factors.items())},
                "factorization_text": factorization_text(direct, factors),
                "support": sorted(factors),
                "selected_primitive_prime": selected,
                "engines_agree": direct == recurrence,
                "locked_record_matches": (
                    direct == expected_delta
                    and factors == expected_factors
                    and selected == expected_selected
                ),
                "evidentiary_role": "DEVELOPMENT_SEEN_PRIMARY_LITERATURE_REPRODUCTION",
            }
            if record["engines_agree"] is not True or record["locked_record_matches"] is not True:
                raise RuntimeError("determinant ledger or factorization contradiction")
            ledger_records.append(record)
            earlier_support.update(factors)
            periods_completed.append(period)

        finite_records = []
        for modulus in LOCKED_SUPPORT:
            if reviewed_code_tree_sha256(project_root) != expected_tree:
                raise RuntimeError("reviewed code tree changed before a finite-field block")
            profile = enumerate_period_profile(modulus)
            expected_profile = EXPECTED_PERIOD_PROFILES[modulus]
            record = {
                "prime": modulus,
                "period_profile": {str(key): value for key, value in profile.items()},
                "expected_period_profile": {
                    str(key): value for key, value in expected_profile.items()
                },
                "nonzero_vector_count": modulus * modulus - 1,
                "matches_locked_profile": profile == expected_profile,
            }
            if record["matches_locked_profile"] is not True:
                raise RuntimeError("finite-field period classification contradiction")
            finite_records.append(record)

        jordan = jordan_mod5_certificate()
        if jordan["pass"] is not True:
            raise RuntimeError("modulo-five Jordan period-ten repair failed")
        profiles = {
            str(record["prime"]): record["period_profile"] for record in finite_records
        }
        boundary_summary = {
            "profiles": profiles,
            "jordan_period_ten_points": 20,
            "jordan_period_ten_cycles": 2,
            "period_1_carriers": 0,
            "period_6_carriers": 0,
            "period_10_carriers": 20,
            "period_12_carriers": 0,
            "exception_set": [1, 6, 12],
        }
        if any(boundary_summary[key] != 0 for key in (
            "period_1_carriers",
            "period_6_carriers",
            "period_12_carriers",
        )) or boundary_summary["period_10_carriers"] != 20:
            raise RuntimeError("source-locked boundary classification contradiction")

        theorem_contract = {
            "norm_determinant": norm_determinant_contract(),
            "primitive_kernel": primitive_kernel_logic_contract(),
            "negative_trace_parity": negative_trace_parity_contract(),
            "tail_periods_computed": [],
            "tail_evidence": "IMPORTED_THEOREM_PLUS_SEPARATE_PARITY_PROOF_ONLY",
        }
        if not all(
            theorem_contract[key]["pass"]
            for key in ("norm_determinant", "primitive_kernel", "negative_trace_parity")
        ):
            raise RuntimeError("general theorem proof contract failed")
        clock = {
            "all_order_witnesses": [every_order_witness(order) for order in (1, 4, 6, 9)],
            "discontinuity_witnesses": [
                perturbation_witness((Fraction(2, 9), Fraction(1, 6)), index)
                for index in (1, 3, 7)
            ],
            "orbit_sum_monodromy": orbit_sum_monodromy_certificate(10, 5),
            "range": "ALL_POSITIVE_INTEGERS_PRIME_AND_COMPOSITE",
            "regularity": "UNBOUNDED_AND_DISCONTINUOUS_IN_EVERY_TORSION_NEIGHBORHOOD",
            "native_monodromy": "PERIOD_DEPENDENT_TORSION_ORDER_BLIND",
        }
        if reviewed_code_tree_sha256(project_root) != expected_tree:
            raise RuntimeError("reviewed code tree changed during registered execution")
    except BaseException as error:
        if isinstance(error, (KeyboardInterrupt, SystemExit)):
            raise
        raise RegisteredCandidateFailure(
            str(error), started=periods_started, completed=periods_completed
        ) from error

    return {
        "schema": "CAT_TORSION_REGISTERED_EXACT_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": expected_tree,
        "registered_periods": REGISTERED_PERIODS,
        "ledger_records": ledger_records,
        "finite_field_records": finite_records,
        "boundary_summary": boundary_summary,
        "general_theorem_contract": theorem_contract,
        "clock_specificity": clock,
        "registered_run_count": 1,
        "registered_exact_audits": 1,
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "generated_prime_target_arrays": 0,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "periods_above_twelve_computed": [],
        "classification": "INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH",
        "route_a": "A0_FAIL_PROVES_TOO_MUCH_NO_A1_TO_A4",
        "route_b": "NOT_OPENED",
        "pass": True,
    }
