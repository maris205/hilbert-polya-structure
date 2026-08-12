#!/usr/bin/env python3
"""Independently replay the mock R401-VAL-L3-A1 branch archive.

This checker deliberately imports neither the scheduler nor the branch
runtime.  It reconstructs their published schemas, the exact 102-cell
matrix, the accepted L1 primary inputs, the evaluator transcript ABI, and
the branch-tube implication from independent code.  The currently executable
path accepts only ``MOCK_ONLY_NON_LICENSING`` archives.  Consequently a pass
is an implementation-replay result: component, milestone, theorem, and final
statuses all remain null.  A future scientific path must be added only after
an accepted main freeze.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import stat
import sys
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, localcontext
from fractions import Fraction
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve()
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_RELEASE_CHAIN = (L1_RELEASE, L1_SUMMARY, L1_MANIFEST, L1_CHECKER, L1_POSTCHECK)
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"
SCHEDULER_CONTRACT = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"
CHECKER_CONTRACT = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
RELEASE_CONTRACT = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
RUNTIME = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
SCHEDULER = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
EVALUATOR_SOURCE = ROOT / "validated/capd_r401_phase_branch_tube_mp_a1.cpp"
MOCK_EVALUATOR_SOURCE = ROOT / "scripts/mock_r401_val_l3_a1_branch_evaluator.py"

SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-A1"
CHECKER_ROLE = "BRANCH_INDEPENDENT_CHECKER"
POSTCHECK_ROLE = "BRANCH_POSTCHECK"
MOCK_ARTIFACT_STATUS = "MOCK_ONLY_NON_LICENSING"
MOCK_CHECKER_STATUS = "PASS_MOCK_INDEPENDENT_REPLAY"
MOCK_POSTCHECK_STATUS = "PASS_MOCK_WRITE_ONCE_POSTCHECK"
CELL_PASS_STATUS = "BRANCH_CELL_CERTIFIED"
SCHEDULER_PASS = "COMMITTED_EVALUATOR_RESULT"
SLABS = tuple(f"S{index:03d}" for index in range(51))
PRECISIONS = (128, 256)
PHASE_GRID = 64
TAYLOR_ORDER = 24
TUBE_RADIUS_SQ = Fraction(1, 625)
CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
NUMBER_RE = re.compile(rf"{NUMBER}\Z")
INTERVAL_RE = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")

CELL_CLAIM_BOUNDARY = (
    "accepted-branch complete-period tube cell only; no arbitrary-candidate "
    "tube routing, global uniqueness, trace, Hilbert--Polya, zeta, or RH claim"
)
MOCK_CLAIM_BOUNDARY = (
    "mock-only all-slab branch archive replay for transaction, transcript, "
    "tube-implication, aggregate, and cross-precision engineering; no "
    "component, local theorem, global orbit, trace-formula, Hilbert--Polya, "
    "zeta-zero, or RH authority"
)
MOCK_POSTCHECK_CLAIM_BOUNDARY = (
    "write-once replay of the mock branch checker and aggregate chain only; "
    "no scientific component, theorem, trace, Hilbert--Polya, zeta, or RH authority"
)
PRODUCER_MOCK_CLAIM_BOUNDARY = (
    "synthetic static/branch scheduler transaction only; no Arb/CAPD "
    "scientific evaluation, no component or local theorem, no global "
    "routing, trace, Hilbert-Polya, zeta-zero, or RH claim"
)
MOCK_TRANSCRIPT_CLAIM_BOUNDARY = (
    "synthetic branch ABI replay only; no scientific proof"
)

L1_SUMMARY_KEYS = {
    "bridge_job_count", "claim_boundary", "cross_precision_gates", "environment",
    "final_status", "hash_gates", "job_count_per_precision", "milestone_status",
    "plan_gates", "precision_gates", "primary_job_count", "protocol_id",
    "records", "requested_precisions",
}
L1_MANIFEST_KEYS = {"capd_commit", "files", "final_status", "milestone_status", "protocol_id"}
L1_CHECKER_KEYS = {
    "aggregate_check_count", "arithmetic_replay_count", "checker_status",
    "final_status", "frozen_hash_gates", "global_gates", "job_failures",
    "manifest_file_count", "manifest_hash_failures", "milestone_status",
    "plan_gates", "protocol_id", "scope",
}
L1_POSTCHECK_KEYS = {"checker_status", "files", "final_status", "milestone_status", "protocol_id"}
L1_RELEASE_KEYS = {"files", "final_status", "protocol_id", "release_status", "scope"}
L1_POSTCHECK_FILES = {
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/summary.json",
    "scripts/check_r401_val_l1_independent.py",
}
L1_RELEASE_FILES = {
    "research/route_a_wave_trace/A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md",
    "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    "research/route_a_wave_trace/R401_VAL_L1_PROTOCOL_V2.md",
    "research/route_a_wave_trace/R401_VAL_L1_V2_FREEZE.md",
    "results/R401_VAL_INVALIDATION_REGISTRY.json",
    "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/summary.json",
    "scripts/check_r401_val_l1_independent.py",
    "scripts/run_r401_val_l1_branch.py",
    "validated/capd_r401_local_slab_grid_mp.cpp",
}
L1_SUMMARY_BOUNDARY = (
    "one primitive full-return branch, unique only inside the frozen local primary "
    "boxes and bridge hulls, for every epsilon in [0,0.101]; no root-complement, "
    "global phase-space cover, delta_tr, Hilbert-Polya, or RH claim"
)


class BranchCheckError(RuntimeError):
    pass


class FormalBranchAuthorityError(BranchCheckError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BranchCheckError(message)


def exact_keys(payload: Mapping[str, Any], expected: set[str], context: str) -> None:
    require(type(payload) is dict, f"{context}: expected an exact JSON object")
    actual = set(payload)
    require(
        actual == expected,
        f"{context}: keys differ; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}",
    )


def exact_int(value: Any, context: str, *, expected: int | None = None, minimum: int | None = None) -> int:
    require(type(value) is int, f"{context}: expected an exact JSON integer")
    if expected is not None:
        require(value == expected, f"{context}: expected {expected}, got {value}")
    if minimum is not None:
        require(value >= minimum, f"{context}: below minimum {minimum}")
    return value


def exact_bool(value: Any, expected: bool, context: str) -> None:
    require(type(value) is bool and value is expected, f"{context}: Boolean mismatch")


def json_exact_equal(actual: Any, expected: Any) -> bool:
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, dict):
        return set(actual) == set(expected) and all(
            json_exact_equal(actual[key], expected[key]) for key in expected
        )
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(
            json_exact_equal(left, right)
            for left, right in zip(actual, expected, strict=True)
        )
    return bool(actual == expected)


def require_json_exact(actual: Any, expected: Any, context: str) -> None:
    require(json_exact_equal(actual, expected), f"{context}: exact JSON mismatch")


def canonical_json_bytes(payload: Any) -> bytes:
    _require_plain_runtime_json(payload, context="$compact")
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


def _require_plain_runtime_json(
    value: Any,
    context: str = "$",
    ancestors: set[int] | None = None,
) -> None:
    """Reject non-plain Python values before branch-byte serialization."""

    if value is None or type(value) in (str, bool, int):
        return
    if type(value) is float:
        require(math.isfinite(value), f"nonfinite runtime JSON number at {context}")
        return
    if type(value) not in (dict, list):
        raise BranchCheckError(
            f"non-plain runtime JSON value at {context}: {type(value).__name__}"
        )
    active = ancestors if ancestors is not None else set()
    identity = id(value)
    if identity in active:
        raise BranchCheckError(f"cyclic runtime JSON container at {context}")
    active.add(identity)
    try:
        if type(value) is dict:
            for key, item in value.items():
                if type(key) is not str:
                    raise BranchCheckError(
                        f"non-string runtime JSON object key at {context}: "
                        f"{type(key).__name__}"
                    )
                _require_plain_runtime_json(item, f"{context}.{key}", active)
        else:
            for index, item in enumerate(value):
                _require_plain_runtime_json(item, f"{context}[{index}]", active)
    finally:
        active.remove(identity)


def runtime_json_bytes(payload: Any) -> bytes:
    _require_plain_runtime_json(payload)
    return (
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def require_sha256(value: Any, context: str) -> str:
    require(type(value) is str and HEX64.fullmatch(value) is not None, f"{context}: invalid SHA-256")
    return value


def matrix_payload() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": slab_id}
        for bits in PRECISIONS
        for slab_id in SLABS
    ]


def canonical_matrix_id() -> str:
    return sha256_bytes(canonical_json_bytes(matrix_payload()))


def reject_symlink_components(path: Path, context: str) -> None:
    require(path.is_absolute(), f"{context}: path is not absolute")
    cursor = Path(path.anchor)
    seen: set[tuple[int, int]] = set()
    try:
        root_stat = os.lstat(cursor)
        seen.add((root_stat.st_dev, root_stat.st_ino))
    except OSError as error:
        raise BranchCheckError(f"{context}: cannot inspect filesystem root") from error
    for part in path.parts[1:]:
        cursor = cursor / part
        try:
            metadata = os.lstat(cursor)
        except FileNotFoundError:
            break
        require(not stat.S_ISLNK(metadata.st_mode), f"{context}: symlink component {cursor}")
        if cursor != path:
            require(stat.S_ISDIR(metadata.st_mode), f"{context}: nondirectory ancestor {cursor}")
            identity = (metadata.st_dev, metadata.st_ino)
            require(identity not in seen, f"{context}: ancestor inode alias {cursor}")
            seen.add(identity)


def canonical_absolute_path(value: str | os.PathLike[str], context: str) -> Path:
    raw = os.fspath(value)
    require(
        type(raw) is str
        and raw.startswith("/")
        and not raw.startswith("//")
        and "\x00" not in raw
        and "\\" not in raw
        and "//" not in raw[1:]
        and not raw.endswith("/")
        and all(part not in ("", ".", "..") for part in raw[1:].split("/")),
        f"{context}: noncanonical absolute path",
    )
    path = Path(raw)
    require(path.as_posix() == raw, f"{context}: path spelling alias")
    reject_symlink_components(path, context)
    return path


def canonical_relative_path(value: Any, context: str) -> PurePosixPath:
    require(type(value) is str and value and "\x00" not in value and "\\" not in value, f"{context}: malformed relative path")
    path = PurePosixPath(value)
    require(
        not path.is_absolute()
        and path.as_posix() == value
        and "//" not in value
        and not value.endswith("/")
        and all(part not in ("", ".", "..") and not part.startswith(".") for part in path.parts),
        f"{context}: noncanonical relative path",
    )
    return path


@dataclass(frozen=True)
class CapturedFile:
    path: Path
    raw: bytes
    fingerprint: tuple[int, ...]

    @property
    def sha256(self) -> str:
        return sha256_bytes(self.raw)

    @property
    def size(self) -> int:
        return len(self.raw)

    def verify_unchanged(self, context: str) -> None:
        # Metadata alone is not a sufficient replay gate: a same-size rewrite
        # can be timestamp-indistinguishable on a coarse or virtual
        # filesystem.  Reopen through the same no-follow pinned reader and
        # compare both inode metadata and the complete byte image.
        current = capture_file(self.path, f"{context} current image")
        require(
            current.fingerprint == self.fingerprint and current.raw == self.raw,
            f"{context}: file changed after capture",
        )


def _fingerprint(metadata: os.stat_result) -> tuple[int, ...]:
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


def capture_file(path: Path, context: str, *, maximum_bytes: int | None = None) -> CapturedFile:
    reject_symlink_components(path, context)
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise BranchCheckError(f"{context}: cannot open {path}") from error
    try:
        before = os.fstat(descriptor)
        lexical = os.stat(path, follow_symlinks=False)
        fingerprint = _fingerprint(before)
        require(stat.S_ISREG(before.st_mode), f"{context}: not a regular file")
        require(before.st_nlink == 1 and lexical.st_nlink == 1, f"{context}: hard-link alias")
        require(_fingerprint(lexical) == fingerprint, f"{context}: path/inode mismatch")
        if maximum_bytes is not None:
            require(before.st_size <= maximum_bytes, f"{context}: exceeds byte cap")
        chunks: list[bytes] = []
        offset = 0
        while True:
            chunk = os.pread(descriptor, 1024 * 1024, offset)
            if not chunk:
                break
            chunks.append(chunk)
            offset += len(chunk)
            if maximum_bytes is not None:
                require(offset <= maximum_bytes, f"{context}: exceeds byte cap")
        raw = b"".join(chunks)
        after = os.fstat(descriptor)
        lexical_after = os.stat(path, follow_symlinks=False)
        require(len(raw) == before.st_size, f"{context}: short captured read")
        require(_fingerprint(after) == fingerprint and _fingerprint(lexical_after) == fingerprint, f"{context}: mutation during capture")
        return CapturedFile(path, raw, fingerprint)
    finally:
        os.close(descriptor)


def sha256_file(path: Path) -> str:
    return capture_file(path, "hash input").sha256


def strict_json_from_bytes(raw: bytes, context: str) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        answer: dict[str, Any] = {}
        for key, value in pairs:
            require(key not in answer, f"{context}: duplicate JSON key {key!r}")
            answer[key] = value
        return answer

    def reject_constant(value: str) -> None:
        raise BranchCheckError(f"{context}: forbidden nonfinite constant {value}")

    try:
        payload = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
    except BranchCheckError:
        raise
    except Exception as error:
        raise BranchCheckError(f"{context}: invalid JSON") from error
    require(type(payload) is dict, f"{context}: top-level object required")

    def finite(value: Any) -> None:
        if type(value) is float:
            require(math.isfinite(value), f"{context}: nonfinite JSON float")
        elif type(value) is list:
            for item in value:
                finite(item)
        elif type(value) is dict:
            for item in value.values():
                finite(item)

    finite(payload)
    return payload


def load_json(path: Path, context: str, *, canonical: str | None = None, maximum_bytes: int | None = None) -> tuple[dict[str, Any], CapturedFile]:
    image = capture_file(path, context, maximum_bytes=maximum_bytes)
    payload = strict_json_from_bytes(image.raw, context)
    if canonical == "compact":
        require(image.raw == canonical_json_bytes(payload), f"{context}: noncanonical compact JSON")
    elif canonical == "runtime":
        require(image.raw == runtime_json_bytes(payload), f"{context}: noncanonical runtime JSON")
    image.verify_unchanged(context)
    return payload, image


def project_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate_bound_hash_map(payload: Any, expected: set[str], captured: Mapping[str, str], context: str) -> None:
    exact_keys(payload, expected, context)
    for role in sorted(expected):
        require_sha256(payload[role], f"{context}.{role}")
        actual = captured.get(role)
        if actual is None:
            role_path = ROOT / Path(*canonical_relative_path(role, context).parts)
            actual = sha256_file(role_path)
        require(payload[role] == actual, f"{context}: hash mismatch for {role}")


@dataclass(frozen=True)
class L1Bundle:
    plan: dict[str, dict[str, Any]]
    primary: dict[tuple[int, str], dict[str, Any]]
    primary_hashes: dict[tuple[int, str], str]
    chain_hashes: dict[str, str]
    plan_sha256: str
    snapshots: tuple[CapturedFile, ...]


def load_l1_bundle() -> L1Bundle:
    images = {path: load_json(path, f"accepted L1 {path.name}") for path in L1_RELEASE_CHAIN}
    plan_payload, plan_image = load_json(PLAN, "accepted L1 final plan")
    summary, summary_image = images[L1_SUMMARY]
    manifest, _ = images[L1_MANIFEST]
    checker, _ = images[L1_CHECKER]
    postcheck, _ = images[L1_POSTCHECK]
    release, _ = images[L1_RELEASE]
    captured = {project_relative(path): image.sha256 for path, (_, image) in images.items()}
    captured[project_relative(PLAN)] = plan_image.sha256
    exact_keys(summary, L1_SUMMARY_KEYS, "accepted L1 summary")
    exact_keys(manifest, L1_MANIFEST_KEYS, "accepted L1 manifest")
    exact_keys(checker, L1_CHECKER_KEYS, "accepted L1 checker")
    exact_keys(postcheck, L1_POSTCHECK_KEYS, "accepted L1 postcheck")
    exact_keys(release, L1_RELEASE_KEYS, "accepted L1 release")
    require(
        summary.get("protocol_id") == "R401-VAL-L1-V2"
        and summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and summary.get("final_status") is None
        and summary.get("claim_boundary") == L1_SUMMARY_BOUNDARY,
        "accepted L1 summary status gate",
    )
    require(
        manifest.get("protocol_id") == "R401-VAL-L1-V2"
        and manifest.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and manifest.get("final_status") is None
        and manifest.get("capd_commit") == CAPD_COMMIT,
        "accepted L1 manifest status gate",
    )
    require(
        checker.get("protocol_id") == "R401-VAL-L1-V2"
        and checker.get("checker_status") == "PASS"
        and checker.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and checker.get("final_status") is None
        and checker.get("job_failures") == []
        and checker.get("manifest_hash_failures") == [],
        "accepted L1 checker status gate",
    )
    require(
        postcheck.get("protocol_id") == "R401-VAL-L1-V2"
        and postcheck.get("checker_status") == "PASS"
        and postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and postcheck.get("final_status") is None,
        "accepted L1 postcheck status gate",
    )
    require(
        release.get("protocol_id") == "R401-VAL-L1-V2"
        and release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and release.get("final_status") is None,
        "accepted L1 release status gate",
    )
    files = manifest.get("files")
    require(type(files) is dict and len(files) == 417, "accepted L1 manifest exact file count")
    require(files.get(project_relative(PLAN)) == plan_image.sha256, "accepted L1 plan binding")
    validate_bound_hash_map(postcheck.get("files"), L1_POSTCHECK_FILES, captured, "accepted L1 postcheck files")
    validate_bound_hash_map(release.get("files"), L1_RELEASE_FILES, captured, "accepted L1 release files")

    exact_keys(
        plan_payload,
        {"all_floating_residuals_lt_1e-9", "bridge_count", "bridge_hull_padding", "bridges", "claim_boundary", "coverage", "milestone_id", "minimum_positive_overlap", "protocol_id", "slab_count", "slabs"},
        "accepted L1 plan",
    )
    require(plan_payload.get("protocol_id") == "R401-VAL-V2", "accepted L1 plan protocol")
    slabs = plan_payload.get("slabs")
    require(type(slabs) is list and len(slabs) == 51, "accepted L1 plan slab count")
    plan: dict[str, dict[str, Any]] = {}
    for expected_slab, record in zip(SLABS, slabs, strict=True):
        require(type(record) is dict and record.get("slab_id") == expected_slab, "accepted L1 plan slab order")
        exact_keys(record, {"center", "epsilon_lower", "epsilon_upper", "floating_residual_inf", "root_radii", "slab_id"}, f"plan {expected_slab}")
        exact_keys(record["center"], {"p_slow", "period", "q_fast", "q_slow"}, f"plan {expected_slab}.center")
        exact_keys(record["root_radii"], {"p_slow", "period", "q_fast", "q_slow"}, f"plan {expected_slab}.root_radii")
        plan[expected_slab] = record

    records = summary.get("records")
    require(type(records) is list and len(records) == 202, "accepted L1 summary record count")
    primary: dict[tuple[int, str], dict[str, Any]] = {}
    primary_hashes: dict[tuple[int, str], str] = {}
    for record in records:
        require(type(record) is dict, "accepted L1 record is not object")
        if record.get("job_type") != "primary":
            continue
        pair = (record.get("precision_bits"), record.get("job_id"))
        require(pair[0] in PRECISIONS and pair[1] in SLABS and pair not in primary, "accepted L1 primary identity")
        require(record.get("status") == "PASS_LOCAL_SLAB" and record.get("passed") is True, f"accepted L1 primary pass {pair}")
        plan_record = plan[pair[1]]
        command = record.get("command_arguments")
        expected_command = [
            str(pair[0]),
            plan_record["epsilon_lower"],
            plan_record["epsilon_upper"],
            plan_record["center"]["q_slow"],
            plan_record["center"]["q_fast"],
            plan_record["center"]["p_slow"],
            plan_record["center"]["period"],
            plan_record["root_radii"]["q_slow"],
            plan_record["root_radii"]["q_fast"],
            plan_record["root_radii"]["p_slow"],
            plan_record["root_radii"]["period"],
        ]
        require_json_exact(command, expected_command, f"accepted L1 primary command {pair}")
        primary[pair] = record
        primary_hashes[pair] = sha256_bytes(canonical_json_bytes(record))
    require(set(primary) == {(bits, slab) for bits in PRECISIONS for slab in SLABS}, "accepted L1 primary matrix incomplete")
    return L1Bundle(
        plan=plan,
        primary=primary,
        primary_hashes=primary_hashes,
        chain_hashes={project_relative(path): image.sha256 for path, (_, image) in images.items()},
        plan_sha256=plan_image.sha256,
        snapshots=tuple(image for _, image in images.values()) + (plan_image,),
    )


def canonical_decimal_token(value: Decimal | str) -> str:
    try:
        parsed = value if isinstance(value, Decimal) else Decimal(value)
    except (InvalidOperation, ValueError, TypeError) as error:
        raise BranchCheckError(f"invalid exact decimal token {value!r}") from error
    require(parsed.is_finite(), "nonfinite exact decimal token")
    text = format(parsed, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in {"", "-0", "+0"} else text


@dataclass(frozen=True)
class ExpectedTask:
    precision_bits: int
    slab_id: str
    epsilon: tuple[str, str]
    root_box: tuple[tuple[str, str], ...]
    evaluator_binary_path: str
    accepted_l1_primary_record_id: str
    accepted_l1_primary_record_sha256: str

    @property
    def tolerance(self) -> str:
        return "1e-30" if self.precision_bits == 128 else "1e-60"

    def argv(self) -> list[str]:
        return [
            self.evaluator_binary_path,
            str(self.precision_bits),
            self.epsilon[0],
            self.epsilon[1],
            *(token for pair in self.root_box for token in pair),
        ]

    def payload(self) -> dict[str, Any]:
        return {
            "accepted_l1_primary_record_id": self.accepted_l1_primary_record_id,
            "accepted_l1_primary_record_sha256": self.accepted_l1_primary_record_sha256,
            "epsilon": list(self.epsilon),
            "phase_grid": PHASE_GRID,
            "precision_bits": self.precision_bits,
            "root_box": [list(pair) for pair in self.root_box],
            "slab_id": self.slab_id,
            "taylor_order": TAYLOR_ORDER,
            "tolerance": self.tolerance,
            "tube_radius_sq": "1/625",
        }


def expected_root_box(plan_record: Mapping[str, Any]) -> tuple[tuple[str, str], ...]:
    center = plan_record["center"]
    radii = plan_record["root_radii"]
    result: list[tuple[str, str]] = []
    for name in ("q_slow", "q_fast", "p_slow", "period"):
        require(type(center[name]) is str and type(radii[name]) is str, f"plan {name}: lexical decimal")
        try:
            midpoint = Decimal(center[name])
            radius = Decimal(radii[name])
        except InvalidOperation as error:
            raise BranchCheckError(f"plan {name}: invalid decimal") from error
        require(midpoint.is_finite() and radius.is_finite() and radius > 0, f"plan {name}: invalid domain")
        with localcontext() as decimal_context:
            decimal_context.prec = 256
            result.append(
                (
                    canonical_decimal_token(midpoint - radius),
                    canonical_decimal_token(midpoint + radius),
                )
            )
    return tuple(result)


def expected_tasks(bundle: L1Bundle, evaluator_path: str) -> tuple[ExpectedTask, ...]:
    canonical_absolute_path(evaluator_path, "mock evaluator")
    tasks: list[ExpectedTask] = []
    for bits in PRECISIONS:
        for slab_id in SLABS:
            plan = bundle.plan[slab_id]
            task = ExpectedTask(
                precision_bits=bits,
                slab_id=slab_id,
                epsilon=(plan["epsilon_lower"], plan["epsilon_upper"]),
                root_box=expected_root_box(plan),
                evaluator_binary_path=evaluator_path,
                accepted_l1_primary_record_id=f"{bits}/{slab_id}/primary",
                accepted_l1_primary_record_sha256=bundle.primary_hashes[(bits, slab_id)],
            )
            require(len(task.argv()) == 12, f"task {bits}:{slab_id}: argv cardinality")
            tasks.append(task)
    for index, slab_id in enumerate(SLABS):
        left, right = tasks[index], tasks[51 + index]
        require(left.epsilon == right.epsilon and left.root_box == right.root_box, f"task {slab_id}: cross-precision exact domain")
    return tuple(tasks)


RUN_CONFIG_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "production_authorized",
    "scientific_licensing_enabled", "matrix", "matrix_id", "scheduler_policy",
    "limits", "paths", "main_freeze", "machine_freeze", "prefreeze_review",
    "source_bindings", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
PRODUCER_SOURCE_PATHS = {
    project_relative(SCHEDULER),
    project_relative(PLAN),
    project_relative(RUNTIME),
    project_relative(MOCK_EVALUATOR_SOURCE),
    project_relative(PROTOCOL),
    project_relative(SCHEDULER_CONTRACT),
    project_relative(CHECKER_CONTRACT),
    project_relative(RELEASE_CONTRACT),
}


@dataclass(frozen=True)
class MockRunContext:
    input_dir: Path
    operational_dir: Path
    run_config: dict[str, Any]
    run_config_image: CapturedFile
    branch_limits: dict[str, Any]
    producer_source_bindings: dict[str, str]


def validate_mock_run_config(input_dir: Path) -> MockRunContext:
    input_dir = canonical_absolute_path(str(input_dir), "branch checker input directory")
    require(input_dir.is_dir() and not input_dir.is_symlink(), "branch checker input directory absent")
    run_config, image = load_json(input_dir / "run_config.json", "mock run config", canonical="compact")
    exact_keys(run_config, RUN_CONFIG_KEYS, "mock run config")
    exact_int(run_config["schema_version"], "mock run config.schema_version", expected=SCHEMA_VERSION)
    require(run_config["protocol_id"] == PROTOCOL_ID and run_config["artifact_role"] == "RUN_CONFIG", "mock run config identity")
    if run_config["artifact_status"] != MOCK_ARTIFACT_STATUS:
        raise FormalBranchAuthorityError(
            "this executable accepts only MOCK_ONLY_NON_LICENSING archives; "
            "the formal branch aggregate path remains fail-closed"
        )
    require(run_config["authority"] == "PRODUCER_ONLY", "mock run config authority")
    exact_bool(run_config["mock_only"], True, "mock run config.mock_only")
    exact_bool(run_config["production_authorized"], False, "mock run config.production_authorized")
    exact_bool(run_config["scientific_licensing_enabled"], False, "mock run config.scientific_licensing_enabled")
    require_json_exact(run_config["matrix"], matrix_payload(), "mock run config.matrix")
    require(run_config["matrix_id"] == canonical_matrix_id(), "mock run config.matrix_id")
    require(run_config["scheduler_policy"] == "deterministic_component_barrier_batches_v1", "mock run config.scheduler policy")
    require_json_exact(run_config["main_freeze"], {"path": None, "sha256": None}, "mock run config.main_freeze")
    require_json_exact(run_config["machine_freeze"], {"path": None, "sha256": None}, "mock run config.machine_freeze")
    require_json_exact(run_config["prefreeze_review"], {"path": None, "sha256": None, "accepted": False}, "mock run config.prefreeze_review")
    require(run_config["claim_boundary"] == PRODUCER_MOCK_CLAIM_BOUNDARY, "mock run config claim boundary")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(run_config[key] is None, f"mock run config unauthorized {key}")
    exact_keys(run_config["paths"], {"authoritative_root", "operational_root"}, "mock run config.paths")
    require(run_config["paths"]["authoritative_root"] == str(input_dir), "mock run config authoritative path")
    operational = input_dir.parent / f"{input_dir.name}.operational"
    require(run_config["paths"]["operational_root"] == str(operational), "mock run config operational path")
    reject_symlink_components(operational, "mock operational root")

    source_bindings = run_config["source_bindings"]
    exact_keys(source_bindings, PRODUCER_SOURCE_PATHS, "mock producer source bindings")
    for relative in PRODUCER_SOURCE_PATHS:
        require_sha256(source_bindings[relative], f"mock producer source {relative}")
        require(source_bindings[relative] == sha256_file(ROOT / Path(*PurePosixPath(relative).parts)), f"mock producer source hash {relative}")

    limits = run_config["limits"]
    exact_keys(limits, {"branch", "global_scientific_budget", "max_inflight_per_component_cell", "static"}, "mock run config.limits")
    require(limits["global_scientific_budget"] is None, "mock global scientific budget")
    exact_int(limits["max_inflight_per_component_cell"], "mock max inflight", expected=1)
    branch = limits["branch"]
    exact_keys(branch, {"record_bytes", "stderr_bytes", "stdout_bytes", "timeout_seconds", "total_cell_bytes", "workers"}, "mock branch limits")
    for key, expected in {
        "record_bytes": 4 * 1024 * 1024,
        "stderr_bytes": 1024 * 1024,
        "stdout_bytes": 16 * 1024 * 1024,
        "timeout_seconds": 600,
        "total_cell_bytes": 32 * 1024 * 1024,
        "workers": 6,
    }.items():
        exact_int(branch[key], f"mock branch limits.{key}", expected=expected)
    return MockRunContext(
        input_dir=input_dir,
        operational_dir=operational,
        run_config=run_config,
        run_config_image=image,
        branch_limits=dict(branch),
        producer_source_bindings=dict(source_bindings),
    )


Interval = tuple[Fraction, Fraction]


def parse_number(value: str, context: str) -> Fraction:
    require(type(value) is str and len(value) <= 512 and NUMBER_RE.fullmatch(value) is not None, f"{context}: noncanonical decimal")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise BranchCheckError(f"{context}: invalid rational decimal") from error


def parse_interval(value: str, context: str) -> Interval:
    match = INTERVAL_RE.fullmatch(value)
    require(match is not None, f"{context}: exact CAPD interval required")
    lower, upper = parse_number(match.group(1), context), parse_number(match.group(2), context)
    require(lower <= upper, f"{context}: reversed interval")
    return lower, upper


def parse_vector(value: str, count: int, context: str) -> list[Interval]:
    require(type(value) is str, f"{context}: vector is not text")
    matches = list(INTERVAL_RE.finditer(value))
    require(len(matches) == count, f"{context}: expected {count} intervals")
    residual = INTERVAL_RE.sub("I", value)
    residual = re.sub(r"\s+", "", residual)
    require(residual == "{" + ",".join("I" for _ in range(count)) + "}", f"{context}: vector grammar")
    result: list[Interval] = []
    for match in matches:
        lower = parse_number(match.group(1), context)
        upper = parse_number(match.group(2), context)
        require(lower <= upper, f"{context}: reversed vector interval")
        result.append((lower, upper))
    return result


def parse_scalar_or_point_interval(value: str, context: str) -> Fraction:
    if NUMBER_RE.fullmatch(value) is not None:
        return parse_number(value, context)
    interval = parse_interval(value, context)
    require(interval[0] == interval[1], f"{context}: non-point domain endpoint")
    return interval[0]


def interval_add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def interval_sub(left: Interval, right: Interval) -> Interval:
    return left[0] - right[1], left[1] - right[0]


def interval_mul(left: Interval, right: Interval) -> Interval:
    products = (left[0] * right[0], left[0] * right[1], left[1] * right[0], left[1] * right[1])
    return min(products), max(products)


def interval_square(value: Interval) -> Interval:
    lower, upper = value
    if lower >= 0:
        return lower * lower, upper * upper
    if upper <= 0:
        return upper * upper, lower * lower
    return Fraction(0), max(lower * lower, upper * upper)


def overlaps(left: Interval, right: Interval) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def contains_exact(outer: Interval, inner: tuple[str, str]) -> bool:
    return outer[0] <= parse_number(inner[0], "exact input lower") and parse_number(inner[1], "exact input upper") <= outer[1]


def arb_fraction_endpoint(value: arb, lower: bool) -> Fraction:
    endpoint = value.lower() if lower else value.upper()
    rational = endpoint.fmpq()
    return Fraction(int(rational.p), int(rational.q))


def independent_omega_slow(bits: int) -> Interval:
    previous = ctx.prec
    try:
        ctx.prec = bits
        a = arb(51) / 50
        c = 2 * ((1 + a).sqrt() - 1)
        discriminant = c * (c * c + 4).sqrt()
        lambda_slow = (c * c + 2 - discriminant) / 2
        omega = 2 * arb.pi() * lambda_slow.sqrt()
        return arb_fraction_endpoint(omega, True), arb_fraction_endpoint(omega, False)
    finally:
        ctx.prec = previous


def transcript_fields(raw: bytes, context: str) -> dict[str, str]:
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise BranchCheckError(f"{context}: non-UTF8 transcript") from error
    require(text.endswith("\n"), f"{context}: transcript lacks final LF")
    fields: dict[str, str] = {}
    for line in text.splitlines():
        require(line and "=" in line, f"{context}: malformed transcript line")
        key, value = line.split("=", 1)
        require(re.fullmatch(r"[a-z][a-z0-9_]*", key) is not None, f"{context}: malformed field name {key!r}")
        require(key not in fields, f"{context}: duplicate field {key}")
        fields[key] = value
    return fields


@dataclass(frozen=True)
class TranscriptReplay:
    maximum_rslow_sq_upper: Fraction
    minimum_margin_sq_lower: Fraction
    phase_checks: int
    input_domain: tuple[tuple[str, str], tuple[tuple[str, str], ...]]
    evaluator_status: str


def replay_transcript(raw: bytes, task: ExpectedTask, context: str) -> TranscriptReplay:
    fields = transcript_fields(raw, context)
    common = {
        "protocol_id": PROTOCOL_ID,
        "artifact_role": "BRANCH_CELL_EVALUATOR_TRANSCRIPT",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": "false",
        "dispatch_authorized_by_evaluator": "false",
        "component_status": "null",
        "milestone_status": "null",
        "theorem_status": "null",
        "final_status": "null",
        "claim_boundary": MOCK_TRANSCRIPT_CLAIM_BOUNDARY,
        "input_argv_count": "12",
        "precision_bits": str(task.precision_bits),
        "taylor_order": "24",
        "tolerance": task.tolerance,
        "phase_grid": "64",
    }
    expected_keys = set(common) | {
        *(f"input_arg_{index:02d}" for index in range(12)),
        "epsilon", "root_box", "initial_state_box", "omega_slow",
        "tube_radius_sq", "solution_left_domain", "solution_right_domain",
        "solution_piece_count", "terminal_state_box",
        "maximum_rslow_sq_upper", "all_segments_inside",
        "lower_bound_violation_witness", "status",
    }
    for index in range(PHASE_GRID):
        stem = f"segment_{index:03d}"
        expected_keys.update(
            {f"{stem}_phase", f"{stem}_state", f"{stem}_rslow_sq", f"{stem}_margin_sq", f"{stem}_relation"}
        )
    require(set(fields) == expected_keys, f"{context}: transcript exact field set")
    for key, expected in common.items():
        require(fields[key] == expected, f"{context}: field {key}")
    for index, expected in enumerate(task.argv()):
        require(fields[f"input_arg_{index:02d}"] == expected, f"{context}: input echo {index}")

    printed_epsilon = parse_interval(fields["epsilon"], f"{context}.epsilon")
    printed_root = parse_vector(fields["root_box"], 4, f"{context}.root_box")
    require(contains_exact(printed_epsilon, task.epsilon), f"{context}: epsilon does not contain exact task")
    require(all(contains_exact(value, expected) for value, expected in zip(printed_root, task.root_box, strict=True)), f"{context}: root box does not contain exact task")
    initial = parse_vector(fields["initial_state_box"], 6, f"{context}.initial_state_box")
    expected_initial = [*task.root_box[:3], ("0", "0"), task.epsilon, task.root_box[3]]
    require(all(contains_exact(value, expected) for value, expected in zip(initial, expected_initial, strict=True)), f"{context}: initial state does not contain exact task")
    printed_omega = parse_interval(fields["omega_slow"], f"{context}.omega_slow")
    omega = independent_omega_slow(task.precision_bits)
    require(printed_omega[0] <= omega[0] and omega[1] <= printed_omega[1], f"{context}: printed omega does not contain independent Arb enclosure")
    printed_radius = parse_interval(fields["tube_radius_sq"], f"{context}.tube_radius_sq")
    require(printed_radius[0] <= TUBE_RADIUS_SQ <= printed_radius[1], f"{context}: tube threshold enclosure")

    maximum = Fraction(0)
    minimum_margin: Fraction | None = None
    printed_maximum = Fraction(0)
    for index in range(PHASE_GRID):
        stem = f"segment_{index:03d}"
        phase = parse_interval(fields[f"{stem}_phase"], f"{context}.{stem}.phase")
        require(phase == (Fraction(index, PHASE_GRID), Fraction(index + 1, PHASE_GRID)), f"{context}: phase {index} is not exact dyadic cell")
        state = parse_vector(fields[f"{stem}_state"], 6, f"{context}.{stem}.state")
        printed_rslow = parse_interval(fields[f"{stem}_rslow_sq"], f"{context}.{stem}.rslow")
        printed_margin = parse_interval(fields[f"{stem}_margin_sq"], f"{context}.{stem}.margin")
        require(fields[f"{stem}_relation"] == "INSIDE", f"{context}: phase {index} relation")
        recomputed = interval_add(interval_square(interval_mul(omega, state[0])), interval_square(state[2]))
        margin = interval_sub((TUBE_RADIUS_SQ, TUBE_RADIUS_SQ), recomputed)
        require(recomputed[1] < TUBE_RADIUS_SQ and margin[0] > 0, f"{context}: phase {index} fails independent tube gate")
        require(overlaps(printed_rslow, recomputed), f"{context}: phase {index} printed radius inconsistent")
        require(overlaps(printed_margin, margin), f"{context}: phase {index} printed margin inconsistent")
        maximum = max(maximum, recomputed[1])
        printed_maximum = max(printed_maximum, printed_rslow[1])
        minimum_margin = margin[0] if minimum_margin is None else min(minimum_margin, margin[0])

    require(parse_scalar_or_point_interval(fields["solution_left_domain"], f"{context}.left_domain") == 0, f"{context}: SolutionCurve left domain")
    require(parse_scalar_or_point_interval(fields["solution_right_domain"], f"{context}.right_domain") == 1, f"{context}: SolutionCurve right domain")
    require(re.fullmatch(r"[1-9][0-9]*", fields["solution_piece_count"]) is not None, f"{context}: positive piece count")
    parse_vector(fields["terminal_state_box"], 6, f"{context}.terminal_state_box")
    aggregate_maximum = parse_interval(fields["maximum_rslow_sq_upper"], f"{context}.maximum")
    require(aggregate_maximum[0] <= printed_maximum <= aggregate_maximum[1], f"{context}: printed aggregate maximum")
    require(fields["all_segments_inside"] == "1", f"{context}: all-segments flag")
    require(fields["lower_bound_violation_witness"] == "0", f"{context}: violation witness")
    require(fields["status"] == CELL_PASS_STATUS, f"{context}: terminal status")
    assert minimum_margin is not None
    return TranscriptReplay(
        maximum_rslow_sq_upper=maximum,
        minimum_margin_sq_lower=minimum_margin,
        phase_checks=PHASE_GRID,
        input_domain=(task.epsilon, task.root_box),
        evaluator_status=CELL_PASS_STATUS,
    )


RUNTIME_COMMON_KEYS = {
    "artifact_role", "authority", "claim_boundary", "component_status",
    "final_status", "freeze_sha256", "matrix_id", "milestone_status",
    "protocol_id", "run_config_sha256", "schema_version",
    "scientific_licensing_enabled", "theorem_status",
}
RECORD_KEYS = RUNTIME_COMMON_KEYS | {
    "bindings", "budgets", "cell", "execution_pin", "invocation", "raw", "scheduler_result",
}
MANIFEST_KEYS = RUNTIME_COMMON_KEYS | {"budgets", "cell_identity", "files", "task_binding_sha256"}
RUNTIME_BUDGET = {
    "pipe_close_grace_ms": 1_000,
    "record_bytes": 4 * 1024 * 1024,
    "stderr_bytes": 1024 * 1024,
    "stdout_bytes": 16 * 1024 * 1024,
    "term_grace_ms": 2_000,
    "timeout_ms": 600_000,
    "total_cell_bytes": 32 * 1024 * 1024,
}


def expected_runtime_bindings(mock_evaluator: Mapping[str, Any]) -> dict[str, str]:
    return {
        "capd_commit": "0" * 40,
        "capd_flags_sha256": sha256_bytes(b"R401-VAL-L3-A1 mock CAPD flags absent sentinel\n"),
        "evaluator_binary_sha256": mock_evaluator["sha256"],
        "evaluator_source_path": mock_evaluator["path"],
        "evaluator_source_sha256": mock_evaluator["sha256"],
        "runtime_libraries_sha256": sha256_bytes(b"R401-VAL-L3-A1 mock runtime libraries absent sentinel\n"),
    }


def validate_runtime_common(payload: Mapping[str, Any], role: str, context: MockRunContext, label: str) -> None:
    exact_int(payload["schema_version"], f"{label}.schema_version", expected=1)
    require(payload["protocol_id"] == PROTOCOL_ID and payload["artifact_role"] == role, f"{label}: identity")
    require(payload["authority"] == "PRODUCER_ONLY" and payload["claim_boundary"] == CELL_CLAIM_BOUNDARY, f"{label}: authority/claim")
    exact_bool(payload["scientific_licensing_enabled"], False, f"{label}.scientific_licensing_enabled")
    for key in ("component_status", "milestone_status", "theorem_status", "final_status"):
        require(payload[key] is None, f"{label}: unauthorized {key}")
    require(payload["matrix_id"] == context.run_config["matrix_id"], f"{label}: matrix")
    require(payload["run_config_sha256"] == context.run_config_image.sha256, f"{label}: run config")
    require(payload["freeze_sha256"] == sha256_bytes(b"R401-VAL-L3-A1 mock freeze absent sentinel\n"), f"{label}: mock freeze sentinel")


@dataclass(frozen=True)
class CellReplay:
    aggregate_entry: dict[str, Any]
    transcript: TranscriptReplay
    evaluator_binding: dict[str, str]
    snapshots: tuple[CapturedFile, ...]


def validate_execution_pin(payload: Any, mock_evaluator: Mapping[str, Any], label: str) -> None:
    exact_keys(payload, {"binary", "source"}, f"{label}.execution_pin")
    evaluator_path = canonical_absolute_path(mock_evaluator["path"], f"{label}.mock evaluator")
    evaluator_image = capture_file(evaluator_path, f"{label}.mock evaluator")
    evaluator_stat = os.stat(evaluator_path, follow_symlinks=False)
    require(evaluator_image.sha256 == mock_evaluator["sha256"], f"{label}: mock evaluator hash")
    for role in ("binary", "source"):
        pin = payload[role]
        exact_keys(
            pin,
            {"descriptor_hash_matches_after", "descriptor_identity_matches_after", "device", "inode", "mode", "path", "path_identity_matches_after", "sha256", "size"},
            f"{label}.execution_pin.{role}",
        )
        for key in ("descriptor_hash_matches_after", "descriptor_identity_matches_after", "path_identity_matches_after"):
            exact_bool(pin[key], True, f"{label}.execution_pin.{role}.{key}")
        for key in ("device", "inode", "mode", "size"):
            exact_int(pin[key], f"{label}.execution_pin.{role}.{key}", minimum=0)
        require(
            pin["path"] == str(evaluator_path)
            and pin["sha256"] == evaluator_image.sha256
            and pin["size"] == evaluator_image.size
            and pin["device"] == evaluator_stat.st_dev
            and pin["inode"] == evaluator_stat.st_ino
            and pin["mode"] == stat.S_IMODE(evaluator_stat.st_mode),
            f"{label}: execution pin binding",
        )


def validate_branch_cell(context: MockRunContext, task: ExpectedTask, mock_evaluator: Mapping[str, Any]) -> CellReplay:
    label = f"branch cell {task.precision_bits}:{task.slab_id}"
    cell = context.input_dir / "branch" / "cells" / str(task.precision_bits) / task.slab_id
    require_exact_directory_names(cell, {"record.json", "stderr.txt", "stdout.txt"}, label)
    stdout_image = capture_file(cell / "stdout.txt", f"{label}.stdout", maximum_bytes=RUNTIME_BUDGET["stdout_bytes"])
    stderr_image = capture_file(cell / "stderr.txt", f"{label}.stderr", maximum_bytes=RUNTIME_BUDGET["stderr_bytes"])
    record, record_image = load_json(cell / "record.json", f"{label}.record", canonical="runtime", maximum_bytes=RUNTIME_BUDGET["record_bytes"])
    require(stderr_image.raw == b"", f"{label}: certified stderr is nonempty")
    exact_keys(record, RECORD_KEYS, f"{label}.record")
    validate_runtime_common(record, "BRANCH_CELL_RECORD", context, f"{label}.record")
    expected_binding = expected_runtime_bindings(mock_evaluator)
    require_json_exact(record["bindings"], expected_binding, f"{label}.bindings")
    require_json_exact(record["budgets"], RUNTIME_BUDGET, f"{label}.budgets")
    require_json_exact(record["cell"], task.payload(), f"{label}.task")
    validate_execution_pin(record["execution_pin"], mock_evaluator, label)

    invocation = record["invocation"]
    exact_keys(invocation, {"argument_echo_count", "argv", "argv0_scheduler_binding", "argv_sha256", "exact_string_count"}, f"{label}.invocation")
    expected_argv = task.argv()
    require_json_exact(invocation["argv"], expected_argv, f"{label}.argv")
    require(invocation["argv0_scheduler_binding"] == expected_argv[0], f"{label}: argv0 binding")
    exact_int(invocation["argument_echo_count"], f"{label}.argument_echo_count", expected=12)
    exact_int(invocation["exact_string_count"], f"{label}.exact_string_count", expected=12)
    require(invocation["argv_sha256"] == sha256_bytes(runtime_json_bytes(expected_argv)), f"{label}: argv hash")

    raw = record["raw"]
    exact_keys(raw, {"record_cap_bytes", "record_truncated", "stderr_bytes", "stderr_cap_bytes", "stderr_file", "stderr_sha256", "stderr_truncated", "stdout_bytes", "stdout_cap_bytes", "stdout_file", "stdout_sha256", "stdout_truncated", "total_cell_cap_bytes"}, f"{label}.raw")
    stdout_relative = f"branch/cells/{task.precision_bits}/{task.slab_id}/stdout.txt"
    stderr_relative = f"branch/cells/{task.precision_bits}/{task.slab_id}/stderr.txt"
    require(raw["stdout_file"] == stdout_relative and raw["stderr_file"] == stderr_relative, f"{label}: raw paths")
    for stem, image, cap in (("stdout", stdout_image, RUNTIME_BUDGET["stdout_bytes"]), ("stderr", stderr_image, RUNTIME_BUDGET["stderr_bytes"])):
        exact_int(raw[f"{stem}_bytes"], f"{label}.{stem}_bytes", expected=image.size)
        exact_int(raw[f"{stem}_cap_bytes"], f"{label}.{stem}_cap", expected=cap)
        require(raw[f"{stem}_sha256"] == image.sha256, f"{label}: {stem} hash")
        exact_bool(raw[f"{stem}_truncated"], False, f"{label}.{stem}_truncated")
    exact_int(raw["record_cap_bytes"], f"{label}.record_cap", expected=RUNTIME_BUDGET["record_bytes"])
    exact_int(raw["total_cell_cap_bytes"], f"{label}.total_cap", expected=RUNTIME_BUDGET["total_cell_bytes"])
    exact_bool(raw["record_truncated"], False, f"{label}.record_truncated")
    require(record_image.size < RUNTIME_BUDGET["record_bytes"] and record_image.size + stdout_image.size + stderr_image.size < RUNTIME_BUDGET["total_cell_bytes"], f"{label}: byte caps")

    result = record["scheduler_result"]
    exact_keys(result, {"classification", "descendant_group_survived_parent", "descendant_pipe_leak", "evaluator_status", "failure_reason", "kill_sent", "process_group_residual", "return_code", "signal_number", "term_sent", "timed_out"}, f"{label}.scheduler_result")
    require(result["classification"] == SCHEDULER_PASS and result["evaluator_status"] == CELL_PASS_STATUS, f"{label}: passing scheduler/evaluator status")
    exact_int(result["return_code"], f"{label}.return_code", expected=0)
    require(result["failure_reason"] is None and result["signal_number"] is None, f"{label}: unexpected failure metadata")
    for key in ("descendant_group_survived_parent", "descendant_pipe_leak", "kill_sent", "process_group_residual", "term_sent", "timed_out"):
        exact_bool(result[key], False, f"{label}.{key}")
    transcript = replay_transcript(stdout_image.raw, task, f"{label}.transcript")

    manifest_path = context.input_dir / "branch" / "cell_manifests" / str(task.precision_bits) / f"{task.slab_id}.json"
    manifest, manifest_image = load_json(manifest_path, f"{label}.manifest", canonical="runtime", maximum_bytes=RUNTIME_BUDGET["record_bytes"])
    exact_keys(manifest, MANIFEST_KEYS, f"{label}.manifest")
    validate_runtime_common(manifest, "BRANCH_CELL_MANIFEST", context, f"{label}.manifest")
    require_json_exact(manifest["budgets"], RUNTIME_BUDGET, f"{label}.manifest.budgets")
    require_json_exact(manifest["cell_identity"], {"precision_bits": task.precision_bits, "slab_id": task.slab_id}, f"{label}.manifest.cell_identity")
    expected_files = {
        f"branch/cells/{task.precision_bits}/{task.slab_id}/record.json": record_image.sha256,
        stderr_relative: stderr_image.sha256,
        stdout_relative: stdout_image.sha256,
    }
    require_json_exact(manifest["files"], expected_files, f"{label}.manifest.files")
    require(manifest["task_binding_sha256"] == sha256_bytes(runtime_json_bytes(task.payload())), f"{label}: task binding hash")
    return CellReplay(
        aggregate_entry={
            "cell": {"precision_bits": task.precision_bits, "slab_id": task.slab_id},
            "path": f"branch/cell_manifests/{task.precision_bits}/{task.slab_id}.json",
            "sha256": manifest_image.sha256,
            "size_bytes": manifest_image.size,
        },
        transcript=transcript,
        evaluator_binding=expected_binding,
        snapshots=(stdout_image, stderr_image, record_image, manifest_image),
    )


def directory_names(path: Path, context: str) -> set[str]:
    reject_symlink_components(path, context)
    require(path.is_dir() and not path.is_symlink(), f"{context}: directory required")
    before = os.stat(path, follow_symlinks=False)
    names: set[str] = set()
    identities: set[tuple[int, int]] = set()
    for entry in path.iterdir():
        metadata = os.lstat(entry)
        require(not stat.S_ISLNK(metadata.st_mode), f"{context}: symlink entry {entry.name}")
        identity = (metadata.st_dev, metadata.st_ino)
        require(identity not in identities, f"{context}: inode alias {entry.name}")
        identities.add(identity)
        names.add(entry.name)
    after = os.stat(path, follow_symlinks=False)
    require(
        _fingerprint(before) == _fingerprint(after),
        f"{context}: directory changed during exact scan",
    )
    return names


def require_exact_directory_names(path: Path, expected: set[str], context: str) -> None:
    actual = directory_names(path, context)
    require(actual == expected, f"{context}: names differ; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")


AGGREGATE_SUMMARY_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "matrix", "cell_count",
    "ordered_cell_manifest_root", "status_counts",
    "scheduler_classification_counts", "mock_evaluator",
    "scientific_licensing_enabled", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
AGGREGATE_MANIFEST_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "artifact_status",
    "authority", "mock_only", "matrix_id", "main_freeze_sha256",
    "run_config_sha256", "ordered_cell_manifest_root", "cell_manifests",
    "summary", "mock_evaluator", "scientific_licensing_enabled",
    "claim_boundary", "component_status", "milestone_status",
    "theorem_status", "final_status",
}
CHECKER_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "checker_status", "component_status", "scientific_licensing_enabled",
    "passed", "matrix_id", "main_freeze_sha256", "run_config_sha256",
    "component_aggregate_summary_sha256",
    "component_aggregate_manifest_sha256", "replay_counts",
    "cross_precision", "diagnostics", "failures", "source_bindings",
    "claim_boundary", "milestone_status", "theorem_status", "final_status",
}
POSTCHECK_KEYS = {
    "schema_version", "protocol_id", "artifact_role", "authority",
    "postcheck_status", "passed", "checker_path", "checker_sha256",
    "main_freeze_sha256", "run_config_sha256", "bound_artifacts",
    "replay_counts", "failures", "claim_boundary", "component_status",
    "milestone_status", "theorem_status", "final_status",
}
INTERRUPTED_LOCK_PATTERN = re.compile(
    r"(S(?:00[0-9]|0[1-4][0-9]|050))\.attempt-(0|[1-9][0-9]*)"
    r"\.generation-([0-9a-f]{16})\.owner-([0-9a-f]{32})\.lock\Z"
)
LOCK_KEYS = {
    "artifact_role", "attempt", "generation_prefix",
    "owner_process_start_time", "owner_token", "pid", "precision_bits",
    "protocol_id", "slab_id",
}


def _within(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def validate_mock_evaluator(
    payload: Any,
    context: MockRunContext,
    label: str,
) -> tuple[dict[str, str], CapturedFile]:
    exact_keys(payload, {"path", "sha256"}, label)
    evaluator_path = canonical_absolute_path(payload["path"], f"{label}.path")
    require(
        not _within(evaluator_path, context.input_dir)
        and not _within(evaluator_path, context.operational_dir),
        f"{label}: evaluator lies inside a result root",
    )
    image = capture_file(evaluator_path, label, maximum_bytes=1024 * 1024)
    metadata = os.stat(evaluator_path, follow_symlinks=False)
    require(metadata.st_mode & 0o111 != 0, f"{label}: evaluator is not executable")
    require_sha256(payload["sha256"], f"{label}.sha256")
    require(payload["sha256"] == image.sha256, f"{label}: evaluator hash mismatch")
    return {"path": str(evaluator_path), "sha256": image.sha256}, image


def validate_authoritative_namespace(input_dir: Path, *, allow_checker: bool) -> None:
    root_names = directory_names(input_dir, "mock authoritative root")
    required = {"run_config.json", "static", "branch"}
    permitted = required | {"independent_static_checker.json", "STATIC_POSTCHECK_STATUS.json"}
    if allow_checker:
        required.add("independent_branch_checker.json")
        permitted.add("independent_branch_checker.json")
    require(required <= root_names, "mock authoritative root: required branch objects missing")
    require(
        root_names <= permitted,
        f"mock authoritative root: extra paths {sorted(root_names-permitted)}",
    )
    directory_names(input_dir / "static", "mock static sibling")
    branch = input_dir / "branch"
    require_exact_directory_names(
        branch,
        {"cells", "cell_manifests", "aggregate_summary.json", "aggregate_manifest.json"},
        "mock branch root",
    )
    require_exact_directory_names(
        branch / "cells", {str(bits) for bits in PRECISIONS}, "mock branch cells"
    )
    require_exact_directory_names(
        branch / "cell_manifests",
        {str(bits) for bits in PRECISIONS},
        "mock branch cell manifests",
    )
    for bits in PRECISIONS:
        require_exact_directory_names(
            branch / "cells" / str(bits), set(SLABS), f"mock branch cells {bits}"
        )
        require_exact_directory_names(
            branch / "cell_manifests" / str(bits),
            {f"{slab}.json" for slab in SLABS},
            f"mock branch manifests {bits}",
        )
        for slab_id in SLABS:
            require_exact_directory_names(
                branch / "cells" / str(bits) / slab_id,
                {"record.json", "stderr.txt", "stdout.txt"},
                f"mock branch cell {bits}:{slab_id}",
            )


def _validate_empty_precision_tree(path: Path, context: str) -> None:
    require_exact_directory_names(path, {"128", "256"}, context)
    for bits in PRECISIONS:
        require_exact_directory_names(path / str(bits), set(), f"{context} {bits}")


def _validate_interrupted_lock(path: Path, bits: int, prefix: str) -> None:
    match = INTERRUPTED_LOCK_PATTERN.fullmatch(path.name)
    require(match is not None, f"interrupted lock: malformed name {path.name}")
    slab_id, attempt, generation, owner = match.groups()
    payload, _image = load_json(path, "interrupted branch lock", canonical="compact", maximum_bytes=64 * 1024)
    exact_keys(payload, LOCK_KEYS, "interrupted branch lock")
    require(
        payload["artifact_role"] == "BRANCH_CELL_OPERATIONAL_LOCK"
        and payload["protocol_id"] == PROTOCOL_ID,
        "interrupted branch lock identity",
    )
    exact_int(payload["attempt"], "interrupted lock.attempt", expected=int(attempt))
    exact_int(payload["precision_bits"], "interrupted lock.precision_bits", expected=bits)
    exact_int(payload["pid"], "interrupted lock.pid", minimum=1)
    exact_int(payload["owner_process_start_time"], "interrupted lock.start", minimum=1)
    require(
        payload["slab_id"] == slab_id
        and payload["generation_prefix"] == generation == prefix
        and payload["owner_token"] == owner,
        "interrupted branch lock filename/payload mismatch",
    )


def validate_quiescent_operational(context: MockRunContext) -> None:
    path = context.operational_dir
    if not os.path.lexists(path):
        return
    names = directory_names(path, "mock operational root")
    require(names <= {"staging", "locks", "interrupted"}, "mock operational root: extra namespace")
    if "staging" in names:
        components = directory_names(path / "staging", "mock operational staging")
        require(components <= {"static", "branch"}, "mock operational staging: unexpected component")
        require("branch" in components, "mock operational staging: branch namespace absent")
        for component in components:
            _validate_empty_precision_tree(
                path / "staging" / component,
                f"mock operational staging {component}",
            )
    if "locks" in names:
        components = directory_names(path / "locks", "mock operational locks")
        require(components <= {"static", "branch"}, "mock operational locks: unexpected component")
        for component in components:
            _validate_empty_precision_tree(
                path / "locks" / component,
                f"mock operational locks {component}",
            )
    if "interrupted" in names:
        interrupted = path / "interrupted"
        interrupted_names = directory_names(interrupted, "mock interrupted root")
        require(
            "branch" not in interrupted_names and interrupted_names <= {"locks"},
            "withdrawn or unexpected interrupted branch staging namespace",
        )
        if "locks" in interrupted_names:
            locks = interrupted / "locks"
            require_exact_directory_names(locks, {"branch"}, "mock interrupted locks")
            branch = locks / "branch"
            precision_names = directory_names(branch, "mock interrupted branch locks")
            require(precision_names <= {"128", "256"}, "mock interrupted lock precision namespace")
            for precision in precision_names:
                leaf = branch / precision
                for name in directory_names(leaf, f"mock interrupted locks {precision}"):
                    _validate_interrupted_lock(
                        leaf / name,
                        int(precision),
                        context.run_config_image.sha256[:16],
                    )


def aggregate_common(
    role: str,
    context: MockRunContext,
    ordered_root: str,
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": role,
        "artifact_status": MOCK_ARTIFACT_STATUS,
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": context.run_config["matrix_id"],
        "main_freeze_sha256": None,
        "run_config_sha256": context.run_config_image.sha256,
        "ordered_cell_manifest_root": ordered_root,
    }


@dataclass(frozen=True)
class AggregateReplay:
    summary: dict[str, Any]
    summary_image: CapturedFile
    manifest: dict[str, Any]
    manifest_image: CapturedFile
    mock_evaluator: dict[str, str]
    evaluator_image: CapturedFile


def load_aggregate_envelope(context: MockRunContext) -> AggregateReplay:
    summary, summary_image = load_json(
        context.input_dir / "branch" / "aggregate_summary.json",
        "mock branch aggregate summary",
        canonical="compact",
    )
    manifest, manifest_image = load_json(
        context.input_dir / "branch" / "aggregate_manifest.json",
        "mock branch aggregate manifest",
        canonical="compact",
    )
    exact_keys(summary, AGGREGATE_SUMMARY_KEYS, "mock branch aggregate summary")
    exact_keys(manifest, AGGREGATE_MANIFEST_KEYS, "mock branch aggregate manifest")
    mock_evaluator, evaluator_image = validate_mock_evaluator(
        summary["mock_evaluator"], context, "mock branch evaluator"
    )
    require_json_exact(manifest["mock_evaluator"], mock_evaluator, "aggregate evaluator agreement")
    return AggregateReplay(
        summary=summary,
        summary_image=summary_image,
        manifest=manifest,
        manifest_image=manifest_image,
        mock_evaluator=mock_evaluator,
        evaluator_image=evaluator_image,
    )


def validate_aggregate(
    context: MockRunContext,
    aggregate: AggregateReplay,
    entries: list[dict[str, Any]],
) -> str:
    require(len(entries) == 102, "mock branch aggregate requires 102 entries")
    ordered_root = sha256_bytes(canonical_json_bytes(entries))
    expected_summary = {
        **aggregate_common(
            "MOCK_BRANCH_AGGREGATE_SUMMARY", context, ordered_root
        ),
        "matrix": matrix_payload(),
        "cell_count": 102,
        "status_counts": {CELL_PASS_STATUS: 102},
        "scheduler_classification_counts": {SCHEDULER_PASS: 102},
        "mock_evaluator": aggregate.mock_evaluator,
        "scientific_licensing_enabled": False,
        "claim_boundary": PRODUCER_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    require_json_exact(aggregate.summary, expected_summary, "mock branch aggregate summary")
    expected_manifest = {
        **aggregate_common(
            "MOCK_BRANCH_AGGREGATE_MANIFEST", context, ordered_root
        ),
        "cell_manifests": entries,
        "summary": {
            "path": "branch/aggregate_summary.json",
            "sha256": aggregate.summary_image.sha256,
            "size_bytes": aggregate.summary_image.size,
        },
        "mock_evaluator": aggregate.mock_evaluator,
        "scientific_licensing_enabled": False,
        "claim_boundary": PRODUCER_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    require_json_exact(aggregate.manifest, expected_manifest, "mock branch aggregate manifest")
    return ordered_root


def fraction_token(value: Fraction) -> str:
    # Composite control objects freeze the diagnostic grammar as p/q even for
    # integral rationals (notably the synthetic maximum 0/1).
    return f"{value.numerator}/{value.denominator}"


def validate_cross_precision(
    cells: Mapping[tuple[int, str], CellReplay],
) -> tuple[int, int]:
    expected = {(bits, slab) for bits in PRECISIONS for slab in SLABS}
    require(set(cells) == expected, "branch replay matrix incomplete")
    input_agreement = 0
    status_agreement = 0
    for slab_id in SLABS:
        left = cells[(128, slab_id)].transcript
        right = cells[(256, slab_id)].transcript
        require(
            left.input_domain == right.input_domain,
            f"branch {slab_id}: cross-precision input disagreement",
        )
        input_agreement += 1
        require(
            left.evaluator_status == right.evaluator_status == CELL_PASS_STATUS,
            f"branch {slab_id}: cross-precision verdict disagreement",
        )
        status_agreement += 1
    require(
        input_agreement == status_agreement == 51,
        "branch cross-precision gate incomplete",
    )
    return input_agreement, status_agreement


def replay_mock_branch_archive(
    input_dir: Path,
    *,
    allow_checker: bool,
) -> dict[str, Any]:
    input_dir = canonical_absolute_path(str(input_dir), "branch checker input directory")
    validate_authoritative_namespace(input_dir, allow_checker=allow_checker)
    context = validate_mock_run_config(input_dir)
    validate_quiescent_operational(context)
    bundle = load_l1_bundle()
    aggregate = load_aggregate_envelope(context)
    tasks = expected_tasks(bundle, aggregate.mock_evaluator["path"])
    entries: list[dict[str, Any]] = []
    cells: dict[tuple[int, str], CellReplay] = {}
    snapshots: list[CapturedFile] = [
        context.run_config_image,
        aggregate.summary_image,
        aggregate.manifest_image,
        aggregate.evaluator_image,
        *bundle.snapshots,
    ]
    common_binding: dict[str, str] | None = None
    maximum = Fraction(0)
    minimum_margin: Fraction | None = None
    phase_checks = 0
    for task in tasks:
        replay = validate_branch_cell(context, task, aggregate.mock_evaluator)
        identity = (task.precision_bits, task.slab_id)
        require(identity not in cells, f"duplicate replayed branch cell {identity}")
        cells[identity] = replay
        entries.append(replay.aggregate_entry)
        snapshots.extend(replay.snapshots)
        if common_binding is None:
            common_binding = replay.evaluator_binding
        else:
            require_json_exact(replay.evaluator_binding, common_binding, "cross-cell evaluator binding")
        maximum = max(maximum, replay.transcript.maximum_rslow_sq_upper)
        minimum_margin = (
            replay.transcript.minimum_margin_sq_lower
            if minimum_margin is None
            else min(minimum_margin, replay.transcript.minimum_margin_sq_lower)
        )
        phase_checks += replay.transcript.phase_checks
    ordered_root = validate_aggregate(context, aggregate, entries)
    input_agreement, status_agreement = validate_cross_precision(cells)
    require(phase_checks == 102 * PHASE_GRID, "branch phase replay count")
    require(maximum < TUBE_RADIUS_SQ, "mock replayed tube maximum reaches threshold")
    require(minimum_margin is not None and minimum_margin > 0, "mock replayed tube margin is not positive")
    for image in snapshots:
        image.verify_unchanged(f"final snapshot replay {image.path.name}")
    aggregate.evaluator_image.verify_unchanged("final mock evaluator replay")
    return {
        "run_config_sha256": context.run_config_image.sha256,
        "matrix_id": context.run_config["matrix_id"],
        "aggregate_summary_sha256": aggregate.summary_image.sha256,
        "aggregate_manifest_sha256": aggregate.manifest_image.sha256,
        "ordered_cell_manifest_root": ordered_root,
        "producer_source_bindings": context.producer_source_bindings,
        "accepted_l1_chain_bindings": {
            **bundle.chain_hashes,
            project_relative(PLAN): bundle.plan_sha256,
        },
        "mock_evaluator": aggregate.mock_evaluator,
        "replay_counts": {
            "accepted_l1_chain_objects": 6,
            "aggregate_objects": 2,
            "cell_directories": 102,
            "cell_manifests": 102,
            "cell_records": 102,
            "hash_bound_payloads": 408,
            "phase_records": phase_checks,
            "raw_stderr_objects": 102,
            "raw_transcripts": 102,
            "tube_implication_checks": phase_checks,
        },
        "cross_precision": {
            "all_agree": True,
            "input_domains_agree": input_agreement,
            "mock_only": True,
            "scientific_domain_replay_performed": False,
            "slab_pairs": 51,
            "status_pairs_agree": status_agreement,
        },
        "maximum_rslow_sq_upper": fraction_token(maximum),
        "minimum_margin_sq_lower": fraction_token(minimum_margin),
    }


def build_mock_checker_result(replay: Mapping[str, Any]) -> dict[str, Any]:
    result = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": CHECKER_ROLE,
        "authority": "INDEPENDENT_CHECKER",
        "checker_status": MOCK_CHECKER_STATUS,
        "component_status": None,
        "scientific_licensing_enabled": False,
        "passed": True,
        "matrix_id": replay["matrix_id"],
        "main_freeze_sha256": None,
        "run_config_sha256": replay["run_config_sha256"],
        "component_aggregate_summary_sha256": replay["aggregate_summary_sha256"],
        "component_aggregate_manifest_sha256": replay["aggregate_manifest_sha256"],
        "replay_counts": replay["replay_counts"],
        "cross_precision": replay["cross_precision"],
        "diagnostics": {
            "archive_transcripts_are_synthetic": True,
            "artifact_status": MOCK_ARTIFACT_STATUS,
            "maximum_rslow_sq_upper": replay["maximum_rslow_sq_upper"],
            "minimum_margin_sq_lower": replay["minimum_margin_sq_lower"],
            "mock_only": True,
            "ordered_cell_manifest_root": replay["ordered_cell_manifest_root"],
            "production_dispatch_observed": False,
            "scientific_flow_replay_performed": False,
            "synthetic_tube_implication_replay_performed": True,
        },
        "failures": [],
        "source_bindings": {
            "accepted_l1_chain_bindings": replay["accepted_l1_chain_bindings"],
            "checker_sha256": sha256_file(CHECKER),
            "mock_evaluator": replay["mock_evaluator"],
            "producer_source_bindings": replay["producer_source_bindings"],
        },
        "claim_boundary": MOCK_CLAIM_BOUNDARY,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(result, CHECKER_KEYS, "mock branch checker result")
    return result


def run_checker(input_dir: Path) -> dict[str, Any]:
    """Replay a complete synthetic branch archive without scientific authority."""

    return build_mock_checker_result(
        replay_mock_branch_archive(input_dir, allow_checker=False)
    )


def run_postcheck(input_dir: Path) -> dict[str, Any]:
    input_dir = canonical_absolute_path(str(input_dir), "branch postcheck input directory")
    replay = replay_mock_branch_archive(input_dir, allow_checker=True)
    expected_checker = build_mock_checker_result(replay)
    checker_path = input_dir / "independent_branch_checker.json"
    published, checker_image = load_json(
        checker_path, "published mock branch checker", canonical="compact"
    )
    exact_keys(published, CHECKER_KEYS, "published mock branch checker")
    require_json_exact(published, expected_checker, "published mock branch checker")
    result = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": POSTCHECK_ROLE,
        "authority": "POSTCHECK_ONLY",
        "postcheck_status": MOCK_POSTCHECK_STATUS,
        "passed": True,
        "checker_path": "independent_branch_checker.json",
        "checker_sha256": checker_image.sha256,
        "main_freeze_sha256": None,
        "run_config_sha256": replay["run_config_sha256"],
        "bound_artifacts": {
            "aggregate_manifest": {
                "path": "branch/aggregate_manifest.json",
                "sha256": replay["aggregate_manifest_sha256"],
            },
            "aggregate_summary": {
                "path": "branch/aggregate_summary.json",
                "sha256": replay["aggregate_summary_sha256"],
            },
            "checker_source": {
                "path": project_relative(CHECKER),
                "sha256": sha256_file(CHECKER),
            },
        },
        "replay_counts": replay["replay_counts"],
        "failures": [],
        "claim_boundary": MOCK_POSTCHECK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    exact_keys(result, POSTCHECK_KEYS, "mock branch postcheck result")
    return result


def _open_directory_fd(path: Path) -> int:
    return os.open(
        path,
        os.O_RDONLY
        | getattr(os, "O_DIRECTORY", 0)
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0),
    )


def write_once(path: Path, payload: bytes) -> None:
    path = canonical_absolute_path(str(path), "checker output path")
    require(type(payload) is bytes, "checker output payload must be bytes")
    reject_symlink_components(path.parent, "checker output parent")
    try:
        parent_fd = _open_directory_fd(path.parent)
    except OSError as error:
        raise BranchCheckError(f"checker output parent failed: {error}") from error
    parent_before = os.fstat(parent_fd)
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path.name,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0),
            0o644,
            dir_fd=parent_fd,
        )
        view = memoryview(payload)
        while view:
            written = os.write(descriptor, view)
            require(written > 0, "checker output short write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        require(
            stat.S_ISREG(info.st_mode)
            and info.st_nlink == 1
            and info.st_size == len(payload),
            "checker output publication mismatch",
        )
        entry = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        require(
            (entry.st_dev, entry.st_ino) == (info.st_dev, info.st_ino),
            "checker output directory entry mismatch",
        )
        replay_fd = _open_directory_fd(path.parent)
        try:
            parent_after = os.fstat(replay_fd)
            replay_entry = os.stat(path.name, dir_fd=replay_fd, follow_symlinks=False)
            require(
                (parent_before.st_dev, parent_before.st_ino)
                == (parent_after.st_dev, parent_after.st_ino)
                and (replay_entry.st_dev, replay_entry.st_ino)
                == (info.st_dev, info.st_ino),
                "checker output lexical replay mismatch",
            )
            os.fsync(replay_fd)
        finally:
            os.close(replay_fd)
        os.fsync(parent_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(parent_fd)


def canonical_absolute_argument(value: str) -> Path:
    try:
        return canonical_absolute_path(value, "command-line path")
    except BranchCheckError as error:
        raise argparse.ArgumentTypeError(str(error)) from error


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=canonical_absolute_argument, required=True)
    parser.add_argument(
        "--postcheck",
        action="store_true",
        help="replay the published mock branch checker and write its postcheck",
    )
    parser.add_argument(
        "--output",
        type=canonical_absolute_argument,
        default=None,
        help="canonical write-once output path",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        input_dir = arguments.input_dir
        expected_output = input_dir / (
            "BRANCH_POSTCHECK_STATUS.json"
            if arguments.postcheck
            else "independent_branch_checker.json"
        )
        if arguments.output is not None and arguments.output != expected_output:
            raise BranchCheckError("checker output must use the canonical archive path")
        result = run_postcheck(input_dir) if arguments.postcheck else run_checker(input_dir)
        write_once(expected_output, canonical_json_bytes(result))
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    if arguments.postcheck:
        print(
            f"postcheck_status={result['postcheck_status']} "
            f"component_status={result['component_status']}"
        )
    else:
        print(
            f"checker_status={result['checker_status']} "
            f"component_status={result['component_status']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
