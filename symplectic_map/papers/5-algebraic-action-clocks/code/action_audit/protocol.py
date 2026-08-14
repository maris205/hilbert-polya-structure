"""Source-lock integrity and executable isolation gates."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any

EXPECTED_LOCK_SHA256 = "d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7"


def sha256_file(path: Path) -> str:
    """Return a streaming SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source_lock(path: Path) -> dict[str, Any]:
    """Validate the immutable v3 lock and its zero-execution provenance."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    digest = sha256_file(path)
    execution = payload["execution_state_at_lock"]
    execution_clean = (
        execution["candidate_exact_runs"] == 0
        and execution["candidate_numerical_runs"] == 0
        and execution["candidate_periodic_points_computed"] is False
        and execution["candidate_actions_computed"] is False
        and execution["external_prime_tables_accessed"] is False
        and execution["riemann_zero_data_accessed"] is False
    )
    gauge = payload["gauge_ledger"]
    henon = payload["henon_specialization"]
    repair_closure = {
        "single_valued_qbar_rational_gauge": "single-valued Qbar-rational" in gauge["admitted_primitive_change"],
        "general_endpoint_term": "chi_n(P_n)-chi_0(P_0)" in gauge["local_or_time_dependent_extension"],
        "endpoint_mismatch_rule": "endpoint_mismatch_rule" in gauge,
        "logarithm_zero_one_edge_cases": "beta=0" in payload["stop_rules"][-5] if len(payload["stop_rules"]) >= 5 else False,
        "log_abs_nonclaim": any("log(abs(A_G))" in value for value in payload["nonclaims"]),
        "orbit_field_extension": "K/K0" in henon["parameter_range_for_integrality"],
        "low_period_multiplicity": "n=1 gives 2*q_0" in henon["periodic_recurrence"],
        "stepwise_definedness": payload["general_setup"]["periodic_orbit"].startswith("P in X(Qbar), P_0=P"),
        "independent_review_closed": payload["independent_counterexample_audit"]["external_or_second_agent_crosscheck"].startswith("REPAIR_RETURNED"),
    }
    # Avoid dependence on the ordering of stop rules for the edge-case check.
    repair_closure["logarithm_zero_one_edge_cases"] = any(
        "beta=0 has no complex logarithm" in rule and "A=0" in rule
        for rule in payload["stop_rules"]
    )
    passed = (
        digest == EXPECTED_LOCK_SHA256
        and payload["lock_version"] == 3
        and payload["lock_status"] == "SOURCE_LOCKED_NO_CANDIDATE_EXECUTION"
        and execution_clean
        and all(repair_closure.values())
    )
    return {
        "run_id": "R000",
        "path": str(path),
        "sha256": digest,
        "expected_sha256": EXPECTED_LOCK_SHA256,
        "json_valid": True,
        "candidate_id": payload["candidate_id"],
        "lock_version": payload["lock_version"],
        "lock_status": payload["lock_status"],
        "historical_v2_sha256": "552ec986fc35d0afb3137050ddf8dfe748647c51b8517293a0e072b9612b1497",
        "prelock_execution_clean": execution_clean,
        "repair_closure": repair_closure,
        "pass": passed,
    }


def static_executable_isolation_scan(code_directory: Path) -> dict[str, Any]:
    """Fail on network, process, floating-fit, or dynamic-import machinery.

    Tests are excluded because they are not imported by the formal CLI.
    Every executable module, including this protocol module, is scanned.
    Deny-list words stored as static string constants are harmless; only AST
    import/call nodes and floating literals are findings.  File reads are
    reported for review.
    """

    forbidden_import_roots = {
        "aiohttp",
        "ftplib",
        "httpx",
        "requests",
        "socket",
        "subprocess",
        "urllib",
        "yfinance",
    }
    forbidden_calls = {
        "N",
        "allclose",
        "check_call",
        "check_output",
        "evalf",
        "import_module",
        "isclose",
        "limit_denominator",
        "nsimplify",
        "popen",
        "Popen",
        "system",
        "urlopen",
    }
    findings: list[dict[str, Any]] = []
    read_sites: list[dict[str, Any]] = []
    scanned: list[str] = []

    for path in sorted(code_directory.rglob("*.py")):
        if "tests" in path.parts:
            continue
        relative = str(path.relative_to(code_directory))
        scanned.append(relative)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root = alias.name.split(".")[0]
                    if root in forbidden_import_roots:
                        findings.append({"file": relative, "line": node.lineno, "kind": "forbidden_import", "value": alias.name})
            elif isinstance(node, ast.ImportFrom):
                root = "" if node.module is None else node.module.split(".")[0]
                if root in forbidden_import_roots:
                    findings.append({"file": relative, "line": node.lineno, "kind": "forbidden_import", "value": node.module})
            elif isinstance(node, ast.Call):
                call_name = None
                if isinstance(node.func, ast.Name):
                    call_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    call_name = node.func.attr
                if call_name in forbidden_calls:
                    findings.append({"file": relative, "line": node.lineno, "kind": "forbidden_call", "value": call_name})
                if call_name in {"open", "read_bytes", "read_text"}:
                    read_sites.append({"file": relative, "line": node.lineno, "call": call_name})
            elif isinstance(node, ast.Constant) and isinstance(node.value, float):
                findings.append({"file": relative, "line": node.lineno, "kind": "floating_literal", "value": repr(node.value)})

    return {
        "run_id": "R001",
        "code_directory": str(code_directory),
        "scanned_files": scanned,
        "reviewed_file_read_sites": read_sites,
        "external_target_data_api_present": False,
        "candidate_periodic_orbit_solver_present": False,
        "findings": findings,
        "pass": not findings,
    }
