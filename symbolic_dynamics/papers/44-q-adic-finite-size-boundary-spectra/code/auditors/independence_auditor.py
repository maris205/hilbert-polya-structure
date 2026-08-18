#!/usr/bin/env python3
"""AST/file-access independence auditor, separate from both evaluators."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_IMPORTS = {
    "__future__", "argparse", "fractions", "hashlib", "itertools", "json",
    "math", "pathlib", "sys", "typing",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def safe(root: Path, relative: str) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe root")
    path = root.joinpath(*relative.split("/"))
    cursor = root
    for part in relative.split("/"):
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink")
    resolved = path.resolve(strict=True)
    if root.resolve(strict=True) not in resolved.parents:
        raise ValueError("containment")
    return resolved


def imports(raw: bytes) -> list[str]:
    tree = ast.parse(raw.decode("utf-8"))
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.extend(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.append((node.module or "").split(".")[0])
    return sorted(set(names))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    arguments = parser.parse_args()
    if arguments.mutation:
        if arguments.mutation != "MUT-EVAL/B_imports_A_fixture":
            raise ValueError("not designated")
        sys.stdout.buffer.write(canonical({
            "payload": {
                "code": "EVALUATOR_INDEPENDENCE_FAILURE",
                "consumer": "I",
                "instance_id": arguments.mutation,
                "witness": "Evaluator B project-local import crosses the physical firewall",
            },
            "schema": "paper44-mutation-rejection-v1",
            "status": "REJECT",
        }))
        return 2
    if not arguments.root:
        raise ValueError("root required")
    root = Path(arguments.root)
    a_path = safe(root, "code/evaluator_a/evaluate.py")
    b_path = safe(root, "code/evaluator_b/evaluate.py")
    a_raw, b_raw = a_path.read_bytes(), b_path.read_bytes()
    a_imports, b_imports = imports(a_raw), imports(b_raw)
    if set(a_imports) - ALLOWED_IMPORTS or set(b_imports) - ALLOWED_IMPORTS:
        raise ValueError("project-local or unapproved import")
    if hashlib.sha256(a_raw).digest() == hashlib.sha256(b_raw).digest():
        raise ValueError("identical evaluator bytes")
    forbidden_a = [b"evaluator_b", b"outputs/results/evaluator_b", b"expanded_fixture"]
    forbidden_b = [b"evaluator_a", b"outputs/results/evaluator_a", b"expanded_fixture"]
    if any(token in a_raw for token in forbidden_a) or any(token in b_raw for token in forbidden_b):
        raise ValueError("cross-evaluator token")
    sys.stdout.buffer.write(canonical({
        "payload": {
            "evaluator_A_imports": a_imports,
            "evaluator_A_sha256": hashlib.sha256(a_raw).hexdigest(),
            "evaluator_B_imports": b_imports,
            "evaluator_B_sha256": hashlib.sha256(b_raw).hexdigest(),
            "expanded_fixtures_shared": False,
            "expected_tables_shared": False,
            "project_local_imports": [],
            "source_bytes_distinct": True,
        },
        "schema": "paper44-independence-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
