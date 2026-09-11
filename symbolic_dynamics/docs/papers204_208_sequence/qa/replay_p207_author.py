#!/usr/bin/env python3
"""Scoped root pair for P207's author-owned seal, not the old package schema.

The paper is being integrated; only the closed author-owned dependency set
is a replay input. The immutable historical generic harness is not changed.
"""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


def info(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper", type=Path)
    parser.add_argument("new_output", type=Path)
    args = parser.parse_args()
    paper = args.paper.resolve(strict=True)
    out = args.new_output.resolve()
    seal = paper / "author_replay/OWNED_MANIFEST.sha256"
    pinned = {}
    for line in seal.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        path = paper / relative
        if not path.is_relative_to(paper) or ".." in Path(relative).parts:
            raise SystemExit("unsafe seal path")
        if info(path)["sha256"] != digest or relative in pinned:
            raise SystemExit("bad author-owned seal")
        pinned[relative] = info(path)
    if not all(name in pinned for name in ("verify.py", "CANONICAL.json", "record_author.py", "AUTHOR_EXECUTION.md")):
        raise SystemExit("required closed author inputs absent")
    out.mkdir(parents=True, exist_ok=False)
    for name in ("verify.py", "CANONICAL.json"):
        shutil.copyfile(paper / name, out / name)
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    settings = {"LC_ALL": "C", "TZ": "UTC", "PYTHONHASHSEED": "0",
                "PYTHONDONTWRITEBYTECODE": "1", "PYTHONSAFEPATH": "1"}
    env.update(settings)
    commands = []

    def execute(command, label, cwd):
        child = subprocess.run(command, cwd=cwd, env=env, capture_output=True)
        stdout, stderr = out / (label + ".stdout"), out / (label + ".stderr")
        stdout.write_bytes(child.stdout)
        stderr.write_bytes(child.stderr)
        row = {"command": command, "cwd": str(cwd), "exit_code": child.returncode,
               "stdout": info(stdout), "stderr": info(stderr)}
        commands.append(row)
        return row

    execute(["sha256sum", "-c", str(seal)], "owned_seal", paper)
    execute([sys.executable, "--version"], "python_version", out)
    counts = []
    for label in ("run1", "run2"):
        row = execute([sys.executable, "-B", str(out / "verify.py")], label, out)
        if row["exit_code"] == 0:
            counts.append(json.loads((out / (label + ".stdout")).read_bytes())["assertions"])
        execute(["cmp", str(out / "CANONICAL.json"), str(out / (label + ".stdout"))], label + ".cmp", out)
    execute(["cmp", str(out / "run1.stdout"), str(out / "run2.stdout")], "pair.cmp", out)
    after = {relative: info(paper / relative) for relative in pinned}
    passed = (all(row["exit_code"] == 0 for row in commands)
              and pinned == after and len(counts) == 2
              and all((out / (label + ".stderr")).stat().st_size == 0 for label in ("run1", "run2"))
              and info(out / "verify.py") == pinned["verify.py"]
              and info(out / "CANONICAL.json") == pinned["CANONICAL.json"])
    receipt = {"kind": "ACTUAL_ROOT_REPLAY_OF_P207_AUTHOR_NOT_INDEPENDENT_REVIEW",
               "utc": datetime.now(timezone.utc).isoformat(), "pass": passed,
               "paper": str(paper), "harness": info(Path(__file__)), "settings": settings,
               "python": sys.version, "author_owned_manifest": info(seal),
               "owned_input_count": len(pinned), "before_inputs": pinned,
               "after_inputs": after, "inputs_unchanged": pinned == after,
               "assertions_per_run": counts, "commands": commands}
    (out / "RECEIPT.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": passed, "assertions": counts, "receipt": str(out / "RECEIPT.json")}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
