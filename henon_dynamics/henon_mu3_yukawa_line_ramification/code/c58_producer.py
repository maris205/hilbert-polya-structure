#!/usr/bin/env python3
"""Build the strict HCS-C58 PREFREEZE certificate from immutable evidence."""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path
from pathlib import PurePosixPath
import subprocess
import sys
from typing import Any

from c58_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deterministic_gzip,
    deep_exact,
    prepare_output_targets,
    read_stable,
    reject_optimized_python,
    require_canonical_compact_json,
    safe_relative_path,
    sha256_bytes,
    strict_gzip_json,
    strict_json_loads,
)
from c58_pipeline import (
    clean_environment,
    gap_preflight,
    python_preflight,
    run_canonical_report,
)


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

REPO = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
CODE = PROJECT / "code"
RESULTS = PROJECT / "results"
C55 = REPO / "henon_dynamics/henon_mu3_rational_yukawa_surface"
C56 = REPO / "henon_dynamics/henon_mu3_yukawa_line_field"
C57 = REPO / "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump"

CODE_FILES = (
    "README.md",
    "c58_arithmetic.py",
    "c58_atomic_promote.py",
    "c58_checker.py",
    "c58_checker_group.g",
    "c58_checker_pari.py",
    "c58_exact.py",
    "c58_group.py",
    "c58_hash_manifest.py",
    "c58_pipeline.py",
    "c58_producer.py",
    "c58_surface.py",
    "run_all.sh",
    "test_c58.py",
)
CODE_SOURCE_NAMES = set(CODE_FILES)
ARTIFACT_NAMES = (
    "c58_arithmetic_evidence.json.gz",
    "c58_group_evidence.json",
)
PAYLOAD_KEYS = (
    "C58_source_contract",
    "G0_upstream_source_lock",
    "G1_bad_prime_exhaustion",
    "G2_local_order_exact",
    "G3_dual_action_classification",
    "G4_filtered_inertia",
    "G5_character_conductors",
    "G6_global_and_infinity",
    "G7_replay_and_scope",
    "artifact_contract",
    "backends",
    "documentation_contract",
    "nonresults_firewall",
    "scope_firewall",
    "status_contract",
)
UPSTREAM = {
    "C55": {
        "project": C55,
        "inventory": C55 / "results/ARTIFACT_HASHES.sha256",
        "inventory_sha256": "8b9a935bddb4aee04561860491eb982311b6776e250b41c8598336fe6bfc2fc9",
        "entry_count": 47,
        "release_commit": "c124ba53c3d89514a00b0949e62b645228dbcfc5",
        "certificate": C55 / "results/c55_certificate.json",
        "certificate_sha256": "aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f",
    },
    "C56": {
        "project": C56,
        "inventory": C56 / "FULL_PROJECT_HASHES.sha256",
        "inventory_sha256": "26e3e4226cd1baea14543f14bac9ffd060ed8031741cb1ec0a38e22cd07487f4",
        "entry_count": 46,
        "release_commit": "a55f31dca338d1e3757704b8c95d11e28c9c98d4",
        "certificate": C56 / "results/c56_certificate.json",
        "certificate_sha256": "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4",
        "check_report": C56 / "results/c56_check_report.json",
        "check_report_sha256": "4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9",
        "scoped_manifest": C56 / "results/scoped_hash_manifest.json",
        "scoped_manifest_sha256": "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a",
    },
    "C57": {
        "project": C57,
        "inventory": C57 / "FULL_PROJECT_HASHES.sha256",
        "inventory_sha256": "140bbc3dcc723c533b62512dd2f21cd47bd32fc26a4e2cf7344a9aa070872745",
        "entry_count": 64,
        "release_commit": "7775269a4cab9c85e291a719eb561cec188ede09",
        "certificate": C57 / "results/c57_certificate.json",
        "certificate_sha256": "3078baf167d2344982d9f93811f1fd59a8258c8178ecce4decbd2b054b16092f",
        "check_report": C57 / "results/c57_check_report.json",
        "check_report_sha256": "fb0afb77f130fb2d0a792af8d949e5c1a8e1b7864525dd62f1d1a41d99a79bcf",
        "scoped_manifest": C57 / "results/scoped_hash_manifest.json",
        "scoped_manifest_sha256": "864c05b18e0bdcafbc5b5e3206840a1b25afa355b9737ebcc9d1806e33fcec5d",
    },
}
Q = 14932047182473291995860108491583652133938007263719
SURFACE_BAD_PRIME_ENVELOPE = (2, 3, 5, 181, 283, 997, 1801, 2346241, Q)
RAMIFIED_SUPPORT = SURFACE_BAD_PRIME_ENVELOPE[1:]
DIRECT_PRIMES = (3, 5, 181, 997, 2346241)
FIELD_EXPONENTS = (0, 46, 36, 18, 6, 18, 6, 18, 6)


def git(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["/usr/bin/git", *arguments],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=clean_environment(),
        check=check,
        timeout=60,
    )


def source_contract() -> dict[str, Any]:
    children = list(CODE.iterdir())
    if any(path.is_symlink() or not path.is_file() for path in children):
        raise StrictDataError("C58 code inventory contains a non-regular entry")
    names = {path.name for path in children}
    if len(names) != len(children) or names != set(CODE_FILES):
        raise StrictDataError(
            f"C58 code inventory mismatch; missing={sorted(set(CODE_FILES)-names)}; "
            f"extra={sorted(names-set(CODE_FILES))}"
        )
    entries = []
    for name in CODE_FILES:
        raw, fingerprint = read_stable(CODE / name, max_bytes=3_000_000)
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": len(raw),
            }
        )
    return {
        "entries": entries,
        "entry_count": len(entries),
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [
            f"code/{name}" for name in sorted(CODE_SOURCE_NAMES)
        ],
        "schema_id": "hcs-c58-exact-source-contract-v1",
        "self_reference_policy": (
            "certificate/schema/check/manifest digests are excluded; immutable raw evidence is separately rebound"
        ),
    }


def parse_inventory(name: str, contract: dict[str, Any]) -> dict[str, Any]:
    project = contract["project"]
    inventory_path = contract["inventory"]
    raw, fingerprint = read_stable(inventory_path, max_bytes=1_000_000)
    if fingerprint.sha256 != contract["inventory_sha256"]:
        raise StrictDataError(f"{name} full inventory digest changed")
    try:
        lines = raw.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise StrictDataError(f"{name} inventory is not UTF-8") from exc
    entries = []
    declared_paths = set()
    for line in lines:
        if len(line) < 67 or line[64:66] != "  ":
            raise StrictDataError(f"{name} inventory line is malformed")
        digest, relative = line[:64], line[66:]
        if (
            len(digest) != 64
            or any(character not in "0123456789abcdef" for character in digest)
            or not safe_relative_path(relative)
            or relative in declared_paths
        ):
            raise StrictDataError(f"{name} inventory entry is unsafe")
        path = project / relative
        file_raw, file_fingerprint = read_stable(path, max_bytes=200_000_000)
        if file_fingerprint.sha256 != digest:
            raise StrictDataError(f"{name} inventory leaf changed: {relative}")
        declared_paths.add(relative)
        entries.append(
            {
                "path": relative,
                "sha256": digest,
                "size_bytes": len(file_raw),
            }
        )
    inventory_relative = inventory_path.relative_to(project).as_posix()
    allowed_directories = set()
    for relative in declared_paths | {inventory_relative}:
        for parent in PurePosixPath(relative).parents:
            if parent.as_posix() != ".":
                allowed_directories.add(parent.as_posix())
    observed_paths = set()
    observed_directories = set()
    for path in project.rglob("*"):
        relative = path.relative_to(project).as_posix()
        if path.is_symlink():
            raise StrictDataError(f"{name} upstream tree contains a symlink")
        if path.is_file():
            if relative != inventory_relative:
                observed_paths.add(relative)
        elif path.is_dir():
            observed_directories.add(relative)
        else:
            raise StrictDataError(f"{name} upstream tree contains a special object")
    if (
        declared_paths != observed_paths
        or observed_directories != allowed_directories
        or len(entries) != contract["entry_count"]
    ):
        raise StrictDataError(f"{name} full live inventory is not exact")
    certificate_raw, certificate_fingerprint = read_stable(
        contract["certificate"], max_bytes=10_000_000
    )
    if certificate_fingerprint.sha256 != contract["certificate_sha256"]:
        raise StrictDataError(f"{name} certificate changed")
    certificate = strict_json_loads(certificate_raw, max_bytes=10_000_000)
    payload = certificate.get("payload")
    if (
        type(payload) is not dict
        or certificate.get("payload_sha256")
        != sha256_bytes(canonical_leaf_bytes(payload))
    ):
        raise StrictDataError(f"{name} certificate payload digest is invalid")
    if name == "C55":
        certificate_status = payload.get("artifact_status")
        if certificate_status != "RELEASE_CANDIDATE":
            raise StrictDataError("C55 certificate semantic status is not release-candidate")
    elif name == "C56":
        certificate_status = payload.get("theorem_gates", {}).get("final_status")
        if certificate_status != "PREFREEZE_CODE_RESULTS_PASS":
            raise StrictDataError("C56 certificate semantic status is not PASS")
    elif name == "C57":
        certificate_status = certificate.get("status")
        if certificate_status != "PREFREEZE_CODE_RESULTS_PASS":
            raise StrictDataError("C57 certificate semantic status is not PASS")
    else:
        raise StrictDataError("unknown upstream certificate status contract")
    extra = {}
    for key in ("check_report", "scoped_manifest"):
        if key in contract:
            leaf_raw, leaf_fingerprint = read_stable(
                contract[key], max_bytes=20_000_000
            )
            if leaf_fingerprint.sha256 != contract[f"{key}_sha256"]:
                raise StrictDataError(f"{name} {key} changed")
            extra[f"{key}_sha256"] = leaf_fingerprint.sha256
            extra[f"{key}_size_bytes"] = len(leaf_raw)
            if key == "check_report":
                check_report = strict_json_loads(leaf_raw, max_bytes=20_000_000)
                if (
                    check_report.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
                    or check_report.get("payload_sha256")
                    != certificate["payload_sha256"]
                    or (
                        name == "C57"
                        and check_report.get("full_semantic_leaf_rebuild") is not True
                    )
                ):
                    raise StrictDataError(f"{name} check report semantic PASS gate failed")
                extra["check_report_result"] = check_report["result"]
    extra["certificate_semantic_status"] = certificate_status
    return {
        "certificate_payload_sha256": certificate.get("payload_sha256"),
        "certificate_sha256": certificate_fingerprint.sha256,
        "full_inventory_entries": entries,
        "full_inventory_entry_count": len(entries),
        "full_inventory_exact_live_rebind": True,
        "full_inventory_sha256": fingerprint.sha256,
        "release_commit": contract["release_commit"],
        **extra,
    }


def upstream_source_lock() -> dict[str, Any]:
    result = {}
    for name, contract in UPSTREAM.items():
        release = contract["release_commit"]
        if git("merge-base", "--is-ancestor", release, "HEAD", check=False).returncode:
            raise StrictDataError(f"{name} release is not an ancestor of HEAD")
        relative = contract["project"].relative_to(REPO).as_posix()
        if git("diff", "--quiet", release, "--", relative, check=False).returncode:
            raise StrictDataError(f"tracked {name} subtree changed after release")
        result[name] = parse_inventory(name, contract)
        result[name]["release_is_ancestor_of_HEAD"] = True
        result[name]["tracked_subtree_unchanged"] = True
    return {
        "all_three_full_live_inventories_rebound": True,
        "upstream_projects": result,
    }


def artifact_contract(artifact_dir: Path):
    if artifact_dir.is_symlink() or not artifact_dir.is_dir():
        raise StrictDataError("artifact directory must be a non-symlink directory")
    arithmetic_path = artifact_dir / ARTIFACT_NAMES[0]
    arithmetic, arithmetic_raw, arithmetic_fingerprint = strict_gzip_json(
        arithmetic_path,
        max_compressed_bytes=4_000_000,
        max_decompressed_bytes=8_000_000,
    )
    require_canonical_compact_json(arithmetic_raw)
    compressed_raw, _ = read_stable(arithmetic_path, max_bytes=4_000_000)
    if deterministic_gzip(arithmetic_raw) != compressed_raw:
        raise StrictDataError("arithmetic evidence gzip is not deterministic")
    if arithmetic.get("schema_id") != "hcs-c58-arithmetic-evidence-v1":
        raise StrictDataError("arithmetic evidence schema changed")
    group_path = artifact_dir / ARTIFACT_NAMES[1]
    group_raw, group_fingerprint = read_stable(group_path, max_bytes=1_000_000)
    group = strict_json_loads(group_raw, max_bytes=1_000_000)
    if group_raw != canonical_json_bytes(group, pretty=True):
        raise StrictDataError("group evidence is not canonical pretty JSON")
    if group.get("schema_id") != "hcs-c58-group-evidence-v1":
        raise StrictDataError("group evidence schema changed")
    contract = {
        "artifact_count": 2,
        "artifacts": [
            {
                "decompressed_sha256": sha256_bytes(arithmetic_raw),
                "decompressed_size_bytes": len(arithmetic_raw),
                "format": "deterministic_gzip_canonical_compact_json",
                "path": f"results/{ARTIFACT_NAMES[0]}",
                "sha256": arithmetic_fingerprint.sha256,
                "size_bytes": arithmetic_fingerprint.size_bytes,
            },
            {
                "format": "canonical_pretty_json",
                "path": f"results/{ARTIFACT_NAMES[1]}",
                "sha256": group_fingerprint.sha256,
                "size_bytes": group_fingerprint.size_bytes,
            },
        ],
        "immutable_raw_evidence_carriers": True,
        "schema_id": "hcs-c58-artifact-contract-v1",
    }
    return contract, arithmetic, group


def normalized_backends(
    pari_python: Path, flint_python: Path, gap: Path
) -> dict[str, Any]:
    python = python_preflight(pari_python, flint_python)
    gap_value = gap_preflight(gap)
    if gap_value.get("ctbllib_version") != "1.3.1":
        raise StrictDataError("CTblLib 1.3.1 is required")
    return {
        "FLINT_SYMPY": {
            "path_contract": "MINICONDA3_BIN_PYTHON3",
            **{key: value for key, value in python["flint_group"].items() if key != "resolved_executable"},
        },
        "GAP_TOMLIB_SMALLGRP": {
            "path_contract": "USR_BIN_GAP",
            **{key: value for key, value in gap_value.items() if key != "resolved_executable"},
        },
        "PARI": {
            "path_contract": "USR_BIN_PYTHON3",
            **{key: value for key, value in python["pari"].items() if key != "resolved_executable"},
        },
    }


def exact_reports(
    artifact_dir: Path, pari_python: Path, flint_python: Path
) -> dict[str, Any]:
    arithmetic_path = artifact_dir / ARTIFACT_NAMES[0]
    group_path = artifact_dir / ARTIFACT_NAMES[1]
    arithmetic, arithmetic_sha = run_canonical_report(
        pari_python,
        CODE / "c58_arithmetic.py",
        ["--evidence", arithmetic_path],
        timeout=900,
    )
    surface_flint, surface_flint_sha = run_canonical_report(
        flint_python,
        CODE / "c58_surface.py",
        ["--engine", "flint", "--evidence", arithmetic_path],
        timeout=180,
    )
    surface_bareiss, surface_bareiss_sha = run_canonical_report(
        flint_python,
        CODE / "c58_surface.py",
        ["--engine", "bareiss", "--evidence", arithmetic_path],
        timeout=180,
    )
    group, group_sha = run_canonical_report(
        flint_python,
        CODE / "c58_group.py",
        ["--evidence", group_path],
        timeout=300,
    )
    for label, report in (
        ("surface_flint", surface_flint),
        ("surface_bareiss", surface_bareiss),
        ("group", group),
    ):
        if report.get("status") != "PASS":
            raise StrictDataError(f"{label} producer replay did not pass")
    if surface_flint["macaulay_sha256"] != surface_bareiss["macaulay_sha256"]:
        raise StrictDataError("independent surface determinant engines disagree")
    if arithmetic.get("schema_id") != "hcs-c58-checker-pari-report-v1":
        raise StrictDataError("arithmetic producer replay schema changed")
    precision_gate = arithmetic.get("degree36_precision_gate", {})
    if precision_gate.get(
        "theta_precision_exceeds_global_polynomial_discriminant_exponent"
    ) is not True:
        raise StrictDataError("theta36 resolver-separation authority gate failed")
    if precision_gate.get(
        "theta_precision_exceeds_twice_max_factor_discriminant_exponent"
    ) is not True:
        raise StrictDataError("theta36 factor-Krasner authority gate failed")
    if arithmetic.get("surface_bad_prime_envelope_isprime") != [True] * 9:
        raise StrictDataError("surface bad-prime envelope primality gate failed")
    wild_authority = arithmetic.get("wild_degree36_theta_authority", {})
    if (
        wild_authority.get("resolver") != "theta36"
        or wild_authority.get("authority_role") != "KRASNER_CERTIFIED_AUTHORITY"
        or wild_authority.get("certified_precisions") != [900, 950, 1000]
        or wild_authority.get("delta36_role")
        != "BOUNDED_NON_RESULT_NONDEPENDENCY"
        or sorted(wild_authority.get("prime_records", {})) != ["3", "5"]
        or any(
            not row.get("all_factors_monic_simple")
            or not row.get("authority_bound_satisfied")
            or not row.get("factor_rows_stable_across_precisions")
            or row.get("factor_krasner_bounds_satisfied") != [True, True, True]
            or row.get("resolver_separation_bounds_satisfied")
            != [True, True, True]
            or row.get("minimum_multiplyback_valuations") != [900, 950, 1000]
            for row in wild_authority.get("prime_records", {}).values()
        )
    ):
        raise StrictDataError("wild theta36 high-precision authority gate failed")
    if (
        arithmetic.get("theta36_real_root_count") != 4
        or arithmetic.get("line_field_signature") != [3, 12]
    ):
        raise StrictDataError("archimedean arithmetic authority gate failed")
    surface_boolean_keys = (
        "reflection_affine_hessian_units",
        "reflection_chart0_reduced_point_bases_verified",
        "reflection_critical_points_hensel_lift_uniquely",
        "reflection_critical_values_congruent_to_integer_witness_mod_p_squared",
        "reflection_residue_characteristics_odd",
        "reflection_smoothing_parameter_valuation_exactly_one",
        "reflection_unique_geometric_singular_point_each_prime",
    )
    if any(
        surface_flint.get(key) is not True
        or surface_bareiss.get(key) is not True
        for key in surface_boolean_keys
    ):
        raise StrictDataError("reflection local-geometry replay gate failed")
    if group.get("tame_C3_degree_36_local_rows_unique") is not True:
        raise StrictDataError("theta36 local rows do not uniquely select tame inertia")
    if (
        group.get("p3_all_tom_decomposition_pattern_hits")
        != [[140, 18, [18, 4]], [142, 18, [18, 3]], [206, 36, [36, 10]]]
        or group.get("p3_valid_decomposition_inertia_pairs")
        != [[140, 140, 1], [142, 142, 1], [206, 140, 2], [206, 142, 2]]
        or group.get("p5_all_tom_decomposition_pattern_hits")
        != [[147, 20, [20, 3]], [247, 60, [60, 5]], [295, 120, [120, 34]]]
        or group.get("p5_valid_decomposition_inertia_pairs") != [[147, 147, 1]]
        or group.get("p5_wild_normalizer_filter_unique") is not True
    ):
        raise StrictDataError("exhaustive decomposition/inertia group gate failed")
    return {
        "arithmetic": {"report": arithmetic, "report_sha256": arithmetic_sha},
        "group": {"report": group, "report_sha256": group_sha},
        "surface_bareiss": {
            "report": surface_bareiss,
            "report_sha256": surface_bareiss_sha,
        },
        "surface_flint": {
            "report": surface_flint,
            "report_sha256": surface_flint_sha,
        },
    }


def decimal_guard(value: int) -> dict[str, Any]:
    text = str(value)
    return {
        "decimal_newline_sha256": sha256_bytes((text + "\n").encode("ascii")),
        "digits": len(text.lstrip("-")),
        "positive": value > 0,
    }


def build_payload(
    artifact_dir: Path,
    pari_python: Path,
    flint_python: Path,
    gap: Path,
) -> dict[str, Any]:
    source_before = source_contract()
    upstream_before = upstream_source_lock()
    artifacts_before, arithmetic, group = artifact_contract(artifact_dir)
    backends = normalized_backends(pari_python, flint_python, gap)
    reports = exact_reports(artifact_dir, pari_python, flint_python)

    if not deep_exact(source_before, source_contract()):
        raise StrictDataError("C58 source changed during producer replay")
    if not deep_exact(upstream_before, upstream_source_lock()):
        raise StrictDataError("upstream source changed during producer replay")
    artifacts_after, arithmetic_after, group_after = artifact_contract(artifact_dir)
    if not (
        deep_exact(artifacts_before, artifacts_after)
        and deep_exact(arithmetic, arithmetic_after)
        and deep_exact(group, group_after)
    ):
        raise StrictDataError("immutable evidence changed during producer replay")

    group_report = group["group_report"]
    pari_report = reports["arithmetic"]["report"]
    p3 = group_report["p3"]
    p5 = group_report["p5"]
    tame = group_report["tame_C3"]
    theta_local = arithmetic["degree36_local_factors"]["theta36"]
    delta_local = arithmetic["degree36_local_factors"]["delta36"]
    if not all(
        row["authority_bound_satisfied"]
        and row["factor_krasner_bound_satisfied"]
        and row["resolver_separation_bound_satisfied"]
        and row["authority_role"] == "KRASNER_CERTIFIED_AUTHORITY"
        and row["authority_precision"] == 40
        and row["global_polynomial_discriminant_exponent"] == 24
        and row["twice_max_polynomial_discriminant_exponent"] == 24
        for row in theta_local.values()
    ):
        raise StrictDataError("theta36 evidence authority fields changed")
    if not all(
        not row["authority_bound_satisfied"]
        and not row["factor_krasner_bound_satisfied"]
        and not row["resolver_separation_bound_satisfied"]
        and row["authority_role"] == "BOUNDED_NON_RESULT_NONDEPENDENCY"
        and row["global_polynomial_discriminant_exponent"] == 840
        and row["twice_max_polynomial_discriminant_exponent"] == 408
        for row in delta_local.values()
    ):
        raise StrictDataError("delta36 nonresult firewall changed")
    wild_theta = arithmetic["wild_degree36_theta_authority"]
    if not deep_exact(
        wild_theta, pari_report["wild_degree36_theta_authority"]
    ):
        raise StrictDataError("wild theta36 evidence/replay cross-binding changed")
    wild_p3 = wild_theta["prime_records"]["3"]
    wild_p5 = wild_theta["prime_records"]["5"]
    if (
        wild_theta["certified_precisions"] != [900, 950, 1000]
        or wild_p3["factor_degree_multiplicities"]
        != [[3, 3], [9, 1], [18, 1]]
        or wild_p5["factor_degree_multiplicities"]
        != [[1, 1], [5, 1], [10, 3]]
        or wild_p3["global_polynomial_discriminant_exponent"] != 886
        or wild_p3["twice_max_polynomial_discriminant_exponent"] != 538
        or wild_p5["global_polynomial_discriminant_exponent"] != 746
        or wild_p5["twice_max_polynomial_discriminant_exponent"] != 246
    ):
        raise StrictDataError("wild theta36 compact authority values changed")
    tom_exhaustion = group_report["tom_dual_action_exhaustion"]
    p3_all_tom_hits = [
        [row["tom_index"], row["order"], row["id_group"]]
        for row in tom_exhaustion["p3_all_tom_decomposition_pattern_hits"]
    ]
    p5_all_tom_hits = [
        [row["tom_index"], row["order"], row["id_group"]]
        for row in tom_exhaustion["p5_all_tom_decomposition_pattern_hits"]
    ]
    if (
        p3_all_tom_hits
        != [[140, 18, [18, 4]], [142, 18, [18, 3]], [206, 36, [36, 10]]]
        or p5_all_tom_hits
        != [[147, 20, [20, 3]], [247, 60, [60, 5]], [295, 120, [120, 34]]]
        or tom_exhaustion["p3_valid_decomposition_inertia_pairs"]
        != [[140, 140, 1], [142, 142, 1], [206, 140, 2], [206, 142, 2]]
        or tom_exhaustion["p5_valid_decomposition_inertia_pairs"]
        != [[147, 147, 1]]
    ):
        raise StrictDataError("ToM decomposition/inertia exhaustion changed")
    p3_equation = p3["filtration_multiplicity_equation"]
    p5_equation = p5["candidate"]["filtration_multiplicity_equation"]
    deep_C3_exhaustion = p3["deep_C3_exhaustion"]
    p5_filtration_equation = p5["filtration_equation"]
    if (
        p3_equation["nonnegative_integer_solutions"]
        != [{"deep_C3_layers": 6, "wild_C3_squared_layers": 1}]
        or p3_equation["unique"] is not True
        or p5_equation["nonnegative_integer_solutions"]
        != [{"wild_C5_layers": 3}]
        or p5_equation["unique"] is not True
    ):
        raise StrictDataError("wild filtration multiplicity solution changed")

    A = 181 * 997 * 2346241
    B = 283 * 1801 * Q
    conductor6 = 3**11 * 5**7 * A**6 * B
    conductor20 = 3**35 * 5**29 * A**12 * B**5
    disc_e = arithmetic["field_discriminant"]["value"]
    if conductor6 * conductor20 != disc_e:
        raise StrictDataError("conductor-discriminant identity for E failed")
    normal_exponents = {
        "p3": 106560,
        "p5": 80352,
        "reflection_C2": 25920,
        "tame_C3": 34560,
    }
    disc_k = (
        3 ** normal_exponents["p3"]
        * 5 ** normal_exponents["p5"]
        * A ** normal_exponents["tame_C3"]
        * B ** normal_exponents["reflection_C2"]
    )
    disc_k_guard = decimal_guard(disc_k)
    if disc_k_guard != {
        "decimal_newline_sha256": "951c29693b90bfdc8ab1d9ad03d11a5b54ab42e7eef8b57154b97aef5040c3d9",
        "digits": 1931353,
        "positive": True,
    }:
        raise StrictDataError("normal-closure discriminant guard changed")
    if not group_report["counts"]["line_action_faithful"]:
        raise StrictDataError("line action is not faithful")

    def expanded_factor_degrees(row: dict[str, Any]) -> list[int]:
        return [
            degree
            for degree, count in row["factor_degree_multiplicities"]
            for _ in range(count)
        ]

    all_wild_rows = [wild_p3, wild_p5]
    wild_authority_compact = {
        "all_factor_rows_stable": all(
            row["factor_rows_stable_across_precisions"] for row in all_wild_rows
        ),
        "all_krasner_and_separation_bounds_satisfied": all(
            row["authority_bound_satisfied"]
            and row["factor_krasner_bounds_satisfied"] == [True, True, True]
            and row["resolver_separation_bounds_satisfied"] == [True, True, True]
            for row in all_wild_rows
        ),
        "all_multiplybacks_satisfied": all(
            all(
                valuation >= precision
                for valuation, precision in zip(
                    row["minimum_multiplyback_valuations"],
                    wild_theta["certified_precisions"],
                )
            )
            for row in all_wild_rows
        ),
        "certified_precisions": wild_theta["certified_precisions"],
        "delta36_role": wild_theta["delta36_role"],
        "p3": {
            "factor_degrees": expanded_factor_degrees(wild_p3),
            "global_polynomial_discriminant_exponent": wild_p3[
                "global_polynomial_discriminant_exponent"
            ],
            "twice_max_polynomial_discriminant_exponent": wild_p3[
                "twice_max_polynomial_discriminant_exponent"
            ],
        },
        "p5": {
            "factor_degrees": expanded_factor_degrees(wild_p5),
            "global_polynomial_discriminant_exponent": wild_p5[
                "global_polynomial_discriminant_exponent"
            ],
            "twice_max_polynomial_discriminant_exponent": wild_p5[
                "twice_max_polynomial_discriminant_exponent"
            ],
        },
        "resolver": wild_theta["resolver"],
    }
    if wild_authority_compact != {
        "all_factor_rows_stable": True,
        "all_krasner_and_separation_bounds_satisfied": True,
        "all_multiplybacks_satisfied": True,
        "certified_precisions": [900, 950, 1000],
        "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
        "p3": {
            "factor_degrees": [3, 3, 3, 9, 18],
            "global_polynomial_discriminant_exponent": 886,
            "twice_max_polynomial_discriminant_exponent": 538,
        },
        "p5": {
            "factor_degrees": [1, 5, 10, 10, 10],
            "global_polynomial_discriminant_exponent": 746,
            "twice_max_polynomial_discriminant_exponent": 246,
        },
        "resolver": "theta36",
    }:
        raise StrictDataError("wild theta36 compact authority changed")

    surface_report = reports["surface_flint"]["report"]
    order_two_profiles = group_report["order_two_tom_profiles"]
    reflection_bridge = {
        "affine_hessian_units": surface_report[
            "reflection_affine_hessian_units"
        ],
        "all_order_two_profiles": order_two_profiles,
        "critical_points_hensel_lift_uniquely": surface_report[
            "reflection_critical_points_hensel_lift_uniquely"
        ],
        "critical_values_congruent_to_integer_witness_mod_p_squared": surface_report[
            "reflection_critical_values_congruent_to_integer_witness_mod_p_squared"
        ],
        "filtered_orders": [2, 1],
        "inertia_generator_action": "E6_ROOT_REFLECTION",
        "inertia_tame": all(prime % 2 for prime in (283, 1801, Q)),
        "residue_characteristics_odd": surface_report[
            "reflection_residue_characteristics_odd"
        ],
        "selected_inertia_tom_index": 2,
        "smoothing_parameter_valuation_exactly_one": surface_report[
            "reflection_smoothing_parameter_valuation_exactly_one"
        ],
        "unique_geometric_singular_point_each_prime": surface_report[
            "reflection_unique_geometric_singular_point_each_prime"
        ],
    }
    if [
        row["tom_index"] for row in order_two_profiles
        if row["line_orbit_rle"] == [[1, 15], [2, 6]]
        and row["fixed_dimensions_V6_V20"] == [5, 15]
    ] != [2]:
        raise StrictDataError("reflection ToM profile is not unique")

    character_match = group_report["complex_conjugation"][
        "character_table_match"
    ]
    field_signature = pari_report["line_field_signature"]
    theta36_real_root_count = pari_report["theta36_real_root_count"]
    line_involution_target = [
        [1, field_signature[0]],
        [2, field_signature[1]],
    ]
    double_six_involution_target = [
        [1, theta36_real_root_count],
        [2, (36 - theta36_real_root_count) // 2],
    ]
    if (
        arithmetic["archimedean"]["line_orbits_27"]
        != [1] * field_signature[0] + [2] * field_signature[1]
        or arithmetic["archimedean"]["double_six_orbits_36"]
        != [1] * theta36_real_root_count
        + [2] * ((36 - theta36_real_root_count) // 2)
    ):
        raise StrictDataError("archimedean arithmetic orbit cross-binding changed")
    matching_order_two = [
        row["tom_index"]
        for row in order_two_profiles
        if row["line_orbit_rle"] == line_involution_target
        and row["double_six_orbit_rle"] == double_six_involution_target
    ]
    archimedean_authority_chain = {
        "character_table": character_match["character_table_name"],
        "double_six_fixed_count": theta36_real_root_count,
        "element_centralizer_order": character_match[
            "element_centralizer_order"
        ],
        "element_class_order": character_match["element_class_order"],
        "element_class_size": character_match["element_class_size"],
        "field_signature_from_nf": field_signature,
        "line_fixed_count": field_signature[0],
        "matching_element_class_indices": character_match[
            "element_class_matching_indices"
        ],
        "matching_order2_tom_indices": matching_order_two,
        "selected_element_class_index": character_match["element_class_index"],
        "selected_subgroup_tom_index": character_match["subgroup_tom_index"],
        "theta36_real_root_count_from_polsturm": theta36_real_root_count,
    }
    if archimedean_authority_chain != {
        "character_table": "U4(2).2",
        "double_six_fixed_count": 4,
        "element_centralizer_order": 96,
        "element_class_order": 2,
        "element_class_size": 540,
        "field_signature_from_nf": [3, 12],
        "line_fixed_count": 3,
        "matching_element_class_indices": [17],
        "matching_order2_tom_indices": [5],
        "selected_element_class_index": 17,
        "selected_subgroup_tom_index": 5,
        "theta36_real_root_count_from_polsturm": 4,
    }:
        raise StrictDataError("archimedean authority chain changed")

    return {
        "C58_source_contract": source_before,
        "G0_upstream_source_lock": upstream_before,
        "G1_bad_prime_exhaustion": {
            "all_surface_bad_prime_envelope_entries_proven_prime": (
                pari_report["surface_bad_prime_envelope_isprime"] == [True] * 9
            ),
            "divided_discriminant_decimal_newline_sha256": reports["surface_flint"]["report"][
                "divided_discriminant_decimal_newline_sha256"
            ],
            "dual_exact_determinant_engines_agree": True,
            "factorization": arithmetic["macaulay"]["factorization"],
            "reflection_ODP_primes": [283, 1801, Q],
            "reflection_witnesses_sha256": reports["surface_flint"]["report"][
                "reflection_witnesses_sha256"
            ],
            "reflection_chart0_reduced_point_bases_verified": surface_report[
                "reflection_chart0_reduced_point_bases_verified"
            ],
            "surface_bad_prime_envelope": list(SURFACE_BAD_PRIME_ENVELOPE),
            "support_exhausted": True,
        },
        "G2_local_order_exact": {
            "basis_reused_exactly": pari_report["basis_reused_exactly"],
            "field_discriminant_decimal_newline_sha256": pari_report[
                "field_discriminant_decimal_newline_sha256"
            ],
            "field_discriminant_exponents_on_surface_bad_prime_envelope": pari_report[
                "field_discriminant_exponents_on_surface_bad_prime_envelope"
            ],
            "generator_image_proves_oriented_field_identity": pari_report[
                "generator_image_proves_oriented_field_identity"
            ],
            "integral_basis_canonical_sha256": arithmetic["maximal_order"][
                "integral_basis_canonical_sha256"
            ],
            "local_prime_ideals_sha256": pari_report["local_prime_ideals_sha256"],
            "nfcertify_unresolved": pari_report["nfcertify_unresolved"],
            "p2_field_discriminant_exponent": 0,
            "ramified_support": list(RAMIFIED_SUPPORT),
        },
        "G3_dual_action_classification": {
            "decomposition_degrees_alone_leave_two_C3_classes": True,
            "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
            "full_labelled_action_arrays_bound": True,
            "p3_all_tom_decomposition_pattern_hits": p3_all_tom_hits,
            "p3_tame_quotient_filter_excludes_206_as_inertia": (
                next(
                    row
                    for row in tom_exhaustion[
                        "p3_all_tom_decomposition_pattern_hits"
                    ]
                    if row["tom_index"] == 206
                )["tame_quotient_cyclic"]
                is False
            ),
            "p3_valid_decomposition_inertia_pairs": tom_exhaustion[
                "p3_valid_decomposition_inertia_pairs"
            ],
            "p5_all_tom_decomposition_pattern_hits": p5_all_tom_hits,
            "p5_valid_decomposition_inertia_pairs": tom_exhaustion[
                "p5_valid_decomposition_inertia_pairs"
            ],
            "p5_wild_normalizer_filter_unique": p5[
                "wild_normalizer_filter_unique"
            ],
            "tame_theta36_all_precision_factor_multiplybacks": all(
                pari_report["degree36_hensel_product_congruences"]["theta"][
                    str(prime)
                ]
                == [20, 30, 40]
                for prime in (181, 997, 2346241)
            ),
            "tame_theta36_authority_precision": 40,
            "tame_theta36_factor_krasner_bound_satisfied": True,
            "tame_theta36_global_polynomial_discriminant_exponent": 24,
            "tame_theta36_local_discriminant_exponent": 24,
            "tame_theta36_local_rows": [[3, 3, 1, 2], [6, 3, 2, 2], [9, 3, 3, 2], [18, 3, 6, 2]],
            "tame_theta36_prime_scope": [181, 997, 2346241],
            "tame_theta36_resolver_separation_bound_satisfied": True,
            "tame_theta36_twice_max_polynomial_discriminant_exponent": 24,
            "tame_theta36_uniquely_selects_fixed_point_free_C3": True,
            "tame_C3_selected_tom_index": 6,
            "wild_degree36_theta_authority": wild_authority_compact,
        },
        "G4_filtered_inertia": {
            "p3": {
                "deep_C3_exhaustion": deep_C3_exhaustion,
                "deep_C3_normal_in_all_surviving_decomposition_groups": p3[
                    "deep_C3_normal_in_all_surviving_decomposition_groups"
                ],
                "decomposition_orders_not_resolved": [18, 36],
                "filtration_multiplicity_solution": {
                    "deep_C3_layers": 6,
                    "unique": p3_equation["unique"],
                    "wild_C3_squared_layers": 1,
                },
                "filtered_orders": [18, 9] + [3] * 6 + [1],
                "inertia_tom_index": 140,
                "serre_last_nonzero_grade": 7,
                "serre_required_action": "inversion",
            },
            "p5": {
                "filtration_equation": p5_filtration_equation,
                "filtration_multiplicity_solution": {
                    "unique": p5_equation["unique"],
                    "wild_C5_layers": 3,
                },
                "filtered_orders": [20] + [5] * 3 + [1],
                "inertia_and_decomposition_tom_index": 147,
            },
            "reflection": {"filtered_orders": [2, 1]},
            "reflection_picard_lefschetz_bridge": reflection_bridge,
            "tame_C3": {"filtered_orders": [3, 1], "inertia_tom_index": 6},
        },
        "G5_character_conductors": {
            "p3": {
                "artin_V6_V20": [11, 35],
                "swan_V6_V20": [5, 18],
            },
            "p5": {
                "artin_V6_V20": [7, 29],
                "swan_V6_V20": [3, 12],
            },
            "reflection_C2": {"artin_V6_V20": [1, 5], "swan_V6_V20": [0, 0]},
            "tame_C3": {"artin_V6_V20": [6, 12], "swan_V6_V20": [0, 0]},
        },
        "G6_global_and_infinity": {
            "archimedean": arithmetic["archimedean"],
            "archimedean_authority_chain": archimedean_authority_chain,
            "conductor_discriminant_identity_E": True,
            "conductors": {
                "V6": {
                    "factorization_exponents_3_5_A_B": [11, 7, 6, 1],
                    "decimal_newline_sha256": decimal_guard(conductor6)[
                        "decimal_newline_sha256"
                    ],
                    "digits": decimal_guard(conductor6)["digits"],
                    "positive": decimal_guard(conductor6)["positive"],
                },
                "V20": {
                    "factorization_exponents_3_5_A_B": [35, 29, 12, 5],
                    "decimal_newline_sha256": decimal_guard(conductor20)[
                        "decimal_newline_sha256"
                    ],
                    "digits": decimal_guard(conductor20)["digits"],
                    "positive": decimal_guard(conductor20)["positive"],
                },
            },
            "disc_E": {
                "exponents_on_surface_bad_prime_envelope": list(FIELD_EXPONENTS),
                "decimal_newline_sha256": decimal_guard(disc_e)[
                    "decimal_newline_sha256"
                ],
                "digits": decimal_guard(disc_e)["digits"],
                "positive": decimal_guard(disc_e)["positive"],
            },
            "disc_K": {
                "factorization_exponents_by_type": normal_exponents,
                "decimal_newline_sha256": disc_k_guard[
                    "decimal_newline_sha256"
                ],
                "digits": disc_k_guard["digits"],
                "positive": disc_k_guard["positive"],
            },
            "normal_closure_ramified_support": list(RAMIFIED_SUPPORT),
            "p2_normal_closure_unramified_from_zero_permutation_discriminant_and_faithful_action": True,
            "support_exhausted_by_exact_DiscE_and_faithful_action": True,
        },
        "G7_replay_and_scope": {
            "all_evidence_and_source_snapshots_equal_before_after": True,
            "producer_exact_report_sha256": {
                key: value["report_sha256"] for key, value in sorted(reports.items())
            },
            "raw_huge_CHANGE_excluded_from_formal_output": True,
            "runtime_and_absolute_paths_excluded": True,
        },
        "artifact_contract": artifacts_before,
        "backends": backends,
        "documentation_contract": {
            "later_document_and_paper_freeze_requires_external_full_project_manifest": True,
            "paper_bytes_are_machine_certificate_inputs": False,
            "root_document_bytes_are_machine_certificate_inputs": False,
            "status": "PAPER_PENDING",
        },
        "nonresults_firewall": {
            "delta36_local_lane": {
                "certificate_dependency": False,
                "reason": "precision_40_below_global_polynomial_discriminant_exponent_840",
                "status": "BOUNDED_NON_RESULT_NONDEPENDENCY",
            },
            "p3_decomposition_order": {
                "allowed_values": [18, 36],
                "character_conductor_dependency": False,
                "status": "UNRESOLVED_NONDEPENDENCY",
            },
        },
        "scope_firewall": {
            "arithmetic_equivalence_claimed": False,
            "Artin_holomorphy_claimed": False,
            "automorphy_claimed": False,
            "bad_Euler_factors_beyond_filtered_inertia_claimed": False,
            "Brauer_Manin_obstruction_claimed": False,
            "Calabi_Yau_realization_claimed": False,
            "decomposition_Frobenius_claimed": False,
            "delta36_local_factorization_used_as_authority": False,
            "dynamics_claimed": False,
            "general_cubic_surface_theorem_claimed": False,
            "general_line_field_theorem_claimed": False,
            "Hilbert_Polya_operator_claimed": False,
            "local_root_numbers_claimed": False,
            "local_epsilon_factors_claimed": False,
            "p3_decomposition_order_unique_claimed": False,
            "paper_complete_claimed": False,
            "rational_or_local_points_claimed": False,
            "release_claimed": False,
            "Riemann_Hypothesis_claimed": False,
            "VHS_realization_claimed": False,
        },
        "status_contract": {
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "documentation_status": "PAPER_PENDING",
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "project_release_status": "PAPER_PENDING",
            "promotion_authorized": False,
        },
    }


def shape_value(value: Any) -> Any:
    if type(value) is dict:
        return {key: shape_value(value[key]) for key in sorted(value)}
    if type(value) is list:
        return [len(value), [shape_value(item) for item in value]]
    if value is None:
        return "null"
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is str:
        return "str"
    raise StrictDataError(f"unsupported payload leaf type: {type(value).__name__}")


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(item) for item in value)
    if value is None or type(value) in (bool, int, str):
        return 1
    raise StrictDataError(f"unsupported payload leaf type: {type(value).__name__}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-output", type=Path, required=True)
    parser.add_argument("--pari-python", type=Path, default=Path("/usr/bin/python3"))
    parser.add_argument(
        "--flint-group-python",
        type=Path,
        default=Path("/root/miniconda3/bin/python3"),
    )
    parser.add_argument("--gap", type=Path, default=Path("/usr/bin/gap"))
    arguments = parser.parse_args()
    if (
        arguments.output.name != "c58_certificate.json"
        or arguments.schema_output.name != "c58_schema.json"
    ):
        raise StrictDataError("producer output basenames are fixed")
    protected = [arguments.artifact_dir / name for name in ARTIFACT_NAMES]
    protected.extend(path for path in CODE.iterdir() if path.is_file())
    protected.extend(
        contract[key]
        for contract in UPSTREAM.values()
        for key in ("inventory", "certificate", "check_report", "scoped_manifest")
        if key in contract
    )
    outputs = prepare_output_targets(
        (arguments.output, arguments.schema_output), protected=protected
    )
    try:
        reject_optimized_python()
        payload = build_payload(
            arguments.artifact_dir,
            arguments.pari_python,
            arguments.flint_group_python,
            arguments.gap,
        )
        if set(payload) != set(PAYLOAD_KEYS):
            raise StrictDataError("C58 payload top-level key contract changed")
        shape = shape_value(payload)
        schema = {
            "booleans_rejected_in_integer_slots": True,
            "duplicate_keys_rejected": True,
            "floats_rejected": True,
            "gzip_mtime_zero_and_deterministic_recompression_required": True,
            "max_certificate_bytes": 5_000_000,
            "non_UTF8_rejected": True,
            "noncanonical_integers_rejected": True,
            "optimized_python_rejected": True,
            "oversized_input_rejected": True,
            "payload_scalar_leaf_count": scalar_leaf_count(payload),
            "payload_shape_sha256": sha256_bytes(canonical_leaf_bytes(shape)),
            "payload_top_level_keys": sorted(payload),
            "schema_id": "hcs-c58-certificate-schema-v1",
            "unknown_fields_rejected_by_full_leaf_rebuild": True,
        }
        schema_raw = canonical_json_bytes(schema, pretty=True)
        envelope = {
            "canonical_schema_sha256": sha256_bytes(canonical_leaf_bytes(schema)),
            "paper_status": "PAPER_PENDING",
            "payload": payload,
            "payload_sha256": sha256_bytes(canonical_leaf_bytes(payload)),
            "schema_descriptor_id": "hcs-c58-certificate-schema-v1",
            "schema_id": "hcs-c58-certificate-v1",
            "schema_sha256": sha256_bytes(schema_raw),
            "status": "PREFREEZE_CODE_RESULTS_PASS",
        }
        raw = canonical_json_bytes(envelope, pretty=True)
        if len(raw) > 5_000_000 or len(schema_raw) > 100_000:
            raise StrictDataError("generated certificate or schema exceeds byte ceiling")
        final_source = source_contract()
        final_upstream = upstream_source_lock()
        final_artifacts, _, _ = artifact_contract(arguments.artifact_dir)
        if not deep_exact(payload["C58_source_contract"], final_source):
            raise StrictDataError("C58 source changed before final producer writes")
        if not deep_exact(payload["G0_upstream_source_lock"], final_upstream):
            raise StrictDataError("upstream source changed before final producer writes")
        if not deep_exact(payload["artifact_contract"], final_artifacts):
            raise StrictDataError("immutable evidence changed before final producer writes")
        atomic_write(outputs[1], schema_raw)
        atomic_write(outputs[0], raw)
    except BaseException:
        for output in outputs:
            if output.exists() and output.is_file() and not output.is_symlink():
                output.unlink()
        raise
    print("HCS-C58 PRODUCER PASS PREFREEZE")
    print(f"certificate_sha256={hashlib.sha256(raw).hexdigest()}")
    print(f"payload_sha256={envelope['payload_sha256']}")


if __name__ == "__main__":
    main()
