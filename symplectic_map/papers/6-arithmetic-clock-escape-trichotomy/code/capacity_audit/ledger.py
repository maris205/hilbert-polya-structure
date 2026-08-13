"""Structured proof and scope ledger validation without phrase-based proof gates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .protocol import CANDIDATE_ID, EXPECTED_LOCK_SHA256, EXPECTED_REVIEW_SHA256


REQUIRED_PROOF_IDS = {
    "T001",
    "T002",
    "T003",
    "T004",
    "T005",
    "T006",
    "T007",
    "T008",
    "T009",
    "T010",
    "L001",
    "M001",
    "M002",
    "M003",
    "M004",
    "M005",
    "A001",
    "A002",
    "C001",
    "E001",
}
ALLOWED_PROOF_KINDS = {
    "ASSUMPTION",
    "LEMMA",
    "PROOF_STEP",
    "THEOREM",
    "CLASS_CERTIFICATE",
    "COROLLARY",
}
ALLOWED_PROOF_STATUSES = {"LOCKED", "PROVED"}

REQUIRED_ADMITTED_SCOPE_IDS = {f"S{index:03d}" for index in range(1, 11)}
REQUIRED_EXCLUDED_SCOPE_IDS = {f"X{index:03d}" for index in range(1, 10)}
REQUIRED_FORBIDDEN_OUTPUT_IDS = {
    "UNIVERSAL_SYMPLECTIC_NO_GO",
    "COMPLETE_ESCAPE_TRICHOTOMY",
    "PRIME_CLOCKS_REQUIRE_INFINITE_DIMENSION",
    "HISTORICAL_FIRST",
    "RIEMANN_ZERO_PROGRESS",
    "ROUTE_B_PROGRESS",
}


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("ledger root must be a JSON object")
    return payload


def _dependency_cycles(records: dict[str, dict[str, Any]]) -> list[list[str]]:
    state: dict[str, int] = {claim_id: 0 for claim_id in records}
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(claim_id: str) -> None:
        state[claim_id] = 1
        stack.append(claim_id)
        for dependency in records[claim_id]["depends_on"]:
            if dependency not in records:
                continue
            if state[dependency] == 0:
                visit(dependency)
            elif state[dependency] == 1:
                start = stack.index(dependency)
                cycles.append(stack[start:] + [dependency])
        stack.pop()
        state[claim_id] = 2

    for claim_id in records:
        if state[claim_id] == 0:
            visit(claim_id)
    return cycles


def audit_proof_ledger(project_root: Path) -> dict[str, Any]:
    """Validate IDs, dependencies, statuses, and immutable provenance."""

    path = project_root.resolve() / "experiments" / "proof_ledger.json"
    payload = _load_json(path)
    claims = payload.get("claims", [])
    ids = [claim.get("id") for claim in claims if isinstance(claim, dict)]
    unique_ids = set(ids)
    duplicates = sorted({claim_id for claim_id in ids if ids.count(claim_id) > 1})
    records = {
        claim["id"]: claim
        for claim in claims
        if isinstance(claim, dict) and isinstance(claim.get("id"), str)
    }
    missing_dependencies = sorted(
        {
            dependency
            for claim in records.values()
            for dependency in claim.get("depends_on", [])
            if dependency not in records
        }
    )
    malformed = sorted(
        claim_id
        for claim_id, claim in records.items()
        if claim.get("kind") not in ALLOWED_PROOF_KINDS
        or claim.get("status") not in ALLOWED_PROOF_STATUSES
        or not isinstance(claim.get("evidence_ref"), str)
        or not claim["evidence_ref"].startswith("PROOF_PACKAGE.md#")
        or not isinstance(claim.get("depends_on"), list)
        or not isinstance(claim.get("statement"), str)
        or not claim["statement"]
    )
    cycles = _dependency_cycles(records) if not missing_dependencies and not malformed else []
    id_set_exact = unique_ids == REQUIRED_PROOF_IDS and len(ids) == len(REQUIRED_PROOF_IDS)
    provenance = (
        payload.get("schema") == "CAPACITY_PROOF_LEDGER_V1"
        and payload.get("candidate_id") == CANDIDATE_ID
        and payload.get("source_lock_sha256") == EXPECTED_LOCK_SHA256
        and payload.get("independent_review_sha256") == EXPECTED_REVIEW_SHA256
        and payload.get("machine_role")
        == "dependency and provenance ledger only; it does not replace the human mathematical proof"
    )
    passed = id_set_exact and not duplicates and not missing_dependencies and not malformed and not cycles and provenance
    return {
        "gate_id": "G080_PROOF_LEDGER",
        "path": str(path),
        "required_ids": sorted(REQUIRED_PROOF_IDS),
        "observed_ids": sorted(unique_ids),
        "id_set_exact": id_set_exact,
        "duplicates": duplicates,
        "missing_dependencies": missing_dependencies,
        "malformed_records": malformed,
        "dependency_cycles": cycles,
        "provenance_bound": provenance,
        "phrase_based_proof_acceptance": False,
        "pass": passed,
    }


def audit_scope_ledger(project_root: Path) -> dict[str, Any]:
    """Validate exact admitted/excluded operation IDs and escape semantics."""

    path = project_root.resolve() / "experiments" / "scope_ledger.json"
    payload = _load_json(path)
    admitted = payload.get("admitted", [])
    excluded = payload.get("excluded", [])
    admitted_ids = [record.get("id") for record in admitted if isinstance(record, dict)]
    excluded_ids = [record.get("id") for record in excluded if isinstance(record, dict)]
    malformed = [
        record.get("id", "<MISSING_ID>") if isinstance(record, dict) else "<NON_OBJECT>"
        for record in admitted + excluded
        if not isinstance(record, dict)
        or not isinstance(record.get("id"), str)
        or not isinstance(record.get("operation"), str)
        or not isinstance(record.get("reason"), str)
        or not record.get("reason")
    ]
    escape = payload.get("escape_semantics", {})
    escape_safe = (
        escape.get("necessary_certificate_failures") is True
        and escape.get("mutually_exclusive") is False
        and escape.get("jointly_exhaustive_for_all_dynamics") is False
        and escape.get("sufficient_for_arithmetic_correspondence") is False
    )
    forbidden_output_ids = set(payload.get("forbidden_output_claim_ids", []))
    provenance = (
        payload.get("schema") == "CAPACITY_SCOPE_LEDGER_V1"
        and payload.get("candidate_id") == CANDIDATE_ID
        and payload.get("source_lock_sha256") == EXPECTED_LOCK_SHA256
        and payload.get("readout_form") == "L=v+log(q)+alpha"
    )
    id_sets_exact = (
        set(admitted_ids) == REQUIRED_ADMITTED_SCOPE_IDS
        and len(admitted_ids) == len(REQUIRED_ADMITTED_SCOPE_IDS)
        and set(excluded_ids) == REQUIRED_EXCLUDED_SCOPE_IDS
        and len(excluded_ids) == len(REQUIRED_EXCLUDED_SCOPE_IDS)
    )
    passed = (
        id_sets_exact
        and not malformed
        and escape_safe
        and forbidden_output_ids == REQUIRED_FORBIDDEN_OUTPUT_IDS
        and provenance
    )
    return {
        "gate_id": "G080_SCOPE_LEDGER",
        "path": str(path),
        "admitted_ids": sorted(admitted_ids),
        "excluded_ids": sorted(excluded_ids),
        "id_sets_exact": id_sets_exact,
        "malformed_records": malformed,
        "escape_semantics_safe": escape_safe,
        "forbidden_output_ids_exact": forbidden_output_ids == REQUIRED_FORBIDDEN_OUTPUT_IDS,
        "provenance_bound": provenance,
        "pass": passed,
    }
