#!/usr/bin/env python3
"""Record the declared, original-box OFS tree probe in a fresh directory."""
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        raise SystemExit("usage: record_tree_probe.py SERIAL")
    folder = ROOT / ("tree_execution_"+sys.argv[1].zfill(2))
    folder.mkdir(exist_ok=False)
    inputs = ("DESK_DECLARATION.md", "INTAKE.md", "pilot.py",
              "OFS_FOLLOWUP_DECLARATION.md", "ofs_tree_probe.py", "record_tree_probe.py")
    pins = {name: sha(ROOT/name) for name in inputs}
    for name in inputs:
        shutil.copy2(ROOT/name, folder/name)
    command = [sys.executable, "-I", str(folder/"ofs_tree_probe.py")]
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    child = subprocess.run(command, cwd=folder, capture_output=True)
    ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (folder/"stdout.json").write_bytes(child.stdout)
    (folder/"stderr.txt").write_bytes(child.stderr)
    after = {name: sha(ROOT/name) for name in inputs}
    record = {"role": "author_tree_probe_not_independent_review", "command": command,
              "cwd": str(folder), "started_utc": started, "ended_utc": ended,
              "child_exit": child.returncode, "before_inputs": pins,
              "after_inputs": after, "inputs_unchanged": pins == after,
              "stdout_bytes": len(child.stdout), "stderr_bytes": len(child.stderr),
              "stdout_sha256": hashlib.sha256(child.stdout).hexdigest()}
    (folder/"RECORD.json").write_text(json.dumps(record, sort_keys=True, indent=2)+"\n")
    print(json.dumps(record, sort_keys=True, indent=2))
    if child.returncode or pins != after:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
