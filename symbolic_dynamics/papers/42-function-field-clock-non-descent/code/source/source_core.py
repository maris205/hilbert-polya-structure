#!/usr/bin/env python3
"""Build and authenticate the raw-only Paper 42 / SD-C44 source packet."""

from __future__ import annotations

import base64
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PACKAGE_MANIFEST_SHA256 = "f8f3ada901a3e26735819db05e3bcd01a26e571a8f9bd6cc4af8e1a2e705a433"
RESEARCH_LOCK_SHA256 = "fc4d3613165bebdd812789f0407329de983e1ec81020ef1024a665563293ffc2"
SOURCE_MANIFEST_SHA256 = "4d06a1149ad0288bee9fe84e7ac1d16a2fcfa9ca2ce8a9130e0bdc37fee10ad1"
ROUTE_EXPECTATION_SHA256 = "79eafee424590e0e1b65ffa7dc48d2a066a4822513ff1520f6bcf35593c6f71c"
DA_REPORT_SHA256 = "e46ecdab5aec15a3aa3dd5b80277e62f32677cd5162d803100a565b812bb265d"
DA_SIDECAR_SHA256 = "1f691de1d3fd87c096fe95e65bd42b30b0664ac7bc24e8a5f37dfbcfb2c34585"
WRITER_MANIFEST_SHA256 = "d930e78b2ce4ccb2bf84d88708f60c3b21227e8764d0c33fda66ad55d561e471"
WRITER_SNAPSHOT_SHA256 = "39245d8515161da277c99d931df705e9f6eaf7cacd6528a09fb2317eb87c994c"
BLUEPRINT_SHA256 = "403faba95ca79ccb98409451dc84e6974463b7d453911fe8fd4c90f286e8fd28"
ROUTE_SCHEMA_SHA256 = "41fc1b22773d2298f7ecbd9ca4eec6d65088ccd66a4919ad21c3ca5ab080dcc6"
ROUTE_SKILL_DECODED_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
GOVERNANCE_LOCK_SHA256 = "19fd82ebecf5f203bcc39d198f771e100c7b7ed52a4fdd8760bc20f972c0b976"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def file_digest(relative: str) -> str:
    return digest((ROOT / relative).read_bytes())


def safe_relative(value: Any) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in ("", ".", "..") for part in path.parts)


def parse_hash_manifest(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in path.read_text(encoding="ascii").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None or not safe_relative(match.group(2)):
            raise RuntimeError(f"invalid manifest row in {path.name}")
        rows.append((match.group(1), match.group(2)))
    names = [name for _, name in rows]
    if names != sorted(names) or len(names) != len(set(names)):
        raise RuntimeError(f"manifest not C-sorted and unique: {path.name}")
    return rows


def verify_manifest(path: Path, base: Path, expected_count: int) -> list[tuple[str, str]]:
    rows = parse_hash_manifest(path)
    if len(rows) != expected_count:
        raise RuntimeError(f"manifest count differs: {path.name}")
    for expected, relative in rows:
        target = base / relative
        if not target.is_file() or target.is_symlink() or digest(target.read_bytes()) != expected:
            raise RuntimeError(f"manifest hash differs: {relative}")
    return rows


def load_json(relative: str, *, require_canonical: bool = True) -> dict[str, Any]:
    raw = (ROOT / relative).read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict) or (require_canonical and canonical(value) != raw):
        raise RuntimeError(f"noncanonical JSON: {relative}")
    return value


def verify_immutable_inputs() -> dict[str, Any]:
    if file_digest("RESEARCH_LOCK.json") != GOVERNANCE_LOCK_SHA256:
        raise RuntimeError("integration governance lock seal differs")
    if file_digest("preauthority/SHA256SUMS.txt") != PACKAGE_MANIFEST_SHA256:
        raise RuntimeError("package manifest seal differs")
    package_rows = verify_manifest(ROOT / "preauthority/SHA256SUMS.txt", ROOT / "preauthority", 16)
    actual_package = sorted(path.name for path in (ROOT / "preauthority").iterdir() if path.is_file())
    expected_package = sorted([name for _, name in package_rows] + ["SHA256SUMS.txt"])
    if actual_package != expected_package:
        raise RuntimeError("package exact set differs")
    if file_digest("preauthority/RESEARCH_LOCK.json") != RESEARCH_LOCK_SHA256:
        raise RuntimeError("research lock seal differs")
    research = load_json("preauthority/RESEARCH_LOCK.json", require_canonical=False)
    mapping = research.get("immutable_package_files")
    if not isinstance(mapping, dict) or list(mapping) != sorted(mapping) or len(mapping) != 15:
        raise RuntimeError("research lock mapping differs")
    for name, expected in mapping.items():
        if not isinstance(expected, str) or file_digest("preauthority/" + name) != expected:
            raise RuntimeError(f"research lock hash differs: {name}")
    if file_digest("preauthority/SOURCE_HASHES.sha256") != SOURCE_MANIFEST_SHA256:
        raise RuntimeError("source manifest seal differs")
    if file_digest("preauthority/ROUTE_EXPECTATION.yaml") != ROUTE_EXPECTATION_SHA256:
        raise RuntimeError("Route expectation seal differs")

    if file_digest("independent_da/paper42_DA_REPORT.md") != DA_REPORT_SHA256:
        raise RuntimeError("DA report seal differs")
    if file_digest("independent_da/paper42_DA_REPORT.sha256") != DA_SIDECAR_SHA256:
        raise RuntimeError("DA sidecar seal differs")
    sidecar = (ROOT / "independent_da/paper42_DA_REPORT.sha256").read_text(encoding="ascii")
    if sidecar != f"{DA_REPORT_SHA256}  paper42_DA_REPORT.md\n":
        raise RuntimeError("DA sidecar binding differs")
    da_actual = sorted(path.name for path in (ROOT / "independent_da").iterdir() if path.is_file())
    if da_actual != ["paper42_DA_REPORT.md", "paper42_DA_REPORT.sha256"]:
        raise RuntimeError("DA exact set differs")

    if file_digest("WRITER_SHA256SUMS.txt") != WRITER_MANIFEST_SHA256:
        raise RuntimeError("writer manifest seal differs")
    writer_rows = verify_manifest(ROOT / "WRITER_SHA256SUMS.txt", ROOT, 18)
    if any((ROOT / relative).exists() or (ROOT / relative).is_symlink()
           for relative in ("COMPILATION_REPORT.md", "main.pdf")):
        raise RuntimeError("canonical integration requires baseline writer state")
    snapshot_raw = (ROOT / "docs/inputs/WRITER_BASELINE_SNAPSHOT.json").read_bytes()
    if digest(snapshot_raw) != WRITER_SNAPSHOT_SHA256:
        raise RuntimeError("writer baseline snapshot seal differs")
    snapshot = json.loads(snapshot_raw)
    if type(snapshot) is not dict or canonical(snapshot) != snapshot_raw or set(snapshot) != {
        "baseline_manifest_sha256", "entries", "manifest_utf8_b64", "schema"
    }:
        raise RuntimeError("writer baseline snapshot structure differs")
    if snapshot["schema"] != "paper42-writer-baseline-snapshot-v1" \
            or snapshot["baseline_manifest_sha256"] != WRITER_MANIFEST_SHA256:
        raise RuntimeError("writer baseline snapshot provenance differs")
    archived_manifest = base64.b64decode(snapshot["manifest_utf8_b64"], validate=True)
    if archived_manifest != (ROOT / "WRITER_SHA256SUMS.txt").read_bytes():
        raise RuntimeError("writer baseline manifest archive differs")
    entries = snapshot["entries"]
    if type(entries) is not list or len(entries) != 18 \
            or [entry.get("path") for entry in entries] != [name for _, name in writer_rows]:
        raise RuntimeError("writer baseline snapshot exact set differs")
    for entry, (expected, relative) in zip(entries, writer_rows):
        if type(entry) is not dict or set(entry) != {"decoded_sha256", "path", "utf8_b64"} \
                or entry["decoded_sha256"] != expected or entry["path"] != relative \
                or digest(base64.b64decode(entry["utf8_b64"], validate=True)) != expected:
            raise RuntimeError(f"writer baseline snapshot entry differs: {relative}")
    if file_digest("experiments/EXPERIMENT_PLAN.md") != BLUEPRINT_SHA256:
        raise RuntimeError("experiment blueprint seal differs")
    return research


def verify_portable_inputs() -> tuple[dict[str, Any], list[dict[str, str]]]:
    lock = load_json("docs/DEPENDENCY_LOCK.json")
    if lock.get("schema") != "paper42-portable-dependency-lock-v1":
        raise RuntimeError("dependency lock schema differs")
    if lock.get("writer") != {
        "baseline_manifest_sha256": WRITER_MANIFEST_SHA256,
        "baseline_manifest_entry_count": 18,
        "baseline_snapshot_path": "docs/inputs/WRITER_BASELINE_SNAPSHOT.json",
        "baseline_snapshot_sha256": WRITER_SNAPSHOT_SHA256,
        "canonical_integration_mutates_writer_paths": False,
        "current_manifest_path": "WRITER_SHA256SUMS.txt",
        "post_output_writer_sync_is_separate_authorized_lane": True,
    }:
        raise RuntimeError("writer dependency boundary differs")
    if file_digest("code/contracts/ROUTE_A_V0_2_SCHEMA.json") != ROUTE_SCHEMA_SHA256:
        raise RuntimeError("Route schema bytes differ")
    encoded = (ROOT / "docs/inputs/route-a-evaluator-v0.2.0.md.b64").read_bytes()
    if digest(base64.b64decode(encoded)) != ROUTE_SKILL_DECODED_SHA256:
        raise RuntimeError("Route skill decoded bytes differ")

    source_rows = parse_hash_manifest(ROOT / "preauthority/SOURCE_HASHES.sha256")
    expected_by_id = {source_id: expected for expected, source_id in source_rows}
    rows = lock.get("snapshot", {}).get("rows")
    if not isinstance(rows, list) or len(rows) != 29:
        raise RuntimeError("snapshot row count differs")
    ids = [row.get("source_id") for row in rows if isinstance(row, dict)]
    if ids != sorted(ids) or len(ids) != len(set(ids)) or set(ids) != set(expected_by_id):
        raise RuntimeError("snapshot source-ID exact set differs")
    public_rows: list[dict[str, str]] = []
    for row in rows:
        if set(row) != {"container_path", "decoded_sha256", "encoded_sha256", "kind", "source_id"}:
            raise RuntimeError("snapshot row key set differs")
        source_id = row["source_id"]
        container = row["container_path"]
        if not safe_relative(container) or not container.startswith("docs/inputs/source_snapshot/"):
            raise RuntimeError("unsafe snapshot path")
        path = ROOT / container
        if not path.is_file() or path.is_symlink():
            raise RuntimeError("snapshot container missing")
        encoded_raw = path.read_bytes()
        if digest(encoded_raw) != row["encoded_sha256"]:
            raise RuntimeError("snapshot encoded hash differs")
        try:
            decoded = base64.b64decode(encoded_raw, validate=False)
        except Exception as exc:
            raise RuntimeError("invalid snapshot base64") from exc
        if digest(decoded) != expected_by_id[source_id] or row["decoded_sha256"] != expected_by_id[source_id]:
            raise RuntimeError("snapshot decoded hash differs")
        expected_kind = "repo" if source_id.startswith("repo:") else "dependency"
        if row["kind"] != expected_kind:
            raise RuntimeError("snapshot type differs")
        public_rows.append({
            "container_path": container,
            "decoded_sha256": row["decoded_sha256"],
            "encoded_sha256": row["encoded_sha256"],
            "kind": row["kind"],
            "source_id": source_id,
        })
    if lock["snapshot"].get("external_historical_tree_query") != "NOT_QUERIED":
        raise RuntimeError("external tree state differs")
    return lock, public_rows


def build_packet() -> dict[str, Any]:
    verify_immutable_inputs()
    dependency_lock, source_rows = verify_portable_inputs()
    selection_raw = (ROOT / "docs/inputs/SESSION4_SELECTION_PACKET.json").read_bytes()
    selection = json.loads(selection_raw)
    if canonical(selection) != selection_raw:
        raise RuntimeError("selection packet is not canonical")
    card_yaml_rows: list[dict[str, str]] = []
    card_by_source = {card["source_id"]: card for card in selection["cards"]}
    for row in source_rows:
        if row["source_id"] not in card_by_source:
            continue
        encoded_card = (ROOT / row["container_path"]).read_text(encoding="ascii").strip()
        card_yaml_rows.append({
            "candidate_id": card_by_source[row["source_id"]]["candidate_id"],
            "historical_byte_sha256": row["decoded_sha256"],
            "source_id": row["source_id"],
            "yaml_utf8_b64": encoded_card
        })
    card_yaml_rows.sort(key=lambda row: row["candidate_id"])
    if len(card_yaml_rows) != 6:
        raise RuntimeError("historical card snapshot exact set differs")
    chronology = {
        "authority_run_had_not_occurred_at_static_freeze": True,
        "blind": False,
        "cards_science_witnesses_da_known_before_blueprint": True,
        "final_blueprint_bytes_frozen_after_disposable_smoke": True,
        "final_writer_bytes_frozen_after_disposable_smoke": True,
        "fully_prospective": False,
        "initial_blueprint_design_predated_implementation": True,
        "known_corrections": [
            "p41_transaction_architecture_adapted_after_p41_outputs_known",
            "paper42_disposable_scratch_smoke_outputs_known_before_static_seal",
            "stale_p41_mutation_harness_replaced_after_disposable_scratch_smoke",
            "route_paired_state_exact_rejection_class_repaired_after_disposable_scratch_smoke",
            "auditor_canonical_json_order_and_critical_result_semantic_closure_repaired_after_disposable_scratch_smoke",
            "first_transactional_stage_smoke_failed_before_mutation_completion",
            "nested_evaluations_snapshot_static_clone_exclusion_gap_repaired_after_disposable_scratch_smoke",
            "final_writer_numbered_reference_portability_and_chronology_reseal_d930_ingested_before_final_static_seal",
            "blueprint_rebound_to_final_writer_d930_before_final_static_seal",
            "final_blueprint_writer_timing_overclaim_repaired_after_p39_static_hold_and_interrupted_disposable_replay",
            "host_temporary_path_vocabulary_and_boundary_scanner_gap_repaired_before_replacement_static_seal",
            "post_materialization_chronology_present_tense_gap_repaired_before_replacement_static_seal",
            "writer_baseline_provenance_and_post_output_sync_lane_gap_repaired_before_replacement_static_seal",
            "whole_tree_exact_set_and_packet_registry_partition_gaps_repaired_before_replacement_static_seal",
            "evaluator_check_set_and_hostile_parent_evidence_gaps_repaired_before_replacement_static_seal",
            "authority_governance_lock_and_fresh_input_map_gate_added_before_replacement_static_seal",
            "packet_semantic_reanchor_lane_gap_repaired_before_final_replacement_static_seal",
            "static_mutation_actual_auditor_envelope_gap_repaired_before_final_replacement_static_seal",
            "coordinated_run_route_projection_closure_gap_repaired_before_final_replacement_static_seal",
            "unsafe_path_pre_io_containment_gap_repaired_before_final_replacement_static_seal",
            "cli_argument_contract_gap_repaired_before_final_replacement_static_seal",
            "terminal_contract_block_anchor_gap_repaired_before_final_replacement_static_seal",
            "json_container_and_nested_duplicate_mutation_gap_repaired_before_final_replacement_static_seal",
            "expected_output_rename_and_symlink_replacement_gap_repaired_before_final_replacement_static_seal",
            "external_frozen_auditor_exception_totality_gap_repaired_before_final_replacement_static_seal",
            "route_artifact_precanonical_path_classification_gap_repaired_before_final_replacement_static_seal",
            "semantic_fixture_hash_collision_reuse_gap_repaired_after_full_mutation_replay",
            "route_raw_order_and_artifact_structure_exact_rejection_envelope_gaps_repaired_after_full_mutation_replay"
        ],
        "novelty_credit": False,
        "outcome_independent": False,
        "paper39_ranking_or_authorization_used": False,
        "paper40_ranking_or_authorization_used": False,
        "paper41_ranking_or_authorization_used": False,
        "preregistered": False,
        "priority_credit": False,
        "prospective": False,
        "results_unseen": False,
        "static_candidate_frozen_after_disposable_smoke": True,
        "status": "RETROSPECTIVE_STATIC_SEAL_FROZEN_BEFORE_AUTHORITY_MATERIALIZATION"
    }
    packet = {
        "candidate_id": "SD-C44",
        "claim_boundary": "Exact non-descent only for the frozen full-q-shift primitive factors, finite-field degree clock, source-symbol marker, ordinary word powers, multiplicity, and weighted-adjacency determinant; no universal no-go for changed markers, induced systems, countable or infinite-memory models, or all function-field/number-field correspondences.",
        "control_grid": {
            "field_sizes": [2, 3, 5],
            "fixed_point_periods": {"maximum": 3, "minimum": 1},
            "irreducible_polynomial_degrees": {"maximum": 4, "minimum": 1},
            "word_lengths": {"maximum": 6, "minimum": 1}
        },
        "integration_chronology": chronology,
        "marker_contract": {
            "comparison_mode": "formal_monomials_in_free_z_before_any_specialization",
            "source_marker": "z^n_for_length_n_primitive_necklace",
            "source_unit": "one_original_full_shift_symbol",
            "specialization_z_equals_one_allowed_for_marker_credit": False,
            "target_marker": "z_for_one_rational_prime_loop_traversal"
        },
        "operator_contract": {
            "source_determinant_convention": "D_q(s,z)=det(I-L_q,s,z)=1-z*q^(1-s)",
            "source_hilbert_space": "C",
            "source_operator_action": "L_q,s,z*f=z*q^(1-s)*f",
            "source_owner": "full_q_shift_weighted_adjacency",
            "target_determinant_convention": "D_P(s,z)=det(I-z*Q_s)=product_p(1-z*p^(-s))",
            "target_domain": "Re(s)>1",
            "target_hilbert_space": "ell^2(rational_primes)",
            "target_operator_action": "Q_s*e_p=p^(-s)*e_p",
            "target_owner": "separate_rational_prime_diagonal_inventory"
        },
        "portable_source_input": {
            "dependency_lock_sha256": file_digest("docs/DEPENDENCY_LOCK.json"),
            "external_historical_tree_query": "NOT_QUERIED",
            "rows": source_rows,
            "source_manifest_sha256": SOURCE_MANIFEST_SHA256,
            "source_row_count": 29,
            "writer_baseline_manifest_sha256": WRITER_MANIFEST_SHA256,
            "writer_baseline_snapshot_sha256": WRITER_SNAPSHOT_SHA256
        },
        "positive_control_input": {
            "controls": [
                "function_field_prime_polynomial_degree_count",
                "single_length_one_factor_non_total_projection",
                "separate_target_diagonal_operator",
                "source_repetition_weight"
            ],
            "cross_type_bijection_claimed": False,
            "source_ledger_failure_premise": False
        },
        "raw_repair_rows": [
            {"id": "finite_field_norm_q_power_n", "operation": "label_each_length_n_source_primitive_by_q^n"},
            {"id": "keep_degree_one_necklaces", "operation": "project_to_all_length_one_source_primitives"},
            {"id": "choose_one_degree_one_necklace", "operation": "project_to_one_length_one_source_primitive"},
            {"id": "enumerate_necklaces_by_rational_primes", "operation": "externally_relabel_source_primitives_by_chosen_rational_primes"},
            {"id": "induce_every_primitive_orbit_to_one_return", "operation": "replace_source_symbol_marker_by_first_return_marker"},
            {"id": "finite_field_prime_polynomial_dictionary", "operation": "retype_degree_n_necklaces_as_finite_field_prime_polynomials"}
        ],
        "raw_selection_cards": {
            "card_yaml_rows": card_yaml_rows,
            "packet": selection,
            "packet_sha256": digest(selection_raw),
            "packet_utf8_b64": base64.b64encode(selection_raw).decode("ascii")
        },
        "schema": "paper42-exact-source-packet-v1",
        "source_object_input": {
            "alphabet_model": "F_q",
            "dynamics": "left_shift",
            "field_sizes": [2, 3, 5],
            "object": "two_sided_full_q_shift_F_q^Z",
            "orientation": "cyclic_rotations_identified_reversal_not_identified",
            "primitive_relation": "aperiodic_nonempty_word_modulo_cyclic_rotation",
            "repetition": "ordinary_word_power",
            "source_clock": "n*log(q)"
        },
        "target_object_input": {
            "factor_multiplicity": 1,
            "object": "positive_rational_prime_atoms",
            "primitive_relation": "p_maps_to_p^r_under_repetition",
            "support_type": "rational_prime",
            "target_clock": "log(p)"
        },
        "terminal_contract": {
            "branch_status": "CLOSE_SD_C01_SAME_CLOCK_SAME_MARKER_RATIONAL_PRIME_PROJECTION",
            "literature_boundary_external": "STOP_DUPLICATE",
            "route_terminals": [
                "STOP_FIRST_MARKED_COEFFICIENT_MISMATCH",
                "STOP_MARKER_MULTIPLICITY_CONJUNCTION",
                "STOP_Q_POWER_RATIONAL_PRIME_SUPPORT"
            ],
            "universal_no_go_claimed": False
        },
        "type_ledger": [
            {"marker": "z^n", "name": "ShiftPrimitiveNecklace_q", "not_owned": "rational_prime_diagonal_inventory", "owner": "full_q_shift"},
            {"marker": "degree_marker", "name": "FiniteFieldPrimePolynomial_q", "not_owned": "canonical_objectwise_necklace_bijection", "owner": "affine_line_function_field_zeta"},
            {"marker": "z", "name": "RationalPrimeAtom", "not_owned": "full_q_shift_weighted_adjacency", "owner": "separate_rational_prime_diagonal_inventory"}
        ],
        "witness_input": {
            "clock_support_word": [0, 1],
            "clock_support_word_text": "01",
            "factor_obligations": [
                "totality",
                "rational_prime_support",
                "exact_clock",
                "original_marker",
                "multiplicity_one",
                "temporal_repetition",
                "source_operator_ownership"
            ],
            "marker_variable": "z",
            "requested_analytic_comparison": "first_z_coefficient_on_Re(s)>1",
            "requested_multiplicity_layer": 1
        }
    }
    return packet


def packet_bytes() -> bytes:
    return canonical(build_packet())
