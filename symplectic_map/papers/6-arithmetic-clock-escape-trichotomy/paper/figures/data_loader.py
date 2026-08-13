"""Fail-closed loader for the Paper-5 publication figures.

The figures may consume only the five official machine-readable artifacts in
``ALLOWED_INPUTS``.  This module validates their mutual hashes, source lock,
reviewed tree, registered classification, zero-target-data counters, proof and
scope provenance, and terminal upstream records before returning display data.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ALLOWED_INPUTS = {
    "results": PROJECT_ROOT / "results" / "EXPERIMENT_RESULTS.json",
    "manifest": PROJECT_ROOT / "results" / "result_manifest.json",
    "proof": PROJECT_ROOT / "experiments" / "proof_ledger.json",
    "scope": PROJECT_ROOT / "experiments" / "scope_ledger.json",
    "upstream": PROJECT_ROOT / "experiments" / "upstream_bindings.json",
}


class FigureDataError(RuntimeError):
    """Raised when an official figure input fails provenance or scope checks."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise FigureDataError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _regular_in_project(path: Path) -> bool:
    project = PROJECT_ROOT.resolve()
    absolute = path.absolute()
    try:
        absolute.relative_to(project)
    except ValueError:
        return False
    current = absolute
    while current != project:
        if current.is_symlink():
            return False
        current = current.parent
    return absolute.is_file() and absolute.resolve() == absolute


def _read_json(path: Path) -> Any:
    if path not in ALLOWED_INPUTS.values():
        raise FigureDataError(f"unapproved figure input: {path}")
    if not _regular_in_project(path):
        raise FigureDataError(f"unsafe or missing figure input: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except json.JSONDecodeError as error:
        raise FigureDataError(f"malformed JSON in {path.name}: {error}") from error


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _exact_int(value: Any, expected: int) -> bool:
    return type(value) is int and value == expected


def _hash_string(value: Any) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise FigureDataError(message)


@dataclass(frozen=True)
class FigureData:
    candidate_id: str
    source_lock_sha256: str
    reviewed_code_sha256: str
    registered_at_utc: str
    classification: str
    readout_form: str
    theorem_statement: str
    proof_claims: dict[str, dict[str, Any]]
    proof_flow: tuple[dict[str, Any], ...]
    source_classes: tuple[dict[str, Any], ...]
    admitted_operations: tuple[dict[str, Any], ...]
    excluded_operations: tuple[dict[str, Any], ...]
    escape_semantics: dict[str, bool]
    controls: dict[str, dict[str, Any]]
    gate_rows: tuple[dict[str, Any], ...]
    upstream_rows: tuple[dict[str, Any], ...]
    audit_metrics: dict[str, int]
    input_hashes: dict[str, str]


def load_figure_data() -> FigureData:
    """Load and validate every official input before exposing figure data."""

    result = _read_json(ALLOWED_INPUTS["results"])
    manifest = _read_json(ALLOWED_INPUTS["manifest"])
    proof = _read_json(ALLOWED_INPUTS["proof"])
    scope = _read_json(ALLOWED_INPUTS["scope"])
    upstream = _read_json(ALLOWED_INPUTS["upstream"])
    for label, payload in {
        "results": result,
        "manifest": manifest,
        "proof": proof,
        "scope": scope,
        "upstream": upstream,
    }.items():
        _require(type(payload) is dict, f"{label} root is not an object")

    candidate = result.get("candidate_id")
    source_hash = result.get("source_lock_sha256")
    tree_hash = result.get("reviewed_code_sha256")
    _require(type(candidate) is str and candidate, "missing registered candidate ID")
    _require(_hash_string(source_hash), "invalid registered source-lock hash")
    _require(_hash_string(tree_hash), "invalid registered reviewed-tree hash")
    _require(result.get("schema") == "CAPACITY_REGISTERED_AUDIT_V1", "wrong registered schema")
    _require(result.get("audit_type") == "EXACT_SYMBOLIC_AND_STATIC_ONLY", "wrong audit type")
    _require(result.get("classification") == "CAPACITY_BOUND_CERTIFIED", "uncertified classification")
    _require(result.get("pass") is True, "registered audit is not passing")
    _require(result.get("external_prime_tables_accessed") is False, "prime table flag is not false")
    _require(result.get("prime_target_arrays_generated") is False, "target-array flag is not false")
    _require(result.get("riemann_zero_data_accessed") is False, "zero-data flag is not false")
    _require(_exact_int(result.get("candidate_numerical_runs"), 0), "candidate run count is not exact zero")
    _require(_exact_int(result.get("target_matches_computed"), 0), "target match count is not exact zero")

    gates = result.get("gates")
    expected_gate_ids = {
        "escape_semantics",
        "exact_controls",
        "executable_isolation",
        "independent_code_review",
        "output_scope",
        "proof_ledger",
        "scope_ledger",
        "source_lock",
        "upstream_bindings",
    }
    _require(type(gates) is dict and set(gates) == expected_gate_ids, "registered gate set is not exact")
    _require(
        all(type(record) is dict and record.get("pass") is True for record in gates.values()),
        "one or more registered gates are not passing",
    )
    review = gates["independent_code_review"]
    authority = review.get("authority")
    _require(type(authority) is dict, "missing independent review authority")
    _require(authority.get("reviewed_code_sha256") == tree_hash, "review/tree mismatch")
    _require(authority.get("source_lock_sha256") == source_hash, "review/source mismatch")
    _require(authority.get("reviewer_independent") is True, "review is not independent")
    _require(authority.get("verdict") == "DEPLOYMENT_PASS", "review did not pass")
    source_gate = gates["source_lock"]
    _require(source_gate.get("sha256") == source_hash, "source gate digest mismatch")
    _require(source_gate.get("expected_sha256") == source_hash, "source gate expectation mismatch")

    _require(manifest.get("schema") == "CAPACITY_RESULT_MANIFEST_V1", "wrong result-manifest schema")
    _require(manifest.get("candidate_id") == candidate, "manifest candidate mismatch")
    _require(manifest.get("source_lock_sha256") == source_hash, "manifest source mismatch")
    _require(manifest.get("reviewed_code_sha256") == tree_hash, "manifest tree mismatch")
    _require(manifest.get("pass") is True, "result manifest is not passing")
    _require(manifest.get("result_tree", {}).get("pass") is True, "result-tree closure failed")
    semantics = manifest.get("semantic_checks")
    _require(type(semantics) is dict and semantics.get("pass") is True, "manifest semantics failed")
    _require(semantics.get("reviewed_code_sha256") == tree_hash, "semantic tree mismatch")

    file_records = manifest.get("files")
    _require(type(file_records) is list, "manifest file list is missing")
    file_hashes: dict[str, str] = {}
    for record in file_records:
        _require(type(record) is dict and set(record) == {"path", "sha256"}, "malformed manifest record")
        relative = record.get("path")
        digest = record.get("sha256")
        _require(type(relative) is str and _hash_string(digest), "malformed manifest hash record")
        _require(relative not in file_hashes, "duplicate manifest path")
        file_hashes[relative] = digest
    for key in ("results", "proof", "scope", "upstream"):
        relative = ALLOWED_INPUTS[key].relative_to(PROJECT_ROOT).as_posix()
        _require(file_hashes.get(relative) == _sha256(ALLOWED_INPUTS[key]), f"manifest hash mismatch: {relative}")
    _require(semantics.get("result_sha256") == _sha256(ALLOWED_INPUTS["results"]), "result digest mismatch")

    _require(proof.get("schema") == "CAPACITY_PROOF_LEDGER_V1", "wrong proof-ledger schema")
    _require(scope.get("schema") == "CAPACITY_SCOPE_LEDGER_V1", "wrong scope-ledger schema")
    _require(upstream.get("schema") == "CAPACITY_UPSTREAM_BINDINGS_V2", "wrong upstream schema")
    for label, payload in {"proof": proof, "scope": scope, "upstream": upstream}.items():
        _require(payload.get("candidate_id") == candidate, f"{label} candidate mismatch")
    _require(proof.get("source_lock_sha256") == source_hash, "proof source mismatch")
    _require(scope.get("source_lock_sha256") == source_hash, "scope source mismatch")

    claims_list = proof.get("claims")
    _require(type(claims_list) is list and claims_list, "proof claims are missing")
    proof_claims: dict[str, dict[str, Any]] = {}
    for claim in claims_list:
        _require(type(claim) is dict and type(claim.get("id")) is str, "malformed proof claim")
        claim_id = claim["id"]
        _require(claim_id not in proof_claims, "duplicate proof claim ID")
        _require(claim.get("status") in {"LOCKED", "PROVED"}, "unaccepted proof status")
        _require(type(claim.get("statement")) is str and claim["statement"], "empty proof statement")
        proof_claims[claim_id] = claim
    _require("T010" in proof_claims, "terminal capacity theorem claim is missing")
    proof_flow_ids = tuple(f"T{index:03d}" for index in range(5, 11))
    _require(all(claim_id in proof_claims for claim_id in proof_flow_ids), "proof flow is incomplete")

    source_classes: list[dict[str, Any]] = []
    for prefix, label in (("L", "Locally constant"), ("M", "Multiplier"), ("A", "Algebraic action")):
        records = sorted(
            (claim for claim_id, claim in proof_claims.items() if claim_id.startswith(prefix)),
            key=lambda claim: claim["id"],
        )
        _require(records and all(record["status"] == "PROVED" for record in records), f"Class {prefix} not proved")
        source_classes.append(
            {
                "prefix": prefix,
                "label": label,
                "count": len(records),
                "ids": tuple(record["id"] for record in records),
                "terminal_statement": records[-1]["statement"],
                "all_proved": True,
            }
        )

    admitted = scope.get("admitted")
    excluded = scope.get("excluded")
    escape = scope.get("escape_semantics")
    _require(type(admitted) is list and type(excluded) is list, "scope operations are missing")
    _require(type(escape) is dict, "escape semantics are missing")
    expected_escape = {
        "necessary_certificate_failures": True,
        "mutually_exclusive": False,
        "jointly_exhaustive_for_all_dynamics": False,
        "sufficient_for_arithmetic_correspondence": False,
    }
    _require(escape == expected_escape, "escape semantics changed")

    control_list = gates["exact_controls"].get("records")
    _require(type(control_list) is list and control_list, "exact controls are missing")
    controls: dict[str, dict[str, Any]] = {}
    for control in control_list:
        _require(type(control) is dict and type(control.get("control_id")) is str, "malformed control")
        _require(control.get("pass") is True, "a boundary control failed")
        controls[control["control_id"]] = control
    _require({"K001", "K002", "K003"}.issubset(controls), "boundary controls are incomplete")

    binding_list = upstream.get("bindings")
    upstream_gate_records = gates["upstream_bindings"].get("records")
    _require(type(binding_list) is list and type(upstream_gate_records) is list, "upstream records are missing")
    bindings_by_id = {record.get("id"): record for record in binding_list if type(record) is dict}
    gate_upstream_by_id = {record.get("id"): record for record in upstream_gate_records if type(record) is dict}
    _require(len(bindings_by_id) == len(binding_list) == 2, "upstream binding ID set is not exact")
    _require(set(bindings_by_id) == set(gate_upstream_by_id), "binding/gate upstream IDs differ")
    upstream_rows: list[dict[str, Any]] = []
    for upstream_id in sorted(bindings_by_id):
        binding = bindings_by_id[upstream_id]
        gate_record = gate_upstream_by_id[upstream_id]
        _require(binding.get("status") == "FINAL_INTEGRITY_VERIFIED", "upstream status is not terminal")
        for field in ("binding_matches_frozen_constants", "manifest_semantics_pass", "pipeline_final_semantics_pass", "pass"):
            _require(gate_record.get(field) is True, f"upstream {upstream_id} failed {field}")
        for hash_field in (
            "source_lock_sha256",
            "proof_package_sha256",
            "final_result_manifest_sha256",
            "pipeline_state_sha256",
            "final_integrity_sha256",
            "final_pdf_sha256",
            "final_review_sha256",
        ):
            _require(binding.get(hash_field) == gate_record.get(hash_field), f"upstream cross-hash mismatch: {hash_field}")
        upstream_rows.append(
            {
                "id": upstream_id,
                "candidate_id": binding["candidate_id"],
                "frozen": gate_record["binding_matches_frozen_constants"],
                "manifest": gate_record["manifest_semantics_pass"],
                "pipeline": gate_record["pipeline_final_semantics_pass"],
                "pass": gate_record["pass"],
            }
        )

    gate_rows = tuple(
        {
            "id": gate_id,
            "label": gate_id.replace("_", " ").title(),
            "pass": gates[gate_id]["pass"],
        }
        for gate_id in (
            "escape_semantics",
            "source_lock",
            "independent_code_review",
            "proof_ledger",
            "scope_ledger",
            "exact_controls",
            "executable_isolation",
            "upstream_bindings",
            "output_scope",
        )
    )
    audit_metrics = {
        "proof_ids": len(gates["proof_ledger"].get("observed_ids", [])),
        "proof_cycles": len(gates["proof_ledger"].get("dependency_cycles", [])),
        "admitted_operations": len(gates["scope_ledger"].get("admitted_ids", [])),
        "excluded_operations": len(gates["scope_ledger"].get("excluded_ids", [])),
        "controls": len(control_list),
        "scanned_files": len(gates["executable_isolation"].get("scanned_files", [])),
        "scanner_findings": len(gates["executable_isolation"].get("findings", [])),
        "target_matches": result["target_matches_computed"],
    }

    return FigureData(
        candidate_id=candidate,
        source_lock_sha256=source_hash,
        reviewed_code_sha256=tree_hash,
        registered_at_utc=result["registered_at_utc"],
        classification=result["classification"],
        readout_form=scope["readout_form"],
        theorem_statement=proof_claims["T010"]["statement"],
        proof_claims=proof_claims,
        proof_flow=tuple(proof_claims[claim_id] for claim_id in proof_flow_ids),
        source_classes=tuple(source_classes),
        admitted_operations=tuple(admitted),
        excluded_operations=tuple(excluded),
        escape_semantics=escape,
        controls=controls,
        gate_rows=gate_rows,
        upstream_rows=tuple(upstream_rows),
        audit_metrics=audit_metrics,
        input_hashes={key: _sha256(path) for key, path in ALLOWED_INPUTS.items()},
    )


if __name__ == "__main__":
    data = load_figure_data()
    print(
        json.dumps(
            {
                "candidate_id": data.candidate_id,
                "source_lock_sha256": data.source_lock_sha256,
                "reviewed_code_sha256": data.reviewed_code_sha256,
                "classification": data.classification,
                "input_hashes": data.input_hashes,
            },
            indent=2,
            sort_keys=True,
        )
    )
