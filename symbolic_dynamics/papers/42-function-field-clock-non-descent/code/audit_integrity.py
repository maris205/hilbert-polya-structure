#!/usr/bin/env python3
"""Independent read-only exact-set and semantic integrity audit for Paper 42."""

from __future__ import annotations

import ast
import base64
import copy
import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any

import yaml


PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ZERO = "0" * 40
DUMMY = "0123456789abcdef0123456789abcdef01234567"
ROUTE_REL = "evaluations/route_a/SD-C44/2026-08-17.yaml"
LEDGER_REL = "results/SHA256SUMS.txt"
MANIFEST_REL = "PAPER_MANIFEST.sha256"
EXPECTED_PACKET_SHA256 = "47a66b4d75cae55b3fc3fcd8f57174d7f69ebc91c37e052fd22ba9f1cb31e6c9"
EXPECTED_SCIENCE_SHA256 = "078d98da2f3c89c0f5f4e7ef6be84066ee60a1c1d82c86788de675ad349b7848"
EXPECTED_REPORT_SHA256 = "0772ec227307add3728beadda909ac17576b1ae05886e1f0dfcf0f11c137a365"
EXPECTED_BOUNDARY_SHA256 = "ec7791c92ea98e50703ac68505586b7c8b8301308abf0c3864f3aa045b72e2c0"
EXPECTED_NORMALIZED_ROUTE_SHA256 = "02881794a6d550974cb71c1d5c3692175a577e5d46c679f36a345ad369463f06"
EXPECTED_STAGE1_ROUTE_RAW_SHA256 = "86f5458ce09c3a28f8d879187b1f159054b89044ffedebe58cba7a2b9ded61a8"
EXPECTED_DUMMY_ROUTE_RAW_SHA256 = "5bb40051460ffad7af8bf7edfe1551e5711dfa43b54c05b558401b748dd61954"
STAGE1_NOTE = (
    "State A authority artifact has source_commit, code_commit, and "
    "source_lock.code_commit equal to PENDING_FIRST_ARTIFACT_COMMIT and no "
    "PAPER_MANIFEST.sha256. State B is metadata-only: one identical lowercase "
    "nonzero 40-hex State-A commit replaces those three fields and a C-sorted "
    "self-excluding PAPER_MANIFEST.sha256 is added."
)
CHECK_NAMES = sorted([
    "algorithm_boundary", "chronology_exact", "code_exact_set",
    "critical_result_semantics_exact", "dependency_bytes", "evaluation_exact_set",
    "experiment_exact_set", "experiment_freeze", "governance_lock", "immutable_da", "immutable_package",
    "immutable_research_lock", "integration_hygiene", "integration_no_absolute_path_tokens",
    "integration_no_cache", "integration_no_symlink", "ledger_exact_set", "ledger_format",
    "ledger_hashes", "ledger_safe_paths", "ledger_self_excluded", "ledger_sorted_unique",
    "manifest_exact_set", "manifest_format", "manifest_hashes", "manifest_presence_pair",
    "manifest_safe_paths", "manifest_self_excluded", "manifest_sorted_unique",
    "owned_path_boundary", "paired_route_note", "paired_route_triple", "report_mutation_ledger_exact",
    "report_present", "result_declaration_exact", "result_exact_set", "route_artifact_base",
    "route_artifact_paths", "route_b_locked", "route_canonical_payload",
    "route_duplicate_safe_parse", "route_exact_tuple", "route_file_present", "route_raw_order",
    "route_raw_serialization", "route_science_hash", "route_terminal_set", "science_byte_equality_control",
    "snapshot_exact_set", "source_manifest_anchor", "text_declaration_exact", "text_exact_set",
    "whole_tree_exact_set", "writer_excluded", "writer_lane_boundary", "writer_manifest",
])


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def decode_locked_base64(raw: bytes) -> bytes:
    """Decode an already byte-hash-locked, optionally line-wrapped container."""
    return base64.b64decode(b"".join(raw.split()), validate=True)


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def pass_result() -> dict[str, Any]:
    return {"check_count": len(CHECK_NAMES), "checks": {name: True for name in CHECK_NAMES}, "schema": "paper42-read-only-integrity-audit-v1", "status": "PASS"}


def safe_path(value: Any) -> bool:
    if type(value) is not str or not value or "\\" in value or "\x00" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in ("", ".", "..") for part in path.parts)


def contained_regular_file(root: Path, value: Any) -> bool:
    """Lexically validate and lstat every component before any file read."""
    if not safe_path(value):
        return False
    current = root
    parts = PurePosixPath(value).parts
    for index, part in enumerate(parts):
        current = current / part
        try:
            mode = os.lstat(current).st_mode
        except OSError:
            return False
        if stat.S_ISLNK(mode):
            return False
        if index < len(parts) - 1 and not stat.S_ISDIR(mode):
            return False
        if index == len(parts) - 1 and not stat.S_ISREG(mode):
            return False
    try:
        return current.resolve().is_relative_to(root.resolve())
    except (OSError, RuntimeError):
        return False


def parse_hash_bytes(raw: bytes) -> tuple[list[tuple[str, str]], bool]:
    try:
        lines = raw.decode("ascii").splitlines()
    except Exception:
        return [], False
    rows: list[tuple[str, str]] = []
    valid = True
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None:
            valid = False
            continue
        rows.append((match.group(1), match.group(2)))
    return rows, valid


def parse_hash_file(path: Path) -> tuple[list[tuple[str, str]], bool]:
    try:
        return parse_hash_bytes(path.read_bytes())
    except Exception:
        return [], False


def unique_json(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def json_value(path: Path) -> Any:
    try:
        raw = path.read_bytes()
        value = json.loads(raw, object_pairs_hook=unique_json)
        if canonical(value) != raw:
            return None
        return value
    except Exception:
        return None


def yaml_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError("duplicate YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def sealed_note(commit: str) -> str:
    return (
        f"State A artifact commit {commit} contained the three "
        "PENDING_FIRST_ARTIFACT_COMMIT fields and no PAPER_MANIFEST.sha256. "
        "State B is metadata-only: source_commit, code_commit, and "
        "source_lock.code_commit are sealed to that same commit and the "
        "C-sorted self-excluding PAPER_MANIFEST.sha256 is added."
    )


def dump_route(value: dict[str, Any]) -> bytes:
    return yaml.dump(value, Dumper=yaml.SafeDumper, allow_unicode=False, default_flow_style=False, explicit_start=False, sort_keys=False, width=1000).encode("ascii")


def file_inventory(root: Path, top: str) -> list[str]:
    base = root / top
    if not base.is_dir() or base.is_symlink():
        return []
    return sorted(path.relative_to(root).as_posix() for path in base.rglob("*") if path.is_file() and not path.is_symlink())


def recursive_pointer_operations(value: Any, *, skip_route_provenance: bool = False) -> set[tuple[str, str]]:
    rows: set[tuple[str, str]] = set()
    skipped = {"/source_commit", "/code_commit", "/source_lock/code_commit", "/freeze_note"} \
        if skip_route_provenance else set()

    def esc(text: str) -> str:
        return text.replace("~", "~0").replace("/", "~1")

    def walk(current: Any, pointer: str) -> None:
        if type(current) is dict:
            rows.add((pointer or "/", "EXTRA_KEY"))
            for key, child in current.items():
                child_pointer = pointer + "/" + esc(key)
                if child_pointer not in skipped:
                    rows.add((child_pointer, "KEY_DELETION"))
                    walk(child, child_pointer)
        elif type(current) is list:
            if current:
                rows.add((pointer, "MEMBER_DELETION"))
                rows.add((pointer, "MEMBER_DUPLICATION"))
                if len(current) > 1 and current != list(reversed(current)):
                    rows.add((pointer, "ORDER_REVERSAL"))
            for index, child in enumerate(current):
                walk(child, f"{pointer}/{index}")
        elif pointer not in skipped:
            rows.add((pointer, "VALUE_DRIFT"))
            rows.add((pointer, "VALUE_AND_TYPE_DRIFT"))

    walk(value, "")
    return rows


def route_special_contract() -> set[tuple[str, str, str]]:
    operations = (
        ("RRAW0001", "/candidate_id", "DUPLICATE_TOP_KEY"),
        ("RRAW0002", "/", "RAW_WHITESPACE"),
        ("RRAW0003", "/", "RAW_KEY_ORDER_SWAP"),
        ("RPATH0001", "/source_lock/artifact_paths/0", "ARTIFACT_ABSOLUTE_PATH"),
        ("RPATH0002", "/a0/artifacts/0", "ARTIFACT_PARENT_ESCAPE"),
        ("RPATH0003", "/a1/artifacts/0", "ARTIFACT_SAFE_MISSING"),
        ("RPATH0004", "/a2/artifacts/0", "ARTIFACT_WRONG_BASE_EXISTING"),
        ("RPATH0005", "/a3/artifacts/0", "ARTIFACT_SYMLINK_COMPONENT"),
        ("RSTATE0001", "/source_commit", "STAGE_A_SOURCE_COMMIT_DRIFT"),
        ("RSTATE0002", "/code_commit", "STAGE_A_CODE_COMMIT_DRIFT"),
        ("RSTATE0003", "/source_lock/code_commit", "STAGE_A_SOURCE_LOCK_COMMIT_DRIFT"),
        ("RSTATE0004", "/freeze_note", "STAGE_A_FREEZE_NOTE_DRIFT"),
        ("RSTATE0005", "/source_commit", "STAGE_A_SOURCE_COMMIT_TYPE_DRIFT"),
        ("RSTATE0006", "/", "STAGE_A_MANIFEST_PRESENT"),
        ("RSTATE0007", "/", "STAGE_B_MANIFEST_ABSENT"),
        ("RSTATE0008", "/source_commit", "STAGE_B_SOURCE_COMMIT_DRIFT"),
        ("RSTATE0009", "/code_commit", "STAGE_B_CODE_COMMIT_DRIFT"),
        ("RSTATE0010", "/source_lock/code_commit", "STAGE_B_SOURCE_LOCK_COMMIT_DRIFT"),
        ("RSTATE0011", "/", "STAGE_B_ZERO_COMMIT_TRIPLE"),
        ("RSTATE0012", "/", "STAGE_B_NONHEX_COMMIT_TRIPLE"),
        ("RSTATE0013", "/", "STAGE_B_UPPERCASE_COMMIT_TRIPLE"),
        ("RSTATE0014", "/", "STAGE_B_WRONG_LENGTH_COMMIT_TRIPLE"),
        ("RSTATE0015", "/", "STAGE_B_PENDING_TRIPLE_WITH_MANIFEST"),
        ("RSTATE0016", "/freeze_note", "STAGE_B_STALE_FREEZE_NOTE"),
        ("RSTATE0017", "/freeze_note", "STAGE_B_FREEZE_NOTE_TYPE_DRIFT"),
        ("RSTATE0018", "/source_commit", "STAGE_B_SOURCE_COMMIT_DELETION"),
        ("RSTATE0019", "/code_commit", "STAGE_B_CODE_COMMIT_DELETION"),
        ("RSTATE0020", "/source_lock/code_commit", "STAGE_B_SOURCE_LOCK_COMMIT_DELETION"),
        ("RSTATE0021", "/freeze_note", "STAGE_B_FREEZE_NOTE_DELETION"),
        ("RSTATE0022", "/", "STAGE_B_WRONG_VALID_COMMIT_STALE_NOTE"),
        ("RSTATE0023", "/freeze_note", "STAGE_A_FREEZE_NOTE_TYPE_DRIFT"),
        ("RSTATE0024", "/source_commit", "STAGE_A_SOURCE_COMMIT_DELETION"),
        ("RSTATE0025", "/code_commit", "STAGE_A_CODE_COMMIT_DELETION"),
        ("RSTATE0026", "/source_lock/code_commit", "STAGE_A_SOURCE_LOCK_COMMIT_DELETION"),
        ("RSTATE0027", "/code_commit", "STAGE_A_CODE_COMMIT_TYPE_DRIFT"),
        ("RSTATE0028", "/source_lock/code_commit", "STAGE_A_SOURCE_LOCK_COMMIT_TYPE_DRIFT"),
        ("RSTATE0029", "/freeze_note", "STAGE_A_FREEZE_NOTE_DELETION"),
        ("RSTATE0030", "/source_commit", "STAGE_B_SOURCE_COMMIT_TYPE_DRIFT"),
        ("RSTATE0031", "/code_commit", "STAGE_B_CODE_COMMIT_TYPE_DRIFT"),
        ("RSTATE0032", "/source_lock/code_commit", "STAGE_B_SOURCE_LOCK_COMMIT_TYPE_DRIFT"),
    )
    return set(operations)


def packet_semantic_contract() -> set[tuple[str, str, str]]:
    return {
        ("PSEM0001", "/control_grid/field_sizes", "SEMANTIC_REANCHOR_ORDER_REVERSAL"),
        ("PSEM0002", "/claim_boundary", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0003", "/marker_contract/source_marker", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0004", "/operator_contract/source_owner", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0005", "/positive_control_input/cross_type_bijection_claimed", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0006", "/raw_repair_rows/0/id", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0007", "/source_object_input/orientation", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0008", "/target_object_input/target_clock", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0009", "/type_ledger/0/name", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0010", "/witness_input/clock_support_word_text", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0011", "/integration_chronology/blind", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0012", "/terminal_contract/route_terminals", "SEMANTIC_REANCHOR_ORDER_REVERSAL"),
        ("PSEM0013", "/portable_source_input/rows/0/source_id", "SEMANTIC_SOURCE_ID_SCHEME_DRIFT"),
        ("PSEM0014", "/portable_source_input/source_manifest_sha256", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0015", "/terminal_contract/branch_status", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0016", "/terminal_contract/literature_boundary_external", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
        ("PSEM0017", "/terminal_contract/universal_no_go_claimed", "SEMANTIC_REANCHOR_VALUE_DRIFT"),
    }


def selection_semantic_contract() -> set[tuple[str, str, str]]:
    return {
        ("SSEM0001", "/raw_selection_cards/packet/cards/0/source_clock", "SEMANTIC_SELECTION_VALUE_DRIFT"),
        ("SSEM0002", "/raw_selection_cards/packet/cards/0/a0_verdict", "SEMANTIC_SELECTION_VALUE_DRIFT"),
        ("SSEM0003", "/raw_selection_cards/packet/rule/clauses/0", "SEMANTIC_SELECTION_VALUE_DRIFT"),
        ("SSEM0004", "/raw_selection_cards/packet/chronology/novelty_credit", "SEMANTIC_SELECTION_VALUE_DRIFT"),
        ("SSEM0005", "/raw_selection_cards/packet/cards", "SEMANTIC_SELECTION_ORDER_REVERSAL"),
    }


def chronology_semantic_contract(packet: dict[str, Any]) -> set[tuple[str, str, str]]:
    pointers: list[str] = []

    def escape(text: str) -> str:
        return text.replace("~", "~0").replace("/", "~1")

    def walk(value: Any, pointer: str) -> None:
        if type(value) is dict:
            for key, child in value.items():
                walk(child, pointer + "/" + escape(key))
        elif type(value) is list:
            for index, child in enumerate(value):
                walk(child, f"{pointer}/{index}")
        else:
            pointers.append(pointer)

    walk(packet["integration_chronology"], "/integration_chronology")
    return {
        (f"PCHR{index:04d}", pointer, "SEMANTIC_CHRONOLOGY_VALUE_DRIFT")
        for index, pointer in enumerate(sorted(pointers), 1)
    }


def structural_special_contract() -> set[tuple[str, str, str]]:
    return {
        ("PSTRUCT0001", "/control_grid/field_sizes", "LIST_CONTAINER_TO_SCALAR"),
        ("SSTRUCT0001", "/raw_selection_cards/packet/cards", "LIST_CONTAINER_TO_SCALAR"),
    }


def expected_mutation_result(root: Path, contract: dict[str, Any], packet: dict[str, Any]) -> dict[str, Any] | None:
    registry_path = root / "code/contracts/MUTATION_REGISTRY.json"
    if not contained_regular_file(root, "code/contracts/MUTATION_REGISTRY.json"):
        return None
    registry = json_value(registry_path)
    if type(registry) is not dict:
        return None
    frozen = contract.get("mutation_registry", {})
    if digest(registry_path.read_bytes()) != frozen.get("sha256"):
        return None
    packet_recursive = recursive_pointer_operations(packet)
    selection_expected = {item for item in packet_recursive if item[0].startswith("/raw_selection_cards")}
    packet_expected = packet_recursive - selection_expected
    packet_actual = {
        (row.get("json_pointer"), row.get("operation"))
        for row in registry.get("packet_mutations", []) if str(row.get("id", "")).startswith("PKT")
    }
    selection_actual = {
        (row.get("json_pointer"), row.get("operation"))
        for row in registry.get("selection_mutations", []) if str(row.get("id", "")).startswith("SEL")
    }
    packet_specials = {
        (row.get("id"), row.get("json_pointer"), row.get("operation"))
        for row in registry.get("packet_mutations", []) if str(row.get("id", "")).startswith("PRAW")
    }
    if packet_actual != packet_expected or selection_actual != selection_expected \
            or packet_specials != {
                ("PRAW0001", "/", "NONCANONICAL_WHITESPACE"),
                ("PRAW0002", "/", "DUPLICATE_TOP_KEY"),
                ("PRAW0003", "/", "RAW_KEY_ORDER_SWAP"),
                ("PRAW0004", "/", "DUPLICATE_NESTED_KEY"),
            }:
        return None
    packet_semantics = {
        (row.get("id"), row.get("json_pointer"), row.get("operation"))
        for row in registry.get("packet_mutations", []) if str(row.get("id", "")).startswith("PSEM")
    }
    selection_semantics = {
        (row.get("id"), row.get("json_pointer"), row.get("operation"))
        for row in registry.get("selection_mutations", []) if str(row.get("id", "")).startswith("SSEM")
    }
    if packet_semantics != packet_semantic_contract() \
            or selection_semantics != selection_semantic_contract():
        return None
    chronology_semantics = {
        (row.get("id"), row.get("json_pointer"), row.get("operation"))
        for row in registry.get("packet_mutations", [])
        if str(row.get("id", "")).startswith("PCHR")
    }
    if chronology_semantics != chronology_semantic_contract(packet):
        return None
    structural_specials = {
        (row.get("id"), row.get("json_pointer"), row.get("operation"))
        for group in ("packet_mutations", "selection_mutations")
        for row in registry.get(group, []) if "STRUCT" in str(row.get("id", ""))
    }
    if structural_specials != structural_special_contract():
        return None
    route_actual = {
        (row.get("json_pointer"), row.get("operation"))
        for row in registry.get("route_mutations", []) if str(row.get("id", "")).startswith("RSEM")
    }
    route_specials = {
        (row.get("id"), row.get("json_pointer"), row.get("operation"))
        for row in registry.get("route_mutations", []) if not str(row.get("id", "")).startswith("RSEM")
    }
    # The live rendered Route is the only canonical recursive source; the
    # expectation document is not substituted for its output bytes here.
    try:
        if not contained_regular_file(root, ROUTE_REL):
            return None
        route_value = yaml.load((root / ROUTE_REL).read_bytes(), Loader=UniqueLoader)
    except Exception:
        return None
    if type(route_value) is not dict \
            or route_actual != recursive_pointer_operations(route_value, skip_route_provenance=True) \
            or route_specials != route_special_contract():
        return None
    specs = {
        "audit": ("audit_mutations", "auditor_rejects"),
        "packet": ("packet_mutations", "dual"),
        "route": ("route_mutations", "dual"),
        "selection": ("selection_mutations", "dual"),
        "static": ("static_mutations", "auditor_rejects"),
    }
    groups: dict[str, Any] = {}
    all_ids: list[str] = []
    dual = 0
    for group, (key, decision) in specs.items():
        rows = registry.get(key)
        if type(rows) is not list:
            return None
        ids = [row.get("id") for row in rows]
        if ids != sorted(set(ids)):
            return None
        all_ids.extend(ids)
        executed = []
        for row in rows:
            decisions = {"independent_rejects": True, "main_rejects": True} if decision == "dual" else {decision: True}
            if decision == "dual":
                dual += 2
            executed.append({**decisions, "expected_rejection": row["expected_rejection"], "id": row["id"], "json_pointer": row["json_pointer"], "operation": row["operation"]})
        id_hash = digest("".join(identifier + "\n" for identifier in ids).encode("ascii"))
        groups[group] = {"count": len(rows), "id_sha256": id_hash, "rows": executed, "survivors": []}
    all_ids.sort()
    return {
        "audit_rejections": len(registry["audit_mutations"]),
        "dual_rejections": dual,
        "groups": groups,
        "mutation_ids": all_ids,
        "mutation_ids_sha256": digest("".join(identifier + "\n" for identifier in all_ids).encode("ascii")),
        "registry_sha256": digest(registry_path.read_bytes()),
        "schema": "paper42-adversarial-mutation-results-v2",
        "static_rejections": len(registry["static_mutations"]),
        "survivors": [],
        "total_mutations": len(all_ids),
        "writer_state_control": {
            "baseline_audit_accepted": True,
            "final_manifest_entry_count": 20,
            "final_pdf_deletion_rejected": True,
            "final_pdf_symlink_rejected": True,
            "post_output_sync_audit_accepted": True,
            "schema": "paper42-writer-state-control-v1",
            "unauthorized_integration_owned_write_rejected": True,
            "unauthorized_writer_path_rejected": True,
        },
    }


def expected_route_projection(science: dict[str, Any], independent: bool) -> dict[str, Any]:
    checks = (
        ["artifact_paths", "candidate", "canonical_payload", "chronology", "evidence_statuses", "overall", "paired_state", "route_b", "route_tuple", "science_hash", "source_lock", "terminal_codes", "type_and_owner"]
        if independent else
        ["a0", "a1", "a2", "a3", "a4", "artifact_paths", "authority_integration", "canonical_payload", "claim_scope", "chronology", "evidence_statuses", "overall", "paired_state", "raw_serialization", "route_b", "route_tuple", "schema", "science_hash", "source_lock", "terminal_codes", "type_and_owner"]
    )
    return {
        "check_count": len(checks),
        "checks": {name: True for name in checks},
        "overall_verdict": "ROUTE_A_REJECTED",
        "paired_state": "STATE_A",
        "route_b_invocation_allowed": False,
        "route_tuple": science["route"]["route_tuple"],
        "schema": "paper42-independent-route-evaluation-v1" if independent else "paper42-route-evaluation-v1",
        "terminal_codes": science["terminal_codes"],
    }


def critical_semantics(root: Path, contract: dict[str, Any]) -> tuple[bool, bool]:
    json_paths = [
        path for path in contract["owned_paths"]["results"] if path.endswith(".json")
    ] + [contract["evaluation"]["route_json_path"]]
    if any(not contained_regular_file(root, relative)
           for relative in json_paths):
        return False, False
    objects = {relative: json_value(root / relative) for relative in json_paths}
    if any(type(value) is not dict for value in objects.values()):
        return False, False
    packet_raw = (root / "results/source_packet.json").read_bytes()
    science_raw = (root / "results/scientific_results.json").read_bytes()
    science = objects["results/scientific_results.json"]
    if EXPECTED_PACKET_SHA256 and digest(packet_raw) != EXPECTED_PACKET_SHA256:
        return False, False
    if EXPECTED_SCIENCE_SHA256 and digest(science_raw) != EXPECTED_SCIENCE_SHA256:
        return False, False
    if type(science) is not dict or sorted(science) != contract["exact_science"]["science_top_level_keys"]:
        return False, False
    if not strict_equal(science["integration_chronology"], contract["chronology"]):
        return False, False
    main = objects["results/main_evaluation.json"]
    independent = objects["results/independent_evaluation.json"]
    if canonical(main.get("science")) != science_raw or canonical(independent.get("science")) != science_raw:
        return False, False
    expected_main_checks = {name: True for name in contract["evaluation"]["main_check_names"]}
    expected_independent_checks = {name: True for name in contract["evaluation"]["independent_check_names"]}
    if not strict_equal(main.get("checks"), expected_main_checks) \
            or not strict_equal(independent.get("checks"), expected_independent_checks):
        return False, False
    if set(main) != {"checks", "implementation", "schema", "science"} \
            or main["implementation"] != "algorithm_m_enumeration_and_trial_division" \
            or main["schema"] != "paper42-main-evaluation-v1" \
            or set(independent) != {"checks", "implementation", "schema", "science"} \
            or independent["implementation"] != "algorithm_r_divisor_recurrence_rabin_and_line_parser" \
            or independent["schema"] != "paper42-independent-evaluation-v1":
        return False, False
    run_files = ["independent_evaluation.json", "main_evaluation.json", "route_evaluation.json", "scientific_results.json", "source_packet.json"]
    for name in run_files:
        raws = [(root / f"results/runs/{label}/{name}").read_bytes() for label in "ABC"]
        if not (raws[0] == raws[1] == raws[2]):
            return False, False
        if name != "route_evaluation.json" and raws[0] != (root / f"results/{name}").read_bytes():
            return False, False
    expected_run_route = {
        "candidate_id": "SD-C44",
        "overall_verdict": science["route"]["overall_verdict"],
        "route_b_invocation_allowed": science["route"]["route_b_invocation_allowed"],
        "route_tuple": science["route"]["route_tuple"],
        "schema": "paper42-run-route-projection-v1",
        "science_sha256": digest(science_raw),
        "terminal_codes": science["terminal_codes"],
    }
    if any(not strict_equal(objects[f"results/runs/{label}/route_evaluation.json"],
                            expected_run_route) for label in "ABC"):
        return False, False
    if not strict_equal(objects["results/source_resolver.json"], science["source_resolver"]):
        return False, False
    if not strict_equal(objects["results/selection_resolver.json"], science["selection"]):
        return False, False
    exact_projections = {
        "results/determinant_coefficient_certificate.json": science["determinant_certificate"],
        "results/function_field_positive_control.json": science["function_field_positive_control"],
        "results/operator_ownership_certificate.json": science["operator_ledger"],
        "results/repair_matrix_certificate.json": science["repair_classification"],
        "results/witness_certificate.json": science["witness_ledger"],
        "results/type_contract_certificate.json": {"marker_ledger": science["marker_ledger"], "schema": "paper42-type-contract-certificate-v1", "type_ledger": science["type_ledger"], "type_strict": True},
    }
    if any(not strict_equal(objects[path], expected) for path, expected in exact_projections.items()):
        return False, False
    state_a_main = expected_route_projection(science, False)
    state_a_ind = expected_route_projection(science, True)
    if not strict_equal(objects["results/route_evaluation.json"], state_a_main) or not strict_equal(objects[contract["evaluation"]["route_json_path"]], state_a_ind):
        return False, False
    packet = objects["results/source_packet.json"]
    if type(packet) is not dict:
        return False, False
    mutation_expected = expected_mutation_result(root, contract, packet)
    if mutation_expected is None or not strict_equal(objects["results/adversarial_tests.json"], mutation_expected):
        return False, False
    run_hashes = {label: {name: digest((root / f"results/runs/{label}/{name}").read_bytes()) for name in run_files} for label in "ABC"}
    reproducibility = {"all_equal": True, "artifact_count_per_run": 5, "run_hashes": run_hashes, "schema": "paper42-reproducibility-certificate-v1"}
    if not strict_equal(objects["results/reproducibility_certificate.json"], reproducibility):
        return False, False
    fixed = {
        "results/cold_copy_certificate.json": {"external_historical_tree_read": False, "non_project_cwd": True, "relocated": True, "run_c_equals_run_a": True, "schema": "paper42-cold-copy-certificate-v1"},
        "results/external_provenance_stability.json": {"comparison_affects_science_bytes": False, "external_historical_tree_available": "NOT_QUERIED_CANONICAL", "external_historical_tree_read": False, "live_files_compared": 0, "matches": "NOT_APPLICABLE_CANONICAL_PORTABLE_RUN", "schema": "paper42-optional-live-provenance-comparison-v1", "snapshot_container_count": 29, "status": "PASS"},
        "results/idempotence_certificate.json": {"changed_paths": 0, "schema": "paper42-idempotence-certificate-v1", "status": "PASS"},
        "results/immutable_inputs.json": {
            **contract["immutable_release"],
            "schema": "paper42-immutable-input-reproduction-v1",
            "status": "PASS",
            "writer_baseline": {
                "manifest_sha256": contract["writer"]["baseline_manifest_sha256"],
                "snapshot_sha256": contract["writer"]["baseline_snapshot_sha256"],
            },
        },
        "results/research_reproduction.json": {"determinant_certificate": science["determinant_certificate"], "function_field_positive_control": science["function_field_positive_control"], "main_independent_equal": True, "necklace_census": science["necklace_census"], "schema": "paper42-research-reproduction-v1", "theorems": science["theorems"], "universal_no_go_claimed": False},
        "results/analysis_summary.json": {"candidate_id": "SD-C44", "main_independent_science_equal": True, "mutation_survivors": 0, "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "schema": "paper42-analysis-summary-v1", "science_sha256": digest(science_raw), "source_packet_sha256": digest(packet_raw)},
    }
    if any(not strict_equal(objects[path], expected) for path, expected in fixed.items()):
        return False, False
    expected_isolation = {
        "canonical_child_isolated": True,
        "canonical_emitter_explicit_I_B": True,
        "canonical_emitter_stdout_sha256": digest(packet_raw),
        "canonical_hostile_modules_imported": [],
        "canonical_parent_explicit_I_B": True,
        "canonical_pycache_created": False,
        "hostile_modules_tested": ["hashlib", "json", "pathlib", "sitecustomize", "source_core", "yaml"],
        "hostile_parent_environment_normalized": True,
        "hostile_parent_variables_tested": ["PYTHONDONTWRITEBYTECODE", "PYTHONHOME", "PYTHONPYCACHEPREFIX"],
        "naive_hostile_invocation_allowed": False,
        "naive_child_bytecode_suppression_env_cleared": True,
        "naive_prestartup_contamination_observed": True,
        "naive_sitecustomize_marker_observed": True,
        "schema": "paper42-hostile-pythonpath-control-v3",
    }
    expected_dependency = {
        "PyYAML": "6.0.2",
        "dependency_lock_sha256": contract["dependencies"]["dependency_lock_sha256"],
        "entrypoint_policy": contract["entrypoint_policy"],
        "interpreter_isolation": expected_isolation,
        "python_minimum": "3.11",
        "python_minimum_satisfied": True,
        "route_schema_sha256": contract["dependencies"]["route_schema_sha256"],
        "route_skill_decoded_sha256": contract["dependencies"]["route_skill_decoded_sha256"],
        "schema": "paper42-dependency-controls-v1",
        "source_snapshot_files": 29,
        "status": "PASS",
        "writer_baseline_manifest_sha256": contract["dependencies"]["writer_baseline_manifest_sha256"],
        "writer_baseline_snapshot_sha256": contract["dependencies"]["writer_baseline_snapshot_sha256"],
    }
    if not strict_equal(objects["results/dependency_controls.json"], expected_dependency):
        return False, False
    boundary_raw = (root / "results/source_evaluator_boundary.json").read_bytes()
    if EXPECTED_BOUNDARY_SHA256 and digest(boundary_raw) != EXPECTED_BOUNDARY_SHA256:
        return False, False
    boundary = objects["results/source_evaluator_boundary.json"]
    if boundary.get("source_imports_evaluator") is not False or boundary.get("main_imports_source") is not False or boundary.get("independent_imports_main_or_route") is not False:
        return False, False
    algorithm = objects["results/algorithm_independence.json"]
    expected_algorithm = {"main_implementation": main["implementation"], "independent_implementation": independent["implementation"], "main_independent_science_byte_equal": True, "process_boundary": True, "schema": "paper42-algorithm-independence-certificate-v1", "source_evaluator_boundary_sha256": digest(boundary_raw), "status": "PASS"}
    if not strict_equal(algorithm, expected_algorithm):
        return False, False
    transaction_control = {
        "forced_failure_class": "FORCED_LATE_PREINSTALL_FAILURE",
        "forced_failure_observed": True,
        "schema": "paper42-transactional-preinstall-control-v1",
        "target_cache_entries": 0,
        "target_output_paths_present": 0,
        "target_physical_writes": 0,
    }
    static_gate = {
        "code_path_count": len(contract["owned_paths"]["code"]),
        "dont_write_bytecode": True,
        "experiment_path_count": len(contract["owned_paths"]["experiments"]),
        "isolated_interpreter": True,
        "python_minimum": "3.11",
        "python_minimum_satisfied": True,
        "PyYAML": "6.0.2",
        "snapshot_path_count": 29,
        "transactional_preinstall_control": transaction_control,
    }
    expected_integrity_contract = {
        "contract_sha256": digest((root / "code/contracts/INTEGRATION_CONTRACT.json").read_bytes()),
        "managed_path_count": len(contract["owned_paths"]["static"] + contract["owned_paths"]["outputs"]),
        "result_path_count": len(contract["owned_paths"]["results"]),
        "schema": "paper42-integrity-contract-result-v1",
        "static_gate": static_gate,
    }
    if not strict_equal(objects["results/integrity_contract.json"], expected_integrity_contract):
        return False, False
    expected_route_certificate = {
        "independent_check_count": objects[contract["evaluation"]["route_json_path"]]["check_count"],
        "independent_route_sha256": digest((root / contract["evaluation"]["route_json_path"]).read_bytes()),
        "main_check_count": objects["results/route_evaluation.json"]["check_count"],
        "main_route_sha256": digest((root / "results/route_evaluation.json").read_bytes()),
        "paired_state": "VALID_STAGE1",
        "schema": "paper42-route-schema-certificate-v1",
        "tuple_agreement": True,
    }
    if not strict_equal(objects["results/route_schema_certificate.json"], expected_route_certificate):
        return False, False
    exact_results = {"paths": contract["owned_paths"]["results"], "schema": "paper42-exact-result-set-v1"}
    exact_text = {"ledger_exclusions": [LEDGER_REL, MANIFEST_REL, ROUTE_REL], "managed_paths": sorted(contract["owned_paths"]["static"] + contract["owned_paths"]["outputs"]), "schema": "paper42-exact-integration-text-set-v1", "writer_paths_included": False}
    if not strict_equal(objects["results/exact_result_set.json"], exact_results) or not strict_equal(objects["results/exact_text_set.json"], exact_text):
        return False, False
    audit_bytes = canonical(pass_result())
    if (root / "results/integrity_audit.json").read_bytes() != audit_bytes:
        return False, False
    sealed = {"audit_stdout_sha256": digest(audit_bytes), "dummy_commit": DUMMY, "schema": "paper42-sealed-state-compatibility-v1", "state_a_status": "PASS", "state_b_status": "PASS", "stdout_byte_identical": True}
    if not strict_equal(objects["results/sealed_state_compatibility.json"], sealed):
        return False, False
    report_ok = (root / "EXPERIMENT_REPORT.md").is_file()
    if EXPECTED_REPORT_SHA256:
        report_ok = report_ok and digest((root / "EXPERIMENT_REPORT.md").read_bytes()) == EXPECTED_REPORT_SHA256
    elif report_ok:
        report = (root / "EXPERIMENT_REPORT.md").read_text(encoding="utf-8")
        report_ok = report_ok and contract["chronology"]["status"] in report and mutation_expected["mutation_ids_sha256"] in report
    return True, report_ok


def role_import_boundary(root: Path) -> bool:
    roles = {
        "source_core": [root / "code/source/source_core.py"],
        "source_emit": [root / "code/source/emit_packet.py"],
        "main": [root / "code/evaluator/evaluate_packet.py"],
        "independent": [root / "code/evaluator/independent_evaluator.py"],
        "route": [root / "code/evaluator/evaluate_route_a.py"],
        "auditor": [root / "code/audit_integrity.py"],
    }
    expected_imports = {
        "source_core": {
            "__future__", "__future__.annotations", "base64", "hashlib", "json", "pathlib",
            "pathlib.Path", "pathlib.PurePosixPath", "re", "typing", "typing.Any",
        },
        "source_emit": {
            "__future__", "__future__.annotations", "os", "pathlib", "pathlib.Path",
            "source_core", "source_core.build_packet", "source_core.canonical", "sys",
        },
        "main": {
            "__future__", "__future__.annotations", "base64", "hashlib", "itertools", "json",
            "pathlib", "pathlib.PurePosixPath", "re", "sys", "typing", "typing.Any", "yaml",
        },
        "independent": {
            "__future__", "__future__.annotations", "base64", "hashlib", "json", "pathlib",
            "pathlib.Path", "pathlib.PurePosixPath", "re", "stat", "sys", "typing", "typing.Any", "yaml",
        },
        "route": {
            "__future__", "__future__.annotations", "copy", "hashlib", "json", "pathlib",
            "pathlib.Path", "pathlib.PurePosixPath", "re", "stat", "sys", "typing", "typing.Any", "yaml",
        },
        "auditor": {
            "__future__", "__future__.annotations", "ast", "base64", "copy", "hashlib", "json",
            "os", "pathlib", "pathlib.Path", "pathlib.PurePosixPath", "re", "stat", "sys", "typing",
            "typing.Any", "yaml",
        },
    }
    allowed_reads = {
        "main": {"open(argv[1], 'rb')", "open(argv[1], 'rb').read()"},
        "independent": {
            "Path(argv[2]).read_bytes()", "handle.read()", "open(argv[1], 'rb')",
            "open(argv[1], 'rb').read()", "science_file.read_bytes()",
        },
    }
    dynamic_names = {"__import__", "compile", "eval", "exec", "execfile", "import_module"}
    try:
        for role, paths in roles.items():
            for path in paths:
                tree = ast.parse(path.read_text(encoding="utf-8"))
                imports: set[str] = set()
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        imports.update(alias.name for alias in node.names)
                    elif isinstance(node, ast.ImportFrom):
                        module = node.module or ""
                        imports.add(module)
                        imports.update(
                            f"{module}.{alias.name}" if module else alias.name
                            for alias in node.names if alias.name != "*"
                        )
                if imports != expected_imports[role]:
                    return False
                for node in ast.walk(tree):
                    if not isinstance(node, ast.Call):
                        continue
                    rendered = ast.unparse(node)
                    if isinstance(node.func, ast.Name):
                        call_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        call_name = node.func.attr
                    else:
                        call_name = ""
                    if call_name in dynamic_names:
                        return False
                    if role in {"source_core", "source_emit"} \
                            and call_name in {"open", "read", "read_bytes", "read_text"} \
                            and "code/evaluator/" in rendered:
                        return False
                    if role in allowed_reads and call_name in {"open", "read", "read_bytes", "read_text"} \
                            and rendered not in allowed_reads[role]:
                        return False
                    if role in {"route", "auditor"} and call_name in {"open", "read", "read_bytes", "read_text"} \
                            and any(token in rendered for token in
                                    ("source_core", "evaluate_packet", "independent_evaluator", "evaluate_route_a")):
                        return False
    except Exception:
        return False
    return True


def audit(root: Path) -> dict[str, Any]:
    checks = {name: False for name in CHECK_NAMES}
    if not contained_regular_file(root, "code/contracts/INTEGRATION_CONTRACT.json"):
        return checks
    contract = json_value(root / "code/contracts/INTEGRATION_CONTRACT.json")
    if type(contract) is not dict:
        return checks
    expected_static = contract["owned_paths"]["static"]
    expected_outputs = contract["owned_paths"]["outputs"]
    actual_static = sorted(
        (["RESEARCH_LOCK.json"] if (root / "RESEARCH_LOCK.json").is_file()
         and not (root / "RESEARCH_LOCK.json").is_symlink() else [])
        + file_inventory(root, "code") + file_inventory(root, "docs")
        + file_inventory(root, "experiments")
    )
    actual_results = file_inventory(root, "results")
    actual_evaluations = file_inventory(root, "evaluations")
    actual_outputs = sorted(actual_results + actual_evaluations + (["EXPERIMENT_REPORT.md"] if (root / "EXPERIMENT_REPORT.md").is_file() else []))
    checks["code_exact_set"] = file_inventory(root, "code") == contract["owned_paths"]["code"]
    checks["experiment_exact_set"] = file_inventory(root, "experiments") == contract["owned_paths"]["experiments"]
    checks["evaluation_exact_set"] = actual_evaluations == contract["owned_paths"]["evaluations"]
    checks["result_exact_set"] = actual_results == contract["owned_paths"]["results"]
    checks["text_exact_set"] = actual_static == expected_static
    checks["owned_path_boundary"] = actual_outputs == expected_outputs
    checks["report_present"] = (root / "EXPERIMENT_REPORT.md").is_file()
    checks["route_file_present"] = (root / ROUTE_REL).is_file()
    checks["algorithm_boundary"] = role_import_boundary(root)
    checks["experiment_freeze"] = all(contained_regular_file(root, path)
        and digest((root / path).read_bytes()) == expected
        for path, expected in contract["experiment_freeze"].items())
    governance = json_value(root / "RESEARCH_LOCK.json") \
        if contained_regular_file(root, "RESEARCH_LOCK.json") else None
    checks["governance_lock"] = type(governance) is dict \
        and digest((root / "RESEARCH_LOCK.json").read_bytes()) == contract["dependencies"]["governance_lock_sha256"] \
        and strict_equal(governance.get("chronology"), contract["chronology"]) \
        and governance.get("authority_copy_requires_fresh_exact_input_map") is True \
        and governance.get("integration_ownership", {}).get("static_path_count") == len(expected_static) \
        and governance.get("integration_ownership", {}).get("transactional_output_path_count") == len(expected_outputs)

    package_manifest = root / "preauthority/SHA256SUMS.txt"
    package_rows, package_format = parse_hash_file(package_manifest) \
        if contained_regular_file(root, "preauthority/SHA256SUMS.txt") else ([], False)
    package_expected = sorted(["preauthority/" + name for _, name in package_rows] + ["preauthority/SHA256SUMS.txt"])
    package_actual = file_inventory(root, "preauthority")
    checks["immutable_package"] = package_format \
        and digest(package_manifest.read_bytes()) == contract["immutable_release"]["package_manifest_sha256"] \
        and package_actual == package_expected and len(package_rows) == 16 \
        and all(safe_path(name) and contained_regular_file(root, "preauthority/" + name)
                and digest((root / "preauthority" / name).read_bytes()) == expected
                for expected, name in package_rows)
    try:
        research = json.loads(
            (root / "preauthority/RESEARCH_LOCK.json").read_bytes()
            if contained_regular_file(root, "preauthority/RESEARCH_LOCK.json") else b"null",
            object_pairs_hook=unique_json,
        )
    except Exception:
        research = None
    mapping = research.get("immutable_package_files") if type(research) is dict else None
    checks["immutable_research_lock"] = contained_regular_file(root, "preauthority/RESEARCH_LOCK.json") \
        and digest((root / "preauthority/RESEARCH_LOCK.json").read_bytes()) == contract["immutable_release"]["research_lock_sha256"] \
        and type(mapping) is dict and list(mapping) == sorted(mapping) and len(mapping) == 15 \
        and all(safe_path(name) and contained_regular_file(root, "preauthority/" + name)
                and digest((root / "preauthority" / name).read_bytes()) == expected
                for name, expected in mapping.items())
    da_paths = file_inventory(root, "independent_da")
    da_report = root / "independent_da/paper42_DA_REPORT.md"
    da_sidecar = root / "independent_da/paper42_DA_REPORT.sha256"
    checks["immutable_da"] = da_paths == ["independent_da/paper42_DA_REPORT.md", "independent_da/paper42_DA_REPORT.sha256"] \
        and contained_regular_file(root, "independent_da/paper42_DA_REPORT.md") \
        and contained_regular_file(root, "independent_da/paper42_DA_REPORT.sha256") \
        and digest(da_report.read_bytes()) == contract["immutable_release"]["da_report_sha256"] \
        and digest(da_sidecar.read_bytes()) == contract["immutable_release"]["da_sidecar_sha256"] \
        and da_sidecar.read_text(encoding="ascii") == f"{digest(da_report.read_bytes())}  paper42_DA_REPORT.md\n"
    writer = contract["writer"]
    snapshot_path = root / writer["baseline_snapshot_path"]
    snapshot = json_value(snapshot_path) \
        if contained_regular_file(root, writer["baseline_snapshot_path"]) else None
    snapshot_ok = type(snapshot) is dict \
        and digest(snapshot_path.read_bytes()) == writer["baseline_snapshot_sha256"] \
        and set(snapshot) == {"baseline_manifest_sha256", "entries", "manifest_utf8_b64", "schema"} \
        and snapshot["schema"] == "paper42-writer-baseline-snapshot-v1" \
        and snapshot["baseline_manifest_sha256"] == writer["baseline_manifest_sha256"]
    archived_rows: list[tuple[str, str]] = []
    if snapshot_ok:
        try:
            archived_manifest = base64.b64decode(snapshot["manifest_utf8_b64"], validate=True)
            archived_rows, archived_format = parse_hash_bytes(archived_manifest)
            entries = snapshot["entries"]
            snapshot_ok = archived_format \
                and digest(archived_manifest) == writer["baseline_manifest_sha256"] \
                and len(archived_rows) == writer["baseline_manifest_entry_count"] \
                and [name for _, name in archived_rows] == sorted(set(name for _, name in archived_rows)) \
                and type(entries) is list and len(entries) == len(archived_rows)
            if snapshot_ok:
                for entry, (expected, relative) in zip(entries, archived_rows):
                    snapshot_ok = snapshot_ok and type(entry) is dict \
                        and set(entry) == {"decoded_sha256", "path", "utf8_b64"} \
                        and entry["decoded_sha256"] == expected and entry["path"] == relative \
                        and digest(base64.b64decode(entry["utf8_b64"], validate=True)) == expected
        except Exception:
            snapshot_ok = False
    baseline_content_paths = [name for _, name in archived_rows] if snapshot_ok else []
    baseline_hashes = {name: expected for expected, name in archived_rows}
    mutable_sync_paths = {
        "PAPER_PLAN.md", "WRITER_HANDOFF.md", "sections/6_route_reproducibility.tex"
    }
    final_content_paths = sorted(baseline_content_paths + writer["final_artifact_paths"])
    writer_rows, writer_format = parse_hash_file(root / writer["current_manifest_path"]) \
        if contained_regular_file(root, writer["current_manifest_path"]) else ([], False)
    writer_row_paths = [name for _, name in writer_rows]
    writer_state = None
    if writer_format and writer_row_paths == baseline_content_paths:
        writer_state = "BASELINE_RESULT_FREE"
    elif writer_format and writer_row_paths == final_content_paths:
        writer_state = "POST_OUTPUT_SYNCED_COMPILED"
    writer_hashes_ok = writer_state is not None and all(
        safe_path(name) and contained_regular_file(root, name)
        and digest((root / name).read_bytes()) == expected
        for expected, name in writer_rows
    )
    if writer_state == "BASELINE_RESULT_FREE":
        writer_hashes_ok = writer_hashes_ok \
            and digest((root / writer["current_manifest_path"]).read_bytes()) == writer["baseline_manifest_sha256"]
    elif writer_state == "POST_OUTPUT_SYNCED_COMPILED":
        writer_hashes_ok = writer_hashes_ok and all(
            digest((root / relative).read_bytes()) == baseline_hashes[relative]
            for relative in baseline_content_paths if relative not in mutable_sync_paths
        )
    binary_ok = True
    if writer_state == "POST_OUTPUT_SYNCED_COMPILED":
        pdf_path = root / "main.pdf"
        if not pdf_path.is_file() or pdf_path.is_symlink():
            binary_ok = False
        else:
            pdf_raw = pdf_path.read_bytes()
            binary_ok = pdf_raw.startswith(bytes((37, 80, 68, 70, 45))) \
                and pdf_raw.rstrip().endswith(bytes((37, 37, 69, 79, 70)))
    checks["writer_manifest"] = snapshot_ok and writer_hashes_ok and binary_ok
    checks["writer_excluded"] = not any(path in expected_static or path in expected_outputs for path in writer["paths"])
    checks["writer_lane_boundary"] = writer_state in writer["allowed_states"] \
        and writer["canonical_integration_mutates_writer_paths"] is False \
        and writer["post_output_writer_sync_is_separate_authorized_lane"] is True \
        and writer["post_sync_semantic_and_compile_audit_owner"] == "root_writer_audit"

    dependency = json_value(root / "docs/DEPENDENCY_LOCK.json") \
        if contained_regular_file(root, "docs/DEPENDENCY_LOCK.json") else None
    snapshot_paths = file_inventory(root, "docs/inputs/source_snapshot")
    snapshot_rows = dependency.get("snapshot", {}).get("rows") if type(dependency) is dict else None
    source_rows, source_format = parse_hash_file(root / "preauthority/SOURCE_HASHES.sha256") \
        if contained_regular_file(root, "preauthority/SOURCE_HASHES.sha256") else ([], False)
    source_ids = [source_id for _, source_id in source_rows]
    source_map = {source_id: expected for expected, source_id in source_rows}
    source_ids_ok = source_format and len(source_rows) == 29 \
        and source_ids == sorted(set(source_ids)) \
        and all(
            (source_id.startswith("repo:") or source_id.startswith("dependency:"))
            and "\\" not in source_id and not source_id.startswith(("repo:/", "dependency:/"))
            and all(part not in {"", ".", ".."} for part in source_id.split(":", 1)[1].split("/"))
            for source_id in source_ids
        )
    snapshot_ok = type(snapshot_rows) is list and len(snapshot_rows) == 29 and source_ids_ok
    if snapshot_ok:
        expected_snapshot = sorted(row["container_path"] for row in snapshot_rows)
        row_ids = [row.get("source_id") for row in snapshot_rows if type(row) is dict]
        snapshot_ok = row_ids == source_ids and expected_snapshot == sorted(set(expected_snapshot)) \
            and snapshot_paths == expected_snapshot
        if snapshot_ok:
            for row in snapshot_rows:
                try:
                    container_path = row.get("container_path")
                    if not contained_regular_file(root, container_path):
                        snapshot_ok = False
                        break
                    encoded = (root / container_path).read_bytes()
                    decoded = decode_locked_base64(encoded)
                    snapshot_ok = snapshot_ok and digest(encoded) == row["encoded_sha256"] \
                        and digest(decoded) == row["decoded_sha256"] \
                        and row["decoded_sha256"] == source_map[row["source_id"]]
                except Exception:
                    snapshot_ok = False
    checks["snapshot_exact_set"] = snapshot_ok
    route_skill_relative = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
    route_skill_encoded = (root / route_skill_relative).read_bytes() \
        if contained_regular_file(root, route_skill_relative) else b""
    try:
        route_skill_decoded = decode_locked_base64(route_skill_encoded)
    except Exception:
        route_skill_decoded = b""
    route_schema_relative = "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
    checks["dependency_bytes"] = type(dependency) is dict \
        and digest((root / "docs/DEPENDENCY_LOCK.json").read_bytes()) == contract["dependencies"]["dependency_lock_sha256"] \
        and contained_regular_file(root, route_schema_relative) \
        and digest((root / route_schema_relative).read_bytes()) == contract["dependencies"]["route_schema_sha256"] \
        and digest(route_skill_encoded) == contract["dependencies"]["route_skill_encoded_sha256"] \
        and digest(route_skill_decoded) == contract["dependencies"]["route_skill_decoded_sha256"]
    checks["source_manifest_anchor"] = source_ids_ok \
        and digest((root / "preauthority/SOURCE_HASHES.sha256").read_bytes()) == contract["dependencies"]["source_manifest_sha256"]

    ledger_rows, ledger_format = parse_hash_file(root / LEDGER_REL) \
        if contained_regular_file(root, LEDGER_REL) else ([], False)
    ledger_paths = [path for _, path in ledger_rows]
    expected_ledger = sorted(set(expected_static + expected_outputs) - {LEDGER_REL, ROUTE_REL, MANIFEST_REL})
    checks["ledger_format"] = ledger_format
    checks["ledger_sorted_unique"] = ledger_paths == sorted(set(ledger_paths))
    checks["ledger_safe_paths"] = all(safe_path(path) for path in ledger_paths)
    checks["ledger_self_excluded"] = LEDGER_REL not in ledger_paths and ROUTE_REL not in ledger_paths and MANIFEST_REL not in ledger_paths
    checks["ledger_exact_set"] = ledger_paths == expected_ledger
    checks["ledger_hashes"] = ledger_format and checks["ledger_safe_paths"] \
        and all(contained_regular_file(root, path)
                and digest((root / path).read_bytes()) == expected for expected, path in ledger_rows)

    manifest = root / MANIFEST_REL
    manifest_present = contained_regular_file(root, MANIFEST_REL)
    manifest_rows, manifest_format = parse_hash_file(manifest) if manifest_present else ([], True)
    manifest_paths = [path for _, path in manifest_rows]
    actual_all = sorted(path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file() and path.relative_to(root).as_posix() != MANIFEST_REL)
    checks["manifest_format"] = manifest_format
    checks["manifest_sorted_unique"] = not manifest_present or manifest_paths == sorted(set(manifest_paths))
    checks["manifest_safe_paths"] = not manifest_present or all(safe_path(path) for path in manifest_paths)
    checks["manifest_self_excluded"] = MANIFEST_REL not in manifest_paths
    checks["manifest_exact_set"] = not manifest_present or manifest_paths == actual_all
    checks["manifest_hashes"] = not manifest_present or (
        checks["manifest_safe_paths"] and all(
            contained_regular_file(root, path)
            and digest((root / path).read_bytes()) == expected for expected, path in manifest_rows
        )
    )
    writer_expected_paths = []
    if writer_state == "BASELINE_RESULT_FREE":
        writer_expected_paths = sorted(baseline_content_paths + [writer["current_manifest_path"]])
    elif writer_state == "POST_OUTPUT_SYNCED_COMPILED":
        writer_expected_paths = sorted(final_content_paths + [writer["current_manifest_path"]])
    expected_whole_tree = sorted(set(
        expected_static + expected_outputs + package_expected + da_paths + writer_expected_paths
        + ([MANIFEST_REL] if manifest_present else [])
    ))
    actual_whole_tree = sorted(
        path.relative_to(root).as_posix() for path in root.rglob("*")
        if path.is_file() and not path.is_symlink()
    )
    checks["whole_tree_exact_set"] = actual_whole_tree == expected_whole_tree

    route: dict[str, Any] | None = None
    duplicate_safe = False
    route_raw = b""
    try:
        if not contained_regular_file(root, ROUTE_REL):
            raise ValueError("Route path is not a contained regular file")
        route_raw = (root / ROUTE_REL).read_bytes()
        route = yaml.load(route_raw, Loader=UniqueLoader)
        duplicate_safe = type(route) is dict
    except Exception:
        route = None
    checks["route_duplicate_safe_parse"] = duplicate_safe
    if route is not None:
        commits = [route.get("source_commit"), route.get("code_commit"), route.get("source_lock", {}).get("code_commit")]
        state_a = commits == [PENDING, PENDING, PENDING] and not manifest_present
        state_b = len(set(commits)) == 1 and type(commits[0]) is str and re.fullmatch(r"[0-9a-f]{40}", commits[0]) is not None and commits[0] != ZERO and manifest_present
        checks["paired_route_triple"] = state_a or state_b
        checks["manifest_presence_pair"] = state_a or state_b
        checks["paired_route_note"] = route.get("freeze_note") == (STAGE1_NOTE if state_a else sealed_note(commits[0]) if state_b else None)
        schema = json_value(root / "code/contracts/ROUTE_A_V0_2_SCHEMA.json")
        checks["route_raw_order"] = type(schema) is dict and list(route) == schema["ordered_top_level_keys"] and list(route.get("source_lock", {})) == schema["ordered_source_lock_keys"]
        normalized = copy.deepcopy(route)
        normalized["source_commit"] = PENDING
        normalized["code_commit"] = PENDING
        normalized["source_lock"]["code_commit"] = PENDING
        normalized["freeze_note"] = STAGE1_NOTE
        normalized["authority_integration"]["paired_state"] = "STATE_A"
        normalized["authority_integration"]["status"] = "CANONICAL_PENDING_FIRST_ARTIFACT_COMMIT"
        normalized_sha = digest(canonical(normalized))
        checks["route_canonical_payload"] = not EXPECTED_NORMALIZED_ROUTE_SHA256 or normalized_sha == EXPECTED_NORMALIZED_ROUTE_SHA256
        if state_a:
            checks["route_raw_serialization"] = not EXPECTED_STAGE1_ROUTE_RAW_SHA256 or digest(route_raw) == EXPECTED_STAGE1_ROUTE_RAW_SHA256
        elif state_b:
            dummy = copy.deepcopy(route)
            dummy["source_commit"] = DUMMY
            dummy["code_commit"] = DUMMY
            dummy["source_lock"]["code_commit"] = DUMMY
            dummy["freeze_note"] = sealed_note(DUMMY)
            checks["route_raw_serialization"] = not EXPECTED_DUMMY_ROUTE_RAW_SHA256 or digest(dump_route(dummy)) == EXPECTED_DUMMY_ROUTE_RAW_SHA256
        else:
            checks["route_raw_serialization"] = False
        checks["route_artifact_base"] = route.get("artifact_path_base") == contract["artifact_path_base"]
        artifacts = list(route.get("source_lock", {}).get("artifact_paths", []))
        for layer in ["a0", "a1", "a2", "a3", "a4"]:
            artifacts.extend(route.get(layer, {}).get("artifacts", []))
        checks["route_artifact_paths"] = all(contained_regular_file(root, path) for path in artifacts)
        checks["route_exact_tuple"] = route.get("route_tuple") == contract["exact_science"]["route_tuple"] and route.get("overall_verdict") == "ROUTE_A_REJECTED"
        checks["route_b_locked"] = route.get("route_b_invocation_allowed") is False and route.get("route_b", {}).get("invocation_allowed") is False
        checks["route_terminal_set"] = strict_equal(route.get("terminal_codes"), contract["exact_science"]["terminal_codes"])
        science_path = root / "results/scientific_results.json"
        checks["route_science_hash"] = science_path.is_file() and route.get("authority_integration", {}).get("scientific_results_sha256") == digest(science_path.read_bytes())
    else:
        for name in ["paired_route_triple", "manifest_presence_pair", "paired_route_note", "route_raw_order", "route_canonical_payload", "route_raw_serialization", "route_artifact_base", "route_artifact_paths", "route_exact_tuple", "route_b_locked", "route_terminal_set", "route_science_hash"]:
            checks[name] = False

    critical, report_ok = critical_semantics(root, contract)
    checks["critical_result_semantics_exact"] = critical
    checks["report_mutation_ledger_exact"] = report_ok
    checks["result_declaration_exact"] = critical
    checks["text_declaration_exact"] = critical
    checks["science_byte_equality_control"] = critical
    checks["chronology_exact"] = critical

    symlinks = [path for path in root.rglob("*") if path.is_symlink()]
    caches = [path for path in root.rglob("*") if path.name in {"__pycache__", ".pytest_cache"} or path.suffix in {".pyc", ".pyo"}]
    checks["integration_no_symlink"] = not symlinks
    checks["integration_no_cache"] = not caches
    hygiene = True
    no_absolute = True
    binary_writer_paths = set(writer["final_binary_paths"] if writer_state == "POST_OUTPUT_SYNCED_COMPILED" else [])
    host_tokens = (
        bytes((47, 116, 109, 112)),
        bytes((47, 114, 111, 111, 116, 47)),
        bytes((47, 104, 111, 109, 101, 47)),
        bytes((84, 77, 80, 95)),
    )
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root).as_posix()
        raw = path.read_bytes()
        if relative not in binary_writer_paths and (
            b"\x00" in raw or b"\r" in raw or (raw and not raw.endswith(b"\n"))
            or any(line.endswith((b" ", b"\t")) for line in raw.splitlines())
        ):
            hygiene = False
        if relative in expected_static + expected_outputs:
            if any(token in raw for token in host_tokens) or str(root).encode() in raw:
                no_absolute = False
    checks["integration_hygiene"] = hygiene
    checks["integration_no_absolute_path_tokens"] = no_absolute
    return checks


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("FAIL: ARGUMENT_CONTRACT\n")
        return 2
    root = Path(argv[1]).resolve()
    try:
        checks = audit(root)
    except Exception:
        # The auditor is exception-total: malformed or absent inputs produce the
        # same closed, sorted rejection envelope rather than a traceback/rc1.
        checks = {name: False for name in CHECK_NAMES}
    failures = sorted(name for name in CHECK_NAMES if checks.get(name) is not True)
    if failures:
        sys.stderr.write("FAIL: integrity checks failed: " + ", ".join(failures) + "\n")
        return 2
    sys.stdout.buffer.write(canonical(pass_result()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
