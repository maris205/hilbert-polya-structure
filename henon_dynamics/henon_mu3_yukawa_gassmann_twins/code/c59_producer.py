#!/usr/bin/env python3
"""Assemble the strict HCS-C59 PREFREEZE certificate.

The two mathematical evidence carriers are immutable inputs.  This module
rebinds the exact released predecessors, formal target, source inventory,
backends, and evidence before and after assembly.  It deliberately contains
no table-of-marks transport and no primitive-resolvent implementation.
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

import c59_exact
import c59_group
import c59_pipeline
import c59_resolvent


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
if CODE.name == "code" and PROJECT.name == "henon_mu3_yukawa_gassmann_twins":
    REPO = PROJECT.parents[1]
else:
    # A staged source may be imported for pure fixture tests, but repository
    # assembly must fail closed until the source occupies its canonical path.
    REPO = Path("/__C59_STAGED_SOURCE_HAS_NO_REPOSITORY_AUTHORITY__")
    PROJECT = REPO / "henon_dynamics/henon_mu3_yukawa_gassmann_twins"
    CODE = PROJECT / "code"
RESULTS = PROJECT / "results"
BATCH = REPO / "henon_dynamics/BATCH_PLAN_C57_C61.md"
GUARD = REPO / "henon_dynamics/codex_prompt.md"
ROUTE = PROJECT / "route_a_evaluation.yaml"

CODE_FILES = (
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
)
RESULT_FILES = (
    "RESULTS.md",
    "TEST_REPORT.md",
    "c59_certificate.json",
    "c59_check_report.json",
    "c59_group_evidence.json",
    "c59_resolvent_evidence.json",
    "c59_schema.json",
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
    "c59_group_evidence.json",
    "c59_resolvent_evidence.json",
)
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
SCOPE_NONCLAIM_KEYS = (
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
)
WRITTEN_BRIDGE_KEYS = (
    "integral_scaling_and_orbit_product",
    "graph_labelling_and_transported_subgroups",
    "modular_noncollision_to_fixed_field",
    "core_normal_closure_nonisomorphism_and_artin_formalism",
    "permutation_conductor_to_signed_field_discriminant",
    "double_cosets_to_local_completion_rows_and_degree_separator",
)

# Frozen only after the independent C59 formal-hostile pass.  These are
# authority expectations, not payload-selected paths or pending sentinels.
FORMAL_PACKAGE_SHA256 = "19f3e829b69816758af132bc5e2c4a478c838e312f99a74390a1d26724cba30f"
ROUTE_SHA256 = "81f6b6c95b269e10b4d0d3f83589cc310bb2eaef4130df314c4946fa254886a7"
BATCH_SHA256 = "d78acbe23fe99c8801ac8e90ec75d691a65dc1baf949713e00cc417260382d12"
GUARD_SHA256 = "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead"

PREDECESSORS = {
    "C56": {
        "project": REPO / "henon_dynamics/henon_mu3_yukawa_line_field",
        "release_commit": "a55f31dca338d1e3757704b8c95d11e28c9c98d4",
        "manifest_sha256": "26e3e4226cd1baea14543f14bac9ffd060ed8031741cb1ec0a38e22cd07487f4",
        "manifest_entry_count": 46,
        "certificate_sha256": "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4",
        "payload_sha256": "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661",
        "schema_sha256": "adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504",
        "check_sha256": "4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9",
        "scoped_sha256": "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a",
        "route_sha256": "cc17a14a3565165de2249bc5219f209b6546ffd91b583e75ac07bbba7730ca73",
        "archive": "evaluations/route_a/HCS-C56/20260815T000000Z.yaml",
        "certificate": "results/c56_certificate.json",
        "schema": "results/c56_schema.json",
        "check_report": "results/c56_check_report.json",
        "scoped_manifest": "results/scoped_hash_manifest.json",
        "code_commit": "a55f31dca338d1e3757704b8c95d11e28c9c98d4",
    },
    "C58": {
        "project": REPO / "henon_dynamics/henon_mu3_yukawa_line_ramification",
        "release_commit": "184b9a8a91234a5d793d5deaa3b652ed56a524bd",
        "manifest_sha256": "06b7c24190d532d6c543b93f74a65d650265988734f340bbb8896953e34d3cb0",
        "manifest_entry_count": 56,
        "certificate_sha256": "456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee",
        "payload_sha256": "fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f",
        "schema_sha256": "ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a",
        "check_sha256": "64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9",
        "scoped_sha256": "a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730",
        "route_sha256": "4300ea23d084a2e16a0b37e63df3311e692d58efd2750ba4e204f0602e8225fd",
        "group_evidence_sha256": "0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd",
        "archive": "evaluations/route_a/HCS-C58/20260816T000000Z.yaml",
        "certificate": "results/c58_certificate.json",
        "schema": "results/c58_schema.json",
        "check_report": "results/c58_check_report.json",
        "scoped_manifest": "results/scoped_hash_manifest.json",
        "code_commit": "184b9a8a91234a5d793d5deaa3b652ed56a524bd",
    },
}

SCHEMA_ID = "hcs-c59-certificate-schema-v1"
MAX_CERTIFICATE_BYTES = 5_000_000
MAX_JSON_BYTES = 20_000_000
MANIFEST_PATTERN = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")
STAGE_NAME_PATTERN = re.compile(r"^\.c59-stage-[A-Za-z0-9]{8}$")

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


def _fail(message: str) -> None:
    raise c59_exact.StrictDataError(message)


def _require_digest(value: Any, label: str) -> str:
    return c59_exact.require_sha256(value, label)


def _require_keys(value: Any, expected: Iterable[str], label: str) -> dict[str, Any]:
    return c59_exact.require_exact_keys(value, set(expected), label)


def _canonical_payload_sha256(value: Any) -> str:
    return c59_exact.sha256_bytes(c59_exact.canonical_leaf_bytes(value))


def _canonical_report_sha256(value: Any) -> str:
    return c59_exact.sha256_bytes(c59_exact.canonical_json_bytes(value))


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


def _read_json(path: Path, *, max_bytes: int, canonical_pretty: bool) -> tuple[dict[str, Any], bytes, c59_exact.Fingerprint]:
    raw, fingerprint = c59_exact.read_stable(path, max_bytes=max_bytes)
    value = c59_exact.strict_json_loads(raw, max_bytes=max_bytes)
    if type(value) is not dict:
        _fail(f"JSON root must be an object: {path}")
    expected = c59_exact.canonical_json_bytes(value, pretty=canonical_pretty)
    if raw != expected:
        _fail(f"JSON bytes are not canonical: {path}")
    return value, raw, fingerprint


def _parse_sha256_manifest(raw: bytes, label: str) -> dict[str, str]:
    try:
        lines = raw.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise c59_exact.StrictDataError(f"{label} manifest is not UTF-8") from exc
    entries: dict[str, str] = {}
    for line in lines:
        match = MANIFEST_PATTERN.fullmatch(line)
        if match is None:
            _fail(f"{label} manifest row is malformed")
        digest, relative = match.groups()
        if not c59_exact.safe_relative_path(relative) or relative in entries:
            _fail(f"{label} manifest contains an unsafe/duplicate path")
        entries[relative] = digest
    if not entries or list(entries) != sorted(entries):
        _fail(f"{label} manifest must be nonempty and path-sorted")
    return entries


def _git_ancestor(commit: str) -> bool:
    result = subprocess.run(
        ["/usr/bin/git", "merge-base", "--is-ancestor", commit, "HEAD"],
        cwd=REPO,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=c59_pipeline.clean_environment(),
        check=False,
        timeout=60,
    )
    if result.stdout or result.stderr:
        _fail("git ancestry check emitted output")
    return result.returncode == 0


def source_contract() -> dict[str, Any]:
    code = _regular_directory(CODE, "C59 code directory")
    children = list(code.iterdir())
    if any(path.is_symlink() or not path.is_file() for path in children):
        _fail("C59 code inventory contains a non-regular entry")
    observed = {path.name for path in children}
    expected = set(CODE_FILES)
    if len(observed) != len(children) or observed != expected:
        _fail(
            f"C59 code inventory mismatch; missing={sorted(expected-observed)}; "
            f"extra={sorted(observed-expected)}"
        )
    entries = []
    for name in CODE_FILES:
        raw, fingerprint = c59_exact.read_stable(code / name, max_bytes=3_000_000)
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": len(raw),
            }
        )
    return {
        "entries": entries,
        "entry_count": 13,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [f"code/{name}" for name in sorted(CODE_FILES)],
        "schema_id": "hcs-c59-source-contract-v1",
        "self_reference_policy": "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE",
    }


def _released_object_projection(label: str, payload: dict[str, Any]) -> dict[str, Any]:
    if label == "C56":
        try:
            eliminant = payload["irreducibility"]["eliminant_coefficients_d_0_to_27"]
            chart = payload["grassmann_main_chart"]
            weyl = payload["we6"]
        except (KeyError, TypeError) as exc:
            raise c59_exact.StrictDataError("C56 exact line carrier is missing") from exc
        if (
            type(eliminant) is not list
            or len(eliminant) != 28
            or type(chart.get("lex_shape")) is not list
            or len(chart["lex_shape"]) != 4
            or type(chart.get("line_equations_sparse")) is not list
            or len(chart["line_equations_sparse"]) != 4
            or type(weyl.get("line_class_intersection_matrix")) is not list
            or len(weyl["line_class_intersection_matrix"]) != 27
            or type(weyl.get("simple_reflection_line_permutations")) is not list
            or len(weyl["simple_reflection_line_permutations"]) != 6
        ):
            _fail("C56 exact line-carrier shape changed")
        return {
            "eliminant_coefficients_sha256": _canonical_payload_sha256(eliminant),
            "eliminant_degree": 27,
            "lex_shape_sha256": _canonical_payload_sha256(chart["lex_shape"]),
            "line_equations_sparse_sha256": _canonical_payload_sha256(
                chart["line_equations_sparse"]
            ),
            "line_incidence_matrix_sha256": _canonical_payload_sha256(
                weyl["line_class_intersection_matrix"]
            ),
            "line_weyl_generators_sha256": _canonical_payload_sha256(
                weyl["simple_reflection_line_permutations"]
            ),
        }
    if label == "C58":
        try:
            dual = payload["G3_dual_action_classification"]
            filtration = payload["G4_filtered_inertia"]
            global_data = payload["G6_global_and_infinity"]
        except (KeyError, TypeError) as exc:
            raise c59_exact.StrictDataError("C58 filtered-local carrier is missing") from exc
        expected_p3_pairs = [
            [140, 140, 1],
            [142, 142, 1],
            [206, 140, 2],
            [206, 142, 2],
        ]
        if (
            dual.get("p3_valid_decomposition_inertia_pairs") != expected_p3_pairs
            or filtration.get("p3", {}).get("inertia_tom_index") != 140
            or filtration.get("p3", {}).get("serre_required_action") != "inversion"
            or filtration.get("p3", {}).get("filtered_orders")
            != [18, 9, 3, 3, 3, 3, 3, 3, 1]
            or filtration.get("p5", {}).get("filtered_orders") != [20, 5, 5, 5, 1]
            or filtration.get("tame_C3", {}).get("filtered_orders") != [3, 1]
            or filtration.get("reflection", {}).get("filtered_orders") != [2, 1]
            or global_data.get("normal_closure_ramified_support")
            != [
                3,
                5,
                181,
                283,
                997,
                1801,
                2346241,
                14932047182473291995860108491583652133938007263719,
            ]
        ):
            _fail("C58 filtered-local semantic projection changed")
        return {
            "exact_eight_prime_support": global_data["normal_closure_ramified_support"],
            "filtered_local_carrier_sha256": _canonical_payload_sha256(filtration),
            "p3_permitted_decomposition_inertia_tom_pairs": [[140, 140], [206, 140]],
            "p3_filtered_orders": filtration["p3"]["filtered_orders"],
            "p5_filtered_orders": filtration["p5"]["filtered_orders"],
            "reflection_filtered_orders": filtration["reflection"]["filtered_orders"],
            "tame_C3_filtered_orders": filtration["tame_C3"]["filtered_orders"],
        }
    _fail("unknown released predecessor projection")


def _validate_released_certificate(
    label: str,
    certificate: dict[str, Any],
    schema: dict[str, Any],
    schema_raw: bytes,
    check_report: dict[str, Any],
    scoped_manifest: dict[str, Any],
) -> tuple[str, str, str]:
    if label == "C56":
        _require_keys(
            certificate,
            {"schema", "schema_sha256", "payload", "payload_sha256"},
            "C56 certificate",
        )
        if not c59_exact.deep_exact(certificate["schema"], schema):
            _fail("C56 embedded/separate schema objects differ")
        if certificate["schema_sha256"] != _canonical_payload_sha256(schema):
            _fail("C56 canonical schema digest failed")
        payload = certificate["payload"]
        if certificate["payload_sha256"] != _canonical_payload_sha256(payload):
            _fail("C56 payload digest failed")
        status = payload.get("theorem_gates", {}).get("final_status")
        if status != "PREFREEZE_CODE_RESULTS_PASS":
            _fail("C56 certificate semantic status changed")
        if (
            check_report.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
            or check_report.get("payload_sha256") != certificate["payload_sha256"]
            or check_report.get("schema_sha256") != certificate["schema_sha256"]
        ):
            _fail("C56 independent check binding failed")
    elif label == "C58":
        _require_keys(
            certificate,
            {
                "canonical_schema_sha256",
                "paper_status",
                "payload",
                "payload_sha256",
                "schema_descriptor_id",
                "schema_id",
                "schema_sha256",
                "status",
            },
            "C58 certificate",
        )
        payload = certificate["payload"]
        if certificate["payload_sha256"] != _canonical_payload_sha256(payload):
            _fail("C58 payload digest failed")
        if (
            certificate["schema_sha256"] != c59_exact.sha256_bytes(schema_raw)
            or certificate["canonical_schema_sha256"] != _canonical_payload_sha256(schema)
            or certificate["status"] != "PREFREEZE_CODE_RESULTS_PASS"
        ):
            _fail("C58 schema/status binding failed")
        status = certificate["status"]
        if (
            check_report.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
            or check_report.get("payload_sha256") != certificate["payload_sha256"]
            or check_report.get("full_semantic_leaf_rebuild") is not True
        ):
            _fail("C58 independent check binding failed")
    else:
        _fail("unknown released certificate")
    if (
        scoped_manifest.get("status") != "PREFREEZE_CODE_RESULTS_PASS"
        or scoped_manifest.get("manifest_self_included") is not False
    ):
        _fail(f"{label} scoped manifest status/self-exclusion changed")
    return certificate["payload_sha256"], status, check_report["result"]


def _bind_released_predecessor(label: str, contract: dict[str, Any]) -> dict[str, Any]:
    project = _regular_directory(contract["project"], f"{label} project")
    manifest_path = project / "FULL_PROJECT_HASHES.sha256"
    manifest_raw, manifest_fingerprint = c59_exact.read_stable(
        manifest_path, max_bytes=2_000_000
    )
    if manifest_fingerprint.sha256 != contract["manifest_sha256"]:
        _fail(f"{label} release-manifest digest changed")
    manifest = _parse_sha256_manifest(manifest_raw, label)
    if len(manifest) != contract["manifest_entry_count"]:
        _fail(f"{label} release-manifest count changed")

    inventory_entries = []
    for relative, digest in manifest.items():
        raw, fingerprint = c59_exact.read_stable(
            project / relative, max_bytes=210_000_000
        )
        if fingerprint.sha256 != digest:
            _fail(f"{label} released leaf changed: {relative}")
        inventory_entries.append(
            {"path": relative, "sha256": digest, "size_bytes": len(raw)}
        )

    manifest_relative = "FULL_PROJECT_HASHES.sha256"
    declared_paths = set(manifest)
    observed_paths: set[str] = set()
    observed_directories: set[str] = set()
    for path in project.rglob("*"):
        relative = path.relative_to(project).as_posix()
        if path.is_symlink():
            _fail(f"{label} released tree contains a symlink")
        if path.is_file():
            if relative != manifest_relative:
                observed_paths.add(relative)
        elif path.is_dir():
            observed_directories.add(relative)
        else:
            _fail(f"{label} released tree contains a special object")
    allowed_directories: set[str] = set()
    for relative in declared_paths | {manifest_relative}:
        for parent in PurePosixPath(relative).parents:
            if parent.as_posix() != ".":
                allowed_directories.add(parent.as_posix())
    if declared_paths != observed_paths or allowed_directories != observed_directories:
        _fail(f"{label} full released live inventory is not exact")

    route_raw, route_fingerprint = c59_exact.read_stable(
        project / "route_a_evaluation.yaml", max_bytes=1_000_000
    )
    archive_raw, archive_fingerprint = c59_exact.read_stable(
        project / contract["archive"], max_bytes=1_000_000
    )
    if route_raw != archive_raw:
        _fail(f"{label} live/archive Route bytes differ")
    route_text = route_raw.decode("utf-8", errors="strict")
    for token in (
        "release_status: RELEASE_FROZEN",
        "code_results_status: PREFREEZE_CODE_RESULTS_PASS",
    ):
        if token not in route_text:
            _fail(f"{label} released Route status token missing: {token}")

    certificate, certificate_raw, certificate_fingerprint = _read_json(
        project / contract["certificate"],
        max_bytes=MAX_JSON_BYTES,
        canonical_pretty=True,
    )
    schema, schema_raw, schema_fingerprint = _read_json(
        project / contract["schema"], max_bytes=1_000_000, canonical_pretty=True
    )
    check_report, check_raw, check_fingerprint = _read_json(
        project / contract["check_report"],
        max_bytes=2_000_000,
        canonical_pretty=True,
    )
    scoped, scoped_raw, scoped_fingerprint = _read_json(
        project / contract["scoped_manifest"],
        max_bytes=2_000_000,
        canonical_pretty=True,
    )
    payload_sha256, semantic_status, check_result = _validate_released_certificate(
        label, certificate, schema, schema_raw, check_report, scoped
    )
    special_paths = {
        "route_a_evaluation.yaml": route_fingerprint.sha256,
        contract["archive"]: archive_fingerprint.sha256,
        contract["certificate"]: certificate_fingerprint.sha256,
        contract["schema"]: schema_fingerprint.sha256,
        contract["check_report"]: check_fingerprint.sha256,
        contract["scoped_manifest"]: scoped_fingerprint.sha256,
    }
    if any(manifest.get(path) != digest for path, digest in special_paths.items()):
        _fail(f"{label} release manifest does not bind a required object")
    if not _git_ancestor(contract["code_commit"]):
        _fail(f"{label} implementation commit is not an ancestor of HEAD")
    return {
        "certificate_payload_sha256": payload_sha256,
        "certificate_semantic_status": semantic_status,
        "certificate_sha256": certificate_fingerprint.sha256,
        "certificate_size_bytes": len(certificate_raw),
        "check_report_result": check_result,
        "check_report_sha256": check_fingerprint.sha256,
        "check_report_size_bytes": len(check_raw),
        "full_inventory_entries": inventory_entries,
        "full_inventory_entry_count": len(inventory_entries),
        "full_inventory_exact_live_rebind": True,
        "full_inventory_sha256": manifest_fingerprint.sha256,
        "full_inventory_size_bytes": len(manifest_raw),
        "implementation_commit": contract["code_commit"],
        "implementation_commit_is_ancestor_of_HEAD": True,
        "released_object_projection": _released_object_projection(
            label, certificate["payload"]
        ),
        "route_archive_path": contract["archive"],
        "route_archive_sha256": archive_fingerprint.sha256,
        "route_archive_size_bytes": len(archive_raw),
        "route_live_archive_byte_identical": True,
        "route_sha256": route_fingerprint.sha256,
        "route_size_bytes": len(route_raw),
        "schema_file_sha256": schema_fingerprint.sha256,
        "schema_file_size_bytes": len(schema_raw),
        "scoped_manifest_sha256": scoped_fingerprint.sha256,
        "scoped_manifest_size_bytes": len(scoped_raw),
    }


def released_predecessors() -> dict[str, Any]:
    return {
        label: _bind_released_predecessor(label, PREDECESSORS[label])
        for label in ("C56", "C58")
    }


def _file_binding(path: Path, expected_sha256: str, label: str) -> tuple[dict[str, Any], bytes]:
    raw, fingerprint = c59_exact.read_stable(path, max_bytes=5_000_000)
    if fingerprint.sha256 != expected_sha256:
        _fail(f"{label} digest changed")
    return {
        "path": path.relative_to(REPO).as_posix(),
        "sha256": fingerprint.sha256,
        "size_bytes": len(raw),
    }, raw


def _formal_aggregate() -> tuple[dict[str, Any], dict[str, bytes]]:
    observed = {
        path.name
        for path in PROJECT.iterdir()
        if path.is_file() and path.suffix == ".md"
    }
    if observed != set(FORMAL_FILES):
        _fail(
            f"formal Markdown inventory mismatch; missing={sorted(set(FORMAL_FILES)-observed)}; "
            f"extra={sorted(observed-set(FORMAL_FILES))}"
        )
    entries = []
    raw_by_name: dict[str, bytes] = {}
    aggregate_rows = bytearray()
    for name in sorted(FORMAL_FILES):
        raw, fingerprint = c59_exact.read_stable(
            PROJECT / name, max_bytes=2_000_000
        )
        raw_by_name[name] = raw
        entries.append(
            {"path": name, "sha256": fingerprint.sha256, "size_bytes": len(raw)}
        )
        aggregate_rows.extend(f"{fingerprint.sha256}  {name}\n".encode("ascii"))
    aggregate = c59_exact.sha256_bytes(bytes(aggregate_rows))
    if aggregate != FORMAL_PACKAGE_SHA256:
        _fail("C59 formal-package aggregate changed")
    return {
        "aggregate_sha256": aggregate,
        "aggregate_definition": (
            "SHA256_OF_LEXICOGRAPHICALLY_BASENAME_ORDERED_SHA256SUM_LINES_FOR_EXACT_13_ROOT_MARKDOWN_FILES_ROUTE_EXCLUDED"
        ),
        "entries": entries,
        "entry_count": 13,
        "exact_formal_inventory": True,
        "formal_hostile_status": "FORMAL_HOSTILE_PASS",
    }, raw_by_name


def written_bridges_from_formal(raw_by_name: dict[str, bytes]) -> dict[str, bool]:
    proof = raw_by_name["PROOF_PACKAGE.md"].decode("utf-8", errors="strict")
    required_sections = {
        "integral_scaling_and_orbit_product": (
            "## 2. Integrality of the scaled roots and orbit sums",
            "The orbit product is therefore the monic integral irreducible separable",
        ),
        "graph_labelling_and_transported_subgroups": (
            "## 4. Graph-labelling lemma",
            "transports\n$H_\\pm$ with the relabelling",
        ),
        "modular_noncollision_to_fixed_field": (
            "## 3. Stabilizer and primitive-element lemma",
            "The distinct reductions therefore\nprove 320 distinct characteristic-zero conjugates",
        ),
        "core_normal_closure_nonisomorphism_and_artin_formalism": (
            "## 6. Common normal closure and field nonisomorphism",
            "## 7. Equality of Dedekind zeta functions",
        ),
        "permutation_conductor_to_signed_field_discriminant": (
            "## 9. Conductor-discriminant calculation",
            "exact signed identity",
        ),
        "double_cosets_to_local_completion_rows_and_degree_separator": (
            "## 10. Double-coset/local-completion lemma",
            "## 11. Branch-independent local separation",
        ),
    }
    result = {}
    for key in WRITTEN_BRIDGE_KEYS:
        tokens = required_sections[key]
        result[key] = all(token in proof for token in tokens)
    if not all(result.values()):
        _fail("one or more required written bridges is absent")
    return result


def formal_authority() -> tuple[dict[str, Any], dict[str, bool]]:
    formal, raw_by_name = _formal_aggregate()
    route_binding, route_raw = _file_binding(ROUTE, ROUTE_SHA256, "C59 Route")
    batch_binding, batch_raw = _file_binding(BATCH, BATCH_SHA256, "Batch target lock")
    guard_binding, _ = _file_binding(GUARD, GUARD_SHA256, "protected guard")
    route_text = route_raw.decode("utf-8", errors="strict")
    route_formal_match = re.search(
        r'(?m)^  formal_package: "([0-9a-f]{64})"$', route_text
    )
    if route_formal_match is None or route_formal_match.group(1) != FORMAL_PACKAGE_SHA256:
        _fail("C59 Route does not bind the exact formal aggregate")
    for token in (
        "candidate_id: HCS-C59",
        "formal_root_hostile_audit_status: FORMAL_HOSTILE_PASS",
        "code_results_status: IMPLEMENTATION_PENDING",
        "promotion_authorized: false",
        "NO_BAD_EULER_OR_ROOT_NUMBER",
        "planned_code_files: 13",
        "planned_result_files: 8",
        "planned_scope_nonclaim_leaves: 30",
    ):
        if token not in route_text:
            _fail(f"C59 Route target-lock token missing: {token}")
    batch_text = batch_raw.decode("utf-8", errors="strict")
    for token in (
        "## HCS-C59: primitive Gassmann twins from the 27 lines",
        "TARGET_LOCK_GO",
        "FORMAL_HOSTILE_PASS",
        "NO_BAD_EULER_OR_ROOT_NUMBER",
    ):
        if token not in batch_text:
            _fail(f"Batch C59 target-lock token missing: {token}")
    source_audit = raw_by_name["SOURCE_AUDIT.md"].decode("utf-8", errors="strict")
    for credited_name in (
        "James",
        "Perlis",
        "Bosma",
        "McReynolds",
        "Mantilla-Soler",
        "Komatsu",
        "Stauduhar",
        "Klueners",
    ):
        if credited_name not in source_audit:
            _fail(f"source ledger is missing required attribution: {credited_name}")
    formal["route_binding"] = route_binding
    formal["route_declared_aggregate_matches"] = True
    return {
        "all_released_full_inventories_rebound": True,
        "batch_target_lock": batch_binding,
        "fixed_predecessor_paths_only": True,
        "formal_target_lock": formal,
        "protected_guard": guard_binding,
        "released_predecessors": released_predecessors(),
        "schema_id": "hcs-c59-released-authority-rebind-v1",
    }, written_bridges_from_formal(raw_by_name)


def artifact_contract(artifact_dir: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    directory = _regular_directory(artifact_dir, "C59 evidence directory")
    if (
        not STAGE_NAME_PATTERN.fullmatch(directory.name)
        or directory.parent != RESULTS.resolve(strict=True)
    ):
        _fail("evidence directory is not the canonical direct-child C59 runner stage")
    paths = [directory / name for name in ARTIFACT_NAMES]
    if any(path.name != name for path, name in zip(paths, ARTIFACT_NAMES)):
        _fail("evidence basenames changed")
    if any(path.parent.resolve(strict=True) != directory for path in paths):
        _fail("evidence files do not share one real parent")

    group, group_raw, group_fingerprint = _read_json(
        paths[0], max_bytes=2_000_000, canonical_pretty=False
    )
    try:
        c59_group.validate_evidence(group)
    except Exception as exc:
        raise c59_exact.StrictDataError("group evidence validation failed") from exc
    if group.get("schema_id") != c59_group.SCHEMA_ID:
        _fail("group evidence schema id changed")

    resolvent, resolvent_raw, resolvent_fingerprint = _read_json(
        paths[1], max_bytes=2_000_000, canonical_pretty=False
    )
    try:
        c59_resolvent.validate_evidence_document(resolvent)
    except Exception as exc:
        raise c59_exact.StrictDataError("resolvent evidence validation failed") from exc
    if resolvent.get("schema_id") != c59_resolvent.SCHEMA_ID:
        _fail("resolvent evidence schema id changed")

    arrays = group["frozen_permutation_arrays"]["arrays"]
    resolvent_payload = resolvent["payload"]
    w_zero_based = [[value - 1 for value in row] for row in arrays["w27_simple_reflection_generators"]]
    h301_zero_based = [[value - 1 for value in row] for row in arrays["h301_generators"]]
    h303_zero_based = [[value - 1 for value in row] for row in arrays["h303_generators"]]
    if (
        resolvent_payload["group_and_automorphisms"]["w_generators"] != w_zero_based
        or resolvent_payload["invariants"]["301"]["h_generators"] != h301_zero_based
        or resolvent_payload["invariants"]["303"]["h_generators"] != h303_zero_based
    ):
        _fail("group/resolvent W/H arrays are not exactly cross-bound")
    durable = {
        "301": {
            "generators": arrays["h301_generators"],
            "smallgroup_id": [162, 11],
            "tom_locator": 301,
        },
        "303": {
            "generators": arrays["h303_generators"],
            "smallgroup_id": [162, 19],
            "tom_locator": 303,
        },
    }
    if (
        resolvent_payload["authority"]["durable_field_subgroups_sha256"]
        != c59_resolvent.compact_sha256(durable)
    ):
        _fail("resolvent durable subgroup digest is not the group-evidence carrier")

    group_report_sha = group["independent_replay"]["checker"][
        "checker_projection_sha256"
    ]
    _require_digest(group_report_sha, "group internal report digest")
    _require_digest(resolvent["payload_sha256"], "resolvent internal report digest")
    contract = {
        "artifact_count": 2,
        "artifacts": [
            {
                "format": "canonical_compact_json",
                "internal_report_sha256": group_report_sha,
                "path": "results/c59_group_evidence.json",
                "schema_id": group["schema_id"],
                "sha256": group_fingerprint.sha256,
                "size_bytes": len(group_raw),
            },
            {
                "format": "canonical_compact_json",
                "internal_report_sha256": resolvent["payload_sha256"],
                "path": "results/c59_resolvent_evidence.json",
                "schema_id": resolvent["schema_id"],
                "schema_sha256": resolvent["schema_sha256"],
                "sha256": resolvent_fingerprint.sha256,
                "size_bytes": len(resolvent_raw),
            },
        ],
        "immutable_inputs": True,
        "same_real_nonsymlink_parent": True,
        "schema_id": "hcs-c59-artifact-contract-v1",
    }
    return contract, group, resolvent


@dataclass(frozen=True)
class _StageFileSeal:
    sha256: str
    size_bytes: int
    mode: int
    mtime_ns: int
    device: int
    inode: int
    links: int


@dataclass(frozen=True)
class StageBinding:
    """Canonical runner stage and immutable evidence identities."""

    parent: Path
    group_evidence: Path
    resolvent_evidence: Path
    output: Path
    schema_output: Path
    parent_device: int
    parent_inode: int
    group_seal: _StageFileSeal
    resolvent_seal: _StageFileSeal

    def assert_unchanged(self, label: str) -> None:
        metadata = self.parent.stat()
        if (
            self.parent.is_symlink()
            or not stat.S_ISDIR(metadata.st_mode)
            or self.parent.resolve(strict=True) != self.parent
            or (metadata.st_dev, metadata.st_ino)
            != (self.parent_device, self.parent_inode)
        ):
            _fail(f"canonical stage parent changed at {label}")
        if _seal_stage_input(self.group_evidence) != self.group_seal:
            _fail(f"group evidence changed at {label}")
        if _seal_stage_input(self.resolvent_evidence) != self.resolvent_seal:
            _fail(f"resolvent evidence changed at {label}")


def _seal_stage_input(path: Path) -> _StageFileSeal:
    if path.is_symlink() or not path.is_file():
        _fail(f"stage input must be a regular non-symlink file: {path.name}")
    metadata = path.stat()
    if metadata.st_nlink != 1:
        _fail(f"stage input must have link count one: {path.name}")
    raw, fingerprint = c59_exact.read_stable(path, max_bytes=5_000_000)
    if not raw:
        _fail(f"stage input must be nonempty: {path.name}")
    return _StageFileSeal(
        sha256=fingerprint.sha256,
        size_bytes=fingerprint.size_bytes,
        mode=fingerprint.mode,
        mtime_ns=fingerprint.mtime_ns,
        device=metadata.st_dev,
        inode=metadata.st_ino,
        links=metadata.st_nlink,
    )


def validate_fixed_paths(arguments: argparse.Namespace) -> StageBinding:
    """Bind the one runner-owned canonical direct-child stage directory."""

    artifact_dir = Path(arguments.artifact_dir).absolute()
    output = Path(arguments.output).absolute()
    schema_output = Path(arguments.schema_output).absolute()
    results = RESULTS.resolve(strict=True)
    if (
        not STAGE_NAME_PATTERN.fullmatch(artifact_dir.name)
        or artifact_dir.parent != results
        or not artifact_dir.is_dir()
        or artifact_dir.is_symlink()
        or artifact_dir.resolve(strict=True) != artifact_dir
    ):
        _fail(
            "artifact directory must be one real canonical "
            "PROJECT/results/.c59-stage-[A-Za-z0-9]{8} direct child"
        )
    group_path = artifact_dir / ARTIFACT_NAMES[0]
    resolvent_path = artifact_dir / ARTIFACT_NAMES[1]
    if output != artifact_dir / "c59_certificate.json":
        _fail("producer output must be the fixed certificate basename in the stage")
    if schema_output != artifact_dir / "c59_schema.json":
        _fail("producer schema output must be the fixed schema basename in the stage")
    if len({group_path, resolvent_path, output, schema_output}) != 4:
        _fail("stage input/output paths alias")
    group_seal = _seal_stage_input(group_path)
    resolvent_seal = _seal_stage_input(resolvent_path)
    if (group_seal.device, group_seal.inode) == (
        resolvent_seal.device,
        resolvent_seal.inode,
    ):
        _fail("stage evidence files hardlink one another")
    protected_inodes = {
        (group_seal.device, group_seal.inode),
        (resolvent_seal.device, resolvent_seal.inode),
    }
    output_inodes: set[tuple[int, int]] = set()
    for target in (output, schema_output):
        if os.path.lexists(target):
            metadata = target.lstat()
            if (
                stat.S_ISLNK(metadata.st_mode)
                or not stat.S_ISREG(metadata.st_mode)
                or metadata.st_nlink != 1
            ):
                _fail("existing stage output must be a regular single-link file")
            inode = (metadata.st_dev, metadata.st_ino)
            if inode in protected_inodes or inode in output_inodes:
                _fail("stage output hardlinks an input or another output")
            output_inodes.add(inode)
    parent_metadata = artifact_dir.stat()
    return StageBinding(
        parent=artifact_dir,
        group_evidence=group_path,
        resolvent_evidence=resolvent_path,
        output=output,
        schema_output=schema_output,
        parent_device=parent_metadata.st_dev,
        parent_inode=parent_metadata.st_ino,
        group_seal=group_seal,
        resolvent_seal=resolvent_seal,
    )


def _relative_to_repo(path: Path) -> str:
    try:
        return path.resolve(strict=True).relative_to(REPO.resolve(strict=True)).as_posix()
    except ValueError as exc:
        raise c59_exact.StrictDataError(f"path escapes repository: {path}") from exc


def _batch_c59_section(raw: bytes) -> bytes:
    start = raw.find(b"## HCS-C59:")
    end = raw.find(b"## HCS-C60", start + 1)
    if start < 0 or end < 0 or end <= start:
        _fail("C59 Batch section boundaries are missing")
    return raw[start:end]


def _git_release_manifest_rebind(label: str, contract: dict[str, Any]) -> None:
    commit = contract["release_commit"]
    if not _git_ancestor(commit):
        _fail(f"{label} release commit is not an ancestor of HEAD")
    relative = (contract["project"] / "FULL_PROJECT_HASHES.sha256").relative_to(
        REPO
    ).as_posix()
    completed = subprocess.run(
        ["/usr/bin/git", "show", f"{commit}:{relative}"],
        cwd=REPO,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=c59_pipeline.clean_environment(),
        check=False,
        timeout=60,
    )
    live, _ = c59_exact.read_stable(
        contract["project"] / "FULL_PROJECT_HASHES.sha256", max_bytes=1_000_000
    )
    if completed.returncode != 0 or completed.stderr or completed.stdout != live:
        _fail(f"{label} release commit does not bind the live full manifest")


def _scoped_manifest_summary(label: str, contract: dict[str, Any]) -> dict[str, Any]:
    project = contract["project"]
    path = project / contract["scoped_manifest"]
    value, raw, fingerprint = _read_json(
        path, max_bytes=2_000_000, canonical_pretty=True
    )
    if fingerprint.sha256 != contract["scoped_sha256"]:
        _fail(f"{label} scoped-manifest digest changed")
    _require_keys(
        value,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        f"{label} scoped manifest",
    )
    entries = value["entries"]
    if (
        type(entries) is not list
        or type(value["entry_count"]) is not int
        or value["entry_count"] != len(entries)
        or value["manifest_self_included"] is not False
        or value["status"] != "PREFREEZE_CODE_RESULTS_PASS"
    ):
        _fail(f"{label} scoped-manifest status/count changed")
    declared: set[str] = set()
    for row in entries:
        _require_keys(row, {"path", "sha256", "size_bytes"}, "scoped row")
        relative = row["path"]
        if not c59_exact.safe_relative_path(relative) or relative in declared:
            _fail(f"{label} scoped-manifest path changed")
        declared.add(relative)
        member_raw, member = c59_exact.read_stable(
            project / relative, max_bytes=500_000_000
        )
        if (
            row["sha256"] != member.sha256
            or type(row["size_bytes"]) is not int
            or row["size_bytes"] != member.size_bytes
            or len(member_raw) != member.size_bytes
        ):
            _fail(f"{label} scoped-manifest member changed: {relative}")
    live: set[str] = set()
    for root in (project / "code", project / "results"):
        for child in root.rglob("*"):
            if child.is_symlink() or (not child.is_dir() and not child.is_file()):
                _fail(f"{label} scoped tree contains a special object")
            if child.is_file():
                relative = child.relative_to(project).as_posix()
                if relative != contract["scoped_manifest"]:
                    live.add(relative)
    if live != declared:
        _fail(f"{label} scoped live inventory is not exact")
    return {
        "entry_count": len(declared),
        "inventory_exact_excluding_self": True,
        "manifest_path": _relative_to_repo(path),
        "manifest_sha256": fingerprint.sha256,
        "manifest_size_bytes": len(raw),
    }


def _carrier_projection(label: str, payload: dict[str, Any]) -> dict[str, Any]:
    if label == "C56":
        return {
            "eliminant_coefficients_d_0_to_27": payload["irreducibility"]["eliminant_coefficients_d_0_to_27"],
            "lex_shape": payload["grassmann_main_chart"]["lex_shape"],
            "line_equations_sparse": payload["grassmann_main_chart"]["line_equations_sparse"],
            "line_class_intersection_matrix": payload["we6"]["line_class_intersection_matrix"],
            "simple_reflection_line_permutations": payload["we6"]["simple_reflection_line_permutations"],
        }
    group_raw, group_fingerprint = c59_exact.read_stable(
        PREDECESSORS["C58"]["project"] / "results/c58_group_evidence.json",
        max_bytes=2_000_000,
    )
    if (
        not group_raw
        or group_fingerprint.sha256
        != PREDECESSORS["C58"]["group_evidence_sha256"]
    ):
        _fail("C58 group-evidence authority changed")
    return {
        "G3_dual_action_classification": payload["G3_dual_action_classification"],
        "G4_filtered_inertia": payload["G4_filtered_inertia"],
        "G6_global_and_infinity": payload["G6_global_and_infinity"],
        "group_evidence_sha256": group_fingerprint.sha256,
    }


def _predecessor_summary(label: str) -> dict[str, Any]:
    contract = PREDECESSORS[label]
    _git_release_manifest_rebind(label, contract)
    bound = _bind_released_predecessor(label, contract)
    project = contract["project"]
    certificate_path = project / contract["certificate"]
    schema_path = project / contract["schema"]
    check_path = project / contract["check_report"]
    certificate, certificate_raw, certificate_fp = _read_json(
        certificate_path, max_bytes=5_000_000, canonical_pretty=True
    )
    _, schema_raw, schema_fp = _read_json(
        schema_path, max_bytes=1_000_000, canonical_pretty=True
    )
    _, check_raw, check_fp = _read_json(
        check_path, max_bytes=2_000_000, canonical_pretty=True
    )
    if (
        certificate_fp.sha256 != contract["certificate_sha256"]
        or certificate.get("payload_sha256") != contract["payload_sha256"]
        or schema_fp.sha256 != contract["schema_sha256"]
        or check_fp.sha256 != contract["check_sha256"]
    ):
        _fail(f"{label} certificate/schema/check authority changed")
    route_path = project / "route_a_evaluation.yaml"
    archive_path = project / contract["archive"]
    route_raw, route_fp = c59_exact.read_stable(route_path, max_bytes=1_000_000)
    archive_raw, archive_fp = c59_exact.read_stable(archive_path, max_bytes=1_000_000)
    if (
        route_raw != archive_raw
        or route_fp.sha256 != contract["route_sha256"]
        or archive_fp.sha256 != contract["route_sha256"]
    ):
        _fail(f"{label} live/archive Route authority changed")
    full_path = project / "FULL_PROJECT_HASHES.sha256"
    return {
        "candidate_id": label,
        "certificate_path": _relative_to_repo(certificate_path),
        "certificate_sha256": certificate_fp.sha256,
        "certificate_size_bytes": len(certificate_raw),
        "payload_sha256": certificate["payload_sha256"],
        "schema_path": _relative_to_repo(schema_path),
        "schema_sha256": schema_fp.sha256,
        "check_report_path": _relative_to_repo(check_path),
        "check_report_sha256": check_fp.sha256,
        "carrier_projection_sha256": _canonical_payload_sha256(
            _carrier_projection(label, certificate["payload"])
        ),
        "release_commit": contract["release_commit"],
        "release_commit_ancestor_of_current_head": True,
        "full_manifest": {
            "entry_count": bound["full_inventory_entry_count"],
            "inventory_exact_excluding_self": True,
            "manifest_path": _relative_to_repo(full_path),
            "manifest_sha256": bound["full_inventory_sha256"],
            "manifest_size_bytes": bound["full_inventory_size_bytes"],
        },
        "scoped_manifest": _scoped_manifest_summary(label, contract),
        "live_route_path": _relative_to_repo(route_path),
        "archive_route_path": _relative_to_repo(archive_path),
        "route_sha256": route_fp.sha256,
        "live_archive_route_identical": True,
    }


def rebuild_g0() -> tuple[dict[str, Any], dict[str, bool]]:
    formal, raw_by_name = _formal_aggregate()
    if any(b"NO_BAD_EULER_OR_ROOT_NUMBER" not in raw for raw in raw_by_name.values()):
        _fail("the formal package does not carry the semantic firewall in every file")
    route_raw, route_fp = c59_exact.read_stable(ROUTE, max_bytes=1_000_000)
    batch_raw, batch_fp = c59_exact.read_stable(BATCH, max_bytes=1_000_000)
    guard_raw, guard_fp = c59_exact.read_stable(GUARD, max_bytes=1_000_000)
    if (
        formal["aggregate_sha256"] != FORMAL_PACKAGE_SHA256
        or route_fp.sha256 != ROUTE_SHA256
        or batch_fp.sha256 != BATCH_SHA256
        or guard_fp.sha256 != GUARD_SHA256
    ):
        _fail("C59 formal/Route/Batch/guard lock changed")
    for literal in (
        b"TARGET_LOCK_GO", b"THEOREM_TARGET_LOCKED", b"IMPLEMENTATION_PENDING",
        b"FORMAL_HOSTILE_PASS", b"NOT_RELEASED",
        b"NO_BAD_EULER_OR_ROOT_NUMBER",
    ):
        if literal not in route_raw:
            _fail(f"C59 Route status/firewall literal missing: {literal!r}")
    section = _batch_c59_section(batch_raw)
    value = {
        "schema_id": "hcs-c59-released-authority-rebind-v1",
        "all_released_full_inventories_rebound": True,
        "fixed_predecessor_paths_only": True,
        "released_predecessors": [
            _predecessor_summary("C56"),
            _predecessor_summary("C58"),
        ],
        "formal_target_lock": {
            "markdown_file_count": 13,
            "markdown_aggregate_sha256": formal["aggregate_sha256"],
            "route_path": _relative_to_repo(ROUTE),
            "route_sha256": route_fp.sha256,
            "route_size_bytes": len(route_raw),
            "status": "FORMAL_HOSTILE_PASS_IMPLEMENTATION_PENDING",
        },
        "batch_target_lock": {
            "path": _relative_to_repo(BATCH),
            "sha256": batch_fp.sha256,
            "size_bytes": len(batch_raw),
            "c59_section_sha256": c59_exact.sha256_bytes(section),
            "c59_section_size_bytes": len(section),
        },
        "protected_guard": {
            "path": _relative_to_repo(GUARD),
            "sha256": guard_fp.sha256,
            "size_bytes": len(guard_raw),
        },
    }
    return value, written_bridges_from_formal(raw_by_name)


def _validate_g1(gate: dict[str, Any]) -> None:
    _require_keys(
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
        or gate["schlaefli_graph_parameters"]
        != {"vertices": 27, "edges": 135, "degree": 10}
    ):
        _fail("G1 primitive-resolvent summary changed")
    for label in ("301", "303"):
        if gate["modular_polynomials"].get(label) != {
            "coefficient_count": 321,
            "sha256": EXPECTED_RESOLVENT_HASHES[label],
        }:
            _fail(f"G1 modular polynomial changed: {label}")


def _derive_g3(g1: dict[str, Any], g2: dict[str, Any]) -> dict[str, Any]:
    fields = {
        row.get("label"): row
        for row in g2.get("durable_field_subgroup_invariants", [])
        if type(row) is dict
    }
    if set(fields) != {"H301", "H303"}:
        _fail("G3 cannot locate both durable field subgroups")
    if (
        g1["distinct_values"] != {"301": 320, "303": 320}
        or g2.get("full_permutation_character_equality") is not True
        or type(g2.get("all_350_subgroup_classes")) is not list
        or len(g2["all_350_subgroup_classes"]) != 350
        or g2["all_350_subgroup_classes"][300]["permutation_character_values"]
        != g2["all_350_subgroup_classes"][302]["permutation_character_values"]
    ):
        _fail("G3 character/noncollision premises changed")
    if any(
        fields[label]["support"]["stabilizer_equals_frozen_field_subgroup"]
        is not True
        for label in fields
    ):
        _fail("G3 support-invariance premise changed")
    if (
        [fields["H301"]["core_order"], fields["H303"]["core_order"]] != [1, 1]
        or fields["H301"]["tom_locator"] == fields["H303"]["tom_locator"]
        or fields["H301"]["small_group_id"] == fields["H303"]["small_group_id"]
    ):
        _fail("G3 core/nonconjugacy/nonisomorphism premise changed")
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
        "payload_shape_sha256": c59_exact.sha256_bytes(
            c59_exact.canonical_leaf_bytes(shape_value(payload))
        ),
        "payload_top_level_keys": sorted(payload),
        "schema_id": SCHEMA_ID,
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


def build_payload(
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
    """Build the exact path-free 15-key payload from nine rebound fixtures."""

    for value, label in (
        (group_projection_sha256, "group projection digest"),
        (group_evidence_sha256, "group evidence digest"),
        (resolvent_evidence_sha256, "resolvent evidence digest"),
    ):
        _require_digest(value, label)
    _require_keys(
        source_contract,
        {"entries", "entry_count", "exact_code_inventory", "exact_code_path_allowlist", "schema_id", "self_reference_policy"},
        "source contract",
    )
    _require_keys(
        g0,
        {"all_released_full_inventories_rebound", "batch_target_lock", "fixed_predecessor_paths_only", "formal_target_lock", "protected_guard", "released_predecessors", "schema_id"},
        "G0",
    )
    _require_keys(
        artifact_contract_value,
        {"artifact_count", "artifacts", "immutable_inputs", "same_real_nonsymlink_parent", "schema_id"},
        "artifact contract",
    )
    _require_keys(
        backend_contract_value,
        {"gap", "math_python", "pari_dependency", "schema_id", "singular_dependency", "two_run_deterministic"},
        "backend contract",
    )
    try:
        c59_group.validate_evidence(group_evidence)
    except Exception as exc:
        raise c59_exact.StrictDataError("group evidence is not producer-valid") from exc
    if type(resolver_payload) is not dict:
        _fail("resolver payload must be an object")
    g1 = deepcopy(resolver_payload["G1_primitive_orbit_resolvents"])
    _validate_g1(g1)
    g2 = deepcopy(group_evidence["G2_gassmann_minimality"])
    g4 = deepcopy(group_evidence["G4_global_arithmetic"])
    g5 = deepcopy(group_evidence["G5_tom140_local_algebra"])
    g6 = deepcopy(group_evidence["G6_tom206_local_algebra"])
    g3 = _derive_g3(g1, g2)
    g7 = _base_g7(
        group_projection_sha256=group_projection_sha256,
        group_evidence_sha256=group_evidence_sha256,
        resolvent_checker_payload_sha256=c59_exact.sha256_bytes(
            c59_exact.canonical_json_bytes(resolver_payload)
        ),
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
        _fail("payload does not have the exact 15-key contract")
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
            env=c59_pipeline.clean_environment(),
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
    math = c59_pipeline.executable(math_python, "FLINT/SymPy/NetworkX")
    gap = c59_pipeline.executable(gap_path, "GAP")
    math_raw, math_fp = c59_exact.read_stable(math, max_bytes=40_000_000)
    gap_raw, gap_fp = c59_exact.read_stable(gap, max_bytes=1_000_000)
    expected_math = c59_pipeline.EXPECTED_BACKENDS["math"]
    if (
        c59_exact.sha256_bytes(math_raw) != expected_math["executable_sha256"]
        or math_fp.size_bytes != expected_math["executable_size_bytes"]
        or c59_exact.sha256_bytes(gap_raw)
        != c59_pipeline.EXPECTED_GAP["executable_sha256"]
        or gap_fp.size_bytes
        != c59_pipeline.EXPECTED_GAP["executable_size_bytes"]
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
    python_value = c59_exact.strict_json_loads(
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
    if not c59_exact.deep_exact(python_value, expected_python):
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
        raise c59_exact.StrictDataError("GAP preflight output is not ASCII") from exc
    observed_gap = {
        "resolved_executable": str(gap),
        "executable_sha256": c59_exact.sha256_bytes(gap_raw),
        "executable_size_bytes": gap_fp.size_bytes,
        "gap_version": fields[0] if len(fields) == 4 else "",
        "tomlib_version": fields[1] if len(fields) == 4 else "",
        "smallgrp_version": fields[2] if len(fields) == 4 else "",
        "ctbllib_version": fields[3] if len(fields) == 4 else "",
    }
    if not c59_exact.deep_exact(observed_gap, c59_pipeline.EXPECTED_GAP):
        _fail("GAP versions or executable identity changed")
    return {
        "schema_id": "hcs-c59-backend-contract-v1",
        "math_python": {
            "resolved_executable": str(math),
            "executable_sha256": c59_exact.sha256_bytes(math_raw),
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
        output=Path(artifact_dir) / "c59_certificate.json",
        schema_output=Path(artifact_dir) / "c59_schema.json",
    )
    binding = validate_fixed_paths(namespace)
    source_before = source_contract()
    g0, written = rebuild_g0()
    if written != {key: True for key in WRITTEN_BRIDGE_KEYS}:
        _fail("formal written-bridge lock changed")
    artifacts, group, resolvent = artifact_contract(binding.parent)
    backends = _backend_contract(Path(math_python), Path(gap), binding)
    group_projection_sha256 = group["independent_replay"]["checker"][
        "checker_projection_sha256"
    ]
    payload = build_payload(
        source_before,
        g0,
        artifacts,
        resolvent["payload"],
        group,
        backends,
        group_projection_sha256,
        binding.group_seal.sha256,
        binding.resolvent_seal.sha256,
    )
    binding.assert_unchanged("after payload assembly")
    final_source = source_contract()
    final_g0, final_written = rebuild_g0()
    final_artifacts, final_group, final_resolvent = artifact_contract(binding.parent)
    if (
        not c59_exact.deep_exact(source_before, final_source)
        or not c59_exact.deep_exact(g0, final_g0)
        or written != final_written
        or not c59_exact.deep_exact(artifacts, final_artifacts)
        or not c59_exact.deep_exact(group, final_group)
        or not c59_exact.deep_exact(resolvent, final_resolvent)
    ):
        _fail("source, formal authority, or immutable evidence changed during assembly")
    binding.assert_unchanged("at payload assembly return")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-output", type=Path, required=True)
    parser.add_argument(
        "--math-python",
        type=Path,
        default=Path("/root/miniconda3/bin/python3"),
    )
    parser.add_argument("--gap", type=Path, default=Path("/usr/bin/gap"))
    arguments = parser.parse_args()
    c59_exact.reject_optimized_python()
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
        "schema_sha256": c59_exact.sha256_bytes(
            c59_exact.canonical_leaf_bytes(schema)
        ),
        "payload": payload,
        "payload_sha256": c59_exact.sha256_bytes(
            c59_exact.canonical_leaf_bytes(payload)
        ),
    }
    schema_raw = c59_exact.canonical_json_bytes(schema, pretty=True)
    certificate_raw = c59_exact.canonical_json_bytes(certificate, pretty=True)
    if len(schema_raw) > 200_000 or len(certificate_raw) > MAX_CERTIFICATE_BYTES:
        _fail("generated schema or certificate exceeds its byte ceiling")
    binding.assert_unchanged("before final producer rebound")
    if (
        not c59_exact.deep_exact(payload["source_contract"], source_contract())
        or not c59_exact.deep_exact(
            payload["G0_released_authority_rebind"], rebuild_g0()[0]
        )
        or not c59_exact.deep_exact(
            payload["artifact_contract"], artifact_contract(binding.parent)[0]
        )
    ):
        _fail("producer authority changed before certificate/schema write")
    binding.assert_unchanged("immediately before output preparation")
    outputs = c59_exact.prepare_output_targets(
        (binding.output, binding.schema_output),
        protected=(binding.group_evidence, binding.resolvent_evidence),
    )
    try:
        c59_exact.atomic_write(outputs[1], schema_raw)
        c59_exact.atomic_write(outputs[0], certificate_raw)
    except BaseException:
        for output in outputs:
            if output.exists() and output.is_file() and not output.is_symlink():
                output.unlink()
        raise
    print("C59 PRODUCER PASS PREFREEZE")
    print(f"payload_scalar_leaves={scalar_leaf_count(payload)}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    print(f"certificate_sha256={hashlib.sha256(certificate_raw).hexdigest()}")


if __name__ == "__main__":
    main()
