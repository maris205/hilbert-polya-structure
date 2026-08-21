#!/usr/bin/env python3
"""AST-level physical import-separation audit for the two science engines."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED = {"__future__", "argparse", "fractions", "itertools", "json", "math", "pathlib", "sys", "typing"}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def imports(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module.split(".")[0])
    return sorted(found)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    try:
        production = root / "code" / "engines" / "production.py"
        independent = root / "code" / "audit" / "independent_science.py"
        production_imports = imports(production)
        independent_imports = imports(independent)
        if set(production_imports) - ALLOWED or set(independent_imports) - ALLOWED:
            raise AssertionError("project-local or third-party import")
        if sha(production) == sha(independent):
            raise AssertionError("identical engines")
        output = {
            "payload": {
                "independent_imports": independent_imports,
                "independent_sha256": sha(independent),
                "no_project_local_imports": True,
                "production_imports": production_imports,
                "production_sha256": sha(production),
            },
            "schema": "stage0-independence-audit-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(canonical(output))
        return 0
    except (AssertionError, OSError, SyntaxError, ValueError):
        sys.stdout.buffer.write(canonical({"payload": {"code": "REJECT_ENGINE_INDEPENDENCE"}, "schema": "stage0-independence-audit-v1", "status": "REJECT"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
