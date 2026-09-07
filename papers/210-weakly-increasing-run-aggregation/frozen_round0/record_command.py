#!/usr/bin/env python3
"""Capture one real author producer command; write only an absent local record dir."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def main():
    paper = Path(__file__).resolve().parent
    tag, *command = sys.argv[1:]
    if not tag or "/" in tag or tag in {".", ".."}:
        raise ValueError("single record tag required")
    record = paper / "execution" / tag
    record.mkdir(parents=True, exist_ok=False)
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()
    pinned = {str(Path(__file__).resolve()): sha(Path(__file__))}
    for value in command:
        path = Path(value)
        if path.is_file():
            pinned[str(path.resolve())] = sha(path)
    metadata = {"argv": command, "cwd": str(Path.cwd()), "start_ns": time.time_ns(),
                "input_sha256": pinned,
                "relevant_parent_environment": {k: os.environ.get(k) for k in
                    ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "PYTHONHOME", "PYTHONPATH",
                     "PYTHONHASHSEED", "PYTHONPYCACHEPREFIX", "SOURCE_DATE_EPOCH", "TEXINPUTS")}}
    (record / "ATTEMPT.json").write_text(json.dumps(metadata, indent=2) + "\n")
    with (record / "stdout").open("xb") as stdout, (record / "stderr").open("xb") as stderr:
        result = subprocess.run(command, stdout=stdout, stderr=stderr, check=False)
    post = {name: sha(Path(name)) for name in pinned}
    report = {"native_exit": result.returncode, "end_ns": time.time_ns(),
              "stdout_sha256": sha(record / "stdout"), "stderr_sha256": sha(record / "stderr"),
              "input_sha256_after": post, "inputs_unchanged": pinned == post}
    (record / "RESULT.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"tag": tag, **report}, sort_keys=True))
    return result.returncode if pinned == post else 1


if __name__ == "__main__":
    raise SystemExit(main())
