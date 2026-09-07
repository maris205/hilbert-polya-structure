#!/usr/bin/env python3
"""Outer full-stream receipt for the new root P209 manuscript-B replay pair.

Disclosed path/role/canonical adaptation of the physically saved B launcher.
No recorder or scientific implementation is imported. Existing B canonical
bytes are mandatory and read-only. All preparation-fixed original inputs
are checked before copying or recorder launch; root pins this wrapper.
The original bounded observation and UNCLOSED_NO_SEAL policy is retained.
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

SCRIPT = Path(__file__).resolve()
ROOT = Path("/root/autodl-tmp/symbolic_dynamics")
PAPER = ROOT / "docs/papers204_208_sequence/reviews/p209_b"
OUTPUT_ROOT = ROOT / "docs/papers204_208_sequence/qa/root_replays/p209_b_strict"
RECORDER = SCRIPT.with_name("root_record_pair.py")
FIXED_INPUTS = SCRIPT.with_name("FIXED_INPUTS.json")
EXPECTED_FIXED_INPUTS = "09a5033597e9b218296f624c256fe2d370331e08269bf1fcc2928352104fb7c8"
EXPECTED_B_INPUTS = {
    "record_review.py": "01623b42719e6159ae31c0e422079929766de61e4f07459c6d579b7f952fa272",
    "launch_review.py": "f190bf2e91b130428a97025bfd708f9a652e80f31ca41706dd81d0259c15693d",
    "bootstrap.py": "dc2f0ef968f2b451ceaf390ac7a8189005881246624a0f94ab64879efa18a80b",
    "verify.py": "d5fd105ddfc162323f06cd530fbd696b0093643a7a0c24c64747cd9c9be30467",
    "PARAMETERS.json": "3b292d4c771041cd07f82c5da2bf534bfa77e67fc971e78df3d08910e937b8e4",
    "INPUT_PINS.sha256": "eee2b677a37c82bc3e99b209f0d310231f1bd0358752724ce7f9d0f3588f200f",
    "CANONICAL.json": "612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c",
    "SHA256SUMS": "d88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea",
}
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
    if receipt["mode"] != mode or (exit_code == 0 and receipt["status"] != "PASS_ROOT_REVIEW_B_" + mode.upper()):
        raise RuntimeError("Recorder receipt disagrees with actual normal exit")
    if exit_code != 0 and receipt["status"] != "FAIL_PRESERVED":
        raise RuntimeError("Nonzero recorder exit lacks a closed failure receipt")
    return {"manifest": pin(manifest), "payloads": len(seen), "status": receipt["status"]}


def main():
    if sys.argv[1:] != ["pair", "root_b_pair_01"]:
        raise RuntimeError("root_launch_pair.py pair root_b_pair_01")
    mode, label = sys.argv[1:]
    if OUTPUT_ROOT.resolve() != OUTPUT_ROOT:
        raise RuntimeError("Root output path aliases another directory")
    out, recorder_out = OUTPUT_ROOT / ("launcher_" + label), OUTPUT_ROOT / label
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
    if not (PAPER / "CANONICAL.json").is_file():
        raise RuntimeError("ROOT_CANONICAL_REQUIRED_NO_ADOPTION")
    if pin(FIXED_INPUTS)["sha256"] != EXPECTED_FIXED_INPUTS:
        raise RuntimeError("FIXED_INPUT_MANIFEST_CHANGED")
    fixed = json.loads(FIXED_INPUTS.read_bytes())
    if len(fixed) != 2021:
        raise RuntimeError("FIXED_ORIGINAL_SCOPE_CHANGED")
    inputs = [SCRIPT, RECORDER, FIXED_INPUTS] + list(map(Path, fixed))
    inputs += [Path("/usr/bin/python3.10"), Path("/usr/bin/env")]
    before = {str(p): pin(p) for p in inputs}
    if not all(all(before[p][key] == value[key] for key in ("sha256", "bytes", "resolved"))
               and value["symlink"] is None for p, value in fixed.items()):
        raise RuntimeError("EXACT_PREPARATION_FULL_INPUTS_CHANGED")
    if not all(before[str(PAPER / name)]["sha256"] == digest
               for name, digest in EXPECTED_B_INPUTS.items()):
        raise RuntimeError("EXACT_PREPARATION_B_INPUTS_CHANGED")
    OUTPUT_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    out.mkdir(mode=0o700)
    save(out / "INPUTS_BEFORE.json", before)
    for source in (SCRIPT, RECORDER, PAPER / "bootstrap.py", PAPER / "verify.py"):
        shutil.copyfile(source, out / source.name)
        copied = pin(out / source.name)
        if any(copied[key] != before[str(source)][key] for key in ("sha256", "bytes")):
            raise RuntimeError("Pre-pinned launcher source copy changed")
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X",
            "pycache_prefix=" + str(recorder_out / "never_created_parent_cache"),
            str(RECORDER), mode, label]
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
    row["status"] = "PASS_ROOT_LAUNCH" if okay else "FAIL_PRESERVED"
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
