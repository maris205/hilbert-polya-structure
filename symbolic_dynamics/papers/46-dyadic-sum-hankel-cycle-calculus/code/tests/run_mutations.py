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
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for key, value in pairs:
        if key in answer:
            raise ValueError("duplicate key")
        answer[key] = value
    return answer


def root_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute() or path.is_symlink() or not path.is_dir():
        raise ValueError("unsafe root")
    return path.resolve(strict=True)


def static_file(root: Path, relative: str) -> Path:
    cursor = root
    for component in relative.split("/"):
        if component in {"", ".", ".."}:
            raise ValueError("unsafe relative")
        cursor /= component
        if cursor.is_symlink():
            raise ValueError("static symlink")
    value = cursor.resolve(strict=True)
    if root not in value.parents or not value.is_file():
        raise ValueError("static containment")
    return value


def invoke(python: str, script: Path, identifier: str, cwd: Path,
           hostile: Path) -> tuple[int, bytes, bytes]:
    environment = {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONPATH": str(hostile),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    result = subprocess.run(
        [python, "-I", "-B", str(script), "--mutation", identifier],
        cwd=cwd, env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode, result.stdout, result.stderr


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--scratch", required=True)
    args = parser.parse_args()
    root = root_path(args.root)
    scratch = Path(args.scratch)
    if not scratch.is_absolute() or scratch.exists() or scratch.is_symlink():
        raise ValueError("scratch must be absent absolute path")
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
                              cwd=unrelated, env=environment, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=False)
    if naive.returncode == 0 or isolated.returncode != 0:
        raise ValueError("hostile module-shadow control")
    registry_path = static_file(root, "contracts/MUTATION_REGISTRY.json")
    raw = registry_path.read_bytes()
    registry = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(registry):
        raise ValueError("registry canonicalization")
    instances = registry["instances"]
    families = {entry["family_id"] for entry in instances}
    if len(instances) != registry["expected_instance_count"] \
            or len(families) != registry["expected_family_count"] \
            or len({entry["instance_id"] for entry in instances}) != len(instances):
        raise ValueError("registry counts")
    allowed = {"ACCEPT", "HARNESS_ERROR", "REJECT"}
    if set(registry["outcome_union"]) != allowed:
        raise ValueError("outcome union")
    records: list[dict[str, Any]] = []
    invocation_count = 0
    survivor_count = 0
    for instance in instances:
        designated = instance["consumers"]
        if type(designated) is not list or len(designated) != len(set(designated)) \
                or any(consumer not in registry["consumer_contract"] for consumer in designated):
            raise ValueError("consumer set")
        observed: dict[str, Any] = {}
        for consumer in designated:
            invocation_count += 1
            script = static_file(root, registry["consumer_contract"][consumer])
            returncode, stdout, stderr = invoke(sys.executable, script,
                                                instance["instance_id"], unrelated, hostile)
            outcome = "HARNESS_ERROR"
            code: Any = "UNPARSEABLE_CONSUMER_ENVELOPE"
            is_canonical = False
            try:
                envelope = json.loads(stdout.decode("ascii"), object_pairs_hook=unique)
                is_canonical = stdout == canonical(envelope)
                code = envelope.get("payload", {}).get("code")
                exact = is_canonical and set(envelope) == {"payload", "schema", "status"} \
                    and envelope["schema"] == "paper46-mutation-rejection-v1" \
                    and envelope["status"] == "REJECT" \
                    and set(envelope["payload"]) == {"code", "consumer", "instance_id", "witness"} \
                    and envelope["payload"]["consumer"] == consumer \
                    and envelope["payload"]["instance_id"] == instance["instance_id"] \
                    and code == instance["expected_code"] \
                    and returncode == instance["expected_exit"] and stderr == b""
                outcome = "REJECT" if exact else "HARNESS_ERROR"
            except Exception:
                exact = False
            observed[consumer] = {
                "code": code,
                "envelope_canonical": is_canonical,
                "exit": returncode,
                "outcome": outcome,
            }
        exact_consumers = list(observed) == designated and set(observed) == set(designated)
        passed = exact_consumers and all(item["outcome"] == "REJECT" for item in observed.values())
        if not passed:
            survivor_count += 1
        records.append({
            "consumers": observed,
            "designated_consumers": designated,
            "domain": instance["domain"],
            "expected_code": instance["expected_code"],
            "family_id": instance["family_id"],
            "instance_id": instance["instance_id"],
            "status": "REJECTED_BY_EVERY_DESIGNATED_CONSUMER" if passed else "SURVIVED",
        })
    if survivor_count:
        raise ValueError("mutation survivor")
    sys.stdout.buffer.write(canonical({
        "payload": {
            "consumer_invocation_count": invocation_count,
            "environment_control": "NAIVE_REJECTED_ISOLATED_PASSED",
            "family_count": len(families),
            "instance_count": len(instances),
            "outcome_union": ["ACCEPT", "HARNESS_ERROR", "REJECT"],
            "records": records,
            "survivor_count": 0,
        },
        "schema": "paper46-mutation-results-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
