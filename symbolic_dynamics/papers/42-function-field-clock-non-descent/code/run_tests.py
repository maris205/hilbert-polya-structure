#!/usr/bin/env python3
"""Execute the frozen Paper 42 mutation registry with exact rejection envelopes."""

from __future__ import annotations

import copy
import base64
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_REL = "code/contracts/MUTATION_REGISTRY.json"
REGISTRY_SHA256 = "3056749e0a026a33ed0d9aa517c5deb8414f2bd7a6464998413e033b0d31c7e6"
CONTRACT_REL = "code/contracts/INTEGRATION_CONTRACT.json"
MAIN_REL = "code/evaluator/evaluate_packet.py"
INDEPENDENT_REL = "code/evaluator/independent_evaluator.py"
ROUTE_MAIN_REL = "code/evaluator/evaluate_route_a.py"
AUDITOR_REL = "code/audit_integrity.py"
ROUTE_REL = "evaluations/route_a/SD-C44/2026-08-17.yaml"
LEDGER_REL = "results/SHA256SUMS.txt"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
DUMMY_COMMIT = "0123456789abcdef0123456789abcdef01234567"


def stage1_note() -> str:
    return (
        "State A authority artifact has source_commit, code_commit, and "
        "source_lock.code_commit equal to PENDING_FIRST_ARTIFACT_COMMIT and no "
        "PAPER_MANIFEST.sha256. State B is metadata-only: one identical lowercase "
        "nonzero 40-hex State-A commit replaces those three fields and a C-sorted "
        "self-excluding PAPER_MANIFEST.sha256 is added."
    )


def sealed_note(commit: str) -> str:
    return (
        f"State A artifact commit {commit} contained the three "
        "PENDING_FIRST_ARTIFACT_COMMIT fields and no PAPER_MANIFEST.sha256. "
        "State B is metadata-only: source_commit, code_commit, and "
        "source_lock.code_commit are sealed to that same commit and the "
        "C-sorted self-excluding PAPER_MANIFEST.sha256 is added."
    )


def as_state_b(value: dict[str, Any], commit: str = DUMMY_COMMIT) -> None:
    value["source_commit"] = commit
    value["code_commit"] = commit
    value["source_lock"]["code_commit"] = commit
    value["freeze_note"] = sealed_note(commit)
    value["authority_integration"]["paired_state"] = "STATE_B"
    value["authority_integration"]["status"] = "SEALED_METADATA_ONLY_STATE_B"


def route_special_contract() -> set[tuple[str, str, str]]:
    """Exact non-recursive Route controls promised by the paired-state contract."""
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


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def parse_hash_bytes(raw: bytes) -> tuple[list[tuple[str, str]], bool]:
    try:
        lines = raw.decode("ascii").splitlines()
    except Exception:
        return [], False
    rows: list[tuple[str, str]] = []
    valid = True
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64 \
                or any(character not in "0123456789abcdef" for character in parts[0]):
            valid = False
            continue
        rows.append((parts[0], parts[1]))
    return rows, valid


def environment() -> dict[str, str]:
    value = os.environ.copy()
    value.pop("PYTHONPATH", None)
    value.pop("PYTHONHOME", None)
    value.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1"})
    return value


def python(script: Path, *arguments: str) -> list[str]:
    return [sys.executable, "-I", "-B", str(script), *arguments]


def exact_reject(arguments: list[str], expected: str, cwd: Path) -> None:
    completed = subprocess.run(arguments, cwd=cwd, env=environment(), capture_output=True, check=False)
    if completed.returncode != 2 or completed.stdout or completed.stderr != expected.encode("utf-8"):
        raise RuntimeError(
            "exact rejection differs: "
            f"rc={completed.returncode}; stdout={completed.stdout!r}; "
            f"expected={expected!r}; stderr={completed.stderr!r}"
        )


def tokens(pointer: str) -> list[str]:
    if pointer in {"", "/"}:
        return []
    if not pointer.startswith("/"):
        raise ValueError("invalid RFC6901 pointer")
    return [item.replace("~1", "/").replace("~0", "~") for item in pointer[1:].split("/")]


def resolve(value: Any, pointer: str) -> Any:
    current = value
    for token in tokens(pointer):
        current = current[int(token)] if type(current) is list else current[token]
    return current


def parent_key(value: Any, pointer: str) -> tuple[Any, str]:
    parts = tokens(pointer)
    if not parts:
        raise ValueError("root has no parent")
    current = value
    for token in parts[:-1]:
        current = current[int(token)] if type(current) is list else current[token]
    return current, parts[-1]


def replace(value: Any, pointer: str, replacement: Any) -> None:
    parent, key = parent_key(value, pointer)
    if type(parent) is list:
        parent[int(key)] = replacement
    else:
        parent[key] = replacement


def drift(value: Any) -> Any:
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "_MUTATED"
    raise ValueError("VALUE_DRIFT requires a scalar")


def type_drift(value: Any) -> Any:
    if type(value) is bool:
        return int(value)
    if type(value) is int:
        return float(value)
    if type(value) is str:
        return 17
    raise ValueError("TYPE_DRIFT requires a scalar")


def apply_recursive(value: Any, pointer: str, operation: str) -> None:
    if operation == "EXTRA_KEY":
        target = resolve(value, pointer)
        if type(target) is not dict:
            raise ValueError("EXTRA_KEY target is not a mapping")
        target["__mutation_extra__"] = True
    elif operation == "KEY_DELETION":
        parent, key = parent_key(value, pointer)
        if type(parent) is list:
            del parent[int(key)]
        else:
            del parent[key]
    elif operation == "MEMBER_DELETION":
        target = resolve(value, pointer)
        del target[0]
    elif operation == "MEMBER_DUPLICATION":
        target = resolve(value, pointer)
        target.append(copy.deepcopy(target[0]))
    elif operation == "ORDER_REVERSAL":
        resolve(value, pointer).reverse()
    elif operation == "VALUE_DRIFT":
        replace(value, pointer, drift(resolve(value, pointer)))
    elif operation == "VALUE_AND_TYPE_DRIFT":
        replace(value, pointer, type_drift(resolve(value, pointer)))
    else:
        raise ValueError(f"unsupported recursive operation: {operation}")


def load_registry(route: dict[str, Any], packet: dict[str, Any]) -> dict[str, Any]:
    path = ROOT / REGISTRY_REL
    raw = path.read_bytes()
    if REGISTRY_SHA256 and digest(raw) != REGISTRY_SHA256:
        raise RuntimeError("mutation registry byte seal differs")
    value = json.loads(raw)
    if type(value) is not dict or value.get("schema") != "paper42-exhaustive-mutation-registry-v1":
        raise RuntimeError("mutation registry schema differs")
    expected = {"schema", "packet_mutations", "selection_mutations", "route_mutations", "static_mutations", "audit_mutations"}
    if set(value) != expected:
        raise RuntimeError("mutation registry group set differs")
    all_ids: list[str] = []
    for group in sorted(expected - {"schema"}):
        rows = value[group]
        ids = [row["id"] for row in rows]
        if ids != sorted(set(ids)):
            raise RuntimeError(f"{group} IDs are not sorted and unique")
        for row in rows:
            if set(row) != {"expected_rejection", "id", "json_pointer", "operation", "target"}:
                raise RuntimeError(f"registry row shape differs: {row.get('id')}")
            tokens(row["json_pointer"])
        all_ids.extend(ids)
    if len(all_ids) != len(set(all_ids)):
        raise RuntimeError("mutation IDs collide across groups")
    route_pointers = {
        (row["json_pointer"], row["operation"])
        for row in value["route_mutations"] if row["id"].startswith("RSEM")
    }
    if route_pointers != recursive_pointer_operations(route, skip_provenance=True):
        raise RuntimeError("Route registry is not the full recursive canonical enumeration")
    route_specials = {
        (row["id"], row["json_pointer"], row["operation"])
        for row in value["route_mutations"] if not row["id"].startswith("RSEM")
    }
    if route_specials != route_special_contract():
        raise RuntimeError("Route raw/paired-state special registry differs")
    packet_recursive = recursive_pointer_operations(packet)
    expected_selection = {
        item for item in packet_recursive if item[0].startswith("/raw_selection_cards")
    }
    expected_packet = packet_recursive - expected_selection
    actual_packet = {
        (row["json_pointer"], row["operation"])
        for row in value["packet_mutations"] if row["id"].startswith("PKT")
    }
    actual_selection = {
        (row["json_pointer"], row["operation"])
        for row in value["selection_mutations"] if row["id"].startswith("SEL")
    }
    if actual_packet != expected_packet:
        raise RuntimeError("packet registry is not the full recursive canonical partition")
    if actual_selection != expected_selection:
        raise RuntimeError("selection registry is not the full recursive canonical partition")
    packet_specials = {
        (row["id"], row["json_pointer"], row["operation"])
        for row in value["packet_mutations"] if row["id"].startswith("PRAW")
    }
    if packet_specials != {
        ("PRAW0001", "/", "NONCANONICAL_WHITESPACE"),
        ("PRAW0002", "/", "DUPLICATE_TOP_KEY"),
        ("PRAW0003", "/", "RAW_KEY_ORDER_SWAP"),
        ("PRAW0004", "/", "DUPLICATE_NESTED_KEY"),
    }:
        raise RuntimeError("packet raw-special registry differs")
    packet_semantics = {
        (row["id"], row["json_pointer"], row["operation"])
        for row in value["packet_mutations"] if row["id"].startswith("PSEM")
    }
    selection_semantics = {
        (row["id"], row["json_pointer"], row["operation"])
        for row in value["selection_mutations"] if row["id"].startswith("SSEM")
    }
    if packet_semantics != packet_semantic_contract() \
            or selection_semantics != selection_semantic_contract():
        raise RuntimeError("packet/selection semantic-lane registry differs")
    chronology_semantics = {
        (row["id"], row["json_pointer"], row["operation"])
        for row in value["packet_mutations"] if row["id"].startswith("PCHR")
    }
    if chronology_semantics != chronology_semantic_contract(packet):
        raise RuntimeError("chronology semantic-lane registry differs")
    structural_specials = {
        (row["id"], row["json_pointer"], row["operation"])
        for group in ("packet_mutations", "selection_mutations")
        for row in value[group] if "STRUCT" in row["id"]
    }
    if structural_specials != structural_special_contract():
        raise RuntimeError("packet/selection structural-special registry differs")
    return value


def reanchored_evaluator_paths(temp: Path, packet_hash: str) -> tuple[Path, Path]:
    directory = temp / ("semantic_evaluators_" + packet_hash[:16])
    # Distinct registered controls may intentionally produce identical packet
    # bytes (for example a general chronology leaf and its named semantic
    # control). Reuse the byte-addressed evaluator fixture deterministically.
    directory.mkdir(exist_ok=True)
    main = directory / "evaluate_packet.py"
    independent = directory / "independent_evaluator.py"
    baseline_hash = digest(canonical(json.loads((temp / "baseline_packet.json").read_bytes())))
    main_text = (ROOT / MAIN_REL).read_text(encoding="utf-8").replace(
        f'EXPECTED_PACKET_SHA256 = "{baseline_hash}"',
        f'EXPECTED_PACKET_SHA256 = "{packet_hash}"',
        1,
    )
    independent_text = (ROOT / INDEPENDENT_REL).read_text(encoding="utf-8").replace(
        f'PACKET_SHA = "{baseline_hash}"',
        f'PACKET_SHA = "{packet_hash}"',
        1,
    )
    if f'EXPECTED_PACKET_SHA256 = "{packet_hash}"' not in main_text \
            or f'PACKET_SHA = "{packet_hash}"' not in independent_text:
        raise RuntimeError("semantic evaluator packet re-anchor substitution failed")
    main.write_text(main_text, encoding="utf-8")
    independent.write_text(independent_text, encoding="utf-8")
    return main, independent


def recursive_pointer_operations(value: Any, *, skip_provenance: bool = False) -> set[tuple[str, str]]:
    rows: set[tuple[str, str]] = set()
    skipped = {"/source_commit", "/code_commit", "/source_lock/code_commit", "/freeze_note"} if skip_provenance else set()

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


def group_result(rows: list[dict[str, Any]], executed: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [row["id"] for row in rows]
    if [row["id"] for row in executed] != ids:
        raise RuntimeError("executed mutation order differs")
    return {
        "count": len(rows),
        "id_sha256": digest("".join(item + "\n" for item in ids).encode("ascii")),
        "rows": executed,
        "survivors": [],
    }


def result_row(row: dict[str, Any], **decisions: bool) -> dict[str, Any]:
    return {
        **decisions,
        "expected_rejection": row["expected_rejection"],
        "id": row["id"],
        "json_pointer": row["json_pointer"],
        "operation": row["operation"],
    }


def static_inventory(root: Path) -> list[str]:
    return sorted(
        (["RESEARCH_LOCK.json"] if (root / "RESEARCH_LOCK.json").is_file()
         and not (root / "RESEARCH_LOCK.json").is_symlink() else [])
        + [
            path.relative_to(root).as_posix()
            for top in ("code", "docs", "experiments")
            for path in (root / top).rglob("*")
            if path.is_file() and not path.is_symlink()
        ]
    )


def apply_static(root: Path, row: dict[str, Any]) -> None:
    operation = row["operation"]
    pointer = row["json_pointer"]
    relative = tokens(pointer)[0] if pointer not in {"", "/"} else ""
    path = root / relative
    if operation == "FILE_DELETION":
        path.unlink()
    elif operation == "EXTRA_FILE":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"mutation\n")
    elif operation == "STATIC_SYMLINK":
        path.symlink_to("missing-static-target")
    else:
        raise ValueError(f"unsupported static operation: {operation}")


def static_rejection(root: Path, contract: dict[str, Any]) -> str | None:
    if static_inventory(root) != contract["owned_paths"]["static"]:
        return "STATIC_EXACT_SET"
    if any(path.is_symlink() for path in root.rglob("*")):
        return "STATIC_SYMLINK"
    return None


def refresh_ledger(root: Path, relative: str) -> None:
    ledger = root / LEDGER_REL
    rows = []
    found = False
    for line in ledger.read_text(encoding="ascii").splitlines():
        old, path = line.split("  ", 1)
        if path == relative:
            old = digest((root / relative).read_bytes())
            found = True
        rows.append((old, path))
    if not found:
        raise RuntimeError(f"ledger has no row for {relative}")
    ledger.write_text("".join(f"{value}  {path}\n" for value, path in rows), encoding="ascii")


def hash_rows_for_tree(root: Path) -> list[tuple[str, str]]:
    return [
        (digest(path.read_bytes()), path.relative_to(root).as_posix())
        for path in root.rglob("*")
        if path.is_file() and not path.is_symlink()
        and path.relative_to(root).as_posix() != "PAPER_MANIFEST.sha256"
    ]


def write_hash_rows(path: Path, rows: list[tuple[str, str]]) -> None:
    path.write_bytes("".join(f"{value}  {relative}\n" for value, relative in rows).encode("ascii"))


def make_state_b(root: Path) -> None:
    route_path = root / ROUTE_REL
    route = yaml.safe_load(route_path.read_bytes())
    as_state_b(route)
    route_path.write_text(yaml.safe_dump(route, sort_keys=False, width=1000), encoding="ascii")
    write_hash_rows(root / "PAPER_MANIFEST.sha256", sorted(hash_rows_for_tree(root), key=lambda row: row[1]))


def make_final_writer_state(root: Path) -> list[str]:
    sync_text = b"\nCanonical integration result synchronization completed in the separate writer lane.\n"
    for relative in ("PAPER_PLAN.md", "WRITER_HANDOFF.md", "sections/6_route_reproducibility.tex"):
        path = root / relative
        path.write_bytes(path.read_bytes() + sync_text)
    (root / "COMPILATION_REPORT.md").write_bytes(
        b"# Writer compilation report\n\nStatus: simulated exact post-output writer-state control.\n"
    )
    (root / "main.pdf").write_bytes(
        bytes((37, 80, 68, 70, 45)) + b"1.4\n% writer-state control\n"
        + bytes((37, 37, 69, 79, 70)) + b"\n"
    )
    baseline_rows, valid = parse_hash_bytes((root / "WRITER_SHA256SUMS.txt").read_bytes())
    if not valid or len(baseline_rows) != 18:
        raise RuntimeError("writer final-state fixture baseline map differs")
    paths = sorted([relative for _, relative in baseline_rows] + ["COMPILATION_REPORT.md", "main.pdf"])
    write_hash_rows(
        root / "WRITER_SHA256SUMS.txt",
        [(digest((root / relative).read_bytes()), relative) for relative in paths],
    )
    return paths


def refresh_writer_manifest(root: Path, paths: list[str]) -> None:
    write_hash_rows(
        root / "WRITER_SHA256SUMS.txt",
        [(digest((root / relative).read_bytes()), relative) for relative in paths],
    )


def coordinate_check_map_mutation(root: Path, *, independent: bool, operation: str) -> None:
    name = "independent_evaluation.json" if independent else "main_evaluation.json"
    relatives = [f"results/{name}"] + [f"results/runs/{label}/{name}" for label in "ABC"]
    for relative in relatives:
        value = json.loads((root / relative).read_bytes())
        checks = value["checks"]
        first = sorted(checks)[0]
        if operation.endswith("ADD_RELEDGER"):
            checks["audit_gap_probe"] = True
        elif operation.endswith("DELETE_RELEDGER"):
            del checks[first]
        elif operation.endswith("RENAME_RELEDGER"):
            checks[first + "_renamed"] = checks.pop(first)
        else:
            raise ValueError(f"unsupported check-map operation: {operation}")
        (root / relative).write_bytes(canonical(value))
        refresh_ledger(root, relative)
    reproduction_path = root / "results/reproducibility_certificate.json"
    reproduction = json.loads(reproduction_path.read_bytes())
    for label in "ABC":
        reproduction["run_hashes"][label][name] = digest(
            (root / f"results/runs/{label}/{name}").read_bytes()
        )
    reproduction_path.write_bytes(canonical(reproduction))
    refresh_ledger(root, "results/reproducibility_certificate.json")


def writer_state_control(project_root: Path, temp: Path, baseline_stdout: bytes,
                         registry: dict[str, Any]) -> dict[str, Any]:
    clone = temp / "writer_state_control"
    shutil.copytree(project_root, clone, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    sync_text = b"\nCanonical integration result synchronization completed in the separate writer lane.\n"
    for relative in ("PAPER_PLAN.md", "WRITER_HANDOFF.md", "sections/6_route_reproducibility.tex"):
        path = clone / relative
        path.write_bytes(path.read_bytes() + sync_text)
    (clone / "COMPILATION_REPORT.md").write_bytes(
        b"# Writer compilation report\n\nStatus: simulated exact post-output writer-state control.\n"
    )
    (clone / "main.pdf").write_bytes(
        bytes((37, 80, 68, 70, 45)) + b"1.4\n% writer-state control\n" + bytes((37, 37, 69, 79, 70)) + b"\n"
    )
    manifest = clone / "WRITER_SHA256SUMS.txt"
    baseline_rows, valid = parse_hash_bytes(manifest.read_bytes())
    if not valid or len(baseline_rows) != 18:
        raise RuntimeError("writer-state control baseline map differs")
    paths = sorted([relative for _, relative in baseline_rows] + ["COMPILATION_REPORT.md", "main.pdf"])
    manifest.write_bytes("".join(
        f"{digest((clone / relative).read_bytes())}  {relative}\n" for relative in paths
    ).encode("ascii"))
    accepted = subprocess.run(
        python(clone / AUDITOR_REL, str(clone)), cwd=ROOT, env=environment(),
        capture_output=True, check=False,
    )
    if accepted.returncode != 0 or accepted.stderr or accepted.stdout != baseline_stdout:
        raise RuntimeError(f"bounded post-output writer-state control differs: {accepted.stderr!r}")
    by_operation = {row["operation"]: row for row in registry["audit_mutations"]}
    for operation in (
        "WRITER_FINAL_INTEGRATION_STATIC_DRIFT",
        "WRITER_FINAL_UNAUTHORIZED_ABSTRACT_REHASH",
        "WRITER_FINAL_PDF_DELETE",
        "WRITER_FINAL_PDF_SYMLINK",
    ):
        negative = temp / ("writer_state_" + operation.lower())
        shutil.copytree(clone, negative)
        if operation == "WRITER_FINAL_INTEGRATION_STATIC_DRIFT":
            relative = "experiments/EXPERIMENT_PLAN.md"
            target = negative / relative
            target.write_bytes(target.read_bytes() + b"unauthorized integration-owned byte drift\n")
            refresh_ledger(negative, relative)
        elif operation == "WRITER_FINAL_UNAUTHORIZED_ABSTRACT_REHASH":
            target = negative / "sections/0_abstract.tex"
            target.write_bytes(target.read_bytes() + b"unauthorized writer byte drift\n")
            refresh_writer_manifest(negative, paths)
        elif operation == "WRITER_FINAL_PDF_DELETE":
            (negative / "main.pdf").unlink()
        else:
            (negative / "main.pdf").unlink()
            (negative / "main.pdf").symlink_to("missing-writer-pdf")
        codes = by_operation[operation]["expected_rejection"]["auditor"]
        exact_reject(
            python(ROOT / AUDITOR_REL, str(negative)),
            f"FAIL: integrity checks failed: {', '.join(codes)}\n", ROOT,
        )
    return {
        "baseline_audit_accepted": True,
        "final_manifest_entry_count": 20,
        "post_output_sync_audit_accepted": True,
        "final_pdf_deletion_rejected": True,
        "final_pdf_symlink_rejected": True,
        "schema": "paper42-writer-state-control-v1",
        "unauthorized_integration_owned_write_rejected": True,
        "unauthorized_writer_path_rejected": True,
    }


def apply_audit(root: Path, row: dict[str, Any]) -> None:
    operation = row["operation"]
    relative = tokens(row["json_pointer"])[0]
    path = root / relative
    if operation == "OUTPUT_DELETION":
        path.unlink()
    elif operation == "OUTPUT_EXPECTED_RENAME":
        path.rename(path.with_name(path.stem + ".renamed" + path.suffix))
    elif operation in {"OUTPUT_EXPECTED_SYMLINK_EXTERNAL", "ROUTE_EXPECTED_SYMLINK_EXTERNAL"}:
        external = root.parent / (root.name + "_expected_output_external")
        external.mkdir()
        sentinel = external / "sentinel.txt"
        sentinel.write_bytes(b"expected-output external sentinel must never be opened\n")
        path.unlink()
        path.symlink_to(sentinel)
    elif operation == "OUTPUT_EXTRA":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"mutation\n")
    elif operation == "OUTPUT_SYMLINK":
        path.symlink_to("missing-output-target")
    elif operation == "BYTE_DRIFT_RELEDGER":
        path.write_bytes(path.read_bytes() + b"mutation\n")
        refresh_ledger(root, relative)
    elif operation == "JSON_BOOL_TO_INT_RELEDGER":
        value = json.loads(path.read_bytes())
        target = resolve(value, "/" + "/".join(tokens(row["json_pointer"])[1:]))
        if type(target) is not bool:
            raise RuntimeError("audit bool-to-int target is not bool")
        replace(value, "/" + "/".join(tokens(row["json_pointer"])[1:]), int(target))
        path.write_bytes(canonical(value))
        refresh_ledger(root, relative)
    elif operation in {"JSON_INT_TO_FLOAT_RELEDGER", "JSON_INT_TO_BOOL_RELEDGER"}:
        value = json.loads(path.read_bytes())
        inner_pointer = "/" + "/".join(tokens(row["json_pointer"])[1:])
        target = resolve(value, inner_pointer)
        if type(target) is not int:
            raise RuntimeError("audit numeric target is not an int")
        replacement = float(target) if operation == "JSON_INT_TO_FLOAT_RELEDGER" else bool(target)
        replace(value, inner_pointer, replacement)
        path.write_bytes(canonical(value))
        refresh_ledger(root, relative)
    elif operation == "ROUTE_VALUE_DRIFT":
        value = yaml.safe_load(path.read_bytes())
        replace(value, "/" + "/".join(tokens(row["json_pointer"])[1:]), "AUDIT_ROUTE_DRIFT")
        path.write_text(yaml.safe_dump(value, sort_keys=False, width=1000), encoding="ascii")
    elif operation == "IMMUTABLE_BYTE_DRIFT":
        path.write_bytes(path.read_bytes() + b"mutation\n")
    elif operation == "LEDGER_HASH_DRIFT":
        lines = path.read_text(encoding="ascii").splitlines()
        first_hash, first_path = lines[0].split("  ", 1)
        lines[0] = "0" * 64 + "  " + first_path
        path.write_text("\n".join(lines) + "\n", encoding="ascii")
    elif operation in {
        "LEDGER_SELF_INCLUDE", "LEDGER_UNSORTED", "LEDGER_DUPLICATE",
        "LEDGER_OMIT", "LEDGER_UNSAFE_PARENT",
    }:
        rows, valid = parse_hash_bytes(path.read_bytes())
        if not valid:
            raise RuntimeError("ledger fixture format differs")
        if operation == "LEDGER_SELF_INCLUDE":
            rows.append(("0" * 64, LEDGER_REL))
            rows.sort(key=lambda item: item[1])
        elif operation == "LEDGER_UNSORTED":
            rows[0], rows[1] = rows[1], rows[0]
        elif operation == "LEDGER_DUPLICATE":
            rows.insert(1, rows[0])
        elif operation == "LEDGER_OMIT":
            del rows[0]
        elif operation == "LEDGER_UNSAFE_PARENT":
            rows.append(("0" * 64, "../outside"))
        else:
            raise ValueError(f"unsupported ledger operation: {operation}")
        write_hash_rows(path, rows)
    elif operation == "MANIFEST_PRESENT_STAGE_A":
        write_hash_rows(path, sorted(hash_rows_for_tree(root), key=lambda item: item[1]))
    elif operation in {
        "STAGE_B_MANIFEST_ABSENT", "STAGE_B_MANIFEST_SELF_INCLUDE",
        "STAGE_B_MANIFEST_UNSORTED", "STAGE_B_MANIFEST_DUPLICATE",
        "STAGE_B_MANIFEST_OMIT", "STAGE_B_MANIFEST_EXTRA",
        "STAGE_B_MANIFEST_UNSAFE_PARENT", "STAGE_B_MANIFEST_WRONG_HASH",
    }:
        make_state_b(root)
        manifest = root / "PAPER_MANIFEST.sha256"
        if operation == "STAGE_B_MANIFEST_ABSENT":
            manifest.unlink()
        else:
            rows, valid = parse_hash_bytes(manifest.read_bytes())
            if not valid:
                raise RuntimeError("Stage-B manifest fixture format differs")
            if operation == "STAGE_B_MANIFEST_SELF_INCLUDE":
                rows.append(("0" * 64, "PAPER_MANIFEST.sha256"))
                rows.sort(key=lambda item: item[1])
            elif operation == "STAGE_B_MANIFEST_UNSORTED":
                rows[0], rows[1] = rows[1], rows[0]
            elif operation == "STAGE_B_MANIFEST_DUPLICATE":
                rows.insert(1, rows[0])
            elif operation == "STAGE_B_MANIFEST_OMIT":
                del rows[0]
            elif operation == "STAGE_B_MANIFEST_EXTRA":
                rows.append(("0" * 64, "UNDECLARED_MANIFEST_ENTRY"))
                rows.sort(key=lambda item: item[1])
            elif operation == "STAGE_B_MANIFEST_UNSAFE_PARENT":
                rows.append(("0" * 64, "../outside"))
            elif operation == "STAGE_B_MANIFEST_WRONG_HASH":
                rows[0] = ("0" * 64, rows[0][1])
            else:
                raise ValueError(f"unsupported Stage-B manifest operation: {operation}")
            write_hash_rows(manifest, rows)
    elif operation == "PREAUTH_FILE_DELETE":
        path.unlink()
    elif operation == "PREAUTH_NESTED_EXTRA":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"nested immutable namespace mutation\n")
    elif operation.startswith("PACKAGE_MANIFEST_"):
        rows, valid = parse_hash_bytes(path.read_bytes())
        if not valid:
            raise RuntimeError("package manifest fixture format differs")
        if operation == "PACKAGE_MANIFEST_BAD_HASH":
            rows[0] = ("0" * 64, rows[0][1])
        elif operation == "PACKAGE_MANIFEST_REORDER":
            rows[0], rows[1] = rows[1], rows[0]
        elif operation == "PACKAGE_MANIFEST_DUPLICATE":
            rows.insert(1, rows[0])
        else:
            raise ValueError(f"unsupported package manifest operation: {operation}")
        write_hash_rows(path, rows)
    elif operation.startswith("RESEARCH_LOCK_MAPPING_"):
        value = json.loads(path.read_bytes())
        mapping = value["immutable_package_files"]
        first = sorted(mapping)[0]
        if operation == "RESEARCH_LOCK_MAPPING_MISSING":
            del mapping[first]
        elif operation == "RESEARCH_LOCK_MAPPING_EXTRA":
            mapping["UNDECLARED.md"] = "0" * 64
        elif operation == "RESEARCH_LOCK_MAPPING_BAD_HASH":
            mapping[first] = "0" * 64
        else:
            raise ValueError(f"unsupported research-lock operation: {operation}")
        path.write_bytes(canonical(value))
    elif operation == "DA_FILE_DELETE":
        path.unlink()
    elif operation == "DA_FILE_EXTRA":
        path.write_bytes(b"independent audit namespace mutation\n")
    elif operation == "DA_SIDECAR_MISMATCH":
        path.write_bytes(("0" * 64 + "  paper42_DA_REPORT.md\n").encode("ascii"))
    elif operation == "WRITER_BASELINE_DELETE":
        path.unlink()
    elif operation == "WRITER_BASELINE_EXTRA":
        path.write_bytes(b"writer namespace mutation\n")
    elif operation in {
        "WRITER_FINAL_PDF_DELETE", "WRITER_FINAL_PDF_SYMLINK",
        "WRITER_FINAL_UNAUTHORIZED_ABSTRACT_REHASH",
        "WRITER_FINAL_UNAUTHORIZED_REFERENCE_REHASH",
        "WRITER_FINAL_UNAUTHORIZED_FIGURE_REHASH",
    }:
        final_paths = make_final_writer_state(root)
        if operation == "WRITER_FINAL_PDF_DELETE":
            (root / "main.pdf").unlink()
        elif operation == "WRITER_FINAL_PDF_SYMLINK":
            (root / "main.pdf").unlink()
            (root / "main.pdf").symlink_to("missing-writer-pdf")
        else:
            target = {
                "WRITER_FINAL_UNAUTHORIZED_ABSTRACT_REHASH": "sections/0_abstract.tex",
                "WRITER_FINAL_UNAUTHORIZED_REFERENCE_REHASH": "references.bib",
                "WRITER_FINAL_UNAUTHORIZED_FIGURE_REHASH": "figures/repair_ownership.tex",
            }.get(operation)
            if target is None:
                raise ValueError(f"unsupported final-writer operation: {operation}")
            target_path = root / target
            target_path.write_bytes(target_path.read_bytes() + b"unauthorized writer mutation\n")
            refresh_writer_manifest(root, final_paths)
    elif operation.startswith("SOURCE_MANIFEST_"):
        if operation == "SOURCE_MANIFEST_MISSING":
            path.unlink()
        else:
            rows, valid = parse_hash_bytes(path.read_bytes())
            if not valid:
                raise RuntimeError("source manifest fixture format differs")
            if operation == "SOURCE_MANIFEST_DUPLICATE":
                rows.insert(1, rows[0])
            elif operation == "SOURCE_MANIFEST_UNSORTED":
                rows[0], rows[1] = rows[1], rows[0]
            elif operation == "SOURCE_MANIFEST_BAD_HASH":
                rows[0] = ("0" * 64, rows[0][1])
            else:
                replacement = {
                    "SOURCE_MANIFEST_ABSOLUTE_ID": "/absolute/source",
                    "SOURCE_MANIFEST_PARENT_ID": "repo:../parent",
                    "SOURCE_MANIFEST_UNKNOWN_SCHEME": "unknown:source",
                }.get(operation)
                if replacement is None:
                    raise ValueError(f"unsupported source-manifest operation: {operation}")
                rows[0] = (rows[0][0], replacement)
            write_hash_rows(path, rows)
    elif operation == "SNAPSHOT_CONTAINER_EXTRA":
        path.write_bytes(b"YQ==")
    elif operation == "SNAPSHOT_CONTAINER_DELETE":
        path.unlink()
    elif operation == "SNAPSHOT_CONTAINER_SYMLINK":
        path.symlink_to("missing-snapshot")
    elif operation == "SNAPSHOT_ENCODED_BYTE_DRIFT":
        path.write_bytes(path.read_bytes() + b"A")
        refresh_ledger(root, relative)
    elif operation == "SNAPSHOT_DECLARED_DECODED_HASH_DRIFT":
        value = json.loads(path.read_bytes())
        value["snapshot"]["rows"][0]["decoded_sha256"] = "0" * 64
        path.write_bytes(canonical(value))
        refresh_ledger(root, relative)
    elif operation == "ROUTE_SKILL_CONTAINER_CORRUPTION":
        path.write_bytes(path.read_bytes() + b"A")
        refresh_ledger(root, relative)
    elif operation == "DEPENDENCY_LOCK_SEMANTIC_DRIFT":
        value = json.loads(path.read_bytes())
        value["dependencies"]["python_minimum"] = "99.0"
        path.write_bytes(canonical(value))
        refresh_ledger(root, relative)
    elif operation in {
        "SOURCE_IMPORT_EVALUATOR", "SOURCE_DIRECT_READ_EVALUATOR",
        "SOURCE_DYNAMIC_IMPORT_EVALUATOR", "EMITTER_IMPORT_EVALUATOR",
        "MAIN_IMPORT_SOURCE", "MAIN_DIRECT_READ_SOURCE", "MAIN_IMPORT_INDEPENDENT",
        "MAIN_IMPORT_ROUTE", "INDEPENDENT_IMPORT_SOURCE", "INDEPENDENT_IMPORT_MAIN",
        "INDEPENDENT_IMPORT_ROUTE", "ROUTE_IMPORT_SOURCE", "AUDITOR_IMPORT_ROUTE",
    }:
        statements = {
            "SOURCE_IMPORT_EVALUATOR": "\nimport code.evaluator.evaluate_packet\n",
            "SOURCE_DIRECT_READ_EVALUATOR": "\nif False:\n    open('code/evaluator/evaluate_packet.py', 'rb').read()\n",
            "SOURCE_DYNAMIC_IMPORT_EVALUATOR": "\nif False:\n    __import__('code.evaluator.evaluate_packet')\n",
            "EMITTER_IMPORT_EVALUATOR": "\nimport code.evaluator.evaluate_packet\n",
            "MAIN_IMPORT_SOURCE": "\nimport code.source.source_core\n",
            "MAIN_DIRECT_READ_SOURCE": "\nif False:\n    open('code/source/source_core.py', 'rb').read()\n",
            "MAIN_IMPORT_INDEPENDENT": "\nimport code.evaluator.independent_evaluator\n",
            "MAIN_IMPORT_ROUTE": "\nimport code.evaluator.evaluate_route_a\n",
            "INDEPENDENT_IMPORT_SOURCE": "\nimport code.source.source_core\n",
            "INDEPENDENT_IMPORT_MAIN": "\nimport code.evaluator.evaluate_packet\n",
            "INDEPENDENT_IMPORT_ROUTE": "\nimport code.evaluator.evaluate_route_a\n",
            "ROUTE_IMPORT_SOURCE": "\nimport code.source.source_core\n",
            "AUDITOR_IMPORT_ROUTE": "\nimport code.evaluator.evaluate_route_a\n",
        }
        path.write_text(path.read_text(encoding="utf-8") + statements[operation], encoding="utf-8")
        refresh_ledger(root, relative)
    elif operation == "CACHE_INJECTION":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"cache mutation\n")
    elif operation == "AUX_INJECTION":
        path.write_bytes(b"auxiliary mutation\n")
    elif operation.startswith("HOST_TOKEN_"):
        token = {
            "HOST_TOKEN_TEMP_BOUNDARY": bytes((47, 116, 109, 112)),
            "HOST_TOKEN_ROOT_BOUNDARY": bytes((47, 114, 111, 111, 116, 47)),
            "HOST_TOKEN_HOME_BOUNDARY": bytes((47, 104, 111, 109, 101, 47)),
            "HOST_TOKEN_TEMP_SYMBOL": bytes((84, 77, 80, 95)),
        }[operation]
        path.write_bytes(path.read_bytes() + b"host token probe: " + token + b"\n")
        refresh_ledger(root, relative)
    elif operation == "ROOT_UNDECLARED_EXTRA":
        path.write_bytes(b"undeclared root mutation\n")
    elif operation.startswith("MAIN_CHECK_") or operation.startswith("INDEPENDENT_CHECK_"):
        coordinate_check_map_mutation(
            root, independent=operation.startswith("INDEPENDENT_"), operation=operation,
        )
    elif operation == "MAIN_TOP_OBJECT_TYPE_RELEDGER":
        path.write_bytes(canonical([]))
        refresh_ledger(root, relative)
    elif operation.startswith("AUDIT_ROUTE_"):
        route_path = root / ROUTE_REL
        route = yaml.safe_load(route_path.read_bytes())
        if operation == "AUDIT_ROUTE_STAGE_A_COMMIT_DRIFT":
            route["source_commit"] = DUMMY_COMMIT
        elif operation == "AUDIT_ROUTE_STAGE_A_MANIFEST_PRESENT":
            write_hash_rows(root / "PAPER_MANIFEST.sha256", sorted(hash_rows_for_tree(root), key=lambda item: item[1]))
        elif operation == "AUDIT_ROUTE_STAGE_B_MANIFEST_ABSENT":
            as_state_b(route)
        elif operation in {"AUDIT_ROUTE_STAGE_B_ZERO_TRIPLE", "AUDIT_ROUTE_STAGE_B_STALE_NOTE"}:
            as_state_b(route)
            if operation == "AUDIT_ROUTE_STAGE_B_ZERO_TRIPLE":
                route["source_commit"] = route["code_commit"] = "0" * 40
                route["source_lock"]["code_commit"] = "0" * 40
            else:
                route["freeze_note"] = stage1_note()
            route_path.write_text(yaml.safe_dump(route, sort_keys=False, width=1000), encoding="ascii")
            write_hash_rows(root / "PAPER_MANIFEST.sha256", sorted(hash_rows_for_tree(root), key=lambda item: item[1]))
            return
        else:
            raise ValueError(f"unsupported audit Route operation: {operation}")
        route_path.write_text(yaml.safe_dump(route, sort_keys=False, width=1000), encoding="ascii")
    elif operation == "GOVERNANCE_BYTE_DRIFT_RELEDGER":
        path.write_bytes(path.read_bytes() + b"governance mutation\n")
        refresh_ledger(root, relative)
    elif operation == "RUN_ROUTE_PROJECTION_COORDINATED_RELEDGER":
        for label in "ABC":
            relative_run = f"results/runs/{label}/route_evaluation.json"
            value = json.loads((root / relative_run).read_bytes())
            value["candidate_id"] = "SD-C44_MUTATED"
            (root / relative_run).write_bytes(canonical(value))
            refresh_ledger(root, relative_run)
        reproduction_path = root / "results/reproducibility_certificate.json"
        reproduction = json.loads(reproduction_path.read_bytes())
        for label in "ABC":
            reproduction["run_hashes"][label]["route_evaluation.json"] = digest(
                (root / f"results/runs/{label}/route_evaluation.json").read_bytes()
            )
        reproduction_path.write_bytes(canonical(reproduction))
        refresh_ledger(root, "results/reproducibility_certificate.json")
    elif operation == "WRITER_FINAL_INTEGRATION_STATIC_DRIFT":
        make_final_writer_state(root)
        path.write_bytes(path.read_bytes() + b"unauthorized integration mutation\n")
        refresh_ledger(root, relative)
    elif operation in {
        "LEDGER_SYMLINK_COMPONENT_EXTERNAL", "STAGE_B_MANIFEST_SYMLINK_COMPONENT_EXTERNAL",
        "SNAPSHOT_DECLARED_SYMLINK_COMPONENT_EXTERNAL",
    }:
        external = root.parent / (root.name + "_external_sentinel")
        external.mkdir()
        sentinel = external / "sentinel.txt"
        sentinel.write_bytes(b"external sentinel must never be opened\n")
        (root / "escape").symlink_to(external, target_is_directory=True)
        if operation == "LEDGER_SYMLINK_COMPONENT_EXTERNAL":
            rows, valid = parse_hash_bytes((root / LEDGER_REL).read_bytes())
            if not valid:
                raise RuntimeError("ledger fixture format differs")
            rows.append((digest(b"external sentinel must never be opened\n"), "escape/sentinel.txt"))
            write_hash_rows(root / LEDGER_REL, sorted(rows, key=lambda item: item[1]))
        elif operation == "STAGE_B_MANIFEST_SYMLINK_COMPONENT_EXTERNAL":
            make_state_b(root)
            rows, valid = parse_hash_bytes((root / "PAPER_MANIFEST.sha256").read_bytes())
            if not valid:
                raise RuntimeError("manifest fixture format differs")
            rows.append((digest(b"external sentinel must never be opened\n"), "escape/sentinel.txt"))
            write_hash_rows(root / "PAPER_MANIFEST.sha256", sorted(rows, key=lambda item: item[1]))
        else:
            dependency_path = root / "docs/DEPENDENCY_LOCK.json"
            dependency = json.loads(dependency_path.read_bytes())
            dependency["snapshot"]["rows"][0]["container_path"] = "escape/sentinel.txt"
            dependency_path.write_bytes(canonical(dependency))
            refresh_ledger(root, "docs/DEPENDENCY_LOCK.json")
    else:
        raise ValueError(f"unsupported audit operation: {operation}")


def run(packet_path: Path, route_path: Path, project_root: Path) -> dict[str, Any]:
    packet = json.loads(packet_path.read_bytes())
    route = yaml.safe_load(route_path.read_bytes())
    if type(packet) is not dict or type(route) is not dict:
        raise RuntimeError("baseline packet/Route is not a mapping")
    registry = load_registry(route, packet)
    contract = json.loads((project_root / CONTRACT_REL).read_bytes())
    groups: dict[str, Any] = {}
    with tempfile.TemporaryDirectory(prefix="paper42_mutations_") as temp_name:
        temp = Path(temp_name)
        (temp / "baseline_packet.json").write_bytes(canonical(packet))
        for group_name, registry_name in (("packet", "packet_mutations"), ("selection", "selection_mutations")):
            executed = []
            for row in registry[registry_name]:
                value = copy.deepcopy(packet)
                path = temp / f"{row['id']}.json"
                operation = row["operation"]
                main_script = ROOT / MAIN_REL
                independent_script = ROOT / INDEPENDENT_REL
                if operation == "NONCANONICAL_WHITESPACE":
                    raw = b" " + canonical(value)
                elif operation == "DUPLICATE_TOP_KEY":
                    raw = canonical(value).replace(
                        b'  "candidate_id": "SD-C44",\n',
                        b'  "candidate_id": "SD-C44",\n  "candidate_id": "SD-C44",\n',
                        1,
                    )
                elif operation == "DUPLICATE_NESTED_KEY":
                    prefix = b'  "control_grid": {\n'
                    field = (
                        b'    "field_sizes": [\n'
                        b'      2,\n'
                        b'      3,\n'
                        b'      5\n'
                        b'    ],\n'
                    )
                    needle = prefix + field
                    baseline_raw = canonical(value)
                    if baseline_raw.count(needle) != 1:
                        raise RuntimeError("nested duplicate-key fixture differs")
                    raw = baseline_raw.replace(needle, prefix + field + field, 1)
                elif operation == "RAW_KEY_ORDER_SWAP":
                    items = list(value.items())
                    items[0], items[1] = items[1], items[0]
                    raw = (json.dumps(dict(items), sort_keys=False, indent=2, ensure_ascii=True) + "\n").encode("ascii")
                elif operation.startswith("SEMANTIC_SELECTION_"):
                    embedded = value["raw_selection_cards"]["packet"]
                    inner = "/" + "/".join(tokens(row["json_pointer"])[2:])
                    if operation == "SEMANTIC_SELECTION_ORDER_REVERSAL":
                        resolve(embedded, inner).reverse()
                    else:
                        replace(embedded, inner, drift(resolve(embedded, inner)))
                    embedded_raw = canonical(embedded)
                    value["raw_selection_cards"]["packet_sha256"] = digest(embedded_raw)
                    value["raw_selection_cards"]["packet_utf8_b64"] = base64.b64encode(embedded_raw).decode("ascii")
                    raw = canonical(value)
                    main_script, independent_script = reanchored_evaluator_paths(temp, digest(raw))
                elif operation == "SEMANTIC_SOURCE_ID_SCHEME_DRIFT":
                    replace(value, row["json_pointer"], "unknown:semantic-lane")
                    raw = canonical(value)
                    main_script, independent_script = reanchored_evaluator_paths(temp, digest(raw))
                elif operation.startswith("SEMANTIC_REANCHOR_"):
                    base_operation = operation.removeprefix("SEMANTIC_REANCHOR_")
                    apply_recursive(value, row["json_pointer"], base_operation)
                    raw = canonical(value)
                    main_script, independent_script = reanchored_evaluator_paths(temp, digest(raw))
                elif operation == "SEMANTIC_CHRONOLOGY_VALUE_DRIFT":
                    replace(value, row["json_pointer"], drift(resolve(value, row["json_pointer"])))
                    raw = canonical(value)
                    main_script, independent_script = reanchored_evaluator_paths(temp, digest(raw))
                elif operation == "LIST_CONTAINER_TO_SCALAR":
                    replace(value, row["json_pointer"], 17)
                    raw = canonical(value)
                else:
                    apply_recursive(value, row["json_pointer"], operation)
                    raw = canonical(value)
                path.write_bytes(raw)
                expected = row["expected_rejection"]
                exact_reject(python(main_script, str(path)), f"REJECT: {expected['main']}\n", ROOT)
                exact_reject(python(independent_script, str(path)), f"REJECT: {expected['independent']}\n", ROOT)
                executed.append(result_row(row, main_rejects=True, independent_rejects=True))
            groups[group_name] = group_result(registry[registry_name], executed)

        executed = []
        for row in registry["route_mutations"]:
            value = copy.deepcopy(route)
            path = temp / f"{row['id']}.yaml"
            operation = row["operation"]
            manifest_state = "absent"
            validation_root = project_root
            if operation == "DUPLICATE_TOP_KEY":
                raw = route_path.read_bytes() + b"candidate_id: SD-C44\n"
            elif operation == "RAW_WHITESPACE":
                raw = route_path.read_bytes() + b"\n"
            elif operation == "RAW_KEY_ORDER_SWAP":
                items = list(value.items())
                items[0], items[1] = items[1], items[0]
                raw = yaml.safe_dump(dict(items), sort_keys=False, width=1000).encode("ascii")
            elif operation.startswith("ARTIFACT_"):
                replacements = {
                    "ARTIFACT_ABSOLUTE_PATH": "/etc/passwd",
                    "ARTIFACT_PARENT_ESCAPE": "../preauthority/SOURCE_LOCK.md",
                    "ARTIFACT_SAFE_MISSING": "preauthority/__missing_artifact__.md",
                    "ARTIFACT_WRONG_BASE_EXISTING": "code/contracts/INTEGRATION_CONTRACT.json",
                }
                if operation == "ARTIFACT_SYMLINK_COMPONENT":
                    validation_root = temp / f"{row['id']}_root"
                    shutil.copytree(
                        project_root, validation_root,
                        ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc", "*.pyo"),
                    )
                    external = temp / f"{row['id']}_external"
                    external.mkdir()
                    sentinel = external / "sentinel.md"
                    sentinel.write_bytes(b"external artifact sentinel\n")
                    link = validation_root / "preauthority/__artifact_link__"
                    link.symlink_to(external, target_is_directory=True)
                    replacement = "preauthority/__artifact_link__/sentinel.md"
                else:
                    replacement = replacements[operation]
                replace(value, row["json_pointer"], replacement)
                raw = yaml.safe_dump(value, sort_keys=False, width=1000).encode("ascii")
            elif operation.startswith("STAGE_A_"):
                if operation == "STAGE_A_SOURCE_COMMIT_DRIFT":
                    value["source_commit"] = DUMMY_COMMIT
                elif operation == "STAGE_A_CODE_COMMIT_DRIFT":
                    value["code_commit"] = DUMMY_COMMIT
                elif operation == "STAGE_A_SOURCE_LOCK_COMMIT_DRIFT":
                    value["source_lock"]["code_commit"] = DUMMY_COMMIT
                elif operation == "STAGE_A_FREEZE_NOTE_DRIFT":
                    value["freeze_note"] += " MUTATED"
                elif operation == "STAGE_A_SOURCE_COMMIT_TYPE_DRIFT":
                    value["source_commit"] = 17
                elif operation == "STAGE_A_CODE_COMMIT_TYPE_DRIFT":
                    value["code_commit"] = 17
                elif operation == "STAGE_A_SOURCE_LOCK_COMMIT_TYPE_DRIFT":
                    value["source_lock"]["code_commit"] = 17
                elif operation == "STAGE_A_MANIFEST_PRESENT":
                    manifest_state = "present"
                elif operation == "STAGE_A_FREEZE_NOTE_TYPE_DRIFT":
                    value["freeze_note"] = 17
                elif operation == "STAGE_A_SOURCE_COMMIT_DELETION":
                    del value["source_commit"]
                elif operation == "STAGE_A_CODE_COMMIT_DELETION":
                    del value["code_commit"]
                elif operation == "STAGE_A_SOURCE_LOCK_COMMIT_DELETION":
                    del value["source_lock"]["code_commit"]
                elif operation == "STAGE_A_FREEZE_NOTE_DELETION":
                    del value["freeze_note"]
                else:
                    raise ValueError(f"unsupported Stage-A Route operation: {operation}")
                raw = yaml.safe_dump(value, sort_keys=False, width=1000).encode("ascii")
            elif operation.startswith("STAGE_B_"):
                as_state_b(value)
                manifest_state = "present"
                if operation == "STAGE_B_MANIFEST_ABSENT":
                    manifest_state = "absent"
                elif operation == "STAGE_B_SOURCE_COMMIT_DRIFT":
                    value["source_commit"] = "1123456789abcdef0123456789abcdef01234567"
                elif operation == "STAGE_B_CODE_COMMIT_DRIFT":
                    value["code_commit"] = "1123456789abcdef0123456789abcdef01234567"
                elif operation == "STAGE_B_SOURCE_LOCK_COMMIT_DRIFT":
                    value["source_lock"]["code_commit"] = "1123456789abcdef0123456789abcdef01234567"
                elif operation in {"STAGE_B_ZERO_COMMIT_TRIPLE", "STAGE_B_NONHEX_COMMIT_TRIPLE",
                                   "STAGE_B_UPPERCASE_COMMIT_TRIPLE", "STAGE_B_WRONG_LENGTH_COMMIT_TRIPLE",
                                   "STAGE_B_PENDING_TRIPLE_WITH_MANIFEST"}:
                    replacement = {
                        "STAGE_B_ZERO_COMMIT_TRIPLE": "0" * 40,
                        "STAGE_B_NONHEX_COMMIT_TRIPLE": "g" * 40,
                        "STAGE_B_UPPERCASE_COMMIT_TRIPLE": "ABCDEF0123456789ABCDEF0123456789ABCDEF01",
                        "STAGE_B_WRONG_LENGTH_COMMIT_TRIPLE": "1" * 39,
                        "STAGE_B_PENDING_TRIPLE_WITH_MANIFEST": PENDING,
                    }[operation]
                    value["source_commit"] = replacement
                    value["code_commit"] = replacement
                    value["source_lock"]["code_commit"] = replacement
                elif operation == "STAGE_B_STALE_FREEZE_NOTE":
                    value["freeze_note"] = stage1_note()
                elif operation == "STAGE_B_FREEZE_NOTE_TYPE_DRIFT":
                    value["freeze_note"] = 17
                elif operation == "STAGE_B_SOURCE_COMMIT_DELETION":
                    del value["source_commit"]
                elif operation == "STAGE_B_SOURCE_COMMIT_TYPE_DRIFT":
                    value["source_commit"] = 17
                elif operation == "STAGE_B_CODE_COMMIT_DELETION":
                    del value["code_commit"]
                elif operation == "STAGE_B_CODE_COMMIT_TYPE_DRIFT":
                    value["code_commit"] = 17
                elif operation == "STAGE_B_SOURCE_LOCK_COMMIT_DELETION":
                    del value["source_lock"]["code_commit"]
                elif operation == "STAGE_B_SOURCE_LOCK_COMMIT_TYPE_DRIFT":
                    value["source_lock"]["code_commit"] = 17
                elif operation == "STAGE_B_FREEZE_NOTE_DELETION":
                    del value["freeze_note"]
                elif operation == "STAGE_B_WRONG_VALID_COMMIT_STALE_NOTE":
                    replacement = "1123456789abcdef0123456789abcdef01234567"
                    value["source_commit"] = replacement
                    value["code_commit"] = replacement
                    value["source_lock"]["code_commit"] = replacement
                else:
                    raise ValueError(f"unsupported Stage-B Route operation: {operation}")
                raw = yaml.safe_dump(value, sort_keys=False, width=1000).encode("ascii")
            else:
                apply_recursive(value, row["json_pointer"], operation)
                raw = yaml.safe_dump(value, sort_keys=False, width=1000).encode("ascii")
            path.write_bytes(raw)
            expected = row["expected_rejection"]
            exact_reject(
                python(ROOT / ROUTE_MAIN_REL, "validate", str(path), manifest_state, str(validation_root)),
                f"REJECT: {expected['main']}\n", ROOT,
            )
            exact_reject(
                python(ROOT / INDEPENDENT_REL, "route", str(path), manifest_state, str(validation_root)),
                f"REJECT: {expected['independent']}\n", ROOT,
            )
            executed.append(result_row(row, main_rejects=True, independent_rejects=True))
        groups["route"] = group_result(registry["route_mutations"], executed)

        executed = []
        for row in registry["static_mutations"]:
            clone = temp / row["id"]
            shutil.copytree(
                project_root, clone,
                ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc", "*.pyo"),
            )
            apply_static(clone, row)
            rejection = static_rejection(clone, contract)
            expected_gate = row["expected_rejection"]["static_gate"]
            if rejection != expected_gate:
                raise RuntimeError(f"static rejection differs for {row['id']}: {rejection!r} != {expected_gate!r}")
            codes = row["expected_rejection"]["auditor"]
            expected = f"FAIL: integrity checks failed: {', '.join(codes)}\n"
            exact_reject(python(ROOT / AUDITOR_REL, str(clone)), expected, ROOT)
            executed.append(result_row(row, auditor_rejects=True))
            shutil.rmtree(clone)
        groups["static"] = group_result(registry["static_mutations"], executed)

        baseline = subprocess.run(python(project_root / AUDITOR_REL, str(project_root)), cwd=ROOT, env=environment(), capture_output=True, check=False)
        if baseline.returncode != 0 or baseline.stderr or not baseline.stdout:
            raise RuntimeError(f"audit mutation baseline is not accepted: {baseline.stderr!r}")
        writer_control = writer_state_control(project_root, temp, baseline.stdout, registry)
        executed = []
        for row in registry["audit_mutations"]:
            clone = temp / row["id"]
            shutil.copytree(project_root, clone, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
            apply_audit(clone, row)
            codes = row["expected_rejection"]["auditor"]
            expected = f"FAIL: integrity checks failed: {', '.join(codes)}\n"
            exact_reject(python(ROOT / AUDITOR_REL, str(clone)), expected, ROOT)
            executed.append(result_row(row, auditor_rejects=True))
            shutil.rmtree(clone)
        groups["audit"] = group_result(registry["audit_mutations"], executed)

    all_ids = sorted(
        row["id"]
        for name in ("packet_mutations", "selection_mutations", "route_mutations", "static_mutations", "audit_mutations")
        for row in registry[name]
    )
    dual = 2 * sum(groups[name]["count"] for name in ("packet", "selection", "route"))
    return {
        "audit_rejections": groups["audit"]["count"],
        "dual_rejections": dual,
        "groups": groups,
        "mutation_ids": all_ids,
        "mutation_ids_sha256": digest("".join(item + "\n" for item in all_ids).encode("ascii")),
        "registry_sha256": digest((ROOT / REGISTRY_REL).read_bytes()),
        "schema": "paper42-adversarial-mutation-results-v2",
        "static_rejections": groups["static"]["count"],
        "survivors": [],
        "total_mutations": len(all_ids),
        "writer_state_control": writer_control,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("FAIL: argument contract", file=sys.stderr)
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
