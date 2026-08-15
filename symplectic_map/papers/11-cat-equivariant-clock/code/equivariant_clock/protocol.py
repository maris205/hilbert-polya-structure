"""Strict evidence I/O, closed-tree hashing, and executable isolation."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any

from .constants import (
    CAT_MATRIX,
    CODE_DIRECTORIES,
    CODE_FILES,
    DESIGN_REVIEWED_PATHS,
    LOCKED_COMPOSITES,
    LOCKED_MODULI,
    LOCKED_PRIMES,
    STRUCTURAL_CONTROL,
)


class DuplicateJSONKeyError(ValueError):
    """An exact evidence object repeated a key."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError("duplicate JSON key: " + key)
        result[key] = value
    return result


def strict_json_loads(text: str) -> Any:
    def reject_nonfinite(value: str) -> None:
        raise ValueError("non-finite JSON value: " + value)

    return json.loads(
        text,
        object_pairs_hook=_unique_object,
        parse_constant=reject_nonfinite,
        parse_float=lambda value: (_ for _ in ()).throw(
            ValueError("floating JSON value forbidden: " + value)
        ),
    )


def _contains_float(value: Any) -> bool:
    if type(value) is float:
        return True
    if type(value) is dict:
        return any(_contains_float(key) or _contains_float(item) for key, item in value.items())
    if type(value) in {list, tuple}:
        return any(_contains_float(item) for item in value)
    return False


def exact_json(value: Any) -> Any:
    if _contains_float(value):
        raise TypeError("floating evidence is forbidden")
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is tuple:
        return [exact_json(item) for item in value]
    if type(value) is list:
        return [exact_json(item) for item in value]
    if type(value) is dict:
        result: dict[str, Any] = {}
        for key, item in value.items():
            if type(key) not in {str, int}:
                raise TypeError("JSON evidence key must be string or integer")
            text = str(key)
            if text in result:
                raise ValueError("JSON key collision after normalization")
            result[text] = exact_json(item)
        return result
    raise TypeError("unsupported exact evidence type: " + type(value).__name__)


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        exact_json(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def pretty_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(exact_json(value), sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _reject_symlink_components(path: Path) -> None:
    absolute = lexical_absolute(path)
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        if current.exists() and stat.S_ISLNK(current.lstat().st_mode):
            raise RuntimeError("symlink component forbidden: " + os.fspath(current))


def regular_directory(path: Path) -> bool:
    try:
        absolute = lexical_absolute(path)
        _reject_symlink_components(absolute)
        return stat.S_ISDIR(absolute.stat().st_mode)
    except (OSError, RuntimeError):
        return False


def regular_file(path: Path) -> bool:
    try:
        absolute = lexical_absolute(path)
        _reject_symlink_components(absolute)
        return stat.S_ISREG(absolute.lstat().st_mode)
    except (OSError, RuntimeError):
        return False


def _identity(metadata: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def stable_file_bytes(path: Path) -> bytes:
    absolute = lexical_absolute(path)
    _reject_symlink_components(absolute)
    before = absolute.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise RuntimeError("stable read requires a regular file")
    descriptor = os.open(os.fspath(absolute), os.O_RDONLY | os.O_NOFOLLOW)
    try:
        opened = os.fstat(descriptor)
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    final = absolute.lstat()
    if _identity(before) != _identity(opened) or _identity(opened) != _identity(after):
        raise RuntimeError("file changed during stable read")
    if _identity(after) != _identity(final):
        raise RuntimeError("path changed during stable read")
    data = b"".join(chunks)
    if len(data) != before.st_size:
        raise RuntimeError("stable read size mismatch")
    return data


def sha256_file(path: Path) -> str:
    return hashlib.sha256(stable_file_bytes(path)).hexdigest()


def load_exact_json(path: Path) -> Any:
    return strict_json_loads(stable_file_bytes(path).decode("utf-8"))


def _write_all(descriptor: int, data: bytes) -> None:
    offset = 0
    while offset < len(data):
        written = os.write(descriptor, data[offset:])
        if written < 1:
            raise OSError("short evidence write")
        offset += written


def _fsync_parent_directory(path: Path) -> None:
    descriptor = os.open(os.fspath(path.parent), os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_bytes(path: Path, data: bytes, *, exclusive: bool = False) -> None:
    absolute = lexical_absolute(path)
    _reject_symlink_components(absolute.parent)
    if not regular_directory(absolute.parent):
        raise RuntimeError("evidence parent is not a regular directory")
    flags = os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW
    if exclusive:
        descriptor = os.open(os.fspath(absolute), flags | os.O_EXCL, 0o600)
        try:
            _write_all(descriptor, data)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        _fsync_parent_directory(absolute)
        return
    temporary = absolute.parent / ("." + absolute.name + ".paper11-write")
    if temporary.exists():
        raise RuntimeError("stale temporary evidence file")
    descriptor = os.open(os.fspath(temporary), flags | os.O_EXCL, 0o600)
    try:
        _write_all(descriptor, data)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    try:
        os.replace(os.fspath(temporary), os.fspath(absolute))
        _fsync_parent_directory(absolute)
    except BaseException:
        if temporary.exists():
            temporary.unlink()
        raise


def write_json(path: Path, value: Any, *, exclusive: bool = False) -> None:
    write_bytes(path, pretty_json_bytes(value), exclusive=exclusive)


def _inventory_once(code_root: Path) -> dict[str, Any]:
    root = lexical_absolute(code_root)
    files: list[str] = []
    directories: list[str] = []
    errors: list[str] = []
    if not regular_directory(root):
        return {"files": files, "directories": directories, "errors": ["CODE_ROOT_UNSAFE"]}
    for entry in sorted(root.iterdir(), key=lambda item: item.name):
        metadata = entry.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            errors.append("SYMLINK:" + entry.name)
        elif stat.S_ISDIR(metadata.st_mode):
            directories.append(entry.name)
            for child in sorted(entry.iterdir(), key=lambda item: item.name):
                child_metadata = child.lstat()
                relative = entry.name + "/" + child.name
                if stat.S_ISREG(child_metadata.st_mode):
                    files.append(relative)
                else:
                    errors.append("NONREGULAR:" + relative)
        elif stat.S_ISREG(metadata.st_mode):
            files.append(entry.name)
        else:
            errors.append("NONREGULAR:" + entry.name)
    return {"files": files, "directories": directories, "errors": errors}


def code_inventory(code_root: Path) -> dict[str, Any]:
    first = _inventory_once(code_root)
    second = _inventory_once(code_root)
    errors = list(first["errors"])
    if first != second:
        errors.append("CODE_INVENTORY_UNSTABLE")
    if set(first["files"]) != set(CODE_FILES) or len(first["files"]) != len(CODE_FILES):
        errors.append("CODE_FILES_NOT_EXACT")
    if set(first["directories"]) != set(CODE_DIRECTORIES):
        errors.append("CODE_DIRECTORIES_NOT_EXACT")
    return {
        "files": first["files"],
        "directories": first["directories"],
        "errors": errors,
        "pass": not errors,
    }


def reviewed_tree_paths(project_root: Path) -> tuple[str, ...]:
    root = lexical_absolute(project_root)
    paths = tuple(sorted(DESIGN_REVIEWED_PATHS + tuple("code/" + item for item in CODE_FILES)))
    for relative in paths:
        if not regular_file(root / relative):
            raise RuntimeError("reviewed tree file missing or unsafe: " + relative)
    return paths


def code_tree_sha256(project_root: Path) -> str:
    root = lexical_absolute(project_root)
    inventory = code_inventory(root / "code")
    if inventory["pass"] is not True:
        raise RuntimeError("closed code inventory failed")
    digest = hashlib.sha256()
    for relative in reviewed_tree_paths(root):
        path_data = relative.encode("utf-8")
        file_data = stable_file_bytes(root / relative)
        digest.update(len(path_data).to_bytes(8, "big"))
        digest.update(path_data)
        digest.update(len(file_data).to_bytes(8, "big"))
        digest.update(file_data)
    return digest.hexdigest()


# Filled after the executable tree is complete.  The scanner excludes this
# assignment from this module's own AST digest to avoid a self-hash cycle.
EXPECTED_EXECUTABLE_AST_SHA256: dict[str, str] = {
    "equivariant_clock/__init__.py": "97598b13f08964d256d29db7a61f2d004cc55b0a44b40d44cac1c5f3f9a831b9",
    "equivariant_clock/candidate.py": "f2bc3cc1e3add0f69ae544bce56feab5b5318746d291ca7d705807d57ffd7e23",
    "equivariant_clock/cli.py": "ce55508034f5f45c5359b15b478b93af6fbe58cf4ff31578b71730d955e411dd",
    "equivariant_clock/constants.py": "262d8a5837f6bdaa530a2feefe3255b81fae4bfe35dcbf457efe7b4faa54478a",
    "equivariant_clock/cyclic_cset.py": "5d73e6ae03e0802f2209182ffda165cf50fcd509bcc4d790a1e5dc48dd568085",
    "equivariant_clock/finite_module.py": "6f9eb52c74b0872fb0a1bdb359bffb5ea7888ee0c9fc30786530c465ff823f0c",
    "equivariant_clock/gates.py": "075ff6aae96f6054fae64378666dbbdb591b81f77713f53c0e4d15643c8a0cac",
    "equivariant_clock/invariants.py": "e9bd12fb8270b3dd622e3bd0121db98e4d5712d49e3550b5ee11becbf051dbcb",
    "equivariant_clock/lifecycle.py": "f33284457d2616c41bd2fd8bc445c930a8173414519d33c0a404926ccac085c8",
    "equivariant_clock/manifest.py": "8e586ff03dd4e408ccb03b7359a260cbbd20aa89b50df8fd6199c7f6d5c414e6",
    "equivariant_clock/protocol.py": "fe10bc9896cabd538c96a74a473e63ec7764990e9a791edd39cc0ef51811b674",
    "equivariant_clock/review.py": "52cf7d50f42bda553f7eadfc52bb78d8c54b25cd5c78eb5f5278418b54660af7",
    "scripts/build_result_manifest.py": "200989960aa9dcc6c583e5c66cde6085c822845e9f083de654e06b4fba96ce85",
    "scripts/run_registered_audit.py": "c8a11dc38a90dfa8731d3dead6885a7f51a791be180d539c7f841d0e3b280dfb",
    "scripts/run_safe_preflight.py": "2b99c695eabb11c34c3e266c4e1ac4e337663e5222b66b9acbc0dc99df484e05",
    "scripts/show_code_hash.py": "218e864923cc4f3e3d6e52af6a5d8d173afabd1f00e5540c17a60e7bce632a1b",
}


def _is_digest_assignment(node: ast.AST) -> bool:
    if isinstance(node, ast.Assign):
        return any(
            isinstance(target, ast.Name) and target.id == "EXPECTED_EXECUTABLE_AST_SHA256"
            for target in node.targets
        )
    return isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and (
        node.target.id == "EXPECTED_EXECUTABLE_AST_SHA256"
    )


def executable_ast_sha256(tree: ast.AST, relative: str) -> str:
    if not isinstance(tree, ast.Module):
        raise ValueError("module AST required")
    body = list(tree.body)
    if relative == "equivariant_clock/protocol.py":
        body = [node for node in body if not _is_digest_assignment(node)]
    canonical = ast.dump(
        ast.Module(body=body, type_ignores=tree.type_ignores),
        annotate_fields=True,
        include_attributes=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


FORBIDDEN_IMPORT_ROOTS = frozenset(
    {
        "aiohttp", "ctypes", "ftplib", "http", "importlib", "marshal",
        "multiprocessing", "numpy", "pandas", "pickle", "random", "requests",
        "scipy", "socket", "subprocess", "telnetlib", "urllib", "webbrowser",
    }
)
FORBIDDEN_NAMES = frozenset(
    {
        "__import__", "breakpoint", "compile", "delattr", "eval", "exec",
        "getattr", "globals", "help", "input", "locals", "setattr", "vars",
    }
)
FORBIDDEN_ATTRIBUTES = frozenset(
    {
        "connect", "fork", "forkpty", "fromfile", "genfromtxt", "kill",
        "loadtxt", "popen", "recv", "request", "send", "socket", "spawnl",
        "spawnle", "spawnlp", "spawnlpe", "spawnv", "spawnve", "spawnvp",
        "spawnvpe", "system", "urlopen", "urlretrieve",
    }
)
FORBIDDEN_NUMERIC_NAMES = frozenset({"exp", "log", "log10", "log2", "sqrt"})


def _literal_assignment(tree: ast.AST, name: str) -> Any:
    if not isinstance(tree, ast.Module):
        raise ValueError("module AST required")
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return ast.literal_eval(node.value)
    raise ValueError("frozen assignment missing: " + name)


def executable_isolation_scan(code_root: Path) -> dict[str, Any]:
    root = lexical_absolute(code_root)
    inventory = code_inventory(root)
    errors = list(inventory["errors"])
    records: list[dict[str, Any]] = []
    executable_paths = sorted(
        item for item in CODE_FILES
        if item.endswith(".py")
        and (item.startswith("equivariant_clock/") or item.startswith("scripts/"))
    )
    for relative in executable_paths:
        findings: list[str] = []
        try:
            tree = ast.parse(stable_file_bytes(root / relative).decode("utf-8"), filename=relative)
        except (OSError, RuntimeError, UnicodeDecodeError, SyntaxError):
            findings.append("UNREADABLE_OR_INVALID_PYTHON")
            records.append({"path": relative, "errors": findings, "pass": False})
            errors.append(relative + ":UNREADABLE_OR_INVALID_PYTHON")
            continue
        observed = executable_ast_sha256(tree, relative)
        if EXPECTED_EXECUTABLE_AST_SHA256.get(relative) != observed:
            findings.append("DYNAMIC:EXECUTABLE_AST_SIGNATURE_NOT_EXACT")
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and type(node.value) is float:
                findings.append("FLOAT:FLOAT_LITERAL")
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in FORBIDDEN_IMPORT_ROOTS:
                        findings.append("CAPABILITY:FORBIDDEN_IMPORT:" + alias.name)
            elif isinstance(node, ast.ImportFrom):
                root_name = (node.module or "").split(".")[0]
                if node.level == 0 and root_name in FORBIDDEN_IMPORT_ROOTS:
                    findings.append("CAPABILITY:FORBIDDEN_IMPORT:" + (node.module or ""))
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                if node.id in FORBIDDEN_NAMES:
                    findings.append("DYNAMIC:FORBIDDEN_NAME:" + node.id)
                if node.id in FORBIDDEN_NUMERIC_NAMES:
                    findings.append("NUMERIC:FORBIDDEN_NAME:" + node.id)
                if node.id == "open":
                    findings.append("DATA_LOADER:BUILTIN_OPEN")
            elif isinstance(node, ast.Attribute):
                if node.attr in FORBIDDEN_ATTRIBUTES:
                    findings.append("CAPABILITY:FORBIDDEN_ATTRIBUTE:" + node.attr)
                if node.attr in FORBIDDEN_NUMERIC_NAMES:
                    findings.append("NUMERIC:FORBIDDEN_ATTRIBUTE:" + node.attr)
                if node.attr in {"__dict__", "__globals__", "__subclasses__"}:
                    findings.append("DYNAMIC:FORBIDDEN_DUNDER:" + node.attr)
                if node.attr in {"open", "read_bytes", "read_text", "write_bytes", "write_text"} and (
                    relative != "equivariant_clock/protocol.py"
                ):
                    findings.append("DATA_LOADER:UNREVIEWED_PATH_IO:" + node.attr)
            elif isinstance(node, ast.Call) and not isinstance(node.func, (ast.Name, ast.Attribute)):
                findings.append("DYNAMIC:UNRESOLVED_CALL_TARGET")
        unique = sorted(set(findings))
        records.append({"path": relative, "ast_sha256": observed, "errors": unique, "pass": not unique})
        errors.extend(relative + ":" + item for item in unique)
    constants_tree = ast.parse(
        stable_file_bytes(root / "equivariant_clock/constants.py").decode("utf-8")
    )
    frozen_checks = {
        "matrix_literal_exact": _literal_assignment(constants_tree, "CAT_MATRIX") == CAT_MATRIX,
        "moduli_literal_exact": _literal_assignment(constants_tree, "LOCKED_MODULI") == LOCKED_MODULI,
        "primes_literal_exact": _literal_assignment(constants_tree, "LOCKED_PRIMES") == LOCKED_PRIMES,
        "composites_literal_exact": _literal_assignment(constants_tree, "LOCKED_COMPOSITES") == LOCKED_COMPOSITES,
        "structural_control_literal_exact": _literal_assignment(constants_tree, "STRUCTURAL_CONTROL") == STRUCTURAL_CONTROL,
    }
    if not all(frozen_checks.values()):
        errors.append("FROZEN_SCIENTIFIC_LITERALS_NOT_EXACT")
    return {
        "stage": "P2_CLOSED_WORLD_EXECUTABLE_SCAN",
        "records": records,
        "frozen_literal_checks": frozen_checks,
        "capability_findings": sum(
            item.startswith("CAPABILITY:") for record in records for item in record["errors"]
        ),
        "data_loader_findings": sum(
            item.startswith("DATA_LOADER:") for record in records for item in record["errors"]
        ),
        "dynamic_findings": sum(
            item.startswith("DYNAMIC:") for record in records for item in record["errors"]
        ),
        "floating_findings": sum(
            item.startswith("FLOAT:") for record in records for item in record["errors"]
        ),
        "numeric_findings": sum(
            item.startswith("NUMERIC:") for record in records for item in record["errors"]
        ),
        "errors": errors,
        "pass": not errors,
    }
