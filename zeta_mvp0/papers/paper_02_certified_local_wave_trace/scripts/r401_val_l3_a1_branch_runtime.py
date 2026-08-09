#!/usr/bin/env python3
"""Prospective A4.16 L3-A1 branch process and transaction primitives.

This is an import-only implementation module.  It deliberately has no CLI,
does not compile CAPD code, does not construct a freeze or machine record, and
does not authorize evaluator dispatch.  Tests exercise it only with synthetic
mock executables.  A later accepted protocol/freeze may bind these exact bytes
and call :func:`run_branch_cell_transaction` from the all-slab scheduler.

The module keeps three boundaries explicit:

* the evaluator has a closed status/return-code namespace;
* resource/provenance failures are scheduler classifications, never evaluator
  statuses; and
* a cell becomes committed only after an operational-sibling staging
  directory is atomically published and its separate manifest is written
  last as a write-once commit marker.
"""

from __future__ import annotations

import hashlib
import ctypes
import errno
import fcntl
import json
import os
import re
import secrets
import signal
import stat
import subprocess
import threading
import time
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence


SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-A1"
CLAIM_BOUNDARY = (
    "accepted-branch complete-period tube cell only; no arbitrary-candidate "
    "tube routing, global uniqueness, trace, Hilbert--Polya, zeta, or RH claim"
)

EVALUATOR_STATUS_CODES: dict[str, int] = {
    "BRANCH_CELL_CERTIFIED": 0,
    "BRANCH_TUBE_UNRESOLVED": 2,
    "BRANCH_FLOW_FAIL": 3,
    "BRANCH_TUBE_VIOLATION": 4,
    "INVALID_BRANCH_PROOF_CONTRACT": 5,
}
SCHEDULER_CLASSIFICATIONS = frozenset(
    {
        "COMMITTED_EVALUATOR_RESULT",
        "CELL_TIMEOUT",
        "CELL_SIGNAL",
        "CELL_OUTPUT_BUDGET_EXHAUSTED",
        "MALFORMED_EVALUATOR_OUTPUT",
        "PROVENANCE_INVALID",
    }
)
SLAB_PATTERN = re.compile(r"S(?:00[0-9]|0[1-4][0-9]|050)\Z")
HEX64_PATTERN = re.compile(r"[0-9a-f]{64}\Z")
HEX40_PATTERN = re.compile(r"[0-9a-f]{40}\Z")
DECIMAL_PATTERN = re.compile(
    r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?\Z"
)
STATUS_PATTERN = re.compile(r"status=([A-Z][A-Z0-9_]*)\Z")
STAGING_NAME_PATTERN = re.compile(
    r"\.(S(?:00[0-9]|0[1-4][0-9]|050))\.tmp-([0-9a-f]{16})-(0|[1-9][0-9]*)\Z"
)
INTERRUPTED_LOCK_NAME_PATTERN = re.compile(
    r"(S(?:00[0-9]|0[1-4][0-9]|050))\.attempt-(0|[1-9][0-9]*)"
    r"\.generation-([0-9a-f]{16})\.owner-([0-9a-f]{32})\.lock\Z"
)
# Operational fail-closed deadline for the prospective single-generation
# namespace mutex.  This is not a scientific cell timeout or status.  A later
# machine/run-config freeze must bind these implementation bytes before any
# production dispatch.
LOCK_GUARD_ACQUIRE_TIMEOUT_SECONDS = 30.0


class BranchRuntimeError(RuntimeError):
    """Base class for prospective branch runtime contract failures."""


class BranchContractError(BranchRuntimeError):
    """An immutable task, binding, or ABI contract is malformed."""


class BranchProvenanceError(BranchRuntimeError):
    """A source, binary, path, digest, or committed byte is invalid."""


class BranchAlreadyRunningError(BranchRuntimeError):
    """Another operational owner holds the exact cell lock."""


class BranchOutputRecordError(BranchRuntimeError):
    """Even the bounded failure record cannot fit its frozen cap."""


class _SchedulerTerminationSignal(BaseException):
    """Internal unwind used to clean evaluator groups before SIGTERM exit."""

    def __init__(self, signal_number: int) -> None:
        super().__init__(f"scheduler received signal {signal_number}")
        self.signal_number = signal_number


@dataclass(frozen=True)
class BranchBudgets:
    """Candidate A4.16 branch limits from the reviewed pre-freeze design."""

    timeout_seconds: float = 600.0
    term_grace_seconds: float = 2.0
    pipe_close_grace_seconds: float = 1.0
    stdout_bytes: int = 16 * 1024 * 1024
    stderr_bytes: int = 1 * 1024 * 1024
    record_bytes: int = 4 * 1024 * 1024
    total_cell_bytes: int = 32 * 1024 * 1024

    def validate(self) -> None:
        for name in (
            "timeout_seconds",
            "term_grace_seconds",
            "pipe_close_grace_seconds",
        ):
            value = getattr(self, name)
            if type(value) not in (int, float) or isinstance(value, bool) or value <= 0:
                raise BranchContractError(f"{name} must be a positive finite scalar")
            if value != value or value in (float("inf"), float("-inf")):
                raise BranchContractError(f"{name} must be finite")
        for name in (
            "stdout_bytes",
            "stderr_bytes",
            "record_bytes",
            "total_cell_bytes",
        ):
            value = getattr(self, name)
            if type(value) is not int or value <= 0:
                raise BranchContractError(f"{name} must be a positive exact integer")
        if self.record_bytes < 64 * 1024:
            raise BranchContractError(
                "record byte cap is below the closed-schema minimum"
            )
        if self.total_cell_bytes < (
            self.stdout_bytes + self.stderr_bytes + self.record_bytes
        ):
            raise BranchContractError(
                "total cell cap must dominate stdout + stderr + record caps"
            )

    def payload(self) -> dict[str, int | float]:
        self.validate()
        return {
            "pipe_close_grace_seconds": self.pipe_close_grace_seconds,
            "record_bytes": self.record_bytes,
            "stderr_bytes": self.stderr_bytes,
            "stdout_bytes": self.stdout_bytes,
            "term_grace_seconds": self.term_grace_seconds,
            "timeout_seconds": self.timeout_seconds,
            "total_cell_bytes": self.total_cell_bytes,
        }


@dataclass(frozen=True)
class BranchBindings:
    """Already-frozen identities consumed by one future branch transaction.

    This dataclass does not create or bless any of these identities.  It only
    gives the process/transaction layer a closed object to bind into records.
    """

    matrix_id: str
    freeze_sha256: str
    run_config_sha256: str
    evaluator_source_path: str
    evaluator_source_sha256: str
    evaluator_binary_sha256: str
    capd_commit: str
    capd_flags_sha256: str
    runtime_libraries_sha256: str

    def validate(self) -> None:
        for name in (
            "matrix_id",
            "freeze_sha256",
            "run_config_sha256",
            "evaluator_source_sha256",
            "evaluator_binary_sha256",
            "capd_flags_sha256",
            "runtime_libraries_sha256",
        ):
            value = getattr(self, name)
            if type(value) is not str or HEX64_PATTERN.fullmatch(value) is None:
                raise BranchContractError(f"{name} must be lowercase SHA-256")
        if type(self.capd_commit) is not str or HEX40_PATTERN.fullmatch(
            self.capd_commit
        ) is None:
            raise BranchContractError("capd_commit must be a lowercase 40-hex commit")
        _require_absolute_lexical_path(self.evaluator_source_path, "evaluator source")

    def payload(self) -> dict[str, str]:
        return {
            "capd_commit": self.capd_commit,
            "capd_flags_sha256": self.capd_flags_sha256,
            "evaluator_binary_sha256": self.evaluator_binary_sha256,
            "evaluator_source_path": self.evaluator_source_path,
            "evaluator_source_sha256": self.evaluator_source_sha256,
            "runtime_libraries_sha256": self.runtime_libraries_sha256,
        }


IntervalStrings = tuple[str, str]


@dataclass(frozen=True)
class BranchCellTask:
    precision_bits: int
    slab_id: str
    epsilon: IntervalStrings
    root_box: tuple[
        IntervalStrings, IntervalStrings, IntervalStrings, IntervalStrings
    ]
    evaluator_binary_path: str
    accepted_l1_primary_record_id: str
    accepted_l1_primary_record_sha256: str

    def validate(self) -> None:
        if type(self.precision_bits) is not int or self.precision_bits not in (128, 256):
            raise BranchContractError("precision_bits must be exact integer 128 or 256")
        if type(self.slab_id) is not str or SLAB_PATTERN.fullmatch(self.slab_id) is None:
            raise BranchContractError("slab_id must be S000 through S050")
        if type(self.epsilon) is not tuple or len(self.epsilon) != 2:
            raise BranchContractError("epsilon must be one endpoint pair")
        if type(self.root_box) is not tuple or len(self.root_box) != 4:
            raise BranchContractError("root_box must contain exactly four endpoint pairs")
        for label, pair in (("epsilon", self.epsilon), *(
            (f"root_box[{index}]", value)
            for index, value in enumerate(self.root_box)
        )):
            _validate_interval_strings(pair, label)
        _require_absolute_lexical_path(self.evaluator_binary_path, "evaluator binary")
        if (
            type(self.accepted_l1_primary_record_id) is not str
            or not self.accepted_l1_primary_record_id
            or len(self.accepted_l1_primary_record_id.encode("utf-8")) > 1024
            or "\x00" in self.accepted_l1_primary_record_id
        ):
            raise BranchContractError("accepted L1 primary record ID is malformed")
        if (
            type(self.accepted_l1_primary_record_sha256) is not str
            or HEX64_PATTERN.fullmatch(self.accepted_l1_primary_record_sha256) is None
        ):
            raise BranchContractError("accepted L1 primary record hash is malformed")
        argv = self.argv()
        if len(argv) != 12 or not all(type(value) is str for value in argv):
            raise BranchContractError("branch evaluator argv is not exactly 12 strings")

    @property
    def tolerance(self) -> str:
        return "1e-30" if self.precision_bits == 128 else "1e-60"

    def argv(self) -> list[str]:
        values = [
            self.evaluator_binary_path,
            str(self.precision_bits),
            self.epsilon[0],
            self.epsilon[1],
        ]
        for lower, upper in self.root_box:
            values.extend((lower, upper))
        return values

    def payload(self) -> dict[str, Any]:
        return {
            "accepted_l1_primary_record_id": self.accepted_l1_primary_record_id,
            "accepted_l1_primary_record_sha256": self.accepted_l1_primary_record_sha256,
            "epsilon": list(self.epsilon),
            "phase_grid": 64,
            "precision_bits": self.precision_bits,
            "root_box": [list(pair) for pair in self.root_box],
            "slab_id": self.slab_id,
            "taylor_order": 24,
            "tolerance": self.tolerance,
            "tube_radius_sq": "1/625",
        }


@dataclass(frozen=True)
class StreamedProcessOutcome:
    return_code: int | None
    timed_out: bool
    output_budget_exhausted: bool
    descendant_group_survived_parent: bool
    descendant_pipe_leak: bool
    term_sent: bool
    kill_sent: bool
    stdout_size: int
    stderr_size: int
    stdout_truncated: bool
    stderr_truncated: bool
    stream_error: bool
    process_group_residual: bool
    spawn_error: bool


@dataclass(frozen=True)
class BranchTransactionResult:
    record: dict[str, Any]
    manifest: dict[str, Any]
    resumed_without_dispatch: bool


@dataclass
class PinnedRegularFile:
    """One no-follow open inode with pre/post identity and content replay."""

    path: Path
    descriptor: int
    device: int
    inode: int
    mode: int
    size: int
    sha256: str

    @classmethod
    def open(
        cls,
        path: Path,
        expected_sha256: str,
        *,
        executable: bool,
        context: str,
    ) -> "PinnedRegularFile":
        _reject_symlink_components(path, context)
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        try:
            descriptor = os.open(path, flags)
        except OSError as error:
            raise BranchProvenanceError(f"cannot pin {context}: {path}") from error
        try:
            metadata = os.fstat(descriptor)
            lexical = os.stat(path, follow_symlinks=False)
            if (
                not stat.S_ISREG(metadata.st_mode)
                or not stat.S_ISREG(lexical.st_mode)
                or (metadata.st_dev, metadata.st_ino)
                != (lexical.st_dev, lexical.st_ino)
            ):
                raise BranchProvenanceError(f"{context} path/inode mismatch")
            if executable and metadata.st_mode & 0o111 == 0:
                raise BranchProvenanceError(f"{context} is not executable")
            digest = _sha256_descriptor(descriptor)
            if digest != expected_sha256:
                raise BranchProvenanceError(f"{context} hash mismatch")
            return cls(
                path=path,
                descriptor=descriptor,
                device=metadata.st_dev,
                inode=metadata.st_ino,
                mode=stat.S_IMODE(metadata.st_mode),
                size=metadata.st_size,
                sha256=digest,
            )
        except Exception:
            os.close(descriptor)
            raise

    def verify_after(self) -> dict[str, Any]:
        metadata = os.fstat(self.descriptor)
        descriptor_identity_matches = (
            stat.S_ISREG(metadata.st_mode)
            and metadata.st_dev == self.device
            and metadata.st_ino == self.inode
            and stat.S_IMODE(metadata.st_mode) == self.mode
            and metadata.st_size == self.size
        )
        descriptor_hash_matches = _sha256_descriptor(self.descriptor) == self.sha256
        try:
            lexical = os.stat(self.path, follow_symlinks=False)
            path_identity_matches = (
                stat.S_ISREG(lexical.st_mode)
                and lexical.st_dev == self.device
                and lexical.st_ino == self.inode
            )
        except FileNotFoundError:
            path_identity_matches = False
        return {
            "descriptor_hash_matches_after": descriptor_hash_matches,
            "descriptor_identity_matches_after": descriptor_identity_matches,
            "device": self.device,
            "inode": self.inode,
            "mode": self.mode,
            "path": str(self.path),
            "path_identity_matches_after": path_identity_matches,
            "sha256": self.sha256,
            "size": self.size,
        }

    def close(self) -> None:
        os.close(self.descriptor)


def _stat_fingerprint(metadata: os.stat_result) -> tuple[int, ...]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_nlink,
        metadata.st_uid,
        metadata.st_gid,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


@dataclass(frozen=True)
class RegularFileSnapshot:
    """One immutable read used for parsing, hashing, and size binding."""

    path: Path
    payload: bytes
    fingerprint: tuple[int, ...]

    def verify_unchanged(self, context: str) -> None:
        _reject_symlink_components(self.path, context)
        try:
            current = os.stat(self.path, follow_symlinks=False)
        except (FileNotFoundError, OSError) as error:
            raise BranchProvenanceError(
                f"{context} changed after its captured read"
            ) from error
        if (
            not stat.S_ISREG(current.st_mode)
            or current.st_nlink != 1
            or _stat_fingerprint(current) != self.fingerprint
        ):
            raise BranchProvenanceError(
                f"{context} changed after its captured read"
            )


def _snapshot_regular_file(
    path: Path,
    context: str,
    *,
    maximum_bytes: int | None = None,
) -> RegularFileSnapshot:
    """Read one no-follow inode once and reject mutation during the read."""

    _reject_symlink_components(path, context)
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise BranchProvenanceError(f"cannot snapshot {context}: {path}") from error
    try:
        before = os.fstat(descriptor)
        lexical_before = os.stat(path, follow_symlinks=False)
        before_fingerprint = _stat_fingerprint(before)
        if before.st_nlink != 1 or lexical_before.st_nlink != 1:
            raise BranchProvenanceError(f"hard-link alias in {context}")
        if (
            not stat.S_ISREG(before.st_mode)
            or _stat_fingerprint(lexical_before) != before_fingerprint
        ):
            raise BranchProvenanceError(
                f"{context} is not one unaliased regular inode"
            )
        if maximum_bytes is not None and before.st_size > maximum_bytes:
            raise BranchProvenanceError(f"{context} exceeds its read cap")

        chunks: list[bytes] = []
        offset = 0
        while True:
            chunk = os.pread(descriptor, 1024 * 1024, offset)
            if not chunk:
                break
            chunks.append(chunk)
            offset += len(chunk)
            if maximum_bytes is not None and offset > maximum_bytes:
                raise BranchProvenanceError(f"{context} exceeds its read cap")
        payload = b"".join(chunks)
        after = os.fstat(descriptor)
        lexical_after = os.stat(path, follow_symlinks=False)
        if (
            len(payload) != before.st_size
            or _stat_fingerprint(after) != before_fingerprint
            or _stat_fingerprint(lexical_after) != before_fingerprint
        ):
            raise BranchProvenanceError(f"{context} changed during its captured read")
        return RegularFileSnapshot(path, payload, before_fingerprint)
    except OSError as error:
        raise BranchProvenanceError(f"cannot complete {context} snapshot") from error
    finally:
        os.close(descriptor)


def _validate_interval_strings(value: object, context: str) -> None:
    if type(value) is not tuple or len(value) != 2:
        raise BranchContractError(f"{context} must be an exact tuple pair")
    lower, upper = value
    if not all(
        type(token) is str
        and len(token) <= 512
        and DECIMAL_PATTERN.fullmatch(token)
        for token in value
    ):
        raise BranchContractError(f"{context} has a noncanonical decimal token")
    # Decimal lexical order is not numeric order.  Use Decimal only locally
    # after the closed grammar rejects nonfinite forms.
    from decimal import Decimal

    if Decimal(lower) > Decimal(upper):
        raise BranchContractError(f"{context} has reversed endpoints")


def _require_absolute_lexical_path(value: object, context: str) -> Path:
    if (
        type(value) is not str
        or not value
        or len(value.encode("utf-8")) > 4096
        or "\x00" in value
        or "\\" in value
        or any(ord(character) < 0x20 or ord(character) == 0x7F for character in value)
    ):
        raise BranchContractError(f"{context} path is malformed")
    path = Path(value)
    if (
        not path.is_absolute()
        or value.startswith("//")
        or path.as_posix() != value
        or any(part in ("", ".", "..") for part in path.parts)
    ):
        raise BranchContractError(f"{context} path must be canonical and absolute")
    return path


def _strict_relative(value: str) -> PurePosixPath:
    if type(value) is not str or not value or "\x00" in value or "\\" in value:
        raise BranchProvenanceError("unsafe relative path")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or path.as_posix() != value
        or any(part in ("", ".", "..") or part.startswith(".") for part in path.parts)
    ):
        raise BranchProvenanceError("noncanonical relative path")
    return path


def canonical_json_bytes(payload: Any) -> bytes:
    return (
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_descriptor(descriptor: int) -> str:
    digest = hashlib.sha256()
    offset = 0
    while True:
        chunk = os.pread(descriptor, 1024 * 1024, offset)
        if not chunk:
            break
        digest.update(chunk)
        offset += len(chunk)
    return digest.hexdigest()


def sha256_file(path: Path) -> str:
    _require_regular_file(path, "hash input")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _reject_symlink_components(path: Path, context: str) -> None:
    candidate = Path(path.anchor)
    seen_directory_inodes: set[tuple[int, int]] = set()
    if candidate.exists():
        root_metadata = os.lstat(candidate)
        seen_directory_inodes.add((root_metadata.st_dev, root_metadata.st_ino))
    for part in path.parts[1:]:
        candidate = candidate / part
        try:
            metadata = os.lstat(candidate)
        except FileNotFoundError:
            break
        if stat.S_ISLNK(metadata.st_mode):
            raise BranchProvenanceError(f"symlink component in {context}: {candidate}")
        if stat.S_ISDIR(metadata.st_mode):
            identity = (metadata.st_dev, metadata.st_ino)
            if identity in seen_directory_inodes:
                raise BranchProvenanceError(
                    f"ancestor inode alias in {context}: {candidate}"
                )
            seen_directory_inodes.add(identity)
        elif candidate != path:
            raise BranchProvenanceError(
                f"nondirectory ancestor in {context}: {candidate}"
            )


def _require_regular_file(path: Path, context: str) -> os.stat_result:
    _reject_symlink_components(path, context)
    if path.is_symlink() or not path.is_file():
        raise BranchProvenanceError(f"{context} is not a regular file: {path}")
    metadata = path.stat()
    if not stat.S_ISREG(metadata.st_mode):
        raise BranchProvenanceError(f"{context} is not regular: {path}")
    return metadata


def _exact_fields(raw: str, key: str) -> list[str]:
    prefix = f"{key}="
    return [line[len(prefix) :] for line in raw.splitlines() if line.startswith(prefix)]


def parse_evaluator_abi(
    stdout: bytes,
    stderr: bytes,
    return_code: int,
    task: BranchCellTask,
) -> str:
    """Parse only the closed process ABI; scientific replay belongs elsewhere."""

    try:
        text = stdout.decode("utf-8", errors="strict")
        stderr_text = stderr.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise BranchContractError("NON_UTF8_TRANSCRIPT") from error

    required_singletons = {
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "BRANCH_CELL_EVALUATOR_TRANSCRIPT",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": "false",
        "dispatch_authorized_by_evaluator": "false",
        "component_status": "null",
        "milestone_status": "null",
        "theorem_status": "null",
        "final_status": "null",
        "input_argv_count": "12",
        "precision_bits": str(task.precision_bits),
        "taylor_order": "24",
        "tolerance": task.tolerance,
        "phase_grid": "64",
    }
    for key, expected in required_singletons.items():
        values = _exact_fields(text, key)
        if values != [expected]:
            raise BranchContractError(f"ABI_FIELD_MISMATCH:{key}")
    for index, expected in enumerate(task.argv()):
        key = f"input_arg_{index:02d}"
        if _exact_fields(text, key) != [expected]:
            raise BranchContractError(f"INPUT_ECHO_MISMATCH:{key}")

    status_lines = [
        line for line in text.splitlines() if line.startswith("status=")
    ]
    if len(status_lines) != 1:
        raise BranchContractError("STATUS_CARDINALITY")
    status_match = STATUS_PATTERN.fullmatch(status_lines[0])
    if status_match is None:
        raise BranchContractError("UNKNOWN_EVALUATOR_STATUS")
    status_value = status_match.group(1)
    if status_value not in EVALUATOR_STATUS_CODES:
        raise BranchContractError("UNKNOWN_EVALUATOR_STATUS")
    if return_code != EVALUATOR_STATUS_CODES[status_value]:
        raise BranchContractError("STATUS_RETURN_CODE_MISMATCH")
    if status_value == "BRANCH_CELL_CERTIFIED" and stderr_text:
        raise BranchContractError("NONEMPTY_STDERR_ON_CERTIFIED_RESULT")
    return status_value


def _write_exclusive_fsync(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _rename_noreplace(source: Path, destination: Path) -> None:
    """Linux atomic rename with RENAME_NOREPLACE; never fall back to overwrite."""

    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = getattr(libc, "renameat2", None)
    if renameat2 is None:
        raise BranchProvenanceError("renameat2(RENAME_NOREPLACE) is unavailable")
    renameat2.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    result = renameat2(
        -100,
        os.fsencode(source),
        -100,
        os.fsencode(destination),
        1,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in (errno.EEXIST, errno.ENOTEMPTY):
        raise FileExistsError(error_number, os.strerror(error_number), destination)
    raise BranchProvenanceError(
        f"atomic no-replace rename failed with errno {error_number}"
    )


def _enable_child_subreaper() -> None:
    """Require Linux subreaper semantics so killed evaluator descendants are reaped."""

    libc = ctypes.CDLL(None, use_errno=True)
    prctl = getattr(libc, "prctl", None)
    if prctl is None:
        raise BranchProvenanceError("prctl(PR_SET_CHILD_SUBREAPER) is unavailable")
    prctl.argtypes = [
        ctypes.c_int,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_ulong,
    ]
    prctl.restype = ctypes.c_int
    if prctl(36, 1, 0, 0, 0) != 0:
        error_number = ctypes.get_errno()
        raise BranchProvenanceError(
            f"cannot enable child subreaper, errno {error_number}"
        )


def _reap_process_group_children(process_group: int) -> None:
    while True:
        try:
            child, _status = os.waitpid(-process_group, os.WNOHANG)
        except ChildProcessError:
            return
        if child == 0:
            return


def _process_group_exists(process_group: int) -> bool:
    try:
        os.killpg(process_group, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


@dataclass
class _SpawnedProcess:
    pid: int
    stdout: Any
    stderr: Any
    args: list[str]
    returncode: int | None = None

    def poll(self) -> int | None:
        if self.returncode is not None:
            return self.returncode
        try:
            waited_pid, status_value = os.waitpid(self.pid, os.WNOHANG)
        except ChildProcessError:
            return self.returncode
        if waited_pid == 0:
            return None
        self.returncode = os.waitstatus_to_exitcode(status_value)
        return self.returncode

    def wait(self, timeout: float | None = None) -> int:
        if self.returncode is not None:
            return self.returncode
        if timeout is None:
            try:
                _waited_pid, status_value = os.waitpid(self.pid, 0)
            except ChildProcessError:
                if self.returncode is None:
                    raise
            else:
                self.returncode = os.waitstatus_to_exitcode(status_value)
            assert self.returncode is not None
            return self.returncode
        deadline = time.monotonic() + timeout
        while True:
            result = self.poll()
            if result is not None:
                return result
            if time.monotonic() >= deadline:
                raise subprocess.TimeoutExpired(self.args, timeout)
            time.sleep(min(0.005, max(0.0, deadline - time.monotonic())))


def _spawn_pinned_process(
    argv: Sequence[str],
    executable_descriptor: int,
    child_signal_mask: set[signal.Signals],
) -> _SpawnedProcess:
    """Atomically acquire a child PID using posix_spawn and pinned-fd exec."""

    stdout_read = stdout_write = stderr_read = stderr_write = -1
    devnull_descriptor = execution_descriptor = -1
    child_pid: int | None = None
    stdout_stream: Any | None = None
    stderr_stream: Any | None = None
    try:
        stdout_read, stdout_write = os.pipe2(getattr(os, "O_CLOEXEC", 0))
        stderr_read, stderr_write = os.pipe2(getattr(os, "O_CLOEXEC", 0))
        devnull_descriptor = os.open(
            os.devnull, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0)
        )
        execution_descriptor = os.dup(executable_descriptor)
        os.set_inheritable(execution_descriptor, True)
        executable_path = f"/proc/self/fd/{execution_descriptor}"
        file_actions = (
            (os.POSIX_SPAWN_DUP2, devnull_descriptor, 0),
            (os.POSIX_SPAWN_DUP2, stdout_write, 1),
            (os.POSIX_SPAWN_DUP2, stderr_write, 2),
            (os.POSIX_SPAWN_CLOSE, stdout_read),
            (os.POSIX_SPAWN_CLOSE, stderr_read),
            (os.POSIX_SPAWN_CLOSE, stdout_write),
            (os.POSIX_SPAWN_CLOSE, stderr_write),
            (os.POSIX_SPAWN_CLOSE, devnull_descriptor),
        )
        child_pid = os.posix_spawn(
            executable_path,
            list(argv),
            dict(os.environ),
            file_actions=file_actions,
            # A fresh process group (PGID == child PID) is sufficient for the
            # complete descendant TERM/KILL contract.  ``setsid`` is not
            # available in posix_spawn on every supported libc, whereas
            # POSIX_SPAWN_SETPGROUP is.
            setpgroup=0,
            setsigmask=child_signal_mask,
            setsigdef={signal.SIGPIPE},
        )
        os.close(stdout_write)
        stdout_write = -1
        os.close(stderr_write)
        stderr_write = -1
        os.close(devnull_descriptor)
        devnull_descriptor = -1
        os.close(execution_descriptor)
        execution_descriptor = -1
        stdout_stream = os.fdopen(stdout_read, "rb", buffering=0)
        stdout_read = -1
        stderr_stream = os.fdopen(stderr_read, "rb", buffering=0)
        stderr_read = -1
        return _SpawnedProcess(
            child_pid,
            stdout_stream,
            stderr_stream,
            list(argv),
        )
    except BaseException:
        for stream in (stdout_stream, stderr_stream):
            if stream is not None:
                try:
                    stream.close()
                except OSError:
                    pass
        if child_pid is not None:
            try:
                os.killpg(child_pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                pass
            try:
                os.waitpid(child_pid, 0)
            except ChildProcessError:
                pass
            # The scheduler is a child subreaper.  If a post-spawn setup
            # failure occurs after the evaluator forked descendants, killing
            # and waiting only for the group leader leaves adopted zombies.
            # Reap every child in the failed process group before reporting a
            # spawn error.
            reap_deadline = time.monotonic() + 1.0
            while time.monotonic() < reap_deadline:
                _reap_process_group_children(child_pid)
                if not _process_group_exists(child_pid):
                    break
                try:
                    os.killpg(child_pid, signal.SIGKILL)
                except (ProcessLookupError, PermissionError):
                    pass
                time.sleep(0.005)
            _reap_process_group_children(child_pid)
        raise
    finally:
        for descriptor in (
            stdout_read,
            stdout_write,
            stderr_read,
            stderr_write,
            devnull_descriptor,
            execution_descriptor,
        ):
            if descriptor >= 0:
                try:
                    os.close(descriptor)
                except OSError:
                    pass


def _terminate_process_group(
    process: _SpawnedProcess, grace_seconds: float
) -> tuple[bool, bool, bool]:
    term_sent = False
    kill_sent = False
    process_group = process.pid
    if _process_group_exists(process_group):
        try:
            os.killpg(process_group, signal.SIGTERM)
            term_sent = True
        except ProcessLookupError:
            pass
    deadline = time.monotonic() + grace_seconds
    while _process_group_exists(process_group) and time.monotonic() < deadline:
        if process.poll() is None:
            try:
                process.wait(timeout=min(0.02, max(0.001, deadline - time.monotonic())))
            except subprocess.TimeoutExpired:
                pass
        else:
            time.sleep(0.005)
    if _process_group_exists(process_group):
        try:
            os.killpg(process_group, signal.SIGKILL)
            kill_sent = True
        except ProcessLookupError:
            pass
    try:
        process.wait(timeout=max(0.1, grace_seconds))
    except subprocess.TimeoutExpired:
        # A SIGKILL-resistant process would violate the host/runtime contract.
        # Do not block indefinitely; the caller records provenance failure.
        pass
    residual_deadline = time.monotonic() + max(1.0, grace_seconds)
    while time.monotonic() < residual_deadline:
        _reap_process_group_children(process_group)
        if not _process_group_exists(process_group):
            return term_sent, kill_sent, False
        time.sleep(0.005)
    _reap_process_group_children(process_group)
    return term_sent, kill_sent, _process_group_exists(process_group)


def _cleanup_process_group_after_scheduler_failure(
    process: _SpawnedProcess,
    threads: Sequence[threading.Thread],
    budgets: BranchBudgets,
) -> None:
    """Best-effort shielded cleanup before propagating a scheduler failure."""

    try:
        _term, _kill, residual = _terminate_process_group(
            process, float(budgets.term_grace_seconds)
        )
    except BaseException:
        residual = True
    if residual or _process_group_exists(process.pid):
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
        try:
            process.wait(timeout=max(0.1, float(budgets.term_grace_seconds)))
        except (subprocess.TimeoutExpired, ChildProcessError):
            pass
        for _index in range(200):
            _reap_process_group_children(process.pid)
            if not _process_group_exists(process.pid):
                break
            time.sleep(0.005)

    close_deadline = time.monotonic() + float(budgets.pipe_close_grace_seconds)
    process_sources = (process.stdout, process.stderr)
    for source in process_sources[len(threads) :]:
        if source is not None:
            try:
                source.close()
            except OSError:
                pass
    for index, thread in enumerate(threads):
        if thread.ident is None and process_sources[index] is not None:
            try:
                process_sources[index].close()
            except OSError:
                pass
        if thread.ident is not None:
            thread.join(timeout=max(0.0, close_deadline - time.monotonic()))
    if any(thread.is_alive() for thread in threads):
        for source in (process.stdout, process.stderr):
            if source is not None:
                try:
                    source.close()
                except OSError:
                    pass
        for thread in threads:
            if thread.ident is not None:
                thread.join(timeout=float(budgets.pipe_close_grace_seconds))
    _reap_process_group_children(process.pid)


def run_bounded_process(
    argv: Sequence[str],
    stdout_path: Path,
    stderr_path: Path,
    budgets: BranchBudgets,
    *,
    executable_descriptor: int,
) -> StreamedProcessOutcome:
    """Run one exact argv in a new process group with bounded streamed output."""

    budgets.validate()
    if type(argv) not in (list, tuple) or len(argv) != 12 or not all(
        type(value) is str for value in argv
    ):
        raise BranchContractError("process argv must be exactly 12 strings")
    if stdout_path.exists() or stderr_path.exists():
        raise BranchProvenanceError("raw staging output is not write-once")
    if type(executable_descriptor) is not int or executable_descriptor < 0:
        raise BranchContractError("a pinned executable descriptor is required")
    _enable_child_subreaper()

    stdout_stream = stdout_path.open("xb", buffering=0)
    stderr_stream = stderr_path.open("xb", buffering=0)
    process: _SpawnedProcess | None = None
    threads: tuple[threading.Thread, ...] = ()
    cleanup_state = {"active": False}
    previous_signal_handlers: dict[int, Any] = {}
    managed_signals = {signal.SIGINT, signal.SIGTERM}

    def unwind_for_scheduler_signal(
        signal_number: int, _frame: Any
    ) -> None:
        if cleanup_state["active"]:
            return
        if signal_number == signal.SIGINT:
            raise KeyboardInterrupt
        raise _SchedulerTerminationSignal(signal_number)

    try:
        if threading.current_thread() is threading.main_thread():
            prior_setup_mask = signal.pthread_sigmask(
                signal.SIG_BLOCK, managed_signals
            )
            try:
                for signal_number in (signal.SIGINT, signal.SIGTERM):
                    previous_signal_handlers[signal_number] = signal.getsignal(
                        signal_number
                    )
                    signal.signal(signal_number, unwind_for_scheduler_signal)
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, prior_setup_mask)
        try:
            # Block ownership-changing scheduler signals in every calling
            # thread, not only the main thread that can install Python signal
            # handlers.  A directly targeted pthread signal therefore cannot
            # interrupt the spawn-return/PID-assignment window either.
            prior_spawn_mask = signal.pthread_sigmask(
                signal.SIG_BLOCK, managed_signals
            )
            child_signal_mask = prior_spawn_mask
            try:
                process = _spawn_pinned_process(
                    argv,
                    executable_descriptor,
                    child_signal_mask,
                )
            finally:
                signal.pthread_sigmask(
                    signal.SIG_SETMASK, prior_spawn_mask
                )
        except OSError:
            stdout_stream.flush()
            stderr_stream.flush()
            os.fsync(stdout_stream.fileno())
            os.fsync(stderr_stream.fileno())
            return StreamedProcessOutcome(
                return_code=None,
                timed_out=False,
                output_budget_exhausted=False,
                descendant_group_survived_parent=False,
                descendant_pipe_leak=False,
                term_sent=False,
                kill_sent=False,
                stdout_size=0,
                stderr_size=0,
                stdout_truncated=False,
                stderr_truncated=False,
                stream_error=False,
                process_group_residual=False,
                spawn_error=True,
            )

        assert process.stdout is not None and process.stderr is not None
        budget_event = threading.Event()
        counts = {"stdout": 0, "stderr": 0}
        truncated = {"stdout": False, "stderr": False}
        stream_errors: list[str] = []

        def drain(
            name: str,
            source: Any,
            target: Any,
            cap: int,
        ) -> None:
            try:
                while True:
                    chunk = os.read(source.fileno(), 64 * 1024)
                    if not chunk:
                        break
                    remaining = cap - counts[name]
                    accepted = min(len(chunk), max(0, remaining))
                    if accepted:
                        view = memoryview(chunk)[:accepted]
                        while view:
                            written = target.write(view)
                            if written is None or written <= 0:
                                raise OSError("short raw-stream write")
                            view = view[written:]
                        counts[name] += accepted
                    if counts[name] >= cap:
                        truncated[name] = True
                        budget_event.set()
                        break
            except Exception:  # fixed fail-closed bit; no host-dependent message
                stream_errors.append(name)
                budget_event.set()
            finally:
                try:
                    source.close()
                except OSError:
                    pass
                try:
                    target.flush()
                    os.fsync(target.fileno())
                except OSError:
                    stream_errors.append(name)
                    budget_event.set()

        threads = (
            threading.Thread(
                target=drain,
                args=("stdout", process.stdout, stdout_stream, budgets.stdout_bytes),
                name="branch-stdout-drain",
                daemon=True,
            ),
            threading.Thread(
                target=drain,
                args=("stderr", process.stderr, stderr_stream, budgets.stderr_bytes),
                name="branch-stderr-drain",
                daemon=True,
            ),
        )
        for thread in threads:
            thread.start()

        deadline = time.monotonic() + float(budgets.timeout_seconds)
        timed_out = False
        output_exhausted = False
        term_sent = False
        kill_sent = False
        process_group_residual = False
        while process.poll() is None:
            if budget_event.wait(timeout=0.005):
                output_exhausted = True
                term_sent, kill_sent, process_group_residual = _terminate_process_group(
                    process, float(budgets.term_grace_seconds)
                )
                break
            if time.monotonic() >= deadline:
                timed_out = True
                term_sent, kill_sent, process_group_residual = _terminate_process_group(
                    process, float(budgets.term_grace_seconds)
                )
                break

        if process.poll() is None:
            # Defensive fallback if the process-group helper could not reap.
            more_term, more_kill, more_residual = _terminate_process_group(
                process, float(budgets.term_grace_seconds)
            )
            term_sent = term_sent or more_term
            kill_sent = kill_sent or more_kill
            process_group_residual = process_group_residual or more_residual
        else:
            process.wait()

        # Give pipes owned only by the exited leader one bounded opportunity to
        # reach EOF.  Threads still blocked after this grace period, while the
        # process group remains live, are evidence that a descendant retained
        # a copied pipe descriptor rather than a scheduler-thread race.
        pipe_close_deadline = time.monotonic() + float(
            budgets.pipe_close_grace_seconds
        )
        for thread in threads:
            thread.join(timeout=max(0.0, pipe_close_deadline - time.monotonic()))

        descendant_group_survived_parent = _process_group_exists(process.pid)
        pipe_held_by_descendant = (
            descendant_group_survived_parent
            and any(thread.is_alive() for thread in threads)
        )
        if descendant_group_survived_parent:
            more_term, more_kill, more_residual = _terminate_process_group(
                process, float(budgets.term_grace_seconds)
            )
            term_sent = term_sent or more_term
            kill_sent = kill_sent or more_kill
            process_group_residual = process_group_residual or more_residual

        pipe_close_deadline = time.monotonic() + float(
            budgets.pipe_close_grace_seconds
        )
        for thread in threads:
            thread.join(timeout=max(0.0, pipe_close_deadline - time.monotonic()))
        output_exhausted = output_exhausted or (
            budget_event.is_set() and not stream_errors
        )
        descendant_leak = pipe_held_by_descendant or any(
            thread.is_alive() for thread in threads
        )
        if descendant_leak:
            more_term, more_kill, more_residual = _terminate_process_group(
                process, float(budgets.term_grace_seconds)
            )
            term_sent = term_sent or more_term
            kill_sent = kill_sent or more_kill
            process_group_residual = process_group_residual or more_residual
            for thread in threads:
                thread.join(timeout=float(budgets.pipe_close_grace_seconds))
            if any(thread.is_alive() for thread in threads):
                process_group_residual = True

        stdout_stream.flush()
        stderr_stream.flush()
        os.fsync(stdout_stream.fileno())
        os.fsync(stderr_stream.fileno())
        return StreamedProcessOutcome(
            return_code=process.returncode,
            timed_out=timed_out,
            output_budget_exhausted=output_exhausted,
            descendant_group_survived_parent=descendant_group_survived_parent,
            descendant_pipe_leak=descendant_leak,
            term_sent=term_sent,
            kill_sent=kill_sent,
            stdout_size=counts["stdout"],
            stderr_size=counts["stderr"],
            stdout_truncated=truncated["stdout"],
            stderr_truncated=truncated["stderr"],
            stream_error=bool(stream_errors),
            process_group_residual=process_group_residual,
            spawn_error=False,
        )
    except BaseException:
        cleanup_state["active"] = True
        if process is not None:
            _cleanup_process_group_after_scheduler_failure(
                process, threads, budgets
            )
        for stream in (stdout_stream, stderr_stream):
            try:
                stream.flush()
                os.fsync(stream.fileno())
            except OSError:
                pass
        raise
    finally:
        prior_restore_mask: set[signal.Signals] | None = None
        try:
            if previous_signal_handlers:
                prior_restore_mask = signal.pthread_sigmask(
                    signal.SIG_BLOCK, managed_signals
                )
                for signal_number, previous_handler in (
                    previous_signal_handlers.items()
                ):
                    signal.signal(signal_number, previous_handler)
        finally:
            stdout_stream.close()
            stderr_stream.close()
            if prior_restore_mask is not None:
                signal.pthread_sigmask(
                    signal.SIG_SETMASK, prior_restore_mask
                )


def _common_record_fields(
    artifact_role: str, bindings: BranchBindings
) -> dict[str, Any]:
    return {
        "artifact_role": artifact_role,
        "authority": "PRODUCER_ONLY",
        "claim_boundary": CLAIM_BOUNDARY,
        "component_status": None,
        "final_status": None,
        "freeze_sha256": bindings.freeze_sha256,
        "matrix_id": bindings.matrix_id,
        "milestone_status": None,
        "protocol_id": PROTOCOL_ID,
        "run_config_sha256": bindings.run_config_sha256,
        "schema_version": SCHEMA_VERSION,
        "scientific_licensing_enabled": False,
        "theorem_status": None,
    }


def _classify_process(
    outcome: StreamedProcessOutcome,
    stdout: bytes,
    stderr: bytes,
    task: BranchCellTask,
) -> tuple[str, str | None, str | None]:
    if outcome.spawn_error:
        return "PROVENANCE_INVALID", None, "PROCESS_SPAWN_FAILED"
    if outcome.stream_error:
        return "PROVENANCE_INVALID", None, "RAW_STREAM_IO_FAILED"
    if outcome.process_group_residual:
        return "PROVENANCE_INVALID", None, "PROCESS_GROUP_RESIDUAL"
    if outcome.output_budget_exhausted:
        return "CELL_OUTPUT_BUDGET_EXHAUSTED", None, "RAW_STREAM_CAP_REACHED"
    if outcome.timed_out:
        return "CELL_TIMEOUT", None, "FROZEN_CELL_TIMEOUT"
    if outcome.return_code is None:
        return "PROVENANCE_INVALID", None, "MISSING_RETURN_CODE"
    if outcome.return_code < 0:
        return "CELL_SIGNAL", None, "EVALUATOR_SIGNAL"
    if outcome.descendant_group_survived_parent:
        return "PROVENANCE_INVALID", None, "DESCENDANT_GROUP_SURVIVED_PARENT"
    if outcome.descendant_pipe_leak:
        return "PROVENANCE_INVALID", None, "DESCENDANT_PIPE_LEAK"
    try:
        evaluator_status = parse_evaluator_abi(
            stdout, stderr, outcome.return_code, task
        )
    except BranchContractError as error:
        return "MALFORMED_EVALUATOR_OUTPUT", None, str(error)
    return "COMMITTED_EVALUATOR_RESULT", evaluator_status, None


def _record_payload(
    task: BranchCellTask,
    bindings: BranchBindings,
    budgets: BranchBudgets,
    outcome: StreamedProcessOutcome,
    stdout_path: str,
    stderr_path: str,
    stdout: bytes,
    stderr: bytes,
    *,
    execution_pin: Mapping[str, Any],
    provenance_failure_reason: str | None = None,
) -> dict[str, Any]:
    classification, evaluator_status, failure_reason = _classify_process(
        outcome, stdout, stderr, task
    )
    if provenance_failure_reason is not None:
        classification = "PROVENANCE_INVALID"
        evaluator_status = None
        failure_reason = provenance_failure_reason
    if classification not in SCHEDULER_CLASSIFICATIONS:
        raise AssertionError("internal scheduler classification escaped whitelist")
    argv = task.argv()
    record = _common_record_fields("BRANCH_CELL_RECORD", bindings)
    record.update(
        {
            "bindings": bindings.payload(),
            "budgets": budgets.payload(),
            "cell": task.payload(),
            "execution_pin": dict(execution_pin),
            "invocation": {
                "argument_echo_count": 12,
                "argv": argv,
                "argv0_scheduler_binding": argv[0],
                "argv_sha256": sha256_bytes(canonical_json_bytes(argv)),
                "exact_string_count": len(argv),
            },
            "raw": {
                "stderr_bytes": len(stderr),
                "stderr_cap_bytes": budgets.stderr_bytes,
                "stderr_file": stderr_path,
                "stderr_sha256": sha256_bytes(stderr),
                "stderr_truncated": outcome.stderr_truncated,
                "stdout_bytes": len(stdout),
                "stdout_cap_bytes": budgets.stdout_bytes,
                "stdout_file": stdout_path,
                "stdout_sha256": sha256_bytes(stdout),
                "stdout_truncated": outcome.stdout_truncated,
                "total_cell_cap_bytes": budgets.total_cell_bytes,
            },
            "scheduler_result": {
                "classification": classification,
                "descendant_group_survived_parent": (
                    outcome.descendant_group_survived_parent
                ),
                "descendant_pipe_leak": outcome.descendant_pipe_leak,
                "evaluator_status": evaluator_status,
                "failure_reason": failure_reason,
                "kill_sent": outcome.kill_sent,
                "process_group_residual": outcome.process_group_residual,
                "return_code": outcome.return_code,
                "signal_number": (
                    -outcome.return_code
                    if outcome.return_code is not None and outcome.return_code < 0
                    else None
                ),
                "term_sent": outcome.term_sent,
                "timed_out": outcome.timed_out,
            },
        }
    )
    record["raw"]["record_cap_bytes"] = budgets.record_bytes
    record["raw"]["record_truncated"] = False
    return record


def _canonical_paths(
    output_root: Path, operational_root: Path, task: BranchCellTask
) -> tuple[Path, Path, Path, Path, Path]:
    cell = output_root / "branch" / "cells" / str(task.precision_bits) / task.slab_id
    manifest = (
        output_root
        / "branch"
        / "cell_manifests"
        / str(task.precision_bits)
        / f"{task.slab_id}.json"
    )
    staging_parent = (
        operational_root / "staging" / "branch" / str(task.precision_bits)
    )
    lock_parent = operational_root / "locks" / "branch" / str(task.precision_bits)
    lock = lock_parent / f"{task.slab_id}.lock"
    return cell, manifest, staging_parent, lock_parent, lock


def _manifest_payload(
    output_root: Path,
    cell: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    budgets: BranchBudgets,
    file_role_map: Mapping[str, str],
) -> dict[str, Any]:
    expected_roles = {
        (cell / name).relative_to(output_root).as_posix()
        for name in ("record.json", "stderr.txt", "stdout.txt")
    }
    if set(file_role_map) != expected_roles or any(
        type(relative) is not str
        or _strict_relative(relative).as_posix() != relative
        or type(digest) is not str
        or HEX64_PATTERN.fullmatch(digest) is None
        for relative, digest in file_role_map.items()
    ):
        raise BranchProvenanceError("manifest file-role map is not exact")
    payload = _common_record_fields("BRANCH_CELL_MANIFEST", bindings)
    payload.update(
        {
            "budgets": budgets.payload(),
            "cell_identity": {
                "precision_bits": task.precision_bits,
                "slab_id": task.slab_id,
            },
            "files": dict(file_role_map),
            "task_binding_sha256": sha256_bytes(
                canonical_json_bytes(task.payload())
            ),
        }
    )
    return payload


def _publish_write_once(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _reject_symlink_components(path.parent, "write-once parent")
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != payload:
            raise BranchProvenanceError(f"write-once object differs: {path}")
        return
    temporary = path.parent / f".{path.name}.publish-{os.getpid()}-{threading.get_ident()}"
    try:
        _write_exclusive_fsync(temporary, payload)
        try:
            os.link(temporary, path, follow_symlinks=False)
        except FileExistsError:
            if path.is_symlink() or not path.is_file() or path.read_bytes() != payload:
                raise BranchProvenanceError(f"concurrent write-once conflict: {path}")
        _fsync_directory(path.parent)
    finally:
        if temporary.exists():
            temporary.unlink()
            _fsync_directory(path.parent)


def _pin_persistent_inputs(
    task: BranchCellTask,
    bindings: BranchBindings,
    output_root: Path,
    operational_root: Path,
) -> tuple[PinnedRegularFile, PinnedRegularFile]:
    binary = Path(task.evaluator_binary_path)
    source = Path(bindings.evaluator_source_path)
    for candidate, label in ((binary, "binary"), (source, "source")):
        resolved = candidate.resolve(strict=True)
        for forbidden_root in (output_root.resolve(), operational_root.resolve()):
            if resolved == forbidden_root or forbidden_root in resolved.parents:
                raise BranchProvenanceError(
                    f"persistent evaluator {label} may not live in a result directory"
                )
    source_pin: PinnedRegularFile | None = None
    binary_pin: PinnedRegularFile | None = None
    try:
        source_pin = PinnedRegularFile.open(
            source,
            bindings.evaluator_source_sha256,
            executable=False,
            context="evaluator source",
        )
        binary_pin = PinnedRegularFile.open(
            binary,
            bindings.evaluator_binary_sha256,
            executable=True,
            context="persistent evaluator binary",
        )
        return source_pin, binary_pin
    except Exception:
        if binary_pin is not None:
            binary_pin.close()
        if source_pin is not None:
            source_pin.close()
        raise


def _verify_pins(
    source_pin: PinnedRegularFile,
    binary_pin: PinnedRegularFile,
) -> tuple[dict[str, Any], str | None]:
    execution_pin = {
        "binary": binary_pin.verify_after(),
        "source": source_pin.verify_after(),
    }
    for role in ("source", "binary"):
        pin = execution_pin[role]
        if not pin["descriptor_identity_matches_after"]:
            return execution_pin, f"PINNED_{role.upper()}_INODE_CHANGED"
        if not pin["descriptor_hash_matches_after"]:
            return execution_pin, f"PINNED_{role.upper()}_HASH_CHANGED"
        if not pin["path_identity_matches_after"]:
            return execution_pin, f"PINNED_{role.upper()}_PATH_SWAPPED"
    return execution_pin, None


def _strict_json_object_bytes(payload: bytes, context: str) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise BranchProvenanceError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject_constant(token: str) -> None:
        raise BranchProvenanceError(f"nonfinite JSON token: {token}")

    try:
        value = json.loads(
            payload.decode("utf-8", errors="strict"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise BranchProvenanceError(f"strict JSON parse failed: {context}") from error
    if type(value) is not dict:
        raise BranchProvenanceError("top-level JSON object required")
    return value


def _strict_json_object(path: Path) -> dict[str, Any]:
    snapshot = _snapshot_regular_file(path, "strict JSON object")
    value = _strict_json_object_bytes(snapshot.payload, str(path))
    if canonical_json_bytes(value) != snapshot.payload:
        raise BranchProvenanceError(f"JSON object is not canonical: {path}")
    snapshot.verify_unchanged("strict JSON object")
    return value


def _validate_cell_without_manifest(
    output_root: Path,
    cell: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    budgets: BranchBudgets,
) -> tuple[
    dict[str, Any],
    dict[str, str],
    dict[str, RegularFileSnapshot],
]:
    """Validate every canonical cell byte before trusting/publishing a manifest."""

    _reject_symlink_components(cell, "committed cell")
    if cell.is_symlink() or not cell.is_dir():
        raise BranchProvenanceError("committed cell directory is absent or aliased")
    actual = {path.name for path in cell.iterdir()}
    if actual != {"stdout.txt", "stderr.txt", "record.json"}:
        raise BranchProvenanceError(f"committed branch cell file set mismatch: {actual}")
    snapshots = {
        "record.json": _snapshot_regular_file(
            cell / "record.json",
            "committed branch record",
            maximum_bytes=budgets.record_bytes,
        ),
        "stderr.txt": _snapshot_regular_file(
            cell / "stderr.txt",
            "committed branch stderr",
            maximum_bytes=budgets.stderr_bytes,
        ),
        "stdout.txt": _snapshot_regular_file(
            cell / "stdout.txt",
            "committed branch stdout",
            maximum_bytes=budgets.stdout_bytes,
        ),
    }
    record_payload = snapshots["record.json"].payload
    record = _strict_json_object_bytes(record_payload, "committed branch record")
    if canonical_json_bytes(record) != record_payload:
        raise BranchProvenanceError("record JSON is not canonical")
    expected_common = _common_record_fields("BRANCH_CELL_RECORD", bindings)
    expected_top_keys = set(expected_common) | {
        "bindings",
        "budgets",
        "cell",
        "execution_pin",
        "invocation",
        "raw",
        "scheduler_result",
    }
    if set(record) != expected_top_keys:
        raise BranchProvenanceError("record top-level schema is not closed")
    if any(record.get(key) != value or type(record.get(key)) is not type(value)
           for key, value in expected_common.items()):
        raise BranchProvenanceError("record common binding mismatch")
    if canonical_json_bytes(record.get("bindings")) != canonical_json_bytes(
        bindings.payload()
    ):
        raise BranchProvenanceError("record evaluator/dependency binding mismatch")
    if canonical_json_bytes(record.get("budgets")) != canonical_json_bytes(
        budgets.payload()
    ):
        raise BranchProvenanceError("record frozen-budget binding mismatch")
    execution_pin = record.get("execution_pin")
    if type(execution_pin) is not dict or set(execution_pin) != {"binary", "source"}:
        raise BranchProvenanceError("record execution-pin schema is not closed")
    for role, expected_path, expected_hash in (
        ("binary", task.evaluator_binary_path, bindings.evaluator_binary_sha256),
        ("source", bindings.evaluator_source_path, bindings.evaluator_source_sha256),
    ):
        pin = execution_pin.get(role)
        if (
            type(pin) is not dict
            or set(pin)
            != {
                "descriptor_hash_matches_after",
                "descriptor_identity_matches_after",
                "device",
                "inode",
                "mode",
                "path",
                "path_identity_matches_after",
                "sha256",
                "size",
            }
            or pin.get("path") != expected_path
            or pin.get("sha256") != expected_hash
        ):
            raise BranchProvenanceError("record pinned-file binding mismatch")
        for key in (
            "descriptor_hash_matches_after",
            "descriptor_identity_matches_after",
            "path_identity_matches_after",
        ):
            if type(pin.get(key)) is not bool:
                raise BranchProvenanceError("record pinned-file Boolean is malformed")
        for key in ("device", "inode", "mode", "size"):
            if type(pin.get(key)) is not int or pin[key] < 0:
                raise BranchProvenanceError("record pinned-file integer is malformed")
    if canonical_json_bytes(record.get("cell")) != canonical_json_bytes(task.payload()):
        raise BranchProvenanceError("record task binding mismatch")
    invocation = record.get("invocation")
    expected_argv = task.argv()
    if (
        type(invocation) is not dict
        or set(invocation)
        != {
            "argument_echo_count",
            "argv",
            "argv0_scheduler_binding",
            "argv_sha256",
            "exact_string_count",
        }
        or invocation.get("argv") != expected_argv
        or invocation.get("argv0_scheduler_binding") != expected_argv[0]
        or invocation.get("argument_echo_count") != 12
        or type(invocation.get("argument_echo_count")) is not int
        or invocation.get("exact_string_count") != 12
        or type(invocation.get("exact_string_count")) is not int
        or invocation.get("argv_sha256")
        != sha256_bytes(canonical_json_bytes(expected_argv))
    ):
        raise BranchProvenanceError("record invocation mismatch")
    raw = record.get("raw")
    if type(raw) is not dict:
        raise BranchProvenanceError("record raw binding is absent")
    base_raw_keys = {
        "record_cap_bytes",
        "record_truncated",
        "stderr_bytes",
        "stderr_cap_bytes",
        "stderr_file",
        "stderr_sha256",
        "stderr_truncated",
        "stdout_bytes",
        "stdout_cap_bytes",
        "stdout_file",
        "stdout_sha256",
        "stdout_truncated",
        "total_cell_cap_bytes",
    }
    if set(raw) != base_raw_keys:
        raise BranchProvenanceError("record raw schema is not closed")
    for key in (
        "record_cap_bytes",
        "stderr_bytes",
        "stderr_cap_bytes",
        "stdout_bytes",
        "stdout_cap_bytes",
        "total_cell_cap_bytes",
    ):
        if type(raw.get(key)) is not int or raw[key] < 0:
            raise BranchProvenanceError("record raw integer field is malformed")
    for key in ("record_truncated", "stderr_truncated", "stdout_truncated"):
        if type(raw.get(key)) is not bool:
            raise BranchProvenanceError("record truncation field is not Boolean")
    if raw["record_truncated"] is not False:
        raise BranchProvenanceError("closed-schema record may not self-truncate")
    for stem in ("stdout", "stderr"):
        relative = raw.get(f"{stem}_file")
        if type(relative) is not str:
            raise BranchProvenanceError("record raw path is malformed")
        parts = _strict_relative(relative)
        raw_path = output_root / Path(*parts.parts)
        if raw_path != cell / f"{stem}.txt":
            raise BranchProvenanceError("record raw path is noncanonical")
        payload = snapshots[f"{stem}.txt"].payload
        if (
            raw.get(f"{stem}_sha256") != sha256_bytes(payload)
            or raw.get(f"{stem}_bytes") != len(payload)
            or type(raw.get(f"{stem}_bytes")) is not int
        ):
            raise BranchProvenanceError("record raw byte binding mismatch")
    if raw["stdout_cap_bytes"] != budgets.stdout_bytes:
        raise BranchProvenanceError("record stdout cap differs from frozen budget")
    if raw["stderr_cap_bytes"] != budgets.stderr_bytes:
        raise BranchProvenanceError("record stderr cap differs from frozen budget")
    if raw["record_cap_bytes"] != budgets.record_bytes:
        raise BranchProvenanceError("record byte cap differs from frozen budget")
    if raw["total_cell_cap_bytes"] != budgets.total_cell_bytes:
        raise BranchProvenanceError("record total-cell cap differs from frozen budget")
    if raw["stdout_bytes"] > budgets.stdout_bytes:
        raise BranchProvenanceError("stdout exceeds frozen byte cap")
    if raw["stderr_bytes"] > budgets.stderr_bytes:
        raise BranchProvenanceError("stderr exceeds frozen byte cap")
    if raw["stdout_truncated"] and raw["stdout_bytes"] != budgets.stdout_bytes:
        raise BranchProvenanceError("stdout truncation lacks exact cap equality")
    if raw["stderr_truncated"] and raw["stderr_bytes"] != budgets.stderr_bytes:
        raise BranchProvenanceError("stderr truncation lacks exact cap equality")
    record_size = len(record_payload)
    if record_size >= budgets.record_bytes:
        raise BranchProvenanceError("record reaches or exceeds frozen byte cap")
    if raw["stdout_bytes"] + raw["stderr_bytes"] + record_size >= budgets.total_cell_bytes:
        raise BranchProvenanceError("cell reaches or exceeds frozen total byte cap")
    scheduler_result = record.get("scheduler_result")
    if (
        type(scheduler_result) is not dict
        or set(scheduler_result)
        != {
            "classification",
            "descendant_group_survived_parent",
            "descendant_pipe_leak",
            "evaluator_status",
            "failure_reason",
            "kill_sent",
            "process_group_residual",
            "return_code",
            "signal_number",
            "term_sent",
            "timed_out",
        }
        or scheduler_result.get("classification") not in SCHEDULER_CLASSIFICATIONS
    ):
        raise BranchProvenanceError("record scheduler classification mismatch")
    for key in (
        "descendant_group_survived_parent",
        "descendant_pipe_leak",
        "kill_sent",
        "process_group_residual",
        "term_sent",
        "timed_out",
    ):
        if type(scheduler_result.get(key)) is not bool:
            raise BranchProvenanceError("scheduler process-control field is not Boolean")
    if scheduler_result.get("return_code") is not None and type(
        scheduler_result["return_code"]
    ) is not int:
        raise BranchProvenanceError("scheduler return code is not an exact integer")
    if scheduler_result.get("signal_number") is not None and type(
        scheduler_result["signal_number"]
    ) is not int:
        raise BranchProvenanceError("scheduler signal number is not an exact integer")
    classification = scheduler_result["classification"]
    evaluator_status = scheduler_result.get("evaluator_status")
    pin_all_valid = all(
        pin[key]
        for pin in execution_pin.values()
        for key in (
            "descriptor_hash_matches_after",
            "descriptor_identity_matches_after",
            "path_identity_matches_after",
        )
    )
    if not pin_all_valid and classification != "PROVENANCE_INVALID":
        raise BranchProvenanceError("invalid pinned identity escaped provenance failure")
    if classification == "COMMITTED_EVALUATOR_RESULT":
        if scheduler_result.get("failure_reason") is not None:
            raise BranchProvenanceError("committed evaluator result carries failure reason")
        if evaluator_status not in EVALUATOR_STATUS_CODES:
            raise BranchProvenanceError("committed evaluator status is invalid")
        return_code = scheduler_result.get("return_code")
        if type(return_code) is not int:
            raise BranchProvenanceError("committed evaluator return code is absent")
        try:
            parsed_status = parse_evaluator_abi(
                snapshots["stdout.txt"].payload,
                snapshots["stderr.txt"].payload,
                return_code,
                task,
            )
        except BranchContractError as error:
            raise BranchProvenanceError(
                "committed evaluator transcript fails ABI replay"
            ) from error
        if parsed_status != evaluator_status:
            raise BranchProvenanceError("committed evaluator status replay mismatch")
    elif evaluator_status is not None:
        raise BranchProvenanceError("scheduler failure forged evaluator status")
    elif type(scheduler_result.get("failure_reason")) is not str:
        raise BranchProvenanceError("scheduler failure lacks an exact reason string")
    return_code = scheduler_result.get("return_code")
    signal_number = scheduler_result.get("signal_number")
    if type(return_code) is int and return_code < 0:
        if type(signal_number) is not int or signal_number != -return_code:
            raise BranchProvenanceError("terminal signal metadata is contradictory")
    elif signal_number is not None:
        raise BranchProvenanceError("nonsignaled process carries a signal number")
    if classification == "CELL_SIGNAL" and (
        type(return_code) is not int or return_code >= 0
    ):
        raise BranchProvenanceError("scheduler signal classification lacks a signal")
    if (
        scheduler_result.get("descendant_group_survived_parent") is True
        and classification not in {"CELL_SIGNAL", "PROVENANCE_INVALID"}
    ):
        raise BranchProvenanceError(
            "surviving descendant group escaped scheduler failure"
        )
    if classification == "CELL_TIMEOUT" and scheduler_result.get("timed_out") is not True:
        raise BranchProvenanceError("timeout classification lacks timeout witness")
    if scheduler_result.get("process_group_residual") is True and classification != "PROVENANCE_INVALID":
        raise BranchProvenanceError("process-group residual escaped provenance failure")
    if classification == "CELL_OUTPUT_BUDGET_EXHAUSTED" and not any(
        raw[key]
        for key in ("stdout_truncated", "stderr_truncated", "record_truncated")
    ):
        raise BranchProvenanceError("output-budget classification lacks truncation witness")
    _reject_symlink_components(cell, "committed cell after snapshot validation")
    if cell.is_symlink() or not cell.is_dir() or {
        path.name for path in cell.iterdir()
    } != set(snapshots):
        raise BranchProvenanceError("committed branch cell changed during validation")
    for name, snapshot in snapshots.items():
        snapshot.verify_unchanged(f"committed branch {name}")
    file_role_map: dict[str, str] = {}
    for name, snapshot in snapshots.items():
        relative = (cell / name).relative_to(output_root).as_posix()
        _strict_relative(relative)
        file_role_map[relative] = sha256_bytes(snapshot.payload)
    return record, file_role_map, snapshots


def validate_committed_branch_cell(
    output_root: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    budgets: BranchBudgets,
) -> tuple[dict[str, Any], dict[str, Any]]:
    cell, manifest_path, _staging, _lock_parent, _lock = _canonical_paths(
        output_root, output_root.parent / f"{output_root.name}.operational", task
    )
    record, file_role_map, cell_snapshots = _validate_cell_without_manifest(
        output_root, cell, task, bindings, budgets
    )

    _reject_symlink_components(manifest_path, "branch cell manifest")
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise BranchProvenanceError("branch cell manifest is absent or aliased")
    manifest_snapshot = _snapshot_regular_file(
        manifest_path,
        "branch cell manifest",
        maximum_bytes=budgets.record_bytes,
    )
    manifest = _strict_json_object_bytes(
        manifest_snapshot.payload, "branch cell manifest"
    )
    if canonical_json_bytes(manifest) != manifest_snapshot.payload:
        raise BranchProvenanceError("manifest JSON is not canonical")
    expected_manifest = _manifest_payload(
        output_root, cell, task, bindings, budgets, file_role_map
    )
    if canonical_json_bytes(manifest) != canonical_json_bytes(expected_manifest):
        raise BranchProvenanceError("branch cell manifest differs from recomputation")
    for name, snapshot in cell_snapshots.items():
        snapshot.verify_unchanged(f"committed branch {name}")
    manifest_snapshot.verify_unchanged("branch cell manifest")
    return record, manifest


def _recover_manifestless_commit(
    output_root: Path,
    operational_root: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    budgets: BranchBudgets,
) -> tuple[dict[str, Any], dict[str, Any]]:
    cell, manifest_path, _staging, _lock_parent, _lock = _canonical_paths(
        output_root, operational_root, task
    )
    if not cell.is_dir() or cell.is_symlink() or manifest_path.exists() or manifest_path.is_symlink():
        raise BranchProvenanceError("manifestless recovery precondition failed")
    # Revalidate every canonical cell byte before constructing the unique
    # manifest.  Publication happens only after this full replay succeeds; the
    # cell itself remains byte-for-byte unchanged.
    _record, file_role_map, _snapshots = _validate_cell_without_manifest(
        output_root, cell, task, bindings, budgets
    )
    manifest = _manifest_payload(
        output_root, cell, task, bindings, budgets, file_role_map
    )
    _publish_write_once(manifest_path, canonical_json_bytes(manifest))
    return validate_committed_branch_cell(output_root, task, bindings, budgets)


def _process_start_time(pid: int) -> int | None:
    try:
        raw = Path(f"/proc/{pid}/stat").read_text(encoding="utf-8")
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None
    closing = raw.rfind(")")
    if closing < 0:
        return None
    fields_after_comm = raw[closing + 2 :].split()
    if len(fields_after_comm) <= 19:
        return None
    try:
        return int(fields_after_comm[19])
    except ValueError:
        return None


def _scan_exact_staging_namespace(
    operational_root: Path, expected_generation_prefix: str | None = None
) -> dict[tuple[int, str], tuple[Path, int, str]]:
    branch_root = operational_root / "staging" / "branch"
    if not branch_root.exists() and not branch_root.is_symlink():
        return {}
    _reject_symlink_components(branch_root, "branch staging namespace")
    if branch_root.is_symlink() or not branch_root.is_dir():
        raise BranchProvenanceError("branch staging root is not a regular directory")
    observed_cells: set[tuple[str, str]] = set()
    active: dict[tuple[int, str], tuple[Path, int, str]] = {}
    for precision_entry in branch_root.iterdir():
        if precision_entry.name not in {"128", "256"}:
            raise BranchProvenanceError("unexpected precision in branch staging namespace")
        if precision_entry.is_symlink() or not precision_entry.is_dir():
            raise BranchProvenanceError("branch staging precision path is aliased")
        for entry in precision_entry.iterdir():
            match = STAGING_NAME_PATTERN.fullmatch(entry.name)
            if match is None:
                raise BranchProvenanceError(
                    f"unexpected branch staging name: {entry.name}"
                )
            if (
                expected_generation_prefix is not None
                and match.group(2) != expected_generation_prefix
            ):
                raise BranchProvenanceError(
                    "staging generation differs from the sealed run configuration"
                )
            cell_key = (precision_entry.name, match.group(1))
            if cell_key in observed_cells:
                raise BranchProvenanceError(
                    "multiple live staging owners for one branch cell"
                )
            observed_cells.add(cell_key)
            if entry.is_symlink() or not entry.is_dir():
                raise BranchProvenanceError("branch staging object is not a directory")
            active[(int(precision_entry.name), match.group(1))] = (
                entry,
                int(match.group(3)),
                match.group(2),
            )
    return active


def _reject_withdrawn_interrupted_staging_namespace(
    operational_root: Path,
) -> None:
    branch_root = operational_root / "interrupted" / "branch"
    if not branch_root.exists() and not branch_root.is_symlink():
        return
    raise BranchProvenanceError(
        "detached per-cell interrupted staging namespace is withdrawn"
    )


def _reject_retained_staging_before_admission(
    operational_root: Path,
    task: BranchCellTask,
    current_generation_prefix: str,
) -> None:
    _reject_withdrawn_interrupted_staging_namespace(operational_root)
    active = _scan_exact_staging_namespace(
        operational_root, current_generation_prefix
    )
    for (precision_bits, slab_id), (
        stage,
        stage_attempt,
        generation_prefix,
    ) in active.items():
        if (precision_bits, slab_id) == (task.precision_bits, task.slab_id):
            raise BranchProvenanceError(
                "retained branch staging blocks this cell admission; "
                "whole-generation quarantine required"
            )
        lock_path = (
            operational_root
            / "locks"
            / "branch"
            / str(precision_bits)
            / f"{slab_id}.lock"
        )
        payload, snapshot = _validated_lock_snapshot(
            lock_path,
            context="live owner for another branch staging cell",
            expected_precision_bits=precision_bits,
            expected_slab_id=slab_id,
            expected_generation_prefix=generation_prefix,
        )
        if payload["attempt"] != stage_attempt:
            raise BranchProvenanceError(
                "other-cell staging attempt differs from its live owner lock"
            )
        if _process_start_time(payload["pid"]) != payload["owner_process_start_time"]:
            raise BranchProvenanceError(
                "other-cell staging has no matching live owner"
            )
        if not stage.is_dir() or stage.is_symlink():
            raise BranchProvenanceError("other-cell staging changed during admission")
        snapshot.verify_unchanged("live owner for another branch staging cell")


@dataclass(frozen=True)
class _LockNamespaceGuard:
    descriptor: int
    anchor_path: Path
    anchor_identity: tuple[int, int]
    operational_path: Path
    operational_identity: tuple[int, int]
    locks_path: Path
    locks_identity: tuple[int, int]
    branch_path: Path
    branch_identity: tuple[int, int]


@dataclass
class _LockNamespaceGuardOwner:
    guard: _LockNamespaceGuard | None = None


@dataclass
class _CellLockOwner:
    descriptor: int | None = None
    identity: tuple[int, int] | None = None
    payload: bytes | None = None


def _guard_directory_identity(path: Path, context: str) -> tuple[int, int]:
    _reject_symlink_components(path, context)
    try:
        metadata = os.stat(path, follow_symlinks=False)
    except OSError as error:
        raise BranchProvenanceError(f"cannot bind {context}") from error
    if path.is_symlink() or not stat.S_ISDIR(metadata.st_mode):
        raise BranchProvenanceError(f"{context} is not a canonical directory")
    return metadata.st_dev, metadata.st_ino


def _validate_lock_guard_paths(
    operational_root: Path,
) -> tuple[
    Path,
    tuple[int, int],
    Path,
    tuple[int, int],
    Path,
    tuple[int, int],
    Path,
    tuple[int, int],
]:
    anchor_path = operational_root.parent
    operational_identity = _guard_directory_identity(
        operational_root, "operational lock-guard root"
    )
    locks_path = operational_root / "locks"
    locks_identity = _guard_directory_identity(
        locks_path, "lock-guard namespace root"
    )
    branch_path = locks_path / "branch"
    branch_identity = _guard_directory_identity(
        branch_path, "branch lock publication namespace"
    )
    unexpected = {
        entry.name for entry in locks_path.iterdir()
    } - {"branch", "static"}
    if unexpected:
        raise BranchProvenanceError(
            "unexpected object in the component lock namespace root"
        )
    anchor_identity = _guard_directory_identity(
        anchor_path, "lock-guard stable parent"
    )
    return (
        anchor_path,
        anchor_identity,
        operational_root,
        operational_identity,
        locks_path,
        locks_identity,
        branch_path,
        branch_identity,
    )


def _acquire_lock_namespace_guard(
    operational_root: Path,
    owner: _LockNamespaceGuardOwner | None = None,
) -> _LockNamespaceGuard:
    # Lock the stable parent, not the replaceable `locks/branch` leaf.  A
    # rename/recreate of that leaf can otherwise create two independently
    # locked inodes.  Canonical path identities are replayed after acquiring
    # the parent lock and again before release.
    managed_signals = {signal.SIGINT, signal.SIGTERM}
    active_prior_mask: set[signal.Signals] | None = None
    descriptor = -1
    locked = False
    transferred = False
    try:
        anchor_path = operational_root.parent
        _reject_symlink_components(anchor_path, "lock-guard stable parent")
        active_prior_mask = signal.pthread_sigmask(
            signal.SIG_BLOCK, managed_signals
        )
        descriptor = os.open(
            anchor_path,
            os.O_RDONLY
            | getattr(os, "O_DIRECTORY", 0)
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0),
        )
        signal.pthread_sigmask(signal.SIG_SETMASK, active_prior_mask)
        active_prior_mask = None

        # Never wait in a blocking flock while scheduler signals are masked.
        # Each nonblocking attempt is briefly shielded so a successful kernel
        # acquisition and the local ownership bit are atomic with respect to
        # SIGINT/SIGTERM.  Contended backoff remains signal-responsive.
        acquisition_deadline = (
            time.monotonic() + LOCK_GUARD_ACQUIRE_TIMEOUT_SECONDS
        )
        while not locked:
            active_prior_mask = signal.pthread_sigmask(
                signal.SIG_BLOCK, managed_signals
            )
            try:
                fcntl.flock(
                    descriptor,
                    fcntl.LOCK_EX | fcntl.LOCK_NB,
                )
                locked = True
            except OSError as error:
                if error.errno not in (errno.EACCES, errno.EAGAIN):
                    raise
            if not locked:
                signal.pthread_sigmask(
                    signal.SIG_SETMASK, active_prior_mask
                )
                active_prior_mask = None
                remaining = acquisition_deadline - time.monotonic()
                if remaining <= 0:
                    raise BranchProvenanceError(
                        "branch lock-guard acquisition deadline exceeded"
                    )
                time.sleep(min(0.01, remaining))

        # Once `locked` owns the successful flock, restore immediately: path
        # replay may touch the filesystem and must remain interruptible.  Any
        # exception from this point is handled by the owned-descriptor cleanup
        # below.  Production callers separately shield their return/assignment
        # ownership handoffs.
        assert active_prior_mask is not None
        signal.pthread_sigmask(signal.SIG_SETMASK, active_prior_mask)
        active_prior_mask = None
        paths = _validate_lock_guard_paths(operational_root)
        descriptor_identity = os.fstat(descriptor)
        if (
            not stat.S_ISDIR(descriptor_identity.st_mode)
            or (descriptor_identity.st_dev, descriptor_identity.st_ino)
            != paths[1]
        ):
            raise BranchProvenanceError(
                "lock-guard descriptor is detached from its canonical parent"
            )
        guard = _LockNamespaceGuard(descriptor, *paths)
        if owner is not None:
            if owner.guard is not None:
                raise BranchProvenanceError(
                    "lock-guard ownership sink is already populated"
                )
            active_prior_mask = signal.pthread_sigmask(
                signal.SIG_BLOCK, managed_signals
            )
            owner.guard = guard
            transferred = True
            signal.pthread_sigmask(
                signal.SIG_SETMASK, active_prior_mask
            )
            active_prior_mask = None
        return guard
    except BaseException:
        if locked and not transferred:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
        if descriptor >= 0 and not transferred:
            try:
                os.close(descriptor)
            except OSError:
                pass
        raise
    finally:
        if active_prior_mask is not None:
            signal.pthread_sigmask(
                signal.SIG_SETMASK, active_prior_mask
            )


def _release_lock_namespace_guard(guard: _LockNamespaceGuard) -> None:
    managed_signals = {signal.SIGINT, signal.SIGTERM}
    prior_mask = signal.pthread_sigmask(signal.SIG_BLOCK, managed_signals)
    validation_error: BaseException | None = None
    try:
        try:
            current = _validate_lock_guard_paths(guard.operational_path)
            descriptor_identity = os.fstat(guard.descriptor)
            expected = (
                guard.anchor_path,
                guard.anchor_identity,
                guard.operational_path,
                guard.operational_identity,
                guard.locks_path,
                guard.locks_identity,
                guard.branch_path,
                guard.branch_identity,
            )
            if (
                current != expected
                or not stat.S_ISDIR(descriptor_identity.st_mode)
                or (descriptor_identity.st_dev, descriptor_identity.st_ino)
                != guard.anchor_identity
            ):
                raise BranchProvenanceError(
                    "lock-guard canonical directory identity changed"
                )
        except BaseException as error:
            validation_error = error
        try:
            fcntl.flock(guard.descriptor, fcntl.LOCK_UN)
        finally:
            os.close(guard.descriptor)
        if validation_error is not None:
            raise validation_error
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, prior_mask)


def _release_owned_lock_namespace_guard(
    owner: _LockNamespaceGuardOwner,
) -> None:
    prior_mask = signal.pthread_sigmask(
        signal.SIG_BLOCK, {signal.SIGINT, signal.SIGTERM}
    )
    try:
        guard = owner.guard
        if guard is None:
            return
        owner.guard = None
        _release_lock_namespace_guard(guard)
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, prior_mask)


def _scan_lock_namespace(
    lock_parent: Path, expected_generation_prefix: str
) -> None:
    if not lock_parent.exists() and not lock_parent.is_symlink():
        return
    _reject_symlink_components(lock_parent, "branch lock namespace")
    if lock_parent.is_symlink() or not lock_parent.is_dir():
        raise BranchProvenanceError("branch lock namespace is not a directory")
    for path in lock_parent.iterdir():
        match = re.fullmatch(
            r"(S(?:00[0-9]|0[1-4][0-9]|050))\.lock", path.name
        )
        if match is None:
            raise BranchProvenanceError(f"unexpected branch lock name: {path.name}")
        _payload, snapshot = _validated_lock_snapshot(
            path,
            context="branch cell lock",
            expected_precision_bits=int(lock_parent.name),
            expected_slab_id=match.group(1),
            expected_generation_prefix=expected_generation_prefix,
        )
        snapshot.verify_unchanged("branch cell lock")


def _scan_all_lock_namespaces(
    operational_root: Path,
    expected_generation_prefix: str,
    *,
    namespace_guarded: bool = False,
) -> None:
    branch_root = operational_root / "locks" / "branch"
    if not branch_root.exists() and not branch_root.is_symlink():
        return
    if not namespace_guarded:
        guard_owner = _LockNamespaceGuardOwner()
        try:
            _acquire_lock_namespace_guard(
                operational_root, owner=guard_owner
            )
            _scan_all_lock_namespaces(
                operational_root,
                expected_generation_prefix,
                namespace_guarded=True,
            )
            return
        finally:
            _release_owned_lock_namespace_guard(guard_owner)
    _reject_symlink_components(branch_root, "all branch locks")
    if branch_root.is_symlink() or not branch_root.is_dir():
        raise BranchProvenanceError("branch lock root is not a directory")
    for precision_entry in branch_root.iterdir():
        if precision_entry.name not in {"128", "256"}:
            raise BranchProvenanceError("unexpected branch lock precision namespace")
        _scan_lock_namespace(precision_entry, expected_generation_prefix)


def _scan_interrupted_lock_namespaces(
    operational_root: Path,
    expected_generation_prefix: str,
    *,
    namespace_guarded: bool = False,
) -> None:
    branch_root = operational_root / "interrupted" / "locks" / "branch"
    if not branch_root.exists() and not branch_root.is_symlink():
        return
    live_branch_root = operational_root / "locks" / "branch"
    if not namespace_guarded and live_branch_root.exists():
        guard_owner = _LockNamespaceGuardOwner()
        try:
            _acquire_lock_namespace_guard(
                operational_root, owner=guard_owner
            )
            _scan_interrupted_lock_namespaces(
                operational_root,
                expected_generation_prefix,
                namespace_guarded=True,
            )
            return
        finally:
            _release_owned_lock_namespace_guard(guard_owner)
    _reject_symlink_components(branch_root, "all interrupted branch locks")
    if branch_root.is_symlink() or not branch_root.is_dir():
        raise BranchProvenanceError("interrupted lock root is not a directory")
    for precision_entry in branch_root.iterdir():
        if precision_entry.name not in {"128", "256"}:
            raise BranchProvenanceError("unexpected interrupted lock precision")
        if precision_entry.is_symlink() or not precision_entry.is_dir():
            raise BranchProvenanceError("interrupted lock precision path is aliased")
        for entry in precision_entry.iterdir():
            match = INTERRUPTED_LOCK_NAME_PATTERN.fullmatch(entry.name)
            if match is None:
                raise BranchProvenanceError("unexpected interrupted branch lock name")
            snapshot = _snapshot_regular_file(
                entry, "interrupted branch lock", maximum_bytes=64 * 1024
            )
            payload = _strict_json_object_bytes(
                snapshot.payload, "interrupted branch lock"
            )
            if canonical_json_bytes(payload) != snapshot.payload:
                raise BranchProvenanceError(
                    "interrupted branch lock is not canonical JSON"
                )
            _validate_lock_payload(payload, entry)
            slab_id, attempt_text, generation_prefix, owner_token = match.groups()
            if (
                payload["precision_bits"] != int(precision_entry.name)
                or payload["slab_id"] != slab_id
                or payload["attempt"] != int(attempt_text)
                or payload["generation_prefix"] != generation_prefix
                or payload["owner_token"] != owner_token
                or payload["generation_prefix"] != expected_generation_prefix
            ):
                raise BranchProvenanceError(
                    "interrupted branch lock basename/payload mismatch"
                )
            snapshot.verify_unchanged("interrupted branch lock")


def _lock_payload(
    task: BranchCellTask,
    bindings: BranchBindings,
    attempt: int,
    owner_token: str,
) -> dict[str, Any]:
    start_time = _process_start_time(os.getpid())
    if start_time is None:
        raise BranchProvenanceError("cannot bind scheduler process start time")
    return {
        "artifact_role": "BRANCH_CELL_OPERATIONAL_LOCK",
        "attempt": attempt,
        "generation_prefix": bindings.run_config_sha256[:16],
        "owner_process_start_time": start_time,
        "owner_token": owner_token,
        "pid": os.getpid(),
        "precision_bits": task.precision_bits,
        "protocol_id": PROTOCOL_ID,
        "slab_id": task.slab_id,
    }


def _validate_lock_payload(payload: Mapping[str, Any], path: Path) -> None:
    expected_keys = {
        "artifact_role",
        "attempt",
        "generation_prefix",
        "owner_process_start_time",
        "owner_token",
        "pid",
        "precision_bits",
        "protocol_id",
        "slab_id",
    }
    if set(payload) != expected_keys:
        raise BranchProvenanceError(f"cell lock schema is not closed: {path}")
    if (
        payload.get("artifact_role") != "BRANCH_CELL_OPERATIONAL_LOCK"
        or payload.get("protocol_id") != PROTOCOL_ID
        or type(payload.get("attempt")) is not int
        or payload["attempt"] < 0
        or type(payload.get("pid")) is not int
        or payload["pid"] <= 0
        or type(payload.get("owner_process_start_time")) is not int
        or payload["owner_process_start_time"] <= 0
        or type(payload.get("precision_bits")) is not int
        or payload["precision_bits"] not in (128, 256)
        or type(payload.get("slab_id")) is not str
        or SLAB_PATTERN.fullmatch(payload["slab_id"]) is None
        or type(payload.get("generation_prefix")) is not str
        or re.fullmatch(r"[0-9a-f]{16}", payload["generation_prefix"]) is None
        or type(payload.get("owner_token")) is not str
        or re.fullmatch(r"[0-9a-f]{32}", payload["owner_token"]) is None
    ):
        raise BranchProvenanceError(f"cell lock value contract is malformed: {path}")


def _validated_lock_snapshot(
    path: Path,
    *,
    context: str,
    expected_precision_bits: int,
    expected_slab_id: str,
    expected_generation_prefix: str,
) -> tuple[dict[str, Any], RegularFileSnapshot]:
    snapshot = _snapshot_regular_file(path, context, maximum_bytes=64 * 1024)
    payload = _strict_json_object_bytes(snapshot.payload, context)
    if canonical_json_bytes(payload) != snapshot.payload:
        raise BranchProvenanceError(f"{context} is not canonical JSON")
    _validate_lock_payload(payload, path)
    if (
        payload["precision_bits"] != expected_precision_bits
        or payload["slab_id"] != expected_slab_id
        or payload["generation_prefix"] != expected_generation_prefix
    ):
        raise BranchProvenanceError(f"{context} identity/generation mismatch")
    return payload, snapshot


def _archive_stale_lock(
    lock_path: Path,
    operational_root: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    new_attempt: int,
) -> None:
    snapshot = _snapshot_regular_file(
        lock_path, "existing branch cell lock", maximum_bytes=64 * 1024
    )
    payload = _strict_json_object_bytes(
        snapshot.payload, "existing branch cell lock"
    )
    if canonical_json_bytes(payload) != snapshot.payload:
        raise BranchProvenanceError("existing branch lock is not canonical JSON")
    _validate_lock_payload(payload, lock_path)
    if (
        payload["precision_bits"] != task.precision_bits
        or payload["slab_id"] != task.slab_id
        or payload["generation_prefix"] != bindings.run_config_sha256[:16]
    ):
        raise BranchProvenanceError("existing branch lock identity/generation mismatch")
    live_start = _process_start_time(payload["pid"])
    if live_start == payload["owner_process_start_time"]:
        raise BranchAlreadyRunningError(
            f"live branch owner exists for {payload['precision_bits']}/{payload['slab_id']}"
        )
    if new_attempt <= payload["attempt"]:
        raise BranchContractError(
            "a recovered branch lock requires a strictly greater attempt"
        )
    interrupted_parent = (
        operational_root
        / "interrupted"
        / "locks"
        / "branch"
        / str(payload["precision_bits"])
    )
    interrupted_parent.mkdir(parents=True, exist_ok=True)
    _reject_symlink_components(interrupted_parent, "interrupted lock parent")
    if interrupted_parent.stat().st_dev != lock_path.parent.stat().st_dev:
        raise BranchProvenanceError("stale lock archive is not same-filesystem")
    _scan_interrupted_lock_namespaces(
        operational_root,
        bindings.run_config_sha256[:16],
        namespace_guarded=True,
    )
    destination = interrupted_parent / (
        f"{payload['slab_id']}.attempt-{payload['attempt']}.generation-"
        f"{payload['generation_prefix']}.owner-{payload['owner_token']}.lock"
    )
    snapshot.verify_unchanged("existing branch cell lock")
    try:
        _rename_noreplace(lock_path, destination)
    except FileExistsError as error:
        raise BranchProvenanceError("stale lock archive already exists") from error
    archived = _snapshot_regular_file(
        destination, "archived stale branch lock", maximum_bytes=64 * 1024
    )
    if (
        archived.payload != snapshot.payload
        or archived.fingerprint[:2] != snapshot.fingerprint[:2]
    ):
        raise BranchProvenanceError("stale lock changed during archive")
    archived.verify_unchanged("archived stale branch lock")
    _fsync_directory(lock_path.parent)
    _fsync_directory(interrupted_parent)


def _acquire_cell_lock(
    lock_path: Path,
    lock_parent: Path,
    operational_root: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    attempt: int,
    owner: _CellLockOwner,
) -> tuple[int, tuple[int, int], bytes]:
    generation_prefix = bindings.run_config_sha256[:16]
    guard_owner = _LockNamespaceGuardOwner()
    try:
        _acquire_lock_namespace_guard(
            operational_root, owner=guard_owner
        )
        _scan_all_lock_namespaces(
            operational_root,
            generation_prefix,
            namespace_guarded=True,
        )
        _scan_interrupted_lock_namespaces(
            operational_root,
            generation_prefix,
            namespace_guarded=True,
        )
        if lock_path.exists() or lock_path.is_symlink():
            _archive_stale_lock(
                lock_path, operational_root, task, bindings, attempt
            )
        owner_token = secrets.token_hex(16)
        payload = canonical_json_bytes(
            _lock_payload(task, bindings, attempt, owner_token)
        )
        temporary_path = lock_parent / (
            f".{task.slab_id}.lock.publish-{owner_token}"
        )
        try:
            descriptor = os.open(
                temporary_path,
                os.O_RDWR
                | os.O_CREAT
                | os.O_EXCL
                | getattr(os, "O_CLOEXEC", 0)
                | getattr(os, "O_NOFOLLOW", 0),
                0o600,
            )
        except OSError as error:
            raise BranchProvenanceError(
                "cannot create atomic branch lock publication inode"
            ) from error
        published = False
        transferred = False
        try:
            view = memoryview(payload)
            while view:
                written = os.write(descriptor, view)
                if written <= 0:
                    raise OSError("short lock write")
                view = view[written:]
            os.fsync(descriptor)
            metadata = os.fstat(descriptor)
            if metadata.st_nlink != 1 or not stat.S_ISREG(metadata.st_mode):
                raise BranchProvenanceError(
                    "branch lock publication inode is malformed"
                )
            try:
                _rename_noreplace(temporary_path, lock_path)
            except FileExistsError as error:
                raise BranchAlreadyRunningError(
                    f"branch owner raced admission for "
                    f"{task.precision_bits}/{task.slab_id}"
                ) from error
            published = True
            metadata = os.fstat(descriptor)
            descriptor_payload = os.pread(descriptor, len(payload) + 1, 0)
            canonical_payload, canonical_snapshot = _validated_lock_snapshot(
                lock_path,
                context="newly published branch cell lock",
                expected_precision_bits=task.precision_bits,
                expected_slab_id=task.slab_id,
                expected_generation_prefix=generation_prefix,
            )
            if (
                metadata.st_nlink != 1
                or not stat.S_ISREG(metadata.st_mode)
                or descriptor_payload != payload
                or canonical_snapshot.payload != payload
                or canonical_snapshot.fingerprint != _stat_fingerprint(metadata)
                or canonical_payload["attempt"] != attempt
                or canonical_payload["owner_token"] != owner_token
            ):
                raise BranchProvenanceError(
                    "published branch lock inode/payload binding is invalid"
                )
            canonical_snapshot.verify_unchanged(
                "newly published branch cell lock"
            )
            _fsync_directory(lock_parent)
            # Complete and validate the namespace-guard release while the
            # publication descriptor is still locally owned.  If canonical
            # directory replay fails, the exception is handled by the lock
            # cleanup state machine below rather than escaping after the
            # descriptor tuple has become unowned.
            _release_owned_lock_namespace_guard(guard_owner)
            if (
                owner.descriptor is not None
                or owner.identity is not None
                or owner.payload is not None
            ):
                raise BranchProvenanceError(
                    "cell-lock ownership sink is already populated"
                )
            handoff_mask = signal.pthread_sigmask(
                signal.SIG_BLOCK, {signal.SIGINT, signal.SIGTERM}
            )
            try:
                owner.descriptor = descriptor
                owner.identity = (metadata.st_dev, metadata.st_ino)
                owner.payload = payload
                transferred = True
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, handoff_mask)
            return descriptor, (metadata.st_dev, metadata.st_ino), payload
        except BaseException:
            if transferred:
                raise
            if not published:
                # `_rename_noreplace` may have completed the rename and then
                # been interrupted before the Python ownership flag was set.
                # Infer only the provable case: the canonical name is the
                # still-open publication inode with the exact payload.
                try:
                    lexical = os.stat(lock_path, follow_symlinks=False)
                    current = os.fstat(descriptor)
                    descriptor_payload = os.pread(
                        descriptor, len(payload) + 1, 0
                    )
                    published = (
                        stat.S_ISREG(lexical.st_mode)
                        and stat.S_ISREG(current.st_mode)
                        and (lexical.st_dev, lexical.st_ino)
                        == (current.st_dev, current.st_ino)
                        and descriptor_payload == payload
                    )
                except OSError:
                    published = False
            if published:
                # The no-replace publication established that this call
                # created the canonical name.  If a same-window substitution
                # was detected, remove that newly-created name while the
                # namespace guard is still held; never return a malformed
                # canonical lock to another scheduler.
                try:
                    os.unlink(lock_path)
                    _fsync_directory(lock_parent)
                except OSError:
                    pass
            else:
                try:
                    lexical = os.stat(temporary_path, follow_symlinks=False)
                    current = os.fstat(descriptor)
                    if (
                        stat.S_ISREG(lexical.st_mode)
                        and (lexical.st_dev, lexical.st_ino)
                        == (current.st_dev, current.st_ino)
                    ):
                        temporary_path.unlink()
                        _fsync_directory(lock_parent)
                except OSError:
                    pass
            os.close(descriptor)
            raise
    finally:
        _release_owned_lock_namespace_guard(guard_owner)


def _unlink_owned_cell_lock(
    descriptor: int,
    identity: tuple[int, int],
    payload: bytes,
    lock_path: Path,
    lock_parent: Path,
) -> None:
    descriptor_metadata = os.fstat(descriptor)
    try:
        lexical_metadata = os.stat(lock_path, follow_symlinks=False)
    except OSError as error:
        raise BranchProvenanceError(
            "branch lock ownership changed before release"
        ) from error
    descriptor_payload = b""
    offset = 0
    while len(descriptor_payload) <= len(payload):
        chunk = os.pread(
            descriptor,
            len(payload) + 1 - len(descriptor_payload),
            offset,
        )
        if not chunk:
            break
        descriptor_payload += chunk
        offset += len(chunk)
    if (
        not stat.S_ISREG(descriptor_metadata.st_mode)
        or not stat.S_ISREG(lexical_metadata.st_mode)
        or (descriptor_metadata.st_dev, descriptor_metadata.st_ino) != identity
        or (lexical_metadata.st_dev, lexical_metadata.st_ino) != identity
        or descriptor_metadata.st_nlink != 1
        or lexical_metadata.st_nlink != 1
        or descriptor_payload != payload
    ):
        raise BranchProvenanceError(
            "branch lock ownership changed before release"
        )
    lock_path.unlink()
    if os.fstat(descriptor).st_nlink != 0:
        raise BranchProvenanceError(
            "branch lock inode survived canonical release"
        )
    _fsync_directory(lock_parent)


def _release_cell_lock(
    descriptor: int,
    identity: tuple[int, int],
    payload: bytes,
    lock_path: Path,
    lock_parent: Path,
) -> None:
    operational_root = lock_parent.parents[2]
    guard_owner = _LockNamespaceGuardOwner()
    acquisition_error: BaseException | None = None
    try:
        try:
            _acquire_lock_namespace_guard(
                operational_root, owner=guard_owner
            )
        except BaseException as error:
            acquisition_error = error

        # Even if guard acquisition itself is interrupted, do not leave a live
        # lock whose PID/start-time continues to name this scheduler.  Shield
        # only this bounded ownership transition, never guard contention.
        cleanup_mask = signal.pthread_sigmask(
            signal.SIG_BLOCK, {signal.SIGINT, signal.SIGTERM}
        )
        try:
            _unlink_owned_cell_lock(
                descriptor, identity, payload, lock_path, lock_parent
            )
        finally:
            signal.pthread_sigmask(signal.SIG_SETMASK, cleanup_mask)
        if acquisition_error is not None:
            raise acquisition_error
    finally:
        try:
            _release_owned_lock_namespace_guard(guard_owner)
        finally:
            os.close(descriptor)


def _validate_staging_before_publish(staging: Path) -> None:
    _reject_symlink_components(staging, "branch staging transaction")
    if staging.is_symlink() or not staging.is_dir():
        raise BranchProvenanceError("branch staging transaction is not a directory")
    actual = {path.name for path in staging.iterdir()}
    if actual != {"stdout.txt", "stderr.txt", "record.json"}:
        raise BranchProvenanceError("branch staging transaction file set mismatch")
    for path in staging.iterdir():
        metadata = _require_regular_file(path, "branch staging object")
        if metadata.st_nlink != 1:
            raise BranchProvenanceError("hard-link alias in branch staging transaction")


def run_branch_cell_transaction(
    *,
    output_root: Path,
    operational_root: Path,
    task: BranchCellTask,
    bindings: BranchBindings,
    budgets: BranchBudgets = BranchBudgets(),
    attempt: int = 0,
) -> BranchTransactionResult:
    """Run and durably commit one future branch cell.

    Calling this function is a dispatch operation.  The module itself never
    calls it, exposes no command-line entry point, and has no production
    authorization bit.  Current tests pass only synthetic mock executables.
    """

    task.validate()
    bindings.validate()
    budgets.validate()
    if type(attempt) is not int or attempt < 0:
        raise BranchContractError("attempt must be an exact nonnegative integer")
    output_root = Path(output_root)
    operational_root = Path(operational_root)
    _require_absolute_lexical_path(str(output_root), "authoritative root")
    _require_absolute_lexical_path(str(operational_root), "operational root")
    if not output_root.is_absolute() or not operational_root.is_absolute():
        raise BranchContractError("result roots must be absolute")
    if output_root == operational_root:
        raise BranchContractError("authoritative and operational roots must differ")
    expected_operational = output_root.parent / f"{output_root.name}.operational"
    if operational_root != expected_operational:
        raise BranchContractError(
            "operational root must be the exact same-filesystem .operational sibling"
        )
    _reject_symlink_components(output_root, "authoritative root")
    _reject_symlink_components(operational_root, "operational root")
    source_pin, binary_pin = _pin_persistent_inputs(
        task, bindings, output_root, operational_root
    )
    lock_owner = _CellLockOwner()
    lock_parent: Path | None = None
    lock_path: Path | None = None
    try:
        cell, manifest_path, staging_parent, lock_parent, lock_path = _canonical_paths(
            output_root, operational_root, task
        )
        complete_cell_exists = cell.exists() or cell.is_symlink()
        manifest_exists = manifest_path.exists() or manifest_path.is_symlink()
        if complete_cell_exists and manifest_exists:
            _execution_pin, pin_failure = _verify_pins(source_pin, binary_pin)
            if pin_failure is not None:
                raise BranchProvenanceError(pin_failure)
            record, manifest = validate_committed_branch_cell(
                output_root, task, bindings, budgets
            )
            _resume_pin, resume_pin_failure = _verify_pins(
                source_pin, binary_pin
            )
            if resume_pin_failure is not None:
                raise BranchProvenanceError(resume_pin_failure)
            return BranchTransactionResult(record, manifest, True)
        if manifest_exists and not complete_cell_exists:
            raise BranchProvenanceError("branch manifest exists without its canonical cell")

        cell.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        staging_parent.mkdir(parents=True, exist_ok=True)
        lock_parent.mkdir(parents=True, exist_ok=True)
        for path, label in (
            (output_root, "authoritative root"),
            (operational_root, "operational root"),
            (cell.parent, "canonical cell parent"),
            (manifest_path.parent, "manifest parent"),
            (staging_parent, "staging parent"),
            (lock_parent, "lock parent"),
        ):
            _reject_symlink_components(path, label)
        device_ids = {
            cell.parent.stat().st_dev,
            manifest_path.parent.stat().st_dev,
            staging_parent.stat().st_dev,
            lock_parent.stat().st_dev,
        }
        if len(device_ids) != 1:
            raise BranchProvenanceError(
                "cell, manifest, staging, and lock parents are not same-filesystem"
            )

        generation_prefix = bindings.run_config_sha256[:16]
        _reject_retained_staging_before_admission(
            operational_root,
            task,
            generation_prefix,
        )
        _acquire_cell_lock(
            lock_path,
            lock_parent,
            operational_root,
            task,
            bindings,
            attempt,
            lock_owner,
        )

        # Recheck after acquiring ownership to close the admission race.
        complete_cell_exists = cell.exists() or cell.is_symlink()
        manifest_exists = manifest_path.exists() or manifest_path.is_symlink()
        if complete_cell_exists and not manifest_exists:
            _execution_pin, pin_failure = _verify_pins(source_pin, binary_pin)
            if pin_failure is not None:
                raise BranchProvenanceError(pin_failure)
            record, manifest = _recover_manifestless_commit(
                output_root, operational_root, task, bindings, budgets
            )
            _recovery_pin, recovery_pin_failure = _verify_pins(
                source_pin, binary_pin
            )
            if recovery_pin_failure is not None:
                raise BranchProvenanceError(recovery_pin_failure)
            return BranchTransactionResult(record, manifest, True)
        if complete_cell_exists or manifest_exists:
            raise BranchProvenanceError("cell appeared during branch admission")

        staging = staging_parent / (
            f".{task.slab_id}.tmp-{generation_prefix}-{attempt}"
        )
        lifecycle_guard_owner = _LockNamespaceGuardOwner()
        try:
            _acquire_lock_namespace_guard(
                operational_root, owner=lifecycle_guard_owner
            )
            # Lock publication, the post-lock namespace replay, and staging
            # creation share one guard.  Thus another cooperative scheduler
            # cannot expose a staging directory without the matching live
            # lock between our admission check and our own stage creation.
            _reject_retained_staging_before_admission(
                operational_root,
                task,
                generation_prefix,
            )
            try:
                staging.mkdir(mode=0o700)
            except FileExistsError as error:
                raise BranchProvenanceError(
                    "exact interrupted staging path already exists; choose a new attempt or quarantine"
                ) from error
            _fsync_directory(staging_parent)
        finally:
            _release_owned_lock_namespace_guard(lifecycle_guard_owner)

        stdout_stage = staging / "stdout.txt"
        stderr_stage = staging / "stderr.txt"
        outcome = run_bounded_process(
            task.argv(),
            stdout_stage,
            stderr_stage,
            budgets,
            executable_descriptor=binary_pin.descriptor,
        )
        stdout = stdout_stage.read_bytes()
        stderr = stderr_stage.read_bytes()
        execution_pin, pin_failure = _verify_pins(source_pin, binary_pin)
        stdout_relative = (
            cell / "stdout.txt"
        ).relative_to(output_root).as_posix()
        stderr_relative = (
            cell / "stderr.txt"
        ).relative_to(output_root).as_posix()
        _strict_relative(stdout_relative)
        _strict_relative(stderr_relative)
        record = _record_payload(
            task,
            bindings,
            budgets,
            outcome,
            stdout_relative,
            stderr_relative,
            stdout,
            stderr,
            execution_pin=execution_pin,
            provenance_failure_reason=pin_failure,
        )
        record_bytes = canonical_json_bytes(record)
        if len(record_bytes) >= budgets.record_bytes:
            raise BranchOutputRecordError(
                "closed branch record unexpectedly reaches the frozen record cap"
            )
        if len(stdout) + len(stderr) + len(record_bytes) >= budgets.total_cell_bytes:
            raise BranchOutputRecordError("committed cell would reach the total byte cap")
        _write_exclusive_fsync(staging / "record.json", record_bytes)
        _validate_staging_before_publish(staging)
        prepublish_pin, _prepublish_pin_failure = _verify_pins(
            source_pin, binary_pin
        )
        if canonical_json_bytes(prepublish_pin) != canonical_json_bytes(execution_pin):
            raise BranchProvenanceError("PIN_STATE_CHANGED_AFTER_RECORD")
        _fsync_directory(staging)
        try:
            _rename_noreplace(staging, cell)
        except FileExistsError as error:
            raise BranchProvenanceError(
                "concurrent canonical branch target already exists"
            ) from error
        _fsync_directory(staging_parent)
        _fsync_directory(cell.parent)
        postpublish_pin, _postpublish_pin_failure = _verify_pins(
            source_pin, binary_pin
        )
        if canonical_json_bytes(postpublish_pin) != canonical_json_bytes(execution_pin):
            raise BranchProvenanceError("PIN_STATE_CHANGED_DURING_PUBLICATION")

        _validated_record, file_role_map, _snapshots = (
            _validate_cell_without_manifest(
                output_root, cell, task, bindings, budgets
            )
        )
        manifest = _manifest_payload(
            output_root, cell, task, bindings, budgets, file_role_map
        )
        _publish_write_once(manifest_path, canonical_json_bytes(manifest))
        record, manifest = validate_committed_branch_cell(
            output_root, task, bindings, budgets
        )
        final_pin, _final_pin_failure = _verify_pins(source_pin, binary_pin)
        if canonical_json_bytes(final_pin) != canonical_json_bytes(execution_pin):
            raise BranchProvenanceError("PIN_STATE_CHANGED_DURING_COMMIT")
        return BranchTransactionResult(record, manifest, False)
    finally:
        try:
            if lock_owner.descriptor is not None:
                assert lock_owner.identity is not None
                assert lock_owner.payload is not None
                assert lock_path is not None
                assert lock_parent is not None
                _release_cell_lock(
                    lock_owner.descriptor,
                    lock_owner.identity,
                    lock_owner.payload,
                    lock_path,
                    lock_parent,
                )
        finally:
            binary_pin.close()
            source_pin.close()


__all__ = [
    "BranchAlreadyRunningError",
    "BranchBindings",
    "BranchBudgets",
    "BranchCellTask",
    "BranchContractError",
    "BranchOutputRecordError",
    "BranchProvenanceError",
    "BranchRuntimeError",
    "BranchTransactionResult",
    "EVALUATOR_STATUS_CODES",
    "PROTOCOL_ID",
    "SCHEDULER_CLASSIFICATIONS",
    "canonical_json_bytes",
    "parse_evaluator_abi",
    "run_bounded_process",
    "run_branch_cell_transaction",
    "sha256_file",
    "validate_committed_branch_cell",
]
