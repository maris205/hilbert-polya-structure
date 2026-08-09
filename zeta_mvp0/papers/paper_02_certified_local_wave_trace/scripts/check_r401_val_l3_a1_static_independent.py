#!/usr/bin/env python3
"""Independently replay formal R401-VAL-L3-A1 static proof objects.

The checker deliberately duplicates the exact model reconstruction, Arb
interval formulas, terminal predicates, and rational bisection rules.  It
does not import the static evaluator or scheduler.  A successful full-matrix
replay may assign only the component value
``PASS_STATIC_PHASE_ANCHOR_ALL_SLABS``; all programme-level fields remain
null, and the composite checker must independently bind this result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve()
EVALUATOR = ROOT / "scripts/evaluate_r401_val_l3_a1_static_cell.py"
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
CELL_ROLE = "STATIC_CELL_PROOF"
CHECKER_ROLE = "STATIC_INDEPENDENT_CHECKER"
PASS_STATUS = "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"
CELL_PASS_STATUS = "STATIC_CELL_CERTIFIED"
SLABS = tuple(f"S{index:03d}" for index in range(51))
PRECISIONS = (128, 256)
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
EXPECTED_DERIVATION = {
    "qminus": "r_minus<=0.06 implies |Q_minus|<=0.06/omega_minus",
    "qplus": "K=1 and exprel(s)>=1 imply |W|<=1/(sqrt(2)pi); triangle inequality for A Q=W+(a epsilon q1^2,0) and the fast singular direction gives the displayed bound",
    "pplus": "K=1 with nonnegative potential implies |P_plus|<=sqrt(2)",
    "winding": "theta_dot<18 and T<=0.69 imply Delta theta<4pi",
}

CLAIM_BOUNDARY = (
    "all-slab static phase-anchor component only, conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no branch-tube, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)
CELL_CLAIM_BOUNDARY = (
    "producer-only static phase-anchor cell conditional on K=1 and "
    "whole-orbit residence in r_minus<0.06; no component, composite, "
    "global-orbit, trace-formula, Hilbert-Polya, zeta-zero, or RH authority"
)


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def exact_keys(payload: dict[str, Any], expected: set[str], context: str) -> None:
    actual = set(payload)
    require(
        actual == expected,
        f"{context}: keys differ; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}",
    )


def require_exact_int(
    value: Any,
    context: str,
    *,
    expected: int | None = None,
    minimum: int | None = None,
) -> int:
    require(type(value) is int, f"{context}: expected an exact JSON integer")
    if expected is not None:
        require(value == expected, f"{context}: expected {expected}, found {value}")
    if minimum is not None:
        require(value >= minimum, f"{context}: integer below {minimum}")
    return value


def json_exact_equal(actual: Any, expected: Any) -> bool:
    """Recursive equality that never identifies bool, int, and float."""

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
    require(json_exact_equal(actual, expected), f"{context}: exact JSON value mismatch")


def canonical_json_bytes(payload: Any) -> bytes:
    return (
        json.dumps(
            payload,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
    )


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(read_pinned_regular_bytes(path))


def require_canonical_absolute_path(value: str | os.PathLike[str], context: str) -> Path:
    text = os.fspath(value)
    require(text.startswith("/") and not text.startswith("//"), f"{context}: one POSIX root slash required")
    require(
        "\x00" not in text
        and "\\" not in text
        and "//" not in text[1:]
        and not text.endswith("/"),
        f"{context}: non-canonical path spelling",
    )
    require(
        all(component not in ("", ".", "..") for component in text[1:].split("/")),
        f"{context}: dot or empty path component",
    )
    path = Path(text)
    require(path.is_absolute() and os.path.abspath(text) == text, f"{context}: normalized path alias")
    return path


def canonical_absolute_argument(value: str) -> Path:
    try:
        return require_canonical_absolute_path(value, "checker CLI path")
    except CheckError as error:
        raise argparse.ArgumentTypeError(str(error)) from error


def _open_directory_fd(path: Path) -> int:
    path = require_canonical_absolute_path(path, "checker directory path")
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
    path = require_canonical_absolute_path(path, "checker input path")
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        directory_fd = _open_directory_fd(path.parent)
    except OSError as error:
        raise CheckError(f"{path}: cannot open pinned parent: {error}") from error
    parent_before = os.fstat(directory_fd)
    descriptor: int | None = None
    try:
        descriptor = os.open(path.name, os.O_RDONLY | nofollow, dir_fd=directory_fd)
    except OSError as error:
        os.close(directory_fd)
        raise CheckError(f"{path}: cannot open pinned regular file: {error}") from error
    try:
        before = os.fstat(descriptor)
        require(stat.S_ISREG(before.st_mode), f"{path}: not a regular file")
        require(before.st_nlink == 1, f"{path}: hard-link alias rejected")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(descriptor)
        require(
            (
                before.st_dev,
                before.st_ino,
                before.st_size,
                before.st_mtime_ns,
                before.st_ctime_ns,
            )
            == (
                after.st_dev,
                after.st_ino,
                after.st_size,
                after.st_mtime_ns,
                after.st_ctime_ns,
            ),
            f"{path}: file changed during pinned read",
        )
        raw = b"".join(chunks)
        require(len(raw) == before.st_size, f"{path}: pinned read size mismatch")
        directory_entry = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        require(
            (directory_entry.st_dev, directory_entry.st_ino)
            == (before.st_dev, before.st_ino),
            f"{path}: directory entry changed during pinned read",
        )
        try:
            replay_parent_fd = _open_directory_fd(path.parent)
        except OSError as error:
            raise CheckError(f"{path}: lexical parent changed during pinned read: {error}") from error
        try:
            replay_parent = os.fstat(replay_parent_fd)
            lexical_entry = os.stat(
                path.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
        except OSError as error:
            raise CheckError(f"{path}: lexical path changed during pinned read: {error}") from error
        finally:
            os.close(replay_parent_fd)
        require(
            (lexical_entry.st_dev, lexical_entry.st_ino)
            == (before.st_dev, before.st_ino)
            and (replay_parent.st_dev, replay_parent.st_ino)
            == (parent_before.st_dev, parent_before.st_ino),
            f"{path}: lexical path no longer names pinned inode",
        )
        return raw
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_fd)


def write_once(path: Path, payload: bytes) -> None:
    path = require_canonical_absolute_path(path, "checker output path")
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    try:
        directory_fd = _open_directory_fd(path.parent)
    except OSError as error:
        raise CheckError(f"checker output parent failed: {error}") from error
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
            require(written > 0, "checker short write")
            view = view[written:]
        os.fsync(descriptor)
        info = os.fstat(descriptor)
        require(
            stat.S_ISREG(info.st_mode)
            and info.st_nlink == 1
            and info.st_size == len(payload),
            "checker output publication mismatch",
        )
        entry = os.stat(path.name, dir_fd=directory_fd, follow_symlinks=False)
        require(
            (entry.st_dev, entry.st_ino) == (info.st_dev, info.st_ino),
            "checker output directory entry mismatch",
        )
        try:
            replay_parent_fd = _open_directory_fd(path.parent)
        except OSError as error:
            raise CheckError(f"checker output parent changed: {error}") from error
        try:
            replay_parent = os.fstat(replay_parent_fd)
            replay_entry = os.stat(
                path.name,
                dir_fd=replay_parent_fd,
                follow_symlinks=False,
            )
            require(
                (replay_parent.st_dev, replay_parent.st_ino)
                == (parent_before.st_dev, parent_before.st_ino)
                and (replay_entry.st_dev, replay_entry.st_ino)
                == (info.st_dev, info.st_ino),
                "checker output lexical replay mismatch",
            )
            os.fsync(replay_parent_fd)
        finally:
            os.close(replay_parent_fd)
        os.fsync(directory_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_fd)


def strict_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise CheckError(f"forbidden non-finite JSON number {value}")
    return parsed


def load_canonical_json_with_raw(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = read_pinned_regular_bytes(path)

    def reject_constant(value: str) -> None:
        raise CheckError(f"{path.name}: forbidden non-finite JSON constant {value}")

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        answer: dict[str, Any] = {}
        for key, value in pairs:
            if key in answer:
                raise CheckError(f"{path.name}: duplicate JSON key {key!r}")
            answer[key] = value
        return answer

    try:
        payload = json.loads(
            raw,
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
            parse_float=strict_float,
        )
    except CheckError:
        raise
    except Exception as error:
        raise CheckError(f"{path.name}: invalid JSON: {error}") from error
    require(isinstance(payload, dict), f"{path.name}: JSON root is not an object")
    require(raw == canonical_json_bytes(payload), f"{path.name}: JSON is not canonical")
    return payload, raw


def load_canonical_json(path: Path) -> dict[str, Any]:
    return load_canonical_json_with_raw(path)[0]


def parse_fraction_record(payload: Any, context: str) -> Fraction:
    require(isinstance(payload, dict), f"{context}: fraction is not an object")
    exact_keys(payload, {"numerator", "denominator"}, context)
    numerator_text = payload["numerator"]
    denominator_text = payload["denominator"]
    require(
        isinstance(numerator_text, str) and isinstance(denominator_text, str),
        f"{context}: numerator/denominator must be strings",
    )
    require(
        numerator_text == str(int(numerator_text)),
        f"{context}: numerator is not canonical",
    )
    require(
        denominator_text == str(int(denominator_text)),
        f"{context}: denominator is not canonical",
    )
    numerator = int(numerator_text)
    denominator = int(denominator_text)
    require(denominator > 0, f"{context}: denominator is not positive")
    require(math.gcd(numerator, denominator) == 1, f"{context}: fraction is not reduced")
    return Fraction(numerator, denominator)


def parse_interval_record(payload: Any, context: str) -> tuple[Fraction, Fraction]:
    require(isinstance(payload, list) and len(payload) == 2, f"{context}: interval shape")
    lower = parse_fraction_record(payload[0], f"{context}.lower")
    upper = parse_fraction_record(payload[1], f"{context}.upper")
    require(lower <= upper, f"{context}: reversed interval")
    return lower, upper


def parse_box_record(
    payload: Any,
    coordinates: tuple[str, ...],
    context: str,
) -> dict[str, tuple[Fraction, Fraction]]:
    require(isinstance(payload, dict), f"{context}: box is not an object")
    exact_keys(payload, set(coordinates), context)
    return {
        coordinate: parse_interval_record(payload[coordinate], f"{context}.{coordinate}")
        for coordinate in coordinates
    }


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def point_ball(value: Fraction | int) -> arb:
    return arb(as_fmpq(Fraction(value)))


def interval_ball(interval: tuple[Fraction, Fraction]) -> arb:
    lower, upper = interval
    return arb(as_fmpq((lower + upper) / 2), as_fmpq((upper - lower) / 2))


def square_enclosure(value: arb) -> arb:
    lower = value.lower()
    upper = value.upper()
    zero = arb(0)
    if lower >= zero:
        return arb.union(lower * lower, upper * upper).nonnegative_part()
    if upper <= zero:
        return arb.union(upper * upper, lower * lower).nonnegative_part()
    maximum = max(abs(lower).upper(), abs(upper).upper())
    return arb.union(zero, maximum * maximum).nonnegative_part()


def exprel_enclosure(value: arb) -> arb:
    require(value.lower() >= arb(0), "replay exprel input is not nonnegative")
    order = 16
    result = arb(1)
    summand = arb(1)
    for index in range(1, order + 1):
        summand = summand * value / (index + 1)
        result += summand
    radius = abs(value).upper()
    factorial = math.factorial(order + 2)
    error = radius ** (order + 1) * radius.exp() / factorial
    return result + arb(0, error.upper())


@dataclass(frozen=True)
class IndependentModel:
    a: arb
    c: arb
    pi: arb
    lambda_slow: arb
    lambda_fast: arb
    omega_slow: arb
    omega_fast: arb
    slow_basis: tuple[arb, arb]
    fast_basis: tuple[arb, arb]


def independent_model() -> IndependentModel:
    a = point_ball(Fraction(51, 50))
    pi_value = arb.pi()
    c = 2 * ((1 + a).sqrt() - 1)
    discriminant = c * (c * c + 4).sqrt()
    lambda_slow = (c * c + 2 - discriminant) / 2
    lambda_fast = (c * c + 2 + discriminant) / 2
    slow_raw = (1 - lambda_slow, -c)
    fast_raw = (lambda_fast - 1, c)
    slow_length = (
        square_enclosure(slow_raw[0]) + square_enclosure(slow_raw[1])
    ).sqrt()
    fast_length = (
        square_enclosure(fast_raw[0]) + square_enclosure(fast_raw[1])
    ).sqrt()
    return IndependentModel(
        a=a,
        c=c,
        pi=pi_value,
        lambda_slow=lambda_slow,
        lambda_fast=lambda_fast,
        omega_slow=2 * pi_value * lambda_slow.sqrt(),
        omega_fast=2 * pi_value * lambda_fast.sqrt(),
        slow_basis=(slow_raw[0] / slow_length, slow_raw[1] / slow_length),
        fast_basis=(fast_raw[0] / fast_length, fast_raw[1] / fast_length),
    )


@dataclass(frozen=True)
class ReplayMetrics:
    energy: arb
    tube_squared: arb
    denominator: arb | None
    N_plus: arb | None
    numerator: arb | None
    angular_velocity: arb | None


def recompute_metrics(
    model: IndependentModel,
    epsilon_interval: tuple[Fraction, Fraction],
    box: dict[str, tuple[Fraction, Fraction]],
    *,
    section: bool,
) -> ReplayMetrics:
    epsilon = interval_ball(epsilon_interval)
    qm = interval_ball(box["qminus"])
    qp = interval_ball(box["qplus"])
    pm = interval_ball(box["pminus"])
    pp = arb(0) if section else interval_ball(box["pplus"])

    q1 = model.slow_basis[0] * qm + model.fast_basis[0] * qp
    q2 = model.slow_basis[1] * qm + model.fast_basis[1] * qp
    w1 = -model.c * q1 - q2 - model.a * epsilon * square_enclosure(q1)
    w2 = q1
    w_norm_squared = square_enclosure(w1) + square_enclosure(w2)
    # Positivity is an exact structural fact; remove only the artificial
    # negative sliver introduced by midpoint-radius dependency loss.
    s = (
        model.pi * square_enclosure(epsilon) * w_norm_squared
    ).nonnegative_part()
    potential = (
        2 * model.pi * model.pi * w_norm_squared * exprel_enclosure(s)
    )
    energy = (square_enclosure(pm) + square_enclosure(pp)) / 2 + potential
    tube_squared = square_enclosure(model.omega_slow * qm) + square_enclosure(pm)
    if section:
        return ReplayMetrics(energy, tube_squared, None, None, None, None)

    dw1_dq1 = -model.c - 2 * model.a * epsilon * q1
    radial_factor = 4 * model.pi * model.pi * s.exp()
    grad_q1 = radial_factor * (dw1_dq1 * w1 + w2)
    grad_q2 = -radial_factor * w1
    grad_fast = model.fast_basis[0] * grad_q1 + model.fast_basis[1] * grad_q2
    denominator = square_enclosure(model.omega_fast * qp) + square_enclosure(pp)
    N_plus = square_enclosure(pp) + qp * grad_fast
    # Numerator of theta_dot: omega_fast * N_plus.
    numerator = model.omega_fast * N_plus
    angular_velocity = numerator / denominator
    return ReplayMetrics(
        energy,
        tube_squared,
        denominator,
        N_plus,
        numerator,
        angular_velocity,
    )


def expected_terminal(
    metrics: ReplayMetrics,
    box: dict[str, tuple[Fraction, Fraction]],
    goal: str,
) -> str | None:
    if metrics.tube_squared.lower() > point_ball(TUBE_RADIUS_SQUARED):
        return "TUBE_EXCLUDED"
    if metrics.energy.upper() < point_ball(1) or metrics.energy.lower() > point_ball(1):
        return "ENERGY_EXCLUDED"
    if goal == "ANGLE_COVER":
        assert metrics.denominator is not None
        assert metrics.N_plus is not None
        assert metrics.numerator is not None
        assert metrics.angular_velocity is not None
        if (
            metrics.denominator.lower() > arb(0)
            and metrics.N_plus.lower() > arb(0)
            and metrics.numerator.lower() > arb(0)
            and metrics.angular_velocity.upper() < point_ball(ANGLE_CEILING)
        ):
            return "ANGLE_CERTIFIED"
        return None
    if goal == "SECTION_WINDOW_COVER":
        lower, upper = box["qplus"]
        if lower >= Fraction(12, 100) and upper <= Fraction(17, 100):
            return "LANDING_CLOSED_WINDOW"
    return None


def independently_selected_coordinate(
    box: dict[str, tuple[Fraction, Fraction]],
    root_box: dict[str, tuple[Fraction, Fraction]],
    coordinates: tuple[str, ...],
) -> str:
    best = coordinates[0]
    best_width = Fraction(-1)
    for coordinate in coordinates:
        width = (box[coordinate][1] - box[coordinate][0]) / (
            root_box[coordinate][1] - root_box[coordinate][0]
        )
        if width > best_width:
            best = coordinate
            best_width = width
    return best


def split_exactly(
    box: dict[str, tuple[Fraction, Fraction]], coordinate: str
) -> tuple[Fraction, dict[str, tuple[Fraction, Fraction]], dict[str, tuple[Fraction, Fraction]]]:
    lower, upper = box[coordinate]
    midpoint = (lower + upper) / 2
    left = dict(box)
    right = dict(box)
    left[coordinate] = (lower, midpoint)
    right[coordinate] = (midpoint, upper)
    return midpoint, left, right


def decisive_values(metrics: ReplayMetrics, classification: str) -> dict[str, arb]:
    if classification == "TUBE_EXCLUDED":
        return {"tube_squared": metrics.tube_squared}
    if classification == "ENERGY_EXCLUDED":
        return {"energy": metrics.energy}
    if classification == "ANGLE_CERTIFIED":
        assert metrics.denominator is not None
        assert metrics.N_plus is not None
        assert metrics.numerator is not None
        assert metrics.angular_velocity is not None
        return {
            "D_plus": metrics.denominator,
            "N_plus": metrics.N_plus,
            "theta_numerator": metrics.numerator,
            "theta_dot": metrics.angular_velocity,
        }
    if classification == "LANDING_CLOSED_WINDOW":
        return {}
    raise CheckError(f"unknown terminal class {classification}")


def verify_printed_intervals(
    stored: Any,
    recomputed: dict[str, arb],
    context: str,
) -> int:
    require(isinstance(stored, dict), f"{context}: decisive_intervals not object")
    exact_keys(stored, set(recomputed), context)
    checks = 0
    for key, value in recomputed.items():
        text = stored[key]
        require(isinstance(text, str), f"{context}.{key}: not text")
        try:
            printed = arb(text)
        except Exception as error:
            raise CheckError(f"{context}.{key}: invalid Arb text: {error}") from error
        require(
            printed.contains(value),
            f"{context}.{key}: printed interval does not contain recomputation",
        )
        checks += 1
    return checks


def replay_tree(
    payload: Any,
    epsilon: tuple[Fraction, Fraction],
    model: IndependentModel,
    expected_tree_id: str,
    expected_root: dict[str, tuple[Fraction, Fraction]],
) -> dict[str, Any]:
    require(isinstance(payload, dict), f"{expected_tree_id}: tree not object")
    exact_keys(
        payload,
        {
            "tree_id",
            "goal",
            "coordinates",
            "root_box",
            "split_rule",
            "node_count",
            "internal_count",
            "terminal_count",
            "unresolved_count",
            "maximum_depth",
            "terminal_counts",
            "angle_extrema",
            "complete",
            "nodes",
            "content_hash_definition",
            "content_sha256",
        },
        expected_tree_id,
    )
    require(
        payload["content_hash_definition"]
        == "sha256(canonical_json(tree_without_content_sha256))",
        f"{expected_tree_id}: content-hash definition",
    )
    content_sha256 = payload["content_sha256"]
    require(
        isinstance(content_sha256, str)
        and len(content_sha256) == 64
        and all(character in "0123456789abcdef" for character in content_sha256),
        f"{expected_tree_id}: malformed content hash",
    )
    without_content_hash = dict(payload)
    del without_content_hash["content_sha256"]
    require(
        content_sha256 == sha256_bytes(canonical_json_bytes(without_content_hash)),
        f"{expected_tree_id}: content hash mismatch",
    )
    require(payload["tree_id"] == expected_tree_id, f"{expected_tree_id}: id mismatch")
    goal = payload["goal"]
    require(goal in {"ANGLE_COVER", "SECTION_WINDOW_COVER"}, f"{expected_tree_id}: goal")
    coordinates = ANGLE_COORDINATES if goal == "ANGLE_COVER" else SECTION_COORDINATES
    require(payload["coordinates"] == list(coordinates), f"{expected_tree_id}: coordinates")
    require(
        payload["split_rule"]
        == "largest_normalized_width_then_coordinate_order_exact_midpoint",
        f"{expected_tree_id}: split rule",
    )
    root = parse_box_record(payload["root_box"], coordinates, f"{expected_tree_id}.root")
    require(root == expected_root, f"{expected_tree_id}: unexpected root geometry")
    nodes = payload["nodes"]
    require(isinstance(nodes, list) and nodes, f"{expected_tree_id}: empty nodes")
    require_exact_int(
        payload["node_count"],
        f"{expected_tree_id}.node_count",
        expected=len(nodes),
    )
    require_exact_int(
        payload["maximum_depth"],
        f"{expected_tree_id}.maximum_depth",
        minimum=0,
    )
    require_exact_int(payload["internal_count"], f"{expected_tree_id}.internal_count", minimum=0)
    require_exact_int(payload["terminal_count"], f"{expected_tree_id}.terminal_count", minimum=1)
    require_exact_int(
        payload["unresolved_count"],
        f"{expected_tree_id}.unresolved_count",
        expected=0,
    )
    require(isinstance(payload["terminal_counts"], dict), f"{expected_tree_id}: terminal counts object")
    for terminal_name, count in payload["terminal_counts"].items():
        require(isinstance(terminal_name, str), f"{expected_tree_id}: terminal name type")
        require_exact_int(count, f"{expected_tree_id}.terminal_counts.{terminal_name}", minimum=0)
    require(payload["complete"] is True, f"{expected_tree_id}: incomplete")
    index = 0
    terminal_counts: dict[str, int] = {}
    internal_count = 0
    maximum_depth = 0
    interval_checks = 0
    minimum_D_lower: arb | None = None
    minimum_N_lower: arb | None = None
    minimum_theta_numerator_lower: arb | None = None
    maximum_theta_dot_upper: arb | None = None

    def replay(
        node_id: str,
        parent_id: str | None,
        depth: int,
        box: dict[str, tuple[Fraction, Fraction]],
    ) -> None:
        nonlocal index, maximum_depth, interval_checks, internal_count
        nonlocal minimum_D_lower, minimum_N_lower
        nonlocal minimum_theta_numerator_lower, maximum_theta_dot_upper
        require(index < len(nodes), f"{expected_tree_id}: missing node {node_id}")
        node = nodes[index]
        index += 1
        require(isinstance(node, dict), f"{node_id}: node is not object")
        maximum_depth = max(maximum_depth, depth)
        require(node.get("node_id") == node_id, f"{node_id}: node id mismatch")
        require(node.get("parent_id") == parent_id, f"{node_id}: parent mismatch")
        require_exact_int(node.get("depth"), f"{node_id}.depth", expected=depth)
        metrics = recompute_metrics(
            model,
            epsilon,
            box,
            section=goal != "ANGLE_COVER",
        )
        terminal = expected_terminal(metrics, box, goal)
        if terminal is not None:
            exact_keys(
                node,
                {"node_id", "parent_id", "depth", "classification", "decisive_intervals"},
                node_id,
            )
            require(node["classification"] == terminal, f"{node_id}: terminal class mismatch")
            interval_checks += verify_printed_intervals(
                node["decisive_intervals"],
                decisive_values(metrics, terminal),
                f"{node_id}.decisive_intervals",
            )
            if terminal == "ANGLE_CERTIFIED":
                assert metrics.denominator is not None
                assert metrics.N_plus is not None
                assert metrics.numerator is not None
                assert metrics.angular_velocity is not None
                D_lower = metrics.denominator.lower()
                N_lower = metrics.N_plus.lower()
                numerator_lower = metrics.numerator.lower()
                theta_upper = metrics.angular_velocity.upper()
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
            terminal_counts[terminal] = terminal_counts.get(terminal, 0) + 1
            return

        exact_keys(
            node,
            {"node_id", "parent_id", "depth", "classification", "split_coordinate", "split_point"},
            node_id,
        )
        require(node["classification"] == "SPLIT", f"{node_id}: expected split")
        internal_count += 1
        coordinate = independently_selected_coordinate(box, root, coordinates)
        require(node["split_coordinate"] == coordinate, f"{node_id}: split coordinate")
        midpoint, left, right = split_exactly(box, coordinate)
        recorded_midpoint = parse_fraction_record(node["split_point"], f"{node_id}.split_point")
        require(recorded_midpoint == midpoint, f"{node_id}: non-dyadic split geometry")
        replay(node_id + "0", node_id, depth + 1, left)
        replay(node_id + "1", node_id, depth + 1, right)

    replay(expected_tree_id, None, 0, root)
    require(index == len(nodes), f"{expected_tree_id}: unreachable trailing nodes")
    require_exact_int(
        payload["maximum_depth"],
        f"{expected_tree_id}.maximum_depth",
        expected=maximum_depth,
    )
    require_json_exact(
        payload["terminal_counts"],
        dict(sorted(terminal_counts.items())),
        f"{expected_tree_id}.terminal_counts",
    )
    terminal_count = sum(terminal_counts.values())
    require_exact_int(
        payload["internal_count"],
        f"{expected_tree_id}.internal_count",
        expected=internal_count,
    )
    require_exact_int(
        payload["terminal_count"],
        f"{expected_tree_id}.terminal_count",
        expected=terminal_count,
    )
    require(len(nodes) == internal_count + terminal_count, f"{expected_tree_id}: node accounting")
    if goal == "ANGLE_COVER":
        require(
            all(
                value is not None
                for value in (
                    minimum_D_lower,
                    minimum_N_lower,
                    minimum_theta_numerator_lower,
                    maximum_theta_dot_upper,
                )
            ),
            f"{expected_tree_id}: missing recomputed angle extrema",
        )
        stored_extrema = payload["angle_extrema"]
        require(isinstance(stored_extrema, dict), f"{expected_tree_id}: extrema object")
        exact_keys(
            stored_extrema,
            {
                "minimum_D_plus_lower",
                "minimum_N_plus_lower",
                "minimum_theta_numerator_lower",
                "maximum_theta_dot_upper",
                "theta_numerator_definition",
            },
            f"{expected_tree_id}.angle_extrema",
        )
        require(
            stored_extrema["theta_numerator_definition"] == "omega_fast_times_N_plus",
            f"{expected_tree_id}: theta numerator definition",
        )
        interval_checks += verify_printed_intervals(
            {
                key: value
                for key, value in stored_extrema.items()
                if key != "theta_numerator_definition"
            },
            {
                "minimum_D_plus_lower": minimum_D_lower,
                "minimum_N_plus_lower": minimum_N_lower,
                "minimum_theta_numerator_lower": minimum_theta_numerator_lower,
                "maximum_theta_dot_upper": maximum_theta_dot_upper,
            },
            f"{expected_tree_id}.angle_extrema",
        )
    else:
        require(payload["angle_extrema"] is None, f"{expected_tree_id}: unexpected angle extrema")
    return {
        "tree_id": expected_tree_id,
        "node_count": len(nodes),
        "internal_count": internal_count,
        "terminal_count": terminal_count,
        "unresolved_count": 0,
        "terminal_counts": terminal_counts,
        "interval_checks": interval_checks,
        "maximum_depth": maximum_depth,
        "content_sha256": content_sha256,
        "angle_extrema": payload["angle_extrema"],
    }


def verify_outer_containment(
    payload: Any,
    model: IndependentModel,
    bits: int,
    context: str,
) -> int:
    require(isinstance(payload, dict), f"{context}: outer containment not object")
    exact_keys(payload, {"derivation", "values", "gates", "all_pass"}, context)
    require(payload["derivation"] == EXPECTED_DERIVATION, f"{context}: derivation text")
    sqrt_two = point_ball(2).sqrt()
    w_bound = 1 / (sqrt_two * model.pi)
    qplus_bound = (
        w_bound + model.a * point_ball(EPSILON_CAP) * square_enclosure(w_bound)
    ) / model.lambda_fast.sqrt()
    qminus_bound = point_ball(Fraction(6, 100)) / model.omega_slow
    winding_bound = 4 * model.pi / point_ball(PERIOD_MAX)
    values = {
        "qminus_bound": qminus_bound,
        "qplus_bound": qplus_bound,
        "pplus_bound": sqrt_two,
        "four_pi_over_period_max": winding_bound,
    }
    expected_gates = {
        "qminus_bound_lt_0.015": qminus_bound.upper() < point_ball(Fraction(15, 1000)),
        "qplus_bound_lt_0.18": qplus_bound.upper() < point_ball(Fraction(18, 100)),
        "pplus_bound_lt_1.415": sqrt_two.upper() < point_ball(Fraction(1415, 1000)),
        "theta_ceiling_18_lt_four_pi_over_0.69": point_ball(18) < winding_bound.lower(),
    }
    require_json_exact(payload["gates"], expected_gates, f"{context}.gates")
    require(payload["all_pass"] is True and all(expected_gates.values()), f"{context}: gate failure")
    return verify_printed_intervals(payload["values"], values, f"{context}.values")


def load_strict_json_object_from_bytes(raw: bytes, path: Path) -> dict[str, Any]:
    """Parse one already-pinned byte image as a strict JSON object."""

    def reject_constant(value: str) -> None:
        raise CheckError(f"{path.name}: forbidden non-finite JSON constant {value}")

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        answer: dict[str, Any] = {}
        for key, value in pairs:
            if key in answer:
                raise CheckError(f"{path.name}: duplicate JSON key {key!r}")
            answer[key] = value
        return answer

    try:
        payload = json.loads(
            raw,
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
            parse_float=strict_float,
        )
    except CheckError:
        raise
    except Exception as error:
        raise CheckError(f"{path.name}: invalid JSON: {error}") from error
    require(isinstance(payload, dict), f"{path.name}: root is not an object")
    return payload


def load_strict_json_object(path: Path) -> dict[str, Any]:
    return load_strict_json_object_with_raw(path)[0]


def load_strict_json_object_with_raw(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = read_pinned_regular_bytes(path)
    return load_strict_json_object_from_bytes(raw, path), raw


def project_relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def project_bound_path(value: Any, context: str) -> Path:
    require(type(value) is str and value and not value.startswith("/"), f"{context}: project-relative path")
    require(
        "\x00" not in value
        and "\\" not in value
        and "//" not in value
        and not value.endswith("/")
        and all(component not in ("", ".", "..") for component in value.split("/")),
        f"{context}: unsafe project path",
    )
    return require_canonical_absolute_path(ROOT / value, context)


def validate_bound_hash_map(
    payload: Any,
    expected_paths: set[str],
    context: str,
    captured_hashes: dict[str, str] | None = None,
) -> None:
    require(isinstance(payload, dict), f"{context}: hash map is not object")
    exact_keys(payload, expected_paths, context)
    for relative in sorted(expected_paths):
        expected_hash = payload[relative]
        require(
            type(expected_hash) is str
            and len(expected_hash) == 64
            and all(character in "0123456789abcdef" for character in expected_hash),
            f"{context}: invalid SHA-256 for {relative}",
        )
        actual_hash = (
            captured_hashes[relative]
            if captured_hashes is not None and relative in captured_hashes
            else sha256_file(project_bound_path(relative, context))
        )
        require(
            actual_hash == expected_hash,
            f"{context}: byte hash mismatch for {relative}",
        )


def independently_validate_l1_bundle() -> tuple[dict[str, str], dict[str, Any], str]:
    """Replay the accepted L1 chain and return its captured PLAN image.

    The parsed slab semantics and the PLAN digest deliberately come from the
    same pinned byte snapshot.  Callers must propagate the returned bindings
    rather than reopen PLAN during the same proof verification.
    """

    images = {
        path: load_strict_json_object_with_raw(path)
        for path in L1_RELEASE_CHAIN
    }
    summary, _ = images[L1_SUMMARY]
    manifest, _ = images[L1_MANIFEST]
    checker, _ = images[L1_CHECKER]
    postcheck, _ = images[L1_POSTCHECK]
    release, _ = images[L1_RELEASE]
    plan_raw = read_pinned_regular_bytes(PLAN)
    plan_payload = load_strict_json_object_from_bytes(plan_raw, PLAN)
    captured_hashes = {
        project_relative(path): sha256_bytes(raw)
        for path, (_, raw) in images.items()
    }
    captured_hashes[project_relative(PLAN)] = sha256_bytes(plan_raw)
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
        and manifest.get("capd_commit") == "731079217a9254ea2948d742df2b170895effe7f",
        "accepted L1 manifest status gate",
    )
    require(
        checker.get("protocol_id") == "R401-VAL-L1-V2"
        and checker.get("checker_status") == "PASS"
        and checker.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and checker.get("final_status") is None
        and checker.get("job_failures") == []
        and checker.get("manifest_hash_failures") == []
        and checker.get("scope")
        == "independent exact-rational replay of archived Krawczyk arithmetic, plan coverage, bridge gluing, phase gates, and hashes; not an independent ODE integration",
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
        and release.get("final_status") is None
        and release.get("scope")
        == "Post-production provenance binding; uniqueness is only inside the frozen local primary boxes and guarded bridge hulls.",
        "accepted L1 release status gate",
    )
    manifest_files = manifest.get("files")
    require(
        isinstance(manifest_files, dict) and len(manifest_files) == 417,
        "accepted L1 manifest exact file count",
    )
    require(
        manifest_files.get(project_relative(PLAN))
        == captured_hashes[project_relative(PLAN)],
        "accepted L1 manifest final-plan binding",
    )
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
    hashes = {
        project_relative(path): captured_hashes[project_relative(path)]
        for path in L1_RELEASE_CHAIN
    }
    return hashes, plan_payload, captured_hashes[project_relative(PLAN)]


def independently_validate_l1_release_chain() -> dict[str, str]:
    return independently_validate_l1_bundle()[0]


class ValidatedPlanRecord(dict[str, Any]):
    validated_source_bindings: dict[str, Any]


def expected_source_bindings(
    plan_record: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if isinstance(plan_record, ValidatedPlanRecord):
        bindings = plan_record.validated_source_bindings
        return {
            **bindings,
            "l1_release_chain_sha256": dict(bindings["l1_release_chain_sha256"]),
        }
    hashes, plan_payload, plan_hash = independently_validate_l1_bundle()
    del plan_payload
    return {
        "evaluator_sha256": sha256_file(EVALUATOR),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": plan_hash,
        "l1_release_chain_sha256": hashes,
    }


def verify_source_bindings(
    payload: Any,
    context: str,
    plan_record: Mapping[str, Any] | None = None,
) -> None:
    require(isinstance(payload, dict), f"{context}: bindings not object")
    exact_keys(
        payload,
        {
            "evaluator_sha256",
            "checker_sha256",
            "l1_final_plan_sha256",
            "l1_release_chain_sha256",
        },
        context,
    )
    expected = expected_source_bindings(plan_record)
    require_json_exact(payload, expected, f"{context}: source binding mismatch")


def load_plan() -> dict[str, dict[str, Any]]:
    hashes, payload, plan_hash = independently_validate_l1_bundle()
    require(isinstance(payload.get("slabs"), list), "L1 plan slab list")
    bindings = {
        "evaluator_sha256": sha256_file(EVALUATOR),
        "checker_sha256": sha256_file(CHECKER),
        "l1_final_plan_sha256": plan_hash,
        "l1_release_chain_sha256": hashes,
    }
    records: dict[str, dict[str, Any]] = {}
    for record in payload["slabs"]:
        require(isinstance(record, dict), "L1 plan slab record")
        slab_id = record.get("slab_id")
        require(type(slab_id) is str and slab_id in SLABS, "L1 plan slab id")
        require(slab_id not in records, "duplicate L1 plan slab")
        captured = ValidatedPlanRecord(record)
        captured.validated_source_bindings = bindings
        records[slab_id] = captured
    require(list(records) == list(SLABS), "L1 plan exact ordered 51 slabs")
    return records


def plan_epsilon(plan: dict[str, dict[str, Any]], slab_id: str) -> tuple[Fraction, Fraction]:
    record = plan[slab_id]
    return Fraction(str(record["epsilon_lower"])), Fraction(str(record["epsilon_upper"]))


def plan_record_sha256(record: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(record))


@dataclass(frozen=True)
class FormalStaticContext:
    matrix_id: str
    freeze_sha256: str
    run_config_sha256: str
    max_depth: int
    max_nodes_per_tree: int
    max_nodes_per_cell: int


def validate_formal_context(context: FormalStaticContext) -> None:
    for label in ("matrix_id", "freeze_sha256", "run_config_sha256"):
        value = getattr(context, label)
        require(
            type(value) is str
            and len(value) == 64
            and all(character in "0123456789abcdef" for character in value),
            f"context.{label}: lowercase SHA-256 required",
        )
    for label in ("max_depth", "max_nodes_per_tree", "max_nodes_per_cell"):
        value = getattr(context, label)
        require(
            type(value) is int and value > 0,
            f"context.{label}: positive exact integer required",
        )
    require(
        context.max_nodes_per_cell >= context.max_nodes_per_tree,
        "context: cell node cap below tree node cap",
    )


def verify_proof(
    path: Path,
    *,
    expected_bits: int,
    expected_slab: str,
    plan: dict[str, dict[str, Any]],
    context: FormalStaticContext,
) -> dict[str, Any]:
    validate_formal_context(context)
    payload, proof_raw = load_canonical_json_with_raw(path)
    exact_keys(
        payload,
        {
            "schema_version",
            "protocol_id",
            "artifact_role",
            "authority",
            "scientific_licensing_enabled",
            "matrix_id",
            "freeze_sha256",
            "run_config_sha256",
            "component_status",
            "milestone_status",
            "theorem_status",
            "final_status",
            "evaluator_status",
            "slab_id",
            "precision_bits",
            "epsilon",
            "period_window",
            "input_echo",
            "claim_boundary",
            "proof_complete",
            "outer_containment",
            "trees",
            "counts",
            "source_bindings",
            "proof_content_hash_definition",
            "proof_content_sha256",
        },
        path.name,
    )
    require_exact_int(payload["schema_version"], f"{path.name}.schema_version", expected=SCHEMA_VERSION)
    require(payload["protocol_id"] == PROTOCOL_ID, f"{path.name}: protocol")
    require(payload["artifact_role"] == CELL_ROLE, f"{path.name}: artifact role")
    require(payload["authority"] == "PRODUCER_ONLY", f"{path.name}: authority")
    require(payload["scientific_licensing_enabled"] is False, f"{path.name}: licensing flag")
    require(payload["matrix_id"] == context.matrix_id, f"{path.name}: matrix id")
    require(payload["freeze_sha256"] == context.freeze_sha256, f"{path.name}: freeze")
    require(payload["run_config_sha256"] == context.run_config_sha256, f"{path.name}: run config")
    require(payload["component_status"] is None, f"{path.name}: producer component status")
    require(payload["milestone_status"] is None, f"{path.name}: milestone status")
    require(payload["theorem_status"] is None, f"{path.name}: theorem status")
    require(payload["final_status"] is None, f"{path.name}: final status")
    require(payload["evaluator_status"] == CELL_PASS_STATUS, f"{path.name}: evaluator status")
    require(payload["proof_complete"] is True, f"{path.name}: proof completeness")
    require(payload["slab_id"] == expected_slab, f"{path.name}: slab")
    require_exact_int(payload["precision_bits"], f"{path.name}.precision_bits", expected=expected_bits)
    require(payload["claim_boundary"] == CELL_CLAIM_BOUNDARY, f"{path.name}: claim boundary")
    epsilon = parse_interval_record(payload["epsilon"], f"{path.name}.epsilon")
    require(epsilon == plan_epsilon(plan, expected_slab), f"{path.name}: plan epsilon")
    require(
        parse_interval_record(payload["period_window"], f"{path.name}.period_window")
        == (Fraction(64, 100), PERIOD_MAX),
        f"{path.name}: period window",
    )
    record = plan[expected_slab]
    require_json_exact(
        payload["input_echo"],
        {
            "slab_id": expected_slab,
            "precision_bits": expected_bits,
            "epsilon_lower": record["epsilon_lower"],
            "epsilon_upper": record["epsilon_upper"],
            "matrix_id": context.matrix_id,
            "freeze_sha256": context.freeze_sha256,
            "run_config_sha256": context.run_config_sha256,
            "plan_record_sha256": plan_record_sha256(record),
            "max_depth": context.max_depth,
            "max_nodes_per_tree": context.max_nodes_per_tree,
            "max_nodes_per_cell": context.max_nodes_per_cell,
        },
        f"{path.name}.input_echo",
    )
    verify_source_bindings(
        payload["source_bindings"],
        f"{path.name}.source_bindings",
        record,
    )
    require(
        payload["proof_content_hash_definition"]
        == "sha256(canonical_json(proof_without_proof_content_sha256))",
        f"{path.name}: proof hash definition",
    )
    without_hash = dict(payload)
    stored_content_hash = without_hash.pop("proof_content_sha256")
    require(
        stored_content_hash == sha256_bytes(canonical_json_bytes(without_hash)),
        f"{path.name}: proof content hash",
    )

    previous_precision = ctx.prec
    ctx.prec = expected_bits
    try:
        model = independent_model()
        interval_checks = verify_outer_containment(
            payload["outer_containment"], model, expected_bits, f"{path.name}.outer"
        )
        trees = payload["trees"]
        require(isinstance(trees, list) and len(trees) == 4, f"{path.name}: tree matrix")
        expected = [
            ("ANGLE", ANGLE_ROOT),
            *[(tree_id, SECTION_ROOTS[tree_id]) for tree_id in SECTION_ROOTS],
        ]
        results = [
            replay_tree(tree, epsilon, model, tree_id, root)
            for tree, (tree_id, root) in zip(trees, expected, strict=True)
        ]
        interval_checks += sum(item["interval_checks"] for item in results)
    finally:
        ctx.prec = previous_precision

    result_by_id = {item["tree_id"]: item for item in results}
    for result in results:
        require(
            result["node_count"] <= context.max_nodes_per_tree,
            f"{path.name}: tree node count exceeds frozen per-tree cap",
        )
        require(
            result["maximum_depth"] <= context.max_depth,
            f"{path.name}: tree depth exceeds frozen cap",
        )
    require(
        sum(item["node_count"] for item in results) <= context.max_nodes_per_cell,
        f"{path.name}: cell node count exceeds frozen cap",
    )
    require(result_by_id["ANGLE"]["terminal_counts"].get("ANGLE_CERTIFIED", 0) > 0, f"{path.name}: no angle leaves")
    for tree_id in ("SECTION_LOW", "SECTION_HIGH"):
        require(
            set(result_by_id[tree_id]["terminal_counts"])
            <= {"ENERGY_EXCLUDED", "TUBE_EXCLUDED"},
            f"{path.name}: {tree_id} retained a section candidate",
        )
    require_json_exact(
        result_by_id["SECTION_WINDOW"]["terminal_counts"],
        {"LANDING_CLOSED_WINDOW": 1},
        f"{path.name}: middle section window contract",
    )
    counts = payload["counts"]
    require(isinstance(counts, dict), f"{path.name}: counts object")
    exact_keys(
        counts,
        {
            "tree_count",
            "node_count",
            "internal_count",
            "terminal_count",
            "unresolved_count",
            "maximum_depth",
        },
        f"{path.name}.counts",
    )
    require_exact_int(counts["tree_count"], f"{path.name}.counts.tree_count", expected=4)
    require_exact_int(
        counts["node_count"],
        f"{path.name}.counts.node_count",
        expected=sum(item["node_count"] for item in results),
    )
    require_exact_int(
        counts["internal_count"],
        f"{path.name}.counts.internal_count",
        expected=sum(item["internal_count"] for item in results),
    )
    require_exact_int(
        counts["terminal_count"],
        f"{path.name}.counts.terminal_count",
        expected=sum(item["terminal_count"] for item in results),
    )
    require_exact_int(
        counts["unresolved_count"],
        f"{path.name}.counts.unresolved_count",
        expected=0,
    )
    require_exact_int(
        counts["maximum_depth"],
        f"{path.name}.counts.maximum_depth",
        expected=max(item["maximum_depth"] for item in results),
    )
    return {
        "path": path.name,
        "precision_bits": expected_bits,
        "slab_id": expected_slab,
        "node_count": counts["node_count"],
        "internal_count": counts["internal_count"],
        "terminal_count": counts["terminal_count"],
        "unresolved_count": counts["unresolved_count"],
        "maximum_depth": counts["maximum_depth"],
        "interval_checks": interval_checks,
        "sha256": sha256_bytes(proof_raw),
        "tree_content_sha256": {
            item["tree_id"]: item["content_sha256"] for item in results
        },
        "angle_extrema": result_by_id["ANGLE"]["angle_extrema"],
    }


def run_checker(_input_dir: Path) -> dict[str, Any]:
    """Fail closed until the formal aggregate and run-config replay is complete."""

    raise CheckError(
        "formal 102-cell static aggregate replay is not yet implemented; "
        "this implementation-design checker core cannot issue component authority"
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=canonical_absolute_argument, required=True)
    parser.add_argument(
        "--output",
        type=canonical_absolute_argument,
        default=None,
        help="write-once checker JSON path",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.input_dir.is_symlink():
            raise CheckError("input directory must not be a symlink")
        if arguments.output is not None and arguments.output.is_symlink():
            raise CheckError("checker output must not be a symlink")
        input_dir = arguments.input_dir
        output = (
            arguments.output
            if arguments.output is not None
            else input_dir / "independent_static_checker.json"
        )
        result = run_checker(input_dir)
        write_once(output, canonical_json_bytes(result))
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"checker_status={result['checker_status']} "
        f"component_status={result['component_status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
