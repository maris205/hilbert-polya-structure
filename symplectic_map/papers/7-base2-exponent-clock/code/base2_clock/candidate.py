"""Fail-closed P4 exact reproduction for the frozen candidate."""

from __future__ import annotations

from pathlib import Path
from time import perf_counter_ns
from typing import Any

from .algebra import candidate_map
from .dynatomic import audit_period, certificate_record
from .lifecycle import validate_registered_claim
from .protocol import EXPECTED_LOCK_SHA256, _raw_absolute, load_exact_json
from .review_gate import reviewed_code_tree_sha256


REGISTERED_PERIODS = tuple(range(2, 8))


def _require_deployment_authority(project_root: Path) -> dict[str, Any]:
    """Revalidate P0--P3 and the durable STARTED claim immediately before P4."""

    from .manifest import collect_safe_preflight, validate_official_preflight

    preflight = collect_safe_preflight(project_root)
    source = preflight["gates"]["source_lock"]
    review = preflight["independent_review"]
    current_digest = reviewed_code_tree_sha256(project_root)
    if preflight.get("pass") is not True:
        raise RuntimeError("P0--P2 gate failed before registered candidate execution")
    if preflight.get("status") != "AUTHORIZED_FOR_REGISTERED_EXECUTION":
        raise RuntimeError("P3 independent DEPLOYMENT_PASS is missing or stale")
    authority = review.get("authority")
    if type(authority) is not dict:
        raise RuntimeError("independent review authority is malformed")
    if authority.get("source_lock_sha256") != EXPECTED_LOCK_SHA256:
        raise RuntimeError("independent review is not bound to source-lock v2")
    if authority.get("reviewed_code_sha256") != current_digest:
        raise RuntimeError("independent review is not bound to the current code tree")
    official_path = project_root / "results" / "PRE_EXECUTION_AUDIT.json"
    official = load_exact_json(official_path)
    official_errors = validate_official_preflight(official, preflight)
    if official_errors:
        raise RuntimeError("official pre-execution audit is not the live P0--P3 snapshot")
    claim = validate_registered_claim(project_root, current_digest, require_clean_started=True)
    if claim.get("pass") is not True:
        raise RuntimeError("durable STARTED claim is missing or invalid")
    return {
        "source_lock": source,
        "independent_review": review,
        "preflight": preflight,
        "claim": claim,
        "reviewed_code_sha256": current_digest,
    }


def run_registered_candidate(project_root: Path) -> dict[str, Any]:
    """Run exactly periods 2--7, stopping on any hit or certificate mismatch."""

    project_root = _raw_absolute(project_root)
    authorization = _require_deployment_authority(project_root)
    expected_tree = authorization["reviewed_code_sha256"]
    field, base = candidate_map()
    period_records: list[dict[str, Any]] = []
    stopped_on_hit = False
    for period in REGISTERED_PERIODS:
        if reviewed_code_tree_sha256(project_root) != expected_tree:
            raise RuntimeError("reviewed code tree changed before a registered period")
        started = perf_counter_ns()
        certificate = audit_period(base, period, targets=(1, -1), field=field)
        elapsed_ns = perf_counter_ns() - started
        record = certificate_record(certificate, field=field, include_polynomials=True)
        record["run_id"] = f"R04{period}"
        record["evidentiary_role"] = "DEVELOPMENT_SEEN_REPRODUCTION"
        record["wall_time_nanoseconds"] = elapsed_ns
        record["optional_q3_diagnostic"] = "NOT_REQUESTED"
        if record["status"] != "PASS":
            raise RuntimeError(f"mandatory exact-engine disagreement at period {period}")
        hits = [item for item in record["targets"] if item["hit"]]
        period_records.append(record)
        if hits:
            stopped_on_hit = True
            break

    if reviewed_code_tree_sha256(project_root) != expected_tree:
        raise RuntimeError("reviewed code tree changed during registered execution")

    periods_executed = [record["period"] for record in period_records]
    completed_cutoff = periods_executed == list(REGISTERED_PERIODS)
    if stopped_on_hit:
        classification = "TARGET_HIT_STOP_REQUIRES_TWO_EXACT_EXTRACTION_CERTIFICATES"
    elif completed_cutoff:
        classification = "BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN"
    else:
        classification = "NOT_EXECUTED_RESOURCE_LIMIT"
    return {
        "schema": "BASE2_REGISTERED_CANDIDATE_AUDIT_V1",
        "candidate_id": "pcf_quadratic_exact_2adic_boundary_v1",
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": expected_tree,
        "registered_periods_frozen": list(REGISTERED_PERIODS),
        "periods_executed": periods_executed,
        "new_blind_periods": [],
        "development_seen_periods": list(REGISTERED_PERIODS),
        "period_records": period_records,
        "stopped_on_target_hit": stopped_on_hit,
        "completed_frozen_cutoff": completed_cutoff,
        "candidate_numerical_runs": 0,
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "approximate_matching_used": False,
        "classification": classification,
        "all_period_equality_status": "OPEN_FOR_N_GE_4",
        "route_a": "NOT_ADVANCED",
        "route_b": "NOT_OPENED",
        "pass": completed_cutoff and not stopped_on_hit,
    }
