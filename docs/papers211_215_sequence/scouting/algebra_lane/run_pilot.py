"""Capture one native bounded pilot; generated artifacts are never overwritten."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "execution_01"
OUT.mkdir(exist_ok=False)


def pin(path):
    path = Path(path).resolve()
    return {"path": str(path), "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


inputs = [ROOT / "INTAKE.md", ROOT / "pilot.py", ROOT / "run_pilot.py",
          Path(sys.executable).resolve()]
before = [pin(p) for p in inputs]
env = {"PATH": "/usr/bin:/bin", "LC_ALL": "C", "LANG": "C",
       "TZ": "UTC", "PYTHONHASHSEED": "0"}
argv = [str(Path(sys.executable).resolve()), "-I", "-S", "-B", str(ROOT / "pilot.py")]
started = time.time()
result = subprocess.run(argv, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, timeout=60, check=False)
elapsed = time.time() - started
(OUT / "stdout.jsonl").write_bytes(result.stdout)
(OUT / "stderr.txt").write_bytes(result.stderr)
after = [pin(p) for p in inputs]
modules = []
for name, module in sorted(sys.modules.items()):
    file = getattr(module, "__file__", None)
    if file and Path(file).is_file():
        modules.append({"module": name, **pin(file)})
receipt = {"scope": "ONE_EXPLORATORY_NATIVE_RUN_NOT_HERMETIC_REPLAY",
           "argv": argv, "cwd": str(ROOT), "environment": env,
           "timeout_seconds": 60, "native_exit": result.returncode,
           "elapsed_seconds": elapsed, "started_unix_seconds": started,
           "python_version": sys.version, "input_pins_before": before,
           "input_pins_after": after, "inputs_unchanged": before == after,
           "driver_loaded_module_pins": modules,
           "provenance_limit": "The final child_runtime row pins child-loaded modules; neither inventory is a complete loader/config key.",
           "stdout": pin(OUT / "stdout.jsonl"), "stderr": pin(OUT / "stderr.txt")}
(OUT / "NATIVE_RECEIPT.json").write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n", encoding="utf-8")
assert before == after
assert result.returncode == 0, result.returncode
for line in result.stdout.splitlines():
    row = json.loads(line)
    if row["kind"] == "summary":
        row.pop("cycles")
        row.pop("deepest_states")
        print(json.dumps(row, sort_keys=True))
print(json.dumps({"native_exit": result.returncode, "elapsed_seconds": elapsed,
                  "stdout_bytes": len(result.stdout), "stderr_bytes": len(result.stderr),
                  "inputs_unchanged": before == after}, sort_keys=True))
