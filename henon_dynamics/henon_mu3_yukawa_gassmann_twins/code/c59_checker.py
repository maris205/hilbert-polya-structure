#!/usr/bin/env python3
"""Independent, fail-closed checker for the HCS-C59 machine tuple.

The theorem boundary is deliberately asymmetric.  The producer owns no
checker answer and this module imports no producer theorem implementation.
It reconstructs G1 through the independently written resolver checker,
executes the independently written GAP checker for G2/G4/G5/G6, and derives
G3 and the remaining arithmetic/contract leaves locally.  Shared Python code
is restricted to exact I/O, environment cleaning, and backend constants.

The production entry point requires the exact thirteen-file source inventory.
Consequently this staged source fails closed until the complete official
inventory is present beside it as ``code/c59_checker.py``.
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

from c59_exact import (
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
from c59_pipeline import EXPECTED_BACKENDS, EXPECTED_GAP, clean_environment
from c59_checker_resolvent import reconstruct_payload as reconstruct_resolvent_payload


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
if CODE.name == "code" and PROJECT.name == "henon_mu3_yukawa_gassmann_twins":
    REPO = PROJECT.parents[1]
else:
    # Staged syntax/self-tests have no repository authority.  Production
    # functions below therefore resolve to a guaranteed-missing sentinel and
    # cannot silently consume the ambient working directory.
    REPO = Path("/__C59_STAGED_SOURCE_HAS_NO_REPOSITORY_AUTHORITY__")
C56 = REPO / "henon_dynamics/henon_mu3_yukawa_line_field"
C58 = REPO / "henon_dynamics/henon_mu3_yukawa_line_ramification"
C59 = REPO / "henon_dynamics/henon_mu3_yukawa_gassmann_twins"
BATCH = REPO / "henon_dynamics/BATCH_PLAN_C57_C61.md"
GUARD = REPO / "henon_dynamics/codex_prompt.md"

CERTIFICATE_SCHEMA_ID = "hcs-c59-certificate-schema-v1"
CHECK_REPORT_SCHEMA_ID = "hcs-c59-independent-check-report-v1"
GROUP_EVIDENCE_SCHEMA_ID = "hcs-c59-group-evidence-v1"
GROUP_PROJECTION_SCHEMA_ID = "hcs-c59-checker-group-projection-v1"
RESOLVENT_EVIDENCE_SCHEMA_ID = "hcs-c59-resolvent-evidence-v1"
MAX_CERTIFICATE_BYTES = 5_000_000
MAX_SCHEMA_BYTES = 200_000
MAX_GROUP_EVIDENCE_BYTES = 2_000_000
MAX_RESOLVENT_EVIDENCE_BYTES = 5_000_000
MAX_CHILD_STDOUT_BYTES = 8_000_000

PAYLOAD_KEYS = (
    "artifact_contract",
    "G0_released_authority_rebind",
    "G1_primitive_orbit_resolvents",
    "G2_gassmann_minimality",
    "G3_fixed_fields_and_zeta",
    "G4_global_arithmetic",
    "G5_tom140_local_algebra",
    "G6_tom206_local_algebra",
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
    "c59_atomic_promote.py",
    "c59_checker.py",
    "c59_checker_group.g",
    "c59_checker_resolvent.py",
    "c59_exact.py",
    "c59_group.py",
    "c59_hash_manifest.py",
    "c59_pipeline.py",
    "c59_producer.py",
    "c59_resolvent.py",
    "run_all.sh",
    "test_c59.py",
}
RESULT_NAMES = {
    "RESULTS.md",
    "TEST_REPORT.md",
    "c59_certificate.json",
    "c59_check_report.json",
    "c59_group_evidence.json",
    "c59_resolvent_evidence.json",
    "c59_schema.json",
    "scoped_hash_manifest.json",
}
ARTIFACT_NAMES = (
    "c59_group_evidence.json",
    "c59_resolvent_evidence.json",
)
WRITTEN_BRIDGE_KEYS = {
    "integral_scaling_and_orbit_product",
    "graph_labelling_and_transported_subgroups",
    "modular_noncollision_to_fixed_field",
    "core_normal_closure_nonisomorphism_and_artin_formalism",
    "permutation_conductor_to_signed_field_discriminant",
    "double_cosets_to_local_completion_rows_and_degree_separator",
}
SCOPE_NONCLAIM_KEYS = {
    "integral_permutation_equivalence_claimed",
    "rings_of_integers_isomorphic_claimed",
    "class_number_equality_claimed",
    "idele_group_isomorphism_claimed",
    "local_equivalence_claimed",
    "adelic_equivalence_claimed",
    "d3_branch_selected",
    "local_fields_classified_by_nefd_rows",
    "expanded_characteristic_zero_resolvent_claimed",
    "characteristic_zero_coefficient_hash_claimed",
    "integral_basis_claimed",
    "maximal_order_claimed",
    "monogenicity_claimed",
    "polynomial_discriminant_equals_field_discriminant_claimed",
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

if len(CODE_SOURCE_NAMES) != 13 or len(RESULT_NAMES) != 8:
    raise RuntimeError("C59 source/result inventory cardinality changed")
if len(PAYLOAD_KEYS) != 15 or len(SCOPE_NONCLAIM_KEYS) != 30:
    raise RuntimeError("C59 payload/scope contract cardinality changed")

RELEASES = {
    "C56": {
        "project": C56,
        "release_commit": "a55f31dca338d1e3757704b8c95d11e28c9c98d4",
        "manifest_sha256": "26e3e4226cd1baea14543f14bac9ffd060ed8031741cb1ec0a38e22cd07487f4",
        "manifest_entries": 46,
        "certificate_sha256": "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4",
        "payload_sha256": "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661",
        "schema_sha256": "adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504",
        "check_sha256": "4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9",
        "scoped_sha256": "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a",
        "route_sha256": "cc17a14a3565165de2249bc5219f209b6546ffd91b583e75ac07bbba7730ca73",
        "archive": "evaluations/route_a/HCS-C56/20260815T000000Z.yaml",
    },
    "C58": {
        "project": C58,
        "release_commit": "184b9a8a91234a5d793d5deaa3b652ed56a524bd",
        "manifest_sha256": "06b7c24190d532d6c543b93f74a65d650265988734f340bbb8896953e34d3cb0",
        "manifest_entries": 56,
        "certificate_sha256": "456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee",
        "payload_sha256": "fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f",
        "schema_sha256": "ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a",
        "check_sha256": "64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9",
        "scoped_sha256": "a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730",
        "route_sha256": "4300ea23d084a2e16a0b37e63df3311e692d58efd2750ba4e204f0602e8225fd",
        "archive": "evaluations/route_a/HCS-C58/20260816T000000Z.yaml",
        "group_evidence_sha256": "0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd",
    },
}

FORMAL_LOCK = {
    "markdown_aggregate_sha256": "19f3e829b69816758af132bc5e2c4a478c838e312f99a74390a1d26724cba30f",
    "route_sha256": "81f6b6c95b269e10b4d0d3f83589cc310bb2eaef4130df314c4946fa254886a7",
    "batch_sha256": "d78acbe23fe99c8801ac8e90ec75d691a65dc1baf949713e00cc417260382d12",
    "guard_sha256": "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead",
}

EXPECTED_COLLISION_BUCKETS = [
    [12, 15], [17, 21], [29, 36], [31, 39], [41, 42], [46, 48],
    [57, 58], [59, 64], [112, 120], [132, 140], [301, 303],
]
EXPECTED_ORBIT_COUNTS = [36, 56, 112, 16, 64, 128, 160, 168]
EXPECTED_EXPONENTS = [624, 496, 192, 160]
LARGE_PRIME = 14932047182473291995860108491583652133938007263719
EXPECTED_FACTORIZATION = [
    [3, 624], [5, 496], [181, 192], [283, 160], [997, 192],
    [1801, 160], [2346241, 192], [LARGE_PRIME, 160],
]
EXPECTED_DISCRIMINANT_SHA256 = (
    "7f3ed0f731e5905f9af8254df2114ad15c2bb7d96cfa9a8b464a58ae8ea3ae70"
)
EXPECTED_RESOLVENT_HASHES = {
    "301": "21b304679d3b77a7b1fae4182e203d8f2652588efffa4a160cccd98ac3e81257",
    "303": "76fa8081c92e58839f60659fa7c9979d9b002fae5408cc30777341d21665acb2",
}


def canonical_pretty(raw: bytes, *, max_bytes: int, label: str) -> Any:
    value = strict_json_loads(raw, max_bytes=max_bytes)
    if raw != canonical_json_bytes(value, pretty=True):
        raise StrictDataError(f"{label} is not canonical pretty JSON")
    return value


def compact_document(raw: bytes, *, max_bytes: int, label: str) -> dict[str, Any]:
    value = strict_json_loads(raw, max_bytes=max_bytes)
    require_canonical_compact_json(raw)
    if type(value) is not dict:
        raise StrictDataError(f"{label} must be a JSON object")
    return value


def relative_to_repo(path: Path) -> str:
    try:
        return str(path.resolve(strict=True).relative_to(REPO.resolve(strict=True)).as_posix())
    except ValueError as exc:
        raise StrictDataError(f"path escapes repository: {path}") from exc


def parse_sha_manifest(raw: bytes, *, expected_entries: int, label: str) -> list[tuple[str, str]]:
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise StrictDataError(f"{label} must have exactly one terminal newline")
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
            raise StrictDataError(f"{label} line grammar mismatch")
        digest, relative = line[:64], line[66:]
        require_sha256(digest, f"{label} entry digest")
        if not safe_relative_path(relative) or relative in seen:
            raise StrictDataError(f"{label} unsafe or duplicate path")
        seen.add(relative)
        rows.append((relative, digest))
    if [path for path, _ in rows] != sorted(seen):
        raise StrictDataError(f"{label} entries are not path-sorted")
    return rows


def manifest_member_paths() -> list[Path]:
    paths: list[Path] = []
    for tag, authority in RELEASES.items():
        project = authority["project"]
        manifest = project / "FULL_PROJECT_HASHES.sha256"
        raw, fingerprint = read_stable(manifest, max_bytes=1_000_000)
        if fingerprint.sha256 != authority["manifest_sha256"]:
            raise StrictDataError(f"{tag} full manifest digest mismatch")
        rows = parse_sha_manifest(
            raw,
            expected_entries=authority["manifest_entries"],
            label=f"{tag} full manifest",
        )
        paths.append(manifest)
        paths.extend(project / relative for relative, _ in rows)
    return paths


@dataclass(frozen=True)
class FileSeal:
    sha256: str
    size_bytes: int
    mode: int
    mtime_ns: int
    device: int
    inode: int


@dataclass(frozen=True)
class DirectorySeal:
    mode: int
    mtime_ns: int
    device: int
    inode: int


def seal_file(path: Path) -> FileSeal:
    raw, fingerprint = read_stable(path, max_bytes=500_000_000)
    metadata = path.stat()
    return FileSeal(
        sha256=sha256_bytes(raw),
        size_bytes=fingerprint.size_bytes,
        mode=fingerprint.mode,
        mtime_ns=fingerprint.mtime_ns,
        device=metadata.st_dev,
        inode=metadata.st_ino,
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
        raise StrictDataError(f"directory changed while being bound: {path}")
    return DirectorySeal(
        mode=stat.S_IMODE(opened.st_mode),
        mtime_ns=opened.st_mtime_ns,
        device=opened.st_dev,
        inode=opened.st_ino,
    )


class SnapshotGuard:
    """Byte/inode snapshot rebound before and after every child process."""

    def __init__(self, paths: Iterable[Path], *, directories: Iterable[Path] = ()):
        normalized = tuple(sorted({path.resolve(strict=True) for path in paths}, key=str))
        self.paths = normalized
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
                    key
                    for key in set(observed_directories) & set(self.expected_directories)
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
            list(command),
            cwd=cwd,
            env=clean_environment(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout,
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
    if not CODE.is_dir() or CODE.is_symlink() or CODE.resolve(strict=True) != CODE:
        raise StrictDataError("C59 code directory must be one real non-symlink directory")
    children = list(CODE.iterdir())
    names = {child.name for child in children}
    if names != CODE_SOURCE_NAMES:
        raise StrictDataError(
            "C59 exact 13-source inventory mismatch; "
            f"missing={sorted(CODE_SOURCE_NAMES-names)} extra={sorted(names-CODE_SOURCE_NAMES)}"
        )
    entries = []
    for name in sorted(CODE_SOURCE_NAMES):
        path = CODE / name
        raw, fingerprint = read_stable(path, max_bytes=5_000_000)
        if len(raw) != fingerprint.size_bytes:
            raise StrictDataError("source stable-read size mismatch")
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": fingerprint.size_bytes,
            }
        )
    return {
        "schema_id": "hcs-c59-source-contract-v1",
        "entry_count": 13,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [f"code/{name}" for name in sorted(CODE_SOURCE_NAMES)],
        "entries": entries,
        "self_reference_policy": "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE",
    }


def verify_full_manifest(tag: str) -> dict[str, Any]:
    authority = RELEASES[tag]
    project: Path = authority["project"]
    manifest = project / "FULL_PROJECT_HASHES.sha256"
    raw, fingerprint = read_stable(manifest, max_bytes=1_000_000)
    if fingerprint.sha256 != authority["manifest_sha256"]:
        raise StrictDataError(f"{tag} full manifest digest mismatch")
    rows = parse_sha_manifest(
        raw,
        expected_entries=authority["manifest_entries"],
        label=f"{tag} full manifest",
    )
    declared = {relative for relative, _ in rows}
    for relative, digest in rows:
        member_raw, member = read_stable(project / relative, max_bytes=500_000_000)
        if member.sha256 != digest or len(member_raw) != member.size_bytes:
            raise StrictDataError(f"{tag} full manifest member mismatch: {relative}")
    live_files: set[str] = set()
    live_directories: set[str] = set()
    special: list[str] = []
    for child in project.rglob("*"):
        relative = str(child.relative_to(project).as_posix())
        if child.is_symlink() or (not child.is_file() and not child.is_dir()):
            special.append(relative)
        elif child.is_file() and relative != "FULL_PROJECT_HASHES.sha256":
            live_files.add(relative)
        elif child.is_dir():
            live_directories.add(relative)
    allowed_directories: set[str] = set()
    for relative in (*declared, "FULL_PROJECT_HASHES.sha256"):
        for parent in Path(relative).parents:
            if str(parent.as_posix()) != ".":
                allowed_directories.add(str(parent.as_posix()))
    if special or live_files != declared or live_directories != allowed_directories:
        raise StrictDataError(
            f"{tag} exact full inventory mismatch; special={special}; "
            f"missing={sorted(declared-live_files)} extra={sorted(live_files-declared)}; "
            f"missing_dirs={sorted(allowed_directories-live_directories)} "
            f"extra_dirs={sorted(live_directories-allowed_directories)}"
        )
    return {
        "entry_count": len(rows),
        "inventory_exact_excluding_self": True,
        "manifest_path": relative_to_repo(manifest),
        "manifest_sha256": fingerprint.sha256,
        "manifest_size_bytes": fingerprint.size_bytes,
    }


def verify_scoped_manifest(tag: str) -> dict[str, Any]:
    authority = RELEASES[tag]
    project: Path = authority["project"]
    path = project / "results/scoped_hash_manifest.json"
    raw, fingerprint = read_stable(path, max_bytes=1_000_000)
    if fingerprint.sha256 != authority["scoped_sha256"]:
        raise StrictDataError(f"{tag} scoped manifest digest mismatch")
    value = canonical_pretty(raw, max_bytes=1_000_000, label=f"{tag} scoped manifest")
    require_exact_keys(
        value,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        f"{tag} scoped manifest",
    )
    if (
        type(value["entry_count"]) is not int
        or value["entry_count"] != len(value["entries"])
        or value["manifest_self_included"] is not False
        or value["status"] != "PREFREEZE_CODE_RESULTS_PASS"
    ):
        raise StrictDataError(f"{tag} scoped manifest status/count mismatch")
    declared: set[str] = set()
    for entry in value["entries"]:
        require_exact_keys(entry, {"path", "sha256", "size_bytes"}, "scoped manifest row")
        relative = entry["path"]
        if not safe_relative_path(relative) or relative in declared:
            raise StrictDataError(f"{tag} scoped manifest path mismatch")
        declared.add(relative)
        member_raw, member = read_stable(project / relative, max_bytes=500_000_000)
        if (
            type(entry["size_bytes"]) is not int
            or entry["size_bytes"] != member.size_bytes
            or entry["sha256"] != member.sha256
            or len(member_raw) != member.size_bytes
        ):
            raise StrictDataError(f"{tag} scoped manifest member mismatch: {relative}")
    live: set[str] = set()
    for root in (project / "code", project / "results"):
        for child in root.rglob("*"):
            if child.is_symlink() or (not child.is_dir() and not child.is_file()):
                raise StrictDataError(f"{tag} scoped tree contains special file")
            if child.is_file():
                relative = str(child.relative_to(project).as_posix())
                if relative != "results/scoped_hash_manifest.json":
                    live.add(relative)
    if live != declared:
        raise StrictDataError(
            f"{tag} scoped inventory mismatch; missing={sorted(declared-live)} extra={sorted(live-declared)}"
        )
    return {
        "entry_count": len(declared),
        "inventory_exact_excluding_self": True,
        "manifest_path": relative_to_repo(path),
        "manifest_sha256": fingerprint.sha256,
        "manifest_size_bytes": fingerprint.size_bytes,
    }


def validate_predecessor_certificate(tag: str) -> tuple[dict[str, Any], dict[str, Any]]:
    authority = RELEASES[tag]
    project: Path = authority["project"]
    certificate_path = project / f"results/{tag.lower()}_certificate.json"
    schema_path = project / f"results/{tag.lower()}_schema.json"
    check_path = project / f"results/{tag.lower()}_check_report.json"
    certificate_raw, certificate_fp = read_stable(certificate_path, max_bytes=5_000_000)
    schema_raw, schema_fp = read_stable(schema_path, max_bytes=1_000_000)
    check_raw, check_fp = read_stable(check_path, max_bytes=2_000_000)
    if (
        certificate_fp.sha256 != authority["certificate_sha256"]
        or schema_fp.sha256 != authority["schema_sha256"]
        or check_fp.sha256 != authority["check_sha256"]
    ):
        raise StrictDataError(f"{tag} certificate/schema/check byte authority mismatch")
    certificate = canonical_pretty(certificate_raw, max_bytes=5_000_000, label=f"{tag} certificate")
    schema = canonical_pretty(schema_raw, max_bytes=1_000_000, label=f"{tag} schema")
    check = canonical_pretty(check_raw, max_bytes=2_000_000, label=f"{tag} check")
    if certificate.get("payload_sha256") != authority["payload_sha256"]:
        raise StrictDataError(f"{tag} payload authority mismatch")
    if certificate["payload_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["payload"])):
        raise StrictDataError(f"{tag} payload digest does not rebind")
    if tag == "C56":
        require_exact_keys(certificate, {"schema", "schema_sha256", "payload", "payload_sha256"}, "C56 certificate")
        if (
            not deep_exact(certificate["schema"], schema)
            or certificate["schema_sha256"] != sha256_bytes(canonical_leaf_bytes(schema))
            or check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        ):
            raise StrictDataError("C56 semantic status/schema binding mismatch")
        carrier = {
            "eliminant_coefficients_d_0_to_27": certificate["payload"]["irreducibility"]["eliminant_coefficients_d_0_to_27"],
            "lex_shape": certificate["payload"]["grassmann_main_chart"]["lex_shape"],
            "line_equations_sparse": certificate["payload"]["grassmann_main_chart"]["line_equations_sparse"],
            "line_class_intersection_matrix": certificate["payload"]["we6"]["line_class_intersection_matrix"],
            "simple_reflection_line_permutations": certificate["payload"]["we6"]["simple_reflection_line_permutations"],
        }
    else:
        require_exact_keys(
            certificate,
            {"canonical_schema_sha256", "paper_status", "payload", "payload_sha256", "schema_descriptor_id", "schema_id", "schema_sha256", "status"},
            "C58 certificate",
        )
        if (
            certificate["schema_sha256"] != schema_fp.sha256
            or certificate["canonical_schema_sha256"] != sha256_bytes(canonical_leaf_bytes(schema))
            or certificate["status"] != "PREFREEZE_CODE_RESULTS_PASS"
            or check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        ):
            raise StrictDataError("C58 semantic status/schema binding mismatch")
        group_raw, group_fp = read_stable(project / "results/c58_group_evidence.json", max_bytes=2_000_000)
        if group_fp.sha256 != authority["group_evidence_sha256"] or not group_raw:
            raise StrictDataError("C58 group evidence authority mismatch")
        carrier = {
            "G3_dual_action_classification": certificate["payload"]["G3_dual_action_classification"],
            "G4_filtered_inertia": certificate["payload"]["G4_filtered_inertia"],
            "G6_global_and_infinity": certificate["payload"]["G6_global_and_infinity"],
            "group_evidence_sha256": group_fp.sha256,
        }
    summary = {
        "candidate_id": tag,
        "certificate_path": relative_to_repo(certificate_path),
        "certificate_sha256": certificate_fp.sha256,
        "certificate_size_bytes": certificate_fp.size_bytes,
        "payload_sha256": certificate["payload_sha256"],
        "schema_path": relative_to_repo(schema_path),
        "schema_sha256": schema_fp.sha256,
        "check_report_path": relative_to_repo(check_path),
        "check_report_sha256": check_fp.sha256,
        "carrier_projection_sha256": sha256_bytes(canonical_leaf_bytes(carrier)),
    }
    return summary, certificate


def batch_c59_section(raw: bytes) -> bytes:
    start = raw.find(b"## HCS-C59:")
    end = raw.find(b"## HCS-C60", start + 1)
    if start < 0 or end < 0 or end <= start:
        raise StrictDataError("C59 Batch section boundaries missing")
    return raw[start:end]


def formal_target_lock() -> dict[str, Any]:
    markdown = {path.name: path for path in C59.glob("*.md")}
    if set(markdown) != FORMAL_MARKDOWN_NAMES:
        raise StrictDataError("C59 exact 13-Markdown formal lock mismatch")
    aggregate_lines = []
    for name in sorted(markdown):
        raw, fingerprint = read_stable(markdown[name], max_bytes=2_000_000)
        if b"NO_BAD_EULER_OR_ROOT_NUMBER" not in raw:
            raise StrictDataError(f"formal firewall missing in {name}")
        aggregate_lines.append(f"{fingerprint.sha256}  {name}\n".encode("ascii"))
    aggregate = sha256_bytes(b"".join(aggregate_lines))
    route_raw, route = read_stable(C59 / "route_a_evaluation.yaml", max_bytes=1_000_000)
    batch_raw, batch = read_stable(BATCH, max_bytes=1_000_000)
    guard_raw, guard = read_stable(GUARD, max_bytes=1_000_000)
    if (
        aggregate != FORMAL_LOCK["markdown_aggregate_sha256"]
        or route.sha256 != FORMAL_LOCK["route_sha256"]
        or batch.sha256 != FORMAL_LOCK["batch_sha256"]
        or guard.sha256 != FORMAL_LOCK["guard_sha256"]
    ):
        raise StrictDataError("C59 frozen formal/Batch/guard authority mismatch")
    for literal in (
        b"TARGET_LOCK_GO", b"THEOREM_TARGET_LOCKED", b"IMPLEMENTATION_PENDING",
        b"FORMAL_HOSTILE_PASS", b"NOT_RELEASED",
    ):
        if literal not in route_raw:
            raise StrictDataError(f"C59 Route status literal missing: {literal!r}")
    if b"NO_BAD_EULER_OR_ROOT_NUMBER" not in route_raw:
        raise StrictDataError("C59 Route semantic firewall mismatch")
    section = batch_c59_section(batch_raw)
    return {
        "formal_target_lock": {
            "markdown_file_count": 13,
            "markdown_aggregate_sha256": aggregate,
            "route_path": relative_to_repo(C59 / "route_a_evaluation.yaml"),
            "route_sha256": route.sha256,
            "route_size_bytes": route.size_bytes,
            "status": "FORMAL_HOSTILE_PASS_IMPLEMENTATION_PENDING",
        },
        "batch_target_lock": {
            "path": relative_to_repo(BATCH),
            "sha256": batch.sha256,
            "size_bytes": batch.size_bytes,
            "c59_section_sha256": sha256_bytes(section),
            "c59_section_size_bytes": len(section),
        },
        "protected_guard": {
            "path": relative_to_repo(GUARD),
            "sha256": guard.sha256,
            "size_bytes": guard.size_bytes,
        },
    }


def git_released_commit_rebind(tag: str, guard: SnapshotGuard) -> None:
    authority = RELEASES[tag]
    commit = authority["release_commit"]
    ancestor = run_bound_child(
        guard,
        ["/usr/bin/git", "merge-base", "--is-ancestor", commit, "HEAD"],
        cwd=REPO,
        timeout=60,
        label=f"{tag} release ancestry",
    )
    if ancestor.stdout:
        raise StrictDataError(f"{tag} ancestry command emitted stdout")
    relative_manifest = str((authority["project"] / "FULL_PROJECT_HASHES.sha256").relative_to(REPO).as_posix())
    committed = run_bound_child(
        guard,
        ["/usr/bin/git", "show", f"{commit}:{relative_manifest}"],
        cwd=REPO,
        timeout=60,
        label=f"{tag} committed manifest",
    )
    live, _ = read_stable(authority["project"] / "FULL_PROJECT_HASHES.sha256", max_bytes=1_000_000)
    if committed.stdout != live:
        raise StrictDataError(f"{tag} release commit does not bind live full manifest")


def rebuild_g0(guard: SnapshotGuard) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    released = []
    certificates: dict[str, dict[str, Any]] = {}
    for tag in ("C56", "C58"):
        git_released_commit_rebind(tag, guard)
        full = verify_full_manifest(tag)
        scoped = verify_scoped_manifest(tag)
        certificate_summary, certificate = validate_predecessor_certificate(tag)
        certificates[tag] = certificate
        authority = RELEASES[tag]
        project: Path = authority["project"]
        live_route = project / "route_a_evaluation.yaml"
        archive = project / authority["archive"]
        live_raw, live_fp = read_stable(live_route, max_bytes=1_000_000)
        archive_raw, archive_fp = read_stable(archive, max_bytes=1_000_000)
        if (
            live_fp.sha256 != authority["route_sha256"]
            or archive_fp.sha256 != authority["route_sha256"]
            or live_raw != archive_raw
        ):
            raise StrictDataError(f"{tag} live/archive Route identity mismatch")
        released.append(
            {
                **certificate_summary,
                "release_commit": authority["release_commit"],
                "release_commit_ancestor_of_current_head": True,
                "full_manifest": full,
                "scoped_manifest": scoped,
                "live_route_path": relative_to_repo(live_route),
                "archive_route_path": relative_to_repo(archive),
                "route_sha256": live_fp.sha256,
                "live_archive_route_identical": True,
            }
        )
    formal = formal_target_lock()
    return (
        {
            "schema_id": "hcs-c59-released-authority-rebind-v1",
            "all_released_full_inventories_rebound": True,
            "fixed_predecessor_paths_only": True,
            "released_predecessors": released,
            **formal,
        },
        certificates,
    )


def executable_file(path: Path, *, label: str) -> Path:
    resolved = path.resolve(strict=True)
    metadata = resolved.stat()
    if not stat.S_ISREG(metadata.st_mode) or not os.access(resolved, os.X_OK):
        raise StrictDataError(f"{label} must be an executable regular file")
    return resolved


def backend_contract(
    math_python: Path,
    gap_path: Path,
    guard: SnapshotGuard,
) -> dict[str, Any]:
    math = executable_file(math_python, label="math Python")
    gap = executable_file(gap_path, label="GAP")
    math_raw, math_fp = read_stable(math, max_bytes=40_000_000)
    gap_raw, gap_fp = read_stable(gap, max_bytes=1_000_000)
    expected_math = EXPECTED_BACKENDS["math"]
    if (
        sha256_bytes(math_raw) != expected_math["executable_sha256"]
        or math_fp.size_bytes != expected_math["executable_size_bytes"]
    ):
        raise StrictDataError("math Python executable bytes changed")
    if (
        sha256_bytes(gap_raw) != EXPECTED_GAP["executable_sha256"]
        or gap_fp.size_bytes != EXPECTED_GAP["executable_size_bytes"]
    ):
        raise StrictDataError("GAP executable bytes changed")

    python_source = (
        "import importlib.metadata,json,sys,flint,sympy,networkx,jsonschema;"
        "assert not sys.flags.optimize;"
        "print(json.dumps({'backend':'FLINT_SYMPY_NETWORKX',"
        "'python':list(sys.version_info[:3]),"
        "'flint':getattr(flint,'__version__','unknown'),"
        "'sympy':sympy.__version__,'networkx':networkx.__version__,"
        "'jsonschema':importlib.metadata.version('jsonschema')},"
        "sort_keys=True,separators=(',',':')))"
    )
    python_runs = [
        run_bound_child(
            guard,
            [str(math), "-s", "-B", "-c", python_source],
            cwd=Path("/"),
            timeout=60,
            label=f"math Python preflight run {index}",
        )
        for index in (1, 2)
    ]
    if python_runs[0].stdout != python_runs[1].stdout:
        raise StrictDataError("math Python preflight is nondeterministic")
    python_value = strict_json_loads(python_runs[0].stdout.strip(), max_bytes=10_000)
    expected_python_value = {
        "backend": "FLINT_SYMPY_NETWORKX",
        "python": expected_math["python"],
        "flint": expected_math["flint"],
        "sympy": expected_math["sympy"],
        "networkx": expected_math["networkx"],
        "jsonschema": expected_math["jsonschema"],
    }
    if not deep_exact(python_value, expected_python_value):
        raise StrictDataError(f"math Python versions changed: {python_value}")

    gap_source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",PackageInfo("ctbllib")[1].Version,"\\n");QUIT;'
    )
    gap_runs = [
        run_bound_child(
            guard,
            [str(gap), "-q", "-c", gap_source],
            cwd=Path("/"),
            timeout=60,
            label=f"GAP preflight run {index}",
        )
        for index in (1, 2)
    ]
    if gap_runs[0].stdout != gap_runs[1].stdout:
        raise StrictDataError("GAP preflight is nondeterministic")
    try:
        gap_fields = gap_runs[0].stdout.decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise StrictDataError("GAP preflight output is not ASCII") from exc
    observed_gap = {
        "resolved_executable": str(gap),
        "executable_sha256": sha256_bytes(gap_raw),
        "executable_size_bytes": gap_fp.size_bytes,
        "gap_version": gap_fields[0] if len(gap_fields) == 4 else "",
        "tomlib_version": gap_fields[1] if len(gap_fields) == 4 else "",
        "smallgrp_version": gap_fields[2] if len(gap_fields) == 4 else "",
        "ctbllib_version": gap_fields[3] if len(gap_fields) == 4 else "",
    }
    if not deep_exact(observed_gap, EXPECTED_GAP):
        raise StrictDataError(f"GAP versions/bytes changed: {observed_gap}")
    return {
        "schema_id": "hcs-c59-backend-contract-v1",
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
    script = CODE / "c59_checker_group.g"
    if script.is_symlink() or not script.is_file():
        raise StrictDataError("fixed checker-owned GAP source is missing")
    runs = [
        run_bound_child(
            guard,
            [str(gap), "-q", str(script)],
            cwd=CODE,
            timeout=900,
            label=f"independent group replay run {index}",
        )
        for index in (1, 2)
    ]
    if runs[0].stdout != runs[1].stdout:
        raise StrictDataError("independent GAP group projection is nondeterministic")
    raw = runs[0].stdout
    require_canonical_compact_json(raw)
    projection = strict_json_loads(raw, max_bytes=MAX_CHILD_STDOUT_BYTES)
    require_exact_keys(
        projection,
        {
            "G2_gassmann_minimality", "G4_global_arithmetic",
            "G5_tom140_local_algebra", "G6_tom206_local_algebra",
            "action", "contract_alignment", "schema_id", "software", "status",
        },
        "independent GAP group projection",
    )
    if (
        projection["schema_id"] != GROUP_PROJECTION_SCHEMA_ID
        or projection["status"] != "PASS"
        or projection["software"]
        != {"gap": "4.11.1", "tomlib": "1.2.9", "smallgrp": "1.4.1", "ctbllib": "1.3.1"}
    ):
        raise StrictDataError("independent GAP group projection identity mismatch")
    return projection, sha256_bytes(raw), len(raw)


def expected_contract_alignment() -> dict[str, Any]:
    return {
        "certificate_payload_top_level_keys": list(PAYLOAD_KEYS),
        "planned_code_inventory": sorted(CODE_SOURCE_NAMES),
        "planned_result_inventory": sorted(RESULT_NAMES),
        "scaled_integral_invariant_notation": "eta_i",
        "scaled_line_coordinate_notation": "alpha_i=L*d_i",
        "scaled_relation": "eta_i=L^2*tilde_eta_i",
        "unscaled_invariant_notation": "tilde_eta_i",
    }


def validate_group_evidence(
    document: dict[str, Any],
    projection: dict[str, Any],
    projection_sha256: str,
    projection_size_bytes: int,
) -> None:
    require_exact_keys(
        document,
        {
            "G2_gassmann_minimality", "G4_global_arithmetic",
            "G5_tom140_local_algebra", "G6_tom206_local_algebra",
            "contract_alignment", "frozen_permutation_arrays",
            "independent_replay", "provenance", "schema_id", "status",
        },
        "C59 group evidence",
    )
    if document["schema_id"] != GROUP_EVIDENCE_SCHEMA_ID or document["status"] != "PASS":
        raise StrictDataError("C59 group evidence identity/status mismatch")
    if not deep_exact(document["contract_alignment"], expected_contract_alignment()):
        raise StrictDataError("C59 group evidence contract alignment mismatch")
    if not deep_exact(projection["contract_alignment"], expected_contract_alignment()):
        raise StrictDataError("independent GAP contract alignment mismatch")
    for gate in (
        "G2_gassmann_minimality", "G4_global_arithmetic",
        "G5_tom140_local_algebra", "G6_tom206_local_algebra",
    ):
        if not deep_exact(document[gate], projection[gate]):
            raise StrictDataError(f"group evidence differs from independent projection: {gate}")
    frozen = document["frozen_permutation_arrays"]
    require_exact_keys(
        frozen,
        {"arrays", "canonical_sha256", "phase1_design_input_read_at_runtime", "phase1_design_input_sha256"},
        "group frozen arrays",
    )
    if (
        frozen["phase1_design_input_read_at_runtime"] is not False
        or frozen["canonical_sha256"] != sha256_bytes(canonical_leaf_bytes(frozen["arrays"]))
        or frozen["canonical_sha256"] != "ff809bc0908b1dfd059df119a767aacaa797ab0a9ad7b638c084e771f6441322"
    ):
        raise StrictDataError("group frozen array authority mismatch")
    replay = document["independent_replay"]
    require_exact_keys(replay, {"checker", "cross_checks", "python_projection"}, "group independent replay")
    checker = replay["checker"]
    require_exact_keys(
        checker,
        {
            "checker_projection_sha256", "checker_projection_size_bytes",
            "checker_source_sha256", "checker_source_size_bytes",
            "gap_executable_sha256", "gap_executable_size_bytes", "two_run_deterministic",
        },
        "group checker report",
    )
    checker_raw, checker_fp = read_stable(CODE / "c59_checker_group.g", max_bytes=1_000_000)
    if (
        checker["checker_projection_sha256"] != projection_sha256
        or checker["checker_projection_size_bytes"] != projection_size_bytes
        or checker["checker_source_sha256"] != checker_fp.sha256
        or checker["checker_source_size_bytes"] != checker_fp.size_bytes
        or checker["gap_executable_sha256"] != EXPECTED_GAP["executable_sha256"]
        or checker["gap_executable_size_bytes"] != EXPECTED_GAP["executable_size_bytes"]
        or checker["two_run_deterministic"] is not True
        or len(checker_raw) != checker_fp.size_bytes
    ):
        raise StrictDataError("group independent replay digest/size mismatch")
    cross = replay["cross_checks"]
    if type(cross) is not dict or not cross or any(value is not True for value in cross.values()):
        raise StrictDataError("group evidence Python/GAP cross-check status mismatch")
    if document["provenance"].get("released_C56_C58_line_arrays_deep_equal") is not True:
        raise StrictDataError("group evidence released line-array binding missing")


def validate_resolvent_evidence(
    document: dict[str, Any],
    c56_certificate: Path,
    c56_manifest: Path,
    guard: SnapshotGuard,
) -> dict[str, Any]:
    require_exact_keys(
        document,
        {"payload", "payload_sha256", "schema_id", "schema_sha256"},
        "C59 resolvent evidence",
    )
    if document["schema_id"] != RESOLVENT_EVIDENCE_SCHEMA_ID:
        raise StrictDataError("C59 resolvent evidence schema id mismatch")
    require_sha256(document["schema_sha256"], "resolvent evidence schema digest")
    require_sha256(document["payload_sha256"], "resolvent evidence payload digest")
    if document["payload_sha256"] != sha256_bytes(canonical_json_bytes(document["payload"])):
        raise StrictDataError("resolvent evidence newline-canonical payload digest mismatch")
    guard.assert_unchanged("before in-process resolver reconstruction")
    try:
        expected = reconstruct_resolvent_payload(c56_certificate, c56_manifest, document["payload"])
    except Exception as exc:
        raise StrictDataError("independent resolver reconstruction failed") from exc
    finally:
        guard.assert_unchanged("after in-process resolver reconstruction")
    if not deep_exact(document["payload"], expected):
        raise StrictDataError("resolvent evidence differs from independent full reconstruction")
    return expected


def artifact_contract(
    group_path: Path,
    group_raw: bytes,
    group_document: dict[str, Any],
    resolvent_path: Path,
    resolvent_raw: bytes,
    resolvent_document: dict[str, Any],
) -> dict[str, Any]:
    group_internal = group_document["independent_replay"]["checker"]["checker_projection_sha256"]
    resolver_internal = resolvent_document["payload_sha256"]
    rows = [
        {
            "path": "results/c59_group_evidence.json",
            "format": "canonical_compact_json",
            "sha256": sha256_bytes(group_raw),
            "size_bytes": len(group_raw),
            "schema_id": GROUP_EVIDENCE_SCHEMA_ID,
            "internal_report_sha256": group_internal,
        },
        {
            "path": "results/c59_resolvent_evidence.json",
            "format": "canonical_compact_json",
            "sha256": sha256_bytes(resolvent_raw),
            "size_bytes": len(resolvent_raw),
            "schema_id": RESOLVENT_EVIDENCE_SCHEMA_ID,
            "internal_report_sha256": resolver_internal,
            "schema_sha256": resolvent_document["schema_sha256"],
        },
    ]
    if group_path.name != ARTIFACT_NAMES[0] or resolvent_path.name != ARTIFACT_NAMES[1]:
        raise StrictDataError("artifact basename mismatch")
    return {
        "artifact_count": 2,
        "artifacts": rows,
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c59-artifact-contract-v1",
    }


def validate_group_g2(gate: dict[str, Any]) -> None:
    require_exact_keys(
        gate,
        {
            "all_350_subgroup_classes", "collision_bucket_indices",
            "durable_field_subgroup_invariants", "exact_11_collision_buckets",
            "full_permutation_character_equality", "minimum_collision_index",
            "table_of_marks_name", "tom_subgroup_class_count",
            "unique_minimum_index320_bucket",
        },
        "G2",
    )
    rows = gate["all_350_subgroup_classes"]
    if type(rows) is not list or len(rows) != 350:
        raise StrictDataError("G2 does not contain all 350 subgroup classes")
    buckets: dict[tuple[int, ...], list[int]] = {}
    degrees: dict[int, int] = {}
    for expected_index, row in enumerate(rows, 1):
        require_exact_keys(
            row,
            {"field_degree", "permutation_character_values", "subgroup_order", "tom_index"},
            "G2 subgroup row",
        )
        if (
            type(row["tom_index"]) is not int
            or row["tom_index"] != expected_index
            or type(row["subgroup_order"]) is not int
            or type(row["field_degree"]) is not int
            or row["subgroup_order"] * row["field_degree"] != 51840
            or type(row["permutation_character_values"]) is not list
            or len(row["permutation_character_values"]) != 25
            or any(type(value) is not int for value in row["permutation_character_values"])
        ):
            raise StrictDataError("G2 subgroup row type/order/character mismatch")
        key = tuple(row["permutation_character_values"])
        buckets.setdefault(key, []).append(expected_index)
        degrees[expected_index] = row["field_degree"]
    collisions = sorted((indices for indices in buckets.values() if len(indices) > 1), key=lambda row: row[0])
    if collisions != EXPECTED_COLLISION_BUCKETS or gate["exact_11_collision_buckets"] != EXPECTED_COLLISION_BUCKETS:
        raise StrictDataError("G2 exact collision buckets mismatch")
    collision_degrees = [degrees[bucket[0]] for bucket in collisions]
    if (
        gate["collision_bucket_indices"] != collision_degrees
        or min(collision_degrees) != 320
        or collision_degrees.count(320) != 1
        or gate["minimum_collision_index"] != 320
        or gate["unique_minimum_index320_bucket"] != [301, 303]
        or gate["tom_subgroup_class_count"] != 350
        or gate["table_of_marks_name"] != "U4(2).2"
        or gate["full_permutation_character_equality"] is not True
    ):
        raise StrictDataError("G2 minimum/full-character summary mismatch")
    fields = gate["durable_field_subgroup_invariants"]
    if type(fields) is not list or len(fields) != 2:
        raise StrictDataError("G2 durable field invariant count mismatch")
    expected = {
        "H301": {"tom": 301, "small": [162, 11], "abelian": [2, 3], "derived": 27},
        "H303": {"tom": 303, "small": [162, 19], "abelian": [2], "derived": 81},
    }
    for field in fields:
        label = field.get("label")
        if label not in expected:
            raise StrictDataError("G2 durable field label mismatch")
        target = expected[label]
        if (
            field.get("tom_locator") != target["tom"]
            or field.get("small_group_id") != target["small"]
            or field.get("abelian_invariants") != target["abelian"]
            or field.get("derived_subgroup_order") != target["derived"]
            or field.get("order") != 162
            or field.get("field_degree") != 320
            or field.get("core_order") != 1
            or field.get("normalizer_order") != 324
            or field.get("support", {}).get("stabilizer_equals_frozen_field_subgroup") is not True
            or field.get("support", {}).get("weyl_orbit_size") != 320
        ):
            raise StrictDataError(f"G2 durable invariant mismatch: {label}")
    if rows[300]["permutation_character_values"] != rows[302]["permutation_character_values"]:
        raise StrictDataError("G2 H301/H303 full character vectors differ")


def validate_g1(gate: dict[str, Any]) -> None:
    require_exact_keys(
        gate,
        {
            "all_27_lines_all_4_equations", "aut_graph_equals_released_w_permutation_set",
            "aut_graph_order", "distinct_values", "factor_degrees",
            "frozen_w_h_arrays_bound", "integral_normalization", "modular_polynomials",
            "multiplyback_proven", "orbit_sizes", "scaled_invariant_name",
            "schlaefli_graph_parameters", "split_prime", "support_component_sizes",
            "support_stabilizers_exact",
        },
        "G1",
    )
    if (
        gate["all_27_lines_all_4_equations"] is not True
        or gate["aut_graph_equals_released_w_permutation_set"] is not True
        or gate["aut_graph_order"] != 51840
        or gate["factor_degrees"] != [[1, 27]]
        or gate["frozen_w_h_arrays_bound"] is not True
        or gate["integral_normalization"] != "alpha_i=L*d_i"
        or gate["scaled_invariant_name"] != "eta"
        or gate["multiplyback_proven"] is not True
        or gate["split_prime"] != 692717
        or gate["support_component_sizes"] != {"301": [27, 27], "303": [81]}
        or gate["support_stabilizers_exact"] != {"301": True, "303": True}
        or gate["orbit_sizes"] != {"301": 320, "303": 320}
        or gate["distinct_values"] != {"301": 320, "303": 320}
        or gate["schlaefli_graph_parameters"] != {"vertices": 27, "edges": 135, "degree": 10}
    ):
        raise StrictDataError("G1 exact primitive-resolvent summary mismatch")
    for label in ("301", "303"):
        row = gate["modular_polynomials"].get(label)
        if row != {"coefficient_count": 321, "sha256": EXPECTED_RESOLVENT_HASHES[label]}:
            raise StrictDataError(f"G1 modular polynomial mismatch: {label}")


def validate_local_table(table: dict[str, Any], *, factor_count: int, expected_rows: list[Any]) -> None:
    require_exact_keys(
        table,
        {
            "complete_collected_rows_n_e_f_d_with_multiplicity", "degree_total",
            "different_exponent_total", "double_coset_count", "e_f_identity_all_rows",
        },
        "complete local table",
    )
    rows = table["complete_collected_rows_n_e_f_d_with_multiplicity"]
    if rows != expected_rows:
        raise StrictDataError("complete local table exact rows mismatch")
    factors = degree = different = 0
    for item in rows:
        if type(item) is not list or len(item) != 2 or type(item[0]) is not list or len(item[0]) != 4:
            raise StrictDataError("complete local row shape mismatch")
        (n, e, f, d), multiplicity = item
        if any(type(value) is not int for value in (n, e, f, d, multiplicity)):
            raise StrictDataError("complete local row integer type mismatch")
        if n != e * f or min(n, e, f, multiplicity) <= 0 or d < 0:
            raise StrictDataError("complete local row n=e*f/positivity mismatch")
        factors += multiplicity
        degree += multiplicity * n
        different += multiplicity * f * d
    if (
        factors != factor_count
        or degree != 320
        or different != 624
        or table["double_coset_count"] != factor_count
        or table["degree_total"] != 320
        or table["different_exponent_total"] != 624
        or table["e_f_identity_all_rows"] is not True
    ):
        raise StrictDataError("complete local table totals mismatch")


ROWS_140_301 = [[[1, 1, 1, 0], 8], [[6, 6, 1, 11], 10], [[9, 9, 1, 18], 8], [[18, 18, 1, 37], 10]]
ROWS_140_303 = [[[2, 2, 1, 1], 4], [[3, 3, 1, 5], 12], [[6, 6, 1, 11], 4], [[9, 9, 1, 18], 4], [[18, 18, 1, 37], 12]]
ROWS_206_301 = [[[2, 1, 2, 0], 4], [[12, 6, 2, 11], 5], [[18, 9, 2, 18], 4], [[36, 18, 2, 37], 5]]
ROWS_206_303 = [[[4, 2, 2, 1], 2], [[6, 3, 2, 5], 6], [[12, 6, 2, 11], 2], [[18, 9, 2, 18], 2], [[36, 18, 2, 37], 6]]


def validate_structure(structure: dict[str, Any], *, branch: int) -> None:
    require_exact_keys(
        structure,
        {
            "deep_Q_unique_in_P_subject_to_D_I_normality",
            "inertia_unique_normal_tom140_in_D", "normality",
            "orders_D_I_P_Q", "tom_D_I_P_Q",
        },
        "local structure",
    )
    if any(
        structure[key] is not True
        for key in ("deep_Q_unique_in_P_subject_to_D_I_normality", "inertia_unique_normal_tom140_in_D")
    ):
        raise StrictDataError("local structure uniqueness mismatch")
    normality = structure["normality"]
    require_exact_keys(
        normality,
        {"I_normal_in_D", "P_normal_in_D", "P_normal_in_I", "Q_normal_in_D", "Q_normal_in_I"},
        "local normality",
    )
    if any(value is not True for value in normality.values()):
        raise StrictDataError("local filtration normality mismatch")
    expected_tom = [140, 140, 72, 7] if branch == 140 else [206, 140, 72, 7]
    expected_orders = [18, 18, 9, 3] if branch == 140 else [36, 18, 9, 3]
    if structure["tom_D_I_P_Q"] != expected_tom or structure["orders_D_I_P_Q"] != expected_orders:
        raise StrictDataError("local structure ToM/order chain mismatch")


def validate_g5_g6(g5: dict[str, Any], g6: dict[str, Any]) -> None:
    require_exact_keys(
        g5,
        {"complete_H301_table", "complete_H303_table", "degree_one_factor_counts_H301_H303", "finite_etale_Q3_algebras_nonisomorphic", "structure"},
        "G5",
    )
    validate_local_table(g5["complete_H301_table"], factor_count=36, expected_rows=ROWS_140_301)
    validate_local_table(g5["complete_H303_table"], factor_count=36, expected_rows=ROWS_140_303)
    validate_structure(g5["structure"], branch=140)
    if g5["degree_one_factor_counts_H301_H303"] != [8, 0] or g5["finite_etale_Q3_algebras_nonisomorphic"] is not True:
        raise StrictDataError("G5 degree-one separator mismatch")
    require_exact_keys(
        g6,
        {"complete_H301_table", "complete_H303_table", "d3_branch_selected", "finite_etale_Q3_algebras_nonisomorphic", "structure", "unramified_quadratic_factor_counts_H301_H303"},
        "G6",
    )
    validate_local_table(g6["complete_H301_table"], factor_count=18, expected_rows=ROWS_206_301)
    validate_local_table(g6["complete_H303_table"], factor_count=18, expected_rows=ROWS_206_303)
    validate_structure(g6["structure"], branch=206)
    if (
        g6["unramified_quadratic_factor_counts_H301_H303"] != [4, 0]
        or g6["finite_etale_Q3_algebras_nonisomorphic"] is not True
        or g6["d3_branch_selected"] is not False
    ):
        raise StrictDataError("G6 unramified-quadratic/branch separator mismatch")


def validate_g4(gate: dict[str, Any]) -> None:
    require_exact_keys(
        gate,
        {
            "common_conductor_exponents_p3_p5_A_B",
            "common_field_discriminant_decimal_no_newline_digits",
            "common_field_discriminant_decimal_no_newline_sha256",
            "common_field_discriminant_factorization",
            "common_field_discriminant_positive", "exact_eight_prime_support",
            "local_orbit_counts_I3_P3_Q3_I5_P5_C3_reflection_Cinf",
            "signature_r1_r2",
        },
        "G4",
    )
    counts = gate["local_orbit_counts_I3_P3_Q3_I5_P5_C3_reflection_Cinf"]
    require_exact_keys(counts, {"H301", "H303", "local_tom_indices"}, "G4 orbit counts")
    if counts["H301"] != EXPECTED_ORBIT_COUNTS or counts["H303"] != EXPECTED_ORBIT_COUNTS:
        raise StrictDataError("G4 orbit-count vectors mismatch")
    if counts["local_tom_indices"] != [140, 72, 7, 147, 23, 6, 2, 5]:
        raise StrictDataError("G4 local ToM locator vector mismatch")
    if gate["common_conductor_exponents_p3_p5_A_B"] != EXPECTED_EXPONENTS:
        raise StrictDataError("G4 conductor exponent vector mismatch")
    # Tame C3/reflection exponents and signature are independently determined
    # from permutation orbit counts; the wild exponents are cross-checked by
    # both complete lower-filtration tables below.
    if 320 - EXPECTED_ORBIT_COUNTS[5] != 192 or 320 - EXPECTED_ORBIT_COUNTS[6] != 160:
        raise StrictDataError("G4 tame conductor derivation failed")
    fixed_real = 2 * EXPECTED_ORBIT_COUNTS[7] - 320
    signature = [fixed_real, (320 - fixed_real) // 2]
    if signature != [16, 152] or gate["signature_r1_r2"] != signature:
        raise StrictDataError("G4 archimedean signature derivation failed")
    if gate["common_field_discriminant_factorization"] != EXPECTED_FACTORIZATION:
        raise StrictDataError("G4 exact discriminant factorization mismatch")
    discriminant = 1
    for prime, exponent in EXPECTED_FACTORIZATION:
        discriminant *= prime ** exponent
    decimal = str(discriminant).encode("ascii")
    if (
        len(decimal) != 11658
        or sha256_bytes(decimal) != EXPECTED_DISCRIMINANT_SHA256
        or gate["common_field_discriminant_decimal_no_newline_digits"] != len(decimal)
        or gate["common_field_discriminant_decimal_no_newline_sha256"] != sha256_bytes(decimal)
        or gate["common_field_discriminant_positive"] is not True
        or gate["exact_eight_prime_support"] != [row[0] for row in EXPECTED_FACTORIZATION]
    ):
        raise StrictDataError("G4 exact signed discriminant/support mismatch")


def derive_g3(g1: dict[str, Any], g2: dict[str, Any]) -> dict[str, Any]:
    fields = {row["label"]: row for row in g2["durable_field_subgroup_invariants"]}
    if set(fields) != {"H301", "H303"}:
        raise StrictDataError("G3 cannot locate the two durable subgroups")
    support_invariance = all(
        fields[label]["support"]["stabilizer_equals_frozen_field_subgroup"] is True
        for label in fields
    )
    degree_counts = g1["distinct_values"]
    full_character_equal = (
        g2["full_permutation_character_equality"] is True
        and g2["all_350_subgroup_classes"][300]["permutation_character_values"]
        == g2["all_350_subgroup_classes"][302]["permutation_character_values"]
    )
    if not support_invariance or degree_counts != {"301": 320, "303": 320} or not full_character_equal:
        raise StrictDataError("G3 bridge premises are absent")
    cores = [fields["H301"]["core_order"], fields["H303"]["core_order"]]
    nonconjugate = fields["H301"]["tom_locator"] != fields["H303"]["tom_locator"]
    nonisomorphic = fields["H301"]["small_group_id"] != fields["H303"]["small_group_id"]
    if cores != [1, 1] or not nonconjugate or not nonisomorphic:
        raise StrictDataError("G3 core/nonconjugacy/nonisomorphism premises fail")
    return {
        "characteristic_zero_conjugate_counts": {"H301": 320, "H303": 320},
        "common_normal_closure": "K",
        "common_normal_closure_from_trivial_cores": True,
        "dedekind_zeta_functions_equal": True,
        "field_degrees": {"H301": 320, "H303": 320},
        "field_isomorphism_would_conjugate_stabilizers": True,
        "fields_nonisomorphic": True,
        "fixed_field_equalities": ["Q(eta_301)=K^H301", "Q(eta_303)=K^H303"],
        "full_permutation_character_identity_used": True,
        "modular_noncollision_lifts_to_characteristic_zero": True,
        "normal_closure_degree": 51840,
        "orbit_sums_invariant_under_frozen_subgroups": True,
        "subgroup_cores": {"H301": 1, "H303": 1},
        "subgroups_nonconjugate": True,
        "subgroups_nonisomorphic": True,
        "written_bridge_required": True,
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


def _base_g7(
    *,
    group_projection_sha256: str,
    group_evidence_sha256: str,
    resolvent_checker_payload_sha256: str,
    resolvent_evidence_sha256: str,
) -> dict[str, Any]:
    return {
        "acyclic_hash_graph": True,
        "all_eight_gates_independently_rebuilt": True,
        "all_evidence_and_source_snapshots_stable_before_certificate_write": True,
        "certificate_root_exact_four_keys": True,
        "evidence_rebound_mutation_count_expected": 8,
        "exact_payload_top_level_key_count": 15,
        "group_checker_projection_sha256": group_projection_sha256,
        "group_evidence_sha256": group_evidence_sha256,
        "independent_check_report_policy": "LATER_CHECK_REPORT_NOT_CERTIFICATE_INPUT",
        "later_manifest_self_excluding": True,
        "payload_scalar_leaf_count": 0,
        "planned_exact_live_code_results_files": 21,
        "planned_result_files": 8,
        "planned_scoped_manifest_entries": 20,
        "planned_source_files": 13,
        "producer_checker_theorem_call_graphs_disjoint": True,
        "resolvent_checker_payload_sha256": resolvent_checker_payload_sha256,
        "resolvent_evidence_sha256": resolvent_evidence_sha256,
        "schema_scalar_leaf_count": 0,
        "strict_exact_key_and_type_checks": True,
        "strict_parser_required": True,
        "structural_mutation_count_expected": 12,
        "type_mutation_count_expected": 0,
        "value_mutation_count_expected": 0,
    }


def expected_payload(
    source_contract: dict[str, Any],
    g0: dict[str, Any],
    artifact_contract_value: dict[str, Any],
    resolver_payload: dict[str, Any],
    group_evidence: dict[str, Any],
    backend_contract_value: dict[str, Any],
    group_projection_sha256: str,
    group_evidence_sha256: str,
    resolvent_evidence_sha256: str,
) -> dict[str, Any]:
    """Return the exact 15-key certificate payload.

    This is the stable integration signature for the C59 release scaffold.
    Every argument is an already independently rebound value; no path is
    certificate-selected and no producer theorem helper is called here.
    """
    require_sha256(group_projection_sha256, "group projection digest")
    require_sha256(group_evidence_sha256, "group evidence digest")
    require_sha256(resolvent_evidence_sha256, "resolvent evidence digest")
    g1 = deepcopy(resolver_payload["G1_primitive_orbit_resolvents"])
    g2 = deepcopy(group_evidence["G2_gassmann_minimality"])
    g4 = deepcopy(group_evidence["G4_global_arithmetic"])
    g5 = deepcopy(group_evidence["G5_tom140_local_algebra"])
    g6 = deepcopy(group_evidence["G6_tom206_local_algebra"])
    validate_g1(g1)
    validate_group_g2(g2)
    validate_g4(g4)
    validate_g5_g6(g5, g6)
    g3 = derive_g3(g1, g2)
    resolver_checker_payload_sha256 = sha256_bytes(canonical_json_bytes(resolver_payload))
    g7 = _base_g7(
        group_projection_sha256=group_projection_sha256,
        group_evidence_sha256=group_evidence_sha256,
        resolvent_checker_payload_sha256=resolver_checker_payload_sha256,
        resolvent_evidence_sha256=resolvent_evidence_sha256,
    )
    payload: dict[str, Any] = {
        "artifact_contract": deepcopy(artifact_contract_value),
        "G0_released_authority_rebind": deepcopy(g0),
        "G1_primitive_orbit_resolvents": g1,
        "G2_gassmann_minimality": g2,
        "G3_fixed_fields_and_zeta": g3,
        "G4_global_arithmetic": g4,
        "G5_tom140_local_algebra": g5,
        "G6_tom206_local_algebra": g6,
        "G7_independence_scope_release": g7,
        "written_bridges": {key: True for key in sorted(WRITTEN_BRIDGE_KEYS)},
        "backend_contract": deepcopy(backend_contract_value),
        "source_contract": deepcopy(source_contract),
        "scope_nonclaims": {key: False for key in sorted(SCOPE_NONCLAIM_KEYS)},
        "nonresults": {
            "characteristic_zero_resolvents": "UNEXPANDED_ORBIT_PRODUCTS_ONLY",
            "discriminant_authority": "PERMUTATION_CONDUCTORS_NOT_POLYNOMIAL_DISCRIMINANTS",
            "local_row_scope": "FACTOR_DEGREE_SEPARATOR_NOT_LOCAL_FIELD_CLASSIFICATION",
            "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "unsupported_machine_dependencies": ["PARI", "Singular"],
        },
        "status": {
            "candidate_id": "HCS-C59",
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "paper_status": "PAPER_PENDING",
            "promotion_authorized": False,
            "release_status": "NOT_RELEASED",
            "theorem_gate_count": 8,
        },
    }
    if set(payload) != set(PAYLOAD_KEYS):
        raise StrictDataError("C59 payload does not have the exact 15-key contract")
    payload_leaves = scalar_leaf_count(payload)
    payload["G7_independence_scope_release"]["payload_scalar_leaf_count"] = payload_leaves
    temporary_schema = schema_descriptor(payload)
    schema_leaves = scalar_leaf_count(temporary_schema)
    payload["G7_independence_scope_release"]["schema_scalar_leaf_count"] = schema_leaves
    scalar_mutations = payload_leaves + schema_leaves + 2
    payload["G7_independence_scope_release"]["value_mutation_count_expected"] = scalar_mutations
    payload["G7_independence_scope_release"]["type_mutation_count_expected"] = scalar_mutations
    if scalar_leaf_count(payload) != payload_leaves or scalar_leaf_count(schema_descriptor(payload)) != schema_leaves:
        raise StrictDataError("C59 payload/schema scalar-count fixed point failed")
    return payload


_EXPECTED_DIGEST_CACHE: dict[int, tuple[Any, str]] = {}


def expected_semantic_digest(value: Any) -> str:
    """Cache the digest of an immutable checker-owned expected object."""
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
        "C59 certificate root",
    )
    if type(sidecar_schema) is not dict:
        raise StrictDataError("C59 schema sidecar must be an object")
    require_exact_keys(sidecar_schema, set(expected_schema), "C59 schema sidecar")
    if type(certificate["schema_sha256"]) is not str or type(certificate["payload_sha256"]) is not str:
        raise StrictDataError("C59 certificate digest leaves must be strings")
    require_sha256(certificate["schema_sha256"], "C59 schema digest")
    require_sha256(certificate["payload_sha256"], "C59 payload digest")
    if not deep_exact(certificate["schema"], sidecar_schema):
        raise StrictDataError("embedded schema differs from c59_schema.json")
    expected_schema_digest = expected_semantic_digest(expected_schema)
    expected_payload_digest = expected_semantic_digest(expected)
    if certificate["schema_sha256"] != expected_schema_digest:
        raise StrictDataError("schema digest differs from independent expected schema")
    if certificate["payload_sha256"] != expected_payload_digest:
        raise StrictDataError("payload digest differs from independent expected payload")
    if not deep_exact(certificate["payload"], expected):
        raise StrictDataError("full C59 semantic payload rebuild mismatch")
    if not deep_exact(sidecar_schema, expected_schema):
        raise StrictDataError("full C59 schema descriptor rebuild mismatch")
    if certificate["schema_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["schema"])):
        raise StrictDataError("compact embedded-schema digest mismatch")
    if certificate["payload_sha256"] != sha256_bytes(canonical_leaf_bytes(certificate["payload"])):
        raise StrictDataError("compact payload digest mismatch")


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
    raise StrictDataError("unsupported value mutation leaf")


def type_mutation(value: Any) -> Any:
    if type(value) is bool:
        return 0
    if type(value) is int:
        return False
    if type(value) is str:
        return 0
    if value is None:
        return False
    raise StrictDataError("unsupported type mutation leaf")


def canonical_bytes_and_leaf_spans(value: Any) -> tuple[bytes, dict[tuple[Any, ...], tuple[int, int]]]:
    """Serialize once and record every scalar byte interval.

    The mutation sweep can then recompute each self-consistent SHA-256 with
    three streaming updates instead of reserializing the 10k-leaf payload.
    The constructed bytes are checked against ``canonical_leaf_bytes`` before
    any mutation is trusted.
    """
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
        raise StrictDataError("canonical scalar-span serialization disagrees with exact I/O")
    return raw, spans


def rebound_digest(
    original_raw: bytes,
    span: tuple[int, int],
    replacement: Any,
) -> str:
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
    raise StrictDataError(f"C59 verifier accepted hostile mutation: {label}")


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
            set_path(schema_mutant, path, mutator(original))
            set_path(schema_certificate["schema"], path, get_path(schema_mutant, path))
            schema_certificate["schema_sha256"] = sha256_bytes(
                canonical_leaf_bytes(schema_mutant)
            )
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
            expect_core_rejection(
                root_mutant, schema, expected, expected_schema, f"root-{kind}:{key}"
            )
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
    mutant = deepcopy(certificate); mutant["payload"]["G3_fixed_fields_and_zeta"] = []; mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-gate-container", mutant, schema))
    mutant = deepcopy(certificate); mutant["payload"]["G3_fixed_fields_and_zeta"]["fixed_field_equalities"].pop(); mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
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
    mutant = deepcopy(certificate)
    structural.append(("schema-sidecar-container", mutant, []))
    if len(structural) != 12:
        raise RuntimeError("structural mutation inventory changed")
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
        raise StrictDataError("mutation sweep count differs from certificate G7 contract")
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


def evidence_rebound_suite(
    certificate: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
    group_document: dict[str, Any],
    group_projection: dict[str, Any],
    resolver_document: dict[str, Any],
    resolver_expected: dict[str, Any],
) -> dict[str, int]:
    rejected = 0

    resolver_mutations = []
    mutant = deepcopy(resolver_document); mutant["payload"]["G1_primitive_orbit_resolvents"]["split_prime"] += 2
    resolver_mutations.append(mutant)
    mutant = deepcopy(resolver_document); mutant["payload"]["unknown"] = False
    resolver_mutations.append(mutant)
    for mutant in resolver_mutations:
        mutant["payload_sha256"] = sha256_bytes(canonical_json_bytes(mutant["payload"]))
        if deep_exact(mutant["payload"], resolver_expected):
            raise StrictDataError("resolver evidence mutation was ineffective")
        mutant_raw = canonical_json_bytes(mutant)
        rebound_certificate = deepcopy(certificate)
        artifact_row = rebound_certificate["payload"]["artifact_contract"]["artifacts"][1]
        artifact_row["sha256"] = sha256_bytes(mutant_raw)
        artifact_row["size_bytes"] = len(mutant_raw)
        artifact_row["internal_report_sha256"] = mutant["payload_sha256"]
        rebound_certificate["payload"]["G1_primitive_orbit_resolvents"] = deepcopy(
            mutant["payload"].get("G1_primitive_orbit_resolvents", {})
        )
        rebound_certificate["payload_sha256"] = sha256_bytes(
            canonical_leaf_bytes(rebound_certificate["payload"])
        )
        expect_core_rejection(
            rebound_certificate, schema, expected, expected_schema,
            "self-consistent-resolver-evidence-rebound",
        )
        rejected += 1

    group_mutations = []
    mutant = deepcopy(group_document); mutant["G2_gassmann_minimality"]["all_350_subgroup_classes"].pop()
    group_mutations.append(("G2_gassmann_minimality", mutant))
    mutant = deepcopy(group_document); mutant["G4_global_arithmetic"]["common_conductor_exponents_p3_p5_A_B"][0] += 1
    group_mutations.append(("G4_global_arithmetic", mutant))
    mutant = deepcopy(group_document); mutant["G5_tom140_local_algebra"]["complete_H301_table"]["degree_total"] += 1
    group_mutations.append(("G5_tom140_local_algebra", mutant))
    mutant = deepcopy(group_document); mutant["G6_tom206_local_algebra"]["d3_branch_selected"] = True
    group_mutations.append(("G6_tom206_local_algebra", mutant))
    mutant = deepcopy(group_document); mutant["unknown"] = False
    group_mutations.append(("root", mutant))
    for gate, mutant in group_mutations:
        mutant_raw = canonical_json_bytes(mutant)
        rebound_certificate = deepcopy(certificate)
        artifact_row = rebound_certificate["payload"]["artifact_contract"]["artifacts"][0]
        artifact_row["sha256"] = sha256_bytes(mutant_raw)
        artifact_row["size_bytes"] = len(mutant_raw)
        if gate == "root":
            try:
                require_exact_keys(mutant, set(group_document), "mutated group evidence")
            except StrictDataError:
                pass
            else:
                raise StrictDataError("group root mutation was accepted")
        elif deep_exact(mutant[gate], group_projection[gate]):
            raise StrictDataError(f"group evidence mutation was ineffective: {gate}")
        else:
            rebound_certificate["payload"][gate] = deepcopy(mutant[gate])
        rebound_certificate["payload_sha256"] = sha256_bytes(
            canonical_leaf_bytes(rebound_certificate["payload"])
        )
        expect_core_rejection(
            rebound_certificate, schema, expected, expected_schema,
            f"self-consistent-group-evidence-rebound:{gate}",
        )
        rejected += 1

    mutant_certificate = deepcopy(certificate)
    mutant_certificate["payload"]["artifact_contract"]["artifacts"][0]["sha256"] = "0" * 64
    mutant_certificate["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant_certificate["payload"]))
    expect_core_rejection(mutant_certificate, schema, expected, expected_schema, "artifact-self-consistent-rebound")
    rejected += 1
    if rejected != expected["G7_independence_scope_release"]["evidence_rebound_mutation_count_expected"]:
        raise StrictDataError("evidence rebound mutation count mismatch")
    return {"self_consistent_evidence_rebound_mutations_rejected": rejected}


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
            raise StrictDataError("canonical compact parser accepted noncanonical bytes")
    huge = b'{"a":' + b"9" * 100_000 + b"}"
    value = strict_json_loads(huge, max_bytes=len(huge))
    if type(value["a"]) is not int:
        raise StrictDataError("canonical 100k-digit integer was not accepted")
    return {
        "canonical_100k_digit_integer_accepted": 1,
        "invalid_or_noncanonical_cases_rejected": rejected,
    }


def literal_dictionary_and_import_audit() -> dict[str, int | bool]:
    dictionary_nodes = 0
    for name in sorted(CODE_SOURCE_NAMES):
        if not name.endswith(".py"):
            continue
        raw, _ = read_stable(CODE / name, max_bytes=5_000_000)
        try:
            tree = ast.parse(raw.decode("utf-8", errors="strict"), filename=name)
        except (SyntaxError, UnicodeDecodeError) as exc:
            raise StrictDataError(f"C59 source parse failed: {name}") from exc
        for node in ast.walk(tree):
            if type(node) is ast.Dict:
                keys = [
                    key.value for key in node.keys
                    if type(key) is ast.Constant and type(key.value) is str
                ]
                if len(keys) != len(set(keys)):
                    raise StrictDataError(f"duplicate literal dictionary key in {name}")
                dictionary_nodes += 1

    def local_imports(name: str) -> set[str]:
        raw, _ = read_stable(CODE / name, max_bytes=5_000_000)
        tree = ast.parse(raw.decode("utf-8", errors="strict"), filename=name)
        result: set[str] = set()
        for node in ast.walk(tree):
            if type(node) is ast.Import:
                result.update(alias.name.split(".")[0] for alias in node.names if alias.name.startswith("c59_"))
            elif type(node) is ast.ImportFrom and node.module and node.module.startswith("c59_"):
                result.add(node.module.split(".")[0])
        return result

    checker_imports = local_imports("c59_checker.py")
    producer_imports = local_imports("c59_producer.py")
    if checker_imports != {"c59_exact", "c59_pipeline", "c59_checker_resolvent"}:
        raise StrictDataError(f"checker local import boundary mismatch: {checker_imports}")
    if not producer_imports <= {"c59_exact", "c59_pipeline", "c59_group", "c59_resolvent"}:
        raise StrictDataError(f"producer local import boundary mismatch: {producer_imports}")
    forbidden_checker = {"c59_producer", "c59_group", "c59_resolvent"}
    if checker_imports & forbidden_checker:
        raise StrictDataError("checker imports a producer theorem helper")
    return {
        "literal_dictionary_nodes_checked": dictionary_nodes,
        "checker_exact_local_import_set": True,
        "producer_checker_theorem_import_sets_disjoint": True,
    }


def validate_fixed_paths(arguments: argparse.Namespace) -> tuple[Path, Path, Path, Path, Path, Path]:
    mapping = {
        arguments.certificate: "c59_certificate.json",
        arguments.schema: "c59_schema.json",
        arguments.group_evidence: "c59_group_evidence.json",
        arguments.resolvent_evidence: "c59_resolvent_evidence.json",
        arguments.output: "c59_check_report.json",
    }
    if any(path.name != basename for path, basename in mapping.items()):
        raise StrictDataError("C59 certificate/schema/evidence/output basenames are fixed")
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
        or re.fullmatch(r"\.c59-stage-[A-Za-z0-9]{8}", parent.name) is None
    ):
        raise StrictDataError(
            "C59 inputs/output must share one canonical real .c59-stage-* direct child of PROJECT/results"
        )
    parent_seal = seal_directory(parent)
    inputs = absolute[:4]
    inodes: set[tuple[int, int]] = set()
    for path in inputs:
        raw, _ = read_stable(path, max_bytes=MAX_RESOLVENT_EVIDENCE_BYTES)
        metadata = path.stat()
        inode = (metadata.st_dev, metadata.st_ino)
        if inode in inodes or metadata.st_nlink != 1 or not raw:
            raise StrictDataError("C59 inputs hardlink/link-count/empty-file firewall failed")
        inodes.add(inode)
    if seal_directory(parent) != parent_seal:
        raise StrictDataError("C59 stage parent changed during path validation")
    return (*absolute, parent)


def protected_paths(
    certificate: Path,
    schema: Path,
    group_evidence: Path,
    resolvent_evidence: Path,
    math_python: Path,
    gap_path: Path,
) -> list[Path]:
    paths = [CODE / name for name in sorted(CODE_SOURCE_NAMES)]
    paths.extend(manifest_member_paths())
    paths.extend([certificate, schema, group_evidence, resolvent_evidence])
    paths.extend(C59 / name for name in sorted(FORMAL_MARKDOWN_NAMES))
    paths.extend([C59 / "route_a_evaluation.yaml", BATCH, GUARD])
    paths.extend([math_python.resolve(strict=True), gap_path.resolve(strict=True)])
    return paths


def rebind_raw_inputs(
    certificate: Path,
    schema: Path,
    group_evidence: Path,
    resolvent_evidence: Path,
    originals: tuple[bytes, bytes, bytes, bytes],
) -> None:
    paths = (certificate, schema, group_evidence, resolvent_evidence)
    for path, expected_raw in zip(paths, originals):
        raw, _ = read_stable(path, max_bytes=MAX_RESOLVENT_EVIDENCE_BYTES)
        if raw != expected_raw:
            raise StrictDataError(f"C59 input changed during replay: {path.name}")


def self_test() -> None:
    parser = strict_parser_cases()
    payload = {key: {"sentinel": True} for key in PAYLOAD_KEYS}
    payload["G3_fixed_fields_and_zeta"] = {"fixed_field_equalities": ["a", "b"], "sentinel": True}
    schema = schema_descriptor(payload)
    certificate = {
        "schema": deepcopy(schema),
        "schema_sha256": sha256_bytes(canonical_leaf_bytes(schema)),
        "payload": deepcopy(payload),
        "payload_sha256": sha256_bytes(canonical_leaf_bytes(payload)),
    }
    core_verify(certificate, schema, payload, schema)
    # The full sweep's count contract belongs to the theorem payload.  For a
    # synthetic smoke test, temporarily install the exactly derived counters.
    payload["G7_independence_scope_release"] = {
        "value_mutation_count_expected": 0,
        "type_mutation_count_expected": 0,
        "structural_mutation_count_expected": 12,
    }
    schema = schema_descriptor(payload)
    count = scalar_leaf_count(payload) + scalar_leaf_count(schema) + 2
    payload["G7_independence_scope_release"]["value_mutation_count_expected"] = count
    payload["G7_independence_scope_release"]["type_mutation_count_expected"] = count
    schema = schema_descriptor(payload)
    certificate = {
        "schema": deepcopy(schema),
        "schema_sha256": sha256_bytes(canonical_leaf_bytes(schema)),
        "payload": deepcopy(payload),
        "payload_sha256": sha256_bytes(canonical_leaf_bytes(payload)),
    }
    rebound = verifier_rebound_sweep(certificate, schema, payload, schema)
    result = {
        "status": "SELF_TEST_ONLY_NO_THEOREM",
        "production_exact_13_inventory_bypassed": False,
        "strict_parser_cases": parser,
        "synthetic_rebound": rebound,
    }
    sys.stdout.buffer.write(canonical_json_bytes(result))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, nargs="?")
    parser.add_argument("--schema", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--group-evidence", type=Path)
    parser.add_argument("--resolvent-evidence", type=Path)
    parser.add_argument("--math-python", type=Path, default=Path("/root/miniconda3/bin/python3"))
    parser.add_argument("--gap", type=Path, default=Path("/usr/bin/gap"))
    parser.add_argument("--self-test", action="store_true")
    arguments = parser.parse_args()
    reject_optimized_python()
    if arguments.self_test:
        if any(
            value is not None
            for value in (
                arguments.certificate, arguments.schema, arguments.output,
                arguments.group_evidence, arguments.resolvent_evidence,
            )
        ):
            raise StrictDataError("--self-test accepts no production paths")
        self_test()
        return
    if any(
        value is None
        for value in (
            arguments.certificate, arguments.schema, arguments.output,
            arguments.group_evidence, arguments.resolvent_evidence,
        )
    ):
        parser.error("production verification requires CERT and all four path options")

    # This check intentionally precedes output preparation: an incomplete
    # staged source tree cannot delete or rewrite even a stale report.
    source_before = exact_source_contract()
    certificate_path, schema_path, group_path, resolver_path, output_path, stage_parent = validate_fixed_paths(arguments)
    certificate_raw, certificate_fp = read_stable(certificate_path, max_bytes=MAX_CERTIFICATE_BYTES)
    schema_raw, schema_fp = read_stable(schema_path, max_bytes=MAX_SCHEMA_BYTES)
    group_raw, group_fp = read_stable(group_path, max_bytes=MAX_GROUP_EVIDENCE_BYTES)
    resolver_raw, resolver_fp = read_stable(resolver_path, max_bytes=MAX_RESOLVENT_EVIDENCE_BYTES)
    certificate = canonical_pretty(certificate_raw, max_bytes=MAX_CERTIFICATE_BYTES, label="C59 certificate")
    schema = canonical_pretty(schema_raw, max_bytes=MAX_SCHEMA_BYTES, label="C59 schema")
    group_document = compact_document(group_raw, max_bytes=MAX_GROUP_EVIDENCE_BYTES, label="C59 group evidence")
    resolver_document = compact_document(resolver_raw, max_bytes=MAX_RESOLVENT_EVIDENCE_BYTES, label="C59 resolvent evidence")

    protected = protected_paths(
        certificate_path, schema_path, group_path, resolver_path,
        arguments.math_python, arguments.gap,
    )
    (output,) = prepare_output_targets((output_path,), protected=protected)
    guard = SnapshotGuard(protected, directories=(stage_parent,))
    originals = (certificate_raw, schema_raw, group_raw, resolver_raw)
    try:
        backends = backend_contract(arguments.math_python, arguments.gap, guard)
        g0, _ = rebuild_g0(guard)
        group_projection, group_projection_sha256, group_projection_size = run_group_projection(arguments.gap, guard)
        validate_group_evidence(group_document, group_projection, group_projection_sha256, group_projection_size)
        resolver_expected = validate_resolvent_evidence(
            resolver_document,
            C56 / "results/c56_certificate.json",
            C56 / "FULL_PROJECT_HASHES.sha256",
            guard,
        )
        artifacts = artifact_contract(
            group_path, group_raw, group_document,
            resolver_path, resolver_raw, resolver_document,
        )
        expected = expected_payload(
            source_before,
            g0,
            artifacts,
            resolver_expected,
            group_document,
            backends,
            group_projection_sha256,
            group_fp.sha256,
            resolver_fp.sha256,
        )
        expected_schema = schema_descriptor(expected)
        core_verify(certificate, schema, expected, expected_schema)
        source_audit = literal_dictionary_and_import_audit()
        parser_report = strict_parser_cases()
        rebound = verifier_rebound_sweep(certificate, schema, expected, expected_schema)
        evidence_rebound = evidence_rebound_suite(
            certificate, schema, expected, expected_schema,
            group_document, group_projection, resolver_document, resolver_expected,
        )

        if not deep_exact(source_before, exact_source_contract()):
            raise StrictDataError("C59 source contract changed during checker replay")
        rebind_raw_inputs(certificate_path, schema_path, group_path, resolver_path, originals)
        guard.assert_unchanged("after all semantic and mutation replay")
        final_g0, _ = rebuild_g0(guard)
        if not deep_exact(g0, final_g0):
            raise StrictDataError("C56/C58/C59 authority changed during checker replay")

        report = {
            "schema_id": CHECK_REPORT_SCHEMA_ID,
            "status": "PREFREEZE_CODE_RESULTS_PASS",
            "result": "PASS_PREFREEZE_CODE_RESULTS",
            "certificate": {
                "path": "results/c59_certificate.json",
                "sha256": certificate_fp.sha256,
                "size_bytes": certificate_fp.size_bytes,
                "payload_sha256": certificate["payload_sha256"],
            },
            "schema_file": {
                "path": "results/c59_schema.json",
                "sha256": schema_fp.sha256,
                "size_bytes": schema_fp.size_bytes,
                "compact_embedded_schema_sha256": certificate["schema_sha256"],
                "parsed_deep_equal_embedded_schema": True,
            },
            "evidence": {
                "group_sha256": group_fp.sha256,
                "group_size_bytes": group_fp.size_bytes,
                "group_projection_sha256": group_projection_sha256,
                "resolvent_sha256": resolver_fp.sha256,
                "resolvent_size_bytes": resolver_fp.size_bytes,
                "resolvent_payload_sha256": resolver_document["payload_sha256"],
            },
            "source_contract_sha256": sha256_bytes(canonical_leaf_bytes(source_before)),
            "g0_released_authority_sha256": sha256_bytes(canonical_leaf_bytes(g0)),
            "executed_gates": [f"G{index}" for index in range(8)],
            "gate_payload_sha256": {
                f"G{index}": sha256_bytes(canonical_leaf_bytes(expected[key]))
                for index, key in enumerate(
                    (
                        "G0_released_authority_rebind", "G1_primitive_orbit_resolvents",
                        "G2_gassmann_minimality", "G3_fixed_fields_and_zeta",
                        "G4_global_arithmetic", "G5_tom140_local_algebra",
                        "G6_tom206_local_algebra", "G7_independence_scope_release",
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
            "paper_status": "PAPER_PENDING",
            "release_status": "NOT_RELEASED",
            "promotion_authorized": False,
        }
        report_raw = canonical_json_bytes(report, pretty=True)

        # Final closure is intentionally adjacent to the only checker write.
        if not deep_exact(source_before, exact_source_contract()):
            raise StrictDataError("C59 source changed before report write")
        rebind_raw_inputs(certificate_path, schema_path, group_path, resolver_path, originals)
        guard.assert_unchanged("immediately before independent report write")
        atomic_write(output, report_raw)
    except BaseException:
        if output.exists() and output.is_file() and not output.is_symlink():
            output.unlink()
        raise
    print("C59 CHECK PASS PREFREEZE")
    print("theorem_gates=8")
    print(f"payload_scalar_leaves={scalar_leaf_count(expected)}")
    print(f"rebound_mutations={rebound['total_certificate_mutations_rejected']}")


if __name__ == "__main__":
    main()
