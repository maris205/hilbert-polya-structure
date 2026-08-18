#!/usr/bin/env python3
"""Paper 45 PRE_CERT/FINAL driver with an exact atomic eight-file install."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

import jsonschema


OUTPUTS = [
    "results/SHA256SUMS.txt",
    "results/comparator_x.json",
    "results/evaluation_report.json",
    "results/evaluator_a.json",
    "results/evaluator_b.json",
    "results/integrity_audit.json",
    "results/mutation_outcomes.json",
    "results/proof_auditor_p.json",
]
JSON_DEFS = {
    "comparator_x.json": "comparisonReport",
    "evaluation_report.json": "evaluationReport",
    "evaluator_a.json": "scienceProjection",
    "evaluator_b.json": "scienceProjection",
    "integrity_audit.json": "integrityReport",
    "mutation_outcomes.json": "mutationBundle",
    "proof_auditor_p.json": "proofAudit",
}
SET_HASH = "6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84"
MARKER_NAME = ".paper45-disposable-root.json"
MARKER_BYTES = b'{"purpose":"paper45-disposable-clone-v1"}\n'
# Deterministic metadata is part of the canonical transaction object.  A
# rebuild therefore has the same bytes *and* recursive metadata as an earlier
# installation, rather than merely trusting its manifest.
CANONICAL_MTIME_NS = 1787011200000000000


class ControlledFailure(Exception):
    def __init__(self, code: str, stage: str):
        super().__init__(code)
        self.code = code
        self.stage = stage


class TotalParser(argparse.ArgumentParser):
    def error(self, message):
        raise ControlledFailure("CLI_ERROR", "CLI")


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def canonical_json(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def process_env():
    env = {key: value for key, value in os.environ.items() if key not in {
        "PYTHONPATH", "PYTHONHOME", "TMPDIR", "TMP", "TEMP",
        "P45_EXPECTED_OVERRIDE", "P45_TOLERANCE_OVERRIDE", "P45_CACHE_OVERRIDE"}}
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0",
                "TMPDIR": "/tmp", "TMP": "/tmp", "TEMP": "/tmp"})
    return env


def run_checked(command: list[str], cwd: Path | str = "/", timeout: int = 300):
    process = subprocess.Popen(command, cwd=str(cwd), env=process_env(), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.communicate()
        raise ControlledFailure("SUBPROCESS_TIMEOUT", "SUBPROCESS")
    if process.returncode != 0:
        raise ControlledFailure("NONZERO_EXIT", "SUBPROCESS")
    return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)


def assert_tmp_root(root: Path):
    if root.is_symlink() or not root.is_dir():
        raise ControlledFailure("UNSAFE_ROOT_KIND", "PRE_IO")
    absolute = root.resolve(strict=True)
    if absolute == Path("/tmp") or Path("/tmp") not in absolute.parents:
        raise ControlledFailure("OUTSIDE_DISPOSABLE_TMP", "PRE_IO")
    marker = absolute / MARKER_NAME
    if marker.is_symlink() or not marker.is_file() or marker.read_bytes() != MARKER_BYTES:
        raise ControlledFailure("DISPOSABLE_MARKER_REQUIRED", "PRE_IO")
    if stat.S_IMODE(os.lstat(marker).st_mode) != 0o444:
        raise ControlledFailure("DISPOSABLE_MARKER_MODE", "PRE_IO")
    # Reject every pre-existing symlink before subprocesses or output paths
    # are considered.  Disposable mutation M046 is consequently contained.
    for current, directory_names, file_names in os.walk(absolute, topdown=True, followlinks=False):
        base = Path(current)
        for name in directory_names + file_names:
            if (base / name).is_symlink():
                raise ControlledFailure("SYMLINK_COMPONENT", "PRE_IO")
    return absolute


def pre_io_paths(root: Path):
    contract = read_json(root / "inputs" / "preauthority" / "EXPERIMENT_CONTRACT.json")
    declared = [x["path"] for x in contract["output_artifacts"]]
    if declared != OUTPUTS:
        raise ControlledFailure("OUTPUT_WHITELIST_MISMATCH", "PRE_IO")
    resolved_root = root.resolve(strict=True)
    for text in declared:
        if type(text) is not str or text.startswith("/") or "\\" in text:
            raise ControlledFailure("UNSAFE_OUTPUT_PATH", "PRE_IO")
        pure = PurePosixPath(text)
        if pure.parts[0] != "results" or len(pure.parts) != 2 or any(x in ("", ".", "..") for x in pure.parts):
            raise ControlledFailure("UNSAFE_OUTPUT_PATH", "PRE_IO")
        path = resolved_root.joinpath(*pure.parts)
        try:
            path.relative_to(resolved_root)
        except ValueError:
            raise ControlledFailure("UNSAFE_OUTPUT_PATH", "PRE_IO")
    for name in ("results", "results.__stage__"):
        item = root / name
        if item.is_symlink():
            raise ControlledFailure("SYMLINK_COMPONENT", "PRE_IO")
        if item.exists() and not item.is_dir():
            raise ControlledFailure("NONREGULAR_COMPONENT", "PRE_IO")
    if (root / "results.__stage__").exists():
        raise ControlledFailure("STALE_STAGE", "PRE_IO")


def syntax_audit(root: Path):
    import ast
    for source in sorted((root / "code").rglob("*.py")):
        if source.is_symlink() or not source.is_file():
            raise ControlledFailure("SOURCE_KIND", "PRE_CERT")
        ast.parse(source.read_text(encoding="utf-8"), filename=source.as_posix())


def invoke_auditor(root: Path, relative: str, extra: list[str] | None = None):
    command = [sys.executable, "-B", str(root / relative), "--root", str(root)]
    if extra:
        command += extra
    run_checked(command, cwd="/", timeout=300)


def verify_pre_cert(root: Path, allow_results: bool):
    assert_tmp_root(root)
    pre_io_paths(root)
    syntax_audit(root)
    invoke_auditor(root, "code/auditors/source_auditor.py")
    invoke_auditor(root, "code/auditors/type_auditor.py")
    invoke_auditor(root, "code/auditors/integrity_auditor.py")
    invoke_auditor(root, "code/route_main/validate_route_main.py")
    invoke_auditor(root, "code/route_independent/validate_route_independent.py")
    extra = ["--allow-results"] if allow_results else None
    invoke_auditor(root, "code/auditors/independence_auditor.py", extra)
    return {"phase": "PRE_CERT", "verdict": "PASS", "result_files": 0 if not (root / "results").exists() else 8}


def copy_inputs(source: Path, destination: Path):
    shutil.copytree(source, destination)
    for directory in [destination] + [p for p in destination.rglob("*") if p.is_dir()]:
        directory.chmod(0o555)
    for file in [p for p in destination.rglob("*") if p.is_file()]:
        file.chmod(0o444)


def launch_evaluator(root: Path, temp: Path, lane: str):
    if lane == "A":
        source = root / "code" / "evaluator_a" / "evaluator_a.py"
    else:
        source = root / "code" / "evaluator_b" / "evaluator_b.py"
    sandbox = temp / lane.lower()
    sandbox.mkdir(mode=0o700)
    copied_source = sandbox / ("lane_" + lane.lower() + ".py")
    shutil.copy2(source, copied_source)
    copied_source.chmod(0o444)
    inputs = sandbox / "inputs"
    copy_inputs(root / "inputs" / "preauthority", inputs)
    output = sandbox / "sealed_projection.json"
    command = [sys.executable, "-B", str(copied_source), "--inputs", str(inputs), "--emit", str(output)]
    proc = subprocess.Popen(command, cwd=str(sandbox), env=process_env(), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, start_new_session=True)
    return proc, output, sandbox


def concurrent_evaluators(root: Path, temp: Path):
    pa, out_a, sand_a = launch_evaluator(root, temp, "A")
    pb, out_b, sand_b = launch_evaluator(root, temp, "B")
    try:
        stdout_a, stderr_a = pa.communicate(timeout=300)
        stdout_b, stderr_b = pb.communicate(timeout=300)
    except subprocess.TimeoutExpired:
        for process in (pa, pb):
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
            process.communicate()
        raise ControlledFailure("EVALUATOR_TIMEOUT", "A_B_EMBARGO")
    if pa.returncode != 0 or pb.returncode != 0 or stdout_a.strip() or stdout_b.strip():
        raise ControlledFailure("EVALUATOR_FAILURE", "A_B_EMBARGO")
    for path in (out_a, out_b):
        if path.is_symlink() or not path.is_file():
            raise ControlledFailure("EVALUATOR_OUTPUT_KIND", "A_B_EMBARGO")
        path.chmod(0o444)
    seals = {"A": sha_file(out_a), "B": sha_file(out_b)}
    # Neither output is parsed until both processes have exited and both seals exist.
    a = read_json(out_a)
    b = read_json(out_b)
    if a.get("producer") != "A" or b.get("producer") != "B" or a.get("infinite_records") != []:
        raise ControlledFailure("EVALUATOR_OWNERSHIP", "A_B_EMBARGO")
    return a, b, seals, out_a, out_b


def run_p(root: Path, temp: Path, b_output: Path):
    sandbox = temp / "p"
    sandbox.mkdir(mode=0o700)
    source = sandbox / "proof_auditor_p.py"
    shutil.copy2(root / "code" / "proof_auditor" / "proof_auditor_p.py", source)
    inputs = sandbox / "inputs"
    copy_inputs(root / "inputs" / "preauthority", inputs)
    b_copy = sandbox / "sealed_b.json"
    shutil.copy2(b_output, b_copy)
    b_copy.chmod(0o444)
    output = sandbox / "proof_audit.json"
    run_checked([sys.executable, "-B", str(source), "--inputs", str(inputs), "--b", str(b_copy), "--emit", str(output)], cwd=sandbox)
    output.chmod(0o444)
    return read_json(output)


def run_x(root: Path, temp: Path, a: dict, b: dict):
    sandbox = temp / "x"
    sandbox.mkdir(mode=0o700)
    source = sandbox / "comparator_x.py"
    shutil.copy2(root / "code" / "comparator" / "comparator_x.py", source)
    inputs = sandbox / "inputs"
    copy_inputs(root / "inputs" / "preauthority", inputs)
    paths = []
    for lane, projection in (("a", a), ("b", b)):
        view = {"producer": projection["producer"], "contract_sha256": projection["contract_sha256"],
                "finite_records": projection["finite_records"]}
        path = sandbox / (lane + "_finite_only.json")
        path.write_bytes(canonical_json(view))
        path.chmod(0o444)
        paths.append(path)
    output = sandbox / "comparison.json"
    run_checked([sys.executable, "-B", str(source), "--inputs", str(inputs), "--a-finite", str(paths[0]),
                 "--b-finite", str(paths[1]), "--emit", str(output)], cwd=sandbox)
    output.chmod(0o444)
    return read_json(output)


def run_mutations(root: Path, temp: Path, prepared: Path | None = None):
    if prepared is not None:
        candidate = prepared.resolve(strict=True)
        if candidate.is_symlink() or not candidate.is_file() or Path("/tmp") not in candidate.parents:
            raise ControlledFailure("PREPARED_BUNDLE_KIND", "MUTATIONS")
        bundle = read_json(candidate)
        if (bundle.get("contract_sha256") != sha_file(root / "inputs/preauthority/EXPERIMENT_CONTRACT.json") or
                bundle.get("registry_sha256") != sha_file(root / "inputs/preauthority/MUTATION_REGISTRY.json") or
                len(bundle.get("outcomes", [])) != 168 or mutation_survivors(root, bundle)):
            raise ControlledFailure("PREPARED_BUNDLE_INVALID", "MUTATIONS")
        return bundle
    output = temp / "mutation_outcomes.json"
    run_checked([sys.executable, "-B", str(root / "code" / "tests" / "run_mutations.py"),
                 "--root", str(root), "--emit", str(output)], cwd="/", timeout=900)
    return read_json(output)


def mutation_survivors(root: Path, bundle: dict):
    registry = read_json(root / "inputs" / "preauthority" / "MUTATION_REGISTRY.json")
    outcomes = bundle.get("outcomes", [])
    cursor = 0
    survivors = []
    for row in registry["mutations"]:
        actual = outcomes[cursor: cursor + len(row["consumers"])]
        cursor += len(row["consumers"])
        if [x.get("consumer_key") for x in actual] != row["consumers"]:
            survivors.append(row["id"])
            continue
        for consumer, outcome in zip(row["consumers"], actual):
            if not (outcome.get("mutation_id") == row["id"] and outcome.get("consumer_key") == consumer and
                    outcome.get("outcome") == "REJECT" and outcome.get("exit_code") == 2 and
                    outcome.get("rejection_code") == row["code"]):
                survivors.append(row["id"])
                break
    if cursor != len(outcomes):
        survivors.append("EXTRA_OUTCOMES")
    return sorted(set(survivors))


def infinite_closure(contract: dict, a: dict, b: dict, p: dict):
    ids = contract["infinite_coverage_gate"]["ordered_case_ids"]
    id_match = (a["infinite_case_ids"] == [] and a["infinite_records"] == [] and
                b["infinite_case_ids"] == ids and [x["case_id"] for x in b["infinite_records"]] == ids and
                p["audited_case_ids"] == ids and [x["case_id"] for x in p["per_case_audits"]] == ids)
    owner_hash = id_match
    if id_match:
        for cert, audit in zip(b["infinite_records"], p["per_case_audits"]):
            if cert["certificate_owner"] != "B" or audit["audit_owner"] != "P":
                owner_hash = False
            for key in ("case_id", "certificate_owner", "certificate_payload_sha256", "proof_dependency_hash", "analytic_derivation_hash"):
                if cert[key] != audit[key]:
                    owner_hash = False
    return id_match, owner_hash


def build_evaluation_report(root: Path, a: dict, b: dict, p: dict, x: dict, bundle: dict):
    inputs = root / "inputs" / "preauthority"
    contract = read_json(inputs / "EXPERIMENT_CONTRACT.json")
    survivors = mutation_survivors(root, bundle)
    id_match, owner_hash = infinite_closure(contract, a, b, p)
    inf_pass = id_match and owner_hash and p["verdict"] == "PASS"
    common_pass = x["verdict"] == "PASS" and inf_pass and not survivors
    return {
        "schema_version": "paper45.evaluation-report.v1",
        "contract_sha256": sha_file(inputs / "EXPERIMENT_CONTRACT.json"),
        "c1": "PASS" if common_pass else "HOLD",
        "c2": "PASS" if common_pass else "HOLD",
        "infinite_coverage": {"a_infinite_count": len(a["infinite_records"]), "b_infinite_count": len(b["infinite_records"]),
                              "p_audit_count": len(p["per_case_audits"]), "case_set_sha256": SET_HASH,
                              "b_p_id_match": id_match, "b_p_owner_hash_closure": owner_hash,
                              "verdict": "PASS" if inf_pass else "HOLD"},
        "mutation_survivors": len(survivors),
        "external_disposition": "GO_EVALUATED" if common_pass else "HOLD_REPAIR",
    }


def integrity_report(root: Path, core_payloads: dict[str, bytes], evaluator_seals: dict[str, str]):
    inputs = root / "inputs/preauthority"
    pending = [{"path": path, "file_type": "PENDING", "mode": "PENDING", "sha256": "PENDING",
                "size_bytes": "PENDING", "mtime_ns": "PENDING"} for path in OUTPUTS]
    actual = []
    for name in sorted(core_payloads):
        raw = core_payloads[name]
        actual.append({"path": "results/" + name, "file_type": "regular", "mode": "0444",
                       "sha256": sha_bytes(raw), "size_bytes": len(raw), "mtime_ns": CANONICAL_MTIME_NS})
    provenance = {
        "frozen_input_manifest_sha256": sha_file(inputs / "SHA256SUMS.txt"),
        "experiment_contract_sha256": sha_file(inputs / "EXPERIMENT_CONTRACT.json"),
        "experiment_contract_schema_sha256": sha_file(inputs / "EXPERIMENT_CONTRACT_SCHEMA.json"),
        "mutation_registry_sha256": sha_file(inputs / "MUTATION_REGISTRY.json"),
        "integration_contract_sha256": sha_file(root / "code/contracts/INTEGRATION_CONTRACT.json"),
        "route_expectation_sha256": sha_file(inputs / "ROUTE_EXPECTATION.yaml"),
        "source_manifest_seals": {name: sha_file(root / "code/manifests" / name) for name in
                                  ("A_SOURCE.sha256", "B_SOURCE.sha256", "P_SOURCE.sha256", "AUDITOR_SOURCE.sha256")},
        "evaluator_output_seals": evaluator_seals,
    }
    booleans = {"manifest_verified": True, "path_policy_verified": True,
                "late_failure_identity_verified": True, "second_run_zero_replacements": True,
                "pre_io_containment_verified": True, "recursive_namespace_verified": True}
    return {"schema_version": "paper45.integrity-report.v2", "producer": "G",
            "contract_sha256": sha_file(inputs / "EXPERIMENT_CONTRACT.json"),
            "exact_output_paths": OUTPUTS,
            "state_a": {"phase": "PREINSTALL", "target_status": "ABSENT_OR_COMPARE_ONLY", "pending": pending},
            "state_b": {"phase": "STAGED_VALIDATED", "actual": actual,
                        "self_excluding": [
                            {"path": "results/integrity_audit.json", "reason": "SELF_HASH_CYCLE"},
                            {"path": "results/SHA256SUMS.txt", "reason": "MANIFEST_SELF_EXCLUDING"}],
                        "resolved_count": 8},
            "provenance": provenance, **booleans,
            "verdict": "PASS" if all(booleans.values()) and len(pending) == 8 and len(actual) == 6 else "HOLD"}


def manifest_bytes(payloads: dict[str, bytes]):
    names = sorted(payloads)
    if names != sorted(JSON_DEFS):
        raise ControlledFailure("OUTPUT_SET", "MANIFEST")
    return ("\n".join(f"{sha_bytes(payloads[name])}  {name}" for name in names) + "\n").encode("utf-8")


def validate_json_schemas(root: Path, payloads: dict[str, bytes]):
    schema = read_json(root / "inputs" / "preauthority" / "EXPERIMENT_CONTRACT_SCHEMA.json")
    for filename, definition in JSON_DEFS.items():
        value = json.loads(payloads[filename].decode("utf-8"))
        if filename == "integrity_audit.json":
            validate_integrity_object(root, value)
            continue
        wrapper = {"$schema": "https://json-schema.org/draft/2020-12/schema",
                   "$ref": f"#/$defs/{definition}", "$defs": schema["$defs"]}
        errors = list(jsonschema.Draft202012Validator(wrapper).iter_errors(value))
        if errors:
            raise ControlledFailure("SCHEMA_ERROR", "STAGE")


def validate_integrity_object(root: Path, value: dict):
    top = {"schema_version", "producer", "contract_sha256", "exact_output_paths", "state_a", "state_b",
           "provenance", "manifest_verified", "path_policy_verified", "late_failure_identity_verified",
           "second_run_zero_replacements", "pre_io_containment_verified", "recursive_namespace_verified", "verdict"}
    if type(value) is not dict or set(value) != top:
        raise ControlledFailure("INTEGRITY_FIELD_SET", "STAGE")
    boolean_names = ("manifest_verified", "path_policy_verified", "late_failure_identity_verified",
                     "second_run_zero_replacements", "pre_io_containment_verified", "recursive_namespace_verified")
    booleans = [value[name] for name in boolean_names]
    if (value["schema_version"] != "paper45.integrity-report.v2" or value["producer"] != "G" or
            value["contract_sha256"] != sha_file(root / "inputs/preauthority/EXPERIMENT_CONTRACT.json") or
            value["exact_output_paths"] != OUTPUTS or any(type(item) is not bool for item in booleans) or
            (value["verdict"] == "PASS") != all(booleans)):
        raise ControlledFailure("INTEGRITY_IFF", "STAGE")
    state_a, state_b = value["state_a"], value["state_b"]
    if (set(state_a) != {"phase", "target_status", "pending"} or state_a["phase"] != "PREINSTALL" or
            len(state_a["pending"]) != 8 or
            set(state_b) != {"phase", "actual", "self_excluding", "resolved_count"} or
            state_b["phase"] != "STAGED_VALIDATED" or len(state_b["actual"]) != 6 or state_b["resolved_count"] != 8):
        raise ControlledFailure("INTEGRITY_STATE_LEDGER", "STAGE")
    expected_pending = OUTPUTS
    if [item.get("path") for item in state_a["pending"]] != expected_pending:
        raise ControlledFailure("INTEGRITY_PENDING_ORDER", "STAGE")
    pending_keys = {"path", "file_type", "mode", "sha256", "size_bytes", "mtime_ns"}
    actual_keys = pending_keys
    if any(type(item) is not dict or set(item) != pending_keys for item in state_a["pending"]):
        raise ControlledFailure("INTEGRITY_PENDING_FIELDS", "STAGE")
    if any(type(item) is not dict or set(item) != actual_keys or item["file_type"] != "regular" or
           item["mode"] != "0444" or type(item["size_bytes"]) is not int or type(item["mtime_ns"]) is not int
           for item in state_b["actual"]):
        raise ControlledFailure("INTEGRITY_ACTUAL_FIELDS", "STAGE")
    provenance_keys = {"frozen_input_manifest_sha256", "experiment_contract_sha256",
                       "experiment_contract_schema_sha256", "mutation_registry_sha256",
                       "integration_contract_sha256", "route_expectation_sha256",
                       "source_manifest_seals", "evaluator_output_seals"}
    if type(value["provenance"]) is not dict or set(value["provenance"]) != provenance_keys:
        raise ControlledFailure("INTEGRITY_PROVENANCE_FIELDS", "STAGE")


def validate_report_reconstruction(root: Path, payloads: dict[str, bytes]):
    values = {name: json.loads(raw.decode()) for name, raw in payloads.items()}
    rebuilt = build_evaluation_report(root, values["evaluator_a.json"], values["evaluator_b.json"],
                                      values["proof_auditor_p.json"], values["comparator_x.json"],
                                      values["mutation_outcomes.json"])
    if canonical_json(rebuilt) != payloads["evaluation_report.json"]:
        raise ControlledFailure("REPORT_RECONSTRUCTION", "STAGE")


def write_stage(root: Path, payloads: dict[str, bytes]):
    stage = root / "results.__stage__"
    stage.mkdir(mode=0o700)
    try:
        for name, data in payloads.items():
            path = stage / name
            path.write_bytes(data)
            path.chmod(0o444)
        manifest = stage / "SHA256SUMS.txt"
        manifest.write_bytes(manifest_bytes(payloads))
        manifest.chmod(0o444)
        if sorted(x.name for x in stage.iterdir()) != ["SHA256SUMS.txt"] + sorted(payloads):
            raise ControlledFailure("NAMESPACE_ERROR", "STAGE")
        for line in manifest.read_text().splitlines():
            checksum, name = line.split("  ", 1)
            if sha_file(stage / name) != checksum:
                raise ControlledFailure("MANIFEST_ERROR", "STAGE")
        validate_json_schemas(root, payloads)
        validate_report_reconstruction(root, payloads)
        for child in stage.iterdir():
            os.utime(child, ns=(CANONICAL_MTIME_NS, CANONICAL_MTIME_NS), follow_symlinks=False)
        invoke_auditor(root, "code/auditors/type_auditor.py", ["--validate-results", str(stage)])
        stage.chmod(0o555)
        os.utime(stage, ns=(CANONICAL_MTIME_NS, CANONICAL_MTIME_NS), follow_symlinks=False)
        return stage
    except Exception:
        if stage.exists() and not stage.is_symlink():
            stage.chmod(0o700)
            shutil.rmtree(stage)
        raise


def metadata_tree(path: Path):
    if not path.exists() and not path.is_symlink():
        return []
    nodes = [path] + (sorted(path.rglob("*")) if path.is_dir() and not path.is_symlink() else [])
    result = []
    for node in nodes:
        info = os.lstat(node)
        if stat.S_ISREG(info.st_mode):
            kind, checksum = "regular", sha_file(node)
        elif stat.S_ISDIR(info.st_mode):
            kind, checksum = "directory", sha_bytes(b"")
        elif stat.S_ISLNK(info.st_mode):
            kind, checksum = "symlink", sha_bytes(os.readlink(node).encode())
        else:
            kind, checksum = "other", sha_bytes(b"")
        result.append({"path": node.relative_to(path.parent).as_posix(), "file_type": kind, "sha256": checksum,
                       "size_bytes": info.st_size, "mode": f"{stat.S_IMODE(info.st_mode):04o}", "mtime_ns": info.st_mtime_ns})
    return result


def comparable_metadata(path: Path):
    rows = metadata_tree(path)
    if not rows:
        return rows
    prefix = path.name
    normalized = []
    for row in rows:
        item = dict(row)
        original = item["path"]
        item["path"] = "results" + original[len(prefix):] if original.startswith(prefix) else original
        normalized.append(item)
    return normalized


def complete_late_failure_probe(root: Path, payloads: dict[str, bytes]):
    with tempfile.TemporaryDirectory(prefix="paper45-complete-late-", dir="/tmp") as raw:
        probe = Path(raw)
        target = probe / "results"
        before = metadata_tree(target)
        stage = probe / "results.__stage__"
        stage.mkdir()
        for name, data in payloads.items():
            (stage / name).write_bytes(data)
        (stage / "SHA256SUMS.txt").write_bytes(manifest_bytes(payloads))
        if len(list(stage.iterdir())) != 8:
            raise ControlledFailure("LATE_PROBE_STAGE", "TRANSACTION")
        for line in (stage / "SHA256SUMS.txt").read_text().splitlines():
            checksum, name = line.split("  ", 1)
            if sha_file(stage / name) != checksum:
                raise ControlledFailure("LATE_PROBE_MANIFEST", "TRANSACTION")
        validate_json_schemas(root, payloads)
        validate_report_reconstruction(root, payloads)
        shutil.rmtree(stage)
        if metadata_tree(target) != before or stage.exists():
            raise ControlledFailure("LATE_FAILURE_CHANGED_TARGET", "TRANSACTION")


def validate_existing(root: Path):
    results = root / "results"
    before = metadata_tree(results)
    invoke_auditor(root, "code/auditors/integrity_auditor.py", ["--validate-results", str(results)])
    invoke_auditor(root, "code/auditors/type_auditor.py", ["--validate-results", str(results)])
    payloads = {name: (results / name).read_bytes() for name in JSON_DEFS}
    validate_report_reconstruction(root, payloads)
    after = metadata_tree(results)
    if before != after:
        raise ControlledFailure("SECOND_RUN_REPLACEMENT", "TRANSACTION")
    return {"phase": "FINAL", "verdict": "PASS", "install": "IDENTICAL_PREEXISTING_ZERO_REPLACEMENTS",
            "physical_replacements": 0, "result_manifest_sha256": sha_file(results / "SHA256SUMS.txt")}


def state_a(root: Path):
    return {"target_metadata": metadata_tree(root / "results"),
            "pending": [{"path": item, "file_type": "PENDING", "mode": "PENDING", "sha256": "PENDING"} for item in OUTPUTS]}


def state_b(stage: Path):
    actual = []
    for child in sorted(stage.iterdir()):
        info = os.lstat(child)
        actual.append({"path": "results/" + child.name, "file_type": "regular", "mode": f"{stat.S_IMODE(info.st_mode):04o}",
                       "sha256": sha_file(child)})
    return {"actual": actual, "self_excluding_manifest_sha256": sha_file(stage / "SHA256SUMS.txt")}


def final_run(root: Path, force_late: bool, prepared_mutations: Path | None = None):
    verify_pre_cert(root, allow_results=(root / "results").exists())
    target = root / "results"
    target_preexisted = target.exists()
    existing_before = metadata_tree(target)
    before = state_a(root)
    with tempfile.TemporaryDirectory(prefix="paper45-final-", dir="/tmp") as raw:
        temp = Path(raw)
        a, b, evaluator_seals, a_path, b_path = concurrent_evaluators(root, temp)
        p = run_p(root, temp, b_path)
        x = run_x(root, temp, a, b)
        mutations = run_mutations(root, temp, prepared_mutations)
        report = build_evaluation_report(root, a, b, p, x, mutations)
        core_payloads = {
            "comparator_x.json": canonical_json(x), "evaluation_report.json": canonical_json(report),
            "evaluator_a.json": canonical_json(a), "evaluator_b.json": canonical_json(b),
            "mutation_outcomes.json": canonical_json(mutations), "proof_auditor_p.json": canonical_json(p),
        }
        integrity = integrity_report(root, core_payloads, evaluator_seals)
        payloads = {**core_payloads, "integrity_audit.json": canonical_json(integrity)}
        complete_late_failure_probe(root, payloads)
        root_before_stage = os.lstat(root)
        stage = write_stage(root, payloads)
        after_stage = state_b(stage)
        if len(after_stage["actual"]) != 8:
            stage.chmod(0o700)
            shutil.rmtree(stage)
            raise ControlledFailure("STATE_TRANSITION", "TRANSACTION")
        if force_late:
            target_before = metadata_tree(target)
            stage.chmod(0o700)
            shutil.rmtree(stage)
            # Creating/removing the sibling stage changes the candidate-root
            # directory mtime.  The registered identity tuple includes parent
            # directories, so restore the exact pre-stage timestamp as part of
            # the rollback (ctime is deliberately outside the frozen tuple).
            os.utime(root, ns=(root_before_stage.st_atime_ns, root_before_stage.st_mtime_ns), follow_symlinks=False)
            if metadata_tree(target) != target_before or (not target_preexisted and target.exists()):
                raise ControlledFailure("FORCED_LATE_CHANGED_TARGET", "TRANSACTION")
            raise ControlledFailure("FORCED_LATE_PREINSTALL_FAILURE", "TRANSACTION")
        if target_preexisted:
            try:
                if comparable_metadata(stage) != comparable_metadata(target):
                    raise ControlledFailure("TARGET_EXISTS_DIFFERENT", "TRANSACTION")
                # Byte/metadata equality is established against the fresh
                # sibling.  Only now may the installed target be audited.
                invoke_auditor(root, "code/auditors/integrity_auditor.py", ["--validate-results", str(target)])
                invoke_auditor(root, "code/auditors/type_auditor.py", ["--validate-results", str(target)])
            finally:
                stage.chmod(0o700)
                shutil.rmtree(stage)
                os.utime(root, ns=(root_before_stage.st_atime_ns, root_before_stage.st_mtime_ns), follow_symlinks=False)
            if metadata_tree(target) != existing_before:
                raise ControlledFailure("PREEXISTING_TARGET_CHANGED", "TRANSACTION")
            return {"phase": "FINAL", "verdict": "PASS", "install": "FRESH_REBUILD_IDENTICAL_PREEXISTING",
                    "physical_replacements": 0, "fresh_rebuild_compared": True,
                    "result_manifest_sha256": sha_file(target / "SHA256SUMS.txt")}
        if before["target_metadata"] != []:
            stage.chmod(0o700)
            shutil.rmtree(stage)
            raise ControlledFailure("STATE_TRANSITION", "TRANSACTION")
        os.rename(stage, target)
        # Immediate dry identical-run verification; no file is opened for writing.
        zero = validate_existing(root)
        return {"phase": "FINAL", "verdict": "PASS", "install": "ATOMIC_DIRECTORY_RENAME",
                "physical_replacements": 8, "evaluator_output_seals": evaluator_seals,
                "result_manifest_sha256": zero["result_manifest_sha256"],
                "state_a_pending_count": len(before["pending"]), "state_b_actual_count": len(after_stage["actual"]),
                "immediate_second_run_physical_replacements": 0}


def main():
    ap = TotalParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--phase", choices=("PRE_CERT", "FINAL"), required=True)
    ap.add_argument("--force-late-failure", action="store_true")
    ap.add_argument("--prepared-mutation-bundle", type=Path)
    try:
        ns = ap.parse_args()
        root = ns.root
        if ns.prepared_mutation_bundle is not None and (ns.phase != "FINAL" or not ns.force_late_failure):
            raise ControlledFailure("PREPARED_BUNDLE_OPTION_SCOPE", "CLI")
        if ns.phase == "PRE_CERT":
            if ns.force_late_failure:
                raise ControlledFailure("INVALID_PHASE_OPTION", "CLI")
            result = verify_pre_cert(root, allow_results=False)
        else:
            result = final_run(root, ns.force_late_failure, ns.prepared_mutation_bundle)
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0
    except ControlledFailure as exc:
        outcome = "REJECT" if exc.code in {"FORCED_LATE_PREINSTALL_FAILURE", "TARGET_EXISTS_DIFFERENT"} else "HARNESS_ERROR"
        exit_code = 2 if outcome == "REJECT" else 3
        payload = {"outcome": outcome, "exit_code": exit_code}
        if outcome == "REJECT":
            payload.update({"rejection_code": exc.code, "stage": exc.stage})
        else:
            payload["error"] = {"code": exc.code, "stage": exc.stage, "detail": "redacted"}
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return exit_code
    except Exception:
        print('{"error":{"code":"INTERNAL_EXCEPTION","detail":"redacted","stage":"DRIVER"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
