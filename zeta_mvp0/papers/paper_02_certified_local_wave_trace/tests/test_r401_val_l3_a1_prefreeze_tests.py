from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

import pytest


ROOT = Path(__file__).absolute().parents[1]
PRODUCER_PATH = ROOT / "scripts/build_r401_val_l3_a1_prefreeze_tests.py"
CHECKER_PATH = ROOT / "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


P = load_module(PRODUCER_PATH, "r401_l3_a1_prefreeze_test_producer")
C = load_module(CHECKER_PATH, "r401_l3_a1_prefreeze_test_checker")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def owned_tmp_dir(prefix: str) -> Path:
    path = Path(tempfile.mkdtemp(prefix=prefix, dir="/tmp"))
    path.chmod(0o700)
    return path


def remove_owned_tmp_dir(path: Path) -> None:
    for entry in list(path.iterdir()):
        entry.unlink()
    path.rmdir()


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT.parents[2], text=True
    ).strip()


def verify_receipt(status: str, digest: str, size: int) -> dict:
    return {
        "verification_status": status,
        "authority": P.VERIFY_AUTHORITY,
        "candidate_sha256": digest,
        "size_bytes": size,
        "promotion_authorized": False,
    }


def role_entries() -> list[dict]:
    entries = []
    for index, (role, path) in enumerate(P.PRE_REVIEW_INPUT_ROLES, 1):
        entry = {
            "role": role,
            "path": path,
            "sha256": f"{index:064x}",
            "size_bytes": 1000 + index,
            "mode": "0755" if role == "branch_evaluator_binary" else "0644",
            "nlink": 1,
        }
        if role == "machine_freeze":
            entry.update(sha256=P.MACHINE_SHA256, size_bytes=P.MACHINE_SIZE_BYTES)
        if role == "s0_compatibility":
            entry.update(sha256=P.ROLE13_SHA256, size_bytes=P.ROLE13_SIZE_BYTES)
        entries.append(entry)
    return entries


def pytest_passes(name: str) -> int:
    expected = getattr(P, "EXPECTED_TEST_PASSED", None)
    total_name = P.PYTEST_RESULT_TOTAL_NAMES.get(name)
    value = (
        expected.get(total_name)
        if isinstance(expected, dict) and total_name is not None
        else None
    )
    return value if type(value) is int and value > 0 else 3


def command_result(
    name: str,
    kind: str,
    roles: dict[str, dict],
) -> dict:
    if name == "second_fresh_rebuild":
        output = "/tmp/a416-l3a1-role11-rebuild.AbC123/" + P.REBUILD_OUTPUT_BASENAME
        argv = [*P.REBUILD_COMMAND_ARGV_PREFIX, output]
    else:
        argv = list(P.FIXED_COMMAND_ARGV[name])

    counts = None
    receipt = None
    stdout = ""
    if name in P.PYTEST_RESULT_TOTAL_NAMES:
        passed = pytest_passes(name)
        counts = {
            "passed": passed,
            "failed": 0,
            "skipped": 0,
            "xfailed": 0,
            "xpassed": 0,
        }
        stdout = f"{passed} passed in 0.01s\n"
    elif name == "role24_machine_verify":
        receipt = verify_receipt(
            P.MACHINE_VERIFY_STATUS, P.MACHINE_SHA256, P.MACHINE_SIZE_BYTES
        )
        stdout = (
            f"machine_freeze_verification={P.MACHINE_VERIFY_STATUS} "
            f"authority={P.VERIFY_AUTHORITY} "
            f"candidate_sha256={P.MACHINE_SHA256} "
            f"size_bytes={P.MACHINE_SIZE_BYTES} promotion_authorized=false\n"
        )
    elif name == "role13_compatibility_verify":
        receipt = verify_receipt(
            P.ROLE13_VERIFY_STATUS, P.ROLE13_SHA256, P.ROLE13_SIZE_BYTES
        )
        stdout = (
            f"s0_compatibility_verification={P.ROLE13_VERIFY_STATUS} "
            f"authority={P.VERIFY_AUTHORITY} "
            f"candidate_sha256={P.ROLE13_SHA256} "
            f"size_bytes={P.ROLE13_SIZE_BYTES} promotion_authorized=false\n"
        )
    elif name == "second_fresh_rebuild":
        source = roles["branch_evaluator_source"]
        binary = roles["branch_evaluator_binary"]
        receipt = {
            "verification_status": P.SECOND_REBUILD_STATUS,
            "authority": P.SECOND_REBUILD_AUTHORITY,
            "source_path": source["path"],
            "source_sha256": source["sha256"],
            "persistent_binary_path": binary["path"],
            "persistent_before_sha256": binary["sha256"],
            "persistent_after_sha256": binary["sha256"],
            "persistent_before_device_id": 101,
            "persistent_before_inode": 202,
            "persistent_after_device_id": 101,
            "persistent_after_inode": 202,
            "persistent_identity_unchanged": True,
            "persistent_overwrite_performed": False,
            "staging_output_sha256": binary["sha256"],
            "staging_output_size_bytes": binary["size_bytes"],
            "staging_output_mode": binary["mode"],
            "staging_output_removed": True,
            "byte_for_byte_equal": True,
            "scientific_evaluator_dispatched": False,
        }
        stdout = P.canonical_json_bytes(receipt).decode("utf-8")

    stdout_raw = stdout.encode("utf-8")
    stderr_raw = b""
    return {
        "name": name,
        "kind": kind,
        "argv": argv,
        "cwd": str(ROOT),
        "environment": dict(P.CLEAN_ENVIRONMENT),
        "return_code": 0,
        "started_at_utc": "2026-08-11T12:00:00Z",
        "wall_duration_ms": 100,
        "stdout_utf8": stdout,
        "stdout_sha256": sha(stdout_raw),
        "stdout_size_bytes": len(stdout_raw),
        "stderr_utf8": "",
        "stderr_sha256": sha(stderr_raw),
        "stderr_size_bytes": 0,
        "pytest_counts": counts,
        "semantic_receipt": receipt,
    }


def valid_record() -> dict:
    entries = role_entries()
    roles = {entry["role"]: entry for entry in entries}
    results = [command_result(name, kind, roles) for name, kind in P.COMMAND_SPECS]
    machine_receipt = copy.deepcopy(results[0]["semantic_receipt"])
    role13_receipt = copy.deepcopy(results[1]["semantic_receipt"])
    rebuild_receipt = copy.deepcopy(results[6]["semantic_receipt"])
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    origin_url = getattr(
        P, "ORIGIN_URL", "git@github.com:maris205/hilbert-polya-structure.git"
    )
    repository_snapshot = {
        "authority_root": str(ROOT),
        "branch": "main",
        "capture_commit_oid": head,
        "capture_tree_oid": tree,
        "origin_url": origin_url,
        "origin_main_oid": head,
        "live_remote_main_oid": head,
        "head_equals_origin_main": True,
        "head_equals_live_remote_main": True,
        "ahead": 0,
        "behind": 0,
        "worktree_clean_before": True,
        "worktree_clean_after": True,
    }
    machine = {
        **roles["machine_freeze"],
        "publication_commit_oid": P.MACHINE_PUBLICATION_COMMIT,
        "producer_path": roles["scheduler"]["path"],
        "producer_sha256": roles["scheduler"]["sha256"],
        "verifier_path": roles["release_builder"]["path"],
        "verifier_sha256": roles["release_builder"]["sha256"],
        "verify_receipt": machine_receipt,
        "promotion_authorized": False,
    }
    role13 = {
        **roles["s0_compatibility"],
        "publication_commit_oid": P.ROLE13_PUBLICATION_COMMIT,
        "producer_path": roles["s0_adapter"]["path"],
        "producer_sha256": roles["s0_adapter"]["sha256"],
        "verify_receipt": role13_receipt,
        "promotion_authorized": False,
    }
    prerequisites = {
        "machine_role10": machine,
        "s0_compatibility_role13": role13,
        "second_fresh_rebuild_replay": {
            "command_result_name": "second_fresh_rebuild",
            "command_result_sha256": sha(P.canonical_json_bytes(results[6])),
            "semantic_receipt": rebuild_receipt,
        },
        "canonical_absence": {
            "prefreeze_review_role12_exists": False,
            "main_freeze_role54_exists": False,
            "canonical_result_root_exists": False,
            "canonical_operational_root_exists": False,
        },
    }
    tools = {
        "producer": {
            "path": "scripts/build_r401_val_l3_a1_prefreeze_tests.py",
            "sha256": "a" * 64,
            "size_bytes": 100,
            "mode": "0644",
            "nlink": 1,
        },
        "independent_checker": {
            "path": "scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py",
            "sha256": "b" * 64,
            "size_bytes": 100,
            "mode": "0644",
            "nlink": 1,
        },
        "focused_test": {
            "path": "tests/test_r401_val_l3_a1_prefreeze_tests.py",
            "sha256": "c" * 64,
            "size_bytes": 100,
            "mode": "0644",
            "nlink": 1,
        },
    }
    return P.build_prefreeze_test_record(
        recorded_at_utc="2026-08-11T12:00:01Z",
        repository_snapshot=repository_snapshot,
        prerequisite_bindings=prerequisites,
        pre_review_input_roles=entries,
        evidence_tool_bindings=tools,
        command_results=results,
    )


def reject(record: dict, pattern: str | None = None) -> None:
    with pytest.raises(P.PrefreezeEvidenceError, match=pattern):
        P.validate_prefreeze_test_record(record)


def test_valid_record_and_exact_top_level_schema() -> None:
    record = valid_record()
    P.validate_prefreeze_test_record(record)
    assert set(record) == P.TOP_LEVEL_KEYS
    assert len(record) == 22
    assert record["component_status"] is None
    assert record["milestone_status"] is None
    assert record["theorem_status"] is None
    assert record["final_status"] is None


def test_ordered_51_roles_matches_frozen_projection() -> None:
    assert len(P.PRE_REVIEW_INPUT_ROLES) == 51
    assert all(role not in {"prefreeze_tests", "prefreeze_review"} for role, _ in P.PRE_REVIEW_INPUT_ROLES)
    assert P.PRE_REVIEW_INPUT_ROLES[9][0] == "machine_freeze"
    assert P.PRE_REVIEW_INPUT_ROLES[10][0] == "s0_compatibility"


def test_canonical_json_known_answer_and_single_lf() -> None:
    assert P.canonical_json_bytes({"b": [True, None], "a": 1}) == b'{"a":1,"b":[true,null]}\n'


@pytest.mark.parametrize(
    "bad",
    [
        {"x": (1, 2)},
        {1: "x"},
        {"x": 1.0},
        {"x": float("nan")},
        {"x": float("inf")},
    ],
)
def test_serializer_rejects_non_plain_json_aliases(bad) -> None:
    with pytest.raises(P.PrefreezeEvidenceError):
        P.canonical_json_bytes(bad)


def test_serializer_rejects_cycle() -> None:
    value: list = []
    value.append(value)
    with pytest.raises(P.PrefreezeEvidenceError, match="cyclic"):
        P.canonical_json_bytes(value)


@pytest.mark.parametrize("field", ["authority", "artifact_status", "claim_boundary"])
def test_authority_literals_are_exact(field: str) -> None:
    record = valid_record()
    record[field] += "_FORGED"
    reject(record)


@pytest.mark.parametrize(
    "field",
    ["scientific_licensing_enabled", "production_authorized", "scientific_dispatch_performed"],
)
def test_authority_booleans_cannot_promote(field: str) -> None:
    record = valid_record()
    record[field] = True
    reject(record)


@pytest.mark.parametrize("field", ["component_status", "milestone_status", "theorem_status", "final_status"])
def test_scientific_statuses_must_remain_null(field: str) -> None:
    record = valid_record()
    record[field] = "PASS_FORGED"
    reject(record)


def test_top_level_extra_and_missing_reject() -> None:
    extra = valid_record()
    extra["status"] = "PASS_FORGED"
    reject(extra, "top-level")
    missing = valid_record()
    del missing["authority"]
    reject(missing, "top-level")


def test_role_order_path_size_and_link_are_strict() -> None:
    for mutation in ("order", "path", "size", "link"):
        record = valid_record()
        entries = record["pre_review_input_roles"]
        if mutation == "order":
            entries[0], entries[1] = entries[1], entries[0]
        elif mutation == "path":
            entries[0]["path"] = entries[1]["path"]
        elif mutation == "size":
            entries[0]["size_bytes"] = 0
        else:
            entries[0]["nlink"] = 2
        reject(record)


def test_machine_and_role13_direct_bindings_cross_check_role_array() -> None:
    for key in ("machine_role10", "s0_compatibility_role13"):
        record = valid_record()
        record["prerequisite_bindings"][key]["sha256"] = "7" * 64
        reject(record)


def test_command_order_and_kind_are_exact() -> None:
    record = valid_record()
    record["command_results"][0], record["command_results"][1] = (
        record["command_results"][1], record["command_results"][0]
    )
    reject(record)
    record = valid_record()
    record["command_results"][2]["kind"] = "PYTEST_FORGED"
    reject(record)


def test_raw_transcript_hash_size_and_nul_are_replayed() -> None:
    for mutation in ("hash", "size", "nul"):
        record = valid_record()
        result = record["command_results"][2]
        if mutation == "hash":
            result["stdout_sha256"] = "0" * 64
        elif mutation == "size":
            result["stdout_size_bytes"] += 1
        else:
            result["stdout_utf8"] += "\x00"
            raw = result["stdout_utf8"].encode()
            result["stdout_size_bytes"] = len(raw)
            result["stdout_sha256"] = sha(raw)
        reject(record)


@pytest.mark.parametrize(
    "summary",
    [
        "3 passed, 1 skipped in 0.01s\n",
        "3 passed, 1 deselected in 0.01s\n",
        "3 passed, 1 error in 0.01s\n",
        "ERROR collecting forged.py\n3 passed in 0.01s\n",
        "FAILED forged.py::test_claim\n3 passed in 0.01s\n",
        "3 passed in 0.01s\n3 passed in 0.01s\n",
        "\x1b[32m3 passed in 0.01s\x1b[0m\n",
    ],
)
def test_pytest_summary_rejects_nonpass_or_ambiguous_categories(summary: str) -> None:
    record = valid_record()
    result = record["command_results"][2]
    result["stdout_utf8"] = summary
    raw = summary.encode()
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    reject(record)


@pytest.mark.parametrize(
    "summary",
    [
        "ERROR collecting forged.py\n3 passed in 0.01s\n",
        "FAILED forged.py::test_claim\n3 passed in 0.01s\n",
    ],
)
def test_independent_checker_rejects_hidden_pytest_failure_tokens(summary: str) -> None:
    record = valid_record()
    result = record["command_results"][2]
    result["stdout_utf8"] = summary
    raw = summary.encode("utf-8")
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    with pytest.raises(C.PrefreezeCheckError):
        C.validate_record(record)


@pytest.mark.parametrize(
    "prefix",
    [
        "fail\n", "xfail\n", "xpass\n", "\t", "\x7f",
        "\u0085", "\u2028", "\u2029",
    ],
)
def test_producer_checker_reject_the_same_pytest_token_and_control_domain(
    prefix: str,
) -> None:
    record = valid_record()
    result = record["command_results"][2]
    result["stdout_utf8"] = prefix + result["stdout_utf8"]
    raw = result["stdout_utf8"].encode("utf-8")
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    with pytest.raises(P.PrefreezeEvidenceError):
        P.validate_prefreeze_test_record(record)
    with pytest.raises(C.PrefreezeCheckError):
        C.validate_record(record)


@pytest.mark.parametrize("prefix", ["_failed_\n", "failure_count\n"])
def test_producer_checker_allow_the_same_identifier_internal_tokens(prefix: str) -> None:
    record = valid_record()
    result = record["command_results"][2]
    result["stdout_utf8"] = prefix + result["stdout_utf8"]
    raw = result["stdout_utf8"].encode("utf-8")
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    P.validate_prefreeze_test_record(record)
    C.validate_record(record)


def test_coherent_forged_pytest_count_and_total_reject() -> None:
    record = valid_record()
    result = record["command_results"][2]
    result["stdout_utf8"] = "2 passed in 0.01s\n"
    raw = result["stdout_utf8"].encode()
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    result["pytest_counts"]["passed"] = 2
    record["test_totals"]["prefreeze_focused"]["passed"] = 2
    expected = getattr(P, "EXPECTED_TEST_PASSED", None)
    if not isinstance(expected, dict) or expected.get("prefreeze_focused") is None:
        # Before the final totals are mechanically frozen, the capture CLI is
        # fail-closed and only the structural pure builder is available.
        P.validate_prefreeze_test_record(record)
    else:
        reject(record)


def test_verify_transcripts_must_match_semantic_receipts() -> None:
    record = valid_record()
    result = record["command_results"][0]
    result["semantic_receipt"]["promotion_authorized"] = True
    reject(record)
    record = valid_record()
    result = record["command_results"][1]
    result["stdout_utf8"] = result["stdout_utf8"].replace("false", "true")
    raw = result["stdout_utf8"].encode()
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    reject(record)


def test_git_diff_check_must_have_empty_transcript() -> None:
    record = valid_record()
    result = record["command_results"][5]
    result["stdout_utf8"] = "clean\n"
    raw = result["stdout_utf8"].encode()
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    reject(record)


def test_second_rebuild_receipt_binds_binary_and_persistent_inode() -> None:
    for field, value in (
        ("staging_output_sha256", "9" * 64),
        ("persistent_after_inode", 203),
        ("persistent_overwrite_performed", True),
        ("staging_output_removed", False),
        ("scientific_evaluator_dispatched", True),
    ):
        record = valid_record()
        receipt = record["command_results"][6]["semantic_receipt"]
        receipt[field] = value
        result = record["command_results"][6]
        result["stdout_utf8"] = P.canonical_json_bytes(receipt).decode()
        raw = result["stdout_utf8"].encode()
        result["stdout_size_bytes"] = len(raw)
        result["stdout_sha256"] = sha(raw)
        record["prerequisite_bindings"]["second_fresh_rebuild_replay"]["semantic_receipt"] = copy.deepcopy(receipt)
        record["prerequisite_bindings"]["second_fresh_rebuild_replay"]["command_result_sha256"] = sha(P.canonical_json_bytes(result))
        reject(record)


def test_repository_snapshot_and_canonical_absence_are_exact() -> None:
    record = valid_record()
    record["repository_snapshot"]["origin_main_oid"] = "1" * 40
    reject(record)
    record = valid_record()
    record["prerequisite_bindings"]["canonical_absence"]["main_freeze_role54_exists"] = True
    reject(record)


def test_covered_gates_are_ordered_and_exact() -> None:
    record = valid_record()
    record["covered_gates"].reverse()
    reject(record)


def test_fixed_pytest_commands_disable_cache_and_color() -> None:
    assert P.COMMAND_TIMEOUT_SECONDS == C.COMMAND_TIMEOUT_SECONDS == 600
    assert P.MAX_COMMAND_WALL_DURATION_MS == C.MAX_COMMAND_WALL_DURATION_MS == 603000
    for name in ("prefreeze_focused_pytest", "l3_a1_modules_pytest", "paper02_full_pytest"):
        argv = P.FIXED_COMMAND_ARGV[name]
        assert ("-p", "no:cacheprovider") == argv[4:6]
        assert "--color=no" in argv
    assert P.CLEAN_ENVIRONMENT["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] == "1"
    long_summary = "621 passed in 170.57s (0:02:50)\n"
    expected = {"passed": 621, "failed": 0, "skipped": 0, "xfailed": 0, "xpassed": 0}
    assert P._parse_pytest_counts(long_summary, "long pytest summary") == expected
    assert C.parse_pytest(long_summary, "long pytest summary") == expected
    rounded_without_suffix = "621 passed in 60.00s\n"
    assert P._parse_pytest_counts(rounded_without_suffix, "rounded pytest summary") == expected
    assert C.parse_pytest(rounded_without_suffix, "rounded pytest summary") == expected
    rounded_long_suffix = "621 passed in 171.00s (0:02:50)\n"
    assert P._parse_pytest_counts(rounded_long_suffix, "rounded long pytest summary") == expected
    assert C.parse_pytest(rounded_long_suffix, "rounded long pytest summary") == expected
    for malformed in (
        "621 passed in 170.57s\n",
        "621 passed in 170.57s (0:02:49)\n",
        "3 passed in 0.01s (0:00:00)\n",
        "621 passed in 600.01s (0:10:00)\n",
        "621 passed in 601.00s (0:10:01)\n",
        "621 passed in 3600.00s (1:00:00)\n",
        "0621 passed in 170.57s (0:02:50)\n",
        "621 passed in 0170.57s (0:02:50)\n",
        "621 passed in 170.57s (00:02:50)\n",
        f"{'9' * 5000} passed in 0.01s\n",
    ):
        with pytest.raises(P.PrefreezeEvidenceError):
            P._parse_pytest_counts(malformed, "malformed pytest summary")
        with pytest.raises(C.PrefreezeCheckError):
            C.parse_pytest(malformed, "malformed pytest summary")
    for c1_control in ("\u0080", "\u009b", "\u009d", "\u009f"):
        poisoned = c1_control + "621 passed in 0.01s\n"
        with pytest.raises(P.PrefreezeEvidenceError):
            P._parse_pytest_counts(poisoned, "C1 pytest summary")
        with pytest.raises(C.PrefreezeCheckError):
            C.parse_pytest(poisoned, "C1 pytest summary")
    record = valid_record()
    record["command_results"][2]["wall_duration_ms"] = 603001
    record["test_totals"]["prefreeze_focused"]["wall_duration_ms"] = 603001
    with pytest.raises(P.PrefreezeEvidenceError):
        P.validate_prefreeze_test_record(record)
    with pytest.raises(C.PrefreezeCheckError):
        C.validate_record(record)
    record = valid_record()
    result = record["command_results"][2]
    result["stdout_utf8"] = "100 passed in 0.11s\n"
    raw = result["stdout_utf8"].encode("utf-8")
    result["stdout_size_bytes"] = len(raw)
    result["stdout_sha256"] = sha(raw)
    with pytest.raises(P.PrefreezeEvidenceError):
        P.validate_prefreeze_test_record(record)
    with pytest.raises(C.PrefreezeCheckError):
        C.validate_record(record)


def test_independent_checker_source_has_no_producer_import_or_subprocess() -> None:
    source = CHECKER_PATH.read_text(encoding="utf-8")
    assert "import build_r401_val_l3_a1_prefreeze_tests" not in source
    assert "from build_r401_val_l3_a1_prefreeze_tests" not in source
    assert "import subprocess" not in source
    assert "subprocess." not in source


def test_producer_checker_schema_constants_match_exactly() -> None:
    names = (
        "TOP_LEVEL_KEYS",
        "HELD_OUT_POLICY_KEYS",
        "REPOSITORY_SNAPSHOT_KEYS",
        "PREREQUISITE_BINDING_KEYS",
        "CANONICAL_ABSENCE_KEYS",
        "ROLE_ENTRY_KEYS",
        "FILE_BINDING_KEYS",
        "EVIDENCE_TOOL_BINDING_KEYS",
        "MACHINE_BINDING_KEYS",
        "ROLE13_BINDING_KEYS",
        "VERIFY_RECEIPT_KEYS",
        "SECOND_REBUILD_REPLAY_KEYS",
        "SECOND_REBUILD_RECEIPT_KEYS",
        "COMMAND_RESULT_KEYS",
        "PYTEST_COUNT_KEYS",
        "TEST_TOTAL_KEYS",
        "TEST_TOTALS_KEYS",
        "PRE_REVIEW_INPUT_ROLES",
        "COMMAND_SPECS",
        "CLEAN_ENVIRONMENT",
        "COVERED_GATES",
        "CLAIM_BOUNDARY",
        "MACHINE_SHA256",
        "MACHINE_SIZE_BYTES",
        "ROLE13_SHA256",
        "ROLE13_SIZE_BYTES",
    )
    for name in names:
        assert getattr(C, name) == getattr(P, name), name
    assert C.PYTEST_TO_TOTAL == P.PYTEST_RESULT_TOTAL_NAMES
    assert C.EXPECTED_TEST_PASSED == P.EXPECTED_TEST_PASSED


def test_independent_checker_accepts_the_same_valid_internal_record() -> None:
    C.validate_record(copy.deepcopy(valid_record()))


def test_producer_checker_utc_domain_matches_beyond_current_century() -> None:
    record = valid_record()
    record["recorded_at_utc"] = "2100-01-01T00:00:01Z"
    for result in record["command_results"]:
        result["started_at_utc"] = "2100-01-01T00:00:00Z"
    record["prerequisite_bindings"]["second_fresh_rebuild_replay"][
        "command_result_sha256"
    ] = sha(P.canonical_json_bytes(record["command_results"][6]))
    P.validate_prefreeze_test_record(record)
    C.validate_record(record)


@pytest.mark.parametrize(
    "mutator",
    [
        lambda r: r["held_out_policy"].__setitem__("scientific_evaluator_dispatch_count", 1),
        lambda r: r["repository_snapshot"].__setitem__("origin_main_oid", "1" * 40),
        lambda r: r["command_results"][2].__setitem__("stdout_sha256", "0" * 64),
        lambda r: r["command_results"][2]["pytest_counts"].__setitem__("passed", 4),
        lambda r: r["test_totals"]["prefreeze_focused"].__setitem__("passed", 4),
        lambda r: r["prerequisite_bindings"]["machine_role10"].__setitem__("promotion_authorized", True),
        lambda r: r["prerequisite_bindings"]["canonical_absence"].__setitem__("main_freeze_role54_exists", True),
        lambda r: r.__setitem__("scientific_dispatch_performed", True),
    ],
)
def test_independent_checker_rejects_nested_authority_mutations(mutator) -> None:
    record = valid_record()
    mutator(record)
    with pytest.raises(C.PrefreezeCheckError):
        C.validate_record(record)


def test_bounded_command_fixes_umask_and_restores_subreaper() -> None:
    before = P._child_subreaper_state()
    code = "import os; old=os.umask(0); os.umask(old); print(f'{old:03o}')"
    result = P.run_bounded_command((P.PYTHON, "-c", code), timeout_seconds=10)
    assert result.return_code == 0
    assert result.stdout == b"022\n"
    assert result.stderr == b""
    assert P._child_subreaper_state() is before


def test_bounded_command_caps_output_and_reaps_process_group() -> None:
    before = P._child_subreaper_state()
    with pytest.raises(P.PrefreezeEvidenceError, match="cap exceeded"):
        P.run_bounded_command(
            (P.PYTHON, "-c", "import sys; sys.stdout.write('x'*4096)"),
            timeout_seconds=10,
            stdout_cap=128,
        )
    assert P._child_subreaper_state() is before


def test_bounded_command_kills_pipe_holding_descendant(tmp_path: Path) -> None:
    pid_path = tmp_path / "descendant.pid"
    code = (
        "import os,signal,time,pathlib; "
        "child=os.fork(); "
        f"pathlib.Path({str(pid_path)!r}).write_text(str(child)) if child else None; "
        "os._exit(0) if child else "
        "(signal.signal(signal.SIGTERM, signal.SIG_IGN), time.sleep(30))"
    )
    before = P._child_subreaper_state()
    with pytest.raises(P.PrefreezeEvidenceError, match="retained output pipes"):
        P.run_bounded_command((P.PYTHON, "-c", code), timeout_seconds=10)
    assert P._child_subreaper_state() is before
    descendant = int(pid_path.read_text())
    deadline = time.monotonic() + 2
    while time.monotonic() < deadline:
        try:
            os.kill(descendant, 0)
        except ProcessLookupError:
            break
        time.sleep(0.02)
    else:
        pytest.fail(f"descendant {descendant} survived bounded-command cleanup")


def test_bounded_command_timeout_kills_group_and_restores_state() -> None:
    before = P._child_subreaper_state()
    with pytest.raises(P.PrefreezeEvidenceError, match="timeout"):
        P.run_bounded_command(
            (P.PYTHON, "-c", "import time; time.sleep(30)"),
            timeout_seconds=1,
        )
    assert P._child_subreaper_state() is before


def test_independent_s0_verify_cli_is_exact_and_non_authorizing() -> None:
    completed = subprocess.run(
        [
            P.PYTHON,
            str(CHECKER_PATH),
            "--verify-s0-compatibility",
            str(P.ROLE13_CANONICAL),
        ],
        cwd=ROOT,
        env=dict(P.CLEAN_ENVIRONMENT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert completed.returncode == 0
    assert completed.stderr == b""
    assert completed.stdout == (
        f"s0_compatibility_verification={P.ROLE13_VERIFY_STATUS} "
        f"authority={P.VERIFY_AUTHORITY} candidate_sha256={P.ROLE13_SHA256} "
        f"size_bytes={P.ROLE13_SIZE_BYTES} promotion_authorized=false\n"
    ).encode()


def test_checker_temp_candidate_reader_requires_0600_single_link() -> None:
    parent = owned_tmp_dir("a416-role11-checker-reader.")
    try:
        candidate = parent / "candidate.json"
        candidate.write_bytes(b"{}\n")
        candidate.chmod(0o600)
        payload, raw = C.read_candidate(candidate)
        assert payload == {}
        assert raw == b"{}\n"
        candidate.chmod(0o644)
        with pytest.raises(C.PrefreezeCheckError, match="mode"):
            C.read_candidate(candidate)
    finally:
        remove_owned_tmp_dir(parent)


def test_checker_candidate_reader_rejects_hardlink_symlink_and_fifo() -> None:
    hard_parent = owned_tmp_dir("a416-role11-checker-hardlink.")
    try:
        source = hard_parent / "source.json"
        source.write_bytes(b"{}\n")
        source.chmod(0o600)
        os.link(source, hard_parent / "hardlink.json")
        with pytest.raises(C.PrefreezeCheckError):
            C.read_candidate(source)
    finally:
        remove_owned_tmp_dir(hard_parent)

    target_parent = owned_tmp_dir("a416-role11-checker-target.")
    symlink_parent = owned_tmp_dir("a416-role11-checker-symlink.")
    try:
        target = target_parent / "target.json"
        target.write_bytes(b"{}\n")
        target.chmod(0o600)
        symlink = symlink_parent / "candidate.json"
        symlink.symlink_to(target)
        with pytest.raises((C.PrefreezeCheckError, OSError)):
            C.read_candidate(symlink)
    finally:
        remove_owned_tmp_dir(symlink_parent)
        remove_owned_tmp_dir(target_parent)

    fifo_parent = owned_tmp_dir("a416-role11-checker-fifo.")
    try:
        fifo = fifo_parent / "candidate.fifo"
        os.mkfifo(fifo, 0o600)
        started = time.monotonic()
        with pytest.raises(C.PrefreezeCheckError, match="not regular"):
            C.read_candidate(fifo)
        assert time.monotonic() - started < 1
    finally:
        remove_owned_tmp_dir(fifo_parent)


def test_producer_candidate_writer_requires_one_empty_owned_0700_parent() -> None:
    parent = Path(tempfile.mkdtemp(prefix="a416-role11-candidate.", dir="/tmp"))
    output = parent / "candidate.json"
    try:
        captured = P._write_exclusive_candidate(output, b"{}\n")
        assert output.read_bytes() == b"{}\n"
        assert output.stat().st_mode & 0o777 == 0o600
        assert output.stat().st_nlink == 1
        P._remove_owned_candidate(output, captured)
        assert not output.exists()

        foreign = parent / "foreign"
        foreign.write_bytes(b"x")
        with pytest.raises(P.PrefreezeEvidenceError, match="empty owned mode-0700"):
            P._write_exclusive_candidate(output, b"{}\n")
        foreign.unlink()
    finally:
        if output.exists():
            output.unlink()
        for entry in list(parent.iterdir()):
            entry.unlink()
        parent.rmdir()

    with pytest.raises(P.PrefreezeEvidenceError, match="one owned directory"):
        P._candidate_output_path("/tmp/candidate.json")


def test_capture_replays_candidate_after_long_terminal_live_replay(monkeypatch) -> None:
    parent = owned_tmp_dir("a416-role11-capture-terminal.")
    output = parent / "candidate.json"
    monkeypatch.setattr(
        P,
        "EXPECTED_TEST_PASSED",
        {"prefreeze_focused": 3, "l3_a1_modules": 3, "paper02_full": 3},
    )
    template = valid_record()
    monkeypatch.setattr(
        P, "capture_repository_snapshot",
        lambda: copy.deepcopy(template["repository_snapshot"]),
    )
    monkeypatch.setattr(
        P, "capture_pre_review_input_roles",
        lambda: copy.deepcopy(template["pre_review_input_roles"]),
    )
    monkeypatch.setattr(
        P, "capture_evidence_tool_bindings",
        lambda: copy.deepcopy(template["evidence_tool_bindings"]),
    )
    monkeypatch.setattr(
        P, "_run_fixed_evidence_commands",
        lambda _roles: copy.deepcopy(template["command_results"]),
    )
    monkeypatch.setattr(
        P, "_prerequisite_bindings",
        lambda _roles, _results: copy.deepcopy(template["prerequisite_bindings"]),
    )
    monkeypatch.setattr(P, "assert_prefreeze_namespaces_absent", lambda: None)
    monkeypatch.setattr(P, "replay_pre_review_input_roles", lambda _roles: None)
    monkeypatch.setattr(P, "replay_evidence_tool_bindings", lambda _tools: None)
    monkeypatch.setattr(P, "replay_repository_snapshot", lambda _snapshot: None)
    monkeypatch.setattr(P, "_utc_now", lambda: "2026-08-11T12:00:01Z")

    def replace_same_bytes(phase: str) -> None:
        assert phase == "BEFORE_FINAL_CANDIDATE_REPLAY"
        raw = output.read_bytes()
        replacement = parent / "replacement.json"
        replacement.write_bytes(raw)
        replacement.chmod(0o600)
        os.replace(replacement, output)

    monkeypatch.setattr(P, "_capture_fault_hook", replace_same_bytes)
    try:
        with pytest.raises(P.PrefreezeEvidenceError):
            P.capture_prefreeze_test_candidate(str(output))
        # The replacement inode is not producer-owned and must not be deleted.
        assert output.exists()
        assert output.stat().st_mode & 0o777 == 0o600
    finally:
        remove_owned_tmp_dir(parent)


def publication_fixture(monkeypatch, tmp_path: Path) -> dict:
    authority = tmp_path / "authority"
    destination = authority / P.CANONICAL_RELATIVE
    destination.parent.mkdir(parents=True)
    candidate_parent = owned_tmp_dir("a416-role11-publication-candidate.")
    candidate = candidate_parent / "candidate.json"

    monkeypatch.setattr(P, "ROOT", ROOT)
    monkeypatch.setattr(
        P,
        "EXPECTED_TEST_PASSED",
        {"prefreeze_focused": 3, "l3_a1_modules": 3, "paper02_full": 3},
    )
    record = valid_record()
    monkeypatch.setattr(P, "ROOT", authority)
    record["repository_snapshot"]["authority_root"] = str(authority)
    for result in record["command_results"]:
        result["cwd"] = str(authority)
    record["prerequisite_bindings"]["second_fresh_rebuild_replay"][
        "command_result_sha256"
    ] = sha(P.canonical_json_bytes(record["command_results"][6]))
    P.validate_prefreeze_test_record(record)
    raw = P.canonical_json_bytes(record)
    candidate.write_bytes(raw)
    candidate.chmod(0o600)

    verifier_calls: list[tuple[Path, str, int]] = []

    def verify(path: Path, digest: str, size: int) -> None:
        verifier_calls.append((path, digest, size))

    monkeypatch.setattr(P, "_verify_candidate_independently", verify)
    monkeypatch.setattr(P, "_replay_live_publication_inputs", lambda *a, **k: None)
    monkeypatch.setattr(P, "assert_prefreeze_namespaces_absent", lambda: None)
    return {
        "authority": authority,
        "candidate_parent": candidate_parent,
        "candidate": candidate,
        "destination": destination,
        "raw": raw,
        "digest": sha(raw),
        "verifier_calls": verifier_calls,
    }


def cleanup_publication_fixture(fixture: dict) -> None:
    remove_owned_tmp_dir(fixture["candidate_parent"])


def publication_worker(queue, candidate: str, digest: str, authority: str) -> None:
    try:
        receipt = P.publish_prefreeze_test_record(
            candidate_value=candidate,
            expected_sha256=digest,
            authority_root_value=authority,
        )
    except BaseException as error:
        queue.put(("error", type(error).__name__, str(error)))
    else:
        queue.put(("success", receipt["prefreeze_tests_sha256"]))


def test_role11_publication_success_receipt_is_closed_and_write_once(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    try:
        receipt = P.publish_prefreeze_test_record(
            candidate_value=str(fixture["candidate"]),
            expected_sha256=fixture["digest"],
            authority_root_value=str(fixture["authority"]),
        )
        assert set(receipt) == P.PUBLICATION_RECEIPT_KEYS
        assert receipt["artifact_status"] == P.PUBLICATION_STATUS
        assert receipt["authority"] == "PREFREEZE_TEST_PRODUCER_PUBLICATION_ONLY"
        assert receipt["independent_verification_performed"] is True
        assert receipt["promotion_authorized"] is False
        assert receipt["scientific_licensing_enabled"] is False
        assert receipt["production_authorized"] is False
        assert receipt["scientific_dispatch_performed"] is False
        assert all(
            receipt[key] is None
            for key in ("component_status", "milestone_status", "theorem_status", "final_status")
        )
        assert fixture["destination"].read_bytes() == fixture["raw"]
        assert fixture["destination"].stat().st_mode & 0o777 == 0o644
        assert fixture["destination"].stat().st_nlink == 1
        assert fixture["candidate"].read_bytes() == fixture["raw"]
        assert fixture["candidate"].stat().st_mode & 0o777 == 0o600
        assert fixture["verifier_calls"] == [
            (fixture["candidate"], fixture["digest"], len(fixture["raw"]))
        ]
        with pytest.raises(P.PrefreezeEvidenceError, match="already exists"):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
    finally:
        cleanup_publication_fixture(fixture)


@pytest.mark.parametrize("leaf_kind", ["identical", "different", "directory", "symlink", "fifo"])
def test_role11_publication_rejects_every_existing_destination(
    monkeypatch, tmp_path: Path, leaf_kind: str,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    destination = fixture["destination"]
    try:
        if leaf_kind == "identical":
            destination.write_bytes(fixture["raw"])
        elif leaf_kind == "different":
            destination.write_bytes(b"different")
        elif leaf_kind == "directory":
            destination.mkdir()
        elif leaf_kind == "symlink":
            destination.symlink_to(fixture["candidate"])
        else:
            os.mkfifo(destination, 0o600)
        with pytest.raises(P.PrefreezeEvidenceError, match="already exists"):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
    finally:
        cleanup_publication_fixture(fixture)


@pytest.mark.parametrize(
    "phase",
    [
        "AFTER_STAGE_WRITE",
        "AFTER_STAGE_FILE_FSYNC",
        "AFTER_STAGING_PARENT_FSYNC",
        "BEFORE_TERMINAL_REPLAY",
        "BEFORE_RENAME",
    ],
)
def test_role11_publication_prerename_failpoints_clean_owned_stage(
    monkeypatch, tmp_path: Path, phase: str,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)

    def fail(current: str) -> None:
        if current == phase:
            raise RuntimeError("injected pre-rename failure")

    monkeypatch.setattr(P, "_publication_fault_hook", fail)
    try:
        with pytest.raises(RuntimeError, match="injected pre-rename"):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert not fixture["destination"].exists()
        assert not list(
            fixture["destination"].parent.glob(P.PUBLICATION_STAGE_PREFIX + "*")
        )
    finally:
        cleanup_publication_fixture(fixture)


@pytest.mark.parametrize(
    "phase",
    [
        "AFTER_RENAME",
        "AFTER_DESTINATION_FSYNC",
        "AFTER_PUBLICATION_PARENT_FSYNC",
        "AFTER_POSTPUBLICATION_REPLAY",
    ],
)
def test_role11_publication_postrename_failpoints_never_roll_back(
    monkeypatch, tmp_path: Path, phase: str,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)

    def fail(current: str) -> None:
        if current == phase:
            raise RuntimeError("injected post-rename failure")

    monkeypatch.setattr(P, "_publication_fault_hook", fail)
    try:
        with pytest.raises(RuntimeError, match="injected post-rename"):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert fixture["destination"].read_bytes() == fixture["raw"]
        assert fixture["destination"].stat().st_mode & 0o777 == 0o644
        assert not list(
            fixture["destination"].parent.glob(P.PUBLICATION_STAGE_PREFIX + "*")
        )
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_replays_canonical_after_final_hook(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)

    def mutate_without_raising(current: str) -> None:
        if current == "AFTER_POSTPUBLICATION_REPLAY":
            replacement = fixture["destination"].parent / "post-hook-replacement"
            replacement.write_bytes(b"post-hook mutation")
            replacement.chmod(0o644)
            os.replace(replacement, fixture["destination"])

    monkeypatch.setattr(P, "_publication_fault_hook", mutate_without_raising)
    try:
        with pytest.raises(P.PrefreezeEvidenceError):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        # Rename already happened: failure must be reported, never "repaired"
        # by rolling the write-once destination back or overwriting it.
        assert fixture["destination"].read_bytes() == b"post-hook mutation"
        assert fixture["candidate"].read_bytes() == fixture["raw"]
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_rejects_same_byte_candidate_inode_swap(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)

    def swap(current: str) -> None:
        if current != "BEFORE_RENAME":
            return
        replacement = fixture["candidate_parent"] / "replacement.json"
        replacement.write_bytes(fixture["raw"])
        replacement.chmod(0o600)
        os.replace(replacement, fixture["candidate"])

    monkeypatch.setattr(P, "_publication_fault_hook", swap)
    try:
        with pytest.raises(
            P.PrefreezeEvidenceError,
            match="candidate parent changed|inode or bytes changed",
        ):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert not fixture["destination"].exists()
        assert not list(
            fixture["destination"].parent.glob(P.PUBLICATION_STAGE_PREFIX + "*")
        )
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_rejects_terminal_live_input_drift(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    calls = 0

    def replay(*_args, **_kwargs) -> None:
        nonlocal calls
        calls += 1
        if calls == 3:
            raise P.PrefreezeEvidenceError("injected live input drift")

    monkeypatch.setattr(P, "_replay_live_publication_inputs", replay)
    try:
        with pytest.raises(P.PrefreezeEvidenceError, match="live input drift"):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert calls == 3
        assert not fixture["destination"].exists()
        assert not list(
            fixture["destination"].parent.glob(P.PUBLICATION_STAGE_PREFIX + "*")
        )
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_stage_collision_preserves_foreign_entry(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    names = iter(
        [P.PUBLICATION_STAGE_PREFIX + "0" * 32, P.PUBLICATION_STAGE_PREFIX + "1" * 32]
    )
    foreign = fixture["destination"].parent / (P.PUBLICATION_STAGE_PREFIX + "0" * 32)
    foreign.write_bytes(b"foreign")
    monkeypatch.setattr(P, "_publication_stage_name", lambda: next(names))
    try:
        P.publish_prefreeze_test_record(
            candidate_value=str(fixture["candidate"]),
            expected_sha256=fixture["digest"],
            authority_root_value=str(fixture["authority"]),
        )
        assert foreign.read_bytes() == b"foreign"
        assert fixture["destination"].read_bytes() == fixture["raw"]
        assert not (fixture["destination"].parent / (P.PUBLICATION_STAGE_PREFIX + "1" * 32)).exists()
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_cleanup_refuses_replaced_stage_inode(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    replaced: list[Path] = []

    def replace_stage(current: str) -> None:
        if current != "AFTER_STAGE_WRITE":
            return
        stages = list(
            fixture["destination"].parent.glob(P.PUBLICATION_STAGE_PREFIX + "*")
        )
        assert len(stages) == 1
        stage = stages[0]
        stage.unlink()
        stage.write_bytes(b"foreign replacement")
        replaced.append(stage)
        raise RuntimeError("injected replaced stage")

    monkeypatch.setattr(P, "_publication_fault_hook", replace_stage)
    try:
        with pytest.raises(P.PrefreezeEvidenceError, match="replaced publication stage"):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert len(replaced) == 1
        assert replaced[0].read_bytes() == b"foreign replacement"
        assert not fixture["destination"].exists()
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_detects_prerename_parent_swap(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    original_parent = fixture["destination"].parent
    moved_parent = original_parent.with_name("route_a_wave_trace.pinned-old")

    def swap_parent(current: str) -> None:
        if current != "BEFORE_RENAME":
            return
        original_parent.rename(moved_parent)
        original_parent.mkdir()

    monkeypatch.setattr(P, "_publication_fault_hook", swap_parent)
    try:
        with pytest.raises(P.PrefreezeEvidenceError):
            P.publish_prefreeze_test_record(
                candidate_value=str(fixture["candidate"]),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert not fixture["destination"].exists()
        assert not list(moved_parent.glob(P.PUBLICATION_STAGE_PREFIX + "*"))
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_two_processes_have_exactly_one_winner(
    monkeypatch, tmp_path: Path,
) -> None:
    context = multiprocessing.get_context("fork")
    for round_index in range(12):
        fixture = publication_fixture(monkeypatch, tmp_path / f"round-{round_index:02d}")
        queue = context.Queue()
        processes = [
            context.Process(
                target=publication_worker,
                args=(
                    queue,
                    str(fixture["candidate"]),
                    fixture["digest"],
                    str(fixture["authority"]),
                ),
            )
            for _ in range(2)
        ]
        try:
            for process in processes:
                process.start()
            for process in processes:
                process.join(10)
                assert process.exitcode == 0
            outcomes = [queue.get(timeout=2), queue.get(timeout=2)]
            assert [item[0] for item in outcomes].count("success") == 1
            assert [item[0] for item in outcomes].count("error") == 1
            assert fixture["destination"].read_bytes() == fixture["raw"]
            assert not list(
                fixture["destination"].parent.glob(P.PUBLICATION_STAGE_PREFIX + "*")
            )
        finally:
            for process in processes:
                if process.is_alive():
                    process.terminate()
                    process.join(2)
            queue.close()
            cleanup_publication_fixture(fixture)


@pytest.mark.parametrize("mutation", ["mode", "hardlink", "symlink", "fifo", "oversize"])
def test_role11_publication_candidate_preopen_contract_fails_fast(
    monkeypatch, tmp_path: Path, mutation: str,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    extra: Path | None = None
    try:
        candidate = fixture["candidate"]
        if mutation == "mode":
            candidate.chmod(0o644)
        elif mutation == "hardlink":
            extra = fixture["candidate_parent"] / "hardlink.json"
            os.link(candidate, extra)
        elif mutation == "symlink":
            target_parent = tmp_path / "symlink-target"
            target_parent.mkdir()
            target = target_parent / "target.json"
            target.write_bytes(fixture["raw"])
            candidate.unlink()
            candidate.symlink_to(target)
        elif mutation == "fifo":
            candidate.unlink()
            os.mkfifo(candidate, 0o600)
        else:
            candidate.unlink()
            with candidate.open("wb") as stream:
                stream.truncate(P.MAX_CANDIDATE_BYTES + 1)
            candidate.chmod(0o600)
        started = time.monotonic()
        with pytest.raises((P.PrefreezeEvidenceError, OSError)):
            P.publish_prefreeze_test_record(
                candidate_value=str(candidate),
                expected_sha256=fixture["digest"],
                authority_root_value=str(fixture["authority"]),
            )
        assert time.monotonic() - started < 1
        assert not fixture["destination"].exists()
    finally:
        if extra is not None and extra.exists():
            extra.unlink()
        cleanup_publication_fixture(fixture)


def test_role11_publication_rejects_path_hash_and_authority_aliases(
    monkeypatch, tmp_path: Path,
) -> None:
    fixture = publication_fixture(monkeypatch, tmp_path)
    try:
        cases = [
            (str(fixture["candidate"]), fixture["digest"].upper(), str(fixture["authority"])),
            (str(fixture["candidate"]), "0" * 64, str(fixture["authority"])),
            ("relative.json", fixture["digest"], str(fixture["authority"])),
            (str(fixture["candidate"]), fixture["digest"], str(tmp_path / "other")),
        ]
        for candidate, digest, authority in cases:
            with pytest.raises(P.PrefreezeEvidenceError):
                P.publish_prefreeze_test_record(
                    candidate_value=candidate,
                    expected_sha256=digest,
                    authority_root_value=authority,
                )
        assert not fixture["destination"].exists()
    finally:
        cleanup_publication_fixture(fixture)


def test_role11_publication_cli_exact_xor_and_compact_receipt(
    monkeypatch, capsys,
) -> None:
    receipt = {key: None for key in P.PUBLICATION_RECEIPT_KEYS}
    receipt.update(
        schema_version=P.SCHEMA_VERSION,
        protocol_id=P.PROTOCOL_ID,
        artifact_role="PREFREEZE_TEST_PUBLICATION_RECEIPT",
        artifact_status=P.PUBLICATION_STATUS,
        authority=P.PUBLICATION_AUTHORITY,
        candidate_path="/tmp/a416-role11-candidate.AbC123/candidate.json",
        canonical_path=str(P.ROOT / P.CANONICAL_RELATIVE),
        prefreeze_tests_sha256="1" * 64,
        size_bytes=123,
        mode="0644",
        nlink=1,
        serializer=P.SERIALIZER,
        publication_method=P.PUBLICATION_METHOD,
        independent_verification_status=P.PREFREEZE_VERIFY_STATUS,
        independent_verification_performed=True,
        independent_verifier_path="scripts/check_r401_val_l3_a1_prefreeze_tests_independent.py",
        independent_verifier_sha256="2" * 64,
        promotion_authorized=False,
        scientific_licensing_enabled=False,
        production_authorized=False,
        scientific_dispatch_performed=False,
    )
    calls: list[tuple[str, str, str]] = []

    def publish(*, candidate_value: str, expected_sha256: str, authority_root_value: str):
        calls.append((candidate_value, expected_sha256, authority_root_value))
        return receipt

    monkeypatch.setattr(P, "publish_prefreeze_test_record", publish)
    argv = [
        "--publish-prefreeze-tests",
        "--candidate", receipt["candidate_path"],
        "--expected-sha256", receipt["prefreeze_tests_sha256"],
        "--authority-root", str(P.ROOT),
    ]
    assert P.main(argv) == 0
    captured = capsys.readouterr()
    assert captured.out.encode("utf-8") == P.canonical_json_bytes(receipt)
    assert captured.err == ""
    assert calls == [
        (receipt["candidate_path"], receipt["prefreeze_tests_sha256"], str(P.ROOT))
    ]

    invalid = [
        ["--publish-prefreeze-tests"],
        ["--capture-prefreeze-tests", "--publish-prefreeze-tests"],
        ["--publish-prefreeze-tests", "--candidate", receipt["candidate_path"]],
        [
            "--publish-prefreeze-tests", "--candidate", receipt["candidate_path"],
            "--expected-sha256", "1" * 64, "--authority-root", str(P.ROOT),
            "--output", "/tmp/forbidden",
        ],
    ]
    for bad_argv in invalid:
        assert P.main(bad_argv) == 1
        bad = capsys.readouterr()
        assert bad.out == ""
        assert bad.err.startswith("ERROR: PrefreezeEvidenceError:")
