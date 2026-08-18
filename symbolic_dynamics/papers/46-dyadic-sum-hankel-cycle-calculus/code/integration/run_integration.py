#!/usr/bin/env python3
"""Transactional isolated P46 integration runner."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


STATE_A = [
    "RESULT_LEDGER.json", "audits/external_auditor_mutations.json",
    "audits/independence_audit.json", "audits/integrity_audit.json",
    "audits/proof_audit.json", "audits/route_independent.json",
    "audits/route_primary.json", "audits/source_audit.json",
    "audits/type_audit.json", "data/source_packet.json",
    "evaluations/route_a/SD-C48/2026-08-18.yaml",
    "reports/EXPERIMENT_REPORT.md", "results/evaluator_c.json",
    "results/evaluator_m.json", "results/exact_comparison.json",
    "tests/mutation_results.json",
]
FORCE_LATE_FAILURE_EXIT = 86
STATIC_MANIFEST_EXCLUSIONS = frozenset({
    "STATIC_INPUT_SHA256SUMS.txt",
    "PREOUTPUT_STATIC_SEAL.json",
})
PAPER_MANIFEST_ROOT_EXCLUSIONS = frozenset({"PREOUTPUT_STATIC_SEAL.json"})
PAPER_MANIFEST_SELF = "outputs/PAPER_MANIFEST.sha256"
OUTPUT_TREE_HASH_DOMAIN = "OUTPUTS_RELATIVE_PATH_NUL_RAW_BYTES_ONLY_V1"


class StrictParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValueError(f"CLI_ARGUMENT_ERROR: {message}")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate key")
        output[key] = value
    return output


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def lexical_root(raw: str) -> Path:
    if not raw.startswith("/"):
        raise ValueError("root must be absolute")
    if any(part in {"", ".", ".."} for part in raw.split("/")[1:]):
        raise ValueError("noncanonical root path")
    path = Path(raw)
    if path.is_symlink() or not path.is_dir():
        raise ValueError("unsafe root")
    return path.resolve(strict=True)


def lexical_output(raw: str, root: Path) -> Path:
    if not raw.startswith("/") or any(part in {"", ".", ".."} for part in raw.split("/")[1:]):
        raise ValueError("noncanonical output path")
    path = Path(raw)
    if path != root / "outputs":
        raise ValueError("output must be exact package-relative outputs directory")
    cursor = root
    if cursor.is_symlink():
        raise ValueError("root symlink")
    if path.exists() and (path.is_symlink() or not path.is_dir()):
        raise ValueError("unsafe existing target")
    return path


def static_file(root: Path, relative: str) -> Path:
    cursor = root
    for part in relative.split("/"):
        if part in {"", ".", ".."}:
            raise ValueError("unsafe relative")
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("static symlink")
    result = cursor.resolve(strict=True)
    if root not in result.parents or not result.is_file():
        raise ValueError("static containment")
    return result


def verify_static(root: Path) -> tuple[int, str]:
    manifest = static_file(root, "STATIC_INPUT_SHA256SUMS.txt")
    raw = manifest.read_bytes()
    names: list[str] = []
    for line in raw.decode("ascii").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_./-]+)", line)
        if not match:
            raise ValueError("static manifest row")
        expected, relative = match.groups()
        if relative in STATIC_MANIFEST_EXCLUSIONS \
                or relative.startswith("outputs/"):
            raise ValueError("static manifest scope")
        if sha(static_file(root, relative).read_bytes()) != expected:
            raise ValueError("static drift")
        names.append(relative)
    actual = sorted(path.relative_to(root).as_posix() for path in root.rglob("*")
                    if path.is_file() and not path.is_symlink()
                    and not path.relative_to(root).as_posix().startswith("outputs/")
                    and path.relative_to(root).as_posix() not in
                    STATIC_MANIFEST_EXCLUSIONS)
    if names != sorted(names) or names != actual or len(names) != len(set(names)):
        raise ValueError("static exact set")
    offenders = [path for path in root.rglob("*")
                 if path.is_symlink() or path.name == "__pycache__" or path.suffix == ".pyc"]
    if offenders:
        raise ValueError("static hygiene")
    return len(names), sha(raw)


def environment(hostile: Path) -> dict[str, str]:
    return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "PYTHONPATH": str(hostile), "PYTHONDONTWRITEBYTECODE": "1"}


def run_script(root: Path, relative: str, arguments: list[str], cwd: Path,
               hostile: Path, expected_exit: int = 0) -> bytes:
    script = static_file(root, relative)
    process = subprocess.run([sys.executable, "-I", "-B", str(script), *arguments],
                             cwd=cwd, env=environment(hostile), stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=False)
    if process.returncode != expected_exit or (expected_exit == 0 and process.stderr):
        raise ValueError(f"subprocess failure: {relative}: {process.returncode}")
    return process.stdout


def start_script(root: Path, relative: str, arguments: list[str], cwd: Path,
                 hostile: Path) -> subprocess.Popen[bytes]:
    script = static_file(root, relative)
    return subprocess.Popen([sys.executable, "-I", "-B", str(script), *arguments],
                            cwd=cwd, env=environment(hostile), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)


def canonical_json(raw: bytes, schema: str | None = None) -> dict[str, Any]:
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique,
                       parse_constant=lambda word: (_ for _ in ()).throw(ValueError(word)))
    if raw != canonical(value):
        raise ValueError("noncanonical JSON subprocess output")
    if schema is not None and (value.get("schema") != schema or value.get("status") != "PASS"):
        raise ValueError("wrong subprocess envelope")
    return value


def put(output: Path, relative: str, raw: bytes) -> None:
    target = output.joinpath(*relative.split("/"))
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        raise ValueError("duplicate staged output")
    target.write_bytes(raw)


def build_paper_manifest(root: Path, output: Path, integrity_raw: bytes) -> bytes:
    rows: list[tuple[str, str]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("outputs/") or relative in PAPER_MANIFEST_ROOT_EXCLUSIONS \
                or path.is_symlink() or not path.is_file():
            continue
        rows.append((relative, sha(path.read_bytes())))
    for name in STATE_A:
        raw = integrity_raw if name == "audits/integrity_audit.json" else (output / name).read_bytes()
        rows.append(("outputs/" + name, sha(raw)))
    rows.sort()
    names = [name for name, _ in rows]
    forbidden = set(PAPER_MANIFEST_ROOT_EXCLUSIONS) | {PAPER_MANIFEST_SELF}
    if len(names) != len(set(names)) or forbidden.intersection(names):
        raise ValueError("paper manifest forbidden inclusion")
    expected_root = sorted(
        path.relative_to(root).as_posix() for path in root.rglob("*")
        if path.is_file() and not path.is_symlink()
        and not path.relative_to(root).as_posix().startswith("outputs/")
        and path.relative_to(root).as_posix() not in PAPER_MANIFEST_ROOT_EXCLUSIONS
    )
    expected_names = sorted(expected_root + ["outputs/" + name for name in STATE_A])
    if names != expected_names:
        raise ValueError("paper manifest exact inclusion domain")
    return "".join(f"{digest}  {name}\n" for name, digest in rows).encode("ascii")


def build_ledger(output: Path, state: str) -> bytes:
    excluded = {"RESULT_LEDGER.json", "audits/integrity_audit.json", "PAPER_MANIFEST.sha256"}
    rows = [{"path": "outputs/" + name, "sha256": sha((output / name).read_bytes())}
            for name in sorted(item for item in STATE_A if item not in excluded)]
    return canonical({"payload": {"entry_count": len(rows), "rows": rows, "state": state},
                      "schema": "paper46-result-ledger-v1", "status": "PASS"})


def output_map(output: Path) -> dict[str, bytes]:
    return {path.relative_to(output).as_posix(): path.read_bytes()
            for path in sorted(output.rglob("*")) if path.is_file() and not path.is_symlink()}


def tree_digest(files: dict[str, bytes]) -> str:
    if any(not name or name.startswith("/") or "\0" in name
           or any(part in {"", ".", ".."} for part in name.split("/"))
           for name in files):
        raise ValueError("unsafe output tree hash domain")
    hasher = hashlib.sha256()
    for name in sorted(files):
        hasher.update(name.encode("ascii") + b"\0" + files[name])
    return hasher.hexdigest()


def build_once(root: Path, workspace: Path, state: str, commit: str | None,
               execute_external_mutations: bool) -> Path:
    output = workspace / "outputs"
    output.mkdir()
    unrelated = workspace / "hostile_cwd"
    hostile = workspace / "hostile_modules"
    unrelated.mkdir()
    hostile.mkdir()
    (hostile / "json.py").write_text("raise RuntimeError('hostile json imported')\n", encoding="ascii")
    (hostile / "sitecustomize.py").write_text("raise RuntimeError('hostile site imported')\n", encoding="ascii")
    common_state = ["--state", state] + (["--commit", commit] if commit else [])
    packet = run_script(root, "code/source/build_packet.py", ["--root", str(root), *common_state],
                        unrelated, hostile)
    canonical_json(packet, "paper46-source-packet-v1")
    put(output, "data/source_packet.json", packet)
    m_process = start_script(root, "code/evaluator_m/evaluate.py", ["--root", str(root)],
                             unrelated, hostile)
    c_process = start_script(root, "code/evaluator_c/evaluate.py", ["--root", str(root)],
                             unrelated, hostile)
    m_stdout, m_stderr = m_process.communicate()
    c_stdout, c_stderr = c_process.communicate()
    if m_process.returncode != 0 or c_process.returncode != 0 or m_stderr or c_stderr:
        raise ValueError("evaluator failure")
    canonical_json(m_stdout, "paper46-evaluator-m-v1")
    canonical_json(c_stdout, "paper46-evaluator-c-v1")
    put(output, "results/evaluator_m.json", m_stdout)
    put(output, "results/evaluator_c.json", c_stdout)
    comparison = run_script(root, "code/comparator/exact_compare.py",
                            ["--output-root", str(output), "--mode", "produce"],
                            unrelated, hostile)
    comparison_value = canonical_json(comparison, "paper46-exact-comparison-v1")
    if comparison_value["payload"]["finite_trace_mismatch_count"] != 0:
        raise ValueError("finite trace mismatch")
    put(output, "results/exact_comparison.json", comparison)
    route = run_script(root, "code/route/render_route.py", common_state, unrelated, hostile)
    canonical_json(route)
    put(output, "evaluations/route_a/SD-C48/2026-08-18.yaml", route)
    proof = run_script(root, "code/auditors/proof_auditor.py", ["--root", str(root)],
                       unrelated, hostile)
    canonical_json(proof, "paper46-proof-audit-v1")
    put(output, "audits/proof_audit.json", proof)
    independence = run_script(root, "code/auditors/independence_auditor.py",
                              ["--root", str(root)], unrelated, hostile)
    canonical_json(independence, "paper46-independence-audit-v1")
    put(output, "audits/independence_audit.json", independence)
    source = run_script(root, "code/auditors/source_auditor.py",
                        ["--root", str(root), "--output-root", str(output)], unrelated, hostile)
    canonical_json(source, "paper46-source-audit-v1")
    put(output, "audits/source_audit.json", source)
    types = run_script(root, "code/auditors/type_auditor.py", ["--output-root", str(output)],
                       unrelated, hostile)
    canonical_json(types, "paper46-type-audit-v1")
    put(output, "audits/type_audit.json", types)
    manifest_arg = "false" if state == "A" else "true"
    primary = run_script(root, "code/route/validate_route.py",
                         ["--output-root", str(output), "--state", state,
                          "--manifest-present", manifest_arg], unrelated, hostile)
    canonical_json(primary, "paper46-route-primary-audit-v1")
    put(output, "audits/route_primary.json", primary)
    independent = run_script(root, "code/route/audit_route_independent.py",
                             ["--output-root", str(output), "--state", state,
                              "--manifest-present", manifest_arg], unrelated, hostile)
    canonical_json(independent, "paper46-route-independent-audit-v1")
    put(output, "audits/route_independent.json", independent)
    mutation_scratch = workspace / "mutation_scratch"
    mutations = run_script(root, "code/tests/run_mutations.py",
                           ["--root", str(root), "--scratch", str(mutation_scratch)],
                           unrelated, hostile)
    canonical_json(mutations, "paper46-mutation-results-v1")
    put(output, "tests/mutation_results.json", mutations)
    external_template = run_script(root, "code/tests/run_external_auditor_mutations.py",
                                   ["--template"], unrelated, hostile)
    canonical_json(external_template, "paper46-external-auditor-mutations-v1")
    put(output, "audits/external_auditor_mutations.json", external_template)
    report = run_script(root, "code/report/reconstruct_report.py",
                        ["--output-root", str(output)], unrelated, hostile)
    put(output, "reports/EXPERIMENT_REPORT.md", report)
    put(output, "RESULT_LEDGER.json", build_ledger(output, state))
    preview = run_script(root, "code/integration/audit_integrity.py",
                         ["--root", str(root), "--output-root", str(output),
                          "--state", state, "--phase", "preview"], unrelated, hostile)
    canonical_json(preview, "paper46-read-only-integrity-audit-v1")
    if state == "B":
        put(output, "PAPER_MANIFEST.sha256", build_paper_manifest(root, output, preview))
        final = run_script(root, "code/integration/audit_integrity.py",
                           ["--root", str(root), "--output-root", str(output),
                            "--state", state, "--phase", "final"], unrelated, hostile)
        if final != preview:
            raise ValueError("integrity preview/final mismatch")
    else:
        final = preview
    put(output, "audits/integrity_audit.json", final)
    comparison_existing = run_script(
        root, "code/comparator/exact_compare.py",
        ["--output-root", str(output), "--mode", "audit-existing"], unrelated, hostile)
    canonical_json(comparison_existing, "paper46-comparison-existing-audit-v1")
    integrity_existing = run_script(
        root, "code/integration/audit_integrity.py",
        ["--root", str(root), "--output-root", str(output), "--state", state,
         "--phase", "audit-existing"], unrelated, hostile)
    canonical_json(integrity_existing, "paper46-integrity-existing-audit-v1")
    external = run_script(root, "external_auditor/frozen_auditor.py",
                          ["--root", str(root), "--output-root", str(output), "--state", state],
                          unrelated, hostile)
    canonical_json(external, "paper46-frozen-external-audit-v1")
    if execute_external_mutations:
        external_scratch = workspace / "external_mutation_scratch"
        actual = run_script(root, "code/tests/run_external_auditor_mutations.py",
                            ["--root", str(root), "--output-root", str(output),
                             "--state", state, "--scratch", str(external_scratch)],
                            unrelated, hostile)
        if actual != external_template:
            raise ValueError("physical external mutation audit differs from frozen template")
    external_again = run_script(root, "external_auditor/frozen_auditor.py",
                                ["--root", str(root), "--output-root", str(output), "--state", state],
                                unrelated, hostile)
    if external_again != external:
        raise ValueError("external audit nondeterminism")
    expected_names = sorted(STATE_A + (["PAPER_MANIFEST.sha256"] if state == "B" else []))
    if sorted(output_map(output)) != expected_names:
        raise ValueError("final staged namespace")
    return output


def clone_static(root: Path, destination: Path) -> None:
    def ignore_outputs(directory: str, names: list[str]) -> list[str]:
        return ["outputs"] if Path(directory).resolve() == root and "outputs" in names else []
    shutil.copytree(root, destination, symlinks=True, ignore=ignore_outputs)


def snapshot_target(target: Path) -> tuple[dict[str, tuple[str, int, int]], int | None]:
    if not target.exists():
        return {}, None
    records = {path.relative_to(target).as_posix():
               (sha(path.read_bytes()), path.stat().st_mtime_ns, path.stat().st_mode)
               for path in target.rglob("*") if path.is_file() and not path.is_symlink()}
    return records, target.stat().st_mtime_ns


def main() -> int:
    parser = StrictParser(add_help=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--state", choices=["A", "B"], required=True)
    parser.add_argument("--commit")
    parser.add_argument("--force-late-failure", action="store_true")
    args = parser.parse_args()
    root = lexical_root(args.root)
    target = lexical_output(args.output_root, root)
    if args.state == "A" and args.commit is not None:
        raise ValueError("State A commit forbidden")
    if args.state == "B" and (args.commit is None
                              or re.fullmatch(r"[0-9a-f]{40}", args.commit) is None
                              or args.commit == "0" * 40):
        raise ValueError("State B commit required")
    static_count, static_manifest_sha = verify_static(root)
    before = snapshot_target(target)
    holder = Path(tempfile.mkdtemp(prefix=".p46-transaction-", dir=str(root.parent)))
    try:
        primary_workspace = holder / "primary"
        second_workspace = holder / "second"
        relocated_root = holder / "relocated_package"
        relocated_workspace = holder / "relocated_build"
        primary_workspace.mkdir()
        second_workspace.mkdir()
        primary = build_once(root, primary_workspace, args.state, args.commit, True)
        second = build_once(root, second_workspace, args.state, args.commit, False)
        primary_map, second_map = output_map(primary), output_map(second)
        if primary_map != second_map:
            raise ValueError("two reconstructions differ")
        clone_static(root, relocated_root)
        relocated_workspace.mkdir()
        relocated = build_once(relocated_root, relocated_workspace, args.state, args.commit, False)
        if primary_map != output_map(relocated):
            raise ValueError("cold relocation differs")
        if args.force_late_failure:
            if snapshot_target(target) != before:
                raise ValueError("target changed before forced late failure")
            return FORCE_LATE_FAILURE_EXIT
        if target.exists():
            if output_map(target) != primary_map:
                raise ValueError("existing target differs; refusing overwrite")
            physical_writes = 0
        else:
            primary.rename(target)
            physical_writes = len(primary_map)
        receipt = {
            "payload": {
                "candidate_id": "SD-C48",
                "cold_relocation_equal": True,
                "output_file_count": len(primary_map),
                "output_tree_sha256": tree_digest(primary_map),
                "output_tree_sha256_domain": OUTPUT_TREE_HASH_DOMAIN,
                "physical_target_writes": physical_writes,
                "preoutput_seal_in_generated_hash_domains": False,
                "state": args.state,
                "static_file_count": static_count,
                "static_manifest_sha256": static_manifest_sha,
                "two_reconstructions_equal": True,
            },
            "schema": "paper46-integration-run-receipt-v1",
            "status": "PASS",
        }
        sys.stdout.buffer.write(canonical(receipt))
        return 0
    finally:
        shutil.rmtree(holder, ignore_errors=True)


def runner_rejection(code: str) -> int:
    sys.stdout.buffer.write(canonical({
        "payload": {"code": code},
        "schema": "paper46-runner-rejection-v1",
        "status": "REJECT",
    }))
    return 2


def classify_failure(error: Exception) -> str:
    message = str(error)
    if message.startswith("CLI_ARGUMENT_ERROR"):
        return "CLI_ARGUMENT_ERROR"
    if any(piece in message for piece in ["root must be absolute", "noncanonical root path",
                                           "unsafe root", "noncanonical output path",
                                           "output must be exact", "root symlink",
                                           "unsafe existing target", "No such file",
                                           "Not a directory"]):
        return "PATH_ROOT_INVALID"
    return "VALIDATION_RUNTIME_FAILURE"


def guarded_main() -> int:
    try:
        return main()
    except Exception as error:  # Totalized runner validation boundary.
        return runner_rejection(classify_failure(error))


if __name__ == "__main__":
    raise SystemExit(guarded_main())
