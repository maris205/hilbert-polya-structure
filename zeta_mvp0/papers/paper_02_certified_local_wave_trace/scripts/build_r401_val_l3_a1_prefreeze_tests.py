#!/usr/bin/env python3
"""Build and validate the non-licensing L3-A1 role-11 test record.

This module deliberately contains no scientific evaluator dispatch.  A pure
test helper exercises the exact schema using caller-owned fixtures, but no
authority-bearing CLI accepts injected command evidence.  Capture and
canonical publication remain fail-closed in this implementation increment.
"""

from __future__ import annotations

import argparse
import ctypes
from datetime import datetime, timezone
import errno
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import selectors
import signal
import stat
import subprocess
import sys
import threading
import time
from typing import Any, Mapping, NamedTuple, Sequence


ROOT = Path(__file__).absolute().parents[1]
SCRIPT = Path(__file__).absolute()
SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-A1-PREFREEZE-TESTS"
ARTIFACT_ROLE = "PREFREEZE_TEST_RECORD"
ARTIFACT_STATUS = "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW"
AUTHORITY = "PREFREEZE_TEST_EVIDENCE_ONLY"
SERIALIZER = "CJ_COMPACT_V1"
ORIGIN_URL = "git@github.com:maris205/hilbert-polya-structure.git"
MAX_STDOUT_BYTES = 1024 * 1024
MAX_STDERR_BYTES = 1024 * 1024
MAX_CANDIDATE_BYTES = 4 * 1024 * 1024
MAX_ROLE_BYTES = 128 * 1024 * 1024
COMMAND_TIMEOUT_SECONDS = 600
COMMAND_TERM_GRACE_SECONDS = 2
COMMAND_PIPE_CLOSE_GRACE_SECONDS = 1
EXPECTED_TEST_PASSED: dict[str, int] | None = {
    "prefreeze_focused": 100,
    "l3_a1_modules": 621,
    "paper02_full": 1016,
}
PREFREEZE_VERIFY_STATUS = "PASS_PREFREEZE_TEST_RECORD_VERIFY_ONLY"
PUBLICATION_AUTHORITY = "PREFREEZE_TEST_PRODUCER_PUBLICATION_ONLY"
PUBLICATION_STATUS = "PUBLISHED_WRITE_ONCE_NON_LICENSING"
PUBLICATION_METHOD = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
PUBLICATION_LOCK_FLAGS = fcntl.LOCK_EX | fcntl.LOCK_NB
PUBLICATION_STAGE_PREFIX = ".R401_VAL_L3_A1_PREFREEZE_TESTS.json.stage."
PUBLICATION_HOOK_PHASES = frozenset({
    "AFTER_STAGE_WRITE",
    "AFTER_STAGE_FILE_FSYNC",
    "AFTER_STAGING_PARENT_FSYNC",
    "BEFORE_TERMINAL_REPLAY",
    "BEFORE_RENAME",
    "AFTER_RENAME",
    "AFTER_DESTINATION_FSYNC",
    "AFTER_PUBLICATION_PARENT_FSYNC",
    "AFTER_POSTPUBLICATION_REPLAY",
})
CAPTURE_HOOK_PHASES = frozenset({"BEFORE_FINAL_CANDIDATE_REPLAY"})
PUBLICATION_RECEIPT_KEYS = frozenset({
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "candidate_path", "canonical_path",
    "prefreeze_tests_sha256", "size_bytes", "mode", "nlink",
    "serializer", "publication_method", "independent_verification_status",
    "independent_verification_performed", "independent_verifier_path",
    "independent_verifier_sha256", "promotion_authorized",
    "scientific_licensing_enabled", "production_authorized",
    "scientific_dispatch_performed", "component_status", "milestone_status",
    "theorem_status", "final_status",
})

MACHINE_SHA256 = "0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e"
MACHINE_SIZE_BYTES = 54526
MACHINE_PUBLICATION_COMMIT = "5086e33c7c66f33785338e90b340347e086d9941"
ROLE13_SHA256 = "d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30"
ROLE13_SIZE_BYTES = 8820
ROLE13_PUBLICATION_COMMIT = "be2a732625d9cab97879539873a756e1eabd366d"

MACHINE_VERIFY_STATUS = "PASS_MACHINE_FREEZE_VERIFY_ONLY"
ROLE13_VERIFY_STATUS = "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
VERIFY_AUTHORITY = "NON_AUTHORITATIVE_VERIFY_ONLY"
SECOND_REBUILD_STATUS = "PASS_SECOND_FRESH_REBUILD"
SECOND_REBUILD_AUTHORITY = "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY"

CANONICAL_RELATIVE = PurePosixPath(
    "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json"
)
ROLE12_RELATIVE = PurePosixPath(
    "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md"
)
ROLE54_RELATIVE = PurePosixPath(
    "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
)
CANONICAL_RESULT_ROOT = PurePosixPath("results/r401_val_l3_all_slabs")
CANONICAL_OPERATIONAL_ROOT = PurePosixPath(
    "results/r401_val_l3_all_slabs.operational"
)

CLAIM_BOUNDARY = (
    "pre-freeze engineering test evidence only; no held-out or all-slab L3 "
    "result was read and no scientific evaluator was dispatched; no L3-A1 "
    "component, milestone, theorem, final, global tube-routing, trace-formula, "
    "Hilbert-Polya, zeta-zero, RH, or implication-toward-RH claim"
)

COVERED_GATES = (
    "EXACT_51_ROLE_ORDER_AND_SAME_BYTE_SNAPSHOTS",
    "CANONICAL_ROLE10_AND_ROLE13_REPLAY",
    "SEVEN_FIXED_COMMAND_IDENTITIES",
    "BOUNDED_RAW_UTF8_TRANSCRIPT_REHASH",
    "PYTEST_SUMMARY_REPARSE_AND_ZERO_NONPASS_COUNTS",
    "CLEAN_REPOSITORY_AND_FIXED_ENVIRONMENT",
    "PROCESS_GROUP_TIMEOUT_AND_DESCENDANT_CLEANUP",
    "SECOND_REBUILD_NO_OVERWRITE_BYTE_EQUALITY",
    "STRICT_SCHEMA_TYPES_PATHS_LINKS_AND_TOCTOU_REPLAY",
    "INDEPENDENT_CHECKER_SOURCE_SEPARATION",
    "WRITE_ONCE_FIXED_DESTINATION_NOREPLACE_PUBLICATION",
)

TOP_LEVEL_KEYS = frozenset({
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "recorded_at_utc", "scientific_licensing_enabled",
    "production_authorized", "scientific_dispatch_performed",
    "held_out_policy", "repository_snapshot", "prerequisite_bindings",
    "pre_review_input_roles", "evidence_tool_bindings", "command_results",
    "test_totals", "covered_gates", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
})
HELD_OUT_POLICY_KEYS = frozenset({
    "held_out_l3_scientific_outputs_read", "held_out_l3_evaluator_dispatched",
    "scientific_evaluator_dispatch_count", "new_archive_scope",
    "s0_archive_access", "canonical_result_created",
})
REPOSITORY_SNAPSHOT_KEYS = frozenset({
    "authority_root", "branch", "capture_commit_oid", "capture_tree_oid",
    "origin_url", "origin_main_oid", "live_remote_main_oid",
    "head_equals_origin_main", "head_equals_live_remote_main", "ahead",
    "behind", "worktree_clean_before", "worktree_clean_after",
})
PREREQUISITE_BINDING_KEYS = frozenset({
    "machine_role10", "s0_compatibility_role13",
    "second_fresh_rebuild_replay", "canonical_absence",
})
CANONICAL_ABSENCE_KEYS = frozenset({
    "prefreeze_review_role12_exists", "main_freeze_role54_exists",
    "canonical_result_root_exists", "canonical_operational_root_exists",
})
ROLE_ENTRY_KEYS = frozenset({
    "role", "path", "sha256", "size_bytes", "mode", "nlink",
})
FILE_BINDING_KEYS = frozenset({"path", "sha256", "size_bytes", "mode", "nlink"})
EVIDENCE_TOOL_BINDING_KEYS = frozenset({
    "producer", "independent_checker", "focused_test",
})
MACHINE_BINDING_KEYS = frozenset({
    "role", "path", "sha256", "size_bytes", "mode", "nlink",
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verifier_path", "verifier_sha256", "verify_receipt",
    "promotion_authorized",
})
ROLE13_BINDING_KEYS = frozenset({
    "role", "path", "sha256", "size_bytes", "mode", "nlink",
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verify_receipt", "promotion_authorized",
})
VERIFY_RECEIPT_KEYS = frozenset({
    "verification_status", "authority", "candidate_sha256", "size_bytes",
    "promotion_authorized",
})
SECOND_REBUILD_REPLAY_KEYS = frozenset({
    "command_result_name", "command_result_sha256", "semantic_receipt",
})
SECOND_REBUILD_RECEIPT_KEYS = frozenset({
    "verification_status", "authority", "source_path", "source_sha256",
    "persistent_binary_path", "persistent_before_sha256",
    "persistent_after_sha256", "persistent_before_device_id",
    "persistent_before_inode", "persistent_after_device_id",
    "persistent_after_inode", "persistent_identity_unchanged",
    "persistent_overwrite_performed", "staging_output_sha256",
    "staging_output_size_bytes", "staging_output_mode",
    "staging_output_removed", "byte_for_byte_equal",
    "scientific_evaluator_dispatched",
})
COMMAND_RESULT_KEYS = frozenset({
    "name", "kind", "argv", "cwd", "environment", "return_code",
    "started_at_utc", "wall_duration_ms", "stdout_utf8", "stdout_sha256",
    "stdout_size_bytes", "stderr_utf8", "stderr_sha256",
    "stderr_size_bytes", "pytest_counts", "semantic_receipt",
})
PYTEST_COUNT_KEYS = frozenset({"passed", "failed", "skipped", "xfailed", "xpassed"})
TEST_TOTAL_KEYS = frozenset({
    "passed", "failed", "skipped", "xfailed", "xpassed", "wall_duration_ms",
})
TEST_TOTALS_KEYS = frozenset({"prefreeze_focused", "l3_a1_modules", "paper02_full"})

PRE_REVIEW_INPUT_ROLES: tuple[tuple[str, str], ...] = (
    ("a416_derivation", "research/route_a_wave_trace/A416_PHASE_FLOWBOX_DERIVATION.md"),
    ("s0_protocol", "research/route_a_wave_trace/R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md"),
    ("s0_report", "research/route_a_wave_trace/A416_REPRESENTATIVE_PHASE_TUBE_SMOKE.md"),
    ("prefreeze_design", "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md"),
    ("implementation_design_review", "research/route_a_wave_trace/R401_VAL_L3_A1_DESIGN_REVIEW.md"),
    ("formal_protocol", "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"),
    ("scheduler_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"),
    ("checker_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"),
    ("release_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"),
    ("machine_freeze", "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"),
    ("s0_compatibility", "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"),
    ("capd_dependency", "validated/CAPD_DEPENDENCY.md"),
    ("static_evaluator", "scripts/evaluate_r401_val_l3_a1_static_cell.py"),
    ("branch_evaluator_source", "validated/capd_r401_phase_branch_tube_mp_a1.cpp"),
    ("branch_evaluator_binary", "validated/bin/capd_r401_phase_branch_tube_mp_a1"),
    ("branch_runtime", "scripts/r401_val_l3_a1_branch_runtime.py"),
    ("scheduler", "scripts/run_r401_val_l3_a1_all_slabs.py"),
    ("static_checker_source", "scripts/check_r401_val_l3_a1_static_independent.py"),
    ("branch_checker_source", "scripts/check_r401_val_l3_a1_branch_independent.py"),
    ("composite_checker_source", "scripts/check_r401_val_l3_a1_composite_independent.py"),
    ("s0_adapter", "scripts/replay_r401_val_l3_s0_through_a1_checkers.py"),
    ("release_builder", "scripts/build_r401_val_l3_a1_release_provenance.py"),
    ("test_static_evaluator", "tests/test_r401_val_l3_a1_static_cell.py"),
    ("test_static_scheduler", "tests/test_r401_val_l3_a1_static_scheduler.py"),
    ("test_static_checker", "tests/test_r401_val_l3_a1_static_checker.py"),
    ("test_branch_scheduler", "tests/test_r401_val_l3_a1_branch_scheduler.py"),
    ("test_branch_checker", "tests/test_r401_val_l3_a1_branch_checker.py"),
    ("test_s0_compatibility", "tests/test_r401_val_l3_a1_s0_compatibility.py"),
    ("test_composite", "tests/test_r401_val_l3_a1_composite_contract.py"),
    ("test_adversarial", "tests/test_r401_val_l3_a1_adversarial_e2e.py"),
    ("test_release", "tests/test_r401_val_l3_a1_release_provenance.py"),
    ("l1_final_plan", "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"),
    ("l1_summary", "results/r401_val_l1_branch/summary.json"),
    ("l1_manifest", "results/r401_val_l1_branch/manifest.json"),
    ("l1_checker", "results/r401_val_l1_branch/independent_checker.json"),
    ("l1_postcheck", "results/r401_val_l1_branch/POSTCHECK_STATUS.json"),
    ("l1_release", "results/r401_val_l1_branch/RELEASE_PROVENANCE.json"),
    ("a415_summary", "results/r401_val_l2_all_slabs/aggregate_summary.json"),
    ("a415_manifest", "results/r401_val_l2_all_slabs/aggregate_manifest.json"),
    ("a415_checker", "results/r401_val_l2_all_slabs/independent_checker.json"),
    ("a415_postcheck", "results/r401_val_l2_all_slabs/POSTCHECK_STATUS.json"),
    ("a415_release", "results/r401_val_l2_all_slabs/RELEASE_PROVENANCE.json"),
    ("s0_static_summary", "results/r401_val_l3_phase_tube_smoke/summary.json"),
    ("s0_static_manifest", "results/r401_val_l3_phase_tube_smoke/manifest.json"),
    ("s0_static_checker", "results/r401_val_l3_phase_tube_smoke/independent_checker.json"),
    ("s0_branch_summary", "results/r401_val_l3_branch_tube_smoke/summary.json"),
    ("s0_branch_manifest", "results/r401_val_l3_branch_tube_smoke/manifest.json"),
    ("s0_branch_checker", "results/r401_val_l3_branch_tube_smoke/independent_checker.json"),
    ("s0_composite_summary", "results/r401_val_l3_s0_composite/summary.json"),
    ("s0_composite_manifest", "results/r401_val_l3_s0_composite/manifest.json"),
    ("s0_composite_checker", "results/r401_val_l3_s0_composite/independent_checker.json"),
)

COMMAND_SPECS: tuple[tuple[str, str], ...] = (
    ("role24_machine_verify", "VERIFY_MACHINE_FREEZE"),
    ("role13_compatibility_verify", "VERIFY_S0_COMPATIBILITY"),
    ("prefreeze_focused_pytest", "PYTEST_FOCUSED"),
    ("l3_a1_modules_pytest", "PYTEST_L3_A1"),
    ("paper02_full_pytest", "PYTEST_PAPER02"),
    ("git_diff_check", "GIT_DIFF_CHECK"),
    ("second_fresh_rebuild", "SECOND_FRESH_REBUILD"),
)
PYTHON = "/root/miniconda3/bin/python3"
CLEAN_ENVIRONMENT = {
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
}
ROLE24_SCRIPT = ROOT / "scripts/build_r401_val_l3_a1_release_provenance.py"
ROLE11_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py"
ROLE11_TEST = ROOT / "tests/test_r401_val_l3_a1_prefreeze_tests.py"
MACHINE_CANONICAL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
ROLE13_CANONICAL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
FIXED_COMMAND_ARGV: dict[str, tuple[str, ...]] = {
    "role24_machine_verify": (
        PYTHON, os.fspath(ROLE24_SCRIPT), "--verify-machine-freeze",
        os.fspath(MACHINE_CANONICAL),
    ),
    "role13_compatibility_verify": (
        PYTHON, os.fspath(ROLE11_CHECKER), "--verify-s0-compatibility",
        os.fspath(ROLE13_CANONICAL),
    ),
    "prefreeze_focused_pytest": (
        PYTHON, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no",
        "tests/test_r401_val_l3_a1_prefreeze_tests.py",
    ),
    "l3_a1_modules_pytest": (
        PYTHON, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no",
        "tests/test_r401_val_l3_a1_static_cell.py",
        "tests/test_r401_val_l3_a1_static_scheduler.py",
        "tests/test_r401_val_l3_a1_static_checker.py",
        "tests/test_r401_val_l3_a1_branch_scheduler.py",
        "tests/test_r401_val_l3_a1_branch_checker.py",
        "tests/test_r401_val_l3_a1_s0_compatibility.py",
        "tests/test_r401_val_l3_a1_composite_contract.py",
        "tests/test_r401_val_l3_a1_adversarial_e2e.py",
        "tests/test_r401_val_l3_a1_release_provenance.py",
        "tests/test_r401_val_l3_a1_prefreeze_tests.py",
    ),
    "paper02_full_pytest": (
        PYTHON, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no",
    ),
    "git_diff_check": ("/usr/bin/git", "diff", "--check", "HEAD", "--"),
}
REBUILD_COMMAND_ARGV_PREFIX = (
    PYTHON, os.fspath(SCRIPT), "--second-fresh-rebuild-only", "--output",
)
COMPILER_ARGV_PREFIX = (
    "/usr/bin/g++", "-Wall", "-Wextra", "-Wpedantic", "-Werror",
    os.fspath(ROOT / "validated/capd_r401_phase_branch_tube_mp_a1.cpp"),
    "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
    "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
    "-DFILIB_HAVE_SSE",
    "-I/root/autodl-tmp/zeta/dependencies/capd-r401-a1/capdDynSys/include",
    "-I/root/autodl-tmp/zeta/dependencies/capd-r401-a1/capdAlg/include",
    "-I/root/autodl-tmp/zeta/dependencies/capd-r401-a1/capdAux/include",
    "-I/root/autodl-tmp/zeta/dependencies/capd-r401-a1/capdExt/include",
    "-I/root/autodl-tmp/zeta/dependencies/capd-r401-a1/capdExt/filibsrc",
    "-L/root/autodl-tmp/zeta/dependencies/capd-r401-a1/build-mp",
    "-L/root/autodl-tmp/zeta/dependencies/capd-r401-a1/build-mp/capdExt/filibsrc",
    "-lcapd", "-lfilib", "-lmpfr", "-lgmp", "-o",
)
REBUILD_OUTPUT_BASENAME = "capd_r401_phase_branch_tube_mp_a1"
PYTEST_RESULT_TOTAL_NAMES = {
    "prefreeze_focused_pytest": "prefreeze_focused",
    "l3_a1_modules_pytest": "l3_a1_modules",
    "paper02_full_pytest": "paper02_full",
}


class PrefreezeEvidenceError(RuntimeError):
    """A strict role-11 evidence-contract violation."""


class SyntheticPrefreezePublicationCrash(RuntimeError):
    """Test-only marker for a frozen publication crash boundary."""


class FileImage(NamedTuple):
    raw: bytes
    device_id: int
    inode: int
    mode: int
    nlink: int
    size_bytes: int
    mtime_ns: int
    ctime_ns: int

    @property
    def identity(self) -> tuple[int, int, int, int, int, int, int]:
        return (
            self.device_id, self.inode, self.mode, self.nlink,
            self.size_bytes, self.mtime_ns, self.ctime_ns,
        )


def _stat_identity(info: os.stat_result) -> tuple[int, int, int, int, int, int, int]:
    return (
        info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
        info.st_size, info.st_mtime_ns, info.st_ctime_ns,
    )


def _absolute_lexical(path: Path, context: str) -> Path:
    text = os.fspath(path)
    if "\x00" in text or not path.is_absolute() or os.path.normpath(text) != text:
        raise PrefreezeEvidenceError(f"{context}: canonical absolute path required")
    return path


def _directory_identity(info: os.stat_result) -> tuple[int, int, int, int]:
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink)


def _relative_directory_identity(
    info: os.stat_result,
) -> tuple[int, int, int, int, int]:
    return (*_directory_identity(info), info.st_ctime_ns)


def _open_absolute_directory(path: Path, context: str) -> tuple[int, list[tuple[int, int, int, int]]]:
    """Open every absolute directory component without following symlinks."""

    path = _absolute_lexical(path, context)
    descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    chain: list[tuple[int, int, int, int]] = []
    try:
        root_info = os.fstat(descriptor)
        chain.append(_directory_identity(root_info))
        for part in path.parts[1:]:
            next_descriptor = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=descriptor,
            )
            current = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            opened = os.fstat(next_descriptor)
            if (
                not stat.S_ISDIR(opened.st_mode)
                or (current.st_dev, current.st_ino) != (opened.st_dev, opened.st_ino)
            ):
                os.close(next_descriptor)
                raise PrefreezeEvidenceError(f"{context}: directory namespace mismatch")
            os.close(descriptor)
            descriptor = next_descriptor
            chain.append(_directory_identity(opened))
        return descriptor, chain
    except BaseException:
        os.close(descriptor)
        raise


def _replay_open_directory(
    path: Path, descriptor: int,
    chain: Sequence[tuple[int, int, int, int]], context: str,
) -> None:
    current = os.fstat(descriptor)
    if not stat.S_ISDIR(current.st_mode) or _directory_identity(current) != chain[-1]:
        raise PrefreezeEvidenceError(f"{context}: open directory changed")
    replay_fd, replay_chain = _open_absolute_directory(path, context)
    try:
        if list(chain) != replay_chain:
            raise PrefreezeEvidenceError(f"{context}: directory chain changed")
    finally:
        os.close(replay_fd)


def _replay_relative_directories(
    parts: Sequence[str], expected: Sequence[tuple[int, int, int, int, int]],
    context: str,
) -> None:
    descriptor, _root_chain = _open_absolute_directory(ROOT, "Paper02 authority root")
    try:
        if len(parts) != len(expected):
            raise PrefreezeEvidenceError(f"{context}: internal parent-chain mismatch")
        for part, signature in zip(parts, expected):
            next_fd = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
                | getattr(os, "O_CLOEXEC", 0),
                dir_fd=descriptor,
            )
            lexical = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            opened = os.fstat(next_fd)
            if (
                not stat.S_ISDIR(opened.st_mode)
                or _relative_directory_identity(lexical) != signature
                or _relative_directory_identity(opened) != signature
            ):
                os.close(next_fd)
                raise PrefreezeEvidenceError(f"{context}: relative directory chain changed")
            os.close(descriptor)
            descriptor = next_fd
    except OSError as error:
        raise PrefreezeEvidenceError(f"{context}: parent replay failed: {error}") from error
    finally:
        os.close(descriptor)


def secure_read_relative(
    relative: str, context: str, *, maximum_bytes: int = MAX_ROLE_BYTES,
) -> FileImage:
    """Read one ROOT-relative, regular, single-link file from a pinned inode."""

    relative = _relative_path(relative, context)
    parts = PurePosixPath(relative).parts
    root_fd, root_chain = _open_absolute_directory(ROOT, "Paper02 authority root")
    parent_fd = root_fd
    owned_parent = False
    file_fd: int | None = None
    relative_chain: list[tuple[int, int, int, int, int]] = []
    try:
        for part in parts[:-1]:
            lexical_before = os.stat(part, dir_fd=parent_fd, follow_symlinks=False)
            if not stat.S_ISDIR(lexical_before.st_mode):
                raise PrefreezeEvidenceError(f"{context}: non-directory parent")
            next_fd = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
                | getattr(os, "O_CLOEXEC", 0),
                dir_fd=parent_fd,
            )
            lexical = os.stat(part, dir_fd=parent_fd, follow_symlinks=False)
            opened = os.fstat(next_fd)
            if (
                not stat.S_ISDIR(opened.st_mode)
                or _relative_directory_identity(lexical_before)
                != _relative_directory_identity(opened)
                or _relative_directory_identity(lexical)
                != _relative_directory_identity(opened)
            ):
                os.close(next_fd)
                raise PrefreezeEvidenceError(f"{context}: parent directory mismatch")
            relative_chain.append(_relative_directory_identity(opened))
            if owned_parent:
                os.close(parent_fd)
            parent_fd = next_fd
            owned_parent = True
        lexical_preopen = os.stat(
            parts[-1], dir_fd=parent_fd, follow_symlinks=False
        )
        if (
            not stat.S_ISREG(lexical_preopen.st_mode)
            or lexical_preopen.st_nlink != 1
            or lexical_preopen.st_size < 1
            or lexical_preopen.st_size > maximum_bytes
        ):
            raise PrefreezeEvidenceError(
                f"{context}: pre-open regular single-link size contract mismatch"
            )
        file_fd = os.open(
            parts[-1],
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0),
            dir_fd=parent_fd,
        )
        before = os.fstat(file_fd)
        lexical_before = os.stat(parts[-1], dir_fd=parent_fd, follow_symlinks=False)
        if (
            not stat.S_ISREG(before.st_mode) or before.st_nlink != 1
            or before.st_size < 1 or before.st_size > maximum_bytes
            or _stat_identity(lexical_preopen) != _stat_identity(before)
            or _stat_identity(before) != _stat_identity(lexical_before)
        ):
            raise PrefreezeEvidenceError(f"{context}: regular single-link size contract mismatch")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(file_fd, min(1024 * 1024, maximum_bytes - total + 1))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total > maximum_bytes:
                raise PrefreezeEvidenceError(f"{context}: input cap exceeded")
        after = os.fstat(file_fd)
        lexical_after = os.stat(parts[-1], dir_fd=parent_fd, follow_symlinks=False)
        if (
            _stat_identity(before) != _stat_identity(after)
            or _stat_identity(after) != _stat_identity(lexical_after)
            or total != after.st_size
        ):
            raise PrefreezeEvidenceError(f"{context}: file changed during capture")
        _replay_open_directory(ROOT, root_fd, root_chain, "Paper02 authority root")
        _replay_relative_directories(parts[:-1], relative_chain, context)
        return FileImage(
            raw=b"".join(chunks), device_id=after.st_dev, inode=after.st_ino,
            mode=after.st_mode, nlink=after.st_nlink, size_bytes=after.st_size,
            mtime_ns=after.st_mtime_ns, ctime_ns=after.st_ctime_ns,
        )
    except OSError as error:
        raise PrefreezeEvidenceError(f"{context}: secure read failed: {error}") from error
    finally:
        if file_fd is not None:
            os.close(file_fd)
        if owned_parent:
            os.close(parent_fd)
        os.close(root_fd)


def role_binding(role: str, relative: str) -> dict[str, Any]:
    image = secure_read_relative(relative, f"role {role}")
    return {
        "role": role,
        "path": relative,
        "sha256": hashlib.sha256(image.raw).hexdigest(),
        "size_bytes": image.size_bytes,
        "mode": f"0{stat.S_IMODE(image.mode):03o}",
        "nlink": image.nlink,
    }


def capture_pre_review_input_roles() -> list[dict[str, Any]]:
    rows = [role_binding(role, relative) for role, relative in PRE_REVIEW_INPUT_ROLES]
    if len(rows) != 51:
        raise PrefreezeEvidenceError("internal pre-review role map is not exactly 51")
    return rows


def replay_pre_review_input_roles(expected: Sequence[Mapping[str, Any]]) -> None:
    if type(expected) is not list or len(expected) != 51:
        raise PrefreezeEvidenceError("terminal role replay requires exact 51-entry list")
    actual = capture_pre_review_input_roles()
    if not _exact_json_equal(actual, expected):
        raise PrefreezeEvidenceError("terminal pre-review input replay changed")


def capture_evidence_tool_bindings() -> dict[str, dict[str, Any]]:
    paths = {
        "producer": "scripts/build_r401_val_l3_a1_prefreeze_tests.py",
        "independent_checker": "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py",
        "focused_test": "tests/test_r401_val_l3_a1_prefreeze_tests.py",
    }
    result: dict[str, dict[str, Any]] = {}
    for name, relative in paths.items():
        row = role_binding(name, relative)
        result[name] = {key: row[key] for key in FILE_BINDING_KEYS}
    return result


def replay_evidence_tool_bindings(expected: Mapping[str, Any]) -> None:
    actual = capture_evidence_tool_bindings()
    if not _exact_json_equal(actual, expected):
        raise PrefreezeEvidenceError("terminal evidence-tool replay changed")


class BoundedCommand(NamedTuple):
    argv: tuple[str, ...]
    return_code: int
    stdout: bytes
    stderr: bytes
    wall_duration_ms: int


_SUBREAPER_LOCK = threading.RLock()


def _child_subreaper_state() -> bool:
    if not sys.platform.startswith("linux"):
        raise PrefreezeEvidenceError("bounded command subreaper requires Linux")
    libc = ctypes.CDLL(None, use_errno=True)
    prctl = getattr(libc, "prctl", None)
    if prctl is None:
        raise PrefreezeEvidenceError("prctl(PR_GET_CHILD_SUBREAPER) unavailable")
    prctl.restype = ctypes.c_int
    state = ctypes.c_int(-1)
    ctypes.set_errno(0)
    result = prctl(
        ctypes.c_int(37), ctypes.byref(state), ctypes.c_ulong(0),
        ctypes.c_ulong(0), ctypes.c_ulong(0),
    )
    if result != 0 or state.value not in (0, 1):
        raise PrefreezeEvidenceError(
            f"cannot read child-subreaper state (errno {ctypes.get_errno()})"
        )
    return bool(state.value)


def _set_child_subreaper(enabled: bool) -> None:
    if type(enabled) is not bool or not sys.platform.startswith("linux"):
        raise PrefreezeEvidenceError("invalid child-subreaper transition")
    libc = ctypes.CDLL(None, use_errno=True)
    prctl = getattr(libc, "prctl", None)
    if prctl is None:
        raise PrefreezeEvidenceError("prctl(PR_SET_CHILD_SUBREAPER) unavailable")
    prctl.restype = ctypes.c_int
    ctypes.set_errno(0)
    result = prctl(
        ctypes.c_int(36), ctypes.c_ulong(int(enabled)), ctypes.c_ulong(0),
        ctypes.c_ulong(0), ctypes.c_ulong(0),
    )
    if result != 0 or _child_subreaper_state() is not enabled:
        raise PrefreezeEvidenceError(
            f"cannot set child-subreaper state (errno {ctypes.get_errno()})"
        )


def _process_group_exists(process_group: int) -> bool:
    try:
        os.killpg(process_group, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _reap_process_group_children(process_group: int) -> None:
    """Reap adopted children in exactly one owned PGID, never process-wide."""

    while True:
        try:
            child, _status = os.waitpid(-process_group, os.WNOHANG)
        except ChildProcessError:
            return
        if child == 0:
            return


def _finish_process_group(process_group: int, *, deadline_seconds: float) -> None:
    deadline = time.monotonic() + deadline_seconds
    while True:
        _reap_process_group_children(process_group)
        if not _process_group_exists(process_group):
            return
        try:
            os.killpg(process_group, signal.SIGKILL)
        except ProcessLookupError:
            pass
        if time.monotonic() >= deadline:
            break
        time.sleep(0.005)
    _reap_process_group_children(process_group)
    if _process_group_exists(process_group):
        raise PrefreezeEvidenceError("owned process group survived SIGKILL/reap")


def _terminate_process_group(process: subprocess.Popen[bytes]) -> None:
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    deadline = time.monotonic() + COMMAND_TERM_GRACE_SECONDS
    while time.monotonic() < deadline:
        _reap_process_group_children(process.pid)
        if not _process_group_exists(process.pid):
            break
        time.sleep(0.02)
    _finish_process_group(
        process.pid, deadline_seconds=COMMAND_TERM_GRACE_SECONDS
    )
    if process.poll() is None:
        process.wait(timeout=COMMAND_TERM_GRACE_SECONDS)


def _run_bounded_command_with_subreaper(
    argv: Sequence[str], *, timeout_seconds: int = COMMAND_TIMEOUT_SECONDS,
    stdout_cap: int = MAX_STDOUT_BYTES, stderr_cap: int = MAX_STDERR_BYTES,
    environment: Mapping[str, str] = CLEAN_ENVIRONMENT,
) -> BoundedCommand:
    """Run one fixed argv with bounded streaming and a new process group."""

    if type(argv) not in (list, tuple) or not argv or any(
        type(item) is not str or not item or "\x00" in item for item in argv
    ):
        raise PrefreezeEvidenceError("bounded command requires exact argv strings")
    if type(environment) is not dict or any(
        type(key) is not str or type(value) is not str
        for key, value in environment.items()
    ):
        raise PrefreezeEvidenceError("bounded command requires exact string environment")
    started = time.monotonic_ns()
    try:
        process = subprocess.Popen(
            list(argv), cwd=ROOT, env=dict(environment), shell=False,
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, start_new_session=True,
            close_fds=True, umask=0o022,
        )
    except OSError as error:
        raise PrefreezeEvidenceError(f"command launch failed: {error}") from error
    assert process.stdout is not None and process.stderr is not None
    streams = {process.stdout.fileno(): ("stdout", process.stdout), process.stderr.fileno(): ("stderr", process.stderr)}
    for descriptor in streams:
        os.set_blocking(descriptor, False)
    buffers = {"stdout": bytearray(), "stderr": bytearray()}
    selector = selectors.DefaultSelector()
    for descriptor in streams:
        selector.register(descriptor, selectors.EVENT_READ)
    deadline = time.monotonic() + timeout_seconds
    exit_seen_at: float | None = None
    failure: str | None = None
    try:
        while selector.get_map():
            now = time.monotonic()
            if now >= deadline:
                failure = "command timeout"
                break
            if process.poll() is not None:
                if exit_seen_at is None:
                    exit_seen_at = now
                elif now - exit_seen_at > COMMAND_PIPE_CLOSE_GRACE_SECONDS:
                    failure = "command descendants retained output pipes"
                    break
            events = selector.select(min(0.05, max(0.0, deadline - now)))
            for key, _mask in events:
                descriptor = key.fd
                stream_name, _stream = streams[descriptor]
                try:
                    chunk = os.read(descriptor, 65536)
                except BlockingIOError:
                    continue
                if not chunk:
                    selector.unregister(descriptor)
                    continue
                buffers[stream_name].extend(chunk)
                cap = stdout_cap if stream_name == "stdout" else stderr_cap
                if len(buffers[stream_name]) > cap:
                    failure = f"command {stream_name} cap exceeded"
                    break
            if failure is not None:
                break
        if failure is not None:
            _terminate_process_group(process)
            raise PrefreezeEvidenceError(failure)
        return_code = process.wait(timeout=COMMAND_TERM_GRACE_SECONDS)
        _reap_process_group_children(process.pid)
        if _process_group_exists(process.pid):
            _finish_process_group(
                process.pid, deadline_seconds=COMMAND_TERM_GRACE_SECONDS
            )
            raise PrefreezeEvidenceError("command left a surviving process-group member")
        duration_ms = max(1, (time.monotonic_ns() - started + 999_999) // 1_000_000)
        return BoundedCommand(
            argv=tuple(argv), return_code=return_code,
            stdout=bytes(buffers["stdout"]), stderr=bytes(buffers["stderr"]),
            wall_duration_ms=duration_ms,
        )
    finally:
        selector.close()
        process.stdout.close()
        process.stderr.close()
        if process.poll() is None:
            _terminate_process_group(process)


def run_bounded_command(
    argv: Sequence[str], *, timeout_seconds: int = COMMAND_TIMEOUT_SECONDS,
    stdout_cap: int = MAX_STDOUT_BYTES, stderr_cap: int = MAX_STDERR_BYTES,
    environment: Mapping[str, str] = CLEAN_ENVIRONMENT,
) -> BoundedCommand:
    """Run with owned-PGID cleanup and exact restoration of subreaper state."""

    with _SUBREAPER_LOCK:
        original_state = _child_subreaper_state()
        changed = not original_state
        if changed:
            _set_child_subreaper(True)
        try:
            return _run_bounded_command_with_subreaper(
                argv, timeout_seconds=timeout_seconds,
                stdout_cap=stdout_cap, stderr_cap=stderr_cap,
                environment=environment,
            )
        finally:
            if changed:
                _set_child_subreaper(False)
            if _child_subreaper_state() is not original_state:
                raise PrefreezeEvidenceError("child-subreaper state was not restored")


def _git_stdout(*arguments: str, timeout_seconds: int = 60) -> str:
    git_environment = dict(CLEAN_ENVIRONMENT)
    git_environment.update({"GIT_TERMINAL_PROMPT": "0"})
    captured = run_bounded_command(
        ("/usr/bin/git", *arguments), timeout_seconds=timeout_seconds,
        stdout_cap=256 * 1024, stderr_cap=256 * 1024,
        environment=git_environment,
    )
    if captured.return_code != 0 or captured.stderr:
        raise PrefreezeEvidenceError(
            f"read-only Git command failed: {' '.join(arguments)}"
        )
    try:
        return captured.stdout.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise PrefreezeEvidenceError("Git output is not strict UTF-8") from error


def capture_repository_snapshot() -> dict[str, Any]:
    """Capture and internally cross-check the clean local/live Git identity."""

    top = _git_stdout("rev-parse", "--show-toplevel").strip()
    if top != os.fspath(ROOT.parents[2]):
        raise PrefreezeEvidenceError("Git top-level differs from repository authority")
    branch = _git_stdout("branch", "--show-current").strip()
    commit = _git_stdout("rev-parse", "HEAD").strip()
    tree = _git_stdout("rev-parse", "HEAD^{tree}").strip()
    commit_object = _git_stdout("cat-file", "-p", commit)
    first_line = commit_object.splitlines()[0] if commit_object else ""
    if first_line != f"tree {tree}":
        raise PrefreezeEvidenceError("capture commit does not bind capture tree")
    origin_url = _git_stdout("remote", "get-url", "origin").strip()
    origin_oid = _git_stdout("rev-parse", "refs/remotes/origin/main").strip()
    live_lines = _git_stdout(
        "ls-remote", "--heads", "origin", "refs/heads/main",
        timeout_seconds=120,
    ).splitlines()
    if len(live_lines) != 1:
        raise PrefreezeEvidenceError("live origin/main lookup is not unique")
    live_fields = live_lines[0].split("\t")
    if len(live_fields) != 2 or live_fields[1] != "refs/heads/main":
        raise PrefreezeEvidenceError("live origin/main lookup shape mismatch")
    live_oid = live_fields[0]
    ahead_behind = _git_stdout(
        "rev-list", "--left-right", "--count",
        "HEAD...refs/remotes/origin/main",
    ).strip().split()
    if len(ahead_behind) != 2 or any(not item.isdecimal() for item in ahead_behind):
        raise PrefreezeEvidenceError("Git ahead/behind result shape mismatch")
    status = _git_stdout("status", "--porcelain=v1", "--untracked-files=all")
    clean = status == ""
    snapshot = {
        "authority_root": os.fspath(ROOT),
        "branch": branch,
        "capture_commit_oid": commit,
        "capture_tree_oid": tree,
        "origin_url": origin_url,
        "origin_main_oid": origin_oid,
        "live_remote_main_oid": live_oid,
        "head_equals_origin_main": commit == origin_oid,
        "head_equals_live_remote_main": commit == live_oid,
        "ahead": int(ahead_behind[0]),
        "behind": int(ahead_behind[1]),
        "worktree_clean_before": clean,
        "worktree_clean_after": clean,
    }
    _validate_repository_snapshot(snapshot)
    return snapshot


def replay_repository_snapshot(expected: Mapping[str, Any]) -> None:
    actual = capture_repository_snapshot()
    if not _exact_json_equal(actual, expected):
        raise PrefreezeEvidenceError("terminal repository snapshot changed")


def replay_repository_snapshot_with_untracked(
    expected: Mapping[str, Any], untracked_paths: Sequence[Path],
) -> None:
    """Replay the frozen Git envelope allowing only exact publisher-owned files."""

    snapshot = _validate_repository_snapshot(expected)
    top = Path(_git_stdout("rev-parse", "--show-toplevel").strip())
    if top != ROOT.parents[2]:
        raise PrefreezeEvidenceError("Git top-level changed during publication")
    branch = _git_stdout("branch", "--show-current").strip()
    commit = _git_stdout("rev-parse", "HEAD").strip()
    tree = _git_stdout("rev-parse", "HEAD^{tree}").strip()
    commit_object = _git_stdout("cat-file", "-p", commit)
    if not commit_object or commit_object.splitlines()[0] != f"tree {tree}":
        raise PrefreezeEvidenceError("publication Git commit/tree mismatch")
    origin_url = _git_stdout("remote", "get-url", "origin").strip()
    origin_oid = _git_stdout("rev-parse", "refs/remotes/origin/main").strip()
    live_lines = _git_stdout(
        "ls-remote", "--heads", "origin", "refs/heads/main",
        timeout_seconds=120,
    ).splitlines()
    if len(live_lines) != 1:
        raise PrefreezeEvidenceError("publication live origin/main lookup mismatch")
    live_fields = live_lines[0].split("\t")
    if len(live_fields) != 2 or live_fields[1] != "refs/heads/main":
        raise PrefreezeEvidenceError("publication live origin/main shape mismatch")
    ahead_behind = _git_stdout(
        "rev-list", "--left-right", "--count",
        "HEAD...refs/remotes/origin/main",
    ).strip().split()
    if len(ahead_behind) != 2 or any(not item.isdecimal() for item in ahead_behind):
        raise PrefreezeEvidenceError("publication Git ahead/behind shape mismatch")
    facts = {
        "authority_root": os.fspath(ROOT),
        "branch": branch,
        "capture_commit_oid": commit,
        "capture_tree_oid": tree,
        "origin_url": origin_url,
        "origin_main_oid": origin_oid,
        "live_remote_main_oid": live_fields[0],
        "head_equals_origin_main": commit == origin_oid,
        "head_equals_live_remote_main": commit == live_fields[0],
        "ahead": int(ahead_behind[0]),
        "behind": int(ahead_behind[1]),
    }
    for key, value in facts.items():
        if not _exact_json_equal(value, snapshot[key]):
            raise PrefreezeEvidenceError(f"publication Git fact changed: {key}")
    relative_paths: list[str] = []
    for path in untracked_paths:
        path = _absolute_lexical(path, "publisher-owned untracked path")
        try:
            relative = path.relative_to(top)
        except ValueError as error:
            raise PrefreezeEvidenceError(
                "publisher-owned path is outside Git worktree"
            ) from error
        relative_text = PurePosixPath(relative).as_posix()
        if relative_text in relative_paths:
            raise PrefreezeEvidenceError("duplicate publisher-owned untracked path")
        relative_paths.append(relative_text)
    expected_status = "".join(f"?? {path}\n" for path in sorted(relative_paths))
    status = _git_stdout("status", "--porcelain=v1", "--untracked-files=all", "--")
    if status != expected_status:
        raise PrefreezeEvidenceError("Git status contains non-publisher changes")
    if _git_stdout("diff", "--check", "HEAD", "--") != "":
        raise PrefreezeEvidenceError("tracked diff-check changed during publication")


def secure_relative_exists(relative: str, context: str) -> bool:
    relative = _relative_path(relative, context)
    parts = PurePosixPath(relative).parts
    descriptor, root_chain = _open_absolute_directory(ROOT, "Paper02 authority root")
    relative_chain: list[tuple[int, int, int, int, int]] = []
    try:
        for part in parts[:-1]:
            try:
                lexical_before = os.stat(
                    part, dir_fd=descriptor, follow_symlinks=False
                )
                next_fd = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
                    | getattr(os, "O_CLOEXEC", 0),
                    dir_fd=descriptor,
                )
            except FileNotFoundError:
                return False
            lexical = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            opened = os.fstat(next_fd)
            if (
                not stat.S_ISDIR(opened.st_mode)
                or _relative_directory_identity(lexical_before)
                != _relative_directory_identity(opened)
                or _relative_directory_identity(lexical)
                != _relative_directory_identity(opened)
            ):
                os.close(next_fd)
                raise PrefreezeEvidenceError(f"{context}: namespace parent mismatch")
            relative_chain.append(_relative_directory_identity(opened))
            os.close(descriptor)
            descriptor = next_fd
        try:
            os.stat(parts[-1], dir_fd=descriptor, follow_symlinks=False)
        except FileNotFoundError:
            exists = False
        else:
            exists = True
        replay_fd, replay_chain = _open_absolute_directory(ROOT, "Paper02 authority root")
        try:
            if replay_chain != root_chain:
                raise PrefreezeEvidenceError(f"{context}: authority root changed")
        finally:
            os.close(replay_fd)
        _replay_relative_directories(parts[:-1], relative_chain, context)
        return exists
    except OSError as error:
        raise PrefreezeEvidenceError(f"{context}: namespace inspection failed: {error}") from error
    finally:
        os.close(descriptor)


def assert_prefreeze_namespaces_absent() -> None:
    reserved = (
        (os.fspath(CANONICAL_RELATIVE), "canonical role11"),
        (os.fspath(ROLE12_RELATIVE), "canonical role12"),
        (os.fspath(ROLE54_RELATIVE), "canonical role54"),
        (os.fspath(CANONICAL_RESULT_ROOT), "canonical result root"),
        (os.fspath(CANONICAL_OPERATIONAL_ROOT), "canonical operational root"),
    )
    for relative, context in reserved:
        if secure_relative_exists(relative, context):
            raise PrefreezeEvidenceError(f"{context} must be absent before role11 publication")


def assert_downstream_namespaces_absent() -> None:
    reserved = (
        (os.fspath(ROLE12_RELATIVE), "canonical role12"),
        (os.fspath(ROLE54_RELATIVE), "canonical role54"),
        (os.fspath(CANONICAL_RESULT_ROOT), "canonical result root"),
        (os.fspath(CANONICAL_OPERATIONAL_ROOT), "canonical operational root"),
    )
    for relative, context in reserved:
        if secure_relative_exists(relative, context):
            raise PrefreezeEvidenceError(
                f"{context} must remain absent during role11 publication"
            )


def _validate_rebuild_output_path(value: str) -> Path:
    if type(value) is not str or not value or "\x00" in value:
        raise PrefreezeEvidenceError("rebuild output must be an exact path string")
    output = _absolute_lexical(Path(value), "rebuild output")
    pure = PurePosixPath(value)
    if (
        pure.parts[:2] != ("/", "tmp")
        or pure.name != REBUILD_OUTPUT_BASENAME
        or not pure.parent.name.startswith("a416-l3a1-role11-rebuild.")
        or pure.parent.parent != PurePosixPath("/tmp")
    ):
        raise PrefreezeEvidenceError("rebuild output is not the fixed owned /tmp shape")
    suffix = pure.parent.name.removeprefix("a416-l3a1-role11-rebuild.")
    if len(suffix) < 6 or any(
        character not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for character in suffix
    ):
        raise PrefreezeEvidenceError("rebuild output temporary suffix mismatch")
    return output


def _read_regular_at(
    parent_fd: int, name: str, context: str, *, maximum_bytes: int,
) -> FileImage:
    lexical_pre = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    if (
        not stat.S_ISREG(lexical_pre.st_mode) or lexical_pre.st_nlink != 1
        or lexical_pre.st_size < 1 or lexical_pre.st_size > maximum_bytes
    ):
        raise PrefreezeEvidenceError(f"{context}: regular single-link size contract mismatch")
    descriptor = os.open(
        name,
        os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0),
        dir_fd=parent_fd,
    )
    try:
        before = os.fstat(descriptor)
        if _stat_identity(before) != _stat_identity(lexical_pre):
            raise PrefreezeEvidenceError(f"{context}: pre-open identity mismatch")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(descriptor, min(1024 * 1024, maximum_bytes - total + 1))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total > maximum_bytes:
                raise PrefreezeEvidenceError(f"{context}: byte cap exceeded")
        after = os.fstat(descriptor)
        lexical_post = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if (
            _stat_identity(before) != _stat_identity(after)
            or _stat_identity(after) != _stat_identity(lexical_post)
            or total != after.st_size
        ):
            raise PrefreezeEvidenceError(f"{context}: changed during read")
        return FileImage(
            raw=b"".join(chunks), device_id=after.st_dev, inode=after.st_ino,
            mode=after.st_mode, nlink=after.st_nlink, size_bytes=after.st_size,
            mtime_ns=after.st_mtime_ns, ctime_ns=after.st_ctime_ns,
        )
    finally:
        os.close(descriptor)


def _external_followed_image(path: Path, context: str) -> tuple[str, FileImage]:
    """Capture one fixed external alias and its resolved regular file."""

    path = _absolute_lexical(path, context)
    try:
        lexical_before = os.lstat(path)
        link_before = os.readlink(path) if stat.S_ISLNK(lexical_before.st_mode) else None
        resolved = Path(os.path.realpath(path))
        if not resolved.is_absolute() or not resolved.is_file():
            raise PrefreezeEvidenceError(f"{context}: resolved target is not a file")
        parent_fd, parent_chain = _open_absolute_directory(resolved.parent, context)
        try:
            image = _read_regular_at(
                parent_fd, resolved.name, context, maximum_bytes=MAX_ROLE_BYTES,
            )
            _replay_open_directory(resolved.parent, parent_fd, parent_chain, context)
        finally:
            os.close(parent_fd)
        lexical_after = os.lstat(path)
        link_after = os.readlink(path) if stat.S_ISLNK(lexical_after.st_mode) else None
        if (
            _stat_identity(lexical_before) != _stat_identity(lexical_after)
            or link_before != link_after
            or Path(os.path.realpath(path)) != resolved
        ):
            raise PrefreezeEvidenceError(f"{context}: external alias changed")
        return os.fspath(resolved), image
    except OSError as error:
        raise PrefreezeEvidenceError(f"{context}: external capture failed: {error}") from error


COMPILER_ENVIRONMENT_PATHS = (
    Path("/usr/bin/g++"),
    Path("/root/autodl-tmp/zeta/dependencies/capd-r401-a1/build-mp/libcapd.a"),
    Path(
        "/root/autodl-tmp/zeta/dependencies/capd-r401-a1/"
        "build-mp/capdExt/filibsrc/libfilib.a"
    ),
    Path("/usr/lib/x86_64-linux-gnu/libmpfr.so.6"),
    Path("/usr/lib/x86_64-linux-gnu/libgmp.so.10"),
)


def _capture_compiler_environment() -> dict[str, tuple[str, FileImage]]:
    result = {
        os.fspath(path): _external_followed_image(path, f"compiler binding {path}")
        for path in COMPILER_ENVIRONMENT_PATHS
    }
    compiler = result["/usr/bin/g++"][1]
    if hashlib.sha256(compiler.raw).hexdigest() != (
        "d7122fd9a7a8fe12d12c00c54d3a6fbebcb3e9285cf675709674e751d900fc63"
    ):
        raise PrefreezeEvidenceError("live /usr/bin/g++ hash differs from role10")
    return result


def _remove_rebuild_parent(output: Path, parent_identity: tuple[int, int]) -> None:
    tmp_fd, tmp_chain = _open_absolute_directory(Path("/tmp"), "rebuild /tmp parent")
    try:
        entry = os.stat(output.parent.name, dir_fd=tmp_fd, follow_symlinks=False)
        if (
            not stat.S_ISDIR(entry.st_mode)
            or (entry.st_dev, entry.st_ino) != parent_identity
            or entry.st_uid != os.geteuid()
            or stat.S_IMODE(entry.st_mode) != 0o700
        ):
            raise PrefreezeEvidenceError("refused to remove replaced rebuild parent")
        os.rmdir(output.parent.name, dir_fd=tmp_fd)
        os.fsync(tmp_fd)
        try:
            os.stat(output.parent.name, dir_fd=tmp_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("rebuild parent remained after cleanup")
        tmp_chain[-1] = _directory_identity(os.fstat(tmp_fd))
        _replay_open_directory(Path("/tmp"), tmp_fd, tmp_chain, "rebuild /tmp parent")
    except OSError as error:
        raise PrefreezeEvidenceError(f"rebuild parent cleanup failed: {error}") from error
    finally:
        os.close(tmp_fd)


def run_second_fresh_rebuild(output_value: str) -> dict[str, Any]:
    """Compile frozen role 16 once to owned /tmp and prove role 17 untouched."""

    output = _validate_rebuild_output_path(output_value)
    parent_fd, parent_chain = _open_absolute_directory(output.parent, "rebuild parent")
    stage_inode: tuple[int, int] | None = None
    parent_identity: tuple[int, int] | None = None
    cleanup_authorized = False
    receipt: dict[str, Any] | None = None
    try:
        parent_info = os.fstat(parent_fd)
        if (
            not stat.S_ISDIR(parent_info.st_mode)
            or stat.S_IMODE(parent_info.st_mode) != 0o700
            or parent_info.st_uid != os.geteuid()
        ):
            raise PrefreezeEvidenceError("rebuild parent must be owned mode-0700 directory")
        parent_identity = (parent_info.st_dev, parent_info.st_ino)
        try:
            os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("rebuild output already exists")
        cleanup_authorized = True

        compiler_environment_before = _capture_compiler_environment()
        source_before = secure_read_relative(
            "validated/capd_r401_phase_branch_tube_mp_a1.cpp", "frozen branch source"
        )
        persistent_before = secure_read_relative(
            "validated/bin/capd_r401_phase_branch_tube_mp_a1",
            "persistent branch binary",
        )
        persistent_hash = hashlib.sha256(persistent_before.raw).hexdigest()
        if persistent_hash != "25aec3d7d68883c2a97f765682a40cabc3feb91f159f67ac2910b6f82025e521":
            raise PrefreezeEvidenceError("persistent role17 hash differs from machine freeze")

        stage_fd = os.open(
            output.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_CLOEXEC", 0),
            0o600,
            dir_fd=parent_fd,
        )
        try:
            initial = os.fstat(stage_fd)
            if not stat.S_ISREG(initial.st_mode) or initial.st_nlink != 1:
                raise PrefreezeEvidenceError("rebuild staging inode contract mismatch")
            stage_inode = (initial.st_dev, initial.st_ino)
            os.fchmod(stage_fd, 0o644)
            os.fsync(stage_fd)
        finally:
            os.close(stage_fd)
        os.fsync(parent_fd)
        parent_chain[-1] = _directory_identity(os.fstat(parent_fd))
        _replay_open_directory(output.parent, parent_fd, parent_chain, "rebuild parent")

        compiler_argv = (*COMPILER_ARGV_PREFIX, os.fspath(output))
        compiled = run_bounded_command(
            compiler_argv, timeout_seconds=COMMAND_TIMEOUT_SECONDS,
            stdout_cap=MAX_STDOUT_BYTES, stderr_cap=MAX_STDERR_BYTES,
        )
        if compiled.return_code != 0 or compiled.stdout or compiled.stderr:
            raise PrefreezeEvidenceError("fresh compiler invocation was not exact silent success")
        _replay_open_directory(output.parent, parent_fd, parent_chain, "rebuild parent")
        rebuilt = _read_regular_at(
            parent_fd, output.name, "fresh rebuild output", maximum_bytes=MAX_ROLE_BYTES,
        )
        if (
            (rebuilt.device_id, rebuilt.inode) != stage_inode
            or stat.S_IMODE(rebuilt.mode) != 0o755
            or rebuilt.raw != persistent_before.raw
        ):
            raise PrefreezeEvidenceError("fresh rebuild differs from persistent role17")
        if (rebuilt.device_id, rebuilt.inode) == (
            persistent_before.device_id, persistent_before.inode
        ):
            raise PrefreezeEvidenceError("fresh rebuild aliases persistent role17")

        source_after = secure_read_relative(
            "validated/capd_r401_phase_branch_tube_mp_a1.cpp", "frozen branch source replay"
        )
        persistent_after = secure_read_relative(
            "validated/bin/capd_r401_phase_branch_tube_mp_a1",
            "persistent branch binary replay",
        )
        if source_after != source_before or persistent_after != persistent_before:
            raise PrefreezeEvidenceError("source or persistent role17 changed during rebuild")
        _replay_open_directory(output.parent, parent_fd, parent_chain, "rebuild parent")
        terminal_rebuilt = _read_regular_at(
            parent_fd, output.name, "terminal fresh rebuild output",
            maximum_bytes=MAX_ROLE_BYTES,
        )
        if terminal_rebuilt != rebuilt:
            raise PrefreezeEvidenceError("fresh rebuild output changed terminally")

        compiler_environment_after = _capture_compiler_environment()
        if compiler_environment_after != compiler_environment_before:
            raise PrefreezeEvidenceError("compiler or link libraries changed during rebuild")

        receipt = {
            "verification_status": SECOND_REBUILD_STATUS,
            "authority": SECOND_REBUILD_AUTHORITY,
            "source_path": "validated/capd_r401_phase_branch_tube_mp_a1.cpp",
            "source_sha256": hashlib.sha256(source_before.raw).hexdigest(),
            "persistent_binary_path": "validated/bin/capd_r401_phase_branch_tube_mp_a1",
            "persistent_before_sha256": persistent_hash,
            "persistent_after_sha256": hashlib.sha256(persistent_after.raw).hexdigest(),
            "persistent_before_device_id": persistent_before.device_id,
            "persistent_before_inode": persistent_before.inode,
            "persistent_after_device_id": persistent_after.device_id,
            "persistent_after_inode": persistent_after.inode,
            "persistent_identity_unchanged": persistent_after.identity == persistent_before.identity,
            "persistent_overwrite_performed": False,
            "staging_output_sha256": hashlib.sha256(rebuilt.raw).hexdigest(),
            "staging_output_size_bytes": rebuilt.size_bytes,
            "staging_output_mode": f"0{stat.S_IMODE(rebuilt.mode):03o}",
            "staging_output_removed": True,
            "byte_for_byte_equal": rebuilt.raw == persistent_before.raw,
            "scientific_evaluator_dispatched": False,
        }
    finally:
        cleanup_error: BaseException | None = None
        if stage_inode is not None:
            try:
                current = os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
            except FileNotFoundError:
                cleanup_error = PrefreezeEvidenceError(
                    "owned rebuild staging output disappeared before cleanup"
                )
            else:
                if (current.st_dev, current.st_ino) == stage_inode:
                    try:
                        os.unlink(output.name, dir_fd=parent_fd)
                        os.fsync(parent_fd)
                    except OSError as error:
                        cleanup_error = PrefreezeEvidenceError(
                            f"rebuild staging cleanup failed: {error}"
                        )
                else:
                    cleanup_error = PrefreezeEvidenceError(
                        "refused to clean a replaced rebuild staging inode"
                    )
        os.close(parent_fd)
        if cleanup_error is None and cleanup_authorized and parent_identity is not None:
            try:
                _remove_rebuild_parent(output, parent_identity)
            except BaseException as error:
                cleanup_error = error
        if cleanup_error is not None:
            raise cleanup_error

    if receipt is None:
        raise PrefreezeEvidenceError("fresh rebuild produced no receipt")
    if output.exists() or output.parent.exists():
        raise PrefreezeEvidenceError("fresh rebuild temporary namespace survived cleanup")
    roles = {
        "branch_evaluator_source": role_binding(
            "branch_evaluator_source", "validated/capd_r401_phase_branch_tube_mp_a1.cpp"
        ),
        "branch_evaluator_binary": role_binding(
            "branch_evaluator_binary", "validated/bin/capd_r401_phase_branch_tube_mp_a1"
        ),
    }
    _validate_second_rebuild_receipt(receipt, roles, "fresh rebuild receipt")
    canonical_json_bytes(receipt)
    return receipt


HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
GIT_OID = re.compile(r"^[0-9a-f]{40}$")
UTC_SECOND = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
MODE_TEXT = re.compile(r"^0[0-7]{3}$")
PYTEST_SUMMARY = re.compile(
    r"^(?P<counts>[0-9]+ (?:passed|failed|skipped|xfailed|xpassed)"
    r"(?:, [0-9]+ (?:passed|failed|skipped|xfailed|xpassed))*) "
    r"in [0-9]+(?:\.[0-9]+)?s$"
)


def _plain_json(value: Any, context: str, seen: set[int] | None = None) -> None:
    """Accept only the exact, acyclic plain-JSON Python domain."""

    if seen is None:
        seen = set()
    if value is None or type(value) in (bool, int):
        return
    if type(value) is str:
        try:
            value.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise PrefreezeEvidenceError(
                f"{context}: string is not strict UTF-8 encodable"
            ) from error
        return
    if type(value) not in (list, dict):
        raise PrefreezeEvidenceError(
            f"{context}: non-plain JSON value {type(value).__name__}"
        )
    identity = id(value)
    if identity in seen:
        raise PrefreezeEvidenceError(f"{context}: cyclic JSON value")
    seen.add(identity)
    try:
        if type(value) is list:
            for index, item in enumerate(value):
                _plain_json(item, f"{context}[{index}]", seen)
        else:
            for key, item in value.items():
                if type(key) is not str:
                    raise PrefreezeEvidenceError(
                        f"{context}: object key is not an exact string"
                    )
                _plain_json(key, f"{context} key", seen)
                _plain_json(item, f"{context}.{key}", seen)
    finally:
        seen.remove(identity)


def canonical_json_bytes(payload: Any) -> bytes:
    _plain_json(payload, "canonical JSON payload")
    return (
        json.dumps(
            payload, sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise PrefreezeEvidenceError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise PrefreezeEvidenceError(f"non-finite JSON constant: {value}")


def strict_json_bytes(data: bytes, context: str) -> dict[str, Any]:
    if type(data) is not bytes:
        raise PrefreezeEvidenceError(f"{context}: exact bytes required")
    try:
        payload = json.loads(
            data.decode("utf-8", errors="strict"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except PrefreezeEvidenceError:
        raise
    except Exception as error:
        raise PrefreezeEvidenceError(f"{context}: invalid strict JSON: {error}") from error
    _plain_json(payload, context)
    if type(payload) is not dict:
        raise PrefreezeEvidenceError(f"{context}: top-level object required")
    return payload


def _exact_dict(value: Any, keys: frozenset[str], context: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != keys:
        raise PrefreezeEvidenceError(f"{context}: exact key set mismatch")
    return value


def _exact_string(value: Any, context: str, *, expected: str | None = None) -> str:
    if type(value) is not str or not value or "\x00" in value:
        raise PrefreezeEvidenceError(f"{context}: nonempty exact string required")
    if expected is not None and value != expected:
        raise PrefreezeEvidenceError(f"{context}: literal mismatch")
    return value


def _exact_int(
    value: Any, context: str, *, minimum: int = 0, expected: int | None = None,
) -> int:
    if type(value) is not int or value < minimum:
        raise PrefreezeEvidenceError(f"{context}: exact integer out of range")
    if expected is not None and value != expected:
        raise PrefreezeEvidenceError(f"{context}: integer literal mismatch")
    return value


def _exact_bool(value: Any, context: str, *, expected: bool) -> None:
    if type(value) is not bool or value is not expected:
        raise PrefreezeEvidenceError(f"{context}: Boolean literal mismatch")


def _hash(value: Any, context: str, *, expected: str | None = None) -> str:
    value = _exact_string(value, context)
    if HEX_SHA256.fullmatch(value) is None:
        raise PrefreezeEvidenceError(f"{context}: lowercase SHA-256 required")
    if expected is not None and value != expected:
        raise PrefreezeEvidenceError(f"{context}: SHA-256 mismatch")
    return value


def _git_oid(value: Any, context: str) -> str:
    value = _exact_string(value, context)
    if GIT_OID.fullmatch(value) is None:
        raise PrefreezeEvidenceError(f"{context}: lowercase SHA-1 Git OID required")
    return value


def _utc(value: Any, context: str) -> datetime:
    value = _exact_string(value, context)
    if UTC_SECOND.fullmatch(value) is None:
        raise PrefreezeEvidenceError(f"{context}: UTC whole-second timestamp required")
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError as error:
        raise PrefreezeEvidenceError(f"{context}: invalid UTC timestamp") from error
    if parsed.strftime("%Y-%m-%dT%H:%M:%SZ") != value:
        raise PrefreezeEvidenceError(f"{context}: noncanonical UTC timestamp")
    return parsed


def _relative_path(value: Any, context: str, *, expected: str | None = None) -> str:
    value = _exact_string(value, context, expected=expected)
    if "\\" in value:
        raise PrefreezeEvidenceError(f"{context}: POSIX path required")
    path = PurePosixPath(value)
    if (
        path.is_absolute() or os.fspath(path) != value or not path.parts
        or any(part in ("", ".", "..") for part in path.parts)
    ):
        raise PrefreezeEvidenceError(f"{context}: canonical relative path required")
    return value


def _mode(value: Any, context: str) -> str:
    value = _exact_string(value, context)
    if MODE_TEXT.fullmatch(value) is None:
        raise PrefreezeEvidenceError(f"{context}: four-character octal mode required")
    return value


def _exact_json_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(
            _exact_json_equal(left[key], right[key]) for key in left
        )
    if type(left) is list:
        return len(left) == len(right) and all(
            _exact_json_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def _validate_role_entry(
    value: Any, expected_role: str, expected_path: str, context: str,
) -> dict[str, Any]:
    entry = _exact_dict(value, ROLE_ENTRY_KEYS, context)
    _exact_string(entry["role"], f"{context}.role", expected=expected_role)
    _relative_path(entry["path"], f"{context}.path", expected=expected_path)
    _hash(entry["sha256"], f"{context}.sha256")
    _exact_int(entry["size_bytes"], f"{context}.size_bytes", minimum=1)
    _mode(entry["mode"], f"{context}.mode")
    _exact_int(entry["nlink"], f"{context}.nlink", minimum=1, expected=1)
    return entry


def _validate_file_binding(value: Any, expected_path: str, context: str) -> dict[str, Any]:
    binding = _exact_dict(value, FILE_BINDING_KEYS, context)
    _relative_path(binding["path"], f"{context}.path", expected=expected_path)
    _hash(binding["sha256"], f"{context}.sha256")
    _exact_int(binding["size_bytes"], f"{context}.size_bytes", minimum=1)
    _mode(binding["mode"], f"{context}.mode")
    _exact_int(binding["nlink"], f"{context}.nlink", minimum=1, expected=1)
    return binding


def _validate_verify_receipt(
    value: Any, *, status: str, candidate_sha256: str, size_bytes: int,
    context: str,
) -> dict[str, Any]:
    receipt = _exact_dict(value, VERIFY_RECEIPT_KEYS, context)
    _exact_string(receipt["verification_status"], f"{context}.verification_status", expected=status)
    _exact_string(receipt["authority"], f"{context}.authority", expected=VERIFY_AUTHORITY)
    _hash(receipt["candidate_sha256"], f"{context}.candidate_sha256", expected=candidate_sha256)
    _exact_int(receipt["size_bytes"], f"{context}.size_bytes", expected=size_bytes)
    _exact_bool(receipt["promotion_authorized"], f"{context}.promotion_authorized", expected=False)
    return receipt


def _validate_second_rebuild_receipt(
    value: Any, roles: Mapping[str, dict[str, Any]], context: str,
) -> dict[str, Any]:
    receipt = _exact_dict(value, SECOND_REBUILD_RECEIPT_KEYS, context)
    _exact_string(receipt["verification_status"], f"{context}.verification_status", expected=SECOND_REBUILD_STATUS)
    _exact_string(receipt["authority"], f"{context}.authority", expected=SECOND_REBUILD_AUTHORITY)
    source = roles["branch_evaluator_source"]
    binary = roles["branch_evaluator_binary"]
    _relative_path(receipt["source_path"], f"{context}.source_path", expected=source["path"])
    _hash(receipt["source_sha256"], f"{context}.source_sha256", expected=source["sha256"])
    _relative_path(receipt["persistent_binary_path"], f"{context}.persistent_binary_path", expected=binary["path"])
    for name in ("persistent_before_sha256", "persistent_after_sha256", "staging_output_sha256"):
        _hash(receipt[name], f"{context}.{name}", expected=binary["sha256"])
    _exact_int(receipt["staging_output_size_bytes"], f"{context}.staging_output_size_bytes", expected=binary["size_bytes"])
    _exact_string(receipt["staging_output_mode"], f"{context}.staging_output_mode", expected=binary["mode"])
    for name in (
        "persistent_before_device_id", "persistent_before_inode",
        "persistent_after_device_id", "persistent_after_inode",
    ):
        _exact_int(receipt[name], f"{context}.{name}", minimum=1)
    if (
        receipt["persistent_before_device_id"] != receipt["persistent_after_device_id"]
        or receipt["persistent_before_inode"] != receipt["persistent_after_inode"]
    ):
        raise PrefreezeEvidenceError(f"{context}: persistent inode identity changed")
    _exact_bool(receipt["persistent_identity_unchanged"], f"{context}.persistent_identity_unchanged", expected=True)
    _exact_bool(receipt["persistent_overwrite_performed"], f"{context}.persistent_overwrite_performed", expected=False)
    _exact_bool(receipt["staging_output_removed"], f"{context}.staging_output_removed", expected=True)
    _exact_bool(receipt["byte_for_byte_equal"], f"{context}.byte_for_byte_equal", expected=True)
    _exact_bool(receipt["scientific_evaluator_dispatched"], f"{context}.scientific_evaluator_dispatched", expected=False)
    return receipt


def _parse_pytest_counts(stdout: str, context: str) -> dict[str, int]:
    if any(
        (ord(character) < 32 and character != "\n")
        or ord(character) == 127
        or character in "\u0085\u2028\u2029"
        for character in stdout
    ):
        raise PrefreezeEvidenceError(
            f"{context}: ANSI/control output is forbidden"
        )
    if not stdout.endswith("\n"):
        raise PrefreezeEvidenceError(
            f"{context}: exactly one terminal pytest summary required"
        )
    lines = stdout[:-1].split("\n")
    matches = [PYTEST_SUMMARY.fullmatch(line) for line in lines]
    matched = [match for match in matches if match is not None]
    if len(matched) != 1 or not lines or matches[-1] is None:
        raise PrefreezeEvidenceError(f"{context}: exactly one terminal pytest summary required")
    forbidden = re.search(
        r"(?i)(?<![A-Za-z0-9_])"
        r"(?:errors?|fail(?:ed|ures?)?|warnings?|deselected|"
        r"skipped|xfail(?:ed)?|xpass(?:ed)?)"
        r"(?![A-Za-z0-9_])",
        stdout,
    )
    if forbidden is not None:
        raise PrefreezeEvidenceError(
            f"{context}: forbidden pytest token {forbidden.group(0)!r}"
        )
    counts = {name: 0 for name in PYTEST_COUNT_KEYS}
    observed: set[str] = set()
    assert matched[0] is not None
    for item in matched[0].group("counts").split(", "):
        count_text, name = item.split(" ", 1)
        if name in observed:
            raise PrefreezeEvidenceError(f"{context}: duplicate pytest category")
        observed.add(name)
        counts[name] = int(count_text)
    if counts["passed"] <= 0 or any(counts[name] != 0 for name in counts if name != "passed"):
        raise PrefreezeEvidenceError(f"{context}: pytest result is not an all-pass record")
    return counts


def _validate_command_argv(name: str, argv: Any, context: str) -> list[str]:
    if type(argv) is not list or not argv or any(
        type(item) is not str or not item or "\x00" in item for item in argv
    ):
        raise PrefreezeEvidenceError(f"{context}: exact nonempty argv strings required")
    if name != "second_fresh_rebuild":
        if tuple(argv) != FIXED_COMMAND_ARGV[name]:
            raise PrefreezeEvidenceError(f"{context}: fixed argv mismatch")
        return argv
    if tuple(argv[:-1]) != REBUILD_COMMAND_ARGV_PREFIX:
        raise PrefreezeEvidenceError(f"{context}: rebuild argv prefix mismatch")
    output = PurePosixPath(argv[-1])
    if (
        not output.is_absolute() or os.fspath(output) != argv[-1]
        or output.name != REBUILD_OUTPUT_BASENAME
        or not output.parent.name.startswith("a416-l3a1-role11-rebuild.")
        or output.parts[:2] != ("/", "tmp")
        or any(part in ("", ".", "..") for part in output.parts[1:])
    ):
        raise PrefreezeEvidenceError(f"{context}: rebuild output is not an owned /tmp path")
    suffix = output.parent.name.removeprefix("a416-l3a1-role11-rebuild.")
    if len(suffix) < 6 or any(character not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for character in suffix):
        raise PrefreezeEvidenceError(f"{context}: rebuild temporary suffix mismatch")
    return argv


def _validate_command_result(
    value: Any, index: int, roles: Mapping[str, dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, int] | None]:
    expected_name, expected_kind = COMMAND_SPECS[index]
    context = f"command_results[{index}]"
    result = _exact_dict(value, COMMAND_RESULT_KEYS, context)
    _exact_string(result["name"], f"{context}.name", expected=expected_name)
    _exact_string(result["kind"], f"{context}.kind", expected=expected_kind)
    _validate_command_argv(expected_name, result["argv"], f"{context}.argv")
    _exact_string(result["cwd"], f"{context}.cwd", expected=os.fspath(ROOT))
    if type(result["environment"]) is not dict or not _exact_json_equal(result["environment"], CLEAN_ENVIRONMENT):
        raise PrefreezeEvidenceError(f"{context}.environment: fixed environment mismatch")
    _exact_int(result["return_code"], f"{context}.return_code", expected=0)
    _utc(result["started_at_utc"], f"{context}.started_at_utc")
    _exact_int(result["wall_duration_ms"], f"{context}.wall_duration_ms", minimum=1)
    for stream_name, cap in (("stdout", MAX_STDOUT_BYTES), ("stderr", MAX_STDERR_BYTES)):
        text = result[f"{stream_name}_utf8"]
        if type(text) is not str or "\x00" in text:
            raise PrefreezeEvidenceError(f"{context}.{stream_name}_utf8: exact NUL-free string required")
        try:
            raw = text.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise PrefreezeEvidenceError(f"{context}.{stream_name}_utf8: invalid UTF-8") from error
        if len(raw) > cap:
            raise PrefreezeEvidenceError(f"{context}.{stream_name}_utf8: output cap exceeded")
        _exact_int(result[f"{stream_name}_size_bytes"], f"{context}.{stream_name}_size_bytes", expected=len(raw))
        _hash(result[f"{stream_name}_sha256"], f"{context}.{stream_name}_sha256", expected=hashlib.sha256(raw).hexdigest())
    if result["stderr_utf8"] != "":
        raise PrefreezeEvidenceError(f"{context}: successful command stderr must be empty")

    parsed_counts: dict[str, int] | None = None
    if expected_name in PYTEST_RESULT_TOTAL_NAMES:
        parsed_counts = _parse_pytest_counts(result["stdout_utf8"], context)
        if EXPECTED_TEST_PASSED is not None:
            if not _test_totals_locked():
                raise PrefreezeEvidenceError(
                    "stable expected pytest totals constant is malformed"
                )
            total_name = PYTEST_RESULT_TOTAL_NAMES[expected_name]
            if (
                set(EXPECTED_TEST_PASSED) != TEST_TOTALS_KEYS
                or parsed_counts["passed"] != EXPECTED_TEST_PASSED[total_name]
            ):
                raise PrefreezeEvidenceError(
                    f"{context}: passed count differs from stable expected total"
                )
        counts = _exact_dict(result["pytest_counts"], PYTEST_COUNT_KEYS, f"{context}.pytest_counts")
        for key in PYTEST_COUNT_KEYS:
            _exact_int(counts[key], f"{context}.pytest_counts.{key}", expected=parsed_counts[key])
        if result["semantic_receipt"] is not None:
            raise PrefreezeEvidenceError(f"{context}: pytest semantic_receipt must be null")
    else:
        if result["pytest_counts"] is not None:
            raise PrefreezeEvidenceError(f"{context}: non-pytest pytest_counts must be null")
        if expected_name == "role24_machine_verify":
            receipt = _validate_verify_receipt(
                result["semantic_receipt"], status=MACHINE_VERIFY_STATUS,
                candidate_sha256=MACHINE_SHA256, size_bytes=MACHINE_SIZE_BYTES,
                context=f"{context}.semantic_receipt",
            )
            expected_stdout = (
                f"machine_freeze_verification={MACHINE_VERIFY_STATUS} "
                f"authority={VERIFY_AUTHORITY} candidate_sha256={MACHINE_SHA256} "
                f"size_bytes={MACHINE_SIZE_BYTES} promotion_authorized=false\n"
            )
            if result["stdout_utf8"] != expected_stdout:
                raise PrefreezeEvidenceError(f"{context}: machine verify transcript mismatch")
        elif expected_name == "role13_compatibility_verify":
            receipt = _validate_verify_receipt(
                result["semantic_receipt"], status=ROLE13_VERIFY_STATUS,
                candidate_sha256=ROLE13_SHA256, size_bytes=ROLE13_SIZE_BYTES,
                context=f"{context}.semantic_receipt",
            )
            expected_stdout = (
                f"s0_compatibility_verification={ROLE13_VERIFY_STATUS} "
                f"authority={VERIFY_AUTHORITY} candidate_sha256={ROLE13_SHA256} "
                f"size_bytes={ROLE13_SIZE_BYTES} promotion_authorized=false\n"
            )
            if result["stdout_utf8"] != expected_stdout:
                raise PrefreezeEvidenceError(f"{context}: role13 verify transcript mismatch")
        elif expected_name == "git_diff_check":
            if result["stdout_utf8"] != "" or result["semantic_receipt"] is not None:
                raise PrefreezeEvidenceError(f"{context}: diff-check success must be empty/null")
        else:
            receipt = _validate_second_rebuild_receipt(
                result["semantic_receipt"], roles,
                f"{context}.semantic_receipt",
            )
            if result["stdout_utf8"].encode("utf-8") != canonical_json_bytes(receipt):
                raise PrefreezeEvidenceError(f"{context}: rebuild transcript/receipt mismatch")
    return result, parsed_counts


def _validate_repository_snapshot(value: Any) -> dict[str, Any]:
    snapshot = _exact_dict(value, REPOSITORY_SNAPSHOT_KEYS, "repository_snapshot")
    _exact_string(snapshot["authority_root"], "repository_snapshot.authority_root", expected=os.fspath(ROOT))
    _exact_string(snapshot["branch"], "repository_snapshot.branch", expected="main")
    capture_commit = _git_oid(snapshot["capture_commit_oid"], "repository_snapshot.capture_commit_oid")
    _git_oid(snapshot["capture_tree_oid"], "repository_snapshot.capture_tree_oid")
    _exact_string(
        snapshot["origin_url"], "repository_snapshot.origin_url",
        expected=ORIGIN_URL,
    )
    origin = _git_oid(snapshot["origin_main_oid"], "repository_snapshot.origin_main_oid")
    live = _git_oid(snapshot["live_remote_main_oid"], "repository_snapshot.live_remote_main_oid")
    if capture_commit != origin or capture_commit != live:
        raise PrefreezeEvidenceError("repository_snapshot: capture/origin/live OIDs differ")
    for name in (
        "head_equals_origin_main", "head_equals_live_remote_main",
        "worktree_clean_before", "worktree_clean_after",
    ):
        _exact_bool(snapshot[name], f"repository_snapshot.{name}", expected=True)
    _exact_int(snapshot["ahead"], "repository_snapshot.ahead", expected=0)
    _exact_int(snapshot["behind"], "repository_snapshot.behind", expected=0)
    return snapshot


def _validate_prerequisites(
    value: Any, roles: Mapping[str, dict[str, Any]], command_results: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    prerequisites = _exact_dict(value, PREREQUISITE_BINDING_KEYS, "prerequisite_bindings")
    machine = _exact_dict(prerequisites["machine_role10"], MACHINE_BINDING_KEYS, "prerequisite_bindings.machine_role10")
    role10 = roles["machine_freeze"]
    for key in ROLE_ENTRY_KEYS:
        if not _exact_json_equal(machine[key], role10[key]):
            raise PrefreezeEvidenceError(f"machine role10 binding differs from role snapshot: {key}")
    _hash(machine["sha256"], "machine_role10.sha256", expected=MACHINE_SHA256)
    _exact_int(machine["size_bytes"], "machine_role10.size_bytes", expected=MACHINE_SIZE_BYTES)
    _exact_string(machine["mode"], "machine_role10.mode", expected="0644")
    _exact_string(machine["publication_commit_oid"], "machine_role10.publication_commit_oid", expected=MACHINE_PUBLICATION_COMMIT)
    _relative_path(machine["producer_path"], "machine_role10.producer_path", expected="scripts/run_r401_val_l3_a1_all_slabs.py")
    _hash(machine["producer_sha256"], "machine_role10.producer_sha256", expected=roles["scheduler"]["sha256"])
    _relative_path(machine["verifier_path"], "machine_role10.verifier_path", expected="scripts/build_r401_val_l3_a1_release_provenance.py")
    _hash(machine["verifier_sha256"], "machine_role10.verifier_sha256", expected=roles["release_builder"]["sha256"])
    _exact_bool(machine["promotion_authorized"], "machine_role10.promotion_authorized", expected=False)
    role10_receipt = _validate_verify_receipt(
        machine["verify_receipt"], status=MACHINE_VERIFY_STATUS,
        candidate_sha256=MACHINE_SHA256, size_bytes=MACHINE_SIZE_BYTES,
        context="machine_role10.verify_receipt",
    )
    if not _exact_json_equal(role10_receipt, command_results[0]["semantic_receipt"]):
        raise PrefreezeEvidenceError("machine role10 receipt differs from command result")

    compatibility = _exact_dict(prerequisites["s0_compatibility_role13"], ROLE13_BINDING_KEYS, "prerequisite_bindings.s0_compatibility_role13")
    role13 = roles["s0_compatibility"]
    for key in ROLE_ENTRY_KEYS:
        if not _exact_json_equal(compatibility[key], role13[key]):
            raise PrefreezeEvidenceError(f"role13 binding differs from role snapshot: {key}")
    _hash(compatibility["sha256"], "role13.sha256", expected=ROLE13_SHA256)
    _exact_int(compatibility["size_bytes"], "role13.size_bytes", expected=ROLE13_SIZE_BYTES)
    _exact_string(compatibility["mode"], "role13.mode", expected="0644")
    _exact_string(compatibility["publication_commit_oid"], "role13.publication_commit_oid", expected=ROLE13_PUBLICATION_COMMIT)
    _relative_path(compatibility["producer_path"], "role13.producer_path", expected="scripts/replay_r401_val_l3_s0_through_a1_checkers.py")
    _hash(compatibility["producer_sha256"], "role13.producer_sha256", expected=roles["s0_adapter"]["sha256"])
    _exact_bool(compatibility["promotion_authorized"], "role13.promotion_authorized", expected=False)
    role13_receipt = _validate_verify_receipt(
        compatibility["verify_receipt"], status=ROLE13_VERIFY_STATUS,
        candidate_sha256=ROLE13_SHA256, size_bytes=ROLE13_SIZE_BYTES,
        context="role13.verify_receipt",
    )
    if not _exact_json_equal(role13_receipt, command_results[1]["semantic_receipt"]):
        raise PrefreezeEvidenceError("role13 receipt differs from command result")

    absence = _exact_dict(prerequisites["canonical_absence"], CANONICAL_ABSENCE_KEYS, "prerequisite_bindings.canonical_absence")
    for key in CANONICAL_ABSENCE_KEYS:
        _exact_bool(absence[key], f"canonical_absence.{key}", expected=False)

    rebuild = _exact_dict(prerequisites["second_fresh_rebuild_replay"], SECOND_REBUILD_REPLAY_KEYS, "prerequisite_bindings.second_fresh_rebuild_replay")
    _exact_string(rebuild["command_result_name"], "second_fresh_rebuild_replay.command_result_name", expected="second_fresh_rebuild")
    expected_command_hash = hashlib.sha256(canonical_json_bytes(command_results[6])).hexdigest()
    _hash(rebuild["command_result_sha256"], "second_fresh_rebuild_replay.command_result_sha256", expected=expected_command_hash)
    receipt = _validate_second_rebuild_receipt(
        rebuild["semantic_receipt"], roles,
        "second_fresh_rebuild_replay.semantic_receipt",
    )
    if not _exact_json_equal(receipt, command_results[6]["semantic_receipt"]):
        raise PrefreezeEvidenceError("second rebuild receipt differs from command result")
    return prerequisites


def validate_prefreeze_test_record(payload: Mapping[str, Any]) -> None:
    """Strictly validate one prospective non-authoritative role-11 object."""

    _plain_json(payload, "role-11 record")
    if type(payload) is not dict or set(payload) != TOP_LEVEL_KEYS:
        raise PrefreezeEvidenceError("role-11 top-level key set mismatch")

    _exact_int(payload["schema_version"], "schema_version", expected=SCHEMA_VERSION)
    _exact_string(payload["protocol_id"], "protocol_id", expected=PROTOCOL_ID)
    _exact_string(payload["artifact_role"], "artifact_role", expected=ARTIFACT_ROLE)
    _exact_string(payload["artifact_status"], "artifact_status", expected=ARTIFACT_STATUS)
    _exact_string(payload["authority"], "authority", expected=AUTHORITY)
    recorded_at = _utc(payload["recorded_at_utc"], "recorded_at_utc")
    for name in (
        "scientific_licensing_enabled", "production_authorized",
        "scientific_dispatch_performed",
    ):
        _exact_bool(payload[name], name, expected=False)
    for name in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload[name] is not None:
            raise PrefreezeEvidenceError(f"{name}: null required")

    policy = _exact_dict(payload["held_out_policy"], HELD_OUT_POLICY_KEYS, "held_out_policy")
    _exact_bool(policy["held_out_l3_scientific_outputs_read"], "held_out_policy.held_out_l3_scientific_outputs_read", expected=False)
    _exact_bool(policy["held_out_l3_evaluator_dispatched"], "held_out_policy.held_out_l3_evaluator_dispatched", expected=False)
    _exact_int(policy["scientific_evaluator_dispatch_count"], "held_out_policy.scientific_evaluator_dispatch_count", expected=0)
    _exact_string(policy["new_archive_scope"], "held_out_policy.new_archive_scope", expected="TEMPORARY_MOCK_ONLY")
    _exact_string(policy["s0_archive_access"], "held_out_policy.s0_archive_access", expected="READ_ONLY_SEALED_PUBLIC_SIX_CELL")
    _exact_bool(policy["canonical_result_created"], "held_out_policy.canonical_result_created", expected=False)
    _validate_repository_snapshot(payload["repository_snapshot"])

    entries = payload["pre_review_input_roles"]
    if type(entries) is not list or len(entries) != len(PRE_REVIEW_INPUT_ROLES) or len(entries) != 51:
        raise PrefreezeEvidenceError("pre_review_input_roles: exact 51-entry list required")
    roles: dict[str, dict[str, Any]] = {}
    paths: set[str] = set()
    for index, ((expected_role, expected_path), entry) in enumerate(zip(PRE_REVIEW_INPUT_ROLES, entries)):
        validated = _validate_role_entry(entry, expected_role, expected_path, f"pre_review_input_roles[{index}]")
        if expected_role in roles or expected_path in paths:
            raise PrefreezeEvidenceError("pre_review_input_roles: duplicate role/path")
        roles[expected_role] = validated
        paths.add(expected_path)

    tools = _exact_dict(payload["evidence_tool_bindings"], EVIDENCE_TOOL_BINDING_KEYS, "evidence_tool_bindings")
    expected_tools = {
        "producer": "scripts/build_r401_val_l3_a1_prefreeze_tests.py",
        "independent_checker": "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py",
        "focused_test": "tests/test_r401_val_l3_a1_prefreeze_tests.py",
    }
    tool_paths: set[str] = set()
    for name, expected_path in expected_tools.items():
        binding = _validate_file_binding(tools[name], expected_path, f"evidence_tool_bindings.{name}")
        if binding["path"] in tool_paths:
            raise PrefreezeEvidenceError("evidence_tool_bindings: duplicate path")
        tool_paths.add(binding["path"])

    results = payload["command_results"]
    if type(results) is not list or len(results) != len(COMMAND_SPECS):
        raise PrefreezeEvidenceError("command_results: exact ordered seven-entry list required")
    validated_results: list[dict[str, Any]] = []
    parsed_counts: dict[str, dict[str, int]] = {}
    last_started: datetime | None = None
    for index, result in enumerate(results):
        validated, counts = _validate_command_result(result, index, roles)
        started = _utc(validated["started_at_utc"], f"command_results[{index}].started_at_utc")
        if last_started is not None and started < last_started:
            raise PrefreezeEvidenceError("command_results: start timestamps are not ordered")
        if started > recorded_at:
            raise PrefreezeEvidenceError("command_results: command starts after record time")
        last_started = started
        validated_results.append(validated)
        if counts is not None:
            parsed_counts[validated["name"]] = counts

    _validate_prerequisites(payload["prerequisite_bindings"], roles, validated_results)

    totals = _exact_dict(payload["test_totals"], TEST_TOTALS_KEYS, "test_totals")
    by_name = {result["name"]: result for result in validated_results}
    for result_name, total_name in PYTEST_RESULT_TOTAL_NAMES.items():
        total = _exact_dict(totals[total_name], TEST_TOTAL_KEYS, f"test_totals.{total_name}")
        for key in PYTEST_COUNT_KEYS:
            _exact_int(total[key], f"test_totals.{total_name}.{key}", expected=parsed_counts[result_name][key])
        _exact_int(
            total["wall_duration_ms"], f"test_totals.{total_name}.wall_duration_ms",
            minimum=1, expected=by_name[result_name]["wall_duration_ms"],
        )

    if type(payload["covered_gates"]) is not list or payload["covered_gates"] != list(COVERED_GATES):
        raise PrefreezeEvidenceError("covered_gates: exact ordered list mismatch")
    _exact_string(payload["claim_boundary"], "claim_boundary", expected=CLAIM_BOUNDARY)

    encoded = canonical_json_bytes(payload)
    if not encoded.endswith(b"\n") or len(encoded) > MAX_CANDIDATE_BYTES:
        raise PrefreezeEvidenceError("role-11 candidate exceeds canonical size contract")


def validate_prefreeze_test_record_bytes(raw: bytes) -> dict[str, Any]:
    """Parse and replay one exact ``CJ_COMPACT_V1`` candidate image."""

    if type(raw) is not bytes or not raw or len(raw) > MAX_CANDIDATE_BYTES:
        raise PrefreezeEvidenceError("role-11 candidate byte-size contract mismatch")
    payload = strict_json_bytes(raw, "role-11 candidate")
    if raw != canonical_json_bytes(payload):
        raise PrefreezeEvidenceError("role-11 candidate is not CJ_COMPACT_V1")
    validate_prefreeze_test_record(payload)
    return payload


def build_prefreeze_test_record(
    *,
    recorded_at_utc: str,
    repository_snapshot: dict[str, Any],
    prerequisite_bindings: dict[str, Any],
    pre_review_input_roles: list[dict[str, Any]],
    evidence_tool_bindings: dict[str, Any],
    command_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Assemble a test-only candidate from internally captured evidence.

    The authoritative CLI does not accept these structures from a caller;
    this pure function exists so focused tests can exercise the closed schema.
    """

    test_totals: dict[str, Any] = {}
    for result in command_results:
        if type(result) is dict and result.get("name") in PYTEST_RESULT_TOTAL_NAMES:
            total_name = PYTEST_RESULT_TOTAL_NAMES[result["name"]]
            counts = result.get("pytest_counts")
            if type(counts) is dict:
                test_totals[total_name] = {
                    **counts,
                    "wall_duration_ms": result.get("wall_duration_ms"),
                }
    payload = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": ARTIFACT_ROLE,
        "artifact_status": ARTIFACT_STATUS,
        "authority": AUTHORITY,
        "recorded_at_utc": recorded_at_utc,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "held_out_policy": {
            "held_out_l3_scientific_outputs_read": False,
            "held_out_l3_evaluator_dispatched": False,
            "scientific_evaluator_dispatch_count": 0,
            "new_archive_scope": "TEMPORARY_MOCK_ONLY",
            "s0_archive_access": "READ_ONLY_SEALED_PUBLIC_SIX_CELL",
            "canonical_result_created": False,
        },
        "repository_snapshot": repository_snapshot,
        "prerequisite_bindings": prerequisite_bindings,
        "pre_review_input_roles": pre_review_input_roles,
        "evidence_tool_bindings": evidence_tool_bindings,
        "command_results": command_results,
        "test_totals": test_totals,
        "covered_gates": list(COVERED_GATES),
        "claim_boundary": CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    validate_prefreeze_test_record(payload)
    return payload


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _test_totals_locked() -> bool:
    return (
        type(EXPECTED_TEST_PASSED) is dict
        and set(EXPECTED_TEST_PASSED) == TEST_TOTALS_KEYS
        and all(
            type(EXPECTED_TEST_PASSED[name]) is int
            and EXPECTED_TEST_PASSED[name] > 0
            for name in TEST_TOTALS_KEYS
        )
    )


def _decode_transcript(raw: bytes, context: str) -> str:
    try:
        value = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise PrefreezeEvidenceError(f"{context}: transcript is not strict UTF-8") from error
    if "\x00" in value:
        raise PrefreezeEvidenceError(f"{context}: transcript contains NUL")
    return value


def _command_result_from_capture(
    *, index: int, argv: Sequence[str], started_at_utc: str,
    captured: BoundedCommand, roles: Mapping[str, dict[str, Any]],
) -> dict[str, Any]:
    name, kind = COMMAND_SPECS[index]
    stdout = _decode_transcript(captured.stdout, f"{name} stdout")
    stderr = _decode_transcript(captured.stderr, f"{name} stderr")
    if captured.return_code != 0:
        raise PrefreezeEvidenceError(f"{name}: nonzero return code")
    semantic: dict[str, Any] | None
    counts: dict[str, int] | None = None
    if name == "role24_machine_verify":
        semantic = {
            "verification_status": MACHINE_VERIFY_STATUS,
            "authority": VERIFY_AUTHORITY,
            "candidate_sha256": MACHINE_SHA256,
            "size_bytes": MACHINE_SIZE_BYTES,
            "promotion_authorized": False,
        }
    elif name == "role13_compatibility_verify":
        semantic = {
            "verification_status": ROLE13_VERIFY_STATUS,
            "authority": VERIFY_AUTHORITY,
            "candidate_sha256": ROLE13_SHA256,
            "size_bytes": ROLE13_SIZE_BYTES,
            "promotion_authorized": False,
        }
    elif name in PYTEST_RESULT_TOTAL_NAMES:
        semantic = None
        counts = _parse_pytest_counts(stdout, name)
    elif name == "git_diff_check":
        semantic = None
    else:
        semantic = strict_json_bytes(captured.stdout, "second rebuild receipt")
        _validate_second_rebuild_receipt(semantic, roles, "second rebuild receipt")
    result = {
        "name": name,
        "kind": kind,
        "argv": list(argv),
        "cwd": os.fspath(ROOT),
        "environment": dict(CLEAN_ENVIRONMENT),
        "return_code": captured.return_code,
        "started_at_utc": started_at_utc,
        "wall_duration_ms": captured.wall_duration_ms,
        "stdout_utf8": stdout,
        "stdout_sha256": hashlib.sha256(captured.stdout).hexdigest(),
        "stdout_size_bytes": len(captured.stdout),
        "stderr_utf8": stderr,
        "stderr_sha256": hashlib.sha256(captured.stderr).hexdigest(),
        "stderr_size_bytes": len(captured.stderr),
        "pytest_counts": counts,
        "semantic_receipt": semantic,
    }
    _validate_command_result(result, index, roles)
    return result


def _create_owned_rebuild_parent() -> tuple[Path, tuple[int, int]]:
    tmp_fd, tmp_chain = _open_absolute_directory(Path("/tmp"), "rebuild /tmp parent")
    created_name: str | None = None
    created_identity: tuple[int, int] | None = None
    committed = False
    try:
        for _attempt in range(32):
            name = "a416-l3a1-role11-rebuild." + os.urandom(16).hex()
            try:
                os.mkdir(name, 0o700, dir_fd=tmp_fd)
            except FileExistsError:
                continue
            created_name = name
            entry = os.stat(name, dir_fd=tmp_fd, follow_symlinks=False)
            created_identity = (entry.st_dev, entry.st_ino)
            if (
                not stat.S_ISDIR(entry.st_mode) or entry.st_uid != os.geteuid()
                or stat.S_IMODE(entry.st_mode) != 0o700
            ):
                raise PrefreezeEvidenceError("owned rebuild parent creation mismatch")
            os.fsync(tmp_fd)
            tmp_chain[-1] = _directory_identity(os.fstat(tmp_fd))
            _replay_open_directory(Path("/tmp"), tmp_fd, tmp_chain, "rebuild /tmp parent")
            committed = True
            return Path("/tmp") / name, (entry.st_dev, entry.st_ino)
        raise PrefreezeEvidenceError("exhausted rebuild parent collision attempts")
    finally:
        cleanup_error: BaseException | None = None
        if not committed and created_name is not None and created_identity is not None:
            try:
                current = os.stat(
                    created_name, dir_fd=tmp_fd, follow_symlinks=False
                )
            except FileNotFoundError:
                pass
            else:
                if (
                    not stat.S_ISDIR(current.st_mode)
                    or (current.st_dev, current.st_ino) != created_identity
                ):
                    cleanup_error = PrefreezeEvidenceError(
                        "refused to clean replaced rebuild parent"
                    )
                else:
                    try:
                        os.rmdir(created_name, dir_fd=tmp_fd)
                        os.fsync(tmp_fd)
                    except OSError as error:
                        cleanup_error = PrefreezeEvidenceError(
                            f"owned rebuild parent cleanup failed: {error}"
                        )
        os.close(tmp_fd)
        if cleanup_error is not None:
            raise cleanup_error


def _run_fixed_evidence_commands(
    roles: Mapping[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for index, (name, _kind) in enumerate(COMMAND_SPECS):
        rebuild_parent: Path | None = None
        rebuild_parent_identity: tuple[int, int] | None = None
        if name == "second_fresh_rebuild":
            rebuild_parent, rebuild_parent_identity = _create_owned_rebuild_parent()
            rebuild_output = rebuild_parent / REBUILD_OUTPUT_BASENAME
            argv = (*REBUILD_COMMAND_ARGV_PREFIX, os.fspath(rebuild_output))
        else:
            argv = FIXED_COMMAND_ARGV[name]
        started = _utc_now()
        try:
            captured = run_bounded_command(
                argv, timeout_seconds=COMMAND_TIMEOUT_SECONDS,
                stdout_cap=MAX_STDOUT_BYTES, stderr_cap=MAX_STDERR_BYTES,
            )
            result = _command_result_from_capture(
                index=index, argv=argv, started_at_utc=started,
                captured=captured, roles=roles,
            )
            results.append(result)
        finally:
            if rebuild_parent is not None and rebuild_parent.exists():
                assert rebuild_parent_identity is not None
                _remove_rebuild_parent(
                    rebuild_parent / REBUILD_OUTPUT_BASENAME,
                    rebuild_parent_identity,
                )
                raise PrefreezeEvidenceError(
                    "second rebuild wrapper left its owned temporary parent"
                )
    if len(results) != 7:
        raise PrefreezeEvidenceError("fixed evidence command count mismatch")
    return results


def _prerequisite_bindings(
    roles: Sequence[dict[str, Any]], command_results: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    by_role = {entry["role"]: entry for entry in roles}
    machine_receipt = command_results[0]["semantic_receipt"]
    role13_receipt = command_results[1]["semantic_receipt"]
    rebuild_receipt = command_results[6]["semantic_receipt"]
    return {
        "machine_role10": {
            **by_role["machine_freeze"],
            "publication_commit_oid": MACHINE_PUBLICATION_COMMIT,
            "producer_path": by_role["scheduler"]["path"],
            "producer_sha256": by_role["scheduler"]["sha256"],
            "verifier_path": by_role["release_builder"]["path"],
            "verifier_sha256": by_role["release_builder"]["sha256"],
            "verify_receipt": machine_receipt,
            "promotion_authorized": False,
        },
        "s0_compatibility_role13": {
            **by_role["s0_compatibility"],
            "publication_commit_oid": ROLE13_PUBLICATION_COMMIT,
            "producer_path": by_role["s0_adapter"]["path"],
            "producer_sha256": by_role["s0_adapter"]["sha256"],
            "verify_receipt": role13_receipt,
            "promotion_authorized": False,
        },
        "second_fresh_rebuild_replay": {
            "command_result_name": "second_fresh_rebuild",
            "command_result_sha256": hashlib.sha256(
                canonical_json_bytes(command_results[6])
            ).hexdigest(),
            "semantic_receipt": rebuild_receipt,
        },
        "canonical_absence": {
            "prefreeze_review_role12_exists": False,
            "main_freeze_role54_exists": False,
            "canonical_result_root_exists": False,
            "canonical_operational_root_exists": False,
        },
    }


def _candidate_output_path(value: str) -> Path:
    if type(value) is not str or not value or "\x00" in value:
        raise PrefreezeEvidenceError("temporary candidate path must be exact string")
    output = _absolute_lexical(Path(value), "temporary role11 candidate")
    pure = PurePosixPath(value)
    if (
        pure.parts[:2] != ("/", "tmp")
        or pure.parent.parent != PurePosixPath("/tmp")
    ):
        raise PrefreezeEvidenceError(
            "temporary role11 candidate must use one owned directory below /tmp"
        )
    try:
        output.relative_to(ROOT)
    except ValueError:
        pass
    else:
        raise PrefreezeEvidenceError("temporary role11 candidate must be outside project")
    if output.name in ("", ".", ".."):
        raise PrefreezeEvidenceError("temporary role11 candidate basename mismatch")
    return output


def _write_exclusive_candidate(output: Path, raw: bytes) -> FileImage:
    if not raw or len(raw) > MAX_CANDIDATE_BYTES:
        raise PrefreezeEvidenceError("temporary candidate size contract mismatch")
    parent_fd, parent_chain = _open_absolute_directory(
        output.parent, "temporary candidate parent"
    )
    descriptor: int | None = None
    owned_inode: tuple[int, int] | None = None
    committed = False
    try:
        parent_info = os.fstat(parent_fd)
        if (
            not stat.S_ISDIR(parent_info.st_mode)
            or parent_info.st_uid != os.geteuid()
            or stat.S_IMODE(parent_info.st_mode) != 0o700
            or parent_info.st_nlink != 2
            or os.listdir(parent_fd) != []
        ):
            raise PrefreezeEvidenceError(
                "temporary candidate parent must be an empty owned mode-0700 directory"
            )
        try:
            os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("temporary candidate already exists")
        descriptor = os.open(
            output.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_CLOEXEC", 0),
            0o600,
            dir_fd=parent_fd,
        )
        initial = os.fstat(descriptor)
        if (
            not stat.S_ISREG(initial.st_mode) or initial.st_nlink != 1
            or stat.S_IMODE(initial.st_mode) != 0o600
        ):
            raise PrefreezeEvidenceError("temporary candidate inode contract mismatch")
        owned_inode = (initial.st_dev, initial.st_ino)
        view = memoryview(raw)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise PrefreezeEvidenceError("temporary candidate short write")
            view = view[written:]
        os.fsync(descriptor)
        captured = _read_regular_at(
            parent_fd, output.name, "temporary candidate replay",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if (
            captured.raw != raw
            or (captured.device_id, captured.inode) != owned_inode
            or stat.S_IMODE(captured.mode) != 0o600
        ):
            raise PrefreezeEvidenceError("temporary candidate replay mismatch")
        os.fsync(parent_fd)
        parent_chain[-1] = _directory_identity(os.fstat(parent_fd))
        _replay_open_directory(
            output.parent, parent_fd, parent_chain, "temporary candidate parent"
        )
        committed = True
        return captured
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if not committed and owned_inode is not None:
            try:
                current = os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
            except FileNotFoundError:
                pass
            else:
                if (current.st_dev, current.st_ino) != owned_inode:
                    raise PrefreezeEvidenceError(
                        "refused to remove replaced temporary candidate inode"
                    )
                os.unlink(output.name, dir_fd=parent_fd)
                os.fsync(parent_fd)
        os.close(parent_fd)


def _remove_owned_candidate(output: Path, owned: FileImage) -> None:
    parent_fd, parent_chain = _open_absolute_directory(
        output.parent, "temporary candidate cleanup parent"
    )
    try:
        current = os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
        if (
            _stat_identity(current) != owned.identity
            or not stat.S_ISREG(current.st_mode) or current.st_nlink != 1
        ):
            raise PrefreezeEvidenceError(
                "refused to remove replaced temporary candidate inode"
            )
        os.unlink(output.name, dir_fd=parent_fd)
        os.fsync(parent_fd)
        try:
            os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("temporary candidate survived cleanup")
        parent_chain[-1] = _directory_identity(os.fstat(parent_fd))
        _replay_open_directory(
            output.parent, parent_fd, parent_chain,
            "temporary candidate cleanup parent",
        )
    finally:
        os.close(parent_fd)


def _capture_fault_hook(phase: str) -> None:
    """No-op production hook for the frozen final-candidate attack boundary."""

    if phase not in CAPTURE_HOOK_PHASES:
        raise PrefreezeEvidenceError(f"unknown capture failpoint: {phase}")


def capture_prefreeze_test_candidate(output_value: str) -> dict[str, Any]:
    """Internally run the frozen seven commands and write one /tmp candidate."""

    if not _test_totals_locked():
        raise PrefreezeEvidenceError(
            "exact stable pytest pass totals are not mechanically locked"
        )
    output = _candidate_output_path(output_value)
    assert_prefreeze_namespaces_absent()
    repository_snapshot = capture_repository_snapshot()
    roles = capture_pre_review_input_roles()
    tools = capture_evidence_tool_bindings()
    by_role = {entry["role"]: entry for entry in roles}
    if (
        by_role["machine_freeze"]["sha256"] != MACHINE_SHA256
        or by_role["machine_freeze"]["size_bytes"] != MACHINE_SIZE_BYTES
        or by_role["s0_compatibility"]["sha256"] != ROLE13_SHA256
        or by_role["s0_compatibility"]["size_bytes"] != ROLE13_SIZE_BYTES
    ):
        raise PrefreezeEvidenceError("canonical prerequisite raw identity mismatch")
    command_results = _run_fixed_evidence_commands(by_role)
    prerequisites = _prerequisite_bindings(roles, command_results)

    assert_prefreeze_namespaces_absent()
    replay_pre_review_input_roles(roles)
    replay_evidence_tool_bindings(tools)
    replay_repository_snapshot(repository_snapshot)
    recorded_at = _utc_now()
    payload = build_prefreeze_test_record(
        recorded_at_utc=recorded_at,
        repository_snapshot=repository_snapshot,
        prerequisite_bindings=prerequisites,
        pre_review_input_roles=roles,
        evidence_tool_bindings=tools,
        command_results=command_results,
    )
    raw = canonical_json_bytes(payload)
    validate_prefreeze_test_record_bytes(raw)

    assert_prefreeze_namespaces_absent()
    replay_pre_review_input_roles(roles)
    replay_evidence_tool_bindings(tools)
    replay_repository_snapshot(repository_snapshot)
    captured = _write_exclusive_candidate(output, raw)
    try:
        terminal_parent_fd, terminal_parent_chain = _open_absolute_directory(
            output.parent, "candidate terminal parent"
        )
        try:
            terminal_parent_identity = _relative_directory_identity(
                os.fstat(terminal_parent_fd)
            )
            terminal = _read_regular_at(
                terminal_parent_fd, output.name, "candidate terminal replay",
                maximum_bytes=MAX_CANDIDATE_BYTES,
            )
            _replay_open_directory(
                output.parent, terminal_parent_fd, terminal_parent_chain,
                "candidate terminal parent",
            )
            if terminal != captured:
                raise PrefreezeEvidenceError(
                    "temporary candidate changed after capture"
                )
            assert_prefreeze_namespaces_absent()
            replay_pre_review_input_roles(roles)
            replay_evidence_tool_bindings(tools)
            replay_repository_snapshot(repository_snapshot)
            _capture_fault_hook("BEFORE_FINAL_CANDIDATE_REPLAY")
            _replay_publication_candidate(
                candidate=output, parent_fd=terminal_parent_fd,
                parent_chain=terminal_parent_chain,
                parent_identity=terminal_parent_identity, expected=captured,
            )
        finally:
            os.close(terminal_parent_fd)
    except BaseException:
        _remove_owned_candidate(output, captured)
        raise
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "TEMP_PREFREEZE_TEST_CANDIDATE_RECEIPT",
        "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
        "authority": "NON_AUTHORITATIVE_CAPTURE_ONLY",
        "candidate_path": os.fspath(output),
        "candidate_sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "mode": "0600",
        "nlink": 1,
        "serializer": SERIALIZER,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def _publication_fault_hook(phase: str) -> None:
    """No-op production hook; tests may raise at a frozen crash boundary."""

    if phase not in PUBLICATION_HOOK_PHASES:
        raise PrefreezeEvidenceError(f"unknown publication failpoint: {phase}")


def _publication_stage_name() -> str:
    name = PUBLICATION_STAGE_PREFIX + os.urandom(16).hex()
    suffix = name.removeprefix(PUBLICATION_STAGE_PREFIX)
    if len(suffix) != 32 or any(character not in "0123456789abcdef" for character in suffix):
        raise PrefreezeEvidenceError("publication stage basename malformed")
    return name


def _rename_noreplace(parent_fd: int, source_name: str, destination_name: str) -> None:
    if sys.platform != "linux":
        raise PrefreezeEvidenceError("Linux renameat2(RENAME_NOREPLACE) is required")
    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = getattr(libc, "renameat2", None)
    if renameat2 is None:
        raise PrefreezeEvidenceError("renameat2(RENAME_NOREPLACE) is unavailable")
    renameat2.argtypes = [
        ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    ctypes.set_errno(0)
    result = renameat2(
        parent_fd, os.fsencode(source_name), parent_fd,
        os.fsencode(destination_name), 1,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in (errno.EEXIST, errno.ENOTEMPTY):
        raise PrefreezeEvidenceError("canonical role11 destination already exists")
    raise PrefreezeEvidenceError(
        "renameat2(RENAME_NOREPLACE) failed: " + os.strerror(error_number)
    )


def _write_all(descriptor: int, raw: bytes, context: str) -> None:
    view = memoryview(raw)
    while view:
        written = os.write(descriptor, view)
        if written <= 0:
            raise PrefreezeEvidenceError(f"{context}: short write")
        view = view[written:]


def _cleanup_publication_stage(
    parent_fd: int, name: str, owned_inode: tuple[int, int],
) -> None:
    try:
        current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    except OSError as error:
        raise PrefreezeEvidenceError(
            f"publication stage cleanup stat failed: {error}"
        ) from error
    if (
        not stat.S_ISREG(current.st_mode)
        or (current.st_dev, current.st_ino) != owned_inode
    ):
        raise PrefreezeEvidenceError(
            "refused to remove a replaced publication stage inode"
        )
    try:
        os.unlink(name, dir_fd=parent_fd)
        os.fsync(parent_fd)
    except OSError as error:
        raise PrefreezeEvidenceError(
            f"publication stage cleanup failed: {error}"
        ) from error


def _open_publication_candidate(
    candidate: Path,
) -> tuple[int, list[tuple[int, int, int, int]], tuple[int, int, int, int, int], FileImage, dict[str, Any]]:
    parent_fd, parent_chain = _open_absolute_directory(
        candidate.parent, "publication candidate parent"
    )
    try:
        parent_info = os.fstat(parent_fd)
        parent_identity = _relative_directory_identity(parent_info)
        if (
            not stat.S_ISDIR(parent_info.st_mode)
            or parent_info.st_uid != os.geteuid()
            or stat.S_IMODE(parent_info.st_mode) != 0o700
            or parent_info.st_nlink != 2
            or os.listdir(parent_fd) != [candidate.name]
        ):
            raise PrefreezeEvidenceError(
                "publication candidate parent must contain only one owned 0600 leaf"
            )
        image = _read_regular_at(
            parent_fd, candidate.name, "publication candidate",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if stat.S_IMODE(image.mode) != 0o600 or image.nlink != 1:
            raise PrefreezeEvidenceError("publication candidate mode/link mismatch")
        payload = validate_prefreeze_test_record_bytes(image.raw)
        _replay_open_directory(
            candidate.parent, parent_fd, parent_chain,
            "publication candidate parent",
        )
        return parent_fd, parent_chain, parent_identity, image, payload
    except BaseException:
        os.close(parent_fd)
        raise


def _replay_publication_candidate(
    *, candidate: Path, parent_fd: int,
    parent_chain: Sequence[tuple[int, int, int, int]],
    parent_identity: tuple[int, int, int, int, int], expected: FileImage,
) -> None:
    current_parent = os.fstat(parent_fd)
    if (
        _relative_directory_identity(current_parent) != parent_identity
        or os.listdir(parent_fd) != [candidate.name]
    ):
        raise PrefreezeEvidenceError("publication candidate parent changed")
    _replay_open_directory(
        candidate.parent, parent_fd, parent_chain,
        "publication candidate parent",
    )
    current = _read_regular_at(
        parent_fd, candidate.name, "publication candidate terminal replay",
        maximum_bytes=MAX_CANDIDATE_BYTES,
    )
    if current != expected:
        raise PrefreezeEvidenceError("publication candidate inode or bytes changed")


def _verify_candidate_independently(
    candidate: Path, expected_sha256: str, size_bytes: int,
) -> None:
    checker = ROOT / "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py"
    argv = (
        PYTHON, os.fspath(checker), "--verify-prefreeze-tests",
        os.fspath(candidate),
    )
    completed = run_bounded_command(
        argv, timeout_seconds=COMMAND_TIMEOUT_SECONDS,
        stdout_cap=MAX_STDOUT_BYTES, stderr_cap=MAX_STDERR_BYTES,
    )
    expected_stdout = (
        f"prefreeze_test_verification={PREFREEZE_VERIFY_STATUS} "
        f"authority={VERIFY_AUTHORITY} candidate_sha256={expected_sha256} "
        f"size_bytes={size_bytes} promotion_authorized=false\n"
    ).encode("utf-8")
    if (
        completed.return_code != 0 or completed.stderr != b""
        or completed.stdout != expected_stdout
    ):
        raise PrefreezeEvidenceError(
            "independent role11 checker did not return the exact PASS receipt"
        )


def _replay_live_publication_inputs(
    payload: Mapping[str, Any], *, untracked_paths: Sequence[Path],
) -> None:
    replay_pre_review_input_roles(payload["pre_review_input_roles"])
    replay_evidence_tool_bindings(payload["evidence_tool_bindings"])
    assert_downstream_namespaces_absent()
    if untracked_paths:
        replay_repository_snapshot_with_untracked(
            payload["repository_snapshot"], untracked_paths,
        )
    else:
        replay_repository_snapshot(payload["repository_snapshot"])


def _fsync_regular_at(
    parent_fd: int, name: str, expected_inode: tuple[int, int], context: str,
) -> None:
    descriptor = os.open(
        name,
        os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_CLOEXEC", 0),
        dir_fd=parent_fd,
    )
    try:
        info = os.fstat(descriptor)
        if (
            not stat.S_ISREG(info.st_mode) or info.st_nlink != 1
            or (info.st_dev, info.st_ino) != expected_inode
        ):
            raise PrefreezeEvidenceError(f"{context}: fsync inode mismatch")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def publish_prefreeze_test_record(
    *, candidate_value: str, expected_sha256: str, authority_root_value: str,
) -> dict[str, Any]:
    """Publish canonical role11 once, after independent zero-write verification."""

    if not _test_totals_locked():
        raise PrefreezeEvidenceError(
            "exact stable pytest pass totals are not mechanically locked"
        )
    expected_sha256 = _hash(expected_sha256, "expected role11 candidate SHA-256")
    authority_root = _absolute_lexical(
        Path(authority_root_value), "publication authority root"
    )
    if authority_root != _absolute_lexical(ROOT, "live Paper02 root"):
        raise PrefreezeEvidenceError(
            "publication authority root must equal exact live Paper02 root"
        )
    candidate = _candidate_output_path(candidate_value)
    destination = authority_root / CANONICAL_RELATIVE
    if candidate == destination:
        raise PrefreezeEvidenceError("publication candidate aliases canonical role11")

    candidate_parent_fd: int | None = None
    root_fd: int | None = None
    publication_parent_fd: int | None = None
    stage_fd: int | None = None
    stage_name: str | None = None
    stage_inode: tuple[int, int] | None = None
    renamed = False
    try:
        (
            candidate_parent_fd, candidate_parent_chain,
            candidate_parent_identity, candidate_image, payload,
        ) = _open_publication_candidate(candidate)
        if hashlib.sha256(candidate_image.raw).hexdigest() != expected_sha256:
            raise PrefreezeEvidenceError(
                "publication candidate SHA-256 differs from expected intent"
            )
        assert_prefreeze_namespaces_absent()
        _replay_live_publication_inputs(payload, untracked_paths=())
        _verify_candidate_independently(
            candidate, expected_sha256, candidate_image.size_bytes,
        )
        _replay_publication_candidate(
            candidate=candidate, parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            parent_identity=candidate_parent_identity, expected=candidate_image,
        )
        assert_prefreeze_namespaces_absent()
        _replay_live_publication_inputs(payload, untracked_paths=())

        root_fd, root_chain = _open_absolute_directory(
            authority_root, "publication authority root"
        )
        publication_parent_fd, publication_parent_chain = _open_absolute_directory(
            destination.parent, "role11 publication parent"
        )
        try:
            fcntl.flock(publication_parent_fd, PUBLICATION_LOCK_FLAGS)
        except OSError as error:
            if error.errno in (errno.EACCES, errno.EAGAIN):
                raise PrefreezeEvidenceError(
                    "role11 publication parent is locked by a concurrent publisher"
                ) from error
            raise PrefreezeEvidenceError(
                f"role11 publication parent lock failed: {error}"
            ) from error
        _replay_open_directory(
            authority_root, root_fd, root_chain, "publication authority root"
        )
        _replay_open_directory(
            destination.parent, publication_parent_fd, publication_parent_chain,
            "role11 publication parent",
        )
        try:
            os.stat(
                destination.name, dir_fd=publication_parent_fd,
                follow_symlinks=False,
            )
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("canonical role11 destination already exists")

        for _attempt in range(32):
            proposed = _publication_stage_name()
            try:
                stage_fd = os.open(
                    proposed,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL
                    | getattr(os, "O_NOFOLLOW", 0)
                    | getattr(os, "O_CLOEXEC", 0),
                    0o600,
                    dir_fd=publication_parent_fd,
                )
            except FileExistsError:
                continue
            except OSError as error:
                raise PrefreezeEvidenceError(
                    f"publication stage creation failed: {error}"
                ) from error
            stage_name = proposed
            initial_stage = os.fstat(stage_fd)
            if not stat.S_ISREG(initial_stage.st_mode) or initial_stage.st_nlink != 1:
                raise PrefreezeEvidenceError("publication stage inode contract mismatch")
            stage_inode = (initial_stage.st_dev, initial_stage.st_ino)
            break
        else:
            raise PrefreezeEvidenceError(
                "publication exhausted collision-safe stage names"
            )
        assert stage_fd is not None and stage_name is not None and stage_inode is not None

        _write_all(stage_fd, candidate_image.raw, "publication stage")
        _publication_fault_hook("AFTER_STAGE_WRITE")
        os.fchmod(stage_fd, 0o644)
        os.fsync(stage_fd)
        _publication_fault_hook("AFTER_STAGE_FILE_FSYNC")
        staged = _read_regular_at(
            publication_parent_fd, stage_name, "publication stage replay",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if (
            staged.raw != candidate_image.raw
            or (staged.device_id, staged.inode) != stage_inode
            or stat.S_IMODE(staged.mode) != 0o644
        ):
            raise PrefreezeEvidenceError("publication stage replay mismatch")
        os.fsync(publication_parent_fd)
        _publication_fault_hook("AFTER_STAGING_PARENT_FSYNC")

        _publication_fault_hook("BEFORE_TERMINAL_REPLAY")
        _replay_publication_candidate(
            candidate=candidate, parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            parent_identity=candidate_parent_identity, expected=candidate_image,
        )
        _replay_open_directory(
            authority_root, root_fd, root_chain, "publication authority root"
        )
        _replay_open_directory(
            destination.parent, publication_parent_fd, publication_parent_chain,
            "role11 publication parent",
        )
        terminal_stage = _read_regular_at(
            publication_parent_fd, stage_name, "terminal publication stage",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if terminal_stage != staged:
            raise PrefreezeEvidenceError("publication stage changed terminally")
        _replay_live_publication_inputs(
            payload, untracked_paths=(destination.parent / stage_name,),
        )

        _publication_fault_hook("BEFORE_RENAME")
        _replay_publication_candidate(
            candidate=candidate, parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            parent_identity=candidate_parent_identity, expected=candidate_image,
        )
        _replay_open_directory(
            authority_root, root_fd, root_chain, "publication authority root"
        )
        _replay_open_directory(
            destination.parent, publication_parent_fd, publication_parent_chain,
            "role11 publication parent",
        )
        final_stage = _read_regular_at(
            publication_parent_fd, stage_name, "publication boundary stage",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if final_stage != staged:
            raise PrefreezeEvidenceError("publication stage changed at rename boundary")
        _replay_live_publication_inputs(
            payload, untracked_paths=(destination.parent / stage_name,),
        )
        try:
            os.stat(
                destination.name, dir_fd=publication_parent_fd,
                follow_symlinks=False,
            )
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("canonical role11 appeared before rename")
        _rename_noreplace(publication_parent_fd, stage_name, destination.name)
        renamed = True
        _publication_fault_hook("AFTER_RENAME")

        try:
            os.stat(stage_name, dir_fd=publication_parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError("publication rename left stage entry")
        open_stage = os.fstat(stage_fd)
        if (
            not stat.S_ISREG(open_stage.st_mode) or open_stage.st_nlink != 1
            or stat.S_IMODE(open_stage.st_mode) != 0o644
            or (open_stage.st_dev, open_stage.st_ino) != stage_inode
            or open_stage.st_size != candidate_image.size_bytes
        ):
            raise PrefreezeEvidenceError("open stage inode changed after rename")
        published = _read_regular_at(
            publication_parent_fd, destination.name, "canonical role11",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if (
            published.raw != candidate_image.raw
            or (published.device_id, published.inode) != stage_inode
            or stat.S_IMODE(published.mode) != 0o644
            or hashlib.sha256(published.raw).hexdigest() != expected_sha256
        ):
            raise PrefreezeEvidenceError("canonical role11 postrename mismatch")
        _fsync_regular_at(
            publication_parent_fd, destination.name, stage_inode,
            "canonical role11",
        )
        _publication_fault_hook("AFTER_DESTINATION_FSYNC")
        os.fsync(publication_parent_fd)
        _publication_fault_hook("AFTER_PUBLICATION_PARENT_FSYNC")

        _replay_open_directory(
            authority_root, root_fd, root_chain, "publication authority root"
        )
        _replay_open_directory(
            destination.parent, publication_parent_fd, publication_parent_chain,
            "role11 publication parent",
        )
        lexical = secure_read_relative(
            os.fspath(CANONICAL_RELATIVE), "canonical role11 lexical replay",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if lexical != published:
            raise PrefreezeEvidenceError("canonical role11 lexical replay mismatch")
        validate_prefreeze_test_record_bytes(lexical.raw)
        _replay_publication_candidate(
            candidate=candidate, parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            parent_identity=candidate_parent_identity, expected=candidate_image,
        )
        _replay_live_publication_inputs(payload, untracked_paths=(destination,))
        _publication_fault_hook("AFTER_POSTPUBLICATION_REPLAY")

        # The final fault boundary is deliberately mutation-capable in the
        # attack tests.  Never issue a success receipt from evidence observed
        # before that boundary: reopen both the pinned and lexical namespaces
        # and bind the destination back to the exact staged inode/image.
        _replay_open_directory(
            authority_root, root_fd, root_chain, "publication authority root"
        )
        _replay_open_directory(
            destination.parent, publication_parent_fd, publication_parent_chain,
            "role11 publication parent",
        )
        try:
            os.stat(stage_name, dir_fd=publication_parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PrefreezeEvidenceError(
                "publication stage reappeared at final receipt boundary"
            )
        final_published = _read_regular_at(
            publication_parent_fd, destination.name,
            "canonical role11 final receipt replay",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if (
            final_published != published
            or (final_published.device_id, final_published.inode) != stage_inode
            or stat.S_IMODE(final_published.mode) != 0o644
            or final_published.nlink != 1
            or hashlib.sha256(final_published.raw).hexdigest() != expected_sha256
        ):
            raise PrefreezeEvidenceError(
                "canonical role11 changed at final receipt boundary"
            )
        final_lexical = secure_read_relative(
            os.fspath(CANONICAL_RELATIVE),
            "canonical role11 final lexical replay",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if final_lexical != final_published:
            raise PrefreezeEvidenceError(
                "canonical role11 final lexical replay mismatch"
            )
        _replay_publication_candidate(
            candidate=candidate, parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            parent_identity=candidate_parent_identity, expected=candidate_image,
        )
        _replay_live_publication_inputs(payload, untracked_paths=(destination,))
        terminal_published = _read_regular_at(
            publication_parent_fd, destination.name,
            "canonical role11 terminal receipt replay",
            maximum_bytes=MAX_CANDIDATE_BYTES,
        )
        if terminal_published != final_published:
            raise PrefreezeEvidenceError(
                "canonical role11 changed during final live replay"
            )

        verifier = payload["evidence_tool_bindings"]["independent_checker"]
        receipt = {
            "schema_version": SCHEMA_VERSION,
            "protocol_id": PROTOCOL_ID,
            "artifact_role": "PREFREEZE_TEST_PUBLICATION_RECEIPT",
            "artifact_status": PUBLICATION_STATUS,
            "authority": PUBLICATION_AUTHORITY,
            "candidate_path": os.fspath(candidate),
            "canonical_path": os.fspath(destination),
            "prefreeze_tests_sha256": expected_sha256,
            "size_bytes": candidate_image.size_bytes,
            "mode": "0644",
            "nlink": 1,
            "serializer": SERIALIZER,
            "publication_method": PUBLICATION_METHOD,
            "independent_verification_status": PREFREEZE_VERIFY_STATUS,
            "independent_verification_performed": True,
            "independent_verifier_path": verifier["path"],
            "independent_verifier_sha256": verifier["sha256"],
            "promotion_authorized": False,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        if set(receipt) != PUBLICATION_RECEIPT_KEYS:
            raise PrefreezeEvidenceError("publication receipt key set mismatch")
        canonical_json_bytes(receipt)
        return receipt
    finally:
        cleanup_error: BaseException | None = None
        if (
            publication_parent_fd is not None and stage_name is not None
            and stage_inode is not None and not renamed
        ):
            try:
                _cleanup_publication_stage(
                    publication_parent_fd, stage_name, stage_inode,
                )
            except BaseException as error:
                cleanup_error = error
        for descriptor in (
            stage_fd, publication_parent_fd, root_fd, candidate_parent_fd,
        ):
            if descriptor is not None:
                try:
                    os.close(descriptor)
                except OSError as error:
                    if cleanup_error is None:
                        cleanup_error = error
        if cleanup_error is not None:
            raise cleanup_error


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-prefreeze-tests", action="store_true")
    parser.add_argument("--publish-prefreeze-tests", action="store_true")
    parser.add_argument("--second-fresh-rebuild-only", action="store_true")
    parser.add_argument("--output")
    parser.add_argument("--candidate")
    parser.add_argument("--expected-sha256")
    parser.add_argument("--authority-root")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        modes = sum(
            bool(value)
            for value in (
                arguments.capture_prefreeze_tests,
                arguments.publish_prefreeze_tests,
                arguments.second_fresh_rebuild_only,
            )
        )
        if modes != 1:
            raise PrefreezeEvidenceError("exactly one producer mode is required")
        if arguments.second_fresh_rebuild_only:
            if (
                arguments.output is None or arguments.candidate is not None
                or arguments.expected_sha256 is not None
                or arguments.authority_root is not None
            ):
                raise PrefreezeEvidenceError(
                    "second rebuild requires only --output"
                )
            receipt = run_second_fresh_rebuild(arguments.output)
            sys.stdout.buffer.write(canonical_json_bytes(receipt))
            return 0
        if arguments.capture_prefreeze_tests:
            if (
                arguments.output is None or arguments.candidate is not None
                or arguments.expected_sha256 is not None
                or arguments.authority_root is not None
            ):
                raise PrefreezeEvidenceError(
                    "role11 capture requires only --output"
                )
            receipt = capture_prefreeze_test_candidate(arguments.output)
            sys.stdout.buffer.write(canonical_json_bytes(receipt))
            return 0
        if (
            arguments.output is not None or arguments.candidate is None
            or arguments.expected_sha256 is None
            or arguments.authority_root is None
        ):
            raise PrefreezeEvidenceError(
                "role11 publication requires --candidate, --expected-sha256, "
                "and --authority-root, without --output"
            )
        receipt = publish_prefreeze_test_record(
            candidate_value=arguments.candidate,
            expected_sha256=arguments.expected_sha256,
            authority_root_value=arguments.authority_root,
        )
        sys.stdout.buffer.write(canonical_json_bytes(receipt))
        return 0
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
