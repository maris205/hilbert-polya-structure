"""Frozen negative requests rejected before either scientific engine starts."""

from __future__ import annotations

from typing import Any


NEGATIVE_FIXTURES: tuple[dict[str, Any], ...] = (
    {
        "control_id": "K001",
        "request": "mutate_cyclic_jacobian",
        "mutation": "omit_epsilon_squared_sum",
    },
    {
        "control_id": "K002",
        "request": "mutate_trace_residue_exponent",
        "residue_power_offset": 0,
    },
    {
        "control_id": "K003",
        "request": "mutate_period_normalization",
        "divide_by_three_before_fixed_subtraction": True,
    },
    {
        "control_id": "K004",
        "request": "assert_quartic_fiber_membership",
        "polynomial": "x^4-x",
    },
    {
        "control_id": "K005",
        "request": "expand_conjugacy_scope",
        "scope": "unrestricted_global_polynomial_automorphisms",
    },
    {
        "control_id": "K006",
        "request": "promote_finite_history",
        "history_indices": [2, 3, 4, 5, 6, 7],
        "claim": "universal_nonvanishing",
    },
    {
        "control_id": "K007",
        "request": "breach_engine_isolation",
        "targets": [
            "track_q_private_intermediate_to_track_r",
            "track_r_private_helper_to_track_q",
            "acceptance_ledger_to_scientific_engine",
        ],
    },
    {
        "control_id": "K008",
        "request": "breach_closed_world",
        "targets": [
            "index_10",
            "network",
            "external_prime_table",
            "numerical_root_solver",
            "interpolation",
        ],
    },
)


REASON_CODES = {
    "K001": "CYCLIC_JACOBIAN_DEFINITION_MUTATION",
    "K002": "TRACE_RESIDUE_EXPONENT_MUTATION",
    "K003": "PREMATURE_CYCLE_NORMALIZATION",
    "K004": "QUARTIC_SIMPLE_ROOT_OUTSIDE_FIBER",
    "K005": "NORMALIZED_SCOPE_EXPANSION",
    "K006": "FINITE_HISTORY_UNIVERSAL_OVERCLAIM",
    "K007": "ENGINE_OR_LEDGER_ISOLATION_BREACH",
    "K008": "CLOSED_WORLD_OR_INDEX_BREACH",
}


def reject_request(fixture: dict[str, Any]) -> dict[str, Any]:
    if type(fixture) is not dict or type(fixture.get("control_id")) is not str:
        raise TypeError("malformed negative fixture")
    control_id = fixture["control_id"]
    if control_id not in REASON_CODES:
        raise ValueError("unregistered negative fixture")
    expected_request = {
        "K001": "mutate_cyclic_jacobian",
        "K002": "mutate_trace_residue_exponent",
        "K003": "mutate_period_normalization",
        "K004": "assert_quartic_fiber_membership",
        "K005": "expand_conjugacy_scope",
        "K006": "promote_finite_history",
        "K007": "breach_engine_isolation",
        "K008": "breach_closed_world",
    }[control_id]
    if fixture.get("request") != expected_request:
        raise ValueError("fixture ID/request mismatch")
    return {
        "control_id": control_id,
        "outcome": "REJECTED_BEFORE_SCIENTIFIC_DISPATCH",
        "reason_code": REASON_CODES[control_id],
        "scientific_engine_dispatch_count": 0,
        "scientific_field_emitted_count": 0,
    }


def run_negative_controls() -> list[dict[str, Any]]:
    records = [reject_request(dict(fixture)) for fixture in NEGATIVE_FIXTURES]
    if len(records) != 8 or [record["control_id"] for record in records] != [
        "K001", "K002", "K003", "K004", "K005", "K006", "K007", "K008"
    ]:
        raise RuntimeError("negative control registry changed")
    if any(record["scientific_engine_dispatch_count"] != 0 for record in records):
        raise RuntimeError("negative control reached an engine")
    return records
