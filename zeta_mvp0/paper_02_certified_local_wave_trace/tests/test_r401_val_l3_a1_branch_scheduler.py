from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import signal
import subprocess
import sys
import threading
import time
from dataclasses import replace
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
SCHEDULER = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
MOCK_EVALUATOR = ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"
STATIC_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
BRANCH_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_branch_independent.py"
COMPOSITE_CHECKER = ROOT / "scripts/check_r401_val_l3_a1_composite_independent.py"
FORMAL_SOURCE = ROOT / "validated/capd_r401_phase_branch_tube_mp_a1.cpp"


def load_runtime():
    name = "r401_val_l3_a1_branch_runtime_test"
    spec = importlib.util.spec_from_file_location(name, RUNTIME)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


R = load_runtime()


def load_scheduler():
    name = "r401_val_l3_a1_all_slabs_branch_archive_test"
    spec = importlib.util.spec_from_file_location(name, SCHEDULER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


S = load_scheduler()


class SyntheticSchedulerAbort(BaseException):
    pass


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _abi_python(status: str, return_code: int, extra: str = "") -> str:
    return f'''#!/usr/bin/env python3
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

CANONICAL_ARGV0 = sys.argv[0]
if CANONICAL_ARGV0.startswith("/proc/self/fd/"):
    CANONICAL_ARGV0 = os.readlink(CANONICAL_ARGV0)
    if CANONICAL_ARGV0.endswith(" (deleted)"):
        CANONICAL_ARGV0 = CANONICAL_ARGV0[:-10]
ECHO_ARGV = [CANONICAL_ARGV0, *sys.argv[1:]]

def emit_common():
    print("protocol_id=R401-VAL-L3-A1")
    print("artifact_role=BRANCH_CELL_EVALUATOR_TRANSCRIPT")
    print("authority=PRODUCER_ONLY")
    print("scientific_licensing_enabled=false")
    print("dispatch_authorized_by_evaluator=false")
    print("component_status=null")
    print("milestone_status=null")
    print("theorem_status=null")
    print("final_status=null")
    print("input_argv_count=12")
    for index, value in enumerate(ECHO_ARGV):
        print(f"input_arg_{{index:02d}}={{value}}")
    print(f"precision_bits={{sys.argv[1]}}")
    print("taylor_order=24")
    print("tolerance=" + ("1e-30" if sys.argv[1] == "128" else "1e-60"))
    print("phase_grid=64")

{extra}
emit_common()
print("status={status}")
raise SystemExit({return_code})
'''


def _make_executable(tmp_path: Path, text: str, name: str = "mock_eval") -> Path:
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    path.chmod(0o755)
    return path


def _task(binary: Path, *, bits: int = 128, slab: str = "S000"):
    return R.BranchCellTask(
        precision_bits=bits,
        slab_id=slab,
        epsilon=("0", "0.0021"),
        root_box=(
            ("-0.0001", "0.0001"),
            ("0.149", "0.150"),
            ("-0.00008", "0.00008"),
            ("0.663", "0.664"),
        ),
        evaluator_binary_path=str(binary.resolve()),
        accepted_l1_primary_record_id=f"{bits}/{slab}/primary",
        accepted_l1_primary_record_sha256="a" * 64,
    )


def _bindings(binary: Path):
    return R.BranchBindings(
        matrix_id="1" * 64,
        freeze_sha256="2" * 64,
        run_config_sha256="3" * 64,
        evaluator_source_path=str(FORMAL_SOURCE.resolve()),
        evaluator_source_sha256=_sha(FORMAL_SOURCE),
        evaluator_binary_sha256=_sha(binary),
        capd_commit="4" * 40,
        capd_flags_sha256="5" * 64,
        runtime_libraries_sha256="6" * 64,
    )


def _roots(tmp_path: Path) -> tuple[Path, Path]:
    return (tmp_path / "r401_val_l3_all_slabs", tmp_path / "r401_val_l3_all_slabs.operational")


def _run(tmp_path: Path, binary: Path, **kwargs):
    output, operational = _roots(tmp_path)
    return R.run_branch_cell_transaction(
        output_root=output,
        operational_root=operational,
        task=kwargs.pop("task", _task(binary)),
        bindings=kwargs.pop("bindings", _bindings(binary)),
        **kwargs,
    )


def _acquire_test_cell_lock(*args, **kwargs):
    owner = R._CellLockOwner()
    result = R._acquire_cell_lock(*args, owner=owner, **kwargs)
    assert owner.descriptor == result[0]
    assert owner.identity == result[1]
    assert owner.payload == result[2]
    return result


def _gone_or_zombie(pid: int) -> bool:
    status = Path(f"/proc/{pid}/stat")
    if not status.exists():
        return True
    try:
        return status.read_text(encoding="utf-8").split()[2] == "Z"
    except FileNotFoundError:
        return True


def test_formal_cpp_closes_status_namespace_and_lower_bound_boundary() -> None:
    text = FORMAL_SOURCE.read_text(encoding="utf-8")
    compact = " ".join(text.split())
    for status, code in R.EVALUATOR_STATUS_CODES.items():
        assert status in text
        assert f"return {code};" in compact
    assert "argc != 12" in text
    assert "for (int index = 0; index < argc; ++index)" in text
    assert "is_canonical_argv0(argv[0])" in text
    assert "const MpInterval tube_radius_sq = MpInterval(1) / MpInterval(625);" in compact
    assert "rslow_sq.rightBound() < tube_radius_sq.leftBound()" in compact
    assert "rslow_sq.leftBound() >= tube_radius_sq.rightBound()" in compact
    assert "any_segment_violation" in text
    assert "BRANCH_TUBE_UNRESOLVED" in text
    assert "scientific_licensing_enabled=false" in text
    for field in ("component_status=null", "milestone_status=null", "theorem_status=null", "final_status=null"):
        assert field in text


def test_exact_twelve_string_argv_and_precision_dependent_tolerance(tmp_path: Path) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    for bits, tolerance in ((128, "1e-30"), (256, "1e-60")):
        task = _task(binary, bits=bits)
        task.validate()
        assert len(task.argv()) == 12
        assert all(type(value) is str for value in task.argv())
        assert task.argv() == [
            str(binary.resolve()),
            str(bits),
            "0",
            "0.0021",
            "-0.0001",
            "0.0001",
            "0.149",
            "0.150",
            "-0.00008",
            "0.00008",
            "0.663",
            "0.664",
        ]
        assert task.tolerance == tolerance


def test_doubled_leading_separator_argv0_alias_is_rejected() -> None:
    task = replace(
        _task(Path("/tmp/noncanonical-branch-evaluator")),
        evaluator_binary_path="//tmp/noncanonical-branch-evaluator",
    )
    with pytest.raises(R.BranchContractError, match="canonical and absolute"):
        task.validate()


def test_doubled_leading_separator_result_root_alias_is_rejected(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    doubled_parent = "//" + tmp_path.as_posix().lstrip("/")
    output = Path(doubled_parent + "/r401_val_l3_all_slabs")
    operational = Path(doubled_parent + "/r401_val_l3_all_slabs.operational")
    with pytest.raises(R.BranchContractError, match="canonical and absolute"):
        R.run_branch_cell_transaction(
            output_root=output,
            operational_root=operational,
            task=_task(binary),
            bindings=_bindings(binary),
        )


def test_successful_atomic_cell_manifest_and_write_once_resume(tmp_path: Path) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_CELL_CERTIFIED", 0, counter_code),
    )
    first = _run(tmp_path, binary)
    assert first.resumed_without_dispatch is False
    assert first.record["scheduler_result"]["classification"] == "COMMITTED_EVALUATOR_RESULT"
    assert first.record["scheduler_result"]["evaluator_status"] == "BRANCH_CELL_CERTIFIED"
    assert first.record["milestone_status"] is None
    assert first.record["theorem_status"] is None
    assert first.record["final_status"] is None
    output, operational = _roots(tmp_path)
    cell = output / "branch/cells/128/S000"
    manifest = output / "branch/cell_manifests/128/S000.json"
    assert {path.name for path in cell.iterdir()} == {"stdout.txt", "stderr.txt", "record.json"}
    assert manifest.is_file()
    assert not any((operational / "staging/branch/128").iterdir())
    first_bytes = {path: path.read_bytes() for path in (*cell.iterdir(), manifest)}

    second = _run(tmp_path, binary)
    assert second.resumed_without_dispatch is True
    assert (tmp_path / "mock_eval.count").read_text(encoding="utf-8").splitlines() == ["dispatch"]
    assert {path: path.read_bytes() for path in (*cell.iterdir(), manifest)} == first_bytes


def test_manifestless_rename_recovery_never_redispatches(tmp_path: Path) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_TUBE_UNRESOLVED", 2, counter_code),
    )
    first = _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    manifest_path = output / "branch/cell_manifests/128/S000.json"
    manifest_path.unlink()
    cell = output / "branch/cells/128/S000"
    before = {path.name: path.read_bytes() for path in cell.iterdir()}
    recovered = _run(tmp_path, binary)
    assert recovered.resumed_without_dispatch is True
    assert recovered.record["scheduler_result"]["evaluator_status"] == "BRANCH_TUBE_UNRESOLVED"
    assert {path.name: path.read_bytes() for path in cell.iterdir()} == before
    assert (tmp_path / "mock_eval.count").read_text(encoding="utf-8").splitlines() == ["dispatch"]


def test_manifestless_recovery_replays_every_raw_byte_before_publication(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    bindings = _bindings(binary)
    _run(tmp_path, binary, bindings=bindings)
    output, _operational = _roots(tmp_path)
    manifest_path = output / "branch/cell_manifests/128/S000.json"
    manifest_path.unlink()
    stdout = output / "branch/cells/128/S000/stdout.txt"
    stdout.write_bytes(stdout.read_bytes() + b"post-rename corruption\n")
    with pytest.raises(R.BranchProvenanceError):
        _run(tmp_path, binary)
    assert not manifest_path.exists()


def test_resume_rejects_changed_live_persistent_binary(tmp_path: Path) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    bindings = _bindings(binary)
    _run(tmp_path, binary, bindings=bindings)
    binary.write_text(
        _abi_python("BRANCH_TUBE_UNRESOLVED", 2), encoding="utf-8"
    )
    binary.chmod(0o755)
    with pytest.raises(R.BranchProvenanceError, match="binary hash mismatch"):
        _run(tmp_path, binary, bindings=bindings)


@pytest.mark.parametrize(
    ("status", "return_code", "mutation", "reason"),
    (
        ("BRANCH_CELL_CERTIFIED", 2, "", "STATUS_RETURN_CODE_MISMATCH"),
        ("UNKNOWN_BRANCH_STATUS", 0, "", "UNKNOWN_EVALUATOR_STATUS"),
        (
            "BRANCH_CELL_CERTIFIED",
            0,
            'print("status=BRANCH_CELL_CERTIFIED")',
            "STATUS_CARDINALITY",
        ),
        (
            "BRANCH_CELL_CERTIFIED",
            0,
            'print("status=evil")',
            "STATUS_CARDINALITY",
        ),
    ),
)
def test_malformed_unknown_duplicate_or_code_mismatch_never_gets_evaluator_status(
    tmp_path: Path,
    status: str,
    return_code: int,
    mutation: str,
    reason: str,
) -> None:
    binary = _make_executable(
        tmp_path,
        _abi_python(status, return_code, mutation),
    )
    result = _run(tmp_path, binary)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "MALFORMED_EVALUATOR_OUTPUT"
    assert scheduler["evaluator_status"] is None
    assert reason in scheduler["failure_reason"]


def test_nonempty_stderr_on_nominal_pass_is_malformed(tmp_path: Path) -> None:
    extra = 'print("not-empty", file=sys.stderr)'
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, extra)
    )
    result = _run(tmp_path, binary)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "MALFORMED_EVALUATOR_OUTPUT"
    assert scheduler["failure_reason"] == "NONEMPTY_STDERR_ON_CERTIFIED_RESULT"


def test_default_branch_budgets_use_exact_integer_milliseconds_and_byte_caps() -> None:
    budgets = R.BranchBudgets()
    assert budgets.timeout_ms == 600_000
    assert budgets.term_grace_ms == 2_000
    assert budgets.pipe_close_grace_ms == 1_000
    assert budgets.stdout_bytes == 16 * 1024 * 1024
    assert budgets.stderr_bytes == 1 * 1024 * 1024
    assert budgets.record_bytes == 4 * 1024 * 1024
    assert budgets.total_cell_bytes == 32 * 1024 * 1024
    assert budgets.payload() == {
        "pipe_close_grace_ms": 1_000,
        "record_bytes": 4 * 1024 * 1024,
        "stderr_bytes": 1 * 1024 * 1024,
        "stdout_bytes": 16 * 1024 * 1024,
        "term_grace_ms": 2_000,
        "timeout_ms": 600_000,
        "total_cell_bytes": 32 * 1024 * 1024,
    }
    assert all(type(value) is int for value in budgets.payload().values())
    budgets.validate()


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("timeout_ms", 600_000.0),
        ("timeout_ms", True),
        ("timeout_ms", 0),
        ("term_grace_ms", 2_000.0),
        ("term_grace_ms", False),
        ("term_grace_ms", -1),
        ("pipe_close_grace_ms", 1_000.0),
        ("pipe_close_grace_ms", True),
        ("pipe_close_grace_ms", 0),
    ],
)
def test_frozen_millisecond_budgets_reject_noninteger_or_nonpositive_aliases(
    field: str, bad_value: object
) -> None:
    with pytest.raises(R.BranchContractError, match="positive exact integer"):
        R.BranchBudgets(**{field: bad_value}).validate()


def test_branch_runtime_pretty_serializer_requires_exact_plain_json() -> None:
    class DictAlias(dict):
        pass

    class ListAlias(list):
        pass

    class StringAlias(str):
        pass

    cycle = []
    cycle.append(cycle)
    attacks = [
        ("tuple",),
        {1: "non-string-key"},
        {StringAlias("alias-key"): "value"},
        DictAlias({"key": "value"}),
        ListAlias([1]),
        {"nested": [StringAlias("value")]},
        {"nested": [float("nan")]},
        {"nested": [float("inf")]},
        {"nested": [float("-inf")]},
        cycle,
    ]
    for payload in attacks:
        with pytest.raises(R.BranchContractError):
            R.canonical_json_bytes(payload)

    assert R.canonical_json_bytes(
        {"finite": 1.25, "items": [True, None, 3]}
    ) == (
        b'{\n  "finite": 1.25,\n  "items": [\n'
        b"    true,\n    null,\n    3\n  ]\n}\n"
    )
    shared = [1]
    assert R.canonical_json_bytes({"left": shared, "right": shared}) == (
        b'{\n  "left": [\n    1\n  ],\n'
        b'  "right": [\n    1\n  ]\n}\n'
    )


def test_stdout_is_streamed_to_exact_16_mib_cap_and_group_is_stopped(tmp_path: Path) -> None:
    extra = '''chunk = b"x" * (1024 * 1024)
for _ in range(17):
    os.write(1, chunk)
time.sleep(30)
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_CELL_CERTIFIED", 0, extra),
    )
    result = _run(tmp_path, binary)
    scheduler = result.record["scheduler_result"]
    raw = result.record["raw"]
    assert scheduler["classification"] == "CELL_OUTPUT_BUDGET_EXHAUSTED"
    assert scheduler["evaluator_status"] is None
    assert raw["stdout_bytes"] == 16 * 1024 * 1024
    assert raw["stdout_truncated"] is True
    assert raw["record_cap_bytes"] == 4 * 1024 * 1024
    output, _operational = _roots(tmp_path)
    cell = output / "branch/cells/128/S000"
    assert sum(path.stat().st_size for path in cell.iterdir()) < 32 * 1024 * 1024


def test_stderr_is_streamed_to_exact_1_mib_cap(tmp_path: Path) -> None:
    extra = '''chunk = b"e" * (1024 * 1024)
os.write(2, chunk)
os.write(2, b"overflow")
time.sleep(30)
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_FLOW_FAIL", 3, extra),
    )
    result = _run(tmp_path, binary)
    assert result.record["scheduler_result"]["classification"] == "CELL_OUTPUT_BUDGET_EXHAUSTED"
    assert result.record["raw"]["stderr_bytes"] == 1 * 1024 * 1024
    assert result.record["raw"]["stderr_truncated"] is True


def test_timeout_uses_new_process_group_term_then_kill_and_leaves_no_live_descendant(
    tmp_path: Path,
) -> None:
    extra = '''signal.signal(signal.SIGTERM, signal.SIG_IGN)
child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
])
Path(CANONICAL_ARGV0).with_suffix(".descendant").write_text(str(child.pid), encoding="utf-8")
time.sleep(60)
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_CELL_CERTIFIED", 0, extra),
    )
    budgets = R.BranchBudgets(
        timeout_ms=250,
        term_grace_ms=100,
        pipe_close_grace_ms=200,
    )
    result = _run(tmp_path, binary, budgets=budgets)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "CELL_TIMEOUT"
    assert scheduler["evaluator_status"] is None
    assert scheduler["term_sent"] is True
    assert scheduler["kill_sent"] is True
    descendant = int((tmp_path / "mock_eval.descendant").read_text(encoding="utf-8"))
    deadline = time.monotonic() + 2
    while not _gone_or_zombie(descendant) and time.monotonic() < deadline:
        time.sleep(0.02)
    assert _gone_or_zombie(descendant)


def test_signaled_evaluator_with_pipe_holding_descendant_is_fully_killed_and_reaped(
    tmp_path: Path,
) -> None:
    extra = '''child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
])
Path(CANONICAL_ARGV0).with_suffix(".descendant").write_text(str(child.pid), encoding="utf-8")
os.kill(os.getpid(), signal.SIGKILL)
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_TUBE_UNRESOLVED", 2, extra),
    )
    budgets = R.BranchBudgets(
        timeout_ms=2_000,
        term_grace_ms=100,
        pipe_close_grace_ms=50,
    )
    result = _run(tmp_path, binary, budgets=budgets)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "CELL_SIGNAL"
    assert scheduler["evaluator_status"] is None
    assert scheduler["descendant_group_survived_parent"] is True
    assert scheduler["descendant_pipe_leak"] is True
    assert scheduler["term_sent"] is True
    assert scheduler["kill_sent"] is True
    assert scheduler["process_group_residual"] is False
    descendant = int((tmp_path / "mock_eval.descendant").read_text(encoding="utf-8"))
    assert not Path(f"/proc/{descendant}").exists()


def test_signaled_evaluator_with_closed_pipe_descendant_is_fully_killed_and_reaped(
    tmp_path: Path,
) -> None:
    extra = '''child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
Path(CANONICAL_ARGV0).with_suffix(".descendant").write_text(str(child.pid), encoding="utf-8")
os.kill(os.getpid(), signal.SIGKILL)
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_TUBE_UNRESOLVED", 2, extra),
    )
    budgets = R.BranchBudgets(
        timeout_ms=2_000,
        term_grace_ms=100,
        pipe_close_grace_ms=50,
    )
    result = _run(tmp_path, binary, budgets=budgets)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "CELL_SIGNAL"
    assert scheduler["evaluator_status"] is None
    assert scheduler["descendant_group_survived_parent"] is True
    assert scheduler["descendant_pipe_leak"] is False
    assert scheduler["term_sent"] is True
    assert scheduler["kill_sent"] is True
    assert scheduler["process_group_residual"] is False
    descendant = int((tmp_path / "mock_eval.descendant").read_text(encoding="utf-8"))
    assert not Path(f"/proc/{descendant}").exists()


def test_timeout_stops_cooperative_group_with_term_without_kill(tmp_path: Path) -> None:
    extra = '''def stop(_signum, _frame):
    raise SystemExit(9)
signal.signal(signal.SIGTERM, stop)
time.sleep(60)
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_CELL_CERTIFIED", 0, extra),
    )
    budgets = R.BranchBudgets(
        timeout_ms=200,
        term_grace_ms=500,
        pipe_close_grace_ms=200,
    )
    result = _run(tmp_path, binary, budgets=budgets)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "CELL_TIMEOUT"
    assert scheduler["term_sent"] is True
    assert scheduler["kill_sent"] is False


def test_direct_signal_is_scheduler_signal_not_evaluator_unresolved(tmp_path: Path) -> None:
    extra = 'os.kill(os.getpid(), signal.SIGKILL)'
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_TUBE_UNRESOLVED", 2, extra),
    )
    result = _run(tmp_path, binary)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "CELL_SIGNAL"
    assert scheduler["evaluator_status"] is None
    assert scheduler["signal_number"] == signal.SIGKILL


@pytest.mark.parametrize("abort_type", (KeyboardInterrupt, SyntheticSchedulerAbort))
def test_scheduler_baseexception_cleans_complete_mock_process_group(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    abort_type: type[BaseException],
) -> None:
    extra = '''signal.signal(signal.SIGTERM, signal.SIG_IGN)
child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
])
Path(CANONICAL_ARGV0).with_suffix(".processes").write_text(
    f"{os.getpid()} {child.pid}", encoding="utf-8"
)
time.sleep(60)
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, extra)
    )
    process_file = tmp_path / "mock_eval.processes"
    real_event = R.threading.Event

    class InterruptingEvent:
        def __init__(self) -> None:
            self.inner = real_event()
            self.interrupted = False

        def set(self) -> None:
            self.inner.set()

        def is_set(self) -> bool:
            return self.inner.is_set()

        def wait(self, timeout=None):
            if not self.interrupted:
                deadline = time.monotonic() + 2.0
                while not process_file.exists() and time.monotonic() < deadline:
                    time.sleep(0.005)
                assert process_file.exists()
                self.interrupted = True
                raise abort_type
            return self.inner.wait(timeout)

    def budget_event_factory():
        monkeypatch.setattr(R.threading, "Event", real_event)
        return InterruptingEvent()

    monkeypatch.setattr(R.threading, "Event", budget_event_factory)
    budgets = R.BranchBudgets(
        timeout_ms=5_000,
        term_grace_ms=100,
        pipe_close_grace_ms=100,
    )
    with pytest.raises(abort_type):
        _run(tmp_path, binary, budgets=budgets)
    evaluator_pid, descendant_pid = map(
        int, process_file.read_text(encoding="utf-8").split()
    )
    assert not Path(f"/proc/{evaluator_pid}").exists()
    assert not Path(f"/proc/{descendant_pid}").exists()


def test_scheduler_sigterm_cleans_mock_group_before_parent_exits(
    tmp_path: Path,
) -> None:
    process_file = tmp_path / "sigterm-processes"
    mock = _make_executable(
        tmp_path,
        '''#!/usr/bin/env python3
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

signal.signal(signal.SIGTERM, signal.SIG_IGN)
child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
])
Path(os.environ["A416_PROCESS_FILE"]).write_text(
    f"{os.getpid()} {child.pid}", encoding="utf-8"
)
time.sleep(60)
''',
        name="sigterm_mock",
    )
    driver = tmp_path / "sigterm_driver.py"
    driver.write_text(
        '''import importlib.util
import os
import sys
from pathlib import Path

runtime_path = Path(sys.argv[1])
binary = Path(sys.argv[2])
raw_root = Path(sys.argv[3])
spec = importlib.util.spec_from_file_location("a416_sigterm_runtime", runtime_path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
descriptor = os.open(binary, os.O_RDONLY)
try:
    module.run_bounded_process(
        [str(binary), "128", "0", "0.1", "0", "1", "0", "1", "0", "1", "1", "2"],
        raw_root / "stdout.txt",
        raw_root / "stderr.txt",
        module.BranchBudgets(
            timeout_ms=30_000,
            term_grace_ms=100,
            pipe_close_grace_ms=100,
        ),
        executable_descriptor=descriptor,
    )
finally:
    os.close(descriptor)
''',
        encoding="utf-8",
    )
    environment = dict(os.environ)
    environment["A416_PROCESS_FILE"] = str(process_file)
    parent = subprocess.Popen(
        [sys.executable, str(driver), str(RUNTIME), str(mock), str(tmp_path)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=environment,
    )
    try:
        deadline = time.monotonic() + 5.0
        while not process_file.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        assert process_file.exists()
        os.kill(parent.pid, signal.SIGTERM)
        assert parent.wait(timeout=5.0) != 0
    finally:
        if parent.poll() is None:
            parent.kill()
            parent.wait(timeout=5.0)
    evaluator_pid, descendant_pid = map(
        int, process_file.read_text(encoding="utf-8").split()
    )
    assert not Path(f"/proc/{evaluator_pid}").exists()
    assert not Path(f"/proc/{descendant_pid}").exists()


def test_signal_queued_after_spawn_is_delivered_only_after_pid_ownership(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    extra = '''signal.signal(signal.SIGTERM, signal.SIG_IGN)
child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
])
Path(CANONICAL_ARGV0).with_suffix(".processes").write_text(
    f"{os.getpid()} {child.pid}", encoding="utf-8"
)
time.sleep(60)
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, extra)
    )
    process_file = tmp_path / "mock_eval.processes"
    real_spawn = R._spawn_pinned_process
    delivered_before_return = False

    def spawn_then_queue_signal(*args, **kwargs):
        nonlocal delivered_before_return
        spawned = real_spawn(*args, **kwargs)
        deadline = time.monotonic() + 2.0
        while not process_file.exists() and time.monotonic() < deadline:
            time.sleep(0.005)
        assert process_file.exists()
        try:
            os.kill(os.getpid(), signal.SIGTERM)
            return spawned
        except BaseException:
            delivered_before_return = True
            R._cleanup_process_group_after_scheduler_failure(
                spawned,
                (),
                R.BranchBudgets(
                    timeout_ms=5_000,
                    term_grace_ms=100,
                    pipe_close_grace_ms=100,
                ),
            )
            raise

    monkeypatch.setattr(R, "_spawn_pinned_process", spawn_then_queue_signal)
    budgets = R.BranchBudgets(
        timeout_ms=5_000,
        term_grace_ms=100,
        pipe_close_grace_ms=100,
    )
    with pytest.raises(R._SchedulerTerminationSignal):
        _run(tmp_path, binary, budgets=budgets)
    assert delivered_before_return is False
    evaluator_pid, descendant_pid = map(
        int, process_file.read_text(encoding="utf-8").split()
    )
    assert not Path(f"/proc/{evaluator_pid}").exists()
    assert not Path(f"/proc/{descendant_pid}").exists()


def test_post_spawn_stream_setup_failure_reaps_adopted_descendant(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    extra = '''signal.signal(signal.SIGTERM, signal.SIG_IGN)
child = subprocess.Popen([
    sys.executable,
    "-c",
    "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)",
])
Path(CANONICAL_ARGV0).with_suffix(".processes").write_text(
    f"{os.getpid()} {child.pid}", encoding="utf-8"
)
time.sleep(60)
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, extra)
    )
    process_file = tmp_path / "mock_eval.processes"
    real_fdopen = R.os.fdopen
    injected = False

    def fail_first_stream_wrap(*args, **kwargs):
        nonlocal injected
        if not injected:
            injected = True
            deadline = time.monotonic() + 2.0
            while not process_file.exists() and time.monotonic() < deadline:
                time.sleep(0.005)
            assert process_file.exists()
            raise OSError("synthetic fdopen failure")
        return real_fdopen(*args, **kwargs)

    monkeypatch.setattr(R.os, "fdopen", fail_first_stream_wrap)
    result = _run(
        tmp_path,
        binary,
        budgets=R.BranchBudgets(
            timeout_ms=5_000,
            term_grace_ms=100,
            pipe_close_grace_ms=100,
        ),
    )
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "PROVENANCE_INVALID"
    assert scheduler["failure_reason"] == "PROCESS_SPAWN_FAILED"
    evaluator_pid, descendant_pid = map(
        int, process_file.read_text(encoding="utf-8").split()
    )
    assert not Path(f"/proc/{evaluator_pid}").exists()
    assert not Path(f"/proc/{descendant_pid}").exists()


def test_partial_signal_handler_install_is_restored_on_pending_sigint(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    previous_int = signal.getsignal(signal.SIGINT)
    previous_term = signal.getsignal(signal.SIGTERM)
    real_signal = R.signal.signal
    injected = False

    def install_then_interrupt(signal_number, handler):
        nonlocal injected
        result = real_signal(signal_number, handler)
        if signal_number == signal.SIGINT and not injected:
            injected = True
            os.kill(os.getpid(), signal.SIGINT)
        return result

    monkeypatch.setattr(R.signal, "signal", install_then_interrupt)
    descriptor = os.open(binary, os.O_RDONLY)
    try:
        with pytest.raises(KeyboardInterrupt):
            R.run_bounded_process(
                _task(binary).argv(),
                tmp_path / "handler-stdout.txt",
                tmp_path / "handler-stderr.txt",
                R.BranchBudgets(
                    timeout_ms=1_000,
                    term_grace_ms=100,
                    pipe_close_grace_ms=100,
                ),
                executable_descriptor=descriptor,
            )
    finally:
        os.close(descriptor)
    assert injected is True
    assert signal.getsignal(signal.SIGINT) == previous_int
    assert signal.getsignal(signal.SIGTERM) == previous_term


def test_interrupted_staging_is_preserved_and_never_authoritative(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, counter_code)
    )
    real_rename = R._rename_noreplace

    def crash_before_publish(source, destination):
        if Path(destination).name == "S000":
            raise RuntimeError("synthetic crash before canonical rename")
        return real_rename(source, destination)

    monkeypatch.setattr(R, "_rename_noreplace", crash_before_publish)
    with pytest.raises(RuntimeError, match="synthetic crash"):
        _run(tmp_path, binary)
    output, operational = _roots(tmp_path)
    expected_stage = operational / "staging/branch/128/.S000.tmp-3333333333333333-0"
    assert expected_stage.is_dir()
    assert {path.name for path in expected_stage.iterdir()} == {"stdout.txt", "stderr.txt", "record.json"}
    assert not (output / "branch/cells/128/S000").exists()
    assert not (output / "branch/cell_manifests/128/S000.json").exists()

    monkeypatch.setattr(R, "_rename_noreplace", real_rename)
    with pytest.raises(R.BranchProvenanceError, match="whole-generation quarantine"):
        _run(tmp_path, binary, attempt=0)
    with pytest.raises(R.BranchProvenanceError, match="whole-generation quarantine"):
        _run(tmp_path, binary, attempt=1)
    assert expected_stage.is_dir()
    assert not (operational / "interrupted/branch").exists()
    assert (tmp_path / "mock_eval.count").read_text(encoding="utf-8").splitlines() == [
        "dispatch"
    ]


def test_staging_namespace_scanner_rejects_every_noncanonical_extra(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    bad = operational / "staging/branch/128/.S000.tmp-bad-0"
    bad.mkdir(parents=True)
    with pytest.raises(R.BranchProvenanceError, match="staging name"):
        _run(tmp_path, binary)


def test_distinct_live_owned_stage_does_not_block_another_barrier_cell(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    bindings = _bindings(binary)
    other_task = _task(binary, slab="S001")
    other_stage = (
        operational / "staging/branch/128/.S001.tmp-3333333333333333-0"
    )
    other_stage.mkdir(parents=True)
    other_lock = operational / "locks/branch/128/S001.lock"
    other_lock.parent.mkdir(parents=True)
    other_lock.write_bytes(
        R.canonical_json_bytes(
            R._lock_payload(other_task, bindings, 0, "9" * 32)
        )
    )

    result = _run(tmp_path, binary, bindings=bindings)
    assert result.record["scheduler_result"]["classification"] == (
        "COMMITTED_EVALUATOR_RESULT"
    )
    assert (output / "branch/cells/128/S000").is_dir()
    assert other_stage.is_dir()
    assert other_lock.is_file()


@pytest.mark.parametrize("mode", ("missing-lock", "stale-lock", "attempt-mismatch"))
def test_other_cell_stage_without_exact_live_owner_blocks_admission(
    tmp_path: Path, mode: str
) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, counter_code)
    )
    output, operational = _roots(tmp_path)
    bindings = _bindings(binary)
    other_task = _task(binary, slab="S001")
    other_stage = (
        operational / "staging/branch/128/.S001.tmp-3333333333333333-0"
    )
    other_stage.mkdir(parents=True)
    if mode != "missing-lock":
        payload = R._lock_payload(
            other_task,
            bindings,
            1 if mode == "attempt-mismatch" else 0,
            "9" * 32,
        )
        if mode == "stale-lock":
            payload["pid"] = 999_999_999
            payload["owner_process_start_time"] = 1
        other_lock = operational / "locks/branch/128/S001.lock"
        other_lock.parent.mkdir(parents=True)
        other_lock.write_bytes(R.canonical_json_bytes(payload))

    expected = {
        "missing-lock": "cannot snapshot",
        "stale-lock": "no matching live owner",
        "attempt-mismatch": "attempt differs",
    }[mode]
    with pytest.raises(R.BranchProvenanceError, match=expected):
        _run(tmp_path, binary, bindings=bindings)
    assert not (output / "branch/cells/128/S000").exists()
    assert not (tmp_path / "mock_eval.count").exists()


def test_post_lock_recheck_rejects_new_unowned_other_cell_stage(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, counter_code)
    )
    output, operational = _roots(tmp_path)
    real_acquire = R._acquire_cell_lock

    def acquire_then_inject(*args, **kwargs):
        result = real_acquire(*args, **kwargs)
        injected = (
            operational
            / "staging/branch/128/.S001.tmp-3333333333333333-0"
        )
        injected.mkdir(parents=True)
        return result

    monkeypatch.setattr(R, "_acquire_cell_lock", acquire_then_inject)
    with pytest.raises(R.BranchProvenanceError, match="cannot snapshot"):
        _run(tmp_path, binary)
    assert not (output / "branch/cells/128/S000").exists()
    assert not (operational / "locks/branch/128/S000.lock").exists()
    assert not (tmp_path / "mock_eval.count").exists()


@pytest.mark.parametrize("namespace", ("branch-staging", "branch-lock"))
def test_withdrawn_or_malformed_interrupted_namespace_blocks_admission(
    tmp_path: Path, namespace: str
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    if namespace == "branch-staging":
        (operational / "interrupted/branch/128/EVIL").mkdir(parents=True)
        match = "withdrawn"
    else:
        evil = operational / "interrupted/locks/branch/128/EVIL"
        evil.parent.mkdir(parents=True)
        evil.write_text("invalid\n", encoding="utf-8")
        match = "interrupted branch lock name"
    with pytest.raises(R.BranchProvenanceError, match=match):
        _run(tmp_path, binary)
    assert not (output / "branch/cells/128/S000").exists()


def test_well_named_malformed_interrupted_lock_archive_blocks_admission(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    archived = (
        operational
        / "interrupted/locks/branch/128/"
        "S001.attempt-2.generation-3333333333333333.owner-"
        f"{'8' * 32}.lock"
    )
    archived.parent.mkdir(parents=True)
    archived.write_text("not-json\n", encoding="utf-8")
    with pytest.raises(R.BranchProvenanceError, match="strict JSON"):
        _run(tmp_path, binary)
    assert not (output / "branch/cells/128/S000").exists()


def test_dangling_interrupted_lock_root_symlink_blocks_admission(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    branch_root = operational / "interrupted/locks/branch"
    branch_root.parent.mkdir(parents=True)
    branch_root.symlink_to(tmp_path / "absent-interrupted-lock-root")
    with pytest.raises(R.BranchProvenanceError, match="symlink component"):
        _run(tmp_path, binary)
    assert not (output / "branch/cells/128/S000").exists()


def test_well_named_malformed_active_lock_blocks_other_cell_admission(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    active = operational / "locks/branch/128/S001.lock"
    active.parent.mkdir(parents=True)
    active.write_text("not-json\n", encoding="utf-8")
    with pytest.raises(R.BranchProvenanceError, match="strict JSON"):
        _run(tmp_path, binary)
    assert not (output / "branch/cells/128/S000").exists()


@pytest.mark.parametrize("namespace", ("active", "interrupted"))
def test_every_lock_namespace_is_bound_to_current_generation(
    tmp_path: Path, namespace: str
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    task = _task(binary, slab="S001")
    bindings = _bindings(binary)
    payload = R._lock_payload(task, bindings, 2, "8" * 32)
    payload["generation_prefix"] = "f" * 16
    if namespace == "active":
        path = operational / "locks/branch/128/S001.lock"
    else:
        path = (
            operational
            / "interrupted/locks/branch/128/"
            "S001.attempt-2.generation-ffffffffffffffff.owner-"
            f"{'8' * 32}.lock"
        )
    path.parent.mkdir(parents=True)
    path.write_bytes(R.canonical_json_bytes(payload))
    with pytest.raises(R.BranchProvenanceError, match="generation|mismatch"):
        _run(tmp_path, binary)
    assert not (output / "branch/cells/128/S000").exists()


def test_lock_publication_never_exposes_a_half_written_canonical_lock(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    task = _task(binary)
    bindings = _bindings(binary)
    lock_parent = operational / "locks/branch/128"
    lock_parent.mkdir(parents=True)
    lock_path = lock_parent / "S000.lock"
    real_write = R.os.write
    half_written = threading.Event()
    permit_completion = threading.Event()
    blocked_once = False

    def blocking_first_write(descriptor, payload):
        nonlocal blocked_once
        if not blocked_once:
            blocked_once = True
            accepted = real_write(
                descriptor, payload[: max(1, len(payload) // 2)]
            )
            half_written.set()
            assert permit_completion.wait(timeout=3.0)
            return accepted
        return real_write(descriptor, payload)

    monkeypatch.setattr(R.os, "write", blocking_first_write)
    owner_result = {}
    owner_errors = []

    def acquire_owner() -> None:
        try:
            owner_result["value"] = _acquire_test_cell_lock(
                lock_path,
                lock_parent,
                operational,
                task,
                bindings,
                0,
            )
        except BaseException as error:
            owner_errors.append(error)

    owner = threading.Thread(target=acquire_owner)
    owner.start()
    assert half_written.wait(timeout=3.0)
    assert not lock_path.exists()

    scan_finished = threading.Event()
    scan_errors = []

    def scan_namespace() -> None:
        try:
            R._scan_all_lock_namespaces(
                operational, bindings.run_config_sha256[:16]
            )
        except BaseException as error:
            scan_errors.append(error)
        finally:
            scan_finished.set()

    scanner = threading.Thread(target=scan_namespace)
    scanner.start()
    time.sleep(0.05)
    assert not scan_finished.is_set()
    permit_completion.set()
    owner.join(timeout=3.0)
    scanner.join(timeout=3.0)
    assert not owner.is_alive() and not scanner.is_alive()
    assert owner_errors == [] and scan_errors == []
    assert lock_path.is_file()
    descriptor, identity, payload = owner_result["value"]
    R._release_cell_lock(
        descriptor, identity, payload, lock_path, lock_parent
    )


def test_lock_publication_rejects_temporary_path_inode_substitution(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    task = _task(binary)
    bindings = _bindings(binary)
    lock_parent = operational / "locks/branch/128"
    lock_parent.mkdir(parents=True)
    lock_path = lock_parent / "S000.lock"
    saved_inode = lock_parent / ".substituted-valid-lock-inode"
    real_rename = R._rename_noreplace
    injected = False

    def substitute_source(source: Path, destination: Path) -> None:
        nonlocal injected
        if destination == lock_path and not injected:
            injected = True
            source.rename(saved_inode)
            source.write_bytes(b"{")
        real_rename(source, destination)

    monkeypatch.setattr(R, "_rename_noreplace", substitute_source)
    with pytest.raises(R.BranchProvenanceError, match="strict JSON"):
        _acquire_test_cell_lock(
            lock_path,
            lock_parent,
            operational,
            task,
            bindings,
            0,
        )
    assert injected is True
    assert not lock_path.exists()
    assert saved_inode.is_file()


def test_lock_rename_success_then_interrupt_does_not_leak_live_owner(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    task = _task(binary)
    bindings = _bindings(binary)
    lock_parent = operational / "locks/branch/128"
    lock_parent.mkdir(parents=True)
    lock_path = lock_parent / "S000.lock"
    real_rename = R._rename_noreplace

    def rename_then_interrupt(source: Path, destination: Path) -> None:
        real_rename(source, destination)
        if destination == lock_path:
            raise KeyboardInterrupt

    monkeypatch.setattr(R, "_rename_noreplace", rename_then_interrupt)
    with pytest.raises(KeyboardInterrupt):
        _acquire_test_cell_lock(
            lock_path,
            lock_parent,
            operational,
            task,
            bindings,
            0,
        )
    assert not lock_path.exists()


def test_guard_leaf_replacement_cannot_create_two_exclusive_namespaces(
    tmp_path: Path,
) -> None:
    _output, operational = _roots(tmp_path)
    branch_root = operational / "locks/branch"
    branch_root.mkdir(parents=True)
    first = R._acquire_lock_namespace_guard(operational)
    displaced = operational / "locks/branch-old"
    branch_root.rename(displaced)
    branch_root.mkdir()
    acquired = []
    errors = []

    def acquire_second() -> None:
        try:
            acquired.append(R._acquire_lock_namespace_guard(operational))
        except BaseException as error:
            errors.append(error)

    contender = threading.Thread(target=acquire_second)
    contender.start()
    time.sleep(0.1)
    assert contender.is_alive()
    assert acquired == []
    with pytest.raises(R.BranchProvenanceError, match="unexpected object|identity"):
        R._release_lock_namespace_guard(first)
    contender.join(timeout=3.0)
    assert not contender.is_alive()
    assert acquired == []
    assert len(errors) == 1
    assert isinstance(errors[0], R.BranchProvenanceError)


def test_contended_guard_wait_delivers_sigint_before_holder_release(
    tmp_path: Path,
) -> None:
    _output, operational = _roots(tmp_path)
    (operational / "locks/branch").mkdir(parents=True)
    holder_ready = threading.Event()
    holder_errors = []

    def hold_guard() -> None:
        try:
            guard = R._acquire_lock_namespace_guard(operational)
            holder_ready.set()
            time.sleep(0.8)
            R._release_lock_namespace_guard(guard)
        except BaseException as error:
            holder_errors.append(error)
            holder_ready.set()

    holder = threading.Thread(target=hold_guard)
    holder.start()
    assert holder_ready.wait(timeout=2.0)
    assert holder_errors == []

    def queue_interrupt() -> None:
        time.sleep(0.1)
        os.kill(os.getpid(), signal.SIGINT)

    interrupter = threading.Thread(target=queue_interrupt)
    interrupter.start()
    started = time.monotonic()
    with pytest.raises(KeyboardInterrupt):
        R._acquire_lock_namespace_guard(operational)
    elapsed = time.monotonic() - started
    interrupter.join(timeout=2.0)
    holder.join(timeout=2.0)
    assert not interrupter.is_alive() and not holder.is_alive()
    assert elapsed < 0.5
    assert holder_errors == []


def test_contended_guard_has_explicit_fail_closed_deadline(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _output, operational = _roots(tmp_path)
    (operational / "locks/branch").mkdir(parents=True)
    holder = R._acquire_lock_namespace_guard(operational)
    monkeypatch.setattr(R, "LOCK_GUARD_ACQUIRE_TIMEOUT_SECONDS", 0.05)
    started = time.monotonic()
    try:
        with pytest.raises(R.BranchProvenanceError, match="deadline exceeded"):
            R._acquire_lock_namespace_guard(operational)
    finally:
        R._release_lock_namespace_guard(holder)
    assert time.monotonic() - started < 0.5


def test_single_thread_release_wait_is_interruptible_with_external_holder(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    task = _task(binary)
    bindings = _bindings(binary)
    lock_parent = operational / "locks/branch/128"
    lock_parent.mkdir(parents=True)
    lock_path = lock_parent / "S000.lock"
    descriptor, identity, payload = _acquire_test_cell_lock(
        lock_path,
        lock_parent,
        operational,
        task,
        bindings,
        0,
    )

    ready_read, ready_write = os.pipe()
    holder_pid = os.fork()
    if holder_pid == 0:
        try:
            os.close(ready_read)
            guard = R._acquire_lock_namespace_guard(operational)
            os.write(ready_write, b"1")
            os.close(ready_write)
            time.sleep(0.8)
            R._release_lock_namespace_guard(guard)
            os._exit(0)
        except BaseException:
            os._exit(2)
    os.close(ready_write)
    assert os.read(ready_read, 1) == b"1"
    os.close(ready_read)

    parent_pid = os.getpid()
    sender_pid = os.fork()
    if sender_pid == 0:
        time.sleep(0.1)
        os.kill(parent_pid, signal.SIGINT)
        os._exit(0)

    started = time.monotonic()
    try:
        with pytest.raises(KeyboardInterrupt):
            R._release_cell_lock(
                descriptor, identity, payload, lock_path, lock_parent
            )
        elapsed = time.monotonic() - started
    finally:
        _sender_waited, sender_status = os.waitpid(sender_pid, 0)
        _holder_waited, holder_status = os.waitpid(holder_pid, 0)
    assert os.waitstatus_to_exitcode(sender_status) == 0
    assert os.waitstatus_to_exitcode(holder_status) == 0
    assert elapsed < 0.5
    assert not lock_path.exists()
    with pytest.raises(OSError):
        os.fstat(descriptor)


def test_guard_replay_failure_cleans_unhanded_cell_lock_descriptor(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    task = _task(binary)
    bindings = _bindings(binary)
    lock_parent = operational / "locks/branch/128"
    lock_parent.mkdir(parents=True)
    lock_path = lock_parent / "S000.lock"
    real_open = R.os.open
    publication_descriptor = None

    def capture_publication_descriptor(path, *args, **kwargs):
        nonlocal publication_descriptor
        descriptor = real_open(path, *args, **kwargs)
        if ".lock.publish-" in os.fspath(path):
            publication_descriptor = descriptor
        return descriptor

    real_release = R._release_lock_namespace_guard
    displaced = operational / "locks/branch-old"
    injected = False

    def replace_leaf_then_release(guard):
        nonlocal injected
        if not injected:
            injected = True
            (operational / "locks/branch").rename(displaced)
            (operational / "locks/branch").mkdir()
        return real_release(guard)

    monkeypatch.setattr(R.os, "open", capture_publication_descriptor)
    monkeypatch.setattr(
        R, "_release_lock_namespace_guard", replace_leaf_then_release
    )
    with pytest.raises(R.BranchProvenanceError, match="unexpected object|identity"):
        _acquire_test_cell_lock(
            lock_path,
            lock_parent,
            operational,
            task,
            bindings,
            0,
        )
    assert publication_descriptor is not None
    with pytest.raises(OSError):
        os.fstat(publication_descriptor)
    assert not (operational / "locks/branch/128/S000.lock").exists()
    assert (displaced / "128/S000.lock").is_file()


def test_release_guard_acquisition_interrupt_removes_owned_lock_and_closes_fd(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    task = _task(binary)
    bindings = _bindings(binary)
    lock_parent = operational / "locks/branch/128"
    lock_parent.mkdir(parents=True)
    lock_path = lock_parent / "S000.lock"
    descriptor, identity, payload = _acquire_test_cell_lock(
        lock_path,
        lock_parent,
        operational,
        task,
        bindings,
        0,
    )

    def interrupt_guard(_operational_root: Path, **_kwargs):
        raise KeyboardInterrupt

    monkeypatch.setattr(R, "_acquire_lock_namespace_guard", interrupt_guard)
    with pytest.raises(KeyboardInterrupt):
        R._release_cell_lock(
            descriptor, identity, payload, lock_path, lock_parent
        )
    assert not lock_path.exists()
    with pytest.raises(OSError):
        os.fstat(descriptor)


def test_pending_sigint_after_lock_return_waits_for_caller_ownership(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    real_acquire = R._acquire_cell_lock
    acquired = []

    def acquire_then_queue_sigint(*args, **kwargs):
        result = real_acquire(*args, **kwargs)
        acquired.append(result)
        os.kill(os.getpid(), signal.SIGINT)
        return result

    monkeypatch.setattr(R, "_acquire_cell_lock", acquire_then_queue_sigint)
    with pytest.raises(KeyboardInterrupt):
        _run(tmp_path, binary)
    assert len(acquired) == 1
    descriptor = acquired[0][0]
    assert not (operational / "locks/branch/128/S000.lock").exists()
    with pytest.raises(OSError):
        os.fstat(descriptor)


def test_pending_sigint_after_lifecycle_guard_return_releases_every_owner(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0, counter_code)
    )
    _output, operational = _roots(tmp_path)
    real_acquire = R._acquire_lock_namespace_guard
    call_count = 0
    lifecycle_descriptor = None

    def acquire_then_queue_on_lifecycle(*args, **kwargs):
        nonlocal call_count, lifecycle_descriptor
        guard = real_acquire(*args, **kwargs)
        call_count += 1
        if call_count == 2:
            lifecycle_descriptor = guard.descriptor
            os.kill(os.getpid(), signal.SIGINT)
        return guard

    monkeypatch.setattr(
        R, "_acquire_lock_namespace_guard", acquire_then_queue_on_lifecycle
    )
    with pytest.raises(KeyboardInterrupt):
        _run(tmp_path, binary)
    assert call_count >= 3
    assert lifecycle_descriptor is not None
    with pytest.raises(OSError):
        os.fstat(lifecycle_descriptor)
    assert not (operational / "locks/branch/128/S000.lock").exists()
    assert not (
        operational / "staging/branch/128/.S000.tmp-3333333333333333-0"
    ).exists()
    assert not (tmp_path / "mock_eval.count").exists()


def test_single_owner_lock_rejects_duplicate_admission(tmp_path: Path) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    lock = operational / "locks/branch/128/S000.lock"
    lock.parent.mkdir(parents=True)
    task = _task(binary)
    bindings = _bindings(binary)
    lock.write_bytes(
        R.canonical_json_bytes(
            R._lock_payload(task, bindings, 0, "7" * 32)
        )
    )
    with pytest.raises(R.BranchAlreadyRunningError):
        _run(tmp_path, binary, task=task, bindings=bindings)


def test_malformed_existing_lock_is_not_silently_treated_as_stale(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _output, operational = _roots(tmp_path)
    lock = operational / "locks/branch/128/S000.lock"
    lock.parent.mkdir(parents=True)
    lock.write_text("existing-owner\n", encoding="utf-8")
    with pytest.raises(R.BranchProvenanceError):
        _run(tmp_path, binary)


def test_stale_canonical_lock_is_archived_before_new_owner_is_admitted(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    task = _task(binary)
    bindings = _bindings(binary)
    _output, operational = _roots(tmp_path)
    lock = operational / "locks/branch/128/S000.lock"
    lock.parent.mkdir(parents=True)
    stale = R._lock_payload(task, bindings, 2, "8" * 32)
    stale["pid"] = 999_999_999
    stale["owner_process_start_time"] = 1
    lock.write_bytes(R.canonical_json_bytes(stale))
    with pytest.raises(R.BranchContractError, match="strictly greater attempt"):
        _run(
            tmp_path,
            binary,
            task=task,
            bindings=bindings,
            attempt=2,
        )
    assert lock.is_file()
    result = _run(
        tmp_path,
        binary,
        task=task,
        bindings=bindings,
        attempt=3,
    )
    assert result.record["scheduler_result"]["classification"] == "COMMITTED_EVALUATOR_RESULT"
    archived = (
        operational
        / "interrupted/locks/branch/128/"
        "S000.attempt-2.generation-3333333333333333.owner-"
        f"{'8' * 32}.lock"
    )
    assert archived.is_file()
    assert not lock.exists()


def test_tampered_write_once_manifest_or_raw_bytes_fail_closed(tmp_path: Path) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    stdout = output / "branch/cells/128/S000/stdout.txt"
    stdout.write_bytes(stdout.read_bytes() + b"tamper\n")
    with pytest.raises(R.BranchProvenanceError):
        _run(tmp_path, binary)


def test_record_snapshot_cannot_mix_parsed_bytes_with_later_manifest_hash(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    committed = _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    record_path = output / "branch/cells/128/S000/record.json"
    manifest_path = output / "branch/cell_manifests/128/S000.json"

    attacker_record = json.loads(json.dumps(committed.record))
    attacker_record["authority"] = "ATTACKER_ONLY"
    attacker_record_bytes = R.canonical_json_bytes(attacker_record)
    attacker_manifest = json.loads(json.dumps(committed.manifest))
    record_role = record_path.relative_to(output).as_posix()
    attacker_manifest["files"][record_role] = hashlib.sha256(
        attacker_record_bytes
    ).hexdigest()
    attacker_manifest_bytes = R.canonical_json_bytes(attacker_manifest)

    real_snapshot = R._snapshot_regular_file
    mutated = False

    def mutate_same_inode_after_record_snapshot(path, context, **kwargs):
        nonlocal mutated
        snapshot = real_snapshot(path, context, **kwargs)
        if Path(path) == record_path and not mutated:
            record_path.write_bytes(attacker_record_bytes)
            manifest_path.write_bytes(attacker_manifest_bytes)
            mutated = True
        return snapshot

    monkeypatch.setattr(
        R, "_snapshot_regular_file", mutate_same_inode_after_record_snapshot
    )
    with pytest.raises(R.BranchProvenanceError, match="captured read"):
        _run(tmp_path, binary)
    assert mutated is True


def test_hard_link_alias_in_committed_or_staging_bytes_fails_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    real_validate = R._validate_staging_before_publish

    def inject_hard_link(staging: Path) -> None:
        os.link(staging / "stdout.txt", tmp_path / "staging-stdout-alias")
        real_validate(staging)

    monkeypatch.setattr(R, "_validate_staging_before_publish", inject_hard_link)
    with pytest.raises(R.BranchProvenanceError, match="hard-link alias"):
        _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    assert not (output / "branch/cells/128/S000").exists()


@pytest.mark.parametrize("role", ("cell", "manifest"))
def test_committed_cell_or_manifest_hard_link_alias_is_rejected_on_resume(
    tmp_path: Path, role: str
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    target = (
        output / "branch/cells/128/S000/stdout.txt"
        if role == "cell"
        else output / "branch/cell_manifests/128/S000.json"
    )
    os.link(target, tmp_path / f"{role}-alias")
    with pytest.raises(R.BranchProvenanceError, match="hard-link alias"):
        _run(tmp_path, binary)


def test_committed_manifest_parent_symlink_swap_is_rejected_on_resume(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    manifest_parent = output / "branch/cell_manifests/128"
    relocated_parent = tmp_path / "relocated-manifest-parent"
    manifest_parent.rename(relocated_parent)
    manifest_parent.symlink_to(relocated_parent, target_is_directory=True)

    with pytest.raises(R.BranchProvenanceError, match="symlink component"):
        _run(tmp_path, binary)


@pytest.mark.parametrize("which", ("manifest", "staging"))
def test_symlinked_authoritative_manifest_or_staging_ancestor_fails_before_dispatch(
    tmp_path: Path, which: str
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    output, operational = _roots(tmp_path)
    outside = tmp_path / "outside"
    outside.mkdir()
    if which == "manifest":
        (output / "branch").mkdir(parents=True)
        (output / "branch/cell_manifests").symlink_to(
            outside, target_is_directory=True
        )
    else:
        operational.mkdir(parents=True)
        (operational / "staging").symlink_to(outside, target_is_directory=True)
    with pytest.raises(R.BranchProvenanceError, match="symlink component"):
        _run(tmp_path, binary)
    assert not (tmp_path / "mock_eval.count").exists()
    assert not (output / "branch/cells/128/S000").exists()
    assert not any((operational / "staging/branch/128").iterdir())


def test_resume_exactly_binds_frozen_branch_budgets(tmp_path: Path) -> None:
    counter_code = '''counter = Path(CANONICAL_ARGV0).with_suffix(".count")
with counter.open("a", encoding="utf-8") as stream:
    stream.write("dispatch\\n")
'''
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_CELL_CERTIFIED", 0, counter_code),
    )
    _run(tmp_path, binary)
    changed = R.BranchBudgets(timeout_ms=601_000)
    with pytest.raises(R.BranchProvenanceError, match="budget binding"):
        _run(tmp_path, binary, budgets=changed)
    assert (tmp_path / "mock_eval.count").read_text(encoding="utf-8").splitlines() == ["dispatch"]


def test_pinned_fd_executes_original_inode_and_detects_path_swap(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path,
        _abi_python("BRANCH_CELL_CERTIFIED", 0),
    )
    replacement = _make_executable(
        tmp_path,
        _abi_python("BRANCH_TUBE_UNRESOLVED", 2),
        name="replacement",
    )
    bindings = _bindings(binary)
    real_posix_spawn = R.os.posix_spawn
    swapped = False

    def swap_then_spawn(*args, **kwargs):
        nonlocal swapped
        if not swapped:
            os.replace(replacement, binary)
            swapped = True
        return real_posix_spawn(*args, **kwargs)

    monkeypatch.setattr(R.os, "posix_spawn", swap_then_spawn)
    result = _run(tmp_path, binary, bindings=bindings)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "PROVENANCE_INVALID"
    assert scheduler["failure_reason"] == "PINNED_BINARY_PATH_SWAPPED"
    assert result.record["execution_pin"]["binary"]["path_identity_matches_after"] is False
    output, _operational = _roots(tmp_path)
    raw = (output / "branch/cells/128/S000/stdout.txt").read_text(encoding="utf-8")
    assert "status=BRANCH_CELL_CERTIFIED" in raw
    assert "status=BRANCH_TUBE_UNRESOLVED" not in raw


def test_atomic_directory_publish_never_replaces_concurrent_empty_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    real_rename = R._rename_noreplace
    injected = False

    def inject_empty_target(source: Path, destination: Path) -> None:
        nonlocal injected
        if destination.name == "S000" and not injected:
            destination.mkdir()
            injected = True
        real_rename(source, destination)

    monkeypatch.setattr(R, "_rename_noreplace", inject_empty_target)
    with pytest.raises(R.BranchProvenanceError, match="target already exists"):
        _run(tmp_path, binary)
    output, operational = _roots(tmp_path)
    target = output / "branch/cells/128/S000"
    assert target.is_dir() and not any(target.iterdir())
    assert not (output / "branch/cell_manifests/128/S000.json").exists()
    staging = operational / "staging/branch/128/.S000.tmp-3333333333333333-0"
    assert staging.is_dir()


@pytest.mark.parametrize("control", ("\n", "\x1f", "\x7f", "\\"))
def test_argv0_path_control_or_alias_injection_is_rejected(
    tmp_path: Path, control: str
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_CELL_CERTIFIED", 0)
    )
    task = _task(binary)
    forged = R.BranchCellTask(
        precision_bits=task.precision_bits,
        slab_id=task.slab_id,
        epsilon=task.epsilon,
        root_box=task.root_box,
        evaluator_binary_path=task.evaluator_binary_path + control,
        accepted_l1_primary_record_id=task.accepted_l1_primary_record_id,
        accepted_l1_primary_record_sha256=task.accepted_l1_primary_record_sha256,
    )
    with pytest.raises(R.BranchContractError):
        forged.validate()


@pytest.mark.parametrize("mode", ("missing", "duplicate"))
def test_missing_or_duplicate_argv0_echo_is_malformed(
    tmp_path: Path, mode: str
) -> None:
    text = _abi_python("BRANCH_CELL_CERTIFIED", 0)
    if mode == "missing":
        text = text.replace(
            '        print(f"input_arg_{index:02d}={value}")',
            '        if index != 0:\n            print(f"input_arg_{index:02d}={value}")',
        )
    else:
        text = text.replace(
            "\nemit_common()\n",
            '\nprint(f"input_arg_00={CANONICAL_ARGV0}")\nemit_common()\n',
            1,
        )
    binary = _make_executable(tmp_path, text)
    result = _run(tmp_path, binary)
    scheduler = result.record["scheduler_result"]
    assert scheduler["classification"] == "MALFORMED_EVALUATOR_OUTPUT"
    assert scheduler["evaluator_status"] is None
    assert "INPUT_ECHO_MISMATCH:input_arg_00" in scheduler["failure_reason"]


def test_runtime_contains_no_compile_or_unbounded_capture_path() -> None:
    text = RUNTIME.read_text(encoding="utf-8")
    assert "capture_output=True" not in text
    assert "os.posix_spawn(" in text
    assert "setpgroup=0" in text
    assert "setsigmask=child_signal_mask" in text
    assert 'executable_path = f"/proc/self/fd/{execution_descriptor}"' in text
    assert "os.POSIX_SPAWN_DUP2" in text
    assert "os.killpg" in text
    assert 'getattr(libc, "renameat2", None)' in text
    assert "os.rename(" not in text
    assert '"g++"' not in text
    assert "capd-config" not in text
    assert "subprocess.run(" not in text
    assert "if __name__ ==" not in text


def test_record_and_manifest_are_canonical_json_without_authority_widening(
    tmp_path: Path,
) -> None:
    binary = _make_executable(
        tmp_path, _abi_python("BRANCH_TUBE_VIOLATION", 4)
    )
    result = _run(tmp_path, binary)
    output, _operational = _roots(tmp_path)
    record_path = output / "branch/cells/128/S000/record.json"
    manifest_path = output / "branch/cell_manifests/128/S000.json"
    assert record_path.read_bytes() == R.canonical_json_bytes(result.record)
    assert manifest_path.read_bytes() == R.canonical_json_bytes(result.manifest)
    for payload in (result.record, result.manifest):
        assert payload["authority"] == "PRODUCER_ONLY"
        assert payload["scientific_licensing_enabled"] is False
        assert payload["component_status"] is None
        assert payload["milestone_status"] is None
        assert payload["theorem_status"] is None
        assert payload["final_status"] is None
    assert result.record["scheduler_result"]["classification"] == "COMMITTED_EVALUATOR_RESULT"
    assert result.record["scheduler_result"]["evaluator_status"] == "BRANCH_TUBE_VIOLATION"
    assert result.record["budgets"] == R.BranchBudgets().payload()
    assert result.manifest["budgets"] == R.BranchBudgets().payload()
    assert result.record["invocation"]["argv0_scheduler_binding"] == str(
        binary.resolve()
    )
    assert result.record["invocation"]["argument_echo_count"] == 12
    for pin in result.record["execution_pin"].values():
        assert pin["descriptor_hash_matches_after"] is True
        assert pin["descriptor_identity_matches_after"] is True
        assert pin["path_identity_matches_after"] is True
    assert json.loads(record_path.read_text(encoding="utf-8")) == result.record


def _branch_archive_bytes(output: Path) -> dict[str, bytes]:
    branch = output / "branch"
    return {
        path.relative_to(branch).as_posix(): path.read_bytes()
        for path in sorted(branch.rglob("*"))
        if path.is_file()
    }


def _run_mock_checker(source: Path, output: Path, *, postcheck: bool) -> None:
    command = [
        sys.executable,
        str(source),
        "--input-dir",
        str(output),
    ]
    if postcheck:
        command.append("--postcheck")
    completed = subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


def test_mock_task_builder_binds_exact_l1_records_and_cross_precision_domains() -> None:
    tasks = S.build_mock_branch_tasks(MOCK_EVALUATOR.resolve())
    assert len(tasks) == 102
    assert [(task.precision_bits, task.slab_id) for task in tasks] == [
        (cell.precision_bits, cell.slab_id) for cell in S.exact_matrix()
    ]
    assert tasks[0].accepted_l1_primary_record_id == "128/S000/primary"
    assert tasks[51].accepted_l1_primary_record_id == "256/S000/primary"
    assert tasks[0].epsilon == ("0.0000", "0.0021")
    assert tasks[0].root_box == (
        ("-0.0000621099303404812157", "0.0000178900696595187843"),
        ("0.149388644835276716", "0.149428644835276716"),
        ("-0.00008", "0.00008"),
        ("0.663823949234225406", "0.663863949234225406"),
    )
    for index in range(51):
        assert tasks[index].epsilon == tasks[51 + index].epsilon
        assert tasks[index].root_box == tasks[51 + index].root_box
        assert tasks[index].accepted_l1_primary_record_sha256 != (
            tasks[51 + index].accepted_l1_primary_record_sha256
        )
    assert S.canonical_decimal_token("0.0000") == "0"
    assert S.canonical_decimal_token("-0.000") == "0"


def test_complete_102_mock_branch_archive_partial_resume_and_aggregate(
    tmp_path: Path,
) -> None:
    output = tmp_path / "archive"
    static = S.run_mock_static(output, 102, resume=False)
    assert static["aggregate_finalized"] is True
    _run_mock_checker(STATIC_CHECKER, output, postcheck=False)
    _run_mock_checker(STATIC_CHECKER, output, postcheck=True)

    partial = S.run_mock_branch(
        output,
        MOCK_EVALUATOR,
        18,
        resume=False,
        completion_delays={
            f"128:S{index:03d}": (5 - index % 6) * 0.002
            for index in range(18)
        },
    )
    assert partial["completed_cells"] == 18
    assert partial["barrier_count"] == 3
    assert partial["promotion_blocked"] is False
    assert partial["aggregate_finalized"] is False
    assert not S.branch_aggregate_summary_path(output).exists()
    assert not S.branch_aggregate_manifest_path(output).exists()

    completed = S.run_mock_branch(
        output,
        MOCK_EVALUATOR,
        102,
        resume=True,
    )
    assert completed["completed_cells"] == 102
    assert completed["barrier_count"] == 17
    assert completed["promotion_blocked"] is False
    assert completed["aggregate_finalized"] is True
    assert sum(
        state["state"] == "RESUMED_COMMITTED"
        for state in completed["states"]
    ) == 18
    summary_path = S.branch_aggregate_summary_path(output)
    manifest_path = S.branch_aggregate_manifest_path(output)
    summary_before = summary_path.read_bytes()
    manifest_before = manifest_path.read_bytes()
    summary = S.strict_json_load(summary_path, require_canonical=True)
    manifest = S.strict_json_load(manifest_path, require_canonical=True)
    assert summary["cell_count"] == 102
    assert summary["matrix"] == S.matrix_payload()
    assert summary["status_counts"] == {"BRANCH_CELL_CERTIFIED": 102}
    assert summary["scheduler_classification_counts"] == {
        "COMMITTED_EVALUATOR_RESULT": 102
    }
    assert summary["mock_only"] is True
    assert summary["scientific_licensing_enabled"] is False
    assert summary["component_status"] is None
    assert summary["milestone_status"] is None
    assert summary["theorem_status"] is None
    assert summary["final_status"] is None
    assert len(manifest["cell_manifests"]) == 102
    assert manifest["cell_manifests"][0]["path"] == (
        "branch/cell_manifests/128/S000.json"
    )
    assert manifest["cell_manifests"][-1]["path"] == (
        "branch/cell_manifests/256/S050.json"
    )
    assert manifest["ordered_cell_manifest_root"] == S.sha256_bytes(
        S.canonical_json_bytes(manifest["cell_manifests"])
    )
    assert manifest["summary"] == {
        "path": "branch/aggregate_summary.json",
        "sha256": S.sha256(summary_path),
        "size_bytes": summary_path.stat().st_size,
    }

    resumed = S.run_mock_branch(
        output,
        MOCK_EVALUATOR,
        102,
        resume=True,
    )
    assert resumed["aggregate"]["state"] == "RESUMED_COMMITTED"
    assert all(
        state["state"] == "RESUMED_COMMITTED" for state in resumed["states"]
    )
    assert summary_path.read_bytes() == summary_before
    assert manifest_path.read_bytes() == manifest_before

    _run_mock_checker(BRANCH_CHECKER, output, postcheck=False)
    _run_mock_checker(BRANCH_CHECKER, output, postcheck=True)
    composite_state, composite_summary, composite_manifest = (
        S.finalize_mock_composite_controls(output)
    )
    assert composite_state == "COMMITTED"
    assert composite_summary["cell_count_per_component"] == 102
    assert composite_summary["component_status"] is None
    assert composite_summary["milestone_status"] is None
    assert composite_summary["theorem_status"] is None
    assert composite_summary["final_status"] is None
    assert composite_manifest["archive_generation_sha256"] == (
        composite_summary["archive_generation_sha256"]
    )
    _run_mock_checker(COMPOSITE_CHECKER, output, postcheck=False)
    _run_mock_checker(COMPOSITE_CHECKER, output, postcheck=True)
    downstream_before = {
        name: (output / name).read_bytes()
        for name in (
            "composite_summary.json",
            "composite_manifest.json",
            "independent_checker.json",
            "POSTCHECK_STATUS.json",
        )
    }
    composite_resume, _, _ = S.finalize_mock_composite_controls(output)
    assert composite_resume == "RESUMED_COMMITTED"
    assert {
        name: (output / name).read_bytes() for name in downstream_before
    } == downstream_before


def test_mock_barrier_completion_order_does_not_change_canonical_branch_bytes(
    tmp_path: Path,
) -> None:
    output = tmp_path / "stable-path"
    S.run_mock_static(output, 102, resume=False)
    first = S.run_mock_branch(
        output,
        MOCK_EVALUATOR,
        12,
        resume=False,
        completion_delays={
            f"128:S{index:03d}": (index % 6) * 0.05
            for index in range(12)
        },
    )
    assert first["completed_cells"] == 12
    first_bytes = _branch_archive_bytes(output)
    first_completion = first["barrier_completion_order"]

    quarantined, quarantined_operational = S.quarantine_incompatible_generation(
        output, "MOCK_COMPLETION_ORDER_REPLAY"
    )
    assert quarantined.is_dir()
    assert quarantined_operational is not None
    assert quarantined_operational.is_dir()
    assert not output.exists()
    S.run_mock_static(output, 102, resume=False)
    second = S.run_mock_branch(
        output,
        MOCK_EVALUATOR,
        12,
        resume=False,
        completion_delays={
            f"128:S{index:03d}": (5 - index % 6) * 0.05
            for index in range(12)
        },
    )
    assert second["completed_cells"] == 12
    assert second["barrier_completion_order"] != first_completion
    assert _branch_archive_bytes(output) == first_bytes


def test_branch_aggregate_rejects_extra_namespace_and_live_stage(
    tmp_path: Path,
) -> None:
    output = tmp_path / "archive"
    S.run_mock_static(output, 102, resume=False)
    S.run_mock_branch(output, MOCK_EVALUATOR, 102, resume=False)
    run_config_sha256 = S.sha256(S.run_config_path(output))
    stage = (
        S.operational_root_for(output)
        / "staging"
        / "branch"
        / "128"
        / f".S000.tmp-{run_config_sha256[:16]}-0"
    )
    stage.mkdir()
    run_config = S.strict_json_load(
        S.run_config_path(output), require_canonical=True
    )
    mock_evaluator = S.validate_mock_branch_evaluator(output, MOCK_EVALUATOR)
    tasks = S.build_mock_branch_tasks(MOCK_EVALUATOR)
    bindings = S.mock_branch_bindings(
        run_config["matrix_id"], run_config_sha256, mock_evaluator
    )
    with pytest.raises(S.CorruptGeneration, match="live staging owners"):
        S.validate_branch_mock_aggregate(
            output,
            tasks,
            bindings,
            R.BranchBudgets(),
            mock_evaluator,
        )
