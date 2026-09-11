"""Physical pre-execution lock and native runtime probe; no KIP execution."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
DESK = BASE.with_name("finite_semigroup_lane")
EXE = Path("/usr/bin/python3.10")
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C", "LC_ALL": "C", "TZ": "UTC"}


def digest(path):
    raw = Path(path).read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")


def assert_desk():
    manifest = json.loads((DESK / "MANIFEST.json").read_text())
    actual = {str(path.relative_to(DESK)) for path in DESK.rglob("*")
              if path.is_file() and path != DESK / "MANIFEST.json"}
    if actual != {row["path"] for row in manifest["files"]}:
        raise AssertionError("sealed desk inventory changed")
    for row in manifest["files"]:
        if digest(DESK / row["path"]) != {key: row[key] for key in ("bytes", "sha256")}:
            raise AssertionError(("sealed desk bytes changed", row["path"]))
    return manifest


def main():
    capacity = os.statvfs(BASE)
    available = capacity.f_bavail * capacity.f_frsize
    if available < 64 * 1024 * 1024:
        raise RuntimeError("less than the 64 MiB conservative lock/output allowance")
    manifest = assert_desk()
    lock = BASE / "lock"
    lock.mkdir(exist_ok=False)
    preflight = BASE / "preflight"
    preflight.mkdir(exist_ok=False)
    rows = []

    def copy_pin(origin, frozen, role):
        original = Path(origin).resolve()
        raw = original.read_bytes()
        frozen.parent.mkdir(parents=True, exist_ok=True)
        frozen.write_bytes(raw)
        if original.read_bytes() != frozen.read_bytes():
            raise AssertionError(("copy changed", str(original)))
        rows.append({"origin": str(original), "frozen": str(frozen.relative_to(BASE)),
                     "role": role, **digest(frozen)})

    for row in manifest["files"]:
        copy_pin(DESK / row["path"], lock / "desk" / row["path"], "sealed_desk_payload")
    copy_pin(DESK / "MANIFEST.json", lock / "desk" / "MANIFEST.json", "sealed_desk_manifest")
    for name in ("producer.py", "run_pilot.py", "runtime_probe.py", "freeze.py", "audit.py"):
        compile((BASE / name).read_bytes(), str(BASE / name), "exec")
        copy_pin(BASE / name, lock / name, "actual_execution_or_artifact_source")
    copy_pin(BASE / "AUTHORIZATION.md", lock / "AUTHORIZATION.md", "execution_authority")

    argv = [str(EXE), "-I", "-S", "-B", str(lock / "runtime_probe.py")]
    started = time.time_ns()
    result = subprocess.run(argv, cwd=BASE, env=ENV, capture_output=True,
                            timeout=30, check=False)
    (preflight / "runtime_probe.stdout.json").write_bytes(result.stdout)
    (preflight / "runtime_probe.stderr.txt").write_bytes(result.stderr)
    dump(preflight / "NATIVE_RECEIPT.json", {
        "kind": "readonly_runtime_discovery_not_science", "argv": argv,
        "cwd": str(BASE), "environment": ENV, "started_ns": started,
        "finished_ns": time.time_ns(), "native_exit": result.returncode,
        "stdout": digest(preflight / "runtime_probe.stdout.json"),
        "stderr": digest(preflight / "runtime_probe.stderr.txt"),
    })
    if result.returncode != 0:
        raise AssertionError("runtime preflight failed; evidence retained; no science run")
    profile = json.loads(result.stdout)
    for index, record in enumerate(profile["file_pins"], 1):
        original = Path(record["path"])
        expected = {key: record[key] for key in ("bytes", "sha256")}
        if digest(original) != expected:
            raise AssertionError(("runtime changed after probe", str(original)))
        destination = lock / "runtime" / f"{index:03d}_{original.name}"
        copy_pin(original, destination, "preflight_observed_runtime_input")
    for row in rows:
        expected = {key: row[key] for key in ("bytes", "sha256")}
        if digest(row["origin"]) != expected or digest(BASE / row["frozen"]) != expected:
            raise AssertionError(("prelock input changed", row["origin"]))
    assert_desk()
    dump(BASE / "PRE_EXECUTION_PINS.json", {
        "schema": "kip_single_pilot_lock_v1", "frozen_ns": time.time_ns(),
        "producer_invocations_so_far": 0, "available_bytes_at_start": available,
        "executable": str(EXE), "environment": ENV, "timeout_seconds": 60,
        "desk_manifest": digest(DESK / "MANIFEST.json"), "rows": rows,
        "runtime_limit": "observed stdlib/interpreter/mapped files, not a complete configuration or hermetic reuse key",
    })
    print(json.dumps({"physical_lock_rows": len(rows),
                      "runtime_input_files": len(profile["file_pins"]),
                      "desk_payloads": len(manifest["files"]),
                      "all_original_copy_pairs_equal": True,
                      "science_invocations": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
