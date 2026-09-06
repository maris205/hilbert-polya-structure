#!/usr/bin/env python3
"""Exclusive-output recorder for the declared static inverse follow-up."""
from datetime import datetime, timezone
from pathlib import Path
from hashlib import sha256
import json
import os
import subprocess
import sys
import time


here = Path(__file__).resolve().parent
root = here.parents[3]
out = here / "inverse_execution_01"
out.mkdir(exist_ok=False)
sources = [here / name for name in ("INTAKE.md", "CORRECTIONS_AND_FOLLOWUP.md",
                                    "qef_inverse.py", "record_inverse.py")]


def put(path, content):
    with path.open("xb") as file:
        file.write(content)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def pins():
    return "".join(f"{digest(path)}  {path.relative_to(root)}\n" for path in sources).encode()


before = pins()
put(out / "INPUTS_BEFORE.sha256", before)
for source in sources:
    put(out / source.name, source.read_bytes())
environment = dict(os.environ)
environment.update(PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1", LC_ALL="C", TZ="UTC")
environment.pop("PYTHONPATH", None)
environment.pop("PYTHONHOME", None)
receipts = []
for i in range(3):
    command = [sys.executable, "-B", str(out / "qef_inverse.py")]
    start = datetime.now(timezone.utc).isoformat()
    monotonic = time.monotonic()
    result = subprocess.run(command, cwd=out, env=environment, capture_output=True)
    put(out / f"run{i}.stdout", result.stdout)
    put(out / f"run{i}.stderr", result.stderr)
    receipt = {"command": command, "cwd": str(out), "returncode": result.returncode,
               "start_utc": start, "end_utc": datetime.now(timezone.utc).isoformat(),
               "elapsed_seconds": time.monotonic()-monotonic,
               "stdout_sha256": sha256(result.stdout).hexdigest(),
               "stderr_sha256": sha256(result.stderr).hexdigest()}
    put(out / f"run{i}.receipt.json", (json.dumps(receipt, sort_keys=True, indent=2)+"\n").encode())
    receipts.append(receipt)
    if result.returncode:
        raise SystemExit(result.returncode)
    if i == 0:
        put(here / "QEF_INVERSE_CANONICAL.json", result.stdout)
for i in range(3):
    command = ["cmp", str(out / f"run{i}.stdout"), str(here / "QEF_INVERSE_CANONICAL.json")]
    result = subprocess.run(command, capture_output=True)
    put(out / f"cmp{i}.stdout", result.stdout)
    put(out / f"cmp{i}.stderr", result.stderr)
    put(out / f"cmp{i}.receipt.json", (json.dumps({"command": command,
        "returncode": result.returncode, "utc": datetime.now(timezone.utc).isoformat()},
        sort_keys=True, indent=2)+"\n").encode())
    if result.returncode:
        raise SystemExit(result.returncode)
after = pins()
put(out / "INPUTS_AFTER.sha256", after)
if before != after:
    raise RuntimeError("source changed during run triple")
summary = {"runs": receipts, "raw_comparisons": 3, "inputs_unchanged": True,
           "canonical_sha256": digest(here / "QEF_INVERSE_CANONICAL.json")}
put(out / "SUMMARY.json", (json.dumps(summary, sort_keys=True, indent=2)+"\n").encode())
manifest = "".join(f"{digest(path)}  {path.relative_to(out)}\n" for path in sorted(out.rglob("*")) if path.is_file())
put(out / "SHA256SUMS", manifest.encode())
print(json.dumps({"status": "PASS", "runs": 3, "raw_comparisons": 3,
                  "canonical_sha256": summary["canonical_sha256"]}, sort_keys=True))
