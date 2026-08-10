#!/usr/bin/env python3
"""Prospective L3-A1 scheduler framework.

This module implements strict matrix/run-binding plus complete mock-only
static and branch archive transactions.  The branch path can execute only an
explicit synthetic executable outside either result root; it reuses the
hardened bounded-process and branch-cell transaction runtime.  It also has a
formal *preflight* handshake which can snapshot the prospective 53 input
roles and write one visibly non-licensing, non-promotable run-config candidate
in an explicit noncanonical temporary root.  That handshake is not the future
production run config and cannot dispatch either evaluator.  Production
dispatch remains unconditionally disabled until the formal freeze schemas and
a separate execution-authorization contract are finalized.
"""

from __future__ import annotations

import argparse
import base64
import ctypes
import csv
import errno
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import shlex
import stat
import struct
import sys
import time
import types
import zlib
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, localcontext
from fractions import Fraction
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
L1_ACCEPTED_SUMMARY = ROOT / "results/r401_val_l1_branch/summary.json"
BRANCH_RUNTIME_PATH = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
MOCK_BRANCH_EVALUATOR = (
    ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"
)
STATIC_CHECKER_SOURCE = (
    ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
)
BRANCH_CHECKER_SOURCE = (
    ROOT / "scripts/check_r401_val_l3_a1_branch_independent.py"
)
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"
SCHEDULER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"
)
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
)
MACHINE_FREEZE = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
)
MAIN_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
PREFREEZE_REVIEW = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md"
)
CANONICAL_RESULT = ROOT / "results/r401_val_l3_all_slabs"
CANONICAL_OPERATIONAL = ROOT / "results/r401_val_l3_all_slabs.operational"

PROTOCOL_ID = "R401-VAL-L3-A1"
SCHEMA_VERSION = 1
PRECISIONS = (128, 256)
SLAB_IDS = tuple(f"S{index:03d}" for index in range(51))
COMPONENTS = ("STATIC", "BRANCH")
SCHEDULER_POLICY = "deterministic_component_barrier_batches_v1"
PREFREEZE_ACCEPT_LINE = "Verdict: ACCEPT_FOR_FREEZE"
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
GENERATION_STAGING_PATTERN = (
    r"^\.(S(?:00[0-9]|0[1-4][0-9]|050))\.tmp-([0-9a-f]{16})-"
    r"(0|[1-9][0-9]*)$"
)
STAGING_BASENAME = re.compile(GENERATION_STAGING_PATTERN)

MOCK_CLAIM_BOUNDARY = (
    "synthetic static/branch scheduler transaction only; no Arb/CAPD "
    "scientific evaluation, no component or local theorem, no global "
    "routing, trace, Hilbert-Polya, zeta-zero, or RH claim"
)
COMPOSITE_MOCK_CLAIM_BOUNDARY = (
    "mock 102-static plus 102-branch archive replay only; no scientific "
    "licensing, local theorem, global routing, trace-formula, Hilbert-Polya, "
    "zeta-zero, or RH promotion"
)
MOCK_CHECKER_STATUS = "PASS_MOCK_INDEPENDENT_REPLAY"
MOCK_POSTCHECK_STATUS = "PASS_MOCK_WRITE_ONCE_POSTCHECK"

FORMAL_PREFLIGHT_CLAIM_BOUNDARY = (
    "formal-control-plane implementation preflight only; exact prospective "
    "53-role hash handshake with no evaluator dispatch, no reusable production "
    "run configuration, no component or theorem status, and no Hilbert-Polya, "
    "zeta-zero, or RH claim"
)

# This order is the prospective 53-role order already frozen by the release
# contract.  It is duplicated deliberately: the scheduler must not import a
# release builder or checker in order to decide what it is allowed to bind.
FORMAL_INPUT_ROLES: tuple[tuple[str, str], ...] = (
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
    ("prefreeze_tests", "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json"),
    ("prefreeze_review", "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md"),
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

FORMAL_MAIN_FREEZE_REQUIRED_KEYS = frozenset(
    {
        "schema_version",
        "protocol_id",
        "artifact_role",
        "status",
        "authority",
        "scientific_licensing_enabled",
        "matrix",
        "matrix_id",
        "machine_freeze_sha256",
        "input_roles",
        "claim_boundary",
        "component_status",
        "milestone_status",
        "theorem_status",
        "final_status",
    }
)

MACHINE_FREEZE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "production_authorized", "capture", "machine_requirements",
    "machine_observations", "python_arb", "capd", "compiler",
    "branch_binary", "runtime_libraries", "resource_evidence",
    "resource_admission", "filesystem", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}
MACHINE_CAPTURE_KEYS = {
    "captured_at_utc", "capture_tool_path", "capture_tool_sha256",
    "boot_id_sha256",
}
MACHINE_REQUIREMENT_KEYS = {
    "logical_cpu_count", "memory_limit_bytes", "static_workers",
    "branch_workers", "memory_admission_limit_bytes", "reserve_bytes",
    "launch_free_bytes", "warning_free_bytes", "pause_free_bytes",
    "recovery_only_free_bytes",
}
MACHINE_OBSERVATION_KEYS = {
    "logical_cpu_count", "memory_limit_bytes", "result_parent_free_bytes",
    "idle_baseline_rss_bytes", "representative_static_peak_rss_bytes",
    "representative_branch_peak_rss_bytes",
}
MACHINE_RESOURCE_ADMISSION_KEYS = {
    "static_required_bytes", "branch_required_bytes", "admitted_required_bytes",
    "admission_limit_bytes", "static_inequality_passed",
    "branch_inequality_passed", "storage_launch_passed",
}
MACHINE_PYTHON_ARB_KEYS = {
    "executable_path", "executable_sha256", "python_version",
    "implementation", "python_flint_version", "flint_version", "arb_version",
    "conda_manifest_algorithm", "conda_manifest_file_count",
    "conda_installed_manifest_root_sha256",
    "python_flint_record_sha256",
    "python_flint_installed_manifest_root_sha256",
    "arb_extension", "fmpq_extension", "bundled_libraries",
}
CONDA_MANIFEST_ALGORITHM = "CONDA_META_LIVE_FILES_CJ_COMPACT_V1"
CONDA_MANIFEST_ROW_KEYS = {"kind", "mode", "path", "sha256", "size_bytes"}
CAPD_TREE_ALGORITHM = "GIT_INDEX_LIVE_TREE_CJ_COMPACT_V1"
CAPD_TREE_ROW_KEYS = {
    "git_blob_sha1", "mode", "path", "sha256", "size_bytes",
}
MACHINE_CAPD_KEYS = {
    "checkout_path", "commit", "tree_algorithm", "tree_sha256", "clean", "cmake_cache_path",
    "cmake_cache_sha256", "config_path", "config_sha256", "raw_flags",
    "raw_flags_sha256", "libcapd", "libfilib",
}
MACHINE_COMPILER_KEYS = {
    "executable_path", "executable_sha256", "version", "build_record",
}
MACHINE_BUILD_RECORD_KEYS = {
    "cwd", "environment", "umask", "argv", "argv_sha256", "stdout_sha256",
    "stderr_sha256", "stdout", "stderr", "return_code",
}
MACHINE_BRANCH_BINARY_KEYS = {
    "path", "sha256", "size_bytes", "executable_mode", "build_id", "source_path",
    "source_sha256", "elf_sha256", "dt_needed", "dt_needed_sha256",
    "runtime_libraries_sha256",
}
MACHINE_BRANCH_DT_NEEDED = [
    "libc.so.6", "libgcc_s.so.1", "libm.so.6", "libmpfr.so.6",
    "libstdc++.so.6",
]
MACHINE_PYTHON_BUNDLED_SONAMES = (
    "libflint-6839011d.so.24.0.0",
    "libgmp-e0c82b6b.so.10.5.0",
    "libmpfr-be332c05.so.6.2.2",
)
MACHINE_CAPD_SYSTEM_SONAMES = (
    "ld-linux-x86-64.so.2", "libc.so.6", "libgcc_s.so.1", "libgmp.so.10",
    "libm.so.6", "libmpfr.so.6", "libstdc++.so.6",
)
PYTHON_FLINT_RECORD_SHA256 = (
    "a140c3cb2ba819edc913c2adae2dc0a60d49f7f3be547f139b7beb8be9c0d3da"
)
PYTHON_FLINT_INSTALLED_FILE_COUNT = 139
PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256 = (
    "32a2b16585f81fe5cd4a4c3b7d0d70e0f867f1a032db4b9c3b0f414cf991c870"
)
MACHINE_PYTHON_VERSION = (
    "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) "
    "[GCC 11.2.0]"
)
MACHINE_COMPILER_VERSION = "g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
MACHINE_RUNTIME_LIBRARY_KEYS = {
    "soname", "path", "mode", "size_bytes", "sha256", "build_id",
}
MACHINE_RUNTIME_LIBRARIES_KEYS = {"python_bundled", "capd_system"}
MACHINE_EXTENSION_BINDING_KEYS = {"path", "mode", "size_bytes", "sha256", "build_id"}
MACHINE_RESOURCE_EVIDENCE_KEYS = {
    "static_payload_raw_utf8", "static_payload_sha256",
    "branch_payload_raw_utf8", "branch_payload_sha256",
    "persistent_binary_sha256",
}
STATIC_RESOURCE_PAYLOAD_KEYS = {
    "admission", "artifact_role", "bindings", "claim_boundary",
    "component_status", "concurrent_runs", "concurrent_schedule",
    "execution_environment", "final_status", "measurement",
    "milestone_status", "production_authorized", "project_root",
    "protocol_id", "schema_version", "scientific_licensing_enabled", "scope",
    "sequential_runs", "temporary_root", "theorem_status",
}
STATIC_RESOURCE_ADMISSION_KEYS = {
    "admission_limit_bytes", "formula", "headroom_bytes",
    "idle_baseline_bytes", "lhs_bytes", "passes",
    "representative_peak_rss_bytes", "reserve_bytes", "workers",
}
STATIC_RESOURCE_BINDINGS_KEYS = {
    "calibration_binding", "evaluator", "interpreter", "plan", "python_flint",
}
STATIC_RESOURCE_CALIBRATION_BINDING_KEYS = {
    "matrix_id", "nonfreeze_sha256", "nonrunconfig_sha256",
}
STATIC_RESOURCE_EVALUATOR_BINDING_KEYS = {"mode", "path", "sha256", "size_bytes"}
STATIC_RESOURCE_INTERPRETER_BINDING_KEYS = {
    "invocation_path", "resolved_path", "sha256", "size_bytes", "version",
}
STATIC_RESOURCE_PLAN_BINDING_KEYS = {"path", "public_slab_ids", "sha256"}
STATIC_RESOURCE_PYTHON_FLINT_KEYS = {
    "arb_extension_path", "arb_extension_sha256", "flint_version",
    "installed_manifest_sha256", "installed_record_file_count", "module_path",
    "record_path", "record_sha256", "version",
}
STATIC_RESOURCE_MEASUREMENT_KEYS = {
    "baseline_conservative_bytes", "baseline_samples_bytes", "bytes_per_kib",
    "cgroup_limit_bytes", "cgroup_limit_path", "cgroup_usage_path",
    "concurrent_peak_bytes", "concurrent_samples_bytes", "method",
    "ru_maxrss_unit", "sample_interval_seconds",
}
STATIC_RESOURCE_RUN_KEYS = {
    "argv", "component_status", "elapsed_seconds", "evaluator_status",
    "final_status", "label", "milestone_status", "output", "output_bytes",
    "output_sha256", "peak_rss_kib", "precision_bits", "replica",
    "returncode", "scientific_status", "slab_id", "stderr", "stderr_bytes",
    "stderr_empty", "stderr_sha256", "stdout", "stdout_bytes",
    "stdout_exact_status_line", "stdout_sha256", "system_cpu_seconds",
    "theorem_status", "user_cpu_seconds",
}
STATIC_RESOURCE_SCHEDULE_KEYS = {"precision_bits", "slab_id"}
BRANCH_RESOURCE_PAYLOAD_KEYS = {
    "admission", "baseline_conservative_bytes", "baseline_samples_bytes",
    "binary", "binary_sha256", "cgroup_limit_bytes", "final_status",
    "milestone_status", "per_process_peak_rss_max_kib", "post_samples_bytes",
    "results", "sampled_concurrent_increment_bytes",
    "sampled_concurrent_peak_bytes", "scientific_status", "scope",
    "task_count", "theorem_status",
}
BRANCH_RESOURCE_ADMISSION_KEYS = {
    "baseline_bytes", "formula", "headroom_bytes", "lhs_bytes", "limit_bytes",
    "passes", "peak_rss_bytes", "reserve_bytes", "workers",
}
BRANCH_RESOURCE_RUN_KEYS = {
    "abi_verified", "argv", "argv_count", "elapsed_seconds", "peak_rss_kib",
    "precision_bits", "returncode", "slab_id", "stderr_bytes",
    "stderr_sha256", "stdout_bytes", "stdout_sha256", "system_cpu_seconds",
    "terminal_abi_value", "user_cpu_seconds",
}
MACHINE_RESOURCE_SUMMARY_KEYS = {
    "scope", "baseline_bytes", "peak_rss_bytes", "workers", "reserve_bytes",
    "limit_bytes", "lhs_bytes", "headroom_bytes", "passes", "run_count",
}
MACHINE_RESOURCE_ROW_KEYS = {
    "precision_bits", "slab_id", "replica", "argv_count", "returncode",
    "peak_rss_kib", "stdout_bytes", "stdout_sha256", "stderr_bytes",
    "stderr_sha256", "abi_verified",
}
MACHINE_FILESYSTEM_KEYS = {
    "project_root", "result_parent", "operational_parent", "project_device_id",
    "result_device_id", "operational_device_id", "same_filesystem",
}

MAIN_FREEZE_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "matrix", "matrix_id", "input_roles",
    "machine_freeze_sha256", "prefreeze_review", "serializers", "scheduler",
    "limits", "status_tables", "evaluators", "checkers", "archive_layout",
    "machine_requirements", "failure_policy", "execution_policy",
    "claim_boundary", "component_status", "milestone_status", "theorem_status",
    "final_status",
}
PREFREEZE_REVIEW_BINDING_KEYS = {"path", "sha256", "verdict"}
SERIALIZER_KEYS = {"compact_json", "branch_pretty_json", "artifact_bindings"}
SERIALIZER_DEFINITION_KEYS = {
    "id", "sort_keys", "ensure_ascii", "allow_nan", "indent", "separators",
    "trailing_lf",
}
FORMAL_SCHEDULER_KEYS = {
    "policy", "component_order", "static_workers", "branch_workers",
    "static_barrier_size", "branch_barrier_size", "max_inflight_per_cell",
    "global_scientific_budget",
}
FORMAL_LIMIT_KEYS = {"static", "branch", "admission"}
FORMAL_STATIC_LIMIT_KEYS = {
    "max_depth_per_tree", "max_nodes_per_tree", "max_nodes_per_cell",
    "timeout_ms", "total_cell_bytes",
}
FORMAL_BRANCH_LIMIT_KEYS = {
    "timeout_ms", "term_grace_ms", "pipe_close_grace_ms", "stdout_bytes",
    "stderr_bytes", "record_bytes", "total_cell_bytes", "phase_cells",
    "taylor_order", "tolerance_128", "tolerance_256",
}
FORMAL_ADMISSION_LIMIT_KEYS = {
    "memory_pause_bytes", "launch_free_bytes", "warning_free_bytes",
    "pause_free_bytes", "recovery_only_free_bytes",
}
STATUS_TABLE_KEYS = {"static_evaluator", "branch_evaluator", "scheduler"}
STATUS_ENTRY_KEYS = {"status", "return_code", "promotion"}
SCHEDULER_STATUS_ENTRY_KEYS = {"classification", "evaluator_status_required", "promotion"}
EVALUATOR_BINDING_KEYS = {"static", "branch"}
STATIC_EVALUATOR_BINDING_KEYS = {"path", "sha256", "abi", "argv_count"}
BRANCH_EVALUATOR_BINDING_KEYS = {
    "source_path", "source_sha256", "binary_path", "binary_sha256",
    "runtime_path", "runtime_sha256", "abi", "argv_count",
}
CHECKER_BINDING_KEYS = {"static", "branch", "composite", "release_builder"}
CODE_BINDING_KEYS = {"path", "sha256"}
ARCHIVE_LAYOUT_KEYS = {
    "authoritative_relative", "operational_suffix", "static_cell_files",
    "branch_cell_files", "static_serializer", "branch_serializer",
    "aggregate_serializer",
}
FAILURE_POLICY_KEYS = {
    "stop_after_current_barrier", "retry_same_generation",
    "aggregate_requires_certified_cells", "quarantine_on_corrupt_recovery",
}
EXECUTION_POLICY_KEYS = {
    "initialize_only_writes_run_config", "execute_requires_existing_config",
    "execute_requires_resume", "explicit_execution_flags",
    "config_self_authorizes", "branch_millisecond_migration_complete",
}

FINAL_RUN_CONFIG_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "scientific_licensing_enabled", "dispatch_authorized_by_artifact",
    "matrix", "matrix_id", "freeze_sha256", "main_freeze_sha256",
    "main_freeze", "machine_freeze", "prefreeze_review", "input_roles",
    "serializers", "scheduler", "limits", "status_tables", "evaluators",
    "checkers", "archive_layout", "machine_requirements", "execution_policy",
    "paths", "filesystem_identity", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
FINAL_RUN_PATH_KEYS = {"authoritative_root", "operational_root"}
FINAL_FILESYSTEM_KEYS = {
    "authoritative_parent_device_id", "operational_parent_device_id",
    "same_filesystem",
}

STATIC_PROOF_SENTINEL_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority", "matrix_id",
    "freeze_sha256", "main_freeze_sha256", "run_config_sha256", "cell",
    "scheduler_classification", "evaluator_status", "reason_code",
    "scientific_licensing_enabled", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}

FORMAL_STATIC_PROOF_COMMON_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "scientific_licensing_enabled", "matrix_id", "freeze_sha256",
    "run_config_sha256", "component_status", "milestone_status",
    "theorem_status", "final_status", "evaluator_status", "slab_id",
    "precision_bits", "epsilon", "period_window", "input_echo",
    "claim_boundary", "proof_complete", "trees", "counts",
    "proof_content_hash_definition", "proof_content_sha256",
}
FORMAL_STATIC_PASS_PROOF_KEYS = FORMAL_STATIC_PROOF_COMMON_KEYS | {
    "outer_containment", "source_bindings",
}
FORMAL_STATIC_NONPASS_PROOF_KEYS = FORMAL_STATIC_PROOF_COMMON_KEYS | {
    "failure",
}
FORMAL_STATIC_INPUT_ECHO_KEYS = {
    "slab_id", "precision_bits", "epsilon_lower", "epsilon_upper",
    "matrix_id", "freeze_sha256", "run_config_sha256",
    "plan_record_sha256", "max_depth", "max_nodes_per_tree",
    "max_nodes_per_cell",
}
FORMAL_STATIC_SOURCE_BINDING_KEYS = {
    "evaluator_sha256", "checker_sha256", "l1_final_plan_sha256",
    "l1_release_chain_sha256",
}
FORMAL_STATIC_L1_SOURCE_ROLES = (
    "l1_release", "l1_summary", "l1_manifest", "l1_checker", "l1_postcheck",
)

FORMAL_STATIC_RECORD_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "scientific_licensing_enabled", "matrix_id", "freeze_sha256",
    "main_freeze_sha256", "run_config_sha256", "cell", "task",
    "semantic_invocation", "scheduler_result", "evaluator_result", "files",
    "limits", "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}
FORMAL_STATIC_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "scientific_licensing_enabled", "matrix_id", "freeze_sha256",
    "main_freeze_sha256", "run_config_sha256", "cell",
    "semantic_invocation_sha256", "scheduler_classification",
    "evaluator_status", "record", "files", "claim_boundary",
    "component_status", "milestone_status", "theorem_status", "final_status",
}
FORMAL_STATIC_TASK_KEYS = {"epsilon_lower", "epsilon_upper", "plan_record_sha256"}
FORMAL_STATIC_INVOCATION_KEYS = {
    "argv", "argv_sha256", "exact_string_count", "output_token",
}
FORMAL_STATIC_SCHEDULER_RESULT_KEYS = {
    "classification", "evaluator_status", "return_code", "proof_kind",
    "reason_code",
}
FORMAL_STATIC_EVALUATOR_RESULT_KEYS = {"status", "return_code", "status_line_count"}
FORMAL_STATIC_FILE_BINDING_KEYS = {
    "path", "sha256", "size_bytes", "serializer", "truncated",
}
FORMAL_STATIC_FILE_NAMES = ("proof.json", "stdout.txt", "stderr.txt", "record.json")
FORMAL_STATIC_PROOF_KINDS = {
    "EVALUATOR_PROOF", "INVALID_EVALUATOR_PROOF", "SCHEDULER_NO_PROOF_SENTINEL",
}
FORMAL_STATIC_STATUS_CODES = {
    "STATIC_CELL_CERTIFIED": 0,
    "STATIC_UNRESOLVED_DEPTH": 2,
    "STATIC_UNRESOLVED_NODE_BUDGET": 2,
    "STATIC_INTERVAL_FAIL": 3,
    "INVALID_STATIC_PROOF_CONTRACT": 5,
}
FORMAL_STATIC_CLASSIFICATIONS = {
    "COMMITTED_EVALUATOR_RESULT", "CELL_TIMEOUT", "CELL_SIGNAL",
    "CELL_OUTPUT_BUDGET_EXHAUSTED", "MALFORMED_EVALUATOR_OUTPUT",
    "PROVENANCE_INVALID",
}
FORMAL_STATIC_SENTINEL_REASONS = {
    "CELL_TIMEOUT": "TIMEOUT",
    "CELL_SIGNAL": "SIGNAL",
    "CELL_OUTPUT_BUDGET_EXHAUSTED": "OUTPUT_BUDGET",
    "PROVENANCE_INVALID": "PROVENANCE",
    "MALFORMED_EVALUATOR_OUTPUT": "NO_EVALUATOR_PROOF",
}
FORMAL_AGGREGATE_COMMON_KEYS = {
    "schema_version", "protocol_id", "artifact_status", "authority",
    "scientific_licensing_enabled", "matrix_id", "freeze_sha256",
    "main_freeze_sha256", "run_config_sha256", "ordered_cell_manifest_root",
    "evaluator_roles", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
FORMAL_AGGREGATE_SUMMARY_KEYS = FORMAL_AGGREGATE_COMMON_KEYS | {
    "artifact_role", "matrix", "cell_count", "status_counts",
    "scheduler_classification_counts",
}
FORMAL_AGGREGATE_MANIFEST_KEYS = FORMAL_AGGREGATE_COMMON_KEYS | {
    "artifact_role", "cell_manifests", "summary",
}

MACHINE_CLAIM_BOUNDARY = (
    "machine, toolchain, persistent-binary, filesystem, and representative "
    "resource admission only; no evaluator dispatch, component status, local "
    "theorem, global routing, Hilbert-Polya, zeta-zero, or RH claim"
)
RESOURCE_EVIDENCE_CLAIM_BOUNDARY = (
    "representative public-cell resource calibration only; recorded paths are "
    "inert evidence and no held-out scientific result or production authority is claimed"
)
MAIN_FREEZE_CLAIM_BOUNDARY = (
    "exact control-plane and ordered 53-role pre-freeze authority only; no "
    "evaluator result, component status, theorem, Hilbert-Polya, zeta-zero, or RH claim"
)
FORMAL_RUN_CONFIG_CLAIM_BOUNDARY = (
    "write-once formal run binding only; the artifact never self-authorizes "
    "scientific dispatch or any component, theorem, Hilbert-Polya, zeta-zero, or RH claim"
)
FORMAL_STATIC_CELL_CLAIM_BOUNDARY = (
    "producer-only static phase-anchor cell conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no component, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
FORMAL_AGGREGATE_CLAIM_BOUNDARY = (
    "complete 102-cell producer archive only; independent component replay "
    "remains required and no component, theorem, Hilbert-Polya, zeta-zero, or RH status is assigned"
)


def _load_branch_runtime() -> Any:
    """Load the import-only runtime under one stable module identity."""

    name = "r401_val_l3_a1_branch_runtime_scheduler"
    existing = sys.modules.get(name)
    if existing is not None:
        return existing
    spec = importlib.util.spec_from_file_location(name, BRANCH_RUNTIME_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the prospective branch runtime")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_BRANCH_RUNTIME_MODULE: Any | None = None
_FORMAL_BRANCH_RUNTIME_MODULES: dict[str, Any] = {}
_ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS: dict[
    Path,
    tuple[
        tuple[int, int, int, int, int],
        Path,
        bytes,
        tuple[int, int, int, int, int],
    ],
] | None = None


def _branch_runtime() -> Any:
    global _BRANCH_RUNTIME_MODULE
    if _BRANCH_RUNTIME_MODULE is None:
        _BRANCH_RUNTIME_MODULE = _load_branch_runtime()
    return _BRANCH_RUNTIME_MODULE


def _formal_runtime_module_name(raw_sha256: str) -> str:
    if type(raw_sha256) is not str or HEX_SHA256.fullmatch(raw_sha256) is None:
        raise ProductionAuthorityError("formal runtime SHA-256 is malformed")
    return f"r401_val_l3_a1_branch_runtime_formal_{raw_sha256}"


def _load_formal_branch_runtime(record: "FormalRoleRecord") -> Any:
    """Compile the cross-bound captured runtime bytes without reopening a path."""

    if record.role != "branch_runtime" or sha256_bytes(record.raw) != record.sha256:
        raise ProductionAuthorityError("captured formal runtime hash binding mismatch")
    name = _formal_runtime_module_name(record.sha256)
    existing = sys.modules.get(name)
    if existing is not None:
        if getattr(existing, "__formal_runtime_sha256__", None) != record.sha256:
            raise ProductionAuthorityError("pre-cached formal runtime lacks exact SHA binding")
        cached = _FORMAL_BRANCH_RUNTIME_MODULES.get(record.sha256)
        if cached is not existing:
            raise ProductionAuthorityError("formal runtime cache identity mismatch")
        return existing
    if record.sha256 in _FORMAL_BRANCH_RUNTIME_MODULES:
        raise ProductionAuthorityError("formal runtime cache lost its module identity")
    try:
        source = record.raw.decode("utf-8")
    except UnicodeError as error:
        raise ProductionAuthorityError("captured formal runtime is not UTF-8") from error
    origin = str(BRANCH_RUNTIME_PATH)
    module = types.ModuleType(name)
    module.__file__ = origin
    module.__package__ = ""
    module.__loader__ = None
    module.__spec__ = importlib.util.spec_from_loader(name, loader=None, origin=origin)
    module.__formal_runtime_sha256__ = record.sha256
    sys.modules[name] = module
    try:
        exec(compile(source, origin, "exec", dont_inherit=True), module.__dict__)
    except BaseException:
        if sys.modules.get(name) is module:
            del sys.modules[name]
        raise
    if module.__file__ != origin or getattr(module, "__formal_runtime_sha256__", None) != record.sha256:
        if sys.modules.get(name) is module:
            del sys.modules[name]
        raise ProductionAuthorityError("formal runtime mutated fixed origin/hash metadata")
    _FORMAL_BRANCH_RUNTIME_MODULES[record.sha256] = module
    return module


class SchedulerContractError(RuntimeError):
    """Base fail-closed scheduler error."""


class StrictJSONError(SchedulerContractError):
    """Strict JSON or type contract failure."""


class PathContractError(SchedulerContractError):
    """Unsafe, aliased, linked, or off-filesystem path."""


class ProductionAuthorityError(SchedulerContractError):
    """Missing or invalid production authority."""


class RunBindingMismatch(SchedulerContractError):
    """Resume binding differs from the sealed run config."""


class CorruptGeneration(SchedulerContractError):
    """Published or staged generation bytes fail validation."""


class SyntheticCrash(RuntimeError):
    """Test-only crash injected after the canonical cell rename."""


class SyntheticQuarantineCrash(RuntimeError):
    """Test-only crash injected at a durable quarantine boundary."""


@dataclass(frozen=True)
class FormalRoleRecord:
    role: str
    path: str
    sha256: str
    raw: bytes
    stat_identity: tuple[int, int, int, int, int]

    def payload(self) -> dict[str, str]:
        return {"role": self.role, "path": self.path, "sha256": self.sha256}


@dataclass(frozen=True)
class FormalAuthoritySnapshot:
    """One pinned, non-dispatching image of the prospective formal authority.

    The exact schemas of the future machine and main freezes are not yet
    contractual.  Consequently this object proves only the required semantic
    envelope and exact ordered 53-role hash handshake.  It never represents
    execution authorization.
    """

    authority_root: Path
    main_freeze_path: Path
    main_freeze_sha256: str
    machine_freeze_path: Path
    machine_freeze_sha256: str
    prefreeze_review_path: Path
    prefreeze_review_sha256: str
    input_roles: tuple[FormalRoleRecord, ...]
    main_freeze_raw: bytes
    main_freeze_stat_identity: tuple[int, int, int, int, int]
    machine_freeze_raw: bytes


@dataclass(frozen=True)
class FormalStaticTransactionPlan:
    """Pure formal static transaction description; it cannot execute."""

    cell: "CellKey"
    evaluator_path: Path
    evaluator_sha256: str
    proof_path: Path
    stdout_path: Path
    stderr_path: Path
    record_path: Path
    argv: tuple[str, ...]
    semantic_argv: tuple[str, ...]
    semantic_argv_sha256: str
    checker_sha256: str
    l1_final_plan_sha256: str
    l1_release_chain_sha256: tuple[tuple[str, str], ...]
    matrix_id: str
    freeze_sha256: str
    main_freeze_sha256: str
    run_config_sha256: str

    def validate(self) -> None:
        if self.freeze_sha256 != self.main_freeze_sha256:
            raise ProductionAuthorityError(
                "static freeze_sha256/main_freeze_sha256 mismatch"
            )
        for value in (
            self.evaluator_sha256,
            self.checker_sha256,
            self.l1_final_plan_sha256,
            self.matrix_id,
            self.freeze_sha256,
            self.main_freeze_sha256,
            self.run_config_sha256,
        ):
            if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
                raise ProductionAuthorityError("static transaction hash is malformed")
        expected_l1_paths = tuple(
            dict(FORMAL_INPUT_ROLES)[role]
            for role in FORMAL_STATIC_L1_SOURCE_ROLES
        )
        if (
            type(self.l1_release_chain_sha256) is not tuple
            or tuple(path for path, _digest in self.l1_release_chain_sha256)
            != expected_l1_paths
            or any(
                type(item) is not tuple
                or len(item) != 2
                or type(item[0]) is not str
                or type(item[1]) is not str
                or HEX_SHA256.fullmatch(item[1]) is None
                for item in self.l1_release_chain_sha256
            )
        ):
            raise ProductionAuthorityError(
                "static transaction L1 source-binding chain is malformed"
            )
        if self.matrix_id != canonical_matrix_id():
            raise ProductionAuthorityError("static transaction matrix binding mismatch")
        if len(self.argv) != 26 or not all(type(item) is str for item in self.argv):
            raise SchedulerContractError("static process argv must be exactly 26 strings")
        if self.argv[0] != sys.executable or self.argv[1] != str(self.evaluator_path):
            raise SchedulerContractError("static interpreter/evaluator argv binding mismatch")
        evaluator_raw, _ = read_pinned_regular_file(self.evaluator_path)
        if sha256_bytes(evaluator_raw) != self.evaluator_sha256:
            raise ProductionAuthorityError("static evaluator changed after plan construction")
        if len(self.semantic_argv) != 26 or not all(
            type(item) is str for item in self.semantic_argv
        ):
            raise SchedulerContractError("static semantic argv must be exactly 26 strings")
        if self.argv[-1] != str(self.proof_path):
            raise SchedulerContractError("static evaluator output is not the planned proof")
        if (
            self.argv[:-1] != self.semantic_argv[:-1]
            or self.semantic_argv[-1] != "<STAGING_PROOF_PATH>"
            or self.semantic_argv_sha256
            != sha256_bytes(canonical_json_bytes(list(self.semantic_argv)))
        ):
            raise SchedulerContractError("static semantic invocation binding mismatch")
        if tuple(path.name for path in (
            self.proof_path, self.stdout_path, self.stderr_path, self.record_path
        )) != ("proof.json", "stdout.txt", "stderr.txt", "record.json"):
            raise SchedulerContractError("formal static provisional archive shape mismatch")

    def expected_source_bindings(self) -> dict[str, Any]:
        """Return the exact evaluator provenance object expected in a pass proof."""

        return {
            "evaluator_sha256": self.evaluator_sha256,
            "checker_sha256": self.checker_sha256,
            "l1_final_plan_sha256": self.l1_final_plan_sha256,
            "l1_release_chain_sha256": dict(self.l1_release_chain_sha256),
        }


@dataclass(frozen=True)
class FormalBranchTransactionPlan:
    """Pure formal branch transaction description; it cannot execute."""

    task: Any
    evaluator_source_path: Path
    evaluator_source_sha256: str
    evaluator_binary_path: Path
    evaluator_binary_sha256: str
    freeze_sha256: str
    main_freeze_sha256: str
    run_config_sha256: str

    def validate(self) -> None:
        if self.freeze_sha256 != self.main_freeze_sha256:
            raise ProductionAuthorityError(
                "branch freeze_sha256/main_freeze_sha256 mismatch"
            )
        for value in (
            self.evaluator_source_sha256,
            self.evaluator_binary_sha256,
            self.freeze_sha256,
            self.main_freeze_sha256,
            self.run_config_sha256,
        ):
            if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
                raise ProductionAuthorityError("branch transaction hash is malformed")
        self.task.validate()
        if self.task.evaluator_binary_path != str(self.evaluator_binary_path):
            raise ProductionAuthorityError("branch task binary path is not frozen")


@dataclass(frozen=True, order=True)
class CellKey:
    precision_bits: int
    slab_id: str

    def __post_init__(self) -> None:
        if type(self.precision_bits) is not int or self.precision_bits not in PRECISIONS:
            raise SchedulerContractError("invalid precision")
        if type(self.slab_id) is not str or self.slab_id not in SLAB_IDS:
            raise SchedulerContractError("invalid slab id")

    @property
    def label(self) -> str:
        return f"{self.precision_bits}:{self.slab_id}"

    def payload(self) -> dict[str, Any]:
        return {
            "precision_bits": self.precision_bits,
            "slab_id": self.slab_id,
        }


def exact_matrix() -> tuple[CellKey, ...]:
    return tuple(CellKey(bits, slab) for bits in PRECISIONS for slab in SLAB_IDS)


def matrix_payload() -> list[dict[str, Any]]:
    return [cell.payload() for cell in exact_matrix()]


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJSONError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise StrictJSONError(f"nonfinite JSON constant: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise StrictJSONError(f"nonfinite JSON number: {value}")
    return parsed


def strict_json_loads(raw: str) -> Any:
    try:
        return json.loads(
            raw,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except StrictJSONError:
        raise
    except (ValueError, TypeError, json.JSONDecodeError) as error:
        raise StrictJSONError(f"invalid JSON: {error}") from error


def strict_json_load(
    path: Path,
    *,
    reject_hardlink: bool = True,
    require_canonical: bool = False,
) -> Any:
    return strict_json_image(
        path,
        reject_hardlink=reject_hardlink,
        require_canonical=require_canonical,
    )[0]


def strict_json_image(
    path: Path,
    *,
    reject_hardlink: bool = True,
    require_canonical: bool = False,
) -> tuple[Any, bytes, os.stat_result]:
    raw_bytes, info = read_pinned_regular_file(
        path,
        reject_hardlink=reject_hardlink,
    )
    try:
        raw = raw_bytes.decode("utf-8")
    except UnicodeError as error:
        raise StrictJSONError(f"non-UTF8 JSON: {path}") from error
    payload = strict_json_loads(raw)
    if require_canonical and raw_bytes != canonical_json_bytes(payload):
        raise StrictJSONError(f"noncanonical JSON bytes: {path}")
    return payload, raw_bytes, info


def _require_exact_json_value(value: Any, context: str = "$") -> None:
    """Restrict serializers to the frozen JSON data model, without aliases."""

    if value is None or type(value) in (bool, str, int):
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise StrictJSONError(f"{context}: non-finite JSON number")
        return
    if type(value) is list:
        for index, item in enumerate(value):
            _require_exact_json_value(item, f"{context}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise StrictJSONError(
                    f"{context}: JSON object key is not an exact string"
                )
            _require_exact_json_value(item, f"{context}.{key}")
        return
    raise StrictJSONError(
        f"{context}: unsupported exact JSON value type {type(value).__name__}"
    )


def canonical_json_bytes(payload: Any) -> bytes:
    _require_exact_json_value(payload)
    try:
        return (
            json.dumps(
                payload,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise StrictJSONError(f"payload is not canonical JSON: {error}") from error


def pretty_json_bytes(payload: Any) -> bytes:
    """Return the branch calibration/runtime pretty serializer domain."""

    _require_exact_json_value(payload)
    try:
        return (
            json.dumps(
                payload,
                sort_keys=True,
                indent=2,
                ensure_ascii=False,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise StrictJSONError(f"payload is not pretty canonical JSON: {error}") from error


def exact_json_equal(actual: Any, expected: Any) -> bool:
    if type(actual) is not type(expected):
        return False
    if isinstance(actual, dict):
        return (
            set(actual) == set(expected)
            and all(exact_json_equal(actual[key], expected[key]) for key in actual)
        )
    if isinstance(actual, list):
        return len(actual) == len(expected) and all(
            exact_json_equal(left, right) for left, right in zip(actual, expected)
        )
    return actual == expected


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    raw, _ = read_pinned_regular_file(path, reject_hardlink=False)
    return hashlib.sha256(raw).hexdigest()


def canonical_matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(matrix_payload()))


def exact_int(value: Any, context: str, *, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise StrictJSONError(f"{context} must be an exact integer >= {minimum}")
    return value


def exact_keys(payload: Mapping[str, Any], expected: set[str], context: str) -> None:
    if type(payload) is not dict or set(payload) != expected:
        actual = set(payload) if isinstance(payload, dict) else type(payload).__name__
        raise StrictJSONError(f"{context} key set mismatch: {actual}")


def safe_relative_path(value: str) -> PurePosixPath:
    if type(value) is not str or not value:
        raise PathContractError("relative path must be a nonempty string")
    if "\\" in value or value.startswith("/") or "//" in value:
        raise PathContractError(f"unsafe path: {value}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise PathContractError(f"unsafe path: {value}")
    if path.as_posix() != value or value.endswith("/"):
        raise PathContractError(f"noncanonical path: {value}")
    return path


def safe_absolute_path(value: str, context: str) -> Path:
    if type(value) is not str or not value.startswith("/"):
        raise PathContractError(f"{context} must be an absolute POSIX path string")
    if "\\" in value or "//" in value or value.endswith("/"):
        raise PathContractError(f"noncanonical {context}: {value}")
    pure = PurePosixPath(value)
    if any(part in {"", ".", ".."} for part in pure.parts[1:]):
        raise PathContractError(f"unsafe {context}: {value}")
    if pure.as_posix() != value:
        raise PathContractError(f"noncanonical {context}: {value}")
    return Path(value)


def reject_symlink_components(path: Path, *, allow_missing_leaf: bool = True) -> None:
    candidate = path.absolute()
    parts = candidate.parts
    current = Path(parts[0])
    for part in parts[1:]:
        current = current / part
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            if allow_missing_leaf:
                return
            raise PathContractError(f"missing path component: {current}")
        if stat.S_ISLNK(mode):
            raise PathContractError(f"symlink path component: {current}")


def require_regular_file(path: Path, *, reject_hardlink: bool = True) -> None:
    reject_symlink_components(path, allow_missing_leaf=False)
    info = path.stat()
    if not stat.S_ISREG(info.st_mode):
        raise PathContractError(f"not a regular file: {path}")
    if reject_hardlink and info.st_nlink != 1:
        raise PathContractError(f"hard-link alias rejected: {path}")


def require_directory(path: Path) -> None:
    reject_symlink_components(path, allow_missing_leaf=False)
    if not path.is_dir():
        raise PathContractError(f"not a directory: {path}")


def _open_directory_fd(path: Path) -> int:
    canonical = safe_absolute_path(os.fspath(path), "directory path")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for component in canonical.parts[1:]:
            next_fd = os.open(component, flags | nofollow, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = next_fd
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def ensure_real_directory_tree(path: Path) -> None:
    canonical = safe_absolute_path(os.fspath(path), "directory path")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for component in canonical.parts[1:]:
            try:
                next_fd = os.open(
                    component, flags | nofollow, dir_fd=descriptor
                )
            except FileNotFoundError:
                os.mkdir(component, 0o755, dir_fd=descriptor)
                os.fsync(descriptor)
                next_fd = os.open(
                    component, flags | nofollow, dir_fd=descriptor
                )
            os.close(descriptor)
            descriptor = next_fd
    except Exception:
        os.close(descriptor)
        raise
    os.close(descriptor)


def read_pinned_regular_file(
    path: Path,
    *,
    reject_hardlink: bool = True,
) -> tuple[bytes, os.stat_result]:
    canonical = safe_absolute_path(os.fspath(path), "file path")
    try:
        parent_fd = _open_directory_fd(canonical.parent)
    except OSError as error:
        raise PathContractError(f"secure file parent failed for {canonical}: {error}") from error
    parent_before = os.fstat(parent_fd)
    descriptor: int | None = None
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(canonical.name, os.O_RDONLY | nofollow, dir_fd=parent_fd)
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise PathContractError(f"not a regular file: {canonical}")
        if reject_hardlink and before.st_nlink != 1:
            raise PathContractError(f"hard-link alias rejected: {canonical}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        metadata_before = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        metadata_after = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if metadata_before != metadata_after:
            raise PathContractError(f"file changed during pinned read: {canonical}")
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        replay_parent_fd = _open_directory_fd(canonical.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            lexical = os.stat(
                canonical.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
        finally:
            os.close(replay_parent_fd)
        if (
            (entry.st_dev, entry.st_ino) != (before.st_dev, before.st_ino)
            or (lexical.st_dev, lexical.st_ino) != (before.st_dev, before.st_ino)
            or (replay_parent.st_dev, replay_parent.st_ino)
            != (parent_before.st_dev, parent_before.st_ino)
        ):
            raise PathContractError(f"path changed during pinned read: {canonical}")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise PathContractError(f"short pinned read: {canonical}")
        return raw, before
    except OSError as error:
        raise PathContractError(f"secure file open failed for {canonical}: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def file_binding(path: Path, *, reject_hardlink: bool = True) -> dict[str, Any]:
    raw, info = read_pinned_regular_file(path, reject_hardlink=reject_hardlink)
    return {
        "sha256": sha256_bytes(raw),
        "size_bytes": info.st_size,
    }


def nearest_existing_parent(path: Path) -> Path:
    current = path.absolute()
    while not current.exists():
        if current.parent == current:
            raise PathContractError(f"no existing parent: {path}")
        current = current.parent
    reject_symlink_components(current, allow_missing_leaf=False)
    return current


def ensure_same_filesystem(left: Path, right: Path) -> None:
    if nearest_existing_parent(left).stat().st_dev != nearest_existing_parent(right).stat().st_dev:
        raise PathContractError("authoritative and operational roots differ in filesystem")


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.absolute().relative_to(parent.absolute())
        return True
    except ValueError:
        return False


def ensure_mock_output_allowed(output: Path) -> None:
    reject_symlink_components(output, allow_missing_leaf=True)
    if is_within(output, CANONICAL_RESULT) or is_within(output, CANONICAL_OPERATIONAL):
        raise PathContractError("mock output cannot use canonical production namespace")
    if output.absolute() in {CANONICAL_RESULT.absolute(), CANONICAL_OPERATIONAL.absolute()}:
        raise PathContractError("mock output cannot equal canonical production namespace")


def fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def rename_directory_noreplace(source: Path, destination: Path) -> None:
    """Atomically publish one directory without replacing any destination."""

    source = safe_absolute_path(os.fspath(source), "rename source")
    destination = safe_absolute_path(os.fspath(destination), "rename destination")
    source_parent_fd = _open_directory_fd(source.parent)
    destination_parent_fd = _open_directory_fd(destination.parent)
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        renameat2 = getattr(libc, "renameat2", None)
        if renameat2 is None:
            raise PathContractError("renameat2(RENAME_NOREPLACE) is unavailable")
        renameat2.argtypes = [
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]
        renameat2.restype = ctypes.c_int
        result = renameat2(
            source_parent_fd,
            os.fsencode(source.name),
            destination_parent_fd,
            os.fsencode(destination.name),
            1,
        )
        if result != 0:
            error_number = ctypes.get_errno()
            if error_number == errno.EEXIST:
                raise CorruptGeneration(
                    f"no-replace destination collision: {destination}"
                )
            raise PathContractError(
                f"renameat2 no-replace failed: {os.strerror(error_number)}"
            )
        try:
            os.stat(source.name, dir_fd=source_parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise CorruptGeneration("no-replace rename left source entry present")
        target_info = os.stat(
            destination.name,
            dir_fd=destination_parent_fd,
            follow_symlinks=False,
        )
        if not stat.S_ISDIR(target_info.st_mode):
            raise CorruptGeneration("no-replace rename published non-directory")
        os.fsync(source_parent_fd)
        if destination_parent_fd != source_parent_fd:
            os.fsync(destination_parent_fd)
    finally:
        os.close(source_parent_fd)
        os.close(destination_parent_fd)


def exclusive_write_bytes(path: Path, payload: bytes) -> None:
    canonical = safe_absolute_path(os.fspath(path), "exclusive output path")
    try:
        ensure_real_directory_tree(canonical.parent)
        parent_fd = _open_directory_fd(canonical.parent)
    except OSError as error:
        raise PathContractError(f"exclusive output parent failed: {error}") from error
    parent_before = os.fstat(parent_fd)
    descriptor: int | None = None
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(
            canonical.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | nofollow,
            0o644,
            dir_fd=parent_fd,
        )
        view = memoryview(payload)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short exclusive write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        if (
            not stat.S_ISREG(info.st_mode)
            or info.st_nlink != 1
            or info.st_size != len(payload)
        ):
            raise PathContractError("exclusive output publication mismatch")
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        if (entry.st_dev, entry.st_ino) != (info.st_dev, info.st_ino):
            raise PathContractError("exclusive output directory entry mismatch")
        replay_parent_fd = _open_directory_fd(canonical.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            replay_entry = os.stat(
                canonical.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
            if (
                (replay_parent.st_dev, replay_parent.st_ino)
                != (parent_before.st_dev, parent_before.st_ino)
                or (replay_entry.st_dev, replay_entry.st_ino)
                != (info.st_dev, info.st_ino)
            ):
                raise PathContractError("exclusive output lexical replay mismatch")
            os.fsync(replay_parent_fd)
        finally:
            os.close(replay_parent_fd)
        os.fsync(parent_fd)
    except FileExistsError:
        raise
    except OSError as error:
        raise PathContractError(f"exclusive output publication failed: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def exclusive_write_json(path: Path, payload: Any) -> None:
    exclusive_write_bytes(path, canonical_json_bytes(payload))


def load_plan(path: Path = PLAN) -> dict[str, Mapping[str, Any]]:
    payload = strict_json_load(path, reject_hardlink=False)
    return validate_plan_payload(payload)


def validate_plan_payload(payload: Any) -> dict[str, Mapping[str, Any]]:
    if type(payload) is not dict or type(payload.get("slabs")) is not list:
        raise StrictJSONError("L1 plan must contain a slabs array")
    if payload.get("slab_count") != 51 or type(payload.get("slab_count")) is not int:
        raise StrictJSONError("L1 plan slab count mismatch")
    records: dict[str, Mapping[str, Any]] = {}
    for record in payload["slabs"]:
        if type(record) is not dict or type(record.get("slab_id")) is not str:
            raise StrictJSONError("invalid plan slab record")
        slab_id = record["slab_id"]
        if slab_id in records:
            raise StrictJSONError(f"duplicate plan slab: {slab_id}")
        for key in ("epsilon_lower", "epsilon_upper", "center", "root_radii"):
            if key not in record:
                raise StrictJSONError(f"plan slab missing {key}: {slab_id}")
        records[slab_id] = record
    if tuple(records) != SLAB_IDS:
        raise StrictJSONError("L1 plan slab order or identity mismatch")
    return records


def source_bindings() -> dict[str, str]:
    paths = (
        SCRIPT,
        PLAN,
        BRANCH_RUNTIME_PATH,
        MOCK_BRANCH_EVALUATOR,
        PROTOCOL,
        SCHEDULER_CONTRACT,
        CHECKER_CONTRACT,
        RELEASE_CONTRACT,
    )
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths}


def candidate_limits() -> dict[str, Any]:
    return {
        "branch": {
            "record_bytes": 4 * 1024 * 1024,
            "stderr_bytes": 1 * 1024 * 1024,
            "stdout_bytes": 16 * 1024 * 1024,
            "timeout_seconds": 600,
            "total_cell_bytes": 32 * 1024 * 1024,
            "workers": 6,
        },
        "global_scientific_budget": None,
        "max_inflight_per_component_cell": 1,
        "static": {
            "max_depth_per_tree": 24,
            "max_nodes_per_cell": 1_000_000,
            "max_nodes_per_tree": 250_000,
            "timeout_seconds": 1800,
            "total_cell_bytes": 512 * 1024 * 1024,
            "workers": 8,
        },
    }


def build_mock_binding(output: Path, operational: Path) -> dict[str, Any]:
    ensure_mock_output_allowed(output)
    ensure_mock_output_allowed(operational)
    ensure_same_filesystem(output, operational)
    load_plan()
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "RUN_CONFIG",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "production_authorized": False,
        "scientific_licensing_enabled": False,
        "matrix": matrix_payload(),
        "matrix_id": canonical_matrix_id(),
        "scheduler_policy": SCHEDULER_POLICY,
        "limits": candidate_limits(),
        "paths": {
            "authoritative_root": str(output.absolute()),
            "operational_root": str(operational.absolute()),
        },
        "main_freeze": {"path": None, "sha256": None},
        "machine_freeze": {"path": None, "sha256": None},
        "prefreeze_review": {"path": None, "sha256": None, "accepted": False},
        "source_bindings": source_bindings(),
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


RUN_CONFIG_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "production_authorized",
    "scientific_licensing_enabled",
    "matrix",
    "matrix_id",
    "scheduler_policy",
    "limits",
    "paths",
    "main_freeze",
    "machine_freeze",
    "prefreeze_review",
    "source_bindings",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def validate_mock_binding(binding: Any) -> dict[str, Any]:
    exact_keys(binding, RUN_CONFIG_KEYS, "mock run binding")
    exact_int(binding["schema_version"], "schema_version", minimum=1)
    if binding["schema_version"] != SCHEMA_VERSION:
        raise StrictJSONError("schema version mismatch")
    if binding["protocol_id"] != PROTOCOL_ID or binding["artifact_role"] != "RUN_CONFIG":
        raise StrictJSONError("run binding identity mismatch")
    if (
        binding["artifact_status"] != "MOCK_ONLY_NON_LICENSING"
        or binding["authority"] != "PRODUCER_ONLY"
    ):
        raise StrictJSONError("mock artifact status mismatch")
    for key, expected in {
        "mock_only": True,
        "production_authorized": False,
        "scientific_licensing_enabled": False,
    }.items():
        if binding[key] is not expected:
            raise StrictJSONError(f"mock binding {key} mismatch")
    if binding["matrix_id"] != canonical_matrix_id():
        raise StrictJSONError("matrix id mismatch")
    if not exact_json_equal(binding["matrix"], matrix_payload()):
        raise StrictJSONError("matrix payload mismatch")
    if binding["scheduler_policy"] != SCHEDULER_POLICY:
        raise StrictJSONError("scheduler policy mismatch")
    if not exact_json_equal(binding["limits"], candidate_limits()):
        raise StrictJSONError("candidate resource limits mismatch")
    if not exact_json_equal(
        binding["main_freeze"], {"path": None, "sha256": None}
    ):
        raise StrictJSONError("mock main-freeze binding mismatch")
    if not exact_json_equal(
        binding["machine_freeze"], {"path": None, "sha256": None}
    ):
        raise StrictJSONError("mock machine-freeze binding mismatch")
    if not exact_json_equal(
        binding["prefreeze_review"],
        {"path": None, "sha256": None, "accepted": False},
    ):
        raise StrictJSONError("mock review binding mismatch")
    if not exact_json_equal(binding["source_bindings"], source_bindings()):
        raise StrictJSONError("source bindings mismatch")
    if binding["claim_boundary"] != MOCK_CLAIM_BOUNDARY:
        raise StrictJSONError("mock claim boundary mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if binding[key] is not None:
            raise StrictJSONError(f"unauthorized mock status: {key}")
    exact_keys(
        binding["paths"],
        {"authoritative_root", "operational_root"},
        "mock run paths",
    )
    output = safe_absolute_path(
        binding["paths"]["authoritative_root"], "authoritative root"
    )
    operational = safe_absolute_path(
        binding["paths"]["operational_root"], "operational root"
    )
    if operational != operational_root_for(output):
        raise PathContractError("operational root is not the canonical sibling")
    ensure_mock_output_allowed(output)
    ensure_mock_output_allowed(operational)
    ensure_same_filesystem(output, operational)
    return dict(binding)


def run_config_path(output: Path) -> Path:
    return output / "run_config.json"


def ensure_run_config(
    output: Path, binding: Mapping[str, Any], *, resume: bool
) -> tuple[dict[str, Any], str]:
    validate_mock_binding(binding)
    target = run_config_path(output)
    if target.exists():
        stored, raw, _ = strict_json_image(target, require_canonical=True)
        validate_mock_binding(stored)
        if not exact_json_equal(stored, binding):
            raise RunBindingMismatch("stored run config differs from expected binding")
        if not resume:
            raise RunBindingMismatch("run config already exists; explicit resume required")
        return dict(stored), sha256_bytes(raw)
    if resume:
        raise RunBindingMismatch("resume requested but run config is missing")
    output.mkdir(parents=True, exist_ok=False)
    exclusive_write_json(target, binding)
    stored, raw, _ = strict_json_image(target, require_canonical=True)
    if not exact_json_equal(stored, binding):
        raise RunBindingMismatch("new run config publication mismatch")
    return dict(stored), sha256_bytes(raw)


FORMAL_PREFLIGHT_RUN_CONFIG_KEYS = FINAL_RUN_CONFIG_KEYS


def ensure_formal_preflight_output_allowed(
    output: Path | str, authority_root: Path | str
) -> Path:
    candidate = safe_absolute_path(os.fspath(output), "preflight output")
    root = safe_absolute_path(os.fspath(authority_root), "authority root")
    reject_symlink_components(candidate, allow_missing_leaf=True)
    if (
        is_within(candidate, CANONICAL_RESULT)
        or is_within(candidate, CANONICAL_OPERATIONAL)
        or candidate in {CANONICAL_RESULT.absolute(), CANONICAL_OPERATIONAL.absolute()}
    ):
        raise PathContractError("formal preflight cannot use canonical production namespace")
    authority_canonical = root / "results/r401_val_l3_all_slabs"
    authority_operational = root / "results/r401_val_l3_all_slabs.operational"
    if is_within(candidate, authority_canonical) or is_within(
        candidate, authority_operational
    ):
        raise PathContractError("formal preflight cannot use authority production namespace")
    if is_within(candidate, root) or is_within(root, candidate):
        raise PathContractError("formal preflight output must not overlap authority inputs")
    return candidate


def build_formal_preflight_binding(
    snapshot: FormalAuthoritySnapshot, output: Path | str
) -> dict[str, Any]:
    """Build the exact final-shaped, non-self-authorizing run binding."""

    main = _validate_formal_main_envelope(
        strict_json_loads(snapshot.main_freeze_raw.decode("utf-8")),
        snapshot.input_roles,
        snapshot.machine_freeze_sha256,
    )
    output = ensure_formal_preflight_output_allowed(output, snapshot.authority_root)
    operational = operational_root_for(output)
    authoritative_device = nearest_existing_parent(output).stat().st_dev
    operational_device = nearest_existing_parent(operational).stat().st_dev
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "RUN_CONFIG",
        "artifact_status": "SEALED_CONTROL_PLANE_BINDING",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "dispatch_authorized_by_artifact": False,
        "matrix": matrix_payload(),
        "matrix_id": canonical_matrix_id(),
        "freeze_sha256": snapshot.main_freeze_sha256,
        "main_freeze_sha256": snapshot.main_freeze_sha256,
        "main_freeze": {
            "path": "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json",
            "sha256": snapshot.main_freeze_sha256,
        },
        "machine_freeze": {
            "path": dict(FORMAL_INPUT_ROLES)["machine_freeze"],
            "sha256": snapshot.machine_freeze_sha256,
        },
        "prefreeze_review": {
            "path": dict(FORMAL_INPUT_ROLES)["prefreeze_review"],
            "sha256": snapshot.prefreeze_review_sha256,
            "verdict": "ACCEPT_FOR_FREEZE",
        },
        "input_roles": [item.payload() for item in snapshot.input_roles],
        "serializers": main["serializers"],
        "scheduler": main["scheduler"],
        "limits": main["limits"],
        "status_tables": main["status_tables"],
        "evaluators": main["evaluators"],
        "checkers": main["checkers"],
        "archive_layout": main["archive_layout"],
        "machine_requirements": main["machine_requirements"],
        "execution_policy": main["execution_policy"],
        "paths": {
            "authoritative_root": str(output),
            "operational_root": str(operational),
        },
        "filesystem_identity": {
            "authoritative_parent_device_id": authoritative_device,
            "operational_parent_device_id": operational_device,
            "same_filesystem": authoritative_device == operational_device,
        },
        "claim_boundary": FORMAL_RUN_CONFIG_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_formal_preflight_binding(
    binding: Any,
    snapshot: FormalAuthoritySnapshot,
    output: Path,
) -> dict[str, Any]:
    exact_keys(binding, FINAL_RUN_CONFIG_KEYS, "formal run binding")
    exact_int(binding["schema_version"], "formal run schema", minimum=1)
    if binding["schema_version"] != SCHEMA_VERSION or binding["protocol_id"] != PROTOCOL_ID:
        raise StrictJSONError("formal run identity mismatch")
    if (
        binding["artifact_role"] != "RUN_CONFIG"
        or binding["artifact_status"] != "SEALED_CONTROL_PLANE_BINDING"
        or binding["authority"] != "PRODUCER_ONLY"
    ):
        raise ProductionAuthorityError("formal run binding status mismatch")
    for key, expected in {
        "scientific_licensing_enabled": False,
        "dispatch_authorized_by_artifact": False,
    }.items():
        if binding[key] is not expected:
            raise ProductionAuthorityError(f"formal run binding {key} mismatch")
    if binding["freeze_sha256"] != binding["main_freeze_sha256"]:
        raise ProductionAuthorityError("freeze_sha256/main_freeze_sha256 mismatch")
    if binding["main_freeze_sha256"] != snapshot.main_freeze_sha256:
        raise ProductionAuthorityError("formal run/main-freeze hash mismatch")
    if not exact_json_equal(binding["matrix"], matrix_payload()) or binding[
        "matrix_id"
    ] != canonical_matrix_id():
        raise ProductionAuthorityError("formal run matrix mismatch")
    expected = build_formal_preflight_binding(snapshot, output)
    if not exact_json_equal(binding, expected):
        raise RunBindingMismatch("formal run binding differs from authority snapshot")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if binding[key] is not None:
            raise ProductionAuthorityError(f"formal run binding overclaims {key}")
    return dict(binding)


def initialize_formal_preflight(
    snapshot: FormalAuthoritySnapshot,
    output: Path | str,
    *,
    _fail_at: str | None = None,
) -> tuple[dict[str, Any], str]:
    """Write one non-resumable final-shaped control-plane binding only."""

    revalidate_formal_snapshot(snapshot)
    output = ensure_formal_preflight_output_allowed(output, snapshot.authority_root)
    if output.exists():
        raise RunBindingMismatch(
            "formal preflight output already exists and cannot be resumed or promoted"
        )
    binding = build_formal_preflight_binding(snapshot, output)
    validate_formal_preflight_binding(binding, snapshot, output)
    raw = canonical_json_bytes(binding)
    ensure_real_directory_tree(output.parent)
    parent_fd = _open_directory_fd(output.parent)
    temp_fd: int | None = None
    temp_name: str | None = None
    temp_identity: tuple[int, int] | None = None
    published = False
    try:
        for attempt in range(64):
            candidate = (
                f".{output.name}.formal-preflight-"
                f"{sha256_bytes(raw)[:16]}-{attempt}"
            )
            try:
                os.mkdir(candidate, 0o755, dir_fd=parent_fd)
            except FileExistsError:
                continue
            temp_name = candidate
            break
        if temp_name is None:
            raise PathContractError("formal preflight staging namespace exhausted")
        temp_fd = os.open(
            temp_name,
            os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
        temp_info = os.fstat(temp_fd)
        temp_identity = (temp_info.st_dev, temp_info.st_ino)
        if _fail_at == "AFTER_STAGE_DIR":
            raise SyntheticCrash("formal preflight crash after staging directory")
        config_fd = os.open(
            "run_config.json",
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o644,
            dir_fd=temp_fd,
        )
        try:
            view = memoryview(raw)
            while view:
                written = os.write(config_fd, view)
                if written <= 0:
                    raise OSError("short formal preflight write")
                view = view[written:]
            os.fsync(config_fd)
            info = os.fstat(config_fd)
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size != len(raw):
                raise PathContractError("formal preflight staged config mismatch")
        finally:
            os.close(config_fd)
        os.fsync(temp_fd)
        if _fail_at in {"AFTER_CONFIG_FSYNC", "BEFORE_RENAME"}:
            raise SyntheticCrash("formal preflight crash before publication")
        libc = ctypes.CDLL(None, use_errno=True)
        renameat2 = getattr(libc, "renameat2", None)
        if renameat2 is None:
            raise PathContractError("renameat2(RENAME_NOREPLACE) is unavailable")
        renameat2.argtypes = [
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]
        renameat2.restype = ctypes.c_int
        if renameat2(
            parent_fd,
            os.fsencode(temp_name),
            parent_fd,
            os.fsencode(output.name),
            1,
        ) != 0:
            number = ctypes.get_errno()
            if number == errno.EEXIST:
                raise RunBindingMismatch("formal preflight output appeared before publication")
            raise PathContractError(
                f"formal preflight no-replace publication failed: {os.strerror(number)}"
            )
        destination = os.stat(output.name, dir_fd=parent_fd, follow_symlinks=False)
        if not stat.S_ISDIR(destination.st_mode) or (
            destination.st_dev,
            destination.st_ino,
        ) != temp_identity:
            raise PathContractError("formal preflight published inode mismatch")
        os.fsync(parent_fd)
        published = True
        return dict(binding), sha256_bytes(raw)
    finally:
        if temp_fd is not None:
            if not published and temp_name is not None and temp_identity is not None:
                try:
                    current = os.stat(temp_name, dir_fd=parent_fd, follow_symlinks=False)
                    if (current.st_dev, current.st_ino) == temp_identity:
                        try:
                            os.unlink("run_config.json", dir_fd=temp_fd)
                        except FileNotFoundError:
                            pass
                        os.fsync(temp_fd)
                        os.rmdir(temp_name, dir_fd=parent_fd)
                        os.fsync(parent_fd)
                except FileNotFoundError:
                    pass
            os.close(temp_fd)
        elif not published and temp_name is not None:
            try:
                current = os.stat(temp_name, dir_fd=parent_fd, follow_symlinks=False)
                if temp_identity is None or (
                    current.st_dev,
                    current.st_ino,
                ) == temp_identity:
                    os.rmdir(temp_name, dir_fd=parent_fd)
                    os.fsync(parent_fd)
            except FileNotFoundError:
                pass
        os.close(parent_fd)


# Exact-schema names for new callers.  The historical preflight names remain
# as compatibility aliases while every execution entry point stays locked.
build_formal_run_binding = build_formal_preflight_binding
validate_formal_run_binding = validate_formal_preflight_binding
initialize_formal_run_binding = initialize_formal_preflight


def authority_project_file(authority_root: Path | str, relative: str) -> Path:
    """Return one lexical project file without resolving path aliases."""

    root = safe_absolute_path(os.fspath(authority_root), "authority root")
    relative_path = safe_relative_path(relative)
    candidate = root.joinpath(*relative_path.parts)
    if not is_within(candidate, root):
        raise PathContractError("formal role escapes the authority root")
    return candidate


def formal_role_binding(
    authority_root: Path, role: str, relative: str
) -> tuple[FormalRoleRecord, bytes]:
    if type(role) is not str or not role:
        raise ProductionAuthorityError("formal input role name is malformed")
    path = authority_project_file(authority_root, relative)
    raw, info = read_pinned_regular_file(path)
    if relative.endswith(".json"):
        try:
            strict_json_loads(raw.decode("utf-8"))
        except UnicodeError as error:
            raise StrictJSONError(f"non-UTF8 formal JSON input: {relative}") from error
    return FormalRoleRecord(
        role=role,
        path=relative,
        sha256=sha256_bytes(raw),
        raw=raw,
        stat_identity=(
            info.st_dev,
            info.st_ino,
            info.st_size,
            info.st_mtime_ns,
            info.st_ctime_ns,
        ),
    ), raw


def capture_formal_input_roles(
    authority_root: Path,
) -> tuple[tuple[FormalRoleRecord, ...], dict[str, bytes]]:
    root = safe_absolute_path(os.fspath(authority_root), "authority root")
    require_directory(root)
    if len(FORMAL_INPUT_ROLES) != 53:
        raise ProductionAuthorityError("formal input role table is not exactly 53 roles")
    if len({role for role, _ in FORMAL_INPUT_ROLES}) != 53:
        raise ProductionAuthorityError("duplicate formal input role")
    if len({relative for _, relative in FORMAL_INPUT_ROLES}) != 53:
        raise ProductionAuthorityError("duplicate formal input path")
    bindings: list[FormalRoleRecord] = []
    images: dict[str, bytes] = {}
    for role, relative in FORMAL_INPUT_ROLES:
        binding, raw = formal_role_binding(root, role, relative)
        bindings.append(binding)
        images[role] = raw
    return tuple(bindings), images


def markdown_has_verdict_declaration(line: str) -> bool:
    """Detect any case-insensitive standalone Verdict token in one line."""

    return re.search(
        r"(?<![A-Za-z0-9_])Verdict(?![A-Za-z0-9_])", line, re.IGNORECASE
    ) is not None


def validate_prefreeze_review(path: Path) -> str:
    """Require one lexical, undecorated ACCEPT declaration in pinned bytes."""

    raw, _ = read_pinned_regular_file(path)
    try:
        text = raw.decode("ascii")
    except UnicodeError as error:
        raise ProductionAuthorityError("pre-freeze review must be strict ASCII") from error
    # In an authority-bearing review there is no need for entity syntax.
    # Reject the introducer itself, rather than attempting to emulate every
    # browser rule for optional semicolons, leading zeroes, nested decoding,
    # or ambiguous hexadecimal termination.
    if "&" in text:
        raise ProductionAuthorityError("pre-freeze review contains forbidden entity syntax")
    lines = text.splitlines()
    declarations = [line for line in lines if markdown_has_verdict_declaration(line)]
    if declarations != [PREFREEZE_ACCEPT_LINE]:
        raise ProductionAuthorityError(
            "pre-freeze review is not the sole exact ACCEPT verdict"
        )
    return sha256_bytes(raw)


def formal_serializers() -> dict[str, Any]:
    return {
        "compact_json": {
            "id": "CJ_COMPACT_V1", "sort_keys": True, "ensure_ascii": False,
            "allow_nan": False, "indent": None, "separators": [",", ":"],
            "trailing_lf": True,
        },
        "branch_pretty_json": {
            "id": "CJ_PRETTY_2_V1", "sort_keys": True, "ensure_ascii": False,
            "allow_nan": False, "indent": 2, "separators": None,
            "trailing_lf": True,
        },
        "artifact_bindings": {
            "main_freeze": "CJ_COMPACT_V1",
            "run_config": "CJ_COMPACT_V1",
            "static_proof": "CJ_COMPACT_V1",
            "static_record": "CJ_COMPACT_V1",
            "static_manifest": "CJ_COMPACT_V1",
            "branch_task_hash": "CJ_PRETTY_2_V1",
            "branch_argv_hash": "CJ_PRETTY_2_V1",
            "branch_record": "CJ_PRETTY_2_V1",
            "branch_manifest": "CJ_PRETTY_2_V1",
            "aggregates": "CJ_COMPACT_V1",
        },
    }


def formal_scheduler_policy() -> dict[str, Any]:
    return {
        "policy": SCHEDULER_POLICY,
        "component_order": ["STATIC", "BRANCH"],
        "static_workers": 8,
        "branch_workers": 6,
        "static_barrier_size": 8,
        "branch_barrier_size": 6,
        "max_inflight_per_cell": 1,
        "global_scientific_budget": None,
    }


def formal_limits() -> dict[str, Any]:
    return {
        "static": {
            "max_depth_per_tree": 24,
            "max_nodes_per_tree": 250_000,
            "max_nodes_per_cell": 1_000_000,
            "timeout_ms": 1_800_000,
            "total_cell_bytes": 512 * 1024 * 1024,
        },
        "branch": {
            "timeout_ms": 600_000,
            "term_grace_ms": 2_000,
            "pipe_close_grace_ms": 1_000,
            "stdout_bytes": 16 * 1024 * 1024,
            "stderr_bytes": 1 * 1024 * 1024,
            "record_bytes": 4 * 1024 * 1024,
            "total_cell_bytes": 32 * 1024 * 1024,
            "phase_cells": 64,
            "taylor_order": 24,
            "tolerance_128": "1e-30",
            "tolerance_256": "1e-60",
        },
        "admission": {
            "memory_pause_bytes": 48 * 1024**3,
            "launch_free_bytes": 200 * 1024**3,
            "warning_free_bytes": 180 * 1024**3,
            "pause_free_bytes": 150 * 1024**3,
            "recovery_only_free_bytes": 120 * 1024**3,
        },
    }


def formal_status_tables() -> dict[str, Any]:
    return {
        "static_evaluator": [
            {"status": "STATIC_CELL_CERTIFIED", "return_code": 0, "promotion": "ELIGIBLE"},
            {"status": "STATIC_UNRESOLVED_DEPTH", "return_code": 2, "promotion": "BLOCKED"},
            {"status": "STATIC_UNRESOLVED_NODE_BUDGET", "return_code": 2, "promotion": "BLOCKED"},
            {"status": "STATIC_INTERVAL_FAIL", "return_code": 3, "promotion": "BLOCKED"},
            {"status": "INVALID_STATIC_PROOF_CONTRACT", "return_code": 5, "promotion": "BLOCKED"},
        ],
        "branch_evaluator": [
            {"status": "BRANCH_CELL_CERTIFIED", "return_code": 0, "promotion": "ELIGIBLE"},
            {"status": "BRANCH_TUBE_UNRESOLVED", "return_code": 2, "promotion": "BLOCKED"},
            {"status": "BRANCH_FLOW_FAIL", "return_code": 3, "promotion": "BLOCKED"},
            {"status": "BRANCH_TUBE_VIOLATION", "return_code": 4, "promotion": "SCIENTIFIC_STOP"},
            {"status": "INVALID_BRANCH_PROOF_CONTRACT", "return_code": 5, "promotion": "BLOCKED"},
        ],
        "scheduler": [
            {"classification": name, "evaluator_status_required": name == "COMMITTED_EVALUATOR_RESULT", "promotion": "CONDITIONAL" if name == "COMMITTED_EVALUATOR_RESULT" else "BLOCKED"}
            for name in (
                "COMMITTED_EVALUATOR_RESULT", "CELL_TIMEOUT", "CELL_SIGNAL",
                "CELL_OUTPUT_BUDGET_EXHAUSTED", "MALFORMED_EVALUATOR_OUTPUT",
                "PROVENANCE_INVALID",
            )
        ],
    }


def formal_archive_layout() -> dict[str, Any]:
    return {
        "authoritative_relative": "results/r401_val_l3_all_slabs",
        "operational_suffix": ".operational",
        "static_cell_files": ["proof.json", "stdout.txt", "stderr.txt", "record.json"],
        "branch_cell_files": ["stdout.txt", "stderr.txt", "record.json"],
        "static_serializer": "CJ_COMPACT_V1",
        "branch_serializer": "CJ_PRETTY_2_V1",
        "aggregate_serializer": "CJ_COMPACT_V1",
    }


def formal_failure_policy() -> dict[str, Any]:
    return {
        "stop_after_current_barrier": True,
        "retry_same_generation": False,
        "aggregate_requires_certified_cells": 102,
        "quarantine_on_corrupt_recovery": True,
    }


def formal_execution_policy() -> dict[str, Any]:
    return {
        "initialize_only_writes_run_config": True,
        "execute_requires_existing_config": True,
        "execute_requires_resume": True,
        "explicit_execution_flags": ["--production", "--execute-scientific-dispatch", "--resume"],
        "config_self_authorizes": False,
        # The formal runtime and independent checker both bind exact integer
        # millisecond fields.  This completed representation migration is not
        # execution authority: scientific dispatch remains unconditionally
        # rejected by the CLI and dispatch entry points.
        "branch_millisecond_migration_complete": True,
    }


def _exact_positive_ints(payload: Mapping[str, Any], context: str) -> None:
    for key, value in payload.items():
        if type(value) is not int or value <= 0:
            raise ProductionAuthorityError(f"{context}.{key} must be a positive exact integer")


def _exact_sha(value: Any, context: str) -> str:
    if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
        raise ProductionAuthorityError(f"{context} must be lowercase SHA-256")
    return value


def _exact_nonempty_string(value: Any, context: str) -> str:
    if type(value) is not str or not value or "\x00" in value:
        raise ProductionAuthorityError(f"{context} must be a nonempty exact string")
    return value


def _exact_utc_timestamp(value: Any, context: str) -> str:
    value = _exact_nonempty_string(value, context)
    if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", value) is None:
        raise ProductionAuthorityError(f"{context} must be an exact second-resolution UTC timestamp")
    return value


def formal_machine_requirements() -> dict[str, int]:
    """Return the exact host/resource policy frozen by the A4.16 design."""

    return {
        "logical_cpu_count": 32,
        "memory_limit_bytes": 60 * 1024**3,
        "static_workers": 8,
        "branch_workers": 6,
        "memory_admission_limit_bytes": 48 * 1024**3,
        "reserve_bytes": 8 * 1024**3,
        "launch_free_bytes": 200 * 1024**3,
        "warning_free_bytes": 180 * 1024**3,
        "pause_free_bytes": 150 * 1024**3,
        "recovery_only_free_bytes": 120 * 1024**3,
    }


def formal_build_environment() -> dict[str, str]:
    return {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}


def _validate_extension_binding(
    payload: Any, context: str, *, allow_null_build_id: bool
) -> dict[str, Any]:
    exact_keys(payload, MACHINE_EXTENSION_BINDING_KEYS, context)
    safe_absolute_path(payload["path"], f"{context} path")
    exact_int(payload["mode"], f"{context}.mode", minimum=0)
    exact_int(payload["size_bytes"], f"{context}.size_bytes", minimum=1)
    _exact_sha(payload["sha256"], f"{context}.sha256")
    build_id = payload["build_id"]
    if allow_null_build_id and build_id is None:
        pass
    elif type(build_id) is not str or re.fullmatch(r"[0-9a-f]{40}", build_id) is None:
        raise ProductionAuthorityError(f"{context}.build_id must be 40-hex")
    return dict(payload)


def _validate_runtime_library(payload: Any, context: str) -> dict[str, Any]:
    exact_keys(payload, MACHINE_RUNTIME_LIBRARY_KEYS, context)
    _exact_nonempty_string(payload["soname"], f"{context}.soname")
    safe_absolute_path(payload["path"], f"{context} path")
    exact_int(payload["mode"], f"{context}.mode", minimum=0)
    exact_int(payload["size_bytes"], f"{context}.size_bytes", minimum=1)
    _exact_sha(payload["sha256"], f"{context}.sha256")
    if type(payload["build_id"]) is not str or re.fullmatch(
        r"[0-9a-f]{40}", payload["build_id"]
    ) is None:
        raise ProductionAuthorityError(f"{context}.build_id must be 40-hex")
    return dict(payload)


def _read_external_pinned_path(
    value: Any, context: str
) -> tuple[bytes, os.stat_result, Path]:
    """Pin a distribution-managed absolute path, allowing a final symlink."""

    lexical = safe_absolute_path(value, f"{context} path")
    try:
        before = os.lstat(lexical)
        if not (stat.S_ISREG(before.st_mode) or stat.S_ISLNK(before.st_mode)):
            raise PathContractError(f"{context} is not a regular file/link")
        resolved = lexical.resolve(strict=True)
        safe_absolute_path(str(resolved), f"{context} resolved path")
        raw, info = read_pinned_regular_file(resolved)
        after = os.lstat(lexical)
        replay_resolved = lexical.resolve(strict=True)
        replay_raw, replay_info = read_pinned_regular_file(replay_resolved)
    except OSError as error:
        raise PathContractError(f"{context} live path read failed: {error}") from error
    if (
        _stat_identity(before) != _stat_identity(after)
        or replay_resolved != resolved
        or replay_raw != raw
        or _stat_identity(replay_info) != _stat_identity(info)
    ):
        raise PathContractError(f"{context} changed during terminal replay")
    if _ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS is not None:
        captured = (
            _stat_identity(after),
            resolved,
            raw,
            _stat_identity(info),
        )
        previous = _ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS.setdefault(
            lexical, captured
        )
        if previous != captured:
            raise PathContractError(
                f"{context} external identity differs across bound reads"
            )
    return raw, info, resolved


def _validate_live_elf_binding(
    payload: Any,
    context: str,
    *,
    expected_soname: str | None = None,
) -> tuple[bytes, os.stat_result]:
    """Replay one exact file binding and its GNU build-id/SONAME."""

    _validate_extension_binding(payload, context, allow_null_build_id=False)
    raw, info, _ = _read_external_pinned_path(payload["path"], context)
    if (
        stat.S_IMODE(info.st_mode) != payload["mode"]
        or len(raw) != payload["size_bytes"]
        or sha256_bytes(raw) != payload["sha256"]
    ):
        raise ProductionAuthorityError(f"{context} live file binding mismatch")
    build_id, _, soname = _elf_metadata(raw, context)
    if build_id != payload["build_id"]:
        raise ProductionAuthorityError(f"{context} live GNU build-id mismatch")
    if expected_soname is not None and soname != expected_soname:
        raise ProductionAuthorityError(f"{context} live DT_SONAME mismatch")
    return raw, info


def _validate_live_runtime_binding(
    payload: Any, context: str, *, expected_soname: str
) -> tuple[bytes, os.stat_result]:
    _validate_runtime_library(payload, context)
    if payload["soname"] != expected_soname:
        raise ProductionAuthorityError(f"{context} SONAME/order mismatch")
    raw, info, _ = _read_external_pinned_path(payload["path"], context)
    if (
        stat.S_IMODE(info.st_mode) != payload["mode"]
        or len(raw) != payload["size_bytes"]
        or sha256_bytes(raw) != payload["sha256"]
    ):
        raise ProductionAuthorityError(f"{context} live file binding mismatch")
    build_id, _, soname = _elf_metadata(raw, context)
    if build_id != payload["build_id"] or soname != expected_soname:
        raise ProductionAuthorityError(
            f"{context} live GNU build-id/DT_SONAME mismatch"
        )
    return raw, info


def _live_boot_id_bytes() -> bytes:
    """Read and identity-replay the bounded procfs boot UUID image."""

    path = Path("/proc/sys/kernel/random/boot_id")
    before = os.stat(path, follow_symlinks=False)
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        raw = os.read(descriptor, 256)
        if os.read(descriptor, 1):
            raise PathContractError("boot ID exceeded its bounded ABI")
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    replay = os.stat(path, follow_symlinks=False)
    if (
        (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino)
        or (before.st_dev, before.st_ino) != (replay.st_dev, replay.st_ino)
        or re.fullmatch(
            rb"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\n",
            raw,
        )
        is None
    ):
        raise PathContractError("boot ID changed or is malformed")
    return raw


def _elf_metadata(
    raw: bytes, context: str
) -> tuple[str, list[str], str | None]:
    """Parse the exact GNU build-id and dynamic names from a pinned ELF image.

    Formal A4.16 machine evidence admits only 64-bit little-endian x86-64
    ELF.  Parsing the section tables locally avoids giving an unbound
    ``readelf`` executable any authority over the machine handshake.
    """

    if type(raw) is not bytes:
        raise ProductionAuthorityError(f"{context} must be an exact byte image")
    header_format = "<16sHHIQQQIHHHHHH"
    section_format = "<IIQQQQIIQQ"
    dynamic_format = "<qQ"
    header_size = struct.calcsize(header_format)
    section_size = struct.calcsize(section_format)
    if len(raw) < header_size:
        raise ProductionAuthorityError(f"{context} is a truncated ELF image")
    header = struct.unpack_from(header_format, raw, 0)
    ident = header[0]
    if (
        ident[:4] != b"\x7fELF"
        or ident[4] != 2
        or ident[5] != 1
        or ident[6] != 1
        or header[2] != 62
        or header[3] != 1
        or header[8] != header_size
        or header[11] != section_size
    ):
        raise ProductionAuthorityError(f"{context} ELF identity/header mismatch")
    section_offset = header[6]
    section_count = header[12]
    section_name_index = header[13]
    if (
        section_offset <= 0
        or section_count <= 0
        or section_name_index >= section_count
        or section_offset + section_count * section_size > len(raw)
    ):
        raise ProductionAuthorityError(f"{context} ELF section table is malformed")
    sections = [
        struct.unpack_from(
            section_format, raw, section_offset + index * section_size
        )
        for index in range(section_count)
    ]

    def section_bytes(index: int, label: str) -> bytes:
        if index < 0 or index >= len(sections):
            raise ProductionAuthorityError(
                f"{context} ELF {label} section index is invalid"
            )
        section = sections[index]
        offset, size = section[4], section[5]
        if offset > len(raw) or size > len(raw) - offset:
            raise ProductionAuthorityError(
                f"{context} ELF {label} section is out of bounds"
            )
        return raw[offset : offset + size]

    if sections[section_name_index][1] != 3:
        raise ProductionAuthorityError(
            f"{context} ELF section-name table is malformed"
        )
    section_bytes(section_name_index, "section-name")
    build_ids: list[str] = []
    needed: list[str] = []
    sonames: list[str] = []
    for index, section in enumerate(sections):
        section_type = section[1]
        if section_type == 7:  # SHT_NOTE
            note = section_bytes(index, "note")
            cursor = 0
            while cursor < len(note):
                if len(note) - cursor < 12:
                    raise ProductionAuthorityError(
                        f"{context} ELF note header is truncated"
                    )
                name_size, description_size, note_type = struct.unpack_from(
                    "<III", note, cursor
                )
                cursor += 12
                name_end = cursor + name_size
                description_start = (name_end + 3) & ~3
                description_end = description_start + description_size
                next_cursor = (description_end + 3) & ~3
                if (
                    name_end > len(note)
                    or description_end > len(note)
                    or next_cursor > len(note)
                ):
                    raise ProductionAuthorityError(
                        f"{context} ELF note payload is truncated"
                    )
                if note[cursor:name_end] == b"GNU\x00" and note_type == 3:
                    description = note[description_start:description_end]
                    if len(description) != 20:
                        raise ProductionAuthorityError(
                            f"{context} GNU build-id is not 20 bytes"
                        )
                    build_ids.append(description.hex())
                cursor = next_cursor
        elif section_type == 6:  # SHT_DYNAMIC
            dynamic = section_bytes(index, "dynamic")
            entry_size = section[9]
            string_index = section[6]
            if (
                entry_size != struct.calcsize(dynamic_format)
                or len(dynamic) % entry_size != 0
                or string_index >= len(sections)
                or sections[string_index][1] != 3
            ):
                raise ProductionAuthorityError(
                    f"{context} ELF dynamic table is malformed"
                )
            strings = section_bytes(string_index, "dynamic-string")

            def dynamic_string(offset: int) -> str:
                if offset <= 0 or offset >= len(strings):
                    raise ProductionAuthorityError(
                        f"{context} ELF dynamic string offset is invalid"
                    )
                end = strings.find(b"\x00", offset)
                if end < 0:
                    raise ProductionAuthorityError(
                        f"{context} ELF dynamic string is unterminated"
                    )
                try:
                    value = strings[offset:end].decode("ascii")
                except UnicodeDecodeError as error:
                    raise ProductionAuthorityError(
                        f"{context} ELF dynamic string is not ASCII"
                    ) from error
                if not value or "/" in value or "\x00" in value:
                    raise ProductionAuthorityError(
                        f"{context} ELF dynamic string is unsafe"
                    )
                return value

            for cursor in range(0, len(dynamic), entry_size):
                tag, value = struct.unpack_from(dynamic_format, dynamic, cursor)
                if tag == 0:
                    break
                if tag == 1:
                    needed.append(dynamic_string(value))
                elif tag == 14:
                    sonames.append(dynamic_string(value))
    if len(build_ids) != 1 or re.fullmatch(r"[0-9a-f]{40}", build_ids[0]) is None:
        raise ProductionAuthorityError(
            f"{context} must contain one exact GNU build-id"
        )
    if len(needed) != len(set(needed)):
        raise ProductionAuthorityError(f"{context} repeats a DT_NEEDED entry")
    if len(sonames) > 1:
        raise ProductionAuthorityError(f"{context} repeats DT_SONAME")
    return build_ids[0], sorted(needed), sonames[0] if sonames else None


def _exact_nonnegative_float(value: Any, context: str) -> float:
    if type(value) is not float or not math.isfinite(value) or value < 0:
        raise ProductionAuthorityError(f"{context} must be an exact finite nonnegative float")
    return value


def _exact_int_array(value: Any, context: str, *, nonempty: bool = True) -> list[int]:
    if type(value) is not list or (nonempty and not value):
        raise ProductionAuthorityError(f"{context} must be a nonempty exact integer array")
    for index, item in enumerate(value):
        exact_int(item, f"{context}[{index}]", minimum=0)
    return list(value)


def _resource_plan_records(
    project_root: Path,
) -> tuple[dict[str, Mapping[str, Any]], str]:
    """Read the live L1 plan once and return its exact record map/image hash."""

    plan_path = project_root / dict(FORMAL_INPUT_ROLES)["l1_final_plan"]
    raw, _ = read_pinned_regular_file(plan_path)
    try:
        payload = strict_json_loads(raw.decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("resource-calibration L1 plan is not UTF-8") from error
    return validate_plan_payload(payload), sha256_bytes(raw)


def _static_resource_argv(
    run: Mapping[str, Any],
    bindings: Mapping[str, Any],
    plan_record: Mapping[str, Any],
) -> list[str]:
    return [
        bindings["interpreter"]["invocation_path"],
        bindings["evaluator"]["path"],
        "--slab-id", run["slab_id"],
        "--precision-bits", str(run["precision_bits"]),
        "--epsilon-lower", plan_record["epsilon_lower"],
        "--epsilon-upper", plan_record["epsilon_upper"],
        "--matrix-id", bindings["calibration_binding"]["matrix_id"],
        "--freeze-sha256", bindings["calibration_binding"]["nonfreeze_sha256"],
        "--run-config-sha256", bindings["calibration_binding"]["nonrunconfig_sha256"],
        "--plan-record-sha256", sha256_bytes(canonical_json_bytes(plan_record)),
        "--max-depth", "24",
        "--max-nodes-per-tree", "250000",
        "--max-nodes-per-cell", "1000000",
        "--output", run["output"],
    ]


def _validate_static_resource_run(
    run: Any,
    expected: tuple[int, str, int],
    *,
    bindings: Mapping[str, Any],
    plan_records: Mapping[str, Mapping[str, Any]],
    temporary_root: Path,
    expected_label: str,
    context: str,
) -> int:
    exact_keys(run, STATIC_RESOURCE_RUN_KEYS, context)
    bits, slab, replica = expected
    for key in ("output_bytes", "peak_rss_kib", "precision_bits", "replica", "returncode", "stderr_bytes", "stdout_bytes"):
        exact_int(run[key], f"{context}.{key}", minimum=0)
    for key in ("elapsed_seconds", "system_cpu_seconds", "user_cpu_seconds"):
        _exact_nonnegative_float(run[key], f"{context}.{key}")
    if (run["precision_bits"], run["slab_id"], run["replica"]) != expected:
        raise ProductionAuthorityError(f"{context} ordered cell/replica mismatch")
    if bits not in PRECISIONS or slab not in ("S000", "S025", "S050"):
        raise ProductionAuthorityError(f"{context} is not a public calibration cell")
    if run["label"] != expected_label:
        raise ProductionAuthorityError(f"{context} label mismatch")
    if run["argv"] != _static_resource_argv(run, bindings, plan_records[slab]):
        raise ProductionAuthorityError(f"{context} exact invocation mismatch")
    if (
        run["returncode"] != 0
        or run["peak_rss_kib"] <= 0
        or run["output_bytes"] <= 0
        or run["evaluator_status"] != "STATIC_CELL_CERTIFIED"
        or run["stdout_exact_status_line"] != "evaluator_status=STATIC_CELL_CERTIFIED"
        or run["stderr_empty"] is not True
        or run["stderr_bytes"] != 0
    ):
        raise ProductionAuthorityError(f"{context} evaluator ABI did not pass")
    for key in ("output_sha256", "stdout_sha256", "stderr_sha256"):
        _exact_sha(run[key], f"{context}.{key}")
    expected_stdout = b"evaluator_status=STATIC_CELL_CERTIFIED\n"
    if (
        run["stdout_bytes"] != len(expected_stdout)
        or run["stdout_sha256"] != sha256_bytes(expected_stdout)
        or run["stderr_sha256"] != sha256_bytes(b"")
    ):
        raise ProductionAuthorityError(f"{context} stdout/stderr ABI receipt mismatch")
    for key in ("output", "stdout", "stderr"):
        path = safe_absolute_path(run[key], f"{context}.{key}")
        try:
            path.relative_to(temporary_root)
        except ValueError as error:
            raise PathContractError(
                f"{context}.{key} escaped the inert temporary evidence root"
            ) from error
    for key in (
        "component_status", "milestone_status", "scientific_status",
        "theorem_status", "final_status",
    ):
        if run[key] is not None:
            raise ProductionAuthorityError(f"{context} overclaims {key}")
    return run["peak_rss_kib"] * 1024


def _validate_static_resource_payload(
    payload: Any,
    requirements: Mapping[str, int],
    observations: Mapping[str, int],
    project_root: Path,
) -> dict[str, Any]:
    context = "static resource payload"
    exact_keys(payload, STATIC_RESOURCE_PAYLOAD_KEYS, context)
    exact_int(payload["schema_version"], f"{context}.schema_version", minimum=1)
    if (
        payload["schema_version"] != SCHEMA_VERSION
        or payload["protocol_id"] != PROTOCOL_ID
        or payload["artifact_role"] != "TEMP_PUBLIC_STATIC_RSS_CALIBRATION"
        or payload["scope"] != "PUBLIC_S0_RESOURCE_CALIBRATION_ONLY"
        or payload["production_authorized"] is not False
        or payload["scientific_licensing_enabled"] is not False
    ):
        raise ProductionAuthorityError(f"{context} identity/authority mismatch")
    if payload["claim_boundary"] != (
        "resource telemetry on already-public S000/S025/S050 at 128/256 only; "
        "no held-out/all-slab evaluation, no freeze, no scientific promotion"
    ):
        raise ProductionAuthorityError(f"{context} claim boundary mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload[key] is not None:
            raise ProductionAuthorityError(f"{context} overclaims {key}")
    if payload["project_root"] != str(project_root):
        raise ProductionAuthorityError(f"{context} project root mismatch")
    temporary_root = safe_absolute_path(
        payload["temporary_root"], f"{context}.temporary_root"
    )
    if temporary_root.parts[:2] != ("/", "tmp"):
        raise PathContractError(f"{context} must record inert /tmp evidence")
    exact_keys(payload["bindings"], STATIC_RESOURCE_BINDINGS_KEYS, f"{context}.bindings")
    bindings = payload["bindings"]
    exact_keys(bindings["calibration_binding"], STATIC_RESOURCE_CALIBRATION_BINDING_KEYS, f"{context}.calibration_binding")
    if bindings["calibration_binding"]["matrix_id"] != canonical_matrix_id():
        raise ProductionAuthorityError(f"{context} matrix binding mismatch")
    for key in ("nonfreeze_sha256", "nonrunconfig_sha256"):
        _exact_sha(bindings["calibration_binding"][key], f"{context}.{key}")
    exact_keys(bindings["evaluator"], STATIC_RESOURCE_EVALUATOR_BINDING_KEYS, f"{context}.evaluator")
    exact_keys(bindings["interpreter"], STATIC_RESOURCE_INTERPRETER_BINDING_KEYS, f"{context}.interpreter")
    exact_keys(bindings["plan"], STATIC_RESOURCE_PLAN_BINDING_KEYS, f"{context}.plan")
    exact_keys(bindings["python_flint"], STATIC_RESOURCE_PYTHON_FLINT_KEYS, f"{context}.python_flint")
    evaluator = bindings["evaluator"]
    interpreter = bindings["interpreter"]
    expected_evaluator = project_root / dict(FORMAL_INPUT_ROLES)["static_evaluator"]
    evaluator_raw, evaluator_info = read_pinned_regular_file(expected_evaluator)
    if (
        evaluator["path"] != str(expected_evaluator)
        or evaluator["mode"] != "0644"
        or evaluator["mode"] != f"{stat.S_IMODE(evaluator_info.st_mode):04o}"
        or evaluator["sha256"] != sha256_bytes(evaluator_raw)
        or evaluator["size_bytes"] != len(evaluator_raw)
    ):
        raise ProductionAuthorityError(f"{context} live evaluator binding mismatch")
    for item_context, item in (("evaluator", evaluator), ("interpreter", interpreter)):
        _exact_sha(item["sha256"], f"{context}.{item_context}.sha256")
        exact_int(item["size_bytes"], f"{context}.{item_context}.size_bytes", minimum=1)
    for key in ("path",):
        _exact_nonempty_string(evaluator[key], f"{context}.evaluator.{key}")
    for key in ("invocation_path", "resolved_path", "version"):
        _exact_nonempty_string(interpreter[key], f"{context}.interpreter.{key}")
    plan_binding = bindings["plan"]
    plan_records, plan_sha = _resource_plan_records(project_root)
    expected_plan = project_root / dict(FORMAL_INPUT_ROLES)["l1_final_plan"]
    _exact_nonempty_string(plan_binding["path"], f"{context}.plan.path")
    _exact_sha(plan_binding["sha256"], f"{context}.plan.sha256")
    if (
        plan_binding["path"] != str(expected_plan)
        or plan_binding["sha256"] != plan_sha
        or plan_binding["public_slab_ids"] != ["S000", "S025", "S050"]
    ):
        raise ProductionAuthorityError(f"{context} live plan binding mismatch")
    python_flint = bindings["python_flint"]
    for key in ("arb_extension_path", "module_path", "record_path", "flint_version", "version"):
        _exact_nonempty_string(python_flint[key], f"{context}.python_flint.{key}")
    for key in ("arb_extension_sha256", "installed_manifest_sha256", "record_sha256"):
        _exact_sha(python_flint[key], f"{context}.python_flint.{key}")
    exact_int(python_flint["installed_record_file_count"], f"{context}.installed_record_file_count", minimum=1)
    exact_keys(payload["measurement"], STATIC_RESOURCE_MEASUREMENT_KEYS, f"{context}.measurement")
    measurement = payload["measurement"]
    for key in ("baseline_conservative_bytes", "bytes_per_kib", "cgroup_limit_bytes", "concurrent_peak_bytes"):
        exact_int(measurement[key], f"{context}.measurement.{key}", minimum=1)
    baseline_samples = _exact_int_array(measurement["baseline_samples_bytes"], f"{context}.baseline_samples")
    concurrent_samples = _exact_int_array(measurement["concurrent_samples_bytes"], f"{context}.concurrent_samples")
    if len(baseline_samples) != 21:
        raise ProductionAuthorityError(f"{context} must contain exactly 21 baseline samples")
    for index, value in enumerate([*baseline_samples, *concurrent_samples]):
        if value <= 0:
            raise ProductionAuthorityError(
                f"{context} cgroup sample {index} must be positive"
            )
    for key in ("cgroup_limit_path", "cgroup_usage_path", "method", "ru_maxrss_unit"):
        _exact_nonempty_string(measurement[key], f"{context}.measurement.{key}")
    if (
        measurement["method"]
        != "os.wait4(pid,0/WNOHANG).rusage.ru_maxrss on Linux"
        or measurement["ru_maxrss_unit"] != "KiB"
        or measurement["bytes_per_kib"] != 1024
        or measurement["cgroup_usage_path"]
        != "/sys/fs/cgroup/memory/memory.usage_in_bytes"
        or measurement["cgroup_limit_path"]
        != "/sys/fs/cgroup/memory/memory.limit_in_bytes"
        or measurement["baseline_conservative_bytes"] != max(baseline_samples)
        or measurement["concurrent_peak_bytes"] != max(concurrent_samples)
        or measurement["cgroup_limit_bytes"] != requirements["memory_limit_bytes"]
        or type(measurement["sample_interval_seconds"]) is not float
        or measurement["sample_interval_seconds"] != 0.05
    ):
        raise ProductionAuthorityError(f"{context} measurement arithmetic mismatch")
    expected_sequential = [
        (bits, slab, 0) for bits in PRECISIONS for slab in ("S000", "S025", "S050")
    ]
    expected_concurrent = expected_sequential + [(256, "S025", 1), (256, "S050", 1)]
    if type(payload["sequential_runs"]) is not list or type(payload["concurrent_runs"]) is not list:
        raise ProductionAuthorityError(f"{context} run arrays are malformed")
    if len(payload["sequential_runs"]) != 6 or len(payload["concurrent_runs"]) != 8:
        raise ProductionAuthorityError(f"{context} run counts mismatch")
    peaks: list[int] = []
    for index, (run, expected) in enumerate(
        zip(payload["sequential_runs"], expected_sequential, strict=True)
    ):
        peaks.append(_validate_static_resource_run(
            run,
            expected,
            bindings=bindings,
            plan_records=plan_records,
            temporary_root=temporary_root,
            expected_label=f"{expected[0]}_{expected[1]}",
            context=f"{context}.sequential_runs[{index}]",
        ))
    for index, (run, expected) in enumerate(
        zip(payload["concurrent_runs"], expected_concurrent, strict=True)
    ):
        peaks.append(_validate_static_resource_run(
            run,
            expected,
            bindings=bindings,
            plan_records=plan_records,
            temporary_root=temporary_root,
            expected_label=(
                f"{index:02d}_{expected[0]}_{expected[1]}_r{expected[2]}"
            ),
            context=f"{context}.concurrent_runs[{index}]",
        ))
    if type(payload["concurrent_schedule"]) is not list or len(payload["concurrent_schedule"]) != 8:
        raise ProductionAuthorityError(f"{context} concurrent schedule mismatch")
    for index, (item, expected) in enumerate(zip(payload["concurrent_schedule"], expected_concurrent)):
        exact_keys(item, STATIC_RESOURCE_SCHEDULE_KEYS, f"{context}.concurrent_schedule[{index}]")
        if (item["precision_bits"], item["slab_id"]) != expected[:2]:
            raise ProductionAuthorityError(f"{context} concurrent schedule order mismatch")
    expected_environment = {
        "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1", "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1", "TZ": "UTC",
    }
    if not exact_json_equal(payload["execution_environment"], expected_environment):
        raise ProductionAuthorityError(f"{context} execution environment mismatch")
    exact_keys(payload["admission"], STATIC_RESOURCE_ADMISSION_KEYS, f"{context}.admission")
    admission = payload["admission"]
    for key in (
        "admission_limit_bytes", "headroom_bytes", "idle_baseline_bytes",
        "lhs_bytes", "representative_peak_rss_bytes", "reserve_bytes", "workers",
    ):
        exact_int(admission[key], f"{context}.admission.{key}", minimum=0)
    peak = max(peaks)
    lhs = measurement["baseline_conservative_bytes"] + requirements["static_workers"] * peak + requirements["reserve_bytes"]
    if (
        admission["formula"] != "idle_baseline_bytes + workers * representative_peak_rss_bytes + reserve_bytes <= admission_limit_bytes"
        or admission["idle_baseline_bytes"] != measurement["baseline_conservative_bytes"]
        or admission["representative_peak_rss_bytes"] != peak
        or admission["workers"] != requirements["static_workers"]
        or admission["reserve_bytes"] != requirements["reserve_bytes"]
        or admission["admission_limit_bytes"] != requirements["memory_admission_limit_bytes"]
        or admission["lhs_bytes"] != lhs
        or admission["headroom_bytes"] != admission["admission_limit_bytes"] - lhs
        or admission["passes"]
        is not (lhs <= admission["admission_limit_bytes"])
    ):
        raise ProductionAuthorityError(f"{context} admission arithmetic mismatch")
    return dict(payload)


def _branch_resource_argv(
    binary_path: str,
    bits: int,
    plan_record: Mapping[str, Any],
) -> list[str]:
    center = plan_record["center"]
    radii = plan_record["root_radii"]

    def endpoint(name: str, sign: int) -> str:
        return format(
            Decimal(center[name]) + sign * Decimal(radii[name]),
            "f",
        )

    return [
        binary_path,
        str(bits),
        plan_record["epsilon_lower"],
        plan_record["epsilon_upper"],
        endpoint("q_slow", -1),
        endpoint("q_slow", 1),
        endpoint("q_fast", -1),
        endpoint("q_fast", 1),
        endpoint("p_slow", -1),
        endpoint("p_slow", 1),
        endpoint("period", -1),
        endpoint("period", 1),
    ]


def _validate_branch_resource_payload(
    payload: Any,
    requirements: Mapping[str, int],
    observations: Mapping[str, int],
    project_root: Path,
    expected_binary_sha256: str,
) -> dict[str, Any]:
    context = "branch resource payload"
    exact_keys(payload, BRANCH_RESOURCE_PAYLOAD_KEYS, context)
    if payload["scope"] != "REPRESENTATIVE_S0_CALIBRATION_ONLY":
        raise ProductionAuthorityError(f"{context} scope mismatch")
    for key in ("milestone_status", "scientific_status", "theorem_status", "final_status"):
        if payload[key] is not None:
            raise ProductionAuthorityError(f"{context} overclaims {key}")
    for key in (
        "baseline_conservative_bytes", "cgroup_limit_bytes",
        "per_process_peak_rss_max_kib", "sampled_concurrent_peak_bytes",
        "task_count",
    ):
        exact_int(payload[key], f"{context}.{key}", minimum=1)
    exact_int(
        payload["sampled_concurrent_increment_bytes"],
        f"{context}.sampled_concurrent_increment_bytes",
        minimum=0,
    )
    baseline_samples = _exact_int_array(payload["baseline_samples_bytes"], f"{context}.baseline_samples")
    post_samples = _exact_int_array(payload["post_samples_bytes"], f"{context}.post_samples")
    if len(baseline_samples) != 21 or len(post_samples) != 21:
        raise ProductionAuthorityError(f"{context} sample arrays must each have length 21")
    if any(value <= 0 for value in [*baseline_samples, *post_samples]):
        raise ProductionAuthorityError(f"{context} cgroup samples must be positive")
    binary_path = str(safe_absolute_path(payload["binary"], f"{context}.binary"))
    if binary_path != payload["binary"]:
        raise PathContractError(f"{context}.binary is not canonical absolute")
    _exact_sha(payload["binary_sha256"], f"{context}.binary_sha256")
    if payload["binary_sha256"] != expected_binary_sha256:
        raise ProductionAuthorityError(
            f"{context} is not bound to the persistent branch binary"
        )
    plan_records, _ = _resource_plan_records(project_root)
    expected_identities = [
        (bits, slab) for bits in PRECISIONS for slab in ("S000", "S025", "S050")
    ]
    if type(payload["results"]) is not list or len(payload["results"]) != 6:
        raise ProductionAuthorityError(f"{context}.results must contain six rows")
    for index, (run, expected) in enumerate(zip(payload["results"], expected_identities)):
        run_context = f"{context}.results[{index}]"
        exact_keys(run, BRANCH_RESOURCE_RUN_KEYS, run_context)
        for key in ("argv_count", "peak_rss_kib", "precision_bits", "returncode", "stderr_bytes", "stdout_bytes"):
            exact_int(run[key], f"{run_context}.{key}", minimum=0)
        for key in ("elapsed_seconds", "system_cpu_seconds", "user_cpu_seconds"):
            _exact_nonnegative_float(run[key], f"{run_context}.{key}")
        if (run["precision_bits"], run["slab_id"]) != expected:
            raise ProductionAuthorityError(f"{run_context} ordered cell mismatch")
        if (
            run["argv_count"] != 12
            or run["argv"]
            != _branch_resource_argv(binary_path, expected[0], plan_records[expected[1]])
        ):
            raise ProductionAuthorityError(f"{run_context} exact invocation mismatch")
        if (
            run["returncode"] != 0
            or run["peak_rss_kib"] <= 0
            or run["stdout_bytes"] <= 0
            or run["abi_verified"] is not True
            or run["terminal_abi_value"] != "BRANCH_CELL_CERTIFIED"
            or run["stderr_bytes"] != 0
        ):
            raise ProductionAuthorityError(f"{run_context} evaluator ABI did not pass")
        for key in ("stdout_sha256", "stderr_sha256"):
            _exact_sha(run[key], f"{run_context}.{key}")
        if run["stderr_sha256"] != sha256_bytes(b""):
            raise ProductionAuthorityError(f"{run_context} empty stderr hash mismatch")
    peak = max(run["peak_rss_kib"] * 1024 for run in payload["results"])
    if (
        payload["baseline_conservative_bytes"] != max(baseline_samples)
        or payload["cgroup_limit_bytes"] != requirements["memory_limit_bytes"]
        or payload["per_process_peak_rss_max_kib"] * 1024 != peak
        or payload["sampled_concurrent_increment_bytes"]
        != payload["sampled_concurrent_peak_bytes"] - payload["baseline_conservative_bytes"]
        or payload["task_count"] != 6
    ):
        raise ProductionAuthorityError(f"{context} measurement arithmetic mismatch")
    exact_keys(payload["admission"], BRANCH_RESOURCE_ADMISSION_KEYS, f"{context}.admission")
    admission = payload["admission"]
    for key in ("baseline_bytes", "headroom_bytes", "lhs_bytes", "limit_bytes", "peak_rss_bytes", "reserve_bytes", "workers"):
        exact_int(admission[key], f"{context}.admission.{key}", minimum=0)
    lhs = payload["baseline_conservative_bytes"] + requirements["branch_workers"] * peak + requirements["reserve_bytes"]
    if (
        admission["formula"] != "baseline + 6*peak_rss + 8GiB <= 48GiB"
        or admission["baseline_bytes"] != payload["baseline_conservative_bytes"]
        or admission["peak_rss_bytes"] != peak
        or admission["workers"] != requirements["branch_workers"]
        or admission["reserve_bytes"] != requirements["reserve_bytes"]
        or admission["limit_bytes"] != requirements["memory_admission_limit_bytes"]
        or admission["lhs_bytes"] != lhs
        or admission["headroom_bytes"] != admission["limit_bytes"] - lhs
        or admission["passes"] is not (lhs <= admission["limit_bytes"])
    ):
        raise ProductionAuthorityError(f"{context} admission arithmetic mismatch")
    return dict(payload)


def _conda_lstat_at(path: Path) -> tuple[os.stat_result, int]:
    """Securely lstat one Conda manifest leaf and return its pinned parent fd."""

    canonical = safe_absolute_path(os.fspath(path), "Conda installed path")
    try:
        parent_fd = _open_directory_fd(canonical.parent)
        info = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as error:
        if "parent_fd" in locals():
            os.close(parent_fd)
        raise PathContractError(f"secure Conda lstat failed for {canonical}: {error}") from error
    return info, parent_fd


def _conda_symlink_image(path: Path) -> tuple[bytes, os.stat_result]:
    info, parent_fd = _conda_lstat_at(path)
    try:
        if not stat.S_ISLNK(info.st_mode):
            raise PathContractError(f"Conda path is not a symlink: {path}")
        target = os.readlink(path.name, dir_fd=parent_fd)
        try:
            raw = target.encode("utf-8")
        except UnicodeError as error:
            raise PathContractError(
                f"Conda symlink target is not UTF-8: {path}"
            ) from error
        after = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        replay = os.readlink(path.name, dir_fd=parent_fd)
        if _stat_identity(after) != _stat_identity(info) or replay != target:
            raise PathContractError(f"Conda symlink changed during read: {path}")
        if len(raw) != info.st_size:
            raise PathContractError(f"Conda symlink size/image mismatch: {path}")
        return raw, info
    finally:
        os.close(parent_fd)


def _conda_live_file_row(
    prefix: Path, relative: str
) -> tuple[dict[str, Any], tuple[int, int, int, int, int], bytes]:
    safe = safe_relative_path(relative)
    path = prefix.joinpath(*safe.parts)
    info, parent_fd = _conda_lstat_at(path)
    os.close(parent_fd)
    if stat.S_ISREG(info.st_mode):
        raw, pinned = read_pinned_regular_file(path, reject_hardlink=False)
        kind = "REGULAR"
    elif stat.S_ISLNK(info.st_mode):
        raw, pinned = _conda_symlink_image(path)
        kind = "SYMLINK"
    else:
        raise PathContractError(f"unsupported Conda installed path type: {path}")
    if _stat_identity(pinned) != _stat_identity(info):
        raise PathContractError(f"Conda path identity changed before read: {path}")
    row = {
        "kind": kind,
        "mode": f"{stat.S_IMODE(pinned.st_mode):04o}",
        "path": relative,
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
    }
    exact_keys(row, CONDA_MANIFEST_ROW_KEYS, "Conda installed manifest row")
    return row, _stat_identity(pinned), raw


def recompute_conda_python_manifest(
    executable_path: str,
) -> tuple[str, int, str]:
    """Replay the exact live Python-package manifest rooted at a Conda prefix."""

    executable = safe_absolute_path(executable_path, "Python executable")
    if executable.name != "python3" or executable.parent.name != "bin":
        raise ProductionAuthorityError(
            "Conda manifest requires lexical <prefix>/bin/python3"
        )
    prefix = executable.parent.parent
    conda_meta = prefix / "conda-meta"
    meta_fd = _open_directory_fd(conda_meta)
    try:
        before_names = sorted(os.listdir(meta_fd), key=lambda item: item.encode("utf-8"))
    finally:
        os.close(meta_fd)
    pattern = re.compile(r"python-3\.12\.3-[A-Za-z0-9_.-]+\.json\Z")
    candidates = [name for name in before_names if pattern.fullmatch(name)]
    if len(candidates) != 1:
        raise ProductionAuthorityError(
            "Conda prefix must contain one python-3.12.3 metadata record"
        )
    metadata_path = conda_meta / candidates[0]
    metadata_raw, metadata_info = read_pinned_regular_file(
        metadata_path, reject_hardlink=False
    )
    try:
        metadata = strict_json_loads(metadata_raw.decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("Conda Python metadata is not UTF-8") from error
    if type(metadata) is not dict or metadata.get("name") != "python" or metadata.get(
        "version"
    ) != "3.12.3":
        raise ProductionAuthorityError("Conda Python metadata identity mismatch")
    files = metadata.get("files")
    paths_data = metadata.get("paths_data")
    if (
        type(files) is not list
        or not files
        or not all(type(item) is str for item in files)
        or len(set(files)) != len(files)
        or type(paths_data) is not dict
        or type(paths_data.get("paths")) is not list
    ):
        raise ProductionAuthorityError("Conda Python metadata file set is malformed")
    path_rows = paths_data["paths"]
    declared_paths: list[str] = []
    for index, item in enumerate(path_rows):
        if type(item) is not dict or type(item.get("_path")) is not str:
            raise ProductionAuthorityError(
                f"Conda paths_data.paths[{index}] is malformed"
            )
        declared_paths.append(item["_path"])
    if (
        len(declared_paths) != len(files)
        or len(set(declared_paths)) != len(declared_paths)
        or set(declared_paths) != set(files)
    ):
        raise ProductionAuthorityError(
            "Conda files and paths_data.paths._path differ"
        )
    for relative in files:
        safe_relative_path(relative)
        try:
            relative.encode("utf-8")
        except UnicodeError as error:
            raise PathContractError("Conda installed path is not UTF-8") from error
    ordered = sorted(files, key=lambda item: item.encode("utf-8"))
    rows: list[dict[str, Any]] = []
    captures: list[tuple[str, tuple[int, int, int, int, int], bytes]] = []
    for relative in ordered:
        row, identity, raw = _conda_live_file_row(prefix, relative)
        rows.append(row)
        captures.append((relative, identity, raw))

    # Terminal replay closes a long manifest scan: every lexical leaf must
    # still name the same inode/image and the metadata/listing must be stable.
    for (relative, identity, raw), expected_row in zip(
        captures, rows, strict=True
    ):
        replay_row, replay_identity, replay_raw = _conda_live_file_row(
            prefix, relative
        )
        if (
            replay_identity != identity
            or replay_raw != raw
            or not exact_json_equal(replay_row, expected_row)
        ):
            raise PathContractError(
                f"Conda installed path changed during terminal replay: {relative}"
            )
    replay_metadata_raw, replay_metadata_info = read_pinned_regular_file(
        metadata_path, reject_hardlink=False
    )
    replay_meta_fd = _open_directory_fd(conda_meta)
    try:
        after_names = sorted(
            os.listdir(replay_meta_fd), key=lambda item: item.encode("utf-8")
        )
    finally:
        os.close(replay_meta_fd)
    if (
        replay_metadata_raw != metadata_raw
        or _stat_identity(replay_metadata_info) != _stat_identity(metadata_info)
        or after_names != before_names
    ):
        raise PathContractError("Conda metadata changed during manifest replay")
    return (
        CONDA_MANIFEST_ALGORITHM,
        len(rows),
        sha256_bytes(canonical_json_bytes(rows)),
    )


def recompute_python_flint_manifest(
    record_path: str, record_raw: bytes
) -> tuple[int, str]:
    """Replay every exact python-flint RECORD file and its installed root."""

    record = safe_absolute_path(record_path, "python-flint RECORD")
    if type(record_raw) is not bytes:
        raise ProductionAuthorityError("python-flint RECORD image must be bytes")
    site_packages = record.parents[1]
    try:
        parsed = list(
            csv.reader(io.StringIO(record_raw.decode("utf-8"), newline=""))
        )
    except (UnicodeDecodeError, csv.Error) as error:
        raise ProductionAuthorityError(
            "python-flint RECORD is not strict UTF-8 CSV"
        ) from error
    if len(parsed) != PYTHON_FLINT_INSTALLED_FILE_COUNT:
        raise ProductionAuthorityError(
            "python-flint RECORD must contain exactly 139 installed files"
        )
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    captures: list[
        tuple[Path, bytes, tuple[int, int, int, int, int]]
    ] = []
    for index, record_row in enumerate(parsed):
        if len(record_row) != 3:
            raise ProductionAuthorityError(
                f"python-flint RECORD row {index} is malformed"
            )
        relative_raw, declared_digest, declared_size = record_row
        relative = safe_relative_path(relative_raw)
        relative_text = relative.as_posix()
        if relative_text in seen:
            raise ProductionAuthorityError("python-flint RECORD repeats a path")
        seen.add(relative_text)
        target = site_packages.joinpath(*relative.parts)
        raw, info = read_pinned_regular_file(target, reject_hardlink=False)
        digest = sha256_bytes(raw)
        if declared_digest:
            if not declared_digest.startswith("sha256="):
                raise ProductionAuthorityError(
                    "python-flint RECORD uses a non-SHA256 digest"
                )
            encoded = declared_digest.removeprefix("sha256=")
            try:
                decoded = base64.urlsafe_b64decode(
                    encoded + "=" * (-len(encoded) % 4)
                )
            except Exception as error:
                raise ProductionAuthorityError(
                    "python-flint RECORD digest is malformed"
                ) from error
            if decoded.hex() != digest or declared_size != str(len(raw)):
                raise ProductionAuthorityError(
                    "python-flint RECORD differs from installed bytes"
                )
        elif declared_size != "":
            raise ProductionAuthorityError(
                "python-flint RECORD has size without digest"
            )
        rows.append(
            {
                "mode": f"{stat.S_IMODE(info.st_mode):04o}",
                "path": relative_text,
                "sha256": digest,
                "size_bytes": len(raw),
            }
        )
        captures.append((target, raw, _stat_identity(info)))
    rows.sort(key=lambda row: row["path"].encode("utf-8"))
    for target, raw, identity in captures:
        replay_raw, replay_info = read_pinned_regular_file(
            target, reject_hardlink=False
        )
        if replay_raw != raw or _stat_identity(replay_info) != identity:
            raise PathContractError(
                f"python-flint installed file changed during replay: {target}"
            )
    return len(rows), sha256_bytes(canonical_json_bytes(rows))


def _git_blob_sha1(raw: bytes) -> str:
    if type(raw) is not bytes:
        raise ProductionAuthorityError("Git blob image must be exact bytes")
    framed = b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw
    return hashlib.sha1(framed, usedforsecurity=False).hexdigest()


def _read_capd_git_index(
    checkout: Path,
) -> tuple[list[tuple[str, int, str]], bytes, os.stat_result]:
    """Parse the checksum-covered, ordered v2 Git index without Git CLI."""

    git_dir_fd = _open_directory_fd(checkout / ".git")
    os.close(git_dir_fd)
    raw, info = read_pinned_regular_file(
        checkout / ".git/index", reject_hardlink=False
    )
    if len(raw) < 32 or raw[:4] != b"DIRC":
        raise ProductionAuthorityError("CAPD Git index header is malformed")
    version, count = struct.unpack_from(">II", raw, 4)
    if version != 2 or count <= 0:
        raise ProductionAuthorityError("CAPD Git index is not a nonempty v2 index")
    body, checksum = raw[:-20], raw[-20:]
    if hashlib.sha1(body, usedforsecurity=False).digest() != checksum:
        raise ProductionAuthorityError("CAPD Git index checksum mismatch")
    fixed_format = ">LLLLLLLLLL20sH"
    fixed_size = struct.calcsize(fixed_format)
    cursor = 12
    records: list[tuple[str, int, str]] = []
    for index in range(count):
        entry_start = cursor
        if cursor + fixed_size > len(body):
            raise ProductionAuthorityError(
                f"CAPD Git index entry {index} is truncated"
            )
        fields = struct.unpack_from(fixed_format, body, cursor)
        mode, object_id, flags = fields[6], fields[10].hex(), fields[11]
        cursor += fixed_size
        if flags & 0xF000:
            raise ProductionAuthorityError(
                "CAPD Git index uses staged/extended entries"
            )
        try:
            path_end = body.index(b"\x00", cursor)
        except ValueError as error:
            raise ProductionAuthorityError(
                "CAPD Git index path is unterminated"
            ) from error
        path_raw = body[cursor:path_end]
        try:
            path_text = path_raw.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ProductionAuthorityError(
                "CAPD Git index path is not UTF-8"
            ) from error
        relative = safe_relative_path(path_text).as_posix()
        if flags & 0x0FFF != min(len(path_raw), 0x0FFF):
            raise ProductionAuthorityError(
                "CAPD Git index path-length flag mismatch"
            )
        if mode not in (0o100644, 0o100755, 0o120000):
            raise ProductionAuthorityError(
                "CAPD Git index contains an unsupported mode"
            )
        cursor = path_end + 1
        while (cursor - entry_start) % 8:
            if cursor >= len(body) or body[cursor] != 0:
                raise ProductionAuthorityError(
                    "CAPD Git index entry padding is malformed"
                )
            cursor += 1
        records.append((relative, mode, object_id))
    while cursor < len(body):
        if cursor + 8 > len(body):
            raise ProductionAuthorityError("CAPD Git index extension is truncated")
        signature = body[cursor : cursor + 4]
        extension_size = struct.unpack_from(">I", body, cursor + 4)[0]
        cursor += 8
        if (
            re.fullmatch(rb"[A-Z]{4}", signature) is None
            or extension_size > len(body) - cursor
        ):
            raise ProductionAuthorityError(
                "CAPD Git index extension is malformed or required"
            )
        cursor += extension_size
    if len({path for path, _, _ in records}) != len(records) or records != sorted(
        records, key=lambda item: item[0].encode("utf-8")
    ):
        raise ProductionAuthorityError(
            "CAPD Git index paths are duplicate or unordered"
        )
    return records, raw, info


def _git_index_tree_oid(records: list[tuple[str, int, str]]) -> str:
    """Recursively reproduce Git's tree object from stage-zero index rows."""

    def node() -> dict[str, dict[str, Any]]:
        return {"files": {}, "directories": {}}

    root = node()
    for relative, mode, object_id in records:
        parts = PurePosixPath(relative).parts
        current = root
        for part in parts[:-1]:
            if part in current["files"]:
                raise ProductionAuthorityError(
                    "CAPD Git index has a file/directory prefix collision"
                )
            current = current["directories"].setdefault(part, node())
        name = parts[-1]
        if name in current["files"] or name in current["directories"]:
            raise ProductionAuthorityError(
                "CAPD Git index has a duplicate tree entry"
            )
        current["files"][name] = (mode, object_id)

    def digest_tree(current: dict[str, dict[str, Any]]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, (mode, object_id) in current["files"].items():
            name_raw = name.encode("utf-8")
            payload = (
                f"{mode:06o}".encode("ascii")
                + b" " + name_raw + b"\x00" + bytes.fromhex(object_id)
            )
            entries.append((name_raw, payload))
        for name, child in current["directories"].items():
            name_raw = name.encode("utf-8")
            child_id = digest_tree(child)
            payload = b"40000 " + name_raw + b"\x00" + bytes.fromhex(child_id)
            entries.append((name_raw + b"/", payload))
        content = b"".join(payload for _, payload in sorted(entries))
        framed = b"tree " + str(len(content)).encode("ascii") + b"\x00" + content
        return hashlib.sha1(framed, usedforsecurity=False).hexdigest()

    return digest_tree(root)


def _inflate_git_object(raw: bytes, context: str) -> bytes:
    inflater = zlib.decompressobj()
    try:
        inflated = inflater.decompress(raw, 4 * 1024 * 1024 + 1)
    except zlib.error as error:
        raise ProductionAuthorityError(
            f"{context} zlib stream is malformed"
        ) from error
    if (
        not inflater.eof
        or len(inflated) > 4 * 1024 * 1024
        or inflater.unconsumed_tail
    ):
        raise ProductionAuthorityError(
            f"{context} zlib stream exceeds its exact bound"
        )
    return inflated


def _parse_git_object(
    framed: bytes, expected_oid: str, expected_kind: bytes, context: str
) -> bytes:
    if hashlib.sha1(framed, usedforsecurity=False).hexdigest() != expected_oid:
        raise ProductionAuthorityError(f"{context} Git object ID mismatch")
    try:
        header, payload = framed.split(b"\x00", 1)
        kind, size_raw = header.split(b" ", 1)
        size = int(size_raw.decode("ascii"))
    except (ValueError, UnicodeDecodeError) as error:
        raise ProductionAuthorityError(
            f"{context} Git object header is malformed"
        ) from error
    if (
        kind != expected_kind
        or str(size).encode("ascii") != size_raw
        or size != len(payload)
    ):
        raise ProductionAuthorityError(f"{context} Git object kind/size mismatch")
    return payload


def _git_packed_commit_object(git_dir: Path, object_id: str) -> bytes | None:
    """Resolve a non-delta commit through a checksum-verified pack index v2."""

    pack_dir = git_dir / "objects/pack"
    try:
        pack_fd = _open_directory_fd(pack_dir)
    except (FileNotFoundError, NotADirectoryError):
        return None
    else:
        os.close(pack_fd)
    index_names = sorted(
        entry.name
        for entry in os.scandir(pack_dir)
        if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name) is not None
    )
    matches: list[bytes] = []
    needle = bytes.fromhex(object_id)
    for index_name in index_names:
        index_raw, _ = read_pinned_regular_file(
            pack_dir / index_name, reject_hardlink=False
        )
        if (
            len(index_raw) < 8 + 256 * 4 + 40
            or index_raw[:4] != b"\xfftOc"
            or struct.unpack_from(">I", index_raw, 4)[0] != 2
            or hashlib.sha1(index_raw[:-20], usedforsecurity=False).digest()
            != index_raw[-20:]
        ):
            raise ProductionAuthorityError(
                "CAPD Git pack index identity/checksum mismatch"
            )
        fanout = struct.unpack_from(">256I", index_raw, 8)
        if any(left > right for left, right in zip(fanout, fanout[1:])):
            raise ProductionAuthorityError("CAPD Git pack index fanout is unordered")
        count = fanout[-1]
        names_offset = 8 + 256 * 4
        crc_offset = names_offset + count * 20
        offsets_offset = crc_offset + count * 4
        large_offset = offsets_offset + count * 4
        if large_offset + 40 > len(index_raw):
            raise ProductionAuthorityError("CAPD Git pack index tables are truncated")
        lower = fanout[needle[0] - 1] if needle[0] else 0
        upper = fanout[needle[0]]
        found_index: int | None = None
        while lower < upper:
            middle = (lower + upper) // 2
            candidate = index_raw[
                names_offset + middle * 20 : names_offset + (middle + 1) * 20
            ]
            if candidate < needle:
                lower = middle + 1
            else:
                upper = middle
        if lower < count and index_raw[
            names_offset + lower * 20 : names_offset + (lower + 1) * 20
        ] == needle:
            found_index = lower
        if found_index is None:
            continue
        packed_offset = struct.unpack_from(
            ">I", index_raw, offsets_offset + found_index * 4
        )[0]
        if packed_offset & 0x80000000:
            large_index = packed_offset & 0x7FFFFFFF
            location = large_offset + large_index * 8
            if location + 8 > len(index_raw) - 40:
                raise ProductionAuthorityError(
                    "CAPD Git pack large-offset table is malformed"
                )
            packed_offset = struct.unpack_from(">Q", index_raw, location)[0]
        pack_name = index_name[:-4] + ".pack"
        pack_raw, _ = read_pinned_regular_file(
            pack_dir / pack_name, reject_hardlink=False
        )
        if (
            len(pack_raw) < 32
            or pack_raw[:4] != b"PACK"
            or struct.unpack_from(">I", pack_raw, 4)[0] not in (2, 3)
            or hashlib.sha1(pack_raw[:-20], usedforsecurity=False).digest()
            != pack_raw[-20:]
            or index_raw[-40:-20] != pack_raw[-20:]
            or packed_offset < 12
            or packed_offset >= len(pack_raw) - 20
        ):
            raise ProductionAuthorityError("CAPD Git pack identity/checksum mismatch")
        cursor = packed_offset
        first = pack_raw[cursor]
        cursor += 1
        object_type = (first >> 4) & 7
        object_size = first & 0x0F
        shift = 4
        current = first
        while current & 0x80:
            if cursor >= len(pack_raw) - 20 or shift > 60:
                raise ProductionAuthorityError(
                    "CAPD Git packed-object header is malformed"
                )
            current = pack_raw[cursor]
            cursor += 1
            object_size |= (current & 0x7F) << shift
            shift += 7
        if object_type != 1:
            raise ProductionAuthorityError(
                "CAPD HEAD commit is stored as an unsupported Git delta"
            )
        payload = _inflate_git_object(
            pack_raw[cursor:-20], "CAPD packed HEAD commit"
        )
        if len(payload) != object_size:
            raise ProductionAuthorityError("CAPD packed HEAD commit size mismatch")
        matches.append(
            b"commit " + str(len(payload)).encode("ascii") + b"\x00" + payload
        )
    if len(matches) > 1:
        raise ProductionAuthorityError("CAPD HEAD object is ambiguously packed")
    return matches[0] if matches else None


def _git_commit_tree_oid(git_dir: Path, commit: str) -> str:
    loose_path = git_dir / "objects" / commit[:2] / commit[2:]
    framed: bytes | None = None
    try:
        loose_raw, _ = read_pinned_regular_file(loose_path, reject_hardlink=False)
    except PathContractError:
        pass
    else:
        framed = _inflate_git_object(loose_raw, "CAPD loose HEAD commit")
    packed = _git_packed_commit_object(git_dir, commit)
    if framed is not None and packed is not None:
        raise ProductionAuthorityError(
            "CAPD HEAD object is ambiguously loose and packed"
        )
    framed = framed if framed is not None else packed
    if framed is None:
        raise ProductionAuthorityError("CAPD HEAD commit object is unavailable")
    payload = _parse_git_object(
        framed, commit, b"commit", "CAPD HEAD commit"
    )
    match = re.match(rb"tree ([0-9a-f]{40})\n", payload)
    if match is None:
        raise ProductionAuthorityError(
            "CAPD HEAD commit has no canonical tree header"
        )
    return match.group(1).decode("ascii")


def _capd_namespace_signature(
    checkout: Path, tracked: frozenset[str]
) -> tuple[tuple[str, str, tuple[int, int, int, int, int]], ...]:
    """Capture the exact clean namespace, excluding only .git/build-mp."""

    expected_directories: set[str] = set()
    for relative in tracked:
        parent = PurePosixPath(relative).parent
        while parent != PurePosixPath("."):
            expected_directories.add(parent.as_posix())
            parent = parent.parent
    observed_files: set[str] = set()
    observed_directories: set[str] = set()
    rows: list[tuple[str, str, tuple[int, int, int, int, int]]] = []
    pending = [checkout]
    while pending:
        directory = pending.pop()
        try:
            entries = sorted(
                os.scandir(directory), key=lambda item: item.name.encode("utf-8")
            )
        except UnicodeError as error:
            raise PathContractError("CAPD namespace name is not UTF-8") from error
        for entry in entries:
            relative = Path(entry.path).relative_to(checkout).as_posix()
            if relative in {".git", "build-mp"}:
                continue
            info = entry.stat(follow_symlinks=False)
            if stat.S_ISDIR(info.st_mode):
                observed_directories.add(relative)
                rows.append((relative, "DIRECTORY", _stat_identity(info)))
                pending.append(Path(entry.path))
            elif stat.S_ISREG(info.st_mode):
                observed_files.add(relative)
                rows.append((relative, "REGULAR", _stat_identity(info)))
            elif stat.S_ISLNK(info.st_mode):
                observed_files.add(relative)
                rows.append((relative, "SYMLINK", _stat_identity(info)))
            else:
                raise PathContractError(
                    f"unsupported CAPD namespace entry: {relative}"
                )
    if observed_files != set(tracked) or observed_directories != expected_directories:
        raise PathContractError(
            "CAPD checkout has tracked or untracked namespace drift"
        )
    rows.sort(key=lambda row: row[0].encode("utf-8"))
    return tuple(rows)


def _capd_tracked_image(
    checkout: Path, relative: str, git_mode: int
) -> tuple[bytes, os.stat_result]:
    target = checkout.joinpath(*safe_relative_path(relative).parts)
    if git_mode == 0o120000:
        raw, info = _conda_symlink_image(target)
        if not stat.S_ISLNK(info.st_mode):
            raise PathContractError(
                f"CAPD indexed symlink is not a live symlink: {relative}"
            )
        return raw, info
    raw, info = read_pinned_regular_file(target, reject_hardlink=False)
    expected_executable = git_mode == 0o100755
    if bool(stat.S_IMODE(info.st_mode) & 0o111) is not expected_executable:
        raise PathContractError(
            f"CAPD tracked file mode differs from Git index: {relative}"
        )
    return raw, info


def recompute_capd_git_index_tree(
    checkout_path: str,
) -> tuple[str, str, str]:
    """Replay detached HEAD, v2 index, tracked bytes, and clean namespace.

    The returned tuple is ``(algorithm, commit, live_tree_root)``.  The root
    is the SHA-256 of the compact ordered row array; the separate HEAD-tree
    equality gate is applied by the same replay once the commit-object image
    is resolved below.
    """

    checkout = safe_absolute_path(checkout_path, "CAPD checkout")
    descriptor = _open_directory_fd(checkout)
    os.close(descriptor)
    head_raw, head_info = read_pinned_regular_file(
        checkout / ".git/HEAD", reject_hardlink=False
    )
    if re.fullmatch(rb"[0-9a-f]{40}\n", head_raw) is None:
        raise ProductionAuthorityError(
            "CAPD Git HEAD is not detached at an exact commit"
        )
    commit = head_raw[:-1].decode("ascii")
    records, index_raw, index_info = _read_capd_git_index(checkout)
    index_tree = _git_index_tree_oid(records)
    head_tree = _git_commit_tree_oid(checkout / ".git", commit)
    if index_tree != head_tree:
        raise ProductionAuthorityError(
            "CAPD Git index tree differs from detached HEAD tree"
        )
    tracked = frozenset(path for path, _, _ in records)
    namespace_before = _capd_namespace_signature(checkout, tracked)
    rows: list[dict[str, Any]] = []
    captures: list[
        tuple[str, int, str, bytes, tuple[int, int, int, int, int]]
    ] = []
    for relative, git_mode, object_id in records:
        raw, info = _capd_tracked_image(checkout, relative, git_mode)
        if _git_blob_sha1(raw) != object_id:
            raise ProductionAuthorityError(
                f"CAPD tracked bytes differ from Git index: {relative}"
            )
        row = {
            "git_blob_sha1": object_id,
            "mode": f"{git_mode:06o}",
            "path": relative,
            "sha256": sha256_bytes(raw),
            "size_bytes": len(raw),
        }
        exact_keys(row, CAPD_TREE_ROW_KEYS, "CAPD live tree row")
        rows.append(row)
        captures.append(
            (relative, git_mode, object_id, raw, _stat_identity(info))
        )

    for relative, git_mode, object_id, raw, identity in captures:
        replay_raw, replay_info = _capd_tracked_image(
            checkout, relative, git_mode
        )
        if (
            _stat_identity(replay_info) != identity
            or replay_raw != raw
            or _git_blob_sha1(replay_raw) != object_id
        ):
            raise PathContractError(
                f"CAPD tracked image changed during terminal replay: {relative}"
            )
    replay_head, replay_head_info = read_pinned_regular_file(
        checkout / ".git/HEAD", reject_hardlink=False
    )
    _, replay_index, replay_index_info = _read_capd_git_index(checkout)
    namespace_after = _capd_namespace_signature(checkout, tracked)
    if (
        replay_head != head_raw
        or _stat_identity(replay_head_info) != _stat_identity(head_info)
        or replay_index != index_raw
        or _stat_identity(replay_index_info) != _stat_identity(index_info)
        or namespace_after != namespace_before
    ):
        raise PathContractError("CAPD Git namespace changed during live replay")
    return (
        CAPD_TREE_ALGORITHM,
        commit,
        sha256_bytes(canonical_json_bytes(rows)),
    )


def _validate_formal_machine_envelope_once(machine: Any) -> dict[str, Any]:
    """Validate the exact, non-self-authorizing machine-freeze schema."""

    exact_keys(machine, MACHINE_FREEZE_KEYS, "machine freeze")
    exact_int(machine.get("schema_version"), "machine-freeze schema", minimum=1)
    if machine["schema_version"] != SCHEMA_VERSION:
        raise ProductionAuthorityError("machine-freeze schema version mismatch")
    if machine.get("protocol_id") != PROTOCOL_ID:
        raise ProductionAuthorityError("machine-freeze protocol mismatch")
    if machine.get("artifact_role") != "MACHINE_FREEZE":
        raise ProductionAuthorityError("machine-freeze role mismatch")
    if machine.get("status") != "FROZEN_FOR_PRODUCTION":
        raise ProductionAuthorityError("machine-freeze status is not accepted")
    if machine.get("authority") != "MACHINE_ADMISSION_ONLY":
        raise ProductionAuthorityError("machine-freeze authority mismatch")
    if machine.get("scientific_licensing_enabled") is not True:
        raise ProductionAuthorityError("machine freeze does not enable licensing")
    if machine["production_authorized"] is not False:
        raise ProductionAuthorityError("machine freeze cannot self-authorize production")
    nested = (
        ("capture", MACHINE_CAPTURE_KEYS),
        ("machine_requirements", MACHINE_REQUIREMENT_KEYS),
        ("machine_observations", MACHINE_OBSERVATION_KEYS),
        ("python_arb", MACHINE_PYTHON_ARB_KEYS),
        ("capd", MACHINE_CAPD_KEYS),
        ("compiler", MACHINE_COMPILER_KEYS),
        ("branch_binary", MACHINE_BRANCH_BINARY_KEYS),
        ("resource_evidence", MACHINE_RESOURCE_EVIDENCE_KEYS),
        ("resource_admission", MACHINE_RESOURCE_ADMISSION_KEYS),
        ("filesystem", MACHINE_FILESYSTEM_KEYS),
    )
    for key, keys in nested:
        exact_keys(machine[key], keys, f"machine freeze {key}")
    if not exact_json_equal(machine["machine_requirements"], formal_machine_requirements()):
        raise ProductionAuthorityError("machine requirements differ from the frozen policy")
    _exact_positive_ints(machine["machine_observations"], "machine_observations")
    requirements = machine["machine_requirements"]
    observations = machine["machine_observations"]
    if requirements["logical_cpu_count"] != observations["logical_cpu_count"] or requirements[
        "memory_limit_bytes"
    ] != observations["memory_limit_bytes"]:
        raise ProductionAuthorityError("machine requirements/observations mismatch")
    if len(os.sched_getaffinity(0)) != requirements["logical_cpu_count"]:
        raise ProductionAuthorityError("live CPU affinity count mismatch")
    memory_limit_path = Path("/sys/fs/cgroup/memory/memory.limit_in_bytes")
    try:
        live_memory_limit = int(
            memory_limit_path.read_text(encoding="ascii").strip()
        )
    except (OSError, UnicodeError, ValueError) as error:
        raise ProductionAuthorityError(
            "live cgroup memory limit is unavailable or malformed"
        ) from error
    if live_memory_limit != requirements["memory_limit_bytes"]:
        raise ProductionAuthorityError("live cgroup memory limit mismatch")
    capture = machine["capture"]
    timestamp = _exact_utc_timestamp(
        capture["captured_at_utc"], "machine capture timestamp"
    )
    try:
        capture_time = datetime.strptime(
            timestamp, "%Y-%m-%dT%H:%M:%SZ"
        ).replace(tzinfo=timezone.utc)
        uptime_seconds = Decimal(
            Path("/proc/uptime").read_text(encoding="ascii").split()[0]
        )
    except (OSError, UnicodeError, ValueError, IndexError, ArithmeticError) as error:
        raise ProductionAuthorityError(
            "machine capture time/live uptime is malformed"
        ) from error
    age_seconds = (datetime.now(timezone.utc) - capture_time).total_seconds()
    if age_seconds < -300.0 or age_seconds > float(uptime_seconds) + 300.0:
        raise ProductionAuthorityError(
            "machine capture timestamp is outside the live boot window"
        )
    capture_tool_relative = safe_relative_path(capture["capture_tool_path"])
    expected_capture_tool = dict(FORMAL_INPUT_ROLES)["scheduler"]
    if capture_tool_relative.as_posix() != expected_capture_tool:
        raise ProductionAuthorityError("machine capture tool role mismatch")
    _exact_sha(capture["capture_tool_sha256"], "machine capture tool hash")
    _exact_sha(capture["boot_id_sha256"], "machine boot-id hash")
    project_root_for_capture = safe_absolute_path(
        machine["filesystem"]["project_root"], "machine project root"
    )
    capture_raw, _ = read_pinned_regular_file(
        project_root_for_capture.joinpath(*capture_tool_relative.parts)
    )
    if sha256_bytes(capture_raw) != capture["capture_tool_sha256"]:
        raise ProductionAuthorityError("machine capture tool live hash mismatch")
    if sha256_bytes(_live_boot_id_bytes()) != capture["boot_id_sha256"]:
        raise ProductionAuthorityError("machine boot ID changed after capture")
    admission = machine["resource_admission"]
    for key in (
        "static_required_bytes", "branch_required_bytes", "admitted_required_bytes",
        "admission_limit_bytes",
    ):
        exact_int(admission[key], f"resource_admission.{key}", minimum=1)
    for key in ("static_inequality_passed", "branch_inequality_passed", "storage_launch_passed"):
        if type(admission[key]) is not bool:
            raise ProductionAuthorityError(f"resource_admission.{key} must be exact Boolean")
    expected_static = observations["idle_baseline_rss_bytes"] + requirements[
        "static_workers"
    ] * observations["representative_static_peak_rss_bytes"] + requirements["reserve_bytes"]
    expected_branch = observations["idle_baseline_rss_bytes"] + requirements[
        "branch_workers"
    ] * observations["representative_branch_peak_rss_bytes"] + requirements["reserve_bytes"]
    if admission["static_required_bytes"] != expected_static or admission[
        "branch_required_bytes"
    ] != expected_branch or admission["admitted_required_bytes"] != max(expected_static, expected_branch):
        raise ProductionAuthorityError("machine resource equation mismatch")
    if admission["admission_limit_bytes"] != requirements["memory_admission_limit_bytes"]:
        raise ProductionAuthorityError("machine admission limit mismatch")
    if admission["static_inequality_passed"] is not (expected_static <= admission["admission_limit_bytes"]):
        raise ProductionAuthorityError("static admission Boolean mismatch")
    if admission["branch_inequality_passed"] is not (expected_branch <= admission["admission_limit_bytes"]):
        raise ProductionAuthorityError("branch admission Boolean mismatch")
    if admission["storage_launch_passed"] is not (
        observations["result_parent_free_bytes"] >= requirements["launch_free_bytes"]
    ):
        raise ProductionAuthorityError("storage admission Boolean mismatch")
    if (
        admission["static_inequality_passed"] is not True
        or admission["branch_inequality_passed"] is not True
        or admission["storage_launch_passed"] is not True
    ):
        raise ProductionAuthorityError("machine resource admission did not pass")
    compiler = machine["compiler"]
    safe_absolute_path(compiler["executable_path"], "compiler executable")
    _exact_sha(compiler["executable_sha256"], "compiler executable hash")
    _exact_nonempty_string(compiler["version"], "compiler version")
    compiler_raw, _, _ = _read_external_pinned_path(
        compiler["executable_path"], "compiler executable"
    )
    if sha256_bytes(compiler_raw) != compiler["executable_sha256"]:
        raise ProductionAuthorityError("compiler executable live hash mismatch")
    if compiler["version"] != MACHINE_COMPILER_VERSION:
        raise ProductionAuthorityError("compiler version mismatch")
    exact_keys(compiler["build_record"], MACHINE_BUILD_RECORD_KEYS, "machine build record")
    build_record = compiler["build_record"]
    safe_absolute_path(build_record["cwd"], "build cwd")
    if type(build_record["argv"]) is not list or not build_record["argv"] or not all(type(item) is str for item in build_record["argv"]):
        raise ProductionAuthorityError("machine build argv is malformed")
    if not exact_json_equal(build_record["environment"], formal_build_environment()):
        raise ProductionAuthorityError("machine build environment mismatch")
    if build_record["umask"] != "0022":
        raise ProductionAuthorityError("machine build umask mismatch")
    for key in ("stdout", "stderr"):
        if type(build_record[key]) is not str:
            raise ProductionAuthorityError(f"build_record.{key} must be exact UTF-8 text")
    if (
        build_record["argv_sha256"] != sha256_bytes(canonical_json_bytes(build_record["argv"]))
        or build_record["stdout_sha256"] != sha256_bytes(build_record["stdout"].encode("utf-8"))
        or build_record["stderr_sha256"] != sha256_bytes(build_record["stderr"].encode("utf-8"))
        or build_record["stdout"] != ""
        or build_record["stderr"] != ""
        or type(build_record["return_code"]) is not int
        or build_record["return_code"] != 0
    ):
        raise ProductionAuthorityError("machine build receipt hash/status mismatch")
    python = machine["python_arb"]
    safe_absolute_path(python["executable_path"], "Python executable")
    _exact_sha(python["executable_sha256"], "Python executable hash")
    python_raw, _, python_resolved = _read_external_pinned_path(
        python["executable_path"], "Python executable"
    )
    if sha256_bytes(python_raw) != python["executable_sha256"]:
        raise ProductionAuthorityError("Python executable live hash mismatch")
    for key in (
        "python_version", "implementation", "python_flint_version",
        "flint_version", "arb_version",
    ):
        _exact_nonempty_string(python[key], f"python_arb.{key}")
    if (
        python["implementation"] != "CPython"
        or python["python_version"] != MACHINE_PYTHON_VERSION
        or python["python_flint_version"] != "0.9.0"
        or python["flint_version"] != "3.6.0"
        or python["arb_version"] != "FLINT-3.6.0"
    ):
        raise ProductionAuthorityError("Python/Arb version binding mismatch")
    live_conda_algorithm, live_conda_count, live_conda_root = (
        recompute_conda_python_manifest(python["executable_path"])
    )
    exact_int(
        python["conda_manifest_file_count"],
        "python_arb.conda_manifest_file_count",
        minimum=1,
    )
    if (
        python["conda_manifest_algorithm"] != CONDA_MANIFEST_ALGORITHM
        or python["conda_manifest_algorithm"] != live_conda_algorithm
        or python["conda_manifest_file_count"] != live_conda_count
        or python["conda_installed_manifest_root_sha256"] != live_conda_root
    ):
        raise ProductionAuthorityError("live Conda Python manifest mismatch")
    python_identity_roots = tuple(
        python[key]
        for key in (
            "conda_installed_manifest_root_sha256",
            "python_flint_record_sha256",
            "python_flint_installed_manifest_root_sha256",
        )
    )
    for key in (
        "conda_installed_manifest_root_sha256",
        "python_flint_record_sha256",
        "python_flint_installed_manifest_root_sha256",
    ):
        _exact_sha(python[key], f"python_arb.{key}")
    if len(set(python_identity_roots)) != len(python_identity_roots):
        raise ProductionAuthorityError(
            "Conda manifest, python-flint RECORD, and installed-manifest roots "
            "must be pairwise distinct"
        )
    if (
        python["python_flint_record_sha256"] != PYTHON_FLINT_RECORD_SHA256
        or python["python_flint_installed_manifest_root_sha256"]
        != PYTHON_FLINT_INSTALLED_MANIFEST_ROOT_SHA256
    ):
        raise ProductionAuthorityError(
            "python-flint frozen RECORD/installed roots mismatch"
        )
    for key in ("arb_extension", "fmpq_extension"):
        _validate_live_elf_binding(python[key], f"python_arb.{key}")
    if (
        type(python["bundled_libraries"]) is not list
        or len(python["bundled_libraries"])
        != len(MACHINE_PYTHON_BUNDLED_SONAMES)
    ):
        raise ProductionAuthorityError("python bundled library list is malformed")
    exact_keys(machine["runtime_libraries"], MACHINE_RUNTIME_LIBRARIES_KEYS, "runtime libraries")
    expected_runtime_sonames = {
        "python_bundled": MACHINE_PYTHON_BUNDLED_SONAMES,
        "capd_system": MACHINE_CAPD_SYSTEM_SONAMES,
    }
    for domain, expected_sonames in expected_runtime_sonames.items():
        libraries = machine["runtime_libraries"][domain]
        if type(libraries) is not list or len(libraries) != len(expected_sonames):
            raise ProductionAuthorityError(f"runtime library domain is malformed: {domain}")
        paths: list[str] = []
        for index, (item, expected_soname) in enumerate(
            zip(libraries, expected_sonames, strict=True)
        ):
            _validate_live_runtime_binding(
                item,
                f"runtime library {domain}[{index}]",
                expected_soname=expected_soname,
            )
            paths.append(item["path"])
        if len(set(paths)) != len(paths):
            raise ProductionAuthorityError(
                f"runtime library {domain} repeats a live path"
            )
    if not exact_json_equal(python["bundled_libraries"], machine["runtime_libraries"]["python_bundled"]):
        raise ProductionAuthorityError("Python bundled-library closure mismatch")
    capd = machine["capd"]
    safe_absolute_path(capd["checkout_path"], "CAPD checkout")
    if type(capd["commit"]) is not str or re.fullmatch(r"[0-9a-f]{40}", capd["commit"]) is None:
        raise ProductionAuthorityError("CAPD commit must be lowercase 40-hex")
    _exact_sha(capd["tree_sha256"], "CAPD tree hash")
    if capd["tree_algorithm"] != CAPD_TREE_ALGORITHM:
        raise ProductionAuthorityError("CAPD tree algorithm mismatch")
    if capd["clean"] is not True:
        raise ProductionAuthorityError("CAPD checkout must be captured clean")
    live_capd_algorithm, live_capd_commit, live_capd_tree = (
        recompute_capd_git_index_tree(capd["checkout_path"])
    )
    if (
        live_capd_algorithm != CAPD_TREE_ALGORITHM
        or capd["commit"] != live_capd_commit
        or capd["tree_sha256"] != live_capd_tree
    ):
        raise ProductionAuthorityError("live CAPD commit/tree replay mismatch")
    for key in ("cmake_cache_path", "config_path"):
        safe_absolute_path(capd[key], f"CAPD {key}")
    for key in ("cmake_cache_sha256", "config_sha256"):
        _exact_sha(capd[key], f"CAPD {key}")
    if type(capd["raw_flags"]) is not str or not capd["raw_flags"].endswith("\n"):
        raise ProductionAuthorityError("CAPD raw flags must be exact UTF-8 text")
    if capd["raw_flags_sha256"] != sha256_bytes(capd["raw_flags"].encode("utf-8")):
        raise ProductionAuthorityError("CAPD raw flags hash mismatch")
    for key in ("libcapd", "libfilib"):
        _validate_extension_binding(capd[key], f"capd.{key}", allow_null_build_id=True)
        if capd[key]["build_id"] is not None:
            raise ProductionAuthorityError(f"CAPD static archive {key} build_id must be null")
    checkout_path = Path(capd["checkout_path"])
    expected_capd_paths = {
        "cmake_cache_path": checkout_path / "build-mp/CMakeCache.txt",
        "config_path": checkout_path / "build-mp/bin/capd-config",
        "libcapd": checkout_path / "build-mp/libcapd.a",
        "libfilib": checkout_path / "build-mp/capdExt/filibsrc/libfilib.a",
    }
    for key in ("cmake_cache_path", "config_path"):
        expected_path = expected_capd_paths[key]
        if capd[key] != str(expected_path):
            raise ProductionAuthorityError(f"CAPD {key} pinned layout mismatch")
        raw, _ = read_pinned_regular_file(expected_path)
        digest_key = key.replace("_path", "_sha256")
        if sha256_bytes(raw) != capd[digest_key]:
            raise ProductionAuthorityError(f"CAPD {key} live hash mismatch")
    for key in ("libcapd", "libfilib"):
        expected_path = expected_capd_paths[key]
        binding = capd[key]
        if binding["path"] != str(expected_path):
            raise ProductionAuthorityError(f"CAPD {key} pinned layout mismatch")
        raw, info = read_pinned_regular_file(expected_path)
        if (
            len(raw) != binding["size_bytes"]
            or sha256_bytes(raw) != binding["sha256"]
            or stat.S_IMODE(info.st_mode) != binding["mode"]
        ):
            raise ProductionAuthorityError(f"CAPD {key} live binding mismatch")
    binary = machine["branch_binary"]
    binary_relative = safe_relative_path(binary["path"])
    source_relative = safe_relative_path(binary["source_path"])
    expected_role_paths = dict(FORMAL_INPUT_ROLES)
    if (
        binary_relative.as_posix()
        != expected_role_paths["branch_evaluator_binary"]
        or source_relative.as_posix()
        != expected_role_paths["branch_evaluator_source"]
    ):
        raise ProductionAuthorityError("branch source/binary role path mismatch")
    for key in ("sha256", "source_sha256", "elf_sha256", "dt_needed_sha256", "runtime_libraries_sha256"):
        _exact_sha(binary[key], f"branch_binary.{key}")
    if type(binary["build_id"]) is not str or re.fullmatch(
        r"[0-9a-f]{40}", binary["build_id"]
    ) is None:
        raise ProductionAuthorityError("branch binary build_id must be 40-hex")
    exact_int(binary["size_bytes"], "branch binary size", minimum=1)
    exact_int(binary["executable_mode"], "branch binary mode", minimum=0)
    if binary["executable_mode"] != 0o755 or binary["elf_sha256"] != binary["sha256"]:
        raise ProductionAuthorityError("branch binary executable/ELF binding mismatch")
    if type(binary["dt_needed"]) is not list or not all(type(item) is str and item for item in binary["dt_needed"]):
        raise ProductionAuthorityError("branch DT_NEEDED is malformed")
    if binary["dt_needed"] != sorted(set(binary["dt_needed"])):
        raise ProductionAuthorityError("branch DT_NEEDED order/uniqueness mismatch")
    if binary["dt_needed"] != MACHINE_BRANCH_DT_NEEDED:
        raise ProductionAuthorityError("branch DT_NEEDED frozen closure mismatch")
    if binary["dt_needed_sha256"] != sha256_bytes(canonical_json_bytes(binary["dt_needed"])):
        raise ProductionAuthorityError("branch DT_NEEDED hash mismatch")
    if binary["runtime_libraries_sha256"] != sha256_bytes(canonical_json_bytes(machine["runtime_libraries"])):
        raise ProductionAuthorityError("branch runtime-library root mismatch")
    try:
        capd_tokens = shlex.split(capd["raw_flags"], posix=True)
    except ValueError as error:
        raise ProductionAuthorityError("CAPD raw flags cannot be tokenized") from error
    checkout = capd["checkout_path"]
    expected_capd_tokens = [
        "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
        "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
        "-DFILIB_HAVE_SSE", f"-I{checkout}/capdDynSys/include",
        f"-I{checkout}/capdAlg/include", f"-I{checkout}/capdAux/include",
        f"-I{checkout}/capdExt/include", f"-I{checkout}/capdExt/filibsrc",
        f"-L{checkout}/build-mp", f"-L{checkout}/build-mp/capdExt/filibsrc",
        "-lcapd", "-lfilib", "-lmpfr", "-lgmp",
    ]
    if capd_tokens != expected_capd_tokens:
        raise ProductionAuthorityError("CAPD ordered raw-flag contract mismatch")
    project_root = machine["filesystem"]["project_root"]
    project_root_path = safe_absolute_path(project_root, "machine project root")
    live_binary_raw, live_binary_info = read_pinned_regular_file(
        project_root_path.joinpath(*binary_relative.parts)
    )
    live_source_raw, _ = read_pinned_regular_file(
        project_root_path.joinpath(*source_relative.parts)
    )
    live_build_id, live_dt_needed, live_soname = _elf_metadata(
        live_binary_raw, "persistent branch binary"
    )
    if (
        sha256_bytes(live_binary_raw) != binary["sha256"]
        or len(live_binary_raw) != binary["size_bytes"]
        or stat.S_IMODE(live_binary_info.st_mode) != binary["executable_mode"]
        or sha256_bytes(live_source_raw) != binary["source_sha256"]
        or live_build_id != binary["build_id"]
        or live_dt_needed != binary["dt_needed"]
        or live_soname is not None
    ):
        raise ProductionAuthorityError(
            "persistent branch binary/source live replay mismatch"
        )
    expected_build_argv = [
        compiler["executable_path"], "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(Path(project_root) / binary["source_path"]), *capd_tokens,
        "-o", str(Path(project_root) / binary["path"]),
    ]
    if build_record["cwd"] != project_root or not exact_json_equal(build_record["argv"], expected_build_argv):
        raise ProductionAuthorityError("machine build argv/cwd mismatch")
    evidence = machine["resource_evidence"]
    static_raw_text = evidence["static_payload_raw_utf8"]
    branch_raw_text = evidence["branch_payload_raw_utf8"]
    if type(static_raw_text) is not str or type(branch_raw_text) is not str:
        raise ProductionAuthorityError("resource payload images must be exact UTF-8 strings")
    static_raw = static_raw_text.encode("utf-8")
    branch_raw = branch_raw_text.encode("utf-8")
    if (
        evidence["static_payload_sha256"] != sha256_bytes(static_raw)
        or evidence["branch_payload_sha256"] != sha256_bytes(branch_raw)
    ):
        raise ProductionAuthorityError("resource payload raw hash mismatch")
    static_payload = strict_json_loads(static_raw_text)
    branch_payload = strict_json_loads(branch_raw_text)
    if static_raw != canonical_json_bytes(static_payload):
        raise ProductionAuthorityError("static resource payload is not CJ_COMPACT_V1")
    if branch_raw != pretty_json_bytes(branch_payload):
        raise ProductionAuthorityError("branch resource payload is not CJ_PRETTY_2_V1")
    _validate_static_resource_payload(
        static_payload, requirements, observations, project_root_for_capture
    )
    _validate_branch_resource_payload(
        branch_payload,
        requirements,
        observations,
        project_root_for_capture,
        binary["sha256"],
    )
    static_bindings = static_payload["bindings"]
    flint_binding = static_bindings["python_flint"]
    module_raw, _, module_resolved = _read_external_pinned_path(
        flint_binding["module_path"], "python-flint module"
    )
    if not module_raw:
        raise ProductionAuthorityError("python-flint module is empty")
    record_raw, _, record_resolved = _read_external_pinned_path(
        flint_binding["record_path"], "python-flint RECORD"
    )
    site_packages = record_resolved.parent.parent
    expected_dist_info = f"python_flint-{python['python_flint_version']}.dist-info"
    expected_module = site_packages / "flint/__init__.py"
    expected_arb = site_packages / "flint/types/arb.abi3.so"
    expected_fmpq = site_packages / "flint/types/fmpq.abi3.so"
    if (
        record_resolved.name != "RECORD"
        or record_resolved.parent.name != expected_dist_info
        or module_resolved != expected_module
        or flint_binding["module_path"] != str(expected_module)
        or flint_binding["record_path"] != str(record_resolved)
        or flint_binding["arb_extension_path"] != str(expected_arb)
        or python["arb_extension"]["path"] != str(expected_arb)
        or python["fmpq_extension"]["path"] != str(expected_fmpq)
    ):
        raise ProductionAuthorityError(
            "python-flint module/RECORD/arb/fmpq site-packages layout mismatch"
        )
    installed_count, installed_root = recompute_python_flint_manifest(
        str(record_resolved), record_raw
    )
    if (
        static_bindings["interpreter"]["invocation_path"]
        != python["executable_path"]
        or static_bindings["interpreter"]["resolved_path"]
        != str(python_resolved)
        or static_bindings["interpreter"]["sha256"] != python["executable_sha256"]
        or static_bindings["interpreter"]["size_bytes"] != len(python_raw)
        or static_bindings["interpreter"]["version"] != python["python_version"]
        or static_bindings["python_flint"]["version"] != python["python_flint_version"]
        or static_bindings["python_flint"]["flint_version"] != python["flint_version"]
        or static_bindings["python_flint"]["installed_manifest_sha256"]
        != python["python_flint_installed_manifest_root_sha256"]
        or static_bindings["python_flint"]["installed_record_file_count"]
        != installed_count
        or installed_count != PYTHON_FLINT_INSTALLED_FILE_COUNT
        or installed_root
        != python["python_flint_installed_manifest_root_sha256"]
        or static_bindings["python_flint"]["record_sha256"]
        != python["python_flint_record_sha256"]
        or sha256_bytes(record_raw) != python["python_flint_record_sha256"]
        or static_bindings["python_flint"]["arb_extension_sha256"]
        != python["arb_extension"]["sha256"]
    ):
        raise ProductionAuthorityError("machine Python/Arb chain differs from static calibration")
    static_admission = static_payload["admission"]
    branch_admission = branch_payload["admission"]
    if (
        observations["idle_baseline_rss_bytes"]
        != max(static_admission["idle_baseline_bytes"], branch_admission["baseline_bytes"])
        or observations["representative_static_peak_rss_bytes"]
        != static_admission["representative_peak_rss_bytes"]
        or observations["representative_branch_peak_rss_bytes"]
        != branch_admission["peak_rss_bytes"]
    ):
        raise ProductionAuthorityError("machine observations do not conservatively transfer calibration evidence")
    if evidence["persistent_binary_sha256"] != binary["sha256"]:
        raise ProductionAuthorityError("resource evidence persistent binary transfer mismatch")
    for key in ("static_payload_sha256", "branch_payload_sha256", "persistent_binary_sha256"):
        _exact_sha(evidence[key], f"resource evidence {key}")
    fs = machine["filesystem"]
    for key in ("project_root", "result_parent", "operational_parent"):
        safe_absolute_path(fs[key], f"machine filesystem {key}")
    for key in ("project_device_id", "result_device_id", "operational_device_id"):
        exact_int(fs[key], f"machine filesystem {key}", minimum=1)
    expected_parent = project_root_for_capture / "results"
    if (
        fs["project_root"] != str(project_root_for_capture)
        or fs["result_parent"] != str(expected_parent)
        or fs["operational_parent"] != str(expected_parent)
    ):
        raise ProductionAuthorityError("machine filesystem pinned layout mismatch")
    observed_devices: list[int] = []
    for key in ("project_root", "result_parent", "operational_parent"):
        descriptor = _open_directory_fd(Path(fs[key]))
        try:
            observed_devices.append(os.fstat(descriptor).st_dev)
        finally:
            os.close(descriptor)
    if (
        fs["same_filesystem"] is not True
        or len(set(observed_devices)) != 1
        or [
            fs["project_device_id"],
            fs["result_device_id"],
            fs["operational_device_id"],
        ]
        != observed_devices
    ):
        raise ProductionAuthorityError("machine filesystem admission mismatch")
    filesystem_stats = os.statvfs(expected_parent)
    current_free = filesystem_stats.f_bavail * filesystem_stats.f_frsize
    if current_free < requirements["launch_free_bytes"]:
        raise ProductionAuthorityError("live filesystem no longer passes launch gate")
    if machine["claim_boundary"] != MACHINE_CLAIM_BOUNDARY:
        raise ProductionAuthorityError("machine freeze claim boundary mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if machine[key] is not None:
            raise ProductionAuthorityError(f"machine freeze overclaims {key}")
    return dict(machine)


def _validate_formal_machine_envelope(machine: Any) -> dict[str, Any]:
    """Validate one machine generation and terminally replay external paths."""

    global _ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS
    if _ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS is not None:
        return _validate_formal_machine_envelope_once(machine)
    captures: dict[
        Path,
        tuple[
            tuple[int, int, int, int, int],
            Path,
            bytes,
            tuple[int, int, int, int, int],
        ],
    ] = {}
    _ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS = captures
    try:
        validated = _validate_formal_machine_envelope_once(machine)
        for lexical, (
            expected_lexical,
            expected_resolved,
            expected_raw,
            expected_target,
        ) in captures.items():
            lexical_info = os.lstat(lexical)
            resolved = lexical.resolve(strict=True)
            raw, info = read_pinned_regular_file(resolved)
            if (
                _stat_identity(lexical_info) != expected_lexical
                or resolved != expected_resolved
                or raw != expected_raw
                or _stat_identity(info) != expected_target
            ):
                raise PathContractError(
                    f"external machine path changed during validation: {lexical}"
                )
        return validated
    finally:
        _ACTIVE_FORMAL_MACHINE_EXTERNAL_PATHS = None


def _validate_formal_main_envelope(
    main: Any,
    input_roles: Sequence[FormalRoleRecord],
    machine_sha256: str,
) -> dict[str, Any]:
    """Validate the exact main-freeze schema and ordered role/hash DAG."""

    exact_keys(main, MAIN_FREEZE_KEYS, "main freeze")
    for forbidden in ("sha256", "freeze_sha256", "main_freeze_sha256"):
        if forbidden in main:
            raise ProductionAuthorityError("main freeze must not contain a self hash")
    exact_int(main["schema_version"], "main-freeze schema", minimum=1)
    if main["schema_version"] != SCHEMA_VERSION:
        raise ProductionAuthorityError("main-freeze schema version mismatch")
    if main["protocol_id"] != PROTOCOL_ID or main["artifact_role"] != "MAIN_FREEZE":
        raise ProductionAuthorityError("main-freeze identity mismatch")
    if (
        main["status"] != "FROZEN_FOR_PRODUCTION"
        or main["authority"] != "INDEPENDENT_PREFREEZE_REVIEW"
        or main["scientific_licensing_enabled"] is not True
    ):
        raise ProductionAuthorityError("main freeze has no accepted formal authority")
    if main["matrix_id"] != canonical_matrix_id() or not exact_json_equal(
        main["matrix"], matrix_payload()
    ):
        raise ProductionAuthorityError("main-freeze matrix mismatch")
    if main["machine_freeze_sha256"] != machine_sha256:
        raise ProductionAuthorityError("main/machine freeze hash mismatch")
    expected_roles = [item.payload() for item in input_roles]
    if not exact_json_equal(main["input_roles"], expected_roles):
        raise ProductionAuthorityError("main freeze ordered 53-role handshake mismatch")
    for item in main["input_roles"]:
        exact_keys(item, {"role", "path", "sha256"}, "formal input role")
        safe_relative_path(item["path"])
        if type(item["role"]) is not str or not item["role"]:
            raise ProductionAuthorityError("formal input role name is malformed")
        if type(item["sha256"]) is not str or HEX_SHA256.fullmatch(item["sha256"]) is None:
            raise ProductionAuthorityError("formal input role hash is malformed")
    roles = {item.role: item for item in input_roles}
    if len(roles) != 53:
        raise ProductionAuthorityError("main freeze role names are not unique")
    review = main["prefreeze_review"]
    exact_keys(review, PREFREEZE_REVIEW_BINDING_KEYS, "main pre-freeze review")
    if not exact_json_equal(
        review,
        {
            "path": roles["prefreeze_review"].path,
            "sha256": roles["prefreeze_review"].sha256,
            "verdict": "ACCEPT_FOR_FREEZE",
        },
    ):
        raise ProductionAuthorityError("main pre-freeze review binding mismatch")
    expected_exact_sections = {
        "serializers": formal_serializers(),
        "scheduler": formal_scheduler_policy(),
        "limits": formal_limits(),
        "status_tables": formal_status_tables(),
        "archive_layout": formal_archive_layout(),
        "machine_requirements": formal_machine_requirements(),
        "failure_policy": formal_failure_policy(),
        "execution_policy": formal_execution_policy(),
    }
    for key, expected in expected_exact_sections.items():
        if not exact_json_equal(main[key], expected):
            raise ProductionAuthorityError(f"main-freeze exact section mismatch: {key}")
    expected_evaluators = {
        "static": {
            "path": roles["static_evaluator"].path,
            "sha256": roles["static_evaluator"].sha256,
            "abi": "PYTHON_STATIC_ABI_26_STRINGS_V1",
            "argv_count": 26,
        },
        "branch": {
            "source_path": roles["branch_evaluator_source"].path,
            "source_sha256": roles["branch_evaluator_source"].sha256,
            "binary_path": roles["branch_evaluator_binary"].path,
            "binary_sha256": roles["branch_evaluator_binary"].sha256,
            "runtime_path": roles["branch_runtime"].path,
            "runtime_sha256": roles["branch_runtime"].sha256,
            "abi": "CAPD_BRANCH_ABI_12_STRINGS_V1",
            "argv_count": 12,
        },
    }
    if not exact_json_equal(main["evaluators"], expected_evaluators):
        raise ProductionAuthorityError("main-freeze evaluator bindings mismatch")
    expected_checkers = {
        name: {"path": roles[role].path, "sha256": roles[role].sha256}
        for name, role in (
            ("static", "static_checker_source"),
            ("branch", "branch_checker_source"),
            ("composite", "composite_checker_source"),
            ("release_builder", "release_builder"),
        )
    }
    if not exact_json_equal(main["checkers"], expected_checkers):
        raise ProductionAuthorityError("main-freeze checker bindings mismatch")
    if main["claim_boundary"] != MAIN_FREEZE_CLAIM_BOUNDARY:
        raise ProductionAuthorityError("main-freeze claim boundary mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if main[key] is not None:
            raise ProductionAuthorityError(f"main freeze overclaims {key}")
    return dict(main)


def load_formal_authority(
    authority_root: Path | str = ROOT,
) -> FormalAuthoritySnapshot:
    """Capture and replay a prospective authority without authorizing dispatch."""

    root = safe_absolute_path(os.fspath(authority_root), "authority root")
    require_directory(root)
    bindings, images = capture_formal_input_roles(root)
    roles = {item.role: item for item in bindings}

    # Executable code cannot validate a different frozen scheduler/runtime than
    # the bytes it is actually using, even in a preflight-only handshake.
    live_bindings = {
        "scheduler": SCRIPT,
        "branch_runtime": BRANCH_RUNTIME_PATH,
    }
    for role, live_path in live_bindings.items():
        if roles[role].sha256 != sha256(live_path):
            raise ProductionAuthorityError(f"live {role} bytes differ from frozen role")

    machine_binding = roles["machine_freeze"]
    try:
        machine_payload = strict_json_loads(images["machine_freeze"].decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("machine freeze is not UTF-8") from error
    if images["machine_freeze"] != canonical_json_bytes(machine_payload):
        raise StrictJSONError("machine freeze is not canonical JSON")
    machine = _validate_formal_machine_envelope(machine_payload)
    if not exact_json_equal(machine["machine_requirements"], formal_machine_requirements()):
        raise ProductionAuthorityError("machine/main implementation policy mismatch")
    if (
        machine["capture"]["capture_tool_path"] != roles["scheduler"].path
        or machine["capture"]["capture_tool_sha256"] != roles["scheduler"].sha256
    ):
        raise ProductionAuthorityError("machine capture tool is not role 19 scheduler")
    binary = machine["branch_binary"]
    if (
        binary["path"] != roles["branch_evaluator_binary"].path
        or binary["sha256"] != roles["branch_evaluator_binary"].sha256
        or binary["size_bytes"] != len(roles["branch_evaluator_binary"].raw)
        or binary["source_path"] != roles["branch_evaluator_source"].path
        or binary["source_sha256"] != roles["branch_evaluator_source"].sha256
    ):
        raise ProductionAuthorityError("machine persistent branch binary/source role mismatch")
    evidence = machine["resource_evidence"]
    static_calibration = strict_json_loads(evidence["static_payload_raw_utf8"])
    branch_calibration = strict_json_loads(evidence["branch_payload_raw_utf8"])
    if (
        static_calibration["bindings"]["evaluator"]["sha256"]
        != roles["static_evaluator"].sha256
        or static_calibration["bindings"]["plan"]["sha256"]
        != roles["l1_final_plan"].sha256
        or static_calibration["bindings"]["interpreter"]["sha256"]
        != machine["python_arb"]["executable_sha256"]
        or static_calibration["bindings"]["python_flint"]["arb_extension_sha256"]
        != machine["python_arb"]["arb_extension"]["sha256"]
    ):
        raise ProductionAuthorityError("static calibration is stale against frozen roles/toolchain")
    if (
        branch_calibration["binary_sha256"] != roles["branch_evaluator_binary"].sha256
        or evidence["persistent_binary_sha256"] != roles["branch_evaluator_binary"].sha256
    ):
        raise ProductionAuthorityError("branch calibration is stale against persistent binary")
    filesystem = machine["filesystem"]
    if (
        filesystem["project_root"] != str(root)
        or filesystem["result_parent"] != str(root / "results")
        or filesystem["operational_parent"] != str(root / "results")
    ):
        raise ProductionAuthorityError("machine filesystem roots mismatch authority root")
    binary_path = authority_project_file(root, roles["branch_evaluator_binary"].path)
    binary_info = binary_path.stat()
    results_info = (root / "results").stat()
    if (
        binary["executable_mode"] != (binary_info.st_mode & 0o777)
        or binary_info.st_size != binary["size_bytes"]
        or filesystem["project_device_id"] != root.stat().st_dev
        or filesystem["result_device_id"] != results_info.st_dev
        or filesystem["operational_device_id"] != results_info.st_dev
    ):
        raise ProductionAuthorityError("machine live mode/size/filesystem identity mismatch")

    review_path = authority_project_file(root, dict(FORMAL_INPUT_ROLES)["prefreeze_review"])
    review_sha256 = validate_prefreeze_review(review_path)
    if review_sha256 != roles["prefreeze_review"].sha256:
        raise ProductionAuthorityError("pre-freeze review changed during authority capture")

    main_path = authority_project_file(
        root, "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
    )
    main_payload, main_raw, main_info = strict_json_image(
        main_path, require_canonical=True
    )
    main = _validate_formal_main_envelope(
        main_payload, bindings, machine_binding.sha256
    )
    if not exact_json_equal(main["machine_requirements"], machine["machine_requirements"]):
        raise ProductionAuthorityError("main/machine requirements mismatch")
    main_sha256 = sha256_bytes(main_raw)

    # End-of-handshake replay closes the interval in which any role or main
    # freeze could otherwise be swapped after its semantic parse.
    replay_bindings, _ = capture_formal_input_roles(root)
    if replay_bindings != bindings:
        raise ProductionAuthorityError("formal input changed during authority handshake")
    replay_main, replay_raw, replay_info = strict_json_image(
        main_path, require_canonical=True
    )
    if (
        not exact_json_equal(replay_main, main)
        or replay_raw != main_raw
        or (
            replay_info.st_dev,
            replay_info.st_ino,
            replay_info.st_size,
            replay_info.st_mtime_ns,
            replay_info.st_ctime_ns,
        )
        != (
            main_info.st_dev,
            main_info.st_ino,
            main_info.st_size,
            main_info.st_mtime_ns,
            main_info.st_ctime_ns,
        )
    ):
        raise ProductionAuthorityError("main freeze changed during authority handshake")
    return FormalAuthoritySnapshot(
        authority_root=root,
        main_freeze_path=main_path,
        main_freeze_sha256=main_sha256,
        machine_freeze_path=authority_project_file(
            root, dict(FORMAL_INPUT_ROLES)["machine_freeze"]
        ),
        machine_freeze_sha256=machine_binding.sha256,
        prefreeze_review_path=review_path,
        prefreeze_review_sha256=review_sha256,
        input_roles=bindings,
        main_freeze_raw=main_raw,
        main_freeze_stat_identity=(
            main_info.st_dev,
            main_info.st_ino,
            main_info.st_size,
            main_info.st_mtime_ns,
            main_info.st_ctime_ns,
        ),
        machine_freeze_raw=images["machine_freeze"],
    )


def validate_production_authority(authority_root: Path = ROOT) -> None:
    """Compatibility gate: validate if possible, then always reject execution."""

    try:
        load_formal_authority(authority_root)
    except (FileNotFoundError, PathContractError) as error:
        raise ProductionAuthorityError(
            f"formal authority is absent or unsafe; production rejected: {error}"
        ) from error
    raise ProductionAuthorityError(
        "formal scientific dispatch is unconditionally disabled pending finalized contracts"
    )


def operational_root_for(output: Path) -> Path:
    return output.with_name(output.name + ".operational")


def staging_basename(
    cell: CellKey,
    run_config_sha256: str,
    attempt: int = 0,
) -> str:
    if (
        type(run_config_sha256) is not str
        or HEX_SHA256.fullmatch(run_config_sha256) is None
    ):
        raise PathContractError("run-config digest is not an exact SHA-256")
    exact_int(attempt, "staging attempt", minimum=0)
    name = f".{cell.slab_id}.tmp-{run_config_sha256[:16]}-{attempt}"
    if STAGING_BASENAME.fullmatch(name) is None:
        raise PathContractError(f"invalid staging basename: {name}")
    return name


def staging_path(
    operational: Path,
    cell: CellKey,
    run_config_sha256: str,
    attempt: int = 0,
) -> Path:
    return (
        operational
        / "staging"
        / "static"
        / str(cell.precision_bits)
        / staging_basename(cell, run_config_sha256, attempt)
    )


def validate_static_staging_namespace(
    operational: Path, run_config_sha256: str
) -> dict[tuple[int, str], Path]:
    root = operational / "staging" / "static"
    if not path_lexists(root):
        return {}
    require_directory(root)
    precision_names = {path.name for path in root.iterdir()}
    if not precision_names <= {str(bits) for bits in PRECISIONS}:
        raise CorruptGeneration(
            f"static staging precision namespace mismatch: {precision_names}"
        )
    expected_prefix = run_config_sha256[:16]
    active: dict[tuple[int, str], Path] = {}
    for precision_root in root.iterdir():
        require_directory(precision_root)
        precision_bits = int(precision_root.name)
        for stage in precision_root.iterdir():
            match = STAGING_BASENAME.fullmatch(stage.name)
            if match is None:
                raise CorruptGeneration(f"invalid static staging name: {stage.name}")
            slab_id, generation_prefix, _attempt = match.groups()
            if generation_prefix != expected_prefix:
                raise CorruptGeneration(
                    f"foreign-generation static staging name: {stage.name}"
                )
            key = (precision_bits, slab_id)
            if key in active:
                raise CorruptGeneration(
                    f"multiple active static staging owners for {slab_id}"
                )
            active[key] = stage
            require_directory(stage)
    return active


def static_cell_path(output: Path, cell: CellKey) -> Path:
    return output / "static" / "cells" / str(cell.precision_bits) / cell.slab_id


def static_manifest_path(output: Path, cell: CellKey) -> Path:
    return output / "static" / "cell_manifests" / str(cell.precision_bits) / f"{cell.slab_id}.json"


def static_aggregate_summary_path(output: Path) -> Path:
    return output / "static" / "aggregate_summary.json"


def static_aggregate_manifest_path(output: Path) -> Path:
    return output / "static" / "aggregate_manifest.json"


def mock_proof(cell: CellKey, matrix_id: str, run_config_sha256: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_PROOF",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "cell": cell.payload(),
        "matrix_id": matrix_id,
        "run_config_sha256": run_config_sha256,
        "synthetic_trees": ["ANGLE", "SECTION_LOW", "SECTION_HIGH", "SECTION_WINDOW"],
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def mock_record(
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
    proof_sha256: str,
    proof_size_bytes: int,
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_CELL_RECORD",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "cell": cell.payload(),
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "returncode": 0,
        "evaluator_payload": {
            "path": "proof.json",
            "sha256": proof_sha256,
            "size_bytes": proof_size_bytes,
        },
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_mock_cell_directory(
    directory: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    require_directory(directory)
    actual = {path.name for path in directory.iterdir()}
    if actual != {"proof.json", "record.json"}:
        raise CorruptGeneration(f"mock cell file set mismatch: {actual}")
    for child in directory.iterdir():
        require_regular_file(child)
    proof, proof_raw, proof_info = strict_json_image(
        directory / "proof.json", require_canonical=True
    )
    record, record_raw, record_info = strict_json_image(
        directory / "record.json", require_canonical=True
    )
    expected_proof = mock_proof(cell, matrix_id, run_config_sha256)
    if not exact_json_equal(proof, expected_proof):
        raise CorruptGeneration("mock proof content mismatch")
    expected_record = mock_record(
        cell,
        matrix_id,
        run_config_sha256,
        sha256_bytes(proof_raw),
        proof_info.st_size,
    )
    if not exact_json_equal(record, expected_record):
        raise CorruptGeneration("mock record content mismatch")
    return proof, record, {
        "proof.json": {
            "sha256": sha256_bytes(proof_raw),
            "size_bytes": proof_info.st_size,
        },
        "record.json": {
            "sha256": sha256_bytes(record_raw),
            "size_bytes": record_info.st_size,
        },
    }


def derive_static_manifest(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    directory = static_cell_path(output, cell)
    _, _, bindings = validate_mock_cell_directory(
        directory, cell, matrix_id, run_config_sha256
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_CELL_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "cell": cell.payload(),
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "files": bindings,
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_static_manifest(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    return validate_static_manifest_image(
        output, cell, matrix_id, run_config_sha256
    )[0]


def validate_static_manifest_image(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    target = static_manifest_path(output, cell)
    stored, raw, info = strict_json_image(target, require_canonical=True)
    expected = derive_static_manifest(output, cell, matrix_id, run_config_sha256)
    if not exact_json_equal(stored, expected):
        raise CorruptGeneration("static cell manifest mismatch")
    return dict(stored), {
        "sha256": sha256_bytes(raw),
        "size_bytes": info.st_size,
    }


def validate_static_cell_namespace(output: Path) -> None:
    """Require exactly 102 cell directories with exactly two files each."""

    root = output / "static" / "cells"
    require_directory(root)
    precision_names = {path.name for path in root.iterdir()}
    if precision_names != {str(bits) for bits in PRECISIONS}:
        raise CorruptGeneration(
            f"static cell precision namespace mismatch: {precision_names}"
        )
    for bits in PRECISIONS:
        precision_root = root / str(bits)
        require_directory(precision_root)
        expected = set(SLAB_IDS)
        actual = {path.name for path in precision_root.iterdir()}
        if actual != expected:
            raise CorruptGeneration(
                f"static cell namespace mismatch for {bits}: {actual}"
            )
        for slab in SLAB_IDS:
            directory = precision_root / slab
            require_directory(directory)
            names = {path.name for path in directory.iterdir()}
            if names != {"proof.json", "record.json"}:
                raise CorruptGeneration(
                    f"static cell file namespace mismatch for {bits}:{slab}: {names}"
                )
            for path in directory.iterdir():
                require_regular_file(path)


def validate_static_manifest_namespace(output: Path) -> None:
    """Require the full 102-manifest namespace and no aliases or extras."""

    root = output / "static" / "cell_manifests"
    require_directory(root)
    precision_names = {path.name for path in root.iterdir()}
    if precision_names != {str(bits) for bits in PRECISIONS}:
        raise CorruptGeneration(
            f"static manifest precision namespace mismatch: {precision_names}"
        )
    for bits in PRECISIONS:
        precision_root = root / str(bits)
        require_directory(precision_root)
        expected = {f"{slab}.json" for slab in SLAB_IDS}
        actual = {path.name for path in precision_root.iterdir()}
        if actual != expected:
            raise CorruptGeneration(
                f"static manifest namespace mismatch for {bits}: {actual}"
            )
        for path in precision_root.iterdir():
            require_regular_file(path)


def validate_mock_authoritative_namespace(output: Path) -> None:
    """Reject every unexpected authoritative object, including hidden paths."""

    require_directory(output)
    output_names = {path.name for path in output.iterdir()}
    if not {"run_config.json", "static"} <= output_names or not output_names <= {
        "run_config.json",
        "static",
        "branch",
        "independent_static_checker.json",
        "STATIC_POSTCHECK_STATUS.json",
        "independent_branch_checker.json",
        "BRANCH_POSTCHECK_STATUS.json",
        "composite_summary.json",
        "composite_manifest.json",
        "independent_checker.json",
        "POSTCHECK_STATUS.json",
    }:
        raise CorruptGeneration(
            f"mock authoritative root namespace mismatch: {output_names}"
        )
    require_regular_file(run_config_path(output))
    if "branch" in output_names:
        require_directory(output / "branch")
    for name in (
        "independent_static_checker.json",
        "STATIC_POSTCHECK_STATUS.json",
        "independent_branch_checker.json",
        "BRANCH_POSTCHECK_STATUS.json",
        "composite_summary.json",
        "composite_manifest.json",
        "independent_checker.json",
        "POSTCHECK_STATUS.json",
    ):
        if name in output_names:
            require_regular_file(output / name)
    static_root = output / "static"
    require_directory(static_root)
    aggregate_names = {
        path.name
        for path in (
            static_aggregate_summary_path(output),
            static_aggregate_manifest_path(output),
        )
        if path.exists()
    }
    if aggregate_names == {"aggregate_manifest.json"}:
        raise CorruptGeneration("static aggregate manifest exists without summary")
    permitted_aggregate_states = (
        set(),
        {"aggregate_summary.json"},
        {"aggregate_summary.json", "aggregate_manifest.json"},
    )
    if aggregate_names not in permitted_aggregate_states:
        raise CorruptGeneration("invalid static aggregate namespace state")
    expected = {"cells", "cell_manifests"} | aggregate_names
    actual = {path.name for path in static_root.iterdir()}
    if actual != expected:
        raise CorruptGeneration(f"static authoritative namespace mismatch: {actual}")
    validate_static_cell_namespace(output)
    validate_static_manifest_namespace(output)


def ordered_static_manifest_entries(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
) -> list[dict[str, Any]]:
    active_staging = validate_static_staging_namespace(
        operational_root_for(output), run_config_sha256
    )
    if active_staging:
        labels = sorted(f"{bits}:{slab}" for bits, slab in active_staging)
        raise CorruptGeneration(
            "static aggregate cannot coexist with live staging owners: "
            + ",".join(labels)
        )
    validate_mock_authoritative_namespace(output)
    entries: list[dict[str, Any]] = []
    for cell in exact_matrix():
        path = static_manifest_path(output, cell)
        _, binding = validate_static_manifest_image(
            output, cell, matrix_id, run_config_sha256
        )
        entries.append(
            {
                "cell": cell.payload(),
                "path": path.relative_to(output).as_posix(),
                "sha256": binding["sha256"],
                "size_bytes": binding["size_bytes"],
            }
        )
    return entries


def build_static_aggregate_summary(
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
) -> dict[str, Any]:
    if len(entries) != 102:
        raise CorruptGeneration("static aggregate requires exactly 102 cell manifests")
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_AGGREGATE_SUMMARY",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "matrix": matrix_payload(),
        "cell_count": 102,
        "ordered_cell_manifest_root": sha256_bytes(canonical_json_bytes(entries)),
        "status_counts": {"STATIC_CELL_CERTIFIED": 102},
        "scheduler_classification_counts": {"COMMITTED_EVALUATOR_RESULT": 102},
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def build_static_aggregate_manifest(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
    summary: Mapping[str, Any],
) -> dict[str, Any]:
    summary_bytes = canonical_json_bytes(summary)
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_STATIC_AGGREGATE_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "ordered_cell_manifest_root": sha256_bytes(canonical_json_bytes(entries)),
        "cell_manifests": entries,
        "summary": {
            "path": static_aggregate_summary_path(output).relative_to(output).as_posix(),
            "sha256": sha256_bytes(summary_bytes),
            "size_bytes": len(summary_bytes),
        },
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_static_mock_aggregate(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    summary_path = static_aggregate_summary_path(output)
    manifest_path = static_aggregate_manifest_path(output)
    if not summary_path.exists() or not manifest_path.exists():
        raise CorruptGeneration("static aggregate summary/manifest pair is incomplete")
    entries = ordered_static_manifest_entries(output, matrix_id, run_config_sha256)
    expected_summary = build_static_aggregate_summary(
        matrix_id, run_config_sha256, entries
    )
    stored_summary = strict_json_load(summary_path, require_canonical=True)
    if not exact_json_equal(stored_summary, expected_summary):
        raise CorruptGeneration("static aggregate summary mismatch")
    expected_manifest = build_static_aggregate_manifest(
        output, matrix_id, run_config_sha256, entries, expected_summary
    )
    stored_manifest = strict_json_load(manifest_path, require_canonical=True)
    if not exact_json_equal(stored_manifest, expected_manifest):
        raise CorruptGeneration("static aggregate manifest mismatch")
    return dict(stored_summary), dict(stored_manifest)


def finalize_static_mock_aggregate(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
) -> tuple[str, dict[str, Any], dict[str, Any]]:
    """Publish the mock aggregate with the manifest as the commit marker."""

    summary_path = static_aggregate_summary_path(output)
    manifest_path = static_aggregate_manifest_path(output)
    if manifest_path.exists():
        summary, manifest = validate_static_mock_aggregate(
            output, matrix_id, run_config_sha256
        )
        return "RESUMED_COMMITTED", summary, manifest

    entries = ordered_static_manifest_entries(output, matrix_id, run_config_sha256)
    summary = build_static_aggregate_summary(matrix_id, run_config_sha256, entries)
    manifest = build_static_aggregate_manifest(
        output, matrix_id, run_config_sha256, entries, summary
    )
    if summary_path.exists():
        stored_summary = strict_json_load(summary_path, require_canonical=True)
        if not exact_json_equal(stored_summary, summary):
            raise CorruptGeneration("manifest-less aggregate summary mismatch")
        state = "RECOVERED_MANIFEST"
    else:
        exclusive_write_json(summary_path, summary)
        state = "COMMITTED"
    exclusive_write_json(manifest_path, manifest)
    checked_summary, checked_manifest = validate_static_mock_aggregate(
        output, matrix_id, run_config_sha256
    )
    return state, checked_summary, checked_manifest


def publish_manifestless_cell(
    output: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
) -> dict[str, Any]:
    target = static_manifest_path(output, cell)
    if target.exists():
        return validate_static_manifest(output, cell, matrix_id, run_config_sha256)
    manifest = derive_static_manifest(output, cell, matrix_id, run_config_sha256)
    exclusive_write_json(target, manifest)
    return manifest


def write_mock_stage(stage: Path, cell: CellKey, matrix_id: str, run_config_sha256: str) -> None:
    stage.parent.mkdir(parents=True, exist_ok=True)
    if stage.exists():
        raise CorruptGeneration(f"live staging path already exists: {stage}")
    stage.mkdir(mode=0o755)
    fsync_directory(stage.parent)
    proof_payload = canonical_json_bytes(mock_proof(cell, matrix_id, run_config_sha256))
    exclusive_write_bytes(stage / "proof.json", proof_payload)
    record_payload = canonical_json_bytes(
        mock_record(
            cell,
            matrix_id,
            run_config_sha256,
            sha256_bytes(proof_payload),
            len(proof_payload),
        )
    )
    exclusive_write_bytes(stage / "record.json", record_payload)
    fsync_directory(stage)


def commit_mock_static_cell(
    output: Path,
    operational: Path,
    cell: CellKey,
    matrix_id: str,
    run_config_sha256: str,
    *,
    fail_after_cell_rename: bool = False,
) -> tuple[str, dict[str, Any]]:
    ensure_same_filesystem(output, operational)
    target = static_cell_path(output, cell)
    manifest_target = static_manifest_path(output, cell)
    stage = staging_path(operational, cell, run_config_sha256)
    active_staging = validate_static_staging_namespace(
        operational, run_config_sha256
    )
    existing_stage = active_staging.get((cell.precision_bits, cell.slab_id))
    if existing_stage is not None and existing_stage != stage:
        raise CorruptGeneration(
            f"noncanonical active staging attempt for {cell.label}: {existing_stage.name}"
        )

    if manifest_target.exists():
        return "RESUMED_COMMITTED", validate_static_manifest(
            output, cell, matrix_id, run_config_sha256
        )
    if target.exists():
        return "RECOVERED_MANIFEST", publish_manifestless_cell(
            output, cell, matrix_id, run_config_sha256
        )
    if stage.exists():
        validate_mock_cell_directory(stage, cell, matrix_id, run_config_sha256)
    else:
        write_mock_stage(stage, cell, matrix_id, run_config_sha256)

    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise CorruptGeneration(f"canonical cell already exists: {target}")
    rename_directory_noreplace(stage, target)
    fsync_directory(stage.parent)
    fsync_directory(target.parent)
    if fail_after_cell_rename:
        raise SyntheticCrash("synthetic crash after canonical cell rename")
    return "COMMITTED", publish_manifestless_cell(
        output, cell, matrix_id, run_config_sha256
    )


def canonical_decimal_token(value: Decimal | str) -> str:
    """Serialize one finite exact decimal without exponent or lexical aliases."""

    try:
        parsed = value if isinstance(value, Decimal) else Decimal(value)
    except (InvalidOperation, ValueError, TypeError) as error:
        raise StrictJSONError(f"invalid exact decimal token: {value!r}") from error
    if not parsed.is_finite():
        raise StrictJSONError("exact decimal token must be finite")
    text = format(parsed, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    if text in {"", "-0", "+0"}:
        return "0"
    return text


def exact_primary_root_box(plan_record: Mapping[str, Any]) -> tuple[tuple[str, str], ...]:
    """Rebuild the exact pre-outward L1 box from plan center and radii."""

    exact_keys(
        plan_record,
        {
            "center",
            "epsilon_lower",
            "epsilon_upper",
            "floating_residual_inf",
            "root_radii",
            "slab_id",
        },
        "L1 plan slab record",
    )
    center = plan_record["center"]
    radii = plan_record["root_radii"]
    coordinate_order = ("q_slow", "q_fast", "p_slow", "period")
    exact_keys(center, set(coordinate_order), "L1 plan center")
    exact_keys(radii, set(coordinate_order), "L1 plan root radii")
    box: list[tuple[str, str]] = []
    for name in coordinate_order:
        if type(center[name]) is not str or type(radii[name]) is not str:
            raise StrictJSONError(f"L1 plan {name} center/radius must be strings")
        try:
            midpoint = Decimal(center[name])
            radius = Decimal(radii[name])
        except InvalidOperation as error:
            raise StrictJSONError(f"L1 plan {name} is not an exact decimal") from error
        if not midpoint.is_finite() or not radius.is_finite() or radius <= 0:
            raise StrictJSONError(f"L1 plan {name} radius/domain is invalid")
        with localcontext() as context:
            context.prec = 256
            lower = midpoint - radius
            upper = midpoint + radius
        box.append(
            (
                canonical_decimal_token(lower),
                canonical_decimal_token(upper),
            )
        )
    return tuple(box)


def accepted_l1_primary_records(
    path: Path = L1_ACCEPTED_SUMMARY,
) -> dict[tuple[int, str], Mapping[str, Any]]:
    """Index the exact accepted L1 summary primary records."""

    payload = strict_json_load(path, reject_hardlink=False)
    return accepted_l1_primary_records_payload(payload)


def accepted_l1_primary_records_payload(
    payload: Any,
) -> dict[tuple[int, str], Mapping[str, Any]]:
    if type(payload) is not dict or type(payload.get("records")) is not list:
        raise StrictJSONError("accepted L1 summary lacks a records array")
    if payload.get("milestone_status") != "PASS_CONTIGUOUS_LOCAL_BRANCH":
        raise StrictJSONError("accepted L1 summary milestone is not passing")
    index: dict[tuple[int, str], Mapping[str, Any]] = {}
    for record in payload["records"]:
        if type(record) is not dict or record.get("job_type") != "primary":
            continue
        precision = record.get("precision_bits")
        slab_id = record.get("job_id")
        if (
            type(precision) is not int
            or precision not in PRECISIONS
            or type(slab_id) is not str
            or slab_id not in SLAB_IDS
        ):
            raise StrictJSONError("accepted L1 primary identity is malformed")
        key = (precision, slab_id)
        if key in index:
            raise StrictJSONError(f"duplicate accepted L1 primary record: {key}")
        if (
            record.get("status") != "PASS_LOCAL_SLAB"
            or record.get("passed") is not True
            or record.get("returncode") != 0
            or type(record.get("returncode")) is not int
        ):
            raise StrictJSONError(f"accepted L1 primary record is not passing: {key}")
        index[key] = record
    expected = {(bits, slab) for bits in PRECISIONS for slab in SLAB_IDS}
    if set(index) != expected:
        raise StrictJSONError("accepted L1 primary record matrix is not exact")
    return index


def _validate_l1_record_against_plan(
    record: Mapping[str, Any],
    plan_record: Mapping[str, Any],
    cell: CellKey,
) -> None:
    center = plan_record["center"]
    radii = plan_record["root_radii"]
    expected_argv = [
        str(cell.precision_bits),
        plan_record["epsilon_lower"],
        plan_record["epsilon_upper"],
        center["q_slow"],
        center["q_fast"],
        center["p_slow"],
        center["period"],
        radii["q_slow"],
        radii["q_fast"],
        radii["p_slow"],
        radii["period"],
    ]
    if not exact_json_equal(record.get("command_arguments"), expected_argv):
        raise StrictJSONError(
            f"accepted L1 primary command differs from exact plan: {cell.label}"
        )
    expected_raw = f"raw/{cell.precision_bits}/primary/{cell.slab_id}.txt"
    expected_stderr = (
        f"raw/{cell.precision_bits}/primary/{cell.slab_id}.stderr.txt"
    )
    if record.get("raw_file") != expected_raw or record.get("stderr_file") != expected_stderr:
        raise StrictJSONError(f"accepted L1 primary raw path mismatch: {cell.label}")


def validate_mock_branch_evaluator(
    output: Path, evaluator: Path
) -> dict[str, Any]:
    """Bind one explicit synthetic executable outside both result roots."""

    output = output.absolute()
    operational = operational_root_for(output)
    supplied = evaluator.absolute()
    reject_symlink_components(supplied, allow_missing_leaf=False)
    resolved = supplied.resolve(strict=True)
    if supplied != resolved:
        raise PathContractError("mock branch evaluator path must be canonical")
    require_regular_file(resolved)
    info = resolved.stat()
    if info.st_mode & 0o111 == 0:
        raise PathContractError("mock branch evaluator is not executable")
    if is_within(resolved, output) or is_within(resolved, operational):
        raise PathContractError("mock branch evaluator must live outside result roots")
    raw, _ = read_pinned_regular_file(resolved)
    return {
        "path": str(resolved),
        "sha256": sha256_bytes(raw),
    }


def mock_branch_bindings(
    matrix_id: str,
    run_config_sha256: str,
    mock_evaluator: Mapping[str, Any],
) -> Any:
    """Construct a visibly synthetic binding accepted by the hardened runtime."""

    exact_keys(mock_evaluator, {"path", "sha256"}, "mock evaluator binding")
    return _branch_runtime().BranchBindings(
        matrix_id=matrix_id,
        freeze_sha256=sha256_bytes(
            b"R401-VAL-L3-A1 mock freeze absent sentinel\n"
        ),
        run_config_sha256=run_config_sha256,
        evaluator_source_path=mock_evaluator["path"],
        evaluator_source_sha256=mock_evaluator["sha256"],
        evaluator_binary_sha256=mock_evaluator["sha256"],
        capd_commit="0" * 40,
        capd_flags_sha256=sha256_bytes(
            b"R401-VAL-L3-A1 mock CAPD flags absent sentinel\n"
        ),
        runtime_libraries_sha256=sha256_bytes(
            b"R401-VAL-L3-A1 mock runtime libraries absent sentinel\n"
        ),
    )


def build_branch_tasks(
    evaluator: Path,
    *,
    plan_path: Path = PLAN,
    l1_summary_path: Path = L1_ACCEPTED_SUMMARY,
) -> tuple[Any, ...]:
    """Build the exact 102 pre-outward branch tasks in protocol order."""

    return build_branch_tasks_from_payloads(
        evaluator,
        strict_json_load(plan_path, reject_hardlink=False),
        strict_json_load(l1_summary_path, reject_hardlink=False),
    )


def build_branch_tasks_from_payloads(
    evaluator: Path,
    plan_payload: Any,
    l1_summary_payload: Any,
    *,
    runtime: Any | None = None,
) -> tuple[Any, ...]:
    evaluator_path = str(evaluator.absolute())
    plan = validate_plan_payload(plan_payload)
    accepted = accepted_l1_primary_records_payload(l1_summary_payload)
    runtime = _branch_runtime() if runtime is None else runtime
    tasks: list[Any] = []
    for cell in exact_matrix():
        plan_record = plan[cell.slab_id]
        record = accepted[(cell.precision_bits, cell.slab_id)]
        _validate_l1_record_against_plan(record, plan_record, cell)
        epsilon = (
            plan_record["epsilon_lower"],
            plan_record["epsilon_upper"],
        )
        if not all(type(value) is str for value in epsilon):
            raise StrictJSONError(f"plan epsilon is not lexical: {cell.label}")
        task = runtime.BranchCellTask(
            precision_bits=cell.precision_bits,
            slab_id=cell.slab_id,
            epsilon=epsilon,
            root_box=exact_primary_root_box(plan_record),
            evaluator_binary_path=evaluator_path,
            accepted_l1_primary_record_id=(
                f"{cell.precision_bits}/{cell.slab_id}/primary"
            ),
            accepted_l1_primary_record_sha256=sha256_bytes(
                canonical_json_bytes(record)
            ),
        )
        task.validate()
        tasks.append(task)
    for slab_index, slab_id in enumerate(SLAB_IDS):
        left = tasks[slab_index]
        right = tasks[51 + slab_index]
        if left.epsilon != right.epsilon or left.root_box != right.root_box:
            raise StrictJSONError(
                f"cross-precision pre-outward domain mismatch: {slab_id}"
            )
    return tuple(tasks)


def build_mock_branch_tasks(evaluator: Path) -> tuple[Any, ...]:
    """Build the mock-bound task matrix without changing its accepted ABI."""

    return build_branch_tasks(evaluator)


def _formal_role(snapshot: FormalAuthoritySnapshot, role: str) -> FormalRoleRecord:
    matches = [item for item in snapshot.input_roles if item.role == role]
    if len(matches) != 1:
        raise ProductionAuthorityError(f"formal role is not unique: {role}")
    return matches[0]


def _stat_identity(info: os.stat_result) -> tuple[int, int, int, int, int]:
    return (
        info.st_dev,
        info.st_ino,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )


def revalidate_formal_snapshot(
    snapshot: FormalAuthoritySnapshot, roles: Sequence[str] = ()
) -> None:
    """Replay immutable main bytes and selected role inode identities."""

    main = strict_json_loads(snapshot.main_freeze_raw.decode("utf-8"))
    _validate_formal_main_envelope(
        main, snapshot.input_roles, snapshot.machine_freeze_sha256
    )
    raw, info = read_pinned_regular_file(snapshot.main_freeze_path)
    if raw != snapshot.main_freeze_raw or _stat_identity(info) != snapshot.main_freeze_stat_identity:
        raise ProductionAuthorityError("main freeze inode/image changed after snapshot")
    selected = tuple(roles) if roles else tuple(item.role for item in snapshot.input_roles)
    if len(set(selected)) != len(selected):
        raise ProductionAuthorityError("duplicate role in snapshot replay")
    for role in selected:
        record = _formal_role(snapshot, role)
        path = authority_project_file(snapshot.authority_root, record.path)
        current, current_info = read_pinned_regular_file(path)
        if current != record.raw or _stat_identity(current_info) != record.stat_identity:
            raise ProductionAuthorityError(f"formal role inode/image changed: {role}")


def _validate_preflight_for_transaction(
    snapshot: FormalAuthoritySnapshot,
    binding: Mapping[str, Any],
    run_config_sha256: str,
    output: Path,
) -> None:
    validate_formal_preflight_binding(binding, snapshot, output)
    expected_hash = sha256_bytes(canonical_json_bytes(binding))
    if run_config_sha256 != expected_hash:
        raise ProductionAuthorityError("formal transaction run-config hash mismatch")
    if binding["freeze_sha256"] != snapshot.main_freeze_sha256:
        raise ProductionAuthorityError("formal transaction freeze hash mismatch")


def build_formal_static_transaction_plan(
    snapshot: FormalAuthoritySnapshot,
    binding: Mapping[str, Any],
    run_config_sha256: str,
    output: Path,
    cell: CellKey,
) -> FormalStaticTransactionPlan:
    """Construct, but never execute, one provisional static transaction."""

    output = ensure_formal_preflight_output_allowed(output, snapshot.authority_root)
    _validate_preflight_for_transaction(snapshot, binding, run_config_sha256, output)
    evaluator_role = _formal_role(snapshot, "static_evaluator")
    checker_role = _formal_role(snapshot, "static_checker_source")
    plan_role = _formal_role(snapshot, "l1_final_plan")
    l1_source_roles = tuple(
        _formal_role(snapshot, role) for role in FORMAL_STATIC_L1_SOURCE_ROLES
    )
    revalidate_formal_snapshot(
        snapshot,
        (
            "static_evaluator", "static_checker_source", "l1_final_plan",
            *FORMAL_STATIC_L1_SOURCE_ROLES,
        ),
    )
    evaluator_path = authority_project_file(snapshot.authority_root, evaluator_role.path)
    if not evaluator_role.raw:
        raise ProductionAuthorityError("formal static evaluator is empty")
    try:
        plan_payload = strict_json_loads(plan_role.raw.decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("captured L1 plan is not UTF-8") from error
    plan_record = validate_plan_payload(plan_payload)[cell.slab_id]
    plan_record_sha256 = sha256_bytes(canonical_json_bytes(plan_record))
    stage = (
        operational_root_for(output)
        / "staging"
        / "static"
        / str(cell.precision_bits)
        / staging_basename(cell, run_config_sha256)
    )
    proof_path = stage / "proof.json"
    execution_argv = (
        sys.executable,
        str(evaluator_path),
        "--slab-id",
        cell.slab_id,
        "--precision-bits",
        str(cell.precision_bits),
        "--epsilon-lower",
        plan_record["epsilon_lower"],
        "--epsilon-upper",
        plan_record["epsilon_upper"],
        "--matrix-id",
        canonical_matrix_id(),
        "--freeze-sha256",
        snapshot.main_freeze_sha256,
        "--run-config-sha256",
        run_config_sha256,
        "--plan-record-sha256",
        plan_record_sha256,
        "--max-depth",
        str(candidate_limits()["static"]["max_depth_per_tree"]),
        "--max-nodes-per-tree",
        str(candidate_limits()["static"]["max_nodes_per_tree"]),
        "--max-nodes-per-cell",
        str(candidate_limits()["static"]["max_nodes_per_cell"]),
        "--output",
        str(proof_path),
    )
    semantic_argv = (*execution_argv[:-1], "<STAGING_PROOF_PATH>")
    plan = FormalStaticTransactionPlan(
        cell=cell,
        evaluator_path=evaluator_path,
        evaluator_sha256=evaluator_role.sha256,
        proof_path=proof_path,
        stdout_path=stage / "stdout.txt",
        stderr_path=stage / "stderr.txt",
        record_path=stage / "record.json",
        argv=execution_argv,
        semantic_argv=semantic_argv,
        semantic_argv_sha256=sha256_bytes(canonical_json_bytes(list(semantic_argv))),
        checker_sha256=checker_role.sha256,
        l1_final_plan_sha256=plan_role.sha256,
        l1_release_chain_sha256=tuple(
            (record.path, record.sha256) for record in l1_source_roles
        ),
        matrix_id=canonical_matrix_id(),
        freeze_sha256=snapshot.main_freeze_sha256,
        main_freeze_sha256=snapshot.main_freeze_sha256,
        run_config_sha256=run_config_sha256,
    )
    plan.validate()
    return plan


def build_formal_branch_transaction_plan(
    snapshot: FormalAuthoritySnapshot,
    binding: Mapping[str, Any],
    run_config_sha256: str,
    output: Path,
    cell: CellKey,
) -> FormalBranchTransactionPlan:
    """Construct, but never execute, one persistent-binary branch task."""

    output = ensure_formal_preflight_output_allowed(output, snapshot.authority_root)
    _validate_preflight_for_transaction(snapshot, binding, run_config_sha256, output)
    source_role = _formal_role(snapshot, "branch_evaluator_source")
    binary_role = _formal_role(snapshot, "branch_evaluator_binary")
    plan_role = _formal_role(snapshot, "l1_final_plan")
    summary_role = _formal_role(snapshot, "l1_summary")
    runtime_role = _formal_role(snapshot, "branch_runtime")
    revalidate_formal_snapshot(
        snapshot,
        (
            "branch_runtime",
            "branch_evaluator_source",
            "branch_evaluator_binary",
            "l1_final_plan",
            "l1_summary",
        ),
    )
    formal_runtime = _load_formal_branch_runtime(runtime_role)
    source_path = authority_project_file(snapshot.authority_root, source_role.path)
    binary_path = authority_project_file(snapshot.authority_root, binary_role.path)
    binary_info = binary_path.stat()
    if binary_info.st_mode & 0o111 == 0:
        raise ProductionAuthorityError("formal branch persistent binary is not executable")
    try:
        plan_payload = strict_json_loads(plan_role.raw.decode("utf-8"))
        summary_payload = strict_json_loads(summary_role.raw.decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("captured L1 plan/summary is not UTF-8") from error
    tasks = build_branch_tasks_from_payloads(
        binary_path,
        plan_payload,
        summary_payload,
        runtime=formal_runtime,
    )
    task = tasks[exact_matrix().index(cell)]
    plan = FormalBranchTransactionPlan(
        task=task,
        evaluator_source_path=source_path,
        evaluator_source_sha256=source_role.sha256,
        evaluator_binary_path=binary_path,
        evaluator_binary_sha256=binary_role.sha256,
        freeze_sha256=snapshot.main_freeze_sha256,
        main_freeze_sha256=snapshot.main_freeze_sha256,
        run_config_sha256=run_config_sha256,
    )
    plan.validate()
    return plan


def _semantic_flag(plan: FormalStaticTransactionPlan, flag: str) -> str:
    positions = [index for index, value in enumerate(plan.semantic_argv) if value == flag]
    if len(positions) != 1 or positions[0] + 1 >= len(plan.semantic_argv):
        raise SchedulerContractError(f"static semantic invocation lacks exact {flag}")
    value = plan.semantic_argv[positions[0] + 1]
    if type(value) is not str:
        raise SchedulerContractError(f"static semantic invocation {flag} value is not a string")
    return value


def _formal_static_fraction_record(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def _formal_static_interval_record(
    lower: Fraction, upper: Fraction
) -> list[dict[str, str]]:
    return [
        _formal_static_fraction_record(lower),
        _formal_static_fraction_record(upper),
    ]


def _formal_static_expected_input_echo(
    plan: FormalStaticTransactionPlan,
) -> dict[str, Any]:
    return {
        "slab_id": plan.cell.slab_id,
        "precision_bits": plan.cell.precision_bits,
        "epsilon_lower": _semantic_flag(plan, "--epsilon-lower"),
        "epsilon_upper": _semantic_flag(plan, "--epsilon-upper"),
        "matrix_id": plan.matrix_id,
        "freeze_sha256": plan.freeze_sha256,
        "run_config_sha256": plan.run_config_sha256,
        "plan_record_sha256": _semantic_flag(plan, "--plan-record-sha256"),
        "max_depth": int(_semantic_flag(plan, "--max-depth")),
        "max_nodes_per_tree": int(
            _semantic_flag(plan, "--max-nodes-per-tree")
        ),
        "max_nodes_per_cell": int(
            _semantic_flag(plan, "--max-nodes-per-cell")
        ),
    }


def _validate_formal_static_nonpass_failure(
    payload: Any, evaluator_status: str
) -> None:
    if type(payload) is not dict:
        raise SchedulerContractError("formal static nonpass failure is not an exact object")
    if evaluator_status == "STATIC_UNRESOLVED_NODE_BUDGET":
        exact_keys(
            payload,
            {"scope", "tree_id", "limit", "consumed_before_node"},
            "formal static node-budget failure",
        )
        if payload["scope"] not in {"tree", "cell"} or type(payload["tree_id"]) is not str:
            raise SchedulerContractError("formal static node-budget failure identity mismatch")
        exact_int(payload["limit"], "formal static node-budget limit", minimum=1)
        exact_int(
            payload["consumed_before_node"],
            "formal static node-budget consumed count",
            minimum=0,
        )
    elif evaluator_status == "STATIC_UNRESOLVED_DEPTH":
        if set(payload) not in (
            {"tree_id", "limit", "unresolved_depth"},
            {"tree_id", "limit", "unresolved_depth", "node_id"},
        ):
            raise SchedulerContractError("formal static depth-failure key set mismatch")
        if type(payload["tree_id"]) is not str or (
            "node_id" in payload and type(payload["node_id"]) is not str
        ):
            raise SchedulerContractError("formal static depth-failure identity mismatch")
        exact_int(payload["limit"], "formal static depth limit", minimum=1)
        exact_int(
            payload["unresolved_depth"],
            "formal static unresolved depth",
            minimum=0,
        )
    elif evaluator_status == "INVALID_STATIC_PROOF_CONTRACT":
        exact_keys(payload, {"reason"}, "formal static invalid-contract failure")
        if type(payload["reason"]) is not str:
            raise SchedulerContractError("formal static invalid-contract reason is not a string")
    elif evaluator_status == "STATIC_INTERVAL_FAIL":
        exact_keys(
            payload, {"error_type", "reason"}, "formal static interval failure"
        )
        if not all(type(payload[key]) is str for key in ("error_type", "reason")):
            raise SchedulerContractError("formal static interval-failure values are not strings")
    else:
        raise SchedulerContractError("formal static nonpass evaluator status is unsupported")


def _validate_formal_static_evaluator_proof(
    plan: FormalStaticTransactionPlan,
    payload: Any,
    evaluator_status: str,
) -> None:
    """Replay the cheap exact proof ABI before a committed archive is formed.

    Arb interval arithmetic and tree semantics remain the independent
    checker's responsibility.  This gate prevents a producer from labeling a
    merely canonical or minimally forged JSON object as an evaluator result.
    """

    if type(payload) is not dict:
        raise SchedulerContractError("formal static evaluator proof is not an exact object")
    expected_keys = (
        FORMAL_STATIC_PASS_PROOF_KEYS
        if evaluator_status == "STATIC_CELL_CERTIFIED"
        else FORMAL_STATIC_NONPASS_PROOF_KEYS
    )
    exact_keys(payload, expected_keys, "formal static evaluator proof")
    if (
        type(payload["schema_version"]) is not int
        or payload["schema_version"] != SCHEMA_VERSION
        or payload["protocol_id"] != PROTOCOL_ID
        or payload["artifact_role"] != "STATIC_CELL_PROOF"
        or payload["authority"] != "PRODUCER_ONLY"
        or payload["scientific_licensing_enabled"] is not False
        or payload["matrix_id"] != plan.matrix_id
        or payload["freeze_sha256"] != plan.freeze_sha256
        or payload["run_config_sha256"] != plan.run_config_sha256
        or payload["evaluator_status"] != evaluator_status
        or payload["slab_id"] != plan.cell.slab_id
        or type(payload["precision_bits"]) is not int
        or payload["precision_bits"] != plan.cell.precision_bits
        or payload["claim_boundary"] != FORMAL_STATIC_CELL_CLAIM_BOUNDARY
    ):
        raise SchedulerContractError("formal static evaluator proof identity mismatch")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload[key] is not None:
            raise SchedulerContractError(f"formal static evaluator proof overclaims {key}")
    expected_echo = _formal_static_expected_input_echo(plan)
    exact_keys(payload["input_echo"], FORMAL_STATIC_INPUT_ECHO_KEYS, "formal static input echo")
    if not exact_json_equal(payload["input_echo"], expected_echo):
        raise SchedulerContractError("formal static evaluator proof input echo mismatch")
    expected_epsilon = _formal_static_interval_record(
        Fraction(expected_echo["epsilon_lower"]),
        Fraction(expected_echo["epsilon_upper"]),
    )
    if not exact_json_equal(payload["epsilon"], expected_epsilon) or not exact_json_equal(
        payload["period_window"],
        _formal_static_interval_record(Fraction(64, 100), Fraction(69, 100)),
    ):
        raise SchedulerContractError("formal static evaluator proof interval binding mismatch")
    if payload["proof_content_hash_definition"] != (
        "sha256(canonical_json(proof_without_proof_content_sha256))"
    ):
        raise SchedulerContractError("formal static evaluator proof hash definition mismatch")
    without_hash = dict(payload)
    stored_hash = without_hash.pop("proof_content_sha256")
    if (
        type(stored_hash) is not str
        or HEX_SHA256.fullmatch(stored_hash) is None
        or stored_hash != sha256_bytes(canonical_json_bytes(without_hash))
    ):
        raise SchedulerContractError("formal static evaluator proof content hash mismatch")
    if evaluator_status == "STATIC_CELL_CERTIFIED":
        if payload["proof_complete"] is not True:
            raise SchedulerContractError("formal static certified proof is incomplete")
        exact_keys(
            payload["source_bindings"],
            FORMAL_STATIC_SOURCE_BINDING_KEYS,
            "formal static proof source bindings",
        )
        if not exact_json_equal(
            payload["source_bindings"], plan.expected_source_bindings()
        ):
            raise SchedulerContractError("formal static proof source-binding mismatch")
        if (
            type(payload["outer_containment"]) is not dict
            or type(payload["trees"]) is not list
            or type(payload["counts"]) is not dict
        ):
            raise SchedulerContractError("formal static certified proof content containers mismatch")
    else:
        if payload["proof_complete"] is not False or payload["trees"] != []:
            raise SchedulerContractError("formal static nonpass proof completeness mismatch")
        if not exact_json_equal(
            payload["counts"],
            {
                "tree_count": 0,
                "node_count": 0,
                "internal_count": 0,
                "terminal_count": 0,
                "unresolved_count": 1,
                "maximum_depth": None,
            },
        ):
            raise SchedulerContractError("formal static nonpass proof counts mismatch")
        _validate_formal_static_nonpass_failure(payload["failure"], evaluator_status)


def _formal_static_file_binding(
    path: str, raw: bytes, serializer: str, truncated: bool
) -> dict[str, Any]:
    safe_relative_path(path)
    if serializer not in {"CJ_COMPACT_V1", "RAW_BYTES"} or type(truncated) is not bool:
        raise SchedulerContractError("formal static file binding domain mismatch")
    return {
        "path": path,
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "serializer": serializer,
        "truncated": truncated,
    }


def build_formal_static_absent_sentinel(
    plan: FormalStaticTransactionPlan,
    scheduler_classification: str,
    reason_code: str,
) -> dict[str, Any]:
    """Build the only canonical substitute for a truly absent proof stream."""

    plan.validate()
    expected_reason = FORMAL_STATIC_SENTINEL_REASONS.get(scheduler_classification)
    if expected_reason is None or reason_code != expected_reason:
        raise SchedulerContractError("formal static absent-proof reason mapping mismatch")
    sentinel = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "STATIC_PROOF_ABSENT",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": plan.matrix_id,
        "freeze_sha256": plan.freeze_sha256,
        "main_freeze_sha256": plan.main_freeze_sha256,
        "run_config_sha256": plan.run_config_sha256,
        "cell": plan.cell.payload(),
        "scheduler_classification": scheduler_classification,
        "evaluator_status": None,
        "reason_code": reason_code,
        "claim_boundary": FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(sentinel, STATIC_PROOF_SENTINEL_KEYS, "formal static absent sentinel")
    return sentinel


def build_formal_static_archive_candidates(
    plan: FormalStaticTransactionPlan,
    *,
    scheduler_classification: str,
    proof_raw: bytes | None,
    stdout_raw: bytes,
    stderr_raw: bytes,
    return_code: int | None,
    evaluator_status: str | None,
    truncated: Mapping[str, bool] | None = None,
) -> tuple[dict[str, bytes], dict[str, Any]]:
    """Package one exact four-file formal static transaction without executing.

    The function is deliberately pure and does not publish an archive.  It is
    usable by deterministic tests and by a future already-authorized bounded
    process wrapper.  It never synthesizes a scientific proof.
    """

    plan.validate()
    if scheduler_classification not in FORMAL_STATIC_CLASSIFICATIONS:
        raise SchedulerContractError("formal static scheduler classification is closed")
    if proof_raw is not None and type(proof_raw) is not bytes:
        raise SchedulerContractError("formal static proof stream must be exact bytes")
    if type(stdout_raw) is not bytes or type(stderr_raw) is not bytes:
        raise SchedulerContractError("formal static raw streams must be bytes")
    if return_code is not None and type(return_code) is not int:
        raise SchedulerContractError("formal static return code type mismatch")
    if evaluator_status is not None and type(evaluator_status) is not str:
        raise SchedulerContractError("formal static evaluator status type mismatch")
    truncation = {name: False for name in ("proof.json", "stdout.txt", "stderr.txt")}
    if truncated is not None:
        exact_keys(truncated, set(truncation), "formal static truncation map")
        if not all(type(value) is bool for value in truncated.values()):
            raise SchedulerContractError("formal static truncation values must be Boolean")
        truncation.update(truncated)
    if (
        scheduler_classification == "CELL_OUTPUT_BUDGET_EXHAUSTED"
        and not any(truncation.values())
    ):
        raise SchedulerContractError(
            "output-budget classification lacks truncation evidence"
        )

    proof_kind: str
    reason_code: str | None
    evaluator_result: dict[str, Any]
    if scheduler_classification == "COMMITTED_EVALUATOR_RESULT":
        if evaluator_status not in FORMAL_STATIC_STATUS_CODES:
            raise SchedulerContractError("committed formal static status is not in the frozen table")
        expected_code = FORMAL_STATIC_STATUS_CODES[evaluator_status]
        if return_code != expected_code:
            raise SchedulerContractError("committed formal static status/code mismatch")
        if proof_raw is None:
            raise SchedulerContractError("committed formal static cell lacks proof bytes")
        try:
            proof_payload = strict_json_loads(proof_raw.decode("utf-8"))
        except (UnicodeError, StrictJSONError) as error:
            raise SchedulerContractError("committed formal static proof is malformed") from error
        if type(proof_payload) is not dict or proof_raw != canonical_json_bytes(proof_payload):
            raise SchedulerContractError("committed formal static proof is not CJ_COMPACT_V1")
        _validate_formal_static_evaluator_proof(
            plan, proof_payload, evaluator_status
        )
        if stdout_raw != f"evaluator_status={evaluator_status}\n".encode("ascii") or stderr_raw != b"":
            raise SchedulerContractError("committed formal static stream ABI mismatch")
        if any(truncation.values()):
            raise SchedulerContractError("committed formal static files cannot be truncated")
        proof_kind = "EVALUATOR_PROOF"
        reason_code = None
        evaluator_result = {
            "status": evaluator_status,
            "return_code": expected_code,
            "status_line_count": 1,
        }
    else:
        if evaluator_status is not None:
            raise SchedulerContractError("noncommitted formal static status must be null")
        evaluator_result = {"status": None, "return_code": None, "status_line_count": 0}
        if proof_raw is None:
            reason_code = FORMAL_STATIC_SENTINEL_REASONS.get(scheduler_classification)
            if reason_code is None:
                raise SchedulerContractError("classification cannot represent an absent proof")
            if return_code is not None:
                raise SchedulerContractError("absent-proof sentinel return code must be null")
            proof_payload = build_formal_static_absent_sentinel(
                plan, scheduler_classification, reason_code
            )
            proof_raw = canonical_json_bytes(proof_payload)
            proof_kind = "SCHEDULER_NO_PROOF_SENTINEL"
            truncation["proof.json"] = False
        else:
            if type(proof_raw) is not bytes or len(proof_raw) == 0:
                raise SchedulerContractError("formal static invalid proof image is empty")
            try:
                payload = strict_json_loads(proof_raw.decode("utf-8"))
                canonical = type(payload) is dict and proof_raw == canonical_json_bytes(payload)
            except (UnicodeError, StrictJSONError):
                canonical = False
            if canonical:
                if scheduler_classification != "MALFORMED_EVALUATOR_OUTPUT":
                    raise SchedulerContractError("canonical noncommitted proof classification mismatch")
                proof_kind = "EVALUATOR_PROOF"
                reason_code = "STATUS_OR_RETURN_CODE_MISMATCH"
            else:
                if scheduler_classification == "MALFORMED_EVALUATOR_OUTPUT":
                    reason_code = "MALFORMED_OR_NONCANONICAL_PROOF"
                elif scheduler_classification == "CELL_OUTPUT_BUDGET_EXHAUSTED":
                    reason_code = "OUTPUT_BUDGET"
                else:
                    raise SchedulerContractError("invalid proof classification mismatch")
                proof_kind = "INVALID_EVALUATOR_PROOF"

    assert proof_raw is not None
    proof_serializer = "RAW_BYTES" if proof_kind == "INVALID_EVALUATOR_PROOF" else "CJ_COMPACT_V1"
    raw_files = {
        "proof.json": proof_raw,
        "stdout.txt": stdout_raw,
        "stderr.txt": stderr_raw,
    }
    bindings = {
        name: _formal_static_file_binding(
            name,
            raw,
            proof_serializer if name == "proof.json" else "RAW_BYTES",
            truncation[name],
        )
        for name, raw in raw_files.items()
    }
    semantic_argv = list(plan.semantic_argv)
    task = {
        "epsilon_lower": _semantic_flag(plan, "--epsilon-lower"),
        "epsilon_upper": _semantic_flag(plan, "--epsilon-upper"),
        "plan_record_sha256": _semantic_flag(plan, "--plan-record-sha256"),
    }
    record = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "STATIC_CELL_RECORD",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": plan.matrix_id,
        "freeze_sha256": plan.freeze_sha256,
        "main_freeze_sha256": plan.main_freeze_sha256,
        "run_config_sha256": plan.run_config_sha256,
        "cell": plan.cell.payload(),
        "task": task,
        "semantic_invocation": {
            "argv": semantic_argv,
            "argv_sha256": plan.semantic_argv_sha256,
            "exact_string_count": 26,
            "output_token": "<STAGING_PROOF_PATH>",
        },
        "scheduler_result": {
            "classification": scheduler_classification,
            "evaluator_status": evaluator_status,
            "return_code": return_code,
            "proof_kind": proof_kind,
            "reason_code": reason_code,
        },
        "evaluator_result": evaluator_result,
        "files": bindings,
        "limits": formal_limits()["static"],
        "claim_boundary": FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(record, FORMAL_STATIC_RECORD_KEYS, "formal static record candidate")
    record_raw = canonical_json_bytes(record)
    raw_files["record.json"] = record_raw
    record_binding = _formal_static_file_binding(
        "record.json", record_raw, "CJ_COMPACT_V1", False
    )
    manifest_files = {**bindings, "record.json": record_binding}
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "STATIC_CELL_MANIFEST",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": plan.matrix_id,
        "freeze_sha256": plan.freeze_sha256,
        "main_freeze_sha256": plan.main_freeze_sha256,
        "run_config_sha256": plan.run_config_sha256,
        "cell": plan.cell.payload(),
        "semantic_invocation_sha256": plan.semantic_argv_sha256,
        "scheduler_classification": scheduler_classification,
        "evaluator_status": evaluator_status if scheduler_classification == "COMMITTED_EVALUATOR_RESULT" else None,
        "record": record_binding,
        "files": manifest_files,
        "claim_boundary": FORMAL_STATIC_CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(manifest, FORMAL_STATIC_MANIFEST_KEYS, "formal static manifest candidate")
    if sum(len(raw) for raw in raw_files.values()) > formal_limits()["static"]["total_cell_bytes"]:
        raise SchedulerContractError("formal static archive exceeds total-cell byte cap")
    return raw_files, manifest


def dispatch_formal_static_transaction(
    plan: FormalStaticTransactionPlan, *, executor: Any = None
) -> None:
    plan.validate()
    raise ProductionAuthorityError(
        "formal static execution is unconditionally disabled; executor was not called"
    )


def dispatch_formal_branch_transaction(
    plan: FormalBranchTransactionPlan, *, transaction_runner: Any = None
) -> None:
    plan.validate()
    raise ProductionAuthorityError(
        "formal branch execution is unconditionally disabled; transaction runner was not called"
    )


def build_formal_component_aggregate_candidates(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    run_config_sha256: str,
    entries: Sequence[Mapping[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Build exact, non-published component aggregate objects.

    This pure function has no publication side effect.  Objects exist only
    for an exact 102-entry certified frontier; a nonpass/resource/invalid
    frontier has no component aggregate.
    """

    if component not in COMPONENTS:
        raise SchedulerContractError("formal aggregate component is invalid")
    revalidate_formal_snapshot(
        snapshot,
        ("static_evaluator",)
        if component == "STATIC"
        else ("branch_evaluator_source", "branch_evaluator_binary"),
    )
    if type(entries) not in (list, tuple) or len(entries) != 102:
        raise CorruptGeneration("formal aggregate requires exactly 102 entries")
    prefix = component.upper()
    certified = f"{prefix}_CELL_CERTIFIED"
    normalized: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for cell, entry in zip(exact_matrix(), entries):
        exact_keys(
            entry,
            {
                "cell", "path", "sha256", "size_bytes",
                "evaluator_status", "scheduler_classification",
            },
            "formal manifest entry",
        )
        if not exact_json_equal(entry["cell"], cell.payload()):
            raise CorruptGeneration("formal aggregate cell order mismatch")
        safe_relative_path(entry["path"])
        expected_path = (
            f"{component.lower()}/cell_manifests/"
            f"{cell.precision_bits}/{cell.slab_id}.json"
        )
        if entry["path"] != expected_path or entry["path"] in seen_paths:
            raise CorruptGeneration("formal aggregate entry path/order mismatch")
        seen_paths.add(entry["path"])
        if type(entry["sha256"]) is not str or HEX_SHA256.fullmatch(entry["sha256"]) is None:
            raise CorruptGeneration("formal aggregate entry hash is malformed")
        exact_int(entry["size_bytes"], "formal aggregate entry size", minimum=1)
        if (
            entry["evaluator_status"] != certified
            or entry["scheduler_classification"] != "COMMITTED_EVALUATOR_RESULT"
        ):
            raise CorruptGeneration("formal aggregate entry is not producer-certified")
        normalized.append(dict(entry))
    if type(run_config_sha256) is not str or HEX_SHA256.fullmatch(run_config_sha256) is None:
        raise CorruptGeneration("formal aggregate run-config hash is malformed")
    evaluator_roles = (
        {"static_evaluator": _formal_role(snapshot, "static_evaluator").payload()}
        if component == "STATIC"
        else {
            "branch_evaluator_source": _formal_role(snapshot, "branch_evaluator_source").payload(),
            "branch_evaluator_binary": _formal_role(snapshot, "branch_evaluator_binary").payload(),
        }
    )
    root_hash = sha256_bytes(canonical_json_bytes(normalized))
    common = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_status": "COMPLETE_PRODUCER_ARCHIVE",
        "authority": "PRODUCER_ONLY",
        "matrix_id": canonical_matrix_id(),
        "freeze_sha256": snapshot.main_freeze_sha256,
        "main_freeze_sha256": snapshot.main_freeze_sha256,
        "run_config_sha256": run_config_sha256,
        "ordered_cell_manifest_root": root_hash,
        "evaluator_roles": evaluator_roles,
        "scientific_licensing_enabled": False,
        "claim_boundary": FORMAL_AGGREGATE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    summary = {
        **common,
        "artifact_role": f"{prefix}_AGGREGATE_SUMMARY",
        "matrix": matrix_payload(),
        "cell_count": 102,
        "status_counts": {certified: 102},
        "scheduler_classification_counts": {"COMMITTED_EVALUATOR_RESULT": 102},
    }
    relative_summary = (
        "static/aggregate_summary.json"
        if component == "STATIC"
        else "branch/aggregate_summary.json"
    )
    summary_raw = canonical_json_bytes(summary)
    manifest = {
        **common,
        "artifact_role": f"{prefix}_AGGREGATE_MANIFEST",
        "cell_manifests": normalized,
        "summary": {
            "path": relative_summary,
            "sha256": sha256_bytes(summary_raw),
            "size_bytes": len(summary_raw),
        },
    }
    if summary["freeze_sha256"] != summary["main_freeze_sha256"] or manifest[
        "freeze_sha256"
    ] != manifest["main_freeze_sha256"]:
        raise ProductionAuthorityError("formal aggregate freeze hash mismatch")
    exact_keys(summary, FORMAL_AGGREGATE_SUMMARY_KEYS, "formal aggregate summary")
    exact_keys(manifest, FORMAL_AGGREGATE_MANIFEST_KEYS, "formal aggregate manifest")
    return summary, manifest


def branch_cell_path(output: Path, cell: CellKey) -> Path:
    return output / "branch" / "cells" / str(cell.precision_bits) / cell.slab_id


def branch_manifest_path(output: Path, cell: CellKey) -> Path:
    return (
        output
        / "branch"
        / "cell_manifests"
        / str(cell.precision_bits)
        / f"{cell.slab_id}.json"
    )


def branch_aggregate_summary_path(output: Path) -> Path:
    return output / "branch" / "aggregate_summary.json"


def branch_aggregate_manifest_path(output: Path) -> Path:
    return output / "branch" / "aggregate_manifest.json"


def validate_branch_cell_namespace(output: Path) -> None:
    root = output / "branch" / "cells"
    require_directory(root)
    if {path.name for path in root.iterdir()} != {"128", "256"}:
        raise CorruptGeneration("branch cell precision namespace mismatch")
    for bits in PRECISIONS:
        precision_root = root / str(bits)
        require_directory(precision_root)
        if {path.name for path in precision_root.iterdir()} != set(SLAB_IDS):
            raise CorruptGeneration(f"branch cell namespace mismatch for {bits}")
        for slab_id in SLAB_IDS:
            cell = precision_root / slab_id
            require_directory(cell)
            if {path.name for path in cell.iterdir()} != {
                "stdout.txt",
                "stderr.txt",
                "record.json",
            }:
                raise CorruptGeneration(
                    f"branch cell file namespace mismatch for {bits}:{slab_id}"
                )
            for path in cell.iterdir():
                require_regular_file(path)


def validate_branch_manifest_namespace(output: Path) -> None:
    root = output / "branch" / "cell_manifests"
    require_directory(root)
    if {path.name for path in root.iterdir()} != {"128", "256"}:
        raise CorruptGeneration("branch manifest precision namespace mismatch")
    for bits in PRECISIONS:
        precision_root = root / str(bits)
        require_directory(precision_root)
        expected = {f"{slab}.json" for slab in SLAB_IDS}
        if {path.name for path in precision_root.iterdir()} != expected:
            raise CorruptGeneration(
                f"branch manifest namespace mismatch for {bits}"
            )
        for path in precision_root.iterdir():
            require_regular_file(path)


def validate_mock_branch_namespace(output: Path) -> None:
    branch = output / "branch"
    require_directory(branch)
    aggregate_names = {
        path.name
        for path in (
            branch_aggregate_summary_path(output),
            branch_aggregate_manifest_path(output),
        )
        if path.exists()
    }
    if aggregate_names == {"aggregate_manifest.json"}:
        raise CorruptGeneration("branch aggregate manifest exists without summary")
    permitted_aggregates = (
        set(),
        {"aggregate_summary.json"},
        {"aggregate_summary.json", "aggregate_manifest.json"},
    )
    if aggregate_names not in permitted_aggregates:
        raise CorruptGeneration("invalid branch aggregate namespace state")
    expected = {"cells", "cell_manifests"} | aggregate_names
    actual = {path.name for path in branch.iterdir()}
    if actual != expected:
        raise CorruptGeneration(f"branch authoritative namespace mismatch: {actual}")
    validate_branch_cell_namespace(output)
    validate_branch_manifest_namespace(output)


def validate_branch_operational_quiescent(
    operational: Path, run_config_sha256: str
) -> None:
    active = _branch_runtime()._scan_exact_staging_namespace(
        operational, run_config_sha256[:16]
    )
    if active:
        labels = sorted(f"{bits}:{slab}" for bits, slab in active)
        raise CorruptGeneration(
            "branch aggregate cannot coexist with live staging owners: "
            + ",".join(labels)
        )
    _branch_runtime()._reject_withdrawn_interrupted_staging_namespace(operational)
    locks = operational / "locks" / "branch"
    if path_lexists(locks):
        require_directory(locks)
        unexpected = {path.name for path in locks.iterdir()} - {"128", "256"}
        if unexpected:
            raise CorruptGeneration(f"unexpected branch lock namespace: {unexpected}")
        for precision_root in locks.iterdir():
            require_directory(precision_root)
            if any(precision_root.iterdir()):
                raise CorruptGeneration("live branch lock blocks aggregate publication")
    _branch_runtime()._scan_interrupted_lock_namespaces(
        operational, run_config_sha256[:16]
    )


def ordered_branch_manifest_entries(
    output: Path,
    tasks: Sequence[Any],
    bindings: Any,
    budgets: Any,
) -> list[dict[str, Any]]:
    if len(tasks) != 102:
        raise CorruptGeneration("branch aggregate task matrix is not 102 cells")
    validate_branch_operational_quiescent(
        operational_root_for(output), bindings.run_config_sha256
    )
    validate_mock_branch_namespace(output)
    entries: list[dict[str, Any]] = []
    for cell, task in zip(exact_matrix(), tasks):
        record, _manifest = _branch_runtime().validate_committed_branch_cell(
            output, task, bindings, budgets
        )
        scheduler = record["scheduler_result"]
        if (
            scheduler["classification"] != "COMMITTED_EVALUATOR_RESULT"
            or scheduler["evaluator_status"] != "BRANCH_CELL_CERTIFIED"
        ):
            raise CorruptGeneration(
                f"mock branch cell is not certified: {cell.label}"
            )
        path = branch_manifest_path(output, cell)
        raw, info = read_pinned_regular_file(path)
        entries.append(
            {
                "cell": cell.payload(),
                "path": path.relative_to(output).as_posix(),
                "sha256": sha256_bytes(raw),
                "size_bytes": info.st_size,
            }
        )
    return entries


def build_branch_aggregate_summary(
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
    mock_evaluator: Mapping[str, Any],
) -> dict[str, Any]:
    if len(entries) != 102:
        raise CorruptGeneration("branch aggregate requires exactly 102 manifests")
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_BRANCH_AGGREGATE_SUMMARY",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "matrix": matrix_payload(),
        "cell_count": 102,
        "ordered_cell_manifest_root": sha256_bytes(canonical_json_bytes(entries)),
        "status_counts": {"BRANCH_CELL_CERTIFIED": 102},
        "scheduler_classification_counts": {
            "COMMITTED_EVALUATOR_RESULT": 102
        },
        "mock_evaluator": dict(mock_evaluator),
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def build_branch_aggregate_manifest(
    output: Path,
    matrix_id: str,
    run_config_sha256: str,
    entries: list[dict[str, Any]],
    summary: Mapping[str, Any],
    mock_evaluator: Mapping[str, Any],
) -> dict[str, Any]:
    summary_bytes = canonical_json_bytes(summary)
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_BRANCH_AGGREGATE_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": matrix_id,
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "ordered_cell_manifest_root": sha256_bytes(canonical_json_bytes(entries)),
        "cell_manifests": entries,
        "summary": {
            "path": branch_aggregate_summary_path(output).relative_to(output).as_posix(),
            "sha256": sha256_bytes(summary_bytes),
            "size_bytes": len(summary_bytes),
        },
        "mock_evaluator": dict(mock_evaluator),
        "scientific_licensing_enabled": False,
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_branch_mock_aggregate(
    output: Path,
    tasks: Sequence[Any],
    bindings: Any,
    budgets: Any,
    mock_evaluator: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    summary_path = branch_aggregate_summary_path(output)
    manifest_path = branch_aggregate_manifest_path(output)
    if not summary_path.exists() or not manifest_path.exists():
        raise CorruptGeneration("branch aggregate summary/manifest pair is incomplete")
    entries = ordered_branch_manifest_entries(output, tasks, bindings, budgets)
    expected_summary = build_branch_aggregate_summary(
        bindings.matrix_id,
        bindings.run_config_sha256,
        entries,
        mock_evaluator,
    )
    stored_summary = strict_json_load(summary_path, require_canonical=True)
    if not exact_json_equal(stored_summary, expected_summary):
        raise CorruptGeneration("branch aggregate summary mismatch")
    expected_manifest = build_branch_aggregate_manifest(
        output,
        bindings.matrix_id,
        bindings.run_config_sha256,
        entries,
        expected_summary,
        mock_evaluator,
    )
    stored_manifest = strict_json_load(manifest_path, require_canonical=True)
    if not exact_json_equal(stored_manifest, expected_manifest):
        raise CorruptGeneration("branch aggregate manifest mismatch")
    return dict(stored_summary), dict(stored_manifest)


def finalize_branch_mock_aggregate(
    output: Path,
    tasks: Sequence[Any],
    bindings: Any,
    budgets: Any,
    mock_evaluator: Mapping[str, Any],
) -> tuple[str, dict[str, Any], dict[str, Any]]:
    """Publish a deterministic branch aggregate with manifest last."""

    summary_path = branch_aggregate_summary_path(output)
    manifest_path = branch_aggregate_manifest_path(output)
    if manifest_path.exists():
        summary, manifest = validate_branch_mock_aggregate(
            output, tasks, bindings, budgets, mock_evaluator
        )
        return "RESUMED_COMMITTED", summary, manifest
    entries = ordered_branch_manifest_entries(output, tasks, bindings, budgets)
    summary = build_branch_aggregate_summary(
        bindings.matrix_id,
        bindings.run_config_sha256,
        entries,
        mock_evaluator,
    )
    manifest = build_branch_aggregate_manifest(
        output,
        bindings.matrix_id,
        bindings.run_config_sha256,
        entries,
        summary,
        mock_evaluator,
    )
    if summary_path.exists():
        stored = strict_json_load(summary_path, require_canonical=True)
        if not exact_json_equal(stored, summary):
            raise CorruptGeneration("manifest-less branch aggregate summary mismatch")
        state = "RECOVERED_MANIFEST"
    else:
        exclusive_write_json(summary_path, summary)
        state = "COMMITTED"
    exclusive_write_json(manifest_path, manifest)
    checked_summary, checked_manifest = validate_branch_mock_aggregate(
        output, tasks, bindings, budgets, mock_evaluator
    )
    return state, checked_summary, checked_manifest


def quarantine_paths(output: Path, index: int) -> tuple[Path, Path]:
    operational = operational_root_for(output)
    return (
        output.with_name(f"{output.name}.quarantine-{index:04d}"),
        operational.with_name(f"{operational.name}.quarantine-{index:04d}"),
    )


def quarantine_journal_path(output: Path) -> Path:
    return output.with_name(f"{output.name}.quarantine-transaction.json")


QUARANTINE_FAILURE_POINTS = {
    "AFTER_JOURNAL",
    "AFTER_AUTHORITATIVE_RENAME",
    "AFTER_OPERATIONAL_RENAME",
    "AFTER_RECORD",
}


QUARANTINE_INTENT_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "artifact_status",
    "authority",
    "mock_only",
    "transaction_index",
    "reason",
    "source_authoritative_root",
    "source_operational_root",
    "destination_authoritative_root",
    "destination_operational_root",
    "operational_present",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def path_lexists(path: Path) -> bool:
    return os.path.lexists(path)


def build_quarantine_intent(
    output: Path,
    reason: str,
    index: int,
    operational_present: bool,
) -> dict[str, Any]:
    output = output.absolute()
    operational = operational_root_for(output)
    q_output, q_operational = quarantine_paths(output, index)
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "QUARANTINE_TRANSACTION_INTENT",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "transaction_index": index,
        "reason": reason,
        "source_authoritative_root": str(output),
        "source_operational_root": str(operational),
        "destination_authoritative_root": str(q_output),
        "destination_operational_root": str(q_operational),
        "operational_present": operational_present,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def validate_quarantine_intent(output: Path, payload: Any) -> dict[str, Any]:
    exact_keys(payload, QUARANTINE_INTENT_KEYS, "quarantine transaction intent")
    if payload["schema_version"] != SCHEMA_VERSION or type(payload["schema_version"]) is not int:
        raise CorruptGeneration("quarantine intent schema mismatch")
    expected_scalars = {
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "QUARANTINE_TRANSACTION_INTENT",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    for key, expected in expected_scalars.items():
        if type(payload[key]) is not type(expected) or payload[key] != expected:
            raise CorruptGeneration(f"quarantine intent {key} mismatch")
    index = exact_int(
        payload["transaction_index"], "quarantine transaction index", minimum=1
    )
    if index >= 10_000:
        raise CorruptGeneration("quarantine transaction index exceeds namespace")
    if type(payload["reason"]) is not str or not payload["reason"]:
        raise CorruptGeneration("quarantine intent reason is invalid")
    if type(payload["operational_present"]) is not bool:
        raise CorruptGeneration("quarantine operational_present must be Boolean")

    output = output.absolute()
    operational = operational_root_for(output)
    q_output, q_operational = quarantine_paths(output, index)
    expected_paths = {
        "source_authoritative_root": output,
        "source_operational_root": operational,
        "destination_authoritative_root": q_output,
        "destination_operational_root": q_operational,
    }
    for key, expected in expected_paths.items():
        actual = safe_absolute_path(payload[key], key.replace("_", " "))
        if actual != expected:
            raise CorruptGeneration(f"quarantine intent {key} is not canonical")
    return dict(payload)


def quarantine_record_payload(
    intent: Mapping[str, Any], journal_sha256: str
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "QUARANTINE_RECORD",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "transaction_index": intent["transaction_index"],
        "transaction_journal_sha256": journal_sha256,
        "reason": intent["reason"],
        "source_authoritative_root": intent["source_authoritative_root"],
        "source_operational_root": intent["source_operational_root"],
        "destination_authoritative_root": intent["destination_authoritative_root"],
        "destination_operational_root": intent["destination_operational_root"],
        "operational_present": intent["operational_present"],
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def _quarantine_move_or_validate(source: Path, destination: Path, label: str) -> bool:
    source_exists = path_lexists(source)
    destination_exists = path_lexists(destination)
    if source_exists and destination_exists:
        raise CorruptGeneration(f"split quarantine has both {label} source and destination")
    if not source_exists and not destination_exists:
        raise CorruptGeneration(f"quarantine lost both {label} source and destination")
    if destination_exists:
        require_directory(destination)
        return False
    require_directory(source)
    rename_directory_noreplace(source, destination)
    fsync_directory(source.parent)
    if destination.parent != source.parent:
        fsync_directory(destination.parent)
    return True


def _complete_quarantine_transaction(
    output: Path,
    *,
    fail_at: str | None = None,
) -> tuple[Path, Path | None]:
    output = output.absolute()
    journal = quarantine_journal_path(output)
    intent = validate_quarantine_intent(
        output, strict_json_load(journal, require_canonical=True)
    )
    journal_digest = sha256(journal)
    source_output = Path(intent["source_authoritative_root"])
    source_operational = Path(intent["source_operational_root"])
    q_output = Path(intent["destination_authoritative_root"])
    q_operational = Path(intent["destination_operational_root"])

    moved_output = _quarantine_move_or_validate(
        source_output, q_output, "authoritative"
    )
    if moved_output and fail_at == "AFTER_AUTHORITATIVE_RENAME":
        raise SyntheticQuarantineCrash("crash after authoritative quarantine rename")

    moved_operational: Path | None = None
    if intent["operational_present"]:
        _quarantine_move_or_validate(
            source_operational, q_operational, "operational"
        )
        moved_operational = q_operational
    elif path_lexists(source_operational) or path_lexists(q_operational):
        raise CorruptGeneration(
            "operational quarantine path exists contrary to frozen transaction intent"
        )
    if fail_at == "AFTER_OPERATIONAL_RENAME":
        raise SyntheticQuarantineCrash("crash after operational quarantine rename")

    record_path = q_output / "QUARANTINE_RECORD.json"
    expected_record = quarantine_record_payload(intent, journal_digest)
    if path_lexists(record_path):
        stored_record = strict_json_load(record_path, require_canonical=True)
        if not exact_json_equal(stored_record, expected_record):
            raise CorruptGeneration("quarantine record mismatch")
    else:
        exclusive_write_json(record_path, expected_record)
    if fail_at == "AFTER_RECORD":
        raise SyntheticQuarantineCrash("crash after quarantine record commit")

    journal.unlink()
    fsync_directory(journal.parent)
    return q_output, moved_operational


def recover_quarantine_transaction(output: Path) -> tuple[Path, Path | None] | None:
    output = output.absolute()
    journal = quarantine_journal_path(output)
    if not path_lexists(journal):
        return None
    return _complete_quarantine_transaction(output)


def quarantine_incompatible_generation(
    output: Path,
    reason: str,
    *,
    fail_at: str | None = None,
) -> tuple[Path, Path | None]:
    output = output.absolute()
    journal = quarantine_journal_path(output)
    if fail_at is not None and fail_at not in QUARANTINE_FAILURE_POINTS:
        raise SchedulerContractError(f"unknown quarantine failure point: {fail_at}")
    if path_lexists(journal):
        intent = validate_quarantine_intent(
            output, strict_json_load(journal, require_canonical=True)
        )
        if intent["reason"] != reason:
            raise CorruptGeneration("active quarantine intent has a different reason")
        return _complete_quarantine_transaction(output, fail_at=fail_at)
    if not path_lexists(output):
        raise PathContractError("authoritative generation does not exist")
    if type(reason) is not str or not reason:
        raise SchedulerContractError("quarantine reason must be nonempty")
    operational = operational_root_for(output)
    require_directory(output)
    operational_present = path_lexists(operational)
    if operational_present:
        require_directory(operational)
        ensure_same_filesystem(output, operational)
    ensure_same_filesystem(output, journal)
    for index in range(1, 10_000):
        q_output, q_operational = quarantine_paths(output, index)
        if not path_lexists(q_output) and not path_lexists(q_operational):
            break
    else:
        raise SchedulerContractError("quarantine namespace exhausted")
    intent = build_quarantine_intent(output, reason, index, operational_present)
    exclusive_write_json(journal, intent)
    if fail_at == "AFTER_JOURNAL":
        raise SyntheticQuarantineCrash("crash after quarantine intent commit")
    return _complete_quarantine_transaction(output, fail_at=fail_at)


def run_mock_static(output: Path, cell_limit: int, *, resume: bool) -> dict[str, Any]:
    ensure_mock_output_allowed(output)
    operational = operational_root_for(output)
    ensure_mock_output_allowed(operational)
    recovered_quarantine = recover_quarantine_transaction(output)
    if recovered_quarantine is not None:
        raise RunBindingMismatch(
            "pending quarantine transaction was completed; the quarantined "
            "generation cannot be resumed"
        )
    exact_int(cell_limit, "mock cell limit", minimum=0)
    if cell_limit > 102:
        raise SchedulerContractError("mock cell limit cannot exceed 102")
    binding = build_mock_binding(output, operational)
    _, config_hash = ensure_run_config(output, binding, resume=resume)
    operational.mkdir(parents=True, exist_ok=True)
    ensure_same_filesystem(output, operational)
    states: list[dict[str, Any]] = []
    for cell in exact_matrix()[:cell_limit]:
        state, manifest = commit_mock_static_cell(
            output,
            operational,
            cell,
            binding["matrix_id"],
            config_hash,
        )
        states.append({"cell": cell.payload(), "state": state, "manifest": manifest})
    aggregate: dict[str, Any] | None = None
    if cell_limit == 102:
        aggregate_state, summary, manifest = finalize_static_mock_aggregate(
            output,
            binding["matrix_id"],
            config_hash,
        )
        aggregate = {
            "state": aggregate_state,
            "ordered_cell_manifest_root": summary["ordered_cell_manifest_root"],
            "summary_sha256": manifest["summary"]["sha256"],
            "manifest_sha256": sha256(static_aggregate_manifest_path(output)),
        }
    return {
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "mock_only": True,
        "production_authorized": False,
        "matrix_id": binding["matrix_id"],
        "requested_cells": cell_limit,
        "completed_cells": len(states),
        "states": states,
        "aggregate_finalized": aggregate is not None,
        "aggregate": aggregate,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


def scan_partial_branch_frontier(output: Path) -> tuple[set[CellKey], set[CellKey]]:
    """Validate a partial branch namespace and return cell/manifest identities."""

    branch = output / "branch"
    if not path_lexists(branch):
        return set(), set()
    require_directory(branch)
    allowed = {"cells", "cell_manifests"}
    aggregate_pair = {
        name
        for name in ("aggregate_summary.json", "aggregate_manifest.json")
        if (branch / name).exists()
    }
    if aggregate_pair not in (
        set(),
        {"aggregate_summary.json"},
        {"aggregate_summary.json", "aggregate_manifest.json"},
    ):
        raise CorruptGeneration("partial branch aggregate state is invalid")
    allowed |= aggregate_pair
    if {path.name for path in branch.iterdir()} != allowed:
        raise CorruptGeneration("partial branch namespace has an extra object")
    cells: set[CellKey] = set()
    manifests: set[CellKey] = set()
    cells_root = branch / "cells"
    manifests_root = branch / "cell_manifests"
    for root, role in ((cells_root, "cell"), (manifests_root, "manifest")):
        if not path_lexists(root):
            continue
        require_directory(root)
        for precision_root in root.iterdir():
            if precision_root.name not in {"128", "256"}:
                raise CorruptGeneration(f"partial branch {role} precision is invalid")
            require_directory(precision_root)
            bits = int(precision_root.name)
            for entry in precision_root.iterdir():
                if role == "cell":
                    slab_id = entry.name
                    if slab_id not in SLAB_IDS:
                        raise CorruptGeneration("partial branch cell ID is invalid")
                    require_directory(entry)
                    if {path.name for path in entry.iterdir()} != {
                        "stdout.txt",
                        "stderr.txt",
                        "record.json",
                    }:
                        raise CorruptGeneration("partial branch cell files are invalid")
                    for path in entry.iterdir():
                        require_regular_file(path)
                    cells.add(CellKey(bits, slab_id))
                else:
                    if not entry.name.endswith(".json"):
                        raise CorruptGeneration("partial branch manifest name is invalid")
                    slab_id = entry.name.removesuffix(".json")
                    if slab_id not in SLAB_IDS:
                        raise CorruptGeneration("partial branch manifest ID is invalid")
                    require_regular_file(entry)
                    manifests.add(CellKey(bits, slab_id))
    if not manifests <= cells:
        raise CorruptGeneration("branch manifest exists without its canonical cell")
    if aggregate_pair and (len(cells) != 102 or len(manifests) != 102):
        raise CorruptGeneration("partial branch aggregate exists before full matrix")
    return cells, manifests


def _validate_mock_delay_map(
    values: Mapping[str, float] | None,
) -> dict[str, float]:
    if values is None:
        return {}
    if type(values) is not dict:
        raise SchedulerContractError("mock completion delays must be a dictionary")
    labels = {cell.label for cell in exact_matrix()}
    result: dict[str, float] = {}
    for label, delay in values.items():
        if type(label) is not str or label not in labels:
            raise SchedulerContractError(f"unknown mock delay cell: {label}")
        if (
            type(delay) not in (int, float)
            or isinstance(delay, bool)
            or not math.isfinite(delay)
            or delay < 0
            or delay > 5
        ):
            raise SchedulerContractError("mock completion delay is out of range")
        result[label] = float(delay)
    return result


def _run_one_mock_branch_cell(
    *,
    output: Path,
    operational: Path,
    task: Any,
    bindings: Any,
    budgets: Any,
    delay_seconds: float,
) -> Any:
    if delay_seconds:
        time.sleep(delay_seconds)
    # Concurrent mock owners can observe another cooperative owner exactly
    # between its staging rename and lock release.  The hardened runtime
    # correctly fails closed.  For this engineering replay only, retry that
    # exact *pre-dispatch* race after proving the current task has published
    # no cell, manifest, stage, or lock.  Evaluator/resource outcomes are
    # never retried.
    transient_phrases = (
        "other-cell staging changed during admission",
        "cannot snapshot live owner for another branch staging cell",
        "branch staging object is not a directory",
    )
    runtime = _branch_runtime()
    for retry_index in range(65):
        try:
            return runtime.run_branch_cell_transaction(
                output_root=output,
                operational_root=operational,
                task=task,
                bindings=bindings,
                budgets=budgets,
                attempt=0,
            )
        except runtime.BranchProvenanceError as error:
            if not any(phrase in str(error) for phrase in transient_phrases):
                raise
            own_cell = (
                output
                / "branch"
                / "cells"
                / str(task.precision_bits)
                / task.slab_id
            )
            own_manifest = (
                output
                / "branch"
                / "cell_manifests"
                / str(task.precision_bits)
                / f"{task.slab_id}.json"
            )
            own_stage = (
                operational
                / "staging"
                / "branch"
                / str(task.precision_bits)
                / (
                    f".{task.slab_id}.tmp-"
                    f"{bindings.run_config_sha256[:16]}-0"
                )
            )
            own_lock = (
                operational
                / "locks"
                / "branch"
                / str(task.precision_bits)
                / f"{task.slab_id}.lock"
            )
            if any(
                path_lexists(path)
                for path in (own_cell, own_manifest, own_stage, own_lock)
            ):
                raise
            if retry_index == 64:
                raise
            time.sleep(0.005)
    raise AssertionError("unreachable mock branch admission retry")


def run_mock_branch(
    output: Path,
    evaluator: Path,
    cell_limit: int,
    *,
    resume: bool,
    completion_delays: Mapping[str, float] | None = None,
) -> dict[str, Any]:
    """Run up to 102 synthetic branch cells in deterministic six-cell barriers."""

    ensure_mock_output_allowed(output)
    operational = operational_root_for(output)
    ensure_mock_output_allowed(operational)
    recovered_quarantine = recover_quarantine_transaction(output)
    if recovered_quarantine is not None:
        raise RunBindingMismatch(
            "pending quarantine transaction was completed; the quarantined "
            "generation cannot be resumed"
        )
    exact_int(cell_limit, "mock branch cell limit", minimum=0)
    if cell_limit > 102:
        raise SchedulerContractError("mock branch cell limit cannot exceed 102")
    if not output.exists():
        raise RunBindingMismatch("branch stage requires an existing static generation")
    binding = build_mock_binding(output, operational)
    _, config_hash = ensure_run_config(output, binding, resume=True)
    ensure_same_filesystem(output, operational)

    static_summary, _static_manifest = validate_static_mock_aggregate(
        output, binding["matrix_id"], config_hash
    )
    if (
        static_summary["cell_count"] != 102
        or static_summary["status_counts"] != {"STATIC_CELL_CERTIFIED": 102}
        or static_summary["scheduler_classification_counts"]
        != {"COMMITTED_EVALUATOR_RESULT": 102}
    ):
        raise CorruptGeneration("branch admission requires the full static producer gate")

    existing_cells, existing_manifests = scan_partial_branch_frontier(output)
    if (existing_cells or existing_manifests) and not resume:
        raise RunBindingMismatch("branch archive already exists; explicit resume required")
    requested = set(exact_matrix()[:cell_limit])
    if not existing_cells <= requested:
        raise RunBindingMismatch("requested branch frontier is behind committed cells")
    if branch_aggregate_manifest_path(output).exists() and cell_limit != 102:
        raise RunBindingMismatch("committed branch aggregate requires the full frontier")

    mock_evaluator = validate_mock_branch_evaluator(output, evaluator)
    tasks = build_mock_branch_tasks(Path(mock_evaluator["path"]))
    bindings = mock_branch_bindings(
        binding["matrix_id"], config_hash, mock_evaluator
    )
    bindings.validate()
    budgets = _branch_runtime().BranchBudgets()
    budgets.validate()
    delays = _validate_mock_delay_map(completion_delays)

    states: list[dict[str, Any]] = []
    barrier_completion_order: list[list[str]] = []
    promotion_blocked = False
    selected_tasks = tasks[:cell_limit]
    for start in range(0, len(selected_tasks), 6):
        barrier = selected_tasks[start : start + 6]
        futures: dict[Future[Any], Any] = {}
        by_identity: dict[tuple[int, str], Any] = {}
        completion_labels: list[str] = []
        with ThreadPoolExecutor(
            max_workers=len(barrier),
            thread_name_prefix="a416-mock-branch",
        ) as pool:
            for task in barrier:
                label = f"{task.precision_bits}:{task.slab_id}"
                future = pool.submit(
                    _run_one_mock_branch_cell,
                    output=output,
                    operational=operational,
                    task=task,
                    bindings=bindings,
                    budgets=budgets,
                    delay_seconds=delays.get(label, 0.0),
                )
                futures[future] = task
            for future in as_completed(futures):
                task = futures[future]
                result = future.result()
                identity = (task.precision_bits, task.slab_id)
                if identity in by_identity:
                    raise CorruptGeneration("duplicate branch barrier completion")
                by_identity[identity] = result
                completion_labels.append(f"{task.precision_bits}:{task.slab_id}")
        barrier_completion_order.append(completion_labels)
        for task in barrier:
            identity = (task.precision_bits, task.slab_id)
            result = by_identity[identity]
            scheduler = result.record["scheduler_result"]
            passing = (
                scheduler["classification"] == "COMMITTED_EVALUATOR_RESULT"
                and scheduler["evaluator_status"] == "BRANCH_CELL_CERTIFIED"
            )
            states.append(
                {
                    "cell": {
                        "precision_bits": task.precision_bits,
                        "slab_id": task.slab_id,
                    },
                    "state": (
                        "RESUMED_COMMITTED"
                        if result.resumed_without_dispatch
                        else "COMMITTED"
                    ),
                    "scheduler_classification": scheduler["classification"],
                    "evaluator_status": scheduler["evaluator_status"],
                }
            )
            if not passing:
                promotion_blocked = True
        if promotion_blocked:
            break

    aggregate: dict[str, Any] | None = None
    if cell_limit == 102 and len(states) == 102 and not promotion_blocked:
        aggregate_state, summary, manifest = finalize_branch_mock_aggregate(
            output, tasks, bindings, budgets, mock_evaluator
        )
        aggregate = {
            "state": aggregate_state,
            "ordered_cell_manifest_root": summary["ordered_cell_manifest_root"],
            "summary_sha256": manifest["summary"]["sha256"],
            "manifest_sha256": sha256(branch_aggregate_manifest_path(output)),
        }
    return {
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "mock_only": True,
        "production_authorized": False,
        "matrix_id": binding["matrix_id"],
        "requested_cells": cell_limit,
        "completed_cells": len(states),
        "worker_limit": 6,
        "barrier_count": len(barrier_completion_order),
        "barrier_completion_order": barrier_completion_order,
        "states": states,
        "promotion_blocked": promotion_blocked,
        "aggregate_finalized": aggregate is not None,
        "aggregate": aggregate,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }


COMPONENT_CHECKER_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "authority",
    "checker_status",
    "component_status",
    "scientific_licensing_enabled",
    "passed",
    "matrix_id",
    "main_freeze_sha256",
    "run_config_sha256",
    "component_aggregate_summary_sha256",
    "component_aggregate_manifest_sha256",
    "replay_counts",
    "cross_precision",
    "diagnostics",
    "failures",
    "source_bindings",
    "claim_boundary",
    "milestone_status",
    "theorem_status",
    "final_status",
}

COMPONENT_POSTCHECK_KEYS = {
    "schema_version",
    "protocol_id",
    "artifact_role",
    "authority",
    "postcheck_status",
    "passed",
    "checker_path",
    "checker_sha256",
    "main_freeze_sha256",
    "run_config_sha256",
    "bound_artifacts",
    "replay_counts",
    "failures",
    "claim_boundary",
    "component_status",
    "milestone_status",
    "theorem_status",
    "final_status",
}


def _require_null_authority_statuses(payload: Mapping[str, Any], context: str) -> None:
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        if payload.get(key) is not None:
            raise CorruptGeneration(f"unauthorized {context} status: {key}")


def _canonical_control_image(path: Path) -> tuple[dict[str, Any], bytes, os.stat_result]:
    payload, raw, info = strict_json_image(path, require_canonical=True)
    if type(payload) is not dict:
        raise CorruptGeneration(f"control is not a JSON object: {path}")
    return dict(payload), raw, info


def _validated_component_control_chain(
    output: Path,
    name: str,
    run_config_sha256: str,
    aggregate_summary: Mapping[str, Any],
    aggregate_manifest: Mapping[str, Any],
) -> dict[str, Any]:
    if name not in {"static", "branch"}:
        raise SchedulerContractError("unknown component control chain")
    summary_path = output / name / "aggregate_summary.json"
    manifest_path = output / name / "aggregate_manifest.json"
    checker_path = output / f"independent_{name}_checker.json"
    postcheck_path = output / f"{name.upper()}_POSTCHECK_STATUS.json"
    summary_raw, summary_info = read_pinned_regular_file(summary_path)
    manifest_raw, manifest_info = read_pinned_regular_file(manifest_path)
    checker, checker_raw, checker_info = _canonical_control_image(checker_path)
    postcheck, postcheck_raw, postcheck_info = _canonical_control_image(postcheck_path)

    exact_keys(checker, COMPONENT_CHECKER_KEYS, f"{name} checker")
    exact_keys(postcheck, COMPONENT_POSTCHECK_KEYS, f"{name} postcheck")
    if checker["schema_version"] != SCHEMA_VERSION or type(checker["schema_version"]) is not int:
        raise CorruptGeneration(f"{name} checker schema mismatch")
    if (
        checker["protocol_id"] != PROTOCOL_ID
        or checker["artifact_role"] != f"{name.upper()}_INDEPENDENT_CHECKER"
        or checker["authority"] != "INDEPENDENT_CHECKER"
        or checker["checker_status"] != MOCK_CHECKER_STATUS
        or checker["passed"] is not True
        or checker["scientific_licensing_enabled"] is not False
        or checker["matrix_id"] != canonical_matrix_id()
        or checker["main_freeze_sha256"] is not None
        or checker["run_config_sha256"] != run_config_sha256
        or checker["component_aggregate_summary_sha256"]
        != sha256_bytes(summary_raw)
        or checker["component_aggregate_manifest_sha256"]
        != sha256_bytes(manifest_raw)
        or checker["failures"] != []
    ):
        raise CorruptGeneration(f"{name} checker mock chain mismatch")
    _require_null_authority_statuses(checker, f"{name} checker")

    if postcheck["schema_version"] != SCHEMA_VERSION or type(postcheck["schema_version"]) is not int:
        raise CorruptGeneration(f"{name} postcheck schema mismatch")
    checker_source = (
        STATIC_CHECKER_SOURCE if name == "static" else BRANCH_CHECKER_SOURCE
    )
    expected_bound = {
        "aggregate_manifest": {
            "path": f"{name}/aggregate_manifest.json",
            "sha256": sha256_bytes(manifest_raw),
        },
        "aggregate_summary": {
            "path": f"{name}/aggregate_summary.json",
            "sha256": sha256_bytes(summary_raw),
        },
        "checker_source": {
            "path": checker_source.relative_to(ROOT).as_posix(),
            "sha256": sha256(checker_source),
        },
    }
    if (
        postcheck["protocol_id"] != PROTOCOL_ID
        or postcheck["artifact_role"] != f"{name.upper()}_POSTCHECK"
        or postcheck["authority"] != "POSTCHECK_ONLY"
        or postcheck["postcheck_status"] != MOCK_POSTCHECK_STATUS
        or postcheck["passed"] is not True
        or postcheck["checker_path"] != f"independent_{name}_checker.json"
        or postcheck["checker_sha256"] != sha256_bytes(checker_raw)
        or postcheck["main_freeze_sha256"] is not None
        or postcheck["run_config_sha256"] != run_config_sha256
        or not exact_json_equal(postcheck["bound_artifacts"], expected_bound)
        or postcheck["failures"] != []
    ):
        raise CorruptGeneration(f"{name} postcheck mock chain mismatch")
    _require_null_authority_statuses(postcheck, f"{name} postcheck")

    if aggregate_summary["ordered_cell_manifest_root"] != (
        aggregate_manifest["ordered_cell_manifest_root"]
    ):
        raise CorruptGeneration(f"{name} aggregate root disagreement")
    # Size metadata are read from the same pinned images used for hashing.
    if summary_info.st_size != len(summary_raw) or manifest_info.st_size != len(manifest_raw):
        raise CorruptGeneration(f"{name} aggregate snapshot size mismatch")
    if checker_info.st_size != len(checker_raw) or postcheck_info.st_size != len(postcheck_raw):
        raise CorruptGeneration(f"{name} control snapshot size mismatch")
    return {
        "aggregate_summary": {
            "path": summary_path.relative_to(output).as_posix(),
            "sha256": sha256_bytes(summary_raw),
        },
        "aggregate_manifest": {
            "path": manifest_path.relative_to(output).as_posix(),
            "sha256": sha256_bytes(manifest_raw),
        },
        "checker": {
            "path": checker_path.relative_to(output).as_posix(),
            "sha256": sha256_bytes(checker_raw),
        },
        "postcheck": {
            "path": postcheck_path.relative_to(output).as_posix(),
            "sha256": sha256_bytes(postcheck_raw),
        },
        "ordered_cell_manifest_root": aggregate_summary[
            "ordered_cell_manifest_root"
        ],
    }


def validated_mock_component_chains(
    output: Path,
) -> tuple[str, dict[str, Any], dict[str, Any]]:
    binding = build_mock_binding(output, operational_root_for(output))
    stored, run_config_sha256 = ensure_run_config(output, binding, resume=True)
    static_summary, static_manifest = validate_static_mock_aggregate(
        output, stored["matrix_id"], run_config_sha256
    )
    branch_summary = strict_json_load(
        branch_aggregate_summary_path(output), require_canonical=True
    )
    if type(branch_summary) is not dict or type(branch_summary.get("mock_evaluator")) is not dict:
        raise CorruptGeneration("branch aggregate lacks its mock evaluator binding")
    mock_evaluator = validate_mock_branch_evaluator(
        output, Path(branch_summary["mock_evaluator"].get("path", ""))
    )
    if not exact_json_equal(mock_evaluator, branch_summary["mock_evaluator"]):
        raise CorruptGeneration("live mock evaluator differs from branch aggregate")
    tasks = build_mock_branch_tasks(Path(mock_evaluator["path"]))
    branch_bindings = mock_branch_bindings(
        stored["matrix_id"], run_config_sha256, mock_evaluator
    )
    branch_summary, branch_manifest = validate_branch_mock_aggregate(
        output,
        tasks,
        branch_bindings,
        _branch_runtime().BranchBudgets(),
        mock_evaluator,
    )
    static_chain = _validated_component_control_chain(
        output,
        "static",
        run_config_sha256,
        static_summary,
        static_manifest,
    )
    branch_chain = _validated_component_control_chain(
        output,
        "branch",
        run_config_sha256,
        branch_summary,
        branch_manifest,
    )
    return run_config_sha256, static_chain, branch_chain


def expected_mock_composite_controls(
    run_config_sha256: str,
    static_chain: Mapping[str, Any],
    branch_chain: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    chains = {"static": dict(static_chain), "branch": dict(branch_chain)}
    generation = sha256_bytes(canonical_json_bytes(chains))
    summary = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_COMPOSITE_SUMMARY",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": canonical_matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "matrix": matrix_payload(),
        "cell_count_per_component": 102,
        "component_chains": chains,
        "archive_generation_sha256": generation,
        "scientific_licensing_enabled": False,
        "claim_boundary": COMPOSITE_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    summary_raw = canonical_json_bytes(summary)
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MOCK_COMPOSITE_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": canonical_matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_config_sha256,
        "component_chains": chains,
        "archive_generation_sha256": generation,
        "summary": {
            "path": "composite_summary.json",
            "sha256": sha256_bytes(summary_raw),
            "size_bytes": len(summary_raw),
        },
        "scientific_licensing_enabled": False,
        "claim_boundary": COMPOSITE_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    return summary, manifest


def validate_mock_composite_controls(
    output: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    run_config_sha256, static_chain, branch_chain = (
        validated_mock_component_chains(output)
    )
    expected_summary, expected_manifest = expected_mock_composite_controls(
        run_config_sha256, static_chain, branch_chain
    )
    summary = strict_json_load(
        output / "composite_summary.json", require_canonical=True
    )
    manifest = strict_json_load(
        output / "composite_manifest.json", require_canonical=True
    )
    if not exact_json_equal(summary, expected_summary):
        raise CorruptGeneration("mock composite summary mismatch")
    if not exact_json_equal(manifest, expected_manifest):
        raise CorruptGeneration("mock composite manifest mismatch")
    return dict(summary), dict(manifest)


def finalize_mock_composite_controls(
    output: Path,
) -> tuple[str, dict[str, Any], dict[str, Any]]:
    """Write the null-authority composite producer pair, manifest last."""

    summary_path = output / "composite_summary.json"
    manifest_path = output / "composite_manifest.json"
    if manifest_path.exists() and not summary_path.exists():
        raise CorruptGeneration("composite manifest exists without summary")
    if manifest_path.exists():
        summary, manifest = validate_mock_composite_controls(output)
        return "RESUMED_COMMITTED", summary, manifest
    run_config_sha256, static_chain, branch_chain = (
        validated_mock_component_chains(output)
    )
    summary, manifest = expected_mock_composite_controls(
        run_config_sha256, static_chain, branch_chain
    )
    if summary_path.exists():
        stored = strict_json_load(summary_path, require_canonical=True)
        if not exact_json_equal(stored, summary):
            raise CorruptGeneration("manifest-less composite summary mismatch")
        state = "RECOVERED_MANIFEST"
    else:
        exclusive_write_json(summary_path, summary)
        state = "COMMITTED"
    exclusive_write_json(manifest_path, manifest)
    checked_summary, checked_manifest = validate_mock_composite_controls(output)
    return state, checked_summary, checked_manifest


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    # Keep the raw lexical spelling for the formal path gate.  Converting to
    # Path/absolute first would erase relative, '..', repeated-separator, and
    # trailing-slash provenance that must fail closed.
    parser.add_argument("--output")
    parser.add_argument("--authority-root", default=str(ROOT))
    parser.add_argument("--initialize-only", action="store_true")
    parser.add_argument("--mock-only", action="store_true")
    parser.add_argument("--mock-static-cells", type=int, default=0)
    parser.add_argument("--mock-branch-cells", type=int, default=0)
    parser.add_argument(
        "--mock-branch-evaluator",
        type=Path,
        default=MOCK_BRANCH_EVALUATOR,
    )
    parser.add_argument("--finalize-mock-composite", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--production", action="store_true")
    parser.add_argument("--execute-scientific-dispatch", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.mock_only:
            if arguments.production or arguments.execute_scientific_dispatch:
                raise SchedulerContractError("mock and production modes are exclusive")
            if (
                not arguments.initialize_only
                and arguments.mock_static_cells == 0
                and arguments.mock_branch_cells == 0
                and not arguments.finalize_mock_composite
            ):
                raise SchedulerContractError(
                    "mock-only requires initialize, static cells, or branch cells"
                )
            output = Path(arguments.output or CANONICAL_RESULT).absolute()
            static_result: dict[str, Any] | None = None
            branch_result: dict[str, Any] | None = None
            composite_result: dict[str, Any] | None = None
            if arguments.initialize_only or arguments.mock_static_cells:
                static_result = run_mock_static(
                    output,
                    arguments.mock_static_cells,
                    resume=arguments.resume,
                )
            if arguments.mock_branch_cells:
                if arguments.mock_static_cells not in (0, 102):
                    raise SchedulerContractError(
                        "branch mock requires the complete 102-cell static gate"
                    )
                if arguments.mock_static_cells == 0 and not arguments.resume:
                    raise SchedulerContractError(
                        "branch-only continuation requires explicit --resume"
                    )
                branch_result = run_mock_branch(
                    output,
                    arguments.mock_branch_evaluator.absolute(),
                    arguments.mock_branch_cells,
                    resume=arguments.resume,
                )
            if arguments.finalize_mock_composite:
                if (
                    arguments.mock_static_cells == 0
                    and arguments.mock_branch_cells == 0
                    and not arguments.resume
                ):
                    raise SchedulerContractError(
                        "composite-only continuation requires explicit --resume"
                    )
                composite_state, composite_summary, composite_manifest = (
                    finalize_mock_composite_controls(output)
                )
                composite_result = {
                    "state": composite_state,
                    "archive_generation_sha256": composite_summary[
                        "archive_generation_sha256"
                    ],
                    "summary_sha256": composite_manifest["summary"]["sha256"],
                    "manifest_sha256": sha256(output / "composite_manifest.json"),
                }
            if branch_result is None and composite_result is None:
                assert static_result is not None
                result: dict[str, Any] = static_result
            else:
                result = {
                    "artifact_status": "MOCK_ONLY_NON_LICENSING",
                    "mock_only": True,
                    "static": static_result,
                    "branch": branch_result,
                    "composite": composite_result,
                    "component_status": None,
                    "milestone_status": None,
                    "theorem_status": None,
                    "final_status": None,
                }
            print(json.dumps(result, sort_keys=True))
            return 0

        if arguments.initialize_only:
            if arguments.production or arguments.execute_scientific_dispatch or arguments.resume:
                raise RunBindingMismatch("formal initialize/execute modes are an exact XOR")
            if (
                arguments.mock_static_cells
                or arguments.mock_branch_cells
                or arguments.finalize_mock_composite
            ):
                raise SchedulerContractError(
                    "formal initialize-only cannot request component work"
                )
            if arguments.output is None:
                raise PathContractError(
                    "formal initialize-only requires an explicit noncanonical --output"
                )
            # Authority is captured before inspecting or creating the output.
            try:
                snapshot = load_formal_authority(arguments.authority_root)
            except (FileNotFoundError, PathContractError) as error:
                raise ProductionAuthorityError(
                    f"formal authority absent or unsafe; production rejected: {error}"
                ) from error
            binding, run_config_sha256 = initialize_formal_preflight(
                snapshot, arguments.output
            )
            print(
                json.dumps(
                    {
                        "artifact_status": binding["artifact_status"],
                        "artifact_role": binding["artifact_role"],
                        "authority": binding["authority"],
                        "production_authorized": False,
                        "scientific_licensing_enabled": False,
                        "dispatch_authorized_by_artifact": False,
                        "input_role_count": len(binding["input_roles"]),
                        "freeze_sha256": binding["freeze_sha256"],
                        "main_freeze_sha256": binding["main_freeze_sha256"],
                        "run_config_sha256": run_config_sha256,
                        "component_status": None,
                        "milestone_status": None,
                        "theorem_status": None,
                        "final_status": None,
                    },
                    sort_keys=True,
                )
            )
            return 0

        execute_tuple = (
            arguments.production,
            arguments.execute_scientific_dispatch,
            arguments.resume,
        )
        if any(execute_tuple):
            if execute_tuple != (True, True, True):
                raise ProductionAuthorityError(
                    "production rejected: execute mode requires exact flags "
                    "--production --execute-scientific-dispatch --resume"
                )
            # Even the exact execution spelling remains an unconditional hard
            # stop until the branch millisecond migration and independent
            # freeze/release gates are complete.
            raise ProductionAuthorityError(
                "production rejected: formal scientific dispatch is "
                "unconditionally disabled pending finalized contracts"
            )

        raise ProductionAuthorityError(
            "production rejected: choose mock-only or formal initialize-only; "
            "scientific dispatch is disabled"
        )
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
