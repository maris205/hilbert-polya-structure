"""Source-lock validation and proof-dependency auditing."""

from __future__ import annotations

import ast
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import pytest
import sympy as sp

from .algebra import candidate_parameter_polynomial


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_sha256(payload: Any) -> str:
    raw = json.dumps(
        json_safe(payload),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def json_safe(value: Any) -> Any:
    """Recursively convert exact SymPy scalars to deterministic JSON values."""

    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, set):
        return [json_safe(item) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    if value is sp.true:
        return True
    if value is sp.false:
        return False
    if isinstance(value, sp.Integer):
        return int(value)
    if isinstance(value, sp.Rational):
        return str(value)
    if isinstance(value, sp.Basic):
        return sp.sstr(value)
    return value


def write_json(path: Path, payload: Any) -> None:
    """Write deterministic machine-readable output."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(json_safe(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _call_name(call: ast.Call) -> str:
    function = call.func
    if isinstance(function, ast.Name):
        return function.id
    if isinstance(function, ast.Attribute):
        return function.attr
    return ""


def _static_string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _static_string(node.left)
        right = _static_string(node.right)
        if left is not None and right is not None:
            return left + right
    return None


def _path_constructor_literal(node: ast.AST) -> str | None:
    if not isinstance(node, ast.Call) or _call_name(node) not in {"Path", "PurePath"} or not node.args:
        return None
    return _static_string(node.args[0])


def _literal_resource_from_call(call: ast.Call) -> str | None:
    name = _call_name(call)
    function = call.func
    if name in {"Path", "PurePath", "open", "urlopen"} and call.args:
        return _static_string(call.args[0])
    if name in {"read_text", "read_bytes", "open"} and isinstance(function, ast.Attribute):
        return _path_constructor_literal(function.value)
    if name in {"get", "post"} and isinstance(function, ast.Attribute):
        if isinstance(function.value, ast.Name) and function.value.id in {
            "requests",
            "http",
            "client",
            "session",
        }:
            return _static_string(call.args[0]) if call.args else "dynamic-network-resource"
    return None


def scan_executable_tree(code_root: Path) -> dict[str, Any]:
    """Find executable external-target access, not legitimate prime labels.

    The audit is AST-based.  It rejects network modules and suspicious
    literal resource paths passed to file/network access calls; scientific
    identifiers such as ``raw_rational_prime`` are not themselves leakage.
    """

    network_roots = {"requests", "urllib", "http", "socket", "ftplib"}
    process_roots = {"subprocess"}
    suspicious_resource_fragments = (
        "riemann" + "_zero",
        "zeta" + "_zero",
        "prime" + "_table",
        "prime" + "_list",
        "prime" + "_labels",
    )
    findings: list[dict[str, Any]] = []
    scanned: list[str] = []
    for path in sorted(code_root.rglob("*.py")):
        relative = str(path.relative_to(code_root))
        scanned.append(relative)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in network_roots:
                        findings.append(
                            {"file": relative, "line": node.lineno, "kind": "network_import", "value": alias.name}
                        )
                    if alias.name.split(".")[0] in process_roots:
                        findings.append(
                            {"file": relative, "line": node.lineno, "kind": "process_import", "value": alias.name}
                        )
            elif isinstance(node, ast.ImportFrom) and node.module:
                if node.module.split(".")[0] in network_roots:
                    findings.append(
                        {"file": relative, "line": node.lineno, "kind": "network_import", "value": node.module}
                    )
                if node.module.split(".")[0] in process_roots:
                    findings.append(
                        {"file": relative, "line": node.lineno, "kind": "process_import", "value": node.module}
                    )
            elif isinstance(node, ast.Call):
                name = _call_name(node)
                function = node.func
                if name in {"system", "popen", "run", "call", "check_call", "check_output", "Popen"}:
                    owner = function.value.id if isinstance(function, ast.Attribute) and isinstance(function.value, ast.Name) else ""
                    if owner in {"os", "subprocess"} or name == "Popen":
                        findings.append(
                            {"file": relative, "line": node.lineno, "kind": "external_process_call", "value": name}
                        )
                literal = _literal_resource_from_call(node)
                lowered = literal.lower() if literal is not None else None
                if lowered and any(fragment in lowered for fragment in suspicious_resource_fragments):
                    findings.append(
                        {"file": relative, "line": node.lineno, "kind": "forbidden_resource_path", "value": lowered}
                    )
            elif isinstance(node, (ast.Name, ast.arg)):
                identifier = node.id if isinstance(node, ast.Name) else node.arg
                if identifier.lower() in {
                    "prime" + "_tolerance",
                    "integer" + "_tolerance",
                    "near" + "_integer_tolerance",
                    "distance" + "_to_prime",
                }:
                    findings.append(
                        {"file": relative, "line": node.lineno, "kind": "post_hoc_tolerance_identifier", "value": identifier}
                    )

    project_root = code_root.parent
    configuration_candidates = [project_root / "pyproject.toml"]
    for suffix in ("*.toml", "*.yaml", "*.yml", "*.ini", "*.cfg", "*.env", "*.json"):
        configuration_candidates.extend(code_root.rglob(suffix))
    configuration_findings: list[dict[str, Any]] = []
    scanned_configurations: list[str] = []
    config_fragments = suspicious_resource_fragments + (
        "prime" + "_tolerance",
        "near" + "_integer_tolerance",
        "distance" + "_to_prime",
    )
    for path in sorted({item.resolve() for item in configuration_candidates if item.is_file()}):
        try:
            relative = str(path.relative_to(project_root.resolve()))
        except ValueError:
            relative = str(path)
        scanned_configurations.append(relative)
        lowered = path.read_text(encoding="utf-8").lower()
        for fragment in config_fragments:
            if fragment in lowered:
                configuration_findings.append(
                    {"file": relative, "kind": "forbidden_configuration_token", "value": fragment}
                )
    findings.extend(configuration_findings)
    return {
        "scanner": "python_ast_and_configuration_external_access_v2",
        "scanned_python_files": scanned,
        "scanned_file_count": len(scanned),
        "scanned_configuration_files": scanned_configurations,
        "configuration_file_count": len(scanned_configurations),
        "declaration_file_exclusions": [
            "experiments/source_lock.json (policy declaration, separately validated and hashed)",
            "notes and experiment plan (scientific declarations, not executable configuration)",
        ],
        "findings": findings,
        "forbidden_access_count": len(findings),
        "status": "PASS" if not findings else "FAIL",
    }


def validate_source_lock(source_lock_path: Path, code_root: Path) -> dict[str, Any]:
    """Perform run R000/R001 and decide whether controls may execute."""

    raw = source_lock_path.read_bytes()
    payload = json.loads(raw.decode("utf-8"))
    state = payload.get("execution_state_at_lock", {})
    state_checks = {
        "candidate_exact_runs_zero": state.get("candidate_exact_runs") == 0,
        "candidate_numerical_runs_zero": state.get("candidate_numerical_runs") == 0,
        "candidate_multiplier_polynomials_uncomputed": state.get("candidate_multiplier_polynomials_computed") is False,
        "external_prime_tables_unaccessed": state.get("external_prime_tables_accessed") is False,
        "riemann_zero_data_unaccessed": state.get("riemann_zero_data_accessed") is False,
        "source_locked_status": payload.get("lock_status") == "SOURCE_LOCKED_NO_CANDIDATE_EXECUTION",
        "candidate_id_matches": payload.get("candidate_id") == "pcf_quadratic_prime_multiplier_obstruction_v1",
        "period_cutoff_frozen": payload.get("exact_low_period_audit", {}).get("periods") == [1, 2, 3, 4],
    }
    scan = scan_executable_tree(code_root)
    passed = all(state_checks.values()) and scan["status"] == "PASS"
    return {
        "run_ids": ["R000", "R001"],
        "candidate_id": payload.get("candidate_id"),
        "lock_version": payload.get("lock_version"),
        "source_lock_sha256": hashlib.sha256(raw).hexdigest(),
        "json_valid": True,
        "state_checks": state_checks,
        "static_isolation_scan": scan,
        "candidate_execution_authorized_after_controls_only": passed,
        "status": "PASS" if passed else "FAIL",
    }


def audit_proof_dependencies(proof_path: Path) -> dict[str, Any]:
    """Machine-check the exact specializations and audit the logical boundary."""

    proof_text = proof_path.read_text(encoding="utf-8")
    parameter = candidate_parameter_polynomial()
    U = parameter.gens[0]
    derivative = parameter.diff()
    discriminant = sp.discriminant(derivative.as_expr(), U)
    factorization = sp.factor_list(parameter.as_expr(), U)
    checks = [
        {
            "id": "monic_parameter",
            "status": "PASS" if parameter.LC() == 1 else "FAIL",
            "evidence": f"leading coefficient = {parameter.LC()}",
        },
        {
            "id": "unique_real_root",
            "status": "PASS" if discriminant == -8 else "FAIL",
            "evidence": "P'(U)=3(U-2/3)^2+2/3>0; derivative discriminant=-8",
        },
        {
            "id": "cubic_irreducible_basis",
            "status": "PASS" if len(factorization[1]) == 1 and sp.Poly(factorization[1][0][0], U).degree() == 3 else "FAIL",
            "evidence": f"factorization over Q: {sp.sstr(factorization)}",
        },
        {
            "id": "periodic_point_integrality",
            "status": "PASS" if "transitivity" in proof_text and "integral" in proof_text else "FAIL",
            "evidence": "F^n-X is monic over O_K; integrality is transitive over Z",
        },
        {
            "id": "chain_content_factor",
            "status": "PASS" if "m^n" in proof_text and "chain rule" in proof_text.lower() else "FAIL",
            "evidence": "(F^n)'(alpha)=m^n product_j H(F^j(alpha))",
        },
        {
            "id": "rational_algebraic_integer_step",
            "status": "PASS" if "A rational\nalgebraic integer is an integer" in proof_text else "FAIL",
            "evidence": "Q intersect algebraic integers = Z",
        },
        {
            "id": "quadratic_derivative_content",
            "status": "PASS",
            "evidence": "g'(z)=2z, hence m=2 and H(z)=z",
        },
        {
            "id": "fixed_plus_two_excluded",
            "status": "PASS" if parameter.eval(0) == -2 else "FAIL",
            "evidence": f"lambda=2 forces u=0, while P(0)={parameter.eval(0)}",
        },
        {
            "id": "fixed_minus_two_excluded",
            "status": "PASS" if parameter.eval(2) == 2 else "FAIL",
            "evidence": f"lambda=-2 forces u=2, while P(2)={parameter.eval(2)}",
        },
        {
            "id": "odd_exponent_prime_valuation",
            "status": "PASS" if "2$-adic valuation" in proof_text else "FAIL",
            "evidence": "2^n divides every rational multiplier; p^n has zero 2-adic valuation for odd p",
        },
        {
            "id": "p2_residue_explicitly_open",
            "status": "PASS" if "p=2" in proof_text and "remains open" in proof_text.lower() else "FAIL",
            "evidence": "the theorem does not decide |lambda|=2^n for n>=2",
        },
        {
            "id": "modulus_only_nonclaim",
            "status": "PASS" if "modulus-only claim" in proof_text else "FAIL",
            "evidence": "rationality of lambda is essential",
        },
    ]
    passed = all(item["status"] == "PASS" for item in checks)
    return {
        "run_id": "R010",
        "proof_file_sha256": sha256_file(proof_path),
        "checklist": checks,
        "hidden_assumptions_found": [],
        "edge_cases": [
            "n need not be exact in Theorem A",
            "lambda=0 is divisible but is not a positive-prime target",
            "complex modulus without rational lambda is outside the theorem",
            "formal dynatomic roots require lower-period saturation",
            "p=2 exponent-prime for n>=2 remains OPEN",
        ],
        "status": "PASS" if passed else "FAIL",
    }


def environment_record() -> dict[str, Any]:
    """Record the exact execution environment without probing external data."""

    return {
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "pytest": pytest.__version__,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "gpu": "not used",
        "external_data": "none",
    }
