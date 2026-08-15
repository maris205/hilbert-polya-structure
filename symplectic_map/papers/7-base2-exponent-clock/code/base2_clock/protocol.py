"""Immutable P0 bindings, strict JSON, and executable-isolation gates."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any

import sympy as sp


CANDIDATE_ID = "pcf_quadratic_exact_2adic_boundary_v1"
EXPECTED_LOCK_SHA256 = "205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1"
EXPECTED_PROOF_SHA256 = "9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9"
EXPECTED_PYPROJECT_SHA256 = "79c52764384b3f7111b702e9be08d90e5e53b089a55a9c2ff0938036e4acd59e"
EXPECTED_UPSTREAM_EXACT_POLYNOMIALS_SHA256 = (
    "dd5272f51243586523d13ba5e716503c648c46d43a0699153d686ae6fe8f1947"
)

UPSTREAM_BINDINGS = {
    "paper2_source_lock_sha256": (
        "../3-prime-multiplier-obstruction/experiments/source_lock.json",
        "aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842",
    ),
    "paper2_proof_package_sha256": (
        "../3-prime-multiplier-obstruction/notes/PROOF_PACKAGE.md",
        "6d01f26b5832bd88923d4f4ba0bb5ed7010a571f17f46a0e75b6247499034e17",
    ),
    "paper2_final_pdf_sha256": (
        "../3-prime-multiplier-obstruction/paper/paper_final.pdf",
        "160e9c6fa12c35f500fbae39d9316fc55e8c9b4f1b044ef3deda6037e0b5b1c3",
    ),
    "paper5_capacity_final_pdf_sha256": (
        "../6-arithmetic-clock-escape-trichotomy/paper/paper_final.pdf",
        "9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8",
    ),
}

EXPECTED_CODE_FILES = frozenset(
    {
        "README.md",
        "base2_clock/__init__.py",
        "base2_clock/algebra.py",
        "base2_clock/candidate.py",
        "base2_clock/cli.py",
        "base2_clock/controls.py",
        "base2_clock/dynatomic.py",
        "base2_clock/finite_field.py",
        "base2_clock/lifecycle.py",
        "base2_clock/manifest.py",
        "base2_clock/proof_contract.py",
        "base2_clock/protocol.py",
        "base2_clock/review_gate.py",
        "scripts/build_result_manifest.py",
        "scripts/run_registered_audit.py",
        "scripts/run_safe_preflight.py",
        "tests/test_algebra.py",
        "tests/test_controls.py",
        "tests/test_dynatomic.py",
        "tests/test_lifecycle.py",
        "tests/test_proof_contract.py",
        "tests/test_protocol.py",
        "tests/test_review_gate.py",
        "tests/test_round1_repairs.py",
    }
)
EXPECTED_CODE_DIRECTORIES = frozenset({"base2_clock", "scripts", "tests"})


class DuplicateJSONKeyError(ValueError):
    """Raised when a supposedly canonical JSON object repeats a key."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(text: str) -> Any:
    """Decode one JSON value and reject duplicate keys at every level."""

    def reject_nonfinite(value: str) -> None:
        raise ValueError(f"non-finite JSON constant is forbidden: {value}")

    return json.loads(
        text,
        object_pairs_hook=_unique_object,
        parse_constant=reject_nonfinite,
    )


def _raw_absolute(path: Path) -> Path:
    """Normalize ``.``/``..`` lexically without following any symlink."""

    return Path(os.path.abspath(os.fspath(path)))


def _metadata_identity(metadata: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
        metadata.st_nlink,
    )


def _directory_identity(metadata: os.stat_result) -> tuple[int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def _open_directory_chain(path: Path) -> int:
    """Open a lexical absolute directory one no-follow component at a time."""

    absolute = _raw_absolute(path)
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
    descriptor = os.open(absolute.anchor, flags)
    try:
        for component in absolute.parts[1:]:
            next_descriptor = os.open(component, flags, dir_fd=descriptor)
            metadata = os.fstat(next_descriptor)
            if not stat.S_ISDIR(metadata.st_mode):
                os.close(next_descriptor)
                raise NotADirectoryError(os.fspath(absolute))
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _open_parent_directory(path: Path) -> tuple[int, str]:
    absolute = _raw_absolute(path)
    if absolute == Path(absolute.anchor) or not absolute.name:
        raise ValueError("a filesystem root has no parent-relative leaf")
    return _open_directory_chain(absolute.parent), absolute.name


def _current_regular_identity(path: Path) -> tuple[int, int, int, int, int, int] | None:
    parent_descriptor: int | None = None
    descriptor: int | None = None
    try:
        parent_descriptor, name = _open_parent_directory(path)
        flags = os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC
        descriptor = os.open(name, flags, dir_fd=parent_descriptor)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
            return None
        return _metadata_identity(metadata)
    except (OSError, ValueError):
        return None
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if parent_descriptor is not None:
            os.close(parent_descriptor)


def regular_file(path: Path) -> bool:
    """Require a single-link regular file through a held no-follow dirfd chain."""

    return _current_regular_identity(path) is not None


def regular_directory(path: Path) -> bool:
    """Require an existing directory through a held no-follow dirfd chain."""

    descriptor: int | None = None
    try:
        descriptor = _open_directory_chain(path)
        return stat.S_ISDIR(os.fstat(descriptor).st_mode)
    except OSError:
        return False
    finally:
        if descriptor is not None:
            os.close(descriptor)


def safe_directory_entries(path: Path) -> list[dict[str, Any]]:
    """Return one flat no-follow inventory bound to a stable directory inode."""

    descriptor = _open_directory_chain(path)
    try:
        before = _directory_identity(os.fstat(descriptor))
        records: list[dict[str, Any]] = []
        with os.scandir(descriptor) as entries:
            for entry in entries:
                metadata = entry.stat(follow_symlinks=False)
                records.append(
                    {
                        "name": entry.name,
                        "mode": metadata.st_mode,
                        "nlink": metadata.st_nlink,
                    }
                )
        after = _directory_identity(os.fstat(descriptor))
    finally:
        os.close(descriptor)
    current = _open_directory_chain(path)
    try:
        current_identity = _directory_identity(os.fstat(current))
    finally:
        os.close(current)
    if before != after or after != current_identity:
        raise RuntimeError(f"directory changed during stable inventory: {path}")
    return sorted(records, key=lambda item: item["name"])


def stable_file_bytes(path: Path) -> bytes:
    """Read from a held parent dirfd and reject any identity/path-chain change."""

    parent_descriptor: int | None = None
    descriptor: int | None = None
    try:
        parent_descriptor, name = _open_parent_directory(path)
        flags = os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC
        descriptor = os.open(name, flags, dir_fd=parent_descriptor)
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise ValueError(f"not a regular file descriptor: {path}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        terminal = os.stat(name, dir_fd=parent_descriptor, follow_symlinks=False)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if parent_descriptor is not None:
            os.close(parent_descriptor)
    identity_before = _metadata_identity(before)
    identity_after = _metadata_identity(after)
    identity_terminal = _metadata_identity(terminal)
    if identity_before != identity_after or identity_after != identity_terminal:
        raise RuntimeError(f"file changed during stable read: {path}")
    if _current_regular_identity(path) != identity_after:
        raise RuntimeError(f"file path chain changed during stable read: {path}")
    return b"".join(chunks)


def sha256_file(path: Path) -> str:
    """Hash a stable raw-path read without resolving away symlink evidence."""

    return hashlib.sha256(stable_file_bytes(path)).hexdigest()


def load_strict_json(path: Path) -> Any:
    return strict_json_loads(stable_file_bytes(path).decode("utf-8"))


def load_exact_json(path: Path) -> Any:
    """Load JSON for exact official evidence and reject every finite float."""

    payload = load_strict_json(path)

    def contains_float(value: Any) -> bool:
        if type(value) is float:
            return True
        if type(value) is dict:
            return any(contains_float(key) or contains_float(item) for key, item in value.items())
        if type(value) is list:
            return any(contains_float(item) for item in value)
        return False

    if contains_float(payload):
        raise ValueError("floating JSON values are forbidden in exact official evidence")
    return payload


def load_strict_json_with_sha256(path: Path) -> tuple[Any, str]:
    """Parse and hash the same stable byte snapshot of one JSON file."""

    data = stable_file_bytes(path)
    return strict_json_loads(data.decode("utf-8")), hashlib.sha256(data).hexdigest()


def json_safe(value: Any) -> Any:
    """Normalize exact scalars without converting them to decimals."""

    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if type(value) is float:
        raise TypeError("floating values are forbidden in exact JSON")
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


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        json_safe(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def write_json(path: Path, value: Any, *, exclusive: bool = False) -> None:
    """Write deterministic JSON; official outputs may require exclusive creation."""

    data = (json.dumps(json_safe(value), indent=2, sort_keys=True) + "\n").encode("utf-8")
    parent_descriptor, name = _open_parent_directory(path)
    create_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC
    try:
        if exclusive:
            descriptor = os.open(name, create_flags, 0o600, dir_fd=parent_descriptor)
            try:
                offset = 0
                while offset < len(data):
                    offset += os.write(descriptor, data[offset:])
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
            os.fsync(parent_descriptor)
            return
        try:
            existing = os.stat(name, dir_fd=parent_descriptor, follow_symlinks=False)
        except FileNotFoundError:
            existing = None
        if existing is not None and (
            not stat.S_ISREG(existing.st_mode) or existing.st_nlink != 1
        ):
            raise ValueError(f"refusing to replace unsafe output: {path}")
        temporary_name = f".{name}.safe-tmp"
        try:
            descriptor = os.open(
                temporary_name,
                create_flags,
                0o600,
                dir_fd=parent_descriptor,
            )
        except FileExistsError as error:
            raise FileExistsError(
                f"stale safe-output temporary file: {path.parent / temporary_name}"
            ) from error
        try:
            try:
                offset = 0
                while offset < len(data):
                    offset += os.write(descriptor, data[offset:])
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
            os.replace(
                temporary_name,
                name,
                src_dir_fd=parent_descriptor,
                dst_dir_fd=parent_descriptor,
            )
            os.fsync(parent_descriptor)
        except BaseException:
            try:
                os.unlink(temporary_name, dir_fd=parent_descriptor)
            except FileNotFoundError:
                pass
            raise
    finally:
        os.close(parent_descriptor)


def validate_source_lock(project_root: Path) -> dict[str, Any]:
    """Validate the exact v2 lock and the frozen no-run provenance."""

    project_root = _raw_absolute(project_root)
    if not regular_directory(project_root):
        raise ValueError("project root is missing or has a symlink component")
    path = project_root / "experiments" / "source_lock.json"
    payload, digest = load_strict_json_with_sha256(path)
    state = payload.get("execution_state_at_lock", {})
    registered = payload.get("registered_exact_audit", {})
    bindings = payload.get("upstream_bindings", {})
    checks = {
        "source_lock_sha256": digest == EXPECTED_LOCK_SHA256,
        "candidate_id": payload.get("candidate_id") == CANDIDATE_ID,
        "lock_version_v2": payload.get("lock_version") == 2,
        "lock_status": payload.get("lock_status") == "SOURCE_LOCKED_V2_NO_REGISTERED_EXECUTION",
        "registered_runs_zero": state.get("registered_runs") == 0,
        "official_candidate_runs_zero": state.get("official_candidate_runs") == 0,
        "development_seen_disclosed": state.get("prelock_development_seen_periods") == list(range(1, 9)),
        "external_tables_unaccessed": state.get("external_prime_tables_accessed") is False,
        "zero_data_unaccessed": state.get("riemann_zero_data_accessed") is False,
        "parameter_search_absent": state.get("parameter_search_performed") is False,
        "approximate_search_absent": state.get("approximate_target_search_performed") is False,
        "registered_periods_frozen": registered.get("periods") == list(range(2, 8)),
        "no_blind_periods": registered.get("new_blind_periods") == [],
        "post_null_extension_forbidden": registered.get("post_null_extension_allowed") is False,
        "radical_exact_set_frozen": "rad(F_n)/gcd(rad(F_n)" in registered.get("exact_set_component", ""),
        "norm_is_independent_engine": "rational field norm" in registered.get("independent_engine", ""),
        "q3_only_optional": "optional diagnostic" in registered.get("independent_engine", ""),
        "upstream_binding_keys_exact": set(bindings) == set(UPSTREAM_BINDINGS),
        "upstream_binding_values_exact": all(
            bindings.get(key) == expected for key, (_, expected) in UPSTREAM_BINDINGS.items()
        ),
    }
    return {
        "stage": "P0_SOURCE_LOCK",
        "candidate_id": payload.get("candidate_id"),
        "source_lock_sha256": digest,
        "checks": checks,
        "pass": all(checks.values()),
    }


def validate_upstream_bindings(project_root: Path) -> dict[str, Any]:
    """Recompute every v2 source-lock upstream digest from local artifacts."""

    project_root = _raw_absolute(project_root)
    if not regular_directory(project_root):
        raise ValueError("project root is missing or has a symlink component")
    source_lock, _ = load_strict_json_with_sha256(
        project_root / "experiments" / "source_lock.json"
    )
    locked = source_lock["upstream_bindings"]
    records = []
    for binding_id, (relative, expected) in UPSTREAM_BINDINGS.items():
        # Construct from the nonsymlink papers root; never resolve the artifact.
        relative_parts = Path(relative).parts
        if relative_parts[:1] != ("..",):
            raise ValueError("upstream path must be a single papers-root relative binding")
        path = project_root.parent.joinpath(*relative_parts[1:])
        safe = regular_file(path)
        observed = (
            hashlib.sha256(stable_file_bytes(path)).hexdigest() if safe else None
        )
        records.append(
            {
                "binding_id": binding_id,
                "path": relative,
                "locked_sha256": locked.get(binding_id),
                "expected_sha256": expected,
                "observed_sha256": observed,
                "regular_nonsymlink_file": safe,
                "pass": safe and locked.get(binding_id) == expected == observed,
            }
        )
    return {
        "stage": "P0_UPSTREAM_BINDINGS",
        "records": records,
        "pass": all(record["pass"] for record in records),
    }


def code_tree_inventory(code_root: Path) -> dict[str, Any]:
    """Inventory the exact tree through held dirfds without following symlinks."""

    root = _raw_absolute(code_root)
    symlinks: list[str] = []
    unsupported: list[str] = []
    source_files: list[str] = []
    generated_files: list[str] = []
    root_descriptor: int | None = None
    try:
        root_descriptor = _open_directory_chain(root)
    except OSError:
        return {
            "source_files": [],
            "generated_files": [],
            "symlinks": ["<code-root-missing-or-symlink>"],
            "unsupported": [],
            "missing": sorted(EXPECTED_CODE_FILES),
            "extra": [],
            "pass": False,
        }
    root_identity = _directory_identity(os.fstat(root_descriptor))
    directory_flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
    stack: list[tuple[int, tuple[str, ...]]] = [(root_descriptor, ())]
    root_descriptor = None
    while stack:
        directory_descriptor, relative_parts = stack.pop()
        try:
            before = _directory_identity(os.fstat(directory_descriptor))
            with os.scandir(directory_descriptor) as entries:
                for entry in entries:
                    child_parts = (*relative_parts, entry.name)
                    relative = "/".join(child_parts)
                    metadata = entry.stat(follow_symlinks=False)
                    if stat.S_ISLNK(metadata.st_mode):
                        symlinks.append(relative)
                    elif stat.S_ISDIR(metadata.st_mode):
                        if relative not in EXPECTED_CODE_DIRECTORIES:
                            unsupported.append(f"directory:{relative}")
                            continue
                        try:
                            child_descriptor = os.open(
                                entry.name,
                                directory_flags,
                                dir_fd=directory_descriptor,
                            )
                        except OSError:
                            unsupported.append(f"changed-directory:{relative}")
                            continue
                        if _directory_identity(os.fstat(child_descriptor)) != _directory_identity(
                            metadata
                        ):
                            os.close(child_descriptor)
                            unsupported.append(f"changed-directory:{relative}")
                            continue
                        stack.append((child_descriptor, child_parts))
                    elif stat.S_ISREG(metadata.st_mode):
                        if "__pycache__" in child_parts or relative.endswith(".pyc"):
                            generated_files.append(relative)
                        else:
                            source_files.append(relative)
                    else:
                        unsupported.append(relative)
            after = _directory_identity(os.fstat(directory_descriptor))
            if before != after:
                unsupported.append(f"changed-directory:{'/'.join(relative_parts) or '.'}")
        finally:
            os.close(directory_descriptor)
    current_descriptor: int | None = None
    try:
        current_descriptor = _open_directory_chain(root)
        if _directory_identity(os.fstat(current_descriptor)) != root_identity:
            unsupported.append("changed-directory:<code-root>")
    except OSError:
        unsupported.append("changed-directory:<code-root>")
    finally:
        if current_descriptor is not None:
            os.close(current_descriptor)
    discovered = set(source_files)
    missing = sorted(EXPECTED_CODE_FILES.difference(discovered))
    extra = sorted(discovered.difference(EXPECTED_CODE_FILES))
    return {
        "source_files": sorted(source_files),
        "generated_files": sorted(generated_files),
        "symlinks": sorted(symlinks),
        "unsupported": sorted(unsupported),
        "missing": missing,
        "extra": extra,
        "pass": (
            not generated_files
            and not symlinks
            and not unsupported
            and not missing
            and not extra
        ),
    }


class _IsolationVisitor(ast.NodeVisitor):
    """Conservative alias/string/path-aware scanner for one Python module."""

    ALLOWED_IMPORT_ROOTS = {
        "__future__",
        "argparse",
        "ast",
        "base2_clock",
        "dataclasses",
        "fcntl",
        "fractions",
        "functools",
        "hashlib",
        "json",
        "os",
        "pathlib",
        "pytest",
        "stat",
        "sympy",
        "sys",
        "time",
        "typing",
        "xml",
    }
    FORBIDDEN_MODULE_ROOTS = {
        "aiohttp",
        "builtins",
        "ctypes",
        "ftplib",
        "http",
        "importlib",
        "mpmath",
        "numpy",
        "requests",
        "scipy",
        "socket",
        "subprocess",
        "urllib",
    }
    FORBIDDEN_PROVENANCE = {
        "builtins.__import__",
        "builtins.compile",
        "builtins.complex",
        "builtins.delattr",
        "builtins.eval",
        "builtins.exec",
        "builtins.float",
        "builtins.getattr",
        "builtins.globals",
        "builtins.locals",
        "builtins.open",
        "builtins.setattr",
        "builtins.vars",
        "os.popen",
        "os.system",
    }
    FORBIDDEN_SUFFIXES = (
        ".evalf",
        ".lambdify",
        ".nroots",
        ".nsimplify",
    )
    SUSPICIOUS_FRAGMENTS = (
        "riemann" + "_zero",
        "zeta" + "_zero",
        "prime" + "_table",
        "prime" + "_list",
        "near" + "_rational",
        "target" + "_zero",
    )
    FORBIDDEN_DYNAMIC_ATTRIBUTES = {
        "__builtins__",
        "__class__",
        "__closure__",
        "__code__",
        "__dict__",
        "__getattribute__",
        "__globals__",
        "__import__",
        "__mro__",
        "__subclasses__",
    }
    PATH_MUTATING_OR_READING_METHODS = {
        "chmod",
        "hardlink_to",
        "exists",
        "glob",
        "group",
        "is_dir",
        "is_file",
        "iterdir",
        "lchmod",
        "link_to",
        "lstat",
        "mkdir",
        "open",
        "owner",
        "read_bytes",
        "readlink",
        "read_text",
        "rename",
        "replace",
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
    PATH_METHOD_ALLOWLIST = {
        "base2_clock/lifecycle.py": {"mkdir"},
        "base2_clock/manifest.py": {"is_dir", "is_file"},
        "base2_clock/protocol.py": {
            "exists",
            "is_dir",
            "is_file",
            "mkdir",
            "stat",
        },
        "tests/test_lifecycle.py": {"is_file"},
        "tests/test_protocol.py": {"mkdir", "symlink_to", "write_text"},
        "tests/test_round1_repairs.py": {
            "mkdir",
            "symlink_to",
            "write_bytes",
            "write_text",
        },
    }
    OS_CALL_ALLOWLIST = {
        "base2_clock/lifecycle.py": {"os.path.lexists"},
        "base2_clock/manifest.py": {"os.path.lexists", "os.scandir"},
        "base2_clock/protocol.py": {
            "os.close",
            "os.fspath",
            "os.fstat",
            "os.fsync",
            "os.lstat",
            "os.open",
            "os.path.abspath",
            "os.read",
            "os.replace",
            "os.scandir",
            "os.stat",
            "os.unlink",
            "os.write",
        },
    }

    def __init__(self, relative: str):
        self.relative = relative
        self.aliases: dict[str, str] = {
            "Path": "pathlib.Path",
            "__import__": "builtins.__import__",
            "compile": "builtins.compile",
            "complex": "builtins.complex",
            "delattr": "builtins.delattr",
            "eval": "builtins.eval",
            "exec": "builtins.exec",
            "float": "builtins.float",
            "getattr": "builtins.getattr",
            "globals": "builtins.globals",
            "locals": "builtins.locals",
            "open": "builtins.open",
            "setattr": "builtins.setattr",
            "vars": "builtins.vars",
        }
        self.strings: dict[str, str] = {}
        self.paths: dict[str, str] = {}
        self.findings: list[dict[str, Any]] = []

    def finding(self, node: ast.AST, kind: str, value: str = "") -> None:
        item: dict[str, Any] = {
            "file": self.relative,
            "line": node.lineno,
            "kind": kind,
        }
        if value:
            item["value"] = value
        self.findings.append(item)

    def provenance(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return self.aliases.get(node.id, node.id)
        if isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name) and node.value.id in self.paths:
                return f"pathlib.Path.{node.attr}"
            if (
                isinstance(node.value, ast.Call)
                and self.provenance(node.value.func) == "pathlib.Path"
            ):
                return f"pathlib.Path.{node.attr}"
            owner = self.provenance(node.value)
            return f"{owner}.{node.attr}" if owner else None
        if isinstance(node, ast.Subscript):
            index = node.slice.value if isinstance(node.slice, ast.Constant) else None
            if isinstance(index, int) and isinstance(node.value, (ast.Tuple, ast.List)):
                if -len(node.value.elts) <= index < len(node.value.elts):
                    return self.provenance(node.value.elts[index])
            if isinstance(node.value, ast.Dict):
                key = self.static_string(node.slice)
                for candidate_key, candidate_value in zip(
                    node.value.keys, node.value.values, strict=True
                ):
                    if candidate_key is not None and self.static_string(candidate_key) == key:
                        return self.provenance(candidate_value)
        return None

    def static_string(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return self.strings.get(node.id)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left = self.static_string(node.left)
            right = self.static_string(node.right)
            if left is not None and right is not None:
                return left + right
        return None

    def static_path(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return self.paths.get(node.id)
        if isinstance(node, ast.Call) and self.provenance(node.func) == "pathlib.Path" and node.args:
            return self.static_string(node.args[0])
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            left = self.static_path(node.left)
            right = self.static_string(node.right)
            if left is not None and right is not None:
                return left.rstrip("/") + "/" + right
        return None

    def bind_name(self, name: str, value: ast.AST) -> None:
        provenance = self.provenance(value)
        if provenance:
            self.aliases[name] = provenance
        string = self.static_string(value)
        if string is not None:
            self.strings[name] = string
        path = self.static_path(value)
        if path is not None:
            self.paths[name] = path

    def bind_target(self, target: ast.AST, value: ast.AST) -> None:
        if isinstance(target, ast.Name):
            self.bind_name(target.id, value)
        elif isinstance(target, (ast.Tuple, ast.List)) and isinstance(
            value, (ast.Tuple, ast.List)
        ):
            if len(target.elts) == len(value.elts):
                for child_target, child_value in zip(
                    target.elts, value.elts, strict=True
                ):
                    self.bind_target(child_target, child_value)

    def dangerous_value_provenance(self, node: ast.AST) -> str | None:
        """Recursively classify a capability produced as a Python value."""

        provenance = self.provenance(node)
        if provenance is not None:
            method = provenance.rsplit(".", 1)[-1]
            if provenance in self.FORBIDDEN_PROVENANCE:
                return provenance
            if provenance.endswith(self.FORBIDDEN_SUFFIXES):
                return provenance
            if method in self.PATH_MUTATING_OR_READING_METHODS:
                return provenance
            if provenance.startswith(("os.exec", "os.spawn", "os.fork")):
                return provenance
        branches: list[ast.AST] = []
        if isinstance(node, ast.IfExp):
            branches = [node.body, node.orelse]
        elif isinstance(node, ast.Lambda):
            branches = [node.body, *node.args.defaults]
            branches.extend(
                item for item in node.args.kw_defaults if item is not None
            )
        elif isinstance(node, ast.BoolOp):
            branches = list(node.values)
        elif isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            branches = list(node.elts)
        elif isinstance(node, ast.Dict):
            branches = [
                item for item in [*node.keys, *node.values] if item is not None
            ]
        elif isinstance(node, ast.Starred):
            branches = [node.value]
        elif isinstance(node, ast.NamedExpr):
            branches = [node.value]
        for branch in branches:
            dangerous = self.dangerous_value_provenance(branch)
            if dangerous is not None:
                return dangerous
        return None

    def inspect_stored_values(self, nodes: list[ast.AST]) -> None:
        for node in nodes:
            provenance = self.dangerous_value_provenance(node)
            if provenance is not None:
                self.finding(node, "forbidden_callable_storage", provenance)

    def visit_Module(self, node: ast.Module) -> None:
        """Seed import and assignment aliases to a fixed point before checks."""

        nodes = list(ast.walk(node))
        for item in nodes:
            if isinstance(item, ast.Import):
                for alias in item.names:
                    self.aliases[alias.asname or alias.name.split(".")[0]] = alias.name
            elif isinstance(item, ast.ImportFrom):
                module = item.module or ""
                for alias in item.names:
                    self.aliases[alias.asname or alias.name] = (
                        f"{module}.{alias.name}" if module else alias.name
                    )
        assignments = [
            item
            for item in nodes
            if isinstance(item, (ast.Assign, ast.AnnAssign))
        ]
        for _ in range(len(assignments) + 1):
            before = (dict(self.aliases), dict(self.strings), dict(self.paths))
            for item in assignments:
                value = item.value
                if value is None:
                    continue
                targets = item.targets if isinstance(item, ast.Assign) else [item.target]
                for target in targets:
                    self.bind_target(target, value)
            after = (self.aliases, self.strings, self.paths)
            if before == after:
                break
        for statement in node.body:
            self.visit(statement)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            root = alias.name.split(".")[0]
            local = alias.asname or root
            self.aliases[local] = alias.name
            if root in self.FORBIDDEN_MODULE_ROOTS or root not in self.ALLOWED_IMPORT_ROOTS:
                self.finding(node, "forbidden_import", alias.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module = node.module or ""
        root = module.split(".")[0] if module else ""
        if node.level == 0 and (
            root in self.FORBIDDEN_MODULE_ROOTS or root not in self.ALLOWED_IMPORT_ROOTS
        ):
            self.finding(node, "forbidden_import", module)
        for alias in node.names:
            local = alias.asname or alias.name
            full = f"{module}.{alias.name}" if module else alias.name
            self.aliases[local] = full
            if full in self.FORBIDDEN_PROVENANCE:
                self.finding(node, "forbidden_imported_callable", full)

    def visit_Assign(self, node: ast.Assign) -> None:
        self.inspect_stored_values([node.value])
        for target in node.targets:
            self.bind_target(target, node.value)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None:
            self.inspect_stored_values([node.value])
            self.bind_target(node.target, node.value)
        self.generic_visit(node)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.inspect_stored_values([node.value])
        self.bind_target(node.target, node.value)
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        if node.value is not None:
            self.inspect_stored_values([node.value])
        self.generic_visit(node)

    def visit_Yield(self, node: ast.Yield) -> None:
        if node.value is not None:
            self.inspect_stored_values([node.value])
        self.generic_visit(node)

    def visit_YieldFrom(self, node: ast.YieldFrom) -> None:
        self.inspect_stored_values([node.value])
        self.generic_visit(node)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        defaults = [*node.args.defaults]
        defaults.extend(item for item in node.args.kw_defaults if item is not None)
        self.inspect_stored_values([node.body, *defaults])
        self.generic_visit(node)

    def inspect_function_defaults(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        defaults = [*node.args.defaults]
        defaults.extend(item for item in node.args.kw_defaults if item is not None)
        self.inspect_stored_values(defaults)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.inspect_function_defaults(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.inspect_function_defaults(node)
        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant) -> None:
        if isinstance(node.value, float):
            self.finding(node, "floating_literal")

    def visit_Tuple(self, node: ast.Tuple) -> None:
        self.inspect_stored_values(list(node.elts))
        self.generic_visit(node)

    def visit_List(self, node: ast.List) -> None:
        self.inspect_stored_values(list(node.elts))
        self.generic_visit(node)

    def visit_Set(self, node: ast.Set) -> None:
        self.inspect_stored_values(list(node.elts))
        self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> None:
        self.inspect_stored_values(
            [item for item in [*node.keys, *node.values] if item is not None]
        )
        self.generic_visit(node)

    def visit_ListComp(self, node: ast.ListComp) -> None:
        self.inspect_stored_values([node.elt])
        self.generic_visit(node)

    def visit_SetComp(self, node: ast.SetComp) -> None:
        self.inspect_stored_values([node.elt])
        self.generic_visit(node)

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        self.inspect_stored_values([node.elt])
        self.generic_visit(node)

    def visit_DictComp(self, node: ast.DictComp) -> None:
        self.inspect_stored_values([node.key, node.value])
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if node.attr in self.FORBIDDEN_DYNAMIC_ATTRIBUTES:
            self.finding(node, "forbidden_dynamic_attribute", node.attr)
        if node.attr == "resolve":
            self.finding(node, "symlink_resolving_path_operation", node.attr)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        provenance = self.provenance(node.func)
        path_method = (
            node.func.attr
            if isinstance(node.func, ast.Attribute)
            else provenance.rsplit(".", 1)[-1]
            if provenance is not None
            else None
        )
        if isinstance(node.func, (ast.Call, ast.Subscript, ast.Lambda)):
            self.finding(node, "dynamic_callable_invocation")
        if provenance in self.FORBIDDEN_PROVENANCE or (
            provenance is not None and provenance.endswith(self.FORBIDDEN_SUFFIXES)
        ):
            self.finding(node, "forbidden_call", provenance or "")
        if provenance and provenance.startswith("os."):
            allowed = self.OS_CALL_ALLOWLIST.get(self.relative, set())
            if provenance not in allowed:
                self.finding(node, "forbidden_os_capability", provenance)
        if provenance and provenance.startswith("subprocess."):
            self.finding(node, "external_process", provenance)
        if provenance not in {"isinstance", "issubclass"}:
            for argument in [*node.args, *(item.value for item in node.keywords)]:
                argument_provenance = self.dangerous_value_provenance(argument)
                if argument_provenance is not None:
                    self.finding(
                        argument,
                        "forbidden_callable_argument",
                        argument_provenance,
                    )
        if (
            path_method in self.PATH_MUTATING_OR_READING_METHODS
            and not (provenance and provenance.startswith("os."))
            and not (provenance and provenance.startswith("ast."))
            and path_method not in self.PATH_METHOD_ALLOWLIST.get(self.relative, set())
        ):
            self.finding(
                node,
                "forbidden_path_capability",
                path_method or "",
            )
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in self.PATH_MUTATING_OR_READING_METHODS
            and not (provenance and provenance.startswith("os."))
        ):
            resource = self.static_path(node.func.value)
            if resource and any(
                fragment in resource.lower() for fragment in self.SUSPICIOUS_FRAGMENTS
            ):
                self.finding(node, "forbidden_resource", resource)
        if provenance == "builtins.open" and node.args:
            resource = self.static_string(node.args[0])
            if resource and any(
                fragment in resource.lower() for fragment in self.SUSPICIOUS_FRAGMENTS
            ):
                self.finding(node, "forbidden_resource", resource)
        if provenance == "os.open" and node.args:
            resource = self.static_string(node.args[0])
            if resource and any(
                fragment in resource.lower() for fragment in self.SUSPICIOUS_FRAGMENTS
            ):
                self.finding(node, "forbidden_resource", resource)
        self.generic_visit(node)


def executable_isolation_scan(code_root: Path) -> dict[str, Any]:
    """Reject network, process, dynamic-import, and approximate-matching paths."""

    inventory = code_tree_inventory(code_root)
    findings: list[dict[str, Any]] = []
    scanned: list[str] = []
    if not inventory["pass"]:
        findings.append(
            {
                "file": "<code-tree>",
                "line": 0,
                "kind": "closed_world_inventory_mismatch",
                "value": json.dumps(
                    {
                        "symlinks": inventory["symlinks"],
                        "generated_files": inventory["generated_files"],
                        "unsupported": inventory["unsupported"],
                        "missing": inventory["missing"],
                        "extra": inventory["extra"],
                    },
                    sort_keys=True,
                ),
            }
        )
    root = _raw_absolute(code_root)
    for relative in sorted(item for item in inventory["source_files"] if item.endswith(".py")):
        path = root / relative
        scanned.append(relative)
        if not regular_file(path):
            findings.append(
                {"file": relative, "line": 0, "kind": "unsafe_source_file"}
            )
            continue
        tree = ast.parse(stable_file_bytes(path).decode("utf-8"), filename=str(path))
        visitor = _IsolationVisitor(relative)
        visitor.visit(tree)
        findings.extend(visitor.findings)
    pyproject = _raw_absolute(code_root).parent / "pyproject.toml"
    configuration_files = []
    if regular_file(pyproject):
        configuration_files.append("pyproject.toml")
        if sha256_file(pyproject) != EXPECTED_PYPROJECT_SHA256:
            findings.append(
                {
                    "file": "../pyproject.toml",
                    "line": 0,
                    "kind": "configuration_hash_mismatch",
                }
            )
    else:
        findings.append(
            {
                "file": "../pyproject.toml",
                "line": 0,
                "kind": "configuration_missing_or_unsafe",
            }
        )
    return {
        "stage": "P0_EXECUTABLE_ISOLATION",
        "scanner": "CLOSED_WORLD_ALIAS_DATAFLOW_AST_V2",
        "inventory": inventory,
        "scanned_python_files": scanned,
        "configuration_files": configuration_files,
        "findings": findings,
        "forbidden_access_count": len(findings),
        "pass": not findings,
    }
