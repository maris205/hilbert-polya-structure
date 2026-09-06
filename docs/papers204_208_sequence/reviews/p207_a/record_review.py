#!/usr/bin/env python3
"""Actual exclusive-write P207 A execution receipts; not a math producer.

Run once with initial, then independently with pair_01 and pair_02. Each
mathematical child is a new Python process in its own new source-only cwd.
The producer itself neither reads this recorder nor any pinned data.
"""

from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[3]
SETTINGS = {"LC_ALL": "C", "TZ": "UTC", "PYTHONHASHSEED": "0",
            "PYTHONDONTWRITEBYTECODE": "1", "PYTHONSAFEPATH": "1"}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def write(path, data):
    with path.open("xb") as stream:
        stream.write(data if isinstance(data, bytes) else data.encode())


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(path, value):
    write(path, json.dumps(value, sort_keys=True, indent=2) + "\n")


def command(argv, folder, stem, env):
    started, clock = stamp(), time.monotonic()
    out, err = folder / (stem + ".stdout"), folder / (stem + ".stderr")
    with out.open("xb") as stdout, err.open("xb") as stderr:
        child = subprocess.run(argv, cwd=folder, env=env, stdout=stdout, stderr=stderr, check=False)
    return {"argv": argv, "cwd": str(folder), "started_utc": started,
            "finished_utc": stamp(), "elapsed_seconds": time.monotonic() - clock,
            "exit_code": child.returncode,
            "stdout": {"path": str(out.relative_to(HERE)), "bytes": out.stat().st_size, "sha256": digest(out)},
            "stderr": {"path": str(err.relative_to(HERE)), "bytes": err.stat().st_size, "sha256": digest(err)}}


def require(item):
    if item["exit_code"]:
        raise RuntimeError("Failed child preserved: " + repr(item["argv"]))


def pin_inputs():
    pins = {}
    for line in (HERE / "INPUT_PINS.sha256").read_text().splitlines():
        expected, relative = line.split("  ", 1)
        actual = digest(WORKSPACE / relative)
        if actual != expected:
            raise RuntimeError("Frozen input does not match intake pin: " + relative)
        pins[relative] = actual
    for filename in ("verify.py", "record_review.py", "INPUT_PINS.sha256"):
        path = HERE / filename
        pins[str(path.relative_to(WORKSPACE))] = digest(path)
    return pins


def lines(pins):
    return "".join(f"{value}  {name}\n" for name, value in sorted(pins.items()))


def main():
    tag = sys.argv[1] if len(sys.argv) == 2 else ""
    if tag not in {"initial", "pair_01", "pair_02"}:
        raise SystemExit("expected exactly initial, pair_01 or pair_02")
    attempt = HERE / "execution" / tag
    attempt.mkdir(parents=True, exist_ok=False)
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    env.update(SETTINGS)
    before = pin_inputs()
    write(attempt / "INPUT_PINS.before.sha256", lines(before))
    executable = str(Path(sys.executable).resolve())
    receipt = {"schema": "p207-review-a-actual-execution-v1", "attempt": tag,
               "started_utc": stamp(), "status": "IN_PROGRESS", "commands": [],
               "reviewer": "batch197_lzk_gate", "reviewer_not_mathematical_author": True,
               "prior_gate_familiarity_and_algorithm_reuse_disclosed": True,
               "python": {"executable": executable, "sha256": digest(Path(executable)),
                          "version": sys.version, "platform": platform.platform()},
               "declared_environment": SETTINGS, "frozen_plus_own_inputs": len(before),
               "canonical_is_output_not_math_producer_input": True}
    try:
        version = command([executable, "--version"], attempt, "python_version", env)
        receipt["commands"].append(version)
        require(version)
        dependency = command(["ldd", executable], attempt, "python_link_dependencies", env)
        receipt["commands"].append(dependency)
        require(dependency)
        canonical = HERE / "CANONICAL.json"
        if tag == "initial" and canonical.exists():
            raise RuntimeError("Initial production refuses to overwrite canonical")
        if tag != "initial":
            write(attempt / "CANONICAL.input.json", canonical.read_bytes())
        outputs = []
        for number in ([0] if tag == "initial" else [1, 2]):
            folder = attempt / f"run{number}"
            folder.mkdir()
            snapshot = folder / "verify.py"
            write(snapshot, (HERE / "verify.py").read_bytes())
            if digest(snapshot) != digest(HERE / "verify.py"):
                raise RuntimeError("Snapshot differs from pinned independent source")
            run = command([executable, "-B", str(snapshot)], folder, "producer", env)
            receipt["commands"].append(run)
            require(run)
            output = folder / "producer.stdout"
            parsed = json.loads(output.read_bytes())
            if parsed.get("status") != "PASS" or not parsed.get("assertions"):
                raise RuntimeError("Missing full independent PASS output")
            if parsed["assertions"] != sum(parsed["assertions_by_section"].values()):
                raise RuntimeError("Incorrect independent assertion census")
            if run["stderr"]["bytes"]:
                raise RuntimeError("Producer stderr is nonempty and preserved")
            receipt.setdefault("numerical_runs", []).append({"number": number,
                "assertions": parsed["assertions"], "complete_stdout_sha256": digest(output),
                "ordered_checked_record_sha256": parsed["ordered_checked_record_sha256"],
                "source_sha256": digest(snapshot)})
            if tag == "initial":
                write(canonical, output.read_bytes())
                write(attempt / "CANONICAL.input.json", output.read_bytes())
            comparison = command(["cmp", str(output), str(attempt / "CANONICAL.input.json")],
                                 folder, "canonical.cmp", env)
            receipt["commands"].append(comparison)
            require(comparison)
            outputs.append(output)
        if len(outputs) == 2:
            comparison = command(["cmp", str(outputs[0]), str(outputs[1])], attempt, "pair.cmp", env)
            receipt["commands"].append(comparison)
            require(comparison)
        comparison = command(["cmp", str(canonical), str(attempt / "CANONICAL.input.json")],
                             attempt, "live_canonical.cmp", env)
        receipt["commands"].append(comparison)
        require(comparison)
        after = pin_inputs()
        write(attempt / "INPUT_PINS.after.sha256", lines(after))
        if before != after:
            raise RuntimeError("Inputs changed during actual independent run")
        receipt["inputs_unchanged"] = True
        receipt["status"] = "PASS"
    except BaseException as error:
        receipt["status"] = "FAIL"
        receipt["failure"] = {"type": type(error).__name__, "message": str(error)}
        write(attempt / "exception.txt", traceback.format_exc())
    receipt["finished_utc"] = stamp()
    save(attempt / "RECEIPT.json", receipt)
    manifest = []
    for path in sorted(attempt.rglob("*")):
        if path.is_file():
            manifest.append(f"{digest(path)}  {path.relative_to(attempt)}\n")
    write(attempt / "MANIFEST.sha256", "".join(manifest))
    print(json.dumps({"status": receipt["status"], "receipt": str(attempt / "RECEIPT.json"),
                      "numerical_runs": receipt.get("numerical_runs", [])}, sort_keys=True, indent=2))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
