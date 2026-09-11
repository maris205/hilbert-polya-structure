#!/usr/bin/env python3
"""Outer full-stream receipt for one new P209 author recorder invocation.

This wrapper does not import the recorder or any scientific implementation.
The recorder is separately pinned before this wrapper starts its process;
the recorder inventories every known producer/build input before children.
No claim of tracing this wrapper's own OS startup is made.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback

PAPER = Path(__file__).resolve().parent
ROOT = PAPER.parents[3]
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}


def pin(path):
    path = Path(path)
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return {"sha256": h.hexdigest(), "bytes": path.stat().st_size,
            "resolved": str(path.resolve())}


def save(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def check_closed_recorder(base, mode, exit_code):
    manifest = base / "SHA256SUMS"
    seen = set()
    for line in manifest.read_text().splitlines():
        digest, name = line.split("  ", 1)
        relative = Path(name)
        if not (len(digest) == 64 and set(digest) <= set("0123456789abcdef") and
                not relative.is_absolute() and ".." not in relative.parts and
                name != "SHA256SUMS" and name not in seen):
            raise RuntimeError("Unsafe, self or duplicate recorder manifest entry")
        if (base / name).is_symlink() or pin(base / name)["sha256"] != digest:
            raise RuntimeError("Recorder manifest payload mismatch: " + name)
        seen.add(name)
    if seen != {p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file() and p != manifest}:
        raise RuntimeError("Recorder manifest is not complete")
    receipt = json.loads((base / "RECEIPT.json").read_bytes())
    if receipt["mode"] != mode or (exit_code == 0 and receipt["status"] != "PASS_REVIEW_B_" + mode.upper()):
        raise RuntimeError("Recorder receipt disagrees with actual normal exit")
    if exit_code != 0 and receipt["status"] != "FAIL_PRESERVED":
        raise RuntimeError("Nonzero recorder exit lacks a closed failure receipt")
    return {"manifest": pin(manifest), "payloads": len(seen), "status": receipt["status"]}


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in {"pair", "build"}:
        raise RuntimeError("launch_review.py pair|build review_pair_N|review_build_N")
    mode, label = sys.argv[1:]
    prefix = "review_" + mode + "_"
    if not label.startswith(prefix) or not label[len(prefix):].isdigit():
        raise RuntimeError("Invalid direct-child output label")
    out, recorder_out = PAPER / ("launcher_" + label), PAPER / label
    if out.exists() or out.is_symlink() or recorder_out.exists() or recorder_out.is_symlink():
        raise RuntimeError("Refuse existing launcher or recorder output")
    if dict(os.environ) != ENV or Path.cwd() != ROOT or not (
        sys.flags.isolated == 1 and sys.flags.no_site == 1 and
        sys.flags.optimize == 0 and sys.dont_write_bytecode and
        Path(sys.executable).resolve() == Path("/usr/bin/python3.10") and
        sys.pycache_prefix == str(out / "never_created_launcher_cache") and
        not Path(sys.pycache_prefix).exists()
    ):
        raise RuntimeError("Launcher settings differ from declared isolated minimal environment")
    out.mkdir(mode=0o700)
    for name in ("launch_review.py", "record_review.py", "bootstrap.py", "verify.py"):
        shutil.copyfile(PAPER / name, out / name)
    inputs = [PAPER / name for name in ("launch_review.py", "record_review.py", "bootstrap.py", "verify.py", "PARAMETERS.json")]
    inputs += [Path("/usr/bin/python3.10"), Path("/usr/bin/env")]
    before = {str(p): pin(p) for p in inputs}
    save(out / "INPUTS_BEFORE.json", before)
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X",
            "pycache_prefix=" + str(recorder_out / "never_created_parent_cache"),
            str(PAPER / "record_review.py"), mode, label]
    row = {"argv": argv, "cwd": str(ROOT), "env": ENV,
           "started_epoch": time.time(), "exit": None, "outcome": "NOT_STARTED",
           "launcher_orig_argv": sys.orig_argv, "launcher_flags": str(sys.flags),
           "launcher_cache": sys.pycache_prefix, "stdout": "recorder.stdout", "stderr": "recorder.stderr"}
    save(out / "PRE_SPAWN_ATTEMPT.json", row)
    failure = None
    proc = None
    try:
        with (out / "recorder.stdout").open("xb") as stdout, (out / "recorder.stderr").open("xb") as stderr:
            proc = subprocess.Popen(argv, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr)
            row["pid"] = proc.pid
            exit_code = proc.wait()
        row.update(exit=exit_code, outcome="COMPLETED")
    except BaseException:
        failure = traceback.format_exc()
        row["outcome"] = "NO_COMPLETED_RESULT"
    closed = None
    if failure is None and row["outcome"] == "COMPLETED":
        try:
            closed = check_closed_recorder(recorder_out, mode, row["exit"])
        except BaseException:
            failure = traceback.format_exc()
    if closed is None:
        # No inferred process-tree termination and no final hashes of streams
        # that an interrupted recorder or its command group may still modify.
        row.update(status="UNCLOSED_NO_SEAL", failure=failure,
                   finished_epoch=time.time(),
                   scope="Only attempt, PID when known, raw streams and exception facts are retained. No settled-stream hashes, final seal or PASS.")
        save(out / "UNCLOSED.json", row)
        print(json.dumps({"status": "UNCLOSED_NO_SEAL", "output": str(out), "exit": row["exit"]}, sort_keys=True))
        return 1
    after = {str(p): pin(p) for p in inputs}
    save(out / "INPUTS_AFTER.json", after)
    row.update(finished_epoch=time.time(), failure=failure, inputs_unchanged=before == after,
               cache_absent=not Path(sys.pycache_prefix).exists())
    for name in ("recorder.stdout", "recorder.stderr"):
        if (out / name).is_file():
            row[name + "_pin"] = pin(out / name)
    row["recorder_closure"] = closed
    row["recorder_seal"] = closed["manifest"]
    okay = failure is None and row["exit"] == 0 and before == after and row["cache_absent"]
    row["status"] = "PASS_LAUNCH" if okay else "FAIL_PRESERVED"
    save(out / "RECEIPT.json", row)
    paths = sorted(p for p in out.rglob("*") if p.is_file())
    with (out / "SHA256SUMS").open("x") as stream:
        for p in paths:
            stream.write(pin(p)["sha256"] + "  " + p.relative_to(out).as_posix() + "\n")
    print(json.dumps({"status": row["status"], "exit": row["exit"], "output": str(out),
                      "launcher_seal": pin(out / "SHA256SUMS"),
                      "recorder_seal": row.get("recorder_seal")}, sort_keys=True))
    return 0 if okay else 1


if __name__ == "__main__":
    raise SystemExit(main())
