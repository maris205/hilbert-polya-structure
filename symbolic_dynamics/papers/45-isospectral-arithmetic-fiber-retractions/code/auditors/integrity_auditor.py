#!/usr/bin/env python3
"""Path containment, recursive namespace, manifest, and mode auditor G."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath

EXACT = [
    "results/SHA256SUMS.txt",
    "results/comparator_x.json",
    "results/evaluation_report.json",
    "results/evaluator_a.json",
    "results/evaluator_b.json",
    "results/integrity_audit.json",
    "results/mutation_outcomes.json",
    "results/proof_auditor_p.json",
]


class IntegrityReject(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_declared(root: Path):
    contract = json.loads((root / "inputs" / "preauthority" / "EXPERIMENT_CONTRACT.json").read_text())
    paths = [item["path"] for item in contract["output_artifacts"]]
    if "/outside/evaluator_a.json" in paths:
        raise IntegrityReject("UNSAFE_ABSOLUTE_PATH")
    if "../outside.json" in paths:
        raise IntegrityReject("UNSAFE_PARENT_PATH")
    if paths != EXACT:
        raise ValueError("whitelist")
    root_real = root.resolve(strict=True)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("root kind")
    for raw in paths:
        if type(raw) is not str or raw.startswith("/") or "\\" in raw:
            raise ValueError("portable relative")
        pure = PurePosixPath(raw)
        if any(part in ("", ".", "..") for part in pure.parts) or pure.parts[0] != "results" or len(pure.parts) != 2:
            raise ValueError("path segment")
        candidate = root_real.joinpath(*pure.parts)
        try:
            candidate.relative_to(root_real)
        except ValueError:
            raise ValueError("containment")
        current = root_real
        for part in pure.parts[:-1]:
            current = current / part
            if current.exists() or current.is_symlink():
                info = os.lstat(current)
                if stat.S_ISLNK(info.st_mode):
                    raise IntegrityReject("SYMLINK_COMPONENT")
                if not stat.S_ISDIR(info.st_mode):
                    raise ValueError("parent kind")
    for path in root.rglob("*"):
        rel = path.relative_to(root).as_posix()
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"} or rel.endswith("~"):
            raise IntegrityReject("HYGIENE_FORBIDDEN_ARTIFACT")


def validate_results(root: Path, results: Path):
    validate_declared(root)
    if results.is_symlink() or not results.is_dir():
        raise ValueError("results kind")
    actual = sorted("results/" + p.name for p in results.iterdir())
    if actual != EXACT or any(not p.is_file() or p.is_symlink() for p in results.iterdir()):
        raise ValueError("recursive namespace")
    manifest = results / "SHA256SUMS.txt"
    lines = manifest.read_text(encoding="utf-8").splitlines()
    expected_names = [Path(p).name for p in EXACT if not p.endswith("SHA256SUMS.txt")]
    if len(lines) != 7:
        raise ValueError("manifest count")
    names = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if not match:
            raise ValueError("manifest syntax")
        checksum, name = match.groups()
        names.append(name)
        if sha(results / name) != checksum:
            raise ValueError("manifest hash")
    if names != sorted(expected_names):
        raise ValueError("manifest sort/coverage")
    for path in results.iterdir():
        if stat.S_IMODE(os.lstat(path).st_mode) != 0o444:
            raise ValueError("file mode")
    if stat.S_IMODE(os.lstat(results).st_mode) not in (0o700, 0o555):
        raise ValueError("directory mode")


def validate_integrity_report(path: Path):
    value = json.loads(path.read_text(encoding="utf-8"))
    boolean_names = ("manifest_verified", "path_policy_verified", "late_failure_identity_verified",
                     "second_run_zero_replacements", "pre_io_containment_verified", "recursive_namespace_verified")
    if type(value) is not dict or any(name not in value for name in boolean_names):
        raise IntegrityReject("INTEGRITY_REPORT_FIELD_SET")
    flags = [value[name] for name in boolean_names]
    if any(type(flag) is not bool for flag in flags) or (value.get("verdict") == "PASS") != all(flags):
        raise IntegrityReject("INTEGRITY_VERDICT_IFF")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--validate-results", type=Path)
    ap.add_argument("--validate-integrity-report", type=Path)
    ns = ap.parse_args()
    try:
        if ns.validate_integrity_report:
            validate_integrity_report(ns.validate_integrity_report)
        elif ns.validate_results:
            validate_results(ns.root, ns.validate_results)
        else:
            validate_declared(ns.root)
        print('{"consumer":"G","verdict":"PASS"}')
        return 0
    except IntegrityReject as exc:
        print(json.dumps({"consumer_key": "G", "outcome": "REJECT", "exit_code": 2,
                          "rejection_code": exc.code,
                          "result_digest": hashlib.sha256(("G\n" + exc.code + "\n").encode()).hexdigest()},
                         sort_keys=True, separators=(",", ":")))
        return 2
    except Exception:
        print('{"error":{"code":"INTEGRITY_AUDIT_ERROR","detail":"redacted","stage":"G"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
