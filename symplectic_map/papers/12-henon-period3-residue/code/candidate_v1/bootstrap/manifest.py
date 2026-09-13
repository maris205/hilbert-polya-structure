"""Closed-tree, AST, import-DAG, capability, and source-binding audits."""

from __future__ import annotations

import ast
import hashlib
import os
import stat
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any

from .constants import (
    CANDIDATE_ID,
    JUNIT_PATH,
    PREFLIGHT_PATH,
    PRESERVED_R1_PATH,
    PRESERVED_R1_SHA256,
    PROOF_PATH,
    PROOF_SHA256,
    SOURCE_BINDINGS,
    SOURCE_LOCK_PATH,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_PATH,
    SOURCE_REVIEW_SHA256,
)
from .protocol import (
    canonical_json_bytes,
    exact_same,
    load_exact_json,
    load_source_json,
    regular_directory,
    regular_file,
    sha256_file,
    stable_file_bytes,
    strict_json_loads,
    validate_canonical_json_file,
)


FORBIDDEN_TREE_NAMES = frozenset(
    {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".coverage", "htmlcov"}
)
SCIENCE_FILES = (
    "candidate_v1/track_q/engine.py",
    "candidate_v1/track_r/engine.py",
)
TRACK_Q_PREFIX = "candidate_v1/track_q/"
TRACK_R_PREFIX = "candidate_v1/track_r/"
SHARED_PREFIX = "candidate_v1/shared/"

DEFINITION_ROOT_KEYS = frozenset(
    {
        "allowed_task_ids",
        "candidate_id",
        "category",
        "cyclic_orientation",
        "exact_serialization",
        "family",
        "formal_period_convention",
        "nonclaim_tags",
        "output_field_names",
        "registered_coefficient_indices",
        "schema",
        "symbol_names",
    }
)
LEDGER_COUNTER_KEYS = frozenset(
    {
        "coefficient_check_outside_registered_tuple_count",
        "cross_track_scientific_read_count",
        "definitions_only_shared_schema_count",
        "degree_parameter_scan_count",
        "engine_acceptance_ledger_access_count",
        "engine_source_document_access_count",
        "exact_engine_count",
        "external_modulus_data_access_count",
        "external_prime_data_access_count",
        "external_zero_data_access_count",
        "filesystem_read_outside_allowlist_count",
        "filesystem_write_outside_allowlist_count",
        "floating_field_count",
        "full_quotient_residue_at_registered_tuple_count",
        "global_quartic_or_conjugacy_claim_count",
        "historical_m2_m7_result_access_count",
        "historical_source_stage_diagnostic_used_as_evidence_count",
        "interpolation_count",
        "machine_source_proof_verdict_count",
        "network_access_count",
        "new_modulus_scan_count",
        "numerical_root_solve_count",
        "period3_all_m_separation_claim_count",
        "post_result_retune_count",
        "random_seed_count",
        "registered_audit_count",
        "registered_candidate_id_count",
        "registered_coefficient_check_count",
        "registered_coefficient_check_order",
        "registered_engine_index_evaluation_count",
        "shared_H_A_implementation_count",
        "shared_arithmetic_helper_count",
        "shared_binomial_implementation_count",
        "shared_generalized_binomial_implementation_count",
        "shared_schema_scientific_field_count",
        "shared_scientific_implementation_count",
        "stored_D8_D9_expected_value_count",
        "stored_expected_E8_E9_count",
        "track_q_collapsed_formula_access_count",
        "track_r_precollapse_formula_access_count",
        "universal_Dm_nonvanishing_claim_count",
    }
)


def _exact_string_list(value: Any, *, minimum: int = 1) -> bool:
    return (
        type(value) is list
        and len(value) >= minimum
        and all(type(item) is str and item for item in value)
        and len(set(value)) == len(value)
    )


def _definitions_findings(definitions: Any) -> list[str]:
    errors: list[str] = []
    if type(definitions) is not dict or set(definitions) != DEFINITION_ROOT_KEYS:
        return ["DEFINITIONS_ROOT_KEYS"]
    if definitions["schema"] != "HENON_PERIOD3_DEFINITIONS_ONLY_V1":
        errors.append("DEFINITIONS_SCHEMA_INVALID")
    if definitions["candidate_id"] != CANDIDATE_ID:
        errors.append("DEFINITIONS_CANDIDATE_INVALID")
    indices = definitions["registered_coefficient_indices"]
    if indices != [8, 9] or any(type(value) is not int for value in indices):
        errors.append("DEFINITIONS_TUPLE_INVALID")
    expected_nested = {
        "category": {
            "base_field",
            "characteristic",
            "conjugacy_scope",
            "formal_period_objects",
            "jacobian_determinant",
        },
        "cyclic_orientation": {"F_i", "index_group", "q_i", "t_epsilon"},
        "exact_serialization": {"integer", "polynomial", "rational"},
        "formal_period_convention": {
            "exact_period_two",
            "exact_period_three",
            "moment_normalization",
        },
        "output_field_names": {
            "coefficient_diagnostics",
            "quartic",
            "track",
            "witness_digest",
        },
    }
    for key, keys in expected_nested.items():
        nested = definitions[key]
        if type(nested) is not dict or set(nested) != keys:
            errors.append("DEFINITIONS_NESTED_KEYS:" + key)
        elif key != "category" and any(
            type(value) is not str or not value for value in nested.values()
        ):
            errors.append("DEFINITIONS_NESTED_TYPES:" + key)
    category = definitions["category"]
    if type(category) is dict:
        if type(category.get("characteristic")) is not int or category.get("characteristic") != 0:
            errors.append("DEFINITIONS_CHARACTERISTIC")
        if type(category.get("jacobian_determinant")) is not int or category.get(
            "jacobian_determinant"
        ) != -1:
            errors.append("DEFINITIONS_JACOBIAN")
        for key in {"base_field", "conjugacy_scope", "formal_period_objects"}:
            if type(category.get(key)) is not str or not category.get(key):
                errors.append("DEFINITIONS_CATEGORY_TYPE:" + key)
    for key in ("allowed_task_ids", "nonclaim_tags", "symbol_names"):
        if not _exact_string_list(definitions[key]):
            errors.append("DEFINITIONS_LIST:" + key)
    if definitions["allowed_task_ids"] != [
        "B1_CONTRACT_WITNESSES",
        "B2_QUARTIC_FIBER_LOW_PERIOD",
        "B3_QUARTIC_PERIOD_THREE",
        "B4_ISOLATED_COEFFICIENT_DIAGNOSTICS",
        "B5_SCOPE_AND_ISOLATION_CONTROLS",
    ]:
        errors.append("DEFINITIONS_TASK_IDS")
    if definitions["symbol_names"] != ["m", "a", "epsilon", "x_0", "x_1", "x_2", "L"]:
        errors.append("DEFINITIONS_SYMBOLS")
    if definitions["nonclaim_tags"] != [
        "UNIVERSAL_D_M_NONVANISHING_OPEN",
        "NO_ALL_M_PERIOD3_SEPARATION",
        "NO_ALL_QUARTIC_HENON_SEPARATION",
        "NO_GLOBAL_P4_EQUALS_3",
        "NO_FAMILY_OR_LOW_PERIOD_PRIORITY",
        "NO_RESIDUE_METHOD_PRIORITY",
        "NO_HISTORICAL_PRIORITY_FROM_BOUNDED_SEARCH",
    ]:
        errors.append("DEFINITIONS_NONCLAIMS")
    if type(definitions["family"]) is not str or not definitions["family"]:
        errors.append("DEFINITIONS_FAMILY")
    serialized = canonical_json_bytes(definitions).decode("ascii").lower()
    for token in ("theorem_pass", "source_proved", "expected_d8", "expected_d9", "expected_e8", "expected_e9"):
        if token in serialized:
            errors.append("DEFINITIONS_FORBIDDEN_TOKEN:" + token)
    return errors


def _moment_shape_errors(value: Any, label: str) -> list[str]:
    if type(value) is not dict or set(value) != {"terms", "variable"}:
        return [label + "_KEYS"]
    errors: list[str] = []
    if type(value["variable"]) is not str or not value["variable"]:
        errors.append(label + "_VARIABLE")
    terms = value["terms"]
    if type(terms) is not list or len(terms) != 2:
        return errors + [label + "_TERMS"]
    exponents: list[int] = []
    for term in terms:
        if type(term) is not dict or set(term) != {"coefficient", "exponent"}:
            errors.append(label + "_TERM_KEYS")
            continue
        if type(term["coefficient"]) is not int or type(term["exponent"]) is not int:
            errors.append(label + "_TERM_TYPES")
        else:
            exponents.append(term["exponent"])
    if exponents != sorted(exponents) or len(set(exponents)) != len(exponents):
        errors.append(label + "_TERM_ORDER")
    return errors


def _ledger_findings(ledger: Any) -> list[str]:
    root_keys = {
        "candidate_id",
        "coefficient_boundary",
        "counter_expectations",
        "negative_reason_codes",
        "quartic_expected",
        "schema",
    }
    if type(ledger) is not dict or set(ledger) != root_keys:
        return ["PRIVATE_LEDGER_ROOT_KEYS"]
    errors: list[str] = []
    if ledger["schema"] != "HENON_PERIOD3_PRIVATE_ACCEPTANCE_LEDGER_V1":
        errors.append("PRIVATE_LEDGER_SCHEMA")
    if ledger["candidate_id"] != CANDIDATE_ID:
        errors.append("PRIVATE_LEDGER_CANDIDATE")
    boundary = ledger["coefficient_boundary"]
    if type(boundary) is not dict or set(boundary) != {
        "comparison",
        "expected_value_storage_count",
        "indices",
    }:
        errors.append("PRIVATE_LEDGER_BOUNDARY_KEYS")
    else:
        if boundary["comparison"] != "track_q_final_integer_equals_track_r_final_integer":
            errors.append("PRIVATE_LEDGER_BOUNDARY_COMPARISON")
        if (type(boundary["expected_value_storage_count"]) is not int
                or boundary["expected_value_storage_count"] != 0):
            errors.append("PRIVATE_LEDGER_COEFFICIENT_EXPECTATION_PRESENT")
        if boundary["indices"] != [8, 9] or any(
            type(value) is not int for value in boundary["indices"]
        ):
            errors.append("PRIVATE_LEDGER_TUPLE_INVALID")
    counters = ledger["counter_expectations"]
    if type(counters) is not dict or set(counters) != LEDGER_COUNTER_KEYS:
        errors.append("PRIVATE_LEDGER_COUNTER_KEYS")
    else:
        for key, value in counters.items():
            if key == "registered_coefficient_check_order":
                if value != [8, 9] or any(type(item) is not int for item in value):
                    errors.append("PRIVATE_LEDGER_COUNTER_ORDER")
            elif type(value) is not int or value < 0:
                errors.append("PRIVATE_LEDGER_COUNTER_TYPE:" + key)
    reasons = ledger["negative_reason_codes"]
    expected_reasons = {
        "K001": "CYCLIC_JACOBIAN_DEFINITION_MUTATION",
        "K002": "TRACE_RESIDUE_EXPONENT_MUTATION",
        "K003": "PREMATURE_CYCLE_NORMALIZATION",
        "K004": "QUARTIC_SIMPLE_ROOT_OUTSIDE_FIBER",
        "K005": "NORMALIZED_SCOPE_EXPANSION",
        "K006": "FINITE_HISTORY_UNIVERSAL_OVERCLAIM",
        "K007": "ENGINE_OR_LEDGER_ISOLATION_BREACH",
        "K008": "CLOSED_WORLD_OR_INDEX_BREACH",
    }
    if type(reasons) is not dict or reasons != expected_reasons:
        errors.append("PRIVATE_LEDGER_REASON_CODES")
    quartic = ledger["quartic_expected"]
    quartic_keys = {
        "cyclewise_moment",
        "exact_period_three_length",
        "fiber_normal_form",
        "fixed_length",
        "fixed_moment",
        "normalized_conjugacy_coordinate",
        "period_one_characteristic_polynomial",
        "period_two_characteristic_polynomial",
        "pointwise_moment",
        "quotient_rank",
    }
    if type(quartic) is not dict or set(quartic) != quartic_keys:
        errors.append("PRIVATE_LEDGER_QUARTIC_KEYS")
    else:
        errors.extend(_moment_shape_errors(quartic["cyclewise_moment"], "PRIVATE_LEDGER_CYCLE"))
        errors.extend(_moment_shape_errors(quartic["pointwise_moment"], "PRIVATE_LEDGER_POINT"))
        for key in ("exact_period_three_length", "fixed_length", "fixed_moment", "quotient_rank"):
            if type(quartic[key]) is not int:
                errors.append("PRIVATE_LEDGER_QUARTIC_INTEGER:" + key)
        for key in (
            "fiber_normal_form",
            "normalized_conjugacy_coordinate",
            "period_one_characteristic_polynomial",
            "period_two_characteristic_polynomial",
        ):
            if type(quartic[key]) is not str or not quartic[key]:
                errors.append("PRIVATE_LEDGER_QUARTIC_STRING:" + key)
    return errors


def _inventory(code_root: Path) -> tuple[list[str], list[str]]:
    if not regular_directory(code_root):
        raise RuntimeError("code root is unsafe")
    files: list[str] = []
    errors: list[str] = []
    for directory, directory_names, file_names in os.walk(code_root, topdown=True, followlinks=False):
        directory_names.sort()
        file_names.sort()
        current = Path(directory)
        for name in list(directory_names):
            path = current / name
            if name in FORBIDDEN_TREE_NAMES:
                errors.append("FORBIDDEN_DIRECTORY:" + path.relative_to(code_root).as_posix())
                directory_names.remove(name)
                continue
            metadata = path.lstat()
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
                errors.append("UNSAFE_DIRECTORY:" + path.relative_to(code_root).as_posix())
                directory_names.remove(name)
        for name in file_names:
            path = current / name
            relative = path.relative_to(code_root).as_posix()
            if name in FORBIDDEN_TREE_NAMES or name.endswith((".pyc", ".pyo", "~")):
                errors.append("FORBIDDEN_FILE:" + relative)
                continue
            if not regular_file(path):
                errors.append("UNSAFE_FILE:" + relative)
                continue
            files.append(relative)
    return sorted(files), sorted(errors)


def code_inventory(code_root: Path) -> dict[str, Any]:
    first_files, first_errors = _inventory(code_root)
    second_files, second_errors = _inventory(code_root)
    errors = list(first_errors)
    if first_files != second_files or first_errors != second_errors:
        errors.append("UNSTABLE_CODE_INVENTORY")
    return {"files": first_files, "errors": sorted(set(errors)), "status": "CLOSED" if not errors else "REJECTED"}


def code_tree_sha256(code_root: Path, expected_paths: list[str] | None = None) -> str:
    inventory = code_inventory(code_root)
    if inventory["status"] != "CLOSED":
        raise RuntimeError("cannot hash unsafe code tree")
    paths = inventory["files"]
    if expected_paths is not None and paths != expected_paths:
        raise RuntimeError("code path inventory differs from reviewed manifest")
    digest = hashlib.sha256()
    for relative in paths:
        relative_bytes = relative.encode("utf-8")
        data = stable_file_bytes(code_root / relative)
        digest.update(len(relative_bytes).to_bytes(8, "big"))
        digest.update(relative_bytes)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def _qualified_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _qualified_name(node.value)
        return None if prefix is None else prefix + "." + node.attr
    return None


def _safe_container_receiver(node: ast.AST, local_functions: set[str]) -> bool:
    if isinstance(node, ast.Name):
        return not node.id.startswith("__")
    if isinstance(node, (ast.Dict, ast.List, ast.Tuple)):
        return True
    if isinstance(node, ast.Subscript):
        return _safe_container_receiver(node.value, local_functions)
    if isinstance(node, ast.Call):
        return isinstance(node.func, ast.Name) and node.func.id in local_functions
    return False


def _assigned_names(node: ast.AST) -> set[str]:
    if isinstance(node, ast.Name):
        return {node.id}
    if isinstance(node, (ast.Tuple, ast.List)):
        result: set[str] = set()
        for element in node.elts:
            result.update(_assigned_names(element))
        return result
    return set()


def _binding_names(node: ast.AST) -> set[str]:
    if isinstance(node, ast.Assign):
        result: set[str] = set()
        for target in node.targets:
            result.update(_assigned_names(target))
        return result
    if isinstance(node, (ast.AnnAssign, ast.NamedExpr, ast.For, ast.AsyncFor, ast.comprehension)):
        return _assigned_names(node.target)
    if isinstance(node, ast.withitem):
        return _assigned_names(node.optional_vars) if node.optional_vars is not None else set()
    if isinstance(node, ast.ExceptHandler):
        return {node.name} if type(node.name) is str else set()
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        arguments = (
            list(node.args.posonlyargs)
            + list(node.args.args)
            + list(node.args.kwonlyargs)
        )
        result = {argument.arg for argument in arguments}
        if node.args.vararg is not None:
            result.add(node.args.vararg.arg)
        if node.args.kwarg is not None:
            result.add(node.args.kwarg.arg)
        return result
    return set()


def _import_signature(node: ast.AST) -> str:
    if isinstance(node, ast.Import):
        names = ",".join(
            alias.name + (" as " + alias.asname if alias.asname else "") for alias in node.names
        )
        return "import " + names
    if isinstance(node, ast.ImportFrom):
        names = ",".join(
            alias.name + (" as " + alias.asname if alias.asname else "") for alias in node.names
        )
        return "from " + "." * node.level + (node.module or "") + " import " + names
    raise TypeError("import node required")


def analyze_python(path: Path, relative: str) -> dict[str, Any]:
    source = stable_file_bytes(path).decode("utf-8")
    tree = ast.parse(source, filename=relative)
    imports = sorted(
        _import_signature(node) for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))
    )
    call_sites = Counter()
    dunder_attributes: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _qualified_name(node.func)
            call_sites[name if name is not None else "<dynamic-call>"] += 1
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            dunder_attributes.append(node.attr)
    canonical_ast = ast.dump(tree, annotate_fields=True, include_attributes=False).encode("utf-8")
    function_body_sha256: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            body = ast.Module(body=node.body, type_ignores=[])
            body_bytes = ast.dump(
                body, annotate_fields=True, include_attributes=False
            ).encode("utf-8")
            function_body_sha256[node.name] = hashlib.sha256(body_bytes).hexdigest()
    return {
        "ast_sha256": hashlib.sha256(canonical_ast).hexdigest(),
        "function_body_sha256": dict(sorted(function_body_sha256.items())),
        "imports": imports,
        "call_site_multiset": dict(sorted(call_sites.items())),
        "dunder_attributes": sorted(dunder_attributes),
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
    }


def _science_capability_findings(code_root: Path, relative: str) -> list[str]:
    path = code_root / relative
    source = stable_file_bytes(path).decode("utf-8")
    tree = ast.parse(source, filename=relative)
    findings: list[str] = []
    imports = [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
    if imports:
        findings.append(relative + ":SCIENTIFIC_IMPORT_PRESENT")
    forbidden_names = {
        "open",
        "eval",
        "exec",
        "compile",
        "__import__",
        "input",
        "globals",
        "locals",
        "vars",
        "getattr",
        "setattr",
        "delattr",
        "breakpoint",
        "exit",
        "help",
        "print",
        "quit",
    }
    forbidden_suffixes = {
        ".open",
        ".read",
        ".read_text",
        ".read_bytes",
        ".write",
        ".write_text",
        ".write_bytes",
        ".fsync",
        ".close",
        ".pipe",
        ".dup2",
        ".set_inheritable",
        ".system",
        ".popen",
        ".spawnl",
        ".spawnv",
        ".fork",
        ".execv",
        ".connect",
        ".urlopen",
    }
    harmless_container_methods = {
        "append",
        "extend",
        "get",
        "items",
        "pop",
        "setdefault",
        "values",
    }
    harmless_builtin_calls = {
        "ArithmeticError",
        "TypeError",
        "ValueError",
        "all",
        "any",
        "dict",
        "enumerate",
        "int",
        "iter",
        "len",
        "list",
        "max",
        "min",
        "next",
        "range",
        "set",
        "sorted",
        "str",
        "sum",
        "tuple",
        "type",
        "zip",
    }
    local_function_names = {
        node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    protected_call_names = local_function_names | harmless_builtin_calls
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and type(node.value) is float:
            findings.append(relative + ":FLOAT_LITERAL")
        if isinstance(node, (ast.ClassDef, ast.Lambda)):
            findings.append(relative + ":DYNAMIC_OBJECT_DEFINITION")
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.decorator_list:
            findings.append(relative + ":DECORATED_SCIENCE_FUNCTION:" + node.name)
        for name in _binding_names(node):
            if name in protected_call_names:
                findings.append(relative + ":SHADOWED_CALL_TARGET:" + name)
        if isinstance(node, ast.Call):
            name = _qualified_name(node.func)
            if isinstance(node.func, ast.Attribute):
                if (node.func.attr not in harmless_container_methods
                        or not _safe_container_receiver(node.func.value, local_function_names)):
                    findings.append(relative + ":FORBIDDEN_METHOD_TARGET:" + node.func.attr)
            elif name is None:
                findings.append(relative + ":DYNAMIC_CALL_TARGET")
            elif name in forbidden_names or any(name.endswith(suffix) for suffix in forbidden_suffixes):
                findings.append(relative + ":FORBIDDEN_CALL:" + name)
            elif isinstance(node.func, ast.Name) and name not in local_function_names | harmless_builtin_calls:
                findings.append(relative + ":UNBOUND_CALL_TARGET:" + name)
        if isinstance(node, ast.Name) and node.id in forbidden_names:
            findings.append(relative + ":FORBIDDEN_NAME:" + node.id)
        if isinstance(node, ast.Name) and node.id.startswith("__"):
            findings.append(relative + ":DUNDER_NAME:" + node.id)
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            findings.append(relative + ":DUNDER_ATTRIBUTE:" + node.attr)
        if isinstance(node, ast.Attribute) and _qualified_name(node) == "sys.modules":
            findings.append(relative + ":SYS_MODULES_ACCESS")
        if isinstance(node, ast.Subscript) and _qualified_name(node.value) in {"__builtins__", "builtins.__dict__"}:
            findings.append(relative + ":BUILTINS_CONTAINER_ACCESS")
    lower_source = source.lower()
    for token in ("proof_package", "source_lock.json", "acceptance_ledger", "m2_m7", "http://", "https://"):
        if token in lower_source:
            findings.append(relative + ":FORBIDDEN_SOURCE_TOKEN:" + token)
    if relative.startswith(TRACK_Q_PREFIX):
        for token in ("H_value", "A_value", "E_value", "generalized_binomial", "9.27", "9.28"):
            if token in source:
                findings.append(relative + ":Q_ROUTE_BREACH:" + token)
    if relative.startswith(TRACK_R_PREFIX):
        for token in ("_q_reduction_state", "admissible", "9.8", "9.9", "9.13", "mathcal"):
            if token in source:
                findings.append(relative + ":R_ROUTE_BREACH:" + token)
    return sorted(set(findings))


def _capability_category_counts(code_root: Path, findings: list[str]) -> dict[str, int]:
    science_findings = [
        finding for finding in findings if any(finding.startswith(relative + ":") for relative in SCIENCE_FILES)
    ]
    if not science_findings:
        return {
            "network": 0,
            "process": 0,
            "filesystem": 0,
            "dynamic_loader": 0,
            "floating": 0,
        }
    sources = "\n".join(
        stable_file_bytes(code_root / relative).decode("utf-8").lower()
        for relative in SCIENCE_FILES
        if regular_file(code_root / relative)
    )
    joined = "\n".join(science_findings).lower()
    network_tokens = ("socket", "connect", "urlopen", "http://", "https://", "urllib")
    process_tokens = (
        "os.system", "popen", "spawnl", "spawnv", "fork", "execv", "subprocess"
    )
    filesystem_tokens = (
        "open", "read", "write", "fsync", "glob", "pathlib", "os.listdir", "os.scandir"
    )
    dynamic_markers = (
        "dynamic", "dunder", "sys_modules", "builtins", "unbound_call", "shadowed",
        "scientific_import", "decorated", "object_definition",
    )
    return {
        "network": sum(token in sources for token in network_tokens),
        "process": sum(token in sources for token in process_tokens),
        "filesystem": sum(token in sources for token in filesystem_tokens),
        "dynamic_loader": sum(marker in joined for marker in dynamic_markers),
        "floating": sum("float_literal" in finding.lower() for finding in science_findings),
    }


def _runner_boundary_findings(code_root: Path, relative: str, track: str) -> list[str]:
    source = stable_file_bytes(code_root / relative).decode("utf-8")
    tree = ast.parse(source, filename=relative)
    expected_imports = {
        "import hashlib",
        "import json",
        "import os",
        "from pathlib import Path",
    }
    observed_imports = {
        _import_signature(node)
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        and not (isinstance(node, ast.ImportFrom) and node.module == "engine")
    }
    findings: list[str] = []
    if observed_imports != expected_imports:
        findings.append(relative + ":RUNNER_IMPORT_SIGNATURE")
    main_nodes = [
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main"
    ]
    if len(main_nodes) != 1:
        return findings + [relative + ":RUNNER_MAIN_SHAPE"]
    main_node = main_nodes[0]
    engine_imports = [
        node for node in ast.walk(main_node)
        if isinstance(node, ast.ImportFrom) and node.module == "engine"
    ]
    all_engine_imports = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module == "engine"
    ]
    if len(engine_imports) != 1 or len(all_engine_imports) != 1:
        findings.append(relative + ":ENGINE_IMPORT_NESTING")
        return findings
    prefix = "_q_" if track == "Q" else "_r_"
    calls = {
        name: [
            node.lineno for node in ast.walk(main_node)
            if isinstance(node, ast.Call) and _qualified_name(node.func) == name
        ]
        for name in (prefix + "capability", prefix + "validate_claim", "run_science")
    }
    if any(len(lines) != 1 for lines in calls.values()):
        findings.append(relative + ":RUNNER_GATE_CALL_COUNTS")
    else:
        capability_line = calls[prefix + "capability"][0]
        claim_line = calls[prefix + "validate_claim"][0]
        import_line = engine_imports[0].lineno
        science_line = calls["run_science"][0]
        if not capability_line < claim_line < import_line < science_line:
            findings.append(relative + ":RUNNER_PRECLAIM_ORDER")
    for forbidden_path in (
        "notes/",
        "experiments/",
        "acceptance_ledger.json",
        "track_r/" if track == "Q" else "track_q/",
    ):
        if forbidden_path in source:
            findings.append(relative + ":RUNNER_FORBIDDEN_PATH:" + forbidden_path)
    return sorted(set(findings))


def static_code_audit(code_root: Path) -> dict[str, Any]:
    inventory = code_inventory(code_root)
    analyses: dict[str, Any] = {}
    findings: list[str] = list(inventory["errors"])
    for relative in inventory["files"]:
        if relative.endswith(".py"):
            analyses[relative] = analyze_python(code_root / relative, relative)
    for relative in SCIENCE_FILES:
        if relative not in inventory["files"]:
            findings.append("MISSING_SCIENCE_FILE:" + relative)
        else:
            findings.extend(_science_capability_findings(code_root, relative))
    for relative, track in (
        ("candidate_v1/track_q/runner.py", "Q"),
        ("candidate_v1/track_r/runner.py", "R"),
    ):
        if relative not in inventory["files"]:
            findings.append("MISSING_TRACK_RUNNER:" + relative)
        else:
            findings.extend(_runner_boundary_findings(code_root, relative, track))
    for relative, record in analyses.items():
        if relative.startswith("candidate_v1/bootstrap/") and any(
            token in signature
            for signature in record["imports"]
            for token in ("track_q", "track_r", "engine", "adjudicator")
        ):
            findings.append("PRECLAIM_SCIENCE_IMPORT:" + relative)
    shared_python = [
        relative for relative in inventory["files"] if relative.startswith(SHARED_PREFIX) and relative.endswith(".py")
    ]
    if shared_python:
        findings.append("SHARED_PYTHON_IMPLEMENTATION_PRESENT")
    q_imports = set()
    r_imports = set()
    for relative, record in analyses.items():
        if relative.startswith(TRACK_Q_PREFIX):
            q_imports.update(record["imports"])
        if relative.startswith(TRACK_R_PREFIX):
            r_imports.update(record["imports"])
    if any("track_r" in item for item in q_imports) or any("track_q" in item for item in r_imports):
        findings.append("CROSS_TRACK_IMPORT")
    definitions = load_exact_json(code_root / "candidate_v1/shared/definitions.json")
    definitions_bytes = stable_file_bytes(code_root / "candidate_v1/shared/definitions.json")
    findings.extend(_definitions_findings(definitions))
    ledger = load_exact_json(code_root / "candidate_v1/adjudicator/acceptance_ledger.json")
    findings.extend(_ledger_findings(ledger))
    return {
        "schema": "HENON_PERIOD3_STATIC_CODE_AUDIT_V1",
        "code_inventory": inventory,
        "python_analyses": analyses,
        "science_capability_findings": sorted(set(findings)),
        "science_capability_category_counts": _capability_category_counts(code_root, findings),
        "definitions_sha256": hashlib.sha256(definitions_bytes).hexdigest(),
        "shared_python_implementation_count": len(shared_python),
        "track_q_import_signatures": sorted(q_imports),
        "track_r_import_signatures": sorted(r_imports),
        "status": "CLEAN" if not findings else "REJECTED",
    }


def validate_source_package(project_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    if sha256_file(project_root / SOURCE_LOCK_PATH) != SOURCE_LOCK_SHA256:
        errors.append("SOURCE_LOCK_HASH")
    if sha256_file(project_root / SOURCE_REVIEW_PATH) != SOURCE_REVIEW_SHA256:
        errors.append("SOURCE_REVIEW_HASH")
    if sha256_file(project_root / PROOF_PATH) != PROOF_SHA256:
        errors.append("PROOF_HASH")
    lock = load_source_json(project_root / SOURCE_LOCK_PATH)
    if lock.get("candidate_id") != CANDIDATE_ID or lock.get("lock_version") != 2:
        errors.append("SOURCE_LOCK_IDENTITY")
    bindings = lock.get("local_source_bindings")
    if type(bindings) is not dict or len(bindings) != 14:
        errors.append("SOURCE_BINDING_COUNT")
    for relative, expected in SOURCE_BINDINGS.items():
        if not regular_file(project_root / relative) or sha256_file(project_root / relative) != expected:
            errors.append("SOURCE_BINDING:" + relative)
    if sha256_file(project_root / PRESERVED_R1_PATH) != PRESERVED_R1_SHA256:
        errors.append("PRESERVED_R1_HASH")
    review_text = stable_file_bytes(project_root / SOURCE_REVIEW_PATH).decode("utf-8")
    if "SOURCE_LOCK_PASS" not in review_text or SOURCE_LOCK_SHA256 not in review_text:
        errors.append("SOURCE_REVIEW_AUTHORITY")
    return {
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "proof_sha256": PROOF_SHA256,
        "bound_source_file_count": 14,
        "preserved_review_file_count": 1,
        "errors": errors,
        "status": "VALID" if not errors else "REJECTED",
    }


def parse_junit(path: Path) -> dict[str, Any]:
    if not regular_file(path):
        return {"errors": ["JUNIT_MISSING"], "status": "REJECTED"}
    data = stable_file_bytes(path)
    root = ET.fromstring(data)
    if root.tag == "testsuite":
        suites = [root]
    elif root.tag == "testsuites" and all(child.tag == "testsuite" for child in root):
        suites = list(root)
    else:
        return {"errors": ["JUNIT_ROOT_STRUCTURE"], "status": "REJECTED"}
    if not suites:
        return {"errors": ["JUNIT_NO_SUITES"], "status": "REJECTED"}
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    parse_errors: list[str] = []
    for suite in suites:
        declared: dict[str, int] = {}
        for key in totals:
            raw = suite.attrib.get(key)
            if raw is None:
                parse_errors.append("JUNIT_MISSING_" + key.upper())
                declared[key] = -1
                continue
            if not raw.isdigit():
                parse_errors.append("JUNIT_NONINTEGER_" + key.upper())
                declared[key] = -1
            else:
                declared[key] = int(raw)
        cases = [child for child in suite if child.tag == "testcase"]
        allowed_suite_children = {"testcase", "properties", "system-out", "system-err"}
        if any(child.tag not in allowed_suite_children for child in suite):
            parse_errors.append("JUNIT_UNEXPECTED_SUITE_CHILD")
        actual = {"tests": len(cases), "failures": 0, "errors": 0, "skipped": 0}
        for case in cases:
            outcomes = [
                child.tag for child in case if child.tag in {"failure", "error", "skipped"}
            ]
            if any(child.tag not in {"failure", "error", "skipped", "system-out", "system-err"}
                   for child in case):
                parse_errors.append("JUNIT_UNEXPECTED_CASE_CHILD")
            if len(outcomes) > 1:
                parse_errors.append("JUNIT_MULTIPLE_CASE_OUTCOMES")
            for outcome in outcomes:
                actual[{"failure": "failures", "error": "errors", "skipped": "skipped"}[outcome]] += 1
        for key in totals:
            if declared.get(key) != actual[key]:
                parse_errors.append("JUNIT_DECLARATION_MISMATCH_" + key.upper())
            totals[key] += actual[key]
    if totals["tests"] < 1:
        parse_errors.append("JUNIT_EMPTY")
    if totals["failures"] or totals["errors"] or totals["skipped"]:
        parse_errors.append("JUNIT_NOT_CLEAN")
    return {
        "sha256": hashlib.sha256(data).hexdigest(),
        **totals,
        "errors_detail": parse_errors,
        "status": "VALID" if not parse_errors else "REJECTED",
    }


def build_code_manifest(project_root: Path) -> dict[str, Any]:
    code_root = project_root / "code"
    audit = static_code_audit(code_root)
    if audit["status"] != "CLEAN":
        raise RuntimeError("static code audit is not clean")
    source = validate_source_package(project_root)
    if source["status"] != "VALID":
        raise RuntimeError("source package does not validate")
    junit = parse_junit(project_root / JUNIT_PATH)
    if junit["status"] != "VALID":
        raise RuntimeError("JUnit evidence does not validate")
    preflight = validate_canonical_json_file(project_root / PREFLIGHT_PATH)
    if preflight.get("status") != "PREEXECUTION_PASS_REGISTERED_COUNT_ZERO":
        raise RuntimeError("preflight does not authorize deployment review")
    files = audit["code_inventory"]["files"]
    file_hashes = {relative: sha256_file(code_root / relative) for relative in files}
    manifest = {
        "schema": "HENON_PERIOD3_CODE_DEPLOYMENT_MANIFEST_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "proof_sha256": PROOF_SHA256,
        "code_tree_sha256": code_tree_sha256(code_root, files),
        "code_file_count": len(files),
        "code_files": file_hashes,
        "python_ast_sha256": {
            relative: record["ast_sha256"] for relative, record in audit["python_analyses"].items()
        },
        "python_function_body_sha256": {
            relative: record["function_body_sha256"]
            for relative, record in audit["python_analyses"].items()
        },
        "python_import_signatures": {
            relative: record["imports"] for relative, record in audit["python_analyses"].items()
        },
        "capability_call_site_multisets": {
            relative: record["call_site_multiset"] for relative, record in audit["python_analyses"].items()
        },
        "definitions_sha256": audit["definitions_sha256"],
        "shared_python_implementation_count": audit["shared_python_implementation_count"],
        "science_capability_finding_count": len(audit["science_capability_findings"]),
        "science_capability_category_counts": audit["science_capability_category_counts"],
        "junit_sha256": junit["sha256"],
        "junit_test_count": junit["tests"],
        "preflight_sha256": sha256_file(project_root / PREFLIGHT_PATH),
        "review_read_allowlists": {
            "track_q": [
                "runtime/candidate_v1/official/durable_claim.json",
                "code/candidate_v1/shared/definitions.json",
                "code/candidate_v1/track_q/engine.py",
                "code/candidate_v1/track_q/runner.py",
            ],
            "track_r": [
                "runtime/candidate_v1/official/durable_claim.json",
                "code/candidate_v1/shared/definitions.json",
                "code/candidate_v1/track_r/engine.py",
                "code/candidate_v1/track_r/runner.py",
            ],
            "adjudicator": [
                "runtime/candidate_v1/official/durable_claim.json",
                "code/candidate_v1/adjudicator/adjudicate.py",
                "code/candidate_v1/shared/result_envelope.schema.json",
                "code/candidate_v1/adjudicator/acceptance_ledger.json",
                "runtime/candidate_v1/staging/track_q/sealed_envelope.json",
                "runtime/candidate_v1/staging/track_r/sealed_envelope.json",
            ],
        },
        "registered_execution_count_at_freeze": 0,
        "official_claim_result_terminal_present": False,
    }
    return manifest


def validate_code_manifest(project_root: Path) -> dict[str, Any]:
    from .constants import CODE_MANIFEST_PATH

    errors: list[str] = []
    manifest = validate_canonical_json_file(project_root / CODE_MANIFEST_PATH)
    required = {
        "schema",
        "candidate_id",
        "source_lock_sha256",
        "source_review_sha256",
        "proof_sha256",
        "code_tree_sha256",
        "code_file_count",
        "code_files",
        "python_ast_sha256",
        "python_function_body_sha256",
        "python_import_signatures",
        "capability_call_site_multisets",
        "definitions_sha256",
        "shared_python_implementation_count",
        "science_capability_finding_count",
        "science_capability_category_counts",
        "junit_sha256",
        "junit_test_count",
        "preflight_sha256",
        "review_read_allowlists",
        "registered_execution_count_at_freeze",
        "official_claim_result_terminal_present",
    }
    if type(manifest) is not dict or set(manifest) != required:
        errors.append("CODE_MANIFEST_KEYS")
        return {"errors": errors, "status": "REJECTED"}
    if manifest["schema"] != "HENON_PERIOD3_CODE_DEPLOYMENT_MANIFEST_V1":
        errors.append("CODE_MANIFEST_SCHEMA")
    if manifest["candidate_id"] != CANDIDATE_ID:
        errors.append("CODE_MANIFEST_CANDIDATE")
    if manifest["source_lock_sha256"] != SOURCE_LOCK_SHA256 or manifest["source_review_sha256"] != SOURCE_REVIEW_SHA256:
        errors.append("CODE_MANIFEST_SOURCE_BINDING")
    if manifest["proof_sha256"] != PROOF_SHA256:
        errors.append("CODE_MANIFEST_PROOF_BINDING")
    expected_paths = sorted(manifest["code_files"])
    if manifest["code_file_count"] != len(expected_paths) or type(manifest["code_file_count"]) is not int:
        errors.append("CODE_MANIFEST_COUNT")
    inventory = code_inventory(project_root / "code")
    if inventory["files"] != expected_paths or inventory["status"] != "CLOSED":
        errors.append("CODE_MANIFEST_INVENTORY")
    for relative, expected in manifest["code_files"].items():
        if not regular_file(project_root / "code" / relative) or sha256_file(project_root / "code" / relative) != expected:
            errors.append("CODE_FILE_HASH:" + relative)
    try:
        observed_tree = code_tree_sha256(project_root / "code", expected_paths)
    except RuntimeError:
        observed_tree = ""
    if observed_tree != manifest["code_tree_sha256"]:
        errors.append("CODE_TREE_HASH")
    fresh_audit = static_code_audit(project_root / "code")
    if fresh_audit["status"] != "CLEAN":
        errors.append("STATIC_AUDIT")
    else:
        for relative, record in fresh_audit["python_analyses"].items():
            if manifest["python_ast_sha256"].get(relative) != record["ast_sha256"]:
                errors.append("AST_HASH:" + relative)
            if manifest["python_function_body_sha256"].get(relative) != record["function_body_sha256"]:
                errors.append("FUNCTION_BODY_HASH:" + relative)
            if manifest["python_import_signatures"].get(relative) != record["imports"]:
                errors.append("IMPORT_SIGNATURE:" + relative)
            if manifest["capability_call_site_multisets"].get(relative) != record["call_site_multiset"]:
                errors.append("CALLSITE_MULTISET:" + relative)
    if sha256_file(project_root / JUNIT_PATH) != manifest["junit_sha256"]:
        errors.append("JUNIT_HASH")
    if sha256_file(project_root / PREFLIGHT_PATH) != manifest["preflight_sha256"]:
        errors.append("PREFLIGHT_HASH")
    if manifest["registered_execution_count_at_freeze"] != 0 or type(
        manifest["registered_execution_count_at_freeze"]
    ) is not int:
        errors.append("FREEZE_REGISTERED_COUNT")
    if manifest["official_claim_result_terminal_present"] is not False:
        errors.append("FREEZE_OFFICIAL_STATE")
    try:
        fresh_manifest = build_code_manifest(project_root)
    except (OSError, RuntimeError, TypeError, ValueError):
        fresh_manifest = None
        errors.append("FRESH_MANIFEST_RECOMPUTATION")
    if fresh_manifest is not None and not exact_same(manifest, fresh_manifest):
        errors.append("FRESH_MANIFEST_MISMATCH")
    return {
        "manifest": manifest,
        "manifest_sha256": sha256_file(project_root / CODE_MANIFEST_PATH),
        "errors": errors,
        "status": "VALID" if not errors else "REJECTED",
    }
