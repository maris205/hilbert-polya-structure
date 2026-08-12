from __future__ import annotations

import ast
import importlib.util
import json
import math
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
SCHEDULER_SOURCE = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
S0_PROOF = ROOT / "results/r401_val_l3_phase_tube_smoke/proof_128_S000.json"


def load_checker():
    name = "check_r401_val_l3_a1_static_independent_tested"
    spec = importlib.util.spec_from_file_location(name, CHECKER_SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_scheduler():
    name = "r401_val_l3_a1_scheduler_for_static_checker_test"
    spec = importlib.util.spec_from_file_location(name, SCHEDULER_SOURCE)
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
def full_mock_archive(checker, tmp_path: Path):
    scheduler = load_scheduler()
    output = tmp_path / "full-static-mock"
    result = scheduler.run_mock_static(output, 102, resume=False)
    assert result["aggregate_finalized"] is True
    return output, scheduler


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


def test_full_102_cell_mock_checker_and_postcheck_are_nonlicensing(
    checker, full_mock_archive
) -> None:
    output, _scheduler = full_mock_archive
    result = checker.run_checker(output)
    assert set(result) == {
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
    assert result["checker_status"] == "PASS_MOCK_INDEPENDENT_REPLAY"
    assert result["replay_counts"]["cell_directories"] == 102
    assert result["replay_counts"]["cell_manifests"] == 102
    assert result["cross_precision"] == {
        "all_agree": True,
        "mock_only": True,
        "scientific_domain_replay_performed": False,
        "slab_pairs": 51,
        "status_pairs_agree": 51,
    }
    assert result["scientific_licensing_enabled"] is False
    assert result["component_status"] is None
    assert result["milestone_status"] is None
    assert result["theorem_status"] is None
    assert result["final_status"] is None

    checker_path = output / "independent_static_checker.json"
    checker.write_once(checker_path, checker.canonical_json_bytes(result))
    postcheck = checker.run_postcheck(output)
    assert set(postcheck) == {
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
    assert postcheck["postcheck_status"] == "PASS_MOCK_WRITE_ONCE_POSTCHECK"
    assert postcheck["component_status"] is None
    assert postcheck["milestone_status"] is None
    assert postcheck["theorem_status"] is None
    assert postcheck["final_status"] is None
    checker.write_once(
        output / "STATIC_POSTCHECK_STATUS.json",
        checker.canonical_json_bytes(postcheck),
    )
    with pytest.raises(FileExistsError):
        checker.write_once(
            output / "STATIC_POSTCHECK_STATUS.json",
            checker.canonical_json_bytes(postcheck),
        )


def test_full_mock_checker_rejects_manifest_root_and_type_mutations(
    checker, full_mock_archive
) -> None:
    output, _scheduler = full_mock_archive
    summary_path = output / "static/aggregate_summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["ordered_cell_manifest_root"] = "0" * 64
    summary_path.write_bytes(checker.canonical_json_bytes(summary))
    with pytest.raises(checker.CheckError, match="ordered root"):
        checker.run_checker(output)


def test_full_mock_checker_rejects_extra_path_and_live_stage(
    checker, full_mock_archive
) -> None:
    output, scheduler = full_mock_archive
    extra = output / "static/cells/128/S000/hidden.json"
    extra.write_text("{}\n", encoding="utf-8")
    with pytest.raises(checker.CheckError, match="namespace differs"):
        checker.run_checker(output)
    extra.unlink()

    run_config_sha256 = checker.sha256_file(output / "run_config.json")
    stage = (
        output.with_name(output.name + ".operational")
        / "staging/static/128"
        / scheduler.staging_basename(scheduler.CellKey(128, "S000"), run_config_sha256)
    )
    stage.mkdir()
    with pytest.raises(checker.CheckError, match="namespace differs"):
        checker.run_checker(output)


def test_postcheck_rejects_changed_published_checker(
    checker, full_mock_archive
) -> None:
    output, _scheduler = full_mock_archive
    result = checker.run_checker(output)
    result["passed"] = False
    checker.write_once(
        output / "independent_static_checker.json",
        checker.canonical_json_bytes(result),
    )
    with pytest.raises(checker.CheckError, match="published mock static checker"):
        checker.run_postcheck(output)


def test_mock_checker_cli_publication_is_write_once(
    checker, full_mock_archive, tmp_path: Path
) -> None:
    output, _scheduler = full_mock_archive
    outside = tmp_path / "outside-checker.json"
    assert checker.main(
        ["--input-dir", str(output), "--output", str(outside)]
    ) == 1
    assert not outside.exists()
    assert checker.main(["--input-dir", str(output)]) == 0
    checker_bytes = (output / "independent_static_checker.json").read_bytes()
    assert checker.main(["--input-dir", str(output)]) == 1
    assert (output / "independent_static_checker.json").read_bytes() == checker_bytes
    assert checker.main(["--input-dir", str(output), "--postcheck"]) == 0
    postcheck_bytes = (output / "STATIC_POSTCHECK_STATUS.json").read_bytes()
    assert checker.main(["--input-dir", str(output), "--postcheck"]) == 1
    assert (output / "STATIC_POSTCHECK_STATUS.json").read_bytes() == postcheck_bytes
