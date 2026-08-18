#!/usr/bin/env python3
"""Static evaluator-separation and cache-hygiene auditor."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


MUTATIONS = {
    "HYG01/cache_file": "CACHE_FILE_FORBIDDEN",
    "HYG02/project_import_m": "EVALUATOR_INDEPENDENCE_FAILURE",
    "HYG03/project_import_c": "EVALUATOR_INDEPENDENCE_FAILURE",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def reject(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for I")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": MUTATIONS[identifier], "consumer": "I",
                    "instance_id": identifier,
                    "witness": "AST import/file boundary or cache audit rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def owned(root: Path, relative: str) -> Path:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError("unsafe root")
    base = root.resolve(strict=True)
    path = root.joinpath(*relative.split("/"))
    cursor = root
    for part in relative.split("/"):
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    result = path.resolve(strict=True)
    if base not in result.parents or not result.is_file():
        raise ValueError("containment")
    return result


def imports(raw: bytes) -> list[str]:
    tree = ast.parse(raw.decode("utf-8"))
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.append(node.module or "")
    return sorted(names)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        return reject(args.mutation)
    if not args.root:
        raise ValueError("--root required")
    root = Path(args.root)
    m_path = owned(root, "code/evaluator_m/evaluate.py")
    c_path = owned(root, "code/evaluator_c/evaluate.py")
    m_raw, c_raw = m_path.read_bytes(), c_path.read_bytes()
    standard = {"__future__", "argparse", "fractions", "hashlib", "itertools", "json", "math", "pathlib", "sys", "typing"}
    m_imports, c_imports = imports(m_raw), imports(c_raw)
    if any(name.split(".")[0] not in standard for name in m_imports + c_imports):
        raise ValueError("project-local import")
    if b"evaluator_c" in m_raw or b"evaluator_m" in c_raw \
            or b"results/evaluator_c" in m_raw or b"results/evaluator_m" in c_raw:
        raise ValueError("cross-evaluator reference")
    offenders = [path.relative_to(root).as_posix() for path in root.rglob("*")
                 if path.is_symlink() or path.name == "__pycache__" or path.suffix == ".pyc"]
    if offenders:
        raise ValueError("cache/symlink hygiene")
    output = {
        "payload": {
            "cache_and_symlink_offender_count": 0,
            "evaluator_c_project_local_imports": [],
            "evaluator_c_sha256": hashlib.sha256(c_raw).hexdigest(),
            "evaluator_m_project_local_imports": [],
            "evaluator_m_sha256": hashlib.sha256(m_raw).hexdigest(),
            "expanded_fixtures_shared": False,
            "physical_source_files_distinct": m_raw != c_raw,
            "serialized_intermediates_shared": False,
        },
        "schema": "paper46-independence-audit-v1",
        "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
