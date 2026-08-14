#!/usr/bin/env python3
"""Audit physical separation of candidate generation and arithmetic labels."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path


EXPECTED_CORE_SHA256 = (
    "3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168"
)
BANNED_IDENTIFIERS = {
    "accepted_support",
    "classify",
    "evaluator_class",
    "evaluator_prime",
    "factor_integer",
    "is_prime",
    "mixed_composite",
    "prime_power",
    "prime_table",
    "riemann_zero",
    "target_zero",
    "zeta_zero",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identifier_hits(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found: set[str] = set()
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
            if lowered in BANNED_IDENTIFIERS:
                found.add(lowered)
    return sorted(found)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default="results")
    args = parser.parse_args()

    code_dir = Path(__file__).resolve().parent
    result_dir = Path(args.result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    candidate_paths = [
        code_dir / "cycle_quotient_core.py",
        code_dir / "source_generator.py",
    ]
    files = []
    all_hits: list[str] = []
    for path in candidate_paths:
        hits = identifier_hits(path)
        files.append({
            "path": path.name,
            "sha256": digest(path),
            "banned_identifier_hits": hits,
        })
        all_hits.extend(f"{path.name}:{hit}" for hit in hits)

    required_separate_files = [
        code_dir / "post_census_classifier.py",
        code_dir / "independent_evaluator.py",
    ]
    payload = {
        "candidate_id": "SD-C35",
        "certificate_type": "candidate_source_post_census_separation",
        "audit_method": "Python AST identifier audit; string literals ignored",
        "banned_identifiers": sorted(BANNED_IDENTIFIERS),
        "candidate_files": files,
        "banned_identifier_hits": all_hits,
        "core_bridge_sha256_expected": EXPECTED_CORE_SHA256,
        "core_bridge_sha256_actual": digest(candidate_paths[0]),
        "core_bridge_exact": digest(candidate_paths[0]) == EXPECTED_CORE_SHA256,
        "classifier_process": required_separate_files[0].name,
        "independent_evaluator_process": required_separate_files[1].name,
        "separate_process_files_exist": all(
            path.is_file() for path in required_separate_files
        ),
    }
    payload["pass"] = (
        not payload["banned_identifier_hits"]
        and payload["core_bridge_exact"]
        and payload["separate_process_files_exist"]
    )
    (result_dir / "source_separation_certificate.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "candidate_id": "SD-C35",
        "pass": payload["pass"],
        "source_files": len(candidate_paths),
    }, sort_keys=True))
    if not payload["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
