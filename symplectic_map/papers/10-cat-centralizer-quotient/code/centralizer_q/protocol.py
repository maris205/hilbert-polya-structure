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
        flags |= os.O_EXCL
        descriptor = os.open(os.fspath(absolute), flags, 0o600)
        try:
            _write_all(descriptor, data)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        _fsync_parent_directory(absolute)
        return
    temporary = absolute.parent / ("." + absolute.name + ".paper10-write")
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
            continue
        if stat.S_ISDIR(metadata.st_mode):
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


# Populated only after the complete executable tree is frozen.  The protocol
# module's digest excludes this one assignment, avoiding a self-hash cycle.
EXPECTED_EXECUTABLE_AST_SHA256: dict[str, str] = {
    "centralizer_q/__init__.py": "822217531913b82d743cd1cd18c9d192e640394fce3efbd29a9e3c368a9aa646",
    "centralizer_q/candidate.py": "5ace7c12388fe89192b2da6cb3b2c011bd1ea29afce1d0a54a80b39fe8d23bfa",
    "centralizer_q/cli.py": "2bd99aa977566e982975ca33c834a106f0194aa6fcca4a36b0c156212e458ea5",
    "centralizer_q/constants.py": "d235a0ad7d006bf94dad2b04089c1dcae3d83c9486ae5626255e3e1b6d8edb8f",
    "centralizer_q/finite_module.py": "ba1d26525cfdb86def524ba7a9ff9c88565fdcdbcecebb183bd9401ee66fce9a",
    "centralizer_q/gates.py": "abdc101861fa9f26108c3e7ee1864bec6ca1f51236ead8eb66f1f78a2b4ead51",
    "centralizer_q/lifecycle.py": "deec2aeac260ad70caa631a26e54c8167b7277c040c517dde1e3ad3b402ae5a5",
    "centralizer_q/manifest.py": "9d7126dbfc5f12c8c0ab9f4b9b5d54967cee9ea95b75617a389a11179c59f797",
    "centralizer_q/protocol.py": "f502e245737aaf201c6d6efb19bb7e2ce6749eb6ec02dd8d1fc7940dc8f6053f",
    "centralizer_q/review.py": "4a921c183af98dd83a535ce7e0aa4dfa5c4aef5ca8042ae39b242f605b21d286",
    "scripts/build_result_manifest.py": "410bd1b527bf4b595da44cba7bbb493f79dbb23a91fef8e6dba6d066bddbd82c",
    "scripts/run_registered_audit.py": "49569128dafcbaa6aff5791b4eae6799d852a64eb99e110153718f1cfd49f71d",
    "scripts/run_safe_preflight.py": "edbfcdec69d9b6549bb62df8c746f4de06d706e1853f9638fec4d22e4dc99c54",
    "scripts/show_code_hash.py": "dfdff42619854f0048468b9de1d9aa5c1d16014563bd9c911048a936d4dc082d",
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
    if relative == "centralizer_q/protocol.py":
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
        if item.endswith(".py") and (item.startswith("centralizer_q/") or item.startswith("scripts/"))
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
                    relative != "centralizer_q/protocol.py"
                ):
                    findings.append("DATA_LOADER:UNREVIEWED_PATH_IO:" + node.attr)
            elif isinstance(node, ast.Call) and not isinstance(node.func, (ast.Name, ast.Attribute)):
                findings.append("DYNAMIC:UNRESOLVED_CALL_TARGET")
        unique = sorted(set(findings))
        records.append({"path": relative, "ast_sha256": observed, "errors": unique, "pass": not unique})
        errors.extend(relative + ":" + item for item in unique)
    constants_tree = ast.parse(stable_file_bytes(root / "centralizer_q/constants.py").decode("utf-8"))
    frozen_checks = {
        "matrix_literal_exact": _literal_assignment(constants_tree, "CAT_MATRIX") == CAT_MATRIX,
        "moduli_literal_exact": _literal_assignment(constants_tree, "LOCKED_MODULI") == LOCKED_MODULI,
        "primes_literal_exact": _literal_assignment(constants_tree, "LOCKED_PRIMES") == LOCKED_PRIMES,
        "composites_literal_exact": _literal_assignment(constants_tree, "LOCKED_COMPOSITES") == LOCKED_COMPOSITES,
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
