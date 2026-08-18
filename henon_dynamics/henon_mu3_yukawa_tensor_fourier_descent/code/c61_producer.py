#!/usr/bin/env python3
"""Assemble the strict integrated HCS-C61 PREFREEZE certificate.

The tensor/Burnside group evidence and Fourier/resolvent evidence are immutable
inputs.  This producer owns the integration layer: it rebinds the immutable
P60/C60 release, the installed C61 target layer, the exact source inventory,
and the executable backends; validates complete component documents; and
reconstructs every integrated G1--G6 conclusion from component leaves.

Both component documents are validated through their independently frozen,
source-owned public APIs before any integrated conclusion is constructed.
Selection aids are never runtime inputs or theorem authority.
"""

from __future__ import annotations

import argparse
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

import c61_exact
import c61_group
import c61_pipeline
import c61_resolvent


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


PROJECT_BASENAME = "henon_mu3_yukawa_tensor_fourier_descent"
CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
if (
    CODE.name == "code"
    and PROJECT.name == PROJECT_BASENAME
    and PROJECT.parent.name == "henon_dynamics"
):
    REPO = PROJECT.parents[1]
else:
    REPO = Path("/__C61_STAGED_SOURCE_HAS_NO_REPOSITORY_AUTHORITY__")
    PROJECT = REPO / "henon_dynamics" / PROJECT_BASENAME
    CODE = PROJECT / "code"
RESULTS = PROJECT / "results"
DYNAMICS = PROJECT.parent
BATCH = DYNAMICS / "BATCH_PLAN_C57_C61.md"
GUARD = DYNAMICS / "codex_prompt.md"
ROUTE = PROJECT / "route_a_evaluation.yaml"
C60_PROJECT = DYNAMICS / "henon_mu3_yukawa_biquadratic_envelope"
C60_ROUTE = C60_PROJECT / "route_a_evaluation.yaml"
C60_ROUTE_ARCHIVE = (
    C60_PROJECT / "evaluations/route_a/HCS-C60/20260817T000000Z.yaml"
)
C60_FULL_MANIFEST = C60_PROJECT / "FULL_PROJECT_HASHES.sha256"
C60_SCOPED_MANIFEST = C60_PROJECT / "results/scoped_hash_manifest.json"
C60_CERTIFICATE = C60_PROJECT / "results/c60_certificate.json"
C60_SCHEMA = C60_PROJECT / "results/c60_schema.json"
C60_CHECK_REPORT = C60_PROJECT / "results/c60_check_report.json"
C60_GROUP_EVIDENCE = C60_PROJECT / "results/c60_group_evidence.json"
C60_RESOLVENT_EVIDENCE = C60_PROJECT / "results/c60_resolvent_evidence.json"


CODE_FILES = (
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
)
RESULT_FILES = (
    "RESULTS.md",
    "TEST_REPORT.md",
    "c61_certificate.json",
    "c61_check_report.json",
    "c61_group_evidence.json",
    "c61_resolvent_evidence.json",
    "c61_schema.json",
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
    "c61_group_evidence.json",
    "c61_resolvent_evidence.json",
)
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
SCOPE_NONCLAIM_KEYS = (
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
)


# Immutable release, installed target-layer, and independent component pins.
P60_RELEASE_COMMIT = "fe1217810b72840619efdf40a2af31b8b80d96f6"
P60_RELEASE_PARENT = "f3b3726c40519cdd8ac7832f9f22df16d451b890"
P60_RELEASE_TREE = "22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a"
P60_RELEASED_BATCH_SHA256 = (
    "d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5"
)
P60_RELEASED_BATCH_SIZE_BYTES = 34_176

FORMAL_PACKAGE_SHA256 = (
    "c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28"
)
ROUTE_SHA256 = "c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b"
BATCH_SHA256 = "13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814"
TARGET_LOCK_INPUT_LEDGER_SHA256 = (
    "61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5"
)
TARGET_LOCK_INPUT_TOTAL_BYTES = 199_565
TARGET_LOCK_INPUT_LINE_COUNT = 5_094
GUARD_SHA256 = "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead"

C60_FULL_MANIFEST_SHA256 = (
    "37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4"
)
C60_ROUTE_SHA256 = "8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"
C60_CERTIFICATE_SHA256 = (
    "d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518"
)
C60_PAYLOAD_SHA256 = "dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead"
C60_SCHEMA_SHA256 = "c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5"
C60_CHECK_REPORT_SHA256 = (
    "25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44"
)
C60_SCOPED_MANIFEST_SHA256 = (
    "f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7"
)
C60_GROUP_EVIDENCE_SHA256 = (
    "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2"
)
C60_RESOLVENT_EVIDENCE_SHA256 = (
    "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da"
)
C60_SOURCE_CONTRACT_SHA256 = (
    "4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90"
)
C60_FROZEN_ARRAYS_SHA256 = (
    "0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5"
)
C60_L_CARRIER_SHA256 = (
    "fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5"
)

GROUP_COMPONENT: dict[str, Any] | None = {
    "aggregate_sha256": (
        "f6fccf6aa815476a29193a5764ba4cac3916851ff68dbd9788620b6751b87208"
    ),
    "producer_sha256": (
        "64dfabdec2cf5767e4022c21a0ad7385efaa191df209c739ab7e015c46a83b5f"
    ),
    "checker_sha256": (
        "4fc377dc16f5b4ebec68767709d1e3e5e2a137b6694567f0b42cb9d88406862e"
    ),
    "evidence_sha256": (
        "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9"
    ),
    "replay_sha256": (
        "ebd3c174ecc76cb26792dfd24e547a59148f1d13e7a59d4f74a53f8bfb8c860b"
    ),
    "python_projection_sha256": (
        "34ab65dadc1a2fe2b697d290f473b8fbb349b46b6772401eaef21ab8d9d0e970"
    ),
    "artifact_count": 4,
    "total_bytes": 1_283_518,
}
RESOLVER_COMPONENT: dict[str, Any] | None = {
    "aggregate_sha256": (
        "b43f6902f7fec40d5d595ccab423f9d8260da2ade1824dc3d12ba006fd4bf74c"
    ),
    "producer_sha256": (
        "1c6e18ba4533908ef327cbc574e9d3b8268d1d0f2c9adf6ab2a9d6e86ae40c20"
    ),
    "checker_sha256": (
        "f247dfdf393499c6a41df3dfa34815c1f4557781ec604639da47b921e90c9f6a"
    ),
    "evidence_sha256": (
        "1be0f9ac4e05ee7a747d39c546502d59dc29bb1407932e14875b61a3b82afe0f"
    ),
    "payload_sha256": (
        "956f99f419e08f78d7b8c3304e840a90ca50ac7271635b5e46d9ba5c9c391918"
    ),
    "schema_sha256": (
        "9925f23879bef26b6f5805ae2f0affe37785d5e569c929c706afaf80abdecf1d"
    ),
    "artifact_count": 3,
    "total_bytes": 750_694,
}
WRITTEN_BRIDGE_KEYS: tuple[str, ...] | None = (
    "released_P60_C60_to_target_object_and_conventions",
    "three_tensor_atlases_to_burnside_and_zeta_products",
    "mixed_160_12_8_atlas_to_fixed_field_dictionary",
    "split_noncollision_and_stabilizers_to_primitive_fixed_fields",
    "fourier_characters_and_type3_to_degree_40_diamond",
    "conductor_orbits_to_signed_global_and_relative_discriminants",
    "both_D3_branches_to_relative_towers_and_primewise_ideal_laws",
)
COMPONENT_SOURCE_LOCKS: dict[str, str] | None = {
    "c61_checker_group.g": (
        "4fc377dc16f5b4ebec68767709d1e3e5e2a137b6694567f0b42cb9d88406862e"
    ),
    "c61_checker_resolvent.py": (
        "f247dfdf393499c6a41df3dfa34815c1f4557781ec604639da47b921e90c9f6a"
    ),
    "c61_group.py": (
        "64dfabdec2cf5767e4022c21a0ad7385efaa191df209c739ab7e015c46a83b5f"
    ),
    "c61_resolvent.py": (
        "1c6e18ba4533908ef327cbc574e9d3b8268d1d0f2c9adf6ab2a9d6e86ae40c20"
    ),
}

SCHEMA_ID = "hcs-c61-certificate-schema-v1"
MAX_CERTIFICATE_BYTES = 12_000_000
MAX_JSON_BYTES = 30_000_000
MANIFEST_PATTERN = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")
STAGE_NAME_PATTERN = re.compile(r"^\.c61-stage-[A-Za-z0-9]{8}$")


def _fail(message: str) -> None:
    raise c61_exact.StrictDataError(message)


def _require_digest(value: Any, label: str) -> str:
    return c61_exact.require_sha256(value, label)


def _require_keys(
    value: Any, expected: Iterable[str], label: str
) -> dict[str, Any]:
    return c61_exact.require_exact_keys(value, set(expected), label)


def _canonical_payload_sha256(value: Any) -> str:
    return c61_exact.sha256_bytes(c61_exact.canonical_leaf_bytes(value))


def _canonical_report_sha256(value: Any) -> str:
    return c61_exact.sha256_bytes(c61_exact.canonical_json_bytes(value))


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
        raise c61_exact.StrictDataError(f"required file is missing: {path}") from exc
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
    value = c61_exact.strict_json_loads(raw, max_bytes=max_bytes)
    if type(value) is not dict:
        _fail(f"JSON root must be an object: {path}")
    expected = c61_exact.canonical_json_bytes(value, pretty=canonical_pretty)
    if raw != expected:
        _fail(f"JSON bytes are not canonical: {path}")
    return value, raw, fingerprint


def _parse_sha256_manifest(raw: bytes, label: str) -> dict[str, str]:
    try:
        lines = raw.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise c61_exact.StrictDataError(f"{label} manifest is not UTF-8") from exc
    entries: dict[str, str] = {}
    for line in lines:
        match = MANIFEST_PATTERN.fullmatch(line)
        if match is None:
            _fail(f"{label} manifest row is malformed")
        digest, relative = match.groups()
        if not c61_exact.safe_relative_path(relative) or relative in entries:
            _fail(f"{label} manifest contains an unsafe/duplicate path")
        entries[relative] = digest
    if not entries or list(entries) != sorted(entries):
        _fail(f"{label} manifest must be nonempty and path-sorted")
    return entries


def _relative_to_repo(path: Path) -> str:
    try:
        return path.resolve(strict=True).relative_to(
            REPO.resolve(strict=True)
        ).as_posix()
    except ValueError as exc:
        raise c61_exact.StrictDataError(f"path escapes repository: {path}") from exc


def _file_binding(
    path: Path, expected_sha256: str, label: str, *, max_bytes: int = 8_000_000
) -> tuple[dict[str, Any], bytes]:
    raw, seal = _stable_bytes(path, max_bytes=max_bytes)
    if seal.sha256 != expected_sha256:
        _fail(f"{label} digest changed")
    return {
        "path": _relative_to_repo(path),
        "sha256": seal.sha256,
        "size_bytes": seal.size_bytes,
    }, raw


def _git_stdout(arguments: Sequence[str], label: str) -> bytes:
    result = subprocess.run(
        ["/usr/bin/git", "-C", str(REPO), *arguments],
        cwd=Path("/"),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=c61_pipeline.clean_environment(),
        check=False,
        timeout=60,
    )
    if result.returncode != 0 or result.stderr or len(result.stdout) > 2_000_000:
        _fail(f"{label} failed or emitted invalid output")
    return result.stdout


def _git_ascii(arguments: Sequence[str], label: str) -> str:
    try:
        return _git_stdout(arguments, label).decode("ascii", errors="strict").strip()
    except UnicodeDecodeError as exc:
        raise c61_exact.StrictDataError(f"{label} is not ASCII") from exc


def _route_top_scalar(route_text: str, key: str) -> str | bool | None:
    matches = re.findall(rf"(?m)^{re.escape(key)}:[ \t]*(.*?)$", route_text)
    if len(matches) != 1:
        _fail(f"installed Route top-level scalar is missing/duplicated: {key}")
    token = matches[0]
    if token == "true":
        return True
    if token == "false":
        return False
    if token == "null":
        return None
    if len(token) >= 2 and token[0] == token[-1] == '"':
        decoded = json.loads(token)
        if type(decoded) is not str:
            _fail(f"installed Route scalar has a non-string quoted value: {key}")
        return decoded
    if not token or token[0] in "'[{&*!|>@`":
        _fail(f"installed Route scalar uses a forbidden complex form: {key}")
    return token


def source_contract() -> dict[str, Any]:
    code = _regular_directory(CODE, "C61 code directory")
    code_before = _directory_snapshot(code)
    imported_modules = {
        "c61_exact.py": c61_exact,
        "c61_group.py": c61_group,
        "c61_pipeline.py": c61_pipeline,
        "c61_resolvent.py": c61_resolvent,
    }
    for name, module in imported_modules.items():
        module_file = getattr(module, "__file__", None)
        if (
            type(module_file) is not str
            or Path(module_file).resolve(strict=True)
            != (code / name).resolve(strict=True)
        ):
            _fail(f"imported C61 module does not come from canonical code: {name}")
    children = list(code.iterdir())
    if any(path.is_symlink() or not path.is_file() for path in children):
        _fail("C61 code inventory contains a non-regular entry")
    observed = {path.name for path in children}
    expected = set(CODE_FILES)
    if len(observed) != len(children) or observed != expected:
        _fail(
            f"C61 code inventory mismatch; missing={sorted(expected-observed)}; "
            f"extra={sorted(observed-expected)}"
        )
    locks = COMPONENT_SOURCE_LOCKS
    if locks is None:
        _fail("C61 component source hashes are not frozen")
    if set(locks) != {
        "c61_group.py", "c61_checker_group.g",
        "c61_resolvent.py", "c61_checker_resolvent.py",
    }:
        _fail("C61 component source lock has the wrong exact-four keys")
    entries: list[dict[str, Any]] = []
    for name in CODE_FILES:
        raw, fingerprint = _stable_bytes(code / name, max_bytes=8_000_000)
        expected_mode = "0755" if name == "run_all.sh" else "0644"
        observed_mode = f"{stat.S_IMODE(fingerprint.mode):04o}"
        if observed_mode != expected_mode:
            _fail(
                f"C61 code mode mismatch for {name}: "
                f"expected {expected_mode}, observed {observed_mode}"
            )
        if name in locks and fingerprint.sha256 != locks[name]:
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
        _fail("C61 code directory changed during source-contract binding")
    return {
        "schema_id": "hcs-c61-source-contract-v1",
        "entry_count": 13,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [f"code/{name}" for name in CODE_FILES],
        "entries": entries,
        "mode_policy": "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644",
        "self_reference_policy": (
            "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE"
        ),
    }


def _verify_released_c60_full_manifest() -> tuple[dict[str, Any], dict[str, str]]:
    project = _regular_directory(C60_PROJECT, "released C60 project")
    project_before = _directory_snapshot(project)
    raw, seal = _stable_bytes(C60_FULL_MANIFEST, max_bytes=2_000_000)
    if seal.sha256 != C60_FULL_MANIFEST_SHA256:
        _fail("released C60 full-manifest digest changed")
    c60_git_root = f"henon_dynamics/{C60_PROJECT.name}"
    git_manifest = _git_stdout(
        ["show", f"{P60_RELEASE_COMMIT}:{c60_git_root}/FULL_PROJECT_HASHES.sha256"],
        "released C60 immutable full-manifest lookup",
    )
    if git_manifest != raw:
        _fail("released C60 live/Git-object full manifests differ")
    manifest = _parse_sha256_manifest(raw, "C60 full")
    if len(manifest) != 88 or "FULL_PROJECT_HASHES.sha256" in manifest:
        _fail("released C60 full-manifest count/self-exclusion changed")
    try:
        git_tree_paths = _git_stdout(
            [
                "ls-tree", "-r", "--name-only", P60_RELEASE_COMMIT,
                "--", c60_git_root,
            ],
            "released C60 immutable tree inventory",
        ).decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise c61_exact.StrictDataError(
            "released C60 immutable tree inventory is not UTF-8"
        ) from exc
    prefix = f"{c60_git_root}/"
    if any(not path.startswith(prefix) for path in git_tree_paths):
        _fail("released C60 immutable tree inventory escaped its root")
    git_relatives = [path[len(prefix):] for path in git_tree_paths]
    if (
        git_relatives != sorted(git_relatives)
        or set(git_relatives)
        != set(manifest) | {"FULL_PROJECT_HASHES.sha256"}
    ):
        _fail("released C60 immutable Git tree differs from its exact manifest")

    observed_files: set[str] = set()
    observed_directories: set[str] = set()
    for path in project.rglob("*"):
        relative = path.relative_to(project).as_posix()
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            _fail("released C60 tree contains a symlink")
        if stat.S_ISREG(metadata.st_mode):
            if relative != "FULL_PROJECT_HASHES.sha256":
                observed_files.add(relative)
        elif stat.S_ISDIR(metadata.st_mode):
            observed_directories.add(relative)
        else:
            _fail("released C60 tree contains a special object")
    allowed_directories: set[str] = set()
    for relative in set(manifest) | {"FULL_PROJECT_HASHES.sha256"}:
        for parent in PurePosixPath(relative).parents:
            if parent.as_posix() != ".":
                allowed_directories.add(parent.as_posix())
    if observed_files != set(manifest) or observed_directories != allowed_directories:
        _fail("released C60 live tree does not exactly match its 88-entry manifest")

    total_bytes = 0
    immutable_git_total_bytes = 0
    for relative, expected in manifest.items():
        leaf_raw, leaf_seal = _stable_bytes(
            project / relative, max_bytes=210_000_000
        )
        if leaf_seal.sha256 != expected:
            _fail(f"released C60 leaf changed: {relative}")
        git_raw = _git_stdout(
            ["show", f"{P60_RELEASE_COMMIT}:{c60_git_root}/{relative}"],
            f"released C60 immutable leaf lookup {relative}",
        )
        if git_raw != leaf_raw:
            _fail(f"released C60 live/Git-object leaf differs: {relative}")
        total_bytes += len(leaf_raw)
        immutable_git_total_bytes += len(git_raw)
    final_files: set[str] = set()
    final_directories: set[str] = set()
    for path in project.rglob("*"):
        relative = path.relative_to(project).as_posix()
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            _fail("released C60 tree gained a symlink during rebind")
        if stat.S_ISREG(metadata.st_mode):
            if relative != "FULL_PROJECT_HASHES.sha256":
                final_files.add(relative)
        elif stat.S_ISDIR(metadata.st_mode):
            final_directories.add(relative)
        else:
            _fail("released C60 tree gained a special object during rebind")
    if (
        _directory_snapshot(project) != project_before
        or final_files != observed_files
        or final_directories != observed_directories
    ):
        _fail("released C60 tree changed during full-manifest verification")
    return {
        "entry_count": 88,
        "inventory_exact_excluding_self": True,
        "manifest_path": _relative_to_repo(C60_FULL_MANIFEST),
        "manifest_sha256": seal.sha256,
        "manifest_size_bytes": seal.size_bytes,
        "verified_leaf_total_bytes": total_bytes,
        "immutable_git_object_inventory_exact": True,
        "immutable_git_object_leaves_rebound": 88,
        "immutable_git_object_leaf_total_bytes": immutable_git_total_bytes,
        "live_tree_equals_immutable_git_tree": True,
    }, manifest


def _validate_c60_scoped_manifest(full_manifest: dict[str, str]) -> dict[str, Any]:
    value, raw, seal = _read_json(
        C60_SCOPED_MANIFEST, max_bytes=2_000_000, canonical_pretty=True
    )
    if seal.sha256 != C60_SCOPED_MANIFEST_SHA256:
        _fail("released C60 scoped-manifest digest changed")
    _require_keys(
        value,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        "released C60 scoped manifest",
    )
    if (
        value["entry_count"] != 20
        or value["manifest_self_included"] is not False
        or value["schema"] != "hcs-c60-scoped-hash-manifest-v1"
        or value["scope"] != "exact_C60_code_and_results_artifacts"
        or type(value["entries"]) is not list
        or len(value["entries"]) != 20
    ):
        _fail("released C60 scoped-manifest header changed")
    seen: set[str] = set()
    for index, row in enumerate(value["entries"]):
        row = _require_keys(
            row, {"path", "sha256", "size_bytes"},
            f"released C60 scoped manifest row {index}",
        )
        relative = row["path"]
        if (
            type(relative) is not str
            or not c61_exact.safe_relative_path(relative)
            or relative in seen
            or full_manifest.get(relative) != row["sha256"]
            or type(row["size_bytes"]) is not int
            or type(row["size_bytes"]) is bool
            or row["size_bytes"] < 0
        ):
            _fail("released C60 scoped-manifest row changed")
        leaf_raw, leaf_seal = _stable_bytes(
            C60_PROJECT / relative, max_bytes=8_000_000
        )
        if leaf_seal.sha256 != row["sha256"] or len(leaf_raw) != row["size_bytes"]:
            _fail("released C60 scoped-manifest leaf binding changed")
        seen.add(relative)
    if [row["path"] for row in value["entries"]] != sorted(seen):
        _fail("released C60 scoped-manifest rows are not path-sorted")
    return {
        "path": _relative_to_repo(C60_SCOPED_MANIFEST),
        "sha256": seal.sha256,
        "size_bytes": len(raw),
        "entry_count": 20,
        "full_manifest_consistent": True,
    }


def _rebind_released_p60_c60() -> dict[str, Any]:
    commit = _git_ascii(["rev-parse", P60_RELEASE_COMMIT], "P60 commit lookup")
    parent = _git_ascii(
        ["rev-parse", f"{P60_RELEASE_COMMIT}^"], "P60 parent lookup"
    )
    tree = _git_ascii(
        ["rev-parse", f"{P60_RELEASE_COMMIT}^{{tree}}"], "P60 tree lookup"
    )
    object_type = _git_ascii(
        ["cat-file", "-t", P60_RELEASE_COMMIT], "P60 object-type lookup"
    )
    if (
        commit != P60_RELEASE_COMMIT
        or parent != P60_RELEASE_PARENT
        or tree != P60_RELEASE_TREE
        or object_type != "commit"
    ):
        _fail("immutable P60 commit/parent/tree object identity changed")
    ancestor = subprocess.run(
        [
            "/usr/bin/git", "-C", str(REPO), "merge-base", "--is-ancestor",
            P60_RELEASE_COMMIT, "HEAD",
        ],
        cwd=Path("/"), stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, env=c61_pipeline.clean_environment(),
        check=False, timeout=60,
    )
    if ancestor.returncode != 0 or ancestor.stdout or ancestor.stderr:
        _fail("immutable P60 commit is not an ancestor of current HEAD")
    released_batch = _git_stdout(
        [
            "show",
            f"{P60_RELEASE_COMMIT}:henon_dynamics/BATCH_PLAN_C57_C61.md",
        ],
        "released P60 Batch blob lookup",
    )
    if (
        hashlib.sha256(released_batch).hexdigest() != P60_RELEASED_BATCH_SHA256
        or len(released_batch) != P60_RELEASED_BATCH_SIZE_BYTES
    ):
        _fail("immutable P60 Batch blob changed")

    full, manifest = _verify_released_c60_full_manifest()
    scoped = _validate_c60_scoped_manifest(manifest)
    live_route, live_raw = _file_binding(
        C60_ROUTE, C60_ROUTE_SHA256, "released C60 live Route"
    )
    archive_route, archive_raw = _file_binding(
        C60_ROUTE_ARCHIVE, C60_ROUTE_SHA256, "released C60 archive Route"
    )
    if live_raw != archive_raw:
        _fail("released C60 live/archive Route bytes differ")

    certificate, certificate_raw, certificate_seal = _read_json(
        C60_CERTIFICATE, max_bytes=5_000_000, canonical_pretty=True
    )
    if certificate_seal.sha256 != C60_CERTIFICATE_SHA256:
        _fail("released C60 certificate digest changed")
    _require_keys(
        certificate, {"payload", "payload_sha256", "schema", "schema_sha256"},
        "released C60 certificate",
    )
    if (
        _canonical_payload_sha256(certificate["payload"]) != C60_PAYLOAD_SHA256
        or certificate["payload_sha256"] != C60_PAYLOAD_SHA256
        or _canonical_payload_sha256(certificate["schema"])
        != certificate["schema_sha256"]
    ):
        _fail("released C60 certificate internal hashes changed")
    source_contract_value = certificate["payload"].get("source_contract")
    if (
        type(source_contract_value) is not dict
        or _canonical_payload_sha256(source_contract_value)
        != C60_SOURCE_CONTRACT_SHA256
    ):
        _fail("released C60 source-contract projection changed")

    schema, schema_raw = _file_binding(
        C60_SCHEMA, C60_SCHEMA_SHA256, "released C60 schema"
    )
    check_report, check_raw = _file_binding(
        C60_CHECK_REPORT, C60_CHECK_REPORT_SHA256,
        "released C60 independent check report",
    )
    group, group_raw = _file_binding(
        C60_GROUP_EVIDENCE, C60_GROUP_EVIDENCE_SHA256,
        "released C60 group evidence",
    )
    resolver, resolver_raw = _file_binding(
        C60_RESOLVENT_EVIDENCE, C60_RESOLVENT_EVIDENCE_SHA256,
        "released C60 resolvent evidence",
    )
    return {
        "status": "RELEASED_P60_C60_REBOUND",
        "p60_git_objects": {
            "commit": commit,
            "parent": parent,
            "tree": tree,
            "commit_object_type": object_type,
            "ancestor_of_current_HEAD": True,
            "released_batch_sha256": P60_RELEASED_BATCH_SHA256,
            "released_batch_size_bytes": len(released_batch),
        },
        "c60_full_manifest": full,
        "c60_scoped_manifest": scoped,
        "c60_live_route": live_route,
        "c60_archive_route": archive_route,
        "c60_live_archive_route_identical": True,
        "c60_certificate_bundle": {
            "path": _relative_to_repo(C60_CERTIFICATE),
            "sha256": certificate_seal.sha256,
            "size_bytes": len(certificate_raw),
            "payload_sha256": C60_PAYLOAD_SHA256,
            "source_contract_sha256": C60_SOURCE_CONTRACT_SHA256,
            "schema": schema,
            "schema_bytes_rebound": len(schema_raw),
            "independent_check": check_report,
            "independent_check_bytes_rebound": len(check_raw),
        },
        "c60_group_evidence": {
            **group,
            "bytes_rebound": len(group_raw),
            "frozen_arrays_sha256": C60_FROZEN_ARRAYS_SHA256,
        },
        "c60_resolvent_evidence": {
            **resolver,
            "bytes_rebound": len(resolver_raw),
            "L_carrier_sha256": C60_L_CARRIER_SHA256,
        },
    }


def _formal_target_lock() -> dict[str, Any]:
    project = _regular_directory(PROJECT, "C61 project directory")
    project_before = _directory_snapshot(project)
    observed_markdown = {path.name for path in project.glob("*.md")}
    if observed_markdown != set(FORMAL_FILES):
        _fail("installed C61 target must have exactly 13 root Markdown files")
    rows: list[bytes] = []
    entries: list[dict[str, Any]] = []
    exact15: list[tuple[str, bytes]] = []
    for name in FORMAL_FILES:
        raw, seal = _stable_bytes(project / name, max_bytes=2_000_000)
        rows.append(f"{seal.sha256}  {name}\n".encode("ascii"))
        entries.append(
            {"path": name, "sha256": seal.sha256, "size_bytes": len(raw)}
        )
        exact15.append((f"{PROJECT_BASENAME}/{name}", raw))
    markdown_aggregate = hashlib.sha256(b"".join(rows)).hexdigest()
    route_raw, route_seal = _stable_bytes(ROUTE, max_bytes=1_000_000)
    batch_raw, batch_seal = _stable_bytes(BATCH, max_bytes=1_000_000)
    exact15.extend(
        (
            ("BATCH_PLAN_C57_C61.md", batch_raw),
            (f"{PROJECT_BASENAME}/route_a_evaluation.yaml", route_raw),
        )
    )
    exact15.sort(key=lambda row: row[0])
    ledger = b"".join(
        f"{hashlib.sha256(raw).hexdigest()}  {relative}\n".encode("ascii")
        for relative, raw in exact15
    )
    if (
        markdown_aggregate != FORMAL_PACKAGE_SHA256
        or route_seal.sha256 != ROUTE_SHA256
        or batch_seal.sha256 != BATCH_SHA256
        or hashlib.sha256(ledger).hexdigest() != TARGET_LOCK_INPUT_LEDGER_SHA256
        or sum(len(raw) for _, raw in exact15) != TARGET_LOCK_INPUT_TOTAL_BYTES
        or sum(raw.count(b"\n") for _, raw in exact15)
        != TARGET_LOCK_INPUT_LINE_COUNT
        or _directory_snapshot(project) != project_before
    ):
        _fail("installed C61 formal target-lock bytes changed")
    try:
        route_text = route_raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise c61_exact.StrictDataError("installed C61 Route is not UTF-8") from exc
    route_projection = {
        key: _route_top_scalar(route_text, key)
        for key in (
            "candidate_id", "candidate_definition", "project_root",
            "documentation_status", "theorem_status", "code_results_status",
            "paper_status", "release_status", "promotion_authorized",
        )
    }
    if route_projection != {
        "candidate_id": "HCS-C61",
        "candidate_definition": (
            "target-locked conditional theorem: three pairwise nonisomorphic "
            "but rationally linearized/zeta-equivalent finite-etale tensor "
            "algebras of the released W(E6) Gassmann pair, their complete "
            "self/mixed double-coset decompositions, and an exact normalized "
            "Fourier descent identifying the mixed type-3 degree-40 base"
        ),
        "project_root": (
            "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent"
        ),
        "documentation_status": "TARGET_LOCKED",
        "theorem_status": "TARGET_LOCKED",
        "code_results_status": "IMPLEMENTATION_PENDING",
        "paper_status": "PAPER_PENDING",
        "release_status": "NOT_RELEASED",
        "promotion_authorized": False,
    }:
        _fail("installed C61 Route target/status projection changed")
    return {
        "status": "TARGET_LOCK_INPUT_REBOUND",
        "aggregate_definition": (
            "SHA256_OF_LEXICOGRAPHIC_BASENAME_ORDERED_SHA256SUM_LINES_FOR_13_MARKDOWN_ROOTS"
        ),
        "entry_count": 13,
        "exact_formal_inventory": True,
        "entries": entries,
        "markdown_aggregate_sha256": markdown_aggregate,
        "route_path": _relative_to_repo(ROUTE),
        "route_sha256": route_seal.sha256,
        "route_size_bytes": len(route_raw),
        "route_semantic_projection": route_projection,
        "target_lock_input_entry_count": 15,
        "target_lock_input_ledger_sha256": hashlib.sha256(ledger).hexdigest(),
        "target_lock_input_total_bytes": TARGET_LOCK_INPUT_TOTAL_BYTES,
        "target_lock_input_line_count": TARGET_LOCK_INPUT_LINE_COUNT,
    }


def rebuild_g0() -> tuple[dict[str, Any], dict[str, bool]]:
    released = _rebind_released_p60_c60()
    formal = _formal_target_lock()
    batch, _ = _file_binding(BATCH, BATCH_SHA256, "installed C61 Batch")
    guard, _ = _file_binding(GUARD, GUARD_SHA256, "protected guard")
    bridge_keys = WRITTEN_BRIDGE_KEYS
    if bridge_keys is None:
        bridges: dict[str, bool] = {}
    else:
        if len(bridge_keys) == 0 or len(set(bridge_keys)) != len(bridge_keys):
            _fail("frozen written-bridge contract is invalid")
        bridges = {key: True for key in bridge_keys}
    return {
        "schema_id": "hcs-c61-released-authority-rebind-v1",
        "released_P60_C60": released,
        "formal_target_lock": formal,
        "batch_target_lock": batch,
        "protected_guard": guard,
        "target_object_and_conventions": {
            "candidate_id": "HCS-C61",
            "project_basename": PROJECT_BASENAME,
            "ambient_group": "W(E6)",
            "ambient_group_order": 51840,
            "subgroup_orders_Hplus_Hminus": [162, 162],
            "ordered_tensor_algebras": [
                "Fplus_tensor_Fplus", "Fplus_tensor_Fminus",
                "Fminus_tensor_Fminus",
            ],
            "tensor_algebra_dimension_each": 102400,
            "finite_etale_objects_not_single_fields": True,
            "permutation_arrays": "one_based",
            "sparse_monomial_labels": "zero_based",
            "composition": "left_after_right",
            "polynomial_action": "p(X_i)=X_p(i)",
            "tensor_cosets": "right_cosets_with_left_subgroup_action",
            "split_prime": 692717,
            "exact_arithmetic_only": True,
            "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        },
        "fixed_predecessor_paths_only": True,
        "all_released_full_inventories_rebound": True,
    }, bridges


def _require_component_contracts() -> tuple[dict[str, Any], dict[str, Any]]:
    if GROUP_COMPONENT is None or RESOLVER_COMPONENT is None:
        _fail("C61 component hashes and schemas are not frozen")
    group_keys = (
        "aggregate_sha256", "producer_sha256", "checker_sha256",
        "evidence_sha256", "replay_sha256", "python_projection_sha256",
        "artifact_count", "total_bytes",
    )
    resolver_keys = (
        "aggregate_sha256", "producer_sha256", "checker_sha256",
        "evidence_sha256", "payload_sha256", "schema_sha256",
        "artifact_count", "total_bytes",
    )
    if tuple(GROUP_COMPONENT) != group_keys:
        _fail("C61 group component lock has the wrong exact-eight shape")
    if tuple(RESOLVER_COMPONENT) != resolver_keys:
        _fail("C61 resolver component lock has the wrong exact-eight shape")
    for label, contract, keys, count, total in (
        (
            "group", GROUP_COMPONENT, group_keys[:6], 4, 1_283_518,
        ),
        (
            "resolver", RESOLVER_COMPONENT, resolver_keys[:6], 3, 750_694,
        ),
    ):
        for key in keys:
            _require_digest(contract[key], f"{label} component {key}")
        if (
            type(contract["artifact_count"]) is not int
            or type(contract["artifact_count"]) is bool
            or contract["artifact_count"] != count
            or type(contract["total_bytes"]) is not int
            or type(contract["total_bytes"]) is bool
            or contract["total_bytes"] != total
        ):
            _fail(f"C61 {label} component count/byte lock changed")
    return deepcopy(GROUP_COMPONENT), deepcopy(RESOLVER_COMPONENT)


def _artifact_contract_from_documents(
    group: dict[str, Any], resolver: dict[str, Any],
    *, group_size_bytes: int, resolver_size_bytes: int,
    validate_documents: bool = True,
) -> dict[str, Any]:
    group_lock, resolver_lock = _require_component_contracts()
    _strict_int(group_size_bytes, "group evidence size", minimum=1)
    _strict_int(resolver_size_bytes, "resolver evidence size", minimum=1)
    if validate_documents:
        _validate_component_documents(group, resolver)
    return {
        "artifact_count": 2,
        "artifacts": [
            {
                "path": "results/c61_group_evidence.json",
                "format": "canonical_compact_json",
                "sha256": group_lock["evidence_sha256"],
                "size_bytes": group_size_bytes,
                "schema_id": group["schema_id"],
                "internal_report_sha256": group_lock["replay_sha256"],
                "component_aggregate_sha256": group_lock["aggregate_sha256"],
            },
            {
                "path": "results/c61_resolvent_evidence.json",
                "format": "canonical_compact_json",
                "sha256": resolver_lock["evidence_sha256"],
                "size_bytes": resolver_size_bytes,
                "schema_id": resolver["schema_id"],
                "internal_report_sha256": resolver_lock["payload_sha256"],
                "component_aggregate_sha256": resolver_lock["aggregate_sha256"],
                "schema_descriptor_sha256": resolver_lock["schema_sha256"],
            },
        ],
        "component_contracts": {
            "group": group_lock,
            "fourier_resolvent": resolver_lock,
        },
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c61-artifact-contract-v1",
        "source_owned_full_document_validation": True,
    }


def artifact_contract(
    artifact_dir: Path, *, validate_documents: bool = True,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    directory = _regular_directory(artifact_dir, "C61 evidence directory")
    if (
        not STAGE_NAME_PATTERN.fullmatch(directory.name)
        or directory.parent != RESULTS.resolve(strict=True)
    ):
        _fail("evidence directory is not the canonical C61 runner stage")
    group_path = directory / ARTIFACT_NAMES[0]
    resolver_path = directory / ARTIFACT_NAMES[1]
    group, group_raw, group_seal = _read_json(
        group_path, max_bytes=MAX_JSON_BYTES, canonical_pretty=False
    )
    resolver, resolver_raw, resolver_seal = _read_json(
        resolver_path, max_bytes=MAX_JSON_BYTES, canonical_pretty=False
    )
    group_lock, resolver_lock = _require_component_contracts()
    if (
        group_seal.sha256 != group_lock["evidence_sha256"]
        or resolver_seal.sha256 != resolver_lock["evidence_sha256"]
        or stat.S_IMODE(group_seal.mode) != 0o644
        or stat.S_IMODE(resolver_seal.mode) != 0o644
    ):
        _fail("C61 component evidence digest/mode changed")
    contract = _artifact_contract_from_documents(
        group, resolver,
        group_size_bytes=len(group_raw), resolver_size_bytes=len(resolver_raw),
        validate_documents=validate_documents,
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
        _, group = _stable_bytes(self.group_evidence, max_bytes=MAX_JSON_BYTES)
        _, resolver = _stable_bytes(
            self.resolvent_evidence, max_bytes=MAX_JSON_BYTES
        )
        if group != self.group_seal or resolver != self.resolver_seal:
            _fail(f"immutable evidence changed at {label}")
        expected_names = {
            self.group_evidence.name, self.resolvent_evidence.name,
            self.output.name, self.schema_output.name,
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
                target_metadata = target.lstat()
                inode = (target_metadata.st_dev, target_metadata.st_ino)
                if (
                    not stat.S_ISREG(target_metadata.st_mode)
                    or target_metadata.st_nlink != 1
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
            "PROJECT/results/.c61-stage-[A-Za-z0-9]{8} direct child"
        )
    group_path = artifact_dir / ARTIFACT_NAMES[0]
    resolver_path = artifact_dir / ARTIFACT_NAMES[1]
    if output != artifact_dir / "c61_certificate.json":
        _fail("producer output must use the fixed certificate basename")
    if schema_output != artifact_dir / "c61_schema.json":
        _fail("producer schema output must use the fixed schema basename")
    expected_children = {
        group_path.name, resolver_path.name, output.name, schema_output.name,
    }
    observed_children = {path.name for path in artifact_dir.iterdir()}
    if not observed_children.issubset(expected_children):
        _fail("canonical stage contains an unexpected entry")
    if any(path.is_dir() for path in artifact_dir.iterdir()):
        _fail("canonical stage may contain files only")

    _, group_seal = _stable_bytes(group_path, max_bytes=MAX_JSON_BYTES)
    _, resolver_seal = _stable_bytes(resolver_path, max_bytes=MAX_JSON_BYTES)
    if (
        stat.S_IMODE(group_seal.mode) != 0o644
        or stat.S_IMODE(resolver_seal.mode) != 0o644
    ):
        _fail("stage evidence files must both have mode 0644")
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


def _validate_component_documents(
    group_evidence: dict[str, Any], resolver_evidence: dict[str, Any]
) -> None:
    """Invoke both independent source-owned full-document validators."""

    group_lock, resolver_lock = _require_component_contracts()
    if type(group_evidence) is not dict or type(resolver_evidence) is not dict:
        _fail("C61 component evidence roots must be objects")
    group_result = c61_group.validate_fast(group_evidence)
    if group_result is not None:
        _fail("C61 group validator changed its no-return PASS contract")
    resolver_result = c61_resolvent.validate_evidence_document(
        resolver_evidence
    )
    resolver_result = _require_keys(
        resolver_result,
        {
            "schema_id", "payload_sha256", "candidate_payload_sha256",
            "status", "release_status",
        },
        "resolver object-validation result",
    )
    embedded_candidate = _require_digest(
        resolver_evidence["independence_contract"]["checker_attestation"][
            "candidate_payload_sha256"
        ],
        "resolver embedded candidate payload digest",
    )
    if (
        resolver_result["schema_id"]
        != "hcs-c61-resolvent-object-validation-v1"
        or resolver_result["payload_sha256"]
        != resolver_lock["payload_sha256"]
        or resolver_result["candidate_payload_sha256"]
        != embedded_candidate
        or resolver_result["status"] != "PASS"
        or resolver_result["release_status"] != "NOT_RELEASED"
    ):
        _fail("C61 resolver object-validation result changed")
    group_hashes = _require_keys(
        group_evidence["component_hashes"],
        {
            "python_projection_sha256", "gap_projection_sha256",
            "subgroup_registry_sha256", "all_36_tensor_rows_sha256",
            "mixed_160_position_sha256", "raw_global_local_input_sha256",
        },
        "group component hashes",
    )
    if (
        group_evidence.get("schema_id") != "hcs-c61-group-evidence-v1"
        or group_evidence.get("semantic_firewall")
        != "NO_BAD_EULER_OR_ROOT_NUMBER"
        or group_evidence.get("status")
        != "STAGED_NONRELEASE_GROUP_COMPONENT"
        or group_hashes["python_projection_sha256"]
        != group_lock["python_projection_sha256"]
        or group_hashes["gap_projection_sha256"]
        != group_lock["replay_sha256"]
        or resolver_evidence.get("schema_id")
        != "hcs-c61-resolvent-evidence-v1"
        or resolver_evidence.get("schema_sha256")
        != resolver_lock["schema_sha256"]
        or resolver_evidence.get("payload_sha256")
        != resolver_lock["payload_sha256"]
        or resolver_evidence.get("status", {}).get(
            "resolver_component_status"
        ) != "RESOLVER_COMPONENT_PASS"
        or resolver_evidence.get("status", {}).get("release_status")
        != "NOT_RELEASED"
    ):
        _fail("C61 component evidence identity/status tuple changed")


def _strict_int(value: Any, label: str, *, minimum: int | None = None) -> int:
    if (
        type(value) is not int
        or (minimum is not None and value < minimum)
    ):
        _fail(f"{label} must be a strict integer")
    return value


def _strict_bool(value: Any, expected: bool, label: str) -> bool:
    if type(value) is not bool or value is not expected:
        _fail(f"{label} must be the Boolean {expected}")
    return value


def _strict_list(
    value: Any, label: str, *, length: int | None = None,
) -> list[Any]:
    if type(value) is not list or (length is not None and len(value) != length):
        _fail(f"{label} must have the required list shape")
    return value


def _deep_equal(left: Any, right: Any, label: str) -> None:
    if not c61_exact.deep_exact(left, right):
        _fail(f"{label} changed")


def _validate_source_contract_value(value: Any) -> dict[str, Any]:
    value = _require_keys(
        value,
        {
            "schema_id", "entry_count", "exact_code_inventory",
            "exact_code_path_allowlist", "entries", "mode_policy",
            "self_reference_policy",
        },
        "source contract",
    )
    if (
        value["schema_id"] != "hcs-c61-source-contract-v1"
        or value["entry_count"] != 13
        or value["exact_code_inventory"] is not True
        or value["exact_code_path_allowlist"]
        != [f"code/{name}" for name in CODE_FILES]
        or value["mode_policy"]
        != "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644"
        or value["self_reference_policy"]
        != (
            "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_"
            "CHECK_REPORT_LATER_BINDS_CERTIFICATE"
        )
    ):
        _fail("source-contract header changed")
    entries = _strict_list(value["entries"], "source-contract entries", length=13)
    if [row.get("path") if type(row) is dict else None for row in entries] != [
        f"code/{name}" for name in CODE_FILES
    ]:
        _fail("source-contract rows changed order or path")
    locks = COMPONENT_SOURCE_LOCKS
    if locks is None:
        _fail("component source locks are not frozen")
    for index, (name, row) in enumerate(zip(CODE_FILES, entries)):
        row = _require_keys(
            row, {"path", "sha256", "size_bytes", "mode_octal"},
            f"source-contract row {index}",
        )
        _require_digest(row["sha256"], f"source-contract digest {name}")
        _strict_int(row["size_bytes"], f"source-contract size {name}", minimum=1)
        expected_mode = "0755" if name == "run_all.sh" else "0644"
        if row["path"] != f"code/{name}" or row["mode_octal"] != expected_mode:
            _fail(f"source-contract path/mode changed: {name}")
        if name in locks and row["sha256"] != locks[name]:
            _fail(f"component source-contract digest changed: {name}")
    return value


def _validate_g0_value(value: Any) -> dict[str, Any]:
    value = _require_keys(
        value,
        {
            "schema_id", "released_P60_C60", "formal_target_lock",
            "batch_target_lock", "protected_guard",
            "target_object_and_conventions",
            "fixed_predecessor_paths_only",
            "all_released_full_inventories_rebound",
        },
        "G0 authority",
    )
    if value["schema_id"] != "hcs-c61-released-authority-rebind-v1":
        _fail("G0 schema changed")
    _strict_bool(
        value["fixed_predecessor_paths_only"], True,
        "G0 fixed-predecessor policy",
    )
    _strict_bool(
        value["all_released_full_inventories_rebound"], True,
        "G0 full-inventory rebind",
    )
    formal = _require_keys(
        value["formal_target_lock"],
        {
            "status", "aggregate_definition", "entry_count",
            "exact_formal_inventory", "entries", "markdown_aggregate_sha256",
            "route_path", "route_sha256", "route_size_bytes",
            "route_semantic_projection",
            "target_lock_input_entry_count",
            "target_lock_input_ledger_sha256",
            "target_lock_input_total_bytes", "target_lock_input_line_count",
        },
        "G0 formal target",
    )
    if (
        formal["status"] != "TARGET_LOCK_INPUT_REBOUND"
        or formal["entry_count"] != 13
        or formal["exact_formal_inventory"] is not True
        or formal["markdown_aggregate_sha256"] != FORMAL_PACKAGE_SHA256
        or formal["route_sha256"] != ROUTE_SHA256
        or formal["target_lock_input_entry_count"] != 15
        or formal["target_lock_input_ledger_sha256"]
        != TARGET_LOCK_INPUT_LEDGER_SHA256
        or formal["target_lock_input_total_bytes"]
        != TARGET_LOCK_INPUT_TOTAL_BYTES
        or formal["target_lock_input_line_count"]
        != TARGET_LOCK_INPUT_LINE_COUNT
    ):
        _fail("G0 formal target-lock tuple changed")
    expected_route_projection = {
        "candidate_id": "HCS-C61",
        "candidate_definition": (
            "target-locked conditional theorem: three pairwise nonisomorphic "
            "but rationally linearized/zeta-equivalent finite-etale tensor "
            "algebras of the released W(E6) Gassmann pair, their complete "
            "self/mixed double-coset decompositions, and an exact normalized "
            "Fourier descent identifying the mixed type-3 degree-40 base"
        ),
        "project_root": "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent",
        "documentation_status": "TARGET_LOCKED",
        "theorem_status": "TARGET_LOCKED",
        "code_results_status": "IMPLEMENTATION_PENDING",
        "paper_status": "PAPER_PENDING",
        "release_status": "NOT_RELEASED",
        "promotion_authorized": False,
    }
    if not c61_exact.deep_exact(
        formal["route_semantic_projection"], expected_route_projection
    ):
        _fail("G0 Route semantic projection changed")
    if (
        value["batch_target_lock"].get("sha256") != BATCH_SHA256
        or value["protected_guard"].get("sha256") != GUARD_SHA256
    ):
        _fail("G0 Batch/guard binding changed")
    released = _require_keys(
        value["released_P60_C60"],
        {
            "status", "p60_git_objects", "c60_full_manifest",
            "c60_scoped_manifest", "c60_live_route", "c60_archive_route",
            "c60_live_archive_route_identical", "c60_certificate_bundle",
            "c60_group_evidence", "c60_resolvent_evidence",
        },
        "G0 released P60/C60",
    )
    git_objects = released["p60_git_objects"]
    full_manifest = _require_keys(
        released["c60_full_manifest"],
        {
            "entry_count", "inventory_exact_excluding_self",
            "manifest_path", "manifest_sha256", "manifest_size_bytes",
            "verified_leaf_total_bytes",
            "immutable_git_object_inventory_exact",
            "immutable_git_object_leaves_rebound",
            "immutable_git_object_leaf_total_bytes",
            "live_tree_equals_immutable_git_tree",
        },
        "G0 released C60 full manifest",
    )
    if (
        released["status"] != "RELEASED_P60_C60_REBOUND"
        or released["c60_live_archive_route_identical"] is not True
        or git_objects.get("commit") != P60_RELEASE_COMMIT
        or git_objects.get("parent") != P60_RELEASE_PARENT
        or git_objects.get("tree") != P60_RELEASE_TREE
        or git_objects.get("released_batch_sha256")
        != P60_RELEASED_BATCH_SHA256
        or full_manifest["manifest_sha256"] != C60_FULL_MANIFEST_SHA256
        or full_manifest["entry_count"] != 88
        or full_manifest["inventory_exact_excluding_self"] is not True
        or full_manifest["immutable_git_object_inventory_exact"] is not True
        or full_manifest["immutable_git_object_leaves_rebound"] != 88
        or full_manifest["immutable_git_object_leaf_total_bytes"]
        != full_manifest["verified_leaf_total_bytes"]
        or full_manifest["live_tree_equals_immutable_git_tree"] is not True
        or released["c60_scoped_manifest"].get("sha256")
        != C60_SCOPED_MANIFEST_SHA256
        or released["c60_scoped_manifest"].get("entry_count") != 20
        or released["c60_live_route"].get("sha256") != C60_ROUTE_SHA256
        or released["c60_archive_route"].get("sha256") != C60_ROUTE_SHA256
        or released["c60_certificate_bundle"].get("sha256")
        != C60_CERTIFICATE_SHA256
        or released["c60_certificate_bundle"].get("payload_sha256")
        != C60_PAYLOAD_SHA256
        or released["c60_group_evidence"].get("sha256")
        != C60_GROUP_EVIDENCE_SHA256
        or released["c60_resolvent_evidence"].get("sha256")
        != C60_RESOLVENT_EVIDENCE_SHA256
    ):
        _fail("G0 released P60/C60 tuple changed")
    expected_object = {
        "candidate_id": "HCS-C61",
        "project_basename": PROJECT_BASENAME,
        "ambient_group": "W(E6)",
        "ambient_group_order": 51840,
        "subgroup_orders_Hplus_Hminus": [162, 162],
        "ordered_tensor_algebras": [
            "Fplus_tensor_Fplus", "Fplus_tensor_Fminus",
            "Fminus_tensor_Fminus",
        ],
        "tensor_algebra_dimension_each": 102400,
        "finite_etale_objects_not_single_fields": True,
        "permutation_arrays": "one_based",
        "sparse_monomial_labels": "zero_based",
        "composition": "left_after_right",
        "polynomial_action": "p(X_i)=X_p(i)",
        "tensor_cosets": "right_cosets_with_left_subgroup_action",
        "split_prime": 692717,
        "exact_arithmetic_only": True,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
    }
    if not c61_exact.deep_exact(
        value["target_object_and_conventions"], expected_object
    ):
        _fail("G0 target object/conventions changed")
    return value


def _group_python(group: dict[str, Any]) -> dict[str, Any]:
    return _require_keys(
        group["python_projection"],
        {
            "schema_id", "conventions", "ambient", "tensor_atlas",
            "burnside_linearization", "mixed_160_12_8", "P3_P6",
            "mixed_degree_640_recovery", "raw_global_local_inputs",
            "subgroup_registry", "status",
        },
        "group Python projection",
    )


def _cross_component_authority_and_sources(
    source_contract_value: dict[str, Any], g0: dict[str, Any],
    group: dict[str, Any], resolver: dict[str, Any],
) -> None:
    source_hashes = {
        row["path"]: row["sha256"] for row in source_contract_value["entries"]
    }
    group_source = group["source_contract"]
    group_repository = group_source["repository"]
    resolver_authority = resolver["authority"]
    resolver_release = resolver_authority["release"]
    if (
        group_repository.get("head") != P60_RELEASE_COMMIT
        or group_repository.get("origin_main") != P60_RELEASE_COMMIT
        or group_repository.get("sole_parent") != P60_RELEASE_PARENT
        or group_repository.get("tree") != P60_RELEASE_TREE
        or resolver_release.get("commit") != P60_RELEASE_COMMIT
        or resolver_release.get("parent") != P60_RELEASE_PARENT
        or resolver_release.get("tree") != P60_RELEASE_TREE
        or resolver_release.get("worktree_layer_included") is not False
    ):
        _fail("group/resolver immutable P60 authority differs")
    group_formal = group_source["formal_input"]
    resolver_formal = resolver_authority["formal_target"]
    if (
        group_formal.get("formal_13_root_sha256") != FORMAL_PACKAGE_SHA256
        or group_formal.get("formal_route_sha256") != ROUTE_SHA256
        or group_formal.get("formal_batch_sha256") != BATCH_SHA256
        or group_formal.get("formal_exact15_sha256")
        != TARGET_LOCK_INPUT_LEDGER_SHA256
        or resolver_formal.get("formal_root_aggregate_sha256")
        != FORMAL_PACKAGE_SHA256
        or resolver_formal.get("route_sha256") != ROUTE_SHA256
        or resolver_formal.get("batch_sha256") != BATCH_SHA256
        or resolver_formal.get("exact15_ledger_sha256")
        != TARGET_LOCK_INPUT_LEDGER_SHA256
        or resolver_formal.get("exact15_count") != 15
        or resolver_formal.get("exact15_bytes") != TARGET_LOCK_INPUT_TOTAL_BYTES
        or resolver_formal.get("exact15_lines") != TARGET_LOCK_INPUT_LINE_COUNT
        or not c61_exact.deep_exact(
            g0["formal_target_lock"]["route_semantic_projection"],
            {
                "candidate_id": "HCS-C61",
                "candidate_definition": (
                    "target-locked conditional theorem: three pairwise "
                    "nonisomorphic but rationally linearized/zeta-equivalent "
                    "finite-etale tensor algebras of the released W(E6) "
                    "Gassmann pair, their complete self/mixed double-coset "
                    "decompositions, and an exact normalized Fourier descent "
                    "identifying the mixed type-3 degree-40 base"
                ),
                "project_root": (
                    "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent"
                ),
                "documentation_status": "TARGET_LOCKED",
                "theorem_status": "TARGET_LOCKED",
                "code_results_status": "IMPLEMENTATION_PENDING",
                "paper_status": "PAPER_PENDING",
                "release_status": "NOT_RELEASED",
                "promotion_authorized": False,
            },
        )
    ):
        _fail("group/resolver/producer installed formal authority differs")
    if (
        group_source.get("c60_payload_sha256") != C60_PAYLOAD_SHA256
        or group_source.get("c60_frozen_arrays_sha256")
        != C60_FROZEN_ARRAYS_SHA256
        or resolver_authority.get("c60_payload_sha256") != C60_PAYLOAD_SHA256
        or resolver_authority.get("frozen_permutation_arrays_sha256")
        != C60_FROZEN_ARRAYS_SHA256
        or resolver_authority.get("lambda_carrier_sha256")
        != C60_L_CARRIER_SHA256
        or group_source.get("pilot_runtime_inputs") != []
        or resolver_authority.get("runtime_pilot_dependencies") != []
    ):
        _fail("group/resolver released C60 or runtime-authority bridge differs")
    if (
        group["backend_contract"]["python"].get("producer_source_sha256")
        != source_hashes["code/c61_group.py"]
        or group["backend_contract"]["gap"].get("checker_source_sha256")
        != source_hashes["code/c61_checker_group.g"]
        or resolver_authority["source_files"]["producer"].get("sha256")
        != source_hashes["code/c61_resolvent.py"]
        or resolver_authority["source_files"]["checker"].get("sha256")
        != source_hashes["code/c61_checker_resolvent.py"]
    ):
        _fail("component evidence source hashes differ from exact source contract")


def _build_g1(group: dict[str, Any], resolver: dict[str, Any]) -> dict[str, Any]:
    del resolver
    python = _group_python(group)
    atlas = _require_keys(
        python["tensor_atlas"],
        {
            "rows", "row_counts", "degree_spectra", "dimensions",
            "Q_types", "P_types", "Q_type_count", "P_type_count",
            "Q_type_multisets",
        },
        "group tensor atlas",
    )
    rows = _require_keys(atlas["rows"], {"Tpp", "Tpm", "Tmm"}, "tensor rows")
    expected_spectra = {
        "Tpp": [320, 320, 960, 960, 1920, 5760, 5760, 8640, 8640, 17280, 25920, 25920],
        "Tpm": [640, 960, 960, 1920, 2880, 2880, 2880, 2880, 8640, 8640, 17280, 51840],
        "Tmm": [320, 320, 960, 960, 1920, 5760, 5760, 8640, 8640, 17280, 25920, 25920],
    }
    if (
        atlas["row_counts"] != {"Tpp": 12, "Tpm": 12, "Tmm": 12}
        or atlas["degree_spectra"] != expected_spectra
        or atlas["dimensions"] != {"Tpp": 102400, "Tpm": 102400, "Tmm": 102400}
        or atlas["Q_type_count"] != 18
        or atlas["P_type_count"] != 8
    ):
        _fail("G1 tensor atlas target tuple changed")
    for lane in ("Tpp", "Tpm", "Tmm"):
        lane_rows = _strict_list(rows[lane], f"G1 {lane} rows", length=12)
        if [row.get("simple_factor_degree") for row in lane_rows] != expected_spectra[lane]:
            _fail(f"G1 {lane} row/spectrum relation changed")
        if sum(row.get("simple_factor_degree", -1) for row in lane_rows) != 102400:
            _fail(f"G1 {lane} tensor dimension changed")
    burnside = _require_keys(
        python["burnside_linearization"],
        {
            "Hplus_conjugate_count", "Hminus_conjugate_count",
            "Hplus_Hminus_nonconjugate",
            "common_character_values_on_canonical_W",
            "common_character_sha256",
            "common_tensor_character_values_on_canonical_W",
            "common_tensor_character_sha256", "all_three_linearizations_equal",
            "all_three_zeta_products_equal_formal_Artin_consequence",
            "three_G_sets_pairwise_nonisomorphic",
            "three_field_factor_multisets_pairwise_distinct",
            "self_self_separator", "mixed_self_separator",
        },
        "group Burnside linearization",
    )
    character = _strict_list(
        burnside["common_character_values_on_canonical_W"],
        "G1 common character", length=51840,
    )
    square = _strict_list(
        burnside["common_tensor_character_values_on_canonical_W"],
        "G1 tensor character", length=51840,
    )
    if (
        square != [entry * entry for entry in character]
        or _canonical_payload_sha256(character) != burnside["common_character_sha256"]
        or _canonical_payload_sha256(square)
        != burnside["common_tensor_character_sha256"]
        or burnside["Hplus_conjugate_count"] != 160
        or burnside["Hminus_conjugate_count"] != 160
        or any(
            burnside[key] is not True
            for key in (
                "Hplus_Hminus_nonconjugate", "all_three_linearizations_equal",
                "all_three_zeta_products_equal_formal_Artin_consequence",
                "three_G_sets_pairwise_nonisomorphic",
                "three_field_factor_multisets_pairwise_distinct",
            )
        )
        or len({tuple(atlas["Q_type_multisets"][lane]) for lane in rows}) != 3
    ):
        _fail("G1 Burnside character/separation reconstruction changed")
    p3 = python["P3_P6"]
    if (
        p3.get("conjugated_minus_complete_set_equals_plus") is not True
        or p3.get("P3_nonconjugate_to_P6") is not True
        or p3.get("three_pairwise_nonconjugate_joins_claimed") is not False
        or p3.get("plus_self_seed") != 69
        or p3.get("minus_self_seed") != 86
        or p3.get("mixed_fourier_seed") != 149
        or p3.get("mixed_P6_join_sha256")
        != "55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc"
    ):
        _fail("G1 exact P3/P6 distinction changed")
    cross = group["cross_checks"]
    if cross.get("tensor_rows_checked") != 36 or any(
        value is not True for key, value in cross.items()
        if key != "tensor_rows_checked"
    ):
        _fail("G1 Python/GAP full-row cross-check changed")
    gap_burnside = group["gap_projection"]["burnside"]
    burnside_projection = {
        "Hplus_conjugate_count": burnside["Hplus_conjugate_count"],
        "Hminus_conjugate_count": burnside["Hminus_conjugate_count"],
        "Hplus_Hminus_nonconjugate": burnside[
            "Hplus_Hminus_nonconjugate"
        ],
        "common_character_value_count": len(character),
        "common_character_sha256": burnside["common_character_sha256"],
        "common_tensor_character_value_count": len(square),
        "common_tensor_character_sha256": burnside[
            "common_tensor_character_sha256"
        ],
        "common_character_values_on_25_GAP_classes": deepcopy(
            gap_burnside["common_character_values_on_25_classes"]
        ),
        "common_tensor_character_values_on_25_GAP_classes": deepcopy(
            gap_burnside[
                "common_tensor_character_values_on_25_classes"
            ]
        ),
        "all_three_linearizations_equal": burnside[
            "all_three_linearizations_equal"
        ],
        "all_three_zeta_products_equal_formal_Artin_consequence": burnside[
            "all_three_zeta_products_equal_formal_Artin_consequence"
        ],
        "three_G_sets_pairwise_nonisomorphic": burnside[
            "three_G_sets_pairwise_nonisomorphic"
        ],
        "three_field_factor_multisets_pairwise_distinct": burnside[
            "three_field_factor_multisets_pairwise_distinct"
        ],
        "self_self_separator": burnside["self_self_separator"],
        "mixed_self_separator": burnside["mixed_self_separator"],
        "full_51840_value_arrays_validated_not_duplicated": True,
    }
    return {
        "schema_id": "hcs-c61-g1-tensor-burnside-v1",
        "tensor_rows": deepcopy(rows),
        "row_counts": deepcopy(atlas["row_counts"]),
        "degree_spectra": deepcopy(atlas["degree_spectra"]),
        "tensor_dimensions": deepcopy(atlas["dimensions"]),
        "Q_types": deepcopy(atlas["Q_types"]),
        "P_types": deepcopy(atlas["P_types"]),
        "Q_type_count": 18,
        "P_type_count": 8,
        "Q_type_multisets": deepcopy(atlas["Q_type_multisets"]),
        "burnside_linearization": burnside_projection,
        "P3_P6_exact_distinction": deepcopy(p3),
        "python_gap_cross_checks": deepcopy(cross),
        "status": "G1_PASS",
    }


def _resolver_mixed_rows(resolver: dict[str, Any]) -> list[dict[str, Any]]:
    bridge = resolver["GAF4_mixed_type3_exact_bridge"]
    rows = _strict_list(bridge.get("mixed_rows"), "resolver mixed rows", length=12)
    if bridge.get("mixed_row_count") != 12:
        _fail("resolver mixed-row count changed")
    return rows


def _cross_mixed_rows(
    group_rows: list[dict[str, Any]], resolver_rows: list[dict[str, Any]],
) -> None:
    by_seed = {row.get("seed"): row for row in resolver_rows}
    if len(by_seed) != 12:
        _fail("resolver mixed rows have duplicate seeds")
    for row in group_rows:
        other = by_seed.get(row.get("seed"))
        expected = {
            "representative_one_based": row.get("representative_one_based"),
            "tensor_right_coset_orbit_size": row.get("orbit_size"),
            "intersection_order": row.get("intersection", {}).get("order"),
            "intersection_sha256": row.get("intersection", {}).get("group_sha256"),
            "simple_factor_degree": row.get("simple_factor_degree"),
            "join_order": row.get("join", {}).get("order"),
            "join_sha256": row.get("join", {}).get("group_sha256"),
            "intersection_field_degree": row.get("base_field_degree"),
        }
        if type(other) is not dict or any(other.get(key) != value for key, value in expected.items()):
            _fail(f"group/resolver mixed row differs at seed {row.get('seed')}")


def _build_g2(group: dict[str, Any], resolver: dict[str, Any]) -> dict[str, Any]:
    python = _group_python(group)
    atlas = python["tensor_atlas"]
    mixed = _require_keys(
        python["mixed_160_12_8"],
        {
            "conjugate_positions", "relative_position_types",
            "conjugate_position_count", "double_coset_factor_count",
            "Q_isomorphism_type_count", "multiplicities",
        },
        "group mixed atlas",
    )
    positions = _strict_list(
        mixed["conjugate_positions"], "mixed conjugate positions", length=160
    )
    types = _strict_list(
        mixed["relative_position_types"], "mixed relative-position types",
        length=8,
    )
    mixed_rows = _strict_list(
        atlas["rows"]["Tpm"], "mixed tensor rows", length=12
    )
    resolver_rows = _resolver_mixed_rows(resolver)
    _cross_mixed_rows(mixed_rows, resolver_rows)
    expected = {
        "raw_count": [1, 3, 3, 9, 9, 27, 27, 81],
        "tensor_factor_multiplicity": [1, 2, 1, 2, 2, 2, 1, 1],
        "compositum_degree": [640, 960, 1920, 2880, 2880, 8640, 17280, 51840],
        "base_field_degree": [160, 40, 40, 1, 1, 1, 1, 1],
        "intersection_order": [81, 54, 27, 18, 18, 6, 3, 1],
        "join_order": [324, 1296, 1296, 51840, 51840, 51840, 51840, 51840],
    }
    observed = {
        "raw_count": [row.get("raw_count") for row in types],
        "tensor_factor_multiplicity": [
            row.get("tensor_factor_multiplicity") for row in types
        ],
        "compositum_degree": [row.get("compositum_degree") for row in types],
        "base_field_degree": [row.get("base_field_degree") for row in types],
        "intersection_order": [row.get("intersection", {}).get("order") for row in types],
        "join_order": [row.get("join", {}).get("order") for row in types],
    }
    if (
        observed != expected
        or mixed["conjugate_position_count"] != 160
        or mixed["double_coset_factor_count"] != 12
        or mixed["Q_isomorphism_type_count"] != 8
        or mixed["multiplicities"] != expected["tensor_factor_multiplicity"]
        or sorted(row.get("index") for row in positions) != list(range(160))
        or sum(expected["raw_count"]) != 160
        or sum(expected["tensor_factor_multiplicity"]) != 12
    ):
        _fail("G2 exact 160/12/8 dictionary changed")
    for index, row in enumerate(types, 1):
        if (
            row.get("relative_position_type") != index
            or row.get("intersection", {}).get("core_order") != 1
        ):
            _fail("G2 type ordering/core-free extension changed")
    recovery = python["mixed_degree_640_recovery"]
    if (
        recovery.get("mixed_seed") != 148
        or recovery.get("factor_degree") != 640
        or recovery.get("base_degree") != 160
        or recovery.get("intersection_equals_released_C60_J_complete_set") is not True
        or recovery.get("join_equals_released_C60_N_complete_set") is not True
    ):
        _fail("G2 exact minimum C60 J/N recovery changed")
    if sum(row.get("simple_factor_degree") == 51840 for row in mixed_rows) != 1:
        _fail("G2 unique maximum K factor changed")
    return {
        "schema_id": "hcs-c61-g2-mixed-field-dictionary-v1",
        "conjugate_positions": deepcopy(positions),
        "conjugate_position_count": 160,
        "mixed_tensor_rows": deepcopy(mixed_rows),
        "mixed_resolver_rows": deepcopy(resolver_rows),
        "double_coset_factor_count": 12,
        "relative_position_types": deepcopy(types),
        "Q_isomorphism_type_count": 8,
        "multiplicities": deepcopy(mixed["multiplicities"]),
        "core_free_extension_for_all_eight_types": True,
        "unique_minimum_degree_640_recovery": deepcopy(recovery),
        "unique_maximum_factor_is_K": True,
        "group_resolver_complete_mixed_rows_cross_bound": True,
        "status": "G2_PASS",
    }


def _build_g3(group: dict[str, Any], resolver: dict[str, Any]) -> dict[str, Any]:
    python = _group_python(group)
    product = _require_keys(
        resolver["GAF3_stabilizers_and_noncollision"][
            "product_form_mixed_base_A_B_resolvents"
        ],
        {
            "construction", "split_prime", "labelled_root_count",
            "labelled_roots_sha256", "univariate_lagrange_basis_sha256",
            "integer_vanishing_polynomial_sha256",
            "full_mod_p_orbit_evaluation_matrix",
            "all_14_advertised_carriers_reconstructed", "carriers",
            "runtime_pilot_dependency",
        },
        "resolver product-form family",
    )
    carriers = _require_keys(
        product["carriers"],
        {
            *(f"E{index}" for index in range(1, 9)),
            *(f"C{index}" for index in range(1, 5)),
            "A40", "B80",
        },
        "resolver product-form carriers",
    )
    expected_degrees = {
        "E1": 640, "E2": 960, "E3": 1920, "E4": 2880,
        "E5": 2880, "E6": 8640, "E7": 17280, "E8": 51840,
        "C1": 160, "C2": 40, "C3": 40, "C4": 1,
        "A40": 40, "B80": 80,
    }
    if (
        product["split_prime"] != 692717
        or product["labelled_root_count"] != 27
        or product["full_mod_p_orbit_evaluation_matrix"] != "identity"
        or product["all_14_advertised_carriers_reconstructed"] is not True
        or product["runtime_pilot_dependency"] is not False
        or {name: row.get("degree") for name, row in carriers.items()}
        != expected_degrees
    ):
        _fail("G3 product-form family header/degrees changed")
    split_certificate = _require_keys(
        resolver["authority"][
            "released_C59_completely_split_prime_certificate"
        ],
        {
            "source_git_object", "prime_locator", "prime",
            "prime_proven_locator", "prime_proven", "factor_degrees_locator",
            "factor_degrees", "G1_factor_degrees_locator",
            "G1_factor_degrees", "labelled_roots_locator",
            "labelled_root_count", "labelled_roots_sha256",
            "labelled_roots_pairwise_distinct",
            "all_equation_residues_zero_locator",
            "all_equation_residues_zero", "K_completely_split_at_prime",
        },
        "released C59 completely-split certificate",
    )
    if (
        split_certificate["prime"] != 692717
        or split_certificate["prime_proven"] is not True
        or split_certificate["factor_degrees"] != [[1, 27]]
        or split_certificate["G1_factor_degrees"] != [[1, 27]]
        or split_certificate["labelled_root_count"] != 27
        or split_certificate["labelled_roots_pairwise_distinct"] is not True
        or split_certificate["all_equation_residues_zero"] is not True
        or split_certificate["K_completely_split_at_prime"] is not True
        or split_certificate["labelled_roots_sha256"]
        != product["labelled_roots_sha256"]
    ):
        _fail("G3 released C59 completely-split/27-label bridge changed")
    for name, row in carriers.items():
        degree = expected_degrees[name]
        if (
            row.get("field") != name
            or row.get("formal_stabilizer_equals_embedded_subgroup") is not True
            or row.get("complete_noncollision") is not True
            or row.get("modular_distinct_value_count") != degree
            or row.get("product_form_orbit_polynomial_factor_count") != degree
            or row.get("identity_value_mod_p") != 1
            or row.get("integral") is not True
            or row.get("exact_monomial_content") != 1
            or row.get("characteristic_zero_expanded_coefficients_claimed") is not False
        ):
            _fail(f"G3 product-form carrier semantics changed: {name}")
    relative_types = python["mixed_160_12_8"]["relative_position_types"]
    expected_subgroups = {
        **{
            f"E{index}": relative_types[index - 1]["intersection"]["group_sha256"]
            for index in range(1, 9)
        },
        **{
            f"C{index}": relative_types[index - 1]["join"]["group_sha256"]
            for index in range(1, 5)
        },
    }
    expected_subgroups["A40"] = expected_subgroups["C3"]
    expected_subgroups["B80"] = resolver["GAF3_stabilizers_and_noncollision"]["Splus"]["complete_group_sha256"]
    if any(
        carriers[name].get("subgroup_complete_group_sha256") != digest
        for name, digest in expected_subgroups.items()
    ):
        _fail("G3 group/resolver stabilizer hash cross-binding changed")
    ambient = python["ambient"]
    if (
        ambient.get("orders_W_Hplus_Hminus") != [51840, 162, 162]
        or ambient.get("W_permutation_count") != 51840
        or ambient.get("W_distinct_labelled_permutation_count") != 51840
        or ambient.get("labelled_W_action_faithful") is not True
        or group["gap_projection"].get("ambient")
        != {
            "W_permutation_count": 51840,
            "W_distinct_labelled_permutation_count": 51840,
            "labelled_W_action_faithful": True,
        }
    ):
        _fail(
            "G3 faithful labelled W action was not independently derived "
            "by both Python and GAP"
        )
    return {
        "schema_id": "hcs-c61-g3-product-resolvents-v1",
        "split_prime": product["split_prime"],
        "labelled_root_count": product["labelled_root_count"],
        "labelled_roots_sha256": product["labelled_roots_sha256"],
        "split_prime_complete_split_authority": deepcopy(
            split_certificate
        ),
        "labelled_W_action_faithful": True,
        "product_form_construction": product["construction"],
        "univariate_lagrange_basis_sha256": product[
            "univariate_lagrange_basis_sha256"
        ],
        "integer_vanishing_polynomial_sha256": product[
            "integer_vanishing_polynomial_sha256"
        ],
        "full_mod_p_orbit_evaluation_matrix": "identity",
        "carriers": deepcopy(carriers),
        "carrier_count": 14,
        "all_mod_p_orbit_values_pairwise_distinct": True,
        "all_characteristic_zero_orbit_values_pairwise_distinct": True,
        "all_Q_generator_fields_equal_exact_fixed_fields": True,
        "proof_bridge": (
            "faithful_labelled_W_action_plus_exact_formal_stabilizer_plus_"
            "complete_split_mod_p_noncollision"
        ),
        "runtime_pilot_dependency": False,
        "status": "G3_PASS",
    }


def _build_g4(group: dict[str, Any], resolver: dict[str, Any]) -> dict[str, Any]:
    fourier = resolver["GAF1_fourier_carrier_dag"]
    span = resolver["GAF2_orbit_span_and_nonnormality"]
    stabilizers = resolver["GAF3_stabilizers_and_noncollision"]
    bridge = resolver["GAF4_mixed_type3_exact_bridge"]
    diamond = resolver["GAF5_fixed_field_diamond"]
    records = fourier.get("normalized_carriers")
    expected_hashes = {
        "Trace": "a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7",
        "rplus": "2edfe1e8f952faf2ddbfae3af135da4509f3f40e4175e188e240a5f09b785a96",
        "r3": "b9c21c9fc7060d4e52630a75d6ec0c10305ac33946f78c2c93e33fad68df8c7e",
        "r0": "a26813d1b2874ee700ececba786af55391dacc2a30a0d4da0390ecb871f63382",
        "delta_plus": "1b5927b4d213dfd5af490067a9a551ae0942791a5221e2fb2f9f826440b040c3",
        "delta3": "5f8baf7254f5c27478afce45b5667c62d13a35b205739bbf20ebd36651a144e7",
    }
    if (
        type(records) is not dict
        or set(records) != set(expected_hashes)
        or any(records[name].get("carrier_sha256") != digest for name, digest in expected_hashes.items())
        or fourier.get("delta0_factorized_dag_sha256")
        != "ed8974824f48cc65299443609c94db5ceab06efb8bed36f44b99ead311d28a66"
        or fourier.get("identity_values_mod_p", {}).get("Trace") != 581739
        or fourier.get("identity_values_mod_p", {}).get("rplus") != 643771
        or fourier.get("identity_values_mod_p", {}).get("r3") != 119649
        or fourier.get("raw_components", {}).get("R0", {}).get("zero") is not True
        or any(value is not True for value in fourier.get("formal_identities", {}).values())
    ):
        _fail("G4 Fourier carrier/identity tuple changed")
    orbit_records = stabilizers.get("fourier_formal_and_evaluated_orbits")
    expected_orbits = {
        "rplus": 80, "delta_plus": 40, "r3": 320,
        "delta3": 160, "r0": 320, "delta0": 160,
    }
    if (
        type(orbit_records) is not dict
        or set(orbit_records) != set(expected_orbits)
        or any(
            orbit_records[name].get("formal_orbit_size") != degree
            or orbit_records[name].get("modular_distinct_value_count") != degree
            for name, degree in expected_orbits.items()
        )
        or span.get("orbit_span_dimension_over_M") != 3
        or span.get("all_three_components_nonzero") is not True
        or span.get("rational_character_idempotents_prove_independence") is not True
    ):
        _fail("G4 Fourier orbit/span reconstruction changed")
    group_p3 = _group_python(group)["P3_P6"]
    if (
        bridge.get("seed149") != 149
        or bridge.get("factor_degree") != 1920
        or bridge.get("Tmix_order") != 1296
        or bridge.get("Tmix_sha256")
        != "55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc"
        or bridge.get("Tmix_sha256") != bridge.get("Tplus_sha256")
        or bridge.get("exact_embedded_element_set_equality_Tmix_Tplus") is not True
        or bridge.get("order_hash_or_conjugacy_alone_used") is not False
        or bridge.get("unique_mixed_degree1920_row") is not True
        or group_p3.get("mixed_P6_join_sha256") != bridge.get("Tmix_sha256")
        or group_p3.get("P3_nonconjugate_to_P6") is not True
    ):
        _fail("G4 exact mixed type-3/Tplus bridge changed")
    if (
        diamond.get("degrees_A40_B80_M160_Fplus320") != [40, 80, 160, 320]
        or diamond.get("B80_intersection_M160_equals_A40") is not True
        or diamond.get("B80_compositum_M160_equals_Fplus320") is not True
        or diamond.get("all_four_normal_closures_equal_K") is not True
        or diamond.get("Gal_B80_over_A40_order") != 2
        or diamond.get("Aut_Q_A40_order") != 1
        or diamond.get("Aut_Q_B80_order") != 2
    ):
        _fail("G4 fixed-field diamond changed")
    return {
        "schema_id": "hcs-c61-g4-fourier-diamond-v1",
        "fourier_carrier_dag": deepcopy(fourier),
        "orbit_span_and_nonnormality": deepcopy(span),
        "fourier_orbit_records": deepcopy(orbit_records),
        "Splus_exact_stabilizer": deepcopy(stabilizers["Splus"]),
        "Tplus_exact_line_stabilizer": deepcopy(stabilizers["Tplus"]),
        "mixed_type3_exact_bridge": deepcopy(bridge),
        "fixed_field_diamond": deepcopy(diamond),
        "group_resolver_Tplus_complete_set_cross_bound": True,
        "status": "G4_PASS",
    }


def _group_arithmetic_rows(group: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = _strict_list(
        _group_python(group)["raw_global_local_inputs"]["field_type_rows"],
        "group arithmetic rows", length=26,
    )
    result = {row.get("type_label"): row for row in rows}
    if set(result) != {
        *(f"Q{index}" for index in range(1, 19)),
        *(f"P{index}" for index in range(1, 9)),
    }:
        _fail("group arithmetic type-row inventory changed")
    return result


def _cross_global_rows(
    group: dict[str, Any], resolver: dict[str, Any],
) -> dict[str, str]:
    group_rows = _group_arithmetic_rows(group)
    types = _group_python(group)["mixed_160_12_8"]["relative_position_types"]
    fields = resolver["GAF6_global_arithmetic"]["fields"]
    mapping: dict[str, str] = {}
    for index in range(1, 9):
        mapping[f"E{index}"] = types[index - 1]["Q_type"]
    for index in range(1, 5):
        mapping[f"C{index}"] = types[index - 1]["P_type"]
    for resolver_label, group_label in mapping.items():
        left = fields[resolver_label]
        right = group_rows[group_label]
        expected_sign = -1 if right["signature_r1_r2"][1] % 2 else 1
        if (
            left.get("degree") != right.get("degree")
            or left.get("signature_r1_r2") != right.get("signature_r1_r2")
            or left.get("discriminant_sign") != expected_sign
            or left.get("absolute_exponents_3_5_PiA_PiB")
            != right.get("conductor_exponents")
        ):
            _fail(f"group/resolver global arithmetic differs: {resolver_label}")
    return mapping


def _build_g5(group: dict[str, Any], resolver: dict[str, Any]) -> dict[str, Any]:
    global_evidence = resolver["GAF6_global_arithmetic"]
    mapping = _cross_global_rows(group, resolver)
    fields = global_evidence["fields"]
    expected_fields = {
        "E1": (640, [0, 320], 1, [1264, 992, 384, 320]),
        "E2": (960, [16, 472], 1, [1944, 1488, 624, 480]),
        "E3": (1920, [0, 960], 1, [3808, 2976, 1152, 960]),
        "E4": (2880, [16, 1432], 1, [5872, 4464, 1872, 1440]),
        "E5": (2880, [48, 1416], 1, [5856, 4464, 1872, 1440]),
        "E6": (8640, [48, 4296], 1, [17640, 13392, 5616, 4320]),
        "E7": (17280, [0, 8640], 1, [35504, 26784, 11520, 8640]),
        "E8": (51840, [0, 25920], 1, [106560, 80352, 34560, 25920]),
        "C1": (160, [16, 72], 1, [308, 248, 96, 80]),
        "C2": (40, [8, 16], 1, [68, 62, 18, 20]),
        "C3": (40, [6, 17], -1, [75, 61, 24, 15]),
        "C4": (1, [1, 0], 1, [0, 0, 0, 0]),
        "B80": (80, [4, 38], 1, [154, 122, 48, 30]),
    }
    if set(fields) != set(expected_fields):
        _fail("G5 global field inventory changed")
    for name, (degree, signature, sign, exponents) in expected_fields.items():
        row = fields[name]
        if (
            row.get("degree") != degree
            or row.get("signature_r1_r2") != signature
            or row.get("discriminant_sign") != sign
            or row.get("absolute_exponents_3_5_PiA_PiB") != exponents
        ):
            _fail(f"G5 global field tuple changed: {name}")
    expected_diamond = {
        "d_B80_over_A40": [4, 0, 0, 0],
        "d_M160_over_A40": [8, 4, 0, 20],
        "d_Fplus320_over_B80": [8, 8, 0, 40],
        "d_Fplus320_over_A40": [24, 8, 0, 40],
        "d_Fplus320_over_M160": [8, 0, 0, 0],
    }
    if (
        global_evidence.get("diamond_relative_discriminant_norm_vectors")
        != expected_diamond
        or global_evidence.get("diamond_route_via_B80") != [24, 8, 0, 40]
        or global_evidence.get("diamond_route_via_M160") != [24, 8, 0, 40]
        or global_evidence.get("field_discriminants_distinct_from_product_form_polynomial_and_order_discriminants") is not True
        or global_evidence.get("maximal_order_claimed") is not False
    ):
        _fail("G5 diamond relative discriminant reconstruction changed")
    return {
        "schema_id": "hcs-c61-g5-global-arithmetic-v1",
        "filtration_order": deepcopy(global_evidence["filtration_order"]),
        "filtration_tom_locators": deepcopy(global_evidence["filtration_tom_locators"]),
        "filtration_group_orders": deepcopy(global_evidence["filtration_group_orders"]),
        "prime_products": deepcopy(global_evidence["prime_products"]),
        "exact_ramified_support": deepcopy(global_evidence["exact_ramified_support"]),
        "fields": deepcopy(fields),
        "mixed_relative_discriminant_norm_vectors": deepcopy(
            global_evidence["mixed_relative_discriminant_norm_vectors"]
        ),
        "diamond_fields": deepcopy(global_evidence["diamond_fields"]),
        "diamond_relative_discriminant_norm_vectors": deepcopy(expected_diamond),
        "diamond_route_via_B80": deepcopy(global_evidence["diamond_route_via_B80"]),
        "diamond_route_via_M160": deepcopy(global_evidence["diamond_route_via_M160"]),
        "group_resolver_field_type_mapping": mapping,
        "all_group_resolver_global_rows_cross_bound": True,
        "field_discriminants_not_polynomial_or_order_discriminants": True,
        "maximal_order_claimed": False,
        "status": "G5_PASS",
    }


def _canonical_group_local_table(table: dict[str, Any]) -> dict[str, Any]:
    rows = [
        {
            "prime_index": index,
            "coset_seed": row["orbit_seed"],
            "row_n_e_f_d": [row["n"], row["e"], row["f"], row["d"]],
        }
        for index, row in enumerate(table["uncollected_rows"])
    ]
    return {
        "degree_total": table["degree_total"],
        "different_total": table["different_total"],
        "factor_count": table["factor_count"],
        "uncollected_prime_rows": rows,
        "collected_rows_with_multiplicity": [
            {
                "row_n_e_f_d": [row["n"], row["e"], row["f"], row["d"]],
                "multiplicity": row["multiplicity"],
            }
            for row in table["collected_rows"]
        ],
    }


def _build_g6(group: dict[str, Any], resolver: dict[str, Any]) -> dict[str, Any]:
    local = resolver["GAF7_both_local_branches_and_ideal_laws"]
    if local.get("retained_branches") != ["ToM140", "ToM206"] or local.get("branch_selected") is not False:
        _fail("G6 both-branch retention changed")
    mapping = _cross_global_rows(group, resolver)
    group_rows = _group_arithmetic_rows(group)
    absolute = local["absolute_local_tables"]
    if set(absolute) != {"ToM140", "ToM206"}:
        _fail("G6 absolute-local branch inventory changed")
    for branch, group_key in (("ToM140", "tom140"), ("ToM206", "tom206")):
        for resolver_label, group_label in mapping.items():
            observed = absolute[branch][resolver_label]
            expected = _canonical_group_local_table(group_rows[group_label][group_key])
            _deep_equal(observed, expected, f"G6 group/resolver {branch}/{resolver_label}")
    towers = local["V4_relative_towers_over_M"]
    expected_types = {
        "ToM140": {"Hplus": 8, "H3": 8, "trivial": 6, "H0": 0},
        "ToM206": {"Hplus": 4, "H3": 4, "trivial": 3, "H0": 0},
    }
    if set(towers) != set(expected_types):
        _fail("G6 V4 branch inventory changed")
    for branch, expected in expected_types.items():
        tower = towers[branch]
        if (
            tower.get("V4_type_counts") != expected
            or tower.get("residue_degree_masses")
            != {"Hplus": 8, "H3": 8, "trivial": 6, "H0": 0}
            or tower.get("relative_norm_exponents_Fplus_F0_F3_L")
            != [8, 16, 8, 32]
            or tower.get("all_rows_verify_ideal_laws") is not True
        ):
            _fail(f"G6 V4 branch summary changed: {branch}")
        for row in tower.get("uncollected_base_prime_rows", []):
            if not all(
                row.get(key) is True
                for key in (
                    "Fplus_F3_coprime", "F0_product_law", "L_square_law",
                    "conductor_discriminant_law",
                )
            ):
                _fail(f"G6 primewise ideal law changed: {branch}")
            for relative in row.get("relative_rows_g_e_f_d", {}).values():
                if relative[3] > 0 and (relative[1], relative[3]) != (2, 1):
                    _fail(f"G6 non-tame relative row appeared: {branch}")
    if (
        local.get("all_primewise_ideal_laws") is not True
        or local.get("all_ramified_relative_rows_tame_e2_d1") is not True
        or local.get("local_fields_classified_by_nefd_rows") is not False
        or local.get("archimedean_complementarity", {}).get("real_places_of_M") != 16
        or local.get("archimedean_complementarity", {}).get("V4_type_counts")
        != {"Hplus": 8, "H3": 8, "H0": 0}
    ):
        _fail("G6 ideal-law/infinite-place conclusion changed")
    absolute_commitments = {
        branch: _canonical_payload_sha256(absolute[branch])
        for branch in ("ToM140", "ToM206")
    }
    absolute_summaries = {
        branch: {
            field: {
                "degree_total": table["degree_total"],
                "different_total": table["different_total"],
                "factor_count": table["factor_count"],
                "collected_rows_with_multiplicity": deepcopy(
                    table["collected_rows_with_multiplicity"]
                ),
            }
            for field, table in absolute[branch].items()
        }
        for branch in ("ToM140", "ToM206")
    }
    return {
        "schema_id": "hcs-c61-g6-local-towers-v1",
        "retained_branches": ["ToM140", "ToM206"],
        "branch_selected": False,
        "absolute_local_table_commitments": absolute_commitments,
        "absolute_local_table_summaries": absolute_summaries,
        "all_absolute_uncollected_rows_validated_not_duplicated": True,
        "expected_factor_counts": deepcopy(local["expected_factor_counts"]),
        "V4_relative_towers_over_M": deepcopy(towers),
        "ideal_equalities": deepcopy(local["ideal_equalities"]),
        "all_primewise_ideal_laws": True,
        "all_ramified_relative_rows_tame_e2_d1": True,
        "archimedean_complementarity": deepcopy(local["archimedean_complementarity"]),
        "group_resolver_absolute_rows_cross_bound": True,
        "local_fields_classified_by_nefd_rows": False,
        "status": "G6_PASS",
    }


def _build_g7(
    group: dict[str, Any], resolver: dict[str, Any],
    *, group_replay_sha256: str, group_evidence_sha256: str,
    resolver_evidence_sha256: str,
) -> dict[str, Any]:
    group_lock, resolver_lock = _require_component_contracts()
    return {
        "schema_id": "hcs-c61-g7-independence-scope-release-v1",
        "group_component": {
            "evidence_sha256": group_evidence_sha256,
            "replay_sha256": group_replay_sha256,
            "component_contract": group_lock,
            "independence_contract": deepcopy(group["independence_contract"]),
            "backend_contract": deepcopy(group["backend_contract"]),
        },
        "fourier_resolvent_component": {
            "evidence_sha256": resolver_evidence_sha256,
            "payload_sha256": resolver["payload_sha256"],
            "component_contract": resolver_lock,
            "independence_contract": deepcopy(resolver["independence_contract"]),
        },
        "producer_imports_only_four_C61_modules": True,
        "producer_checker_shared_mathematical_helpers": False,
        "component_documents_fully_source_validated": True,
        "group_resolver_cross_bindings_reconstructed": True,
        "target_selection_or_unpromoted_aids_are_authority": False,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "payload_scalar_leaf_count": 0,
        "schema_scalar_leaf_count": 0,
        "evidence_rebound_mutation_count_expected": 10,
        "structural_mutation_count_expected": 14,
        "type_mutation_count_expected": 0,
        "value_mutation_count_expected": 0,
        "status": "G7_PASS",
    }


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(item) for item in value)
    if type(value) in {str, int, bool} or value is None:
        return 1
    _fail(f"unsupported payload leaf type: {type(value).__name__}")
    raise AssertionError("unreachable")


def schema_descriptor(payload: dict[str, Any]) -> dict[str, Any]:
    if type(payload) is not dict or tuple(payload) != PAYLOAD_KEYS:
        _fail("schema input does not have the exact ordered payload contract")
    return {
        "schema_id": SCHEMA_ID,
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
    _cross_component_authority_and_sources(
        source_contract_value, g0, group_evidence, resolver_evidence
    )
    group_lock, resolver_lock = _require_component_contracts()
    for value, expected, label in (
        (group_replay_sha256, group_lock["replay_sha256"], "group replay"),
        (group_evidence_sha256, group_lock["evidence_sha256"], "group evidence"),
        (
            resolver_evidence_sha256, resolver_lock["evidence_sha256"],
            "resolver evidence",
        ),
    ):
        _require_digest(value, f"{label} digest")
        if value != expected:
            _fail(f"{label} digest changed")
    if (
        _canonical_report_sha256(group_evidence) != group_evidence_sha256
        or _canonical_report_sha256(resolver_evidence)
        != resolver_evidence_sha256
        or resolver_evidence.get("payload_sha256")
        != resolver_lock["payload_sha256"]
    ):
        _fail("C61 top-level evidence rebound changed")

    artifact_contract_value = _require_keys(
        artifact_contract_value,
        {
            "artifact_count", "artifacts", "component_contracts",
            "immutable_inputs", "same_real_nonsymlink_parent", "schema_id",
            "source_owned_full_document_validation",
        },
        "artifact contract",
    )
    artifact_rows = _strict_list(
        artifact_contract_value["artifacts"], "artifact rows", length=2
    )
    sizes = {
        row.get("path"): row.get("size_bytes")
        for row in artifact_rows if type(row) is dict
    }
    expected_artifact_contract = _artifact_contract_from_documents(
        group_evidence,
        resolver_evidence,
        group_size_bytes=sizes.get("results/c61_group_evidence.json"),
        resolver_size_bytes=sizes.get("results/c61_resolvent_evidence.json"),
        validate_documents=False,
    )
    _deep_equal(
        artifact_contract_value, expected_artifact_contract,
        "full artifact contract",
    )

    backend_contract_value = _require_keys(
        backend_contract_value,
        {
            "gap", "math_python", "pari_dependency", "schema_id",
            "singular_dependency", "two_run_deterministic",
        },
        "backend contract",
    )
    expected_math = c61_pipeline.EXPECTED_BACKENDS["math"]
    math_backend = backend_contract_value["math_python"]
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
        != "hcs-c61-backend-contract-v1"
        or backend_contract_value["two_run_deterministic"] is not True
        or backend_contract_value["pari_dependency"] is not False
        or backend_contract_value["singular_dependency"] is not False
        or type(math_backend) is not dict
        or type(math_backend.get("resolved_executable")) is not str
        or not Path(math_backend["resolved_executable"]).is_absolute()
        or math_backend.get("executable_sha256")
        != expected_math["executable_sha256"]
        or math_backend.get("executable_size_bytes")
        != expected_math["executable_size_bytes"]
        or not c61_exact.deep_exact(math_backend.get("versions"), expected_versions)
        or not c61_exact.deep_exact(
            backend_contract_value["gap"], c61_pipeline.EXPECTED_GAP
        )
    ):
        _fail("C61 backend contract changed")

    g1 = _build_g1(group_evidence, resolver_evidence)
    g2 = _build_g2(group_evidence, resolver_evidence)
    g3 = _build_g3(group_evidence, resolver_evidence)
    g4 = _build_g4(group_evidence, resolver_evidence)
    g5 = _build_g5(group_evidence, resolver_evidence)
    g6 = _build_g6(group_evidence, resolver_evidence)
    g7 = _build_g7(
        group_evidence,
        resolver_evidence,
        group_replay_sha256=group_replay_sha256,
        group_evidence_sha256=group_evidence_sha256,
        resolver_evidence_sha256=resolver_evidence_sha256,
    )
    bridge_keys = WRITTEN_BRIDGE_KEYS
    if bridge_keys is None or len(bridge_keys) == 0 or len(set(bridge_keys)) != len(bridge_keys):
        _fail("C61 written-bridge contract is not frozen")
    payload: dict[str, Any] = {
        "artifact_contract": deepcopy(artifact_contract_value),
        "G0_released_authority_conventions_object": deepcopy(g0),
        "G1_three_tensor_products_burnside": g1,
        "G2_mixed_160_12_8_field_dictionary": g2,
        "G3_product_form_resolvents_primitivity": g3,
        "G4_fourier_kummer_type3_diamond": g4,
        "G5_complete_global_arithmetic": g5,
        "G6_both_local_branches_ideal_laws": g6,
        "G7_independence_sources_scope_release": g7,
        "written_bridges": {key: True for key in bridge_keys},
        "backend_contract": deepcopy(backend_contract_value),
        "source_contract": deepcopy(source_contract_value),
        "scope_nonclaims": {
            key: False for key in sorted(SCOPE_NONCLAIM_KEYS)
        },
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
            "semantic_firewall": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "selection_aids": "CHRONOLOGY_ONLY_NOT_THEOREM_AUTHORITY",
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
        _fail("payload does not have the exact ordered 15-key contract")
    if (
        len(payload["scope_nonclaims"]) != 30
        or any(type(flag) is not bool or flag for flag in payload["scope_nonclaims"].values())
    ):
        _fail("C61 exact 30-false scope firewall changed")
    if len(payload["written_bridges"]) != len(bridge_keys) or not all(
        value is True for value in payload["written_bridges"].values()
    ):
        _fail("C61 written-bridge truth contract changed")

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
    binding: StageBinding, command: Sequence[str], *, label: str,
) -> bytes:
    binding.assert_unchanged(f"before {label}")
    try:
        completed = subprocess.run(
            list(command), cwd=Path("/"), stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=c61_pipeline.clean_environment(), check=False, timeout=60,
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
    math_python: Path, gap_path: Path, binding: StageBinding,
) -> dict[str, Any]:
    math = c61_pipeline.executable(math_python, "FLINT/SymPy/NetworkX")
    gap = c61_pipeline.executable(gap_path, "GAP")
    math_raw, math_fp = _stable_bytes(math, max_bytes=40_000_000)
    gap_raw, gap_fp = _stable_bytes(gap, max_bytes=1_000_000)
    expected_math = c61_pipeline.EXPECTED_BACKENDS["math"]
    if (
        c61_exact.sha256_bytes(math_raw) != expected_math["executable_sha256"]
        or math_fp.size_bytes != expected_math["executable_size_bytes"]
        or c61_exact.sha256_bytes(gap_raw)
        != c61_pipeline.EXPECTED_GAP["executable_sha256"]
        or gap_fp.size_bytes != c61_pipeline.EXPECTED_GAP["executable_size_bytes"]
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
            binding, [str(math), "-s", "-B", "-c", python_source],
            label=f"math Python preflight run {index}",
        )
        for index in (1, 2)
    ]
    if python_runs[0] != python_runs[1]:
        _fail("math Python preflight is nondeterministic")
    python_value = c61_exact.strict_json_loads(
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
    if not c61_exact.deep_exact(python_value, expected_python):
        _fail("math Python versions changed")
    gap_source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",'
        'PackageInfo("ctbllib")[1].Version,"\\n");QUIT;'
    )
    gap_runs = [
        _run_stage_bound_child(
            binding, [str(gap), "-q", "-c", gap_source],
            label=f"GAP preflight run {index}",
        )
        for index in (1, 2)
    ]
    if gap_runs[0] != gap_runs[1]:
        _fail("GAP preflight is nondeterministic")
    try:
        fields = gap_runs[0].decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise c61_exact.StrictDataError("GAP preflight output is not ASCII") from exc
    observed_gap = {
        "resolved_executable": str(gap),
        "executable_sha256": c61_exact.sha256_bytes(gap_raw),
        "executable_size_bytes": gap_fp.size_bytes,
        "gap_version": fields[0] if len(fields) == 4 else "",
        "tomlib_version": fields[1] if len(fields) == 4 else "",
        "smallgrp_version": fields[2] if len(fields) == 4 else "",
        "ctbllib_version": fields[3] if len(fields) == 4 else "",
    }
    if not c61_exact.deep_exact(observed_gap, c61_pipeline.EXPECTED_GAP):
        _fail("GAP versions or executable identity changed")
    final_math_raw, final_math_fp = _stable_bytes(math, max_bytes=40_000_000)
    final_gap_raw, final_gap_fp = _stable_bytes(gap, max_bytes=1_000_000)
    if (
        final_math_raw != math_raw or final_math_fp != math_fp
        or final_gap_raw != gap_raw or final_gap_fp != gap_fp
    ):
        _fail("backend executable changed during deterministic preflight")
    binding.assert_unchanged("at backend-contract return")
    return {
        "schema_id": "hcs-c61-backend-contract-v1",
        "math_python": {
            "resolved_executable": str(math),
            "executable_sha256": c61_exact.sha256_bytes(math_raw),
            "executable_size_bytes": math_fp.size_bytes,
            "versions": python_value,
        },
        "gap": observed_gap,
        "two_run_deterministic": True,
        "pari_dependency": False,
        "singular_dependency": False,
    }


def assemble_payload(
    artifact_dir: Path, math_python: Path, gap: Path,
) -> dict[str, Any]:
    """Rebind live authority/evidence and call the path-free payload builder."""

    namespace = argparse.Namespace(
        artifact_dir=Path(artifact_dir),
        output=Path(artifact_dir) / "c61_certificate.json",
        schema_output=Path(artifact_dir) / "c61_schema.json",
    )
    binding = validate_fixed_paths(namespace)
    source_before = source_contract()
    g0, written = rebuild_g0()
    if WRITTEN_BRIDGE_KEYS is None or written != {
        key: True for key in WRITTEN_BRIDGE_KEYS
    }:
        _fail("C61 written-bridge lock is not frozen")
    artifacts, group, resolver = artifact_contract(
        binding.parent, validate_documents=False
    )
    backends = _backend_contract(Path(math_python), Path(gap), binding)
    group_replay_sha256 = _group_replay_digest(group)
    payload = build_payload(
        source_before, g0, artifacts, group, resolver, backends,
        group_replay_sha256, binding.group_seal.sha256,
        binding.resolver_seal.sha256,
    )
    binding.assert_unchanged("after payload assembly")
    final_source = source_contract()
    final_g0, final_written = rebuild_g0()
    final_artifacts, final_group, final_resolver = artifact_contract(
        binding.parent, validate_documents=False
    )
    final_backends = _backend_contract(Path(math_python), Path(gap), binding)
    if (
        not c61_exact.deep_exact(source_before, final_source)
        or not c61_exact.deep_exact(g0, final_g0)
        or written != final_written
        or not c61_exact.deep_exact(artifacts, final_artifacts)
        or not c61_exact.deep_exact(group, final_group)
        or not c61_exact.deep_exact(resolver, final_resolver)
        or not c61_exact.deep_exact(backends, final_backends)
    ):
        _fail(
            "source, formal authority, evidence, or backends changed during assembly"
        )
    binding.assert_unchanged("at payload assembly return")
    return payload


def _group_replay_digest(group_evidence: dict[str, Any]) -> str:
    component_hashes = _require_keys(
        group_evidence["component_hashes"],
        {
            "python_projection_sha256", "gap_projection_sha256",
            "subgroup_registry_sha256", "all_36_tensor_rows_sha256",
            "mixed_160_position_sha256", "raw_global_local_input_sha256",
        },
        "group component hashes",
    )
    replay = _require_digest(
        component_hashes["gap_projection_sha256"],
        "group independent GAP projection digest",
    )
    if GROUP_COMPONENT is None or replay != GROUP_COMPONENT["replay_sha256"]:
        _fail("group independent GAP projection digest changed")
    return replay


def _assert_payload_authority_rebound(
    payload: dict[str, Any], binding: StageBinding,
    math_python: Path, gap: Path, label: str,
) -> None:
    if (
        not c61_exact.deep_exact(payload["source_contract"], source_contract())
        or not c61_exact.deep_exact(
            payload["G0_released_authority_conventions_object"], rebuild_g0()[0]
        )
        or not c61_exact.deep_exact(
            payload["artifact_contract"],
            artifact_contract(binding.parent, validate_documents=False)[0],
        )
        or not c61_exact.deep_exact(
            payload["backend_contract"],
            _backend_contract(Path(math_python), Path(gap), binding),
        )
    ):
        _fail(f"producer authority changed {label}")
    binding.assert_unchanged(label)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-output", type=Path, required=True)
    parser.add_argument("--math-python", type=Path, required=True)
    parser.add_argument("--gap", type=Path, required=True)
    arguments = parser.parse_args()
    c61_exact.reject_optimized_python()
    binding = validate_fixed_paths(arguments)
    source_contract()
    payload = assemble_payload(
        binding.parent, arguments.math_python, arguments.gap,
    )
    schema = schema_descriptor(payload)
    certificate = {
        "schema": deepcopy(schema),
        "schema_sha256": c61_exact.sha256_bytes(
            c61_exact.canonical_leaf_bytes(schema)
        ),
        "payload": payload,
        "payload_sha256": c61_exact.sha256_bytes(
            c61_exact.canonical_leaf_bytes(payload)
        ),
    }
    schema_raw = c61_exact.canonical_json_bytes(schema, pretty=True)
    certificate_raw = c61_exact.canonical_json_bytes(certificate, pretty=True)
    if len(schema_raw) > 200_000 or len(certificate_raw) > MAX_CERTIFICATE_BYTES:
        _fail("generated schema or certificate exceeds its byte ceiling")
    binding.assert_unchanged("before final producer rebound")
    _assert_payload_authority_rebound(
        payload, binding, arguments.math_python, arguments.gap,
        "before certificate/schema write",
    )
    binding.assert_unchanged("immediately before output preparation")
    outputs = c61_exact.prepare_output_targets(
        (binding.output, binding.schema_output),
        protected=(binding.group_evidence, binding.resolvent_evidence),
    )
    try:
        c61_exact.atomic_write(outputs[1], schema_raw)
        c61_exact.atomic_write(outputs[0], certificate_raw)
        binding.assert_unchanged("after certificate/schema write")
        _assert_payload_authority_rebound(
            payload, binding, arguments.math_python, arguments.gap,
            "after certificate/schema write",
        )
        observed_schema, schema_seal = _stable_bytes(
            outputs[1], max_bytes=200_000
        )
        observed_certificate, certificate_seal = _stable_bytes(
            outputs[0], max_bytes=MAX_CERTIFICATE_BYTES
        )
        if (
            observed_schema != schema_raw
            or observed_certificate != certificate_raw
            or stat.S_IMODE(schema_seal.mode) != 0o644
            or stat.S_IMODE(certificate_seal.mode) != 0o644
            or schema_seal.links != 1
            or certificate_seal.links != 1
        ):
            _fail("written certificate/schema bytes or metadata changed")
        binding.assert_unchanged("at producer success")
    except BaseException:
        for output in outputs:
            if output.exists() and output.is_file() and not output.is_symlink():
                output.unlink()
        raise
    print("C61 PRODUCER PASS PREFREEZE")
    print(f"payload_scalar_leaves={scalar_leaf_count(payload)}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    print(f"certificate_sha256={hashlib.sha256(certificate_raw).hexdigest()}")


if __name__ == "__main__":
    main()
