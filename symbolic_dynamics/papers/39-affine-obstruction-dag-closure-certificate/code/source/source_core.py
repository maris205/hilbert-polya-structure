#!/usr/bin/env python3
"""Source-only byte-locked extraction for the Paper 39 closure prototype."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any


HEX64 = re.compile(r"^[0-9a-f]{64}$")
MANIFEST_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")
TERMINAL_CODE = re.compile(r"\b(?:CLOSE|GO|RETURN|ROUTE|STOP)_[A-Z0-9_]+\b")

RETROSPECTIVE_PREREGISTRATION = {
    "checker_inputs_frozen_before_checker_run": True,
    "closure_universe_and_predicate_status": "RETROSPECTIVE_ENCODING_FROM_KNOWN_P35_P38_OUTCOMES",
    "freeze_boundary": "FROZEN_BEFORE_PAPER39_CHECKER_EXECUTION_NOT_BEFORE_PREDECESSOR_OUTCOMES",
    "independent_of_predecessor_results_claimed": False,
    "predecessor_outcomes_known_when_encoded": True,
}


def canonical_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_manifest(path: Path) -> dict[str, str]:
    raw = path.read_bytes()
    require(raw.endswith(b"\n") and not raw.endswith(b"\n\n"), f"manifest EOF: {path}")
    require(b"\r" not in raw, f"manifest CR: {path}")
    rows: list[tuple[str, str]] = []
    for line in raw.decode("utf-8").splitlines():
        match = MANIFEST_LINE.fullmatch(line)
        require(match is not None, f"manifest format: {path}: {line!r}")
        rows.append((match.group(2), match.group(1)))
    paths = [row[0] for row in rows]
    require(paths == sorted(set(paths)), f"manifest sorted unique: {path}")
    require("PAPER_MANIFEST.sha256" not in paths, f"manifest self inclusion: {path}")
    return dict(rows)


def _line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def extract_scalar(text: str, key: str, indent: int = 0) -> str:
    lines = text.splitlines()
    prefix = " " * indent + key + ":"
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix) and _line_indent(line) == indent]
    require(len(indexes) == 1, f"scalar {key!r} at indent {indent}: {len(indexes)} matches")
    index = indexes[0]
    tail = lines[index][len(prefix):].strip()
    if tail in {">-", ">", "|-", "|"}:
        values: list[str] = []
        for line in lines[index + 1:]:
            if line.strip() and _line_indent(line) <= indent:
                break
            values.append(line.strip())
        return " ".join(value for value in values if value)
    if tail.startswith('"') and tail.endswith('"'):
        return json.loads(tail)
    return tail.strip("'")


def extract_list(text: str, key: str, indent: int = 0) -> list[str]:
    lines = text.splitlines()
    prefix = " " * indent + key + ":"
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix) and _line_indent(line) == indent]
    require(len(indexes) == 1, f"list {key!r} at indent {indent}: {len(indexes)} matches")
    index = indexes[0]
    values: list[str] = []
    item_indent = indent + 2
    for line in lines[index + 1:]:
        if line.strip() and _line_indent(line) <= indent:
            break
        if _line_indent(line) == item_indent and line.strip().startswith("-"):
            value = line.strip()[1:].strip()
            if value.startswith('"') and value.endswith('"'):
                value = json.loads(value)
            values.append(value)
        elif values and line.strip() and _line_indent(line) > item_indent:
            values[-1] += " " + line.strip()
    return values


def source_lock_block(route_text: str) -> str:
    lines = route_text.splitlines()
    start = next(index for index, line in enumerate(lines) if line == "source_lock:")
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].strip() and _line_indent(lines[index]) == 0:
            end = index
            break
    return "\n".join(lines[start:end]) + "\n"


def top_level_block(route_text: str, key: str) -> str:
    lines = route_text.splitlines()
    marker = key + ":"
    indexes = [index for index, line in enumerate(lines) if line == marker]
    require(len(indexes) == 1, f"top-level block {key}: {len(indexes)} matches")
    start = indexes[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].strip() and _line_indent(lines[index]) == 0:
            end = index
            break
    return "\n".join(lines[start:end]) + "\n"


def normalize_repair(raw: str) -> str:
    value = raw.lower().replace("--", "-")
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value


def extract_repair_alphabet(round2_text: str) -> list[dict[str, str]]:
    compact = " ".join(round2_text.split())
    match = re.search(r"Do not retry another (.+?) as a repair of SD-C40\.", compact)
    require(match is not None, "P38 repair alphabet sentence absent")
    body = match.group(1).replace(", or ", ", ")
    raw_items = [item.strip() for item in body.split(",")]
    require(len(raw_items) == 14, f"repair alphabet size {len(raw_items)}")
    return [{"raw": item, "repair_class": normalize_repair(item)} for item in raw_items]


def parse_registry(registry_text: str, prereg_text: str) -> list[dict[str, Any]]:
    require("# Session 4 Candidate Registry" in registry_text, "registry title")
    require("Candidate definitions and stop rules are frozen" in registry_text, "registry freeze phrase")
    require("# Session 4 Preregistration and Source Lock" in prereg_text, "prereg source-lock title")
    prereg_compact = " ".join(prereg_text.split())
    initial_pre_result = "Status at freeze: candidate definitions frozen; no numerical candidate result inspected" in prereg_compact
    addendum_pre_result = "Two objects discovered during the source audit were added before any experiment on either object was run" in prereg_compact
    require(initial_pre_result, "initial registry pre-result assertion")
    require(addendum_pre_result, "addendum registry pre-result assertion")
    rows: list[dict[str, Any]] = []
    for line in registry_text.splitlines():
        if not line.startswith("| [`SD-C"):
            continue
        fields = [field.strip() for field in line.strip().strip("|").split("|")]
        require(len(fields) == 6, f"registry field count: {line}")
        match = re.match(r"\[`(SD-C\d{2})`\]\(([^)]+)\)", fields[0])
        require(match is not None, f"registry ID cell: {fields[0]}")
        candidate_id = match.group(1)
        heading = re.search(rf"^#{{2,3}} {re.escape(candidate_id)}\s+[—-]", prereg_text, re.MULTILINE)
        require(heading is not None, f"candidate section absent: {candidate_id}")
        next_heading = re.search(r"^#{2,3} SD-C\d{2}(?:\s+[—-]|\s+implementation-freeze)", prereg_text[heading.end():], re.MULTILINE)
        section_end = heading.end() + next_heading.start() if next_heading else len(prereg_text)
        section = prereg_text[heading.start():section_end]
        initial_candidate = candidate_id in {"SD-C01", "SD-C02", "SD-C03", "SD-C04"}
        evidence = {
            "candidate_section_present": True,
            "fixed_tests_present": ("Fixed tests and stop rule" in section) if initial_candidate else ("fixed tests" in " ".join(section.lower().split())),
            "frozen_object_present": ("Frozen object" in section) if initial_candidate else bool(re.search(r"\b(?:Define|Set)\b", section)),
            "pre_result_declaration_present": initial_pre_result if initial_candidate else addendum_pre_result,
            "stop_rule_present": "stop" in section.lower(),
        }
        source_locked = all(evidence.values())
        affine_tokens = ("affine", "cayley", "bass-serre", "bs(1")
        is_affine = any(token in fields[1].lower() for token in affine_tokens)
        rows.append({
            "branch_class": "AFFINE" if is_affine else "NON_AFFINE_PREEXISTING_SOURCE_LOCKED",
            "candidate_id": candidate_id,
            "frozen_route_tuple": fields[2].strip("`"),
            "object": fields[1],
            "overall_status": fields[3].strip("`"),
            "route_a_path": match.group(2),
            "route_b": fields[5],
            "source_locked": source_locked,
            "source_lock_evidence": evidence,
            "strongest_failure": fields[4]
        })
    require(rows, "registry rows absent")
    return rows


def parse_terminal_evidence(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        "codes": sorted(set(TERMINAL_CODE.findall(path.read_text(encoding="utf-8")))),
        "sha256": digest(path),
        "top_level_keys": sorted(payload)
    }


def parse_paper(base: Path, spec: dict[str, Any]) -> dict[str, Any]:
    root = base / spec["slug"]
    require(root.is_dir(), f"paper root missing: {root}")
    locked_hashes: dict[str, str] = spec["files"]
    observed: dict[str, str] = {}
    for relative, expected in locked_hashes.items():
        require(HEX64.fullmatch(expected) is not None, f"bad lock hash: {relative}")
        path = root / relative
        require(path.is_file(), f"locked file missing: {path}")
        observed[relative] = digest(path)
        require(observed[relative] == expected, f"locked hash mismatch: {path}")
    manifest = parse_manifest(root / "PAPER_MANIFEST.sha256")
    for relative, expected in locked_hashes.items():
        if relative == "PAPER_MANIFEST.sha256":
            continue
        require(manifest.get(relative) == expected, f"manifest pointer mismatch: {spec['paper_id']}:{relative}")

    route_path = root / spec["route_relative"]
    route_text = route_path.read_text(encoding="utf-8")
    lock_text = source_lock_block(route_text)
    source_commit = extract_scalar(route_text, "source_commit", 0)
    code_commit = extract_scalar(route_text, "code_commit", 0)
    nested_commit = extract_scalar(lock_text, "code_commit", 2)
    require(source_commit == code_commit == nested_commit == spec["artifact_commit"], f"sealed provenance: {spec['paper_id']}")
    round2_text = (root / "ROUND2_CLUES.md").read_text(encoding="utf-8")
    compilation_text = (root / "COMPILATION_REPORT.md").read_text(encoding="utf-8")
    terminal = parse_terminal_evidence(root / spec["terminal_evidence_relative"])
    terminal["codes"] = sorted(set(terminal["codes"]) | set(TERMINAL_CODE.findall(compilation_text)) | set(TERMINAL_CODE.findall(round2_text)))

    record = {
        "artifact_commit": spec["artifact_commit"],
        "blocking_conditions": extract_list(route_text, "blocking_conditions", 0),
        "candidate_id": extract_scalar(route_text, "candidate_id", 0),
        "determinant_convention": extract_scalar(lock_text, "determinant_convention", 2),
        "forbidden_repairs": extract_list(lock_text, "forbidden_data", 2),
        "input_hashes": observed,
        "main_theorem_marker": extract_scalar(lock_text, "main_theorem_marker", 2),
        "manifest_entry_count": len(manifest),
        "manifest_sha256": observed["PAPER_MANIFEST.sha256"],
        "next_smallest_test": extract_scalar(route_text, "next_smallest_test", 0),
        "normalization": extract_scalar(lock_text, "normalization", 2),
        "object": extract_scalar(lock_text, "object", 2),
        "operator_ownership": {
            "determinant_convention": extract_scalar(lock_text, "determinant_convention", 2),
            "operator_object": extract_scalar(lock_text, "object", 2),
            "regularization_order": extract_scalar(lock_text, "regularization_order", 2),
        },
        "overall_verdict": extract_scalar(route_text, "overall_verdict", 0),
        "paper_id": spec["paper_id"],
        "round2_clues": extract_list(route_text, "round2_clues", 0),
        "route_b_invocation_allowed": extract_scalar(route_text, "route_b_invocation_allowed", 0) == "true",
        "route_tuple": extract_list(route_text, "route_tuple", 0),
        "sealed_provenance_triple": [source_commit, code_commit, nested_commit],
        "strongest_failures": {
            gate: extract_scalar(top_level_block(route_text, gate), "strongest_failure", 2)
            for gate in ("a1", "a2", "a3", "a4")
        },
        "terminal_evidence": terminal
    }
    record["terminal_codes"] = terminal["codes"]
    record["typed_normalization"] = {
        "forbidden_repairs": record["forbidden_repairs"],
        "inherited_obligation": record["next_smallest_test"],
        "marker": record["main_theorem_marker"],
        "object": record["object"],
        "obstructions": {
            "blocking_conditions": record["blocking_conditions"],
            "strongest_failures": record["strongest_failures"],
        },
        "operator_ownership": record["operator_ownership"],
        "terminal_codes": record["terminal_codes"],
    }
    if spec["paper_id"] == "P38":
        record["repair_alphabet"] = extract_repair_alphabet(round2_text)
        record["empty_registry_fallback_present"] = "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR" in round2_text
    return record


def build_packet(input_lock_path: Path) -> dict[str, Any]:
    input_lock = json.loads(input_lock_path.read_text(encoding="utf-8"))
    require(input_lock.get("schema") == "paper39-input-lock-v1", "input lock schema")
    route_evaluator_lock = input_lock["route_a_evaluator"]
    route_evaluator_path = Path(route_evaluator_lock["absolute_path"])
    require(route_evaluator_path.is_file(), "Route-A evaluator authority missing")
    require(digest(route_evaluator_path) == route_evaluator_lock["sha256"], "Route-A evaluator stale provenance")
    route_evaluator_text = route_evaluator_path.read_text(encoding="utf-8")
    require("**Version:** `0.2.0`" in route_evaluator_text, "Route-A evaluator version text")
    good_map = route_evaluator_lock["good_conjunct_criterion_map"]
    require([row.get("good_conjunct") for row in good_map] == ["I", "R", "S", "D", "M", "C"], "Good conjunct map exact order")
    require(all(row.get("criterion_ids") and row.get("required_anchor_substrings") for row in good_map), "Good conjunct map nonempty fields")
    require(all(anchor in route_evaluator_text for row in good_map for anchor in row["required_anchor_substrings"]), "Good conjunct map authority anchors")
    base = Path(input_lock["authority_papers_base"])
    records = [parse_paper(base, spec) for spec in input_lock["papers"]]
    registry_spec = input_lock["registry"]
    registry_path = base / registry_spec["candidate_registry_relative"]
    prereg_path = base / registry_spec["preregistration_relative"]
    require(digest(registry_path) == registry_spec["candidate_registry_sha256"], "registry stale provenance")
    require(digest(prereg_path) == registry_spec["preregistration_sha256"], "registry prereg stale provenance")
    rows = parse_registry(registry_path.read_text(encoding="utf-8"), prereg_path.read_text(encoding="utf-8"))
    source_locked_non_affine = [row for row in rows if row["source_locked"] and row["branch_class"] == "NON_AFFINE_PREEXISTING_SOURCE_LOCKED"]
    realized_terminal = (
        "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY"
        if source_locked_non_affine
        else "STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR"
    )
    by_id = {record["paper_id"]: record for record in records}
    declared_edges = [
        {
            "edge_id": "E35_36",
            "from": "N35_OBJECT_FIREWALL",
            "inherited_obligation": by_id["P35"]["next_smallest_test"],
            "target_determinant": by_id["P36"]["determinant_convention"],
            "target_marker": by_id["P36"]["main_theorem_marker"],
            "target_object": by_id["P36"]["object"],
            "target_operator_ownership": by_id["P36"]["operator_ownership"],
            "to": "N36_CELLULAR_CANCELLATION"
        },
        {
            "edge_id": "E36_37",
            "from": "N36_CELLULAR_CANCELLATION",
            "inherited_obligation": by_id["P36"]["next_smallest_test"],
            "target_determinant": by_id["P37"]["determinant_convention"],
            "target_marker": by_id["P37"]["main_theorem_marker"],
            "target_object": by_id["P37"]["object"],
            "target_operator_ownership": by_id["P37"]["operator_ownership"],
            "to": "N37_COEFFICIENT_SATURATION"
        },
        {
            "edge_id": "E37_38",
            "from": "N37_COEFFICIENT_SATURATION",
            "inherited_obligation": by_id["P37"]["next_smallest_test"],
            "target_determinant": by_id["P38"]["determinant_convention"],
            "target_marker": by_id["P38"]["main_theorem_marker"],
            "target_object": by_id["P38"]["object"],
            "target_operator_ownership": by_id["P38"]["operator_ownership"],
            "to": "N38_TREE_ORBITAL_TRILEMMA"
        },
        {
            "edge_id": "E38_CLOSE",
            "from": "N38_TREE_ORBITAL_TRILEMMA",
            "inherited_obligation": by_id["P38"]["next_smallest_test"],
            "target_determinant": "NO_NEW_DETERMINANT_AUDIT_ONLY",
            "target_marker": "NO_NEW_MARKER_AUDIT_ONLY",
            "target_object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM",
            "target_operator_ownership": {
                "determinant_convention": "NO_NEW_DETERMINANT_AUDIT_ONLY",
                "operator_object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM",
                "regularization_order": "AUDIT_ONLY_NOT_APPLICABLE"
            },
            "to": "N39_AFFINE_BRANCH_CLOSED"
        },
        {
            "edge_id": "E_CLOSE_REGISTRY",
            "from": "N39_AFFINE_BRANCH_CLOSED",
            "inherited_obligation": "Return control to the pre-existing global Symbolic Dynamics candidate registry without creating, ranking, or proposing a mechanism.",
            "target_determinant": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
            "target_marker": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
            "target_object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY",
            "target_operator_ownership": {
                "determinant_convention": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
                "operator_object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY",
                "regularization_order": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY"
            },
            "to": "N_REGISTRY_HANDOFF"
        }
    ]
    raw_node_types = {
        "N35_OBJECT_FIREWALL": {
            "determinant_owner": by_id["P35"]["determinant_convention"],
            "marker": by_id["P35"]["main_theorem_marker"],
            "object": by_id["P35"]["object"],
            "operator_owner": by_id["P35"]["operator_ownership"],
        },
        "N36_CELLULAR_CANCELLATION": {
            "determinant_owner": by_id["P36"]["determinant_convention"],
            "marker": by_id["P36"]["main_theorem_marker"],
            "object": by_id["P36"]["object"],
            "operator_owner": by_id["P36"]["operator_ownership"],
        },
        "N37_COEFFICIENT_SATURATION": {
            "determinant_owner": by_id["P37"]["determinant_convention"],
            "marker": by_id["P37"]["main_theorem_marker"],
            "object": by_id["P37"]["object"],
            "operator_owner": by_id["P37"]["operator_ownership"],
        },
        "N38_TREE_ORBITAL_TRILEMMA": {
            "determinant_owner": by_id["P38"]["determinant_convention"],
            "marker": by_id["P38"]["main_theorem_marker"],
            "object": by_id["P38"]["object"],
            "operator_owner": by_id["P38"]["operator_ownership"],
        },
        "N39_AFFINE_BRANCH_CLOSED": {
            "determinant_owner": "NO_NEW_DETERMINANT_AUDIT_ONLY",
            "marker": "NO_NEW_MARKER_AUDIT_ONLY",
            "object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM",
            "operator_owner": {
                "determinant_convention": "NO_NEW_DETERMINANT_AUDIT_ONLY",
                "operator_object": "TYPED_HISTORY_ONLY_NO_NEW_SYMBOLIC_MECHANISM",
                "regularization_order": "AUDIT_ONLY_NOT_APPLICABLE",
            },
        },
        "N_REGISTRY_HANDOFF": {
            "determinant_owner": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
            "marker": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
            "object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY",
            "operator_owner": {
                "determinant_convention": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
                "operator_object": "SESSION4_GLOBAL_CANDIDATE_REGISTRY",
                "regularization_order": "NOT_APPLICABLE_REGISTRY_CLASSIFICATION_ONLY",
            },
        },
    }
    transfer_rules = {
        "E35_36": {
            field: {"mode": "RESET", "reset_authority_id": "P36_SOURCE_LOCK_SD_C38"}
            for field in ("determinant_owner", "marker", "object", "operator_owner")
        },
        "E36_37": {
            field: {"mode": "RESET", "reset_authority_id": "P37_SOURCE_LOCK_SD_C39"}
            for field in ("determinant_owner", "marker", "object", "operator_owner")
        },
        "E37_38": {field: {"mode": "RESET", "reset_authority_id": "P38_SOURCE_LOCK_SD_C40"} for field in ("determinant_owner", "marker", "object", "operator_owner")},
        "E38_CLOSE": {field: {"mode": "RESET", "reset_authority_id": "P39_AUDIT_ONLY_CONTRACT"} for field in ("determinant_owner", "marker", "object", "operator_owner")},
        "E_CLOSE_REGISTRY": {field: {"mode": "RESET", "reset_authority_id": "SESSION4_REGISTRY_SOURCE_LOCK"} for field in ("determinant_owner", "marker", "object", "operator_owner")},
    }
    for edge in declared_edges:
        source_types = raw_node_types[edge["from"]]
        target_types = raw_node_types[edge["to"]]
        edge["source_determinant"] = source_types["determinant_owner"]
        edge["source_marker"] = source_types["marker"]
        edge["source_object"] = source_types["object"]
        edge["source_operator_ownership"] = source_types["operator_owner"]
        edge["target_determinant"] = target_types["determinant_owner"]
        edge["target_marker"] = target_types["marker"]
        edge["target_object"] = target_types["object"]
        edge["target_operator_ownership"] = target_types["operator_owner"]
        edge["field_transfer"] = {
            field: {
                **transfer_rules[edge["edge_id"]][field],
                "source": source_types[field],
                "target": target_types[field],
            }
            for field in ("determinant_owner", "marker", "object", "operator_owner")
        }
    return {
        "candidate_contract_scope": "FINITE_FROZEN_P35_P38_REPAIR_ALPHABET_ONLY",
        "declared_edges": declared_edges,
        "mechanism_creation": {"new_mechanisms": [], "ranking": [], "successor_proposals": []},
        "paper_records": records,
        "preregistration_semantics": RETROSPECTIVE_PREREGISTRATION,
        "registry": {
            "candidate_registry_sha256": digest(registry_path),
            "chronology_basis": "trusted_hashed_source_assertion",
            "chronology_evidence_status": "TRUSTED_HASHED_SOURCE_ASSERTION_NOT_INDEPENDENTLY_ESTABLISHED",
            "preregistration_sha256": digest(prereg_path),
            "preregistration_source_lock_path": registry_spec["preregistration_relative"],
            "realized_terminal": realized_terminal,
            "rows": rows,
            "source_locked_non_affine_count": len(source_locked_non_affine)
        },
        "route_a_evaluator_provenance": {
            "absolute_path": route_evaluator_lock["absolute_path"],
            "current_hash_verified": True,
            "good_conjunct_criterion_map": good_map,
            "provenance_role": route_evaluator_lock["provenance_role"],
            "sha256": route_evaluator_lock["sha256"],
            "skill_version": route_evaluator_lock["skill_version"],
        },
        "schema": "paper39-source-packet-v1",
        "source_evaluator_separated": True,
        "universal_affine_no_go_claimed": False
    }
