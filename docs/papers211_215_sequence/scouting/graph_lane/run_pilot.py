#!/usr/bin/env python3
"""Capture one bounded native author execution without hidden retries."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "execution_01"


def pin(path):
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def main():
    OUTPUT.mkdir(exist_ok=False)
    relative = [
        "docs/papers211_215_sequence/scouting/graph_lane/pilot_cbf.py",
        "docs/papers211_215_sequence/scouting/graph_lane/run_pilot.py",
        "docs/papers211_215_sequence/scouting/graph_lane/INTAKE.md",
        "papers/123-odd-component-complementation/main.tex",
        "papers/163-complemented-shadow-dynamics/main.tex",
        "docs/papers197_201_sequence/scouting/replacement_lane/BREADTH_AND_KILL_LEDGER.md",
        "docs/papers117_121_sequence/scouting/COMBINATORIAL_LANDSCAPE.md",
    ]
    command = [sys.executable, "-I", "-S", str(HERE / "pilot_cbf.py")]
    # Explicit environment: no inherited PYTHONPATH/site settings or user secrets.
    env = {"PATH": "/usr/bin:/bin", "LC_ALL": "C", "TZ": "UTC"}
    before = [pin(ROOT / p) for p in relative]
    before.append(pin(Path(sys.executable).resolve()))
    start = time.time()
    completed = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, timeout=60)
    end = time.time()
    (OUTPUT / "stdout.jsonl").write_bytes(completed.stdout)
    (OUTPUT / "stderr.txt").write_bytes(completed.stderr)
    after = [pin(ROOT / p) for p in relative]
    after.append(pin(Path(sys.executable).resolve()))
    receipt = {"command": command, "cwd": str(ROOT), "environment": env,
               "started_unix": start, "ended_unix": end, "seconds": end-start,
               "returncode": completed.returncode, "inputs_before": before,
               "inputs_after": after, "input_pins_unchanged": before == after,
               "stdout": pin(OUTPUT / "stdout.jsonl"), "stderr": pin(OUTPUT / "stderr.txt"),
               "runtime_scope": "CPython executable and explicit flags/environment pinned; stdlib/dynamic-loader closure not captured. This scout is not a strict terminal replay or reusable manuscript-review execution."}
    (OUTPUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: receipt[k] for k in ("command", "returncode", "seconds", "input_pins_unchanged", "stdout", "stderr")}, sort_keys=True))
    for line in completed.stdout.splitlines():
        if b'"kind":"box"' in line or b'"kind":"complete"' in line:
            print(line.decode("utf-8"))
    return completed.returncode


if __name__ == "__main__":
    sys.exit(main())
