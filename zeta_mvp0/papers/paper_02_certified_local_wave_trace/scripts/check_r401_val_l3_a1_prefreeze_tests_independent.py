#!/usr/bin/env python3
"""Zero-write independent checker for the L3-A1 role-11 evidence record.

This module intentionally duplicates the role-11 contract.  It never imports
the producer, launches a subprocess, writes a sidecar, or dispatches a
scientific evaluator.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import struct
import sys
from typing import Any
import zlib


ROOT = Path(__file__).absolute().parents[1]
CHECKER = Path(__file__).absolute()
REPOSITORY_ROOT = ROOT.parents[2]
GIT_DIR = REPOSITORY_ROOT / ".git"
PROTOCOL_ID = "R401-VAL-L3-A1-PREFREEZE-TESTS"
MAX_CANDIDATE_BYTES = 4 * 1024 * 1024
MAX_STDOUT_BYTES = MAX_STDERR_BYTES = 1024 * 1024
MAX_ROLE_BYTES = 128 * 1024 * 1024
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
UTC = re.compile(r"[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z\Z")

MACHINE_SHA256 = "0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e"
MACHINE_SIZE_BYTES = 54526
ROLE13_SHA256 = "d2844c9fd98f76bd41dda937e8f19f978aa48468c17c5a24ebd25baf125f5e30"
ROLE13_SIZE_BYTES = 8820

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
ROLE_ENTRY_KEYS = frozenset({"role", "path", "sha256", "size_bytes", "mode", "nlink"})
FILE_BINDING_KEYS = frozenset({"path", "sha256", "size_bytes", "mode", "nlink"})
EVIDENCE_TOOL_BINDING_KEYS = frozenset({"producer", "independent_checker", "focused_test"})
COMMAND_RESULT_KEYS = frozenset({
    "name", "kind", "argv", "cwd", "environment", "return_code",
    "started_at_utc", "wall_duration_ms", "stdout_utf8", "stdout_sha256",
    "stdout_size_bytes", "stderr_utf8", "stderr_sha256",
    "stderr_size_bytes", "pytest_counts", "semantic_receipt",
})
PYTEST_COUNT_KEYS = frozenset({"passed", "failed", "skipped", "xfailed", "xpassed"})
TEST_TOTAL_KEYS = frozenset((*PYTEST_COUNT_KEYS, "wall_duration_ms"))
TEST_TOTALS_KEYS = frozenset({"prefreeze_focused", "l3_a1_modules", "paper02_full"})
MACHINE_BINDING_KEYS = frozenset({
    "role", "path", "sha256", "size_bytes", "mode", "nlink",
    "publication_commit_oid", "producer_path", "producer_sha256",
    "verifier_path", "verifier_sha256", "verify_receipt", "promotion_authorized",
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
    "staging_output_size_bytes", "staging_output_mode", "byte_for_byte_equal",
    "scientific_evaluator_dispatched", "staging_output_removed",
})

MACHINE_PUBLICATION_COMMIT = "5086e33c7c66f33785338e90b340347e086d9941"
ROLE13_PUBLICATION_COMMIT = "be2a732625d9cab97879539873a756e1eabd366d"
MACHINE_VERIFY_STATUS = "PASS_MACHINE_FREEZE_VERIFY_ONLY"
ROLE13_VERIFY_STATUS = "PASS_S0_COMPATIBILITY_VERIFY_ONLY"
VERIFY_AUTHORITY = "NON_AUTHORITATIVE_VERIFY_ONLY"
SECOND_REBUILD_STATUS = "PASS_SECOND_FRESH_REBUILD"
SECOND_REBUILD_AUTHORITY = "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY"
PREFREEZE_VERIFY_STATUS = "PASS_PREFREEZE_TEST_RECORD_VERIFY_ONLY"
EXPECTED_TEST_PASSED: dict[str, int] | None = {
    "prefreeze_focused": 100,
    "l3_a1_modules": 621,
    "paper02_full": 1016,
}
ORIGIN_URL = "git@github.com:maris205/hilbert-polya-structure.git"
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

COMMAND_SPECS = (
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
    "PATH": "/root/miniconda3/bin:/usr/bin:/bin", "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8", "TZ": "UTC", "PYTHONHASHSEED": "0",
    "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1",
    "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
    "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1",
}
MACHINE_RELATIVE = "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
ROLE13_RELATIVE = "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
PRODUCER_RELATIVE = "scripts/build_r401_val_l3_a1_prefreeze_tests.py"
CHECKER_RELATIVE = "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py"
TEST_RELATIVE = "tests/test_r401_val_l3_a1_prefreeze_tests.py"
FIXED_COMMAND_ARGV = {
    "role24_machine_verify": (
        PYTHON, os.fspath(ROOT / "scripts/build_r401_val_l3_a1_release_provenance.py"),
        "--verify-machine-freeze", os.fspath(ROOT / MACHINE_RELATIVE),
    ),
    "role13_compatibility_verify": (
        PYTHON, os.fspath(CHECKER), "--verify-s0-compatibility",
        os.fspath(ROOT / ROLE13_RELATIVE),
    ),
    "prefreeze_focused_pytest": (
        PYTHON, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no",
        TEST_RELATIVE,
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
        TEST_RELATIVE,
    ),
    "paper02_full_pytest": (
        PYTHON, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no",
    ),
    "git_diff_check": ("/usr/bin/git", "diff", "--check", "HEAD", "--"),
}
REBUILD_COMMAND_ARGV_PREFIX = (
    PYTHON, os.fspath(ROOT / PRODUCER_RELATIVE), "--second-fresh-rebuild-only", "--output",
)
REBUILD_OUTPUT_BASENAME = "capd_r401_phase_branch_tube_mp_a1"
PYTEST_TO_TOTAL = {
    "prefreeze_focused_pytest": "prefreeze_focused",
    "l3_a1_modules_pytest": "l3_a1_modules",
    "paper02_full_pytest": "paper02_full",
}
PYTEST_SUMMARY = re.compile(
    r"(?P<counts>[0-9]+ (?:passed|failed|skipped|xfailed|xpassed)"
    r"(?:, [0-9]+ (?:passed|failed|skipped|xfailed|xpassed))*) "
    r"in [0-9]+(?:\.[0-9]+)?s\Z"
)


class PrefreezeCheckError(RuntimeError):
    """The candidate violates the independently duplicated contract."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PrefreezeCheckError(message)


def canonical_json_bytes(payload: Any) -> bytes:
    def visit(value: Any, context: str = "$") -> None:
        if value is None or type(value) in (bool, str, int):
            return
        if type(value) is list:
            for index, item in enumerate(value):
                visit(item, f"{context}[{index}]")
            return
        require(type(value) is dict, f"{context}: unsupported JSON type")
        for key, item in value.items():
            require(type(key) is str, f"{context}: non-string key")
            visit(item, f"{context}.{key}")
    visit(payload)
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      allow_nan=False).encode("utf-8") + b"\n"


def strict_json_image(raw: bytes) -> dict[str, Any]:
    require(len(raw) <= MAX_CANDIDATE_BYTES, "candidate exceeds byte cap")
    require(not raw.startswith(b"\xef\xbb\xbf"), "UTF-8 BOM is forbidden")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise PrefreezeCheckError("candidate is not strict UTF-8") from error
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            require(key not in result, f"duplicate JSON key: {key}")
            result[key] = value
        return result
    try:
        payload = json.loads(text, object_pairs_hook=pairs,
                             parse_constant=lambda token: (_ for _ in ()).throw(
                                 PrefreezeCheckError(f"invalid JSON constant: {token}")))
    except (json.JSONDecodeError, UnicodeError) as error:
        raise PrefreezeCheckError("malformed candidate JSON") from error
    require(type(payload) is dict, "candidate root is not an object")
    require(raw == canonical_json_bytes(payload), "candidate is not CJ_COMPACT_V1 plus LF")
    return payload


def exact_dict(value: Any, keys: frozenset[str], context: str) -> dict[str, Any]:
    require(type(value) is dict and set(value) == keys, f"{context}: exact key set mismatch")
    return value


def exact_string(value: Any, context: str, expected: str | None = None) -> str:
    require(type(value) is str and value != "" and "\x00" not in value,
            f"{context}: nonempty exact string required")
    if expected is not None:
        require(value == expected, f"{context}: literal mismatch")
    return value


def exact_int(value: Any, context: str, minimum: int = 0, expected: int | None = None) -> int:
    require(type(value) is int and value >= minimum, f"{context}: exact integer out of range")
    if expected is not None:
        require(value == expected, f"{context}: integer mismatch")
    return value


def exact_bool(value: Any, context: str, expected: bool) -> None:
    require(type(value) is bool and value is expected, f"{context}: Boolean mismatch")


def exact_hash(value: Any, context: str, expected: str | None = None) -> str:
    value = exact_string(value, context)
    require(HEX64.fullmatch(value) is not None, f"{context}: lowercase SHA-256 required")
    if expected is not None:
        require(value == expected, f"{context}: hash mismatch")
    return value


def exact_utc(value: Any, context: str) -> datetime:
    value = exact_string(value, context)
    require(UTC.fullmatch(value) is not None, f"{context}: whole-second UTC required")
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError as error:
        raise PrefreezeCheckError(f"{context}: invalid timestamp") from error
    require(parsed.strftime("%Y-%m-%dT%H:%M:%SZ") == value, f"{context}: noncanonical timestamp")
    return parsed


def exact_relative(value: Any, context: str, expected: str | None = None) -> str:
    value = exact_string(value, context, expected)
    pure = PurePosixPath(value)
    require("\\" not in value and not pure.is_absolute() and os.fspath(pure) == value
            and pure.parts and all(part not in ("", ".", "..") for part in pure.parts),
            f"{context}: canonical relative POSIX path required")
    return value


def json_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(json_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(json_equal(a, b) for a, b in zip(left, right, strict=True))
    return bool(left == right)


def validate_file_binding(binding: Any, expected_path: str, context: str,
                          *, with_role: str | None = None, verify_live: bool = True) -> dict[str, Any]:
    keys = ROLE_ENTRY_KEYS if with_role is not None else FILE_BINDING_KEYS
    binding = exact_dict(binding, keys, context)
    if with_role is not None:
        exact_string(binding["role"], f"{context}.role", with_role)
    path = exact_relative(binding["path"], f"{context}.path", expected_path)
    digest = exact_hash(binding["sha256"], f"{context}.sha256")
    size = exact_int(binding["size_bytes"], f"{context}.size_bytes", 1)
    mode_text = exact_string(binding["mode"], f"{context}.mode")
    require(re.fullmatch(r"0[0-7]{3}", mode_text) is not None, f"{context}.mode: octal mode required")
    exact_int(binding["nlink"], f"{context}.nlink", 1, 1)
    if verify_live:
        raw, info = read_pinned_absolute(ROOT / path, MAX_ROLE_BYTES, context,
                                         modes={int(mode_text, 8)})
        require(len(raw) == size, f"{context}: live size mismatch")
        require(hashlib.sha256(raw).hexdigest() == digest, f"{context}: live hash mismatch")
        require(info.st_nlink == binding["nlink"], f"{context}: live nlink mismatch")
    return binding


def validate_verify_receipt(value: Any, status: str, digest: str, size: int,
                            context: str) -> dict[str, Any]:
    receipt = exact_dict(value, VERIFY_RECEIPT_KEYS, context)
    exact_string(receipt["verification_status"], f"{context}.verification_status", status)
    exact_string(receipt["authority"], f"{context}.authority", VERIFY_AUTHORITY)
    exact_hash(receipt["candidate_sha256"], f"{context}.candidate_sha256", digest)
    exact_int(receipt["size_bytes"], f"{context}.size_bytes", 0, size)
    exact_bool(receipt["promotion_authorized"], f"{context}.promotion_authorized", False)
    return receipt


def parse_pytest(stdout: str, context: str) -> dict[str, int]:
    require("\x1b" not in stdout and "\r" not in stdout and stdout.endswith("\n"),
            f"{context}: ANSI/CR/nonterminated transcript")
    require(not any(separator in stdout for separator in ("\u0085", "\u2028", "\u2029")),
            f"{context}: non-LF Unicode line separator in transcript")
    require(all(character == "\n" or (ord(character) >= 32 and ord(character) != 127)
                for character in stdout),
            f"{context}: control character in transcript")
    lines = stdout[:-1].split("\n")
    matches = [(index, PYTEST_SUMMARY.fullmatch(line)) for index, line in enumerate(lines)]
    matches = [(index, match) for index, match in matches if match is not None]
    require(len(matches) == 1 and matches[0][0] == len(lines) - 1,
            f"{context}: exactly one terminal summary required")
    forbidden = re.compile(
        r"(?i)(?<![A-Za-z0-9_])(?:errors?|fail(?:ed|ures?)?|warnings?|"
        r"deselected|skipped|xfail(?:ed)?|xpass(?:ed)?)(?![A-Za-z0-9_])"
    )
    require(forbidden.search(stdout) is None, f"{context}: failure/unmodeled pytest token")
    counts = {key: 0 for key in PYTEST_COUNT_KEYS}
    seen: set[str] = set()
    match = matches[0][1]
    assert match is not None
    for token in match.group("counts").split(", "):
        number, category = token.split(" ", 1)
        require(category not in seen, f"{context}: duplicate pytest category")
        seen.add(category)
        counts[category] = int(number)
    require(counts["passed"] > 0 and all(counts[key] == 0 for key in counts if key != "passed"),
            f"{context}: pytest evidence is not all-pass")
    return counts


def validate_second_receipt(value: Any, roles: dict[str, dict[str, Any]],
                            context: str) -> dict[str, Any]:
    receipt = exact_dict(value, SECOND_REBUILD_RECEIPT_KEYS, context)
    exact_string(receipt["verification_status"], f"{context}.verification_status", SECOND_REBUILD_STATUS)
    exact_string(receipt["authority"], f"{context}.authority", SECOND_REBUILD_AUTHORITY)
    source = roles["branch_evaluator_source"]
    binary = roles["branch_evaluator_binary"]
    exact_relative(receipt["source_path"], f"{context}.source_path", source["path"])
    exact_hash(receipt["source_sha256"], f"{context}.source_sha256", source["sha256"])
    exact_relative(receipt["persistent_binary_path"], f"{context}.persistent_binary_path",
                   binary["path"])
    for field in ("persistent_before_sha256", "persistent_after_sha256", "staging_output_sha256"):
        exact_hash(receipt[field], f"{context}.{field}", binary["sha256"])
    exact_int(receipt["staging_output_size_bytes"], f"{context}.staging_output_size_bytes",
              1, binary["size_bytes"])
    exact_string(receipt["staging_output_mode"], f"{context}.staging_output_mode", binary["mode"])
    for field in ("persistent_before_device_id", "persistent_before_inode",
                  "persistent_after_device_id", "persistent_after_inode"):
        exact_int(receipt[field], f"{context}.{field}", 1)
    require(receipt["persistent_before_device_id"] == receipt["persistent_after_device_id"]
            and receipt["persistent_before_inode"] == receipt["persistent_after_inode"],
            f"{context}: persistent inode changed")
    exact_bool(receipt["persistent_identity_unchanged"], f"{context}.persistent_identity_unchanged", True)
    exact_bool(receipt["persistent_overwrite_performed"], f"{context}.persistent_overwrite_performed", False)
    exact_bool(receipt["byte_for_byte_equal"], f"{context}.byte_for_byte_equal", True)
    exact_bool(receipt["scientific_evaluator_dispatched"], f"{context}.scientific_evaluator_dispatched", False)
    exact_bool(receipt["staging_output_removed"], f"{context}.staging_output_removed", True)
    return receipt


def validate_argv(name: str, value: Any, context: str) -> list[str]:
    require(type(value) is list and value and all(type(item) is str and item and "\x00" not in item
                                                  for item in value),
            f"{context}: exact nonempty argv required")
    if name != "second_fresh_rebuild":
        require(tuple(value) == FIXED_COMMAND_ARGV[name], f"{context}: fixed argv mismatch")
        return value
    require(tuple(value[:-1]) == REBUILD_COMMAND_ARGV_PREFIX, f"{context}: rebuild prefix mismatch")
    output_text = value[-1]
    output = PurePosixPath(output_text)
    require(output.is_absolute() and os.fspath(output) == output_text
            and output.parts[:2] == ("/", "tmp") and output.name == REBUILD_OUTPUT_BASENAME
            and all(part not in ("", ".", "..") for part in output.parts[1:]),
            f"{context}: unsafe rebuild output")
    prefix = "a416-l3a1-role11-rebuild."
    require(output.parent.parent == PurePosixPath("/tmp") and output.parent.name.startswith(prefix),
            f"{context}: rebuild output parent mismatch")
    suffix = output.parent.name[len(prefix):]
    require(len(suffix) >= 6 and suffix.isalnum() and suffix.isascii(),
            f"{context}: rebuild suffix mismatch")
    return value


def validate_command(value: Any, index: int, roles: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], dict[str, int] | None]:
    name, kind = COMMAND_SPECS[index]
    context = f"command_results[{index}]"
    result = exact_dict(value, COMMAND_RESULT_KEYS, context)
    exact_string(result["name"], f"{context}.name", name)
    exact_string(result["kind"], f"{context}.kind", kind)
    validate_argv(name, result["argv"], f"{context}.argv")
    exact_string(result["cwd"], f"{context}.cwd", os.fspath(ROOT))
    require(json_equal(result["environment"], CLEAN_ENVIRONMENT), f"{context}: environment mismatch")
    exact_int(result["return_code"], f"{context}.return_code", 0, 0)
    exact_utc(result["started_at_utc"], f"{context}.started_at_utc")
    exact_int(result["wall_duration_ms"], f"{context}.wall_duration_ms", 1)
    for stream, cap in (("stdout", MAX_STDOUT_BYTES), ("stderr", MAX_STDERR_BYTES)):
        text_value = result[f"{stream}_utf8"]
        require(type(text_value) is str and "\x00" not in text_value,
                f"{context}.{stream}_utf8: NUL-free exact string required")
        try:
            raw = text_value.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise PrefreezeCheckError(f"{context}.{stream}_utf8: invalid UTF-8") from error
        require(len(raw) <= cap, f"{context}.{stream}: cap exceeded")
        exact_int(result[f"{stream}_size_bytes"], f"{context}.{stream}_size_bytes", 0, len(raw))
        exact_hash(result[f"{stream}_sha256"], f"{context}.{stream}_sha256",
                   hashlib.sha256(raw).hexdigest())
    require(result["stderr_utf8"] == "", f"{context}: passing stderr must be empty")

    if name in PYTEST_TO_TOTAL:
        counts = parse_pytest(result["stdout_utf8"], context)
        recorded = exact_dict(result["pytest_counts"], PYTEST_COUNT_KEYS,
                              f"{context}.pytest_counts")
        for category in PYTEST_COUNT_KEYS:
            exact_int(recorded[category], f"{context}.pytest_counts.{category}", 0,
                      counts[category])
        require(result["semantic_receipt"] is None, f"{context}: pytest receipt must be null")
        return result, counts

    require(result["pytest_counts"] is None, f"{context}: non-pytest counts must be null")
    if name == "role24_machine_verify":
        validate_verify_receipt(result["semantic_receipt"], MACHINE_VERIFY_STATUS,
                                MACHINE_SHA256, MACHINE_SIZE_BYTES,
                                f"{context}.semantic_receipt")
        expected = (f"machine_freeze_verification={MACHINE_VERIFY_STATUS} "
                    f"authority={VERIFY_AUTHORITY} candidate_sha256={MACHINE_SHA256} "
                    f"size_bytes={MACHINE_SIZE_BYTES} promotion_authorized=false\n")
        require(result["stdout_utf8"] == expected, f"{context}: transcript mismatch")
    elif name == "role13_compatibility_verify":
        validate_verify_receipt(result["semantic_receipt"], ROLE13_VERIFY_STATUS,
                                ROLE13_SHA256, ROLE13_SIZE_BYTES,
                                f"{context}.semantic_receipt")
        expected = (f"s0_compatibility_verification={ROLE13_VERIFY_STATUS} "
                    f"authority={VERIFY_AUTHORITY} candidate_sha256={ROLE13_SHA256} "
                    f"size_bytes={ROLE13_SIZE_BYTES} promotion_authorized=false\n")
        require(result["stdout_utf8"] == expected, f"{context}: transcript mismatch")
    elif name == "git_diff_check":
        require(result["stdout_utf8"] == "" and result["semantic_receipt"] is None,
                f"{context}: diff success must be empty/null")
    else:
        receipt = validate_second_receipt(result["semantic_receipt"], roles,
                                          f"{context}.semantic_receipt")
        require(result["stdout_utf8"].encode("utf-8") == canonical_json_bytes(receipt),
                f"{context}: rebuild raw receipt mismatch")
    return result, None


def validate_repository(value: Any) -> dict[str, Any]:
    snapshot = exact_dict(value, REPOSITORY_SNAPSHOT_KEYS, "repository_snapshot")
    exact_string(snapshot["authority_root"], "repository_snapshot.authority_root", os.fspath(ROOT))
    exact_string(snapshot["branch"], "repository_snapshot.branch", "main")
    oids: list[str] = []
    for field in ("capture_commit_oid", "capture_tree_oid", "origin_main_oid", "live_remote_main_oid"):
        oid = exact_string(snapshot[field], f"repository_snapshot.{field}")
        require(re.fullmatch(r"[0-9a-f]{40}", oid) is not None,
                f"repository_snapshot.{field}: Git OID required")
        oids.append(oid)
    require(oids[0] == oids[2] == oids[3], "repository snapshot commit OIDs differ")
    exact_string(snapshot["origin_url"], "repository_snapshot.origin_url", ORIGIN_URL)
    for field in ("head_equals_origin_main", "head_equals_live_remote_main",
                  "worktree_clean_before", "worktree_clean_after"):
        exact_bool(snapshot[field], f"repository_snapshot.{field}", True)
    exact_int(snapshot["ahead"], "repository_snapshot.ahead", 0, 0)
    exact_int(snapshot["behind"], "repository_snapshot.behind", 0, 0)
    return snapshot


def validate_machine_live(roles: dict[str, dict[str, Any]]) -> None:
    raw, _ = read_pinned_absolute(ROOT / MACHINE_RELATIVE, MAX_ROLE_BYTES,
                                  "canonical machine role10", modes={0o644})
    require(len(raw) == MACHINE_SIZE_BYTES and hashlib.sha256(raw).hexdigest() == MACHINE_SHA256,
            "canonical machine role10 raw identity mismatch")
    machine = strict_json_image(raw)
    machine_keys = frozenset({
        "artifact_role", "authority", "branch_binary", "capd", "capture",
        "claim_boundary", "compiler", "component_status", "filesystem",
        "final_status", "machine_observations", "machine_requirements",
        "milestone_status", "production_authorized", "protocol_id", "python_arb",
        "resource_admission", "resource_evidence", "runtime_libraries",
        "schema_version", "scientific_licensing_enabled", "status", "theorem_status",
    })
    exact_dict(machine, machine_keys, "machine role10")
    exact_int(machine["schema_version"], "machine.schema_version", 0, 1)
    exact_string(machine["protocol_id"], "machine.protocol_id", "R401-VAL-L3-A1")
    exact_string(machine["artifact_role"], "machine.artifact_role", "MACHINE_FREEZE")
    exact_string(machine["status"], "machine.status", "FROZEN_FOR_PRODUCTION")
    exact_string(machine["authority"], "machine.authority", "MACHINE_ADMISSION_ONLY")
    exact_bool(machine["scientific_licensing_enabled"], "machine.scientific_licensing_enabled", True)
    exact_bool(machine["production_authorized"], "machine.production_authorized", False)
    for field in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(machine[field] is None, f"machine.{field}: null required")
    capture = exact_dict(machine["capture"], frozenset({
        "boot_id_sha256", "capture_tool_path", "capture_tool_sha256", "captured_at_utc",
    }), "machine.capture")
    exact_relative(capture["capture_tool_path"], "machine.capture.capture_tool_path",
                   roles["scheduler"]["path"])
    exact_hash(capture["capture_tool_sha256"], "machine.capture.capture_tool_sha256",
               roles["scheduler"]["sha256"])
    branch = exact_dict(machine["branch_binary"], frozenset({
        "build_id", "dt_needed", "dt_needed_sha256", "elf_sha256", "executable_mode",
        "path", "runtime_libraries_sha256", "sha256", "size_bytes", "source_path",
        "source_sha256",
    }), "machine.branch_binary")
    exact_relative(branch["path"], "machine.branch_binary.path", roles["branch_evaluator_binary"]["path"])
    exact_hash(branch["sha256"], "machine.branch_binary.sha256",
               roles["branch_evaluator_binary"]["sha256"])
    exact_int(branch["size_bytes"], "machine.branch_binary.size_bytes", 1,
              roles["branch_evaluator_binary"]["size_bytes"])
    exact_relative(branch["source_path"], "machine.branch_binary.source_path",
                   roles["branch_evaluator_source"]["path"])
    exact_hash(branch["source_sha256"], "machine.branch_binary.source_sha256",
               roles["branch_evaluator_source"]["sha256"])


ROLE13_CONTROL_PATHS = {
    "static_summary": "results/r401_val_l3_phase_tube_smoke/summary.json",
    "static_manifest": "results/r401_val_l3_phase_tube_smoke/manifest.json",
    "static_checker": "results/r401_val_l3_phase_tube_smoke/independent_checker.json",
    "branch_summary": "results/r401_val_l3_branch_tube_smoke/summary.json",
    "branch_manifest": "results/r401_val_l3_branch_tube_smoke/manifest.json",
    "branch_checker": "results/r401_val_l3_branch_tube_smoke/independent_checker.json",
    "composite_summary": "results/r401_val_l3_s0_composite/summary.json",
    "composite_manifest": "results/r401_val_l3_s0_composite/manifest.json",
    "composite_checker": "results/r401_val_l3_s0_composite/independent_checker.json",
}
ROLE13_SOURCE_PATHS = (
    "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md",
    "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md",
    "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md",
    "scripts/replay_r401_val_l3_s0_through_a1_checkers.py",
)
ROLE13_CLAIM_BOUNDARY = (
    "read-only compatibility replay of the sealed representative 3x2 S0 archive only; "
    "non-licensing and no evaluator dispatch; no all-slab result, theorem promotion, "
    "global orbit exclusion, trace formula, Hilbert-Polya construction, zeta-zero result, "
    "or RH claim"
)


def validate_s0_compatibility(path: Path) -> tuple[dict[str, Any], bytes]:
    require(os.fspath(path) == os.fspath(ROOT / ROLE13_RELATIVE),
            "S0 verify target must be the fixed canonical role13 path")
    raw, _ = read_pinned_absolute(path, MAX_ROLE_BYTES, "canonical role13", modes={0o644})
    require(len(raw) == ROLE13_SIZE_BYTES and hashlib.sha256(raw).hexdigest() == ROLE13_SHA256,
            "canonical role13 raw identity mismatch")
    payload = strict_json_image(raw)
    exact_dict(payload, frozenset({
        "artifact_role", "artifact_status", "branch_facts", "claim_boundary",
        "composite_facts", "control_hashes", "failures", "final_status", "matrix",
        "milestone_status", "protocol_id", "replay_status", "role_sets",
        "schema_version", "source_bindings", "source_protocols", "static_facts",
        "theorem_status",
    }), "role13")
    exact_int(payload["schema_version"], "role13.schema_version", 0, 1)
    exact_string(payload["protocol_id"], "role13.protocol_id",
                 "R401-VAL-L3-A1-PREFREEZE-S0-COMPATIBILITY")
    exact_string(payload["artifact_role"], "role13.artifact_role", "S0_TO_A1_COMPATIBILITY_REPLAY")
    exact_string(payload["artifact_status"], "role13.artifact_status", "NON_LICENSING")
    exact_string(payload["replay_status"], "role13.replay_status", "PASS_S0_COMPATIBILITY_REPLAY")
    exact_string(payload["claim_boundary"], "role13.claim_boundary", ROLE13_CLAIM_BOUNDARY)
    for field in ("milestone_status", "theorem_status", "final_status"):
        require(payload[field] is None, f"role13.{field}: null required")
    require(payload["failures"] == [] and type(payload["failures"]) is list,
            "role13.failures must be exact empty list")
    require(json_equal(payload["matrix"], {"cell_count": 6, "precisions": [128, 256],
                                            "slabs": ["S000", "S025", "S050"]}),
            "role13.matrix mismatch")
    require(json_equal(payload["source_protocols"], {
        "branch": "R401-VAL-L3-BT-S0", "composite": "R401-VAL-L3-S0-COMPOSITE-DRAFT",
        "static": "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT",
    }), "role13.source_protocols mismatch")
    require(json_equal(payload["branch_facts"], {"manifest_file_count": 26, "raw_replay_count": 6}),
            "role13.branch_facts mismatch")
    require(json_equal(payload["composite_facts"], {
        "cell_replay_count": 6, "failure_count": 0, "manifest_binding_count": 18,
    }), "role13.composite_facts mismatch")
    require(json_equal(payload["static_facts"], {
        "independent_interval_checks": 122300, "internal_count": 42074,
        "maximum_depth": 14, "node_count": 84172, "proof_count": 6,
        "terminal_count": 42098, "unresolved_count": 0,
    }), "role13.static_facts mismatch")
    controls = exact_dict(payload["control_hashes"], frozenset(ROLE13_CONTROL_PATHS),
                          "role13.control_hashes")
    for name, relative in ROLE13_CONTROL_PATHS.items():
        digest = exact_hash(controls[name], f"role13.control_hashes.{name}")
        control_raw, _ = read_pinned_absolute(ROOT / relative, MAX_ROLE_BYTES,
                                              f"role13 control {name}", modes={0o644})
        require(hashlib.sha256(control_raw).hexdigest() == digest,
                f"role13 control {name}: live hash mismatch")
    bindings = exact_dict(payload["source_bindings"], frozenset(ROLE13_SOURCE_PATHS),
                          "role13.source_bindings")
    for relative in ROLE13_SOURCE_PATHS:
        digest = exact_hash(bindings[relative], f"role13.source_bindings.{relative}")
        source_raw, _ = read_pinned_absolute(ROOT / relative, MAX_ROLE_BYTES,
                                             f"role13 source {relative}", modes={0o644})
        require(hashlib.sha256(source_raw).hexdigest() == digest,
                f"role13 source {relative}: live hash mismatch")
    role_sets = exact_dict(payload["role_sets"], frozenset({
        "branch_manifest_roles", "composite_component_roles", "composite_manifest_roles",
        "static_proof_entries",
    }), "role13.role_sets")
    require(type(role_sets["branch_manifest_roles"]) is list and len(role_sets["branch_manifest_roles"]) == 26,
            "role13 branch role count mismatch")
    require(type(role_sets["composite_component_roles"]) is list and len(role_sets["composite_component_roles"]) == 6,
            "role13 component role count mismatch")
    require(type(role_sets["composite_manifest_roles"]) is list and len(role_sets["composite_manifest_roles"]) == 12,
            "role13 manifest role count mismatch")
    proofs = role_sets["static_proof_entries"]
    require(type(proofs) is list and len(proofs) == 6 and all(type(item) is dict for item in proofs),
            "role13 proof entry count mismatch")
    require(sum(item.get("node_count", -1) for item in proofs) == 84172
            and sum(item.get("internal_count", -1) for item in proofs) == 42074
            and sum(item.get("terminal_count", -1) for item in proofs) == 42098
            and all(item.get("unresolved_count") == 0 for item in proofs),
            "role13 proof aggregate mismatch")
    return payload, raw


def validate_record(payload: dict[str, Any], *, verify_live: bool = False) -> None:
    """Validate the full closed role-11 record; live replay is opt-in for tests."""

    exact_dict(payload, TOP_LEVEL_KEYS, "role11")
    require(len(PRE_REVIEW_INPUT_ROLES) == 51, "independent 51-role map invariant")
    require(len(COMMAND_SPECS) == 7, "independent seven-command invariant")
    exact_int(payload["schema_version"], "schema_version", 0, 1)
    exact_string(payload["protocol_id"], "protocol_id", PROTOCOL_ID)
    exact_string(payload["artifact_role"], "artifact_role", "PREFREEZE_TEST_RECORD")
    exact_string(payload["artifact_status"], "artifact_status",
                 "PASS_PENDING_INDEPENDENT_PREFREEZE_REVIEW")
    exact_string(payload["authority"], "authority", "PREFREEZE_TEST_EVIDENCE_ONLY")
    recorded_at = exact_utc(payload["recorded_at_utc"], "recorded_at_utc")
    for field in ("scientific_licensing_enabled", "production_authorized",
                  "scientific_dispatch_performed"):
        exact_bool(payload[field], field, False)
    for field in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[field] is None, f"{field}: null required")

    policy = exact_dict(payload["held_out_policy"], HELD_OUT_POLICY_KEYS, "held_out_policy")
    exact_bool(policy["held_out_l3_scientific_outputs_read"],
               "held_out_policy.held_out_l3_scientific_outputs_read", False)
    exact_bool(policy["held_out_l3_evaluator_dispatched"],
               "held_out_policy.held_out_l3_evaluator_dispatched", False)
    exact_int(policy["scientific_evaluator_dispatch_count"],
              "held_out_policy.scientific_evaluator_dispatch_count", 0, 0)
    exact_string(policy["new_archive_scope"], "held_out_policy.new_archive_scope",
                 "TEMPORARY_MOCK_ONLY")
    exact_string(policy["s0_archive_access"], "held_out_policy.s0_archive_access",
                 "READ_ONLY_SEALED_PUBLIC_SIX_CELL")
    exact_bool(policy["canonical_result_created"], "held_out_policy.canonical_result_created", False)
    validate_repository(payload["repository_snapshot"])

    entries = payload["pre_review_input_roles"]
    require(type(entries) is list and len(entries) == 51, "pre-review role count mismatch")
    roles: dict[str, dict[str, Any]] = {}
    seen_paths: set[str] = set()
    for index, (item, (role, path)) in enumerate(zip(entries, PRE_REVIEW_INPUT_ROLES, strict=True)):
        validated = validate_file_binding(item, path, f"pre_review_input_roles[{index}]",
                                          with_role=role, verify_live=verify_live)
        require(role not in roles and path not in seen_paths, "duplicate role/path")
        roles[role] = validated
        seen_paths.add(path)

    tools = exact_dict(payload["evidence_tool_bindings"], EVIDENCE_TOOL_BINDING_KEYS,
                       "evidence_tool_bindings")
    expected_tools = {
        "producer": PRODUCER_RELATIVE, "independent_checker": CHECKER_RELATIVE,
        "focused_test": TEST_RELATIVE,
    }
    tool_paths: set[str] = set()
    for name, path in expected_tools.items():
        binding = validate_file_binding(tools[name], path, f"evidence_tool_bindings.{name}",
                                        verify_live=verify_live)
        require(binding["path"] not in tool_paths, "duplicate evidence tool path")
        tool_paths.add(binding["path"])

    results = payload["command_results"]
    require(type(results) is list and len(results) == 7, "command result count mismatch")
    validated_results: list[dict[str, Any]] = []
    parsed_counts: dict[str, dict[str, int]] = {}
    previous_start: datetime | None = None
    for index, item in enumerate(results):
        result, counts = validate_command(item, index, roles)
        start = exact_utc(result["started_at_utc"], f"command_results[{index}].started_at_utc")
        require(previous_start is None or start >= previous_start,
                "command start timestamps are not ordered")
        require(start <= recorded_at, "command starts after record timestamp")
        previous_start = start
        validated_results.append(result)
        if counts is not None:
            parsed_counts[result["name"]] = counts

    prerequisites = exact_dict(payload["prerequisite_bindings"], PREREQUISITE_BINDING_KEYS,
                               "prerequisite_bindings")
    machine = exact_dict(prerequisites["machine_role10"], MACHINE_BINDING_KEYS,
                         "prerequisite_bindings.machine_role10")
    role10 = roles["machine_freeze"]
    for field in ROLE_ENTRY_KEYS:
        require(json_equal(machine[field], role10[field]), f"machine cross-binding mismatch: {field}")
    exact_hash(machine["sha256"], "machine_role10.sha256", MACHINE_SHA256)
    exact_int(machine["size_bytes"], "machine_role10.size_bytes", 1, MACHINE_SIZE_BYTES)
    exact_string(machine["mode"], "machine_role10.mode", "0644")
    exact_string(machine["publication_commit_oid"], "machine_role10.publication_commit_oid",
                 MACHINE_PUBLICATION_COMMIT)
    exact_relative(machine["producer_path"], "machine_role10.producer_path",
                   "scripts/run_r401_val_l3_a1_all_slabs.py")
    exact_hash(machine["producer_sha256"], "machine_role10.producer_sha256",
               roles["scheduler"]["sha256"])
    exact_relative(machine["verifier_path"], "machine_role10.verifier_path",
                   "scripts/build_r401_val_l3_a1_release_provenance.py")
    exact_hash(machine["verifier_sha256"], "machine_role10.verifier_sha256",
               roles["release_builder"]["sha256"])
    exact_bool(machine["promotion_authorized"], "machine_role10.promotion_authorized", False)
    machine_receipt = validate_verify_receipt(machine["verify_receipt"], MACHINE_VERIFY_STATUS,
                                              MACHINE_SHA256, MACHINE_SIZE_BYTES,
                                              "machine_role10.verify_receipt")
    require(json_equal(machine_receipt, validated_results[0]["semantic_receipt"]),
            "machine receipt cross-binding mismatch")

    compatibility = exact_dict(prerequisites["s0_compatibility_role13"], ROLE13_BINDING_KEYS,
                               "prerequisite_bindings.s0_compatibility_role13")
    role13 = roles["s0_compatibility"]
    for field in ROLE_ENTRY_KEYS:
        require(json_equal(compatibility[field], role13[field]), f"role13 cross-binding mismatch: {field}")
    exact_hash(compatibility["sha256"], "role13.sha256", ROLE13_SHA256)
    exact_int(compatibility["size_bytes"], "role13.size_bytes", 1, ROLE13_SIZE_BYTES)
    exact_string(compatibility["mode"], "role13.mode", "0644")
    exact_string(compatibility["publication_commit_oid"], "role13.publication_commit_oid",
                 ROLE13_PUBLICATION_COMMIT)
    exact_relative(compatibility["producer_path"], "role13.producer_path",
                   "scripts/replay_r401_val_l3_s0_through_a1_checkers.py")
    exact_hash(compatibility["producer_sha256"], "role13.producer_sha256",
               roles["s0_adapter"]["sha256"])
    exact_bool(compatibility["promotion_authorized"], "role13.promotion_authorized", False)
    role13_receipt = validate_verify_receipt(compatibility["verify_receipt"], ROLE13_VERIFY_STATUS,
                                             ROLE13_SHA256, ROLE13_SIZE_BYTES,
                                             "role13.verify_receipt")
    require(json_equal(role13_receipt, validated_results[1]["semantic_receipt"]),
            "role13 receipt cross-binding mismatch")

    absence = exact_dict(prerequisites["canonical_absence"], CANONICAL_ABSENCE_KEYS,
                         "prerequisite_bindings.canonical_absence")
    for field in CANONICAL_ABSENCE_KEYS:
        exact_bool(absence[field], f"canonical_absence.{field}", False)

    rebuild = exact_dict(prerequisites["second_fresh_rebuild_replay"],
                         SECOND_REBUILD_REPLAY_KEYS, "second_fresh_rebuild_replay")
    exact_string(rebuild["command_result_name"], "second_fresh_rebuild_replay.command_result_name",
                 "second_fresh_rebuild")
    command_hash = hashlib.sha256(canonical_json_bytes(validated_results[6])).hexdigest()
    exact_hash(rebuild["command_result_sha256"], "second_fresh_rebuild_replay.command_result_sha256",
               command_hash)
    rebuild_receipt = validate_second_receipt(rebuild["semantic_receipt"], roles,
                                              "second_fresh_rebuild_replay.semantic_receipt")
    require(json_equal(rebuild_receipt, validated_results[6]["semantic_receipt"]),
            "second rebuild receipt cross-binding mismatch")

    totals = exact_dict(payload["test_totals"], TEST_TOTALS_KEYS, "test_totals")
    by_name = {result["name"]: result for result in validated_results}
    for result_name, total_name in PYTEST_TO_TOTAL.items():
        total = exact_dict(totals[total_name], TEST_TOTAL_KEYS, f"test_totals.{total_name}")
        for category in PYTEST_COUNT_KEYS:
            exact_int(total[category], f"test_totals.{total_name}.{category}", 0,
                      parsed_counts[result_name][category])
        exact_int(total["wall_duration_ms"], f"test_totals.{total_name}.wall_duration_ms", 1,
                  by_name[result_name]["wall_duration_ms"])
        if EXPECTED_TEST_PASSED is not None:
            require(set(EXPECTED_TEST_PASSED) == set(PYTEST_TO_TOTAL.values()),
                    "frozen pytest total map key mismatch")
            exact_int(parsed_counts[result_name]["passed"],
                      f"frozen pytest total {result_name}", 1,
                      EXPECTED_TEST_PASSED[total_name])

    require(type(payload["covered_gates"]) is list
            and json_equal(payload["covered_gates"], list(COVERED_GATES)),
            "covered_gates mismatch")
    exact_string(payload["claim_boundary"], "claim_boundary", CLAIM_BOUNDARY)
    require(len(canonical_json_bytes(payload)) <= MAX_CANDIDATE_BYTES, "candidate exceeds byte cap")
    if verify_live:
        require(EXPECTED_TEST_PASSED is not None,
                "live verification is fail-closed until exact pytest totals are frozen")
        validate_git_snapshot(payload["repository_snapshot"], require_current=False)
        validate_machine_live(roles)
        validate_s0_compatibility(ROOT / ROLE13_RELATIVE)
        _, binary_info = read_pinned_absolute(
            ROOT / roles["branch_evaluator_binary"]["path"], MAX_ROLE_BYTES,
            "second rebuild persistent binary replay",
            modes={int(roles["branch_evaluator_binary"]["mode"], 8)},
        )
        live_receipt = validated_results[6]["semantic_receipt"]
        require(
            live_receipt["persistent_before_device_id"] == binary_info.st_dev
            and live_receipt["persistent_after_device_id"] == binary_info.st_dev
            and live_receipt["persistent_before_inode"] == binary_info.st_ino
            and live_receipt["persistent_after_inode"] == binary_info.st_ino,
            "second rebuild receipt/live persistent inode mismatch",
        )


def _absolute_parts(path: Path, context: str) -> tuple[str, ...]:
    text = os.fspath(path)
    require(text.startswith("/") and not text.startswith("//"), f"{context}: one root slash required")
    pure = PurePosixPath(text)
    require(os.fspath(pure) == text and pure.is_absolute(), f"{context}: canonical absolute path required")
    parts = pure.parts[1:]
    require(parts and all(part not in ("", ".", "..") for part in parts),
            f"{context}: unsafe component")
    return parts


def _signature(info: os.stat_result) -> tuple[int, int, int, int, int, int, int]:
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink, info.st_size,
            info.st_mtime_ns, info.st_ctime_ns)


def _directory_identity(info: os.stat_result) -> tuple[int, int, int, int]:
    return (info.st_dev, info.st_ino, stat.S_IFMT(info.st_mode), stat.S_IMODE(info.st_mode))


def _namespace_signature(parts: tuple[str, ...], context: str, *,
                         terminal_kind: str = "regular") -> tuple[tuple[str, tuple[int, ...]], ...]:
    flags = os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    rows: list[tuple[str, tuple[int, ...]]] = []
    try:
        for index, part in enumerate(parts):
            info = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            identity = _signature(info) if index == len(parts) - 1 else _directory_identity(info)
            rows.append((part, identity))
            if index == len(parts) - 1:
                if terminal_kind == "regular":
                    require(stat.S_ISREG(info.st_mode), f"{context}: terminal is not regular")
                elif terminal_kind == "symlink":
                    require(stat.S_ISLNK(info.st_mode), f"{context}: terminal is not symlink")
                else:
                    raise PrefreezeCheckError(f"{context}: unsupported terminal kind")
                continue
            require(stat.S_ISDIR(info.st_mode), f"{context}: parent is not directory")
            child = os.open(part, flags, dir_fd=descriptor)
            require(_directory_identity(os.fstat(child)) == _directory_identity(info),
                    f"{context}: namespace open race")
            os.close(descriptor)
            descriptor = child
    finally:
        os.close(descriptor)
    return tuple(rows)


def read_pinned_absolute(path: Path, cap: int, context: str, *, modes: set[int],
                         allow_empty: bool = False) -> tuple[bytes, os.stat_result]:
    """Read one file through a no-follow dirfd chain without ever blocking."""

    parts = _absolute_parts(path, context)
    namespace_before = _namespace_signature(parts, context)
    directory_flags = os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", directory_flags)
    try:
        for part in parts[:-1]:
            before = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            require(stat.S_ISDIR(before.st_mode), f"{context}: parent is not a directory")
            child = os.open(part, directory_flags, dir_fd=descriptor)
            opened = os.fstat(child)
            require(_directory_identity(before) == _directory_identity(opened),
                    f"{context}: parent changed during traversal")
            os.close(descriptor)
            descriptor = child
        name = parts[-1]
        before = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
        require(stat.S_ISREG(before.st_mode), f"{context}: target is not regular")
        require(before.st_nlink == 1, f"{context}: target is not single-link")
        require((allow_empty or before.st_size > 0) and before.st_size <= cap,
                f"{context}: target size outside cap")
        require(stat.S_IMODE(before.st_mode) in modes, f"{context}: mode mismatch")
        flags = (os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_CLOEXEC", 0)
                 | getattr(os, "O_NOFOLLOW", 0))
        file_descriptor = os.open(name, flags, dir_fd=descriptor)
        try:
            opened = os.fstat(file_descriptor)
            require(_signature(opened) == _signature(before), f"{context}: open race")
            chunks: list[bytes] = []
            remaining = before.st_size
            while remaining:
                chunk = os.read(file_descriptor, min(1024 * 1024, remaining))
                require(bool(chunk), f"{context}: short read")
                chunks.append(chunk)
                remaining -= len(chunk)
            require(os.read(file_descriptor, 1) == b"", f"{context}: grew during read")
            after = os.fstat(file_descriptor)
            terminal = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
            require(_signature(after) == _signature(before) == _signature(terminal),
                    f"{context}: target changed during read")
            raw = b"".join(chunks)
        finally:
            os.close(file_descriptor)
    finally:
        os.close(descriptor)
    require(_namespace_signature(parts, context) == namespace_before,
            f"{context}: namespace changed during terminal replay")
    return raw, before


def read_pinned_symlink_absolute(path: Path, context: str) -> tuple[bytes, os.stat_result]:
    parts = _absolute_parts(path, context)
    namespace_before = _namespace_signature(parts, context, terminal_kind="symlink")
    flags = os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for part in parts[:-1]:
            before_parent = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            require(stat.S_ISDIR(before_parent.st_mode), f"{context}: parent is not directory")
            child = os.open(part, flags, dir_fd=descriptor)
            require(_directory_identity(os.fstat(child)) == _directory_identity(before_parent),
                    f"{context}: parent open race")
            os.close(descriptor)
            descriptor = child
        name = parts[-1]
        before = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
        require(stat.S_ISLNK(before.st_mode) and before.st_nlink == 1,
                f"{context}: single-link symlink required")
        target = os.readlink(name, dir_fd=descriptor)
        raw = os.fsencode(target)
        require(len(raw) <= 1024 * 1024 and len(raw) == before.st_size,
                f"{context}: symlink target size mismatch")
        after = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
        require(_signature(after) == _signature(before), f"{context}: symlink changed")
    finally:
        os.close(descriptor)
    require(_namespace_signature(parts, context, terminal_kind="symlink") == namespace_before,
            f"{context}: symlink namespace changed during replay")
    return raw, before


def _inflate_git(raw: bytes, context: str, cap: int = 4 * 1024 * 1024) -> bytes:
    inflater = zlib.decompressobj()
    try:
        value = inflater.decompress(raw, cap + 1)
    except zlib.error as error:
        raise PrefreezeCheckError(f"{context}: malformed zlib stream") from error
    require(inflater.eof and len(value) <= cap and not inflater.unconsumed_tail,
            f"{context}: incomplete/oversize zlib stream")
    return value


def _commit_tree_from_framed(framed: bytes, oid: str, context: str) -> str:
    require(hashlib.sha1(framed, usedforsecurity=False).hexdigest() == oid,
            f"{context}: object ID mismatch")
    try:
        header, payload = framed.split(b"\x00", 1)
        kind, size_raw = header.split(b" ", 1)
        size = int(size_raw.decode("ascii"))
    except (ValueError, UnicodeDecodeError) as error:
        raise PrefreezeCheckError(f"{context}: malformed Git header") from error
    require(kind == b"commit" and str(size).encode("ascii") == size_raw and size == len(payload),
            f"{context}: commit kind/size mismatch")
    match = re.match(rb"tree ([0-9a-f]{40})\n", payload)
    require(match is not None, f"{context}: missing canonical tree header")
    assert match is not None
    return match.group(1).decode("ascii")


def _packed_commit(oid: str) -> bytes | None:
    pack_directory = GIT_DIR / "objects/pack"
    try:
        first_names = sorted(
            entry.name for entry in os.scandir(pack_directory)
            if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name)
        )
    except FileNotFoundError:
        return None
    needle = bytes.fromhex(oid)
    matches: list[bytes] = []
    for index_name in first_names:
        index_raw, _ = read_pinned_absolute(pack_directory / index_name, 128 * 1024 * 1024,
                                            f"Git pack index {index_name}", modes={0o444, 0o644})
        require(len(index_raw) >= 8 + 256 * 4 + 40 and index_raw[:4] == b"\xfftOc"
                and struct.unpack_from(">I", index_raw, 4)[0] == 2
                and hashlib.sha1(index_raw[:-20], usedforsecurity=False).digest() == index_raw[-20:],
                f"Git pack index {index_name}: identity/checksum mismatch")
        fanout = struct.unpack_from(">256I", index_raw, 8)
        require(all(a <= b for a, b in zip(fanout, fanout[1:])),
                f"Git pack index {index_name}: unordered fanout")
        count = fanout[-1]
        names_offset = 8 + 256 * 4
        crc_offset = names_offset + count * 20
        offsets_offset = crc_offset + count * 4
        large_offset = offsets_offset + count * 4
        require(large_offset + 40 <= len(index_raw), f"Git pack index {index_name}: truncated")
        low = fanout[needle[0] - 1] if needle[0] else 0
        high = fanout[needle[0]]
        while low < high:
            middle = (low + high) // 2
            candidate = index_raw[names_offset + 20 * middle:names_offset + 20 * (middle + 1)]
            if candidate < needle:
                low = middle + 1
            else:
                high = middle
        if low >= count or index_raw[names_offset + 20 * low:names_offset + 20 * (low + 1)] != needle:
            continue
        offset = struct.unpack_from(">I", index_raw, offsets_offset + 4 * low)[0]
        if offset & 0x80000000:
            location = large_offset + 8 * (offset & 0x7FFFFFFF)
            require(location + 8 <= len(index_raw) - 40, "Git pack large offset is malformed")
            offset = struct.unpack_from(">Q", index_raw, location)[0]
        pack_name = index_name[:-4] + ".pack"
        pack_raw, _ = read_pinned_absolute(pack_directory / pack_name, 1024 * 1024 * 1024,
                                           f"Git pack {pack_name}", modes={0o444, 0o644})
        require(len(pack_raw) >= 32 and pack_raw[:4] == b"PACK"
                and struct.unpack_from(">I", pack_raw, 4)[0] in (2, 3)
                and hashlib.sha1(pack_raw[:-20], usedforsecurity=False).digest() == pack_raw[-20:]
                and index_raw[-40:-20] == pack_raw[-20:]
                and 12 <= offset < len(pack_raw) - 20,
                f"Git pack {pack_name}: identity/checksum mismatch")
        cursor = offset
        first = pack_raw[cursor]
        cursor += 1
        object_type = (first >> 4) & 7
        object_size = first & 0x0F
        shift = 4
        current = first
        while current & 0x80:
            require(cursor < len(pack_raw) - 20 and shift <= 60,
                    "Git packed object header is malformed")
            current = pack_raw[cursor]
            cursor += 1
            object_size |= (current & 0x7F) << shift
            shift += 7
        require(object_type == 1, "Git commit is stored as unsupported delta")
        payload = _inflate_git(pack_raw[cursor:-20], "packed Git commit")
        require(len(payload) == object_size, "packed Git commit size mismatch")
        matches.append(b"commit " + str(len(payload)).encode("ascii") + b"\x00" + payload)
    second_names = sorted(
        entry.name for entry in os.scandir(pack_directory)
        if re.fullmatch(r"pack-[0-9a-f]{40}\.idx", entry.name)
    )
    require(second_names == first_names, "Git pack namespace changed during replay")
    require(len(matches) <= 1, "Git commit is ambiguously packed")
    return matches[0] if matches else None


def git_commit_tree(oid: str) -> str:
    loose = GIT_DIR / "objects" / oid[:2] / oid[2:]
    framed: bytes | None = None
    try:
        raw, _ = read_pinned_absolute(loose, 4 * 1024 * 1024, "loose Git commit",
                                      modes={0o444, 0o644})
    except FileNotFoundError:
        pass
    else:
        framed = _inflate_git(raw, "loose Git commit")
    packed = _packed_commit(oid)
    require(not (framed is not None and packed is not None), "Git commit ambiguously loose/packed")
    framed = framed if framed is not None else packed
    require(framed is not None, "captured Git commit object unavailable")
    assert framed is not None
    return _commit_tree_from_framed(framed, oid, "captured Git commit")


def _git_ref(relative: str) -> str:
    path = GIT_DIR / relative
    try:
        raw, _ = read_pinned_absolute(path, 1024 * 1024, f"Git ref {relative}", modes={0o644})
    except FileNotFoundError:
        packed_raw, _ = read_pinned_absolute(GIT_DIR / "packed-refs", 16 * 1024 * 1024,
                                             "Git packed refs", modes={0o644})
        text = packed_raw.decode("ascii", errors="strict")
        found = [line[:40] for line in text.splitlines()
                 if re.fullmatch(rf"[0-9a-f]{{40}} {re.escape(relative)}", line)]
        require(len(found) == 1, f"Git ref {relative}: missing/ambiguous")
        return found[0]
    text = raw.decode("ascii", errors="strict")
    require(re.fullmatch(r"[0-9a-f]{40}\n", text) is not None,
            f"Git ref {relative}: malformed")
    return text[:-1]


def _git_index_records() -> tuple[list[tuple[str, int, str]], bytes, os.stat_result]:
    raw, info = read_pinned_absolute(GIT_DIR / "index", 128 * 1024 * 1024,
                                     "Git index", modes={0o644})
    require(len(raw) >= 32 and raw[:4] == b"DIRC", "Git index header is malformed")
    version, count = struct.unpack_from(">II", raw, 4)
    require(version == 2 and count > 0, "Git index must be nonempty version 2")
    body, checksum = raw[:-20], raw[-20:]
    require(hashlib.sha1(body, usedforsecurity=False).digest() == checksum,
            "Git index checksum mismatch")
    cursor = 12
    fixed_format = ">LLLLLLLLLL20sH"
    fixed_size = struct.calcsize(fixed_format)
    records: list[tuple[str, int, str]] = []
    for index in range(count):
        entry_start = cursor
        require(cursor + fixed_size <= len(body), f"Git index entry {index} is truncated")
        fields = struct.unpack_from(fixed_format, body, cursor)
        mode, object_id, flags = fields[6], fields[10].hex(), fields[11]
        cursor += fixed_size
        require(flags & 0xF000 == 0, "Git index uses staged/extended entries")
        try:
            path_end = body.index(b"\x00", cursor)
        except ValueError as error:
            raise PrefreezeCheckError("Git index path is unterminated") from error
        path_raw = body[cursor:path_end]
        try:
            path = path_raw.decode("utf-8", errors="strict")
        except UnicodeDecodeError as error:
            raise PrefreezeCheckError("Git index path is not UTF-8") from error
        exact_relative(path, f"Git index entry {index}.path")
        require(flags & 0x0FFF == min(len(path_raw), 0x0FFF),
                "Git index path-length flag mismatch")
        require(mode in (0o100644, 0o100755, 0o120000),
                "Git index contains unsupported file mode")
        cursor = path_end + 1
        while (cursor - entry_start) % 8:
            require(cursor < len(body) and body[cursor] == 0,
                    "Git index padding is malformed")
            cursor += 1
        records.append((path, mode, object_id))
    while cursor < len(body):
        require(cursor + 8 <= len(body), "Git index extension is truncated")
        signature = body[cursor:cursor + 4]
        extension_size = struct.unpack_from(">I", body, cursor + 4)[0]
        cursor += 8
        require(re.fullmatch(rb"[A-Z]{4}", signature) is not None
                and extension_size <= len(body) - cursor,
                "Git index extension is malformed or required")
        cursor += extension_size
    require(records == sorted(records, key=lambda item: item[0].encode("utf-8"))
            and len({item[0] for item in records}) == len(records),
            "Git index paths are unordered or duplicated")
    return records, raw, info


def _index_tree_oid(records: list[tuple[str, int, str]]) -> str:
    def node() -> dict[str, dict[str, Any]]:
        return {"files": {}, "directories": {}}

    root = node()
    for relative, mode, oid in records:
        current = root
        parts = PurePosixPath(relative).parts
        for part in parts[:-1]:
            require(part not in current["files"], "Git index file/directory prefix collision")
            current = current["directories"].setdefault(part, node())
        name = parts[-1]
        require(name not in current["files"] and name not in current["directories"],
                "Git index duplicate tree entry")
        current["files"][name] = (mode, oid)

    def digest(current: dict[str, dict[str, Any]]) -> str:
        entries: list[tuple[bytes, bytes]] = []
        for name, (mode, oid) in current["files"].items():
            encoded = name.encode("utf-8")
            entries.append((encoded, f"{mode:o}".encode("ascii") + b" " + encoded
                            + b"\x00" + bytes.fromhex(oid)))
        for name, child in current["directories"].items():
            encoded = name.encode("utf-8")
            entries.append((encoded + b"/", b"40000 " + encoded + b"\x00"
                            + bytes.fromhex(digest(child))))
        content = b"".join(payload for _, payload in sorted(entries))
        framed = b"tree " + str(len(content)).encode("ascii") + b"\x00" + content
        return hashlib.sha1(framed, usedforsecurity=False).hexdigest()
    return digest(root)


def validate_tracked_worktree(
    expected_tree: str, required_bindings: list[dict[str, Any]] | None = None,
) -> None:
    records, index_raw, index_info = _git_index_records()
    require(_index_tree_oid(records) == expected_tree,
            "Git index tree differs from captured commit tree")
    record_map = {relative: (mode, oid) for relative, mode, oid in records}
    namespace_before = tracked_namespace_signature(records)
    for index, (relative, mode, oid) in enumerate(records):
        if mode == 0o120000:
            raw, _ = read_pinned_symlink_absolute(
                REPOSITORY_ROOT / relative, f"tracked worktree symlink {index}:{relative}"
            )
        else:
            accepted_modes = {
                candidate for candidate in range(0o1000)
                if bool(candidate & 0o111) is (mode == 0o100755)
            }
            raw, info = read_pinned_absolute(
                REPOSITORY_ROOT / relative, 1024 * 1024 * 1024,
                f"tracked worktree file {index}:{relative}",
                modes=accepted_modes, allow_empty=True,
            )
            require(bool(stat.S_IMODE(info.st_mode) & 0o111) is (mode == 0o100755),
                    f"tracked worktree file {relative}: executable-bit mismatch")
        framed = b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw
        require(hashlib.sha1(framed, usedforsecurity=False).hexdigest() == oid,
                f"tracked worktree file {relative}: blob mismatch")
    namespace_after = tracked_namespace_signature(records)
    require(namespace_after == namespace_before,
            "tracked worktree namespace changed across full replay")
    records_after, index_raw_after, index_info_after = _git_index_records()
    require(records_after == records and index_raw_after == index_raw
            and _signature(index_info_after) == _signature(index_info),
            "Git index changed across tracked worktree replay")
    if required_bindings is not None:
        prefix = "zeta_mvp0/papers/paper_02_certified_local_wave_trace/"
        for binding in required_bindings:
            repository_relative = prefix + binding["path"]
            require(repository_relative in record_map,
                    f"authority binding is not tracked at capture tree: {binding['path']}")
            mode, _ = record_map[repository_relative]
            binding_mode = int(binding["mode"], 8)
            require(mode != 0o120000
                    and bool(binding_mode & 0o111) is (mode == 0o100755),
                    f"authority binding/index mode mismatch: {binding['path']}")
            validate_file_binding(
                binding, binding["path"], f"terminal authority replay {binding['path']}",
                with_role=binding.get("role") if "role" in binding else None,
                verify_live=True,
            )


def tracked_namespace_signature(
    records: list[tuple[str, int, str]],
) -> tuple[tuple[str, tuple[tuple[str, tuple[int, ...]], ...]], ...]:
    rows: list[tuple[str, tuple[tuple[str, tuple[int, ...]], ...]]] = []
    for relative, mode, _ in records:
        path = REPOSITORY_ROOT / relative
        parts = _absolute_parts(path, f"tracked namespace {relative}")
        kind = "symlink" if mode == 0o120000 else "regular"
        rows.append((relative, _namespace_signature(parts, f"tracked namespace {relative}",
                                                     terminal_kind=kind)))
    return tuple(rows)


def validate_prefreeze_forbidden_namespaces() -> None:
    relatives = (
        "zeta_mvp0/papers/paper_02_certified_local_wave_trace/research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json",
        "zeta_mvp0/papers/paper_02_certified_local_wave_trace/research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md",
        "zeta_mvp0/papers/paper_02_certified_local_wave_trace/research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json",
        "zeta_mvp0/papers/paper_02_certified_local_wave_trace/results/r401_val_l3_all_slabs",
        "zeta_mvp0/papers/paper_02_certified_local_wave_trace/results/r401_val_l3_all_slabs.operational",
    )
    for relative in relatives:
        require_absent_absolute(REPOSITORY_ROOT / relative,
                                f"prepublication forbidden namespace {relative}")


def require_absent_absolute(path: Path, context: str) -> None:
    parts = _absolute_parts(path, context)
    flags = os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)

    def snapshot() -> tuple[tuple[tuple[str, tuple[int, ...]], ...], bool]:
        descriptor = os.open("/", flags)
        rows: list[tuple[str, tuple[int, ...]]] = []
        try:
            for index, part in enumerate(parts):
                try:
                    info = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
                except FileNotFoundError:
                    rows.append((part, (-1, index)))
                    return tuple(rows), False
                if index == len(parts) - 1:
                    rows.append((part, _signature(info)))
                    return tuple(rows), True
                require(stat.S_ISDIR(info.st_mode), f"{context}: parent is not directory")
                rows.append((part, _directory_identity(info)))
                child = os.open(part, flags, dir_fd=descriptor)
                require(_directory_identity(os.fstat(child)) == _directory_identity(info),
                        f"{context}: parent open race")
                os.close(descriptor)
                descriptor = child
        finally:
            os.close(descriptor)
        raise PrefreezeCheckError(f"{context}: unreachable absence traversal")

    before, exists = snapshot()
    require(not exists, f"{context}: exists")
    after, exists_after = snapshot()
    require(not exists_after and after == before, f"{context}: namespace changed during absence replay")


def validate_git_snapshot(
    snapshot: dict[str, Any], *, require_current: bool,
    required_bindings: list[dict[str, Any]] | None = None,
) -> None:
    commit = snapshot["capture_commit_oid"]
    require(git_commit_tree(commit) == snapshot["capture_tree_oid"],
            "repository snapshot commit/tree mismatch")
    if require_current:
        head_raw, _ = read_pinned_absolute(GIT_DIR / "HEAD", 4096, "Git HEAD", modes={0o644})
        require(head_raw == b"ref: refs/heads/main\n", "Git HEAD is not the exact main symbolic ref")
        require(_git_ref("refs/heads/main") == commit, "current main differs from capture commit")
        require(_git_ref("refs/remotes/origin/main") == snapshot["origin_main_oid"],
                "current origin/main differs from recorded origin")
        validate_prefreeze_forbidden_namespaces()
        validate_tracked_worktree(snapshot["capture_tree_oid"], required_bindings)
        validate_prefreeze_forbidden_namespaces()


def read_candidate(path: Path) -> tuple[dict[str, Any], bytes]:
    canonical = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json"
    owned_parent_identity: tuple[int, int, int, int] | None = None
    owned_entries: tuple[str, ...] | None = None
    if os.fspath(path) == os.fspath(canonical):
        modes = {0o644}
    else:
        parts = _absolute_parts(path, "candidate")
        require(len(parts) == 3 and parts[0] == "tmp",
                "temporary candidate must be /tmp/<owned-dir>/<leaf>")
        parent = path.parent
        parent_info = os.stat(parent, follow_symlinks=False)
        require(stat.S_ISDIR(parent_info.st_mode) and parent_info.st_uid == os.geteuid()
                and stat.S_IMODE(parent_info.st_mode) == 0o700 and parent_info.st_nlink == 2,
                "temporary candidate parent must be euid-owned 0700 nlink2")
        owned_parent_identity = _directory_identity(parent_info)
        owned_entries = tuple(sorted(entry.name for entry in os.scandir(parent)))
        modes = {0o600}
    raw, _ = read_pinned_absolute(path, MAX_CANDIDATE_BYTES, "candidate", modes=modes)
    if owned_parent_identity is not None:
        parent_after = os.stat(path.parent, follow_symlinks=False)
        entries_after = tuple(sorted(entry.name for entry in os.scandir(path.parent)))
        require(_directory_identity(parent_after) == owned_parent_identity
                and entries_after == owned_entries,
                "temporary candidate parent changed during replay")
        require(owned_entries == (path.name,), "temporary candidate parent is not singleton")
    return strict_json_image(raw), raw


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--verify-prefreeze-tests", "--candidate", dest="candidate")
    modes.add_argument("--verify-s0-compatibility")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.verify_s0_compatibility is not None:
            _, raw = validate_s0_compatibility(Path(arguments.verify_s0_compatibility))
            print(
                f"s0_compatibility_verification={ROLE13_VERIFY_STATUS} "
                f"authority={VERIFY_AUTHORITY} "
                f"candidate_sha256={hashlib.sha256(raw).hexdigest()} "
                f"size_bytes={len(raw)} promotion_authorized=false"
            )
            return 0
        candidate_path = Path(arguments.candidate)
        payload, raw = read_candidate(candidate_path)
        validate_record(payload, verify_live=True)
        canonical = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json"
        if os.fspath(candidate_path) != os.fspath(canonical):
            required = [*payload["pre_review_input_roles"],
                        *payload["evidence_tool_bindings"].values()]
            validate_git_snapshot(payload["repository_snapshot"], require_current=True,
                                  required_bindings=required)
        print(
            f"prefreeze_test_verification={PREFREEZE_VERIFY_STATUS} "
            f"authority={VERIFY_AUTHORITY} candidate_sha256={hashlib.sha256(raw).hexdigest()} "
            f"size_bytes={len(raw)} promotion_authorized=false"
        )
        return 0
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
