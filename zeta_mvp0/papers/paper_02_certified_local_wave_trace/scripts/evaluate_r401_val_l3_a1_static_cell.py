#!/usr/bin/env python3
"""Evaluate one prospective R401-VAL-L3-A1 static phase-anchor cell.

This is a one-cell producer, not a scheduler and not a scientific authority.
It uses Arb interval arithmetic and exact rational subdivision geometry to
cover the normalized energy-one slow tube for one frozen slab/precision cell.
The two obligations are:

* the fast polar angle has positive numerator and denominator and satisfies
  ``theta_dot < 18`` on every feasible tube box; and
* every feasible positive ``P_+ = 0`` point has ``0.12 < Q_+ < 0.17``.

No ODE enclosure, full-orbit tube-residence claim, all-slab result, or
scientific release is made by this producer.  The formal independent checker
is a separate implementation and must not import this module.  Until a later
main freeze exists, executing this evaluator on a production or held-out cell
is prohibited; the module may be imported by mock-only contract tests.
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
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[1]
RUNNER = Path(__file__).resolve()
CHECKER = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_RELEASE_CHAIN = (
    L1_RELEASE,
    L1_SUMMARY,
    L1_MANIFEST,
    L1_CHECKER,
    L1_POSTCHECK,
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

SCHEMA_VERSION = 1
PROTOCOL_ID = "R401-VAL-L3-A1"
ARTIFACT_ROLE = "STATIC_CELL_PROOF"
AUTHORITY = "PRODUCER_ONLY"
PASS_STATUS = "STATIC_CELL_CERTIFIED"
PRECISIONS = (128, 256)
SLAB_PATTERN = re.compile(r"S(?:00[0-9]|0[1-4][0-9]|050)\Z")
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}\Z")

ANGLE_COORDINATES = ("qminus", "qplus", "pminus", "pplus")
SECTION_COORDINATES = ("qminus", "qplus", "pminus")
ANGLE_ROOT: dict[str, tuple[Fraction, Fraction]] = {
    "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
    "qplus": (Fraction(-18, 100), Fraction(18, 100)),
    "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    "pplus": (Fraction(-1415, 1000), Fraction(1415, 1000)),
}
SECTION_ROOTS: dict[str, dict[str, tuple[Fraction, Fraction]]] = {
    "SECTION_LOW": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(0), Fraction(12, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
    "SECTION_HIGH": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(17, 100), Fraction(18, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
    "SECTION_WINDOW": {
        "qminus": (Fraction(-15, 1000), Fraction(15, 1000)),
        "qplus": (Fraction(12, 100), Fraction(17, 100)),
        "pminus": (Fraction(-6, 100), Fraction(6, 100)),
    },
}

ENERGY_LEVEL = Fraction(1)
TUBE_RADIUS_SQUARED = Fraction(36, 10_000)
ANGLE_CEILING = Fraction(18)
EPSILON_CAP = Fraction(101, 1000)
PERIOD_MAX = Fraction(69, 100)
DEFAULT_MAX_DEPTH = 24
DEFAULT_MAX_NODES_PER_TREE = 250_000
DEFAULT_MAX_NODES_PER_CELL = 1_000_000

CLAIM_BOUNDARY = (
    "producer-only static phase-anchor cell conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no component, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)


class StaticCellContractError(RuntimeError):
    """A malformed frozen input or contradictory evaluator state."""


class StaticCellLimit(RuntimeError):
    """A frozen depth or node limit stopped a cell without a verdict."""

    def __init__(self, status: str, details: dict[str, Any]):
        super().__init__(status)
        self.status = status
        self.details = details


def _require_exact_json_value(value: Any, context: str = "$") -> None:
    """Reject Python aliases that have no frozen JSON data-model meaning.

    In particular, ``json.dumps`` otherwise accepts tuples, non-string object
    keys, integer subclasses, and non-finite floats.  The formal compact
    serializer is intentionally defined only on exact JSON values so that its
    byte image is reproducible outside this producer.
    """

    if value is None or type(value) in (bool, str, int):
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise StaticCellContractError(f"{context}: non-finite JSON number")
        return
    if type(value) is list:
        for index, item in enumerate(value):
            _require_exact_json_value(item, f"{context}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise StaticCellContractError(f"{context}: JSON object key is not an exact string")
            _require_exact_json_value(item, f"{context}.{key}")
        return
    raise StaticCellContractError(
        f"{context}: unsupported exact JSON value type {type(value).__name__}"
    )


def canonical_json_bytes(payload: Any) -> bytes:
    """Serialize the frozen ``CJ_COMPACT_V1`` byte image."""

    _require_exact_json_value(payload)
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
    )


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StaticCellContractError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise StaticCellContractError(f"nonfinite JSON number: {value}")


def _strict_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise StaticCellContractError(f"nonfinite JSON number: {value}")
    return parsed


def require_canonical_absolute_path(value: str | os.PathLike[str], context: str) -> Path:
    text = os.fspath(value)
    if not text.startswith("/") or text.startswith("//"):
        raise StaticCellContractError(f"{context}: one POSIX root slash required")
    if (
        "\x00" in text
        or "\\" in text
        or "//" in text[1:]
        or text.endswith("/")
        or any(component in ("", ".", "..") for component in text[1:].split("/"))
        or os.path.abspath(text) != text
    ):
        raise StaticCellContractError(f"{context}: non-canonical path spelling")
    return Path(text)


def _open_directory_fd(path: Path) -> int:
    path = require_canonical_absolute_path(path, "static directory path")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open("/", flags)
    try:
        for component in path.parts[1:]:
            next_fd = os.open(
                component, flags | nofollow, dir_fd=descriptor
            )
            os.close(descriptor)
            descriptor = next_fd
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def read_pinned_regular_bytes(path: Path) -> bytes:
    path = require_canonical_absolute_path(path, "static frozen input")
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        directory_fd = _open_directory_fd(path.parent)
    except OSError as error:
        raise StaticCellContractError(f"secure static input parent failed: {error}") from error
    parent_before = os.fstat(directory_fd)
    descriptor: int | None = None
    try:
        descriptor = os.open(path.name, os.O_RDONLY | nofollow, dir_fd=directory_fd)
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise StaticCellContractError("static frozen input must be one regular inode")
        if before.st_size > 64 * 1024 * 1024:
            raise StaticCellContractError("static frozen input exceeds byte cap")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        metadata_before = (
            before.st_dev,
            before.st_ino,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        metadata_after = (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if metadata_before != metadata_after:
            raise StaticCellContractError("static frozen input changed during read")
        entry = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        replay_parent_fd = _open_directory_fd(path.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            lexical = os.stat(
                path.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
        finally:
            os.close(replay_parent_fd)
        if (
            (entry.st_dev, entry.st_ino) != (before.st_dev, before.st_ino)
            or (lexical.st_dev, lexical.st_ino) != (before.st_dev, before.st_ino)
            or (replay_parent.st_dev, replay_parent.st_ino)
            != (parent_before.st_dev, parent_before.st_ino)
        ):
            raise StaticCellContractError("static frozen input path changed during read")
        raw = b"".join(chunks)
        if len(raw) != before.st_size:
            raise StaticCellContractError("static frozen input short read")
        return raw
    except OSError as error:
        raise StaticCellContractError(f"secure static input open failed: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_fd)


def strict_json_load(path: Path) -> Any:
    return strict_json_image(path)[0]


def strict_json_image(path: Path) -> tuple[Any, bytes]:
    raw = read_pinned_regular_bytes(path)
    return strict_json_bytes(raw, path), raw


def strict_json_bytes(raw: bytes, path: Path) -> Any:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise StaticCellContractError(f"non-UTF-8 JSON: {path}") from error
    try:
        payload = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_strict_float,
        )
    except (json.JSONDecodeError, ValueError) as error:
        raise StaticCellContractError(f"invalid strict JSON: {path}") from error
    return payload


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(read_pinned_regular_bytes(path))


def write_once(path: Path, payload: bytes) -> None:
    """Publish one evaluator payload without replacement.

    The transaction scheduler owns the containing staging directory.  This
    leaf writer deliberately refuses to create or resolve the parent so that
    a path alias cannot redirect a frozen cell.
    """

    path = require_canonical_absolute_path(path, "static evaluator output")
    if path.name != "proof.json":
        raise StaticCellContractError("static evaluator output must be proof.json")
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        directory_fd = _open_directory_fd(path.parent)
    except OSError as error:
        raise StaticCellContractError(f"secure static output parent failed: {error}") from error
    parent_before = os.fstat(directory_fd)
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | nofollow,
            0o644,
            dir_fd=directory_fd,
        )
        view = memoryview(payload)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        if (
            not stat.S_ISREG(info.st_mode)
            or info.st_nlink != 1
            or info.st_size != len(payload)
        ):
            raise StaticCellContractError("static output publication mismatch")
        entry = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        if (entry.st_dev, entry.st_ino) != (info.st_dev, info.st_ino):
            raise StaticCellContractError("static output directory entry mismatch")
        replay_parent_fd = _open_directory_fd(path.parent)
        try:
            replay_parent = os.fstat(replay_parent_fd)
            replay_entry = os.stat(
                path.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
            if (
                (replay_parent.st_dev, replay_parent.st_ino)
                != (parent_before.st_dev, parent_before.st_ino)
                or (replay_entry.st_dev, replay_entry.st_ino)
                != (info.st_dev, info.st_ino)
            ):
                raise StaticCellContractError("static output lexical replay mismatch")
            os.fsync(replay_parent_fd)
        finally:
            os.close(replay_parent_fd)
        os.fsync(directory_fd)
    except FileExistsError:
        raise
    except OSError as error:
        raise StaticCellContractError(f"secure static output open failed: {error}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_fd)


def require_sha256(value: str, label: str) -> str:
    if SHA256_PATTERN.fullmatch(value) is None:
        raise StaticCellContractError(f"{label} must be lowercase SHA-256")
    return value


def canonical_positive_int(value: str) -> int:
    if re.fullmatch(r"[1-9][0-9]*", value) is None:
        raise argparse.ArgumentTypeError("expected canonical positive decimal integer")
    return int(value)


def canonical_precision(value: str) -> int:
    if value not in {"128", "256"}:
        raise argparse.ArgumentTypeError("precision must be exactly 128 or 256")
    return int(value)


def lexical_absolute_output(value: str) -> Path:
    if (
        not value.startswith("/")
        or value.endswith("/")
        or "//" in value
        or "\\" in value
        or "\x00" in value
    ):
        raise argparse.ArgumentTypeError("output path is not canonical absolute POSIX")
    segments = value.split("/")[1:]
    if any(segment in {"", ".", ".."} for segment in segments):
        raise argparse.ArgumentTypeError("output path contains a path alias")
    return Path(value)


def fraction_record(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def interval_record_exact(
    interval: tuple[Fraction, Fraction],
) -> list[dict[str, str]]:
    return [fraction_record(interval[0]), fraction_record(interval[1])]


def box_record(
    box: dict[str, tuple[Fraction, Fraction]],
    coordinates: Iterable[str],
) -> dict[str, list[dict[str, str]]]:
    return {coordinate: interval_record_exact(box[coordinate]) for coordinate in coordinates}


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def point_ball(value: Fraction | int) -> arb:
    return arb(as_fmpq(Fraction(value)))


def interval_ball(interval: tuple[Fraction, Fraction]) -> arb:
    lower, upper = interval
    midpoint = (lower + upper) / 2
    radius = (upper - lower) / 2
    return arb(as_fmpq(midpoint), as_fmpq(radius))


def hull(left: arb, right: arb) -> arb:
    return arb.union(left, right)


def square_interval(value: arb) -> arb:
    """A dependency-aware square enclosure for a real Arb ball."""

    lower = value.lower()
    upper = value.upper()
    zero = arb(0)
    if lower >= zero:
        return hull(lower * lower, upper * upper).nonnegative_part()
    if upper <= zero:
        return hull(upper * upper, lower * lower).nonnegative_part()
    maximum = max(abs(lower).upper(), abs(upper).upper())
    return hull(zero, maximum * maximum).nonnegative_part()


def exprel_nonnegative(value: arb, *, order: int = 16) -> arb:
    """Enclose (exp(value)-1)/value on a nonnegative input interval."""

    if value.lower() < arb(0):
        raise ArithmeticError("exprel input is not certified nonnegative")
    total = arb(1)
    term = arb(1)
    for degree in range(1, order + 1):
        term = term * value / (degree + 1)
        total += term
    radius = abs(value).upper()
    factorial = 1
    for factor in range(2, order + 3):
        factorial *= factor
    remainder = radius ** (order + 1) * radius.exp() / factorial
    return total + arb(0, remainder.upper())


def printed_ball(value: arb, bits: int) -> str:
    digits = 52 if bits == 128 else 92
    return value.str(digits, radius=True, more=True)


@dataclass(frozen=True)
class Model:
    a: arb
    c: arb
    pi: arb
    lambda_slow: arb
    lambda_fast: arb
    omega_slow: arb
    omega_fast: arb
    e_slow: tuple[arb, arb]
    e_fast: tuple[arb, arb]


def build_model() -> Model:
    a = point_ball(Fraction(51, 50))
    pi_value = arb.pi()
    c = 2 * ((1 + a).sqrt() - 1)
    discriminant = c * (c * c + 4).sqrt()
    lambda_slow = (c * c + 2 - discriminant) / 2
    lambda_fast = (c * c + 2 + discriminant) / 2
    slow_raw = (1 - lambda_slow, -c)
    fast_raw = (lambda_fast - 1, c)
    slow_norm = square_interval(slow_raw[0]) + square_interval(slow_raw[1])
    fast_norm = square_interval(fast_raw[0]) + square_interval(fast_raw[1])
    slow_norm = slow_norm.sqrt()
    fast_norm = fast_norm.sqrt()
    return Model(
        a=a,
        c=c,
        pi=pi_value,
        lambda_slow=lambda_slow,
        lambda_fast=lambda_fast,
        omega_slow=2 * pi_value * lambda_slow.sqrt(),
        omega_fast=2 * pi_value * lambda_fast.sqrt(),
        e_slow=(slow_raw[0] / slow_norm, slow_raw[1] / slow_norm),
        e_fast=(fast_raw[0] / fast_norm, fast_raw[1] / fast_norm),
    )


@dataclass(frozen=True)
class Metrics:
    energy: arb
    tube_squared: arb
    angle_denominator: arb | None
    N_plus: arb | None
    angle_numerator: arb | None
    theta_dot: arb | None


@dataclass
class CellBudget:
    max_depth: int
    max_nodes_per_tree: int
    max_nodes_per_cell: int
    consumed_nodes: int = 0

    def consume(self, *, tree_id: str, tree_nodes: int, depth: int) -> None:
        if tree_nodes >= self.max_nodes_per_tree:
            raise StaticCellLimit(
                "STATIC_UNRESOLVED_NODE_BUDGET",
                {
                    "scope": "tree",
                    "tree_id": tree_id,
                    "limit": self.max_nodes_per_tree,
                    "consumed_before_node": tree_nodes,
                },
            )
        if self.consumed_nodes >= self.max_nodes_per_cell:
            raise StaticCellLimit(
                "STATIC_UNRESOLVED_NODE_BUDGET",
                {
                    "scope": "cell",
                    "tree_id": tree_id,
                    "limit": self.max_nodes_per_cell,
                    "consumed_before_node": self.consumed_nodes,
                },
            )
        if depth > self.max_depth:
            raise StaticCellLimit(
                "STATIC_UNRESOLVED_DEPTH",
                {
                    "tree_id": tree_id,
                    "limit": self.max_depth,
                    "unresolved_depth": depth,
                },
            )
        self.consumed_nodes += 1


def evaluate_metrics(
    model: Model,
    epsilon: arb,
    box: dict[str, tuple[Fraction, Fraction]],
    *,
    section: bool,
) -> Metrics:
    qm = interval_ball(box["qminus"])
    qp = interval_ball(box["qplus"])
    pm = interval_ball(box["pminus"])
    pp = arb(0) if section else interval_ball(box["pplus"])

    physical_q1 = model.e_slow[0] * qm + model.e_fast[0] * qp
    physical_q2 = model.e_slow[1] * qm + model.e_fast[1] * qp
    warped_1 = (
        -model.c * physical_q1
        - physical_q2
        - model.a * epsilon * square_interval(physical_q1)
    )
    warped_2 = physical_q1
    warped_squared = square_interval(warped_1) + square_interval(warped_2)
    # Every factor is mathematically nonnegative.  Arb's midpoint-radius
    # multiplication can display a tiny negative lower endpoint when one
    # factor contains zero, so intersect with the proved half-line.
    exponential_argument = (
        model.pi * square_interval(epsilon) * warped_squared
    ).nonnegative_part()
    potential = (
        2
        * model.pi
        * model.pi
        * warped_squared
        * exprel_nonnegative(exponential_argument)
    )
    energy = (
        square_interval(pm) + square_interval(pp)
    ) / 2 + potential
    tube_squared = (
        square_interval(model.omega_slow * qm) + square_interval(pm)
    )

    if section:
        return Metrics(energy, tube_squared, None, None, None, None)

    j11 = -model.c - 2 * model.a * epsilon * physical_q1
    exponential = exponential_argument.exp()
    factor = 4 * model.pi * model.pi * exponential
    gradient_physical_1 = factor * (j11 * warped_1 + warped_2)
    gradient_physical_2 = -factor * warped_1
    gradient_fast = (
        model.e_fast[0] * gradient_physical_1
        + model.e_fast[1] * gradient_physical_2
    )
    angle_denominator = (
        square_interval(model.omega_fast * qp) + square_interval(pp)
    )
    N_plus = square_interval(pp) + qp * gradient_fast
    # This is the numerator of theta_dot, namely omega_fast * N_plus.
    angle_numerator = model.omega_fast * N_plus
    theta_dot = angle_numerator / angle_denominator
    return Metrics(
        energy,
        tube_squared,
        angle_denominator,
        N_plus,
        angle_numerator,
        theta_dot,
    )


def terminal_classification(
    metrics: Metrics,
    box: dict[str, tuple[Fraction, Fraction]],
    *,
    goal: str,
) -> str | None:
    if metrics.tube_squared.lower() > point_ball(TUBE_RADIUS_SQUARED):
        return "TUBE_EXCLUDED"
    if (
        metrics.energy.upper() < point_ball(ENERGY_LEVEL)
        or metrics.energy.lower() > point_ball(ENERGY_LEVEL)
    ):
        return "ENERGY_EXCLUDED"
    if goal == "ANGLE_COVER":
        assert metrics.angle_denominator is not None
        assert metrics.N_plus is not None
        assert metrics.angle_numerator is not None
        assert metrics.theta_dot is not None
        if (
            metrics.angle_denominator.lower() > arb(0)
            and metrics.N_plus.lower() > arb(0)
            and metrics.angle_numerator.lower() > arb(0)
            and metrics.theta_dot.upper() < point_ball(ANGLE_CEILING)
        ):
            return "ANGLE_CERTIFIED"
        return None
    if goal == "SECTION_WINDOW_COVER":
        qlower, qupper = box["qplus"]
        if qlower >= Fraction(12, 100) and qupper <= Fraction(17, 100):
            return "LANDING_CLOSED_WINDOW"
    return None


def decisive_metrics_record(metrics: Metrics, classification: str, bits: int) -> dict[str, str]:
    if classification == "TUBE_EXCLUDED":
        return {"tube_squared": printed_ball(metrics.tube_squared, bits)}
    if classification == "ENERGY_EXCLUDED":
        return {"energy": printed_ball(metrics.energy, bits)}
    if classification == "ANGLE_CERTIFIED":
        assert metrics.angle_denominator is not None
        assert metrics.N_plus is not None
        assert metrics.angle_numerator is not None
        assert metrics.theta_dot is not None
        return {
            "D_plus": printed_ball(metrics.angle_denominator, bits),
            "N_plus": printed_ball(metrics.N_plus, bits),
            "theta_numerator": printed_ball(metrics.angle_numerator, bits),
            "theta_dot": printed_ball(metrics.theta_dot, bits),
        }
    if classification == "LANDING_CLOSED_WINDOW":
        return {}
    raise ValueError(f"unknown terminal classification {classification}")


def split_coordinate(
    box: dict[str, tuple[Fraction, Fraction]],
    root_box: dict[str, tuple[Fraction, Fraction]],
    coordinates: tuple[str, ...],
) -> str:
    def normalized_width(coordinate: str) -> Fraction:
        lower, upper = box[coordinate]
        root_lower, root_upper = root_box[coordinate]
        return (upper - lower) / (root_upper - root_lower)

    return max(coordinates, key=normalized_width)


def split_box(
    box: dict[str, tuple[Fraction, Fraction]],
    coordinate: str,
) -> tuple[Fraction, dict[str, tuple[Fraction, Fraction]], dict[str, tuple[Fraction, Fraction]]]:
    lower, upper = box[coordinate]
    midpoint = (lower + upper) / 2
    if not lower < midpoint < upper:
        raise ArithmeticError("non-strict exact midpoint")
    left = dict(box)
    right = dict(box)
    left[coordinate] = (lower, midpoint)
    right[coordinate] = (midpoint, upper)
    return midpoint, left, right


def build_tree(
    model: Model,
    epsilon: tuple[Fraction, Fraction],
    *,
    bits: int,
    tree_id: str,
    goal: str,
    root_box: dict[str, tuple[Fraction, Fraction]],
    budget: CellBudget,
) -> dict[str, Any]:
    coordinates = ANGLE_COORDINATES if goal == "ANGLE_COVER" else SECTION_COORDINATES
    epsilon_ball = interval_ball(epsilon)
    stack: list[tuple[str, str | None, int, dict[str, tuple[Fraction, Fraction]]]] = [
        (tree_id, None, 0, root_box)
    ]
    nodes: list[dict[str, Any]] = []
    terminal_counts: dict[str, int] = {}
    internal_count = 0
    terminal_count = 0
    maximum_depth = 0
    minimum_D_lower: arb | None = None
    minimum_N_lower: arb | None = None
    minimum_theta_numerator_lower: arb | None = None
    maximum_theta_dot_upper: arb | None = None
    while stack:
        node_id, parent_id, depth, box = stack.pop()
        budget.consume(tree_id=tree_id, tree_nodes=len(nodes), depth=depth)
        maximum_depth = max(maximum_depth, depth)
        metrics = evaluate_metrics(
            model,
            epsilon_ball,
            box,
            section=goal != "ANGLE_COVER",
        )
        classification = terminal_classification(metrics, box, goal=goal)
        node: dict[str, Any] = {
            "node_id": node_id,
            "parent_id": parent_id,
            "depth": depth,
        }
        if classification is not None:
            node["classification"] = classification
            node["decisive_intervals"] = decisive_metrics_record(
                metrics, classification, bits
            )
            terminal_counts[classification] = terminal_counts.get(classification, 0) + 1
            terminal_count += 1
            if classification == "ANGLE_CERTIFIED":
                assert metrics.angle_denominator is not None
                assert metrics.N_plus is not None
                assert metrics.angle_numerator is not None
                assert metrics.theta_dot is not None
                D_lower = metrics.angle_denominator.lower()
                N_lower = metrics.N_plus.lower()
                numerator_lower = metrics.angle_numerator.lower()
                theta_upper = metrics.theta_dot.upper()
                minimum_D_lower = (
                    D_lower if minimum_D_lower is None else min(minimum_D_lower, D_lower)
                )
                minimum_N_lower = (
                    N_lower if minimum_N_lower is None else min(minimum_N_lower, N_lower)
                )
                minimum_theta_numerator_lower = (
                    numerator_lower
                    if minimum_theta_numerator_lower is None
                    else min(minimum_theta_numerator_lower, numerator_lower)
                )
                maximum_theta_dot_upper = (
                    theta_upper
                    if maximum_theta_dot_upper is None
                    else max(maximum_theta_dot_upper, theta_upper)
                )
            nodes.append(node)
            continue
        if depth >= budget.max_depth:
            raise StaticCellLimit(
                "STATIC_UNRESOLVED_DEPTH",
                {
                    "tree_id": tree_id,
                    "limit": budget.max_depth,
                    "unresolved_depth": depth,
                    "node_id": node_id,
                },
            )
        coordinate = split_coordinate(box, root_box, coordinates)
        midpoint, left, right = split_box(box, coordinate)
        node.update(
            {
                "classification": "SPLIT",
                "split_coordinate": coordinate,
                "split_point": fraction_record(midpoint),
            }
        )
        internal_count += 1
        nodes.append(node)
        # Push right first so the serialized depth-first order is left first.
        stack.append((node_id + "1", node_id, depth + 1, right))
        stack.append((node_id + "0", node_id, depth + 1, left))

    if goal == "ANGLE_COVER":
        if any(
            value is None
            for value in (
                minimum_D_lower,
                minimum_N_lower,
                minimum_theta_numerator_lower,
                maximum_theta_dot_upper,
            )
        ):
            raise RuntimeError(f"{tree_id}: no certified angle leaf for extrema")
        angle_extrema: dict[str, str] | None = {
            "minimum_D_plus_lower": printed_ball(minimum_D_lower, bits),
            "minimum_N_plus_lower": printed_ball(minimum_N_lower, bits),
            "minimum_theta_numerator_lower": printed_ball(
                minimum_theta_numerator_lower, bits
            ),
            "maximum_theta_dot_upper": printed_ball(maximum_theta_dot_upper, bits),
            "theta_numerator_definition": "omega_fast_times_N_plus",
        }
    else:
        angle_extrema = None
    tree_payload: dict[str, Any] = {
        "tree_id": tree_id,
        "goal": goal,
        "coordinates": list(coordinates),
        "root_box": box_record(root_box, coordinates),
        "split_rule": "largest_normalized_width_then_coordinate_order_exact_midpoint",
        "node_count": len(nodes),
        "internal_count": internal_count,
        "terminal_count": terminal_count,
        "unresolved_count": 0,
        "maximum_depth": maximum_depth,
        "terminal_counts": dict(sorted(terminal_counts.items())),
        "angle_extrema": angle_extrema,
        "complete": True,
        "nodes": nodes,
        "content_hash_definition": (
            "sha256(canonical_json(tree_without_content_sha256))"
        ),
    }
    if len(nodes) != internal_count + terminal_count:
        raise RuntimeError(f"{tree_id}: inconsistent node accounting")
    tree_payload["content_sha256"] = sha256_bytes(
        canonical_json_bytes(tree_payload)
    )
    return tree_payload


def outer_containment_gates(model: Model, bits: int) -> dict[str, Any]:
    sqrt_two = point_ball(2).sqrt()
    warped_radius = 1 / (sqrt_two * model.pi)
    qplus_bound = (
        warped_radius
        + model.a * point_ball(EPSILON_CAP) * square_interval(warped_radius)
    ) / model.lambda_fast.sqrt()
    qminus_bound = point_ball(Fraction(6, 100)) / model.omega_slow
    angular_ceiling = 4 * model.pi / point_ball(PERIOD_MAX)
    values = {
        "qminus_bound": qminus_bound,
        "qplus_bound": qplus_bound,
        "pplus_bound": sqrt_two,
        "four_pi_over_period_max": angular_ceiling,
    }
    gates = {
        "qminus_bound_lt_0.015": qminus_bound.upper() < point_ball(Fraction(15, 1000)),
        "qplus_bound_lt_0.18": qplus_bound.upper() < point_ball(Fraction(18, 100)),
        "pplus_bound_lt_1.415": sqrt_two.upper() < point_ball(Fraction(1415, 1000)),
        "theta_ceiling_18_lt_four_pi_over_0.69": point_ball(18) < angular_ceiling.lower(),
    }
    return {
        "derivation": {
            "qminus": "r_minus<=0.06 implies |Q_minus|<=0.06/omega_minus",
            "qplus": "K=1 and exprel(s)>=1 imply |W|<=1/(sqrt(2)pi); triangle inequality for A Q=W+(a epsilon q1^2,0) and the fast singular direction gives the displayed bound",
            "pplus": "K=1 with nonnegative potential implies |P_plus|<=sqrt(2)",
            "winding": "theta_dot<18 and T<=0.69 imply Delta theta<4pi",
        },
        "values": {key: printed_ball(value, bits) for key, value in values.items()},
        "gates": gates,
        "all_pass": all(gates.values()),
    }


def project_relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def project_bound_path(value: Any, context: str) -> Path:
    if type(value) is not str or not value or value.startswith("/"):
        raise StaticCellContractError(f"{context}: canonical project-relative path required")
    if (
        "\x00" in value
        or "\\" in value
        or "//" in value
        or value.endswith("/")
        or any(component in ("", ".", "..") for component in value.split("/"))
    ):
        raise StaticCellContractError(f"{context}: unsafe project path")
    return require_canonical_absolute_path(ROOT / value, context)


def require_exact_object_keys(payload: Any, expected: set[str], context: str) -> dict[str, Any]:
    if type(payload) is not dict or set(payload) != expected:
        raise StaticCellContractError(f"{context}: exact top-level schema mismatch")
    return payload


def validate_bound_hash_map(
    payload: Any,
    expected_paths: set[str],
    context: str,
    captured_hashes: Mapping[str, str] | None = None,
) -> None:
    mapping = require_exact_object_keys(payload, expected_paths, context)
    for relative in sorted(expected_paths):
        expected_hash = mapping[relative]
        if type(expected_hash) is not str or SHA256_PATTERN.fullmatch(expected_hash) is None:
            raise StaticCellContractError(f"{context}: invalid SHA-256 for {relative}")
        actual_hash = (
            captured_hashes[relative]
            if captured_hashes is not None and relative in captured_hashes
            else sha256_file(project_bound_path(relative, context))
        )
        if actual_hash != expected_hash:
            raise StaticCellContractError(f"{context}: byte hash mismatch for {relative}")


def validate_l1_bundle() -> tuple[dict[str, str], dict[str, Any], str]:
    required = (*L1_RELEASE_CHAIN, PLAN)
    if any(not path.is_file() or path.is_symlink() for path in required):
        raise FileNotFoundError("accepted A4.12 five-object release chain is incomplete")
    images = {
        path: strict_json_image(path)
        for path in L1_RELEASE_CHAIN
    }
    summary, _ = images[L1_SUMMARY]
    manifest, _ = images[L1_MANIFEST]
    checker, _ = images[L1_CHECKER]
    postcheck, _ = images[L1_POSTCHECK]
    release, _ = images[L1_RELEASE]
    plan_raw = read_pinned_regular_bytes(PLAN)
    plan_payload = strict_json_bytes(plan_raw, PLAN)
    if type(plan_payload) is not dict:
        raise StaticCellContractError("accepted L1 plan root is not an object")
    captured_hashes = {
        project_relative(path): sha256_bytes(raw)
        for path, (_, raw) in images.items()
    }
    captured_hashes[project_relative(PLAN)] = sha256_bytes(plan_raw)
    require_exact_object_keys(summary, L1_SUMMARY_KEYS, "accepted L1 summary")
    require_exact_object_keys(manifest, L1_MANIFEST_KEYS, "accepted L1 manifest")
    require_exact_object_keys(checker, L1_CHECKER_KEYS, "accepted L1 checker")
    require_exact_object_keys(postcheck, L1_POSTCHECK_KEYS, "accepted L1 postcheck")
    require_exact_object_keys(release, L1_RELEASE_KEYS, "accepted L1 release")
    gates = {
        "summary": summary.get("protocol_id") == "R401-VAL-L1-V2"
        and summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and summary.get("final_status") is None
        and summary.get("claim_boundary") == L1_SUMMARY_BOUNDARY,
        "manifest": manifest.get("protocol_id") == "R401-VAL-L1-V2"
        and manifest.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and manifest.get("final_status") is None
        and manifest.get("capd_commit") == "731079217a9254ea2948d742df2b170895effe7f",
        "checker": checker.get("protocol_id") == "R401-VAL-L1-V2"
        and checker.get("checker_status") == "PASS"
        and checker.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and checker.get("final_status") is None
        and checker.get("job_failures") == []
        and checker.get("manifest_hash_failures") == []
        and checker.get("scope")
        == "independent exact-rational replay of archived Krawczyk arithmetic, plan coverage, bridge gluing, phase gates, and hashes; not an independent ODE integration",
        "postcheck": postcheck.get("protocol_id") == "R401-VAL-L1-V2"
        and postcheck.get("checker_status") == "PASS"
        and postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and postcheck.get("final_status") is None,
        "release": release.get("protocol_id") == "R401-VAL-L1-V2"
        and release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and release.get("final_status") is None
        and release.get("scope")
        == "Post-production provenance binding; uniqueness is only inside the frozen local primary boxes and guarded bridge hulls.",
    }
    if not all(gates.values()):
        raise RuntimeError(f"accepted A4.12 status gate failed: {gates}")
    manifest_files = manifest.get("files")
    if type(manifest_files) is not dict or len(manifest_files) != 417:
        raise StaticCellContractError("accepted L1 manifest exact file-count mismatch")
    plan_relative = project_relative(PLAN)
    if manifest_files.get(plan_relative) != captured_hashes[plan_relative]:
        raise StaticCellContractError("accepted L1 manifest does not bind final plan")
    validate_bound_hash_map(
        postcheck.get("files"),
        L1_POSTCHECK_FILES,
        "accepted L1 postcheck files",
        captured_hashes,
    )
    validate_bound_hash_map(
        release.get("files"),
        L1_RELEASE_FILES,
        "accepted L1 release files",
        captured_hashes,
    )
    actual = {
        project_relative(path): captured_hashes[project_relative(path)]
        for path in L1_RELEASE_CHAIN
    }
    return actual, plan_payload, captured_hashes[plan_relative]


def validate_l1_release_chain() -> dict[str, str]:
    return validate_l1_bundle()[0]


class ValidatedPlanRecord(dict[str, Any]):
    validated_source_bindings: dict[str, Any]


def source_bindings(plan_record: Mapping[str, Any] | None = None) -> dict[str, Any]:
    if isinstance(plan_record, ValidatedPlanRecord):
        bindings = plan_record.validated_source_bindings
        return {
            **bindings,
            "l1_release_chain_sha256": dict(bindings["l1_release_chain_sha256"]),
        }
    if not CHECKER.is_file() or CHECKER.is_symlink():
        raise StaticCellContractError("formal static checker source is unavailable")
    chain_hashes, plan_payload, plan_hash = validate_l1_bundle()
    del plan_payload
    return {
        "evaluator_sha256": sha256_file(RUNNER),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": plan_hash,
        "l1_release_chain_sha256": chain_hashes,
    }


def load_plan() -> dict[str, dict[str, Any]]:
    chain_hashes, payload, plan_hash = validate_l1_bundle()
    if not isinstance(payload, dict) or not isinstance(payload.get("slabs"), list):
        raise StaticCellContractError("L1 plan has no slab list")
    bindings = {
        "evaluator_sha256": sha256_file(RUNNER),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": plan_hash,
        "l1_release_chain_sha256": chain_hashes,
    }
    records: dict[str, dict[str, Any]] = {}
    for record in payload["slabs"]:
        if not isinstance(record, dict) or type(record.get("slab_id")) is not str:
            raise StaticCellContractError("L1 plan slab record is malformed")
        slab_id = record["slab_id"]
        if SLAB_PATTERN.fullmatch(slab_id) is None or slab_id in records:
            raise StaticCellContractError(f"invalid or duplicate slab id: {slab_id}")
        captured = ValidatedPlanRecord(record)
        captured.validated_source_bindings = bindings
        records[slab_id] = captured
    expected = [f"S{index:03d}" for index in range(51)]
    if list(records) != expected:
        raise StaticCellContractError("L1 plan is not the exact ordered 51-slab matrix")
    return records


def slab_epsilon(record: dict[str, Any]) -> tuple[Fraction, Fraction]:
    lower = Fraction(str(record["epsilon_lower"]))
    upper = Fraction(str(record["epsilon_upper"]))
    if not Fraction(0) <= lower < upper <= EPSILON_CAP:
        raise ValueError("slab epsilon interval lies outside [0,0.101]")
    return lower, upper


@dataclass(frozen=True)
class FrozenStaticInput:
    slab_id: str
    precision_bits: int
    epsilon_lower: str
    epsilon_upper: str
    matrix_id: str
    freeze_sha256: str
    run_config_sha256: str
    plan_record_sha256: str
    max_depth: int
    max_nodes_per_tree: int
    max_nodes_per_cell: int
    output: Path


def plan_record_sha256(record: dict[str, Any]) -> str:
    # ``ValidatedPlanRecord`` carries an out-of-band pinned provenance
    # attribute; only its exact JSON object image participates in this digest.
    return sha256_bytes(canonical_json_bytes(dict(record)))


def validate_frozen_input(arguments: argparse.Namespace) -> tuple[FrozenStaticInput, dict[str, Any]]:
    slab_id = arguments.slab_id
    if SLAB_PATTERN.fullmatch(slab_id) is None:
        raise StaticCellContractError("slab id must be S000 through S050")
    if type(arguments.precision_bits) is not int or arguments.precision_bits not in PRECISIONS:
        raise StaticCellContractError("precision must be exact integer 128 or 256")
    for label in ("max_depth", "max_nodes_per_tree", "max_nodes_per_cell"):
        value = getattr(arguments, label)
        if type(value) is not int or value <= 0:
            raise StaticCellContractError(f"{label} must be a positive exact integer")
    if arguments.max_nodes_per_cell < arguments.max_nodes_per_tree:
        raise StaticCellContractError("cell node budget cannot be below tree node budget")
    plan = load_plan()
    record = plan[slab_id]
    epsilon = slab_epsilon(record)
    if (
        type(record.get("epsilon_lower")) is not str
        or type(record.get("epsilon_upper")) is not str
        or arguments.epsilon_lower != record["epsilon_lower"]
        or arguments.epsilon_upper != record["epsilon_upper"]
    ):
        raise StaticCellContractError("epsilon text is not the canonical L1 plan echo")
    supplied_epsilon = (
        Fraction(arguments.epsilon_lower),
        Fraction(arguments.epsilon_upper),
    )
    if supplied_epsilon != epsilon:
        raise StaticCellContractError("epsilon echo does not match accepted L1 plan")
    expected_record_hash = plan_record_sha256(record)
    if arguments.plan_record_sha256 != expected_record_hash:
        raise StaticCellContractError("plan record hash mismatch")
    output = arguments.output
    if not output.is_absolute() or output.name != "proof.json":
        raise StaticCellContractError("output must be an absolute proof.json path")
    return (
        FrozenStaticInput(
            slab_id=slab_id,
            precision_bits=arguments.precision_bits,
            epsilon_lower=arguments.epsilon_lower,
            epsilon_upper=arguments.epsilon_upper,
            matrix_id=require_sha256(arguments.matrix_id, "matrix_id"),
            freeze_sha256=require_sha256(arguments.freeze_sha256, "freeze_sha256"),
            run_config_sha256=require_sha256(
                arguments.run_config_sha256, "run_config_sha256"
            ),
            plan_record_sha256=expected_record_hash,
            max_depth=arguments.max_depth,
            max_nodes_per_tree=arguments.max_nodes_per_tree,
            max_nodes_per_cell=arguments.max_nodes_per_cell,
            output=output,
        ),
        record,
    )


def common_payload(cell: FrozenStaticInput, status: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "artifact_role": ARTIFACT_ROLE,
        "authority": AUTHORITY,
        "scientific_licensing_enabled": False,
        "matrix_id": cell.matrix_id,
        "freeze_sha256": cell.freeze_sha256,
        "run_config_sha256": cell.run_config_sha256,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "evaluator_status": status,
        "slab_id": cell.slab_id,
        "precision_bits": cell.precision_bits,
        "epsilon": interval_record_exact(
            (Fraction(cell.epsilon_lower), Fraction(cell.epsilon_upper))
        ),
        "period_window": interval_record_exact((Fraction(64, 100), PERIOD_MAX)),
        "input_echo": {
            "slab_id": cell.slab_id,
            "precision_bits": cell.precision_bits,
            "epsilon_lower": cell.epsilon_lower,
            "epsilon_upper": cell.epsilon_upper,
            "matrix_id": cell.matrix_id,
            "freeze_sha256": cell.freeze_sha256,
            "run_config_sha256": cell.run_config_sha256,
            "plan_record_sha256": cell.plan_record_sha256,
            "max_depth": cell.max_depth,
            "max_nodes_per_tree": cell.max_nodes_per_tree,
            "max_nodes_per_cell": cell.max_nodes_per_cell,
        },
        "claim_boundary": CLAIM_BOUNDARY,
    }


def evaluate_cell(cell: FrozenStaticInput, plan_record: dict[str, Any]) -> dict[str, Any]:
    previous_precision = ctx.prec
    ctx.prec = cell.precision_bits
    try:
        model = build_model()
        epsilon = slab_epsilon(plan_record)
        budget = CellBudget(
            max_depth=cell.max_depth,
            max_nodes_per_tree=cell.max_nodes_per_tree,
            max_nodes_per_cell=cell.max_nodes_per_cell,
        )
        containment = outer_containment_gates(model, cell.precision_bits)
        if not containment["all_pass"]:
            raise StaticCellContractError("analytic outer-containment gate failed")
        trees = [
            build_tree(
                model,
                epsilon,
                bits=cell.precision_bits,
                tree_id="ANGLE",
                goal="ANGLE_COVER",
                root_box=ANGLE_ROOT,
                budget=budget,
            )
        ]
        for tree_id, root_box in SECTION_ROOTS.items():
            trees.append(
                build_tree(
                    model,
                    epsilon,
                    bits=cell.precision_bits,
                    tree_id=tree_id,
                    goal="SECTION_WINDOW_COVER",
                    root_box=root_box,
                    budget=budget,
                )
            )
        tree_by_id = {tree["tree_id"]: tree for tree in trees}
        low_ok = set(tree_by_id["SECTION_LOW"]["terminal_counts"]) <= {
            "ENERGY_EXCLUDED",
            "TUBE_EXCLUDED",
        }
        high_ok = set(tree_by_id["SECTION_HIGH"]["terminal_counts"]) <= {
            "ENERGY_EXCLUDED",
            "TUBE_EXCLUDED",
        }
        window_ok = tree_by_id["SECTION_WINDOW"]["terminal_counts"] == {
            "LANDING_CLOSED_WINDOW": 1
        }
        angle_ok = (
            tree_by_id["ANGLE"]["terminal_counts"].get("ANGLE_CERTIFIED", 0) > 0
            and set(tree_by_id["ANGLE"]["terminal_counts"])
            <= {"ANGLE_CERTIFIED", "ENERGY_EXCLUDED", "TUBE_EXCLUDED"}
        )
        if not (all(tree["complete"] for tree in trees) and low_ok and high_ok and window_ok and angle_ok):
            raise StaticCellContractError("tree terminal contract failed")
        payload = common_payload(cell, PASS_STATUS)
        payload.update(
            {
                "proof_complete": True,
                "outer_containment": containment,
                "trees": trees,
                "counts": {
                    "tree_count": len(trees),
                    "node_count": sum(int(tree["node_count"]) for tree in trees),
                    "internal_count": sum(int(tree["internal_count"]) for tree in trees),
                    "terminal_count": sum(
                        sum(tree["terminal_counts"].values()) for tree in trees
                    ),
                    "unresolved_count": 0,
                    "maximum_depth": max(int(tree["maximum_depth"]) for tree in trees),
                },
                # The plan record carries the exact L1 byte snapshot used to
                # derive this cell's epsilon interval.  Reusing that binding
                # here prevents a second PLAN read from mixing semantic bytes
                # from one image with provenance bytes from another.
                "source_bindings": source_bindings(plan_record),
                "proof_content_hash_definition": (
                    "sha256(canonical_json(proof_without_proof_content_sha256))"
                ),
            }
        )
        if payload["counts"]["node_count"] != budget.consumed_nodes:
            raise StaticCellContractError("cell node accounting mismatch")
        payload["proof_content_sha256"] = sha256_bytes(canonical_json_bytes(payload))
        return payload
    finally:
        ctx.prec = previous_precision


def nonpass_payload(
    cell: FrozenStaticInput,
    status: str,
    details: dict[str, Any],
) -> dict[str, Any]:
    payload = common_payload(cell, status)
    payload.update(
        {
            "proof_complete": False,
            "failure": details,
            "trees": [],
            "counts": {
                "tree_count": 0,
                "node_count": 0,
                "internal_count": 0,
                "terminal_count": 0,
                "unresolved_count": 1,
                "maximum_depth": None,
            },
            "proof_content_hash_definition": (
                "sha256(canonical_json(proof_without_proof_content_sha256))"
            ),
        }
    )
    payload["proof_content_sha256"] = sha256_bytes(canonical_json_bytes(payload))
    return payload


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slab-id", required=True)
    parser.add_argument("--precision-bits", required=True, type=canonical_precision)
    parser.add_argument("--epsilon-lower", required=True)
    parser.add_argument("--epsilon-upper", required=True)
    parser.add_argument("--matrix-id", required=True)
    parser.add_argument("--freeze-sha256", required=True)
    parser.add_argument("--run-config-sha256", required=True)
    parser.add_argument("--plan-record-sha256", required=True)
    parser.add_argument("--max-depth", type=canonical_positive_int, default=DEFAULT_MAX_DEPTH)
    parser.add_argument(
        "--max-nodes-per-tree",
        type=canonical_positive_int,
        default=DEFAULT_MAX_NODES_PER_TREE,
    )
    parser.add_argument(
        "--max-nodes-per-cell",
        type=canonical_positive_int,
        default=DEFAULT_MAX_NODES_PER_CELL,
    )
    parser.add_argument("--output", required=True, type=lexical_absolute_output)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        cell, plan_record = validate_frozen_input(arguments)
    except Exception as error:
        print(f"INVALID_STATIC_PROOF_CONTRACT: {error}", file=sys.stderr)
        return 5
    try:
        proof = evaluate_cell(cell, plan_record)
        return_code = 0
    except StaticCellLimit as error:
        proof = nonpass_payload(cell, error.status, error.details)
        return_code = 2
    except StaticCellContractError as error:
        proof = nonpass_payload(
            cell,
            "INVALID_STATIC_PROOF_CONTRACT",
            {"reason": str(error)},
        )
        return_code = 5
    except Exception as error:
        proof = nonpass_payload(
            cell,
            "STATIC_INTERVAL_FAIL",
            {"error_type": type(error).__name__, "reason": str(error)},
        )
        return_code = 3
    try:
        write_once(cell.output, canonical_json_bytes(proof))
    except Exception as error:
        print(f"INVALID_STATIC_PROOF_CONTRACT: {error}", file=sys.stderr)
        return 5
    print(f"evaluator_status={proof['evaluator_status']}")
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
