"""Real isolated child launch with capability-fd restoration and diagnostics."""

import errno
import fcntl
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

from .canonical import canonical_bytes, read_regular_bytes, sha256_bytes, strict_canonical_load
from .constants import (
    CANDIDATE_ID,
    DEFINITIONS_RELATIVE,
    Q_ENGINE_RELATIVE,
    Q_FIXTURE_RELATIVE,
    Q_RUNNER_RELATIVE,
    R_ENGINE_RELATIVE,
    R_FIXTURE_RELATIVE,
    R_RUNNER_RELATIVE,
)
from .lifecycle import bounded_child_diagnostic


class ChildLaunchError(RuntimeError):
    def __init__(self, message, diagnostic):
        super().__init__(message)
        self.child_diagnostic = diagnostic


MAX_CHILD_STREAM_BYTES = 65536
PROCESS_GROUP_QUIESCENCE_SECONDS = 2
SAFE_PROBE_EXPECTED_COUNTS = {
    "denied_cross_track_read_count": 1,
    "denied_dynamic_loader_count": 2,
    "denied_ledger_read_count": 1,
    "denied_network_count": 1,
    "denied_outside_read_count": 3,
    "denied_outside_write_count": 3,
    "denied_process_count": 2,
    "denied_review_read_count": 1,
    "denied_source_read_count": 1,
    "run_science_call_count": 0,
    "successful_outside_read_count": 0,
    "successful_outside_write_count": 0,
}


def _descriptor_snapshot(descriptor):
    try:
        stat = os.fstat(descriptor)
    except OSError as exc:
        if exc.errno == errno.EBADF:
            return None
        raise
    return {
        "device": stat.st_dev,
        "inode": stat.st_ino,
        "mode": stat.st_mode,
        "inheritable": os.get_inheritable(descriptor),
    }


def _restore_descriptor_three(saved_descriptor, saved_inheritable):
    try:
        os.close(3)
    except OSError as exc:
        if exc.errno != errno.EBADF:
            raise
    if saved_descriptor is not None:
        try:
            os.dup2(saved_descriptor, 3, inheritable=saved_inheritable)
        finally:
            os.close(saved_descriptor)


def _safe_close_descriptor(descriptor):
    if descriptor is None:
        return None
    try:
        os.close(descriptor)
    except BaseException as exc:
        if not isinstance(exc, OSError) or exc.errno != errno.EBADF:
            return exc
    return None


def _safe_close_stream(stream):
    try:
        if stream is None or stream.closed:
            return None
        stream.close()
    except BaseException as exc:
        return exc
    return None


def _safe_close_process_stream(process, name):
    try:
        stream = getattr(process, name)
    except BaseException as exc:
        return exc
    return _safe_close_stream(stream)


def _safe_poll(process):
    if process is None:
        return None, None
    try:
        return process.poll(), None
    except BaseException as exc:
        return None, exc


def _leader_exited_without_reap(process):
    """Observe the isolated leader without consuming its wait status."""
    if process is None:
        return True
    if process.returncode is not None:
        return True
    try:
        information = os.waitid(
            os.P_PID,
            process.pid,
            os.WEXITED | os.WNOHANG | os.WNOWAIT,
        )
    except ChildProcessError:
        return process.returncode is not None
    return information is not None


def _kill_isolated_process_group(process):
    """Kill the session created for one child without ever targeting our group."""
    try:
        if process is None:
            return None
        group_id = process.pid
        if type(group_id) is not int or group_id <= 1 or group_id == os.getpgrp():
            return RuntimeError("unsafe isolated process-group identity")
        os.killpg(group_id, signal.SIGKILL)
    except ProcessLookupError:
        pass
    except BaseException as exc:
        return exc
    return None


def _live_process_group_members(group_id):
    """Return non-zombie Linux /proc members, or None when /proc is unavailable."""
    proc_root = Path("/proc")
    try:
        if not proc_root.is_dir():
            return None
        entries = list(proc_root.iterdir())
    except OSError:
        return None
    live_members = []
    for entry in entries:
        if not entry.name.isdecimal():
            continue
        try:
            stat_text = (entry / "stat").read_text(encoding="ascii")
        except OSError as exc:
            if exc.errno in (errno.ENOENT, errno.ESRCH):
                continue
            raise
        closing_parenthesis = stat_text.rfind(")")
        if closing_parenthesis < 0:
            raise RuntimeError("malformed /proc process stat record")
        fields = stat_text[closing_parenthesis + 1 :].split()
        if len(fields) < 4:
            raise RuntimeError("short /proc process stat record")
        state = fields[0]
        try:
            process_group = int(fields[2])
            session_id = int(fields[3])
            pid = int(entry.name)
        except ValueError as exc:
            raise RuntimeError("nonintegral /proc process stat record") from exc
        if (
            process_group == group_id
            and session_id == group_id
            and state not in {"Z", "X", "x"}
        ):
            live_members.append(pid)
    return sorted(live_members)


def _quiesce_isolated_process_group(process):
    """Kill and observe the isolated group before its leader can be reaped."""
    if process is None:
        return None
    group_id = process.pid
    if type(group_id) is not int or group_id <= 1 or group_id == os.getpgrp():
        return RuntimeError("unsafe isolated process-group identity")
    deadline = time.monotonic() + PROCESS_GROUP_QUIESCENCE_SECONDS
    last_live_members = None
    initial_kill_error = _kill_isolated_process_group(process)
    if initial_kill_error is not None:
        return initial_kill_error
    while True:
        try:
            live_members = _live_process_group_members(group_id)
        except BaseException as exc:
            return exc
        if live_members is not None:
            if not live_members:
                return None
            last_live_members = live_members
        else:
            try:
                os.killpg(group_id, 0)
            except ProcessLookupError:
                return None
            except BaseException as exc:
                return exc
            last_live_members = [group_id]
        kill_error = _kill_isolated_process_group(process)
        if kill_error is not None:
            return kill_error
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return RuntimeError(
                "isolated process group did not quiesce: "
                + ",".join(str(pid) for pid in last_live_members)
            )
        time.sleep(min(0.01, remaining))


def _add_cleanup_error(current, new_error, label):
    if new_error is None:
        return current
    if current is None:
        return new_error
    try:
        current.add_note(label + ": " + repr(new_error))
    except BaseException:
        pass
    return current


def _run_child(script: Path, token: bytes, working_directory: Path, timeout_seconds):
    if type(token) is not bytes or not token:
        raise TypeError("nonempty capability bytes required")
    if type(timeout_seconds) not in (int,) or timeout_seconds <= 0:
        raise TypeError("positive integral timeout required")
    original_snapshot = _descriptor_snapshot(3)
    saved_descriptor = None
    saved_inheritable = False
    if original_snapshot is not None:
        saved_inheritable = original_snapshot["inheritable"]
        saved_descriptor = os.dup(3)
    read_descriptor = None
    write_descriptor = None
    completed_returncode = None
    captured_stdout = b""
    captured_stderr = b""
    timed_out = False
    overflowed = False
    pending_error = None
    restoration_error = None
    unexpected_error = None
    cleanup_error = None
    process = None
    process_group_quiesced = False
    process_leader_reaped = False
    selector = None
    termination_deadline = None
    stdout_buffer = bytearray()
    stderr_buffer = bytearray()
    try:
        read_descriptor, write_descriptor = os.pipe()
        if read_descriptor != 3:
            os.dup2(read_descriptor, 3, inheritable=True)
            os.close(read_descriptor)
            read_descriptor = None
        else:
            os.set_inheritable(3, True)
            read_descriptor = None
        offset = 0
        while offset < len(token):
            written = os.write(write_descriptor, token[offset:])
            if written <= 0:
                raise OSError("short capability write")
            offset += written
        os.close(write_descriptor)
        write_descriptor = None
        try:
            process = subprocess.Popen(
                [sys.executable, "-I", "-S", "-B", os.fspath(script)],
                cwd=working_directory,
                env={
                    "LANG": "C",
                    "LC_ALL": "C",
                    "PATH": os.defpath,
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                pass_fds=(3,),
                start_new_session=True,
            )
        except OSError as exc:
            diagnostic = bounded_child_diagnostic(
                127,
                b"",
                (type(exc).__name__ + ": " + str(exc)).encode("utf-8", errors="backslashreplace"),
                False,
            )
            pending_error = ChildLaunchError("isolated child could not start", diagnostic)
        else:
            selector = selectors.DefaultSelector()
            streams = {
                process.stdout.fileno(): ("stdout", stdout_buffer),
                process.stderr.fileno(): ("stderr", stderr_buffer),
            }
            for descriptor in streams:
                os.set_blocking(descriptor, False)
                selector.register(descriptor, selectors.EVENT_READ)
            deadline = time.monotonic() + timeout_seconds
            while selector.get_map():
                now = time.monotonic()
                if termination_deadline is not None and now >= termination_deadline:
                    break
                remaining = deadline - now
                if remaining <= 0 and not timed_out:
                    timed_out = True
                    cleanup_error = _add_cleanup_error(
                        cleanup_error,
                        _kill_isolated_process_group(process),
                        "timeout group kill",
                    )
                    termination_deadline = time.monotonic() + 2
                    remaining = 1
                if termination_deadline is not None:
                    remaining = min(remaining, termination_deadline - time.monotonic())
                events = selector.select(min(max(remaining, 0), 1))
                if not events and _leader_exited_without_reap(process):
                    events = [(key, selectors.EVENT_READ) for key in selector.get_map().values()]
                for key, _mask in events:
                    descriptor = key.fd
                    try:
                        block = os.read(descriptor, 8192)
                    except BlockingIOError:
                        continue
                    if not block:
                        selector.unregister(descriptor)
                        continue
                    _name, buffer = streams[descriptor]
                    if len(buffer) + len(block) > MAX_CHILD_STREAM_BYTES:
                        remaining_capacity = MAX_CHILD_STREAM_BYTES + 1 - len(buffer)
                        if remaining_capacity > 0:
                            buffer.extend(block[:remaining_capacity])
                        overflowed = True
                        if termination_deadline is None:
                            termination_deadline = time.monotonic() + 2
                        cleanup_error = _add_cleanup_error(
                            cleanup_error,
                            _kill_isolated_process_group(process),
                            "overflow group kill",
                        )
                    else:
                        buffer.extend(block)
            # Before reaping the session leader, remove any descendant that
            # closed the captured pipes and would otherwise survive unseen.
            pre_reap_error = _quiesce_isolated_process_group(process)
            cleanup_error = _add_cleanup_error(
                cleanup_error,
                pre_reap_error,
                "pre-reap group quiescence",
            )
            process_group_quiesced = pre_reap_error is None
            selector.close()
            selector = None
            try:
                completed_returncode = process.wait(timeout=2)
                process_leader_reaped = True
            except subprocess.TimeoutExpired:
                cleanup_error = _add_cleanup_error(
                    cleanup_error,
                    _kill_isolated_process_group(process),
                    "wait group kill",
                )
                completed_returncode = process.wait(timeout=2)
                process_leader_reaped = True
            captured_stdout = bytes(stdout_buffer)
            captured_stderr = bytes(stderr_buffer)
            process.stdout.close()
            process.stderr.close()
    except BaseException as exc:
        unexpected_error = exc
    finally:
        # Cleanup errors are accumulated, never allowed to bypass fd3 restoration.
        if process is not None and not process_group_quiesced and not process_leader_reaped:
            cleanup_error = _add_cleanup_error(
                cleanup_error,
                _quiesce_isolated_process_group(process),
                "final group quiescence",
            )
        final_status, final_poll_error = _safe_poll(process)
        cleanup_error = _add_cleanup_error(
            cleanup_error,
            final_poll_error,
            "initial final poll",
        )
        if final_status is not None:
            process_leader_reaped = True
        if selector is not None:
            try:
                selector.close()
            except BaseException as exc:
                cleanup_error = _add_cleanup_error(cleanup_error, exc, "selector close")
        if process is not None:
            final_status, final_poll_error = _safe_poll(process)
            cleanup_error = _add_cleanup_error(
                cleanup_error,
                final_poll_error,
                "post-kill poll",
            )
            if final_status is None:
                try:
                    completed_returncode = process.wait(timeout=2)
                    process_leader_reaped = True
                except BaseException as exc:
                    cleanup_error = _add_cleanup_error(cleanup_error, exc, "child wait")
            else:
                completed_returncode = final_status
                process_leader_reaped = True
            cleanup_error = _add_cleanup_error(
                cleanup_error,
                _safe_close_process_stream(process, "stdout"),
                "stdout close",
            )
            cleanup_error = _add_cleanup_error(
                cleanup_error,
                _safe_close_process_stream(process, "stderr"),
                "stderr close",
            )
        cleanup_error = _add_cleanup_error(
            cleanup_error,
            _safe_close_descriptor(write_descriptor),
            "capability writer close",
        )
        cleanup_error = _add_cleanup_error(
            cleanup_error,
            _safe_close_descriptor(read_descriptor),
            "capability reader close",
        )
        try:
            captured_stdout = bytes(stdout_buffer)
            captured_stderr = bytes(stderr_buffer)
        except BaseException as exc:
            cleanup_error = _add_cleanup_error(cleanup_error, exc, "diagnostic buffer copy")
        try:
            _restore_descriptor_three(saved_descriptor, saved_inheritable)
            if _descriptor_snapshot(3) != original_snapshot:
                raise RuntimeError("descriptor three was not restored")
        except BaseException as exc:
            restoration_error = exc
        if cleanup_error is not None and restoration_error is not None:
            try:
                restoration_error.add_note("child cleanup error: " + repr(cleanup_error))
            except BaseException:
                pass
    if restoration_error is not None:
        if pending_error is not None:
            restoration_error.add_note("child error before restoration: " + repr(pending_error))
        if unexpected_error is not None:
            restoration_error.add_note("unexpected child-launch error: " + repr(unexpected_error))
        raise restoration_error
    if pending_error is not None:
        if cleanup_error is not None:
            pending_error.add_note("child cleanup error: " + repr(cleanup_error))
        raise pending_error
    diagnostic = bounded_child_diagnostic(
        None if timed_out else (
            completed_returncode if type(completed_returncode) is int else 127
        ),
        captured_stdout,
        captured_stderr,
        timed_out,
    )
    if unexpected_error is not None:
        wrapped = ChildLaunchError("isolated child launch raised unexpectedly", diagnostic)
        if cleanup_error is not None:
            wrapped.add_note("child cleanup error: " + repr(cleanup_error))
        raise wrapped from unexpected_error
    if cleanup_error is not None:
        wrapped = ChildLaunchError("isolated child cleanup failed", diagnostic)
        raise wrapped from cleanup_error
    if timed_out:
        raise ChildLaunchError("isolated child timed out", diagnostic)
    if overflowed:
        raise ChildLaunchError("isolated child exceeded stream cap", diagnostic)
    if completed_returncode != 0:
        raise ChildLaunchError("isolated child returned nonzero", diagnostic)
    if captured_stderr:
        raise ChildLaunchError("isolated child wrote stderr", diagnostic)
    return captured_stdout, diagnostic


def _is_sha256(value):
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _safe_token(project_root: Path, track: str):
    if track not in {"Q", "R"}:
        raise ValueError("track identity")
    runner_relative = Q_RUNNER_RELATIVE if track == "Q" else R_RUNNER_RELATIVE
    runner_bytes = read_regular_bytes(project_root / runner_relative)
    definitions_bytes = read_regular_bytes(project_root / DEFINITIONS_RELATIVE)
    runner_sha256 = sha256_bytes(runner_bytes)
    definitions_sha256 = sha256_bytes(definitions_bytes)
    nonce = sha256_bytes(
        ("P13_SAFE_RUNTIME_PROBE_" + track + runner_sha256 + definitions_sha256).encode("ascii")
    )[:32]
    token = {
        "candidate_id": CANDIDATE_ID,
        "claim_sha256": None,
        "definitions_sha256": definitions_sha256,
        "engine_sha256": None,
        "fixture_sha256": None,
        "nonce": nonce,
        "purpose": "SAFE_RUNTIME_PROBE",
        "runner_sha256": runner_sha256,
        "schema": "P13_TRACK_CAPABILITY_V1",
        "track": track,
    }
    return canonical_bytes(token), token


def _validate_safe_response(project_root: Path, response, token):
    required = {
        "access_counters",
        "access_log",
        "candidate_id",
        "capability_sha256",
        "definitions_sha256",
        "purpose",
        "runner_sha256",
        "schema",
        "track",
    }
    if type(response) is not dict or set(response) != required:
        raise ValueError("safe response keys")
    if response["schema"] != "P13_SAFE_RUNTIME_PROBE_V1":
        raise ValueError("safe response schema")
    if response["candidate_id"] != CANDIDATE_ID or response["track"] != token["track"]:
        raise ValueError("safe response identity")
    if response["purpose"] != "SAFE_RUNTIME_PROBE":
        raise ValueError("safe response purpose")
    if response["definitions_sha256"] != token["definitions_sha256"]:
        raise ValueError("safe response definitions hash")
    if response["runner_sha256"] != token["runner_sha256"]:
        raise ValueError("safe response runner hash")
    if not _is_sha256(response["capability_sha256"]):
        raise ValueError("safe response capability hash")
    counters = response["access_counters"]
    required_counters = {
        "denied_cross_track_read_count",
        "denied_dynamic_loader_count",
        "denied_ledger_read_count",
        "denied_network_count",
        "denied_outside_read_count",
        "denied_outside_write_count",
        "denied_process_count",
        "denied_review_read_count",
        "denied_source_read_count",
        "run_science_call_count",
        "successful_outside_read_count",
        "successful_outside_write_count",
    }
    if type(counters) is not dict or set(counters) != required_counters:
        raise ValueError("safe response counter keys")
    if any(type(value) is not int or value < 0 for value in counters.values()):
        raise TypeError("safe response counters")
    if counters != SAFE_PROBE_EXPECTED_COUNTS:
        raise RuntimeError("safe probe counter inventory drift")
    access_log = response["access_log"]
    if type(access_log) is not dict or set(access_log) != {
        "allowed_read_counts",
        "purpose",
        "schema",
        "track",
    }:
        raise ValueError("safe access-log keys")
    if access_log["schema"] != "P13_TRACK_ACCESS_LOG_V1" or access_log["track"] != token["track"]:
        raise ValueError("safe access-log identity")
    if access_log["purpose"] != "SAFE_RUNTIME_PROBE":
        raise ValueError("safe access-log purpose")
    runner_relative = Q_RUNNER_RELATIVE if token["track"] == "Q" else R_RUNNER_RELATIVE
    expected_paths = {
        DEFINITIONS_RELATIVE.as_posix(): 1,
        runner_relative.as_posix(): 0,
    }
    if access_log["allowed_read_counts"] != expected_paths:
        raise ValueError("safe allowed-read log")


def launch_safe_probe(project_root: Path, track: str, timeout_seconds=30):
    token_bytes, token = _safe_token(project_root, track)
    runner_relative = Q_RUNNER_RELATIVE if track == "Q" else R_RUNNER_RELATIVE
    runner_path = project_root / runner_relative
    stdout, diagnostic = _run_child(
        runner_path,
        token_bytes,
        runner_path.parent,
        timeout_seconds,
    )
    try:
        response = strict_canonical_load(stdout)
        if response.get("capability_sha256") != sha256_bytes(token_bytes):
            raise ValueError("safe capability response binding")
        _validate_safe_response(project_root, response, token)
    except BaseException as exc:
        error = ChildLaunchError("isolated child protocol invalid", diagnostic)
        raise error from exc
    return {"diagnostic": diagnostic, "response": response}


def _registered_nonce(
    track,
    claim_sha256,
    runner_sha256,
    engine_sha256,
    fixture_sha256,
    definitions_sha256,
):
    if track not in {"Q", "R"} or any(
        not _is_sha256(value)
        for value in (
            claim_sha256,
            runner_sha256,
            engine_sha256,
            fixture_sha256,
            definitions_sha256,
        )
    ):
        raise ValueError("registered nonce inputs")
    material = "\0".join(
        (
            "P13_REGISTERED_CAPABILITY_NONCE_V1",
            track,
            claim_sha256,
            runner_sha256,
            engine_sha256,
            fixture_sha256,
            definitions_sha256,
        )
    ).encode("ascii")
    return sha256_bytes(material)[:32]


def _registered_token(project_root: Path, track: str, claim_receipt: dict):
    if track not in {"Q", "R"}:
        raise ValueError("registered track identity")
    if type(claim_receipt) is not dict or set(claim_receipt) != {
        "claim",
        "claim_bytes",
        "claim_sha256",
        "official",
    }:
        raise ValueError("registered claim receipt shape")
    claim = claim_receipt["claim"]
    if (
        canonical_bytes(claim) != claim_receipt["claim_bytes"]
        or sha256_bytes(claim_receipt["claim_bytes"]) != claim_receipt["claim_sha256"]
    ):
        raise ValueError("registered claim receipt integrity")
    relatives = {
        "Q": (Q_RUNNER_RELATIVE, Q_ENGINE_RELATIVE, Q_FIXTURE_RELATIVE),
        "R": (R_RUNNER_RELATIVE, R_ENGINE_RELATIVE, R_FIXTURE_RELATIVE),
    }
    runner_relative, engine_relative, fixture_relative = relatives[track]
    observed = {
        "definitions_sha256": sha256_bytes(read_regular_bytes(project_root / DEFINITIONS_RELATIVE)),
        "engine_sha256": sha256_bytes(read_regular_bytes(project_root / engine_relative)),
        "fixture_sha256": sha256_bytes(read_regular_bytes(project_root / fixture_relative)),
        "runner_sha256": sha256_bytes(read_regular_bytes(project_root / runner_relative)),
    }
    expected = dict(claim["track_bindings"][track])
    expected["definitions_sha256"] = claim["definitions_sha256"]
    if canonical_bytes(observed) != canonical_bytes(expected):
        raise RuntimeError(track + " registered live input binding drift")
    nonce = _registered_nonce(
        track,
        claim_receipt["claim_sha256"],
        observed["runner_sha256"],
        observed["engine_sha256"],
        observed["fixture_sha256"],
        observed["definitions_sha256"],
    )
    token = {
        "candidate_id": CANDIDATE_ID,
        "claim_sha256": claim_receipt["claim_sha256"],
        "definitions_sha256": observed["definitions_sha256"],
        "engine_sha256": observed["engine_sha256"],
        "fixture_sha256": observed["fixture_sha256"],
        "nonce": nonce,
        "purpose": "REGISTERED_R100",
        "runner_sha256": observed["runner_sha256"],
        "schema": "P13_TRACK_CAPABILITY_V1",
        "track": track,
    }
    return canonical_bytes(token), token


def launch_registered_track(project_root: Path, track: str, claim_receipt: dict, timeout_seconds=30):
    """Launch one registered track.  This is never called by safe preflight."""
    token_bytes, token = _registered_token(project_root, track, claim_receipt)
    runner_relative = Q_RUNNER_RELATIVE if track == "Q" else R_RUNNER_RELATIVE
    runner_path = project_root / runner_relative
    stdout, diagnostic = _run_child(
        runner_path,
        token_bytes,
        runner_path.parent,
        timeout_seconds,
    )
    try:
        response = strict_canonical_load(stdout)
        from .lifecycle import _validate_registered_capability, _validate_registered_envelope

        _validate_registered_capability(token, track, claim_receipt["claim"], response)
        _validate_registered_envelope(response, track, claim_receipt["claim"], token_bytes)
    except BaseException as exc:
        error = ChildLaunchError("registered isolated child protocol invalid", diagnostic)
        raise error from exc
    return {
        "capability_bytes": token_bytes,
        "diagnostic": diagnostic,
        "envelope_bytes": stdout,
    }
