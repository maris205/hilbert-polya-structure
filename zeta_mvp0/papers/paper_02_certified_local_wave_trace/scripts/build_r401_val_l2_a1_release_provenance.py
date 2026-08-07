#!/usr/bin/env python3
"""Build or verify the final R401-VAL-L2-A1 release provenance object.

This script is deliberately independent of both the producer and the formal
checker.  It runs only after the authoritative checker and postcheck have
accepted one complete 102-tree generation.  The resulting
``RELEASE_PROVENANCE.json`` is a deterministic, write-once hash envelope; it
does not contain its own hash and it cannot promote any claim beyond the
frozen reduced-chart local-complement milestone.

No evaluator is invoked here.  ``--verify-only`` is entirely read-only.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from contextvars import ContextVar
import hashlib
import json
import math
import os
import re
import secrets
import stat
from pathlib import Path, PurePosixPath
from typing import Any, Iterator, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PROTOCOL_ID = "R401-VAL-L2-A1"
SCHEMA_VERSION = 1
PASS_STATUS = "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
CHECKER_STATUS = "PASS_INDEPENDENT_CHECKER"
CHECKER_MODE = "INDEPENDENT_EXACT_RATIONAL_REPLAY"
RELEASE_CONTRACT = "write_once_exact_hash_dag_v1"
MARKDOWN_CLAIM_BOUNDARY = (
    "Claim boundary: local P_+=0 reduced-chart result only; no "
    "energy-shell/global, trace-formula, Hilbert-Polya, zeta-zero, or RH promotion"
)
CHECKER_CLAIM_BOUNDARY = (
    "pointwise reduced-root uniqueness in the frozen local P_+=0 chart only; "
    "no energy-shell/global, phase-cover, trace-domain, arithmetic-prime, "
    "Hilbert--Polya, zeta-zero, or RH promotion"
)
RESULT_RELATIVE = PurePosixPath("results/r401_val_l2_all_slabs")
RELEASE_NAME = "RELEASE_PROVENANCE.json"
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
EXPECTED_MACHINE_REQUIREMENTS = {
    "cpu_logical": 32,
    "memory_limit_bytes": 64_424_509_440,
    "min_launch_free_bytes": 107_374_182_400,
    "operational_pause_below_free_bytes": 161_061_273_600,
}
EXPECTED_PER_TREE_LIMITS = {"max_depth": 48, "max_nodes": 20_000}
EXPECTED_SCHEDULER = {
    "policy": "deterministic_round_robin_barrier_batches_v1",
    "workers": 24,
    "node_timeout_seconds": 7200,
    "global_scientific_budget": None,
    "max_inflight_per_tree": 1,
}
EXPECTED_LOGICAL_THRESHOLDS = {
    "logical_margin_128": "1e-30",
    "logical_margin_256": "1e-60",
    "newton_guard_128": "1e-40",
    "newton_guard_256": "1e-75",
}
EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
REQUIRED_CAPD_FLAGS = frozenset(
    {"-D__HAVE_MPFR__", "-lmpfr", "-lgmp", "-frounding-math"}
)
EXPECTED_STATUS_RETURNCODE_WHITELIST = {
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
EXPECTED_EVALUATOR_KEYS = {
    "source_file",
    "source_sha256",
    "binary_file",
    "binary_sha256",
    "capd_commit",
    "capd_flags",
    "status_returncode_whitelist",
}
EXPECTED_RUN_BINDING_KEYS = {
    "schema_version",
    "protocol_id",
    "licensing",
    "scientific_licensing_enabled",
    "l2_a1_freeze_sha256",
    "machine_freeze_sha256",
    "machine_requirements",
    "matrix",
    "per_tree_limits",
    "scheduler",
    "evaluator",
    "logical_thresholds",
    "input_hashes",
}

FORMAL_PROTOCOL = "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md"
MACHINE_FREEZE = "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json"
MAIN_FREEZE = "research/route_a_wave_trace/R401_VAL_L2_A1_FREEZE.json"
PREFREEZE_REVIEW = "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md"
S0_REPLAY = "research/route_a_wave_trace/R401_VAL_L2_A1_S0_COMPATIBILITY_REPLAY.json"
PRODUCER = "scripts/run_r401_val_l2_all_slabs.py"
CHECKER = "scripts/check_r401_val_l2_all_slabs_independent.py"
S0_ADAPTER = "scripts/replay_r401_val_l2_s0_through_a1_checker.py"
RELEASE_BUILDER = "scripts/build_r401_val_l2_a1_release_provenance.py"
RELEASE_CONTRACT_DOC = (
    "research/route_a_wave_trace/R401_VAL_L2_A1_RELEASE_PROVENANCE_CONTRACT.md"
)
EVALUATOR_SOURCE = "validated/capd_r401_local_complement_mp.cpp"
RUN_CONFIG = f"{RESULT_RELATIVE.as_posix()}/run_config.json"
AGGREGATE_SUMMARY = f"{RESULT_RELATIVE.as_posix()}/aggregate_summary.json"
AGGREGATE_MANIFEST = f"{RESULT_RELATIVE.as_posix()}/aggregate_manifest.json"
INDEPENDENT_CHECKER = f"{RESULT_RELATIVE.as_posix()}/independent_checker.json"
POSTCHECK = f"{RESULT_RELATIVE.as_posix()}/POSTCHECK_STATUS.json"
A415_CERTIFICATE = (
    "research/route_a_wave_trace/A415_ALL_SLAB_LOCAL_COMPLEMENT_CERTIFICATE.md"
)
PRODUCTION_REPORT = f"{RESULT_RELATIVE.as_posix()}/R401_VAL_L2_A1_REPORT.md"
S0_RESULT_RELATIVE = "results/r401_val_l2_s0_local_complement"
S0_REPLAY_HASH_FILES = {
    "checker_source_sha256": CHECKER,
    "adapter_source_sha256": S0_ADAPTER,
    "s0_release_provenance_sha256": (
        f"{S0_RESULT_RELATIVE}/RELEASE_PROVENANCE.json"
    ),
    "s0_manifest_sha256": f"{S0_RESULT_RELATIVE}/manifest.json",
    "s0_postcheck_sha256": f"{S0_RESULT_RELATIVE}/POSTCHECK_STATUS.json",
}
EXPECTED_S0_REPLAY_KEYS = {
    "protocol_id",
    "status",
    "source_release",
    *S0_REPLAY_HASH_FILES,
    "tree_count",
    "node_count",
    "manifest_hash_checks",
    "status_counts",
    "tree_counts",
    "claim_boundary",
}
EXPECTED_S0_STATUS_COUNTS = {
    "ENERGY_EXCLUDED": 183,
    "RETURN_EXCLUDED": 1_349,
    "UNKNOWN": 1_484,
}
EXPECTED_S0_TREE_COUNTS = [
    {
        "precision_bits": 128,
        "slab_id": "S000",
        "node_count": 486,
        "status_counts": {
            "ENERGY_EXCLUDED": 18,
            "RETURN_EXCLUDED": 229,
            "UNKNOWN": 239,
        },
    },
    {
        "precision_bits": 128,
        "slab_id": "S025",
        "node_count": 546,
        "status_counts": {
            "ENERGY_EXCLUDED": 31,
            "RETURN_EXCLUDED": 246,
            "UNKNOWN": 269,
        },
    },
    {
        "precision_bits": 128,
        "slab_id": "S050",
        "node_count": 574,
        "status_counts": {
            "ENERGY_EXCLUDED": 44,
            "RETURN_EXCLUDED": 247,
            "UNKNOWN": 283,
        },
    },
    {
        "precision_bits": 256,
        "slab_id": "S000",
        "node_count": 436,
        "status_counts": {
            "ENERGY_EXCLUDED": 18,
            "RETURN_EXCLUDED": 204,
            "UNKNOWN": 214,
        },
    },
    {
        "precision_bits": 256,
        "slab_id": "S025",
        "node_count": 488,
        "status_counts": {
            "ENERGY_EXCLUDED": 31,
            "RETURN_EXCLUDED": 217,
            "UNKNOWN": 240,
        },
    },
    {
        "precision_bits": 256,
        "slab_id": "S050",
        "node_count": 486,
        "status_counts": {
            "ENERGY_EXCLUDED": 41,
            "RETURN_EXCLUDED": 206,
            "UNKNOWN": 239,
        },
    },
]
S0_CLAIM_BOUNDARY = (
    "public S0 compatibility replay only; no held-out A1 slab was read or evaluated"
)

# These inputs must be present in the main freeze before production.  The
# main freeze itself is intentionally absent: a freeze may not hash itself.
REQUIRED_MAIN_FREEZE_HASHES = (
    CHECKER,
    PRODUCER,
    EVALUATOR_SOURCE,
    "validated/CAPD_DEPENDENCY.md",
    "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
    FORMAL_PROTOCOL,
    MACHINE_FREEZE,
    PREFREEZE_REVIEW,
    S0_REPLAY,
    S0_ADAPTER,
    RELEASE_BUILDER,
    RELEASE_CONTRACT_DOC,
    "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    "results/r401_val_l1_branch/summary.json",
    "results/r401_val_l1_branch/manifest.json",
    "results/r401_val_l1_branch/independent_checker.json",
    "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
)

L1_REPLAY_FILES = {
    "release_sha256": "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
    "summary_sha256": "results/r401_val_l1_branch/summary.json",
    "manifest_sha256": "results/r401_val_l1_branch/manifest.json",
    "checker_sha256": "results/r401_val_l1_branch/independent_checker.json",
    "postcheck_sha256": "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
}

STATIC_ROLES = {
    "formal_protocol": FORMAL_PROTOCOL,
    "machine_freeze": MACHINE_FREEZE,
    "main_freeze": MAIN_FREEZE,
    "prefreeze_review": PREFREEZE_REVIEW,
    "s0_compatibility_replay": S0_REPLAY,
    "producer_source": PRODUCER,
    "checker_source": CHECKER,
    "s0_adapter_source": S0_ADAPTER,
    "release_builder_source": RELEASE_BUILDER,
    "release_contract": RELEASE_CONTRACT_DOC,
    "evaluator_source": EVALUATOR_SOURCE,
}

RESULT_ROLES = {
    "run_config": RUN_CONFIG,
    "aggregate_summary": AGGREGATE_SUMMARY,
    "aggregate_manifest": AGGREGATE_MANIFEST,
    "independent_checker": INDEPENDENT_CHECKER,
    "postcheck": POSTCHECK,
    "a415_certificate": A415_CERTIFICATE,
    "production_report": PRODUCTION_REPORT,
}

EXPECTED_PROVENANCE_BINDING_KEYS = {
    "freeze_sha256",
    "run_config_file",
    "run_config_sha256",
    "aggregate_summary_file",
    "aggregate_summary_sha256",
    "aggregate_manifest_file",
    "aggregate_manifest_sha256",
    "evaluator_source_sha256",
    "evaluator_binary_file",
    "evaluator_binary_sha256",
    "capd_commit",
    "capd_flags",
    "scheduler",
    "logical_thresholds",
    "machine_freeze_file",
    "machine_freeze_sha256",
    "machine_requirements",
    "prefreeze_review_file",
    "prefreeze_review_sha256",
    "tree_manifest_root",
    "archive_generation_sha256",
}
EXPECTED_CHECKER_KEYS = {
    "schema_version",
    "protocol_id",
    "checker_mode",
    "checker_status",
    "milestone_status",
    "theorem_status",
    "final_status",
    "promotion_authorized",
    "aggregate_checks",
    "failure_count",
    "failures",
    "tree_stats",
    "l1_protected_box_replay",
    "checker_source_sha256",
    "provenance_bindings",
    "claim_boundary",
}
EXPECTED_POSTCHECK_KEYS = {
    "schema_version",
    "protocol_id",
    "checker_mode",
    "checker_status",
    "milestone_status",
    "theorem_status",
    "final_status",
    "promotion_authorized",
    "checker_file",
    "checker_sha256",
    "archive_generation_sha256",
    "provenance_bindings_sha256",
}

EXPECTED_RELEASE_KEYS = {
    "schema_version",
    "protocol_id",
    "release_contract",
    "release_status",
    "milestone_status",
    "theorem_status",
    "final_status",
    "promotion_authorized",
    "archive_generation_sha256",
    "tree_manifest_root",
    "artifact_roles",
    "files",
    "claim_boundary",
}


class ReleaseContractError(RuntimeError):
    """The final release hash or authority contract was violated."""


class StrictJSONError(ReleaseContractError):
    """A JSON object was malformed, ambiguous, or non-finite."""


class PathContractError(ReleaseContractError):
    """An input path was unsafe, non-canonical, missing, or a symlink."""


class StatusContractError(ReleaseContractError):
    """The checker/certificate status chain was not exactly accepted."""


class GenerationContractError(ReleaseContractError):
    """The ordered tree root or archive-generation binding disagreed."""


class InputSnapshot:
    """One-byte-snapshot view of every authoritative input opened in a pass."""

    def __init__(self) -> None:
        self._bytes: dict[Path, bytes] = {}

    def read_bytes(self, path: Path) -> bytes:
        checked = checked_path(path, label="SNAPSHOT_INPUT", require_file=True)
        if checked not in self._bytes:
            try:
                self._bytes[checked] = checked.read_bytes()
            except OSError as error:
                raise PathContractError(
                    f"UNREADABLE_SNAPSHOT_INPUT: {checked}: {error}"
                ) from error
        return self._bytes[checked]

    def assert_unchanged(self) -> None:
        """Fail closed if any path stopped naming its validated snapshot bytes."""

        for path, expected in self._bytes.items():
            checked = checked_path(path, label="SNAPSHOT_RECHECK", require_file=True)
            try:
                actual = checked.read_bytes()
            except OSError as error:
                raise GenerationContractError(
                    f"INPUT_CHANGED_DURING_RELEASE_BUILD: {checked}: {error}"
                ) from error
            if actual != expected:
                raise GenerationContractError(
                    f"INPUT_CHANGED_DURING_RELEASE_BUILD: {checked}"
                )


_ACTIVE_SNAPSHOT: ContextVar[InputSnapshot | None] = ContextVar(
    "r401_a1_release_snapshot",
    default=None,
)


@contextmanager
def capture_input_snapshot() -> Iterator[InputSnapshot]:
    snapshot = InputSnapshot()
    token = _ACTIVE_SNAPSHOT.set(snapshot)
    try:
        yield snapshot
    finally:
        _ACTIVE_SNAPSHOT.reset(token)


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

    def parse_finite_float(value: str) -> float:
        """Reject exponent overflow that ``parse_constant`` cannot see."""

        parsed = float(value)
        if not math.isfinite(parsed):
            raise StrictJSONError(f"NONFINITE_JSON_NUMBER: {value}")
        return parsed

    try:
        return json.loads(
            raw,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=reject_constant,
            parse_float=parse_finite_float,
        )
    except StrictJSONError:
        raise
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        raise StrictJSONError(f"MALFORMED_JSON: {error}") from error


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
    """Compare JSON values without Python's bool/int/float equality coercions."""

    try:
        return canonical_json_bytes(actual) == canonical_json_bytes(expected)
    except (TypeError, ValueError):
        return False


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def checked_path(
    path: Path,
    *,
    label: str,
    require_file: bool = False,
    require_directory: bool = False,
    allow_missing_leaf: bool = False,
) -> Path:
    """Reject symlinks before accepting a lexical absolute path."""

    absolute = lexical_absolute(path)
    cursor = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        cursor = cursor / part
        if cursor.is_symlink():
            raise PathContractError(f"SYMLINK_REJECTED_{label}: {cursor}")
        if not cursor.exists():
            if allow_missing_leaf and cursor == absolute:
                break
            raise PathContractError(f"MISSING_PATH_{label}: {cursor}")
    if require_file and not absolute.is_file():
        raise PathContractError(f"MISSING_REGULAR_FILE_{label}: {absolute}")
    if require_directory and not absolute.is_dir():
        raise PathContractError(f"MISSING_DIRECTORY_{label}: {absolute}")
    return absolute


def safe_relative_path(value: str) -> PurePosixPath:
    if (
        not isinstance(value, str)
        or not value
        or "\\" in value
        or "\x00" in value
    ):
        raise PathContractError(f"UNSAFE_PATH: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise PathContractError(f"PATH_TRAVERSAL: {value!r}")
    if (
        path.as_posix() != value
        or any(part in {"", "."} or part.startswith(".") for part in path.parts)
    ):
        raise PathContractError(f"NONCANONICAL_PATH: {value!r}")
    return path


def project_file(project_root: Path, relative: str) -> Path:
    safe = safe_relative_path(relative)
    candidate = project_root.joinpath(*safe.parts)
    try:
        lexical_absolute(candidate).relative_to(project_root)
    except ValueError as error:
        raise PathContractError(f"PATH_ESCAPES_PROJECT: {relative!r}") from error
    return checked_path(candidate, label=relative, require_file=True)


def project_relative(project_root: Path, path: Path) -> str:
    checked = checked_path(path, label="PROJECT_ARTIFACT", require_file=True)
    try:
        relative = checked.relative_to(project_root).as_posix()
    except ValueError as error:
        raise PathContractError(f"ARTIFACT_OUTSIDE_PROJECT: {checked}") from error
    return safe_relative_path(relative).as_posix()


def sha256(path: Path) -> str:
    snapshot = _ACTIVE_SNAPSHOT.get()
    if snapshot is not None:
        raw = snapshot.read_bytes(path)
    else:
        checked = checked_path(path, label="HASH_INPUT", require_file=True)
        raw = checked.read_bytes()
    return hashlib.sha256(raw).hexdigest()


def authoritative_text(path: Path) -> str:
    snapshot = _ACTIVE_SNAPSHOT.get()
    try:
        raw = (
            snapshot.read_bytes(path)
            if snapshot is not None
            else checked_path(path, label="TEXT_INPUT", require_file=True).read_bytes()
        )
        return raw.decode("utf-8")
    except (OSError, UnicodeError) as error:
        raise StrictJSONError(f"UNREADABLE_UTF8_TEXT: {path}: {error}") from error


def strict_json_load(path: Path) -> Any:
    try:
        return strict_json_loads(authoritative_text(path))
    except StrictJSONError:
        raise


def require_mapping(payload: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(payload, Mapping):
        raise StrictJSONError(f"{label}_NOT_AN_OBJECT")
    return payload


def require_sha256(value: Any, label: str) -> str:
    if not isinstance(value, str) or not HEX_SHA256.fullmatch(value):
        raise GenerationContractError(f"INVALID_SHA256_{label}: {value!r}")
    return value


def expected_matrix() -> list[dict[str, Any]]:
    return [
        {"precision_bits": bits, "slab_id": f"S{index:03d}"}
        for bits in (128, 256)
        for index in range(51)
    ]


def require_namespace(payload: Mapping[str, Any], label: str) -> None:
    if not (
        type(payload.get("schema_version")) is int
        and payload.get("schema_version") == SCHEMA_VERSION
        and payload.get("protocol_id") == PROTOCOL_ID
    ):
        raise StatusContractError(f"{label}_NAMESPACE_MISMATCH")


def require_no_unexpected_authority_fields(
    payload: Mapping[str, Any],
    label: str,
    *,
    allowed: set[str],
) -> None:
    """Reject hidden status/verdict/authorization declarations in JSON."""

    for key in payload:
        lowered = str(key).lower()
        authority_like = (
            lowered == "status"
            or lowered == "verdict"
            or lowered.endswith("_status")
            or lowered.endswith("_authorized")
        )
        if authority_like and key not in allowed:
            raise StatusContractError(f"{label}_UNEXPECTED_AUTHORITY_FIELD: {key}")


def require_no_nested_authority_fields(
    payload: Any,
    label: str,
    *,
    path: str = "$",
) -> None:
    """Reject authority-like keys inside accepted checker containers."""

    if isinstance(payload, Mapping):
        for key, value in payload.items():
            lowered = str(key).lower()
            if (
                lowered == "status"
                or lowered == "verdict"
                or lowered.endswith("_status")
                or lowered.endswith("_authorized")
            ):
                raise StatusContractError(
                    f"{label}_NESTED_AUTHORITY_FIELD: {path}.{key}"
                )
            require_no_nested_authority_fields(
                value,
                label,
                path=f"{path}.{key}",
            )
    elif isinstance(payload, list):
        for index, value in enumerate(payload):
            require_no_nested_authority_fields(
                value,
                label,
                path=f"{path}[{index}]",
            )


def validate_checker_diagnostics(
    project_root: Path,
    checker: Mapping[str, Any],
) -> None:
    """Recompute non-authorizing checker diagnostics from bound artifacts.

    ``tree_stats`` and the L1 replay hashes are useful diagnostics, but they
    must not be accepted as self-authenticating prose.  Bind the former to the
    102 strict tree payload snapshots and the latter to the five actual L1
    release-chain files.
    """

    stats = checker.get("tree_stats")
    matrix = expected_matrix()
    if not isinstance(stats, list) or len(stats) != len(matrix):
        raise StatusContractError("INDEPENDENT_CHECKER_TREE_STATS_MATRIX_MISMATCH")
    expected_keys = {
        "precision_bits",
        "slab_id",
        "node_count",
        "energy_excluded",
        "return_excluded",
        "split_nodes",
    }
    for expected, record in zip(matrix, stats, strict=True):
        if not isinstance(record, Mapping) or set(record) != expected_keys:
            raise StatusContractError("INDEPENDENT_CHECKER_TREE_STATS_SCHEMA_MISMATCH")
        if not exact_json_equal(
            {
                "precision_bits": record.get("precision_bits"),
                "slab_id": record.get("slab_id"),
            },
            expected,
        ):
            raise StatusContractError("INDEPENDENT_CHECKER_TREE_STATS_ORDER_MISMATCH")
        counts = [
            record.get("node_count"),
            record.get("energy_excluded"),
            record.get("return_excluded"),
            record.get("split_nodes"),
        ]
        if not all(type(value) is int and value >= 0 for value in counts):
            raise StatusContractError("INDEPENDENT_CHECKER_TREE_STATS_COUNT_TYPE_MISMATCH")
        if counts[0] <= 0 or counts[0] != counts[1] + counts[2] + counts[3]:
            raise StatusContractError("INDEPENDENT_CHECKER_TREE_STATS_COUNT_MISMATCH")

        tree_relative = (
            f"{RESULT_RELATIVE.as_posix()}/trees/"
            f"{expected['precision_bits']}/{expected['slab_id']}.json"
        )
        tree = require_mapping(
            strict_json_load(project_file(project_root, tree_relative)),
            f"TREE_PAYLOAD_{expected['precision_bits']}_{expected['slab_id']}",
        )
        if not exact_json_equal(tree.get("tree"), expected):
            raise StatusContractError(
                "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_IDENTITY_MISMATCH"
            )
        nodes = tree.get("nodes")
        evaluated = tree.get("evaluated_node_count")
        if (
            not isinstance(nodes, list)
            or not nodes
            or type(evaluated) is not int
            or evaluated != len(nodes)
        ):
            raise StatusContractError(
                "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_NODE_COUNT_MISMATCH"
            )
        classifications: list[str] = []
        for node in nodes:
            if not isinstance(node, Mapping):
                raise StatusContractError(
                    "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_NODE_SCHEMA_MISMATCH"
                )
            evaluator_result = node.get("evaluator_result")
            if not isinstance(evaluator_result, Mapping):
                raise StatusContractError(
                    "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_NODE_SCHEMA_MISMATCH"
                )
            classification = evaluator_result.get("classification")
            if (
                not isinstance(classification, str)
                or classification not in {
                    "ENERGY_EXCLUDED",
                    "RETURN_EXCLUDED",
                    "SPLIT",
                }
            ):
                raise StatusContractError(
                    "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_CLASSIFICATION_MISMATCH"
                )
            classifications.append(classification)
        recomputed = {
            "node_count": len(nodes),
            "energy_excluded": classifications.count("ENERGY_EXCLUDED"),
            "return_excluded": classifications.count("RETURN_EXCLUDED"),
            "split_nodes": classifications.count("SPLIT"),
        }
        if not exact_json_equal(
            tree.get("terminal_counts"),
            {
                "ENERGY_EXCLUDED": recomputed["energy_excluded"],
                "RETURN_EXCLUDED": recomputed["return_excluded"],
            },
        ):
            raise StatusContractError(
                "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_TERMINAL_COUNT_MISMATCH"
            )
        if not exact_json_equal(
            {key: record.get(key) for key in recomputed},
            recomputed,
        ):
            raise StatusContractError(
                "INDEPENDENT_CHECKER_TREE_STATS_PAYLOAD_RECOMPUTATION_MISMATCH"
            )

    l1 = checker.get("l1_protected_box_replay")
    l1_keys = {
        "release_sha256",
        "summary_sha256",
        "manifest_sha256",
        "checker_sha256",
        "postcheck_sha256",
        "minimum_krawczyk_to_plan_boundary_margin",
    }
    if not isinstance(l1, Mapping) or set(l1) != l1_keys:
        raise StatusContractError("INDEPENDENT_CHECKER_L1_REPLAY_SCHEMA_MISMATCH")
    for key, relative in L1_REPLAY_FILES.items():
        claimed = require_sha256(l1.get(key), f"CHECKER_L1_{key}")
        if claimed != sha256(project_file(project_root, relative)):
            raise StatusContractError(
                f"INDEPENDENT_CHECKER_L1_REPLAY_HASH_MISMATCH: {key}"
            )
    margin = l1.get("minimum_krawczyk_to_plan_boundary_margin")
    if not isinstance(margin, Mapping) or set(margin) != {"numerator", "denominator"}:
        raise StatusContractError("INDEPENDENT_CHECKER_L1_MARGIN_SCHEMA_MISMATCH")
    if not (
        type(margin.get("numerator")) is int
        and margin.get("numerator") > 0
        and type(margin.get("denominator")) is int
        and margin.get("denominator") > 0
    ):
        raise StatusContractError("INDEPENDENT_CHECKER_L1_MARGIN_TYPE_MISMATCH")


def require_formal_producer_object(
    payload: Mapping[str, Any],
    label: str,
    producer_state: str,
) -> None:
    """Replay the immutable producer authority namespace on release inputs."""

    require_namespace(payload, label)
    require_no_unexpected_authority_fields(
        payload,
        label,
        allowed={"milestone_status", "theorem_status", "final_status"},
    )
    if not (
        payload.get("licensing") == "FROZEN_PRODUCTION"
        and payload.get("scientific_licensing_enabled") is True
        and payload.get("producer_state") == producer_state
        and payload.get("milestone_status") is None
        and payload.get("theorem_status") is None
        and payload.get("final_status") is None
    ):
        raise StatusContractError(f"{label}_FORMAL_PRODUCER_AUTHORITY_MISMATCH")


def require_null_final(payload: Mapping[str, Any], label: str) -> None:
    if payload.get("final_status") is not None:
        raise StatusContractError(f"{label}_FINAL_STATUS_MUST_BE_NULL")


def markdown_has_authority_declaration(line: str, *, verdict_only: bool = False) -> bool:
    """Fail closed on any standalone authority token in an evidence line.

    Exact accepted bytes are checked by the caller.  Token discovery must not
    depend on a separator catalogue: Markdown escapes, HTML entities, tables,
    and future punctuation all leave the standalone authority token visible.
    """

    token = (
        r"Verdict"
        if verdict_only
        else r"(?:Status|[A-Za-z][A-Za-z0-9_-]*_status|Verdict|"
        r"promotion_authorized|Claim\s+boundary)"
    )
    return re.search(
        rf"(?<![A-Za-z0-9_]){token}(?![A-Za-z0-9_])",
        line,
        flags=re.IGNORECASE,
    ) is not None


def require_exact_release_markdown(path: Path, label: str) -> None:
    """Require one closed, contradiction-free certificate status block.

    Markdown is not treated as free-form evidence at this final authority
    edge.  Every declaration-like line is collected, so appending a second
    PASS/FAIL status or a non-null final status cannot hide behind an earlier
    accepted substring.
    """

    checked = checked_path(path, label=label, require_file=True)
    try:
        lines = authoritative_text(checked).splitlines()
    except StrictJSONError as error:
        raise StatusContractError(f"{label}_NOT_UTF8_TEXT") from error
    declarations = [line for line in lines if markdown_has_authority_declaration(line)]
    expected = [
        f"Status: {PASS_STATUS}",
        f"milestone_status = {PASS_STATUS}",
        f"theorem_status = {PASS_STATUS}",
        "final_status = null",
        MARKDOWN_CLAIM_BOUNDARY,
    ]
    if declarations != expected:
        raise StatusContractError(
            f"{label}_STATUS_BLOCK_NOT_EXACT_OR_CONTRADICTORY"
        )


def require_exact_prefreeze_verdict(path: Path) -> None:
    """Mirror the checker gate without importing or trusting the checker."""

    checked = checked_path(path, label="PREFREEZE_REVIEW", require_file=True)
    try:
        lines = authoritative_text(checked).splitlines()
    except StrictJSONError as error:
        raise StatusContractError("PREFREEZE_REVIEW_NOT_UTF8_TEXT") from error
    declarations = [
        line
        for line in lines
        if markdown_has_authority_declaration(line, verdict_only=True)
    ]
    if declarations != ["Verdict: ACCEPT_FOR_FREEZE"]:
        raise StatusContractError("PREFREEZE_REVIEW_NOT_EXACTLY_ACCEPTED")


def expected_s0_replay_payload(project_root: Path) -> dict[str, Any]:
    """Build the one accepted S0 replay object from current immutable bytes."""

    bound_hashes: dict[str, str] = {}
    for field, relative in S0_REPLAY_HASH_FILES.items():
        path = project_file(project_root, relative)
        # The three public S0 objects remain JSON semantic evidence rather than
        # opaque blobs.  Parse and hash the same snapshot bytes.
        if relative.startswith(f"{S0_RESULT_RELATIVE}/"):
            strict_json_load(path)
        bound_hashes[field] = sha256(path)
    return {
        "protocol_id": "R401-VAL-L2-A1-PREFREEZE-S0-REPLAY",
        "status": "PASS_S0_READ_ONLY_COMPATIBILITY_REPLAY",
        "source_release": "R401-VAL-L2-S0",
        **bound_hashes,
        "tree_count": 6,
        "node_count": 3_016,
        "manifest_hash_checks": 6_055,
        "status_counts": EXPECTED_S0_STATUS_COUNTS,
        "tree_counts": EXPECTED_S0_TREE_COUNTS,
        "claim_boundary": S0_CLAIM_BOUNDARY,
    }


def validate_s0_replay(project_root: Path, s0: Mapping[str, Any]) -> None:
    """Require the exact ordered S0 compatibility replay and all byte hashes."""

    if set(s0) != EXPECTED_S0_REPLAY_KEYS:
        raise StatusContractError("S0_REPLAY_KEY_SET_MISMATCH")
    expected = expected_s0_replay_payload(project_root)
    for field in S0_REPLAY_HASH_FILES:
        claimed = require_sha256(s0.get(field), f"S0_REPLAY_{field}")
        if claimed != expected[field]:
            raise StatusContractError(f"S0_REPLAY_HASH_MISMATCH: {field}")
    if not (
        s0.get("protocol_id") == expected["protocol_id"]
        and s0.get("status") == expected["status"]
        and s0.get("source_release") == expected["source_release"]
        and s0.get("claim_boundary") == expected["claim_boundary"]
    ):
        raise StatusContractError("S0_REPLAY_NAMESPACE_STATUS_OR_BOUNDARY_MISMATCH")
    for field in ("tree_count", "node_count", "manifest_hash_checks"):
        if type(s0.get(field)) is not int or s0.get(field) != expected[field]:
            raise StatusContractError(f"S0_REPLAY_EXACT_COUNT_MISMATCH: {field}")
    if not exact_json_equal(s0.get("status_counts"), expected["status_counts"]):
        raise StatusContractError("S0_REPLAY_STATUS_COUNTS_MISMATCH")
    if not exact_json_equal(s0.get("tree_counts"), expected["tree_counts"]):
        raise StatusContractError("S0_REPLAY_TREE_COUNTS_MISMATCH")


def validate_static_chain(project_root: Path) -> tuple[Mapping[str, Any], Mapping[str, Any], str]:
    formal_protocol = project_file(project_root, FORMAL_PROTOCOL)
    if f"`{PROTOCOL_ID}`" not in authoritative_text(formal_protocol):
        raise StatusContractError("FORMAL_PROTOCOL_ID_MISSING")

    machine = require_mapping(
        strict_json_load(project_file(project_root, MACHINE_FREEZE)),
        "MACHINE_FREEZE",
    )
    require_namespace(machine, "MACHINE_FREEZE")
    require_no_unexpected_authority_fields(
        machine,
        "MACHINE_FREEZE",
        allowed={"status"},
    )
    if not (
        machine.get("status") == "FROZEN_FOR_PRODUCTION"
        and machine.get("scientific_licensing_enabled") is True
        and exact_json_equal(
            machine.get("machine_requirements"), EXPECTED_MACHINE_REQUIREMENTS
        )
    ):
        raise StatusContractError("MACHINE_FREEZE_STATUS_MISMATCH")

    main_path = project_file(project_root, MAIN_FREEZE)
    main = require_mapping(strict_json_load(main_path), "MAIN_FREEZE")
    require_namespace(main, "MAIN_FREEZE")
    require_no_unexpected_authority_fields(
        main,
        "MAIN_FREEZE",
        allowed={"status"},
    )
    if not (
        main.get("status") == "FROZEN_FOR_PRODUCTION"
        and main.get("scientific_licensing_enabled") is True
        and main.get("checker_mode") == CHECKER_MODE
        and exact_json_equal(main.get("matrix"), expected_matrix())
        and exact_json_equal(
            main.get("machine_requirements"), EXPECTED_MACHINE_REQUIREMENTS
        )
        and exact_json_equal(main.get("per_tree_limits"), EXPECTED_PER_TREE_LIMITS)
        and exact_json_equal(main.get("scheduler"), EXPECTED_SCHEDULER)
        and exact_json_equal(
            main.get("logical_thresholds"), EXPECTED_LOGICAL_THRESHOLDS
        )
    ):
        raise StatusContractError("MAIN_FREEZE_STATUS_OR_MATRIX_MISMATCH")
    input_hashes = require_mapping(main.get("input_hashes"), "MAIN_FREEZE_INPUT_HASHES")
    if MAIN_FREEZE in input_hashes:
        raise GenerationContractError("MAIN_FREEZE_MUST_NOT_HASH_ITSELF")
    missing = set(REQUIRED_MAIN_FREEZE_HASHES) - set(input_hashes)
    if missing:
        raise GenerationContractError(
            f"MAIN_FREEZE_MISSING_RELEASE_INPUT_HASHES: {sorted(missing)}"
        )
    for relative, claimed_hash in input_hashes.items():
        if not isinstance(relative, str):
            raise GenerationContractError("MAIN_FREEZE_INPUT_PATH_NOT_STRING")
        safe_relative_path(relative)
        expected = require_sha256(claimed_hash, f"FROZEN_{relative}")
        input_path = project_file(project_root, relative)
        if sha256(input_path) != expected:
            raise GenerationContractError(f"MAIN_FREEZE_INPUT_HASH_MISMATCH: {relative}")
        if PurePosixPath(relative).suffix.lower() == ".json":
            strict_json_load(input_path)
    frozen_checker_hash = require_sha256(
        input_hashes.get(CHECKER), "FROZEN_CHECKER_SOURCE"
    )
    if main.get("checker_source_sha256") != frozen_checker_hash:
        raise GenerationContractError("MAIN_FREEZE_CHECKER_HASH_DAG_MISMATCH")
    if sha256(project_file(project_root, RELEASE_BUILDER)) != sha256(SCRIPT):
        raise GenerationContractError("EXECUTING_RELEASE_BUILDER_DIFFERS_FROM_FROZEN_SOURCE")

    evaluator = require_mapping(main.get("evaluator"), "MAIN_FREEZE_EVALUATOR")
    if set(evaluator) != EXPECTED_EVALUATOR_KEYS:
        raise GenerationContractError("MAIN_FREEZE_EVALUATOR_KEY_SET_MISMATCH")
    if evaluator.get("source_file") != EVALUATOR_SOURCE:
        raise GenerationContractError("MAIN_FREEZE_EVALUATOR_SOURCE_PATH_MISMATCH")
    if evaluator.get("source_sha256") != sha256(project_file(project_root, EVALUATOR_SOURCE)):
        raise GenerationContractError("MAIN_FREEZE_EVALUATOR_SOURCE_HASH_MISMATCH")
    binary_text = evaluator.get("binary_file")
    if (
        not isinstance(binary_text, str)
        or not Path(binary_text).is_absolute()
        or "\x00" in binary_text
        or "\\" in binary_text
        or "//" in binary_text
        or binary_text.endswith("/")
        or any(part in {".", ".."} for part in binary_text.split("/"))
        or os.path.abspath(binary_text) != binary_text
    ):
        raise PathContractError("MAIN_FREEZE_EVALUATOR_BINARY_NOT_ABSOLUTE")
    binary = checked_path(Path(binary_text), label="EVALUATOR_BINARY", require_file=True)
    if str(binary) != binary_text:
        raise PathContractError("MAIN_FREEZE_EVALUATOR_BINARY_NOT_CANONICAL")
    binary_hash = require_sha256(evaluator.get("binary_sha256"), "EVALUATOR_BINARY")
    if sha256(binary) != binary_hash:
        raise GenerationContractError("MAIN_FREEZE_EVALUATOR_BINARY_HASH_MISMATCH")
    capd_flags = evaluator.get("capd_flags")
    if (
        evaluator.get("capd_commit") != EXPECTED_CAPD_COMMIT
        or not isinstance(capd_flags, list)
        or not all(isinstance(flag, str) for flag in capd_flags)
        or not REQUIRED_CAPD_FLAGS.issubset(capd_flags)
    ):
        raise GenerationContractError("MAIN_FREEZE_EVALUATOR_CAPD_BINDING_MISMATCH")
    if not exact_json_equal(
        evaluator.get("status_returncode_whitelist"),
        EXPECTED_STATUS_RETURNCODE_WHITELIST,
    ):
        raise GenerationContractError("MAIN_FREEZE_EVALUATOR_WHITELIST_MISMATCH")

    machine_evaluator = require_mapping(machine.get("evaluator"), "MACHINE_FREEZE_EVALUATOR")
    if not (
        machine_evaluator.get("source_file") == EVALUATOR_SOURCE
        and machine_evaluator.get("source_sha256") == evaluator.get("source_sha256")
        and machine_evaluator.get("binary_file") == binary_text
        and machine_evaluator.get("binary_sha256") == binary_hash
    ):
        raise GenerationContractError("MACHINE_MAIN_EVALUATOR_BINDING_MISMATCH")

    require_exact_prefreeze_verdict(project_file(project_root, PREFREEZE_REVIEW))
    s0 = require_mapping(
        strict_json_load(project_file(project_root, S0_REPLAY)),
        "S0_REPLAY",
    )
    require_no_unexpected_authority_fields(s0, "S0_REPLAY", allowed={"status"})
    validate_s0_replay(project_root, s0)
    return main, machine, project_relative(project_root, binary)


def validate_producer_objects(
    project_root: Path,
    main: Mapping[str, Any],
) -> tuple[Mapping[str, Any], Mapping[str, Any], Mapping[str, Any]]:
    run_config = require_mapping(
        strict_json_load(project_file(project_root, RUN_CONFIG)), "RUN_CONFIG"
    )
    require_namespace(run_config, "RUN_CONFIG")
    require_no_unexpected_authority_fields(
        run_config,
        "RUN_CONFIG",
        allowed={"milestone_status", "theorem_status", "final_status"},
    )
    if not (
        run_config.get("licensing") == "FROZEN_PRODUCTION"
        and run_config.get("scientific_licensing_enabled") is True
        and run_config.get("producer_state") == "FROZEN_GENERATION_INITIALIZED"
        and run_config.get("milestone_status") is None
        and run_config.get("theorem_status") is None
    ):
        raise StatusContractError("RUN_CONFIG_AUTHORITY_MISMATCH")
    require_null_final(run_config, "RUN_CONFIG")
    binding = require_mapping(run_config.get("binding"), "RUN_CONFIG_BINDING")
    require_no_unexpected_authority_fields(
        binding,
        "RUN_CONFIG_BINDING",
        allowed=set(),
    )
    if set(binding) != EXPECTED_RUN_BINDING_KEYS:
        raise GenerationContractError("RUN_CONFIG_BINDING_KEY_SET_MISMATCH")
    if not (
        type(binding.get("schema_version")) is int
        and binding.get("schema_version") == SCHEMA_VERSION
        and binding.get("protocol_id") == PROTOCOL_ID
        and binding.get("licensing") == "FROZEN_PRODUCTION"
        and binding.get("scientific_licensing_enabled") is True
    ):
        raise StatusContractError("RUN_CONFIG_BINDING_NAMESPACE_OR_LICENSE_MISMATCH")
    if run_config.get("binding_sha256") != sha256_bytes(canonical_json_bytes(binding)):
        raise GenerationContractError("RUN_CONFIG_BINDING_HASH_MISMATCH")
    if binding.get("l2_a1_freeze_sha256") != sha256(project_file(project_root, MAIN_FREEZE)):
        raise GenerationContractError("RUN_CONFIG_MAIN_FREEZE_HASH_MISMATCH")
    if not exact_json_equal(binding.get("matrix"), expected_matrix()):
        raise GenerationContractError("RUN_CONFIG_MATRIX_MISMATCH")
    if not exact_json_equal(binding.get("input_hashes"), main.get("input_hashes")):
        raise GenerationContractError("RUN_CONFIG_INPUT_HASH_DAG_MISMATCH")
    if not exact_json_equal(binding.get("evaluator"), main.get("evaluator")):
        raise GenerationContractError("RUN_CONFIG_EVALUATOR_DIFFERS_FROM_FREEZE")
    for key, expected in (
        ("machine_requirements", EXPECTED_MACHINE_REQUIREMENTS),
        ("per_tree_limits", EXPECTED_PER_TREE_LIMITS),
        ("scheduler", EXPECTED_SCHEDULER),
        ("logical_thresholds", EXPECTED_LOGICAL_THRESHOLDS),
    ):
        if not exact_json_equal(binding.get(key), expected):
            raise GenerationContractError(f"RUN_CONFIG_{key.upper()}_MISMATCH")
    if binding.get("machine_freeze_sha256") != sha256(
        project_file(project_root, MACHINE_FREEZE)
    ):
        raise GenerationContractError("RUN_CONFIG_MACHINE_FREEZE_HASH_MISMATCH")

    summary = require_mapping(
        strict_json_load(project_file(project_root, AGGREGATE_SUMMARY)),
        "AGGREGATE_SUMMARY",
    )
    manifest = require_mapping(
        strict_json_load(project_file(project_root, AGGREGATE_MANIFEST)),
        "AGGREGATE_MANIFEST",
    )
    run_hash = sha256(project_file(project_root, RUN_CONFIG))
    for payload, label, state in (
        (summary, "AGGREGATE_SUMMARY", "FROZEN_ALL_TREES_ARCHIVED"),
        (manifest, "AGGREGATE_MANIFEST", "FROZEN_AGGREGATE_COMMITTED"),
    ):
        require_namespace(payload, label)
        require_no_unexpected_authority_fields(
            payload,
            label,
            allowed={"milestone_status", "theorem_status", "final_status"},
        )
        if not (
            payload.get("licensing") == "FROZEN_PRODUCTION"
            and payload.get("scientific_licensing_enabled") is True
            and payload.get("producer_state") == state
            and payload.get("run_config_sha256") == run_hash
            and payload.get("milestone_status") is None
            and payload.get("theorem_status") is None
        ):
            raise StatusContractError(f"{label}_AUTHORITY_OR_RUN_BINDING_MISMATCH")
        require_null_final(payload, label)
    if type(summary.get("tree_count")) is not int or summary.get("tree_count") != 102:
        raise GenerationContractError("AGGREGATE_SUMMARY_TREE_COUNT_MISMATCH")
    if manifest.get("aggregate_summary_file") != "aggregate_summary.json":
        raise PathContractError("AGGREGATE_SUMMARY_PATH_MISMATCH")
    if manifest.get("aggregate_summary_sha256") != sha256(
        project_file(project_root, AGGREGATE_SUMMARY)
    ):
        raise GenerationContractError("AGGREGATE_SUMMARY_HASH_MISMATCH")
    return run_config, summary, manifest


def canonical_manifest_entries(
    project_root: Path,
    summary: Mapping[str, Any],
    manifest: Mapping[str, Any],
) -> list[dict[str, Any]]:
    summary_entries = summary.get("trees")
    manifest_entries = manifest.get("tree_manifests")
    if not isinstance(summary_entries, list) or not isinstance(manifest_entries, list):
        raise GenerationContractError("AGGREGATE_TREE_MANIFEST_LIST_MISSING")
    if not exact_json_equal(summary_entries, manifest_entries):
        raise GenerationContractError("AGGREGATE_TREE_MANIFEST_LIST_MISMATCH")
    matrix = expected_matrix()
    if len(summary_entries) != len(matrix):
        raise GenerationContractError("TREE_MANIFEST_MATRIX_LENGTH_MISMATCH")
    canonical: list[dict[str, Any]] = []
    seen: set[tuple[int, str]] = set()
    result_root = RESULT_RELATIVE.as_posix()
    run_hash = sha256(project_file(project_root, RUN_CONFIG))
    for expected, entry in zip(matrix, summary_entries, strict=True):
        if not isinstance(entry, Mapping):
            raise GenerationContractError("MALFORMED_TREE_MANIFEST_ENTRY")
        entry_identity = {
            "precision_bits": entry.get("precision_bits"),
            "slab_id": entry.get("slab_id"),
        }
        if not exact_json_equal(entry_identity, expected):
            raise GenerationContractError(
                f"TREE_MANIFEST_IDENTITY_TYPE_OR_VALUE_MISMATCH: {entry_identity!r}"
            )
        identity = (entry.get("precision_bits"), entry.get("slab_id"))
        expected_identity = (expected["precision_bits"], expected["slab_id"])
        if identity in seen:
            raise GenerationContractError(f"DUPLICATE_TREE_IDENTITY: {identity}")
        seen.add(identity)
        relative_inside_result = (
            f"tree_manifests/{expected['precision_bits']}/{expected['slab_id']}.json"
        )
        if entry.get("tree_manifest_file") != relative_inside_result:
            # Validate first so traversal is reported as such rather than only
            # as an identity mismatch.
            safe_relative_path(str(entry.get("tree_manifest_file", "")))
            raise PathContractError(
                f"TREE_MANIFEST_PATH_MISMATCH: {entry.get('tree_manifest_file')!r}"
            )
        project_relative_path = f"{result_root}/{relative_inside_result}"
        manifest_path = project_file(project_root, project_relative_path)
        # A hash is not a parser.  Strictly parse every manifest before using
        # its digest so duplicate keys or non-finite JSON cannot be hidden by
        # coherently updating the aggregate/checker hash chain.
        tree_manifest = require_mapping(
            strict_json_load(manifest_path),
            f"TREE_MANIFEST_{expected_identity}",
        )
        require_formal_producer_object(
            tree_manifest,
            f"TREE_MANIFEST_{expected_identity}",
            "FROZEN_TREE_COMMITTED",
        )
        if (
            not exact_json_equal(tree_manifest.get("tree"), expected)
            or tree_manifest.get("run_config_sha256") != run_hash
        ):
            raise GenerationContractError(
                f"TREE_MANIFEST_IDENTITY_OR_RUN_BINDING_MISMATCH: {expected_identity}"
            )
        tree_relative_inside_result = (
            f"trees/{expected['precision_bits']}/{expected['slab_id']}.json"
        )
        if tree_manifest.get("tree_file") != tree_relative_inside_result:
            safe_relative_path(str(tree_manifest.get("tree_file", "")))
            raise PathContractError(
                f"TREE_FILE_PATH_MISMATCH: {expected_identity}"
            )
        tree_project_relative = f"{result_root}/{tree_relative_inside_result}"
        tree_path = project_file(project_root, tree_project_relative)
        tree_payload = require_mapping(
            strict_json_load(tree_path),
            f"TREE_{expected_identity}",
        )
        require_formal_producer_object(
            tree_payload,
            f"TREE_{expected_identity}",
            "FROZEN_TREE_ARCHIVED",
        )
        if (
            not exact_json_equal(tree_payload.get("tree"), expected)
            or tree_payload.get("run_config_sha256") != run_hash
        ):
            raise GenerationContractError(
                f"TREE_IDENTITY_OR_RUN_BINDING_MISMATCH: {expected_identity}"
            )
        if tree_manifest.get("tree_sha256") != sha256(tree_path):
            raise GenerationContractError(
                f"TREE_FILE_HASH_MISMATCH: {expected_identity}"
            )
        if not isinstance(tree_manifest.get("node_files"), Mapping):
            raise GenerationContractError(
                f"TREE_MANIFEST_NODE_MAP_MISSING: {expected_identity}"
            )
        actual_hash = sha256(manifest_path)
        claimed_hash = require_sha256(
            entry.get("tree_manifest_sha256"),
            f"TREE_MANIFEST_{expected_identity}",
        )
        if claimed_hash != actual_hash:
            raise GenerationContractError(
                f"TREE_MANIFEST_HASH_MISMATCH: {expected_identity}"
            )
        if set(entry) != {
            "precision_bits",
            "slab_id",
            "tree_manifest_file",
            "tree_manifest_sha256",
        }:
            raise GenerationContractError(
                f"TREE_MANIFEST_ENTRY_KEY_SET_MISMATCH: {expected_identity}"
            )
        canonical.append(dict(entry))
    return canonical


def validate_checker_chain(
    project_root: Path,
    main: Mapping[str, Any],
    machine: Mapping[str, Any],
    evaluator_binary_relative: str,
    summary: Mapping[str, Any],
    manifest: Mapping[str, Any],
) -> tuple[Mapping[str, Any], Mapping[str, Any], dict[str, Any], str]:
    checker = require_mapping(
        strict_json_load(project_file(project_root, INDEPENDENT_CHECKER)),
        "INDEPENDENT_CHECKER",
    )
    postcheck = require_mapping(
        strict_json_load(project_file(project_root, POSTCHECK)), "POSTCHECK"
    )
    require_namespace(checker, "INDEPENDENT_CHECKER")
    require_namespace(postcheck, "POSTCHECK")
    if set(checker) != EXPECTED_CHECKER_KEYS:
        raise StatusContractError("INDEPENDENT_CHECKER_KEY_SET_MISMATCH")
    if set(postcheck) != EXPECTED_POSTCHECK_KEYS:
        raise StatusContractError("POSTCHECK_KEY_SET_MISMATCH")
    for payload, label in ((checker, "INDEPENDENT_CHECKER"), (postcheck, "POSTCHECK")):
        require_no_unexpected_authority_fields(
            payload,
            label,
            allowed={
                "checker_status",
                "milestone_status",
                "theorem_status",
                "final_status",
                "promotion_authorized",
            },
        )
        if not (
            payload.get("checker_mode") == CHECKER_MODE
            and payload.get("checker_status") == CHECKER_STATUS
            and payload.get("milestone_status") == PASS_STATUS
            and payload.get("theorem_status") == PASS_STATUS
            and payload.get("promotion_authorized") is True
        ):
            raise StatusContractError(f"{label}_STATUS_MISMATCH")
        require_null_final(payload, label)
    root_authority = {
        "checker_status",
        "milestone_status",
        "theorem_status",
        "final_status",
        "promotion_authorized",
    }
    for key, value in checker.items():
        if key not in root_authority:
            require_no_nested_authority_fields(
                value,
                "INDEPENDENT_CHECKER",
                path=f"$.{key}",
            )
    validate_checker_diagnostics(project_root, checker)
    if not (
        checker.get("checker_source_sha256")
        == sha256(project_file(project_root, CHECKER))
        and checker.get("claim_boundary") == CHECKER_CLAIM_BOUNDARY
        and type(checker.get("aggregate_checks")) is int
        and checker.get("aggregate_checks") > 0
        and type(checker.get("failure_count")) is int
        and checker.get("failure_count") == 0
        and checker.get("failures") == []
    ):
        raise StatusContractError("INDEPENDENT_CHECKER_SOURCE_OR_CLAIM_MISMATCH")
    if postcheck.get("checker_file") != "independent_checker.json":
        raise PathContractError("POSTCHECK_CHECKER_PATH_MISMATCH")
    if postcheck.get("checker_sha256") != sha256(
        project_file(project_root, INDEPENDENT_CHECKER)
    ):
        raise GenerationContractError("POSTCHECK_CHECKER_HASH_MISMATCH")

    bindings = require_mapping(
        checker.get("provenance_bindings"), "CHECKER_PROVENANCE_BINDINGS"
    )
    if set(bindings) != EXPECTED_PROVENANCE_BINDING_KEYS:
        raise GenerationContractError(
            "CHECKER_PROVENANCE_BINDING_KEY_SET_MISMATCH: "
            f"missing={sorted(EXPECTED_PROVENANCE_BINDING_KEYS - set(bindings))}, "
            f"extra={sorted(set(bindings) - EXPECTED_PROVENANCE_BINDING_KEYS)}"
        )

    entries = canonical_manifest_entries(project_root, summary, manifest)
    root_hash = sha256_bytes(canonical_json_bytes(entries))
    expected_root = {
        "algorithm": "sha256_canonical_json_ordered_manifest_entries_v1",
        "entry_count": 102,
        "sha256": root_hash,
    }
    if not exact_json_equal(bindings.get("tree_manifest_root"), expected_root):
        raise GenerationContractError("CHECKER_TREE_MANIFEST_ROOT_MISMATCH")

    main_hash = sha256(project_file(project_root, MAIN_FREEZE))
    machine_hash = sha256(project_file(project_root, MACHINE_FREEZE))
    expected_scalar_bindings = {
        "freeze_sha256": main_hash,
        "run_config_file": "run_config.json",
        "run_config_sha256": sha256(project_file(project_root, RUN_CONFIG)),
        "aggregate_summary_file": "aggregate_summary.json",
        "aggregate_summary_sha256": sha256(
            project_file(project_root, AGGREGATE_SUMMARY)
        ),
        "aggregate_manifest_file": "aggregate_manifest.json",
        "aggregate_manifest_sha256": sha256(
            project_file(project_root, AGGREGATE_MANIFEST)
        ),
        "evaluator_source_sha256": sha256(
            project_file(project_root, EVALUATOR_SOURCE)
        ),
        "evaluator_binary_file": str(project_file(project_root, evaluator_binary_relative)),
        "evaluator_binary_sha256": sha256(
            project_file(project_root, evaluator_binary_relative)
        ),
        "machine_freeze_file": MACHINE_FREEZE,
        "machine_freeze_sha256": machine_hash,
        "prefreeze_review_file": PREFREEZE_REVIEW,
        "prefreeze_review_sha256": sha256(
            project_file(project_root, PREFREEZE_REVIEW)
        ),
    }
    for key, expected in expected_scalar_bindings.items():
        if bindings.get(key) != expected:
            raise GenerationContractError(f"CHECKER_BINDING_MISMATCH: {key}")
    if not exact_json_equal(
        bindings.get("machine_requirements"), machine.get("machine_requirements")
    ):
        raise GenerationContractError("CHECKER_MACHINE_REQUIREMENTS_MISMATCH")
    if not exact_json_equal(bindings.get("scheduler"), main.get("scheduler")):
        raise GenerationContractError("CHECKER_SCHEDULER_MISMATCH")
    if not exact_json_equal(
        bindings.get("logical_thresholds"), main.get("logical_thresholds")
    ):
        raise GenerationContractError("CHECKER_THRESHOLDS_MISMATCH")
    evaluator = require_mapping(main.get("evaluator"), "MAIN_FREEZE_EVALUATOR")
    if not (
        bindings.get("capd_commit") == evaluator.get("capd_commit")
        and bindings.get("capd_flags") == evaluator.get("capd_flags")
    ):
        raise GenerationContractError("CHECKER_CAPD_BINDING_MISMATCH")

    without_generation = dict(bindings)
    claimed_generation = require_sha256(
        without_generation.pop("archive_generation_sha256"),
        "ARCHIVE_GENERATION",
    )
    recomputed_generation = sha256_bytes(canonical_json_bytes(without_generation))
    if claimed_generation != recomputed_generation:
        raise GenerationContractError("ARCHIVE_GENERATION_SHA256_MISMATCH")
    if postcheck.get("archive_generation_sha256") != claimed_generation:
        raise GenerationContractError("POSTCHECK_ARCHIVE_GENERATION_MISMATCH")
    if postcheck.get("provenance_bindings_sha256") != sha256_bytes(
        canonical_json_bytes(bindings)
    ):
        raise GenerationContractError("POSTCHECK_PROVENANCE_BINDINGS_HASH_MISMATCH")
    return checker, postcheck, expected_root, claimed_generation


def _build_expected_release_from_active_snapshot(project_root: Path) -> dict[str, Any]:
    project_root = checked_path(
        project_root, label="PROJECT_ROOT", require_directory=True
    )
    expected_result = project_root.joinpath(*RESULT_RELATIVE.parts)
    checked_path(expected_result, label="RESULT_DIRECTORY", require_directory=True)
    main, machine, binary_relative = validate_static_chain(project_root)
    _run_config, summary, manifest = validate_producer_objects(project_root, main)
    _checker, _postcheck, tree_root, generation = validate_checker_chain(
        project_root,
        main,
        machine,
        binary_relative,
        summary,
        manifest,
    )

    require_exact_release_markdown(
        project_file(project_root, A415_CERTIFICATE), "A415_CERTIFICATE"
    )
    require_exact_release_markdown(
        project_file(project_root, PRODUCTION_REPORT), "PRODUCTION_REPORT"
    )

    roles = {**STATIC_ROLES, "evaluator_binary": binary_relative, **RESULT_ROLES}
    if len(set(roles.values())) != len(roles):
        raise PathContractError("DUPLICATE_ARTIFACT_ROLE_PATH")
    files = {relative: sha256(project_file(project_root, relative)) for relative in roles.values()}
    release_relative = f"{RESULT_RELATIVE.as_posix()}/{RELEASE_NAME}"
    if release_relative in files or release_relative in roles.values():
        raise GenerationContractError("RELEASE_PROVENANCE_MUST_NOT_HASH_ITSELF")
    return {
        "schema_version": SCHEMA_VERSION,
        "protocol_id": PROTOCOL_ID,
        "release_contract": RELEASE_CONTRACT,
        "release_status": PASS_STATUS,
        "milestone_status": PASS_STATUS,
        "theorem_status": PASS_STATUS,
        "final_status": None,
        "promotion_authorized": True,
        "archive_generation_sha256": generation,
        "tree_manifest_root": tree_root,
        "artifact_roles": roles,
        "files": files,
        "claim_boundary": (
            "pointwise reduced-root uniqueness in the frozen local P_+=0 chart only; "
            "no energy-shell/global, phase-cover, trace-domain, arithmetic-prime, "
            "Hilbert--Polya, zeta-zero, or RH promotion"
        ),
    }


def capture_expected_release(
    project_root: Path,
) -> tuple[dict[str, Any], InputSnapshot]:
    """Build one release from exactly the bytes parsed in this capture pass."""

    with capture_input_snapshot() as snapshot:
        payload = _build_expected_release_from_active_snapshot(project_root)
    return payload, snapshot


def build_expected_release(project_root: Path) -> dict[str, Any]:
    """Compatibility wrapper used by callers that only need the payload."""

    payload, snapshot = capture_expected_release(project_root)
    snapshot.assert_unchanged()
    return payload


def validate_release_payload(
    project_root: Path,
    payload: Mapping[str, Any],
) -> None:
    if set(payload) != EXPECTED_RELEASE_KEYS:
        raise GenerationContractError(
            "RELEASE_KEY_SET_MISMATCH: "
            f"missing={sorted(EXPECTED_RELEASE_KEYS - set(payload))}, "
            f"extra={sorted(set(payload) - EXPECTED_RELEASE_KEYS)}"
        )
    if not (
        type(payload.get("schema_version")) is int
        and payload.get("schema_version") == SCHEMA_VERSION
        and payload.get("protocol_id") == PROTOCOL_ID
        and payload.get("release_contract") == RELEASE_CONTRACT
        and payload.get("release_status") == PASS_STATUS
        and payload.get("milestone_status") == PASS_STATUS
        and payload.get("theorem_status") == PASS_STATUS
        and payload.get("final_status") is None
        and payload.get("promotion_authorized") is True
    ):
        raise StatusContractError("RELEASE_STATUS_MISMATCH")
    roles = require_mapping(payload.get("artifact_roles"), "RELEASE_ARTIFACT_ROLES")
    files = require_mapping(payload.get("files"), "RELEASE_FILES")
    expected_roles = set(STATIC_ROLES) | set(RESULT_ROLES) | {"evaluator_binary"}
    if set(roles) != expected_roles:
        raise GenerationContractError("RELEASE_ARTIFACT_ROLE_SET_MISMATCH")
    values: list[str] = []
    for role in sorted(roles):
        value = roles[role]
        if not isinstance(value, str):
            raise PathContractError(f"NONSTRING_ARTIFACT_PATH: {role}")
        values.append(safe_relative_path(value).as_posix())
    if len(set(values)) != len(values):
        raise PathContractError("DUPLICATE_ARTIFACT_ROLE_PATH")
    if set(files) != set(values):
        raise GenerationContractError("RELEASE_FILE_HASH_EXACT_SET_MISMATCH")
    release_relative = f"{RESULT_RELATIVE.as_posix()}/{RELEASE_NAME}"
    if release_relative in values or release_relative in files:
        raise GenerationContractError("RELEASE_PROVENANCE_MUST_NOT_HASH_ITSELF")
    for relative, expected_hash in files.items():
        safe_relative_path(relative)
        if sha256(project_file(project_root, relative)) != require_sha256(
            expected_hash, f"RELEASE_FILE_{relative}"
        ):
            raise GenerationContractError(f"RELEASE_FILE_HASH_MISMATCH: {relative}")


def write_once_or_verify(path: Path, payload: Mapping[str, Any]) -> None:
    """Publish from an open inode into a pinned directory without overwrite."""

    expected = canonical_json_bytes(payload)
    parent = checked_path(path.parent, label="RELEASE_PARENT", require_directory=True)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    cloexec = getattr(os, "O_CLOEXEC", 0)
    directory_fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | nofollow | cloexec)

    def read_descriptor(descriptor: int) -> bytes:
        os.lseek(descriptor, 0, os.SEEK_SET)
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                return b"".join(chunks)
            chunks.append(chunk)

    def open_existing() -> int | None:
        try:
            descriptor = os.open(
                path.name,
                os.O_RDONLY | nofollow | cloexec,
                dir_fd=directory_fd,
            )
        except FileNotFoundError:
            return None
        except OSError as error:
            raise PathContractError(
                f"UNSAFE_OR_UNREADABLE_RELEASE_OUTPUT: {path}: {error}"
            ) from error
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            os.close(descriptor)
            raise PathContractError(f"RELEASE_OUTPUT_NOT_REGULAR_FILE: {path}")
        return descriptor

    try:
        existing_fd = open_existing()
    except Exception:
        os.close(directory_fd)
        raise
    if existing_fd is not None:
        try:
            if os.fstat(existing_fd).st_nlink != 1:
                raise PathContractError("RELEASE_OUTPUT_HAS_HARDLINK_ALIAS")
            if read_descriptor(existing_fd) != expected:
                raise GenerationContractError(
                    "RELEASE_ALREADY_BOUND_TO_DIFFERENT_GENERATION"
                )
            return
        finally:
            os.close(existing_fd)
            os.close(directory_fd)

    temporary_name = (
        f".{path.name}.seal-{os.getpid()}-{secrets.token_hex(16)}"
    )
    temporary_fd: int | None = None
    temporary_unlinked = False
    try:
        temporary_fd = os.open(
            temporary_name,
            os.O_RDWR | os.O_CREAT | os.O_EXCL | nofollow | cloexec,
            0o600,
            dir_fd=directory_fd,
        )
        view = memoryview(expected)
        while view:
            written = os.write(temporary_fd, view)
            if written <= 0:
                raise OSError("short write while sealing release")
            view = view[written:]
        os.fsync(temporary_fd)
        source_stat = os.fstat(temporary_fd)
        created = False
        try:
            # /proc/self/fd plus AT_SYMLINK_FOLLOW makes linkat bind the open
            # source inode, not the mutable temporary pathname.
            os.link(
                f"/proc/self/fd/{temporary_fd}",
                path.name,
                dst_dir_fd=directory_fd,
                follow_symlinks=True,
            )
            created = True
        except FileExistsError:
            created = False
        except OSError as error:
            raise GenerationContractError(
                f"RELEASE_PUBLICATION_SOURCE_OR_LINK_FAILURE: {error}"
            ) from error

        published_fd = open_existing()
        if published_fd is None:
            raise GenerationContractError("RELEASE_PUBLICATION_DISAPPEARED")
        try:
            published_stat = os.fstat(published_fd)
            if created and (
                published_stat.st_dev != source_stat.st_dev
                or published_stat.st_ino != source_stat.st_ino
            ):
                raise GenerationContractError("RELEASE_PUBLICATION_INODE_MISMATCH")
            if read_descriptor(published_fd) != expected:
                raise GenerationContractError(
                    "RELEASE_ALREADY_BOUND_TO_DIFFERENT_GENERATION"
                )
            os.unlink(temporary_name, dir_fd=directory_fd)
            temporary_unlinked = True
            if os.fstat(published_fd).st_nlink != 1:
                raise GenerationContractError("RELEASE_PUBLICATION_LINK_COUNT_MISMATCH")
        finally:
            os.close(published_fd)
        os.fsync(directory_fd)
    finally:
        if temporary_fd is not None:
            os.close(temporary_fd)
        if not temporary_unlinked:
            try:
                os.unlink(temporary_name, dir_fd=directory_fd)
            except FileNotFoundError:
                pass
        os.close(directory_fd)


def release_path(project_root: Path) -> Path:
    return project_root.joinpath(*RESULT_RELATIVE.parts, RELEASE_NAME)


def build_release(project_root: Path) -> dict[str, Any]:
    project_root = checked_path(
        project_root, label="PROJECT_ROOT", require_directory=True
    )
    payload, snapshot = capture_expected_release(project_root)
    snapshot.assert_unchanged()
    validate_release_payload(project_root, payload)
    snapshot.assert_unchanged()
    write_once_or_verify(release_path(project_root), payload)
    return payload


def verify_release(project_root: Path) -> dict[str, Any]:
    """Read-only validation of both the release bytes and their full DAG."""

    project_root = checked_path(
        project_root, label="PROJECT_ROOT", require_directory=True
    )
    path = checked_path(
        release_path(project_root), label="RELEASE_OUTPUT", require_file=True
    )
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    cloexec = getattr(os, "O_CLOEXEC", 0)
    try:
        release_fd = os.open(path, os.O_RDONLY | nofollow | cloexec)
    except OSError as error:
        raise PathContractError(f"UNREADABLE_RELEASE_OUTPUT: {path}: {error}") from error
    try:
        release_stat = os.fstat(release_fd)
        if not stat.S_ISREG(release_stat.st_mode):
            os.close(release_fd)
            raise PathContractError("RELEASE_OUTPUT_NOT_REGULAR_FILE")
        if release_stat.st_nlink != 1:
            os.close(release_fd)
            raise PathContractError("RELEASE_OUTPUT_HAS_HARDLINK_ALIAS")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(release_fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        raw = b"".join(chunks)
        decoded = raw.decode("utf-8")
    except (OSError, UnicodeError) as error:
        os.close(release_fd)
        raise StrictJSONError(f"UNREADABLE_JSON: {path}: {error}") from error
    try:
        payload = require_mapping(strict_json_loads(decoded), "RELEASE_PROVENANCE")
        if raw != canonical_json_bytes(payload):
            raise GenerationContractError("RELEASE_NONCANONICAL_BYTES")
        # Validate attacker-controlled paths before comparing with recomputation.
        validate_release_payload(project_root, payload)
        expected, snapshot = capture_expected_release(project_root)
        snapshot.assert_unchanged()
        if raw != canonical_json_bytes(expected):
            raise GenerationContractError("RELEASE_RECOMPUTATION_MISMATCH")
        current_stat = os.stat(path, follow_symlinks=False)
        final_fd_stat = os.fstat(release_fd)
        if (
            current_stat.st_dev != final_fd_stat.st_dev
            or current_stat.st_ino != final_fd_stat.st_ino
            or final_fd_stat.st_nlink != 1
        ):
            raise GenerationContractError("RELEASE_CHANGED_DURING_VERIFY")
        os.lseek(release_fd, 0, os.SEEK_SET)
        if os.read(release_fd, len(raw) + 1) != raw:
            raise GenerationContractError("RELEASE_CHANGED_DURING_VERIFY")
        return dict(payload)
    finally:
        os.close(release_fd)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="perform a strictly read-only replay; require an existing release",
    )
    args = parser.parse_args()
    payload = (
        verify_release(args.project_root)
        if args.verify_only
        else build_release(args.project_root)
    )
    print(
        json.dumps(
            {
                "protocol_id": payload["protocol_id"],
                "release_status": payload["release_status"],
                "archive_generation_sha256": payload["archive_generation_sha256"],
                "artifact_count": len(payload["files"]),
                "mode": "VERIFY_ONLY" if args.verify_only else "BUILD_OR_VERIFY_IDENTICAL",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
