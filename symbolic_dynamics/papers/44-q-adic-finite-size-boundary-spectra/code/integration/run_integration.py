#!/usr/bin/env python3
"""Stage-all, independently certify, then atomically install Paper 44 outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Callable


PYTHON = sys.executable
FILES_A = [
    "RESULT_LEDGER.json", "audits/external_auditor_mutations.json",
    "audits/independence_audit.json", "audits/integrity_audit.json",
    "audits/proof_audit.json", "audits/route_independent.json",
    "audits/route_primary.json", "audits/source_audit.json", "audits/type_audit.json",
    "data/source_packet.json", "evaluations/route_a/SD-C46/2026-08-18.yaml",
    "reports/EXPERIMENT_REPORT.md", "results/evaluator_a.json", "results/evaluator_b.json",
    "results/exact_comparison.json", "tests/mutation_results.json",
]
DIRECTORIES = ["audits", "data", "evaluations", "evaluations/route_a",
               "evaluations/route_a/SD-C46", "reports", "results", "tests"]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe_relative(value: str) -> bool:
    pure = PurePosixPath(value)
    return type(value) is str and value != "" and "\\" not in value \
        and not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def validate_root_before_io(root: Path) -> None:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink() \
            or root.resolve(strict=True) != root:
        raise ValueError("unsafe integration root")
    for path in root.rglob("*"):
        metadata = os.lstat(path)
        if stat.S_ISLNK(metadata.st_mode) or path.name == "__pycache__" or path.suffix == ".pyc":
            raise ValueError("root hygiene")
        if not stat.S_ISDIR(metadata.st_mode) and not stat.S_ISREG(metadata.st_mode):
            raise ValueError("nonregular root node")
    target = root / "outputs"
    if target.exists() and (target.is_symlink() or not target.is_dir()):
        raise ValueError("unsafe target")


def static_file(root: Path, relative: str) -> Path:
    if not safe_relative(relative): raise ValueError("unsafe static relative")
    cursor = root
    for part in relative.split("/"):
        cursor = cursor / part
        if cursor.is_symlink(): raise ValueError("static symlink")
    resolved = cursor.resolve(strict=True)
    metadata = os.lstat(resolved)
    if root not in resolved.parents or not stat.S_ISREG(metadata.st_mode):
        raise ValueError("static containment/kind")
    return resolved


def invoke(script: Path, arguments: list[str], cwd: Path, hostile: Path,
           expected_exit: int = 0) -> bytes:
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                   "PYTHONPATH": str(hostile), "PYTHONDONTWRITEBYTECODE": "1"}
    process = subprocess.run([PYTHON, "-I", "-B", str(script), *arguments], cwd=cwd,
                             env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             check=False)
    if process.returncode != expected_exit or process.stderr:
        detail = process.stderr.decode("utf-8", errors="replace").splitlines()[-4:]
        raise ValueError(f"subprocess {script.name} rc={process.returncode}: {detail}")
    return process.stdout


def decode(raw: bytes, schema: str | None = None) -> dict[str, Any]:
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if type(value) is not dict or raw != canonical(value): raise ValueError("noncanonical subprocess JSON")
    if schema is not None and value.get("schema") != schema: raise ValueError("subprocess schema")
    return value


def ensure_parent_modes(output: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    cursor = target.parent
    while cursor != output:
        cursor.chmod(0o755)
        cursor = cursor.parent


def write_stage(output: Path, relative: str, raw: bytes) -> None:
    if not safe_relative(relative): raise ValueError("unsafe staged relative")
    target = output.joinpath(*relative.split("/"))
    ensure_parent_modes(output, target)
    cursor = target
    while cursor != output:
        if cursor.exists() and cursor.is_symlink(): raise ValueError("stage symlink")
        cursor = cursor.parent
    target.write_bytes(raw)
    target.chmod(0o644)


def rows(output: Path, excluded: set[str] | None = None) -> list[dict[str, Any]]:
    excluded = excluded or set()
    answer = []
    for path in output.rglob("*"):
        relative = path.relative_to(output).as_posix()
        if relative in excluded: continue
        metadata = os.lstat(path)
        mode = stat.S_IMODE(metadata.st_mode)
        if stat.S_ISLNK(metadata.st_mode): raise ValueError("output symlink")
        if stat.S_ISDIR(metadata.st_mode):
            answer.append({"kind": "directory", "mode": f"{mode:04o}", "path": relative})
        elif stat.S_ISREG(metadata.st_mode):
            answer.append({"kind": "regular", "mode": f"{mode:04o}", "path": relative,
                           "sha256": sha(path.read_bytes())})
        else: raise ValueError("output nonregular")
    return sorted(answer, key=lambda row: row["path"])


def exact_tree(output: Path, state: str) -> list[dict[str, Any]]:
    if stat.S_IMODE(os.lstat(output).st_mode) != 0o755:
        raise ValueError("output root mode contract")
    expected_files = sorted(FILES_A + (["PAPER_MANIFEST.sha256"] if state == "B" else []))
    actual = rows(output)
    file_rows = [row for row in actual if row["kind"] == "regular"]
    dir_rows = [row for row in actual if row["kind"] == "directory"]
    if [row["path"] for row in file_rows] != expected_files \
            or [row["path"] for row in dir_rows] != sorted(DIRECTORIES):
        raise ValueError("FINAL exact recursive namespace")
    if any(row["mode"] != "0644" for row in file_rows) \
            or any(row["mode"] != "0755" for row in dir_rows):
        raise ValueError("FINAL mode contract")
    return actual


def result_ledger(output: Path, state: str) -> bytes:
    excluded = {"RESULT_LEDGER.json", "audits/integrity_audit.json", "PAPER_MANIFEST.sha256"}
    ledger_rows = rows(output, excluded)
    return canonical({"payload": {"entry_count": len(ledger_rows), "rows": ledger_rows, "state": state},
                      "schema": "paper44-result-ledger-v2", "status": "PASS"})


def paper_manifest(root: Path, output: Path) -> bytes:
    manifest_rows: list[tuple[str, str, str, str]] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if relative == "outputs" or relative.startswith("outputs/") \
                or relative == "PREOUTPUT_STATIC_SEAL.json":
            continue
        metadata = os.lstat(path); mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode): manifest_rows.append((relative, "directory", mode, "-"))
        elif stat.S_ISREG(metadata.st_mode): manifest_rows.append((relative, "regular", mode, sha(path.read_bytes())))
        else: raise ValueError("paper manifest nonregular static")
    for path in output.rglob("*"):
        rel = path.relative_to(output).as_posix()
        if rel == "PAPER_MANIFEST.sha256": continue
        relative = "outputs/" + rel
        metadata = os.lstat(path); mode = f"{stat.S_IMODE(metadata.st_mode):04o}"
        if stat.S_ISDIR(metadata.st_mode): manifest_rows.append((relative, "directory", mode, "-"))
        elif stat.S_ISREG(metadata.st_mode): manifest_rows.append((relative, "regular", mode, sha(path.read_bytes())))
        else: raise ValueError("paper manifest nonregular output")
    manifest_rows.sort()
    header = "paper44-state-b-manifest-v2 exclude=PREOUTPUT_STATIC_SEAL.json,PAPER_MANIFEST.sha256\n"
    return (header + "".join(f"{kind} {mode} {digest} {path}\n"
                              for path, kind, mode, digest in manifest_rows)).encode("ascii")


def route_args(build: Path, output: Path, state: str, commit: str | None) -> list[str]:
    args = ["--stage", str(build), "--route", str(output / "evaluations/route_a/SD-C46/2026-08-18.yaml"),
            "--comparison", str(output / "results/exact_comparison.json"), "--state", state]
    if state == "B": args += ["--commit", str(commit)]
    return args


def hostile_workspace(build: Path) -> tuple[Path, Path]:
    cwd, hostile = build / "hostile_cwd", build / "hostile_modules"
    cwd.mkdir(mode=0o755); hostile.mkdir(mode=0o755)
    (hostile / "json.py").write_text("raise RuntimeError('hostile json shadow')\n", encoding="ascii")
    (hostile / "sitecustomize.py").write_text("raise RuntimeError('hostile sitecustomize')\n", encoding="ascii")
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(hostile)}
    naive = subprocess.run([PYTHON, "-c", "import json"], cwd=cwd, env=environment,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    isolated = subprocess.run([PYTHON, "-I", "-B", "-c", "import json"], cwd=cwd,
                              env={**environment, "PYTHONDONTWRITEBYTECODE": "1"},
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if naive.returncode == 0 or isolated.returncode != 0: raise ValueError("hostile isolation control")
    return cwd, hostile


def run_route_validators(root: Path, build: Path, output: Path, state: str,
                         commit: str | None, cwd: Path, hostile: Path) -> tuple[bytes, bytes]:
    arguments = route_args(build, output, state, commit)
    primary = invoke(static_file(root, "code/route/validate_route.py"), arguments, cwd, hostile)
    independent = invoke(static_file(root, "code/route/audit_route_independent.py"), arguments, cwd, hostile)
    p, q = decode(primary, "paper44-route-primary-audit-v2"), decode(independent, "paper44-route-independent-audit-v2")
    if p["status"] != "PASS" or q["status"] != "PASS" \
            or p["payload"]["route_sha256"] != q["payload"]["route_sha256"]:
        raise ValueError("Route auditors disagree")
    return primary, independent


def build_once(root: Path, build: Path, state: str, commit: str | None) -> Path:
    output = build / "outputs"; output.mkdir(mode=0o755); output.chmod(0o755)
    cwd, hostile = hostile_workspace(build)
    packet = invoke(static_file(root, "code/source/build_packet.py"), ["--root", str(root)], cwd, hostile)
    decode(packet, "paper44-result-free-source-packet-v1"); write_stage(output, "data/source_packet.json", packet)
    eval_a = invoke(static_file(root, "code/evaluator_a/evaluate.py"), ["--root", str(root)], cwd, hostile)
    decode(eval_a, "paper44-evaluator-a-v1"); write_stage(output, "results/evaluator_a.json", eval_a)
    eval_b = invoke(static_file(root, "code/evaluator_b/evaluate.py"), ["--root", str(root)], cwd, hostile)
    decode(eval_b, "paper44-evaluator-b-v1"); write_stage(output, "results/evaluator_b.json", eval_b)
    comparison = invoke(static_file(root, "code/comparator/exact_compare.py"), [
        "--root", str(root), "--stage", str(build), "--a", str(output / "results/evaluator_a.json"),
        "--b", str(output / "results/evaluator_b.json")], cwd, hostile)
    decode(comparison, "paper44-exact-comparison-v1"); write_stage(output, "results/exact_comparison.json", comparison)
    for name, script, schema in [
        ("proof_audit.json", "code/auditors/proof_auditor.py", "paper44-proof-audit-v1"),
        ("source_audit.json", "code/auditors/source_auditor.py", "paper44-source-audit-v1"),
        ("type_audit.json", "code/auditors/type_auditor.py", "paper44-type-audit-v1"),
        ("independence_audit.json", "code/auditors/independence_auditor.py", "paper44-independence-audit-v1")]:
        raw = invoke(static_file(root, script), ["--root", str(root)], cwd, hostile)
        decode(raw, schema); write_stage(output, "audits/" + name, raw)
    mutation_raw = invoke(static_file(root, "code/tests/run_mutations.py"),
                          ["--root", str(root), "--scratch", str(build / "mutation_scratch")], cwd, hostile)
    decode(mutation_raw, "paper44-mutation-results-v1"); write_stage(output, "tests/mutation_results.json", mutation_raw)
    external_raw = invoke(static_file(root, "code/tests/run_external_auditor_mutations.py"),
                          ["--root", str(root), "--scratch", str(build / "external_scratch")], cwd, hostile)
    decode(external_raw, "paper44-external-auditor-mutations-v2")
    write_stage(output, "audits/external_auditor_mutations.json", external_raw)
    render_args = ["--stage", str(build), "--comparison", str(output / "results/exact_comparison.json"), "--state", state]
    if state == "B": render_args += ["--commit", str(commit)]
    route = invoke(static_file(root, "code/route/render_route.py"), render_args, cwd, hostile)
    decode(route, "paper44-route-a-v0.3"); write_stage(output, "evaluations/route_a/SD-C46/2026-08-18.yaml", route)
    primary, independent = run_route_validators(root, build, output, state, commit, cwd, hostile)
    write_stage(output, "audits/route_primary.json", primary)
    write_stage(output, "audits/route_independent.json", independent)
    report = invoke(static_file(root, "code/report/reconstruct_report.py"), ["--output-root", str(output)], cwd, hostile)
    report.decode("ascii"); write_stage(output, "reports/EXPERIMENT_REPORT.md", report)
    write_stage(output, "RESULT_LEDGER.json", result_ledger(output, state))
    integrity_args = ["--root", str(root), "--output-root", str(output), "--state", state, "--phase", "PRE_CERT"]
    if state == "B": integrity_args += ["--commit", str(commit)]
    certificate = invoke(static_file(root, "code/integration/audit_integrity.py"), integrity_args, cwd, hostile)
    decode(certificate, "paper44-runtime-integrity-certificate-v2")
    write_stage(output, "audits/integrity_audit.json", certificate)
    if state == "B": write_stage(output, "PAPER_MANIFEST.sha256", paper_manifest(root, output))
    final_args = list(integrity_args); final_args[final_args.index("PRE_CERT")] = "FINAL"
    verification = invoke(static_file(root, "code/integration/audit_integrity.py"), final_args, cwd, hostile)
    decode(verification, "paper44-runtime-final-verification-v1")
    exact_tree(output, state)
    return output


def derive_state(root: Path, source: Path, build: Path, state: str, commit: str | None) -> Path:
    output = build / "outputs"; shutil.copytree(source, output, copy_function=shutil.copy2)
    for relative in ["RESULT_LEDGER.json", "audits/integrity_audit.json", "audits/route_primary.json",
                     "audits/route_independent.json", "evaluations/route_a/SD-C46/2026-08-18.yaml",
                     "reports/EXPERIMENT_REPORT.md", "PAPER_MANIFEST.sha256"]:
        path = output / relative
        if path.exists(): path.unlink()
    cwd, hostile = hostile_workspace(build)
    render_args = ["--stage", str(build), "--comparison", str(output / "results/exact_comparison.json"), "--state", state]
    if state == "B": render_args += ["--commit", str(commit)]
    route = invoke(static_file(root, "code/route/render_route.py"), render_args, cwd, hostile)
    write_stage(output, "evaluations/route_a/SD-C46/2026-08-18.yaml", route)
    primary, independent = run_route_validators(root, build, output, state, commit, cwd, hostile)
    write_stage(output, "audits/route_primary.json", primary); write_stage(output, "audits/route_independent.json", independent)
    report = invoke(static_file(root, "code/report/reconstruct_report.py"), ["--output-root", str(output)], cwd, hostile)
    write_stage(output, "reports/EXPERIMENT_REPORT.md", report)
    write_stage(output, "RESULT_LEDGER.json", result_ledger(output, state))
    args = ["--root", str(root), "--output-root", str(output), "--state", state, "--phase", "PRE_CERT"]
    if state == "B": args += ["--commit", str(commit)]
    cert = invoke(static_file(root, "code/integration/audit_integrity.py"), args, cwd, hostile)
    write_stage(output, "audits/integrity_audit.json", cert)
    if state == "B": write_stage(output, "PAPER_MANIFEST.sha256", paper_manifest(root, output))
    args[args.index("PRE_CERT")] = "FINAL"
    decode(invoke(static_file(root, "code/integration/audit_integrity.py"), args, cwd, hostile),
           "paper44-runtime-final-verification-v1")
    exact_tree(output, state)
    return output


def json_mutate(path: Path, change: Callable[[dict[str, Any]], None]) -> None:
    value = json.loads(path.read_text(encoding="ascii"), object_pairs_hook=unique)
    change(value); path.write_bytes(canonical(value)); path.chmod(0o644)


def runtime_rejects(root: Path, output: Path, state: str, commit: str | None, cwd: Path) -> int:
    args = [PYTHON, "-I", "-B", str(static_file(root, "code/integration/audit_integrity.py")),
            "--root", str(root), "--output-root", str(output), "--state", state, "--phase", "FINAL"]
    if state == "B": args += ["--commit", str(commit)]
    process = subprocess.run(args, cwd=cwd, env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                             "PYTHONPATH": "", "PYTHONDONTWRITEBYTECODE": "1"},
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return process.returncode


def physical_survivor_suite(root: Path, output_a: Path, output_b: Path, scratch: Path) -> bytes:
    scratch.mkdir(mode=0o755); cwd = scratch / "cwd"; cwd.mkdir(mode=0o755)
    cases: list[tuple[str, str, Callable[[Path], None]]] = []
    def add(identifier: str, state: str, fn: Callable[[Path], None]) -> None: cases.append((identifier, state, fn))
    add("evaluator_z_bool", "A", lambda o: json_mutate(o/"results/evaluator_a.json", lambda x: x["payload"]["finite_records"][0].__setitem__("z_n", True)))
    add("evaluator_extra_key", "A", lambda o: json_mutate(o/"results/evaluator_a.json", lambda x: x["payload"]["finite_records"][0].__setitem__("extra", 0)))
    add("gamma_bits", "A", lambda o: json_mutate(o/"results/evaluator_a.json", lambda x: x["payload"]["gamma_intervals"][0].__setitem__("bits", 999)))
    add("gamma_truncation", "A", lambda o: json_mutate(o/"results/evaluator_b.json", lambda x: x["payload"]["gamma_intervals"][0].__setitem__("truncation_index", 1)))
    def false_interval(o: Path) -> None:
        def f(x: dict[str, Any]) -> None:
            row=x["payload"]["gamma_intervals"][0]; row["lower_numerator"]="1"; row["lower_denominator"]="1"; row["upper_numerator"]="2"; row["upper_denominator"]="1"
        json_mutate(o/"results/evaluator_a.json", f)
    add("gamma_false_interval", "A", false_interval)
    add("gamma_tail_noninteger", "A", lambda o: json_mutate(o/"results/evaluator_b.json", lambda x: x["payload"]["gamma_intervals"][0].__setitem__("tail_bound_numerator", "1.5")))
    add("gamma_tail_missing", "A", lambda o: json_mutate(o/"results/evaluator_b.json", lambda x: x["payload"]["gamma_intervals"][0].__delitem__("tail_bound_denominator")))
    add("proof_bool_to_int", "A", lambda o: json_mutate(o/"audits/proof_audit.json", lambda x: x["payload"].__setitem__("finite_grid_used_as_proof", 0)))
    add("source_int_to_bool", "A", lambda o: json_mutate(o/"audits/source_audit.json", lambda x: x["payload"].__setitem__("leading_results_novelty_credit", False)))
    add("type_false_to_list", "A", lambda o: json_mutate(o/"audits/type_audit.json", lambda x: x["payload"].__setitem__("determinant_defined", [])))
    add("type_extra_key", "A", lambda o: json_mutate(o/"audits/type_audit.json", lambda x: x["payload"].__setitem__("extra", 0)))
    add("registry_record_add", "A", lambda o: json_mutate(o/"tests/mutation_results.json", lambda x: x["payload"]["records"].append(x["payload"]["records"][0])))
    add("registry_record_delete", "A", lambda o: json_mutate(o/"tests/mutation_results.json", lambda x: x["payload"]["records"].pop()))
    add("registry_record_reorder", "A", lambda o: json_mutate(o/"tests/mutation_results.json", lambda x: x["payload"]["records"].reverse()))
    add("registry_record_rename", "A", lambda o: json_mutate(o/"tests/mutation_results.json", lambda x: x["payload"]["records"][0].__setitem__("instance_id", "renamed")))
    add("registry_survivor_bool", "A", lambda o: json_mutate(o/"tests/mutation_results.json", lambda x: x["payload"].__setitem__("survivor_count", False)))
    add("route_extra_key", "A", lambda o: json_mutate(o/"evaluations/route_a/SD-C46/2026-08-18.yaml", lambda x: x.__setitem__("undeclared", True)))
    def mixed_route(o: Path) -> None:
        def f(x: dict[str, Any]) -> None:
            x["authority_integration"].update({"state":"A","authority_writes":77,"git_operations":88}); x["terminal_codes"]["theorem_counterexample"]="RENAMED"; x["external_literature_disposition"]["owner"]="wrong"
        json_mutate(o/"evaluations/route_a/SD-C46/2026-08-18.yaml", f)
    add("route_mixed_state_writes_git_terminal_external", "B", mixed_route)
    add("route_missing_artifact", "A", lambda o: (o/"data/source_packet.json").unlink())
    add("route_unsafe_path", "A", lambda o: json_mutate(o/"evaluations/route_a/SD-C46/2026-08-18.yaml", lambda x: x["artifact_paths"].__setitem__(0,"../escape")))
    add("route_checkmap_add", "A", lambda o: json_mutate(o/"audits/route_primary.json", lambda x: x["payload"]["checks"].__setitem__("extra", True)))
    add("route_checkmap_delete", "A", lambda o: json_mutate(o/"audits/route_independent.json", lambda x: x["payload"]["checks"].pop(next(iter(x["payload"]["checks"])))))
    def rename_check(o: Path) -> None:
        def f(x: dict[str, Any]) -> None:
            checks=x["payload"]["checks"]; key=next(iter(checks)); checks["renamed"] = checks.pop(key)
        json_mutate(o/"audits/route_primary.json", f)
    add("route_checkmap_rename", "A", rename_check)
    add("output_file_mode", "A", lambda o: (o/"README_DOES_NOT_EXIST").chmod(0o600))
    # Replace the placeholder mode mutator before execution; it needs a guaranteed file.
    cases[-1] = ("output_file_mode", "A", lambda o: (o/"reports/EXPERIMENT_REPORT.md").chmod(0o600))
    add("output_empty_directory", "A", lambda o: (o/"rogue-empty").mkdir(mode=0o755))
    add("canonical_false_report", "A", lambda o: (o/"reports/EXPERIMENT_REPORT.md").write_bytes(b"# canonical but false report\n"))
    def coordinated(o: Path) -> None:
        json_mutate(o/"results/evaluator_a.json", lambda x: x["payload"]["finite_records"][1].__setitem__("z_n", True))
        json_mutate(o/"RESULT_LEDGER.json", lambda x: [row.__setitem__("sha256", sha((o/"results/evaluator_a.json").read_bytes())) for row in x["payload"]["rows"] if row["path"]=="results/evaluator_a.json"])
        report=o/"reports/EXPERIMENT_REPORT.md"; report.write_bytes(report.read_bytes().replace(b"Exact finite replay",b"Re-ledgered false replay")); report.chmod(0o644)
        json_mutate(o/"RESULT_LEDGER.json", lambda x: [row.__setitem__("sha256", sha(report.read_bytes())) for row in x["payload"]["rows"] if row["path"]=="reports/EXPERIMENT_REPORT.md"])
    add("coordinated_reledger_rereport", "A", coordinated)
    records=[]
    for index,(identifier,state,mutate) in enumerate(cases):
        case_root=scratch/f"case_{index:02d}"; output=case_root/"outputs"
        shutil.copytree(output_a if state=="A" else output_b, output, copy_function=shutil.copy2)
        mutate(output)
        rc=runtime_rejects(root,output,state,"1"*40 if state=="B" else None,cwd)
        if rc==0: raise ValueError("physical survivor mutation accepted: "+identifier)
        records.append({"id":identifier,"outcome":"REJECT","returncode_nonzero":True})
    return canonical({"payload":{"case_count":len(records),"records":records,"survivor_count":0},
                      "schema":"paper44-survivor-physical-mutations-v1","status":"PASS"})


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--state",choices=("A","B"),default="A")
    parser.add_argument("--commit"); parser.add_argument("--force-late-failure",action="store_true")
    parser.add_argument("--run-survivor-mutations",action="store_true")
    args=parser.parse_args(); root=Path(__file__).resolve().parents[2]
    validate_root_before_io(root)
    if args.state=="A" and args.commit is not None: raise ValueError("State A commit forbidden")
    if args.state=="B" and (args.commit is None or re.fullmatch(r"[0-9a-f]{40}",args.commit) is None or args.commit=="0"*40): raise ValueError("State B commit")
    with tempfile.TemporaryDirectory(prefix="paper44_transaction_",dir=str(root.parent)) as temporary_name:
        temporary=Path(temporary_name); pre_cwd=temporary/"preflight_cwd"; pre_hostile=temporary/"preflight_hostile"
        pre_cwd.mkdir(); pre_hostile.mkdir()
        frozen=invoke(static_file(root,"external_auditor/frozen_auditor.py"),["--root",str(root)],pre_cwd,pre_hostile)
        if decode(frozen,"paper44-frozen-external-audit-v2")["status"]!="PASS": raise ValueError("frozen preflight")
        one,two=temporary/"build_one",temporary/"build_two"; one.mkdir(); two.mkdir()
        first=build_once(root,one,args.state,args.commit); second=build_once(root,two,args.state,args.commit)
        if rows(first)!=rows(second): raise ValueError("two staged builds differ")
        tree_hash=sha(canonical(rows(first)))
        other_state="B" if args.state=="A" else "A"; other_commit="1"*40 if other_state=="B" else None
        paired_build=temporary/"paired_state"; paired_build.mkdir()
        paired=derive_state(root,first,paired_build,other_state,other_commit)
        output_a=first if args.state=="A" else paired; output_b=first if args.state=="B" else paired
        survivor_raw=canonical({"payload":{"case_count":0,"records":[],"survivor_count":0},"schema":"paper44-survivor-physical-mutations-v1","status":"NOT_RUN"})
        if args.run_survivor_mutations:
            survivor_raw=physical_survivor_suite(root,output_a,output_b,temporary/"survivor_suite")
        target=root/"outputs"; before=rows(target) if target.exists() else []
        if args.force_late_failure:
            after=rows(target) if target.exists() else []
            if before!=after: raise ValueError("late failure changed target")
            sys.stdout.buffer.write(canonical({"payload":{"atomic_rename_count":0,
                "late_failure_target_unchanged":True,"physical_target_writes":0,
                "state":args.state,"survivor_mutation_count":decode(survivor_raw)["payload"]["case_count"],
                "survivor_mutation_result_sha256":sha(survivor_raw),"tree_sha256":tree_hash},
                "schema":"paper44-transaction-result-v2","status":"FORCED_LATE_FAILURE"}))
            return 86
        if target.exists():
            if rows(target)!=rows(first): raise ValueError("existing outputs differ; no overwrite")
            writes,renames,disposition=0,0,"IDEMPOTENT_NO_WRITE"
        else:
            writes=sum(row["kind"]=="regular" for row in rows(first)); os.replace(first,target)
            renames,disposition=1,"ATOMIC_INSTALL"
        sys.stdout.buffer.write(canonical({"payload":{"atomic_rename_count":renames,
            "disposition":disposition,"physical_target_writes":writes,"state":args.state,
            "survivor_mutation_count":decode(survivor_raw)["payload"]["case_count"],
            "survivor_mutation_result_sha256":sha(survivor_raw),"tree_sha256":tree_hash},
            "schema":"paper44-transaction-result-v2","status":"PASS"}))
        return 0


if __name__=="__main__": raise SystemExit(main())
