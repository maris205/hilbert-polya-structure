from contextlib import contextmanager
import errno
import os
from pathlib import Path

import pytest

from candidate_v1.bootstrap import launcher
from candidate_v1.bootstrap.lifecycle import bounded_child_diagnostic


def _write_script(path, body):
    path.write_text(body, encoding="utf-8")
    return path


@contextmanager
def _descriptor_three_mode(open_descriptor, tmp_path, open_inheritable=False):
    original = launcher._descriptor_snapshot(3)
    saved = os.dup(3) if original is not None else None
    saved_inheritable = original["inheritable"] if original is not None else False
    try:
        try:
            os.close(3)
        except OSError as exc:
            if exc.errno != errno.EBADF:
                raise
        if open_descriptor:
            descriptor = os.open(tmp_path / "fd3-sentinel", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            if descriptor != 3:
                os.dup2(descriptor, 3, inheritable=open_inheritable)
                os.close(descriptor)
            else:
                os.set_inheritable(3, open_inheritable)
        expected = launcher._descriptor_snapshot(3)
        yield expected
        assert launcher._descriptor_snapshot(3) == expected
    finally:
        launcher._restore_descriptor_three(saved, saved_inheritable)
        assert launcher._descriptor_snapshot(3) == original


def _run_matrix(open_descriptor, tmp_path, monkeypatch, open_inheritable=False):
    success = _write_script(
        tmp_path / ("success-open.py" if open_descriptor else "success-closed.py"),
        "import os\nos.read(3, 4096)\nos.write(1, b'ok')\n",
    )
    nonzero = _write_script(
        tmp_path / ("nonzero-open.py" if open_descriptor else "nonzero-closed.py"),
        "import os\nos.read(3, 4096)\nos.write(1, b'out')\nos.write(2, b'err')\nraise SystemExit(7)\n",
    )
    timeout = _write_script(
        tmp_path / ("timeout-open.py" if open_descriptor else "timeout-closed.py"),
        "import os, time\nos.read(3, 4096)\ntime.sleep(60)\n",
    )
    overflow = _write_script(
        tmp_path / ("overflow-open.py" if open_descriptor else "overflow-closed.py"),
        "import os\nos.read(3, 4096)\nos.write(1, b'x' * 70000)\n",
    )
    injected = _write_script(
        tmp_path / ("injected-open.py" if open_descriptor else "injected-closed.py"),
        "import os, time\nos.read(3, 4096)\ntime.sleep(60)\n",
    )
    with _descriptor_three_mode(open_descriptor, tmp_path, open_inheritable) as expected:
        stdout, diagnostic = launcher._run_child(success, b"capability\n", tmp_path, 3)
        assert stdout == b"ok" and diagnostic["returncode"] == 0
        assert launcher._descriptor_snapshot(3) == expected

        with pytest.raises(launcher.ChildLaunchError) as caught:
            launcher._run_child(nonzero, b"capability\n", tmp_path, 3)
        assert caught.value.child_diagnostic["returncode"] == 7
        assert caught.value.child_diagnostic["stdout"]["text"] == "out"
        assert caught.value.child_diagnostic["stderr"]["text"] == "err"
        assert launcher._descriptor_snapshot(3) == expected

        with pytest.raises(launcher.ChildLaunchError) as caught:
            launcher._run_child(timeout, b"capability\n", tmp_path, 1)
        assert caught.value.child_diagnostic["timed_out"] is True
        assert caught.value.child_diagnostic["returncode"] is None
        assert launcher._descriptor_snapshot(3) == expected

        with pytest.raises(launcher.ChildLaunchError) as caught:
            launcher._run_child(overflow, b"capability\n", tmp_path, 3)
        assert "stream cap" in str(caught.value)
        assert caught.value.child_diagnostic["stdout"]["byte_count"] > launcher.MAX_CHILD_STREAM_BYTES
        assert caught.value.child_diagnostic["stdout"]["truncated"] is True
        assert launcher._descriptor_snapshot(3) == expected

        real_popen = launcher.subprocess.Popen
        spawned = []

        def recording_popen(*arguments, **keywords):
            process = real_popen(*arguments, **keywords)
            spawned.append(process)

            def injected_poll():
                raise KeyboardInterrupt("injected poll failure")

            process.poll = injected_poll
            return process

        with monkeypatch.context() as local_patch:
            local_patch.setattr(launcher.subprocess, "Popen", recording_popen)
            with pytest.raises(launcher.ChildLaunchError) as caught:
                launcher._run_child(injected, b"capability\n", tmp_path, 3)
        assert isinstance(caught.value.__cause__, KeyboardInterrupt)
        assert spawned and spawned[0].wait(timeout=2) is not None
        assert launcher._descriptor_snapshot(3) == expected


def test_fd3_closed_matrix_success_nonzero_timeout_overflow_and_injected_exception(tmp_path, monkeypatch):
    _run_matrix(False, tmp_path, monkeypatch)


def test_fd3_open_matrix_success_nonzero_timeout_overflow_and_injected_exception(tmp_path, monkeypatch):
    for inheritable in (False, True):
        case_root = tmp_path / ("noninheritable" if not inheritable else "inheritable")
        case_root.mkdir()
        _run_matrix(True, case_root, monkeypatch, inheritable)


def _pid_is_gone_or_zombie(pid):
    stat_path = Path("/proc") / str(pid) / "stat"
    if not stat_path.exists():
        return True
    try:
        fields = stat_path.read_text(encoding="ascii").split()
    except (FileNotFoundError, ProcessLookupError):
        return True
    return len(fields) > 2 and fields[2] == "Z"


def test_descendant_timeout_overflow_and_closed_pipe_are_group_reaped(tmp_path):
    for round_index in range(3):
        suffix = "-" + str(round_index) + ".py"
        hold = _write_script(
            tmp_path / ("descendant-hold" + suffix),
            "import os, time\nos.read(3,4096)\npid=os.fork()\nif pid==0:\n time.sleep(60)\nelse:\n os.write(1,(str(pid)+'\\n').encode())\n os._exit(0)\n",
        )
        with pytest.raises(launcher.ChildLaunchError) as caught:
            launcher._run_child(hold, b"cap\n", tmp_path, 1)
        assert caught.value.child_diagnostic["timed_out"] is True
        held_pid = int(caught.value.child_diagnostic["stdout"]["text"].strip())
        assert _pid_is_gone_or_zombie(held_pid)

        closed = _write_script(
            tmp_path / ("descendant-closed" + suffix),
            "import os, time\nos.read(3,4096)\npid=os.fork()\nif pid==0:\n os.close(1); os.close(2); time.sleep(60)\nelse:\n os.write(1,(str(pid)+'\\n').encode())\n",
        )
        stdout, diagnostic = launcher._run_child(closed, b"cap\n", tmp_path, 3)
        assert diagnostic["returncode"] == 0
        closed_pid = int(stdout.strip())
        assert _pid_is_gone_or_zombie(closed_pid)

        overflowing = _write_script(
            tmp_path / ("descendant-overflow" + suffix),
            "import os, time\nos.read(3,4096)\npid=os.fork()\nif pid==0:\n os.write(1,b'x'*70000); time.sleep(60)\nelse:\n os.write(2,(str(pid)+'\\n').encode())\n",
        )
        with pytest.raises(launcher.ChildLaunchError) as caught:
            launcher._run_child(overflowing, b"cap\n", tmp_path, 3)
        overflow_pid = int(caught.value.child_diagnostic["stderr"]["text"].strip())
        assert caught.value.child_diagnostic["stdout"]["truncated"] is True
        assert _pid_is_gone_or_zombie(overflow_pid)


def test_protocol_and_start_failures_preserve_bounded_diagnostics(paper_root, tmp_path, monkeypatch):
    script = _write_script(tmp_path / "unused.py", "pass\n")
    with pytest.raises(launcher.ChildLaunchError) as caught:
        launcher._run_child(script, b"cap\n", tmp_path / "missing", 3)
    assert caught.value.child_diagnostic["returncode"] == 127
    assert "FileNotFoundError" in caught.value.child_diagnostic["stderr"]["text"]

    diagnostic = bounded_child_diagnostic(0, b"{}\n", b"", False)
    with monkeypatch.context() as local_patch:
        local_patch.setattr(launcher, "_run_child", lambda *args, **kwargs: (b"{}\n", diagnostic))
        with pytest.raises(launcher.ChildLaunchError) as protocol:
            launcher.launch_safe_probe(paper_root, "Q")
    assert protocol.value.child_diagnostic == diagnostic
    assert isinstance(protocol.value.__cause__, (ValueError, KeyError))

    proc_failure_script = _write_script(
        tmp_path / "proc-scan-failure.py",
        "import os, time\nos.read(3,4096)\nos.close(1)\nos.close(2)\ntime.sleep(60)\n",
    )
    real_popen = launcher.subprocess.Popen
    spawned = []

    def recording_popen(*arguments, **keywords):
        process = real_popen(*arguments, **keywords)
        spawned.append(process)
        return process

    def fail_proc_scan(_group_id):
        raise OSError("injected proc scan failure after initial group kill")

    with monkeypatch.context() as local_patch:
        local_patch.setattr(launcher.subprocess, "Popen", recording_popen)
        local_patch.setattr(launcher, "_live_process_group_members", fail_proc_scan)
        with pytest.raises(launcher.ChildLaunchError, match="cleanup failed"):
            launcher._run_child(proc_failure_script, b"cap\n", tmp_path, 3)
    assert spawned and spawned[0].wait(timeout=2) is not None


def test_real_safe_probe_q_never_loads_science(paper_root):
    result = launcher.launch_safe_probe(paper_root, "Q")
    assert result["diagnostic"]["returncode"] == 0
    assert result["response"]["access_counters"] == launcher.SAFE_PROBE_EXPECTED_COUNTS
    assert result["response"]["access_counters"]["run_science_call_count"] == 0
    assert result["response"]["access_log"]["allowed_read_counts"] == {
        "code/candidate_v1/shared/definitions.json": 1,
        "code/candidate_v1/track_q/runner.py": 0,
    }


def test_real_safe_probe_r_never_loads_science(paper_root):
    result = launcher.launch_safe_probe(paper_root, "R")
    assert result["diagnostic"]["returncode"] == 0
    assert result["response"]["access_counters"] == launcher.SAFE_PROBE_EXPECTED_COUNTS
    assert result["response"]["access_counters"]["run_science_call_count"] == 0
    assert result["response"]["access_log"]["allowed_read_counts"] == {
        "code/candidate_v1/shared/definitions.json": 1,
        "code/candidate_v1/track_r/runner.py": 0,
    }
