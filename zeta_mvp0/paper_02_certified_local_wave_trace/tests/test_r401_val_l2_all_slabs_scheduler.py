from __future__ import annotations

import importlib.util
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/run_r401_val_l2_all_slabs.py"
MOCK_EVALUATOR = "/mock/capd_r401_local_complement_mp"
SPEC = importlib.util.spec_from_file_location("r401_val_l2_all_slabs", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def dummy_hash(character: str) -> str:
    return character * 64


def make_task(
    *,
    tree: object | None = None,
    node_id: str = "C0L",
    parent_id: str | None = None,
    depth: int = 0,
) -> object:
    key = tree or MODULE.TreeKey(128, "S000")
    return MODULE.make_node_task(
        tree=key,
        node_id=node_id,
        parent_id=parent_id,
        depth=depth,
        epsilon=(Decimal("0"), Decimal("0.0021")),
        box={
            "q_slow": (Decimal("-0.02"), Decimal("-0.001")),
            "q_fast": (Decimal("0.12"), Decimal("0.17")),
            "p_slow": (Decimal("-0.08"), Decimal("0.08")),
            "period": (Decimal("0.64"), Decimal("0.69")),
        },
        evaluator_path=MOCK_EVALUATOR,
        run_config_sha256=dummy_hash("a"),
        evaluator_source_sha256=dummy_hash("b"),
        evaluator_binary_sha256=dummy_hash("c"),
    )


def terminal_outcome(status: str = "RETURN_EXCLUDED", wall: float = 1.0) -> object:
    return MODULE.EvaluatorOutcome(
        stdout=f"status={status}\n",
        stderr="",
        returncode=0,
        timed_out=False,
        wall_seconds=wall,
    )


def write_minimal_tree_commit(output: Path, tree: object) -> None:
    target = MODULE.tree_path(output, tree)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(
        MODULE.canonical_json_bytes(
            {
                "schema_version": MODULE.SCHEMA_VERSION,
                "protocol_id": MODULE.PROTOCOL_ID,
                "licensing": "FROZEN_PRODUCTION",
                "scientific_licensing_enabled": True,
                "producer_state": "FROZEN_TREE_ARCHIVED",
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
                "tree": tree.payload(),
                "nodes": [],
            }
        )
    )
    manifest = {
        "schema_version": MODULE.SCHEMA_VERSION,
        "protocol_id": MODULE.PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_TREE_COMMITTED",
        "tree": tree.payload(),
        "tree_file": target.relative_to(output).as_posix(),
        "tree_sha256": MODULE.sha256(target),
        "node_files": {},
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    manifest_path = MODULE.tree_manifest_path(output, tree)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(MODULE.canonical_json_bytes(manifest))


def write_synthetic_formal_freeze(
    tmp_path: Path,
) -> tuple[Path, Path, Path, dict[str, object]]:
    project = tmp_path / "synthetic-project"
    project.mkdir()
    input_hashes: dict[str, str] = {}
    for index, relative in enumerate(MODULE.MANDATORY_FROZEN_INPUTS):
        target = project / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if relative == "scripts/run_r401_val_l2_all_slabs.py":
            target.write_bytes(SCRIPT.read_bytes())
        elif relative == "scripts/check_r401_val_l2_all_slabs_independent.py":
            target.write_bytes(MODULE.CHECKER.read_bytes())
        elif relative == "validated/capd_r401_local_complement_mp.cpp":
            target.write_bytes(MODULE.SOURCE.read_bytes())
        elif relative.endswith("R401_VAL_L2_A1_MACHINE_FREEZE.json"):
            target.write_bytes(
                MODULE.canonical_json_bytes(
                    {
                        "schema_version": MODULE.SCHEMA_VERSION,
                        "protocol_id": MODULE.PROTOCOL_ID,
                        "status": MODULE.EXPECTED_FREEZE_STATUS,
                        "scientific_licensing_enabled": True,
                        "machine_requirements": dict(
                            MODULE.EXPECTED_MACHINE_REQUIREMENTS
                        ),
                    }
                )
            )
        elif relative == MODULE.PREFREEZE_REVIEW_RELATIVE:
            target.write_text(
                "# Independent pre-freeze review\n\n"
                f"{MODULE.PREFREEZE_ACCEPT_MARKER}\n",
                encoding="utf-8",
            )
        elif relative in {MODULE.S0_REPLAY_RELATIVE, MODULE.S0_ADAPTER_RELATIVE}:
            target.write_bytes((ROOT / relative).read_bytes())
        else:
            target.write_text(f"synthetic frozen input {index}\n", encoding="utf-8")
        input_hashes[relative] = hashlib.sha256(target.read_bytes()).hexdigest()

    for relative in (
        f"{MODULE.S0_RESULT_RELATIVE}/RELEASE_PROVENANCE.json",
        f"{MODULE.S0_RESULT_RELATIVE}/manifest.json",
        f"{MODULE.S0_RESULT_RELATIVE}/POSTCHECK_STATUS.json",
    ):
        target = project / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / relative).read_bytes())

    binary = project / "validated/capd_r401_local_complement_mp.synthetic"
    binary.write_bytes(b"synthetic frozen evaluator\n")
    scheduler = {
        "policy": MODULE.EXPECTED_SCHEDULER_POLICY,
        "workers": 24,
        "node_timeout_seconds": 7200,
        "global_scientific_budget": None,
        "max_inflight_per_tree": 1,
    }
    evaluator = {
        "source_file": "validated/capd_r401_local_complement_mp.cpp",
        "source_sha256": input_hashes[
            "validated/capd_r401_local_complement_mp.cpp"
        ],
        "binary_file": str(binary),
        "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(),
        "capd_commit": MODULE.EXPECTED_CAPD_COMMIT,
        "capd_flags": [
            "-D__HAVE_MPFR__",
            "-frounding-math",
            "-lmpfr",
            "-lgmp",
        ],
        "status_returncode_whitelist": MODULE.formal_status_whitelist(),
    }
    payload: dict[str, object] = {
        "schema_version": MODULE.SCHEMA_VERSION,
        "protocol_id": MODULE.PROTOCOL_ID,
        "status": MODULE.EXPECTED_FREEZE_STATUS,
        "scientific_licensing_enabled": True,
        "checker_mode": MODULE.EXPECTED_CHECKER_MODE,
        "checker_source_sha256": input_hashes[
            "scripts/check_r401_val_l2_all_slabs_independent.py"
        ],
        "matrix": [
            MODULE.TreeKey(bits, f"S{index:03d}").payload()
            for bits in MODULE.PRECISIONS
            for index in range(51)
        ],
        "per_tree_limits": {"max_depth": 48, "max_nodes": 20_000},
        "scheduler": scheduler,
        "logical_thresholds": dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS),
        "machine_requirements": dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
        "evaluator": evaluator,
        "input_hashes": input_hashes,
    }
    freeze = project / "research/route_a_wave_trace/freeze.synthetic.json"
    freeze.write_bytes(MODULE.canonical_json_bytes(payload))
    return project, freeze, binary, payload


def test_exact_102_matrix_is_canonical_and_matches_the_plan() -> None:
    records = MODULE.load_plan_records()
    matrix = MODULE.exact_production_matrix(records)
    assert len(records) == 51
    assert tuple(records) == tuple(f"S{index:03d}" for index in range(51))
    assert len(matrix) == len(set(matrix)) == 102
    assert matrix == tuple(
        MODULE.TreeKey(bits, f"S{index:03d}")
        for bits in (128, 256)
        for index in range(51)
    )
    assert matrix[0].label == "128:S000"
    assert matrix[-1].label == "256:S050"


def test_round_robin_admission_is_fair_across_all_102_trees() -> None:
    records = MODULE.load_plan_records()
    matrix = MODULE.exact_production_matrix(records)
    queue = MODULE.FairNodeQueue(matrix)
    for tree in matrix:
        # Two distinct synthetic tasks are enough to expose a scheduler that
        # drains one tree before advancing to its neighbor.
        queue.extend(
            tree,
            (
                make_task(tree=tree, node_id="C0L"),
                make_task(tree=tree, node_id="C0U"),
            ),
        )
    first_round = queue.pop_batch(102)
    second_round = queue.pop_batch(102)
    assert [task.tree for task in first_round] == list(matrix)
    assert [task.tree for task in second_round] == list(matrix)
    assert len({task.tree for task in first_round}) == 102
    assert not queue


@pytest.mark.parametrize("tree_count", (1, 2, 3))
def test_barrier_never_admits_two_nodes_from_one_tree_when_workers_exceed_trees(
    tree_count: int,
) -> None:
    matrix = tuple(
        MODULE.TreeKey(128, f"S{index:03d}") for index in range(tree_count)
    )
    queue = MODULE.FairNodeQueue(matrix)
    for tree in matrix:
        queue.extend(
            tree,
            (
                make_task(tree=tree, node_id="C0L"),
                make_task(tree=tree, node_id="C0U"),
                make_task(tree=tree, node_id="C1L"),
            ),
        )
    for _ in range(3):
        batch = queue.pop_batch(24)
        assert len(batch) == tree_count
        assert len({task.tree for task in batch}) == tree_count
    assert not queue


def test_queue_rejects_scheduling_the_same_tree_node_twice() -> None:
    tree = MODULE.TreeKey(128, "S000")
    queue = MODULE.FairNodeQueue((tree,))
    task = make_task(tree=tree)
    queue.extend(tree, (task,))
    with pytest.raises(MODULE.SchedulerContractError, match="more than once"):
        queue.extend(tree, (task,))


def test_atomic_run_config_and_strict_resume_binding(tmp_path: Path) -> None:
    output = tmp_path / "generation"
    binding = {
        "protocol_id": MODULE.PROTOCOL_ID,
        "matrix": [MODULE.TreeKey(128, "S000").payload()],
        "per_tree_limits": {"max_depth": 40, "max_nodes": 20000},
    }
    config, config_hash = MODULE.ensure_run_config(output, binding, resume=False)
    assert config["binding"] == binding
    assert config["protocol_id"] == MODULE.PROTOCOL_ID
    assert config["licensing"] == "FROZEN_PRODUCTION"
    assert config["scientific_licensing_enabled"] is True
    assert config["producer_state"] == "FROZEN_GENERATION_INITIALIZED"
    assert config["milestone_status"] is None
    assert config["theorem_status"] is None
    assert config["final_status"] is None
    assert MODULE.sha256(output / "run_config.json") == config_hash
    assert not list(output.glob(".*.tmp-*"))

    resumed, resumed_hash = MODULE.ensure_run_config(output, binding, resume=True)
    assert resumed == config
    assert resumed_hash == config_hash
    changed = json.loads(json.dumps(binding))
    changed["per_tree_limits"]["max_nodes"] = 20001
    with pytest.raises(MODULE.ResumeBindingError):
        MODULE.ensure_run_config(output, changed, resume=True)
    # A mismatch preserves the original immutable generation.
    assert MODULE.strict_json_load(output / "run_config.json") == config

    unbound = tmp_path / "nonempty-unbound"
    unbound.mkdir()
    (unbound / "foreign.txt").write_text("preserve me", encoding="utf-8")
    with pytest.raises(MODULE.ResumeBindingError, match="nonempty unbound"):
        MODULE.ensure_run_config(unbound, binding, resume=False)


def test_incompatible_generation_quarantine_is_whole_recoverable_and_nonmixing(
    tmp_path: Path,
) -> None:
    output = tmp_path / "formal-generation"
    old_binding = {"protocol_id": MODULE.PROTOCOL_ID, "generation": "old"}
    expected_binding = {"protocol_id": MODULE.PROTOCOL_ID, "generation": "new"}
    _old_config, _old_hash = MODULE.ensure_run_config(
        output, old_binding, resume=False
    )
    sentinel = b"old proof bytes must remain exact\x00\xff"
    (output / "old-proof.bin").write_bytes(sentinel)
    old_config_bytes = (output / "run_config.json").read_bytes()

    quarantine = MODULE.quarantine_incompatible_generation(
        output, expected_binding
    )
    assert not output.exists()
    assert quarantine.parent == output.parent
    assert (quarantine / "old-proof.bin").read_bytes() == sentinel
    assert (quarantine / "run_config.json").read_bytes() == old_config_bytes
    record = MODULE.strict_json_load(quarantine / "QUARANTINE_RECORD.json")
    assert record["reason"] == "RUN_CONFIG_BINDING_MISMATCH"
    assert record["milestone_status"] is None
    assert record["theorem_status"] is None
    assert record["final_status"] is None

    fresh, _fresh_hash = MODULE.ensure_run_config(
        output, expected_binding, resume=False
    )
    assert fresh["binding"] == expected_binding
    assert not (output / "old-proof.bin").exists()
    assert (quarantine / "old-proof.bin").read_bytes() == sentinel
    with pytest.raises(MODULE.ResumeBindingError, match="binding-compatible"):
        MODULE.quarantine_incompatible_generation(output, expected_binding)


@pytest.mark.parametrize(
    ("stored_value", "expected_value"),
    [(1, 1.0), (1, True)],
    ids=("integer-versus-float", "integer-versus-boolean"),
)
def test_quarantine_treats_json_numeric_types_as_distinct(
    tmp_path: Path,
    stored_value: object,
    expected_value: object,
) -> None:
    output = tmp_path / "typed-generation"
    stored = {"protocol_id": MODULE.PROTOCOL_ID, "typed_value": stored_value}
    expected = {"protocol_id": MODULE.PROTOCOL_ID, "typed_value": expected_value}
    MODULE.ensure_run_config(output, stored, resume=False)
    with pytest.raises(MODULE.ResumeBindingError):
        MODULE.ensure_run_config(output, expected, resume=True)
    quarantine = MODULE.quarantine_incompatible_generation(output, expected)
    assert quarantine.is_dir()
    assert not output.exists()
    assert MODULE.strict_json_load(quarantine / "run_config.json")["binding"] == stored


def test_original_scheduler_path_symlink_components_are_rejected(
    tmp_path: Path,
) -> None:
    target = tmp_path / "real"
    target.mkdir()
    evaluator = target / "evaluator"
    evaluator.write_text("synthetic\n", encoding="utf-8")
    leaf_link = tmp_path / "evaluator-link"
    leaf_link.symlink_to(evaluator)
    with pytest.raises(MODULE.SchedulerContractError, match="symlink component"):
        MODULE.checked_lexical_path(
            leaf_link,
            label="evaluator",
            require_file=True,
        )

    parent_link = tmp_path / "linked-parent"
    parent_link.symlink_to(target, target_is_directory=True)
    with pytest.raises(MODULE.SchedulerContractError, match="symlink component"):
        MODULE.checked_lexical_path(
            parent_link / "evaluator",
            label="evaluator",
            require_file=True,
        )


def test_transactional_node_commit_binds_raw_and_rejects_corruption(
    tmp_path: Path,
) -> None:
    task = make_task()
    outcome = MODULE.EvaluatorOutcome(
        stdout="precision_bits=128\nstatus=UNKNOWN\n",
        stderr="diagnostic\n",
        returncode=2,
        wall_seconds=0.1,
    )
    record = MODULE.commit_node_transaction(
        tmp_path, task, outcome, max_depth=40
    )
    directory = MODULE.node_commit_directory(tmp_path, task)
    assert directory.is_dir()
    assert {path.name for path in directory.iterdir()} == {
        "stdout.txt",
        "stderr.txt",
        "telemetry.json",
        "record.json",
    }
    assert record["evaluator_result"]["classification"] == "SPLIT"
    assert record["invocation"]["argv"] == [
        MOCK_EVALUATOR,
        "128",
        "0",
        "0.0021",
        "-0.02",
        "-0.001",
        "0.12",
        "0.17",
        "-0.08",
        "0.08",
        "0.64",
        "0.69",
    ]
    assert record["invocation"]["argv_sha256"] == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(record["invocation"]["argv"])
    )
    assert MODULE.validate_committed_node(tmp_path, task, max_depth=40) == record
    assert not list(directory.parent.glob(f".{task.node_id}.tmp-*"))

    with pytest.raises(MODULE.CorruptShardError, match="second, different commit"):
        MODULE.commit_node_transaction(
            tmp_path,
            task,
            MODULE.EvaluatorOutcome(
                stdout="status=RETURN_EXCLUDED\n",
                stderr="",
                returncode=0,
            ),
            max_depth=40,
        )

    (directory / "stdout.txt").write_text("status=RETURN_EXCLUDED\n", encoding="utf-8")
    with pytest.raises(MODULE.CorruptShardError, match="stdout hash mismatch"):
        MODULE.validate_committed_node(tmp_path, task, max_depth=40)


@pytest.mark.parametrize(
    "mutation",
    ("missing", "order", "endpoint", "path", "hash"),
)
def test_invocation_argv_mutations_are_rejected(
    tmp_path: Path,
    mutation: str,
) -> None:
    task = make_task()
    MODULE.commit_node_transaction(
        tmp_path,
        task,
        terminal_outcome(),
        max_depth=40,
    )
    record_path = MODULE.node_record_path(tmp_path, task)
    payload = MODULE.strict_json_load(record_path)
    if mutation == "missing":
        del payload["invocation"]
    elif mutation == "order":
        payload["invocation"]["argv"][2], payload["invocation"]["argv"][3] = (
            payload["invocation"]["argv"][3],
            payload["invocation"]["argv"][2],
        )
    elif mutation == "endpoint":
        payload["invocation"]["argv"][4] = "-0.019999"
    elif mutation == "path":
        payload["invocation"]["argv"][0] = "/mock/different-evaluator"
    elif mutation == "hash":
        payload["invocation"]["argv_sha256"] = dummy_hash("f")
    else:  # pragma: no cover - parametrization is closed above
        raise AssertionError(mutation)
    MODULE.atomic_write_json(record_path, payload)
    with pytest.raises(MODULE.CorruptShardError, match="invocation"):
        MODULE.validate_committed_node(tmp_path, task, max_depth=40)


def test_resume_ignores_uncommitted_hidden_transaction_but_rejects_orphan_commit(
    tmp_path: Path,
) -> None:
    hidden = tmp_path / "raw/128/S000/.C0L.tmp-interrupted"
    hidden.mkdir(parents=True)
    (hidden / "record.json").write_text('{"partial": true}\n', encoding="utf-8")
    assert MODULE.scan_committed_node_records(tmp_path) == {}

    orphan_task = make_task(node_id="C0L0", parent_id="C0L", depth=1)
    MODULE.commit_node_transaction(
        tmp_path, orphan_task, terminal_outcome(), max_depth=40
    )
    records = MODULE.load_plan_records()
    with pytest.raises(MODULE.CorruptShardError, match="orphan/unreachable"):
        MODULE.reconstruct_trees(
            tmp_path,
            (MODULE.TreeKey(128, "S000"),),
            records,
            evaluator_path=MOCK_EVALUATOR,
            run_config_sha256=dummy_hash("a"),
            evaluator_source_sha256=dummy_hash("b"),
            evaluator_binary_sha256=dummy_hash("c"),
            max_depth=40,
        )


@pytest.mark.parametrize(
    ("status", "returncode", "expected"),
    [
        ("ENERGY_EXCLUDED", 0, "ENERGY_EXCLUDED"),
        ("RETURN_EXCLUDED", 0, "RETURN_EXCLUDED"),
        ("UNKNOWN", 2, "SPLIT"),
        ("ENERGY_DERIVATIVE_FAIL", 3, "SPLIT"),
        ("ENERGY_GUARD_FAIL", 3, "SPLIT"),
        ("FLOW_FAIL", 3, "SPLIT"),
        ("ROOT_CANDIDATE", 4, "ROOT_CANDIDATE"),
        (
            "INVALID_EXCLUSION_UNIQUENESS_CONFLICT",
            5,
            "INVALID_EVALUATOR_CONFLICT",
        ),
        ("UNKNOWN", 0, "INVALID_EVALUATOR_RESULT"),
        ("NO_STATUS", 2, "INVALID_EVALUATOR_RESULT"),
    ],
)
def test_status_returncode_mapping_is_an_exact_whitelist(
    status: str, returncode: int, expected: str
) -> None:
    result = MODULE.classify_outcome(
        make_task(),
        MODULE.EvaluatorOutcome(
            stdout=f"status={status}\n" if status != "NO_STATUS" else "",
            stderr="",
            returncode=returncode,
        ),
        max_depth=40,
    )
    assert result["classification"] == expected


def test_repeated_status_or_boolean_returncode_is_malformed() -> None:
    task = make_task()
    repeated = MODULE.classify_outcome(
        task,
        MODULE.EvaluatorOutcome(
            "status=UNKNOWN\nstatus=UNKNOWN\n", "", 2
        ),
        max_depth=40,
    )
    boolean_code = MODULE.classify_outcome(
        task,
        MODULE.EvaluatorOutcome("status=RETURN_EXCLUDED\n", "", False),
        max_depth=40,
    )
    assert repeated["classification"] == "INVALID_EVALUATOR_RESULT"
    assert boolean_code["classification"] == "INVALID_EVALUATOR_RESULT"


def test_exact_tree_matrix_rejects_missing_duplicate_extra_and_symlink(
    tmp_path: Path,
) -> None:
    records = MODULE.load_plan_records()
    matrix = MODULE.exact_production_matrix(records)
    for tree in matrix:
        write_minimal_tree_commit(tmp_path, tree)
    hidden_partial = tmp_path / "trees/128/.S000.json.tmp-interrupted"
    hidden_partial.write_text("partial", encoding="utf-8")
    manifests = MODULE.validate_tree_commit_matrix(
        tmp_path, matrix, require_complete=True
    )
    assert len(manifests) == 102

    missing = MODULE.tree_manifest_path(tmp_path, matrix[-1])
    missing_bytes = missing.read_bytes()
    missing.unlink()
    with pytest.raises(MODULE.MatrixContractError, match="missing canonical"):
        MODULE.validate_tree_commit_matrix(tmp_path, matrix, require_complete=True)
    missing.write_bytes(missing_bytes)

    extra = tmp_path / "tree_manifests/128/S000.copy.json"
    extra.write_bytes(MODULE.tree_manifest_path(tmp_path, matrix[0]).read_bytes())
    with pytest.raises(MODULE.MatrixContractError, match="unexpected canonical"):
        MODULE.validate_tree_commit_matrix(tmp_path, matrix, require_complete=True)
    extra.unlink()

    symlink = MODULE.tree_manifest_path(tmp_path, matrix[0])
    saved = symlink.read_bytes()
    symlink.unlink()
    symlink.symlink_to(MODULE.tree_manifest_path(tmp_path, matrix[1]))
    with pytest.raises(MODULE.MatrixContractError, match="non-regular authoritative"):
        MODULE.validate_tree_commit_matrix(tmp_path, matrix, require_complete=True)
    symlink.unlink()
    symlink.write_bytes(saved)


def test_duplicate_json_keys_and_noncanonical_summary_entries_are_rejected() -> None:
    with pytest.raises(MODULE.CorruptShardError, match="duplicate JSON key"):
        MODULE.strict_json_loads('{"tree": 1, "tree": 2}')
    with pytest.raises(MODULE.CorruptShardError, match="non-finite JSON number"):
        MODULE.strict_json_loads('{"x": 1e400}')
    matrix = (MODULE.TreeKey(128, "S000"), MODULE.TreeKey(256, "S000"))
    duplicate = [matrix[0].payload(), matrix[0].payload()]
    with pytest.raises(MODULE.MatrixContractError, match="duplicate or missing"):
        MODULE.validate_summary_matrix(duplicate, matrix)
    reversed_entries = [matrix[1].payload(), matrix[0].payload()]
    with pytest.raises(MODULE.MatrixContractError, match="order/matrix"):
        MODULE.validate_summary_matrix(reversed_entries, matrix)
    coercible = [matrix[0].payload(), matrix[1].payload()]
    coercible[0]["precision_bits"] = 128.0
    with pytest.raises(MODULE.MatrixContractError, match="malformed aggregate"):
        MODULE.validate_summary_matrix(coercible, matrix)


@pytest.mark.parametrize("unsafe", ["./a.json", "a//b.json", "a/"])
def test_frozen_input_path_normalization_aliases_are_rejected(unsafe: str) -> None:
    with pytest.raises(MODULE.CorruptShardError, match="unsafe|non-canonical"):
        MODULE.safe_relative_path(unsafe)


@pytest.mark.parametrize(
    ("field", "value"),
    [("schema_version", True), ("matrix_precision", 128.0)],
)
def test_formal_freeze_rejects_coercible_exact_contract_types(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    project, freeze, _binary, payload = write_synthetic_formal_freeze(tmp_path)
    if field == "schema_version":
        payload["schema_version"] = value
    else:
        payload["matrix"][0]["precision_bits"] = value
    freeze.write_bytes(MODULE.canonical_json_bytes(payload))
    with pytest.raises((MODULE.SchedulerContractError, MODULE.MatrixContractError)):
        MODULE.validate_formal_freeze(freeze, project_root=project)


def test_tree_and_manifest_are_invariant_to_completion_order_and_wall_time(
    tmp_path: Path,
) -> None:
    tree = MODULE.TreeKey(128, "S000")
    task_a = make_task(tree=tree, node_id="C0L")
    task_b = make_task(tree=tree, node_id="C0U")
    outputs = (tmp_path / "forward", tmp_path / "reverse")
    orders = ((task_a, task_b), (task_b, task_a))
    walls = ((0.1, 9.0), (99.0, 0.001))
    records_by_output: list[list[dict[str, object]]] = []
    for output, order, timings in zip(outputs, orders, walls, strict=True):
        records_for_tree: list[dict[str, object]] = []
        for task, wall in zip(order, timings, strict=True):
            records_for_tree.append(
                MODULE.commit_node_transaction(
                    output,
                    task,
                    terminal_outcome(wall=wall),
                    max_depth=40,
                )
            )
        records_by_output.append(records_for_tree)
        MODULE.finalize_tree_transaction(
            output,
            tree,
            MODULE.load_plan_records()["S000"],
            records_for_tree,
            run_config_sha256=dummy_hash("a"),
            max_depth=40,
            max_nodes=20_000,
        )

    assert MODULE.tree_path(outputs[0], tree).read_bytes() == MODULE.tree_path(
        outputs[1], tree
    ).read_bytes()
    assert MODULE.tree_manifest_path(
        outputs[0], tree
    ).read_bytes() == MODULE.tree_manifest_path(outputs[1], tree).read_bytes()
    manifest = MODULE.strict_json_load(MODULE.tree_manifest_path(outputs[0], tree))
    tree_payload = MODULE.strict_json_load(MODULE.tree_path(outputs[0], tree))
    tree_invocations = {
        node["task"]["node_id"]: node["invocation"]
        for node in tree_payload["nodes"]
    }
    for node_id, invocation in tree_invocations.items():
        assert manifest["node_files"][node_id]["argv_sha256"] == invocation[
            "argv_sha256"
        ]
    # Telemetry is intentionally allowed to differ without entering either
    # canonical proof object.
    assert (
        MODULE.node_commit_directory(outputs[0], task_a) / "telemetry.json"
    ).read_bytes() != (
        MODULE.node_commit_directory(outputs[1], task_a) / "telemetry.json"
    ).read_bytes()


def test_mocked_session_commits_parent_before_children_become_resume_frontier(
    tmp_path: Path,
) -> None:
    records = MODULE.load_plan_records()
    matrix = (MODULE.TreeKey(128, "S000"),)

    def mock_evaluator(
        _binary: Path,
        _task: object,
        *,
        timeout_seconds: int | None,
    ) -> object:
        assert timeout_seconds is None
        return MODULE.EvaluatorOutcome("status=UNKNOWN\n", "", 2, wall_seconds=0.0)

    state = MODULE.run_scheduler_session(
        output=tmp_path,
        evaluator=tmp_path / "unused-mock",
        matrix=matrix,
        plan_records=records,
        run_config_sha256=dummy_hash("a"),
        evaluator_source_sha256=dummy_hash("b"),
        evaluator_binary_sha256=dummy_hash("c"),
        workers=1,
        max_depth=40,
        max_nodes=20_000,
        node_timeout_seconds=None,
        dispatch_limit=1,
        evaluator_function=mock_evaluator,
    )
    assert state["session_dispatch_count"] == 1
    reconstructed = MODULE.reconstruct_trees(
        tmp_path,
        matrix,
        records,
        evaluator_path=str((tmp_path / "unused-mock").resolve()),
        run_config_sha256=dummy_hash("a"),
        evaluator_source_sha256=dummy_hash("b"),
        evaluator_binary_sha256=dummy_hash("c"),
        max_depth=40,
    )[matrix[0]]
    assert "C0L" in reconstructed.records
    assert reconstructed.records["C0L"]["evaluator_result"]["classification"] == "SPLIT"
    pending_ids = {task.node_id for task in reconstructed.pending}
    assert {"C0L0", "C0L1"} <= pending_ids
    assert len(pending_ids) == 9  # two children plus the seven untouched roots


def test_per_tree_budget_is_not_oversubscribed_by_one_parallel_batch(
    tmp_path: Path,
) -> None:
    records = MODULE.load_plan_records()
    matrix = (MODULE.TreeKey(128, "S000"),)

    def mock_terminal(
        _binary: Path,
        _task: object,
        *,
        timeout_seconds: int | None,
    ) -> object:
        assert timeout_seconds is None
        return MODULE.EvaluatorOutcome("status=RETURN_EXCLUDED\n", "", 0)

    state = MODULE.run_scheduler_session(
        output=tmp_path,
        evaluator=tmp_path / "unused-mock",
        matrix=matrix,
        plan_records=records,
        run_config_sha256=dummy_hash("a"),
        evaluator_source_sha256=dummy_hash("b"),
        evaluator_binary_sha256=dummy_hash("c"),
        workers=8,
        max_depth=40,
        max_nodes=1,
        node_timeout_seconds=None,
        dispatch_limit=None,
        evaluator_function=mock_terminal,
    )
    assert state["session_dispatch_count"] == 1
    assert state["tree_states"][0]["evaluated_nodes"] == 1
    assert state["tree_states"][0]["pending_frontier_nodes"] == 7
    assert state["tree_states"][0]["per_tree_node_budget_exhausted"] is True


def test_nominal_but_unsealed_fake_freeze_cannot_unlock_formal_loader(
    tmp_path: Path,
) -> None:
    freeze = tmp_path / "fake-freeze.json"
    freeze.write_bytes(
        MODULE.canonical_json_bytes(
            {
                "schema_version": MODULE.SCHEMA_VERSION,
                "protocol_id": MODULE.PROTOCOL_ID,
                "status": MODULE.EXPECTED_FREEZE_STATUS,
                "scientific_licensing_enabled": True,
                "checker_mode": MODULE.EXPECTED_CHECKER_MODE,
            }
        )
    )
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE.validate_formal_freeze(freeze, project_root=tmp_path)


def test_mandatory_frozen_input_tuple_is_exact_complete_17_chain() -> None:
    expected = (
        "scripts/check_r401_val_l2_all_slabs_independent.py",
        "scripts/run_r401_val_l2_all_slabs.py",
        "validated/capd_r401_local_complement_mp.cpp",
        "validated/CAPD_DEPENDENCY.md",
        "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
        "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md",
        "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json",
        "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md",
        "research/route_a_wave_trace/R401_VAL_L2_A1_S0_COMPATIBILITY_REPLAY.json",
        "scripts/replay_r401_val_l2_s0_through_a1_checker.py",
        "scripts/build_r401_val_l2_a1_release_provenance.py",
        "research/route_a_wave_trace/R401_VAL_L2_A1_RELEASE_PROVENANCE_CONTRACT.md",
        "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
        "results/r401_val_l1_branch/summary.json",
        "results/r401_val_l1_branch/manifest.json",
        "results/r401_val_l1_branch/independent_checker.json",
        "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
    )
    assert MODULE.MANDATORY_FROZEN_INPUTS == expected


@pytest.mark.parametrize("missing", MODULE.MANDATORY_FROZEN_INPUTS)
def test_formal_launch_rejects_each_missing_mandatory_input_hash(
    tmp_path: Path,
    missing: str,
) -> None:
    project, freeze, _binary, payload = write_synthetic_formal_freeze(tmp_path)
    del payload["input_hashes"][missing]
    freeze.write_bytes(MODULE.canonical_json_bytes(payload))
    with pytest.raises(MODULE.SchedulerContractError, match="misses mandatory"):
        MODULE.validate_formal_freeze(freeze, project_root=project)


@pytest.mark.parametrize(
    "mutation",
    ("checker_hash", "manifest_checks", "status_counts", "tree_counts", "s0_hash"),
)
def test_formal_launch_rejects_forged_public_s0_replay_semantics(
    tmp_path: Path,
    mutation: str,
) -> None:
    project, freeze, _binary, payload = write_synthetic_formal_freeze(tmp_path)
    replay_path = project / MODULE.S0_REPLAY_RELATIVE
    replay = MODULE.strict_json_load(replay_path)
    if mutation == "checker_hash":
        replay["checker_source_sha256"] = "0" * 64
    elif mutation == "manifest_checks":
        replay["manifest_hash_checks"] = 1
    elif mutation == "status_counts":
        replay["status_counts"] = {"UNKNOWN": 3016}
    elif mutation == "tree_counts":
        replay["tree_counts"][0]["node_count"] = 485
    elif mutation == "s0_hash":
        replay["s0_release_provenance_sha256"] = "0" * 64
    else:  # pragma: no cover - closed parametrization
        raise AssertionError(mutation)
    replay_path.write_bytes(MODULE.canonical_json_bytes(replay))
    payload["input_hashes"][MODULE.S0_REPLAY_RELATIVE] = hashlib.sha256(
        replay_path.read_bytes()
    ).hexdigest()
    freeze.write_bytes(MODULE.canonical_json_bytes(payload))
    with pytest.raises(MODULE.SchedulerContractError, match="S0 compatibility"):
        MODULE.validate_formal_freeze(freeze, project_root=project)


@pytest.mark.parametrize(
    "review_text",
    (
        "Verdict: PENDING\n",
        "No release verdict has been assigned.\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict: ACCEPT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict: REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict: PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict=PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE\n- Verdict: REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\n> Verdict: PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE\n**Verdict:** REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\n| Verdict | REJECT_FOR_FREEZE |\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict - REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict：PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE \n",
        "Verdict:  ACCEPT_FOR_FREEZE\n",
        "verdict: ACCEPT_FOR_FREEZE\n",
    ),
)
def test_prefreeze_review_semantic_gate_rejects_pending_missing_duplicate_or_near_marker(
    tmp_path: Path,
    review_text: str,
) -> None:
    project, freeze, _binary, payload = write_synthetic_formal_freeze(tmp_path)
    review = project / MODULE.PREFREEZE_REVIEW_RELATIVE
    review.write_text(review_text, encoding="utf-8")
    payload["input_hashes"][MODULE.PREFREEZE_REVIEW_RELATIVE] = hashlib.sha256(
        review.read_bytes()
    ).hexdigest()
    freeze.write_bytes(MODULE.canonical_json_bytes(payload))
    with pytest.raises(
        MODULE.SchedulerContractError,
        match="exactly one exact ACCEPT_FOR_FREEZE",
    ):
        MODULE.validate_formal_freeze(freeze, project_root=project)


def test_prefreeze_review_missing_file_is_rejected_even_if_freeze_names_it(
    tmp_path: Path,
) -> None:
    project, freeze, _binary, _payload = write_synthetic_formal_freeze(tmp_path)
    (project / MODULE.PREFREEZE_REVIEW_RELATIVE).unlink()
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE.validate_formal_freeze(freeze, project_root=project)


@pytest.mark.parametrize(
    "mutation",
    (
        "status",
        "matrix",
        "input_hash",
        "scheduler",
        "limits",
        "thresholds",
        "binary_hash",
        "capd_commit",
        "capd_flags",
        "machine",
    ),
)
def test_every_frozen_contract_or_hash_mutation_is_rejected(
    tmp_path: Path,
    mutation: str,
) -> None:
    project, freeze, _binary, payload = write_synthetic_formal_freeze(tmp_path)
    changed = json.loads(json.dumps(payload))
    if mutation == "status":
        changed["status"] = "DRAFT"
    elif mutation == "matrix":
        changed["matrix"][0], changed["matrix"][1] = (
            changed["matrix"][1],
            changed["matrix"][0],
        )
    elif mutation == "input_hash":
        changed["input_hashes"]["validated/CAPD_DEPENDENCY.md"] = dummy_hash("f")
    elif mutation == "scheduler":
        changed["scheduler"]["max_inflight_per_tree"] = 2
    elif mutation == "limits":
        changed["per_tree_limits"]["max_nodes"] += 1
        changed["per_tree_limits"]["unexpected"] = True
    elif mutation == "thresholds":
        changed["logical_thresholds"]["logical_margin_128"] = "1e-29"
    elif mutation == "binary_hash":
        changed["evaluator"]["binary_sha256"] = dummy_hash("e")
    elif mutation == "capd_commit":
        changed["evaluator"]["capd_commit"] = "0" * 40
    elif mutation == "capd_flags":
        changed["evaluator"]["capd_flags"].remove("-frounding-math")
    elif mutation == "machine":
        changed["machine_requirements"]["cpu_logical"] = 31
    else:  # pragma: no cover
        raise AssertionError(mutation)
    freeze.write_bytes(MODULE.canonical_json_bytes(changed))
    with pytest.raises(MODULE.SchedulerContractError):
        MODULE.validate_formal_freeze(freeze, project_root=project)


def test_formal_freeze_builds_exact_checker_compatible_binding_and_initializes(
    tmp_path: Path,
) -> None:
    project, freeze, binary, payload = write_synthetic_formal_freeze(tmp_path)
    formal = MODULE.validate_formal_freeze(freeze, project_root=project)
    binding = MODULE.build_run_binding(
        plan_records=MODULE.load_plan_records(),
        formal=formal,
    )
    assert binding["protocol_id"] == MODULE.PROTOCOL_ID
    assert binding["licensing"] == "FROZEN_PRODUCTION"
    assert binding["scientific_licensing_enabled"] is True
    assert binding["l2_a1_freeze_sha256"] == MODULE.sha256(freeze)
    assert binding["machine_freeze_sha256"] == payload["input_hashes"][
        "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json"
    ]
    assert binding["machine_requirements"] == MODULE.EXPECTED_MACHINE_REQUIREMENTS
    assert binding["matrix"] == payload["matrix"]
    assert binding["per_tree_limits"] == payload["per_tree_limits"]
    assert binding["scheduler"] == payload["scheduler"]
    assert binding["logical_thresholds"] == payload["logical_thresholds"]
    assert binding["evaluator"] == payload["evaluator"]
    assert binding["input_hashes"] == payload["input_hashes"]

    MODULE.validate_cli_contract(
        formal,
        evaluator=binary,
        capd_commit=MODULE.EXPECTED_CAPD_COMMIT,
        capd_flags=payload["evaluator"]["capd_flags"],
        workers=24,
        max_depth=48,
        max_nodes=20_000,
        node_timeout_seconds=7200,
    )
    output = tmp_path / "initialized-formal-generation"
    config, config_hash = MODULE.ensure_run_config(output, binding, resume=False)
    assert config["producer_state"] == "FROZEN_GENERATION_INITIALIZED"
    assert config["milestone_status"] is None
    assert config["theorem_status"] is None
    assert config["final_status"] is None
    assert config_hash == MODULE.sha256(output / "run_config.json")


def test_formal_archive_namespace_never_assigns_scientific_status(
    tmp_path: Path,
) -> None:
    task = make_task()
    record = MODULE.commit_node_transaction(
        tmp_path,
        task,
        terminal_outcome(),
        max_depth=48,
    )
    tree = MODULE.build_tree_payload(
        task.tree,
        MODULE.load_plan_records()[task.tree.slab_id],
        (record,),
        run_config_sha256=dummy_hash("a"),
        max_depth=48,
        max_nodes=20_000,
    )
    for payload in (record, tree):
        assert payload["protocol_id"] == MODULE.PROTOCOL_ID
        assert payload["licensing"] == "FROZEN_PRODUCTION"
        assert payload["scientific_licensing_enabled"] is True
        assert payload["milestone_status"] is None
        assert payload["theorem_status"] is None
        assert payload["final_status"] is None


def test_storage_threshold_creates_operational_pause_without_dispatch_or_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    records = MODULE.load_plan_records()
    matrix = (MODULE.TreeKey(128, "S000"),)
    threshold = MODULE.EXPECTED_MACHINE_REQUIREMENTS[
        "operational_pause_below_free_bytes"
    ]
    monkeypatch.setattr(MODULE, "free_bytes", lambda _path: threshold - 1)

    def forbidden_evaluator(*_args: object, **_kwargs: object) -> object:
        raise AssertionError("storage pause must happen before dispatch")

    state = MODULE.run_scheduler_session(
        output=tmp_path / "generation",
        evaluator=tmp_path / "unused-mock",
        matrix=matrix,
        plan_records=records,
        run_config_sha256=dummy_hash("a"),
        evaluator_source_sha256=dummy_hash("b"),
        evaluator_binary_sha256=dummy_hash("c"),
        workers=24,
        max_depth=48,
        max_nodes=20_000,
        node_timeout_seconds=7200,
        dispatch_limit=None,
        operational_pause_below_free_bytes=threshold,
        evaluator_function=forbidden_evaluator,
    )
    assert state["session_dispatch_count"] == 0
    assert state["operational_pause"] is True
    assert state["milestone_status"] is None
    assert state["theorem_status"] is None
    assert state["final_status"] is None
    live = tmp_path / ".operational/generation/live_status.json"
    assert MODULE.strict_json_load(live)["producer_state"] == "OPERATIONAL_STORAGE_PAUSE"
