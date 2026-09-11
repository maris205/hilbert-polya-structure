#!/usr/bin/env python3
"""Physical pair runner; records observed child exits and raw cmp exits."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import os
import platform
import subprocess
import sys


def h(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    base = Path(__file__).resolve().parent
    workspace = base.parents[4]
    name = sys.argv[1]
    if not name or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789_" for c in name):
        raise ValueError("fixed package-local simple output directory required")
    out = base / name
    out.mkdir(exist_ok=False)
    inputs = {"verify.py": h(base / "verify.py"),
              "CANONICAL.json": h(base / "CANONICAL.json"),
              "INPUT_PINS.sha256": h(base / "INPUT_PINS.sha256")}
    pin_rows = []
    for line in (base / "INPUT_PINS.sha256").read_text().splitlines():
        expected, rel = line.split("  ", 1)
        actual = h(workspace / rel)
        if actual != expected:
            raise AssertionError(["input pin before", rel, expected, actual])
        pin_rows.append((rel, expected))
    env = dict(os.environ)
    settings = {"PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C", "TZ": "UTC"}
    env.update(settings)
    receipt = {"started_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.executable, "python_version": platform.python_version(),
               "cwd": str(base), "settings": settings, "inputs_before": inputs,
               "pinned_input_count": len(pin_rows), "runs": []}
    for run in (1, 2):
        stem = "run" + str(run)
        cmd = [sys.executable, "-B", "verify.py"]
        with (out / (stem + ".stdout.json")).open("wb") as stdout, (out / (stem + ".stderr")).open("wb") as stderr:
            child = subprocess.run(cmd, cwd=base, env=env, stdout=stdout, stderr=stderr)
        cmp_cmd = ["cmp", "CANONICAL.json", str(Path(name) / (stem + ".stdout.json"))]
        with (out / (stem + ".cmp.stdout")).open("wb") as stdout, (out / (stem + ".cmp.stderr")).open("wb") as stderr:
            compared = subprocess.run(cmp_cmd, cwd=base, stdout=stdout, stderr=stderr)
        row = {"command": cmd, "child_exit": child.returncode,
               "compare_command": cmp_cmd, "compare_exit": compared.returncode,
               "stdout_sha256": h(out / (stem + ".stdout.json")),
               "stdout_bytes": (out / (stem + ".stdout.json")).stat().st_size,
               "stderr_bytes": (out / (stem + ".stderr")).stat().st_size}
        receipt["runs"].append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
        if child.returncode or compared.returncode:
            (out / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
            raise AssertionError("child or raw comparator failed; outputs retained")
    receipt["inputs_after"] = {p: h(base / p) for p in inputs}
    receipt["context_pins_unchanged"] = all(h(workspace / p) == expected for p, expected in pin_rows)
    receipt["completed_utc"] = datetime.now(timezone.utc).isoformat()
    receipt["status"] = "PASS" if receipt["inputs_after"] == inputs and receipt["context_pins_unchanged"] else "FAIL"
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    if receipt["status"] != "PASS":
        raise AssertionError("inputs changed")


if __name__ == "__main__":
    main()
