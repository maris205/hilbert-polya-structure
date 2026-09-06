#!/usr/bin/env python3
"""Cold compile and execute UGR reviewer producer; preserve every stream.

With --canonical, the first successful stdout becomes CANONICAL.jsonl;
otherwise perform two fresh complete executions and actual raw cmp calls.
No author/repository verifier is imported or executed.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


def info(path):
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha256(data).hexdigest()}


def main():
    base = Path(__file__).resolve().parent
    if len(sys.argv) not in (2, 3) or Path(sys.argv[1]).name != sys.argv[1]:
        raise SystemExit("usage: record_gate.py NEW_SUBDIRECTORY [--canonical]")
    produce = len(sys.argv) == 3 and sys.argv[2] == "--canonical"
    if len(sys.argv) == 3 and not produce:
        raise SystemExit("unknown option")
    out = base / sys.argv[1]
    out.mkdir(exist_ok=False)
    canonical = base / "CANONICAL.jsonl"
    if produce and canonical.exists():
        raise SystemExit("canonical already exists")
    env = dict(os.environ, LC_ALL="C")
    compile_command = ["g++", "-std=c++17", "-O2", "-Wall", "-Wextra", "-Werror",
                       str(base / "verify_gate.cpp"), "-o", str(out / "verifier")]
    compiler = subprocess.run(["g++", "--version"], capture_output=True, env=env)
    (out / "compiler.stdout").write_bytes(compiler.stdout)
    (out / "compiler.stderr").write_bytes(compiler.stderr)
    compiled = subprocess.run(compile_command, capture_output=True, env=env)
    (out / "compile.stdout").write_bytes(compiled.stdout)
    (out / "compile.stderr").write_bytes(compiled.stderr)
    rows = []
    if compiled.returncode == 0:
        for label in (("run0",) if produce else ("run1", "run2")):
            command = [str(out / "verifier")]
            child = subprocess.run(command, cwd=base, capture_output=True, env=env)
            stdout, stderr = out / (label + ".stdout.jsonl"), out / (label + ".stderr")
            stdout.write_bytes(child.stdout)
            stderr.write_bytes(child.stderr)
            row = {"command": command, "child_exit": child.returncode,
                   "stdout": info(stdout), "stderr": info(stderr)}
            if child.returncode == 0:
                summary = json.loads(child.stdout.splitlines()[-1])
                row["assertions"] = summary["assertions"]
                if produce:
                    canonical.write_bytes(child.stdout)
                else:
                    cmp = subprocess.run(["cmp", str(canonical), str(stdout)], capture_output=True)
                    (out / (label + ".cmp.stdout")).write_bytes(cmp.stdout)
                    (out / (label + ".cmp.stderr")).write_bytes(cmp.stderr)
                    row["comparison_exit"] = cmp.returncode
            rows.append(row)
    receipt = {"utc": datetime.now(timezone.utc).isoformat(),
               "kind": "UGR_NONAUTHOR_CANDIDATE_GATE_ACTUAL_EXECUTION",
               "platform": platform.platform(), "compile_command": compile_command,
               "compiler_exit": compiler.returncode, "compile_exit": compiled.returncode,
               "source": info(base / "verify_gate.cpp"), "runs": rows,
               "binary": info(out / "verifier") if compiled.returncode == 0 else None,
               "canonical_production": produce,
               "pass": compiled.returncode == 0 and len(rows) == (1 if produce else 2)
                       and all(r["child_exit"] == 0 and (produce or r.get("comparison_exit") == 0) for r in rows)}
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if receipt["pass"] else 1)


if __name__ == "__main__":
    main()
