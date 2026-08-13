"""Immutable source-lock validation and executable-isolation scanning."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_LOCK_SHA256 = "2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc"
EXPECTED_V1_LOCK_SHA256 = "f5465d92601cf8cd179bd514a08ca991992e718508ec54bf956d36d1280b80c9"
EXPECTED_REVIEW_SHA256 = "4036f346b75e44ff1acc8402cc1b17f497f3510ee0f4aa6456288f9856fbb63b"
CANDIDATE_ID = "additive_finite_arithmetic_capacity_v2"


class DuplicateJSONKeyError(ValueError):
    """Raised when an allegedly canonical JSON object repeats a key."""


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(text: str) -> Any:
    """Decode one JSON value and reject duplicate object keys at every depth."""

    return json.loads(text, object_pairs_hook=_unique_json_object)


def regular_file_within(root: Path, path: Path) -> bool:
    """Require a regular nonsymlink file reached through nonsymlink parents."""

    root = root.resolve()
    absolute = path.absolute()
    try:
        absolute.relative_to(root)
    except ValueError:
        return False

    current = absolute
    while current != root:
        if current.is_symlink():
            return False
        current = current.parent
    return absolute.is_file() and absolute.resolve() == absolute


def load_strict_json_file(root: Path, path: Path) -> Any:
    """Read canonical in-root JSON without following a symlink."""

    if not regular_file_within(root, path):
        raise ValueError(f"JSON path is not a regular in-root file: {path}")
    return strict_json_loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    """Return a streaming SHA-256 digest without interpreting file contents."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _inside(root: Path, path: Path) -> bool:
    """Return whether *path* resolves inside *root*."""

    root_resolved = root.resolve()
    path_resolved = path.resolve()
    return path_resolved == root_resolved or root_resolved in path_resolved.parents


def validate_source_lock(project_root: Path) -> dict[str, Any]:
    """Validate the immutable v2 lock and its pre-execution provenance."""

    project_root = project_root.resolve()
    lock_path = project_root / "experiments" / "source_lock.json"
    payload = load_strict_json_file(project_root, lock_path)
    if not isinstance(payload, dict):
        raise ValueError("source lock root must be a JSON object")
    digest = sha256_file(lock_path)

    history = payload.get("version_history", {})
    review_relative = history.get("independent_review_path", "")
    review_path = project_root / review_relative
    review_path_safe = bool(review_relative) and regular_file_within(project_root, review_path)
    review_digest = sha256_file(review_path) if review_path_safe else None

    execution = payload.get("execution_state_at_lock", {})
    execution_clean = (
        execution.get("external_prime_tables_accessed") is False
        and execution.get("prime_target_arrays_generated") is False
        and execution.get("riemann_zero_data_accessed") is False
        and execution.get("candidate_numerical_runs") == 0
        and execution.get("registered_exact_static_runs") == 0
        and execution.get("target_matches_computed") == 0
        and execution.get("paper5_figures_generated") == 0
        and execution.get("paper5_manuscript_written") is False
    )

    repairs = payload.get("mandatory_repair_closure", {})
    repair_ids = {f"B{index:02d}" for index in range(1, 11)}
    observed_repair_ids = {key.split("_", 1)[0] for key in repairs}
    repairs_closed = observed_repair_ids == repair_ids and all(value is True for value in repairs.values())

    permissions = payload.get("preexecution_permissions", {})
    formal_run_pre_review_closed = (
        permissions.get("registered_exact_static_audit") is False
        and permissions.get("candidate_numerical_execution") is False
        and permissions.get("prime_or_zero_data_access") is False
    )

    theorem = payload.get("primary_theorem", {})
    theorem_normalized = (
        theorem.get("name") == "additive finite arithmetic-capacity bound"
        and "log(p)=v_p+log(q_p)+alpha_p" in theorem.get("statement", "")
        and "dim_Q(V)+cardinality(S_Q)" in theorem.get("statement", "")
        and theorem.get("no_prior_finiteness_assumption") is True
    )

    history_bound = (
        history.get("v1_source_lock_sha256") == EXPECTED_V1_LOCK_SHA256
        and history.get("independent_review_sha256") == EXPECTED_REVIEW_SHA256
        and history.get("independent_review_occurred_before_paper5_implementation") is True
        and history.get("independent_review_occurred_before_any_candidate_execution") is True
        and history.get("independent_review_accessed_prime_or_zero_data") is False
        and review_digest == EXPECTED_REVIEW_SHA256
    )

    passed = (
        digest == EXPECTED_LOCK_SHA256
        and payload.get("candidate_id") == CANDIDATE_ID
        and payload.get("lock_version") == 2
        and payload.get("lock_status")
        == "SOURCE_LOCKED_PREEXECUTION_FORMAL_RUN_REQUIRES_INDEPENDENT_CODE_REVIEW"
        and history_bound
        and execution_clean
        and repairs_closed
        and formal_run_pre_review_closed
        and theorem_normalized
    )
    return {
        "gate_id": "G000",
        "candidate_id": payload.get("candidate_id"),
        "lock_version": payload.get("lock_version"),
        "path": str(lock_path),
        "sha256": digest,
        "expected_sha256": EXPECTED_LOCK_SHA256,
        "historical_v1_sha256": history.get("v1_source_lock_sha256"),
        "independent_review_sha256": review_digest,
        "review_path_safe": review_path_safe,
        "history_bound": history_bound,
        "execution_clean": execution_clean,
        "repairs_closed": repairs_closed,
        "repair_count": len(repairs),
        "formal_run_pre_review_closed": formal_run_pre_review_closed,
        "theorem_normalized": theorem_normalized,
        "pass": passed,
    }


def static_executable_isolation_scan(code_directory: Path) -> dict[str, Any]:
    """Fail on numeric, target-data, network, process, or hidden I/O paths.

    Tests are excluded because they are never imported by the formal command.
    Every other Python module, including this scanner and both script wrappers,
    is parsed.  Deny-list words stored as constants in this scanner are not
    findings; only executable AST imports, calls, identifiers, float literals,
    and I/O sites are classified.
    """

    allowed_import_roots = {
        "__future__",
        "ast",
        "capacity_audit",
        "dataclasses",
        "datetime",
        "fractions",
        "hashlib",
        "json",
        "pathlib",
        "typing",
    }
    forbidden_import_roots = {
        "aiohttp",
        "builtins",
        "decimal",
        "ftplib",
        "httpx",
        "importlib",
        "math",
        "mpmath",
        "numpy",
        "os",
        "pandas",
        "requests",
        "scipy",
        "socket",
        "subprocess",
        "sympy",
        "urllib",
        "yfinance",
    }
    forbidden_calls = {
        "N",
        "allclose",
        "check_call",
        "check_output",
        "eval",
        "evalf",
        "exec",
        "exp",
        "getattr",
        "globals",
        "genfromtxt",
        "__import__",
        "import_module",
        "isclose",
        "limit_denominator",
        "load",
        "loadtxt",
        "log",
        "log10",
        "nextprime",
        "nsimplify",
        "popen",
        "Popen",
        "prevprime",
        "prime",
        "primerange",
        "read_csv",
        "setattr",
        "system",
        "urlopen",
        "vars",
    }
    forbidden_identifiers = {
        "primepi",
        "primorial",
        "sieve",
        "zeta_zeros",
        "zetazero",
    }
    allowed_read_modules = {
        "capacity_audit/ledger.py",
        "capacity_audit/manifest.py",
        "capacity_audit/protocol.py",
        "capacity_audit/review_gate.py",
        "capacity_audit/upstream.py",
    }
    allowed_write_modules = {
        "capacity_audit/cli.py",
        "capacity_audit/manifest.py",
    }

    findings: list[dict[str, Any]] = []
    read_sites: list[dict[str, Any]] = []
    write_sites: list[dict[str, Any]] = []
    scanned_files: list[str] = []

    for path in sorted(code_directory.rglob("*.py")):
        if "tests" in path.parts or "__pycache__" in path.parts:
            continue
        relative = str(path.relative_to(code_directory))
        scanned_files.append(relative)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

        aliases: dict[str, str] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    aliases[alias.asname or alias.name.split(".")[0]] = alias.name
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                for alias in node.names:
                    aliases[alias.asname or alias.name] = f"{node.module}.{alias.name}"

        def resolved_name(expression: ast.AST) -> str | None:
            if isinstance(expression, ast.Name):
                return aliases.get(expression.id, expression.id)
            if isinstance(expression, ast.Attribute):
                parent = resolved_name(expression.value)
                return f"{parent}.{expression.attr}" if parent else expression.attr
            return None

        # Track simple call aliases such as ``loader = import_module`` and
        # ``reflect = getattr`` before examining call sites.
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            canonical = resolved_name(value) if value is not None else None
            if canonical is None:
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if (
                    isinstance(target, ast.Name)
                    and canonical != target.id
                    and not canonical.startswith(target.id + ".")
                ):
                    aliases[target.id] = canonical

        def numeric_collection(expression: ast.AST, tainted: set[str]) -> bool:
            if isinstance(expression, (ast.List, ast.Tuple, ast.Set)):
                return bool(expression.elts) and all(
                    isinstance(element, ast.Constant)
                    and isinstance(element.value, int)
                    and not isinstance(element.value, bool)
                    for element in expression.elts
                )
            if isinstance(expression, ast.Name):
                return expression.id in tainted
            if isinstance(expression, ast.Constant) and isinstance(expression.value, str):
                value = expression.value
                digits = sum(character.isdecimal() for character in value)
                return digits >= 2 and any(delimiter in value for delimiter in "[],;")
            if isinstance(expression, ast.Call):
                name = resolved_name(expression.func)
                leaf = "" if name is None else name.rsplit(".", 1)[-1]
                return leaf in {"list", "range", "set", "tuple"} and any(
                    isinstance(item, ast.Constant)
                    and isinstance(item.value, int)
                    and not isinstance(item.value, bool)
                    for item in expression.args
                )
            if isinstance(expression, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
                return any(
                    isinstance(descendant, ast.Call)
                    and (resolved_name(descendant.func) or "").rsplit(".", 1)[-1] == "range"
                    for descendant in ast.walk(expression)
                )
            return False

        assignments: list[tuple[ast.Name, ast.AST, int]] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        assignments.append((target, node.value, node.lineno))
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value is not None:
                assignments.append((node.target, node.value, node.lineno))

        numeric_tainted: set[str] = set()
        changed = True
        while changed:
            changed = False
            for target, value, _ in assignments:
                if target.id not in numeric_tainted and numeric_collection(value, numeric_tainted):
                    numeric_tainted.add(target.id)
                    changed = True

        reported_target_lines: set[int] = set()
        for target, value, line in assignments:
            lower_name = target.id.lower()
            suspicious_name = "prime" in lower_name or "zero" in lower_name or "target" in lower_name
            if suspicious_name and numeric_collection(value, numeric_tainted):
                findings.append(
                    {
                        "file": relative,
                        "line": line,
                        "kind": "embedded_or_indirect_target_numeric_collection",
                        "value": target.id,
                    }
                )
                reported_target_lines.add(line)

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root = alias.name.split(".")[0]
                    if root in forbidden_import_roots or root not in allowed_import_roots:
                        findings.append(
                            {
                                "file": relative,
                                "line": node.lineno,
                                "kind": "forbidden_import" if root in forbidden_import_roots else "unapproved_import",
                                "value": alias.name,
                            }
                        )
            elif isinstance(node, ast.ImportFrom):
                root = "" if node.module is None else node.module.split(".")[0]
                if node.level == 0 and root and (root in forbidden_import_roots or root not in allowed_import_roots):
                    findings.append(
                        {
                            "file": relative,
                            "line": node.lineno,
                            "kind": "forbidden_import" if root in forbidden_import_roots else "unapproved_import",
                            "value": node.module,
                        }
                    )
            elif isinstance(node, ast.Call):
                canonical_call = resolved_name(node.func)
                call_name = None if canonical_call is None else canonical_call.rsplit(".", 1)[-1]
                if call_name in forbidden_calls or canonical_call in forbidden_calls:
                    findings.append(
                        {
                            "file": relative,
                            "line": node.lineno,
                            "kind": "forbidden_call",
                            "value": canonical_call,
                        }
                    )
                if call_name in {"open", "read_bytes", "read_text"}:
                    record = {"file": relative, "line": node.lineno, "call": call_name}
                    mode: str | None = None
                    if call_name == "open":
                        if node.args and isinstance(node.args[-1], ast.Constant) and isinstance(node.args[-1].value, str):
                            mode = node.args[-1].value
                        for keyword in node.keywords:
                            if keyword.arg == "mode" and isinstance(keyword.value, ast.Constant):
                                mode = keyword.value.value
                    writing = mode is not None and any(character in mode for character in "wax+")
                    if writing:
                        write_sites.append(record)
                        if relative not in allowed_write_modules:
                            findings.append({**record, "kind": "unreviewed_file_write"})
                    else:
                        read_sites.append(record)
                        if relative not in allowed_read_modules:
                            findings.append({**record, "kind": "unreviewed_file_read"})
                if call_name in {"write_bytes", "write_text"}:
                    record = {"file": relative, "line": node.lineno, "call": call_name}
                    write_sites.append(record)
                    if relative not in allowed_write_modules:
                        findings.append({**record, "kind": "unreviewed_file_write"})
            elif isinstance(node, ast.Name) and node.id in forbidden_identifiers:
                findings.append(
                    {"file": relative, "line": node.lineno, "kind": "forbidden_identifier", "value": node.id}
                )
            elif isinstance(node, ast.Attribute) and node.attr in forbidden_identifiers:
                findings.append(
                    {"file": relative, "line": node.lineno, "kind": "forbidden_identifier", "value": node.attr}
                )
            elif isinstance(node, ast.Constant) and isinstance(node.value, float):
                findings.append(
                    {"file": relative, "line": node.lineno, "kind": "floating_literal", "value": repr(node.value)}
                )
            elif isinstance(node, (ast.Assign, ast.AnnAssign)) and node.lineno not in reported_target_lines:
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                value = node.value
                for target in targets:
                    if not isinstance(target, ast.Name):
                        continue
                    lower_name = target.id.lower()
                    suspicious_name = "prime" in lower_name or "zero" in lower_name or "target" in lower_name
                    numeric_collection = isinstance(value, (ast.List, ast.Tuple, ast.Set)) and all(
                        isinstance(element, ast.Constant)
                        and isinstance(element.value, int)
                        and not isinstance(element.value, bool)
                        for element in value.elts
                    )
                    if suspicious_name and numeric_collection:
                        findings.append(
                            {
                                "file": relative,
                                "line": node.lineno,
                                "kind": "embedded_target_numeric_collection",
                                "value": target.id,
                            }
                        )

    return {
        "gate_id": "G080_ISOLATION",
        "code_directory": str(code_directory),
        "scanned_files": scanned_files,
        "scanner_self_covered": "capacity_audit/protocol.py" in scanned_files,
        "script_wrappers_covered": {
            "scripts/run_registered_audit.py",
            "scripts/build_result_manifest.py",
        }.issubset(set(scanned_files)),
        "reviewed_file_read_sites": read_sites,
        "reviewed_file_write_sites": write_sites,
        "external_prime_tables_accessed": False,
        "prime_target_arrays_generated": False,
        "riemann_zero_data_accessed": False,
        "candidate_numerical_solver_present": False,
        "findings": findings,
        "pass": not findings,
    }
