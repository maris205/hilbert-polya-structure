"""P2 controls using the same exact-period and target engines as P4."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import quadratic_map
from .dynatomic import audit_period, certificate_record
from .protocol import (
    EXPECTED_UPSTREAM_EXACT_POLYNOMIALS_SHA256,
    _raw_absolute,
    regular_file,
    stable_file_bytes,
    strict_json_loads,
)


EXPECTED_CONJUGACY_AUDIT_SHA256 = (
    "c0edd8b509920890470c9f93f0256b0d2f2dbdd3a4f4da367c5abb128282fdb8"
)


def _target(record: dict[str, Any], value: int) -> dict[str, Any]:
    return next(item for item in record["targets"] if item["target"] == str(value))


def power_map_control() -> dict[str, Any]:
    """Exercise equality ``B=+1`` and the negative target ``B=2``."""

    certificate = audit_period(quadratic_map(0), 2, targets=(1, -1, 2))
    record = certificate_record(certificate)
    plus = _target(record, 1)
    minus = _target(record, -1)
    negative = _target(record, 2)
    checks = {
        "exact_period_two_nonempty": record["exact_set_degree"] == 2,
        "positive_equality_hit": plus["hit"] is True and plus["gcd_degree"] == 2,
        "negative_sign_absent": minus["hit"] is False,
        "target_B_equals_2_absent": negative["hit"] is False,
        "all_engines_agree": all(item["gcd_resultant_norm_agree"] for item in record["targets"]),
    }
    return {
        "run_ids": ["R020", "R022"],
        "control_id": "power_map_and_negative_target",
        "map": "z^2",
        "period_record": record,
        "checks": checks,
        "pass": record["status"] == "PASS" and all(checks.values()),
    }


def chebyshev_control() -> dict[str, Any]:
    """Exercise the frozen signed equality prediction at exact period two."""

    base = quadratic_map(-2)
    certificate = audit_period(base, 2, targets=(1, -1))
    record = certificate_record(certificate)
    z = base.gens[0]
    expected_exact = sp.Poly(z**2 + z - 1, z, domain=sp.QQ)
    normalized_remainder = certificate.normalized_cycle_product.rem(certificate.component.exact_set)
    multiplier_remainder = 4 * normalized_remainder
    checks = {
        "Psi_2_equals_X2_plus_X_minus_1": certificate.component.exact_set == expected_exact,
        "B_2_is_minus_one_on_exact_set": normalized_remainder == sp.Poly(-1, z, domain=sp.QQ),
        "negative_equality_hit": _target(record, -1)["hit"] is True,
        "positive_sign_absent_at_n2": _target(record, 1)["hit"] is False,
        "Lambda_equals_minus_4": multiplier_remainder == sp.Poly(-4, z, domain=sp.QQ),
    }
    return {
        "run_id": "R021",
        "control_id": "chebyshev_signed_equality",
        "map": "z^2-2",
        "period_record": record,
        "checks": checks,
        "pass": record["status"] == "PASS" and all(checks.values()),
    }


def formal_period_pollution_control() -> dict[str, Any]:
    """Require the radical exact-set engine to remove all formal period-two pollution."""

    certificate = audit_period(quadratic_map(sp.Rational(-3, 4)), 2, targets=(1, -1))
    record = certificate_record(certificate)
    checks = {
        "formal_component_nonempty": record["formal_dynatomic_degree"] > 0,
        "set_exact_component_empty": record["exact_set_degree"] == 0,
        "formal_diagnostic_not_substituted": record["formal_radical_equals_exact_set"] is False,
        "lower_overlap_removes_all_F2_roots": (
            record["lower_overlap_degree"] == record["iterate_radical_degree"]
        ),
        "no_false_target_hit": all(item["hit"] is False for item in record["targets"]),
    }
    return {
        "run_id": "R023",
        "control_id": "formal_period_pollution",
        "map": "z^2-3/4",
        "period_record": record,
        "checks": checks,
        "pass": record["status"] == "PASS" and all(checks.values()),
    }


def upstream_regression_control(project_root: Path) -> dict[str, Any]:
    """Bind the Paper-2 polynomial ledger and its independent conjugacy audit."""

    upstream_root = _raw_absolute(project_root).parent / "3-prime-multiplier-obstruction"
    exact_path = upstream_root / "results" / "exact_polynomials.json"
    conjugacy_path = upstream_root / "results" / "conjugacy_audit.json"
    exact_safe = regular_file(exact_path)
    conjugacy_safe = regular_file(conjugacy_path)
    exact_bytes = stable_file_bytes(exact_path) if exact_safe else b""
    conjugacy_bytes = stable_file_bytes(conjugacy_path) if conjugacy_safe else b""
    exact_hash = hashlib.sha256(exact_bytes).hexdigest() if exact_safe else None
    conjugacy_hash = hashlib.sha256(conjugacy_bytes).hexdigest() if conjugacy_safe else None
    payload = strict_json_loads(exact_bytes.decode("utf-8")) if exact_safe else {}
    conjugacy = strict_json_loads(conjugacy_bytes.decode("utf-8")) if conjugacy_safe else {}
    candidate = payload.get("candidate_g", {})
    inherited = payload.get("conjugate_f_u", {})
    periods = [str(item) for item in range(1, 5)]
    expected_cycle_expressions = {
        "1": "L**2 - 2*L - 4*u",
        "2": "L - 4 + 4*u",
        "3": "L**2 + L*(-16 + 8*u) - 64 + 64*u",
        "4": "L**3 + L**2*(-48 + 16*u**2) + L*(256 + 256*u**2) + 4096",
    }
    expected_formal_degrees = {"1": 2, "2": 2, "3": 6, "4": 12}
    invariant_matches = all(
        candidate.get(period, {}).get("cycle_multiplier_polynomial")
        == inherited.get(period, {}).get("cycle_multiplier_polynomial")
        and candidate.get(period, {}).get("point_resultant")
        == inherited.get(period, {}).get("point_resultant")
        for period in periods
    )
    cycle_expressions_match = all(
        candidate.get(period, {})
        .get("cycle_multiplier_polynomial", {})
        .get("expression")
        == expected_cycle_expressions[period]
        for period in periods
    )
    formal_degrees_match = all(
        candidate.get(period, {})
        .get("formal_dynatomic_polynomial", {})
        .get("degree")
        == expected_formal_degrees[period]
        for period in periods
    )
    conjugacy_periods_pass = (
        conjugacy.get("status") == "PASS"
        and [item.get("period") for item in conjugacy.get("periods", [])] == list(range(1, 5))
        and all(item.get("status") == "PASS" for item in conjugacy.get("periods", []))
    )
    checks = {
        "exact_polynomial_file_safe": exact_safe,
        "exact_polynomial_hash": exact_hash == EXPECTED_UPSTREAM_EXACT_POLYNOMIALS_SHA256,
        "schema": payload.get("schema") == "exact-polynomial-index-v1",
        "periods_1_to_4_exact": sorted(candidate) == periods and sorted(inherited) == periods,
        "f_u_g_multiplier_invariants_equal": invariant_matches,
        "formal_degrees_2_2_6_12": formal_degrees_match,
        "frozen_cycle_polynomials_equal": cycle_expressions_match,
        "conjugacy_file_safe": conjugacy_safe,
        "conjugacy_hash": conjugacy_hash == EXPECTED_CONJUGACY_AUDIT_SHA256,
        "conjugacy_records_pass": conjugacy_periods_pass,
    }
    return {
        "run_id": "R024",
        "control_id": "upstream_paper2_regression",
        "mode": "HASH_AND_LEDGER_ONLY_NO_CANDIDATE_EXECUTION",
        "exact_polynomials_sha256": exact_hash,
        "conjugacy_audit_sha256": conjugacy_hash,
        "checks": checks,
        "pass": all(checks.values()),
    }


def run_all_controls(project_root: Path) -> dict[str, Any]:
    """Run the four dynamical controls and the hash-only inheritance control."""

    records = [
        power_map_control(),
        chebyshev_control(),
        formal_period_pollution_control(),
        upstream_regression_control(project_root),
    ]
    # R020 and R022 share one power-map engine call but remain separate registry ids.
    return {
        "stage": "P2_CONTROLS_ONLY",
        "records": records,
        "registered_candidate_accessed": False,
        "external_data_accessed": False,
        "pass": all(record["pass"] for record in records),
    }
