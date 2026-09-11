"""Launch exactly the approved frozen producer once and retain native output."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

LOCK = Path(__file__).resolve().parent
if LOCK.name != "lock":
    raise RuntimeError("execute only the physically frozen lock/run_pilot.py")
BASE = LOCK.parent
OUT = BASE / "execution_01"


def digest(path):
    raw = Path(path).read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def dump(path, obj):
    path.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")


def current_inputs(rows):
    result = []
    for row in rows:
        result.append({"origin": row["origin"], "frozen": row["frozen"],
                       "origin_pin": digest(row["origin"]),
                       "frozen_pin": digest(BASE / row["frozen"])})
    return result


def runtime_files():
    files = {str(Path(sys.executable).resolve()), str(Path(__file__).resolve())}
    modules = []
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, "__file__", None)
        if path and Path(path).is_file():
            path = str(Path(path).resolve())
            files.add(path)
            modules.append({"module": name, "path": path})
    mapped = set()
    with open("/proc/self/maps", encoding="utf-8") as stream:
        for line in stream:
            parts = line.rstrip("\n").split(None, 5)
            if len(parts) == 6 and parts[5].startswith("/") and Path(parts[5]).is_file():
                mapped.add(str(Path(parts[5]).resolve()))
    files.update(mapped)
    return {"modules": modules, "mapped_runtime_paths": sorted(mapped),
            "file_pins": [{"path": path, **digest(path)} for path in sorted(files)]}


def main():
    pins_path = BASE / "PRE_EXECUTION_PINS.json"
    pins_digest = digest(pins_path)
    lock = json.loads(pins_path.read_text())
    rows = lock["rows"]
    before = current_inputs(rows)
    for original, record in zip(rows, before):
        expected = {key: original[key] for key in ("bytes", "sha256")}
        if record["origin_pin"] != expected or record["frozen_pin"] != expected:
            raise AssertionError(("pre-execution input differs from physical lock", original["origin"]))
    OUT.mkdir(exist_ok=False)
    argv = [lock["executable"], "-I", "-S", "-B", str(LOCK / "producer.py")]
    environment = lock["environment"]
    started = time.time_ns()
    timed_out = False
    launch_error = None
    stdout = b""
    stderr = b""
    native_exit = None
    pid = None
    try:
        child = subprocess.Popen(argv, cwd=BASE, env=environment,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pid = child.pid
        try:
            stdout, stderr = child.communicate(timeout=lock["timeout_seconds"])
        except subprocess.TimeoutExpired:
            timed_out = True
            child.kill()
            stdout, stderr = child.communicate()
        native_exit = child.returncode
    except OSError as error:
        launch_error = {"type": type(error).__name__, "message": str(error)}
    finished = time.time_ns()
    (OUT / "stdout.jsonl").write_bytes(stdout)
    (OUT / "stderr.txt").write_bytes(stderr)
    after = current_inputs(rows)
    launcher_runtime = runtime_files()
    receipt = {
        "kind": "ONE_EXPLORATORY_NATIVE_AUTHOR_PILOT_NOT_HERMETIC_REPLAY",
        "scientific_producer_invocations": 1 if pid is not None else 0,
        "argv": argv, "cwd": str(BASE), "environment": environment,
        "launcher_argv": sys.argv, "launcher_source": {"path": str(Path(__file__).resolve()),
                                                       **digest(Path(__file__))},
        "launcher_python_version": sys.version,
        "started_ns": started, "finished_ns": finished,
        "elapsed_seconds": (finished - started) / 1000000000,
        "timeout_seconds": lock["timeout_seconds"], "timed_out": timed_out,
        "pid": pid, "native_exit": native_exit, "launch_error": launch_error,
        "pre_execution_pins_before": pins_digest,
        "pre_execution_pins_after": digest(pins_path),
        "input_pins_before": before, "input_pins_after": after,
        "all_locked_inputs_unchanged": before == after,
        "launcher_runtime": launcher_runtime,
        "stdout": digest(OUT / "stdout.jsonl"), "stderr": digest(OUT / "stderr.txt"),
        "scope_limit": "One author exploratory run; actual observed dependencies are not a strict complete hermetic replay key.",
    }
    dump(OUT / "NATIVE_RECEIPT.json", receipt)
    success = (native_exit == 0 and not timed_out and launch_error is None
               and before == after and digest(pins_path) == pins_digest)
    print(json.dumps({"native_exit": native_exit, "timed_out": timed_out,
                      "elapsed_seconds": receipt["elapsed_seconds"],
                      "stdout_bytes": len(stdout), "stderr_bytes": len(stderr),
                      "all_locked_inputs_unchanged": before == after,
                      "success": success}, sort_keys=True))
    if not success:
        raise RuntimeError("one approved pilot failed; evidence retained; no automatic retry")
    for line in stdout.splitlines():
        record = json.loads(line)
        if record["kind"] in ("box", "complete"):
            print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
