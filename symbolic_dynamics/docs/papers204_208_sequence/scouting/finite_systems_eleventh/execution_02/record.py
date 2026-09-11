#!/usr/bin/env python3
"""Freeze original inputs and record actual child execution, never overwrite."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    name = sys.argv[1]
    assert name in ("execution_01", "execution_02")
    dest = BASE/name
    dest.mkdir(exist_ok=False)
    names = ("INTAKE.md", "pilot.py", "record.py")
    for item in names:
        (dest/item).write_bytes((BASE/item).read_bytes())
    before = {item: digest(dest/item) for item in names}
    (dest/"INPUTS_BEFORE.json").write_text(json.dumps(before, indent=2)+"\n")
    started = now()
    command = [sys.executable, "-B", "pilot.py"]
    child = subprocess.run(command, cwd=dest, capture_output=True)
    ended = now()
    (dest/"stdout.jsonl").write_bytes(child.stdout)
    (dest/"stderr.txt").write_bytes(child.stderr)
    after = {item: digest(dest/item) for item in names}
    (dest/"INPUTS_AFTER.json").write_text(json.dumps(after, indent=2)+"\n")
    comparison = None
    if name == "execution_02":
        cmd = ["cmp", "--", str(BASE/"execution_01/stdout.jsonl"),
               str(dest/"stdout.jsonl")]
        proc = subprocess.run(cmd, capture_output=True)
        (dest/"cmp.stdout.txt").write_bytes(proc.stdout)
        (dest/"cmp.stderr.txt").write_bytes(proc.stderr)
        comparison = dict(command=cmd, exit_code=proc.returncode,
                          stdout_bytes=len(proc.stdout), stderr_bytes=len(proc.stderr))
    record = dict(command=command, cwd=str(dest), started=started, ended=ended,
                  python=sys.version, exit_code=child.returncode,
                  stdout_bytes=len(child.stdout), stderr_bytes=len(child.stderr),
                  stdout_sha256=hashlib.sha256(child.stdout).hexdigest(),
                  input_pins_unchanged=before == after, comparison=comparison)
    (dest/"EXECUTION.json").write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps(record, sort_keys=True))
    assert child.returncode == 0 and not child.stderr and before == after
    if comparison:
        assert comparison["exit_code"] == 0


if __name__ == "__main__":
    main()
