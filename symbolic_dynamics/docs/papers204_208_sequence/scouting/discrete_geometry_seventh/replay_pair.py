#!/usr/bin/env python3
"""Read-only replay producer; embeds complete child stdout and stderr.

Prints JSON to stdout; does not write its own receipt or mutate canonicals.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


def main():
    directory = Path(__file__).resolve().parent
    dependencies = ("INTAKE.md", "pilot.py", "CANONICAL.json", "PROOF_BOUNDARIES.md",
                    "proof_checks.py", "PROOF_CANONICAL.json", "replay_pair.py")
    pins = {name: sha256((directory / name).read_bytes()).hexdigest() for name in dependencies}
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0")
    runs, success = [], True
    for script, canonical in (("pilot.py", "CANONICAL.json"),
                              ("proof_checks.py", "PROOF_CANONICAL.json")):
        expected = (directory / canonical).read_bytes()
        for trial in (1, 2):
            command = [sys.executable, script]
            started = datetime.now(timezone.utc).isoformat()
            clock = time.monotonic()
            child = subprocess.run(command, cwd=directory, env=environment, capture_output=True,
                                   check=False, timeout=300)
            comparison_exit = 0 if child.stdout == expected else 1
            success &= child.returncode == 0 and comparison_exit == 0 and child.stderr == b""
            runs.append({"command": command, "cwd": str(directory), "trial": trial,
                         "started_utc": started, "elapsed_seconds": round(time.monotonic() - clock, 6),
                         "exit_code": child.returncode, "canonical": canonical,
                         "raw_bytes_comparison_exit": comparison_exit,
                         "stdout_bytes": len(child.stdout), "stdout_sha256": sha256(child.stdout).hexdigest(),
                         "stdout": child.stdout.decode(), "stderr": child.stderr.decode()})
    after = {name: sha256((directory / name).read_bytes()).hexdigest() for name in dependencies}
    unchanged = after == pins
    success &= unchanged
    print(json.dumps({"status": "PASS" if success else "FAIL", "role": "author_raw_replay_pair",
                      "python": sys.version, "platform": platform.platform(),
                      "environment_overrides": {"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"},
                      "dependencies_before": pins, "dependencies_after": after,
                      "dependencies_unchanged": unchanged, "runs": runs}, sort_keys=True, indent=2))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
