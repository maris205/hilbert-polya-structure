from __future__ import annotations

import importlib.util
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
    target.write_bytes(MODULE.canonical_json_bytes({"tree": tree.payload()}))
    manifest = {
        "tree": tree.payload(),
        "tree_file": target.relative_to(output).as_posix(),
        "tree_sha256": MODULE.sha256(target),
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    manifest_path = MODULE.tree_manifest_path(output, tree)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(MODULE.canonical_json_bytes(manifest))


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
    matrix = (MODULE.TreeKey(128, "S000"), MODULE.TreeKey(256, "S000"))
    duplicate = [matrix[0].payload(), matrix[0].payload()]
    with pytest.raises(MODULE.MatrixContractError, match="duplicate or missing"):
        MODULE.validate_summary_matrix(duplicate, matrix)
    reversed_entries = [matrix[1].payload(), matrix[0].payload()]
    with pytest.raises(MODULE.MatrixContractError, match="order/matrix"):
        MODULE.validate_summary_matrix(reversed_entries, matrix)


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
