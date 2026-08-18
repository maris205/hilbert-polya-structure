#!/usr/bin/env python3
"""Frozen external verifier for the static seal and optional FINAL output tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any


PREAUTH_SHA256 = "1952daeee561e4b0e1d11795a9638803a288a1eecddab0702ebcfec95816a7fd"
EXCLUDED = {"PREOUTPUT_STATIC_SEAL.json", "STATIC_TREE_MANIFEST.json"}
SEAL_KEYS = {
    "candidate_cache_count", "candidate_id", "candidate_output_count", "contract_hashes",
    "counts", "hash_domains", "input_map", "schema", "smoke_evidence", "static_manifest_sha256",
    "static_tree_entry_count", "status", "transaction_expectations",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    answer: dict[str, Any] = {}
    for key, value in pairs:
        if key in answer: raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


def strict(a: Any, b: Any) -> bool:
    if type(a) is not type(b): return False
    if type(a) is dict:
        return set(a) == set(b) and all(strict(a[k], b[k]) for k in a)
    if type(a) is list:
        return len(a) == len(b) and all(strict(x, y) for x, y in zip(a, b))
    return a == b


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe_relative(value: str) -> bool:
    pure = PurePosixPath(value)
    return type(value) is str and value != "" and "\\" not in value \
        and not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def emit(status: str, code: str, payload: dict[str, Any], exit_code: int) -> int:
    sys.stdout.buffer.write(canonical({"payload": {"code": code, **payload},
                                      "schema": "paper44-frozen-external-audit-v2",
                                      "status": status}))
    return exit_code


def load_canonical(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value): raise ValueError("noncanonical JSON")
    return value, raw


def actual_static_rows(root: Path) -> list[dict[str, Any]]:
    rows = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == "outputs" or relative.startswith("outputs/") or relative in EXCLUDED:
            continue
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode): raise RuntimeError("SYMLINK_FORBIDDEN:" + relative)
        mode = stat.S_IMODE(metadata.st_mode)
        if stat.S_ISDIR(metadata.st_mode):
            rows.append({"kind": "directory", "mode": f"{mode:04o}", "path": relative})
        elif stat.S_ISREG(metadata.st_mode):
            rows.append({"kind": "regular", "mode": f"{mode:04o}", "path": relative,
                         "sha256": sha(path.read_bytes())})
        else:
            raise RuntimeError("STATIC_TREE_MISMATCH:" + relative)
    return sorted(rows, key=lambda row: row["path"])


def expected_input_map(root: Path) -> list[dict[str, str]]:
    manifest = root / "preauthority/SHA256SUMS.txt"
    if sha(manifest.read_bytes()) != PREAUTH_SHA256: raise RuntimeError("PREAUTHORITY_MANIFEST_DRIFT")
    rows = []
    for line in manifest.read_text(encoding="ascii").splitlines():
        if len(line) < 67 or line[64:66] != "  " or not safe_relative(line[66:]):
            raise RuntimeError("PREAUTHORITY_MANIFEST_DRIFT")
        rows.append({"path": "preauthority/" + line[66:], "sha256": line[:64]})
    rows.append({"path": "preauthority/SHA256SUMS.txt", "sha256": PREAUTH_SHA256})
    return sorted(rows, key=lambda row: row["path"])


def hex64(value: Any) -> bool:
    return type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def seal_structure(root: Path, seal: dict[str, Any], manifest_raw: bytes,
                   manifest_rows: list[dict[str, Any]]) -> bool:
    if set(seal) != SEAL_KEYS or seal["schema"] != "paper44-preoutput-static-seal-v2" \
            or seal["status"] != "PREOUTPUT_STATIC_SEAL" or seal["candidate_id"] != "SD-C46" \
            or type(seal["candidate_output_count"]) is not int or seal["candidate_output_count"] != 0 \
            or type(seal["candidate_cache_count"]) is not int or seal["candidate_cache_count"] != 0 \
            or seal["static_tree_entry_count"] != len(manifest_rows) \
            or seal["static_manifest_sha256"] != sha(manifest_raw):
        return False
    if not strict(seal["input_map"], expected_input_map(root)): return False
    expected_domains = {
        "final_tree_sha256": "canonical_recursive_rows_strictly_below_outputs_only; PREOUTPUT_STATIC_SEAL.json_not_in_domain",
        "state_B_manifest_sha256": "PAPER_MANIFEST.sha256_bytes; PREOUTPUT_STATIC_SEAL.json_and_manifest_self_excluded",
        "static_manifest_sha256": "STATIC_TREE_MANIFEST.json_bytes; rows_exclude_manifest_self_PREOUTPUT_STATIC_SEAL.json_outputs",
        "survivor_mutation_result_sha256": "canonical_ephemeral_disposable_result_bytes; not_in_static_or_output_tree",
    }
    if not strict(seal["hash_domains"], expected_domains): return False
    contracts = seal["contract_hashes"]
    expected_contract_paths = {
        "case_registry_sha256": "contracts/CASE_REGISTRY.json",
        "integration_contract_sha256": "contracts/INTEGRATION_CONTRACT.json",
        "interval_certification_contract_sha256": "contracts/INTERVAL_CERTIFICATION_CONTRACT.json",
        "mutation_registry_sha256": "contracts/MUTATION_REGISTRY.json",
        "result_schema_sha256": "contracts/RESULT_SCHEMA.json",
    }
    if type(contracts) is not dict or set(contracts) != set(expected_contract_paths): return False
    for key, relative in expected_contract_paths.items():
        if contracts[key] != sha((root / relative).read_bytes()): return False
    counts = seal["counts"]
    count_keys = {"external_static_mutations", "finite_cases", "finite_rejected_scope_cases",
                  "finite_valid_cases", "frozen_input_objects", "gamma_intervals_per_evaluator",
                  "mutation_consumer_invocations", "mutation_families", "mutation_instances",
                  "state_A_final_directories", "state_A_final_files", "state_B_final_directories",
                  "state_B_final_files", "survivor_physical_mutations"}
    if type(counts) is not dict or set(counts) != count_keys \
            or any(type(value) is not int for value in counts.values()): return False
    fixed = {"external_static_mutations": 8, "finite_cases": 580,
             "finite_rejected_scope_cases": 32, "finite_valid_cases": 548,
             "frozen_input_objects": 18, "gamma_intervals_per_evaluator": 33,
             "mutation_consumer_invocations": 52, "mutation_families": 19,
             "mutation_instances": 20, "state_A_final_directories": 8,
             "state_A_final_files": 16, "state_B_final_directories": 8,
             "state_B_final_files": 17}
    if any(counts[key] != value for key, value in fixed.items()) \
            or counts["survivor_physical_mutations"] < 20: return False
    tx = seal["transaction_expectations"]
    expected_tx = {"first_success_atomic_rename_count": 1,
                   "forced_late_failure_exit": 86,
                   "forced_late_failure_physical_target_writes": 0,
                   "forced_late_failure_target_unchanged": True,
                   "second_success_physical_target_writes": 0}
    if not strict(tx, expected_tx): return False
    smoke = seal["smoke_evidence"]
    smoke_keys = {"first_success_atomic_rename_count", "first_success_physical_target_writes",
                  "forced_late_failure_target_unchanged", "hostile_normal_external_byte_equal",
                  "hostile_normal_runtime_byte_equal", "late_failure_physical_target_writes",
                  "second_success_physical_target_writes", "state_A_final_tree_sha256",
                  "state_B_final_tree_sha256", "state_B_manifest_entry_count",
                  "state_B_manifest_sha256", "survivor_mutation_result_sha256",
                  "survivor_mutations_rejected", "seal_byte_change_control", "status"}
    if type(smoke) is not dict or set(smoke) != smoke_keys: return False
    if smoke["status"] != "PASS_SUPERSEDING_DISPOSABLE_RELEASE_SMOKE" \
            or smoke["first_success_atomic_rename_count"] != 1 \
            or smoke["first_success_physical_target_writes"] != 16 \
            or smoke["forced_late_failure_target_unchanged"] is not True \
            or smoke["late_failure_physical_target_writes"] != 0 \
            or smoke["second_success_physical_target_writes"] != 0 \
            or smoke["hostile_normal_external_byte_equal"] is not True \
            or smoke["hostile_normal_runtime_byte_equal"] is not True \
            or smoke["survivor_mutations_rejected"] != counts["survivor_physical_mutations"]:
        return False
    for key in ("state_A_final_tree_sha256", "state_B_final_tree_sha256",
                "state_B_manifest_sha256", "survivor_mutation_result_sha256"):
        if not hex64(smoke[key]) or smoke[key] == "0" * 64: return False
    expected_control = {
        "after_output_tree_sha256": smoke["state_A_final_tree_sha256"],
        "auditor_disposition": "REJECT_SEAL_EXACT_OBJECT_INVALID",
        "before_output_tree_sha256": smoke["state_A_final_tree_sha256"],
        "changed_field": "smoke_evidence.hostile_normal_external_byte_equal",
        "output_tree_sha256_unchanged": True,
        "seal_sha256_changed": True,
    }
    if not strict(smoke["seal_byte_change_control"], expected_control): return False
    return type(smoke["state_B_manifest_entry_count"]) is int and smoke["state_B_manifest_entry_count"] > 0


def runtime_final(root: Path, outputs: Path) -> tuple[str, str, dict[str, Any]]:
    route_path = outputs / "evaluations/route_a/SD-C46/2026-08-18.yaml"
    route, _ = load_canonical(route_path)
    state = route.get("authority_integration", {}).get("state")
    if state not in ("A", "B"): raise RuntimeError("FINAL_RUNTIME_REJECT")
    command = [sys.executable, "-I", "-B", str(root / "code/integration/audit_integrity.py"),
               "--root", str(root), "--output-root", str(outputs), "--state", state,
               "--phase", "FINAL"]
    if state == "B": command += ["--commit", str(route.get("code_commit"))]
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": "",
                   "PYTHONDONTWRITEBYTECODE": "1"}
    process = subprocess.run(command, cwd=outputs.parent, env=environment,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if process.returncode != 0 or process.stderr: raise RuntimeError("FINAL_RUNTIME_REJECT")
    verification = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
    if process.stdout != canonical(verification) or verification.get("status") != "PASS" \
            or verification.get("schema") != "paper44-runtime-final-verification-v1":
        raise RuntimeError("FINAL_RUNTIME_REJECT")
    return state, sha(process.stdout), verification


def audit(root: Path) -> tuple[str, dict[str, Any]]:
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() \
            or root.resolve(strict=True) != root:
        return "UNSAFE_ROOT", {}
    try:
        if stat.S_IMODE(os.lstat(root).st_mode) != 0o755:
            return "STATIC_TREE_MISMATCH", {"path": "."}
        for path in root.rglob("*"):
            relative = path.relative_to(root).as_posix()
            metadata = os.lstat(path)
            if stat.S_ISLNK(metadata.st_mode): return "SYMLINK_FORBIDDEN", {"path": relative}
            if path.name == "__pycache__" or path.suffix == ".pyc": return "CACHE_FORBIDDEN", {"path": relative}
        seal_path, manifest_path = root / "PREOUTPUT_STATIC_SEAL.json", root / "STATIC_TREE_MANIFEST.json"
        if not seal_path.is_file() or not manifest_path.is_file(): return "SEAL_OR_MANIFEST_MISSING", {}
        for special in (seal_path, manifest_path):
            metadata = os.lstat(special)
            if not stat.S_ISREG(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) != 0o644:
                return "STATIC_TREE_MISMATCH", {"path": special.name}
        seal, seal_raw = load_canonical(seal_path)
        manifest, manifest_raw = load_canonical(manifest_path)
        if sha(manifest_raw) != seal.get("static_manifest_sha256"):
            return "STATIC_MANIFEST_HASH_MISMATCH", {}
        if set(manifest) != {"payload", "schema", "status"} \
                or manifest["schema"] != "paper44-static-tree-manifest-v2" \
                or manifest["status"] != "SEALED" \
                or set(manifest["payload"]) != {"entry_count", "excluded_paths", "rows"} \
                or manifest["payload"]["excluded_paths"] != ["PREOUTPUT_STATIC_SEAL.json", "STATIC_TREE_MANIFEST.json", "outputs"]:
            return "STATIC_MANIFEST_OBJECT_INVALID", {}
        rows = manifest["payload"]["rows"]
        if type(rows) is not list or manifest["payload"]["entry_count"] != len(rows) \
                or rows != sorted(rows, key=lambda row: row.get("path", "")):
            return "STATIC_MANIFEST_OBJECT_INVALID", {}
        actual = actual_static_rows(root)
        if [row.get("path") for row in rows] != [row.get("path") for row in actual]:
            return "STATIC_TREE_MISMATCH", {}
        for promised, observed in zip(rows, actual):
            if promised.get("kind") != observed.get("kind") \
                    or promised.get("mode") != observed.get("mode") \
                    or set(promised) != set(observed):
                return "STATIC_TREE_MISMATCH", {"path": observed.get("path")}
            if promised.get("kind") == "regular" \
                    and promised.get("sha256") != observed.get("sha256"):
                return "STATIC_BYTE_DRIFT", {"path": observed.get("path")}
        if not seal_structure(root, seal, manifest_raw, rows): return "SEAL_EXACT_OBJECT_INVALID", {}
        outputs = root / "outputs"
        if outputs.exists():
            if outputs.is_symlink() or not outputs.is_dir(): return "FINAL_RUNTIME_REJECT", {}
            if stat.S_IMODE(os.lstat(outputs).st_mode) != 0o755:
                return "FINAL_RUNTIME_REJECT", {}
            state, runtime_sha, verification = runtime_final(root, outputs)
            output_files = sum(1 for path in outputs.rglob("*") if path.is_file())
            smoke = seal["smoke_evidence"]
            if verification["payload"]["final_tree_sha256"] \
                    != smoke[f"state_{state}_final_tree_sha256"]:
                return "FINAL_RUNTIME_REJECT", {}
            if state == "B":
                paper = outputs / "PAPER_MANIFEST.sha256"
                if sha(paper.read_bytes()) != smoke["state_B_manifest_sha256"] \
                        or sum(1 for _ in paper.open("rb")) - 1 \
                        != smoke["state_B_manifest_entry_count"]:
                    return "FINAL_RUNTIME_REJECT", {}
            return "PASS", {"candidate_output_count_observed": output_files,
                            "final_state": state, "runtime_verification_sha256": runtime_sha,
                            "static_tree_entry_count": len(rows),
                            "static_manifest_sha256": sha(manifest_raw)}
        return "PASS", {"candidate_output_count_observed": 0, "final_state": "PREOUTPUT",
                        "runtime_verification_sha256": "NONE",
                        "static_tree_entry_count": len(rows),
                        "static_manifest_sha256": sha(manifest_raw)}
    except RuntimeError as error:
        text = str(error)
        code = text.split(":", 1)[0] if text else "AUDIT_EXCEPTION"
        return code, {}
    except Exception:
        return "AUDIT_EXCEPTION", {}


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", required=True)
    args = parser.parse_args()
    code, payload = audit(Path(args.root))
    return emit("PASS" if code == "PASS" else "REJECT", code, payload, 0 if code == "PASS" else 2)


if __name__ == "__main__": raise SystemExit(main())
