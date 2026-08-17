#!/usr/bin/env python3
"""Read-only exact-set and provenance auditor for Paper 43 integration.

The auditor writes only canonical stdout.  It does not import the producer,
scientific evaluators, renderer, runner, or project-local helpers.
"""

from __future__ import annotations

import base64
import ast
import hashlib
import json
import copy
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


EXPECTED_STATIC_MANIFEST = "STATIC_INPUT_SHA256SUMS.txt"
EXPECTED_INTEGRITY_CERTIFICATE = {
    "checks": {
        "authority_overlay_state_valid": True,
        "cache_and_symlink_hygiene": True,
        "canonical_json_types_and_bytes_exact": True,
        "canonical_output_payloads_portable": True,
        "da_binding_exact": True,
        "exact_output_namespace": True,
        "exact_result_ledger": True,
        "exact_result_set_certificate": True,
        "frozen_package_exact": True,
        "immutable_source_snapshot_exact": True,
        "integration_contract_exact": True,
        "packet_science_route_bindings_exact": True,
        "paired_provenance_state_legal": True,
        "route_and_independent_audit_clean": True,
        "static_input_manifest_exact": True,
        "writer_pointer_exact": True,
    },
    "checks_passed": 16,
    "checks_total": 16,
    "schema": "paper43-read-only-integrity-audit-v1",
    "status": "PASS",
}
OUTPUT_ROOT_PREFIXES = ("results/", "evaluations/")
HOST_TOKENS = tuple(("/" + name + "/").encode("ascii")
                    for name in ("tmp", "root", "home")) \
    + tuple(("\\" + name + "\\").encode("ascii")
            for name in ("tmp", "root", "home")) \
    + (("TMP" + "_").encode("ascii"),)
BASE64URL = re.compile(r"^[A-Za-z0-9_-]*$")
MAIN_CHECK_KEYS = {
    "card_raw_bytes_valid", "chronology_exact", "control_grid_exact",
    "crt_rows_recomputed", "factor_axioms_exact",
    "factor_proof_schema_recomputed", "finite_p0_rows_recomputed",
    "ledger_recomputed", "marker_operator_types_exact",
    "packet_recursive_schema_exact", "portable_source_exact",
    "route_raw_only", "selection_raw_only", "selection_recomputed",
    "source_periodic_rows_recomputed", "theorem_failure_count_zero",
    "writer_boundary_exact",
}
INDEPENDENT_CHECK_KEYS = {
    "all_raw_sections_hash_bound", "card_bindings_replayed",
    "duplicate_keys_rejected", "exact_scalars_only",
    "factor_permanence_by_contradiction_replayed",
    "finite_P0_stabilizer_replayed", "portable_paths_checked",
    "product_formula_CRT_replayed", "raw_packet_exact_set",
    "selector_state_parser_replayed", "sieve_prime_generation_replayed",
    "source_period_group_proof_replayed", "theorem_failure_count_zero",
}
ROUTE_MAIN_CHECK_KEYS = {
    "adversarial_stop", "artifact_base", "artifact_paths_safe",
    "branch_status", "candidate_skill_date", "chronology",
    "duplicate_token_absent", "full_normalized_payload_exact",
    "json_subset_yaml_canonical", "marker_repetition", "nested_exact",
    "overall", "provenance_state", "repair_scope", "route_b",
    "rung_evidence", "science_claim_scope", "science_hash_binding",
    "source_types", "target_data_absent", "terminal_mapping",
    "top_level_exact", "tuple",
}
ROUTE_INDEPENDENT_CHECK_KEYS = {
    "artifact_base_rebased", "artifact_paths_portable", "candidate_and_skill",
    "canonical_json_yaml_subset", "chronology_not_prospective",
    "determinant_orientation", "duplicate_boundary_external",
    "evidence_vector", "exact_nested_key_sets", "exact_top_key_set",
    "factor_scope", "fixed_counts", "full_normalized_payload_exact",
    "marker_firewall", "operator_scope", "overall_rejected",
    "paired_provenance_state", "repair_nonexhaustive", "route_b_locked",
    "route_tuple", "science_hash_bound", "target_data_absent",
    "terminal_mapping", "typed_source_factor_comparator",
}
MAIN_IMPLEMENTATION = {
    "algorithm": "C_constructive_CRT_source_first",
    "crt": "incremental_extended_euclidean_merge",
    "factor_proof": "epsilon_delta_then_adjacent_orbit_separation",
    "prime_generator": "trial_division",
    "project_local_imports": [],
}
INDEPENDENT_IMPLEMENTATION = {
    "algorithm": "F_factor_permanence_first",
    "crt": "simultaneous_product_formula",
    "factor_proof": "contradiction_via_fixed_anchor_orbit_separation",
    "prime_generator": "sieve",
    "project_local_imports": [],
}
RAW_CONSUMERS = ["algorithm_C", "algorithm_F"]
ROUTE_CONSUMERS = ["independent_route_auditor", "strict_route_validator"]
AUDITOR_CONSUMERS = ["read_only_integrity_auditor"]
THREE_ROUTE_STATE_CONSUMERS = [
    "independent_route_auditor", "read_only_integrity_auditor",
    "strict_route_validator",
]
MUTATION_PROFILE_OVERRIDES = {
    "artifact_path__absolute": ("raw_packet", RAW_CONSUMERS),
    "artifact_path__route_nonexistent_nested_output": (
        "route_card_in_output_tree", THREE_ROUTE_STATE_CONSUMERS),
    "artifact_path__route_wrong_base_output": (
        "route_card_in_output_tree", THREE_ROUTE_STATE_CONSUMERS),
    "check_flag__producer_pass": ("raw_packet", RAW_CONSUMERS),
    "factor_target__result_finite_fiber_restriction": (
        "canonical_output", AUDITOR_CONSUMERS),
    "factor_target__result_hidden_finite_radius": (
        "canonical_output", AUDITOR_CONSUMERS),
    "finite_p0_period__result_nonempty_period_one": (
        "canonical_output", AUDITOR_CONSUMERS),
    "finite_p0_period__result_proper_divisor": (
        "canonical_output", AUDITOR_CONSUMERS),
    "finite_p0_product__result_constant_one": (
        "canonical_output", AUDITOR_CONSUMERS),
    "fixed_anchor__result_anchor": ("canonical_output", AUDITOR_CONSUMERS),
    "fixed_counts__result_fixed_count_row": ("canonical_output", AUDITOR_CONSUMERS),
    "live_dependency__packet_queries_external_tree": (
        "canonical_output", AUDITOR_CONSUMERS),
    "live_dependency__queried": ("raw_packet", RAW_CONSUMERS),
    "marker__result_z_specialized_to_one": ("canonical_output", AUDITOR_CONSUMERS),
    "missing_residue__result_omitted_window_coordinate": (
        "canonical_output", AUDITOR_CONSUMERS),
    "operator_owner__result_c_of_y_owner": ("canonical_output", AUDITOR_CONSUMERS),
    "operator_owner__result_full_source_owner": ("canonical_output", AUDITOR_CONSUMERS),
    "operator_owner__result_hilbert_polya_owner": (
        "canonical_output", AUDITOR_CONSUMERS),
    "path_leak__host_path": ("raw_packet", RAW_CONSUMERS),
    "path_leak__serialized_host_value": ("canonical_output", AUDITOR_CONSUMERS),
    "provenance_state_a__authority_root_lock_missing": (
        "authority_overlay", AUDITOR_CONSUMERS),
    "provenance_state_a__authority_root_lock_tampered": (
        "authority_overlay", AUDITOR_CONSUMERS),
    "periodic_separation__result_period_row": ("canonical_output", AUDITOR_CONSUMERS),
    "prime_allocation__result_assignment_unsorted": (
        "canonical_output", AUDITOR_CONSUMERS),
    "provenance_state_a__manifest_present": (
        "paired_provenance_state", AUDITOR_CONSUMERS),
    "provenance_state_a__partial_code_commit": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_a__partial_source_commit": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_a__partial_source_lock_commit": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_b__nonhex_commit_triple": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_b__physical_manifest_missing": (
        "paired_provenance_state", AUDITOR_CONSUMERS),
    "provenance_state_b__route_claims_missing_manifest": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_b__stale_freeze_note": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_b__unequal_commit": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "provenance_state_b__zero_commit_triple": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "source_id__container_hash": ("raw_packet", RAW_CONSUMERS),
    "source_id__decoded_hash": ("raw_packet", RAW_CONSUMERS),
    "source_id__duplicate": ("raw_packet", RAW_CONSUMERS),
    "source_id__path_escape": ("raw_packet", RAW_CONSUMERS),
    "source_id__rename": ("raw_packet", RAW_CONSUMERS),
    "source_id__unsorted": ("raw_packet", RAW_CONSUMERS),
    "stage_2_scope__report_changed": ("paired_provenance_state", AUDITOR_CONSUMERS),
    "stage_2_scope__result_changed": ("paired_provenance_state", AUDITOR_CONSUMERS),
    "stage_2_scope__science_changed": (
        "paired_provenance_state", THREE_ROUTE_STATE_CONSUMERS),
    "stage_2_scope__static_code_changed": (
        "paired_provenance_state", AUDITOR_CONSUMERS),
    "stage_2_scope__authority_publication_partial_artifact": (
        "authority_overlay", AUDITOR_CONSUMERS),
    "stage_2_scope__authority_writer_unauthorized_change": (
        "authority_overlay", AUDITOR_CONSUMERS),
    "result_set__authority_writer_extra": (
        "authority_overlay", AUDITOR_CONSUMERS),
    "result_set__authority_writer_missing": (
        "authority_overlay", AUDITOR_CONSUMERS),
}
POSITIVE_CONTROL_CONTRACTS = {
    "cache__preflight_static_tree": (
        "cache", "static_tree_hygiene", ["static_hygiene_probe"],
        {"static_hygiene_probe": "PASS_ZERO_CACHE_FILES"}),
    "cwd_relocation__complete_tree_audit": (
        "cwd_relocation", "relocated_complete_output_tree",
        ["read_only_integrity_auditor"],
        {"read_only_integrity_auditor": "PASS_BYTE_IDENTICAL"}),
    "cwd_relocation__isolated_invocation_contract": (
        "cwd_relocation", "runtime_environment", ["process_isolation_probe"],
        {"process_isolation_probe": "PASS_ISOLATED_INVOCATION"}),
    "live_dependency__external_tree_not_queried": (
        "live_dependency", "portable_source_snapshot", ["portable_snapshot_probe"],
        {"portable_snapshot_probe": "PASS_NOT_QUERIED"}),
    "module_shadow__isolated_and_naive_controls": (
        "module_shadow", "runtime_environment", ["process_isolation_probe"],
        {"process_isolation_probe": "NAIVE_REJECTED_ISOLATED_PASSED"}),
    "path_leak__canonical_payload_scan": (
        "path_leak", "canonical_payload_hygiene", ["payload_hygiene_probe"],
        {"payload_hygiene_probe": "PASS_ZERO_HOST_TOKENS"}),
    "provenance_state_a__authority_overlay_baseline": (
        "provenance_state_a", "authority_overlay",
        ["read_only_integrity_auditor"],
        {"read_only_integrity_auditor": "PASS_AUTHORITY_BASELINE"}),
    "stage_2_scope__authority_publication_overlay": (
        "stage_2_scope", "authority_overlay",
        ["read_only_integrity_auditor"],
        {"read_only_integrity_auditor": "PASS_AUTHORITY_PUBLICATION_SYNC"}),
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def strict_json_equal(actual: Any, expected: Any) -> bool:
    """Compare JSON values without Python's bool/int/float equivalence.

    Python deliberately makes ``True == 1`` and ``1 == 1.0``.  Those
    equivalences are invalid for a typed evidence packet.  Keep this routine
    independent of the producer and recurse through every container.
    """
    if type(actual) is not type(expected):
        return False
    if type(actual) is dict:
        return set(actual) == set(expected) and all(
            strict_json_equal(actual[key], expected[key]) for key in actual)
    if type(actual) is list:
        return len(actual) == len(expected) and all(
            strict_json_equal(left, right)
            for left, right in zip(actual, expected))
    return actual == expected


def exact_json_bytes(actual: Any, raw: bytes, expected: Any) -> bool:
    """Require recursive type/value equality and the exact canonical bytes."""
    return strict_json_equal(actual, expected) and raw == canonical(expected)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> tuple[Any, bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if canonical(value) != raw:
        raise ValueError(f"noncanonical JSON: {path.relative_to(path.parents[2])}")
    return value, raw


def decode_container(path: Path, *, container_sha256: str,
                     decoded_sha256: str, role: str | None = None) -> bytes:
    value, raw = read_json(path)
    if digest(raw) != container_sha256 \
            or set(value) != {"decoded_sha256", "encoding", "payload", "role", "schema"} \
            or value["schema"] != "paper43-portable-byte-container-v1" \
            or value["encoding"] != "base64url_no_padding" \
            or value["decoded_sha256"] != decoded_sha256 \
            or role is not None and value["role"] != role \
            or type(value["payload"]) is not str \
            or BASE64URL.fullmatch(value["payload"]) is None \
            or "=" in value["payload"]:
        raise ValueError(f"portable container contract failure: {path.name}")
    padding = "=" * ((4 - len(value["payload"]) % 4) % 4)
    try:
        decoded = base64.urlsafe_b64decode(value["payload"] + padding)
    except Exception as exc:
        raise ValueError(f"portable container decode failure: {path.name}") from exc
    if digest(decoded) != decoded_sha256:
        raise ValueError(f"portable decoded hash failure: {path.name}")
    return decoded


def safe_path(value: str) -> bool:
    if type(value) is not str or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return not pure.is_absolute() and all(part not in {".", ".."} for part in pure.parts)


def instance_variant(class_id: str, identifier: str) -> str:
    prefix = class_id + "__"
    if not identifier.startswith(prefix) or len(identifier) == len(prefix):
        raise ValueError(f"mutation ID/class mismatch: {identifier} / {class_id}")
    return identifier[len(prefix):]


def expected_mutation_contract(row: dict[str, Any],
                               class_contract: dict[str, Any]) -> dict[str, Any]:
    identifier = row["id"]
    class_id = row["class_id"]
    if identifier in MUTATION_PROFILE_OVERRIDES:
        domain, consumers = MUTATION_PROFILE_OVERRIDES[identifier]
    else:
        default = class_contract["default_instance_contract"]
        domain = default["domain"]
        consumers = default["designated_consumers"]
    return {
        "class_id": class_id,
        "designated_consumers": sorted(consumers),
        "domain": domain,
        "expectation": "all_designated_consumers_reject_nonzero",
        "id": identifier,
        "variant": instance_variant(class_id, identifier),
    }


def expected_positive_contract(row: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    identifier = row["id"]
    if identifier not in POSITIVE_CONTROL_CONTRACTS:
        raise ValueError(f"unknown positive-control ID: {identifier}")
    class_id, domain, consumers, outcomes = POSITIVE_CONTROL_CONTRACTS[identifier]
    return ({
        "class_id": class_id,
        "designated_consumers": sorted(consumers),
        "domain": domain,
        "expectation": "exact_positive_control",
        "id": identifier,
        "variant": instance_variant(class_id, identifier),
    }, outcomes)


def parse_manifest(path: Path) -> list[tuple[str, str]]:
    raw = path.read_bytes()
    if b"\r" in raw or raw and not raw.endswith(b"\n"):
        raise ValueError(f"manifest line-ending failure: {path.name}")
    rows: list[tuple[str, str]] = []
    for line in raw.decode("ascii").splitlines():
        if len(line) < 67 or line[64:66] != "  " \
                or re.fullmatch(r"[0-9a-f]{64}", line[:64]) is None \
                or not safe_path(line[66:]):
            raise ValueError(f"manifest row failure: {path.name}")
        rows.append((line[:64], line[66:]))
    paths = [relative for _, relative in rows]
    if paths != sorted(paths) or len(paths) != len(set(paths)):
        raise ValueError(f"manifest order/uniqueness failure: {path.name}")
    return rows


def replay_manifest(base: Path, manifest: Path, *, exact_set: set[str] | None = None) -> int:
    rows = parse_manifest(manifest)
    if exact_set is not None and {relative for _, relative in rows} != exact_set:
        raise ValueError(f"manifest exact-set failure: {manifest.name}")
    for expected, relative in rows:
        path = base / relative
        if not path.is_file() or path.is_symlink() or digest(path.read_bytes()) != expected:
            raise ValueError(f"manifest hash failure: {relative}")
    return len(rows)


def static_file_set(root: Path, excluded_overlay_paths: set[str]) -> set[str]:
    output = set()
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root).as_posix()
        if relative == EXPECTED_STATIC_MANIFEST or relative == "PAPER_MANIFEST.sha256" \
                or relative == "EXPERIMENT_REPORT.md" \
                or relative.startswith(OUTPUT_ROOT_PREFIXES) \
                or relative in excluded_overlay_paths:
            continue
        output.add(relative)
    return output


def output_file_set(root: Path) -> set[str]:
    output = set()
    report = root / "EXPERIMENT_REPORT.md"
    if report.is_file():
        output.add("EXPERIMENT_REPORT.md")
    for prefix in OUTPUT_ROOT_PREFIXES:
        base = root / prefix[:-1]
        if base.exists():
            for path in base.rglob("*"):
                if path.is_file() or path.is_symlink():
                    output.add(path.relative_to(root).as_posix())
    return output


def imported_local_modules(path: Path) -> set[str]:
    local_names = {
        "source_core", "emit_packet", "lint_packet", "evaluate_packet",
        "independent_evaluator", "evaluate_route_a", "validate_route_a",
        "audit_route_a", "run_mutations", "run_integration", "audit_integrity",
    }
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    return imported & local_names


def expected_report_bytes(science: dict[str, Any], main: dict[str, Any],
                          independent: dict[str, Any], route_main: dict[str, Any],
                          route_independent: dict[str, Any],
                          adversarial: dict[str, Any], ledger_raw: bytes,
                          exact_output_count: int) -> bytes:
    """Independently render the only permitted report from canonical objects."""
    crt_rows = len(science["crt_proximality"]["control_rows"])
    finite_rows = len(science["finite_p0_sharpness"]["rows"])
    fixed_rows = len(science["periodic_ledger"]["fixed_count_rows"])
    terminal = science["terminal_codes"]
    lines = [
        "# Paper 43 exact integration report",
        "",
        "## Scope and chronology",
        "",
        "This is an independent executable replay of already-known mathematics. "
        "The selector, theorem, literature disposition, and witnesses were known before "
        "the final canonical run. The run is retrospective, nonblind, nonprospective, "
        "and supplies no novelty, priority, predecessor-ranking, or authorization credit.",
        "",
        "## Theorem replay",
        "",
        f"Algorithm C passed {main['checks_passed']}/{main['checks_total']} checks and "
        f"Algorithm F passed {independent['checks_passed']}/{independent['checks_total']} checks. "
        f"They emitted byte-identical science `{digest(canonical(science))}`. The replay checked "
        f"{crt_rows} exact CRT control rows, {finite_rows} finite-P0 rows, and {fixed_rows} "
        "fixed-count coefficients. The universal statements remain proof-schema replays, "
        "not inferences from the finite grid.",
        "",
        "The two implementations use trial-division plus incremental extended-Euclidean CRT "
        "versus a sieve plus simultaneous product-form CRT. Their factor-periodic arguments "
        "use epsilon--delta adjacent-orbit separation versus contradiction with a fixed-anchor "
        "orbit separation. Both preserve the arbitrary compact metrizable factor quantifier.",
        "",
        "The nonempty finite-P0 constructor and the separate empty-P0 two-fixed-point control "
        "both pass. The factor primitive ledger remains a singleton fixed orbit; temporal "
        "traversals are repetitions, not rational-prime primitive species. The one-dimensional "
        "owner `[1]` yields the inverse determinant `1-z` and owns neither the full source nor "
        "the rational-prime comparator.",
        "",
        "## Strict Route disposition",
        "",
        f"The strict Route tuple is `{science['route']['tuple']}` with overall verdict "
        f"`{science['route']['overall_verdict']}` and Route B allowed = "
        f"`{str(science['route']['route_b_invocation_allowed']).lower()}`. Main Route validation "
        f"passed {route_main['checks_passed']}/{route_main['checks_total']}; independent Route "
        f"audit passed {route_independent['checks_passed']}/{route_independent['checks_total']}.",
        "",
        "The exact four-field terminal mapping is:",
        "",
        f"- determinant_comparison: `{terminal['determinant_comparison']}`",
        f"- factor_cycle_creation: `{terminal['factor_cycle_creation']}`",
        f"- literature: `{terminal['literature']}`",
        f"- rational_prime_identification: `{terminal['rational_prime_identification']}`",
        "",
        "`STOP_DUPLICATE` remains a separate conditional literature/claim-boundary control and "
        "is not a strict Route terminal.",
        "",
        "## Adversarial, portability, and seal evidence",
        "",
        f"The frozen mutation registry contains {adversarial['classes_registered']} classes; "
        f"{adversarial['instance_count']} generated instances had "
        f"{adversarial['survivor_count']} survivors. Runs A, B, and relocated cold Run C are "
        "byte-identical for canonical packet, science, evaluator, and Route artifacts. A full "
        "parent rerun regenerates identical bytes, so its changed-path set is empty. State A "
        "and a disposable legal State B normalize to the same scientific Route payload; mixed "
        "states reject.",
        "",
        f"The exact canonical output namespace has {exact_output_count} paths. The self-excluding "
        f"result ledger has {len(ledger_raw.decode('ascii').splitlines())} entries and SHA-256 "
        f"`{digest(ledger_raw)}`.",
        "",
        "## Claim boundary",
        "",
        "Standalone novelty remains 1/10 and internal typed-closure value remains 2/10. "
        "No new proximality mechanism, universal aperiodic-factor theorem, rational-prime owner, "
        "or priority claim is made. If the same typed closure is found in a primary source, "
        "`STOP_DUPLICATE` closes the standalone route and assigns no novelty credit.",
    ]
    return ("\n".join(lines) + "\n").encode("ascii")


def text_overlay_clean(raw: bytes) -> bool:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return b"\r" not in raw and (not raw or raw.endswith(b"\n")) \
        and not any(token in raw for token in HOST_TOKENS) \
        and all(line == line.rstrip(" \t") for line in text.splitlines())


def verify_authority_overlay(root: Path, contract: dict[str, Any]) -> str:
    policy = contract.get("authority_overlay")
    expected_policy_keys = {
        "baseline_required_paths", "current_writer_manifest_path",
        "publication_artifact_paths", "publication_mutable_writer_paths",
        "root_lock_path", "root_lock_sha256", "root_lock_static_source",
        "states", "static_manifest_excluded_overlay_paths",
        "writer_baseline_manifest_path", "writer_content_paths",
        "writer_manifest_sha256",
    }
    if type(policy) is not dict or set(policy) != expected_policy_keys:
        raise ValueError("authority overlay policy shape")
    writer_paths = policy["writer_content_paths"]
    mutable_paths = policy["publication_mutable_writer_paths"]
    artifact_paths = policy["publication_artifact_paths"]
    excluded_paths = policy["static_manifest_excluded_overlay_paths"]
    required_paths = policy["baseline_required_paths"]
    for values in (writer_paths, mutable_paths, artifact_paths,
                   excluded_paths, required_paths):
        if type(values) is not list or values != sorted(values) \
                or len(values) != len(set(values)) \
                or any(not safe_path(value) for value in values):
            raise ValueError("authority overlay path policy")
    if set(mutable_paths) - set(writer_paths) \
            or set(writer_paths) | {
                policy["current_writer_manifest_path"], policy["root_lock_path"]
            } != set(required_paths) \
            or set(required_paths) | set(artifact_paths) != set(excluded_paths) \
            or policy["states"] != [
                "CANDIDATE_NO_OVERLAY", "AUTHORITY_BASELINE_RESULT_FREE",
                "AUTHORITY_PUBLICATION_SYNC",
            ]:
        raise ValueError("authority overlay ownership partition")
    present = {relative for relative in excluded_paths
               if (root / relative).exists()}
    if not present:
        return "CANDIDATE_NO_OVERLAY"
    if not set(required_paths).issubset(present):
        raise ValueError("partial authority baseline overlay")
    for relative in sorted(present):
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"authority overlay nonfile: {relative}")

    lock_source = root / policy["root_lock_static_source"]
    lock_target = root / policy["root_lock_path"]
    lock_value, lock_source_raw = read_json(lock_source)
    lock_target_value, lock_target_raw = read_json(lock_target)
    if digest(lock_source_raw) != policy["root_lock_sha256"] \
            or not exact_json_bytes(lock_target_value, lock_target_raw, lock_value) \
            or digest(lock_target_raw) != policy["root_lock_sha256"]:
        raise ValueError("authority root research lock mismatch")

    baseline_manifest = root / policy["writer_baseline_manifest_path"]
    pointer_manifest = root / "inputs/writer_pointer/SHA256SUMS.txt"
    current_manifest = root / policy["current_writer_manifest_path"]
    if digest(baseline_manifest.read_bytes()) != policy["writer_manifest_sha256"] \
            or baseline_manifest.read_bytes() != pointer_manifest.read_bytes():
        raise ValueError("archived writer baseline/pointer mismatch")
    baseline_root = baseline_manifest.parent
    replay_manifest(baseline_root, baseline_manifest,
                    exact_set=set(writer_paths))
    replay_manifest(root, current_manifest, exact_set=set(writer_paths))
    baseline_hashes = {relative: expected
                       for expected, relative in parse_manifest(baseline_manifest)}
    current_hashes = {relative: expected
                      for expected, relative in parse_manifest(current_manifest)}
    changed = {relative for relative in writer_paths
               if current_hashes[relative] != baseline_hashes[relative]}
    for relative in writer_paths:
        raw = (root / relative).read_bytes()
        if not text_overlay_clean(raw):
            raise ValueError(f"writer overlay text hygiene: {relative}")
        if relative not in changed \
                and raw != (baseline_root / relative).read_bytes():
            raise ValueError(f"writer baseline byte mismatch: {relative}")
    artifacts_present = present & set(artifact_paths)
    if not changed and not artifacts_present:
        if current_manifest.read_bytes() != baseline_manifest.read_bytes():
            raise ValueError("baseline writer manifest byte mismatch")
        return "AUTHORITY_BASELINE_RESULT_FREE"
    if changed != set(mutable_paths) or artifacts_present != set(artifact_paths):
        raise ValueError("unauthorized or partial publication overlay")
    section_raw = (root / "sections/6_sharpness_route.tex").read_bytes()
    try:
        normalized_section = " ".join(section_raw.decode("utf-8").split())
    except UnicodeDecodeError as exc:
        raise ValueError("publication overlay writer section encoding") from exc
    if contract["writer_sync"]["anchor_text"] not in normalized_section:
        raise ValueError("publication overlay lost writer insertion anchor")
    report_raw = (root / "COMPILATION_REPORT.md").read_bytes()
    pdf_raw = (root / "main.pdf").read_bytes()
    if not text_overlay_clean(report_raw) or b"main.pdf" not in report_raw \
            or len(pdf_raw) < 100 or not pdf_raw.startswith(b"%PDF-") \
            or b"%%EOF" not in pdf_raw \
            or any(token in pdf_raw for token in HOST_TOKENS):
        raise ValueError("publication artifact type/hygiene failure")
    return "AUTHORITY_PUBLICATION_SYNC"


def verify_static(root: Path, contract: dict[str, Any]) -> str:
    manifest_path = root / EXPECTED_STATIC_MANIFEST
    excluded_overlay_paths = set(
        contract["authority_overlay"]["static_manifest_excluded_overlay_paths"])
    expected = static_file_set(root, excluded_overlay_paths)
    replay_manifest(root, manifest_path, exact_set=expected)
    bindings = contract.get("post_smoke_integrity_bindings")
    binding_keys = {
        "chronology", "final_adversarial_instance_count",
        "final_adversarial_instance_contracts_sha256",
        "final_adversarial_instance_ids_sha256",
        "final_adversarial_payload_sha256", "normalized_route_sha256",
        "final_positive_control_count", "final_positive_control_ids_sha256",
        "preflight_adversarial_instance_count",
        "preflight_adversarial_instance_contracts_sha256",
        "preflight_adversarial_instance_ids_sha256",
        "preflight_adversarial_payload_sha256", "raw_packet_sha256",
        "preflight_positive_control_count", "preflight_positive_control_ids_sha256",
        "science_sha256",
    }
    if type(bindings) is not dict or set(bindings) != binding_keys \
            or bindings["chronology"] \
            != "RETROSPECTIVE_DIAGNOSTICS_AND_V5_OUTPUTS_KNOWN_BEFORE_V6_OVERLAY_SEAL" \
            or type(bindings["preflight_adversarial_instance_count"]) is not int \
            or type(bindings["final_adversarial_instance_count"]) is not int \
            or type(bindings["preflight_positive_control_count"]) is not int \
            or type(bindings["final_positive_control_count"]) is not int \
            or bindings["preflight_adversarial_instance_count"] <= 0 \
            or bindings["final_adversarial_instance_count"] <= 0 \
            or bindings["preflight_positive_control_count"] <= 0 \
            or bindings["final_positive_control_count"] <= 0 \
            or any(re.fullmatch(r"[0-9a-f]{64}", bindings[key]) is None
                   for key in binding_keys - {
                       "chronology", "preflight_adversarial_instance_count",
                       "final_adversarial_instance_count",
                       "preflight_positive_control_count",
                       "final_positive_control_count"}):
        raise ValueError("post-smoke retrospective binding contract failure")
    if digest((root / "preauthority/SHA256SUMS.txt").read_bytes()) \
            != contract["immutable_inputs"]["frozen_package_manifest_sha256"]:
        raise ValueError("frozen package manifest binding")
    if replay_manifest(root / "preauthority", root / "preauthority/SHA256SUMS.txt") != 16:
        raise ValueError("frozen package entry count")
    if digest((root / "independent_da/paper43_DA_REPORT.md").read_bytes()) \
            != contract["immutable_inputs"]["da_report_sha256"]:
        raise ValueError("DA report binding")
    if digest((root / "independent_da/paper43_DA_REPORT.sha256").read_bytes()) \
            != contract["immutable_inputs"]["da_sidecar_sha256"]:
        raise ValueError("DA sidecar binding")
    blueprint = root / "inputs/blueprint/paper43_experiment_blueprint.base64.json"
    decoded_blueprint = decode_container(
        blueprint,
        container_sha256=contract["immutable_inputs"]["blueprint_container_sha256"],
        decoded_sha256=contract["immutable_inputs"]["blueprint_sha256"],
        role="paper43_experiment_blueprint",
    )
    if not decoded_blueprint.startswith(b"# Paper 43 exact authority-integration experiment blueprint\n"):
        raise ValueError("blueprint decoded identity")
    writer_manifest = root / "inputs/writer_pointer/SHA256SUMS.txt"
    if digest(writer_manifest.read_bytes()) != contract["immutable_inputs"]["writer_manifest_sha256"]:
        raise ValueError("writer pointer manifest binding")
    writer_rows = parse_manifest(writer_manifest)
    if len(writer_rows) != 17:
        raise ValueError("writer pointer entry count")
    baseline_manifest = root / contract["authority_overlay"] \
        ["writer_baseline_manifest_path"]
    if baseline_manifest.read_bytes() != writer_manifest.read_bytes() \
            or digest(baseline_manifest.read_bytes()) \
            != contract["immutable_inputs"]["writer_manifest_sha256"] \
            or replay_manifest(baseline_manifest.parent, baseline_manifest,
                               exact_set={relative for _, relative in writer_rows}) != 17:
        raise ValueError("portable full writer baseline binding")
    anchor = root / contract["writer_sync"]["anchor_path"]
    baseline_anchor = root / contract["writer_sync"]["baseline_anchor_path"]
    anchor_rows = {relative: expected for expected, relative in writer_rows}
    if digest(anchor.read_bytes()) != anchor_rows["sections/6_sharpness_route.tex"] \
            or baseline_anchor.read_bytes() != anchor.read_bytes():
        raise ValueError("writer anchor binding")
    source_index, source_raw = read_json(root / "inputs/source_snapshot/SOURCE_INDEX.json")
    if digest(source_raw) != contract["immutable_inputs"]["source_index_sha256"] \
            or len(source_index["entries"]) != 40:
        raise ValueError("source index binding")
    if set(source_index) != {"entries", "expected_count", "schema",
                             "source_hash_manifest_sha256"} \
            or source_index["schema"] != "paper43-portable-source-container-index-v2" \
            or type(source_index["expected_count"]) is not int \
            or source_index["expected_count"] != 40:
        raise ValueError("source index schema")
    identifiers: list[str] = []
    paths: list[str] = []
    for row in source_index["entries"]:
        if set(row) != {"container_sha256", "decoded_sha256", "id",
                        "relative_container"} \
                or not safe_path(row["relative_container"]):
            raise ValueError("source snapshot entry shape")
        path = root / row["relative_container"]
        if path.is_symlink():
            raise ValueError("source snapshot symlink")
        decode_container(path,
                         container_sha256=row["container_sha256"],
                         decoded_sha256=row["decoded_sha256"],
                         role=row["id"])
        identifiers.append(row["id"])
        paths.append(row["relative_container"])
    if identifiers != sorted(identifiers) or len(identifiers) != len(set(identifiers)) \
            or len(paths) != len(set(paths)):
        raise ValueError("source snapshot order/uniqueness")
    registry_raw = (root / contract["mutation_registry"]["path"]).read_bytes()
    if digest(registry_raw) != contract["mutation_registry"]["sha256"]:
        raise ValueError("mutation registry binding")
    return verify_authority_overlay(root, contract)


def verify_state(root: Path, route: dict[str, Any], state: str,
                 contract: dict[str, Any]) -> None:
    triple = [route["source_commit"], route["code_commit"],
              route["source_lock"]["code_commit"]]
    authority = route["authority_integration"]
    manifest = root / "PAPER_MANIFEST.sha256"
    if state == "A":
        if triple != ["PENDING_FIRST_ARTIFACT_COMMIT"] * 3 \
                or not strict_json_equal(authority, {
                    "git_operations_by_integrator": 0,
                    "paper_manifest_present": False,
                    "state": "A",
                    "status": "STATE_A_FIRST_ARTIFACT_PENDING_TRIPLE",
                }) or route.get("freeze_note") \
                != contract["provenance_states"]["state_a"]["freeze_note"] \
                or manifest.exists():
            raise ValueError("illegal provenance State A")
    elif state == "B":
        if len(set(triple)) != 1 or re.fullmatch(r"[0-9a-f]{40}", triple[0]) is None \
                or triple[0] == "0" * 40 or not strict_json_equal(authority, {
                    "git_operations_by_integrator": 0,
                    "paper_manifest_present": True,
                    "state": "B",
                    "status": "STATE_B_METADATA_ONLY_SEAL",
                }) or route.get("freeze_note") != contract["provenance_states"]["state_b"] \
                ["freeze_note_template"].format(commit=triple[0]) \
                or not manifest.is_file():
            raise ValueError("illegal provenance State B")
        paper_rows = parse_manifest(manifest)
        if "PAPER_MANIFEST.sha256" in {path for _, path in paper_rows}:
            raise ValueError("paper manifest self-inclusion")
        actual = {path.relative_to(root).as_posix() for path in root.rglob("*")
                  if path.is_file() and not path.is_symlink()
                  and path.relative_to(root).as_posix() != "PAPER_MANIFEST.sha256"}
        if {path for _, path in paper_rows} != actual:
            raise ValueError("paper manifest exact-set failure")
        replay_manifest(root, manifest, exact_set=actual)
    else:
        raise ValueError("unknown provenance state")


def verify_outputs(root: Path, contract: dict[str, Any], state: str,
                   mutation_probe: bool) -> None:
    expected = set(contract["exact_output_paths"])
    actual = output_file_set(root)
    if actual != expected:
        raise ValueError(f"output exact-set failure missing={sorted(expected-actual)} extra={sorted(actual-expected)}")
    for relative in sorted(actual):
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError("output symlink/nonfile")
        raw = path.read_bytes()
        if any(token in raw for token in HOST_TOKENS):
            raise ValueError(f"host path leak: {relative}")
        if b"\r" in raw or raw and not raw.endswith(b"\n"):
            raise ValueError(f"output line-ending failure: {relative}")
    result_subset = {path for path in expected if path.startswith("results/")}
    ledger_set = result_subset - {"results/SHA256SUMS.txt"}
    ledger_path = root / "results/SHA256SUMS.txt"
    replay_manifest(root, ledger_path, exact_set=ledger_set)
    ledger_raw = ledger_path.read_bytes()
    expected_exact_result = {
        "count": len(result_subset),
        "paths": sorted(result_subset),
        "schema": "paper43-exact-result-set-v1",
        "status": "PASS",
    }
    exact_result, exact_result_raw = read_json(root / "results/exact_result_set.json")
    if not exact_json_bytes(exact_result, exact_result_raw, expected_exact_result):
        raise ValueError("exact-result-set certificate failure")
    science, science_raw = read_json(root / "results/scientific_results.json")
    packet, packet_raw = read_json(root / "results/source_packet.json")
    main, main_raw = read_json(root / "results/main_evaluation.json")
    independent, independent_raw = read_json(root / "results/independent_evaluation.json")
    route, route_raw = read_json(root / "evaluations/route_a/SD-C45/2026-08-17.yaml")
    route_main, route_main_raw = read_json(root / "results/route_evaluation.json")
    route_independent, route_independent_raw = read_json(
        root / "evaluations/route_a/SD-C45/independent_evaluation.json")
    if route.get("artifact_path_base") != contract["artifact_path_base"]:
        raise ValueError("Route artifact base mismatch")
    route_artifacts: list[str] = []

    def collect_route_artifacts(node: Any) -> None:
        if type(node) is dict:
            for key, value in node.items():
                if key in {"artifacts", "artifact_paths"} and type(value) is list:
                    route_artifacts.extend(value)
                collect_route_artifacts(value)
        elif type(node) is list:
            for value in node:
                collect_route_artifacts(value)

    collect_route_artifacts(route)
    if not route_artifacts or any(type(relative) is not str
                                  or not safe_path(relative)
                                  or not (root / relative).is_file()
                                  or (root / relative).is_symlink()
                                  for relative in route_artifacts):
        raise ValueError("Route artifact path resolution failure")
    expected_main = {
        "checks": {key: True for key in sorted(MAIN_CHECK_KEYS)},
        "checks_passed": len(MAIN_CHECK_KEYS),
        "checks_total": len(MAIN_CHECK_KEYS),
        "implementation": MAIN_IMPLEMENTATION,
        "schema": "paper43-main-evaluation-v1",
        "science": science,
        "science_sha256": digest(science_raw),
    }
    expected_independent = {
        "checks": {key: True for key in sorted(INDEPENDENT_CHECK_KEYS)},
        "checks_passed": len(INDEPENDENT_CHECK_KEYS),
        "checks_total": len(INDEPENDENT_CHECK_KEYS),
        "implementation": INDEPENDENT_IMPLEMENTATION,
        "schema": "paper43-independent-evaluation-v1",
        "science": science,
        "science_sha256": digest(science_raw),
    }
    if not exact_json_bytes(main, main_raw, expected_main) \
            or not exact_json_bytes(independent, independent_raw,
                                    expected_independent):
        raise ValueError("scientific evaluator exact-object mismatch")
    normalized_route = copy.deepcopy(route)
    normalized_route["source_commit"] = "NORMALIZED_PROVENANCE"
    normalized_route["code_commit"] = "NORMALIZED_PROVENANCE"
    normalized_route["freeze_note"] = "NORMALIZED_PROVENANCE"
    normalized_route["source_lock"]["code_commit"] = "NORMALIZED_PROVENANCE"
    normalized_route["authority_integration"] = {
        "git_operations_by_integrator": 0,
        "paper_manifest_present": False,
        "state": "NORMALIZED",
        "status": "NORMALIZED_PROVENANCE",
    }
    normalized_hash = digest(canonical(normalized_route))
    stage_a_route = copy.deepcopy(route)
    stage_a = contract["provenance_states"]["state_a"]
    stage_a_route["source_commit"] = stage_a["source_commit"]
    stage_a_route["code_commit"] = stage_a["code_commit"]
    stage_a_route["source_lock"]["code_commit"] = stage_a["source_lock_code_commit"]
    stage_a_route["freeze_note"] = stage_a["freeze_note"]
    stage_a_route["authority_integration"] = {
        "git_operations_by_integrator": 0,
        "paper_manifest_present": False,
        "state": "A",
        "status": "STATE_A_FIRST_ARTIFACT_PENDING_TRIPLE",
    }
    stage_a_route_hash = digest(canonical(stage_a_route))
    expected_route_main = {
        "checks": {key: True for key in sorted(ROUTE_MAIN_CHECK_KEYS)},
        "checks_passed": len(ROUTE_MAIN_CHECK_KEYS),
        "checks_total": len(ROUTE_MAIN_CHECK_KEYS),
        "normalized_route_sha256": normalized_hash,
        "route_sha256": stage_a_route_hash,
        "schema": "paper43-route-strict-validation-v1",
        "science_sha256": digest(science_raw),
        "state": "A",
        "status": "PASS",
    }
    expected_route_independent = {
        "checks": {key: True for key in sorted(ROUTE_INDEPENDENT_CHECK_KEYS)},
        "checks_passed": len(ROUTE_INDEPENDENT_CHECK_KEYS),
        "checks_total": len(ROUTE_INDEPENDENT_CHECK_KEYS),
        "normalized_route_sha256": normalized_hash,
        "route_sha256": stage_a_route_hash,
        "schema": "paper43-independent-route-audit-v1",
        "science_sha256": digest(science_raw),
        "state": "A",
        "status": "PASS",
    }
    if not exact_json_bytes(route_main, route_main_raw, expected_route_main) \
            or not exact_json_bytes(route_independent, route_independent_raw,
                                    expected_route_independent):
        raise ValueError("Route auditor exact-object mismatch")
    if packet["schema"] != "paper43-squarefree-factor-raw-packet-v1" \
            or science["schema"] != "paper43-squarefree-factor-science-projection-v1":
        raise ValueError("packet/science schema")
    source_index, source_index_raw = read_json(
        root / "inputs/source_snapshot/SOURCE_INDEX.json")
    portable = packet.get("portable_source_input")
    expected_portable = {
        "entries": source_index["entries"],
        "external_tree_status": "NOT_QUERIED",
        "source_count": 40,
    }
    if not strict_json_equal(portable, expected_portable):
        raise ValueError("packet portable source resolver mismatch")
    expected_cards = contract["selection"]["card_paths"]
    expected_card_hashes = contract["selection"]["card_sha256"]
    cards = packet.get("raw_selection_cards")
    if type(cards) is not list or len(cards) != 3:
        raise ValueError("packet selection-card set mismatch")
    for row in cards:
        candidate = row.get("candidate_id")
        if set(row) != {"bytes_base64", "candidate_id", "relative_container", "sha256"} \
                or candidate not in expected_cards \
                or row["relative_container"] != expected_cards[candidate] \
                or row["sha256"] != expected_card_hashes[candidate]:
            raise ValueError("packet selection-card resolver mismatch")
        try:
            decoded_card = base64.b64decode(row["bytes_base64"], validate=True)
        except Exception as exc:
            raise ValueError("packet selection-card decode failure") from exc
        if digest(decoded_card) != row["sha256"]:
            raise ValueError("packet selection-card decoded hash mismatch")

    def projection(relative: str, schema: str, payload: Any) -> None:
        value, raw = read_json(root / relative)
        expected_projection = {
            "payload": payload,
            "schema": schema,
            "status": "PASS",
        }
        if not exact_json_bytes(value, raw, expected_projection):
            raise ValueError(f"derived projection mismatch: {relative}")

    projection("results/source_topology_certificate.json",
               "paper43-source-topology-certificate-v1", science["source_topology"])
    projection("results/crt_proximality_certificate.json",
               "paper43-crt-proximality-certificate-v1", science["crt_proximality"])
    projection("results/factor_contract_certificate.json",
               "paper43-factor-contract-certificate-v1", {
                   "claim_scope": science["claim_scope"],
                   "factor_axioms": science["factor_periodic_rigidity"]["factor_axioms"],
                   "universal_aperiodic_factor_theorem_claimed": False,
               })
    projection("results/factor_periodic_rigidity_certificate.json",
               "paper43-factor-periodic-rigidity-certificate-v1",
               science["factor_periodic_rigidity"])
    projection("results/finite_p0_sharpness_certificate.json",
               "paper43-finite-p0-sharpness-certificate-v1",
               science["finite_p0_sharpness"])
    projection("results/source_periodic_collapse_certificate.json",
               "paper43-source-periodic-collapse-certificate-v1",
               science["source_periodic_collapse"])
    projection("results/periodic_ledger_certificate.json",
               "paper43-periodic-ledger-certificate-v1", science["periodic_ledger"])
    projection("results/operator_ownership_certificate.json",
               "paper43-operator-ownership-certificate-v1", {
                   "marker_ledger": science["marker_ledger"],
                   "operator_ledger": science["operator_ledger"],
                   "type_ledger": science["type_ledger"],
               })
    projection("results/type_contract_certificate.json",
               "paper43-type-contract-certificate-v1", {
                   "marker_ledger": science["marker_ledger"],
                   "type_ledger": science["type_ledger"],
               })
    projection("results/witness_certificate.json", "paper43-witness-certificate-v1",
               science["witness_ledger"])
    projection("results/selection_resolver.json", "paper43-selection-resolver-v1",
               science["selection"])
    projection("results/source_resolver.json", "paper43-source-resolver-v1", {
        "entries": source_index["entries"],
        "external_tree_status": "NOT_QUERIED",
        "matches": 40,
        "total": 40,
    })
    if imported_local_modules(root / "code/evaluator/evaluate_packet.py") \
            or imported_local_modules(root / "code/evaluator/independent_evaluator.py") \
            or (root / "code/evaluator/evaluate_packet.py").read_bytes() \
            == (root / "code/evaluator/independent_evaluator.py").read_bytes():
        raise ValueError("scientific evaluator import/source independence failure")
    projection("results/algorithm_independence.json",
               "paper43-algorithm-independence-v1", {
                   "algorithm_C": MAIN_IMPLEMENTATION,
                   "algorithm_F": INDEPENDENT_IMPLEMENTATION,
                   "canonical_science_byte_identical": True,
                   "project_local_import_edges": [],
                   "separate_processes": True,
               })
    projection("results/dependency_controls.json",
               "paper43-dependency-controls-v1", {
                   "bytecode_disabled": True,
                   "external_dependencies": [],
                   "hostile_pythonpath_ignored": True,
                   "isolated_python": True,
                   "live_external_tree": "NOT_QUERIED",
                   "network": "NOT_USED",
               })
    projection("results/source_evaluator_boundary.json",
               "paper43-source-evaluator-boundary-v1", {
                   "evaluator_reads": ["canonical_raw_packet"],
                   "packet_forbidden_derived_answers": True,
                   "producer_reads": ["sealed_static_inputs"],
                   "shared_project_helpers": [],
               })
    projection("results/external_provenance_stability.json",
               "paper43-external-provenance-stability-v1", {
                   "source_count": 40,
                   "source_index_sha256": digest(source_index_raw),
                   "status": "PORTABLE_SNAPSHOT_ONLY_LIVE_TREE_NOT_QUERIED",
               })
    static_manifest_sha256 = digest(
        (root / EXPECTED_STATIC_MANIFEST).read_bytes())
    projection("results/immutable_inputs.json", "paper43-immutable-inputs-v1", {
        "bindings": contract["immutable_inputs"],
        "mutation_registry_sha256": contract["mutation_registry"]["sha256"],
        "static_manifest_sha256": static_manifest_sha256,
    })
    projection("results/research_reproduction.json",
               "paper43-research-reproduction-v1", {
                   "chronology": science["integration_chronology"],
                   "claim_scope": science["claim_scope"],
                   "theorems": science["theorems"],
               })
    canonical_artifacts = sorted([
        "packet", "main", "independent", "science", "route", "route_main",
        "route_independent",
    ])
    projection("results/reproducibility_certificate.json",
               "paper43-reproducibility-certificate-v1", {
                   "canonical_artifacts_byte_identical": canonical_artifacts,
                   "run_labels_serialized_in_science": False,
                   "runs": ["A", "B", "C"],
               })
    projection("results/cold_copy_certificate.json",
               "paper43-cold-copy-certificate-v1", {
                   "cold_run_C_equals_run_A": True,
                   "external_tree_status": "NOT_QUERIED",
                   "host_paths_serialized": False,
                   "invocation_cwd": "UNRELATED_NONPROJECT_DIRECTORY",
                   "relocated_static_copy": True,
               })
    projection("results/idempotence_certificate.json",
               "paper43-idempotence-certificate-v1", {
                   "changed_paths_on_complete_parent_rerun": [],
                   "internal_complete_stage_builds_compared": 2,
                   "physical_writes_on_complete_second_parent_run": 0,
               })
    projection("results/sealed_state_compatibility.json",
               "paper43-sealed-state-compatibility-v1", {
                   "legal_states": ["A", "B"],
                   "mixed_states_rejected": True,
                   "normalized_scientific_route_byte_identical": True,
                   "state_b_changed_paths": contract["provenance_states"]["state_b"]
                                                    ["changed_paths"],
               })
    projection("results/integrity_contract.json",
               "paper43-integrity-contract-v1", {
                   "exact_output_paths": sorted(expected),
                   "paper_manifest_forbidden_in_state_a": True,
                   "result_ledger_self_excluding": True,
                   "static_manifest_sha256": static_manifest_sha256,
               })
    route_schema, route_schema_raw = read_json(
        root / "results/route_schema_certificate.json")
    expected_route_schema = {
        "payload": {
            "independent_audit": route_independent,
            "renderer_schema": "route-a-evaluator-v0.2.0",
            "strict_validation": route_main,
        },
        "schema": "paper43-route-schema-certificate-v1",
        "status": "PASS",
    }
    if not exact_json_bytes(route_schema, route_schema_raw,
                            expected_route_schema):
        raise ValueError("Route-schema certificate mismatch")
    adversarial, adversarial_raw = read_json(root / "results/adversarial_tests.json")
    registry, registry_raw = read_json(root / contract["mutation_registry"]["path"])
    if registry.get("schema") != "paper43-static-mutation-class-registry-v3" \
            or registry.get("class_count") != 62 \
            or registry.get("authority_overlay_coverage") != {
                "baseline_exact_writer_and_root_lock": True,
                "publication_artifacts_binary_text_classified": True,
                "publication_changed_paths_bounded": True,
                "unknown_extra_missing_and_unauthorized_reject": True,
                "writer_paths_excluded_from_integration_ledger": True,
            } \
            or registry.get("instance_contract_policy") != {
                "contract_fields": [
                    "class_id", "designated_consumers", "domain", "expectation",
                    "id", "variant",
                ],
                "mutation_outcome":
                    "REJECT_NONZERO_for_every_exact_designated_consumer",
                "observed_outcome_keys_equal_designated_consumers": True,
                "positive_controls_separate_from_rejection_records": True,
                "producer_emits_per_instance_contract": True,
                "read_only_auditor_rederives_each_contract": True,
            }:
        raise ValueError("mutation registry v3 policy mismatch")
    class_by_id = {row["class_id"]: row for row in registry["classes"]}
    registered = sorted(class_by_id)
    if len(registered) != 62 or len(registry["classes"]) != 62:
        raise ValueError("mutation registry class uniqueness/count mismatch")
    adversarial_keys = {
        "class_counts", "classes_exercised", "classes_missing",
        "classes_registered", "classes_unknown", "instance_contracts_sha256",
        "instance_count", "instance_ids_sha256", "mutation_registry_sha256",
        "phase", "positive_class_counts", "positive_control_count",
        "positive_control_failure_count", "positive_control_failure_ids",
        "positive_control_ids_sha256", "positive_controls", "records", "schema",
        "status", "survivor_count", "survivor_ids",
    }
    records = adversarial.get("records")
    positive_controls = adversarial.get("positive_controls")
    if set(adversarial) != adversarial_keys or type(records) is not list \
            or type(positive_controls) is not list:
        raise ValueError("adversarial result exact-key failure")
    record_ids: list[str] = []
    positive_ids: list[str] = []
    derived_counts = {class_id: 0 for class_id in registered}
    positive_counts = {class_id: 0 for class_id in registered}
    instance_contracts: list[dict[str, Any]] = []
    record_keys = {
        "class_id", "designated_consumers", "domain", "expectation", "id",
        "outcomes", "passed", "variant",
    }
    for row in records:
        if type(row) is not dict or set(row) != record_keys \
                or row.get("class_id") not in derived_counts \
                or type(row.get("id")) is not str or not row["id"] \
                or "deferred" in row["id"] or row.get("passed") is not True \
                or type(row.get("outcomes")) is not dict or not row["outcomes"]:
            raise ValueError("adversarial record semantics")
        expected_contract = expected_mutation_contract(
            row, class_by_id[row["class_id"]])
        actual_contract = {key: row[key] for key in (
            "class_id", "designated_consumers", "domain", "expectation", "id", "variant")}
        profile = {key: actual_contract[key] for key in (
            "designated_consumers", "domain", "expectation")}
        if not strict_json_equal(actual_contract, expected_contract) \
                or profile not in class_by_id[row["class_id"]]["allowed_instance_contracts"] \
                or sorted(row["outcomes"]) != row["designated_consumers"] \
                or set(row["outcomes"].values()) != {"REJECT_NONZERO"}:
            raise ValueError(f"adversarial per-instance contract mismatch: {row['id']}")
        record_ids.append(row["id"])
        derived_counts[row["class_id"]] += 1
        instance_contracts.append(actual_contract)
    for row in positive_controls:
        if type(row) is not dict or set(row) != record_keys \
                or row.get("class_id") not in positive_counts \
                or type(row.get("id")) is not str or not row["id"] \
                or row.get("passed") is not True or type(row.get("outcomes")) is not dict:
            raise ValueError("positive-control record semantics")
        expected_contract, expected_outcomes = expected_positive_contract(row)
        actual_contract = {key: row[key] for key in (
            "class_id", "designated_consumers", "domain", "expectation", "id", "variant")}
        profile = {key: actual_contract[key] for key in (
            "designated_consumers", "domain", "expectation")}
        if not strict_json_equal(actual_contract, expected_contract) \
                or not strict_json_equal(row["outcomes"], expected_outcomes) \
                or profile not in class_by_id[row["class_id"]]["allowed_instance_contracts"]:
            raise ValueError(f"positive-control contract mismatch: {row['id']}")
        positive_ids.append(row["id"])
        positive_counts[row["class_id"]] += 1
        instance_contracts.append(actual_contract)
    instance_contracts.sort(key=lambda row: row["id"])
    exercised = sorted(class_id for class_id in registered
                       if derived_counts[class_id] + positive_counts[class_id] > 0)
    missing = sorted(set(registered) - set(exercised))
    retrospective_binding = contract["post_smoke_integrity_bindings"]
    binding_prefix = "preflight" if mutation_probe else "final"
    expected_phase = "PREFLIGHT_BASELINE" if mutation_probe else "FINAL_LITERAL"
    expected_adversarial = {
        "class_counts": derived_counts,
        "classes_exercised": exercised,
        "classes_missing": missing,
        "classes_registered": len(registered),
        "classes_unknown": [],
        "instance_contracts_sha256": digest(canonical(instance_contracts)),
        "instance_count": len(records),
        "instance_ids_sha256": digest(canonical(record_ids)),
        "mutation_registry_sha256": digest(registry_raw),
        "phase": expected_phase,
        "positive_class_counts": positive_counts,
        "positive_control_count": len(positive_controls),
        "positive_control_failure_count": 0,
        "positive_control_failure_ids": [],
        "positive_control_ids_sha256": digest(canonical(positive_ids)),
        "positive_controls": positive_controls,
        "records": records,
        "schema": "paper43-adversarial-mutation-results-v2",
        "status": "PASS",
        "survivor_count": 0,
        "survivor_ids": [],
    }
    if record_ids != sorted(record_ids) or len(record_ids) != len(set(record_ids)) \
            or positive_ids != sorted(positive_ids) \
            or len(positive_ids) != len(set(positive_ids)) \
            or set(record_ids) & set(positive_ids) \
            or not exact_json_bytes(adversarial, adversarial_raw,
                                    expected_adversarial) \
            or (
                retrospective_binding.get("chronology")
                != "RETROSPECTIVE_DIAGNOSTICS_AND_V5_OUTPUTS_KNOWN_BEFORE_V6_OVERLAY_SEAL"
                or digest(packet_raw) != retrospective_binding.get("raw_packet_sha256")
                or digest(science_raw) != retrospective_binding.get("science_sha256")
                or normalized_hash
                != retrospective_binding.get("normalized_route_sha256")
                or len(records)
                != retrospective_binding.get(
                    f"{binding_prefix}_adversarial_instance_count")
                or adversarial["instance_ids_sha256"]
                != retrospective_binding.get(
                    f"{binding_prefix}_adversarial_instance_ids_sha256")
                or adversarial["instance_contracts_sha256"]
                != retrospective_binding.get(
                    f"{binding_prefix}_adversarial_instance_contracts_sha256")
                or adversarial["positive_control_count"]
                != retrospective_binding.get(
                    f"{binding_prefix}_positive_control_count")
                or adversarial["positive_control_ids_sha256"]
                != retrospective_binding.get(
                    f"{binding_prefix}_positive_control_ids_sha256")
                or digest(adversarial_raw)
                != retrospective_binding.get(
                    f"{binding_prefix}_adversarial_payload_sha256")):
        raise ValueError("adversarial result structure mismatch")
    summary, summary_raw = read_json(root / "results/analysis_summary.json")
    expected_summary = {
        "canonical_science_sha256": digest(science_raw),
        "crt_control_failures": 0,
        "crt_control_rows_checked": len(science["crt_proximality"]["control_rows"]),
        "exact_output_path_count": len(expected),
        "finite_p0_failures": 0,
        "finite_p0_rows_checked": len(science["finite_p0_sharpness"]["rows"]),
        "integration_chronology_status": science["integration_chronology"]["status"],
        "mutation_instances": adversarial["instance_count"],
        "mutation_survivors": adversarial["survivor_count"],
        "route_b_invocation_allowed": False,
        "route_tuple": science["route"]["tuple"],
        "schema": "paper43-analysis-summary-v1",
        "selection_survivors": science["selection"]["survivors"],
        "status": "PASS",
        "theorem_failures": science["theorems"]["failure_count"],
    }
    if not exact_json_bytes(summary, summary_raw, expected_summary):
        raise ValueError("analysis summary mismatch")
    exact_text, exact_text_raw = read_json(root / "results/exact_text_set.json")
    expected_text_paths = sorted(
        [relative for _, relative in parse_manifest(root / EXPECTED_STATIC_MANIFEST)]
        + [EXPECTED_STATIC_MANIFEST] + sorted(expected)
    )
    expected_exact_text = {
        "integrator_managed_paths": expected_text_paths,
        "schema": "paper43-exact-text-set-v1",
        "status": "PASS",
        "writer_owned_authority_paths_excluded": True,
    }
    if not exact_json_bytes(exact_text, exact_text_raw, expected_exact_text):
        raise ValueError("exact-text-set certificate mismatch")
    top_run_payloads = {
        "source_packet.json": packet_raw,
        "main_evaluation.json": main_raw,
        "independent_evaluation.json": independent_raw,
        "scientific_results.json": science_raw,
        "route_evaluation.json": route_main_raw,
    }
    for label in "ABC":
        for basename, expected_raw in top_run_payloads.items():
            if (root / f"results/runs/{label}/{basename}").read_bytes() != expected_raw:
                raise ValueError(f"A/B/C exact-byte mismatch: {label}/{basename}")
    if (root / "EXPERIMENT_REPORT.md").read_bytes() != expected_report_bytes(
            science, main, independent, route_main, route_independent,
            adversarial, ledger_raw, len(expected)):
        raise ValueError("experiment report renderer mismatch")
    certificate_raw = canonical(EXPECTED_INTEGRITY_CERTIFICATE)
    if (root / "results/integrity_audit.json").read_bytes() != certificate_raw:
        raise ValueError("integrity certificate payload drift")
    verify_state(root, route, state, contract)


def audit(root: Path, state: str, static_only: bool,
          mutation_probe: bool) -> dict[str, Any]:
    if root.is_symlink() or not root.is_dir():
        raise ValueError("root must be a real directory")
    for path in root.rglob("*"):
        if path.is_symlink() or path.name == "__pycache__" or path.suffix == ".pyc":
            raise ValueError("symlink/cache hygiene failure")
    contract, contract_raw = read_json(root / "code/contracts/INTEGRATION_CONTRACT.json")
    overlay_state = verify_static(root, contract)
    if static_only:
        return {
            "checks": {
                "authority_overlay_state_valid": True,
                "cache_and_symlink_hygiene": True,
                "da_binding_exact": True,
                "frozen_package_exact": True,
                "immutable_source_snapshot_exact": True,
                "integration_contract_exact": True,
                "static_input_manifest_exact": True,
                "writer_pointer_exact": True,
            },
            "checks_passed": 8,
            "checks_total": 8,
            "contract_sha256": digest(contract_raw),
            "authority_overlay_state": overlay_state,
            "schema": "paper43-static-integrity-audit-v1",
            "status": "PASS",
        }
    verify_outputs(root, contract, state, mutation_probe)
    return EXPECTED_INTEGRITY_CERTIFICATE


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("audit_integrity.py requires python3 -I -B")
    if not argv or len(argv) > 5:
        raise SystemExit(
            "usage: audit_integrity.py ROOT [--state A|B] [--static-only] [--mutation-probe]")
    root = Path(argv[0]).resolve()
    state = "A"
    static_only = False
    mutation_probe = False
    index = 1
    while index < len(argv):
        if argv[index] == "--static-only":
            static_only = True
            index += 1
        elif argv[index] == "--mutation-probe":
            mutation_probe = True
            index += 1
        elif argv[index] == "--state" and index + 1 < len(argv):
            state = argv[index + 1]
            index += 2
        else:
            raise SystemExit("invalid integrity-audit arguments")
    if mutation_probe and static_only:
        raise SystemExit("mutation-probe mode requires a full audit")
    result = audit(root, state, static_only, mutation_probe)
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
