"""Immutable bindings, strict exact JSON, safe I/O, and executable isolation."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any


CANDIDATE_ID = "cat_torsion_primitive_divisor_capacity_v1"
EXPECTED_LOCK_SHA256 = "87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce"
EXPECTED_PROOF_SHA256 = "ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af"
EXPECTED_PLAN_SHA256 = "a45fd3c68667e4d93c80f863b724df5d95714a45bb9b8138c896ce3d52858081"
EXPECTED_SOURCE_REVIEW_SHA256 = "38ec6aaacf40da5bcf93f62916b53d6f07f18d2cfcf6d91865989875a997b951"
EXPECTED_PYPROJECT_SHA256 = "fa989cdf66b824c7edad7dcf169d16ee7b27a3fbb843d8617c4e197a21511bb3"
EXPECTED_EXECUTION_TREE_SHA256 = "b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059"

LOCAL_BINDINGS = {
    "readme_sha256": (
        "README.md",
        "3386d710b26900350fe963c2c040fdce569e6ebd3a961cef6c54531bafb5e880",
    ),
    "research_question_sha256": (
        "notes/RESEARCH_QUESTION.md",
        "8f10e2eb2485351e93a58948bfa15dab8584cd549d2998836fcecff5487ca4d5",
    ),
    "novelty_audit_sha256": (
        "notes/NOVELTY_AUDIT.md",
        "dcc30076f31099db5fb960284374819c39fdbf5f9a5c9348c19bf5ed92a22212",
    ),
    "proof_package_sha256": (
        "notes/PROOF_PACKAGE.md",
        EXPECTED_PROOF_SHA256,
    ),
    "experiment_plan_sha256": (
        "experiments/EXPERIMENT_PLAN.md",
        EXPECTED_PLAN_SHA256,
    ),
    "experiment_tracker_sha256": (
        "experiments/EXPERIMENT_TRACKER.md",
        "b977106d20039a5de31db31969ead23829d4dab058d9c7f4c03b1b96e54748f9",
    ),
}

UPSTREAM_BINDINGS = {
    "paper6_source_lock_sha256": (
        "../6-arithmetic-clock-escape-trichotomy/experiments/source_lock.json",
        "2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc",
    ),
    "paper6_proof_package_sha256": (
        "../6-arithmetic-clock-escape-trichotomy/notes/PROOF_PACKAGE.md",
        "62f9dd20e687f05ed085df5fcac233bc2bfbace2f9cdc526a544403409b2d855",
    ),
    "paper6_final_pdf_sha256": (
        "../6-arithmetic-clock-escape-trichotomy/paper/paper_final.pdf",
        "9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8",
    ),
    "paper7_source_lock_sha256": (
        "../7-base2-exponent-clock/experiments/source_lock.json",
        "205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1",
    ),
    "paper7_proof_package_sha256": (
        "../7-base2-exponent-clock/notes/PROOF_PACKAGE.md",
        "9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9",
    ),
    "paper7_final_pdf_sha256": (
        "../7-base2-exponent-clock/paper/paper_final.pdf",
        "fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf",
    ),
    "route_a_evaluator_sha256": (
        "../../skills/route-a-evaluator.md",
        "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
    ),
}

EXPECTED_CODE_FILES = frozenset(
    {
        "README.md",
        "cat_torsion/__init__.py",
        "cat_torsion/algebra.py",
        "cat_torsion/candidate.py",
        "cat_torsion/cli.py",
        "cat_torsion/clock.py",
        "cat_torsion/controls.py",
        "cat_torsion/finite_field.py",
        "cat_torsion/lifecycle.py",
        "cat_torsion/manifest.py",
        "cat_torsion/proof_contract.py",
        "cat_torsion/protocol.py",
        "cat_torsion/review_gate.py",
        "scripts/build_result_manifest.py",
        "scripts/run_registered_audit.py",
        "scripts/run_safe_preflight.py",
        "tests/test_algebra.py",
        "tests/test_clock_proof.py",
        "tests/test_controls.py",
        "tests/test_finite_field.py",
        "tests/test_manifest.py",
        "tests/test_protocol.py",
        "tests/test_review_lifecycle.py",
        "tests/test_security_regressions.py",
    }
)
EXPECTED_CODE_DIRECTORIES = frozenset({"cat_torsion", "scripts", "tests"})


class DuplicateJSONKeyError(ValueError):
    """Raised when an exact JSON object repeats a key."""


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
    if type(value) is dict:
        return any(_contains_float(key) or _contains_float(item) for key, item in value.items())
    if type(value) is list:
        return any(_contains_float(item) for item in value)
    return False


def _raw_absolute(path: Path) -> Path:
    """Normalize lexical components without resolving any symlink."""

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
        raise ValueError("filesystem root has no parent-relative leaf")
    return _open_directory_chain(absolute.parent), absolute.name


def _current_regular_identity(path: Path) -> tuple[int, int, int, int, int, int] | None:
    parent_descriptor: int | None = None
    descriptor: int | None = None
    try:
        parent_descriptor, name = _open_parent_directory(path)
        descriptor = os.open(
            name,
            os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC,
            dir_fd=parent_descriptor,
        )
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
    return _current_regular_identity(path) is not None


def regular_directory(path: Path) -> bool:
    descriptor: int | None = None
    try:
        descriptor = _open_directory_chain(path)
        return stat.S_ISDIR(os.fstat(descriptor).st_mode)
    except OSError:
        return False
    finally:
        if descriptor is not None:
            os.close(descriptor)


def stable_file_bytes(path: Path) -> bytes:
    parent_descriptor: int | None = None
    descriptor: int | None = None
    before: os.stat_result
    after: os.stat_result
    terminal: os.stat_result
    try:
        parent_descriptor, name = _open_parent_directory(path)
        descriptor = os.open(
            name,
            os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC,
            dir_fd=parent_descriptor,
        )
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise ValueError(f"not a single-link regular file: {path}")
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
    identities = (_metadata_identity(before), _metadata_identity(after), _metadata_identity(terminal))
    if len(set(identities)) != 1:
        raise RuntimeError(f"file changed during stable read: {path}")
    if _current_regular_identity(path) != identities[0]:
        raise RuntimeError(f"file path chain changed during stable read: {path}")
    return b"".join(chunks)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(stable_file_bytes(path)).hexdigest()


def load_strict_json(path: Path) -> Any:
    return strict_json_loads(stable_file_bytes(path).decode("utf-8"))


def load_exact_json(path: Path) -> Any:
    payload = load_strict_json(path)
    if _contains_float(payload):
        raise ValueError("floating JSON values are forbidden in exact evidence")
    return payload


def json_safe(value: Any) -> Any:
    if type(value) is dict:
        return {str(key): json_safe(item) for key, item in value.items()}
    if type(value) in {list, tuple}:
        return [json_safe(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if type(value) is float:
        raise TypeError("floating values are forbidden in exact JSON")
    return value


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        json_safe(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def write_json(path: Path, value: Any, *, exclusive: bool = False) -> None:
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
        temporary_name = f".{name}.cat-torsion-safe-tmp"
        descriptor = os.open(
            temporary_name, create_flags, 0o600, dir_fd=parent_descriptor
        )
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


def safe_directory_entries(path: Path) -> list[dict[str, Any]]:
    descriptor = _open_directory_chain(path)
    try:
        before = _directory_identity(os.fstat(descriptor))
        records: list[dict[str, Any]] = []
        with os.scandir(descriptor) as entries:
            for entry in entries:
                metadata = entry.stat(follow_symlinks=False)
                records.append(
                    {"name": entry.name, "mode": metadata.st_mode, "nlink": metadata.st_nlink}
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
    return sorted(records, key=lambda record: record["name"])


def validate_source_lock(project_root: Path) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    lock_path = project_root / "experiments" / "source_lock.json"
    payload = load_exact_json(lock_path)
    digest = sha256_file(lock_path)
    checks: dict[str, bool] = {
        "source_lock_sha256": digest == EXPECTED_LOCK_SHA256,
        "root_object": type(payload) is dict,
    }
    if type(payload) is not dict:
        return {"stage": "P0_SOURCE_LOCK", "checks": checks, "pass": False}
    execution = payload.get("execution_state_at_lock", {})
    permissions = payload.get("preexecution_permissions", {})
    small = payload.get("small_ledger_provenance", {})
    gate = payload.get("formal_run_gate", {})
    frozen = payload.get("frozen_object", {})
    local = payload.get("local_design_bindings", {})
    upstream = payload.get("upstream_bindings", {})
    checks.update(
        {
            "candidate_id": payload.get("candidate_id") == CANDIDATE_ID,
            "lock_version_one": type(payload.get("lock_version")) is int
            and payload.get("lock_version") == 1,
            "lock_status_exact": payload.get("lock_status")
            == "SOURCE_LOCKED_V1_NO_REGISTERED_EXECUTION_INDEPENDENT_DESIGN_INPUTS_INCORPORATED",
            "matrix_exact": frozen.get("matrix") == [[2, 1], [1, 1]],
            "trace_three": frozen.get("matrix_trace") == 3,
            "determinant_one": frozen.get("matrix_determinant") == 1,
            "allowed_periods_exact": small.get("allowed_periods") == list(range(1, 13)),
            "post_null_extension_forbidden": small.get("post_null_extension_allowed") is False,
            "registered_audits_zero": type(execution.get("registered_exact_audits")) is int
            and execution.get("registered_exact_audits") == 0,
            "candidate_numerical_runs_zero": type(execution.get("candidate_numerical_runs"))
            is int
            and execution.get("candidate_numerical_runs") == 0,
            "generated_arrays_zero": type(execution.get("generated_prime_target_arrays")) is int
            and execution.get("generated_prime_target_arrays") == 0,
            "zero_data_unaccessed": execution.get("riemann_zero_data_accessed") is False,
            "external_tables_unaccessed": execution.get("external_prime_target_tables_accessed")
            is False,
            "registered_execution_locked": permissions.get("registered_exact_audit") is False,
            "numerical_execution_locked": permissions.get("candidate_numerical_execution") is False,
            "external_data_locked": permissions.get("external_prime_or_zero_data_access") is False,
            "review_prefix_exact": gate.get("authority_prefix") == "CAT_TORSION_CODE_REVIEW_V1 ",
            "local_binding_keys_exact": set(local) == set(LOCAL_BINDINGS),
            "upstream_binding_keys_exact": set(upstream) == set(UPSTREAM_BINDINGS),
        }
    )
    local_records = []
    for binding_id, (relative, expected) in LOCAL_BINDINGS.items():
        path = project_root / relative
        safe = regular_file(path)
        observed = sha256_file(path) if safe else None
        record = {
            "binding_id": binding_id,
            "path": relative,
            "locked_sha256": local.get(binding_id),
            "expected_sha256": expected,
            "observed_sha256": observed,
            "regular_single_link_file": safe,
            "pass": safe and local.get(binding_id) == expected == observed,
        }
        local_records.append(record)
    checks["all_local_bindings_live"] = all(record["pass"] for record in local_records)
    return {
        "stage": "P0_SOURCE_LOCK",
        "candidate_id": payload.get("candidate_id"),
        "source_lock_sha256": digest,
        "checks": checks,
        "local_binding_records": local_records,
        "pass": all(checks.values()),
    }


def validate_upstream_bindings(project_root: Path) -> dict[str, Any]:
    project_root = _raw_absolute(project_root)
    payload = load_exact_json(project_root / "experiments" / "source_lock.json")
    locked = payload["upstream_bindings"]
    records = []
    for binding_id, (relative, expected) in UPSTREAM_BINDINGS.items():
        parts = Path(relative).parts
        if parts[:1] != ("..",):
            raise ValueError("upstream binding must leave the paper root exactly once")
        if parts[:2] == ("..", ".."):
            path = project_root.parents[1].joinpath(*parts[2:])
        else:
            path = project_root.parent.joinpath(*parts[1:])
        safe = regular_file(path)
        observed = sha256_file(path) if safe else None
        records.append(
            {
                "binding_id": binding_id,
                "path": relative,
                "locked_sha256": locked.get(binding_id),
                "expected_sha256": expected,
                "observed_sha256": observed,
                "regular_single_link_file": safe,
                "pass": safe and locked.get(binding_id) == expected == observed,
            }
        )
    return {
        "stage": "P0_UPSTREAM_BINDINGS",
        "records": records,
        "pass": len(records) == len(UPSTREAM_BINDINGS) and all(
            record["pass"] for record in records
        ),
    }


def code_tree_inventory(code_root: Path) -> dict[str, Any]:
    root = _raw_absolute(code_root)
    source_files: list[str] = []
    generated_files: list[str] = []
    symlinks: list[str] = []
    unsupported: list[str] = []
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
    while stack:
        descriptor, relative_parts = stack.pop()
        try:
            before = _directory_identity(os.fstat(descriptor))
            with os.scandir(descriptor) as entries:
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
                            child = os.open(
                                entry.name, directory_flags, dir_fd=descriptor
                            )
                        except OSError:
                            unsupported.append(f"changed-directory:{relative}")
                            continue
                        if _directory_identity(os.fstat(child)) != _directory_identity(metadata):
                            os.close(child)
                            unsupported.append(f"changed-directory:{relative}")
                        else:
                            stack.append((child, child_parts))
                    elif stat.S_ISREG(metadata.st_mode):
                        if metadata.st_nlink != 1:
                            unsupported.append(f"hardlink:{relative}")
                        elif "__pycache__" in child_parts or relative.endswith(".pyc"):
                            generated_files.append(relative)
                        else:
                            source_files.append(relative)
                    else:
                        unsupported.append(relative)
            after = _directory_identity(os.fstat(descriptor))
            if before != after:
                unsupported.append(f"changed-directory:{'/'.join(relative_parts) or '.'}")
        finally:
            os.close(descriptor)
    current: int | None = None
    try:
        current = _open_directory_chain(root)
        if _directory_identity(os.fstat(current)) != root_identity:
            unsupported.append("changed-directory:<code-root>")
    except OSError:
        unsupported.append("changed-directory:<code-root>")
    finally:
        if current is not None:
            os.close(current)
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
        "pass": not generated_files and not symlinks and not unsupported and not missing and not extra,
    }


class _IsolationVisitor(ast.NodeVisitor):
    ALLOWED_IMPORT_ROOTS = {
        "__future__",
        "argparse",
        "ast",
        "cat_torsion",
        "collections",
        "fractions",
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
        "sympy.nextprime",
        "sympy.prevprime",
        "sympy.primerange",
        "sympy.randprime",
        "sympy.sieve",
    }
    FORBIDDEN_SUFFIXES = (".evalf", ".lambdify", ".nroots", ".nsimplify")
    SUSPICIOUS_FRAGMENTS = (
        "riemann" + "_zero",
        "zeta" + "_zero",
        "prime" + "_table",
        "prime" + "_list",
        "target" + "_zero",
        "nearest" + "_prime",
    )
    DYNAMIC_ATTRIBUTES = {
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
    PATH_METHODS = {
        "chmod",
        "exists",
        "glob",
        "hardlink_to",
        "is_dir",
        "is_file",
        "iterdir",
        "lstat",
        "mkdir",
        "open",
        "read_bytes",
        "read_text",
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
    PATH_ALLOWLIST = {
        "cat_torsion/protocol.py": {"stat"},
        "tests/test_manifest.py": {
            "mkdir",
            "symlink_to",
            "unlink",
            "write_bytes",
            "write_text",
        },
        "tests/test_protocol.py": {"mkdir", "symlink_to", "write_bytes", "write_text"},
        "tests/test_review_lifecycle.py": {"mkdir", "write_bytes", "write_text"},
        "tests/test_security_regressions.py": {
            "hardlink_to",
            "mkdir",
            "symlink_to",
            "unlink",
            "write_bytes",
            "write_text",
        },
    }
    OS_ALLOWLIST = {
        "cat_torsion/protocol.py": {
            "os.close",
            "os.fspath",
            "os.fstat",
            "os.fsync",
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
        self.paths: dict[str, str] = {}
        self.strings: dict[str, str] = {}
        self.findings: list[dict[str, Any]] = []

    def finding(self, node: ast.AST, kind: str, value: str = "") -> None:
        item: dict[str, Any] = {"file": self.relative, "line": node.lineno, "kind": kind}
        if value:
            item["value"] = value
        self.findings.append(item)

    def provenance(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return self.aliases.get(node.id, node.id)
        if isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name) and node.value.id in self.paths:
                return f"pathlib.Path.{node.attr}"
            if isinstance(node.value, ast.Call) and self.provenance(node.value.func) == "pathlib.Path":
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

    def bind_target(self, target: ast.AST, value: ast.AST) -> None:
        if isinstance(target, ast.Name):
            provenance = self.provenance(value)
            if provenance:
                self.aliases[target.id] = provenance
            string = self.static_string(value)
            if string is not None:
                self.strings[target.id] = string
            path = self.static_path(value)
            if path is not None:
                self.paths[target.id] = path
        elif isinstance(target, (ast.Tuple, ast.List)) and isinstance(value, (ast.Tuple, ast.List)):
            if len(target.elts) == len(value.elts):
                for child_target, child_value in zip(target.elts, value.elts, strict=True):
                    self.bind_target(child_target, child_value)

    def dangerous_value(self, node: ast.AST) -> str | None:
        provenance = self.provenance(node)
        if provenance is not None:
            method = provenance.rsplit(".", 1)[-1]
            if provenance in self.FORBIDDEN_PROVENANCE:
                return provenance
            if provenance.endswith(self.FORBIDDEN_SUFFIXES):
                return provenance
            if method in self.PATH_METHODS:
                return provenance
            if provenance.startswith(("os.exec", "os.spawn", "os.fork")):
                return provenance
        branches: list[ast.AST] = []
        if isinstance(node, ast.IfExp):
            branches = [node.body, node.orelse]
        elif isinstance(node, ast.Lambda):
            branches = [node.body, *node.args.defaults]
            branches.extend(item for item in node.args.kw_defaults if item is not None)
        elif isinstance(node, ast.BoolOp):
            branches = list(node.values)
        elif isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            branches = list(node.elts)
        elif isinstance(node, ast.Dict):
            branches = [item for item in [*node.keys, *node.values] if item is not None]
        elif isinstance(node, ast.Starred):
            branches = [node.value]
        elif isinstance(node, ast.NamedExpr):
            branches = [node.value]
        for branch in branches:
            dangerous = self.dangerous_value(branch)
            if dangerous is not None:
                return dangerous
        return None

    def inspect_stored(self, nodes: list[ast.AST]) -> None:
        for node in nodes:
            dangerous = self.dangerous_value(node)
            if dangerous is not None:
                self.finding(node, "forbidden_callable_storage", dangerous)

    def visit_Module(self, node: ast.Module) -> None:
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
        assignments = [item for item in nodes if isinstance(item, (ast.Assign, ast.AnnAssign))]
        for _ in range(len(assignments) + 1):
            before = (dict(self.aliases), dict(self.strings), dict(self.paths))
            for item in assignments:
                value = item.value
                if value is None:
                    continue
                targets = item.targets if isinstance(item, ast.Assign) else [item.target]
                for target in targets:
                    self.bind_target(target, value)
            if before == (self.aliases, self.strings, self.paths):
                break
        for statement in node.body:
            self.visit(statement)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            root = alias.name.split(".")[0]
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
            full = f"{module}.{alias.name}" if module else alias.name
            if full in self.FORBIDDEN_PROVENANCE:
                self.finding(node, "forbidden_imported_callable", full)

    def visit_Assign(self, node: ast.Assign) -> None:
        self.inspect_stored([node.value])
        for target in node.targets:
            self.bind_target(target, node.value)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None:
            self.inspect_stored([node.value])
            self.bind_target(node.target, node.value)
        self.generic_visit(node)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.inspect_stored([node.value])
        self.bind_target(node.target, node.value)
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        if node.value is not None:
            self.inspect_stored([node.value])
        self.generic_visit(node)

    def visit_Yield(self, node: ast.Yield) -> None:
        if node.value is not None:
            self.inspect_stored([node.value])
        self.generic_visit(node)

    def visit_YieldFrom(self, node: ast.YieldFrom) -> None:
        self.inspect_stored([node.value])
        self.generic_visit(node)

    def _inspect_defaults(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        defaults = [*node.args.defaults]
        defaults.extend(item for item in node.args.kw_defaults if item is not None)
        self.inspect_stored(defaults)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._inspect_defaults(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._inspect_defaults(node)
        self.generic_visit(node)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        defaults = [*node.args.defaults]
        defaults.extend(item for item in node.args.kw_defaults if item is not None)
        self.inspect_stored([node.body, *defaults])
        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant) -> None:
        if isinstance(node.value, float) or isinstance(node.value, complex):
            self.finding(node, "floating_or_complex_literal")

    def visit_Tuple(self, node: ast.Tuple) -> None:
        self.inspect_stored(list(node.elts))
        self.generic_visit(node)

    def visit_List(self, node: ast.List) -> None:
        self.inspect_stored(list(node.elts))
        self.generic_visit(node)

    def visit_Set(self, node: ast.Set) -> None:
        self.inspect_stored(list(node.elts))
        self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> None:
        self.inspect_stored([item for item in [*node.keys, *node.values] if item is not None])
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if self.provenance(node.value) == "sys" and node.attr == "modules":
            self.finding(node, "forbidden_module_table_access", "sys.modules")
        if node.attr in self.DYNAMIC_ATTRIBUTES:
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
            if provenance not in self.OS_ALLOWLIST.get(self.relative, set()):
                self.finding(node, "forbidden_os_capability", provenance)
        if provenance not in {"isinstance", "issubclass"}:
            for argument in [*node.args, *(keyword.value for keyword in node.keywords)]:
                dangerous = self.dangerous_value(argument)
                if dangerous is not None:
                    self.finding(argument, "forbidden_callable_argument", dangerous)
        if (
            path_method in self.PATH_METHODS
            and not (provenance and provenance.startswith(("os.", "ast.")))
            and path_method not in self.PATH_ALLOWLIST.get(self.relative, set())
        ):
            self.finding(node, "forbidden_path_capability", path_method or "")
        if isinstance(node.func, ast.Attribute) and node.func.attr in self.PATH_METHODS:
            resource = self.static_path(node.func.value)
            if resource and any(
                fragment in resource.lower() for fragment in self.SUSPICIOUS_FRAGMENTS
            ):
                self.finding(node, "forbidden_resource", resource)
        self.generic_visit(node)


def executable_isolation_scan(code_root: Path) -> dict[str, Any]:
    inventory = code_tree_inventory(code_root)
    findings: list[dict[str, Any]] = []
    if not inventory["pass"]:
        findings.append(
            {
                "file": "<code-tree>",
                "line": 0,
                "kind": "closed_world_inventory_mismatch",
                "value": json.dumps(
                    {
                        "generated": inventory["generated_files"],
                        "symlinks": inventory["symlinks"],
                        "unsupported": inventory["unsupported"],
                        "missing": inventory["missing"],
                        "extra": inventory["extra"],
                    },
                    sort_keys=True,
                ),
            }
        )
    root = _raw_absolute(code_root)
    scanned: list[str] = []
    for relative in sorted(item for item in inventory["source_files"] if item.endswith(".py")):
        path = root / relative
        scanned.append(relative)
        if not regular_file(path):
            findings.append({"file": relative, "line": 0, "kind": "unsafe_source_file"})
            continue
        tree = ast.parse(stable_file_bytes(path).decode("utf-8"), filename=str(path))
        visitor = _IsolationVisitor(relative)
        visitor.visit(tree)
        findings.extend(visitor.findings)
    pyproject = root.parent / "pyproject.toml"
    pyproject_safe = regular_file(pyproject)
    pyproject_hash = sha256_file(pyproject) if pyproject_safe else None
    if not pyproject_safe or pyproject_hash != EXPECTED_PYPROJECT_SHA256:
        findings.append(
            {"file": "../pyproject.toml", "line": 0, "kind": "configuration_hash_mismatch"}
        )
    return {
        "stage": "P0_EXECUTABLE_ISOLATION",
        "scanner": "CLOSED_WORLD_ALIAS_VALUE_FLOW_AST_V1",
        "inventory": inventory,
        "scanned_python_files": scanned,
        "pyproject_sha256": pyproject_hash,
        "findings": findings,
        "forbidden_access_count": len(findings),
        "pass": not findings,
    }
