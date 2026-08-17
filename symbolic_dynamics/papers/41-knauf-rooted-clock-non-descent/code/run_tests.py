#!/usr/bin/env python3
"""Run the exhaustive Paper 41 mutation contract against its responsible gates."""

from __future__ import annotations

import ast
from base64 import b64decode, b64encode
import copy
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "code/contracts/MUTATION_REGISTRY.json"
REGISTRY_SHA256 = "bd19e3abace1d6ac33d9c8f8c5578c28d54e27c00d3aabb94fbf2bb621363eee"
CONTRACT = ROOT / "code/contracts/INTEGRATION_CONTRACT.json"
MAIN = ROOT / "code/evaluator/evaluate_packet.py"
INDEPENDENT = ROOT / "code/evaluator/independent_evaluator.py"
ROUTE_MAIN = ROOT / "code/evaluator/evaluate_route_a.py"
AUDITOR_REL = "code/audit_integrity.py"
ROUTE_REL = "evaluations/route_a/SD-C43/2026-08-17.yaml"
MANIFEST_REL = "PAPER_MANIFEST.sha256"
DUMMY = "0123456789abcdef0123456789abcdef01234567"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
STAGE1_NOTE = (
    "Stage 1 authority artifact has three PENDING_FIRST_ARTIFACT_COMMIT fields and no "
    "PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it replaces source_commit, code_commit, "
    "and source_lock.code_commit with one identical lowercase nonzero 40-hex artifact commit "
    "and adds the sorted self-excluding PAPER_MANIFEST.sha256."
)


class MutationRejected(RuntimeError):
    """Stable local rejection carrying one exact responsibility code."""


def canonical(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def environment() -> dict[str, str]:
    result = os.environ.copy()
    result.pop("PYTHONPATH", None)
    result.pop("PYTHONHOME", None)
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1"})
    return result


def isolated_python(script: Path | str, *arguments: str) -> list[str]:
    return [sys.executable, "-I", "-B", str(script), *arguments]


def stage2_note(commit: str) -> str:
    return (
        f"Stage 1 artifact commit {commit} contained the three PENDING_FIRST_ARTIFACT_COMMIT "
        "fields and no PAPER_MANIFEST.sha256. Stage 2 is metadata-only: it seals source_commit, "
        "code_commit, and source_lock.code_commit to that same lowercase nonzero 40-hex artifact "
        "commit and adds the sorted self-excluding PAPER_MANIFEST.sha256."
    )


def assert_exact_rejection(arguments: list[str], expected_stderr: str, cwd: Path) -> None:
    completed = subprocess.run(arguments, cwd=cwd, env=environment(), capture_output=True, check=False)
    if completed.returncode != 2:
        raise ValueError(f"wrong rejection rc, expected 2: {completed.returncode}; {arguments!r}")
    if completed.stdout:
        raise ValueError(f"rejecting process emitted stdout: {arguments!r}")
    actual_stderr = completed.stderr.decode("utf-8", errors="strict")
    if actual_stderr != expected_stderr:
        raise ValueError(f"wrong exact rejection envelope: expected={expected_stderr!r}, actual={actual_stderr!r}")


def assert_evaluator_rejection(
    arguments: list[str], token: str, cwd: Path, *, structured_detail: str | None = None
) -> None:
    payload = token if structured_detail is None else f"{token}:{structured_detail!r}"
    assert_exact_rejection(arguments, f"REJECT: {payload}\n", cwd)


def assert_audit_rejection(arguments: list[str], codes: list[str], cwd: Path) -> None:
    if codes != sorted(set(codes)) or not codes:
        raise ValueError(f"audit rejection-code list is not sorted, unique, and nonempty: {codes!r}")
    assert_exact_rejection(arguments, f"FAIL: integrity checks failed: {', '.join(codes)}\n", cwd)


def pointer_tokens(pointer: str) -> list[str]:
    if pointer in ("", "/"):
        return []
    if not pointer.startswith("/"):
        raise ValueError(f"not an RFC6901 pointer: {pointer}")
    return [item.replace("~1", "/").replace("~0", "~") for item in pointer[1:].split("/")]


def resolve(value: Any, pointer: str) -> Any:
    current = value
    for token in pointer_tokens(pointer):
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current


def parent_and_key(value: Any, pointer: str) -> tuple[Any, str]:
    tokens = pointer_tokens(pointer)
    if not tokens:
        raise ValueError("operation needs a non-root pointer")
    current = value
    for token in tokens[:-1]:
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current, tokens[-1]


def replace_at(value: Any, pointer: str, replacement: Any) -> None:
    parent, key = parent_and_key(value, pointer)
    if isinstance(parent, list):
        parent[int(key)] = replacement
    else:
        parent[key] = replacement


def delete_at(value: Any, pointer: str) -> None:
    parent, key = parent_and_key(value, pointer)
    if isinstance(parent, list):
        del parent[int(key)]
    else:
        del parent[key]


def value_drift(value: Any) -> Any:
    if isinstance(value, bool):
        return not value
    if isinstance(value, int):
        return value + 1
    if isinstance(value, str):
        return value + "_DRIFT"
    if isinstance(value, list):
        return value + ["__mutation_drift__"]
    if isinstance(value, dict):
        return {**value, "__mutation_drift__": True}
    return "__mutation_drift__"


def type_drift(value: Any) -> Any:
    if isinstance(value, str):
        return 17
    if isinstance(value, bool):
        return "TYPE_DRIFT"
    if isinstance(value, int):
        return "TYPE_DRIFT"
    if isinstance(value, list):
        return "TYPE_DRIFT"
    if isinstance(value, dict):
        return "TYPE_DRIFT"
    return ["TYPE_DRIFT"]


def apply_generic(value: dict[str, Any], pointer: str, operation: str) -> None:
    if operation in {"EXTRA_KEY", "EXTRA_TOP_KEY"}:
        target = resolve(value, pointer)
        if not isinstance(target, dict):
            raise ValueError("EXTRA_KEY target is not a mapping")
        target["__mutation_extra__"] = True
    elif operation == "TRUSTED_PASS_INJECTION":
        value["trusted_pass"] = True
    elif operation == "KEY_DELETION":
        delete_at(value, pointer)
    elif operation == "VALUE_DRIFT":
        replace_at(value, pointer, value_drift(resolve(value, pointer)))
    elif operation == "VALUE_AND_TYPE_DRIFT":
        replace_at(value, pointer, type_drift(resolve(value, pointer)))
    elif operation == "MEMBER_DELETION":
        target = resolve(value, pointer)
        if not isinstance(target, list) or not target:
            raise ValueError("MEMBER_DELETION target is not a nonempty list")
        del target[0]
    elif operation == "MEMBER_DUPLICATION":
        target = resolve(value, pointer)
        if not isinstance(target, list) or not target:
            raise ValueError("MEMBER_DUPLICATION target is not a nonempty list")
        target.append(copy.deepcopy(target[0]))
    elif operation == "ORDER_REVERSAL":
        target = resolve(value, pointer)
        if not isinstance(target, list) or len(target) < 2:
            raise ValueError("ORDER_REVERSAL target has fewer than two members")
        target.reverse()
    elif operation == "RECORD_DELETION":
        delete_at(value, pointer)
    elif operation == "RECORD_DUPLICATION":
        parent, key = parent_and_key(value, pointer)
        if not isinstance(parent, list):
            raise ValueError("RECORD_DUPLICATION parent is not a list")
        index = int(key)
        parent.insert(index, copy.deepcopy(parent[index]))
    else:
        raise KeyError(operation)


def mutate_packet(packet: dict[str, Any], row: dict[str, Any]) -> None:
    pointer, operation = row["json_pointer"], row["operation"]
    if pointer == "/source_input/rows" and operation == "MEMBER_DUPLICATION":
        packet["source_input"]["rows"][-1] = copy.deepcopy(packet["source_input"]["rows"][0])
    elif operation in {
        "EXTRA_KEY", "EXTRA_TOP_KEY", "KEY_DELETION", "MEMBER_DELETION",
        "MEMBER_DUPLICATION", "ORDER_REVERSAL", "TRUSTED_PASS_INJECTION", "VALUE_DRIFT",
    }:
        apply_generic(packet, pointer, operation)
    elif operation == "BAD_SCHEME":
        replace_at(packet, pointer, "unknown:mutation")
    elif operation == "ZERO_HASH" or operation == "HASH_FIELD_DRIFT":
        replace_at(packet, pointer, "0" * 64)
    elif operation == "ABSOLUTE_ID":
        replace_at(packet, pointer, "repo:/absolute")
    elif operation == "PARENT_ESCAPE":
        replace_at(packet, pointer, "repo:../escape")
    elif operation == "BACKSLASH_ID":
        replace_at(packet, pointer, "repo:path\\escape")
    elif operation == "PAYLOAD_SUBSTITUTION":
        replace_at(packet, pointer, b64encode(b"mutation\n").decode("ascii"))
    elif operation == "OBJECT_ONLY_DRIFT":
        target = resolve(packet, pointer)
        target["__mutation_only_in_object__"] = True
    elif operation == "BOOL_TO_INT":
        current = resolve(packet, pointer)
        if type(current) is not bool:
            raise ValueError("BOOL_TO_INT target is not bool")
        replace_at(packet, pointer, int(current))
    elif operation == "INT_TO_FLOAT":
        current = resolve(packet, pointer)
        if type(current) is not int:
            raise ValueError("INT_TO_FLOAT target is not int")
        replace_at(packet, pointer, float(current))
    elif operation == "INT_TO_BOOL":
        current = resolve(packet, pointer)
        if type(current) is not int or current not in (0, 1):
            raise ValueError("INT_TO_BOOL target is not 0/1 int")
        replace_at(packet, pointer, bool(current))
    elif operation in {"NONCANONICAL_PACKET_WHITESPACE", "NONCANONICAL_PACKET_KEY_ORDER"}:
        pass
    else:
        raise KeyError(operation)


def generate_packet_type_rows(packet: dict[str, Any]) -> list[dict[str, Any]]:
    candidates: list[tuple[str, str]] = []

    def visit(value: Any, pointer: str) -> None:
        if type(value) is bool:
            candidates.append((pointer or "/", "BOOL_TO_INT"))
        elif type(value) is int:
            candidates.append((pointer or "/", "INT_TO_FLOAT"))
            if value in (0, 1):
                candidates.append((pointer or "/", "INT_TO_BOOL"))
        elif type(value) is dict:
            for key in sorted(value):
                visit(value[key], pointer + "/" + key.replace("~", "~0").replace("/", "~1"))
        elif type(value) is list:
            for index, child in enumerate(value):
                visit(child, pointer + f"/{index}")

    visit(packet, "")
    rows = []
    for index, (pointer, operation) in enumerate(candidates, 1):
        if operation != "INT_TO_FLOAT" and pointer.startswith("/selection_input/packet/"):
            main = independent = "SELECTION_OUTER_COHERENCE_MISMATCH"
        elif operation != "INT_TO_FLOAT" and pointer.startswith("/route_provenance_input/route_schema/"):
            main = "Route schema object/raw mismatch"
            independent = "Route schema object differs from raw bytes"
        else:
            main = "PACKET_TYPE_SCHEMA_MISMATCH"
            independent = "INDEPENDENT_PACKET_TYPE_SCHEMA_MISMATCH"
        rows.append({
            "expected_rejection": {"independent": independent, "main": main},
            "id": f"PTYPE{index:04d}",
            "json_pointer": pointer,
            "operation": operation,
            "target": "packet",
        })
    return rows


def generate_packet_chronology_rows(packet: dict[str, Any]) -> list[dict[str, Any]]:
    corrections = packet["integration_chronology"]["known_corrections"]
    if not isinstance(corrections, list) or not corrections \
            or not all(isinstance(item, str) and item for item in corrections):
        raise ValueError("canonical chronology corrections are not a nonempty string list")
    return [{
        "expected_rejection": {
            "independent": "INTEGRATION_CHRONOLOGY_MISMATCH",
            "main": "INTEGRATION_CHRONOLOGY_MISMATCH",
        },
        "id": f"PCHRON{index + 1:04d}",
        "json_pointer": f"/integration_chronology/known_corrections/{index}",
        "operation": "VALUE_DRIFT",
        "target": "packet",
    } for index in range(len(corrections))]


def generate_audit_chronology_rows(contract: dict[str, Any]) -> list[dict[str, Any]]:
    corrections = contract["integration_chronology"]["known_corrections"]
    rows: list[dict[str, Any]] = []
    for index in range(len(corrections)):
        for prefix, operation, path in (
            ("ACPROT", "CHRONOLOGY_PROTOCOL_CORRECTION", "/docs~1INTEGRITY_PROTOCOL.md"),
            ("ACRPT", "CHRONOLOGY_REPORT_CORRECTION", "/EXPERIMENT_REPORT.md"),
        ):
            rows.append({
                "expected_rejection": {"auditor": ["chronology_exact", "ledger_hashes"]},
                "id": f"{prefix}{index + 1:04d}",
                "json_pointer": path,
                "operation": f"{operation}_{index}",
                "target": "audit",
            })
    return sorted(rows, key=lambda row: row["id"])


def mutate_selection(packet: dict[str, Any], row: dict[str, Any]) -> None:
    selection = packet["selection_input"]
    value = selection["packet"]
    pointer, operation = row["json_pointer"], row["operation"]
    if operation in {
        "MEMBER_DELETION", "MEMBER_DUPLICATION", "ORDER_REVERSAL",
        "RECORD_DELETION", "RECORD_DUPLICATION", "VALUE_DRIFT",
    }:
        apply_generic(value, pointer, operation)
    elif operation == "HIDDEN_PREDICATE_INSERTION":
        value["rule"]["clauses"].append("candidate_number_order_equals_6")
    elif operation in {"REMOVE_PRIMITIVE_PHRASE", "REMOVE_SIGN_PHRASE"}:
        text = resolve(value, pointer)
        phrase = (
            "construct or rule out a canonical primitive-cycle map"
            if operation == "REMOVE_PRIMITIVE_PHRASE"
            else "pre-existing symmetry produces the sign"
        )
        replacement = text.replace(phrase, "removed_selector_phrase")
        if replacement == text:
            replacement = text + (" primitive_phrase_mutation" if "PRIMITIVE" in operation else " sign_phrase_mutation")
        replace_at(value, pointer, replacement)
    else:
        raise KeyError(operation)
    raw = canonical(value)
    selection["packet_utf8"] = raw.decode("ascii")
    selection["packet_sha256"] = digest(raw)


def make_sealed(route: dict[str, Any], commit: str = DUMMY) -> None:
    route["source_commit"] = commit
    route["code_commit"] = commit
    route["source_lock"]["code_commit"] = commit
    route["freeze_note"] = stage2_note(commit)


def mutate_route(route: dict[str, Any], row: dict[str, Any]) -> bytes | None:
    pointer, operation = row["json_pointer"], row["operation"]
    if row["id"].startswith("RSEM"):
        apply_generic(route, pointer, operation)
    elif operation == "PARENT_ESCAPE":
        replace_at(route, pointer, "../escape")
    elif operation == "ABSOLUTE_PATH":
        replace_at(route, pointer, "/absolute")
    elif operation == "MISSING_PATH":
        replace_at(route, pointer, "results/does-not-exist.json")
    elif operation == "SAFE_EXISTING_ARTIFACT_SUBSTITUTION":
        replace_at(route, pointer, "results/selection_resolver.json")
    elif operation == "DUPLICATE_YAML_KEY":
        raw = yaml.safe_dump(route, sort_keys=False, allow_unicode=False).encode("ascii")
        return raw + b"candidate_id: SD-C43\n"
    elif operation == "PENDING_TRIPLE_MISMATCH":
        route["code_commit"] = DUMMY
    elif operation == "STALE_STAGE1_NOTE":
        route["freeze_note"] = "stale"
    elif operation == "SEALED_UPPERCASE_COMMIT":
        make_sealed(route, DUMMY.upper())
    elif operation == "SEALED_ZERO_COMMIT":
        make_sealed(route, "0" * 40)
    elif operation == "SEALED_TRIPLE_MISMATCH":
        make_sealed(route)
        route["code_commit"] = "1" * 40
    elif operation == "STALE_STAGE2_NOTE":
        make_sealed(route)
        route["freeze_note"] = "stale"
    elif operation == "RAW_WHITESPACE_DRIFT":
        return yaml.safe_dump(route, sort_keys=False, allow_unicode=False, width=100).encode("ascii") + b"\n"
    elif operation == "TOP_KEY_ORDER_DRIFT":
        first_key = next(iter(route))
        first_value = route.pop(first_key)
        route[first_key] = first_value
    elif operation == "PENDING_SOURCE_COMMIT_MISMATCH":
        route["source_commit"] = DUMMY
    elif operation == "PENDING_SOURCE_LOCK_COMMIT_MISMATCH":
        route["source_lock"]["code_commit"] = DUMMY
    elif operation == "SEALED_SOURCE_COMMIT_MISMATCH":
        make_sealed(route)
        route["source_commit"] = "1" * 40
    elif operation == "SEALED_SOURCE_LOCK_COMMIT_MISMATCH":
        make_sealed(route)
        route["source_lock"]["code_commit"] = "1" * 40
    elif operation == "PROVENANCE_KEY_DELETION":
        delete_at(route, pointer)
    elif operation == "PROVENANCE_TYPE_DRIFT":
        replace_at(route, pointer, type_drift(resolve(route, pointer)))
    else:
        raise KeyError(operation)
    return None


def route_expected(pointer: str, operation: str) -> dict[str, str]:
    artifact = "/artifacts/" in pointer or "/artifact_paths/" in pointer
    if artifact and operation == "VALUE_AND_TYPE_DRIFT":
        return {"main": "UNSAFE_ARTIFACT_PATH", "independent": "UNSAFE_ARTIFACT_PATH"}
    if artifact and operation == "VALUE_DRIFT":
        return {"main": "MISSING_ARTIFACT", "independent": "MISSING_ARTIFACT"}
    return {
        "main": "ROUTE_CANONICAL_PAYLOAD_MISMATCH",
        "independent": "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH",
    }


def generate_route_rows(route: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    skipped = {"/source_commit", "/code_commit", "/source_lock/code_commit", "/freeze_note"}
    sequence = 1

    def escaped(value: Any) -> str:
        return str(value).replace("~", "~0").replace("/", "~1")

    def add(pointer: str, operation: str) -> None:
        nonlocal sequence
        rows.append({
            "expected_rejection": route_expected(pointer, operation),
            "id": f"RSEM{sequence:04d}",
            "json_pointer": pointer,
            "operation": operation,
            "target": "route",
        })
        sequence += 1

    def walk(value: Any, pointer: str = "") -> None:
        if isinstance(value, dict):
            add(pointer, "EXTRA_KEY")
            for key, child in value.items():
                child_pointer = pointer + "/" + escaped(key)
                if child_pointer not in skipped:
                    add(child_pointer, "KEY_DELETION")
                walk(child, child_pointer)
        elif isinstance(value, list):
            if value:
                add(pointer, "MEMBER_DELETION")
                add(pointer, "MEMBER_DUPLICATION")
                if len(value) > 1:
                    add(pointer, "ORDER_REVERSAL")
                for index in range(len(value)):
                    add(f"{pointer}/{index}", "VALUE_DRIFT")
            for index, child in enumerate(value):
                walk(child, f"{pointer}/{index}")
        elif pointer not in skipped:
            add(pointer, "VALUE_AND_TYPE_DRIFT")

    walk(route)
    special = [
        ("RART001", "/source_lock/artifact_paths/0", "SAFE_EXISTING_ARTIFACT_SUBSTITUTION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RART002", "/a0/artifacts/0", "SAFE_EXISTING_ARTIFACT_SUBSTITUTION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RART003", "/a1/artifacts/0", "SAFE_EXISTING_ARTIFACT_SUBSTITUTION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RART004", "/a2/artifacts/0", "SAFE_EXISTING_ARTIFACT_SUBSTITUTION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RART005", "/a3/artifacts/0", "SAFE_EXISTING_ARTIFACT_SUBSTITUTION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RART006", "/a4/artifacts/0", "SAFE_EXISTING_ARTIFACT_SUBSTITUTION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RSP001", "/source_lock/artifact_paths/0", "PARENT_ESCAPE", "UNSAFE_ARTIFACT_PATH", "UNSAFE_ARTIFACT_PATH"),
        ("RSP002", "/source_lock/artifact_paths/0", "ABSOLUTE_PATH", "UNSAFE_ARTIFACT_PATH", "UNSAFE_ARTIFACT_PATH"),
        ("RSP003", "/source_lock/artifact_paths/0", "MISSING_PATH", "MISSING_ARTIFACT", "MISSING_ARTIFACT"),
        ("RSP004", "/candidate_id", "DUPLICATE_YAML_KEY", "DUPLICATE_YAML_KEY", "DUPLICATE_YAML_KEY"),
        ("RSP005", "/code_commit", "PENDING_TRIPLE_MISMATCH", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP006", "/freeze_note", "STALE_STAGE1_NOTE", "STALE_FREEZE_NOTE", "STALE_FREEZE_NOTE"),
        ("RSP007", "/source_commit", "SEALED_UPPERCASE_COMMIT", "INVALID_COMMIT_FORMAT", "INVALID_COMMIT_FORMAT"),
        ("RSP008", "/source_commit", "SEALED_ZERO_COMMIT", "INVALID_COMMIT_FORMAT", "INVALID_COMMIT_FORMAT"),
        ("RSP009", "/code_commit", "SEALED_TRIPLE_MISMATCH", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP010", "/freeze_note", "STALE_STAGE2_NOTE", "STALE_FREEZE_NOTE", "STALE_FREEZE_NOTE"),
        ("RSP011", "", "RAW_WHITESPACE_DRIFT", "RAW_ROUTE_RENDERER_BYTES_MISMATCH", "INDEPENDENT_RAW_ROUTE_RENDERER_BYTES_MISMATCH"),
        ("RSP012", "", "TOP_KEY_ORDER_DRIFT", "RAW_ROUTE_RENDERER_BYTES_MISMATCH", "INDEPENDENT_RAW_ROUTE_KEY_ORDER_MISMATCH"),
        ("RSP013", "/source_commit", "PENDING_SOURCE_COMMIT_MISMATCH", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP014", "/source_lock/code_commit", "PENDING_SOURCE_LOCK_COMMIT_MISMATCH", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP015", "/source_commit", "SEALED_SOURCE_COMMIT_MISMATCH", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP016", "/source_lock/code_commit", "SEALED_SOURCE_LOCK_COMMIT_MISMATCH", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP017", "/source_commit", "PROVENANCE_KEY_DELETION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RSP018", "/code_commit", "PROVENANCE_KEY_DELETION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RSP019", "/source_lock/code_commit", "PROVENANCE_KEY_DELETION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RSP020", "/freeze_note", "PROVENANCE_KEY_DELETION", "ROUTE_CANONICAL_PAYLOAD_MISMATCH", "INDEPENDENT_ROUTE_CANONICAL_PAYLOAD_MISMATCH"),
        ("RSP021", "/source_commit", "PROVENANCE_TYPE_DRIFT", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP022", "/code_commit", "PROVENANCE_TYPE_DRIFT", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP023", "/source_lock/code_commit", "PROVENANCE_TYPE_DRIFT", "PAIRED_STATE_MISMATCH", "PAIRED_STATE_MISMATCH"),
        ("RSP024", "/freeze_note", "PROVENANCE_TYPE_DRIFT", "STALE_FREEZE_NOTE", "STALE_FREEZE_NOTE"),
    ]
    rows.extend({
        "expected_rejection": {"main": main, "independent": independent},
        "id": identifier,
        "json_pointer": pointer,
        "operation": operation,
        "target": "route",
    } for identifier, pointer, operation, main, independent in special)
    return sorted(rows, key=lambda row: row["id"])


def load_registry(route: dict[str, Any]) -> dict[str, Any]:
    raw = REGISTRY.read_bytes()
    if digest(raw) != REGISTRY_SHA256:
        raise ValueError("mutation registry changed")
    registry = json.loads(raw)
    expected_groups = {
        "audit_mutations", "packet_mutations", "route_mutations", "schema",
        "selection_mutations", "static_mutations",
    }
    if set(registry) != expected_groups or registry["schema"] != "paper41-exhaustive-mutation-registry-v2":
        raise ValueError("mutation registry schema differs")
    all_ids: list[str] = []
    for group in sorted(expected_groups - {"schema"}):
        rows = registry[group]
        identifiers = [row["id"] for row in rows]
        if identifiers != sorted(set(identifiers)):
            raise ValueError(f"{group} IDs are not sorted and unique")
        for row in rows:
            if set(row) != {"expected_rejection", "id", "json_pointer", "operation", "target"}:
                raise ValueError(f"{row['id']} registry row keys differ")
            pointer_tokens(row["json_pointer"])
            expected_keys = {"auditor"} if group in {"audit_mutations", "static_mutations"} else {"main", "independent"}
            if set(row["expected_rejection"]) != expected_keys:
                raise ValueError(f"{row['id']} rejection-role keys differ")
            values = list(row["expected_rejection"].values())
            if group == "audit_mutations":
                if len(values) != 1 or not isinstance(values[0], list) or values[0] != sorted(set(values[0])) \
                        or not values[0] or not all(isinstance(token, str) and token for token in values[0]):
                    raise ValueError(f"{row['id']} has an invalid exact audit rejection list")
            elif not all(isinstance(token, str) and token for token in values):
                raise ValueError(f"{row['id']} has an empty rejection token")
        all_ids.extend(identifiers)
    if len(all_ids) != len(set(all_ids)):
        raise ValueError("mutation IDs collide across groups")
    if registry["route_mutations"] != generate_route_rows(route):
        raise ValueError("registered Route pointers do not equal recursive canonical enumeration")
    return registry


def snapshot_inventory(root: Path, contract: dict[str, Any]) -> tuple[list[str], str, str]:
    base_rel = contract["owned_paths"]["repo_snapshot_root"]
    base = root / base_rel
    relative = sorted(path.relative_to(base).as_posix() for path in base.rglob("*") if path.is_file())
    path_hash = digest("".join(path + "\n" for path in relative).encode("utf-8"))
    stream = "".join(
        f"{digest((base / path).read_bytes())}  {path}\n" for path in relative
    ).encode("utf-8")
    return relative, path_hash, digest(stream)


def import_map(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.add(node.module or "")
    return names


def import_records(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    records: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            records.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            records.add(module)
            records.update(
                f"{module}.{alias.name}" if module else alias.name
                for alias in node.names if alias.name != "*"
            )
    return records


def call_leaf(call: ast.Call) -> str:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    return ""


def dynamic_call_aliases(tree: ast.AST) -> set[str]:
    """Return local names that can invoke Python's dynamic execution/import API."""
    direct = {"__import__", "compile", "eval", "exec", "getattr"}
    imported = {
        "import_module", "module_from_spec", "run_module", "run_path",
        "spec_from_file_location",
    }
    aliases = set(direct)
    module_aliases: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in {"builtins", "importlib", "importlib.util", "runpy"}:
                    module_aliases.add(alias.asname or alias.name.split(".", 1)[0])
        elif isinstance(node, ast.ImportFrom) and node.module in {
                "builtins", "importlib", "importlib.util", "runpy"}:
            for alias in node.names:
                if alias.name in direct | imported:
                    aliases.add(alias.asname or alias.name)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name) \
                and node.value.id in aliases:
            aliases.update(
                target.id for target in node.targets if isinstance(target, ast.Name)
            )
    return aliases | {
        f"{module}.{name}" for module in module_aliases for name in direct | imported
    }


def dynamic_call_name(call: ast.Call) -> str:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return ast.unparse(call.func)
    return ""


def boundary_ast_check(path: Path, role: str) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    dynamic_aliases = dynamic_call_aliases(tree)
    allowed_reads = {
        "main": {"open(argv[1], 'rb')", "open(argv[1], 'rb').read()"},
        "independent": {
            "Path(argv[2]).read_bytes()", "handle.read()", "open(argv[1], 'rb')",
            "science_file.read_bytes()",
        },
    }
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        leaf = call_leaf(node)
        if dynamic_call_name(node) in dynamic_aliases:
            if role.startswith("source"):
                raise MutationRejected("SOURCE_DYNAMIC_IMPORT_EVALUATOR")
            if role == "main":
                raise MutationRejected("MAIN_DYNAMIC_IMPORT_SOURCE")
            if role == "independent":
                raise MutationRejected("INDEPENDENT_DYNAMIC_IMPORT_PRODUCTION")
            if role == "route":
                raise MutationRejected("ROUTE_DYNAMIC_IMPORT_PRODUCTION")
            raise MutationRejected("AUDITOR_DYNAMIC_IMPORT_PRODUCTION")
        rendered = ast.unparse(node)
        if role.startswith("source") and leaf in {"open", "read", "read_bytes", "read_text"} \
                and "code/evaluator/" in rendered:
            raise MutationRejected("SOURCE_READS_EVALUATOR")
        if role in allowed_reads and leaf in {"open", "read", "read_bytes", "read_text"} \
                and rendered not in allowed_reads[role]:
            if role == "main":
                raise MutationRejected("MAIN_DIRECT_SOURCE_READ")
            raise MutationRejected("INDEPENDENT_DIRECT_SOURCE_READ")


def static_check(root: Path, contract: dict[str, Any]) -> None:
    owned = contract["owned_paths"]
    actual_code = sorted(path.relative_to(root).as_posix() for path in (root / "code").rglob("*") if path.is_file())
    if actual_code != owned["code"]:
        raise MutationRejected("CODE_EXACT_SET")
    actual_docs = sorted(path.relative_to(root).as_posix() for path in (root / "docs").rglob("*") if path.is_file())
    prefix = owned["repo_snapshot_root"] + "/"
    if [path for path in actual_docs if not path.startswith(prefix)] != owned["docs"]:
        raise MutationRejected("DOC_EXACT_SET")
    actual_experiments = sorted(path.relative_to(root).as_posix() for path in (root / "experiments").rglob("*") if path.is_file())
    if actual_experiments != owned["experiments"]:
        raise MutationRejected("EXPERIMENT_EXACT_SET")
    _, path_hash, stream_hash = snapshot_inventory(root, contract)
    if path_hash != contract["dependencies"]["snapshot_path_list_sha256"]:
        raise MutationRejected("SNAPSHOT_EXACT_SET")
    if stream_hash != contract["dependencies"]["snapshot_hash_stream_sha256"]:
        raise MutationRejected("SNAPSHOT_HASH")

    lock_path = root / "docs/DEPENDENCY_LOCK.json"
    try:
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
    except Exception as error:
        raise MutationRejected("DEPENDENCY_MAP") from error
    if lock.get("python", {}).get("third_party") != ["PyYAML==6.0.2"]:
        raise MutationRejected("DEPENDENCY_PYYAML")
    if lock.get("python", {}).get("minimum") != "3.11" or sys.version_info < (3, 11):
        raise MutationRejected("DEPENDENCY_PYTHON_MINIMUM")
    if set(lock.get("dependencies", {})) != {"P40_DA_REPORT", "P40_DA_REPORT_SIDECAR"}:
        raise MutationRejected("DEPENDENCY_MAP")
    if digest(lock_path.read_bytes()) != contract["dependencies"]["dependency_lock_sha256"]:
        raise MutationRejected("DEPENDENCY_MAP")
    dependency_files = [
        ("docs/inputs/dependencies/paper40_DA_REPORT.md", "paper40_da_report_sha256", "DEPENDENCY_P40_REPORT"),
        ("docs/inputs/dependencies/paper40_DA_REPORT.sha256", "paper40_da_sidecar_sha256", "DEPENDENCY_P40_SIDECAR"),
    ]
    for relative, key, code in dependency_files:
        if digest((root / relative).read_bytes()) != contract["dependencies"][key]:
            raise MutationRejected(code)
    encoded = (root / "docs/inputs/route-a-evaluator-v0.2.0.md.b64").read_bytes()
    try:
        decoded = b64decode(b"".join(encoded.split()), validate=True)
    except Exception as error:
        raise MutationRejected("DEPENDENCY_SKILL_ENCODED") from error
    if digest(decoded) != contract["dependencies"]["route_skill_decoded_sha256"]:
        raise MutationRejected("DEPENDENCY_SKILL_DECODED")
    if digest(encoded) != contract["dependencies"]["route_skill_encoded_sha256"]:
        raise MutationRejected("DEPENDENCY_SKILL_ENCODED")
    if digest((root / "code/contracts/ROUTE_A_V0_2_SCHEMA.json").read_bytes()) != contract["dependencies"]["route_schema_sha256"]:
        raise MutationRejected("DEPENDENCY_ROUTE_SCHEMA")

    boundary_ast_check(root / "code/source/source_core.py", "source_core")
    boundary_ast_check(root / "code/source/emit_packet.py", "source_emit")
    boundary_ast_check(root / "code/evaluator/evaluate_packet.py", "main")
    boundary_ast_check(root / "code/evaluator/independent_evaluator.py", "independent")
    boundary_ast_check(root / "code/evaluator/evaluate_route_a.py", "route")
    boundary_ast_check(root / "code/audit_integrity.py", "auditor")
    source_imports = import_map(root / "code/source/source_core.py") | import_map(root / "code/source/emit_packet.py")
    main_imports = import_map(root / "code/evaluator/evaluate_packet.py")
    independent_imports = import_map(root / "code/evaluator/independent_evaluator.py")
    if any("evaluator" in name for name in source_imports):
        raise MutationRejected("SOURCE_IMPORTS_EVALUATOR")
    if any(name == "source_core" or name.startswith("code.source") for name in main_imports):
        raise MutationRejected("MAIN_IMPORTS_SOURCE")
    if any(name == "source_core" or name.startswith("code.source") for name in independent_imports):
        raise MutationRejected("INDEPENDENT_IMPORTS_SOURCE")
    if any("evaluate_packet" in name for name in independent_imports):
        raise MutationRejected("INDEPENDENT_IMPORTS_MAIN")
    if any("evaluate_route_a" in name for name in independent_imports):
        raise MutationRejected("INDEPENDENT_IMPORTS_ROUTE")
    role_records = {
        "source_core": import_records(root / "code/source/source_core.py"),
        "source_emit": import_records(root / "code/source/emit_packet.py"),
        "main": import_records(root / "code/evaluator/evaluate_packet.py"),
        "independent": import_records(root / "code/evaluator/independent_evaluator.py"),
        "route": import_records(root / "code/evaluator/evaluate_route_a.py"),
        "auditor": import_records(root / "code/audit_integrity.py"),
    }
    if any("evaluate" in name or "independent_evaluator" in name or "audit_integrity" in name
           for name in role_records["source_core"] | role_records["source_emit"]):
        raise MutationRejected("SOURCE_IMPORTS_EVALUATOR")
    if any("source_core" in name or "code.source" in name for name in role_records["main"]):
        raise MutationRejected("MAIN_IMPORTS_SOURCE")
    if any("independent_evaluator" in name for name in role_records["main"]):
        raise MutationRejected("MAIN_IMPORTS_INDEPENDENT")
    if any("evaluate_route_a" in name for name in role_records["main"]):
        raise MutationRejected("MAIN_IMPORTS_ROUTE")
    if any(name == "code" or name.startswith("code.") for name in role_records["main"]):
        raise MutationRejected("MAIN_IMPORTS_LOCAL_CODE_NAMESPACE")
    if any("source_core" in name or "code.source" in name for name in role_records["independent"]):
        raise MutationRejected("INDEPENDENT_IMPORTS_SOURCE")
    if any("evaluate_packet" in name for name in role_records["independent"]):
        raise MutationRejected("INDEPENDENT_IMPORTS_MAIN")
    if any("evaluate_route_a" in name for name in role_records["independent"]):
        raise MutationRejected("INDEPENDENT_IMPORTS_ROUTE")
    if any("source_core" in name or "code.source" in name for name in role_records["route"]):
        raise MutationRejected("ROUTE_IMPORTS_SOURCE")
    if any("evaluate_packet" in name or "independent_evaluator" in name or "audit_integrity" in name
           for name in role_records["route"]):
        raise MutationRejected("ROUTE_IMPORTS_PRODUCTION")
    if any("evaluate_route_a" in name for name in role_records["auditor"]):
        raise MutationRejected("AUDITOR_IMPORTS_ROUTE")
    if any("source_core" in name or "evaluate_packet" in name or "independent_evaluator" in name
           for name in role_records["auditor"]):
        raise MutationRejected("AUDITOR_IMPORTS_PRODUCTION")
    allowed = set(sys.stdlib_module_names) | {"", "yaml", "source_core"}
    for relative in owned["code"]:
        if not relative.endswith(".py"):
            continue
        for name in import_map(root / relative):
            if name.split(".", 1)[0] not in allowed:
                raise MutationRejected("UNDECLARED_DEPENDENCY")
    runner_text = (root / "code/run_exact_integration.py").read_text(encoding="utf-8")
    if "sys.dont_write_bytecode = True" not in runner_text:
        raise MutationRejected("RUNNER_BYTECODE_GUARD")
    if "if not sys.flags.isolated:" not in runner_text or "os.execve(" not in runner_text \
            or '[sys.executable, "-I", "-B", os.path.abspath(__file__), *sys.argv[1:]]' not in runner_text:
        raise MutationRejected("RUNNER_ISOLATION_GUARD")
    bootstrap_guard = runner_text.index("if not sys.flags.isolated:")
    bootstrap_end = runner_text.index("sys.dont_write_bytecode = True")
    if bootstrap_guard >= bootstrap_end or any(
        runner_text.index(token) < bootstrap_end
        for token in (
            "import ast", "from base64 import b64decode", "from hashlib import sha256",
            "import importlib.util", "import json", "from pathlib import Path", "import shutil",
            "import subprocess", "import tempfile", "from typing import Any", "import yaml",
        )
    ):
        raise MutationRejected("RUNNER_BOOTSTRAP_ORDER_GUARD")
    if 'return [sys.executable, "-I", "-B", str(script), *arguments]' not in runner_text:
        raise MutationRejected("CHILD_ISOLATION_GUARD")
    if 'result.pop("PYTHONPATH", None)' not in runner_text or 'result.pop("PYTHONHOME", None)' not in runner_text \
            or '"PYTHONNOUSERSITE": "1"' not in runner_text:
        raise MutationRejected("ENVIRONMENT_SCRUB_GUARD")
    emitter_text = (root / "code/source/emit_packet.py").read_text(encoding="utf-8")
    if "if not sys.flags.isolated:" not in emitter_text or "os.execve(" not in emitter_text \
            or '[sys.executable, "-I", "-B", os.path.abspath(__file__), *sys.argv[1:]]' not in emitter_text \
            or "sys.dont_write_bytecode = True" not in emitter_text:
        raise MutationRejected("EMITTER_ISOLATION_GUARD")
    emitter_bootstrap_end = emitter_text.index("sys.dont_write_bytecode = True")
    if any(emitter_text.index(token) < emitter_bootstrap_end for token in (
        "from pathlib import Path", "from source_core import build_packet, canonical_bytes",
    )):
        raise MutationRejected("EMITTER_BOOTSTRAP_ORDER_GUARD")
    if "root.parents[2]" in runner_text or '"external_historical_tree_read": False' not in runner_text \
            or '"external_historical_tree_available": "NOT_QUERIED_CANONICAL"' not in runner_text:
        raise MutationRejected("CANONICAL_EXTERNAL_TREE_GUARD")
    if 'science = require_science_projection_bytes_equal(' not in runner_text \
            or 'raise RuntimeError("MAIN_INDEPENDENT_SCIENCE_BYTES_MISMATCH")' not in runner_text \
            or 'main_data["science"] != independent_data["science"]' in runner_text:
        raise MutationRejected("SCIENCE_BYTE_EQUALITY_GUARD")
    if '"minimal_packet_runtime": minimal_evaluator_packet_control(root)' not in runner_text \
            or '"no_contracts_docs_or_source_present": True' not in runner_text \
            or '"stdout_byte_identical_to_full_tree": True' not in runner_text:
        raise MutationRejected("EVALUATOR_MINIMAL_RUNTIME_GUARD")
    if '"hashlib", "json", "pathlib", "sitecustomize", "source_core", "yaml"' \
            not in runner_text \
            or '"naive_prestartup_contamination_observed": True' not in runner_text \
            or '"naive_sitecustomize_marker_observed": True' not in runner_text:
        raise MutationRejected("NAIVE_HOSTILE_STARTUP_NEGATIVE_GUARD")
    if 'result.pop("PYTHONDONTWRITEBYTECODE", None)' not in runner_text \
            or 'result.pop("PYTHONPYCACHEPREFIX", None)' not in runner_text \
            or '"hostile_parent_environment_normalized": True' not in runner_text:
        raise MutationRejected("HOSTILE_PARENT_ENV_NORMALIZATION_GUARD")
    if "def build_validated_stage_and_install(" not in runner_text \
            or "def transactional_preinstall_control(" not in runner_text \
            or "if force_late_failure:\n        raise RuntimeError(FORCED_LATE_FAILURE)" not in runner_text \
            or 'stage_env[INTERNAL_STAGE_ENV] = "1"' not in runner_text \
            or 'target_output_state(ROOT, contract)' not in runner_text \
            or 'preexisting_state = target_output_state(ROOT, contract)' not in runner_text \
            or 'input_hash_map(stage, contract) != initial_inputs' not in runner_text \
            or 'sys.argv[1:] == ["--force-late-transaction-failure"]' not in runner_text:
        raise MutationRejected("TRANSACTIONAL_INSTALL_GUARD")
    harness_text = (root / "code/run_tests.py").read_text(encoding="utf-8")
    if 'all_ids = sorted(\n        row["id"]' not in harness_text \
            or '"mutation_ids": all_ids' not in harness_text:
        raise MutationRejected("GLOBAL_MUTATION_ID_SORT_GUARD")
    entrypoint_policy = {
        "canonical_emitter_argv": ["python3", "-I", "-B", "code/source/emit_packet.py"],
        "canonical_parent_argv": ["python3", "-I", "-B", "code/run_exact_integration.py"],
        "child_invocation_flags": ["-I", "-B"],
        "child_only_entrypoints": [
            "code/audit_integrity.py", "code/evaluator/evaluate_packet.py",
            "code/evaluator/evaluate_route_a.py", "code/evaluator/independent_evaluator.py",
            "code/run_tests.py",
        ],
        "internal_transaction_stage_argv": [
            "python3", "-I", "-B", "code/run_exact_integration.py", "--build-validated-stage",
        ],
        "naive_hostile_invocation_allowed": False,
        "self_reexec_is_security_boundary": False,
        "transaction_failure_probe_argv": [
            "python3", "-I", "-B", "code/run_exact_integration.py",
            "--force-late-transaction-failure",
        ],
    }
    protocol_text = (root / "docs/INTEGRITY_PROTOCOL.md").read_text(encoding="utf-8")
    if contract.get("entrypoint_policy") != entrypoint_policy or \
            "CANONICAL_PARENT_AND_EMITTER_REQUIRE_EXTERNAL_PYTHON_I_B__NAIVE_HOSTILE_FORBIDDEN" \
            not in protocol_text:
        raise MutationRejected("ENTRYPOINT_POLICY_GUARD")


def path_from_row(root: Path, row: dict[str, Any]) -> Path:
    tokens = pointer_tokens(row["json_pointer"])
    if len(tokens) != 1:
        raise ValueError(f"file mutation pointer is not one encoded relative path: {row['id']}")
    relative = tokens[0]
    if relative.startswith("/") or ".." in Path(relative).parts:
        raise ValueError("unsafe registry file target")
    return root / relative


def apply_static_mutation(root: Path, row: dict[str, Any]) -> None:
    path = path_from_row(root, row)
    operation = row["operation"]
    if operation == "DELETE_FILE":
        path.unlink()
    elif operation == "ADD_FILE":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"mutation\n")
    elif operation in {
        "APPEND_SOURCE_IMPORT_EVALUATOR", "APPEND_MAIN_IMPORT_SOURCE",
        "APPEND_INDEPENDENT_IMPORT_SOURCE", "APPEND_INDEPENDENT_IMPORT_MAIN",
        "APPEND_INDEPENDENT_IMPORT_ROUTE", "APPEND_UNDECLARED_IMPORT",
        "APPEND_MAIN_IMPORT_INDEPENDENT", "APPEND_MAIN_IMPORT_ROUTE",
        "APPEND_ROUTE_IMPORT_SOURCE", "APPEND_AUDITOR_IMPORT_ROUTE", "APPEND_MAIN_CODE_ALIAS",
    }:
        imports = {
            "APPEND_SOURCE_IMPORT_EVALUATOR": "import code.evaluator.evaluate_packet\n",
            "APPEND_MAIN_IMPORT_SOURCE": "import code.source.source_core\n",
            "APPEND_INDEPENDENT_IMPORT_SOURCE": "import code.source.source_core\n",
            "APPEND_INDEPENDENT_IMPORT_MAIN": "import code.evaluator.evaluate_packet\n",
            "APPEND_INDEPENDENT_IMPORT_ROUTE": "import code.evaluator.evaluate_route_a\n",
            "APPEND_UNDECLARED_IMPORT": "import numpy\n",
            "APPEND_MAIN_IMPORT_INDEPENDENT": "import code.evaluator.independent_evaluator\n",
            "APPEND_MAIN_IMPORT_ROUTE": "import code.evaluator.evaluate_route_a\n",
            "APPEND_ROUTE_IMPORT_SOURCE": "import code.source.source_core\n",
            "APPEND_AUDITOR_IMPORT_ROUTE": "import code.evaluator.evaluate_route_a\n",
            "APPEND_MAIN_CODE_ALIAS": "from code import evaluator\n",
        }
        path.write_text(path.read_text(encoding="utf-8") + imports[operation], encoding="utf-8")
    elif operation == "MOVE_SHADOWABLE_IMPORT_BEFORE_REEXEC":
        text = path.read_text(encoding="utf-8")
        import_line = "from pathlib import Path\n"
        guard_line = "if not sys.flags.isolated:\n"
        if text.count(import_line) != 1 or text.count(guard_line) != 1:
            raise ValueError("bootstrap-order fixture is not unique")
        text = text.replace(import_line, "", 1)
        text = text.replace(guard_line, import_line + guard_line, 1)
        path.write_text(text, encoding="utf-8")
    elif operation == "DISABLE_EMITTER_ISOLATION":
        text = path.read_text(encoding="utf-8")
        old = "if not sys.flags.isolated:"
        if text.count(old) != 1:
            raise ValueError("emitter isolation fixture is not unique")
        path.write_text(text.replace(old, "if False:", 1), encoding="utf-8")
    elif operation == "MOVE_EMITTER_IMPORT_BEFORE_REEXEC":
        text = path.read_text(encoding="utf-8")
        import_line = "from pathlib import Path\n"
        guard_line = "if not sys.flags.isolated:\n"
        if text.count(import_line) != 1 or text.count(guard_line) != 1:
            raise ValueError("emitter bootstrap-order fixture is not unique")
        text = text.replace(import_line, "", 1)
        text = text.replace(guard_line, import_line + guard_line, 1)
        path.write_text(text, encoding="utf-8")
    elif operation == "ENABLE_EXTERNAL_TREE_READ":
        text = path.read_text(encoding="utf-8")
        old = (
            '"external_historical_tree_available": "NOT_QUERIED_CANONICAL",\n'
            '        "external_historical_tree_read": False,\n'
            '        "live_files_compared": 0,'
        )
        new = (
            '"external_historical_tree_available": "QUERIED_BY_MUTATION",\n'
            '        "external_historical_tree_read": True,\n'
            '        "live_files_compared": 20,'
        )
        if text.count(old) != 1:
            raise ValueError("external-tree fixture is not unique")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif operation == "REINTRODUCE_PYTHON_SCIENCE_EQUALITY":
        text = path.read_text(encoding="utf-8")
        old = "science = require_science_projection_bytes_equal(\n        main_data[\"science\"], independent_data[\"science\"]\n    )"
        new = "if main_data[\"science\"] != independent_data[\"science\"]:\n        raise RuntimeError(\"MAIN_INDEPENDENT_SCIENCE_BYTES_MISMATCH\")\n    science = canonical(main_data[\"science\"])"
        if text.count(old) != 1:
            raise ValueError("science byte-equality fixture is not unique")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif operation == "REMOVE_SITECUSTOMIZE_NEGATIVE":
        text = path.read_text(encoding="utf-8")
        old = '"hashlib", "json", "pathlib", "sitecustomize", "source_core", "yaml"'
        new = '"hashlib", "json", "pathlib", "source_core", "yaml"'
        if text.count(old) != 1:
            raise ValueError("sitecustomize negative-control fixture is not unique")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif operation == "APPEND_MAIN_DIRECT_SOURCE_READ":
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nopen('code/source/source_core.py', 'rb').read()\n",
            encoding="utf-8",
        )
    elif operation == "APPEND_INDEPENDENT_DIRECT_SOURCE_READ":
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nopen('code/source/source_core.py', 'rb').read()\n",
            encoding="utf-8",
        )
    elif operation == "APPEND_SOURCE_DYNAMIC_IMPORT_EVALUATOR":
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\n__import__('code.evaluator.evaluate_packet')\n",
            encoding="utf-8",
        )
    elif operation == "APPEND_SOURCE_DIRECT_EVALUATOR_READ":
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nopen('code/evaluator/evaluate_packet.py', 'rb').read()\n",
            encoding="utf-8",
        )
    elif operation == "APPEND_MAIN_DYNAMIC_SOURCE":
        path.write_text(path.read_text(encoding="utf-8") + "\n__import__('code.source.source_core')\n", encoding="utf-8")
    elif operation == "APPEND_INDEPENDENT_DYNAMIC_MAIN":
        path.write_text(path.read_text(encoding="utf-8") + "\n__import__('code.evaluator.evaluate_packet')\n", encoding="utf-8")
    elif operation == "APPEND_ROUTE_DYNAMIC_SOURCE":
        path.write_text(path.read_text(encoding="utf-8") + "\n__import__('code.source.source_core')\n", encoding="utf-8")
    elif operation == "APPEND_AUDITOR_DYNAMIC_ROUTE":
        path.write_text(path.read_text(encoding="utf-8") + "\n__import__('code.evaluator.evaluate_route_a')\n", encoding="utf-8")
    elif operation == "DISABLE_MINIMAL_EVALUATOR_RUNTIME":
        text = path.read_text(encoding="utf-8")
        old = '"minimal_packet_runtime": minimal_evaluator_packet_control(root)'
        if text.count(old) != 1:
            raise ValueError("minimal evaluator runtime fixture is not unique")
        path.write_text(text.replace(old, '"minimal_packet_runtime": {}', 1), encoding="utf-8")
    elif operation == "DISABLE_HOSTILE_PARENT_ENV_NORMALIZATION":
        text = path.read_text(encoding="utf-8")
        old = 'result.pop("PYTHONPYCACHEPREFIX", None)'
        if text.count(old) != 1:
            raise ValueError("hostile parent environment fixture is not unique")
        path.write_text(text.replace(old, 'result.get("PYTHONPYCACHEPREFIX", None)', 1), encoding="utf-8")
    elif operation == "DISABLE_TRANSACTIONAL_LATE_FAILURE_GUARD":
        text = path.read_text(encoding="utf-8")
        old = "if force_late_failure:\n        raise RuntimeError(FORCED_LATE_FAILURE)"
        if text.count(old) != 1:
            raise ValueError("transactional late-failure fixture is not unique")
        path.write_text(text.replace(
            old, "if False:\n        raise RuntimeError(FORCED_LATE_FAILURE)", 1
        ), encoding="utf-8")
    elif operation == "WEAKEN_OUTPUT_NAMESPACE_PREFLIGHT":
        text = path.read_text(encoding="utf-8")
        old = "preexisting_state = target_output_state(ROOT, contract)"
        if text.count(old) != 1:
            raise ValueError("output namespace preflight fixture is not unique")
        path.write_text(text.replace(old, 'preexisting_state = "empty"', 1), encoding="utf-8")
    elif operation == "REINTRODUCE_GROUP_CONCAT_ID_ORDER":
        text = path.read_text(encoding="utf-8")
        old = "all_ids = sorted(\n        row[\"id\"]"
        new = "all_ids = list(\n        row[\"id\"]"
        if text.count(old) != 1:
            raise ValueError("global mutation-ID sort fixture is not unique")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif operation == "DRIFT_ENTRYPOINT_PROTOCOL":
        text = path.read_text(encoding="utf-8")
        old = "CANONICAL_PARENT_AND_EMITTER_REQUIRE_EXTERNAL_PYTHON_I_B__NAIVE_HOSTILE_FORBIDDEN"
        if text.count(old) != 1:
            raise ValueError("entrypoint protocol fixture is not unique")
        path.write_text(text.replace(old, "MUTATED_ENTRYPOINT_POLICY", 1), encoding="utf-8")
    elif operation in {
        "DISABLE_BYTECODE_GUARD", "DISABLE_PARENT_ISOLATION",
        "DISABLE_CHILD_ISOLATION", "DISABLE_ENVIRONMENT_SCRUB",
    }:
        text = path.read_text(encoding="utf-8")
        replacements = {
            "DISABLE_BYTECODE_GUARD": ("sys.dont_write_bytecode = True", "sys.dont_write_bytecode = False"),
            "DISABLE_PARENT_ISOLATION": ("if not sys.flags.isolated:", "if False:"),
            "DISABLE_CHILD_ISOLATION": (
                'return [sys.executable, "-I", "-B", str(script), *arguments]',
                'return [sys.executable, str(script), *arguments]',
            ),
            "DISABLE_ENVIRONMENT_SCRUB": (
                'result.pop("PYTHONPATH", None)', 'result.get("PYTHONPATH", None)'
            ),
        }
        old, new = replacements[operation]
        if text.count(old) != 1:
            raise ValueError(f"static isolation fixture is not unique for {operation}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif operation in {"PYYAML_DRIFT", "PYTHON_MINIMUM_DRIFT", "DEPENDENCY_MISSING", "DEPENDENCY_EXTRA"}:
        value = json.loads(path.read_text(encoding="utf-8"))
        if operation == "PYYAML_DRIFT":
            value["python"]["third_party"] = ["PyYAML==9.9.9"]
        elif operation == "PYTHON_MINIMUM_DRIFT":
            value["python"]["minimum"] = "9.9"
        elif operation == "DEPENDENCY_MISSING":
            del value["dependencies"]["P40_DA_REPORT"]
        else:
            value["dependencies"]["EXTRA"] = {"path": "x", "sha256": "0" * 64}
        path.write_bytes(canonical(value))
    elif operation == "BYTE_SUBSTITUTION":
        path.write_bytes(b"not-base64-or-frozen-bytes\n")
    elif operation == "VALID_BASE64_SUBSTITUTION":
        path.write_bytes(b64encode(b"changed decoded skill\n") + b"\n")
    else:
        raise KeyError(operation)


def hash_manifest(root: Path) -> bytes:
    paths = sorted(path.relative_to(root).as_posix() for path in root.rglob("*")
                   if path.is_file() and path.relative_to(root).as_posix() != MANIFEST_REL)
    return "".join(f"{digest((root / relative).read_bytes())}  {relative}\n" for relative in paths).encode("utf-8")


def seal_route_file(root: Path, commit: str = DUMMY) -> None:
    path = root / ROUTE_REL
    route = yaml.safe_load(path.read_text(encoding="ascii"))
    make_sealed(route, commit)
    path.write_bytes(yaml.safe_dump(route, sort_keys=False, allow_unicode=False, width=100).encode("ascii"))


def mutate_hash_lines(path: Path, operation: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    zero = "0" * 64
    if operation.endswith("MISSING") or operation.endswith("MISSING_ROW"):
        lines.pop(0)
    elif operation.endswith("EXTRA") or operation.endswith("EXTRA_ROW"):
        lines.append(f"{zero}  results/__unregistered__.json")
    elif operation.endswith("UNSAFE_PARENT"):
        lines.append(f"{zero}  ../escape")
    elif operation.endswith("ABSOLUTE"):
        lines.append(f"{zero}  /absolute")
    elif operation.endswith("DUPLICATE"):
        lines.append(lines[0])
    elif operation.endswith("UNSORTED"):
        lines.reverse()
    elif operation.endswith("SELF"):
        self_relative = MANIFEST_REL if path.name == MANIFEST_REL else path.relative_to(path.parents[1]).as_posix()
        lines.append(f"{zero}  {self_relative}")
    elif operation == "LEDGER_ROUTE":
        lines.append(f"{zero}  {ROUTE_REL}")
    elif operation == "LEDGER_MANIFEST":
        lines.append(f"{zero}  {MANIFEST_REL}")
    elif operation.endswith("BAD_HASH"):
        parts = lines[0].split("  ", 1)
        lines[0] = f"{zero}  {parts[1]}"
    else:
        raise KeyError(operation)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def refresh_ledger_hash(root: Path, relative: str) -> None:
    ledger = root / "results/SHA256SUMS.txt"
    lines = ledger.read_text(encoding="utf-8").splitlines()
    suffix = "  " + relative
    matches = [index for index, line in enumerate(lines) if line.endswith(suffix)]
    if len(matches) != 1:
        raise ValueError(f"coordinated ledger row not unique: {relative}")
    lines[matches[0]] = f"{digest((root / relative).read_bytes())}  {relative}"
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")


def apply_audit_mutation(root: Path, row: dict[str, Any]) -> None:
    operation = row["operation"]
    if operation.startswith("ROUTE_"):
        path = root / ROUTE_REL
        raw = path.read_bytes()
        route = yaml.safe_load(raw.decode("ascii"))
        if operation == "ROUTE_SOURCE_CLOCK_DRIFT":
            route["source_lock"]["clock"] += "_DRIFT"
        elif operation == "ROUTE_A2_METRIC_VALUE_DRIFT":
            route["a2"]["metrics"]["control_margin"] += "_DRIFT"
        elif operation == "ROUTE_A2_METRIC_TYPE_DRIFT":
            route["a2"]["metrics"]["control_margin"] = 999
        elif operation == "ROUTE_ARTIFACT_SAFE_EXISTING_SWAP":
            route["a0"]["artifacts"][2] = "results/selection_resolver.json"
        elif operation == "ROUTE_DUPLICATE_KEY":
            path.write_bytes(raw + b"candidate_id: SD-C43\n")
            return
        elif operation == "ROUTE_TOP_KEY_ORDER":
            first = next(iter(route))
            route[first] = route.pop(first)
        elif operation == "ROUTE_UNSAFE_ARTIFACT":
            route["source_lock"]["artifact_paths"][0] = "../escape"
        elif operation == "ROUTE_LIST_ORDER":
            route["blocking_conditions"].reverse()
        else:
            raise KeyError(operation)
        path.write_bytes(yaml.safe_dump(
            route, allow_unicode=False, default_flow_style=False, sort_keys=False, width=100
        ).encode("ascii"))
        return
    if operation.startswith("COORDINATED_SOURCE_CHRONOLOGY_TYPE_"):
        key = operation.removeprefix("COORDINATED_SOURCE_CHRONOLOGY_TYPE_")
        relative = "results/source_packet.json"
        value = json.loads((root / relative).read_text(encoding="utf-8"))
        current = value["integration_chronology"][key]
        if type(current) is not bool:
            raise ValueError(f"source chronology fixture is not bool: {key}")
        value["integration_chronology"][key] = int(current)
        (root / relative).write_bytes(canonical(value))
        refresh_ledger_hash(root, relative)
        return
    if operation.startswith("COORDINATED_SCIENCE_CHRONOLOGY_TYPE_"):
        key = operation.removeprefix("COORDINATED_SCIENCE_CHRONOLOGY_TYPE_")
        relative = "results/scientific_results.json"
        value = json.loads((root / relative).read_text(encoding="utf-8"))
        current = value["integration_chronology"][key]
        if type(current) is not bool:
            raise ValueError(f"science chronology fixture is not bool: {key}")
        value["integration_chronology"][key] = int(current)
        (root / relative).write_bytes(canonical(value))
        refresh_ledger_hash(root, relative)
        return
    if operation == "COORDINATED_TEXT_WRITER_BOOL_TO_INT":
        relative = "results/exact_text_set.json"
        value = json.loads((root / relative).read_text(encoding="utf-8"))
        if type(value.get("writer_paths_included")) is not bool:
            raise ValueError("text writer fixture is not bool")
        value["writer_paths_included"] = int(value["writer_paths_included"])
        (root / relative).write_bytes(canonical(value))
        refresh_ledger_hash(root, relative)
        return
    if operation == "COORDINATED_REPORT_MUTATION_LEDGER_DRIFT":
        relative = "EXPERIMENT_REPORT.md"
        path = root / relative
        text = path.read_text(encoding="utf-8")
        if text.count('"AUD0001"') != 1:
            raise ValueError("report mutation-ledger fixture is not unique")
        path.write_text(text.replace('"AUD0001"', '"AUD_MUTATED"', 1), encoding="utf-8")
        refresh_ledger_hash(root, relative)
        return
    critical_json_operations = {
        "CRITICAL_ADVERSARIAL_TOTAL_FLOAT": ("results/adversarial_tests.json", lambda value: value.__setitem__("total_mutations", float(value["total_mutations"]))),
        "CRITICAL_ADVERSARIAL_SURVIVORS_DICT": ("results/adversarial_tests.json", lambda value: value.__setitem__("survivors", {})),
        "CRITICAL_ADVERSARIAL_GROUP_SURVIVORS_DICT": ("results/adversarial_tests.json", lambda value: value["groups"]["packet"].__setitem__("survivors", {})),
        "CRITICAL_REPRO_ALL_EQUAL_INT": ("results/reproducibility_certificate.json", lambda value: value.__setitem__("all_equal", int(value["all_equal"]))),
        "CRITICAL_IDEMPOTENCE_CHANGED_BOOL": ("results/idempotence_certificate.json", lambda value: value.__setitem__("changed_paths", False)),
        "CRITICAL_DEPENDENCY_MINIMUM_INT": ("results/dependency_controls.json", lambda value: value.__setitem__("python_minimum_satisfied", int(value["python_minimum_satisfied"]))),
        "CRITICAL_DEPENDENCY_ISOLATION_INT": ("results/dependency_controls.json", lambda value: value["interpreter_isolation"].__setitem__("canonical_parent_explicit_I_B", 1)),
        "CRITICAL_EXTERNAL_TREE_READ_INT": ("results/external_provenance_stability.json", lambda value: value.__setitem__("external_historical_tree_read", 0)),
        "CRITICAL_STORED_AUDIT_STATUS": ("results/integrity_audit.json", lambda value: value.__setitem__("status", "MUTATED")),
        "CRITICAL_SEALED_CERT_BOOL_INT": ("results/sealed_state_compatibility.json", lambda value: value.__setitem__("stdout_byte_identical", 1)),
        "CRITICAL_TOP_MAIN_SCHEMA": ("results/main_evaluation.json", lambda value: value.__setitem__("schema", "MUTATED")),
        "CRITICAL_ROUTE_CERT_BOOL_INT": ("results/route_schema_certificate.json", lambda value: value.__setitem__("tuple_agreement", 1)),
        "CRITICAL_SELECTION_SURVIVOR_DUPLICATE": ("results/selection_resolver.json", lambda value: value["survivors"].append(value["survivors"][0])),
        "CRITICAL_ANALYSIS_MUTATION_SURVIVORS_BOOL": ("results/analysis_summary.json", lambda value: value.__setitem__("mutation_survivors", False)),
        "CRITICAL_IMMUTABLE_STATUS": ("results/immutable_inputs.json", lambda value: value.__setitem__("status", "MUTATED")),
        "CRITICAL_INTEGRITY_MANAGED_FLOAT": ("results/integrity_contract.json", lambda value: value.__setitem__("managed_path_count", float(value["managed_path_count"]))),
        "CRITICAL_TRANSACTION_CONTROL_BOOL_INT": (
            "results/integrity_contract.json",
            lambda value: value["static_gate"]["transactional_preinstall_control"].__setitem__(
                "forced_failure_observed", 1
            ),
        ),
        "CRITICAL_BOUNDARY_MINIMAL_BOOL_INT": ("results/source_evaluator_boundary.json", lambda value: value["minimal_packet_runtime"].__setitem__("no_contracts_docs_or_source_present", 1)),
        "CRITICAL_COLD_RELOCATED_INT": ("results/cold_copy_certificate.json", lambda value: value.__setitem__("relocated", 1)),
        "CRITICAL_MAIN_ROUTE_COUNT_FLOAT": ("results/route_evaluation.json", lambda value: value.__setitem__("check_count", float(value["check_count"]))),
        "CRITICAL_INDEPENDENT_ROUTE_STATE": ("evaluations/route_a/SD-C43/independent_evaluation.json", lambda value: value.__setitem__("paired_state", "MUTATED")),
        "CRITICAL_RESEARCH_UNIVERSAL_BOOL_INT": ("results/research_reproduction.json", lambda value: value.__setitem__("universal_no_go_claimed", 0)),
        "CRITICAL_SOURCE_MATCHES_FLOAT": ("results/source_resolver.json", lambda value: value.__setitem__("matches", float(value["matches"]))),
    }
    if operation in critical_json_operations:
        relative, mutate = critical_json_operations[operation]
        path = root / relative
        value = json.loads(path.read_text(encoding="utf-8"))
        mutate(value)
        path.write_bytes(canonical(value))
        refresh_ledger_hash(root, relative)
        return
    if operation == "CRITICAL_RUN_B_SOURCE_BYTE_DRIFT":
        relative = "results/runs/B/source_packet.json"
        path = root / relative
        value = json.loads(path.read_text(encoding="utf-8"))
        value["__coordinated_run_mutation__"] = True
        path.write_bytes(canonical(value))
        refresh_ledger_hash(root, relative)
        return
    if operation == "IMMUTABLE_PACKAGE_DELETE_DECLARED":
        (root / "preauthority/SOURCE_LOCK.md").unlink()
        return
    if operation == "IMMUTABLE_PACKAGE_ADD_EXTRA":
        (root / "preauthority/__audit_extra__.txt").write_text("mutation\n", encoding="utf-8")
        return
    if operation.startswith("IMMUTABLE_PACKAGE_MANIFEST_"):
        path = root / "preauthority/SHA256SUMS.txt"
        lines = path.read_text(encoding="utf-8").splitlines()
        if operation.endswith("BAD_HASH"):
            lines[0] = "0" * 64 + "  " + lines[0].split("  ", 1)[1]
        elif operation.endswith("REORDER"):
            lines.reverse()
        elif operation.endswith("DUPLICATE"):
            lines.append(lines[0])
        else:
            raise KeyError(operation)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return
    if operation.startswith("IMMUTABLE_RESEARCH_LOCK_"):
        path = root / "preauthority/RESEARCH_LOCK.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        mapping = value["immutable_package_files"]
        first = sorted(mapping)[0]
        if operation.endswith("MISSING"):
            del mapping[first]
        elif operation.endswith("EXTRA"):
            mapping["__audit_extra__.txt"] = "0" * 64
        elif operation.endswith("BAD_HASH"):
            mapping[first] = "0" * 64
        else:
            raise KeyError(operation)
        path.write_bytes(canonical(value))
        return
    if operation == "IMMUTABLE_DA_REPORT_DELETE":
        (root / "independent_da/paper41_DA_REPORT_v2.md").unlink()
        return
    if operation == "IMMUTABLE_DA_REPORT_BYTE":
        path = root / "independent_da/paper41_DA_REPORT_v2.md"
        path.write_bytes(path.read_bytes() + b"mutation\n")
        return
    if operation == "IMMUTABLE_DA_SIDECAR_BYTE":
        path = root / "independent_da/paper41_DA_REPORT_v2.sha256"
        path.write_bytes(path.read_bytes() + b"mutation\n")
        return
    if operation == "IMMUTABLE_DA_ADD_EXTRA":
        (root / "independent_da/__audit_extra__.txt").write_text("mutation\n", encoding="utf-8")
        return
    path = path_from_row(root, row)
    manifest_ops = operation.startswith("MANIFEST_")
    state_ops = operation.startswith("SEALED_") or operation == "PRESENT_WITH_PENDING_ROUTE"
    if manifest_ops:
        seal_route_file(root)
        (root / MANIFEST_REL).write_bytes(hash_manifest(root))
        if operation == "MANIFEST_MALFORMED_FORMAT":
            (root / MANIFEST_REL).write_bytes(b"malformed\n")
        elif operation == "MANIFEST_CR_FORMAT":
            (root / MANIFEST_REL).write_bytes((root / MANIFEST_REL).read_bytes().replace(b"\n", b"\r\n", 1))
        else:
            mutate_hash_lines(root / MANIFEST_REL, operation)
        return
    if operation == "PRESENT_WITH_PENDING_ROUTE":
        (root / MANIFEST_REL).write_bytes(hash_manifest(root))
        return
    if operation == "SEALED_ROUTE_WITHOUT_MANIFEST":
        seal_route_file(root)
        return
    if state_ops:
        seal_route_file(root)
        (root / MANIFEST_REL).write_bytes(hash_manifest(root))
        route = yaml.safe_load((root / ROUTE_REL).read_text(encoding="ascii"))
        if operation == "SEALED_TRIPLE_MISMATCH":
            route["code_commit"] = "1" * 40
        elif operation == "SEALED_UPPERCASE":
            make_sealed(route, DUMMY.upper())
        elif operation == "SEALED_ZERO":
            make_sealed(route, "0" * 40)
        elif operation == "SEALED_STALE_NOTE":
            route["freeze_note"] = "stale"
        else:
            raise KeyError(operation)
        (root / ROUTE_REL).write_bytes(yaml.safe_dump(route, sort_keys=False, allow_unicode=False, width=100).encode("ascii"))
        return
    if operation == "DELETE_FILE":
        path.unlink()
    elif operation == "ADD_FILE":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"mutation\n")
    elif operation.startswith("RESULT_DECLARATION_") or operation.startswith("TEXT_DECLARATION_"):
        value = json.loads(path.read_text(encoding="utf-8"))
        key = "paths" if operation.startswith("RESULT_") else "managed_paths"
        if operation.endswith("MISSING"):
            value[key].pop(0)
        elif operation.endswith("EXTRA"):
            value[key].append("results/__unregistered__.json")
        elif operation.endswith("DUPLICATE"):
            value[key].append(value[key][0])
        elif operation.endswith("UNSORTED"):
            value[key].reverse()
        elif operation.endswith("WRITER"):
            value[key].append("main.tex")
        else:
            raise KeyError(operation)
        path.write_bytes(canonical(value))
    elif operation.startswith("LEDGER_"):
        if operation == "LEDGER_MALFORMED_FORMAT":
            path.write_bytes(b"malformed\n")
        elif operation == "LEDGER_CR_FORMAT":
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n", 1))
        else:
            mutate_hash_lines(path, operation)
    elif operation == "REPLACE_WITH_SYMLINK":
        path.unlink()
        path.symlink_to("independent_evaluation.json")
    elif operation == "ADD_CACHE":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"mutation")
    elif operation == "ADD_TRAILING_SPACE":
        path.write_bytes(path.read_bytes() + b"trailing \n")
    elif operation == "ADD_CR":
        path.write_bytes(path.read_bytes() + b"carriage\r\n")
    elif operation == "ADD_NUL":
        path.write_bytes(path.read_bytes() + b"nul\x00\n")
    elif operation == "REMOVE_FINAL_LF":
        path.write_bytes(path.read_bytes().rstrip(b"\n"))
    elif operation == "ADD_HOST_ABSOLUTE_TOKEN":
        path.write_bytes(path.read_bytes() + b"/" + b"root/private/host/path\n")
    elif operation.startswith("CHRONOLOGY_REPORT_FIELD_"):
        key = operation.removeprefix("CHRONOLOGY_REPORT_FIELD_")
        chronology = json.loads((root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(encoding="utf-8"))["integration_chronology"]
        old = json.dumps(chronology[key], ensure_ascii=True)
        new = json.dumps(value_drift(chronology[key]), ensure_ascii=True)
        text = path.read_text(encoding="utf-8")
        needle = f'  "{key}": {old}'
        if needle not in text:
            raise ValueError(f"chronology report field not found: {key}")
        path.write_text(text.replace(needle, f'  "{key}": {new}', 1), encoding="utf-8")
    elif operation.startswith("CHRONOLOGY_REPORT_CORRECTION_"):
        index = int(operation.rsplit("_", 1)[1])
        chronology = json.loads((root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(encoding="utf-8"))["integration_chronology"]
        token = chronology["known_corrections"][index]
        text = path.read_text(encoding="utf-8")
        if token not in text:
            raise ValueError(f"chronology correction token not found: {index}")
        path.write_text(text.replace(token, token + "_DRIFT", 1), encoding="utf-8")
    elif operation.startswith("CHRONOLOGY_PROTOCOL_CORRECTION_"):
        index = int(operation.rsplit("_", 1)[1])
        chronology = json.loads((root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(encoding="utf-8"))["integration_chronology"]
        token = chronology["known_corrections"][index]
        text = path.read_text(encoding="utf-8")
        if token not in text:
            raise ValueError(f"chronology protocol correction token not found: {index}")
        path.write_text(text.replace(token, token + "_DRIFT", 1), encoding="utf-8")
    elif operation == "SCIENCE_BYTE_CONTROL_DRIFT":
        value = json.loads(path.read_text(encoding="utf-8"))
        value["science_projection_byte_control"]["cases"]["bool_vs_int"]["rejected"] = False
        path.write_bytes(canonical(value))
    elif operation == "CHRONOLOGY_REPORT_SCIENCE_REPAIR_QUALIFIER":
        text = path.read_text(encoding="utf-8")
        token = "post-result scientific/model repair is used"
        if token not in text:
            raise ValueError("qualified post-result repair statement not found")
        path.write_text(text.replace(token, "post-result repair is used", 1), encoding="utf-8")
    elif operation == "CHRONOLOGY_PROTOCOL_STATUS":
        chronology = json.loads((root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(encoding="utf-8"))["integration_chronology"]
        token = chronology["status"]
        text = path.read_text(encoding="utf-8")
        if token not in text:
            raise ValueError("chronology protocol status token not found")
        path.write_text(text.replace(token, "MUTATED_CHRONOLOGY_STATUS"), encoding="utf-8")
    else:
        raise KeyError(operation)


def group_result(rows: list[dict[str, Any]], executed: list[dict[str, Any]]) -> dict[str, Any]:
    identifiers = [row["id"] for row in rows]
    if [row["id"] for row in executed] != identifiers:
        raise ValueError("executed mutation ledger differs from registry")
    return {
        "count": len(rows),
        "id_sha256": digest("".join(identifier + "\n" for identifier in identifiers).encode("ascii")),
        "rows": executed,
        "survivors": [],
    }


def execution_row(row: dict[str, Any], **decisions: bool) -> dict[str, Any]:
    return {
        **decisions,
        "expected_rejection": row["expected_rejection"],
        "id": row["id"],
        "json_pointer": row["json_pointer"],
        "operation": row["operation"],
    }


def run(packet_path: Path, route_path: Path, project_root: Path) -> dict[str, Any]:
    packet = json.loads(packet_path.read_text(encoding="ascii"))
    route = yaml.safe_load(route_path.read_text(encoding="ascii"))
    if not isinstance(route, dict):
        raise ValueError("base Route is not a mapping")
    registry = load_registry(route)
    registered_type_rows = [row for row in registry["packet_mutations"] if row["id"].startswith("PTYPE")]
    if registered_type_rows != generate_packet_type_rows(packet):
        raise ValueError("registered packet numeric-equivalent type rows differ from canonical enumeration")
    registered_chronology_rows = [
        row for row in registry["packet_mutations"] if row["id"].startswith("PCHRON")
    ]
    if registered_chronology_rows != generate_packet_chronology_rows(packet):
        raise ValueError("registered packet chronology rows differ from final chronology")
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    registered_audit_chronology = [
        row for row in registry["audit_mutations"]
        if row["id"].startswith("ACPROT") or row["id"].startswith("ACRPT")
    ]
    if registered_audit_chronology != generate_audit_chronology_rows(contract):
        raise ValueError("registered report/protocol chronology rows differ from final chronology")
    groups: dict[str, dict[str, Any]] = {}

    with tempfile.TemporaryDirectory(prefix="paper41_mutations_") as temp_name:
        temp = Path(temp_name)
        packet_executed: list[dict[str, Any]] = []
        for row in registry["packet_mutations"]:
            value = copy.deepcopy(packet)
            mutate_packet(value, row)
            path = temp / f"{row['id']}.json"
            if row["operation"] == "NONCANONICAL_PACKET_WHITESPACE":
                raw = b" " + canonical(value)
            elif row["operation"] == "NONCANONICAL_PACKET_KEY_ORDER":
                first = next(iter(value))
                value[first] = value.pop(first)
                raw = (json.dumps(value, indent=2, sort_keys=False, ensure_ascii=True) + "\n").encode("ascii")
            else:
                raw = canonical(value)
            path.write_bytes(raw)
            expected = row["expected_rejection"]
            assert_evaluator_rejection(isolated_python(MAIN, str(path)), expected["main"], ROOT)
            assert_evaluator_rejection(isolated_python(INDEPENDENT, str(path)), expected["independent"], ROOT)
            packet_executed.append(execution_row(row, independent_rejects=True, main_rejects=True))
        groups["packet"] = group_result(registry["packet_mutations"], packet_executed)

        selection_executed: list[dict[str, Any]] = []
        for row in registry["selection_mutations"]:
            value = copy.deepcopy(packet)
            if row["target"] == "selection":
                mutate_selection(value, row)
            elif row["target"] == "packet":
                mutate_packet(value, row)
            else:
                raise ValueError(f"unexpected selection-group target: {row['target']}")
            path = temp / f"{row['id']}.json"
            path.write_bytes(canonical(value))
            expected = row["expected_rejection"]
            assert_evaluator_rejection(isolated_python(MAIN, str(path)), expected["main"], ROOT)
            assert_evaluator_rejection(isolated_python(INDEPENDENT, str(path)), expected["independent"], ROOT)
            selection_executed.append(execution_row(row, independent_rejects=True, main_rejects=True))
        groups["selection"] = group_result(registry["selection_mutations"], selection_executed)

        route_executed: list[dict[str, Any]] = []
        sealed_operations = {
            "SEALED_UPPERCASE_COMMIT", "SEALED_ZERO_COMMIT", "SEALED_TRIPLE_MISMATCH", "STALE_STAGE2_NOTE",
            "SEALED_SOURCE_COMMIT_MISMATCH", "SEALED_SOURCE_LOCK_COMMIT_MISMATCH",
        }
        for row in registry["route_mutations"]:
            value = copy.deepcopy(route)
            custom = mutate_route(value, row)
            raw = custom if custom is not None else yaml.safe_dump(
                value, allow_unicode=False, default_flow_style=False, sort_keys=False, width=100
            ).encode("ascii")
            path = temp / f"{row['id']}.yaml"
            path.write_bytes(raw)
            state = "present" if row["operation"] in sealed_operations else "absent"
            expected = row["expected_rejection"]
            duplicate_detail = (
                pointer_tokens(row["json_pointer"])[-1]
                if row["operation"] == "DUPLICATE_YAML_KEY"
                else None
            )
            assert_evaluator_rejection(
                isolated_python(ROUTE_MAIN, "validate", str(path), state), expected["main"], ROOT,
                structured_detail=duplicate_detail,
            )
            assert_evaluator_rejection(
                isolated_python(INDEPENDENT, "--route", str(path), state, str(project_root)),
                expected["independent"], ROOT, structured_detail=duplicate_detail,
            )
            route_executed.append(execution_row(row, independent_rejects=True, main_rejects=True))
        groups["route"] = group_result(registry["route_mutations"], route_executed)

        static_executed: list[dict[str, Any]] = []
        for row in registry["static_mutations"]:
            clone = temp / row["id"]
            shutil.copytree(project_root, clone, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
            apply_static_mutation(clone, row)
            expected = row["expected_rejection"]["auditor"]
            try:
                static_check(clone, contract)
            except MutationRejected as rejection:
                if str(rejection) != expected:
                    raise ValueError(f"wrong static rejection for {row['id']}: {rejection}; expected {expected}")
            else:
                raise ValueError(f"static mutation survived: {row['id']}")
            static_executed.append(execution_row(row, auditor_rejects=True))
            shutil.rmtree(clone)
        groups["static"] = group_result(registry["static_mutations"], static_executed)

        baseline = subprocess.run(
            isolated_python(project_root / AUDITOR_REL, str(project_root)), cwd=ROOT,
            env=environment(), capture_output=True, check=False,
        )
        if baseline.returncode != 0 or baseline.stderr or not baseline.stdout:
            raise ValueError(f"audit mutation baseline is not accepted: {baseline.stderr.decode(errors='replace')!r}")
        audit_executed: list[dict[str, Any]] = []
        for row in registry["audit_mutations"]:
            clone = temp / row["id"]
            shutil.copytree(project_root, clone, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
            apply_audit_mutation(clone, row)
            expected = row["expected_rejection"]["auditor"]
            assert_audit_rejection(isolated_python(clone / AUDITOR_REL, str(clone)), expected, ROOT)
            audit_executed.append(execution_row(row, auditor_rejects=True))
            shutil.rmtree(clone)
        groups["audit"] = group_result(registry["audit_mutations"], audit_executed)

    dual_count = 2 * sum(groups[name]["count"] for name in ("packet", "selection", "route"))
    all_ids = sorted(
        row["id"]
        for name in ("packet_mutations", "selection_mutations", "route_mutations",
                     "static_mutations", "audit_mutations")
        for row in registry[name]
    )
    return {
        "audit_rejections": groups["audit"]["count"],
        "dual_rejections": dual_count,
        "groups": groups,
        "mutation_ids": all_ids,
        "mutation_ids_sha256": digest("".join(item + "\n" for item in all_ids).encode("ascii")),
        "registry_sha256": REGISTRY_SHA256,
        "schema": "paper41-adversarial-mutation-results-v2",
        "static_rejections": groups["static"]["count"],
        "survivors": [],
        "total_mutations": len(all_ids),
    }


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: run_tests.py PACKET.json ROUTE.yaml PROJECT_ROOT", file=sys.stderr)
        return 2
    try:
        result = run(Path(argv[1]), Path(argv[2]), Path(argv[3]).resolve())
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
