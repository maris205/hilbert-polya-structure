#!/usr/bin/env python3
"""Raw-only packet construction for Paper 43.

This module belongs only to the producer.  Neither scientific evaluator is
allowed to import it or to read any project file other than the emitted raw
packet.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "code/contracts/INTEGRATION_CONTRACT.json"
SOURCE_INDEX_PATH = ROOT / "inputs/source_snapshot/SOURCE_INDEX.json"
HEX64 = re.compile(r"^[0-9a-f]{64}$")
BASE64URL = re.compile(r"^[A-Za-z0-9_-]*$")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=strict_object)
    if raw != canonical(value):
        raise ValueError(f"noncanonical JSON input: {path.name}")
    return value


def decode_container(path: Path, *, expected_container_sha256: str | None = None,
                     expected_decoded_sha256: str | None = None) -> bytes:
    """Decode one canonical, hash-bound portable byte container.

    The stored JSON is the portable artifact.  The decoded bytes retain the
    exact historical source record, including any host-specific provenance
    text that must not appear literally in the static integration tree.
    """
    raw = path.read_bytes()
    if expected_container_sha256 is not None \
            and sha256(raw) != expected_container_sha256:
        raise ValueError(f"container hash mismatch: {path.name}")
    value = json.loads(raw.decode("ascii"), object_pairs_hook=strict_object)
    if raw != canonical(value) or set(value) != {
            "decoded_sha256", "encoding", "payload", "role", "schema"}:
        raise ValueError(f"invalid portable container: {path.name}")
    if value["schema"] != "paper43-portable-byte-container-v1" \
            or value["encoding"] != "base64url_no_padding" \
            or type(value["role"]) is not str \
            or type(value["payload"]) is not str \
            or BASE64URL.fullmatch(value["payload"]) is None \
            or "=" in value["payload"]:
        raise ValueError(f"portable container schema failure: {path.name}")
    padding = "=" * ((4 - len(value["payload"]) % 4) % 4)
    try:
        decoded = base64.urlsafe_b64decode(value["payload"] + padding)
    except Exception as exc:
        raise ValueError(f"portable container decode failure: {path.name}") from exc
    decoded_sha256 = sha256(decoded)
    if not HEX64.fullmatch(value["decoded_sha256"]) \
            or decoded_sha256 != value["decoded_sha256"] \
            or expected_decoded_sha256 is not None \
            and decoded_sha256 != expected_decoded_sha256:
        raise ValueError(f"decoded byte hash mismatch: {path.name}")
    return decoded


def safe_relative(value: str) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return not pure.is_absolute() and ".." not in pure.parts and "." not in pure.parts


def check_hash(path: Path, expected: str) -> None:
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"missing or symlinked input: {path.name}")
    if not HEX64.fullmatch(expected) or sha256(path.read_bytes()) != expected:
        raise ValueError(f"input hash mismatch: {path.name}")


def replay_hash_manifest(root: Path, manifest: Path) -> int:
    rows = manifest.read_text(encoding="ascii").splitlines()
    parsed: list[tuple[str, str]] = []
    for row in rows:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", row)
        if not match or not safe_relative(match.group(2)):
            raise ValueError(f"invalid manifest row: {manifest.name}")
        parsed.append((match.group(1), match.group(2)))
    paths = [path for _, path in parsed]
    if paths != sorted(paths) or len(paths) != len(set(paths)):
        raise ValueError(f"unsorted or duplicate manifest: {manifest.name}")
    if manifest.name in paths:
        raise ValueError(f"self-including manifest: {manifest.name}")
    for expected, relative in parsed:
        check_hash(root / relative, expected)
    return len(parsed)


def validate_static_inputs(contract: dict[str, Any]) -> dict[str, Any]:
    immutable = contract["immutable_inputs"]
    blueprint_path = ROOT / "inputs/blueprint/paper43_experiment_blueprint.base64.json"
    decoded_blueprint = decode_container(
        blueprint_path,
        expected_container_sha256=immutable["blueprint_container_sha256"],
        expected_decoded_sha256=immutable["blueprint_sha256"],
    )
    if not decoded_blueprint.startswith(b"# Paper 43 exact authority-integration experiment blueprint\n"):
        raise ValueError("decoded blueprint identity mismatch")
    check_hash(ROOT / "preauthority/SHA256SUMS.txt",
               immutable["frozen_package_manifest_sha256"])
    check_hash(ROOT / "preauthority/RESEARCH_LOCK.json",
               immutable["frozen_research_lock_sha256"])
    check_hash(ROOT / "preauthority/ROUTE_EXPECTATION.yaml",
               immutable["frozen_route_expectation_sha256"])
    check_hash(ROOT / "preauthority/SOURCE_LOCK.md",
               immutable["frozen_source_lock_sha256"])
    check_hash(ROOT / "independent_da/paper43_DA_REPORT.md",
               immutable["da_report_sha256"])
    check_hash(ROOT / "independent_da/paper43_DA_REPORT.sha256",
               immutable["da_sidecar_sha256"])
    check_hash(ROOT / "inputs/writer_pointer/SHA256SUMS.txt",
               immutable["writer_manifest_sha256"])
    check_hash(ROOT / "code/contracts/ROUTE_A_V0_2_SCHEMA.json",
               immutable["route_schema_sha256"])
    check_hash(SOURCE_INDEX_PATH, immutable["source_index_sha256"])
    package_count = replay_hash_manifest(ROOT / "preauthority",
                                         ROOT / "preauthority/SHA256SUMS.txt")
    writer_manifest = (ROOT / "inputs/writer_pointer/SHA256SUMS.txt").read_text(
        encoding="ascii").splitlines()
    writer_paths: list[str] = []
    writer_hashes: dict[str, str] = {}
    for line in writer_manifest:
        if not line:
            continue
        if len(line) < 67 or line[64:66] != "  ":
            raise ValueError("writer pointer manifest row malformed")
        digest_value, relative = line[:64], line[66:]
        if not safe_relative(relative) or re.fullmatch(r"[0-9a-f]{64}", digest_value) is None:
            raise ValueError("writer pointer manifest row unsafe")
        writer_paths.append(relative)
        writer_hashes[relative] = digest_value
    if writer_paths != sorted(writer_paths) or len(writer_paths) != len(set(writer_paths)):
        raise ValueError("writer pointer manifest is not C-sorted and unique")
    if writer_hashes.get("sections/6_sharpness_route.tex") != sha256(
            (ROOT / "inputs/writer_pointer/sections/6_sharpness_route.tex").read_bytes()):
        raise ValueError("writer insertion anchor does not match writer manifest")
    writer_count = len(writer_paths)
    if package_count != 16 or writer_count != 17:
        raise ValueError("frozen manifest entry count mismatch")
    return {
        "frozen_package_entries": package_count,
        "source_index_entries": 40,
        "writer_entries": writer_count,
    }


def load_source_index(contract: dict[str, Any]) -> list[dict[str, str]]:
    index = load_json(SOURCE_INDEX_PATH)
    if set(index) != {"entries", "expected_count", "schema", "source_hash_manifest_sha256"}:
        raise ValueError("source index key set mismatch")
    entries = index["entries"]
    if type(index["expected_count"]) is not int or index["expected_count"] != 40:
        raise ValueError("source index count mismatch")
    if type(entries) is not list or len(entries) != 40:
        raise ValueError("source entry count mismatch")
    identifiers: list[str] = []
    paths: list[str] = []
    normalized: list[dict[str, str]] = []
    for entry in entries:
        if set(entry) != {"container_sha256", "decoded_sha256", "id",
                          "relative_container"}:
            raise ValueError("source entry key set mismatch")
        identifier = entry["id"]
        relative = entry["relative_container"]
        container_sha256 = entry["container_sha256"]
        decoded_sha256 = entry["decoded_sha256"]
        if not isinstance(identifier, str) or not safe_relative(relative):
            raise ValueError("unsafe source entry")
        decoded = decode_container(
            ROOT / relative,
            expected_container_sha256=container_sha256,
            expected_decoded_sha256=decoded_sha256,
        )
        container = load_json(ROOT / relative)
        if container["role"] != identifier or sha256(decoded) != decoded_sha256:
            raise ValueError("source role or decoded hash mismatch")
        identifiers.append(identifier)
        paths.append(relative)
        normalized.append({
            "container_sha256": container_sha256,
            "decoded_sha256": decoded_sha256,
            "id": identifier,
            "relative_container": relative,
        })
    if identifiers != sorted(identifiers) or len(identifiers) != len(set(identifiers)):
        raise ValueError("source identifiers are not sorted and unique")
    if len(paths) != len(set(paths)):
        raise ValueError("source snapshot paths are not unique")
    if len(normalized) != contract["source_snapshot"]["source_count"]:
        raise ValueError("contract source count mismatch")
    return normalized


def selection_cards(contract: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for candidate in contract["selection"]["commissioned_universe"]:
        relative = contract["selection"]["card_paths"][candidate]
        expected = contract["selection"]["card_sha256"][candidate]
        if not safe_relative(relative):
            raise ValueError("unsafe selection path")
        container = load_json(ROOT / relative)
        raw = decode_container(ROOT / relative,
                               expected_decoded_sha256=expected)
        if sha256(raw) != expected or container["role"].split("/")[-2] != candidate:
            raise ValueError("selection card hash mismatch")
        rows.append({
            "bytes_base64": base64.b64encode(raw).decode("ascii"),
            "candidate_id": candidate,
            "relative_container": relative,
            "sha256": expected,
        })
    return rows


def build_packet() -> dict[str, Any]:
    contract = load_json(CONTRACT_PATH)
    validate_static_inputs(contract)
    sources = load_source_index(contract)
    cards = selection_cards(contract)
    grid = contract["control_grid"]
    packet = {
        "candidate_contract": {
            "candidate_id": "SD-C45",
            "family": "symbolic_dynamics",
            "historical_parent": "SD-C02",
            "source_type": "SquarefreeAdmissiblePoint",
            "target_type": "TopologicalFactorState",
        },
        "claim_question": {
            "determinant_convention": "D_AM_Y(z)=zeta_AM_Y(z)^(-1)",
            "factor_quantifier": "every_continuous_surjective_fully_Z_equivariant_map_to_arbitrary_compact_metrizable_Z_system_with_homeomorphism",
            "question": "can_a_lawful_factor_create_any_periodic_point_other_than_pi_of_zero",
            "source": "all_rational_prime_square_admissible_two_sided_shift",
        },
        "control_grid": grid,
        "factor_axiom_schema": {
            "continuity": True,
            "equivariance_equation": "pi(sigma^n(x))=S^n(pi(x))_for_every_n_in_Z",
            "full_Z_equivariance": True,
            "surjective": True,
            "target_action": "homeomorphism",
            "target_space": "arbitrary_compact_metrizable_space",
        },
        "finite_p0_inputs": {
            "concrete_word": grid["concrete_modulus_four_word"],
            "prime_sets": grid["finite_p0_sets"],
            "product_rule": "Q=product_of_p_squared",
            "witness_rule": "x_n=1_iff_n_congruent_1_mod_Q",
        },
        "integration_chronology": contract["chronology"],
        "literature_boundary_contract": {
            "bounded_search_absence_is_novelty_proof": False,
            "conditional_action": "stop_standalone_route_and_assign_no_novelty_credit",
            "conditional_code": "STOP_DUPLICATE",
            "route_terminal": False,
            "trigger": "primary_source_with_same_squarefree_arbitrary_factor_periodic_ledger_theorem",
        },
        "marker_contract": {
            "comparator_marker": "u",
            "factor_marker": "z",
            "primitive_factor": "z",
            "repetition_rule": "r_fold_traversal_contributes_z_power_r",
            "specialize_u_to_z": False,
        },
        "operator_contract": {
            "determinant": "det(I-z[1])=1-z",
            "dimension": 1,
            "full_state_operator": False,
            "matrix": [[1]],
            "owner": "singleton_periodic_core",
            "trace_rule": "trace([1]^m)=1_for_every_m_at_least_1",
        },
        "portable_source_input": {
            "entries": sources,
            "external_tree_status": "NOT_QUERIED",
            "source_count": 40,
        },
        "raw_route_contract": {
            "artifact_path_base": contract["artifact_path_base"],
            "branch_vocabulary": [
                "CLOSE_SD_C02_TOPOLOGICAL_FACTOR_CYCLE_REPAIR"
            ],
            "evidence_status_vocabulary": [
                "MODELING_CHOICE", "NOT_TESTABLE", "PROVED", "STOP_SCOPED"
            ],
            "rung_names": ["a0", "a1", "a2", "a3", "a4"],
            "rung_status_vocabulary": [
                "A0_FAIL", "A1_FAIL", "A2_ANALYTIC_DETERMINANT",
                "A3_FAIL", "A4_FAIL"
            ],
            "route_b_same_object_completed_structure_required": True,
            "route_schema": "route-a-evaluator-v0.2.0",
            "state_a_pending_token": "PENDING_FIRST_ARTIFACT_COMMIT",
            "terminal_field_names": contract["terminal_contract"]["route_terminal_keys"],
            "terminal_token_vocabulary": sorted(contract["route_contract"]["terminal_codes"].values()),
        },
        "raw_selection_cards": cards,
        "schema": contract["packet_schema"]["schema"],
        "selection_adapter_contract": {
            "clauses": contract["selection"]["literal_clauses"],
            "commissioned_universe": contract["selection"]["commissioned_universe"],
            "rule_chronology": "retrospective_after_all_card_outcomes_literature_and_proof",
        },
        "source_axiom_schema": {
            "admissibility": "support_mod_p_squared_is_not_all_residues_for_every_rational_prime_p",
            "alphabet": [0, 1],
            "dynamics": "two_sided_left_shift_sigma_x_j_equals_x_j_plus_1",
            "prime_quantifier": "all_rational_primes",
            "space": "subset_of_binary_sequences_indexed_by_Z",
        },
        "source_fixture_inputs": {
            "ordered_pairs": grid["ordered_source_pairs"],
            "supports": grid["source_fixture_supports"],
            "windows": grid["windows"],
        },
        "terminal_contract": {
            "external_control": contract["terminal_contract"]["external_literature_control"],
            "external_control_is_route_terminal": False,
            "route_field_names": contract["terminal_contract"]["route_terminal_keys"],
            "route_token_vocabulary": sorted(contract["route_contract"]["terminal_codes"].values()),
        },
        "type_ledger": {
            "comparator": "RationalPrimeAtom",
            "factor_map": "ContinuousOntoZFactorMap",
            "factor_state": "TopologicalFactorState",
            "operator": "FiniteRankLedgerOperator",
            "primitive": "PeriodicOrbit(Y,S)",
            "source_point": "SquarefreeAdmissiblePoint",
        },
        "writer_sync_contract": {
            "allowed_field_names": contract["writer_sync"]["allowed_field_names"],
            "anchor_path": contract["writer_sync"]["anchor_path"],
            "anchor_sha256": sha256((ROOT / contract["writer_sync"]["anchor_path"]).read_bytes()),
            "result_values_allowed_before_final_clean": False,
        },
    }
    if sorted(packet) != contract["packet_schema"]["exact_top_level_keys"]:
        raise ValueError("raw packet top-level key set mismatch")
    return packet
