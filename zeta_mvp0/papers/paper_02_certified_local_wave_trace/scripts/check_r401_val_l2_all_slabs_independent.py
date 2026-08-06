#!/usr/bin/env python3
"""Independent prospective checker for R401-VAL-L2-A1.

This module is intentionally ``DRAFT_NON_LICENSING``.  It does not import
the producer, scheduler, or their helpers.  All constants, path rules,
exact-rational interval operations, tree reconstruction, and status rules
below are independently stated.

The checker has two jobs:

* make the future all-51-slab proof archive mechanically checkable; and
* fail closed while the formal freeze and its sealed run configuration do
  not exist.

It never reruns the ODE integration.  Instead, it replays the proof objects
printed by the interval evaluator.  In particular, it reconstructs every
energy Newton image, mean-value residual, preconditioned residual, and
Krawczyk image using :class:`fractions.Fraction` arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
CHECKER = Path(__file__).resolve()
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
FORMAL_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L2_A1_FREEZE.json"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"

MANDATORY_FROZEN_INPUTS = (
    "scripts/check_r401_val_l2_all_slabs_independent.py",
    "scripts/run_r401_val_l2_all_slabs.py",
    "validated/capd_r401_local_complement_mp.cpp",
    "validated/CAPD_DEPENDENCY.md",
    "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md",
)

FORMAL_PROTOCOL_ID = "R401-VAL-L2-A1"
DRAFT_PROTOCOL_ID = "R401-VAL-L2-A1-DRAFT"
CHECKER_MODE = "DRAFT_NON_LICENSING"
SCHEMA_VERSION = 1
EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
EXPECTED_SCHEDULER_POLICY = "deterministic_round_robin_barrier_batches_v1"
REQUIRED_CAPD_FLAGS = frozenset(
    {"-D__HAVE_MPFR__", "-lmpfr", "-lgmp", "-frounding-math"}
)
EXPECTED_LOGICAL_THRESHOLDS = {
    "logical_margin_128": "1e-30",
    "logical_margin_256": "1e-60",
    "newton_guard_128": "1e-40",
    "newton_guard_256": "1e-75",
}
PRECISIONS = (128, 256)
SLAB_IDS = tuple(f"S{index:03d}" for index in range(51))
COORDINATES = ("q_slow", "q_fast", "p_slow", "period")
BIG_BOX = {
    "q_slow": (Fraction(-1, 50), Fraction(1, 50)),
    "q_fast": (Fraction(3, 25), Fraction(17, 100)),
    "p_slow": (Fraction(-2, 25), Fraction(2, 25)),
    "period": (Fraction(16, 25), Fraction(69, 100)),
}
FULL_WIDTHS = {
    coordinate: upper - lower
    for coordinate, (lower, upper) in BIG_BOX.items()
}
NODE_ID_PATTERN = re.compile(r"^C[0-3][LU][01]*$")
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")

Interval = tuple[Fraction, Fraction]
Vector = tuple[Interval, ...]
Matrix = tuple[Vector, ...]

# Exact closed evaluator namespace.  Anything else, including a timeout,
# signal, missing status, repeated status, or boolean return code, is invalid.
STATUS_ACTION = {
    ("ENERGY_EXCLUDED", 0): "ENERGY_EXCLUDED",
    ("RETURN_EXCLUDED", 0): "RETURN_EXCLUDED",
    ("UNKNOWN", 2): "SPLIT",
    ("ENERGY_DERIVATIVE_FAIL", 3): "SPLIT",
    ("ENERGY_GUARD_FAIL", 3): "SPLIT",
    ("FLOW_FAIL", 3): "SPLIT",
    ("ROOT_CANDIDATE", 4): "SCIENTIFIC_STOP",
    ("INVALID_EXCLUSION_UNIQUENESS_CONFLICT", 5): "INVALID",
}


class CheckerContractError(RuntimeError):
    """An authoritative proof object violated the checker contract."""


class StrictJSONError(CheckerContractError):
    """A JSON input is malformed, ambiguous, or non-finite."""


class PathContractError(CheckerContractError):
    """A path is unsafe, non-canonical, missing, extra, or a symlink."""


class ProofObjectError(CheckerContractError):
    """A mathematical proof object is missing or fails exact replay."""


class MatrixContractError(CheckerContractError):
    """The required 102-pair archive matrix is not exact."""


@dataclass(frozen=True, order=True)
class TreeKey:
    precision_bits: int
    slab_id: str

    @property
    def label(self) -> str:
        return f"{self.precision_bits}:{self.slab_id}"

    def payload(self) -> dict[str, Any]:
        return {"precision_bits": self.precision_bits, "slab_id": self.slab_id}


@dataclass(frozen=True)
class FormalContext:
    freeze: Mapping[str, Any]
    run_config: Mapping[str, Any]
    freeze_sha256: str
    run_config_sha256: str
    max_depth: int
    max_nodes: int
    evaluator_source_sha256: str
    evaluator_binary_sha256: str
    evaluator_binary_file: str
    evaluator_capd_commit: str
    evaluator_capd_flags: tuple[str, ...]
    scheduler: Mapping[str, Any]
    logical_thresholds: Mapping[str, Any]


def exact_matrix() -> tuple[TreeKey, ...]:
    return tuple(
        TreeKey(bits, slab_id)
        for bits in PRECISIONS
        for slab_id in SLAB_IDS
    )


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJSONError(f"DUPLICATE_JSON_KEY: {key}")
        result[key] = value
    return result


def strict_json_loads(raw: str) -> Any:
    def reject_constant(value: str) -> None:
        raise StrictJSONError(f"NONFINITE_JSON_CONSTANT: {value}")

    try:
        return json.loads(
            raw,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=reject_constant,
        )
    except StrictJSONError:
        raise
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        raise StrictJSONError(f"MALFORMED_JSON: {error}") from error


def strict_json_load(path: Path) -> Any:
    require_regular_file(path)
    return strict_json_loads(path.read_text(encoding="utf-8"))


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


def sha256(path: Path) -> str:
    require_regular_file(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_regular_file(path: Path) -> None:
    if path.is_symlink():
        raise PathContractError(f"SYMLINK_REJECTED: {path}")
    if not path.is_file():
        raise PathContractError(f"MISSING_REGULAR_FILE: {path}")


def checked_lexical_path(
    value: Path,
    *,
    label: str,
    require_file: bool = False,
    require_directory: bool = False,
) -> Path:
    """Validate a user- or archive-supplied path before resolving symlinks.

    Calling ``resolve()`` first erases the evidence that the original path (or
    one of its parents) was a symbolic link.  Formal provenance paths are
    therefore normalized lexically, walked component by component, and only
    accepted when no component is a symlink.
    """

    lexical = Path(os.path.abspath(os.fspath(value)))
    cursor = Path(lexical.anchor)
    for part in lexical.parts[1:]:
        cursor = cursor / part
        if cursor.is_symlink():
            raise PathContractError(f"SYMLINK_REJECTED_{label}: {cursor}")
    if require_file and not lexical.is_file():
        raise PathContractError(f"MISSING_REGULAR_FILE_{label}: {lexical}")
    if require_directory and not lexical.is_dir():
        raise PathContractError(f"MISSING_DIRECTORY_{label}: {lexical}")
    return lexical


def safe_relative_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise PathContractError(f"UNSAFE_PATH: {value!r}")
    candidate = PurePosixPath(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise PathContractError(f"PATH_TRAVERSAL: {value!r}")
    if any(part in {"", "."} or part.startswith(".") for part in candidate.parts):
        raise PathContractError(f"NONCANONICAL_PATH: {value!r}")
    return candidate


def resolve_bound_path(root: Path, value: str, *, expected: str | None = None) -> Path:
    relative = safe_relative_path(value)
    if expected is not None and relative.as_posix() != expected:
        raise PathContractError(
            f"PATH_IDENTITY_MISMATCH: expected {expected!r}, got {value!r}"
        )
    candidate = root.joinpath(*relative.parts)
    require_regular_file(candidate)
    # The lexical checks above and the symlink walk below jointly prevent an
    # apparently safe leaf from escaping through a symlinked parent.
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise PathContractError(f"SYMLINK_REJECTED: {cursor}")
    try:
        candidate.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise PathContractError(f"PATH_ESCAPES_ROOT: {value!r}") from error
    return candidate


def scan_exact_json_paths(root: Path, expected: Iterable[Path]) -> None:
    expected_set = set(expected)
    if root.is_symlink() or not root.is_dir():
        raise PathContractError(f"MISSING_OR_SYMLINK_MATRIX_ROOT: {root}")
    actual: set[Path] = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part.startswith(".") for part in relative.parts):
            raise PathContractError(f"HIDDEN_AUTHORITATIVE_PATH: {path}")
        if path.is_symlink():
            raise PathContractError(f"SYMLINK_REJECTED: {path}")
        if path.is_file():
            if path.suffix != ".json":
                raise PathContractError(f"EXTRA_NON_JSON_SHARD: {path}")
            actual.add(path)
    missing = expected_set - actual
    extra = actual - expected_set
    if missing or extra:
        raise MatrixContractError(
            "MISSING_EXTRA_SHARDS: "
            f"missing={sorted(map(str, missing))}, extra={sorted(map(str, extra))}"
        )


def interval(value: Sequence[str] | Sequence[int] | Sequence[Fraction]) -> Interval:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ProofObjectError(f"MALFORMED_INTERVAL: {value!r}")
    try:
        result = Fraction(str(value[0])), Fraction(str(value[1]))
    except (ValueError, ZeroDivisionError) as error:
        raise ProofObjectError(f"MALFORMED_INTERVAL: {value!r}") from error
    if result[0] > result[1]:
        raise ProofObjectError(f"REVERSED_INTERVAL: {value!r}")
    return result


def subset(inner: Interval, outer: Interval) -> bool:
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def strict_inside(inner: Interval, outer: Interval) -> bool:
    return outer[0] < inner[0] <= inner[1] < outer[1]


def iadd(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def ineg(value: Interval) -> Interval:
    return -value[1], -value[0]


def isub(left: Interval, right: Interval) -> Interval:
    return iadd(left, ineg(right))


def imul(left: Interval, right: Interval) -> Interval:
    products = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(products), max(products)


def idiv(numerator: Interval, denominator: Interval) -> Interval:
    if denominator[0] <= 0 <= denominator[1]:
        raise ProofObjectError("DIVISOR_CONTAINS_ZERO")
    reciprocals = Fraction(1, 1) / denominator[0], Fraction(1, 1) / denominator[1]
    return imul(numerator, (min(reciprocals), max(reciprocals)))


def iintersect(left: Interval, right: Interval) -> Interval | None:
    lower, upper = max(left[0], right[0]), min(left[1], right[1])
    return None if lower > upper else (lower, upper)


def igap(left: Interval, right: Interval) -> Fraction:
    if left[1] < right[0]:
        return right[0] - left[1]
    if right[1] < left[0]:
        return left[0] - right[1]
    return Fraction(0)


def distance_from_zero(value: Interval) -> Fraction:
    if value[0] <= 0 <= value[1]:
        return Fraction(0)
    return value[0] if value[0] > 0 else -value[1]


def vector_add(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ProofObjectError("VECTOR_DIMENSION_MISMATCH")
    return tuple(iadd(a, b) for a, b in zip(left, right, strict=True))


def vector_sub(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ProofObjectError("VECTOR_DIMENSION_MISMATCH")
    return tuple(isub(a, b) for a, b in zip(left, right, strict=True))


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ProofObjectError("MATRIX_VECTOR_DIMENSION_MISMATCH")
    output: list[Interval] = []
    for row in matrix:
        total: Interval = (Fraction(0), Fraction(0))
        for coefficient, value in zip(row, vector, strict=True):
            total = iadd(total, imul(coefficient, value))
        output.append(total)
    return tuple(output)


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or any(len(row) != len(right) for row in left):
        raise ProofObjectError("MATRIX_MATRIX_DIMENSION_MISMATCH")
    columns = len(right[0])
    if any(len(row) != columns for row in right):
        raise ProofObjectError("RAGGED_MATRIX")
    result: list[Vector] = []
    for row in left:
        output_row: list[Interval] = []
        for column in range(columns):
            total: Interval = (Fraction(0), Fraction(0))
            for index, coefficient in enumerate(row):
                total = iadd(total, imul(coefficient, right[index][column]))
            output_row.append(total)
        result.append(tuple(output_row))
    return tuple(result)


def identity_matrix(size: int) -> Matrix:
    return tuple(
        tuple(
            (Fraction(1), Fraction(1)) if row == column else (Fraction(0), Fraction(0))
            for column in range(size)
        )
        for row in range(size)
    )


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(
        len(a) != len(b) for a, b in zip(left, right, strict=True)
    ):
        raise ProofObjectError("MATRIX_DIMENSION_MISMATCH")
    return tuple(
        tuple(isub(a, b) for a, b in zip(row_a, row_b, strict=True))
        for row_a, row_b in zip(left, right, strict=True)
    )


class Transcript:
    """Strict parser for the evaluator's line-oriented proof transcript."""

    def __init__(self, raw: str):
        self.raw = raw
        self.lines = raw.splitlines()

    def block(self, key: str) -> str:
        prefix = f"{key}="
        starts = [index for index, line in enumerate(self.lines) if line.startswith(prefix)]
        if len(starts) != 1:
            label = "MISSING" if not starts else "DUPLICATE"
            raise ProofObjectError(f"{label}_PROOF_FIELD: {key}")
        index = starts[0]
        value = self.lines[index][len(prefix) :]
        balance = value.count("{") - value.count("}")
        cursor = index + 1
        while balance > 0 and cursor < len(self.lines):
            value += "\n" + self.lines[cursor]
            balance += self.lines[cursor].count("{") - self.lines[cursor].count("}")
            cursor += 1
        if balance != 0:
            raise ProofObjectError(f"UNBALANCED_PROOF_FIELD: {key}")
        return value.strip()

    def optional_block(self, key: str) -> str | None:
        prefix = f"{key}="
        starts = [index for index, line in enumerate(self.lines) if line.startswith(prefix)]
        if not starts:
            return None
        return self.block(key)

    def scalar(self, key: str) -> str:
        value = self.block(key)
        if "\n" in value:
            raise ProofObjectError(f"SCALAR_FIELD_IS_MULTILINE: {key}")
        return value

    def intervals(self, key: str, expected: int) -> Vector:
        value = self.block(key)
        parsed = tuple(
            (Fraction(lower), Fraction(upper))
            for lower, upper in INTERVAL_PATTERN.findall(value)
        )
        if len(parsed) != expected:
            raise ProofObjectError(
                f"MALFORMED_PROOF_FIELD: {key}: expected {expected} intervals, got {len(parsed)}"
            )
        if any(lower > upper for lower, upper in parsed):
            raise ProofObjectError(f"REVERSED_PROOF_INTERVAL: {key}")
        return parsed

    def vector(self, key: str) -> Vector:
        return self.intervals(key, 4)

    def matrix(self, key: str) -> Matrix:
        flat = self.intervals(key, 16)
        return tuple(tuple(flat[4 * row : 4 * row + 4]) for row in range(4))


def mathematical_margin(bits: int) -> Fraction:
    if bits == 128:
        return Fraction(1, 10**30)
    if bits == 256:
        return Fraction(1, 10**60)
    raise ProofObjectError(f"INVALID_PRECISION: {bits}")


def mathematical_guard(bits: int) -> Fraction:
    if bits == 128:
        return Fraction(1, 10**40)
    if bits == 256:
        return Fraction(1, 10**75)
    raise ProofObjectError(f"INVALID_PRECISION: {bits}")


def status_action(status: str, returncode: Any, *, depth: int, max_depth: int) -> str:
    if not isinstance(returncode, int) or isinstance(returncode, bool):
        raise ProofObjectError("INVALID_RETURN_CODE_TYPE")
    action = STATUS_ACTION.get((status, returncode))
    if action is None:
        raise ProofObjectError(f"STATUS_RETURNCODE_NOT_WHITELISTED: {status}/{returncode}")
    if action == "SPLIT" and depth >= max_depth:
        raise ProofObjectError("DEPTH_EXHAUSTED_NOT_SPLITTABLE")
    return action


def verify_energy_proof(transcript: Transcript, status: str) -> dict[str, Any]:
    bits = int(transcript.scalar("precision_bits"))
    margin = mathematical_margin(bits)
    guard = mathematical_guard(bits)
    displayed_margin = transcript.intervals("logical_margin", 1)[0]
    displayed_guard = transcript.intervals("newton_guard", 1)[0]
    if displayed_margin[0] < margin:
        raise ProofObjectError("LOGICAL_MARGIN_BELOW_FROZEN_GATE")
    if not subset((-guard, guard), displayed_guard):
        raise ProofObjectError("NEWTON_GUARD_BELOW_FROZEN_GATE")

    step_matches = re.findall(r"^energy_step_(\d+)_before=", transcript.raw, re.MULTILINE)
    if not step_matches:
        raise ProofObjectError("MISSING_PROOF_OBJECT: energy_steps")
    step_ids = [int(value) for value in step_matches]
    if step_ids != list(range(len(step_ids))):
        raise ProofObjectError("NONCONTIGUOUS_OR_DUPLICATE_ENERGY_STEPS")

    current = transcript.intervals("qplus_input", 1)[0]
    final_after: Interval | None = None
    empty_gap: Fraction | None = None
    displayed_empty_gap: Interval | None = None
    derivative_failed = False
    last: dict[str, Interval] = {}
    for step_id in step_ids:
        prefix = f"energy_step_{step_id}"
        before = transcript.intervals(prefix + "_before", 1)[0]
        midpoint = transcript.intervals(prefix + "_midpoint", 1)[0]
        residual = transcript.intervals(prefix + "_residual", 1)[0]
        derivative = transcript.intervals(prefix + "_derivative", 1)[0]
        last = {
            "before": before,
            "midpoint": midpoint,
            "residual": residual,
            "derivative": derivative,
        }
        if before != current:
            raise ProofObjectError(f"ENERGY_CHAIN_MISMATCH: {prefix}")
        if not subset(midpoint, before):
            raise ProofObjectError(f"MIDPOINT_OUTSIDE_BEFORE: {prefix}")

        derivative_marker = transcript.optional_block(prefix + "_derivative_positive")
        if derivative[0] <= 0:
            if step_id != step_ids[-1] or derivative_marker != "0":
                raise ProofObjectError(f"MALFORMED_DERIVATIVE_FAILURE: {prefix}")
            derivative_failed = True
            break
        if derivative_marker is not None:
            raise ProofObjectError(f"UNEXPECTED_DERIVATIVE_MARKER: {prefix}")

        newton_raw = transcript.intervals(prefix + "_newton_raw", 1)[0]
        newton = transcript.intervals(prefix + "_newton", 1)[0]
        recomputed = isub(midpoint, idiv(residual, derivative))
        if not subset(recomputed, newton):
            raise ProofObjectError(f"NEWTON_REPLAY_NOT_ENCLOSED: {prefix}")
        if not subset(iadd(newton_raw, displayed_guard), newton):
            raise ProofObjectError(f"GUARDED_NEWTON_IMAGE_MISMATCH: {prefix}")
        intersects = transcript.scalar(prefix + "_intersects")
        exact_intersection = iintersect(before, newton)
        if intersects == "0":
            if step_id != step_ids[-1] or exact_intersection is not None:
                raise ProofObjectError(f"FALSE_EMPTY_INTERSECTION: {prefix}")
            displayed_gap = transcript.intervals(prefix + "_gap", 1)[0]
            displayed_empty_gap = displayed_gap
            empty_gap = igap(before, newton)
            # The displayed operands are themselves widened by decimal
            # conversion, so their exact-rational gap can be a few terminal
            # display units smaller than the separately displayed MPFR gap.
            # We never use that displayed gap to license an exclusion: the
            # independently recomputed ``empty_gap`` below is authoritative.
            if displayed_gap[0] < 0:
                raise ProofObjectError(f"NEGATIVE_DISPLAYED_GAP: {prefix}")
            break
        if intersects != "1" or exact_intersection is None:
            raise ProofObjectError(f"FALSE_NONEMPTY_INTERSECTION: {prefix}")
        after = transcript.intervals(prefix + "_after", 1)[0]
        if not subset(exact_intersection, after) or not subset(after, before) or not subset(after, newton):
            raise ProofObjectError(f"CONTRACTION_REPLAY_MISMATCH: {prefix}")
        current = after
        final_after = after

    if transcript.intervals("energy_qplus_before", 1)[0] != last["before"]:
        raise ProofObjectError("ENERGY_SUMMARY_BEFORE_MISMATCH")
    if transcript.intervals("energy_midpoint", 1)[0] != last["midpoint"]:
        raise ProofObjectError("ENERGY_SUMMARY_MIDPOINT_MISMATCH")
    if transcript.intervals("energy_midpoint_residual", 1)[0] != last["residual"]:
        raise ProofObjectError("ENERGY_SUMMARY_RESIDUAL_MISMATCH")
    if transcript.intervals("energy_derivative", 1)[0] != last["derivative"]:
        raise ProofObjectError("ENERGY_SUMMARY_DERIVATIVE_MISMATCH")

    positive_flag = transcript.scalar("energy_derivative_positive")
    candidate_flag = transcript.scalar("energy_has_candidate")
    exclusion_flag = transcript.scalar("energy_exclusion_guard")
    if derivative_failed:
        if status != "ENERGY_DERIVATIVE_FAIL" or positive_flag != "0":
            raise ProofObjectError("DERIVATIVE_STATUS_MISMATCH")
    elif status == "ENERGY_DERIVATIVE_FAIL":
        raise ProofObjectError("FALSE_DERIVATIVE_FAILURE_STATUS")
    elif empty_gap is not None:
        if status == "ENERGY_EXCLUDED":
            if (
                not empty_gap > margin
                or displayed_empty_gap is None
                or displayed_empty_gap[0] <= margin
                or candidate_flag != "0"
                or exclusion_flag != "1"
            ):
                raise ProofObjectError("ENERGY_EXCLUSION_GAP_NOT_LICENSED")
        elif status == "ENERGY_GUARD_FAIL":
            if (
                empty_gap > margin
                or displayed_empty_gap is None
                or displayed_empty_gap[0] > margin
                or candidate_flag != "1"
                or exclusion_flag != "0"
            ):
                raise ProofObjectError("ENERGY_GUARD_FAILURE_MISMATCH")
        else:
            raise ProofObjectError("EMPTY_ENERGY_IMAGE_WITH_NONENERGY_STATUS")
    else:
        if status in {"ENERGY_EXCLUDED", "ENERGY_GUARD_FAIL"}:
            raise ProofObjectError("ENERGY_STATUS_WITHOUT_EMPTY_IMAGE")
        reported = transcript.intervals("energy_qplus", 1)[0]
        if final_after is None or reported != final_after:
            raise ProofObjectError("ENERGY_FINAL_CONTRACTION_MISMATCH")
        if positive_flag != "1" or candidate_flag != "1" or exclusion_flag != "1":
            raise ProofObjectError("ENERGY_SUMMARY_FLAGS_MISMATCH")

    return {
        "precision_bits": bits,
        "step_count": len(step_ids),
        "derivative_failed": derivative_failed,
        "empty_gap": None if empty_gap is None else fraction_payload(empty_gap),
    }


def first_separating_component(values: Vector, margin: Fraction) -> int:
    for index, value in enumerate(values):
        if distance_from_zero(value) > margin:
            return index
    return -1


def _require_reported_encloses_replay(
    reported: Vector, recomputed: Vector, label: str
) -> None:
    for index, (shown, replayed) in enumerate(zip(reported, recomputed, strict=True)):
        # The exact-rational calculation uses the already outward-displayed
        # operands.  The evaluator's displayed result must enclose that exact
        # calculation; its final MPFR-to-decimal rounding may make it wider.
        if not subset(replayed, shown):
            raise ProofObjectError(
                f"{label}_DOES_NOT_ENCLOSE_EXACT_REPLAY: component {index}"
            )


def verify_return_proof(transcript: Transcript, status: str) -> dict[str, Any]:
    bits = int(transcript.scalar("precision_bits"))
    margin = mathematical_margin(bits)
    x_box = transcript.vector("X")
    x_bar = transcript.vector("x_bar")
    if any(not subset(point, box) for point, box in zip(x_bar, x_box, strict=True)):
        raise ProofObjectError("X_BAR_OUTSIDE_X")
    f_center = transcript.vector("F_center")
    f_direct = transcript.vector("F_direct")
    jacobian = transcript.matrix("J")
    displayed_mean = transcript.vector("F_mean")
    preconditioner = transcript.matrix("C")
    displayed_preconditioned = transcript.vector("F_preconditioned")
    displayed_krawczyk = transcript.vector("K")

    delta = vector_sub(x_box, x_bar)
    recomputed_mean = vector_add(f_center, matrix_vector(jacobian, delta))
    recomputed_preconditioned = matrix_vector(preconditioner, recomputed_mean)
    c_j = matrix_multiply(preconditioner, jacobian)
    remainder = matrix_sub(identity_matrix(4), c_j)
    recomputed_krawczyk = vector_add(
        vector_sub(x_bar, matrix_vector(preconditioner, f_center)),
        matrix_vector(remainder, delta),
    )
    _require_reported_encloses_replay(displayed_mean, recomputed_mean, "F_MEAN")
    _require_reported_encloses_replay(
        displayed_preconditioned,
        recomputed_preconditioned,
        "C_F_MEAN",
    )
    _require_reported_encloses_replay(
        displayed_krawczyk, recomputed_krawczyk, "KRAWCZYK"
    )

    direct_component = int(transcript.scalar("direct_component"))
    mean_component = int(transcript.scalar("mean_component"))
    preconditioned_component = int(transcript.scalar("preconditioned_component"))
    displayed_indices = {
        "direct": first_separating_component(f_direct, margin),
        "mean": first_separating_component(displayed_mean, margin),
        "preconditioned": first_separating_component(displayed_preconditioned, margin),
    }
    actual_indices = {
        "direct": direct_component,
        "mean": mean_component,
        "preconditioned": preconditioned_component,
    }
    if displayed_indices != actual_indices:
        raise ProofObjectError(
            f"SELECTED_COMPONENT_MISMATCH: expected={displayed_indices}, got={actual_indices}"
        )

    independently_licensed: dict[str, Fraction] = {}
    if direct_component >= 0:
        independently_licensed["direct"] = distance_from_zero(f_direct[direct_component])
    if mean_component >= 0:
        independently_licensed["mean"] = distance_from_zero(
            recomputed_mean[mean_component]
        )
    if preconditioned_component >= 0:
        independently_licensed["preconditioned"] = distance_from_zero(
            recomputed_preconditioned[preconditioned_component]
        )
    independently_licensed = {
        key: value for key, value in independently_licensed.items() if value > margin
    }
    producer_excluded = transcript.scalar("excluded")
    expected_producer_excluded = "1" if any(value >= 0 for value in actual_indices.values()) else "0"
    if producer_excluded != expected_producer_excluded:
        raise ProofObjectError("EXCLUDED_FLAG_MISMATCH")
    independent_excluded = bool(independently_licensed)

    producer_subset = transcript.scalar("krawczyk_subset")
    independent_subset = all(
        strict_inside(value, box)
        for value, box in zip(recomputed_krawczyk, x_box, strict=True)
    )
    if producer_subset == "1" and not independent_subset:
        raise ProofObjectError(
            "MISSING_PROOF_OBJECT: printed precision does not license Krawczyk subset"
        )
    if producer_subset == "0" and independent_subset:
        raise ProofObjectError("KRAWCZYK_SUBSET_FLAG_FALSE_NEGATIVE")
    if producer_subset not in {"0", "1"}:
        raise ProofObjectError("INVALID_KRAWCZYK_SUBSET_FLAG")

    expected_status: str
    if independent_excluded and independent_subset:
        expected_status = "INVALID_EXCLUSION_UNIQUENESS_CONFLICT"
    elif independent_excluded:
        expected_status = "RETURN_EXCLUDED"
    elif independent_subset:
        expected_status = "ROOT_CANDIDATE"
    else:
        expected_status = "UNKNOWN"
    if status != expected_status:
        if producer_excluded == "1" and not independent_excluded:
            raise ProofObjectError(
                "MISSING_PROOF_OBJECT: printed intervals do not license selected separation"
            )
        raise ProofObjectError(
            f"RETURN_STATUS_REPLAY_MISMATCH: expected {expected_status}, got {status}"
        )

    minimum_margin = min(independently_licensed.values(), default=None)
    return {
        "recomputed_mean": [fraction_interval_payload(value) for value in recomputed_mean],
        "recomputed_preconditioned": [
            fraction_interval_payload(value) for value in recomputed_preconditioned
        ],
        "recomputed_krawczyk": [
            fraction_interval_payload(value) for value in recomputed_krawczyk
        ],
        "selected_separation_margin": (
            None if minimum_margin is None else fraction_payload(minimum_margin)
        ),
        "independent_krawczyk_subset": independent_subset,
        "exclusion_uniqueness_conflict": independent_excluded and independent_subset,
    }


def fraction_payload(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def fraction_interval_payload(value: Interval) -> list[dict[str, int]]:
    return [fraction_payload(value[0]), fraction_payload(value[1])]


def box_from_json(payload: Mapping[str, Sequence[str]]) -> dict[str, Interval]:
    if not isinstance(payload, Mapping) or set(payload) != set(COORDINATES):
        raise ProofObjectError("MALFORMED_BOX")
    return {coordinate: interval(payload[coordinate]) for coordinate in COORDINATES}


def plan_root_box(record: Mapping[str, Any]) -> dict[str, Interval]:
    answer: dict[str, Interval] = {}
    for coordinate in COORDINATES:
        center = Fraction(str(record["center"][coordinate]))
        radius = Fraction(str(record["root_radii"][coordinate]))
        answer[coordinate] = center - radius, center + radius
    return answer


def expected_shells(protected: Mapping[str, Interval]) -> dict[str, dict[str, Interval]]:
    if any(
        not strict_inside(protected[coordinate], BIG_BOX[coordinate])
        for coordinate in COORDINATES
    ):
        raise ProofObjectError("PROTECTED_BOX_NOT_STRICT_IN_B_LOC")
    shells: dict[str, dict[str, Interval]] = {}
    prefix = dict(BIG_BOX)
    for index, coordinate in enumerate(COORDINATES):
        lower = dict(prefix)
        upper = dict(prefix)
        lower[coordinate] = BIG_BOX[coordinate][0], protected[coordinate][0]
        upper[coordinate] = protected[coordinate][1], BIG_BOX[coordinate][1]
        shells[f"C{index}L"] = lower
        shells[f"C{index}U"] = upper
        prefix[coordinate] = protected[coordinate]
    return shells


def split_box(box: Mapping[str, Interval]) -> tuple[str, Fraction, dict[str, Interval], dict[str, Interval]]:
    ratios = {
        coordinate: (box[coordinate][1] - box[coordinate][0]) / FULL_WIDTHS[coordinate]
        for coordinate in COORDINATES
    }
    # ``max`` retains the first coordinate on an exact tie, freezing the
    # q_slow, q_fast, p_slow, period tie order independently of the producer.
    coordinate = max(COORDINATES, key=lambda key: ratios[key])
    midpoint = (box[coordinate][0] + box[coordinate][1]) / 2
    left, right = dict(box), dict(box)
    left[coordinate] = box[coordinate][0], midpoint
    right[coordinate] = midpoint, box[coordinate][1]
    return coordinate, midpoint, left, right


def canonical_task_binding(task: Mapping[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(task))


def exact_argv(task: Mapping[str, Any], evaluator_binary_file: str) -> list[str]:
    tree = task["tree"]
    box = task["box"]
    values: list[str] = []
    for coordinate in COORDINATES:
        values.extend(str(value) for value in box[coordinate])
    return [
        evaluator_binary_file,
        str(tree["precision_bits"]),
        *[str(value) for value in task["epsilon"]],
        *values,
    ]


def load_plan(path: Path = PLAN) -> dict[str, Mapping[str, Any]]:
    payload = strict_json_load(path)
    slabs = payload.get("slabs") if isinstance(payload, Mapping) else None
    if not isinstance(slabs, list):
        raise MatrixContractError("PLAN_HAS_NO_SLAB_LIST")
    result: dict[str, Mapping[str, Any]] = {}
    order: list[str] = []
    for record in slabs:
        if not isinstance(record, Mapping):
            raise MatrixContractError("MALFORMED_PLAN_RECORD")
        slab_id = str(record.get("slab_id"))
        if slab_id in result:
            raise MatrixContractError(f"DUPLICATE_PLAN_SLAB: {slab_id}")
        result[slab_id] = record
        order.append(slab_id)
    if tuple(order) != SLAB_IDS:
        raise MatrixContractError("PLAN_IS_NOT_EXACT_ORDERED_S000_TO_S050")
    return result


def _matrix_payload(entries: Any, label: str) -> tuple[TreeKey, ...]:
    if not isinstance(entries, list):
        raise MatrixContractError(f"{label}_MATRIX_NOT_A_LIST")
    parsed: list[TreeKey] = []
    for item in entries:
        if not isinstance(item, Mapping):
            raise MatrixContractError(f"MALFORMED_{label}_MATRIX_ENTRY")
        try:
            parsed.append(TreeKey(int(item["precision_bits"]), str(item["slab_id"])))
        except (KeyError, TypeError, ValueError) as error:
            raise MatrixContractError(f"MALFORMED_{label}_MATRIX_ENTRY") from error
    if len(parsed) != len(set(parsed)):
        raise MatrixContractError(f"DUPLICATE_{label}_MATRIX_ENTRY")
    if tuple(parsed) != exact_matrix():
        raise MatrixContractError(f"INCOMPLETE_OR_REORDERED_{label}_102_MATRIX")
    return tuple(parsed)


def load_formal_context(
    output: Path,
    freeze_path: Path = FORMAL_FREEZE,
    project_root: Path = ROOT,
) -> FormalContext:
    """Load the machine-readable freeze and sealed run configuration.

    The current repository deliberately lacks ``R401_VAL_L2_A1_FREEZE.json``;
    consequently this gate currently rejects every promotion attempt.
    """

    if freeze_path.is_symlink() or not freeze_path.is_file():
        raise CheckerContractError("MISSING_FORMAL_FREEZE")
    freeze = strict_json_load(freeze_path)
    if not isinstance(freeze, Mapping):
        raise CheckerContractError("MALFORMED_FORMAL_FREEZE")
    required_freeze = (
        freeze.get("schema_version") == SCHEMA_VERSION,
        freeze.get("protocol_id") == FORMAL_PROTOCOL_ID,
        freeze.get("status") == "FROZEN_FOR_PRODUCTION",
        freeze.get("scientific_licensing_enabled") is True,
        freeze.get("checker_mode") == "INDEPENDENT_EXACT_RATIONAL_REPLAY",
    )
    if not all(required_freeze):
        raise CheckerContractError("FORMAL_FREEZE_STATUS_OR_NAMESPACE_MISMATCH")
    _matrix_payload(freeze.get("matrix"), "FREEZE")
    frozen_checker_hash = freeze.get("checker_source_sha256")
    if frozen_checker_hash != sha256(CHECKER):
        raise CheckerContractError("FORMAL_FREEZE_CHECKER_HASH_MISMATCH")
    frozen_inputs = freeze.get("input_hashes")
    if not isinstance(frozen_inputs, Mapping) or not set(MANDATORY_FROZEN_INPUTS).issubset(
        frozen_inputs
    ):
        raise CheckerContractError("FORMAL_FREEZE_MISSING_MANDATORY_INPUT_HASHES")
    for relative, expected_hash in frozen_inputs.items():
        if not HEX_SHA256.fullmatch(str(expected_hash)):
            raise CheckerContractError(f"INVALID_FROZEN_INPUT_HASH: {relative}")
        input_path = resolve_bound_path(project_root, str(relative))
        if sha256(input_path) != expected_hash:
            raise CheckerContractError(f"FROZEN_INPUT_HASH_MISMATCH: {relative}")
    checker_relative = "scripts/check_r401_val_l2_all_slabs_independent.py"
    if frozen_inputs.get(checker_relative) != frozen_checker_hash:
        raise CheckerContractError("FORMAL_FREEZE_CHECKER_HASH_DAG_MISMATCH")

    expected_whitelist = {
        "excluded": [
            ["ENERGY_EXCLUDED", 0],
            ["RETURN_EXCLUDED", 0],
        ],
        "splittable": [
            ["ENERGY_DERIVATIVE_FAIL", 3],
            ["ENERGY_GUARD_FAIL", 3],
            ["FLOW_FAIL", 3],
            ["UNKNOWN", 2],
        ],
        "scientific_stop": [["ROOT_CANDIDATE", 4]],
        "invalid": [["INVALID_EXCLUSION_UNIQUENESS_CONFLICT", 5]],
    }
    frozen_scheduler = freeze.get("scheduler")
    if not isinstance(frozen_scheduler, Mapping):
        raise CheckerContractError("FORMAL_FREEZE_HAS_NO_SCHEDULER_CONTRACT")
    workers = frozen_scheduler.get("workers")
    timeout = frozen_scheduler.get("node_timeout_seconds")
    if not (
        frozen_scheduler.get("policy") == EXPECTED_SCHEDULER_POLICY
        and isinstance(workers, int)
        and not isinstance(workers, bool)
        and workers > 0
        and (
            timeout is None
            or (
                isinstance(timeout, int)
                and not isinstance(timeout, bool)
                and timeout > 0
            )
        )
        and frozen_scheduler.get("global_scientific_budget") is None
    ):
        raise CheckerContractError("INVALID_FROZEN_SCHEDULER_CONTRACT")
    frozen_thresholds = freeze.get("logical_thresholds")
    if frozen_thresholds != EXPECTED_LOGICAL_THRESHOLDS:
        raise CheckerContractError("INVALID_FROZEN_LOGICAL_THRESHOLDS")
    frozen_evaluator = freeze.get("evaluator")
    if not isinstance(frozen_evaluator, Mapping):
        raise CheckerContractError("FORMAL_FREEZE_HAS_NO_EVALUATOR_CONTRACT")
    source_file = str(frozen_evaluator.get("source_file", ""))
    source_hash = str(frozen_evaluator.get("source_sha256", ""))
    binary_file = str(frozen_evaluator.get("binary_file", ""))
    binary_hash = str(frozen_evaluator.get("binary_sha256", ""))
    capd_flags = frozen_evaluator.get("capd_flags")
    if not HEX_SHA256.fullmatch(source_hash) or not HEX_SHA256.fullmatch(binary_hash):
        raise CheckerContractError("INVALID_FROZEN_EVALUATOR_HASH")
    if frozen_evaluator.get("capd_commit") != EXPECTED_CAPD_COMMIT:
        raise CheckerContractError("INVALID_FROZEN_CAPD_COMMIT")
    if (
        not isinstance(capd_flags, list)
        or not all(isinstance(flag, str) for flag in capd_flags)
        or not REQUIRED_CAPD_FLAGS.issubset(capd_flags)
    ):
        raise CheckerContractError("INVALID_FROZEN_CAPD_FLAGS")
    if frozen_evaluator.get("status_returncode_whitelist") != expected_whitelist:
        raise CheckerContractError("INVALID_FROZEN_STATUS_WHITELIST")
    source_path = resolve_bound_path(project_root, source_file)
    if sha256(source_path) != source_hash or frozen_inputs.get(source_file) != source_hash:
        raise CheckerContractError("FORMAL_FREEZE_EVALUATOR_SOURCE_HASH_DAG_MISMATCH")
    binary_candidate = Path(binary_file)
    if not binary_candidate.is_absolute() or str(binary_candidate) != binary_file:
        raise CheckerContractError("FROZEN_EVALUATOR_BINARY_PATH_NOT_ABSOLUTE_CANONICAL")
    checked_binary = checked_lexical_path(
        binary_candidate,
        label="EVALUATOR_BINARY",
        require_file=True,
    )
    if sha256(checked_binary) != binary_hash:
        raise CheckerContractError("FROZEN_EVALUATOR_BINARY_HASH_MISMATCH")

    run_config_path = output / "run_config.json"
    if run_config_path.is_symlink() or not run_config_path.is_file():
        raise CheckerContractError("MISSING_SEALED_RUN_CONFIG")
    run_config = strict_json_load(run_config_path)
    if not isinstance(run_config, Mapping):
        raise CheckerContractError("MALFORMED_RUN_CONFIG")
    binding = run_config.get("binding")
    if not isinstance(binding, Mapping):
        raise CheckerContractError("RUN_CONFIG_HAS_NO_BINDING")
    binding_sha = sha256_bytes(canonical_json_bytes(binding))
    if run_config.get("binding_sha256") != binding_sha:
        raise CheckerContractError("RUN_CONFIG_BINDING_HASH_MISMATCH")
    status_null = all(
        run_config.get(key) is None
        for key in ("milestone_status", "theorem_status", "final_status")
    )
    if not (
        run_config.get("schema_version") == SCHEMA_VERSION
        and run_config.get("protocol_id") == FORMAL_PROTOCOL_ID
        and run_config.get("licensing") == "FROZEN_PRODUCTION"
        and status_null
        and binding.get("protocol_id") == FORMAL_PROTOCOL_ID
        and binding.get("scientific_licensing_enabled") is True
    ):
        raise CheckerContractError("RUN_CONFIG_DRAFT_OR_PRODUCER_STATUS_PRESENT")
    _matrix_payload(binding.get("matrix"), "RUN_CONFIG")
    freeze_hash = sha256(freeze_path)
    if binding.get("l2_a1_freeze_sha256") != freeze_hash:
        raise CheckerContractError("RUN_CONFIG_FREEZE_HASH_MISMATCH")
    if binding.get("input_hashes") != frozen_inputs:
        raise CheckerContractError("RUN_CONFIG_INPUT_HASH_DAG_MISMATCH")
    if binding.get("scheduler") != frozen_scheduler:
        raise CheckerContractError("RUN_CONFIG_SCHEDULER_DIFFERS_FROM_FREEZE")
    if binding.get("logical_thresholds") != frozen_thresholds:
        raise CheckerContractError("RUN_CONFIG_THRESHOLDS_DIFFER_FROM_FREEZE")
    limits = binding.get("per_tree_limits")
    frozen_limits = freeze.get("per_tree_limits")
    if not isinstance(limits, Mapping) or limits != frozen_limits:
        raise CheckerContractError("RUN_CONFIG_LIMITS_DIFFER_FROM_FREEZE")
    max_depth, max_nodes = limits.get("max_depth"), limits.get("max_nodes")
    if (
        not isinstance(max_depth, int)
        or isinstance(max_depth, bool)
        or not isinstance(max_nodes, int)
        or isinstance(max_nodes, bool)
        or max_depth < 0
        or max_nodes <= 0
    ):
        raise CheckerContractError("INVALID_FROZEN_PER_TREE_LIMITS")
    evaluator = binding.get("evaluator")
    if not isinstance(evaluator, Mapping):
        raise CheckerContractError("RUN_CONFIG_HAS_NO_EVALUATOR_BINDING")
    if evaluator != frozen_evaluator:
        raise CheckerContractError("RUN_CONFIG_EVALUATOR_DIFFERS_FROM_FREEZE")
    # Recheck the actual bytes after comparing the complete frozen object so a
    # run config cannot merely repeat a plausible-looking digest string.
    if sha256(source_path) != evaluator.get("source_sha256"):
        raise CheckerContractError("RUN_CONFIG_EVALUATOR_SOURCE_HASH_MISMATCH")
    if sha256(checked_binary) != evaluator.get("binary_sha256"):
        raise CheckerContractError("RUN_CONFIG_EVALUATOR_BINARY_HASH_MISMATCH")
    return FormalContext(
        freeze=freeze,
        run_config=run_config,
        freeze_sha256=freeze_hash,
        run_config_sha256=sha256(run_config_path),
        max_depth=max_depth,
        max_nodes=max_nodes,
        evaluator_source_sha256=source_hash,
        evaluator_binary_sha256=binary_hash,
        evaluator_binary_file=binary_file,
        evaluator_capd_commit=EXPECTED_CAPD_COMMIT,
        evaluator_capd_flags=tuple(capd_flags),
        scheduler=dict(frozen_scheduler),
        logical_thresholds=dict(frozen_thresholds),
    )


def expected_tree_path(output: Path, tree: TreeKey) -> Path:
    return output / "trees" / str(tree.precision_bits) / f"{tree.slab_id}.json"


def expected_tree_manifest_path(output: Path, tree: TreeKey) -> Path:
    return output / "tree_manifests" / str(tree.precision_bits) / f"{tree.slab_id}.json"


def validate_exact_pair_paths(
    output: Path,
    matrix: Sequence[TreeKey] | None = None,
) -> tuple[dict[TreeKey, Mapping[str, Any]], dict[TreeKey, Mapping[str, Any]]]:
    selected = tuple(exact_matrix() if matrix is None else matrix)
    tree_paths = {tree: expected_tree_path(output, tree) for tree in selected}
    manifest_paths = {
        tree: expected_tree_manifest_path(output, tree) for tree in selected
    }
    scan_exact_json_paths(output / "trees", tree_paths.values())
    scan_exact_json_paths(output / "tree_manifests", manifest_paths.values())
    trees: dict[TreeKey, Mapping[str, Any]] = {}
    manifests: dict[TreeKey, Mapping[str, Any]] = {}
    seen_tree_identities: set[TreeKey] = set()
    seen_manifest_identities: set[TreeKey] = set()
    for tree in selected:
        tree_payload = strict_json_load(tree_paths[tree])
        manifest = strict_json_load(manifest_paths[tree])
        if not isinstance(tree_payload, Mapping) or not isinstance(manifest, Mapping):
            raise MatrixContractError(f"NONOBJECT_TREE_OR_MANIFEST: {tree.label}")
        for payload, seen, label in (
            (tree_payload, seen_tree_identities, "TREE"),
            (manifest, seen_manifest_identities, "TREE_MANIFEST"),
        ):
            identity = payload.get("tree")
            try:
                internal = TreeKey(
                    int(identity["precision_bits"]), str(identity["slab_id"])
                )
            except (KeyError, TypeError, ValueError) as error:
                raise MatrixContractError(f"MALFORMED_{label}_IDENTITY: {tree.label}") from error
            if internal != tree:
                raise MatrixContractError(f"{label}_PATH_IDENTITY_MISMATCH: {tree.label}")
            if internal in seen:
                raise MatrixContractError(f"DUPLICATE_{label}_IDENTITY: {tree.label}")
            seen.add(internal)
        trees[tree] = tree_payload
        manifests[tree] = manifest
    if len(trees) != len(selected) or len(manifests) != len(selected):
        raise MatrixContractError("MISSING_OR_DUPLICATE_TREE_MANIFEST_PAIR")
    return trees, manifests


def expected_raw_paths(output: Path, tree: TreeKey, node_id: str) -> dict[str, Path]:
    directory = output / "raw" / str(tree.precision_bits) / tree.slab_id / node_id
    return {
        "record": directory / "record.json",
        "stdout": directory / "stdout.txt",
        "stderr": directory / "stderr.txt",
        "telemetry": directory / "telemetry.json",
    }


def validate_raw_file_set(output: Path, expected_nodes: Mapping[TreeKey, set[str]]) -> None:
    raw_root = output / "raw"
    if raw_root.is_symlink() or not raw_root.is_dir():
        raise PathContractError("MISSING_OR_SYMLINK_RAW_ROOT")
    expected_files: set[Path] = set()
    expected_directories: set[Path] = {raw_root}
    for tree, node_ids in expected_nodes.items():
        bits_dir = raw_root / str(tree.precision_bits)
        slab_dir = bits_dir / tree.slab_id
        expected_directories.update((bits_dir, slab_dir))
        for node_id in node_ids:
            paths = expected_raw_paths(output, tree, node_id)
            expected_files.update(paths.values())
            expected_directories.add(paths["record"].parent)
    actual_files: set[Path] = set()
    actual_directories: set[Path] = {raw_root}
    for path in raw_root.rglob("*"):
        if path.is_symlink():
            raise PathContractError(f"SYMLINK_REJECTED: {path}")
        if any(part.startswith(".") for part in path.relative_to(raw_root).parts):
            raise PathContractError(f"HIDDEN_AUTHORITATIVE_PATH: {path}")
        if path.is_dir():
            actual_directories.add(path)
        elif path.is_file():
            actual_files.add(path)
        else:
            raise PathContractError(f"NONREGULAR_RAW_OBJECT: {path}")
    if actual_files != expected_files or actual_directories != expected_directories:
        raise PathContractError(
            "MISSING_EXTRA_RAW_OBJECTS: "
            f"missing_files={sorted(map(str, expected_files - actual_files))}, "
            f"extra_files={sorted(map(str, actual_files - expected_files))}, "
            f"missing_dirs={sorted(map(str, expected_directories - actual_directories))}, "
            f"extra_dirs={sorted(map(str, actual_directories - expected_directories))}"
        )


def verify_transcript_identity(
    transcript: Transcript,
    task: Mapping[str, Any],
) -> None:
    bits = int(transcript.scalar("precision_bits"))
    if bits != int(task["tree"]["precision_bits"]):
        raise ProofObjectError("RAW_TASK_PRECISION_MISMATCH")
    requested_epsilon = interval(task["epsilon"])
    if not subset(requested_epsilon, transcript.intervals("epsilon", 1)[0]):
        raise ProofObjectError("RAW_TASK_EPSILON_NOT_ENCLOSED")
    box = box_from_json(task["box"])
    if not subset(box["q_fast"], transcript.intervals("qplus_input", 1)[0]):
        raise ProofObjectError("RAW_TASK_QFAST_NOT_ENCLOSED")
    reduced = transcript.intervals("reduced_box", 3)
    for coordinate, printed in zip(
        ("q_slow", "p_slow", "period"), reduced, strict=True
    ):
        if not subset(box[coordinate], printed):
            raise ProofObjectError(f"RAW_TASK_{coordinate.upper()}_NOT_ENCLOSED")


def verify_node_record(
    output: Path,
    tree: TreeKey,
    node: Mapping[str, Any],
    context: FormalContext,
) -> dict[str, Any]:
    task = node.get("task")
    if not isinstance(task, Mapping):
        raise ProofObjectError("MISSING_PROOF_OBJECT: node.task")
    node_id = str(task.get("node_id"))
    if not NODE_ID_PATTERN.fullmatch(node_id):
        raise ProofObjectError(f"INVALID_NODE_ID: {node_id}")
    paths = expected_raw_paths(output, tree, node_id)
    record = strict_json_load(paths["record"])
    strict_json_load(paths["telemetry"])
    stdout = paths["stdout"].read_text(encoding="utf-8")
    _stderr = paths["stderr"].read_text(encoding="utf-8")
    if not isinstance(record, Mapping):
        raise ProofObjectError("NODE_RECORD_NOT_AN_OBJECT")
    if not (
        record.get("schema_version") == SCHEMA_VERSION
        and record.get("protocol_id") == FORMAL_PROTOCOL_ID
        and record.get("licensing") == "FROZEN_PRODUCTION"
    ):
        raise ProofObjectError("NODE_RECORD_DRAFT_OR_NAMESPACE_MISMATCH")
    if any(record.get(key) is not None for key in ("milestone_status", "theorem_status", "final_status")):
        raise ProofObjectError("PRODUCER_NODE_ASSIGNED_SCIENTIFIC_STATUS")
    if record.get("task") != task or record.get("task_binding_sha256") != canonical_task_binding(task):
        raise ProofObjectError("NODE_RECORD_TASK_BINDING_MISMATCH")
    if node.get("task_binding_sha256") != record.get("task_binding_sha256"):
        raise ProofObjectError("TREE_NODE_TASK_BINDING_MISMATCH")
    for field, expected in (
        ("run_config_sha256", context.run_config_sha256),
        ("evaluator_source_sha256", context.evaluator_source_sha256),
        ("evaluator_binary_sha256", context.evaluator_binary_sha256),
    ):
        if task.get(field) != expected:
            raise ProofObjectError(f"NODE_{field.upper()}_MISMATCH")
    invocation = record.get("invocation")
    if not isinstance(invocation, Mapping) or not isinstance(invocation.get("argv"), list):
        raise ProofObjectError("MISSING_PROOF_OBJECT: invocation.argv")
    expected_argv = exact_argv(task, context.evaluator_binary_file)
    if invocation.get("argv") != expected_argv:
        raise ProofObjectError("NODE_EXACT_ARGV_MISMATCH")
    if invocation.get("argv_sha256") != sha256_bytes(canonical_json_bytes(expected_argv)):
        raise ProofObjectError("NODE_ARGV_HASH_MISMATCH")
    if node.get("invocation") != invocation:
        raise ProofObjectError("TREE_RECORD_INVOCATION_BINDING_MISMATCH")

    raw_binding = record.get("raw")
    if not isinstance(raw_binding, Mapping):
        raise ProofObjectError("MISSING_PROOF_OBJECT: raw binding")
    expected_relatives = {
        "stdout_file": paths["stdout"].relative_to(output).as_posix(),
        "stderr_file": paths["stderr"].relative_to(output).as_posix(),
    }
    for field, expected in expected_relatives.items():
        resolve_bound_path(output, str(raw_binding.get(field, "")), expected=expected)
    if raw_binding.get("stdout_sha256") != sha256(paths["stdout"]):
        raise ProofObjectError("NODE_STDOUT_HASH_MISMATCH")
    if raw_binding.get("stderr_sha256") != sha256(paths["stderr"]):
        raise ProofObjectError("NODE_STDERR_HASH_MISMATCH")
    if node.get("raw") != raw_binding:
        raise ProofObjectError("TREE_NODE_RAW_BINDING_MISMATCH")

    evaluator_result = record.get("evaluator_result")
    if not isinstance(evaluator_result, Mapping) or node.get("evaluator_result") != evaluator_result:
        raise ProofObjectError("TREE_RECORD_EVALUATOR_RESULT_MISMATCH")
    transcript = Transcript(stdout)
    status = transcript.scalar("status")
    if evaluator_result.get("evaluator_status") != status:
        raise ProofObjectError("RECORDED_EVALUATOR_STATUS_MISMATCH")
    depth = task.get("depth")
    if not isinstance(depth, int) or isinstance(depth, bool):
        raise ProofObjectError("INVALID_NODE_DEPTH")
    action = status_action(
        status,
        evaluator_result.get("returncode"),
        depth=depth,
        max_depth=context.max_depth,
    )
    expected_classification = action
    if action in {"SCIENTIFIC_STOP", "INVALID"}:
        expected_classification = {
            "SCIENTIFIC_STOP": "ROOT_CANDIDATE",
            "INVALID": "INVALID_EVALUATOR_CONFLICT",
        }[action]
    if evaluator_result.get("classification") != expected_classification:
        raise ProofObjectError("RECORDED_CLASSIFICATION_MISMATCH")
    verify_transcript_identity(transcript, task)
    energy = verify_energy_proof(transcript, status)
    return_proof = None
    if status in {
        "RETURN_EXCLUDED",
        "UNKNOWN",
        "ROOT_CANDIDATE",
        "INVALID_EXCLUSION_UNIQUENESS_CONFLICT",
    }:
        return_proof = verify_return_proof(transcript, status)
    return {
        "status": status,
        "action": action,
        "energy": energy,
        "return": return_proof,
    }


def verify_tree_structure(
    tree: TreeKey,
    payload: Mapping[str, Any],
    plan_record: Mapping[str, Any],
    *,
    max_depth: int,
    max_nodes: int,
) -> dict[str, dict[str, Any]]:
    if any(payload.get(key) is not None for key in ("milestone_status", "theorem_status", "final_status")):
        raise ProofObjectError(f"PRODUCER_TREE_ASSIGNED_SCIENTIFIC_STATUS: {tree.label}")
    protected = plan_root_box(plan_record)
    shells = expected_shells(protected)
    expected_epsilon = (
        Fraction(str(plan_record["epsilon_lower"])),
        Fraction(str(plan_record["epsilon_upper"])),
    )
    if interval(payload.get("epsilon")) != expected_epsilon:
        raise ProofObjectError(f"TREE_EPSILON_MISMATCH: {tree.label}")
    domain = payload.get("domain")
    if not isinstance(domain, Mapping):
        raise ProofObjectError(f"TREE_DOMAIN_MISSING: {tree.label}")
    if box_from_json(domain.get("big_box")) != BIG_BOX:
        raise ProofObjectError(f"TREE_BIG_BOX_MISMATCH: {tree.label}")
    if box_from_json(domain.get("protected_exact_plan_box")) != protected:
        raise ProofObjectError(f"TREE_PROTECTED_BOX_MISMATCH: {tree.label}")
    limits = payload.get("per_tree_limits")
    if limits != {"max_depth": max_depth, "max_nodes": max_nodes}:
        raise ProofObjectError(f"TREE_LIMITS_MISMATCH: {tree.label}")
    nodes = payload.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        raise ProofObjectError(f"MISSING_TREE_NODES: {tree.label}")
    if len(nodes) > max_nodes or payload.get("evaluated_node_count") != len(nodes):
        raise ProofObjectError(f"TREE_NODE_BUDGET_OR_COUNT_MISMATCH: {tree.label}")
    by_id: dict[str, dict[str, Any]] = {}
    order: list[tuple[int, str]] = []
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get("task"), Mapping):
            raise ProofObjectError(f"MALFORMED_TREE_NODE: {tree.label}")
        task = node["task"]
        node_id = str(task.get("node_id"))
        depth = task.get("depth")
        if node_id in by_id:
            raise ProofObjectError(f"DUPLICATE_TREE_NODE_ID: {tree.label}/{node_id}")
        if not isinstance(depth, int) or isinstance(depth, bool):
            raise ProofObjectError(f"INVALID_TREE_NODE_DEPTH: {tree.label}/{node_id}")
        by_id[node_id] = node
        order.append((depth, node_id))
    if order != sorted(order):
        raise ProofObjectError(f"NONCANONICAL_TREE_NODE_ORDER: {tree.label}")

    expected: dict[str, tuple[str | None, int, dict[str, Interval]]] = {
        node_id: (None, 0, box) for node_id, box in shells.items()
    }
    stack = list(reversed(list(shells)))
    visited: set[str] = set()
    terminal_counts = {"ENERGY_EXCLUDED": 0, "RETURN_EXCLUDED": 0}
    while stack:
        node_id = stack.pop()
        if node_id in visited:
            raise ProofObjectError(f"DUPLICATE_REACHABLE_NODE: {tree.label}/{node_id}")
        visited.add(node_id)
        node = by_id.get(node_id)
        if node is None:
            raise ProofObjectError(f"MISSING_TREE_NODE: {tree.label}/{node_id}")
        task = node["task"]
        parent_id, depth, box = expected[node_id]
        if (
            task.get("tree") != tree.payload()
            or task.get("parent_id") != parent_id
            or task.get("depth") != depth
            or interval(task.get("epsilon")) != expected_epsilon
            or box_from_json(task.get("box")) != box
        ):
            raise ProofObjectError(f"TREE_NODE_IDENTITY_OR_GEOMETRY_MISMATCH: {tree.label}/{node_id}")
        if depth > max_depth:
            raise ProofObjectError(f"TREE_DEPTH_BUDGET_EXCEEDED: {tree.label}/{node_id}")
        evaluator = node.get("evaluator_result")
        if not isinstance(evaluator, Mapping):
            raise ProofObjectError(f"MISSING_EVALUATOR_RESULT: {tree.label}/{node_id}")
        classification = evaluator.get("classification")
        if classification == "SPLIT":
            coordinate, midpoint, left_box, right_box = split_box(box)
            left_id, right_id = node_id + "0", node_id + "1"
            expected_split = {
                "coordinate": coordinate,
                "midpoint": decimal_fraction_text(midpoint),
                "children": [left_id, right_id],
            }
            if evaluator.get("split") != expected_split:
                raise ProofObjectError(f"SPLIT_DAG_MISMATCH: {tree.label}/{node_id}")
            if depth >= max_depth:
                raise ProofObjectError(f"SPLIT_AT_DEPTH_LIMIT: {tree.label}/{node_id}")
            expected[left_id] = node_id, depth + 1, left_box
            expected[right_id] = node_id, depth + 1, right_box
            stack.extend((right_id, left_id))
        elif classification in terminal_counts:
            terminal_counts[str(classification)] += 1
        else:
            raise ProofObjectError(
                f"NONLICENSING_TREE_CLASSIFICATION: {tree.label}/{node_id}/{classification}"
            )
    if visited != set(by_id):
        raise ProofObjectError(
            f"ORPHAN_OR_UNREACHABLE_TREE_NODES: {tree.label}/{sorted(set(by_id) - visited)}"
        )
    if payload.get("terminal_counts") != terminal_counts:
        raise ProofObjectError(f"TREE_TERMINAL_COUNT_MISMATCH: {tree.label}")
    return by_id


def decimal_fraction_text(value: Fraction) -> str:
    """Return the scheduler-compatible terminating decimal for a midpoint."""

    denominator = value.denominator
    twos = fives = 0
    while denominator % 2 == 0:
        twos += 1
        denominator //= 2
    while denominator % 5 == 0:
        fives += 1
        denominator //= 5
    if denominator != 1:
        raise ProofObjectError("NONTERMINATING_DECIMAL_SPLIT")
    digits = max(twos, fives)
    scaled = value.numerator * (2 ** (digits - twos)) * (5 ** (digits - fives))
    sign = "-" if scaled < 0 else ""
    body = str(abs(scaled)).rjust(digits + 1, "0")
    if digits == 0:
        return sign + body
    result = sign + body[:-digits] + "." + body[-digits:]
    return result.rstrip("0").rstrip(".") or "0"


def verify_tree_manifest(
    output: Path,
    tree: TreeKey,
    payload: Mapping[str, Any],
    manifest: Mapping[str, Any],
    nodes: Mapping[str, Mapping[str, Any]],
    context: FormalContext,
) -> None:
    if any(manifest.get(key) is not None for key in ("milestone_status", "theorem_status", "final_status")):
        raise ProofObjectError(f"PRODUCER_MANIFEST_ASSIGNED_SCIENTIFIC_STATUS: {tree.label}")
    if manifest.get("run_config_sha256") != context.run_config_sha256:
        raise ProofObjectError(f"TREE_MANIFEST_RUN_CONFIG_HASH_MISMATCH: {tree.label}")
    expected_tree_file = expected_tree_path(output, tree).relative_to(output).as_posix()
    resolve_bound_path(output, str(manifest.get("tree_file", "")), expected=expected_tree_file)
    if manifest.get("tree_sha256") != sha256(expected_tree_path(output, tree)):
        raise ProofObjectError(f"TREE_MANIFEST_TREE_HASH_MISMATCH: {tree.label}")
    node_files = manifest.get("node_files")
    if not isinstance(node_files, Mapping) or set(node_files) != set(nodes):
        raise ProofObjectError(f"TREE_MANIFEST_NODE_SET_MISMATCH: {tree.label}")
    for node_id, hashes in node_files.items():
        if not isinstance(hashes, Mapping):
            raise ProofObjectError(f"MALFORMED_NODE_FILE_HASHES: {tree.label}/{node_id}")
        paths = expected_raw_paths(output, tree, str(node_id))
        for label, field in (
            ("record", "record_sha256"),
            ("stdout", "stdout_sha256"),
            ("stderr", "stderr_sha256"),
        ):
            if hashes.get(field) != sha256(paths[label]):
                raise ProofObjectError(f"TREE_MANIFEST_{field.upper()}_MISMATCH: {tree.label}/{node_id}")
        tree_invocation = nodes[str(node_id)].get("invocation")
        record = strict_json_load(paths["record"])
        record_invocation = record.get("invocation") if isinstance(record, Mapping) else None
        if not isinstance(tree_invocation, Mapping) or not isinstance(record_invocation, Mapping):
            raise ProofObjectError(
                f"TREE_MANIFEST_MISSING_INVOCATION: {tree.label}/{node_id}"
            )
        tree_argv = tree_invocation.get("argv")
        if not isinstance(tree_argv, list) or not all(
            isinstance(argument, str) for argument in tree_argv
        ):
            raise ProofObjectError(
                f"TREE_MANIFEST_MALFORMED_INVOCATION: {tree.label}/{node_id}"
            )
        expected_argv_hash = tree_invocation.get("argv_sha256")
        if (
            tree_invocation != record_invocation
            or hashes.get("argv_sha256") != expected_argv_hash
            or expected_argv_hash
            != sha256_bytes(canonical_json_bytes(tree_argv))
        ):
            raise ProofObjectError(
                f"TREE_RECORD_MANIFEST_ARGV_BINDING_MISMATCH: {tree.label}/{node_id}"
            )
    if payload.get("run_config_sha256") != context.run_config_sha256:
        raise ProofObjectError(f"TREE_RUN_CONFIG_HASH_MISMATCH: {tree.label}")


def verify_aggregate_hash_dag(
    output: Path,
    matrix: Sequence[TreeKey],
    manifests: Mapping[TreeKey, Mapping[str, Any]],
    context: FormalContext,
) -> None:
    summary_path = output / "aggregate_summary.json"
    aggregate_path = output / "aggregate_manifest.json"
    summary = strict_json_load(summary_path)
    aggregate = strict_json_load(aggregate_path)
    if not isinstance(summary, Mapping) or not isinstance(aggregate, Mapping):
        raise ProofObjectError("AGGREGATE_OBJECT_NOT_A_MAPPING")
    for payload, label in ((summary, "SUMMARY"), (aggregate, "AGGREGATE_MANIFEST")):
        if not (
            payload.get("schema_version") == SCHEMA_VERSION
            and payload.get("protocol_id") == FORMAL_PROTOCOL_ID
            and payload.get("licensing") == "FROZEN_PRODUCTION"
        ):
            raise ProofObjectError(f"{label}_DRAFT_OR_NAMESPACE_MISMATCH")
        if any(payload.get(key) is not None for key in ("milestone_status", "theorem_status", "final_status")):
            raise ProofObjectError(f"PRODUCER_{label}_ASSIGNED_SCIENTIFIC_STATUS")
        if payload.get("run_config_sha256") != context.run_config_sha256:
            raise ProofObjectError(f"{label}_RUN_CONFIG_HASH_MISMATCH")
    if summary.get("tree_count") != len(matrix):
        raise MatrixContractError("AGGREGATE_SUMMARY_TREE_COUNT_MISMATCH")
    summary_entries = summary.get("trees")
    aggregate_entries = aggregate.get("tree_manifests")
    _matrix_payload(summary_entries, "AGGREGATE_SUMMARY")
    _matrix_payload(aggregate_entries, "AGGREGATE_MANIFEST")
    if summary_entries != aggregate_entries:
        raise ProofObjectError("AGGREGATE_TREE_MANIFEST_LIST_MISMATCH")
    for tree, entry in zip(matrix, summary_entries, strict=True):
        expected_file = expected_tree_manifest_path(output, tree).relative_to(output).as_posix()
        resolve_bound_path(output, str(entry.get("tree_manifest_file", "")), expected=expected_file)
        if entry.get("tree_manifest_sha256") != sha256(expected_tree_manifest_path(output, tree)):
            raise ProofObjectError(f"AGGREGATE_TREE_MANIFEST_HASH_MISMATCH: {tree.label}")
    expected_summary_file = summary_path.relative_to(output).as_posix()
    resolve_bound_path(
        output,
        str(aggregate.get("aggregate_summary_file", "")),
        expected=expected_summary_file,
    )
    if aggregate.get("aggregate_summary_sha256") != sha256(summary_path):
        raise ProofObjectError("AGGREGATE_SUMMARY_HASH_MISMATCH")


def build_archive_provenance_bindings(
    output: Path,
    matrix: Sequence[TreeKey],
    context: FormalContext,
) -> dict[str, Any]:
    """Bind a checker verdict to one exact, non-circular archive generation."""

    manifest_entries = [
        {
            **tree.payload(),
            "tree_manifest_file": expected_tree_manifest_path(output, tree)
            .relative_to(output)
            .as_posix(),
            "tree_manifest_sha256": sha256(expected_tree_manifest_path(output, tree)),
        }
        for tree in matrix
    ]
    root_hash = sha256_bytes(canonical_json_bytes(manifest_entries))
    bindings: dict[str, Any] = {
        "freeze_sha256": context.freeze_sha256,
        "run_config_file": "run_config.json",
        "run_config_sha256": context.run_config_sha256,
        "aggregate_summary_file": "aggregate_summary.json",
        "aggregate_summary_sha256": sha256(output / "aggregate_summary.json"),
        "aggregate_manifest_file": "aggregate_manifest.json",
        "aggregate_manifest_sha256": sha256(output / "aggregate_manifest.json"),
        "evaluator_source_sha256": context.evaluator_source_sha256,
        "evaluator_binary_file": context.evaluator_binary_file,
        "evaluator_binary_sha256": context.evaluator_binary_sha256,
        "capd_commit": context.evaluator_capd_commit,
        "capd_flags": list(context.evaluator_capd_flags),
        "scheduler": dict(context.scheduler),
        "logical_thresholds": dict(context.logical_thresholds),
        "tree_manifest_root": {
            "algorithm": "sha256_canonical_json_ordered_manifest_entries_v1",
            "entry_count": len(manifest_entries),
            "sha256": root_hash,
        },
    }
    bindings["archive_generation_sha256"] = sha256_bytes(
        canonical_json_bytes(bindings)
    )
    return bindings


def verify_l1_authority(
    project_root: Path,
    plan: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    release = strict_json_load(project_root / L1_RELEASE.relative_to(ROOT))
    summary = strict_json_load(project_root / L1_SUMMARY.relative_to(ROOT))
    checker = strict_json_load(project_root / L1_CHECKER.relative_to(ROOT))
    postcheck = strict_json_load(project_root / L1_POSTCHECK.relative_to(ROOT))
    if not (
        release.get("release_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and release.get("final_status") is None
        and summary.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
        and checker.get("checker_status") == "PASS"
        and postcheck.get("checker_status") == "PASS"
        and postcheck.get("milestone_status") == "PASS_CONTIGUOUS_LOCAL_BRANCH"
    ):
        raise ProofObjectError("UPSTREAM_L1_STATUS_CHAIN_FAILED")
    files = release.get("files")
    if not isinstance(files, Mapping):
        raise ProofObjectError("UPSTREAM_L1_RELEASE_HAS_NO_HASH_MAP")
    for value, expected_hash in files.items():
        path = resolve_bound_path(project_root, str(value))
        if sha256(path) != expected_hash:
            raise ProofObjectError(f"UPSTREAM_L1_RELEASE_HASH_MISMATCH: {value}")
    records: dict[TreeKey, Mapping[str, Any]] = {}
    for record in summary.get("records", []):
        if record.get("job_type") != "primary":
            continue
        key = TreeKey(int(record["precision_bits"]), str(record["job_id"]))
        if key in records:
            raise ProofObjectError(f"DUPLICATE_UPSTREAM_L1_PRIMARY: {key.label}")
        records[key] = record
    if set(records) != set(exact_matrix()):
        raise ProofObjectError("UPSTREAM_L1_PRIMARY_MATRIX_NOT_EXACT_102")
    minimum_margin: Fraction | None = None
    for key in exact_matrix():
        record = records[key]
        if record.get("passed") is not True:
            raise ProofObjectError(f"UPSTREAM_L1_PRIMARY_NOT_PASSING: {key.label}")
        requested = plan_root_box(plan[key.slab_id])
        actual = tuple(interval(value) for value in record["root_box"])
        image = tuple(interval(value) for value in record["krawczyk_image"])
        for index, coordinate in enumerate(COORDINATES):
            if not subset(requested[coordinate], actual[index]):
                raise ProofObjectError(f"UPSTREAM_L1_PLAN_NOT_IN_ACTUAL: {key.label}/{coordinate}")
            if not strict_inside(image[index], requested[coordinate]):
                raise ProofObjectError(f"UPSTREAM_L1_IMAGE_NOT_IN_PLAN: {key.label}/{coordinate}")
            margin = min(
                image[index][0] - requested[coordinate][0],
                requested[coordinate][1] - image[index][1],
            )
            minimum_margin = margin if minimum_margin is None else min(minimum_margin, margin)
    return {
        "release_sha256": sha256(project_root / L1_RELEASE.relative_to(ROOT)),
        "minimum_krawczyk_to_plan_boundary_margin": (
            None if minimum_margin is None else fraction_payload(minimum_margin)
        ),
    }


def audit_archive(
    output: Path,
    *,
    project_root: Path = ROOT,
    freeze_path: Path = FORMAL_FREEZE,
) -> dict[str, Any]:
    """Audit one prospective archive; return a non-circular checker payload."""

    failures: list[str] = []
    tree_stats: list[dict[str, Any]] = []
    provenance_bindings: dict[str, Any] | None = None
    checks = 0
    try:
        context = load_formal_context(output, freeze_path, project_root)
    except CheckerContractError as error:
        return {
            "protocol_id": FORMAL_PROTOCOL_ID,
            "checker_mode": CHECKER_MODE,
            "checker_status": "REJECT_DRAFT_NON_LICENSING",
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
            "promotion_authorized": False,
            "aggregate_checks": 1,
            "failure_count": 1,
            "failures": [str(error)],
            "tree_stats": [],
            "checker_source_sha256": sha256(CHECKER),
            "provenance_bindings": None,
        }

    try:
        plan = load_plan(project_root / PLAN.relative_to(ROOT))
        checks += 1
        l1 = verify_l1_authority(project_root, plan)
        checks += 1
        matrix = exact_matrix()
        trees, manifests = validate_exact_pair_paths(output, matrix)
        checks += 2 * len(matrix)
        expected_nodes: dict[TreeKey, set[str]] = {}
        node_maps: dict[TreeKey, dict[str, dict[str, Any]]] = {}
        for tree in matrix:
            payload = trees[tree]
            manifest = manifests[tree]
            if not (
                payload.get("protocol_id") == FORMAL_PROTOCOL_ID
                and manifest.get("protocol_id") == FORMAL_PROTOCOL_ID
                and payload.get("licensing") == "FROZEN_PRODUCTION"
                and manifest.get("licensing") == "FROZEN_PRODUCTION"
            ):
                raise ProofObjectError(f"DRAFT_TREE_NAMESPACE: {tree.label}")
            node_map = verify_tree_structure(
                tree,
                payload,
                plan[tree.slab_id],
                max_depth=context.max_depth,
                max_nodes=context.max_nodes,
            )
            node_maps[tree] = node_map
            expected_nodes[tree] = set(node_map)
            checks += len(node_map)
        validate_raw_file_set(output, expected_nodes)
        checks += sum(len(values) for values in expected_nodes.values())
        for tree in matrix:
            replayed: list[dict[str, Any]] = []
            for node_id in sorted(node_maps[tree]):
                replayed.append(
                    verify_node_record(output, tree, node_maps[tree][node_id], context)
                )
                checks += 1
            verify_tree_manifest(
                output,
                tree,
                trees[tree],
                manifests[tree],
                node_maps[tree],
                context,
            )
            tree_stats.append(
                {
                    **tree.payload(),
                    "node_count": len(node_maps[tree]),
                    "energy_excluded": sum(item["status"] == "ENERGY_EXCLUDED" for item in replayed),
                    "return_excluded": sum(item["status"] == "RETURN_EXCLUDED" for item in replayed),
                    "split_nodes": sum(item["action"] == "SPLIT" for item in replayed),
                }
            )
            checks += 1
        verify_aggregate_hash_dag(output, matrix, manifests, context)
        checks += len(matrix) + 2
        provenance_bindings = build_archive_provenance_bindings(
            output,
            matrix,
            context,
        )
    except CheckerContractError as error:
        failures.append(str(error))
        l1 = None
    except (KeyError, TypeError, ValueError, OSError, UnicodeError) as error:
        failures.append(f"MALFORMED_ARCHIVE: {type(error).__name__}: {error}")
        l1 = None

    passed = not failures
    return {
        "protocol_id": FORMAL_PROTOCOL_ID,
        "checker_mode": CHECKER_MODE,
        "checker_status": "PASS_INDEPENDENT_CHECKER" if passed else "FAIL_INDEPENDENT_CHECKER",
        "milestone_status": "PASS_LOCAL_COMPLEMENT_ALL_SLABS" if passed else None,
        "theorem_status": "PASS_LOCAL_COMPLEMENT_ALL_SLABS" if passed else None,
        "final_status": None,
        "promotion_authorized": passed,
        "aggregate_checks": checks,
        "failure_count": len(failures),
        "failures": failures,
        "tree_stats": tree_stats,
        "l1_protected_box_replay": l1,
        "checker_source_sha256": sha256(CHECKER),
        "provenance_bindings": provenance_bindings,
        "claim_boundary": (
            "pointwise reduced-root uniqueness in the frozen local P_+=0 chart only; "
            "no energy-shell/global, phase-cover, trace-domain, arithmetic-prime, "
            "Hilbert--Polya, zeta-zero, or RH promotion"
        ),
    }


def atomic_write_json(path: Path, payload: Any) -> None:
    if path.is_symlink():
        raise PathContractError(f"SYMLINK_REJECTED_OUTPUT: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.parent / f".{path.name}.tmp-{os.getpid()}"
    if temporary.exists():
        raise PathContractError(f"TEMPORARY_PATH_ALREADY_EXISTS: {temporary}")
    try:
        with temporary.open("xb") as stream:
            stream.write(canonical_json_bytes(payload))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def write_once_or_verify_json(path: Path, payload: Any) -> None:
    """Seal an authoritative result without permitting generation overwrite."""

    expected = canonical_json_bytes(payload)
    if path.exists() or path.is_symlink():
        require_regular_file(path)
        if path.read_bytes() != expected:
            raise PathContractError(
                f"AUTHORITATIVE_RESULT_ALREADY_BOUND_TO_DIFFERENT_GENERATION: {path}"
            )
        return
    atomic_write_json(path, payload)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="DRAFT_NON_LICENSING independent R401-VAL-L2-A1 checker"
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=ROOT / "results/r401_val_l2_all_slabs",
    )
    parser.add_argument("--freeze", type=Path, default=FORMAL_FREEZE)
    args = parser.parse_args()
    output = checked_lexical_path(args.input, label="ARCHIVE_INPUT")
    freeze_path = checked_lexical_path(args.freeze, label="FORMAL_FREEZE")
    payload = audit_archive(output, freeze_path=freeze_path)
    # A rejected draft writes only draft-named diagnostics.  It cannot
    # accidentally occupy the authoritative postcheck namespace.
    if payload["promotion_authorized"]:
        checker_path = output / "independent_checker.json"
        postcheck_path = output / "POSTCHECK_STATUS.json"
    else:
        checker_path = output / "independent_checker.draft.json"
        postcheck_path = output / "DRAFT_POSTCHECK_STATUS.json"
    writer = write_once_or_verify_json if payload["promotion_authorized"] else atomic_write_json
    writer(checker_path, payload)
    provenance = payload.get("provenance_bindings")
    postcheck = {
        "protocol_id": FORMAL_PROTOCOL_ID,
        "checker_mode": CHECKER_MODE,
        "checker_status": payload["checker_status"],
        "milestone_status": payload["milestone_status"],
        "theorem_status": payload["theorem_status"],
        "final_status": None,
        "promotion_authorized": payload["promotion_authorized"],
        "checker_file": checker_path.relative_to(output).as_posix(),
        "checker_sha256": sha256(checker_path),
        "archive_generation_sha256": (
            None
            if not isinstance(provenance, Mapping)
            else provenance.get("archive_generation_sha256")
        ),
        "provenance_bindings_sha256": (
            None
            if not isinstance(provenance, Mapping)
            else sha256_bytes(canonical_json_bytes(provenance))
        ),
    }
    writer(postcheck_path, postcheck)
    print(
        json.dumps(
            {
                "checker_status": payload["checker_status"],
                "promotion_authorized": payload["promotion_authorized"],
                "checks": payload["aggregate_checks"],
                "failures": payload["failure_count"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if payload["promotion_authorized"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
