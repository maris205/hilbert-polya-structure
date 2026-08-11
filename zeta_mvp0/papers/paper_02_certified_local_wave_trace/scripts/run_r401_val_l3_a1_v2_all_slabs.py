#!/usr/bin/env python3
"""Prospective L3-A1 scheduler framework.

This module implements strict matrix/run-binding plus complete mock-only
static and branch archive transactions.  The branch path can execute only an
explicit synthetic executable outside either result root; it reuses the
hardened bounded-process and branch-cell transaction runtime.  It also has a
formal *preflight* handshake which can snapshot the prospective 53 input
roles and write one visibly non-licensing, non-promotable run-config candidate
in an explicit noncanonical temporary root.  A separate exact-exclusive mode
can capture a temp-only machine-freeze candidate: it performs metadata probes
and one truthful fresh /tmp compiler rebuild, never executes either scientific
evaluator, never overwrites the persistent binary, and can publish only to a
missing caller-supplied /tmp file.  A distinct exact-exclusive publisher can
copy a previously verified candidate into the fixed role-10 path through a
same-parent, no-replace, durable transaction; it has not been invoked here and
its receipt remains pending an independent role-24 post-publication
verification.  Neither the candidate nor the publication receipt authorizes
dispatch.  Production dispatch remains unconditionally disabled pending the
later 53-input freeze/review/release sequence.
"""

from __future__ import annotations

import argparse
import base64
import ctypes
import csv
import errno
import fcntl
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import selectors
import signal
import shlex
import stat
import struct
import subprocess
import sys
import tempfile
import threading
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
    ROOT / "scripts/check_r401_val_l3_a1_v2_static_independent.py"
)
BRANCH_CHECKER_SOURCE = (
    ROOT / "scripts/check_r401_val_l3_a1_v2_branch_independent.py"
)
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PROTOCOL.md"
SCHEDULER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_SCHEDULER_CONTRACT.md"
)
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_RELEASE_PROVENANCE_CONTRACT.md"
)
MACHINE_FREEZE = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"
)
MAIN_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json"
PREFREEZE_REVIEW = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md"
)
CANONICAL_RESULT = ROOT / "results/r401_val_l3_a1_v2_all_slabs"
CANONICAL_OPERATIONAL = ROOT / "results/r401_val_l3_a1_v2_all_slabs.operational"
DEFAULT_CAPD_CHECKOUT = (
    ROOT.parents[3] / "dependencies/capd-r401-a1"
)
DEFAULT_COMPILER = Path("/usr/bin/g++")
DEFAULT_SYSTEM_LIBRARY_ROOT = Path("/usr/lib/x86_64-linux-gnu")

MACHINE_PUBLICATION_METHOD = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
MACHINE_PUBLICATION_AUTHORITY = "ROLE19_MACHINE_FREEZE_PUBLICATION_ONLY"
PREFREEZE_TEST_PUBLICATION_AUTHORITY = "ROLE19_PREFREEZE_TESTS_PUBLICATION_ONLY"
FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY = "ROLE19_RUN_CONFIG_PUBLICATION_ONLY"
FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY = (
    "ROLE19_COMPONENT_AGGREGATES_PUBLICATION_ONLY"
)
FORMAL_COMPOSITE_PUBLICATION_AUTHORITY = (
    "ROLE19_COMPOSITE_PRODUCER_PUBLICATION_ONLY"
)
V2_ROLE5_PUBLICATION_AUTHORITY = "ROLE19_DESIGN_REVIEW_PUBLICATION_ONLY"
V2_ROLE5_VERIFY_AUTHORITY = "NON_AUTHORITATIVE_VERIFY_ONLY"
V2_ROLE5_VERIFY_STATUS = (
    "PASS_V2_DESIGN_REVIEW_WITHDRAWAL_VERIFY_ONLY"
)
V2_ROLE5_PUBLICATION_METHOD = "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
V2_ROLE5_CANDIDATE_MAX_BYTES = 1024 * 1024
V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES = 4096
V2_ROLE5_CANDIDATE_BASENAME = (
    "R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"
)
V2_ROLE5_VERIFY_RECEIPT_BASENAME = "ROLE24_ROLE5_VERIFY_RECEIPT.json"
V2_ROLE5_CANDIDATE_PARENT_PATTERN = re.compile(
    r"^a416-v2-role5-review\.[0-9a-f]{32}$"
)
V2_ROLE5_VERIFY_PARENT_PATTERN = re.compile(
    r"^a416-v2-role5-verify\.[0-9a-f]{32}$"
)
V2_ROLE5_STAGE_PATTERN = re.compile(
    r"^\.R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL\.json\.publish-"
    r"[0-9a-f]{32}$"
)
V2_ROLE5_VERIFY_RECEIPT_KEYS = {
    "verification_status", "authority", "candidate_sha256",
    "input_map_sha256", "size_bytes", "promotion_authorized",
    "artifacts_written",
}
MACHINE_PUBLICATION_MAX_CANDIDATE_BYTES = 1024 * 1024
FORMAL_PRODUCER_CANDIDATE_MAX_BYTES = 4 * 1024 * 1024
FORMAL_PRODUCER_PUBLICATION_METHOD = (
    "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1"
)
MACHINE_PUBLICATION_STAGE_PATTERN = re.compile(
    r"^\.R401_VAL_L3_A1_V2_MACHINE_FREEZE\.json\.publish-[0-9a-f]{32}$"
)
MACHINE_PUBLICATION_HOOK_PHASES = frozenset(
    {
        "AFTER_STAGE_WRITE",
        "AFTER_STAGE_FILE_FSYNC",
        "AFTER_STAGING_PARENT_FSYNC",
        "BEFORE_TERMINAL_REPLAY",
        "BEFORE_RENAME",
        "AFTER_RENAME",
        "AFTER_DESTINATION_FSYNC",
        "AFTER_PUBLICATION_PARENT_FSYNC",
    }
)
V2_ROLE5_PUBLICATION_HOOK_PHASES = frozenset(
    (*MACHINE_PUBLICATION_HOOK_PHASES, "AFTER_ULTIMATE_REPLAY")
)

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
    ("prefreeze_design", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_DESIGN.md"),
    ("implementation_design_review", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json"),
    ("formal_protocol", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PROTOCOL.md"),
    ("scheduler_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_SCHEDULER_CONTRACT.md"),
    ("checker_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_CHECKER_CONTRACT.md"),
    ("release_contract", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_RELEASE_PROVENANCE_CONTRACT.md"),
    ("machine_freeze", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_MACHINE_FREEZE.json"),
    ("prefreeze_tests", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json"),
    ("prefreeze_review", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_REVIEW.md"),
    ("s0_compatibility", "research/route_a_wave_trace/R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"),
    ("capd_dependency", "validated/CAPD_DEPENDENCY.md"),
    ("static_evaluator", "scripts/evaluate_r401_val_l3_a1_static_cell.py"),
    ("branch_evaluator_source", "validated/capd_r401_phase_branch_tube_mp_a1.cpp"),
    ("branch_evaluator_binary", "validated/bin/capd_r401_phase_branch_tube_mp_a1"),
    ("branch_runtime", "scripts/r401_val_l3_a1_branch_runtime.py"),
    ("scheduler", "scripts/run_r401_val_l3_a1_v2_all_slabs.py"),
    ("static_checker_source", "scripts/check_r401_val_l3_a1_v2_static_independent.py"),
    ("branch_checker_source", "scripts/check_r401_val_l3_a1_v2_branch_independent.py"),
    ("composite_checker_source", "scripts/check_r401_val_l3_a1_v2_composite_independent.py"),
    ("s0_adapter", "scripts/replay_r401_val_l3_s0_through_a1_v2_checkers.py"),
    ("release_builder", "scripts/build_r401_val_l3_a1_v2_release_provenance.py"),
    ("test_static_evaluator", "tests/test_r401_val_l3_a1_static_cell.py"),
    ("test_static_scheduler", "tests/test_r401_val_l3_a1_v2_static_scheduler.py"),
    ("test_static_checker", "tests/test_r401_val_l3_a1_v2_static_checker.py"),
    ("test_branch_scheduler", "tests/test_r401_val_l3_a1_v2_branch_scheduler.py"),
    ("test_branch_checker", "tests/test_r401_val_l3_a1_v2_branch_checker.py"),
    ("test_s0_compatibility", "tests/test_r401_val_l3_a1_v2_s0_compatibility.py"),
    ("test_composite", "tests/test_r401_val_l3_a1_v2_composite_contract.py"),
    ("test_adversarial", "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py"),
    ("test_release", "tests/test_r401_val_l3_a1_v2_release_provenance.py"),
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

# Role 5 is the machine-readable boundary between immutable attempt-1 audit
# evidence and the V2 control plane.  These literals are intentionally
# duplicated from the contracts: role 19 does not import a producer, checker,
# release builder, or Markdown parser to decide authority.
V2_ROLE5_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "production_authorized", "legacy_attempt",
    "reviewed_v2_inputs", "review", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
V2_ROLE5_LEGACY_KEYS = {
    "attempt_id", "status", "terminal_commit", "published_artifacts",
    "defects", "supersession_rule",
}
V2_ROLE5_PUBLISHED_KEYS = {"role", "path", "sha256", "publication_commit"}
V2_ROLE5_DEFECT_KEYS = {"severity", "code", "finding"}
V2_ROLE5_REVIEWED_KEYS = {"role", "path", "sha256"}
V2_ROLE5_REVIEW_KEYS = {
    "reviewer_independent_of_attempt1_author", "verdict", "p0_count",
    "p1_count", "p2_count", "reviewed_commit", "map_matches_contract",
    "legacy_bytes_unchanged", "scientific_protocol_unchanged",
}
V2_ROLE5_LEGACY_ARTIFACTS: tuple[dict[str, Any], ...] = (
    {
        "role": 10,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json",
        "sha256": "0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e",
        "publication_commit": "5086e33c7c66f33785338e90b340347e086d9941",
    },
    {
        "role": 11,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json",
        "sha256": "08ffeb5e7f5d681567bd7a81335585d1b8697040a28d91584b09fdc4304a379a",
        "publication_commit": "201758031a7784a68ab66d37094c25135de52646",
    },
    {
        "role": 12,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md",
        "sha256": "af38e899f9dad9abacadbdaa27f12833d5ea423a9896ee089fb8a4d90b55477c",
        "publication_commit": "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0",
    },
    {
        "role": 13,
        "path": "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json",
        "sha256": "d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30",
        "publication_commit": "be2a732625d9cab97879539873a756e1eabd366d",
    },
)
V2_ROLE5_DEFECTS: tuple[dict[str, str], ...] = (
    {
        "severity": "P1",
        "code": "ROLE24_MOCK_ONLY_NO_FORMAL_54_OR_68_VALIDATION",
        "finding": (
            "legacy role 24 implements mock release and machine verification only; "
            "it does not implement formal role-54 validation or publication or "
            "formal 68-role release validation or publication"
        ),
    },
    {
        "severity": "P1",
        "code": "ROLES20_22_NO_FORMAL_THREE_CHECKER_THREE_POSTCHECK_CHAIN",
        "finding": (
            "legacy roles 20 through 22 do not implement the required formal "
            "static, branch, and composite checker plus postcheck publication chain"
        ),
    },
)
V2_ROLE5_SUPERSESSION_RULE = (
    "legacy attempt-1 bytes remain immutable audit evidence, are not V2 inputs, "
    "and confer no freeze, initialization, scientific licensing, promotion, or "
    "dispatch authority"
)
V2_ROLE5_CLAIM_BOUNDARY = (
    "independent withdrawal of control attempt 1 and acceptance of the reviewed "
    "V2 control implementation only; no machine, main freeze, result, theorem, "
    "release, initialization, promotion, or dispatch acceptance"
)
V2_ROLE5_REVIEWED_ROLES = (
    "prefreeze_design", "formal_protocol", "scheduler_contract",
    "checker_contract", "release_contract", "scheduler",
    "static_checker_source", "branch_checker_source",
    "composite_checker_source", "s0_adapter", "release_builder",
    "test_static_scheduler", "test_static_checker", "test_branch_scheduler",
    "test_branch_checker", "test_s0_compatibility", "test_composite",
    "test_adversarial", "test_release",
)

V2_PREFREEZE_TEST_KEYS = {
    "artifact_role", "artifact_status", "authority", "claim_boundary",
    "command_results", "component_status", "covered_gates",
    "evidence_tool_bindings", "final_status", "held_out_policy",
    "milestone_status", "pre_review_input_roles", "prerequisite_bindings",
    "production_authorized", "protocol_id", "recorded_at_utc",
    "repository_snapshot", "schema_version", "scientific_dispatch_performed",
    "scientific_licensing_enabled", "test_totals", "theorem_status",
}
V2_PREFREEZE_INPUT_KEYS = {"mode", "nlink", "path", "role", "sha256", "size_bytes"}
V2_S0_COMPATIBILITY_KEYS = {
    "artifact_role", "artifact_status", "branch_facts", "claim_boundary",
    "composite_facts", "control_hashes", "failures", "final_status", "matrix",
    "milestone_status", "protocol_id", "replay_status", "role_sets",
    "schema_version", "source_bindings", "source_protocols", "static_facts",
    "theorem_status",
}
V2_S0_COMPATIBILITY_CLAIM_BOUNDARY = (
    "read-only compatibility replay of the sealed representative 3x2 S0 archive "
    "only; non-licensing and no evaluator dispatch; no all-slab result, theorem "
    "promotion, global orbit exclusion, trace formula, Hilbert-Polya construction, "
    "zeta-zero result, or RH claim"
)
V2_S0_CONTROL_ROLE_MAP = {
    "static_summary": "s0_static_summary",
    "static_manifest": "s0_static_manifest",
    "static_checker": "s0_static_checker",
    "branch_summary": "s0_branch_summary",
    "branch_manifest": "s0_branch_manifest",
    "branch_checker": "s0_branch_checker",
    "composite_summary": "s0_composite_summary",
    "composite_manifest": "s0_composite_manifest",
    "composite_checker": "s0_composite_checker",
}
V2_S0_STATIC_FACTS = {
    "proof_count": 6,
    "node_count": 84172,
    "internal_count": 42074,
    "terminal_count": 42098,
    "unresolved_count": 0,
    "independent_interval_checks": 122300,
    "maximum_depth": 14,
}
V2_S0_BRANCH_FACTS = {"raw_replay_count": 6, "manifest_file_count": 26}
V2_S0_COMPOSITE_FACTS = {
    "cell_replay_count": 6,
    "manifest_binding_count": 18,
    "failure_count": 0,
}
V2_S0_SOURCE_PROTOCOLS = {
    "static": "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT",
    "branch": "R401-VAL-L3-BT-S0",
    "composite": "R401-VAL-L3-S0-COMPOSITE-DRAFT",
}
V2_S0_STATIC_ENTRY_KEYS = {
    "internal_count", "node_count", "path", "precision_bits", "sha256",
    "size_bytes", "slab_id", "terminal_count", "tree_content_sha256",
    "unresolved_count",
}
V2_ROLE11_COMMAND_NAMES = (
    "role24_machine_verify", "role13_compatibility_verify",
    "prefreeze_focused_pytest", "l3_a1_modules_pytest",
    "paper02_full_pytest", "git_diff_check", "second_fresh_rebuild",
)
V2_ROLE11_COMMAND_KINDS = (
    "VERIFY_MACHINE_FREEZE", "VERIFY_S0_COMPATIBILITY", "PYTEST_FOCUSED",
    "PYTEST_L3_A1", "PYTEST_PAPER02", "GIT_DIFF_CHECK",
    "SECOND_FRESH_REBUILD",
)
V2_ROLE11_TOOL_ROLES = {
    "producer": "scheduler",
    "independent_checker": "release_builder",
    "focused_test": "test_adversarial",
}
V2_ROLE11_COMMAND_RESULT_KEYS = {
    "name", "kind", "argv", "cwd", "environment", "return_code",
    "started_at_utc", "wall_duration_ms", "stdout_utf8", "stdout_sha256",
    "stdout_size_bytes", "stderr_utf8", "stderr_sha256",
    "stderr_size_bytes", "pytest_counts", "semantic_receipt",
}
V2_ROLE11_TEST_TOTAL_KEYS = {
    "passed", "failed", "skipped", "xfailed", "xpassed", "wall_duration_ms",
}
V2_ROLE11_PROTOCOL_ID = "R401-VAL-L3-A1-PREFREEZE-TESTS"
V2_ROLE11_ARTIFACT_ROLE = "PREFREEZE_TEST_RECORD"
V2_ROLE11_ARTIFACT_STATUS = "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW"
V2_ROLE11_AUTHORITY = "PREFREEZE_TEST_EVIDENCE_ONLY"
V2_ROLE11_CLAIM_BOUNDARY = (
    "pre-freeze engineering test evidence only; no held-out or all-slab L3 "
    "result was read and no scientific evaluator was dispatched; no L3-A1 "
    "component, milestone, theorem, final, global tube-routing, trace-formula, "
    "Hilbert-Polya, zeta-zero, RH, or implication-toward-RH claim"
)
V2_ROLE11_REPOSITORY_KEYS = {
    "authority_root", "branch", "capture_commit_oid", "capture_tree_oid",
    "origin_url", "origin_main_oid", "live_remote_main_oid",
    "head_equals_origin_main", "head_equals_live_remote_main", "ahead",
    "behind", "worktree_clean_before", "worktree_clean_after",
}
V2_ROLE11_PREREQUISITE_KEYS = {
    "machine_role10", "s0_compatibility_role13",
    "second_fresh_rebuild_replay", "canonical_absence",
}
V2_ROLE11_MACHINE_BINDING_KEYS = {
    "role", "path", "sha256", "size_bytes", "mode", "nlink",
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verifier_path", "verifier_sha256", "verify_receipt",
    "promotion_authorized",
}
V2_ROLE11_S0_BINDING_KEYS = {
    "role", "path", "sha256", "size_bytes", "mode", "nlink",
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verify_receipt", "promotion_authorized",
}
V2_ROLE11_VERIFY_RECEIPT_KEYS = {
    "verification_status", "authority", "candidate_sha256", "size_bytes",
    "promotion_authorized",
}
V2_ROLE11_SECOND_REBUILD_REPLAY_KEYS = {
    "command_result_name", "command_result_sha256", "semantic_receipt",
}
V2_ROLE11_CANONICAL_ABSENCE_KEYS = {
    "prefreeze_review_role12_exists", "main_freeze_role54_exists",
    "canonical_result_root_exists", "canonical_operational_root_exists",
}
V2_ROLE11_SECOND_REBUILD_KEYS = {
    "verification_status", "authority", "source_path", "source_sha256",
    "persistent_binary_path", "persistent_before_sha256",
    "persistent_after_sha256", "persistent_before_device_id",
    "persistent_before_inode", "persistent_after_device_id",
    "persistent_after_inode", "persistent_identity_unchanged",
    "persistent_overwrite_performed", "staging_output_sha256",
    "staging_output_size_bytes", "staging_output_mode",
    "staging_output_removed", "byte_for_byte_equal",
    "scientific_evaluator_dispatched",
}
V2_ROLE11_HELD_OUT_POLICY_KEYS = {
    "held_out_l3_scientific_outputs_read", "held_out_l3_evaluator_dispatched",
    "scientific_evaluator_dispatch_count", "new_archive_scope",
    "s0_archive_access", "canonical_result_created",
}
V2_ROLE11_TEST_TOTALS_KEYS = {
    "prefreeze_focused", "l3_a1_modules", "paper02_full",
}
V2_ROLE11_EVIDENCE_TOOL_KEYS = {
    "producer", "independent_checker", "focused_test",
}
V2_ROLE11_FILE_BINDING_KEYS = {
    "path", "sha256", "size_bytes", "mode", "nlink",
}
V2_ROLE11_PRE_REVIEW_ROLES = tuple(
    item for item in FORMAL_INPUT_ROLES
    if item[0] not in {"prefreeze_tests", "prefreeze_review"}
)
V2_ROLE11_TOOL_PATHS = {
    "producer": "scripts/run_r401_val_l3_a1_v2_all_slabs.py",
    "independent_checker": "scripts/build_r401_val_l3_a1_v2_release_provenance.py",
    "focused_test": "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py",
}
V2_ROLE11_COVERED_GATES = (
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
V2_ROLE11_ENVIRONMENT = {
    "PATH": "/root/miniconda3/bin:/usr/bin:/bin",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
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
V2_ROLE11_PYTEST_TOTAL_NAMES = {
    "prefreeze_focused_pytest": "prefreeze_focused",
    "l3_a1_modules_pytest": "l3_a1_modules",
    "paper02_full_pytest": "paper02_full",
}
V2_ROLE11_ORIGIN_URL = "git@github.com:maris205/hilbert-polya-structure.git"
V2_ROLE11_MAX_STREAM_BYTES = 1024 * 1024
V2_ROLE11_MAX_CANDIDATE_BYTES = 4 * 1024 * 1024
V2_ROLE11_MAX_WALL_DURATION_MS = 603000
V2_ROLE11_UTC = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
)
V2_ROLE11_MODE = re.compile(r"^0[0-7]{3}$")
V2_ROLE11_GIT_OID = re.compile(r"^[0-9a-f]{40}$")
V2_ROLE11_REBUILD_OUTPUT = re.compile(
    r"^/tmp/a416-l3a1-v2-role11-rebuild\.[0-9A-Za-z]{6,}/"
    r"capd_r401_phase_branch_tube_mp_a1$"
)
V2_ROLE11_PYTEST_SUMMARY = re.compile(
    r"^(?P<counts>[1-9][0-9]{0,3} (?:passed|failed|skipped|xfailed|xpassed)"
    r"(?:, [1-9][0-9]{0,3} (?:passed|failed|skipped|xfailed|xpassed))*) "
    r"in (?P<elapsed>(?:0|[1-9][0-9]{0,2})\.[0-9]{2})s"
    r"(?: \((?P<hours>0):(?P<minutes>[0-5][0-9]):"
    r"(?P<seconds>[0-5][0-9])\))?$"
)
V2_ROLE11_EXPECTED_TEST_PASSED: dict[str, int] | None = {
    "prefreeze_focused": 23,
    "l3_a1_modules": 972,
    "paper02_full": 1951,
}
V2_ROLE11_FINAL_COMMAND_LOCKED = True

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
        "input_roles",
        "machine_freeze_sha256",
        "prefreeze_review",
        "serializers",
        "scheduler",
        "limits",
        "status_tables",
        "evaluators",
        "checkers",
        "archive_layout",
        "machine_requirements",
        "failure_policy",
        "execution_policy",
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
    "executable_path", "executable_sha256", "version", "build_recipe",
    "fresh_rebuild_receipt", "transfer_evidence",
}
MACHINE_BUILD_RECIPE_KEYS = {
    "cwd", "environment", "umask", "staging_output_token",
    "argv_template", "argv_template_sha256",
}
MACHINE_FRESH_REBUILD_RECEIPT_KEYS = {
    "cwd", "environment", "umask", "staging_directory",
    "staging_output_path", "argv", "argv_sha256", "stdout", "stderr",
    "stdout_sha256", "stderr_sha256", "return_code", "output_sha256",
    "output_size_bytes", "output_mode", "output_build_id",
    "output_dt_needed", "output_dt_needed_sha256", "output_soname",
    "shell_used",
}
MACHINE_TRANSFER_EVIDENCE_KEYS = {
    "branch_calibration_binary_sha256", "staging_output_sha256",
    "staging_output_size_bytes",
    "staging_output_mode", "persistent_before_sha256",
    "persistent_before_size_bytes", "persistent_before_mode",
    "persistent_before_device_id", "persistent_before_inode",
    "persistent_after_sha256", "persistent_after_size_bytes",
    "persistent_after_mode", "persistent_after_device_id",
    "persistent_after_inode", "byte_for_byte_equal",
    "persistent_identity_unchanged", "persistent_overwrite_performed",
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
FORMAL_BRANCH_CELL_CLAIM_BOUNDARY = (
    "accepted-branch complete-period tube cell only; no arbitrary-candidate "
    "tube routing, global uniqueness, trace, Hilbert--Polya, zeta, or RH claim"
)
FORMAL_AGGREGATE_CLAIM_BOUNDARY = (
    "complete 102-cell producer archive only; independent component replay "
    "remains required and no component, theorem, Hilbert-Polya, zeta-zero, or RH status is assigned"
)
FORMAL_STATIC_CHECKER_CLAIM_BOUNDARY = (
    "all-slab static phase-anchor component only, conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no branch-tube, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
FORMAL_BRANCH_CHECKER_CLAIM_BOUNDARY = (
    "all-slab distinguished-branch complete-period tube component only; no "
    "static phase-anchor, composite, global-orbit, trace-formula, "
    "Hilbert--Polya, zeta-zero, or RH authority"
)
FORMAL_STATIC_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the formal 102-cell static checker chain only; "
    "no authority beyond PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
)
FORMAL_BRANCH_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once reproduction of the formal 102-cell branch checker chain only; "
    "no authority beyond PASS_BRANCH_TUBE_ALL_SLABS"
)
FORMAL_COMPOSITE_CLAIM_BOUNDARY = (
    "complete-period local-tube candidate uniqueness modulo time translation "
    "and distinguished-branch tube membership only; no global routing, "
    "trace-formula, Hilbert-Polya, zeta-zero, or RH promotion"
)

FORMAL_COMPOSITE_SUMMARY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "matrix", "cell_count_per_component", "component_chains",
    "archive_generation_sha256", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}
FORMAL_COMPOSITE_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_chains", "archive_generation_sha256", "summary",
    "scientific_licensing_enabled", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
FORMAL_COMPOSITE_COMPONENT_CHAIN_KEYS = {
    "aggregate_summary", "aggregate_manifest", "checker", "postcheck",
    "ordered_cell_manifest_root",
}
FORMAL_COMPOSITE_FILE_EDGE_KEYS = {"path", "sha256"}
FORMAL_BRANCH_MANIFEST_KEYS = {
    "artifact_role", "authority", "claim_boundary", "component_status",
    "final_status", "freeze_sha256", "matrix_id", "milestone_status",
    "protocol_id", "run_config_sha256", "schema_version",
    "scientific_licensing_enabled", "theorem_status", "budgets",
    "cell_identity", "files", "task_binding_sha256",
}
FORMAL_BRANCH_RECORD_KEYS = {
    "artifact_role", "authority", "claim_boundary", "component_status",
    "final_status", "freeze_sha256", "matrix_id", "milestone_status",
    "protocol_id", "run_config_sha256", "schema_version",
    "scientific_licensing_enabled", "theorem_status", "bindings",
    "budgets", "cell", "execution_pin", "invocation", "raw",
    "scheduler_result",
}
FORMAL_COMPONENT_CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_aggregate_summary_sha256",
    "component_aggregate_manifest_sha256", "replay_counts",
    "cross_precision", "diagnostics", "failures", "source_bindings",
    "claim_boundary", "milestone_status", "theorem_status", "final_status",
}
FORMAL_COMPONENT_POSTCHECK_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "postcheck_status", "passed", "checker_path", "checker_sha256",
    "main_freeze_sha256", "run_config_sha256", "bound_artifacts",
    "replay_counts", "failures", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}
FORMAL_PRODUCER_PAIR_RECEIPT_KEYS = {
    "publication_status", "authority", "artifact_kind", "candidate_package",
    "summary", "manifest", "archive_generation_sha256",
    "publication_method", "scientific_licensing_enabled",
    "production_authorized", "scientific_dispatch_performed",
    "independent_postpublication_verification_performed",
    "component_status", "milestone_status", "theorem_status", "final_status",
}
FORMAL_RUN_PUBLICATION_RECEIPT_KEYS = {
    "publication_status", "authority", "artifact_role", "candidate_sha256",
    "canonical_path", "canonical_sha256", "publication_method",
    "scientific_licensing_enabled", "production_authorized",
    "scientific_dispatch_performed",
}


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
_CAPTURE_SUBREAPER_LOCK = threading.RLock()


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


class SyntheticMachinePublicationCrash(RuntimeError):
    """Test-only process-crash boundary in machine-freeze publication."""


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
class V2PrivateCandidateImage:
    raw: bytes
    device_id: int
    inode: int
    mode: int
    nlink: int
    size_bytes: int
    mtime_ns: int
    ctime_ns: int
    parent_device_id: int
    parent_inode: int
    parent_mode: int
    parent_nlink: int
    parent_chain: tuple[tuple[str, int, int, int], ...]


@dataclass(frozen=True)
class FormalPrivatePackageFile:
    name: str
    raw: bytes
    device_id: int
    inode: int
    mode: int
    nlink: int
    size_bytes: int
    mtime_ns: int
    ctime_ns: int


@dataclass(frozen=True)
class FormalPrivatePairPackage:
    path: Path
    directory_device_id: int
    directory_inode: int
    directory_mode: int
    directory_nlink: int
    directory_mtime_ns: int
    directory_ctime_ns: int
    parent_chain: tuple[tuple[str, int, int, int], ...]
    files: tuple[FormalPrivatePackageFile, FormalPrivatePackageFile]


@dataclass(frozen=True)
class FormalLiveGenerationImage:
    root_chain: tuple[tuple[str, int, int, int], ...]
    publication_parent: tuple[str, int, int, int, int]
    directories: tuple[
        tuple[str, int, int, int, int, int, int, tuple[str, ...]], ...
    ]
    files: tuple[
        tuple[str, str, int, int, int, int, int, int, int], ...
    ]
    operational_absence: tuple[tuple[str, int, int], ...]


@dataclass(frozen=True)
class FormalCompositeGenerationImage:
    static: FormalLiveGenerationImage
    branch: FormalLiveGenerationImage
    result_parent: tuple[str, int, int, int, int, tuple[str, ...]]
    controls: tuple[
        tuple[str, str, int, int, int, int, int, int, int], ...
    ]


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
    authority_canonical = root / "results/r401_val_l3_a1_v2_all_slabs"
    authority_operational = root / "results/r401_val_l3_a1_v2_all_slabs.operational"
    if is_within(candidate, authority_canonical) or is_within(
        candidate, authority_operational
    ):
        raise PathContractError("formal preflight cannot use authority production namespace")
    if is_within(candidate, root) or is_within(root, candidate):
        raise PathContractError("formal preflight output must not overlap authority inputs")
    return candidate


def _build_formal_run_binding_payload(
    snapshot: FormalAuthoritySnapshot, output: Path
) -> dict[str, Any]:
    main = _validate_formal_main_envelope(
        strict_json_loads(snapshot.main_freeze_raw.decode("utf-8")),
        snapshot.input_roles,
        snapshot.machine_freeze_sha256,
    )
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
            "path": "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json",
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


def build_formal_preflight_binding(
    snapshot: FormalAuthoritySnapshot, output: Path | str
) -> dict[str, Any]:
    """Build the exact final-shaped, non-self-authorizing run binding."""

    candidate = ensure_formal_preflight_output_allowed(
        output, snapshot.authority_root
    )
    return _build_formal_run_binding_payload(snapshot, candidate)


def build_formal_canonical_run_binding(
    snapshot: FormalAuthoritySnapshot,
) -> dict[str, Any]:
    """Build role 55 for its one fixed V2 result root without writing it."""

    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    operational = result.with_name(result.name + ".operational")
    if result != CANONICAL_RESULT and snapshot.authority_root == ROOT:
        raise PathContractError("formal role-55 destination is not the fixed V2 root")
    if path_lexists(result) or path_lexists(operational):
        raise RunBindingMismatch(
            "formal role-55 result/operational destination already exists"
        )
    return _build_formal_run_binding_payload(snapshot, result)


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


def validate_formal_canonical_run_binding(
    binding: Any,
    snapshot: FormalAuthoritySnapshot,
) -> dict[str, Any]:
    """Strictly validate role 55 against the fixed V2 result destination."""

    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    exact_keys(binding, FINAL_RUN_CONFIG_KEYS, "formal canonical run binding")
    exact_int(binding["schema_version"], "formal run schema", minimum=1)
    if (
        binding["schema_version"] != SCHEMA_VERSION
        or binding["protocol_id"] != PROTOCOL_ID
        or binding["artifact_role"] != "RUN_CONFIG"
        or binding["artifact_status"] != "SEALED_CONTROL_PLANE_BINDING"
        or binding["authority"] != "PRODUCER_ONLY"
        or binding["scientific_licensing_enabled"] is not False
        or binding["dispatch_authorized_by_artifact"] is not False
        or binding["freeze_sha256"] != snapshot.main_freeze_sha256
        or binding["main_freeze_sha256"] != snapshot.main_freeze_sha256
        or binding["freeze_sha256"] != binding["main_freeze_sha256"]
        or binding["claim_boundary"] != FORMAL_RUN_CONFIG_CLAIM_BOUNDARY
    ):
        raise ProductionAuthorityError("formal canonical run identity mismatch")
    if not exact_json_equal(binding["matrix"], matrix_payload()) or binding[
        "matrix_id"
    ] != canonical_matrix_id():
        raise ProductionAuthorityError("formal canonical run matrix mismatch")
    expected = _build_formal_run_binding_payload(snapshot, result)
    if not exact_json_equal(binding, expected):
        raise RunBindingMismatch(
            "formal canonical run binding differs from role-54 authority"
        )
    for key in (
        "component_status", "milestone_status", "theorem_status", "final_status"
    ):
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


def build_formal_run_config_candidate(
    snapshot: FormalAuthoritySnapshot,
    output_value: str,
) -> tuple[dict[str, Any], str]:
    """Write a private role-55 candidate; never initialize the result root."""

    revalidate_formal_snapshot(snapshot)
    output = _v2_private_candidate_path(
        output_value, "formal role-55 private candidate"
    )
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    operational = result.with_name(result.name + ".operational")
    absence = _v2_absence_snapshot(
        (result, operational), "formal role-55 build namespace"
    )
    binding = build_formal_canonical_run_binding(snapshot)
    validate_formal_canonical_run_binding(binding, snapshot)
    raw = canonical_json_bytes(binding)
    image: V2PrivateCandidateImage | None = None
    try:
        image = _v2_write_private_candidate(
            output,
            raw,
            maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
            context="formal role-55 private candidate",
        )
        revalidate_formal_snapshot(snapshot)
        _v2_absence_replay(absence, "formal role-55 build namespace")
        _v2_replay_private_candidate(
            output, image, context="formal role-55 candidate terminal replay"
        )
    except BaseException:
        if image is not None:
            _v2_remove_owned_candidate(output, image)
        raise
    return binding, sha256_bytes(raw)


def _formal_run_publication_fault_hook(_phase: str) -> None:
    """Test-only hook; production callers never install a side effect."""


def _formal_run_publication_replay(
    snapshot: FormalAuthoritySnapshot,
    candidate_path: Path,
    candidate_image: V2PrivateCandidateImage,
    expected_raw: bytes,
    *,
    published: bool,
) -> None:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    operational = result.with_name(result.name + ".operational")
    revalidate_formal_snapshot(snapshot)
    _v2_replay_private_candidate(
        candidate_path,
        candidate_image,
        context="formal role-55 publication candidate replay",
    )
    if path_lexists(operational):
        raise CorruptGeneration("formal role-55 operational namespace appeared")
    if not published:
        if path_lexists(result):
            raise CorruptGeneration("formal role-55 result destination appeared")
        return
    result_fd = _open_directory_fd(result)
    try:
        if tuple(os.listdir(result_fd)) != ("run_config.json",):
            raise CorruptGeneration("formal role-55 result root is not exact")
        raw, info = _read_machine_publication_file_at(
            result_fd,
            "run_config.json",
            "formal canonical role-55",
            expected_mode=0o644,
            maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
        )
        if raw != expected_raw:
            raise CorruptGeneration("formal canonical role-55 bytes changed")
        payload = strict_json_loads(raw.decode("utf-8"))
        if raw != canonical_json_bytes(payload):
            raise StrictJSONError("formal canonical role-55 is noncanonical")
        validate_formal_canonical_run_binding(payload, snapshot)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise CorruptGeneration("formal canonical role-55 inode mismatch")
    finally:
        os.close(result_fd)


def _formal_run_stage_replay(
    parent_fd: int,
    stage_fd: int,
    stage_name: str,
    stage_identity: tuple[int, int],
    expected_raw: bytes,
    *,
    context: str,
    expected_image: tuple[
        tuple[int, int, int, int, int, int, int],
        tuple[int, int, int, int, int, int, int],
    ] | None = None,
) -> tuple[
    tuple[int, int, int, int, int, int, int],
    tuple[int, int, int, int, int, int, int],
]:
    pinned = os.fstat(stage_fd)
    lexical = os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
    fingerprint = lambda info: (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )
    if (
        (pinned.st_dev, pinned.st_ino) != stage_identity
        or fingerprint(lexical) != fingerprint(pinned)
        or not stat.S_ISDIR(pinned.st_mode)
        or stat.S_IMODE(pinned.st_mode) != 0o755
        or pinned.st_nlink != 2
        or tuple(os.listdir(stage_fd)) != ("run_config.json",)
    ):
        raise PathContractError(f"{context} directory identity mismatch")
    raw, file_info = _read_machine_publication_file_at(
        stage_fd,
        "run_config.json",
        f"{context} run config",
        expected_mode=0o644,
        maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
    )
    if raw != expected_raw:
        raise CorruptGeneration(f"{context} run-config bytes mismatch")
    image = (fingerprint(pinned), _machine_publication_file_identity(file_info))
    if expected_image is not None and image != expected_image:
        raise PathContractError(f"{context} full stage image drift")
    return image


def _formal_run_published_directory_replay(
    result: Path,
    parent_fd: int,
    pinned_directory_fd: int,
    stage_identity: tuple[int, int],
    expected_raw: bytes,
    *,
    context: str,
    expected_image: tuple[
        tuple[int, int, int, int, int, int, int],
        tuple[int, int, int, int, int, int, int],
    ] | None = None,
) -> tuple[
    tuple[int, int, int, int, int, int, int],
    tuple[int, int, int, int, int, int, int],
]:
    pinned = os.fstat(pinned_directory_fd)
    lexical = os.stat(result.name, dir_fd=parent_fd, follow_symlinks=False)
    reopened_fd = _open_directory_fd(result)
    try:
        reopened = os.fstat(reopened_fd)
        fingerprint = lambda info: (
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            info.st_size,
            info.st_mtime_ns,
            info.st_ctime_ns,
        )
        if (
            (pinned.st_dev, pinned.st_ino) != stage_identity
            or fingerprint(lexical) != fingerprint(pinned)
            or fingerprint(reopened) != fingerprint(pinned)
            or not stat.S_ISDIR(pinned.st_mode)
            or stat.S_IMODE(pinned.st_mode) != 0o755
            or pinned.st_nlink != 2
            or tuple(os.listdir(pinned_directory_fd)) != ("run_config.json",)
            or tuple(os.listdir(reopened_fd)) != ("run_config.json",)
        ):
            raise PathContractError(f"{context} directory identity mismatch")
        pinned_raw, pinned_file = _read_machine_publication_file_at(
            pinned_directory_fd,
            "run_config.json",
            f"{context} pinned config",
            expected_mode=0o644,
            maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
        )
        reopened_raw, reopened_file = _read_machine_publication_file_at(
            reopened_fd,
            "run_config.json",
            f"{context} lexical config",
            expected_mode=0o644,
            maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
        )
        if (
            pinned_raw != expected_raw
            or reopened_raw != expected_raw
            or _machine_publication_file_identity(pinned_file)
            != _machine_publication_file_identity(reopened_file)
        ):
            raise CorruptGeneration(f"{context} run-config image mismatch")
        image = (
            fingerprint(pinned),
            _machine_publication_file_identity(pinned_file),
        )
        if expected_image is not None and image != expected_image:
            raise PathContractError(f"{context} full published image drift")
        return image
    finally:
        os.close(reopened_fd)


def publish_formal_run_config(
    snapshot: FormalAuthoritySnapshot,
    candidate_value: str,
    expected_sha256: str,
    *,
    publication_authority: str,
    _fail_at: str | None = None,
) -> dict[str, Any]:
    """Atomically initialize the exact role-55 root without dispatching."""

    if publication_authority != FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY:
        raise ProductionAuthorityError("formal role-55 publisher authority mismatch")
    expected_sha256 = _exact_sha(expected_sha256, "formal role-55 expected SHA-256")
    candidate_path = _v2_private_candidate_path(
        candidate_value, "formal role-55 publication candidate"
    )
    candidate_image = _v2_snapshot_private_candidate(
        candidate_path,
        maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
        context="formal role-55 publication candidate",
    )
    if sha256_bytes(candidate_image.raw) != expected_sha256:
        raise ProductionAuthorityError("formal role-55 candidate digest mismatch")
    try:
        payload = strict_json_loads(candidate_image.raw.decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("formal role-55 candidate is not UTF-8") from error
    if candidate_image.raw != canonical_json_bytes(payload):
        raise StrictJSONError("formal role-55 candidate is not CJ_COMPACT_V1")
    validate_formal_canonical_run_binding(payload, snapshot)

    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    results_parent = result.parent
    parent_chain = _machine_publication_directory_chain(results_parent)
    parent_fd = _open_directory_fd(results_parent)
    stage_fd: int | None = None
    stage_name: str | None = None
    stage_identity: tuple[int, int] | None = None
    stage_created = False
    config_identity: tuple[int, int] | None = None
    stage_full_image: tuple[
        tuple[int, int, int, int, int, int, int],
        tuple[int, int, int, int, int, int, int],
    ] | None = None
    published_full_image: tuple[
        tuple[int, int, int, int, int, int, int],
        tuple[int, int, int, int, int, int, int],
    ] | None = None
    renamed = False
    locked = False
    primary_error: BaseException | None = None
    cleanup_error: BaseException | None = None

    def replay_reserved_stages(expected_names: frozenset[str], context: str) -> None:
        prefix = f".{result.name}.role55-publish-"
        observed = {
            name for name in os.listdir(parent_fd) if name.startswith(prefix)
        }
        if observed != set(expected_names):
            raise CorruptGeneration(
                f"{context} role-55 reserved staging namespace mismatch"
            )

    try:
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError("formal role-55 destination parent is locked") from error
        locked = True
        _replay_machine_publication_directory(
            results_parent,
            parent_fd,
            parent_chain,
            "formal role-55 publication parent",
        )
        _formal_run_publication_replay(
            snapshot,
            candidate_path,
            candidate_image,
            candidate_image.raw,
            published=False,
        )
        replay_reserved_stages(frozenset(), "formal role-55 initial")
        stage_name = (
            f".{result.name}.role55-publish-{os.urandom(16).hex()}"
        )
        os.mkdir(stage_name, 0o700, dir_fd=parent_fd)
        stage_created = True
        try:
            stage_fd = os.open(
                stage_name,
                os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
                | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=parent_fd,
            )
        except BaseException:
            # A single open fault still leaves an O_EXCL-created empty
            # directory.  Capture its lexical identity so the outer cleanup
            # can reopen and remove only that same inode.
            recovered_stage = os.stat(
                stage_name, dir_fd=parent_fd, follow_symlinks=False
            )
            if not stat.S_ISDIR(recovered_stage.st_mode):
                raise PathContractError(
                    "formal role-55 created stage became non-directory"
                )
            stage_identity = (
                recovered_stage.st_dev,
                recovered_stage.st_ino,
            )
            raise
        try:
            stage_info = os.fstat(stage_fd)
        except BaseException as error:
            try:
                recovered_stage = os.fstat(stage_fd)
                if not stat.S_ISDIR(recovered_stage.st_mode):
                    raise PathContractError(
                        "formal role-55 opened stage became non-directory"
                    )
                stage_identity = (
                    recovered_stage.st_dev,
                    recovered_stage.st_ino,
                )
            except BaseException:
                raise PathContractError(
                    "formal role-55 could not recover opened stage identity"
                ) from error
            raise
        stage_identity = (stage_info.st_dev, stage_info.st_ino)
        os.fchmod(stage_fd, 0o755)
        stage_info = os.fstat(stage_fd)
        lexical_stage = os.stat(
            stage_name, dir_fd=parent_fd, follow_symlinks=False
        )
        if (
            (stage_info.st_dev, stage_info.st_ino) != stage_identity
            or _machine_publication_file_identity(stage_info)
            != _machine_publication_file_identity(lexical_stage)
            or not stat.S_ISDIR(stage_info.st_mode)
            or stat.S_IMODE(stage_info.st_mode) != 0o755
            or stage_info.st_nlink != 2
        ):
            raise PathContractError("formal role-55 staging directory mismatch")
        config_fd = os.open(
            "run_config.json",
            os.O_RDWR | os.O_CREAT | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            0o644,
            dir_fd=stage_fd,
        )
        try:
            created_config = os.fstat(config_fd)
            config_identity = (created_config.st_dev, created_config.st_ino)
            os.fchmod(config_fd, 0o644)
            _write_machine_publication_bytes(config_fd, candidate_image.raw)
            os.fsync(config_fd)
        except BaseException as error:
            if config_identity is None:
                try:
                    recovered_config = os.fstat(config_fd)
                    if (
                        not stat.S_ISREG(recovered_config.st_mode)
                        or recovered_config.st_nlink != 1
                    ):
                        raise PathContractError(
                            "formal role-55 staged config identity is unrecoverable"
                        )
                    config_identity = (
                        recovered_config.st_dev,
                        recovered_config.st_ino,
                    )
                except BaseException as recovery_error:
                    raise PathContractError(
                        "formal role-55 could not recover staged config identity"
                    ) from error
            raise
        finally:
            os.close(config_fd)
        staged_raw, _ = _read_machine_publication_file_at(
            stage_fd,
            "run_config.json",
            "formal role-55 staged config",
            expected_mode=0o644,
            maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
        )
        if staged_raw != candidate_image.raw:
            raise CorruptGeneration("formal role-55 staged bytes mismatch")
        os.fsync(stage_fd)
        os.fsync(parent_fd)
        stage_full_image = _formal_run_stage_replay(
            parent_fd,
            stage_fd,
            stage_name,
            stage_identity,
            candidate_image.raw,
            context="formal role-55 frozen prehook stage",
        )
        _formal_run_publication_fault_hook("BEFORE_RENAME")
        if _fail_at == "BEFORE_RENAME":
            raise SyntheticCrash("formal role-55 crash before rename")
        _formal_run_publication_replay(
            snapshot,
            candidate_path,
            candidate_image,
            candidate_image.raw,
            published=False,
        )
        _formal_run_stage_replay(
            parent_fd,
            stage_fd,
            stage_name,
            stage_identity,
            candidate_image.raw,
            context="formal role-55 immediate pre-rename stage",
            expected_image=stage_full_image,
        )
        assert stage_name is not None
        replay_reserved_stages(
            frozenset({stage_name}), "formal role-55 immediate pre-rename"
        )
        _replay_machine_publication_directory(
            results_parent,
            parent_fd,
            parent_chain,
            "formal role-55 immediate pre-rename parent",
        )
        _rename_machine_publication_noreplace(parent_fd, stage_name, result.name)
        renamed = True
        os.fsync(parent_fd)
        published_full_image = _formal_run_published_directory_replay(
            result,
            parent_fd,
            stage_fd,
            stage_identity,
            candidate_image.raw,
            context="formal role-55 immediate post-rename",
        )
        replay_reserved_stages(
            frozenset(), "formal role-55 immediate post-rename"
        )
        _formal_run_publication_fault_hook("AFTER_RENAME")
        if _fail_at == "AFTER_RENAME":
            raise SyntheticCrash("formal role-55 crash after rename")
        _formal_run_publication_replay(
            snapshot,
            candidate_path,
            candidate_image,
            candidate_image.raw,
            published=True,
        )
        _formal_run_published_directory_replay(
            result,
            parent_fd,
            stage_fd,
            stage_identity,
            candidate_image.raw,
            context="formal role-55 ultimate published replay",
            expected_image=published_full_image,
        )
        _replay_machine_publication_directory(
            results_parent,
            parent_fd,
            parent_chain,
            "formal role-55 terminal publication parent",
        )
        replay_reserved_stages(frozenset(), "formal role-55 terminal")
        receipt = {
            "publication_status": "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY",
            "authority": FORMAL_RUN_CONFIG_PUBLICATION_AUTHORITY,
            "artifact_role": "RUN_CONFIG_PUBLICATION_RECEIPT",
            "candidate_sha256": expected_sha256,
            "canonical_path": result.relative_to(snapshot.authority_root).as_posix()
            + "/run_config.json",
            "canonical_sha256": expected_sha256,
            "publication_method": FORMAL_PRODUCER_PUBLICATION_METHOD,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
        }
        exact_keys(
            receipt,
            FORMAL_RUN_PUBLICATION_RECEIPT_KEYS,
            "formal role-55 publication receipt",
        )
        receipt_raw = canonical_json_bytes(receipt)
        if not exact_json_equal(
            strict_json_loads(receipt_raw.decode("utf-8")), receipt
        ):
            raise StrictJSONError("formal role-55 receipt canonicalization mismatch")
        # Receipt construction is not a terminal observation.  Replay the
        # complete envelope once more and leave the lexical parent replay as
        # the final filesystem operation before returning the in-memory map.
        _formal_run_publication_replay(
            snapshot,
            candidate_path,
            candidate_image,
            candidate_image.raw,
            published=True,
        )
        _formal_run_published_directory_replay(
            result,
            parent_fd,
            stage_fd,
            stage_identity,
            candidate_image.raw,
            context="formal role-55 post-receipt ultimate replay",
            expected_image=published_full_image,
        )
        _replay_machine_publication_directory(
            results_parent,
            parent_fd,
            parent_chain,
            "formal role-55 post-receipt terminal parent",
        )
        replay_reserved_stages(
            frozenset(), "formal role-55 post-receipt terminal"
        )
        return receipt
    except BaseException as error:
        primary_error = error
        raise
    finally:
        if not renamed and stage_created and stage_name is not None:
            cleanup_stage_fd: int | None = None
            cleanup_stage_fd_is_temporary = False
            try:
                current = os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
                if stage_identity is None or (
                    current.st_dev,
                    current.st_ino,
                ) != stage_identity:
                    raise PathContractError(
                        "formal role-55 refused to clean substituted staging directory"
                    )
                if stage_fd is None:
                    cleanup_stage_fd = os.open(
                        stage_name,
                        os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
                        | getattr(os, "O_NOFOLLOW", 0),
                        dir_fd=parent_fd,
                    )
                    cleanup_stage_fd_is_temporary = True
                else:
                    cleanup_stage_fd = stage_fd
                pinned_cleanup = os.fstat(cleanup_stage_fd)
                if (
                    not stat.S_ISDIR(pinned_cleanup.st_mode)
                    or (pinned_cleanup.st_dev, pinned_cleanup.st_ino)
                    != stage_identity
                ):
                    raise PathContractError(
                        "formal role-55 cleanup stage fd is not the owned inode"
                    )
                try:
                    config_entry = os.stat(
                        "run_config.json",
                        dir_fd=cleanup_stage_fd,
                        follow_symlinks=False,
                    )
                except FileNotFoundError:
                    if tuple(os.listdir(cleanup_stage_fd)) != ():
                        raise PathContractError(
                            "formal role-55 staging cleanup found foreign entries"
                        )
                else:
                    if (
                        config_identity is None
                        or (config_entry.st_dev, config_entry.st_ino)
                        != config_identity
                        or tuple(os.listdir(cleanup_stage_fd))
                        != ("run_config.json",)
                    ):
                        raise PathContractError(
                            "formal role-55 refused substituted staged config cleanup"
                        )
                    os.unlink("run_config.json", dir_fd=cleanup_stage_fd)
                os.fsync(cleanup_stage_fd)
                if tuple(os.listdir(cleanup_stage_fd)) != ():
                    raise PathContractError(
                        "formal role-55 staging directory is nonempty after cleanup"
                    )
                immediate = os.stat(
                    stage_name, dir_fd=parent_fd, follow_symlinks=False
                )
                if (immediate.st_dev, immediate.st_ino) != stage_identity:
                    raise PathContractError(
                        "formal role-55 staging directory swapped before rmdir"
                    )
                os.rmdir(stage_name, dir_fd=parent_fd)
                os.fsync(parent_fd)
            except FileNotFoundError:
                pass
            except BaseException as error:
                cleanup_error = cleanup_error or error
            finally:
                if cleanup_stage_fd_is_temporary and cleanup_stage_fd is not None:
                    try:
                        os.close(cleanup_stage_fd)
                    except BaseException as error:
                        cleanup_error = cleanup_error or error
        for cleanup in (
            (lambda: os.close(stage_fd)) if stage_fd is not None else None,
            (lambda: fcntl.flock(parent_fd, fcntl.LOCK_UN)) if locked else None,
            lambda: os.close(parent_fd),
        ):
            if cleanup is None:
                continue
            try:
                cleanup()
            except BaseException as error:
                cleanup_error = cleanup_error or error
        if cleanup_error is not None:
            if primary_error is not None:
                raise PathContractError(
                    "formal role-55 transaction failed with incomplete cleanup: "
                    f"{type(cleanup_error).__name__}: {cleanup_error}"
                ) from primary_error
            raise cleanup_error


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


def validate_v2_role5_payload(
    payload: Any,
    role_records: Mapping[str, FormalRoleRecord] | None = None,
) -> dict[str, Any]:
    """Validate the closed V2 design-review/withdrawal object.

    Repository and Git-tree replay are deliberately separate below so unit
    fixtures can exercise the exact byte-domain schema without pretending to
    have canonical legacy history.
    """

    exact_keys(payload, V2_ROLE5_KEYS, "V2 role 5")
    expected_scalars = {
        "schema_version": 1,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL",
        "status": "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1",
        "authority": "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "claim_boundary": V2_ROLE5_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    for key, expected in expected_scalars.items():
        if not exact_json_equal(payload[key], expected):
            raise ProductionAuthorityError(f"V2 role 5 scalar mismatch: {key}")

    legacy = payload["legacy_attempt"]
    exact_keys(legacy, V2_ROLE5_LEGACY_KEYS, "V2 role 5 legacy_attempt")
    if (
        legacy["attempt_id"] != "A416_L3_A1_CONTROL_ATTEMPT_1"
        or legacy["status"] != "WITHDRAWN_NON_LICENSING"
        or legacy["terminal_commit"]
        != "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0"
        or legacy["supersession_rule"] != V2_ROLE5_SUPERSESSION_RULE
    ):
        raise ProductionAuthorityError("V2 role 5 legacy scalar mismatch")
    if not exact_json_equal(
        legacy["published_artifacts"], list(V2_ROLE5_LEGACY_ARTIFACTS)
    ):
        raise ProductionAuthorityError("V2 role 5 legacy publication map mismatch")
    for index, item in enumerate(legacy["published_artifacts"]):
        exact_keys(item, V2_ROLE5_PUBLISHED_KEYS, f"V2 role 5 legacy artifact {index}")
        if type(item["role"]) is not int:
            raise ProductionAuthorityError("V2 role 5 legacy role must be an integer")
        safe_relative_path(item["path"])
    if not exact_json_equal(legacy["defects"], list(V2_ROLE5_DEFECTS)):
        raise ProductionAuthorityError("V2 role 5 exact defect array mismatch")
    for index, item in enumerate(legacy["defects"]):
        exact_keys(item, V2_ROLE5_DEFECT_KEYS, f"V2 role 5 defect {index}")

    reviewed = payload["reviewed_v2_inputs"]
    if type(reviewed) is not list or len(reviewed) != len(V2_ROLE5_REVIEWED_ROLES):
        raise ProductionAuthorityError("V2 role 5 reviewed input count mismatch")
    role_paths = dict(FORMAL_INPUT_ROLES)
    seen_paths: set[str] = set()
    for index, (expected_role, item) in enumerate(
        zip(V2_ROLE5_REVIEWED_ROLES, reviewed)
    ):
        exact_keys(item, V2_ROLE5_REVIEWED_KEYS, f"V2 role 5 reviewed input {index}")
        expected_path = role_paths[expected_role]
        if (
            item["role"] != expected_role
            or item["path"] != expected_path
            or type(item["sha256"]) is not str
            or HEX_SHA256.fullmatch(item["sha256"]) is None
            or item["path"] in seen_paths
        ):
            raise ProductionAuthorityError("V2 role 5 reviewed input mismatch")
        seen_paths.add(item["path"])
        if role_records is not None:
            record = role_records.get(expected_role)
            if (
                record is None
                or record.path != expected_path
                or record.sha256 != item["sha256"]
            ):
                raise ProductionAuthorityError(
                    f"V2 role 5 stale reviewed input: {expected_role}"
                )

    review = payload["review"]
    exact_keys(review, V2_ROLE5_REVIEW_KEYS, "V2 role 5 review")
    if (
        review["reviewer_independent_of_attempt1_author"] is not True
        or review["verdict"] != "ACCEPT_CONTROL_PLANE_V2_DESIGN"
        or any(type(review[key]) is not int or review[key] != 0 for key in (
            "p0_count", "p1_count", "p2_count"
        ))
        or type(review["reviewed_commit"]) is not str
        or re.fullmatch(r"[0-9a-f]{40}", review["reviewed_commit"]) is None
        or review["map_matches_contract"] is not True
        or review["legacy_bytes_unchanged"] is not True
        or review["scientific_protocol_unchanged"] is not True
    ):
        raise ProductionAuthorityError("V2 role 5 independent review gate mismatch")
    return dict(payload)


def _v2_git_sha1(raw: bytes) -> str:
    return hashlib.sha1(raw, usedforsecurity=False).hexdigest()


def _v2_git_roots(project_root: Path) -> tuple[Path, Path, PurePosixPath]:
    """Find one enclosing ordinary ``.git`` directory without a child process."""

    root = safe_absolute_path(os.fspath(project_root), "V2 Git project root")
    candidate = root
    while True:
        marker = candidate / ".git"
        try:
            info = os.stat(marker, follow_symlinks=False)
        except FileNotFoundError:
            if candidate.parent == candidate:
                raise ProductionAuthorityError(
                    "V2 authority root is not inside an ordinary Git repository"
                )
            candidate = candidate.parent
            continue
        if not stat.S_ISDIR(info.st_mode):
            raise ProductionAuthorityError(
                "Git indirection files and symlinked Git directories are rejected"
            )
        relative = root.relative_to(candidate)
        prefix = (
            PurePosixPath(relative.as_posix())
            if relative.parts
            else PurePosixPath()
        )
        return candidate, marker, prefix


def _v2_git_snapshot(path: Path, maximum_bytes: int) -> bytes:
    """Bounded pinned Git-object read; FIFO/device swaps cannot block."""

    canonical = safe_absolute_path(os.fspath(path), "V2 Git object path")
    try:
        parent_fd = _open_directory_fd(canonical.parent)
    except OSError as error:
        raise ProductionAuthorityError(
            f"Git object parent open failed: {canonical}"
        ) from error
    descriptor: int | None = None
    parent_before = os.fstat(parent_fd)
    try:
        try:
            before = os.stat(
                canonical.name, dir_fd=parent_fd, follow_symlinks=False
            )
        except FileNotFoundError:
            raise
        except OSError as error:
            raise ProductionAuthorityError(
                f"Git object stat failed: {canonical}"
            ) from error
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_nlink != 1
            or before.st_size < 0
            or before.st_size > maximum_bytes
        ):
            raise ProductionAuthorityError(
                f"unsafe or oversize Git object: {canonical}"
            )
        flags = (
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0)
        )
        try:
            descriptor = os.open(canonical.name, flags, dir_fd=parent_fd)
        except OSError as error:
            raise ProductionAuthorityError(
                f"Git object nonblocking open failed: {canonical}"
            ) from error
        opened = os.fstat(descriptor)
        fingerprint = lambda info: (
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            info.st_size,
            info.st_mtime_ns,
            info.st_ctime_ns,
        )
        if (
            not stat.S_ISREG(opened.st_mode)
            or opened.st_nlink != 1
            or fingerprint(opened) != fingerprint(before)
        ):
            raise ProductionAuthorityError(
                f"Git object path/inode race: {canonical}"
            )
        chunks: list[bytes] = []
        offset = 0
        while True:
            try:
                chunk = os.pread(
                    descriptor,
                    min(1024 * 1024, maximum_bytes + 1 - offset),
                    offset,
                )
            except OSError as error:
                raise ProductionAuthorityError(
                    f"Git object bounded read failed: {canonical}"
                ) from error
            if not chunk:
                break
            chunks.append(chunk)
            offset += len(chunk)
            if offset > maximum_bytes:
                raise ProductionAuthorityError(
                    f"Git object grew beyond read cap: {canonical}"
                )
        raw = b"".join(chunks)
        after = os.fstat(descriptor)
        lexical_after = os.stat(
            canonical.name, dir_fd=parent_fd, follow_symlinks=False
        )
        if (
            len(raw) != before.st_size
            or fingerprint(after) != fingerprint(before)
            or fingerprint(lexical_after) != fingerprint(before)
        ):
            raise ProductionAuthorityError(
                f"Git object changed during bounded read: {canonical}"
            )
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
                or fingerprint(replay_entry) != fingerprint(before)
            ):
                raise ProductionAuthorityError(
                    f"Git object terminal lexical replay failed: {canonical}"
                )
        finally:
            os.close(replay_parent_fd)
        return raw
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def _v2_git_inflate(
    raw: bytes,
    context: str,
    *,
    cap: int = 1024 * 1024 * 1024,
) -> bytes:
    inflater = zlib.decompressobj()
    try:
        value = inflater.decompress(raw, cap + 1)
    except zlib.error as error:
        raise ProductionAuthorityError(f"{context}: malformed zlib stream") from error
    if not inflater.eof or inflater.unconsumed_tail or len(value) > cap:
        raise ProductionAuthorityError(f"{context}: incomplete or oversize zlib stream")
    return value


def _v2_git_parse_framed(
    framed: bytes, oid: str, context: str
) -> tuple[str, bytes]:
    if _v2_git_sha1(framed) != oid:
        raise ProductionAuthorityError(f"{context}: Git object ID mismatch")
    try:
        header, payload = framed.split(b"\x00", 1)
        kind_raw, size_raw = header.split(b" ", 1)
        kind = kind_raw.decode("ascii")
        size = int(size_raw.decode("ascii"))
    except (ValueError, UnicodeError) as error:
        raise ProductionAuthorityError(
            f"{context}: malformed Git loose-object frame"
        ) from error
    if (
        kind not in {"commit", "tree", "blob", "tag"}
        or str(size).encode() != size_raw
        or size != len(payload)
    ):
        raise ProductionAuthorityError(f"{context}: Git object kind/size mismatch")
    return kind, payload


def _v2_git_pack_index(
    index_raw: bytes, context: str
) -> tuple[dict[str, int], bytes]:
    if (
        len(index_raw) < 8 + 256 * 4 + 40
        or index_raw[:4] != b"\xfftOc"
        or struct.unpack_from(">I", index_raw, 4)[0] != 2
        or hashlib.sha1(
            index_raw[:-20], usedforsecurity=False
        ).digest() != index_raw[-20:]
    ):
        raise ProductionAuthorityError(f"{context}: invalid v2 pack index/checksum")
    fanout = struct.unpack_from(">256I", index_raw, 8)
    if any(left > right for left, right in zip(fanout, fanout[1:])):
        raise ProductionAuthorityError(f"{context}: unordered pack fanout")
    count = fanout[-1]
    names_offset = 8 + 256 * 4
    crc_offset = names_offset + count * 20
    offsets_offset = crc_offset + count * 4
    large_offset = offsets_offset + count * 4
    if large_offset + 40 > len(index_raw):
        raise ProductionAuthorityError(f"{context}: truncated pack index")
    result: dict[str, int] = {}
    previous: bytes | None = None
    for index in range(count):
        raw_oid = index_raw[
            names_offset + 20 * index:names_offset + 20 * (index + 1)
        ]
        if len(raw_oid) != 20 or (previous is not None and raw_oid <= previous):
            raise ProductionAuthorityError(
                f"{context}: unordered/duplicate object IDs"
            )
        previous = raw_oid
        offset = struct.unpack_from(">I", index_raw, offsets_offset + 4 * index)[0]
        if offset & 0x80000000:
            location = large_offset + 8 * (offset & 0x7fffffff)
            if location + 8 > len(index_raw) - 40:
                raise ProductionAuthorityError(
                    f"{context}: malformed large pack offset"
                )
            offset = struct.unpack_from(">Q", index_raw, location)[0]
        result[raw_oid.hex()] = offset
    return result, index_raw[-40:-20]


def _v2_git_delta_varint(
    raw: bytes, cursor: int, context: str
) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        if cursor >= len(raw) or shift > 63:
            raise ProductionAuthorityError(f"{context}: malformed delta varint")
        current = raw[cursor]
        cursor += 1
        value |= (current & 0x7f) << shift
        if not current & 0x80:
            return value, cursor
        shift += 7


def _v2_git_apply_delta(base: bytes, delta: bytes, context: str) -> bytes:
    base_size, cursor = _v2_git_delta_varint(delta, 0, context)
    output_size, cursor = _v2_git_delta_varint(delta, cursor, context)
    if base_size != len(base) or output_size > 1024 * 1024 * 1024:
        raise ProductionAuthorityError(f"{context}: delta base/output size mismatch")
    output = bytearray()
    while cursor < len(delta):
        opcode = delta[cursor]
        cursor += 1
        if opcode & 0x80:
            offset = 0
            size = 0
            for bit, shift in ((0x01, 0), (0x02, 8), (0x04, 16), (0x08, 24)):
                if opcode & bit:
                    if cursor >= len(delta):
                        raise ProductionAuthorityError(
                            f"{context}: truncated delta copy offset"
                        )
                    offset |= delta[cursor] << shift
                    cursor += 1
            for bit, shift in ((0x10, 0), (0x20, 8), (0x40, 16)):
                if opcode & bit:
                    if cursor >= len(delta):
                        raise ProductionAuthorityError(
                            f"{context}: truncated delta copy size"
                        )
                    size |= delta[cursor] << shift
                    cursor += 1
            if size == 0:
                size = 0x10000
            if offset + size > len(base) or len(output) + size > output_size:
                raise ProductionAuthorityError(f"{context}: delta copy exceeds bounds")
            output.extend(base[offset:offset + size])
        else:
            if (
                opcode == 0
                or cursor + opcode > len(delta)
                or len(output) + opcode > output_size
            ):
                raise ProductionAuthorityError(f"{context}: malformed delta literal")
            output.extend(delta[cursor:cursor + opcode])
            cursor += opcode
    if len(output) != output_size:
        raise ProductionAuthorityError(f"{context}: reconstructed delta size mismatch")
    return bytes(output)


def _v2_git_unpack_at(
    pack_raw: bytes,
    offset: int,
    *,
    load_oid: Any,
    memo: dict[int, tuple[str, bytes]],
    active: set[int],
    context: str,
) -> tuple[str, bytes]:
    cached = memo.get(offset)
    if cached is not None:
        return cached
    if offset in active or not (12 <= offset < len(pack_raw) - 20):
        raise ProductionAuthorityError(f"{context}: cyclic/out-of-range packed object")
    active.add(offset)
    try:
        cursor = offset
        current = pack_raw[cursor]
        cursor += 1
        object_type = (current >> 4) & 7
        declared_size = current & 0x0f
        shift = 4
        while current & 0x80:
            if cursor >= len(pack_raw) - 20 or shift > 60:
                raise ProductionAuthorityError(
                    f"{context}: malformed packed-object header"
                )
            current = pack_raw[cursor]
            cursor += 1
            declared_size |= (current & 0x7f) << shift
            shift += 7
        if object_type in (1, 2, 3, 4):
            data = _v2_git_inflate(pack_raw[cursor:-20], context)
            if len(data) != declared_size:
                raise ProductionAuthorityError(
                    f"{context}: packed-object size mismatch"
                )
            kind = {1: "commit", 2: "tree", 3: "blob", 4: "tag"}[object_type]
            result = (kind, data)
        elif object_type == 6:
            if cursor >= len(pack_raw) - 20:
                raise ProductionAuthorityError(f"{context}: truncated OFS delta")
            current = pack_raw[cursor]
            cursor += 1
            distance = current & 0x7f
            while current & 0x80:
                if cursor >= len(pack_raw) - 20:
                    raise ProductionAuthorityError(
                        f"{context}: truncated OFS delta base"
                    )
                current = pack_raw[cursor]
                cursor += 1
                distance = ((distance + 1) << 7) | (current & 0x7f)
            base_kind, base_data = _v2_git_unpack_at(
                pack_raw,
                offset - distance,
                load_oid=load_oid,
                memo=memo,
                active=active,
                context=context,
            )
            delta = _v2_git_inflate(pack_raw[cursor:-20], context)
            if len(delta) != declared_size:
                raise ProductionAuthorityError(
                    f"{context}: OFS delta instruction size mismatch"
                )
            result = (base_kind, _v2_git_apply_delta(base_data, delta, context))
        elif object_type == 7:
            if cursor + 20 > len(pack_raw) - 20:
                raise ProductionAuthorityError(f"{context}: truncated REF delta")
            base_oid = pack_raw[cursor:cursor + 20].hex()
            cursor += 20
            base_kind, base_data = load_oid(base_oid)
            delta = _v2_git_inflate(pack_raw[cursor:-20], context)
            if len(delta) != declared_size:
                raise ProductionAuthorityError(
                    f"{context}: REF delta instruction size mismatch"
                )
            result = (base_kind, _v2_git_apply_delta(base_data, delta, context))
        else:
            raise ProductionAuthorityError(f"{context}: reserved packed-object type")
        memo[offset] = result
        return result
    finally:
        active.remove(offset)


def _v2_git_read_object(project_root: Path, oid: str) -> tuple[str, bytes]:
    if type(oid) is not str or V2_ROLE11_GIT_OID.fullmatch(oid) is None:
        raise ProductionAuthorityError("Git object ID must be lowercase SHA-1")
    _repository_root, git_dir, _prefix = _v2_git_roots(project_root)
    matches: list[tuple[str, bytes]] = []
    loose = git_dir / "objects" / oid[:2] / oid[2:]
    try:
        loose_raw = _v2_git_snapshot(loose, 1024 * 1024 * 1024)
    except FileNotFoundError:
        pass
    else:
        framed = _v2_git_inflate(loose_raw, f"loose Git object {oid}")
        matches.append(
            _v2_git_parse_framed(framed, oid, f"loose Git object {oid}")
        )
    pack_dir = git_dir / "objects" / "pack"
    try:
        first_names = tuple(sorted(
            entry.name for entry in os.scandir(pack_dir)
            if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name)
        ))
    except FileNotFoundError:
        first_names = ()
    for index_name in first_names:
        index_raw = _v2_git_snapshot(
            pack_dir / index_name, 128 * 1024 * 1024
        )
        offsets, pack_checksum = _v2_git_pack_index(
            index_raw, f"Git pack index {index_name}"
        )
        if oid not in offsets:
            continue
        pack_path = pack_dir / f"{index_name[:-4]}.pack"
        pack_raw = _v2_git_snapshot(pack_path, 1024 * 1024 * 1024)
        if (
            len(pack_raw) < 32
            or pack_raw[:4] != b"PACK"
            or struct.unpack_from(">I", pack_raw, 4)[0] not in (2, 3)
            or hashlib.sha1(
                pack_raw[:-20], usedforsecurity=False
            ).digest() != pack_raw[-20:]
            or pack_raw[-20:] != pack_checksum
        ):
            raise ProductionAuthorityError(
                f"Git pack {pack_path.name}: header/checksum mismatch"
            )
        memo: dict[int, tuple[str, bytes]] = {}

        def load_base(base_oid: str) -> tuple[str, bytes]:
            if base_oid in offsets:
                return _v2_git_unpack_at(
                    pack_raw,
                    offsets[base_oid],
                    load_oid=load_base,
                    memo=memo,
                    active=set(),
                    context=f"Git pack {pack_path.name}",
                )
            return _v2_git_read_object(project_root, base_oid)

        kind, data = _v2_git_unpack_at(
            pack_raw,
            offsets[oid],
            load_oid=load_base,
            memo=memo,
            active=set(),
            context=f"Git pack {pack_path.name}",
        )
        framed = kind.encode() + b" " + str(len(data)).encode() + b"\x00" + data
        if _v2_git_sha1(framed) != oid:
            raise ProductionAuthorityError(
                f"Git packed object {oid}: reconstructed ID mismatch"
            )
        matches.append((kind, data))
    try:
        second_names = tuple(sorted(
            entry.name for entry in os.scandir(pack_dir)
            if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name)
        ))
    except FileNotFoundError:
        second_names = ()
    if (
        second_names != first_names
        or not matches
        or any(match != matches[0] for match in matches[1:])
    ):
        raise ProductionAuthorityError(
            f"Git object {oid} is missing, ambiguous, or pack namespace changed"
        )
    return matches[0]


def _v2_git_commit_metadata(
    project_root: Path, commit_oid: str
) -> tuple[str, tuple[str, ...]]:
    """Parse one ordinary commit's closed header grammar from object bytes."""

    kind, payload = _v2_git_read_object(project_root, commit_oid)
    if kind != "commit":
        raise ProductionAuthorityError("reviewed Git OID is not a commit")
    separator = payload.find(b"\n\n")
    if separator < 0:
        raise ProductionAuthorityError("reviewed Git commit lacks header terminator")
    header_raw = payload[:separator]
    if b"\x00" in header_raw or b"\r" in header_raw:
        raise ProductionAuthorityError("reviewed Git commit header has control syntax")
    headers = header_raw.split(b"\n")
    if any(not header or header.startswith(b" ") for header in headers):
        raise ProductionAuthorityError(
            "reviewed Git commit has empty/continued header syntax"
        )
    tree_match = re.fullmatch(rb"tree ([0-9a-f]{40})", headers[0])
    if tree_match is None:
        raise ProductionAuthorityError("reviewed Git commit lacks canonical tree header")
    cursor = 1
    parents: list[str] = []
    while cursor < len(headers):
        parent = re.fullmatch(rb"parent ([0-9a-f]{40})", headers[cursor])
        if parent is None:
            break
        oid = parent.group(1).decode("ascii")
        if oid in parents:
            raise ProductionAuthorityError("reviewed Git commit repeats a parent")
        parents.append(oid)
        cursor += 1

    def require_identity(header: bytes, label: bytes) -> None:
        match = re.fullmatch(
            label
            + rb" ([^<>\x00-\x1f\x7f]+) <([^<>\x00-\x20\x7f]+)> "
            + rb"(0|[1-9][0-9]*) ([+-])((?:0[0-9])|(?:1[0-4]))([0-5][0-9])",
            header,
        )
        if match is None or match.group(1) != match.group(1).strip():
            raise ProductionAuthorityError(
                f"reviewed Git commit has malformed {label.decode()} header"
            )
        if match.group(5) == b"14" and match.group(6) != b"00":
            raise ProductionAuthorityError(
                f"reviewed Git commit has malformed {label.decode()} timezone"
            )

    if len(headers) != cursor + 2:
        raise ProductionAuthorityError(
            "reviewed Git commit has missing, duplicate, or unknown headers"
        )
    require_identity(headers[cursor], b"author")
    require_identity(headers[cursor + 1], b"committer")
    return tree_match.group(1).decode("ascii"), tuple(parents)


def _v2_git_commit_tree(project_root: Path, commit_oid: str) -> str:
    return _v2_git_commit_metadata(project_root, commit_oid)[0]


def _v2_git_tree_entry(
    project_root: Path, tree_oid: str, name: str
) -> tuple[int, str]:
    kind, payload = _v2_git_read_object(project_root, tree_oid)
    if kind != "tree":
        raise ProductionAuthorityError(
            "Git path traversal encountered a non-tree object"
        )
    wanted = name.encode("utf-8")
    cursor = 0
    matches: list[tuple[int, str]] = []
    previous: bytes | None = None
    while cursor < len(payload):
        space = payload.find(b" ", cursor)
        nul = payload.find(b"\x00", space + 1)
        if space <= cursor or nul < 0 or nul + 21 > len(payload):
            raise ProductionAuthorityError("malformed Git tree object")
        mode_raw = payload[cursor:space]
        entry_name = payload[space + 1:nul]
        if previous is not None and entry_name == previous:
            raise ProductionAuthorityError("duplicate Git tree entry")
        previous = entry_name
        try:
            mode = int(mode_raw, 8)
        except ValueError as error:
            raise ProductionAuthorityError("malformed Git tree mode") from error
        child_oid = payload[nul + 1:nul + 21].hex()
        if entry_name == wanted:
            matches.append((mode, child_oid))
        cursor = nul + 21
    if len(matches) != 1:
        raise ProductionAuthorityError(
            f"Git tree path component {name!r} is missing/ambiguous"
        )
    return matches[0]


def _v2_git_optional_tree_entry(
    project_root: Path, tree_oid: str, name: str
) -> tuple[int, str] | None:
    """Return one tree entry, distinguishing strict absence from corruption."""

    kind, payload = _v2_git_read_object(project_root, tree_oid)
    if kind != "tree":
        raise ProductionAuthorityError(
            "Git optional path traversal encountered a non-tree object"
        )
    wanted = name.encode("utf-8")
    cursor = 0
    names: set[bytes] = set()
    match: tuple[int, str] | None = None
    while cursor < len(payload):
        space = payload.find(b" ", cursor)
        nul = payload.find(b"\x00", space + 1)
        if space <= cursor or nul < 0 or nul + 21 > len(payload):
            raise ProductionAuthorityError("malformed Git tree object")
        mode_raw = payload[cursor:space]
        entry_name = payload[space + 1:nul]
        if (
            not entry_name
            or b"/" in entry_name
            or entry_name in {b".", b".."}
            or entry_name in names
            or re.fullmatch(rb"[0-7]+", mode_raw) is None
        ):
            raise ProductionAuthorityError("malformed/duplicate Git tree entry")
        names.add(entry_name)
        mode = int(mode_raw, 8)
        child_oid = payload[nul + 1:nul + 21].hex()
        if entry_name == wanted:
            match = (mode, child_oid)
        cursor = nul + 21
    if cursor != len(payload):
        raise ProductionAuthorityError("malformed Git tree terminator")
    return match


def _v2_git_commit_blob(
    project_root: Path, commit_oid: str, relative: str
) -> tuple[int, bytes, str]:
    safe_relative_path(relative)
    _repository_root, _git_dir, prefix = _v2_git_roots(project_root)
    parts = (*prefix.parts, *PurePosixPath(relative).parts)
    oid = _v2_git_commit_tree(project_root, commit_oid)
    mode = 0
    for index, part in enumerate(parts):
        mode, child = _v2_git_tree_entry(project_root, oid, part)
        if index != len(parts) - 1:
            if mode != 0o40000:
                raise ProductionAuthorityError(
                    "Git reviewed path crosses a non-directory"
                )
            oid = child
        else:
            if mode not in (0o100644, 0o100755):
                raise ProductionAuthorityError(
                    "Git reviewed artifact is not a regular tracked blob"
                )
            kind, raw = _v2_git_read_object(project_root, child)
            if kind != "blob":
                raise ProductionAuthorityError(
                    "Git reviewed path does not resolve to a blob"
                )
            framed = b"blob " + str(len(raw)).encode() + b"\x00" + raw
            if _v2_git_sha1(framed) != child:
                raise ProductionAuthorityError("Git reviewed blob ID mismatch")
            return mode, raw, child
    raise ProductionAuthorityError("empty Git reviewed path")


def _v2_git_optional_commit_blob(
    project_root: Path, commit_oid: str, relative: str
) -> tuple[int, bytes, str] | None:
    """Resolve a regular blob or return None only for lexical path absence."""

    safe_relative_path(relative)
    _repository_root, _git_dir, prefix = _v2_git_roots(project_root)
    parts = (*prefix.parts, *PurePosixPath(relative).parts)
    oid = _v2_git_commit_tree(project_root, commit_oid)
    for index, part in enumerate(parts):
        entry = _v2_git_optional_tree_entry(project_root, oid, part)
        if entry is None:
            return None
        mode, child = entry
        if index != len(parts) - 1:
            if mode != 0o40000:
                raise ProductionAuthorityError(
                    "Git optional path crosses a non-directory"
                )
            oid = child
            continue
        if mode not in (0o100644, 0o100755):
            raise ProductionAuthorityError(
                "Git optional artifact is not a regular tracked blob"
            )
        kind, raw = _v2_git_read_object(project_root, child)
        if kind != "blob":
            raise ProductionAuthorityError(
                "Git optional path does not resolve to a blob"
            )
        framed = b"blob " + str(len(raw)).encode() + b"\x00" + raw
        if _v2_git_sha1(framed) != child:
            raise ProductionAuthorityError("Git optional blob ID mismatch")
        return mode, raw, child
    raise ProductionAuthorityError("empty Git optional path")


def _v2_git_assert_binding(
    resolved: tuple[int, bytes, str] | None,
    binding: Mapping[str, Any],
    context: str,
) -> None:
    if resolved is None:
        raise ProductionAuthorityError(f"{context}: tracked path is absent")
    mode, raw, _blob_oid = resolved
    expected_mode = (
        0o100755 if int(binding["mode"], 8) & 0o111 else 0o100644
    )
    if (
        mode != expected_mode
        or len(raw) != binding["size_bytes"]
        or sha256_bytes(raw) != binding["sha256"]
    ):
        raise ProductionAuthorityError(f"{context}: Git blob/mode drift")


def _v2_git_validate_continuous_introduction(
    project_root: Path,
    *,
    capture_commit: str,
    introduction_commit: str,
    binding: Mapping[str, Any],
    context: str,
) -> None:
    """Prove first-parent reachability, continuity, and one exact introduction."""

    for oid, label in (
        (capture_commit, "capture"),
        (introduction_commit, "introduction"),
    ):
        if type(oid) is not str or V2_ROLE11_GIT_OID.fullmatch(oid) is None:
            raise ProductionAuthorityError(f"{context}: malformed {label} OID")
    current = capture_commit
    seen: set[str] = set()
    for _depth in range(65536):
        if current in seen:
            raise ProductionAuthorityError(f"{context}: cyclic commit ancestry")
        seen.add(current)
        _v2_git_assert_binding(
            _v2_git_optional_commit_blob(
                project_root, current, binding["path"]
            ),
            binding,
            f"{context} continuity at {current}",
        )
        _tree, parents = _v2_git_commit_metadata(project_root, current)
        if current == introduction_commit:
            if len(parents) != 1:
                raise ProductionAuthorityError(
                    f"{context}: introduction must be an ordinary single-parent commit"
                )
            older = parents[0]
            for _older_depth in range(65536 - len(seen)):
                if older in seen:
                    raise ProductionAuthorityError(
                        f"{context}: cyclic pre-introduction ancestry"
                    )
                seen.add(older)
                if _v2_git_optional_commit_blob(
                    project_root, older, binding["path"]
                ) is not None:
                    raise ProductionAuthorityError(
                        f"{context}: path existed before its claimed introduction"
                    )
                _older_tree, older_parents = _v2_git_commit_metadata(
                    project_root, older
                )
                if not older_parents:
                    return
                older = older_parents[0]
            raise ProductionAuthorityError(
                f"{context}: pre-introduction ancestry exceeds cap"
            )
        if not parents:
            raise ProductionAuthorityError(
                f"{context}: introduction is not first-parent reachable"
            )
        current = parents[0]
    raise ProductionAuthorityError(f"{context}: commit ancestry exceeds cap")


def _v2_git_find_continuous_introduction(
    project_root: Path,
    *,
    capture_commit: str,
    binding: Mapping[str, Any],
    context: str,
) -> str:
    """Find the unique first-parent introduction while rejecting drift/re-adds."""

    current = capture_commit
    seen: set[str] = set()
    for _depth in range(65536):
        if current in seen:
            raise ProductionAuthorityError(f"{context}: cyclic commit ancestry")
        seen.add(current)
        _v2_git_assert_binding(
            _v2_git_optional_commit_blob(
                project_root, current, binding["path"]
            ),
            binding,
            f"{context} continuity at {current}",
        )
        _tree, parents = _v2_git_commit_metadata(project_root, current)
        if parents:
            parent_value = _v2_git_optional_commit_blob(
                project_root, parents[0], binding["path"]
            )
            if parent_value is None:
                if len(parents) != 1:
                    raise ProductionAuthorityError(
                        f"{context}: introduction must be an ordinary "
                        "single-parent commit"
                    )
                _v2_git_validate_continuous_introduction(
                    project_root,
                    capture_commit=capture_commit,
                    introduction_commit=current,
                    binding=binding,
                    context=context,
                )
                return current
        if not parents:
            raise ProductionAuthorityError(
                f"{context}: path was introduced by a root commit"
            )
        current = parents[0]
    raise ProductionAuthorityError(f"{context}: commit ancestry exceeds cap")


def _v2_git_ref(project_root: Path, relative: str) -> str:
    _repository_root, git_dir, _prefix = _v2_git_roots(project_root)
    safe_relative_path(relative)
    path = git_dir.joinpath(*PurePosixPath(relative).parts)
    try:
        raw = _v2_git_snapshot(path, 1024 * 1024)
    except FileNotFoundError:
        packed = _v2_git_snapshot(git_dir / "packed-refs", 16 * 1024 * 1024)
        try:
            text = packed.decode("ascii", errors="strict")
        except UnicodeError as error:
            raise ProductionAuthorityError("Git packed refs is not ASCII") from error
        matches = [
            line[:40]
            for line in text.splitlines()
            if re.fullmatch(rf"[0-9a-f]{{40}} {re.escape(relative)}", line)
        ]
        if len(matches) != 1:
            raise ProductionAuthorityError(f"Git ref {relative} missing/ambiguous")
        return matches[0]
    try:
        text = raw.decode("ascii", errors="strict")
    except UnicodeError as error:
        raise ProductionAuthorityError(f"Git ref {relative} is not ASCII") from error
    if re.fullmatch(r"[0-9a-f]{40}\n", text) is None:
        raise ProductionAuthorityError(f"Git ref {relative} is malformed")
    return text[:-1]


def _v2_git_index_records(
    project_root: Path,
) -> tuple[list[tuple[str, int, str]], bytes]:
    _repository_root, git_dir, _prefix = _v2_git_roots(project_root)
    raw = _v2_git_snapshot(git_dir / "index", 128 * 1024 * 1024)
    if len(raw) < 32 or raw[:4] != b"DIRC":
        raise ProductionAuthorityError("Git index header is malformed")
    version, count = struct.unpack_from(">II", raw, 4)
    if version != 2 or count <= 0:
        raise ProductionAuthorityError("Git index must be nonempty version 2")
    body, checksum = raw[:-20], raw[-20:]
    if hashlib.sha1(body, usedforsecurity=False).digest() != checksum:
        raise ProductionAuthorityError("Git index checksum mismatch")
    cursor = 12
    fixed_format = ">LLLLLLLLLL20sH"
    fixed_size = struct.calcsize(fixed_format)
    records: list[tuple[str, int, str]] = []
    for index in range(count):
        entry_start = cursor
        if cursor + fixed_size > len(body):
            raise ProductionAuthorityError(f"Git index entry {index} is truncated")
        fields = struct.unpack_from(fixed_format, body, cursor)
        mode, object_id, flags = fields[6], fields[10].hex(), fields[11]
        cursor += fixed_size
        if flags & 0xF000:
            raise ProductionAuthorityError("Git index uses staged/extended entries")
        try:
            path_end = body.index(b"\x00", cursor)
        except ValueError as error:
            raise ProductionAuthorityError("Git index path is unterminated") from error
        path_raw = body[cursor:path_end]
        try:
            relative = path_raw.decode("utf-8", errors="strict")
        except UnicodeError as error:
            raise ProductionAuthorityError("Git index path is not UTF-8") from error
        safe_relative_path(relative)
        if (flags & 0x0FFF) != min(len(path_raw), 0x0FFF):
            raise ProductionAuthorityError("Git index path-length flag mismatch")
        if mode not in (0o100644, 0o100755):
            raise ProductionAuthorityError(
                "V2 authority Git index permits regular tracked files only"
            )
        cursor = path_end + 1
        while (cursor - entry_start) % 8:
            if cursor >= len(body) or body[cursor] != 0:
                raise ProductionAuthorityError("Git index padding is malformed")
            cursor += 1
        records.append((relative, mode, object_id))
    while cursor < len(body):
        if cursor + 8 > len(body):
            raise ProductionAuthorityError("Git index extension is truncated")
        signature = body[cursor:cursor + 4]
        extension_size = struct.unpack_from(">I", body, cursor + 4)[0]
        cursor += 8
        if (
            re.fullmatch(rb"[A-Z]{4}", signature) is None
            or extension_size > len(body) - cursor
        ):
            raise ProductionAuthorityError(
                "Git index extension is malformed or required"
            )
        cursor += extension_size
    if records != sorted(records, key=lambda item: item[0].encode("utf-8")) or len(
        {item[0] for item in records}
    ) != len(records):
        raise ProductionAuthorityError("Git index paths are unordered/duplicated")
    return records, raw


def _v2_git_index_tree_oid(records: Sequence[tuple[str, int, str]]) -> str:
    def node() -> dict[str, dict[str, Any]]:
        return {"files": {}, "directories": {}}

    root = node()
    for relative, mode, oid in records:
        current = root
        parts = PurePosixPath(relative).parts
        for part in parts[:-1]:
            if part in current["files"]:
                raise ProductionAuthorityError(
                    "Git index file/directory prefix collision"
                )
            current = current["directories"].setdefault(part, node())
        name = parts[-1]
        if name in current["files"] or name in current["directories"]:
            raise ProductionAuthorityError("Git index duplicate tree entry")
        current["files"][name] = (mode, oid)

    def digest(current: dict[str, dict[str, Any]]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, (mode, oid) in current["files"].items():
            encoded = name.encode("utf-8")
            entries.append((
                encoded,
                f"{mode:o}".encode("ascii") + b" " + encoded + b"\x00"
                + bytes.fromhex(oid),
            ))
        for name, child in current["directories"].items():
            encoded = name.encode("utf-8")
            entries.append((
                encoded + b"/",
                b"40000 " + encoded + b"\x00" + bytes.fromhex(digest(child)),
            ))
        content = b"".join(payload for _sort_key, payload in sorted(entries))
        framed = b"tree " + str(len(content)).encode() + b"\x00" + content
        return _v2_git_sha1(framed)

    return digest(root)


def _v2_git_validate_current_repository(
    project_root: Path,
    *,
    capture_commit: str,
    capture_tree: str,
    origin_main: str,
    required_bindings: Sequence[Mapping[str, Any]],
) -> None:
    """Pure index/ref/worktree replay used only at role-11 capture/publish."""

    repository_root, git_dir, prefix = _v2_git_roots(project_root)
    head = _v2_git_snapshot(git_dir / "HEAD", 4096)
    if head != b"ref: refs/heads/main\n":
        raise ProductionAuthorityError("Git HEAD is not exact symbolic main")
    if (
        _v2_git_ref(project_root, "refs/heads/main") != capture_commit
        or _v2_git_ref(project_root, "refs/remotes/origin/main") != origin_main
    ):
        raise ProductionAuthorityError("Git current refs differ from role-11 snapshot")
    records, index_raw = _v2_git_index_records(project_root)
    if _v2_git_index_tree_oid(records) != capture_tree:
        raise ProductionAuthorityError("Git index tree differs from capture tree")
    record_map = {path: (mode, oid) for path, mode, oid in records}
    required_repository_paths = {
        PurePosixPath(*prefix.parts, *PurePosixPath(item["path"]).parts).as_posix()
        for item in required_bindings
    }
    if not required_repository_paths.issubset(record_map):
        raise ProductionAuthorityError("role-11 required binding is not Git-tracked")
    for relative, mode, oid in records:
        path = repository_root.joinpath(*PurePosixPath(relative).parts)
        raw = _v2_git_snapshot(path, 1024 * 1024 * 1024)
        info = os.stat(path, follow_symlinks=False)
        if bool(stat.S_IMODE(info.st_mode) & 0o111) is not (mode == 0o100755):
            raise ProductionAuthorityError(
                f"Git worktree executable bit differs: {relative}"
            )
        framed = b"blob " + str(len(raw)).encode() + b"\x00" + raw
        if _v2_git_sha1(framed) != oid:
            raise ProductionAuthorityError(f"Git worktree blob differs: {relative}")
    replay_records, replay_raw = _v2_git_index_records(project_root)
    if replay_records != records or replay_raw != index_raw:
        raise ProductionAuthorityError("Git index changed during worktree replay")
    if (
        _v2_git_ref(project_root, "refs/heads/main") != capture_commit
        or _v2_git_ref(project_root, "refs/remotes/origin/main") != origin_main
    ):
        raise ProductionAuthorityError("Git refs changed during worktree replay")


def _v2_git_origin_url(project_root: Path) -> str:
    _repository_root, git_dir, _prefix = _v2_git_roots(project_root)
    raw = _v2_git_snapshot(git_dir / "config", 1024 * 1024)
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as error:
        raise ProductionAuthorityError("Git config is not UTF-8") from error
    current: tuple[str, str | None] | None = None
    origin_sections = 0
    urls: list[str] = []
    for line in text.splitlines():
        if line.endswith("\\"):
            raise ProductionAuthorityError(
                "Git config continuation syntax is forbidden"
            )
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", ";")):
            continue
        section = re.fullmatch(
            r'[ \t]*\[([A-Za-z][A-Za-z0-9.-]*)(?:[ \t]+"([^"\\]*)")?\][ \t]*',
            line,
        )
        if section is not None:
            base = section.group(1).lower()
            subsection = section.group(2)
            if base in {"include", "includeif", "url"}:
                raise ProductionAuthorityError(
                    "Git include and URL-rewrite sections are forbidden"
                )
            current = (base, subsection)
            if current == ("remote", "origin"):
                origin_sections += 1
            continue
        key_value = re.fullmatch(
            r"[ \t]+([A-Za-z][A-Za-z0-9.-]*)[ \t]*(?:=[ \t]*(.*?)[ \t]*)?",
            line,
        )
        if current is None or key_value is None:
            raise ProductionAuthorityError("Git config line grammar is malformed")
        key = key_value.group(1).lower()
        value = key_value.group(2)
        if key in {"insteadof", "pushinsteadof"} or key.endswith(
            (".insteadof", ".pushinsteadof")
        ):
            raise ProductionAuthorityError("Git URL rewrite directive is forbidden")
        if current == ("remote", "origin") and key == "url":
            if value is None or re.fullmatch(r"\S+", value) is None:
                raise ProductionAuthorityError("Git origin URL syntax is malformed")
            urls.append(value)
    if origin_sections != 1 or urls != [V2_ROLE11_ORIGIN_URL]:
        raise ProductionAuthorityError("Git origin URL config mismatch")
    return urls[0]


def _v2_role11_live_remote_probe(project_root: Path) -> str:
    """Truthfully observe the live remote main ref with bounded plumbing."""

    repository_root, _git_dir, _prefix = _v2_git_roots(project_root)
    remote = _capture_command(
        (
            "/usr/bin/git", "-C", os.fspath(repository_root), "ls-remote",
            "--heads", "origin", "refs/heads/main",
        ),
        cwd=repository_root,
        environment=V2_ROLE11_ENVIRONMENT,
        timeout_seconds=60,
        umask=0o022,
    )
    if (
        remote.returncode != 0
        or remote.stderr != b""
        or len(remote.stdout) > V2_ROLE11_MAX_STREAM_BYTES
    ):
        raise ProductionAuthorityError(
            "V2 role 11 live-remote repository probe failed"
        )
    match = re.fullmatch(
        rb"([0-9a-f]{40})\trefs/heads/main\n", remote.stdout
    )
    if match is None:
        raise ProductionAuthorityError("V2 role 11 ls-remote transcript mismatch")
    return match.group(1).decode("ascii")


def _v2_role11_status_probe(project_root: Path) -> bytes:
    """Return one bounded exact porcelain transcript without interpreting it."""

    repository_root, _git_dir, _prefix = _v2_git_roots(project_root)
    status = _capture_command(
        (
            "/usr/bin/git", "-C", os.fspath(repository_root), "status",
            "--porcelain=v1", "--untracked-files=all",
        ),
        cwd=repository_root,
        environment=V2_ROLE11_ENVIRONMENT,
        timeout_seconds=60,
        umask=0o022,
    )
    if (
        status.returncode != 0
        or status.stderr != b""
        or len(status.stdout) > V2_ROLE11_MAX_STREAM_BYTES
    ):
        raise ProductionAuthorityError("V2 role 11 status repository probe failed")
    return status.stdout


def _v2_role11_repository_probes(project_root: Path) -> str:
    """Require one live-remote observation and an exactly clean worktree."""

    remote = _v2_role11_live_remote_probe(project_root)
    if _v2_role11_status_probe(project_root) != b"":
        raise ProductionAuthorityError("V2 role 11 worktree is not exactly clean")
    return remote


def _v2_role11_expect_publication_status(
    project_root: Path,
    path: Path,
    expected_identity: tuple[int, int],
    context: str,
) -> None:
    """Allow exactly one owned untracked publication leaf and nothing else."""

    repository_root, _git_dir, _prefix = _v2_git_roots(project_root)
    try:
        relative = path.relative_to(repository_root).as_posix()
    except ValueError as error:
        raise PathContractError(f"{context}: path escapes repository") from error
    expected = f"?? {relative}\n".encode("ascii")
    if _v2_role11_status_probe(project_root) != expected:
        raise ProductionAuthorityError(
            f"{context}: porcelain transcript is not the one owned leaf"
        )
    parent_fd = _open_directory_fd(path.parent)
    try:
        entry = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        if (
            not stat.S_ISREG(entry.st_mode)
            or entry.st_nlink != 1
            or (entry.st_dev, entry.st_ino) != expected_identity
        ):
            raise PathContractError(f"{context}: owned publication inode mismatch")
    finally:
        os.close(parent_fd)


def _v2_role11_publication_fault_hook(_boundary: str) -> None:
    """No-op production hook; tests may inject durable-boundary failures."""

    return None


def validate_v2_role5_repository_bindings(
    payload: Mapping[str, Any],
    authority_root: Path,
    role_records: Mapping[str, FormalRoleRecord],
) -> None:
    """Replay role 5 against live legacy bytes and its reviewed Git tree."""

    root = safe_absolute_path(os.fspath(authority_root), "V2 role 5 authority root")
    validate_v2_role5_payload(payload, role_records)
    reviewed_commit = payload["review"]["reviewed_commit"]
    for item in V2_ROLE5_LEGACY_ARTIFACTS:
        path = authority_project_file(root, item["path"])
        raw, info = read_pinned_regular_file(path)
        if sha256_bytes(raw) != item["sha256"]:
            raise ProductionAuthorityError("V2 role 5 legacy bytes changed")
        legacy_binding = {
            "path": item["path"],
            "sha256": item["sha256"],
            "size_bytes": len(raw),
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
        }
        _v2_git_validate_continuous_introduction(
            root,
            capture_commit=reviewed_commit,
            introduction_commit=item["publication_commit"],
            binding=legacy_binding,
            context=f"V2 role 5 legacy role {item['role']}",
        )
    for item in payload["reviewed_v2_inputs"]:
        record = role_records[item["role"]]
        path = authority_project_file(root, item["path"])
        live_raw, live_info = read_pinned_regular_file(path)
        if live_raw != record.raw:
            raise ProductionAuthorityError(
                f"V2 role 5 reviewed live replay mismatch: {item['role']}"
            )
        git_mode, committed, _blob_oid = _v2_git_commit_blob(
            root, reviewed_commit, item["path"]
        )
        expected_mode = (
            0o100755 if stat.S_IMODE(live_info.st_mode) & 0o111 else 0o100644
        )
        if (
            committed != record.raw
            or sha256_bytes(committed) != item["sha256"]
            or git_mode != expected_mode
        ):
            raise ProductionAuthorityError(
                f"V2 role 5 reviewed commit mismatch: {item['role']}"
            )


def _v2_role11_plain_json(
    value: Any, context: str, active: set[int] | None = None
) -> None:
    """Reject aliases outside the exact acyclic JSON domain used by role 11."""

    if active is None:
        active = set()
    if value is None or type(value) in (bool, int):
        return
    if type(value) is str:
        try:
            value.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise ProductionAuthorityError(
                f"{context}: string is not strict UTF-8"
            ) from error
        return
    if type(value) not in (list, dict):
        raise ProductionAuthorityError(
            f"{context}: non-plain JSON value {type(value).__name__}"
        )
    identity = id(value)
    if identity in active:
        raise ProductionAuthorityError(f"{context}: cyclic JSON value")
    active.add(identity)
    try:
        if type(value) is list:
            for index, item in enumerate(value):
                _v2_role11_plain_json(item, f"{context}[{index}]", active)
        else:
            for key, item in value.items():
                if type(key) is not str:
                    raise ProductionAuthorityError(
                        f"{context}: object key is not an exact string"
                    )
                _v2_role11_plain_json(item, f"{context}.{key}", active)
    finally:
        active.remove(identity)


def _v2_role11_string(
    value: Any, context: str, *, expected: str | None = None
) -> str:
    if type(value) is not str or not value or "\x00" in value:
        raise ProductionAuthorityError(f"{context}: exact nonempty string required")
    if expected is not None and value != expected:
        raise ProductionAuthorityError(f"{context}: literal mismatch")
    return value


def _v2_role11_int(
    value: Any,
    context: str,
    *,
    minimum: int = 0,
    maximum: int | None = None,
    expected: int | None = None,
) -> int:
    if type(value) is not int or value < minimum:
        raise ProductionAuthorityError(f"{context}: exact integer out of range")
    if maximum is not None and value > maximum:
        raise ProductionAuthorityError(f"{context}: exact integer exceeds cap")
    if expected is not None and value != expected:
        raise ProductionAuthorityError(f"{context}: integer literal mismatch")
    return value


def _v2_role11_bool(value: Any, context: str, expected: bool) -> None:
    if type(value) is not bool or value is not expected:
        raise ProductionAuthorityError(f"{context}: Boolean literal mismatch")


def _v2_role11_hash(
    value: Any, context: str, *, expected: str | None = None
) -> str:
    text = _v2_role11_string(value, context)
    if HEX_SHA256.fullmatch(text) is None:
        raise ProductionAuthorityError(f"{context}: lowercase SHA-256 required")
    if expected is not None and text != expected:
        raise ProductionAuthorityError(f"{context}: SHA-256 mismatch")
    return text


def _v2_role11_git_oid(value: Any, context: str) -> str:
    text = _v2_role11_string(value, context)
    if V2_ROLE11_GIT_OID.fullmatch(text) is None:
        raise ProductionAuthorityError(f"{context}: lowercase Git OID required")
    return text


def _v2_role11_utc(value: Any, context: str) -> datetime:
    text = _v2_role11_string(value, context)
    if V2_ROLE11_UTC.fullmatch(text) is None:
        raise ProductionAuthorityError(
            f"{context}: canonical whole-second UTC timestamp required"
        )
    try:
        parsed = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError as error:
        raise ProductionAuthorityError(f"{context}: invalid UTC timestamp") from error
    if parsed.strftime("%Y-%m-%dT%H:%M:%SZ") != text:
        raise ProductionAuthorityError(f"{context}: noncanonical UTC timestamp")
    return parsed


def _v2_role11_mode(value: Any, context: str) -> str:
    text = _v2_role11_string(value, context)
    if V2_ROLE11_MODE.fullmatch(text) is None:
        raise ProductionAuthorityError(f"{context}: four-digit octal mode required")
    return text


def _v2_role11_relative(
    value: Any, context: str, *, expected: str | None = None
) -> str:
    text = _v2_role11_string(value, context, expected=expected)
    try:
        safe_relative_path(text)
    except PathContractError as error:
        raise ProductionAuthorityError(f"{context}: unsafe relative path") from error
    return text


def _v2_role11_role_entry(
    value: Any,
    expected_role: str,
    expected_path: str,
    context: str,
) -> dict[str, Any]:
    exact_keys(value, V2_PREFREEZE_INPUT_KEYS, context)
    _v2_role11_string(value["role"], f"{context}.role", expected=expected_role)
    _v2_role11_relative(value["path"], f"{context}.path", expected=expected_path)
    _v2_role11_hash(value["sha256"], f"{context}.sha256")
    _v2_role11_int(value["size_bytes"], f"{context}.size_bytes", minimum=1)
    _v2_role11_mode(value["mode"], f"{context}.mode")
    _v2_role11_int(value["nlink"], f"{context}.nlink", expected=1)
    return dict(value)


def _v2_role11_file_binding(
    value: Any, expected_path: str, context: str
) -> dict[str, Any]:
    exact_keys(value, V2_ROLE11_FILE_BINDING_KEYS, context)
    _v2_role11_relative(value["path"], f"{context}.path", expected=expected_path)
    _v2_role11_hash(value["sha256"], f"{context}.sha256")
    _v2_role11_int(value["size_bytes"], f"{context}.size_bytes", minimum=1)
    _v2_role11_mode(value["mode"], f"{context}.mode")
    _v2_role11_int(value["nlink"], f"{context}.nlink", expected=1)
    return dict(value)


def _v2_role11_git_binding(
    authority_root: Path,
    commit_oid: str,
    binding: Mapping[str, Any],
    context: str,
) -> None:
    git_mode, raw, _blob_oid = _v2_git_commit_blob(
        authority_root, commit_oid, binding["path"]
    )
    expected_git_mode = (
        0o100755 if int(binding["mode"], 8) & 0o111 else 0o100644
    )
    if (
        git_mode != expected_git_mode
        or len(raw) != binding["size_bytes"]
        or sha256_bytes(raw) != binding["sha256"]
    ):
        raise ProductionAuthorityError(f"{context}: Git tree binding mismatch")


def _v2_absence_snapshot(
    paths: Sequence[Path], context: str
) -> tuple[tuple[str, int, int], ...]:
    """Pin lexical parents and require missing leaves of every possible type."""

    records: list[tuple[str, int, int]] = []
    for path in paths:
        canonical = safe_absolute_path(os.fspath(path), f"{context} path")
        parent_fd = _open_directory_fd(canonical.parent)
        try:
            parent = os.fstat(parent_fd)
            try:
                os.stat(
                    canonical.name,
                    dir_fd=parent_fd,
                    follow_symlinks=False,
                )
            except FileNotFoundError:
                pass
            else:
                raise ProductionAuthorityError(
                    f"{context}: namespace leaf already exists: {canonical}"
                )
            records.append((os.fspath(canonical), parent.st_dev, parent.st_ino))
        finally:
            os.close(parent_fd)
    return tuple(records)


def _v2_absence_replay(
    records: Sequence[tuple[str, int, int]], context: str
) -> None:
    for path_text, expected_device, expected_inode in records:
        path = safe_absolute_path(path_text, f"{context} replay path")
        parent_fd = _open_directory_fd(path.parent)
        try:
            parent = os.fstat(parent_fd)
            if (parent.st_dev, parent.st_ino) != (
                expected_device,
                expected_inode,
            ):
                raise ProductionAuthorityError(
                    f"{context}: lexical parent changed: {path.parent}"
                )
            try:
                os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
            except FileNotFoundError:
                pass
            else:
                raise ProductionAuthorityError(
                    f"{context}: namespace appeared during replay: {path}"
                )
        finally:
            os.close(parent_fd)


def v2_role11_fixed_command_argv(
    authority_root: Path,
    python_executable: str,
    *,
    rebuild_output: str,
) -> tuple[tuple[str, ...], ...]:
    """Return the seven duplicated, non-scientific V2 argv identities."""

    root = safe_absolute_path(os.fspath(authority_root), "role-11 authority root")
    python_path = safe_absolute_path(python_executable, "role-11 Python executable")
    if V2_ROLE11_REBUILD_OUTPUT.fullmatch(rebuild_output) is None:
        raise ProductionAuthorityError("role-11 rebuild output path mismatch")
    return (
        (
            os.fspath(python_path),
            os.fspath(root / V2_ROLE11_TOOL_PATHS["independent_checker"]),
            "--verify-machine-freeze",
            os.fspath(root / dict(FORMAL_INPUT_ROLES)["machine_freeze"]),
        ),
        (
            os.fspath(python_path),
            os.fspath(root / V2_ROLE11_TOOL_PATHS["independent_checker"]),
            "--verify-s0-compatibility",
            os.fspath(root / dict(FORMAL_INPUT_ROLES)["s0_compatibility"]),
        ),
        (
            os.fspath(python_path), "-m", "pytest", "-q", "-p",
            "no:cacheprovider", "--color=no",
            "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py",
        ),
        (
            os.fspath(python_path), "-m", "pytest", "-q", "-p",
            "no:cacheprovider", "--color=no",
            "tests/test_r401_val_l3_a1_static_cell.py",
            "tests/test_r401_val_l3_a1_v2_static_scheduler.py",
            "tests/test_r401_val_l3_a1_v2_static_checker.py",
            "tests/test_r401_val_l3_a1_v2_branch_scheduler.py",
            "tests/test_r401_val_l3_a1_v2_branch_checker.py",
            "tests/test_r401_val_l3_a1_v2_s0_compatibility.py",
            "tests/test_r401_val_l3_a1_v2_composite_contract.py",
            "tests/test_r401_val_l3_a1_v2_adversarial_e2e.py",
            "tests/test_r401_val_l3_a1_v2_release_provenance.py",
        ),
        (
            os.fspath(python_path), "-m", "pytest", "-q", "-p",
            "no:cacheprovider", "--color=no",
        ),
        ("/usr/bin/git", "diff", "--check", "HEAD", "--"),
        (
            os.fspath(python_path),
            os.fspath(root / V2_ROLE11_TOOL_PATHS["producer"]),
            "--second-fresh-rebuild-only", "--output", rebuild_output,
        ),
    )


def _require_v2_role11_mechanical_lock() -> None:
    if V2_ROLE11_FINAL_COMMAND_LOCKED is not True:
        raise ProductionAuthorityError(
            "V2 role-11 argv/environment mechanical lock is not final"
        )
    if (
        type(V2_ROLE11_EXPECTED_TEST_PASSED) is not dict
        or set(V2_ROLE11_EXPECTED_TEST_PASSED) != V2_ROLE11_TEST_TOTALS_KEYS
        or any(
            type(value) is not int or value <= 0
            for value in V2_ROLE11_EXPECTED_TEST_PASSED.values()
        )
    ):
        raise ProductionAuthorityError(
            "V2 role-11 stable pytest count registry is not final"
        )


def _v2_role11_verify_receipt(
    value: Any,
    *,
    status_value: str,
    candidate_sha256: str,
    size_bytes: int,
    context: str,
) -> dict[str, Any]:
    exact_keys(value, V2_ROLE11_VERIFY_RECEIPT_KEYS, context)
    _v2_role11_string(
        value["verification_status"],
        f"{context}.verification_status",
        expected=status_value,
    )
    _v2_role11_string(
        value["authority"],
        f"{context}.authority",
        expected="NON_AUTHORITATIVE_VERIFY_ONLY",
    )
    _v2_role11_hash(
        value["candidate_sha256"],
        f"{context}.candidate_sha256",
        expected=candidate_sha256,
    )
    _v2_role11_int(
        value["size_bytes"], f"{context}.size_bytes", expected=size_bytes
    )
    _v2_role11_bool(
        value["promotion_authorized"],
        f"{context}.promotion_authorized",
        False,
    )
    return dict(value)


def _v2_role11_second_rebuild_receipt(
    value: Any, roles: Mapping[str, Mapping[str, Any]], context: str
) -> dict[str, Any]:
    exact_keys(value, V2_ROLE11_SECOND_REBUILD_KEYS, context)
    source = roles["branch_evaluator_source"]
    binary = roles["branch_evaluator_binary"]
    literals = {
        "verification_status": "PASS_SECOND_FRESH_REBUILD",
        "authority": "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY",
        "source_path": source["path"],
        "persistent_binary_path": binary["path"],
        "staging_output_mode": "0755",
    }
    for key, expected in literals.items():
        _v2_role11_string(value[key], f"{context}.{key}", expected=expected)
    _v2_role11_hash(
        value["source_sha256"],
        f"{context}.source_sha256",
        expected=source["sha256"],
    )
    for key in (
        "persistent_before_sha256", "persistent_after_sha256",
        "staging_output_sha256",
    ):
        _v2_role11_hash(
            value[key], f"{context}.{key}", expected=binary["sha256"]
        )
    _v2_role11_int(
        value["staging_output_size_bytes"],
        f"{context}.staging_output_size_bytes",
        expected=binary["size_bytes"],
    )
    for key in (
        "persistent_before_device_id", "persistent_before_inode",
        "persistent_after_device_id", "persistent_after_inode",
    ):
        _v2_role11_int(value[key], f"{context}.{key}", minimum=1)
    if (
        value["persistent_before_device_id"]
        != value["persistent_after_device_id"]
        or value["persistent_before_inode"]
        != value["persistent_after_inode"]
    ):
        raise ProductionAuthorityError(
            f"{context}: persistent binary identity changed"
        )
    for key, expected in (
        ("persistent_identity_unchanged", True),
        ("persistent_overwrite_performed", False),
        ("staging_output_removed", True),
        ("byte_for_byte_equal", True),
        ("scientific_evaluator_dispatched", False),
    ):
        _v2_role11_bool(value[key], f"{context}.{key}", expected)
    return dict(value)


def _v2_role11_parse_pytest(
    stdout: str, context: str
) -> tuple[dict[str, int], int]:
    if type(stdout) is not str or not stdout.endswith("\n"):
        raise ProductionAuthorityError(
            f"{context}: terminal pytest summary/newline required"
        )
    if any(
        (ord(character) < 0x20 and character != "\n")
        or 0x7f <= ord(character) <= 0x9f
        or character in "\u2028\u2029"
        for character in stdout
    ):
        raise ProductionAuthorityError(f"{context}: control output is forbidden")
    lines = stdout[:-1].split("\n")
    matches = [V2_ROLE11_PYTEST_SUMMARY.fullmatch(line) for line in lines]
    if sum(match is not None for match in matches) != 1 or matches[-1] is None:
        raise ProductionAuthorityError(
            f"{context}: exactly one terminal pytest summary required"
        )
    summary = matches[-1]
    assert summary is not None
    elapsed_whole_text, elapsed_fraction = summary.group("elapsed").split(".", 1)
    whole_seconds = int(elapsed_whole_text)
    elapsed_centiseconds = whole_seconds * 100 + int(elapsed_fraction)
    if elapsed_centiseconds > 60000:
        raise ProductionAuthorityError(
            f"{context}: pytest duration exceeds fixed 600-second timeout"
        )
    human_parts = tuple(
        summary.group(name) for name in ("hours", "minutes", "seconds")
    )
    if all(part is None for part in human_parts):
        if whole_seconds > 60 or (
            whole_seconds == 60 and elapsed_fraction != "00"
        ):
            raise ProductionAuthorityError(
                f"{context}: missing long-duration pytest suffix"
            )
    else:
        if any(part is None for part in human_parts):
            raise ProductionAuthorityError(
                f"{context}: malformed long-duration pytest suffix"
            )
        hours, minutes, seconds = (
            int(part) for part in human_parts if part is not None
        )
        human_seconds = hours * 3600 + minutes * 60 + seconds
        allowed_human_seconds = {whole_seconds}
        if elapsed_fraction == "00" and whole_seconds > 60:
            allowed_human_seconds.add(whole_seconds - 1)
        if human_seconds < 60 or human_seconds not in allowed_human_seconds:
            raise ProductionAuthorityError(
                f"{context}: inconsistent long-duration pytest suffix"
            )
    forbidden = re.search(
        r"(?i)(?<![A-Za-z0-9_])"
        r"(?:errors?|fail(?:ed|ures?)?|warnings?|deselected|"
        r"skipped|xfail(?:ed)?|xpass(?:ed)?)"
        r"(?![A-Za-z0-9_])",
        stdout,
    )
    if forbidden is not None:
        raise ProductionAuthorityError(
            f"{context}: forbidden pytest token {forbidden.group(0)!r}"
        )
    counts = {key: 0 for key in V2_ROLE11_TEST_TOTAL_KEYS if key != "wall_duration_ms"}
    observed: set[str] = set()
    for part in summary.group("counts").split(", "):
        count_text, name = part.split(" ", 1)
        if name in observed or name not in counts:
            raise ProductionAuthorityError(f"{context}: duplicate pytest category")
        observed.add(name)
        counts[name] = int(count_text)
    if counts["passed"] <= 0 or any(
        value != 0 for key, value in counts.items() if key != "passed"
    ):
        raise ProductionAuthorityError(f"{context}: pytest is not exact all-pass")
    return counts, elapsed_centiseconds * 10


def _v2_role11_pytest_counts(stdout: str, context: str) -> dict[str, int]:
    return _v2_role11_parse_pytest(stdout, context)[0]


def _v2_role11_command_result(
    value: Any,
    index: int,
    *,
    authority_root: Path,
    python_executable: str,
    roles: Mapping[str, Mapping[str, Any]],
) -> tuple[dict[str, Any], dict[str, int] | None]:
    context = f"command_results[{index}]"
    exact_keys(value, V2_ROLE11_COMMAND_RESULT_KEYS, context)
    expected_name = V2_ROLE11_COMMAND_NAMES[index]
    expected_kind = V2_ROLE11_COMMAND_KINDS[index]
    _v2_role11_string(value["name"], f"{context}.name", expected=expected_name)
    _v2_role11_string(value["kind"], f"{context}.kind", expected=expected_kind)
    argv = value["argv"]
    if type(argv) is not list or not argv or any(
        type(item) is not str or not item or "\x00" in item for item in argv
    ):
        raise ProductionAuthorityError(f"{context}.argv: exact string list required")
    rebuild_output = argv[-1] if expected_name == "second_fresh_rebuild" else (
        "/tmp/a416-l3a1-v2-role11-rebuild.AAAAAA/"
        "capd_r401_phase_branch_tube_mp_a1"
    )
    expected_argv = v2_role11_fixed_command_argv(
        authority_root, python_executable, rebuild_output=rebuild_output
    )[index]
    if tuple(argv) != expected_argv:
        raise ProductionAuthorityError(f"{context}.argv: fixed argv mismatch")
    root_text = os.fspath(
        safe_absolute_path(os.fspath(authority_root), "role-11 authority root")
    )
    _v2_role11_string(value["cwd"], f"{context}.cwd", expected=root_text)
    if not exact_json_equal(value["environment"], V2_ROLE11_ENVIRONMENT):
        raise ProductionAuthorityError(f"{context}.environment: fixed map mismatch")
    _v2_role11_int(value["return_code"], f"{context}.return_code", expected=0)
    _v2_role11_utc(value["started_at_utc"], f"{context}.started_at_utc")
    wall_ms = _v2_role11_int(
        value["wall_duration_ms"],
        f"{context}.wall_duration_ms",
        minimum=1,
        maximum=V2_ROLE11_MAX_WALL_DURATION_MS,
    )
    for stream in ("stdout", "stderr"):
        text = value[f"{stream}_utf8"]
        if type(text) is not str or "\x00" in text:
            raise ProductionAuthorityError(
                f"{context}.{stream}_utf8: NUL-free string required"
            )
        try:
            raw = text.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise ProductionAuthorityError(
                f"{context}.{stream}_utf8: invalid UTF-8"
            ) from error
        if len(raw) > V2_ROLE11_MAX_STREAM_BYTES:
            raise ProductionAuthorityError(
                f"{context}.{stream}_utf8: transcript cap exceeded"
            )
        _v2_role11_int(
            value[f"{stream}_size_bytes"],
            f"{context}.{stream}_size_bytes",
            expected=len(raw),
        )
        _v2_role11_hash(
            value[f"{stream}_sha256"],
            f"{context}.{stream}_sha256",
            expected=sha256_bytes(raw),
        )
    if value["stderr_utf8"] != "":
        raise ProductionAuthorityError(f"{context}: successful stderr must be empty")

    parsed: dict[str, int] | None = None
    if expected_name in V2_ROLE11_PYTEST_TOTAL_NAMES:
        parsed, elapsed_ms = _v2_role11_parse_pytest(
            value["stdout_utf8"], context
        )
        exact_keys(value["pytest_counts"], V2_ROLE11_TEST_TOTAL_KEYS - {"wall_duration_ms"}, f"{context}.pytest_counts")
        for key, expected in parsed.items():
            _v2_role11_int(
                value["pytest_counts"][key],
                f"{context}.pytest_counts.{key}",
                expected=expected,
            )
        if value["semantic_receipt"] is not None:
            raise ProductionAuthorityError(
                f"{context}: pytest semantic receipt must be null"
            )
        if V2_ROLE11_EXPECTED_TEST_PASSED is not None:
            total_name = V2_ROLE11_PYTEST_TOTAL_NAMES[expected_name]
            if parsed["passed"] != V2_ROLE11_EXPECTED_TEST_PASSED.get(total_name):
                raise ProductionAuthorityError(
                    f"{context}: stable passed-count mismatch"
                )
        if elapsed_ms > wall_ms + 5:
            raise ProductionAuthorityError(
                f"{context}: pytest duration exceeds outer wall duration"
            )
    else:
        if value["pytest_counts"] is not None:
            raise ProductionAuthorityError(
                f"{context}: non-pytest counts must be null"
            )
        if expected_name in {
            "role24_machine_verify", "role13_compatibility_verify"
        }:
            role = (
                roles["machine_freeze"]
                if expected_name == "role24_machine_verify"
                else roles["s0_compatibility"]
            )
            status_value = (
                "PASS_MACHINE_FREEZE_VERIFY_ONLY"
                if expected_name == "role24_machine_verify"
                else "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
            )
            receipt = _v2_role11_verify_receipt(
                value["semantic_receipt"],
                status_value=status_value,
                candidate_sha256=role["sha256"],
                size_bytes=role["size_bytes"],
                context=f"{context}.semantic_receipt",
            )
            prefix = (
                "machine_freeze_verification="
                if expected_name == "role24_machine_verify"
                else "s0_compatibility_verification="
            )
            expected_stdout = (
                f"{prefix}{status_value} authority=NON_AUTHORITATIVE_VERIFY_ONLY "
                f"candidate_sha256={role['sha256']} size_bytes={role['size_bytes']} "
                "promotion_authorized=false\n"
            )
            if value["stdout_utf8"] != expected_stdout or not exact_json_equal(
                value["semantic_receipt"], receipt
            ):
                raise ProductionAuthorityError(
                    f"{context}: verify transcript/receipt mismatch"
                )
        elif expected_name == "git_diff_check":
            if value["stdout_utf8"] != "" or value["semantic_receipt"] is not None:
                raise ProductionAuthorityError(
                    f"{context}: diff-check transcript must be empty/null"
                )
        else:
            receipt = _v2_role11_second_rebuild_receipt(
                value["semantic_receipt"], roles, f"{context}.semantic_receipt"
            )
            if value["stdout_utf8"].encode("utf-8") != canonical_json_bytes(receipt):
                raise ProductionAuthorityError(
                    f"{context}: rebuild transcript/receipt mismatch"
                )
    return dict(value), parsed


def validate_v2_prefreeze_test_record(
    payload: Any,
    *,
    authority_root: Path,
    python_executable: str,
    role5_payload: Mapping[str, Any],
    role_records: Mapping[str, FormalRoleRecord] | None = None,
    require_locked: bool = True,
    require_live_absence: bool = False,
) -> dict[str, Any]:
    """Validate the exact V2 role-11 record without running a subprocess.

    ``require_live_absence`` is used only at capture/publication time.  A
    historical role-11 replay after roles 12/54/results exist validates the
    recorded false facts and does not pretend those downstream paths remain
    absent forever.
    """

    if require_locked:
        _require_v2_role11_mechanical_lock()
    root = safe_absolute_path(os.fspath(authority_root), "role-11 authority root")
    absence_records: tuple[tuple[str, int, int], ...] = ()
    if require_live_absence:
        absence_records = _v2_absence_snapshot(
            (
                root / dict(FORMAL_INPUT_ROLES)["prefreeze_tests"],
                root / dict(FORMAL_INPUT_ROLES)["prefreeze_review"],
                root / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json",
                root / "results/r401_val_l3_a1_v2_all_slabs",
                root / "results/r401_val_l3_a1_v2_all_slabs.operational",
            ),
            "V2 role 11 current-stage absence",
        )
    _v2_role11_plain_json(payload, "V2 role 11")
    exact_keys(payload, V2_PREFREEZE_TEST_KEYS, "V2 role 11")
    scalar_literals = {
        "schema_version": 1,
        "protocol_id": V2_ROLE11_PROTOCOL_ID,
        "artifact_role": V2_ROLE11_ARTIFACT_ROLE,
        "artifact_status": V2_ROLE11_ARTIFACT_STATUS,
        "authority": V2_ROLE11_AUTHORITY,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "claim_boundary": V2_ROLE11_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    for key, expected in scalar_literals.items():
        if not exact_json_equal(payload[key], expected):
            raise ProductionAuthorityError(f"V2 role 11 scalar mismatch: {key}")
    recorded_at = _v2_role11_utc(payload["recorded_at_utc"], "recorded_at_utc")

    repository = payload["repository_snapshot"]
    exact_keys(repository, V2_ROLE11_REPOSITORY_KEYS, "repository_snapshot")
    _v2_role11_string(
        repository["authority_root"],
        "repository_snapshot.authority_root",
        expected=os.fspath(root),
    )
    _v2_role11_string(repository["branch"], "repository_snapshot.branch", expected="main")
    capture_commit = _v2_role11_git_oid(
        repository["capture_commit_oid"], "repository_snapshot.capture_commit_oid"
    )
    _v2_role11_git_oid(
        repository["capture_tree_oid"], "repository_snapshot.capture_tree_oid"
    )
    _v2_role11_string(
        repository["origin_url"],
        "repository_snapshot.origin_url",
        expected=V2_ROLE11_ORIGIN_URL,
    )
    for key in ("origin_main_oid", "live_remote_main_oid"):
        if _v2_role11_git_oid(repository[key], f"repository_snapshot.{key}") != capture_commit:
            raise ProductionAuthorityError("V2 role 11 capture/origin/live OIDs differ")
    for key in (
        "head_equals_origin_main", "head_equals_live_remote_main",
        "worktree_clean_before", "worktree_clean_after",
    ):
        _v2_role11_bool(repository[key], f"repository_snapshot.{key}", True)
    _v2_role11_int(repository["ahead"], "repository_snapshot.ahead", expected=0)
    _v2_role11_int(repository["behind"], "repository_snapshot.behind", expected=0)

    entries = payload["pre_review_input_roles"]
    if type(entries) is not list or len(entries) != 51:
        raise ProductionAuthorityError("V2 role 11 needs exact 51-role list")
    roles: dict[str, dict[str, Any]] = {}
    for index, ((expected_role, expected_path), entry) in enumerate(
        zip(V2_ROLE11_PRE_REVIEW_ROLES, entries)
    ):
        validated = _v2_role11_role_entry(
            entry, expected_role, expected_path, f"pre_review_input_roles[{index}]"
        )
        if expected_role in roles:
            raise ProductionAuthorityError("V2 role 11 duplicate role")
        roles[expected_role] = validated
        if role_records is not None:
            record = role_records.get(expected_role)
            if (
                record is None
                or record.path != expected_path
                or record.sha256 != validated["sha256"]
                or len(record.raw) != validated["size_bytes"]
            ):
                raise ProductionAuthorityError(
                    f"V2 role 11 stale live role: {expected_role}"
                )
            live_path = authority_project_file(root, expected_path)
            live_raw, live_info = read_pinned_regular_file(live_path)
            if (
                live_raw != record.raw
                or f"{stat.S_IMODE(live_info.st_mode):04o}" != validated["mode"]
                or live_info.st_nlink != validated["nlink"]
            ):
                raise ProductionAuthorityError(
                    f"V2 role 11 live stat mismatch: {expected_role}"
                )

    if _v2_git_commit_tree(root, capture_commit) != repository["capture_tree_oid"]:
        raise ProductionAuthorityError(
            "V2 role 11 capture commit/tree binding mismatch"
        )
    for role, _path in V2_ROLE11_PRE_REVIEW_ROLES:
        _v2_role11_git_binding(
            root,
            capture_commit,
            roles[role],
            f"V2 role 11 captured role {role}",
        )
    if require_live_absence:
        _v2_git_validate_current_repository(
            root,
            capture_commit=capture_commit,
            capture_tree=repository["capture_tree_oid"],
            origin_main=repository["origin_main_oid"],
            required_bindings=entries,
        )

    validate_v2_role5_payload(role5_payload, role_records)
    reviewed = {
        item["role"]: item for item in role5_payload["reviewed_v2_inputs"]
    }
    tools = payload["evidence_tool_bindings"]
    exact_keys(tools, V2_ROLE11_EVIDENCE_TOOL_KEYS, "evidence_tool_bindings")
    tool_roles = {
        "producer": "scheduler",
        "independent_checker": "release_builder",
        "focused_test": "test_adversarial",
    }
    for name, role in tool_roles.items():
        binding = _v2_role11_file_binding(
            tools[name], V2_ROLE11_TOOL_PATHS[name], f"evidence_tool_bindings.{name}"
        )
        role_entry = roles[role]
        role5_entry = reviewed.get(role)
        expected_subset = {
            key: role_entry[key] for key in V2_ROLE11_FILE_BINDING_KEYS
        }
        if (
            not exact_json_equal(binding, expected_subset)
            or role5_entry is None
            or role5_entry["path"] != binding["path"]
            or role5_entry["sha256"] != binding["sha256"]
        ):
            raise ProductionAuthorityError(
                f"V2 role 11 tool four-way binding mismatch: {name}"
            )

    results = payload["command_results"]
    if type(results) is not list or len(results) != 7:
        raise ProductionAuthorityError("V2 role 11 needs seven command results")
    validated_results: list[dict[str, Any]] = []
    parsed_counts: dict[str, dict[str, int]] = {}
    previous_started: datetime | None = None
    for index, result in enumerate(results):
        validated, counts = _v2_role11_command_result(
            result,
            index,
            authority_root=root,
            python_executable=python_executable,
            roles=roles,
        )
        started = _v2_role11_utc(
            validated["started_at_utc"], f"command_results[{index}].started_at_utc"
        )
        if previous_started is not None and started < previous_started:
            raise ProductionAuthorityError("V2 role 11 command timestamps reordered")
        if started > recorded_at:
            raise ProductionAuthorityError("V2 role 11 command starts after record")
        previous_started = started
        validated_results.append(validated)
        if counts is not None:
            parsed_counts[validated["name"]] = counts

    if role_records is not None:
        binary_record = role_records["branch_evaluator_binary"]
        device_id, inode = binary_record.stat_identity[:2]
        rebuild_receipt = validated_results[6]["semantic_receipt"]
        if any(
            rebuild_receipt[key] != expected
            for key, expected in (
                ("persistent_before_device_id", device_id),
                ("persistent_after_device_id", device_id),
                ("persistent_before_inode", inode),
                ("persistent_after_inode", inode),
            )
        ):
            raise ProductionAuthorityError(
                "V2 role 11 rebuild receipt is not bound to live role 17 inode"
            )
        binary_path = authority_project_file(root, binary_record.path)
        terminal_raw, terminal_info = read_pinned_regular_file(binary_path)
        if terminal_raw != binary_record.raw or (
            terminal_info.st_dev,
            terminal_info.st_ino,
            terminal_info.st_size,
            terminal_info.st_mtime_ns,
            terminal_info.st_ctime_ns,
        ) != binary_record.stat_identity:
            raise ProductionAuthorityError(
                "V2 role 11 live role 17 changed before terminal replay"
            )

    prerequisites = payload["prerequisite_bindings"]
    exact_keys(prerequisites, V2_ROLE11_PREREQUISITE_KEYS, "prerequisite_bindings")
    machine = prerequisites["machine_role10"]
    exact_keys(machine, V2_ROLE11_MACHINE_BINDING_KEYS, "machine_role10")
    for key in V2_PREFREEZE_INPUT_KEYS:
        if not exact_json_equal(machine[key], roles["machine_freeze"][key]):
            raise ProductionAuthorityError(f"machine_role10 mismatch: {key}")
    if machine["mode"] != "0644" or machine["nlink"] != 1:
        raise ProductionAuthorityError("machine_role10 mode/link mismatch")
    machine_publication_commit = _v2_role11_git_oid(
        machine["publication_commit_oid"], "machine_role10 publication commit"
    )
    _v2_git_validate_continuous_introduction(
        root,
        capture_commit=capture_commit,
        introduction_commit=machine_publication_commit,
        binding=machine,
        context="machine_role10 publication",
    )
    _v2_role11_relative(machine["producer_path"], "machine_role10 producer", expected=V2_ROLE11_TOOL_PATHS["producer"])
    _v2_role11_hash(machine["producer_sha256"], "machine_role10 producer hash", expected=roles["scheduler"]["sha256"])
    _v2_role11_relative(machine["verifier_path"], "machine_role10 verifier", expected=V2_ROLE11_TOOL_PATHS["independent_checker"])
    _v2_role11_hash(machine["verifier_sha256"], "machine_role10 verifier hash", expected=roles["release_builder"]["sha256"])
    _v2_role11_bool(machine["promotion_authorized"], "machine_role10 promotion", False)
    machine_receipt = _v2_role11_verify_receipt(
        machine["verify_receipt"],
        status_value="PASS_MACHINE_FREEZE_VERIFY_ONLY",
        candidate_sha256=machine["sha256"],
        size_bytes=machine["size_bytes"],
        context="machine_role10.verify_receipt",
    )
    if not exact_json_equal(machine_receipt, validated_results[0]["semantic_receipt"]):
        raise ProductionAuthorityError("machine receipt differs from command result")

    compatibility = prerequisites["s0_compatibility_role13"]
    exact_keys(compatibility, V2_ROLE11_S0_BINDING_KEYS, "s0_compatibility_role13")
    for key in V2_PREFREEZE_INPUT_KEYS:
        if not exact_json_equal(compatibility[key], roles["s0_compatibility"][key]):
            raise ProductionAuthorityError(f"s0 role13 mismatch: {key}")
    if compatibility["mode"] != "0644" or compatibility["nlink"] != 1:
        raise ProductionAuthorityError("s0 role13 mode/link mismatch")
    s0_publication_commit = _v2_role11_git_oid(
        compatibility["publication_commit_oid"], "s0 role13 publication commit"
    )
    _v2_git_validate_continuous_introduction(
        root,
        capture_commit=capture_commit,
        introduction_commit=s0_publication_commit,
        binding=compatibility,
        context="s0 role13 publication",
    )
    _v2_role11_relative(
        compatibility["producer_path"],
        "s0 role13 producer",
        expected=dict(FORMAL_INPUT_ROLES)["s0_adapter"],
    )
    _v2_role11_hash(
        compatibility["producer_sha256"],
        "s0 role13 producer hash",
        expected=roles["s0_adapter"]["sha256"],
    )
    _v2_role11_bool(compatibility["promotion_authorized"], "s0 role13 promotion", False)
    s0_receipt = _v2_role11_verify_receipt(
        compatibility["verify_receipt"],
        status_value="PASS_S0_COMPATIBILITY_VERIFY_ONLY",
        candidate_sha256=compatibility["sha256"],
        size_bytes=compatibility["size_bytes"],
        context="s0_compatibility_role13.verify_receipt",
    )
    if not exact_json_equal(s0_receipt, validated_results[1]["semantic_receipt"]):
        raise ProductionAuthorityError("s0 receipt differs from command result")

    absence = prerequisites["canonical_absence"]
    exact_keys(absence, V2_ROLE11_CANONICAL_ABSENCE_KEYS, "canonical_absence")
    for key in V2_ROLE11_CANONICAL_ABSENCE_KEYS:
        _v2_role11_bool(absence[key], f"canonical_absence.{key}", False)
    rebuild = prerequisites["second_fresh_rebuild_replay"]
    exact_keys(rebuild, V2_ROLE11_SECOND_REBUILD_REPLAY_KEYS, "second_fresh_rebuild_replay")
    _v2_role11_string(rebuild["command_result_name"], "second rebuild name", expected="second_fresh_rebuild")
    _v2_role11_hash(
        rebuild["command_result_sha256"],
        "second rebuild command hash",
        expected=sha256_bytes(canonical_json_bytes(validated_results[6])),
    )
    replay_receipt = _v2_role11_second_rebuild_receipt(
        rebuild["semantic_receipt"], roles, "second_fresh_rebuild_replay.semantic_receipt"
    )
    if not exact_json_equal(replay_receipt, validated_results[6]["semantic_receipt"]):
        raise ProductionAuthorityError("second rebuild receipt mismatch")

    totals = payload["test_totals"]
    exact_keys(totals, V2_ROLE11_TEST_TOTALS_KEYS, "test_totals")
    by_name = {result["name"]: result for result in validated_results}
    for result_name, total_name in V2_ROLE11_PYTEST_TOTAL_NAMES.items():
        total = totals[total_name]
        exact_keys(total, V2_ROLE11_TEST_TOTAL_KEYS, f"test_totals.{total_name}")
        for key, expected in parsed_counts[result_name].items():
            _v2_role11_int(total[key], f"test_totals.{total_name}.{key}", expected=expected)
        _v2_role11_int(
            total["wall_duration_ms"],
            f"test_totals.{total_name}.wall_duration_ms",
            expected=by_name[result_name]["wall_duration_ms"],
        )

    policy = payload["held_out_policy"]
    exact_keys(policy, V2_ROLE11_HELD_OUT_POLICY_KEYS, "held_out_policy")
    expected_policy = {
        "held_out_l3_scientific_outputs_read": False,
        "held_out_l3_evaluator_dispatched": False,
        "scientific_evaluator_dispatch_count": 0,
        "new_archive_scope": "TEMPORARY_MOCK_ONLY",
        "s0_archive_access": "READ_ONLY_SEALED_PUBLIC_SIX_CELL",
        "canonical_result_created": False,
    }
    if not exact_json_equal(policy, expected_policy):
        raise ProductionAuthorityError("V2 role 11 held-out policy mismatch")
    if not exact_json_equal(payload["covered_gates"], list(V2_ROLE11_COVERED_GATES)):
        raise ProductionAuthorityError("V2 role 11 covered-gates mismatch")
    encoded = canonical_json_bytes(payload)
    if len(encoded) > V2_ROLE11_MAX_CANDIDATE_BYTES:
        raise ProductionAuthorityError("V2 role 11 candidate exceeds byte cap")
    if require_live_absence:
        _v2_absence_replay(
            absence_records, "V2 role 11 current-stage absence"
        )
    return dict(payload)


def validate_v2_prefreeze_test_record_bytes(
    raw: bytes,
    **kwargs: Any,
) -> dict[str, Any]:
    if type(raw) is not bytes or not raw or len(raw) > V2_ROLE11_MAX_CANDIDATE_BYTES:
        raise ProductionAuthorityError("V2 role 11 candidate byte-size mismatch")
    try:
        payload = strict_json_loads(raw.decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("V2 role 11 candidate is not UTF-8") from error
    if raw != canonical_json_bytes(payload):
        raise StrictJSONError("V2 role 11 candidate is not CJ_COMPACT_V1")
    return validate_v2_prefreeze_test_record(payload, **kwargs)


def build_v2_prefreeze_test_record(
    *,
    recorded_at_utc: str,
    repository_snapshot: Mapping[str, Any],
    evidence_tool_bindings: Mapping[str, Any],
    pre_review_input_roles: Sequence[Mapping[str, Any]],
    prerequisite_bindings: Mapping[str, Any],
    command_results: Sequence[Mapping[str, Any]],
    authority_root: Path,
    python_executable: str,
    role5_payload: Mapping[str, Any],
    role_records: Mapping[str, FormalRoleRecord] | None = None,
    require_locked: bool = True,
    require_live_absence: bool = False,
) -> dict[str, Any]:
    """Assemble role 11 from internally captured facts, then replay it."""

    totals: dict[str, Any] = {}
    for result in command_results:
        if type(result) is dict and result.get("name") in V2_ROLE11_PYTEST_TOTAL_NAMES:
            name = V2_ROLE11_PYTEST_TOTAL_NAMES[result["name"]]
            counts = result.get("pytest_counts")
            if type(counts) is dict:
                totals[name] = {
                    **counts,
                    "wall_duration_ms": result.get("wall_duration_ms"),
                }
    payload = {
        "schema_version": 1,
        "protocol_id": V2_ROLE11_PROTOCOL_ID,
        "artifact_role": V2_ROLE11_ARTIFACT_ROLE,
        "artifact_status": V2_ROLE11_ARTIFACT_STATUS,
        "authority": V2_ROLE11_AUTHORITY,
        "recorded_at_utc": recorded_at_utc,
        "repository_snapshot": dict(repository_snapshot),
        "evidence_tool_bindings": dict(evidence_tool_bindings),
        "pre_review_input_roles": [dict(item) for item in pre_review_input_roles],
        "prerequisite_bindings": dict(prerequisite_bindings),
        "command_results": [dict(item) for item in command_results],
        "test_totals": totals,
        "covered_gates": list(V2_ROLE11_COVERED_GATES),
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
        "claim_boundary": V2_ROLE11_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    return validate_v2_prefreeze_test_record(
        payload,
        authority_root=authority_root,
        python_executable=python_executable,
        role5_payload=role5_payload,
        role_records=role_records,
        require_locked=require_locked,
        require_live_absence=require_live_absence,
    )


def _validate_v2_s0_compatibility_payload(
    project_root: Path,
    payload: Any,
    roles: Mapping[str, FormalRoleRecord],
) -> dict[str, Any]:
    """Replay all eighteen role-13 fields against nine sealed controls."""

    exact_keys(payload, V2_S0_COMPATIBILITY_KEYS, "V2 S0 compatibility")
    _v2_role11_int(payload["schema_version"], "V2 S0 schema", expected=1)
    expected_controls = {
        name: roles[role].sha256
        for name, role in V2_S0_CONTROL_ROLE_MAP.items()
    }
    expected_sources = {
        roles[role].path: roles[role].sha256
        for role in (
            "s0_adapter",
            "prefreeze_design",
            "checker_contract",
            "release_contract",
        )
    }
    expected_matrix = {
        "precisions": [128, 256],
        "slabs": ["S000", "S025", "S050"],
        "cell_count": 6,
    }
    if (
        payload["protocol_id"]
        != "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY"
        or payload["artifact_role"] != "S0_TO_A1_COMPATIBILITY_REPLAY"
        or payload["artifact_status"] != "NON_LICENSING"
        or payload["replay_status"] != "PASS_S0_COMPATIBILITY_REPLAY"
        or not exact_json_equal(payload["failures"], [])
        or payload["claim_boundary"] != V2_S0_COMPATIBILITY_CLAIM_BOUNDARY
        or not exact_json_equal(payload["matrix"], expected_matrix)
        or not exact_json_equal(payload["source_protocols"], V2_S0_SOURCE_PROTOCOLS)
        or not exact_json_equal(payload["static_facts"], V2_S0_STATIC_FACTS)
        or not exact_json_equal(payload["branch_facts"], V2_S0_BRANCH_FACTS)
        or not exact_json_equal(payload["composite_facts"], V2_S0_COMPOSITE_FACTS)
        or not exact_json_equal(payload["control_hashes"], expected_controls)
        or not exact_json_equal(payload["source_bindings"], expected_sources)
        or any(
            payload[key] is not None
            for key in ("milestone_status", "theorem_status", "final_status")
        )
    ):
        raise ProductionAuthorityError(
            "V2 S0 exact identity/facts/bindings mismatch"
        )
    for name, digest in expected_controls.items():
        _v2_role11_hash(digest, f"V2 S0 control {name}")
    for path, digest in expected_sources.items():
        safe_relative_path(path)
        _v2_role11_hash(digest, f"V2 S0 source {path}")

    controls: dict[str, Mapping[str, Any]] = {}
    for name, role in V2_S0_CONTROL_ROLE_MAP.items():
        record = roles[role]
        raw, info = read_pinned_regular_file(
            authority_project_file(project_root, record.path)
        )
        if (
            raw != record.raw
            or sha256_bytes(raw) != record.sha256
            or (
                info.st_dev,
                info.st_ino,
                info.st_size,
                info.st_mtime_ns,
                info.st_ctime_ns,
            ) != record.stat_identity
        ):
            raise ProductionAuthorityError(f"V2 S0 live control changed: {name}")
        try:
            control = strict_json_loads(raw.decode("utf-8"))
        except UnicodeError as error:
            raise StrictJSONError(f"V2 S0 control is not UTF-8: {name}") from error
        if type(control) is not dict:
            raise ProductionAuthorityError(f"V2 S0 control is not an object: {name}")
        controls[name] = control

    static_summary = controls["static_summary"]
    static_checker = controls["static_checker"]
    branch_manifest = controls["branch_manifest"]
    branch_checker = controls["branch_checker"]
    composite_manifest = controls["composite_manifest"]
    composite_checker = controls["composite_checker"]
    if (
        static_summary.get("totals", {}).get("node_count") != 84172
        or static_summary.get("totals", {}).get("internal_count") != 42074
        or static_summary.get("totals", {}).get("terminal_count") != 42098
        or static_summary.get("totals", {}).get("unresolved_count") != 0
        or static_checker.get("independent_interval_checks") != 122300
        or branch_checker.get("raw_replay_count") != 6
        or branch_checker.get("manifest_file_count") != 26
        or composite_checker.get("cell_replay_count") != 6
        or composite_checker.get("manifest_binding_count") != 18
        or not exact_json_equal(composite_checker.get("failures"), [])
    ):
        raise ProductionAuthorityError(
            "V2 S0 sealed control facts disagree with role13"
        )

    role_sets = payload["role_sets"]
    exact_keys(
        role_sets,
        {
            "static_proof_entries",
            "branch_manifest_roles",
            "composite_manifest_roles",
            "composite_component_roles",
        },
        "V2 S0 role sets",
    )
    proofs = static_summary.get("proofs")
    if (
        type(proofs) is not list
        or len(proofs) != 6
        or not exact_json_equal(role_sets["static_proof_entries"], proofs)
    ):
        raise ProductionAuthorityError("V2 S0 six static proof roles mismatch")
    expected_pairs = tuple(
        (precision, slab)
        for precision in (128, 256)
        for slab in ("S000", "S025", "S050")
    )
    for index, (entry, pair) in enumerate(zip(proofs, expected_pairs, strict=True)):
        exact_keys(entry, V2_S0_STATIC_ENTRY_KEYS, f"V2 S0 static proof {index}")
        if (
            entry["precision_bits"] != pair[0]
            or type(entry["precision_bits"]) is not int
            or entry["slab_id"] != pair[1]
            or entry["path"] != f"proof_{pair[0]}_{pair[1]}.json"
        ):
            raise ProductionAuthorityError(
                "V2 S0 static proof identity/order mismatch"
            )
        safe_relative_path(entry["path"])
        _v2_role11_hash(entry["sha256"], f"V2 S0 static proof {index} hash")
        _v2_role11_int(
            entry["size_bytes"], f"V2 S0 static proof {index} size", minimum=1
        )
        nodes = _v2_role11_int(
            entry["node_count"], f"V2 S0 static proof {index} nodes", minimum=1
        )
        internal = _v2_role11_int(
            entry["internal_count"], f"V2 S0 static proof {index} internal"
        )
        terminal = _v2_role11_int(
            entry["terminal_count"], f"V2 S0 static proof {index} terminal", minimum=1
        )
        _v2_role11_int(
            entry["unresolved_count"],
            f"V2 S0 static proof {index} unresolved",
            expected=0,
        )
        if nodes != internal + terminal:
            raise ProductionAuthorityError(
                "V2 S0 static proof count conservation failed"
            )
        tree_hashes = entry["tree_content_sha256"]
        exact_keys(
            tree_hashes,
            {"ANGLE", "SECTION_HIGH", "SECTION_LOW", "SECTION_WINDOW"},
            f"V2 S0 static proof {index} tree hashes",
        )
        for tree, digest in tree_hashes.items():
            _v2_role11_hash(
                digest, f"V2 S0 proof {index} tree {tree}"
            )

    branch_files = branch_manifest.get("files")
    if type(branch_files) is not dict:
        raise ProductionAuthorityError(
            "V2 S0 branch manifest files is not an object"
        )
    prefix = f"{project_root}/"
    branch_roles: list[str] = []
    for absolute in branch_files:
        if type(absolute) is not str or not absolute.startswith(prefix):
            raise ProductionAuthorityError(
                "V2 S0 branch manifest path escapes authority root"
            )
        relative = absolute[len(prefix):]
        safe_relative_path(relative)
        branch_roles.append(relative)
    if not exact_json_equal(role_sets["branch_manifest_roles"], branch_roles):
        raise ProductionAuthorityError(
            "V2 S0 ordered branch manifest roles mismatch"
        )

    composite_files = composite_manifest.get("files")
    component_files = composite_manifest.get("component_files")
    if type(composite_files) is not list or type(component_files) is not list:
        raise ProductionAuthorityError(
            "V2 S0 composite manifest role arrays missing"
        )
    expected_composite = [
        {"scope": row.get("scope"), "path": row.get("path")}
        for row in composite_files
        if type(row) is dict
    ]
    expected_components = [
        {"component": row.get("component"), "path": row.get("path")}
        for row in component_files
        if type(row) is dict
    ]
    if (
        len(expected_composite) != len(composite_files)
        or len(expected_components) != len(component_files)
        or not exact_json_equal(
            role_sets["composite_manifest_roles"], expected_composite
        )
        or not exact_json_equal(
            role_sets["composite_component_roles"], expected_components
        )
    ):
        raise ProductionAuthorityError("V2 S0 composite role sets mismatch")
    for row in expected_composite:
        exact_keys(row, {"scope", "path"}, "V2 S0 composite manifest role")
        if row["scope"] not in ("ROOT", "OUTPUT"):
            raise ProductionAuthorityError("V2 S0 composite role scope mismatch")
        safe_relative_path(row["path"])
    for row in expected_components:
        exact_keys(row, {"component", "path"}, "V2 S0 component role")
        if row["component"] not in ("static", "branch"):
            raise ProductionAuthorityError(
                "V2 S0 component role identity mismatch"
            )
        safe_relative_path(row["path"])
    return {
        "replay_sha256": roles["s0_compatibility"].sha256,
        "control_hashes": expected_controls,
    }


def _v2_role11_capture_inputs(
    root: Path,
) -> tuple[
    tuple[FormalRoleRecord, ...],
    list[dict[str, Any]],
    dict[str, bytes],
    dict[str, Any],
    dict[str, Any],
]:
    records: list[FormalRoleRecord] = []
    entries: list[dict[str, Any]] = []
    images: dict[str, bytes] = {}
    for role, relative in V2_ROLE11_PRE_REVIEW_ROLES:
        record, raw = formal_role_binding(root, role, relative)
        live_raw, info = read_pinned_regular_file(
            authority_project_file(root, relative)
        )
        if live_raw != raw:
            raise ProductionAuthorityError(f"role-11 input raced: {role}")
        records.append(record)
        images[role] = raw
        entries.append({
            "role": role,
            "path": relative,
            "sha256": record.sha256,
            "size_bytes": len(raw),
            "mode": f"{stat.S_IMODE(info.st_mode):04o}",
            "nlink": info.st_nlink,
        })
    by_role = {record.role: record for record in records}
    try:
        role5 = strict_json_loads(
            images["implementation_design_review"].decode("utf-8")
        )
        machine_payload = strict_json_loads(images["machine_freeze"].decode("utf-8"))
        role13 = strict_json_loads(images["s0_compatibility"].decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("role-11 prerequisite JSON is not UTF-8") from error
    for role, payload in (
        ("implementation_design_review", role5),
        ("machine_freeze", machine_payload),
        ("s0_compatibility", role13),
    ):
        if images[role] != canonical_json_bytes(payload):
            raise StrictJSONError(f"role-11 prerequisite is noncanonical: {role}")
    validate_v2_role5_repository_bindings(role5, root, by_role)
    machine = _validate_formal_machine_envelope(machine_payload)
    _validate_v2_s0_compatibility_payload(root, role13, by_role)
    return tuple(records), entries, images, role5, machine


def _v2_role11_command_capture(
    index: int,
    argv: Sequence[str],
    roles: Mapping[str, Mapping[str, Any]],
    root: Path,
) -> dict[str, Any]:
    started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    start_ns = time.monotonic_ns()
    completed = _capture_command(
        argv,
        cwd=root,
        environment=V2_ROLE11_ENVIRONMENT,
        timeout_seconds=600,
        umask=0o022,
    )
    wall_duration_ms = max(1, (time.monotonic_ns() - start_ns + 999999) // 1000000)
    try:
        stdout = completed.stdout.decode("utf-8", errors="strict")
        stderr = completed.stderr.decode("utf-8", errors="strict")
    except UnicodeError as error:
        raise ProductionAuthorityError("role-11 command transcript is not UTF-8") from error
    name = V2_ROLE11_COMMAND_NAMES[index]
    pytest_counts: dict[str, int] | None = None
    semantic_receipt: dict[str, Any] | None = None
    if name in V2_ROLE11_PYTEST_TOTAL_NAMES:
        pytest_counts = _v2_role11_pytest_counts(stdout, f"captured {name}")
    elif name in {"role24_machine_verify", "role13_compatibility_verify"}:
        role = roles[
            "machine_freeze" if name == "role24_machine_verify" else "s0_compatibility"
        ]
        semantic_receipt = {
            "verification_status": (
                "PASS_MACHINE_FREEZE_VERIFY_ONLY"
                if name == "role24_machine_verify"
                else "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
            ),
            "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
            "candidate_sha256": role["sha256"],
            "size_bytes": role["size_bytes"],
            "promotion_authorized": False,
        }
    elif name == "second_fresh_rebuild":
        try:
            semantic_receipt = strict_json_loads(completed.stdout.decode("utf-8"))
        except UnicodeError as error:
            raise StrictJSONError("second rebuild receipt is not UTF-8") from error
        if completed.stdout != canonical_json_bytes(semantic_receipt):
            raise StrictJSONError("second rebuild receipt is not canonical JSON")
    return {
        "name": name,
        "kind": V2_ROLE11_COMMAND_KINDS[index],
        "argv": list(argv),
        "cwd": os.fspath(root),
        "environment": dict(V2_ROLE11_ENVIRONMENT),
        "return_code": completed.returncode,
        "started_at_utc": started_at,
        "wall_duration_ms": wall_duration_ms,
        "stdout_utf8": stdout,
        "stdout_sha256": sha256_bytes(completed.stdout),
        "stdout_size_bytes": len(completed.stdout),
        "stderr_utf8": stderr,
        "stderr_sha256": sha256_bytes(completed.stderr),
        "stderr_size_bytes": len(completed.stderr),
        "pytest_counts": pytest_counts,
        "semantic_receipt": semantic_receipt,
    }


def _v2_remove_owned_candidate(
    path: Path, identity: V2PrivateCandidateImage
) -> None:
    parent_fd = _open_directory_fd(path.parent)
    try:
        _replay_machine_publication_directory(
            path.parent,
            parent_fd,
            identity.parent_chain,
            "private candidate cleanup parent",
        )
        parent = os.fstat(parent_fd)
        if (
            parent.st_dev,
            parent.st_ino,
            parent.st_mode,
            parent.st_nlink,
        ) != (
            identity.parent_device_id,
            identity.parent_inode,
            identity.parent_mode,
            identity.parent_nlink,
        ):
            raise PathContractError(
                "refusing to remove candidate through a substituted parent"
            )
        try:
            entry = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            return
        if (entry.st_dev, entry.st_ino) != (
            identity.device_id,
            identity.inode,
        ):
            raise PathContractError("refusing to remove substituted private candidate")
        os.unlink(path.name, dir_fd=parent_fd)
        os.fsync(parent_fd)
        try:
            os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PathContractError("private candidate remained after owned cleanup")
    finally:
        os.close(parent_fd)


def capture_v2_prefreeze_test_candidate(
    output_value: str,
    authority_root: Path | str = ROOT,
) -> tuple[dict[str, Any], str]:
    """Run the fixed engineering evidence capture into one private candidate."""

    _require_v2_role11_mechanical_lock()
    root = safe_absolute_path(os.fspath(authority_root), "role-11 authority root")
    output = _v2_private_candidate_path(output_value, "role-11 candidate output")
    absence = _v2_absence_snapshot(
        (
            root / dict(FORMAL_INPUT_ROLES)["prefreeze_tests"],
            root / dict(FORMAL_INPUT_ROLES)["prefreeze_review"],
            root / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json",
            root / "results/r401_val_l3_a1_v2_all_slabs",
            root / "results/r401_val_l3_a1_v2_all_slabs.operational",
        ),
        "V2 role 11 capture absence",
    )
    records, entries, images, role5, machine = _v2_role11_capture_inputs(root)
    roles = {entry["role"]: entry for entry in entries}
    repository_root, _git_dir, _prefix = _v2_git_roots(root)
    capture_commit = _v2_git_ref(root, "refs/heads/main")
    capture_tree = _v2_git_commit_tree(root, capture_commit)
    origin_main = _v2_git_ref(root, "refs/remotes/origin/main")
    live_remote = _v2_role11_repository_probes(root)
    if capture_commit != origin_main or capture_commit != live_remote:
        raise ProductionAuthorityError("role-11 preprobe commit/origin/live mismatch")
    _v2_git_validate_current_repository(
        root,
        capture_commit=capture_commit,
        capture_tree=capture_tree,
        origin_main=origin_main,
        required_bindings=entries,
    )
    repository_snapshot = {
        "authority_root": os.fspath(root),
        "branch": "main",
        "capture_commit_oid": capture_commit,
        "capture_tree_oid": capture_tree,
        "origin_url": _v2_git_origin_url(root),
        "origin_main_oid": origin_main,
        "live_remote_main_oid": live_remote,
        "head_equals_origin_main": True,
        "head_equals_live_remote_main": True,
        "ahead": 0,
        "behind": 0,
        "worktree_clean_before": True,
        "worktree_clean_after": True,
    }
    python_executable = machine["python_arb"]["executable_path"]
    rebuild_parent = Path(
        "/tmp/a416-l3a1-v2-role11-rebuild." + os.urandom(8).hex()
    )
    os.mkdir(rebuild_parent, 0o700)
    rebuild_output = os.fspath(
        rebuild_parent / "capd_r401_phase_branch_tube_mp_a1"
    )
    argv_rows = v2_role11_fixed_command_argv(
        root, python_executable, rebuild_output=rebuild_output
    )
    command_results: list[dict[str, Any]] = []
    try:
        for index, argv in enumerate(argv_rows):
            command_results.append(
                _v2_role11_command_capture(index, argv, roles, root)
            )
    finally:
        if rebuild_parent.exists():
            try:
                if not tuple(os.scandir(rebuild_parent)):
                    os.rmdir(rebuild_parent)
            except OSError:
                pass
    post_live = _v2_role11_repository_probes(root)
    if post_live != capture_commit:
        raise ProductionAuthorityError("role-11 postprobe live remote changed")
    _v2_git_validate_current_repository(
        root,
        capture_commit=capture_commit,
        capture_tree=capture_tree,
        origin_main=origin_main,
        required_bindings=entries,
    )
    evidence_tools = {
        name: {
            key: roles[role][key] for key in V2_ROLE11_FILE_BINDING_KEYS
        }
        for name, role in (
            ("producer", "scheduler"),
            ("independent_checker", "release_builder"),
            ("focused_test", "test_adversarial"),
        )
    }
    machine_receipt = command_results[0]["semantic_receipt"]
    s0_receipt = command_results[1]["semantic_receipt"]
    rebuild_receipt = command_results[6]["semantic_receipt"]
    machine_publication_commit = _v2_git_find_continuous_introduction(
        root,
        capture_commit=capture_commit,
        binding=roles["machine_freeze"],
        context="role-11 machine role10 publication history",
    )
    s0_publication_commit = _v2_git_find_continuous_introduction(
        root,
        capture_commit=capture_commit,
        binding=roles["s0_compatibility"],
        context="role-11 S0 role13 publication history",
    )
    prerequisites = {
        "machine_role10": {
            **roles["machine_freeze"],
            "publication_commit_oid": machine_publication_commit,
            "producer_path": V2_ROLE11_TOOL_PATHS["producer"],
            "producer_sha256": roles["scheduler"]["sha256"],
            "verifier_path": V2_ROLE11_TOOL_PATHS["independent_checker"],
            "verifier_sha256": roles["release_builder"]["sha256"],
            "verify_receipt": machine_receipt,
            "promotion_authorized": False,
        },
        "s0_compatibility_role13": {
            **roles["s0_compatibility"],
            "publication_commit_oid": s0_publication_commit,
            "producer_path": roles["s0_adapter"]["path"],
            "producer_sha256": roles["s0_adapter"]["sha256"],
            "verify_receipt": s0_receipt,
            "promotion_authorized": False,
        },
        "second_fresh_rebuild_replay": {
            "command_result_name": "second_fresh_rebuild",
            "command_result_sha256": sha256_bytes(
                canonical_json_bytes(command_results[6])
            ),
            "semantic_receipt": rebuild_receipt,
        },
        "canonical_absence": {
            "prefreeze_review_role12_exists": False,
            "main_freeze_role54_exists": False,
            "canonical_result_root_exists": False,
            "canonical_operational_root_exists": False,
        },
    }
    payload = build_v2_prefreeze_test_record(
        recorded_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        repository_snapshot=repository_snapshot,
        evidence_tool_bindings=evidence_tools,
        pre_review_input_roles=entries,
        prerequisite_bindings=prerequisites,
        command_results=command_results,
        authority_root=root,
        python_executable=python_executable,
        role5_payload=role5,
        role_records={record.role: record for record in records},
        require_locked=True,
        require_live_absence=True,
    )
    raw = canonical_json_bytes(payload)
    owned_identity: V2PrivateCandidateImage | None = None
    try:
        owned_identity = _v2_write_private_candidate(
            output,
            raw,
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
            context="role-11 candidate output",
        )
        terminal_live = _v2_role11_repository_probes(root)
        terminal_records, terminal_entries, terminal_images, terminal_role5, _ = (
            _v2_role11_capture_inputs(root)
        )
        if (
            terminal_live != capture_commit
            or terminal_records != records
            or not exact_json_equal(terminal_entries, entries)
            or terminal_images != images
            or not exact_json_equal(terminal_role5, role5)
        ):
            raise ProductionAuthorityError("role-11 terminal input replay mismatch")
        _v2_git_validate_current_repository(
            root,
            capture_commit=capture_commit,
            capture_tree=capture_tree,
            origin_main=origin_main,
            required_bindings=entries,
        )
        _v2_absence_replay(absence, "V2 role 11 capture absence")
        _v2_replay_private_candidate(
            output,
            owned_identity,
            context="role-11 terminal candidate replay",
        )
        # The earlier probe precedes several long pure-Git/input replays.  A
        # final live/status observation closes that interval, and the fast
        # candidate replay after it closes the probe-to-return interval.
        if _v2_role11_repository_probes(root) != capture_commit:
            raise ProductionAuthorityError(
                "role-11 final capture repository probe mismatch"
            )
        _v2_replay_private_candidate(
            output,
            owned_identity,
            context="role-11 final postprobe candidate replay",
        )
    except BaseException:
        if owned_identity is not None:
            _v2_remove_owned_candidate(output, owned_identity)
        raise
    return payload, sha256_bytes(raw)


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
    by_role = {item.role: item for item in bindings}
    try:
        role5 = strict_json_loads(images["implementation_design_review"].decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("V2 role 5 is not UTF-8") from error
    if images["implementation_design_review"] != canonical_json_bytes(role5):
        raise StrictJSONError("V2 role 5 is not canonical JSON")
    validate_v2_role5_repository_bindings(role5, root, by_role)
    try:
        machine_payload = strict_json_loads(images["machine_freeze"].decode("utf-8"))
        role11 = strict_json_loads(images["prefreeze_tests"].decode("utf-8"))
        role13 = strict_json_loads(images["s0_compatibility"].decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("V2 role 10, 11, or 13 is not UTF-8") from error
    for role_name, payload in (
        ("machine_freeze", machine_payload),
        ("prefreeze_tests", role11),
        ("s0_compatibility", role13),
    ):
        if images[role_name] != canonical_json_bytes(payload):
            raise StrictJSONError(f"V2 {role_name} is not canonical JSON")
    machine = _validate_formal_machine_envelope(machine_payload)
    validate_v2_prefreeze_test_record(
        role11,
        authority_root=root,
        python_executable=machine["python_arb"]["executable_path"],
        role5_payload=role5,
        role_records=by_role,
        require_locked=True,
        require_live_absence=False,
    )
    _validate_v2_s0_compatibility_payload(root, role13, by_role)
    if images["prefreeze_review"] != b"Verdict: ACCEPT_FOR_FREEZE\n":
        raise ProductionAuthorityError("V2 role 12 is not the exact 27-byte verdict")
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
        "authoritative_relative": "results/r401_val_l3_a1_v2_all_slabs",
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
    """Return the complete environment used by the fresh deterministic build."""

    return {
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PATH": "/usr/bin:/bin",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONNOUSERSITE": "1",
        "TZ": "UTC",
    }


def formal_capd_flag_tokens(checkout_path: str) -> list[str]:
    """Return the exact ordered 20-token CAPD compile/link ABI."""

    checkout = str(safe_absolute_path(checkout_path, "CAPD checkout"))
    return [
        "-std=c++17", "-O2", "-frounding-math", "-D__USE_FILIB__",
        "-D__HAVE_MPFR__", "-O2", "-frounding-math", "-DFILIB_EXTENDED",
        "-DFILIB_HAVE_SSE", f"-I{checkout}/capdDynSys/include",
        f"-I{checkout}/capdAlg/include", f"-I{checkout}/capdAux/include",
        f"-I{checkout}/capdExt/include", f"-I{checkout}/capdExt/filibsrc",
        f"-L{checkout}/build-mp", f"-L{checkout}/build-mp/capdExt/filibsrc",
        "-lcapd", "-lfilib", "-lmpfr", "-lgmp",
    ]


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
    exact_keys(
        compiler["build_recipe"], MACHINE_BUILD_RECIPE_KEYS,
        "machine build recipe",
    )
    exact_keys(
        compiler["fresh_rebuild_receipt"],
        MACHINE_FRESH_REBUILD_RECEIPT_KEYS,
        "machine fresh rebuild receipt",
    )
    exact_keys(
        compiler["transfer_evidence"], MACHINE_TRANSFER_EVIDENCE_KEYS,
        "machine build transfer evidence",
    )
    build_recipe = compiler["build_recipe"]
    fresh_receipt = compiler["fresh_rebuild_receipt"]
    transfer = compiler["transfer_evidence"]
    for context, record in (
        ("machine build recipe", build_recipe),
        ("machine fresh rebuild receipt", fresh_receipt),
    ):
        safe_absolute_path(record["cwd"], f"{context} cwd")
        if not exact_json_equal(record["environment"], formal_build_environment()):
            raise ProductionAuthorityError(f"{context} environment mismatch")
        if record["umask"] != "0022":
            raise ProductionAuthorityError(f"{context} umask mismatch")
    if build_recipe["staging_output_token"] != "@STAGING_BINARY@":
        raise ProductionAuthorityError("machine build recipe staging token mismatch")
    argv_template = build_recipe["argv_template"]
    if (
        type(argv_template) is not list
        or not argv_template
        or not all(type(item) is str and item for item in argv_template)
        or argv_template[-1] != build_recipe["staging_output_token"]
        or argv_template.count(build_recipe["staging_output_token"]) != 1
        or build_recipe["argv_template_sha256"]
        != sha256_bytes(canonical_json_bytes(argv_template))
    ):
        raise ProductionAuthorityError("machine build recipe template is malformed")
    staging_directory = safe_absolute_path(
        fresh_receipt["staging_directory"], "fresh build staging directory"
    )
    staging_output = safe_absolute_path(
        fresh_receipt["staging_output_path"], "fresh build staging output"
    )
    if (
        staging_directory.parts[:2] != ("/", "tmp")
        or staging_directory.parent != Path("/tmp")
        or staging_output.parent != staging_directory
        or staging_output.name != "capd_r401_phase_branch_tube_mp_a1"
        or is_within(staging_directory, project_root_for_capture)
    ):
        raise ProductionAuthorityError("fresh build staging namespace mismatch")
    actual_argv = fresh_receipt["argv"]
    if (
        type(actual_argv) is not list
        or not all(type(item) is str and item for item in actual_argv)
        or actual_argv != [*argv_template[:-1], str(staging_output)]
        or fresh_receipt["argv_sha256"]
        != sha256_bytes(canonical_json_bytes(actual_argv))
    ):
        raise ProductionAuthorityError("fresh build actual argv mismatch")
    for key in ("stdout", "stderr"):
        if type(fresh_receipt[key]) is not str:
            raise ProductionAuthorityError(
                f"fresh_rebuild_receipt.{key} must be exact UTF-8 text"
            )
    for key in (
        "output_size_bytes", "output_mode",
    ):
        exact_int(fresh_receipt[key], f"fresh_rebuild_receipt.{key}", minimum=1)
    for key in (
        "output_sha256", "output_dt_needed_sha256", "argv_sha256",
        "stdout_sha256", "stderr_sha256",
    ):
        _exact_sha(fresh_receipt[key], f"fresh_rebuild_receipt.{key}")
    if (
        fresh_receipt["stdout_sha256"]
        != sha256_bytes(fresh_receipt["stdout"].encode("utf-8"))
        or fresh_receipt["stderr_sha256"]
        != sha256_bytes(fresh_receipt["stderr"].encode("utf-8"))
        or fresh_receipt["stdout"] != ""
        or fresh_receipt["stderr"] != ""
        or type(fresh_receipt["return_code"]) is not int
        or fresh_receipt["return_code"] != 0
        or fresh_receipt["output_mode"] != 0o755
        or type(fresh_receipt["output_build_id"]) is not str
        or re.fullmatch(r"[0-9a-f]{40}", fresh_receipt["output_build_id"])
        is None
        or fresh_receipt["output_soname"] is not None
        or fresh_receipt["shell_used"] is not False
        or type(fresh_receipt["output_dt_needed"]) is not list
        or fresh_receipt["output_dt_needed"]
        != sorted(set(fresh_receipt["output_dt_needed"]))
        or fresh_receipt["output_dt_needed_sha256"]
        != sha256_bytes(canonical_json_bytes(fresh_receipt["output_dt_needed"]))
    ):
        raise ProductionAuthorityError("machine fresh rebuild receipt mismatch")
    for key in (
        "staging_output_size_bytes", "staging_output_mode",
        "persistent_before_size_bytes", "persistent_before_mode",
        "persistent_before_device_id", "persistent_before_inode",
        "persistent_after_size_bytes", "persistent_after_mode",
        "persistent_after_device_id", "persistent_after_inode",
    ):
        exact_int(transfer[key], f"transfer_evidence.{key}", minimum=1)
    for key in (
        "branch_calibration_binary_sha256", "staging_output_sha256",
        "persistent_before_sha256", "persistent_after_sha256",
    ):
        _exact_sha(transfer[key], f"transfer_evidence.{key}")
    for key in (
        "byte_for_byte_equal", "persistent_identity_unchanged",
        "persistent_overwrite_performed",
    ):
        if type(transfer[key]) is not bool:
            raise ProductionAuthorityError(f"transfer_evidence.{key} must be Boolean")
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
    expected_capd_tokens = formal_capd_flag_tokens(checkout)
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
    expected_build_template = [
        compiler["executable_path"], "-Wall", "-Wextra", "-Wpedantic", "-Werror",
        str(Path(project_root) / binary["source_path"]), *capd_tokens,
        "-o", "@STAGING_BINARY@",
    ]
    if (
        build_recipe["cwd"] != project_root
        or fresh_receipt["cwd"] != project_root
        or not exact_json_equal(
            build_recipe["argv_template"], expected_build_template
        )
        or not exact_json_equal(
            fresh_receipt["argv"],
            [*expected_build_template[:-1], fresh_receipt["staging_output_path"]],
        )
        or fresh_receipt["output_sha256"] != binary["sha256"]
        or fresh_receipt["output_size_bytes"] != binary["size_bytes"]
        or fresh_receipt["output_mode"] != binary["executable_mode"]
        or fresh_receipt["output_build_id"] != binary["build_id"]
        or fresh_receipt["output_dt_needed"] != binary["dt_needed"]
    ):
        raise ProductionAuthorityError(
            "machine fresh build recipe/receipt differs from branch binary"
        )
    persistent_identity = (live_binary_info.st_dev, live_binary_info.st_ino)
    if (
        transfer["staging_output_sha256"] != binary["sha256"]
        or transfer["staging_output_size_bytes"] != binary["size_bytes"]
        or transfer["staging_output_mode"] != binary["executable_mode"]
        or transfer["persistent_before_sha256"] != binary["sha256"]
        or transfer["persistent_before_size_bytes"] != binary["size_bytes"]
        or transfer["persistent_before_mode"] != binary["executable_mode"]
        or (
            transfer["persistent_before_device_id"],
            transfer["persistent_before_inode"],
        )
        != persistent_identity
        or transfer["persistent_after_sha256"] != binary["sha256"]
        or transfer["persistent_after_size_bytes"] != binary["size_bytes"]
        or transfer["persistent_after_mode"] != binary["executable_mode"]
        or (
            transfer["persistent_after_device_id"],
            transfer["persistent_after_inode"],
        )
        != persistent_identity
        or transfer["byte_for_byte_equal"] is not True
        or transfer["persistent_identity_unchanged"] is not True
        or transfer["persistent_overwrite_performed"] is not False
    ):
        raise ProductionAuthorityError(
            "fresh staging/persistent byte-transfer evidence mismatch"
        )
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
    if (
        transfer["branch_calibration_binary_sha256"]
        != branch_payload["binary_sha256"]
        or transfer["branch_calibration_binary_sha256"] != binary["sha256"]
    ):
        raise ProductionAuthorityError(
            "branch calibration/fresh build/persistent transfer mismatch"
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


def _exact_json_clone(payload: Any) -> Any:
    """Clone one exact JSON value without consulting filesystem state."""

    return strict_json_loads(canonical_json_bytes(payload).decode("utf-8"))


def build_formal_machine_freeze_candidate(
    *,
    captured_at_utc: str,
    capture_tool_sha256: str,
    boot_id_sha256: str,
    machine_observations: Mapping[str, Any],
    python_arb: Mapping[str, Any],
    capd: Mapping[str, Any],
    compiler: Mapping[str, Any],
    branch_binary: Mapping[str, Any],
    runtime_libraries: Mapping[str, Any],
    static_payload_raw: bytes,
    branch_payload_raw: bytes,
    filesystem: Mapping[str, Any],
) -> dict[str, Any]:
    """Purely assemble one exact, non-self-authorizing machine candidate.

    This function performs no reads, writes, subprocess execution, clock access,
    or scientific dispatch.  Its inputs are already-captured observations.  The
    live capture wrapper below separately validates every byte image and only
    then publishes the returned CJ_COMPACT_V1 image to a noncanonical /tmp
    target.
    """

    if type(static_payload_raw) is not bytes or type(branch_payload_raw) is not bytes:
        raise StrictJSONError("machine resource evidence must be exact byte images")
    try:
        static_text = static_payload_raw.decode("utf-8")
        branch_text = branch_payload_raw.decode("utf-8")
    except UnicodeError as error:
        raise StrictJSONError("machine resource evidence is not UTF-8") from error
    static_payload = strict_json_loads(static_text)
    branch_payload = strict_json_loads(branch_text)
    if static_payload_raw != canonical_json_bytes(static_payload):
        raise StrictJSONError("static calibration is not CJ_COMPACT_V1")
    if branch_payload_raw != pretty_json_bytes(branch_payload):
        raise StrictJSONError("branch calibration is not CJ_PRETTY_2_V1")
    exact_keys(static_payload, STATIC_RESOURCE_PAYLOAD_KEYS, "static calibration")
    exact_keys(branch_payload, BRANCH_RESOURCE_PAYLOAD_KEYS, "branch calibration")

    _exact_utc_timestamp(captured_at_utc, "machine capture timestamp")
    _exact_sha(capture_tool_sha256, "machine capture tool hash")
    _exact_sha(boot_id_sha256, "machine boot ID hash")
    exact_keys(dict(machine_observations), MACHINE_OBSERVATION_KEYS, "machine observations")
    _exact_positive_ints(machine_observations, "machine observations")
    exact_keys(dict(python_arb), MACHINE_PYTHON_ARB_KEYS, "machine python_arb")
    exact_keys(dict(capd), MACHINE_CAPD_KEYS, "machine CAPD")
    exact_keys(dict(compiler), MACHINE_COMPILER_KEYS, "machine compiler")
    exact_keys(dict(branch_binary), MACHINE_BRANCH_BINARY_KEYS, "machine branch binary")
    exact_keys(dict(runtime_libraries), MACHINE_RUNTIME_LIBRARIES_KEYS, "machine runtime libraries")
    exact_keys(dict(filesystem), MACHINE_FILESYSTEM_KEYS, "machine filesystem")

    requirements = formal_machine_requirements()
    observations = _exact_json_clone(dict(machine_observations))
    static_baseline = static_payload["admission"]["idle_baseline_bytes"]
    branch_baseline = branch_payload["admission"]["baseline_bytes"]
    static_peak = static_payload["admission"]["representative_peak_rss_bytes"]
    branch_peak = branch_payload["admission"]["peak_rss_bytes"]
    if (
        type(static_baseline) is not int
        or type(branch_baseline) is not int
        or type(static_peak) is not int
        or type(branch_peak) is not int
        or min(static_baseline, branch_baseline, static_peak, branch_peak) <= 0
    ):
        raise ProductionAuthorityError("resource calibration metrics are malformed")
    if (
        observations["idle_baseline_rss_bytes"]
        != max(static_baseline, branch_baseline)
        or observations["representative_static_peak_rss_bytes"] != static_peak
        or observations["representative_branch_peak_rss_bytes"] != branch_peak
        or observations["logical_cpu_count"] != requirements["logical_cpu_count"]
        or observations["memory_limit_bytes"] != requirements["memory_limit_bytes"]
    ):
        raise ProductionAuthorityError(
            "machine observations do not exactly transfer calibration/live policy"
        )
    static_required = (
        observations["idle_baseline_rss_bytes"]
        + requirements["static_workers"] * static_peak
        + requirements["reserve_bytes"]
    )
    branch_required = (
        observations["idle_baseline_rss_bytes"]
        + requirements["branch_workers"] * branch_peak
        + requirements["reserve_bytes"]
    )
    admission_limit = requirements["memory_admission_limit_bytes"]
    resource_admission = {
        "static_required_bytes": static_required,
        "branch_required_bytes": branch_required,
        "admitted_required_bytes": max(static_required, branch_required),
        "admission_limit_bytes": admission_limit,
        "static_inequality_passed": static_required <= admission_limit,
        "branch_inequality_passed": branch_required <= admission_limit,
        "storage_launch_passed": (
            observations["result_parent_free_bytes"]
            >= requirements["launch_free_bytes"]
        ),
    }
    if not all(
        resource_admission[key]
        for key in (
            "static_inequality_passed",
            "branch_inequality_passed",
            "storage_launch_passed",
        )
    ):
        raise ProductionAuthorityError("machine candidate failed resource admission")

    branch_sha = branch_binary["sha256"]
    _exact_sha(branch_sha, "machine branch binary hash")
    if branch_payload["binary_sha256"] != branch_sha:
        raise ProductionAuthorityError(
            "branch calibration is stale relative to the persistent binary"
        )
    candidate = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MACHINE_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "MACHINE_ADMISSION_ONLY",
        "scientific_licensing_enabled": True,
        "production_authorized": False,
        "capture": {
            "captured_at_utc": captured_at_utc,
            "capture_tool_path": dict(FORMAL_INPUT_ROLES)["scheduler"],
            "capture_tool_sha256": capture_tool_sha256,
            "boot_id_sha256": boot_id_sha256,
        },
        "machine_requirements": requirements,
        "machine_observations": observations,
        "python_arb": _exact_json_clone(dict(python_arb)),
        "capd": _exact_json_clone(dict(capd)),
        "compiler": _exact_json_clone(dict(compiler)),
        "branch_binary": _exact_json_clone(dict(branch_binary)),
        "runtime_libraries": _exact_json_clone(dict(runtime_libraries)),
        "resource_evidence": {
            "static_payload_raw_utf8": static_text,
            "static_payload_sha256": sha256_bytes(static_payload_raw),
            "branch_payload_raw_utf8": branch_text,
            "branch_payload_sha256": sha256_bytes(branch_payload_raw),
            "persistent_binary_sha256": branch_sha,
        },
        "resource_admission": resource_admission,
        "filesystem": _exact_json_clone(dict(filesystem)),
        "claim_boundary": MACHINE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(candidate, MACHINE_FREEZE_KEYS, "machine candidate")
    cloned = _exact_json_clone(candidate)
    if not exact_json_equal(cloned, candidate):
        raise StrictJSONError("machine candidate is not stable under CJ_COMPACT_V1")
    return cloned


def _machine_tmp_file(
    value: str, context: str, *, serializer: str
) -> tuple[Any, bytes, os.stat_result]:
    """Capture one hardlink-free calibration image from an exact /tmp path."""

    path = safe_absolute_path(value, f"{context} path")
    if path.parts[:2] != ("/", "tmp") or len(path.parts) < 3:
        raise PathContractError(f"{context} must be an absolute /tmp file")
    raw, info = read_pinned_regular_file(path)
    try:
        text = raw.decode("utf-8")
    except UnicodeError as error:
        raise StrictJSONError(f"{context} is not UTF-8") from error
    payload = strict_json_loads(text)
    expected = (
        canonical_json_bytes(payload)
        if serializer == "CJ_COMPACT_V1"
        else pretty_json_bytes(payload)
    )
    if raw != expected:
        raise StrictJSONError(f"{context} is not {serializer}")
    return payload, raw, info


def machine_capture_output_path(value: str) -> Path:
    """Validate the exact, missing, noncanonical /tmp capture destination."""

    target = safe_absolute_path(value, "machine capture output")
    if target.parts[:2] != ("/", "tmp") or len(target.parts) < 3:
        raise PathContractError("machine capture output must be below /tmp")
    if target == MACHINE_FREEZE or is_within(target, ROOT):
        raise PathContractError("machine capture cannot publish in the project tree")
    try:
        parent_fd = _open_directory_fd(target.parent)
    except OSError as error:
        raise PathContractError(
            f"machine capture output parent is unsafe or absent: {error}"
        ) from error
    try:
        parent_info = os.fstat(parent_fd)
        if not stat.S_ISDIR(parent_info.st_mode):
            raise PathContractError("machine capture output parent is not a directory")
        try:
            os.stat(target.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PathContractError("machine capture output already exists")
    finally:
        os.close(parent_fd)
    return target


def _capture_child_subreaper_state() -> bool:
    """Read this process's exact Linux child-subreaper state."""

    if not sys.platform.startswith("linux"):
        raise ProductionAuthorityError(
            "capture child-subreaper semantics require Linux"
        )
    libc = ctypes.CDLL(None, use_errno=True)
    prctl = getattr(libc, "prctl", None)
    if prctl is None:
        raise ProductionAuthorityError(
            "prctl(PR_GET_CHILD_SUBREAPER) is unavailable"
        )
    prctl.restype = ctypes.c_int
    state = ctypes.c_int(-1)
    ctypes.set_errno(0)
    result = prctl(
        ctypes.c_int(37),
        ctypes.byref(state),
        ctypes.c_ulong(0),
        ctypes.c_ulong(0),
        ctypes.c_ulong(0),
    )
    if result != 0 or state.value not in (0, 1):
        error_number = ctypes.get_errno()
        raise ProductionAuthorityError(
            "cannot read capture child-subreaper state "
            f"(errno {error_number})"
        )
    return bool(state.value)


def _set_capture_child_subreaper(enabled: bool) -> None:
    """Set and verify this process's Linux child-subreaper state."""

    if type(enabled) is not bool:
        raise ProductionAuthorityError(
            "capture child-subreaper state must be Boolean"
        )
    if not sys.platform.startswith("linux"):
        raise ProductionAuthorityError(
            "capture child-subreaper semantics require Linux"
        )
    libc = ctypes.CDLL(None, use_errno=True)
    prctl = getattr(libc, "prctl", None)
    if prctl is None:
        raise ProductionAuthorityError(
            "prctl(PR_SET_CHILD_SUBREAPER) is unavailable"
        )
    prctl.restype = ctypes.c_int
    ctypes.set_errno(0)
    result = prctl(
        ctypes.c_int(36),
        ctypes.c_ulong(int(enabled)),
        ctypes.c_ulong(0),
        ctypes.c_ulong(0),
        ctypes.c_ulong(0),
    )
    if result != 0:
        error_number = ctypes.get_errno()
        raise ProductionAuthorityError(
            "cannot set capture child-subreaper state "
            f"(errno {error_number})"
        )
    if _capture_child_subreaper_state() is not enabled:
        raise ProductionAuthorityError(
            "capture child-subreaper state did not take effect"
        )


def _capture_process_group_exists(process_group: int) -> bool:
    """Return whether this exact capture process group still has members."""

    try:
        os.killpg(process_group, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _reap_capture_process_group_children(process_group: int) -> None:
    """Reap only adopted descendants belonging to one owned process group."""

    while True:
        try:
            child, _status = os.waitpid(-process_group, os.WNOHANG)
        except ChildProcessError:
            return
        if child == 0:
            return


def _finish_capture_process_group(
    process_group: int, *, deadline_seconds: float
) -> None:
    """SIGKILL and reap one owned group within a hard monotonic deadline."""

    if deadline_seconds <= 0:
        raise ProductionAuthorityError(
            "capture process-group cleanup deadline must be positive"
        )
    deadline = time.monotonic() + deadline_seconds
    while True:
        _reap_capture_process_group_children(process_group)
        if not _capture_process_group_exists(process_group):
            return
        try:
            os.killpg(process_group, signal.SIGKILL)
        except ProcessLookupError:
            pass
        if time.monotonic() >= deadline:
            break
        time.sleep(0.005)
    _reap_capture_process_group_children(process_group)
    if _capture_process_group_exists(process_group):
        raise ProductionAuthorityError(
            "capture process group survived bounded SIGKILL/reap cleanup"
        )


def _capture_command(
    argv: Sequence[str],
    *,
    cwd: Path,
    environment: Mapping[str, str],
    timeout_seconds: int,
    umask: int = -1,
) -> subprocess.CompletedProcess[bytes]:
    """Stream-cap, timeout, terminate, and reap one non-scientific command."""

    if (
        type(argv) not in (list, tuple)
        or not argv
        or not all(type(item) is str and item and "\x00" not in item for item in argv)
    ):
        raise ProductionAuthorityError("capture command argv is malformed")
    forbidden_executables = {
        str(ROOT / dict(FORMAL_INPUT_ROLES)["static_evaluator"]),
        str(ROOT / dict(FORMAL_INPUT_ROLES)["branch_evaluator_binary"]),
    }
    if argv[0] in forbidden_executables or "--slab-id" in argv:
        raise ProductionAuthorityError(
            "machine capture command attempted scientific dispatch"
        )
    with _CAPTURE_SUBREAPER_LOCK:
        original_subreaper_state = _capture_child_subreaper_state()
        changed_subreaper_state = not original_subreaper_state
        process: subprocess.Popen[bytes] | None = None
        if changed_subreaper_state:
            _set_capture_child_subreaper(True)
        selector: selectors.BaseSelector | None = None
        try:
            process = subprocess.Popen(
                list(argv),
                cwd=cwd,
                env=dict(environment),
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                close_fds=True,
                shell=False,
                start_new_session=True,
                umask=umask,
            )
            assert process.stdout is not None and process.stderr is not None
            streams = {
                process.stdout.fileno(): ("stdout", process.stdout),
                process.stderr.fileno(): ("stderr", process.stderr),
            }
            for descriptor in streams:
                os.set_blocking(descriptor, False)
            buffers = {"stdout": bytearray(), "stderr": bytearray()}
            selector = selectors.DefaultSelector()
            for descriptor in streams:
                selector.register(descriptor, selectors.EVENT_READ)
            deadline = time.monotonic() + timeout_seconds
            exit_seen_at: float | None = None
            failure: str | None = None
            while selector.get_map():
                now = time.monotonic()
                if now >= deadline:
                    failure = f"capture command timed out after {timeout_seconds}s"
                    break
                if process.poll() is not None:
                    if exit_seen_at is None:
                        exit_seen_at = now
                    elif now - exit_seen_at > 1.0:
                        failure = "capture command descendants retained output pipes"
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
                    if len(buffers[stream_name]) > 1024 * 1024:
                        failure = f"capture command {stream_name} cap exceeded"
                        break
                if failure is not None:
                    break
            if failure is not None:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                term_deadline = time.monotonic() + 2.0
                while time.monotonic() < term_deadline:
                    _reap_capture_process_group_children(process.pid)
                    if not _capture_process_group_exists(process.pid):
                        break
                    time.sleep(0.02)
                _finish_capture_process_group(
                    process.pid, deadline_seconds=2.0
                )
                raise ProductionAuthorityError(failure)
            return_code = process.wait(timeout=2)
            _reap_capture_process_group_children(process.pid)
            if _capture_process_group_exists(process.pid):
                _finish_capture_process_group(
                    process.pid, deadline_seconds=2.0
                )
                raise ProductionAuthorityError(
                    "capture command left a live descendant process"
                )
            completed = subprocess.CompletedProcess(
                list(argv), return_code,
                bytes(buffers["stdout"]), bytes(buffers["stderr"]),
            )
        finally:
            try:
                if selector is not None:
                    selector.close()
                if process is not None:
                    if process.stdout is not None:
                        process.stdout.close()
                    if process.stderr is not None:
                        process.stderr.close()
                if process is not None:
                    _finish_capture_process_group(
                        process.pid, deadline_seconds=2.0
                    )
            finally:
                if changed_subreaper_state:
                    _set_capture_child_subreaper(False)
                if (
                    _capture_child_subreaper_state()
                    is not original_subreaper_state
                ):
                    raise ProductionAuthorityError(
                        "capture child-subreaper state was not restored"
                    )
    return completed


def _capture_external_binding(
    path: Path,
    context: str,
    *,
    expected_soname: str | None,
) -> dict[str, Any]:
    raw, info, _ = _read_external_pinned_path(str(path), context)
    build_id, _needed, soname = _elf_metadata(raw, context)
    if expected_soname is not None and soname != expected_soname:
        raise ProductionAuthorityError(f"{context} DT_SONAME mismatch")
    return {
        "path": str(path),
        "mode": stat.S_IMODE(info.st_mode),
        "size_bytes": len(raw),
        "sha256": sha256_bytes(raw),
        "build_id": build_id,
    }


def _capture_runtime_binding(
    path: Path, soname: str, context: str
) -> dict[str, Any]:
    return {
        "soname": soname,
        **_capture_external_binding(
            path, context, expected_soname=soname
        ),
    }


def _capture_regular_archive_binding(path: Path, context: str) -> dict[str, Any]:
    raw, info = read_pinned_regular_file(path)
    return {
        "path": str(path),
        "mode": stat.S_IMODE(info.st_mode),
        "size_bytes": len(raw),
        "sha256": sha256_bytes(raw),
        "build_id": None,
    }


def _capture_python_arb_chain(
    project_root: Path,
    static_payload: Mapping[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Capture the live Python/Arb identity and its bundled ELF closure."""

    bindings = static_payload["bindings"]
    interpreter_binding = bindings["interpreter"]
    flint_binding = bindings["python_flint"]
    interpreter = safe_absolute_path(
        interpreter_binding["invocation_path"], "capture Python executable"
    )
    executable_raw, _executable_info, executable_resolved = (
        _read_external_pinned_path(str(interpreter), "capture Python executable")
    )
    introspection_source = (
        "import importlib,json,platform,sys,flint\n"
        "arb=importlib.import_module('flint.types.arb')\n"
        "fmpq=importlib.import_module('flint.types.fmpq')\n"
        "payload={'python_version':sys.version,'implementation':platform.python_implementation(),"
        "'python_flint_version':flint.__version__,'flint_version':flint.__FLINT_VERSION__,"
        "'arb_version':'FLINT-'+flint.__FLINT_VERSION__,'module_path':flint.__file__,"
        "'arb_extension_path':arb.__file__,'fmpq_extension_path':fmpq.__file__}\n"
        "print(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False))\n"
    )
    completed = _capture_command(
        [str(interpreter), "-I", "-c", introspection_source],
        cwd=project_root,
        environment=formal_build_environment(),
        timeout_seconds=60,
    )
    if completed.returncode != 0 or completed.stderr:
        raise ProductionAuthorityError("Python/Arb live introspection failed")
    try:
        introspection_text = completed.stdout.decode("utf-8")
    except UnicodeError as error:
        raise ProductionAuthorityError(
            "Python/Arb introspection output is not UTF-8"
        ) from error
    introspection = strict_json_loads(introspection_text)
    introspection_keys = {
        "python_version", "implementation", "python_flint_version",
        "flint_version", "arb_version", "module_path", "arb_extension_path",
        "fmpq_extension_path",
    }
    exact_keys(introspection, introspection_keys, "Python/Arb introspection")
    if completed.stdout != canonical_json_bytes(introspection):
        raise ProductionAuthorityError(
            "Python/Arb introspection is not canonical JSON"
        )
    for key in introspection_keys:
        _exact_nonempty_string(introspection[key], f"Python introspection {key}")
    if (
        introspection["python_version"] != MACHINE_PYTHON_VERSION
        or introspection["implementation"] != "CPython"
        or introspection["python_flint_version"] != "0.9.0"
        or introspection["flint_version"] != "3.6.0"
        or introspection["arb_version"] != "FLINT-3.6.0"
        or str(executable_resolved) != interpreter_binding["resolved_path"]
        or sha256_bytes(executable_raw) != interpreter_binding["sha256"]
        or len(executable_raw) != interpreter_binding["size_bytes"]
        or introspection["python_version"] != interpreter_binding["version"]
        or introspection["module_path"] != flint_binding["module_path"]
        or introspection["arb_extension_path"]
        != flint_binding["arb_extension_path"]
    ):
        raise ProductionAuthorityError(
            "Python/Arb live introspection differs from static calibration"
        )

    record_path = safe_absolute_path(
        flint_binding["record_path"], "python-flint RECORD"
    )
    record_raw, _record_info, record_resolved = _read_external_pinned_path(
        str(record_path), "python-flint RECORD"
    )
    installed_count, installed_root = recompute_python_flint_manifest(
        str(record_resolved), record_raw
    )
    if (
        sha256_bytes(record_raw) != flint_binding["record_sha256"]
        or installed_count != flint_binding["installed_record_file_count"]
        or installed_root != flint_binding["installed_manifest_sha256"]
    ):
        raise ProductionAuthorityError(
            "python-flint live RECORD/installed manifest is stale"
        )
    conda_algorithm, conda_count, conda_root = recompute_conda_python_manifest(
        str(interpreter)
    )
    arb_path = safe_absolute_path(
        introspection["arb_extension_path"], "Arb extension"
    )
    fmpq_path = safe_absolute_path(
        introspection["fmpq_extension_path"], "fmpq extension"
    )
    arb_binding = _capture_external_binding(
        arb_path, "Arb extension", expected_soname=None
    )
    fmpq_binding = _capture_external_binding(
        fmpq_path, "fmpq extension", expected_soname=None
    )
    if arb_binding["sha256"] != flint_binding["arb_extension_sha256"]:
        raise ProductionAuthorityError("Arb extension is stale relative to calibration")
    site_packages = record_resolved.parent.parent
    bundled_root = site_packages / "python_flint.libs"
    bundled_libraries = [
        _capture_runtime_binding(
            bundled_root / soname,
            soname,
            f"Python bundled runtime {soname}",
        )
        for soname in MACHINE_PYTHON_BUNDLED_SONAMES
    ]
    python_arb = {
        "executable_path": str(interpreter),
        "executable_sha256": sha256_bytes(executable_raw),
        "python_version": introspection["python_version"],
        "implementation": introspection["implementation"],
        "python_flint_version": introspection["python_flint_version"],
        "flint_version": introspection["flint_version"],
        "arb_version": introspection["arb_version"],
        "conda_manifest_algorithm": conda_algorithm,
        "conda_manifest_file_count": conda_count,
        "conda_installed_manifest_root_sha256": conda_root,
        "python_flint_record_sha256": sha256_bytes(record_raw),
        "python_flint_installed_manifest_root_sha256": installed_root,
        "arb_extension": arb_binding,
        "fmpq_extension": fmpq_binding,
        "bundled_libraries": bundled_libraries,
    }
    exact_keys(python_arb, MACHINE_PYTHON_ARB_KEYS, "captured Python/Arb")
    return python_arb, bundled_libraries


def _capture_capd_chain(
    project_root: Path, checkout_value: str
) -> tuple[dict[str, Any], list[str]]:
    """Capture the clean CAPD checkout/build products and exact flag output."""

    checkout = safe_absolute_path(checkout_value, "capture CAPD checkout")
    algorithm, commit, tree_root = recompute_capd_git_index_tree(str(checkout))
    cache_path = checkout / "build-mp/CMakeCache.txt"
    config_path = checkout / "build-mp/bin/capd-config"
    libcapd_path = checkout / "build-mp/libcapd.a"
    libfilib_path = checkout / "build-mp/capdExt/filibsrc/libfilib.a"
    cache_raw, _ = read_pinned_regular_file(cache_path)
    config_raw, config_info = read_pinned_regular_file(config_path)
    completed = _capture_command(
        [str(config_path), "--cflags", "--libs"],
        cwd=project_root,
        environment=formal_build_environment(),
        timeout_seconds=60,
    )
    replay_config, replay_info = read_pinned_regular_file(config_path)
    if (
        completed.returncode != 0
        or completed.stderr
        or not completed.stdout
        or replay_config != config_raw
        or _stat_identity(replay_info) != _stat_identity(config_info)
    ):
        raise ProductionAuthorityError("CAPD config capture failed or changed")
    try:
        raw_flags = completed.stdout.decode("utf-8")
        tokens = shlex.split(raw_flags, posix=True)
    except (UnicodeError, ValueError) as error:
        raise ProductionAuthorityError("CAPD raw flags are malformed") from error
    if (
        not raw_flags.endswith("\n")
        or tokens != formal_capd_flag_tokens(str(checkout))
    ):
        raise ProductionAuthorityError("CAPD ordered flag output mismatch")
    capd = {
        "checkout_path": str(checkout),
        "commit": commit,
        "tree_algorithm": algorithm,
        "tree_sha256": tree_root,
        "clean": True,
        "cmake_cache_path": str(cache_path),
        "cmake_cache_sha256": sha256_bytes(cache_raw),
        "config_path": str(config_path),
        "config_sha256": sha256_bytes(config_raw),
        "raw_flags": raw_flags,
        "raw_flags_sha256": sha256_bytes(completed.stdout),
        "libcapd": _capture_regular_archive_binding(
            libcapd_path, "CAPD libcapd archive"
        ),
        "libfilib": _capture_regular_archive_binding(
            libfilib_path, "CAPD libfilib archive"
        ),
    }
    exact_keys(capd, MACHINE_CAPD_KEYS, "captured CAPD")
    return capd, tokens


def _capture_system_runtime_libraries() -> list[dict[str, Any]]:
    return [
        _capture_runtime_binding(
            DEFAULT_SYSTEM_LIBRARY_ROOT / soname,
            soname,
            f"CAPD system runtime {soname}",
        )
        for soname in MACHINE_CAPD_SYSTEM_SONAMES
    ]


def _replay_capd_after_fresh_build(
    project_root: Path, capd: Mapping[str, Any]
) -> None:
    """Terminally replay every CAPD build input after the compiler exits."""

    checkout = safe_absolute_path(capd["checkout_path"], "CAPD replay checkout")
    algorithm, commit, tree_root = recompute_capd_git_index_tree(str(checkout))
    if (
        algorithm != capd["tree_algorithm"]
        or commit != capd["commit"]
        or tree_root != capd["tree_sha256"]
    ):
        raise PathContractError("CAPD tracked generation changed during fresh build")
    for path_key, hash_key in (
        ("cmake_cache_path", "cmake_cache_sha256"),
        ("config_path", "config_sha256"),
    ):
        raw, _ = read_pinned_regular_file(Path(capd[path_key]))
        if sha256_bytes(raw) != capd[hash_key]:
            raise PathContractError(f"CAPD {path_key} changed during fresh build")
    for key in ("libcapd", "libfilib"):
        binding = capd[key]
        raw, info = read_pinned_regular_file(Path(binding["path"]))
        if (
            sha256_bytes(raw) != binding["sha256"]
            or len(raw) != binding["size_bytes"]
            or stat.S_IMODE(info.st_mode) != binding["mode"]
        ):
            raise PathContractError(f"CAPD {key} changed during fresh build")
    flags_run = _capture_command(
        [capd["config_path"], "--cflags", "--libs"],
        cwd=project_root,
        environment=formal_build_environment(),
        timeout_seconds=60,
    )
    if (
        flags_run.returncode != 0
        or flags_run.stderr
        or flags_run.stdout != capd["raw_flags"].encode("utf-8")
    ):
        raise PathContractError("CAPD config output changed during fresh build")


def _capture_compiler_and_fresh_rebuild(
    *,
    project_root: Path,
    compiler_value: str,
    capd_tokens: Sequence[str],
    runtime_libraries: Mapping[str, Any],
    branch_calibration_binary_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Perform the one truthful fresh /tmp rebuild without touching role 17."""

    compiler_path = safe_absolute_path(compiler_value, "capture compiler")
    compiler_lexical_before = os.lstat(compiler_path)
    compiler_raw, compiler_info, compiler_resolved = _read_external_pinned_path(
        str(compiler_path), "capture compiler"
    )
    version_run = _capture_command(
        [str(compiler_path), "--version"],
        cwd=project_root,
        environment=formal_build_environment(),
        timeout_seconds=60,
    )
    if version_run.returncode != 0 or version_run.stderr:
        raise ProductionAuthorityError("compiler version capture failed")
    try:
        version_lines = version_run.stdout.decode("utf-8").splitlines()
    except UnicodeError as error:
        raise ProductionAuthorityError("compiler version is not UTF-8") from error
    if not version_lines or version_lines[0] != MACHINE_COMPILER_VERSION:
        raise ProductionAuthorityError("compiler version differs from frozen ABI")

    role_paths = dict(FORMAL_INPUT_ROLES)
    source_relative = role_paths["branch_evaluator_source"]
    binary_relative = role_paths["branch_evaluator_binary"]
    source_path = project_root.joinpath(*safe_relative_path(source_relative).parts)
    persistent_path = project_root.joinpath(*safe_relative_path(binary_relative).parts)
    source_raw, source_before = read_pinned_regular_file(source_path)
    persistent_before_raw, persistent_before = read_pinned_regular_file(
        persistent_path
    )
    if (
        stat.S_IMODE(persistent_before.st_mode) != 0o755
        or sha256_bytes(persistent_before_raw)
        != branch_calibration_binary_sha256
    ):
        raise ProductionAuthorityError(
            "persistent branch binary is stale relative to branch calibration"
        )
    persistent_build_id, persistent_needed, persistent_soname = _elf_metadata(
        persistent_before_raw, "persistent branch binary before rebuild"
    )
    if (
        persistent_needed != MACHINE_BRANCH_DT_NEEDED
        or persistent_soname is not None
    ):
        raise ProductionAuthorityError("persistent branch ELF closure mismatch")

    environment = formal_build_environment()
    argv_template = [
        str(compiler_path),
        "-Wall",
        "-Wextra",
        "-Wpedantic",
        "-Werror",
        str(source_path),
        *capd_tokens,
        "-o",
        "@STAGING_BINARY@",
    ]
    build_recipe = {
        "cwd": str(project_root),
        "environment": environment,
        "umask": "0022",
        "staging_output_token": "@STAGING_BINARY@",
        "argv_template": argv_template,
        "argv_template_sha256": sha256_bytes(
            canonical_json_bytes(argv_template)
        ),
    }

    with tempfile.TemporaryDirectory(
        prefix="a416-l3a1-machine-build.", dir="/tmp"
    ) as staging_text:
        staging_directory = safe_absolute_path(
            staging_text, "fresh build staging directory"
        )
        if staging_directory.parent != Path("/tmp"):
            raise PathContractError("fresh build directory is not a direct /tmp child")
        staging_output = staging_directory / "capd_r401_phase_branch_tube_mp_a1"
        actual_argv = [*argv_template[:-1], str(staging_output)]
        completed = _capture_command(
            actual_argv,
            cwd=project_root,
            environment=environment,
            timeout_seconds=600,
            umask=0o022,
        )
        if completed.returncode != 0:
            raise ProductionAuthorityError(
                f"fresh deterministic branch rebuild failed with rc={completed.returncode}"
            )
        if completed.stdout or completed.stderr:
            raise ProductionAuthorityError(
                "fresh deterministic branch rebuild produced a transcript"
            )
        staged_raw, staged_info = read_pinned_regular_file(staging_output)
        staged_mode = stat.S_IMODE(staged_info.st_mode)
        staged_build_id, staged_needed, staged_soname = _elf_metadata(
            staged_raw, "fresh staging branch binary"
        )
        fresh_receipt = {
            "cwd": str(project_root),
            "environment": environment,
            "umask": "0022",
            "staging_directory": str(staging_directory),
            "staging_output_path": str(staging_output),
            "argv": actual_argv,
            "argv_sha256": sha256_bytes(canonical_json_bytes(actual_argv)),
            "stdout": completed.stdout.decode("utf-8"),
            "stderr": completed.stderr.decode("utf-8"),
            "stdout_sha256": sha256_bytes(completed.stdout),
            "stderr_sha256": sha256_bytes(completed.stderr),
            "return_code": completed.returncode,
            "output_sha256": sha256_bytes(staged_raw),
            "output_size_bytes": len(staged_raw),
            "output_mode": staged_mode,
            "output_build_id": staged_build_id,
            "output_dt_needed": staged_needed,
            "output_dt_needed_sha256": sha256_bytes(
                canonical_json_bytes(staged_needed)
            ),
            "output_soname": staged_soname,
            "shell_used": False,
        }
        persistent_after_raw, persistent_after = read_pinned_regular_file(
            persistent_path
        )
        source_after_raw, source_after = read_pinned_regular_file(source_path)
        compiler_after_raw, compiler_after_info, compiler_after_resolved = (
            _read_external_pinned_path(str(compiler_path), "capture compiler replay")
        )
        compiler_lexical_after = os.lstat(compiler_path)

    before_identity = (persistent_before.st_dev, persistent_before.st_ino)
    after_identity = (persistent_after.st_dev, persistent_after.st_ino)
    byte_equal = staged_raw == persistent_before_raw == persistent_after_raw
    identity_unchanged = (
        _stat_identity(persistent_after) == _stat_identity(persistent_before)
    )
    if (
        not byte_equal
        or not identity_unchanged
        or staged_mode != 0o755
        or staged_build_id != persistent_build_id
        or staged_needed != persistent_needed
        or staged_soname is not None
        or source_after_raw != source_raw
        or _stat_identity(source_after) != _stat_identity(source_before)
        or compiler_after_raw != compiler_raw
        or _stat_identity(compiler_after_info) != _stat_identity(compiler_info)
        or compiler_after_resolved != compiler_resolved
        or _stat_identity(compiler_lexical_after)
        != _stat_identity(compiler_lexical_before)
    ):
        raise ProductionAuthorityError(
            "fresh rebuild is not byte-identical or persistent role 17 changed"
        )
    persistent_sha = sha256_bytes(persistent_before_raw)
    transfer = {
        "branch_calibration_binary_sha256": branch_calibration_binary_sha256,
        "staging_output_sha256": sha256_bytes(staged_raw),
        "staging_output_size_bytes": len(staged_raw),
        "staging_output_mode": staged_mode,
        "persistent_before_sha256": persistent_sha,
        "persistent_before_size_bytes": len(persistent_before_raw),
        "persistent_before_mode": stat.S_IMODE(persistent_before.st_mode),
        "persistent_before_device_id": before_identity[0],
        "persistent_before_inode": before_identity[1],
        "persistent_after_sha256": sha256_bytes(persistent_after_raw),
        "persistent_after_size_bytes": len(persistent_after_raw),
        "persistent_after_mode": stat.S_IMODE(persistent_after.st_mode),
        "persistent_after_device_id": after_identity[0],
        "persistent_after_inode": after_identity[1],
        "byte_for_byte_equal": byte_equal,
        "persistent_identity_unchanged": identity_unchanged,
        "persistent_overwrite_performed": False,
    }
    branch_binary = {
        "path": binary_relative,
        "sha256": persistent_sha,
        "size_bytes": len(persistent_before_raw),
        "executable_mode": stat.S_IMODE(persistent_before.st_mode),
        "build_id": persistent_build_id,
        "source_path": source_relative,
        "source_sha256": sha256_bytes(source_raw),
        "elf_sha256": persistent_sha,
        "dt_needed": persistent_needed,
        "dt_needed_sha256": sha256_bytes(
            canonical_json_bytes(persistent_needed)
        ),
        "runtime_libraries_sha256": sha256_bytes(
            canonical_json_bytes(dict(runtime_libraries))
        ),
    }
    compiler = {
        "executable_path": str(compiler_path),
        "executable_sha256": sha256_bytes(compiler_raw),
        "version": version_lines[0],
        "build_recipe": build_recipe,
        "fresh_rebuild_receipt": fresh_receipt,
        "transfer_evidence": transfer,
    }
    exact_keys(compiler, MACHINE_COMPILER_KEYS, "captured compiler")
    exact_keys(branch_binary, MACHINE_BRANCH_BINARY_KEYS, "captured branch binary")
    return compiler, branch_binary


def _capture_machine_filesystem(project_root: Path) -> tuple[dict[str, Any], int]:
    """Capture the exact project/results device identity and current free bytes."""

    project = safe_absolute_path(str(project_root), "capture project root")
    result_parent = project / "results"
    descriptors: list[int] = []
    devices: list[int] = []
    try:
        for path in (project, result_parent, result_parent):
            descriptor = _open_directory_fd(path)
            descriptors.append(descriptor)
            devices.append(os.fstat(descriptor).st_dev)
    finally:
        for descriptor in descriptors:
            os.close(descriptor)
    if len(set(devices)) != 1:
        raise PathContractError("machine capture project/results filesystems differ")
    stats = os.statvfs(result_parent)
    free_bytes = stats.f_bavail * stats.f_frsize
    filesystem = {
        "project_root": str(project),
        "result_parent": str(result_parent),
        "operational_parent": str(result_parent),
        "project_device_id": devices[0],
        "result_device_id": devices[1],
        "operational_device_id": devices[2],
        "same_filesystem": True,
    }
    exact_keys(filesystem, MACHINE_FILESYSTEM_KEYS, "captured filesystem")
    return filesystem, free_bytes


def capture_live_formal_machine_freeze_candidate(
    *,
    project_root_value: str,
    static_calibration_value: str,
    branch_calibration_value: str,
    capd_checkout_value: str,
    compiler_value: str,
) -> dict[str, Any]:
    """Capture and live-validate one temp-only machine-freeze candidate.

    The only child processes are Python metadata introspection, capd-config,
    compiler version reporting, and one fresh compiler invocation.  Neither
    scientific evaluator nor the persistent branch binary is ever executed.
    """

    project_root = safe_absolute_path(project_root_value, "capture project root")
    if project_root != ROOT:
        raise PathContractError(
            "machine capture is bound to the live Paper02 project root"
        )
    static_payload, static_raw, static_info = _machine_tmp_file(
        static_calibration_value,
        "static calibration",
        serializer="CJ_COMPACT_V1",
    )
    branch_payload, branch_raw, branch_info = _machine_tmp_file(
        branch_calibration_value,
        "branch calibration",
        serializer="CJ_PRETTY_2_V1",
    )
    capture_tool_relative = dict(FORMAL_INPUT_ROLES)["scheduler"]
    capture_tool_path = project_root.joinpath(
        *safe_relative_path(capture_tool_relative).parts
    )
    capture_tool_raw, capture_tool_info = read_pinned_regular_file(
        capture_tool_path
    )
    boot_raw = _live_boot_id_bytes()
    requirements = formal_machine_requirements()
    try:
        memory_limit = int(
            Path("/sys/fs/cgroup/memory/memory.limit_in_bytes")
            .read_text(encoding="ascii")
            .strip()
        )
    except (OSError, UnicodeError, ValueError) as error:
        raise ProductionAuthorityError(
            "live cgroup memory limit is unavailable or malformed"
        ) from error
    logical_cpu_count = len(os.sched_getaffinity(0))
    filesystem, result_free_bytes = _capture_machine_filesystem(project_root)
    observations = {
        "logical_cpu_count": logical_cpu_count,
        "memory_limit_bytes": memory_limit,
        "result_parent_free_bytes": result_free_bytes,
        "idle_baseline_rss_bytes": max(
            static_payload["admission"]["idle_baseline_bytes"],
            branch_payload["admission"]["baseline_bytes"],
        ),
        "representative_static_peak_rss_bytes": static_payload["admission"][
            "representative_peak_rss_bytes"
        ],
        "representative_branch_peak_rss_bytes": branch_payload["admission"][
            "peak_rss_bytes"
        ],
    }
    if (
        logical_cpu_count != requirements["logical_cpu_count"]
        or memory_limit != requirements["memory_limit_bytes"]
    ):
        raise ProductionAuthorityError("live CPU/cgroup requirements are not met")

    role_binary = project_root.joinpath(
        *safe_relative_path(
            dict(FORMAL_INPUT_ROLES)["branch_evaluator_binary"]
        ).parts
    )
    persistent_raw, _ = read_pinned_regular_file(role_binary)
    persistent_sha = sha256_bytes(persistent_raw)
    _validate_static_resource_payload(
        static_payload, requirements, observations, project_root
    )
    _validate_branch_resource_payload(
        branch_payload, requirements, observations, project_root, persistent_sha
    )

    python_arb, python_libraries = _capture_python_arb_chain(
        project_root, static_payload
    )
    capd, capd_tokens = _capture_capd_chain(
        project_root, capd_checkout_value
    )
    capd_libraries = _capture_system_runtime_libraries()
    runtime_libraries = {
        "python_bundled": python_libraries,
        "capd_system": capd_libraries,
    }
    compiler, branch_binary = _capture_compiler_and_fresh_rebuild(
        project_root=project_root,
        compiler_value=compiler_value,
        capd_tokens=capd_tokens,
        runtime_libraries=runtime_libraries,
        branch_calibration_binary_sha256=branch_payload["binary_sha256"],
    )
    _replay_capd_after_fresh_build(project_root, capd)
    candidate = build_formal_machine_freeze_candidate(
        captured_at_utc=datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        capture_tool_sha256=sha256_bytes(capture_tool_raw),
        boot_id_sha256=sha256_bytes(boot_raw),
        machine_observations=observations,
        python_arb=python_arb,
        capd=capd,
        compiler=compiler,
        branch_binary=branch_binary,
        runtime_libraries=runtime_libraries,
        static_payload_raw=static_raw,
        branch_payload_raw=branch_raw,
        filesystem=filesystem,
    )
    _validate_formal_machine_envelope(candidate)

    replay_static, replay_static_info = read_pinned_regular_file(
        safe_absolute_path(static_calibration_value, "static calibration path")
    )
    replay_branch, replay_branch_info = read_pinned_regular_file(
        safe_absolute_path(branch_calibration_value, "branch calibration path")
    )
    replay_tool, replay_tool_info = read_pinned_regular_file(capture_tool_path)
    if (
        replay_static != static_raw
        or _stat_identity(replay_static_info) != _stat_identity(static_info)
        or replay_branch != branch_raw
        or _stat_identity(replay_branch_info) != _stat_identity(branch_info)
        or replay_tool != capture_tool_raw
        or _stat_identity(replay_tool_info) != _stat_identity(capture_tool_info)
    ):
        raise PathContractError("machine capture input changed before publication")
    return candidate


def capture_and_publish_formal_machine_freeze(
    *,
    output_value: str,
    project_root_value: str,
    static_calibration_value: str,
    branch_calibration_value: str,
    capd_checkout_value: str,
    compiler_value: str,
) -> tuple[dict[str, Any], str]:
    """Write one validated candidate exactly once to a noncanonical /tmp file."""

    target = machine_capture_output_path(output_value)
    candidate = capture_live_formal_machine_freeze_candidate(
        project_root_value=project_root_value,
        static_calibration_value=static_calibration_value,
        branch_calibration_value=branch_calibration_value,
        capd_checkout_value=capd_checkout_value,
        compiler_value=compiler_value,
    )
    raw = canonical_json_bytes(candidate)
    exclusive_write_bytes(target, raw)
    replay, replay_info = read_pinned_regular_file(target)
    if (
        replay != raw
        or stat.S_IMODE(replay_info.st_mode) != 0o644
        or replay_info.st_nlink != 1
    ):
        raise CorruptGeneration("published machine candidate replay mismatch")
    # The candidate remains temp-only, but success is reported only after a
    # second independent live terminal replay closes the validation/write gap.
    _validate_formal_machine_envelope(candidate)
    return candidate, sha256_bytes(raw)


def _machine_publication_crash_hook(phase: str) -> None:
    """No-op production hook used only to inject exact crash boundaries."""

    if phase not in MACHINE_PUBLICATION_HOOK_PHASES:
        raise AssertionError(f"unknown machine publication hook phase: {phase}")


def _machine_publication_stage_basename() -> str:
    """Return one collision-resistant, contract-shaped same-parent name."""

    name = (
        ".R401_VAL_L3_A1_V2_MACHINE_FREEZE.json.publish-"
        f"{os.urandom(16).hex()}"
    )
    if MACHINE_PUBLICATION_STAGE_PATTERN.fullmatch(name) is None:
        raise AssertionError("machine publication staging name is malformed")
    return name


def _machine_publication_file_identity(
    info: os.stat_result,
) -> tuple[int, int, int, int, int, int, int]:
    """Return the mutation-sensitive identity pinned by publication."""

    return (
        info.st_dev,
        info.st_ino,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
        stat.S_IMODE(info.st_mode),
        info.st_nlink,
    )


def _machine_publication_directory_chain(
    path: Path,
) -> tuple[tuple[str, int, int, int], ...]:
    """Capture every exact lexical directory component without symlinks."""

    canonical = safe_absolute_path(os.fspath(path), "publication directory")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    current = Path("/")
    signatures: list[tuple[str, int, int, int]] = []
    try:
        root_info = os.fstat(descriptor)
        if not stat.S_ISDIR(root_info.st_mode):
            raise PathContractError("filesystem root is not a directory")
        signatures.append(
            ("/", root_info.st_dev, root_info.st_ino, stat.S_IFMT(root_info.st_mode))
        )
        for component in canonical.parts[1:]:
            next_fd = os.open(
                component,
                flags | nofollow,
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = next_fd
            current /= component
            info = os.fstat(descriptor)
            if not stat.S_ISDIR(info.st_mode):
                raise PathContractError(
                    f"publication namespace component is not a directory: {current}"
                )
            signatures.append(
                (
                    os.fspath(current),
                    info.st_dev,
                    info.st_ino,
                    stat.S_IFMT(info.st_mode),
                )
            )
        return tuple(signatures)
    except OSError as error:
        raise PathContractError(
            f"publication directory chain is unsafe: {canonical}: {error}"
        ) from error
    finally:
        os.close(descriptor)


def _replay_machine_publication_directory(
    path: Path,
    pinned_fd: int,
    expected_chain: tuple[tuple[str, int, int, int], ...],
    context: str,
) -> None:
    """Prove both the pinned terminal inode and its full lexical chain."""

    pinned = os.fstat(pinned_fd)
    if (
        not stat.S_ISDIR(pinned.st_mode)
        or not expected_chain
        or (pinned.st_dev, pinned.st_ino)
        != (expected_chain[-1][1], expected_chain[-1][2])
        or _machine_publication_directory_chain(path) != expected_chain
    ):
        raise PathContractError(f"{context} directory namespace changed")


def _read_machine_publication_file_at(
    parent_fd: int,
    name: str,
    context: str,
    *,
    fsync_file: bool = False,
    expected_mode: int = 0o644,
    maximum_bytes: int = MACHINE_PUBLICATION_MAX_CANDIDATE_BYTES,
) -> tuple[bytes, os.stat_result]:
    """Read one exact-mode, single-link regular file through a pinned parent."""

    if type(name) is not str or not name or "/" in name or name in {".", ".."}:
        raise PathContractError(f"{context} basename is malformed")
    descriptor: int | None = None
    try:
        entry_before = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if not stat.S_ISREG(entry_before.st_mode):
            raise PathContractError(f"{context} is not a regular file")
        if (
            type(expected_mode) is not int
            or expected_mode not in {0o600, 0o644, 0o755}
            or stat.S_IMODE(entry_before.st_mode) != expected_mode
        ):
            raise PathContractError(
                f"{context} mode is not exact {expected_mode:04o}"
            )
        if entry_before.st_nlink != 1:
            raise PathContractError(f"{context} hard-link alias rejected")
        if type(maximum_bytes) is not int or not (1 <= maximum_bytes <= 64 * 1024 * 1024):
            raise PathContractError(f"{context} byte cap is invalid")
        if (
            entry_before.st_size <= 0
            or entry_before.st_size > maximum_bytes
        ):
            raise PathContractError(
                f"{context} size is outside 1.."
                f"{maximum_bytes} bytes"
            )
        descriptor = os.open(
            name,
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise PathContractError(f"{context} is not a regular file")
        if stat.S_IMODE(before.st_mode) != expected_mode:
            raise PathContractError(
                f"{context} mode is not exact {expected_mode:04o}"
            )
        if before.st_nlink != 1:
            raise PathContractError(f"{context} hard-link alias rejected")
        if (
            _machine_publication_file_identity(before)
            != _machine_publication_file_identity(entry_before)
        ):
            raise PathContractError(f"{context} changed before pinned open")
        chunks: list[bytes] = []
        total_bytes = 0
        while True:
            chunk = os.read(
                descriptor,
                min(
                    1024 * 1024,
                    maximum_bytes - total_bytes + 1,
                ),
            )
            if not chunk:
                break
            chunks.append(chunk)
            total_bytes += len(chunk)
            if total_bytes > maximum_bytes:
                raise PathContractError(
                    f"{context} exceeded the pinned publication size cap"
                )
        if fsync_file:
            os.fsync(descriptor)
        after = os.fstat(descriptor)
        entry = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        identity = _machine_publication_file_identity(before)
        if (
            identity != _machine_publication_file_identity(after)
            or identity != _machine_publication_file_identity(entry)
            or (entry.st_dev, entry.st_ino) != (before.st_dev, before.st_ino)
        ):
            raise PathContractError(f"{context} changed during pinned replay")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise PathContractError(f"{context} pinned read was short")
        return raw, before
    except OSError as error:
        raise PathContractError(f"{context} secure replay failed: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _replay_machine_publication_candidate(
    *,
    path: Path,
    parent_fd: int,
    parent_chain: tuple[tuple[str, int, int, int], ...],
    expected_raw: bytes,
    expected_identity: tuple[int, int, int, int, int, int, int],
) -> None:
    """Terminally prove that the caller's candidate namespace is unchanged."""

    _replay_machine_publication_directory(
        path.parent,
        parent_fd,
        parent_chain,
        "machine candidate parent",
    )
    raw, info = _read_machine_publication_file_at(
        parent_fd,
        path.name,
        "machine publication candidate",
    )
    if (
        raw != expected_raw
        or _machine_publication_file_identity(info) != expected_identity
    ):
        raise PathContractError("machine publication candidate changed")


def _write_machine_publication_bytes(descriptor: int, raw: bytes) -> None:
    """Write all staging bytes; split out for deterministic fault injection."""

    view = memoryview(raw)
    while view:
        written = os.write(descriptor, view)
        if written <= 0:
            raise OSError("short machine publication staging write")
        view = view[written:]


def _rename_machine_publication_noreplace(
    parent_fd: int,
    source_name: str,
    destination_name: str,
) -> None:
    """Atomically publish one regular file with no fallback or replacement."""

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
    ctypes.set_errno(0)
    result = renameat2(
        parent_fd,
        os.fsencode(source_name),
        parent_fd,
        os.fsencode(destination_name),
        1,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in {errno.EEXIST, errno.ENOTEMPTY}:
        raise CorruptGeneration(
            "canonical machine freeze destination already exists or collided"
        )
    raise PathContractError(
        "machine publication renameat2(RENAME_NOREPLACE) failed: "
        f"{os.strerror(error_number)}"
    )


def _cleanup_machine_publication_stage(
    parent_fd: int,
    name: str,
    owned_inode: tuple[int, int],
) -> None:
    """Remove only this invocation's exact pre-rename inode, then sync."""

    try:
        entry = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    except OSError as error:
        raise PathContractError(
            f"machine publication staging cleanup stat failed: {error}"
        ) from error
    if (entry.st_dev, entry.st_ino) != owned_inode:
        raise PathContractError(
            "machine publication refused to unlink a replaced staging inode"
        )
    try:
        os.unlink(name, dir_fd=parent_fd)
        os.fsync(parent_fd)
    except OSError as error:
        raise PathContractError(
            f"machine publication staging cleanup failed: {error}"
        ) from error


def _machine_publication_scheduler_snapshot(
    root: Path,
    machine: Mapping[str, Any],
) -> tuple[bytes, tuple[int, int, int, int, int, int, int]]:
    """Bind the candidate to the exact role-19 file in this authority root."""

    scheduler_relative = dict(FORMAL_INPUT_ROLES)["scheduler"]
    capture = machine.get("capture")
    if type(capture) is not dict:
        raise ProductionAuthorityError("machine publication capture record malformed")
    if capture.get("capture_tool_path") != scheduler_relative:
        raise ProductionAuthorityError("machine publication capture tool is not role 19")
    scheduler_path = authority_project_file(root, scheduler_relative)
    raw, info = read_pinned_regular_file(scheduler_path)
    if sha256_bytes(raw) != capture.get("capture_tool_sha256"):
        raise ProductionAuthorityError(
            "machine publication candidate is stale relative to live role 19"
        )
    return raw, _machine_publication_file_identity(info)


def publish_formal_machine_freeze(
    *,
    candidate_value: str,
    expected_sha256: str,
    authority_root_value: str,
) -> dict[str, Any]:
    """Publish role 10 once, without dispatch or independent-review claims.

    The destination is derived only from the exact Paper02 authority root and
    the frozen role-10 path.  A successful ``renameat2`` is never rolled back:
    any later error is deliberately fail-closed and leaves the write-once
    canonical inode for a separate role-24 verification.
    """

    expected_sha256 = _exact_sha(
        expected_sha256, "expected machine publication SHA-256"
    )
    root = safe_absolute_path(authority_root_value, "publication authority root")
    live_root = safe_absolute_path(os.fspath(ROOT), "live Paper02 root")
    if root != live_root:
        raise PathContractError(
            "machine publication authority root must equal the exact live Paper02 root"
        )
    candidate_path = safe_absolute_path(candidate_value, "machine candidate path")
    if candidate_path.parts[:2] != ("/", "tmp") or len(candidate_path.parts) < 3:
        raise PathContractError("machine publication candidate must be an absolute /tmp file")
    destination = authority_project_file(
        root, dict(FORMAL_INPUT_ROLES)["machine_freeze"]
    )
    if candidate_path == destination:
        raise PathContractError("machine publication candidate aliases role 10")

    candidate_parent_fd: int | None = None
    root_fd: int | None = None
    publication_parent_fd: int | None = None
    stage_fd: int | None = None
    stage_name: str | None = None
    stage_inode: tuple[int, int] | None = None
    renamed = False
    preserve_crash_residue = False
    try:
        candidate_parent_fd = _open_directory_fd(candidate_path.parent)
        candidate_parent_chain = _machine_publication_directory_chain(
            candidate_path.parent
        )
        _replay_machine_publication_directory(
            candidate_path.parent,
            candidate_parent_fd,
            candidate_parent_chain,
            "machine candidate parent",
        )
        candidate_raw, candidate_info = _read_machine_publication_file_at(
            candidate_parent_fd,
            candidate_path.name,
            "machine publication candidate",
        )
        candidate_identity = _machine_publication_file_identity(candidate_info)
        if sha256_bytes(candidate_raw) != expected_sha256:
            raise ProductionAuthorityError(
                "machine publication candidate SHA-256 differs from expected intent"
            )
        try:
            candidate_text = candidate_raw.decode("utf-8")
        except UnicodeError as error:
            raise StrictJSONError(
                "machine publication candidate is not UTF-8"
            ) from error
        machine = strict_json_loads(candidate_text)
        if candidate_raw != canonical_json_bytes(machine):
            raise StrictJSONError(
                "machine publication candidate is not CJ_COMPACT_V1"
            )
        if (
            type(machine) is not dict
            or type(machine.get("filesystem")) is not dict
            or machine["filesystem"].get("project_root") != os.fspath(root)
        ):
            raise ProductionAuthorityError(
                "machine publication candidate authority root mismatch"
            )
        _validate_formal_machine_envelope(machine)
        scheduler_raw, scheduler_identity = (
            _machine_publication_scheduler_snapshot(root, machine)
        )
        _replay_machine_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )

        root_fd = _open_directory_fd(root)
        root_chain = _machine_publication_directory_chain(root)
        _replay_machine_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        publication_parent_fd = _open_directory_fd(destination.parent)
        publication_parent_chain = _machine_publication_directory_chain(
            destination.parent
        )
        _replay_machine_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "machine publication parent",
        )
        try:
            os.stat(
                destination.name,
                dir_fd=publication_parent_fd,
                follow_symlinks=False,
            )
        except FileNotFoundError:
            pass
        else:
            raise CorruptGeneration(
                "canonical machine freeze destination already exists"
            )

        for _attempt in range(32):
            proposed_name = _machine_publication_stage_basename()
            if MACHINE_PUBLICATION_STAGE_PATTERN.fullmatch(proposed_name) is None:
                raise PathContractError(
                    "machine publication staging basename violates the contract"
                )
            try:
                stage_fd = os.open(
                    proposed_name,
                    os.O_WRONLY
                    | os.O_CREAT
                    | os.O_EXCL
                    | getattr(os, "O_NOFOLLOW", 0),
                    0o600,
                    dir_fd=publication_parent_fd,
                )
            except FileExistsError:
                continue
            except OSError as error:
                raise PathContractError(
                    f"machine publication staging create failed: {error}"
                ) from error
            stage_name = proposed_name
            initial_stage = os.fstat(stage_fd)
            if not stat.S_ISREG(initial_stage.st_mode) or initial_stage.st_nlink != 1:
                raise PathContractError(
                    "machine publication staging inode is not exclusive regular file"
                )
            stage_inode = (initial_stage.st_dev, initial_stage.st_ino)
            break
        else:
            raise PathContractError(
                "machine publication exhausted collision-safe staging names"
            )
        assert stage_fd is not None and stage_name is not None and stage_inode is not None
        os.fchmod(stage_fd, 0o644)
        _write_machine_publication_bytes(stage_fd, candidate_raw)
        try:
            _machine_publication_crash_hook("AFTER_STAGE_WRITE")
        except SyntheticMachinePublicationCrash:
            preserve_crash_residue = True
            raise
        os.fsync(stage_fd)
        try:
            _machine_publication_crash_hook("AFTER_STAGE_FILE_FSYNC")
        except SyntheticMachinePublicationCrash:
            preserve_crash_residue = True
            raise
        staged_raw, staged_info = _read_machine_publication_file_at(
            publication_parent_fd,
            stage_name,
            "machine publication staging file",
            fsync_file=True,
        )
        if (
            staged_raw != candidate_raw
            or (staged_info.st_dev, staged_info.st_ino) != stage_inode
            or staged_info.st_size != len(candidate_raw)
        ):
            raise CorruptGeneration("machine publication staging replay mismatch")
        os.fsync(publication_parent_fd)
        try:
            _machine_publication_crash_hook("AFTER_STAGING_PARENT_FSYNC")
        except SyntheticMachinePublicationCrash:
            preserve_crash_residue = True
            raise

        _machine_publication_crash_hook("BEFORE_TERMINAL_REPLAY")
        _replay_machine_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )
        _replay_machine_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_machine_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "machine publication parent",
        )
        _validate_formal_machine_envelope(machine)
        replay_scheduler_raw, replay_scheduler_identity = (
            _machine_publication_scheduler_snapshot(root, machine)
        )
        if (
            replay_scheduler_raw != scheduler_raw
            or replay_scheduler_identity != scheduler_identity
        ):
            raise PathContractError("live role-19 scheduler changed before publication")

        _machine_publication_crash_hook("BEFORE_RENAME")
        _replay_machine_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )
        _replay_machine_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_machine_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "machine publication parent",
        )
        if sha256_bytes(_live_boot_id_bytes()) != machine["capture"]["boot_id_sha256"]:
            raise ProductionAuthorityError(
                "machine boot ID changed immediately before publication"
            )
        replay_scheduler_raw, replay_scheduler_identity = (
            _machine_publication_scheduler_snapshot(root, machine)
        )
        if (
            replay_scheduler_raw != scheduler_raw
            or replay_scheduler_identity != scheduler_identity
        ):
            raise PathContractError("live role-19 scheduler changed at publication")
        staged_raw, staged_info = _read_machine_publication_file_at(
            publication_parent_fd,
            stage_name,
            "machine publication staging file",
        )
        if (
            staged_raw != candidate_raw
            or (staged_info.st_dev, staged_info.st_ino) != stage_inode
        ):
            raise CorruptGeneration("machine publication staging inode changed")

        _rename_machine_publication_noreplace(
            publication_parent_fd, stage_name, destination.name
        )
        renamed = True
        _machine_publication_crash_hook("AFTER_RENAME")

        try:
            os.stat(stage_name, dir_fd=publication_parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise CorruptGeneration(
                "machine publication rename left the staging entry present"
            )
        open_stage = os.fstat(stage_fd)
        if (
            (open_stage.st_dev, open_stage.st_ino) != stage_inode
            or stat.S_IMODE(open_stage.st_mode) != 0o644
            or open_stage.st_nlink != 1
            or open_stage.st_size != len(candidate_raw)
        ):
            raise CorruptGeneration(
                "machine publication open staging inode changed after rename"
            )
        published_raw, published_info = _read_machine_publication_file_at(
            publication_parent_fd,
            destination.name,
            "canonical machine freeze",
            fsync_file=True,
        )
        if (
            published_raw != candidate_raw
            or sha256_bytes(published_raw) != expected_sha256
            or (published_info.st_dev, published_info.st_ino) != stage_inode
            or published_info.st_size != len(candidate_raw)
        ):
            raise CorruptGeneration(
                "canonical machine freeze post-publication replay mismatch"
            )
        _machine_publication_crash_hook("AFTER_DESTINATION_FSYNC")
        os.fsync(publication_parent_fd)
        _machine_publication_crash_hook("AFTER_PUBLICATION_PARENT_FSYNC")

        _replay_machine_publication_directory(
            root, root_fd, root_chain, "publication authority root"
        )
        _replay_machine_publication_directory(
            destination.parent,
            publication_parent_fd,
            publication_parent_chain,
            "machine publication parent",
        )
        lexical_raw, lexical_info = read_pinned_regular_file(destination)
        if (
            lexical_raw != candidate_raw
            or _machine_publication_file_identity(lexical_info)
            != _machine_publication_file_identity(published_info)
        ):
            raise CorruptGeneration(
                "canonical machine freeze lexical terminal replay mismatch"
            )
        _replay_machine_publication_candidate(
            path=candidate_path,
            parent_fd=candidate_parent_fd,
            parent_chain=candidate_parent_chain,
            expected_raw=candidate_raw,
            expected_identity=candidate_identity,
        )
        _validate_formal_machine_envelope(machine)
        terminal_scheduler_raw, terminal_scheduler_identity = (
            _machine_publication_scheduler_snapshot(root, machine)
        )
        if (
            terminal_scheduler_raw != scheduler_raw
            or terminal_scheduler_identity != scheduler_identity
        ):
            raise PathContractError("live role-19 scheduler changed after publication")

        receipt = {
            "schema_version": SCHEMA_VERSION,
            "protocol_id": PROTOCOL_ID,
            "artifact_role": "MACHINE_FREEZE_PUBLICATION_RECEIPT",
            "artifact_status": "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY",
            "authority": MACHINE_PUBLICATION_AUTHORITY,
            "candidate_path": os.fspath(candidate_path),
            "canonical_path": os.fspath(destination),
            "machine_freeze_sha256": expected_sha256,
            "size_bytes": len(candidate_raw),
            "mode": "0644",
            "nlink": 1,
            "serializer": "CJ_COMPACT_V1",
            "publication_method": MACHINE_PUBLICATION_METHOD,
            "independent_verification_performed": False,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        if canonical_json_bytes(receipt).decode("utf-8") != (
            json.dumps(
                receipt,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            )
            + "\n"
        ):
            raise StrictJSONError("machine publication receipt is not CJ_COMPACT_V1")
        return receipt
    finally:
        cleanup_error: BaseException | None = None
        if (
            publication_parent_fd is not None
            and stage_name is not None
            and stage_inode is not None
            and not renamed
            and not preserve_crash_residue
        ):
            try:
                _cleanup_machine_publication_stage(
                    publication_parent_fd, stage_name, stage_inode
                )
            except BaseException as error:
                cleanup_error = error
        close_error: OSError | None = None
        for descriptor in (
            stage_fd,
            publication_parent_fd,
            root_fd,
            candidate_parent_fd,
        ):
            if descriptor is None:
                continue
            try:
                os.close(descriptor)
            except OSError as error:
                if close_error is None:
                    close_error = error
        if cleanup_error is not None:
            raise cleanup_error
        if close_error is not None:
            raise PathContractError(
                f"machine publication descriptor close failed: {close_error}"
            ) from close_error


def publish_v2_prefreeze_test_record(
    *,
    candidate_value: str,
    expected_sha256: str,
    authority_root_value: str,
) -> dict[str, Any]:
    """Publish role 11 once; the fixed routing literal is not authorization."""

    _require_v2_role11_mechanical_lock()
    root = safe_absolute_path(authority_root_value, "role-11 publication root")
    if root != ROOT:
        raise PathContractError("role-11 publication root must equal live Paper02 root")
    if type(expected_sha256) is not str or HEX_SHA256.fullmatch(expected_sha256) is None:
        raise PathContractError("role-11 expected SHA-256 is malformed")
    candidate = _v2_private_candidate_path(
        candidate_value, "role-11 publication candidate"
    )
    candidate_image = _v2_snapshot_private_candidate(
        candidate,
        maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        context="role-11 publication candidate",
    )
    candidate_raw = candidate_image.raw
    if sha256_bytes(candidate_raw) != expected_sha256:
        raise PathContractError("role-11 publication candidate contract mismatch")
    destination = authority_project_file(
        root, dict(FORMAL_INPUT_ROLES)["prefreeze_tests"]
    )
    publication_absence = _v2_absence_snapshot(
        (
            destination,
            root / dict(FORMAL_INPUT_ROLES)["prefreeze_review"],
            root / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json",
            root / "results/r401_val_l3_a1_v2_all_slabs",
            root / "results/r401_val_l3_a1_v2_all_slabs.operational",
        ),
        "V2 role 11 publication absence",
    )
    downstream_absence = _v2_absence_snapshot(
        tuple(
            Path(path_text)
            for path_text, _device, _inode in publication_absence[1:]
        ),
        "V2 role 11 downstream publication absence",
    )
    records, entries, images, role5, machine = _v2_role11_capture_inputs(root)
    by_role = {record.role: record for record in records}
    payload = validate_v2_prefreeze_test_record_bytes(
        candidate_raw,
        authority_root=root,
        python_executable=machine["python_arb"]["executable_path"],
        role5_payload=role5,
        role_records=by_role,
        require_locked=True,
        require_live_absence=True,
    )
    repository = payload["repository_snapshot"]
    capture_commit = repository["capture_commit_oid"]
    if _v2_role11_repository_probes(root) != capture_commit:
        raise ProductionAuthorityError("role-11 publication live preprobe mismatch")
    root_chain = _machine_publication_directory_chain(root)
    publication_parent_chain = _machine_publication_directory_chain(
        destination.parent
    )
    root_fd = _open_directory_fd(root)
    try:
        parent_fd = _open_directory_fd(destination.parent)
    except BaseException:
        os.close(root_fd)
        raise

    def replay_publication_directories(context: str) -> None:
        _replay_machine_publication_directory(
            root, root_fd, root_chain, f"{context} authority root"
        )
        _replay_machine_publication_directory(
            destination.parent,
            parent_fd,
            publication_parent_chain,
            f"{context} publication parent",
        )

    stage_fd: int | None = None
    stage_name: str | None = None
    stage_identity: tuple[int, int] | None = None
    stage_full_identity: tuple[int, int, int, int, int, int, int] | None = None
    locked = False
    renamed = False
    try:
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError(
                "role-11 publication parent transaction is already locked"
            ) from error
        locked = True
        replay_publication_directories("role-11 prestage")
        if _v2_role11_repository_probes(root) != capture_commit:
            raise ProductionAuthorityError(
                "role-11 publication repository changed before staging"
            )
        _v2_absence_replay(
            publication_absence, "V2 role 11 prestage publication absence"
        )
        residues = tuple(
            name
            for name in os.listdir(parent_fd)
            if name.startswith(
                ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-"
            )
        )
        if residues:
            raise PathContractError("role-11 publication stage residue exists")
        stage_name = (
            ".R401_VAL_L3_A1_V2_PREFREEZE_TESTS.json.publish-"
            + os.urandom(16).hex()
        )
        stage_fd = os.open(
            stage_name,
            os.O_RDWR | os.O_CREAT | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
            0o600,
            dir_fd=parent_fd,
        )
        stage_open = os.fstat(stage_fd)
        stage_identity = (stage_open.st_dev, stage_open.st_ino)
        if (
            not stat.S_ISREG(stage_open.st_mode)
            or stat.S_IMODE(stage_open.st_mode) != 0o600
            or stage_open.st_nlink != 1
            or stage_open.st_size != 0
        ):
            raise PathContractError("role-11 publication stage is not private/empty")
        _write_machine_publication_bytes(stage_fd, candidate_raw)
        os.fchmod(stage_fd, 0o644)
        os.fsync(stage_fd)
        staged = os.fstat(stage_fd)
        if (
            (staged.st_dev, staged.st_ino) != stage_identity
            or staged.st_size != len(candidate_raw)
            or stat.S_IMODE(staged.st_mode) != 0o644
            or staged.st_nlink != 1
        ):
            raise PathContractError("role-11 staged inode mismatch")
        stage_full_identity = _machine_publication_file_identity(staged)
        os.fsync(parent_fd)
        _v2_role11_publication_fault_hook("AFTER_STAGE_DURABLE")
        replay_publication_directories("role-11 staged terminal")

        assert stage_identity is not None and stage_full_identity is not None
        stage_path = destination.parent / stage_name
        _v2_role11_expect_publication_status(
            root,
            stage_path,
            stage_identity,
            "role-11 prerename stage status",
        )
        terminal_live = _v2_role11_live_remote_probe(root)
        terminal_records, terminal_entries, terminal_images, terminal_role5, terminal_machine = (
            _v2_role11_capture_inputs(root)
        )
        if (
            terminal_live != capture_commit
            or terminal_records != records
            or not exact_json_equal(terminal_entries, entries)
            or terminal_images != images
            or not exact_json_equal(terminal_role5, role5)
            or not exact_json_equal(terminal_machine, machine)
        ):
            raise ProductionAuthorityError("role-11 publication terminal input replay mismatch")
        _v2_git_validate_current_repository(
            root,
            capture_commit=capture_commit,
            capture_tree=repository["capture_tree_oid"],
            origin_main=repository["origin_main_oid"],
            required_bindings=entries,
        )
        _v2_replay_private_candidate(
            candidate,
            candidate_image,
            context="role-11 candidate before rename",
        )
        validate_v2_prefreeze_test_record_bytes(
            candidate_raw,
            authority_root=root,
            python_executable=machine["python_arb"]["executable_path"],
            role5_payload=role5,
            role_records=by_role,
            require_locked=True,
            require_live_absence=False,
        )
        _v2_absence_replay(
            publication_absence, "V2 role 11 prerename publication absence"
        )
        stage_replay_raw, stage_replay_info = _read_machine_publication_file_at(
            parent_fd,
            stage_name,
            "role-11 publication stage",
            fsync_file=True,
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        )
        if (
            stage_replay_raw != candidate_raw
            or _machine_publication_file_identity(stage_replay_info)
            != stage_full_identity
        ):
            raise PathContractError("role-11 staged bytes/inode changed")
        _v2_role11_publication_fault_hook("BEFORE_RENAME")

        # BEFORE_RENAME is an adversarial boundary.  Nothing captured before
        # it authorizes the write-once edge: independently repeat the entire
        # envelope and finish with compact stage/status/directory checks.
        replay_publication_directories("role-11 posthook prerename")
        if _v2_role11_live_remote_probe(root) != capture_commit:
            raise ProductionAuthorityError(
                "role-11 posthook prerename remote replay mismatch"
            )
        (
            posthook_records,
            posthook_entries,
            posthook_images,
            posthook_role5,
            posthook_machine,
        ) = _v2_role11_capture_inputs(root)
        if (
            posthook_records != records
            or not exact_json_equal(posthook_entries, entries)
            or posthook_images != images
            or not exact_json_equal(posthook_role5, role5)
            or not exact_json_equal(posthook_machine, machine)
        ):
            raise ProductionAuthorityError(
                "role-11 posthook prerename full input replay mismatch"
            )
        _v2_git_validate_current_repository(
            root,
            capture_commit=capture_commit,
            capture_tree=repository["capture_tree_oid"],
            origin_main=repository["origin_main_oid"],
            required_bindings=entries,
        )
        if _v2_git_origin_url(root) != V2_ROLE11_ORIGIN_URL:
            raise ProductionAuthorityError(
                "role-11 posthook prerename origin URL mismatch"
            )
        _v2_replay_private_candidate(
            candidate,
            candidate_image,
            context="role-11 posthook prerename candidate replay",
        )
        validate_v2_prefreeze_test_record_bytes(
            candidate_raw,
            authority_root=root,
            python_executable=machine["python_arb"]["executable_path"],
            role5_payload=role5,
            role_records=by_role,
            require_locked=True,
            require_live_absence=False,
        )
        _v2_absence_replay(
            publication_absence,
            "V2 role 11 posthook prerename publication/downstream absence",
        )
        posthook_stage_raw, posthook_stage_info = (
            _read_machine_publication_file_at(
                parent_fd,
                stage_name,
                "role-11 posthook prerename stage",
                fsync_file=True,
                maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
            )
        )
        if (
            posthook_stage_raw != candidate_raw
            or _machine_publication_file_identity(posthook_stage_info)
            != stage_full_identity
        ):
            raise PathContractError(
                "role-11 posthook prerename staged bytes/inode changed"
            )
        _v2_role11_expect_publication_status(
            root,
            stage_path,
            stage_identity,
            "role-11 posthook prerename stage-only status",
        )
        replay_publication_directories("role-11 immediate prerename")
        immediate_stage_raw, immediate_stage_info = _read_machine_publication_file_at(
            parent_fd,
            stage_name,
            "role-11 immediate prerename stage",
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        )
        if (
            immediate_stage_raw != candidate_raw
            or _machine_publication_file_identity(immediate_stage_info)
            != stage_full_identity
        ):
            raise PathContractError("role-11 immediate prerename stage mismatch")
        _rename_machine_publication_noreplace(
            parent_fd, stage_name, destination.name
        )
        renamed = True
        _v2_role11_publication_fault_hook("AFTER_RENAME")
        replay_publication_directories("role-11 postrename")
        try:
            os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PathContractError("role-11 rename left its stage name present")
        open_stage = os.fstat(stage_fd)
        postrename_identity = _machine_publication_file_identity(open_stage)
        stable_indexes = (0, 1, 2, 3, 5, 6)
        if (
            any(
                postrename_identity[index] != stage_full_identity[index]
                for index in stable_indexes
            )
            or postrename_identity[4] < stage_full_identity[4]
        ):
            raise PathContractError("role-11 open stage inode changed after rename")
        canonical_raw, canonical_info = _read_machine_publication_file_at(
            parent_fd,
            destination.name,
            "canonical role-11 prefreeze tests",
            fsync_file=True,
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        )
        if (
            canonical_raw != candidate_raw
            or _machine_publication_file_identity(canonical_info)
            != postrename_identity
            or sha256_bytes(canonical_raw) != expected_sha256
        ):
            raise PathContractError("role-11 postrename canonical replay mismatch")
        os.fsync(parent_fd)
        _v2_role11_publication_fault_hook("AFTER_PUBLICATION_PARENT_FSYNC")
        replay_publication_directories("role-11 post-parent-fsync")
        validate_v2_prefreeze_test_record_bytes(
            canonical_raw,
            authority_root=root,
            python_executable=machine["python_arb"]["executable_path"],
            role5_payload=role5,
            role_records=by_role,
            require_locked=True,
            require_live_absence=False,
        )
        _v2_role11_expect_publication_status(
            root,
            destination,
            stage_identity,
            "role-11 postrename canonical status",
        )
        if _v2_role11_live_remote_probe(root) != capture_commit:
            raise ProductionAuthorityError("role-11 publication postprobe mismatch")
        ultimate_records, ultimate_entries, ultimate_images, ultimate_role5, ultimate_machine = (
            _v2_role11_capture_inputs(root)
        )
        if (
            ultimate_records != records
            or not exact_json_equal(ultimate_entries, entries)
            or ultimate_images != images
            or not exact_json_equal(ultimate_role5, role5)
            or not exact_json_equal(ultimate_machine, machine)
        ):
            raise ProductionAuthorityError(
                "role-11 postrename full input replay mismatch"
            )
        _v2_git_validate_current_repository(
            root,
            capture_commit=capture_commit,
            capture_tree=repository["capture_tree_oid"],
            origin_main=repository["origin_main_oid"],
            required_bindings=entries,
        )
        _v2_absence_replay(
            downstream_absence, "V2 role 11 postrename downstream absence"
        )
        _v2_replay_private_candidate(
            candidate,
            candidate_image,
            context="role-11 postrename candidate replay",
        )
        terminal_raw, terminal_info = read_pinned_regular_file(destination)
        if (
            terminal_raw != canonical_raw
            or _machine_publication_file_identity(terminal_info)
            != postrename_identity
        ):
            raise PathContractError("role-11 ultimate canonical replay mismatch")
        _v2_role11_publication_fault_hook("AFTER_ULTIMATE_REPLAY")
        replay_publication_directories("role-11 posthook terminal")
        final_raw, final_info = _read_machine_publication_file_at(
            parent_fd,
            destination.name,
            "role-11 posthook canonical terminal replay",
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        )
        if (
            final_raw != candidate_raw
            or sha256_bytes(final_raw) != expected_sha256
            or _machine_publication_file_identity(final_info)
            != postrename_identity
        ):
            raise PathContractError("role-11 posthook canonical replay mismatch")
        try:
            os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PathContractError("role-11 posthook stage namespace reappeared")
        _v2_role11_expect_publication_status(
            root,
            destination,
            stage_identity,
            "role-11 posthook canonical status",
        )
        if _v2_role11_live_remote_probe(root) != capture_commit:
            raise ProductionAuthorityError("role-11 posthook remote replay mismatch")
        final_records, final_entries, final_images, final_role5, final_machine = (
            _v2_role11_capture_inputs(root)
        )
        if (
            final_records != records
            or not exact_json_equal(final_entries, entries)
            or final_images != images
            or not exact_json_equal(final_role5, role5)
            or not exact_json_equal(final_machine, machine)
        ):
            raise ProductionAuthorityError("role-11 posthook input replay mismatch")
        _v2_git_validate_current_repository(
            root,
            capture_commit=capture_commit,
            capture_tree=repository["capture_tree_oid"],
            origin_main=repository["origin_main_oid"],
            required_bindings=entries,
        )
        _v2_absence_replay(
            downstream_absence, "V2 role 11 posthook downstream absence"
        )
        _v2_replay_private_candidate(
            candidate,
            candidate_image,
            context="role-11 posthook candidate terminal replay",
        )
        # Close the long posthook input/Git interval with a fresh network
        # observation and exact one-leaf porcelain transcript.  Two compact
        # file/status passes then reject namespace insertion during either
        # terminal reopen without leaving another fault hook afterward.
        if _v2_role11_live_remote_probe(root) != capture_commit:
            raise ProductionAuthorityError(
                "role-11 ultimate remote replay mismatch"
            )
        _v2_role11_expect_publication_status(
            root,
            destination,
            stage_identity,
            "role-11 ultimate canonical-only status",
        )
        replay_publication_directories("role-11 ultimate compact replay")
        compact_raw, compact_info = _read_machine_publication_file_at(
            parent_fd,
            destination.name,
            "role-11 ultimate compact canonical replay",
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        )
        if (
            compact_raw != candidate_raw
            or sha256_bytes(compact_raw) != expected_sha256
            or _machine_publication_file_identity(compact_info)
            != postrename_identity
        ):
            raise PathContractError("role-11 ultimate compact canonical mismatch")
        _v2_replay_private_candidate(
            candidate,
            candidate_image,
            context="role-11 ultimate compact candidate replay",
        )
        _v2_role11_expect_publication_status(
            root,
            destination,
            stage_identity,
            "role-11 final canonical-only status",
        )
        replay_publication_directories("role-11 final compact replay")
        final_compact_raw, final_compact_info = _read_machine_publication_file_at(
            parent_fd,
            destination.name,
            "role-11 final compact canonical replay",
            maximum_bytes=V2_ROLE11_MAX_CANDIDATE_BYTES,
        )
        if (
            final_compact_raw != candidate_raw
            or sha256_bytes(final_compact_raw) != expected_sha256
            or _machine_publication_file_identity(final_compact_info)
            != postrename_identity
        ):
            raise PathContractError("role-11 final compact canonical mismatch")
        _v2_replay_private_candidate(
            candidate,
            candidate_image,
            context="role-11 final compact candidate replay",
        )
        return {
            "schema_version": 1,
            "protocol_id": V2_ROLE11_PROTOCOL_ID,
            "artifact_role": "PREFREEZE_TEST_PUBLICATION_RECEIPT",
            "artifact_status": "PUBLISHED_WRITE_ONCE_NON_LICENSING",
            "authority": PREFREEZE_TEST_PUBLICATION_AUTHORITY,
            "candidate_path": os.fspath(candidate),
            "canonical_path": os.fspath(destination),
            "prefreeze_tests_sha256": expected_sha256,
            "size_bytes": len(candidate_raw),
            "mode": "0644",
            "nlink": 1,
            "serializer": "CJ_COMPACT_V1",
            "publication_method": MACHINE_PUBLICATION_METHOD,
            "independent_verification_performed": False,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
    finally:
        primary_error = sys.exc_info()[1]
        cleanup_error: BaseException | None = None
        if (
            not renamed
            and stage_name is not None
            and stage_identity is None
            and stage_fd is not None
        ):
            try:
                recovered_stage = os.fstat(stage_fd)
                if (
                    not stat.S_ISREG(recovered_stage.st_mode)
                    or recovered_stage.st_nlink != 1
                ):
                    raise PathContractError(
                        "role-11 publication opened stage cannot be recovered safely"
                    )
                stage_identity = (
                    recovered_stage.st_dev,
                    recovered_stage.st_ino,
                )
            except BaseException as error:
                cleanup_error = error
        if not renamed and stage_name is not None and stage_identity is not None:
            try:
                _cleanup_machine_publication_stage(
                    parent_fd, stage_name, stage_identity
                )
            except BaseException as error:
                cleanup_error = error
        if stage_fd is not None:
            try:
                os.close(stage_fd)
            except BaseException as error:
                if cleanup_error is None:
                    cleanup_error = error
        if locked:
            try:
                fcntl.flock(parent_fd, fcntl.LOCK_UN)
            except BaseException as error:
                if cleanup_error is None:
                    cleanup_error = PathContractError(
                        f"role-11 publication unlock failed: {error}"
                    )
        try:
            os.close(parent_fd)
        except BaseException as error:
            if cleanup_error is None:
                cleanup_error = error
        try:
            os.close(root_fd)
        except BaseException as error:
            if cleanup_error is None:
                cleanup_error = error
        if cleanup_error is not None:
            if primary_error is not None:
                raise cleanup_error from primary_error
            raise cleanup_error


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


V2_MAIN_CANDIDATE_MAX_BYTES = 1024 * 1024


def build_v2_main_freeze_payload(
    input_roles: Sequence[FormalRoleRecord],
    machine_payload: Mapping[str, Any],
) -> dict[str, Any]:
    """Construct and self-validate the exact 26-key role-54 candidate."""

    if (
        type(input_roles) not in (list, tuple)
        or len(input_roles) != 53
        or tuple((item.role, item.path) for item in input_roles)
        != FORMAL_INPUT_ROLES
    ):
        raise ProductionAuthorityError(
            "V2 main candidate requires exact ordered 53-role records"
        )
    roles = {item.role: item for item in input_roles}
    if len(roles) != 53:
        raise ProductionAuthorityError("V2 main candidate role names are not unique")
    machine = _validate_formal_machine_envelope(machine_payload)
    machine_record = roles["machine_freeze"]
    if machine_record.raw != canonical_json_bytes(machine):
        raise ProductionAuthorityError(
            "V2 main candidate machine bytes/payload mismatch"
        )
    review = roles["prefreeze_review"]
    if review.raw != b"Verdict: ACCEPT_FOR_FREEZE\n":
        raise ProductionAuthorityError(
            "V2 main candidate role 12 is not exact 27-byte verdict"
        )
    payload = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "MAIN_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "INDEPENDENT_PREFREEZE_REVIEW",
        "scientific_licensing_enabled": True,
        "matrix": matrix_payload(),
        "matrix_id": canonical_matrix_id(),
        "input_roles": [item.payload() for item in input_roles],
        "machine_freeze_sha256": machine_record.sha256,
        "prefreeze_review": {
            "path": review.path,
            "sha256": review.sha256,
            "verdict": "ACCEPT_FOR_FREEZE",
        },
        "serializers": formal_serializers(),
        "scheduler": formal_scheduler_policy(),
        "limits": formal_limits(),
        "status_tables": formal_status_tables(),
        "evaluators": {
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
        },
        "checkers": {
            name: {"path": roles[role].path, "sha256": roles[role].sha256}
            for name, role in (
                ("static", "static_checker_source"),
                ("branch", "branch_checker_source"),
                ("composite", "composite_checker_source"),
                ("release_builder", "release_builder"),
            )
        },
        "archive_layout": formal_archive_layout(),
        "machine_requirements": formal_machine_requirements(),
        "failure_policy": formal_failure_policy(),
        "execution_policy": formal_execution_policy(),
        "claim_boundary": MAIN_FREEZE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(payload, FORMAL_MAIN_FREEZE_REQUIRED_KEYS, "V2 main candidate")
    validated = _validate_formal_main_envelope(
        payload, input_roles, machine_record.sha256
    )
    raw = canonical_json_bytes(validated)
    if len(raw) > V2_MAIN_CANDIDATE_MAX_BYTES:
        raise ProductionAuthorityError("V2 main candidate exceeds 1 MiB")
    return validated


def _v2_private_candidate_path(value: str, context: str) -> Path:
    path = safe_absolute_path(value, context)
    if (
        path.parent.parent != Path("/tmp")
        or path.parent == Path("/tmp")
        or path.name in {"", ".", ".."}
        or path.name.startswith(".")
    ):
        raise PathContractError(
            f"{context} must be /tmp/<owned-0700-singleton>/<leaf>"
        )
    parent = os.stat(path.parent, follow_symlinks=False)
    if (
        not stat.S_ISDIR(parent.st_mode)
        or parent.st_uid != os.geteuid()
        or stat.S_IMODE(parent.st_mode) != 0o700
        or parent.st_nlink != 2
    ):
        raise PathContractError(
            f"{context} parent is not an owned mode-0700 nlink-2 singleton"
        )
    return path


def _v2_replay_private_candidate(
    path: Path,
    image: V2PrivateCandidateImage,
    *,
    context: str,
) -> None:
    """Replay a complete candidate/parent image without following aliases."""

    canonical = _v2_private_candidate_path(os.fspath(path), context)
    parent_fd = _open_directory_fd(canonical.parent)
    descriptor: int | None = None
    try:
        _replay_machine_publication_directory(
            canonical.parent,
            parent_fd,
            image.parent_chain,
            f"{context} parent chain",
        )
        parent_before = os.fstat(parent_fd)
        if (
            parent_before.st_dev,
            parent_before.st_ino,
            parent_before.st_mode,
            parent_before.st_nlink,
        ) != (
            image.parent_device_id,
            image.parent_inode,
            image.parent_mode,
            image.parent_nlink,
        ) or tuple(os.listdir(parent_fd)) != (canonical.name,):
            raise PathContractError(f"{context} parent/namespace replay mismatch")
        descriptor = os.open(
            canonical.name,
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        before = os.fstat(descriptor)
        expected_stat = (
            image.device_id,
            image.inode,
            image.mode,
            image.nlink,
            image.size_bytes,
            image.mtime_ns,
            image.ctime_ns,
        )
        if (
            before.st_dev,
            before.st_ino,
            before.st_mode,
            before.st_nlink,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        ) != expected_stat:
            raise PathContractError(f"{context} full inode replay mismatch")
        raw = bytearray()
        offset = 0
        while len(raw) <= image.size_bytes:
            chunk = os.pread(
                descriptor,
                min(65536, image.size_bytes + 1 - len(raw)),
                offset,
            )
            if not chunk:
                break
            raw.extend(chunk)
            offset += len(chunk)
        after = os.fstat(descriptor)
        entry = os.stat(
            canonical.name, dir_fd=parent_fd, follow_symlinks=False
        )
        parent_after = os.fstat(parent_fd)
        if bytes(raw) != image.raw or len(raw) != image.size_bytes:
            raise PathContractError(f"{context} bounded byte replay mismatch")
        for info in (after, entry):
            if (
                info.st_dev,
                info.st_ino,
                info.st_mode,
                info.st_nlink,
                info.st_size,
                info.st_mtime_ns,
                info.st_ctime_ns,
            ) != expected_stat:
                raise PathContractError(f"{context} terminal inode replay mismatch")
        if (
            parent_after.st_dev,
            parent_after.st_ino,
            parent_after.st_mode,
            parent_after.st_nlink,
        ) != (
            image.parent_device_id,
            image.parent_inode,
            image.parent_mode,
            image.parent_nlink,
        ) or tuple(os.listdir(parent_fd)) != (canonical.name,):
            raise PathContractError(f"{context} terminal parent replay mismatch")
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def _v2_snapshot_private_candidate(
    path: Path,
    *,
    maximum_bytes: int,
    context: str,
) -> V2PrivateCandidateImage:
    """Pin a caller-owned 0600 singleton candidate without ever modifying it."""

    canonical = _v2_private_candidate_path(os.fspath(path), context)
    parent_chain = _machine_publication_directory_chain(canonical.parent)
    parent_fd = _open_directory_fd(canonical.parent)
    descriptor: int | None = None
    try:
        _replay_machine_publication_directory(
            canonical.parent,
            parent_fd,
            parent_chain,
            f"{context} initial parent chain",
        )
        parent_before = os.fstat(parent_fd)
        if tuple(os.listdir(parent_fd)) != (canonical.name,):
            raise PathContractError(f"{context} parent is not a singleton")
        descriptor = os.open(
            canonical.name,
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            dir_fd=parent_fd,
        )
        before = os.fstat(descriptor)
        if (
            not stat.S_ISREG(before.st_mode)
            or stat.S_IMODE(before.st_mode) != 0o600
            or before.st_nlink != 1
            or before.st_size <= 0
            or before.st_size > maximum_bytes
        ):
            raise PathContractError(f"{context} inode/mode/size mismatch")
        raw = bytearray()
        offset = 0
        while len(raw) <= maximum_bytes:
            chunk = os.pread(
                descriptor,
                min(65536, maximum_bytes + 1 - len(raw)),
                offset,
            )
            if not chunk:
                break
            raw.extend(chunk)
            offset += len(chunk)
        if len(raw) > maximum_bytes:
            raise PathContractError(f"{context} exceeded byte cap")
        after = os.fstat(descriptor)
        entry = os.stat(
            canonical.name, dir_fd=parent_fd, follow_symlinks=False
        )
        parent_after = os.fstat(parent_fd)
        fingerprint = lambda info: (
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            info.st_size,
            info.st_mtime_ns,
            info.st_ctime_ns,
        )
        if (
            len(raw) != before.st_size
            or fingerprint(after) != fingerprint(before)
            or fingerprint(entry) != fingerprint(before)
            or (
                parent_after.st_dev,
                parent_after.st_ino,
                parent_after.st_mode,
                parent_after.st_nlink,
            ) != (
                parent_before.st_dev,
                parent_before.st_ino,
                parent_before.st_mode,
                parent_before.st_nlink,
            )
            or tuple(os.listdir(parent_fd)) != (canonical.name,)
        ):
            raise PathContractError(f"{context} changed during snapshot")
        image = V2PrivateCandidateImage(
            raw=bytes(raw),
            device_id=before.st_dev,
            inode=before.st_ino,
            mode=before.st_mode,
            nlink=before.st_nlink,
            size_bytes=before.st_size,
            mtime_ns=before.st_mtime_ns,
            ctime_ns=before.st_ctime_ns,
            parent_device_id=parent_before.st_dev,
            parent_inode=parent_before.st_ino,
            parent_mode=parent_before.st_mode,
            parent_nlink=parent_before.st_nlink,
            parent_chain=parent_chain,
        )
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)
    _v2_replay_private_candidate(canonical, image, context=f"{context} terminal")
    return image


def _v2_write_private_candidate(
    path: Path,
    raw: bytes,
    *,
    maximum_bytes: int,
    context: str,
) -> V2PrivateCandidateImage:
    if type(raw) is not bytes or not raw or len(raw) > maximum_bytes:
        raise PathContractError(f"{context} byte cap mismatch")
    canonical = _v2_private_candidate_path(os.fspath(path), context)
    parent_chain = _machine_publication_directory_chain(canonical.parent)
    parent_fd = _open_directory_fd(canonical.parent)
    descriptor: int | None = None
    created_identity: tuple[int, int] | None = None
    image: V2PrivateCandidateImage | None = None
    try:
        parent_before = os.fstat(parent_fd)
        _replay_machine_publication_directory(
            canonical.parent,
            parent_fd,
            parent_chain,
            f"{context} initial parent chain",
        )
        namespace = tuple(os.listdir(parent_fd))
        if namespace == (canonical.name,):
            raise PathContractError(f"{context} destination already exists")
        if (
            not stat.S_ISDIR(parent_before.st_mode)
            or parent_before.st_uid != os.geteuid()
            or stat.S_IMODE(parent_before.st_mode) != 0o700
            or parent_before.st_nlink != 2
            or namespace != ()
        ):
            raise PathContractError(f"{context} parent is not an empty singleton")
        descriptor = os.open(
            canonical.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
            0o600,
            dir_fd=parent_fd,
        )
        created = os.fstat(descriptor)
        created_identity = (created.st_dev, created.st_ino)
        os.fchmod(descriptor, 0o600)
        view = memoryview(raw)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short private candidate write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        if (
            not stat.S_ISREG(info.st_mode)
            or stat.S_IMODE(info.st_mode) != 0o600
            or info.st_nlink != 1
            or info.st_size != len(raw)
        ):
            raise PathContractError(f"{context} final inode mismatch")
        entry = os.stat(canonical.name, dir_fd=parent_fd, follow_symlinks=False)
        parent_after = os.fstat(parent_fd)
        if (
            entry.st_dev,
            entry.st_ino,
            entry.st_mode,
            entry.st_nlink,
            entry.st_size,
        ) != (
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            info.st_size,
        ) or (
            parent_after.st_dev,
            parent_after.st_ino,
            parent_after.st_mode,
            parent_after.st_nlink,
        ) != (
            parent_before.st_dev,
            parent_before.st_ino,
            parent_before.st_mode,
            parent_before.st_nlink,
        ) or tuple(os.listdir(parent_fd)) != (canonical.name,):
            raise PathContractError(f"{context} directory entry mismatch")
        os.fsync(parent_fd)
        image = V2PrivateCandidateImage(
            raw=raw,
            device_id=info.st_dev,
            inode=info.st_ino,
            mode=info.st_mode,
            nlink=info.st_nlink,
            size_bytes=info.st_size,
            mtime_ns=info.st_mtime_ns,
            ctime_ns=info.st_ctime_ns,
            parent_device_id=parent_after.st_dev,
            parent_inode=parent_after.st_ino,
            parent_mode=parent_after.st_mode,
            parent_nlink=parent_after.st_nlink,
            parent_chain=parent_chain,
        )
    except FileExistsError as error:
        raise PathContractError(f"{context} destination already exists") from error
    except BaseException as error:
        recovery_error: BaseException | None = None
        if created_identity is None and descriptor is not None:
            try:
                recovered = os.fstat(descriptor)
                if (
                    not stat.S_ISREG(recovered.st_mode)
                    or recovered.st_nlink != 1
                ):
                    raise PathContractError(
                        f"{context} opened inode cannot be recovered safely"
                    )
                created_identity = (recovered.st_dev, recovered.st_ino)
            except BaseException as identity_error:
                recovery_error = identity_error
        if created_identity is not None:
            try:
                entry = os.stat(
                    canonical.name, dir_fd=parent_fd, follow_symlinks=False
                )
            except FileNotFoundError:
                pass
            else:
                if (entry.st_dev, entry.st_ino) != created_identity:
                    raise PathContractError(
                        f"{context} substituted leaf preserved after write failure"
                    ) from error
                os.unlink(canonical.name, dir_fd=parent_fd)
                os.fsync(parent_fd)
        if recovery_error is not None:
            raise PathContractError(
                f"{context} could not recover its opened inode for cleanup"
            ) from error
        raise
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)
    if image is None:
        raise PathContractError(f"{context} candidate image was not captured")
    try:
        _v2_replay_private_candidate(canonical, image, context=context)
    except BaseException:
        _v2_remove_owned_candidate(canonical, image)
        raise
    return image


def _v2_role5_external_path(value: str, *, candidate: bool) -> Path:
    """Accept only the two review-controlled, direct-/tmp namespaces."""

    context = (
        "role-5 design-review candidate"
        if candidate
        else "role-24 role-5 verification receipt"
    )
    path = safe_absolute_path(value, context)
    expected_leaf = (
        V2_ROLE5_CANDIDATE_BASENAME
        if candidate
        else V2_ROLE5_VERIFY_RECEIPT_BASENAME
    )
    parent_pattern = (
        V2_ROLE5_CANDIDATE_PARENT_PATTERN
        if candidate
        else V2_ROLE5_VERIFY_PARENT_PATTERN
    )
    if (
        path.parent.parent != Path("/tmp")
        or path.name != expected_leaf
        or parent_pattern.fullmatch(path.parent.name) is None
    ):
        raise PathContractError(f"{context} path shape mismatch")
    return _v2_private_candidate_path(os.fspath(path), context)


def _v2_role5_publication_fault_hook(phase: str) -> None:
    """No-op production hook with one closed nine-phase test vocabulary."""

    if phase not in V2_ROLE5_PUBLICATION_HOOK_PHASES:
        raise AssertionError(f"unknown role-5 publication hook phase: {phase}")


def _v2_role5_stage_basename() -> str:
    name = (
        ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-"
        + os.urandom(16).hex()
    )
    if V2_ROLE5_STAGE_PATTERN.fullmatch(name) is None:
        raise AssertionError("role-5 publication staging name is malformed")
    return name


def _v2_role5_live_records(root: Path) -> tuple[FormalRoleRecord, ...]:
    """Capture the exact ordered 19 reviewed source images, independently."""

    records: list[FormalRoleRecord] = []
    role_paths = dict(FORMAL_INPUT_ROLES)
    for role in V2_ROLE5_REVIEWED_ROLES:
        record, raw = formal_role_binding(root, role, role_paths[role])
        if raw != record.raw or sha256_bytes(raw) != record.sha256:
            raise ProductionAuthorityError(
                f"role-5 reviewed source capture mismatch: {role}"
            )
        records.append(record)
    if tuple(record.role for record in records) != V2_ROLE5_REVIEWED_ROLES:
        raise ProductionAuthorityError("role-5 reviewed source order mismatch")
    return tuple(records)


def _v2_role5_validate_verify_receipt(
    receipt: Any,
    *,
    candidate_sha256: str,
    input_map_sha256: str,
    size_bytes: int,
) -> dict[str, Any]:
    exact_keys(
        receipt,
        V2_ROLE5_VERIFY_RECEIPT_KEYS,
        "role-24 role-5 verification receipt",
    )
    expected = {
        "verification_status": V2_ROLE5_VERIFY_STATUS,
        "authority": V2_ROLE5_VERIFY_AUTHORITY,
        "candidate_sha256": candidate_sha256,
        "input_map_sha256": input_map_sha256,
        "size_bytes": size_bytes,
        "promotion_authorized": False,
        "artifacts_written": False,
    }
    if not exact_json_equal(receipt, expected):
        raise ProductionAuthorityError(
            "role-24 role-5 verification receipt facts mismatch"
        )
    return dict(receipt)


def _v2_role5_parse_compact_json(raw: bytes, context: str) -> Any:
    try:
        payload = strict_json_loads(raw.decode("utf-8", errors="strict"))
    except UnicodeError as error:
        raise StrictJSONError(f"{context} is not UTF-8") from error
    if raw != canonical_json_bytes(payload):
        raise StrictJSONError(f"{context} is not CJ_COMPACT_V1")
    return payload


def _v2_role5_repository_status_replay(
    root: Path,
    *,
    reviewed_commit: str,
    reviewed_tree: str,
    reviewed_rows: Sequence[Mapping[str, Any]],
    sole_untracked_path: Path | None,
    sole_untracked_identity: tuple[int, int] | None,
    context: str,
) -> None:
    """Replay symbolic main, both local refs, live remote, index, and status."""

    if (
        _v2_git_ref(root, "refs/heads/main") != reviewed_commit
        or _v2_git_ref(root, "refs/remotes/origin/main") != reviewed_commit
        or _v2_role11_live_remote_probe(root) != reviewed_commit
    ):
        raise ProductionAuthorityError(
            f"{context}: HEAD/origin/live-remote commit mismatch"
        )
    _v2_git_validate_current_repository(
        root,
        capture_commit=reviewed_commit,
        capture_tree=reviewed_tree,
        origin_main=reviewed_commit,
        required_bindings=reviewed_rows,
    )
    if _v2_git_origin_url(root) != V2_ROLE11_ORIGIN_URL:
        raise ProductionAuthorityError(f"{context}: origin URL mismatch")
    if sole_untracked_path is None:
        expected_status = b""
    else:
        repository_root, _git_dir, _prefix = _v2_git_roots(root)
        try:
            relative = sole_untracked_path.relative_to(repository_root).as_posix()
        except ValueError as error:
            raise PathContractError(
                f"{context}: publication leaf escapes repository"
            ) from error
        expected_status = f"?? {relative}\n".encode("utf-8")
    if _v2_role11_status_probe(root) != expected_status:
        raise ProductionAuthorityError(
            f"{context}: worktree is not the exact expected publication state"
        )
    if sole_untracked_path is not None:
        if sole_untracked_identity is None:
            raise AssertionError("role-5 publication status identity is absent")
        parent_fd = _open_directory_fd(sole_untracked_path.parent)
        try:
            entry = os.stat(
                sole_untracked_path.name,
                dir_fd=parent_fd,
                follow_symlinks=False,
            )
            if (
                not stat.S_ISREG(entry.st_mode)
                or stat.S_IMODE(entry.st_mode) != 0o644
                or entry.st_nlink != 1
                or (entry.st_dev, entry.st_ino) != sole_untracked_identity
            ):
                raise PathContractError(
                    f"{context}: publication inode/status mismatch"
                )
        finally:
            os.close(parent_fd)


def publish_v2_role5(
    candidate_value: str,
    role24_receipt_value: str,
    expected_sha256: str,
    expected_reviewed_commit: str,
    publication_authority: str,
    authority_root_value: str,
) -> dict[str, Any]:
    """Pure write-once transport for an externally reviewed role-5 object.

    This entry point cannot construct, capture, or synthesize either input.  It
    independently reopens the exact review candidate, role-24 verify-only
    receipt, reviewed live sources, legacy evidence, and clean/live Git state.
    The verify-only receipt is evidence, never publication authority.
    """

    if (
        type(expected_sha256) is not str
        or HEX_SHA256.fullmatch(expected_sha256) is None
    ):
        raise PathContractError("role-5 expected SHA-256 is malformed")
    if (
        type(expected_reviewed_commit) is not str
        or re.fullmatch(r"[0-9a-f]{40}", expected_reviewed_commit) is None
    ):
        raise ProductionAuthorityError(
            "role-5 expected reviewed commit is malformed"
        )
    if publication_authority != V2_ROLE5_PUBLICATION_AUTHORITY:
        raise ProductionAuthorityError("role-5 publication authority mismatch")
    root = safe_absolute_path(authority_root_value, "role-5 publication root")
    live_root = safe_absolute_path(os.fspath(ROOT), "live Paper02 root")
    if root != live_root:
        raise PathContractError(
            "role-5 publication root must equal the exact live Paper02 root"
        )

    candidate = _v2_role5_external_path(candidate_value, candidate=True)
    role24_receipt = _v2_role5_external_path(
        role24_receipt_value, candidate=False
    )
    try:
        candidate_image = _v2_snapshot_private_candidate(
            candidate,
            maximum_bytes=V2_ROLE5_CANDIDATE_MAX_BYTES,
            context="role-5 design-review candidate",
        )
        verify_image = _v2_snapshot_private_candidate(
            role24_receipt,
            maximum_bytes=V2_ROLE5_VERIFY_RECEIPT_MAX_BYTES,
            context="role-24 role-5 verification receipt",
        )
    except OSError as error:
        raise PathContractError(
            f"role-5 external input open failed: {error}"
        ) from error
    candidate_raw = candidate_image.raw
    verify_raw = verify_image.raw
    if sha256_bytes(candidate_raw) != expected_sha256:
        raise ProductionAuthorityError("role-5 candidate SHA-256 mismatch")
    candidate_payload = _v2_role5_parse_compact_json(
        candidate_raw, "role-5 design-review candidate"
    )
    validate_v2_role5_payload(candidate_payload)
    if candidate_payload["review"]["reviewed_commit"] != expected_reviewed_commit:
        raise ProductionAuthorityError(
            "role-5 candidate reviewed commit differs from explicit intent"
        )
    reviewed_rows = candidate_payload["reviewed_v2_inputs"]
    input_map_sha256 = sha256_bytes(canonical_json_bytes(reviewed_rows))
    verify_payload = _v2_role5_parse_compact_json(
        verify_raw, "role-24 role-5 verification receipt"
    )
    _v2_role5_validate_verify_receipt(
        verify_payload,
        candidate_sha256=expected_sha256,
        input_map_sha256=input_map_sha256,
        size_bytes=len(candidate_raw),
    )

    records = _v2_role5_live_records(root)
    by_role = {record.role: record for record in records}
    validate_v2_role5_repository_bindings(candidate_payload, root, by_role)
    reviewed_tree = _v2_git_commit_tree(root, expected_reviewed_commit)
    _v2_role5_repository_status_replay(
        root,
        reviewed_commit=expected_reviewed_commit,
        reviewed_tree=reviewed_tree,
        reviewed_rows=reviewed_rows,
        sole_untracked_path=None,
        sole_untracked_identity=None,
        context="role-5 initial clean repository",
    )

    destination = authority_project_file(
        root, dict(FORMAL_INPUT_ROLES)["implementation_design_review"]
    )
    publication_absence = _v2_absence_snapshot(
        (destination,), "role-5 canonical publication absence"
    )
    root_chain = _machine_publication_directory_chain(root)
    parent_chain = _machine_publication_directory_chain(destination.parent)
    root_fd = _open_directory_fd(root)
    try:
        parent_fd = _open_directory_fd(destination.parent)
    except BaseException:
        os.close(root_fd)
        raise

    def replay_directories(context: str) -> None:
        _replay_machine_publication_directory(
            root, root_fd, root_chain, f"{context} authority root"
        )
        _replay_machine_publication_directory(
            destination.parent,
            parent_fd,
            parent_chain,
            f"{context} publication parent",
        )

    def replay_external_and_review(context: str) -> None:
        _v2_replay_private_candidate(
            candidate, candidate_image, context=f"{context} candidate"
        )
        _v2_replay_private_candidate(
            role24_receipt,
            verify_image,
            context=f"{context} role-24 receipt",
        )
        current = _v2_role5_live_records(root)
        if current != records:
            raise ProductionAuthorityError(
                f"{context}: reviewed source image changed"
            )
        current_by_role = {record.role: record for record in current}
        validate_v2_role5_repository_bindings(
            candidate_payload, root, current_by_role
        )
        if (
            candidate_raw != canonical_json_bytes(candidate_payload)
            or sha256_bytes(candidate_raw) != expected_sha256
            or sha256_bytes(canonical_json_bytes(reviewed_rows))
            != input_map_sha256
        ):
            raise ProductionAuthorityError(
                f"{context}: candidate review envelope changed"
            )
        _v2_role5_validate_verify_receipt(
            verify_payload,
            candidate_sha256=expected_sha256,
            input_map_sha256=input_map_sha256,
            size_bytes=len(candidate_raw),
        )

    stage_fd: int | None = None
    stage_name: str | None = None
    stage_identity: tuple[int, int] | None = None
    stage_full_identity: tuple[int, int, int, int, int, int, int] | None = None
    locked = False
    renamed = False
    try:
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError(
                "role-5 publication parent transaction is already locked"
            ) from error
        locked = True
        replay_directories("role-5 prestage")
        replay_external_and_review("role-5 prestage")
        _v2_role5_repository_status_replay(
            root,
            reviewed_commit=expected_reviewed_commit,
            reviewed_tree=reviewed_tree,
            reviewed_rows=reviewed_rows,
            sole_untracked_path=None,
            sole_untracked_identity=None,
            context="role-5 prestage clean repository",
        )
        _v2_absence_replay(
            publication_absence, "role-5 prestage canonical absence"
        )
        stage_prefix = (
            ".R401_VAL_L3_A1_V2_DESIGN_REVIEW_AND_WITHDRAWAL.json.publish-"
        )
        if any(name.startswith(stage_prefix) for name in os.listdir(parent_fd)):
            raise PathContractError("role-5 publication stage residue exists")
        stage_name = _v2_role5_stage_basename()
        stage_fd = os.open(
            stage_name,
            os.O_RDWR | os.O_CREAT | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            0o644,
            dir_fd=parent_fd,
        )
        os.fchmod(stage_fd, 0o644)
        opened = os.fstat(stage_fd)
        stage_identity = (opened.st_dev, opened.st_ino)
        if (
            not stat.S_ISREG(opened.st_mode)
            or stat.S_IMODE(opened.st_mode) != 0o644
            or opened.st_nlink != 1
            or opened.st_size != 0
        ):
            raise PathContractError("role-5 publication stage is not empty 0644")
        _write_machine_publication_bytes(stage_fd, candidate_raw)
        _v2_role5_publication_fault_hook("AFTER_STAGE_WRITE")
        os.fsync(stage_fd)
        _v2_role5_publication_fault_hook("AFTER_STAGE_FILE_FSYNC")
        staged = os.fstat(stage_fd)
        if (
            (staged.st_dev, staged.st_ino) != stage_identity
            or not stat.S_ISREG(staged.st_mode)
            or stat.S_IMODE(staged.st_mode) != 0o644
            or staged.st_nlink != 1
            or staged.st_size != len(candidate_raw)
        ):
            raise PathContractError("role-5 staged inode mismatch")
        stage_full_identity = _machine_publication_file_identity(staged)
        os.fsync(parent_fd)
        _v2_role5_publication_fault_hook("AFTER_STAGING_PARENT_FSYNC")

        _v2_role5_publication_fault_hook("BEFORE_TERMINAL_REPLAY")
        replay_directories("role-5 terminal prerename")
        replay_external_and_review("role-5 terminal prerename")
        assert stage_name is not None and stage_identity is not None
        assert stage_full_identity is not None
        stage_path = destination.parent / stage_name
        _v2_role5_repository_status_replay(
            root,
            reviewed_commit=expected_reviewed_commit,
            reviewed_tree=reviewed_tree,
            reviewed_rows=reviewed_rows,
            sole_untracked_path=stage_path,
            sole_untracked_identity=stage_identity,
            context="role-5 terminal prerename repository",
        )
        _v2_absence_replay(
            publication_absence, "role-5 terminal prerename canonical absence"
        )
        staged_raw, staged_info = _read_machine_publication_file_at(
            parent_fd,
            stage_name,
            "role-5 terminal staging file",
            fsync_file=True,
            expected_mode=0o644,
            maximum_bytes=V2_ROLE5_CANDIDATE_MAX_BYTES,
        )
        if (
            staged_raw != candidate_raw
            or _machine_publication_file_identity(staged_info)
            != stage_full_identity
        ):
            raise PathContractError("role-5 terminal staged replay mismatch")

        _v2_role5_publication_fault_hook("BEFORE_RENAME")
        # The hook is an adversarial boundary.  Reopen the complete authority
        # envelope after it; no fact observed before the hook licenses rename.
        replay_directories("role-5 posthook immediate prerename")
        replay_external_and_review("role-5 posthook immediate prerename")
        _v2_role5_repository_status_replay(
            root,
            reviewed_commit=expected_reviewed_commit,
            reviewed_tree=reviewed_tree,
            reviewed_rows=reviewed_rows,
            sole_untracked_path=stage_path,
            sole_untracked_identity=stage_identity,
            context="role-5 posthook immediate prerename repository",
        )
        _v2_absence_replay(
            publication_absence,
            "role-5 posthook immediate canonical absence",
        )
        immediate_raw, immediate_info = _read_machine_publication_file_at(
            parent_fd,
            stage_name,
            "role-5 posthook immediate staging file",
            fsync_file=True,
            expected_mode=0o644,
            maximum_bytes=V2_ROLE5_CANDIDATE_MAX_BYTES,
        )
        if (
            immediate_raw != candidate_raw
            or _machine_publication_file_identity(immediate_info)
            != stage_full_identity
        ):
            raise PathContractError(
                "role-5 posthook immediate staged replay mismatch"
            )
        # Close the source-to-rename interval with one last byte-image capture.
        if _v2_role5_live_records(root) != records:
            raise ProductionAuthorityError(
                "role-5 reviewed source changed immediately before rename"
            )
        _rename_machine_publication_noreplace(
            parent_fd, stage_name, destination.name
        )
        renamed = True
        _v2_role5_publication_fault_hook("AFTER_RENAME")

        replay_directories("role-5 postrename")
        try:
            os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise PathContractError("role-5 rename left stage namespace present")
        open_stage = os.fstat(stage_fd)
        postrename_identity = _machine_publication_file_identity(open_stage)
        stable_indexes = (0, 1, 2, 3, 5, 6)
        if (
            any(
                postrename_identity[index] != stage_full_identity[index]
                for index in stable_indexes
            )
            or postrename_identity[4] < stage_full_identity[4]
        ):
            raise PathContractError("role-5 open stage inode changed after rename")
        canonical_raw, canonical_info = _read_machine_publication_file_at(
            parent_fd,
            destination.name,
            "canonical role-5 design review",
            fsync_file=True,
            expected_mode=0o644,
            maximum_bytes=V2_ROLE5_CANDIDATE_MAX_BYTES,
        )
        if (
            canonical_raw != candidate_raw
            or sha256_bytes(canonical_raw) != expected_sha256
            or _machine_publication_file_identity(canonical_info)
            != postrename_identity
        ):
            raise PathContractError("role-5 canonical postrename replay mismatch")
        _v2_role5_publication_fault_hook("AFTER_DESTINATION_FSYNC")
        os.fsync(parent_fd)
        _v2_role5_publication_fault_hook("AFTER_PUBLICATION_PARENT_FSYNC")

        replay_directories("role-5 ultimate replay")
        replay_external_and_review("role-5 ultimate replay")
        _v2_role5_repository_status_replay(
            root,
            reviewed_commit=expected_reviewed_commit,
            reviewed_tree=reviewed_tree,
            reviewed_rows=reviewed_rows,
            sole_untracked_path=destination,
            sole_untracked_identity=stage_identity,
            context="role-5 ultimate repository",
        )
        ultimate_raw, ultimate_info = read_pinned_regular_file(destination)
        if (
            ultimate_raw != candidate_raw
            or _machine_publication_file_identity(ultimate_info)
            != postrename_identity
        ):
            raise PathContractError("role-5 ultimate canonical replay mismatch")
        _v2_role5_publication_fault_hook("AFTER_ULTIMATE_REPLAY")

        # No hook follows this final compact pass.  Reopen canonical, both
        # external inputs, directory chains, and live Git before signing the
        # transient transport receipt.
        final_raw, final_info = _read_machine_publication_file_at(
            parent_fd,
            destination.name,
            "role-5 posthook final canonical replay",
            fsync_file=True,
            expected_mode=0o644,
            maximum_bytes=V2_ROLE5_CANDIDATE_MAX_BYTES,
        )
        if (
            final_raw != candidate_raw
            or sha256_bytes(final_raw) != expected_sha256
            or _machine_publication_file_identity(final_info)
            != postrename_identity
        ):
            raise PathContractError("role-5 posthook canonical replay mismatch")
        replay_external_and_review("role-5 posthook final")
        replay_directories("role-5 posthook final")
        _v2_role5_repository_status_replay(
            root,
            reviewed_commit=expected_reviewed_commit,
            reviewed_tree=reviewed_tree,
            reviewed_rows=reviewed_rows,
            sole_untracked_path=destination,
            sole_untracked_identity=stage_identity,
            context="role-5 posthook final repository",
        )
        verify_receipt_sha256 = sha256_bytes(verify_raw)
        receipt = {
            "schema_version": 1,
            "protocol_id": PROTOCOL_ID,
            "artifact_role": "DESIGN_REVIEW_AND_WITHDRAWAL_PUBLICATION_RECEIPT",
            "artifact_status": "PUBLISHED_WRITE_ONCE_NON_LICENSING",
            "authority": V2_ROLE5_PUBLICATION_AUTHORITY,
            "candidate_path": os.fspath(candidate),
            "canonical_path": os.fspath(destination),
            "design_review_sha256": expected_sha256,
            "reviewed_commit": expected_reviewed_commit,
            "size_bytes": len(candidate_raw),
            "mode": "0644",
            "nlink": 1,
            "serializer": "CJ_COMPACT_V1",
            "publication_method": V2_ROLE5_PUBLICATION_METHOD,
            "verify_receipt_sha256": verify_receipt_sha256,
            "input_map_sha256": input_map_sha256,
            "independent_verification_receipt_validated": True,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        if len(receipt) != 24:
            raise AssertionError("role-5 publication receipt key count mismatch")
        canonical_json_bytes(receipt)
        return receipt
    finally:
        primary_error = sys.exc_info()[1]
        cleanup_error: BaseException | None = None
        if (
            not renamed
            and stage_name is not None
            and stage_identity is None
            and stage_fd is not None
        ):
            try:
                recovered = os.fstat(stage_fd)
                if not stat.S_ISREG(recovered.st_mode) or recovered.st_nlink != 1:
                    raise PathContractError(
                        "role-5 opened stage cannot be recovered safely"
                    )
                stage_identity = (recovered.st_dev, recovered.st_ino)
            except BaseException as error:
                cleanup_error = error
        if not renamed and stage_name is not None and stage_identity is not None:
            try:
                _cleanup_machine_publication_stage(
                    parent_fd, stage_name, stage_identity
                )
            except BaseException as error:
                if cleanup_error is None:
                    cleanup_error = error
        for cleanup in (
            (lambda: os.close(stage_fd)) if stage_fd is not None else None,
            (lambda: fcntl.flock(parent_fd, fcntl.LOCK_UN)) if locked else None,
            lambda: os.close(parent_fd),
            lambda: os.close(root_fd),
        ):
            if cleanup is None:
                continue
            try:
                cleanup()
            except BaseException as error:
                if cleanup_error is None:
                    cleanup_error = error
        if cleanup_error is not None:
            if primary_error is not None:
                raise cleanup_error from primary_error
            raise cleanup_error


def _formal_private_pair_package_path(value: str, context: str) -> Path:
    package = safe_absolute_path(value, context)
    if (
        package.parent != Path("/tmp")
        or package.name in {"", ".", ".."}
        or package.name.startswith(".")
    ):
        raise PathContractError(
            f"{context} must be one owned mode-0700 direct child of /tmp"
        )
    info = os.stat(package, follow_symlinks=False)
    if (
        not stat.S_ISDIR(info.st_mode)
        or info.st_uid != os.geteuid()
        or stat.S_IMODE(info.st_mode) != 0o700
        or info.st_nlink != 2
    ):
        raise PathContractError(
            f"{context} is not an owned mode-0700 nlink-2 directory"
        )
    return package


def _formal_package_file_image(
    name: str, raw: bytes, info: os.stat_result
) -> FormalPrivatePackageFile:
    return FormalPrivatePackageFile(
        name=name,
        raw=raw,
        device_id=info.st_dev,
        inode=info.st_ino,
        mode=info.st_mode,
        nlink=info.st_nlink,
        size_bytes=info.st_size,
        mtime_ns=info.st_mtime_ns,
        ctime_ns=info.st_ctime_ns,
    )


def _snapshot_formal_private_pair_package(
    package_value: str,
    names: tuple[str, str],
    *,
    context: str,
) -> FormalPrivatePairPackage:
    if (
        type(names) is not tuple
        or len(names) != 2
        or len(set(names)) != 2
        or any(
            type(name) is not str
            or not name
            or name.startswith(".")
            or "/" in name
            or name in {".", ".."}
            for name in names
        )
    ):
        raise PathContractError(f"{context} exact two-leaf names are malformed")
    package = _formal_private_pair_package_path(package_value, context)
    lexical_initial = os.stat(package, follow_symlinks=False)
    chain = _machine_publication_directory_chain(package)
    package_fd = _open_directory_fd(package)
    locked = False
    primary_error: BaseException | None = None
    cleanup_error: BaseException | None = None
    try:
        try:
            fcntl.flock(package_fd, fcntl.LOCK_SH | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError(f"{context} is locked by another process") from error
        locked = True
        _replay_machine_publication_directory(
            package, package_fd, chain, f"{context} initial chain"
        )
        before = os.fstat(package_fd)
        if (
            not stat.S_ISDIR(before.st_mode)
            or before.st_uid != os.geteuid()
            or stat.S_IMODE(before.st_mode) != 0o700
            or before.st_nlink != 2
            or (
                before.st_dev,
                before.st_ino,
                before.st_mode,
                before.st_nlink,
                before.st_uid,
            )
            != (
                lexical_initial.st_dev,
                lexical_initial.st_ino,
                lexical_initial.st_mode,
                lexical_initial.st_nlink,
                lexical_initial.st_uid,
            )
        ):
            raise PathContractError(
                f"{context} pinned directory differs from initial lexical inode"
            )
        if tuple(sorted(os.listdir(package_fd))) != tuple(sorted(names)):
            raise PathContractError(f"{context} is not the exact two-leaf package")
        files: list[FormalPrivatePackageFile] = []
        for name in names:
            raw, info = _read_machine_publication_file_at(
                package_fd,
                name,
                f"{context} {name}",
                expected_mode=0o600,
                maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
            )
            files.append(_formal_package_file_image(name, raw, info))
        after = os.fstat(package_fd)
        directory_image = lambda info: (
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            info.st_mtime_ns,
            info.st_ctime_ns,
        )
        if (
            directory_image(after) != directory_image(before)
            or tuple(sorted(os.listdir(package_fd))) != tuple(sorted(names))
        ):
            raise PathContractError(f"{context} changed during snapshot")
        _replay_machine_publication_directory(
            package, package_fd, chain, f"{context} terminal chain"
        )
        image = FormalPrivatePairPackage(
            path=package,
            directory_device_id=before.st_dev,
            directory_inode=before.st_ino,
            directory_mode=before.st_mode,
            directory_nlink=before.st_nlink,
            directory_mtime_ns=before.st_mtime_ns,
            directory_ctime_ns=before.st_ctime_ns,
            parent_chain=chain,
            files=(files[0], files[1]),
        )
        return image
    except BaseException as error:
        primary_error = error
        raise
    finally:
        if locked:
            try:
                fcntl.flock(package_fd, fcntl.LOCK_UN)
            except BaseException as error:
                cleanup_error = cleanup_error or error
        try:
            os.close(package_fd)
        except BaseException as error:
            cleanup_error = cleanup_error or error
        if cleanup_error is not None:
            if primary_error is not None:
                raise PathContractError(
                    f"{context} snapshot failed with incomplete cleanup: "
                    f"{type(cleanup_error).__name__}: {cleanup_error}"
                ) from primary_error
            raise cleanup_error


def _replay_formal_private_pair_package(
    image: FormalPrivatePairPackage,
    names: tuple[str, str],
    *,
    context: str,
) -> None:
    replay = _snapshot_formal_private_pair_package(
        os.fspath(image.path), names, context=context
    )
    if replay != image:
        raise PathContractError(f"{context} package image changed")


def _write_formal_private_pair_package(
    package_value: str,
    payloads: Mapping[str, bytes],
    names: tuple[str, str],
    *,
    context: str,
) -> FormalPrivatePairPackage:
    if type(payloads) is not dict or set(payloads) != set(names):
        raise PathContractError(f"{context} payload set is not the exact pair")
    for name in names:
        raw = payloads[name]
        if (
            type(raw) is not bytes
            or not raw
            or len(raw) > FORMAL_PRODUCER_CANDIDATE_MAX_BYTES
        ):
            raise PathContractError(f"{context} {name} byte cap mismatch")
    package = _formal_private_pair_package_path(package_value, context)
    lexical_initial = os.stat(package, follow_symlinks=False)
    package_chain = _machine_publication_directory_chain(package)
    package_fd = _open_directory_fd(package)
    locked = False
    owned: dict[str, tuple[int, int]] = {}
    open_descriptors: dict[str, int] = {}
    written_files: dict[str, FormalPrivatePackageFile] = {}
    expected_image: FormalPrivatePairPackage | None = None
    primary_error: BaseException | None = None
    outer_cleanup_error: BaseException | None = None
    try:
        try:
            fcntl.flock(package_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError(f"{context} is locked by another process") from error
        locked = True
        _replay_machine_publication_directory(
            package, package_fd, package_chain, f"{context} initial chain"
        )
        package_before = os.fstat(package_fd)
        if (
            not stat.S_ISDIR(package_before.st_mode)
            or package_before.st_uid != os.geteuid()
            or stat.S_IMODE(package_before.st_mode) != 0o700
            or package_before.st_nlink != 2
            or (
                package_before.st_dev,
                package_before.st_ino,
                package_before.st_mode,
                package_before.st_nlink,
                package_before.st_uid,
            )
            != (
                lexical_initial.st_dev,
                lexical_initial.st_ino,
                lexical_initial.st_mode,
                lexical_initial.st_nlink,
                lexical_initial.st_uid,
            )
        ):
            raise PathContractError(
                f"{context} pinned directory differs from initial lexical inode"
            )
        if tuple(os.listdir(package_fd)) != ():
            raise PathContractError(f"{context} package is not initially empty")
        for name in names:
            descriptor = os.open(
                name,
                os.O_WRONLY | os.O_CREAT | os.O_EXCL
                | getattr(os, "O_NOFOLLOW", 0)
                | getattr(os, "O_NONBLOCK", 0),
                0o600,
                dir_fd=package_fd,
            )
            open_descriptors[name] = descriptor
            file_primary_error: BaseException | None = None
            file_close_error: BaseException | None = None
            try:
                created = os.fstat(descriptor)
                owned[name] = (created.st_dev, created.st_ino)
                os.fchmod(descriptor, 0o600)
                view = memoryview(payloads[name])
                while view:
                    written = os.write(descriptor, view)
                    if written <= 0:
                        raise OSError("short formal producer package write")
                    view = view[written:]
                os.fsync(descriptor)
                final = os.fstat(descriptor)
                if (
                    not stat.S_ISREG(final.st_mode)
                    or stat.S_IMODE(final.st_mode) != 0o600
                    or final.st_nlink != 1
                    or final.st_size != len(payloads[name])
                ):
                    raise PathContractError(f"{context} {name} final inode mismatch")
                written_files[name] = _formal_package_file_image(
                    name, payloads[name], final
                )
            except BaseException as error:
                file_primary_error = error
                if name not in owned:
                    try:
                        try:
                            recovered = os.fstat(descriptor)
                        except BaseException:
                            # Independent descriptor-stat syscall; unlike a
                            # lexical stat this cannot bind a substituted leaf.
                            recovered = os.stat(descriptor)
                        if (
                            not stat.S_ISREG(recovered.st_mode)
                            or recovered.st_nlink != 1
                        ):
                            raise PathContractError(
                                f"{context} opened {name} is not safely recoverable"
                            )
                        owned[name] = (recovered.st_dev, recovered.st_ino)
                    except BaseException as recovery_error:
                        raise PathContractError(
                            f"{context} cannot recover opened {name} for cleanup"
                        ) from recovery_error
                raise
            finally:
                # If identity recovery itself failed, keep the fd live for
                # the outer all-attempt recovery/cleanup pass.
                if name in owned or file_primary_error is None:
                    try:
                        os.close(descriptor)
                    except BaseException as error:
                        file_close_error = error
                    open_descriptors.pop(name, None)
                if file_close_error is not None:
                    if file_primary_error is not None:
                        raise PathContractError(
                            f"{context} {name} failed with incomplete descriptor cleanup"
                        ) from file_primary_error
                    raise file_close_error
        os.fsync(package_fd)
        package_after = os.fstat(package_fd)
        if (
            (package_after.st_dev, package_after.st_ino)
            != (package_before.st_dev, package_before.st_ino)
            or package_after.st_uid != os.geteuid()
            or stat.S_IMODE(package_after.st_mode) != 0o700
            or package_after.st_nlink != 2
            or tuple(sorted(os.listdir(package_fd))) != tuple(sorted(names))
        ):
            raise PathContractError(f"{context} package directory changed while writing")
        _replay_machine_publication_directory(
            package, package_fd, package_chain, f"{context} terminal chain"
        )
        expected_image = FormalPrivatePairPackage(
            path=package,
            directory_device_id=package_after.st_dev,
            directory_inode=package_after.st_ino,
            directory_mode=package_after.st_mode,
            directory_nlink=package_after.st_nlink,
            directory_mtime_ns=package_after.st_mtime_ns,
            directory_ctime_ns=package_after.st_ctime_ns,
            parent_chain=package_chain,
            files=(written_files[names[0]], written_files[names[1]]),
        )
    except BaseException as error:
        primary_error = error
        cleanup_error: BaseException | None = None
        for name, descriptor in tuple(open_descriptors.items()):
            if name not in owned:
                try:
                    try:
                        recovered = os.fstat(descriptor)
                    except BaseException:
                        recovered = os.stat(descriptor)
                    if stat.S_ISREG(recovered.st_mode) and recovered.st_nlink == 1:
                        owned[name] = (recovered.st_dev, recovered.st_ino)
                except BaseException as recovery_error:
                    cleanup_error = cleanup_error or recovery_error
            try:
                os.close(descriptor)
            except BaseException as close_error:
                cleanup_error = cleanup_error or close_error
        for name, identity in owned.items():
            try:
                entry = os.stat(name, dir_fd=package_fd, follow_symlinks=False)
            except FileNotFoundError:
                continue
            except BaseException as stat_error:
                cleanup_error = cleanup_error or stat_error
                continue
            if (entry.st_dev, entry.st_ino) != identity:
                cleanup_error = cleanup_error or PathContractError(
                    f"{context} refused to remove substituted {name}"
                )
                continue
            try:
                os.unlink(name, dir_fd=package_fd)
            except BaseException as unlink_error:
                cleanup_error = cleanup_error or unlink_error
        try:
            os.fsync(package_fd)
        except BaseException as sync_error:
            cleanup_error = cleanup_error or sync_error
        if cleanup_error is not None:
            raise PathContractError(f"{context} cleanup failed") from primary_error
        raise
    finally:
        if locked:
            try:
                fcntl.flock(package_fd, fcntl.LOCK_UN)
            except BaseException as error:
                outer_cleanup_error = outer_cleanup_error or error
        try:
            os.close(package_fd)
        except BaseException as error:
            outer_cleanup_error = outer_cleanup_error or error
        if outer_cleanup_error is not None:
            if primary_error is not None:
                raise PathContractError(
                    f"{context} writer failed with incomplete cleanup: "
                    f"{type(outer_cleanup_error).__name__}: {outer_cleanup_error}"
                ) from primary_error
            raise outer_cleanup_error
    if expected_image is None:
        raise PathContractError(f"{context} completed without a pinned image")
    completed = _snapshot_formal_private_pair_package(
        os.fspath(package), names, context=f"{context} completed"
    )
    if completed != expected_image:
        raise PathContractError(
            f"{context} terminal lexical package differs from written inode image"
        )
    return completed


def capture_v2_main_freeze_candidate(
    output_value: str,
    authority_root: Path | str = ROOT,
) -> tuple[dict[str, Any], str]:
    """Build role 54 into one private file; never publish its canonical path."""

    root = safe_absolute_path(os.fspath(authority_root), "main candidate authority root")
    output = _v2_private_candidate_path(output_value, "main candidate output")
    absence = _v2_absence_snapshot(
        (
            root / "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json",
            root / "results/r401_val_l3_a1_v2_all_slabs",
            root / "results/r401_val_l3_a1_v2_all_slabs.operational",
        ),
        "V2 main candidate canonical absence",
    )
    bindings, images = capture_formal_input_roles(root)
    try:
        machine = strict_json_loads(images["machine_freeze"].decode("utf-8"))
    except UnicodeError as error:
        raise StrictJSONError("V2 machine freeze is not UTF-8") from error
    if images["machine_freeze"] != canonical_json_bytes(machine):
        raise StrictJSONError("V2 machine freeze is not canonical JSON")
    payload = build_v2_main_freeze_payload(bindings, machine)
    raw = canonical_json_bytes(payload)
    owned_image: V2PrivateCandidateImage | None = None
    try:
        owned_image = _v2_write_private_candidate(
            output,
            raw,
            maximum_bytes=V2_MAIN_CANDIDATE_MAX_BYTES,
            context="main candidate output",
        )
        replay_bindings, replay_images = capture_formal_input_roles(root)
        if replay_bindings != bindings or replay_images != images:
            raise ProductionAuthorityError(
                "V2 input role changed during main candidate construction"
            )
        _v2_absence_replay(absence, "V2 main candidate canonical absence")
        _v2_replay_private_candidate(
            output, owned_image, context="main candidate final replay"
        )
    except BaseException:
        if owned_image is not None:
            _v2_remove_owned_candidate(output, owned_image)
        raise
    return payload, sha256_bytes(raw)


def run_v2_role11_second_fresh_rebuild(
    output_value: str,
    authority_root: Path | str = ROOT,
) -> dict[str, Any]:
    """Compile one temporary role-17 image, compare it, then remove it."""

    root = safe_absolute_path(os.fspath(authority_root), "rebuild authority root")
    output = _v2_private_candidate_path(output_value, "second rebuild output")
    if V2_ROLE11_REBUILD_OUTPUT.fullmatch(os.fspath(output)) is None:
        raise PathContractError("second rebuild output path does not match V2 contract")
    parent_fd = _open_directory_fd(output.parent)
    parent_info = os.fstat(parent_fd)
    parent_identity = (
        parent_info.st_dev,
        parent_info.st_ino,
        parent_info.st_mode,
        parent_info.st_nlink,
    )
    locked = False
    owned_output_identity: tuple[int, int, int, int, int, int, int] | None = None
    cleanup_error: BaseException | None = None
    primary_error: BaseException | None = None
    try:
        if (
            not stat.S_ISDIR(parent_info.st_mode)
            or parent_info.st_uid != os.geteuid()
            or stat.S_IMODE(parent_info.st_mode) != 0o700
            or parent_info.st_nlink != 2
            or tuple(os.listdir(parent_fd)) != ()
        ):
            raise PathContractError("second rebuild parent is not initially empty")
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError("second rebuild parent is already locked") from error
        locked = True
        machine_path = authority_project_file(
            root, dict(FORMAL_INPUT_ROLES)["machine_freeze"]
        )
        machine_payload, machine_raw, _machine_info = strict_json_image(
            machine_path, require_canonical=True
        )
        machine = _validate_formal_machine_envelope(machine_payload)
        if machine_raw != canonical_json_bytes(machine):
            raise StrictJSONError("second rebuild machine image mismatch")
        source_relative = dict(FORMAL_INPUT_ROLES)["branch_evaluator_source"]
        binary_relative = dict(FORMAL_INPUT_ROLES)["branch_evaluator_binary"]
        source_path = authority_project_file(root, source_relative)
        binary_path = authority_project_file(root, binary_relative)
        source_raw, source_info = read_pinned_regular_file(source_path)
        binary_before_raw, binary_before = read_pinned_regular_file(binary_path)
        frozen_binary = machine["branch_binary"]
        if (
            sha256_bytes(source_raw) != frozen_binary["source_sha256"]
            or sha256_bytes(binary_before_raw) != frozen_binary["sha256"]
            or len(binary_before_raw) != frozen_binary["size_bytes"]
            or stat.S_IMODE(binary_before.st_mode) != 0o755
        ):
            raise ProductionAuthorityError(
                "second rebuild frozen source/binary mismatch"
            )
        recipe = machine["compiler"]["build_recipe"]
        template = recipe["argv_template"]
        if (
            type(template) is not list
            or template.count("@STAGING_BINARY@") != 1
            or template[-1] != "@STAGING_BINARY@"
        ):
            raise ProductionAuthorityError("second rebuild frozen recipe mismatch")
        argv = [*template[:-1], os.fspath(output)]
        try:
            completed = _capture_command(
                argv,
                cwd=root,
                environment=recipe["environment"],
                timeout_seconds=600,
                umask=0o022,
            )
        finally:
            try:
                observed = os.stat(
                    output.name, dir_fd=parent_fd, follow_symlinks=False
                )
            except FileNotFoundError:
                pass
            else:
                if not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
                    raise PathContractError(
                        "second rebuild produced/received a foreign nonregular leaf"
                    )
                owned_output_identity = _machine_publication_file_identity(observed)
        if completed.returncode != 0 or completed.stdout or completed.stderr:
            raise ProductionAuthorityError(
                "second rebuild compiler failed or produced a transcript"
            )
        if owned_output_identity is None:
            raise ProductionAuthorityError("second rebuild compiler created no output")
        staged_raw, staged_info = _read_machine_publication_file_at(
            parent_fd,
            output.name,
            "second rebuild staging output",
            expected_mode=0o755,
        )
        if _machine_publication_file_identity(staged_info) != owned_output_identity:
            raise PathContractError("second rebuild output changed after observation")
        binary_after_raw, binary_after = read_pinned_regular_file(binary_path)
        source_after_raw, source_after = read_pinned_regular_file(source_path)
        if (
            staged_raw != binary_before_raw
            or binary_after_raw != binary_before_raw
            or source_after_raw != source_raw
            or stat.S_IMODE(staged_info.st_mode) != 0o755
            or _stat_identity(binary_after) != _stat_identity(binary_before)
            or _stat_identity(source_after) != _stat_identity(source_info)
        ):
            raise ProductionAuthorityError(
                "second rebuild changed persistent inputs or differed byte-for-byte"
            )
        receipt = {
            "verification_status": "PASS_SECOND_FRESH_REBUILD",
            "authority": "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY",
            "source_path": source_relative,
            "source_sha256": sha256_bytes(source_raw),
            "persistent_binary_path": binary_relative,
            "persistent_before_sha256": sha256_bytes(binary_before_raw),
            "persistent_after_sha256": sha256_bytes(binary_after_raw),
            "persistent_before_device_id": binary_before.st_dev,
            "persistent_before_inode": binary_before.st_ino,
            "persistent_after_device_id": binary_after.st_dev,
            "persistent_after_inode": binary_after.st_ino,
            "persistent_identity_unchanged": True,
            "persistent_overwrite_performed": False,
            "staging_output_sha256": sha256_bytes(staged_raw),
            "staging_output_size_bytes": len(staged_raw),
            "staging_output_mode": "0755",
            "staging_output_removed": True,
            "byte_for_byte_equal": True,
            "scientific_evaluator_dispatched": False,
        }
        roles = {
            "branch_evaluator_source": {
                "path": source_relative,
                "sha256": sha256_bytes(source_raw),
            },
            "branch_evaluator_binary": {
                "path": binary_relative,
                "sha256": sha256_bytes(binary_before_raw),
                "size_bytes": len(binary_before_raw),
            },
        }
        _v2_role11_second_rebuild_receipt(
            receipt, roles, "second rebuild receipt"
        )
    except BaseException as error:
        primary_error = error
        raise
    finally:
        parent_safe_to_remove = True
        if owned_output_identity is not None:
            try:
                entry = os.stat(
                    output.name, dir_fd=parent_fd, follow_symlinks=False
                )
            except FileNotFoundError:
                pass
            except BaseException as error:
                cleanup_error = cleanup_error or error
                parent_safe_to_remove = False
            else:
                if _machine_publication_file_identity(entry) != owned_output_identity:
                    cleanup_error = PathContractError(
                        "second rebuild refused to remove a substituted output"
                    )
                    parent_safe_to_remove = False
                else:
                    try:
                        os.unlink(output.name, dir_fd=parent_fd)
                        os.fsync(parent_fd)
                    except OSError as error:
                        cleanup_error = PathContractError(
                            f"second rebuild owned-output cleanup failed: {error}"
                        )
                        parent_safe_to_remove = False
        try:
            remaining = tuple(os.listdir(parent_fd))
        except BaseException as error:
            cleanup_error = cleanup_error or error
            parent_safe_to_remove = False
        else:
            if remaining:
                cleanup_error = cleanup_error or PathContractError(
                    "second rebuild preserved a foreign nonempty parent"
                )
                parent_safe_to_remove = False
        try:
            current_parent = os.fstat(parent_fd)
        except BaseException as error:
            cleanup_error = cleanup_error or error
            parent_safe_to_remove = False
        else:
            if (
                current_parent.st_dev,
                current_parent.st_ino,
                current_parent.st_mode,
                current_parent.st_nlink,
            ) != parent_identity:
                cleanup_error = cleanup_error or PathContractError(
                    "second rebuild parent inode changed during lifecycle"
                )
                parent_safe_to_remove = False
        if locked:
            try:
                fcntl.flock(parent_fd, fcntl.LOCK_UN)
            except OSError as error:
                cleanup_error = cleanup_error or PathContractError(
                    f"second rebuild parent unlock failed: {error}"
                )
        try:
            os.close(parent_fd)
        except BaseException as error:
            cleanup_error = cleanup_error or error
        if parent_safe_to_remove:
            tmp_fd: int | None = None
            try:
                tmp_fd = _open_directory_fd(Path("/tmp"))
                lexical_parent = os.stat(
                    output.parent.name, dir_fd=tmp_fd, follow_symlinks=False
                )
                if (
                    lexical_parent.st_dev,
                    lexical_parent.st_ino,
                    lexical_parent.st_mode,
                    lexical_parent.st_nlink,
                ) != parent_identity:
                    raise PathContractError(
                        "second rebuild lexical parent was substituted"
                    )
                os.rmdir(output.parent.name, dir_fd=tmp_fd)
                os.fsync(tmp_fd)
                try:
                    os.stat(
                        output.parent.name,
                        dir_fd=tmp_fd,
                        follow_symlinks=False,
                    )
                except FileNotFoundError:
                    pass
                else:
                    raise PathContractError(
                        "second rebuild parent remained after cleanup"
                    )
            except BaseException as error:
                cleanup_error = cleanup_error or error
            finally:
                if tmp_fd is not None:
                    try:
                        os.close(tmp_fd)
                    except BaseException as error:
                        cleanup_error = cleanup_error or error
        if cleanup_error is not None:
            if primary_error is not None:
                raise PathContractError(
                    "second rebuild failed with incomplete cleanup: "
                    f"{type(cleanup_error).__name__}: {cleanup_error}"
                ) from primary_error
            raise cleanup_error
    return receipt


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
        root, "research/route_a_wave_trace/R401_VAL_L3_A1_V2_FREEZE.json"
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


def _capture_formal_run_config(
    snapshot: FormalAuthoritySnapshot,
) -> tuple[dict[str, Any], bytes, os.stat_result]:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    payload, raw, info = strict_json_image(
        result / "run_config.json", require_canonical=True
    )
    validate_formal_canonical_run_binding(payload, snapshot)
    return dict(payload), raw, info


def _formal_null_status_replay(payload: Mapping[str, Any], context: str) -> None:
    for key in (
        "component_status", "milestone_status", "theorem_status", "final_status"
    ):
        if payload.get(key) is not None:
            raise CorruptGeneration(f"{context} overclaims {key}")


def _formal_static_capture_plan(
    snapshot: FormalAuthoritySnapshot,
    result: Path,
    cell: CellKey,
    run_sha256: str,
    record: Mapping[str, Any],
) -> FormalStaticTransactionPlan:
    invocation = record["semantic_invocation"]
    exact_keys(
        invocation, FORMAL_STATIC_INVOCATION_KEYS,
        "formal static live semantic invocation",
    )
    semantic = invocation["argv"]
    if (
        type(semantic) is not list
        or len(semantic) != 26
        or not all(type(value) is str for value in semantic)
        or semantic[-1] != "<STAGING_PROOF_PATH>"
        or invocation["exact_string_count"] != 26
        or type(invocation["exact_string_count"]) is not int
        or invocation["output_token"] != "<STAGING_PROOF_PATH>"
        or invocation["argv_sha256"]
        != sha256_bytes(canonical_json_bytes(semantic))
    ):
        raise CorruptGeneration("formal static semantic invocation mismatch")
    evaluator = _formal_role(snapshot, "static_evaluator")
    checker = _formal_role(snapshot, "static_checker_source")
    final_plan = _formal_role(snapshot, "l1_final_plan")
    l1_roles = tuple(
        _formal_role(snapshot, role) for role in FORMAL_STATIC_L1_SOURCE_ROLES
    )
    cell_root = result / "static/cells" / str(cell.precision_bits) / cell.slab_id
    proof_path = cell_root / "proof.json"
    try:
        frozen_plan_payload = strict_json_loads(final_plan.raw.decode("utf-8"))
    except UnicodeError as error:
        raise CorruptGeneration("formal static frozen L1 plan is not UTF-8") from error
    frozen_record = validate_plan_payload(frozen_plan_payload)[cell.slab_id]
    frozen_record_sha256 = sha256_bytes(canonical_json_bytes(frozen_record))
    expected_semantic = (
        sys.executable,
        os.fspath(authority_project_file(snapshot.authority_root, evaluator.path)),
        "--slab-id",
        cell.slab_id,
        "--precision-bits",
        str(cell.precision_bits),
        "--epsilon-lower",
        frozen_record["epsilon_lower"],
        "--epsilon-upper",
        frozen_record["epsilon_upper"],
        "--matrix-id",
        canonical_matrix_id(),
        "--freeze-sha256",
        snapshot.main_freeze_sha256,
        "--run-config-sha256",
        run_sha256,
        "--plan-record-sha256",
        frozen_record_sha256,
        "--max-depth",
        str(candidate_limits()["static"]["max_depth_per_tree"]),
        "--max-nodes-per-tree",
        str(candidate_limits()["static"]["max_nodes_per_tree"]),
        "--max-nodes-per-cell",
        str(candidate_limits()["static"]["max_nodes_per_cell"]),
        "--output",
        "<STAGING_PROOF_PATH>",
    )
    if tuple(semantic) != expected_semantic:
        raise CorruptGeneration(
            "formal static semantic invocation differs from frozen task ABI"
        )
    plan = FormalStaticTransactionPlan(
        cell=cell,
        evaluator_path=authority_project_file(snapshot.authority_root, evaluator.path),
        evaluator_sha256=evaluator.sha256,
        proof_path=proof_path,
        stdout_path=cell_root / "stdout.txt",
        stderr_path=cell_root / "stderr.txt",
        record_path=cell_root / "record.json",
        argv=tuple([*semantic[:-1], os.fspath(proof_path)]),
        semantic_argv=tuple(semantic),
        semantic_argv_sha256=invocation["argv_sha256"],
        checker_sha256=checker.sha256,
        l1_final_plan_sha256=final_plan.sha256,
        l1_release_chain_sha256=tuple(
            (role.path, role.sha256) for role in l1_roles
        ),
        matrix_id=canonical_matrix_id(),
        freeze_sha256=snapshot.main_freeze_sha256,
        main_freeze_sha256=snapshot.main_freeze_sha256,
        run_config_sha256=run_sha256,
    )
    plan.validate()
    return plan


def _capture_formal_static_manifest_entry(
    result: Path,
    cell: CellKey,
    main_sha256: str,
    run_sha256: str,
    snapshot: FormalAuthoritySnapshot,
) -> dict[str, Any]:
    relative = (
        f"static/cell_manifests/{cell.precision_bits}/{cell.slab_id}.json"
    )
    manifest, raw, _ = strict_json_image(
        result / Path(relative), require_canonical=True
    )
    exact_keys(manifest, FORMAL_STATIC_MANIFEST_KEYS, "formal static live manifest")
    if (
        manifest["schema_version"] != SCHEMA_VERSION
        or manifest["protocol_id"] != PROTOCOL_ID
        or manifest["artifact_role"] != "STATIC_CELL_MANIFEST"
        or manifest["authority"] != "PRODUCER_ONLY"
        or manifest["scientific_licensing_enabled"] is not False
        or manifest["matrix_id"] != canonical_matrix_id()
        or manifest["freeze_sha256"] != main_sha256
        or manifest["main_freeze_sha256"] != main_sha256
        or manifest["run_config_sha256"] != run_sha256
        or not exact_json_equal(manifest["cell"], cell.payload())
        or manifest["scheduler_classification"] != "COMMITTED_EVALUATOR_RESULT"
        or manifest["evaluator_status"] != "STATIC_CELL_CERTIFIED"
        or manifest["claim_boundary"] != FORMAL_STATIC_CELL_CLAIM_BOUNDARY
    ):
        raise CorruptGeneration("formal static live manifest identity mismatch")
    _formal_null_status_replay(manifest, "formal static live manifest")
    if (
        type(manifest["semantic_invocation_sha256"]) is not str
        or HEX_SHA256.fullmatch(manifest["semantic_invocation_sha256"]) is None
    ):
        raise CorruptGeneration("formal static invocation hash is malformed")
    files = manifest["files"]
    exact_keys(files, set(FORMAL_STATIC_FILE_NAMES), "formal static file bindings")
    cell_root = result / "static/cells" / str(cell.precision_bits) / cell.slab_id
    live_raws: dict[str, bytes] = {}
    for name in FORMAL_STATIC_FILE_NAMES:
        binding = files[name]
        exact_keys(binding, FORMAL_STATIC_FILE_BINDING_KEYS, f"formal static {name}")
        payload_raw, _ = read_pinned_regular_file(cell_root / name)
        live_raws[name] = payload_raw
        serializer = "CJ_COMPACT_V1" if name in {"proof.json", "record.json"} else "RAW_BYTES"
        if (
            binding["path"] != name
            or binding["sha256"] != sha256_bytes(payload_raw)
            or binding["size_bytes"] != len(payload_raw)
            or binding["serializer"] != serializer
            or binding["truncated"] is not False
        ):
            raise CorruptGeneration(f"formal static {name} binding mismatch")
    if not exact_json_equal(manifest["record"], files["record.json"]):
        raise CorruptGeneration("formal static record edge mismatch")
    objects: dict[str, dict[str, Any]] = {}
    for name in ("proof.json", "record.json"):
        try:
            payload = strict_json_loads(live_raws[name].decode("utf-8"))
        except UnicodeError as error:
            raise CorruptGeneration(f"formal static {name} is not UTF-8") from error
        if live_raws[name] != canonical_json_bytes(payload) or type(payload) is not dict:
            raise CorruptGeneration(f"formal static {name} is noncanonical")
        if (
            payload.get("authority") != "PRODUCER_ONLY"
            or payload.get("scientific_licensing_enabled") is not False
            or payload.get("matrix_id") != canonical_matrix_id()
            or payload.get("freeze_sha256") != main_sha256
            or payload.get("run_config_sha256") != run_sha256
            or payload.get("claim_boundary") != FORMAL_STATIC_CELL_CLAIM_BOUNDARY
        ):
            raise CorruptGeneration(f"formal static {name} root authority mismatch")
        _formal_null_status_replay(payload, f"formal static {name}")
        objects[name] = payload
    proof = objects["proof.json"]
    record = objects["record.json"]
    exact_keys(record, FORMAL_STATIC_RECORD_KEYS, "formal static live record")
    plan = _formal_static_capture_plan(
        snapshot, result, cell, run_sha256, record
    )
    expected_task = {
        "epsilon_lower": _semantic_flag(plan, "--epsilon-lower"),
        "epsilon_upper": _semantic_flag(plan, "--epsilon-upper"),
        "plan_record_sha256": _semantic_flag(plan, "--plan-record-sha256"),
    }
    exact_keys(record["task"], FORMAL_STATIC_TASK_KEYS, "formal static live task")
    exact_keys(
        record["scheduler_result"], FORMAL_STATIC_SCHEDULER_RESULT_KEYS,
        "formal static live scheduler result",
    )
    exact_keys(
        record["evaluator_result"], FORMAL_STATIC_EVALUATOR_RESULT_KEYS,
        "formal static live evaluator result",
    )
    expected_scheduler = {
        "classification": "COMMITTED_EVALUATOR_RESULT",
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "return_code": 0,
        "proof_kind": "EVALUATOR_PROOF",
        "reason_code": None,
    }
    expected_evaluator = {
        "status": "STATIC_CELL_CERTIFIED",
        "return_code": 0,
        "status_line_count": 1,
    }
    expected_record_files = {
        name: files[name] for name in ("proof.json", "stdout.txt", "stderr.txt")
    }
    if (
        record["schema_version"] != SCHEMA_VERSION
        or record["protocol_id"] != PROTOCOL_ID
        or record["artifact_role"] != "STATIC_CELL_RECORD"
        or record["main_freeze_sha256"] != main_sha256
        or not exact_json_equal(record["cell"], cell.payload())
        or not exact_json_equal(record["task"], expected_task)
        or not exact_json_equal(record["scheduler_result"], expected_scheduler)
        or not exact_json_equal(record["evaluator_result"], expected_evaluator)
        or not exact_json_equal(record["files"], expected_record_files)
        or not exact_json_equal(record["limits"], formal_limits()["static"])
        or record["semantic_invocation"]["argv_sha256"]
        != manifest["semantic_invocation_sha256"]
        or live_raws["stdout.txt"] != b"evaluator_status=STATIC_CELL_CERTIFIED\n"
        or live_raws["stderr.txt"] != b""
    ):
        raise CorruptGeneration("formal static producer pass ABI mismatch")
    try:
        _validate_formal_static_evaluator_proof(
            plan, proof, "STATIC_CELL_CERTIFIED"
        )
    except SchedulerContractError as error:
        raise CorruptGeneration("formal static proof ABI mismatch") from error
    return {
        "cell": cell.payload(),
        "path": relative,
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
    }


def _formal_branch_capture_context(
    snapshot: FormalAuthoritySnapshot,
    run_sha256: str,
) -> tuple[Any, Any, Any, tuple[Any, ...]]:
    runtime_role = _formal_role(snapshot, "branch_runtime")
    runtime = _load_formal_branch_runtime(runtime_role)
    source = _formal_role(snapshot, "branch_evaluator_source")
    binary = _formal_role(snapshot, "branch_evaluator_binary")
    plan = _formal_role(snapshot, "l1_final_plan")
    l1_summary = _formal_role(snapshot, "l1_summary")
    try:
        machine_payload = strict_json_loads(
            snapshot.machine_freeze_raw.decode("utf-8")
        )
        plan_payload = strict_json_loads(plan.raw.decode("utf-8"))
        l1_summary_payload = strict_json_loads(l1_summary.raw.decode("utf-8"))
    except UnicodeError as error:
        raise CorruptGeneration(
            "formal branch authority payload is not UTF-8"
        ) from error
    machine = _validate_formal_machine_envelope(machine_payload)
    capd = machine["capd"]
    branch_binary = machine["branch_binary"]
    bindings = runtime.BranchBindings(
        matrix_id=canonical_matrix_id(),
        freeze_sha256=snapshot.main_freeze_sha256,
        run_config_sha256=run_sha256,
        evaluator_source_path=os.fspath(
            authority_project_file(snapshot.authority_root, source.path)
        ),
        evaluator_source_sha256=source.sha256,
        evaluator_binary_sha256=binary.sha256,
        capd_commit=capd["commit"],
        capd_flags_sha256=capd["raw_flags_sha256"],
        runtime_libraries_sha256=branch_binary["runtime_libraries_sha256"],
    )
    budget_values = {
        key: formal_limits()["branch"][key]
        for key in (
            "timeout_ms", "term_grace_ms", "pipe_close_grace_ms",
            "stdout_bytes", "stderr_bytes", "record_bytes",
            "total_cell_bytes",
        )
    }
    budgets = runtime.BranchBudgets(**budget_values)
    bindings.validate()
    budgets.validate()
    tasks = build_branch_tasks_from_payloads(
        authority_project_file(snapshot.authority_root, binary.path),
        plan_payload,
        l1_summary_payload,
        runtime=runtime,
    )
    if len(tasks) != 102:
        raise CorruptGeneration("formal branch task matrix is not exact 102")
    return runtime, bindings, budgets, tasks


def _capture_formal_branch_manifest_entry(
    result: Path,
    cell: CellKey,
    main_sha256: str,
    run_sha256: str,
    runtime_context: tuple[Any, Any, Any, Any],
) -> dict[str, Any]:
    relative = (
        f"branch/cell_manifests/{cell.precision_bits}/{cell.slab_id}.json"
    )
    manifest, raw, _ = strict_json_image(result / Path(relative))
    if raw != pretty_json_bytes(manifest):
        raise CorruptGeneration("formal branch live manifest is not CJ_PRETTY_2_V1")
    exact_keys(manifest, FORMAL_BRANCH_MANIFEST_KEYS, "formal branch live manifest")
    expected_budgets = {
        key: formal_limits()["branch"][key]
        for key in (
            "timeout_ms", "term_grace_ms", "pipe_close_grace_ms",
            "stdout_bytes", "stderr_bytes", "record_bytes", "total_cell_bytes",
        )
    }
    if (
        manifest["schema_version"] != SCHEMA_VERSION
        or manifest["protocol_id"] != PROTOCOL_ID
        or manifest["artifact_role"] != "BRANCH_CELL_MANIFEST"
        or manifest["authority"] != "PRODUCER_ONLY"
        or manifest["scientific_licensing_enabled"] is not False
        or manifest["matrix_id"] != canonical_matrix_id()
        or manifest["freeze_sha256"] != main_sha256
        or manifest["run_config_sha256"] != run_sha256
        or not exact_json_equal(manifest["cell_identity"], cell.payload())
        or not exact_json_equal(manifest["budgets"], expected_budgets)
        or manifest["claim_boundary"] != FORMAL_BRANCH_CELL_CLAIM_BOUNDARY
    ):
        raise CorruptGeneration("formal branch live manifest identity mismatch")
    _formal_null_status_replay(manifest, "formal branch live manifest")
    if (
        type(manifest["task_binding_sha256"]) is not str
        or HEX_SHA256.fullmatch(manifest["task_binding_sha256"]) is None
    ):
        raise CorruptGeneration("formal branch task hash is malformed")
    expected_paths = {
        f"branch/cells/{cell.precision_bits}/{cell.slab_id}/{name}"
        for name in ("stdout.txt", "stderr.txt", "record.json")
    }
    files = manifest["files"]
    exact_keys(files, expected_paths, "formal branch live file bindings")
    live_payloads: dict[str, bytes] = {}
    for relative_file, digest in files.items():
        if type(digest) is not str or HEX_SHA256.fullmatch(digest) is None:
            raise CorruptGeneration("formal branch payload digest is malformed")
        payload_raw, _ = read_pinned_regular_file(result / Path(relative_file))
        live_payloads[Path(relative_file).name] = payload_raw
        if sha256_bytes(payload_raw) != digest:
            raise CorruptGeneration("formal branch payload hash mismatch")
        if relative_file.endswith("/record.json"):
            try:
                payload = strict_json_loads(payload_raw.decode("utf-8"))
            except UnicodeError as error:
                raise CorruptGeneration("formal branch record is not UTF-8") from error
            if payload_raw != pretty_json_bytes(payload) or type(payload) is not dict:
                raise CorruptGeneration("formal branch record is noncanonical")
            if (
                payload.get("authority") != "PRODUCER_ONLY"
                or payload.get("scientific_licensing_enabled") is not False
                or payload.get("matrix_id") != canonical_matrix_id()
                or payload.get("freeze_sha256") != main_sha256
                or payload.get("run_config_sha256") != run_sha256
                or payload.get("claim_boundary") != FORMAL_BRANCH_CELL_CLAIM_BOUNDARY
            ):
                raise CorruptGeneration("formal branch record authority mismatch")
            _formal_null_status_replay(payload, "formal branch record")
    runtime, task, bindings, budgets = runtime_context
    try:
        validated_record, validated_manifest = runtime.validate_committed_branch_cell(
            result, task, bindings, budgets
        )
    except Exception as error:
        raise CorruptGeneration(
            "formal branch producer cell ABI replay failed"
        ) from error
    exact_keys(
        validated_record, FORMAL_BRANCH_RECORD_KEYS,
        "formal branch validated record",
    )
    scheduler = validated_record["scheduler_result"]
    if (
        not exact_json_equal(validated_manifest, manifest)
        or scheduler["classification"] != "COMMITTED_EVALUATOR_RESULT"
        or scheduler["evaluator_status"] != "BRANCH_CELL_CERTIFIED"
        or scheduler["return_code"] != 0
        or type(scheduler["return_code"]) is not int
        or scheduler["failure_reason"] is not None
        or live_payloads.get("stderr.txt") != b""
    ):
        raise CorruptGeneration("formal branch producer pass ABI mismatch")
    return {
        "cell": cell.payload(),
        "path": relative,
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "evaluator_status": "BRANCH_CELL_CERTIFIED",
        "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
    }


def _capture_formal_component_generation_image(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    *,
    component_entries: frozenset[str] = frozenset(),
) -> FormalLiveGenerationImage:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    operational = result.with_name(result.name + ".operational")
    absence = _v2_absence_snapshot(
        (operational,), f"formal {component.lower()} operational quiescence"
    )
    root_chain = _machine_publication_directory_chain(result)
    directories: list[
        tuple[str, int, int, int, int, int, int, tuple[str, ...]]
    ] = []
    files: list[tuple[str, str, int, int, int, int, int, int, int]] = []

    def capture_directory(path: Path, expected_names: set[str]) -> None:
        descriptor = _open_directory_fd(path)
        try:
            info = os.fstat(descriptor)
            if (
                not stat.S_ISDIR(info.st_mode)
                or stat.S_IMODE(info.st_mode) != 0o755
                or info.st_nlink < 2
            ):
                raise PathContractError(
                    f"formal canonical directory mode/link mismatch: {path}"
                )
            names = tuple(sorted(os.listdir(descriptor)))
            if set(names) != expected_names:
                raise CorruptGeneration(
                    f"formal {component.lower()} namespace mismatch at {path}"
                )
            relative = path.relative_to(result).as_posix()
            directories.append(
                (
                    relative,
                    info.st_dev,
                    info.st_ino,
                    info.st_mode,
                    info.st_nlink,
                    info.st_mtime_ns,
                    info.st_ctime_ns,
                    names,
                )
            )
        finally:
            os.close(descriptor)

    def capture_file(path: Path) -> None:
        raw, info = read_pinned_regular_file(path)
        if stat.S_IMODE(info.st_mode) != 0o644 or info.st_nlink != 1:
            raise PathContractError(
                f"formal canonical input mode/link mismatch: {path}"
            )
        files.append(
            (
                path.relative_to(result).as_posix(),
                sha256_bytes(raw),
                info.st_dev,
                info.st_ino,
                info.st_mode,
                info.st_nlink,
                info.st_size,
                info.st_mtime_ns,
                info.st_ctime_ns,
            )
        )

    capture_file(result / "run_config.json")
    lower = component.lower()
    component_root = result / lower
    component_fd = _open_directory_fd(component_root)
    try:
        component_info = os.fstat(component_fd)
        if (
            not stat.S_ISDIR(component_info.st_mode)
            or stat.S_IMODE(component_info.st_mode) != 0o755
            or component_info.st_nlink < 2
        ):
            raise PathContractError(
                f"formal {lower} component-root mode/link mismatch"
            )
        component_names = set(os.listdir(component_fd))
        expected_component_names = {
            "cells", "cell_manifests",
        } | set(component_entries)
        if component_names != expected_component_names:
            raise CorruptGeneration(
                f"formal {lower} component-root namespace mismatch"
            )
        publication_parent = (
            lower,
            component_info.st_dev,
            component_info.st_ino,
            component_info.st_mode,
            component_info.st_nlink,
        )
    finally:
        os.close(component_fd)
    cells_root = result / lower / "cells"
    manifests_root = result / lower / "cell_manifests"
    precision_names = {str(bits) for bits in PRECISIONS}
    capture_directory(cells_root, precision_names)
    capture_directory(manifests_root, precision_names)
    cell_names = set(SLAB_IDS)
    manifest_names = {f"{slab}.json" for slab in SLAB_IDS}
    payload_names = (
        {"proof.json", "stdout.txt", "stderr.txt", "record.json"}
        if component == "STATIC"
        else {"stdout.txt", "stderr.txt", "record.json"}
    )
    for bits in PRECISIONS:
        cells_precision = cells_root / str(bits)
        manifests_precision = manifests_root / str(bits)
        capture_directory(cells_precision, cell_names)
        capture_directory(manifests_precision, manifest_names)
        for slab in SLAB_IDS:
            cell = cells_precision / slab
            capture_directory(cell, payload_names)
            for name in sorted(payload_names):
                capture_file(cell / name)
            capture_file(manifests_precision / f"{slab}.json")
    _v2_absence_replay(
        absence, f"formal {component.lower()} operational quiescence"
    )
    if _machine_publication_directory_chain(result) != root_chain:
        raise PathContractError(
            f"formal {component.lower()} result ancestor chain changed"
        )
    return FormalLiveGenerationImage(
        root_chain=root_chain,
        publication_parent=publication_parent,
        directories=tuple(directories),
        files=tuple(files),
        operational_absence=absence,
    )


def capture_formal_component_aggregate_inputs(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    *,
    _component_entries: frozenset[str] = frozenset(),
) -> tuple[
    str,
    tuple[dict[str, Any], ...],
    FormalLiveGenerationImage,
]:
    """Independently reopen role 55 and all 102 canonical cell archives."""

    if component not in COMPONENTS:
        raise SchedulerContractError("formal aggregate component is invalid")
    relevant = (
        ("static_evaluator",)
        if component == "STATIC"
        else ("branch_evaluator_source", "branch_evaluator_binary")
    )
    revalidate_formal_snapshot(snapshot, relevant)
    _run, run_raw, run_info = _capture_formal_run_config(snapshot)
    run_sha256 = sha256_bytes(run_raw)
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    generation_before = _capture_formal_component_generation_image(
        component, snapshot, component_entries=_component_entries
    )
    branch_context = (
        _formal_branch_capture_context(snapshot, run_sha256)
        if component == "BRANCH"
        else None
    )
    entries = tuple(
        (
            _capture_formal_static_manifest_entry(
                result, cell, snapshot.main_freeze_sha256, run_sha256, snapshot
            )
            if component == "STATIC"
            else _capture_formal_branch_manifest_entry(
                result,
                cell,
                snapshot.main_freeze_sha256,
                run_sha256,
                (
                    branch_context[0],
                    branch_context[3][index],
                    branch_context[1],
                    branch_context[2],
                ),
            )
        )
        for index, cell in enumerate(exact_matrix())
    )
    revalidate_formal_snapshot(snapshot, relevant)
    _run_after, run_after, run_after_info = _capture_formal_run_config(snapshot)
    if run_after != run_raw or _stat_identity(run_after_info) != _stat_identity(run_info):
        raise CorruptGeneration("formal run config changed during component capture")
    replay_entries = tuple(
        (
            _capture_formal_static_manifest_entry(
                result, cell, snapshot.main_freeze_sha256, run_sha256, snapshot
            )
            if component == "STATIC"
            else _capture_formal_branch_manifest_entry(
                result,
                cell,
                snapshot.main_freeze_sha256,
                run_sha256,
                (
                    branch_context[0],
                    branch_context[3][index],
                    branch_context[1],
                    branch_context[2],
                ),
            )
        )
        for index, cell in enumerate(exact_matrix())
    )
    if not exact_json_equal(list(replay_entries), list(entries)):
        raise CorruptGeneration("formal cell frontier changed during capture")
    generation_after = _capture_formal_component_generation_image(
        component, snapshot, component_entries=_component_entries
    )
    if generation_after != generation_before:
        raise CorruptGeneration(
            "formal cell frontier identity changed during capture"
        )
    return run_sha256, entries, generation_before


def _formal_component_control_chain(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    run_sha256: str,
    entries: Sequence[Mapping[str, Any]],
) -> dict[str, str]:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    lower = component.lower()
    summary, summary_raw, _ = strict_json_image(
        result / lower / "aggregate_summary.json", require_canonical=True
    )
    manifest, manifest_raw, _ = strict_json_image(
        result / lower / "aggregate_manifest.json", require_canonical=True
    )
    expected_summary, expected_manifest = build_formal_component_aggregate_candidates(
        component, snapshot, run_sha256, entries
    )
    if (
        summary_raw != canonical_json_bytes(expected_summary)
        or manifest_raw != canonical_json_bytes(expected_manifest)
        or not exact_json_equal(summary, expected_summary)
        or not exact_json_equal(manifest, expected_manifest)
    ):
        raise CorruptGeneration(f"formal {lower} aggregate pair mismatch")
    checker, checker_raw, _ = strict_json_image(
        result / f"independent_{lower}_checker.json", require_canonical=True
    )
    postcheck, postcheck_raw, _ = strict_json_image(
        result / f"{component}_POSTCHECK_STATUS.json", require_canonical=True
    )
    exact_keys(checker, FORMAL_COMPONENT_CHECKER_KEYS, f"formal {lower} checker")
    exact_keys(
        postcheck, FORMAL_COMPONENT_POSTCHECK_KEYS, f"formal {lower} postcheck"
    )
    summary_sha = sha256_bytes(summary_raw)
    manifest_sha = sha256_bytes(manifest_raw)
    root_hash = expected_summary["ordered_cell_manifest_root"]
    component_status = (
        "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
        if component == "STATIC"
        else "PASS_BRANCH_TUBE_ALL_SLABS"
    )
    checker_claim = (
        FORMAL_STATIC_CHECKER_CLAIM_BOUNDARY
        if component == "STATIC"
        else FORMAL_BRANCH_CHECKER_CLAIM_BOUNDARY
    )
    postcheck_claim = (
        FORMAL_STATIC_POSTCHECK_CLAIM_BOUNDARY
        if component == "STATIC"
        else FORMAL_BRANCH_POSTCHECK_CLAIM_BOUNDARY
    )
    role_map = {record.role: record for record in snapshot.input_roles}
    checker_source = role_map[f"{lower}_checker_source"]
    producer_source = role_map["scheduler"]
    source_bindings = {
        "checker_source": {
            "path": checker_source.path,
            "sha256": checker_source.sha256,
        },
        "producer_source": {
            "path": producer_source.path,
            "sha256": producer_source.sha256,
        },
    }
    replay_counts = {
        "cell_manifests": 102,
        "hash_bound_payloads": 408 if component == "STATIC" else 306,
    }
    diagnostics = {
        "ordered_cell_manifest_root": root_hash,
        "aggregate_summary_sha256": summary_sha,
        "aggregate_manifest_sha256": manifest_sha,
    }
    if (
        checker["schema_version"] != SCHEMA_VERSION
        or checker["protocol_id"] != PROTOCOL_ID
        or checker["artifact_role"] != f"{component}_INDEPENDENT_CHECKER"
        or checker["authority"] != "INDEPENDENT_CHECKER"
        or checker["checker_status"] != "PASS_INDEPENDENT_CHECKER"
        or checker["component_status"] != component_status
        or checker["scientific_licensing_enabled"] is not False
        or checker["passed"] is not True
        or checker["matrix_id"] != canonical_matrix_id()
        or checker["main_freeze_sha256"] != snapshot.main_freeze_sha256
        or checker["run_config_sha256"] != run_sha256
        or checker["component_aggregate_summary_sha256"] != summary_sha
        or checker["component_aggregate_manifest_sha256"] != manifest_sha
        or not exact_json_equal(checker["replay_counts"], replay_counts)
        or not exact_json_equal(
            checker["cross_precision"],
            {"slab_pairs": 51, "status_pairs_agree": 51, "passed": True},
        )
        or not exact_json_equal(checker["diagnostics"], diagnostics)
        or checker["failures"] != []
        or not exact_json_equal(checker["source_bindings"], source_bindings)
        or checker["claim_boundary"] != checker_claim
        or checker["milestone_status"] is not None
        or checker["theorem_status"] is not None
        or checker["final_status"] is not None
    ):
        raise CorruptGeneration(f"formal {lower} checker mismatch")
    expected_bound = {
        "aggregate_summary": {
            "path": f"{lower}/aggregate_summary.json",
            "sha256": summary_sha,
            "size_bytes": len(summary_raw),
        },
        "aggregate_manifest": {
            "path": f"{lower}/aggregate_manifest.json",
            "sha256": manifest_sha,
            "size_bytes": len(manifest_raw),
        },
        "ordered_cell_manifest_root": root_hash,
    }
    if (
        postcheck["schema_version"] != SCHEMA_VERSION
        or postcheck["protocol_id"] != PROTOCOL_ID
        or postcheck["artifact_role"] != f"{component}_POSTCHECK"
        or postcheck["authority"] != "POSTCHECK_ONLY"
        or postcheck["postcheck_status"] != "PASS_WRITE_ONCE_POSTCHECK"
        or postcheck["passed"] is not True
        or postcheck["checker_path"] != f"independent_{lower}_checker.json"
        or postcheck["checker_sha256"] != sha256_bytes(checker_raw)
        or postcheck["main_freeze_sha256"] != snapshot.main_freeze_sha256
        or postcheck["run_config_sha256"] != run_sha256
        or not exact_json_equal(postcheck["bound_artifacts"], expected_bound)
        or not exact_json_equal(postcheck["replay_counts"], replay_counts)
        or postcheck["failures"] != []
        or postcheck["scientific_licensing_enabled"] is not False
        or postcheck["claim_boundary"] != postcheck_claim
        or postcheck["component_status"] != component_status
        or postcheck["milestone_status"] is not None
        or postcheck["theorem_status"] is not None
        or postcheck["final_status"] is not None
    ):
        raise CorruptGeneration(f"formal {lower} postcheck mismatch")
    return {
        "aggregate_summary_sha256": summary_sha,
        "aggregate_manifest_sha256": manifest_sha,
        "checker_sha256": sha256_bytes(checker_raw),
        "postcheck_sha256": sha256_bytes(postcheck_raw),
        "ordered_cell_manifest_root": root_hash,
    }


def _capture_formal_composite_control_files(
    snapshot: FormalAuthoritySnapshot,
) -> tuple[tuple[str, str, int, int, int, int, int, int, int], ...]:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    relatives = (
        "static/aggregate_summary.json",
        "static/aggregate_manifest.json",
        "independent_static_checker.json",
        "STATIC_POSTCHECK_STATUS.json",
        "branch/aggregate_summary.json",
        "branch/aggregate_manifest.json",
        "independent_branch_checker.json",
        "BRANCH_POSTCHECK_STATUS.json",
    )
    images: list[tuple[str, str, int, int, int, int, int, int, int]] = []
    for relative in relatives:
        raw, info = read_pinned_regular_file(result / relative)
        if stat.S_IMODE(info.st_mode) != 0o644 or info.st_nlink != 1:
            raise PathContractError(
                f"formal composite control mode/link mismatch: {relative}"
            )
        images.append(
            (
                relative,
                sha256_bytes(raw),
                info.st_dev,
                info.st_ino,
                info.st_mode,
                info.st_nlink,
                info.st_size,
                info.st_mtime_ns,
                info.st_ctime_ns,
            )
        )
    return tuple(images)


FORMAL_COMPOSITE_BASELINE_RESULT_NAMES = frozenset(
    {
        "run_config.json",
        "static",
        "branch",
        "independent_static_checker.json",
        "STATIC_POSTCHECK_STATUS.json",
        "independent_branch_checker.json",
        "BRANCH_POSTCHECK_STATUS.json",
    }
)


def _capture_formal_composite_result_parent(
    snapshot: FormalAuthoritySnapshot,
    transient_entries: frozenset[str],
) -> tuple[str, int, int, int, int, tuple[str, ...]]:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    descriptor = _open_directory_fd(result)
    try:
        info = os.fstat(descriptor)
        if (
            not stat.S_ISDIR(info.st_mode)
            or stat.S_IMODE(info.st_mode) != 0o755
            or info.st_nlink < 2
        ):
            raise PathContractError(
                "formal composite result-root mode/link mismatch"
            )
        names = set(os.listdir(descriptor))
        expected = set(FORMAL_COMPOSITE_BASELINE_RESULT_NAMES) | set(
            transient_entries
        )
        if names != expected:
            raise CorruptGeneration(
                "formal composite result-root namespace mismatch"
            )
        return (
            result.name,
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            tuple(sorted(FORMAL_COMPOSITE_BASELINE_RESULT_NAMES)),
        )
    finally:
        os.close(descriptor)


def capture_formal_composite_inputs(
    snapshot: FormalAuthoritySnapshot,
    *,
    _result_entries: frozenset[str] = frozenset(),
) -> tuple[
    str,
    dict[str, dict[str, str]],
    FormalCompositeGenerationImage,
]:
    """Reopen both 102-cell archives and roles 56--63 independently."""

    result_parent_before = _capture_formal_composite_result_parent(
        snapshot, _result_entries
    )
    component_published = frozenset(
        {"aggregate_summary.json", "aggregate_manifest.json"}
    )
    static_run, static_entries, static_generation = capture_formal_component_aggregate_inputs(
        "STATIC", snapshot, _component_entries=component_published
    )
    branch_run, branch_entries, branch_generation = capture_formal_component_aggregate_inputs(
        "BRANCH", snapshot, _component_entries=component_published
    )
    if static_run != branch_run:
        raise CorruptGeneration("formal component run-config hashes differ")
    controls_before = _capture_formal_composite_control_files(snapshot)
    chains = {
        "static": _formal_component_control_chain(
            "STATIC", snapshot, static_run, static_entries
        ),
        "branch": _formal_component_control_chain(
            "BRANCH", snapshot, branch_run, branch_entries
        ),
    }
    revalidate_formal_snapshot(snapshot)
    controls_after = _capture_formal_composite_control_files(snapshot)
    if controls_after != controls_before:
        raise CorruptGeneration("formal roles 56--63 changed during composite capture")
    terminal_static_run, terminal_static_entries, terminal_static_generation = (
        capture_formal_component_aggregate_inputs(
            "STATIC", snapshot, _component_entries=component_published
        )
    )
    terminal_branch_run, terminal_branch_entries, terminal_branch_generation = (
        capture_formal_component_aggregate_inputs(
            "BRANCH", snapshot, _component_entries=component_published
        )
    )
    revalidate_formal_snapshot(snapshot)
    controls_terminal = _capture_formal_composite_control_files(snapshot)
    result_parent_after = _capture_formal_composite_result_parent(
        snapshot, _result_entries
    )
    if (
        terminal_static_run != static_run
        or terminal_branch_run != branch_run
        or not exact_json_equal(list(terminal_static_entries), list(static_entries))
        or not exact_json_equal(list(terminal_branch_entries), list(branch_entries))
        or terminal_static_generation != static_generation
        or terminal_branch_generation != branch_generation
        or result_parent_after != result_parent_before
        or controls_terminal != controls_before
    ):
        raise CorruptGeneration(
            "formal component generations changed during composite capture"
        )
    return (
        static_run,
        chains,
        FormalCompositeGenerationImage(
            static=static_generation,
            branch=branch_generation,
            result_parent=result_parent_before,
            controls=controls_before,
        ),
    )


def _formal_verbose_component_chains(
    component_chains: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    if type(component_chains) is not dict or set(component_chains) != {
        "static", "branch"
    }:
        raise CorruptGeneration("formal composite component chain set mismatch")
    verbose: dict[str, Any] = {}
    for name in ("static", "branch"):
        chain = component_chains[name]
        exact_keys(
            chain,
            {
                "aggregate_summary_sha256", "aggregate_manifest_sha256",
                "checker_sha256", "postcheck_sha256",
                "ordered_cell_manifest_root",
            },
            f"formal composite {name} compact chain",
        )
        for value in chain.values():
            if type(value) is not str or HEX_SHA256.fullmatch(value) is None:
                raise CorruptGeneration(
                    f"formal composite {name} chain digest is malformed"
                )
        verbose[name] = {
            "aggregate_summary": {
                "path": f"{name}/aggregate_summary.json",
                "sha256": chain["aggregate_summary_sha256"],
            },
            "aggregate_manifest": {
                "path": f"{name}/aggregate_manifest.json",
                "sha256": chain["aggregate_manifest_sha256"],
            },
            "checker": {
                "path": f"independent_{name}_checker.json",
                "sha256": chain["checker_sha256"],
            },
            "postcheck": {
                "path": f"{name.upper()}_POSTCHECK_STATUS.json",
                "sha256": chain["postcheck_sha256"],
            },
            "ordered_cell_manifest_root": chain[
                "ordered_cell_manifest_root"
            ],
        }
        exact_keys(
            verbose[name],
            FORMAL_COMPOSITE_COMPONENT_CHAIN_KEYS,
            f"formal composite {name} verbose chain",
        )
        for edge_name in (
            "aggregate_summary", "aggregate_manifest", "checker", "postcheck"
        ):
            exact_keys(
                verbose[name][edge_name],
                FORMAL_COMPOSITE_FILE_EDGE_KEYS,
                f"formal composite {name} {edge_name} edge",
            )
    return verbose


def build_formal_composite_candidates(
    snapshot: FormalAuthoritySnapshot,
    run_config_sha256: str,
    component_chains: Mapping[str, Mapping[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Build exact roles 64/65 from two already-replayed component chains."""

    revalidate_formal_snapshot(snapshot)
    if (
        type(run_config_sha256) is not str
        or HEX_SHA256.fullmatch(run_config_sha256) is None
    ):
        raise CorruptGeneration("formal composite run-config hash is malformed")
    verbose = _formal_verbose_component_chains(component_chains)
    generation = sha256_bytes(canonical_json_bytes(verbose))
    common = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_status": "COMPLETE_PRODUCER_ARCHIVE",
        "authority": "PRODUCER_ONLY",
        "matrix_id": canonical_matrix_id(),
        "main_freeze_sha256": snapshot.main_freeze_sha256,
        "run_config_sha256": run_config_sha256,
        "component_chains": verbose,
        "archive_generation_sha256": generation,
        "scientific_licensing_enabled": False,
        "claim_boundary": FORMAL_COMPOSITE_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    summary = {
        **common,
        "artifact_role": "COMPOSITE_SUMMARY",
        "matrix": matrix_payload(),
        "cell_count_per_component": 102,
    }
    summary_raw = canonical_json_bytes(summary)
    manifest = {
        **common,
        "artifact_role": "COMPOSITE_MANIFEST",
        "summary": {
            "path": "composite_summary.json",
            "sha256": sha256_bytes(summary_raw),
            "size_bytes": len(summary_raw),
        },
    }
    exact_keys(summary, FORMAL_COMPOSITE_SUMMARY_KEYS, "formal composite summary")
    exact_keys(
        manifest, FORMAL_COMPOSITE_MANIFEST_KEYS, "formal composite manifest"
    )
    return summary, manifest


def build_formal_component_aggregate_candidate_package(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    run_config_sha256: str,
    entries: Sequence[Mapping[str, Any]],
    package_value: str,
) -> tuple[dict[str, Any], dict[str, Any], FormalPrivatePairPackage]:
    captured_run, captured_entries, generation = capture_formal_component_aggregate_inputs(
        component, snapshot
    )
    if captured_run != run_config_sha256 or not exact_json_equal(
        list(captured_entries), list(entries)
    ):
        raise CorruptGeneration(
            "formal component candidate inputs differ from canonical frontier"
        )
    summary, manifest = build_formal_component_aggregate_candidates(
        component, snapshot, run_config_sha256, entries
    )
    names = ("aggregate_summary.json", "aggregate_manifest.json")
    image = _write_formal_private_pair_package(
        package_value,
        {
            names[0]: canonical_json_bytes(summary),
            names[1]: canonical_json_bytes(manifest),
        },
        names,
        context=f"formal {component.lower()} aggregate candidate package",
    )
    revalidate_formal_snapshot(snapshot)
    _replay_formal_private_pair_package(
        image,
        names,
        context=f"formal {component.lower()} aggregate candidate terminal replay",
    )
    terminal_run, terminal_entries, terminal_generation = (
        capture_formal_component_aggregate_inputs(component, snapshot)
    )
    if (
        terminal_run != captured_run
        or not exact_json_equal(list(terminal_entries), list(captured_entries))
        or terminal_generation != generation
    ):
        raise CorruptGeneration(
            "formal component generation changed while building candidate"
        )
    _replay_formal_private_pair_package(
        image,
        names,
        context=f"formal {component.lower()} aggregate candidate ultimate replay",
    )
    return summary, manifest, image


def build_formal_composite_candidate_package(
    snapshot: FormalAuthoritySnapshot,
    run_config_sha256: str,
    component_chains: Mapping[str, Mapping[str, Any]],
    package_value: str,
) -> tuple[dict[str, Any], dict[str, Any], FormalPrivatePairPackage]:
    captured_run, captured_chains, generation = capture_formal_composite_inputs(
        snapshot
    )
    if captured_run != run_config_sha256 or not exact_json_equal(
        captured_chains, component_chains
    ):
        raise CorruptGeneration(
            "formal composite candidate inputs differ from canonical roles 55--63"
        )
    summary, manifest = build_formal_composite_candidates(
        snapshot, run_config_sha256, component_chains
    )
    names = ("composite_summary.json", "composite_manifest.json")
    image = _write_formal_private_pair_package(
        package_value,
        {
            names[0]: canonical_json_bytes(summary),
            names[1]: canonical_json_bytes(manifest),
        },
        names,
        context="formal composite candidate package",
    )
    revalidate_formal_snapshot(snapshot)
    _replay_formal_private_pair_package(
        image, names, context="formal composite candidate terminal replay"
    )
    terminal_run, terminal_chains, terminal_generation = (
        capture_formal_composite_inputs(snapshot)
    )
    if (
        terminal_run != captured_run
        or not exact_json_equal(terminal_chains, captured_chains)
        or terminal_generation != generation
    ):
        raise CorruptGeneration(
            "formal composite generation changed while building candidate"
        )
    _replay_formal_private_pair_package(
        image, names, context="formal composite candidate ultimate replay"
    )
    return summary, manifest, image


def capture_formal_component_aggregate_candidate_package(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    package_value: str,
) -> tuple[dict[str, Any], dict[str, Any], FormalPrivatePairPackage]:
    run_sha256, entries, _generation = capture_formal_component_aggregate_inputs(
        component, snapshot
    )
    return build_formal_component_aggregate_candidate_package(
        component,
        snapshot,
        run_sha256,
        entries,
        package_value,
    )


def capture_formal_composite_candidate_package(
    snapshot: FormalAuthoritySnapshot,
    package_value: str,
) -> tuple[dict[str, Any], dict[str, Any], FormalPrivatePairPackage]:
    run_sha256, chains, _generation = capture_formal_composite_inputs(snapshot)
    return build_formal_composite_candidate_package(
        snapshot, run_sha256, chains, package_value
    )


def publish_captured_formal_component_aggregates(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    package_value: str,
    expected_summary_sha256: str,
    expected_manifest_sha256: str,
    *,
    publication_authority: str,
) -> dict[str, Any]:
    run_sha256, entries, _generation = capture_formal_component_aggregate_inputs(
        component, snapshot
    )
    return publish_formal_component_aggregates(
        component,
        snapshot,
        run_sha256,
        entries,
        package_value,
        expected_summary_sha256,
        expected_manifest_sha256,
        publication_authority=publication_authority,
    )


def publish_captured_formal_composite_candidates(
    snapshot: FormalAuthoritySnapshot,
    package_value: str,
    expected_summary_sha256: str,
    expected_manifest_sha256: str,
    *,
    publication_authority: str,
) -> dict[str, Any]:
    run_sha256, chains, _generation = capture_formal_composite_inputs(snapshot)
    return publish_formal_composite_candidates(
        snapshot,
        run_sha256,
        chains,
        package_value,
        expected_summary_sha256,
        expected_manifest_sha256,
        publication_authority=publication_authority,
    )


def _formal_pair_file_receipt(
    path: Path, raw: bytes, info: os.stat_result, root: Path
) -> dict[str, Any]:
    return {
        "path": path.relative_to(root).as_posix(),
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
        "mode": f"{stat.S_IMODE(info.st_mode):04o}",
        "nlink": info.st_nlink,
    }


def _formal_pair_publication_fault_hook(_phase: str) -> None:
    """Test-only hook around producer-pair commit boundaries."""


def _formal_pair_canonical_replay(
    parent_fd: int,
    names: tuple[str, str],
    raws: tuple[bytes, bytes],
    *,
    summary_published: bool,
    manifest_published: bool,
    context: str,
) -> tuple[os.stat_result | None, os.stat_result | None]:
    expected_presence = (summary_published, manifest_published)
    infos: list[os.stat_result | None] = []
    for name, raw, present in zip(names, raws, expected_presence, strict=True):
        try:
            entry = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            if present:
                raise CorruptGeneration(f"{context} missing {name}")
            infos.append(None)
            continue
        if not present:
            raise CorruptGeneration(f"{context} unexpected existing {name}")
        replay_raw, info = _read_machine_publication_file_at(
            parent_fd,
            name,
            f"{context} {name}",
            expected_mode=0o644,
            maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
        )
        if replay_raw != raw or (
            entry.st_dev,
            entry.st_ino,
        ) != (info.st_dev, info.st_ino):
            raise CorruptGeneration(f"{context} changed {name}")
        infos.append(info)
    return infos[0], infos[1]


def _write_formal_pair_stage(
    parent_fd: int,
    name: str,
    raw: bytes,
    *,
    context: str,
) -> tuple[str, tuple[int, int, int, int, int, int, int]]:
    stage_name = f".{name}.role19-publish-{os.urandom(16).hex()}"
    descriptor = os.open(
        stage_name,
        os.O_RDWR | os.O_CREAT | os.O_EXCL
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0),
        0o644,
        dir_fd=parent_fd,
    )
    identity: tuple[int, int] | None = None
    primary_error: BaseException | None = None
    recovery_error: BaseException | None = None
    close_error: BaseException | None = None
    final_identity: tuple[int, int, int, int, int, int, int] | None = None
    try:
        created = os.fstat(descriptor)
        identity = (created.st_dev, created.st_ino)
        os.fchmod(descriptor, 0o644)
        _write_machine_publication_bytes(descriptor, raw)
        os.fsync(descriptor)
        os.lseek(descriptor, 0, os.SEEK_SET)
        staged = bytearray()
        while len(staged) <= len(raw):
            chunk = os.read(descriptor, min(65536, len(raw) + 1 - len(staged)))
            if not chunk:
                break
            staged.extend(chunk)
        final = os.fstat(descriptor)
        entry = os.stat(stage_name, dir_fd=parent_fd, follow_symlinks=False)
        if (
            bytes(staged) != raw
            or not stat.S_ISREG(final.st_mode)
            or stat.S_IMODE(final.st_mode) != 0o644
            or final.st_nlink != 1
            or final.st_size != len(raw)
            or _machine_publication_file_identity(final)
            != _machine_publication_file_identity(entry)
        ):
            raise PathContractError(f"{context} staged file mismatch")
        final_identity = _machine_publication_file_identity(final)
    except BaseException as error:
        primary_error = error
        if identity is None:
            try:
                recovered = os.fstat(descriptor)
                if not stat.S_ISREG(recovered.st_mode) or recovered.st_nlink != 1:
                    raise PathContractError(
                        f"{context} opened stage cannot be recovered safely"
                    )
                identity = (recovered.st_dev, recovered.st_ino)
            except BaseException as error:
                recovery_error = error
    try:
        os.close(descriptor)
    except BaseException as error:
        close_error = error
    if primary_error is not None or recovery_error is not None or close_error is not None:
        cleanup_error: BaseException | None = None
        if identity is not None:
            try:
                _cleanup_machine_publication_stage(parent_fd, stage_name, identity)
            except BaseException as error:
                cleanup_error = error
        terminal_error = (
            primary_error or recovery_error or close_error
        )
        assert terminal_error is not None
        if cleanup_error is not None:
            raise PathContractError(f"{context} stage cleanup failed") from terminal_error
        if recovery_error is not None or close_error is not None:
            details = "; ".join(
                f"{type(error).__name__}: {error}"
                for error in (recovery_error, close_error)
                if error is not None
            )
            raise PathContractError(
                f"{context} stage failed with incomplete descriptor cleanup: "
                f"{details}"
            ) from terminal_error
        raise terminal_error
    if identity is None or final_identity is None:
        raise PathContractError(f"{context} stage identity was not captured")
    return stage_name, final_identity


def _formal_pair_stage_replay(
    parent_fd: int,
    stage: tuple[str, tuple[int, int, int, int, int, int, int]],
    expected_raw: bytes,
    *,
    context: str,
) -> None:
    raw, info = _read_machine_publication_file_at(
        parent_fd,
        stage[0],
        context,
        expected_mode=0o644,
        maximum_bytes=FORMAL_PRODUCER_CANDIDATE_MAX_BYTES,
    )
    if raw != expected_raw or _machine_publication_file_identity(info) != stage[1]:
        raise PathContractError(f"{context} full staged image changed")


def _formal_pair_parent_namespace_replay(
    parent_fd: int,
    baseline_names: frozenset[str],
    transaction_names: frozenset[str],
    *,
    context: str,
) -> None:
    actual = set(os.listdir(parent_fd))
    expected = set(baseline_names) | set(transaction_names)
    if actual != expected:
        raise CorruptGeneration(f"{context} parent namespace mismatch")


def _publish_formal_producer_pair(
    *,
    snapshot: FormalAuthoritySnapshot,
    package_value: str,
    names: tuple[str, str],
    destinations: tuple[Path, Path],
    expected_sha256: tuple[str, str],
    publication_authority: str,
    expected_authority: str,
    artifact_kind: str,
    rebuild: Any,
    baseline_parent_names: frozenset[str],
    generation_sha256: str,
    _fail_at: str | None = None,
) -> dict[str, Any]:
    if publication_authority != expected_authority:
        raise ProductionAuthorityError(f"formal {artifact_kind} authority mismatch")
    expected = tuple(
        _exact_sha(value, f"formal {artifact_kind} expected digest")
        for value in expected_sha256
    )
    if destinations[0].parent != destinations[1].parent:
        raise PathContractError("formal pair destinations are not same-parent")
    package = _snapshot_formal_private_pair_package(
        package_value, names, context=f"formal {artifact_kind} candidate package"
    )
    raws = (package.files[0].raw, package.files[1].raw)
    if tuple(sha256_bytes(raw) for raw in raws) != expected:
        raise ProductionAuthorityError(f"formal {artifact_kind} candidate digest mismatch")

    def replay_inputs(parent_entries: frozenset[str]) -> None:
        revalidate_formal_snapshot(snapshot)
        rebuilt_summary, rebuilt_manifest = rebuild(parent_entries)
        rebuilt = (
            canonical_json_bytes(rebuilt_summary),
            canonical_json_bytes(rebuilt_manifest),
        )
        if rebuilt != raws:
            raise CorruptGeneration(f"formal {artifact_kind} input replay mismatch")
        _replay_formal_private_pair_package(
            package, names, context=f"formal {artifact_kind} candidate replay"
        )

    replay_inputs(frozenset())
    parent = destinations[0].parent
    parent_chain = _machine_publication_directory_chain(parent)
    parent_fd = _open_directory_fd(parent)
    locked = False
    stages: list[
        tuple[str, tuple[int, int, int, int, int, int, int]] | None
    ] = [None, None]
    summary_published = False
    manifest_published = False
    summary_publication_identity: tuple[int, int, int, int, int, int, int] | None = None
    manifest_publication_identity: tuple[int, int, int, int, int, int, int] | None = None
    primary_error: BaseException | None = None
    cleanup_error: BaseException | None = None

    def transaction_entries() -> frozenset[str]:
        values = {stage[0] for stage in stages if stage is not None}
        if summary_published:
            values.add(destinations[0].name)
        if manifest_published:
            values.add(destinations[1].name)
        return frozenset(values)

    def replay_parent_namespace(context: str) -> None:
        _formal_pair_parent_namespace_replay(
            parent_fd,
            baseline_parent_names,
            transaction_entries(),
            context=context,
        )
    try:
        try:
            fcntl.flock(parent_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PathContractError(f"formal {artifact_kind} parent is locked") from error
        locked = True
        _replay_machine_publication_directory(
            parent, parent_fd, parent_chain, f"formal {artifact_kind} parent"
        )
        _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=False,
            manifest_published=False,
            context=f"formal {artifact_kind} initial destinations",
        )
        replay_parent_namespace(f"formal {artifact_kind} initial")
        for index, raw in enumerate(raws):
            stages[index] = _write_formal_pair_stage(
                parent_fd,
                destinations[index].name,
                raw,
                context=f"formal {artifact_kind} stage {index}",
            )
        os.fsync(parent_fd)
        replay_inputs(transaction_entries())
        replay_parent_namespace(f"formal {artifact_kind} staged")
        _formal_pair_publication_fault_hook("BEFORE_SUMMARY_RENAME")
        if _fail_at == "BEFORE_SUMMARY_RENAME":
            raise SyntheticCrash("formal producer crash before summary rename")
        # The hook is adversarial.  Nothing it observed remains trusted: close
        # the entire authority/package/stage/destination envelope again, with
        # the parent-chain replay as the final operation before rename.
        replay_inputs(transaction_entries())
        for index, stage in enumerate(stages):
            assert stage is not None
            _formal_pair_stage_replay(
                parent_fd,
                stage,
                raws[index],
                context=f"formal {artifact_kind} pre-summary stage {index}",
            )
        _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=False,
            manifest_published=False,
            context=f"formal {artifact_kind} pre-summary destinations",
        )
        replay_parent_namespace(f"formal {artifact_kind} immediate pre-summary")
        _replay_machine_publication_directory(
            parent, parent_fd, parent_chain,
            f"formal {artifact_kind} immediate pre-summary parent",
        )
        assert stages[0] is not None
        _rename_machine_publication_noreplace(
            parent_fd, stages[0][0], destinations[0].name
        )
        summary_published = True
        stages[0] = None
        os.fsync(parent_fd)
        summary_info, _ = _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=True,
            manifest_published=False,
            context=f"formal {artifact_kind} immediate post-summary state",
        )
        assert summary_info is not None
        summary_publication_identity = _machine_publication_file_identity(
            summary_info
        )
        _formal_pair_publication_fault_hook("AFTER_SUMMARY_RENAME")
        if _fail_at == "AFTER_SUMMARY_RENAME":
            raise SyntheticCrash("formal producer crash after summary rename")
        replay_inputs(transaction_entries())
        summary_info, _ = _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=True,
            manifest_published=False,
            context=f"formal {artifact_kind} summary-only state",
        )
        if (
            summary_info is None
            or _machine_publication_file_identity(summary_info)
            != summary_publication_identity
        ):
            raise PathContractError(
                f"formal {artifact_kind} post-summary identity changed"
            )
        replay_parent_namespace(f"formal {artifact_kind} summary-only")
        _formal_pair_publication_fault_hook("BEFORE_MANIFEST_RENAME")
        if _fail_at == "BEFORE_MANIFEST_RENAME":
            raise SyntheticCrash("formal producer crash before manifest rename")
        replay_inputs(transaction_entries())
        assert stages[1] is not None
        _formal_pair_stage_replay(
            parent_fd,
            stages[1],
            raws[1],
            context=f"formal {artifact_kind} pre-manifest stage",
        )
        replayed_summary, _ = _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=True,
            manifest_published=False,
            context=f"formal {artifact_kind} posthook summary-only state",
        )
        if (
            replayed_summary is None
            or _machine_publication_file_identity(replayed_summary)
            != summary_publication_identity
        ):
            raise PathContractError(
                f"formal {artifact_kind} published summary identity changed"
            )
        replay_parent_namespace(f"formal {artifact_kind} immediate pre-manifest")
        _replay_machine_publication_directory(
            parent, parent_fd, parent_chain,
            f"formal {artifact_kind} immediate pre-manifest parent",
        )
        _rename_machine_publication_noreplace(
            parent_fd, stages[1][0], destinations[1].name
        )
        manifest_published = True
        stages[1] = None
        os.fsync(parent_fd)
        immediate_summary, immediate_manifest = _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=True,
            manifest_published=True,
            context=f"formal {artifact_kind} immediate post-manifest pair",
        )
        assert immediate_summary is not None and immediate_manifest is not None
        if _machine_publication_file_identity(
            immediate_summary
        ) != summary_publication_identity:
            raise PathContractError(
                f"formal {artifact_kind} summary changed during manifest commit"
            )
        manifest_publication_identity = _machine_publication_file_identity(
            immediate_manifest
        )
        _formal_pair_publication_fault_hook("AFTER_MANIFEST_RENAME")
        if _fail_at == "AFTER_MANIFEST_RENAME":
            raise SyntheticCrash("formal producer crash after manifest rename")
        replay_inputs(transaction_entries())
        summary_info, manifest_info = _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=True,
            manifest_published=True,
            context=f"formal {artifact_kind} terminal pair",
        )
        _replay_machine_publication_directory(
            parent, parent_fd, parent_chain, f"formal {artifact_kind} terminal parent"
        )
        replay_parent_namespace(f"formal {artifact_kind} terminal")
        assert summary_info is not None and manifest_info is not None
        if (
            summary_publication_identity is None
            or _machine_publication_file_identity(summary_info)
            != summary_publication_identity
        ):
            raise PathContractError(
                f"formal {artifact_kind} terminal summary identity changed"
            )
        if (
            manifest_publication_identity is None
            or _machine_publication_file_identity(manifest_info)
            != manifest_publication_identity
        ):
            raise PathContractError(
                f"formal {artifact_kind} terminal manifest identity changed"
            )
        receipt = {
            "publication_status": "PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY",
            "authority": expected_authority,
            "artifact_kind": artifact_kind,
            "candidate_package": os.fspath(package.path),
            "summary": _formal_pair_file_receipt(
                destinations[0], raws[0], summary_info, snapshot.authority_root
            ),
            "manifest": _formal_pair_file_receipt(
                destinations[1], raws[1], manifest_info, snapshot.authority_root
            ),
            "archive_generation_sha256": generation_sha256,
            "publication_method": FORMAL_PRODUCER_PUBLICATION_METHOD,
            "scientific_licensing_enabled": False,
            "production_authorized": False,
            "scientific_dispatch_performed": False,
            "independent_postpublication_verification_performed": False,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        exact_keys(receipt, FORMAL_PRODUCER_PAIR_RECEIPT_KEYS, "formal pair receipt")
        receipt_raw = canonical_json_bytes(receipt)
        if not exact_json_equal(
            strict_json_loads(receipt_raw.decode("utf-8")), receipt
        ):
            raise StrictJSONError("formal pair receipt canonicalization mismatch")
        replay_inputs(transaction_entries())
        ultimate_summary, ultimate_manifest = _formal_pair_canonical_replay(
            parent_fd,
            tuple(path.name for path in destinations),
            raws,
            summary_published=True,
            manifest_published=True,
            context=f"formal {artifact_kind} post-receipt ultimate pair",
        )
        if (
            ultimate_summary is None
            or ultimate_manifest is None
            or _machine_publication_file_identity(ultimate_summary)
            != summary_publication_identity
            or _machine_publication_file_identity(ultimate_manifest)
            != manifest_publication_identity
        ):
            raise PathContractError(
                f"formal {artifact_kind} post-receipt identity changed"
            )
        _replay_machine_publication_directory(
            parent,
            parent_fd,
            parent_chain,
            f"formal {artifact_kind} post-receipt terminal parent",
        )
        replay_parent_namespace(f"formal {artifact_kind} post-receipt terminal")
        return receipt
    except BaseException as error:
        primary_error = error
        raise
    finally:
        for stage in stages:
            if stage is None:
                continue
            try:
                _cleanup_machine_publication_stage(
                    parent_fd, stage[0], stage[1][:2]
                )
            except BaseException as error:
                cleanup_error = cleanup_error or error
        for cleanup in (
            (lambda: fcntl.flock(parent_fd, fcntl.LOCK_UN)) if locked else None,
            lambda: os.close(parent_fd),
        ):
            if cleanup is None:
                continue
            try:
                cleanup()
            except BaseException as error:
                cleanup_error = cleanup_error or error
        if cleanup_error is not None:
            if primary_error is not None:
                raise PathContractError(
                    f"formal {artifact_kind} transaction failed with incomplete "
                    f"cleanup: {type(cleanup_error).__name__}: {cleanup_error}"
                ) from primary_error
            raise cleanup_error


def publish_formal_component_aggregates(
    component: str,
    snapshot: FormalAuthoritySnapshot,
    run_config_sha256: str,
    entries: Sequence[Mapping[str, Any]],
    package_value: str,
    expected_summary_sha256: str,
    expected_manifest_sha256: str,
    *,
    publication_authority: str,
    _fail_at: str | None = None,
) -> dict[str, Any]:
    if component not in COMPONENTS:
        raise SchedulerContractError("formal aggregate component is invalid")
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    lower = component.lower()
    initial_run, initial_entries, initial_generation = (
        capture_formal_component_aggregate_inputs(component, snapshot)
    )
    if initial_run != run_config_sha256 or not exact_json_equal(
        list(initial_entries), list(entries)
    ):
        raise CorruptGeneration(
            "formal aggregate publication caller frontier mismatch"
        )

    def rebuild(
        parent_entries: frozenset[str],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        captured_run, captured_entries, captured_generation = (
            capture_formal_component_aggregate_inputs(
                component, snapshot, _component_entries=parent_entries
            )
        )
        if (
            captured_run != initial_run
            or not exact_json_equal(list(captured_entries), list(initial_entries))
            or captured_generation != initial_generation
        ):
            raise CorruptGeneration(
                "formal aggregate publication canonical frontier changed"
            )
        return build_formal_component_aggregate_candidates(
            component, snapshot, captured_run, captured_entries
        )

    summary, _ = rebuild(frozenset())
    return _publish_formal_producer_pair(
        snapshot=snapshot,
        package_value=package_value,
        names=("aggregate_summary.json", "aggregate_manifest.json"),
        destinations=(
            result / lower / "aggregate_summary.json",
            result / lower / "aggregate_manifest.json",
        ),
        expected_sha256=(expected_summary_sha256, expected_manifest_sha256),
        publication_authority=publication_authority,
        expected_authority=FORMAL_COMPONENT_AGGREGATES_PUBLICATION_AUTHORITY,
        artifact_kind=f"{lower}_component_aggregate_pair",
        rebuild=rebuild,
        baseline_parent_names=frozenset({"cells", "cell_manifests"}),
        generation_sha256=summary["ordered_cell_manifest_root"],
        _fail_at=_fail_at,
    )


def publish_formal_composite_candidates(
    snapshot: FormalAuthoritySnapshot,
    run_config_sha256: str,
    component_chains: Mapping[str, Mapping[str, Any]],
    package_value: str,
    expected_summary_sha256: str,
    expected_manifest_sha256: str,
    *,
    publication_authority: str,
    _fail_at: str | None = None,
) -> dict[str, Any]:
    result = snapshot.authority_root / "results/r401_val_l3_a1_v2_all_slabs"
    initial_run, initial_chains, initial_generation = (
        capture_formal_composite_inputs(snapshot)
    )
    if initial_run != run_config_sha256 or not exact_json_equal(
        initial_chains, component_chains
    ):
        raise CorruptGeneration(
            "formal composite publication caller roles 55--63 mismatch"
        )

    def rebuild(
        parent_entries: frozenset[str],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        captured_run, captured_chains, captured_generation = (
            capture_formal_composite_inputs(
                snapshot, _result_entries=parent_entries
            )
        )
        if (
            captured_run != initial_run
            or not exact_json_equal(captured_chains, initial_chains)
            or captured_generation != initial_generation
        ):
            raise CorruptGeneration(
                "formal composite publication roles 55--63 changed"
            )
        return build_formal_composite_candidates(
            snapshot, captured_run, captured_chains
        )

    summary, _ = rebuild(frozenset())
    return _publish_formal_producer_pair(
        snapshot=snapshot,
        package_value=package_value,
        names=("composite_summary.json", "composite_manifest.json"),
        destinations=(
            result / "composite_summary.json",
            result / "composite_manifest.json",
        ),
        expected_sha256=(expected_summary_sha256, expected_manifest_sha256),
        publication_authority=publication_authority,
        expected_authority=FORMAL_COMPOSITE_PUBLICATION_AUTHORITY,
        artifact_kind="composite_producer_pair",
        rebuild=rebuild,
        baseline_parent_names=FORMAL_COMPOSITE_BASELINE_RESULT_NAMES,
        generation_sha256=summary["archive_generation_sha256"],
        _fail_at=_fail_at,
    )


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
    parser.add_argument("--authority-root")
    parser.add_argument("--initialize-only", action="store_true")
    parser.add_argument("--capture-machine-freeze", action="store_true")
    parser.add_argument("--publish-machine-freeze", action="store_true")
    parser.add_argument("--capture-prefreeze-tests", action="store_true")
    parser.add_argument("--publish-prefreeze-tests", action="store_true")
    parser.add_argument("--publish-role5", action="store_true")
    parser.add_argument("--build-main-freeze-candidate", action="store_true")
    parser.add_argument("--second-fresh-rebuild-only", action="store_true")
    parser.add_argument("--build-formal-run-config-candidate", action="store_true")
    parser.add_argument("--publish-formal-run-config", action="store_true")
    parser.add_argument(
        "--build-formal-component-aggregate-candidates", action="store_true"
    )
    parser.add_argument("--publish-formal-component-aggregates", action="store_true")
    parser.add_argument("--build-formal-composite-candidates", action="store_true")
    parser.add_argument("--publish-formal-composite-candidates", action="store_true")
    parser.add_argument("--candidate")
    parser.add_argument("--role24-receipt")
    parser.add_argument("--expected-sha256")
    parser.add_argument("--expected-reviewed-commit")
    parser.add_argument("--expected-summary-sha256")
    parser.add_argument("--expected-manifest-sha256")
    parser.add_argument("--publication-authority")
    parser.add_argument("--component")
    parser.add_argument("--static-calibration")
    parser.add_argument("--branch-calibration")
    parser.add_argument("--capd-checkout")
    parser.add_argument("--compiler")
    parser.add_argument("--mock-only", action="store_true")
    parser.add_argument("--mock-static-cells", type=int, default=None)
    parser.add_argument("--mock-branch-cells", type=int, default=None)
    parser.add_argument(
        "--mock-branch-evaluator",
        type=Path,
    )
    parser.add_argument("--finalize-mock-composite", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--production", action="store_true")
    parser.add_argument("--execute-scientific-dispatch", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(argv)
    mock_static_option_present = arguments.mock_static_cells is not None
    mock_branch_option_present = arguments.mock_branch_cells is not None
    try:
        if arguments.publish_role5:
            other_modes = (
                arguments.initialize_only,
                arguments.capture_machine_freeze,
                arguments.publish_machine_freeze,
                arguments.capture_prefreeze_tests,
                arguments.publish_prefreeze_tests,
                arguments.build_main_freeze_candidate,
                arguments.second_fresh_rebuild_only,
                arguments.build_formal_run_config_candidate,
                arguments.publish_formal_run_config,
                arguments.build_formal_component_aggregate_candidates,
                arguments.publish_formal_component_aggregates,
                arguments.build_formal_composite_candidates,
                arguments.publish_formal_composite_candidates,
                arguments.mock_only,
                mock_static_option_present,
                mock_branch_option_present,
                arguments.finalize_mock_composite,
                arguments.resume,
                arguments.production,
                arguments.execute_scientific_dispatch,
            )
            unrelated_values = (
                arguments.output,
                arguments.expected_summary_sha256,
                arguments.expected_manifest_sha256,
                arguments.component,
                arguments.static_calibration,
                arguments.branch_calibration,
                arguments.capd_checkout,
                arguments.compiler,
                arguments.mock_branch_evaluator,
            )
            if any(other_modes) or any(
                value is not None for value in unrelated_values
            ):
                raise SchedulerContractError(
                    "role-5 publication is exact-exclusive from every other mode"
                )
            if any(
                value is None
                for value in (
                    arguments.candidate,
                    arguments.role24_receipt,
                    arguments.expected_sha256,
                    arguments.expected_reviewed_commit,
                    arguments.publication_authority,
                    arguments.authority_root,
                )
            ):
                raise SchedulerContractError(
                    "role-5 publication requires exactly --candidate, "
                    "--role24-receipt, --expected-sha256, "
                    "--expected-reviewed-commit, --publication-authority, "
                    "and --authority-root"
                )
            receipt = publish_v2_role5(
                arguments.candidate,
                arguments.role24_receipt,
                arguments.expected_sha256,
                arguments.expected_reviewed_commit,
                arguments.publication_authority,
                arguments.authority_root,
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0

        if (
            arguments.role24_receipt is not None
            or arguments.expected_reviewed_commit is not None
        ):
            raise SchedulerContractError(
                "role-5 auxiliary options require --publish-role5"
            )

        formal_source_modes = (
            arguments.build_formal_run_config_candidate,
            arguments.publish_formal_run_config,
            arguments.build_formal_component_aggregate_candidates,
            arguments.publish_formal_component_aggregates,
            arguments.build_formal_composite_candidates,
            arguments.publish_formal_composite_candidates,
        )
        if sum(bool(value) for value in formal_source_modes) > 1:
            raise SchedulerContractError(
                "formal producer candidate/publication modes are an exact XOR"
            )
        if any(formal_source_modes):
            old_primary = (
                arguments.second_fresh_rebuild_only,
                arguments.build_main_freeze_candidate,
                arguments.capture_machine_freeze,
                arguments.publish_machine_freeze,
                arguments.capture_prefreeze_tests,
                arguments.publish_prefreeze_tests,
                arguments.initialize_only,
                arguments.mock_only,
                mock_static_option_present,
                mock_branch_option_present,
                arguments.finalize_mock_composite,
                arguments.resume,
                arguments.production,
                arguments.execute_scientific_dispatch,
            )
            if any(old_primary) or any(
                value is not None
                for value in (
                    arguments.static_calibration,
                    arguments.branch_calibration,
                    arguments.capd_checkout,
                    arguments.compiler,
                    arguments.mock_branch_evaluator,
                )
            ):
                raise SchedulerContractError(
                    "formal producer mode is exact-exclusive from all legacy, "
                    "mock, prefreeze, and scientific modes"
                )
            if arguments.authority_root is None:
                raise SchedulerContractError(
                    "formal producer mode requires raw --authority-root"
                )
            if arguments.build_formal_run_config_candidate:
                if (
                    arguments.output is None
                    or arguments.candidate is not None
                    or arguments.expected_sha256 is not None
                    or arguments.expected_summary_sha256 is not None
                    or arguments.expected_manifest_sha256 is not None
                    or arguments.publication_authority is not None
                    or arguments.component is not None
                ):
                    raise SchedulerContractError(
                        "role-55 build requires only --output and --authority-root"
                    )
                snapshot = load_formal_authority(arguments.authority_root)
                payload, digest = build_formal_run_config_candidate(
                    snapshot, arguments.output
                )
                receipt = {
                    "artifact_role": "TEMP_RUN_CONFIG_CANDIDATE",
                    "artifact_status": "BUILT_VALIDATED_TEMP_ONLY",
                    "authority": "ROLE19_RUN_CONFIG_CANDIDATE_ONLY",
                    "candidate_sha256": digest,
                    "run_artifact_role": payload["artifact_role"],
                    "output_path": arguments.output,
                    "scientific_licensing_enabled": False,
                    "production_authorized": False,
                    "scientific_dispatch_performed": False,
                    "component_status": None,
                    "milestone_status": None,
                    "theorem_status": None,
                    "final_status": None,
                }
                print(canonical_json_bytes(receipt).decode("utf-8"), end="")
                return 0

            if arguments.publish_formal_run_config:
                if (
                    arguments.output is not None
                    or arguments.candidate is None
                    or arguments.expected_sha256 is None
                    or arguments.expected_summary_sha256 is not None
                    or arguments.expected_manifest_sha256 is not None
                    or arguments.component is not None
                    or arguments.publication_authority is None
                ):
                    raise SchedulerContractError(
                        "role-55 publish requires --candidate, --expected-sha256, "
                        "--publication-authority, and --authority-root only"
                    )
                snapshot = load_formal_authority(arguments.authority_root)
                receipt = publish_formal_run_config(
                    snapshot,
                    arguments.candidate,
                    arguments.expected_sha256,
                    publication_authority=arguments.publication_authority,
                )
                print(canonical_json_bytes(receipt).decode("utf-8"), end="")
                return 0

            component_mode = (
                arguments.build_formal_component_aggregate_candidates
                or arguments.publish_formal_component_aggregates
            )
            if component_mode and arguments.component not in COMPONENTS:
                raise SchedulerContractError(
                    "formal component mode requires exact --component STATIC|BRANCH"
                )
            if not component_mode and arguments.component is not None:
                raise SchedulerContractError(
                    "--component is forbidden outside formal component mode"
                )

            if arguments.build_formal_component_aggregate_candidates:
                if (
                    arguments.output is None
                    or arguments.candidate is not None
                    or arguments.expected_sha256 is not None
                    or arguments.expected_summary_sha256 is not None
                    or arguments.expected_manifest_sha256 is not None
                    or arguments.publication_authority is not None
                ):
                    raise SchedulerContractError(
                        "component build requires only --output, --component, "
                        "and --authority-root"
                    )
                snapshot = load_formal_authority(arguments.authority_root)
                summary, manifest, package = (
                    capture_formal_component_aggregate_candidate_package(
                        arguments.component, snapshot, arguments.output
                    )
                )
                receipt = {
                    "artifact_role": "TEMP_COMPONENT_AGGREGATE_PAIR",
                    "artifact_status": "BUILT_VALIDATED_TEMP_ONLY",
                    "authority": "ROLE19_COMPONENT_CANDIDATE_ONLY",
                    "component": arguments.component,
                    "candidate_package": os.fspath(package.path),
                    "summary_sha256": sha256_bytes(canonical_json_bytes(summary)),
                    "manifest_sha256": sha256_bytes(canonical_json_bytes(manifest)),
                    "scientific_licensing_enabled": False,
                    "production_authorized": False,
                    "scientific_dispatch_performed": False,
                    "component_status": None,
                    "milestone_status": None,
                    "theorem_status": None,
                    "final_status": None,
                }
                print(canonical_json_bytes(receipt).decode("utf-8"), end="")
                return 0

            if arguments.publish_formal_component_aggregates:
                if (
                    arguments.output is not None
                    or arguments.candidate is None
                    or arguments.expected_sha256 is not None
                    or arguments.expected_summary_sha256 is None
                    or arguments.expected_manifest_sha256 is None
                    or arguments.publication_authority is None
                ):
                    raise SchedulerContractError(
                        "component publish requires --candidate, two expected "
                        "digests, --component, --publication-authority, and "
                        "--authority-root only"
                    )
                snapshot = load_formal_authority(arguments.authority_root)
                receipt = publish_captured_formal_component_aggregates(
                    arguments.component,
                    snapshot,
                    arguments.candidate,
                    arguments.expected_summary_sha256,
                    arguments.expected_manifest_sha256,
                    publication_authority=arguments.publication_authority,
                )
                print(canonical_json_bytes(receipt).decode("utf-8"), end="")
                return 0

            if arguments.build_formal_composite_candidates:
                if (
                    arguments.output is None
                    or arguments.candidate is not None
                    or arguments.expected_sha256 is not None
                    or arguments.expected_summary_sha256 is not None
                    or arguments.expected_manifest_sha256 is not None
                    or arguments.publication_authority is not None
                ):
                    raise SchedulerContractError(
                        "composite build requires only --output and --authority-root"
                    )
                snapshot = load_formal_authority(arguments.authority_root)
                summary, manifest, package = (
                    capture_formal_composite_candidate_package(
                        snapshot, arguments.output
                    )
                )
                receipt = {
                    "artifact_role": "TEMP_COMPOSITE_PRODUCER_PAIR",
                    "artifact_status": "BUILT_VALIDATED_TEMP_ONLY",
                    "authority": "ROLE19_COMPOSITE_CANDIDATE_ONLY",
                    "candidate_package": os.fspath(package.path),
                    "summary_sha256": sha256_bytes(canonical_json_bytes(summary)),
                    "manifest_sha256": sha256_bytes(canonical_json_bytes(manifest)),
                    "archive_generation_sha256": summary[
                        "archive_generation_sha256"
                    ],
                    "scientific_licensing_enabled": False,
                    "production_authorized": False,
                    "scientific_dispatch_performed": False,
                    "component_status": None,
                    "milestone_status": None,
                    "theorem_status": None,
                    "final_status": None,
                }
                print(canonical_json_bytes(receipt).decode("utf-8"), end="")
                return 0

            if arguments.publish_formal_composite_candidates:
                if (
                    arguments.output is not None
                    or arguments.candidate is None
                    or arguments.expected_sha256 is not None
                    or arguments.expected_summary_sha256 is None
                    or arguments.expected_manifest_sha256 is None
                    or arguments.publication_authority is None
                ):
                    raise SchedulerContractError(
                        "composite publish requires --candidate, two expected "
                        "digests, --publication-authority, and --authority-root only"
                    )
                snapshot = load_formal_authority(arguments.authority_root)
                receipt = publish_captured_formal_composite_candidates(
                    snapshot,
                    arguments.candidate,
                    arguments.expected_summary_sha256,
                    arguments.expected_manifest_sha256,
                    publication_authority=arguments.publication_authority,
                )
                print(canonical_json_bytes(receipt).decode("utf-8"), end="")
                return 0
            raise SchedulerContractError("unreachable formal producer mode")

        if any(
            value is not None
            for value in (
                arguments.expected_summary_sha256,
                arguments.expected_manifest_sha256,
                arguments.publication_authority,
                arguments.component,
            )
        ):
            raise SchedulerContractError(
                "formal producer auxiliary options require one formal producer mode"
            )

        if arguments.second_fresh_rebuild_only:
            if (
                arguments.build_main_freeze_candidate
                or arguments.capture_machine_freeze
                or arguments.publish_machine_freeze
                or arguments.capture_prefreeze_tests
                or arguments.publish_prefreeze_tests
                or arguments.initialize_only
                or arguments.candidate is not None
                or arguments.expected_sha256 is not None
                or arguments.authority_root is not None
                or arguments.static_calibration is not None
                or arguments.branch_calibration is not None
                or arguments.capd_checkout is not None
                or arguments.compiler is not None
                or arguments.mock_only
                or mock_static_option_present
                or mock_branch_option_present
                or arguments.mock_branch_evaluator is not None
                or arguments.finalize_mock_composite
                or arguments.resume
                or arguments.production
                or arguments.execute_scientific_dispatch
            ):
                raise SchedulerContractError(
                    "second rebuild mode is exact-exclusive from every other mode"
                )
            if arguments.output is None:
                raise SchedulerContractError(
                    "second rebuild mode requires raw --output"
                )
            receipt = run_v2_role11_second_fresh_rebuild(arguments.output)
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0

        if arguments.build_main_freeze_candidate:
            if (
                arguments.capture_machine_freeze
                or arguments.publish_machine_freeze
                or arguments.capture_prefreeze_tests
                or arguments.publish_prefreeze_tests
                or arguments.second_fresh_rebuild_only
                or arguments.initialize_only
                or arguments.candidate is not None
                or arguments.expected_sha256 is not None
                or arguments.static_calibration is not None
                or arguments.branch_calibration is not None
                or arguments.capd_checkout is not None
                or arguments.compiler is not None
                or arguments.mock_only
                or mock_static_option_present
                or mock_branch_option_present
                or arguments.mock_branch_evaluator is not None
                or arguments.finalize_mock_composite
                or arguments.resume
                or arguments.production
                or arguments.execute_scientific_dispatch
            ):
                raise SchedulerContractError(
                    "main candidate mode is exact-exclusive from machine, "
                    "initialize, mock, resume, and scientific modes"
                )
            if arguments.output is None or arguments.authority_root is None:
                raise SchedulerContractError(
                    "main candidate mode requires raw --output and --authority-root"
                )
            payload, digest = capture_v2_main_freeze_candidate(
                arguments.output, arguments.authority_root
            )
            print(canonical_json_bytes({
                "artifact_role": "TEMP_MAIN_FREEZE_CANDIDATE",
                "artifact_status": "BUILT_VALIDATED_TEMP_ONLY",
                "authority": "ROLE19_MAIN_CANDIDATE_CONSTRUCTION_ONLY",
                "candidate_sha256": digest,
                "main_artifact_role": payload["artifact_role"],
                "output_path": arguments.output,
                "scientific_licensing_enabled": False,
                "production_authorized": False,
                "scientific_dispatch_performed": False,
                "component_status": None,
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
            }).decode("utf-8"), end="")
            return 0

        if arguments.capture_prefreeze_tests:
            if (
                arguments.publish_prefreeze_tests
                or arguments.capture_machine_freeze
                or arguments.publish_machine_freeze
                or arguments.initialize_only
                or arguments.candidate is not None
                or arguments.expected_sha256 is not None
                or arguments.static_calibration is not None
                or arguments.branch_calibration is not None
                or arguments.capd_checkout is not None
                or arguments.compiler is not None
                or arguments.mock_only
                or mock_static_option_present
                or mock_branch_option_present
                or arguments.mock_branch_evaluator is not None
                or arguments.finalize_mock_composite
                or arguments.resume
                or arguments.production
                or arguments.execute_scientific_dispatch
            ):
                raise SchedulerContractError(
                    "role-11 capture is exact-exclusive from every other mode"
                )
            if arguments.output is None or arguments.authority_root is None:
                raise SchedulerContractError(
                    "role-11 capture requires raw --output and --authority-root"
                )
            payload, digest = capture_v2_prefreeze_test_candidate(
                arguments.output, arguments.authority_root
            )
            print(canonical_json_bytes({
                "artifact_role": "TEMP_PREFREEZE_TESTS_CANDIDATE",
                "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
                "authority": "ROLE19_PREFREEZE_TESTS_CAPTURE_ONLY",
                "candidate_sha256": digest,
                "prefreeze_artifact_role": payload["artifact_role"],
                "output_path": arguments.output,
                "scientific_licensing_enabled": False,
                "production_authorized": False,
                "scientific_dispatch_performed": False,
                "component_status": None,
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
            }).decode("utf-8"), end="")
            return 0

        if arguments.publish_prefreeze_tests:
            if (
                arguments.capture_machine_freeze
                or arguments.publish_machine_freeze
                or arguments.initialize_only
                or arguments.output is not None
                or arguments.static_calibration is not None
                or arguments.branch_calibration is not None
                or arguments.capd_checkout is not None
                or arguments.compiler is not None
                or arguments.mock_only
                or mock_static_option_present
                or mock_branch_option_present
                or arguments.mock_branch_evaluator is not None
                or arguments.finalize_mock_composite
                or arguments.resume
                or arguments.production
                or arguments.execute_scientific_dispatch
            ):
                raise SchedulerContractError(
                    "role-11 publication is exact-exclusive from every other mode"
                )
            if (
                arguments.candidate is None
                or arguments.expected_sha256 is None
                or arguments.authority_root is None
            ):
                raise SchedulerContractError(
                    "role-11 publication requires --candidate, "
                    "--expected-sha256, and --authority-root"
                )
            receipt = publish_v2_prefreeze_test_record(
                candidate_value=arguments.candidate,
                expected_sha256=arguments.expected_sha256,
                authority_root_value=arguments.authority_root,
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0

        if not (
            arguments.publish_machine_freeze
            or arguments.publish_prefreeze_tests
        ) and (
            arguments.candidate is not None
            or arguments.expected_sha256 is not None
        ):
            raise SchedulerContractError(
                "machine publication arguments require --publish-machine-freeze"
            )

        if arguments.publish_machine_freeze:
            if (
                arguments.capture_machine_freeze
                or arguments.capture_prefreeze_tests
                or arguments.publish_prefreeze_tests
                or arguments.initialize_only
                or arguments.output is not None
                or arguments.static_calibration is not None
                or arguments.branch_calibration is not None
                or arguments.capd_checkout is not None
                or arguments.compiler is not None
                or arguments.mock_only
                or mock_static_option_present
                or mock_branch_option_present
                or arguments.mock_branch_evaluator is not None
                or arguments.finalize_mock_composite
                or arguments.resume
                or arguments.production
                or arguments.execute_scientific_dispatch
            ):
                raise SchedulerContractError(
                    "machine publication is exact-exclusive from capture, "
                    "initialize, mock, output, resume, and scientific execution modes"
                )
            if (
                arguments.candidate is None
                or arguments.expected_sha256 is None
                or arguments.authority_root is None
            ):
                raise SchedulerContractError(
                    "machine publication requires --candidate, "
                    "--expected-sha256, and --authority-root"
                )
            receipt = publish_formal_machine_freeze(
                candidate_value=arguments.candidate,
                expected_sha256=arguments.expected_sha256,
                authority_root_value=arguments.authority_root,
            )
            print(canonical_json_bytes(receipt).decode("utf-8"), end="")
            return 0

        if arguments.capture_machine_freeze:
            if (
                arguments.initialize_only
                or arguments.capture_prefreeze_tests
                or arguments.publish_prefreeze_tests
                or arguments.mock_only
                or mock_static_option_present
                or mock_branch_option_present
                or arguments.finalize_mock_composite
                or arguments.resume
                or arguments.production
                or arguments.execute_scientific_dispatch
            ):
                raise SchedulerContractError(
                    "machine capture is exact-exclusive from initialize, mock, "
                    "resume, and scientific execution modes"
                )
            if (
                arguments.output is None
                or arguments.static_calibration is None
                or arguments.branch_calibration is None
            ):
                raise SchedulerContractError(
                    "machine capture requires --output, --static-calibration, "
                    "and --branch-calibration"
                )
            candidate, candidate_sha256 = (
                capture_and_publish_formal_machine_freeze(
                    output_value=arguments.output,
                    project_root_value=arguments.authority_root or str(ROOT),
                    static_calibration_value=arguments.static_calibration,
                    branch_calibration_value=arguments.branch_calibration,
                    capd_checkout_value=(
                        arguments.capd_checkout or str(DEFAULT_CAPD_CHECKOUT)
                    ),
                    compiler_value=arguments.compiler or str(DEFAULT_COMPILER),
                )
            )
            print(
                json.dumps(
                    {
                        "artifact_role": "TEMP_MACHINE_FREEZE_CANDIDATE",
                        "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
                        "authority": candidate["authority"],
                        "candidate_sha256": candidate_sha256,
                        "machine_artifact_role": candidate["artifact_role"],
                        "machine_status": candidate["status"],
                        "output_path": arguments.output,
                        "serializer": "CJ_COMPACT_V1",
                        "production_authorized": False,
                        "scientific_dispatch_performed": False,
                        "component_status": None,
                        "milestone_status": None,
                        "theorem_status": None,
                        "final_status": None,
                    },
                    sort_keys=True,
                )
            )
            return 0

        if arguments.mock_static_cells is None:
            arguments.mock_static_cells = 0
        if arguments.mock_branch_cells is None:
            arguments.mock_branch_cells = 0

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
                    (
                        arguments.mock_branch_evaluator
                        or MOCK_BRANCH_EVALUATOR
                    ).absolute(),
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
                mock_static_option_present
                or mock_branch_option_present
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
                snapshot = load_formal_authority(arguments.authority_root or ROOT)
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
