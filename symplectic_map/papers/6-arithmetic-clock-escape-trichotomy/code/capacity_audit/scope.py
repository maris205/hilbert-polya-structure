"""Fail-closed output and escape-semantics classifiers."""

from __future__ import annotations

from typing import Any, Iterable


ALLOWED_DECISION_LABELS = {
    "CAPACITY_BOUND_CERTIFIED",
    "NARROW_OR_MERGE",
    "REJECTED_OR_REQUIRES_AMENDMENT",
}
FORBIDDEN_CLAIM_IDS = {
    "UNIVERSAL_SYMPLECTIC_NO_GO",
    "COMPLETE_ESCAPE_TRICHOTOMY",
    "PRIME_CLOCKS_REQUIRE_INFINITE_DIMENSION",
    "HISTORICAL_FIRST",
    "RIEMANN_ZERO_PROGRESS",
    "ROUTE_B_PROGRESS",
}


def audit_output_scope(
    decision_label: str,
    asserted_claim_ids: Iterable[str] = (),
) -> dict[str, Any]:
    """Reject unknown decisions and every explicitly forbidden broad claim."""

    asserted = list(asserted_claim_ids)
    forbidden_asserted = sorted(FORBIDDEN_CLAIM_IDS.intersection(asserted))
    unknown_asserted = sorted(set(asserted).difference(FORBIDDEN_CLAIM_IDS))
    decision_allowed = decision_label in ALLOWED_DECISION_LABELS
    return {
        "decision_label": decision_label,
        "decision_allowed": decision_allowed,
        "asserted_claim_ids": asserted,
        "forbidden_asserted": forbidden_asserted,
        "unknown_asserted": unknown_asserted,
        "universal_no_go_asserted": False if not forbidden_asserted else None,
        "complete_trichotomy_asserted": False if not forbidden_asserted else None,
        "route_b_progress_asserted": False if not forbidden_asserted else None,
        "pass": decision_allowed and not forbidden_asserted and not unknown_asserted,
    }


def audit_escape_semantics(
    *,
    necessary: bool,
    mutually_exclusive: bool,
    exhaustive_for_all_dynamics: bool,
    sufficient: bool,
) -> dict[str, Any]:
    """Accept only the scoped necessary-failure interpretation."""

    passed = necessary and not mutually_exclusive and not exhaustive_for_all_dynamics and not sufficient
    return {
        "necessary_certificate_failures": necessary,
        "mutually_exclusive": mutually_exclusive,
        "exhaustive_for_all_dynamics": exhaustive_for_all_dynamics,
        "sufficient_for_arithmetic_correspondence": sufficient,
        "pass": passed,
    }
