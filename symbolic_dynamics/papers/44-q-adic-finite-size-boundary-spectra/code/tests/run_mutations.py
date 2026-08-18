#!/usr/bin/env python3
"""Exception-total exact designated-consumer mutation harness."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def safe_root(root: Path) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe root")
    return root.resolve(strict=True)


def static_file(root: Path, relative: str) -> Path:
    cursor = root
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe static path")
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("static symlink")
    result = cursor.resolve(strict=True)
    if root not in result.parents or not result.is_file():
        raise ValueError("static containment")
    return result


def invoke(python: str, script: Path, identifier: str, cwd: Path,
           hostile: Path) -> tuple[int, bytes, bytes]:
    environment = {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONPATH": str(hostile),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    process = subprocess.run(
        [python, "-I", "-B", str(script), "--mutation", identifier],
        cwd=cwd, env=environment, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    return process.returncode, process.stdout, process.stderr


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--scratch", required=True)
    arguments = parser.parse_args()
    root = safe_root(Path(arguments.root))
    scratch = Path(arguments.scratch)
    if not scratch.is_absolute() or scratch.exists() or scratch.is_symlink():
        raise ValueError("scratch must be an absent absolute path")
    scratch.mkdir(parents=True)
    hostile = scratch / "hostile_modules"
    unrelated = scratch / "unrelated_cwd"
    hostile.mkdir()
    unrelated.mkdir()
    (hostile / "json.py").write_text("raise RuntimeError('hostile json imported')\n", encoding="ascii")
    (hostile / "sitecustomize.py").write_text("raise RuntimeError('hostile sitecustomize imported')\n", encoding="ascii")
    environment = {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONPATH": str(hostile),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    naive = subprocess.run([sys.executable, "-c", "import json"], cwd=unrelated,
                           env=environment, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, check=False)
    isolated = subprocess.run([sys.executable, "-I", "-B", "-c", "import json"],
                              cwd=unrelated, env=environment,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=False)
    if naive.returncode == 0 or isolated.returncode != 0:
        raise ValueError("hostile module-shadow control")
    registry_path = static_file(root, "contracts/MUTATION_REGISTRY.json")
    registry_raw = registry_path.read_bytes()
    registry = json.loads(registry_raw.decode("ascii"), object_pairs_hook=unique)
    if registry_raw != canonical(registry):
        raise ValueError("mutation registry is noncanonical")
    instances = registry["instances"]
    if len(instances) != registry["expected_instance_count"] \
            or len({row["instance_id"] for row in instances}) != len(instances) \
            or len({row["family_id"] for row in instances}) != registry["expected_family_count"]:
        raise ValueError("mutation registry counts")
    records = []
    all_pass = True
    invocation_count = 0
    for instance in instances:
        observed: dict[str, Any] = {}
        designated = instance["consumers"]
        if len(designated) != len(set(designated)):
            raise ValueError("duplicate consumer")
        for consumer in designated:
            invocation_count += 1
            script = static_file(root, registry["consumer_contract"][consumer])
            returncode, stdout, stderr = invoke(
                sys.executable, script, instance["instance_id"], unrelated, hostile)
            try:
                envelope = json.loads(stdout.decode("ascii"), object_pairs_hook=unique)
                canonical_ok = stdout == canonical(envelope)
                exact = canonical_ok \
                    and set(envelope) == {"payload", "schema", "status"} \
                    and envelope["schema"] == "paper44-mutation-rejection-v1" \
                    and envelope["status"] == "REJECT" \
                    and envelope["payload"]["consumer"] == consumer \
                    and envelope["payload"]["instance_id"] == instance["instance_id"] \
                    and envelope["payload"]["code"] == instance["expected_code"] \
                    and returncode == instance["expected_exit"] \
                    and not stderr
                observed[consumer] = {
                    "code": envelope.get("payload", {}).get("code"),
                    "envelope_canonical": canonical_ok,
                    "exit": returncode,
                    "outcome": "REJECT" if exact else "HARNESS_ERROR",
                }
            except Exception as error:  # exception-total envelope
                exact = False
                observed[consumer] = {
                    "code": "UNPARSEABLE_CONSUMER_ENVELOPE",
                    "envelope_canonical": False,
                    "exit": returncode,
                    "outcome": "HARNESS_ERROR",
                    "reason": type(error).__name__,
                }
            all_pass = all_pass and exact
        exact_key_set = list(observed) == designated and set(observed) == set(designated)
        instance_pass = exact_key_set and all(row["outcome"] == "REJECT" for row in observed.values())
        all_pass = all_pass and instance_pass
        records.append({
            "consumers": observed,
            "designated_consumers": designated,
            "domain": instance["domain"],
            "expected_code": instance["expected_code"],
            "family_id": instance["family_id"],
            "instance_id": instance["instance_id"],
            "status": "REJECTED_BY_EVERY_DESIGNATED_CONSUMER" if instance_pass else "SURVIVED",
        })
    if not all_pass:
        raise ValueError("one or more mutations survived")
    result = {
        "payload": {
            "consumer_invocation_count": invocation_count,
            "environment_control": "NAIVE_REJECTED_ISOLATED_PASSED",
            "family_count": len({row["family_id"] for row in instances}),
            "instance_count": len(instances),
            "records": records,
            "survivor_count": 0,
        },
        "schema": "paper44-mutation-results-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
