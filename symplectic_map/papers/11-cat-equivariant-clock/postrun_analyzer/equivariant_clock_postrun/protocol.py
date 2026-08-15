"""Strict I/O, closed inventories, hashing, and safe evidence parsing."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import stat
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Iterable

from .constants import (
    ANALYZER_DIRECTORIES,
    ANALYZER_FILES,
    EXECUTION_CODE_DIRECTORIES,
    EXECUTION_CODE_FILES,
    EXECUTION_TREE_FILES,
    REQUIRED_ANALYZER_TESTS,
)


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _has_symlink_component(path: Path) -> bool:
    absolute = lexical_absolute(path)
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            return False
        if stat.S_ISLNK(metadata.st_mode):
            return True
    return False


def regular_directory(path: Path) -> bool:
    absolute = lexical_absolute(path)
    if _has_symlink_component(absolute):
        return False
    try:
        metadata = absolute.lstat()
    except OSError:
        return False
    return stat.S_ISDIR(metadata.st_mode)


def regular_file(path: Path) -> bool:
    absolute = lexical_absolute(path)
    if _has_symlink_component(absolute):
        return False
    try:
        metadata = absolute.lstat()
    except OSError:
        return False
    return stat.S_ISREG(metadata.st_mode) and metadata.st_nlink == 1


def stable_file_bytes(path: Path) -> bytes:
    absolute = lexical_absolute(path)
    if not regular_file(absolute):
        raise OSError("file is missing, linked, or unsafe")
    first_stat = absolute.stat()
    first = absolute.read_bytes()
    middle_stat = absolute.stat()
    second = absolute.read_bytes()
    final_stat = absolute.stat()
    signature = lambda item: (
        item.st_dev,
        item.st_ino,
        item.st_mode,
        item.st_nlink,
        item.st_size,
        item.st_mtime_ns,
        item.st_ctime_ns,
    )
    if signature(first_stat) != signature(middle_stat) or signature(middle_stat) != signature(final_stat):
        raise RuntimeError("file metadata changed during read")
    if first != second:
        raise RuntimeError("file bytes changed during read")
    return first


def sha256_file(path: Path) -> str:
    return hashlib.sha256(stable_file_bytes(path)).hexdigest()


def _reject_float(_: str) -> None:
    raise ValueError("floating-point JSON values are forbidden")


def _reject_constant(_: str) -> None:
    raise ValueError("non-finite JSON constants are forbidden")


def _object_without_duplicates(pairs: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def strict_json_loads(text: str) -> Any:
    value = json.loads(
        text,
        object_pairs_hook=_object_without_duplicates,
        parse_float=_reject_float,
        parse_constant=_reject_constant,
    )
    canonical_json_bytes(value)
    return value


def load_exact_json(path: Path) -> Any:
    raw = stable_file_bytes(path)
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("JSON is not UTF-8") from error
    return strict_json_loads(text)


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def pretty_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def write_pretty_json_exclusive(path: Path, value: Any) -> None:
    absolute = lexical_absolute(path)
    if not regular_directory(absolute.parent):
        raise OSError("output directory is missing or unsafe")
    payload = pretty_json_bytes(value)
    descriptor = os.open(
        absolute,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL,
        0o644,
    )
    try:
        with os.fdopen(descriptor, "wb", closefd=False) as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        os.close(descriptor)


def _inventory_once(root: Path) -> dict[str, list[str]]:
    absolute = lexical_absolute(root)
    files: list[str] = []
    directories: list[str] = []
    errors: list[str] = []
    if not regular_directory(absolute):
        return {"files": [], "directories": [], "errors": ["ROOT_UNSAFE"]}
    for entry in sorted(absolute.iterdir(), key=lambda item: item.name):
        try:
            metadata = entry.lstat()
        except OSError:
            errors.append("UNREADABLE:" + entry.name)
            continue
        if stat.S_ISLNK(metadata.st_mode):
            errors.append("SYMLINK:" + entry.name)
        elif stat.S_ISREG(metadata.st_mode):
            if metadata.st_nlink != 1:
                errors.append("HARDLINK:" + entry.name)
            files.append(entry.name)
        elif stat.S_ISDIR(metadata.st_mode):
            directories.append(entry.name)
            for child in sorted(entry.iterdir(), key=lambda item: item.name):
                relative = entry.name + "/" + child.name
                try:
                    child_metadata = child.lstat()
                except OSError:
                    errors.append("UNREADABLE:" + relative)
                    continue
                if stat.S_ISREG(child_metadata.st_mode):
                    if child_metadata.st_nlink != 1:
                        errors.append("HARDLINK:" + relative)
                    files.append(relative)
                elif stat.S_ISLNK(child_metadata.st_mode):
                    errors.append("SYMLINK:" + relative)
                else:
                    errors.append("NONREGULAR_OR_NESTED:" + relative)
        else:
            errors.append("NONREGULAR:" + entry.name)
    return {"files": files, "directories": directories, "errors": errors}


def closed_inventory(
    root: Path,
    *,
    expected_files: frozenset[str],
    expected_directories: frozenset[str],
) -> dict[str, Any]:
    first = _inventory_once(root)
    second = _inventory_once(root)
    errors = list(first["errors"])
    if first != second:
        errors.append("INVENTORY_UNSTABLE")
    if set(first["files"]) != set(expected_files) or len(first["files"]) != len(expected_files):
        errors.append("FILES_NOT_EXACT")
    if set(first["directories"]) != set(expected_directories):
        errors.append("DIRECTORIES_NOT_EXACT")
    return {
        "files": first["files"],
        "directories": first["directories"],
        "errors": errors,
        "pass": not errors,
    }


def _framed_tree_hash(root: Path, relative_paths: Iterable[str]) -> str:
    digest = hashlib.sha256()
    for relative in sorted(relative_paths):
        encoded_path = relative.encode("utf-8")
        content = stable_file_bytes(root / relative)
        digest.update(len(encoded_path).to_bytes(8, "big"))
        digest.update(encoded_path)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def execution_tree_sha256(project_root: Path) -> str:
    root = lexical_absolute(project_root)
    inventory = closed_inventory(
        root / "code",
        expected_files=EXECUTION_CODE_FILES,
        expected_directories=EXECUTION_CODE_DIRECTORIES,
    )
    if inventory["pass"] is not True:
        raise RuntimeError("immutable execution code inventory is not exact")
    first = _framed_tree_hash(root, EXECUTION_TREE_FILES)
    middle = closed_inventory(
        root / "code",
        expected_files=EXECUTION_CODE_FILES,
        expected_directories=EXECUTION_CODE_DIRECTORIES,
    )
    second = _framed_tree_hash(root, EXECUTION_TREE_FILES)
    if middle["pass"] is not True or first != second:
        raise RuntimeError("immutable execution tree changed during hashing")
    return first


def analyzer_tree_sha256(project_root: Path) -> str:
    root = lexical_absolute(project_root) / "postrun_analyzer"
    inventory = closed_inventory(
        root,
        expected_files=ANALYZER_FILES,
        expected_directories=ANALYZER_DIRECTORIES,
    )
    if inventory["pass"] is not True:
        raise RuntimeError("post-run analyzer inventory is not exact")
    first = _framed_tree_hash(root, ANALYZER_FILES)
    middle = closed_inventory(
        root,
        expected_files=ANALYZER_FILES,
        expected_directories=ANALYZER_DIRECTORIES,
    )
    second = _framed_tree_hash(root, ANALYZER_FILES)
    if middle["pass"] is not True or first != second:
        raise RuntimeError("post-run analyzer tree changed during hashing")
    return first


def result_inventory(project_root: Path, expected: frozenset[str]) -> dict[str, Any]:
    root = lexical_absolute(project_root) / "results"
    errors: list[str] = []
    if not regular_directory(root):
        return {"observed": [], "expected": sorted(expected), "errors": ["RESULTS_UNSAFE"], "pass": False}

    def scan() -> list[str]:
        names: list[str] = []
        for entry in sorted(root.iterdir(), key=lambda item: item.name):
            names.append(entry.name)
            if not regular_file(entry):
                errors.append("RESULT_FILE_UNSAFE:" + entry.name)
        return names

    first = scan()
    second = scan()
    if first != second:
        errors.append("RESULT_INVENTORY_UNSTABLE")
    if set(first) != set(expected) or len(first) != len(expected):
        errors.append("RESULT_INVENTORY_NOT_EXACT")
    return {
        "observed": first,
        "expected": sorted(expected),
        "errors": sorted(set(errors)),
        "pass": not errors,
    }


def parse_analyzer_junit(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    if not regular_file(path):
        return {
            "stage": "R121_ANALYZER_TEST_EVIDENCE",
            "path": "results/POSTRUN_ANALYZER_PYTEST.xml",
            "errors": ["ANALYZER_JUNIT_MISSING_OR_UNSAFE"],
            "pass": False,
        }
    raw = stable_file_bytes(path)
    if b"<!DOCTYPE" in raw or b"<!ENTITY" in raw:
        errors.append("ANALYZER_JUNIT_DTD_OR_ENTITY_FORBIDDEN")
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        errors.append("ANALYZER_JUNIT_XML_MALFORMED")
        root = None
    names: list[str] = []
    failures = errors_count = skipped = 0
    if root is not None:
        cases = list(root.iter("testcase"))
        for case in cases:
            name = case.attrib.get("name")
            if type(name) is not str or not name:
                errors.append("ANALYZER_JUNIT_TEST_NAME_INVALID")
            else:
                names.append(name)
            failures += len(list(case.findall("failure")))
            errors_count += len(list(case.findall("error")))
            skipped += len(list(case.findall("skipped")))
        if len(names) != len(set(names)):
            errors.append("ANALYZER_JUNIT_TEST_NAMES_DUPLICATE")
        if set(names) != set(REQUIRED_ANALYZER_TESTS) or len(names) != len(REQUIRED_ANALYZER_TESTS):
            errors.append("ANALYZER_JUNIT_REQUIRED_TESTS_NOT_EXACT")
        if failures or errors_count or skipped:
            errors.append("ANALYZER_JUNIT_NOT_ALL_PASSING")
    return {
        "stage": "R121_ANALYZER_TEST_EVIDENCE",
        "path": "results/POSTRUN_ANALYZER_PYTEST.xml",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "required_tests": sorted(REQUIRED_ANALYZER_TESTS),
        "observed_tests": sorted(names),
        "totals": {
            "tests": len(names),
            "failures": failures,
            "errors": errors_count,
            "skipped": skipped,
        },
        "errors": errors,
        "pass": not errors,
    }


FORBIDDEN_IMPORT_ROOTS = frozenset(
    {
        "aiohttp",
        "equivariant_clock",
        "ftplib",
        "http",
        "importlib",
        "multiprocessing",
        "numpy",
        "pandas",
        "pickle",
        "random",
        "requests",
        "scipy",
        "socket",
        "subprocess",
        "telnetlib",
        "urllib",
        "webbrowser",
    }
)
FORBIDDEN_CALL_NAMES = frozenset(
    {"__import__", "compile", "eval", "exec", "input", "open"}
)
FORBIDDEN_ATTRIBUTES = frozenset(
    {
        "connect",
        "popen",
        "request",
        "run",
        "socket",
        "system",
        "urlopen",
        "urlretrieve",
    }
)


def analyzer_executable_isolation(project_root: Path) -> dict[str, Any]:
    root = lexical_absolute(project_root) / "postrun_analyzer"
    executable = sorted(
        relative
        for relative in ANALYZER_FILES
        if relative.endswith(".py") and not relative.startswith("tests/")
    )
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for relative in executable:
        findings: list[str] = []
        try:
            source = stable_file_bytes(root / relative).decode("utf-8")
            tree = ast.parse(source, filename=relative)
        except (OSError, UnicodeDecodeError, SyntaxError, RuntimeError):
            findings.append("UNREADABLE_OR_INVALID_PYTHON")
            tree = None
        if tree is not None:
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and type(node.value) is float:
                    findings.append("FLOAT_LITERAL")
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split(".")[0] in FORBIDDEN_IMPORT_ROOTS:
                            findings.append("FORBIDDEN_IMPORT:" + alias.name)
                elif isinstance(node, ast.ImportFrom):
                    name = (node.module or "").split(".")[0]
                    if node.level == 0 and name in FORBIDDEN_IMPORT_ROOTS:
                        findings.append("FORBIDDEN_IMPORT:" + (node.module or ""))
                elif isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_CALL_NAMES:
                        findings.append("FORBIDDEN_CALL:" + node.func.id)
                    elif isinstance(node.func, ast.Attribute) and node.func.attr in FORBIDDEN_ATTRIBUTES:
                        findings.append("FORBIDDEN_ATTRIBUTE:" + node.func.attr)
        unique = sorted(set(findings))
        records.append({"path": relative, "errors": unique, "pass": not unique})
        errors.extend(relative + ":" + item for item in unique)
    return {
        "stage": "R120_ANALYZER_EXECUTABLE_ISOLATION",
        "records": records,
        "errors": errors,
        "pass": not errors,
    }
