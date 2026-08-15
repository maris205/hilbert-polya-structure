"""Safe pre-execution controls, including mandatory corrupted-input rejection."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import Any

from .algebra import (
    CAT_MATRIX,
    LOCKED_LEDGER,
    delta_direct,
    delta_recurrence,
    factor_locked_integer,
    validate_hyperbolic_sl2,
)
from .clock import (
    every_order_witness,
    orbit_sum_monodromy_certificate,
    order_invariance_certificate,
    perturbation_witness,
)
from .finite_field import EXPECTED_PERIOD_PROFILES, boundary_profiles, jordan_mod5_certificate
from .proof_contract import negative_trace_index
from .protocol import _raw_absolute


def validate_locked_ledger_rows(rows: Any) -> dict[str, Any]:
    errors: list[str] = []
    if type(rows) is not list or len(rows) != 12:
        return {"errors": ["LEDGER_ROW_COUNT_NOT_TWELVE"], "pass": False}
    expected_keys = {
        "period",
        "delta_direct",
        "delta_recurrence",
        "factorization",
        "support",
        "selected_primitive_prime",
    }
    earlier_support: set[int] = set()
    for expected, row in zip(LOCKED_LEDGER, rows, strict=True):
        period, delta, factors, selected = expected
        prefix = f"N{period}:"
        if type(row) is not dict or set(row) != expected_keys:
            errors.append(prefix + "ROW_KEYS_NOT_EXACT")
            continue
        expected_factor_json = {str(key): value for key, value in sorted(factors.items())}
        if type(row["period"]) is not int or row["period"] != period:
            errors.append(prefix + "PERIOD_MISMATCH")
        if type(row["delta_direct"]) is not int or row["delta_direct"] != delta:
            errors.append(prefix + "DIRECT_DELTA_MISMATCH")
        if type(row["delta_recurrence"]) is not int or row["delta_recurrence"] != delta:
            errors.append(prefix + "RECURRENCE_DELTA_MISMATCH")
        if row["factorization"] != expected_factor_json:
            errors.append(prefix + "FACTORIZATION_MISMATCH")
        if row["support"] != sorted(factors):
            errors.append(prefix + "SUPPORT_MISMATCH")
        if row["selected_primitive_prime"] != selected:
            errors.append(prefix + "SELECTED_PRIMITIVE_MISMATCH")
        new_support = sorted(set(factors).difference(earlier_support))
        if (new_support[0] if len(new_support) == 1 else None) != selected:
            errors.append(prefix + "FIRST_APPEARANCE_MISMATCH")
        earlier_support.update(factors)
    return {"errors": errors, "pass": not errors}


def validate_boundary_summary(summary: Any) -> dict[str, Any]:
    errors: list[str] = []
    if type(summary) is not dict or set(summary) != {
        "profiles",
        "jordan_period_ten_points",
        "jordan_period_ten_cycles",
        "period_6_carriers",
        "period_12_carriers",
    }:
        return {"errors": ["BOUNDARY_KEYS_NOT_EXACT"], "pass": False}
    expected_profiles = {
        str(prime): {str(period): count for period, count in profile.items()}
        for prime, profile in EXPECTED_PERIOD_PROFILES.items()
    }
    if summary["profiles"] != expected_profiles:
        errors.append("BOUNDARY_PROFILES_MISMATCH")
    exact_scalars = {
        "jordan_period_ten_points": 20,
        "jordan_period_ten_cycles": 2,
        "period_6_carriers": 0,
        "period_12_carriers": 0,
    }
    for key, expected in exact_scalars.items():
        if type(summary[key]) is not int or summary[key] != expected:
            errors.append(key.upper() + "_MISMATCH")
    return {"errors": errors, "pass": not errors}


def input_scope_controls() -> dict[str, Any]:
    identity = validate_hyperbolic_sl2(((1, 0), (0, 1)))
    parabolic = validate_hyperbolic_sl2(((1, 1), (0, 1)))
    positive = validate_hyperbolic_sl2(CAT_MATRIX)
    negative = validate_hyperbolic_sl2(((-2, -1), (-1, -1)))
    checks = {
        "identity_rejected": identity["accepted"] is False,
        "nonhyperbolic_rejected": parabolic["accepted"] is False,
        "positive_trace_hyperbolic_accepted": positive["accepted"] is True,
        "negative_trace_hyperbolic_accepted": negative["accepted"] is True,
        "determinant_minus_one_rejected": validate_hyperbolic_sl2(((2, 1), (1, 0)))[
            "accepted"
        ]
        is False,
    }
    return {
        "run_id": "R020-control-scope",
        "records": [identity, parabolic, positive, negative],
        "checks": checks,
        "pass": all(checks.values()),
    }


def exact_small_controls() -> dict[str, Any]:
    determinant_checks = {
        "n1_dual_engine": delta_direct(CAT_MATRIX, 1) == delta_recurrence(CAT_MATRIX, 1) == -1,
        "n2_dual_engine": delta_direct(CAT_MATRIX, 2) == delta_recurrence(CAT_MATRIX, 2) == -5,
        "n12_sign_prediction_frozen": LOCKED_LEDGER[-1][1] < 0,
        "locked_n10_factorization": factor_locked_integer(-15125) == {5: 3, 11: 2},
    }
    boundary = boundary_profiles()
    jordan = jordan_mod5_certificate()
    return {
        "run_ids": ["R020-control", "R030", "R031", "R032", "R033"],
        "determinant_checks": determinant_checks,
        "boundary": boundary,
        "jordan": jordan,
        "pass": all(determinant_checks.values()) and boundary["pass"] and jordan["pass"],
    }


def corruption_rejection_controls() -> dict[str, Any]:
    rows = []
    for period, delta, factors, selected in LOCKED_LEDGER:
        rows.append(
            {
                "period": period,
                "delta_direct": delta,
                "delta_recurrence": delta,
                "factorization": {str(key): value for key, value in sorted(factors.items())},
                "support": sorted(factors),
                "selected_primitive_prime": selected,
            }
        )
    valid = validate_locked_ledger_rows(rows)
    corrupted_period = [{**row} for row in rows]
    corrupted_period[5]["delta_direct"] = -319
    corrupted_factor = [{**row} for row in rows]
    corrupted_factor[9]["factorization"] = {"5": 2, "11": 2}
    expected_profiles = {
        str(prime): {str(period): count for period, count in profile.items()}
        for prime, profile in EXPECTED_PERIOD_PROFILES.items()
    }
    boundary = {
        "profiles": expected_profiles,
        "jordan_period_ten_points": 20,
        "jordan_period_ten_cycles": 2,
        "period_6_carriers": 0,
        "period_12_carriers": 0,
    }
    corrupted_jordan = {**boundary, "jordan_period_ten_points": 19}
    checks = {
        "valid_static_rows_accepted": valid["pass"],
        "corrupted_period_rejected": validate_locked_ledger_rows(corrupted_period)["pass"] is False,
        "corrupted_factorization_rejected": validate_locked_ledger_rows(corrupted_factor)["pass"] is False,
        "valid_boundary_accepted": validate_boundary_summary(boundary)["pass"],
        "corrupted_jordan_rejected": validate_boundary_summary(corrupted_jordan)["pass"] is False,
        "forbidden_negative_trace_shortcut_rejected": negative_trace_index(14)[
            "primitive_index"
        ]
        != 14,
    }
    return {
        "run_id": "R034-negative-controls",
        "checks": checks,
        "pass": all(checks.values()),
    }


def clock_controls() -> dict[str, Any]:
    point = (Fraction(2, 9), Fraction(1, 6))
    invariant = order_invariance_certificate(CAT_MATRIX, point)
    integer_witnesses = [every_order_witness(order) for order in (1, 4, 6, 9)]
    perturbations = [perturbation_witness(point, index) for index in (1, 3, 7)]
    monodromy_5 = orbit_sum_monodromy_certificate(5, 11)
    monodromy_7 = orbit_sum_monodromy_certificate(7, 29)
    checks = {
        "exact_order_invariant": invariant["pass"],
        "prime_and_composite_orders_same_construction": all(
            record["pass"] for record in integer_witnesses
        ),
        "coprime_perturbations_have_product_order": all(
            record["pass"] for record in perturbations
        ),
        "orbit_sum_signature_exact": monodromy_5["orbit_sum"] == "5*log(11)",
        "monodromy_p_blind": (
            monodromy_5["dependence_signature"]["native_monodromy"] == ["period"]
            and monodromy_7["dependence_signature"]["native_monodromy"] == ["period"]
        ),
    }
    return {
        "run_ids": ["R040", "R041", "R042", "R043"],
        "invariance": invariant,
        "integer_witnesses": integer_witnesses,
        "perturbations": perturbations,
        "monodromy_records": [monodromy_5, monodromy_7],
        "checks": checks,
        "pass": all(checks.values()),
    }


def run_all_controls(project_root: Path) -> dict[str, Any]:
    _raw_absolute(project_root)
    records = {
        "input_scope": input_scope_controls(),
        "small_exact": exact_small_controls(),
        "corruption_rejection": corruption_rejection_controls(),
        "clock": clock_controls(),
    }
    return {
        "stage": "P2_CONTROLS_ONLY",
        "records": records,
        "registered_candidate_accessed": False,
        "periods_above_twelve_computed": False,
        "external_data_accessed": False,
        "pass": all(record["pass"] for record in records.values()),
    }
