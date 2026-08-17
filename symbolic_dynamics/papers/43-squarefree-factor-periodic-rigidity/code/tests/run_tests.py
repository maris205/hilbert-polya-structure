#!/usr/bin/env python3
"""Cold static and optional post-output test suite for Paper 43."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


PYTHON = sys.executable
LOCAL_NAMES = {
    "source_core", "emit_packet", "lint_packet", "evaluate_packet",
    "independent_evaluator", "evaluate_route_a", "validate_route_a",
    "audit_route_a", "run_mutations", "run_integration", "audit_integrity",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate key: {key}")
        output[key] = value
    return output


def invoke(script: Path, arguments: list[str], cwd: Path) -> bytes:
    process = subprocess.run(
        [PYTHON, "-I", "-B", str(script), *arguments], cwd=cwd,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
             "PYTHONPATH": "/hostile/shadow"},
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if process.returncode != 0:
        detail = process.stderr.decode("utf-8", errors="replace").splitlines()[-3:]
        raise ValueError(f"test subprocess failed: {script.name}: {detail}")
    return process.stdout


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module.split(".")[0])
    return modules


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("run_tests.py requires python3 -I -B")
    if len(argv) not in (1, 2) or (len(argv) == 2 and argv[1] != "--post-output"):
        raise SystemExit("usage: run_tests.py ROOT [--post-output]")
    root = Path(argv[0]).resolve()
    checks: dict[str, bool] = {}
    with tempfile.TemporaryDirectory(prefix="paper43_tests_") as temporary_name:
        temporary = Path(temporary_name)
        cwd = temporary / "unrelated_cwd"
        cwd.mkdir()
        audit = json.loads(invoke(root / "code/integration/audit_integrity.py",
                                  [str(root), "--static-only"], cwd),
                           object_pairs_hook=unique)
        checks["static_integrity"] = (
            audit["status"] == "PASS"
            and audit["authority_overlay_state"] == "CANDIDATE_NO_OVERLAY"
            and audit["checks"]["authority_overlay_state_valid"] is True
        )
        packet = invoke(root / "code/source/emit_packet.py", [], cwd)
        packet_path = temporary / "packet.json"
        packet_path.write_bytes(packet)
        lint = json.loads(invoke(root / "code/source/lint_packet.py", [str(packet_path)], cwd),
                          object_pairs_hook=unique)
        checks["packet_lint"] = lint["status"] == "PASS"
        main_raw = invoke(root / "code/evaluator/evaluate_packet.py", [str(packet_path)], cwd)
        independent_raw = invoke(root / "code/evaluator/independent_evaluator.py",
                                 [str(packet_path)], cwd)
        main = json.loads(main_raw, object_pairs_hook=unique)
        independent = json.loads(independent_raw, object_pairs_hook=unique)
        checks["main_evaluator"] = main["checks_passed"] == main["checks_total"]
        checks["independent_evaluator"] = (
            independent["checks_passed"] == independent["checks_total"])
        science_raw = canonical(main["science"])
        checks["science_byte_identity"] = (
            main["science"] == independent["science"]
            and hashlib.sha256(science_raw).hexdigest() == main["science_sha256"]
            and main["science_sha256"] == independent["science_sha256"]
        )
        science_path = temporary / "science.json"
        science_path.write_bytes(science_raw)
        route_raw = invoke(root / "code/evaluator/evaluate_route_a.py", [str(science_path)], cwd)
        route_path = temporary / "route.yaml"
        route_path.write_bytes(route_raw)
        route_main = json.loads(invoke(root / "code/route/validate_route_a.py",
                                       [str(route_path), str(science_path)], cwd),
                                object_pairs_hook=unique)
        route_independent = json.loads(invoke(root / "code/route/audit_route_a.py",
                                              [str(route_path), str(science_path)], cwd),
                                       object_pairs_hook=unique)
        checks["strict_route"] = route_main["status"] == "PASS"
        checks["independent_route"] = route_independent["status"] == "PASS"
        checks["route_normalized_identity"] = (
            route_main["normalized_route_sha256"]
            == route_independent["normalized_route_sha256"])
        mutation = json.loads(invoke(root / "code/tests/run_mutations.py", [
            str(packet_path), str(science_path), str(route_path)
        ], cwd), object_pairs_hook=unique)
        mutation_contracts = sorted([
            {key: row[key] for key in (
                "class_id", "designated_consumers", "domain", "expectation",
                "id", "variant")}
            for row in mutation["records"] + mutation["positive_controls"]
        ], key=lambda row: row["id"])
        checks["mutation_classes_exact"] = (
            mutation["classes_registered"] == 62
            and mutation["classes_missing"] == [
                "output_tamper", "provenance_state_a", "provenance_state_b",
                "result_ledger", "result_set", "run_a_b_c", "science_hash",
                "stage_2_scope",
            ])
        checks["mutation_zero_survivors"] = (
            mutation["status"] == "PASS" and mutation["survivor_count"] == 0
            and mutation["positive_control_failure_count"] == 0)
        checks["mutation_per_instance_consumer_matrix"] = (
            mutation["phase"] == "PREFLIGHT_BASELINE"
            and all(sorted(row["outcomes"]) == row["designated_consumers"]
                    for row in mutation["records"] + mutation["positive_controls"])
            and all(set(row["outcomes"].values()) == {"REJECT_NONZERO"}
                    for row in mutation["records"])
            and hashlib.sha256(canonical(mutation_contracts)).hexdigest()
                    == mutation["instance_contracts_sha256"])
    algorithm_c_imports = imported_modules(root / "code/evaluator/evaluate_packet.py")
    algorithm_f_imports = imported_modules(root / "code/evaluator/independent_evaluator.py")
    checks["algorithm_import_graph_separate"] = (
        not (algorithm_c_imports | algorithm_f_imports) & LOCAL_NAMES)
    checks["algorithm_sources_distinct"] = (
        (root / "code/evaluator/evaluate_packet.py").read_bytes()
        != (root / "code/evaluator/independent_evaluator.py").read_bytes())
    expected = json.loads((root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(
        encoding="ascii"))["exact_output_paths"]
    checks["exact_output_contract"] = (
        len(expected) == 53 and expected == sorted(expected)
        and len(expected) == len(set(expected)))
    if len(argv) == 2:
        post = json.loads(invoke(root / "code/integration/audit_integrity.py",
                                 [str(root), "--state", "A"], root.parent),
                          object_pairs_hook=unique)
        checks["post_output_integrity"] = post["status"] == "PASS"
    else:
        present = []
        for relative in expected:
            if (root / relative).exists():
                present.append(relative)
        checks["preoutput_namespace_empty"] = not present
    failed = sorted(key for key, value in checks.items() if not value)
    result = {
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "failure_count": len(failed),
        "failures": failed,
        "schema": "paper43-integration-test-report-v1",
        "status": "PASS" if not failed else "FAIL",
    }
    sys.stdout.buffer.write(canonical(result))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
