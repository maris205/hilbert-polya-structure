#!/usr/bin/env python3
"""Record non-overwriting P207 author executions and raw-byte comparisons.

This recorder reads/pins provenance files and writes receipts. verify.py,
the mathematical producer, does neither. Every producer runs a byte-pinned
standalone snapshot inside its own fresh attempt directory. Only the paths
owned by this author are written. Failed attempts are never overwritten.
"""

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import time
import traceback


PAPER = Path(__file__).resolve().parent
WORKSPACE = PAPER.parents[1]
SCOUT = "docs/papers204_208_sequence/scouting/word_local/"
SOURCE_PATHS = (
    "docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md",
    "docs/papers204_208_sequence/ARTIFACT_CONTRACT.md",
    SCOUT + "UGR_PROOF_WORK/PROOF_PACKAGE.md",
    SCOUT + "UGR_PROOF_WORK/verify_ugr.py",
    SCOUT + "UGR_PROOF_WORK/CANONICAL.json",
    SCOUT + "UGR_PROOF_WORK/MANIFEST.sha256",
    SCOUT + "LNR_INVERSE_WORK/PROOF_PACKAGE.md",
    SCOUT + "LNR_INVERSE_WORK/verify_inverse.py",
    SCOUT + "LNR_INVERSE_WORK/CANONICAL.json",
    SCOUT + "LNR_INVERSE_WORK/SOURCE_BOUNDARY.md",
    SCOUT + "LNR_INVERSE_WORK/MANIFEST.sha256",
    SCOUT + "UGR_GATE/CANDIDATE_GATE.md",
    SCOUT + "UGR_GATE/SOURCE_AUDIT.md",
    SCOUT + "UGR_GATE/INPUT_PINS.sha256",
    SCOUT + "UGR_GATE/MANIFEST.sha256",
)
SETTINGS = {"LC_ALL": "C", "TZ": "UTC", "PYTHONHASHSEED": "0",
            "PYTHONDONTWRITEBYTECODE": "1", "PYTHONSAFEPATH": "1"}


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest_bytes(data):
    return sha256(data).hexdigest()


def digest_file(path):
    return digest_bytes(path.read_bytes())


def exclusive_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def exclusive_text(path, data):
    exclusive_bytes(path, data.encode("utf-8"))


def save_json(path, obj):
    exclusive_text(path, json.dumps(obj, sort_keys=True, indent=2) + "\n")


def pins_text(pins):
    return "".join(f"{digest}  {path}\n" for path, digest in sorted(pins.items()))


def manifest(directory, filename="MANIFEST.sha256"):
    destination = directory / filename
    entries = []
    for path in sorted(directory.rglob("*")):
        if path.is_file() and path != destination:
            entries.append(f"{digest_file(path)}  {path.relative_to(directory).as_posix()}\n")
    exclusive_text(destination, "".join(entries))
    return {"path": str(destination.relative_to(PAPER)), "entries": len(entries),
            "sha256": digest_file(destination)}


def execute(argv, directory, stem, env):
    started, clock = utc(), time.monotonic()
    stdout_path, stderr_path = directory / f"{stem}.stdout", directory / f"{stem}.stderr"
    with stdout_path.open("xb") as output, stderr_path.open("xb") as errors:
        child = subprocess.run(argv, cwd=directory, env=env, stdout=output, stderr=errors, check=False)
    return {"argv": argv, "cwd": str(directory), "started_utc": started,
            "finished_utc": utc(), "elapsed_seconds": time.monotonic() - clock,
            "exit_code": child.returncode,
            "stdout": {"path": stdout_path.name, "bytes": stdout_path.stat().st_size,
                       "sha256": digest_file(stdout_path)},
            "stderr": {"path": stderr_path.name, "bytes": stderr_path.stat().st_size,
                       "sha256": digest_file(stderr_path)}}


def require_success(receipt):
    if receipt["exit_code"] != 0:
        raise RuntimeError(f"child failed with exit {receipt['exit_code']}: {receipt['argv']}")


def record_attempt(tag, initial):
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", tag):
        raise ValueError("tag must be a plain lowercase attempt name")
    directory = PAPER / "author_replay" / tag
    directory.mkdir(parents=True, exist_ok=False)
    receipt = {"schema": "p207-author-execution-v1", "role": "P207 author execution, not independent review",
               "started_utc": utc(), "initial_canonical_production": initial,
               "attempt": tag, "workspace": str(WORKSPACE), "paper_directory": str(PAPER),
               "declared_environment": SETTINGS, "python_executable": sys.executable,
               "python_executable_sha256": digest_file(Path(sys.executable).resolve()),
               "python_version": sys.version, "platform": platform.platform(),
               "producer_has_no_input_file_reads": True,
               "historical_sources_are_provenance_not_producer_runtime_inputs": True,
               "commands": [], "status": "IN_PROGRESS"}
    before = {}
    try:
        own = (PAPER / "verify.py", PAPER / "record_author.py")
        sources = [(path.relative_to(WORKSPACE).as_posix(), path) for path in own]
        sources += [(relative, WORKSPACE / relative) for relative in SOURCE_PATHS]
        for relative, path in sources:
            data = path.read_bytes()
            before[relative] = digest_bytes(data)
            exclusive_bytes(directory / "source_inputs" / relative, data)
        exclusive_text(directory / "INPUT_PINS.before.sha256", pins_text(before))
        snapshot = directory / "verify.py"
        exclusive_bytes(snapshot, (PAPER / "verify.py").read_bytes())
        if digest_file(snapshot) != before[(PAPER / "verify.py").relative_to(WORKSPACE).as_posix()]:
            raise RuntimeError("producer source changed during snapshot")
        canonical_path = PAPER / "CANONICAL.json"
        canonical_input = directory / "CANONICAL.input.json"
        if initial:
            if canonical_path.exists():
                raise FileExistsError("initial mode will not overwrite an existing CANONICAL.json")
        else:
            exclusive_bytes(canonical_input, canonical_path.read_bytes())
            receipt["canonical_input_sha256"] = digest_file(canonical_input)
        env = os.environ.copy()
        # Remove import-location overrides without printing their inherited values.
        env.pop("PYTHONPATH", None)
        env.pop("PYTHONHOME", None)
        env.update(SETTINGS)
        version = execute([sys.executable, "--version"], directory, "python_version", env)
        receipt["commands"].append(version)
        require_success(version)
        run_numbers = (0,) if initial else (1, 2)
        for number in run_numbers:
            run = execute([sys.executable, "-B", str(snapshot)], directory, f"run{number}", env)
            receipt["commands"].append(run)
            require_success(run)
            output_path = directory / f"run{number}.stdout"
            data = output_path.read_bytes()
            parsed = json.loads(data)
            if parsed.get("status") != "PASS" or not isinstance(parsed.get("assertions"), int):
                raise RuntimeError("producer did not emit its complete PASS JSON")
            if parsed["assertions"] <= 0 or sum(parsed["assertions_by_section"].values()) != parsed["assertions"]:
                raise RuntimeError("invalid assertion census")
            if run["stderr"]["bytes"] != 0:
                raise RuntimeError("unexpected producer stderr preserved for inspection")
            receipt.setdefault("numerical_outputs", []).append({
                "run": number, "assertions": parsed["assertions"],
                "ordered_checked_record_sha256": parsed["ordered_checked_record_sha256"],
                "output_sha256": digest_bytes(data), "output_bytes": len(data)})
            if initial:
                exclusive_bytes(canonical_path, data)
                exclusive_bytes(canonical_input, data)
                receipt["canonical_input_sha256"] = digest_bytes(data)
            comparison = execute(["cmp", str(output_path), str(canonical_input)],
                                 directory, f"run{number}.canonical.cmp", env)
            receipt["commands"].append(comparison)
            require_success(comparison)
        if not initial:
            comparison = execute(["cmp", str(directory / "run1.stdout"), str(directory / "run2.stdout")],
                                 directory, "pair.cmp", env)
            receipt["commands"].append(comparison)
            require_success(comparison)
        comparison = execute(["cmp", str(canonical_path), str(canonical_input)],
                             directory, "canonical_live.cmp", env)
        receipt["commands"].append(comparison)
        require_success(comparison)
        after = {relative: digest_file(path) for relative, path in sources}
        exclusive_text(directory / "INPUT_PINS.after.sha256", pins_text(after))
        receipt["input_pins"] = len(before)
        receipt["inputs_unchanged"] = before == after
        receipt["input_pin_mismatches"] = [p for p in before if before[p] != after.get(p)]
        if before != after:
            raise RuntimeError("a pinned scientific/provenance input changed during this attempt")
        if digest_file(snapshot) != before[(PAPER / "verify.py").relative_to(WORKSPACE).as_posix()]:
            raise RuntimeError("standalone snapshot changed during execution")
        receipt["status"] = "PASS"
    except BaseException as error:
        receipt["status"] = "FAIL"
        receipt["error"] = {"type": type(error).__name__, "message": str(error)}
        exclusive_text(directory / "recorder_exception.txt", traceback.format_exc())
    receipt["finished_utc"] = utc()
    save_json(directory / "RECEIPT.json", receipt)
    seal = manifest(directory)
    print(json.dumps({"status": receipt["status"], "receipt": str(directory / "RECEIPT.json"),
                      "manifest": seal, "numerical_outputs": receipt.get("numerical_outputs", [])},
                     sort_keys=True, indent=2))
    return 0 if receipt["status"] == "PASS" else 1


def seal_owned_scope():
    directory = PAPER / "author_replay"
    destination = directory / "OWNED_MANIFEST.sha256"
    paths = [PAPER / name for name in ("verify.py", "CANONICAL.json", "record_author.py", "AUTHOR_EXECUTION.md")]
    paths += [path for path in directory.rglob("*") if path.is_file() and path != destination]
    for path in paths:
        if not path.is_file():
            raise FileNotFoundError(path)
    pins = {path.relative_to(PAPER).as_posix(): digest_file(path) for path in paths}
    exclusive_text(destination, pins_text(pins))
    print(json.dumps({"status": "SEALED_OWNED_SCOPE_ONLY", "entries": len(pins),
                      "manifest": str(destination), "sha256": digest_file(destination),
                      "not_a_whole_paper_manifest": True}, sort_keys=True, indent=2))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", default="pair_01")
    parser.add_argument("--initial", action="store_true")
    parser.add_argument("--seal", action="store_true")
    args = parser.parse_args()
    if args.seal:
        if args.initial:
            parser.error("--seal and --initial are exclusive")
        return seal_owned_scope()
    return record_attempt(args.tag, args.initial)


if __name__ == "__main__":
    sys.exit(main())
