#!/usr/bin/env python3
"""Hostile source, transaction, and release-scaffold tests for HCS-C61."""

from __future__ import annotations

import ast
import hashlib
import io
import json
from contextlib import redirect_stderr, redirect_stdout
import inspect
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import c61_atomic_promote as atomic
import c61_checker as checker
import c61_checker_resolvent as checker_resolver
import c61_group as producer_group
from c61_exact import (
    StrictDataError,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deep_exact,
    strict_json_loads,
)
import c61_hash_manifest as manifest
import c61_pipeline as pipeline
import c61_producer as producer
import c61_resolvent as producer_resolver


CODE = Path(__file__).resolve().parent
RESULTS = CODE.parent / "results"
TEST_EVIDENCE_ENV = "C61_TEST_EVIDENCE_DIR"
EVIDENCE_NAMES = (
    "c61_group_evidence.json",
    "c61_resolvent_evidence.json",
)
STAGE_NAME_PATTERN = re.compile(r"^\.c61-stage-[A-Za-z0-9]{8}$")

# Deliberate implementation locks.  The independently frozen component layer,
# owner-declared SOURCE_STABLE producer/checker pair, shared payload contract,
# and actual runtime-report contract are all bound below.  The full suite and
# runner fail closed on any absent latch or exact source/evidence/count drift.
FROZEN_SUPPORT_SOURCE_HASHES: dict[str, str] | None = {
    "c61_group.py": (
        "64dfabdec2cf5767e4022c21a0ad7385efaa191df209c739ab7e015c46a83b5f"
    ),
    "c61_checker_group.g": (
        "4fc377dc16f5b4ebec68767709d1e3e5e2a137b6694567f0b42cb9d88406862e"
    ),
    "c61_resolvent.py": (
        "1c6e18ba4533908ef327cbc574e9d3b8268d1d0f2c9adf6ab2a9d6e86ae40c20"
    ),
    "c61_checker_resolvent.py": (
        "f247dfdf393499c6a41df3dfa34815c1f4557781ec604639da47b921e90c9f6a"
    ),
}
FROZEN_EVIDENCE_HASHES: dict[str, str] | None = {
    "c61_group_evidence.json": (
        "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9"
    ),
    "c61_resolvent_evidence.json": (
        "1be0f9ac4e05ee7a747d39c546502d59dc29bb1407932e14875b61a3b82afe0f"
    ),
}
FROZEN_COMPONENT_API = {
    "group_producer": ("build_document", "validate_fast"),
    "resolver_producer": (
        "build_resolver_candidate",
        "validate_evidence_document",
    ),
    "resolver_checker": (
        "attest_candidate_document",
        "validate_full_document",
    ),
}
# These adjudication seals are non-runtime integration facts.  They never
# authorize reading chronology-only audit files from production code.
FROZEN_COMPONENT_ADJUDICATION = {
    "group": {
        "status": "GROUP_HOSTILE_PASS",
        "independent_report_sha256": (
            "1da91e7e82ff92888110b07155367410b0275b4c69887da19a6bced91a822d92"
        ),
        "component_report_sha256": (
            "3f14b2d42499e62a55a894206747c2b1f91d049ba971d952bf7c47f41c155f73"
        ),
        "exact4_manifest_sha256": (
            "f6fccf6aa815476a29193a5764ba4cac3916851ff68dbd9788620b6751b87208"
        ),
        "artifact_count": 4,
        "total_bytes": 1_283_518,
        "producer_size_bytes": 100_679,
        "checker_size_bytes": 13_364,
        "evidence_size_bytes": 1_165_113,
        "component_report_size_bytes": 4_362,
        "python_projection_sha256": (
            "34ab65dadc1a2fe2b697d290f473b8fbb349b46b6772401eaef21ab8d9d0e970"
        ),
        "gap_projection_sha256": (
            "ebd3c174ecc76cb26792dfd24e547a59148f1d13e7a59d4f74a53f8bfb8c860b"
        ),
        "handoff_sha256": (
            "5e2770daa75c4246b93d175a97ddf2ed28897124e136a5d40ef50e06159841cc"
        ),
    },
    "resolver": {
        "status": "RESOLVER_HOSTILE_PASS",
        "independent_report_sha256": (
            "745487a4a2e689d415ba4778d20f8331b4561004102e928712f77952a747d9a8"
        ),
        "independent_report_payload_sha256": (
            "c8e33d9c476270c8f537d60b76b0b8e20032e9a27923d5096875b8cd1af02731"
        ),
        "exact3_ledger_sha256": (
            "b43f6902f7fec40d5d595ccab423f9d8260da2ade1824dc3d12ba006fd4bf74c"
        ),
        "artifact_count": 3,
        "total_bytes": 750_694,
        "producer_size_bytes": 91_639,
        "checker_size_bytes": 64_892,
        "evidence_size_bytes": 594_163,
        "evidence_payload_sha256": (
            "956f99f419e08f78d7b8c3304e840a90ca50ac7271635b5e46d9ba5c9c391918"
        ),
        "schema_sha256": (
            "9925f23879bef26b6f5805ae2f0affe37785d5e569c929c706afaf80abdecf1d"
        ),
    },
}
# Owner-frozen pre-source-stability fixture seal.  The wrapper is deliberately
# absent from the promoted project and is never runtime authority; these facts
# record only the independently fixed payload shape/count split for the later
# shared-fixture adapter.
FROZEN_OWNER_WRAPPER_V2_ADJUDICATION = {
    "fixture_status": (
        "NONAUTHORITY_STRUCTURE_SNAPSHOT_ONLY_NOT_THEOREM_OR_RELEASE_AUTHORITY"
    ),
    "wrapper_sha256": (
        "44d4289e7a7afafefee698a3b4ad579ff797985d753c0328b3d70e3a2586418d"
    ),
    "wrapper_size_bytes": 580_695,
    "nested14_sha256": (
        "22fec12f9280b717e1db98029acba790cce4785df38c80cb9a26f90b60cf688f"
    ),
    "candidate_schema_sha256": (
        "729b65e2a3b4ab9b3aae3930908aac94e5f9aefeee93b8032d6bf9b50067515e"
    ),
    "G0_sha256": (
        "41712f83134e5b3843ff14113cdee3928b134496be393d519f9b8167c34a8b54"
    ),
    "payload_scalar_leaf_count": 19_078,
    "schema_scalar_leaf_count": 29,
    "value_mutation_count_expected": 19_109,
    "type_mutation_count_expected": 19_109,
    "structural_mutation_count_expected": 14,
    "evidence_rebound_mutation_count_expected": 10,
    "group_evidence_mutation_count": 6,
    "resolver_evidence_mutation_count": 4,
    "artifact_mutation_count": 2,
    "total_evidence_and_artifact_mutation_count": 12,
}
FROZEN_OWNER_SCHEMA_CONTRACT = {
    "schema_id": "hcs-c61-certificate-schema-v1",
    "payload_top_level_keys": (
        "artifact_contract",
        "G0_released_authority_conventions_object",
        "G1_three_tensor_products_burnside",
        "G2_mixed_160_12_8_field_dictionary",
        "G3_product_form_resolvents_primitivity",
        "G4_fourier_kummer_type3_diamond",
        "G5_complete_global_arithmetic",
        "G6_both_local_branches_ideal_laws",
        "G7_independence_sources_scope_release",
        "written_bridges",
        "backend_contract",
        "source_contract",
        "scope_nonclaims",
        "nonresults",
        "status",
    ),
    "payload_top_level_key_count": 15,
    "strict_json": True,
    "duplicate_keys_rejected": True,
    "floats_rejected": True,
    "booleans_rejected_in_integer_slots": True,
    "unknown_or_missing_fields_rejected": True,
    "scope_false_leaf_count": 30,
    "semantic_gate_count": 8,
    "written_bridge_count": 7,
    "component_artifact_count": 2,
    "source_entry_count": 13,
    "result_entry_count": 8,
    "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
    "canonical_leaf_sha256": (
        "729b65e2a3b4ab9b3aae3930908aac94e5f9aefeee93b8032d6bf9b50067515e"
    ),
    "canonical_leaf_size_bytes": 875,
    "pretty_document_sha256": (
        "a446d693742a327dd0b1edd3ad5da97a50dc76cc0f1f7e171096df341ad10e76"
    ),
    "pretty_document_size_bytes": 1_015,
}
FROZEN_OWNER_HOSTILE_FAMILY_SPLIT = {
    "group_evidence": (
        "group_schema_status_firewall",
        "group_source_authority_rebind",
        "group_tensor_row_semantics",
        "group_mixed_160_12_8_atlas",
        "group_raw_global_local_inputs",
        "group_scope_false_leaf",
    ),
    "resolver_evidence": (
        "resolver_schema_payload",
        "resolver_marker_fourier_carrier",
        "resolver_type3_Tplus_diamond",
        "resolver_global_local_ideal_law",
    ),
    "artifact_contract": (
        "group_artifact_contract",
        "resolver_artifact_contract",
    ),
}
MAIN_SOURCE_LATCH_STATUS = "SOURCE_STABLE"
FROZEN_MACHINE_SOURCE_HASHES: dict[str, str] | None = {
    "c61_producer.py": (
        "dadf8899f2fe82b65131a43ffbe438602db79a12654489b34d35ae8a6ee83d99"
    ),
    "c61_checker.py": (
        "571de05ce06cf98c1acb6809800cf5f212755ce91c5d2f8eb5733eb1aa708887"
    ),
}
FROZEN_PAYLOAD_KEYS: tuple[str, ...] | None = (
    "artifact_contract",
    "G0_released_authority_conventions_object",
    "G1_three_tensor_products_burnside",
    "G2_mixed_160_12_8_field_dictionary",
    "G3_product_form_resolvents_primitivity",
    "G4_fourier_kummer_type3_diamond",
    "G5_complete_global_arithmetic",
    "G6_both_local_branches_ideal_laws",
    "G7_independence_sources_scope_release",
    "written_bridges",
    "backend_contract",
    "source_contract",
    "scope_nonclaims",
    "nonresults",
    "status",
)
FROZEN_G7_COUNTS: dict[str, int] | None = {
    "payload_scalar_leaf_count": 19_078,
    "schema_scalar_leaf_count": 29,
    "value_mutation_count_expected": 19_109,
    "type_mutation_count_expected": 19_109,
    "structural_mutation_count_expected": 14,
    "group_evidence_mutation_count": 6,
    "resolver_evidence_mutation_count": 4,
    "evidence_rebound_mutation_count_expected": 10,
    "artifact_mutation_count": 2,
    "total_evidence_and_artifact_mutation_count": 12,
}
FROZEN_ACTUAL_DEEP_HOSTILE_CASE_COUNT: int | None = 12
FORBIDDEN_EXTERNAL_CHRONOLOGY_SOURCE_TOKENS = (
    b"/tmp",
    b"c61_adaptive_scan_candidate.md",
    b"c61_novelty_source_audit.md",
    b"c61_arithmetic_design.md",
    b"c61_formal_stage_hostile.md",
    b"c61_formal_stage_hostile_audit.py",
    b"eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026",
    b"d8fb7baa602cf32c89e2b457f9f0abf5f52c70ff377c8b23aae0e48ab921be25",
    b"50e37f98be54a8eac7de4ce783f83b7d8bcb42c7668abd4cdab0bb1cc3ac97f9",
    b"78899bcda2ac3c5763b7622eed6340a57e23c248506d58d406f93f4debec01f7",
)

TARGET_LOCK_HASHES = {
    "formal_root13_aggregate_sha256": "c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28",
    "route_sha256": "c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b",
    "batch_sha256": "13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814",
    "formal_exact15_ledger_sha256": "61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5",
    "target_report_sha256": "eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026",
    "novelty_source_audit_sha256": "d8fb7baa602cf32c89e2b457f9f0abf5f52c70ff377c8b23aae0e48ab921be25",
    "formal_hostile_report_sha256": "78899bcda2ac3c5763b7622eed6340a57e23c248506d58d406f93f4debec01f7",
    "protected_guard_sha256": "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead",
}
P60_RELEASE = {
    "commit": "fe1217810b72840619efdf40a2af31b8b80d96f6",
    "parent": "f3b3726c40519cdd8ac7832f9f22df16d451b890",
    "tree": "22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a",
}
P60_RELEASED_BATCH = {
    "sha256": "d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5",
    "size_bytes": 34_176,
}
RELEASED_C60_HASHES = {
    "FULL_PROJECT_HASHES.sha256": "37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4",
    "route_a_evaluation.yaml": "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872",
    "results/c60_certificate.json": "d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518",
    "results/c60_group_evidence.json": "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2",
    "results/c60_resolvent_evidence.json": "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da",
    "results/c60_schema.json": "c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5",
    "results/c60_check_report.json": "25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44",
    "results/scoped_hash_manifest.json": "f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7",
}
C60_CERTIFICATE_PAYLOAD_SHA256 = (
    "dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead"
)
RELEASED_C60_ARCHIVE_ROUTE = (
    "evaluations/route_a/HCS-C60/20260817T000000Z.yaml",
    "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872",
)
PRE_I61_DIRTY_STATUS = {
    "henon_dynamics/BATCH_PLAN_C57_C61.md": " M",
    "henon_dynamics/codex_prompt.md": "??",
    **{
        "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent/" + name: "??"
        for name in (
            "DERIVATION.md",
            "EXPERIMENT_PLAN.md",
            "EXPERIMENT_TRACKER.md",
            "IMPLEMENTATION_CHECKLIST.md",
            "INTEGRITY_REPORT.md",
            "METHODOLOGY_BLUEPRINT.md",
            "NARRATIVE_REPORT.md",
            "PAPER_PLAN.md",
            "PROOF_PACKAGE.md",
            "README.md",
            "RESEARCH_QUESTION.md",
            "SOURCE_AUDIT.md",
            "THEOREM_PACKAGE.md",
            "route_a_evaluation.yaml",
        )
    },
}
RELEASE_SOURCES_FROZEN = (
    FROZEN_SUPPORT_SOURCE_HASHES is not None
    and FROZEN_MACHINE_SOURCE_HASHES is not None
)
MACHINE_CONTRACT_FROZEN = (
    RELEASE_SOURCES_FROZEN
    and FROZEN_EVIDENCE_HASHES is not None
    and FROZEN_PAYLOAD_KEYS is not None
    and FROZEN_G7_COUNTS is not None
    and FROZEN_ACTUAL_DEEP_HOSTILE_CASE_COUNT is not None
)


def _audit_exact_pre_i61_dirty_set(repository: Path) -> dict[str, str]:
    """One-time stage audit; never a generic later-worktree allowance."""

    completed = subprocess.run(
        [
            "/usr/bin/git",
            "-C",
            str(repository),
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        env={"PATH": "/usr/bin:/bin", "LC_ALL": "C"},
        cwd="/",
        timeout=60,
    )
    if completed.stderr:
        raise StrictDataError("pre-I61 porcelain audit emitted stderr")
    observed: dict[str, str] = {}
    for entry in completed.stdout.split(b"\0"):
        if not entry:
            continue
        if len(entry) < 4 or entry[2:3] != b" ":
            raise StrictDataError("pre-I61 porcelain entry is malformed")
        status_text = entry[:2].decode("ascii", errors="strict")
        path_text = entry[3:].decode("utf-8", errors="strict")
        if path_text in observed:
            raise StrictDataError("pre-I61 porcelain path is duplicated")
        observed[path_text] = status_text
    if observed != PRE_I61_DIRTY_STATUS:
        raise StrictDataError(
            "pre-I61 worktree differs from exact target-lock delta plus guard"
        )
    return observed


SCOPE_NONCLAIM_KEYS = (
    "target_selection_pilot_is_theorem_authority",
    "raw_tom_defines_fields",
    "finite_g_sets_isomorphic_from_character_relation",
    "formal_invariant_statement_after_root_relations",
    "expanded_characteristic_zero_resolvent_claimed",
    "characteristic_zero_coefficient_hash_claimed",
    "integral_basis_claimed",
    "maximal_order_claimed",
    "monogenicity_claimed",
    "class_number_claimed",
    "regulator_claimed",
    "trace_form_claimed",
    "d3_branch_selected",
    "local_fields_classified_by_nefd_rows",
    "decomposition_frobenius_claimed",
    "bad_artin_euler_claimed",
    "local_epsilon_factor_claimed",
    "local_root_number_claimed",
    "global_root_number_claimed",
    "artin_holomorphy_claimed",
    "automorphy_claimed",
    "rational_point_claimed",
    "hasse_principle_claimed",
    "weak_approximation_claimed",
    "brauer_manin_claimed",
    "motive_claimed",
    "rh_claimed",
    "hilbert_polya_operator_claimed",
    "paper_complete_claimed",
    "release_claimed",
)

def _fixture_evidence_paths() -> tuple[Path, Path]:
    """Bind the shared fixture to live evidence or the runner's active stage."""

    results = RESULTS.absolute()
    if (
        results.is_symlink()
        or not results.is_dir()
        or results.resolve(strict=True) != results
    ):
        raise StrictDataError("fixture results authority must be one real directory")
    selected = os.environ.get(TEST_EVIDENCE_ENV)
    directory = results
    if selected is not None:
        candidate = Path(selected)
        if (
            not candidate.is_absolute()
            or not STAGE_NAME_PATTERN.fullmatch(candidate.name)
            or candidate.parent != results
            or candidate.is_symlink()
            or not candidate.is_dir()
            or candidate.resolve(strict=True) != candidate
        ):
            raise StrictDataError(
                "test evidence override must be one canonical real direct "
                "PROJECT/results/.c61-stage-[A-Za-z0-9]{8} directory"
            )
        if {entry.name for entry in candidate.iterdir()} != set(EVIDENCE_NAMES):
            raise StrictDataError(
                "test evidence stage must contain exactly the two fixed evidence files"
            )
        directory = candidate

    paths = tuple(directory / name for name in EVIDENCE_NAMES)
    directory_before = directory.stat()
    identities: list[tuple[int, int, int, int, int, int, int]] = []
    for path in paths:
        metadata = path.lstat()
        if (
            path.is_symlink()
            or not stat.S_ISREG(metadata.st_mode)
            or metadata.st_nlink != 1
        ):
            raise StrictDataError(
                "fixture evidence must be fixed regular non-symlink link-count-one files"
            )
        identities.append(
            (
                metadata.st_dev,
                metadata.st_ino,
                metadata.st_mode,
                metadata.st_nlink,
                metadata.st_size,
                metadata.st_mtime_ns,
                metadata.st_ctime_ns,
            )
        )
    directory_after = directory.stat()
    if (
        not stat.S_ISDIR(directory_after.st_mode)
        or (directory_before.st_dev, directory_before.st_ino)
        != (directory_after.st_dev, directory_after.st_ino)
    ):
        raise StrictDataError("fixture evidence directory changed during binding")
    for path, expected in zip(paths, identities):
        metadata = path.lstat()
        observed = (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_nlink,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )
        if observed != expected:
            raise StrictDataError("fixture evidence changed during binding")
    return paths  # type: ignore[return-value]


def _fixture_evidence_documents() -> tuple[dict[str, object], dict[str, object]]:
    paths = _fixture_evidence_paths()
    directory = paths[0].parent
    directory_before = directory.stat()
    seals: list[tuple[int, int, int, int, int, int, int]] = []
    blobs: list[bytes] = []
    for path in paths:
        before = path.lstat()
        blob = path.read_bytes()
        after = path.lstat()
        before_seal = (
            before.st_dev,
            before.st_ino,
            before.st_mode,
            before.st_nlink,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        after_seal = (
            after.st_dev,
            after.st_ino,
            after.st_mode,
            after.st_nlink,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if before_seal != after_seal or len(blob) != after.st_size:
            raise StrictDataError("fixture evidence changed while being read")
        seals.append(after_seal)
        blobs.append(blob)
    directory_after = directory.stat()
    if (
        (directory_before.st_dev, directory_before.st_ino)
        != (directory_after.st_dev, directory_after.st_ino)
        or _fixture_evidence_paths() != paths
    ):
        raise StrictDataError("fixture evidence directory changed during read")
    for path, expected in zip(paths, seals):
        metadata = path.lstat()
        observed = (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_nlink,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )
        if observed != expected:
            raise StrictDataError("fixture evidence changed after read")
    group = strict_json_loads(blobs[0], max_bytes=2_000_000)
    resolvent = strict_json_loads(blobs[1], max_bytes=5_000_000)
    if type(group) is not dict or type(resolvent) is not dict:
        raise StrictDataError("fixture evidence documents must be objects")
    return group, resolvent


def _fixture_backend_contract() -> dict[str, object]:
    """Return the exact locked backend value without launching a child."""

    math = pipeline.EXPECTED_BACKENDS["math"]
    return {
        "gap": dict(pipeline.EXPECTED_GAP),
        "math_python": {
            "executable_sha256": math["executable_sha256"],
            "executable_size_bytes": math["executable_size_bytes"],
            "resolved_executable": str(
                Path("/root/miniconda3/bin/python3").resolve(strict=True)
            ),
            "versions": {
                "backend": "FLINT_SYMPY_NETWORKX",
                "python": math["python"],
                "flint": math["flint"],
                "sympy": math["sympy"],
                "networkx": math["networkx"],
                "jsonschema": math["jsonschema"],
            },
        },
        "pari_dependency": False,
        "schema_id": "hcs-c61-backend-contract-v1",
        "singular_dependency": False,
        "two_run_deterministic": True,
    }


def _imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    answer: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            answer.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            answer.add(node.module.split(".", 1)[0])
    return answer


def _literal_string_dicts(path: Path) -> list[tuple[int, list[str]]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    answer = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [
            key.value
            for key in node.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)
        ]
        answer.append((node.lineno, keys))
    return answer


def _semantic_diff_count(left: object, right: object) -> int:
    if type(left) is not type(right):
        return 1
    if isinstance(left, dict):
        left_keys = set(left)
        right_keys = set(right)  # type: ignore[arg-type]
        return len(left_keys ^ right_keys) + sum(
            _semantic_diff_count(left[key], right[key])  # type: ignore[index]
            for key in left_keys & right_keys
        )
    if isinstance(left, list):
        right_list = right  # type: ignore[assignment]
        return abs(len(left) - len(right_list)) + sum(
            _semantic_diff_count(a, b) for a, b in zip(left, right_list)
        )
    return 0 if left == right else 1


_ACTUAL_SHARED_FIXTURE_CACHE: dict[str, object] | None = None


def _actual_shared_fixture() -> dict[str, object]:
    """Build one producer/checker-independent payload fixture per test process."""

    global _ACTUAL_SHARED_FIXTURE_CACHE
    if _ACTUAL_SHARED_FIXTURE_CACHE is not None:
        return _ACTUAL_SHARED_FIXTURE_CACHE

    group_path, resolver_path = _fixture_evidence_paths()
    stage = group_path.parent
    math_python = Path("/root/miniconda3/bin/python3")
    gap = Path("/usr/bin/gap")
    produced = producer.assemble_payload(stage, math_python, gap)

    group_raw = group_path.read_bytes()
    resolver_raw = resolver_path.read_bytes()
    group_document = checker.compact_document(
        group_raw,
        max_bytes=checker.MAX_GROUP_EVIDENCE_BYTES,
        label="C61 shared-fixture group evidence",
    )
    resolver_document = checker.compact_document(
        resolver_raw,
        max_bytes=checker.MAX_RESOLVER_EVIDENCE_BYTES,
        label="C61 shared-fixture resolver evidence",
    )

    protected = [
        CODE / name
        for name in sorted(checker.CODE_SOURCE_NAMES)
        if name != "c61_producer.py"
    ]
    protected.extend(checker.c60_manifest_member_paths())
    protected.extend((group_path, resolver_path))
    protected.extend(
        checker.PROJECT / name for name in sorted(checker.FORMAL_MARKDOWN_NAMES)
    )
    protected.extend(
        (
            checker.PROJECT / "route_a_evaluation.yaml",
            checker.BATCH,
            checker.GUARD,
            math_python.resolve(strict=True),
            gap.resolve(strict=True),
            Path("/usr/bin/git").resolve(strict=True),
        )
    )
    git_dir = checker.REPO_ROOT / ".git"
    for relative in ("HEAD", "index", "packed-refs", "refs/heads/main"):
        candidate = git_dir / relative
        if candidate.is_file() and not candidate.is_symlink():
            protected.append(candidate)
    guard = checker.SnapshotGuard(
        protected,
        directories=(CODE, stage),
        opaque_paths=(CODE / "c61_producer.py",),
    )

    source_contract_value = checker.exact_source_contract()
    produced_source_contract = producer.source_contract()
    if not deep_exact(source_contract_value, produced_source_contract):
        raise StrictDataError("C61 shared-fixture source-contract delta")
    g0 = checker.rebuild_g0(guard)
    produced_g0, written = producer.rebuild_g0()
    if not deep_exact(g0, produced_g0):
        raise StrictDataError("C61 shared-fixture G0 delta")
    if written != {key: True for key in producer.WRITTEN_BRIDGE_KEYS}:
        raise StrictDataError("C61 shared-fixture written-bridge delta")
    artifacts = checker.artifact_contract(
        group_path,
        group_raw,
        group_document,
        resolver_path,
        resolver_raw,
        resolver_document,
    )
    produced_artifacts, _, _ = producer.artifact_contract(
        stage, validate_documents=False
    )
    if not deep_exact(artifacts, produced_artifacts):
        raise StrictDataError("C61 shared-fixture artifact-contract delta")
    backends = checker.backend_contract(math_python, gap, guard)
    expected = checker.expected_payload(
        source_contract_value,
        g0,
        artifacts,
        group_document,
        resolver_document,
        backends,
    )
    if not deep_exact(produced, expected):
        raise StrictDataError("C61 shared-fixture full-payload delta")
    produced_schema = producer.schema_descriptor(produced)
    expected_schema = checker.schema_descriptor(expected)
    if not deep_exact(produced_schema, expected_schema):
        raise StrictDataError("C61 shared-fixture schema delta")
    certificate = {
        "schema": produced_schema,
        "schema_sha256": hashlib.sha256(
            canonical_leaf_bytes(produced_schema)
        ).hexdigest(),
        "payload": produced,
        "payload_sha256": hashlib.sha256(canonical_leaf_bytes(produced)).hexdigest(),
    }
    checker.core_verify(certificate, produced_schema, expected, expected_schema)
    guard.assert_unchanged("after C61 actual shared fixture")
    _ACTUAL_SHARED_FIXTURE_CACHE = {
        "artifact_contract": artifacts,
        "backend_contract": backends,
        "certificate": certificate,
        "expected_payload": expected,
        "expected_schema": expected_schema,
        "group_document": group_document,
        "group_path": group_path,
        "guard": guard,
        "produced_payload": produced,
        "resolver_document": resolver_document,
        "resolver_path": resolver_path,
        "source_contract": source_contract_value,
    }
    return _ACTUAL_SHARED_FIXTURE_CACHE


class StrictDataTests(unittest.TestCase):
    def test_noncanonical_json_and_type_confusion_rejected(self) -> None:
        for raw in (b'{"x":-0}', b'{"x":01}', b'{"x":1.0}', b'{"x":1,"x":2}'):
            with self.subTest(raw=raw), self.assertRaises(StrictDataError):
                strict_json_loads(raw, max_bytes=100)
        self.assertFalse(deep_exact(True, 1))
        self.assertFalse(deep_exact({"x": [1]}, {"x": [True]}))

    def test_hundred_thousand_digit_integer(self) -> None:
        raw = b'{"x":' + b"9" * 100_000 + b"}"
        value = strict_json_loads(raw, max_bytes=len(raw))
        self.assertIs(type(value["x"]), int)


class SourceArchitectureTests(unittest.TestCase):
    def test_frozen_component_contract_and_hostile_adjudications(self) -> None:
        self.assertIsNotNone(FROZEN_SUPPORT_SOURCE_HASHES)
        self.assertIsNotNone(FROZEN_EVIDENCE_HASHES)
        assert FROZEN_SUPPORT_SOURCE_HASHES is not None
        assert FROZEN_EVIDENCE_HASHES is not None
        self.assertEqual(
            set(FROZEN_SUPPORT_SOURCE_HASHES),
            {
                "c61_group.py",
                "c61_checker_group.g",
                "c61_resolvent.py",
                "c61_checker_resolvent.py",
            },
        )
        self.assertEqual(set(FROZEN_EVIDENCE_HASHES), set(EVIDENCE_NAMES))
        for name, expected in FROZEN_SUPPORT_SOURCE_HASHES.items():
            path = CODE / name
            metadata = path.lstat()
            self.assertFalse(path.is_symlink(), name)
            self.assertTrue(stat.S_ISREG(metadata.st_mode), name)
            self.assertEqual(stat.S_IMODE(metadata.st_mode), 0o644, name)
            self.assertEqual(metadata.st_nlink, 1, name)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)
        for name, expected in FROZEN_EVIDENCE_HASHES.items():
            path = RESULTS / name
            metadata = path.lstat()
            self.assertFalse(path.is_symlink(), name)
            self.assertTrue(stat.S_ISREG(metadata.st_mode), name)
            self.assertEqual(stat.S_IMODE(metadata.st_mode), 0o644, name)
            self.assertEqual(metadata.st_nlink, 1, name)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)
        self.assertEqual(
            pipeline.FROZEN_COMPONENT_SOURCE_HASHES,
            FROZEN_SUPPORT_SOURCE_HASHES,
        )
        self.assertEqual(
            pipeline.FROZEN_COMPONENT_EVIDENCE_HASHES,
            FROZEN_EVIDENCE_HASHES,
        )
        observed_components = pipeline.require_frozen_components()
        self.assertEqual(observed_components["sources"], FROZEN_SUPPORT_SOURCE_HASHES)
        self.assertEqual(observed_components["evidence"], FROZEN_EVIDENCE_HASHES)
        modules = {
            "group_producer": producer_group,
            "resolver_producer": producer_resolver,
            "resolver_checker": checker_resolver,
        }
        for owner, names in FROZEN_COMPONENT_API.items():
            for name in names:
                self.assertTrue(callable(getattr(modules[owner], name)), (owner, name))
        self.assertEqual(
            FROZEN_COMPONENT_ADJUDICATION["group"]["status"],
            "GROUP_HOSTILE_PASS",
        )
        self.assertEqual(
            FROZEN_COMPONENT_ADJUDICATION["resolver"]["status"],
            "RESOLVER_HOSTILE_PASS",
        )
        group_contract = FROZEN_COMPONENT_ADJUDICATION["group"]
        resolver_contract = FROZEN_COMPONENT_ADJUDICATION["resolver"]
        self.assertEqual(
            (CODE / "c61_group.py").stat().st_size,
            group_contract["producer_size_bytes"],
        )
        self.assertEqual(
            (CODE / "c61_checker_group.g").stat().st_size,
            group_contract["checker_size_bytes"],
        )
        self.assertEqual(
            (RESULTS / "c61_group_evidence.json").stat().st_size,
            group_contract["evidence_size_bytes"],
        )
        self.assertEqual(
            group_contract["total_bytes"],
            group_contract["producer_size_bytes"]
            + group_contract["checker_size_bytes"]
            + group_contract["evidence_size_bytes"]
            + group_contract["component_report_size_bytes"],
        )
        self.assertEqual(
            (CODE / "c61_resolvent.py").stat().st_size,
            resolver_contract["producer_size_bytes"],
        )
        self.assertEqual(
            (CODE / "c61_checker_resolvent.py").stat().st_size,
            resolver_contract["checker_size_bytes"],
        )
        self.assertEqual(
            (RESULTS / "c61_resolvent_evidence.json").stat().st_size,
            resolver_contract["evidence_size_bytes"],
        )
        self.assertEqual(
            resolver_contract["total_bytes"],
            resolver_contract["producer_size_bytes"]
            + resolver_contract["checker_size_bytes"]
            + resolver_contract["evidence_size_bytes"],
        )
        wrapper = FROZEN_OWNER_WRAPPER_V2_ADJUDICATION
        self.assertEqual(
            wrapper["fixture_status"],
            "NONAUTHORITY_STRUCTURE_SNAPSHOT_ONLY_NOT_THEOREM_OR_RELEASE_AUTHORITY",
        )
        self.assertEqual(
            wrapper["evidence_rebound_mutation_count_expected"],
            wrapper["group_evidence_mutation_count"]
            + wrapper["resolver_evidence_mutation_count"],
        )
        self.assertEqual(
            wrapper["total_evidence_and_artifact_mutation_count"],
            wrapper["evidence_rebound_mutation_count_expected"]
            + wrapper["artifact_mutation_count"],
        )
        hostile_families = FROZEN_OWNER_HOSTILE_FAMILY_SPLIT
        self.assertEqual(
            len(hostile_families["group_evidence"]),
            wrapper["group_evidence_mutation_count"],
        )
        self.assertEqual(
            len(hostile_families["resolver_evidence"]),
            wrapper["resolver_evidence_mutation_count"],
        )
        self.assertEqual(
            len(hostile_families["artifact_contract"]),
            wrapper["artifact_mutation_count"],
        )
        schema = FROZEN_OWNER_SCHEMA_CONTRACT
        schema_keys = tuple(schema)[:15]
        schema_document = {key: schema[key] for key in schema_keys}
        schema_leaf = canonical_leaf_bytes(schema_document)
        schema_pretty = canonical_json_bytes(schema_document, pretty=True)
        self.assertEqual(len(schema_leaf), schema["canonical_leaf_size_bytes"])
        self.assertEqual(
            hashlib.sha256(schema_leaf).hexdigest(),
            schema["canonical_leaf_sha256"],
        )
        self.assertEqual(
            len(schema_pretty), schema["pretty_document_size_bytes"]
        )
        self.assertEqual(
            hashlib.sha256(schema_pretty).hexdigest(),
            schema["pretty_document_sha256"],
        )
        self.assertTrue(schema_pretty.endswith(b"\n"))
        self.assertEqual(
            MAIN_SOURCE_LATCH_STATUS,
            "SOURCE_STABLE",
        )
        self.assertIsNotNone(FROZEN_MACHINE_SOURCE_HASHES)
        self.assertEqual(FROZEN_PAYLOAD_KEYS, schema["payload_top_level_keys"])
        self.assertEqual(
            FROZEN_G7_COUNTS,
            {
                "payload_scalar_leaf_count": 19_078,
                "schema_scalar_leaf_count": 29,
                "value_mutation_count_expected": 19_109,
                "type_mutation_count_expected": 19_109,
                "structural_mutation_count_expected": 14,
                "group_evidence_mutation_count": 6,
                "resolver_evidence_mutation_count": 4,
                "evidence_rebound_mutation_count_expected": 10,
                "artifact_mutation_count": 2,
                "total_evidence_and_artifact_mutation_count": 12,
            },
        )
        self.assertEqual(FROZEN_ACTUAL_DEEP_HOSTILE_CASE_COUNT, 12)

    def test_exact_inventory_and_manifest_contract(self) -> None:
        observed = {path.name for path in CODE.iterdir()}
        self.assertEqual(observed, set(manifest.CODE_NAMES))
        self.assertEqual(len(observed), 13)
        self.assertNotIn("__pycache__", observed)
        manifest._validate_constants()
        self.assertEqual(len(manifest.SCOPED_RELATIVES), 20)
        self.assertEqual(len(manifest.LIVE_RELATIVES), 21)
        self.assertEqual(manifest.PROMOTED_NAMES, atomic.EXPECTED_TARGET_NAMES)
        self.assertEqual(
            manifest.PROMOTED_NAMES,
            (
                "c61_group_evidence.json",
                "c61_resolvent_evidence.json",
                "c61_schema.json",
                "c61_certificate.json",
                "c61_check_report.json",
                "scoped_hash_manifest.json",
            ),
        )
        for name in manifest.CODE_NAMES:
            metadata = (CODE / name).lstat()
            expected_mode = 0o755 if name == "run_all.sh" else 0o644
            self.assertTrue(stat.S_ISREG(metadata.st_mode), name)
            self.assertEqual(stat.S_IMODE(metadata.st_mode), expected_mode, name)
            self.assertEqual(metadata.st_nlink, 1, name)

    def test_release_sources_are_explicitly_frozen(self) -> None:
        self.assertIsNotNone(
            FROZEN_SUPPORT_SOURCE_HASHES,
            "four C61 component-source seals have not yet been installed",
        )
        self.assertIsNotNone(
            FROZEN_MACHINE_SOURCE_HASHES,
            "producer/checker C61 source seals have not yet been installed",
        )
        assert FROZEN_SUPPORT_SOURCE_HASHES is not None
        assert FROZEN_MACHINE_SOURCE_HASHES is not None
        self.assertEqual(
            set(FROZEN_SUPPORT_SOURCE_HASHES),
            {
                "c61_group.py",
                "c61_checker_group.g",
                "c61_resolvent.py",
                "c61_checker_resolvent.py",
            },
        )
        self.assertEqual(
            set(FROZEN_MACHINE_SOURCE_HASHES),
            {"c61_producer.py", "c61_checker.py"},
        )
        for name, expected in {
            **FROZEN_SUPPORT_SOURCE_HASHES,
            **FROZEN_MACHINE_SOURCE_HASHES,
        }.items():
            self.assertEqual(hashlib.sha256((CODE / name).read_bytes()).hexdigest(), expected)

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 sources are not frozen")
    def test_release_sources_do_not_consume_external_chronology(self) -> None:
        """Chronology-only `/tmp` inputs can never become production authority."""

        for name in pipeline.EXPECTED_RELEASE_SOURCE_NAMES:
            raw = (CODE / name).read_bytes()
            for token in FORBIDDEN_EXTERNAL_CHRONOLOGY_SOURCE_TOKENS:
                self.assertNotIn(token, raw, (name, token))

    def test_pipeline_source_latch_matches_current_phase(self) -> None:
        self.assertEqual(
            pipeline.RELEASE_SOURCE_LATCH_STATUS,
            "SOURCE_STABLE",
        )
        self.assertIsNotNone(pipeline.FROZEN_RELEASE_SOURCE_HASHES)
        assert pipeline.FROZEN_RELEASE_SOURCE_HASHES is not None
        self.assertEqual(
            set(pipeline.EXPECTED_RELEASE_SOURCE_NAMES),
            {
                "c61_group.py",
                "c61_checker_group.g",
                "c61_resolvent.py",
                "c61_checker_resolvent.py",
                "c61_producer.py",
                "c61_checker.py",
            },
        )
        self.assertEqual(
            pipeline.FROZEN_RELEASE_SOURCE_HASHES,
            {**FROZEN_SUPPORT_SOURCE_HASHES, **FROZEN_MACHINE_SOURCE_HASHES},
        )
        self.assertEqual(
            pipeline.require_frozen_release_sources(),
            pipeline.FROZEN_RELEASE_SOURCE_HASHES,
        )

    def test_target_lock_and_released_p60_c60_are_bound(self) -> None:
        project = CODE.parent
        dynamics = project.parent
        repository = dynamics.parent
        formal_names = sorted(
            {
                "README.md",
                "RESEARCH_QUESTION.md",
                "METHODOLOGY_BLUEPRINT.md",
                "THEOREM_PACKAGE.md",
                "DERIVATION.md",
                "PROOF_PACKAGE.md",
                "EXPERIMENT_PLAN.md",
                "EXPERIMENT_TRACKER.md",
                "IMPLEMENTATION_CHECKLIST.md",
                "NARRATIVE_REPORT.md",
                "SOURCE_AUDIT.md",
                "INTEGRITY_REPORT.md",
                "PAPER_PLAN.md",
            }
        )
        root_lines = b"".join(
            (
                hashlib.sha256((project / name).read_bytes()).hexdigest()
                + "  "
                + name
                + "\n"
            ).encode("ascii")
            for name in formal_names
        )
        self.assertEqual(
            hashlib.sha256(root_lines).hexdigest(),
            TARGET_LOCK_HASHES["formal_root13_aggregate_sha256"],
        )
        route = project / "route_a_evaluation.yaml"
        batch = dynamics / "BATCH_PLAN_C57_C61.md"
        self.assertEqual(
            hashlib.sha256(route.read_bytes()).hexdigest(),
            TARGET_LOCK_HASHES["route_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(batch.read_bytes()).hexdigest(),
            TARGET_LOCK_HASHES["batch_sha256"],
        )
        exact15 = [batch, *(project / name for name in formal_names), route]
        exact15.sort(key=lambda path: path.relative_to(dynamics).as_posix())
        exact15_lines = b"".join(
            (
                hashlib.sha256(path.read_bytes()).hexdigest()
                + "  "
                + path.relative_to(dynamics).as_posix()
                + "\n"
            ).encode("ascii")
            for path in exact15
        )
        self.assertEqual(len(exact15), 15)
        self.assertEqual(sum(path.stat().st_size for path in exact15), 199_565)
        self.assertEqual(
            sum(path.read_bytes().count(b"\n") for path in exact15), 5_094
        )
        self.assertEqual(
            hashlib.sha256(exact15_lines).hexdigest(),
            TARGET_LOCK_HASHES["formal_exact15_ledger_sha256"],
        )
        route_text = route.read_text(encoding="utf-8")
        for key in (
            "formal_root13_aggregate_sha256",
            "target_report_sha256",
            "novelty_source_audit_sha256",
        ):
            self.assertIn(TARGET_LOCK_HASHES[key], route_text)

        git_values = {}
        for key, revision in (
            ("commit", P60_RELEASE["commit"]),
            ("parent", P60_RELEASE["commit"] + "^"),
            ("tree", P60_RELEASE["commit"] + "^{tree}"),
        ):
            completed = subprocess.run(
                ["/usr/bin/git", "-C", str(repository), "rev-parse", revision],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                env={"PATH": "/usr/bin:/bin", "LC_ALL": "C"},
                cwd="/",
            )
            self.assertFalse(completed.stderr)
            git_values[key] = completed.stdout.decode("ascii").strip()
        self.assertEqual(git_values, P60_RELEASE)

        released_batch = subprocess.run(
            [
                "/usr/bin/git",
                "-C",
                str(repository),
                "show",
                P60_RELEASE["commit"]
                + ":henon_dynamics/BATCH_PLAN_C57_C61.md",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            env={"PATH": "/usr/bin:/bin", "LC_ALL": "C"},
            cwd="/",
            timeout=60,
        )
        self.assertFalse(released_batch.stderr)
        self.assertEqual(len(released_batch.stdout), P60_RELEASED_BATCH["size_bytes"])
        self.assertEqual(
            hashlib.sha256(released_batch.stdout).hexdigest(),
            P60_RELEASED_BATCH["sha256"],
        )
        guard = dynamics / "codex_prompt.md"
        self.assertEqual(
            hashlib.sha256(guard.read_bytes()).hexdigest(),
            TARGET_LOCK_HASHES["protected_guard_sha256"],
        )
        authority_layers = pipeline.require_authority_layers(
            repository=repository, project=project
        )
        self.assertEqual(
            authority_layers["immutable_released_p60"],
            {
                "commit": P60_RELEASE["commit"],
                "tree": P60_RELEASE["tree"],
                "released_batch_sha256": P60_RELEASED_BATCH["sha256"],
                "released_batch_size_bytes": P60_RELEASED_BATCH["size_bytes"],
            },
        )
        self.assertEqual(
            authority_layers["installed_c61_target_lock"]
            ["exact15_ledger_sha256"],
            TARGET_LOCK_HASHES["formal_exact15_ledger_sha256"],
        )

        released_c60 = dynamics / "henon_mu3_yukawa_biquadratic_envelope"
        for relative, expected in RELEASED_C60_HASHES.items():
            self.assertEqual(
                hashlib.sha256((released_c60 / relative).read_bytes()).hexdigest(),
                expected,
                relative,
            )
        released_certificate = strict_json_loads(
            (released_c60 / "results/c60_certificate.json").read_bytes(),
            max_bytes=1_000_000,
        )
        self.assertIs(type(released_certificate), dict)
        self.assertEqual(
            released_certificate.get("payload_sha256"),
            C60_CERTIFICATE_PAYLOAD_SHA256,
        )
        archive_relative, archive_hash = RELEASED_C60_ARCHIVE_ROUTE
        self.assertEqual(
            hashlib.sha256((released_c60 / archive_relative).read_bytes()).hexdigest(),
            archive_hash,
        )

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 sources are not frozen")
    def test_independent_source_contracts_match(self) -> None:
        produced = producer.source_contract()
        independently_rebuilt = checker.exact_source_contract()
        self.assertTrue(
            deep_exact(produced, independently_rebuilt),
            "producer/checker exact13 source contracts differ",
        )
        self.assertEqual(
            set(produced),
            {
                "schema_id", "entry_count", "exact_code_inventory",
                "exact_code_path_allowlist", "entries", "mode_policy",
                "self_reference_policy",
            },
        )
        self.assertEqual(
            produced["mode_policy"],
            "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644",
        )
        self.assertEqual(
            [row["path"] for row in produced["entries"]],
            sorted(row["path"] for row in produced["entries"]),
        )
        for row in produced["entries"]:
            self.assertEqual(set(row), {"path", "sha256", "size_bytes", "mode_octal"})

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 sources are not frozen")
    def test_independent_g0_contracts_match(self) -> None:
        produced = producer.rebuild_g0()[0]
        guard = checker.SnapshotGuard(())
        independently_rebuilt = checker.rebuild_g0(guard)
        self.assertTrue(
            deep_exact(produced, independently_rebuilt),
            "producer/checker G0 released-authority contracts differ",
        )
        self.assertEqual(
            set(produced),
            {
                "all_released_full_inventories_rebound",
                "batch_target_lock",
                "fixed_predecessor_paths_only",
                "formal_target_lock",
                "protected_guard",
                "released_P60_C60",
                "schema_id",
                "target_object_and_conventions",
            },
        )
        self.assertGreaterEqual(guard.rebind_checks, 2)

    def test_no_duplicate_literal_dictionary_keys(self) -> None:
        for name in manifest.CODE_NAMES:
            if not name.endswith(".py"):
                continue
            for line, keys in _literal_string_dicts(CODE / name):
                self.assertEqual(len(keys), len(set(keys)), (name, line))

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 sources are not frozen")
    def test_producer_checker_theorem_call_graphs_are_disjoint(self) -> None:
        producer_imports = _imports(CODE / "c61_producer.py")
        checker_imports = _imports(CODE / "c61_checker.py")
        self.assertEqual(
            producer_imports & {name for name in producer_imports if name.startswith("c61_")},
            {"c61_exact", "c61_pipeline", "c61_group", "c61_resolvent"},
        )
        self.assertEqual(
            checker_imports & {name for name in checker_imports if name.startswith("c61_")},
            {"c61_exact", "c61_pipeline", "c61_checker_resolvent"},
        )
        self.assertNotIn("c61_checker", producer_imports)
        self.assertNotIn("c61_checker_group", producer_imports)
        self.assertNotIn("c61_checker_resolvent", producer_imports)
        self.assertNotIn("c61_producer", checker_imports)
        self.assertNotIn("c61_group", checker_imports)
        self.assertNotIn("c61_resolvent", checker_imports)
        checker_source = (CODE / "c61_checker.py").read_text(encoding="utf-8")
        self.assertIn("c61_checker_group.g", checker_source)

    @unittest.skipUnless(MACHINE_CONTRACT_FROZEN, "C61 payload contract is not frozen")
    def test_payload_key_scope_and_written_bridge_contract(self) -> None:
        assert FROZEN_PAYLOAD_KEYS is not None
        self.assertEqual(tuple(getattr(producer, "PAYLOAD_KEYS")), FROZEN_PAYLOAD_KEYS)
        self.assertEqual(tuple(getattr(checker, "PAYLOAD_KEYS")), FROZEN_PAYLOAD_KEYS)
        self.assertEqual(
            set(getattr(producer, "SCOPE_NONCLAIM_KEYS")), set(SCOPE_NONCLAIM_KEYS)
        )
        self.assertEqual(
            set(getattr(checker, "SCOPE_NONCLAIM_KEYS")), set(SCOPE_NONCLAIM_KEYS)
        )
        self.assertEqual(len(SCOPE_NONCLAIM_KEYS), 30)
    @unittest.skipUnless(MACHINE_CONTRACT_FROZEN, "C61 components/evidence are not frozen")
    def test_support_sources_and_evidence_are_frozen_and_scratch_free(self) -> None:
        assert FROZEN_SUPPORT_SOURCE_HASHES is not None
        assert FROZEN_EVIDENCE_HASHES is not None
        for name, expected in FROZEN_SUPPORT_SOURCE_HASHES.items():
            raw = (CODE / name).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), expected)
            self.assertNotIn("/tmp", raw.decode("utf-8"))
        for path in _fixture_evidence_paths():
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                FROZEN_EVIDENCE_HASHES[path.name],
            )
        self.assertTrue(
            deep_exact(producer_resolver.SCHEMA_SPEC, checker_resolver.SCHEMA)
        )
        self.assertEqual(
            producer_resolver.digest(producer_resolver.SCHEMA_SPEC),
            checker_resolver.H(checker_resolver.SCHEMA),
        )
        self.assertEqual(
            producer_resolver.EVIDENCE_BASENAME,
            "c61_resolvent_evidence.json",
        )
        self.assertEqual(
            checker_resolver.EVIDENCE_BASENAME,
            producer_resolver.EVIDENCE_BASENAME,
        )
        self.assertNotIn("c61_resolvent_schema.json", manifest.PROMOTED_NAMES)
        self.assertNotIn("c61_resolvent_check_report.json", manifest.PROMOTED_NAMES)
        self.assertNotIn(
            "c61_resolvent", _imports(CODE / "c61_checker_resolvent.py")
        )

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 resolver sources are not frozen")
    def test_resolver_cli_path_helpers_enforce_canonical_results_stage(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repository = Path(temporary) / "repository"
            project = (
                repository
                / "henon_dynamics"
                / "henon_mu3_yukawa_tensor_fourier_descent"
            )
            code = project / "code"
            results = project / "results"
            code.mkdir(parents=True)
            results.mkdir()
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            evidence = stage / "c61_resolvent_evidence.json"
            evidence.write_bytes(b"{}\n")
            producer_file = code / "c61_resolvent.py"
            producer_file.write_bytes(b"# installed resolver fixture\n")
            checker_file = code / "c61_checker_resolvent.py"
            checker_file.write_bytes(b"# installed resolver checker fixture\n")
            with (
                patch.object(producer_resolver, "__file__", str(producer_file)),
                patch.object(checker_resolver, "__file__", str(checker_file)),
            ):
                self.assertEqual(
                    producer_resolver.staged_evidence_path(
                        str(evidence), must_exist=True
                    )[1],
                    stage,
                )
                self.assertEqual(
                    checker_resolver.staged_evidence_path(
                        str(evidence), must_exist=True
                    )[1],
                    stage,
                )

                outside = project / "outside" / ".c61-stage-Ou7s1d34"
                nested = results / "arbitrary" / ".c61-stage-N3st3d99"
                punctuation = results / ".c61-stage-Abcd123!"
                overlong = results / ".c61-stage-ABCDEFGHI"
                for parent in (outside, nested, punctuation, overlong):
                    parent.mkdir(parents=True)
                real_stage = project / "real-stage"
                real_stage.mkdir()
                symlink_stage = results / ".c61-stage-Syml1nk2"
                symlink_stage.symlink_to(real_stage, target_is_directory=True)
                for parent in (
                    code,
                    results,
                    outside,
                    nested,
                    punctuation,
                    overlong,
                    symlink_stage,
                ):
                    for helper, error in (
                        (
                            producer_resolver.staged_evidence_path,
                            producer_resolver.Failure,
                        ),
                        (
                            checker_resolver.staged_evidence_path,
                            checker_resolver.Reject,
                        ),
                    ):
                        with self.subTest(
                            helper=helper.__module__, parent=parent
                        ), self.assertRaises(error):
                            helper(
                                str(parent / "c61_resolvent_evidence.json"),
                                must_exist=True,
                            )

        producer_source = (CODE / "c61_resolvent.py").read_text(encoding="utf-8")
        producer_main = producer_source.index("def main()")
        self.assertLess(
            producer_source.index("staged_evidence_path(", producer_main),
            producer_source.index("build_candidate(", producer_main),
        )
        checker_source = (CODE / "c61_checker_resolvent.py").read_text(
            encoding="utf-8"
        )
        checker_main = checker_source.index("def main()")
        self.assertLess(
            checker_source.index("staged_evidence_path(", checker_main),
            checker_source.index("final_check(", checker_main),
        )

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 resolver sources are not frozen")
    def test_resolver_clis_write_replay_and_reject_hostile_stage_parents(self) -> None:
        def invoke(entrypoint: object, argv: list[str]) -> dict[str, object]:
            raw_output = io.BytesIO()
            output = io.TextIOWrapper(raw_output, encoding="utf-8", write_through=True)
            with patch.object(sys, "argv", argv), redirect_stdout(output):
                entrypoint()  # type: ignore[operator]
            return json.loads(raw_output.getvalue().decode("utf-8"))

        def snapshot(path: Path) -> tuple[bytes, int, int, int, int, int, int]:
            metadata = path.stat()
            return (
                path.read_bytes(),
                metadata.st_dev,
                metadata.st_ino,
                metadata.st_mode,
                metadata.st_size,
                metadata.st_mtime_ns,
                metadata.st_ctime_ns,
            )

        with tempfile.TemporaryDirectory() as temporary:
            repository = Path(temporary) / "repository"
            project = (
                repository
                / "henon_dynamics"
                / "henon_mu3_yukawa_tensor_fourier_descent"
            )
            code = project / "code"
            results = project / "results"
            code.mkdir(parents=True)
            results.mkdir()
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            evidence = stage / "c61_resolvent_evidence.json"
            producer_file = code / "c61_resolvent.py"
            producer_file.write_bytes(b"# frozen producer resolver fixture\n")
            checker_file = code / "c61_checker_resolvent.py"
            checker_file.write_bytes(b"# frozen checker resolver fixture\n")
            authority = {"fixture": "authority"}
            candidate = {
                "authority": authority,
                "payload_sha256": "0" * 64,
            }
            attestation = {"status": "PASS"}
            final = {
                "authority": authority,
                "payload_sha256": "1" * 64,
                "status": {"resolver_component_status": "RESOLVER_COMPONENT_PASS"},
            }
            runtime_snapshot = {"fixture": {"sha256": "2" * 64}}
            with (
                patch.object(producer_resolver, "__file__", str(producer_file)),
                patch.object(
                    producer_resolver,
                    "runtime_input_snapshot",
                    return_value=runtime_snapshot,
                ),
                patch.object(
                    producer_resolver,
                    "bind_authority",
                    return_value=(authority, {}),
                ),
                patch.object(
                    producer_resolver, "build_candidate", return_value=candidate
                ) as build_candidate,
                patch.object(
                    producer_resolver, "invoke_checker", return_value=attestation
                ) as invoke_checker,
                patch.object(producer_resolver, "finalize", return_value=final),
            ):
                written = invoke(
                    producer_resolver.main,
                    ["c61_resolvent.py", "--output", str(evidence)],
                )
                evidence_snapshot = snapshot(evidence)
                replayed = invoke(
                    producer_resolver.main,
                    ["c61_resolvent.py", "--check-existing", str(evidence)],
                )
                self.assertEqual(snapshot(evidence), evidence_snapshot)
                self.assertEqual(written["mode"], "write")
                self.assertEqual(replayed["mode"], "check-existing")
                self.assertEqual(build_candidate.call_count, 4)
                self.assertEqual(invoke_checker.call_count, 4)

                outside = project / "outside" / ".c61-stage-Ou7s1d34"
                nested = results / "arbitrary" / ".c61-stage-N3st3d99"
                punctuation = results / ".c61-stage-Abcd123!"
                overlong = results / ".c61-stage-ABCDEFGHI"
                for parent in (outside, nested, punctuation, overlong):
                    parent.mkdir(parents=True)
                real_stage = project / "real-stage"
                real_stage.mkdir()
                symlink_stage = results / ".c61-stage-Syml1nk2"
                symlink_stage.symlink_to(real_stage, target_is_directory=True)
                rejected_parents = (
                    code, results, outside, nested, punctuation, overlong, symlink_stage
                )
                before_hostile_calls = build_candidate.call_count
                for parent in rejected_parents:
                    hostile_evidence = parent / evidence.name
                    with self.subTest(
                        cli="producer", target=hostile_evidence
                    ), self.assertRaises(producer_resolver.Failure):
                        invoke(
                            producer_resolver.main,
                            ["c61_resolvent.py", "--output", str(hostile_evidence)],
                        )
                self.assertEqual(build_candidate.call_count, before_hostile_calls)

            check_result = {
                "checker_status": "PASS",
                "resolver_component_status": "RESOLVER_COMPONENT_PASS",
            }
            with (
                patch.object(checker_resolver, "__file__", str(checker_file)),
                patch.object(
                    checker_resolver,
                    "final_check",
                    return_value=check_result,
                ) as final_check,
            ):
                first = invoke(
                    checker_resolver.main,
                    [
                        "c61_checker_resolvent.py",
                        "--check-existing",
                        str(evidence),
                    ],
                )
                evidence_snapshot = snapshot(evidence)
                second = invoke(
                    checker_resolver.main,
                    [
                        "c61_checker_resolvent.py",
                        "--check-existing",
                        str(evidence),
                    ],
                )
                self.assertEqual(snapshot(evidence), evidence_snapshot)
                self.assertEqual(first, check_result)
                self.assertEqual(second, check_result)
                self.assertEqual(final_check.call_count, 2)

                with patch.object(
                    checker_resolver,
                    "make_attestation",
                    return_value=attestation,
                ) as make_attestation:
                    self.assertEqual(
                        checker_resolver.attest_candidate_document(
                            evidence.read_bytes(), evidence
                        ),
                        attestation,
                    )
                    self.assertEqual(make_attestation.call_count, 1)

                before_hostile_calls = final_check.call_count
                for parent in rejected_parents:
                    hostile_evidence = parent / evidence.name
                    with self.subTest(
                        cli="checker", target=hostile_evidence
                    ), self.assertRaises(SystemExit):
                        invoke(
                            checker_resolver.main,
                            [
                                "c61_checker_resolvent.py",
                                "--check-existing",
                                str(hostile_evidence),
                            ],
                        )
                self.assertEqual(final_check.call_count, before_hostile_calls)

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 checker source is not frozen")
    def test_checker_accepts_only_one_canonical_direct_stage_parent(self) -> None:
        def namespace(parent: Path) -> SimpleNamespace:
            for name in (
                "c61_certificate.json",
                "c61_schema.json",
                "c61_group_evidence.json",
                "c61_resolvent_evidence.json",
            ):
                (parent / name).write_bytes((name + "\n").encode())
            return SimpleNamespace(
                certificate=parent / "c61_certificate.json",
                schema=parent / "c61_schema.json",
                group_evidence=parent / "c61_group_evidence.json",
                resolvent_evidence=parent / "c61_resolvent_evidence.json",
                output=parent / "c61_check_report.json",
            )

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            results = project / "results"
            results.mkdir(parents=True)
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            arguments = namespace(stage)
            with patch.object(checker, "PROJECT", project):
                accepted = checker.validate_fixed_paths(arguments)
            self.assertEqual(accepted[-1], stage)

            direct = namespace(results)
            with (
                patch.object(checker, "PROJECT", project),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(direct)

            nested = results / "arbitrary" / ".c61-stage-N3st3d99"
            nested.mkdir(parents=True)
            nested_arguments = namespace(nested)
            with (
                patch.object(checker, "PROJECT", project),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(nested_arguments)

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            results = project / "results"
            results.mkdir(parents=True)
            real_stage = results / ".real-stage"
            real_stage.mkdir()
            symlink_stage = results / ".c61-stage-Syml1nk2"
            symlink_stage.symlink_to(real_stage, target_is_directory=True)
            symlink_arguments = namespace(symlink_stage)
            with (
                patch.object(checker, "PROJECT", project),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(symlink_arguments)

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 checker source is not frozen")
    def test_checker_rejects_stage_symlink_swap_during_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            results = project / "results"
            results.mkdir(parents=True)
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            foreign = results / "foreign"
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            for name in (
                "c61_certificate.json",
                "c61_schema.json",
                "c61_group_evidence.json",
                "c61_resolvent_evidence.json",
            ):
                (stage / name).write_bytes((name + "\n").encode())
            arguments = SimpleNamespace(
                certificate=stage / "c61_certificate.json",
                schema=stage / "c61_schema.json",
                group_evidence=stage / "c61_group_evidence.json",
                resolvent_evidence=stage / "c61_resolvent_evidence.json",
                output=stage / "c61_check_report.json",
            )
            original = checker.seal_directory
            calls = 0

            def swap_on_rebind(path: Path):
                nonlocal calls
                calls += 1
                if calls == 2:
                    held = stage.with_name(stage.name + "-held")
                    stage.rename(held)
                    stage.symlink_to(foreign, target_is_directory=True)
                return original(path)

            with (
                patch.object(checker, "PROJECT", project),
                patch.object(checker, "seal_directory", side_effect=swap_on_rebind),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(arguments)
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 producer source is not frozen")
    def test_producer_accepts_only_one_canonical_direct_stage_parent(self) -> None:
        def namespace(parent: Path) -> SimpleNamespace:
            (parent / "c61_group_evidence.json").write_bytes(b"group\n")
            (parent / "c61_resolvent_evidence.json").write_bytes(b"resolvent\n")
            return SimpleNamespace(
                artifact_dir=parent,
                output=parent / "c61_certificate.json",
                schema_output=parent / "c61_schema.json",
            )

        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "project" / "results"
            results.mkdir(parents=True)
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            with patch.object(producer, "RESULTS", results):
                binding = producer.validate_fixed_paths(namespace(stage))
            self.assertEqual(binding.parent, stage)

            with (
                patch.object(producer, "RESULTS", results),
                self.assertRaises(StrictDataError),
            ):
                producer.validate_fixed_paths(namespace(results))

            nested = results / "arbitrary" / ".c61-stage-N3st3d99"
            nested.mkdir(parents=True)
            with (
                patch.object(producer, "RESULTS", results),
                self.assertRaises(StrictDataError),
            ):
                producer.validate_fixed_paths(namespace(nested))

        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "project" / "results"
            results.mkdir(parents=True)
            real_stage = results / ".real-stage"
            real_stage.mkdir()
            symlink_stage = results / ".c61-stage-Syml1nk2"
            symlink_stage.symlink_to(real_stage, target_is_directory=True)
            with (
                patch.object(producer, "RESULTS", results),
                self.assertRaises(StrictDataError),
            ):
                producer.validate_fixed_paths(namespace(symlink_stage))

    @unittest.skipUnless(RELEASE_SOURCES_FROZEN, "C61 producer source is not frozen")
    def test_producer_stage_binding_rejects_later_symlink_swap(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "project" / "results"
            results.mkdir(parents=True)
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            (stage / "c61_group_evidence.json").write_bytes(b"group\n")
            (stage / "c61_resolvent_evidence.json").write_bytes(b"resolvent\n")
            arguments = SimpleNamespace(
                artifact_dir=stage,
                output=stage / "c61_certificate.json",
                schema_output=stage / "c61_schema.json",
            )
            with patch.object(producer, "RESULTS", results):
                binding = producer.validate_fixed_paths(arguments)
            held = stage.with_name(stage.name + "-held")
            foreign = results / "foreign"
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            stage.rename(held)
            stage.symlink_to(foreign, target_is_directory=True)
            with self.assertRaises(StrictDataError):
                binding.assert_unchanged("unit symlink swap")
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    def test_backend_allowlist_excludes_extra_cas(self) -> None:
        self.assertEqual(
            set(pipeline.EXPECTED_BACKENDS),
            {"math"},
        )
        self.assertEqual(
            pipeline.EXPECTED_BACKENDS["math"]["python"], [3, 12, 3]
        )
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["flint"], "0.9.0")
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["sympy"], "1.14.0")
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["networkx"], "3.5")
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["jsonschema"], "4.25.0")
        self.assertEqual(pipeline.EXPECTED_GAP["gap_version"], "4.11.1")
        self.assertEqual(pipeline.EXPECTED_GAP["tomlib_version"], "1.2.9")
        self.assertEqual(pipeline.EXPECTED_GAP["smallgrp_version"], "1.4.1")
        self.assertEqual(pipeline.EXPECTED_GAP["ctbllib_version"], "1.3.1")
        runner = (CODE / "run_all.sh").read_text(encoding="utf-8").lower()
        for forbidden in ("pari_python", "cypari", "singular"):
            self.assertNotIn(forbidden, runner)
        self.assertIn('--math-python "$MATH_PYTHON"', (CODE / "run_all.sh").read_text())

    def test_clean_refresh_fixture_override_and_hostile_paths(self) -> None:
        blobs = (b'{"kind":"group"}\n', b'{"kind":"resolver"}\n')

        def populate(parent: Path) -> None:
            parent.mkdir(parents=True, exist_ok=True)
            for name, blob in zip(EVIDENCE_NAMES, blobs):
                (parent / name).write_bytes(blob)

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            code = project / "code"
            results = project / "results"
            code.mkdir(parents=True)
            results.mkdir()
            for name in manifest.CODE_NAMES:
                (code / name).write_bytes((name + "\n").encode())
            for name in ("RESULTS.md", "TEST_REPORT.md"):
                (results / name).write_bytes((name + "\n").encode())
            stage = results / ".c61-stage-A1b2C3d4"
            populate(stage)
            module = sys.modules[__name__]
            with (
                patch.object(module, "RESULTS", results),
                patch.dict(os.environ, {TEST_EVIDENCE_ENV: str(stage)}),
            ):
                self.assertEqual(
                    _fixture_evidence_paths(),
                    tuple(stage / name for name in EVIDENCE_NAMES),
                )

            outside = project / "outside" / ".c61-stage-Ou7s1d34"
            nested = results / "arbitrary" / ".c61-stage-N3st3d99"
            punctuation = results / ".c61-stage-Abcd123!"
            overlong = results / ".c61-stage-ABCDEFGHI"
            for parent in (outside, nested, punctuation, overlong):
                populate(parent)
            foreign = project / "foreign-stage"
            populate(foreign)
            symlink_stage = results / ".c61-stage-Syml1nk2"
            symlink_stage.symlink_to(foreign, target_is_directory=True)
            extra_stage = results / ".c61-stage-Extra123"
            populate(extra_stage)
            (extra_stage / "unexpected").write_bytes(b"hostile\n")
            file_symlink_stage = results / ".c61-stage-Link1234"
            file_symlink_stage.mkdir()
            (file_symlink_stage / EVIDENCE_NAMES[0]).write_bytes(blobs[0])
            (file_symlink_stage / EVIDENCE_NAMES[1]).symlink_to(
                stage / EVIDENCE_NAMES[1]
            )
            rejected = (
                code,
                results,
                outside,
                nested,
                punctuation,
                overlong,
                symlink_stage,
                extra_stage,
                file_symlink_stage,
                Path(".c61-stage-relative"),
            )
            with patch.object(module, "RESULTS", results):
                for candidate in rejected:
                    with (
                        self.subTest(candidate=candidate),
                        patch.dict(
                            os.environ, {TEST_EVIDENCE_ENV: str(candidate)}
                        ),
                        self.assertRaises(StrictDataError),
                    ):
                        _fixture_evidence_paths()

        runner = (CODE / "run_all.sh").read_text(encoding="utf-8")
        rejection = runner.index(
            "PYTHONPATH PYTHONHOME PYTHONSAFEPATH BASH_ENV ENV C61_TEST_EVIDENCE_DIR"
        )
        stage_assignment = runner.index('C61_TEST_EVIDENCE_DIR="$STAGE_DIR"')
        unittest_launch = runner.index("-m unittest discover")
        self.assertLess(rejection, stage_assignment)
        self.assertLess(stage_assignment, unittest_launch)
        self.assertEqual(runner.count('C61_TEST_EVIDENCE_DIR="$STAGE_DIR"'), 1)

    @unittest.skipUnless(MACHINE_CONTRACT_FROZEN, "C61 shared payload contract is not frozen")
    def test_actual_payload_builders_match_on_shared_fixture(self) -> None:
        fixture = _actual_shared_fixture()
        produced = fixture["produced_payload"]
        expected = fixture["expected_payload"]
        schema = fixture["expected_schema"]
        self.assertTrue(deep_exact(produced, expected))
        self.assertEqual(tuple(produced), FROZEN_PAYLOAD_KEYS)
        self.assertEqual(producer.scalar_leaf_count(produced), 19_078)
        self.assertEqual(checker.scalar_leaf_count(expected), 19_078)
        self.assertEqual(checker.scalar_leaf_count(schema), 29)
        self.assertEqual(
            hashlib.sha256(canonical_leaf_bytes(schema)).hexdigest(),
            FROZEN_OWNER_SCHEMA_CONTRACT["canonical_leaf_sha256"],
        )
        self.assertEqual(
            expected["G7_independence_sources_scope_release"]
            ["evidence_rebound_mutation_count_expected"],
            10,
        )
        self.assertGreaterEqual(fixture["guard"].rebind_checks, 10)

    @unittest.skipUnless(MACHINE_CONTRACT_FROZEN, "C61 hostile-count contract is not frozen")
    def test_actual_evidence_and_artifact_hostile_case_count(self) -> None:
        fixture = _actual_shared_fixture()
        result = checker.evidence_rebound_suite(
            fixture["certificate"],
            fixture["expected_schema"],
            fixture["expected_payload"],
            fixture["expected_schema"],
            fixture["group_document"],
            fixture["resolver_document"],
            fixture["resolver_path"],
            fixture["guard"],
        )
        families = FROZEN_OWNER_HOSTILE_FAMILY_SPLIT
        counts = FROZEN_G7_COUNTS
        assert counts is not None
        self.assertEqual(
            tuple(result["actual_group_verifier_mutation_families"]),
            families["group_evidence"],
        )
        self.assertEqual(
            tuple(result["actual_resolver_verifier_mutation_families"]),
            families["resolver_evidence"],
        )
        self.assertEqual(
            tuple(result["additional_artifact_hostile_families"]),
            families["artifact_contract"],
        )
        self.assertEqual(
            result["actual_group_verifier_mutations_rejected"],
            counts["group_evidence_mutation_count"],
        )
        self.assertEqual(
            result["actual_resolver_verifier_mutations_rejected"],
            counts["resolver_evidence_mutation_count"],
        )
        self.assertEqual(
            result["self_consistent_evidence_rebound_mutations_rejected"],
            counts["evidence_rebound_mutation_count_expected"],
        )
        self.assertEqual(
            result["additional_artifact_hostile_rebounds_rejected"],
            counts["artifact_mutation_count"],
        )
        self.assertEqual(
            result["total_evidence_and_artifact_rebounds_rejected"],
            FROZEN_ACTUAL_DEEP_HOSTILE_CASE_COUNT,
        )

    def test_runner_freezes_and_orders_runtime_counter_contract(self) -> None:
        source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        checker_call = source.index('"$MATH_PYTHON" -s -B "$CODE_DIR/c61_checker.py"')
        runtime_check = source.index("--verify-runtime-report")
        manifest_write = source.index("--write", runtime_check)
        self.assertLess(checker_call, runtime_check)
        self.assertLess(runtime_check, manifest_write)
        self.assertEqual(source.count("--verify-runtime-report"), 1)
        self.assertIsNotNone(pipeline.FROZEN_RUNTIME_REPORT_CONTRACT)
        contract = pipeline.FROZEN_RUNTIME_REPORT_CONTRACT
        assert contract is not None
        self.assertEqual(
            contract["scalar_leaf_rebound"],
            {
                "payload_type_mutations_rejected": 19_078,
                "payload_value_mutations_rejected": 19_078,
                "root_type_mutations_rejected": 2,
                "root_value_mutations_rejected": 2,
                "schema_type_mutations_rejected": 29,
                "schema_value_mutations_rejected": 29,
                "structural_mutations_rejected": 14,
                "total_certificate_mutations_rejected": 38_232,
                "type_mutations_rejected": 19_109,
                "value_mutations_rejected": 19_109,
            },
        )
        self.assertEqual(
            contract["evidence_rebound"],
            {
                "actual_group_verifier_mutation_families": list(
                    FROZEN_OWNER_HOSTILE_FAMILY_SPLIT["group_evidence"]
                ),
                "actual_group_verifier_mutations_rejected": 6,
                "actual_resolver_verifier_mutation_families": list(
                    FROZEN_OWNER_HOSTILE_FAMILY_SPLIT["resolver_evidence"]
                ),
                "actual_resolver_verifier_mutations_rejected": 4,
                "additional_artifact_hostile_families": list(
                    FROZEN_OWNER_HOSTILE_FAMILY_SPLIT["artifact_contract"]
                ),
                "additional_artifact_hostile_rebounds_rejected": 2,
                "self_consistent_evidence_rebound_mutations_rejected": 10,
                "total_evidence_and_artifact_rebounds_rejected": 12,
            },
        )
        with self.assertRaisesRegex(
            StrictDataError, "canonical direct results child"
        ):
            pipeline.verify_runtime_report(Path("/unbound/.c61-stage-A1b2C3d4"))

    def test_runner_has_explicit_three_state_and_persistent_dirfd_contract(self) -> None:
        source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        for token in (
            'RUN_STATE="STAGED_VERIFIED"',
            'RUN_STATE="LIVE_COMMITTED"',
            'RUN_STATE="RELEASE_VERIFIED"',
            "POSTCOMMIT_INCOMPLETE",
            "COMMITTED_WITH_DEBRIS—DO NOT RETRY",
            'exec {RESULTS_FD}<"$RESULTS_DIR"',
            'stat -Lc \'%d\' "/proc/self/fd/$RESULTS_FD"',
            'stat -Lc \'%i\' "/proc/self/fd/$RESULTS_FD"',
            "results pathname device/inode changed",
            "results parent identity changed; retaining all stage/transaction evidence",
        ):
            self.assertIn(token, source)
        self.assertGreaterEqual(source.count("verify_results_binding"), 20)
        self.assertIn(
            'mktemp -d "/proc/self/fd/$RESULTS_FD/.c61-stage-XXXXXXXX"', source
        )
        self.assertNotIn(
            'mktemp -d "$RESULTS_DIR/.c61-stage-XXXXXXXX"', source
        )
        self.assertIn(
            '--group-evidence "$STAGE_DIR/c61_group_evidence.json"', source
        )
        self.assertIn(
            '--resolvent-evidence "$STAGE_DIR/c61_resolvent_evidence.json"', source
        )
        self.assertNotIn('exec /usr/bin/bash -p "$CODE_DIR/run_all.sh"', source)
        self.assertIn('/usr/bin/bash -p "$CODE_DIR/run_all.sh"', source)
        match = re.search(
            r"classify_promotion_status\(\) \{.*?^\}",
            source,
            flags=re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(match)
        probe = (
            match.group(0)
            + "\nfor value in 0 74 75 1 2 129 137 143; do "
            + 'classify_promotion_status "$value"; '
            + 'printf "%s\\n" "$PROMOTION_CLASS"; done\n'
        )
        completed = subprocess.run(
            ["/usr/bin/bash", "-p", "-c", probe],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            env={"PATH": "/usr/bin:/bin"},
            cwd="/",
        )
        self.assertEqual(
            completed.stdout.splitlines(),
            [
                b"LIVE_COMMITTED",
                b"ROLLED_BACK_VERIFIED",
                b"LIVE_COMMITTED_WITH_DEBRIS",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
            ],
        )

    def test_documented_no_concurrent_mutator_boundary_is_not_overclaimed(self) -> None:
        readme = " ".join(
            (CODE / "README.md").read_text(encoding="utf-8").split()
        )
        required = (
            "same-UID",
            "no concurrent pathname mutator",
            "between an external child",
            "first path open",
            "inherited directory fds",
            "reserved `C61_TEST_EVIDENCE_DIR`",
            "runner alone may set",
            "dynamic loader precedes Bash",
            "`PREFREEZE_CODE_RESULTS_PASS`",
            "no paper result, authoritative refresh, promotion authorization, or release",
        )
        for token in required:
            self.assertIn(token, readme)



def _write(path: Path, raw: bytes, mode: int, mtime_ns: int) -> None:
    path.write_bytes(raw)
    path.chmod(mode)
    os.utime(path, ns=(mtime_ns, mtime_ns))


def _snapshot(path: Path) -> tuple[bytes, int, int] | None:
    if not path.exists():
        return None
    metadata = path.stat()
    return path.read_bytes(), stat.S_IMODE(metadata.st_mode), metadata.st_mtime_ns


class AtomicPromotionTests(unittest.TestCase):
    def make_layout(self, root: Path, state: str) -> tuple[Path, Path, list[tuple[Path, str]], dict[str, tuple[bytes, int, int] | None]]:
        results = root / "results"
        results.mkdir()
        _write(results / "RESULTS.md", b"results\n", 0o644, 1_700_000_000_000_000_001)
        _write(results / "TEST_REPORT.md", b"tests\n", 0o644, 1_700_000_000_000_000_002)
        stage = results / ".c61-stage-A1b2C3d4"
        stage.mkdir()
        pairs = []
        before = {}
        for index, name in enumerate(atomic.EXPECTED_TARGET_NAMES):
            source = stage / name
            _write(
                source,
                f"new-{index}\n".encode(),
                0o600 + index % 4,
                1_710_000_000_000_000_000 + index,
            )
            target = results / name
            exists = state == "existing" or (state == "mixed" and index % 2 == 0)
            if exists:
                _write(
                    target,
                    f"old-{index}\n".encode(),
                    0o640 + index % 4,
                    1_690_000_000_000_000_000 + index,
                )
            before[name] = _snapshot(target)
            pairs.append((source, name))
        return results, stage, pairs, before

    def promote(
        self,
        pairs: list[tuple[Path, str]],
        results: Path,
        *,
        fail_after: int | None = None,
    ) -> None:
        stage = results / ".c61-stage-A1b2C3d4"
        metadata = stage.lstat()
        snapshot = atomic.stage_snapshot(
            results,
            stage,
            expected_device=metadata.st_dev,
            expected_inode=metadata.st_ino,
        )
        atomic.promote(
            pairs,
            results,
            expected_stage_snapshot=snapshot,
            fail_after=fail_after,
        )

    def assert_preimage(self, results: Path, before: dict[str, tuple[bytes, int, int] | None]) -> None:
        for name, expected in before.items():
            self.assertEqual(_snapshot(results / name), expected, name)
        self.assertFalse((results / atomic.LOCK_NAME).exists())
        self.assertFalse(any(path.name.startswith(".c61-transaction-") for path in results.iterdir()))

    def test_all_six_injected_failures_restore_absent_existing_and_mixed(self) -> None:
        for state in ("absent", "existing", "mixed"):
            for failure in range(1, 7):
                with self.subTest(state=state, failure=failure), tempfile.TemporaryDirectory() as temporary:
                    results, _, pairs, before = self.make_layout(Path(temporary), state)
                    with self.assertRaisesRegex(RuntimeError, "test-injected"):
                        self.promote(pairs, results, fail_after=failure)
                    self.assert_preimage(results, before)

    def test_success_promotes_all_six(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "mixed")
            expected = {name: _snapshot(source) for source, name in pairs}
            self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)

    def test_post_rename_failure_is_durable_and_rolled_back(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original_replace = atomic.os.replace
            original_bound_fsync = atomic._fsync_directory_binding
            original_fingerprint = atomic._fingerprint_at
            events: list[str] = []
            renamed = False
            injected = False

            def tracked_replace(source, target, *args, **kwargs):
                nonlocal renamed
                value = original_replace(source, target, *args, **kwargs)
                if Path(source).name.startswith("new-"):
                    renamed = True
                    events.append("rename")
                return value

            def tracked_bound(binding, label):
                value = original_bound_fsync(binding, label)
                if renamed and binding.path.name.startswith(".c61-transaction-"):
                    events.append("transaction-fsync")
                elif renamed and binding.path == results:
                    events.append("result-fsync")
                return value

            def fail_placed(binding, name, label="file"):
                nonlocal injected
                if label == "placed target" and not injected:
                    injected = True
                    self.assertEqual(
                        events[-3:], ["rename", "transaction-fsync", "result-fsync"]
                    )
                    raise RuntimeError("post-rename fingerprint injection")
                return original_fingerprint(binding, name, label)

            with (
                patch.object(atomic.os, "replace", side_effect=tracked_replace),
                patch.object(atomic, "_fsync_directory_binding", side_effect=tracked_bound),
                patch.object(atomic, "_fingerprint_at", side_effect=fail_placed),
                self.assertRaisesRegex(RuntimeError, "post-rename"),
            ):
                self.promote(pairs, results)
            self.assertTrue(injected)
            self.assert_preimage(results, before)

    def test_result_parent_fd_rejects_rename_symlink_at_commit_boundaries(self) -> None:
        for boundary in ("precommit", "after-first-replacement"):
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                results, _, pairs, before = self.make_layout(root, "existing")
                held_results = root / "results-held"
                foreign = root / "foreign-results"
                foreign.mkdir()
                (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")

                def substitute_parent() -> None:
                    results.rename(held_results)
                    results.symlink_to(foreign, target_is_directory=True)

                if boundary == "precommit":
                    original_precommit = atomic._verify_precommit_preimages

                    def hostile_precommit(entries, result_binding, transaction_binding):
                        original_precommit(entries, result_binding, transaction_binding)
                        substitute_parent()

                    context = patch.object(
                        atomic,
                        "_verify_precommit_preimages",
                        side_effect=hostile_precommit,
                    )
                else:
                    original_replace = atomic.os.replace
                    substituted = False

                    def hostile_replace(source, target, *args, **kwargs):
                        nonlocal substituted
                        value = original_replace(source, target, *args, **kwargs)
                        if not substituted and Path(source).name.startswith("new-"):
                            substituted = True
                            substitute_parent()
                        return value

                    context = patch.object(
                        atomic.os, "replace", side_effect=hostile_replace
                    )

                with context, self.assertRaisesRegex(
                    atomic.RollbackError, "directory pathname identity changed"
                ):
                    self.promote(pairs, results)

                self.assertTrue(results.is_symlink())
                self.assertEqual(results.resolve(strict=True), foreign)
                self.assertEqual(
                    {path.name for path in foreign.iterdir()}, {"sentinel"}
                )
                self.assertEqual(
                    (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
                )
                self.assertTrue((held_results / atomic.LOCK_NAME).exists())
                self.assertTrue(
                    any(
                        path.name.startswith(".c61-transaction-")
                        for path in held_results.iterdir()
                    )
                )
                if boundary == "precommit":
                    for name, expected in before.items():
                        self.assertEqual(_snapshot(held_results / name), expected)

    def test_postcommit_cleanup_and_lock_failures_are_distinct_committed_outcomes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            expected = {name: _snapshot(source) for source, name in pairs}
            with patch.object(
                atomic, "_cleanup_transaction", side_effect=OSError("cleanup injection")
            ):
                with self.assertRaisesRegex(
                    atomic.PostCommitError, "COMMITTED_WITH_DEBRIS.*DO NOT RETRY"
                ):
                    self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)
            self.assertTrue(
                any(path.name.startswith(".c61-transaction-") for path in results.iterdir())
            )
            self.assertFalse((results / atomic.LOCK_NAME).exists())

        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            expected = {name: _snapshot(source) for source, name in pairs}
            original_release = atomic.release_lock

            def foreign_release(lock, result_binding):
                held = lock.path.with_name(".held-original-lock")
                lock.path.rename(held)
                lock.path.write_bytes(b"foreign-lock\n")
                return original_release(lock, result_binding)

            with patch.object(atomic, "release_lock", side_effect=foreign_release):
                with self.assertRaisesRegex(atomic.PostCommitError, "COMMITTED_WITH_DEBRIS"):
                    self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)
            self.assertEqual((results / atomic.LOCK_NAME).read_bytes(), b"foreign-lock\n")
            self.assertFalse(
                any(path.name.startswith(".c61-transaction-") for path in results.iterdir())
            )

    def test_postcommit_cli_has_fixed_distinct_exit_code(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, stage, pairs, _ = self.make_layout(Path(temporary), "absent")
            metadata = stage.stat()
            snapshot = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            snapshot_argument = canonical_json_bytes(snapshot).decode().rstrip("\n")
            argv = ["c61_atomic_promote.py", "--result-dir", str(results)]
            for source, target in pairs:
                argv.extend(("--source", str(source), "--target", target))
            argv.extend(("--expected-stage-snapshot", snapshot_argument))
            stderr = io.StringIO()
            with (
                patch.object(sys, "argv", argv),
                patch.object(
                    atomic,
                    "promote",
                    side_effect=atomic.PostCommitError("COMMITTED_WITH_DEBRIS: test"),
                ),
                redirect_stderr(stderr),
            ):
                self.assertEqual(atomic.main(), atomic.POSTCOMMIT_EXIT_CODE)
            self.assertIn("COMMITTED_WITH_DEBRIS", stderr.getvalue())
            rollback_stderr = io.StringIO()
            with (
                patch.object(sys, "argv", argv),
                patch.object(
                    atomic,
                    "promote",
                    side_effect=atomic.RolledBackVerifiedError(
                        "ROLLED_BACK_VERIFIED: test"
                    ),
                ),
                redirect_stderr(rollback_stderr),
            ):
                self.assertEqual(atomic.main(), atomic.ROLLED_BACK_EXIT_CODE)
            self.assertIn("ROLLED_BACK_VERIFIED", rollback_stderr.getvalue())

    def test_wrong_count_order_name_and_duplicate_source_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "absent")
            hostile = (
                pairs[:-1],
                [pairs[1], pairs[0], *pairs[2:]],
                [*pairs[:-1], (pairs[-1][0], "wrong.json")],
                [pairs[0], (pairs[0][0], pairs[1][1]), *pairs[2:]],
            )
            for request in hostile:
                with self.subTest(request=[name for _, name in request]), self.assertRaises(StrictDataError):
                    self.promote(request, results)

    def test_symlink_fifo_and_hardlink_sources_rejected(self) -> None:
        mutations = ("symlink", "fifo", "hardlink")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                results, stage, pairs, _ = self.make_layout(root, "absent")
                source = pairs[0][0]
                source.unlink()
                if mutation == "symlink":
                    source.symlink_to(stage / atomic.EXPECTED_TARGET_NAMES[1])
                elif mutation == "fifo":
                    os.mkfifo(source)
                else:
                    _write(source, b"hardlinked\n", 0o600, 1_700_000_000_000_000_000)
                    os.link(source, root / "external-link")
                with self.assertRaises(StrictDataError):
                    self.promote(pairs, results)

    def test_cross_location_and_foreign_debris_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, tempfile.TemporaryDirectory() as external:
            results, _, pairs, _ = self.make_layout(Path(temporary), "absent")
            foreign = Path(external) / "foreign"
            foreign.write_bytes(b"foreign")
            hostile_pairs = [(foreign, pairs[0][1]), *pairs[1:]]
            with self.assertRaises(StrictDataError):
                self.promote(hostile_pairs, results)
        for debris in (".c61-stage-stale", ".c61-transaction-stale", atomic.LOCK_NAME):
            with self.subTest(debris=debris), tempfile.TemporaryDirectory() as temporary:
                results, _, pairs, _ = self.make_layout(Path(temporary), "absent")
                path = results / debris
                if debris == atomic.LOCK_NAME:
                    path.write_bytes(b"stale\n")
                else:
                    path.mkdir()
                with self.assertRaisesRegex(StrictDataError, "debris"):
                    self.promote(pairs, results)

    def test_target_hardlink_result_symlink_parent_symlink_and_dangling_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            results, _, pairs, _ = self.make_layout(root, "existing")
            os.link(results / pairs[0][1], root / "target-hardlink")
            with self.assertRaises(StrictDataError):
                self.promote(pairs, results)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            results, stage, pairs, _ = self.make_layout(root, "absent")
            alias = root / "results-alias"
            alias.symlink_to(results, target_is_directory=True)
            with self.assertRaises(StrictDataError):
                self.promote(pairs, alias)
            stage_alias = root / "stage-alias"
            stage_alias.symlink_to(stage, target_is_directory=True)
            hostile = [(stage_alias / source.name, name) for source, name in pairs]
            with self.assertRaises(StrictDataError):
                self.promote(hostile, results)
            pairs[0][0].unlink()
            pairs[0][0].symlink_to(root / "missing")
            with self.assertRaises(StrictDataError):
                self.promote(pairs, results)

    def test_precommit_target_and_final_source_mutations_are_rejected_and_rolled_back(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original = atomic._verify_precommit_preimages

            def mutate_target(entries, result_binding, transaction_binding):
                entries[0].target.write_bytes(b"hostile-target\n")
                return original(entries, result_binding, transaction_binding)

            with patch.object(atomic, "_verify_precommit_preimages", side_effect=mutate_target):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results)
            # The hostile precommit mutation is deliberately not overwritten:
            # no live replacement had yet been authorized.
            self.assertEqual((results / pairs[0][1]).read_bytes(), b"hostile-target\n")
            self.assertTrue(any(path.name.startswith(".c61-transaction-") for path in results.iterdir()))

        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original = atomic._verify_precommit_preimages

            def mutate_source(entries, result_binding, transaction_binding):
                original(entries, result_binding, transaction_binding)
                entries[0].source.write_bytes(b"hostile-source\n")

            with patch.object(atomic, "_verify_precommit_preimages", side_effect=mutate_source):
                with self.assertRaisesRegex(
                    atomic.RolledBackVerifiedError, "ROLLED_BACK_VERIFIED"
                ):
                    self.promote(pairs, results)
            self.assert_preimage(results, before)

    def test_foreign_identical_target_during_rollback_retains_backups(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            original = atomic._fingerprint_at
            replaced = False

            def replace_before_rollback(binding, name, label="file"):
                nonlocal replaced
                if label == "rollback target" and not replaced:
                    replaced = True
                    path = binding.path / name
                    snapshot = _snapshot(path)
                    assert snapshot is not None
                    raw, mode, mtime_ns = snapshot
                    foreign = path.with_name(".foreign-identical")
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, path)
                return original(binding, name, label)

            with patch.object(atomic, "_fingerprint_at", side_effect=replace_before_rollback):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results, fail_after=1)
            transactions = [path for path in results.iterdir() if path.name.startswith(".c61-transaction-")]
            self.assertEqual(len(transactions), 1)
            self.assertTrue(any(path.name.startswith("old-") for path in transactions[0].iterdir()))

    def test_foreign_backup_substitution_before_restore_is_retained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            original = atomic._fingerprint_at
            replaced = False

            def replace_backup(binding, name, label="file"):
                nonlocal replaced
                if label == "rollback backup" and not replaced:
                    replaced = True
                    path = binding.path / name
                    raw, mode, mtime_ns = _snapshot(path)  # type: ignore[misc]
                    foreign = path.with_name(".foreign-backup")
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, path)
                return original(binding, name, label)

            with patch.object(atomic, "_fingerprint_at", side_effect=replace_backup):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results, fail_after=1)
            self.assertTrue(replaced)
            transactions = [
                path for path in results.iterdir() if path.name.startswith(".c61-transaction-")
            ]
            self.assertEqual(len(transactions), 1)
            self.assertTrue((transactions[0] / "old-00").exists())

    def test_transaction_cleanup_validates_every_resident_before_deleting(self) -> None:
        for mutation in ("missing", "substitution", "extra", "dangling-directory"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                results = Path(temporary) / "results"
                results.mkdir()
                transaction = results / ".c61-transaction-unit"
                transaction.mkdir()
                staged = transaction / "new-00"
                _write(staged, b"owned\n", 0o600, 1_700_000_000_000_000_000)
                owned = atomic.fingerprint(staged, "fixture")
                entry = atomic.Entry(
                    source=staged,
                    target=results / "target",
                    staged=staged,
                    backup=transaction / "old-00",
                    source_fingerprint=owned,
                    preimage=None,
                    staged_fingerprint=owned,
                    staged_resident=True,
                )
                identity = (transaction.stat().st_dev, transaction.stat().st_ino)
                result_binding = atomic._bind_directory(results, "fixture results")
                transaction_binding = atomic._bind_child_directory(
                    result_binding,
                    transaction.name,
                    transaction,
                    "fixture transaction",
                    expected_identity=identity,
                )
                old_transaction = None
                if mutation == "missing":
                    staged.unlink()
                elif mutation == "substitution":
                    raw, mode, mtime_ns = _snapshot(staged)  # type: ignore[misc]
                    foreign = transaction / ".foreign"
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, staged)
                elif mutation == "extra":
                    (transaction / "foreign").write_bytes(b"foreign\n")
                else:
                    old_transaction = transaction.with_name(transaction.name + "-old")
                    transaction.rename(old_transaction)
                    transaction.symlink_to(results / "missing", target_is_directory=True)
                try:
                    with self.assertRaises((StrictDataError, atomic.DirectoryIdentityError)):
                        atomic._cleanup_transaction(
                            [entry], transaction_binding, result_binding
                        )
                finally:
                    atomic._close_directory_binding(transaction_binding)
                    atomic._close_directory_binding(result_binding)
                evidence_root = old_transaction if old_transaction is not None else transaction
                if mutation != "missing":
                    self.assertTrue((evidence_root / "new-00").exists())

    def test_copy_uses_fd_utime_then_fsync_and_short_lock_write_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "destination"
            _write(source, b"copy\n", 0o640, 1_700_000_000_000_000_123)
            expected = atomic.fingerprint(source, "fixture source")
            original_utime = atomic.os.utime
            original_fsync = atomic.os.fsync
            events: list[str] = []

            def tracked_utime(path_or_fd, *args, **kwargs):
                self.assertIs(type(path_or_fd), int)
                events.append("fd-utime")
                return original_utime(path_or_fd, *args, **kwargs)

            def tracked_fsync(descriptor):
                events.append("fsync")
                return original_fsync(descriptor)

            with (
                patch.object(atomic.os, "utime", side_effect=tracked_utime),
                patch.object(atomic.os, "fsync", side_effect=tracked_fsync),
            ):
                copied = atomic._copy_stable(source, destination, expected)
            self.assertEqual(copied.restored_fields(), expected.restored_fields())
            self.assertLess(events.index("fd-utime"), len(events) - 1)
            self.assertIn("fsync", events[events.index("fd-utime") + 1 :])

        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary)
            binding = atomic._bind_directory(results, "fixture results")
            try:
                with patch.object(atomic.os, "write", return_value=0):
                    with self.assertRaisesRegex(StrictDataError, "short"):
                        atomic.acquire_lock(binding)
            finally:
                atomic._close_directory_binding(binding)
            self.assertFalse((results / atomic.LOCK_NAME).exists())

    def test_stage_cleanup_rejects_replacement_and_extension_is_exact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "results"
            results.mkdir()
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            for name in atomic.EXPECTED_TARGET_NAMES[:-1]:
                (stage / name).write_bytes((name + "\n").encode())
            metadata = stage.stat()
            prior = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            (stage / atomic.EXPECTED_TARGET_NAMES[-1]).write_bytes(b"manifest\n")
            current = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            atomic.verify_stage_extension(prior, current)
            victim = stage / atomic.EXPECTED_TARGET_NAMES[0]
            raw, mode, mtime_ns = _snapshot(victim)  # type: ignore[misc]
            foreign = stage / ".foreign"
            _write(foreign, raw, mode, mtime_ns)
            os.replace(foreign, victim)
            with self.assertRaises(StrictDataError):
                atomic.cleanup_active_stage(results, stage, expected_snapshot=current)
            self.assertTrue(victim.exists())

        with tempfile.TemporaryDirectory() as temporary:
            results, stage, pairs, before = self.make_layout(Path(temporary), "absent")
            metadata = stage.stat()
            snapshot = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            victim = pairs[0][0]
            raw, mode, mtime_ns = _snapshot(victim)  # type: ignore[misc]
            foreign = stage / ".foreign"
            _write(foreign, raw, mode, mtime_ns)
            os.replace(foreign, victim)
            with self.assertRaisesRegex(StrictDataError, "final owned stage snapshot"):
                atomic.promote(
                    pairs,
                    results,
                    expected_stage_snapshot=snapshot,
                )
            self.assert_preimage(results, before)

    def test_foreign_lock_replacement_is_retained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary)
            binding = atomic._bind_directory(results, "fixture results")
            try:
                lock = atomic.acquire_lock(binding)
                held = results / ".held-original-lock"
                lock.path.rename(held)
                lock.path.write_bytes(b"foreign\n")
                with self.assertRaisesRegex(StrictDataError, "foreign lock retained"):
                    atomic.release_lock(lock, binding)
                self.assertEqual(lock.path.read_bytes(), b"foreign\n")
                lock.path.unlink()
                held.unlink()
            finally:
                atomic._close_directory_binding(binding)

    def test_optimized_python_and_environment_rejected(self) -> None:
        source = (
            "import pathlib,sys;sys.path.insert(0," + repr(str(CODE)) + ");"
            "from c61_exact import reject_optimized_python;reject_optimized_python()"
        )
        for command, environment in (
            ([sys.executable, "-O", "-B", "-c", source], {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}),
            ([sys.executable, "-B", "-c", source], {**os.environ, "PYTHONOPTIMIZE": "1", "PYTHONDONTWRITEBYTECODE": "1"}),
        ):
            completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(b"optimized Python", completed.stderr)


class ManifestHostileTests(unittest.TestCase):
    def make_project(self, root: Path) -> tuple[Path, Path]:
        code = root / "code"
        results = root / "results"
        code.mkdir()
        results.mkdir()
        for name in manifest.CODE_NAMES:
            (code / name).write_bytes((name + "\n").encode())
        for name in manifest.PROSE_NAMES + manifest.PROMOTED_NAMES:
            (results / name).write_bytes((name + "\n").encode())
        return code, results

    def patched(self, root: Path, code: Path, results: Path):
        return (
            patch.object(manifest, "PROJECT", root),
            patch.object(manifest, "CODE", code),
            patch.object(manifest, "RESULTS", results),
            patch.object(manifest, "DEFAULT_MANIFEST", results / manifest.PROMOTED_NAMES[-1]),
        )

    def test_stage_name_requires_exact_eight_alphanumeric_suffix(self) -> None:
        hostile_names = (
            ".c61-stage-ABC1234",
            ".c61-stage-ABCDEFGHI",
            ".c61-stage-ABC!2345",
        )
        for name in hostile_names:
            with self.subTest(layer="atomic", name=name), tempfile.TemporaryDirectory() as temporary:
                results = Path(temporary) / "results"
                results.mkdir()
                stage = results / name
                stage.mkdir()
                metadata = stage.stat()
                with self.assertRaises(StrictDataError):
                    atomic.stage_snapshot(
                        results,
                        stage,
                        expected_device=metadata.st_dev,
                        expected_inode=metadata.st_ino,
                    )

            with self.subTest(layer="manifest", name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                code, results = self.make_project(root)
                stage = results / name
                stage.mkdir()
                p1, p2, p3, p4 = self.patched(root, code, results)
                with p1, p2, p3, p4, self.assertRaises(StrictDataError):
                    manifest.artifact_paths(stage)

    def test_unknown_file_directory_symlink_and_fifo_rejected(self) -> None:
        for location in ("code", "results"):
            for kind in ("file", "directory", "symlink", "fifo"):
                with self.subTest(
                    location=location, kind=kind
                ), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    code, results = self.make_project(root)
                    hostile = (code if location == "code" else results) / "hostile"
                    if kind == "file":
                        hostile.write_bytes(b"x")
                    elif kind == "directory":
                        hostile.mkdir()
                    elif kind == "symlink":
                        hostile.symlink_to(results / "RESULTS.md")
                    else:
                        os.mkfifo(hostile)
                    p1, p2, p3, p4 = self.patched(root, code, results)
                    with p1, p2, p3, p4, self.assertRaises(StrictDataError):
                        manifest.artifact_paths()

    def test_out_of_scope_hardlink_to_code_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            os.link(code / "README.md", root / "outside-alias-to-code")
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                self.assertRaisesRegex(StrictDataError, "hardlink"),
            ):
                manifest.artifact_paths()

    def test_out_of_scope_hardlink_to_result_rejected(self) -> None:
        for name in (
            "RESULTS.md",
            "c61_group_evidence.json",
            "scoped_hash_manifest.json",
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                code, results = self.make_project(root)
                os.link(results / name, root / f"outside-alias-to-{name}")
                p1, p2, p3, p4 = self.patched(root, code, results)
                with (
                    p1,
                    p2,
                    p3,
                    p4,
                    self.assertRaisesRegex(StrictDataError, "hardlink"),
                ):
                    manifest.artifact_paths()

    def test_stage_promoted_hardlink_and_verified_manifest_hardlink_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            os.link(
                stage / "c61_group_evidence.json",
                root / "outside-alias-to-stage-input",
            )
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                self.assertRaisesRegex(StrictDataError, "hardlink"),
            ):
                manifest.artifact_paths(stage)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            os.link(
                results / "scoped_hash_manifest.json",
                root / "outside-alias-to-verified-manifest",
            )
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                self.assertRaisesRegex(StrictDataError, "link-count-one"),
            ):
                manifest.verify_manifest(results / "scoped_hash_manifest.json")

    def test_write_without_stage_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            p1, p2, p3, p4 = self.patched(root, code, results)
            argv = ["c61_hash_manifest.py", "--write", "--manifest", str(results / "scoped_hash_manifest.json")]
            with p1, p2, p3, p4, patch.object(sys, "argv", argv), self.assertRaises(StrictDataError):
                manifest.main()

    def test_stage_inode_swap_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            # A refresh may have any fixed live targets, but its one active
            # stage must supply all five nonmanifest promoted inputs.
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            original = manifest._stage_sources

            def swap(active):
                value = original(active)
                old = active.with_name(active.name + "-old")
                active.rename(old)
                active.mkdir()
                return value

            p1, p2, p3, p4 = self.patched(root, code, results)
            with p1, p2, p3, p4, patch.object(manifest, "_stage_sources", side_effect=swap), self.assertRaises(StrictDataError):
                manifest.artifact_paths(stage)

    def test_manifest_write_rejects_stage_swap_after_byte_construction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            stage = results / ".c61-stage-A1b2C3d4"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            original = manifest.manifest_bytes

            def swap_after_bytes(active, **kwargs):
                raw = original(active, **kwargs)
                old = active.with_name(active.name + "-old")
                active.rename(old)
                active.mkdir()
                return raw

            argv = [
                "c61_hash_manifest.py",
                "--write",
                "--stage-dir",
                str(stage),
                "--manifest",
                str(stage / manifest.PROMOTED_NAMES[-1]),
            ]
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                patch.object(manifest, "manifest_bytes", side_effect=swap_after_bytes),
                patch.object(sys, "argv", argv),
                self.assertRaises(StrictDataError),
            ):
                manifest.main()
            self.assertFalse((stage / manifest.PROMOTED_NAMES[-1]).exists())

    def test_manifest_result_parent_binding_rejects_rename_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            held_results = root / "results-held"
            foreign = root / "foreign-results"
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            original = manifest.artifact_paths

            def swap_after_inventory(stage=None, **kwargs):
                paths = original(stage, **kwargs)
                results.rename(held_results)
                results.symlink_to(foreign, target_is_directory=True)
                return paths

            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                patch.object(
                    manifest, "artifact_paths", side_effect=swap_after_inventory
                ),
                self.assertRaises(atomic.DirectoryIdentityError),
            ):
                manifest.manifest_object()
            self.assertTrue(results.is_symlink())
            self.assertEqual(results.resolve(strict=True), foreign)
            self.assertEqual({path.name for path in foreign.iterdir()}, {"sentinel"})
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )
            for name in manifest.PROSE_NAMES + manifest.PROMOTED_NAMES:
                self.assertEqual(
                    (held_results / name).read_bytes(), (name + "\n").encode()
                )

    def test_runner_privileged_bootstrap_ignores_and_rejects_BASH_ENV(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            marker = root / "injected"
            payload = root / "bash-env"
            payload.write_text(f"/usr/bin/touch {marker}\n", encoding="utf-8")
            clean_base = dict(os.environ)
            for name in (
                "LD_PRELOAD",
                "LD_LIBRARY_PATH",
                "BASH_ENV",
                "ENV",
                "PYTHONOPTIMIZE",
                "PYTHONPATH",
                "PYTHONHOME",
                "PYTHONSAFEPATH",
                TEST_EVIDENCE_ENV,
            ):
                clean_base.pop(name, None)
            environment = {
                **clean_base,
                "BASH_ENV": str(payload),
                "PATH": str(root),
                "PYTHONDONTWRITEBYTECODE": "1",
            }
            self.assertEqual(
                (CODE / "run_all.sh").read_bytes().splitlines()[0],
                b"#!/usr/bin/bash -p",
            )
            completed = subprocess.run(
                [str(CODE / "run_all.sh")],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=environment,
                cwd="/",
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn(b"BASH_ENV must be completely unset", completed.stderr)
            self.assertFalse(marker.exists())

            injected_evidence_environment = {
                **clean_base,
                TEST_EVIDENCE_ENV: str(root / "hostile-stage"),
                "PYTHONDONTWRITEBYTECODE": "1",
            }
            injected_completed = subprocess.run(
                [str(CODE / "run_all.sh")],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=injected_evidence_environment,
                cwd="/",
            )
            self.assertEqual(injected_completed.returncode, 2)
            self.assertIn(
                b"C61_TEST_EVIDENCE_DIR must be completely unset",
                injected_completed.stderr,
            )

            loader_environment = {
                **clean_base,
                "LD_LIBRARY_PATH": str(root),
                "PYTHONDONTWRITEBYTECODE": "1",
            }
            loader_completed = subprocess.run(
                [str(CODE / "run_all.sh")],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=loader_environment,
                cwd="/",
            )
            self.assertEqual(loader_completed.returncode, 2)
            self.assertIn(
                b"unsafe parent environment already reached the dynamic loader",
                loader_completed.stderr,
            )

    def test_runner_fd_relative_stage_creation_survives_parent_symlink_aba(self) -> None:
        runner_source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        self.assertIn(
            'mktemp -d "/proc/self/fd/$RESULTS_FD/.c61-stage-XXXXXXXX"',
            runner_source,
        )
        self.assertNotIn(
            'mktemp -d "$RESULTS_DIR/.c61-stage-XXXXXXXX"', runner_source
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            results = root / "results"
            held = root / "results-held"
            foreign = root / "foreign-results"
            results.mkdir()
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            probe = r'''
set -euo pipefail
RESULTS_DIR="$1"
HELD_RESULTS="$2"
FOREIGN_RESULTS="$3"
exec {RESULTS_FD}<"$RESULTS_DIR"
/usr/bin/mv -- "$RESULTS_DIR" "$HELD_RESULTS"
/usr/bin/ln -s -- "$FOREIGN_RESULTS" "$RESULTS_DIR"
STAGE_FD_PATH="$(/usr/bin/mktemp -d "/proc/self/fd/$RESULTS_FD/.c61-stage-XXXXXXXX")"
STAGE_BASENAME="${STAGE_FD_PATH##*/}"
/usr/bin/rm -- "$RESULTS_DIR"
/usr/bin/mv -- "$HELD_RESULTS" "$RESULTS_DIR"
/usr/bin/printf '%s\n' "$STAGE_BASENAME"
'''
            completed = subprocess.run(
                ["/usr/bin/bash", "-p", "-c", probe, "_", str(results), str(held), str(foreign)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                env={"PATH": "/usr/bin:/bin"},
                cwd="/",
            )
            stage_name = completed.stdout.decode("ascii").strip()
            self.assertRegex(stage_name, r"^\.c61-stage-[A-Za-z0-9]{8}$")
            self.assertTrue((results / stage_name).is_dir())
            self.assertEqual({path.name for path in foreign.iterdir()}, {"sentinel"})
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    def test_missing_backends_fail_closed(self) -> None:
        missing = Path("/definitely/missing/hcs-c61-backend")
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(missing)
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(missing)
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.gap_preflight(missing)


if __name__ == "__main__":
    if sys.flags.optimize or "PYTHONOPTIMIZE" in os.environ:
        raise SystemExit("optimized Python is forbidden")
    unittest.main(verbosity=2)
