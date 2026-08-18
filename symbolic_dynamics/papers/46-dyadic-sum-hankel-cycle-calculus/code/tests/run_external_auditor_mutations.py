#!/usr/bin/env python3
"""Execute the frozen external auditor on physically mutated disposable clones."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable


CASE_IDS = [
    "EXT01_STATIC_BYTE_DRIFT",
    "EXT02_OUTPUT_DELETE",
    "EXT03_OUTPUT_EXTRA",
    "EXT04_OUTPUT_SYMLINK",
    "EXT05_CACHE_INJECTION",
    "EXT06_RESULT_LEDGER_COORDINATED_EDIT",
    "EXT07_REPORT_LEDGER_COORDINATED_EDIT",
    "EXT08_ROUTE_EDIT",
    "EXT09_INTEGRITY_SELF_TAMPER",
    "EXT10_SOURCE_PACKET_LEDGER_COORDINATED_EDIT",
    "EXT11_COORDINATED_NESTED_COUNT_INT_TO_BOOL",
    "EXT12_COORDINATED_NESTED_CUTOFF_INT_TO_FLOAT",
    "EXT13_COMPARISON_BOOLEAN_TO_INT",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def registry_path() -> Path:
    root = Path(__file__).resolve(strict=True).parents[2]
    path = root / "contracts" / "MUTATION_REGISTRY.json"
    if path.is_symlink() or not path.is_file() or root not in path.resolve(strict=True).parents:
        raise ValueError("unsafe registry path")
    return path


def physical_contracts() -> list[dict[str, Any]]:
    raw = registry_path().read_bytes()
    registry = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(registry) or registry.get("schema") != "paper46-mutation-registry-v1":
        raise ValueError("noncanonical mutation registry")
    cases = registry.get("physical_cases")
    if type(cases) is not list or [case.get("case_id") for case in cases] != CASE_IDS:
        raise ValueError("physical registry exact case order")
    for case in cases:
        if type(case) is not dict or set(case) != {
                "case_id", "consumers", "expected_receipts", "mutation_instance_id"}:
            raise ValueError("physical registry exact keys")
        if type(case["consumers"]) is not list or type(case["expected_receipts"]) is not dict \
                or set(case["consumers"]) != set(case["expected_receipts"]):
            raise ValueError("physical registry consumer binding")
    return cases


def receipt_summary(consumer: str, contract: dict[str, Any], exact: bool) -> dict[str, Any]:
    stdout = canonical(contract["stdout"])
    return {
        "consumer": consumer,
        "exact_rejection": exact,
        "expected_code": contract["stdout"]["payload"]["code"],
        "expected_exit": contract["exit"],
        "expected_stderr_bytes": contract["stderr_bytes"],
        "expected_stdout_sha256": hashlib.sha256(stdout).hexdigest(),
    }


def summary() -> dict[str, Any]:
    cases = physical_contracts()
    return {
        "payload": {
            "accepted_consumer_outcome_count": 0,
            "accepted_mutation_count": 0,
            "base_consumer_audits_passed": True,
            "base_external_audit_passed": True,
            "cases": [
                {
                    "case_id": case["case_id"],
                    "consumer_receipts": [
                        receipt_summary(consumer, case["expected_receipts"][consumer], True)
                        for consumer in case["consumers"]
                    ],
                    "exact_rejection": True,
                    "expected_code": next(iter(case["expected_receipts"].values()))
                    ["stdout"]["payload"]["code"],
                }
                for case in cases
            ],
            "physical_consumer_invocation_count": sum(len(case["consumers"]) for case in cases),
            "physical_mutated_clone_count": len(CASE_IDS),
        },
        "schema": "paper46-external-auditor-mutations-v1",
        "status": "PASS",
    }


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="ascii"))


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate key")
        output[key] = value
    return output


def write(path: Path, value: dict[str, Any]) -> None:
    path.write_bytes(canonical(value))


def rehash_ledger(output: Path, relative: str) -> None:
    ledger_path = output / "RESULT_LEDGER.json"
    ledger = load(ledger_path)
    digest = hashlib.sha256((output / relative).read_bytes()).hexdigest()
    full = "outputs/" + relative
    for row in ledger["payload"]["rows"]:
        if row["path"] == full:
            row["sha256"] = digest
            break
    else:
        raise ValueError("ledger row absent")
    write(ledger_path, ledger)


def mutate_static(root: Path, output: Path) -> None:
    path = root / "preauthority" / "README.md"
    path.chmod(0o644)
    path.write_bytes(path.read_bytes() + b"\nphysical mutation\n")


def mutate_delete(root: Path, output: Path) -> None:
    (output / "results" / "evaluator_m.json").unlink()


def mutate_extra(root: Path, output: Path) -> None:
    (output / "results" / "extra.json").write_bytes(b"{}\n")


def mutate_symlink(root: Path, output: Path) -> None:
    target = output / "results" / "evaluator_m.json"
    target.unlink()
    target.symlink_to("evaluator_c.json")


def mutate_cache(root: Path, output: Path) -> None:
    cache = root / "code" / "__pycache__"
    cache.mkdir()
    (cache / "injected.pyc").write_bytes(b"not-a-cache")


def mutate_result(root: Path, output: Path) -> None:
    path = output / "results" / "evaluator_m.json"
    value = load(path)
    value["payload"]["candidate_id"] = "SD-C48-MUTATED"
    write(path, value)
    rehash_ledger(output, "results/evaluator_m.json")


def mutate_report(root: Path, output: Path) -> None:
    path = output / "reports" / "EXPERIMENT_REPORT.md"
    path.write_bytes(path.read_bytes() + b"Finite cutoffs prove every endpoint.\n")
    rehash_ledger(output, "reports/EXPERIMENT_REPORT.md")


def mutate_route(root: Path, output: Path) -> None:
    path = output / "evaluations" / "route_a" / "SD-C48" / "2026-08-18.yaml"
    value = load(path)
    value["overall_verdict"] = "ROUTE_A_ACCEPTED"
    write(path, value)


def mutate_integrity(root: Path, output: Path) -> None:
    path = output / "audits" / "integrity_audit.json"
    value = load(path)
    value["payload"]["checks_passed"] = 999
    write(path, value)


def mutate_packet(root: Path, output: Path) -> None:
    path = output / "data" / "source_packet.json"
    value = load(path)
    value["payload"]["preauthority_manifest_sha256"] = "0" * 64
    write(path, value)
    rehash_ledger(output, "data/source_packet.json")


def coordinated_evaluator_edit(output: Path, edit: Callable[[dict[str, Any]], None]) -> None:
    values: dict[str, dict[str, Any]] = {}
    for name in ["evaluator_m", "evaluator_c"]:
        path = output / "results" / f"{name}.json"
        value = load(path)
        edit(value)
        write(path, value)
        rehash_ledger(output, f"results/{name}.json")
        values[name] = value
    left = {key: item for key, item in values["evaluator_m"]["payload"].items()
            if key != "implementation_lane"}
    right = {key: item for key, item in values["evaluator_c"]["payload"].items()
             if key != "implementation_lane"}
    if left != right:
        raise ValueError("coordinated evaluator edit diverged")
    comparison_path = output / "results" / "exact_comparison.json"
    comparison = load(comparison_path)
    comparison["payload"]["science_projection_sha256"] = hashlib.sha256(canonical(left)).hexdigest()
    write(comparison_path, comparison)
    rehash_ledger(output, "results/exact_comparison.json")


def mutate_nested_count_bool(root: Path, output: Path) -> None:
    def edit(value: dict[str, Any]) -> None:
        target = value["payload"]["cycle_certificate"]["length_records"][0]
        if type(target["solution_count"]) is not int or target["solution_count"] != 6:
            raise ValueError("unexpected count fixture")
        target["solution_count"] = True
    coordinated_evaluator_edit(output, edit)


def mutate_nested_cutoff_float(root: Path, output: Path) -> None:
    def edit(value: dict[str, Any]) -> None:
        target = value["payload"]["structural_certificate"]["records"][0]
        if type(target["cutoff"]) is not int or target["cutoff"] != 8:
            raise ValueError("unexpected cutoff fixture")
        target["cutoff"] = 8.0
    coordinated_evaluator_edit(output, edit)


def mutate_comparison_boolean_int(root: Path, output: Path) -> None:
    path = output / "results" / "exact_comparison.json"
    value = load(path)
    if type(value["payload"]["strict_recursive_type_and_value_equal"]) is not bool:
        raise ValueError("unexpected comparison boolean")
    value["payload"]["strict_recursive_type_and_value_equal"] = 1
    write(path, value)
    rehash_ledger(output, "results/exact_comparison.json")


MUTATORS: list[Callable[[Path, Path], None]] = [
    mutate_static, mutate_delete, mutate_extra, mutate_symlink, mutate_cache,
    mutate_result, mutate_report, mutate_route, mutate_integrity, mutate_packet,
    mutate_nested_count_bool, mutate_nested_cutoff_float, mutate_comparison_boolean_int,
]


def run_consumer(consumer: str, root: Path, output: Path, state: str, cwd: Path,
                 hostile: Path) -> subprocess.CompletedProcess[bytes]:
    commands = {
        "X": ("code/comparator/exact_compare.py",
              ["--output-root", str(output), "--mode", "audit-existing"]),
        "T": ("code/auditors/type_auditor.py", ["--output-root", str(output)]),
        "G": ("code/integration/audit_integrity.py",
              ["--root", str(root), "--output-root", str(output), "--state", state,
               "--phase", "audit-existing"]),
        "F": ("external_auditor/frozen_auditor.py",
              ["--root", str(root), "--output-root", str(output), "--state", state]),
    }
    if consumer not in commands:
        raise ValueError("unbound physical consumer")
    relative, arguments = commands[consumer]
    script = root.joinpath(*relative.split("/"))
    if script.is_symlink() or not script.is_file() or root not in script.resolve(strict=True).parents:
        raise ValueError("unsafe physical consumer path")
    environment = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                   "PYTHONPATH": str(hostile), "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run([sys.executable, "-I", "-B", str(script), *arguments],
                          cwd=cwd, env=environment, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=False)


def exact_receipt(process: subprocess.CompletedProcess[bytes],
                  contract: dict[str, Any]) -> bool:
    try:
        envelope = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
    except Exception:
        return False
    return process.returncode == contract["exit"] \
        and len(process.stderr) == contract["stderr_bytes"] \
        and process.stdout == canonical(envelope) \
        and envelope == contract["stdout"]


def base_pass(process: subprocess.CompletedProcess[bytes]) -> bool:
    try:
        envelope = json.loads(process.stdout.decode("ascii"), object_pairs_hook=unique)
    except Exception:
        return False
    return process.returncode == 0 and process.stderr == b"" \
        and process.stdout == canonical(envelope) and envelope.get("status") == "PASS"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", action="store_true")
    parser.add_argument("--root")
    parser.add_argument("--output-root")
    parser.add_argument("--state", choices=["A", "B"])
    parser.add_argument("--scratch")
    args = parser.parse_args()
    if args.template:
        sys.stdout.buffer.write(canonical(summary()))
        return 0
    if not all([args.root, args.output_root, args.state, args.scratch]):
        raise ValueError("execution arguments required")
    root, output, scratch = Path(args.root), Path(args.output_root), Path(args.scratch)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir() \
            or not output.is_absolute() or output.is_symlink() or not output.is_dir() \
            or not scratch.is_absolute() or scratch.exists() or scratch.is_symlink():
        raise ValueError("unsafe roots")
    root, output = root.resolve(strict=True), output.resolve(strict=True)
    scratch.mkdir(parents=True)
    unrelated = scratch / "unrelated_cwd"
    hostile = scratch / "hostile_modules"
    unrelated.mkdir()
    hostile.mkdir()
    (hostile / "json.py").write_text("raise RuntimeError('hostile json imported')\n", encoding="ascii")
    contracts = physical_contracts()
    base_results = {consumer: run_consumer(consumer, root, output, args.state, unrelated, hostile)
                    for consumer in ["X", "T", "G", "F"]}
    if not all(base_pass(process) for process in base_results.values()):
        raise ValueError("base consumer audit did not pass")
    observed: list[dict[str, Any]] = []
    accepted_cases = 0
    accepted_outcomes = 0
    for case, mutator in zip(contracts, MUTATORS):
        identifier = case["case_id"]
        clone = scratch / identifier.lower()
        def ignore_existing_outputs(directory: str, names: list[str]) -> list[str]:
            return ["outputs"] if Path(directory).resolve() == root and "outputs" in names else []
        shutil.copytree(root, clone, symlinks=True, ignore=ignore_existing_outputs)
        clone_output = clone / "outputs"
        if clone_output.exists():
            raise ValueError("canonical root unexpectedly contains outputs")
        shutil.copytree(output, clone_output, symlinks=True)
        mutator(clone, clone_output)
        receipt_rows: list[dict[str, Any]] = []
        case_exact = True
        for consumer in case["consumers"]:
            process = run_consumer(consumer, clone, clone_output, args.state, unrelated, hostile)
            receipt_contract = case["expected_receipts"][consumer]
            exact = exact_receipt(process, receipt_contract)
            accepted_outcomes += int(not exact)
            case_exact = case_exact and exact
            receipt_rows.append(receipt_summary(consumer, receipt_contract, exact))
        accepted_cases += int(not case_exact)
        observed.append({
            "case_id": identifier,
            "consumer_receipts": receipt_rows,
            "exact_rejection": case_exact,
            "expected_code": next(iter(case["expected_receipts"].values()))
            ["stdout"]["payload"]["code"],
        })
    result = {
        "payload": {
            "accepted_consumer_outcome_count": accepted_outcomes,
            "accepted_mutation_count": accepted_cases,
            "base_consumer_audits_passed": True,
            "base_external_audit_passed": True,
            "cases": observed,
            "physical_consumer_invocation_count": sum(len(case["consumers"])
                                                       for case in contracts),
            "physical_mutated_clone_count": len(observed),
        },
        "schema": "paper46-external-auditor-mutations-v1",
        "status": "PASS" if accepted_cases == 0 and accepted_outcomes == 0 else "FAIL",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0 if accepted_cases == 0 and accepted_outcomes == 0 and result == summary() else 1


if __name__ == "__main__":
    raise SystemExit(main())
