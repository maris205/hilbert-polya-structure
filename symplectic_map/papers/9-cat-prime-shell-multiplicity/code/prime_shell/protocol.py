"""Strict JSON, stable filesystem reads, closed-tree hashing, and code isolation."""

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
    LOCKED_PRIMES,
    REPEATS,
)


class DuplicateJSONKeyError(ValueError):
    """Raised when exact evidence repeats a JSON object key."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(text: str) -> Any:
    def reject_nonfinite(value: str) -> None:
        raise ValueError(f"non-finite JSON constant is forbidden: {value}")

    return json.loads(
        text,
        object_pairs_hook=_unique_object,
        parse_constant=reject_nonfinite,
    )


def _contains_float(value: Any) -> bool:
    if type(value) is float:
        return True
    if type(value) is list:
        return any(_contains_float(item) for item in value)
    if type(value) is dict:
        return any(_contains_float(key) or _contains_float(item) for key, item in value.items())
    return False


def exact_json(value: Any) -> Any:
    if _contains_float(value):
        raise ValueError("floating values are forbidden in exact evidence")
    return value


def json_safe(value: Any) -> Any:
    if type(value) is dict:
        return {str(key): json_safe(item) for key, item in value.items()}
    if type(value) in {list, tuple}:
        return [json_safe(item) for item in value]
    if isinstance(value, Path):
        return os.fspath(value)
    if type(value) is float:
        raise TypeError("floating values are forbidden in exact JSON")
    if value is None or type(value) in {str, int, bool}:
        return value
    raise TypeError(f"unsupported exact JSON value: {type(value).__name__}")


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        json_safe(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def pretty_json_bytes(value: Any) -> bytes:
    return (json.dumps(json_safe(value), indent=2, sort_keys=True) + "\n").encode("utf-8")


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _reject_symlink_components(path: Path) -> None:
    absolute = lexical_absolute(path)
    current = Path(absolute.anchor)
    for component in absolute.parts[1:]:
        current = current / component
        metadata = current.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            raise ValueError(f"symlink path component is forbidden: {current}")


def regular_directory(path: Path) -> bool:
    try:
        _reject_symlink_components(path)
        metadata = lexical_absolute(path).stat()
    except (FileNotFoundError, OSError, ValueError):
        return False
    return stat.S_ISDIR(metadata.st_mode)


def regular_file(path: Path) -> bool:
    absolute = lexical_absolute(path)
    try:
        _reject_symlink_components(absolute.parent)
        metadata = absolute.lstat()
    except (FileNotFoundError, OSError, ValueError):
        return False
    return stat.S_ISREG(metadata.st_mode) and metadata.st_nlink == 1


def _identity(metadata: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
        metadata.st_nlink,
    )


def stable_file_bytes(path: Path) -> bytes:
    absolute = lexical_absolute(path)
    if not regular_file(absolute):
        raise ValueError(f"not a safe single-link regular file: {absolute}")
    flags = os.O_RDONLY | os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(absolute, flags)
    try:
        before = os.fstat(descriptor)
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    terminal = absolute.lstat()
    if not stat.S_ISREG(terminal.st_mode) or terminal.st_nlink != 1:
        raise RuntimeError(f"file type changed during read: {absolute}")
    if _identity(before) != _identity(after) or _identity(after) != _identity(terminal):
        raise RuntimeError(f"file changed during stable read: {absolute}")
    return b"".join(chunks)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(stable_file_bytes(path)).hexdigest()


def load_exact_json(path: Path) -> Any:
    payload = strict_json_loads(stable_file_bytes(path).decode("utf-8"))
    return exact_json(payload)


def _write_all(descriptor: int, data: bytes) -> None:
    offset = 0
    while offset < len(data):
        offset += os.write(descriptor, data[offset:])


def _fsync_parent_directory(path: Path) -> None:
    parent = lexical_absolute(path).parent
    flags = os.O_RDONLY | os.O_CLOEXEC
    if hasattr(os, "O_DIRECTORY"):
        flags |= os.O_DIRECTORY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(parent, flags)
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISDIR(metadata.st_mode):
            raise ValueError(f"output parent is not a directory: {parent}")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_bytes(path: Path, data: bytes, *, exclusive: bool = False) -> None:
    absolute = lexical_absolute(path)
    if not regular_directory(absolute.parent):
        raise ValueError(f"unsafe or missing output directory: {absolute.parent}")
    flags = os.O_WRONLY | os.O_CREAT | os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    if exclusive:
        descriptor = os.open(absolute, flags | os.O_EXCL, 0o600)
        try:
            _write_all(descriptor, data)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        _fsync_parent_directory(absolute)
        return
    if absolute.exists() and not regular_file(absolute):
        raise ValueError(f"refusing to replace unsafe output: {absolute}")
    temporary = absolute.parent / f".{absolute.name}.prime-shell-safe-tmp"
    try:
        descriptor = os.open(temporary, flags | os.O_EXCL, 0o600)
        try:
            _write_all(descriptor, data)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        os.replace(temporary, absolute)
        _fsync_parent_directory(absolute)
    except BaseException:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def write_json(path: Path, value: Any, *, exclusive: bool = False) -> None:
    write_bytes(path, pretty_json_bytes(value), exclusive=exclusive)


def _inventory_once(code_root: Path) -> dict[str, Any]:
    root = lexical_absolute(code_root)
    files: list[str] = []
    directories: list[str] = []
    symlinks: list[str] = []
    unsupported: list[str] = []
    if not regular_directory(root):
        return {
            "files": [],
            "directories": [],
            "symlinks": ["<unsafe-code-root>"],
            "unsupported": [],
        }
    for entry in sorted(root.iterdir(), key=lambda item: item.name):
        metadata = entry.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            symlinks.append(entry.name)
        elif stat.S_ISDIR(metadata.st_mode):
            directories.append(entry.name)
            if entry.name not in CODE_DIRECTORIES:
                unsupported.append("directory:" + entry.name)
                continue
            for child in sorted(entry.iterdir(), key=lambda item: item.name):
                relative = f"{entry.name}/{child.name}"
                child_metadata = child.lstat()
                if stat.S_ISLNK(child_metadata.st_mode):
                    symlinks.append(relative)
                elif stat.S_ISREG(child_metadata.st_mode):
                    if child_metadata.st_nlink != 1:
                        unsupported.append("hardlink:" + relative)
                    elif child.name.endswith(".pyc"):
                        unsupported.append("generated:" + relative)
                    else:
                        files.append(relative)
                elif stat.S_ISDIR(child_metadata.st_mode):
                    unsupported.append("nested-directory:" + relative)
                else:
                    unsupported.append(relative)
        elif stat.S_ISREG(metadata.st_mode):
            if metadata.st_nlink != 1:
                unsupported.append("hardlink:" + entry.name)
            else:
                files.append(entry.name)
        else:
            unsupported.append(entry.name)
    return {
        "files": sorted(files),
        "directories": sorted(directories),
        "symlinks": sorted(symlinks),
        "unsupported": sorted(unsupported),
    }


def code_inventory(code_root: Path) -> dict[str, Any]:
    first = _inventory_once(code_root)
    second = _inventory_once(code_root)
    errors: list[str] = []
    if first != second:
        errors.append("CODE_INVENTORY_UNSTABLE")
    discovered = set(first["files"])
    missing = sorted(CODE_FILES.difference(discovered))
    extra = sorted(discovered.difference(CODE_FILES))
    if missing:
        errors.append("CODE_FILES_MISSING")
    if extra:
        errors.append("CODE_FILES_EXTRA")
    if set(first["directories"]) != set(CODE_DIRECTORIES):
        errors.append("CODE_DIRECTORIES_NOT_EXACT")
    if first["symlinks"]:
        errors.append("CODE_SYMLINKS_FORBIDDEN")
    if first["unsupported"]:
        errors.append("CODE_UNSUPPORTED_ENTRIES")
    return {
        **first,
        "missing": missing,
        "extra": extra,
        "errors": errors,
        "pass": not errors,
    }


def reviewed_tree_paths(project_root: Path) -> tuple[str, ...]:
    return tuple(
        sorted(
            set(DESIGN_REVIEWED_PATHS)
            | {f"code/{relative}" for relative in CODE_FILES}
        )
    )


def code_tree_sha256(project_root: Path) -> str:
    root = lexical_absolute(project_root)
    inventory = code_inventory(root / "code")
    if inventory["pass"] is not True:
        raise ValueError("code tree is not the exact closed-world inventory")
    paths = reviewed_tree_paths(root)

    def hash_once() -> str:
        digest = hashlib.sha256()
        for relative in paths:
            encoded = relative.encode("utf-8")
            content = stable_file_bytes(root / relative)
            digest.update(len(encoded).to_bytes(8, "big"))
            digest.update(encoded)
            digest.update(len(content).to_bytes(8, "big"))
            digest.update(content)
        return digest.hexdigest()

    first = hash_once()
    middle = code_inventory(root / "code")
    second = hash_once()
    if first != second or inventory != middle:
        raise RuntimeError("reviewed tree changed during framed hashing")
    return first


EXPECTED_IMPORT_SIGNATURES = {
    "prime_shell/__init__.py": ("from:.constants:CANDIDATE_ID",),
    "prime_shell/candidate.py": (
        "from:__future__:annotations",
        "from:typing:Any",
        "from:.constants:CANDIDATE_ID,EXPECTED_LEDGER,EXPECTED_RAW_FACTORS,LOCKED_PRIMES,SOURCE_LOCK_SHA256,TERMINAL_LABELS",
        "from:.finite_field:analytic_case_certificate,comparison_projection,direct_enumeration_certificate,expected_projection",
        "from:.mechanisms:mechanism_audit,symbolic_composite_control",
        "from:.proof_contract:proof_only_contract,validate_proof_only_contract",
        "from:.protocol:canonical_json_bytes",
        "from:.symbolic:symbolic_product_audit",
    ),
    "prime_shell/cli.py": (
        "from:__future__:annotations",
        "import:argparse",
        "import:json",
        "import:sys",
        "from:pathlib:Path",
        "from:.constants:CLAIM_PATH,PREEXECUTION_AUDIT_PATH,RESULT_PATH,TERMINAL_PATH",
        "from:.gates:collect_safe_preflight,write_safe_preflight",
        "from:.lifecycle:claim_registered_run,validate_claim,write_terminal",
        "from:.manifest:collect_postrun_audit,validate_registered_result,write_result_manifest",
        "from:.protocol:code_tree_sha256,lexical_absolute,regular_file,sha256_file,write_json",
        "from:.review:validate_deployment_authority",
        "from:.candidate:RegisteredCandidateFailure,run_registered_candidate",
    ),
    "prime_shell/constants.py": (
        "from:__future__:annotations",
        "from:typing:Final",
    ),
    "prime_shell/finite_field.py": (
        "from:__future__:annotations",
        "from:collections:Counter",
        "from:typing:Any,Iterable",
        "from:.constants:CAT_MATRIX,EXPECTED_LEDGER,IDENTITY,LOCKED_PRIMES",
    ),
    "prime_shell/gates.py": (
        "from:__future__:annotations",
        "import:hashlib",
        "import:xml.etree.ElementTree as element_tree",
        "from:pathlib:Path",
        "from:typing:Any",
        "from:.constants:CANDIDATE_ID,CAT_MATRIX,CLAIM_PATH,LOCAL_BINDINGS,LOCKED_PRIMES,PREEXECUTION_AUDIT_PATH,PREEXECUTION_TEST_PATH,RESULT_PATH,REPEATS,SOURCE_LOCK_SHA256,SOURCE_REVIEW_SHA256,TERMINAL_PATH,UPSTREAM_BINDINGS",
        "from:.proof_contract:proof_only_contract,validate_proof_only_contract",
        "from:.protocol:code_tree_sha256,executable_isolation_scan,lexical_absolute,load_exact_json,regular_file,sha256_file,stable_file_bytes,write_json",
        "from:.review:validate_deployment_authority",
    ),
    "prime_shell/lifecycle.py": (
        "from:__future__:annotations",
        "from:pathlib:Path",
        "from:typing:Any",
        "from:.constants:CANDIDATE_ID,CLAIM_PATH,CODE_REVIEW_PATH,LOCKED_PRIMES,PREEXECUTION_AUDIT_PATH,PREEXECUTION_TEST_PATH,RESULT_PATH,SOURCE_LOCK_SHA256,TERMINAL_PATH",
        "from:.protocol:lexical_absolute,load_exact_json,regular_file,sha256_file,write_json",
    ),
    "prime_shell/manifest.py": (
        "from:__future__:annotations",
        "import:hashlib",
        "from:pathlib:Path",
        "from:typing:Any",
        "from:.constants:CAT_MATRIX,CANDIDATE_ID,CLAIM_PATH,CODE_REVIEW_PATH,EXPECTED_LEDGER,EXPECTED_RAW_FACTORS,LOCKED_PRIMES,OFFICIAL_REPORT_PATHS,POSTRUN_TEST_PATH,PREEXECUTION_AUDIT_PATH,PREEXECUTION_TEST_PATH,RESULT_MANIFEST_PATH,RESULT_PATH,RESULT_REVIEW_PATH,SOURCE_LOCK_SHA256,TERMINAL_LABELS,TERMINAL_PATH",
        "from:.mechanisms:mechanism_audit,symbolic_composite_control",
        "from:.gates:collect_safe_preflight,parse_junit,validate_source_and_design,validate_upstream",
        "from:.lifecycle:validate_claim",
        "from:.proof_contract:proof_only_contract,validate_proof_only_contract",
        "from:.protocol:canonical_json_bytes,code_tree_sha256,lexical_absolute,load_exact_json,regular_file,sha256_file,stable_file_bytes,strict_json_loads,pretty_json_bytes,write_json",
        "from:.review:validate_deployment_authority,validate_result_authority",
        "from:.symbolic:symbolic_product_audit",
    ),
    "prime_shell/mechanisms.py": (
        "from:__future__:annotations",
        "from:fractions:Fraction",
        "from:typing:Any",
        "from:.constants:REPEATS",
        "from:.symbolic:fraction_text",
    ),
    "prime_shell/proof_contract.py": (
        "from:__future__:annotations",
        "from:typing:Any",
        "from:.constants:OUTSIDE_SCOPE_ESCAPES,REQUIRED_ANALYTIC_CONTRACTS",
    ),
    "prime_shell/protocol.py": (
        "from:__future__:annotations",
        "import:ast",
        "import:hashlib",
        "import:json",
        "import:os",
        "import:stat",
        "from:pathlib:Path",
        "from:typing:Any",
        "from:.constants:CAT_MATRIX,CODE_DIRECTORIES,CODE_FILES,DESIGN_REVIEWED_PATHS,LOCKED_PRIMES,REPEATS",
    ),
    "prime_shell/review.py": (
        "from:__future__:annotations",
        "import:hashlib",
        "import:json",
        "from:pathlib:Path",
        "from:typing:Any",
        "from:.constants:CANDIDATE_ID,CODE_REVIEW_PATH,PREEXECUTION_TEST_PATH,RESULT_PATH,RESULT_REVIEW_PATH,SOURCE_LOCK_SHA256",
        "from:.protocol:code_tree_sha256,regular_file,sha256_file,stable_file_bytes,strict_json_loads",
    ),
    "prime_shell/symbolic.py": (
        "from:__future__:annotations",
        "from:fractions:Fraction",
        "from:typing:Any",
        "from:.constants:REPEATS",
    ),
    "scripts/build_result_manifest.py": (
        "import:sys",
        "from:pathlib:Path",
        "from:prime_shell.cli:main",
    ),
    "scripts/run_registered_audit.py": (
        "import:sys",
        "from:pathlib:Path",
        "from:prime_shell.cli:main",
    ),
    "scripts/run_safe_preflight.py": (
        "import:sys",
        "from:pathlib:Path",
        "from:prime_shell.cli:main",
    ),
    "scripts/show_code_hash.py": (
        "import:sys",
        "from:pathlib:Path",
        "from:prime_shell.cli:main",
    ),
}
# Filled with canonical, location-free AST digests for every executable file.
# The protocol entry excludes only this assignment itself, avoiding a digest
# fixed point while keeping the scanner implementation and every capability
# policy constant inside the signed AST body.
EXPECTED_EXECUTABLE_AST_SHA256: dict[str, str] = {
    "prime_shell/__init__.py": "d8babb8d32d86fd4a39e028bb61afcc66b3feda51209c9275802f99c14407f24",
    "prime_shell/candidate.py": "1544e4860b5f7e518953fee99923cbcc9fa38330b5a7e7bd7be960cdeefa21ab",
    "prime_shell/cli.py": "2a480be4212e2a86129783837975fbd05106fd96adc9186a98457b5b28c180d5",
    "prime_shell/constants.py": "9c5ef2ed37a7b795bb693d050a4c8bd58c8856fd444147e83ffefe52d144c67d",
    "prime_shell/finite_field.py": "a651b7095ae51052f5ecb59f1711e585d72a1cf21775066d87aa996afd36bc26",
    "prime_shell/gates.py": "410d4c2ea94340569ead2b1ccc6fa1df3416d8b07129acbbe8c5f0e8df50501f",
    "prime_shell/lifecycle.py": "4da0f4dc8836e1043a057b372b59e6e6da35254a752c74dd7ea0ba7ff4db2f55",
    "prime_shell/manifest.py": "8347ecf4e27115ce1f5c2631e31213ba7841d0f3a65e69190e642ac65f801ef1",
    "prime_shell/mechanisms.py": "825b3aadae705ce466578ff475b8384557bba61c5130749df546b4f35c72b374",
    "prime_shell/proof_contract.py": "3cdb6ddda80fb50ef35ac358b2974f9c7302157da1a44ca2d561104b32476006",
    "prime_shell/protocol.py": "698c62c263da74c9b048ebb04e4b2df72c271afcb0a4a2ce101a900d128dcb6d",
    "prime_shell/review.py": "e6334539974f352a5e56e7cd3820ee5d2acbfc2292dbf0936bfbb8784054b661",
    "prime_shell/symbolic.py": "4ac134d05126a076cc8c98dc89926f2580ce7f55a4ef036a181ef4d2fe3ea919",
    "scripts/build_result_manifest.py": "d0bb21282e83dd6dc2f26b5c71b5b02ce53efa54001a2bae6a3cabd8d6a668f0",
    "scripts/run_registered_audit.py": "9846eb7b978f1940f4a63ffe47d6f509c8c4bebd981d0df24ad24aa7b2ee33f1",
    "scripts/run_safe_preflight.py": "5cfca61dd0595e744617bf1ea250ac3bf512699ea212aed67217d71596c74aca",
    "scripts/show_code_hash.py": "f6401f3398157a2c65fc9f2d2732f94c535522cdf44fb846867dc5fe1066be13",
}
NETWORK_IMPORT_ROOTS = frozenset(
    {"asyncio", "ftplib", "http", "requests", "socket", "ssl", "urllib"}
)
PROCESS_ATTRIBUTES = frozenset(
    {"exec", "execl", "execle", "execlp", "execlpe", "execv", "execve", "execvp", "execvpe", "fork", "kill", "popen", "spawn", "system"}
)
NETWORK_ATTRIBUTES = frozenset(
    {"accept", "bind", "connect", "listen", "request", "socket", "urlopen"}
)
DATA_LOADER_ATTRIBUTES = frozenset(
    {"load", "read_bytes", "read_csv", "read_json", "read_pickle", "read_table", "read_text"}
)
DYNAMIC_NAMES = frozenset(
    {
        "__builtins__",
        "__import__",
        "compile",
        "delattr",
        "eval",
        "exec",
        "getattr",
        "globals",
        "locals",
        "setattr",
        "vars",
    }
)
NUMERIC_FORBIDDEN_NAMES = frozenset({"exp", "log", "log10"})
SAFE_DUNDER_ATTRIBUTES = frozenset({"__init__", "__name__"})

# These are closed-world, AST-derived filesystem capability sites.  The
# deployment scanner does not infer safety from an API spelling: every use of
# the already imported ``os`` module, and every filesystem-touching ``Path``
# method call, must occur in the reviewed file and function with the exact
# canonical target shape recorded here.  Repeated entries are intentional and
# bind the number of reviewed call sites as well as their location.
EXPECTED_OS_ATTRIBUTE_SITES = {
    "prime_shell/protocol.py": tuple(
        sorted(
            (
                "_fsync_parent_directory|os.O_CLOEXEC",
                "_fsync_parent_directory|os.O_DIRECTORY",
                "_fsync_parent_directory|os.O_NOFOLLOW",
                "_fsync_parent_directory|os.O_RDONLY",
                "_fsync_parent_directory|os.close",
                "_fsync_parent_directory|os.fstat",
                "_fsync_parent_directory|os.fsync",
                "_fsync_parent_directory|os.open",
                "_identity|os.stat_result",
                "_write_all|os.write",
                "json_safe|os.fspath",
                "lexical_absolute|os.fspath",
                "lexical_absolute|os.path",
                "lexical_absolute|os.path.abspath",
                "stable_file_bytes|os.O_CLOEXEC",
                "stable_file_bytes|os.O_NOFOLLOW",
                "stable_file_bytes|os.O_RDONLY",
                "stable_file_bytes|os.close",
                "stable_file_bytes|os.fstat",
                "stable_file_bytes|os.fstat",
                "stable_file_bytes|os.open",
                "stable_file_bytes|os.read",
                "write_bytes|os.O_CLOEXEC",
                "write_bytes|os.O_CREAT",
                "write_bytes|os.O_EXCL",
                "write_bytes|os.O_EXCL",
                "write_bytes|os.O_NOFOLLOW",
                "write_bytes|os.O_WRONLY",
                "write_bytes|os.close",
                "write_bytes|os.close",
                "write_bytes|os.fsync",
                "write_bytes|os.fsync",
                "write_bytes|os.open",
                "write_bytes|os.open",
                "write_bytes|os.replace",
            )
        )
    )
}
EXPECTED_BARE_OS_SITES = {
    "prime_shell/protocol.py": tuple(
        sorted(
            (
                "_fsync_parent_directory|hasattr(os, 'O_DIRECTORY')",
                "_fsync_parent_directory|hasattr(os, 'O_NOFOLLOW')",
                "stable_file_bytes|hasattr(os, 'O_NOFOLLOW')",
                "write_bytes|hasattr(os, 'O_NOFOLLOW')",
            )
        )
    )
}
FILESYSTEM_PATH_METHODS = frozenset(
    {
        "absolute",
        "chmod",
        "exists",
        "expanduser",
        "glob",
        "group",
        "hardlink_to",
        "home",
        "is_block_device",
        "is_char_device",
        "is_dir",
        "is_fifo",
        "is_file",
        "is_junction",
        "is_mount",
        "is_socket",
        "is_symlink",
        "iterdir",
        "lchmod",
        "link_to",
        "lstat",
        "mkdir",
        "open",
        "owner",
        "read_bytes",
        "read_text",
        "readlink",
        "rename",
        "replace",
        "resolve",
        "rglob",
        "rmdir",
        "samefile",
        "stat",
        "symlink_to",
        "touch",
        "unlink",
        "walk",
        "write_bytes",
        "write_text",
    }
)
NON_PATH_MODULE_ROOTS = frozenset(
    {"ast", "element_tree", "hashlib", "json", "stat"}
)
EXPECTED_PATH_CALL_SITES = {
    "prime_shell/lifecycle.py": (
        "result_file_names|results.iterdir()",
    ),
    "prime_shell/manifest.py": tuple(
        sorted(
            (
                "_evidence_inventory|root.iterdir()",
                "_evidence_inventory|root.iterdir()",
                "_result_inventory|root.iterdir()",
                "_result_inventory|root.iterdir()",
                "write_result_manifest|output.exists()",
            )
        )
    ),
    "prime_shell/protocol.py": tuple(
        sorted(
            (
                "_inventory_once|child.lstat()",
                "_inventory_once|entry.iterdir()",
                "_inventory_once|entry.lstat()",
                "_inventory_once|root.iterdir()",
                "_reject_symlink_components|current.lstat()",
                "regular_directory|lexical_absolute(path).stat()",
                "regular_file|absolute.lstat()",
                "stable_file_bytes|absolute.lstat()",
                "write_bytes|absolute.exists()",
                "write_bytes|temporary.unlink()",
            )
        )
    ),
    "scripts/build_result_manifest.py": (
        "<module>|Path(__file__).absolute()",
    ),
    "scripts/run_registered_audit.py": (
        "<module>|Path(__file__).absolute()",
    ),
    "scripts/run_safe_preflight.py": (
        "<module>|Path(__file__).absolute()",
    ),
    "scripts/show_code_hash.py": (
        "<module>|Path(__file__).absolute()",
    ),
}


def _assignment_literal(tree: ast.AST, name: str) -> Any:
    if not isinstance(tree, ast.Module):
        raise ValueError("frozen assignment scan requires a module AST")
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return ast.literal_eval(node.value)
    raise ValueError(f"required frozen assignment missing: {name}")


def _import_signature(node: ast.Import | ast.ImportFrom) -> str:
    if isinstance(node, ast.Import):
        return "import:" + ",".join(
            alias.name + (" as " + alias.asname if alias.asname else "")
            for alias in node.names
        )
    module = "." * node.level + (node.module or "")
    names = ",".join(
        alias.name + (" as " + alias.asname if alias.asname else "")
        for alias in node.names
    )
    return f"from:{module}:{names}"


def _is_ast_digest_assignment(node: ast.AST) -> bool:
    if isinstance(node, ast.Assign):
        return any(
            isinstance(target, ast.Name)
            and target.id == "EXPECTED_EXECUTABLE_AST_SHA256"
            for target in node.targets
        )
    if isinstance(node, ast.AnnAssign):
        return (
            isinstance(node.target, ast.Name)
            and node.target.id == "EXPECTED_EXECUTABLE_AST_SHA256"
        )
    return False


def _executable_ast_sha256(tree: ast.AST, relative: str) -> str:
    if not isinstance(tree, ast.Module):
        raise ValueError("executable signature requires a module AST")
    body = list(tree.body)
    if relative == "prime_shell/protocol.py":
        body = [node for node in body if not _is_ast_digest_assignment(node)]
    canonical = ast.dump(
        ast.Module(body=body, type_ignores=tree.type_ignores),
        annotate_fields=True,
        include_attributes=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _assigned_names(node: ast.AST) -> set[str]:
    if isinstance(node, ast.Name):
        return {node.id}
    if isinstance(node, (ast.Tuple, ast.List)):
        return set().union(*(_assigned_names(item) for item in node.elts))
    return set()


def _capability_expression(value: ast.AST, tainted_names: set[str]) -> bool:
    for node in ast.walk(value):
        if isinstance(node, ast.Name) and node.id in (DYNAMIC_NAMES | tainted_names):
            return True
        if isinstance(node, ast.Attribute) and (
            node.attr in PROCESS_ATTRIBUTES
            or node.attr in NETWORK_ATTRIBUTES
            or node.attr in DATA_LOADER_ATTRIBUTES
            or node.attr in {"modules", "__dict__"}
            or (node.attr.startswith("__") and node.attr not in SAFE_DUNDER_ATTRIBUTES)
        ):
            return True
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in tainted_names
        ):
            return True
    return False


def _attribute_root_name(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _filesystem_category(attribute: str) -> str:
    """Classify an already-unreviewed site; detection itself is allowlist-only."""

    if attribute.startswith(("exec", "spawn")) or attribute in {
        "fork",
        "forkpty",
        "kill",
        "popen",
        "system",
    }:
        return "PROCESS"
    if attribute in NETWORK_ATTRIBUTES or attribute.startswith(
        ("socket", "send", "recv")
    ):
        return "NETWORK"
    if attribute in {
        "open",
        "pread",
        "preadv",
        "read",
        "readv",
    }:
        return "DATA_LOADER"
    return "DYNAMIC"


class _FilesystemSiteCollector(ast.NodeVisitor):
    """Collect canonical filesystem sites while retaining lexical scope."""

    def __init__(self, parents: dict[ast.AST, ast.AST]) -> None:
        self.parents = parents
        self.scopes = ["<module>"]
        self.os_attributes: list[tuple[str, str, int]] = []
        self.bare_os: list[tuple[str, int]] = []
        self.path_calls: list[tuple[str, str, int]] = []

    @property
    def scope(self) -> str:
        return ".".join(self.scopes[1:]) if len(self.scopes) > 1 else "<module>"

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.scopes.append(node.name)
        self.generic_visit(node)
        self.scopes.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.scopes.append(node.name)
        self.generic_visit(node)
        self.scopes.pop()

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if _attribute_root_name(node) == "os":
            self.os_attributes.append(
                (self.scope + "|" + ast.unparse(node), node.attr, node.lineno)
            )
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> None:
        if node.id == "os" and isinstance(node.ctx, ast.Load):
            parent = self.parents.get(node)
            is_attribute_root = isinstance(parent, ast.Attribute) and parent.value is node
            if not is_attribute_root:
                parent_text = ast.unparse(parent) if parent is not None else "<missing-parent>"
                self.bare_os.append((self.scope + "|" + parent_text, node.lineno))
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute) and node.func.attr in FILESYSTEM_PATH_METHODS:
            root_name = _attribute_root_name(node.func)
            if root_name not in NON_PATH_MODULE_ROOTS and root_name != "os":
                self.path_calls.append(
                    (
                        self.scope + "|" + ast.unparse(node),
                        node.func.attr,
                        node.lineno,
                    )
                )
        self.generic_visit(node)


def _filesystem_sites(
    tree: ast.AST,
) -> tuple[
    list[tuple[str, str, int]],
    list[tuple[str, int]],
    list[tuple[str, str, int]],
]:
    parents = {
        child: parent
        for parent in ast.walk(tree)
        for child in ast.iter_child_nodes(parent)
    }
    collector = _FilesystemSiteCollector(parents)
    collector.visit(tree)
    return collector.os_attributes, collector.bare_os, collector.path_calls


def _unexpected_sites(
    observed: list[tuple[str, str, int]], expected: tuple[str, ...]
) -> tuple[list[tuple[str, int]], list[str]]:
    remaining = list(expected)
    unexpected: list[tuple[str, int]] = []
    for signature, attribute, line in observed:
        if signature in remaining:
            remaining.remove(signature)
        else:
            unexpected.append((attribute, line))
    return unexpected, remaining


def _unexpected_bare_os_sites(
    observed: list[tuple[str, int]], expected: tuple[str, ...]
) -> tuple[list[int], list[str]]:
    remaining = list(expected)
    unexpected: list[int] = []
    for signature, line in observed:
        if signature in remaining:
            remaining.remove(signature)
        else:
            unexpected.append(line)
    return unexpected, remaining


def executable_isolation_scan(code_root: Path) -> dict[str, Any]:
    root = lexical_absolute(code_root)
    inventory = code_inventory(root)
    errors = list(inventory["errors"])
    records: list[dict[str, Any]] = []
    executable_paths = sorted(
        relative
        for relative in CODE_FILES
        if (relative.startswith("prime_shell/") or relative.startswith("scripts/"))
        and relative.endswith(".py")
    )
    for relative in executable_paths:
        path = root / relative
        file_errors: list[str] = []
        try:
            text = stable_file_bytes(path).decode("utf-8")
            tree = ast.parse(text, filename=relative)
        except (OSError, UnicodeDecodeError, SyntaxError, ValueError, RuntimeError):
            file_errors.append("UNREADABLE_OR_INVALID_PYTHON")
            records.append({"path": relative, "errors": file_errors, "pass": False})
            continue
        findings: list[dict[str, Any]] = []

        def finding(category: str, code: str, line: int) -> None:
            findings.append({"category": category, "code": code, "line": line})

        import_nodes = [
            node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))
        ]
        observed_imports = tuple(_import_signature(node) for node in import_nodes)
        expected_imports = EXPECTED_IMPORT_SIGNATURES.get(relative)
        if observed_imports != expected_imports:
            finding("IMPORT_POLICY", "IMPORT_SIGNATURE_NOT_EXACT", 0)
        observed_ast_sha256 = _executable_ast_sha256(tree, relative)
        if EXPECTED_EXECUTABLE_AST_SHA256.get(relative) != observed_ast_sha256:
            finding("DYNAMIC", "EXECUTABLE_AST_SIGNATURE_NOT_EXACT", 0)
        os_sites, bare_os_sites, path_sites = _filesystem_sites(tree)
        unexpected_os, missing_os = _unexpected_sites(
            os_sites, EXPECTED_OS_ATTRIBUTE_SITES.get(relative, ())
        )
        for attribute, line in unexpected_os:
            finding(
                _filesystem_category(attribute),
                "UNREVIEWED_OS_ATTRIBUTE_SITE:" + attribute,
                line,
            )
        if missing_os:
            finding("DYNAMIC", "REVIEWED_OS_ATTRIBUTE_SITES_MISSING", 0)
        unexpected_bare_os, missing_bare_os = _unexpected_bare_os_sites(
            bare_os_sites, EXPECTED_BARE_OS_SITES.get(relative, ())
        )
        for line in unexpected_bare_os:
            finding("DYNAMIC", "UNREVIEWED_BARE_OS_SITE", line)
        if missing_bare_os:
            finding("DYNAMIC", "REVIEWED_BARE_OS_SITES_MISSING", 0)
        unexpected_path, missing_path = _unexpected_sites(
            path_sites, EXPECTED_PATH_CALL_SITES.get(relative, ())
        )
        for attribute, line in unexpected_path:
            finding(
                "DATA_LOADER",
                "UNREVIEWED_PATH_OPERATION_SITE:" + attribute,
                line,
            )
        if missing_path:
            finding("DYNAMIC", "REVIEWED_PATH_CALL_SITES_MISSING", 0)
        tainted_names: set[str] = set()
        changed = True
        while changed:
            changed = False
            for node in ast.walk(tree):
                targets: list[ast.AST] = []
                value: ast.AST | None = None
                if isinstance(node, ast.Assign):
                    targets = list(node.targets)
                    value = node.value
                elif isinstance(node, ast.AnnAssign):
                    targets = [node.target]
                    value = node.value
                elif isinstance(node, ast.NamedExpr):
                    targets = [node.target]
                    value = node.value
                if value is None or not _capability_expression(value, tainted_names):
                    continue
                discovered = set().union(*(_assigned_names(target) for target in targets))
                if not discovered.issubset(tainted_names):
                    tainted_names.update(discovered)
                    changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and type(node.value) is float:
                finding("FLOAT", "FLOAT_LITERAL", node.lineno)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    root_name = alias.name.split(".")[0]
                    if root_name in NETWORK_IMPORT_ROOTS:
                        finding("NETWORK", "FORBIDDEN_NETWORK_IMPORT:" + alias.name, node.lineno)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                root_name = module.split(".")[0]
                if node.level == 0 and root_name in NETWORK_IMPORT_ROOTS:
                    finding("NETWORK", "FORBIDDEN_NETWORK_IMPORT:" + module, node.lineno)
                for alias in node.names:
                    if alias.name in PROCESS_ATTRIBUTES:
                        finding("PROCESS", "FORBIDDEN_PROCESS_IMPORT:" + alias.name, node.lineno)
                    if alias.name in NETWORK_ATTRIBUTES:
                        finding("NETWORK", "FORBIDDEN_NETWORK_IMPORT_MEMBER:" + alias.name, node.lineno)
                    if alias.name in DATA_LOADER_ATTRIBUTES:
                        finding("DATA_LOADER", "FORBIDDEN_DATA_LOADER_IMPORT:" + alias.name, node.lineno)
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                if node.id in DYNAMIC_NAMES:
                    finding("DYNAMIC", "FORBIDDEN_DYNAMIC_NAME:" + node.id, node.lineno)
                elif node.id in NUMERIC_FORBIDDEN_NAMES:
                    finding("NUMERIC", "FORBIDDEN_NUMERIC_NAME:" + node.id, node.lineno)
                elif node.id == "open":
                    finding("DATA_LOADER", "FORBIDDEN_BUILTIN_OPEN", node.lineno)
            elif isinstance(node, ast.Attribute):
                if node.attr in PROCESS_ATTRIBUTES:
                    finding("PROCESS", "FORBIDDEN_PROCESS_ATTRIBUTE:" + node.attr, node.lineno)
                elif node.attr in NETWORK_ATTRIBUTES:
                    finding("NETWORK", "FORBIDDEN_NETWORK_ATTRIBUTE:" + node.attr, node.lineno)
                elif node.attr in DATA_LOADER_ATTRIBUTES:
                    finding("DATA_LOADER", "FORBIDDEN_DATA_LOADER_ATTRIBUTE:" + node.attr, node.lineno)
                elif node.attr in {"modules", "__dict__"}:
                    finding("DYNAMIC", "FORBIDDEN_DYNAMIC_ATTRIBUTE:" + node.attr, node.lineno)
                elif node.attr.startswith("__") and node.attr not in SAFE_DUNDER_ATTRIBUTES:
                    finding("DYNAMIC", "FORBIDDEN_DUNDER_ATTRIBUTE:" + node.attr, node.lineno)
                elif node.attr in {"open", "read"} and relative != "prime_shell/protocol.py":
                    finding("DATA_LOADER", "UNTRUSTED_FILE_CAPABILITY:" + node.attr, node.lineno)
            elif isinstance(node, ast.Call):
                if not isinstance(node.func, (ast.Name, ast.Attribute)):
                    finding("DYNAMIC", "UNRESOLVED_DYNAMIC_CALL_TARGET", node.lineno)
                if (
                    isinstance(node.func, ast.Name)
                    and node.func.id == "__import__"
                    and node.args
                    and isinstance(node.args[0], ast.Constant)
                    and type(node.args[0].value) is str
                    and node.args[0].value.split(".")[0] in NETWORK_IMPORT_ROOTS
                ):
                    finding("NETWORK", "DYNAMIC_NETWORK_IMPORT", node.lineno)
                if isinstance(node.func, ast.Name) and node.func.id in tainted_names:
                    finding("DYNAMIC", "TAINTED_CAPABILITY_CALL:" + node.func.id, node.lineno)
                    for argument in node.args:
                        if isinstance(argument, ast.Constant) and type(argument.value) is str:
                            requested = argument.value
                            if requested in PROCESS_ATTRIBUTES:
                                finding("PROCESS", "INDIRECT_PROCESS_CAPABILITY:" + requested, node.lineno)
                            if requested in NETWORK_ATTRIBUTES or requested.split(".")[0] in NETWORK_IMPORT_ROOTS:
                                finding("NETWORK", "INDIRECT_NETWORK_CAPABILITY:" + requested, node.lineno)
                            if requested in DATA_LOADER_ATTRIBUTES:
                                finding("DATA_LOADER", "INDIRECT_DATA_LOADER:" + requested, node.lineno)
                            if requested in DYNAMIC_NAMES:
                                finding("DYNAMIC", "INDIRECT_DYNAMIC_CAPABILITY:" + requested, node.lineno)
                if isinstance(node.func, ast.Attribute) and (
                    node.func.attr.startswith("__")
                    and node.func.attr not in SAFE_DUNDER_ATTRIBUTES
                ):
                    for argument in node.args:
                        if isinstance(argument, ast.Constant) and type(argument.value) is str:
                            requested = argument.value
                            if requested in PROCESS_ATTRIBUTES:
                                finding("PROCESS", "DUNDER_PROCESS_CAPABILITY:" + requested, node.lineno)
                            if requested in NETWORK_ATTRIBUTES or requested.split(".")[0] in NETWORK_IMPORT_ROOTS:
                                finding("NETWORK", "DUNDER_NETWORK_CAPABILITY:" + requested, node.lineno)
                            if requested in DATA_LOADER_ATTRIBUTES:
                                finding("DATA_LOADER", "DUNDER_DATA_LOADER:" + requested, node.lineno)
                            if requested in DYNAMIC_NAMES:
                                finding("DYNAMIC", "DUNDER_DYNAMIC_CAPABILITY:" + requested, node.lineno)
        file_errors = sorted(
            {
                f"{item['category']}:{item['code']}:{item['line']}"
                for item in findings
            }
        )
        records.append({"path": relative, "errors": sorted(set(file_errors)), "pass": not file_errors})
        errors.extend(f"{relative}:{item}" for item in file_errors)
    constants_tree = ast.parse(
        stable_file_bytes(root / "prime_shell" / "constants.py").decode("utf-8")
    )
    frozen_checks = {
        "matrix_literal_exact": _assignment_literal(constants_tree, "CAT_MATRIX") == CAT_MATRIX,
        "prime_tuple_literal_exact": _assignment_literal(constants_tree, "LOCKED_PRIMES")
        == LOCKED_PRIMES,
        "repeat_tuple_literal_exact": _assignment_literal(constants_tree, "REPEATS") == REPEATS,
    }
    if not all(frozen_checks.values()):
        errors.append("FROZEN_LITERAL_ASSIGNMENTS_NOT_EXACT")
    return {
        "stage": "P2_CLOSED_WORLD_EXECUTABLE_SCAN",
        "records": records,
        "frozen_literal_checks": frozen_checks,
        "network_modules_imported": sum(
            item.startswith("NETWORK:") for record in records for item in record["errors"]
        ),
        "external_data_loaders": sum(
            item.startswith("DATA_LOADER:") for record in records for item in record["errors"]
        ),
        "process_capabilities": sum(
            item.startswith("PROCESS:") for record in records for item in record["errors"]
        ),
        "dynamic_capabilities": sum(
            item.startswith("DYNAMIC:") for record in records for item in record["errors"]
        ),
        "floating_literals": sum(
            item.startswith("FLOAT:")
            for record in records
            for item in record["errors"]
        ),
        "errors": errors,
        "pass": not errors,
    }
