#!/usr/bin/env python3
"""Freeze declared author inputs and retain actual raw theorem-check runs."""
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
        raise SystemExit("usage: record_ofs_theorems.py SERIAL")
    serial = int(sys.argv[1])
    folder = ROOT/("ofs_theorem_execution_"+str(serial).zfill(2))
    folder.mkdir(exist_ok=False)
    names = ("DESK_DECLARATION.md", "INTAKE.md", "OFS_PROOF_PACKAGE.md",
             "OFS_THEOREM_CHECK_DECLARATION.md", "verify_ofs.py", "record_ofs_theorems.py")
    before = {name: sha(ROOT/name) for name in names}
    for name in names:
        shutil.copy2(ROOT/name, folder/name)
    command = [sys.executable, "-I", str(folder/"verify_ofs.py")]
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    child = subprocess.run(command, cwd=folder, capture_output=True)
    end = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (folder/"stdout.json").write_bytes(child.stdout)
    (folder/"stderr.txt").write_bytes(child.stderr)
    after = {name: sha(ROOT/name) for name in names}
    comparison = None
    if serial > 1:
        cmp_command = ["cmp", str(ROOT/"ofs_theorem_execution_01/stdout.json"), str(folder/"stdout.json")]
        comp = subprocess.run(cmp_command, capture_output=True)
        (folder/"cmp.stdout.txt").write_bytes(comp.stdout)
        (folder/"cmp.stderr.txt").write_bytes(comp.stderr)
        comparison = {"command": cmp_command, "exit": comp.returncode,
                      "stdout_bytes": len(comp.stdout), "stderr_bytes": len(comp.stderr)}
    record = {"role": "standalone_author_theorem_check_not_independent_review",
              "command": command, "cwd": str(folder), "started_utc": start,
              "ended_utc": end, "child_exit": child.returncode,
              "before_inputs": before, "after_inputs": after,
              "inputs_unchanged": before == after,
              "stdout_bytes": len(child.stdout), "stderr_bytes": len(child.stderr),
              "stdout_sha256": hashlib.sha256(child.stdout).hexdigest(),
              "raw_comparison": comparison}
    (folder/"RECORD.json").write_text(json.dumps(record, sort_keys=True, indent=2)+"\n")
    print(json.dumps(record, sort_keys=True, indent=2))
    if child.returncode or child.stderr or before != after or comparison and comparison["exit"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
