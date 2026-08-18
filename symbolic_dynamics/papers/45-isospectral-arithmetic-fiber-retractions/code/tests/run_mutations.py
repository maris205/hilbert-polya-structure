#!/usr/bin/env python3
"""Execute the frozen 75-row suite as physical, disposable mutations.

Only this harness reads the immutable mutation catalogue.  Consumers receive
ordinary input/output paths and derive diagnostics from the malformed
artifact; no mutation identifier or expected code is passed to them.
"""

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
from pathlib import Path

import yaml


CONSUMERS = {
    "A": "code/evaluator_a/evaluator_a.py", "B": "code/evaluator_b/evaluator_b.py",
    "P": "code/proof_auditor/proof_auditor_p.py", "X": "code/comparator/comparator_x.py",
    "T": "code/auditors/type_auditor.py", "S": "code/auditors/source_auditor.py",
    "I": "code/auditors/independence_auditor.py", "G": "code/auditors/integrity_auditor.py",
    "R_MAIN": "code/route_main/validate_route_main.py",
    "R_INDEPENDENT": "code/route_independent/validate_route_independent.py",
}
MARKER_NAME = ".paper45-disposable-root.json"
MARKER_BYTES = b'{"purpose":"paper45-disposable-clone-v1"}\n'


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def safe_environment():
    result = {key: value for key, value in os.environ.items()
              if key not in {"PYTHONPATH", "PYTHONHOME", "TMPDIR", "TMP", "TEMP",
                             "P45_EXPECTED_OVERRIDE", "P45_TOLERANCE_OVERRIDE", "P45_CACHE_OVERRIDE"}}
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "TMPDIR": "/tmp", "TMP": "/tmp", "TEMP": "/tmp"})
    return result


def run_total(command: list[str], timeout: int = 300):
    process = subprocess.Popen(command, cwd="/", env=safe_environment(), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        stdout, stderr = process.communicate()
        raise RuntimeError("consumer timeout")
    return process.returncode, stdout, stderr


def strict_equal(left, right):
    return type(left) is type(right) and left == right


def resolve_parent(document, pointer: str):
    pieces = [item.replace("~1", "/").replace("~0", "~") for item in pointer[1:].split("/")]
    node = document
    for piece in pieces[:-1]:
        node = node[int(piece)] if type(node) is list else node[piece]
    return node, pieces[-1]


def replace_pointer(document, pointer: str, old, new):
    parent, tail = resolve_parent(document, pointer)
    current = parent[int(tail)] if type(parent) is list else parent[tail]
    if not strict_equal(current, old):
        raise RuntimeError("physical mutation precondition")
    if type(parent) is list:
        parent[int(tail)] = new
    else:
        parent[tail] = new


def copy_candidate(source: Path, destination: Path):
    def ignore(_directory, names):
        return {name for name in names if name in {"results", "results.__stage__", "__pycache__", MARKER_NAME}
                or name.endswith((".pyc", ".pyo"))}
    shutil.copytree(source, destination, symlinks=True, ignore=ignore)
    marker = destination / MARKER_NAME
    marker.write_bytes(MARKER_BYTES)
    marker.chmod(0o444)


def mutate_route(clone: Path, mid: str):
    route = clone / "inputs/preauthority/ROUTE_EXPECTATION.yaml"
    document = yaml.safe_load(route.read_text(encoding="utf-8"))
    if mid == "M043":
        document["evaluation_state"] = "EVALUATED"
    elif mid == "M049":
        document["branch_status"] = "GO_EVALUATED"
        document["overall_expectation"] = "GO_EVALUATED"
    else:
        return
    route.chmod(0o644)
    route.write_text(yaml.safe_dump(document, sort_keys=False, allow_unicode=True), encoding="utf-8")
    route.chmod(0o444)


def apply_physical_mutation(clone: Path, row: dict, outer: Path):
    operation = row["operation"]
    kind = operation["kind"]
    if kind == "replace_json_pointer":
        target = clone / "inputs" / "preauthority" / operation["target_artifact"]
        document = load(target)
        replace_pointer(document, operation["pointer"], operation["value_from"], operation["value_to"])
        target.chmod(0o644)
        target.write_bytes(canonical(document))
        target.chmod(0o444)
        mutate_route(clone, row["id"])
    elif kind == "filesystem_symlink_swap":
        target = clone / operation["path"]
        if target.exists() or target.is_symlink():
            raise RuntimeError("symlink precondition")
        sentinel = outer / "external-sentinel"
        sentinel.mkdir(exist_ok=True)
        target.symlink_to(sentinel, target_is_directory=True)
    elif kind == "filesystem_create_forbidden_artifact":
        target = clone / operation["path"]
        if target.exists() or target.is_symlink():
            raise RuntimeError("forbidden artifact precondition")
        target.parent.mkdir(parents=True)
        target.write_text(operation["content_utf8"], encoding="utf-8")
    elif kind == "force_late_failure":
        # The mutation is the production driver's real pre-install exception;
        # no synthetic stage or target is created here.
        return
    else:
        raise RuntimeError("unsupported physical operation")


def build_baseline(root: Path, workspace: Path):
    inputs = root / "inputs/preauthority"
    a_path, b_path = workspace / "baseline-a.json", workspace / "baseline-b.json"
    for lane, output in (("A", a_path), ("B", b_path)):
        rel = CONSUMERS[lane]
        code, stdout, _stderr = run_total([sys.executable, "-B", str(root / rel), "--inputs", str(inputs), "--emit", str(output)])
        if code != 0 or stdout.strip() or not output.is_file():
            raise RuntimeError("baseline evaluator " + lane)
    a, b = load(a_path), load(b_path)
    views = []
    for lane, projection in (("a", a), ("b", b)):
        view = workspace / ("baseline-" + lane + "-finite.json")
        view.write_bytes(canonical({"producer": projection["producer"], "contract_sha256": projection["contract_sha256"],
                                    "finite_records": projection["finite_records"]}))
        views.append(view)
    return {"a": a_path, "b": b_path, "a_view": views[0], "b_view": views[1]}


def expected_bundle(root: Path, catalogue: dict):
    inputs = root / "inputs/preauthority"
    outcomes = []
    for row in catalogue["mutations"]:
        for consumer in row["consumers"]:
            material = f"prepared-transaction-probe\n{row['id']}\n{consumer}\n{row['code']}\n".encode()
            outcomes.append({"mutation_id": row["id"], "consumer_key": consumer, "outcome": "REJECT", "exit_code": 2,
                             "rejection_code": row["code"], "result_digest": hashlib.sha256(material).hexdigest()})
    return {"schema_version": "paper45.mutation-outcomes.v1",
            "contract_sha256": hashlib.sha256((inputs / "EXPERIMENT_CONTRACT.json").read_bytes()).hexdigest(),
            "registry_sha256": hashlib.sha256((inputs / "MUTATION_REGISTRY.json").read_bytes()).hexdigest(),
            "outcomes": outcomes}


def consumer_command(clone: Path, consumer: str, baseline: dict, prepared: Path):
    source = clone / CONSUMERS[consumer]
    inputs = clone / "inputs/preauthority"
    if consumer in {"A", "B"}:
        return [sys.executable, "-B", str(source), "--inputs", str(inputs)]
    if consumer == "P":
        return [sys.executable, "-B", str(source), "--inputs", str(inputs), "--b", str(baseline["b"])]
    if consumer == "X":
        return [sys.executable, "-B", str(source), "--inputs", str(inputs),
                "--a-finite", str(baseline["a_view"]), "--b-finite", str(baseline["b_view"])]
    return [sys.executable, "-B", str(source), "--root", str(clone)]


def invoke(clone: Path, consumer: str, row: dict, baseline: dict, prepared: Path):
    if row["id"] == "M048" and consumer == "G":
        command = [sys.executable, "-B", str(clone / "code/integration/run_integration.py"),
                   "--root", str(clone), "--phase", "FINAL", "--force-late-failure",
                   "--prepared-mutation-bundle", str(prepared)]
        timeout = 900
    else:
        command = consumer_command(clone, consumer, baseline, prepared)
        timeout = 300
    exit_code, stdout, _stderr = run_total(command, timeout)
    lines = [line for line in stdout.splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError("consumer payload cardinality")
    payload = json.loads(lines[0])
    if exit_code != 2 or payload.get("outcome") != "REJECT" or payload.get("exit_code") != 2:
        raise RuntimeError("mutation survived")
    code = payload.get("rejection_code")
    raw_digest = hashlib.sha256((stdout.strip() + "\n").encode()).hexdigest()
    return {"mutation_id": row["id"], "consumer_key": consumer, "outcome": "REJECT", "exit_code": 2,
            "rejection_code": code, "result_digest": raw_digest}


def execute(root: Path):
    root = root.resolve(strict=True)
    inputs = root / "inputs/preauthority"
    catalogue_path = inputs / "MUTATION_REGISTRY.json"
    catalogue = load(catalogue_path)
    if [row["id"] for row in catalogue["mutations"]] != [f"M{number:03d}" for number in range(1, 76)]:
        raise RuntimeError("catalogue sequence")
    outcomes, survivors = [], []
    with tempfile.TemporaryDirectory(prefix="paper45-mutations-", dir="/tmp") as raw:
        workspace = Path(raw)
        baseline = build_baseline(root, workspace)
        prepared = workspace / "prepared-mutation-bundle.json"
        prepared.write_bytes(canonical(expected_bundle(root, catalogue)))
        for row in catalogue["mutations"]:
            clone = workspace / row["id"] / "candidate"
            clone.parent.mkdir()
            copy_candidate(root, clone)
            try:
                apply_physical_mutation(clone, row, clone.parent)
                observed_consumers = []
                for consumer in row["consumers"]:
                    result = invoke(clone, consumer, row, baseline, prepared)
                    outcomes.append(result)
                    observed_consumers.append(consumer)
                    if result["rejection_code"] != row["code"]:
                        survivors.append(row["id"] + ":" + consumer + ":wrong-code")
                if observed_consumers != row["consumers"] or len(set(observed_consumers)) != len(observed_consumers):
                    survivors.append(row["id"] + ":consumer-order")
            except Exception as exc:
                survivors.append(row["id"] + ":harness:" + type(exc).__name__)
    bundle = {"schema_version": "paper45.mutation-outcomes.v1",
              "contract_sha256": hashlib.sha256((inputs / "EXPERIMENT_CONTRACT.json").read_bytes()).hexdigest(),
              "registry_sha256": hashlib.sha256(catalogue_path.read_bytes()).hexdigest(), "outcomes": outcomes}
    return bundle, survivors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--emit", type=Path)
    options = parser.parse_args()
    try:
        bundle, survivors = execute(options.root)
        encoded = canonical(bundle)
        if options.emit:
            options.emit.write_bytes(encoded)
        else:
            sys.stdout.buffer.write(encoded)
        if survivors:
            sys.stderr.write(json.dumps({"survivors": survivors}, sort_keys=True, separators=(",", ":")) + "\n")
            return 2
        return 0
    except Exception:
        sys.stderr.write('{"error":{"code":"INTERNAL_EXCEPTION","detail":"redacted","stage":"MUTATION_RUNNER"},"exit_code":3,"outcome":"HARNESS_ERROR"}\n')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
