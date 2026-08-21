#!/usr/bin/env python3
"""Exercise every locked mutation through both isolated science engines."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def unique_json(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate JSON key")
        return dict(pairs)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def consume(script: Path, root: Path, mutation_id: str, expected_code: str) -> dict[str, Any]:
    environment = {
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONPATH": "/hostile/stage0",
    }
    command = [sys.executable, "-I", "-B", str(script), "--root", str(root), "--state", "A", "--mutation", mutation_id]
    completed = subprocess.run(command, cwd="/", env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=60)
    if completed.returncode != 2 or completed.stderr:
        raise AssertionError("mutation consumer process")

    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate output key")
        return dict(pairs)

    envelope = json.loads(completed.stdout.decode("ascii"), object_pairs_hook=hook)
    expected = {"payload": {"code": expected_code}, "schema": "stage0-error-v1", "status": "REJECT"}
    if envelope != expected or canonical(envelope) != completed.stdout:
        raise AssertionError("mutation consumer rejection")
    return {
        "consumer": script.relative_to(root).as_posix(),
        "exit": completed.returncode,
        "observed_code": envelope["payload"]["code"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    try:
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            raise AssertionError("root")
        contract = unique_json(root / "contracts" / "PROJECT_CONTRACT.json")
        registry = unique_json(root / "contracts" / "MUTATION_REGISTRY.json")
        expected_schema = f"p{contract['paper_number']}-stage0-mutation-registry-v1"
        if registry.get("project_slug") != contract.get("project_slug") or registry.get("schema") != expected_schema:
            raise AssertionError("registry binding")
        engines = [root / "code" / "engines" / "production.py", root / "code" / "audit" / "independent_science.py"]
        records = []
        identifiers = set()
        for mutation in registry["mutations"]:
            if set(mutation) != {"expected_code", "id", "kind", "payload"} or type(mutation["payload"]) is not dict or not mutation["payload"]:
                raise AssertionError("mutation record shape")
            if mutation["id"] in identifiers:
                raise AssertionError("duplicate mutation id")
            identifiers.add(mutation["id"])
            consumers = [consume(engine, root, mutation["id"], mutation["expected_code"]) for engine in engines]
            records.append({
                "consumers": consumers,
                "expected_code": mutation["expected_code"],
                "id": mutation["id"],
                "kind": mutation["kind"],
            })
        output = {
            "payload": {
                "actual_science_consumer_count": len(engines),
                "mutation_count": len(records),
                "records": records,
            },
            "schema": "stage0-mutation-audit-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(canonical(output))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, UnicodeError, json.JSONDecodeError, subprocess.SubprocessError):
        sys.stdout.buffer.write(canonical({"payload": {"code": "REJECT_MUTATION_SURVIVOR"}, "schema": "stage0-mutation-audit-v1", "status": "REJECT"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
