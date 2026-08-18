#!/usr/bin/env python3
"""Physical source, import, seal, and embargo auditor I."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import sys
from pathlib import Path


class IndependenceReject(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


I_ATTACKS = [
    (("independence", "source_trees"), "shared_helper", "SHARED_PRODUCTION_SOURCE"),
    (("independence", "output_embargo"), False, "PRESEAL_OUTPUT_READ"),
    (("comparison", "tolerance"), "selected_after_outputs", "POSTHOC_TOLERANCE"),
    (("independence", "oracle_use"), True, "EVALUATOR_USED_AS_ORACLE"),
    (("independence", "expected_table_shared"), True, "SHARED_EXPECTED_TABLE"),
]


def independence_semantic_code(root: Path):
    contract = json.loads((root / "inputs/preauthority/EXPERIMENT_CONTRACT.json").read_text())
    baseline = contract.get("mutation_baseline")
    if type(baseline) is not dict:
        return "INDEPENDENCE_CONTRACT_SHAPE"
    for path, attacked, code in I_ATTACKS:
        node = baseline
        try:
            for part in path:
                node = node[part]
        except (KeyError, TypeError):
            return "INDEPENDENCE_CONTRACT_SHAPE"
        if type(node) is type(attacked) and node == attacked:
            return code
    return None

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest(root: Path, name: str):
    path = root / "code" / "manifests" / name
    if not path.is_file() or path.is_symlink():
        raise ValueError("source manifest absent")
    for line in path.read_text(encoding="utf-8").splitlines():
        checksum, rel = line.split("  ", 1)
        member = root / rel
        if not member.is_file() or member.is_symlink() or sha(member) != checksum:
            raise ValueError("source manifest mismatch")


def imported_names(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.add(node.module or "")
    return names


def audit(root: Path, allow_results: bool = False):
    semantic_code = independence_semantic_code(root)
    if semantic_code:
        raise IndependenceReject(semantic_code)
    a = root / "code" / "evaluator_a" / "evaluator_a.py"
    b = root / "code" / "evaluator_b" / "evaluator_b.py"
    p = root / "code" / "proof_auditor" / "proof_auditor_p.py"
    for item in (a, b, p):
        if item.is_symlink() or not item.is_file():
            raise ValueError("source kind")
    if len({sha(a), sha(b), sha(p)}) != 3:
        raise ValueError("source identity")
    forbidden_prefixes = ("code.", "evaluator_a", "evaluator_b", "proof_auditor")
    for lane, path in (("A", a), ("B", b), ("P", p)):
        imports = imported_names(path)
        if any(name.startswith(forbidden_prefixes) for name in imports):
            raise ValueError("cross-lane import:" + lane)
    a_text, b_text = a.read_text(), b.read_text()
    if "evaluator_b" in a_text or "evaluator_a" in b_text or "expected_table" in a_text or "expected_table" in b_text:
        raise ValueError("cross-lane token")
    if "numpy" not in a_text or "numpy" in b_text:
        raise ValueError("method family")
    if "matrix_record" not in a_text or "saturated_closed_fiber" not in b_text or "infinite_record" not in b_text:
        raise ValueError("method structure")
    for name in ("A_SOURCE.sha256", "B_SOURCE.sha256", "P_SOURCE.sha256", "AUDITOR_SOURCE.sha256"):
        verify_manifest(root, name)
    # Candidate itself must remain output-free at PRE_CERT.
    if (root / "results").exists() and not allow_results:
        raise ValueError("output embargo")
    if any("__pycache__" in p.parts or p.suffix in {".pyc", ".pyo"} for p in root.rglob("*")):
        raise ValueError("cache")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--allow-results", action="store_true")
    ns = ap.parse_args()
    try:
        audit(ns.root, ns.allow_results)
        print('{"consumer":"I","verdict":"PASS"}')
        return 0
    except IndependenceReject as exc:
        print(json.dumps({"consumer_key": "I", "outcome": "REJECT", "exit_code": 2,
                          "rejection_code": exc.code,
                          "result_digest": hashlib.sha256(("I\n" + exc.code + "\n").encode()).hexdigest()},
                         sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:
        print('{"error":{"code":"INDEPENDENCE_AUDIT_ERROR","detail":"redacted","stage":"I"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
