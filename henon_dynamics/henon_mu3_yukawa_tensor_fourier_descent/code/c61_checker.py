#!/usr/bin/env python3
"""Independent, fail-closed checker for the HCS-C61 machine tuple.

This verifier is deliberately producer-opaque.  It never imports, decodes,
parses, or executes the certificate producer.  It performs one stable raw-byte
read solely to bind that source's SHA-256, size, and filesystem identity.  Its
only local imports are the neutral exact-I/O/backend modules and the
independently written arithmetic checker.  The final GAP group checker is
executed as a bound child process.

The verifier reconstructs the complete certificate payload independently from
the installed authority and frozen component evidence.  The nonauthority
structure fixture is used only during checker development and is never a
runtime dependency.
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

# The checker must never create authority-adjacent bytecode caches, even when a
# caller forgets ``-B``.  This is set before the three local-module imports.
sys.dont_write_bytecode = True

import c61_checker_resolvent as checker_resolvent
import c61_exact as exact
import c61_pipeline as pipeline


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


CODE_DIR = Path(__file__).resolve().parent
PROJECT = CODE_DIR.parent
if (
    CODE_DIR.name == "code"
    and PROJECT.name == "henon_mu3_yukawa_tensor_fourier_descent"
    and PROJECT.parent.name == "henon_dynamics"
):
    REPO_ROOT = PROJECT.parents[1]
else:
    REPO_ROOT = Path("/__C61_STAGED_SOURCE_HAS_NO_REPOSITORY_AUTHORITY__")

HENON = REPO_ROOT / "henon_dynamics"
BATCH = HENON / "BATCH_PLAN_C57_C61.md"
GUARD = HENON / "codex_prompt.md"
C60 = HENON / "henon_mu3_yukawa_biquadratic_envelope"

C60_LOCK = {
    "archive_route_sha256": "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872",
    "certificate_sha256": "d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518",
    "certificate_size_bytes": 294_313,
    "check_sha256": "25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44",
    "check_size_bytes": 4_853,
    "full_manifest_entries": 88,
    "full_manifest_sha256": "37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4",
    "full_manifest_size_bytes": 8_714,
    "full_manifest_total_bytes": 2_058_684,
    "frozen_arrays_sha256": "0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5",
    "group_sha256": "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2",
    "group_size_bytes": 40_911,
    "l_carrier_sha256": "fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5",
    "payload_sha256": "dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead",
    "resolvent_sha256": "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da",
    "resolvent_size_bytes": 9_694,
    "route_sha256": "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872",
    "route_size_bytes": 26_005,
    "schema_sha256": "c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5",
    "schema_size_bytes": 1_007,
    "scoped_manifest_entries": 20,
    "scoped_manifest_sha256": "f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7",
    "scoped_manifest_size_bytes": 3_486,
    "source_contract_sha256": "4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90",
}

P60_LOCK = {
    "commit": "fe1217810b72840619efdf40a2af31b8b80d96f6",
    "parent": "f3b3726c40519cdd8ac7832f9f22df16d451b890",
    "tree": "22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a",
    "released_batch_sha256": "d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5",
    "released_batch_size_bytes": 34_176,
}

CERTIFICATE_SCHEMA_ID = "hcs-c61-certificate-schema-v1"
CHECK_REPORT_SCHEMA_ID = "hcs-c61-independent-check-report-v1"
GROUP_EVIDENCE_SCHEMA_ID = "hcs-c61-group-evidence-v1"
GROUP_PROJECTION_SCHEMA_ID = "hcs-c61-gap-group-projection-v1"
RESOLVER_EVIDENCE_SCHEMA_ID = "hcs-c61-resolvent-evidence-v1"

MAX_CERTIFICATE_BYTES = 8_000_000
MAX_SCHEMA_BYTES = 500_000
MAX_GROUP_EVIDENCE_BYTES = 2_000_000
MAX_RESOLVER_EVIDENCE_BYTES = 8_000_000
MAX_CHILD_STDOUT_BYTES = 12_000_000

PAYLOAD_KEYS = (
    "artifact_contract",
    "G0_released_authority_conventions_object",
    "G1_three_tensor_products_burnside",
    "G2_mixed_160_12_8_field_dictionary",
    "G3_product_form_resolvents_primitivity",
    "G4_fourier_kummer_type3_diamond",
    "G5_complete_global_arithmetic",
    "G6_both_local_branches_ideal_laws",
    "G7_independence_sources_scope_release",
    "written_bridges",
    "backend_contract",
    "source_contract",
    "scope_nonclaims",
    "nonresults",
    "status",
)

# Provisional owner-audited bytes used for the shared actual-CLI candidate.
# Any subsequent SOURCE_STABLE seal supersedes both values atomically.  The
# checker performs only a stable cryptographic byte read of this opaque source:
# it never decodes, parses, imports, or executes it.
CERTIFICATE_PRODUCER_SHA256: str | None = (
    "dadf8899f2fe82b65131a43ffbe438602db79a12654489b34d35ae8a6ee83d99"
)
CERTIFICATE_PRODUCER_SIZE_BYTES: int | None = 122_974

CODE_SOURCE_NAMES = {
    "README.md",
    "c61_atomic_promote.py",
    "c61_checker.py",
    "c61_checker_group.g",
    "c61_checker_resolvent.py",
    "c61_exact.py",
    "c61_group.py",
    "c61_hash_manifest.py",
    "c61_pipeline.py",
    "c61_producer.py",
    "c61_resolvent.py",
    "run_all.sh",
    "test_c61.py",
}
RESULT_NAMES = {
    "RESULTS.md",
    "TEST_REPORT.md",
    "c61_certificate.json",
    "c61_check_report.json",
    "c61_group_evidence.json",
    "c61_resolvent_evidence.json",
    "c61_schema.json",
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
ARTIFACT_NAMES = ("c61_group_evidence.json", "c61_resolvent_evidence.json")

GROUP_LOCK = {
    "aggregate_sha256": "f6fccf6aa815476a29193a5764ba4cac3916851ff68dbd9788620b6751b87208",
    "artifact_count": 4,
    "checker_sha256": "4fc377dc16f5b4ebec68767709d1e3e5e2a137b6694567f0b42cb9d88406862e",
    "checker_size_bytes": 13_364,
    "evidence_sha256": "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9",
    "evidence_size_bytes": 1_165_113,
    "producer_sha256": "64dfabdec2cf5767e4022c21a0ad7385efaa191df209c739ab7e015c46a83b5f",
    "producer_size_bytes": 100_679,
    "python_projection_sha256": "34ab65dadc1a2fe2b697d290f473b8fbb349b46b6772401eaef21ab8d9d0e970",
    "replay_sha256": "ebd3c174ecc76cb26792dfd24e547a59148f1d13e7a59d4f74a53f8bfb8c860b",
    "replay_size_bytes": 31_660,
    "total_bytes": 1_283_518,
}

RESOLVER_LOCK = {
    "aggregate_sha256": "b43f6902f7fec40d5d595ccab423f9d8260da2ade1824dc3d12ba006fd4bf74c",
    "artifact_count": 3,
    "checker_sha256": "f247dfdf393499c6a41df3dfa34815c1f4557781ec604639da47b921e90c9f6a",
    "checker_size_bytes": 64_892,
    "evidence_sha256": "1be0f9ac4e05ee7a747d39c546502d59dc29bb1407932e14875b61a3b82afe0f",
    "evidence_size_bytes": 594_163,
    "payload_sha256": "956f99f419e08f78d7b8c3304e840a90ca50ac7271635b5e46d9ba5c9c391918",
    "producer_sha256": "1c6e18ba4533908ef327cbc574e9d3b8268d1d0f2c9adf6ab2a9d6e86ae40c20",
    "producer_size_bytes": 91_639,
    "schema_sha256": "9925f23879bef26b6f5805ae2f0affe37785d5e569c929c706afaf80abdecf1d",
    "total_bytes": 750_694,
}

WRITTEN_BRIDGE_KEYS = {
    "both_D3_branches_to_relative_towers_and_primewise_ideal_laws",
    "conductor_orbits_to_signed_global_and_relative_discriminants",
    "fourier_characters_and_type3_to_degree_40_diamond",
    "mixed_160_12_8_atlas_to_fixed_field_dictionary",
    "released_P60_C60_to_target_object_and_conventions",
    "split_noncollision_and_stabilizers_to_primitive_fixed_fields",
    "three_tensor_atlases_to_burnside_and_zeta_products",
}

SCOPE_NONCLAIM_KEYS = {
    "artin_holomorphy_claimed",
    "automorphy_claimed",
    "bad_artin_euler_claimed",
    "brauer_manin_claimed",
    "characteristic_zero_coefficient_hash_claimed",
    "class_number_claimed",
    "d3_branch_selected",
    "decomposition_frobenius_claimed",
    "expanded_characteristic_zero_resolvent_claimed",
    "finite_g_sets_isomorphic_from_character_relation",
    "formal_invariant_statement_after_root_relations",
    "global_root_number_claimed",
    "hasse_principle_claimed",
    "hilbert_polya_operator_claimed",
    "integral_basis_claimed",
    "local_epsilon_factor_claimed",
    "local_fields_classified_by_nefd_rows",
    "local_root_number_claimed",
    "maximal_order_claimed",
    "monogenicity_claimed",
    "motive_claimed",
    "paper_complete_claimed",
    "rational_point_claimed",
    "raw_tom_defines_fields",
    "regulator_claimed",
    "release_claimed",
    "rh_claimed",
    "target_selection_pilot_is_theorem_authority",
    "trace_form_claimed",
    "weak_approximation_claimed",
}

if (
    len(PAYLOAD_KEYS) != 15
    or len(CODE_SOURCE_NAMES) != 13
    or len(RESULT_NAMES) != 8
    or len(FORMAL_MARKDOWN_NAMES) != 13
    or len(WRITTEN_BRIDGE_KEYS) != 7
    or len(SCOPE_NONCLAIM_KEYS) != 30
):
    raise RuntimeError("C61 frozen inventory cardinality changed")


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


@dataclass(frozen=True)
class OpaqueFileMetadataSeal:
    size_bytes: int
    mode: int
    mtime_ns: int
    ctime_ns: int
    device: int
    inode: int
    nlink: int


def seal_file(path: Path, *, max_bytes: int = 500_000_000) -> FileSeal:
    raw, fingerprint = exact.read_stable(path, max_bytes=max_bytes)
    metadata = path.stat()
    return FileSeal(
        sha256=exact.sha256_bytes(raw),
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
        raise exact.StrictDataError(f"required real directory missing: {path}")
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_DIRECTORY", 0)
    )
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        after = path.lstat()
    finally:
        os.close(descriptor)
    identity = (before.st_dev, before.st_ino)
    if identity != (opened.st_dev, opened.st_ino) or identity != (after.st_dev, after.st_ino):
        raise exact.StrictDataError(f"directory changed while binding: {path}")
    return DirectorySeal(
        mode=stat.S_IMODE(opened.st_mode),
        mtime_ns=opened.st_mtime_ns,
        ctime_ns=opened.st_ctime_ns,
        device=opened.st_dev,
        inode=opened.st_ino,
        nlink=opened.st_nlink,
    )


def seal_opaque_file_metadata(path: Path) -> OpaqueFileMetadataSeal:
    """Bind metadata for the one source that this checker is forbidden to read."""

    before = path.lstat()
    if path.is_symlink() or not stat.S_ISREG(before.st_mode):
        raise exact.StrictDataError("opaque certificate-producer source is not a regular file")
    after = path.lstat()
    fields = lambda value: (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_nlink,
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )
    if fields(before) != fields(after):
        raise exact.StrictDataError("opaque certificate-producer metadata changed while binding")
    return OpaqueFileMetadataSeal(
        size_bytes=before.st_size,
        mode=stat.S_IMODE(before.st_mode),
        mtime_ns=before.st_mtime_ns,
        ctime_ns=before.st_ctime_ns,
        device=before.st_dev,
        inode=before.st_ino,
        nlink=before.st_nlink,
    )


class SnapshotGuard:
    """Rebind protected bytes and metadata before and after every child."""

    def __init__(
        self,
        paths: Iterable[Path],
        *,
        directories: Iterable[Path] = (),
        opaque_paths: Iterable[Path] = (),
    ):
        self.paths = tuple(sorted({path.resolve(strict=True) for path in paths}, key=str))
        self.directories = tuple(sorted({path.absolute() for path in directories}, key=str))
        self.opaque_paths = tuple(sorted({path.absolute() for path in opaque_paths}, key=str))
        self.expected = self.capture()
        self.expected_directories = self.capture_directories()
        self.expected_opaque = self.capture_opaque()
        self.rebind_checks = 0

    def capture(self) -> dict[str, FileSeal]:
        return {str(path): seal_file(path) for path in self.paths}

    def capture_directories(self) -> dict[str, DirectorySeal]:
        return {str(path): seal_directory(path) for path in self.directories}

    def capture_opaque(self) -> dict[str, OpaqueFileMetadataSeal]:
        return {str(path): seal_opaque_file_metadata(path) for path in self.opaque_paths}

    def assert_unchanged(self, label: str) -> None:
        observed = self.capture()
        observed_directories = self.capture_directories()
        observed_opaque = self.capture_opaque()
        self.rebind_checks += 1
        if (
            observed != self.expected
            or observed_directories != self.expected_directories
            or observed_opaque != self.expected_opaque
        ):
            changed = sorted(
                set(observed) ^ set(self.expected)
                | {
                    key
                    for key in set(observed) & set(self.expected)
                    if observed[key] != self.expected[key]
                }
                | set(observed_directories) ^ set(self.expected_directories)
                | {
                    key
                    for key in set(observed_directories) & set(self.expected_directories)
                    if observed_directories[key] != self.expected_directories[key]
                }
                | set(observed_opaque) ^ set(self.expected_opaque)
                | {
                    key
                    for key in set(observed_opaque) & set(self.expected_opaque)
                    if observed_opaque[key] != self.expected_opaque[key]
                }
            )
            raise exact.StrictDataError(f"protected snapshot changed at {label}: {changed}")


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
            env=pipeline.clean_environment(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout,
        )
    finally:
        guard.assert_unchanged(f"after child {label}")
    if completed.returncode != 0:
        raise exact.StrictDataError(
            f"{label} failed with exit {completed.returncode}; stderr={completed.stderr[:1000]!r}"
        )
    if completed.stderr:
        raise exact.StrictDataError(f"{label} emitted stderr")
    if len(completed.stdout) > MAX_CHILD_STDOUT_BYTES:
        raise exact.StrictDataError(f"{label} stdout exceeds limit")
    return completed


def canonical_pretty(raw: bytes, *, max_bytes: int, label: str) -> Any:
    value = exact.strict_json_loads(raw, max_bytes=max_bytes)
    if raw != exact.canonical_json_bytes(value, pretty=True):
        raise exact.StrictDataError(f"{label} is not canonical pretty JSON")
    return value


def compact_document(raw: bytes, *, max_bytes: int, label: str) -> dict[str, Any]:
    value = exact.strict_json_loads(raw, max_bytes=max_bytes)
    exact.require_canonical_compact_json(raw)
    if type(value) is not dict:
        raise exact.StrictDataError(f"{label} must be an object")
    return value


def relative_to_repo(path: Path) -> str:
    try:
        return path.resolve(strict=True).relative_to(REPO_ROOT.resolve(strict=True)).as_posix()
    except (FileNotFoundError, ValueError) as exc:
        raise exact.StrictDataError(f"path is outside the bound repository: {path}") from exc


def file_binding(path: Path, expected_sha256: str) -> dict[str, Any]:
    bound = seal_file(path)
    if bound.sha256 != expected_sha256 or bound.mode != 0o644 or bound.nlink != 1:
        raise exact.StrictDataError(f"authority file binding changed: {path}")
    return {
        "path": relative_to_repo(path),
        "sha256": bound.sha256,
        "size_bytes": bound.size_bytes,
    }


def group_component_contract() -> dict[str, Any]:
    return {
        "aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
        "artifact_count": GROUP_LOCK["artifact_count"],
        "checker_sha256": GROUP_LOCK["checker_sha256"],
        "evidence_sha256": GROUP_LOCK["evidence_sha256"],
        "producer_sha256": GROUP_LOCK["producer_sha256"],
        "python_projection_sha256": GROUP_LOCK["python_projection_sha256"],
        "replay_sha256": GROUP_LOCK["replay_sha256"],
        "total_bytes": GROUP_LOCK["total_bytes"],
    }


def resolver_component_contract() -> dict[str, Any]:
    return {
        "aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
        "artifact_count": RESOLVER_LOCK["artifact_count"],
        "checker_sha256": RESOLVER_LOCK["checker_sha256"],
        "evidence_sha256": RESOLVER_LOCK["evidence_sha256"],
        "payload_sha256": RESOLVER_LOCK["payload_sha256"],
        "producer_sha256": RESOLVER_LOCK["producer_sha256"],
        "schema_sha256": RESOLVER_LOCK["schema_sha256"],
        "total_bytes": RESOLVER_LOCK["total_bytes"],
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
        raise exact.StrictDataError("C61 artifact basename mismatch")
    if (
        exact.sha256_bytes(group_raw) != GROUP_LOCK["evidence_sha256"]
        or len(group_raw) != GROUP_LOCK["evidence_size_bytes"]
        or exact.sha256_bytes(resolver_raw) != RESOLVER_LOCK["evidence_sha256"]
        or len(resolver_raw) != RESOLVER_LOCK["evidence_size_bytes"]
        or group_document["component_hashes"]["gap_projection_sha256"]
        != GROUP_LOCK["replay_sha256"]
        or resolver_document["payload_sha256"] != RESOLVER_LOCK["payload_sha256"]
        or resolver_document["schema_sha256"] != RESOLVER_LOCK["schema_sha256"]
    ):
        raise exact.StrictDataError("C61 final component tuple differs")
    return {
        "artifact_count": 2,
        "artifacts": [
            {
                "component_aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
                "format": "canonical_compact_json",
                "internal_report_sha256": GROUP_LOCK["replay_sha256"],
                "path": "results/c61_group_evidence.json",
                "schema_id": GROUP_EVIDENCE_SCHEMA_ID,
                "sha256": GROUP_LOCK["evidence_sha256"],
                "size_bytes": GROUP_LOCK["evidence_size_bytes"],
            },
            {
                "component_aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
                "format": "canonical_compact_json",
                "internal_report_sha256": RESOLVER_LOCK["payload_sha256"],
                "path": "results/c61_resolvent_evidence.json",
                "schema_descriptor_sha256": RESOLVER_LOCK["schema_sha256"],
                "schema_id": RESOLVER_EVIDENCE_SCHEMA_ID,
                "sha256": RESOLVER_LOCK["evidence_sha256"],
                "size_bytes": RESOLVER_LOCK["evidence_size_bytes"],
            },
        ],
        "component_contracts": {
            "fourier_resolvent": resolver_component_contract(),
            "group": group_component_contract(),
        },
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c61-artifact-contract-v1",
        "source_owned_full_document_validation": True,
    }


def validate_false_scope(scope: Any, *, allow_literal: bool, label: str) -> None:
    expected = set(SCOPE_NONCLAIM_KEYS)
    if allow_literal:
        expected.add("scope_literal")
    exact.require_exact_keys(scope, expected, label)
    if allow_literal and scope["scope_literal"] != "NO_BAD_EULER_OR_ROOT_NUMBER":
        raise exact.StrictDataError(f"{label} scope literal changed")
    if any(scope[key] is not False for key in SCOPE_NONCLAIM_KEYS):
        raise exact.StrictDataError(f"{label} has a true/nonboolean scope leaf")


def validate_group_document(document: dict[str, Any]) -> None:
    exact.require_exact_keys(
        document,
        {
            "backend_contract",
            "component_hashes",
            "conventions",
            "cross_checks",
            "gap_projection",
            "independence_contract",
            "lifecycle",
            "nonresults",
            "python_projection",
            "schema_id",
            "scope_nonclaims",
            "semantic_firewall",
            "source_contract",
            "status",
        },
        "C61 group evidence",
    )
    if (
        document["schema_id"] != GROUP_EVIDENCE_SCHEMA_ID
        or document["status"] != "STAGED_NONRELEASE_GROUP_COMPONENT"
        or document["semantic_firewall"] != "NO_BAD_EULER_OR_ROOT_NUMBER"
        or document["lifecycle"]
        != {
            "component": "GROUP_MACHINE_PASS",
            "paper": "PAPER_PENDING",
            "project": "IMPLEMENTATION_IN_PROGRESS",
            "promotion_authorized": False,
            "release": "NOT_RELEASED",
        }
    ):
        raise exact.StrictDataError("C61 group status/firewall/lifecycle mismatch")
    validate_false_scope(document["scope_nonclaims"], allow_literal=False, label="group")
    python_projection = document["python_projection"]
    gap_projection = document["gap_projection"]
    python_sha = exact.sha256_bytes(exact.canonical_leaf_bytes(python_projection))
    gap_sha = exact.sha256_bytes(exact.canonical_leaf_bytes(gap_projection))
    hashes = document["component_hashes"]
    source = document["source_contract"]
    formal = source["formal_input"]
    if (
        python_sha != GROUP_LOCK["python_projection_sha256"]
        or gap_sha != GROUP_LOCK["replay_sha256"]
        or hashes["python_projection_sha256"] != python_sha
        or hashes["gap_projection_sha256"] != gap_sha
        or python_projection["status"] != "PYTHON_RECONSTRUCTION_PASS"
        or gap_projection["status"] != "PASS"
        or document["conventions"]["target_degree_or_order_filters_used"] is not False
        or gap_projection["target_degree_or_order_filters_used"] is not False
        or document["independence_contract"]["no_target_degree_or_order_filters"] is not True
        or source["c60_frozen_arrays_sha256"] != C60_LOCK["frozen_arrays_sha256"]
        or source["c60_payload_sha256"] != C60_LOCK["payload_sha256"]
        or source["c60_source_contract_sha256"] != C60_LOCK["source_contract_sha256"]
        or source["c60_manifest_verification"]
        != {"all_entries_verified": True, "entry_count": 88}
        or source["pilot_runtime_inputs"] != []
        or formal["formal_13_root_sha256"]
        != pipeline.C61_TARGET_LOCK_AUTHORITY["formal_root13_aggregate_sha256"]
        or formal["formal_route_sha256"]
        != pipeline.C61_TARGET_LOCK_AUTHORITY["route_sha256"]
        or formal["formal_batch_sha256"]
        != pipeline.C61_TARGET_LOCK_AUTHORITY["batch_sha256"]
        or formal["formal_exact15_sha256"]
        != pipeline.C61_TARGET_LOCK_AUTHORITY["exact15_ledger_sha256"]
        or formal["formal_exact15_count"] != 15
        or formal["formal_root_count"] != 13
        or formal["all_installed_hashes_recomputed"] is not True
    ):
        raise exact.StrictDataError("C61 group projection/hash/filter contract mismatch")


def validate_resolver_document(document: dict[str, Any]) -> None:
    exact.require_exact_keys(
        document,
        {
            "GAF0_released_authority_rebind",
            "GAF1_fourier_carrier_dag",
            "GAF2_orbit_span_and_nonnormality",
            "GAF3_stabilizers_and_noncollision",
            "GAF4_mixed_type3_exact_bridge",
            "GAF5_fixed_field_diamond",
            "GAF6_global_arithmetic",
            "GAF7_both_local_branches_and_ideal_laws",
            "authority",
            "conventions",
            "independence_contract",
            "payload_sha256",
            "schema_id",
            "schema_sha256",
            "scope_nonclaims",
            "status",
        },
        "C61 resolver evidence",
    )
    if (
        document["schema_id"] != RESOLVER_EVIDENCE_SCHEMA_ID
        or document["payload_sha256"] != RESOLVER_LOCK["payload_sha256"]
        or document["schema_sha256"] != RESOLVER_LOCK["schema_sha256"]
        or document["status"]
        != {
            "G3_product_form_resolvents": "PASS",
            "G4_fourier_diamond": "PASS",
            "G5_global_arithmetic": "PASS",
            "G6_both_local_branches": "PASS",
            "integrated_C61_status": "IMPLEMENTATION_PENDING",
            "paper_status": "PAPER_PENDING",
            "promotion_authorized": False,
            "release_status": "NOT_RELEASED",
            "resolver_component_status": "RESOLVER_COMPONENT_PASS",
        }
    ):
        raise exact.StrictDataError("C61 resolver top-level contract mismatch")
    validate_false_scope(document["scope_nonclaims"], allow_literal=True, label="resolver")


def backend_contract(
    math_python: Path, gap_path: Path, guard: SnapshotGuard
) -> dict[str, Any]:
    math = pipeline.executable(math_python, "FLINT/SymPy/NetworkX")
    gap = pipeline.executable(gap_path, "GAP")
    math_seal = seal_file(math, max_bytes=40_000_000)
    gap_seal = seal_file(gap, max_bytes=1_000_000)
    expected_math = pipeline.EXPECTED_BACKENDS["math"]
    if (
        math_seal.sha256 != expected_math["executable_sha256"]
        or math_seal.size_bytes != expected_math["executable_size_bytes"]
        or gap_seal.sha256 != pipeline.EXPECTED_GAP["executable_sha256"]
        or gap_seal.size_bytes != pipeline.EXPECTED_GAP["executable_size_bytes"]
    ):
        raise exact.StrictDataError("C61 backend executable bytes changed")

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
            label=f"C61 math Python preflight run {index}",
        )
        for index in (1, 2)
    ]
    if python_runs[0].stdout != python_runs[1].stdout:
        raise exact.StrictDataError("C61 math Python preflight is nondeterministic")
    math_value = exact.strict_json_loads(
        python_runs[0].stdout.strip(), max_bytes=10_000
    )
    expected_versions = {
        "backend": "FLINT_SYMPY_NETWORKX",
        **{
            name: expected
            for name, expected in expected_math.items()
            if not name.startswith("executable_")
        },
    }
    if math_value != expected_versions:
        raise exact.StrictDataError(f"unsupported C61 math backend: {math_value}")
    math_result = {
        "resolved_executable": str(math),
        "versions": math_value,
        "executable_sha256": math_seal.sha256,
        "executable_size_bytes": math_seal.size_bytes,
    }

    gap_source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",'
        'PackageInfo("ctbllib")[1].Version,"\\n"); QUIT;'
    )
    gap_runs = [
        run_bound_child(
            guard,
            [str(gap), "-q", "-c", gap_source],
            cwd=Path("/"),
            timeout=60,
            label=f"C61 GAP preflight run {index}",
        )
        for index in (1, 2)
    ]
    if gap_runs[0].stdout != gap_runs[1].stdout:
        raise exact.StrictDataError("C61 GAP preflight is nondeterministic")
    try:
        fields = gap_runs[0].stdout.decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise exact.StrictDataError("C61 GAP preflight output is malformed") from exc
    if len(fields) != 4:
        raise exact.StrictDataError("C61 GAP preflight output field count differs")
    gap_result = {
        "resolved_executable": str(gap),
        "executable_sha256": gap_seal.sha256,
        "executable_size_bytes": gap_seal.size_bytes,
        "gap_version": fields[0],
        "tomlib_version": fields[1],
        "smallgrp_version": fields[2],
        "ctbllib_version": fields[3],
    }
    if gap_result != pipeline.EXPECTED_GAP:
        raise exact.StrictDataError(f"unsupported C61 GAP backend: {gap_result}")
    return {
        "gap": gap_result,
        "math_python": math_result,
        "pari_dependency": False,
        "schema_id": "hcs-c61-backend-contract-v1",
        "singular_dependency": False,
        "two_run_deterministic": True,
    }


def validate_group_component(
    document: dict[str, Any],
    evidence_path: Path,
    math_python: Path,
    gap_path: Path,
    guard: SnapshotGuard,
) -> dict[str, Any]:
    validate_group_document(document)
    group_source = CODE_DIR / "c61_group.py"
    gap_source = CODE_DIR / "c61_checker_group.g"
    source_seal = seal_file(group_source, max_bytes=2_000_000)
    gap_seal = seal_file(gap_source, max_bytes=1_000_000)
    if (
        source_seal.sha256 != GROUP_LOCK["producer_sha256"]
        or source_seal.size_bytes != GROUP_LOCK["producer_size_bytes"]
        or gap_seal.sha256 != GROUP_LOCK["checker_sha256"]
        or gap_seal.size_bytes != GROUP_LOCK["checker_size_bytes"]
        or source_seal.mode != 0o644
        or gap_seal.mode != 0o644
        or source_seal.nlink != 1
        or gap_seal.nlink != 1
    ):
        raise exact.StrictDataError("C61 group source/GAP checker tuple differs")
    source_run = run_bound_child(
        guard,
        [
            str(math_python.resolve(strict=True)),
            "-s",
            "-B",
            str(group_source),
            "validate",
            "--evidence",
            str(evidence_path),
            "--project-root",
            str(PROJECT),
        ],
        cwd=CODE_DIR,
        timeout=900,
        label="C61 group full-document source validation",
    )
    source_report = compact_document(
        source_run.stdout,
        max_bytes=100_000,
        label="C61 group validation report",
    )
    if (
        set(source_report) != {"evidence", "sha256", "status"}
        or source_report["sha256"] != GROUP_LOCK["evidence_sha256"]
        or source_report["status"] != "PASS"
    ):
        raise exact.StrictDataError("C61 group source validator report mismatch")
    gap_runs = [
        run_bound_child(
            guard,
            [str(gap_path.resolve(strict=True)), "-q", str(gap_source)],
            cwd=CODE_DIR,
            timeout=900,
            label=f"C61 independent GAP reconstruction run {index}",
        )
        for index in (1, 2)
    ]
    if gap_runs[0].stdout != gap_runs[1].stdout:
        raise exact.StrictDataError("C61 GAP reconstruction is nondeterministic")
    projection = compact_document(
        gap_runs[0].stdout,
        max_bytes=1_000_000,
        label="C61 GAP projection",
    )
    projection_sha = exact.sha256_bytes(exact.canonical_leaf_bytes(projection))
    if (
        projection_sha != GROUP_LOCK["replay_sha256"]
        or not exact.deep_exact(projection, document["gap_projection"])
    ):
        raise exact.StrictDataError("C61 independent GAP projection differs")
    return {
        "gap_projection_sha256": projection_sha,
        "group_source_validator_status": "PASS",
        "two_gap_runs_equal": True,
    }


def validate_resolver_component(
    document: dict[str, Any], evidence_path: Path, guard: SnapshotGuard
) -> dict[str, Any]:
    validate_resolver_document(document)
    resolver_source = CODE_DIR / "c61_resolvent.py"
    resolver_checker = CODE_DIR / "c61_checker_resolvent.py"
    source_seal = seal_file(resolver_source, max_bytes=2_000_000)
    checker_seal = seal_file(resolver_checker, max_bytes=2_000_000)
    if (
        source_seal.sha256 != RESOLVER_LOCK["producer_sha256"]
        or source_seal.size_bytes != RESOLVER_LOCK["producer_size_bytes"]
        or checker_seal.sha256 != RESOLVER_LOCK["checker_sha256"]
        or checker_seal.size_bytes != RESOLVER_LOCK["checker_size_bytes"]
        or source_seal.mode != 0o644
        or checker_seal.mode != 0o644
        or source_seal.nlink != 1
        or checker_seal.nlink != 1
    ):
        raise exact.StrictDataError("C61 resolver source/checker tuple differs")
    guard.assert_unchanged("before resolver full-document validation")
    try:
        report = checker_resolvent.validate_full_document(evidence_path)
    except checker_resolvent.Reject as exc:
        raise exact.StrictDataError("C61 resolver full-document validation failed") from exc
    finally:
        guard.assert_unchanged("after resolver full-document validation")
    expected = {
        "candidate_payload_sha256": document["independence_contract"][
            "checker_attestation"
        ]["candidate_payload_sha256"],
        "checker_status": "PASS",
        "evidence_payload_sha256": RESOLVER_LOCK["payload_sha256"],
        "release_status": "NOT_RELEASED",
        "resolver_component_status": "RESOLVER_COMPONENT_PASS",
        "schema_id": "hcs-c61-resolvent-final-check-v1",
    }
    if not exact.deep_exact(report, expected):
        raise exact.StrictDataError("C61 resolver full-document report mismatch")
    return report


def derive_g1(group_evidence: dict[str, Any]) -> dict[str, Any]:
    python_projection = group_evidence["python_projection"]
    gap_projection = group_evidence["gap_projection"]
    atlas = python_projection["tensor_atlas"]
    burnside = python_projection["burnside_linearization"]
    character = burnside["common_character_values_on_canonical_W"]
    tensor_character = burnside["common_tensor_character_values_on_canonical_W"]
    if (
        len(character) != 51_840
        or len(tensor_character) != 51_840
        or any(type(value) is not int for value in character + tensor_character)
        or tensor_character != [value * value for value in character]
        or exact.sha256_bytes(exact.canonical_leaf_bytes(character))
        != burnside["common_character_sha256"]
        or exact.sha256_bytes(exact.canonical_leaf_bytes(tensor_character))
        != burnside["common_tensor_character_sha256"]
        or character[0] != 320
        or tensor_character[0] != 102_400
        or gap_projection["burnside"]["common_character_values_on_25_classes"]
        != burnside.get("common_character_values_on_25_classes", gap_projection["burnside"]["common_character_values_on_25_classes"])
        or gap_projection["burnside"]["common_tensor_character_values_on_25_classes"]
        != [value * value for value in gap_projection["burnside"]["common_character_values_on_25_classes"]]
    ):
        raise exact.StrictDataError("C61 full Burnside character reconstruction mismatch")
    if (
        set(atlas["rows"]) != {"Tmm", "Tpm", "Tpp"}
        or any(len(atlas["rows"][lane]) != 12 for lane in atlas["rows"])
        or any(
            sum(row["simple_factor_degree"] for row in atlas["rows"][lane])
            != 102_400
            for lane in atlas["rows"]
        )
        or atlas["dimensions"] != {"Tmm": 102_400, "Tpm": 102_400, "Tpp": 102_400}
        or atlas["row_counts"] != {"Tmm": 12, "Tpm": 12, "Tpp": 12}
        or len(atlas["P_types"]) != 8
        or len(atlas["Q_types"]) != 18
        or group_evidence["cross_checks"]["tensor_rows_checked"] != 36
        or any(
            value is not True
            for key, value in group_evidence["cross_checks"].items()
            if key != "tensor_rows_checked"
        )
        or gap_projection["ambient"]
        != {
            "W_distinct_labelled_permutation_count": 51_840,
            "W_permutation_count": 51_840,
            "labelled_W_action_faithful": True,
        }
    ):
        raise exact.StrictDataError("C61 complete tensor-atlas reconstruction mismatch")
    burnside_output = {
        key: deepcopy(value)
        for key, value in burnside.items()
        if key
        not in {
            "common_character_values_on_canonical_W",
            "common_tensor_character_values_on_canonical_W",
        }
    }
    burnside_output.update(
        {
            "common_character_value_count": len(character),
            "common_character_values_on_25_GAP_classes": deepcopy(
                gap_projection["burnside"]["common_character_values_on_25_classes"]
            ),
            "common_tensor_character_value_count": len(tensor_character),
            "common_tensor_character_values_on_25_GAP_classes": deepcopy(
                gap_projection["burnside"]["common_tensor_character_values_on_25_classes"]
            ),
            "full_51840_value_arrays_validated_not_duplicated": True,
        }
    )
    return {
        "P3_P6_exact_distinction": deepcopy(python_projection["P3_P6"]),
        "P_type_count": len(atlas["P_types"]),
        "P_types": deepcopy(atlas["P_types"]),
        "Q_type_count": len(atlas["Q_types"]),
        "Q_type_multisets": deepcopy(atlas["Q_type_multisets"]),
        "Q_types": deepcopy(atlas["Q_types"]),
        "burnside_linearization": burnside_output,
        "degree_spectra": deepcopy(atlas["degree_spectra"]),
        "python_gap_cross_checks": deepcopy(group_evidence["cross_checks"]),
        "row_counts": deepcopy(atlas["row_counts"]),
        "schema_id": "hcs-c61-g1-tensor-burnside-v1",
        "status": "G1_PASS",
        "tensor_dimensions": deepcopy(atlas["dimensions"]),
        "tensor_rows": deepcopy(atlas["rows"]),
    }


def derive_g2(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> dict[str, Any]:
    python_projection = group_evidence["python_projection"]
    mixed = python_projection["mixed_160_12_8"]
    tensor_rows = python_projection["tensor_atlas"]["rows"]["Tpm"]
    resolver_rows = resolver_evidence["GAF4_mixed_type3_exact_bridge"]["mixed_rows"]
    if (
        mixed["conjugate_position_count"] != 160
        or len(mixed["conjugate_positions"]) != 160
        or mixed["double_coset_factor_count"] != 12
        or len(tensor_rows) != 12
        or len(resolver_rows) != 12
        or mixed["Q_isomorphism_type_count"] != 8
        or len(mixed["relative_position_types"]) != 8
        or sum(mixed["multiplicities"]) != 12
    ):
        raise exact.StrictDataError("C61 mixed 160/12/8 counts differ")
    resolver_by_seed = {row["seed"]: row for row in resolver_rows}
    if len(resolver_by_seed) != 12 or set(resolver_by_seed) != {row["seed"] for row in tensor_rows}:
        raise exact.StrictDataError("C61 mixed group/resolver seed registry differs")
    for group_row in tensor_rows:
        resolver_row = resolver_by_seed[group_row["seed"]]
        q_number = int(group_row["Q_type"][1:]) - 7
        if (
            resolver_row["representative_one_based"]
            != group_row["representative_one_based"]
            or resolver_row["simple_factor_degree"] != group_row["simple_factor_degree"]
            or resolver_row["intersection_field_degree"] != group_row["base_field_degree"]
            or resolver_row["intersection_order"] != group_row["intersection"]["order"]
            or resolver_row["intersection_sha256"]
            != group_row["intersection"]["group_sha256"]
            or resolver_row["join_order"] != group_row["join"]["order"]
            or resolver_row["join_sha256"] != group_row["join"]["group_sha256"]
            or resolver_row["q_isomorphism_type"] != q_number
            or resolver_row["tensor_right_coset_orbit_size"]
            != len(group_row["right_coset_orbit"])
        ):
            raise exact.StrictDataError("C61 mixed group/resolver row cross-binding differs")
    minimum = python_projection["mixed_degree_640_recovery"]
    maximum_rows = [row for row in tensor_rows if row["simple_factor_degree"] == 51_840]
    if (
        minimum["factor_degree"] != 640
        or minimum["base_degree"] != 160
        or len([row for row in tensor_rows if row["simple_factor_degree"] == 640]) != 1
        or len(maximum_rows) != 1
        or maximum_rows[0]["join"]["order"] != 51_840
        or any(row["intersection"]["core_order"] != 1 for row in tensor_rows)
    ):
        raise exact.StrictDataError("C61 mixed extremal/core-free claims differ")
    return {
        "Q_isomorphism_type_count": 8,
        "conjugate_position_count": 160,
        "conjugate_positions": deepcopy(mixed["conjugate_positions"]),
        "core_free_extension_for_all_eight_types": True,
        "double_coset_factor_count": 12,
        "group_resolver_complete_mixed_rows_cross_bound": True,
        "mixed_resolver_rows": deepcopy(resolver_rows),
        "mixed_tensor_rows": deepcopy(tensor_rows),
        "multiplicities": deepcopy(mixed["multiplicities"]),
        "relative_position_types": deepcopy(mixed["relative_position_types"]),
        "schema_id": "hcs-c61-g2-mixed-field-dictionary-v1",
        "status": "G2_PASS",
        "unique_maximum_factor_is_K": True,
        "unique_minimum_degree_640_recovery": deepcopy(minimum),
    }


def derive_g3(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> dict[str, Any]:
    product = resolver_evidence["GAF3_stabilizers_and_noncollision"][
        "product_form_mixed_base_A_B_resolvents"
    ]
    carriers = product["carriers"]
    expected_names = {"A40", "B80", "C1", "C2", "C3", "C4", *(f"E{i}" for i in range(1, 9))}
    if set(carriers) != expected_names or len(carriers) != 14:
        raise exact.StrictDataError("C61 exact fourteen-carrier registry differs")
    for name, carrier in carriers.items():
        if (
            carrier["field"] != name
            or carrier["formal_stabilizer_equals_embedded_subgroup"] is not True
            or carrier["complete_noncollision"] is not True
            or carrier["modular_distinct_value_count"] != carrier["degree"]
            or carrier["product_form_orbit_polynomial_factor_count"] != carrier["degree"]
            or carrier["exact_monomial_content"] != 1
            or carrier["integral"] is not True
            or carrier["regular_basis_vector_count"] != 51_840
            or carrier["characteristic_zero_expanded_coefficients_claimed"] is not False
        ):
            raise exact.StrictDataError(f"C61 product carrier invariant differs: {name}")
    if (
        product["all_14_advertised_carriers_reconstructed"] is not True
        or product["full_mod_p_orbit_evaluation_matrix"] != "identity"
        or group_evidence["python_projection"]["ambient"]["labelled_W_action_faithful"]
        is not True
        or product["split_prime"] != 692_717
        or product["runtime_pilot_dependency"] is not False
    ):
        raise exact.StrictDataError("C61 product-form global invariants differ")
    return {
        "all_Q_generator_fields_equal_exact_fixed_fields": True,
        "all_characteristic_zero_orbit_values_pairwise_distinct": True,
        "all_mod_p_orbit_values_pairwise_distinct": True,
        "carrier_count": 14,
        "carriers": deepcopy(carriers),
        "full_mod_p_orbit_evaluation_matrix": "identity",
        "integer_vanishing_polynomial_sha256": product[
            "integer_vanishing_polynomial_sha256"
        ],
        "labelled_W_action_faithful": True,
        "labelled_root_count": product["labelled_root_count"],
        "labelled_roots_sha256": product["labelled_roots_sha256"],
        "product_form_construction": (
            "source-owned regular Lagrange basis with invariant primitive-content marker"
        ),
        "proof_bridge": (
            "faithful_labelled_W_action_plus_exact_formal_stabilizer_plus_"
            "complete_split_mod_p_noncollision"
        ),
        "runtime_pilot_dependency": False,
        "schema_id": "hcs-c61-g3-product-resolvents-v1",
        "split_prime": 692_717,
        "split_prime_complete_split_authority": deepcopy(
            resolver_evidence["authority"]["released_C59_completely_split_prime_certificate"]
        ),
        "status": "G3_PASS",
        "univariate_lagrange_basis_sha256": product[
            "univariate_lagrange_basis_sha256"
        ],
    }


def derive_g4(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> dict[str, Any]:
    stabilizers = resolver_evidence["GAF3_stabilizers_and_noncollision"]
    mixed = resolver_evidence["GAF4_mixed_type3_exact_bridge"]
    group_seed = next(
        row
        for row in group_evidence["python_projection"]["tensor_atlas"]["rows"]["Tpm"]
        if row["seed"] == 149
    )
    if (
        mixed["exact_embedded_element_set_equality_Tmix_Tplus"] is not True
        or mixed["order_hash_or_conjugacy_alone_used"] is not False
        or mixed["unique_mixed_degree1920_row"] is not True
        or mixed["self_P3_substitute_hash_rejected"]
        != group_evidence["python_projection"]["P3_P6"]["plus_self_join_sha256"]
        or group_seed["join"]["group_sha256"] != mixed["Tmix_sha256"]
        or mixed["Tmix_sha256"] != mixed["Tplus_sha256"]
        or mixed["Tplus_sha256"] != stabilizers["Tplus"]["complete_group_sha256"]
        or mixed["factor_degree"] != 1_920
    ):
        raise exact.StrictDataError("C61 Fourier/type-3 exact bridge differs")
    return {
        "Splus_exact_stabilizer": deepcopy(stabilizers["Splus"]),
        "Tplus_exact_line_stabilizer": deepcopy(stabilizers["Tplus"]),
        "fixed_field_diamond": deepcopy(resolver_evidence["GAF5_fixed_field_diamond"]),
        "fourier_carrier_dag": deepcopy(resolver_evidence["GAF1_fourier_carrier_dag"]),
        "fourier_orbit_records": deepcopy(
            stabilizers["fourier_formal_and_evaluated_orbits"]
        ),
        "group_resolver_Tplus_complete_set_cross_bound": True,
        "mixed_type3_exact_bridge": deepcopy(mixed),
        "orbit_span_and_nonnormality": deepcopy(
            resolver_evidence["GAF2_orbit_span_and_nonnormality"]
        ),
        "schema_id": "hcs-c61-g4-fourier-diamond-v1",
        "status": "G4_PASS",
    }


FIELD_TYPE_MAPPING = {
    "B80": "P2",
    "C1": "P5",
    "C2": "P3",
    "C3": "P6",
    "C4": "P4",
    "E1": "Q8",
    "E2": "Q9",
    "E3": "Q10",
    "E4": "Q11",
    "E5": "Q12",
    "E6": "Q13",
    "E7": "Q14",
    "E8": "Q15",
}


def cross_validate_global_fields(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> None:
    group_rows = {
        row["type_label"]: row
        for row in group_evidence["python_projection"]["raw_global_local_inputs"][
            "field_type_rows"
        ]
    }
    resolver_fields = resolver_evidence["GAF6_global_arithmetic"]["fields"]
    if len(group_rows) != 26 or set(resolver_fields) != set(FIELD_TYPE_MAPPING):
        raise exact.StrictDataError("C61 raw/global field registry differs")
    for field, group_type in FIELD_TYPE_MAPPING.items():
        source = group_rows[group_type]
        result = resolver_fields[field]
        if (
            result["degree"] != source["degree"]
            or result["absolute_exponents_3_5_PiA_PiB"]
            != source["conductor_exponents"]
            or result["signature_r1_r2"] != source["signature_r1_r2"]
            or result["orbit_vector_I3_P3_Q3_I5_P5_C3_C2_Cinf"]
            != source["orbit_counts"]
            or result["discriminant_sign"]
            != (1 if source["discriminant_positive"] else -1)
        ):
            raise exact.StrictDataError(f"C61 global field cross-binding differs: {field}")


def derive_g5(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> dict[str, Any]:
    global_arithmetic = resolver_evidence["GAF6_global_arithmetic"]
    cross_validate_global_fields(group_evidence, resolver_evidence)
    group_orders = group_evidence["python_projection"]["raw_global_local_inputs"][
        "local_subgroups"
    ]
    if (
        len(global_arithmetic["exact_ramified_support"]) != 8
        or global_arithmetic["exact_ramified_support"][:2] != [3, 5]
        or global_arithmetic["filtration_order"]
        != ["I3", "P3", "Q3", "I5", "P5", "C3", "C2", "Cinf"]
        or any(
            global_arithmetic["filtration_group_orders"][name]
            != group_orders[name]["order"]
            for name in global_arithmetic["filtration_group_orders"]
        )
        or global_arithmetic["maximal_order_claimed"] is not False
    ):
        raise exact.StrictDataError("C61 global arithmetic support/filtration differs")
    public_mapping = {
        field: FIELD_TYPE_MAPPING[field]
        for field in ("C1", "C2", "C3", "C4", *(f"E{i}" for i in range(1, 9)))
    }
    return {
        "all_group_resolver_global_rows_cross_bound": True,
        "diamond_fields": deepcopy(global_arithmetic["diamond_fields"]),
        "diamond_relative_discriminant_norm_vectors": deepcopy(
            global_arithmetic["diamond_relative_discriminant_norm_vectors"]
        ),
        "diamond_route_via_B80": deepcopy(global_arithmetic["diamond_route_via_B80"]),
        "diamond_route_via_M160": deepcopy(global_arithmetic["diamond_route_via_M160"]),
        "exact_ramified_support": deepcopy(global_arithmetic["exact_ramified_support"]),
        "field_discriminants_not_polynomial_or_order_discriminants": True,
        "fields": deepcopy(global_arithmetic["fields"]),
        "filtration_group_orders": deepcopy(global_arithmetic["filtration_group_orders"]),
        "filtration_order": deepcopy(global_arithmetic["filtration_order"]),
        "filtration_tom_locators": deepcopy(global_arithmetic["filtration_tom_locators"]),
        "group_resolver_field_type_mapping": public_mapping,
        "maximal_order_claimed": False,
        "mixed_relative_discriminant_norm_vectors": deepcopy(
            global_arithmetic["mixed_relative_discriminant_norm_vectors"]
        ),
        "prime_products": deepcopy(global_arithmetic["prime_products"]),
        "schema_id": "hcs-c61-g5-global-arithmetic-v1",
        "status": "G5_PASS",
    }


def normalize_group_local_table(table: dict[str, Any]) -> dict[str, Any]:
    return {
        "collected_rows_with_multiplicity": [
            {
                "multiplicity": row["multiplicity"],
                "row_n_e_f_d": [row["n"], row["e"], row["f"], row["d"]],
            }
            for row in table["collected_rows"]
        ],
        "degree_total": table["degree_total"],
        "different_total": table["different_total"],
        "factor_count": table["factor_count"],
        "uncollected_prime_rows": [
            {
                "coset_seed": row["orbit_seed"],
                "prime_index": index,
                "row_n_e_f_d": [row["n"], row["e"], row["f"], row["d"]],
            }
            for index, row in enumerate(table["uncollected_rows"])
        ],
    }


def derive_g6(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> dict[str, Any]:
    local = resolver_evidence["GAF7_both_local_branches_and_ideal_laws"]
    absolute = local["absolute_local_tables"]
    group_rows = {
        row["type_label"]: row
        for row in group_evidence["python_projection"]["raw_global_local_inputs"][
            "field_type_rows"
        ]
    }
    if set(absolute) != {"ToM140", "ToM206"}:
        raise exact.StrictDataError("C61 exact two local branches differ")
    for branch, group_key in (("ToM140", "tom140"), ("ToM206", "tom206")):
        if set(absolute[branch]) != set(FIELD_TYPE_MAPPING):
            raise exact.StrictDataError(f"C61 absolute local field registry differs: {branch}")
        for field, group_type in FIELD_TYPE_MAPPING.items():
            expected = normalize_group_local_table(group_rows[group_type][group_key])
            if not exact.deep_exact(absolute[branch][field], expected):
                raise exact.StrictDataError(
                    f"C61 group/resolver absolute local row differs: {branch}/{field}"
                )
    commitments = {
        branch: exact.sha256_bytes(exact.canonical_leaf_bytes(absolute[branch]))
        for branch in sorted(absolute)
    }
    summaries = {
        branch: {
            field: {
                key: deepcopy(value)
                for key, value in absolute[branch][field].items()
                if key != "uncollected_prime_rows"
            }
            for field in sorted(absolute[branch])
        }
        for branch in sorted(absolute)
    }
    if (
        local["all_primewise_ideal_laws"] is not True
        or local["all_ramified_relative_rows_tame_e2_d1"] is not True
        or local["branch_selected"] is not False
        or local["local_fields_classified_by_nefd_rows"] is not False
        or local["retained_branches"] != ["ToM140", "ToM206"]
    ):
        raise exact.StrictDataError("C61 local branch/firewall contract differs")
    return {
        "V4_relative_towers_over_M": deepcopy(local["V4_relative_towers_over_M"]),
        "absolute_local_table_commitments": commitments,
        "absolute_local_table_summaries": summaries,
        "all_absolute_uncollected_rows_validated_not_duplicated": True,
        "all_primewise_ideal_laws": True,
        "all_ramified_relative_rows_tame_e2_d1": True,
        "archimedean_complementarity": deepcopy(local["archimedean_complementarity"]),
        "branch_selected": False,
        "expected_factor_counts": deepcopy(local["expected_factor_counts"]),
        "group_resolver_absolute_rows_cross_bound": True,
        "ideal_equalities": deepcopy(local["ideal_equalities"]),
        "local_fields_classified_by_nefd_rows": False,
        "retained_branches": deepcopy(local["retained_branches"]),
        "schema_id": "hcs-c61-g6-local-towers-v1",
        "status": "G6_PASS",
    }


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(child) for child in value)
    if value is None or type(value) in (bool, int, str):
        return 1
    raise exact.StrictDataError(f"unsupported certificate value: {type(value).__name__}")


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
    raise exact.StrictDataError(f"unsupported certificate value: {type(value).__name__}")


def schema_descriptor(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_id": CERTIFICATE_SCHEMA_ID,
        "payload_top_level_keys": list(PAYLOAD_KEYS),
        "payload_top_level_key_count": 15,
        "strict_json": True,
        "duplicate_keys_rejected": True,
        "floats_rejected": True,
        "booleans_rejected_in_integer_slots": True,
        "unknown_or_missing_fields_rejected": True,
        "scope_false_leaf_count": 30,
        "semantic_gate_count": 8,
        "written_bridge_count": 7,
        "component_artifact_count": 2,
        "source_entry_count": 13,
        "result_entry_count": 8,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
    }


def base_g7(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> dict[str, Any]:
    resolver_independence = resolver_evidence["independence_contract"]
    group_independence = group_evidence["independence_contract"]
    if (
        group_independence
        != {
            "arithmetic_resolvent_lane_must_duplicate_literals_and_reconstruct": True,
            "gap_tomlib_reconstructs_independently": True,
            "no_target_degree_or_order_filters": True,
            "pilots_or_tmp_runtime_authority": False,
            "python_reconstructs_all_groups_without_importing_released_code": True,
        }
        or resolver_independence["checker_imports_producer"] is not False
        or resolver_independence["shared_mathematical_helpers"] is not False
        or resolver_independence["producer_two_run_replay"] is not True
        or resolver_independence["checker_attestation_two_run_equal"] is not True
    ):
        raise exact.StrictDataError("C61 component independence contract differs")
    return {
        "component_documents_fully_source_validated": True,
        "evidence_rebound_mutation_count_expected": 10,
        "fourier_resolvent_component": {
            "component_contract": resolver_component_contract(),
            "evidence_sha256": RESOLVER_LOCK["evidence_sha256"],
            "independence_contract": deepcopy(resolver_independence),
            "payload_sha256": RESOLVER_LOCK["payload_sha256"],
        },
        "group_component": {
            "backend_contract": deepcopy(group_evidence["backend_contract"]),
            "component_contract": group_component_contract(),
            "evidence_sha256": GROUP_LOCK["evidence_sha256"],
            "independence_contract": deepcopy(group_independence),
            "replay_sha256": GROUP_LOCK["replay_sha256"],
        },
        "group_resolver_cross_bindings_reconstructed": True,
        "payload_scalar_leaf_count": 0,
        "producer_checker_shared_mathematical_helpers": False,
        "producer_imports_only_four_C61_modules": True,
        "schema_id": "hcs-c61-g7-independence-scope-release-v1",
        "schema_scalar_leaf_count": 0,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "status": "G7_PASS",
        "structural_mutation_count_expected": 14,
        "target_selection_or_unpromoted_aids_are_authority": False,
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
) -> dict[str, Any]:
    if not exact.deep_exact(
        artifact_contract_value,
        {
            "artifact_count": 2,
            "artifacts": [
                {
                    "component_aggregate_sha256": GROUP_LOCK["aggregate_sha256"],
                    "format": "canonical_compact_json",
                    "internal_report_sha256": GROUP_LOCK["replay_sha256"],
                    "path": "results/c61_group_evidence.json",
                    "schema_id": GROUP_EVIDENCE_SCHEMA_ID,
                    "sha256": GROUP_LOCK["evidence_sha256"],
                    "size_bytes": GROUP_LOCK["evidence_size_bytes"],
                },
                {
                    "component_aggregate_sha256": RESOLVER_LOCK["aggregate_sha256"],
                    "format": "canonical_compact_json",
                    "internal_report_sha256": RESOLVER_LOCK["payload_sha256"],
                    "path": "results/c61_resolvent_evidence.json",
                    "schema_descriptor_sha256": RESOLVER_LOCK["schema_sha256"],
                    "schema_id": RESOLVER_EVIDENCE_SCHEMA_ID,
                    "sha256": RESOLVER_LOCK["evidence_sha256"],
                    "size_bytes": RESOLVER_LOCK["evidence_size_bytes"],
                },
            ],
            "component_contracts": {
                "fourier_resolvent": resolver_component_contract(),
                "group": group_component_contract(),
            },
            "immutable_inputs": True,
            "same_real_nonsymlink_parent": True,
            "schema_id": "hcs-c61-artifact-contract-v1",
            "source_owned_full_document_validation": True,
        },
    ):
        raise exact.StrictDataError("C61 artifact contract argument differs")
    payload: dict[str, Any] = {
        "artifact_contract": deepcopy(artifact_contract_value),
        "G0_released_authority_conventions_object": deepcopy(g0),
        "G1_three_tensor_products_burnside": derive_g1(group_evidence),
        "G2_mixed_160_12_8_field_dictionary": derive_g2(
            group_evidence, resolver_evidence
        ),
        "G3_product_form_resolvents_primitivity": derive_g3(
            group_evidence, resolver_evidence
        ),
        "G4_fourier_kummer_type3_diamond": derive_g4(
            group_evidence, resolver_evidence
        ),
        "G5_complete_global_arithmetic": derive_g5(
            group_evidence, resolver_evidence
        ),
        "G6_both_local_branches_ideal_laws": derive_g6(
            group_evidence, resolver_evidence
        ),
        "G7_independence_sources_scope_release": base_g7(
            group_evidence, resolver_evidence
        ),
        "written_bridges": {key: True for key in sorted(WRITTEN_BRIDGE_KEYS)},
        "backend_contract": deepcopy(backend_contract_value),
        "source_contract": deepcopy(source_contract_value),
        "scope_nonclaims": {key: False for key in sorted(SCOPE_NONCLAIM_KEYS)},
        "nonresults": {
            "characteristic_zero_resolvents": (
                "UNEXPANDED_PRODUCT_FORM_WITH_COMPLETE_MODULAR_NONCOLLISION"
            ),
            "component_evidence_role": (
                "FULL_OBJECTS_REBOUND_AND_SEMANTIC_LEAVES_RECONSTRUCTED"
            ),
            "discriminant_authority": (
                "PERMUTATION_CONDUCTORS_NOT_DEFINING_POLYNOMIAL_DISCRIMINANTS"
            ),
            "finite_etale_scope": (
                "TENSOR_DECOMPOSITIONS_AND_ZETA_PRODUCTS_NOT_SINGLE_FIELDS"
            ),
            "local_row_scope": (
                "COMPLETE_ETALE_ALGEBRA_ROWS_NOT_INDIVIDUAL_FIELD_CLASSIFICATION"
            ),
            "selection_aids": "CHRONOLOGY_ONLY_NOT_THEOREM_AUTHORITY",
            "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "unsupported_machine_dependencies": ["PARI", "Singular"],
        },
        "status": {
            "candidate_id": "HCS-C61",
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "paper_status": "PAPER_BLOCKED_ON_POST_MACHINE_FORMAL_PASS",
            "promotion_authorized": False,
            "release_status": "NOT_RELEASED",
            "theorem_gate_count": 8,
        },
    }
    if tuple(payload) != PAYLOAD_KEYS:
        raise exact.StrictDataError("C61 payload insertion order differs from exact fifteen")
    payload_leaves = scalar_leaf_count(payload)
    if payload_leaves != 19_078:
        raise exact.StrictDataError(
            f"C61 payload scalar-leaf count differs before fixed point: {payload_leaves}"
        )
    g7 = payload["G7_independence_sources_scope_release"]
    g7["payload_scalar_leaf_count"] = payload_leaves
    schema_leaves = scalar_leaf_count(schema_descriptor(payload))
    if schema_leaves != 29:
        raise exact.StrictDataError("C61 schema scalar-leaf count differs")
    g7["schema_scalar_leaf_count"] = schema_leaves
    scalar_mutations = payload_leaves + schema_leaves + 2
    if scalar_mutations != 19_109:
        raise exact.StrictDataError("C61 scalar-mutation count differs")
    g7["value_mutation_count_expected"] = scalar_mutations
    g7["type_mutation_count_expected"] = scalar_mutations
    if (
        scalar_leaf_count(payload) != payload_leaves
        or scalar_leaf_count(schema_descriptor(payload)) != schema_leaves
    ):
        raise exact.StrictDataError("C61 payload/schema fixed point differs")
    return payload


def exact_source_contract() -> dict[str, Any]:
    """Rebuild exact13 with a hash-only read of the opaque certificate producer."""

    if CERTIFICATE_PRODUCER_SHA256 is None or CERTIFICATE_PRODUCER_SIZE_BYTES is None:
        raise exact.StrictDataError("certificate-producer SOURCE_STABLE seal is not installed")
    exact.require_sha256(CERTIFICATE_PRODUCER_SHA256, "certificate-producer source digest")
    if (
        not CODE_DIR.is_dir()
        or CODE_DIR.is_symlink()
        or CODE_DIR.resolve(strict=True) != CODE_DIR
    ):
        raise exact.StrictDataError("C61 code directory must be one canonical real directory")
    children = list(CODE_DIR.iterdir())
    names = {child.name for child in children}
    if names != CODE_SOURCE_NAMES:
        raise exact.StrictDataError(
            "C61 exact 13-source inventory mismatch; "
            f"missing={sorted(CODE_SOURCE_NAMES - names)} extra={sorted(names - CODE_SOURCE_NAMES)}"
        )
    entries: list[dict[str, Any]] = []
    for name in sorted(CODE_SOURCE_NAMES):
        path = CODE_DIR / name
        expected_mode = 0o755 if name == "run_all.sh" else 0o644
        if name == "c61_producer.py":
            bound = seal_file(path, max_bytes=8_000_000)
            if (
                bound.mode != expected_mode
                or bound.nlink != 1
                or bound.size_bytes != CERTIFICATE_PRODUCER_SIZE_BYTES
                or bound.sha256 != CERTIFICATE_PRODUCER_SHA256
            ):
                raise exact.StrictDataError(
                    "opaque certificate-producer digest/mode/link/size mismatch"
                )
            digest = bound.sha256
            size_bytes = bound.size_bytes
        else:
            raw, fingerprint = exact.read_stable(path, max_bytes=8_000_000)
            metadata = path.stat()
            if (
                fingerprint.mode != expected_mode
                or metadata.st_nlink != 1
                or len(raw) != fingerprint.size_bytes
            ):
                raise exact.StrictDataError(f"C61 source mode/size/link mismatch: {name}")
            digest = fingerprint.sha256
            size_bytes = fingerprint.size_bytes
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": digest,
                "size_bytes": size_bytes,
                "mode_octal": format(expected_mode, "04o"),
            }
        )
    allowlist = [f"code/{name}" for name in sorted(CODE_SOURCE_NAMES)]
    return {
        "schema_id": "hcs-c61-source-contract-v1",
        "entry_count": 13,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": allowlist,
        "entries": entries,
        "mode_policy": "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644",
        "self_reference_policy": (
            "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE"
        ),
    }


def parse_sha_manifest(
    raw: bytes, *, expected_entries: int, label: str
) -> list[tuple[str, str]]:
    try:
        lines = raw.decode("ascii", errors="strict").splitlines(keepends=True)
    except UnicodeDecodeError as exc:
        raise exact.StrictDataError(f"{label} is not ASCII") from exc
    if len(lines) != expected_entries or not raw.endswith(b"\n"):
        raise exact.StrictDataError(f"{label} entry/newline count differs")
    rows: list[tuple[str, str]] = []
    previous = ""
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)\n", line)
        if match is None:
            raise exact.StrictDataError(f"{label} row syntax differs")
        digest, relative = match.group(1), match.group(2)
        if not exact.safe_relative_path(relative) or relative <= previous:
            raise exact.StrictDataError(f"{label} path order/safety differs")
        previous = relative
        rows.append((relative, digest))
    return rows


def git_stdout(
    guard: SnapshotGuard, arguments: Sequence[str], *, label: str
) -> bytes:
    return run_bound_child(
        guard,
        ["/usr/bin/git", *arguments],
        cwd=REPO_ROOT,
        timeout=120,
        label=label,
    ).stdout


def verify_p60_git_objects(guard: SnapshotGuard) -> dict[str, Any]:
    head = git_stdout(guard, ["rev-parse", "HEAD"], label="P60 HEAD rebind")
    parent = git_stdout(
        guard, ["rev-parse", f"{P60_LOCK['commit']}^"], label="P60 parent rebind"
    )
    tree = git_stdout(
        guard,
        ["rev-parse", f"{P60_LOCK['commit']}^{{tree}}"],
        label="P60 tree rebind",
    )
    object_type = git_stdout(
        guard,
        ["cat-file", "-t", P60_LOCK["commit"]],
        label="P60 commit-object type",
    )
    if (
        head != f"{P60_LOCK['commit']}\n".encode("ascii")
        or parent != f"{P60_LOCK['parent']}\n".encode("ascii")
        or tree != f"{P60_LOCK['tree']}\n".encode("ascii")
        or object_type != b"commit\n"
    ):
        raise exact.StrictDataError("released P60 Git identity differs")
    ancestry = run_bound_child(
        guard,
        ["/usr/bin/git", "merge-base", "--is-ancestor", P60_LOCK["commit"], "HEAD"],
        cwd=REPO_ROOT,
        timeout=60,
        label="P60 ancestry",
    )
    if ancestry.stdout:
        raise exact.StrictDataError("P60 ancestry emitted stdout")
    released_batch = git_stdout(
        guard,
        ["show", f"{P60_LOCK['commit']}:henon_dynamics/BATCH_PLAN_C57_C61.md"],
        label="released P60 Batch",
    )
    if (
        exact.sha256_bytes(released_batch) != P60_LOCK["released_batch_sha256"]
        or len(released_batch) != P60_LOCK["released_batch_size_bytes"]
    ):
        raise exact.StrictDataError("released P60 Batch Git blob differs")
    return {
        "ancestor_of_current_HEAD": True,
        "commit": P60_LOCK["commit"],
        "commit_object_type": "commit",
        "parent": P60_LOCK["parent"],
        "released_batch_sha256": P60_LOCK["released_batch_sha256"],
        "released_batch_size_bytes": P60_LOCK["released_batch_size_bytes"],
        "tree": P60_LOCK["tree"],
    }


def verify_c60_full_manifest(guard: SnapshotGuard) -> tuple[dict[str, Any], dict[str, str]]:
    manifest = C60 / "FULL_PROJECT_HASHES.sha256"
    raw, fingerprint = exact.read_stable(manifest, max_bytes=1_000_000)
    metadata = manifest.stat()
    if (
        fingerprint.sha256 != C60_LOCK["full_manifest_sha256"]
        or fingerprint.size_bytes != C60_LOCK["full_manifest_size_bytes"]
        or fingerprint.mode != 0o644
        or metadata.st_nlink != 1
    ):
        raise exact.StrictDataError("released C60 full-manifest seal differs")
    rows = parse_sha_manifest(
        raw,
        expected_entries=C60_LOCK["full_manifest_entries"],
        label="released C60 full manifest",
    )
    declared = {relative: digest for relative, digest in rows}
    total = 0
    inodes: set[tuple[int, int]] = set()
    for relative, digest in rows:
        member = C60 / relative
        bound = seal_file(member)
        inode = (bound.device, bound.inode)
        if (
            bound.sha256 != digest
            or bound.nlink != 1
            or inode in inodes
            or bound.mode not in (0o644, 0o755)
        ):
            raise exact.StrictDataError(f"released C60 manifest member differs: {relative}")
        inodes.add(inode)
        total += bound.size_bytes
    live_files: set[str] = set()
    live_directories: set[str] = set()
    special: list[str] = []
    for child in C60.rglob("*"):
        relative = child.relative_to(C60).as_posix()
        metadata = child.lstat()
        if child.is_symlink() or not (stat.S_ISREG(metadata.st_mode) or stat.S_ISDIR(metadata.st_mode)):
            special.append(relative)
        elif stat.S_ISREG(metadata.st_mode):
            if relative != "FULL_PROJECT_HASHES.sha256":
                live_files.add(relative)
        else:
            live_directories.add(relative)
    allowed_directories: set[str] = set()
    for relative in (*declared, "FULL_PROJECT_HASHES.sha256"):
        for parent in Path(relative).parents:
            if parent.as_posix() != ".":
                allowed_directories.add(parent.as_posix())
    if (
        total != C60_LOCK["full_manifest_total_bytes"]
        or special
        or live_files != set(declared)
        or live_directories != allowed_directories
        or any("__pycache__" in path or path.endswith((".pyc", ".pyo")) for path in live_files)
    ):
        raise exact.StrictDataError("released C60 live full inventory differs")
    prefix = C60.relative_to(REPO_ROOT).as_posix()
    tracked_raw = git_stdout(
        guard,
        ["ls-tree", "-r", "--name-only", P60_LOCK["commit"], "--", prefix],
        label="released C60 immutable Git inventory",
    )
    try:
        tracked = set(tracked_raw.decode("utf-8", errors="strict").splitlines())
    except UnicodeDecodeError as exc:
        raise exact.StrictDataError("released C60 Git inventory is not UTF-8") from exc
    expected_tracked = {f"{prefix}/{relative}" for relative in declared}
    expected_tracked.add(f"{prefix}/FULL_PROJECT_HASHES.sha256")
    if tracked != expected_tracked:
        raise exact.StrictDataError("released C60 immutable Git inventory differs")
    for arguments, label in (
        (["diff", "--quiet", P60_LOCK["commit"], "--", prefix], "C60 live/Git bytes"),
        (["diff", "--cached", "--quiet", P60_LOCK["commit"], "--", prefix], "C60 index/Git bytes"),
    ):
        completed = run_bound_child(
            guard,
            ["/usr/bin/git", *arguments],
            cwd=REPO_ROOT,
            timeout=120,
            label=label,
        )
        if completed.stdout:
            raise exact.StrictDataError(f"{label} emitted stdout")
    return (
        {
            "entry_count": len(rows),
            "immutable_git_object_inventory_exact": True,
            "immutable_git_object_leaf_total_bytes": total,
            "immutable_git_object_leaves_rebound": len(rows),
            "inventory_exact_excluding_self": True,
            "live_tree_equals_immutable_git_tree": True,
            "manifest_path": relative_to_repo(manifest),
            "manifest_sha256": fingerprint.sha256,
            "manifest_size_bytes": fingerprint.size_bytes,
            "verified_leaf_total_bytes": total,
        },
        declared,
    )


def verify_c60_scoped_manifest(full_declared: dict[str, str]) -> dict[str, Any]:
    path = C60 / "results/scoped_hash_manifest.json"
    raw, fingerprint = exact.read_stable(path, max_bytes=1_000_000)
    if (
        fingerprint.sha256 != C60_LOCK["scoped_manifest_sha256"]
        or fingerprint.size_bytes != C60_LOCK["scoped_manifest_size_bytes"]
    ):
        raise exact.StrictDataError("released C60 scoped-manifest seal differs")
    document = canonical_pretty(raw, max_bytes=1_000_000, label="C60 scoped manifest")
    exact.require_exact_keys(
        document,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        "released C60 scoped manifest",
    )
    if (
        document["entry_count"] != C60_LOCK["scoped_manifest_entries"]
        or document["entry_count"] != len(document["entries"])
        or document["manifest_self_included"] is not False
        or document["schema"] != "hcs-c60-scoped-hash-manifest-v1"
        or document["scope"] != "exact_C60_code_and_results_artifacts"
        or document["status"] != "PREFREEZE_CODE_RESULTS_PASS"
    ):
        raise exact.StrictDataError("released C60 scoped-manifest contract differs")
    declared: set[str] = set()
    for row in document["entries"]:
        exact.require_exact_keys(row, {"path", "sha256", "size_bytes"}, "C60 scoped row")
        relative = row["path"]
        bound = seal_file(C60 / relative)
        if (
            not exact.safe_relative_path(relative)
            or relative in declared
            or full_declared.get(relative) != row["sha256"]
            or bound.sha256 != row["sha256"]
            or bound.size_bytes != row["size_bytes"]
            or bound.mode not in (0o644, 0o755)
            or bound.nlink != 1
        ):
            raise exact.StrictDataError(f"released C60 scoped row differs: {relative}")
        declared.add(relative)
    live = {
        child.relative_to(C60).as_posix()
        for root in (C60 / "code", C60 / "results")
        for child in root.rglob("*")
        if child.is_file() and child.name != "scoped_hash_manifest.json"
    }
    if live != declared:
        raise exact.StrictDataError("released C60 code/results inventory differs")
    return {
        "entry_count": len(declared),
        "full_manifest_consistent": True,
        "path": relative_to_repo(path),
        "sha256": fingerprint.sha256,
        "size_bytes": fingerprint.size_bytes,
    }


def validate_c60_certificate_bundle() -> dict[str, Any]:
    results = C60 / "results"
    paths = {
        "certificate": results / "c60_certificate.json",
        "schema": results / "c60_schema.json",
        "check": results / "c60_check_report.json",
    }
    raw = {key: exact.read_stable(path, max_bytes=5_000_000)[0] for key, path in paths.items()}
    seals = {key: seal_file(path, max_bytes=5_000_000) for key, path in paths.items()}
    if (
        (seals["certificate"].sha256, seals["certificate"].size_bytes)
        != (C60_LOCK["certificate_sha256"], C60_LOCK["certificate_size_bytes"])
        or (seals["schema"].sha256, seals["schema"].size_bytes)
        != (C60_LOCK["schema_sha256"], C60_LOCK["schema_size_bytes"])
        or (seals["check"].sha256, seals["check"].size_bytes)
        != (C60_LOCK["check_sha256"], C60_LOCK["check_size_bytes"])
        or any(seal.mode != 0o644 or seal.nlink != 1 for seal in seals.values())
    ):
        raise exact.StrictDataError("released C60 certificate bundle bytes differ")
    certificate = canonical_pretty(raw["certificate"], max_bytes=5_000_000, label="C60 certificate")
    schema = canonical_pretty(raw["schema"], max_bytes=1_000_000, label="C60 schema")
    check = canonical_pretty(raw["check"], max_bytes=2_000_000, label="C60 check report")
    exact.require_exact_keys(
        certificate,
        {"payload", "payload_sha256", "schema", "schema_sha256"},
        "released C60 certificate",
    )
    source_contract_sha = exact.sha256_bytes(
        exact.canonical_leaf_bytes(certificate["payload"]["source_contract"])
    )
    if (
        certificate["payload_sha256"] != C60_LOCK["payload_sha256"]
        or certificate["payload_sha256"]
        != exact.sha256_bytes(exact.canonical_leaf_bytes(certificate["payload"]))
        or certificate["schema_sha256"]
        != exact.sha256_bytes(exact.canonical_leaf_bytes(certificate["schema"]))
        or not exact.deep_exact(certificate["schema"], schema)
        or source_contract_sha != C60_LOCK["source_contract_sha256"]
        or check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        or check.get("promotion_authorized") is not False
        or check.get("release_status") != "NOT_RELEASED"
    ):
        raise exact.StrictDataError("released C60 certificate bundle semantics differ")
    return {
        "independent_check": file_binding(paths["check"], C60_LOCK["check_sha256"]),
        "independent_check_bytes_rebound": seals["check"].size_bytes,
        "path": relative_to_repo(paths["certificate"]),
        "payload_sha256": certificate["payload_sha256"],
        "schema": file_binding(paths["schema"], C60_LOCK["schema_sha256"]),
        "schema_bytes_rebound": seals["schema"].size_bytes,
        "sha256": seals["certificate"].sha256,
        "size_bytes": seals["certificate"].size_bytes,
        "source_contract_sha256": source_contract_sha,
    }


def formal_target_lock(guard: SnapshotGuard) -> dict[str, Any]:
    guard.assert_unchanged("before C61 authority-layer validation")
    try:
        authority = pipeline.require_authority_layers(
            repository=REPO_ROOT,
            project=PROJECT,
        )
    finally:
        guard.assert_unchanged("after C61 authority-layer validation")
    target = authority["installed_c61_target_lock"]
    markdown = {path.name: path for path in PROJECT.glob("*.md")}
    if set(markdown) != FORMAL_MARKDOWN_NAMES:
        raise exact.StrictDataError("C61 exact thirteen-Markdown target inventory differs")
    entries: list[dict[str, Any]] = []
    aggregate_rows: list[bytes] = []
    exact15: list[tuple[str, bytes]] = []
    for name in sorted(markdown):
        raw, fingerprint = exact.read_stable(markdown[name], max_bytes=2_000_000)
        metadata = markdown[name].stat()
        if (
            b"NO_BAD_EULER_OR_ROOT_NUMBER" not in raw
            or fingerprint.mode != 0o644
            or metadata.st_nlink != 1
        ):
            raise exact.StrictDataError(f"C61 formal target seal/firewall differs: {name}")
        entries.append(
            {"path": name, "sha256": fingerprint.sha256, "size_bytes": fingerprint.size_bytes}
        )
        aggregate_rows.append(f"{fingerprint.sha256}  {name}\n".encode("ascii"))
        exact15.append((f"{PROJECT.name}/{name}", raw))
    aggregate = exact.sha256_bytes(b"".join(aggregate_rows))
    route_path = PROJECT / "route_a_evaluation.yaml"
    route_raw, route = exact.read_stable(route_path, max_bytes=1_000_000)
    batch_raw, batch = exact.read_stable(BATCH, max_bytes=1_000_000)
    guard_raw, guard_file = exact.read_stable(GUARD, max_bytes=1_000_000)
    for path in (route_path, BATCH, GUARD):
        metadata = path.stat()
        if stat.S_IMODE(metadata.st_mode) != 0o644 or metadata.st_nlink != 1:
            raise exact.StrictDataError(f"C61 target authority mode/link differs: {path}")
    exact15.extend(
        (
            (BATCH.name, batch_raw),
            (f"{PROJECT.name}/route_a_evaluation.yaml", route_raw),
        )
    )
    exact15.sort(key=lambda item: item[0])
    ledger = b"".join(
        f"{exact.sha256_bytes(raw)}  {relative}\n".encode("ascii")
        for relative, raw in exact15
    )
    line_count = sum(raw.count(b"\n") for _, raw in exact15)
    total_bytes = sum(len(raw) for _, raw in exact15)
    if (
        aggregate != target["formal_root13_aggregate_sha256"]
        or route.sha256 != target["route_sha256"]
        or batch.sha256 != target["batch_sha256"]
        or guard_file.sha256 != target["protected_guard_sha256"]
        or exact.sha256_bytes(ledger) != target["exact15_ledger_sha256"]
        or total_bytes != target["exact15_total_bytes"]
        or line_count != target["exact15_line_count"]
        or len(exact15) != 15
    ):
        raise exact.StrictDataError("C61 formal/Route/Batch/guard exact lock differs")
    route_projection = {
        "candidate_definition": (
            "target-locked conditional theorem: three pairwise nonisomorphic but "
            "rationally linearized/zeta-equivalent finite-etale tensor algebras of "
            "the released W(E6) Gassmann pair, their complete self/mixed double-coset "
            "decompositions, and an exact normalized Fourier descent identifying the "
            "mixed type-3 degree-40 base"
        ),
        "candidate_id": "HCS-C61",
        "code_results_status": "IMPLEMENTATION_PENDING",
        "documentation_status": "TARGET_LOCKED",
        "paper_status": "PAPER_PENDING",
        "project_root": (
            "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent"
        ),
        "promotion_authorized": False,
        "release_status": "NOT_RELEASED",
        "theorem_status": "TARGET_LOCKED",
    }
    required_route_literals = {
        value.encode("utf-8")
        for value in route_projection.values()
        if type(value) is str
    }
    required_route_literals.add(b"NO_BAD_EULER_OR_ROOT_NUMBER")
    if (
        any(literal not in route_raw for literal in required_route_literals)
        or b"NO_BAD_EULER_OR_ROOT_NUMBER" not in batch_raw
        or not guard_raw
    ):
        raise exact.StrictDataError("C61 Route/Batch semantic target lock differs")
    return {
        "batch_target_lock": {
            "path": relative_to_repo(BATCH),
            "sha256": batch.sha256,
            "size_bytes": batch.size_bytes,
        },
        "formal_target_lock": {
            "aggregate_definition": (
                "SHA256_OF_LEXICOGRAPHIC_BASENAME_ORDERED_SHA256SUM_LINES_FOR_13_MARKDOWN_ROOTS"
            ),
            "entries": entries,
            "entry_count": 13,
            "exact_formal_inventory": True,
            "markdown_aggregate_sha256": aggregate,
            "route_path": relative_to_repo(route_path),
            "route_semantic_projection": route_projection,
            "route_sha256": route.sha256,
            "route_size_bytes": route.size_bytes,
            "status": "TARGET_LOCK_INPUT_REBOUND",
            "target_lock_input_entry_count": 15,
            "target_lock_input_ledger_sha256": exact.sha256_bytes(ledger),
            "target_lock_input_line_count": line_count,
            "target_lock_input_total_bytes": total_bytes,
        },
        "protected_guard": {
            "path": relative_to_repo(GUARD),
            "sha256": guard_file.sha256,
            "size_bytes": guard_file.size_bytes,
        },
    }


def released_c60_component_bindings() -> tuple[dict[str, Any], dict[str, Any]]:
    group_path = C60 / "results/c60_group_evidence.json"
    resolver_path = C60 / "results/c60_resolvent_evidence.json"
    group_raw, group_fp = exact.read_stable(group_path, max_bytes=2_000_000)
    resolver_raw, resolver_fp = exact.read_stable(resolver_path, max_bytes=2_000_000)
    if (
        (group_fp.sha256, group_fp.size_bytes)
        != (C60_LOCK["group_sha256"], C60_LOCK["group_size_bytes"])
        or (resolver_fp.sha256, resolver_fp.size_bytes)
        != (C60_LOCK["resolvent_sha256"], C60_LOCK["resolvent_size_bytes"])
    ):
        raise exact.StrictDataError("released C60 component evidence tuple differs")
    group = compact_document(group_raw, max_bytes=2_000_000, label="C60 group evidence")
    resolver = compact_document(
        resolver_raw, max_bytes=2_000_000, label="C60 resolver evidence"
    )
    arrays_sha = exact.sha256_bytes(
        exact.canonical_leaf_bytes(group["frozen_permutation_arrays"]["arrays"])
    )
    l_sha = resolver["payload"]["carriers"]["L"]["carrier_sha256"]
    if (
        group.get("status") != "PASS"
        or resolver["payload_sha256"]
        != exact.sha256_bytes(exact.canonical_json_bytes(resolver["payload"]))
        or arrays_sha != C60_LOCK["frozen_arrays_sha256"]
        or l_sha != C60_LOCK["l_carrier_sha256"]
    ):
        raise exact.StrictDataError("released C60 component semantic bindings differ")
    return (
        {
            "bytes_rebound": group_fp.size_bytes,
            "frozen_arrays_sha256": arrays_sha,
            "path": relative_to_repo(group_path),
            "sha256": group_fp.sha256,
            "size_bytes": group_fp.size_bytes,
        },
        {
            "L_carrier_sha256": l_sha,
            "bytes_rebound": resolver_fp.size_bytes,
            "path": relative_to_repo(resolver_path),
            "sha256": resolver_fp.sha256,
            "size_bytes": resolver_fp.size_bytes,
        },
    )


def rebuild_g0(guard: SnapshotGuard) -> dict[str, Any]:
    p60 = verify_p60_git_objects(guard)
    full, full_declared = verify_c60_full_manifest(guard)
    scoped = verify_c60_scoped_manifest(full_declared)
    certificate = validate_c60_certificate_bundle()
    group_binding, resolver_binding = released_c60_component_bindings()
    live_route = C60 / "route_a_evaluation.yaml"
    live_raw, live_fp = exact.read_stable(live_route, max_bytes=1_000_000)
    candidates = [
        C60 / relative
        for relative in full_declared
        if relative.startswith("evaluations/route_a/HCS-C60/")
        and relative.endswith(".yaml")
    ]
    if len(candidates) != 1:
        raise exact.StrictDataError("released C60 exact archive Route inventory differs")
    archive_route = candidates[0]
    archive_raw, archive_fp = exact.read_stable(archive_route, max_bytes=1_000_000)
    if (
        live_raw != archive_raw
        or live_fp.sha256 != C60_LOCK["route_sha256"]
        or archive_fp.sha256 != C60_LOCK["archive_route_sha256"]
        or live_fp.size_bytes != C60_LOCK["route_size_bytes"]
        or archive_fp.size_bytes != C60_LOCK["route_size_bytes"]
    ):
        raise exact.StrictDataError("released C60 live/archive Route identity differs")
    formal = formal_target_lock(guard)
    return {
        "all_released_full_inventories_rebound": True,
        **formal,
        "fixed_predecessor_paths_only": True,
        "released_P60_C60": {
            "c60_archive_route": {
                "path": relative_to_repo(archive_route),
                "sha256": archive_fp.sha256,
                "size_bytes": archive_fp.size_bytes,
            },
            "c60_certificate_bundle": certificate,
            "c60_full_manifest": full,
            "c60_group_evidence": group_binding,
            "c60_live_archive_route_identical": True,
            "c60_live_route": {
                "path": relative_to_repo(live_route),
                "sha256": live_fp.sha256,
                "size_bytes": live_fp.size_bytes,
            },
            "c60_resolvent_evidence": resolver_binding,
            "c60_scoped_manifest": scoped,
            "p60_git_objects": p60,
            "status": "RELEASED_P60_C60_REBOUND",
        },
        "schema_id": "hcs-c61-released-authority-rebind-v1",
        "target_object_and_conventions": {
            "ambient_group": "W(E6)",
            "ambient_group_order": 51_840,
            "candidate_id": "HCS-C61",
            "composition": "left_after_right",
            "exact_arithmetic_only": True,
            "finite_etale_objects_not_single_fields": True,
            "ordered_tensor_algebras": [
                "Fplus_tensor_Fplus",
                "Fplus_tensor_Fminus",
                "Fminus_tensor_Fminus",
            ],
            "permutation_arrays": "one_based",
            "polynomial_action": "p(X_i)=X_p(i)",
            "project_basename": PROJECT.name,
            "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "sparse_monomial_labels": "zero_based",
            "split_prime": 692_717,
            "subgroup_orders_Hplus_Hminus": [162, 162],
            "tensor_algebra_dimension_each": 102_400,
            "tensor_cosets": "right_cosets_with_left_subgroup_action",
        },
    }


_EXPECTED_DIGEST_CACHE: dict[int, tuple[Any, str]] = {}


def expected_semantic_digest(value: Any) -> str:
    """Memoize only a strongly held in-process object identity."""

    identity = id(value)
    cached = _EXPECTED_DIGEST_CACHE.get(identity)
    if cached is not None and cached[0] is value:
        return cached[1]
    digest = exact.sha256_bytes(exact.canonical_leaf_bytes(value))
    _EXPECTED_DIGEST_CACHE[identity] = (value, digest)
    return digest


def core_verify(
    certificate: Any,
    sidecar_schema: Any,
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> None:
    exact.require_exact_keys(
        certificate,
        {"schema", "schema_sha256", "payload", "payload_sha256"},
        "C61 certificate root",
    )
    if type(sidecar_schema) is not dict:
        raise exact.StrictDataError("C61 schema sidecar must be an object")
    exact.require_exact_keys(sidecar_schema, set(expected_schema), "C61 schema sidecar")
    exact.require_sha256(certificate["schema_sha256"], "C61 schema digest")
    exact.require_sha256(certificate["payload_sha256"], "C61 payload digest")
    if not exact.deep_exact(certificate["schema"], sidecar_schema):
        raise exact.StrictDataError("embedded C61 schema differs from sidecar")
    if certificate["schema_sha256"] != expected_semantic_digest(expected_schema):
        raise exact.StrictDataError("C61 schema digest differs from independent rebuild")
    if certificate["payload_sha256"] != expected_semantic_digest(expected):
        raise exact.StrictDataError("C61 payload digest differs from independent rebuild")
    if not exact.deep_exact(certificate["payload"], expected):
        raise exact.StrictDataError("full C61 semantic payload rebuild mismatch")
    if not exact.deep_exact(sidecar_schema, expected_schema):
        raise exact.StrictDataError("full C61 schema descriptor rebuild mismatch")
    if certificate["schema_sha256"] != exact.sha256_bytes(
        exact.canonical_leaf_bytes(certificate["schema"])
    ):
        raise exact.StrictDataError("C61 compact embedded-schema digest mismatch")
    if certificate["payload_sha256"] != exact.sha256_bytes(
        exact.canonical_leaf_bytes(certificate["payload"])
    ):
        raise exact.StrictDataError("C61 compact payload digest mismatch")


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
        raise exact.StrictDataError("unsupported mutation leaf type")


def get_path(value: Any, path: tuple[Any, ...]) -> Any:
    current = value
    for component in path:
        current = current[component]
    return current


def set_path(value: Any, path: tuple[Any, ...], replacement: Any) -> None:
    if not path:
        raise exact.StrictDataError("cannot replace an empty mutation path")
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
    raise exact.StrictDataError("unsupported value-mutation leaf")


def type_mutation(value: Any) -> Any:
    if type(value) is bool:
        return 0
    if type(value) is int:
        return False
    if type(value) is str:
        return 0
    if value is None:
        return False
    raise exact.StrictDataError("unsupported type-mutation leaf")


def canonical_bytes_and_leaf_spans(
    value: Any,
) -> tuple[bytes, dict[tuple[Any, ...], tuple[int, int]]]:
    output = bytearray()
    spans: dict[tuple[Any, ...], tuple[int, int]] = {}

    def emit(child: Any, path: tuple[Any, ...]) -> None:
        if type(child) is dict:
            output.extend(b"{")
            for index, key in enumerate(sorted(child)):
                if index:
                    output.extend(b",")
                output.extend(exact.canonical_leaf_bytes(key))
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
            output.extend(exact.canonical_leaf_bytes(child))
            spans[path] = (start, len(output))
        else:
            raise exact.StrictDataError("unsupported canonical-span value")

    emit(value, ())
    raw = bytes(output)
    if raw != exact.canonical_leaf_bytes(value) or len(spans) != scalar_leaf_count(value):
        raise exact.StrictDataError("canonical scalar-span serialization differs")
    return raw, spans


def rebound_digest(original_raw: bytes, span: tuple[int, int], replacement: Any) -> str:
    start, end = span
    digest = hashlib.sha256()
    digest.update(original_raw[:start])
    digest.update(exact.canonical_leaf_bytes(replacement))
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
    except exact.StrictDataError:
        return
    raise exact.StrictDataError(f"C61 checker accepted hostile mutation: {label}")


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
                payload_mutant,
                schema,
                expected,
                expected_schema,
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
            schema_certificate["schema_sha256"] = exact.sha256_bytes(
                exact.canonical_leaf_bytes(schema_mutant)
            )
            expect_core_rejection(
                schema_certificate,
                schema_mutant,
                expected,
                expected_schema,
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
    mutant = deepcopy(certificate)
    mutant["unknown"] = False
    structural.append(("root-extra", mutant, schema))
    mutant = deepcopy(certificate)
    del mutant["schema_sha256"]
    structural.append(("root-missing", mutant, schema))
    mutant = deepcopy(certificate)
    mutant["schema"] = []
    structural.append(("root-schema-container", mutant, schema))
    mutant = deepcopy(certificate)
    mutant["payload"] = []
    structural.append(("root-payload-container", mutant, schema))
    mutant = deepcopy(certificate)
    mutant["payload"]["unknown"] = False
    mutant["payload_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-extra", mutant, schema))
    mutant = deepcopy(certificate)
    del mutant["payload"]["status"]
    mutant["payload_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-missing", mutant, schema))
    mutant = deepcopy(certificate)
    mutant["payload"]["G3_product_form_resolvents_primitivity"] = []
    mutant["payload_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-gate-container", mutant, schema))
    mutant = deepcopy(certificate)
    mutant["payload"]["G4_fourier_kummer_type3_diamond"]["mixed_type3_exact_bridge"][
        "mixed_rows"
    ].pop()
    mutant["payload_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant["payload"]))
    structural.append(("payload-list-length", mutant, schema))
    mutant_schema = deepcopy(schema)
    mutant_schema["unknown"] = False
    mutant = deepcopy(certificate)
    mutant["schema"] = deepcopy(mutant_schema)
    mutant["schema_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant_schema))
    structural.append(("schema-extra", mutant, mutant_schema))
    mutant_schema = deepcopy(schema)
    del mutant_schema["schema_id"]
    mutant = deepcopy(certificate)
    mutant["schema"] = deepcopy(mutant_schema)
    mutant["schema_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant_schema))
    structural.append(("schema-missing", mutant, mutant_schema))
    mutant_schema = deepcopy(schema)
    mutant_schema["payload_top_level_keys"].append("unknown")
    mutant = deepcopy(certificate)
    mutant["schema"] = deepcopy(mutant_schema)
    mutant["schema_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant_schema))
    structural.append(("schema-list-length", mutant, mutant_schema))
    structural.append(("schema-sidecar-container", deepcopy(certificate), []))
    mutant = deepcopy(certificate)
    mutant["payload"]["artifact_contract"]["artifacts"].pop()
    mutant["payload_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant["payload"]))
    structural.append(("artifact-list-length", mutant, schema))
    mutant = deepcopy(certificate)
    del mutant["payload"]["scope_nonclaims"]["release_claimed"]
    mutant["payload_sha256"] = exact.sha256_bytes(exact.canonical_leaf_bytes(mutant["payload"]))
    structural.append(("scope-key-missing", mutant, schema))
    if len(structural) != 14:
        raise RuntimeError("C61 structural mutation inventory changed")
    for label, mutant, mutant_schema in structural:
        expect_core_rejection(mutant, mutant_schema, expected, expected_schema, label)

    value_total = payload_value + schema_value + root_value
    type_total = payload_type + schema_type + root_type
    g7 = expected["G7_independence_sources_scope_release"]
    if (
        value_total != g7["value_mutation_count_expected"]
        or type_total != g7["type_mutation_count_expected"]
        or len(structural) != g7["structural_mutation_count_expected"]
    ):
        raise exact.StrictDataError("C61 mutation sweep count differs from G7 contract")
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


def expect_group_evidence_rejection(mutant: dict[str, Any], label: str) -> None:
    try:
        validate_group_document(mutant)
        # Exercise every consumer-facing projection that is not already forced
        # by the two canonical projection hashes.
        derive_g1(mutant)
    except exact.StrictDataError:
        return
    raise exact.StrictDataError(f"C61 group verifier accepted evidence mutation: {label}")


def resolver_candidate(document: dict[str, Any]) -> dict[str, Any]:
    candidate = deepcopy(document)
    candidate["independence_contract"]["checker_attestation"] = None
    candidate["independence_contract"]["checker_attestation_two_run_equal"] = False
    candidate["status"]["resolver_component_status"] = "PRODUCER_PASS_CHECKER_PENDING"
    candidate["payload_sha256"] = exact.sha256_bytes(
        exact.canonical_leaf_bytes(
            {key: value for key, value in candidate.items() if key != "payload_sha256"}
        )
    )
    return candidate


def expect_resolver_evidence_rejection(
    mutant: dict[str, Any], evidence_path: Path, guard: SnapshotGuard, label: str
) -> None:
    mutant["payload_sha256"] = exact.sha256_bytes(
        exact.canonical_leaf_bytes(
            {key: value for key, value in mutant.items() if key != "payload_sha256"}
        )
    )
    raw = exact.canonical_json_bytes(mutant)
    guard.assert_unchanged(f"before hostile resolver evidence {label}")
    try:
        checker_resolvent.attest_candidate_document(raw, evidence_path)
    except checker_resolvent.Reject:
        guard.assert_unchanged(f"after hostile resolver evidence {label}")
        return
    guard.assert_unchanged(f"after hostile resolver evidence {label}")
    raise exact.StrictDataError(f"C61 resolver verifier accepted evidence mutation: {label}")


def evidence_rebound_suite(
    certificate: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
    group_document: dict[str, Any],
    resolver_document: dict[str, Any],
    resolver_path: Path,
    guard: SnapshotGuard,
) -> dict[str, Any]:
    group_mutations: list[tuple[str, dict[str, Any]]] = []

    mutant = deepcopy(group_document)
    mutant["semantic_firewall"] = "BAD_EULER_ALLOWED"
    group_mutations.append(("group_schema_status_firewall", mutant))

    mutant = deepcopy(group_document)
    mutant["source_contract"]["c60_payload_sha256"] = "0" * 64
    group_mutations.append(("group_source_authority_rebind", mutant))

    mutant = deepcopy(group_document)
    mutant["python_projection"]["tensor_atlas"]["rows"]["Tpp"][0][
        "simple_factor_degree"
    ] += 1
    mutant["component_hashes"]["python_projection_sha256"] = exact.sha256_bytes(
        exact.canonical_leaf_bytes(mutant["python_projection"])
    )
    group_mutations.append(("group_tensor_row_semantics", mutant))

    mutant = deepcopy(group_document)
    mutant["python_projection"]["mixed_160_12_8"]["relative_position_types"][0][
        "raw_count"
    ] += 1
    mutant["component_hashes"]["python_projection_sha256"] = exact.sha256_bytes(
        exact.canonical_leaf_bytes(mutant["python_projection"])
    )
    group_mutations.append(("group_mixed_160_12_8_atlas", mutant))

    mutant = deepcopy(group_document)
    mutant["python_projection"]["raw_global_local_inputs"]["field_type_rows"][0][
        "conductor_exponents"
    ][0] += 1
    mutant["component_hashes"]["python_projection_sha256"] = exact.sha256_bytes(
        exact.canonical_leaf_bytes(mutant["python_projection"])
    )
    group_mutations.append(("group_raw_global_local_inputs", mutant))

    mutant = deepcopy(group_document)
    mutant["scope_nonclaims"]["bad_artin_euler_claimed"] = True
    group_mutations.append(("group_scope_false_leaf", mutant))

    resolver_base = resolver_candidate(resolver_document)
    resolver_mutations: list[tuple[str, dict[str, Any]]] = []

    mutant = deepcopy(resolver_base)
    mutant["schema_sha256"] = "0" * 64
    resolver_mutations.append(("resolver_schema_payload", mutant))

    mutant = deepcopy(resolver_base)
    mutant["GAF3_stabilizers_and_noncollision"][
        "product_form_mixed_base_A_B_resolvents"
    ]["carriers"]["C1"]["exact_monomial_content"] = 2
    resolver_mutations.append(("resolver_marker_fourier_carrier", mutant))

    mutant = deepcopy(resolver_base)
    mutant["GAF4_mixed_type3_exact_bridge"]["Tplus_sha256"] = "0" * 64
    resolver_mutations.append(("resolver_type3_Tplus_diamond", mutant))

    mutant = deepcopy(resolver_base)
    mutant["GAF7_both_local_branches_and_ideal_laws"]["ideal_equalities"][0] += "#"
    resolver_mutations.append(("resolver_global_local_ideal_law", mutant))

    evidence_rejected = 0
    for label, mutant in group_mutations:
        expect_group_evidence_rejection(mutant, label)
        mutant_raw = exact.canonical_json_bytes(mutant)
        rebound = deepcopy(certificate)
        artifact = rebound["payload"]["artifact_contract"]["artifacts"][0]
        artifact["sha256"] = exact.sha256_bytes(mutant_raw)
        artifact["size_bytes"] = len(mutant_raw)
        rebound["payload_sha256"] = exact.sha256_bytes(
            exact.canonical_leaf_bytes(rebound["payload"])
        )
        expect_core_rejection(
            rebound,
            schema,
            expected,
            expected_schema,
            f"group-evidence-rebound:{label}",
        )
        evidence_rejected += 1

    for label, mutant in resolver_mutations:
        expect_resolver_evidence_rejection(mutant, resolver_path, guard, label)
        mutant_raw = exact.canonical_json_bytes(mutant)
        rebound = deepcopy(certificate)
        artifact = rebound["payload"]["artifact_contract"]["artifacts"][1]
        artifact["sha256"] = exact.sha256_bytes(mutant_raw)
        artifact["size_bytes"] = len(mutant_raw)
        artifact["internal_report_sha256"] = mutant["payload_sha256"]
        rebound["payload_sha256"] = exact.sha256_bytes(
            exact.canonical_leaf_bytes(rebound["payload"])
        )
        expect_core_rejection(
            rebound,
            schema,
            expected,
            expected_schema,
            f"resolver-evidence-rebound:{label}",
        )
        evidence_rejected += 1

    artifact_rejected = 0
    artifact_families = ["group_artifact_contract", "resolver_artifact_contract"]
    for index, label in enumerate(artifact_families):
        rebound = deepcopy(certificate)
        rebound["payload"]["artifact_contract"]["artifacts"][index]["sha256"] = "0" * 64
        rebound["payload_sha256"] = exact.sha256_bytes(
            exact.canonical_leaf_bytes(rebound["payload"])
        )
        expect_core_rejection(
            rebound, schema, expected, expected_schema, f"artifact-rebound:{label}"
        )
        artifact_rejected += 1

    group_families = [label for label, _ in group_mutations]
    resolver_families = [label for label, _ in resolver_mutations]
    if (
        len(group_families) != 6
        or len(resolver_families) != 4
        or evidence_rejected
        != expected["G7_independence_sources_scope_release"][
            "evidence_rebound_mutation_count_expected"
        ]
        or artifact_rejected != 2
    ):
        raise exact.StrictDataError("C61 evidence/artifact mutation counts differ")
    return {
        "actual_group_verifier_mutation_families": group_families,
        "actual_group_verifier_mutations_rejected": len(group_families),
        "actual_resolver_verifier_mutation_families": resolver_families,
        "actual_resolver_verifier_mutations_rejected": len(resolver_families),
        "additional_artifact_hostile_families": artifact_families,
        "additional_artifact_hostile_rebounds_rejected": artifact_rejected,
        "self_consistent_evidence_rebound_mutations_rejected": evidence_rejected,
        "total_evidence_and_artifact_rebounds_rejected": (
            evidence_rejected + artifact_rejected
        ),
    }


def checker_source_architecture_audit() -> dict[str, int | bool]:
    raw, _ = exact.read_stable(CODE_DIR / "c61_checker.py", max_bytes=8_000_000)
    forbidden_tmp_prefix = bytes((47, 116, 109, 112))
    try:
        tree = ast.parse(raw.decode("utf-8", errors="strict"), filename="c61_checker.py")
    except (SyntaxError, UnicodeDecodeError) as exc:
        raise exact.StrictDataError("C61 checker source parse failed") from exc
    dictionary_nodes = 0
    local_imports: set[str] = set()
    dynamic_execution_calls = 0
    ast_parse_calls = 0
    for node in ast.walk(tree):
        if type(node) is ast.Dict:
            keys = [
                key.value
                for key in node.keys
                if type(key) is ast.Constant and type(key.value) is str
            ]
            if len(keys) != len(set(keys)):
                raise exact.StrictDataError("duplicate literal dictionary key in C61 checker")
            dictionary_nodes += 1
        elif type(node) is ast.Import:
            local_imports.update(
                alias.name.split(".")[0]
                for alias in node.names
                if alias.name.startswith("c61_")
            )
        elif type(node) is ast.ImportFrom and node.module and node.module.startswith("c61_"):
            local_imports.add(node.module.split(".")[0])
        elif type(node) is ast.Call:
            if type(node.func) is ast.Name and node.func.id in {
                "compile",
                "eval",
                "exec",
                "__import__",
            }:
                dynamic_execution_calls += 1
            if (
                type(node.func) is ast.Attribute
                and type(node.func.value) is ast.Name
                and node.func.value.id == "ast"
                and node.func.attr == "parse"
            ):
                ast_parse_calls += 1
    expected = {"c61_exact", "c61_pipeline", "c61_checker_resolvent"}
    if (
        local_imports != expected
        or dynamic_execution_calls
        or ast_parse_calls != 1
        or forbidden_tmp_prefix in raw
    ):
        raise exact.StrictDataError(f"C61 checker local import boundary mismatch: {sorted(local_imports)}")
    return {
        "checker_literal_dictionary_nodes_checked": dictionary_nodes,
        "checker_exact_local_import_set": True,
        "checker_forbidden_component_or_certificate_producer_imports_absent": True,
        "certificate_producer_opaque_stable_cryptographic_read_only": True,
        "certificate_producer_source_not_decoded_or_parsed": True,
        "dynamic_execution_absent": True,
        "promotable_source_tmp_literals_absent": True,
    }


def strict_parser_cases() -> dict[str, int]:
    rejected = 0
    invalid = (
        b'{"a":1,"a":2}',
        b'{"a":-0}',
        b'{"a":01}',
        b'{"a":1.0}',
        b'{"a":1e2}',
        b'{"a":NaN}',
        b'{"a":Infinity}',
        b"\xef\xbb\xbf{}",
        b'{"a":"\xff"}',
        b'{} trailing',
    )
    for raw in invalid:
        try:
            exact.strict_json_loads(raw, max_bytes=100)
        except exact.StrictDataError:
            rejected += 1
        else:
            raise exact.StrictDataError(f"strict parser accepted invalid bytes: {raw!r}")
    try:
        exact.strict_json_loads(b'{"a":1}', max_bytes=3)
    except exact.StrictDataError:
        rejected += 1
    else:
        raise exact.StrictDataError("strict parser accepted oversized input")
    for raw in (b'{ "a":1}\n', b'{"a" :1}\n', b'{"a": 1}\n', b'{"a":"\\u0061"}\n'):
        try:
            exact.require_canonical_compact_json(raw)
        except exact.StrictDataError:
            rejected += 1
        else:
            raise exact.StrictDataError("compact parser accepted noncanonical bytes")
    huge = b'{"a":' + b"9" * 100_000 + b"}"
    value = exact.strict_json_loads(huge, max_bytes=len(huge))
    if type(value["a"]) is not int:
        raise exact.StrictDataError("canonical 100k-digit integer was not accepted")
    return {
        "canonical_100k_digit_integer_accepted": 1,
        "invalid_or_noncanonical_cases_rejected": rejected,
    }


def c60_manifest_member_paths() -> list[Path]:
    manifest = C60 / "FULL_PROJECT_HASHES.sha256"
    raw, fingerprint = exact.read_stable(manifest, max_bytes=1_000_000)
    if fingerprint.sha256 != C60_LOCK["full_manifest_sha256"]:
        raise exact.StrictDataError("released C60 manifest changed while building snapshot")
    rows = parse_sha_manifest(
        raw,
        expected_entries=C60_LOCK["full_manifest_entries"],
        label="released C60 full manifest",
    )
    return [manifest, *(C60 / relative for relative, _ in rows)]


def protected_paths(
    certificate: Path,
    schema: Path,
    group_evidence: Path,
    resolver_evidence: Path,
    math_python: Path,
    gap_path: Path,
) -> list[Path]:
    paths = [CODE_DIR / name for name in sorted(CODE_SOURCE_NAMES)]
    paths.extend(c60_manifest_member_paths())
    paths.extend((certificate, schema, group_evidence, resolver_evidence))
    paths.extend(PROJECT / name for name in sorted(FORMAL_MARKDOWN_NAMES))
    paths.extend((PROJECT / "route_a_evaluation.yaml", BATCH, GUARD))
    paths.extend(
        (
            math_python.resolve(strict=True),
            gap_path.resolve(strict=True),
            Path("/usr/bin/git").resolve(strict=True),
        )
    )
    git_dir = REPO_ROOT / ".git"
    for relative in ("HEAD", "index", "packed-refs", "refs/heads/main"):
        candidate = git_dir / relative
        if candidate.is_file() and not candidate.is_symlink():
            paths.append(candidate)
    return paths


def rebind_raw_inputs(
    paths: tuple[Path, Path, Path, Path],
    originals: tuple[tuple[bytes, FileSeal], ...],
) -> None:
    limits = (
        MAX_CERTIFICATE_BYTES,
        MAX_SCHEMA_BYTES,
        MAX_GROUP_EVIDENCE_BYTES,
        MAX_RESOLVER_EVIDENCE_BYTES,
    )
    for path, (expected_raw, expected_seal), limit in zip(paths, originals, limits):
        raw, _ = exact.read_stable(path, max_bytes=limit)
        if raw != expected_raw or seal_file(path, max_bytes=limit) != expected_seal:
            raise exact.StrictDataError(f"C61 input changed during replay: {path.name}")


def assert_cache_free() -> None:
    forbidden = sorted(
        child.relative_to(PROJECT).as_posix()
        for child in PROJECT.rglob("*")
        if child.name == "__pycache__" or child.suffix in {".pyc", ".pyo"}
    )
    if forbidden:
        raise exact.StrictDataError(f"C61 authority tree contains Python cache: {forbidden}")


def stage_snapshot(parent: Path, expected_names: set[str]) -> dict[str, FileSeal]:
    if {child.name for child in parent.iterdir()} != expected_names:
        raise exact.StrictDataError("C61 stage inventory changed")
    return {name: seal_file(parent / name, max_bytes=MAX_CERTIFICATE_BYTES) for name in sorted(expected_names)}


def validate_fixed_paths(arguments: argparse.Namespace) -> tuple[Path, Path, Path, Path, Path, Path]:
    requested = (
        (arguments.certificate, "c61_certificate.json"),
        (arguments.schema, "c61_schema.json"),
        (arguments.group_evidence, "c61_group_evidence.json"),
        (arguments.resolvent_evidence, "c61_resolvent_evidence.json"),
        (arguments.output, "c61_check_report.json"),
    )
    if any(path.name != basename for path, basename in requested):
        raise exact.StrictDataError("C61 certificate/schema/evidence/output basenames are fixed")
    absolute = tuple(path.absolute() for path, _ in requested)
    if len(set(absolute)) != 5:
        raise exact.StrictDataError("C61 certificate/schema/evidence/output paths alias")
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
        or re.fullmatch(r"\.c61-stage-[A-Za-z0-9]{8}", parent.name) is None
    ):
        raise exact.StrictDataError(
            "C61 inputs/output must share one canonical real .c61-stage-* direct child of PROJECT/results"
        )
    parent_seal = seal_directory(parent)
    if os.path.lexists(absolute[4]):
        raise exact.StrictDataError("C61 check-report output must be absent")
    stage_names = {child.name for child in parent.iterdir()}
    if stage_names != {basename for _, basename in requested[:4]}:
        raise exact.StrictDataError("C61 stage must contain exactly the four immutable inputs")
    inodes: set[tuple[int, int]] = set()
    limits = (
        MAX_CERTIFICATE_BYTES,
        MAX_SCHEMA_BYTES,
        MAX_GROUP_EVIDENCE_BYTES,
        MAX_RESOLVER_EVIDENCE_BYTES,
    )
    for path, limit in zip(absolute[:4], limits):
        raw, _ = exact.read_stable(path, max_bytes=limit)
        if path.resolve(strict=True) != path:
            raise exact.StrictDataError("C61 input path is not canonical")
        metadata = path.stat()
        inode = (metadata.st_dev, metadata.st_ino)
        if (
            inode in inodes
            or metadata.st_nlink != 1
            or stat.S_IMODE(metadata.st_mode) != 0o644
            or not raw
        ):
            raise exact.StrictDataError("C61 input mode/hardlink/link-count/empty-file firewall failed")
        inodes.add(inode)
    if seal_directory(parent) != parent_seal:
        raise exact.StrictDataError("C61 stage parent changed during path validation")
    return (*absolute, parent)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--group-evidence", type=Path, required=True)
    parser.add_argument("--resolvent-evidence", type=Path, required=True)
    parser.add_argument("--math-python", type=Path, required=True)
    parser.add_argument("--gap", type=Path, required=True)
    arguments = parser.parse_args()
    exact.reject_optimized_python()

    source_before = exact_source_contract()
    (
        certificate_path,
        schema_path,
        group_path,
        resolver_path,
        output_path,
        stage_parent,
    ) = validate_fixed_paths(arguments)
    assert_cache_free()

    certificate_raw, certificate_fp = exact.read_stable(
        certificate_path, max_bytes=MAX_CERTIFICATE_BYTES
    )
    schema_raw, schema_fp = exact.read_stable(schema_path, max_bytes=MAX_SCHEMA_BYTES)
    group_raw, group_fp = exact.read_stable(
        group_path, max_bytes=MAX_GROUP_EVIDENCE_BYTES
    )
    resolver_raw, resolver_fp = exact.read_stable(
        resolver_path, max_bytes=MAX_RESOLVER_EVIDENCE_BYTES
    )
    certificate = canonical_pretty(
        certificate_raw, max_bytes=MAX_CERTIFICATE_BYTES, label="C61 certificate"
    )
    schema = canonical_pretty(schema_raw, max_bytes=MAX_SCHEMA_BYTES, label="C61 schema")
    group_document = compact_document(
        group_raw, max_bytes=MAX_GROUP_EVIDENCE_BYTES, label="C61 group evidence"
    )
    resolver_document = compact_document(
        resolver_raw,
        max_bytes=MAX_RESOLVER_EVIDENCE_BYTES,
        label="C61 resolver evidence",
    )
    originals = tuple(
        (raw, seal_file(path, max_bytes=limit))
        for path, raw, limit in (
            (certificate_path, certificate_raw, MAX_CERTIFICATE_BYTES),
            (schema_path, schema_raw, MAX_SCHEMA_BYTES),
            (group_path, group_raw, MAX_GROUP_EVIDENCE_BYTES),
            (resolver_path, resolver_raw, MAX_RESOLVER_EVIDENCE_BYTES),
        )
    )
    input_names = {
        "c61_certificate.json",
        "c61_schema.json",
        "c61_group_evidence.json",
        "c61_resolvent_evidence.json",
    }
    stage_before = stage_snapshot(stage_parent, input_names)

    protected = protected_paths(
        certificate_path,
        schema_path,
        group_path,
        resolver_path,
        arguments.math_python,
        arguments.gap,
    )
    guard = SnapshotGuard(protected, directories=(CODE_DIR, stage_parent))
    wrote_output = False
    try:
        backends = backend_contract(arguments.math_python, arguments.gap, guard)
        g0 = rebuild_g0(guard)
        group_validation = validate_group_component(
            group_document,
            group_path,
            arguments.math_python,
            arguments.gap,
            guard,
        )
        resolver_validation = validate_resolver_component(
            resolver_document, resolver_path, guard
        )
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
        )
        expected_schema = schema_descriptor(expected)
        core_verify(certificate, schema, expected, expected_schema)
        source_audit = checker_source_architecture_audit()
        parser_report = strict_parser_cases()
        rebound = verifier_rebound_sweep(
            certificate, schema, expected, expected_schema
        )
        evidence_rebound = evidence_rebound_suite(
            certificate,
            schema,
            expected,
            expected_schema,
            group_document,
            resolver_document,
            resolver_path,
            guard,
        )

        if not exact.deep_exact(source_before, exact_source_contract()):
            raise exact.StrictDataError("C61 source contract changed during checker replay")
        rebind_raw_inputs(
            (certificate_path, schema_path, group_path, resolver_path), originals
        )
        guard.assert_unchanged("after semantic and mutation replay")
        final_g0 = rebuild_g0(guard)
        if not exact.deep_exact(g0, final_g0):
            raise exact.StrictDataError("P60/C60/C61 authority changed during checker replay")
        if stage_snapshot(stage_parent, input_names) != stage_before:
            raise exact.StrictDataError("C61 stage inputs changed before report write")
        assert_cache_free()

        gate_keys = (
            "G0_released_authority_conventions_object",
            "G1_three_tensor_products_burnside",
            "G2_mixed_160_12_8_field_dictionary",
            "G3_product_form_resolvents_primitivity",
            "G4_fourier_kummer_type3_diamond",
            "G5_complete_global_arithmetic",
            "G6_both_local_branches_ideal_laws",
            "G7_independence_sources_scope_release",
        )
        report = {
            "schema_id": CHECK_REPORT_SCHEMA_ID,
            "status": "PREFREEZE_CODE_RESULTS_PASS",
            "result": "PASS_PREFREEZE_CODE_RESULTS",
            "certificate": {
                "path": "results/c61_certificate.json",
                "sha256": certificate_fp.sha256,
                "size_bytes": certificate_fp.size_bytes,
                "payload_sha256": certificate["payload_sha256"],
            },
            "schema_file": {
                "path": "results/c61_schema.json",
                "sha256": schema_fp.sha256,
                "size_bytes": schema_fp.size_bytes,
                "compact_embedded_schema_sha256": certificate["schema_sha256"],
                "parsed_deep_equal_embedded_schema": True,
                "descriptor_sha256": expected_semantic_digest(expected_schema),
            },
            "evidence": {
                "group_sha256": group_fp.sha256,
                "group_size_bytes": group_fp.size_bytes,
                "group_projection_sha256": GROUP_LOCK["replay_sha256"],
                "resolver_sha256": resolver_fp.sha256,
                "resolver_size_bytes": resolver_fp.size_bytes,
                "resolver_payload_sha256": resolver_document["payload_sha256"],
            },
            "component_validation": {
                "group": group_validation,
                "resolver": resolver_validation,
            },
            "source_contract_sha256": exact.sha256_bytes(
                exact.canonical_leaf_bytes(source_before)
            ),
            "g0_released_authority_sha256": exact.sha256_bytes(
                exact.canonical_leaf_bytes(g0)
            ),
            "executed_gates": [f"G{index}" for index in range(8)],
            "gate_payload_sha256": {
                f"G{index}": exact.sha256_bytes(
                    exact.canonical_leaf_bytes(expected[key])
                )
                for index, key in enumerate(gate_keys)
            },
            "full_semantic_leaf_rebuild": True,
            "payload_scalar_leaf_count": scalar_leaf_count(expected),
            "payload_shape_sha256": exact.sha256_bytes(
                exact.canonical_leaf_bytes(shape_value(expected))
            ),
            "scalar_leaf_rebound": rebound,
            "evidence_rebound": evidence_rebound,
            "strict_parser_cases": parser_report,
            "source_architecture_audit": source_audit,
            "backend_contract": backends,
            "child_snapshot_rebind_checks": guard.rebind_checks,
            "source_evidence_authority_stable_before_after_every_child": True,
            "independent_checker_does_not_import_or_call_producer_theorem_helpers": True,
            "independent_check_report_policy": (
                "REPORT_HAS_NO_SELF_HASH_AND_IS_NOT_A_CERTIFICATE_INPUT"
            ),
            "paper_status": expected["status"]["paper_status"],
            "release_status": "NOT_RELEASED",
            "promotion_authorized": False,
        }
        report_raw = exact.canonical_json_bytes(report, pretty=True)

        if not exact.deep_exact(source_before, exact_source_contract()):
            raise exact.StrictDataError("C61 source changed before report write")
        rebind_raw_inputs(
            (certificate_path, schema_path, group_path, resolver_path), originals
        )
        guard.assert_unchanged("immediately before independent report write")
        if stage_snapshot(stage_parent, input_names) != stage_before:
            raise exact.StrictDataError("C61 stage changed immediately before report write")
        exact.atomic_write(output_path, report_raw, mode=0o644)
        wrote_output = True

        expected_after_names = set(input_names)
        expected_after_names.add("c61_check_report.json")
        after = stage_snapshot(stage_parent, expected_after_names)
        if any(after[name] != stage_before[name] for name in input_names):
            raise exact.StrictDataError("C61 stage input changed across report write")
        output_seal = after["c61_check_report.json"]
        output_raw, _ = exact.read_stable(output_path, max_bytes=2_000_000)
        if (
            output_raw != report_raw
            or output_seal.sha256 != exact.sha256_bytes(report_raw)
            or output_seal.size_bytes != len(report_raw)
            or output_seal.mode != 0o644
            or output_seal.nlink != 1
            or output_path.resolve(strict=True) != output_path
        ):
            raise exact.StrictDataError("C61 report post-write seal differs")

        post_guard = SnapshotGuard(
            [*protected, output_path], directories=(CODE_DIR, stage_parent)
        )
        if not exact.deep_exact(source_before, exact_source_contract()):
            raise exact.StrictDataError("C61 source changed after report write")
        rebind_raw_inputs(
            (certificate_path, schema_path, group_path, resolver_path), originals
        )
        post_g0 = rebuild_g0(post_guard)
        if not exact.deep_exact(g0, post_g0):
            raise exact.StrictDataError("C61 authority changed across report write")
        post_guard.assert_unchanged("after independent report write and authority rebound")
        assert_cache_free()
    except BaseException:
        if wrote_output and output_path.is_file() and not output_path.is_symlink():
            output_path.unlink()
        raise
    finally:
        _EXPECTED_DIGEST_CACHE.clear()

    print("C61 CHECK PASS PREFREEZE")
    print("theorem_gates=8")
    print(f"payload_scalar_leaves={scalar_leaf_count(expected)}")
    print(f"rebound_mutations={rebound['total_certificate_mutations_rejected']}")
    print(
        "evidence_artifact_rebounds="
        f"{evidence_rebound['total_evidence_and_artifact_rebounds_rejected']}"
    )


if __name__ == "__main__":
    main()
