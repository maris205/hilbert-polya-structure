#!/usr/bin/env python3
"""Strict JSON/runtime type and unassigned-Route audit."""

from __future__ import annotations

import sys

if not sys.flags.isolated or not sys.flags.dont_write_bytecode:
    sys.stdout.buffer.write(b'{\n  "payload": {\n    "code": "REJECT_TYPE_CONTRACT"\n  },\n  "schema": "stage0-type-audit-v1",\n  "status": "REJECT"\n}\n')
    raise SystemExit(2)

import argparse
import importlib.util
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def unique(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate JSON key")
        return dict(pairs)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def strict_scalars(value: Any) -> int:
    if value is None or type(value) in (str, bool, int):
        return 1
    if type(value) is list:
        return 1 + sum(strict_scalars(item) for item in value)
    if type(value) is dict and all(type(key) is str for key in value):
        return 1 + sum(strict_scalars(item) for item in value.values())
    raise AssertionError("forbidden JSON runtime type")


def load_science_validator(root: Path) -> Any:
    path = root / "code" / "auditors" / "result_schema.py"
    specification = importlib.util.spec_from_file_location("stage0_result_schema", path)
    if specification is None or specification.loader is None:
        raise AssertionError("result validator loader")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module.validate_science


def probe(script: Path, root: Path, state: str) -> dict[str, Any]:
    env = {
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONPATH": "/hostile/stage0",
    }
    run = subprocess.run([sys.executable, "-I", "-B", str(script), "--root", str(root), "--state", state], cwd="/", env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=60)
    if run.returncode != 2 or run.stderr or run.stdout != canonical({"payload": {"code": "REJECT_STATE"}, "schema": "stage0-error-v1", "status": "REJECT"}):
        raise AssertionError("invalid-state probe")
    return {"exit": run.returncode, "script": script.relative_to(root).as_posix(), "status": "REJECT_STATE"}


def science_probe(script: Path, root: Path, validator: Any, result_schema: dict[str, Any], contract: dict[str, Any], cases: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    env = {
        "LANG": "C", "LC_ALL": "C", "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "PYTHONPATH": "/hostile/stage0",
    }
    run = subprocess.run([sys.executable, "-I", "-B", str(script), "--root", str(root), "--state", "A"], cwd="/", env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=60)
    if run.returncode != 0 or run.stderr:
        raise AssertionError("science probe process")

    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        if len(pairs) != len({key for key, _ in pairs}):
            raise ValueError("duplicate science key")
        return dict(pairs)

    envelope = json.loads(run.stdout.decode("ascii"), object_pairs_hook=hook)
    if canonical(envelope) != run.stdout:
        raise AssertionError("science canonical bytes")
    nodes = validator(result_schema, contract, cases, envelope)
    return envelope, {"consumer": script.relative_to(root).as_posix(), "runtime_nodes_validated": nodes, "status": "PASS"}


def must_reject_schema(validator: Any, result_schema: dict[str, Any], contract: dict[str, Any], cases: dict[str, Any], envelope: dict[str, Any]) -> None:
    try:
        validator(result_schema, contract, cases, envelope)
    except (AssertionError, KeyError, TypeError, ValueError):
        return
    raise AssertionError("schema negative control survived")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    try:
        contract = unique(root / "contracts" / "PROJECT_CONTRACT.json")
        result_schema = unique(root / "contracts" / "RESULT_SCHEMA.json")
        cases = unique(root / "contracts" / "STATE_A_CASES.json")
        mutations = unique(root / "contracts" / "MUTATION_REGISTRY.json")
        route = unique(root / "contracts" / "ROUTE_EXPECTATION.json")
        scalar_nodes = sum(strict_scalars(value) for value in (contract, result_schema, cases, mutations, route))
        if contract["status"] != "HOLD_FOR_FRESH_INDEPENDENT_PRE_RUN_REAUDIT" or contract["state"] != "A" or contract["finite_checks_are_proof"] is not False:
            raise AssertionError("contract state")
        if (root / "STATUS.txt").read_text(encoding="ascii") != "HOLD_FOR_FRESH_INDEPENDENT_PRE_RUN_REAUDIT\n":
            raise AssertionError("status file")
        if contract["route"] != {"assigned": False, "id": None} or route["candidate_id"] is not None or route["candidate_id_assigned"] is not False or route["installation_authorized"] is not False:
            raise AssertionError("route typing")
        paper_number = contract["paper_number"]
        slug = contract["project_slug"]
        if (type(paper_number) is not int or not slug.startswith(f"{paper_number}-")
                or contract["schema"] != f"p{paper_number}-stage0-project-contract-v1"
                or cases["schema"] != f"p{paper_number}-stage0-state-a-cases-v1"
                or mutations["schema"] != f"p{paper_number}-stage0-mutation-registry-v1"
                or result_schema["schema"] != "stage0-result-schema-v1"
                or route["schema"] != "stage0-route-expectation-v1"
                or route["paper_number"] != paper_number or route["slug"] != slug
                or route["expected_authority_relative_path"] != f"symbolic_dynamics/papers/{slug}"):
            raise AssertionError("paper identity binding")
        if cases["state"] != "A" or cases["project_slug"] != contract["project_slug"] or mutations["project_slug"] != contract["project_slug"]:
            raise AssertionError("contract binding")
        expected_science_schema = f"p{contract['paper_number']}-stage0-science-v1"
        if result_schema["science_schema"] != expected_science_schema:
            raise AssertionError("science schema")
        cross_paper_schema = f"p{50 if contract['paper_number'] == 49 else 49}-stage0-science-v1"
        if cross_paper_schema == expected_science_schema or cross_paper_schema == result_schema["science_schema"]:
            raise AssertionError("cross-paper schema negative control")
        route_scan_file_count = 0
        for path in root.rglob("*"):
            relative = path.relative_to(root).as_posix()
            if relative == "outputs" or relative.startswith("outputs/"):
                continue
            if re.search(r"SD-C[0-9]+", relative):
                raise AssertionError("invented candidate id path")
            if path.is_file() and not path.is_symlink():
                route_scan_file_count += 1
                text = path.read_text(encoding="utf-8", errors="ignore")
                if re.search(r"SD-C[0-9]+", text):
                    raise AssertionError("invented candidate id")
        probes = [
            probe(root / "code" / "engines" / "production.py", root, "B"),
            probe(root / "code" / "audit" / "independent_science.py", root, "B"),
        ]
        validator = load_science_validator(root)
        science_results = [
            science_probe(root / "code" / "engines" / "production.py", root, validator, result_schema, contract, cases),
            science_probe(root / "code" / "audit" / "independent_science.py", root, validator, result_schema, contract, cases),
        ]
        baseline = science_results[0][0]
        wrong_label = json.loads(json.dumps(baseline))
        wrong_label["schema"] = cross_paper_schema
        must_reject_schema(validator, result_schema, contract, cases, wrong_label)
        unknown_field = json.loads(json.dumps(baseline))
        unknown_field["payload"]["cases"][0]["result"]["__unknown__"] = None
        must_reject_schema(validator, result_schema, contract, cases, unknown_field)
        missing_field = json.loads(json.dumps(baseline))
        missing_field["payload"]["cases"][0]["result"].pop(next(iter(missing_field["payload"]["cases"][0]["result"])))
        must_reject_schema(validator, result_schema, contract, cases, missing_field)
        malformed_integer_list = json.loads(json.dumps(baseline))
        malformed_integer_list["payload"]["cases"][0]["result"]["records"][0]["directive"] = [True]
        must_reject_schema(validator, result_schema, contract, cases, malformed_integer_list)
        malformed_deep_record = json.loads(json.dumps(baseline))
        malformed_deep_record["payload"]["cases"][0]["result"]["records"][0]["values"] = [0]
        must_reject_schema(validator, result_schema, contract, cases, malformed_deep_record)
        malformed_integer_scalar = json.loads(json.dumps(baseline))
        composite = next(case for case in malformed_integer_scalar["payload"]["cases"] if case["kind"] == "composite_counterperiod")
        composite["result"]["checked_equalities"] = True
        must_reject_schema(validator, result_schema, contract, cases, malformed_integer_scalar)
        output = {"payload": {"case_count": len(cases["cases"]), "deep_result_schema_negative_controls": ["boolean_as_integer", "cross_paper_label", "malformed_deep_record", "malformed_integer_list", "missing_field", "unknown_field"], "expected_science_schema": expected_science_schema, "mutation_count": len(mutations["mutations"]), "route_id_assigned": False, "route_id_tree_scan_file_count": route_scan_file_count, "scalar_nodes_checked": scalar_nodes, "science_schema_probes": [record for _, record in science_results], "state_rejection_probes": probes}, "schema": "stage0-type-audit-v1", "status": "PASS"}
        sys.stdout.buffer.write(canonical(output))
        return 0
    except (AssertionError, KeyError, OSError, TypeError, ValueError, json.JSONDecodeError, subprocess.SubprocessError):
        sys.stdout.buffer.write(canonical({"payload": {"code": "REJECT_TYPE_CONTRACT"}, "schema": "stage0-type-audit-v1", "status": "REJECT"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
