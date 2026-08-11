from __future__ import annotations

import ast
import copy
import importlib.util
import json
import math
import os
import stat
import sys
import tempfile
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_v2_static_independent.py"
S0_PROOF = ROOT / "results/r401_val_l3_phase_tube_smoke/proof_128_S000.json"

MAIN_FREEZE_KEYS = (
    "schema_version", "protocol_id", "artifact_role", "status", "authority",
    "scientific_licensing_enabled", "matrix", "matrix_id", "input_roles",
    "machine_freeze_sha256", "prefreeze_review", "serializers", "scheduler",
    "limits", "status_tables", "evaluators", "checkers", "archive_layout",
    "machine_requirements", "failure_policy", "execution_policy",
    "claim_boundary", "component_status", "milestone_status", "theorem_status",
    "final_status",
)
FORMAL_CHECKER_KEYS = (
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_aggregate_summary_sha256", "component_aggregate_manifest_sha256",
    "replay_counts", "cross_precision", "diagnostics", "failures",
    "source_bindings", "claim_boundary", "milestone_status", "theorem_status",
    "final_status",
)
FORMAL_POSTCHECK_KEYS = (
    "schema_version", "protocol_id", "artifact_role", "authority",
    "postcheck_status", "passed", "checker_path", "checker_sha256",
    "main_freeze_sha256", "run_config_sha256", "bound_artifacts",
    "replay_counts", "failures", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status", "theorem_status",
    "final_status",
)


def load_checker():
    name = "check_r401_val_l3_a1_v2_static_independent_tested"
    spec = importlib.util.spec_from_file_location(name, CHECKER_SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def checker():
    return load_checker()


@pytest.fixture()
def formal_context(checker):
    return checker.FormalStaticContext(
        matrix_id="1" * 64,
        freeze_sha256="2" * 64,
        run_config_sha256="3" * 64,
        max_depth=24,
        max_nodes_per_tree=250000,
        max_nodes_per_cell=1000000,
    )


@pytest.fixture()
def owned_candidate_parent():
    parent = Path(tempfile.mkdtemp(prefix="a416-v2-role20-test-", dir="/tmp"))
    os.chmod(parent, 0o700)
    try:
        yield parent
    finally:
        for entry in tuple(parent.iterdir()):
            if entry.is_file() or entry.is_symlink():
                entry.unlink()
        parent.rmdir()


def synthetic_formal_replay(checker, tmp_path: Path) -> dict:
    authority = checker.FormalAuthority(
        tmp_path,
        {},
        b"",
        (
            {
                "role": "static_checker_source",
                "path": checker.V2_CHECKER_RELATIVE,
                "sha256": "a" * 64,
            },
            {
                "role": "scheduler",
                "path": "scripts/run_r401_val_l3_a1_v2_all_slabs.py",
                "sha256": "b" * 64,
            },
        ),
        {},
        {},
        {},
    )
    return {
        "authority": authority,
        "main_freeze_sha256": "1" * 64,
        "run_config_sha256": "2" * 64,
        "matrix_id": "3" * 64,
        "aggregate_summary_sha256": "4" * 64,
        "aggregate_manifest_sha256": "5" * 64,
        "aggregate_summary_size_bytes": 10,
        "aggregate_manifest_size_bytes": 11,
        "ordered_cell_manifest_root": "6" * 64,
        "replay_counts": {"cell_manifests": 102, "hash_bound_payloads": 408},
        "cross_precision": {
            "slab_pairs": 51,
            "status_pairs_agree": 51,
            "passed": True,
        },
    }


def build_formal_s0_adapter_proof(checker, context) -> dict:
    source = json.loads(S0_PROOF.read_text(encoding="utf-8"))
    tree_by_id = {tree["tree_id"]: tree for tree in source["trees"]}
    formal_trees = [
        tree_by_id[tree_id]
        for tree_id in ("ANGLE", "SECTION_LOW", "SECTION_HIGH", "SECTION_WINDOW")
    ]
    plan = checker.load_plan()
    record = plan["S000"]
    counts = dict(source["counts"])
    counts["maximum_depth"] = max(tree["maximum_depth"] for tree in formal_trees)
    payload = {
        "schema_version": 1,
        "protocol_id": "R401-VAL-L3-A1",
        "artifact_role": "STATIC_CELL_PROOF",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": context.matrix_id,
        "freeze_sha256": context.freeze_sha256,
        "run_config_sha256": context.run_config_sha256,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "slab_id": "S000",
        "precision_bits": 128,
        "epsilon": source["epsilon"],
        "period_window": source["period_window"],
        "input_echo": {
            "slab_id": "S000",
            "precision_bits": 128,
            "epsilon_lower": record["epsilon_lower"],
            "epsilon_upper": record["epsilon_upper"],
            "matrix_id": context.matrix_id,
            "freeze_sha256": context.freeze_sha256,
            "run_config_sha256": context.run_config_sha256,
            "plan_record_sha256": checker.plan_record_sha256(record),
            "max_depth": context.max_depth,
            "max_nodes_per_tree": context.max_nodes_per_tree,
            "max_nodes_per_cell": context.max_nodes_per_cell,
        },
        "claim_boundary": checker.CELL_CLAIM_BOUNDARY,
        "proof_complete": True,
        "outer_containment": source["outer_containment"],
        "trees": formal_trees,
        "counts": counts,
        "source_bindings": checker.expected_source_bindings(record),
        "proof_content_hash_definition": (
            "sha256(canonical_json(proof_without_proof_content_sha256))"
        ),
    }
    payload["proof_content_sha256"] = checker.sha256_bytes(
        checker.canonical_json_bytes(payload)
    )
    return payload


def write_payload(checker, path: Path, payload: dict) -> None:
    path.write_bytes(checker.canonical_json_bytes(payload))


def formal_binding(
    checker,
    name: str,
    raw: bytes,
    serializer: str,
    *,
    truncated: bool = False,
) -> dict:
    return {
        "path": name,
        "sha256": checker.sha256_bytes(raw),
        "size_bytes": len(raw),
        "serializer": serializer,
        "truncated": truncated,
    }


def build_formal_static_archive(
    checker,
    context,
    tmp_path: Path,
    *,
    outcome: str = "pass",
) -> tuple[Path, Path, list[str], dict]:
    root = tmp_path / f"formal-{outcome}"
    cell_dir = root / "static/cells/128/S000"
    manifest_path = root / "static/cell_manifests/128/S000.json"
    cell_dir.mkdir(parents=True)
    manifest_path.parent.mkdir(parents=True)
    plan = checker.load_plan()
    plan_record = plan["S000"]
    pass_proof = build_formal_s0_adapter_proof(checker, context)
    evaluator_status: str | None
    return_code: int | None
    classification: str
    proof_kind: str
    reason_code: str | None
    proof_serializer: str
    stdout_raw = b""
    stderr_raw = b""
    proof_truncated = False
    stdout_truncated = False
    stderr_truncated = False

    if outcome == "pass":
        proof_raw = checker.canonical_json_bytes(pass_proof)
        evaluator_status = "STATIC_CELL_CERTIFIED"
        return_code = 0
        classification = "COMMITTED_EVALUATOR_RESULT"
        proof_kind = "EVALUATOR_PROOF"
        reason_code = None
        proof_serializer = "CJ_COMPACT_V1"
        stdout_raw = b"evaluator_status=STATIC_CELL_CERTIFIED\n"
    elif outcome == "nonzero":
        proof = {
            key: value
            for key, value in pass_proof.items()
            if key
            not in {
                "outer_containment",
                "source_bindings",
                "proof_content_sha256",
            }
        }
        proof["evaluator_status"] = "STATIC_UNRESOLVED_DEPTH"
        proof["proof_complete"] = False
        proof["failure"] = {
            "tree_id": "ANGLE",
            "limit": context.max_depth,
            "unresolved_depth": context.max_depth,
            "node_id": "ANGLE0",
        }
        proof["trees"] = []
        proof["counts"] = {
            "tree_count": 0,
            "node_count": 0,
            "internal_count": 0,
            "terminal_count": 0,
            "unresolved_count": 1,
            "maximum_depth": None,
        }
        proof["proof_content_sha256"] = checker.sha256_bytes(
            checker.canonical_json_bytes(proof)
        )
        proof_raw = checker.canonical_json_bytes(proof)
        evaluator_status = "STATIC_UNRESOLVED_DEPTH"
        return_code = 2
        classification = "COMMITTED_EVALUATOR_RESULT"
        proof_kind = "EVALUATOR_PROOF"
        reason_code = None
        proof_serializer = "CJ_COMPACT_V1"
        stdout_raw = b"evaluator_status=STATIC_UNRESOLVED_DEPTH\n"
    elif outcome == "status_mismatch":
        proof_raw = checker.canonical_json_bytes(pass_proof)
        evaluator_status = None
        return_code = 9
        classification = "MALFORMED_EVALUATOR_OUTPUT"
        proof_kind = "EVALUATOR_PROOF"
        reason_code = "STATUS_OR_RETURN_CODE_MISMATCH"
        proof_serializer = "CJ_COMPACT_V1"
        stdout_raw = b"evaluator_status=STATIC_CELL_CERTIFIED\nextra\n"
    elif outcome == "invalid_proof":
        proof_raw = b'{"not":"closed"}\ntrailing'
        evaluator_status = None
        return_code = 0
        classification = "MALFORMED_EVALUATOR_OUTPUT"
        proof_kind = "INVALID_EVALUATOR_PROOF"
        reason_code = "MALFORMED_OR_NONCANONICAL_PROOF"
        proof_serializer = "RAW_BYTES"
        stdout_raw = b"evaluator_status=STATIC_CELL_CERTIFIED\n"
    elif outcome in {"sentinel", "cap"}:
        classification = (
            "CELL_TIMEOUT" if outcome == "sentinel" else "CELL_OUTPUT_BUDGET_EXHAUSTED"
        )
        reason_code = "TIMEOUT" if outcome == "sentinel" else "OUTPUT_BUDGET"
        sentinel = {
            "schema_version": 1,
            "protocol_id": "R401-VAL-L3-A1",
            "artifact_role": "STATIC_PROOF_ABSENT",
            "authority": "PRODUCER_ONLY",
            "scientific_licensing_enabled": False,
            "matrix_id": context.matrix_id,
            "freeze_sha256": context.freeze_sha256,
            "main_freeze_sha256": context.freeze_sha256,
            "run_config_sha256": context.run_config_sha256,
            "cell": {"precision_bits": 128, "slab_id": "S000"},
            "scheduler_classification": classification,
            "evaluator_status": None,
            "reason_code": reason_code,
            "claim_boundary": checker.CELL_CLAIM_BOUNDARY,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        }
        proof_raw = checker.canonical_json_bytes(sentinel)
        evaluator_status = None
        return_code = None
        proof_kind = "SCHEDULER_NO_PROOF_SENTINEL"
        proof_serializer = "CJ_COMPACT_V1"
        if outcome == "cap":
            stdout_raw = b"captured-prefix"
            stdout_truncated = True
    else:
        raise AssertionError(outcome)

    (cell_dir / "proof.json").write_bytes(proof_raw)
    (cell_dir / "stdout.txt").write_bytes(stdout_raw)
    (cell_dir / "stderr.txt").write_bytes(stderr_raw)
    semantic_argv = [f"arg-{index}" for index in range(25)] + ["<STAGING_PROOF_PATH>"]
    invocation_sha256 = checker.sha256_bytes(
        checker.canonical_json_bytes(semantic_argv)
    )
    evaluator_result = (
        {
            "status": evaluator_status,
            "return_code": return_code,
            "status_line_count": 1,
        }
        if classification == "COMMITTED_EVALUATOR_RESULT"
        else {"status": None, "return_code": None, "status_line_count": 0}
    )
    limits = {
        "max_depth_per_tree": context.max_depth,
        "max_nodes_per_tree": context.max_nodes_per_tree,
        "max_nodes_per_cell": context.max_nodes_per_cell,
        "timeout_ms": 1_800_000,
        "total_cell_bytes": 512 * 1024 * 1024,
    }
    files = {
        "proof.json": formal_binding(
            checker,
            "proof.json",
            proof_raw,
            proof_serializer,
            truncated=proof_truncated,
        ),
        "stdout.txt": formal_binding(
            checker,
            "stdout.txt",
            stdout_raw,
            "RAW_BYTES",
            truncated=stdout_truncated,
        ),
        "stderr.txt": formal_binding(
            checker,
            "stderr.txt",
            stderr_raw,
            "RAW_BYTES",
            truncated=stderr_truncated,
        ),
    }
    record = {
        "schema_version": 1,
        "protocol_id": "R401-VAL-L3-A1",
        "artifact_role": "STATIC_CELL_RECORD",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": context.matrix_id,
        "freeze_sha256": context.freeze_sha256,
        "main_freeze_sha256": context.freeze_sha256,
        "run_config_sha256": context.run_config_sha256,
        "cell": {"precision_bits": 128, "slab_id": "S000"},
        "task": {
            "epsilon_lower": plan_record["epsilon_lower"],
            "epsilon_upper": plan_record["epsilon_upper"],
            "plan_record_sha256": checker.plan_record_sha256(plan_record),
        },
        "semantic_invocation": {
            "argv": semantic_argv,
            "argv_sha256": invocation_sha256,
            "exact_string_count": 26,
            "output_token": "<STAGING_PROOF_PATH>",
        },
        "scheduler_result": {
            "classification": classification,
            "evaluator_status": evaluator_status,
            "return_code": return_code,
            "proof_kind": proof_kind,
            "reason_code": reason_code,
        },
        "evaluator_result": evaluator_result,
        "files": files,
        "limits": limits,
        "claim_boundary": checker.CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    record_raw = checker.canonical_json_bytes(record)
    (cell_dir / "record.json").write_bytes(record_raw)
    manifest_files = {
        **files,
        "record.json": formal_binding(
            checker, "record.json", record_raw, "CJ_COMPACT_V1"
        ),
    }
    manifest = {
        "schema_version": 1,
        "protocol_id": "R401-VAL-L3-A1",
        "artifact_role": "STATIC_CELL_MANIFEST",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": context.matrix_id,
        "freeze_sha256": context.freeze_sha256,
        "main_freeze_sha256": context.freeze_sha256,
        "run_config_sha256": context.run_config_sha256,
        "cell": {"precision_bits": 128, "slab_id": "S000"},
        "semantic_invocation_sha256": invocation_sha256,
        "scheduler_classification": classification,
        "evaluator_status": evaluator_status,
        "record": manifest_files["record.json"],
        "files": manifest_files,
        "claim_boundary": checker.CELL_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    manifest_path.write_bytes(checker.canonical_json_bytes(manifest))
    return cell_dir, manifest_path, semantic_argv, limits


def rebind_formal_record(checker, cell_dir: Path, manifest_path: Path, record: dict) -> None:
    record_raw = checker.canonical_json_bytes(record)
    (cell_dir / "record.json").write_bytes(record_raw)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for name in ("proof.json", "stdout.txt", "stderr.txt"):
        manifest["files"][name] = record["files"][name]
    binding = formal_binding(checker, "record.json", record_raw, "CJ_COMPACT_V1")
    manifest["record"] = binding
    manifest["files"]["record.json"] = binding
    manifest_path.write_bytes(checker.canonical_json_bytes(manifest))


def test_checker_source_is_independent() -> None:
    source = CHECKER_SOURCE.read_text(encoding="utf-8")
    assert "import evaluate_r401_val_l3_a1_static_cell" not in source
    assert "import run_r401_val_l3_a1_all_slabs" not in source
    assert "run_r401_val_l3_phase_tube_smoke" not in source
    imported: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module)
    assert not imported & {
        "evaluate_r401_val_l3_a1_static_cell",
        "run_r401_val_l3_a1_all_slabs",
        "check_r401_val_l3_a1_branch_independent",
        "check_r401_val_l3_a1_composite_independent",
    }


def test_checker_role_and_tree_order_match_formal_contract(checker) -> None:
    assert checker.CHECKER_ROLE == "STATIC_INDEPENDENT_CHECKER"
    assert tuple(checker.SECTION_ROOTS) == (
        "SECTION_LOW",
        "SECTION_HIGH",
        "SECTION_WINDOW",
    )


def test_checker_compact_serializer_known_answer_and_exact_type_domain(checker) -> None:
    payload = {"z": "λ", "a": [1, True, None, {"x": "y"}]}
    assert checker.canonical_json_bytes(payload) == (
        b'{"a":[1,true,null,{"x":"y"}],"z":"\xce\xbb"}\n'
    )
    for rejected in (
        {"x": (1, 2)},
        {1: "non-string-key"},
        {"x": math.nan},
        {"x": -math.inf},
    ):
        with pytest.raises(checker.CheckError):
            checker.canonical_json_bytes(rejected)


def test_formal_four_file_cell_replays_and_is_only_leaf_eligible(
    checker, formal_context, tmp_path: Path
) -> None:
    cell_dir, manifest_path, argv, limits = build_formal_static_archive(
        checker, formal_context, tmp_path
    )
    result = checker.validate_formal_static_cell(
        cell_dir,
        manifest_path,
        expected_bits=128,
        expected_slab="S000",
        plan=checker.load_plan(),
        context=formal_context,
        expected_semantic_argv=argv,
        expected_limits=limits,
    )
    assert result["component_eligible"] is True
    assert result["scheduler_classification"] == "COMMITTED_EVALUATOR_RESULT"
    assert result["evaluator_status"] == "STATIC_CELL_CERTIFIED"
    assert result["proof_kind"] == "EVALUATOR_PROOF"
    assert result["proof_replay"]["unresolved_count"] == 0


@pytest.mark.parametrize(
    ("outcome", "classification", "proof_kind"),
    [
        ("nonzero", "COMMITTED_EVALUATOR_RESULT", "EVALUATOR_PROOF"),
        ("status_mismatch", "MALFORMED_EVALUATOR_OUTPUT", "EVALUATOR_PROOF"),
        ("invalid_proof", "MALFORMED_EVALUATOR_OUTPUT", "INVALID_EVALUATOR_PROOF"),
        ("sentinel", "CELL_TIMEOUT", "SCHEDULER_NO_PROOF_SENTINEL"),
        ("cap", "CELL_OUTPUT_BUDGET_EXHAUSTED", "SCHEDULER_NO_PROOF_SENTINEL"),
    ],
)
def test_formal_nonpass_status_sentinel_cap_and_malformed_never_promote(
    checker,
    formal_context,
    tmp_path: Path,
    outcome: str,
    classification: str,
    proof_kind: str,
) -> None:
    cell_dir, manifest_path, argv, limits = build_formal_static_archive(
        checker, formal_context, tmp_path, outcome=outcome
    )
    result = checker.validate_formal_static_cell(
        cell_dir,
        manifest_path,
        expected_bits=128,
        expected_slab="S000",
        plan=checker.load_plan(),
        context=formal_context,
        expected_semantic_argv=argv,
        expected_limits=limits,
    )
    assert result["component_eligible"] is False
    assert result["scheduler_classification"] == classification
    assert result["proof_kind"] == proof_kind
    assert result["proof_replay"] is None


@pytest.mark.parametrize(
    ("mutation", "match"),
    [
        ("authority", "authority"),
        ("path", "path"),
        ("hash", "hash"),
        ("size", "size"),
        ("serializer", "serializer"),
        ("truncated", "truncated"),
    ],
)
def test_formal_record_nested_authority_and_file_bindings_fail_closed(
    checker,
    formal_context,
    tmp_path: Path,
    mutation: str,
    match: str,
) -> None:
    cell_dir, manifest_path, argv, limits = build_formal_static_archive(
        checker, formal_context, tmp_path
    )
    record = json.loads((cell_dir / "record.json").read_text(encoding="utf-8"))
    if mutation == "authority":
        record["authority"] = "INDEPENDENT_CHECKER"
    elif mutation == "path":
        record["files"]["proof.json"]["path"] = "../proof.json"
    elif mutation == "hash":
        record["files"]["proof.json"]["sha256"] = "0" * 64
    elif mutation == "size":
        record["files"]["proof.json"]["size_bytes"] += 1
    elif mutation == "serializer":
        record["files"]["proof.json"]["serializer"] = "RAW_BYTES"
    elif mutation == "truncated":
        record["files"]["proof.json"]["truncated"] = True
    else:
        raise AssertionError(mutation)
    rebind_formal_record(checker, cell_dir, manifest_path, record)
    with pytest.raises(checker.CheckError, match=match):
        checker.validate_formal_static_cell(
            cell_dir,
            manifest_path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
            expected_semantic_argv=argv,
            expected_limits=limits,
        )


def test_formal_manifest_authority_and_leaf_symlink_fail_closed(
    checker, formal_context, tmp_path: Path
) -> None:
    cell_dir, manifest_path, argv, limits = build_formal_static_archive(
        checker, formal_context, tmp_path
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["theorem_status"] = "FORGED"
    manifest_path.write_bytes(checker.canonical_json_bytes(manifest))
    with pytest.raises(checker.CheckError, match="theorem_status"):
        checker.validate_formal_static_cell(
            cell_dir,
            manifest_path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
            expected_semantic_argv=argv,
            expected_limits=limits,
        )

    cell_dir, manifest_path, argv, limits = build_formal_static_archive(
        checker, formal_context, tmp_path, outcome="sentinel"
    )
    stdout = cell_dir / "stdout.txt"
    raw = stdout.read_bytes()
    stdout.unlink()
    target = tmp_path / "stdout-target.txt"
    target.write_bytes(raw)
    stdout.symlink_to(target)
    with pytest.raises(checker.CheckError):
        checker.validate_formal_static_cell(
            cell_dir,
            manifest_path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
            expected_semantic_argv=argv,
            expected_limits=limits,
        )


def test_formal_archive_cannot_enter_current_aggregate_checker(
    checker, formal_context, tmp_path: Path
) -> None:
    cell_dir, _manifest_path, _argv, _limits = build_formal_static_archive(
        checker, formal_context, tmp_path
    )
    formal_root = cell_dir.parents[3]
    with pytest.raises(checker.CheckError):
        checker.run_checker(formal_root)


def test_checker_plan_semantics_and_binding_share_one_pinned_snapshot(
    checker, monkeypatch: pytest.MonkeyPatch
) -> None:
    original_read = checker.read_pinned_regular_bytes
    accepted_raw = original_read(checker.PLAN)
    mutated = json.loads(accepted_raw)
    mutated["slabs"][0]["epsilon_lower"] = "0.0001"
    later_raw = checker.canonical_json_bytes(mutated)
    plan_reads = 0

    def staged_read(path: Path) -> bytes:
        nonlocal plan_reads
        if path == checker.PLAN:
            plan_reads += 1
            return accepted_raw if plan_reads == 1 else later_raw
        return original_read(path)

    monkeypatch.setattr(checker, "read_pinned_regular_bytes", staged_read)
    record = checker.load_plan()["S000"]
    bindings = checker.expected_source_bindings(record)

    assert plan_reads == 1
    assert record["epsilon_lower"] == "0.0000"
    assert bindings["l1_final_plan_sha256"] == checker.sha256_bytes(accepted_raw)


def test_checker_rejects_lexical_dotdot_proof_path(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    (tmp_path / "sub").mkdir()
    alias = tmp_path / "sub" / ".." / "proof.json"
    with pytest.raises(checker.CheckError, match="dot or empty"):
        checker.verify_proof(
            alias,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_checker_cli_rejects_path_aliases(checker) -> None:
    for value in ("//tmp/proof.json", "/tmp//proof.json", "/tmp/../proof.json"):
        with pytest.raises(Exception):
            checker.canonical_absolute_argument(value)


def test_checker_upstream_replay_rejects_extra_authority_field(
    checker, monkeypatch: pytest.MonkeyPatch
) -> None:
    payloads = {
        path: checker.load_strict_json_object_with_raw(path)[0]
        for path in (
            checker.L1_SUMMARY,
            checker.L1_MANIFEST,
            checker.L1_CHECKER,
            checker.L1_POSTCHECK,
            checker.L1_RELEASE,
        )
    }
    payloads[checker.L1_SUMMARY] = dict(payloads[checker.L1_SUMMARY])
    payloads[checker.L1_SUMMARY]["theorem_status"] = "FORGED_UNAUTHORIZED"
    monkeypatch.setattr(
        checker,
        "load_strict_json_object_with_raw",
        lambda path: (payloads[path], checker.canonical_json_bytes(payloads[path])),
    )
    with pytest.raises(checker.CheckError, match="keys differ"):
        checker.independently_validate_l1_release_chain()


def test_independent_replay_accepts_read_only_s0_math_adapter(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    result = checker.verify_proof(
        path,
        expected_bits=128,
        expected_slab="S000",
        plan=checker.load_plan(),
        context=formal_context,
    )
    assert result["node_count"] == 13794
    assert result["unresolved_count"] == 0
    assert result["maximum_depth"] == 14
    assert result["interval_checks"] > result["node_count"]


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("schema_version", True),
        ("precision_bits", 128.0),
        ("evaluator_status", "STATIC_UNRESOLVED_DEPTH"),
        ("scientific_licensing_enabled", True),
        ("component_status", "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"),
        ("milestone_status", "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"),
        ("final_status", "PASS_GLOBAL"),
    ],
)
def test_header_authority_and_type_mutations_fail_before_science(
    checker, formal_context, tmp_path: Path, key: str, value: object
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    payload[key] = value
    without_hash = dict(payload)
    without_hash.pop("proof_content_sha256")
    payload["proof_content_sha256"] = checker.sha256_bytes(
        checker.canonical_json_bytes(without_hash)
    )
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_content_hash_mutation_is_rejected(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    payload["proof_content_sha256"] = "0" * 64
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    with pytest.raises(checker.CheckError, match="proof content hash"):
        checker.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_recomputed_proof_cannot_exceed_frozen_resource_caps(checker, tmp_path: Path) -> None:
    context = checker.FormalStaticContext(
        matrix_id="1" * 64,
        freeze_sha256="2" * 64,
        run_config_sha256="3" * 64,
        max_depth=24,
        max_nodes_per_tree=100,
        max_nodes_per_cell=100,
    )
    payload = build_formal_s0_adapter_proof(checker, context)
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    with pytest.raises(checker.CheckError, match="node count exceeds"):
        checker.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=context,
        )


def test_proof_leaf_and_parent_aliases_are_rejected(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    real_parent = tmp_path / "real"
    real_parent.mkdir()
    real_proof = real_parent / "proof.json"
    write_payload(checker, real_proof, payload)

    leaf_alias = tmp_path / "proof-link.json"
    leaf_alias.symlink_to(real_proof)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            leaf_alias,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )

    parent_alias = tmp_path / "parent-link"
    parent_alias.symlink_to(real_parent, target_is_directory=True)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            parent_alias / "proof.json",
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )

    hard_alias = tmp_path / "proof-hard.json"
    hard_alias.hardlink_to(real_proof)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            hard_alias,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_context_rejects_boolean_and_integral_float_aliases(checker) -> None:
    for bad_depth in (True, 24.0):
        context = checker.FormalStaticContext(
            matrix_id="1" * 64,
            freeze_sha256="2" * 64,
            run_config_sha256="3" * 64,
            max_depth=bad_depth,
            max_nodes_per_tree=250000,
            max_nodes_per_cell=1000000,
        )
        with pytest.raises(checker.CheckError):
            checker.validate_formal_context(context)


@pytest.mark.parametrize(
    "raw",
    ['{"x":1,"x":2}\n', '{"x":NaN}\n', '{"x":1e400}\n'],
)
def test_strict_loader_rejects_duplicate_and_nonfinite(
    checker, tmp_path: Path, raw: str
) -> None:
    path = tmp_path / "bad.json"
    path.write_text(raw, encoding="utf-8")
    with pytest.raises(checker.CheckError):
        checker.load_canonical_json(path)


def test_write_once_rejects_existing_checker(checker, tmp_path: Path) -> None:
    output = tmp_path / "independent_static_checker.json"
    checker.write_once(output, b"{}\n")
    with pytest.raises(FileExistsError):
        checker.write_once(output, b"different\n")


def test_formal_checker_and_exact19_postcheck_synthetic_contract(
    checker, tmp_path: Path
) -> None:
    replay = synthetic_formal_replay(checker, tmp_path)
    payload = checker._checker_payload_from_replay(replay)
    assert set(payload) == set(FORMAL_CHECKER_KEYS) == checker.FORMAL_CHECKER_KEYS
    assert payload["checker_status"] == "PASS_INDEPENDENT_CHECKER"
    assert payload["component_status"] == "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
    assert payload["scientific_licensing_enabled"] is False
    checker.validate_checker_payload(payload, payload)

    checker_raw = checker.canonical_json_bytes(payload)
    postcheck = checker._postcheck_payload_from_replay(replay, checker_raw)
    assert set(postcheck) == set(FORMAL_POSTCHECK_KEYS) == checker.FORMAL_POSTCHECK_KEYS
    assert postcheck["postcheck_status"] == "PASS_WRITE_ONCE_POSTCHECK"
    assert postcheck["scientific_licensing_enabled"] is False
    assert postcheck["bound_artifacts"] == {
        "aggregate_summary": {
            "path": "static/aggregate_summary.json", "sha256": "4" * 64,
            "size_bytes": 10,
        },
        "aggregate_manifest": {
            "path": "static/aggregate_manifest.json", "sha256": "5" * 64,
            "size_bytes": 11,
        },
        "ordered_cell_manifest_root": "6" * 64,
    }
    checker.validate_postcheck_payload(postcheck, postcheck)


@pytest.mark.parametrize("missing", FORMAL_CHECKER_KEYS)
def test_exact22_checker_rejects_every_missing_key(
    checker, tmp_path: Path, missing: str
) -> None:
    expected = checker._checker_payload_from_replay(
        synthetic_formal_replay(checker, tmp_path)
    )
    mutated = copy.deepcopy(expected)
    del mutated[missing]
    with pytest.raises(checker.CheckError, match="keys differ"):
        checker.validate_checker_payload(mutated, expected)


@pytest.mark.parametrize("missing", FORMAL_POSTCHECK_KEYS)
def test_exact19_postcheck_rejects_every_missing_key(
    checker, tmp_path: Path, missing: str
) -> None:
    replay = synthetic_formal_replay(checker, tmp_path)
    checker_raw = checker.canonical_json_bytes(
        checker._checker_payload_from_replay(replay)
    )
    expected = checker._postcheck_payload_from_replay(replay, checker_raw)
    mutated = copy.deepcopy(expected)
    del mutated[missing]
    with pytest.raises(checker.CheckError, match="keys differ"):
        checker.validate_postcheck_payload(mutated, expected)


@pytest.mark.parametrize("missing", MAIN_FREEZE_KEYS)
def test_exact26_main_rejects_every_missing_key(
    checker, tmp_path: Path, missing: str
) -> None:
    payload = {key: None for key in MAIN_FREEZE_KEYS}
    del payload[missing]
    with pytest.raises(checker.CheckError, match="keys differ"):
        checker._validate_main_payload(tmp_path, payload, (), {}, {})


@pytest.mark.parametrize(
    ("kind", "mutation"),
    (
        ("checker", "extra"),
        ("checker", "array"),
        ("postcheck", "extra"),
        ("postcheck", "legacy18"),
        ("postcheck", "nested_extra"),
        ("main", "extra"),
        ("main", "array"),
    ),
)
def test_closed_formal_schemas_reject_extra_legacy_and_type_aliases(
    checker, tmp_path: Path, kind: str, mutation: str
) -> None:
    replay = synthetic_formal_replay(checker, tmp_path)
    checker_payload = checker._checker_payload_from_replay(replay)
    if kind == "checker":
        expected = copy.deepcopy(checker_payload)
        payload = copy.deepcopy(expected)
        if mutation == "extra":
            payload["generation"] = "V2"
        else:
            payload = []
        with pytest.raises(checker.CheckError):
            checker.validate_checker_payload(payload, expected)
    elif kind == "postcheck":
        expected = checker._postcheck_payload_from_replay(
            replay, checker.canonical_json_bytes(checker_payload)
        )
        payload = copy.deepcopy(expected)
        if mutation == "extra":
            payload["generation"] = "V2"
        elif mutation == "legacy18":
            del payload["scientific_licensing_enabled"]
        else:
            payload["bound_artifacts"]["receipt"] = {"path": "/tmp/forged"}
            expected = copy.deepcopy(payload)
        with pytest.raises(checker.CheckError):
            checker.validate_postcheck_payload(payload, expected)
    else:
        payload = {key: None for key in MAIN_FREEZE_KEYS}
        if mutation == "extra":
            payload["generation"] = "V2"
        else:
            payload = []
        with pytest.raises(checker.CheckError):
            checker._validate_main_payload(tmp_path, payload, (), {}, {})


@pytest.mark.parametrize(
    ("stdout", "wall_ms", "passed"),
    (
        ("1 passed in 0.01s\n", 15, 1),
        ("9999 passed in 60.00s\n", 60005, 9999),
        ("42 passed in 60.01s (0:01:00)\n", 60015, 42),
        ("42 passed in 600.00s (0:10:00)\n", 600005, 42),
    ),
)
def test_role11_pytest_parser_accepts_only_frozen_success_domain(
    checker, stdout: str, wall_ms: int, passed: int
) -> None:
    assert checker._parse_pytest_counts(
        stdout, "synthetic role11", wall_duration_ms=wall_ms
    ) == {
        "passed": passed, "failed": 0, "skipped": 0,
        "xfailed": 0, "xpassed": 0,
    }


@pytest.mark.parametrize(
    ("stdout", "wall_ms"),
    (
        ("01 passed in 0.01s\n", 100),
        ("1 passed in 0.01s\r\n", 100),
        ("1 passed\x85 in 0.01s\n", 100),
        ("warning\n1 passed in 0.01s\n", 100),
        ("1 failed, 1 passed in 0.01s\n", 100),
        ("1 skipped, 1 passed in 0.01s\n", 100),
        ("1 passed in 60.01s\n", 70000),
        ("1 passed in 61.01s (0:01:00)\n", 70000),
        ("1 passed in 600.01s (0:10:00)\n", 603000),
        ("1 passed in 1.00s\n", 994),
        ("1 passed in 0.01s\n1 passed in 0.01s\n", 100),
        ("1 passed in 0.01s", 100),
    ),
)
def test_role11_pytest_parser_rejects_alias_failure_and_timeout_domains(
    checker, stdout: str, wall_ms: int
) -> None:
    with pytest.raises(checker.CheckError):
        checker._parse_pytest_counts(
            stdout, "synthetic role11", wall_duration_ms=wall_ms
        )


def test_role5_legacy_live_literal_git_blob_triangle(checker) -> None:
    queries = [
        (item["publication_commit"], item["path"])
        for item in checker.ROLE5_LEGACY_ARTIFACTS
    ]
    committed = checker._git_blob_batch(checker.ROOT, queries)
    assert len(committed) == 4
    for item, (raw, mode) in zip(
        checker.ROLE5_LEGACY_ARTIFACTS, committed, strict=True
    ):
        live = checker.read_pinned_regular_bytes(checker.ROOT / item["path"])
        assert raw == live
        assert checker.sha256_bytes(raw) == item["sha256"]
        assert mode == "100644"


@pytest.mark.parametrize(
    ("commit", "path"),
    (
        ("0" * 40, "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"),
        (
            "5086e33c7c66f33785338e90b340347e086d9941",
            "research/route_a_wave_trace/DOES_NOT_EXIST.json",
        ),
    ),
)
def test_pure_git_parser_rejects_unknown_commit_and_path(
    checker, commit: str, path: str
) -> None:
    with pytest.raises(checker.CheckError):
        checker._git_blob_batch(checker.ROOT, [(commit, path)])


def test_role5_exact_reviewed19_and_literal_semantics(
    checker, monkeypatch: pytest.MonkeyPatch
) -> None:
    rows = []
    images = {}
    for index, role in enumerate(checker.ROLE5_REVIEWED_ROLES):
        raw = f"role-{index}\n".encode()
        relative = f"synthetic/reviewed_{index}.txt"
        rows.append({
            "role": role, "path": relative,
            "sha256": checker.sha256_bytes(raw),
        })
        images[role] = raw
    payload = {
        "schema_version": 1,
        "protocol_id": checker.PROTOCOL_ID,
        "artifact_role": "V2_DESIGN_REVIEW_AND_ATTEMPT1_WITHDRAWAL",
        "status": "ACCEPT_V2_CONTROL_DESIGN_WITHDRAW_ATTEMPT1",
        "authority": "INDEPENDENT_CONTROL_DESIGN_REVIEW_ONLY",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "legacy_attempt": {
            "attempt_id": "A416_L3_A1_CONTROL_ATTEMPT_1",
            "status": "WITHDRAWN_NON_LICENSING",
            "terminal_commit": "e9a794d7f4734a1b23ba265c58bbbbc2aca6d5e0",
            "published_artifacts": list(checker.ROLE5_LEGACY_ARTIFACTS),
            "defects": list(checker.ROLE5_LEGACY_DEFECTS),
            "supersession_rule": checker.ROLE5_SUPERSESSION_RULE,
        },
        "reviewed_v2_inputs": copy.deepcopy(rows),
        "review": {
            "reviewer_independent_of_attempt1_author": True,
            "verdict": "ACCEPT_CONTROL_PLANE_V2_DESIGN",
            "p0_count": 0, "p1_count": 0, "p2_count": 0,
            "reviewed_commit": "a" * 40,
            "map_matches_contract": True,
            "legacy_bytes_unchanged": True,
            "scientific_protocol_unchanged": True,
        },
        "claim_boundary": checker.ROLE5_CLAIM_BOUNDARY,
        "component_status": None, "milestone_status": None,
        "theorem_status": None, "final_status": None,
    }
    legacy_raw = [
        checker.read_pinned_regular_bytes(checker.ROOT / item["path"])
        for item in checker.ROLE5_LEGACY_ARTIFACTS
    ]
    monkeypatch.setattr(
        checker,
        "_git_blob_batch",
        lambda _root, _queries: [
            *((raw, "100644") for raw in legacy_raw),
            *((images[row["role"]], "100644") for row in rows),
        ],
    )
    checker._validate_role5(checker.ROOT, payload, rows, images)
    payload["reviewed_v2_inputs"][0]["sha256"] = "0" * 64
    with pytest.raises(checker.CheckError):
        checker._validate_role5(checker.ROOT, payload, rows, images)


def test_role11_second_rebuild_receipt_binds_live_role17_inode(checker) -> None:
    binary_path = checker.ROOT / "validated/bin/capd_r401_phase_branch_tube_mp_a1"
    source_path = checker.ROOT / "validated/capd_r401_phase_branch_tube_mp_a1.cpp"
    binary_raw = checker.read_pinned_regular_bytes(binary_path)
    source_raw = checker.read_pinned_regular_bytes(source_path)
    info = os.stat(binary_path, follow_symlinks=False)
    roles = {
        "branch_evaluator_source": {
            "path": source_path.relative_to(checker.ROOT).as_posix(),
            "sha256": checker.sha256_bytes(source_raw),
        },
        "branch_evaluator_binary": {
            "path": binary_path.relative_to(checker.ROOT).as_posix(),
            "sha256": checker.sha256_bytes(binary_raw),
            "size_bytes": len(binary_raw),
        },
    }
    receipt = {
        "verification_status": "PASS_SECOND_FRESH_REBUILD",
        "authority": "COMPILER_REPRODUCIBILITY_EVIDENCE_ONLY",
        "source_path": roles["branch_evaluator_source"]["path"],
        "source_sha256": roles["branch_evaluator_source"]["sha256"],
        "persistent_binary_path": roles["branch_evaluator_binary"]["path"],
        "persistent_before_sha256": roles["branch_evaluator_binary"]["sha256"],
        "persistent_after_sha256": roles["branch_evaluator_binary"]["sha256"],
        "persistent_before_device_id": info.st_dev,
        "persistent_before_inode": info.st_ino,
        "persistent_after_device_id": info.st_dev,
        "persistent_after_inode": info.st_ino,
        "persistent_identity_unchanged": True,
        "persistent_overwrite_performed": False,
        "staging_output_sha256": roles["branch_evaluator_binary"]["sha256"],
        "staging_output_size_bytes": len(binary_raw),
        "staging_output_mode": "0755",
        "staging_output_removed": True,
        "byte_for_byte_equal": True,
        "scientific_evaluator_dispatched": False,
    }
    checker._validate_second_receipt(
        receipt, roles, "synthetic rebuild", project_root=checker.ROOT
    )
    receipt["persistent_before_inode"] += 1
    receipt["persistent_after_inode"] += 1
    with pytest.raises(checker.CheckError, match="live role17 inode"):
        checker._validate_second_receipt(
            receipt, roles, "synthetic rebuild", project_root=checker.ROOT
        )


def test_role10_live_conda_capd_elf_and_resource_replays_match_freeze(
    checker,
) -> None:
    machine_path = (
        checker.ROOT
        / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
    )
    machine = json.loads(machine_path.read_bytes())
    python = machine["python_arb"]
    assert checker._machine_recompute_conda_manifest(python["executable_path"]) == (
        python["conda_manifest_file_count"],
        python["conda_installed_manifest_root_sha256"],
    )
    assert checker._machine_capd_tree(Path(machine["capd"]["checkout_path"])) == (
        machine["capd"]["commit"],
        machine["capd"]["tree_sha256"],
    )
    binary_raw = (checker.ROOT / machine["branch_binary"]["path"]).read_bytes()
    build_id, needed, soname = checker._machine_elf_metadata(
        binary_raw, "role10 test branch ELF"
    )
    assert build_id == machine["branch_binary"]["build_id"]
    assert needed == machine["branch_binary"]["dt_needed"]
    assert soname is None
    resource = machine["resource_evidence"]
    assert checker._machine_validate_static_resource(
        checker.ROOT, resource["static_payload_raw_utf8"].encode(), machine
    ) == {"baseline_bytes": 24891273216, "peak_rss_bytes": 59949056}
    assert checker._machine_validate_branch_resource(
        checker.ROOT, resource["branch_payload_raw_utf8"].encode(), machine
    ) == {"baseline_bytes": 14505582592, "peak_rss_bytes": 207286272}


@pytest.mark.parametrize("component", ("static", "branch"))
def test_role10_coherently_reserialized_resource_mutation_is_rejected(
    checker, component: str
) -> None:
    machine = json.loads(
        (
            checker.ROOT
            / "research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json"
        ).read_bytes()
    )
    raw = machine["resource_evidence"][f"{component}_payload_raw_utf8"].encode()
    payload = json.loads(raw)
    if component == "static":
        payload["admission"]["workers"] += 1
        mutated = checker.canonical_json_bytes(payload)
        validator = checker._machine_validate_static_resource
    else:
        payload["admission"]["workers"] += 1
        mutated = (
            json.dumps(
                payload,
                sort_keys=True,
                ensure_ascii=False,
                allow_nan=False,
                indent=2,
            )
            + "\n"
        ).encode()
        validator = checker._machine_validate_branch_resource
    with pytest.raises(checker.CheckError):
        validator(checker.ROOT, mutated, machine)


def test_pinned_reader_rejects_symlink_hardlink_directory_and_fifo_without_open(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    regular = tmp_path / "regular"
    regular.write_bytes(b"abc")
    alias = tmp_path / "alias"
    alias.symlink_to(regular)
    hard = tmp_path / "hard"
    os.link(regular, hard)
    fifo = tmp_path / "fifo"
    os.mkfifo(fifo)
    directory = tmp_path / "directory"
    directory.mkdir()
    original_open = checker.os.open
    target_opens = 0

    def observed_open(path, flags, *args, **kwargs):
        nonlocal target_opens
        if path == fifo.name and kwargs.get("dir_fd") is not None:
            target_opens += 1
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(checker.os, "open", observed_open)
    for rejected in (alias, hard, fifo, directory):
        with pytest.raises(checker.CheckError):
            checker.read_pinned_regular_bytes(rejected)
    assert target_opens == 0


def test_pinned_reader_rejects_preopen_inode_swap(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "target"
    target.write_bytes(b"same")
    original_open = checker.os.open
    swapped = False

    def swapping_open(path, flags, *args, **kwargs):
        nonlocal swapped
        if path == target.name and kwargs.get("dir_fd") is not None and not swapped:
            swapped = True
            target.rename(tmp_path / "old-target")
            target.write_bytes(b"same")
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(checker.os, "open", swapping_open)
    with pytest.raises(checker.CheckError, match="race"):
        checker.read_pinned_regular_bytes(target)


def test_main_verify_rejects_same_byte_candidate_inode_swap_during_semantics(
    checker, owned_candidate_parent: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    candidate = owned_candidate_parent / Path(checker.V2_MAIN_RELATIVE).name
    candidate.write_bytes(b"{}\n")
    os.chmod(candidate, 0o600)
    calls = 0

    monkeypatch.setattr(
        checker, "_capture_formal_roles", lambda _root: ([], {}, {}, {})
    )

    def swap_on_semantic_validation(*_args) -> None:
        nonlocal calls
        calls += 1
        if calls == 1:
            replacement = candidate.parent / "replacement"
            replacement.write_bytes(b"{}\n")
            os.chmod(replacement, 0o600)
            os.replace(replacement, candidate)

    monkeypatch.setattr(checker, "_validate_main_payload", swap_on_semantic_validation)
    with pytest.raises(checker.CheckError, match="candidate changed"):
        checker.verify_formal_main_freeze_path(candidate, checker.ROOT)
    assert calls == 1


@pytest.mark.parametrize(
    "swapped_role",
    ("static_checker_source", "implementation_design_review", "machine_freeze"),
)
def test_main_verify_rejects_same_byte_live_role_inode_generation_swap(
    checker, tmp_path: Path, owned_candidate_parent: Path,
    monkeypatch: pytest.MonkeyPatch, swapped_role: str,
) -> None:
    candidate = owned_candidate_parent / Path(checker.V2_MAIN_RELATIVE).name
    candidate.write_bytes(b"{}\n")
    os.chmod(candidate, 0o600)
    role_names = [
        "static_checker_source", "implementation_design_review", "machine_freeze",
        *(f"synthetic_role_{index:02d}" for index in range(50)),
    ]
    rows = []
    for index, role in enumerate(role_names):
        relative = f"inputs/role-{index:02d}.txt"
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(f"role={role}\n".encode())
        rows.append((role, relative))
    monkeypatch.setattr(checker, "INPUT_ROLES", tuple(rows))
    target = tmp_path / dict(rows)[swapped_role]
    calls = 0

    def swap_one_role(*_args) -> None:
        nonlocal calls
        calls += 1
        if calls == 1:
            raw = target.read_bytes()
            replacement = target.with_name(target.name + ".replacement")
            replacement.write_bytes(raw)
            os.replace(replacement, target)

    monkeypatch.setattr(checker, "_validate_main_payload", swap_one_role)
    with pytest.raises(checker.CheckError, match="role inode generation changed"):
        checker.verify_formal_main_freeze_path(candidate, tmp_path)
    assert calls == 1


def test_main_verify_enforces_private_and_canonical_mode_namespaces(
    checker, tmp_path: Path, owned_candidate_parent: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        checker, "_capture_formal_roles", lambda _root: ([], {}, {}, {})
    )
    monkeypatch.setattr(checker, "_validate_main_payload", lambda *_args: None)
    wrong_leaf = owned_candidate_parent / "alias.json"
    wrong_leaf.write_bytes(b"{}\n")
    os.chmod(wrong_leaf, 0o600)
    with pytest.raises(checker.CheckError, match="fixed-leaf"):
        checker.verify_formal_main_freeze_path(wrong_leaf, tmp_path)
    wrong_leaf.unlink()
    private = owned_candidate_parent / Path(checker.V2_MAIN_RELATIVE).name
    private.write_bytes(b"{}\n")
    os.chmod(private, 0o644)
    with pytest.raises(checker.CheckError, match="mode/link"):
        checker.verify_formal_main_freeze_path(private, tmp_path)
    private.unlink()
    canonical = tmp_path / checker.V2_MAIN_RELATIVE
    canonical.parent.mkdir(parents=True)
    canonical.write_bytes(b"{}\n")
    os.chmod(canonical, 0o600)
    with pytest.raises(checker.CheckError, match="mode/link"):
        checker.verify_formal_main_freeze_path(canonical, tmp_path)


def test_private_checker_candidate_is_owned_0700_singleton_0600(
    checker, owned_candidate_parent: Path
) -> None:
    candidate = owned_candidate_parent / checker.V2_CHECKER_OUTPUT
    raw = b'{"synthetic":true}\n'
    snapshot = checker._write_private_candidate(
        candidate, raw, expected_leaf=checker.V2_CHECKER_OUTPUT,
        revalidate=lambda: raw,
    )
    assert snapshot.raw == raw
    assert candidate.read_bytes() == raw
    assert stat.S_IMODE(candidate.stat().st_mode) == 0o600
    assert tuple(path.name for path in owned_candidate_parent.iterdir()) == (
        checker.V2_CHECKER_OUTPUT,
    )


@pytest.mark.parametrize("attack", ("wrong_mode", "extra", "wrong_leaf"))
def test_private_candidate_parent_and_leaf_attacks_fail_closed(
    checker, owned_candidate_parent: Path, attack: str
) -> None:
    candidate = owned_candidate_parent / checker.V2_CHECKER_OUTPUT
    if attack == "wrong_mode":
        os.chmod(owned_candidate_parent, 0o755)
    elif attack == "extra":
        (owned_candidate_parent / "foreign").write_bytes(b"x")
    else:
        candidate = owned_candidate_parent / "alias.json"
    with pytest.raises(checker.CheckError):
        checker._write_private_candidate(
            candidate, b"{}\n", expected_leaf=checker.V2_CHECKER_OUTPUT,
            revalidate=lambda: b"{}\n",
        )


def test_private_candidate_build_api_replays_generation_without_canonical_write(
    checker, tmp_path: Path, owned_candidate_parent: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    result = tmp_path / checker.V2_RESULT_RELATIVE
    result.mkdir(parents=True)
    candidate = owned_candidate_parent / checker.V2_CHECKER_OUTPUT
    payload = checker._checker_payload_from_replay(
        synthetic_formal_replay(checker, tmp_path)
    )
    raw = checker.canonical_json_bytes(payload)
    identities = (("synthetic", (1, 2, 3, 1, 4, 5, 6)),)
    calls = 0

    def state(_root, _result, *, transient, published):
        nonlocal calls
        calls += 1
        assert transient is None and published is False
        return raw, identities

    monkeypatch.setattr(checker, "_checker_publication_state", state)
    receipt = checker.build_checker_candidate(tmp_path, result, candidate)
    assert receipt["candidate_sha256"] == checker.sha256_bytes(raw)
    assert calls == 3
    assert candidate.read_bytes() == raw
    assert not (result / checker.V2_CHECKER_OUTPUT).exists()


def test_publication_is_0644_write_once_and_identical_existing_is_failure(
    checker, tmp_path: Path
) -> None:
    target = tmp_path / "published.json"
    raw = b'{"pass":true}\n'
    checker._publish_no_replace(target, raw, project_root=tmp_path)
    assert target.read_bytes() == raw
    assert stat.S_IMODE(target.stat().st_mode) == 0o644
    assert target.stat().st_nlink == 1
    with pytest.raises(checker.CheckError, match="already exists"):
        checker._publish_no_replace(target, raw, project_root=tmp_path)
    assert target.read_bytes() == raw


def test_publication_handles_partial_writes_and_revalidates_three_times(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "published.json"
    raw = b'{"payload":"abcdefgh"}\n'
    original_write = checker.os.write
    replays = []

    def partial_write(descriptor, view):
        return original_write(descriptor, view[:2])

    def terminal(transient):
        replays.append(transient)
        return raw

    monkeypatch.setattr(checker.os, "write", partial_write)
    checker._publish_no_replace(
        target, raw, project_root=tmp_path, revalidate=terminal
    )
    assert target.read_bytes() == raw
    assert len(replays) == 3
    assert replays[0] is not None and replays[1] is not None
    assert replays[2] is None


def test_publication_rejects_oversize_payload_before_staging(
    checker, tmp_path: Path
) -> None:
    target = tmp_path / "published.json"
    with pytest.raises(checker.CheckError, match="byte cap"):
        checker._publish_no_replace(
            target,
            b"x" * (checker.PUBLICATION_MAX_BYTES + 1),
            project_root=tmp_path,
        )
    assert not target.exists()
    assert tuple(tmp_path.iterdir()) == ()


@pytest.mark.parametrize(
    ("failure_index", "published"),
    ((1, False), (2, False), (3, True), (4, True)),
)
def test_publication_fsync_failures_preserve_transaction_boundary(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
    failure_index: int, published: bool,
) -> None:
    target = tmp_path / "published.json"
    raw = b'{"fsync":"fault"}\n'
    original_fsync = checker.os.fsync
    calls = 0

    def failing_fsync(descriptor: int) -> None:
        nonlocal calls
        calls += 1
        if calls == failure_index:
            raise OSError("synthetic fsync fault")
        original_fsync(descriptor)

    monkeypatch.setattr(checker.os, "fsync", failing_fsync)
    with pytest.raises(OSError, match="fsync fault"):
        checker._publish_no_replace(target, raw, project_root=tmp_path)
    assert target.exists() is published
    if published:
        assert target.read_bytes() == raw
        assert stat.S_IMODE(target.stat().st_mode) == 0o644
    assert not any(path.name.startswith(".") for path in tmp_path.iterdir())


def test_prerename_failure_cleans_only_owned_stage(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "published.json"

    def hook(point: str) -> None:
        if point == "BEFORE_RENAME":
            raise RuntimeError("synthetic pre-rename crash")

    monkeypatch.setattr(checker, "_publication_hook", hook)
    with pytest.raises(RuntimeError, match="pre-rename"):
        checker._publish_no_replace(target, b"{}\n", project_root=tmp_path)
    assert not target.exists()
    assert tuple(tmp_path.iterdir()) == ()


def test_postrename_failure_never_rolls_back_canonical_inode(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "published.json"

    def hook(point: str) -> None:
        if point == "AFTER_RENAME":
            raise RuntimeError("synthetic post-rename crash")

    monkeypatch.setattr(checker, "_publication_hook", hook)
    with pytest.raises(RuntimeError, match="post-rename"):
        checker._publish_no_replace(target, b"{}\n", project_root=tmp_path)
    assert target.read_bytes() == b"{}\n"
    assert stat.S_IMODE(target.stat().st_mode) == 0o644


def test_stage_collision_preserves_foreign_inode(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "published.json"
    token = "d" * 32
    foreign = tmp_path / f".{target.name}.publish-{token}"
    foreign.write_bytes(b"foreign")
    identity = (foreign.stat().st_dev, foreign.stat().st_ino)
    monkeypatch.setattr(checker.secrets, "token_hex", lambda _size: token)
    with pytest.raises(checker.CheckError, match="collision exhaustion"):
        checker._publish_no_replace(target, b"{}\n", project_root=tmp_path)
    assert foreign.read_bytes() == b"foreign"
    assert (foreign.stat().st_dev, foreign.stat().st_ino) == identity
    assert not target.exists()


def test_replaced_stage_is_never_unlinked_as_owned_cleanup(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "published.json"
    foreign_path = None

    def hook(point: str) -> None:
        nonlocal foreign_path
        if point == "AFTER_STAGE_FILE_FSYNC":
            foreign_path = next(
                path for path in tmp_path.iterdir() if path.name.startswith(".")
            )
            foreign_path.unlink()
            foreign_path.write_bytes(b"foreign")

    monkeypatch.setattr(checker, "_publication_hook", hook)
    with pytest.raises(checker.CheckError, match="foreign"):
        checker._publish_no_replace(target, b"{}\n", project_root=tmp_path)
    assert foreign_path is not None and foreign_path.read_bytes() == b"foreign"
    assert not target.exists()


def test_parent_inode_swap_before_rename_is_rejected(
    checker, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    parent = tmp_path / "result"
    parent.mkdir()
    moved = tmp_path / "moved"
    target = parent / "published.json"

    def hook(point: str) -> None:
        if point == "BEFORE_RENAME":
            parent.rename(moved)
            parent.mkdir()

    monkeypatch.setattr(checker, "_publication_hook", hook)
    with pytest.raises(checker.CheckError, match="chain changed"):
        checker._publish_no_replace(target, b"{}\n", project_root=tmp_path)
    assert not target.exists()
    assert not any(path.name.startswith(".") for path in moved.iterdir())


def test_same_byte_source_inode_swap_aborts_checker_publication(
    checker, tmp_path: Path, owned_candidate_parent: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    result = tmp_path / checker.V2_RESULT_RELATIVE
    result.mkdir(parents=True)
    source = tmp_path / "source"
    source.write_bytes(b"same")
    payload = checker._checker_payload_from_replay(
        synthetic_formal_replay(checker, tmp_path)
    )
    raw = checker.canonical_json_bytes(payload)
    candidate = owned_candidate_parent / checker.V2_CHECKER_OUTPUT
    candidate.write_bytes(raw)
    os.chmod(candidate, 0o600)

    def state(_root, _result, *, transient, published):
        info = source.stat()
        return raw, ((str(source), checker._file_identity(info)),)

    def hook(point: str) -> None:
        if point == "AFTER_STAGING_PARENT_FSYNC":
            source.rename(tmp_path / "source-old")
            source.write_bytes(b"same")

    monkeypatch.setattr(checker, "_checker_publication_state", state)
    monkeypatch.setattr(checker, "_publication_hook", hook)
    with pytest.raises(checker.CheckError, match="inode generation changed"):
        checker.publish_checker(
            tmp_path, result, candidate,
            expected_sha256=checker.sha256_bytes(raw),
            authority=checker.PUBLICATION_AUTHORITY,
        )
    assert not (result / checker.V2_CHECKER_OUTPUT).exists()


def test_same_byte_candidate_inode_swap_after_read_is_rejected_atomically(
    checker, tmp_path: Path, owned_candidate_parent: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    result = tmp_path / checker.V2_RESULT_RELATIVE
    result.mkdir(parents=True)
    payload = checker._checker_payload_from_replay(
        synthetic_formal_replay(checker, tmp_path)
    )
    raw = checker.canonical_json_bytes(payload)
    candidate = owned_candidate_parent / checker.V2_CHECKER_OUTPUT
    candidate.write_bytes(raw)
    os.chmod(candidate, 0o600)
    old_candidate = owned_candidate_parent / "old-candidate"
    swapped = False

    def swap_after_read(point: str, path: Path) -> None:
        nonlocal swapped
        if point == "AFTER_READ" and path == candidate and not swapped:
            swapped = True
            candidate.rename(old_candidate)
            candidate.write_bytes(raw)
            os.chmod(candidate, 0o600)

    monkeypatch.setattr(checker, "_pinned_reader_hook", swap_after_read)
    with pytest.raises(checker.CheckError, match="changed during pinned read"):
        checker.publish_checker(
            tmp_path,
            result,
            candidate,
            expected_sha256=checker.sha256_bytes(raw),
            authority=checker.PUBLICATION_AUTHORITY,
        )
    assert swapped is True
    assert not (result / checker.V2_CHECKER_OUTPUT).exists()
    assert not any(path.name.startswith(".") for path in result.iterdir())
    assert candidate.read_bytes() == raw
    assert old_candidate.read_bytes() == raw


def test_two_fork_publication_has_exactly_one_winner(checker, tmp_path: Path) -> None:
    target = tmp_path / "published.json"
    ready_read, ready_write = os.pipe()
    release_read, release_write = os.pipe()
    first = os.fork()
    if first == 0:
        try:
            os.close(ready_read)
            os.close(release_write)

            def hook(point: str) -> None:
                if point == "AFTER_STAGE_WRITE":
                    os.write(ready_write, b"1")
                    os.read(release_read, 1)

            checker._publication_hook = hook
            checker._publish_no_replace(target, b"first\n", project_root=tmp_path)
            os._exit(0)
        except BaseException:
            os._exit(10)
    os.close(ready_write)
    os.close(release_read)
    assert os.read(ready_read, 1) == b"1"
    second = os.fork()
    if second == 0:
        try:
            checker._publish_no_replace(target, b"second\n", project_root=tmp_path)
        except checker.CheckError:
            os._exit(0)
        except BaseException:
            os._exit(11)
        os._exit(12)
    _, second_status = os.waitpid(second, 0)
    os.write(release_write, b"1")
    _, first_status = os.waitpid(first, 0)
    os.close(ready_read)
    os.close(release_write)
    assert os.waitstatus_to_exitcode(first_status) == 0
    assert os.waitstatus_to_exitcode(second_status) == 0
    assert target.read_bytes() == b"first\n"


def test_cli_is_strict_xor_lexical_and_zero_write_on_failure(
    checker, tmp_path: Path
) -> None:
    with pytest.raises(SystemExit):
        checker.parse_args([])
    with pytest.raises(SystemExit):
        checker.parse_args(["--verify-checker", "--verify-postcheck"])
    with pytest.raises(SystemExit):
        checker.parse_args([
            "--build-checker-candidate", str(tmp_path / "." / "candidate") + "/..",
        ])
    result = tmp_path / checker.V2_RESULT_RELATIVE
    before = tuple(tmp_path.rglob("*"))
    assert checker.main([
        "--verify-checker", "--project-root", str(tmp_path),
        "--result-root", str(result),
        "--publication-authority", checker.PUBLICATION_AUTHORITY,
    ]) == 1
    assert tuple(tmp_path.rglob("*")) == before


def test_checker_source_has_no_scheduler_evaluator_release_or_subprocess_import() -> None:
    imported = set()
    for node in ast.walk(ast.parse(CHECKER_SOURCE.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module)
    assert "subprocess" not in imported
    assert not any(
        name.startswith((
            "run_r401", "evaluate_r401", "check_r401", "build_r401",
        ))
        for name in imported
    )


def test_role11_environment_is_exact14_and_remote_config_is_disabled(checker) -> None:
    assert checker.PREFREEZE_CLEAN_ENVIRONMENT == {
        "PATH": "/root/miniconda3/bin:/usr/bin:/bin",
        "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC",
        "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1", "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1", "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": "/dev/null",
    }


@pytest.mark.parametrize("delta_kind", (6, 7))
def test_pure_git_real_ofs_ref_delta_and_malformed_instruction_size(
    checker, delta_kind: int,
) -> None:
    git_dir, _prefix = checker._git_context(checker.ROOT)
    catalog, _offsets = checker._git_pack_catalog(git_dir)
    oid, pack, offset = next(
        (oid, pack, offset)
        for oid, (pack, offset) in catalog.items()
        if ((pack.raw[offset] >> 4) & 7) == delta_kind
    )
    kind, payload = checker._git_read_object(git_dir, oid, catalog)
    assert checker.hashlib.sha1(
        checker._git_object_frame(kind, payload), usedforsecurity=False
    ).hexdigest() == oid
    corrupted = bytearray(pack.raw)
    corrupted[offset] = (
        (corrupted[offset] & 0xF0) | ((corrupted[offset] + 1) & 0x0F)
    )
    forged = checker._GitPack(bytes(corrupted), pack.oid_by_offset)
    with pytest.raises(checker.CheckError, match="instruction size"):
        checker._git_pack_entry(forged, offset, catalog, set())


@pytest.mark.parametrize(
    "mutation",
    (
        "missing", "extra", "candidate_hash", "input_hash", "size_bool",
        "promotion_integer", "written_integer", "status", "authority",
    ),
)
def test_role54_exact7_receipt_rejects_closed_schema_type_and_hash_attacks(
    checker, mutation: str,
) -> None:
    raw = b"{}\n"
    rows = [{"role": "synthetic", "path": "synthetic/input", "sha256": "a" * 64}]
    receipt = {
        "verification_status": "PASS_MAIN_FREEZE_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": checker.sha256_bytes(raw),
        "input_map_sha256": checker.sha256_bytes(checker.canonical_json_bytes(rows)),
        "size_bytes": len(raw),
        "promotion_authorized": False,
        "artifacts_written": False,
    }
    if mutation == "missing":
        del receipt["input_map_sha256"]
    elif mutation == "extra":
        receipt["protocol_id"] = checker.PROTOCOL_ID
    elif mutation == "candidate_hash":
        receipt["candidate_sha256"] = "0" * 64
    elif mutation == "input_hash":
        receipt["input_map_sha256"] = "0" * 64
    elif mutation == "size_bool":
        receipt["size_bytes"] = True
    elif mutation == "promotion_integer":
        receipt["promotion_authorized"] = 0
    elif mutation == "written_integer":
        receipt["artifacts_written"] = 0
    elif mutation == "status":
        receipt["verification_status"] = "PASS_INDEPENDENT_CHECKER"
    else:
        receipt["authority"] = "INDEPENDENT_CHECKER"
    with pytest.raises(checker.CheckError):
        checker.validate_main_verify_receipt(receipt, raw, rows)
