#!/usr/bin/env python3
"""Deterministic State-A orchestrator with a single outputs/ write domain."""

from __future__ import annotations

import sys

if not sys.flags.isolated or not sys.flags.dont_write_bytecode:
    sys.stdout.buffer.write(b'{\n  "payload": {\n    "code": "REJECT_INTEGRATION"\n  },\n  "schema": "stage0-integration-result-v1",\n  "status": "REJECT"\n}\n')
    raise SystemExit(2)

import argparse
import hashlib
import importlib.util
import json
import os
import stat
import subprocess
from pathlib import Path
from typing import Any


ANCHORS = ("STATIC_MANIFEST.json", "PREOUTPUT_SEAL.txt")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return list(sorted(left)) == list(sorted(right)) and all(strict_equal(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def parse_canonical(raw: bytes) -> dict[str, Any]:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate JSON key")
        return dict(pairs)
    value = json.loads(raw.decode("ascii"), object_pairs_hook=hook)
    if type(value) is not dict or set(value) != {"payload", "schema", "status"} or value["status"] != "PASS" or canonical(value) != raw:
        raise ValueError("noncanonical or failing envelope")
    return value


def isolated(script: Path, root: Path, extra: list[str]) -> tuple[bytes, dict[str, Any]]:
    environment = {
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONPATH": "/hostile/stage0",
    }
    command = [sys.executable, "-I", "-B", str(script), "--root", str(root), *extra]
    completed = subprocess.run(command, cwd="/", env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=300)
    if completed.returncode != 0 or completed.stderr:
        raise RuntimeError(f"consumer failed: {script.relative_to(root)}")
    return completed.stdout, parse_canonical(completed.stdout)


def sha_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def require_root(root: Path) -> None:
    if not root.is_absolute():
        raise ValueError("unsafe root path")
    metadata = os.lstat(root)
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise ValueError("unsafe root node")
    if root.resolve(strict=True) != root:
        raise ValueError("unsafe root resolution")


def require_anchor_nodes(root: Path) -> None:
    for name in ANCHORS:
        metadata = os.lstat(root / name)
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
            raise ValueError("unsafe excluded anchor")


def output_namespace_exists(root: Path) -> bool:
    outputs = root / "outputs"
    try:
        metadata = os.lstat(outputs)
    except FileNotFoundError:
        return False
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o755:
        raise ValueError("unsafe outputs root")
    if sorted(path.name for path in outputs.iterdir()) != ["state_A"]:
        raise ValueError("mixed output namespace")
    return True


def load_science_validator(root: Path) -> Any:
    path = root / "code" / "auditors" / "result_schema.py"
    specification = importlib.util.spec_from_file_location("stage0_result_schema", path)
    if specification is None or specification.loader is None:
        raise RuntimeError("result validator loader")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module.validate_science


def require_audit_shape(envelope: dict[str, Any], expected_schema: str, payload_keys: set[str]) -> None:
    if envelope["schema"] != expected_schema or type(envelope["payload"]) is not dict or set(envelope["payload"]) != payload_keys:
        raise RuntimeError("audit schema contract")


def build_artifacts(root: Path, rerun: bool) -> dict[str, bytes]:
    phase = "RERUN" if rerun else "PREOUTPUT"
    static_raw, static = isolated(root / "code" / "auditors" / "static_audit.py", root, ["--phase", phase])
    source_raw, source = isolated(root / "code" / "auditors" / "source_audit.py", root, [])
    independence_raw, independence = isolated(root / "code" / "auditors" / "independence_audit.py", root, [])
    type_raw, types = isolated(root / "code" / "auditors" / "type_audit.py", root, [])
    mutation_raw, mutations = isolated(root / "code" / "auditors" / "mutation_audit.py", root, [])
    audit_contracts = [
        (static, "stage0-static-audit-v1", {"manifest_entry_count", "manifest_sha256", "preoutput_seal_sha256", "project_slug"}),
        (source, "stage0-source-audit-v1", {"copied_input_entry_count", "frozen_manifests", "input_lock_sha256", "plan_status", "plan_review_receipt_path", "plan_review_receipt_sha256", "plan_review_sha256", "source_anchor_count"}),
        (independence, "stage0-independence-audit-v1", {"independent_imports", "independent_sha256", "no_project_local_imports", "production_imports", "production_sha256"}),
        (types, "stage0-type-audit-v1", {"case_count", "deep_result_schema_negative_controls", "expected_science_schema", "mutation_count", "route_id_assigned", "route_id_tree_scan_file_count", "scalar_nodes_checked", "science_schema_probes", "state_rejection_probes"}),
        (mutations, "stage0-mutation-audit-v1", {"actual_science_consumer_count", "mutation_count", "records"}),
    ]
    for audit, expected_schema, payload_keys in audit_contracts:
        require_audit_shape(audit, expected_schema, payload_keys)
    production_raw, production = isolated(root / "code" / "engines" / "production.py", root, ["--state", "A"])
    independent_raw, independent = isolated(root / "code" / "audit" / "independent_science.py", root, ["--state", "A"])
    if not strict_equal(production, independent) or production_raw != independent_raw:
        raise RuntimeError("exact science engines disagree")
    contract = json.loads((root / "contracts" / "PROJECT_CONTRACT.json").read_text(encoding="ascii"))
    result_schema = json.loads((root / "contracts" / "RESULT_SCHEMA.json").read_text(encoding="ascii"))
    cases_spec = json.loads((root / "contracts" / "STATE_A_CASES.json").read_text(encoding="ascii"))
    if production["schema"] != result_schema["science_schema"] or independent["schema"] != result_schema["science_schema"]:
        raise RuntimeError("science schema mismatch")
    if result_schema["science_schema"] != f"p{contract['paper_number']}-stage0-science-v1":
        raise RuntimeError("result schema is not bound to this paper")
    if production["payload"]["project_slug"] != contract["project_slug"] or production["payload"]["evidence_class"] != "FINITE_EXACT_FALSIFICATION_ONLY":
        raise RuntimeError("science contract mismatch")
    validator = load_science_validator(root)
    production_nodes = validator(result_schema, contract, cases_spec, production)
    independent_nodes = validator(result_schema, contract, cases_spec, independent)
    comparison = canonical({
        "payload": {
            "canonical_bytes_equal": True,
            "exact_audit_contract_count": len(audit_contracts),
            "case_count": len(production["payload"]["cases"]),
            "evidence_class": "FINITE_EXACT_FALSIFICATION_ONLY",
            "recursive_runtime_types_equal": True,
            "result_schema_runtime_nodes": production_nodes,
            "science_sha256": sha_bytes(production_raw),
        },
        "schema": "stage0-exact-comparison-v1",
        "status": "PASS",
    })
    artifacts = {
        "audits/independence_audit.json": independence_raw,
        "audits/mutation_audit.json": mutation_raw,
        "audits/source_audit.json": source_raw,
        "audits/static_audit.json": static_raw,
        "audits/type_audit.json": type_raw,
        "results/exact_comparison.json": comparison,
        "results/independent.json": independent_raw,
        "results/production.json": production_raw,
    }
    if production_nodes != independent_nodes or any(value["status"] != "PASS" for value in (static, source, independence, types, mutations)):
        raise RuntimeError("audit status")
    summary_rows = [{"path": path, "sha256": sha_bytes(payload), "size": len(payload)} for path, payload in sorted(artifacts.items())]
    artifacts["RUN_SUMMARY.json"] = canonical({
        "payload": {
            "artifact_count_excluding_summary": len(summary_rows),
            "artifacts": summary_rows,
            "evidence_class": "FINITE_EXACT_FALSIFICATION_ONLY",
            "project_slug": contract["project_slug"],
            "state": "A",
        },
        "schema": "stage0-run-summary-v1",
        "status": "PASS",
    })
    return artifacts


def safe_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o755)
    os.chmod(path.parent, 0o755)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o644)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        try:
            os.close(descriptor)
        except OSError:
            pass
        raise
    os.chmod(path, 0o644)


def install(root: Path, artifacts: dict[str, bytes]) -> int:
    outputs = root / "outputs"
    outputs.mkdir(mode=0o755)
    os.chmod(outputs, 0o755)
    stage = outputs / ".state_A.stage"
    stage.mkdir(mode=0o755)
    writes = 0
    for relative, payload in sorted(artifacts.items()):
        safe_write(stage / relative, payload)
        writes += 1
    final = outputs / "state_A"
    os.rename(stage, final)
    return writes


def verify_installed(root: Path, artifacts: dict[str, bytes]) -> None:
    final = root / "outputs" / "state_A"
    actual_files = sorted(path.relative_to(final).as_posix() for path in final.rglob("*") if path.is_file() and not path.is_symlink())
    if actual_files != sorted(artifacts):
        raise RuntimeError("installed file set mismatch")
    expected_directories = set()
    for relative in artifacts:
        parent = Path(relative).parent
        while parent.as_posix() != ".":
            expected_directories.add(parent.as_posix())
            parent = parent.parent
    actual_directories = sorted(path.relative_to(final).as_posix() for path in final.rglob("*") if path.is_dir() and not path.is_symlink())
    if actual_directories != sorted(expected_directories):
        raise RuntimeError("installed directory set mismatch")
    for path in final.rglob("*"):
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode) or (not stat.S_ISDIR(metadata.st_mode) and not stat.S_ISREG(metadata.st_mode)):
            raise RuntimeError("installed node type")
        expected_mode = 0o755 if stat.S_ISDIR(metadata.st_mode) else 0o644
        if stat.S_IMODE(metadata.st_mode) != expected_mode:
            raise RuntimeError("installed mode")
    for relative, payload in artifacts.items():
        if (final / relative).read_bytes() != payload:
            raise RuntimeError("installed byte mismatch")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--state", required=True)
    args = parser.parse_args()
    try:
        root = Path(args.root)
        if args.state != "A":
            raise ValueError("only State A exists")
        require_root(root)
        require_anchor_nodes(root)
        rerun = output_namespace_exists(root)
        artifacts = build_artifacts(root, rerun)
        if rerun:
            verify_installed(root, artifacts)
            writes = 0
        else:
            writes = install(root, artifacts)
            verify_installed(root, artifacts)
        output = {"payload": {"artifact_count": len(artifacts), "idempotent_replay": rerun, "physical_target_file_writes": writes, "state": "A"}, "schema": "stage0-integration-result-v1", "status": "PASS"}
        sys.stdout.buffer.write(canonical(output))
        return 0
    except (AssertionError, KeyError, OSError, RuntimeError, TypeError, ValueError, json.JSONDecodeError, subprocess.SubprocessError):
        sys.stdout.buffer.write(canonical({"payload": {"code": "REJECT_INTEGRATION"}, "schema": "stage0-integration-result-v1", "status": "REJECT"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
