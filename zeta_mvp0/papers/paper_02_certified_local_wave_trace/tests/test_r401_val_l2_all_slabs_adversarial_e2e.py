from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import random
import shutil
import subprocess
import sys
import threading
import time
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable

import pytest


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "scripts/run_r401_val_l2_all_slabs.py"
CHECKER_PATH = ROOT / "scripts/check_r401_val_l2_all_slabs_independent.py"
S0_ADAPTER_PATH = ROOT / "scripts/replay_r401_val_l2_s0_through_a1_checker.py"


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RUNNER = load_module("r401_val_l2_a1_adversarial_runner", RUNNER_PATH)
CHECKER = load_module("r401_val_l2_a1_adversarial_checker", CHECKER_PATH)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(RUNNER.canonical_json_bytes(payload))


def copy_or_hardlink(source: Path, target: Path) -> None:
    """Materialize an independent regular file without introducing symlinks."""

    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


def make_synthetic_project_root(root: Path, *, name: str) -> Path:
    """Copy the complete frozen/L1 authority DAG and accept only its test copy."""

    project_root = root / f"{name}.project"
    review_relative = RUNNER.PREFREEZE_REVIEW_RELATIVE
    required = set(RUNNER.MANDATORY_FROZEN_INPUTS)
    l1_release = json.loads(
        (ROOT / "results/r401_val_l1_branch/RELEASE_PROVENANCE.json").read_text(
            encoding="utf-8"
        )
    )
    required.update(str(relative) for relative in l1_release["files"])
    for relative in sorted(required - {review_relative}):
        copy_or_hardlink(ROOT / relative, project_root / relative)
    for relative in (
        "results/r401_val_l2_s0_local_complement/RELEASE_PROVENANCE.json",
        "results/r401_val_l2_s0_local_complement/manifest.json",
        "results/r401_val_l2_s0_local_complement/POSTCHECK_STATUS.json",
    ):
        copy_or_hardlink(ROOT / relative, project_root / relative)
    review = project_root / review_relative
    review.parent.mkdir(parents=True, exist_ok=True)
    review.write_text(
        "\n".join(
            [
                "# Synthetic A1 pre-freeze review fixture",
                "",
                "This acceptance exists only below pytest's temporary directory.",
                "It does not alter or authorize the real pending A1 review.",
                "",
                "Verdict: ACCEPT_FOR_FREEZE",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return project_root


def interval_text(lower: Decimal, upper: Decimal) -> str:
    return f"[{RUNNER.decimal_text(lower)},{RUNNER.decimal_text(upper)}]"


def mock_return_excluded_transcript(task: Any) -> str:
    """Emit a small exact proof object accepted by the independent checker."""

    qfast_lower, qfast_upper = task.box["q_fast"]
    midpoint = (qfast_lower + qfast_upper) / 2
    contraction_pad = Decimal("1e-20")
    contracted = midpoint - contraction_pad, midpoint + contraction_pad
    bits = task.tree.precision_bits
    logical_margin = "2e-30" if bits == 128 else "2e-60"
    newton_guard = "1e-40" if bits == 128 else "1e-75"
    qfast_before = interval_text(qfast_lower, qfast_upper)
    qfast_midpoint = interval_text(midpoint, midpoint)
    qfast_contracted = interval_text(*contracted)
    epsilon = interval_text(*task.epsilon)
    reduced = ",".join(
        interval_text(*task.box[coordinate])
        for coordinate in ("q_slow", "p_slow", "period")
    )
    zero_matrix = "{" + ",".join(
        "{" + ",".join("[0,0]" for _ in range(4)) + "}"
        for _ in range(4)
    ) + "}"
    identity_matrix = "{" + ",".join(
        "{" + ",".join("[1,1]" if row == column else "[0,0]" for column in range(4)) + "}"
        for row in range(4)
    ) + "}"
    return "\n".join(
        [
            f"energy_step_0_before={qfast_before}",
            f"energy_step_0_midpoint={qfast_midpoint}",
            "energy_step_0_residual=[0,0]",
            "energy_step_0_derivative=[1,1]",
            f"energy_step_0_newton_raw={qfast_midpoint}",
            f"energy_step_0_newton={qfast_contracted}",
            "energy_step_0_intersects=1",
            f"energy_step_0_after={qfast_contracted}",
            f"precision_bits={bits}",
            f"epsilon={epsilon}",
            f"reduced_box={{{reduced}}}",
            f"qplus_input={qfast_before}",
            f"energy_qplus={qfast_contracted}",
            f"energy_qplus_before={qfast_before}",
            f"energy_midpoint={qfast_midpoint}",
            "energy_midpoint_residual=[0,0]",
            "energy_derivative=[1,1]",
            "energy_iterations=1",
            "energy_derivative_positive=1",
            "energy_has_candidate=1",
            "energy_exclusion_guard=1",
            f"logical_margin=[{logical_margin},{logical_margin}]",
            f"newton_guard=[-{newton_guard},{newton_guard}]",
            f"X={{[-1,1],{qfast_contracted},[-1,1],[-1,1]}}",
            f"x_bar={{[0,0],{qfast_midpoint},[0,0],[0,0]}}",
            "F_center={[2,2],[0,0],[0,0],[0,0]}",
            "F_direct={[2,2],[0,0],[0,0],[0,0]}",
            f"J={zero_matrix}",
            "F_mean={[2,2],[0,0],[0,0],[0,0]}",
            f"C={identity_matrix}",
            "F_preconditioned={[2,2],[0,0],[0,0],[0,0]}",
            f"K={{[-3,-1],{qfast_contracted},[-1,1],[-1,1]}}",
            "direct_component=0",
            "mean_component=0",
            "preconditioned_component=0",
            "excluded=1",
            "krawczyk_subset=0",
            "status=RETURN_EXCLUDED",
            "",
        ]
    )


def terminal_mock_evaluator(
    _evaluator: Path,
    task: Any,
    *,
    timeout_seconds: int | None,
) -> Any:
    del timeout_seconds
    return RUNNER.EvaluatorOutcome(
        stdout=mock_return_excluded_transcript(task),
        stderr="",
        returncode=0,
        timed_out=False,
        wall_seconds=0.0,
    )


def delayed_mock_evaluator(seed: int) -> Callable[..., Any]:
    def evaluate(
        evaluator: Path,
        task: Any,
        *,
        timeout_seconds: int | None,
    ) -> Any:
        delay = random.Random(f"{seed}:{task.binding_sha256}").random() * 0.003
        time.sleep(delay)
        return terminal_mock_evaluator(
            evaluator,
            task,
            timeout_seconds=timeout_seconds,
        )

    return evaluate


def formal_status_whitelist() -> dict[str, list[list[Any]]]:
    return {
        "excluded": [
            ["ENERGY_EXCLUDED", 0],
            ["RETURN_EXCLUDED", 0],
        ],
        "splittable": [
            ["ENERGY_DERIVATIVE_FAIL", 3],
            ["ENERGY_GUARD_FAIL", 3],
            ["FLOW_FAIL", 3],
            ["UNKNOWN", 2],
        ],
        "scientific_stop": [["ROOT_CANDIDATE", 4]],
        "invalid": [["INVALID_EXCLUSION_UNIQUENESS_CONFLICT", 5]],
    }


def initialize_formal_generation(
    root: Path,
    *,
    name: str,
) -> dict[str, Any]:
    """Build a dynamically hash-bound synthetic formal generation.

    The project inputs and accepted L1 archive are read from ``ROOT``.  Only
    the evaluator binary, freeze, run configuration, and generated archive
    live below pytest's temporary directory.
    """

    project_root = make_synthetic_project_root(root, name=name)
    binary = root / "mock" / "capd_r401_local_complement_mp.mock"
    binary.parent.mkdir(parents=True, exist_ok=True)
    binary.write_bytes(b"mock evaluator: never executed as a subprocess\n")
    binary.chmod(0o755)
    input_hashes = {
        relative: file_sha256(project_root / relative)
        for relative in RUNNER.MANDATORY_FROZEN_INPUTS
    }
    scheduler = {
        "policy": RUNNER.EXPECTED_SCHEDULER_POLICY,
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
        "binary_sha256": file_sha256(binary),
        "capd_commit": RUNNER.EXPECTED_CAPD_COMMIT,
        "capd_flags": [
            "-D__HAVE_MPFR__",
            "-frounding-math",
            "-lmpfr",
            "-lgmp",
        ],
        "status_returncode_whitelist": formal_status_whitelist(),
    }
    limits = {"max_depth": 48, "max_nodes": 20_000}
    matrix = RUNNER.exact_production_matrix(RUNNER.load_plan_records())
    freeze_payload = {
        "schema_version": 1,
        "protocol_id": RUNNER.PROTOCOL_ID,
        "status": "FROZEN_FOR_PRODUCTION",
        "scientific_licensing_enabled": True,
        "checker_mode": RUNNER.EXPECTED_CHECKER_MODE,
        "checker_source_sha256": file_sha256(CHECKER_PATH),
        "matrix": [tree.payload() for tree in matrix],
        "per_tree_limits": limits,
        "scheduler": scheduler,
        "machine_requirements": dict(RUNNER.EXPECTED_MACHINE_REQUIREMENTS),
        "logical_thresholds": dict(RUNNER.EXPECTED_LOGICAL_THRESHOLDS),
        "evaluator": evaluator,
        "input_hashes": input_hashes,
    }
    freeze = root / f"{name}.freeze.json"
    dump_json(freeze, freeze_payload)
    machine_relative = (
        "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json"
    )
    formal = RUNNER.validate_formal_freeze(
        freeze,
        project_root=project_root,
    )
    binding = RUNNER.build_run_binding(
        plan_records=RUNNER.load_plan_records(),
        formal=formal,
    )
    assert binding["machine_requirements"] == RUNNER.EXPECTED_MACHINE_REQUIREMENTS
    assert binding["machine_freeze_sha256"] == input_hashes[machine_relative]
    output = root / name
    _config, run_config_sha256 = RUNNER.ensure_run_config(
        output,
        binding,
        resume=False,
    )
    return {
        "output": output,
        "freeze": freeze,
        "project_root": project_root,
        "binary": binary,
        "binding": binding,
        "matrix": matrix,
        "plan": RUNNER.load_plan_records(),
        "run_config_sha256": run_config_sha256,
        "source_sha256": evaluator["source_sha256"],
        "binary_sha256": evaluator["binary_sha256"],
        "limits": limits,
    }


def run_generation(
    fixture: dict[str, Any],
    evaluator_function: Callable[..., Any],
    *,
    matrix: tuple[Any, ...] | None = None,
    max_nodes: int | None = None,
    workers: int = 24,
) -> dict[str, Any]:
    selected = fixture["matrix"] if matrix is None else matrix
    return RUNNER.run_scheduler_session(
        output=fixture["output"],
        evaluator=fixture["binary"],
        matrix=selected,
        plan_records=fixture["plan"],
        run_config_sha256=fixture["run_config_sha256"],
        evaluator_source_sha256=fixture["source_sha256"],
        evaluator_binary_sha256=fixture["binary_sha256"],
        workers=workers,
        max_depth=fixture["limits"]["max_depth"],
        max_nodes=(fixture["limits"]["max_nodes"] if max_nodes is None else max_nodes),
        node_timeout_seconds=7200,
        dispatch_limit=None,
        evaluator_function=evaluator_function,
    )


def canonical_generation_fingerprint(output: Path) -> dict[str, Any]:
    summary = RUNNER.strict_json_load(output / "aggregate_summary.json")
    manifest = RUNNER.strict_json_load(output / "aggregate_manifest.json")
    entries = manifest["tree_manifests"]
    return {
        "aggregate_summary_sha256": file_sha256(output / "aggregate_summary.json"),
        "aggregate_manifest_sha256": file_sha256(output / "aggregate_manifest.json"),
        "ordered_tree_manifest_hashes": [
            entry["tree_manifest_sha256"] for entry in entries
        ],
        "tree_count": summary["tree_count"],
    }


def test_102_tree_mock_producer_archive_checker_e2e_and_delay_invariance(
    tmp_path: Path,
) -> None:
    baseline = initialize_formal_generation(tmp_path, name="baseline")
    delayed = initialize_formal_generation(tmp_path, name="delayed")
    # Model a real SIGKILL before the directory-rename commit.  Resume must
    # ignore this partial transaction, and the independent checker must apply
    # the same protocol-7 non-authoritative rule after all 102 trees finish.
    interrupted = baseline["output"] / "raw/128/S000/.C0L.tmp-1234-deadbeef"
    interrupted.mkdir(parents=True)
    (interrupted / "stdout.txt").write_text("partial evaluator output", encoding="utf-8")
    baseline_state = run_generation(baseline, delayed_mock_evaluator(11))
    delayed_state = run_generation(delayed, delayed_mock_evaluator(97))

    assert baseline_state["committed_tree_count"] == 102
    assert delayed_state["committed_tree_count"] == 102
    assert baseline_state["session_dispatch_count"] == 102 * 8
    assert delayed_state["session_dispatch_count"] == 102 * 8
    assert canonical_generation_fingerprint(
        baseline["output"]
    ) == canonical_generation_fingerprint(delayed["output"])
    assert interrupted.is_dir()

    verdict = CHECKER.audit_archive(
        baseline["output"],
        project_root=baseline["project_root"],
        freeze_path=baseline["freeze"],
    )
    assert type(verdict["schema_version"]) is int
    assert verdict["schema_version"] == CHECKER.SCHEMA_VERSION
    assert verdict["checker_status"] == "PASS_INDEPENDENT_CHECKER"
    assert verdict["promotion_authorized"] is True
    assert verdict["failure_count"] == 0
    assert len(verdict["tree_stats"]) == 102
    assert sum(item["node_count"] for item in verdict["tree_stats"]) == 816
    assert all(item["return_excluded"] == 8 for item in verdict["tree_stats"])
    assert verdict["final_status"] is None
    assert verdict["provenance_bindings"]["tree_manifest_root"][
        "entry_count"
    ] == 102


def test_barrier_enforces_one_inflight_per_tree_and_atomic_node_budgets(
    tmp_path: Path,
) -> None:
    fixture = initialize_formal_generation(tmp_path, name="budget-race")
    selected = tuple(fixture["matrix"][:3])
    lock = threading.Lock()
    active = {tree: 0 for tree in selected}
    maximum = {tree: 0 for tree in selected}

    def observed(
        evaluator: Path,
        task: Any,
        *,
        timeout_seconds: int | None,
    ) -> Any:
        with lock:
            active[task.tree] += 1
            maximum[task.tree] = max(maximum[task.tree], active[task.tree])
        try:
            time.sleep(0.004)
            return terminal_mock_evaluator(
                evaluator,
                task,
                timeout_seconds=timeout_seconds,
            )
        finally:
            with lock:
                active[task.tree] -= 1

    state = run_generation(
        fixture,
        observed,
        matrix=selected,
        max_nodes=1,
        workers=32,
    )
    assert state["session_dispatch_count"] == len(selected)
    assert all(maximum[tree] == 1 for tree in selected)
    assert state["committed_tree_count"] == 0
    assert all(item["evaluated_nodes"] == 1 for item in state["tree_states"])
    assert all(item["per_tree_node_budget_exhausted"] for item in state["tree_states"])


def split_one_root_mock(
    evaluator: Path,
    task: Any,
    *,
    timeout_seconds: int | None,
) -> Any:
    if task.node_id == "C0L" and task.depth == 0:
        return RUNNER.EvaluatorOutcome(
            stdout=f"precision_bits={task.tree.precision_bits}\nstatus=UNKNOWN\n",
            stderr="",
            returncode=2,
            timed_out=False,
            wall_seconds=0.0,
        )
    return terminal_mock_evaluator(
        evaluator,
        task,
        timeout_seconds=timeout_seconds,
    )


def test_crash_after_parent_commit_resumes_at_transaction_boundary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixture = initialize_formal_generation(tmp_path, name="crash-resume")
    selected = (fixture["matrix"][0],)
    original_commit = RUNNER.commit_node_transaction
    injected = False

    def crash_after_commit(*args: Any, **kwargs: Any) -> Any:
        nonlocal injected
        record = original_commit(*args, **kwargs)
        task = args[1]
        if task.node_id == "C0L" and not injected:
            injected = True
            raise RuntimeError("synthetic crash after durable parent commit")
        return record

    monkeypatch.setattr(RUNNER, "commit_node_transaction", crash_after_commit)
    with pytest.raises(RuntimeError, match="synthetic crash"):
        run_generation(fixture, split_one_root_mock, matrix=selected, workers=8)
    committed = RUNNER.scan_committed_node_records(fixture["output"])
    assert set(committed) == {(selected[0], "C0L")}

    monkeypatch.setattr(RUNNER, "commit_node_transaction", original_commit)
    resumed = run_generation(fixture, split_one_root_mock, matrix=selected, workers=8)
    assert resumed["committed_tree_count"] == 1
    assert resumed["session_dispatch_count"] == 9
    tree = RUNNER.strict_json_load(RUNNER.tree_path(fixture["output"], selected[0]))
    assert tree["evaluated_node_count"] == 10
    assert [node["task"]["node_id"] for node in tree["nodes"]].count("C0L") == 1
    assert {"C0L0", "C0L1"}.issubset(
        {node["task"]["node_id"] for node in tree["nodes"]}
    )


def test_whole_generation_quarantine_never_mixes_bindings(tmp_path: Path) -> None:
    generation = tmp_path / "generation"
    old_binding = {"generation": "old", "matrix": [{"precision_bits": 128}]}
    new_binding = {"generation": "new", "matrix": [{"precision_bits": 256}]}
    RUNNER.ensure_run_config(generation, old_binding, resume=False)
    old_raw = generation / "raw/128/S000/C0L/record.json"
    old_raw.parent.mkdir(parents=True)
    old_raw.write_text('{"old": true}\n', encoding="utf-8")

    quarantine = RUNNER.quarantine_incompatible_generation(generation, new_binding)
    assert quarantine.name == "generation.quarantine-0001"
    assert not generation.exists()
    assert (quarantine / old_raw.relative_to(generation)).read_text(
        encoding="utf-8"
    ) == '{"old": true}\n'
    quarantine_record = RUNNER.strict_json_load(
        quarantine / "QUARANTINE_RECORD.json"
    )
    assert quarantine_record["scientific_licensing_enabled"] is False
    assert quarantine_record["reason"] == "RUN_CONFIG_BINDING_MISMATCH"

    RUNNER.ensure_run_config(generation, new_binding, resume=False)
    assert not (generation / "raw").exists()
    assert RUNNER.strict_json_load(generation / "run_config.json")["binding"] == new_binding
    with pytest.raises(RUNNER.ResumeBindingError, match="binding-compatible"):
        RUNNER.quarantine_incompatible_generation(generation, new_binding)
    assert generation.is_dir()
    assert quarantine.is_dir()


def test_accepted_s0_archive_read_only_replays_through_a1_adapter() -> None:
    before = file_sha256(
        ROOT / "results/r401_val_l2_s0_local_complement/RELEASE_PROVENANCE.json"
    )
    completed = subprocess.run(
        [
            sys.executable,
            str(S0_ADAPTER_PATH),
            "--project-root",
            str(ROOT),
            "--s0",
            str(ROOT / "results/r401_val_l2_s0_local_complement"),
        ],
        check=True,
        text=True,
        capture_output=True,
        timeout=90,
    )
    payload = json.loads(completed.stdout)
    assert payload["status"] == "PASS_S0_READ_ONLY_COMPATIBILITY_REPLAY"
    assert payload["tree_count"] == 6
    assert payload["node_count"] == 3_016
    assert payload["manifest_hash_checks"] > 6_000
    assert payload["status_counts"] == {
        "ENERGY_EXCLUDED": 183,
        "RETURN_EXCLUDED": 1_349,
        "UNKNOWN": 1_484,
    }
    assert file_sha256(
        ROOT / "results/r401_val_l2_s0_local_complement/RELEASE_PROVENANCE.json"
    ) == before
