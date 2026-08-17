#!/usr/bin/env python3
"""Build the self-contained primitive packet for Paper 41 / SD-C43."""

from __future__ import annotations

from base64 import b64decode, b64encode
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_REL = "code/contracts/INTEGRATION_CONTRACT.json"
CONTRACT_SHA256 = "2f0bbcf5dd2d2ff725edcb961f94d45c11351ed1c89fe30af803f6ee1aa07bbc"
SELECTION_REL = "docs/inputs/SESSION4_SELECTION_PACKET.json"
ROUTE_SCHEMA_REL = "code/contracts/ROUTE_A_V0_2_SCHEMA.json"
ROUTE_SKILL_REL = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
SOURCE_MANIFEST_REL = "preauthority/SOURCE_HASHES.sha256"
SNAPSHOT_REL = "docs/inputs/repo_snapshot"


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest_bytes(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def digest(relative: str) -> str:
    return digest_bytes((ROOT / relative).read_bytes())


def load_json(relative: str) -> dict[str, Any]:
    value = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected object in {relative}")
    return value


def safe_id_payload(payload: str, *, allow_slash: bool) -> bool:
    if not payload or payload.startswith("/") or "\\" in payload:
        return False
    parts = PurePosixPath(payload).parts
    if any(part in ("", ".", "..") for part in parts):
        return False
    if not allow_slash and len(parts) != 1:
        return False
    return PurePosixPath(payload).as_posix() == payload


def verify_immutable_release(contract: dict[str, Any]) -> None:
    lock = contract["immutable_release"]
    if digest("preauthority/SHA256SUMS.txt") != lock["package_manifest_sha256"]:
        raise ValueError("package manifest anchor changed")
    manifest_raw = (ROOT / "preauthority/SHA256SUMS.txt").read_text(encoding="utf-8")
    rows: list[tuple[str, str]] = []
    for line in manifest_raw.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None:
            raise ValueError("malformed package manifest")
        rows.append((match.group(2), match.group(1)))
    paths = [path for path, _ in rows]
    if len(rows) != lock["package_manifest_entry_count"] or paths != sorted(set(paths)):
        raise ValueError("package manifest count/order mismatch")
    actual = sorted(
        path.relative_to(ROOT / "preauthority").as_posix()
        for path in (ROOT / "preauthority").iterdir()
        if path.is_file()
    )
    if actual != sorted(paths + ["SHA256SUMS.txt"]):
        raise ValueError("preauthority exact file set mismatch")
    for relative, expected in rows:
        if digest(f"preauthority/{relative}") != expected:
            raise ValueError(f"package file hash mismatch: {relative}")

    if digest("preauthority/RESEARCH_LOCK.json") != lock["research_lock_sha256"]:
        raise ValueError("research lock anchor changed")
    research = load_json("preauthority/RESEARCH_LOCK.json")
    mappings = research.get("immutable_package_files")
    if not isinstance(mappings, dict) or len(mappings) != lock["research_lock_mapping_count"]:
        raise ValueError("research lock mapping count mismatch")
    if sorted(mappings) != sorted(set(mappings)):
        raise ValueError("research lock mapping duplicate")
    for relative, expected in mappings.items():
        if digest(f"preauthority/{relative}") != expected:
            raise ValueError(f"research lock hash mismatch: {relative}")

    if digest("preauthority/SOURCE_HASHES.sha256") != lock["source_manifest_sha256"]:
        raise ValueError("source manifest anchor changed")
    if digest("preauthority/ROUTE_EXPECTATION.yaml") != lock["route_expectation_sha256"]:
        raise ValueError("Route expectation anchor changed")
    if digest("independent_da/paper41_DA_REPORT_v2.md") != lock["da_report_sha256"]:
        raise ValueError("DA report anchor changed")
    if digest("independent_da/paper41_DA_REPORT_v2.sha256") != lock["da_sidecar_file_sha256"]:
        raise ValueError("DA sidecar anchor changed")
    sidecar = (ROOT / "independent_da/paper41_DA_REPORT_v2.sha256").read_text(encoding="utf-8")
    match = re.fullmatch(r"([0-9a-f]{64})  paper41_DA_REPORT_v2\.md\n", sidecar)
    if match is None or match.group(1) != lock["da_report_sha256"]:
        raise ValueError("DA sidecar does not bind the report")


def verify_static_inputs(contract: dict[str, Any]) -> None:
    for relative, expected in contract["experiment_freeze"].items():
        if digest(relative) != expected:
            raise ValueError(f"experiment freeze changed: {relative}")
    dependencies = contract["dependencies"]
    checks = {
        "docs/DEPENDENCY_LOCK.json": dependencies["dependency_lock_sha256"],
        SELECTION_REL: dependencies["selection_packet_sha256"],
        ROUTE_SCHEMA_REL: dependencies["route_schema_sha256"],
        ROUTE_SKILL_REL: dependencies["route_skill_encoded_sha256"],
        "docs/inputs/dependencies/paper40_DA_REPORT.md": dependencies["paper40_da_report_sha256"],
        "docs/inputs/dependencies/paper40_DA_REPORT.sha256": dependencies["paper40_da_sidecar_sha256"],
    }
    for relative, expected in checks.items():
        if digest(relative) != expected:
            raise ValueError(f"static dependency changed: {relative}")

    snapshot = ROOT / SNAPSHOT_REL
    paths = sorted(path.relative_to(snapshot).as_posix() for path in snapshot.rglob("*") if path.is_file())
    path_bytes = "".join(f"{path}\n" for path in paths).encode("utf-8")
    rows = "".join(
        f"{digest_bytes((snapshot / path).read_bytes())}  {path}\n" for path in paths
    ).encode("utf-8")
    if len(paths) != dependencies["snapshot_file_count"]:
        raise ValueError("snapshot file count mismatch")
    if digest_bytes(path_bytes) != dependencies["snapshot_path_list_sha256"]:
        raise ValueError("snapshot path list changed")
    if digest_bytes(rows) != dependencies["snapshot_hash_stream_sha256"]:
        raise ValueError("snapshot hash stream changed")


def source_rows(contract: dict[str, Any]) -> list[dict[str, str]]:
    raw = (ROOT / SOURCE_MANIFEST_REL).read_bytes()
    if digest_bytes(raw) != contract["immutable_release"]["source_manifest_sha256"]:
        raise ValueError("portable source manifest changed")
    lines = raw.decode("utf-8").splitlines()
    parsed: list[tuple[str, str, str]] = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  (repo|dependency):(.+)", line)
        if match is None:
            raise ValueError("malformed portable source manifest")
        parsed.append((match.group(2), match.group(3), match.group(1)))
    ids = [f"{kind}:{payload}" for kind, payload, _ in parsed]
    if len(ids) != contract["immutable_release"]["source_manifest_entry_count"]:
        raise ValueError("portable source count mismatch")
    if ids != sorted(set(ids)):
        raise ValueError("portable source IDs are not sorted and unique")

    dependency_paths = {
        "P40_DA_REPORT": "docs/inputs/dependencies/paper40_DA_REPORT.md",
        "P40_DA_REPORT_SIDECAR": "docs/inputs/dependencies/paper40_DA_REPORT.sha256",
    }
    output: list[dict[str, str]] = []
    for kind, payload, expected in parsed:
        if kind == "repo":
            if not safe_id_payload(payload, allow_slash=True):
                raise ValueError(f"unsafe repo ID: {payload}")
            relative = f"{SNAPSHOT_REL}/{payload}.b64"
        else:
            if not safe_id_payload(payload, allow_slash=False) or payload not in dependency_paths:
                raise ValueError(f"unsafe or unknown dependency ID: {payload}")
            relative = dependency_paths[payload]
        path = ROOT / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"source is not a regular non-symlink: {relative}")
        container_bytes = path.read_bytes()
        payload_bytes = b64decode(b"".join(container_bytes.split()), validate=True) if kind == "repo" else container_bytes
        actual = digest_bytes(payload_bytes)
        if actual != expected:
            raise ValueError(f"portable source payload hash mismatch: {kind}:{payload}")
        output.append({
            "expected_sha256": expected,
            "payload_base64": b64encode(payload_bytes).decode("ascii"),
            "source_id": f"{kind}:{payload}",
        })
    return output


def build_packet() -> dict[str, Any]:
    if digest(CONTRACT_REL) != CONTRACT_SHA256:
        raise ValueError("integration contract changed")
    contract = load_json(CONTRACT_REL)
    verify_immutable_release(contract)
    verify_static_inputs(contract)

    selection_raw = (ROOT / SELECTION_REL).read_bytes()
    selection = json.loads(selection_raw)
    route_schema_raw = (ROOT / ROUTE_SCHEMA_REL).read_bytes()
    route_skill_encoded = (ROOT / ROUTE_SKILL_REL).read_bytes()
    rows = source_rows(contract)

    return {
        "candidate_id": "SD-C43",
        "claim_boundary": {
            "changed_models_excluded": [
                "adelic_operator",
                "enlarged_state",
                "Farey_or_Gauss_transfer_operator",
                "history_dependent_cocycle",
                "matrix_trace_or_eigenvalue_clock",
                "Selberg_determinant"
            ],
            "scope": "FROZEN_ROOTED_H_AND_DECLARED_FINITE_REPAIR_FAMILY_ONLY",
            "universal_no_go": False
        },
        "contract_sha256": CONTRACT_SHA256,
        "finite_inventory_input": {
            "max_n": 8,
            "r_max": 3,
            "s": 3,
            "u": [1, 2]
        },
        "integration_chronology": contract["integration_chronology"],
        "marker_ledger": {
            "k": "finite_spin_chain_depth",
            "r": "temporal_repetition_of_putative_primitive_word",
            "s": "inverse_temperature_or_Dirichlet_variable",
            "u": "free_power_marker_for_diagonal_inventory_operator"
        },
        "operator_input": {
            "determinant_formula": "product_n_ge_1(1-u*n^(-s))^phi(n)",
            "determinant_owner": "StateInventoryDiagonal",
            "eigenvalue_one_label": 1,
            "multiplicity_assumption": "full_stable_multiplicity_equals_Euler_phi",
            "primitive_return_owner": False,
            "trace_class_domain": "Re(s)>2",
            "trace_formula": "zeta(s-1)/zeta(s)",
            "trace_log_domain": "|u|<1"
        },
        "positive_control_input": {
            "matrix_power_exponent": 2,
            "matrix_power_word": "01",
            "trace_rotation_words": ["01", "10"]
        },
        "raw_matrices": {
            "L": [[1, 1], [0, 1]],
            "R": [[1, 0], [1, 1]]
        },
        "repair_input": {
            "declared_repairs": [
                "keep_rooted_words",
                "quotient_by_rotations",
                "retain_full_matrix_state",
                "use_diagonal_Q_s",
                "use_matrix_trace_or_eigenvalue",
                "use_word_powers"
            ],
            "scope": "DECLARED_FINITE_REPAIR_FAMILY_ONLY",
            "universal_exhaustiveness": False
        },
        "route_provenance_input": {
            "encoded_skill_sha256": digest_bytes(route_skill_encoded),
            "encoded_skill_utf8": route_skill_encoded.decode("ascii"),
            "route_schema": json.loads(route_schema_raw),
            "route_schema_sha256": digest_bytes(route_schema_raw),
            "route_schema_utf8": route_schema_raw.decode("ascii"),
            "skill_decoded_sha256": contract["dependencies"]["route_skill_decoded_sha256"]
        },
        "schema": "paper41-exact-source-packet-v1",
        "selection_input": {
            "packet": selection,
            "packet_sha256": digest_bytes(selection_raw),
            "packet_utf8": selection_raw.decode("ascii")
        },
        "source_input": {
            "dependency_ids": [
                "dependency:P40_DA_REPORT",
                "dependency:P40_DA_REPORT_SIDECAR"
            ],
            "manifest_sha256": contract["immutable_release"]["source_manifest_sha256"],
            "rows": rows,
            "snapshot_file_count": contract["dependencies"]["snapshot_file_count"]
        },
        "terminal_codes": contract["exact_science"]["terminal_codes"],
        "type_ledger": [
            {"name": "BinaryNecklace", "owns": "cyclic_word_period_and_powers", "not_owned": "rooted_h"},
            {"name": "DynamicalTransferOperator", "owns": "declared_return_powers_only_if_constructed", "not_owned": "not_source_owned_here"},
            {"name": "FareyTraceWord", "owns": "cyclic_trace_and_matrix_power", "not_owned": "frozen_rooted_h_partition_trace"},
            {"name": "KnaufRootedWord", "owns": "M_w_h_and_depth", "not_owned": "cyclic_primitive_class"},
            {"name": "KnaufStableState", "owns": "stable_h_and_multiplicity", "not_owned": "right_append_action"},
            {"name": "LiouvilleStateObservable", "owns": "lambda_of_h", "not_owned": "source_derived_symbolic_cocycle"},
            {"name": "StateInventoryDiagonal", "owns": "trace_and_marked_determinant", "not_owned": "binary_primitive_returns"}
        ],
        "witness_input": {
            "cyclic_clock_pair": ["01", "10"],
            "cyclic_sign_pair": ["001", "010"],
            "direct_limit_generator": ["", "0"],
            "one_letter_words": ["0", "1", "11"],
            "power_clock": {"base": "1", "exponent": 2, "power": "11"},
            "power_sign": {"base": "1", "exponent": 2, "power": "11"},
            "recurrence_prefix_max_length": 3,
            "requested_words": ["", "0", "001", "01", "010", "1", "10", "11"]
        },
        "word_convention": {
            "alphabet": [0, 1],
            "complement": "bitwise_binary_complement",
            "h_column_vector": [1, 0],
            "h_row_vector": [1, 1],
            "product_order": "left_to_right_right_matrix_multiplication"
        }
    }
