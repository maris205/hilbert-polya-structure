#!/usr/bin/env python3
"""Root-only outer full-stream receipt for the P209 terminal build pair.

Direct disclosed adaptation of B's original launcher, not a manuscript
review. It never imports the builder or old code. The builder requires real
accepted A/B deltas and root-verified physical Round2 before qa_final exists.
Bounded early/late launcher observations do not trace OS startup or children.
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
PREPARATION = ROOT / "docs/papers204_208_sequence/qa/p209_terminal_preparation"
BATCH = ROOT / "docs/papers204_208_sequence"
PAPER = ROOT / "papers/209-ordered-fibre-threading"
RECORDER = PREPARATION / "root_terminal_builds.py"
OUTPUT_ROOT = BATCH / "qa/root_replays/p209_terminal_strict"
SOURCE_PINS = PREPARATION / "SOURCE_PINS.json"
EXPECTED_SOURCE_PINS = "bb707e351669318169eb558dc9097ef700bb44c01418253e3944aaa8dd4cd8f2"
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC",
       "SOURCE_DATE_EPOCH": "1788652800", "FORCE_SOURCE_DATE": "1", "openin_any": "p", "openout_any": "p"}


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


def runtime(phase):
    modules = {}
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, "__file__", None)
        if path and Path(path).is_file():
            resolved = Path(path).resolve()
            if resolved.suffix in {".pyc", ".pyo"}:
                raise RuntimeError("Launcher consumed bytecode")
            modules[name] = {"path": str(resolved), **pin(resolved)}
    maps = Path("/proc/self/maps").read_text()
    mapped = {}
    for line in maps.splitlines():
        parts = line.split(None, 5)
        if len(parts) == 6 and parts[5].startswith("/"):
            path = Path(parts[5]).resolve()
            mapped[str(path)] = pin(path)
    return {"phase": phase, "modules": modules, "maps": maps, "mapped_files": mapped,
            "orig_argv": sys.orig_argv, "flags": str(sys.flags), "cwd": str(Path.cwd()),
            "environment": dict(os.environ), "executable": sys.executable, "sys_path": sys.path,
            "cache_prefix": sys.pycache_prefix, "cache_exists": Path(sys.pycache_prefix).exists(),
            "scope": "Early/late launcher only; no continuous startup or child-process trace."}


def check_closed_recorder(base, exit_code):
    if base.resolve() != base or base.is_symlink():
        raise RuntimeError("Aliased terminal output")
    manifest = base / "SHA256SUMS"
    seen = set()
    for line in manifest.read_text().splitlines():
        digest, name = line.split("  ", 1)
        relative = Path(name)
        if not (len(digest) == 64 and set(digest) <= set("0123456789abcdef") and
                relative.as_posix() == name and not relative.is_absolute() and ".." not in relative.parts and
                name != "SHA256SUMS" and name not in seen):
            raise RuntimeError("Unsafe, self or duplicate recorder manifest entry")
        if (base / name).resolve() != base / name or (base / name).is_symlink() or pin(base / name)["sha256"] != digest:
            raise RuntimeError("Recorder manifest payload mismatch: " + name)
        seen.add(name)
    entries = list(base.rglob("*"))
    if any(p.is_symlink() for p in entries) or seen != {p.relative_to(base).as_posix() for p in entries if p.is_file() and p != manifest}:
        raise RuntimeError("Recorder manifest is not complete and physical")
    receipt = json.loads((base / "BUILD_EXECUTION.json").read_bytes())
    if exit_code == 0 and not (receipt["status"] == "PASS_P209_TERMINAL_BUILD_PAIR_NOT_VIEWED" and
            receipt["failures"] == [] and len(receipt["builds"]) == 2 and receipt["command_census_complete"] and
            receipt["visual_review"] == "PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER"):
        raise RuntimeError("Recorder receipt disagrees with actual normal exit")
    if exit_code != 0 and receipt["status"] != "FAIL_PRESERVED":
        raise RuntimeError("Nonzero recorder exit lacks a closed failure receipt")
    return {"manifest": pin(manifest), "payloads": len(seen), "status": receipt["status"]}


def main():
    if sys.argv[1:] != ["terminal-pair-after-round2"] or SCRIPT != PREPARATION / "root_launch_terminal.py":
        raise RuntimeError("Require exact prepared root launcher and terminal-pair-after-round2 argument")
    if OUTPUT_ROOT.resolve() != OUTPUT_ROOT:
        raise RuntimeError("Terminal launcher output root aliases another directory")
    out, recorder_out = OUTPUT_ROOT / "launcher_terminal_pair_01", PAPER / "qa_final"
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
    if pin(SOURCE_PINS)["sha256"] != EXPECTED_SOURCE_PINS:
        raise RuntimeError("SOURCE_PIN_CONTRACT_CHANGED")
    source_pins = json.loads(SOURCE_PINS.read_bytes())
    if len(source_pins) != 8:
        raise RuntimeError("SOURCE_PIN_COUNT_CHANGED")
    inputs = [p for p in PREPARATION.rglob("*") if p.is_file()]
    inputs += [Path("/usr/bin/python3.10"), Path("/usr/bin/env")]
    for stem in ("P209_A_ROOT_DELTA_INSPECTION", "P209_B_ROOT_DELTA_INSPECTION", "P209_ROUND2_ROOT_INSPECTION"):
        inputs.extend([BATCH / ("qa/" + stem + ".actual.json"), BATCH / ("qa/" + stem + ".md")])
    for base in (PAPER, PAPER / "frozen_round1", PAPER / "frozen_round2"):
        inputs.extend(base / name for name in source_pins)
        inputs.append(base / "main.pdf")
    inputs.extend([PAPER / "frozen_round1/SHA256SUMS", PAPER / "frozen_round2/SHA256SUMS"])
    early = runtime("BEFORE_RECORDER_AND_SOURCE_COPY")
    observed = set(early["mapped_files"]) | {v["path"] for v in early["modules"].values()}
    inputs.extend(map(Path, observed))
    before = {str(p): pin(p) for p in inputs}
    if not all(all(before[str(PAPER / n)][key] == v[key] for key in ("sha256", "bytes"))
               for n, v in source_pins.items()):
        raise RuntimeError("UNCHANGED_LIVE_SOURCE_CONTRACT_FAILED")
    OUTPUT_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    out.mkdir(mode=0o700)
    save(out / "INPUTS_BEFORE.json", before)
    save(out / "LAUNCHER_RUNTIME_BEFORE.json", early)
    for source in (SCRIPT, RECORDER):
        shutil.copyfile(source, out / source.name)
        copied = pin(out / source.name)
        if any(copied[key] != before[str(source)][key] for key in ("sha256", "bytes")):
            raise RuntimeError("Pre-pinned terminal source copy changed")
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X",
            "pycache_prefix=" + str(recorder_out / "never_created_parent_cache"),
            str(RECORDER), "terminal-pair-after-round2"]
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
            closed = check_closed_recorder(recorder_out, row["exit"])
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
    late = runtime("AFTER_RECORDER_AND_INPUT_CLOSURE")
    save(out / "LAUNCHER_RUNTIME_AFTER.json", late)
    late_inputs = {**late["mapped_files"], **{v["path"]: {k: v[k] for k in ("sha256", "bytes", "resolved")}
                   for v in late["modules"].values()}}
    known = {v["resolved"]: v for v in before.values()}
    launcher_closure = all(path in known and known[path] == value for path, value in late_inputs.items())
    row["launcher_observed_input_closure"] = launcher_closure
    okay = failure is None and row["exit"] == 0 and before == after and row["cache_absent"] and launcher_closure
    row["status"] = "PASS_ROOT_TERMINAL_LAUNCH_NOT_VIEWED" if okay else "FAIL_PRESERVED"
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
