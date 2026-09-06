#!/usr/bin/env python3
"""Run an actual fresh MNC author pair, preserving complete child bytes.

This standard-library harness does not contribute mathematical assertions.
It refuses existing output directories and never imports the verifier.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
from datetime import datetime, timezone


def digest(path):
    data = path.read_bytes()
    return {"sha256": sha256(data).hexdigest(), "bytes": len(data)}


def main():
    base = Path(__file__).resolve().parent
    if len(sys.argv) != 2 or Path(sys.argv[1]).name != sys.argv[1]:
        raise SystemExit("usage: python3 replay_author.py NEW_DIRECTORY_BASENAME")
    out = base / sys.argv[1]
    out.mkdir(exist_ok=False)
    inputs = [base / name for name in
              ("verify_mnc.py", "CANONICAL.json", "PROOF_PACKAGE.md", "SOURCE_BOUNDARY.md", "replay_author.py")]
    before = {p.name: digest(p) for p in inputs}
    env = dict(os.environ, PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1")
    rows = []
    for label in ("run1", "run2"):
        command = [sys.executable, "-B", str(base / "verify_mnc.py")]
        child = subprocess.run(command, cwd=base, env=env, capture_output=True)
        stdout, stderr = out / (label + ".stdout.json"), out / (label + ".stderr")
        stdout.write_bytes(child.stdout)
        stderr.write_bytes(child.stderr)
        compare = subprocess.run(["cmp", str(base / "CANONICAL.json"), str(stdout)], capture_output=True)
        (out / (label + ".cmp.stdout")).write_bytes(compare.stdout)
        (out / (label + ".cmp.stderr")).write_bytes(compare.stderr)
        rows.append({"label": label, "command": command, "cwd": str(base),
                     "child_exit": child.returncode, "compare_exit": compare.returncode,
                     "stdout": digest(stdout), "stderr": digest(stderr),
                     "assertions": json.loads(child.stdout).get("assertions") if child.returncode == 0 else None})
    after = {p.name: digest(p) for p in inputs}
    verdict = before == after and all(r["child_exit"] == r["compare_exit"] == 0 for r in rows)
    receipt = {"kind": "ACTUAL_FRESH_AUTHOR_PAIR_NOT_REVIEW_OR_ADMISSION",
               "utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version, "platform": platform.platform(),
               "runtime_settings": {"PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1"},
               "inputs_before": before, "inputs_after": after,
               "inputs_unchanged": before == after, "runs": rows,
               "pass": verdict}
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if verdict else 1)


if __name__ == "__main__":
    main()
