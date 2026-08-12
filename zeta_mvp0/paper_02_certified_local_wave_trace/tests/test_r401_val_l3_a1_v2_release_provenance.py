from __future__ import annotations

import copy
import ast
import hashlib
import importlib.util
import json
import os
import shutil
import stat
import struct
import sys
import tempfile
import zlib
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/build_r401_val_l3_a1_v2_release_provenance.py"


def load_builder():
    specification = importlib.util.spec_from_file_location(
        "r401_val_l3_a1_v2_release_for_tests", SOURCE
    )
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


R = load_builder()


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def write_synthetic_delta_pack(
    repository: Path, *, delta_kind: int, declared_size: int | None = None
) -> tuple[str, bytes, int]:
    """Write one checksum-valid pack/index pair without invoking Git."""

    assert delta_kind in (6, 7)
    base = b"A" * 64
    expected = base + b"tail"
    delta = bytes((len(base), len(expected), 0x90, len(base), 4)) + b"tail"

    def oid(payload: bytes) -> str:
        framed = b"blob " + str(len(payload)).encode() + b"\x00" + payload
        return hashlib.sha1(framed, usedforsecurity=False).hexdigest()

    def pack_header(object_type: int, size: int) -> bytes:
        first = (object_type << 4) | (size & 0x0F)
        size >>= 4
        encoded = bytearray((first | (0x80 if size else 0),))
        while size:
            current = size & 0x7F
            size >>= 7
            encoded.append(current | (0x80 if size else 0))
        return bytes(encoded)

    base_oid = oid(base)
    target_oid = oid(expected)
    base_entry = pack_header(3, len(base)) + zlib.compress(base)
    base_offset = 12
    target_offset = base_offset + len(base_entry)
    if delta_kind == 6:
        distance = target_offset - base_offset
        assert 0 < distance < 0x80
        base_reference = bytes((distance,))
    else:
        base_reference = bytes.fromhex(base_oid)
    delta_entry = (
        pack_header(delta_kind, len(delta) if declared_size is None else declared_size)
        + base_reference
        + zlib.compress(delta)
    )
    pack_without_checksum = (
        b"PACK" + struct.pack(">II", 2, 2) + base_entry + delta_entry
    )
    pack_checksum = hashlib.sha1(
        pack_without_checksum, usedforsecurity=False
    ).digest()
    pack_raw = pack_without_checksum + pack_checksum

    locations = {base_oid: base_offset, target_oid: target_offset}
    entries = sorted(locations)
    fanout = []
    cumulative = 0
    for prefix in range(256):
        cumulative += sum(bytes.fromhex(item)[0] == prefix for item in entries)
        fanout.append(cumulative)
    index_without_checksum = b"".join(
        (
            b"\xfftOc",
            struct.pack(">I", 2),
            struct.pack(">256I", *fanout),
            b"".join(bytes.fromhex(item) for item in entries),
            b"".join(
                struct.pack(">I", zlib.crc32(base_entry if item == base_oid else delta_entry))
                for item in entries
            ),
            b"".join(struct.pack(">I", locations[item]) for item in entries),
            pack_checksum,
        )
    )
    index_raw = index_without_checksum + hashlib.sha1(
        index_without_checksum, usedforsecurity=False
    ).digest()

    pack_dir = repository / ".git" / "objects" / "pack"
    pack_dir.mkdir(parents=True)
    stem = f"pack-{pack_checksum.hex()}"
    (pack_dir / f"{stem}.pack").write_bytes(pack_raw)
    (pack_dir / f"{stem}.idx").write_bytes(index_raw)
    return target_oid, expected, len(delta)


def main_checker_receipts(
    candidate_raw: bytes, input_roles: list[dict[str, str]]
) -> dict[str, dict[str, Any]]:
    input_map_sha256 = digest(R.canonical_json_bytes(input_roles))
    receipt = {
        "verification_status": "PASS_MAIN_FREEZE_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": digest(candidate_raw),
        "input_map_sha256": input_map_sha256,
        "size_bytes": len(candidate_raw),
        "promotion_authorized": False,
        "artifacts_written": False,
    }
    return {role: copy.deepcopy(receipt) for role in R.MAIN_CHECKER_RECEIPT_ROLES}


def synthetic_input_roles() -> list[dict[str, str]]:
    return [
        {"role": role, "path": relative, "sha256": f"{index:064x}"}
        for index, (role, relative) in enumerate(R.INPUT_ROLES, start=1)
    ]


def assert_publication_receipt_common(receipt: dict[str, Any]) -> None:
    assert receipt["schema_version"] == 1
    assert receipt["protocol_id"] == R.PROTOCOL_ID
    assert receipt["artifact_status"] == "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY"
    assert receipt["publication_method"] == R.PUBLICATION_METHOD
    for name in (
        "independent_postpublication_verification_performed",
        "scientific_licensing_enabled",
        "production_authorized",
        "scientific_dispatch_performed",
    ):
        assert receipt[name] is False
    for name in (
        "component_status", "milestone_status", "theorem_status", "final_status"
    ):
        assert receipt[name] is None
    for name, mode in (("candidate", "0600"), ("canonical", "0644")):
        binding = receipt[name]
        assert set(binding) == R.PUBLICATION_FILE_BINDING_KEYS
        assert binding["mode"] == mode and binding["nlink"] == 1
        assert binding["size_bytes"] == binding["fingerprint"]["size_bytes"]
        fingerprint = binding["fingerprint"]
        assert set(fingerprint) == R.PUBLICATION_FINGERPRINT_KEYS
        assert all(type(value) is int for value in fingerprint.values())
        assert fingerprint["nlink"] == 1
        assert stat.S_ISREG(fingerprint["mode"])
        assert stat.S_IMODE(fingerprint["mode"]) == int(mode, 8)


def write_raw(path: Path, raw: bytes, *, mode: int = 0o644) -> bytes:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    path.chmod(mode)
    return raw


def write_compact(path: Path, payload: Any) -> bytes:
    return write_raw(path, R.canonical_json_bytes(payload))


def write_pretty(path: Path, payload: Any) -> bytes:
    return write_raw(path, R.pretty_json_bytes(payload))


def producer_payload(claim: str) -> dict[str, Any]:
    return {
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "claim_boundary": claim,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def make_authority(project: Path) -> Any:
    records: list[dict[str, str]] = []
    images: dict[str, bytes] = {}
    for index, (role, relative) in enumerate(R.INPUT_ROLES, start=1):
        if role == "release_builder":
            raw = SOURCE.read_bytes()
        elif role == "prefreeze_review":
            raw = R.PREFREEZE_ACCEPT_RAW
        else:
            raw = R.canonical_json_bytes({"synthetic_role": role, "ordinal": index})
        path = project / relative
        write_raw(path, raw, mode=0o755 if role == "branch_evaluator_binary" else 0o644)
        records.append({"role": role, "path": relative, "sha256": digest(raw)})
        images[role] = raw
    roles = {row["role"]: row for row in records}
    main = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "MAIN_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "INDEPENDENT_PREFREEZE_REVIEW",
        "scientific_licensing_enabled": True,
        "matrix": R.matrix_payload(),
        "matrix_id": R.matrix_id(),
        "input_roles": list(records),
        "machine_freeze_sha256": roles["machine_freeze"]["sha256"],
        "prefreeze_review": {
            "path": roles["prefreeze_review"]["path"],
            "sha256": roles["prefreeze_review"]["sha256"],
            "verdict": "ACCEPT_FOR_FREEZE",
        },
        "serializers": R.formal_serializers(),
        "scheduler": R.formal_scheduler_policy(),
        "limits": R.formal_limits(),
        "status_tables": R.formal_status_tables(),
        "evaluators": {
            "static": {
                "path": roles["static_evaluator"]["path"],
                "sha256": roles["static_evaluator"]["sha256"],
                "abi": "PYTHON_STATIC_ABI_26_STRINGS_V1",
                "argv_count": 26,
            },
            "branch": {
                "source_path": roles["branch_evaluator_source"]["path"],
                "source_sha256": roles["branch_evaluator_source"]["sha256"],
                "binary_path": roles["branch_evaluator_binary"]["path"],
                "binary_sha256": roles["branch_evaluator_binary"]["sha256"],
                "runtime_path": roles["branch_runtime"]["path"],
                "runtime_sha256": roles["branch_runtime"]["sha256"],
                "abi": "CAPD_BRANCH_ABI_12_STRINGS_V1",
                "argv_count": 12,
            },
        },
        "checkers": {
            name: {"path": roles[role]["path"], "sha256": roles[role]["sha256"]}
            for name, role in (
                ("static", "static_checker_source"),
                ("branch", "branch_checker_source"),
                ("composite", "composite_checker_source"),
                ("release_builder", "release_builder"),
            )
        },
        "archive_layout": R.formal_archive_layout(),
        "machine_requirements": R.formal_machine_requirements(),
        "failure_policy": R.formal_failure_policy(),
        "execution_policy": R.formal_execution_policy(),
        "claim_boundary": R.MAIN_FREEZE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    main_raw = R.canonical_json_bytes(main)
    main_path = project / R.MAIN_FREEZE_RELATIVE
    write_raw(main_path, main_raw)
    return R.AuthoritySnapshot(
        project_root=project,
        input_roles=tuple(records),
        role_images=images,
        main=main,
        main_raw=main_raw,
        main_path=main_path,
    )


def make_component(
    authority: Any,
    result: Path,
    component: str,
    run_hash: str,
) -> dict[str, str]:
    main_hash = digest(authority.main_raw)
    roles = {row["role"]: row for row in authority.input_roles}
    component_root = result / component
    entries: list[dict[str, Any]] = []
    certified = f"{component.upper()}_CELL_CERTIFIED"
    for cell in R.matrix_payload():
        bits = cell["precision_bits"]
        slab = cell["slab_id"]
        cell_root = component_root / "cells" / str(bits) / slab
        manifest_path = component_root / "cell_manifests" / str(bits) / f"{slab}.json"
        if component == "static":
            proof_raw = write_compact(
                cell_root / "proof.json", R._plain_copy(producer_payload(R.STATIC_CELL_CLAIM_BOUNDARY))
                if hasattr(R, "_plain_copy") else producer_payload(R.STATIC_CELL_CLAIM_BOUNDARY),
            )
            stdout_raw = write_raw(cell_root / "stdout.txt", b"STATIC_CELL_CERTIFIED\n")
            stderr_raw = write_raw(cell_root / "stderr.txt", b"")
            record_raw = write_compact(
                cell_root / "record.json", producer_payload(R.STATIC_CELL_CLAIM_BOUNDARY)
            )
            file_raw = {
                "proof.json": proof_raw,
                "stdout.txt": stdout_raw,
                "stderr.txt": stderr_raw,
                "record.json": record_raw,
            }
            files = {
                name: {
                    "path": name,
                    "sha256": digest(raw),
                    "size_bytes": len(raw),
                    "serializer": (
                        "CJ_COMPACT_V1"
                        if name in {"proof.json", "record.json"}
                        else "RAW_BYTES"
                    ),
                    "truncated": False,
                }
                for name, raw in file_raw.items()
            }
            manifest = {
                "schema_version": 1,
                "protocol_id": R.PROTOCOL_ID,
                "artifact_role": "STATIC_CELL_MANIFEST",
                "authority": "PRODUCER_ONLY",
                "scientific_licensing_enabled": False,
                "matrix_id": R.matrix_id(),
                "freeze_sha256": main_hash,
                "main_freeze_sha256": main_hash,
                "run_config_sha256": run_hash,
                "cell": cell,
                "semantic_invocation_sha256": digest(R.canonical_json_bytes(cell)),
                "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
                "evaluator_status": certified,
                "record": files["record.json"],
                "files": files,
                "claim_boundary": R.STATIC_CELL_CLAIM_BOUNDARY,
                "component_status": None,
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
            }
            manifest_raw = write_compact(manifest_path, manifest)
        else:
            stdout_raw = write_raw(cell_root / "stdout.txt", b"BRANCH_CELL_CERTIFIED\n")
            stderr_raw = write_raw(cell_root / "stderr.txt", b"")
            record_raw = write_pretty(
                cell_root / "record.json", producer_payload(R.BRANCH_CELL_CLAIM_BOUNDARY)
            )
            relative_root = f"branch/cells/{bits}/{slab}"
            files = {
                f"{relative_root}/stdout.txt": digest(stdout_raw),
                f"{relative_root}/stderr.txt": digest(stderr_raw),
                f"{relative_root}/record.json": digest(record_raw),
            }
            manifest = {
                "schema_version": 1,
                "protocol_id": R.PROTOCOL_ID,
                "artifact_role": "BRANCH_CELL_MANIFEST",
                "authority": "PRODUCER_ONLY",
                "scientific_licensing_enabled": False,
                "matrix_id": R.matrix_id(),
                "freeze_sha256": main_hash,
                "run_config_sha256": run_hash,
                "cell_identity": cell,
                "budgets": R._branch_budgets(),
                "task_binding_sha256": digest(R.pretty_json_bytes(cell)),
                "files": files,
                "claim_boundary": R.BRANCH_CELL_CLAIM_BOUNDARY,
                "component_status": None,
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
            }
            manifest_raw = write_pretty(manifest_path, manifest)
        entries.append(
            {
                "cell": cell,
                "path": f"{component}/cell_manifests/{bits}/{slab}.json",
                "sha256": digest(manifest_raw),
                "size_bytes": len(manifest_raw),
                "evaluator_status": certified,
                "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
            }
        )
    ordered_root = digest(R.canonical_json_bytes(entries))
    evaluator_roles = (
        {"static_evaluator": roles["static_evaluator"]}
        if component == "static"
        else {
            "branch_evaluator_source": roles["branch_evaluator_source"],
            "branch_evaluator_binary": roles["branch_evaluator_binary"],
        }
    )
    common = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_status": "COMPLETE_PRODUCER_ARCHIVE",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": R.matrix_id(),
        "freeze_sha256": main_hash,
        "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash,
        "ordered_cell_manifest_root": ordered_root,
        "evaluator_roles": evaluator_roles,
        "claim_boundary": R.AGGREGATE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    summary = {
        **common,
        "artifact_role": f"{component.upper()}_AGGREGATE_SUMMARY",
        "matrix": R.matrix_payload(),
        "cell_count": 102,
        "status_counts": {certified: 102},
        "scheduler_classification_counts": {"COMMITTED_EVALUATOR_RESULT": 102},
    }
    summary_raw = write_compact(component_root / "aggregate_summary.json", summary)
    manifest = {
        **common,
        "artifact_role": f"{component.upper()}_AGGREGATE_MANIFEST",
        "cell_manifests": entries,
        "summary": {
            "path": f"{component}/aggregate_summary.json",
            "sha256": digest(summary_raw),
            "size_bytes": len(summary_raw),
        },
    }
    manifest_raw = write_compact(component_root / "aggregate_manifest.json", manifest)
    return {
        "aggregate_summary_sha256": digest(summary_raw),
        "aggregate_manifest_sha256": digest(manifest_raw),
        "ordered_cell_manifest_root": ordered_root,
        "summary_size": len(summary_raw),
        "manifest_size": len(manifest_raw),
    }


def make_component_controls(
    authority: Any,
    result: Path,
    component: str,
    run_hash: str,
    chain: dict[str, Any],
) -> dict[str, str]:
    roles = {row["role"]: row for row in authority.input_roles}
    main_hash = digest(authority.main_raw)
    status_value = (
        R.STATIC_COMPONENT_STATUS if component == "static" else R.BRANCH_COMPONENT_STATUS
    )
    checker_claim = (
        R.STATIC_CHECKER_CLAIM_BOUNDARY
        if component == "static"
        else R.BRANCH_CHECKER_CLAIM_BOUNDARY
    )
    postcheck_claim = (
        R.STATIC_POSTCHECK_CLAIM_BOUNDARY
        if component == "static"
        else R.BRANCH_POSTCHECK_CLAIM_BOUNDARY
    )
    replay_counts = R._component_replay_counts(component)
    cross_precision = R._component_cross_precision()
    diagnostics = {
        "ordered_cell_manifest_root": chain["ordered_cell_manifest_root"],
        "aggregate_summary_sha256": chain["aggregate_summary_sha256"],
        "aggregate_manifest_sha256": chain["aggregate_manifest_sha256"],
    }
    checker = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": f"{component.upper()}_INDEPENDENT_CHECKER",
        "authority": "INDEPENDENT_CHECKER",
        "checker_status": R.CHECKER_STATUS,
        "component_status": status_value,
        "scientific_licensing_enabled": False,
        "passed": True,
        "matrix_id": R.matrix_id(),
        "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash,
        "component_aggregate_summary_sha256": chain["aggregate_summary_sha256"],
        "component_aggregate_manifest_sha256": chain["aggregate_manifest_sha256"],
        "replay_counts": replay_counts,
        "cross_precision": cross_precision,
        "diagnostics": diagnostics,
        "failures": [],
        "source_bindings": R._component_source_bindings(roles, component),
        "claim_boundary": checker_claim,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    checker_path = result / f"independent_{component}_checker.json"
    checker_raw = write_compact(checker_path, checker)
    bound = {
        "aggregate_summary": {
            "path": f"{component}/aggregate_summary.json",
            "sha256": chain["aggregate_summary_sha256"],
            "size_bytes": chain["summary_size"],
        },
        "aggregate_manifest": {
            "path": f"{component}/aggregate_manifest.json",
            "sha256": chain["aggregate_manifest_sha256"],
            "size_bytes": chain["manifest_size"],
        },
        "ordered_cell_manifest_root": chain["ordered_cell_manifest_root"],
    }
    postcheck = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": f"{component.upper()}_POSTCHECK",
        "authority": "POSTCHECK_ONLY",
        "postcheck_status": R.POSTCHECK_STATUS,
        "passed": True,
        "checker_path": f"independent_{component}_checker.json",
        "checker_sha256": digest(checker_raw),
        "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash,
        "bound_artifacts": bound,
        "replay_counts": replay_counts,
        "failures": [],
        "scientific_licensing_enabled": False,
        "claim_boundary": postcheck_claim,
        "component_status": status_value,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    postcheck_raw = write_compact(
        result / f"{component.upper()}_POSTCHECK_STATUS.json", postcheck
    )
    return {
        "aggregate_summary_sha256": chain["aggregate_summary_sha256"],
        "aggregate_manifest_sha256": chain["aggregate_manifest_sha256"],
        "ordered_cell_manifest_root": chain["ordered_cell_manifest_root"],
        "checker_sha256": digest(checker_raw),
        "postcheck_sha256": digest(postcheck_raw),
    }


def make_composite(
    authority: Any,
    result: Path,
    run_hash: str,
    component_chains: dict[str, dict[str, str]],
    upstream: dict[str, Any],
    s0: dict[str, Any],
) -> None:
    roles = {row["role"]: row for row in authority.input_roles}
    main_hash = digest(authority.main_raw)
    verbose = R._verbose_component_chains(component_chains)
    generation = digest(R.canonical_json_bytes(verbose))
    common = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_status": "COMPLETE_PRODUCER_ARCHIVE",
        "authority": "PRODUCER_ONLY",
        "matrix_id": R.matrix_id(),
        "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash,
        "component_chains": verbose,
        "archive_generation_sha256": generation,
        "scientific_licensing_enabled": False,
        "claim_boundary": R.RELEASE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    summary = {
        **common,
        "artifact_role": "COMPOSITE_SUMMARY",
        "matrix": R.matrix_payload(),
        "cell_count_per_component": 102,
    }
    summary_raw = write_compact(result / "composite_summary.json", summary)
    manifest = {
        **common,
        "artifact_role": "COMPOSITE_MANIFEST",
        "summary": {
            "path": "composite_summary.json",
            "sha256": digest(summary_raw),
            "size_bytes": len(summary_raw),
        },
    }
    manifest_raw = write_compact(result / "composite_manifest.json", manifest)
    replay_counts = {
        "static_cells": 102,
        "branch_cells": 102,
        "component_chains": 2,
        "upstream_objects": 10,
        "s0_controls": 9,
    }
    cross_precision = {
        "checked_slabs": 51,
        "matching_component_verdicts": 51,
        "passed": True,
    }
    checker = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "COMPOSITE_INDEPENDENT_CHECKER",
        "authority": "INDEPENDENT_CHECKER",
        "checker_status": R.CHECKER_STATUS,
        "component_status": None,
        "scientific_licensing_enabled": True,
        "passed": True,
        "matrix_id": R.matrix_id(),
        "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash,
        "static_chain": verbose["static"],
        "branch_chain": verbose["branch"],
        "upstream_chains": upstream,
        "s0_compatibility": s0,
        "replay_counts": replay_counts,
        "cross_precision": cross_precision,
        "diagnostics": {
            "archive_generation_sha256": generation,
            "composite_summary_sha256": digest(summary_raw),
            "composite_manifest_sha256": digest(manifest_raw),
        },
        "failures": [],
        "source_bindings": R._composite_source_bindings(roles),
        "claim_boundary": R.RELEASE_CLAIM_BOUNDARY,
        "milestone_status": R.COMPOSITE_STATUS,
        "theorem_status": R.COMPOSITE_STATUS,
        "final_status": None,
    }
    checker_raw = write_compact(result / "independent_checker.json", checker)
    postcheck = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "COMPOSITE_POSTCHECK",
        "authority": "POSTCHECK_ONLY",
        "postcheck_status": R.POSTCHECK_STATUS,
        "passed": True,
        "checker_path": "independent_checker.json",
        "checker_sha256": digest(checker_raw),
        "main_freeze_sha256": main_hash,
        "run_config_sha256": run_hash,
        "bound_artifacts": {
            "composite_summary": {
                "path": "composite_summary.json",
                "sha256": digest(summary_raw),
                "size_bytes": len(summary_raw),
            },
            "composite_manifest": {
                "path": "composite_manifest.json",
                "sha256": digest(manifest_raw),
                "size_bytes": len(manifest_raw),
            },
            "archive_generation_sha256": generation,
        },
        "replay_counts": replay_counts,
        "failures": [],
        "scientific_licensing_enabled": True,
        "claim_boundary": R.COMPOSITE_POSTCHECK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": R.COMPOSITE_STATUS,
        "theorem_status": R.COMPOSITE_STATUS,
        "final_status": None,
    }
    write_compact(result / "POSTCHECK_STATUS.json", postcheck)


def formal_fixture(tmp_path: Path) -> tuple[Path, Any, dict[str, Any], dict[str, Any]]:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    authority = make_authority(project)
    result = project / R.RESULT_RELATIVE
    result.mkdir(parents=True)
    run_raw = write_compact(result / "run_config.json", R._expected_run_config(authority, result))
    run_hash = digest(run_raw)
    components: dict[str, dict[str, str]] = {}
    for component in ("static", "branch"):
        archive = make_component(authority, result, component, run_hash)
        components[component] = make_component_controls(
            authority, result, component, run_hash, archive
        )
    zero = "0" * 64
    one = "1" * 64
    upstream = {
        "l1": {f"{name}_sha256": zero for name in (
            "summary", "manifest", "checker", "postcheck", "release"
        )},
        "a415": {f"{name}_sha256": one for name in (
            "summary", "manifest", "checker", "postcheck", "release"
        )},
    }
    s0 = {"replay_sha256": zero, "control_hashes": {"synthetic": one}}
    make_composite(authority, result, run_hash, components, upstream, s0)
    report = (
        f"Status: {R.COMPOSITE_STATUS}\n"
        f"milestone_status = {R.COMPOSITE_STATUS}\n"
        f"theorem_status = {R.COMPOSITE_STATUS}\n"
        "final_status = null\n"
        f"Claim boundary: {R.RELEASE_CLAIM_BOUNDARY}\n"
    )
    write_raw(result / "R401_VAL_L3_A1_REPORT.md", report.encode("ascii"))
    return project, authority, upstream, s0


def patch_external_chains(
    monkeypatch: pytest.MonkeyPatch,
    authority: Any,
    upstream: dict[str, Any],
    s0: dict[str, Any],
) -> None:
    monkeypatch.setattr(R, "validate_formal_main_freeze", lambda _root: authority)
    monkeypatch.setattr(R, "_validate_upstream_chains", lambda _authority: copy.deepcopy(upstream))
    monkeypatch.setattr(R, "_validate_s0_compatibility", lambda _authority: copy.deepcopy(s0))


def make_role11_payload(project: Path) -> dict[str, Any]:
    table = dict(R.INPUT_ROLES)
    python_path = "/usr/bin/python3"
    write_compact(
        project / table["machine_freeze"],
        {
            "python_arb": {"executable_path": python_path},
            "filesystem": {"project_root": str(project)},
        },
    )
    write_compact(project / table["s0_compatibility"], {"synthetic_s0": True})

    def file_binding(relative: str) -> dict[str, Any]:
        path = project / relative
        raw = path.read_bytes()
        info = path.stat()
        return {
            "path": relative,
            "sha256": digest(raw),
            "size_bytes": len(raw),
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "nlink": info.st_nlink,
        }

    tool_anchors: list[dict[str, str]] = []
    for role in R.PREFREEZE_TOOL_ROLES.values():
        binding = file_binding(table[role])
        tool_anchors.append(
            {"role": role, "path": binding["path"], "sha256": binding["sha256"]}
        )
    write_compact(
        project / table["implementation_design_review"],
        {"reviewed_v2_inputs": tool_anchors},
    )

    entries: list[dict[str, Any]] = []
    roles: dict[str, dict[str, Any]] = {}
    for role, relative in R.PREFREEZE_INPUT_ROLES:
        entry = {"role": role, **file_binding(relative)}
        entries.append(entry)
        roles[role] = entry
    tools = {
        name: {key: roles[role][key] for key in R.PREFREEZE_FILE_BINDING_KEYS}
        for name, role in R.PREFREEZE_TOOL_ROLES.items()
    }
    counts_lock = {
        "prefreeze_focused": 2,
        "l3_a1_modules": 3,
        "paper02_full": 4,
    }

    def receipt(binding: dict[str, Any], status_value: str) -> dict[str, Any]:
        return {
            "verification_status": status_value,
            "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
            "candidate_sha256": binding["sha256"],
            "size_bytes": binding["size_bytes"],
            "promotion_authorized": False,
        }

    machine_receipt = receipt(roles["machine_freeze"], "PASS_MACHINE_FREEZE_VERIFY_ONLY")
    s0_receipt = receipt(
        roles["s0_compatibility"], "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
    )
    binary_info = (project / roles["branch_evaluator_binary"]["path"]).stat()
    binary = roles["branch_evaluator_binary"]
    source = roles["branch_evaluator_source"]
    rebuild_receipt = {
        "verification_status": "PASS_SECOND_FRESH_REBUILD",
        "authority": "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY",
        "source_path": source["path"],
        "source_sha256": source["sha256"],
        "persistent_binary_path": binary["path"],
        "persistent_before_sha256": binary["sha256"],
        "persistent_after_sha256": binary["sha256"],
        "persistent_before_device_id": binary_info.st_dev,
        "persistent_before_inode": binary_info.st_ino,
        "persistent_after_device_id": binary_info.st_dev,
        "persistent_after_inode": binary_info.st_ino,
        "persistent_identity_unchanged": True,
        "persistent_overwrite_performed": False,
        "staging_output_sha256": binary["sha256"],
        "staging_output_size_bytes": binary["size_bytes"],
        "staging_output_mode": "0755",
        "staging_output_removed": True,
        "byte_for_byte_equal": True,
        "scientific_evaluator_dispatched": False,
    }
    fixed_argv = R._role11_fixed_argv(project, python_path)
    started = "2026-08-11T00:00:00Z"

    def command(
        index: int,
        *,
        stdout: str,
        semantic: Any,
        pytest_counts: dict[str, int] | None,
        argv: list[str],
    ) -> dict[str, Any]:
        name, kind = R.PREFREEZE_COMMAND_SPECS[index]
        stdout_raw = stdout.encode()
        return {
            "name": name,
            "kind": kind,
            "argv": argv,
            "cwd": str(project),
            "environment": R.PREFREEZE_CLEAN_ENVIRONMENT,
            "return_code": 0,
            "started_at_utc": started,
            "wall_duration_ms": 10,
            "stdout_utf8": stdout,
            "stdout_sha256": digest(stdout_raw),
            "stdout_size_bytes": len(stdout_raw),
            "stderr_utf8": "",
            "stderr_sha256": digest(b""),
            "stderr_size_bytes": 0,
            "pytest_counts": pytest_counts,
            "semantic_receipt": semantic,
        }

    zero_counts = {"passed": 0, "failed": 0, "skipped": 0, "xfailed": 0, "xpassed": 0}
    commands = [
        command(
            0,
            stdout=(
                "machine_freeze_verification=PASS_MACHINE_FREEZE_VERIFY_ONLY "
                f"authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256={roles['machine_freeze']['sha256']} "
                f"size_bytes={roles['machine_freeze']['size_bytes']} promotion_authorized=false\n"
            ),
            semantic=machine_receipt,
            pytest_counts=None,
            argv=fixed_argv["role24_machine_verify"],
        ),
        command(
            1,
            stdout=(
                "s0_compatibility_verification=PASS_S0_COMPATIBILITY_VERIFY_ONLY "
                f"authority=NON_AUTHORITATIVE_VERIFY_ONLY candidate_sha256={roles['s0_compatibility']['sha256']} "
                f"size_bytes={roles['s0_compatibility']['size_bytes']} promotion_authorized=false\n"
            ),
            semantic=s0_receipt,
            pytest_counts=None,
            argv=fixed_argv["role13_compatibility_verify"],
        ),
    ]
    for index, (name, total_name) in enumerate(
        R.PREFREEZE_TEST_RESULT_TOTAL.items(), start=2
    ):
        passed = counts_lock[total_name]
        counts = dict(zero_counts)
        counts["passed"] = passed
        commands.append(
            command(
                index,
                stdout=f"{passed} passed in 0.01s\n",
                semantic=None,
                pytest_counts=counts,
                argv=fixed_argv[name],
            )
        )
    commands.append(
        command(
            5,
            stdout="",
            semantic=None,
            pytest_counts=None,
            argv=fixed_argv["git_diff_check"],
        )
    )
    commands.append(
        command(
            6,
            stdout=R.canonical_json_bytes(rebuild_receipt).decode(),
            semantic=rebuild_receipt,
            pytest_counts=None,
            argv=[
                python_path,
                f"{project}/scripts/run_r401_val_l3_a1_v2_all_slabs.py",
                "--second-fresh-rebuild-only",
                "--output",
                "/tmp/a416-l3a1-v2-role11-rebuild.ABCDEF/"
                "capd_r401_phase_branch_tube_mp_a1",
            ],
        )
    )
    machine_binding = {
        **roles["machine_freeze"],
        "publication_commit_oid": "a" * 40,
        "producer_path": roles["scheduler"]["path"],
        "producer_sha256": roles["scheduler"]["sha256"],
        "verifier_path": roles["release_builder"]["path"],
        "verifier_sha256": roles["release_builder"]["sha256"],
        "verify_receipt": machine_receipt,
        "promotion_authorized": False,
    }
    s0_binding = {
        **roles["s0_compatibility"],
        "publication_commit_oid": "b" * 40,
        "producer_path": roles["s0_adapter"]["path"],
        "producer_sha256": roles["s0_adapter"]["sha256"],
        "verify_receipt": s0_receipt,
        "promotion_authorized": False,
    }
    totals = {}
    for command_name, total_name in R.PREFREEZE_TEST_RESULT_TOTAL.items():
        passed = counts_lock[total_name]
        totals[total_name] = {
            "passed": passed,
            "failed": 0,
            "skipped": 0,
            "xfailed": 0,
            "xpassed": 0,
            "wall_duration_ms": 10,
        }
    return {
        "schema_version": 1,
        "protocol_id": "R401-VAL-L3-A1-PREFREEZE-TESTS",
        "artifact_role": "PREFREEZE_TEST_RECORD",
        "artifact_status": "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW",
        "authority": "PREFREEZE_TEST_EVIDENCE_ONLY",
        "recorded_at_utc": "2026-08-11T00:00:10Z",
        "repository_snapshot": {
            "authority_root": str(project),
            "branch": "main",
            "capture_commit_oid": "c" * 40,
            "capture_tree_oid": "d" * 40,
            "origin_url": "git@github.com:maris205/hilbert-polya-structure.git",
            "origin_main_oid": "c" * 40,
            "live_remote_main_oid": "c" * 40,
            "head_equals_origin_main": True,
            "head_equals_live_remote_main": True,
            "ahead": 0,
            "behind": 0,
            "worktree_clean_before": True,
            "worktree_clean_after": True,
        },
        "evidence_tool_bindings": tools,
        "pre_review_input_roles": entries,
        "prerequisite_bindings": {
            "machine_role10": machine_binding,
            "s0_compatibility_role13": s0_binding,
            "second_fresh_rebuild_replay": {
                "command_result_name": "second_fresh_rebuild",
                "command_result_sha256": digest(R.canonical_json_bytes(commands[6])),
                "semantic_receipt": rebuild_receipt,
            },
            "canonical_absence": {
                "prefreeze_review_role12_exists": False,
                "main_freeze_role54_exists": False,
                "canonical_result_root_exists": False,
                "canonical_operational_root_exists": False,
            },
        },
        "command_results": commands,
        "test_totals": totals,
        "covered_gates": list(R.PREFREEZE_COVERED_GATES),
        "held_out_policy": {
            "held_out_l3_scientific_outputs_read": False,
            "held_out_l3_evaluator_dispatched": False,
            "scientific_evaluator_dispatch_count": 0,
            "new_archive_scope": "TEMPORARY_MOCK_ONLY",
            "s0_archive_access": "READ_ONLY_SEALED_PUBLIC_SIX_CELL",
            "canonical_result_created": False,
        },
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "claim_boundary": R.PREFREEZE_TEST_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


@contextmanager
def private_candidate_dir() -> Iterator[Path]:
    directory = Path(tempfile.mkdtemp(prefix="r401-v2-role24-test-", dir="/tmp"))
    directory.chmod(0o700)
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


@contextmanager
def private_receipt_files(
    receipts: dict[str, dict[str, Any]],
) -> Iterator[dict[str, Path]]:
    directories: list[Path] = []
    paths: dict[str, Path] = {}
    try:
        for role in R.MAIN_CHECKER_RECEIPT_ROLES:
            directory = Path(tempfile.mkdtemp(prefix=f"r401-v2-{role}-receipt-", dir="/tmp"))
            directory.chmod(0o700)
            directories.append(directory)
            path = directory / "receipt.json"
            write_compact(path, receipts[role])
            path.chmod(0o600)
            paths[role] = path
        yield paths
    finally:
        for directory in directories:
            shutil.rmtree(directory)


def rewrite_compact(path: Path, mutator: Any) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    mutator(payload)
    write_compact(path, payload)


def test_synthetic_formal_204_cell_chain_and_exact_68_roles(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    with R.capture_input_generation():
        chain = R._validate_control_chain(authority)
    assert chain["component_chains"]["static"]["ordered_cell_manifest_root"]
    assert chain["component_chains"]["branch"]["ordered_cell_manifest_root"]
    payload = R.build_expected_release(project)
    assert set(payload) == R.RELEASE_KEYS
    assert payload["protocol_id"] == "R401-VAL-L3-A1"
    assert payload["scientific_licensing_enabled"] is True
    assert len(payload["roles"]) == 68
    assert [row["role"] for row in payload["roles"]] == [
        *[role for role, _ in R.INPUT_ROLES],
        "main_freeze",
        *[role for role, _ in R.DOWNSTREAM_ROLES],
    ]


def test_static_and_branch_manifest_mutations_are_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    target = project / R.RESULT_RELATIVE / "static/cell_manifests/128/S000.json"
    rewrite_compact(target, lambda value: value.__setitem__("evaluator_status", "FORGED"))
    with pytest.raises(R.ReleaseError):
        R.build_expected_release(project)


def test_formal_204_namespace_rejects_extra_precision_and_cell_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    extra_precision = project / R.RESULT_RELATIVE / "branch/cells/512"
    extra_precision.mkdir()
    with pytest.raises(R.PathContractError, match="precision-root namespace"):
        R.build_expected_release(project)
    extra_precision.rmdir()
    extra_file = (
        project / R.RESULT_RELATIVE / "static/cells/128/S000/foreign.json"
    )
    write_compact(extra_file, {"foreign": True})
    with pytest.raises(R.PathContractError, match="cell namespace"):
        R.build_expected_release(project)


def test_formal_postcheck_legacy18_and_extra_key_are_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    path = project / R.RESULT_RELATIVE / "STATIC_POSTCHECK_STATUS.json"
    original = json.loads(path.read_text(encoding="utf-8"))
    missing = dict(original)
    missing.pop("scientific_licensing_enabled")
    write_compact(path, missing)
    with pytest.raises(R.ReleaseError, match="key set"):
        R.build_expected_release(project)
    write_compact(path, {**original, "generation": "V2"})
    with pytest.raises(R.ReleaseError, match="key set"):
        R.build_expected_release(project)


def test_main_freeze_exact26_rejects_old15_subset() -> None:
    assert len(R.MAIN_FREEZE_KEYS) == 26
    old_subset = {
        "schema_version", "protocol_id", "artifact_role", "status", "authority",
        "scientific_licensing_enabled", "matrix", "matrix_id", "input_roles",
        "machine_freeze_sha256", "prefreeze_review", "claim_boundary",
        "component_status", "milestone_status", "final_status",
    }
    with pytest.raises(R.ReleaseError, match="key set"):
        R.exact_keys({key: None for key in old_subset}, R.MAIN_FREEZE_KEYS, "role54")


def test_release_schema_is_exact22_without_generation() -> None:
    assert len(R.RELEASE_KEYS) == 22
    assert "generation" not in R.RELEASE_KEYS
    assert R.PROTOCOL_ID == "R401-VAL-L3-A1"
    assert R.RESULT_RELATIVE.as_posix() == "results/r401_val_l3_a1_v2_all_slabs"


@pytest.mark.parametrize(
    "value",
    [
        "/tmp//candidate.json",
        "//tmp/candidate.json",
        "/tmp/./candidate.json",
        "/tmp/a/../candidate.json",
        "/tmp/candidate.json/",
        "/tmp/candidate\\json",
        "/tmp/candidate\x00.json",
    ],
)
def test_cli_paths_retain_and_reject_noncanonical_spelling(value: str) -> None:
    arguments = R.parse_args(["--verify-main-freeze", value])
    assert arguments.verify_main_freeze == value
    with pytest.raises(R.PathContractError):
        R.lexical_absolute(arguments.verify_main_freeze)


@pytest.mark.parametrize(
    ("stdout", "wall_ms", "accepted"),
    [
        ("1 passed in 0.01s\n", 10, True),
        ("9999 passed in 60.00s\n", 60000, True),
        ("1 passed in 61.00s (0:01:01)\n", 61000, True),
        ("1 passed in 600.00s (0:10:00)\n", 600000, True),
        ("0001 passed in 0.01s\n", 10, False),
        ("10000 passed in 0.01s\n", 10, False),
        ("1 passed in 60.01s\n", 60010, False),
        ("1 passed in 600.01s (0:10:00)\n", 600010, False),
        ("1 passed in 1.00s\x85\n", 1000, False),
        ("1 passed in 1.00s\n", 994, False),
        ("1 passed, 1 skipped in 1.00s\n", 1000, False),
    ],
)
def test_role11_pytest_parser_closed_domain(
    stdout: str, wall_ms: int, accepted: bool
) -> None:
    if accepted:
        counts = R._parse_prefreeze_pytest_counts(
            stdout, "pytest", wall_duration_ms=wall_ms
        )
        assert counts["passed"] > 0
        assert sum(value for key, value in counts.items() if key != "passed") == 0
    else:
        with pytest.raises(R.ReleaseError):
            R._parse_prefreeze_pytest_counts(
                stdout, "pytest", wall_duration_ms=wall_ms
            )


def test_role11_parser_differential_corpus_has_zero_mismatch() -> None:
    def load(path: Path, name: str):
        specification = importlib.util.spec_from_file_location(name, path)
        assert specification is not None and specification.loader is not None
        module = importlib.util.module_from_spec(specification)
        sys.modules[name] = module
        specification.loader.exec_module(module)
        return module

    scheduler = load(
        ROOT / "scripts/run_r401_val_l3_a1_v2_all_slabs.py",
        "r401_v2_scheduler_parser_differential",
    )
    checker = load(
        ROOT / "scripts/check_r401_val_l3_a1_v2_static_independent.py",
        "r401_v2_checker_parser_differential",
    )
    corpus = [
        ("1 passed in 0.01s\n", 10),
        ("9999 passed in 60.00s\n", 60000),
        ("1 passed in 61.00s (0:01:01)\n", 61000),
        ("1 passed in 600.00s (0:10:00)\n", 600000),
        ("0001 passed in 0.01s\n", 10),
        ("10000 passed in 0.01s\n", 10),
        ("1 passed in 60.01s\n", 60010),
        ("1 passed in 600.01s (0:10:00)\n", 600010),
        ("1 passed in 1.00s\x85\n", 1000),
        ("1 passed in 1.00s\n", 994),
        ("1 passed, 1 skipped in 1.00s\n", 1000),
        ("1 passed in 61.00s\n", 61000),
        ("9" * 10000 + " passed in 0.01s\n", 10),
    ]

    def accepted(call: Any) -> bool:
        try:
            call()
        except Exception:
            return False
        return True

    for stdout, wall_ms in corpus:
        def scheduler_call() -> None:
            _counts, elapsed_ms = scheduler._v2_role11_parse_pytest(stdout, "diff")
            if elapsed_ms > wall_ms + 5:
                raise ValueError("outer wall mismatch")

        decisions = {
            accepted(scheduler_call),
            accepted(
                lambda: checker._parse_pytest_counts(
                    stdout, "diff", wall_duration_ms=wall_ms
                )
            ),
            accepted(
                lambda: R._parse_prefreeze_pytest_counts(
                    stdout, "diff", wall_duration_ms=wall_ms
                )
            ),
        }
        assert len(decisions) == 1, repr(stdout[:120])


def test_role11_registry_unset_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    expected = {
        "prefreeze_focused": 23,
        "l3_a1_modules": 972,
        "paper02_full": 1951,
    }
    assert R.EXPECTED_PREFREEZE_TEST_PASSED == expected
    assert R._role11_registry() == expected
    monkeypatch.setattr(R, "EXPECTED_PREFREEZE_TEST_PASSED", None)
    with pytest.raises(R.ReleaseError, match="registry is unset"):
        R._role11_registry()


def test_role11_clean_environment_disables_external_git_configuration() -> None:
    assert R.PREFREEZE_CLEAN_ENVIRONMENT == {
        "PATH": "/root/miniconda3/bin:/usr/bin:/bin",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "TZ": "UTC",
        "PYTHONHASHSEED": "0",
        "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
        "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": "/dev/null",
    }


def test_role11_exact22_51_tools_seven_transcripts_and_current_layer(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "role11-project").resolve()
    project.mkdir()
    make_authority(project)
    payload = make_role11_payload(project)
    locked = {"prefreeze_focused": 2, "l3_a1_modules": 3, "paper02_full": 4}
    monkeypatch.setattr(R, "EXPECTED_PREFREEZE_TEST_PASSED", locked)
    monkeypatch.setattr(R, "_validate_role5", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(R, "validate_formal_machine_freeze", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(R, "_validate_s0_payload", lambda *_args, **_kwargs: {})
    monkeypatch.setattr(
        R,
        "_git_verify_commit_bindings",
        lambda _root, _commit, _bindings: payload["repository_snapshot"]["capture_tree_oid"],
    )
    monkeypatch.setattr(
        R, "_git_verify_introduction_binding", lambda *_args, **_kwargs: None
    )
    monkeypatch.setattr(R, "_validate_current_git_snapshot", lambda *_args: None)
    with R.capture_input_generation():
        R._validate_prefreeze_tests_payload(project, payload, require_current=False)
    assert len(R.PREFREEZE_TEST_KEYS) == 22
    assert len(payload["pre_review_input_roles"]) == 51
    assert len(payload["command_results"]) == 7

    missing = dict(payload)
    missing.pop("evidence_tool_bindings")
    with pytest.raises(R.ReleaseError, match="key set"):
        R._validate_prefreeze_tests_payload(project, missing)

    coherent_low_count = copy.deepcopy(payload)
    command = coherent_low_count["command_results"][2]
    command["stdout_utf8"] = "1 passed in 0.01s\n"
    command["stdout_sha256"] = digest(command["stdout_utf8"].encode())
    command["stdout_size_bytes"] = len(command["stdout_utf8"].encode())
    command["pytest_counts"]["passed"] = 1
    coherent_low_count["test_totals"]["prefreeze_focused"]["passed"] = 1
    with R.capture_input_generation():
        with pytest.raises(R.ReleaseError, match="final lock"):
            R._validate_prefreeze_tests_payload(project, coherent_low_count)

    # Historical replay remains valid after downstream namespaces exist;
    # private prepublication replay enforces their live absence.
    with R.capture_input_generation():
        with pytest.raises(R.ReleaseError, match="must be absent"):
            R._validate_prefreeze_tests_payload(project, payload, require_current=True)
    table = dict(R.INPUT_ROLES)
    (project / table["prefreeze_tests"]).unlink()
    (project / table["prefreeze_review"]).unlink()
    (project / R.MAIN_FREEZE_RELATIVE).unlink()
    with R.capture_input_generation():
        R._validate_prefreeze_tests_payload(project, payload, require_current=True)


def test_role11_tool_triangle_rejects_role5_anchor_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "role11-tool-project").resolve()
    project.mkdir()
    make_authority(project)
    payload = make_role11_payload(project)
    monkeypatch.setattr(
        R,
        "EXPECTED_PREFREEZE_TEST_PASSED",
        {"prefreeze_focused": 2, "l3_a1_modules": 3, "paper02_full": 4},
    )
    monkeypatch.setattr(R, "_validate_role5", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(R, "validate_formal_machine_freeze", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(R, "_validate_s0_payload", lambda *_args, **_kwargs: {})
    monkeypatch.setattr(
        R,
        "_git_verify_commit_bindings",
        lambda _root, _commit, _bindings: payload["repository_snapshot"]["capture_tree_oid"],
    )
    monkeypatch.setattr(
        R, "_git_verify_introduction_binding", lambda *_args, **_kwargs: None
    )
    role5_path = project / dict(R.INPUT_ROLES)["implementation_design_review"]
    role5 = json.loads(role5_path.read_text(encoding="utf-8"))
    role5["reviewed_v2_inputs"][0]["sha256"] = "f" * 64
    role5_raw = write_compact(role5_path, role5)
    role5_entry = next(
        row for row in payload["pre_review_input_roles"]
        if row["role"] == "implementation_design_review"
    )
    role5_entry["sha256"] = digest(role5_raw)
    role5_entry["size_bytes"] = len(role5_raw)
    with R.capture_input_generation():
        with pytest.raises(R.ReleaseError, match="stable anchor"):
            R._validate_prefreeze_tests_payload(project, payload)


def test_formal_main_validator_is_exact26_and_type_exact(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "main-project").resolve()
    project.mkdir()
    authority = make_authority(project)
    monkeypatch.setattr(R, "_validate_role5", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(R, "validate_formal_machine_freeze", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        R, "_validate_prefreeze_tests_payload", lambda *_args, **_kwargs: None
    )
    validated = R._validate_main(
        project, authority.main, authority.input_roles, authority.role_images
    )
    assert validated["status"] == "FROZEN_FOR_PRODUCTION"
    float_alias = copy.deepcopy(authority.main)
    float_alias["scheduler"]["static_workers"] = 8.0
    with pytest.raises(R.ReleaseError, match="policy section"):
        R._validate_main(
            project, float_alias, authority.input_roles, authority.role_images
        )
    nested_extra = copy.deepcopy(authority.main)
    nested_extra["limits"]["static"]["coherent_extra"] = 1
    with pytest.raises(R.ReleaseError, match="policy section"):
        R._validate_main(
            project, nested_extra, authority.input_roles, authority.role_images
        )


def test_main_verify_reader_accepts_only_fixed_or_private_candidate(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "reader-project").resolve()
    project.mkdir()
    authority = make_authority(project)
    monkeypatch.setattr(R, "ROOT", project)
    monkeypatch.setattr(R, "_validate_role5", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(R, "validate_formal_machine_freeze", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        R, "_validate_prefreeze_tests_payload", lambda *_args, **_kwargs: None
    )
    canonical_receipt = R.verify_formal_main_freeze_path(authority.main_path)
    assert canonical_receipt["verification_status"] == "PASS_MAIN_FREEZE_VERIFY_ONLY"
    with private_candidate_dir() as directory:
        candidate = directory / "main.json"
        write_raw(candidate, authority.main_raw, mode=0o600)
        receipt = R.verify_formal_main_freeze_path(candidate)
        assert receipt["candidate_sha256"] == digest(authority.main_raw)
    arbitrary = tmp_path / "arbitrary.json"
    write_raw(arbitrary, authority.main_raw, mode=0o600)
    with pytest.raises(R.PathContractError, match="exact /tmp"):
        R.verify_formal_main_freeze_path(arbitrary.resolve())


def test_role54_explicit_candidate_and_publication_authority_route(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "role54-publication-project").resolve()
    (project / R.MAIN_FREEZE_RELATIVE).parent.mkdir(parents=True)
    payload = {
        "formal_role54_synthetic_transaction": True,
        "input_roles": synthetic_input_roles(),
    }
    monkeypatch.setattr(R, "_build_expected_main_freeze", lambda _root: payload)
    with private_candidate_dir() as directory:
        candidate = directory / "main.json"
        R.build_main_freeze_candidate(project, candidate)
        raw = candidate.read_bytes()
        receipts = main_checker_receipts(raw, payload["input_roles"])
        with pytest.raises(R.ReleaseError, match="not authorized"):
            R.publish_main_freeze(
                project,
                candidate,
                checker_receipts=receipts,
                expected_candidate_sha256=digest(raw),
                publication_authority="WRONG",
            )
        with pytest.raises(R.ReleaseError, match="digest mismatch"):
            R.publish_main_freeze(
                project,
                candidate,
                checker_receipts=receipts,
                expected_candidate_sha256="0" * 64,
                publication_authority=R.EXPECTED_MAIN_PUBLICATION_AUTHORITY,
            )
        assert not (project / R.MAIN_FREEZE_RELATIVE).exists()
        publication_receipt = R.publish_main_freeze(
            project,
            candidate,
            checker_receipts=receipts,
            expected_candidate_sha256=digest(raw),
            publication_authority=R.EXPECTED_MAIN_PUBLICATION_AUTHORITY,
        )
        assert set(publication_receipt) == R.MAIN_PUBLICATION_RECEIPT_KEYS
        assert_publication_receipt_common(publication_receipt)
        assert publication_receipt["input_role_count"] == 53
        assert publication_receipt["candidate"]["sha256"] == digest(raw)
        assert publication_receipt["canonical"]["sha256"] == digest(raw)
        assert publication_receipt["checker_receipt_sha256"] == {
            role: digest(R.canonical_json_bytes(receipts[role]))
            for role in R.MAIN_CHECKER_RECEIPT_ROLES
        }
        receipt_attacks = []
        extra = copy.deepcopy(publication_receipt)
        extra["generation"] = "V2"
        receipt_attacks.append(extra)
        type_alias = copy.deepcopy(publication_receipt)
        type_alias["canonical"]["fingerprint"]["size_bytes"] = True
        receipt_attacks.append(type_alias)
        false_gate = copy.deepcopy(publication_receipt)
        false_gate["independent_postpublication_verification_performed"] = True
        receipt_attacks.append(false_gate)
        forged_status = copy.deepcopy(publication_receipt)
        forged_status["final_status"] = "PASS"
        receipt_attacks.append(forged_status)
        wrong_count = copy.deepcopy(publication_receipt)
        wrong_count["input_role_count"] = 52
        receipt_attacks.append(wrong_count)
        for forged in receipt_attacks:
            with pytest.raises(R.ReleaseError):
                R._validate_main_publication_receipt(forged)
    destination = project / R.MAIN_FREEZE_RELATIVE
    assert destination.read_bytes() == R.canonical_json_bytes(payload)
    assert stat.S_IMODE(destination.stat().st_mode) == 0o644
    with private_candidate_dir() as directory:
        candidate = directory / "main.json"
        R.build_main_freeze_candidate(project, candidate)
        with pytest.raises(FileExistsError):
            R.publish_main_freeze(
                project,
                candidate,
                checker_receipts=main_checker_receipts(
                    candidate.read_bytes(), payload["input_roles"]
                ),
                expected_candidate_sha256=digest(candidate.read_bytes()),
                publication_authority=R.EXPECTED_MAIN_PUBLICATION_AUTHORITY,
            )


def test_role54_checker_receipts_are_exact_and_cross_bound() -> None:
    candidate_raw = R.canonical_json_bytes({"input_roles": []})
    receipts = main_checker_receipts(candidate_raw, [])
    validated = R._validate_main_checker_receipts(
        receipts, candidate_raw=candidate_raw, input_roles=[]
    )
    assert tuple(validated) == R.MAIN_CHECKER_RECEIPT_ROLES

    attacks: list[dict[str, dict[str, Any]]] = []
    missing_role = copy.deepcopy(receipts)
    missing_role.pop("branch")
    attacks.append(missing_role)
    extra_key = copy.deepcopy(receipts)
    extra_key["static"]["checker_role"] = "static"
    attacks.append(extra_key)
    for field, value in (
        ("verification_status", "PASS_FORGED"),
        ("authority", "AUTHORITATIVE"),
        ("candidate_sha256", "f" * 64),
        ("input_map_sha256", "e" * 64),
        ("size_bytes", float(len(candidate_raw))),
        ("promotion_authorized", True),
        ("artifacts_written", True),
    ):
        forged = copy.deepcopy(receipts)
        forged["composite"][field] = value
        attacks.append(forged)
    for forged in attacks:
        with pytest.raises(R.ReleaseError):
            R._validate_main_checker_receipts(
                forged, candidate_raw=candidate_raw, input_roles=[]
            )


def test_role54_receipt_paths_are_private_distinct_and_pinned(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    candidate_raw = R.canonical_json_bytes({"input_roles": []})
    receipts = main_checker_receipts(candidate_raw, [])
    with private_receipt_files(receipts) as paths:
        payloads, snapshots = R._read_main_checker_receipt_set(paths)
        assert payloads == receipts
        for snapshot in snapshots.values():
            R._replay_main_checker_receipt(snapshot)
        aliased = dict(paths)
        aliased["branch"] = aliased["static"]
        with pytest.raises(R.PathContractError, match="distinct"):
            R._read_main_checker_receipt_set(aliased)
        original_namespace = R._namespace_signature
        monkeypatch.setattr(
            R,
            "_namespace_signature",
            lambda path: (*original_namespace(path), ("/forged-ancestor", 1, 2, 0o40700)),
        )
        with pytest.raises(R.PathContractError, match="parent/namespace"):
            R._replay_main_checker_receipt(snapshots["static"])


def test_role54_publication_rejects_receipt_inode_drift_before_rename(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "role54-receipt-drift").resolve()
    (project / R.MAIN_FREEZE_RELATIVE).parent.mkdir(parents=True)
    payload = {
        "input_roles": synthetic_input_roles(),
        "formal_role54_synthetic_transaction": True,
    }
    raw = R.canonical_json_bytes(payload)
    monkeypatch.setattr(R, "_build_expected_main_freeze", lambda _root: payload)
    receipts = main_checker_receipts(raw, payload["input_roles"])
    with private_candidate_dir() as candidate_parent, private_receipt_files(receipts) as paths:
        candidate = candidate_parent / "main.json"
        R.build_main_freeze_candidate(project, candidate)
        receipt_payloads, snapshots = R._read_main_checker_receipt_set(paths)
        fired = False

        def hook(phase: str) -> None:
            nonlocal fired
            if phase == "BEFORE_RENAME" and not fired:
                fired = True
                target = paths["branch"]
                saved = target.read_bytes()
                target.unlink()
                write_raw(target, saved, mode=0o600)

        with pytest.raises(R.PathContractError, match="changed"):
            R.publish_main_freeze(
                project,
                candidate,
                checker_receipts=receipt_payloads,
                expected_candidate_sha256=digest(raw),
                publication_authority=R.EXPECTED_MAIN_PUBLICATION_AUTHORITY,
                fault_hook=hook,
                _checker_receipt_snapshots=snapshots,
            )
        assert fired
        assert not (project / R.MAIN_FREEZE_RELATIVE).exists()


def test_role54_postrename_receipt_drift_fails_without_rollback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "role54-postrename-receipt-drift").resolve()
    (project / R.MAIN_FREEZE_RELATIVE).parent.mkdir(parents=True)
    payload = {
        "input_roles": synthetic_input_roles(),
        "formal_role54_synthetic_transaction": True,
    }
    raw = R.canonical_json_bytes(payload)
    monkeypatch.setattr(R, "_build_expected_main_freeze", lambda _root: payload)
    receipts = main_checker_receipts(raw, payload["input_roles"])
    with private_candidate_dir() as candidate_parent, private_receipt_files(receipts) as paths:
        candidate = candidate_parent / "main.json"
        R.build_main_freeze_candidate(project, candidate)
        receipt_payloads, snapshots = R._read_main_checker_receipt_set(paths)

        def hook(phase: str) -> None:
            if phase == "AFTER_POSTPUBLICATION_REPLAY":
                target = paths["composite"]
                saved = target.read_bytes()
                target.unlink()
                write_raw(target, saved, mode=0o600)

        with pytest.raises(R.PathContractError, match="changed"):
            R.publish_main_freeze(
                project,
                candidate,
                checker_receipts=receipt_payloads,
                expected_candidate_sha256=digest(raw),
                publication_authority=R.EXPECTED_MAIN_PUBLICATION_AUTHORITY,
                fault_hook=hook,
                _checker_receipt_snapshots=snapshots,
            )
        destination = project / R.MAIN_FREEZE_RELATIVE
        assert destination.read_bytes() == raw
        assert stat.S_IMODE(destination.stat().st_mode) == 0o644


def test_role54_candidate_enforces_one_mibibyte_cap(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = (tmp_path / "role54-size-cap").resolve()
    project.mkdir()
    payload = {"input_roles": [], "padding": "x" * (1024 * 1024)}
    monkeypatch.setattr(R, "_build_expected_main_freeze", lambda _root: payload)
    with private_candidate_dir() as directory:
        candidate = directory / "main.json"
        with pytest.raises(R.ReleaseError, match="1048576-byte"):
            R.build_main_freeze_candidate(project, candidate)
        assert tuple(directory.iterdir()) == ()


def test_private_candidate_reader_rejects_mode_link_symlink_fifo_and_siblings(
    tmp_path: Path,
) -> None:
    canonical = (tmp_path / "canonical.json").resolve()
    write_compact(canonical, {"canonical": True})

    def read(candidate: Path) -> None:
        R._read_candidate_policy(
            candidate,
            canonical=canonical,
            temporary_mode=0o600,
            maximum_bytes=1024,
        )

    with private_candidate_dir() as directory:
        candidate = directory / "candidate.json"
        write_compact(candidate, {"candidate": True})
        candidate.chmod(0o644)
        with pytest.raises(R.PathContractError, match="mode/link"):
            read(candidate)
    source = (tmp_path / "hardlink-source").resolve()
    write_compact(source, {"candidate": True})
    with private_candidate_dir() as directory:
        candidate = directory / "candidate.json"
        os.link(source, candidate)
        candidate.chmod(0o600)
        with pytest.raises(R.PathContractError, match="unaliased"):
            read(candidate)
    with private_candidate_dir() as directory:
        candidate = directory / "candidate.json"
        candidate.symlink_to(source)
        with pytest.raises(R.PathContractError, match="symlink"):
            read(candidate)
    with private_candidate_dir() as directory:
        candidate = directory / "candidate.json"
        os.mkfifo(candidate, 0o600)
        with pytest.raises(R.PathContractError, match="regular"):
            read(candidate)
    with private_candidate_dir() as directory:
        candidate = directory / "candidate.json"
        write_compact(candidate, {"candidate": True})
        candidate.chmod(0o600)
        write_raw(directory / "sibling", b"foreign\n", mode=0o600)
        with pytest.raises(R.PathContractError, match="singleton"):
            read(candidate)


def test_role68_report_build_verify_publish_and_release_consumes_only(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    destination = project / R.REPORT_RELATIVE
    destination.unlink()
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        raw = R.build_report_candidate(project, candidate)
        assert raw == R.REPORT_EXACT_RAW == candidate.read_bytes()
        assert len(raw) == 371 and len(raw) <= 4096
        assert stat.S_IMODE(candidate.stat().st_mode) == 0o600
        verified = R.verify_report_candidate(project, candidate)
        assert set(verified) == R.REPORT_VERIFY_RECEIPT_KEYS
        assert verified == {
            "verification_status": "PASS_PRODUCTION_REPORT_VERIFY_ONLY",
            "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
            "candidate_sha256": digest(raw),
            "ordered_upstream_roles_sha256": verified[
                "ordered_upstream_roles_sha256"
            ],
            "size_bytes": len(raw),
            "promotion_authorized": False,
            "artifacts_written": False,
        }
        verify_attacks: list[dict[str, Any]] = []
        verify_extra = copy.deepcopy(verified)
        verify_extra["generation"] = "V2"
        verify_attacks.append(verify_extra)
        verify_wrong_candidate = copy.deepcopy(verified)
        verify_wrong_candidate["candidate_sha256"] = "f" * 64
        verify_attacks.append(verify_wrong_candidate)
        verify_wrong_upstream = copy.deepcopy(verified)
        verify_wrong_upstream["ordered_upstream_roles_sha256"] = "e" * 64
        verify_attacks.append(verify_wrong_upstream)
        verify_float_size = copy.deepcopy(verified)
        verify_float_size["size_bytes"] = float(len(raw))
        verify_attacks.append(verify_float_size)
        verify_write = copy.deepcopy(verified)
        verify_write["artifacts_written"] = True
        verify_attacks.append(verify_write)
        for forged in verify_attacks:
            with pytest.raises(R.ReleaseError):
                R._validate_report_verify_receipt(
                    forged,
                    candidate_raw=raw,
                    ordered_upstream_roles_sha256=verified[
                        "ordered_upstream_roles_sha256"
                    ],
                )
        publication = R.publish_report(
            project,
            candidate,
            expected_candidate_sha256=digest(raw),
            publication_authority=R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
        )
        assert set(publication) == R.REPORT_PUBLICATION_RECEIPT_KEYS
        assert_publication_receipt_common(publication)
        assert publication["artifact_role"] == "PRODUCTION_REPORT_PUBLICATION_RECEIPT"
        assert publication["authority"] == R.EXPECTED_REPORT_PUBLICATION_AUTHORITY
        assert publication["claim_boundary"] == R.REPORT_PUBLICATION_CLAIM_BOUNDARY
        assert publication["upstream_role_count"] == 14
        assert publication["ordered_upstream_roles_sha256"] == verified[
            "ordered_upstream_roles_sha256"
        ]
        assert publication["candidate"]["sha256"] == digest(raw)
        assert publication["canonical"]["sha256"] == digest(raw)
        assert destination.read_bytes() == raw
        assert stat.S_IMODE(destination.stat().st_mode) == 0o644
        canonical_verified = R.verify_report_candidate(project, destination)
        assert canonical_verified == verified

        receipt_attacks: list[dict[str, Any]] = []
        extra = copy.deepcopy(publication)
        extra["generation"] = "V2"
        receipt_attacks.append(extra)
        wrong_count = copy.deepcopy(publication)
        wrong_count["upstream_role_count"] = 13
        receipt_attacks.append(wrong_count)
        wrong_digest = copy.deepcopy(publication)
        wrong_digest["ordered_upstream_roles_sha256"] = "f" * 64
        receipt_attacks.append(wrong_digest)
        wrong_archive = copy.deepcopy(publication)
        wrong_archive["archive_generation_sha256"] = "e" * 64
        receipt_attacks.append(wrong_archive)
        type_alias = copy.deepcopy(publication)
        type_alias["canonical"]["fingerprint"]["size_bytes"] = float(len(raw))
        receipt_attacks.append(type_alias)
        false_gate = copy.deepcopy(publication)
        false_gate["scientific_licensing_enabled"] = True
        receipt_attacks.append(false_gate)
        status_forge = copy.deepcopy(publication)
        status_forge["theorem_status"] = R.COMPOSITE_STATUS
        receipt_attacks.append(status_forge)
        for forged in receipt_attacks:
            with pytest.raises(R.ReleaseError):
                R._validate_report_publication_receipt(
                    forged,
                    expected_ordered_upstream_roles_sha256=publication[
                        "ordered_upstream_roles_sha256"
                    ],
                    expected_archive_generation_sha256=publication[
                        "archive_generation_sha256"
                    ],
                )

        with pytest.raises(FileExistsError):
            R.publish_report(
                project,
                candidate,
                expected_candidate_sha256=digest(raw),
                publication_authority=R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
            )

    with private_candidate_dir() as directory:
        release_candidate = directory / "release.json"
        release = R.build_release(project, release_candidate)
        assert len(release["roles"]) == 68
        assert release["roles"][-1] == {
            "role": "production_report",
            "path": R.REPORT_RELATIVE.as_posix(),
            "sha256": digest(R.REPORT_EXACT_RAW),
        }
        R.publish_release(
            project,
            release_candidate,
            expected_candidate_sha256=digest(release_candidate.read_bytes()),
            publication_authority=R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
        )
    # Canonical report verification is historical: a valid later release is
    # replayed strictly but is not folded into the exact14 upstream digest.
    assert R.verify_report_candidate(project, destination) == canonical_verified
    write_raw(
        project / R.RESULT_RELATIVE / R.RELEASE_NAME,
        b"not the exact release image\n",
    )
    with pytest.raises(R.ReleaseError):
        R.verify_report_candidate(project, destination)


def test_role68_report_rejects_wrong_leaf_and_release_destination(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    (project / R.REPORT_RELATIVE).unlink()
    with private_candidate_dir() as directory:
        wrong = directory / "report.md"
        with pytest.raises(R.PathContractError, match="leaf"):
            R.build_report_candidate(project, wrong)
        assert tuple(directory.iterdir()) == ()
    private_directory = tempfile.TemporaryDirectory(dir="/tmp")
    try:
        directory = Path(private_directory.name)
        directory.chmod(0o700)
        candidate = directory / R.REPORT_NAME
        R.build_report_candidate(project, candidate)
        release = project / R.RESULT_RELATIVE / R.RELEASE_NAME
        write_raw(release, b"foreign release\n")
        with pytest.raises(R.PathContractError, match="namespace mismatch"):
            R.verify_report_candidate(project, candidate)
        with pytest.raises(R.PathContractError, match="namespace mismatch"):
            R.publish_report(
                project,
                candidate,
                expected_candidate_sha256=digest(candidate.read_bytes()),
                publication_authority=R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
            )
    finally:
        private_directory.cleanup()
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        with pytest.raises(R.PathContractError, match="namespace mismatch"):
            R.build_report_candidate(project, candidate)
        assert tuple(directory.iterdir()) == ()


def test_role68_report_candidate_reader_rejects_mode_link_and_sibling(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    canonical = project / R.REPORT_RELATIVE
    canonical.chmod(0o600)
    with pytest.raises(R.PathContractError, match="mode/link"):
        R.verify_report_candidate(project, canonical)

    canonical.unlink()
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        R.build_report_candidate(project, candidate)
        candidate.chmod(0o644)
        with pytest.raises(R.PathContractError, match="mode/link"):
            R.verify_report_candidate(project, candidate)

    source = (tmp_path / "report-hardlink-source").resolve()
    write_raw(source, R.REPORT_EXACT_RAW, mode=0o600)
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        os.link(source, candidate)
        with pytest.raises(R.PathContractError, match="unaliased|mode/link"):
            R.verify_report_candidate(project, candidate)

    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        write_raw(candidate, R.REPORT_EXACT_RAW, mode=0o600)
        write_raw(directory / "sibling", b"foreign\n", mode=0o600)
        with pytest.raises(R.PathContractError, match="singleton"):
            R.verify_report_candidate(project, candidate)


def test_role68_prerename_upstream_drift_cleans_stage(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    destination = project / R.REPORT_RELATIVE
    destination.unlink()
    target = project / R.RESULT_RELATIVE / "run_config.json"
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        R.build_report_candidate(project, candidate)
        fired = False

        def hook(phase: str) -> None:
            nonlocal fired
            if phase == "BEFORE_RENAME" and not fired:
                fired = True
                raw = target.read_bytes()
                target.unlink()
                write_raw(target, raw)

        with pytest.raises(R.PathContractError):
            R.publish_report(
                project,
                candidate,
                expected_candidate_sha256=digest(candidate.read_bytes()),
                publication_authority=R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
                fault_hook=hook,
            )
        assert fired and not destination.exists()
        assert not tuple(destination.parent.glob(f".{R.REPORT_NAME}.publish-*"))


def test_role68_posthook_inode_swap_fails_without_rollback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    destination = project / R.REPORT_RELATIVE
    destination.unlink()
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        raw = R.build_report_candidate(project, candidate)
        foreign_inode = 0

        def hook(phase: str) -> None:
            nonlocal foreign_inode
            if phase == "AFTER_POSTPUBLICATION_REPLAY" and foreign_inode == 0:
                destination.unlink()
                write_raw(destination, raw)
                foreign_inode = destination.stat().st_ino

        with pytest.raises(R.PathContractError):
            R.publish_report(
                project,
                candidate,
                expected_candidate_sha256=digest(raw),
                publication_authority=R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
                fault_hook=hook,
            )
        assert destination.read_bytes() == raw
        assert destination.stat().st_ino == foreign_inode
        assert not tuple(destination.parent.glob(f".{R.REPORT_NAME}.publish-*"))


def test_role68_posthook_upstream_drift_fails_without_rollback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    destination = project / R.REPORT_RELATIVE
    destination.unlink()
    target = project / R.RESULT_RELATIVE / "run_config.json"
    with private_candidate_dir() as directory:
        candidate = directory / R.REPORT_NAME
        raw = R.build_report_candidate(project, candidate)
        replacement_inode = 0

        def hook(phase: str) -> None:
            nonlocal replacement_inode
            if phase == "AFTER_POSTPUBLICATION_REPLAY" and replacement_inode == 0:
                same_bytes = target.read_bytes()
                target.unlink()
                write_raw(target, same_bytes)
                replacement_inode = target.stat().st_ino

        with pytest.raises(R.PathContractError):
            R.publish_report(
                project,
                candidate,
                expected_candidate_sha256=digest(raw),
                publication_authority=R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
                fault_hook=hook,
            )
        assert replacement_inode > 0
        assert destination.read_bytes() == raw
        assert stat.S_IMODE(destination.stat().st_mode) == 0o644
        assert not tuple(destination.parent.glob(f".{R.REPORT_NAME}.publish-*"))


def test_release_candidate_build_publish_and_existing_identical_is_fatal(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    with private_candidate_dir() as directory:
        candidate = directory / "release.json"
        built = R.build_release(project, candidate)
        candidate_raw = candidate.read_bytes()
        assert len(built["roles"]) == 68
        assert stat.S_IMODE(candidate.stat().st_mode) == 0o600
        published = R.publish_release(
            project,
            candidate,
            expected_candidate_sha256=digest(candidate_raw),
            publication_authority=R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
        )
        assert set(published) == R.RELEASE_PUBLICATION_RECEIPT_KEYS
        assert_publication_receipt_common(published)
        assert published["artifact_role"] == "RELEASE_PROVENANCE_PUBLICATION_RECEIPT"
        assert published["role_count"] == 68
        assert published["ordered_roles_sha256"] == digest(
            R.canonical_json_bytes(built["roles"])
        )
        assert published["main_freeze_sha256"] == built["main_freeze_sha256"]
        assert published["archive_generation_sha256"] == built["archive_generation_sha256"]
        assert published["candidate"]["sha256"] == digest(candidate_raw)
        assert published["canonical"]["sha256"] == digest(candidate_raw)
    destination = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    before = (destination.read_bytes(), destination.stat().st_ino)
    with private_candidate_dir() as directory:
        second = directory / "release.json"
        R.build_release(project, second)
        with pytest.raises(FileExistsError):
            R.publish_release(
                project,
                second,
                expected_candidate_sha256=digest(second.read_bytes()),
                publication_authority=R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
            )
    assert (destination.read_bytes(), destination.stat().st_ino) == before


def test_live_missing_downstream_fails_before_candidate_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    (project / R.RESULT_RELATIVE / "R401_VAL_L3_A1_REPORT.md").unlink()
    with private_candidate_dir() as directory:
        candidate = directory / "release.json"
        with pytest.raises((FileNotFoundError, R.ReleaseError, R.PathContractError)):
            R.build_release(project, candidate)
        assert tuple(directory.iterdir()) == ()


def test_candidate_terminal_input_swap_cleans_invocation_inode(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    target = project / R.RESULT_RELATIVE / "run_config.json"
    fired = False

    def hook(phase: str) -> None:
        nonlocal fired
        if phase == "AFTER_CANDIDATE_TERMINAL_REPLAY" and not fired:
            fired = True
            raw = target.read_bytes()
            replacement = target.with_name("run_config.replacement")
            replacement.write_bytes(raw)
            replacement.chmod(0o644)
            os.replace(replacement, target)

    with private_candidate_dir() as directory:
        candidate = directory / "release.json"
        with pytest.raises(R.PathContractError, match="changed after snapshot"):
            R.build_release(project, candidate, fault_hook=hook)
        assert fired
        assert tuple(directory.iterdir()) == ()


def test_candidate_foreign_inode_replacement_is_not_deleted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    with private_candidate_dir() as directory:
        candidate = directory / "release.json"
        foreign_inode = 0

        def hook(phase: str) -> None:
            nonlocal foreign_inode
            if phase == "AFTER_CANDIDATE_TERMINAL_REPLAY" and foreign_inode == 0:
                raw = candidate.read_bytes()
                candidate.unlink()
                candidate.write_bytes(raw)
                candidate.chmod(0o600)
                foreign_inode = candidate.stat().st_ino

        with pytest.raises(R.PathContractError, match="foreign inode"):
            R.build_release(project, candidate, fault_hook=hook)
        assert candidate.exists()
        assert candidate.stat().st_ino == foreign_inode


def test_postrename_failure_never_rolls_back_published_name(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    destination = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    with private_candidate_dir() as directory:
        candidate = directory / "release.json"
        R.build_release(project, candidate)
        expected_raw = candidate.read_bytes()
        foreign_inode = 0

        def hook(phase: str) -> None:
            nonlocal foreign_inode
            if phase == "AFTER_POSTPUBLICATION_REPLAY" and foreign_inode == 0:
                destination.unlink()
                destination.write_bytes(expected_raw)
                destination.chmod(0o644)
                foreign_inode = destination.stat().st_ino

        with pytest.raises(R.PathContractError):
            R.publish_release(
                project,
                candidate,
                expected_candidate_sha256=digest(expected_raw),
                publication_authority=R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
                fault_hook=hook,
            )
        assert destination.exists()
        assert destination.stat().st_ino == foreign_inode


def test_foreign_release_stage_is_not_broadly_ignored(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    result = project / R.RESULT_RELATIVE
    with private_candidate_dir() as directory:
        candidate = directory / "release.json"
        R.build_release(project, candidate)
        foreign = result / f".{R.RELEASE_NAME}.publish-{'a' * 32}"
        write_raw(foreign, b"foreign\n")
        with pytest.raises(R.PathContractError, match="namespace mismatch"):
            R.publish_release(
                project,
                candidate,
                expected_candidate_sha256=digest(candidate.read_bytes()),
                publication_authority=R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
            )
        assert foreign.read_bytes() == b"foreign\n"
        assert not (result / R.RELEASE_NAME).exists()


def test_write_once_cleanup_refuses_foreign_stage_inode(tmp_path: Path) -> None:
    parent = (tmp_path / "publication").resolve()
    parent.mkdir()
    destination = parent / "authority.json"
    foreign: Path | None = None

    def hook(phase: str) -> None:
        nonlocal foreign
        if phase == "AFTER_STAGE_WRITE" and foreign is None:
            stages = list(parent.glob(".authority.json.publish-*"))
            assert len(stages) == 1
            foreign = stages[0]
            foreign.unlink()
            write_raw(foreign, b"foreign\n", mode=0o600)

    with R.capture_input_generation():
        with pytest.raises(R.PathContractError, match="foreign inode"):
            R.write_once(destination, b"authority\n", fault_hook=hook)
    assert foreign is not None and foreign.read_bytes() == b"foreign\n"
    assert not destination.exists()


def test_write_once_two_fork_race_has_exactly_one_winner(tmp_path: Path) -> None:
    parent = (tmp_path / "race").resolve()
    parent.mkdir()
    destination = parent / "authority.json"
    start_read, start_write = os.pipe()
    children: list[int] = []
    for _ in range(2):
        child = os.fork()
        if child == 0:
            try:
                os.close(start_write)
                os.read(start_read, 1)
                with R.capture_input_generation():
                    R.write_once(destination, b"winner\n")
            except BaseException:
                os._exit(1)
            os._exit(0)
        children.append(child)
    os.close(start_read)
    os.write(start_write, b"xx")
    os.close(start_write)
    statuses = [os.waitpid(child, 0)[1] for child in children]
    exit_codes = [os.waitstatus_to_exitcode(status) for status in statuses]
    assert sorted(exit_codes) == [0, 1]
    assert destination.read_bytes() == b"winner\n"
    assert list(parent.glob(".authority.json.publish-*")) == []


def test_write_once_rejects_lexical_parent_swap_immediately_before_rename(
    tmp_path: Path,
) -> None:
    parent = (tmp_path / "publication-parent").resolve()
    replacement = (tmp_path / "replacement-parent").resolve()
    parent.mkdir()
    replacement.mkdir()
    destination = parent / "authority.json"
    fired = False

    def hook(phase: str) -> None:
        nonlocal fired
        if phase == "BEFORE_RENAME" and not fired:
            fired = True
            parent.rename(tmp_path / "old-publication-parent")
            replacement.rename(parent)

    with R.capture_input_generation():
        with pytest.raises(R.PathContractError, match="parent changed"):
            R.write_once(destination, b"authority\n", fault_hook=hook)
    assert fired
    assert not destination.exists()
    assert list((tmp_path / "old-publication-parent").iterdir()) == []


def test_read_snapshot_fifo_open_race_is_nonblocking(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = (tmp_path / "racing-input").resolve()
    target.write_bytes(b"regular\n")
    original_open = R.os.open
    fired = False

    def racing_open(path: Any, flags: int, *args: Any, **kwargs: Any) -> int:
        nonlocal fired
        if os.fspath(path) == os.fspath(target) and not fired:
            fired = True
            target.unlink()
            os.mkfifo(target, 0o600)
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(R.os, "open", racing_open)
    with pytest.raises(R.PathContractError):
        R.read_snapshot(target)
    assert fired


def test_read_snapshot_rejects_oversize_and_parent_swap_same_leaf_inode(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    oversize = (tmp_path / "oversize").resolve()
    oversize.write_bytes(b"123456789")
    with pytest.raises(R.PathContractError, match="exceeds bounded"):
        R.read_snapshot(oversize, maximum_bytes=8)

    active = (tmp_path / "active").resolve()
    replacement = (tmp_path / "replacement").resolve()
    active.mkdir()
    replacement.mkdir()
    target = active / "input"
    target.write_bytes(b"same-leaf-inode\n")
    inode = target.stat().st_ino
    original_open = R.os.open
    fired = False

    def swapping_open(path: Any, flags: int, *args: Any, **kwargs: Any) -> int:
        nonlocal fired
        if os.fspath(path) == os.fspath(target) and not fired:
            fired = True
            old = tmp_path / "old-active"
            active.rename(old)
            replacement.rename(active)
            (old / "input").rename(active / "input")
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(R.os, "open", swapping_open)
    with pytest.raises(R.PathContractError, match="ancestor|changed|race"):
        R.read_snapshot(target)
    assert fired
    assert target.stat().st_ino == inode


def test_absent_namespace_is_part_of_terminal_generation(tmp_path: Path) -> None:
    target = (tmp_path / "must-remain-absent").resolve()
    with pytest.raises(R.ReleaseError, match="appeared before terminal replay"):
        with R.capture_input_generation():
            R._assert_absent_namespace(target, "synthetic forbidden namespace")
            write_raw(target, b"late arrival\n")


def test_cli_requires_one_explicit_mode_and_publication_credentials() -> None:
    with pytest.raises(SystemExit):
        R.parse_args([])
    candidate = "/tmp/nonexistent-private/candidate.json"
    assert R.main([
        "--publish-release", candidate,
        "--expected-candidate-sha256", "0" * 64,
        "--publication-authority", "WRONG",
    ]) == 1
    assert R.main([
        "--publish-main-freeze", candidate,
        "--expected-candidate-sha256", "0" * 64,
        "--publication-authority", R.EXPECTED_MAIN_PUBLICATION_AUTHORITY,
    ]) == 1
    assert R.main([
        "--verify-only", "--role20-receipt", candidate,
    ]) == 1
    assert R.main([
        "--publish-report", "/tmp/private-report/R401_VAL_L3_A1_REPORT.md",
    ]) == 1
    assert R.main([
        "--publish-report", "/tmp/private-report/R401_VAL_L3_A1_REPORT.md",
        "--expected-candidate-sha256", "0" * 64,
        "--publication-authority", R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
        "--role20-receipt", candidate,
    ]) == 1


def test_cli_publication_success_emits_only_canonical_receipt(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    receipt = {"publication_receipt": True, "ordinal": 24}
    monkeypatch.setattr(R, "publish_release", lambda *_args, **_kwargs: receipt)
    assert R.main([
        "--publish-release", "/tmp/private-release/release.json",
        "--expected-candidate-sha256", "0" * 64,
        "--publication-authority", R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
    ]) == 0
    captured = capsys.readouterr()
    assert captured.out.encode("utf-8") == R.canonical_json_bytes(receipt)
    assert captured.err == ""


def test_role68_cli_modes_emit_only_the_locked_transport(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    candidate = "/tmp/private-report/R401_VAL_L3_A1_REPORT.md"
    verify_receipt = {
        "verification_status": "PASS_PRODUCTION_REPORT_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": digest(R.REPORT_EXACT_RAW),
        "ordered_upstream_roles_sha256": "a" * 64,
        "size_bytes": len(R.REPORT_EXACT_RAW),
        "promotion_authorized": False,
        "artifacts_written": False,
    }
    publication_receipt = {
        "publication_receipt": "synthetic exact-output probe",
        "ordinal": 68,
    }
    monkeypatch.setattr(
        R, "build_report_candidate",
        lambda *_args, **_kwargs: R.REPORT_EXACT_RAW,
    )
    assert R.main(["--build-report-candidate", candidate]) == 0
    captured = capsys.readouterr()
    assert captured.out == (
        f"report_candidate_sha256={digest(R.REPORT_EXACT_RAW)} "
        "upstream_roles=14\n"
    )
    assert captured.err == ""

    monkeypatch.setattr(
        R, "verify_report_candidate",
        lambda *_args, **_kwargs: verify_receipt,
    )
    assert R.main(["--verify-report", candidate]) == 0
    captured = capsys.readouterr()
    assert captured.out.encode("utf-8") == R.canonical_json_bytes(verify_receipt)
    assert captured.err == ""

    monkeypatch.setattr(
        R, "publish_report",
        lambda *_args, **_kwargs: publication_receipt,
    )
    assert R.main([
        "--publish-report", candidate,
        "--expected-candidate-sha256", "0" * 64,
        "--publication-authority", R.EXPECTED_REPORT_PUBLICATION_AUTHORITY,
    ]) == 0
    captured = capsys.readouterr()
    assert captured.out.encode("utf-8") == R.canonical_json_bytes(
        publication_receipt
    )
    assert captured.err == ""


@pytest.mark.parametrize(
    "forged",
    [
        "status: FORGED",
        "Authority: PRODUCTION",
        "production_authorized = true",
        "scientific licensing enabled: true",
        "scientific_dispatch_performed -> true",
        "MILESTONE STATUS : FORGED",
        "Claim-Boundary: broader",
    ],
)
def test_report_rejects_case_whitespace_and_decorated_authority(
    tmp_path: Path, forged: str
) -> None:
    path = (tmp_path / "report.md").resolve()
    exact = R.REPORT_EXACT_RAW
    write_raw(path, exact + (forged + "\n").encode("ascii"))
    with pytest.raises(R.ReleaseError, match="authority declarations"):
        R._validate_report(path)
    write_raw(path, exact + "Ａuthority: forged\n".encode("utf-8"))
    with pytest.raises(R.ReleaseError, match="ASCII"):
        R._validate_report(path)


@pytest.mark.parametrize(
    "mutated",
    [
        lambda raw: b"narrative appendix\n" + raw,
        lambda raw: raw + b"benign appendix\n",
        lambda raw: raw[:-1],
        lambda raw: raw.replace(b"Status:", b"Status :", 1),
    ],
)
def test_report_is_exact_five_line_lf_terminated_image(
    tmp_path: Path, mutated: Any
) -> None:
    path = (tmp_path / "report.md").resolve()
    write_raw(path, R.REPORT_EXACT_RAW)
    assert R._validate_report(path) == R.REPORT_EXACT_RAW
    write_raw(path, mutated(R.REPORT_EXACT_RAW))
    with pytest.raises(R.ReleaseError):
        R._validate_report(path)


def test_release_candidate_rejects_role_alias_order_hash_and_extra_generation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, authority, upstream, s0 = formal_fixture(tmp_path)
    patch_external_chains(monkeypatch, authority, upstream, s0)
    expected = R.build_expected_release(project)

    def reject(mutator: Any) -> None:
        payload = copy.deepcopy(expected)
        mutator(payload)
        with private_candidate_dir() as directory:
            candidate = directory / "release.json"
            write_compact(candidate, payload)
            candidate.chmod(0o600)
            with pytest.raises(R.ReleaseError, match="68-role DAG"):
                R.verify_release_candidate(project, candidate)

    reject(lambda payload: payload["roles"].__setitem__(1, payload["roles"][0]))
    reject(lambda payload: payload["roles"].__setitem__(slice(0, 2), reversed(payload["roles"][:2])))
    reject(lambda payload: payload["roles"][10].__setitem__("sha256", "f" * 64))
    reject(lambda payload: payload.__setitem__("generation", "V2"))
    assert R.main([
        "--verify-only",
        "--publication-authority", R.EXPECTED_RELEASE_PUBLICATION_AUTHORITY,
    ]) == 1


def test_source_has_no_subprocess_evaluator_or_publication_fallback() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    assert not any(
        isinstance(node, (ast.Import, ast.ImportFrom))
        and (
            (isinstance(node, ast.Import) and any(alias.name == "subprocess" for alias in node.names))
            or (isinstance(node, ast.ImportFrom) and node.module == "subprocess")
        )
        for node in ast.walk(tree)
    )
    assert not any(
        isinstance(node, ast.Name) and node.id == "subprocess"
        for node in ast.walk(tree)
    )
    assert "os.rename(" not in source
    assert "os.replace(" not in source
    assert "os.link(" not in source
    assert "renameat2" in source and "RENAME_NOREPLACE" in source


@pytest.mark.parametrize("delta_kind", (6, 7))
def test_pure_git_synthetic_ofs_ref_delta_binds_instruction_size(
    tmp_path: Path, delta_kind: int,
) -> None:
    valid = (tmp_path / f"valid-{delta_kind}").resolve()
    target_oid, expected, instruction_size = write_synthetic_delta_pack(
        valid, delta_kind=delta_kind
    )
    assert instruction_size != len(expected)
    assert R._git_read_object(valid, target_oid) == ("blob", expected)

    malformed = (tmp_path / f"malformed-{delta_kind}").resolve()
    malformed_oid, malformed_expected, malformed_instruction_size = (
        write_synthetic_delta_pack(
            malformed, delta_kind=delta_kind, declared_size=len(expected)
        )
    )
    assert (malformed_oid, malformed_expected, malformed_instruction_size) == (
        target_oid, expected, instruction_size
    )
    with pytest.raises(R.ReleaseError, match="delta instruction size mismatch"):
        R._git_read_object(malformed, malformed_oid)


def test_git_publication_commit_must_be_single_parent_introduction(
    tmp_path: Path,
) -> None:
    project = (tmp_path / "git-project").resolve()
    objects = project / ".git/objects"
    objects.mkdir(parents=True)

    def store(kind: str, payload: bytes) -> str:
        framed = kind.encode() + b" " + str(len(payload)).encode() + b"\x00" + payload
        oid = hashlib.sha1(framed, usedforsecurity=False).hexdigest()
        write_raw(objects / oid[:2] / oid[2:], zlib.compress(framed))
        return oid

    def tree_entry(mode: bytes, name: bytes, oid: str) -> bytes:
        return mode + b" " + name + b"\x00" + bytes.fromhex(oid)

    def commit(tree: str, parents: list[str], message: bytes) -> str:
        header = [f"tree {tree}".encode()]
        header.extend(f"parent {parent}".encode() for parent in parents)
        header.extend(
            [b"author Test <test@example.invalid> 0 +0000", b"committer Test <test@example.invalid> 0 +0000"]
        )
        return store("commit", b"\n".join(header) + b"\n\n" + message + b"\n")

    empty_tree = store("tree", b"")
    parent = commit(empty_tree, [], b"parent")
    raw = b'{"published":true}\n'
    blob = store("blob", raw)
    leaf = store("tree", tree_entry(b"100644", b"ROLE10.json", blob))
    route = store("tree", tree_entry(b"40000", b"route_a_wave_trace", leaf))
    root_tree = store("tree", tree_entry(b"40000", b"research", route))
    introduction = commit(root_tree, [parent], b"introduce")
    later = commit(root_tree, [introduction], b"later containing commit")
    merge = commit(root_tree, [parent, introduction], b"ambiguous merge")
    deleted = commit(empty_tree, [introduction], b"delete")
    readded = commit(root_tree, [deleted], b"readd")
    orphan = commit(root_tree, [parent], b"unreachable introduction")
    binding = {
        "path": "research/route_a_wave_trace/ROLE10.json",
        "sha256": digest(raw),
        "mode": "0644",
    }
    R._git_verify_introduction_binding(
        project, introduction, binding, descendant_oid=later
    )
    with pytest.raises(R.ReleaseError, match="introduction"):
        R._git_verify_introduction_binding(project, later, binding)
    with pytest.raises(R.ReleaseError, match="exactly one parent"):
        R._git_verify_introduction_binding(project, merge, binding)
    with pytest.raises(R.ReleaseError, match="missing"):
        R._git_verify_introduction_binding(
            project, introduction, binding, descendant_oid=readded
        )
    with pytest.raises(R.ReleaseError, match="unreachable"):
        R._git_verify_introduction_binding(
            project, orphan, binding, descendant_oid=later
        )
    with pytest.raises(R.ReleaseError, match="deletion/re-add"):
        R._git_verify_introduction_binding(project, readded, binding)

    valid_identity = [
        b"author Test <test@example.invalid> 0 +0000",
        b"committer Test <test@example.invalid> 0 +0000",
    ]
    malformed_headers = [
        [f"tree {root_tree}".encode(), f"tree {root_tree}".encode(), *valid_identity],
        [f"tree {root_tree}".encode(), b"parent malformed", *valid_identity],
        [f"tree {root_tree}".encode(), b" continued signature", *valid_identity],
        [f"tree {root_tree}".encode(), valid_identity[0]],
        [f"tree {root_tree}".encode(), valid_identity[0], valid_identity[0], valid_identity[1]],
        [f"tree {root_tree}".encode(), b"encoding UTF-8", *valid_identity],
        [
            f"tree {root_tree}".encode(),
            b"author Test <test@example.invalid> 01 +0000",
            valid_identity[1],
        ],
        [
            f"tree {root_tree}".encode(),
            b"author Test <test@example.invalid> 0 +1460",
            valid_identity[1],
        ],
    ]
    for headers in malformed_headers:
        malformed = store("commit", b"\n".join(headers) + b"\n\nmalformed\n")
        with pytest.raises(R.ReleaseError):
            R._git_commit_tree(project, malformed)
        with pytest.raises(R.ReleaseError):
            R._git_commit_parents(project, malformed)


def test_four_legacy_publications_are_reachable_introductions_from_terminal() -> None:
    terminal = "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0"
    R._git_verify_commit_bindings(R.ROOT, terminal, R.ROLE5_LEGACY_ARTIFACTS)
    for artifact in R.ROLE5_LEGACY_ARTIFACTS:
        live = R.ROOT / artifact["path"]
        binding = {
            **artifact,
            "mode": f"{stat.S_IMODE(live.stat().st_mode):04o}",
        }
        R._git_verify_introduction_binding(
            R.ROOT,
            artifact["publication_commit"],
            binding,
            descendant_oid=terminal,
        )


def test_role5_exact15_19_reviewed_live_blob_mode_and_legacy_introductions(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    project = (tmp_path / "role5-project").resolve()
    objects = project / ".git/objects"
    objects.mkdir(parents=True)

    def store(kind: str, payload: bytes) -> str:
        framed = kind.encode() + b" " + str(len(payload)).encode() + b"\x00" + payload
        oid = hashlib.sha1(framed, usedforsecurity=False).hexdigest()
        write_raw(objects / oid[:2] / oid[2:], zlib.compress(framed))
        return oid

    def commit(tree: str, parents: list[str], message: str) -> str:
        lines = [f"tree {tree}", *[f"parent {parent}" for parent in parents]]
        lines.extend(
            [
                "author Test <test@example.invalid> 0 +0000",
                "committer Test <test@example.invalid> 0 +0000",
            ]
        )
        return store("commit", ("\n".join(lines) + f"\n\n{message}\n").encode())

    files: dict[str, tuple[bytes, int]] = {}
    records: list[dict[str, str]] = []
    executable_role = R.ROLE5_REVIEWED_ROLES[0]
    for index, role in enumerate(R.ROLE5_REVIEWED_ROLES):
        relative = f"reviewed/{index:02d}-{role}.txt"
        raw = f"reviewed:{role}\n".encode()
        mode = 0o755 if role == executable_role else 0o644
        write_raw(project / relative, raw, mode=mode)
        files[relative] = (raw, mode)
        records.append({"role": role, "path": relative, "sha256": digest(raw)})
    synthetic_legacy: list[dict[str, Any]] = []
    for role in range(10, 14):
        relative = f"legacy/role{role}.json"
        raw = R.canonical_json_bytes({"legacy_role": role})
        write_raw(project / relative, raw)
        files[relative] = (raw, 0o644)
        synthetic_legacy.append(
            {
                "role": role,
                "path": relative,
                "sha256": digest(raw),
                "publication_commit": "pending",
            }
        )

    root_node: dict[str, Any] = {}
    for relative, (raw, mode) in files.items():
        node = root_node
        parts = relative.split("/")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = (raw, mode)

    def store_tree(node: dict[str, Any]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, value in node.items():
            encoded = name.encode()
            if isinstance(value, dict):
                oid = store_tree(value)
                entries.append(
                    (encoded + b"/", b"40000 " + encoded + b"\x00" + bytes.fromhex(oid))
                )
            else:
                raw, mode = value
                oid = store("blob", raw)
                git_mode = b"100755" if mode & 0o111 else b"100644"
                entries.append(
                    (encoded, git_mode + b" " + encoded + b"\x00" + bytes.fromhex(oid))
                )
        return store("tree", b"".join(payload for _key, payload in sorted(entries)))

    empty = store("tree", b"")
    parent = commit(empty, [], "empty parent")
    reviewed_tree = store_tree(root_node)
    reviewed_commit = commit(reviewed_tree, [parent], "reviewed and introduced")

    def write_index() -> bytes:
        entries: list[bytes] = []
        for relative, (raw, mode) in sorted(
            files.items(), key=lambda item: item[0].encode("utf-8")
        ):
            encoded = relative.encode("utf-8")
            oid = store("blob", raw)
            fixed = struct.pack(
                ">LLLLLLLLLL20sH",
                0, 0, 0, 0, 0, 0,
                0o100755 if mode & 0o111 else 0o100644,
                0, 0, len(raw), bytes.fromhex(oid), min(len(encoded), 0x0FFF),
            )
            entry = fixed + encoded + b"\x00"
            entry += b"\x00" * (-len(entry) % 8)
            entries.append(entry)
        body = b"DIRC" + struct.pack(">II", 2, len(entries)) + b"".join(entries)
        image = body + hashlib.sha1(body, usedforsecurity=False).digest()
        write_raw(project / ".git/index", image)
        return image

    index_image = write_index()
    write_raw(project / ".git/HEAD", b"ref: refs/heads/main\n")
    write_raw(
        project / ".git/refs/heads/main", f"{reviewed_commit}\n".encode()
    )
    write_raw(
        project / ".git/refs/remotes/origin/main",
        f"{reviewed_commit}\n".encode(),
    )
    fetch_head = (
        f"{reviewed_commit}\t\tbranch 'main' of synthetic.invalid\n".encode()
    )
    write_raw(project / ".git/FETCH_HEAD", fetch_head)
    for artifact in synthetic_legacy:
        artifact["publication_commit"] = reviewed_commit
    monkeypatch.setattr(R, "ROLE5_LEGACY_ARTIFACTS", tuple(synthetic_legacy))
    monkeypatch.setattr(R, "ROLE5_LEGACY_TERMINAL_COMMIT", reviewed_commit)
    reviewed_paths = {
        row["role"]: row["path"] for row in records
    }
    monkeypatch.setattr(
        R,
        "INPUT_ROLES",
        tuple(
            (role, reviewed_paths.get(role, relative))
            for role, relative in R.INPUT_ROLES
        ),
    )
    payload = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL",
        "status": "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1",
        "authority": "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "legacy_attempt": {
            "attempt_id": "A416_L3_A1_CONTROL_ATTEMPT_1",
            "status": "WITHDRAWN_NON_LICENSING",
            "terminal_commit": reviewed_commit,
            "published_artifacts": synthetic_legacy,
            "defects": list(R.ROLE5_LEGACY_DEFECTS),
            "supersession_rule": R.ROLE5_SUPERSESSION_RULE,
        },
        "reviewed_v2_inputs": records,
        "review": {
            "reviewer_independent_of_attempt1_author": True,
            "verdict": "ACCEPT_CONTROL_PLANE_V2_DESIGN",
            "p0_count": 0,
            "p1_count": 0,
            "p2_count": 0,
            "reviewed_commit": reviewed_commit,
            "map_matches_contract": True,
            "legacy_bytes_unchanged": True,
            "scientific_protocol_unchanged": True,
        },
        "claim_boundary": R.ROLE5_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    R._validate_role5(project, payload, records)
    executable = project / records[0]["path"]
    executable.chmod(0o644)
    with pytest.raises(R.ReleaseError, match="live/blob/mode"):
        R._validate_role5(project, payload, records)
    executable.chmod(0o755)
    extra = {**payload, "generation": "V2"}
    with pytest.raises(R.ReleaseError, match="key set"):
        R._validate_role5(project, extra, records)

    # The private verifier uses only the final reviewed tree.  Canonical role
    # 5 and every later V2 edge remain absent at this prepublication boundary.
    (project / "research/route_a_wave_trace").mkdir(parents=True)
    (project / "results").mkdir()
    candidate_parent = Path("/tmp") / (
        "a416-v2-role5-review." + os.urandom(16).hex()
    )
    candidate_parent.mkdir(mode=0o700)
    candidate = candidate_parent / R.ROLE5_CANDIDATE_LEAF
    candidate_raw = write_raw(
        candidate, R.canonical_json_bytes(payload), mode=0o600
    )
    try:
        receipt = R.verify_v2_role5_candidate(project, candidate)
        assert tuple(receipt) == R.ROLE5_VERIFY_RECEIPT_ORDER
        assert receipt == {
            "verification_status": R.ROLE5_VERIFY_STATUS,
            "authority": R.ROLE5_VERIFY_AUTHORITY,
            "candidate_sha256": digest(candidate_raw),
            "input_map_sha256": digest(R.canonical_json_bytes(records)),
            "size_bytes": len(candidate_raw),
            "promotion_authorized": False,
            "artifacts_written": False,
        }
        assert R.validate_role5_verify_receipt(
            receipt, candidate_raw, records
        ) == receipt
        for key, value in (
            ("candidate_sha256", "0" * 64),
            ("input_map_sha256", "1" * 64),
            ("size_bytes", len(candidate_raw) + 1),
            ("promotion_authorized", 0),
            ("artifacts_written", 0),
        ):
            forged = {**receipt, key: value}
            with pytest.raises((R.ReleaseError, R.StrictJSONError)):
                R.validate_role5_verify_receipt(
                    forged, candidate_raw, records
                )

        # CLI is an exact-XOR mode, fixes the authority root to role24 ROOT,
        # and emits only the exact CJ_COMPACT_V1 receipt plus its sole LF.
        calls: list[tuple[Path | str, Path | str]] = []
        with monkeypatch.context() as cli_patch:
            cli_patch.setattr(
                R,
                "verify_v2_role5_candidate",
                lambda root, path: calls.append((root, path)) or receipt,
            )
            assert R.main(["--verify-role5-candidate", str(candidate)]) == 0
            output = capsys.readouterr()
            assert output.out.encode() == R.canonical_json_bytes(receipt)
            assert output.err == ""
            assert calls == [(R.ROOT, str(candidate))]
            with pytest.raises(SystemExit):
                R.parse_args([
                    "--verify-role5-candidate", str(candidate),
                    "--verify-only",
                ])
            capsys.readouterr()
            assert R.main([
                "--verify-role5-candidate", str(candidate),
                "--expected-candidate-sha256", digest(candidate_raw),
            ]) == 1
            output = capsys.readouterr()
            assert output.out == "" and "forbidden" in output.err
    finally:
        shutil.rmtree(candidate_parent)

    @contextmanager
    def role5_candidate(
        raw: bytes = candidate_raw,
        *,
        mode: int = 0o600,
        parent_stem: str = "a416-v2-role5-review.",
        leaf: str = R.ROLE5_CANDIDATE_LEAF,
        fifo: bool = False,
    ) -> Iterator[Path]:
        parent_path = Path("/tmp") / (parent_stem + os.urandom(16).hex())
        parent_path.mkdir(mode=0o700)
        path = parent_path / leaf
        if fifo:
            os.mkfifo(path, mode)
        else:
            write_raw(path, raw, mode=mode)
        try:
            yield path
        finally:
            shutil.rmtree(parent_path)

    # The verifier itself cannot obtain a writable descriptor or call a
    # write primitive.  This guards the implementation, not merely the final
    # absence of a canonical artifact.
    with role5_candidate() as guarded_candidate:
        original_open = R.os.open

        def read_only_open(path, flags, *args, **kwargs):
            forbidden = (
                os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC
                | getattr(os, "O_APPEND", 0)
            )
            assert flags & forbidden == 0
            return original_open(path, flags, *args, **kwargs)

        with monkeypatch.context() as no_write:
            no_write.setattr(R.os, "open", read_only_open)
            no_write.setattr(
                R.os,
                "write",
                lambda *_args, **_kwargs: (_ for _ in ()).throw(
                    AssertionError("role5 verifier attempted a write")
                ),
            )
            guarded_receipt = R.verify_v2_role5_candidate(
                project, guarded_candidate
            )
        assert guarded_receipt["artifacts_written"] is False

    # Lexical path, parent, inode kind/mode/link/cap, and singleton namespace
    # attacks all fail before any semantic PASS can be emitted.
    with role5_candidate() as path_candidate:
        with pytest.raises(R.PathContractError, match="lexical absolute"):
            R.verify_v2_role5_candidate(
                project, str(path_candidate).replace("/tmp/", "//tmp/", 1)
            )
    with role5_candidate(
        parent_stem="a416-v2-role5-review-WRONG."
    ) as bad_parent:
        with pytest.raises(R.PathContractError, match="exact /tmp"):
            R.verify_v2_role5_candidate(project, bad_parent)
    with role5_candidate(leaf="alias.json") as bad_leaf:
        with pytest.raises(R.PathContractError, match="exact /tmp"):
            R.verify_v2_role5_candidate(project, bad_leaf)
    with role5_candidate(mode=0o644) as public_candidate:
        with pytest.raises(R.PathContractError, match="regular 0600"):
            R.verify_v2_role5_candidate(project, public_candidate)
    with role5_candidate(fifo=True) as fifo_candidate:
        with pytest.raises(R.PathContractError, match="regular 0600"):
            R.verify_v2_role5_candidate(project, fifo_candidate)
    with role5_candidate(b"x" * (R.ROLE5_CANDIDATE_MAX_BYTES + 1)) as oversized:
        with pytest.raises(R.PathContractError, match=r"1\.\.1048576"):
            R.verify_v2_role5_candidate(project, oversized)
    with role5_candidate() as linked_candidate:
        outside_link = Path("/tmp") / (
            "a416-v2-role5-hardlink." + os.urandom(8).hex()
        )
        os.link(linked_candidate, outside_link)
        try:
            with pytest.raises(R.PathContractError, match="regular 0600"):
                R.verify_v2_role5_candidate(project, linked_candidate)
        finally:
            outside_link.unlink()
    with role5_candidate() as sibling_candidate:
        write_raw(sibling_candidate.parent / "foreign", b"foreign\n")
        with pytest.raises(R.PathContractError, match="singleton"):
            R.verify_v2_role5_candidate(project, sibling_candidate)

    # A same-byte inode replacement after semantic validation is still a new
    # generation and is caught by the pinned descriptor/lexical replay.
    with role5_candidate() as swap_candidate:
        def swap_candidate_inode(boundary: str) -> None:
            assert boundary == "BEFORE_TERMINAL_REPLAY"
            replacement = swap_candidate.parent / "replacement"
            write_raw(replacement, candidate_raw, mode=0o600)
            os.replace(replacement, swap_candidate)

        with monkeypatch.context() as swap_patch:
            swap_patch.setattr(R, "_role5_verify_fault_hook", swap_candidate_inode)
            with pytest.raises(R.PathContractError, match="generation changed"):
                R.verify_v2_role5_candidate(project, swap_candidate)

    noncanonical = R.pretty_json_bytes(payload)
    with role5_candidate(noncanonical) as pretty_candidate:
        with pytest.raises(R.StrictJSONError, match="not compact canonical"):
            R.verify_v2_role5_candidate(project, pretty_candidate)
    stale_payload = copy.deepcopy(payload)
    stale_payload["reviewed_v2_inputs"][0]["sha256"] = "f" * 64
    with role5_candidate(R.canonical_json_bytes(stale_payload)) as stale_candidate:
        with pytest.raises(R.ReleaseError, match="reviewed live byte map"):
            R.verify_v2_role5_candidate(project, stale_candidate)
    wrong_commit_payload = copy.deepcopy(payload)
    wrong_commit_payload["review"]["reviewed_commit"] = parent
    with role5_candidate(
        R.canonical_json_bytes(wrong_commit_payload)
    ) as wrong_commit_candidate:
        with pytest.raises(R.ReleaseError):
            R.verify_v2_role5_candidate(project, wrong_commit_candidate)

    # Live reviewed bytes, immutable legacy bytes, local refs, fetched remote
    # evidence, and the clean index tree are each independently terminal.
    reviewed_live = project / records[0]["path"]
    reviewed_original = reviewed_live.read_bytes()
    write_raw(reviewed_live, reviewed_original + b"drift", mode=0o755)
    try:
        with role5_candidate() as source_drift_candidate:
            with pytest.raises(R.ReleaseError):
                R.verify_v2_role5_candidate(project, source_drift_candidate)
    finally:
        write_raw(reviewed_live, reviewed_original, mode=0o755)

    legacy_live = project / synthetic_legacy[0]["path"]
    legacy_original = legacy_live.read_bytes()
    write_raw(legacy_live, legacy_original + b"drift")
    try:
        with role5_candidate() as legacy_drift_candidate:
            with pytest.raises(R.ReleaseError, match="legacy"):
                R.verify_v2_role5_candidate(project, legacy_drift_candidate)
    finally:
        write_raw(legacy_live, legacy_original)

    ref_attacks = (
        (project / ".git/refs/heads/main", f"{parent}\n".encode()),
        (project / ".git/refs/remotes/origin/main", f"{parent}\n".encode()),
        (
            project / ".git/FETCH_HEAD",
            f"{parent}\t\tbranch 'main' of synthetic.invalid\n".encode(),
        ),
    )
    for attacked_path, forged_raw in ref_attacks:
        original = attacked_path.read_bytes()
        write_raw(attacked_path, forged_raw)
        try:
            with role5_candidate() as ref_drift_candidate:
                with pytest.raises(R.ReleaseError):
                    R.verify_v2_role5_candidate(project, ref_drift_candidate)
        finally:
            write_raw(attacked_path, original)

    corrupt_index = bytearray(index_image)
    corrupt_index[-1] ^= 1
    write_raw(project / ".git/index", bytes(corrupt_index))
    try:
        with role5_candidate() as index_drift_candidate:
            with pytest.raises(R.ReleaseError, match="index"):
                R.verify_v2_role5_candidate(project, index_drift_candidate)
    finally:
        write_raw(project / ".git/index", index_image)

    assert (project / ".git/index").read_bytes() == index_image
    assert (project / ".git/FETCH_HEAD").read_bytes() == fetch_head
    assert not (project / R.ROLE5_CANONICAL_RELATIVE).exists()


def test_full_live_machine_validator_and_coherent_mutations(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # The immutable attempt-1 role10 has the same closed full machine schema.
    # Rebinding only its capture-tool path lets this V2-independent verifier
    # exercise every live Python/Arb, CAPD, compiler, runtime and resource row.
    old_capture = "scripts/run_r401_val_l3_a1_all_slabs.py"
    monkeypatch.setattr(R, "FORMAL_MACHINE_CAPTURE_TOOL", old_capture)
    payload = json.loads(
        (R.ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json")
        .read_text(encoding="utf-8")
    )
    role_paths = {
        "scheduler": old_capture,
        "static_evaluator": R.FORMAL_MACHINE_STATIC_EVALUATOR,
        "branch_evaluator_source": R.FORMAL_MACHINE_BRANCH_SOURCE,
        "branch_evaluator_binary": R.FORMAL_MACHINE_BRANCH_BINARY,
        "l1_final_plan": "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    }
    roles = {
        role: R._role_binding(R.ROOT, role, relative)
        for role, relative in role_paths.items()
    }
    with R.capture_input_generation():
        R.validate_formal_machine_freeze(R.ROOT, payload, roles)

    float_alias = copy.deepcopy(payload)
    float_alias["machine_requirements"]["static_workers"] = 8.0
    with R.capture_input_generation():
        with pytest.raises(R.ReleaseError, match="requirements"):
            R.validate_formal_machine_freeze(R.ROOT, float_alias, roles)

    coherent_payload_drift = copy.deepcopy(payload)
    coherent_payload_drift["resource_evidence"]["static_payload_raw_utf8"] += "\n"
    coherent_payload_drift["resource_evidence"]["static_payload_sha256"] = digest(
        coherent_payload_drift["resource_evidence"]["static_payload_raw_utf8"].encode()
    )
    with R.capture_input_generation():
        with pytest.raises(R.ReleaseError):
            R.validate_formal_machine_freeze(
                R.ROOT, coherent_payload_drift, roles
            )


def test_s0_exact18_replays_four_sources_and_nine_controls(tmp_path: Path) -> None:
    project = (tmp_path / "s0-project").resolve()
    project.mkdir()
    roles: dict[str, dict[str, Any]] = {}
    input_paths = dict(R.INPUT_ROLES)
    for role in (
        "s0_adapter", "prefreeze_design", "checker_contract", "release_contract"
    ):
        raw = write_raw(project / input_paths[role], f"source:{role}\n".encode())
        roles[role] = {"role": role, "path": input_paths[role], "sha256": digest(raw)}

    proofs = []
    for bits in (128, 256):
        for slab in ("S000", "S025", "S050"):
            proofs.append(
                {
                    "internal_count": 1,
                    "node_count": 2,
                    "path": f"proof_{bits}_{slab}.json",
                    "precision_bits": bits,
                    "sha256": "2" * 64,
                    "size_bytes": 1,
                    "slab_id": slab,
                    "terminal_count": 1,
                    "tree_content_sha256": {
                        name: "3" * 64
                        for name in (
                            "ANGLE", "SECTION_HIGH", "SECTION_LOW", "SECTION_WINDOW"
                        )
                    },
                    "unresolved_count": 0,
                }
            )
    branch_files = {
        f"{project}/sealed/branch/{index:02d}.json": "4" * 64
        for index in range(26)
    }
    composite_files = [
        {"scope": "ROOT", "path": "sealed/composite/root.json"},
        {"scope": "OUTPUT", "path": "sealed/composite/output.json"},
    ]
    component_files = [
        {"component": "static", "path": "sealed/static.json"},
        {"component": "branch", "path": "sealed/branch.json"},
    ]
    controls = {
        "static_summary": {
            "totals": {
                "node_count": 84172,
                "internal_count": 42074,
                "terminal_count": 42098,
                "unresolved_count": 0,
            },
            "proofs": proofs,
        },
        "static_manifest": {"synthetic": True},
        "static_checker": {"independent_interval_checks": 122300},
        "branch_summary": {"synthetic": True},
        "branch_manifest": {"files": branch_files},
        "branch_checker": {"raw_replay_count": 6, "manifest_file_count": 26},
        "composite_summary": {"synthetic": True},
        "composite_manifest": {
            "files": composite_files,
            "component_files": component_files,
        },
        "composite_checker": {
            "cell_replay_count": 6,
            "manifest_binding_count": 18,
            "failures": [],
        },
    }
    for name, role in R.S0_CONTROL_ROLE_MAP.items():
        raw = write_compact(project / input_paths[role], controls[name])
        roles[role] = {"role": role, "path": input_paths[role], "sha256": digest(raw)}
    control_hashes = {
        name: roles[role]["sha256"] for name, role in R.S0_CONTROL_ROLE_MAP.items()
    }
    source_bindings = {
        roles[role]["path"]: roles[role]["sha256"]
        for role in (
            "s0_adapter", "prefreeze_design", "checker_contract", "release_contract"
        )
    }
    payload = {
        "schema_version": 1,
        "protocol_id": "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY",
        "artifact_role": "S0_TO_A1_COMPATIBILITY_REPLAY",
        "artifact_status": "NON_LICENSING",
        "replay_status": "PASS_S0_COMPATIBILITY_REPLAY",
        "matrix": {
            "precisions": [128, 256],
            "slabs": ["S000", "S025", "S050"],
            "cell_count": 6,
        },
        "static_facts": R.S0_STATIC_FACTS,
        "branch_facts": R.S0_BRANCH_FACTS,
        "composite_facts": R.S0_COMPOSITE_FACTS,
        "control_hashes": control_hashes,
        "role_sets": {
            "static_proof_entries": proofs,
            "branch_manifest_roles": [
                absolute.removeprefix(f"{project}/") for absolute in sorted(branch_files)
            ],
            "composite_manifest_roles": composite_files,
            "composite_component_roles": component_files,
        },
        "source_protocols": R.S0_SOURCE_PROTOCOLS,
        "source_bindings": source_bindings,
        "failures": [],
        "claim_boundary": R.S0_COMPATIBILITY_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    roles["s0_compatibility"] = {
        "role": "s0_compatibility",
        "path": input_paths["s0_compatibility"],
        "sha256": "5" * 64,
    }
    with R.capture_input_generation():
        replay = R._validate_s0_payload(project, payload, roles)
    assert replay["control_hashes"] == control_hashes
    forged = copy.deepcopy(payload)
    forged["source_bindings"][next(iter(source_bindings))] = "f" * 64
    with R.capture_input_generation():
        with pytest.raises(R.ReleaseError, match="identity/facts/bindings"):
            R._validate_s0_payload(project, forged, roles)
    legacy17 = dict(payload)
    legacy17.pop("source_bindings")
    with pytest.raises(R.ReleaseError, match="key set"):
        R._validate_s0_payload(project, legacy17, roles)
