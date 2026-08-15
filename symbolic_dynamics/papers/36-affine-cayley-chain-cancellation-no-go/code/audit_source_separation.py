#!/usr/bin/env python3
"""Audit the physical source/evaluator firewall and prototype bridge."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path


SOURCE_CORE_SHA = "041b8a1ee487eddafb1a4e935a015eaedf44aff1c32c6d26443c5a05e6cf94bd"
EVALUATOR_SHA = "ee47e159adbee841e70cbceb49cf860c3f9329284a34cf3a6a878a7eb00060d1"
BANNED_SOURCE_IDENTIFIERS = {
    "accepted_support",
    "factor_integer",
    "is_prime",
    "prime_table",
    "riemann_zero",
    "route_b",
    "target_coefficient",
    "target_zero",
    "zeta_zero",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    values: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            values.update(item.name.split(".")[0] for item in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            values.add(node.module.split(".")[0])
    return values


def identifier_hits(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    values: set[str] = set()
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Name):
            names.append(node.id)
        elif isinstance(node, ast.Attribute):
            names.append(node.attr)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.append(node.name)
        elif isinstance(node, ast.arg):
            names.append(node.arg)
        for name in names:
            lowered = name.lower()
            if lowered in BANNED_SOURCE_IDENTIFIERS:
                values.add(lowered)
    return sorted(values)


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", required=True)
    arguments = parser.parse_args()
    code_dir = Path(__file__).resolve().parent
    result_dir = Path(arguments.result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)

    source_paths = [code_dir / "source_core.py", code_dir / "source_generator.py"]
    evaluator_paths = [
        code_dir / "independent_evaluator.py",
        code_dir / "evaluate_results.py",
    ]
    source_imports = {path.name: sorted(imports(path)) for path in source_paths}
    evaluator_imports = {path.name: sorted(imports(path)) for path in evaluator_paths}
    source_hits = {
        path.name: identifier_hits(path) for path in source_paths
    }
    source_forbidden_imports = sorted(
        name
        for values in source_imports.values()
        for name in values
        if name in {"independent_evaluator", "evaluate_results"}
    )
    evaluator_forbidden_imports = sorted(
        name
        for values in evaluator_imports.values()
        for name in values
        if name in {"source_core", "source_generator"}
    )
    checks = {
        "source_core_bridge_exact": digest(source_paths[0]) == SOURCE_CORE_SHA,
        "independent_evaluator_bridge_exact": digest(evaluator_paths[0])
        == EVALUATOR_SHA,
        "process_files_physically_distinct": len(
            {path.resolve() for path in source_paths + evaluator_paths}
        )
        == 4,
        "source_has_no_evaluator_import": not source_forbidden_imports,
        "evaluator_has_no_source_import": not evaluator_forbidden_imports,
        "source_has_no_banned_identifier": not any(source_hits.values()),
    }
    payload = {
        "schema": "SD-C38-source-separation-certificate-v1",
        "candidate_id": "SD-C38",
        "audit_method": "Python AST imports and identifiers; literals ignored",
        "source_files": [path.name for path in source_paths],
        "evaluator_files": [path.name for path in evaluator_paths],
        "source_imports": source_imports,
        "evaluator_imports": evaluator_imports,
        "source_identifier_hits": source_hits,
        "source_forbidden_imports": source_forbidden_imports,
        "evaluator_forbidden_imports": evaluator_forbidden_imports,
        "source_core_sha256": digest(source_paths[0]),
        "independent_evaluator_sha256": digest(evaluator_paths[0]),
        "checks": checks,
        "pass": all(checks.values()),
    }
    write_json(result_dir / "source_separation_certificate.json", payload)
    print(
        json.dumps(
            {
                "candidate_id": "SD-C38",
                "checks": len(checks),
                "pass": payload["pass"],
            },
            sort_keys=True,
        )
    )
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
