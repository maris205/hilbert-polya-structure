#!/usr/bin/env python3
"""Fail-closed R401-VAL-L2-A1 cross-tree producer.

This producer can initialize or execute only when a complete machine-readable
L2-A1 freeze validates against the exact bytes in its mandatory input hash
DAG.  ``FROZEN_PRODUCTION`` identifies the archive namespace; the producer
never assigns a theorem, milestone, or final scientific status.  Those three
fields remain null until the independent exact-rational checker has replayed
the complete archive.

The proof semantics of each node remain those of
``capd_r401_local_complement_mp.cpp``.  This scheduler only dispatches exact
boxes, commits evaluator transcripts transactionally, and builds canonical
tree shards.  A future independent checker must replay every proof object.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shlex
import subprocess
import sys
import time
import uuid
from collections import OrderedDict, deque
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from decimal import Decimal, getcontext
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterable, Mapping, Sequence


getcontext().prec = 100

ROOT = Path(__file__).resolve().parents[1]
RUNNER = Path(__file__).resolve()
SOURCE = ROOT / "validated/capd_r401_local_complement_mp.cpp"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
CHECKER = ROOT / "scripts/check_r401_val_l2_all_slabs_independent.py"
FORMAL_PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md"
FORMAL_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L2_A1_FREEZE.json"
MACHINE_FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json"
PREFREEZE_REVIEW = ROOT / "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md"
DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"
L1_RESULT = ROOT / "results/r401_val_l1_branch"
L1_RELEASE = L1_RESULT / "RELEASE_PROVENANCE.json"
L1_SUMMARY = L1_RESULT / "summary.json"
L1_MANIFEST = L1_RESULT / "manifest.json"
L1_CHECKER = L1_RESULT / "independent_checker.json"
L1_POSTCHECK = L1_RESULT / "POSTCHECK_STATUS.json"

PROTOCOL_ID = "R401-VAL-L2-A1"
SCHEMA_VERSION = 1
EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
EXPECTED_CHECKER_MODE = "INDEPENDENT_EXACT_RATIONAL_REPLAY"
EXPECTED_FREEZE_STATUS = "FROZEN_FOR_PRODUCTION"
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
MANDATORY_FROZEN_INPUTS = (
    "scripts/check_r401_val_l2_all_slabs_independent.py",
    "scripts/run_r401_val_l2_all_slabs.py",
    "validated/capd_r401_local_complement_mp.cpp",
    "validated/CAPD_DEPENDENCY.md",
    "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md",
    "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json",
    "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md",
    "research/route_a_wave_trace/R401_VAL_L2_A1_S0_COMPATIBILITY_REPLAY.json",
    "scripts/replay_r401_val_l2_s0_through_a1_checker.py",
    "scripts/build_r401_val_l2_a1_release_provenance.py",
    "research/route_a_wave_trace/R401_VAL_L2_A1_RELEASE_PROVENANCE_CONTRACT.md",
    "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    "results/r401_val_l1_branch/summary.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
)
PREFREEZE_REVIEW_RELATIVE = (
    "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md"
)
S0_REPLAY_RELATIVE = (
    "research/route_a_wave_trace/R401_VAL_L2_A1_S0_COMPATIBILITY_REPLAY.json"
)
S0_ADAPTER_RELATIVE = "scripts/replay_r401_val_l2_s0_through_a1_checker.py"
S0_RESULT_RELATIVE = "results/r401_val_l2_s0_local_complement"
PREFREEZE_ACCEPT_MARKER = "Verdict: ACCEPT_FOR_FREEZE"
EXPECTED_MACHINE_REQUIREMENTS = {
    "cpu_logical": 32,
    "memory_limit_bytes": 64_424_509_440,
    "min_launch_free_bytes": 107_374_182_400,
    "operational_pause_below_free_bytes": 161_061_273_600,
}
PRECISIONS = (128, 256)
SLAB_IDS = tuple(f"S{index:03d}" for index in range(51))
COORDINATES = ("q_slow", "q_fast", "p_slow", "period")
BIG_BOX = {
    "q_slow": (Decimal("-0.02"), Decimal("0.02")),
    "q_fast": (Decimal("0.12"), Decimal("0.17")),
    "p_slow": (Decimal("-0.08"), Decimal("0.08")),
    "period": (Decimal("0.64"), Decimal("0.69")),
}
FULL_WIDTHS = {
    coordinate: upper - lower
    for coordinate, (lower, upper) in BIG_BOX.items()
}
NODE_ID_PATTERN = re.compile(r"^C[0-3][LU][01]*$")
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")

# The evaluator status/return-code relation is a closed whitelist.  In
# particular, malformed output, signals, timeouts, and unknown codes are
# invalid; they are never silently subdivided.
EXCLUDED_RESULTS = {
    ("ENERGY_EXCLUDED", 0): "ENERGY_EXCLUDED",
    ("RETURN_EXCLUDED", 0): "RETURN_EXCLUDED",
}
SPLITTABLE_RESULTS = {
    ("UNKNOWN", 2),
    ("ENERGY_DERIVATIVE_FAIL", 3),
    ("ENERGY_GUARD_FAIL", 3),
    ("FLOW_FAIL", 3),
}
SCIENTIFIC_STOP_RESULTS = {("ROOT_CANDIDATE", 4)}
INVALID_RESULTS = {("INVALID_EXCLUSION_UNIQUENESS_CONFLICT", 5)}


class SchedulerContractError(RuntimeError):
    """Base class for prospective scheduler contract failures."""


class ResumeBindingError(SchedulerContractError):
    """The requested resume does not match the immutable run generation."""


class CorruptShardError(SchedulerContractError):
    """A committed shard or its transcript failed strict validation."""


class MatrixContractError(SchedulerContractError):
    """The canonical pair/tree/manifest matrix is incomplete or ambiguous."""


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CorruptShardError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_loads(raw: str) -> Any:
    """Parse JSON while rejecting duplicate object keys and non-finite data."""

    def reject_constant(value: str) -> None:
        raise CorruptShardError(f"non-finite JSON constant: {value}")

    def parse_finite_float(value: str) -> float:
        parsed = float(value)
        if not math.isfinite(parsed):
            raise CorruptShardError(f"non-finite JSON number: {value}")
        return parsed

    try:
        return json.loads(
            raw,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=reject_constant,
            parse_float=parse_finite_float,
        )
    except CorruptShardError:
        raise
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        raise CorruptShardError(f"malformed JSON: {error}") from error


def strict_json_load(path: Path) -> Any:
    if path.is_symlink():
        raise CorruptShardError(f"symlink is not authoritative input: {path}")
    if not path.is_file():
        raise CorruptShardError(f"missing regular JSON file: {path}")
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


def exact_json_equal(actual: Any, expected: Any) -> bool:
    """Compare JSON values without bool/int/float equality coercion."""

    try:
        return canonical_json_bytes(actual) == canonical_json_bytes(expected)
    except (TypeError, ValueError):
        return False


def markdown_has_verdict_declaration(line: str) -> bool:
    """Fail closed on any standalone ``Verdict`` token in a review line.

    The exact accepted byte line is checked separately.  Treating every token
    as a declaration candidate closes Markdown tables, list/quote decoration,
    Unicode punctuation, and dash-separated near-marker aliases.
    """

    return re.search(
        r"(?<![A-Za-z0-9_])Verdict(?![A-Za-z0-9_])", line, re.IGNORECASE
    ) is not None


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    if path.is_symlink() or not path.is_file():
        raise CorruptShardError(f"cannot hash non-regular file: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def atomic_write_bytes(path: Path, payload: bytes) -> None:
    """Durably replace one file using a same-directory temporary file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.parent / f".{path.name}.tmp-{os.getpid()}-{uuid.uuid4().hex}"
    try:
        with temporary.open("xb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        fsync_directory(path.parent)
    finally:
        if temporary.exists():
            temporary.unlink()


def atomic_write_json(path: Path, payload: Any) -> None:
    atomic_write_bytes(path, canonical_json_bytes(payload))


def write_once_or_verify(path: Path, payload: Any) -> None:
    """Create an immutable canonical JSON file, or verify the existing bytes."""

    expected = canonical_json_bytes(payload)
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file():
            raise CorruptShardError(f"immutable path is not a regular file: {path}")
        if path.read_bytes() != expected:
            raise CorruptShardError(f"immutable JSON differs from recomputation: {path}")
        return
    atomic_write_bytes(path, expected)


def safe_relative_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise CorruptShardError(f"unsafe relative path: {value!r}")
    candidate = PurePosixPath(value)
    if (
        candidate.is_absolute()
        or not candidate.parts
        or "\\" in value
        or ".." in candidate.parts
        or any(part.startswith(".") for part in candidate.parts)
        or candidate.as_posix() != value
    ):
        raise CorruptShardError(f"unsafe relative path: {value!r}")
    if any(part in {"", "."} for part in candidate.parts):
        raise CorruptShardError(f"non-canonical relative path: {value!r}")
    return candidate


def resolve_project_input(project_root: Path, value: str) -> Path:
    """Resolve one frozen project-relative file without following symlinks."""

    relative = safe_relative_path(value)
    candidate = checked_lexical_path(
        project_root / Path(*relative.parts),
        label=f"frozen input {value}",
        require_file=True,
    )
    lexical_root = Path(os.path.abspath(os.fspath(project_root)))
    try:
        candidate.relative_to(lexical_root)
    except ValueError as error:
        raise SchedulerContractError(
            f"frozen input escapes project root: {value}"
        ) from error
    return candidate


def checked_lexical_path(
    value: Path,
    *,
    label: str,
    require_file: bool = False,
    require_directory: bool = False,
    allow_missing_leaf: bool = False,
) -> Path:
    """Return an absolute path only after rejecting every symlink component.

    ``Path.resolve()`` follows symlinks and therefore cannot be used before a
    provenance check: after resolution, ``is_symlink()`` observes the target,
    not the user-supplied link.  This helper first constructs a lexical
    absolute path (normalizing ``.``/``..`` without resolving links), walks
    every existing component with ``lstat`` semantics via ``is_symlink()``,
    and only then validates the requested leaf type.
    """

    lexical = Path(os.path.abspath(os.fspath(value)))
    cursor = Path(lexical.anchor)
    for part in lexical.parts[1:]:
        cursor = cursor / part
        if cursor.is_symlink():
            raise SchedulerContractError(
                f"{label} contains a symlink component: {cursor}"
            )
        if not cursor.exists():
            if allow_missing_leaf and cursor == lexical:
                break
            # A missing parent is rejected even for a not-yet-created output.
            if cursor != lexical:
                raise SchedulerContractError(
                    f"{label} has a missing parent component: {cursor}"
                )
    if require_file and not lexical.is_file():
        raise SchedulerContractError(f"{label} is not a regular file: {lexical}")
    if require_directory and not lexical.is_dir():
        raise SchedulerContractError(f"{label} is not a directory: {lexical}")
    if not allow_missing_leaf and not lexical.exists():
        raise SchedulerContractError(f"{label} does not exist: {lexical}")
    return lexical


def decimal_text(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text if text not in {"", "-0"} else "0"


def interval_text(value: tuple[Decimal, Decimal]) -> list[str]:
    return [decimal_text(value[0]), decimal_text(value[1])]


def decimal_interval(value: Sequence[str]) -> tuple[Decimal, Decimal]:
    if len(value) != 2:
        raise CorruptShardError(f"interval has length {len(value)}, expected 2")
    result = Decimal(value[0]), Decimal(value[1])
    if result[0] > result[1]:
        raise CorruptShardError(f"reversed interval: {value}")
    return result


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
class NodeTask:
    tree: TreeKey
    node_id: str
    parent_id: str | None
    depth: int
    epsilon: tuple[Decimal, Decimal]
    box: Mapping[str, tuple[Decimal, Decimal]]
    evaluator_path: str
    run_config_sha256: str
    evaluator_source_sha256: str
    evaluator_binary_sha256: str

    def payload(self) -> dict[str, Any]:
        return {
            "tree": self.tree.payload(),
            "node_id": self.node_id,
            "parent_id": self.parent_id,
            "depth": self.depth,
            "epsilon": interval_text(self.epsilon),
            "box": {coordinate: interval_text(self.box[coordinate]) for coordinate in COORDINATES},
            "evaluator_path": self.evaluator_path,
            "run_config_sha256": self.run_config_sha256,
            "evaluator_source_sha256": self.evaluator_source_sha256,
            "evaluator_binary_sha256": self.evaluator_binary_sha256,
        }

    @property
    def binding_sha256(self) -> str:
        return sha256_bytes(canonical_json_bytes(self.payload()))

    def arguments(self) -> list[str]:
        values: list[str] = []
        for coordinate in COORDINATES:
            values.extend(interval_text(self.box[coordinate]))
        return [
            self.evaluator_path,
            str(self.tree.precision_bits),
            *interval_text(self.epsilon),
            *values,
        ]


@dataclass(frozen=True)
class EvaluatorOutcome:
    stdout: str
    stderr: str
    returncode: int | None
    timed_out: bool = False
    wall_seconds: float | None = None


@dataclass
class ReconstructedTree:
    tree: TreeKey
    records: dict[str, dict[str, Any]]
    pending: list[NodeTask]
    blocking_classifications: list[str]

    @property
    def complete(self) -> bool:
        return bool(self.records) and not self.pending and not self.blocking_classifications


@dataclass(frozen=True)
class FormalFreezeContext:
    """Validated immutable inputs that authorize one formal generation."""

    freeze: Mapping[str, Any]
    freeze_path: Path
    freeze_sha256: str
    input_hashes: Mapping[str, str]
    per_tree_limits: Mapping[str, int]
    scheduler: Mapping[str, Any]
    evaluator: Mapping[str, Any]
    logical_thresholds: Mapping[str, str]


def load_plan_records(path: Path = PLAN) -> OrderedDict[str, dict[str, Any]]:
    payload = strict_json_load(path)
    slabs = payload.get("slabs") if isinstance(payload, dict) else None
    if not isinstance(slabs, list):
        raise MatrixContractError("L1 plan has no slab list")
    records: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for record in slabs:
        slab_id = record.get("slab_id")
        if not isinstance(slab_id, str):
            raise MatrixContractError("plan slab_id is not an exact string")
        if slab_id in records:
            raise MatrixContractError(f"duplicate plan slab: {slab_id}")
        records[slab_id] = record
    if tuple(records) != SLAB_IDS:
        raise MatrixContractError(
            f"expected ordered slabs S000..S050, found {tuple(records)}"
        )
    return records


def exact_production_matrix(
    plan_records: Mapping[str, Mapping[str, Any]],
) -> tuple[TreeKey, ...]:
    if tuple(plan_records) != SLAB_IDS:
        raise MatrixContractError("plan records do not form the exact 51-slab order")
    matrix = tuple(
        TreeKey(bits, slab_id)
        for bits in PRECISIONS
        for slab_id in SLAB_IDS
    )
    if len(matrix) != 102 or len(set(matrix)) != 102:
        raise AssertionError("internal 102-pair matrix construction failed")
    return matrix


def plan_root_box(record: Mapping[str, Any]) -> dict[str, tuple[Decimal, Decimal]]:
    answer: dict[str, tuple[Decimal, Decimal]] = {}
    for coordinate in COORDINATES:
        center = Decimal(str(record["center"][coordinate]))
        radius = Decimal(str(record["root_radii"][coordinate]))
        answer[coordinate] = center - radius, center + radius
    return answer


def strict_inside(
    inner: Mapping[str, tuple[Decimal, Decimal]],
    outer: Mapping[str, tuple[Decimal, Decimal]],
) -> bool:
    return all(
        outer[coordinate][0]
        < inner[coordinate][0]
        < inner[coordinate][1]
        < outer[coordinate][1]
        for coordinate in COORDINATES
    )


def complement_shells(
    protected: Mapping[str, tuple[Decimal, Decimal]],
) -> list[tuple[str, dict[str, tuple[Decimal, Decimal]]]]:
    """Return the eight closed shells covering B_loc minus int(P_j)."""

    if not strict_inside(protected, BIG_BOX):
        raise MatrixContractError("protected exact plan box is not strict in B_loc")
    shells: list[tuple[str, dict[str, tuple[Decimal, Decimal]]]] = []
    prefix = dict(BIG_BOX)
    for index, coordinate in enumerate(COORDINATES):
        lower = dict(prefix)
        upper = dict(prefix)
        lower[coordinate] = BIG_BOX[coordinate][0], protected[coordinate][0]
        upper[coordinate] = protected[coordinate][1], BIG_BOX[coordinate][1]
        shells.append((f"C{index}L", lower))
        shells.append((f"C{index}U", upper))
        prefix[coordinate] = protected[coordinate]
    return shells


def make_node_task(
    *,
    tree: TreeKey,
    node_id: str,
    parent_id: str | None,
    depth: int,
    epsilon: tuple[Decimal, Decimal],
    box: Mapping[str, tuple[Decimal, Decimal]],
    evaluator_path: str,
    run_config_sha256: str,
    evaluator_source_sha256: str,
    evaluator_binary_sha256: str,
) -> NodeTask:
    if not NODE_ID_PATTERN.fullmatch(node_id):
        raise SchedulerContractError(f"non-canonical node ID: {node_id}")
    if parent_id is not None and not NODE_ID_PATTERN.fullmatch(parent_id):
        raise SchedulerContractError(f"non-canonical parent ID: {parent_id}")
    if depth < 0:
        raise SchedulerContractError("negative node depth")
    if set(box) != set(COORDINATES):
        raise SchedulerContractError("node box coordinate set mismatch")
    parsed_evaluator_path = Path(evaluator_path)
    if (
        not parsed_evaluator_path.is_absolute()
        or ".." in parsed_evaluator_path.parts
        or str(parsed_evaluator_path) != evaluator_path
    ):
        raise SchedulerContractError(
            f"evaluator path is not absolute and canonical: {evaluator_path!r}"
        )
    return NodeTask(
        tree=tree,
        node_id=node_id,
        parent_id=parent_id,
        depth=depth,
        epsilon=epsilon,
        box=dict(box),
        evaluator_path=evaluator_path,
        run_config_sha256=run_config_sha256,
        evaluator_source_sha256=evaluator_source_sha256,
        evaluator_binary_sha256=evaluator_binary_sha256,
    )


def root_tasks(
    tree: TreeKey,
    record: Mapping[str, Any],
    *,
    evaluator_path: str,
    run_config_sha256: str,
    evaluator_source_sha256: str,
    evaluator_binary_sha256: str,
) -> list[NodeTask]:
    epsilon = Decimal(str(record["epsilon_lower"])), Decimal(str(record["epsilon_upper"]))
    return [
        make_node_task(
            tree=tree,
            node_id=node_id,
            parent_id=None,
            depth=0,
            epsilon=epsilon,
            box=box,
            evaluator_path=evaluator_path,
            run_config_sha256=run_config_sha256,
            evaluator_source_sha256=evaluator_source_sha256,
            evaluator_binary_sha256=evaluator_binary_sha256,
        )
        for node_id, box in complement_shells(plan_root_box(record))
    ]


def split_task(task: NodeTask) -> tuple[str, Decimal, NodeTask, NodeTask]:
    # max() is stable, so COORDINATES supplies the frozen tie-break order.
    coordinate = max(
        COORDINATES,
        key=lambda key: (task.box[key][1] - task.box[key][0]) / FULL_WIDTHS[key],
    )
    lower, upper = task.box[coordinate]
    midpoint = (lower + upper) / 2
    if not lower < midpoint < upper:
        raise SchedulerContractError(f"non-strict split midpoint for {task.node_id}")
    left_box = dict(task.box)
    right_box = dict(task.box)
    left_box[coordinate] = lower, midpoint
    right_box[coordinate] = midpoint, upper

    def child(suffix: str, child_box: Mapping[str, tuple[Decimal, Decimal]]) -> NodeTask:
        return make_node_task(
            tree=task.tree,
            node_id=task.node_id + suffix,
            parent_id=task.node_id,
            depth=task.depth + 1,
            epsilon=task.epsilon,
            box=child_box,
            evaluator_path=task.evaluator_path,
            run_config_sha256=task.run_config_sha256,
            evaluator_source_sha256=task.evaluator_source_sha256,
            evaluator_binary_sha256=task.evaluator_binary_sha256,
        )

    return coordinate, midpoint, child("0", left_box), child("1", right_box)


class FairNodeQueue:
    """Deterministic round-robin admission across nonempty tree queues."""

    def __init__(self, matrix: Sequence[TreeKey]):
        self._matrix = tuple(matrix)
        self._queues: OrderedDict[TreeKey, deque[NodeTask]] = OrderedDict(
            (tree, deque()) for tree in self._matrix
        )
        self._active: deque[TreeKey] = deque()
        self._active_set: set[TreeKey] = set()
        self._seen_node_ids: set[tuple[TreeKey, str]] = set()

    def extend(self, tree: TreeKey, tasks: Iterable[NodeTask]) -> None:
        if tree not in self._queues:
            raise MatrixContractError(f"task for tree outside matrix: {tree.label}")
        new_tasks = list(tasks)
        new_identities: list[tuple[TreeKey, str]] = []
        for task in new_tasks:
            if task.tree != tree:
                raise SchedulerContractError("task inserted into the wrong tree queue")
            identity = tree, task.node_id
            if identity in self._seen_node_ids or identity in new_identities:
                raise SchedulerContractError(
                    f"node scheduled more than once: {tree.label}/{task.node_id}"
                )
            new_identities.append(identity)
        queue = self._queues[tree]
        self._seen_node_ids.update(new_identities)
        for task in new_tasks:
            queue.append(task)
        if queue and tree not in self._active_set:
            self._active.append(tree)
            self._active_set.add(tree)

    def discard_tree(self, tree: TreeKey) -> list[NodeTask]:
        discarded = list(self._queues[tree])
        self._queues[tree].clear()
        if tree in self._active_set:
            self._active = deque(candidate for candidate in self._active if candidate != tree)
            self._active_set.remove(tree)
        return discarded

    def pop_batch(
        self,
        limit: int,
        admissible: Callable[[TreeKey], bool] | None = None,
        on_accept: Callable[[TreeKey], None] | None = None,
    ) -> list[NodeTask]:
        if limit < 0:
            raise ValueError("negative batch limit")
        accepted: list[NodeTask] = []
        # Inspect each currently active tree at most once.  Re-appending a
        # nonempty queue makes it eligible for the *next* barrier, never for a
        # second in-flight node in this barrier.  This remains true when the
        # worker count exceeds the number of active trees.
        active_at_barrier = len(self._active)
        for _ in range(active_at_barrier):
            if not self._active or len(accepted) >= limit:
                break
            tree = self._active.popleft()
            self._active_set.remove(tree)
            queue = self._queues[tree]
            if admissible is not None and not admissible(tree):
                # Keep the pending frontier intact for a later session.
                self._active.append(tree)
                self._active_set.add(tree)
                continue
            accepted.append(queue.popleft())
            if on_accept is not None:
                on_accept(tree)
            if queue:
                self._active.append(tree)
                self._active_set.add(tree)
        if len({task.tree for task in accepted}) != len(accepted):
            raise AssertionError("barrier admitted more than one node from one tree")
        return accepted

    def pending_counts(self) -> dict[TreeKey, int]:
        return {tree: len(queue) for tree, queue in self._queues.items()}

    def __bool__(self) -> bool:
        return bool(self._active)


def extract_last_status(stdout: str) -> str | None:
    values = [
        line[len("status=") :].strip()
        for line in stdout.splitlines()
        if line.startswith("status=")
    ]
    # The frozen evaluator emits exactly one terminal status.  Missing or
    # repeated status fields are malformed, even if their last values agree.
    return values[0] if len(values) == 1 else None


def classify_outcome(
    task: NodeTask,
    outcome: EvaluatorOutcome,
    *,
    max_depth: int,
) -> dict[str, Any]:
    status = extract_last_status(outcome.stdout)
    returncode_is_exact_int = isinstance(outcome.returncode, int) and not isinstance(
        outcome.returncode, bool
    )
    key = status, outcome.returncode if returncode_is_exact_int else None
    if outcome.timed_out:
        classification = "INVALID_TIMEOUT"
    elif key in EXCLUDED_RESULTS:
        classification = EXCLUDED_RESULTS[key]
    elif key in SCIENTIFIC_STOP_RESULTS:
        classification = "ROOT_CANDIDATE"
    elif key in INVALID_RESULTS:
        classification = "INVALID_EVALUATOR_CONFLICT"
    elif key in SPLITTABLE_RESULTS:
        classification = "RESOURCE_EXHAUSTED_DEPTH" if task.depth >= max_depth else "SPLIT"
    else:
        classification = "INVALID_EVALUATOR_RESULT"
    result: dict[str, Any] = {
        "evaluator_status": status,
        "returncode": outcome.returncode,
        "classification": classification,
    }
    if classification == "SPLIT":
        coordinate, midpoint, left, right = split_task(task)
        result["split"] = {
            "coordinate": coordinate,
            "midpoint": decimal_text(midpoint),
            "children": [left.node_id, right.node_id],
        }
    return result


def node_commit_directory(output: Path, task: NodeTask) -> Path:
    return output / "raw" / str(task.tree.precision_bits) / task.tree.slab_id / task.node_id


def node_record_path(output: Path, task: NodeTask) -> Path:
    return node_commit_directory(output, task) / "record.json"


def _relative_to_output(output: Path, path: Path) -> str:
    return path.relative_to(output).as_posix()


def build_node_record(
    output: Path,
    task: NodeTask,
    outcome: EvaluatorOutcome,
    *,
    max_depth: int,
) -> dict[str, Any]:
    final_directory = node_commit_directory(output, task)
    classification = classify_outcome(task, outcome, max_depth=max_depth)
    argv = task.arguments()
    if len(argv) != 12 or not all(isinstance(argument, str) for argument in argv):
        raise SchedulerContractError("internal evaluator argv is not exactly 12 strings")
    record = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "task": task.payload(),
        "task_binding_sha256": task.binding_sha256,
        "invocation": {
            "argv": argv,
            "argv_sha256": sha256_bytes(canonical_json_bytes(argv)),
        },
        "evaluator_result": classification,
        "raw": {
            "stdout_file": _relative_to_output(output, final_directory / "stdout.txt"),
            "stdout_sha256": sha256_bytes(outcome.stdout.encode("utf-8")),
            "stderr_file": _relative_to_output(output, final_directory / "stderr.txt"),
            "stderr_sha256": sha256_bytes(outcome.stderr.encode("utf-8")),
        },
    }
    return record


def _write_and_fsync(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def commit_node_transaction(
    output: Path,
    task: NodeTask,
    outcome: EvaluatorOutcome,
    *,
    max_depth: int,
) -> dict[str, Any]:
    """Commit stdout, stderr, telemetry, then record.json as one directory.

    The directory rename is the transaction commit.  Hidden temporary
    directories are never treated as authoritative by resume scanning.
    """

    final_directory = node_commit_directory(output, task)
    if final_directory.exists() or final_directory.is_symlink():
        existing = validate_committed_node(output, task, max_depth=max_depth)
        expected = build_node_record(output, task, outcome, max_depth=max_depth)
        if existing != expected:
            raise CorruptShardError(
                f"refusing a second, different commit for {task.tree.label}/{task.node_id}"
            )
        return existing
    parent = final_directory.parent
    parent.mkdir(parents=True, exist_ok=True)
    temporary = parent / f".{task.node_id}.tmp-{os.getpid()}-{uuid.uuid4().hex}"
    temporary.mkdir()
    try:
        record = build_node_record(output, task, outcome, max_depth=max_depth)
        _write_and_fsync(temporary / "stdout.txt", outcome.stdout.encode("utf-8"))
        _write_and_fsync(temporary / "stderr.txt", outcome.stderr.encode("utf-8"))
        telemetry = {
            "wall_seconds": outcome.wall_seconds,
            "note": "operational telemetry; excluded from canonical proof tree and manifest",
        }
        _write_and_fsync(temporary / "telemetry.json", canonical_json_bytes(telemetry))
        # The record is the internal commit marker and is written last inside
        # the staging directory.  The directory itself becomes authoritative
        # only at the atomic rename below.
        _write_and_fsync(temporary / "record.json", canonical_json_bytes(record))
        fsync_directory(temporary)
        try:
            os.rename(temporary, final_directory)
        except FileExistsError:
            # Another process won the exact same commit.  Preserve both data
            # sets until the committed copy has been validated.
            existing = validate_committed_node(output, task, max_depth=max_depth)
            if existing != record:
                raise CorruptShardError(
                    f"concurrent nonidentical commit for {task.tree.label}/{task.node_id}"
                )
            return existing
        fsync_directory(parent)
        return validate_committed_node(output, task, max_depth=max_depth)
    finally:
        # A crash leaves a hidden non-authoritative staging directory.  During
        # normal exceptions we remove only the directory created by this call.
        if temporary.exists():
            for child in temporary.iterdir():
                child.unlink()
            temporary.rmdir()


def _record_task_payload(record: Mapping[str, Any]) -> Mapping[str, Any]:
    task = record.get("task")
    if not isinstance(task, dict):
        raise CorruptShardError("node record has no task object")
    return task


def validate_committed_node(
    output: Path,
    task: NodeTask,
    *,
    max_depth: int,
) -> dict[str, Any]:
    directory = node_commit_directory(output, task)
    if directory.is_symlink() or not directory.is_dir():
        raise CorruptShardError(f"node commit is not a regular directory: {directory}")
    allowed = {"stdout.txt", "stderr.txt", "record.json", "telemetry.json"}
    actual = {path.name for path in directory.iterdir()}
    if actual != allowed:
        raise CorruptShardError(
            f"node commit file set mismatch for {task.tree.label}/{task.node_id}: {actual}"
        )
    if any(path.is_symlink() or not path.is_file() for path in directory.iterdir()):
        raise CorruptShardError(f"node commit contains non-regular file: {directory}")
    record = strict_json_load(directory / "record.json")
    expected_status_nulls = (
        record.get("milestone_status") is None,
        record.get("theorem_status") is None,
        record.get("final_status") is None,
    )
    if (
        type(record.get("schema_version")) is not int
        or record.get("schema_version") != SCHEMA_VERSION
        or record.get("protocol_id") != PROTOCOL_ID
        or record.get("licensing") != "FROZEN_PRODUCTION"
        or record.get("scientific_licensing_enabled") is not True
        or not all(expected_status_nulls)
    ):
        raise CorruptShardError("node record frozen/status namespace mismatch")
    if not exact_json_equal(_record_task_payload(record), task.payload()):
        raise ResumeBindingError(
            f"node task binding mismatch: {task.tree.label}/{task.node_id}"
        )
    if record.get("task_binding_sha256") != task.binding_sha256:
        raise ResumeBindingError(
            f"node task hash mismatch: {task.tree.label}/{task.node_id}"
        )
    invocation = record.get("invocation")
    if not isinstance(invocation, dict):
        raise CorruptShardError(
            f"node record has no exact invocation: {task.tree.label}/{task.node_id}"
        )
    argv = invocation.get("argv")
    expected_argv = task.arguments()
    if (
        not isinstance(argv, list)
        or len(argv) != 12
        or not all(isinstance(argument, str) for argument in argv)
        or argv != expected_argv
    ):
        raise CorruptShardError(
            f"invocation argv mismatch: {task.tree.label}/{task.node_id}"
        )
    expected_argv_sha256 = sha256_bytes(canonical_json_bytes(expected_argv))
    if invocation.get("argv_sha256") != expected_argv_sha256:
        raise CorruptShardError(
            f"invocation argv hash mismatch: {task.tree.label}/{task.node_id}"
        )
    raw = record.get("raw")
    if not isinstance(raw, dict):
        raise CorruptShardError("node record has no raw binding")
    expected_paths = {
        "stdout_file": _relative_to_output(output, directory / "stdout.txt"),
        "stderr_file": _relative_to_output(output, directory / "stderr.txt"),
    }
    for field, expected_relative in expected_paths.items():
        value = str(raw.get(field, ""))
        safe_relative_path(value)
        if value != expected_relative:
            raise CorruptShardError(f"non-canonical raw path in {field}: {value}")
    stdout_path = output / str(raw["stdout_file"])
    stderr_path = output / str(raw["stderr_file"])
    if sha256(stdout_path) != raw.get("stdout_sha256"):
        raise CorruptShardError(f"stdout hash mismatch: {stdout_path}")
    if sha256(stderr_path) != raw.get("stderr_sha256"):
        raise CorruptShardError(f"stderr hash mismatch: {stderr_path}")
    stdout = stdout_path.read_text(encoding="utf-8")
    stored_result = record.get("evaluator_result")
    if not isinstance(stored_result, dict):
        raise CorruptShardError("node record has no evaluator result")
    replay = classify_outcome(
        task,
        EvaluatorOutcome(
            stdout=stdout,
            stderr=stderr_path.read_text(encoding="utf-8"),
            returncode=stored_result.get("returncode"),
            timed_out=stored_result.get("classification") == "INVALID_TIMEOUT",
        ),
        max_depth=max_depth,
    )
    if replay != stored_result:
        raise CorruptShardError(
            f"status/return-code/classification replay mismatch: {task.tree.label}/{task.node_id}"
        )
    return record


def scan_committed_node_records(output: Path) -> dict[tuple[TreeKey, str], Path]:
    raw_root = output / "raw"
    if not raw_root.exists():
        return {}
    if raw_root.is_symlink() or not raw_root.is_dir():
        raise CorruptShardError("raw root is not a regular directory")
    for candidate in raw_root.rglob("*"):
        relative_candidate = candidate.relative_to(raw_root)
        if any(part.startswith(".") for part in relative_candidate.parts):
            continue
        if candidate.is_symlink():
            raise CorruptShardError(f"symlink in authoritative raw archive: {candidate}")
    records: dict[tuple[TreeKey, str], Path] = {}
    for record_path in sorted(raw_root.rglob("record.json")):
        if record_path.is_symlink():
            raise CorruptShardError(f"symlink node record: {record_path}")
        relative = record_path.relative_to(raw_root)
        if any(part.startswith(".") for part in relative.parts):
            # An interrupted transaction is never authoritative.  It remains
            # preserved on disk for post-mortem inspection and is ignored by
            # resume until an operator explicitly quarantines it.
            continue
        if len(relative.parts) != 4 or relative.parts[-1] != "record.json":
            raise CorruptShardError(f"non-canonical node record path: {relative}")
        bits_text, slab_id, node_id, _name = relative.parts
        try:
            tree = TreeKey(int(bits_text), slab_id)
        except ValueError as error:
            raise CorruptShardError(f"invalid precision path: {relative}") from error
        if tree.precision_bits not in PRECISIONS or tree.slab_id not in SLAB_IDS:
            raise CorruptShardError(f"node record outside exact matrix: {relative}")
        if not NODE_ID_PATTERN.fullmatch(node_id):
            raise CorruptShardError(f"invalid node path ID: {relative}")
        identity = tree, node_id
        if identity in records:
            raise CorruptShardError(f"duplicate node identity: {tree.label}/{node_id}")
        records[identity] = record_path
    # JSON files other than the exact record/telemetry names could provide an
    # ambiguous second authoritative record and are rejected.  Hidden staging
    # directories are ignored because their names begin with a dot and they
    # are not committed generations.
    for json_path in sorted(raw_root.rglob("*.json")):
        if any(part.startswith(".") for part in json_path.relative_to(raw_root).parts):
            continue
        if json_path.name not in {"record.json", "telemetry.json"}:
            raise CorruptShardError(f"unexpected JSON in raw archive: {json_path}")
    return records


def _task_from_child(parent: NodeTask, child_id: str) -> NodeTask:
    _coordinate, _midpoint, left, right = split_task(parent)
    children = {left.node_id: left, right.node_id: right}
    if child_id not in children:
        raise CorruptShardError(f"noncanonical child {child_id} of {parent.node_id}")
    return children[child_id]


def reconstruct_trees(
    output: Path,
    matrix: Sequence[TreeKey],
    plan_records: Mapping[str, Mapping[str, Any]],
    *,
    evaluator_path: str,
    run_config_sha256: str,
    evaluator_source_sha256: str,
    evaluator_binary_sha256: str,
    max_depth: int,
) -> dict[TreeKey, ReconstructedTree]:
    committed_paths = scan_committed_node_records(output)
    consumed: set[tuple[TreeKey, str]] = set()
    states: dict[TreeKey, ReconstructedTree] = {}
    for tree in matrix:
        roots = root_tasks(
            tree,
            plan_records[tree.slab_id],
            evaluator_path=evaluator_path,
            run_config_sha256=run_config_sha256,
            evaluator_source_sha256=evaluator_source_sha256,
            evaluator_binary_sha256=evaluator_binary_sha256,
        )
        stack = list(reversed(roots))
        records: dict[str, dict[str, Any]] = {}
        pending: list[NodeTask] = []
        blocking: list[str] = []
        while stack:
            task = stack.pop()
            identity = tree, task.node_id
            path = committed_paths.get(identity)
            if path is None:
                pending.append(task)
                continue
            consumed.add(identity)
            record = validate_committed_node(output, task, max_depth=max_depth)
            records[task.node_id] = record
            classification = str(record["evaluator_result"]["classification"])
            if classification == "SPLIT":
                split_payload = record["evaluator_result"].get("split")
                _coordinate, _midpoint, left, right = split_task(task)
                expected_children = [left.node_id, right.node_id]
                if not isinstance(split_payload, dict) or split_payload.get("children") != expected_children:
                    raise CorruptShardError(
                        f"split child binding mismatch: {tree.label}/{task.node_id}"
                    )
                stack.extend((right, left))
            elif classification not in {"ENERGY_EXCLUDED", "RETURN_EXCLUDED"}:
                blocking.append(classification)
        states[tree] = ReconstructedTree(tree, records, pending, blocking)
    leftovers = set(committed_paths) - consumed
    if leftovers:
        formatted = sorted(f"{tree.label}/{node}" for tree, node in leftovers)
        raise CorruptShardError(f"orphan/unreachable committed node records: {formatted}")
    return states


def canonical_node_for_tree(record: Mapping[str, Any]) -> dict[str, Any]:
    """Remove no scientific data, but omit non-proof telemetry/order fields."""

    return {
        "task": record["task"],
        "task_binding_sha256": record["task_binding_sha256"],
        "invocation": record["invocation"],
        "evaluator_result": record["evaluator_result"],
        "raw": record["raw"],
    }


def canonical_record_order(record: Mapping[str, Any]) -> tuple[int, str]:
    task = _record_task_payload(record)
    return int(task["depth"]), str(task["node_id"])


def build_tree_payload(
    tree: TreeKey,
    plan_record: Mapping[str, Any],
    records: Iterable[Mapping[str, Any]],
    *,
    run_config_sha256: str,
    max_depth: int,
    max_nodes: int,
) -> dict[str, Any]:
    ordered = sorted(records, key=canonical_record_order)
    if not ordered:
        raise MatrixContractError(f"cannot finalize empty tree {tree.label}")
    classifications = [
        str(record["evaluator_result"]["classification"])
        for record in ordered
    ]
    if any(
        value not in {"SPLIT", "ENERGY_EXCLUDED", "RETURN_EXCLUDED"}
        for value in classifications
    ):
        raise MatrixContractError(f"cannot finalize blocked tree {tree.label}")
    terminal_counts = {
        status: classifications.count(status)
        for status in ("ENERGY_EXCLUDED", "RETURN_EXCLUDED")
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_TREE_ARCHIVED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "tree": tree.payload(),
        "epsilon": [
            str(plan_record["epsilon_lower"]),
            str(plan_record["epsilon_upper"]),
        ],
        "domain": {
            "big_box": {
                coordinate: interval_text(BIG_BOX[coordinate])
                for coordinate in COORDINATES
            },
            "protected_exact_plan_box": {
                coordinate: interval_text(plan_root_box(plan_record)[coordinate])
                for coordinate in COORDINATES
            },
            "shell_semantics": "eight closed shells cover B_loc \\ int(P_j)",
        },
        "prospective_pointwise_target": (
            "for every slab j and epsilon in E_j, "
            "Z(F_epsilon) intersect B_loc = {x_j(epsilon)}"
        ),
        "claim_boundary": (
            "even after independent validation this is confined to the frozen "
            "P_+=0 local chart; it is not energy-shell/global uniqueness"
        ),
        "run_config_sha256": run_config_sha256,
        "per_tree_limits": {"max_depth": max_depth, "max_nodes": max_nodes},
        "evaluated_node_count": len(ordered),
        "terminal_counts": terminal_counts,
        "nodes": [canonical_node_for_tree(record) for record in ordered],
    }


def tree_path(output: Path, tree: TreeKey) -> Path:
    return output / "trees" / str(tree.precision_bits) / f"{tree.slab_id}.json"


def tree_manifest_path(output: Path, tree: TreeKey) -> Path:
    return output / "tree_manifests" / str(tree.precision_bits) / f"{tree.slab_id}.json"


def finalize_tree_transaction(
    output: Path,
    tree: TreeKey,
    plan_record: Mapping[str, Any],
    records: Iterable[Mapping[str, Any]],
    *,
    run_config_sha256: str,
    max_depth: int,
    max_nodes: int,
) -> dict[str, Any]:
    """Write canonical tree first and its manifest commit marker last."""

    record_list = list(records)
    payload = build_tree_payload(
        tree,
        plan_record,
        record_list,
        run_config_sha256=run_config_sha256,
        max_depth=max_depth,
        max_nodes=max_nodes,
    )
    target = tree_path(output, tree)
    write_once_or_verify(target, payload)
    node_files: dict[str, dict[str, str]] = {}
    for record in sorted(record_list, key=canonical_record_order):
        task = _record_task_payload(record)
        node_id = str(task["node_id"])
        directory = output / str(PurePosixPath(record["raw"]["stdout_file"]).parent)
        node_files[node_id] = {
            "record_sha256": sha256(directory / "record.json"),
            "stdout_sha256": sha256(directory / "stdout.txt"),
            "stderr_sha256": sha256(directory / "stderr.txt"),
            "argv_sha256": str(record["invocation"]["argv_sha256"]),
        }
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_TREE_COMMITTED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "tree": tree.payload(),
        "run_config_sha256": run_config_sha256,
        "tree_file": target.relative_to(output).as_posix(),
        "tree_sha256": sha256(target),
        "node_files": node_files,
    }
    # This manifest is the commit marker.  It contains no self-hash, avoiding
    # a circular provenance graph.
    write_once_or_verify(tree_manifest_path(output, tree), manifest)
    return manifest


def _canonical_paths(root: Path) -> set[Path]:
    if not root.exists():
        return set()
    if root.is_symlink() or not root.is_dir():
        raise MatrixContractError(f"matrix root is not a regular directory: {root}")
    paths: set[Path] = set()
    for path in root.rglob("*"):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            raise MatrixContractError(f"non-regular authoritative shard: {path}")
        if path.is_file():
            if path.suffix != ".json":
                raise MatrixContractError(f"unexpected non-JSON authoritative shard: {path}")
            paths.add(path)
    return paths


def validate_tree_commit_matrix(
    output: Path,
    matrix: Sequence[TreeKey],
    *,
    require_complete: bool,
) -> list[dict[str, Any]]:
    """Validate exact tree/manifest paths and one-to-one pair identities."""

    expected_trees = {tree_path(output, tree): tree for tree in matrix}
    expected_manifests = {tree_manifest_path(output, tree): tree for tree in matrix}
    actual_trees = _canonical_paths(output / "trees")
    actual_manifests = _canonical_paths(output / "tree_manifests")
    extra_trees = actual_trees - set(expected_trees)
    extra_manifests = actual_manifests - set(expected_manifests)
    if extra_trees or extra_manifests:
        raise MatrixContractError(
            f"unexpected canonical shards: trees={sorted(map(str, extra_trees))}, "
            f"manifests={sorted(map(str, extra_manifests))}"
        )
    if require_complete:
        missing_trees = set(expected_trees) - actual_trees
        missing_manifests = set(expected_manifests) - actual_manifests
        if missing_trees or missing_manifests:
            raise MatrixContractError(
                f"missing canonical shards: trees={len(missing_trees)}, "
                f"manifests={len(missing_manifests)}"
            )
    # A tree without its commit-marker manifest is an interrupted transaction,
    # allowed only during partial resume.  A manifest without a tree is always
    # corrupt.
    for tree in matrix:
        target = tree_path(output, tree)
        manifest_target = tree_manifest_path(output, tree)
        if manifest_target in actual_manifests and target not in actual_trees:
            raise MatrixContractError(f"manifest without tree: {tree.label}")
    manifests: list[dict[str, Any]] = []
    seen_pairs: set[TreeKey] = set()
    for path in sorted(actual_manifests):
        expected_tree = expected_manifests[path]
        manifest = strict_json_load(path)
        internal = manifest.get("tree", {})
        if not isinstance(internal, Mapping) or not exact_json_equal(
            internal, expected_tree.payload()
        ):
            raise MatrixContractError(f"invalid internal tree identity: {path}")
        internal_tree = expected_tree
        if internal_tree != expected_tree:
            raise MatrixContractError(f"tree manifest path/identity mismatch: {path}")
        if internal_tree in seen_pairs:
            raise MatrixContractError(f"duplicate tree manifest identity: {internal_tree.label}")
        seen_pairs.add(internal_tree)
        target = tree_path(output, expected_tree)
        expected_relative = target.relative_to(output).as_posix()
        if manifest.get("tree_file") != expected_relative:
            raise MatrixContractError(f"noncanonical tree path in manifest: {path}")
        if sha256(target) != manifest.get("tree_sha256"):
            raise MatrixContractError(f"tree hash mismatch: {expected_tree.label}")
        if (
            type(manifest.get("schema_version")) is not int
            or manifest.get("schema_version") != SCHEMA_VERSION
            or manifest.get("protocol_id") != PROTOCOL_ID
            or manifest.get("licensing") != "FROZEN_PRODUCTION"
            or manifest.get("scientific_licensing_enabled") is not True
            or manifest.get("producer_state") != "FROZEN_TREE_COMMITTED"
            or manifest.get("milestone_status") is not None
            or manifest.get("theorem_status") is not None
            or manifest.get("final_status") is not None
        ):
            raise MatrixContractError("producer tree manifest namespace/status mismatch")
        tree_payload = strict_json_load(target)
        if (
            type(tree_payload.get("schema_version")) is not int
            or tree_payload.get("schema_version") != SCHEMA_VERSION
            or tree_payload.get("protocol_id") != PROTOCOL_ID
            or tree_payload.get("licensing") != "FROZEN_PRODUCTION"
            or tree_payload.get("scientific_licensing_enabled") is not True
            or tree_payload.get("producer_state") != "FROZEN_TREE_ARCHIVED"
            or any(
                tree_payload.get(key) is not None
                for key in ("milestone_status", "theorem_status", "final_status")
            )
        ):
            raise MatrixContractError("producer tree namespace/status mismatch")
        tree_internal = tree_payload.get("tree", {})
        if not exact_json_equal(tree_internal, expected_tree.payload()):
            raise MatrixContractError(f"tree file path/identity mismatch: {target}")
        node_files = manifest.get("node_files")
        # Every formal manifest binds the exact committed-node set and all
        # authoritative files.  Synthetic tests construct the same namespace.
        if manifest.get("producer_state") == "FROZEN_TREE_COMMITTED":
            if not isinstance(node_files, dict):
                raise MatrixContractError(f"tree manifest has no node file map: {path}")
            tree_nodes = tree_payload.get("nodes")
            if not isinstance(tree_nodes, list):
                raise MatrixContractError(f"tree payload has no node list: {target}")
            tree_node_ids: list[str] = []
            tree_invocations: dict[str, dict[str, Any]] = {}
            for node in tree_nodes:
                try:
                    node_id = str(node["task"]["node_id"])
                    invocation = node["invocation"]
                except (KeyError, TypeError) as error:
                    raise MatrixContractError(f"malformed canonical tree node: {target}") from error
                if not isinstance(invocation, dict):
                    raise MatrixContractError(f"malformed tree invocation: {target}/{node_id}")
                argv = invocation.get("argv")
                if (
                    not isinstance(argv, list)
                    or len(argv) != 12
                    or not all(isinstance(argument, str) for argument in argv)
                    or invocation.get("argv_sha256")
                    != sha256_bytes(canonical_json_bytes(argv))
                ):
                    raise MatrixContractError(f"invalid tree invocation binding: {target}/{node_id}")
                tree_node_ids.append(node_id)
                tree_invocations[node_id] = invocation
            if len(tree_node_ids) != len(set(tree_node_ids)):
                raise MatrixContractError(f"duplicate node ID in tree payload: {target}")
            if set(tree_node_ids) != set(node_files):
                raise MatrixContractError(f"tree/manifest node set mismatch: {expected_tree.label}")
            for node_id, hashes in node_files.items():
                if not NODE_ID_PATTERN.fullmatch(str(node_id)) or not isinstance(hashes, dict):
                    raise MatrixContractError(f"malformed manifest node entry: {path}")
                directory = (
                    output
                    / "raw"
                    / str(expected_tree.precision_bits)
                    / expected_tree.slab_id
                    / str(node_id)
                )
                for filename, hash_field in (
                    ("record.json", "record_sha256"),
                    ("stdout.txt", "stdout_sha256"),
                    ("stderr.txt", "stderr_sha256"),
                ):
                    candidate = directory / filename
                    if not candidate.is_file() or candidate.is_symlink():
                        raise MatrixContractError(f"missing committed node file: {candidate}")
                    if sha256(candidate) != hashes.get(hash_field):
                        raise MatrixContractError(f"committed node hash mismatch: {candidate}")
                record_payload = strict_json_load(directory / "record.json")
                record_invocation = record_payload.get("invocation")
                if not isinstance(record_invocation, dict):
                    raise MatrixContractError(f"committed node lacks invocation: {directory}")
                manifest_argv_sha256 = hashes.get("argv_sha256")
                if (
                    record_invocation != tree_invocations[str(node_id)]
                    or manifest_argv_sha256
                    != tree_invocations[str(node_id)].get("argv_sha256")
                    or manifest_argv_sha256 != record_invocation.get("argv_sha256")
                ):
                    raise MatrixContractError(
                        f"tree/manifest/record argv hash mismatch: {expected_tree.label}/{node_id}"
                    )
        manifests.append(manifest)
    if require_complete and seen_pairs != set(matrix):
        raise MatrixContractError("manifest internal matrix differs from exact 102 pairs")
    return manifests


def validate_summary_matrix(
    entries: Sequence[Mapping[str, Any]], matrix: Sequence[TreeKey]
) -> None:
    internal: list[TreeKey] = []
    for entry in entries:
        if not isinstance(entry, Mapping):
            raise MatrixContractError("malformed aggregate tree entry")
        bits = entry.get("precision_bits")
        slab_id = entry.get("slab_id")
        if type(bits) is not int or not isinstance(slab_id, str):
            raise MatrixContractError("malformed aggregate tree entry")
        internal.append(TreeKey(bits, slab_id))
    if len(internal) != len(matrix) or len(set(internal)) != len(internal):
        raise MatrixContractError("duplicate or missing aggregate summary entry")
    if tuple(internal) != tuple(matrix):
        raise MatrixContractError("aggregate summary order/matrix is not canonical")


def build_aggregate_payloads(
    output: Path,
    matrix: Sequence[TreeKey],
    manifests: Sequence[Mapping[str, Any]],
    *,
    run_config_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    by_tree: dict[TreeKey, Mapping[str, Any]] = {}
    for manifest in manifests:
        internal = manifest["tree"]
        matches = [
            tree for tree in matrix if exact_json_equal(internal, tree.payload())
        ]
        if len(matches) != 1:
            raise MatrixContractError("malformed aggregate manifest identity")
        key = matches[0]
        if key in by_tree:
            raise MatrixContractError(f"duplicate aggregate manifest: {key.label}")
        by_tree[key] = manifest
    if set(by_tree) != set(matrix):
        raise MatrixContractError("aggregate input does not contain the exact 102 manifests")
    entries = [
        {
            **tree.payload(),
            "tree_manifest_file": tree_manifest_path(output, tree).relative_to(output).as_posix(),
            "tree_manifest_sha256": sha256(tree_manifest_path(output, tree)),
        }
        for tree in matrix
    ]
    validate_summary_matrix(entries, matrix)
    summary = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_ALL_TREES_ARCHIVED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "run_config_sha256": run_config_sha256,
        "tree_count": len(entries),
        "trees": entries,
        "claim_boundary": (
            "frozen producer archive only; independent exact-rational replay "
            "has not assigned any scientific status"
        ),
    }
    summary_path = output / "aggregate_summary.json"
    write_once_or_verify(summary_path, summary)
    aggregate_manifest = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_AGGREGATE_COMMITTED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "run_config_sha256": run_config_sha256,
        "aggregate_summary_file": summary_path.relative_to(output).as_posix(),
        "aggregate_summary_sha256": sha256(summary_path),
        "tree_manifests": entries,
    }
    return summary, aggregate_manifest


def command_output(command: list[str]) -> str:
    return subprocess.run(command, check=True, text=True, capture_output=True).stdout.strip()


def formal_status_whitelist() -> dict[str, list[list[Any]]]:
    return {
        "excluded": sorted([list(item) for item in EXCLUDED_RESULTS]),
        "splittable": sorted([list(item) for item in SPLITTABLE_RESULTS]),
        "scientific_stop": sorted([list(item) for item in SCIENTIFIC_STOP_RESULTS]),
        "invalid": sorted([list(item) for item in INVALID_RESULTS]),
    }


def validate_s0_compatibility_replay(project_root: Path) -> None:
    """Replay the exact public-S0 evidence gate before held-out dispatch."""

    checker_relative = "scripts/check_r401_val_l2_all_slabs_independent.py"
    expected = {
        "adapter_source_sha256": sha256(
            resolve_project_input(project_root, S0_ADAPTER_RELATIVE)
        ),
        "checker_source_sha256": sha256(
            resolve_project_input(project_root, checker_relative)
        ),
        "claim_boundary": (
            "public S0 compatibility replay only; no held-out A1 slab was read or evaluated"
        ),
        "manifest_hash_checks": 6055,
        "node_count": 3016,
        "protocol_id": "R401-VAL-L2-A1-PREFREEZE-S0-REPLAY",
        "s0_manifest_sha256": sha256(
            resolve_project_input(project_root, f"{S0_RESULT_RELATIVE}/manifest.json")
        ),
        "s0_postcheck_sha256": sha256(
            resolve_project_input(
                project_root, f"{S0_RESULT_RELATIVE}/POSTCHECK_STATUS.json"
            )
        ),
        "s0_release_provenance_sha256": sha256(
            resolve_project_input(
                project_root, f"{S0_RESULT_RELATIVE}/RELEASE_PROVENANCE.json"
            )
        ),
        "source_release": "R401-VAL-L2-S0",
        "status": "PASS_S0_READ_ONLY_COMPATIBILITY_REPLAY",
        "status_counts": {
            "ENERGY_EXCLUDED": 183,
            "RETURN_EXCLUDED": 1349,
            "UNKNOWN": 1484,
        },
        "tree_count": 6,
        "tree_counts": [
            {"node_count": 486, "precision_bits": 128, "slab_id": "S000", "status_counts": {"ENERGY_EXCLUDED": 18, "RETURN_EXCLUDED": 229, "UNKNOWN": 239}},
            {"node_count": 546, "precision_bits": 128, "slab_id": "S025", "status_counts": {"ENERGY_EXCLUDED": 31, "RETURN_EXCLUDED": 246, "UNKNOWN": 269}},
            {"node_count": 574, "precision_bits": 128, "slab_id": "S050", "status_counts": {"ENERGY_EXCLUDED": 44, "RETURN_EXCLUDED": 247, "UNKNOWN": 283}},
            {"node_count": 436, "precision_bits": 256, "slab_id": "S000", "status_counts": {"ENERGY_EXCLUDED": 18, "RETURN_EXCLUDED": 204, "UNKNOWN": 214}},
            {"node_count": 488, "precision_bits": 256, "slab_id": "S025", "status_counts": {"ENERGY_EXCLUDED": 31, "RETURN_EXCLUDED": 217, "UNKNOWN": 240}},
            {"node_count": 486, "precision_bits": 256, "slab_id": "S050", "status_counts": {"ENERGY_EXCLUDED": 41, "RETURN_EXCLUDED": 206, "UNKNOWN": 239}},
        ],
    }
    replay = strict_json_load(resolve_project_input(project_root, S0_REPLAY_RELATIVE))
    if not exact_json_equal(replay, expected):
        raise SchedulerContractError("public S0 compatibility replay evidence mismatch")


def validate_formal_freeze(
    freeze_path: Path = FORMAL_FREEZE,
    *,
    project_root: Path = ROOT,
) -> FormalFreezeContext:
    """Validate the complete formal gate before initialization or execution.

    The freeze is not trusted because it has a plausible namespace.  Every
    mandatory source byte, the evaluator binary, the exact matrix, scheduler
    resources, proof thresholds, and evaluator ABI are checked before a run
    binding can be constructed.
    """

    freeze_path = checked_lexical_path(
        freeze_path,
        label="formal L2-A1 freeze",
        require_file=True,
    )
    project_root = checked_lexical_path(
        project_root,
        label="project root",
        require_directory=True,
    )
    freeze = strict_json_load(freeze_path)
    if not isinstance(freeze, Mapping):
        raise SchedulerContractError("malformed formal freeze")
    if not (
        type(freeze.get("schema_version")) is int
        and freeze.get("schema_version") == SCHEMA_VERSION
        and freeze.get("protocol_id") == PROTOCOL_ID
        and freeze.get("status") == EXPECTED_FREEZE_STATUS
        and freeze.get("scientific_licensing_enabled") is True
        and freeze.get("checker_mode") == EXPECTED_CHECKER_MODE
    ):
        raise SchedulerContractError("formal freeze status or namespace mismatch")

    expected_matrix = [
        TreeKey(bits, slab_id).payload()
        for bits in PRECISIONS
        for slab_id in SLAB_IDS
    ]
    if not exact_json_equal(freeze.get("matrix"), expected_matrix):
        raise MatrixContractError("formal freeze does not contain the exact ordered 102 matrix")

    input_hashes = freeze.get("input_hashes")
    if not isinstance(input_hashes, Mapping) or not set(MANDATORY_FROZEN_INPUTS).issubset(
        input_hashes
    ):
        raise SchedulerContractError("formal freeze misses mandatory input hashes")
    validated_hashes: dict[str, str] = {}
    for relative, expected in input_hashes.items():
        if not isinstance(relative, str) or not isinstance(expected, str):
            raise SchedulerContractError("formal input hash DAG is not string-to-string")
        if not HEX_SHA256.fullmatch(expected):
            raise SchedulerContractError(f"invalid frozen input hash: {relative}")
        candidate = resolve_project_input(project_root, relative)
        if sha256(candidate) != expected:
            raise SchedulerContractError(f"frozen input hash mismatch: {relative}")
        validated_hashes[relative] = expected

    checker_relative = "scripts/check_r401_val_l2_all_slabs_independent.py"
    runner_relative = "scripts/run_r401_val_l2_all_slabs.py"
    checker_hash = validated_hashes[checker_relative]
    if freeze.get("checker_source_sha256") != checker_hash:
        raise SchedulerContractError("formal checker hash DAG mismatch")
    # State this edge explicitly: the producer may not authorize a freeze that
    # binds a different producer source under a misleading path.
    if validated_hashes[runner_relative] != sha256(
        resolve_project_input(project_root, runner_relative)
    ):
        raise SchedulerContractError("formal producer hash DAG mismatch")
    validate_s0_compatibility_replay(project_root)

    review_path = resolve_project_input(project_root, PREFREEZE_REVIEW_RELATIVE)
    try:
        review_lines = review_path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as error:
        raise SchedulerContractError("pre-freeze review is not UTF-8 text") from error
    review_declarations = [
        line
        for line in review_lines
        if markdown_has_verdict_declaration(line)
    ]
    if review_declarations != [PREFREEZE_ACCEPT_MARKER]:
        raise SchedulerContractError(
            "pre-freeze review must contain exactly one exact ACCEPT_FOR_FREEZE verdict"
        )

    machine_relative = (
        "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json"
    )
    machine_freeze = strict_json_load(
        resolve_project_input(project_root, machine_relative)
    )
    if not isinstance(machine_freeze, Mapping) or not (
        type(machine_freeze.get("schema_version")) is int
        and machine_freeze.get("schema_version") == SCHEMA_VERSION
        and machine_freeze.get("protocol_id") == PROTOCOL_ID
        and machine_freeze.get("status") == EXPECTED_FREEZE_STATUS
        and machine_freeze.get("scientific_licensing_enabled") is True
        and exact_json_equal(
            machine_freeze.get("machine_requirements"),
            EXPECTED_MACHINE_REQUIREMENTS,
        )
    ):
        raise SchedulerContractError("machine freeze status or requirements mismatch")
    if not exact_json_equal(
        freeze.get("machine_requirements"), EXPECTED_MACHINE_REQUIREMENTS
    ):
        raise SchedulerContractError("formal freeze machine requirements mismatch")

    limits = freeze.get("per_tree_limits")
    if not isinstance(limits, Mapping) or set(limits) != {"max_depth", "max_nodes"}:
        raise SchedulerContractError("invalid frozen per-tree limit object")
    max_depth, max_nodes = limits.get("max_depth"), limits.get("max_nodes")
    if (
        not isinstance(max_depth, int)
        or isinstance(max_depth, bool)
        or max_depth < 0
        or not isinstance(max_nodes, int)
        or isinstance(max_nodes, bool)
        or max_nodes <= 0
    ):
        raise SchedulerContractError("invalid frozen per-tree limits")

    scheduler = freeze.get("scheduler")
    if not isinstance(scheduler, Mapping):
        raise SchedulerContractError("formal freeze has no scheduler contract")
    workers = scheduler.get("workers")
    timeout = scheduler.get("node_timeout_seconds")
    if not (
        set(scheduler)
        == {
            "policy",
            "workers",
            "node_timeout_seconds",
            "global_scientific_budget",
            "max_inflight_per_tree",
        }
        and scheduler.get("policy") == EXPECTED_SCHEDULER_POLICY
        and isinstance(workers, int)
        and not isinstance(workers, bool)
        and 0 < workers <= EXPECTED_MACHINE_REQUIREMENTS["cpu_logical"]
        and (
            timeout is None
            or (
                isinstance(timeout, int)
                and not isinstance(timeout, bool)
                and timeout > 0
            )
        )
        and scheduler.get("global_scientific_budget") is None
        and type(scheduler.get("max_inflight_per_tree")) is int
        and scheduler.get("max_inflight_per_tree") == 1
    ):
        raise SchedulerContractError("invalid frozen scheduler contract")

    thresholds = freeze.get("logical_thresholds")
    if not exact_json_equal(thresholds, EXPECTED_LOGICAL_THRESHOLDS):
        raise SchedulerContractError("invalid frozen logical thresholds")

    evaluator = freeze.get("evaluator")
    if not isinstance(evaluator, Mapping):
        raise SchedulerContractError("formal freeze has no evaluator contract")
    source_file = evaluator.get("source_file")
    source_hash = evaluator.get("source_sha256")
    binary_file = evaluator.get("binary_file")
    binary_hash = evaluator.get("binary_sha256")
    capd_flags = evaluator.get("capd_flags")
    if source_file != SOURCE.relative_to(ROOT).as_posix():
        raise SchedulerContractError("frozen evaluator source path mismatch")
    if (
        not isinstance(source_hash, str)
        or not HEX_SHA256.fullmatch(source_hash)
        or validated_hashes.get(str(source_file)) != source_hash
    ):
        raise SchedulerContractError("frozen evaluator source hash DAG mismatch")
    if sha256(resolve_project_input(project_root, str(source_file))) != source_hash:
        raise SchedulerContractError("frozen evaluator source bytes mismatch")
    if not isinstance(binary_file, str) or not Path(binary_file).is_absolute():
        raise SchedulerContractError("frozen evaluator binary path is not absolute")
    binary = checked_lexical_path(
        Path(binary_file),
        label="frozen evaluator binary",
        require_file=True,
    )
    if str(binary) != binary_file:
        raise SchedulerContractError("frozen evaluator binary path is not canonical")
    if (
        not isinstance(binary_hash, str)
        or not HEX_SHA256.fullmatch(binary_hash)
        or sha256(binary) != binary_hash
    ):
        raise SchedulerContractError("frozen evaluator binary hash mismatch")
    if evaluator.get("capd_commit") != EXPECTED_CAPD_COMMIT:
        raise SchedulerContractError("frozen CAPD commit mismatch")
    if (
        not isinstance(capd_flags, list)
        or not all(isinstance(flag, str) for flag in capd_flags)
        or not REQUIRED_CAPD_FLAGS.issubset(capd_flags)
    ):
        raise SchedulerContractError("invalid frozen CAPD flags")
    if not exact_json_equal(
        evaluator.get("status_returncode_whitelist"), formal_status_whitelist()
    ):
        raise SchedulerContractError("frozen evaluator status whitelist mismatch")

    return FormalFreezeContext(
        freeze=dict(freeze),
        freeze_path=freeze_path,
        freeze_sha256=sha256(freeze_path),
        input_hashes=validated_hashes,
        per_tree_limits={"max_depth": max_depth, "max_nodes": max_nodes},
        scheduler=dict(scheduler),
        evaluator=dict(evaluator),
        logical_thresholds=dict(thresholds),
    )


def detected_logical_cpus() -> int:
    if hasattr(os, "sched_getaffinity"):
        return len(os.sched_getaffinity(0))
    return os.cpu_count() or 0


def detected_memory_limit_bytes() -> int:
    """Return the enforced cgroup limit, falling back to physical memory."""

    candidates = (
        Path("/sys/fs/cgroup/memory.max"),
        Path("/sys/fs/cgroup/memory/memory.limit_in_bytes"),
    )
    for candidate in candidates:
        try:
            raw = candidate.read_text(encoding="utf-8").strip()
        except OSError:
            continue
        if raw and raw != "max":
            try:
                value = int(raw)
            except ValueError:
                continue
            if 0 < value < 2**60:
                return value
    for line in Path("/proc/meminfo").read_text(encoding="utf-8").splitlines():
        if line.startswith("MemTotal:"):
            return int(line.split()[1]) * 1024
    raise SchedulerContractError("cannot determine runtime memory limit")


def free_bytes(path: Path) -> int:
    return os.statvfs(path).f_bavail * os.statvfs(path).f_frsize


def validate_runtime_machine(
    formal: FormalFreezeContext,
    *,
    storage_path: Path,
    require_launch_storage: bool,
) -> int:
    requirements = formal.freeze.get("machine_requirements")
    if not exact_json_equal(requirements, EXPECTED_MACHINE_REQUIREMENTS):
        raise SchedulerContractError("runtime machine contract is not frozen")
    if detected_logical_cpus() != requirements["cpu_logical"]:
        raise SchedulerContractError("runtime logical CPU count differs from freeze")
    if detected_memory_limit_bytes() != requirements["memory_limit_bytes"]:
        raise SchedulerContractError("runtime memory limit differs from freeze")
    probe = storage_path if storage_path.exists() else storage_path.parent
    available = free_bytes(probe)
    if require_launch_storage and available < requirements["min_launch_free_bytes"]:
        raise SchedulerContractError(
            "runtime free storage is below the frozen 100 GiB launch gate"
        )
    return available


def build_run_binding(
    *,
    plan_records: Mapping[str, Mapping[str, Any]],
    formal: FormalFreezeContext,
) -> dict[str, Any]:
    matrix = exact_production_matrix(plan_records)
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "l2_a1_freeze_sha256": formal.freeze_sha256,
        "machine_freeze_sha256": formal.input_hashes[
            "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json"
        ],
        "machine_requirements": dict(formal.freeze["machine_requirements"]),
        "matrix": [tree.payload() for tree in matrix],
        "per_tree_limits": dict(formal.per_tree_limits),
        "scheduler": dict(formal.scheduler),
        "evaluator": dict(formal.evaluator),
        "logical_thresholds": dict(formal.logical_thresholds),
        "input_hashes": dict(formal.input_hashes),
    }


def ensure_run_config(
    output: Path,
    binding: Mapping[str, Any],
    *,
    resume: bool,
) -> tuple[dict[str, Any], str]:
    path = output / "run_config.json"
    binding_sha = sha256_bytes(canonical_json_bytes(binding))
    if path.exists() or path.is_symlink():
        if not resume:
            raise ResumeBindingError(
                f"output generation already exists; use --resume only with exact binding: {output}"
            )
        config = strict_json_load(path)
        if (
            not exact_json_equal(config.get("binding"), binding)
            or config.get("binding_sha256") != binding_sha
        ):
            raise ResumeBindingError(
                "run-config binding mismatch; preserve this generation and use a new output directory"
            )
        if (
            type(config.get("schema_version")) is not int
            or config.get("schema_version") != SCHEMA_VERSION
            or config.get("protocol_id") != PROTOCOL_ID
            or config.get("licensing") != "FROZEN_PRODUCTION"
            or config.get("scientific_licensing_enabled") is not True
            or config.get("producer_state") != "FROZEN_GENERATION_INITIALIZED"
            or config.get("milestone_status") is not None
            or config.get("theorem_status") is not None
            or config.get("final_status") is not None
        ):
            raise ResumeBindingError("producer run config namespace/status mismatch")
        return config, sha256(path)
    if resume:
        raise ResumeBindingError(f"cannot resume missing run config: {path}")
    if output.exists() and any(output.iterdir()):
        raise ResumeBindingError(
            f"refusing to initialize a nonempty unbound output directory: {output}"
        )
    output.mkdir(parents=True, exist_ok=True)
    config = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_GENERATION_INITIALIZED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "binding": binding,
        "binding_sha256": binding_sha,
    }
    atomic_write_json(path, config)
    return config, sha256(path)


def quarantine_incompatible_generation(
    output: Path,
    expected_binding: Mapping[str, Any],
) -> Path:
    """Atomically preserve a whole incompatible generation for recovery.

    This operation is deliberately narrow: it is permitted only when an
    existing, parseable run config binds different immutable inputs.  It never
    deletes or merges files.  The caller may initialize a fresh generation at
    the original path only after this rename succeeds.
    """

    if output.is_symlink() or not output.is_dir():
        raise ResumeBindingError("quarantine target is not a regular generation directory")
    run_config_path = output / "run_config.json"
    if run_config_path.is_symlink() or not run_config_path.is_file():
        raise ResumeBindingError("quarantine requires an existing regular run config")
    old_config = strict_json_load(run_config_path)
    if not isinstance(old_config, Mapping) or not isinstance(
        old_config.get("binding"), Mapping
    ):
        raise ResumeBindingError("quarantine requires a parseable run-config binding")
    old_binding = old_config["binding"]
    # JSON bindings are type-strict.  In particular, ``1``, ``1.0``, and
    # ``true`` are three different frozen values even though Python's normal
    # equality relation aliases them.  Use the same canonical-byte comparison
    # as the resume gate so quarantine can always recover a generation that
    # resume correctly rejects.
    if exact_json_equal(old_binding, expected_binding):
        raise ResumeBindingError("refusing to quarantine a binding-compatible generation")

    index = 1
    while True:
        quarantine = output.parent / f"{output.name}.quarantine-{index:04d}"
        if not quarantine.exists() and not quarantine.is_symlink():
            break
        index += 1
    os.rename(output, quarantine)
    fsync_directory(output.parent)
    record = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "OPERATIONAL_RECOVERY_ONLY",
        "scientific_licensing_enabled": False,
        "producer_state": "QUARANTINED_INCOMPATIBLE_GENERATION",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "original_generation_path": str(output),
        "quarantine_path": str(quarantine),
        "reason": "RUN_CONFIG_BINDING_MISMATCH",
        "old_run_config_sha256": sha256(quarantine / "run_config.json"),
        "old_binding_sha256_recomputed": sha256_bytes(
            canonical_json_bytes(old_binding)
        ),
        "old_binding_sha256_stored": old_config.get("binding_sha256"),
        "expected_binding_sha256": sha256_bytes(
            canonical_json_bytes(expected_binding)
        ),
    }
    write_once_or_verify(quarantine / "QUARANTINE_RECORD.json", record)
    return quarantine


def invoke_evaluator(
    evaluator: Path,
    task: NodeTask,
    *,
    timeout_seconds: int | None,
) -> EvaluatorOutcome:
    resolved_evaluator = str(evaluator.resolve())
    if resolved_evaluator != task.evaluator_path:
        raise ResumeBindingError(
            f"runtime evaluator path differs from node binding: {resolved_evaluator}"
        )
    started = time.monotonic()
    try:
        process = subprocess.run(
            task.arguments(),
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
        )
        return EvaluatorOutcome(
            process.stdout,
            process.stderr,
            process.returncode,
            False,
            time.monotonic() - started,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else (error.stdout or "")
        stderr = error.stderr.decode() if isinstance(error.stderr, bytes) else (error.stderr or "")
        return EvaluatorOutcome(
            stdout,
            stderr,
            None,
            True,
            time.monotonic() - started,
        )


def task_order_key(
    task: NodeTask, matrix_index: Mapping[TreeKey, int]
) -> tuple[int, int, str]:
    return matrix_index[task.tree], task.depth, task.node_id


def write_operational_live_status(
    output: Path,
    payload: Mapping[str, Any],
) -> Path:
    """Write mutable telemetry outside the authoritative generation root."""

    status_path = output.parent / ".operational" / output.name / "live_status.json"
    atomic_write_json(status_path, dict(payload))
    return status_path


def run_scheduler_session(
    *,
    output: Path,
    evaluator: Path,
    matrix: Sequence[TreeKey],
    plan_records: Mapping[str, Mapping[str, Any]],
    run_config_sha256: str,
    evaluator_source_sha256: str,
    evaluator_binary_sha256: str,
    workers: int,
    max_depth: int,
    max_nodes: int,
    node_timeout_seconds: int | None,
    dispatch_limit: int | None,
    operational_pause_below_free_bytes: int | None = None,
    evaluator_function: Callable[..., EvaluatorOutcome] = invoke_evaluator,
) -> dict[str, Any]:
    """Run formal deterministic barrier batches without assigning a theorem."""

    evaluator_path = str(evaluator.resolve())
    # A committed tree is immutable.  Validate every existing tree commit
    # before reconstructing pending work, so a missing/corrupt finalized node
    # can never be silently regenerated inside the same generation.
    validate_tree_commit_matrix(output, matrix, require_complete=False)
    states = reconstruct_trees(
        output,
        matrix,
        plan_records,
        evaluator_path=evaluator_path,
        run_config_sha256=run_config_sha256,
        evaluator_source_sha256=evaluator_source_sha256,
        evaluator_binary_sha256=evaluator_binary_sha256,
        max_depth=max_depth,
    )
    queue = FairNodeQueue(matrix)
    used = {tree: len(states[tree].records) for tree in matrix}
    blocked_trees = {
        tree for tree in matrix if states[tree].blocking_classifications
    }
    for tree in matrix:
        if tree not in blocked_trees:
            queue.extend(tree, states[tree].pending)
    matrix_index = {tree: index for index, tree in enumerate(matrix)}
    dispatched = 0
    operational_pause = False
    pause_free_bytes: int | None = None
    while queue:
        if dispatch_limit is not None and dispatched >= dispatch_limit:
            break
        if operational_pause_below_free_bytes is not None:
            pause_free_bytes = free_bytes(output)
            if pause_free_bytes < operational_pause_below_free_bytes:
                operational_pause = True
                write_operational_live_status(
                    output,
                    {
                        "schema_version": SCHEMA_VERSION,
                        "protocol_id": PROTOCOL_ID,
                        "producer_state": "OPERATIONAL_STORAGE_PAUSE",
                        "milestone_status": None,
                        "theorem_status": None,
                        "final_status": None,
                        "generation_path": str(output),
                        "free_bytes": pause_free_bytes,
                        "resume_when_free_bytes_at_least": (
                            operational_pause_below_free_bytes
                        ),
                        "note": "operational pause only; no scientific failure assigned",
                    },
                )
                break
        capacity = workers
        if dispatch_limit is not None:
            capacity = min(capacity, dispatch_limit - dispatched)

        reservations = {tree: 0 for tree in matrix}

        def admissible(tree: TreeKey) -> bool:
            return (
                tree not in blocked_trees
                and used[tree] + reservations[tree] < max_nodes
            )

        def reserve(tree: TreeKey) -> None:
            reservations[tree] += 1

        batch = queue.pop_batch(capacity, admissible, reserve)
        if not batch:
            break
        outcomes: dict[str, EvaluatorOutcome] = {}
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures: dict[Future[EvaluatorOutcome], NodeTask] = {
                executor.submit(
                    evaluator_function,
                    evaluator,
                    task,
                    timeout_seconds=node_timeout_seconds,
                ): task
                for task in batch
            }
            for future in as_completed(futures):
                task = futures[future]
                outcomes[task.binding_sha256] = future.result()

        # Commit and enqueue in canonical order, so proof shards and the next
        # ready frontier are independent of worker completion order.
        for task in sorted(batch, key=lambda item: task_order_key(item, matrix_index)):
            outcome = outcomes[task.binding_sha256]
            record = commit_node_transaction(
                output,
                task,
                outcome,
                max_depth=max_depth,
            )
            used[task.tree] += 1
            dispatched += 1
            classification = str(record["evaluator_result"]["classification"])
            if classification == "SPLIT":
                _coordinate, _midpoint, left, right = split_task(task)
                # Parent commit succeeded before either child becomes ready.
                queue.extend(task.tree, (left, right))
            elif classification not in {"ENERGY_EXCLUDED", "RETURN_EXCLUDED"}:
                blocked_trees.add(task.tree)
                queue.discard_tree(task.tree)

    final_states = reconstruct_trees(
        output,
        matrix,
        plan_records,
        evaluator_path=evaluator_path,
        run_config_sha256=run_config_sha256,
        evaluator_source_sha256=evaluator_source_sha256,
        evaluator_binary_sha256=evaluator_binary_sha256,
        max_depth=max_depth,
    )
    for tree in matrix:
        state = final_states[tree]
        if state.complete:
            finalize_tree_transaction(
                output,
                tree,
                plan_records[tree.slab_id],
                state.records.values(),
                run_config_sha256=run_config_sha256,
                max_depth=max_depth,
                max_nodes=max_nodes,
            )
    partial_manifests = validate_tree_commit_matrix(
        output, matrix, require_complete=False
    )
    scheduler_state = {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_SESSION_ARCHIVED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "run_config_sha256": run_config_sha256,
        "session_dispatch_count": dispatched,
        "max_inflight_per_tree": 1,
        "operational_pause": operational_pause,
        "operational_pause_free_bytes": pause_free_bytes if operational_pause else None,
        "committed_tree_count": len(partial_manifests),
        "tree_states": [
            {
                **tree.payload(),
                "evaluated_nodes": len(final_states[tree].records),
                "pending_frontier_nodes": len(final_states[tree].pending),
                "blocking_classifications": final_states[tree].blocking_classifications,
                "per_tree_node_budget_exhausted": (
                    len(final_states[tree].records) >= max_nodes
                    and bool(final_states[tree].pending)
                ),
            }
            for tree in matrix
        ],
    }
    atomic_write_json(output / "scheduler_state.json", scheduler_state)
    if len(partial_manifests) == len(matrix):
        manifests = validate_tree_commit_matrix(output, matrix, require_complete=True)
        _summary, aggregate_manifest = build_aggregate_payloads(
            output,
            matrix,
            manifests,
            run_config_sha256=run_config_sha256,
        )
        write_once_or_verify(output / "aggregate_manifest.json", aggregate_manifest)
    return scheduler_state


def validate_cli_contract(
    formal: FormalFreezeContext,
    *,
    evaluator: Path,
    capd_commit: str,
    capd_flags: Sequence[str],
    workers: int,
    max_depth: int,
    max_nodes: int,
    node_timeout_seconds: int | None,
) -> None:
    frozen_evaluator = formal.evaluator
    frozen_scheduler = formal.scheduler
    frozen_limits = formal.per_tree_limits
    if str(evaluator) != frozen_evaluator.get("binary_file"):
        raise SchedulerContractError("CLI evaluator path differs from freeze")
    if sha256(evaluator) != frozen_evaluator.get("binary_sha256"):
        raise SchedulerContractError("CLI evaluator bytes differ from freeze")
    if capd_commit != frozen_evaluator.get("capd_commit"):
        raise SchedulerContractError("runtime CAPD commit differs from freeze")
    if list(capd_flags) != frozen_evaluator.get("capd_flags"):
        raise SchedulerContractError("runtime CAPD flags differ from frozen ordered flags")
    if workers != frozen_scheduler.get("workers"):
        raise SchedulerContractError("CLI worker count differs from freeze")
    if node_timeout_seconds != frozen_scheduler.get("node_timeout_seconds"):
        raise SchedulerContractError("CLI node timeout differs from freeze")
    if frozen_scheduler.get("max_inflight_per_tree") != 1:
        raise SchedulerContractError("freeze does not enforce one in-flight node per tree")
    if max_depth != frozen_limits.get("max_depth"):
        raise SchedulerContractError("CLI max depth differs from freeze")
    if max_nodes != frozen_limits.get("max_nodes"):
        raise SchedulerContractError("CLI max nodes differs from freeze")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fail-closed formal R401-VAL-L2-A1 producer; all scientific "
            "statuses remain null pending independent replay"
        )
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results/r401_val_l2_all_slabs",
    )
    parser.add_argument("--evaluator", type=Path, required=True)
    parser.add_argument("--capd-source", type=Path, required=True)
    parser.add_argument("--capd-config", type=Path, required=True)
    parser.add_argument("--freeze", type=Path, default=FORMAL_FREEZE)
    parser.add_argument("--workers", type=int, required=True)
    parser.add_argument("--max-depth", type=int, required=True)
    parser.add_argument("--max-nodes", type=int, required=True)
    parser.add_argument("--node-timeout-seconds", type=int)
    parser.add_argument("--dispatch-limit", type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--quarantine-incompatible", action="store_true")
    parser.add_argument("--initialize-only", action="store_true")
    parser.add_argument("--execute", action="store_true")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    if args.initialize_only == args.execute:
        raise SchedulerContractError(
            "choose exactly one of --initialize-only or --execute"
        )
    if args.resume and args.quarantine_incompatible:
        raise SchedulerContractError(
            "--resume and --quarantine-incompatible are mutually exclusive"
        )
    evaluator = checked_lexical_path(
        args.evaluator,
        label="evaluator",
        require_file=True,
    )
    freeze = checked_lexical_path(
        args.freeze,
        label="formal freeze",
        require_file=True,
    )
    if freeze != Path(os.path.abspath(os.fspath(FORMAL_FREEZE))):
        raise SchedulerContractError(
            "formal production accepts only the canonical L2-A1 freeze path"
        )
    formal = validate_formal_freeze(freeze)
    plan_records = load_plan_records()
    matrix = exact_production_matrix(plan_records)
    capd_source = checked_lexical_path(
        args.capd_source,
        label="CAPD source tree",
        require_directory=True,
    )
    capd_config = checked_lexical_path(
        args.capd_config,
        label="CAPD config helper",
        require_file=True,
    )
    capd_commit = command_output(
        ["git", "-C", str(capd_source), "rev-parse", "HEAD"]
    )
    capd_flags = shlex.split(
        command_output([str(capd_config), "--cflags", "--libs"])
    )
    validate_cli_contract(
        formal,
        evaluator=evaluator,
        capd_commit=capd_commit,
        capd_flags=capd_flags,
        workers=args.workers,
        max_depth=args.max_depth,
        max_nodes=args.max_nodes,
        node_timeout_seconds=args.node_timeout_seconds,
    )
    binding = build_run_binding(
        plan_records=plan_records,
        formal=formal,
    )
    output = checked_lexical_path(
        args.output,
        label="output generation",
        allow_missing_leaf=True,
    )
    validate_runtime_machine(
        formal,
        storage_path=output,
        require_launch_storage=args.execute,
    )
    if args.quarantine_incompatible:
        quarantine_incompatible_generation(output, binding)
    _config, run_config_sha = ensure_run_config(
        output,
        binding,
        resume=args.resume,
    )
    if args.initialize_only:
        state = {
            "schema_version": SCHEMA_VERSION,
            "protocol_id": PROTOCOL_ID,
            "licensing": "FROZEN_PRODUCTION",
            "scientific_licensing_enabled": True,
            "producer_state": "FROZEN_MATRIX_INITIALIZED_ONLY",
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
            "run_config_sha256": run_config_sha,
            "tree_count": len(matrix),
            "note": "no evaluator node was dispatched",
        }
        atomic_write_json(output / "scheduler_state.json", state)
        print(json.dumps(state, indent=2, sort_keys=True))
        return 0
    state = run_scheduler_session(
        output=output,
        evaluator=evaluator,
        matrix=matrix,
        plan_records=plan_records,
        run_config_sha256=run_config_sha,
        evaluator_source_sha256=sha256(SOURCE),
        evaluator_binary_sha256=sha256(evaluator),
        workers=args.workers,
        max_depth=args.max_depth,
        max_nodes=args.max_nodes,
        node_timeout_seconds=args.node_timeout_seconds,
        dispatch_limit=args.dispatch_limit,
        operational_pause_below_free_bytes=formal.freeze["machine_requirements"][
            "operational_pause_below_free_bytes"
        ],
    )
    print(json.dumps(state, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
