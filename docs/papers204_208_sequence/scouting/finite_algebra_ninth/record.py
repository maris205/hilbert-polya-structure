#!/usr/bin/env python3
"""Exclusive-output execution recorder, not a mathematical verifier."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def utc():
    return datetime.now(timezone.utc).isoformat()


def put(path, data):
    with path.open("xb") as out:
        out.write(data)


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    out = HERE / "execution_01"
    out.mkdir(exist_ok=False)
    sources = [HERE / "INTAKE.md", HERE / "pilot.py", HERE / "record.py"]
    pins = "".join(f"{sha(p)}  {p.relative_to(ROOT)}\n" for p in sources).encode()
    put(out / "INPUTS_BEFORE.sha256", pins)
    for p in sources:
        put(out / p.name, p.read_bytes())
    environment = dict(os.environ)
    environment.update(PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1", LC_ALL="C", TZ="UTC")
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    receipts = []
    for i in range(3):
        command = [sys.executable, "-B", str(out / "pilot.py")]
        start = utc()
        clock = time.monotonic()
        result = subprocess.run(command, cwd=out, env=environment, capture_output=True)
        receipt = {"command": command, "cwd": str(out), "start_utc": start,
                   "end_utc": utc(), "elapsed_seconds": time.monotonic()-clock,
                   "returncode": result.returncode,
                   "stdout_sha256": sha256(result.stdout).hexdigest(),
                   "stderr_sha256": sha256(result.stderr).hexdigest()}
        put(out / f"run{i}.stdout", result.stdout)
        put(out / f"run{i}.stderr", result.stderr)
        put(out / f"run{i}.receipt.json", (json.dumps(receipt, sort_keys=True, indent=2)+"\n").encode())
        receipts.append(receipt)
        if result.returncode:
            print(json.dumps(receipt, sort_keys=True))
            return result.returncode
        if i == 0:
            put(HERE / "CANONICAL.json", result.stdout)
    for i in range(3):
        command = ["cmp", str(out / f"run{i}.stdout"), str(HERE / "CANONICAL.json")]
        result = subprocess.run(command, capture_output=True)
        put(out / f"cmp{i}.stdout", result.stdout)
        put(out / f"cmp{i}.stderr", result.stderr)
        receipt = {"command": command, "returncode": result.returncode, "utc": utc()}
        put(out / f"cmp{i}.receipt.json", (json.dumps(receipt, sort_keys=True, indent=2)+"\n").encode())
        if result.returncode:
            raise SystemExit(result.returncode)
    after = "".join(f"{sha(p)}  {p.relative_to(ROOT)}\n" for p in sources).encode()
    put(out / "INPUTS_AFTER.sha256", after)
    if after != pins:
        raise RuntimeError("source mutation during run triple")
    put(out / "SUMMARY.json", (json.dumps({"runs": receipts, "raw_comparisons": 3,
        "inputs_unchanged": True, "canonical_sha256": sha(HERE/"CANONICAL.json")},
        sort_keys=True, indent=2)+"\n").encode())
    manifest = "".join(f"{sha(p)}  {p.relative_to(out)}\n" for p in sorted(out.rglob("*")) if p.is_file())
    put(out / "SHA256SUMS", manifest.encode())
    print(json.dumps({"status": "PASS", "canonical_sha256": sha(HERE/"CANONICAL.json"),
                      "runs": 3, "raw_comparisons": 3}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
