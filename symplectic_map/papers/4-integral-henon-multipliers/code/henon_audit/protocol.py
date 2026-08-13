"""Source-lock validation and target-isolation checks."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path
from typing import Any

EXPECTED_LOCK_SHA256 = "3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source_lock(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    digest = sha256_file(path)
    execution = payload["execution_state_at_lock"]
    prelock_clean = (
        execution["candidate_exact_runs"] == 0
        and execution["candidate_numerical_runs"] == 0
        and not execution["candidate_periodic_points_computed"]
        and not execution["candidate_monodromies_computed"]
        and not execution["external_prime_tables_accessed"]
        and not execution["riemann_zero_data_accessed"]
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
        "prelock_execution_clean": prelock_clean,
        "forbidden_data_rules_count": len(payload["forbidden_data"]),
        "pass": (
            digest == EXPECTED_LOCK_SHA256
            and payload["lock_version"] == 2
            and payload["lock_status"] == "SOURCE_LOCKED_NO_CANDIDATE_EXECUTION"
            and prelock_clean
        ),
    }


def _root_import(module: str | None) -> str:
    return "" if module is None else module.split(".")[0]


def static_target_isolation_scan(code_directory: Path) -> dict[str, Any]:
    """AST-scan executable modules for target-data or network access.

    The scanner itself is excluded because its deny-list constants are not a
    candidate-data dependency.  Tests are likewise outside the executable
    candidate path.
    """

    forbidden_import_roots = {
        "aiohttp",
        "ftplib",
        "importlib",
        "pickle",
        "requests",
        "shelve",
        "subprocess",
        "urllib",
        "httpx",
        "socket",
        "pandas_datareader",
        "yfinance",
    }
    forbidden_call_names = {
        "nearest_prime",
        "load_prime_table",
        "read_prime_table",
        "load_zero_table",
        "read_zero_table",
        "download_zeros",
        "nsimplify",
        "limit_denominator",
        "isclose",
        "allclose",
        "__import__",
        "import_module",
        "system",
        "popen",
        "Popen",
        "check_call",
        "check_output",
    }
    suspicious_path_pattern = re.compile(
        r"(?:riemann|zeta[_ -]?zeros?|nearest[_ -]?prime|"
        r"prime[_ -]?(?:table|list|target|label|file|data)s?|"
        r"zero[_ -]?(?:table|target|file|data)s?)",
        re.IGNORECASE,
    )
    url_pattern = re.compile(r"(?:https?|ftp)://", re.IGNORECASE)
    read_call_names = {
        "open",
        "read_text",
        "read_bytes",
        "load",
        "loads",
        "read_csv",
        "read_json",
    }
    findings: list[dict[str, Any]] = []
    scanned: list[str] = []
    reviewed_file_read_sites: list[dict[str, Any]] = []

    def string_constants(node: ast.AST) -> list[str]:
        return [
            child.value
            for child in ast.walk(node)
            if isinstance(child, ast.Constant) and isinstance(child.value, str)
        ]

    def assignment_names(node: ast.Assign | ast.AnnAssign) -> list[str]:
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        return [child.id for target in targets for child in ast.walk(target) if isinstance(child, ast.Name)]

    def resolve_string_expression(node: ast.AST, aliases: dict[str, str]) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return aliases.get(node.id)
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Div, ast.Add)):
            left = resolve_string_expression(node.left, aliases)
            right = resolve_string_expression(node.right, aliases)
            if left is not None and right is not None:
                separator = "/" if isinstance(node.op, ast.Div) else ""
                return f"{left}{separator}{right}"
        if isinstance(node, ast.Call):
            function_name = None
            if isinstance(node.func, ast.Name):
                function_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                function_name = node.func.attr
            if function_name in {"Path", "PurePath"} and node.args:
                return resolve_string_expression(node.args[0], aliases)
        return None

    def is_abs_call(node: ast.AST) -> bool:
        return (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "abs"
        )

    def float_threshold(node: ast.AST, numeric_aliases: dict[str, float]) -> float | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            return node.value
        if isinstance(node, ast.Name):
            return numeric_aliases.get(node.id)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            value = float_threshold(node.operand, numeric_aliases)
            if value is not None:
                return -value if isinstance(node.op, ast.USub) else value
        return None

    for path in sorted(code_directory.rglob("*.py")):
        if "tests" in path.parts or path.name == "protocol.py":
            continue
        relative = str(path.relative_to(code_directory))
        scanned.append(relative)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        string_aliases: dict[str, str] = {}
        numeric_aliases: dict[str, float] = {}
        assignment_nodes = sorted(
            (
                node
                for node in ast.walk(tree)
                if isinstance(node, (ast.Assign, ast.AnnAssign))
            ),
            key=lambda node: node.lineno,
        )
        # Two passes resolve simple chains such as name -> Path(name).
        for _pass in range(2):
            for assignment in assignment_nodes:
                names = assignment_names(assignment)
                value = assignment.value
                resolved_string = resolve_string_expression(value, string_aliases)
                if resolved_string is not None:
                    for name in names:
                        string_aliases[name] = resolved_string
                if isinstance(value, ast.Constant) and isinstance(value.value, float):
                    for name in names:
                        numeric_aliases[name] = value.value
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root = _root_import(alias.name)
                    if root in forbidden_import_roots:
                        findings.append({"file": relative, "line": node.lineno, "kind": "forbidden_import", "value": alias.name})
            elif isinstance(node, ast.ImportFrom):
                root = _root_import(node.module)
                if root in forbidden_import_roots:
                    findings.append({"file": relative, "line": node.lineno, "kind": "forbidden_import", "value": node.module})
            elif isinstance(node, ast.Call):
                function_name = None
                if isinstance(node.func, ast.Name):
                    function_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    function_name = node.func.attr
                if function_name in forbidden_call_names:
                    findings.append({"file": relative, "line": node.lineno, "kind": "forbidden_call", "value": function_name})
                call_strings = string_constants(node)
                call_strings.extend(
                    string_aliases[child.id]
                    for child in ast.walk(node)
                    if isinstance(child, ast.Name) and child.id in string_aliases
                )
                call_strings = sorted(set(call_strings))
                if function_name in read_call_names:
                    reviewed_file_read_sites.append(
                        {
                            "file": relative,
                            "line": node.lineno,
                            "call": function_name,
                            "literal_fragments": call_strings,
                        }
                    )
                    for literal in call_strings:
                        if suspicious_path_pattern.search(literal):
                            findings.append(
                                {
                                    "file": relative,
                                    "line": node.lineno,
                                    "kind": "forbidden_target_path_literal",
                                    "value": literal,
                                }
                            )
                for literal in call_strings:
                    if url_pattern.search(literal):
                        findings.append(
                            {
                                "file": relative,
                                "line": node.lineno,
                                "kind": "network_url_literal",
                                "value": literal,
                            }
                        )
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                names = assignment_names(node)
                resolved_string = resolve_string_expression(value, string_aliases)
                if resolved_string is not None and suspicious_path_pattern.search(
                    resolved_string
                ):
                    findings.append(
                        {
                            "file": relative,
                            "line": node.lineno,
                            "kind": "suspicious_target_path_alias",
                            "value": resolved_string,
                            "aliases": names,
                        }
                    )
                if resolved_string is not None and url_pattern.search(resolved_string):
                    findings.append(
                        {
                            "file": relative,
                            "line": node.lineno,
                            "kind": "network_url_alias",
                            "value": resolved_string,
                            "aliases": names,
                        }
                    )
                if any(suspicious_path_pattern.search(name) for name in names):
                    if isinstance(value, (ast.List, ast.Tuple, ast.Set)):
                        findings.append(
                            {
                                "file": relative,
                                "line": node.lineno,
                                "kind": "embedded_target_array",
                                "value": names,
                            }
                        )
            elif isinstance(node, ast.Compare) and len(node.ops) == len(node.comparators) == 1:
                operator = node.ops[0]
                left = node.left
                right = node.comparators[0]
                threshold = None
                if isinstance(operator, (ast.Lt, ast.LtE)) and is_abs_call(left):
                    threshold = float_threshold(right, numeric_aliases)
                elif isinstance(operator, (ast.Gt, ast.GtE)) and is_abs_call(right):
                    threshold = float_threshold(left, numeric_aliases)
                if threshold is not None and threshold > 0:
                    findings.append(
                        {
                            "file": relative,
                            "line": node.lineno,
                            "kind": "tolerance_exactness_promotion",
                            "threshold": repr(threshold),
                            "expression": ast.unparse(node),
                        }
                    )

    for path in sorted((code_directory / "scripts").glob("*.sh")):
        relative = str(path.relative_to(code_directory))
        scanned.append(relative)
        source = path.read_text(encoding="utf-8")
        if re.search(r"\b(?:curl|wget|nc|ssh)\b", source):
            findings.append({"file": relative, "line": None, "kind": "shell_network_command"})
        if suspicious_path_pattern.search(source):
            findings.append({"file": relative, "line": None, "kind": "shell_target_reference"})

    return {
        "run_id": "R001",
        "scan_type": "Python AST import/call isolation scan",
        "scanned_executable_files": scanned,
        "excluded": ["scanner implementation", "tests"],
        "forbidden_network_import_roots": sorted(forbidden_import_roots),
        "forbidden_target_call_names": sorted(forbidden_call_names),
        "suspicious_target_path_pattern": suspicious_path_pattern.pattern,
        "reviewed_file_read_sites": reviewed_file_read_sites,
        "dataflow_checks": [
            "simple string aliases and Path aliases are propagated into file-read calls",
            "abs(expression)<positive_float tolerance promotions are forbidden",
        ],
        "findings": findings,
        "external_target_data_accessed": False,
        "prime_generation_policy": "factorint is allowed only on internally derived exact rational denominators or moduli",
        "pass": not findings,
    }
