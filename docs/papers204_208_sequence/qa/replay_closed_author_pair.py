#!/usr/bin/env python3
"""Root replay of a closed author producer; no independent-review claim.

Usage: SCRIPT PACKAGE VERIFIER NEW_OUTPUT_DIRECTORY
The author package must be closed by MANIFEST.sha256. No package file is
modified, existing output directories are refused, and all child bytes stay.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


def file_info(path):
    raw = path.read_bytes()
    return {"sha256": sha256(raw).hexdigest(), "bytes": len(raw)}


def snapshot(package):
    return {str(p.relative_to(package)): file_info(p)
            for p in sorted(package.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts}


def main():
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    root = Path(__file__).resolve().parents[3]
    package, verifier, out = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]).resolve()
    if Path(verifier).name != verifier or not (package / verifier).is_file():
        raise SystemExit("invalid producer basename")
    out.mkdir(parents=True, exist_ok=False)
    before = snapshot(package)
    pin_rows = []
    for filename, cwd in (("MANIFEST.sha256", package), ("INPUT_PINS.sha256", root)):
        command = ["sha256sum", "-c", str(package / filename)]
        checked = subprocess.run(command, cwd=cwd, capture_output=True)
        (out / (filename + ".stdout")).write_bytes(checked.stdout)
        (out / (filename + ".stderr")).write_bytes(checked.stderr)
        pin_rows.append({"command": command, "cwd": str(cwd), "exit": checked.returncode})
    env = dict(os.environ, PYTHONHASHSEED="0", PYTHONDONTWRITEBYTECODE="1")
    runs = []
    for label in ("run1", "run2"):
        command = [sys.executable, "-B", str(package / verifier)]
        child = subprocess.run(command, cwd=package, env=env, capture_output=True)
        stdout = out / (label + ".stdout")
        stdout.write_bytes(child.stdout)
        (out / (label + ".stderr")).write_bytes(child.stderr)
        compare_cmd = ["cmp", str(package / "CANONICAL.json"), str(stdout)]
        comparison = subprocess.run(compare_cmd, capture_output=True)
        (out / (label + ".cmp.stdout")).write_bytes(comparison.stdout)
        (out / (label + ".cmp.stderr")).write_bytes(comparison.stderr)
        result = json.loads(child.stdout) if child.returncode == 0 else {}
        runs.append({"command": command, "cwd": str(package), "child_exit": child.returncode,
                     "compare_command": compare_cmd, "compare_exit": comparison.returncode,
                     "assertions": result.get("assertions"), "stdout": file_info(stdout),
                     "stderr": file_info(out / (label + ".stderr"))})
    pair_cmd = ["cmp", str(out / "run1.stdout"), str(out / "run2.stdout")]
    pair = subprocess.run(pair_cmd, capture_output=True)
    (out / "pair.cmp.stdout").write_bytes(pair.stdout)
    (out / "pair.cmp.stderr").write_bytes(pair.stderr)
    after = snapshot(package)
    passed = (before == after and pair.returncode == 0 and
              all(row["exit"] == 0 for row in pin_rows) and
              all(row["child_exit"] == row["compare_exit"] == 0 for row in runs))
    receipt = {"kind": "ACTUAL_ROOT_REPLAY_OF_AUTHOR_PRODUCER_NOT_INDEPENDENT_REVIEW",
               "utc": datetime.now(timezone.utc).isoformat(), "python": sys.version,
               "platform": platform.platform(), "harness": file_info(Path(__file__)),
               "runtime_settings": {"PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1"},
               "before_package_files": before, "after_package_files": after,
               "package_unchanged": before == after, "pin_checks": pin_rows, "runs": runs,
               "pair_compare_command": pair_cmd, "pair_compare_exit": pair.returncode,
               "pass": passed}
    (out / "RECEIPT.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": passed, "receipt": str(out / "RECEIPT.json"),
                      "assertions": [r["assertions"] for r in runs], "pins": pin_rows}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
