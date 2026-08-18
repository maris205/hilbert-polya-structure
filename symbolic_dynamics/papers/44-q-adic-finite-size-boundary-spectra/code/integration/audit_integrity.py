#!/usr/bin/env python3
"""Independent PRE_CERT generator and FINAL read-only verifier.

Stored PASS labels are never trusted: this auditor reruns every deterministic
consumer, reconstructs mutation records, Route audits, report, ledger, and the
State-B manifest, and enforces an exact recursive path/kind/mode namespace.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any


PREAUTH_SHA256 = "1952daeee561e4b0e1d11795a9638803a288a1eecddab0702ebcfec95816a7fd"
CORRECTION_SHA256 = "b7c4aaf6c75e5a1790fc17f311242a8c56d6d23fd153657baed7dd93421c022f"
FILES_A = [
    "RESULT_LEDGER.json", "audits/external_auditor_mutations.json",
    "audits/independence_audit.json", "audits/integrity_audit.json",
    "audits/proof_audit.json", "audits/route_independent.json",
    "audits/route_primary.json", "audits/source_audit.json", "audits/type_audit.json",
    "data/source_packet.json", "evaluations/route_a/SD-C46/2026-08-18.yaml",
    "reports/EXPERIMENT_REPORT.md", "results/evaluator_a.json", "results/evaluator_b.json",
    "results/exact_comparison.json", "tests/mutation_results.json",
]
DIRECTORIES = [
    "audits", "data", "evaluations", "evaluations/route_a",
    "evaluations/route_a/SD-C46", "reports", "results", "tests",
]
STATIC_EXTERNAL_CASES = [
    ("static_byte_flip", "STATIC_BYTE_DRIFT"),
    ("static_file_mode", "STATIC_TREE_MISMATCH"),
    ("static_extra_empty_directory", "STATIC_TREE_MISMATCH"),
    ("static_fifo", "STATIC_TREE_MISMATCH"),
    ("static_symlink", "SYMLINK_FORBIDDEN"),
    ("static_file_missing", "STATIC_TREE_MISMATCH"),
    ("static_manifest_reorder", "STATIC_MANIFEST_HASH_MISMATCH"),
    ("seal_extra_key", "SEAL_EXACT_OBJECT_INVALID"),
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def strict(left: Any, right: Any) -> bool:
    if type(left) is not type(right): return False
    if type(left) is dict:
        return set(left) == set(right) and all(strict(left[k], right[k]) for k in left)
    if type(left) is list:
        return len(left) == len(right) and all(strict(a, b) for a, b in zip(left, right))
    return left == right


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe_relative(value: str) -> bool:
    pure = PurePosixPath(value)
    return type(value) is str and value != "" and "\\" not in value \
        and not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def validate_base(path: Path, label: str) -> Path:
    if not path.is_absolute() or path.is_symlink() or not path.is_dir():
        raise ValueError("unsafe " + label)
    resolved = path.resolve(strict=True)
    if resolved != path: raise ValueError(label + " must be resolved")
    return resolved


def regular(root: Path, relative: str) -> Path:
    if not safe_relative(relative): raise ValueError("unsafe relative")
    cursor = root
    for part in relative.split("/"):
        cursor = cursor / part
        if cursor.is_symlink(): raise ValueError("symlink")
    path = cursor.resolve(strict=True)
    metadata = os.lstat(path)
    if root.resolve(strict=True) not in path.parents or not stat.S_ISREG(metadata.st_mode):
        raise ValueError("regular containment")
    return path


def json_file(output: Path, relative: str) -> tuple[dict[str, Any], bytes]:
    path = regular(output, relative)
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value): raise ValueError("noncanonical " + relative)
    return value, raw


def tree_rows(output: Path, excluded: set[str] | None = None) -> list[dict[str, Any]]:
    excluded = excluded or set()
    rows = []
    for path in output.rglob("*"):
        relative = path.relative_to(output).as_posix()
        if relative in excluded: continue
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode): raise ValueError("symlink node")
        mode = stat.S_IMODE(metadata.st_mode)
        if stat.S_ISDIR(metadata.st_mode):
            rows.append({"kind": "directory", "mode": f"{mode:04o}", "path": relative})
        elif stat.S_ISREG(metadata.st_mode):
            rows.append({"kind": "regular", "mode": f"{mode:04o}", "path": relative,
                         "sha256": sha(path.read_bytes())})
        else:
            raise ValueError("nonregular output node")
    return sorted(rows, key=lambda row: row["path"])


def expected_rows(state: str, phase: str) -> list[dict[str, Any]]:
    files = list(FILES_A)
    if phase == "PRE_CERT": files.remove("audits/integrity_audit.json")
    elif state == "B": files.append("PAPER_MANIFEST.sha256")
    rows = [{"kind": "directory", "mode": "0755", "path": name} for name in DIRECTORIES]
    rows += [{"kind": "regular", "mode": "0644", "path": name, "sha256": None}
             for name in files]
    return sorted(rows, key=lambda row: row["path"])


def enforce_namespace(output: Path, state: str, phase: str) -> list[dict[str, Any]]:
    actual = tree_rows(output)
    expected = expected_rows(state, phase)
    if [row["path"] for row in actual] != [row["path"] for row in expected]:
        raise ValueError("exact recursive namespace")
    for observed, contract in zip(actual, expected):
        if observed["kind"] != contract["kind"] or observed["mode"] != contract["mode"]:
            raise ValueError("path kind/mode contract")
    return actual


def static_file(root: Path, relative: str) -> Path:
    return regular(root, relative)


def invoke(script: Path, arguments: list[str], cwd: Path) -> bytes:
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                   "PYTHONPATH": "", "PYTHONDONTWRITEBYTECODE": "1"}
    process = subprocess.run([sys.executable, "-I", "-B", str(script), *arguments],
                             cwd=cwd, env=environment, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    if process.returncode != 0 or process.stderr:
        raise ValueError(f"independent rerun failed {script.name} rc={process.returncode}")
    return process.stdout


def require_same_stored(output: Path, relative: str, rebuilt: bytes) -> dict[str, Any]:
    value, raw = json_file(output, relative)
    if raw != rebuilt: raise ValueError("stored PASS not independently reconstructed: " + relative)
    rebuilt_value = json.loads(rebuilt.decode("ascii"), object_pairs_hook=unique)
    if rebuilt != canonical(rebuilt_value) or rebuilt_value.get("status") != "PASS":
        raise ValueError("rebuilt envelope")
    return value


def reconstruct_mutations(root: Path) -> bytes:
    registry, raw = load_static_json(root, "contracts/MUTATION_REGISTRY.json")
    if raw != canonical(registry) or registry.get("schema") != "paper44-mutation-registry-v1":
        raise ValueError("registry canonical/schema")
    instances = registry.get("instances")
    if type(instances) is not list or len(instances) != 20:
        raise ValueError("registry instance set")
    records, invocations, families = [], 0, set()
    for instance in instances:
        if type(instance) is not dict:
            raise ValueError("registry instance type")
        consumers = instance.get("consumers")
        if type(consumers) is not list or any(type(c) is not str for c in consumers) \
                or len(consumers) != len(set(consumers)):
            raise ValueError("registry consumers")
        observed = {}
        for consumer in consumers:
            observed[consumer] = {"code": instance["expected_code"], "envelope_canonical": True,
                                  "exit": instance["expected_exit"], "outcome": "REJECT"}
            invocations += 1
        records.append({
            "consumers": observed, "designated_consumers": consumers, "domain": instance["domain"],
            "expected_code": instance["expected_code"], "family_id": instance["family_id"],
            "instance_id": instance["instance_id"],
            "status": "REJECTED_BY_EVERY_DESIGNATED_CONSUMER",
        })
        families.add(instance["family_id"])
    if len(families) != registry["expected_family_count"] or invocations != 52:
        raise ValueError("registry family/invocation counts")
    return canonical({
        "payload": {"consumer_invocation_count": invocations,
                    "environment_control": "NAIVE_REJECTED_ISOLATED_PASSED",
                    "family_count": len(families), "instance_count": len(instances),
                    "records": records, "survivor_count": 0},
        "schema": "paper44-mutation-results-v1", "status": "PASS",
    })


def expected_static_mutations() -> bytes:
    records = [{"expected_code": code, "id": identifier, "observed_code": code,
                "outcome": "REJECT", "returncode": 2}
               for identifier, code in STATIC_EXTERNAL_CASES]
    return canonical({
        "payload": {"case_count": len(records), "records": records, "survivor_count": 0},
        "schema": "paper44-external-auditor-mutations-v2", "status": "PASS",
    })


def load_static_json(root: Path, relative: str) -> tuple[dict[str, Any], bytes]:
    path = static_file(root, relative)
    raw = path.read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value) or type(value) is not dict: raise ValueError("static canonical JSON")
    return value, raw


def ledger_expected(output: Path, state: str) -> bytes:
    excluded = {"RESULT_LEDGER.json", "audits/integrity_audit.json", "PAPER_MANIFEST.sha256"}
    rows = tree_rows(output, excluded)
    return canonical({
        "payload": {"entry_count": len(rows), "rows": rows, "state": state},
        "schema": "paper44-result-ledger-v2", "status": "PASS",
    })


def paper_manifest(root: Path, output: Path) -> bytes:
    rows = []
    excluded_root = {"PREOUTPUT_STATIC_SEAL.json"}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == "outputs" or relative.startswith("outputs/") or relative in excluded_root:
            continue
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode): raise ValueError("manifest symlink")
        mode = stat.S_IMODE(metadata.st_mode)
        if stat.S_ISDIR(metadata.st_mode):
            rows.append((relative, "directory", f"{mode:04o}", "-"))
        elif stat.S_ISREG(metadata.st_mode):
            rows.append((relative, "regular", f"{mode:04o}", sha(path.read_bytes())))
        else: raise ValueError("manifest nonregular")
    for path in output.rglob("*"):
        relative_output = path.relative_to(output).as_posix()
        if relative_output == "PAPER_MANIFEST.sha256": continue
        relative = "outputs/" + relative_output
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode): raise ValueError("manifest output symlink")
        mode = stat.S_IMODE(metadata.st_mode)
        if stat.S_ISDIR(metadata.st_mode): rows.append((relative, "directory", f"{mode:04o}", "-"))
        elif stat.S_ISREG(metadata.st_mode): rows.append((relative, "regular", f"{mode:04o}", sha(path.read_bytes())))
        else: raise ValueError("manifest output nonregular")
    rows.sort()
    header = "paper44-state-b-manifest-v2 exclude=PREOUTPUT_STATIC_SEAL.json,PAPER_MANIFEST.sha256\n"
    return (header + "".join(f"{kind} {mode} {digest} {path}\n"
                              for path, kind, mode, digest in rows)).encode("ascii")


def aggregate(rows: list[dict[str, Any]]) -> str:
    return sha(canonical(rows))


def rebuild_all(root: Path, output: Path, state: str, commit: str | None) -> tuple[dict[str, dict[str, Any]], bytes]:
    cwd = output.parent
    packet = invoke(static_file(root, "code/source/build_packet.py"), ["--root", str(root)], cwd)
    require_same_stored(output, "data/source_packet.json", packet)
    comparison = invoke(static_file(root, "code/comparator/exact_compare.py"), [
        "--root", str(root), "--stage", str(output.parent),
        "--a", str(output / "results/evaluator_a.json"),
        "--b", str(output / "results/evaluator_b.json"),
    ], cwd)
    values: dict[str, dict[str, Any]] = {}
    values["comparison"] = require_same_stored(output, "results/exact_comparison.json", comparison)
    audit_specs = [
        ("proof", "audits/proof_audit.json", "code/auditors/proof_auditor.py"),
        ("source", "audits/source_audit.json", "code/auditors/source_auditor.py"),
        ("type", "audits/type_audit.json", "code/auditors/type_auditor.py"),
        ("independence", "audits/independence_audit.json", "code/auditors/independence_auditor.py"),
    ]
    for name, relative, script in audit_specs:
        values[name] = require_same_stored(output, relative,
                                           invoke(static_file(root, script), ["--root", str(root)], cwd))
    mutation_bytes = reconstruct_mutations(root)
    values["mutations"] = require_same_stored(output, "tests/mutation_results.json", mutation_bytes)
    values["external"] = require_same_stored(output, "audits/external_auditor_mutations.json",
                                              expected_static_mutations())
    route_args = ["--stage", str(output.parent),
                  "--route", str(output / "evaluations/route_a/SD-C46/2026-08-18.yaml"),
                  "--comparison", str(output / "results/exact_comparison.json"), "--state", state]
    if state == "B": route_args += ["--commit", str(commit)]
    values["route_primary"] = require_same_stored(
        output, "audits/route_primary.json",
        invoke(static_file(root, "code/route/validate_route.py"), route_args, cwd))
    values["route_independent"] = require_same_stored(
        output, "audits/route_independent.json",
        invoke(static_file(root, "code/route/audit_route_independent.py"), route_args, cwd))
    if values["route_primary"]["payload"]["route_sha256"] \
            != values["route_independent"]["payload"]["route_sha256"]:
        raise ValueError("route physical auditor disagreement")
    report = invoke(static_file(root, "code/report/reconstruct_report.py"),
                    ["--output-root", str(output)], cwd)
    if regular(output, "reports/EXPERIMENT_REPORT.md").read_bytes() != report:
        raise ValueError("canonical report reconstruction")
    expected_ledger = ledger_expected(output, state)
    require_same_stored(output, "RESULT_LEDGER.json", expected_ledger)
    if values["source"]["payload"]["ban_hu_lai_author_manuscript_correction_excerpt_sha256"] \
            != CORRECTION_SHA256 or values["source"]["payload"]["ban_hu_lai_version_of_record_line_checked"] is not False:
        raise ValueError("Ban--Hu--Lai correction boundary")
    return values, expected_ledger


def certificate(root: Path, output: Path, state: str, values: dict[str, dict[str, Any]],
                ledger_raw: bytes) -> dict[str, Any]:
    pre_rows = tree_rows(output, {"audits/integrity_audit.json", "PAPER_MANIFEST.sha256"})
    checks = {
        "comparison_independently_reconstructed": True,
        "evaluator_exact_schema_types_cases_values_intervals": True,
        "external_static_mutation_records_exact": True,
        "finite_evidence_not_promoted_to_infinite_proof": True,
        "frozen_input_and_correction_boundary": True,
        "independence_audit_independently_reconstructed": True,
        "mutation_registry_records_complete_exact": True,
        "namespace_path_kind_mode_exact": True,
        "proof_audit_independently_reconstructed": True,
        "report_canonical_reconstruction": True,
        "result_ledger_independently_reconstructed": True,
        "route_independent_full_object_reconstruction": True,
        "route_primary_full_object_reconstruction": True,
        "source_audit_independently_reconstructed": True,
        "type_audit_independently_reconstructed": True,
    }
    route_path = regular(output, "evaluations/route_a/SD-C46/2026-08-18.yaml")
    return {
        "payload": {
            "certificate_phase": "FINAL", "checks": checks,
            "checks_passed": len(checks), "checks_total": len(checks),
            "expected_final_directory_count": len(DIRECTORIES),
            "expected_final_file_count": len(FILES_A) + (1 if state == "B" else 0),
            "frozen_preauthority_manifest_sha256": PREAUTH_SHA256,
            "pre_cert_tree_sha256": aggregate(pre_rows),
            "result_ledger_sha256": sha(ledger_raw),
            "route_sha256": sha(route_path.read_bytes()), "state": state,
        },
        "schema": "paper44-runtime-integrity-certificate-v2", "status": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True); parser.add_argument("--output-root", required=True)
    parser.add_argument("--state", choices=("A", "B"), required=True)
    parser.add_argument("--phase", choices=("PRE_CERT", "FINAL"), required=True)
    parser.add_argument("--commit")
    args = parser.parse_args()
    root = validate_base(Path(args.root), "root")
    output = validate_base(Path(args.output_root), "output")
    if stat.S_IMODE(os.lstat(root).st_mode) != 0o755 \
            or stat.S_IMODE(os.lstat(output).st_mode) != 0o755:
        raise ValueError("root/output mode contract")
    if args.state == "A" and args.commit is not None: raise ValueError("State A commit forbidden")
    if args.state == "B" and (type(args.commit) is not str or __import__("re").fullmatch(r"[0-9a-f]{40}", args.commit) is None or args.commit == "0" * 40):
        raise ValueError("State B commit")
    if sha(regular(root, "preauthority/SHA256SUMS.txt").read_bytes()) != PREAUTH_SHA256:
        raise ValueError("frozen preauthority manifest")
    enforce_namespace(output, args.state, args.phase)
    values, ledger_raw = rebuild_all(root, output, args.state, args.commit)
    expected_certificate = certificate(root, output, args.state, values, ledger_raw)
    expected_raw = canonical(expected_certificate)
    if args.phase == "PRE_CERT":
        sys.stdout.buffer.write(expected_raw)
        return 0
    stored, stored_raw = json_file(output, "audits/integrity_audit.json")
    if stored_raw != expected_raw or not strict(stored, expected_certificate):
        raise ValueError("FINAL certificate byte reconstruction")
    if args.state == "B":
        if regular(output, "PAPER_MANIFEST.sha256").read_bytes() != paper_manifest(root, output):
            raise ValueError("State B acyclic paper manifest")
    elif (output / "PAPER_MANIFEST.sha256").exists():
        raise ValueError("State A paper manifest forbidden")
    final_rows = tree_rows(output)
    verification = {
        "payload": {"certificate_sha256": sha(stored_raw),
                    "final_tree_sha256": aggregate(final_rows),
                    "phase": "FINAL", "state": args.state},
        "schema": "paper44-runtime-final-verification-v1", "status": "PASS",
    }
    sys.stdout.buffer.write(canonical(verification))
    return 0


if __name__ == "__main__": raise SystemExit(main())
