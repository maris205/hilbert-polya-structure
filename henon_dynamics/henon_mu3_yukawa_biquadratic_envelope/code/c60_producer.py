#!/usr/bin/env python3
"""Assemble the strict integrated HCS-C60 PREFREEZE certificate.

The group and primitive-resolvent evidence documents are immutable inputs.
This producer validates their complete source-owned schemas and then rebuilds
G1--G6 leaf by leaf, including every cross-lane convention needed by the
theorem.  It independently rebinds the released C59 project, the final C60
formal-input lock, source inventory, and executable backends before and after
assembly.  Selection aids are never runtime inputs or theorem authority.
"""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
from typing import Any, Iterable, Sequence

import c60_exact
import c60_group
import c60_pipeline
import c60_resolvent


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
if (
    CODE.name == "code"
    and PROJECT.name == "henon_mu3_yukawa_biquadratic_envelope"
    and PROJECT.parent.name == "henon_dynamics"
):
    REPO = PROJECT.parents[1]
else:
    # A staged source may be imported for pure fixture tests, but repository
    # assembly must fail closed until the source occupies its canonical path.
    REPO = Path("/__C60_STAGED_SOURCE_HAS_NO_REPOSITORY_AUTHORITY__")
    PROJECT = REPO / "henon_dynamics/henon_mu3_yukawa_biquadratic_envelope"
    CODE = PROJECT / "code"
RESULTS = PROJECT / "results"
BATCH = REPO / "henon_dynamics/BATCH_PLAN_C57_C61.md"
GUARD = REPO / "henon_dynamics/codex_prompt.md"
ROUTE = PROJECT / "route_a_evaluation.yaml"
C59_PROJECT = REPO / "henon_dynamics/henon_mu3_yukawa_gassmann_twins"
C59_ROUTE = C59_PROJECT / "route_a_evaluation.yaml"
C59_ROUTE_ARCHIVE = (
    C59_PROJECT / "evaluations/route_a/HCS-C59/20260816T000000Z.yaml"
)
C59_FULL_MANIFEST = C59_PROJECT / "FULL_PROJECT_HASHES.sha256"
C59_SCOPED_MANIFEST = C59_PROJECT / "results/scoped_hash_manifest.json"
C59_CERTIFICATE = C59_PROJECT / "results/c59_certificate.json"
C59_SCHEMA = C59_PROJECT / "results/c59_schema.json"
C59_CHECK_REPORT = C59_PROJECT / "results/c59_check_report.json"
C59_GROUP_EVIDENCE = C59_PROJECT / "results/c59_group_evidence.json"
C59_RESOLVENT_EVIDENCE = C59_PROJECT / "results/c59_resolvent_evidence.json"

CODE_FILES = (
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
)
RESULT_FILES = (
    "RESULTS.md",
    "TEST_REPORT.md",
    "c60_certificate.json",
    "c60_check_report.json",
    "c60_group_evidence.json",
    "c60_resolvent_evidence.json",
    "c60_schema.json",
    "scoped_hash_manifest.json",
)
FORMAL_FILES = (
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
)
ARTIFACT_NAMES = (
    "c60_group_evidence.json",
    "c60_resolvent_evidence.json",
)
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
SCOPE_NONCLAIM_KEYS = (
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
)
WRITTEN_BRIDGE_KEYS = (
    "released_C59_transport_to_C60_fixed_fields",
    "orbit_noncollision_to_primitive_fixed_fields",
    "coefficient_orbit_partitions_to_degree_two_obstruction",
    "subgroup_lattice_to_biquadratic_and_automorphisms",
    "v4_character_relation_to_zeta_identity",
    "conductors_to_signed_absolute_and_relative_discriminants",
    "double_cosets_to_relative_local_towers_and_tameness",
)

# Final target-lock input tuple.  These are source-owned expectations, never
# values selected by a certificate or by command-line paths.
FORMAL_PACKAGE_SHA256 = "fd76237963d385b79b10b7ea13477173b2cf17261fc47d5b43697379d9b012ca"
ROUTE_SHA256 = "2c7dc6a6f5f9fbe2d69c73e51a6e7e6aabad52fe516be8db17d3e1c305d94d77"
BATCH_SHA256 = "bd2a4881e636e18efd0d9917b99ba84b01c7507d6dcff0cefe28f5e5a3661cc3"
GUARD_SHA256 = "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead"
TARGET_LOCK_INPUT_LEDGER_SHA256 = "88c467d0e856b334ed7b0e7ef10123d94cbcfe68310c461e234a710b114cab98"
G0_REBOUND_SHA256 = "0512db556004edde7c19176bbb35375beaeba89301da53902d5c5d98001cb8a8"

C59_IMPLEMENTATION_COMMIT = "6c806120f17dab2e7b0bca37fcc156dfc459a4b7"
C59_RELEASE_COMMIT = "961c45f4b0c66ec94d2f069fd9ecc9d4b529d03a"
C59_ROUTE_SHA256 = "fab227cc8e83155e39793d665ea721e46522d5beee77a113a19379b64b2130c5"
C59_FULL_MANIFEST_SHA256 = "4d756452d5b6d981e5fe4de3991cf6b7838f74fb8c411027a91dc2cf89a8d1a4"
C59_SCOPED_MANIFEST_SHA256 = "c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda"
C59_CERTIFICATE_SHA256 = "3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a"
C59_SCHEMA_SHA256 = "07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4"
C59_CHECK_REPORT_SHA256 = "271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3"
C59_GROUP_EVIDENCE_SHA256 = "0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958"
C59_RESOLVENT_EVIDENCE_SHA256 = "667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6"

GROUP_COMPONENT = {
    "aggregate_sha256": "dfd7d16a0128eae7a64906a4449a3022772dbc277abaae8187b6208340302464",
    "producer_sha256": "fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b",
    "checker_sha256": "4338ad0e2af9a0fe096cbb6514de6c8d5227386a2ffadeac487a858fb160dde3",
    "evidence_sha256": "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2",
    "replay_sha256": "77061a473c504925d24cfb2cedc26f7d4bc7057d4ee84615474cfa154323aba0",
    "schema_sha256": "8f57605397dff0bccda2a817775cbb143b6250172f0e938021b1f9cf7e1b2cba",
    "artifact_count": 10,
    "total_bytes": 248016,
}
RESOLVER_COMPONENT = {
    "aggregate_sha256": "9ceda190badd260008fcb37788afd5f2a3e3457ca9e1e452f3999df24c12fe97",
    "producer_sha256": "61b157e8c3e5a68bf304f9499bc176f60fe16bf7c5e5f6d021fbec17d7d9465e",
    "checker_sha256": "5f4070831d4734ba3be93ae578d7a2be893f46676ab40cdaa4a2de6b8d3fb672",
    "evidence_sha256": "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da",
    "payload_sha256": "eb17676ff10190c0b9f78e8f3fcb90121808fcd2c6a3b5d4dd06bfdc6177bb46",
    "artifact_count": 12,
    "total_bytes": 140873,
}
COMPONENT_SOURCE_LOCKS = {
    "c60_group.py": GROUP_COMPONENT["producer_sha256"],
    "c60_checker_group.g": GROUP_COMPONENT["checker_sha256"],
    "c60_resolvent.py": RESOLVER_COMPONENT["producer_sha256"],
    "c60_checker_resolvent.py": RESOLVER_COMPONENT["checker_sha256"],
}

SCHEMA_ID = "hcs-c60-certificate-schema-v1"
MAX_CERTIFICATE_BYTES = 5_000_000
MAX_JSON_BYTES = 20_000_000
MANIFEST_PATTERN = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")
STAGE_NAME_PATTERN = re.compile(r"^\.c60-stage-[A-Za-z0-9]{8}$")

EXPECTED_COLLISION_BUCKETS = [
    [12, 15], [17, 21], [29, 36], [31, 39], [41, 42], [46, 48],
    [57, 58], [59, 64], [112, 120], [132, 140], [301, 303],
]
EXPECTED_COLLISION_FIELD_DEGREES = [
    12960, 12960, 8640, 8640, 6480, 6480, 6480, 6480, 3240, 2880, 320,
]
LARGE_PRIME = 14932047182473291995860108491583652133938007263719
EXPECTED_COEFFICIENT_HASHES = {
    "M": "b8818888c1ceb83e05d2f2df045e9d6e418f1ea18a5f019d1398e4cd0a59ef6b",
    "F0": "ffe9439cd390729bbb0dd7ffa4c6a1045c7fbc9c645e0f37e75c71d1e786e10d",
    "L": "c82feda40496156b7d006de4e47a1b808b3cf3ffffe4a386652d3e3fa77861f1",
}
EXPECTED_CARRIER_HASHES = {
    "M": "0beb2791f4df4bb56214b6a35384517083f5909004219cc988b6de70f494d17c",
    "F0": "83f014bb3087708ad6e65c4f61bc92a73172aa649ef573358164c1ae7d9efbc5",
    "L": "fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5",
}
EXPECTED_ORBIT_DEGREES = {"M": 160, "F0": 320, "L": 640}
EXPECTED_FIELD_ORDER = ["N", "H301", "H302", "H303", "J"]
EXPECTED_RELATIVE_FIELD_ORDER = ["H301", "H302", "H303", "J"]
EXPECTED_RELATIVE_EXPONENTS = {
    "H301": [8, 0, 0, 0],
    "H302": [16, 0, 0, 0],
    "H303": [8, 0, 0, 0],
    "J": [32, 0, 0, 0],
}


def _fail(message: str) -> None:
    raise c60_exact.StrictDataError(message)


def _require_digest(value: Any, label: str) -> str:
    return c60_exact.require_sha256(value, label)


def _require_keys(value: Any, expected: Iterable[str], label: str) -> dict[str, Any]:
    return c60_exact.require_exact_keys(value, set(expected), label)


def _canonical_payload_sha256(value: Any) -> str:
    return c60_exact.sha256_bytes(c60_exact.canonical_leaf_bytes(value))


def _canonical_report_sha256(value: Any) -> str:
    return c60_exact.sha256_bytes(c60_exact.canonical_json_bytes(value))


def _regular_directory(path: Path, label: str) -> Path:
    absolute = path.absolute()
    if (
        not absolute.exists()
        or absolute.is_symlink()
        or not absolute.is_dir()
        or absolute.resolve(strict=True) != absolute
    ):
        _fail(f"{label} must be an existing real non-symlink directory")
    return absolute


def _directory_snapshot(path: Path) -> tuple[int, int, int, int, int, int, int]:
    metadata = path.lstat()
    if not stat.S_ISDIR(metadata.st_mode) or path.is_symlink():
        _fail(f"directory identity is not a real directory: {path}")
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_size,
        metadata.st_mode,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
        metadata.st_nlink,
    )


@dataclass(frozen=True)
class FileSeal:
    sha256: str
    size_bytes: int
    device: int
    inode: int
    mode: int
    mtime_ns: int
    ctime_ns: int
    links: int


def _stable_bytes(path: Path, *, max_bytes: int) -> tuple[bytes, FileSeal]:
    """Read one single-link regular file with full before/after identity."""

    absolute = path.absolute()
    try:
        path_before = absolute.lstat()
    except FileNotFoundError as exc:
        raise c60_exact.StrictDataError(f"required file is missing: {path}") from exc
    if not stat.S_ISREG(path_before.st_mode) or path_before.st_nlink != 1:
        _fail(f"authority must be one single-link regular file: {path}")
    flags = os.O_RDONLY
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(absolute, flags)
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            _fail(f"opened authority is not one single-link regular file: {path}")
        chunks: list[bytes] = []
        total = 0
        while True:
            block = os.read(descriptor, 1 << 20)
            if not block:
                break
            total += len(block)
            if total > max_bytes:
                _fail(f"authority exceeds byte ceiling: {path}")
            chunks.append(block)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    path_after = absolute.lstat()
    identity = lambda value: (
        value.st_dev,
        value.st_ino,
        value.st_size,
        value.st_mode,
        value.st_mtime_ns,
        value.st_ctime_ns,
        value.st_nlink,
    )
    if (
        identity(path_before) != identity(before)
        or identity(before) != identity(after)
        or identity(after) != identity(path_after)
    ):
        _fail(f"authority changed while being read: {path}")
    raw = b"".join(chunks)
    if len(raw) != after.st_size:
        _fail(f"authority size changed while being read: {path}")
    return raw, FileSeal(
        sha256=hashlib.sha256(raw).hexdigest(),
        size_bytes=len(raw),
        device=after.st_dev,
        inode=after.st_ino,
        mode=after.st_mode,
        mtime_ns=after.st_mtime_ns,
        ctime_ns=after.st_ctime_ns,
        links=after.st_nlink,
    )


def _read_json(
    path: Path, *, max_bytes: int, canonical_pretty: bool
) -> tuple[dict[str, Any], bytes, FileSeal]:
    raw, fingerprint = _stable_bytes(path, max_bytes=max_bytes)
    value = c60_exact.strict_json_loads(raw, max_bytes=max_bytes)
    if type(value) is not dict:
        _fail(f"JSON root must be an object: {path}")
    expected = c60_exact.canonical_json_bytes(value, pretty=canonical_pretty)
    if raw != expected:
        _fail(f"JSON bytes are not canonical: {path}")
    return value, raw, fingerprint


def _parse_sha256_manifest(raw: bytes, label: str) -> dict[str, str]:
    try:
        lines = raw.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise c60_exact.StrictDataError(f"{label} manifest is not UTF-8") from exc
    entries: dict[str, str] = {}
    for line in lines:
        match = MANIFEST_PATTERN.fullmatch(line)
        if match is None:
            _fail(f"{label} manifest row is malformed")
        digest, relative = match.groups()
        if not c60_exact.safe_relative_path(relative) or relative in entries:
            _fail(f"{label} manifest contains an unsafe/duplicate path")
        entries[relative] = digest
    if not entries or list(entries) != sorted(entries):
        _fail(f"{label} manifest must be nonempty and path-sorted")
    return entries


def _git_ancestor_of(older: str, newer: str) -> bool:
    result = subprocess.run(
        ["/usr/bin/git", "merge-base", "--is-ancestor", older, newer],
        cwd=REPO,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=c60_pipeline.clean_environment(),
        check=False,
        timeout=60,
    )
    if result.stdout or result.stderr:
        _fail("git ancestry check emitted output")
    return result.returncode == 0


def _git_ancestor(commit: str) -> bool:
    return _git_ancestor_of(commit, "HEAD")


def source_contract() -> dict[str, Any]:
    code = _regular_directory(CODE, "C60 code directory")
    code_before = _directory_snapshot(code)
    imported_modules = {
        "c60_exact.py": c60_exact,
        "c60_group.py": c60_group,
        "c60_pipeline.py": c60_pipeline,
        "c60_resolvent.py": c60_resolvent,
    }
    for name, module in imported_modules.items():
        module_file = getattr(module, "__file__", None)
        if (
            type(module_file) is not str
            or Path(module_file).resolve(strict=True)
            != (code / name).resolve(strict=True)
        ):
            _fail(f"imported C60 module does not come from canonical code: {name}")
    children = list(code.iterdir())
    if any(path.is_symlink() or not path.is_file() for path in children):
        _fail("C60 code inventory contains a non-regular entry")
    observed = {path.name for path in children}
    expected = set(CODE_FILES)
    if len(observed) != len(children) or observed != expected:
        _fail(
            f"C60 code inventory mismatch; missing={sorted(expected-observed)}; "
            f"extra={sorted(observed-expected)}"
        )
    entries = []
    for name in CODE_FILES:
        raw, fingerprint = _stable_bytes(code / name, max_bytes=3_000_000)
        expected_mode = "0755" if name == "run_all.sh" else "0644"
        observed_mode = f"{stat.S_IMODE(fingerprint.mode):04o}"
        if observed_mode != expected_mode:
            _fail(
                f"C60 code mode mismatch for {name}: "
                f"expected {expected_mode}, observed {observed_mode}"
            )
        if (
            name in COMPONENT_SOURCE_LOCKS
            and fingerprint.sha256 != COMPONENT_SOURCE_LOCKS[name]
        ):
            _fail(f"frozen component source digest changed: {name}")
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": len(raw),
                "mode_octal": observed_mode,
            }
        )
    final_children = list(code.iterdir())
    if (
        _directory_snapshot(code) != code_before
        or any(path.is_symlink() or not path.is_file() for path in final_children)
        or {path.name for path in final_children} != expected
        or len(final_children) != len(expected)
    ):
        _fail("C60 code directory changed during source-contract binding")
    return {
        "schema_id": "hcs-c60-source-contract-v1",
        "entry_count": 13,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [f"code/{name}" for name in sorted(CODE_FILES)],
        "entries": entries,
        "mode_policy": "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644",
        "self_reference_policy": "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE",
    }


def _relative_to_repo(path: Path) -> str:
    try:
        return path.resolve(strict=True).relative_to(REPO.resolve(strict=True)).as_posix()
    except ValueError as exc:
        raise c60_exact.StrictDataError(f"path escapes repository: {path}") from exc


def _file_binding(
    path: Path, expected_sha256: str, label: str, *, max_bytes: int = 5_000_000
) -> tuple[dict[str, Any], bytes]:
    raw, seal = _stable_bytes(path, max_bytes=max_bytes)
    if seal.sha256 != expected_sha256:
        _fail(f"{label} digest changed")
    return {
        "path": _relative_to_repo(path),
        "sha256": seal.sha256,
        "size_bytes": seal.size_bytes,
    }, raw


def _verify_c59_full_manifest() -> tuple[dict[str, Any], dict[str, str]]:
    project = _regular_directory(C59_PROJECT, "released C59 project")
    project_before = _directory_snapshot(project)
    raw, seal = _stable_bytes(C59_FULL_MANIFEST, max_bytes=2_000_000)
    if seal.sha256 != C59_FULL_MANIFEST_SHA256:
        _fail("released C59 full-manifest digest changed")
    manifest = _parse_sha256_manifest(raw, "C59 full")
    if len(manifest) != 63 or "FULL_PROJECT_HASHES.sha256" in manifest:
        _fail("released C59 full-manifest count/self-exclusion changed")

    observed_files: set[str] = set()
    observed_directories: set[str] = set()
    for path in project.rglob("*"):
        relative = path.relative_to(project).as_posix()
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            _fail("released C59 tree contains a symlink")
        if stat.S_ISREG(metadata.st_mode):
            if relative != "FULL_PROJECT_HASHES.sha256":
                observed_files.add(relative)
        elif stat.S_ISDIR(metadata.st_mode):
            observed_directories.add(relative)
        else:
            _fail("released C59 tree contains a special object")
    allowed_directories: set[str] = set()
    for relative in set(manifest) | {"FULL_PROJECT_HASHES.sha256"}:
        for parent in PurePosixPath(relative).parents:
            if parent.as_posix() != ".":
                allowed_directories.add(parent.as_posix())
    if observed_files != set(manifest) or observed_directories != allowed_directories:
        _fail("released C59 live tree does not exactly match its 63-entry manifest")

    total_bytes = 0
    for relative, expected in manifest.items():
        leaf_raw, leaf_seal = _stable_bytes(
            project / relative, max_bytes=210_000_000
        )
        if leaf_seal.sha256 != expected:
            _fail(f"released C59 leaf changed: {relative}")
        total_bytes += len(leaf_raw)
    final_files: set[str] = set()
    final_directories: set[str] = set()
    for path in project.rglob("*"):
        relative = path.relative_to(project).as_posix()
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            _fail("released C59 tree gained a symlink during rebind")
        if stat.S_ISREG(metadata.st_mode):
            if relative != "FULL_PROJECT_HASHES.sha256":
                final_files.add(relative)
        elif stat.S_ISDIR(metadata.st_mode):
            final_directories.add(relative)
        else:
            _fail("released C59 tree gained a special object during rebind")
    if (
        _directory_snapshot(project) != project_before
        or final_files != observed_files
        or final_directories != observed_directories
    ):
        _fail("released C59 tree changed during full-manifest verification")
    return {
        "entry_count": 63,
        "inventory_exact_excluding_self": True,
        "manifest_path": _relative_to_repo(C59_FULL_MANIFEST),
        "manifest_sha256": seal.sha256,
        "manifest_size_bytes": seal.size_bytes,
        "verified_leaf_total_bytes": total_bytes,
    }, manifest


def _validate_c59_scoped_manifest(
    full_manifest: dict[str, str],
) -> dict[str, Any]:
    value, raw, seal = _read_json(
        C59_SCOPED_MANIFEST, max_bytes=2_000_000, canonical_pretty=True
    )
    if seal.sha256 != C59_SCOPED_MANIFEST_SHA256:
        _fail("released C59 scoped-manifest digest changed")
    _require_keys(
        value,
        {
            "entries", "entry_count", "manifest_self_included",
            "schema", "scope", "status",
        },
        "released C59 scoped manifest",
    )
    if (
        value["entry_count"] != 20
        or value["manifest_self_included"] is not False
        or value["schema"] != "hcs-c59-scoped-hash-manifest-v1"
        or value["scope"] != "exact_C59_code_and_results_artifacts"
        or value["status"] != "PREFREEZE_CODE_RESULTS_PASS"
        or type(value["entries"]) is not list
        or len(value["entries"]) != 20
    ):
        _fail("released C59 scoped-manifest header changed")
    expected_paths = {
        *[f"code/{name}" for name in (
            "README.md", "c59_atomic_promote.py", "c59_checker.py",
            "c59_checker_group.g", "c59_checker_resolvent.py", "c59_exact.py",
            "c59_group.py", "c59_hash_manifest.py", "c59_pipeline.py",
            "c59_producer.py", "c59_resolvent.py", "run_all.sh",
            "test_c59.py",
        )],
        *[f"results/{name}" for name in (
            "RESULTS.md", "TEST_REPORT.md", "c59_certificate.json",
            "c59_check_report.json", "c59_group_evidence.json",
            "c59_resolvent_evidence.json", "c59_schema.json",
        )],
    }
    rows: dict[str, tuple[str, int]] = {}
    for index, row in enumerate(value["entries"]):
        row = _require_keys(
            row, {"path", "sha256", "size_bytes"},
            f"released C59 scoped row {index}",
        )
        path = row["path"]
        if (
            type(path) is not str
            or not c60_exact.safe_relative_path(path)
            or path in rows
            or type(row["size_bytes"]) is not int
        ):
            _fail("released C59 scoped row path/type changed")
        digest = _require_digest(row["sha256"], "released C59 scoped digest")
        leaf_raw, leaf_seal = _stable_bytes(
            C59_PROJECT / path, max_bytes=20_000_000
        )
        if (
            leaf_seal.sha256 != digest
            or len(leaf_raw) != row["size_bytes"]
            or full_manifest.get(path) != digest
        ):
            _fail(f"released C59 scoped leaf changed: {path}")
        rows[path] = (digest, len(leaf_raw))
    if set(rows) != expected_paths or list(rows) != sorted(rows):
        _fail("released C59 scoped inventory changed")
    return {
        "entry_count": 20,
        "inventory_exact_excluding_self": True,
        "manifest_path": _relative_to_repo(C59_SCOPED_MANIFEST),
        "manifest_sha256": seal.sha256,
        "manifest_size_bytes": len(raw),
        "status": value["status"],
    }


def _validate_c59_certificate_bundle(
    full_manifest: dict[str, str],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    certificate, certificate_raw, certificate_seal = _read_json(
        C59_CERTIFICATE, max_bytes=MAX_JSON_BYTES, canonical_pretty=True
    )
    schema, schema_raw, schema_seal = _read_json(
        C59_SCHEMA, max_bytes=2_000_000, canonical_pretty=True
    )
    check, check_raw, check_seal = _read_json(
        C59_CHECK_REPORT, max_bytes=2_000_000, canonical_pretty=True
    )
    expected_files = {
        "results/c59_certificate.json": C59_CERTIFICATE_SHA256,
        "results/c59_schema.json": C59_SCHEMA_SHA256,
        "results/c59_check_report.json": C59_CHECK_REPORT_SHA256,
    }
    observed = {
        "results/c59_certificate.json": certificate_seal.sha256,
        "results/c59_schema.json": schema_seal.sha256,
        "results/c59_check_report.json": check_seal.sha256,
    }
    if observed != expected_files or any(
        full_manifest.get(path) != digest for path, digest in observed.items()
    ):
        _fail("released C59 certificate bundle bytes changed")
    _require_keys(
        certificate, {"payload", "payload_sha256", "schema", "schema_sha256"},
        "released C59 certificate",
    )
    if not c60_exact.deep_exact(certificate["schema"], schema):
        _fail("released C59 embedded/separate schema differ")
    if certificate["schema_sha256"] != _canonical_payload_sha256(schema):
        _fail("released C59 schema digest failed")
    if certificate["payload_sha256"] != _canonical_payload_sha256(
        certificate["payload"]
    ):
        _fail("released C59 payload digest failed")
    status = certificate["payload"].get("status")
    if (
        type(status) is not dict
        or status.get("machine_code_results_status")
        != "PREFREEZE_CODE_RESULTS_PASS"
        or status.get("release_status") != "NOT_RELEASED"
    ):
        _fail("released C59 certificate semantic status changed")
    check_certificate = check.get("certificate", {})
    check_schema = check.get("schema_file", {})
    if (
        check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        or check_certificate.get("payload_sha256")
        != certificate["payload_sha256"]
        or check_certificate.get("sha256") != C59_CERTIFICATE_SHA256
        or check_schema.get("sha256") != C59_SCHEMA_SHA256
        or check_schema.get("parsed_deep_equal_embedded_schema") is not True
        or check.get("full_semantic_leaf_rebuild") is not True
    ):
        _fail("released C59 independent check binding failed")
    return certificate, {
        "certificate_path": _relative_to_repo(C59_CERTIFICATE),
        "certificate_sha256": certificate_seal.sha256,
        "certificate_size_bytes": len(certificate_raw),
        "payload_sha256": certificate["payload_sha256"],
        "schema_path": _relative_to_repo(C59_SCHEMA),
        "schema_sha256": schema_seal.sha256,
        "schema_size_bytes": len(schema_raw),
        "check_report_path": _relative_to_repo(C59_CHECK_REPORT),
        "check_report_sha256": check_seal.sha256,
        "check_report_size_bytes": len(check_raw),
        "check_result": check["result"],
    }, check


def _released_c59_projection(
    group: dict[str, Any],
    resolver: dict[str, Any],
    certificate: dict[str, Any],
) -> dict[str, Any]:
    _require_keys(
        group,
        {
            "G2_gassmann_minimality", "G4_global_arithmetic",
            "G5_tom140_local_algebra", "G6_tom206_local_algebra",
            "contract_alignment", "frozen_permutation_arrays",
            "independent_replay", "provenance", "schema_id", "status",
        },
        "released C59 group evidence",
    )
    if group["schema_id"] != "hcs-c59-group-evidence-v1" or group["status"] != "PASS":
        _fail("released C59 group evidence identity changed")
    g2 = group["G2_gassmann_minimality"]
    classes = g2["all_350_subgroup_classes"]
    if (
        type(classes) is not list
        or len(classes) != 350
        or g2["tom_subgroup_class_count"] != 350
        or g2["exact_11_collision_buckets"] != EXPECTED_COLLISION_BUCKETS
        or g2["collision_bucket_indices"]
        != EXPECTED_COLLISION_FIELD_DEGREES
    ):
        _fail("released C59 exhaustive group carrier changed")
    profiles = {
        tuple(row["permutation_character_values"]) for row in classes
    }
    if len(profiles) != 339:
        _fail("released C59 character-profile count changed")
    frozen = _require_keys(
        group["frozen_permutation_arrays"],
        {
            "arrays", "canonical_sha256", "phase1_design_input_read_at_runtime",
            "phase1_design_input_sha256",
        },
        "released C59 frozen arrays",
    )["arrays"]
    _require_keys(
        frozen,
        {
            "branch140_D_generators", "branch140_P_generators",
            "branch140_Q_generators", "branch206_D_generators",
            "branch206_I_generators", "branch206_P_generators",
            "branch206_Q_generators", "h301_generators", "h303_generators",
            "w27_simple_reflection_generators",
        },
        "released C59 frozen array map",
    )

    _require_keys(
        resolver, {"payload", "payload_sha256", "schema_id", "schema_sha256"},
        "released C59 resolver evidence",
    )
    if (
        resolver["schema_id"] != "hcs-c59-resolvent-evidence-v1"
        or resolver["payload_sha256"] != _canonical_report_sha256(
            resolver["payload"]
        )
    ):
        _fail("released C59 resolver identity changed")
    resolver_payload = resolver["payload"]
    finite = resolver_payload["finite_field"]
    lines = resolver_payload["line_configuration"]
    invariants = resolver_payload["invariants"]
    if (
        finite["factor_degrees"] != [[1, 27]]
        or len(finite["roots_sorted"]) != 27
        or len(set(finite["roots_sorted"])) != 27
        or resolver_payload["constants"]["prime"] != 692717
        or lines["mapping_is_graph_isomorphism"] is not True
        or lines["all_equation_residues_zero"] is not True
        or invariants["301"]["support_stabilizer_equals_h"] is not True
        or invariants["303"]["support_stabilizer_equals_h"] is not True
    ):
        _fail("released C59 root/support carrier changed")

    labelled_arrays = {
        "W27_generators": frozen["w27_simple_reflection_generators"],
        "Hplus_generators": frozen["h301_generators"],
        "Hminus_generators": frozen["h303_generators"],
    }
    local_arrays = {
        key: deepcopy(frozen[key])
        for key in sorted(frozen)
        if key.startswith("branch")
    }
    root_supports = {
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
    projection = {
        "labelled_W_Hplus_Hminus_arrays_sha256": _canonical_payload_sha256(
            labelled_arrays
        ),
        "line_roots_and_supports_sha256": _canonical_payload_sha256(
            root_supports
        ),
        "retained_C58_local_arrays_sha256": _canonical_payload_sha256(
            local_arrays
        ),
        "tom_subgroup_class_count": 350,
        "distinct_permutation_character_profile_count": 339,
        "exact_collision_buckets": deepcopy(EXPECTED_COLLISION_BUCKETS),
        "collision_bucket_field_degrees": deepcopy(
            EXPECTED_COLLISION_FIELD_DEGREES
        ),
        "split_prime": 692717,
        "c59_certificate_payload_sha256": certificate["payload_sha256"],
    }
    projection["canonical_sha256"] = _canonical_payload_sha256(projection)
    return projection


def _bind_released_c59() -> dict[str, Any]:
    full_summary, full_manifest = _verify_c59_full_manifest()
    route_binding, route_raw = _file_binding(
        C59_ROUTE, C59_ROUTE_SHA256, "released C59 live Route"
    )
    archive_binding, archive_raw = _file_binding(
        C59_ROUTE_ARCHIVE, C59_ROUTE_SHA256, "released C59 archived Route"
    )
    if route_raw != archive_raw:
        _fail("released C59 live/archive Route bytes differ")
    route_text = route_raw.decode("utf-8", errors="strict")
    for token in (
        "candidate_id: HCS-C59",
        "code_results_status: PREFREEZE_CODE_RESULTS_PASS",
        "release_status: RELEASE_FROZEN",
        "promotion_authorized: true",
        f'code_commit: "{C59_IMPLEMENTATION_COMMIT}"',
        "NO_BAD_EULER_OR_ROOT_NUMBER",
    ):
        if token not in route_text:
            _fail(f"released C59 Route token missing: {token}")
    if not _git_ancestor_of(C59_IMPLEMENTATION_COMMIT, C59_RELEASE_COMMIT):
        _fail("I59 is not an ancestor of P59")
    if not _git_ancestor(C59_RELEASE_COMMIT):
        _fail("P59 is not an ancestor of current HEAD")

    scoped = _validate_c59_scoped_manifest(full_manifest)
    certificate, certificate_bundle, _ = _validate_c59_certificate_bundle(
        full_manifest
    )
    group, group_raw, group_seal = _read_json(
        C59_GROUP_EVIDENCE, max_bytes=5_000_000, canonical_pretty=False
    )
    resolver, resolver_raw, resolver_seal = _read_json(
        C59_RESOLVENT_EVIDENCE, max_bytes=5_000_000, canonical_pretty=False
    )
    if (
        group_seal.sha256 != C59_GROUP_EVIDENCE_SHA256
        or resolver_seal.sha256 != C59_RESOLVENT_EVIDENCE_SHA256
        or full_manifest.get("results/c59_group_evidence.json")
        != group_seal.sha256
        or full_manifest.get("results/c59_resolvent_evidence.json")
        != resolver_seal.sha256
    ):
        _fail("released C59 component evidence bytes changed")
    projection = _released_c59_projection(group, resolver, certificate)
    return {
        "candidate_id": "HCS-C59",
        "implementation_commit": C59_IMPLEMENTATION_COMMIT,
        "release_commit": C59_RELEASE_COMMIT,
        "implementation_commit_ancestor_of_release_commit": True,
        "release_commit_ancestor_of_current_HEAD": True,
        "full_manifest": full_summary,
        "scoped_manifest": scoped,
        "live_route": route_binding,
        "archive_route": archive_binding,
        "live_archive_route_identical": True,
        "certificate_bundle": certificate_bundle,
        "group_evidence": {
            "path": _relative_to_repo(C59_GROUP_EVIDENCE),
            "sha256": group_seal.sha256,
            "size_bytes": len(group_raw),
        },
        "resolver_evidence": {
            "path": _relative_to_repo(C59_RESOLVENT_EVIDENCE),
            "sha256": resolver_seal.sha256,
            "size_bytes": len(resolver_raw),
        },
        "released_object_projection": projection,
        "status": "RELEASE_FROZEN",
    }


def _formal_aggregate() -> tuple[dict[str, Any], dict[str, bytes]]:
    project = _regular_directory(PROJECT, "C60 project directory")
    project_before = _directory_snapshot(project)
    observed = {
        path.name
        for path in project.iterdir()
        if path.is_file() and path.suffix == ".md"
    }
    if observed != set(FORMAL_FILES):
        _fail(
            "formal Markdown inventory mismatch; "
            f"missing={sorted(set(FORMAL_FILES)-observed)}; "
            f"extra={sorted(observed-set(FORMAL_FILES))}"
        )
    entries: list[dict[str, Any]] = []
    raw_by_name: dict[str, bytes] = {}
    rows = bytearray()
    for name in sorted(FORMAL_FILES):
        raw, seal = _stable_bytes(PROJECT / name, max_bytes=2_000_000)
        raw_by_name[name] = raw
        entries.append({
            "path": name, "sha256": seal.sha256, "size_bytes": len(raw),
        })
        rows.extend(f"{seal.sha256}  {name}\n".encode("ascii"))
    aggregate = hashlib.sha256(bytes(rows)).hexdigest()
    if aggregate != FORMAL_PACKAGE_SHA256:
        _fail("C60 final formal-package aggregate changed")
    final_observed = {
        path.name
        for path in project.iterdir()
        if path.is_file() and path.suffix == ".md"
    }
    if (
        _directory_snapshot(project) != project_before
        or final_observed != observed
    ):
        _fail("C60 formal Markdown inventory changed during binding")
    return {
        "aggregate_definition": (
            "SHA256_OF_LEXICOGRAPHICALLY_BASENAME_ORDERED_SHA256SUM_LINES_"
            "FOR_EXACT_13_ROOT_MARKDOWN_FILES_ROUTE_EXCLUDED"
        ),
        "entries": entries,
        "entry_count": 13,
        "exact_formal_inventory": True,
        "markdown_aggregate_sha256": aggregate,
        "status": "TARGET_LOCK_FORMAL_INPUT_PASS",
    }, raw_by_name


def written_bridges_from_formal(
    raw_by_name: dict[str, bytes],
) -> dict[str, bool]:
    proof = raw_by_name["PROOF_PACKAGE.md"].decode("utf-8", errors="strict")
    theorem = raw_by_name["THEOREM_PACKAGE.md"].decode("utf-8", errors="strict")
    sections = {
        "released_C59_transport_to_C60_fixed_fields": (
            "### Step 1. Subgroup lattice and field degrees",
            "Left label-map transport is used",
            "$H_3=xH_-x^{-1}$",
        ),
        "orbit_noncollision_to_primitive_fixed_fields": (
            "### Step 3. Integrality and primitivity",
            "full orbit product",
        ),
        "coefficient_orbit_partitions_to_degree_two_obstruction": (
            "### Step 4. Formal invariant-degree obstruction",
            "unordered pairs",
        ),
        "subgroup_lattice_to_biquadratic_and_automorphisms": (
            "### Step 1. Subgroup lattice and field degrees",
            "### Step 2. Normal closures and automorphisms",
        ),
        "v4_character_relation_to_zeta_identity": (
            "### Step 6. Brauer relation and zeta identity",
        ),
        "conductors_to_signed_absolute_and_relative_discriminants": (
            "### Step 7. Signatures and absolute discriminants",
            "released filtration formulas",
            "### Step 8. Relative discriminants",
            "Subtracting twice the exponent vector",
        ),
        "double_cosets_to_relative_local_towers_and_tameness": (
            "### Step 9. Relative local tables",
            "double cosets",
            "retains both branches",
            "is tame",
        ),
    }
    result = {
        key: all(token in proof for token in sections[key])
        for key in WRITTEN_BRIDGE_KEYS
    }
    result["released_C59_transport_to_C60_fixed_fields"] = (
        result["released_C59_transport_to_C60_fixed_fields"]
        and "three quadratic subfields" in theorem
        and "Hminus^x" in theorem
    )
    if set(result) != set(WRITTEN_BRIDGE_KEYS) or not all(result.values()):
        _fail("one or more required C60 written bridges is absent")
    return result


def _target_lock_input_ledger_sha256(
    formal: dict[str, Any],
    route_sha256: str,
    batch_sha256: str,
) -> str:
    bindings = {
        "BATCH_PLAN_C57_C61.md": batch_sha256,
        **{
            f"{PROJECT.name}/{entry['path']}": entry["sha256"]
            for entry in formal["entries"]
        },
        f"{PROJECT.name}/route_a_evaluation.yaml": route_sha256,
    }
    ordered = "".join(
        f"{bindings[path]}  {path}\n" for path in sorted(bindings)
    ).encode("ascii")
    return hashlib.sha256(ordered).hexdigest()


def formal_authority() -> tuple[dict[str, Any], dict[str, bool]]:
    formal, raw_by_name = _formal_aggregate()
    route_binding, route_raw = _file_binding(
        ROUTE, ROUTE_SHA256, "C60 final Route"
    )
    batch_binding, batch_raw = _file_binding(
        BATCH, BATCH_SHA256, "C60 final Batch target lock"
    )
    guard_binding, _ = _file_binding(
        GUARD, GUARD_SHA256, "protected guard"
    )
    route_text = route_raw.decode("utf-8", errors="strict")
    for token in (
        "candidate_id: HCS-C60",
        "documentation_status: TARGET_LOCK_FORMAL_INPUT_PASS",
        "theorem_status: THEOREM_TARGET_LOCKED_IMPLEMENTATION_PENDING",
        "code_results_status: IMPLEMENTATION_PENDING",
        "promotion_authorized: false",
        f'formal_target_lock_package: "{FORMAL_PACKAGE_SHA256}"',
        f'batch_target_lock: "{BATCH_SHA256}"',
        "NO_BAD_EULER_OR_ROOT_NUMBER",
        "G1_common_normalizer_lattice",
        "G6_both_relative_local_towers",
    ):
        if token not in route_text:
            _fail(f"C60 final Route token missing: {token}")
    batch_text = batch_raw.decode("utf-8", errors="strict")
    for token in (
        "## HCS-C60: the biquadratic envelope of the cubic-surface Gassmann twins",
        "TARGET_LOCKED / IMPLEMENTATION_PENDING /",
        "NO_BAD_EULER_OR_ROOT_NUMBER",
        "TARGET_LOCK_FORMAL_INPUT",
    ):
        if token not in batch_text:
            _fail(f"C60 final Batch token missing: {token}")
    input_ledger = _target_lock_input_ledger_sha256(
        formal, route_binding["sha256"], batch_binding["sha256"]
    )
    if input_ledger != TARGET_LOCK_INPUT_LEDGER_SHA256:
        _fail("C60 exact 15-input target-lock ledger changed")
    formal.update({
        "route_path": route_binding["path"],
        "route_sha256": route_binding["sha256"],
        "route_size_bytes": route_binding["size_bytes"],
        "target_lock_input_entry_count": 15,
        "target_lock_input_ledger_sha256": input_ledger,
    })
    return {
        "all_released_full_inventories_rebound": True,
        "batch_target_lock": batch_binding,
        "fixed_predecessor_paths_only": True,
        "formal_target_lock": formal,
        "protected_guard": guard_binding,
        "released_C59": _bind_released_c59(),
        "schema_id": "hcs-c60-released-authority-rebind-v1",
    }, written_bridges_from_formal(raw_by_name)


def rebuild_g0() -> tuple[dict[str, Any], dict[str, bool]]:
    return formal_authority()


def _validate_component_documents(
    group: dict[str, Any],
    resolver: dict[str, Any],
) -> None:
    try:
        c60_group.validate_evidence(group)
    except Exception as exc:
        raise c60_exact.StrictDataError(
            "group evidence is not source-owned producer-valid"
        ) from exc
    try:
        c60_resolvent.validate_evidence_document(resolver)
    except Exception as exc:
        raise c60_exact.StrictDataError(
            "resolver evidence is not source-owned producer-valid"
        ) from exc
    if (
        group["schema_id"] != "hcs-c60-group-evidence-v1"
        or group["status"] != "PASS"
        or resolver["schema_id"] != "hcs-c60-resolvent-evidence-v1"
        or resolver["payload_sha256"] != RESOLVER_COMPONENT["payload_sha256"]
    ):
        _fail("C60 component evidence identity/status changed")
    group_backend = group["backend_contract"]
    group_gap = group["independent_replay"]["gap_checker"]
    if (
        group_backend["producer_source_sha256"]
        != GROUP_COMPONENT["producer_sha256"]
        or group_gap["checker_source_sha256"]
        != GROUP_COMPONENT["checker_sha256"]
        or group_gap["checker_projection_sha256"]
        != GROUP_COMPONENT["replay_sha256"]
    ):
        _fail("C60 group component source/replay tuple changed")


def _cross_bind_group_resolver(
    group: dict[str, Any],
    resolver: dict[str, Any],
) -> None:
    arrays = group["frozen_permutation_arrays"]["arrays"]
    fields = {
        row["label"]: row
        for row in group["G4_biquadratic_tower_characters"]["fields"]
    }
    rp = resolver["payload"]
    hashes = rp["groups"]
    expected_hashes = {
        "Hplus_generators_sha256": _canonical_payload_sha256(
            fields["H301"]["generators_one_based"]
        ),
        "H0_generators_sha256": _canonical_payload_sha256(
            fields["H302"]["generators_one_based"]
        ),
        "Hminus_generators_sha256": _canonical_payload_sha256(
            arrays["H303_generators"]
        ),
        "H3_generators_sha256": _canonical_payload_sha256(
            fields["H303"]["generators_one_based"]
        ),
        "N_generators_sha256": _canonical_payload_sha256(
            arrays["N_generators"]
        ),
        "J_generators_sha256": _canonical_payload_sha256(
            arrays["J_generators"]
        ),
    }
    for key, expected in expected_hashes.items():
        if hashes[key] != expected:
            _fail(f"group/resolver durable array cross-binding failed: {key}")
    if (
        rp["transport"]["label_permutation_one_based"]
        != arrays["normalizer_conjugator"]
        or rp["transport"]["label_permutation_one_based"]
        != group["G1_common_normalizer_uniqueness"][
            "normalizer_transport"
        ]["conjugating_permutation_one_based"]
    ):
        _fail("group/resolver left label-map transport differs")


def _artifact_contract_from_documents(
    group: dict[str, Any],
    resolver: dict[str, Any],
    *,
    group_size_bytes: int,
    resolver_size_bytes: int,
) -> dict[str, Any]:
    if (
        type(group_size_bytes) is not int
        or group_size_bytes <= 0
        or type(resolver_size_bytes) is not int
        or resolver_size_bytes <= 0
    ):
        _fail("component evidence sizes must be positive strict integers")
    _validate_component_documents(group, resolver)
    _cross_bind_group_resolver(group, resolver)
    return {
        "artifact_count": 2,
        "artifacts": [
            {
                "path": "results/c60_group_evidence.json",
                "format": "canonical_compact_json",
                "sha256": GROUP_COMPONENT["evidence_sha256"],
                "size_bytes": group_size_bytes,
                "schema_id": group["schema_id"],
                "internal_report_sha256": GROUP_COMPONENT["replay_sha256"],
                "component_aggregate_sha256": GROUP_COMPONENT[
                    "aggregate_sha256"
                ],
            },
            {
                "path": "results/c60_resolvent_evidence.json",
                "format": "canonical_compact_json",
                "sha256": RESOLVER_COMPONENT["evidence_sha256"],
                "size_bytes": resolver_size_bytes,
                "schema_id": resolver["schema_id"],
                "internal_report_sha256": resolver["payload_sha256"],
                "component_aggregate_sha256": RESOLVER_COMPONENT[
                    "aggregate_sha256"
                ],
                "schema_descriptor_sha256": resolver["schema_sha256"],
            },
        ],
        "component_contracts": {
            "group": deepcopy(GROUP_COMPONENT),
            "primitive_resolvent": deepcopy(RESOLVER_COMPONENT),
        },
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c60-artifact-contract-v1",
        "source_owned_full_document_validation": True,
    }


def artifact_contract(
    artifact_dir: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    directory = _regular_directory(artifact_dir, "C60 evidence directory")
    if (
        not STAGE_NAME_PATTERN.fullmatch(directory.name)
        or directory.parent != RESULTS.resolve(strict=True)
    ):
        _fail("evidence directory is not the canonical C60 runner stage")
    group_path = directory / ARTIFACT_NAMES[0]
    resolver_path = directory / ARTIFACT_NAMES[1]
    group, group_raw, group_seal = _read_json(
        group_path, max_bytes=2_000_000, canonical_pretty=False
    )
    resolver, resolver_raw, resolver_seal = _read_json(
        resolver_path, max_bytes=2_000_000, canonical_pretty=False
    )
    if (
        group_seal.sha256 != GROUP_COMPONENT["evidence_sha256"]
        or resolver_seal.sha256 != RESOLVER_COMPONENT["evidence_sha256"]
    ):
        _fail("C60 component evidence file digest changed")
    contract = _artifact_contract_from_documents(
        group,
        resolver,
        group_size_bytes=len(group_raw),
        resolver_size_bytes=len(resolver_raw),
    )
    return contract, group, resolver


@dataclass(frozen=True)
class StageBinding:
    parent: Path
    group_evidence: Path
    resolvent_evidence: Path
    output: Path
    schema_output: Path
    parent_device: int
    parent_inode: int
    parent_mode: int
    parent_links: int
    group_seal: FileSeal
    resolver_seal: FileSeal

    def assert_unchanged(self, label: str) -> None:
        metadata = self.parent.lstat()
        if (
            self.parent.is_symlink()
            or not stat.S_ISDIR(metadata.st_mode)
            or self.parent.resolve(strict=True) != self.parent
            or (
                metadata.st_dev, metadata.st_ino, metadata.st_mode,
                metadata.st_nlink,
            ) != (
                self.parent_device, self.parent_inode, self.parent_mode,
                self.parent_links,
            )
        ):
            _fail(f"canonical stage identity changed at {label}")
        _, group = _stable_bytes(self.group_evidence, max_bytes=2_000_000)
        _, resolver = _stable_bytes(
            self.resolvent_evidence, max_bytes=2_000_000
        )
        if group != self.group_seal or resolver != self.resolver_seal:
            _fail(f"immutable evidence changed at {label}")
        expected_names = {
            self.group_evidence.name,
            self.resolvent_evidence.name,
            self.output.name,
            self.schema_output.name,
        }
        children = list(self.parent.iterdir())
        if (
            any(path.name not in expected_names for path in children)
            or any(path.is_symlink() or not path.is_file() for path in children)
        ):
            _fail(f"canonical stage inventory changed at {label}")
        protected = {
            (self.group_seal.device, self.group_seal.inode),
            (self.resolver_seal.device, self.resolver_seal.inode),
        }
        output_inodes: set[tuple[int, int]] = set()
        for target in (self.output, self.schema_output):
            if os.path.lexists(target):
                metadata = target.lstat()
                inode = (metadata.st_dev, metadata.st_ino)
                if (
                    not stat.S_ISREG(metadata.st_mode)
                    or metadata.st_nlink != 1
                    or target.is_symlink()
                    or inode in protected
                    or inode in output_inodes
                ):
                    _fail(f"canonical stage output identity changed at {label}")
                output_inodes.add(inode)


def validate_fixed_paths(arguments: argparse.Namespace) -> StageBinding:
    artifact_dir = Path(arguments.artifact_dir).absolute()
    output = Path(arguments.output).absolute()
    schema_output = Path(arguments.schema_output).absolute()
    results = RESULTS.resolve(strict=True)
    if (
        not STAGE_NAME_PATTERN.fullmatch(artifact_dir.name)
        or artifact_dir.parent != results
        or artifact_dir.is_symlink()
        or not artifact_dir.is_dir()
        or artifact_dir.resolve(strict=True) != artifact_dir
    ):
        _fail(
            "artifact directory must be one real canonical "
            "PROJECT/results/.c60-stage-[A-Za-z0-9]{8} direct child"
        )
    group_path = artifact_dir / ARTIFACT_NAMES[0]
    resolver_path = artifact_dir / ARTIFACT_NAMES[1]
    if output != artifact_dir / "c60_certificate.json":
        _fail("producer output must use the fixed certificate basename")
    if schema_output != artifact_dir / "c60_schema.json":
        _fail("producer schema output must use the fixed schema basename")
    expected_children = {
        group_path.name, resolver_path.name, output.name, schema_output.name,
    }
    observed_children = {path.name for path in artifact_dir.iterdir()}
    if not observed_children.issubset(expected_children):
        _fail("canonical stage contains an unexpected entry")
    if any(path.is_dir() for path in artifact_dir.iterdir()):
        _fail("canonical stage may contain files only")

    _, group_seal = _stable_bytes(group_path, max_bytes=2_000_000)
    _, resolver_seal = _stable_bytes(resolver_path, max_bytes=2_000_000)
    if (group_seal.device, group_seal.inode) == (
        resolver_seal.device, resolver_seal.inode
    ):
        _fail("stage evidence files hardlink one another")
    protected = {
        (group_seal.device, group_seal.inode),
        (resolver_seal.device, resolver_seal.inode),
    }
    outputs: set[tuple[int, int]] = set()
    for target in (output, schema_output):
        if os.path.lexists(target):
            metadata = target.lstat()
            if (
                not stat.S_ISREG(metadata.st_mode)
                or metadata.st_nlink != 1
                or target.is_symlink()
            ):
                _fail("existing stage output must be one single-link regular file")
            inode = (metadata.st_dev, metadata.st_ino)
            if inode in protected or inode in outputs:
                _fail("stage output hardlinks an input or another output")
            outputs.add(inode)
    parent = artifact_dir.lstat()
    return StageBinding(
        parent=artifact_dir,
        group_evidence=group_path,
        resolvent_evidence=resolver_path,
        output=output,
        schema_output=schema_output,
        parent_device=parent.st_dev,
        parent_inode=parent.st_ino,
        parent_mode=parent.st_mode,
        parent_links=parent.st_nlink,
        group_seal=group_seal,
        resolver_seal=resolver_seal,
    )


def _group_field_record(row: Any, label: str) -> dict[str, Any]:
    row = _require_keys(
        row,
        {
            "abelian_invariants", "core_order_in_W", "derived_order",
            "field_degree", "generators_one_based", "id_group", "label",
            "normal_in_N", "normalizer_equals_N", "order", "tom_locator",
        },
        label,
    )
    return {
        "abelian_invariants": deepcopy(row["abelian_invariants"]),
        "core_order_in_W": row["core_order_in_W"],
        "derived_order": row["derived_order"],
        "field_degree": row["field_degree"],
        "generators_one_based": deepcopy(row["generators_one_based"]),
        "id_group": deepcopy(row["id_group"]),
        "label": row["label"],
        "normal_in_N": row["normal_in_N"],
        "normalizer_equals_N": row["normalizer_equals_N"],
        "order": row["order"],
        "tom_locator": row["tom_locator"],
    }


def _collision_row(row: Any, label: str) -> dict[str, Any]:
    base_keys = {
        "bucket", "field_degree", "normalizer_indices_over_subgroups",
        "normalizer_orders", "normalizer_tom_locators",
        "normalizers_conjugate_and_index_two_over_both",
        "normalizers_conjugate_in_W", "subgroup_order",
    }
    transported_keys = {
        "transported_generated_order", "transported_intersection_order",
        "transported_intersection_tom_locator",
    }
    if type(row) is not dict:
        _fail(f"{label} must be an object")
    observed_keys = set(row)
    if observed_keys == base_keys:
        row = _require_keys(row, base_keys, label)
    elif observed_keys == base_keys | transported_keys:
        row = _require_keys(row, base_keys | transported_keys, label)
    else:
        _fail(f"{label} has neither allowed exact collision-row shape")
    result = {
        "bucket": deepcopy(row["bucket"]),
        "field_degree": row["field_degree"],
        "normalizer_indices_over_subgroups": deepcopy(
            row["normalizer_indices_over_subgroups"]
        ),
        "normalizer_orders": deepcopy(row["normalizer_orders"]),
        "normalizer_tom_locators": deepcopy(row["normalizer_tom_locators"]),
        "normalizers_conjugate_and_index_two_over_both": row[
            "normalizers_conjugate_and_index_two_over_both"
        ],
        "normalizers_conjugate_in_W": row[
            "normalizers_conjugate_in_W"
        ],
        "subgroup_order": row["subgroup_order"],
    }
    if observed_keys == base_keys | transported_keys:
        result.update({
            "transported_generated_order": row[
                "transported_generated_order"
            ],
            "transported_intersection_order": row[
                "transported_intersection_order"
            ],
            "transported_intersection_tom_locator": row[
                "transported_intersection_tom_locator"
            ],
        })
    return result


def _build_g1(
    group: dict[str, Any], resolver: dict[str, Any]
) -> dict[str, Any]:
    source = _require_keys(
        group["G1_common_normalizer_uniqueness"],
        {
            "action", "collision_normalizer_scan", "common_normalizer",
            "normalizer_transport",
        },
        "group G1",
    )
    action = _require_keys(
        source["action"], {"carrier_degree", "generator_count", "weyl_order"},
        "group G1 action",
    )
    common = _require_keys(
        source["common_normalizer"],
        {
            "abelian_invariants", "core_order_in_W", "derived_order",
            "id_group", "index_in_W", "normalizer_order_in_W", "order",
            "quotient_by_J_id_group", "tom_locator",
        },
        "group G1 common normalizer",
    )
    transport = _require_keys(
        source["normalizer_transport"],
        {
            "H303_transport_contained_in_N",
            "conjugating_permutation_inverse_one_based",
            "conjugating_permutation_one_based", "right_action_equation",
            "right_action_equation_checked_pairs", "right_action_equation_holds",
            "source_N303_generators_one_based",
            "transported_N303_generators_one_based",
            "transported_normalizer_equals_N",
        },
        "group G1 normalizer transport",
    )
    scan = _require_keys(
        source["collision_normalizer_scan"],
        {
            "exact_11_collision_buckets",
            "qualifying_buckets_normalizers_conjugate_and_index_two_over_both",
            "rows",
        },
        "group G1 collision scan",
    )
    if (
        action != {"carrier_degree": 27, "generator_count": 6, "weyl_order": 51840}
        or common != {
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
        or scan["exact_11_collision_buckets"] != EXPECTED_COLLISION_BUCKETS
        or scan[
            "qualifying_buckets_normalizers_conjugate_and_index_two_over_both"
        ] != [[301, 303]]
        or type(scan["rows"]) is not list
        or len(scan["rows"]) != 11
    ):
        _fail("C60 common-normalizer/uniqueness constants changed")
    rows = [
        _collision_row(row, f"group collision row {index}")
        for index, row in enumerate(scan["rows"])
    ]
    if [row["bucket"] for row in rows] != EXPECTED_COLLISION_BUCKETS:
        _fail("C60 collision row order/content changed")
    qualifying = [
        row["bucket"] for row in rows
        if row["normalizers_conjugate_and_index_two_over_both"]
    ]
    if qualifying != [[301, 303]]:
        _fail("C60 exact uniqueness predicate no longer selects one bucket")

    tower = group["G4_biquadratic_tower_characters"]
    fields = [
        _group_field_record(row, f"group tower field {index}")
        for index, row in enumerate(tower["fields"])
    ]
    if [row["label"] for row in fields] != ["H301", "H302", "H303"]:
        _fail("C60 index-two field order changed")
    intersection = _require_keys(
        tower["intersection"],
        {
            "core_order_in_W", "equals_derived_subgroup_of_N",
            "generators_one_based", "index_in_W", "normal_in_N",
            "normalizer_order_in_W", "order", "tom_locator",
        },
        "group tower intersection",
    )
    if (
        [row["order"] for row in fields] != [162, 162, 162]
        or [row["field_degree"] for row in fields] != [320, 320, 320]
        or [row["tom_locator"] for row in fields] != [301, 302, 303]
        or [row["id_group"] for row in fields]
        != [[162, 11], [162, 10], [162, 19]]
        or intersection["order"] != 81
        or intersection["tom_locator"] != 266
        or intersection["equals_derived_subgroup_of_N"] is not True
        or tower["pairwise_intersections_equal_J"] is not True
        or tower["pairwise_intersection_orders"] != [81, 81, 81]
        or tower["pairwise_generated_orders"] != [324, 324, 324]
    ):
        _fail("C60 V4 subgroup lattice changed")
    if (
        transport["right_action_equation_holds"] is not True
        or transport["right_action_equation_checked_pairs"] != 8748
        or transport["H303_transport_contained_in_N"] is not True
        or transport["transported_normalizer_equals_N"] is not True
    ):
        _fail("C60 mutable label transport certificate changed")

    arrays = _require_keys(
        group["frozen_permutation_arrays"]["arrays"],
        {
            "H301_generators", "H302_generators", "H303_generators",
            "J_generators", "N_generators", "W27_generators",
            "branch140_D_generators", "branch140_P_generators",
            "branch140_Q_generators", "branch206_D_generators",
            "branch206_I_generators", "branch206_P_generators",
            "branch206_Q_generators", "normalizer_conjugator",
        },
        "group frozen arrays",
    )
    durable_arrays = {
        "H301_generators": deepcopy(arrays["H301_generators"]),
        "H302_generators": deepcopy(arrays["H302_generators"]),
        "H303_source_generators": deepcopy(arrays["H303_generators"]),
        "H3_transported_generators": deepcopy(
            fields[2]["generators_one_based"]
        ),
        "J_generators": deepcopy(arrays["J_generators"]),
        "N_generators": deepcopy(arrays["N_generators"]),
        "W27_generators": deepcopy(arrays["W27_generators"]),
        "branch140_D_generators": deepcopy(arrays["branch140_D_generators"]),
        "branch140_P_generators": deepcopy(arrays["branch140_P_generators"]),
        "branch140_Q_generators": deepcopy(arrays["branch140_Q_generators"]),
        "branch206_D_generators": deepcopy(arrays["branch206_D_generators"]),
        "branch206_I_generators": deepcopy(arrays["branch206_I_generators"]),
        "branch206_P_generators": deepcopy(arrays["branch206_P_generators"]),
        "branch206_Q_generators": deepcopy(arrays["branch206_Q_generators"]),
        "normalizer_conjugator": deepcopy(arrays["normalizer_conjugator"]),
    }
    direct = group["independent_replay"]["python"]["direct_projection"]
    orders = deepcopy(direct["group_orders"])
    if (
        orders["W"] != 51840
        or orders["N"] != 324
        or orders["H301"] != 162
        or orders["H302"] != 162
        or orders["H303c"] != 162
        or orders["J"] != 81
    ):
        _fail("C60 direct group-order replay changed")
    rp_transport = resolver["payload"]["transport"]
    if (
        rp_transport["H3_equals_transported_support_stabilizer"] is not True
        or rp_transport["H3_contained_in_N"] is not True
        or rp_transport["H3_order"] != 162
        or rp_transport["transported_support_stabilizer_order"] != 162
        or rp_transport["H301_intersection_H3_order"] != 81
    ):
        _fail("C60 transported-support stabilizer certificate changed")

    return {
        "action": {
            "carrier_degree": action["carrier_degree"],
            "generator_count": action["generator_count"],
            "weyl_order": action["weyl_order"],
        },
        "common_normalizer": {
            "abelian_invariants": deepcopy(common["abelian_invariants"]),
            "core_order_in_W": common["core_order_in_W"],
            "derived_order": common["derived_order"],
            "id_group": deepcopy(common["id_group"]),
            "index_in_W": common["index_in_W"],
            "normalizer_order_in_W": common["normalizer_order_in_W"],
            "order": common["order"],
            "quotient_by_J_id_group": deepcopy(
                common["quotient_by_J_id_group"]
            ),
            "tom_locator": common["tom_locator"],
        },
        "index_two_subgroups": fields,
        "common_intersection_J": {
            "core_order_in_W": intersection["core_order_in_W"],
            "equals_derived_subgroup_of_N": intersection[
                "equals_derived_subgroup_of_N"
            ],
            "generators_one_based": deepcopy(
                intersection["generators_one_based"]
            ),
            "index_in_W": intersection["index_in_W"],
            "normal_in_N": intersection["normal_in_N"],
            "normalizer_order_in_W": intersection["normalizer_order_in_W"],
            "order": intersection["order"],
            "tom_locator": intersection["tom_locator"],
        },
        "pairwise_lattice": {
            "generated_orders": deepcopy(tower["pairwise_generated_orders"]),
            "intersection_orders": deepcopy(
                tower["pairwise_intersection_orders"]
            ),
            "intersections_equal_J": tower[
                "pairwise_intersections_equal_J"
            ],
        },
        "left_label_map_transport": {
            "convention": rp_transport["convention"],
            "conjugating_permutation_one_based": deepcopy(
                transport["conjugating_permutation_one_based"]
            ),
            "conjugating_permutation_inverse_one_based": deepcopy(
                transport["conjugating_permutation_inverse_one_based"]
            ),
            "right_action_equation": transport["right_action_equation"],
            "right_action_equation_checked_pairs": transport[
                "right_action_equation_checked_pairs"
            ],
            "right_action_equation_holds": transport[
                "right_action_equation_holds"
            ],
            "source_N303_generators_one_based": deepcopy(
                transport["source_N303_generators_one_based"]
            ),
            "transported_N303_generators_one_based": deepcopy(
                transport["transported_N303_generators_one_based"]
            ),
            "transported_normalizer_equals_N": transport[
                "transported_normalizer_equals_N"
            ],
            "Stab_xSminus_equals_H3": rp_transport[
                "H3_equals_transported_support_stabilizer"
            ],
            "H3_contained_in_N": rp_transport["H3_contained_in_N"],
            "H301_intersection_H3_order": rp_transport[
                "H301_intersection_H3_order"
            ],
        },
        "durable_permutation_arrays": durable_arrays,
        "direct_group_replay": {
            "group_element_set_sha256": deepcopy(
                direct["group_element_set_sha256"]
            ),
            "group_orders": orders,
            "transport": deepcopy(direct["transport"]),
        },
        "exhaustive_collision_scan": {
            "all_subgroup_classes": 350,
            "distinct_permutation_character_profiles": 339,
            "exact_11_collision_buckets": deepcopy(
                scan["exact_11_collision_buckets"]
            ),
            "qualifying_buckets": deepcopy(
                scan[
                    "qualifying_buckets_normalizers_conjugate_and_index_two_over_both"
                ]
            ),
            "rows": rows,
            "predicate": (
                "normalizers_conjugate_in_W AND "
                "normalizer_indices_over_subgroups=[2,2]"
            ),
        },
        "uniqueness_scope": {
            "index_two_common_normalizer_case_unique": True,
            "broader_generated_V4_configuration_unique_claimed": False,
        },
    }


def _carrier_record(record: Any, label: str) -> dict[str, Any]:
    record = _require_keys(
        record,
        {
            "carrier", "carrier_sha256", "label", "modular_polynomial",
            "monomial_degree", "nonzero_monomial_count", "orbit_size",
            "stabilizer_equals_expected", "stabilizer_order",
            "weight_histogram",
        },
        label,
    )
    polynomial = _require_keys(
        record["modular_polynomial"],
        {
            "coefficient_count", "coefficient_sha256",
            "distinct_value_count", "sorted_values_sha256", "value_count",
            "values_sha256",
        },
        f"{label} modular polynomial",
    )
    histogram = _require_keys(
        record["weight_histogram"], {"1", "2"}, f"{label} weight histogram"
    )
    return {
        "carrier": deepcopy(record["carrier"]),
        "carrier_sha256": record["carrier_sha256"],
        "label": record["label"],
        "modular_polynomial": {
            "coefficient_count": polynomial["coefficient_count"],
            "coefficient_sha256": polynomial["coefficient_sha256"],
            "distinct_value_count": polynomial["distinct_value_count"],
            "sorted_values_sha256": polynomial["sorted_values_sha256"],
            "value_count": polynomial["value_count"],
            "values_sha256": polynomial["values_sha256"],
        },
        "monomial_degree": record["monomial_degree"],
        "nonzero_monomial_count": record["nonzero_monomial_count"],
        "orbit_size": record["orbit_size"],
        "stabilizer_equals_expected": record["stabilizer_equals_expected"],
        "stabilizer_order": record["stabilizer_order"],
        "weight_histogram": {"1": histogram["1"], "2": histogram["2"]},
    }


def _build_g2(
    group: dict[str, Any], resolver: dict[str, Any], g0: dict[str, Any]
) -> dict[str, Any]:
    payload = resolver["payload"]
    constants = _require_keys(
        payload["constants"],
        {
            "degree", "expected_coefficient_hashes",
            "expected_orbit_degrees", "prime", "scope_literal", "w_order",
        },
        "resolver constants",
    )
    expected_constants = {
        "degree": 27,
        "expected_coefficient_hashes": EXPECTED_COEFFICIENT_HASHES,
        "expected_orbit_degrees": EXPECTED_ORBIT_DEGREES,
        "prime": 692717,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "w_order": 51840,
    }
    if constants != expected_constants:
        _fail("C60 primitive-resolvent constants changed")
    carriers = {
        name: _carrier_record(payload["carriers"][name], f"carrier {name}")
        for name in ("M", "F0", "L")
    }
    for name, record in carriers.items():
        degree = EXPECTED_ORBIT_DEGREES[name]
        if (
            record["carrier_sha256"] != EXPECTED_CARRIER_HASHES[name]
            or record["orbit_size"] != degree
            or record["stabilizer_equals_expected"] is not True
            or record["modular_polynomial"]["value_count"] != degree
            or record["modular_polynomial"]["distinct_value_count"] != degree
            or record["modular_polynomial"]["coefficient_count"] != degree + 1
            or record["modular_polynomial"]["coefficient_sha256"]
            != EXPECTED_COEFFICIENT_HASHES[name]
        ):
            _fail(f"C60 primitive carrier/noncollision changed: {name}")

    bridge = _require_keys(
        payload["fixed_field_bridge"],
        {
            "K_completely_split_witness", "c59_all_27_line_equations_zero",
            "c59_factor_degrees", "c59_label_map_is_graph_isomorphism",
            "c59_split_roots_distinct",
            "characteristic_zero_orbit_values_distinct",
            "fixed_field_identities", "fixed_field_reason",
            "labelled_W_action_faithful", "modular_distinct_value_counts",
            "prime_unramified",
            "support_stabilizers_exact_on_Z_labelled_carrier",
        },
        "resolver fixed-field bridge",
    )
    direct = group["independent_replay"]["python"]["direct_projection"]
    if (
        direct["group_orders"]["W"] != 51840
        or bridge["labelled_W_action_faithful"] is not True
        or bridge["c59_factor_degrees"] != [[1, 27]]
        or bridge["c59_split_roots_distinct"] is not True
        or bridge["c59_label_map_is_graph_isomorphism"] is not True
        or bridge["c59_all_27_line_equations_zero"] is not True
        or bridge["prime_unramified"] is not True
        or bridge["K_completely_split_witness"] is not True
        or bridge["modular_distinct_value_counts"]
        != EXPECTED_ORBIT_DEGREES
        or bridge["support_stabilizers_exact_on_Z_labelled_carrier"]
        != {"F0": True, "L": True, "M": True}
    ):
        _fail("C60 split-prime/fixed-field bridge changed")
    transport = payload["transport"]
    if (
        transport["H3_equals_transported_support_stabilizer"] is not True
        or transport["H3_contained_in_N"] is not True
        or transport["H3_order"] != 162
        or transport["transported_support_stabilizer_order"] != 162
    ):
        _fail("C60 Stab(xSminus)=H3 subset N bridge changed")
    authority = payload["authority"]
    released = g0["released_C59"]
    if (
        authority["c59_implementation_commit"] != C59_IMPLEMENTATION_COMMIT
        or authority["c59_release_commit"] != C59_RELEASE_COMMIT
        or authority["c59_full_manifest_sha256"]
        != released["full_manifest"]["manifest_sha256"]
        or authority["c59_full_manifest_entry_count"] != 63
        or authority["c59_route_sha256"] != released["live_route"]["sha256"]
        or authority["c59_route_archive_sha256"]
        != released["archive_route"]["sha256"]
        or authority["c59_resolvent_evidence_sha256"]
        != released["resolver_evidence"]["sha256"]
        or authority["released_c59_rebound"] is not True
    ):
        _fail("resolver authority does not rebind integrated G0")

    groups = _require_keys(
        payload["groups"],
        {
            "H0_generators_sha256", "H3_generators_sha256",
            "Hminus_generators_sha256", "Hplus_generators_sha256",
            "J_generators_sha256", "N_generators_sha256",
            "orders_Hplus_H0_Hminus_H3_N_J",
        },
        "resolver group hashes",
    )
    return {
        "constants": {
            "degree": constants["degree"],
            "prime": constants["prime"],
            "w_order": constants["w_order"],
            "expected_orbit_degrees": deepcopy(
                constants["expected_orbit_degrees"]
            ),
            "expected_coefficient_hashes": deepcopy(
                constants["expected_coefficient_hashes"]
            ),
            "scope_literal": constants["scope_literal"],
        },
        "carriers": carriers,
        "group_carrier_hashes": {
            "H0_generators_sha256": groups["H0_generators_sha256"],
            "H3_generators_sha256": groups["H3_generators_sha256"],
            "Hminus_generators_sha256": groups[
                "Hminus_generators_sha256"
            ],
            "Hplus_generators_sha256": groups[
                "Hplus_generators_sha256"
            ],
            "J_generators_sha256": groups["J_generators_sha256"],
            "N_generators_sha256": groups["N_generators_sha256"],
            "orders_Hplus_H0_Hminus_H3_N_J": deepcopy(
                groups["orders_Hplus_H0_Hminus_H3_N_J"]
            ),
        },
        "left_transport_support_certificate": {
            "convention": transport["convention"],
            "label_permutation_one_based": deepcopy(
                transport["label_permutation_one_based"]
            ),
            "H3_order": transport["H3_order"],
            "transported_support_stabilizer_order": transport[
                "transported_support_stabilizer_order"
            ],
            "Stab_xSminus_equals_H3": transport[
                "H3_equals_transported_support_stabilizer"
            ],
            "H3_contained_in_N": transport["H3_contained_in_N"],
            "H301_intersection_H3_order": transport[
                "H301_intersection_H3_order"
            ],
        },
        "labelled_W_action_faithfulness": {
            "carrier_degree": 27,
            "distinct_labelled_permutation_count": 51840,
            "group_element_set_sha256": direct[
                "group_element_set_sha256"
            ]["W"],
            "faithful": bridge["labelled_W_action_faithful"],
            "derived_before_split_implication": True,
        },
        "complete_split_witness": {
            "prime": 692717,
            "factor_degrees": deepcopy(bridge["c59_factor_degrees"]),
            "all_27_roots_distinct": bridge["c59_split_roots_distinct"],
            "label_map_is_graph_isomorphism": bridge[
                "c59_label_map_is_graph_isomorphism"
            ],
            "all_27_line_equations_zero": bridge[
                "c59_all_27_line_equations_zero"
            ],
            "prime_unramified": bridge["prime_unramified"],
            "K_completely_split": bridge["K_completely_split_witness"],
        },
        "orbit_value_noncollision": {
            "modular_distinct_value_counts": deepcopy(
                bridge["modular_distinct_value_counts"]
            ),
            "characteristic_zero_orbit_values_distinct": bridge[
                "characteristic_zero_orbit_values_distinct"
            ],
            "support_stabilizers_exact_on_Z_labelled_carrier": deepcopy(
                bridge[
                    "support_stabilizers_exact_on_Z_labelled_carrier"
                ]
            ),
        },
        "fixed_field_generation_premises": {
            "identities": deepcopy(bridge["fixed_field_identities"]),
            "reason": bridge["fixed_field_reason"],
        },
        "component_authority_rebound": {
            "c59_full_manifest_sha256": authority[
                "c59_full_manifest_sha256"
            ],
            "c59_implementation_commit": authority[
                "c59_implementation_commit"
            ],
            "c59_release_commit": authority["c59_release_commit"],
            "c59_resolvent_evidence_sha256": authority[
                "c59_resolvent_evidence_sha256"
            ],
            "c59_resolvent_module_sha256": authority[
                "c59_resolvent_module_sha256"
            ],
            "c59_resolvent_payload_sha256": authority[
                "c59_resolvent_payload_sha256"
            ],
            "c59_route_archive_sha256": authority[
                "c59_route_archive_sha256"
            ],
            "c59_route_sha256": authority["c59_route_sha256"],
            "c60_durable_carrier_literals_sha256": authority[
                "c60_durable_carrier_literals_sha256"
            ],
            "c60_durable_group_literals_sha256": authority[
                "c60_durable_group_literals_sha256"
            ],
            "released_c59_rebound": authority["released_c59_rebound"],
        },
    }


def _zero_based_point_partition(value: Any) -> list[list[int]]:
    if type(value) is not list:
        _fail("point partition must be a list")
    converted = [[entry - 1 for entry in orbit] for orbit in value]
    return sorted(converted, key=lambda orbit: (len(orbit), orbit))


def _zero_based_pair_partition(value: Any) -> list[list[list[int]]]:
    if type(value) is not list:
        _fail("pair partition must be a list")
    converted = [
        [[left - 1, right - 1] for left, right in orbit]
        for orbit in value
    ]
    return sorted(converted, key=lambda orbit: (len(orbit), orbit))


def _build_g3(
    group: dict[str, Any], resolver: dict[str, Any]
) -> dict[str, Any]:
    source = _require_keys(
        group["G3_orbit_partition_obstruction"],
        {
            "H302_pair_partition_equals_N", "H302_point_partition_equals_N",
            "field_order", "pair_partitions", "point_partitions",
            "transported_N303_pair_partition",
            "transported_N303_pair_partition_equals_N",
            "transported_N303_point_partition",
            "transported_N303_point_partition_equals_N",
        },
        "group G3",
    )
    if source["field_order"] != EXPECTED_FIELD_ORDER:
        _fail("C60 partition field order changed")
    if (
        type(source["point_partitions"]) is not list
        or len(source["point_partitions"]) != 5
        or type(source["pair_partitions"]) is not list
        or len(source["pair_partitions"]) != 5
    ):
        _fail("C60 partition carrier count changed")
    n_index = source["field_order"].index("N")
    h0_index = source["field_order"].index("H302")
    n_points = deepcopy(source["point_partitions"][n_index])
    h0_points = deepcopy(source["point_partitions"][h0_index])
    n_pairs = deepcopy(source["pair_partitions"][n_index])
    h0_pairs = deepcopy(source["pair_partitions"][h0_index])
    if (
        not c60_exact.deep_exact(n_points, h0_points)
        or not c60_exact.deep_exact(n_pairs, h0_pairs)
        or source["H302_point_partition_equals_N"] is not True
        or source["H302_pair_partition_equals_N"] is not True
    ):
        _fail("C60 H0/N actual point or pair partitions differ")

    n_points_zero = _zero_based_point_partition(n_points)
    h0_points_zero = _zero_based_point_partition(h0_points)
    n_pairs_zero = _zero_based_pair_partition(n_pairs)
    h0_pairs_zero = _zero_based_pair_partition(h0_pairs)
    obstruction = resolver["payload"]["invariant_degree_obstruction"]
    if (
        _canonical_payload_sha256(h0_points_zero)
        != obstruction["H0_point_partition_sha256"]
        or _canonical_payload_sha256(h0_pairs_zero)
        != obstruction["H0_pair_partition_sha256"]
        or obstruction["H0_point_orbit_sizes"]
        != [len(orbit) for orbit in h0_points_zero]
        or obstruction["H0_pair_orbit_sizes"]
        != [len(orbit) for orbit in h0_pairs_zero]
        or obstruction["H0_and_N_point_partitions_equal"] is not True
        or obstruction[
            "H0_and_N_unordered_pair_partitions_equal"
        ] is not True
    ):
        _fail("C60 resolver partition hashes do not match group partitions")
    direct = group["independent_replay"]["python"]["direct_projection"]
    for label, value in (("N", n_points), ("H302", h0_points)):
        if _canonical_payload_sha256(value) != (
            direct["point_partition_sha256"][label]
        ):
            _fail(f"C60 one-based point partition hash changed: {label}")
    for label, value in (("N", n_pairs), ("H302", h0_pairs)):
        if _canonical_payload_sha256(value) != (
            direct["pair_partition_sha256"][label]
        ):
            _fail(f"C60 one-based pair partition hash changed: {label}")

    cubic = _carrier_record(
        resolver["payload"]["carriers"]["F0"], "selected H0 cubic carrier"
    )
    if (
        obstruction["selected_cubic_orbit_size"] != 27
        or obstruction["selected_cubic_support_sha256"]
        != cubic["carrier_sha256"]
        or cubic["carrier_sha256"] != EXPECTED_CARRIER_HASHES["F0"]
        or cubic["monomial_degree"] != 3
        or cubic["nonzero_monomial_count"] != 27
        or cubic["stabilizer_order"] != 162
        or cubic["stabilizer_equals_expected"] is not True
    ):
        _fail("C60 selected cubic escape changed")
    if (
        source["transported_N303_point_partition_equals_N"] is not True
        or source["transported_N303_pair_partition_equals_N"] is not True
        or not c60_exact.deep_exact(
            source["transported_N303_point_partition"], n_points
        )
        or not c60_exact.deep_exact(
            source["transported_N303_pair_partition"], n_pairs
        )
    ):
        _fail("C60 transported Hminus normalizer partition changed")

    return {
        "field_order": deepcopy(source["field_order"]),
        "actual_one_based_partitions": {
            "N_point_partition": n_points,
            "H0_point_partition": h0_points,
            "N_unordered_pair_partition": n_pairs,
            "H0_unordered_pair_partition": h0_pairs,
            "H0_and_N_point_partitions_deep_equal": True,
            "H0_and_N_unordered_pair_partitions_deep_equal": True,
        },
        "canonical_zero_based_partitions": {
            "N_point_partition": n_points_zero,
            "H0_point_partition": h0_points_zero,
            "N_unordered_pair_partition": n_pairs_zero,
            "H0_unordered_pair_partition": h0_pairs_zero,
            "indexing_conversion": "one_based_labels_to_zero_based_labels",
            "partition_sort": "(orbit_size,orbit_members)",
        },
        "partition_hash_cross_check": {
            "group_one_based_point_sha256": {
                "N": direct["point_partition_sha256"]["N"],
                "H0": direct["point_partition_sha256"]["H302"],
            },
            "group_one_based_pair_sha256": {
                "N": direct["pair_partition_sha256"]["N"],
                "H0": direct["pair_partition_sha256"]["H302"],
            },
            "resolver_zero_based_point_sha256": obstruction[
                "H0_point_partition_sha256"
            ],
            "resolver_zero_based_pair_sha256": obstruction[
                "H0_pair_partition_sha256"
            ],
            "zero_based_point_hash_reconstructed": _canonical_payload_sha256(
                h0_points_zero
            ),
            "zero_based_pair_hash_reconstructed": _canonical_payload_sha256(
                h0_pairs_zero
            ),
        },
        "transported_source_normalizer_partitions": {
            "point_partition": deepcopy(
                source["transported_N303_point_partition"]
            ),
            "unordered_pair_partition": deepcopy(
                source["transported_N303_pair_partition"]
            ),
            "point_partition_equals_N": source[
                "transported_N303_point_partition_equals_N"
            ],
            "pair_partition_equals_N": source[
                "transported_N303_pair_partition_equals_N"
            ],
        },
        "degree_at_most_two_coefficient_orbits": {
            "constant_basis_covered": True,
            "linear_Xi_basis_covered_by_point_partition": True,
            "square_Xi2_basis_covered_by_point_partition": True,
            "mixed_XiXj_basis_covered_by_unordered_pair_partition": True,
            "formal_polynomial_scope": obstruction[
                "formal_polynomial_scope"
            ],
            "quotient_by_root_relations_claimed": False,
        },
        "exact_cubic_escape": {
            "carrier": cubic["carrier"],
            "carrier_sha256": cubic["carrier_sha256"],
            "monomial_degree": cubic["monomial_degree"],
            "nonzero_monomial_count": cubic[
                "nonzero_monomial_count"
            ],
            "selected_cubic_orbit_size": obstruction[
                "selected_cubic_orbit_size"
            ],
            "stabilizer_order": cubic["stabilizer_order"],
            "stabilizer_equals_H0": cubic[
                "stabilizer_equals_expected"
            ],
        },
    }


def _character_relation_record(source: Any) -> dict[str, Any]:
    source = _require_keys(
        source,
        {
            "H301_equals_H302", "H301_equals_H303", "class_count",
            "class_sizes", "coefficient_order_H301_H302_H303_J_N",
            "relation_zero_on_every_class", "vectors",
        },
        "group character relation",
    )
    vectors = _require_keys(
        source["vectors"], {"H301", "H302", "H303", "J", "N"},
        "group character vectors",
    )
    result = {
        "H301_equals_H302": source["H301_equals_H302"],
        "H301_equals_H303": source["H301_equals_H303"],
        "class_count": source["class_count"],
        "class_sizes": deepcopy(source["class_sizes"]),
        "coefficient_order_H301_H302_H303_J_N": deepcopy(
            source["coefficient_order_H301_H302_H303_J_N"]
        ),
        "relation_zero_on_every_class": source[
            "relation_zero_on_every_class"
        ],
        "vectors": {
            label: deepcopy(vectors[label])
            for label in ("H301", "H302", "H303", "J", "N")
        },
    }
    coefficients = result[
        "coefficient_order_H301_H302_H303_J_N"
    ]
    if (
        result["class_count"] != 25
        or len(result["class_sizes"]) != 25
        or sum(result["class_sizes"]) != 51840
        or coefficients != [-1, -1, -1, 1, 2]
        or result["H301_equals_H303"] is not True
        or result["H301_equals_H302"] is not False
        or result["relation_zero_on_every_class"] is not True
        or any(len(vector) != 25 for vector in result["vectors"].values())
    ):
        _fail("C60 complete character relation changed")
    labels = ["H301", "H302", "H303", "J", "N"]
    if any(
        sum(
            coefficients[index] * result["vectors"][label][position]
            for index, label in enumerate(labels)
        ) != 0
        for position in range(25)
    ):
        _fail("C60 V4 relation is not zero on every class")
    return result


def _build_g4(
    group: dict[str, Any], resolver: dict[str, Any]
) -> dict[str, Any]:
    source = group["G4_biquadratic_tower_characters"]
    fields = [
        _group_field_record(row, f"G4 field {index}")
        for index, row in enumerate(source["fields"])
    ]
    field_map = {row["label"]: row for row in fields}
    common = group["G1_common_normalizer_uniqueness"][
        "common_normalizer"
    ]
    intersection = source["intersection"]
    relation = _character_relation_record(source["character_relation"])
    bridge = resolver["payload"]["fixed_field_bridge"]
    if set(field_map) != {"H301", "H302", "H303"}:
        _fail("C60 field map changed")
    if any(row["core_order_in_W"] != 1 for row in fields):
        _fail("C60 degree-320 fixed fields no longer have normal closure K")
    if common["core_order_in_W"] != 1 or intersection["core_order_in_W"] != 1:
        _fail("C60 M/L normal-closure core changed")
    if (
        common["normalizer_order_in_W"] // common["order"] != 1
        or any(
            (324 // row["order"]) != 2
            or row["normalizer_equals_N"] is not True
            or row["normal_in_N"] is not True
            for row in fields
        )
        or intersection["normalizer_order_in_W"] // intersection["order"] != 4
        or common["quotient_by_J_id_group"] != [4, 2]
    ):
        _fail("C60 automorphism quotient ledger changed")
    if bridge["fixed_field_identities"] != {
        "F0": "Q(xi0)=K^H0",
        "L": "Q(lambda)=K^J",
        "M": "Q(mu)=K^N",
    }:
        _fail("C60 primitive fixed-field identities changed")

    return {
        "field_lattice": {
            "M": {
                "fixed_group": "N", "degree": 160,
                "contains": ["Q"], "contained_in": ["Fplus", "F0", "F3", "L"],
            },
            "Fplus": {
                "fixed_group": "H301", "degree": 320,
                "contains": ["M"], "contained_in": ["L"],
            },
            "F0": {
                "fixed_group": "H302", "degree": 320,
                "contains": ["M"], "contained_in": ["L"],
            },
            "F3": {
                "fixed_group": "H303", "degree": 320,
                "contains": ["M"], "contained_in": ["L"],
            },
            "L": {
                "fixed_group": "J", "degree": 640,
                "contains": ["M", "Fplus", "F0", "F3"],
                "contained_in": ["K"],
            },
            "index_two_subgroup_records": fields,
            "pairwise_generated_orders": deepcopy(
                source["pairwise_generated_orders"]
            ),
            "pairwise_intersection_orders": deepcopy(
                source["pairwise_intersection_orders"]
            ),
            "pairwise_intersections_equal_J": source[
                "pairwise_intersections_equal_J"
            ],
        },
        "normal_closures": {
            "M": {"core_order": common["core_order_in_W"], "normal_closure": "K"},
            "Fplus": {
                "core_order": field_map["H301"]["core_order_in_W"],
                "normal_closure": "K",
            },
            "F0": {
                "core_order": field_map["H302"]["core_order_in_W"],
                "normal_closure": "K",
            },
            "F3": {
                "core_order": field_map["H303"]["core_order_in_W"],
                "normal_closure": "K",
            },
            "L": {
                "core_order": intersection["core_order_in_W"],
                "normal_closure": "K",
            },
            "normal_closure_degree": 51840,
        },
        "automorphism_groups": {
            "M_over_Q": {
                "normalizer_quotient_order": 1, "group": "trivial",
            },
            "Fplus_over_Q": {
                "normalizer_quotient_order": 2, "group": "C2",
            },
            "F0_over_Q": {
                "normalizer_quotient_order": 2, "group": "C2",
            },
            "F3_over_Q": {
                "normalizer_quotient_order": 2, "group": "C2",
            },
            "L_over_Q": {
                "normalizer_quotient_order": 4,
                "id_group": deepcopy(common["quotient_by_J_id_group"]),
                "group": "V4",
            },
            "L_over_M": {
                "degree": 4, "id_group": [4, 2], "group": "V4",
            },
        },
        "primitive_fixed_field_bridge": {
            "identities": deepcopy(bridge["fixed_field_identities"]),
            "reason": bridge["fixed_field_reason"],
            "labelled_W_action_faithful": bridge[
                "labelled_W_action_faithful"
            ],
            "K_completely_split_witness": bridge[
                "K_completely_split_witness"
            ],
            "characteristic_zero_orbit_values_distinct": bridge[
                "characteristic_zero_orbit_values_distinct"
            ],
        },
        "complete_permutation_characters": relation,
        "rational_V4_Brauer_relation": {
            "coefficient_order_H301_H302_H303_J_N": deepcopy(
                relation[
                    "coefficient_order_H301_H302_H303_J_N"
                ]
            ),
            "formula": "[G/J]+2[G/N]=[G/H301]+[G/H302]+[G/H303]",
            "zero_on_all_25_classes": relation[
                "relation_zero_on_every_class"
            ],
        },
        "zeta_written_bridge": {
            "first_identity_target": (
                "zeta_L*zeta_M^2=zeta_Fplus*zeta_F0*zeta_F3"
            ),
            "Hplus_H3_character_equality": relation[
                "H301_equals_H303"
            ],
            "Hplus_H0_character_equality": relation[
                "H301_equals_H302"
            ],
            "second_identity_target": (
                "zeta_L*zeta_M^2=zeta_Fplus^2*zeta_F0"
            ),
            "Artin_formalism_is_written_step": True,
            "finite_G_set_isomorphism_claimed": False,
            "bad_Artin_Euler_inference_claimed": False,
        },
    }


def _global_field_record(row: Any, label: str) -> dict[str, Any]:
    row = _require_keys(
        row,
        {
            "conductor_exponents_p3_p5_A_B", "degree",
            "discriminant_factorization", "discriminant_positive", "field",
            "orbit_counts_I3_P3_Q3_I5_P5_C3_C2_Cinf",
            "signature_r1_r2",
        },
        label,
    )
    return {
        "conductor_exponents_p3_p5_A_B": deepcopy(
            row["conductor_exponents_p3_p5_A_B"]
        ),
        "degree": row["degree"],
        "discriminant_factorization": deepcopy(
            row["discriminant_factorization"]
        ),
        "discriminant_positive": row["discriminant_positive"],
        "field": row["field"],
        "orbit_counts_I3_P3_Q3_I5_P5_C3_C2_Cinf": deepcopy(
            row["orbit_counts_I3_P3_Q3_I5_P5_C3_C2_Cinf"]
        ),
        "signature_r1_r2": deepcopy(row["signature_r1_r2"]),
    }


def _derive_conductor_and_signature(row: dict[str, Any]) -> tuple[list[int], list[int]]:
    n = row["degree"]
    counts = row["orbit_counts_I3_P3_Q3_I5_P5_C3_C2_Cinf"]
    if type(counts) is not list or len(counts) != 8:
        _fail("C60 filtration orbit-count vector changed shape")
    i3, p3, q3, i5, p5, c3, c2, cinf = counts
    if (n - p3) % 2 or (3 * (n - p5)) % 4:
        _fail("C60 conductor formulas are not integral")
    exponents = [
        (n - i3) + (n - p3) // 2 + (n - q3),
        (n - i5) + 3 * (n - p5) // 4,
        n - c3,
        n - c2,
    ]
    signature = [2 * cinf - n, n - cinf]
    return exponents, signature


def _build_g5(group: dict[str, Any]) -> dict[str, Any]:
    source = group["G5_global_relative_discriminants"]
    global_source = _require_keys(
        source["global_arithmetic"],
        {
            "exact_prime_support", "fields",
            "local_subgroup_tom_order_I3_P3_Q3_I5_P5_C3_C2_Cinf",
        },
        "group G5 global arithmetic",
    )
    fields = [
        _global_field_record(row, f"G5 field {index}")
        for index, row in enumerate(global_source["fields"])
    ]
    if [row["field"] for row in fields] != EXPECTED_FIELD_ORDER:
        _fail("C60 global field order changed")
    support = [3, 5, 181, 283, 997, 1801, 2346241, LARGE_PRIME]
    if global_source["exact_prime_support"] != support:
        _fail("C60 exact absolute prime support changed")
    for row in fields:
        exponents, signature = _derive_conductor_and_signature(row)
        factorization = [
            [prime, exponent]
            for prime, exponent in zip(
                support,
                [
                    exponents[0], exponents[1], exponents[2], exponents[3],
                    exponents[2], exponents[3], exponents[2], exponents[3],
                ],
            )
        ]
        if (
            exponents != row["conductor_exponents_p3_p5_A_B"]
            or signature != row["signature_r1_r2"]
            or factorization != row["discriminant_factorization"]
            or row["discriminant_positive"] is not (signature[1] % 2 == 0)
        ):
            _fail(f"C60 global arithmetic derivation failed: {row['field']}")

    by_field = {row["field"]: row for row in fields}
    relatives: list[dict[str, Any]] = []
    for index, row in enumerate(source["relative_discriminants_over_N"]):
        row = _require_keys(
            row,
            {
                "field", "relative_degree_over_N",
                "relative_discriminant_exponents_p3_p5_A_B",
            },
            f"G5 relative row {index}",
        )
        field = row["field"]
        relative_degree = row["relative_degree_over_N"]
        derived = [
            value - relative_degree * base
            for value, base in zip(
                by_field[field]["conductor_exponents_p3_p5_A_B"],
                by_field["N"]["conductor_exponents_p3_p5_A_B"],
            )
        ]
        if (
            derived != row[
                "relative_discriminant_exponents_p3_p5_A_B"
            ]
            or derived != EXPECTED_RELATIVE_EXPONENTS[field]
        ):
            _fail(f"C60 relative discriminant derivation failed: {field}")
        relatives.append({
            "field": field,
            "relative_degree_over_N": relative_degree,
            "relative_discriminant_exponents_p3_p5_A_B": deepcopy(derived),
            "relative_discriminant_norm": f"3^{derived[0]}",
        })
    if [row["field"] for row in relatives] != EXPECTED_RELATIVE_FIELD_ORDER:
        _fail("C60 relative discriminant field order changed")
    if (
        relatives[0]["relative_discriminant_exponents_p3_p5_A_B"][0]
        + relatives[1]["relative_discriminant_exponents_p3_p5_A_B"][0]
        + relatives[2]["relative_discriminant_exponents_p3_p5_A_B"][0]
        != relatives[3]["relative_discriminant_exponents_p3_p5_A_B"][0]
    ):
        _fail("C60 3^(8+16+8)=3^32 relation failed")

    direct = group["independent_replay"]["python"]["direct_projection"]
    discriminants = _require_keys(
        direct["discriminants"], {"H301", "H302", "H303", "J", "N"},
        "direct discriminant hashes",
    )
    direct_records: dict[str, Any] = {}
    for label in EXPECTED_FIELD_ORDER:
        record = _require_keys(
            discriminants[label],
            {
                "decimal_no_newline_digits", "decimal_no_newline_sha256",
                "factorization_sha256", "positive",
            },
            f"direct discriminant {label}",
        )
        if (
            record["positive"] is not True
            or record["factorization_sha256"]
            != _canonical_payload_sha256(
                by_field[label]["discriminant_factorization"]
            )
        ):
            _fail(f"C60 direct discriminant cross-check failed: {label}")
        direct_records[label] = {
            "decimal_no_newline_digits": record[
                "decimal_no_newline_digits"
            ],
            "decimal_no_newline_sha256": record[
                "decimal_no_newline_sha256"
            ],
            "factorization_sha256": record["factorization_sha256"],
            "positive": record["positive"],
        }

    return {
        "filtration_group_tom_order_I3_P3_Q3_I5_P5_C3_C2_Cinf": deepcopy(
            global_source[
                "local_subgroup_tom_order_I3_P3_Q3_I5_P5_C3_C2_Cinf"
            ]
        ),
        "exact_absolute_prime_support": deepcopy(support),
        "absolute_fields": fields,
        "independent_decimal_and_factorization_hashes": direct_records,
        "relative_discriminants_over_M": relatives,
        "relative_norm_product_relation": {
            "left_exponents": [8, 16, 8],
            "right_exponent": 32,
            "identity": "3^(8+16+8)=3^32",
            "verified": True,
        },
        "discriminant_authority": (
            "PERMUTATION_CONDUCTOR_AND_FIELD_DISCRIMINANT_"
            "NOT_DEFINING_POLYNOMIAL_DISCRIMINANT"
        ),
    }


def _absolute_table_record(source: Any, label: str) -> dict[str, Any]:
    source = _require_keys(
        source,
        {
            "degree_total", "different_total", "factor_count",
            "rows_n_e_f_d_with_multiplicity",
        },
        label,
    )
    rows = deepcopy(source["rows_n_e_f_d_with_multiplicity"])
    if type(rows) is not list:
        _fail(f"{label} rows must be a list")
    degree = 0
    different = 0
    factors = 0
    for index, item in enumerate(rows):
        if (
            type(item) is not list or len(item) != 2
            or type(item[0]) is not list or len(item[0]) != 4
            or type(item[1]) is not int
            or any(type(value) is not int for value in item[0])
        ):
            _fail(f"{label} row {index} has wrong shape")
        row, multiplicity = item
        n, e, f, d = row
        if n != e * f or multiplicity <= 0:
            _fail(f"{label} row {index} violates n=e*f")
        degree += multiplicity * n
        # The absolute discriminant exponent is the residue-degree-weighted
        # sum of local different exponents, not the unweighted row sum.
        different += multiplicity * f * d
        factors += multiplicity
    if (
        degree != source["degree_total"]
        or different != source["different_total"]
        or factors != source["factor_count"]
    ):
        _fail(f"{label} total changed")
    return {
        "degree_total": source["degree_total"],
        "different_total": source["different_total"],
        "factor_count": source["factor_count"],
        "rows_n_e_f_d_with_multiplicity": rows,
    }


def _branch_record(
    source: Any,
    branch_name: str,
    expected_relative_exponents: list[int],
) -> dict[str, Any]:
    source = _require_keys(
        source,
        {"absolute_tables", "decomposition_tom_locator", "relative_tower_over_N"},
        f"G6 {branch_name}",
    )
    expected_locator = 140 if branch_name == "tom140" else 206
    if source["decomposition_tom_locator"] != expected_locator:
        _fail(f"C60 {branch_name} locator changed")
    absolute_tables = []
    for index, entry in enumerate(source["absolute_tables"]):
        entry = _require_keys(
            entry, {"field", "table"}, f"{branch_name} absolute entry {index}"
        )
        absolute_tables.append({
            "field": entry["field"],
            "table": _absolute_table_record(
                entry["table"], f"{branch_name} absolute {entry['field']}"
            ),
        })
    if [entry["field"] for entry in absolute_tables] != EXPECTED_FIELD_ORDER:
        _fail(f"C60 {branch_name} absolute field order changed")

    tower = _require_keys(
        source["relative_tower_over_N"],
        {
            "base_prime_count",
            "collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J",
            "relative_factor_counts_H301_H302_H303_J",
            "rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J",
        },
        f"{branch_name} relative tower",
    )
    rows = deepcopy(
        tower[
            "rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J"
        ]
    )
    if len(rows) != tower["base_prime_count"]:
        _fail(f"C60 {branch_name} base-prime row count changed")
    factor_counts = [0, 0, 0, 0]
    norm_exponents = [0, 0, 0, 0]
    relative_degrees = [2, 2, 2, 4]
    all_ramified_tame = True
    for row_index, entry in enumerate(rows):
        if (
            type(entry) is not list or len(entry) != 2
            or type(entry[0]) is not list or len(entry[0]) != 4
            or type(entry[1]) is not list or len(entry[1]) != 4
        ):
            _fail(f"C60 {branch_name} relative row shape changed")
        base = entry[0]
        base_n, base_e, base_f, base_d = base
        if base_n != base_e * base_f:
            _fail(f"C60 {branch_name} base row violates n=e*f")
        for field_index, relative in enumerate(entry[1]):
            if type(relative) is not list or len(relative) != 4:
                _fail(f"C60 {branch_name} relative tuple shape changed")
            g, e, f, d = relative
            if g * e * f != relative_degrees[field_index]:
                _fail(f"C60 {branch_name} relative degree changed")
            factor_counts[field_index] += g
            norm_exponents[field_index] += base_f * g * f * d
            if e > 1 and (e != 2 or d != 1):
                all_ramified_tame = False
    if (
        factor_counts != tower[
            "relative_factor_counts_H301_H302_H303_J"
        ]
        or norm_exponents != expected_relative_exponents
        or not all_ramified_tame
    ):
        _fail(f"C60 {branch_name} relative totals/tameness changed")

    collected = []
    counter: Counter[str] = Counter(
        json.dumps(entry, sort_keys=True, separators=(",", ":"))
        for entry in rows
    )
    first_by_key = {
        json.dumps(entry, sort_keys=True, separators=(",", ":")): entry
        for entry in rows
    }
    for key in sorted(
        counter,
        key=lambda item: json.loads(item),
    ):
        collected.append([deepcopy(first_by_key[key]), counter[key]])
    if not c60_exact.deep_exact(
        collected,
        tower[
            "collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J"
        ],
    ):
        _fail(f"C60 {branch_name} collected/full relative rows differ")
    return {
        "decomposition_tom_locator": source["decomposition_tom_locator"],
        "absolute_tables": absolute_tables,
        "relative_tower_over_M": {
            "base_prime_count": tower["base_prime_count"],
            "rows_base_n_e_f_d_then_relative_g_e_f_d_Fplus_F0_F3_L": rows,
            "collected_rows_with_multiplicity": collected,
            "relative_factor_counts_Fplus_F0_F3_L": factor_counts,
            "relative_discriminant_norm_exponents_Fplus_F0_F3_L": norm_exponents,
            "all_relative_ramified_rows_have_e2_d1": all_ramified_tame,
        },
    }


def _build_g6(group: dict[str, Any]) -> dict[str, Any]:
    source = _require_keys(
        group["G6_two_local_branches"],
        {"relative_field_order", "tom140", "tom206"},
        "group G6",
    )
    if source["relative_field_order"] != EXPECTED_RELATIVE_FIELD_ORDER:
        _fail("C60 relative local field order changed")
    expected = [8, 16, 8, 32]
    tom140 = _branch_record(source["tom140"], "tom140", expected)
    tom206 = _branch_record(source["tom206"], "tom206", expected)
    direct_hashes = group["independent_replay"]["python"][
        "direct_projection"
    ]["local_tower_sha256"]
    if (
        _canonical_payload_sha256(source["tom140"]["relative_tower_over_N"])
        != direct_hashes["tom140"]
        or _canonical_payload_sha256(
            source["tom206"]["relative_tower_over_N"]
        )
        != direct_hashes["tom206"]
    ):
        _fail("C60 local-tower independent hashes changed")
    return {
        "relative_field_order": ["Fplus", "F0", "F3", "L"],
        "source_group_field_order": deepcopy(source["relative_field_order"]),
        "tom140": tom140,
        "tom206": tom206,
        "independent_source_tower_sha256": {
            "tom140": direct_hashes["tom140"],
            "tom206": direct_hashes["tom206"],
        },
        "both_branches_reconcile_relative_norm_exponents": expected,
        "all_relative_ramified_rows_have_e2_d1": True,
        "d3_branch_selected": False,
        "local_fields_classified_by_nefd_rows": False,
    }


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(child) for child in value)
    if value is None or type(value) in (bool, int, str):
        return 1
    _fail(f"unsupported payload type: {type(value).__name__}")


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
    _fail(f"unsupported payload type: {type(value).__name__}")


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
        "payload_shape_sha256": c60_exact.sha256_bytes(
            c60_exact.canonical_leaf_bytes(shape_value(payload))
        ),
        "payload_top_level_keys": sorted(payload),
        "schema_id": SCHEMA_ID,
        "unknown_fields_rejected_by_full_leaf_rebuild": True,
    }

def _validate_source_contract_value(value: dict[str, Any]) -> None:
    value = _require_keys(
        value,
        {
            "entries", "entry_count", "exact_code_inventory",
            "exact_code_path_allowlist", "mode_policy", "schema_id",
            "self_reference_policy",
        },
        "source contract",
    )
    expected_paths = [f"code/{name}" for name in CODE_FILES]
    if (
        value["entry_count"] != 13
        or value["exact_code_inventory"] is not True
        or value["schema_id"] != "hcs-c60-source-contract-v1"
        or value["exact_code_path_allowlist"] != sorted(expected_paths)
        or value["mode_policy"]
        != "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644"
        or value["self_reference_policy"]
        != "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE"
        or type(value["entries"]) is not list
        or len(value["entries"]) != 13
    ):
        _fail("C60 source contract header changed")
    observed: list[str] = []
    for index, row in enumerate(value["entries"]):
        row = _require_keys(
            row, {"mode_octal", "path", "sha256", "size_bytes"},
            f"source contract entry {index}",
        )
        if (
            type(row["path"]) is not str
            or type(row["size_bytes"]) is not int
            or row["size_bytes"] <= 0
            or row["mode_octal"]
            != ("0755" if row["path"] == "code/run_all.sh" else "0644")
        ):
            _fail("C60 source contract entry type changed")
        _require_digest(row["sha256"], "C60 source digest")
        observed.append(row["path"])
    if observed != expected_paths:
        _fail("C60 exact 13-source entry order changed")


def _validate_g0_value(value: dict[str, Any]) -> None:
    value = _require_keys(
        value,
        {
            "all_released_full_inventories_rebound", "batch_target_lock",
            "fixed_predecessor_paths_only", "formal_target_lock",
            "protected_guard", "released_C59", "schema_id",
        },
        "G0",
    )
    if (
        value["all_released_full_inventories_rebound"] is not True
        or value["fixed_predecessor_paths_only"] is not True
        or value["schema_id"] != "hcs-c60-released-authority-rebind-v1"
    ):
        _fail("C60 G0 header changed")
    batch = _require_keys(
        value["batch_target_lock"], {"path", "sha256", "size_bytes"},
        "G0 Batch",
    )
    guard = _require_keys(
        value["protected_guard"], {"path", "sha256", "size_bytes"},
        "G0 guard",
    )
    formal = _require_keys(
        value["formal_target_lock"],
        {
            "aggregate_definition", "entries", "entry_count",
            "exact_formal_inventory", "markdown_aggregate_sha256",
            "route_path", "route_sha256", "route_size_bytes", "status",
            "target_lock_input_entry_count",
            "target_lock_input_ledger_sha256",
        },
        "G0 formal target lock",
    )
    if (
        batch["sha256"] != BATCH_SHA256
        or guard["sha256"] != GUARD_SHA256
        or formal["entry_count"] != 13
        or formal["exact_formal_inventory"] is not True
        or formal["markdown_aggregate_sha256"] != FORMAL_PACKAGE_SHA256
        or formal["route_sha256"] != ROUTE_SHA256
        or formal["target_lock_input_entry_count"] != 15
        or formal["target_lock_input_ledger_sha256"]
        != TARGET_LOCK_INPUT_LEDGER_SHA256
        or formal["status"] != "TARGET_LOCK_FORMAL_INPUT_PASS"
    ):
        _fail("C60 G0 formal/Batch/guard lock changed")
    released = _require_keys(
        value["released_C59"],
        {
            "archive_route", "candidate_id", "certificate_bundle",
            "full_manifest", "group_evidence", "implementation_commit",
            "implementation_commit_ancestor_of_release_commit", "live_route",
            "live_archive_route_identical", "release_commit",
            "release_commit_ancestor_of_current_HEAD",
            "released_object_projection", "resolver_evidence",
            "scoped_manifest", "status",
        },
        "G0 released C59",
    )
    if (
        released["candidate_id"] != "HCS-C59"
        or released["implementation_commit"] != C59_IMPLEMENTATION_COMMIT
        or released["release_commit"] != C59_RELEASE_COMMIT
        or released["implementation_commit_ancestor_of_release_commit"]
        is not True
        or released["release_commit_ancestor_of_current_HEAD"] is not True
        or released["live_archive_route_identical"] is not True
        or released["status"] != "RELEASE_FROZEN"
        or released["full_manifest"]["entry_count"] != 63
        or released["full_manifest"]["manifest_sha256"]
        != C59_FULL_MANIFEST_SHA256
        or released["scoped_manifest"]["entry_count"] != 20
        or released["scoped_manifest"]["manifest_sha256"]
        != C59_SCOPED_MANIFEST_SHA256
        or released["live_route"]["sha256"] != C59_ROUTE_SHA256
        or released["archive_route"]["sha256"] != C59_ROUTE_SHA256
        or released["group_evidence"]["sha256"]
        != C59_GROUP_EVIDENCE_SHA256
        or released["resolver_evidence"]["sha256"]
        != C59_RESOLVENT_EVIDENCE_SHA256
    ):
        _fail("C60 released C59 authority tuple changed")
    if _canonical_payload_sha256(value) != G0_REBOUND_SHA256:
        _fail("C60 exact G0 rebound payload changed")


def _base_g7(
    *,
    group_evidence: dict[str, Any],
    resolver_evidence: dict[str, Any],
    group_replay_sha256: str,
    group_evidence_sha256: str,
    resolver_evidence_sha256: str,
) -> dict[str, Any]:
    group_replay = group_evidence["independent_replay"]
    group_cross = group_replay["cross_checks"]
    group_gap = group_replay["gap_checker"]
    group_python = group_replay["python"]
    resolver_payload = resolver_evidence["payload"]
    resolver_replay = resolver_payload["replay_contract"]
    resolver_status = resolver_payload["status"]
    resolver_scope = resolver_payload["scope"]
    if (
        not all(type(flag) is bool and flag for flag in group_cross.values())
        or not all(
            type(flag) is bool and flag
            for flag in group_python["checks"].values()
        )
        or group_gap["two_run_deterministic"] is not True
        or group_python["status"] != "PASS"
        or resolver_replay["group_evidence_policy"]
        != "C60_GROUP_EVIDENCE_G3_CROSS_CHECK_REQUIRED"
        or resolver_status != {
            "evidence_status": "PASS",
            "implementation_state": "EVIDENCE_REPLAY_PASS",
            "release_authorized": False,
        }
        or any(
            flag is not False
            for key, flag in resolver_scope.items()
            if key != "scope_literal"
        )
        or resolver_scope["scope_literal"]
        != "NO_BAD_EULER_OR_ROOT_NUMBER"
    ):
        _fail("C60 component replay/scope status changed")
    return {
        "acyclic_hash_graph": True,
        "all_evidence_and_source_snapshots_stable_before_certificate_write": True,
        "certificate_root_exact_four_keys": True,
        "exact_payload_top_level_key_count": 15,
        "exact_source_file_count": 13,
        "exact_result_file_count": 8,
        "exact_live_code_results_file_count": 21,
        "planned_scoped_manifest_entries": 20,
        "producer_checker_theorem_call_graphs_disjoint": True,
        "checker_full_leaf_rebuild_required": True,
        "independent_check_report_policy": (
            "LATER_CHECK_REPORT_NOT_CERTIFICATE_INPUT"
        ),
        "later_manifest_self_excluding": True,
        "strict_exact_key_and_type_checks": True,
        "strict_parser_required": True,
        "component_contracts": {
            "group": {
                "aggregate_sha256": GROUP_COMPONENT["aggregate_sha256"],
                "producer_source_sha256": GROUP_COMPONENT["producer_sha256"],
                "independent_checker_source_sha256": GROUP_COMPONENT[
                    "checker_sha256"
                ],
                "evidence_sha256": group_evidence_sha256,
                "replay_projection_sha256": group_replay_sha256,
                "schema_sha256": GROUP_COMPONENT["schema_sha256"],
                "status": group_evidence["status"],
            },
            "primitive_resolvent": {
                "aggregate_sha256": RESOLVER_COMPONENT["aggregate_sha256"],
                "producer_source_sha256": RESOLVER_COMPONENT[
                    "producer_sha256"
                ],
                "independent_checker_source_sha256": RESOLVER_COMPONENT[
                    "checker_sha256"
                ],
                "evidence_sha256": resolver_evidence_sha256,
                "payload_sha256": resolver_evidence["payload_sha256"],
                "evidence_status": resolver_status["evidence_status"],
                "implementation_state": resolver_status[
                    "implementation_state"
                ],
                "release_authorized": resolver_status[
                    "release_authorized"
                ],
            },
        },
        "group_replay": {
            "cross_checks": {
                "C59_bytes_stable_across_replay": group_cross[
                    "C59_bytes_stable_across_replay"
                ],
                "GAP_two_run_deterministic": group_cross[
                    "GAP_two_run_deterministic"
                ],
                "Python_and_GAP_character_relation_agree": group_cross[
                    "Python_and_GAP_character_relation_agree"
                ],
                "Python_and_GAP_local_towers_deep_equal": group_cross[
                    "Python_and_GAP_local_towers_deep_equal"
                ],
                "Python_and_GAP_orbit_partitions_deep_equal": group_cross[
                    "Python_and_GAP_orbit_partitions_deep_equal"
                ],
                "Python_and_GAP_tower_groups_deep_equal": group_cross[
                    "Python_and_GAP_tower_groups_deep_equal"
                ],
            },
            "gap_checker": {
                "checker_projection_sha256": group_gap[
                    "checker_projection_sha256"
                ],
                "checker_projection_size_bytes": group_gap[
                    "checker_projection_size_bytes"
                ],
                "checker_source_sha256": group_gap[
                    "checker_source_sha256"
                ],
                "checker_source_size_bytes": group_gap[
                    "checker_source_size_bytes"
                ],
                "gap_executable_sha256": group_gap[
                    "gap_executable_sha256"
                ],
                "gap_executable_size_bytes": group_gap[
                    "gap_executable_size_bytes"
                ],
                "two_run_deterministic": group_gap[
                    "two_run_deterministic"
                ],
            },
            "python_checks": {
                "actual_pair_partitions_deep_equal": group_python["checks"][
                    "actual_pair_partitions_deep_equal"
                ],
                "actual_point_partitions_deep_equal": group_python["checks"][
                    "actual_point_partitions_deep_equal"
                ],
                "all_51840_element_character_relation": group_python[
                    "checks"
                ]["all_51840_element_character_relation"],
                "character_class_distribution_deep_equal": group_python[
                    "checks"
                ]["character_class_distribution_deep_equal"],
                "derived_subgroup_equals_J": group_python["checks"][
                    "derived_subgroup_equals_J"
                ],
                "exact_normalizers_deep_equal": group_python["checks"][
                    "exact_normalizers_deep_equal"
                ],
                "full_tom140_absolute_and_relative_tables_deep_equal": (
                    group_python["checks"][
                        "full_tom140_absolute_and_relative_tables_deep_equal"
                    ]
                ),
                "full_tom206_absolute_and_relative_tables_deep_equal": (
                    group_python["checks"][
                        "full_tom206_absolute_and_relative_tables_deep_equal"
                    ]
                ),
                "mutable_label_transport_deep_equal": group_python["checks"][
                    "mutable_label_transport_deep_equal"
                ],
            },
            "direct_projection_sha256": group_python[
                "direct_projection_sha256"
            ],
            "status": group_python["status"],
        },
        "resolver_replay": {
            "builder_basename": resolver_replay["builder_basename"],
            "canonical_stage_pattern": resolver_replay[
                "canonical_stage_pattern"
            ],
            "checker_basename": resolver_replay["checker_basename"],
            "durable_literals_source": resolver_replay[
                "durable_literals_source"
            ],
            "evidence_basename": resolver_replay["evidence_basename"],
            "group_evidence_policy": resolver_replay[
                "group_evidence_policy"
            ],
            "schema_basename": resolver_replay["schema_basename"],
        },
        "resolver_scope_cross_check": {
            "bad_artin_euler_claimed": resolver_scope[
                "bad_artin_euler_claimed"
            ],
            "bad_euler_or_root_number_claimed": resolver_scope[
                "bad_euler_or_root_number_claimed"
            ],
            "characteristic_zero_coefficients_claimed": resolver_scope[
                "characteristic_zero_coefficients_claimed"
            ],
            "class_number_claimed": resolver_scope["class_number_claimed"],
            "decomposition_frobenius_claimed": resolver_scope[
                "decomposition_frobenius_claimed"
            ],
            "local_fields_classified_by_tuples": resolver_scope[
                "local_fields_classified_by_tuples"
            ],
            "maximal_orders_claimed": resolver_scope[
                "maximal_orders_claimed"
            ],
            "root_number_claimed": resolver_scope[
                "root_number_claimed"
            ],
            "scope_literal": resolver_scope["scope_literal"],
            "target_selection_or_unpromoted_aids_are_authority": (
                resolver_scope[
                    "target_selection_or_unpromoted_aids_are_authority"
                ]
            ),
        },
        "payload_scalar_leaf_count": 0,
        "schema_scalar_leaf_count": 0,
        "evidence_rebound_mutation_count_expected": 10,
        "structural_mutation_count_expected": 14,
        "type_mutation_count_expected": 0,
        "value_mutation_count_expected": 0,
    }


def build_payload(
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
    """Build the exact path-free 15-key payload from nine rebound fixtures."""

    _validate_source_contract_value(source_contract_value)
    _validate_g0_value(g0)
    _validate_component_documents(group_evidence, resolver_evidence)
    _cross_bind_group_resolver(group_evidence, resolver_evidence)
    for value, expected, label in (
        (
            group_replay_sha256, GROUP_COMPONENT["replay_sha256"],
            "group replay digest",
        ),
        (
            group_evidence_sha256, GROUP_COMPONENT["evidence_sha256"],
            "group evidence digest",
        ),
        (
            resolver_evidence_sha256, RESOLVER_COMPONENT["evidence_sha256"],
            "resolver evidence digest",
        ),
    ):
        _require_digest(value, label)
        if value != expected:
            _fail(f"{label} changed")
    if (
        _canonical_report_sha256(group_evidence) != group_evidence_sha256
        or _canonical_report_sha256(resolver_evidence)
        != resolver_evidence_sha256
        or group_evidence["independent_replay"]["gap_checker"][
            "checker_projection_sha256"
        ] != group_replay_sha256
        or resolver_evidence["payload_sha256"]
        != RESOLVER_COMPONENT["payload_sha256"]
    ):
        _fail("C60 top-level evidence/replay rebound failed")

    artifact_contract_value = _require_keys(
        artifact_contract_value,
        {
            "artifact_count", "artifacts", "component_contracts",
            "immutable_inputs", "same_real_nonsymlink_parent", "schema_id",
            "source_owned_full_document_validation",
        },
        "artifact contract",
    )
    if (
        type(artifact_contract_value["artifacts"]) is not list
        or len(artifact_contract_value["artifacts"]) != 2
    ):
        _fail("C60 artifact contract row count changed")
    sizes = {
        row.get("path"): row.get("size_bytes")
        for row in artifact_contract_value["artifacts"]
        if type(row) is dict
    }
    expected_artifacts = _artifact_contract_from_documents(
        group_evidence,
        resolver_evidence,
        group_size_bytes=sizes.get("results/c60_group_evidence.json"),
        resolver_size_bytes=sizes.get(
            "results/c60_resolvent_evidence.json"
        ),
    )
    if not c60_exact.deep_exact(artifact_contract_value, expected_artifacts):
        _fail("C60 artifact contract is not the full rebound contract")

    backend_contract_value = _require_keys(
        backend_contract_value,
        {
            "gap", "math_python", "pari_dependency", "schema_id",
            "singular_dependency", "two_run_deterministic",
        },
        "backend contract",
    )
    math_backend = _require_keys(
        backend_contract_value["math_python"],
        {
            "executable_sha256", "executable_size_bytes",
            "resolved_executable", "versions",
        },
        "math backend contract",
    )
    gap_backend = _require_keys(
        backend_contract_value["gap"],
        {
            "ctbllib_version", "executable_sha256", "executable_size_bytes",
            "gap_version", "resolved_executable", "smallgrp_version",
            "tomlib_version",
        },
        "GAP backend contract",
    )
    expected_math = c60_pipeline.EXPECTED_BACKENDS["math"]
    expected_versions = {
        "backend": "FLINT_SYMPY_NETWORKX",
        "python": expected_math["python"],
        "flint": expected_math["flint"],
        "sympy": expected_math["sympy"],
        "networkx": expected_math["networkx"],
        "jsonschema": expected_math["jsonschema"],
    }
    if (
        backend_contract_value["schema_id"]
        != "hcs-c60-backend-contract-v1"
        or backend_contract_value["two_run_deterministic"] is not True
        or backend_contract_value["pari_dependency"] is not False
        or backend_contract_value["singular_dependency"] is not False
        or type(math_backend["resolved_executable"]) is not str
        or not Path(math_backend["resolved_executable"]).is_absolute()
        or math_backend["executable_sha256"]
        != expected_math["executable_sha256"]
        or math_backend["executable_size_bytes"]
        != expected_math["executable_size_bytes"]
        or not c60_exact.deep_exact(
            math_backend["versions"], expected_versions
        )
        or not c60_exact.deep_exact(
            gap_backend, c60_pipeline.EXPECTED_GAP
        )
    ):
        _fail("C60 backend contract changed")

    g1 = _build_g1(group_evidence, resolver_evidence)
    g2 = _build_g2(group_evidence, resolver_evidence, g0)
    g3 = _build_g3(group_evidence, resolver_evidence)
    g4 = _build_g4(group_evidence, resolver_evidence)
    g5 = _build_g5(group_evidence)
    g6 = _build_g6(group_evidence)
    g7 = _base_g7(
        group_evidence=group_evidence,
        resolver_evidence=resolver_evidence,
        group_replay_sha256=group_replay_sha256,
        group_evidence_sha256=group_evidence_sha256,
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
        "written_bridges": {
            key: True for key in sorted(WRITTEN_BRIDGE_KEYS)
        },
        "backend_contract": deepcopy(backend_contract_value),
        "source_contract": deepcopy(source_contract_value),
        "scope_nonclaims": {
            key: False for key in sorted(SCOPE_NONCLAIM_KEYS)
        },
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
            "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "selection_aids": "CHRONOLOGY_ONLY_NOT_THEOREM_AUTHORITY",
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
    if tuple(payload) != PAYLOAD_KEYS:
        _fail("payload does not have the exact ordered 15-key contract")
    if (
        len(payload["scope_nonclaims"]) != 30
        or any(
            type(flag) is not bool or flag
            for flag in payload["scope_nonclaims"].values()
        )
    ):
        _fail("C60 exact 30-false scope firewall changed")
    if len(payload["written_bridges"]) != 7 or not all(
        payload["written_bridges"].values()
    ):
        _fail("C60 exact seven written bridges changed")

    payload_leaves = scalar_leaf_count(payload)
    g7["payload_scalar_leaf_count"] = payload_leaves
    schema_leaves = scalar_leaf_count(schema_descriptor(payload))
    g7["schema_scalar_leaf_count"] = schema_leaves
    scalar_mutations = payload_leaves + schema_leaves + 2
    g7["value_mutation_count_expected"] = scalar_mutations
    g7["type_mutation_count_expected"] = scalar_mutations
    if (
        scalar_leaf_count(payload) != payload_leaves
        or scalar_leaf_count(schema_descriptor(payload)) != schema_leaves
    ):
        _fail("payload/schema scalar-count fixed point failed")
    return payload


def _run_stage_bound_child(
    binding: StageBinding,
    command: Sequence[str],
    *,
    label: str,
) -> bytes:
    binding.assert_unchanged(f"before {label}")
    try:
        completed = subprocess.run(
            list(command),
            cwd=Path("/"),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=c60_pipeline.clean_environment(),
            check=False,
            timeout=60,
        )
    finally:
        binding.assert_unchanged(f"after {label}")
    if completed.returncode != 0 or completed.stderr:
        _fail(
            f"{label} failed or emitted stderr: "
            f"returncode={completed.returncode}, stderr={completed.stderr[:1000]!r}"
        )
    if len(completed.stdout) > 100_000:
        _fail(f"{label} emitted oversized stdout")
    return completed.stdout


def _backend_contract(
    math_python: Path,
    gap_path: Path,
    binding: StageBinding,
) -> dict[str, Any]:
    math = c60_pipeline.executable(math_python, "FLINT/SymPy/NetworkX")
    gap = c60_pipeline.executable(gap_path, "GAP")
    math_raw, math_fp = _stable_bytes(math, max_bytes=40_000_000)
    gap_raw, gap_fp = _stable_bytes(gap, max_bytes=1_000_000)
    expected_math = c60_pipeline.EXPECTED_BACKENDS["math"]
    if (
        c60_exact.sha256_bytes(math_raw) != expected_math["executable_sha256"]
        or math_fp.size_bytes != expected_math["executable_size_bytes"]
        or c60_exact.sha256_bytes(gap_raw)
        != c60_pipeline.EXPECTED_GAP["executable_sha256"]
        or gap_fp.size_bytes
        != c60_pipeline.EXPECTED_GAP["executable_size_bytes"]
    ):
        _fail("backend executable bytes changed")
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
        _run_stage_bound_child(
            binding,
            [str(math), "-s", "-B", "-c", python_source],
            label=f"math Python preflight run {index}",
        )
        for index in (1, 2)
    ]
    if python_runs[0] != python_runs[1]:
        _fail("math Python preflight is nondeterministic")
    python_value = c60_exact.strict_json_loads(
        python_runs[0].strip(), max_bytes=10_000
    )
    expected_python = {
        "backend": "FLINT_SYMPY_NETWORKX",
        "python": expected_math["python"],
        "flint": expected_math["flint"],
        "sympy": expected_math["sympy"],
        "networkx": expected_math["networkx"],
        "jsonschema": expected_math["jsonschema"],
    }
    if not c60_exact.deep_exact(python_value, expected_python):
        _fail("math Python versions changed")
    gap_source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",'
        'PackageInfo("ctbllib")[1].Version,"\\n");QUIT;'
    )
    gap_runs = [
        _run_stage_bound_child(
            binding,
            [str(gap), "-q", "-c", gap_source],
            label=f"GAP preflight run {index}",
        )
        for index in (1, 2)
    ]
    if gap_runs[0] != gap_runs[1]:
        _fail("GAP preflight is nondeterministic")
    try:
        fields = gap_runs[0].decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise c60_exact.StrictDataError("GAP preflight output is not ASCII") from exc
    observed_gap = {
        "resolved_executable": str(gap),
        "executable_sha256": c60_exact.sha256_bytes(gap_raw),
        "executable_size_bytes": gap_fp.size_bytes,
        "gap_version": fields[0] if len(fields) == 4 else "",
        "tomlib_version": fields[1] if len(fields) == 4 else "",
        "smallgrp_version": fields[2] if len(fields) == 4 else "",
        "ctbllib_version": fields[3] if len(fields) == 4 else "",
    }
    if not c60_exact.deep_exact(observed_gap, c60_pipeline.EXPECTED_GAP):
        _fail("GAP versions or executable identity changed")
    final_math_raw, final_math_fp = _stable_bytes(
        math, max_bytes=40_000_000
    )
    final_gap_raw, final_gap_fp = _stable_bytes(gap, max_bytes=1_000_000)
    if (
        final_math_raw != math_raw
        or final_math_fp != math_fp
        or final_gap_raw != gap_raw
        or final_gap_fp != gap_fp
    ):
        _fail("backend executable changed during deterministic preflight")
    binding.assert_unchanged("at backend-contract return")
    return {
        "schema_id": "hcs-c60-backend-contract-v1",
        "math_python": {
            "resolved_executable": str(math),
            "executable_sha256": c60_exact.sha256_bytes(math_raw),
            "executable_size_bytes": math_fp.size_bytes,
            "versions": python_value,
        },
        "gap": observed_gap,
        "two_run_deterministic": True,
        "pari_dependency": False,
        "singular_dependency": False,
    }


def assemble_payload(
    artifact_dir: Path,
    math_python: Path,
    gap: Path,
) -> dict[str, Any]:
    """Rebind live authority/evidence and call the path-free fixture builder."""

    namespace = argparse.Namespace(
        artifact_dir=Path(artifact_dir),
        output=Path(artifact_dir) / "c60_certificate.json",
        schema_output=Path(artifact_dir) / "c60_schema.json",
    )
    binding = validate_fixed_paths(namespace)
    source_before = source_contract()
    g0, written = rebuild_g0()
    if written != {key: True for key in WRITTEN_BRIDGE_KEYS}:
        _fail("formal written-bridge lock changed")
    artifacts, group, resolvent = artifact_contract(binding.parent)
    backends = _backend_contract(Path(math_python), Path(gap), binding)
    group_replay_sha256 = group["independent_replay"]["gap_checker"][
        "checker_projection_sha256"
    ]
    payload = build_payload(
        source_before,
        g0,
        artifacts,
        group,
        resolvent,
        backends,
        group_replay_sha256,
        binding.group_seal.sha256,
        binding.resolver_seal.sha256,
    )
    binding.assert_unchanged("after payload assembly")
    final_source = source_contract()
    final_g0, final_written = rebuild_g0()
    final_artifacts, final_group, final_resolvent = artifact_contract(binding.parent)
    if (
        not c60_exact.deep_exact(source_before, final_source)
        or not c60_exact.deep_exact(g0, final_g0)
        or written != final_written
        or not c60_exact.deep_exact(artifacts, final_artifacts)
        or not c60_exact.deep_exact(group, final_group)
        or not c60_exact.deep_exact(resolvent, final_resolvent)
    ):
        _fail("source, formal authority, or immutable evidence changed during assembly")
    binding.assert_unchanged("at payload assembly return")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-output", type=Path, required=True)
    parser.add_argument("--math-python", type=Path, required=True)
    parser.add_argument("--gap", type=Path, required=True)
    arguments = parser.parse_args()
    c60_exact.reject_optimized_python()
    binding = validate_fixed_paths(arguments)
    # The exact source gate precedes all output preparation, so an incomplete
    # staged implementation cannot delete even stale runner outputs.
    source_contract()
    payload = assemble_payload(
        binding.parent,
        arguments.math_python,
        arguments.gap,
    )
    schema = schema_descriptor(payload)
    certificate = {
        "schema": deepcopy(schema),
        "schema_sha256": c60_exact.sha256_bytes(
            c60_exact.canonical_leaf_bytes(schema)
        ),
        "payload": payload,
        "payload_sha256": c60_exact.sha256_bytes(
            c60_exact.canonical_leaf_bytes(payload)
        ),
    }
    schema_raw = c60_exact.canonical_json_bytes(schema, pretty=True)
    certificate_raw = c60_exact.canonical_json_bytes(certificate, pretty=True)
    if len(schema_raw) > 200_000 or len(certificate_raw) > MAX_CERTIFICATE_BYTES:
        _fail("generated schema or certificate exceeds its byte ceiling")
    binding.assert_unchanged("before final producer rebound")
    if (
        not c60_exact.deep_exact(payload["source_contract"], source_contract())
        or not c60_exact.deep_exact(
            payload["G0_released_authority_rebind"], rebuild_g0()[0]
        )
        or not c60_exact.deep_exact(
            payload["artifact_contract"], artifact_contract(binding.parent)[0]
        )
    ):
        _fail("producer authority changed before certificate/schema write")
    binding.assert_unchanged("immediately before output preparation")
    outputs = c60_exact.prepare_output_targets(
        (binding.output, binding.schema_output),
        protected=(binding.group_evidence, binding.resolvent_evidence),
    )
    try:
        c60_exact.atomic_write(outputs[1], schema_raw)
        c60_exact.atomic_write(outputs[0], certificate_raw)
        binding.assert_unchanged("after certificate/schema write")
        if (
            not c60_exact.deep_exact(
                payload["source_contract"], source_contract()
            )
            or not c60_exact.deep_exact(
                payload["G0_released_authority_rebind"], rebuild_g0()[0]
            )
            or not c60_exact.deep_exact(
                payload["artifact_contract"],
                artifact_contract(binding.parent)[0],
            )
        ):
            _fail("producer authority changed after certificate/schema write")
        binding.assert_unchanged("at producer success")
    except BaseException:
        for output in outputs:
            if output.exists() and output.is_file() and not output.is_symlink():
                output.unlink()
        raise
    print("C60 PRODUCER PASS PREFREEZE")
    print(f"payload_scalar_leaves={scalar_leaf_count(payload)}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    print(f"certificate_sha256={hashlib.sha256(certificate_raw).hexdigest()}")


if __name__ == "__main__":
    main()
