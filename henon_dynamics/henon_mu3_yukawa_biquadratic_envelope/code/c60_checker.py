#!/usr/bin/env python3
"""Independent, fail-closed checker for the HCS-C60 machine tuple.

The checker reconstructs the exact fifteen-key payload without importing the
C60 certificate producer, the Python group producer, or the primitive-
resolvent producer.  Shared local imports are restricted to exact I/O and
backend constants plus the independently written primitive-resolvent checker.
The group calculation is executed independently through the final GAP
checker.  Every authority path is derived from this canonical project path;
no command-line path can select an upstream theorem authority.
"""

from __future__ import annotations

import argparse
import ast
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Any, Iterable, Iterator, Sequence

from c60_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deep_exact,
    prepare_output_targets,
    read_stable,
    reject_optimized_python,
    require_canonical_compact_json,
    require_exact_keys,
    require_sha256,
    safe_relative_path,
    sha256_bytes,
    strict_json_loads,
)
from c60_pipeline import EXPECTED_BACKENDS, EXPECTED_GAP, clean_environment
from c60_checker_resolvent import (
    H0_GENERATORS_ONE_BASED,
    J_GENERATORS_ONE_BASED,
    N_GENERATORS_ONE_BASED,
    SCHEMA_DESCRIPTOR as RESOLVER_SCHEMA_DESCRIPTOR,
    TRANSPORT_X_ONE_BASED,
    reconstruct_and_validate as reconstruct_resolver_evidence,
)


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


CODE_DIR = Path(__file__).resolve().parent
PROJECT = CODE_DIR.parent
if (
    CODE_DIR.name == "code"
    and PROJECT.name == "henon_mu3_yukawa_biquadratic_envelope"
    and PROJECT.parent.name == "henon_dynamics"
):
    REPO_ROOT = PROJECT.parents[1]
else:
    # Object-level tests may import a staged source, but no staged path gains
    # repository authority.  A full staging replay must use an isomorphic
    # shadow repository with the canonical henon_dynamics/project topology.
    REPO_ROOT = Path("/__C60_STAGED_SOURCE_HAS_NO_REPOSITORY_AUTHORITY__")

HENON = REPO_ROOT / "henon_dynamics"
C59 = HENON / "henon_mu3_yukawa_gassmann_twins"
BATCH = HENON / "BATCH_PLAN_C57_C61.md"
GUARD = HENON / "codex_prompt.md"
C59_ROUTE_ARCHIVE = C59 / "evaluations/route_a/HCS-C59/20260816T000000Z.yaml"

CERTIFICATE_SCHEMA_ID = "hcs-c60-certificate-schema-v1"
CHECK_REPORT_SCHEMA_ID = "hcs-c60-independent-check-report-v1"
GROUP_EVIDENCE_SCHEMA_ID = "hcs-c60-group-evidence-v1"
GROUP_PROJECTION_SCHEMA_ID = "hcs-c60-gap-normalizer-projection-v1"
RESOLVER_EVIDENCE_SCHEMA_ID = "hcs-c60-resolvent-evidence-v1"

MAX_CERTIFICATE_BYTES = 5_000_000
MAX_SCHEMA_BYTES = 300_000
MAX_GROUP_EVIDENCE_BYTES = 2_000_000
MAX_RESOLVER_EVIDENCE_BYTES = 5_000_000
MAX_CHILD_STDOUT_BYTES = 8_000_000

PAYLOAD_KEYS = (
    "artifact_contract",
    "G0_released_authority_rebind",
    "G1_common_normalizer_lattice",
    "G2_primitive_integral_carriers",
    "G3_formal_invariant_degree_gap",
    "G4_tower_characters_and_zeta",
    "G5_absolute_relative_arithmetic",
    "G6_both_relative_local_towers",
    "G7_independence_scope_release",
    "written_bridges",
    "backend_contract",
    "source_contract",
    "scope_nonclaims",
    "nonresults",
    "status",
)

CODE_SOURCE_NAMES = {
    "README.md",
    "c60_atomic_promote.py",
    "c60_checker.py",
    "c60_checker_group.g",
    "c60_checker_resolvent.py",
    "c60_exact.py",
    "c60_group.py",
    "c60_hash_manifest.py",
    "c60_pipeline.py",
    "c60_producer.py",
    "c60_resolvent.py",
    "run_all.sh",
    "test_c60.py",
}
RESULT_NAMES = {
    "RESULTS.md",
    "TEST_REPORT.md",
    "c60_certificate.json",
    "c60_check_report.json",
    "c60_group_evidence.json",
    "c60_resolvent_evidence.json",
    "c60_schema.json",
    "scoped_hash_manifest.json",
}
FORMAL_MARKDOWN_NAMES = {
    "DERIVATION.md",
    "EXPERIMENT_PLAN.md",
    "EXPERIMENT_TRACKER.md",
    "IMPLEMENTATION_CHECKLIST.md",
    "INTEGRITY_REPORT.md",
    "METHODOLOGY_BLUEPRINT.md",
    "NARRATIVE_REPORT.md",
    "PAPER_PLAN.md",
    "PROOF_PACKAGE.md",
    "README.md",
    "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md",
}
ARTIFACT_NAMES = ("c60_group_evidence.json", "c60_resolvent_evidence.json")

WRITTEN_BRIDGE_KEYS = {
    "released_C59_transport_to_C60_fixed_fields",
    "orbit_noncollision_to_primitive_fixed_fields",
    "coefficient_orbit_partitions_to_degree_two_obstruction",
    "subgroup_lattice_to_biquadratic_and_automorphisms",
    "v4_character_relation_to_zeta_identity",
    "conductors_to_signed_absolute_and_relative_discriminants",
    "double_cosets_to_relative_local_towers_and_tameness",
}

SCOPE_NONCLAIM_KEYS = {
    "target_selection_pilot_is_theorem_authority",
    "raw_tom_defines_fields",
    "finite_g_sets_isomorphic_from_character_relation",
    "formal_invariant_statement_after_root_relations",
    "expanded_characteristic_zero_resolvent_claimed",
    "characteristic_zero_coefficient_hash_claimed",
    "integral_basis_claimed",
    "maximal_order_claimed",
    "monogenicity_claimed",
    "class_number_claimed",
    "regulator_claimed",
    "trace_form_claimed",
    "d3_branch_selected",
    "local_fields_classified_by_nefd_rows",
    "decomposition_frobenius_claimed",
    "bad_artin_euler_claimed",
    "local_epsilon_factor_claimed",
    "local_root_number_claimed",
    "global_root_number_claimed",
    "artin_holomorphy_claimed",
    "automorphy_claimed",
    "rational_point_claimed",
    "hasse_principle_claimed",
    "weak_approximation_claimed",
    "brauer_manin_claimed",
    "motive_claimed",
    "rh_claimed",
    "hilbert_polya_operator_claimed",
    "paper_complete_claimed",
    "release_claimed",
}

if (
    len(PAYLOAD_KEYS) != 15
    or len(CODE_SOURCE_NAMES) != 13
    or len(RESULT_NAMES) != 8
    or len(FORMAL_MARKDOWN_NAMES) != 13
    or len(SCOPE_NONCLAIM_KEYS) != 30
):
    raise RuntimeError("C60 frozen inventory cardinality changed")

FORMAL_LOCK = {
    "markdown_aggregate_sha256": "fd76237963d385b79b10b7ea13477173b2cf17261fc47d5b43697379d9b012ca",
    "route_sha256": "2c7dc6a6f5f9fbe2d69c73e51a6e7e6aabad52fe516be8db17d3e1c305d94d77",
    "batch_sha256": "bd2a4881e636e18efd0d9917b99ba84b01c7507d6dcff0cefe28f5e5a3661cc3",
    "guard_sha256": "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead",
}
C59_LOCK = {
    "implementation_commit": "6c806120f17dab2e7b0bca37fcc156dfc459a4b7",
    "release_commit": "961c45f4b0c66ec94d2f069fd9ecc9d4b529d03a",
    "full_manifest_sha256": "4d756452d5b6d981e5fe4de3991cf6b7838f74fb8c411027a91dc2cf89a8d1a4",
    "full_manifest_entries": 63,
    "route_sha256": "fab227cc8e83155e39793d665ea721e46522d5beee77a113a19379b64b2130c5",
    "certificate_sha256": "3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a",
    "certificate_payload_sha256": "a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b",
    "schema_sha256": "07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4",
    "check_sha256": "271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3",
    "scoped_manifest_sha256": "c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda",
    "scoped_manifest_entries": 20,
    "group_evidence_sha256": "0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958",
    "resolvent_evidence_sha256": "667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6",
    "resolvent_module_sha256": "d4f70749054680487fdf2a2d41d11f4cbf184d03a4084c445d2d49837b5b712b",
}
GROUP_LOCK = {
    "aggregate_sha256": "dfd7d16a0128eae7a64906a4449a3022772dbc277abaae8187b6208340302464",
    "checker_source_sha256": "4338ad0e2af9a0fe096cbb6514de6c8d5227386a2ffadeac487a858fb160dde3",
    "checker_source_size_bytes": 43474,
    "evidence_sha256": "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2",
    "evidence_size_bytes": 40911,
    "projection_sha256": "77061a473c504925d24cfb2cedc26f7d4bc7057d4ee84615474cfa154323aba0",
    "projection_size_bytes": 34644,
    "schema_sha256": "8f57605397dff0bccda2a817775cbb143b6250172f0e938021b1f9cf7e1b2cba",
    "frozen_arrays_sha256": "0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5",
    "python_projection_sha256": "77b4b4cc56df4002dd4b180aef1a688145bd3de3937b399951bf6423dd8cfbac",
}
RESOLVER_LOCK = {
    "aggregate_sha256": "9ceda190badd260008fcb37788afd5f2a3e3457ca9e1e452f3999df24c12fe97",
    "checker_source_sha256": "5f4070831d4734ba3be93ae578d7a2be893f46676ab40cdaa4a2de6b8d3fb672",
    "evidence_sha256": "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da",
    "evidence_size_bytes": 9694,
    "payload_sha256": "eb17676ff10190c0b9f78e8f3fcb90121808fcd2c6a3b5d4dd06bfdc6177bb46",
    "schema_sha256": "fa120e247fa8ff69081059bccd2b94820b399662d2b781cb66c2f3f5f2275e8f",
    "schema_descriptor_sha256": "3144cffe82ff6056c44d2afe9b8c13fc91ef6001359b1fb33c7004993110515a",
}
GROUP_COMPONENT_CONTRACT = {
    "aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
    "producer_sha256": "fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b",
    "checker_sha256": GROUP_LOCK["checker_source_sha256"],
    "evidence_sha256": GROUP_LOCK["evidence_sha256"],
    "replay_sha256": GROUP_LOCK["projection_sha256"],
    "schema_sha256": GROUP_LOCK["schema_sha256"],
    "artifact_count": 10,
    "total_bytes": 248016,
}
RESOLVER_COMPONENT_CONTRACT = {
    "aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
    "producer_sha256": "61b157e8c3e5a68bf304f9499bc176f60fe16bf7c5e5f6d021fbec17d7d9465e",
    "checker_sha256": RESOLVER_LOCK["checker_source_sha256"],
    "evidence_sha256": RESOLVER_LOCK["evidence_sha256"],
    "payload_sha256": RESOLVER_LOCK["payload_sha256"],
    "artifact_count": 12,
    "total_bytes": 140873,
}

EXPECTED_COLLISION_BUCKETS = [
    [12, 15], [17, 21], [29, 36], [31, 39], [41, 42], [46, 48],
    [57, 58], [59, 64], [112, 120], [132, 140], [301, 303],
]
LARGE_PRIME = 14932047182473291995860108491583652133938007263719
EXACT_PRIME_SUPPORT = [3, 5, 181, 283, 997, 1801, 2346241, LARGE_PRIME]


def canonical_pretty(raw: bytes, *, max_bytes: int, label: str) -> Any:
    value = strict_json_loads(raw, max_bytes=max_bytes)
    if raw != canonical_json_bytes(value, pretty=True):
        raise StrictDataError(f"{label} is not canonical pretty JSON")
    return value


def compact_document(raw: bytes, *, max_bytes: int, label: str) -> dict[str, Any]:
    value = strict_json_loads(raw, max_bytes=max_bytes)
    require_canonical_compact_json(raw)
    if type(value) is not dict:
        raise StrictDataError(f"{label} must be an object")
    return value


def relative_to_repo(path: Path) -> str:
    try:
        return str(path.resolve(strict=True).relative_to(REPO_ROOT.resolve(strict=True)).as_posix())
    except ValueError as exc:
        raise StrictDataError(f"path escapes repository: {path}") from exc


def parse_sha_manifest(raw: bytes, *, expected_entries: int, label: str) -> list[tuple[str, str]]:
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise StrictDataError(f"{label} terminal newline mismatch")
    try:
        lines = raw.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise StrictDataError(f"{label} is not UTF-8") from exc
    if len(lines) != expected_entries:
        raise StrictDataError(f"{label} entry count mismatch")
    rows: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line in lines:
        if len(line) < 67 or line[64:66] != "  ":
            raise StrictDataError(f"{label} row grammar mismatch")
        digest, relative = line[:64], line[66:]
        require_sha256(digest, f"{label} digest")
        if not safe_relative_path(relative) or relative in seen:
            raise StrictDataError(f"{label} unsafe/duplicate path")
        seen.add(relative)
        rows.append((relative, digest))
    if [relative for relative, _ in rows] != sorted(seen):
        raise StrictDataError(f"{label} is not path-sorted")
    return rows


@dataclass(frozen=True)
class FileSeal:
    sha256: str
    size_bytes: int
    mode: int
    mtime_ns: int
    ctime_ns: int
    device: int
    inode: int
    nlink: int


@dataclass(frozen=True)
class DirectorySeal:
    mode: int
    mtime_ns: int
    ctime_ns: int
    device: int
    inode: int
    nlink: int


def seal_file(path: Path) -> FileSeal:
    raw, fingerprint = read_stable(path, max_bytes=500_000_000)
    metadata = path.stat()
    return FileSeal(
        sha256=sha256_bytes(raw),
        size_bytes=fingerprint.size_bytes,
        mode=fingerprint.mode,
        mtime_ns=fingerprint.mtime_ns,
        ctime_ns=metadata.st_ctime_ns,
        device=metadata.st_dev,
        inode=metadata.st_ino,
        nlink=metadata.st_nlink,
    )


def seal_directory(path: Path) -> DirectorySeal:
    before = path.lstat()
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISDIR(before.st_mode):
        raise StrictDataError(f"required real directory missing: {path}")
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_DIRECTORY", 0)
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        after = path.lstat()
    finally:
        os.close(descriptor)
    identity = (before.st_dev, before.st_ino)
    if identity != (opened.st_dev, opened.st_ino) or identity != (after.st_dev, after.st_ino):
        raise StrictDataError(f"directory changed while binding: {path}")
    return DirectorySeal(
        mode=stat.S_IMODE(opened.st_mode),
        mtime_ns=opened.st_mtime_ns,
        ctime_ns=opened.st_ctime_ns,
        device=opened.st_dev,
        inode=opened.st_ino,
        nlink=opened.st_nlink,
    )


class SnapshotGuard:
    """Full byte/metadata rebound before and after every child process."""

    def __init__(self, paths: Iterable[Path], *, directories: Iterable[Path] = ()):
        self.paths = tuple(sorted({path.resolve(strict=True) for path in paths}, key=str))
        self.directories = tuple(sorted({path.absolute() for path in directories}, key=str))
        self.expected = self.capture()
        self.expected_directories = self.capture_directories()
        self.rebind_checks = 0

    def capture(self) -> dict[str, FileSeal]:
        return {str(path): seal_file(path) for path in self.paths}

    def capture_directories(self) -> dict[str, DirectorySeal]:
        return {str(path): seal_directory(path) for path in self.directories}

    def assert_unchanged(self, label: str) -> None:
        observed = self.capture()
        observed_directories = self.capture_directories()
        self.rebind_checks += 1
        if observed != self.expected or observed_directories != self.expected_directories:
            changed = sorted(
                set(observed) ^ set(self.expected)
                | {key for key in set(observed) & set(self.expected) if observed[key] != self.expected[key]}
                | set(observed_directories) ^ set(self.expected_directories)
                | {
                    key for key in set(observed_directories) & set(self.expected_directories)
                    if observed_directories[key] != self.expected_directories[key]
                }
            )
            raise StrictDataError(f"protected snapshot changed at {label}: {changed}")


def run_bound_child(
    guard: SnapshotGuard,
    command: Sequence[str],
    *,
    cwd: Path,
    timeout: int,
    label: str,
) -> subprocess.CompletedProcess[bytes]:
    guard.assert_unchanged(f"before child {label}")
    try:
        completed = subprocess.run(
            list(command), cwd=cwd, env=clean_environment(),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=False, timeout=timeout,
        )
    finally:
        guard.assert_unchanged(f"after child {label}")
    if completed.returncode != 0:
        raise StrictDataError(
            f"{label} failed with exit {completed.returncode}; stderr={completed.stderr[:1000]!r}"
        )
    if completed.stderr:
        raise StrictDataError(f"{label} emitted stderr")
    if len(completed.stdout) > MAX_CHILD_STDOUT_BYTES:
        raise StrictDataError(f"{label} stdout exceeds limit")
    return completed


def exact_source_contract() -> dict[str, Any]:
    if not CODE_DIR.is_dir() or CODE_DIR.is_symlink() or CODE_DIR.resolve(strict=True) != CODE_DIR:
        raise StrictDataError("C60 code directory must be one canonical real directory")
    children = list(CODE_DIR.iterdir())
    names = {child.name for child in children}
    if names != CODE_SOURCE_NAMES:
        raise StrictDataError(
            "C60 exact 13-source inventory mismatch; "
            f"missing={sorted(CODE_SOURCE_NAMES-names)} extra={sorted(names-CODE_SOURCE_NAMES)}"
        )
    entries = []
    for name in sorted(CODE_SOURCE_NAMES):
        path = CODE_DIR / name
        raw, fingerprint = read_stable(path, max_bytes=8_000_000)
        expected_mode = 0o755 if name == "run_all.sh" else 0o644
        if fingerprint.mode != expected_mode or len(raw) != fingerprint.size_bytes:
            raise StrictDataError(f"C60 source mode/size mismatch: {name}")
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": fingerprint.size_bytes,
                "mode_octal": f"{expected_mode:04o}",
            }
        )
    return {
        "schema_id": "hcs-c60-source-contract-v1",
        "entry_count": 13,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [f"code/{name}" for name in sorted(CODE_SOURCE_NAMES)],
        "entries": entries,
        "mode_policy": "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644",
        "self_reference_policy": "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE",
    }


def c59_manifest_member_paths() -> list[Path]:
    raw, fingerprint = read_stable(C59 / "FULL_PROJECT_HASHES.sha256", max_bytes=1_000_000)
    if fingerprint.sha256 != C59_LOCK["full_manifest_sha256"]:
        raise StrictDataError("released C59 full-manifest digest mismatch")
    rows = parse_sha_manifest(
        raw,
        expected_entries=C59_LOCK["full_manifest_entries"],
        label="released C59 full manifest",
    )
    return [C59 / "FULL_PROJECT_HASHES.sha256", *(C59 / relative for relative, _ in rows)]


def verify_c59_full_manifest() -> dict[str, Any]:
    manifest = C59 / "FULL_PROJECT_HASHES.sha256"
    raw, fingerprint = read_stable(manifest, max_bytes=1_000_000)
    if fingerprint.sha256 != C59_LOCK["full_manifest_sha256"]:
        raise StrictDataError("released C59 full-manifest digest mismatch")
    rows = parse_sha_manifest(
        raw,
        expected_entries=C59_LOCK["full_manifest_entries"],
        label="released C59 full manifest",
    )
    declared = {relative for relative, _ in rows}
    verified_leaf_total_bytes = 0
    for relative, digest in rows:
        member_raw, member = read_stable(C59 / relative, max_bytes=500_000_000)
        if member.sha256 != digest or len(member_raw) != member.size_bytes:
            raise StrictDataError(f"released C59 manifest member mismatch: {relative}")
        verified_leaf_total_bytes += member.size_bytes
    live_files: set[str] = set()
    live_directories: set[str] = set()
    special: list[str] = []
    for child in C59.rglob("*"):
        relative = child.relative_to(C59).as_posix()
        if child.is_symlink() or (not child.is_file() and not child.is_dir()):
            special.append(relative)
        elif child.is_file() and relative != "FULL_PROJECT_HASHES.sha256":
            live_files.add(relative)
        elif child.is_dir():
            live_directories.add(relative)
    allowed_directories: set[str] = set()
    for relative in (*declared, "FULL_PROJECT_HASHES.sha256"):
        for parent in Path(relative).parents:
            if parent.as_posix() != ".":
                allowed_directories.add(parent.as_posix())
    if special or live_files != declared or live_directories != allowed_directories:
        raise StrictDataError(
            "released C59 exact inventory mismatch; "
            f"special={special}; missing={sorted(declared-live_files)}; "
            f"extra={sorted(live_files-declared)}"
        )
    return {
        "entry_count": len(rows),
        "inventory_exact_excluding_self": True,
        "manifest_path": relative_to_repo(manifest),
        "manifest_sha256": fingerprint.sha256,
        "manifest_size_bytes": fingerprint.size_bytes,
        "verified_leaf_total_bytes": verified_leaf_total_bytes,
    }


def verify_c59_scoped_manifest() -> dict[str, Any]:
    path = C59 / "results/scoped_hash_manifest.json"
    raw, fingerprint = read_stable(path, max_bytes=1_000_000)
    if fingerprint.sha256 != C59_LOCK["scoped_manifest_sha256"]:
        raise StrictDataError("released C59 scoped-manifest digest mismatch")
    value = canonical_pretty(raw, max_bytes=1_000_000, label="released C59 scoped manifest")
    require_exact_keys(
        value,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        "released C59 scoped manifest",
    )
    if (
        type(value["entries"]) is not list
        or value["entry_count"] != C59_LOCK["scoped_manifest_entries"]
        or value["entry_count"] != len(value["entries"])
        or value["manifest_self_included"] is not False
        or value["status"] != "PREFREEZE_CODE_RESULTS_PASS"
    ):
        raise StrictDataError("released C59 scoped-manifest status/count mismatch")
    declared: set[str] = set()
    for row in value["entries"]:
        require_exact_keys(row, {"path", "sha256", "size_bytes"}, "C59 scoped row")
        relative = row["path"]
        if not safe_relative_path(relative) or relative in declared:
            raise StrictDataError("released C59 scoped path mismatch")
        declared.add(relative)
        member_raw, member = read_stable(C59 / relative, max_bytes=500_000_000)
        if (
            type(row["size_bytes"]) is not int
            or row["size_bytes"] != member.size_bytes
            or row["sha256"] != member.sha256
            or len(member_raw) != member.size_bytes
        ):
            raise StrictDataError(f"released C59 scoped member mismatch: {relative}")
    live: set[str] = set()
    for root in (C59 / "code", C59 / "results"):
        for child in root.rglob("*"):
            if child.is_symlink() or (not child.is_dir() and not child.is_file()):
                raise StrictDataError("released C59 scoped tree contains special file")
            if child.is_file():
                relative = child.relative_to(C59).as_posix()
                if relative != "results/scoped_hash_manifest.json":
                    live.add(relative)
    if live != declared:
        raise StrictDataError("released C59 scoped inventory differs from manifest")
    return {
        "entry_count": len(declared),
        "inventory_exact_excluding_self": True,
        "manifest_path": relative_to_repo(path),
        "manifest_sha256": fingerprint.sha256,
        "manifest_size_bytes": fingerprint.size_bytes,
        "status": value["status"],
    }


def formal_target_lock() -> dict[str, Any]:
    markdown = {path.name: path for path in PROJECT.glob("*.md")}
    if set(markdown) != FORMAL_MARKDOWN_NAMES:
        raise StrictDataError("C60 exact 13-Markdown formal inventory mismatch")
    aggregate_rows = []
    entries = []
    for name in sorted(markdown):
        raw, fingerprint = read_stable(markdown[name], max_bytes=2_000_000)
        if b"NO_BAD_EULER_OR_ROOT_NUMBER" not in raw:
            raise StrictDataError(f"C60 formal scope firewall missing: {name}")
        aggregate_rows.append(f"{fingerprint.sha256}  {name}\n".encode("ascii"))
        entries.append(
            {
                "path": name,
                "sha256": fingerprint.sha256,
                "size_bytes": fingerprint.size_bytes,
            }
        )
    aggregate = sha256_bytes(b"".join(aggregate_rows))
    route_raw, route = read_stable(PROJECT / "route_a_evaluation.yaml", max_bytes=1_000_000)
    batch_raw, batch = read_stable(BATCH, max_bytes=1_000_000)
    guard_raw, guard = read_stable(GUARD, max_bytes=1_000_000)
    if (
        aggregate != FORMAL_LOCK["markdown_aggregate_sha256"]
        or route.sha256 != FORMAL_LOCK["route_sha256"]
        or batch.sha256 != FORMAL_LOCK["batch_sha256"]
        or guard.sha256 != FORMAL_LOCK["guard_sha256"]
    ):
        raise StrictDataError("C60 formal/Route/Batch/guard byte lock mismatch")
    for literal in (
        b"TARGET_LOCK_FORMAL_INPUT_PASS",
        b"THEOREM_TARGET_LOCKED_IMPLEMENTATION_PENDING",
        b"IMPLEMENTATION_PENDING",
        b"NOT_RELEASED",
        b"NO_BAD_EULER_OR_ROOT_NUMBER",
        GROUP_LOCK["aggregate_sha256"].encode("ascii"),
        RESOLVER_LOCK["aggregate_sha256"].encode("ascii"),
    ):
        if literal not in route_raw:
            raise StrictDataError(f"C60 Route lock literal missing: {literal!r}")
    if b"NO_BAD_EULER_OR_ROOT_NUMBER" not in batch_raw or not guard_raw:
        raise StrictDataError("C60 Batch/guard firewall mismatch")
    target_input_rows = [
        (BATCH.name, batch.sha256),
        *(
            (f"{PROJECT.name}/{name}", entry["sha256"])
            for name, entry in zip(sorted(markdown), entries)
        ),
        (f"{PROJECT.name}/route_a_evaluation.yaml", route.sha256),
    ]
    target_input_ledger = b"".join(
        f"{digest}  {relative}\n".encode("ascii")
        for relative, digest in sorted(target_input_rows)
    )
    target_input_ledger_sha256 = sha256_bytes(target_input_ledger)
    if target_input_ledger_sha256 != "88c467d0e856b334ed7b0e7ef10123d94cbcfe68310c461e234a710b114cab98":
        raise StrictDataError("C60 exact fifteen-input target-lock ledger differs")
    return {
        "formal_target_lock": {
            "aggregate_definition": "SHA256_OF_LEXICOGRAPHICALLY_BASENAME_ORDERED_SHA256SUM_LINES_FOR_EXACT_13_ROOT_MARKDOWN_FILES_ROUTE_EXCLUDED",
            "entries": entries,
            "entry_count": 13,
            "exact_formal_inventory": True,
            "markdown_aggregate_sha256": aggregate,
            "route_path": relative_to_repo(PROJECT / "route_a_evaluation.yaml"),
            "route_sha256": route.sha256,
            "route_size_bytes": route.size_bytes,
            "status": "TARGET_LOCK_FORMAL_INPUT_PASS",
            "target_lock_input_entry_count": 15,
            "target_lock_input_ledger_sha256": target_input_ledger_sha256,
        },
        "batch_target_lock": {
            "path": relative_to_repo(BATCH),
            "sha256": batch.sha256,
            "size_bytes": batch.size_bytes,
        },
        "protected_guard": {
            "path": relative_to_repo(GUARD),
            "sha256": guard.sha256,
            "size_bytes": guard.size_bytes,
        },
    }


def git_c59_release_rebind(guard: SnapshotGuard) -> None:
    for commit, label in (
        (C59_LOCK["implementation_commit"], "C59 implementation ancestry"),
        (C59_LOCK["release_commit"], "C59 release ancestry"),
    ):
        result = run_bound_child(
            guard,
            ["/usr/bin/git", "merge-base", "--is-ancestor", commit, "HEAD"],
            cwd=REPO_ROOT,
            timeout=60,
            label=label,
        )
        if result.stdout:
            raise StrictDataError(f"{label} emitted stdout")
    implementation_to_release = run_bound_child(
        guard,
        [
            "/usr/bin/git", "merge-base", "--is-ancestor",
            C59_LOCK["implementation_commit"], C59_LOCK["release_commit"],
        ],
        cwd=REPO_ROOT,
        timeout=60,
        label="C59 implementation-to-release ancestry",
    )
    if implementation_to_release.stdout:
        raise StrictDataError("C59 implementation-to-release ancestry emitted stdout")
    relative = (C59 / "FULL_PROJECT_HASHES.sha256").relative_to(REPO_ROOT).as_posix()
    committed = run_bound_child(
        guard,
        ["/usr/bin/git", "show", f"{C59_LOCK['release_commit']}:{relative}"],
        cwd=REPO_ROOT,
        timeout=60,
        label="C59 release committed manifest",
    )
    live, _ = read_stable(C59 / "FULL_PROJECT_HASHES.sha256", max_bytes=1_000_000)
    if committed.stdout != live:
        raise StrictDataError("C59 release commit does not bind live full manifest")


def validate_c59_certificate() -> dict[str, Any]:
    certificate_path = C59 / "results/c59_certificate.json"
    schema_path = C59 / "results/c59_schema.json"
    check_path = C59 / "results/c59_check_report.json"
    certificate_raw, certificate_fp = read_stable(certificate_path, max_bytes=5_000_000)
    schema_raw, schema_fp = read_stable(schema_path, max_bytes=1_000_000)
    check_raw, check_fp = read_stable(check_path, max_bytes=2_000_000)
    if (
        certificate_fp.sha256 != C59_LOCK["certificate_sha256"]
        or schema_fp.sha256 != C59_LOCK["schema_sha256"]
        or check_fp.sha256 != C59_LOCK["check_sha256"]
    ):
        raise StrictDataError("released C59 certificate/schema/check bytes differ")
    certificate = canonical_pretty(certificate_raw, max_bytes=5_000_000, label="C59 certificate")
    schema = canonical_pretty(schema_raw, max_bytes=1_000_000, label="C59 schema")
    check = canonical_pretty(check_raw, max_bytes=2_000_000, label="C59 check report")
    require_exact_keys(
        certificate,
        {"schema", "schema_sha256", "payload", "payload_sha256"},
        "C59 certificate root",
    )
    if (
        certificate["payload_sha256"] != C59_LOCK["certificate_payload_sha256"]
        or certificate["payload_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["payload"]))
        or certificate["schema_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["schema"]))
        or not deep_exact(certificate["schema"], schema)
        or check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
    ):
        raise StrictDataError("released C59 certificate semantic rebound differs")
    for path, expected in (
        (C59 / "results/c59_group_evidence.json", C59_LOCK["group_evidence_sha256"]),
        (C59 / "results/c59_resolvent_evidence.json", C59_LOCK["resolvent_evidence_sha256"]),
        (C59 / "code/c59_resolvent.py", C59_LOCK["resolvent_module_sha256"]),
    ):
        _, fingerprint = read_stable(path, max_bytes=5_000_000)
        if fingerprint.sha256 != expected:
            raise StrictDataError(f"released C59 durable input drift: {path.name}")
    return {
        "certificate_path": relative_to_repo(certificate_path),
        "certificate_sha256": certificate_fp.sha256,
        "certificate_size_bytes": certificate_fp.size_bytes,
        "payload_sha256": certificate["payload_sha256"],
        "schema_path": relative_to_repo(schema_path),
        "schema_sha256": schema_fp.sha256,
        "schema_size_bytes": schema_fp.size_bytes,
        "check_report_path": relative_to_repo(check_path),
        "check_report_sha256": check_fp.sha256,
        "check_report_size_bytes": check_fp.size_bytes,
        "check_result": check["result"],
    }


def file_binding(path: Path, expected_sha256: str) -> dict[str, Any]:
    raw, fingerprint = read_stable(path, max_bytes=5_000_000)
    if fingerprint.sha256 != expected_sha256 or len(raw) != fingerprint.size_bytes:
        raise StrictDataError(f"released file binding differs: {path.name}")
    return {
        "path": relative_to_repo(path),
        "sha256": fingerprint.sha256,
        "size_bytes": fingerprint.size_bytes,
    }


def released_c59_object_projection() -> dict[str, Any]:
    group_path = C59 / "results/c59_group_evidence.json"
    resolver_path = C59 / "results/c59_resolvent_evidence.json"
    group_raw, group_fp = read_stable(group_path, max_bytes=2_000_000)
    resolver_raw, resolver_fp = read_stable(resolver_path, max_bytes=5_000_000)
    if (
        group_fp.sha256 != C59_LOCK["group_evidence_sha256"]
        or resolver_fp.sha256 != C59_LOCK["resolvent_evidence_sha256"]
    ):
        raise StrictDataError("released C59 object-projection evidence bytes differ")
    group_document = compact_document(group_raw, max_bytes=2_000_000, label="C59 group evidence")
    resolver_document = compact_document(resolver_raw, max_bytes=5_000_000, label="C59 resolver evidence")
    require_exact_keys(resolver_document, {"payload", "payload_sha256", "schema_id", "schema_sha256"}, "C59 resolver document")
    if resolver_document["payload_sha256"] != sha256_bytes(canonical_json_bytes(resolver_document["payload"])):
        raise StrictDataError("released C59 resolver payload digest differs")
    resolver = resolver_document["payload"]
    frozen = group_document["frozen_permutation_arrays"]["arrays"]
    finite = resolver["finite_field"]
    lines = resolver["line_configuration"]
    invariants = resolver["invariants"]
    labelled_arrays = {
        "W27_generators": frozen["w27_simple_reflection_generators"],
        "Hplus_generators": frozen["h301_generators"],
        "Hminus_generators": frozen["h303_generators"],
    }
    roots_and_supports = {
        "factor_degrees": finite["factor_degrees"],
        "roots_sorted": finite["roots_sorted"],
        "roots_sha256": finite["roots_sha256"],
        "actual_to_standard_label": lines["actual_to_standard_label"],
        "alpha_by_standard_label": lines["alpha_by_standard_label"],
        "Hplus_seed_pairs": invariants["301"]["seed_pairs"],
        "Hplus_support": invariants["301"]["support"],
        "Hminus_seed_pairs": invariants["303"]["seed_pairs"],
        "Hminus_support": invariants["303"]["support"],
    }
    retained_local = {
        key: frozen[key]
        for key in sorted(frozen)
        if key.startswith("branch")
    }
    subgroup_rows = group_document["G2_gassmann_minimality"]["all_350_subgroup_classes"]
    if type(subgroup_rows) is not list or len(subgroup_rows) != 350:
        raise StrictDataError("released C59 ToM subgroup inventory differs")
    profiles: dict[tuple[int, ...], list[int]] = {}
    degrees = {}
    for index, row in enumerate(subgroup_rows, 1):
        if row.get("tom_index") != index:
            raise StrictDataError("released C59 ToM row order differs")
        profile = tuple(row["permutation_character_values"])
        profiles.setdefault(profile, []).append(index)
        degrees[index] = row["field_degree"]
    collisions = sorted((indices for indices in profiles.values() if len(indices) > 1), key=lambda item: item[0])
    field_degrees = [degrees[bucket[0]] for bucket in collisions]
    if collisions != EXPECTED_COLLISION_BUCKETS or field_degrees != [12960, 12960, 8640, 8640, 6480, 6480, 6480, 6480, 3240, 2880, 320]:
        raise StrictDataError("released C59 collision projection differs")
    projection = {
        "labelled_W_Hplus_Hminus_arrays_sha256": sha256_bytes(canonical_leaf_bytes(labelled_arrays)),
        "line_roots_and_supports_sha256": sha256_bytes(canonical_leaf_bytes(roots_and_supports)),
        "retained_C58_local_arrays_sha256": sha256_bytes(canonical_leaf_bytes(retained_local)),
        "tom_subgroup_class_count": len(subgroup_rows),
        "distinct_permutation_character_profile_count": len(profiles),
        "exact_collision_buckets": collisions,
        "collision_bucket_field_degrees": field_degrees,
        "split_prime": resolver["constants"]["prime"],
        "c59_certificate_payload_sha256": C59_LOCK["certificate_payload_sha256"],
    }
    if projection["split_prime"] != 692717 or finite["prime_proven"] is not True:
        raise StrictDataError("released C59 split-prime witness differs")
    if len(profiles) != 339:
        raise StrictDataError("released C59 distinct character-profile count differs")
    projection["canonical_sha256"] = sha256_bytes(canonical_leaf_bytes(projection))
    return projection


def rebuild_g0(guard: SnapshotGuard) -> dict[str, Any]:
    git_c59_release_rebind(guard)
    full = verify_c59_full_manifest()
    scoped = verify_c59_scoped_manifest()
    certificate = validate_c59_certificate()
    live_path = C59 / "route_a_evaluation.yaml"
    live_raw, live = read_stable(live_path, max_bytes=1_000_000)
    archive_raw, archive = read_stable(C59_ROUTE_ARCHIVE, max_bytes=1_000_000)
    if (
        live.sha256 != C59_LOCK["route_sha256"]
        or archive.sha256 != C59_LOCK["route_sha256"]
        or live_raw != archive_raw
    ):
        raise StrictDataError("released C59 live/archive Route identity mismatch")
    formal = formal_target_lock()
    group_binding = file_binding(
        C59 / "results/c59_group_evidence.json",
        C59_LOCK["group_evidence_sha256"],
    )
    resolver_binding = file_binding(
        C59 / "results/c59_resolvent_evidence.json",
        C59_LOCK["resolvent_evidence_sha256"],
    )
    return {
        "schema_id": "hcs-c60-released-authority-rebind-v1",
        "all_released_full_inventories_rebound": True,
        "fixed_predecessor_paths_only": True,
        "released_C59": {
            "candidate_id": "HCS-C59",
            "implementation_commit": C59_LOCK["implementation_commit"],
            "release_commit": C59_LOCK["release_commit"],
            "implementation_commit_ancestor_of_release_commit": True,
            "release_commit_ancestor_of_current_HEAD": True,
            "full_manifest": full,
            "scoped_manifest": scoped,
            "live_route": {
                "path": relative_to_repo(live_path),
                "sha256": live.sha256,
                "size_bytes": live.size_bytes,
            },
            "archive_route": {
                "path": relative_to_repo(C59_ROUTE_ARCHIVE),
                "sha256": archive.sha256,
                "size_bytes": archive.size_bytes,
            },
            "live_archive_route_identical": True,
            "certificate_bundle": certificate,
            "group_evidence": group_binding,
            "resolver_evidence": resolver_binding,
            "released_object_projection": released_c59_object_projection(),
            "status": "RELEASE_FROZEN",
        },
        **formal,
    }


def executable_file(path: Path, *, label: str) -> Path:
    resolved = path.resolve(strict=True)
    metadata = resolved.stat()
    if not stat.S_ISREG(metadata.st_mode) or not os.access(resolved, os.X_OK):
        raise StrictDataError(f"{label} must be an executable regular file")
    return resolved


def backend_contract(math_python: Path, gap_path: Path, guard: SnapshotGuard) -> dict[str, Any]:
    math = executable_file(math_python, label="math Python")
    gap = executable_file(gap_path, label="GAP")
    math_raw, math_fp = read_stable(math, max_bytes=40_000_000)
    gap_raw, gap_fp = read_stable(gap, max_bytes=1_000_000)
    expected_math = EXPECTED_BACKENDS["math"]
    if (
        sha256_bytes(math_raw) != expected_math["executable_sha256"]
        or math_fp.size_bytes != expected_math["executable_size_bytes"]
        or sha256_bytes(gap_raw) != EXPECTED_GAP["executable_sha256"]
        or gap_fp.size_bytes != EXPECTED_GAP["executable_size_bytes"]
    ):
        raise StrictDataError("backend executable bytes changed")
    python_source = (
        "import importlib.metadata,json,sys,flint,sympy,networkx,jsonschema;"
        "assert not sys.flags.optimize;"
        "print(json.dumps({'backend':'FLINT_SYMPY_NETWORKX',"
        "'python':list(sys.version_info[:3]),'flint':getattr(flint,'__version__','unknown'),"
        "'sympy':sympy.__version__,'networkx':networkx.__version__,"
        "'jsonschema':importlib.metadata.version('jsonschema')},"
        "sort_keys=True,separators=(',',':')))"
    )
    python_runs = [
        run_bound_child(
            guard,
            [str(math), "-s", "-B", "-c", python_source],
            cwd=Path("/"), timeout=60, label=f"math Python preflight run {index}",
        )
        for index in (1, 2)
    ]
    if python_runs[0].stdout != python_runs[1].stdout:
        raise StrictDataError("math Python preflight is nondeterministic")
    python_value = strict_json_loads(python_runs[0].stdout.strip(), max_bytes=10_000)
    expected_python = {
        "backend": "FLINT_SYMPY_NETWORKX",
        "python": expected_math["python"],
        "flint": expected_math["flint"],
        "sympy": expected_math["sympy"],
        "networkx": expected_math["networkx"],
        "jsonschema": expected_math["jsonschema"],
    }
    if not deep_exact(python_value, expected_python):
        raise StrictDataError(f"unsupported math backend versions: {python_value}")
    gap_source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",PackageInfo("ctbllib")[1].Version,"\\n");QUIT;'
    )
    gap_runs = [
        run_bound_child(
            guard,
            [str(gap), "-q", "-c", gap_source],
            cwd=Path("/"), timeout=60, label=f"GAP preflight run {index}",
        )
        for index in (1, 2)
    ]
    if gap_runs[0].stdout != gap_runs[1].stdout:
        raise StrictDataError("GAP preflight is nondeterministic")
    try:
        fields = gap_runs[0].stdout.decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise StrictDataError("GAP preflight is not ASCII") from exc
    observed_gap = {
        "resolved_executable": str(gap),
        "executable_sha256": sha256_bytes(gap_raw),
        "executable_size_bytes": gap_fp.size_bytes,
        "gap_version": fields[0] if len(fields) == 4 else "",
        "tomlib_version": fields[1] if len(fields) == 4 else "",
        "smallgrp_version": fields[2] if len(fields) == 4 else "",
        "ctbllib_version": fields[3] if len(fields) == 4 else "",
    }
    if not deep_exact(observed_gap, EXPECTED_GAP):
        raise StrictDataError(f"unsupported GAP backend: {observed_gap}")
    return {
        "schema_id": "hcs-c60-backend-contract-v1",
        "math_python": {
            "resolved_executable": str(math),
            "executable_sha256": sha256_bytes(math_raw),
            "executable_size_bytes": math_fp.size_bytes,
            "versions": python_value,
        },
        "gap": observed_gap,
        "two_run_deterministic": True,
        "pari_dependency": False,
        "singular_dependency": False,
    }


def run_group_projection(gap_path: Path, guard: SnapshotGuard) -> tuple[dict[str, Any], str, int]:
    gap = executable_file(gap_path, label="GAP")
    script = CODE_DIR / "c60_checker_group.g"
    script_raw, script_fp = read_stable(script, max_bytes=1_000_000)
    if (
        script_fp.sha256 != GROUP_LOCK["checker_source_sha256"]
        or script_fp.size_bytes != GROUP_LOCK["checker_source_size_bytes"]
        or not script_raw
    ):
        raise StrictDataError("final C60 GAP checker source differs")
    runs = [
        run_bound_child(
            guard,
            [str(gap), "-q", str(script)],
            cwd=CODE_DIR,
            timeout=900,
            label=f"independent C60 group replay run {index}",
        )
        for index in (1, 2)
    ]
    if runs[0].stdout != runs[1].stdout:
        raise StrictDataError("independent C60 GAP projection is nondeterministic")
    raw = runs[0].stdout
    require_canonical_compact_json(raw)
    projection = strict_json_loads(raw, max_bytes=MAX_CHILD_STDOUT_BYTES)
    require_exact_keys(
        projection,
        {
            "action", "character_relation", "coefficient_orbit_partitions",
            "collision_normalizer_scan", "frozen_permutation_arrays",
            "global_arithmetic", "local_arithmetic", "normalizer_tower",
            "schema_id", "software", "status",
        },
        "independent C60 GAP projection",
    )
    if (
        projection["schema_id"] != GROUP_PROJECTION_SCHEMA_ID
        or projection["status"] != "PASS"
        or projection["software"]
        != {"gap": "4.11.1", "tomlib": "1.2.9", "smallgrp": "1.4.1", "ctbllib": "1.3.1"}
        or sha256_bytes(raw) != GROUP_LOCK["projection_sha256"]
        or len(raw) != GROUP_LOCK["projection_size_bytes"]
    ):
        raise StrictDataError("independent C60 GAP projection identity differs")
    return projection, sha256_bytes(raw), len(raw)


def validate_group_evidence(
    document: dict[str, Any],
    projection: dict[str, Any],
    projection_sha256: str,
    projection_size_bytes: int,
) -> None:
    require_exact_keys(
        document,
        {
            "G1_common_normalizer_uniqueness",
            "G3_orbit_partition_obstruction",
            "G4_biquadratic_tower_characters",
            "G5_global_relative_discriminants",
            "G6_two_local_branches",
            "backend_contract",
            "frozen_permutation_arrays",
            "independent_replay",
            "schema_id",
            "source_contract",
            "status",
        },
        "C60 group evidence",
    )
    if document["schema_id"] != GROUP_EVIDENCE_SCHEMA_ID or document["status"] != "PASS":
        raise StrictDataError("C60 group evidence identity/status mismatch")
    g1 = document["G1_common_normalizer_uniqueness"]
    g3 = document["G3_orbit_partition_obstruction"]
    g4 = document["G4_biquadratic_tower_characters"]
    g5 = document["G5_global_relative_discriminants"]
    g6 = document["G6_two_local_branches"]
    require_exact_keys(g1, {"action", "collision_normalizer_scan", "common_normalizer", "normalizer_transport"}, "group G1")
    require_exact_keys(
        g4,
        {
            "character_relation", "fields", "intersection",
            "pairwise_generated_orders", "pairwise_intersection_orders",
            "pairwise_intersections_equal_J",
        },
        "group G4",
    )
    if not deep_exact(g1["action"], projection["action"]):
        raise StrictDataError("group evidence/GAP action mismatch")
    if not deep_exact(g1["collision_normalizer_scan"], projection["collision_normalizer_scan"]):
        raise StrictDataError("group evidence/GAP collision scan mismatch")
    if not deep_exact(g3, projection["coefficient_orbit_partitions"]):
        raise StrictDataError("group evidence/GAP coefficient partitions mismatch")
    if not deep_exact(g4["character_relation"], projection["character_relation"]):
        raise StrictDataError("group evidence/GAP character relation mismatch")
    for key in (
        "common_normalizer", "fields", "intersection", "normalizer_transport",
        "pairwise_generated_orders", "pairwise_intersection_orders",
        "pairwise_intersections_equal_J",
    ):
        evidence_value = g1[key] if key in g1 else g4[key]
        if not deep_exact(evidence_value, projection["normalizer_tower"][key]):
            raise StrictDataError(f"group evidence/GAP normalizer tower mismatch: {key}")
    if not deep_exact(g5["global_arithmetic"], projection["global_arithmetic"]):
        raise StrictDataError("group evidence/GAP global arithmetic mismatch")
    if not deep_exact(g6, projection["local_arithmetic"]):
        raise StrictDataError("group evidence/GAP local arithmetic mismatch")

    frozen = document["frozen_permutation_arrays"]
    require_exact_keys(frozen, {"arrays", "canonical_sha256", "runtime_tmp_dependency"}, "group frozen arrays")
    if (
        frozen["runtime_tmp_dependency"] is not False
        or not deep_exact(frozen["arrays"], projection["frozen_permutation_arrays"])
        or frozen["canonical_sha256"] != sha256_bytes(canonical_leaf_bytes(frozen["arrays"]))
        or frozen["canonical_sha256"] != GROUP_LOCK["frozen_arrays_sha256"]
    ):
        raise StrictDataError("group frozen-array authority mismatch")

    source = document["source_contract"]
    require_exact_keys(source, {"released_C59"}, "group source contract")
    released = source["released_C59"]
    if (
        released.get("release_commit") != C59_LOCK["release_commit"]
        or released.get("full_project_manifest_entries_verified") != C59_LOCK["full_manifest_entries"]
        or released.get("group_evidence_manifest_entry_verified") is not True
        or released.get("release_commit_is_ancestor_of_head") is not True
        or released.get("files", {}).get("project_manifest", {}).get("sha256") != C59_LOCK["full_manifest_sha256"]
        or released.get("files", {}).get("group_evidence", {}).get("sha256") != C59_LOCK["group_evidence_sha256"]
    ):
        raise StrictDataError("group evidence released-C59 source contract mismatch")
    backend = document["backend_contract"]
    if (
        backend.get("gap_executable_sha256") != EXPECTED_GAP["executable_sha256"]
        or backend.get("producer_source_sha256") != "fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b"
        or backend.get("producer_source_size_bytes") != 67866
        or backend.get("python_implementation") != "stdlib-only"
        or backend.get("software")
        != {"gap": "4.11.1", "tomlib": "1.2.9", "smallgrp": "1.4.1", "ctbllib": "1.3.1"}
    ):
        raise StrictDataError("group evidence backend contract mismatch")

    replay = document["independent_replay"]
    require_exact_keys(replay, {"cross_checks", "gap_checker", "python"}, "group independent replay")
    checker = replay["gap_checker"]
    if (
        checker.get("checker_projection_sha256") != projection_sha256
        or checker.get("checker_projection_size_bytes") != projection_size_bytes
        or checker.get("checker_source_sha256") != GROUP_LOCK["checker_source_sha256"]
        or checker.get("checker_source_size_bytes") != GROUP_LOCK["checker_source_size_bytes"]
        or checker.get("gap_executable_sha256") != EXPECTED_GAP["executable_sha256"]
        or checker.get("gap_executable_size_bytes") != EXPECTED_GAP["executable_size_bytes"]
        or checker.get("two_run_deterministic") is not True
    ):
        raise StrictDataError("group evidence independent GAP replay mismatch")
    cross = replay["cross_checks"]
    python = replay["python"]
    if (
        type(cross) is not dict
        or not cross
        or any(value is not True for value in cross.values())
        or python.get("status") != "PASS"
        or python.get("direct_projection_sha256") != GROUP_LOCK["python_projection_sha256"]
        or type(python.get("checks")) is not dict
        or any(value is not True for value in python["checks"].values())
    ):
        raise StrictDataError("group evidence independent Python replay mismatch")


def validate_resolver_evidence(
    document: dict[str, Any],
    guard: SnapshotGuard,
) -> dict[str, Any]:
    require_exact_keys(
        document,
        {"payload", "payload_sha256", "schema_id", "schema_sha256"},
        "C60 resolver evidence",
    )
    if (
        document["schema_id"] != RESOLVER_EVIDENCE_SCHEMA_ID
        or document["schema_sha256"] != RESOLVER_LOCK["schema_descriptor_sha256"]
        or document["payload_sha256"] != RESOLVER_LOCK["payload_sha256"]
        or document["payload_sha256"] != sha256_bytes(canonical_json_bytes(document["payload"]))
    ):
        raise StrictDataError("C60 resolver evidence root/digest mismatch")
    checker_raw, checker_fp = read_stable(CODE_DIR / "c60_checker_resolvent.py", max_bytes=1_000_000)
    if checker_fp.sha256 != RESOLVER_LOCK["checker_source_sha256"] or not checker_raw:
        raise StrictDataError("final C60 resolver checker source differs")
    guard.assert_unchanged("before in-process C60 resolver reconstruction")
    try:
        result = reconstruct_resolver_evidence(
            document,
            RESOLVER_SCHEMA_DESCRIPTOR,
            c59_resolvent_module=C59 / "code/c59_resolvent.py",
            c59_resolvent_evidence=C59 / "results/c59_resolvent_evidence.json",
            c59_full_manifest=C59 / "FULL_PROJECT_HASHES.sha256",
            c59_route=C59 / "route_a_evaluation.yaml",
            c59_route_archive=C59_ROUTE_ARCHIVE,
        )
    except Exception as exc:
        raise StrictDataError("independent C60 resolver reconstruction failed") from exc
    finally:
        guard.assert_unchanged("after in-process C60 resolver reconstruction")
    require_exact_keys(result, {"checks", "evidence_payload_sha256", "scope_literal", "status"}, "resolver checker result")
    if (
        result["evidence_payload_sha256"] != RESOLVER_LOCK["payload_sha256"]
        or result["scope_literal"] != "NO_BAD_EULER_OR_ROOT_NUMBER"
        or result["status"]
        != {"evidence_status": "PASS", "implementation_state": "EVIDENCE_REPLAY_PASS", "release_authorized": False}
        or type(result["checks"]) is not dict
        or any(value is not True for value in result["checks"].values())
    ):
        raise StrictDataError("independent C60 resolver reconstruction result mismatch")
    return document["payload"]


Permutation = tuple[int, ...]


def normalize_permutation(values: Sequence[int]) -> Permutation:
    if type(values) not in (list, tuple) or len(values) != 27:
        raise StrictDataError("permutation row length mismatch")
    result = tuple(value - 1 for value in values)
    if any(type(value) is not int for value in values) or sorted(result) != list(range(27)):
        raise StrictDataError("one-based permutation row mismatch")
    return result


def compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(27))


def generated_permutation_group(rows: Sequence[Sequence[int]]) -> tuple[Permutation, ...]:
    generators = tuple(normalize_permutation(row) for row in rows)
    identity = tuple(range(27))
    seen = {identity}
    queue = [identity]
    for element in queue:
        for generator in generators:
            image = compose_permutations(generator, element)
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return tuple(sorted(seen))


def canonical_point_partition(group: Sequence[Permutation]) -> list[list[int]]:
    orbits = {
        tuple(sorted({element[index] for element in group}))
        for index in range(27)
    }
    return [list(orbit) for orbit in sorted(orbits, key=lambda item: (len(item), item))]


def canonical_pair_partition(group: Sequence[Permutation]) -> list[list[list[int]]]:
    orbits = set()
    for left in range(27):
        for right in range(left + 1, 27):
            orbit = tuple(
                sorted(
                    {
                        tuple(sorted((element[left], element[right])))
                        for element in group
                    }
                )
            )
            orbits.add(orbit)
    return [
        [list(pair) for pair in orbit]
        for orbit in sorted(orbits, key=lambda item: (len(item), item))
    ]


def normalize_external_point_partition(value: Any) -> list[list[int]]:
    if type(value) is not list:
        raise StrictDataError("external point partition must be a list")
    normalized = []
    for orbit in value:
        if type(orbit) is not list or any(type(item) is not int for item in orbit):
            raise StrictDataError("external point orbit type mismatch")
        zero = tuple(sorted(item - 1 for item in orbit))
        normalized.append(zero)
    return [list(orbit) for orbit in sorted(set(normalized), key=lambda item: (len(item), item))]


def normalize_external_pair_partition(value: Any) -> list[list[list[int]]]:
    if type(value) is not list:
        raise StrictDataError("external pair partition must be a list")
    normalized = []
    for orbit in value:
        if type(orbit) is not list:
            raise StrictDataError("external pair orbit must be a list")
        pairs = []
        for pair in orbit:
            if (
                type(pair) is not list
                or len(pair) != 2
                or any(type(item) is not int for item in pair)
            ):
                raise StrictDataError("external unordered pair type mismatch")
            zero = tuple(sorted((pair[0] - 1, pair[1] - 1)))
            if zero[0] == zero[1]:
                raise StrictDataError("external unordered pair is diagonal")
            pairs.append(zero)
        normalized.append(tuple(sorted(pairs)))
    return [
        [list(pair) for pair in orbit]
        for orbit in sorted(set(normalized), key=lambda item: (len(item), item))
    ]


def derive_g1(
    group_evidence: dict[str, Any],
    resolver_payload: dict[str, Any],
    g0: dict[str, Any],
) -> dict[str, Any]:
    source = group_evidence["G1_common_normalizer_uniqueness"]
    tower = group_evidence["G4_biquadratic_tower_characters"]
    frozen = group_evidence["frozen_permutation_arrays"]["arrays"]
    scan = source["collision_normalizer_scan"]
    require_exact_keys(
        scan,
        {
            "exact_11_collision_buckets",
            "qualifying_buckets_normalizers_conjugate_and_index_two_over_both",
            "rows",
        },
        "G1 collision scan",
    )
    if (
        not deep_exact(scan["exact_11_collision_buckets"], EXPECTED_COLLISION_BUCKETS)
        or type(scan["rows"]) is not list
        or len(scan["rows"]) != 11
    ):
        raise StrictDataError("G1 exhaustive eleven-bucket scan mismatch")
    qualifying = []
    for bucket, row in zip(EXPECTED_COLLISION_BUCKETS, scan["rows"]):
        if type(row) is not dict or not deep_exact(row.get("bucket"), bucket):
            raise StrictDataError("G1 collision row order/bucket mismatch")
        conjugate = row.get("normalizers_conjugate_in_W")
        indices = row.get("normalizer_indices_over_subgroups")
        declared = row.get("normalizers_conjugate_and_index_two_over_both")
        if type(conjugate) is not bool or type(declared) is not bool:
            raise StrictDataError("G1 exact predicate boolean type mismatch")
        derived = conjugate is True and deep_exact(indices, [2, 2])
        if declared is not derived:
            raise StrictDataError("G1 exact uniqueness predicate was not derived exactly")
        if derived:
            qualifying.append(bucket)
    if (
        not deep_exact(qualifying, [[301, 303]])
        or not deep_exact(
            scan["qualifying_buckets_normalizers_conjugate_and_index_two_over_both"],
            [[301, 303]],
        )
    ):
        raise StrictDataError("G1 exact qualifying bucket is not uniquely 301/303")
    common = source["common_normalizer"]
    expected_common = {
        "abelian_invariants": [2, 2],
        "core_order_in_W": 1,
        "derived_order": 81,
        "id_group": [324, 39],
        "index_in_W": 160,
        "normalizer_order_in_W": 324,
        "order": 324,
        "quotient_by_J_id_group": [4, 2],
        "tom_locator": 327,
    }
    if not deep_exact(common, expected_common):
        raise StrictDataError("G1 common normalizer invariants mismatch")
    fields = tower["fields"]
    expected_fields = {
        "H301": ([162, 11], [2, 3], 27, 301),
        "H302": ([162, 10], [2, 3], 27, 302),
        "H303": ([162, 19], [2], 81, 303),
    }
    if (
        type(fields) is not list
        or len(fields) != 3
        or [row.get("label") for row in fields] != ["H301", "H302", "H303"]
    ):
        raise StrictDataError("G1 field subgroup count mismatch")
    by_label = {}
    for row in fields:
        label = row.get("label") if type(row) is dict else None
        if label not in expected_fields or label in by_label:
            raise StrictDataError("G1 field subgroup label mismatch")
        small, abelian, derived, tom = expected_fields[label]
        if (
            row.get("id_group") != small
            or row.get("abelian_invariants") != abelian
            or row.get("derived_order") != derived
            or row.get("tom_locator") != tom
            or row.get("order") != 162
            or row.get("field_degree") != 320
            or row.get("core_order_in_W") != 1
            or row.get("normal_in_N") is not True
            or row.get("normalizer_equals_N") is not True
        ):
            raise StrictDataError(f"G1 field subgroup invariants mismatch: {label}")
        by_label[label] = row
    intersection = tower["intersection"]
    if (
        intersection.get("order") != 81
        or intersection.get("index_in_W") != 640
        or intersection.get("tom_locator") != 266
        or intersection.get("core_order_in_W") != 1
        or intersection.get("normalizer_order_in_W") != 324
        or intersection.get("equals_derived_subgroup_of_N") is not True
        or intersection.get("normal_in_N") is not True
        or tower["pairwise_generated_orders"] != [324, 324, 324]
        or tower["pairwise_intersection_orders"] != [81, 81, 81]
        or tower["pairwise_intersections_equal_J"] is not True
    ):
        raise StrictDataError("G1 intersection/generated lattice mismatch")
    transport = source["normalizer_transport"]
    if (
        transport.get("transported_normalizer_equals_N") is not True
        or transport.get("H303_transport_contained_in_N") is not True
        or transport.get("right_action_equation_holds") is not True
        or transport.get("right_action_equation_checked_pairs") != 8748
        or transport.get("conjugating_permutation_one_based") != list(TRANSPORT_X_ONE_BASED)
    ):
        raise StrictDataError("G1 left/right transport bridge mismatch")
    durable = {
        "H301_generators": deepcopy(frozen["H301_generators"]),
        "H302_generators": deepcopy(frozen["H302_generators"]),
        "H303_source_generators": deepcopy(frozen["H303_generators"]),
        "H3_transported_generators": deepcopy(fields[2]["generators_one_based"]),
        "J_generators": deepcopy(frozen["J_generators"]),
        "N_generators": deepcopy(frozen["N_generators"]),
        "W27_generators": deepcopy(frozen["W27_generators"]),
        "branch140_D_generators": deepcopy(frozen["branch140_D_generators"]),
        "branch140_P_generators": deepcopy(frozen["branch140_P_generators"]),
        "branch140_Q_generators": deepcopy(frozen["branch140_Q_generators"]),
        "branch206_D_generators": deepcopy(frozen["branch206_D_generators"]),
        "branch206_I_generators": deepcopy(frozen["branch206_I_generators"]),
        "branch206_P_generators": deepcopy(frozen["branch206_P_generators"]),
        "branch206_Q_generators": deepcopy(frozen["branch206_Q_generators"]),
        "normalizer_conjugator": deepcopy(frozen["normalizer_conjugator"]),
    }
    if (
        durable["H302_generators"] != H0_GENERATORS_ONE_BASED
        or durable["J_generators"] != J_GENERATORS_ONE_BASED
        or durable["N_generators"] != N_GENERATORS_ONE_BASED
        or durable["normalizer_conjugator"] != TRANSPORT_X_ONE_BASED
    ):
        raise StrictDataError("G1 durable arrays differ from independent resolver checker")
    resolver_transport = resolver_payload["transport"]
    if (
        resolver_transport.get("label_permutation_one_based") != durable["normalizer_conjugator"]
        or resolver_transport.get("H3_equals_transported_support_stabilizer") is not True
        or resolver_transport.get("H3_contained_in_N") is not True
        or resolver_transport.get("H301_intersection_H3_order") != 81
    ):
        raise StrictDataError("G1 group/resolver transport cross-check mismatch")
    released_projection = g0["released_C59"]["released_object_projection"]
    if (
        released_projection.get("tom_subgroup_class_count") != 350
        or released_projection.get("distinct_permutation_character_profile_count") != 339
        or not deep_exact(released_projection.get("exact_collision_buckets"), EXPECTED_COLLISION_BUCKETS)
    ):
        raise StrictDataError("G1 released C59 exhaustive-scan projection mismatch")
    replay = group_evidence["independent_replay"]["python"]["direct_projection"]
    direct_replay = {
        "group_element_set_sha256": deepcopy(replay["group_element_set_sha256"]),
        "group_orders": deepcopy(replay["group_orders"]),
        "transport": deepcopy(replay["transport"]),
    }
    if (
        direct_replay["group_orders"].get("W") != 51840
        or direct_replay["group_orders"].get("N") != 324
        or direct_replay["group_orders"].get("J") != 81
        or direct_replay["transport"].get("equation_holds") is not True
        or direct_replay["transport"].get("equation_checked_pairs") != 8748
    ):
        raise StrictDataError("G1 independent direct group replay mismatch")
    return {
        "action": deepcopy(source["action"]),
        "common_intersection_J": deepcopy(intersection),
        "common_normalizer": deepcopy(common),
        "direct_group_replay": direct_replay,
        "durable_permutation_arrays": durable,
        "exhaustive_collision_scan": {
            "all_subgroup_classes": released_projection["tom_subgroup_class_count"],
            "distinct_permutation_character_profiles": released_projection[
                "distinct_permutation_character_profile_count"
            ],
            "exact_11_collision_buckets": deepcopy(scan["exact_11_collision_buckets"]),
            "predicate": "normalizers_conjugate_in_W AND normalizer_indices_over_subgroups=[2,2]",
            "qualifying_buckets": deepcopy(qualifying),
            "rows": deepcopy(scan["rows"]),
        },
        "index_two_subgroups": deepcopy(fields),
        "left_label_map_transport": {
            "H301_intersection_H3_order": resolver_transport["H301_intersection_H3_order"],
            "H3_contained_in_N": resolver_transport["H3_contained_in_N"],
            "Stab_xSminus_equals_H3": resolver_transport[
                "H3_equals_transported_support_stabilizer"
            ],
            "conjugating_permutation_inverse_one_based": deepcopy(
                transport["conjugating_permutation_inverse_one_based"]
            ),
            "conjugating_permutation_one_based": deepcopy(
                transport["conjugating_permutation_one_based"]
            ),
            "convention": resolver_transport["convention"],
            "right_action_equation": transport["right_action_equation"],
            "right_action_equation_checked_pairs": transport[
                "right_action_equation_checked_pairs"
            ],
            "right_action_equation_holds": transport["right_action_equation_holds"],
            "source_N303_generators_one_based": deepcopy(
                transport["source_N303_generators_one_based"]
            ),
            "transported_N303_generators_one_based": deepcopy(
                transport["transported_N303_generators_one_based"]
            ),
            "transported_normalizer_equals_N": transport["transported_normalizer_equals_N"],
        },
        "pairwise_lattice": {
            "generated_orders": deepcopy(tower["pairwise_generated_orders"]),
            "intersection_orders": deepcopy(tower["pairwise_intersection_orders"]),
            "intersections_equal_J": tower["pairwise_intersections_equal_J"],
        },
        "uniqueness_scope": {
            "broader_generated_V4_configuration_unique_claimed": False,
            "index_two_common_normalizer_case_unique": len(qualifying) == 1,
        },
    }


def derive_g2(
    resolver_payload: dict[str, Any],
    group_evidence: dict[str, Any],
    g0: dict[str, Any],
) -> dict[str, Any]:
    require_exact_keys(
        resolver_payload,
        {
            "authority", "carriers", "constants", "fixed_field_bridge", "groups",
            "invariant_degree_obstruction", "replay_contract", "scope", "status", "transport",
        },
        "resolver payload",
    )
    carriers = resolver_payload["carriers"]
    if set(carriers) != {"M", "F0", "L"}:
        raise StrictDataError("G2 carrier key set mismatch")
    expected = {
        "M": (160, 324, 2, 81, "0beb2791f4df4bb56214b6a35384517083f5909004219cc988b6de70f494d17c", "b8818888c1ceb83e05d2f2df045e9d6e418f1ea18a5f019d1398e4cd0a59ef6b"),
        "F0": (320, 162, 3, 27, "83f014bb3087708ad6e65c4f61bc92a73172aa649ef573358164c1ae7d9efbc5", "ffe9439cd390729bbb0dd7ffa4c6a1045c7fbc9c645e0f37e75c71d1e786e10d"),
        "L": (640, 81, 2, 135, "fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5", "c82feda40496156b7d006de4e47a1b808b3cf3ffffe4a386652d3e3fa77861f1"),
    }
    for name, target in expected.items():
        degree, stabilizer, monomial_degree, term_count, carrier_hash, coefficient_hash = target
        row = carriers[name]
        if (
            row.get("orbit_size") != degree
            or row.get("stabilizer_order") != stabilizer
            or row.get("stabilizer_equals_expected") is not True
            or row.get("monomial_degree") != monomial_degree
            or row.get("nonzero_monomial_count") != term_count
            or row.get("carrier_sha256") != carrier_hash
            or row.get("carrier_sha256") != sha256_bytes(canonical_leaf_bytes(row.get("carrier")))
            or row.get("modular_polynomial", {}).get("value_count") != degree
            or row.get("modular_polynomial", {}).get("distinct_value_count") != degree
            or row.get("modular_polynomial", {}).get("coefficient_count") != degree + 1
            or row.get("modular_polynomial", {}).get("coefficient_sha256") != coefficient_hash
        ):
            raise StrictDataError(f"G2 primitive carrier mismatch: {name}")
    constants = resolver_payload["constants"]
    if (
        constants.get("degree") != 27
        or constants.get("w_order") != 51840
        or constants.get("prime") != 692717
        or constants.get("scope_literal") != "NO_BAD_EULER_OR_ROOT_NUMBER"
        or constants.get("expected_orbit_degrees") != {"M": 160, "F0": 320, "L": 640}
    ):
        raise StrictDataError("G2 primitive constants mismatch")
    bridge = resolver_payload["fixed_field_bridge"]
    if (
        bridge.get("c59_factor_degrees") != [[1, 27]]
        or bridge.get("c59_split_roots_distinct") is not True
        or bridge.get("c59_label_map_is_graph_isomorphism") is not True
        or bridge.get("c59_all_27_line_equations_zero") is not True
        or bridge.get("labelled_W_action_faithful") is not True
        or bridge.get("K_completely_split_witness") is not True
        or bridge.get("prime_unramified") is not True
        or bridge.get("characteristic_zero_orbit_values_distinct") is not True
        or bridge.get("modular_distinct_value_counts") != {"M": 160, "F0": 320, "L": 640}
        or bridge.get("support_stabilizers_exact_on_Z_labelled_carrier") != {"M": True, "F0": True, "L": True}
        or bridge.get("fixed_field_identities")
        != {"M": "Q(mu)=K^N", "F0": "Q(xi0)=K^H0", "L": "Q(lambda)=K^J"}
    ):
        raise StrictDataError("G2 fixed-field bridge mismatch")
    transport = resolver_payload["transport"]
    if (
        transport.get("convention")
        != "left label-map action: Stab(x*Sminus)=x*Hminus*x^-1=GAP(Hminus^x)"
        or transport.get("label_permutation_one_based") != list(TRANSPORT_X_ONE_BASED)
        or transport.get("H3_equals_transported_support_stabilizer") is not True
        or transport.get("H3_contained_in_N") is not True
        or transport.get("H301_intersection_H3_order") != 81
    ):
        raise StrictDataError("G2 transported support/stabilizer mismatch")
    authority = resolver_payload["authority"]
    require_exact_keys(
        authority,
        {
            "c59_full_manifest_entry_count", "c59_full_manifest_sha256",
            "c59_implementation_commit", "c59_release_commit",
            "c59_resolvent_evidence_sha256", "c59_resolvent_module_sha256",
            "c59_resolvent_payload_sha256", "c59_route_archive_sha256",
            "c59_route_sha256", "c60_durable_carrier_literals_sha256",
            "c60_durable_group_literals_sha256", "released_c59_rebound",
        },
        "G2 resolver authority",
    )
    released = g0["released_C59"]
    if (
        authority["c59_full_manifest_entry_count"]
        != released["full_manifest"]["entry_count"]
        or authority["c59_full_manifest_sha256"]
        != released["full_manifest"]["manifest_sha256"]
        or authority["c59_implementation_commit"] != released["implementation_commit"]
        or authority["c59_release_commit"] != released["release_commit"]
        or authority["c59_route_sha256"] != released["live_route"]["sha256"]
        or authority["c59_route_archive_sha256"] != released["archive_route"]["sha256"]
        or authority["c59_resolvent_evidence_sha256"]
        != released["resolver_evidence"]["sha256"]
        or authority["c59_resolvent_module_sha256"] != C59_LOCK["resolvent_module_sha256"]
        or authority["released_c59_rebound"] is not True
    ):
        raise StrictDataError("G2 resolver authority does not rebound G0")
    direct = group_evidence["independent_replay"]["python"]["direct_projection"]
    w_hash = direct["group_element_set_sha256"]["W"]
    if direct["group_orders"]["W"] != 51840 or not isinstance(w_hash, str):
        raise StrictDataError("G2 direct faithful-action witness mismatch")
    component_authority = {
        key: deepcopy(authority[key])
        for key in (
            "c59_full_manifest_sha256", "c59_implementation_commit",
            "c59_release_commit", "c59_resolvent_evidence_sha256",
            "c59_resolvent_module_sha256", "c59_resolvent_payload_sha256",
            "c59_route_archive_sha256", "c59_route_sha256",
            "c60_durable_carrier_literals_sha256",
            "c60_durable_group_literals_sha256", "released_c59_rebound",
        )
    }
    return {
        "carriers": deepcopy(carriers),
        "complete_split_witness": {
            "K_completely_split": bridge["K_completely_split_witness"],
            "all_27_line_equations_zero": bridge["c59_all_27_line_equations_zero"],
            "all_27_roots_distinct": bridge["c59_split_roots_distinct"],
            "factor_degrees": deepcopy(bridge["c59_factor_degrees"]),
            "label_map_is_graph_isomorphism": bridge[
                "c59_label_map_is_graph_isomorphism"
            ],
            "prime": constants["prime"],
            "prime_unramified": bridge["prime_unramified"],
        },
        "component_authority_rebound": component_authority,
        "constants": deepcopy(constants),
        "fixed_field_generation_premises": {
            "identities": deepcopy(bridge["fixed_field_identities"]),
            "reason": bridge["fixed_field_reason"],
        },
        "group_carrier_hashes": deepcopy(resolver_payload["groups"]),
        "labelled_W_action_faithfulness": {
            "carrier_degree": constants["degree"],
            "derived_before_split_implication": True,
            "distinct_labelled_permutation_count": direct["group_orders"]["W"],
            "faithful": bridge["labelled_W_action_faithful"],
            "group_element_set_sha256": w_hash,
        },
        "left_transport_support_certificate": {
            "H301_intersection_H3_order": transport["H301_intersection_H3_order"],
            "H3_contained_in_N": transport["H3_contained_in_N"],
            "H3_order": transport["H3_order"],
            "Stab_xSminus_equals_H3": transport[
                "H3_equals_transported_support_stabilizer"
            ],
            "convention": transport["convention"],
            "label_permutation_one_based": deepcopy(
                transport["label_permutation_one_based"]
            ),
            "transported_support_stabilizer_order": transport[
                "transported_support_stabilizer_order"
            ],
        },
        "orbit_value_noncollision": {
            "characteristic_zero_orbit_values_distinct": bridge[
                "characteristic_zero_orbit_values_distinct"
            ],
            "modular_distinct_value_counts": deepcopy(
                bridge["modular_distinct_value_counts"]
            ),
            "support_stabilizers_exact_on_Z_labelled_carrier": deepcopy(
                bridge["support_stabilizers_exact_on_Z_labelled_carrier"]
            ),
        },
    }


def derive_g3(group_evidence: dict[str, Any], resolver_payload: dict[str, Any]) -> dict[str, Any]:
    group_gate = group_evidence["G3_orbit_partition_obstruction"]
    field_order = group_gate["field_order"]
    if field_order != ["N", "H301", "H302", "H303", "J"]:
        raise StrictDataError("G3 coefficient partition field order mismatch")
    index_n = field_order.index("N")
    index_h0 = field_order.index("H302")
    h0_group = generated_permutation_group(H0_GENERATORS_ONE_BASED)
    n_group = generated_permutation_group(N_GENERATORS_ONE_BASED)
    if len(h0_group) != 162 or len(n_group) != 324:
        raise StrictDataError("G3 independently generated H0/N order mismatch")
    local_points_h0 = canonical_point_partition(h0_group)
    local_points_n = canonical_point_partition(n_group)
    local_pairs_h0 = canonical_pair_partition(h0_group)
    local_pairs_n = canonical_pair_partition(n_group)
    external_points_h0 = normalize_external_point_partition(group_gate["point_partitions"][index_h0])
    external_points_n = normalize_external_point_partition(group_gate["point_partitions"][index_n])
    external_pairs_h0 = normalize_external_pair_partition(group_gate["pair_partitions"][index_h0])
    external_pairs_n = normalize_external_pair_partition(group_gate["pair_partitions"][index_n])
    if not (
        deep_exact(local_points_h0, local_points_n)
        and deep_exact(local_points_h0, external_points_h0)
        and deep_exact(local_points_n, external_points_n)
        and deep_exact(local_pairs_h0, local_pairs_n)
        and deep_exact(local_pairs_h0, external_pairs_h0)
        and deep_exact(local_pairs_n, external_pairs_n)
        and group_gate["H302_point_partition_equals_N"] is True
        and group_gate["H302_pair_partition_equals_N"] is True
    ):
        raise StrictDataError("G3 actual H0/N point/pair partitions do not deep-compare")
    obstruction = resolver_payload["invariant_degree_obstruction"]
    if (
        obstruction.get("H0_and_N_point_partitions_equal") is not True
        or obstruction.get("H0_and_N_unordered_pair_partitions_equal") is not True
        or obstruction.get("H0_point_orbit_sizes") != [27]
        or obstruction.get("H0_pair_orbit_sizes") != [27, 27, 54, 81, 162]
        or obstruction.get("H0_point_partition_sha256") != sha256_bytes(canonical_leaf_bytes(local_points_h0))
        or obstruction.get("H0_pair_partition_sha256") != sha256_bytes(canonical_leaf_bytes(local_pairs_h0))
        or obstruction.get("selected_cubic_orbit_size") != 27
        or obstruction.get("selected_cubic_support_sha256")
        != resolver_payload["carriers"]["F0"]["carrier_sha256"]
        or obstruction.get("formal_polynomial_scope")
        != "commutative Q-coefficient formal polynomials in 27 independent labelled variables"
    ):
        raise StrictDataError("G3 resolver obstruction differs from actual partitions")
    frozen = group_evidence["frozen_permutation_arrays"]["arrays"]
    resolver_groups = resolver_payload["groups"]
    array_cross = {
        "H0_group_array_equals_resolver_checker_literal": frozen["H302_generators"] == H0_GENERATORS_ONE_BASED,
        "N_group_array_equals_resolver_checker_literal": frozen["N_generators"] == N_GENERATORS_ONE_BASED,
        "J_group_array_equals_resolver_checker_literal": frozen["J_generators"] == J_GENERATORS_ONE_BASED,
        "transport_array_equals_resolver_checker_literal": frozen["normalizer_conjugator"] == TRANSPORT_X_ONE_BASED,
        "H0_array_hash_equals_resolver_evidence": resolver_groups["H0_generators_sha256"] == sha256_bytes(canonical_leaf_bytes(H0_GENERATORS_ONE_BASED)),
        "N_array_hash_equals_resolver_evidence": resolver_groups["N_generators_sha256"] == sha256_bytes(canonical_leaf_bytes(N_GENERATORS_ONE_BASED)),
        "J_array_hash_equals_resolver_evidence": resolver_groups["J_generators_sha256"] == sha256_bytes(canonical_leaf_bytes(J_GENERATORS_ONE_BASED)),
    }
    if any(value is not True for value in array_cross.values()):
        raise StrictDataError("G3 H0/N/J/transport arrays fail cross-carrier deep comparison")
    raw_points_h0 = group_gate["point_partitions"][index_h0]
    raw_points_n = group_gate["point_partitions"][index_n]
    raw_pairs_h0 = group_gate["pair_partitions"][index_h0]
    raw_pairs_n = group_gate["pair_partitions"][index_n]
    direct = group_evidence["independent_replay"]["python"]["direct_projection"]
    point_hashes = {
        "H0": sha256_bytes(canonical_leaf_bytes(raw_points_h0)),
        "N": sha256_bytes(canonical_leaf_bytes(raw_points_n)),
    }
    pair_hashes = {
        "H0": sha256_bytes(canonical_leaf_bytes(raw_pairs_h0)),
        "N": sha256_bytes(canonical_leaf_bytes(raw_pairs_n)),
    }
    if (
        point_hashes["H0"] != direct["point_partition_sha256"]["H302"]
        or point_hashes["N"] != direct["point_partition_sha256"]["N"]
        or pair_hashes["H0"] != direct["pair_partition_sha256"]["H302"]
        or pair_hashes["N"] != direct["pair_partition_sha256"]["N"]
    ):
        raise StrictDataError("G3 independently recomputed one-based partition hashes differ")
    zero_point_hash = sha256_bytes(canonical_leaf_bytes(local_points_h0))
    zero_pair_hash = sha256_bytes(canonical_leaf_bytes(local_pairs_h0))
    if (
        zero_point_hash != obstruction["H0_point_partition_sha256"]
        or zero_pair_hash != obstruction["H0_pair_partition_sha256"]
    ):
        raise StrictDataError("G3 independently recomputed zero-based partition hashes differ")
    f0 = resolver_payload["carriers"]["F0"]
    return {
        "actual_one_based_partitions": {
            "H0_and_N_point_partitions_deep_equal": deep_exact(
                raw_points_h0, raw_points_n
            ),
            "H0_and_N_unordered_pair_partitions_deep_equal": deep_exact(
                raw_pairs_h0, raw_pairs_n
            ),
            "H0_point_partition": deepcopy(raw_points_h0),
            "H0_unordered_pair_partition": deepcopy(raw_pairs_h0),
            "N_point_partition": deepcopy(raw_points_n),
            "N_unordered_pair_partition": deepcopy(raw_pairs_n),
        },
        "canonical_zero_based_partitions": {
            "H0_point_partition": deepcopy(local_points_h0),
            "H0_unordered_pair_partition": deepcopy(local_pairs_h0),
            "N_point_partition": deepcopy(local_points_n),
            "N_unordered_pair_partition": deepcopy(local_pairs_n),
            "indexing_conversion": "one_based_labels_to_zero_based_labels",
            "partition_sort": "(orbit_size,orbit_members)",
        },
        "degree_at_most_two_coefficient_orbits": {
            "constant_basis_covered": True,
            "formal_polynomial_scope": obstruction["formal_polynomial_scope"],
            "linear_Xi_basis_covered_by_point_partition": True,
            "mixed_XiXj_basis_covered_by_unordered_pair_partition": True,
            "quotient_by_root_relations_claimed": False,
            "square_Xi2_basis_covered_by_point_partition": True,
        },
        "exact_cubic_escape": {
            "carrier": deepcopy(f0["carrier"]),
            "carrier_sha256": f0["carrier_sha256"],
            "monomial_degree": f0["monomial_degree"],
            "nonzero_monomial_count": f0["nonzero_monomial_count"],
            "selected_cubic_orbit_size": obstruction["selected_cubic_orbit_size"],
            "stabilizer_equals_H0": f0["stabilizer_equals_expected"],
            "stabilizer_order": f0["stabilizer_order"],
        },
        "field_order": deepcopy(field_order),
        "partition_hash_cross_check": {
            "group_one_based_pair_sha256": pair_hashes,
            "group_one_based_point_sha256": point_hashes,
            "resolver_zero_based_pair_sha256": obstruction[
                "H0_pair_partition_sha256"
            ],
            "resolver_zero_based_point_sha256": obstruction[
                "H0_point_partition_sha256"
            ],
            "zero_based_pair_hash_reconstructed": zero_pair_hash,
            "zero_based_point_hash_reconstructed": zero_point_hash,
        },
        "transported_source_normalizer_partitions": {
            "pair_partition_equals_N": group_gate[
                "transported_N303_pair_partition_equals_N"
            ],
            "point_partition": deepcopy(group_gate["transported_N303_point_partition"]),
            "point_partition_equals_N": group_gate[
                "transported_N303_point_partition_equals_N"
            ],
            "unordered_pair_partition": deepcopy(
                group_gate["transported_N303_pair_partition"]
            ),
        },
    }


def derive_g4(
    group_evidence: dict[str, Any],
    resolver_payload: dict[str, Any],
) -> dict[str, Any]:
    source = group_evidence["G4_biquadratic_tower_characters"]
    relation = source["character_relation"]
    vectors = relation.get("vectors")
    if type(vectors) is not dict or set(vectors) != {"H301", "H302", "H303", "J", "N"}:
        raise StrictDataError("G4 character vector key set mismatch")
    if (
        relation.get("class_count") != 25
        or len(relation.get("class_sizes", [])) != 25
        or sum(relation["class_sizes"]) != 51840
        or relation.get("coefficient_order_H301_H302_H303_J_N") != [-1, -1, -1, 1, 2]
        or relation.get("relation_zero_on_every_class") is not True
        or relation.get("H301_equals_H303") is not True
        or relation.get("H301_equals_H302") is not False
    ):
        raise StrictDataError("G4 character relation summary mismatch")
    for index in range(25):
        value = (
            -vectors["H301"][index]
            - vectors["H302"][index]
            - vectors["H303"][index]
            + vectors["J"][index]
            + 2 * vectors["N"][index]
        )
        if value != 0:
            raise StrictDataError("G4 rational Brauer relation fails on a class")
    fields = source["fields"]
    intersection = source["intersection"]
    if (
        source["pairwise_generated_orders"] != [324, 324, 324]
        or source["pairwise_intersection_orders"] != [81, 81, 81]
        or source["pairwise_intersections_equal_J"] is not True
        or any(row.get("core_order_in_W") != 1 for row in fields)
        or intersection.get("core_order_in_W") != 1
        or intersection.get("normalizer_order_in_W") != 324
    ):
        raise StrictDataError("G4 V4/core/normalizer input mismatch")
    by_label = {row["label"]: row for row in fields}
    if set(by_label) != {"H301", "H302", "H303"}:
        raise StrictDataError("G4 index-two subgroup labels differ")
    common = group_evidence["G1_common_normalizer_uniqueness"]["common_normalizer"]
    if common["order"] != 324 or common["quotient_by_J_id_group"] != [4, 2]:
        raise StrictDataError("G4 common-normalizer quotient mismatch")
    bridge = resolver_payload["fixed_field_bridge"]
    if (
        bridge["K_completely_split_witness"] is not True
        or bridge["characteristic_zero_orbit_values_distinct"] is not True
        or bridge["labelled_W_action_faithful"] is not True
    ):
        raise StrictDataError("G4 primitive fixed-field premises differ")
    field_lattice = {
        "F0": {
            "contained_in": ["L"], "contains": ["M"],
            "degree": by_label["H302"]["field_degree"], "fixed_group": "H302",
        },
        "F3": {
            "contained_in": ["L"], "contains": ["M"],
            "degree": by_label["H303"]["field_degree"], "fixed_group": "H303",
        },
        "Fplus": {
            "contained_in": ["L"], "contains": ["M"],
            "degree": by_label["H301"]["field_degree"], "fixed_group": "H301",
        },
        "L": {
            "contained_in": ["K"], "contains": ["M", "Fplus", "F0", "F3"],
            "degree": intersection["index_in_W"], "fixed_group": "J",
        },
        "M": {
            "contained_in": ["Fplus", "F0", "F3", "L"], "contains": ["Q"],
            "degree": common["index_in_W"], "fixed_group": "N",
        },
        "index_two_subgroup_records": deepcopy(fields),
        "pairwise_generated_orders": deepcopy(source["pairwise_generated_orders"]),
        "pairwise_intersection_orders": deepcopy(source["pairwise_intersection_orders"]),
        "pairwise_intersections_equal_J": source["pairwise_intersections_equal_J"],
    }
    normal_closures = {
        "F0": {"core_order": by_label["H302"]["core_order_in_W"], "normal_closure": "K"},
        "F3": {"core_order": by_label["H303"]["core_order_in_W"], "normal_closure": "K"},
        "Fplus": {"core_order": by_label["H301"]["core_order_in_W"], "normal_closure": "K"},
        "L": {"core_order": intersection["core_order_in_W"], "normal_closure": "K"},
        "M": {"core_order": common["core_order_in_W"], "normal_closure": "K"},
        "normal_closure_degree": sum(source["character_relation"]["class_sizes"]),
    }
    if normal_closures["normal_closure_degree"] != 51840:
        raise StrictDataError("G4 normal-closure degree mismatch")
    automorphisms = {
        "F0_over_Q": {"group": "C2", "normalizer_quotient_order": 324 // by_label["H302"]["order"]},
        "F3_over_Q": {"group": "C2", "normalizer_quotient_order": 324 // by_label["H303"]["order"]},
        "Fplus_over_Q": {"group": "C2", "normalizer_quotient_order": 324 // by_label["H301"]["order"]},
        "L_over_M": {"degree": common["order"] // intersection["order"], "group": "V4", "id_group": deepcopy(common["quotient_by_J_id_group"])},
        "L_over_Q": {"group": "V4", "id_group": deepcopy(common["quotient_by_J_id_group"]), "normalizer_quotient_order": intersection["normalizer_order_in_W"] // intersection["order"]},
        "M_over_Q": {"group": "trivial", "normalizer_quotient_order": common["normalizer_order_in_W"] // common["order"]},
    }
    return {
        "automorphism_groups": automorphisms,
        "complete_permutation_characters": deepcopy(relation),
        "field_lattice": field_lattice,
        "normal_closures": normal_closures,
        "primitive_fixed_field_bridge": {
            "K_completely_split_witness": bridge["K_completely_split_witness"],
            "characteristic_zero_orbit_values_distinct": bridge[
                "characteristic_zero_orbit_values_distinct"
            ],
            "identities": deepcopy(bridge["fixed_field_identities"]),
            "labelled_W_action_faithful": bridge["labelled_W_action_faithful"],
            "reason": bridge["fixed_field_reason"],
        },
        "rational_V4_Brauer_relation": {
            "coefficient_order_H301_H302_H303_J_N": deepcopy(
                relation["coefficient_order_H301_H302_H303_J_N"]
            ),
            "formula": "[G/J]+2[G/N]=[G/H301]+[G/H302]+[G/H303]",
            "zero_on_all_25_classes": relation["relation_zero_on_every_class"],
        },
        "zeta_written_bridge": {
            "Artin_formalism_is_written_step": True,
            "Hplus_H0_character_equality": relation["H301_equals_H302"],
            "Hplus_H3_character_equality": relation["H301_equals_H303"],
            "bad_Artin_Euler_inference_claimed": False,
            "finite_G_set_isomorphism_claimed": False,
            "first_identity_target": "zeta_L*zeta_M^2=zeta_Fplus*zeta_F0*zeta_F3",
            "second_identity_target": "zeta_L*zeta_M^2=zeta_Fplus^2*zeta_F0",
        },
    }


def validate_g5(gate: dict[str, Any]) -> None:
    require_exact_keys(gate, {"global_arithmetic", "relative_discriminants_over_N"}, "G5")
    global_value = gate["global_arithmetic"]
    if global_value.get("exact_prime_support") != EXACT_PRIME_SUPPORT:
        raise StrictDataError("G5 exact prime support mismatch")
    expected = {
        "N": (160, [22, 28, 56, 8, 32, 64, 80, 88], [308, 248, 96, 80], [16, 72]),
        "H301": (320, [36, 56, 112, 16, 64, 128, 160, 168], [624, 496, 192, 160], [16, 152]),
        "H302": (320, [28, 56, 112, 16, 64, 128, 160, 160], [632, 496, 192, 160], [0, 160]),
        "H303": (320, [36, 56, 112, 16, 64, 128, 160, 168], [624, 496, 192, 160], [16, 152]),
        "J": (640, [56, 112, 224, 32, 128, 256, 320, 320], [1264, 992, 384, 320], [0, 320]),
    }
    rows = global_value.get("fields")
    if type(rows) is not list or len(rows) != 5:
        raise StrictDataError("G5 field row count mismatch")
    exponents_by_field = {}
    for row in rows:
        label = row.get("field") if type(row) is dict else None
        if label not in expected or label in exponents_by_field:
            raise StrictDataError("G5 field label mismatch")
        degree, counts, exponents, signature = expected[label]
        i3, p3, q3, i5, p5, c3, c2, cinf = counts
        replay_exponents = [
            (degree - i3) + (degree - p3) // 2 + (degree - q3),
            (degree - i5) + 3 * (degree - p5) // 4,
            degree - c3,
            degree - c2,
        ]
        replay_signature = [2 * cinf - degree, degree - cinf]
        factorization = [
            [3, exponents[0]], [5, exponents[1]],
            [181, exponents[2]], [283, exponents[3]],
            [997, exponents[2]], [1801, exponents[3]],
            [2346241, exponents[2]], [LARGE_PRIME, exponents[3]],
        ]
        if (
            row.get("degree") != degree
            or row.get("orbit_counts_I3_P3_Q3_I5_P5_C3_C2_Cinf") != counts
            or replay_exponents != exponents
            or row.get("conductor_exponents_p3_p5_A_B") != exponents
            or replay_signature != signature
            or row.get("signature_r1_r2") != signature
            or row.get("discriminant_positive") is not True
            or row.get("discriminant_factorization") != factorization
        ):
            raise StrictDataError(f"G5 conductor/signature/discriminant formula mismatch: {label}")
        exponents_by_field[label] = exponents
    relative_expected = {
        "H301": (2, [8, 0, 0, 0]),
        "H302": (2, [16, 0, 0, 0]),
        "H303": (2, [8, 0, 0, 0]),
        "J": (4, [32, 0, 0, 0]),
    }
    relative = gate["relative_discriminants_over_N"]
    if type(relative) is not list or len(relative) != 4:
        raise StrictDataError("G5 relative discriminant row count mismatch")
    for row in relative:
        label = row.get("field") if type(row) is dict else None
        if label not in relative_expected:
            raise StrictDataError("G5 relative discriminant field mismatch")
        degree, exponents = relative_expected[label]
        replay = [
            exponents_by_field[label][index] - degree * exponents_by_field["N"][index]
            for index in range(4)
        ]
        if (
            row.get("relative_degree_over_N") != degree
            or row.get("relative_discriminant_exponents_p3_p5_A_B") != exponents
            or replay != exponents
        ):
            raise StrictDataError(f"G5 relative discriminant tower formula mismatch: {label}")


def derive_g5(group_evidence: dict[str, Any]) -> dict[str, Any]:
    gate = group_evidence["G5_global_relative_discriminants"]
    validate_g5(gate)
    global_value = gate["global_arithmetic"]
    replay = group_evidence["independent_replay"]["python"]["direct_projection"]
    replay_hashes = replay["discriminants"]
    recomputed_hashes: dict[str, Any] = {}
    for row in global_value["fields"]:
        label = row["field"]
        factorization = row["discriminant_factorization"]
        discriminant = 1
        for prime, exponent in factorization:
            discriminant *= prime ** exponent
        decimal = str(discriminant).encode("ascii")
        recomputed = {
            "decimal_no_newline_digits": len(decimal),
            "decimal_no_newline_sha256": sha256_bytes(decimal),
            "factorization_sha256": sha256_bytes(canonical_leaf_bytes(factorization)),
            "positive": discriminant > 0,
        }
        if not deep_exact(recomputed, replay_hashes[label]):
            raise StrictDataError(
                f"G5 independent decimal/factorization hash mismatch: {label}"
            )
        recomputed_hashes[label] = recomputed
    relative = gate["relative_discriminants_over_N"]
    relative_exponents = [row["relative_discriminant_exponents_p3_p5_A_B"][0] for row in relative]
    if relative_exponents != [8, 16, 8, 32]:
        raise StrictDataError("G5 relative norm exponents differ")
    relative_output = []
    for row, exponent in zip(relative, relative_exponents):
        output_row = deepcopy(row)
        output_row["relative_discriminant_norm"] = f"3^{exponent}"
        relative_output.append(output_row)
    return {
        "absolute_fields": deepcopy(global_value["fields"]),
        "discriminant_authority": (
            "PERMUTATION_CONDUCTOR_AND_FIELD_DISCRIMINANT_NOT_"
            "DEFINING_POLYNOMIAL_DISCRIMINANT"
        ),
        "exact_absolute_prime_support": deepcopy(global_value["exact_prime_support"]),
        "filtration_group_tom_order_I3_P3_Q3_I5_P5_C3_C2_Cinf": deepcopy(
            global_value[
                "local_subgroup_tom_order_I3_P3_Q3_I5_P5_C3_C2_Cinf"
            ]
        ),
        "independent_decimal_and_factorization_hashes": recomputed_hashes,
        "relative_discriminants_over_M": relative_output,
        "relative_norm_product_relation": {
            "identity": f"3^({relative_exponents[0]}+{relative_exponents[1]}+{relative_exponents[2]})=3^{relative_exponents[3]}",
            "left_exponents": relative_exponents[:3],
            "right_exponent": relative_exponents[3],
            "verified": sum(relative_exponents[:3]) == relative_exponents[3],
        },
    }


def collected_rows(expanded: list[Any]) -> list[Any]:
    result: list[Any] = []
    for row in expanded:
        if result and deep_exact(result[-1][0], row):
            result[-1][1] += 1
        else:
            result.append([deepcopy(row), 1])
    return result


def validate_g6(gate: dict[str, Any]) -> None:
    require_exact_keys(gate, {"relative_field_order", "tom140", "tom206"}, "G6")
    if gate["relative_field_order"] != ["H301", "H302", "H303", "J"]:
        raise StrictDataError("G6 relative field order mismatch")
    relative_degrees = [2, 2, 2, 4]
    expected_factor_totals = {"tom140": [36, 28, 36, 56], "tom206": [18, 14, 18, 28]}
    expected_locators = {"tom140": 140, "tom206": 206}
    for branch in ("tom140", "tom206"):
        value = gate[branch]
        require_exact_keys(value, {"absolute_tables", "decomposition_tom_locator", "relative_tower_over_N"}, f"G6 {branch}")
        if value["decomposition_tom_locator"] != expected_locators[branch]:
            raise StrictDataError(f"G6 {branch} ToM locator mismatch")
        tables = value["absolute_tables"]
        if type(tables) is not list or [row.get("field") for row in tables] != ["N", "H301", "H302", "H303", "J"]:
            raise StrictDataError(f"G6 {branch} absolute table field order mismatch")
        by_field = {}
        for field_row in tables:
            table = field_row.get("table")
            require_exact_keys(
                table,
                {"degree_total", "different_total", "factor_count", "rows_n_e_f_d_with_multiplicity"},
                f"G6 {branch} absolute table",
            )
            rows = table["rows_n_e_f_d_with_multiplicity"]
            if type(rows) is not list or not rows:
                raise StrictDataError(f"G6 {branch} empty absolute table")
            factor_count = degree_total = different_total = 0
            expanded = []
            for row, multiplicity in rows:
                if (
                    type(row) is not list or len(row) != 4
                    or any(type(item) is not int or item < 0 for item in row)
                    or type(multiplicity) is not int or multiplicity <= 0
                ):
                    raise StrictDataError(f"G6 {branch} absolute row type mismatch")
                n, e, f, d = row
                if n != e * f:
                    raise StrictDataError(f"G6 {branch} absolute n=e*f mismatch")
                factor_count += multiplicity
                degree_total += n * multiplicity
                different_total += f * d * multiplicity
                expanded.extend([row] * multiplicity)
            if (
                table["factor_count"] != factor_count
                or table["degree_total"] != degree_total
                or table["different_total"] != different_total
            ):
                raise StrictDataError(f"G6 {branch} absolute totals mismatch")
            by_field[field_row["field"]] = expanded
        relative = value["relative_tower_over_N"]
        require_exact_keys(
            relative,
            {
                "base_prime_count",
                "collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J",
                "relative_factor_counts_H301_H302_H303_J",
                "rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J",
            },
            f"G6 {branch} relative tower",
        )
        expanded = relative["rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J"]
        if type(expanded) is not list or len(expanded) != relative["base_prime_count"]:
            raise StrictDataError(f"G6 {branch} base-prime count mismatch")
        if not deep_exact(collected_rows(expanded), relative["collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J"]):
            raise StrictDataError(f"G6 {branch} collected/expanded rows mismatch")
        factor_totals = [0, 0, 0, 0]
        derived_absolute = {label: [] for label in ["H301", "H302", "H303", "J"]}
        for row in expanded:
            if type(row) is not list or len(row) != 2:
                raise StrictDataError(f"G6 {branch} relative row shape mismatch")
            base, extensions = row
            if type(base) is not list or len(base) != 4 or type(extensions) is not list or len(extensions) != 4:
                raise StrictDataError(f"G6 {branch} relative row arity mismatch")
            n0, e0, f0, d0 = base
            for index, extension in enumerate(extensions):
                if type(extension) is not list or len(extension) != 4 or any(type(item) is not int for item in extension):
                    raise StrictDataError(f"G6 {branch} relative extension type mismatch")
                g, e, f, d = extension
                if g <= 0 or e <= 0 or f <= 0 or d < 0 or g * e * f != relative_degrees[index]:
                    raise StrictDataError(f"G6 {branch} relative degree formula mismatch")
                if e > 1 and (e != 2 or d != 1):
                    raise StrictDataError(f"G6 {branch} relative ramification is not tame e=2,d=1")
                factor_totals[index] += g
                absolute_row = [n0 * e * f, e0 * e, f0 * f, e * d0 + d]
                derived_absolute[gate["relative_field_order"][index]].extend([absolute_row] * g)
        if (
            factor_totals != expected_factor_totals[branch]
            or relative["relative_factor_counts_H301_H302_H303_J"] != factor_totals
        ):
            raise StrictDataError(f"G6 {branch} relative factor totals mismatch")
        for field, derived in derived_absolute.items():
            if sorted(derived) != sorted(by_field[field]):
                raise StrictDataError(f"G6 {branch} local tower formula mismatch: {field}")


def derive_g6(group_evidence: dict[str, Any]) -> dict[str, Any]:
    gate = group_evidence["G6_two_local_branches"]
    validate_g6(gate)
    source_order = deepcopy(gate["relative_field_order"])
    if source_order != ["H301", "H302", "H303", "J"]:
        raise StrictDataError("G6 source field order differs")
    branches: dict[str, Any] = {}
    branch_exponents: list[list[int]] = []
    all_tame = True
    for branch in ("tom140", "tom206"):
        source = gate[branch]
        relative = source["relative_tower_over_N"]
        exponents = [0, 0, 0, 0]
        branch_tame = True
        rows = relative[
            "rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J"
        ]
        for base, extensions in rows:
            _, _, base_f, _ = base
            for index, extension in enumerate(extensions):
                multiplicity, ramification, residue_degree, different = extension
                exponents[index] += (
                    base_f * multiplicity * residue_degree * different
                )
                if ramification > 1 and (ramification != 2 or different != 1):
                    branch_tame = False
        if exponents != [8, 16, 8, 32] or not branch_tame:
            raise StrictDataError(f"G6 {branch} relative norm/tameness mismatch")
        branch_exponents.append(exponents)
        all_tame = all_tame and branch_tame
        branches[branch] = {
            "absolute_tables": deepcopy(source["absolute_tables"]),
            "decomposition_tom_locator": source["decomposition_tom_locator"],
            "relative_tower_over_M": {
                "all_relative_ramified_rows_have_e2_d1": branch_tame,
                "base_prime_count": relative["base_prime_count"],
                "collected_rows_with_multiplicity": deepcopy(
                    relative[
                        "collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J"
                    ]
                ),
                "relative_discriminant_norm_exponents_Fplus_F0_F3_L": exponents,
                "relative_factor_counts_Fplus_F0_F3_L": deepcopy(
                    relative["relative_factor_counts_H301_H302_H303_J"]
                ),
                "rows_base_n_e_f_d_then_relative_g_e_f_d_Fplus_F0_F3_L": deepcopy(
                    rows
                ),
            },
        }
    direct_hashes = group_evidence["independent_replay"]["python"][
        "direct_projection"
    ]["local_tower_sha256"]
    return {
        "all_relative_ramified_rows_have_e2_d1": all_tame,
        "both_branches_reconcile_relative_norm_exponents": branch_exponents[0]
        if branch_exponents[0] == branch_exponents[1]
        else [],
        "d3_branch_selected": False,
        "independent_source_tower_sha256": deepcopy(direct_hashes),
        "local_fields_classified_by_nefd_rows": False,
        "relative_field_order": ["Fplus", "F0", "F3", "L"],
        "source_group_field_order": source_order,
        **branches,
    }


def artifact_contract(
    group_path: Path,
    group_raw: bytes,
    group_document: dict[str, Any],
    resolver_path: Path,
    resolver_raw: bytes,
    resolver_document: dict[str, Any],
) -> dict[str, Any]:
    if group_path.name != ARTIFACT_NAMES[0] or resolver_path.name != ARTIFACT_NAMES[1]:
        raise StrictDataError("C60 artifact basename mismatch")
    if (
        sha256_bytes(group_raw) != GROUP_LOCK["evidence_sha256"]
        or len(group_raw) != GROUP_LOCK["evidence_size_bytes"]
        or sha256_bytes(resolver_raw) != RESOLVER_LOCK["evidence_sha256"]
        or len(resolver_raw) != RESOLVER_LOCK["evidence_size_bytes"]
    ):
        raise StrictDataError("C60 final component evidence bytes differ")
    rows = [
        {
            "path": "results/c60_group_evidence.json",
            "format": "canonical_compact_json",
            "sha256": sha256_bytes(group_raw),
            "size_bytes": len(group_raw),
            "schema_id": GROUP_EVIDENCE_SCHEMA_ID,
            "internal_report_sha256": group_document["independent_replay"]["gap_checker"]["checker_projection_sha256"],
            "component_aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
        },
        {
            "path": "results/c60_resolvent_evidence.json",
            "format": "canonical_compact_json",
            "sha256": sha256_bytes(resolver_raw),
            "size_bytes": len(resolver_raw),
            "schema_id": RESOLVER_EVIDENCE_SCHEMA_ID,
            "internal_report_sha256": resolver_document["payload_sha256"],
            "schema_descriptor_sha256": resolver_document["schema_sha256"],
            "component_aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
        },
    ]
    return {
        "artifact_count": 2,
        "artifacts": rows,
        "component_contracts": {
            "group": deepcopy(GROUP_COMPONENT_CONTRACT),
            "primitive_resolvent": deepcopy(RESOLVER_COMPONENT_CONTRACT),
        },
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c60-artifact-contract-v1",
        "source_owned_full_document_validation": True,
    }


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(child) for child in value)
    if value is None or type(value) in (bool, int, str):
        return 1
    raise StrictDataError(f"unsupported payload type: {type(value).__name__}")


def shape_value(value: Any) -> Any:
    if type(value) is dict:
        return {key: shape_value(child) for key, child in value.items()}
    if type(value) is list:
        return [shape_value(child) for child in value]
    if value is None:
        return "null"
    if type(value) is bool:
        return "boolean"
    if type(value) is int:
        return "integer"
    if type(value) is str:
        return "string"
    raise StrictDataError(f"unsupported payload type: {type(value).__name__}")


def schema_descriptor(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "booleans_rejected_in_integer_slots": True,
        "duplicate_keys_rejected": True,
        "floats_rejected": True,
        "max_certificate_bytes": MAX_CERTIFICATE_BYTES,
        "non_UTF8_rejected": True,
        "noncanonical_integers_rejected": True,
        "optimized_python_rejected": True,
        "oversized_input_rejected": True,
        "payload_scalar_leaf_count": scalar_leaf_count(payload),
        "payload_shape_sha256": sha256_bytes(canonical_leaf_bytes(shape_value(payload))),
        "payload_top_level_keys": sorted(payload),
        "schema_id": CERTIFICATE_SCHEMA_ID,
        "unknown_fields_rejected_by_full_leaf_rebuild": True,
    }


def base_g7(
    *,
    group_evidence: dict[str, Any],
    resolver_payload: dict[str, Any],
    group_replay_sha256: str,
    group_evidence_sha256: str,
    resolver_payload_sha256: str,
    resolver_evidence_sha256: str,
) -> dict[str, Any]:
    group_replay = group_evidence["independent_replay"]
    resolver_status = resolver_payload["status"]
    if (
        group_evidence["status"] != "PASS"
        or group_replay["python"]["status"] != "PASS"
        or group_replay["python"]["direct_projection_sha256"]
        != GROUP_LOCK["python_projection_sha256"]
        or resolver_status
        != {
            "evidence_status": "PASS",
            "implementation_state": "EVIDENCE_REPLAY_PASS",
            "release_authorized": False,
        }
    ):
        raise StrictDataError("G7 component replay/status mismatch")
    return {
        "acyclic_hash_graph": True,
        "all_evidence_and_source_snapshots_stable_before_certificate_write": True,
        "certificate_root_exact_four_keys": True,
        "checker_full_leaf_rebuild_required": True,
        "component_contracts": {
            "group": {
                "aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
                "evidence_sha256": group_evidence_sha256,
                "independent_checker_source_sha256": GROUP_LOCK[
                    "checker_source_sha256"
                ],
                "producer_source_sha256": GROUP_COMPONENT_CONTRACT[
                    "producer_sha256"
                ],
                "replay_projection_sha256": group_replay_sha256,
                "schema_sha256": GROUP_LOCK["schema_sha256"],
                "status": group_evidence["status"],
            },
            "primitive_resolvent": {
                "aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
                "evidence_sha256": resolver_evidence_sha256,
                "evidence_status": resolver_status["evidence_status"],
                "implementation_state": resolver_status["implementation_state"],
                "independent_checker_source_sha256": RESOLVER_LOCK[
                    "checker_source_sha256"
                ],
                "payload_sha256": resolver_payload_sha256,
                "producer_source_sha256": RESOLVER_COMPONENT_CONTRACT[
                    "producer_sha256"
                ],
                "release_authorized": resolver_status["release_authorized"],
            },
        },
        "evidence_rebound_mutation_count_expected": 10,
        "exact_live_code_results_file_count": 21,
        "exact_payload_top_level_key_count": 15,
        "exact_result_file_count": 8,
        "exact_source_file_count": 13,
        "group_replay": {
            "cross_checks": deepcopy(group_replay["cross_checks"]),
            "direct_projection_sha256": group_replay["python"][
                "direct_projection_sha256"
            ],
            "gap_checker": deepcopy(group_replay["gap_checker"]),
            "python_checks": deepcopy(group_replay["python"]["checks"]),
            "status": group_replay["python"]["status"],
        },
        "independent_check_report_policy": "LATER_CHECK_REPORT_NOT_CERTIFICATE_INPUT",
        "later_manifest_self_excluding": True,
        "payload_scalar_leaf_count": 0,
        "planned_scoped_manifest_entries": 20,
        "producer_checker_theorem_call_graphs_disjoint": True,
        "resolver_replay": deepcopy(resolver_payload["replay_contract"]),
        "resolver_scope_cross_check": deepcopy(resolver_payload["scope"]),
        "schema_scalar_leaf_count": 0,
        "strict_exact_key_and_type_checks": True,
        "strict_parser_required": True,
        "structural_mutation_count_expected": 14,
        "type_mutation_count_expected": 0,
        "value_mutation_count_expected": 0,
    }


def expected_payload(
    source_contract_value: dict[str, Any],
    g0: dict[str, Any],
    artifact_contract_value: dict[str, Any],
    group_evidence: dict[str, Any],
    resolver_evidence: dict[str, Any],
    backend_contract_value: dict[str, Any],
    group_replay_sha256: str,
    group_evidence_sha256: str,
    resolver_evidence_sha256: str,
) -> dict[str, Any]:
    """Independently reconstruct the exact C60 fifteen-key payload.

    The signature is shared with the producer, but this implementation calls
    no producer helper.  Each argument is an already rebound value, never a
    certificate-selected path.
    """

    for value, label, expected in (
        (group_replay_sha256, "group replay digest", GROUP_LOCK["projection_sha256"]),
        (group_evidence_sha256, "group evidence digest", GROUP_LOCK["evidence_sha256"]),
        (resolver_evidence_sha256, "resolver evidence digest", RESOLVER_LOCK["evidence_sha256"]),
    ):
        require_sha256(value, label)
        if value != expected:
            raise StrictDataError(f"{label} differs from frozen component tuple")
    require_exact_keys(resolver_evidence, {"payload", "payload_sha256", "schema_id", "schema_sha256"}, "resolver evidence argument")
    resolver_payload = resolver_evidence["payload"]
    if resolver_evidence["payload_sha256"] != RESOLVER_LOCK["payload_sha256"]:
        raise StrictDataError("resolver payload digest argument mismatch")
    expected_artifact_contract = {
        "artifact_count": 2,
        "artifacts": [
            {
                "path": "results/c60_group_evidence.json",
                "format": "canonical_compact_json",
                "sha256": GROUP_LOCK["evidence_sha256"],
                "size_bytes": GROUP_LOCK["evidence_size_bytes"],
                "schema_id": GROUP_EVIDENCE_SCHEMA_ID,
                "internal_report_sha256": GROUP_LOCK["projection_sha256"],
                "component_aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
            },
            {
                "path": "results/c60_resolvent_evidence.json",
                "format": "canonical_compact_json",
                "sha256": RESOLVER_LOCK["evidence_sha256"],
                "size_bytes": RESOLVER_LOCK["evidence_size_bytes"],
                "schema_id": RESOLVER_EVIDENCE_SCHEMA_ID,
                "internal_report_sha256": RESOLVER_LOCK["payload_sha256"],
                "schema_descriptor_sha256": RESOLVER_LOCK["schema_descriptor_sha256"],
                "component_aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
            },
        ],
        "component_contracts": {
            "group": deepcopy(GROUP_COMPONENT_CONTRACT),
            "primitive_resolvent": deepcopy(RESOLVER_COMPONENT_CONTRACT),
        },
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c60-artifact-contract-v1",
        "source_owned_full_document_validation": True,
    }
    if not deep_exact(artifact_contract_value, expected_artifact_contract):
        raise StrictDataError("artifact contract argument mismatch")

    g1 = derive_g1(group_evidence, resolver_payload, g0)
    g2 = derive_g2(resolver_payload, group_evidence, g0)
    g3 = derive_g3(group_evidence, resolver_payload)
    g4 = derive_g4(group_evidence, resolver_payload)
    g5 = derive_g5(group_evidence)
    g6 = derive_g6(group_evidence)
    resolver_checker_payload_sha256 = sha256_bytes(canonical_json_bytes(resolver_payload))
    if resolver_checker_payload_sha256 != RESOLVER_LOCK["payload_sha256"]:
        raise StrictDataError("resolver payload canonical digest mismatch")
    g7 = base_g7(
        group_evidence=group_evidence,
        resolver_payload=resolver_payload,
        group_replay_sha256=group_replay_sha256,
        group_evidence_sha256=group_evidence_sha256,
        resolver_payload_sha256=resolver_checker_payload_sha256,
        resolver_evidence_sha256=resolver_evidence_sha256,
    )
    payload: dict[str, Any] = {
        "artifact_contract": deepcopy(artifact_contract_value),
        "G0_released_authority_rebind": deepcopy(g0),
        "G1_common_normalizer_lattice": g1,
        "G2_primitive_integral_carriers": g2,
        "G3_formal_invariant_degree_gap": g3,
        "G4_tower_characters_and_zeta": g4,
        "G5_absolute_relative_arithmetic": g5,
        "G6_both_relative_local_towers": g6,
        "G7_independence_scope_release": g7,
        "written_bridges": {key: True for key in sorted(WRITTEN_BRIDGE_KEYS)},
        "backend_contract": deepcopy(backend_contract_value),
        "source_contract": deepcopy(source_contract_value),
        "scope_nonclaims": {key: False for key in sorted(SCOPE_NONCLAIM_KEYS)},
        "nonresults": {
            "characteristic_zero_resolvents": (
                "UNEXPANDED_PRODUCT_FORM_WITH_MODULAR_COEFFICIENT_HASHES_ONLY"
            ),
            "component_evidence_role": (
                "FULL_OBJECTS_REBOUND_AND_SEMANTIC_LEAVES_RECONSTRUCTED"
            ),
            "discriminant_authority": (
                "PERMUTATION_CONDUCTORS_NOT_DEFINING_POLYNOMIAL_DISCRIMINANTS"
            ),
            "formal_invariant_scope": (
                "COMMUTATIVE_Q_COEFFICIENT_FORMAL_POLYNOMIALS_ONLY"
            ),
            "local_row_scope": (
                "COMPLETE_ETALE_ALGEBRA_ROWS_NOT_INDIVIDUAL_FIELD_CLASSIFICATION"
            ),
            "selection_aids": "CHRONOLOGY_ONLY_NOT_THEOREM_AUTHORITY",
            "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "unsupported_machine_dependencies": ["PARI", "Singular"],
        },
        "status": {
            "candidate_id": "HCS-C60",
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "paper_status": "PAPER_BLOCKED_ON_POST_MACHINE_FORMAL_PASS",
            "promotion_authorized": False,
            "release_status": "NOT_RELEASED",
            "theorem_gate_count": 8,
        },
    }
    if set(payload) != set(PAYLOAD_KEYS):
        raise StrictDataError("C60 payload does not have the exact fifteen-key contract")
    payload_leaves = scalar_leaf_count(payload)
    if payload_leaves != 9310:
        raise StrictDataError("C60 canonical payload scalar-leaf count differs")
    payload["G7_independence_scope_release"]["payload_scalar_leaf_count"] = payload_leaves
    temporary_schema = schema_descriptor(payload)
    schema_leaves = scalar_leaf_count(temporary_schema)
    if schema_leaves != 27:
        raise StrictDataError("C60 canonical schema scalar-leaf count differs")
    payload["G7_independence_scope_release"]["schema_scalar_leaf_count"] = schema_leaves
    scalar_mutations = payload_leaves + schema_leaves + 2
    if scalar_mutations != 9339:
        raise StrictDataError("C60 canonical scalar-mutation count differs")
    payload["G7_independence_scope_release"]["value_mutation_count_expected"] = scalar_mutations
    payload["G7_independence_scope_release"]["type_mutation_count_expected"] = scalar_mutations
    if (
        scalar_leaf_count(payload) != payload_leaves
        or scalar_leaf_count(schema_descriptor(payload)) != schema_leaves
    ):
        raise StrictDataError("C60 payload/schema scalar-count fixed point failed")
    return payload


_EXPECTED_DIGEST_CACHE: dict[int, tuple[Any, str]] = {}


def expected_semantic_digest(value: Any) -> str:
    identity = id(value)
    cached = _EXPECTED_DIGEST_CACHE.get(identity)
    if cached is not None and cached[0] is value:
        return cached[1]
    digest = sha256_bytes(canonical_leaf_bytes(value))
    _EXPECTED_DIGEST_CACHE[identity] = (value, digest)
    return digest


def core_verify(
    certificate: Any,
    sidecar_schema: Any,
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> None:
    require_exact_keys(
        certificate,
        {"schema", "schema_sha256", "payload", "payload_sha256"},
        "C60 certificate root",
    )
    if type(sidecar_schema) is not dict:
        raise StrictDataError("C60 schema sidecar must be an object")
    require_exact_keys(sidecar_schema, set(expected_schema), "C60 schema sidecar")
    require_sha256(certificate["schema_sha256"], "C60 schema digest")
    require_sha256(certificate["payload_sha256"], "C60 payload digest")
    if not deep_exact(certificate["schema"], sidecar_schema):
        raise StrictDataError("embedded C60 schema differs from sidecar")
    if certificate["schema_sha256"] != expected_semantic_digest(expected_schema):
        raise StrictDataError("C60 schema digest differs from independent rebuild")
    if certificate["payload_sha256"] != expected_semantic_digest(expected):
        raise StrictDataError("C60 payload digest differs from independent rebuild")
    if not deep_exact(certificate["payload"], expected):
        raise StrictDataError("full C60 semantic payload rebuild mismatch")
    if not deep_exact(sidecar_schema, expected_schema):
        raise StrictDataError("full C60 schema descriptor rebuild mismatch")
    if certificate["schema_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["schema"])):
        raise StrictDataError("C60 compact embedded-schema digest mismatch")
    if certificate["payload_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["payload"])):
        raise StrictDataError("C60 compact payload digest mismatch")


def leaf_paths(value: Any, prefix: tuple[Any, ...] = ()) -> Iterator[tuple[Any, ...]]:
    if type(value) is dict:
        for key in sorted(value):
            yield from leaf_paths(value[key], prefix + (key,))
    elif type(value) is list:
        for index, child in enumerate(value):
            yield from leaf_paths(child, prefix + (index,))
    elif value is None or type(value) in (bool, int, str):
        yield prefix
    else:
        raise StrictDataError("unsupported mutation leaf type")


def get_path(value: Any, path: tuple[Any, ...]) -> Any:
    current = value
    for component in path:
        current = current[component]
    return current


def set_path(value: Any, path: tuple[Any, ...], replacement: Any) -> None:
    if not path:
        raise StrictDataError("cannot replace an empty mutation path")
    current = value
    for component in path[:-1]:
        current = current[component]
    current[path[-1]] = replacement


def value_mutation(value: Any) -> Any:
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1 if value != -1 else value - 1
    if type(value) is str:
        return value + "#"
    if value is None:
        return "non-null"
    raise StrictDataError("unsupported value-mutation leaf")


def type_mutation(value: Any) -> Any:
    if type(value) is bool:
        return 0
    if type(value) is int:
        return False
    if type(value) is str:
        return 0
    if value is None:
        return False
    raise StrictDataError("unsupported type-mutation leaf")


def canonical_bytes_and_leaf_spans(value: Any) -> tuple[bytes, dict[tuple[Any, ...], tuple[int, int]]]:
    output = bytearray()
    spans: dict[tuple[Any, ...], tuple[int, int]] = {}

    def emit(child: Any, path: tuple[Any, ...]) -> None:
        if type(child) is dict:
            output.extend(b"{")
            for index, key in enumerate(sorted(child)):
                if index:
                    output.extend(b",")
                output.extend(canonical_leaf_bytes(key))
                output.extend(b":")
                emit(child[key], path + (key,))
            output.extend(b"}")
        elif type(child) is list:
            output.extend(b"[")
            for index, item in enumerate(child):
                if index:
                    output.extend(b",")
                emit(item, path + (index,))
            output.extend(b"]")
        elif child is None or type(child) in (bool, int, str):
            start = len(output)
            output.extend(canonical_leaf_bytes(child))
            spans[path] = (start, len(output))
        else:
            raise StrictDataError("unsupported canonical span value")

    emit(value, ())
    raw = bytes(output)
    if raw != canonical_leaf_bytes(value) or len(spans) != scalar_leaf_count(value):
        raise StrictDataError("canonical scalar-span serialization differs")
    return raw, spans


def rebound_digest(original_raw: bytes, span: tuple[int, int], replacement: Any) -> str:
    start, end = span
    digest = hashlib.sha256()
    digest.update(original_raw[:start])
    digest.update(canonical_leaf_bytes(replacement))
    digest.update(original_raw[end:])
    return digest.hexdigest()


def expect_core_rejection(
    certificate: Any,
    schema: Any,
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
    label: str,
) -> None:
    try:
        core_verify(certificate, schema, expected, expected_schema)
    except (StrictDataError, KeyError, IndexError, TypeError):
        return
    raise StrictDataError(f"C60 checker accepted hostile mutation: {label}")


def verifier_rebound_sweep(
    certificate: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> dict[str, int]:
    payload_value = payload_type = 0
    payload_mutant = deepcopy(certificate)
    original_payload_digest = payload_mutant["payload_sha256"]
    original_payload_raw, payload_spans = canonical_bytes_and_leaf_spans(expected)
    for path in leaf_paths(expected):
        for kind, mutator in (("value", value_mutation), ("type", type_mutation)):
            original = get_path(payload_mutant["payload"], path)
            replacement = mutator(original)
            set_path(payload_mutant["payload"], path, replacement)
            payload_mutant["payload_sha256"] = rebound_digest(
                original_payload_raw, payload_spans[path], replacement
            )
            expect_core_rejection(
                payload_mutant, schema, expected, expected_schema,
                f"payload-{kind}:{path}",
            )
            set_path(payload_mutant["payload"], path, original)
            payload_mutant["payload_sha256"] = original_payload_digest
            if kind == "value":
                payload_value += 1
            else:
                payload_type += 1

    schema_value = schema_type = 0
    schema_mutant = deepcopy(schema)
    schema_certificate = deepcopy(certificate)
    original_schema_digest = schema_certificate["schema_sha256"]
    for path in leaf_paths(expected_schema):
        for kind, mutator in (("value", value_mutation), ("type", type_mutation)):
            original = get_path(schema_mutant, path)
            replacement = mutator(original)
            set_path(schema_mutant, path, replacement)
            set_path(schema_certificate["schema"], path, replacement)
            schema_certificate["schema_sha256"] = sha256_bytes(canonical_leaf_bytes(schema_mutant))
            expect_core_rejection(
                schema_certificate, schema_mutant, expected, expected_schema,
                f"schema-{kind}:{path}",
            )
            set_path(schema_mutant, path, original)
            set_path(schema_certificate["schema"], path, original)
            schema_certificate["schema_sha256"] = original_schema_digest
            if kind == "value":
                schema_value += 1
            else:
                schema_type += 1

    root_value = root_type = 0
    root_mutant = deepcopy(certificate)
    for key in ("schema_sha256", "payload_sha256"):
        for kind, mutator in (("value", value_mutation), ("type", type_mutation)):
            original = root_mutant[key]
            root_mutant[key] = mutator(original)
            expect_core_rejection(root_mutant, schema, expected, expected_schema, f"root-{kind}:{key}")
            root_mutant[key] = original
            if kind == "value":
                root_value += 1
            else:
                root_type += 1

    structural: list[tuple[str, Any, Any]] = []
    mutant = deepcopy(certificate); mutant["unknown"] = False
    structural.append(("root-extra", mutant, schema))
    mutant = deepcopy(certificate); del mutant["schema_sha256"]
    structural.append(("root-missing", mutant, schema))
    mutant = deepcopy(certificate); mutant["schema"] = []
    structural.append(("root-schema-container", mutant, schema))
    mutant = deepcopy(certificate); mutant["payload"] = []
    structural.append(("root-payload-container", mutant, schema))
    mutant = deepcopy(certificate); mutant["payload"]["unknown"] = False; mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-extra", mutant, schema))
    mutant = deepcopy(certificate); del mutant["payload"]["status"]; mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-missing", mutant, schema))
    mutant = deepcopy(certificate); mutant["payload"]["G3_formal_invariant_degree_gap"] = []; mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-gate-container", mutant, schema))
    mutant = deepcopy(certificate); mutant["payload"]["G3_formal_invariant_degree_gap"]["actual_one_based_partitions"]["H0_unordered_pair_partition"].pop(); mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-list-length", mutant, schema))
    mutant_schema = deepcopy(schema); mutant_schema["unknown"] = False
    mutant = deepcopy(certificate); mutant["schema"] = deepcopy(mutant_schema); mutant["schema_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant_schema))
    structural.append(("schema-extra", mutant, mutant_schema))
    mutant_schema = deepcopy(schema); del mutant_schema["schema_id"]
    mutant = deepcopy(certificate); mutant["schema"] = deepcopy(mutant_schema); mutant["schema_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant_schema))
    structural.append(("schema-missing", mutant, mutant_schema))
    mutant_schema = deepcopy(schema); mutant_schema["payload_top_level_keys"].append("unknown")
    mutant = deepcopy(certificate); mutant["schema"] = deepcopy(mutant_schema); mutant["schema_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant_schema))
    structural.append(("schema-list-length", mutant, mutant_schema))
    structural.append(("schema-sidecar-container", deepcopy(certificate), []))
    mutant = deepcopy(certificate); mutant["payload"]["artifact_contract"]["artifacts"].pop(); mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("artifact-list-length", mutant, schema))
    mutant = deepcopy(certificate); del mutant["payload"]["scope_nonclaims"]["release_claimed"]; mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("scope-key-missing", mutant, schema))
    if len(structural) != 14:
        raise RuntimeError("C60 structural mutation inventory changed")
    for label, mutant, mutant_schema in structural:
        expect_core_rejection(mutant, mutant_schema, expected, expected_schema, label)

    value_total = payload_value + schema_value + root_value
    type_total = payload_type + schema_type + root_type
    g7 = expected["G7_independence_scope_release"]
    if (
        value_total != g7["value_mutation_count_expected"]
        or type_total != g7["type_mutation_count_expected"]
        or len(structural) != g7["structural_mutation_count_expected"]
    ):
        raise StrictDataError("C60 mutation sweep count differs from G7 contract")
    return {
        "payload_value_mutations_rejected": payload_value,
        "payload_type_mutations_rejected": payload_type,
        "schema_value_mutations_rejected": schema_value,
        "schema_type_mutations_rejected": schema_type,
        "root_value_mutations_rejected": root_value,
        "root_type_mutations_rejected": root_type,
        "structural_mutations_rejected": len(structural),
        "value_mutations_rejected": value_total,
        "type_mutations_rejected": type_total,
        "total_certificate_mutations_rejected": value_total + type_total + len(structural),
    }


def actual_resolver_rejects(mutant: dict[str, Any], guard: SnapshotGuard, label: str) -> None:
    guard.assert_unchanged(f"before hostile resolver verifier {label}")
    try:
        reconstruct_resolver_evidence(
            mutant,
            RESOLVER_SCHEMA_DESCRIPTOR,
            c59_resolvent_module=C59 / "code/c59_resolvent.py",
            c59_resolvent_evidence=C59 / "results/c59_resolvent_evidence.json",
            c59_full_manifest=C59 / "FULL_PROJECT_HASHES.sha256",
            c59_route=C59 / "route_a_evaluation.yaml",
            c59_route_archive=C59_ROUTE_ARCHIVE,
        )
    except (ValueError, KeyError, TypeError, IndexError):
        guard.assert_unchanged(f"after hostile resolver verifier {label}")
        return
    guard.assert_unchanged(f"after hostile resolver verifier {label}")
    raise StrictDataError(f"actual resolver verifier accepted mutation: {label}")


def evidence_rebound_suite(
    certificate: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
    group_document: dict[str, Any],
    group_projection: dict[str, Any],
    resolver_document: dict[str, Any],
    guard: SnapshotGuard,
) -> dict[str, int]:
    evidence_rejected = 0
    artifact_rejected = 0
    actual_group_rejections = 0
    actual_resolver_rejections = 0

    group_mutations: list[tuple[str, dict[str, Any]]] = []
    mutant = deepcopy(group_document); mutant["G1_common_normalizer_uniqueness"]["collision_normalizer_scan"]["rows"][-1]["normalizers_conjugate_and_index_two_over_both"] = False
    group_mutations.append(("G1-predicate", mutant))
    mutant = deepcopy(group_document); mutant["G3_orbit_partition_obstruction"]["pair_partitions"][2][0].pop()
    group_mutations.append(("G3-partition", mutant))
    mutant = deepcopy(group_document); mutant["G4_biquadratic_tower_characters"]["character_relation"]["vectors"]["J"][0] += 1
    group_mutations.append(("G4-character", mutant))
    mutant = deepcopy(group_document); mutant["G5_global_relative_discriminants"]["global_arithmetic"]["fields"][0]["conductor_exponents_p3_p5_A_B"][0] += 1
    group_mutations.append(("G5-conductor", mutant))
    mutant = deepcopy(group_document); mutant["G6_two_local_branches"]["tom140"]["relative_tower_over_N"]["relative_factor_counts_H301_H302_H303_J"][0] += 1
    group_mutations.append(("G6-local", mutant))
    mutant = deepcopy(group_document); mutant["frozen_permutation_arrays"]["arrays"]["H302_generators"][0][0], mutant["frozen_permutation_arrays"]["arrays"]["H302_generators"][0][1] = mutant["frozen_permutation_arrays"]["arrays"]["H302_generators"][0][1], mutant["frozen_permutation_arrays"]["arrays"]["H302_generators"][0][0]
    mutant["frozen_permutation_arrays"]["canonical_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["frozen_permutation_arrays"]["arrays"]))
    group_mutations.append(("arrays", mutant))
    for label, mutant in group_mutations:
        try:
            validate_group_evidence(
                mutant,
                group_projection,
                GROUP_LOCK["projection_sha256"],
                GROUP_LOCK["projection_size_bytes"],
            )
        except (StrictDataError, KeyError, TypeError, IndexError):
            actual_group_rejections += 1
        else:
            raise StrictDataError(f"actual group verifier accepted mutation: {label}")
        mutant_raw = canonical_json_bytes(mutant)
        rebound = deepcopy(certificate)
        row = rebound["payload"]["artifact_contract"]["artifacts"][0]
        row["sha256"] = sha256_bytes(mutant_raw)
        row["size_bytes"] = len(mutant_raw)
        rebound["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(rebound["payload"]))
        expect_core_rejection(rebound, schema, expected, expected_schema, f"group-evidence-rebound:{label}")
        evidence_rejected += 1

    resolver_mutations: list[tuple[str, dict[str, Any]]] = []
    mutant = deepcopy(resolver_document)
    mutant["payload"]["carriers"]["M"]["carrier"][0][0] = [0, 26]
    mutant["payload"]["carriers"]["M"]["carrier_sha256"] = sha256_bytes(
        canonical_leaf_bytes(mutant["payload"]["carriers"]["M"]["carrier"])
    )
    resolver_mutations.append(("deep-carrier", mutant))
    mutant = deepcopy(resolver_document)
    mutant["payload"]["carriers"]["L"]["modular_polynomial"]["coefficient_sha256"] = "0" * 64
    resolver_mutations.append(("deep-polynomial", mutant))
    mutant = deepcopy(resolver_document)
    mutant["payload"]["invariant_degree_obstruction"]["H0_pair_partition_sha256"] = "0" * 64
    resolver_mutations.append(("deep-obstruction", mutant))
    mutant = deepcopy(resolver_document); mutant["payload"]["unknown"] = False
    resolver_mutations.append(("payload-extra", mutant))
    for label, mutant in resolver_mutations:
        mutant["payload_sha256"] = sha256_bytes(canonical_json_bytes(mutant["payload"]))
        actual_resolver_rejects(mutant, guard, label)
        actual_resolver_rejections += 1
        mutant_raw = canonical_json_bytes(mutant)
        rebound = deepcopy(certificate)
        row = rebound["payload"]["artifact_contract"]["artifacts"][1]
        row["sha256"] = sha256_bytes(mutant_raw)
        row["size_bytes"] = len(mutant_raw)
        row["internal_report_sha256"] = mutant["payload_sha256"]
        rebound["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(rebound["payload"]))
        expect_core_rejection(rebound, schema, expected, expected_schema, f"resolver-evidence-rebound:{label}")
        evidence_rejected += 1

    for artifact_index in (0, 1):
        rebound = deepcopy(certificate)
        rebound["payload"]["artifact_contract"]["artifacts"][artifact_index]["sha256"] = "0" * 64
        rebound["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(rebound["payload"]))
        expect_core_rejection(rebound, schema, expected, expected_schema, f"artifact-digest-rebound:{artifact_index}")
        artifact_rejected += 1
    if evidence_rejected != expected["G7_independence_scope_release"]["evidence_rebound_mutation_count_expected"]:
        raise StrictDataError("C60 evidence mutation count differs from G7 contract")
    if artifact_rejected != 2:
        raise StrictDataError("C60 artifact hostile-rebound count differs")
    return {
        "actual_group_verifier_mutations_rejected": actual_group_rejections,
        "actual_resolver_verifier_mutations_rejected": actual_resolver_rejections,
        "self_consistent_evidence_rebound_mutations_rejected": evidence_rejected,
        "additional_artifact_hostile_rebounds_rejected": artifact_rejected,
        "total_evidence_and_artifact_rebounds_rejected": (
            evidence_rejected + artifact_rejected
        ),
    }


def strict_parser_cases() -> dict[str, int]:
    rejected = 0
    invalid = (
        b'{"a":1,"a":2}', b'{"a":-0}', b'{"a":01}', b'{"a":1.0}',
        b'{"a":1e2}', b'{"a":NaN}', b'{"a":Infinity}', b"\xef\xbb\xbf{}",
        b'{"a":"\xff"}', b'{} trailing',
    )
    for raw in invalid:
        try:
            strict_json_loads(raw, max_bytes=100)
        except StrictDataError:
            rejected += 1
        else:
            raise StrictDataError(f"strict parser accepted invalid bytes: {raw!r}")
    try:
        strict_json_loads(b'{"a":1}', max_bytes=3)
    except StrictDataError:
        rejected += 1
    else:
        raise StrictDataError("strict parser accepted oversized input")
    for raw in (b'{ "a":1}\n', b'{"a" :1}\n', b'{"a": 1}\n', b'{"a":"\\u0061"}\n'):
        try:
            require_canonical_compact_json(raw)
        except StrictDataError:
            rejected += 1
        else:
            raise StrictDataError("compact parser accepted noncanonical bytes")
    huge = b'{"a":' + b"9" * 100_000 + b"}"
    value = strict_json_loads(huge, max_bytes=len(huge))
    if type(value["a"]) is not int:
        raise StrictDataError("canonical 100k-digit integer was not accepted")
    return {
        "canonical_100k_digit_integer_accepted": 1,
        "invalid_or_noncanonical_cases_rejected": rejected,
    }


def checker_source_architecture_audit() -> dict[str, int | bool]:
    raw, _ = read_stable(CODE_DIR / "c60_checker.py", max_bytes=8_000_000)
    try:
        tree = ast.parse(raw.decode("utf-8", errors="strict"), filename="c60_checker.py")
    except (SyntaxError, UnicodeDecodeError) as exc:
        raise StrictDataError("C60 checker source parse failed") from exc
    dictionary_nodes = 0
    local_imports: set[str] = set()
    for node in ast.walk(tree):
        if type(node) is ast.Dict:
            keys = [
                key.value for key in node.keys
                if type(key) is ast.Constant and type(key.value) is str
            ]
            if len(keys) != len(set(keys)):
                raise StrictDataError("duplicate literal dictionary key in C60 checker")
            dictionary_nodes += 1
        elif type(node) is ast.Import:
            local_imports.update(alias.name.split(".")[0] for alias in node.names if alias.name.startswith("c60_"))
        elif type(node) is ast.ImportFrom and node.module and node.module.startswith("c60_"):
            local_imports.add(node.module.split(".")[0])
    expected = {"c60_exact", "c60_pipeline", "c60_checker_resolvent"}
    forbidden = {"c60_producer", "c60_group", "c60_resolvent"}
    if local_imports != expected or local_imports & forbidden:
        raise StrictDataError(f"C60 checker local import boundary mismatch: {sorted(local_imports)}")
    return {
        "checker_literal_dictionary_nodes_checked": dictionary_nodes,
        "checker_exact_local_import_set": True,
        "checker_forbidden_producer_imports_absent": True,
        "producer_source_not_parsed_by_checker_audit": True,
    }


def validate_fixed_paths(arguments: argparse.Namespace) -> tuple[Path, Path, Path, Path, Path, Path]:
    mapping = {
        arguments.certificate: "c60_certificate.json",
        arguments.schema: "c60_schema.json",
        arguments.group_evidence: "c60_group_evidence.json",
        arguments.resolvent_evidence: "c60_resolvent_evidence.json",
        arguments.output: "c60_check_report.json",
    }
    if any(path.name != basename for path, basename in mapping.items()):
        raise StrictDataError("C60 certificate/schema/evidence/output basenames are fixed")
    absolute = tuple(path.absolute() for path in mapping)
    parent = absolute[0].parent
    results = (PROJECT / "results").absolute()
    if (
        any(path.parent != parent for path in absolute)
        or not parent.is_dir()
        or parent.is_symlink()
        or parent.resolve(strict=True) != parent
        or not results.is_dir()
        or results.is_symlink()
        or results.resolve(strict=True) != results
        or parent.parent != results
        or re.fullmatch(r"\.c60-stage-[A-Za-z0-9]{8}", parent.name) is None
    ):
        raise StrictDataError(
            "C60 inputs/output must share one canonical real .c60-stage-* direct child of PROJECT/results"
        )
    parent_seal = seal_directory(parent)
    inputs = absolute[:4]
    inodes: set[tuple[int, int]] = set()
    limits = (
        MAX_CERTIFICATE_BYTES,
        MAX_SCHEMA_BYTES,
        MAX_GROUP_EVIDENCE_BYTES,
        MAX_RESOLVER_EVIDENCE_BYTES,
    )
    for path, limit in zip(inputs, limits):
        raw, _ = read_stable(path, max_bytes=limit)
        if path.resolve(strict=True) != path:
            raise StrictDataError("C60 input path is not canonical")
        metadata = path.stat()
        inode = (metadata.st_dev, metadata.st_ino)
        if (
            inode in inodes
            or metadata.st_nlink != 1
            or stat.S_IMODE(metadata.st_mode) != 0o644
            or not raw
        ):
            raise StrictDataError("C60 input mode/hardlink/link-count/empty-file firewall failed")
        inodes.add(inode)
    if seal_directory(parent) != parent_seal:
        raise StrictDataError("C60 stage parent changed during path validation")
    return (*absolute, parent)


def protected_paths(
    certificate: Path,
    schema: Path,
    group_evidence: Path,
    resolver_evidence: Path,
    math_python: Path,
    gap_path: Path,
) -> list[Path]:
    paths = [CODE_DIR / name for name in sorted(CODE_SOURCE_NAMES)]
    paths.extend(c59_manifest_member_paths())
    paths.extend([certificate, schema, group_evidence, resolver_evidence])
    paths.extend(PROJECT / name for name in sorted(FORMAL_MARKDOWN_NAMES))
    paths.extend([PROJECT / "route_a_evaluation.yaml", BATCH, GUARD])
    for component in (
        PROJECT / "results/c60_group_evidence.json",
        PROJECT / "results/c60_resolvent_evidence.json",
    ):
        if component.exists():
            paths.append(component)
    paths.extend([math_python.resolve(strict=True), gap_path.resolve(strict=True)])
    return paths


def rebind_raw_inputs(
    paths: tuple[Path, Path, Path, Path],
    originals: tuple[tuple[bytes, FileSeal], ...],
) -> None:
    for path, (expected_raw, expected_seal) in zip(paths, originals):
        raw, _ = read_stable(path, max_bytes=MAX_CERTIFICATE_BYTES)
        if raw != expected_raw or seal_file(path) != expected_seal:
            raise StrictDataError(f"C60 input changed during replay: {path.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--group-evidence", type=Path, required=True)
    parser.add_argument("--resolvent-evidence", type=Path, required=True)
    parser.add_argument("--math-python", type=Path, required=True)
    parser.add_argument("--gap", type=Path, required=True)
    arguments = parser.parse_args()
    reject_optimized_python()

    # An incomplete source tree cannot remove or replace even a stale report.
    source_before = exact_source_contract()
    certificate_path, schema_path, group_path, resolver_path, output_path, stage_parent = validate_fixed_paths(arguments)
    certificate_raw, certificate_fp = read_stable(certificate_path, max_bytes=MAX_CERTIFICATE_BYTES)
    schema_raw, schema_fp = read_stable(schema_path, max_bytes=MAX_SCHEMA_BYTES)
    group_raw, group_fp = read_stable(group_path, max_bytes=MAX_GROUP_EVIDENCE_BYTES)
    resolver_raw, resolver_fp = read_stable(resolver_path, max_bytes=MAX_RESOLVER_EVIDENCE_BYTES)
    certificate = canonical_pretty(certificate_raw, max_bytes=MAX_CERTIFICATE_BYTES, label="C60 certificate")
    schema = canonical_pretty(schema_raw, max_bytes=MAX_SCHEMA_BYTES, label="C60 schema")
    group_document = compact_document(group_raw, max_bytes=MAX_GROUP_EVIDENCE_BYTES, label="C60 group evidence")
    resolver_document = compact_document(resolver_raw, max_bytes=MAX_RESOLVER_EVIDENCE_BYTES, label="C60 resolver evidence")
    originals = tuple(
        (raw, seal_file(path))
        for path, raw in (
            (certificate_path, certificate_raw),
            (schema_path, schema_raw),
            (group_path, group_raw),
            (resolver_path, resolver_raw),
        )
    )

    protected = protected_paths(
        certificate_path,
        schema_path,
        group_path,
        resolver_path,
        arguments.math_python,
        arguments.gap,
    )
    (output,) = prepare_output_targets((output_path,), protected=protected)
    guard = SnapshotGuard(protected, directories=(CODE_DIR, stage_parent))
    try:
        backends = backend_contract(arguments.math_python, arguments.gap, guard)
        g0 = rebuild_g0(guard)
        group_projection, group_projection_sha256, group_projection_size = run_group_projection(arguments.gap, guard)
        validate_group_evidence(
            group_document,
            group_projection,
            group_projection_sha256,
            group_projection_size,
        )
        resolver_payload = validate_resolver_evidence(resolver_document, guard)
        if not deep_exact(resolver_payload, resolver_document["payload"]):
            raise StrictDataError("resolver checker returned a different payload object")
        artifacts = artifact_contract(
            group_path,
            group_raw,
            group_document,
            resolver_path,
            resolver_raw,
            resolver_document,
        )
        expected = expected_payload(
            source_before,
            g0,
            artifacts,
            group_document,
            resolver_document,
            backends,
            group_projection_sha256,
            group_fp.sha256,
            resolver_fp.sha256,
        )
        expected_schema = schema_descriptor(expected)
        core_verify(certificate, schema, expected, expected_schema)
        source_audit = checker_source_architecture_audit()
        parser_report = strict_parser_cases()
        rebound = verifier_rebound_sweep(certificate, schema, expected, expected_schema)
        evidence_rebound = evidence_rebound_suite(
            certificate,
            schema,
            expected,
            expected_schema,
            group_document,
            group_projection,
            resolver_document,
            guard,
        )

        if not deep_exact(source_before, exact_source_contract()):
            raise StrictDataError("C60 source contract changed during checker replay")
        rebind_raw_inputs(
            (certificate_path, schema_path, group_path, resolver_path),
            originals,
        )
        guard.assert_unchanged("after semantic and mutation replay")
        final_g0 = rebuild_g0(guard)
        if not deep_exact(g0, final_g0):
            raise StrictDataError("C59/C60 formal authority changed during checker replay")

        report = {
            "schema_id": CHECK_REPORT_SCHEMA_ID,
            "status": "PREFREEZE_CODE_RESULTS_PASS",
            "result": "PASS_PREFREEZE_CODE_RESULTS",
            "certificate": {
                "path": "results/c60_certificate.json",
                "sha256": certificate_fp.sha256,
                "size_bytes": certificate_fp.size_bytes,
                "payload_sha256": certificate["payload_sha256"],
            },
            "schema_file": {
                "path": "results/c60_schema.json",
                "sha256": schema_fp.sha256,
                "size_bytes": schema_fp.size_bytes,
                "compact_embedded_schema_sha256": certificate["schema_sha256"],
                "parsed_deep_equal_embedded_schema": True,
            },
            "evidence": {
                "group_sha256": group_fp.sha256,
                "group_size_bytes": group_fp.size_bytes,
                "group_projection_sha256": group_projection_sha256,
                "resolver_sha256": resolver_fp.sha256,
                "resolver_size_bytes": resolver_fp.size_bytes,
                "resolver_payload_sha256": resolver_document["payload_sha256"],
            },
            "source_contract_sha256": sha256_bytes(canonical_leaf_bytes(source_before)),
            "g0_released_authority_sha256": sha256_bytes(canonical_leaf_bytes(g0)),
            "executed_gates": [f"G{index}" for index in range(8)],
            "gate_payload_sha256": {
                f"G{index}": sha256_bytes(canonical_leaf_bytes(expected[key]))
                for index, key in enumerate(
                    (
                        "G0_released_authority_rebind",
                        "G1_common_normalizer_lattice",
                        "G2_primitive_integral_carriers",
                        "G3_formal_invariant_degree_gap",
                        "G4_tower_characters_and_zeta",
                        "G5_absolute_relative_arithmetic",
                        "G6_both_relative_local_towers",
                        "G7_independence_scope_release",
                    )
                )
            },
            "full_semantic_leaf_rebuild": True,
            "payload_scalar_leaf_count": scalar_leaf_count(expected),
            "payload_shape_sha256": expected_schema["payload_shape_sha256"],
            "scalar_leaf_rebound": rebound,
            "evidence_rebound": evidence_rebound,
            "strict_parser_cases": parser_report,
            "source_architecture_audit": source_audit,
            "backend_contract": backends,
            "child_snapshot_rebind_checks": guard.rebind_checks,
            "source_evidence_authority_stable_before_after_every_child": True,
            "independent_checker_does_not_import_or_call_producer_theorem_helpers": True,
            "independent_check_report_policy": "REPORT_HAS_NO_SELF_HASH_AND_IS_NOT_A_CERTIFICATE_INPUT",
            "paper_status": expected["status"]["paper_status"],
            "release_status": "NOT_RELEASED",
            "promotion_authorized": False,
        }
        report_raw = canonical_json_bytes(report, pretty=True)

        if not deep_exact(source_before, exact_source_contract()):
            raise StrictDataError("C60 source changed before report write")
        rebind_raw_inputs(
            (certificate_path, schema_path, group_path, resolver_path),
            originals,
        )
        guard.assert_unchanged("immediately before independent report write")
        atomic_write(output, report_raw)
    except BaseException:
        if output.exists() and output.is_file() and not output.is_symlink():
            output.unlink()
        raise
    print("C60 CHECK PASS PREFREEZE")
    print("theorem_gates=8")
    print(f"payload_scalar_leaves={scalar_leaf_count(expected)}")
    print(f"rebound_mutations={rebound['total_certificate_mutations_rejected']}")


if __name__ == "__main__":
    main()
