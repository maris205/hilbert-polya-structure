#!/usr/bin/env python3
"""Independent full-leaf checker for the HCS-C58 ramification package.

Independence boundary
---------------------
The checker imports only producer-neutral exact-I/O and backend-preflight
modules.  It rebuilds the Macaulay discriminant with checker-owned integer
Bareiss elimination, reconstructs the labelled W(E6) carriers and exhausts
the relevant table-of-marks classes in checker-owned GAP, initializes PARI
from the raw certified integral basis, and derives the conductor and global
discriminant formulae with exact rational arithmetic.  No producer theorem
helper is imported or executed.
"""

from __future__ import annotations

import argparse
import ast
from collections import deque
from copy import deepcopy
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, Iterable

from c58_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deep_exact,
    deterministic_gzip,
    prepare_output_targets,
    read_stable,
    reject_optimized_python,
    require_bool,
    require_canonical_compact_json,
    require_exact_keys,
    require_int,
    require_sha256,
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
C55 = REPO / "henon_dynamics/henon_mu3_rational_yukawa_surface"
C56 = REPO / "henon_dynamics/henon_mu3_yukawa_line_field"
C57 = REPO / "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump"
C55_CERTIFICATE = C55 / "results/c55_certificate.json"
C56_CERTIFICATE = C56 / "results/c56_certificate.json"
C57_CERTIFICATE = C57 / "results/c57_certificate.json"
UPSTREAM_RELEASE_COMMIT = "7775269a4cab9c85e291a719eb561cec188ede09"
UPSTREAM_PROJECT_RELEASES = {
    "C55": "c124ba53c3d89514a00b0949e62b645228dbcfc5",
    "C56": "a55f31dca338d1e3757704b8c95d11e28c9c98d4",
    "C57": UPSTREAM_RELEASE_COMMIT,
}

UPSTREAM_FILES = {
    "henon_dynamics/henon_mu3_rational_yukawa_surface/code/c55_checker.py": (
        "61fb7a7fcc71a9fdda534da35567b8618d574806",
        "38d7c144389ba116fc9f6d52bb4327cbe4479f7b7ac71f447c406e69c633834b",
    ),
    "henon_dynamics/henon_mu3_rational_yukawa_surface/results/c55_certificate.json": (
        "cc9ba0728c2931477a9cca082e7d8e8f62d9f7b8",
        "aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f",
    ),
    "henon_dynamics/henon_mu3_rational_yukawa_surface/results/ARTIFACT_HASHES.sha256": (
        "1f0e0e3bb7a5bd89fbd0c7221c081384136f4318",
        "8b9a935bddb4aee04561860491eb982311b6776e250b41c8598336fe6bfc2fc9",
    ),
    "henon_dynamics/henon_mu3_yukawa_line_field/code/c56_checker.py": (
        "05eaa9001c9138c4429c1d369d14dade96e9d09c",
        "83923b42662bb1368380271bf83476966dbd6c0522a78d7b0b86cafb1e1bfd63",
    ),
    "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json": (
        "d8c9faa272682bf9403605c59fcef09fcccbe000",
        "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4",
    ),
    "henon_dynamics/henon_mu3_yukawa_line_field/FULL_PROJECT_HASHES.sha256": (
        "43f5ebb68a7c489c0bb1e1de6ec69bb6dd1ff34d",
        "26e3e4226cd1baea14543f14bac9ffd060ed8031741cb1ec0a38e22cd07487f4",
    ),
    "henon_dynamics/henon_mu3_yukawa_line_field/results/scoped_hash_manifest.json": (
        "e287006599be564b617ba92bf948b253a695bddd",
        "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/code/c57_group.py": (
        "e150d3c4a9e11d86f92a45949792cdc7d3e267c0",
        "01608cc60b38e5283e575a4e5f2176af9421b018c297bbee2f266df482ee359d",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results/c57_certificate.json": (
        "377d773af8a7348f99de69a7a57f98cbcc6a31e6",
        "3078baf167d2344982d9f93811f1fd59a8258c8178ecce4decbd2b054b16092f",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/FULL_PROJECT_HASHES.sha256": (
        "dc6c6b9557aba6770d48cab0752a2f4076b8185e",
        "140bbc3dcc723c533b62512dd2f21cd47bd32fc26a4e2cf7344a9aa070872745",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results/c57_check_report.json": (
        "f8f1e72c4ad2ffb45dd25323fac1360d649802fd",
        "fb0afb77f130fb2d0a792af8d949e5c1a8e1b7864525dd62f1d1a41d99a79bcf",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results/delta_crt.json.gz": (
        "100d3ef7bdc1a4aeddef102fcb7ac3e84ea04370",
        "4deead9914f31b0012afd91088339793330874a3b5156ceaeb1371fcb495f685",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results/scoped_hash_manifest.json": (
        "79c0c510c574219934f511e66f99e7f08ea20297",
        "864c05b18e0bdcafbc5b5e3206840a1b25afa355b9737ebcc9d1806e33fcec5d",
    ),
    "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/results/theta_crt.json.gz": (
        "bbbd792e3d418d917ecaa22bee11d39d4dad1d76",
        "91181a525e0acb17e73d2e96fd4e7d5d7a25913784ef8ad9d3be59c430a4fadd",
    ),
}

CUBIC_TERMS = (
    (75081586157, (3, 0, 0, 0)),
    (-28576620789, (2, 1, 0, 0)),
    (-122000922135, (2, 0, 1, 0)),
    (-5364921951, (2, 0, 0, 1)),
    (164150208636, (1, 2, 0, 0)),
    (-415458334296, (1, 1, 1, 0)),
    (151070718312, (1, 1, 0, 1)),
    (1158143874300, (1, 0, 2, 0)),
    (114691988016, (1, 0, 1, 1)),
    (113572676646, (1, 0, 0, 2)),
    (6898957820, (0, 3, 0, 0)),
    (1132596902196, (0, 2, 1, 0)),
    (-30413540316, (0, 2, 0, 1)),
    (-2054867641020, (0, 1, 2, 0)),
    (151980984216, (0, 1, 1, 1)),
    (36794420832, (0, 1, 0, 2)),
    (2646295985484, (0, 0, 3, 0)),
    (560186573940, (0, 0, 2, 1)),
    (706181383584, (0, 0, 1, 2)),
    (1884468968, (0, 0, 0, 3)),
)

LARGE_REFLECTION_PRIME = 14932047182473291995860108491583652133938007263719
SUPPORT = (2, 3, 5, 181, 283, 997, 1801, 2346241, LARGE_REFLECTION_PRIME)
DIRECT_PRIMES = (3, 5, 181, 997, 2346241)
C3_PRIMES = (181, 997, 2346241)
REFLECTION_PRIMES = (283, 1801, LARGE_REFLECTION_PRIME)
FIELD_DISCRIMINANT_EXPONENTS = (0, 46, 36, 18, 6, 18, 6, 18, 6)
WILD_THETA_AUTHORITY_EXPECTED = {
    "authority_role": "KRASNER_CERTIFIED_AUTHORITY",
    "certified_precisions": [900, 950, 1000],
    "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
    "prime_records": {
        "3": {
            "all_factors_monic_simple": True,
            "authority_bound_satisfied": True,
            "factor_degree_multiplicities": [[3, 3], [9, 1], [18, 1]],
            "factor_krasner_bounds_satisfied": [True, True, True],
            "factor_rows": [
                {
                    "count": 3,
                    "factor_degree": 3,
                    "mod_p_factor_exponent": 3,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 11,
                },
                {
                    "count": 1,
                    "factor_degree": 9,
                    "mod_p_factor_exponent": 9,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 62,
                },
                {
                    "count": 1,
                    "factor_degree": 18,
                    "mod_p_factor_exponent": 18,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 269,
                },
            ],
            "factor_rows_stable_across_precisions": True,
            "global_polynomial_discriminant_exponent": 886,
            "minimum_multiplyback_valuations": [900, 950, 1000],
            "resolver_separation_bounds_satisfied": [True, True, True],
            "twice_max_polynomial_discriminant_exponent": 538,
        },
        "5": {
            "all_factors_monic_simple": True,
            "authority_bound_satisfied": True,
            "factor_degree_multiplicities": [[1, 1], [5, 1], [10, 3]],
            "factor_krasner_bounds_satisfied": [True, True, True],
            "factor_rows": [
                {
                    "count": 1,
                    "factor_degree": 1,
                    "mod_p_factor_exponent": 1,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 0,
                },
                {
                    "count": 1,
                    "factor_degree": 5,
                    "mod_p_factor_exponent": 5,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 27,
                },
                {
                    "count": 3,
                    "factor_degree": 10,
                    "mod_p_factor_exponent": 10,
                    "mod_p_irreducible_factor_degree": 1,
                    "polynomial_discriminant_exponent": 123,
                },
            ],
            "factor_rows_stable_across_precisions": True,
            "global_polynomial_discriminant_exponent": 746,
            "minimum_multiplyback_valuations": [900, 950, 1000],
            "resolver_separation_bounds_satisfied": [True, True, True],
            "twice_max_polynomial_discriminant_exponent": 246,
        },
    },
    "resolver": "theta36",
}
SURFACE_FACTORIZATION = (
    (2, 64),
    (3, 43),
    (5, 7),
    (181, 24),
    (283, 1),
    (997, 24),
    (1801, 1),
    (2346241, 24),
    (LARGE_REFLECTION_PRIME, 1),
)
REFLECTION_WITNESSES = {
    283: {
        "point": [1, 66, 155, 125],
        "hessian": 228,
        "quotient": 212,
    },
    1801: {
        "point": [1, 1437, 538, 511],
        "hessian": 1387,
        "quotient": 818,
    },
    LARGE_REFLECTION_PRIME: {
        "point": [
            1,
            13510103813129040670509336985505882430772547129082,
            9804662502886869685787960537224283370301790578288,
            2060004063224680714367389988490103248145804244874,
        ],
        "hessian": 6136116089260018682592250996037036352166217747437,
        "quotient": 11651769163508833344099877335703302197941640200357,
    },
}

ARTIFACT_NAMES = (
    "c58_arithmetic_evidence.json.gz",
    "c58_group_evidence.json",
)
ARTIFACT_BYTE_AUTHORITY = {
    "c58_arithmetic_evidence.json.gz": {
        "decompressed_sha256": "816b8f11358c266826c3ab7117705e5d8fc2426ad373c08a47026d0ee534cd3d",
        "decompressed_size_bytes": 4_899_976,
        "sha256": "e374d328a7937c48af93e0b46f54eead5a878f01acc161d8053fe4a10c5f6128",
        "size_bytes": 1_952_334,
    },
    "c58_group_evidence.json": {
        "sha256": "0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd",
        "size_bytes": 128_642,
    },
}
PRODUCER_EXACT_REPORT_SHA256 = {
    "arithmetic": "35f2aeee2da982b1ee85ef76332114071276cd2b3562a1c11939d41c8cfb1655",
    "group": "a6f7144393f3ae84b993c25c368a639a865fc85d84b655af7df9dbb2741be18e",
    "surface_bareiss": "3183c4313561d1f2c78c13947a8c08aedc0912164ff64928f3ce31cec6de7dcd",
    "surface_flint": "e3486468f657746b0614efba5cea50064011d978785b5d585a76cd2fb1c6760a",
}
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
CODE_SOURCE_NAMES = {
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
}
if len(CODE_SOURCE_NAMES) != 14:
    raise RuntimeError("C58 exact code allowlist must contain 14 paths")


def canonical_pretty(raw: bytes, *, max_bytes: int, label: str) -> Any:
    value = strict_json_loads(raw, max_bytes=max_bytes)
    if raw != canonical_json_bytes(value, pretty=True):
        raise StrictDataError(f"{label} is not canonical pretty JSON")
    return value


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


def verify_full_sha_manifest(
    project: Path,
    manifest_relative: str,
    expected_sha256: str,
    expected_entries: int,
) -> dict[str, Any]:
    manifest_path = project / manifest_relative
    raw, fingerprint = read_stable(manifest_path, max_bytes=1_000_000)
    if fingerprint.sha256 != expected_sha256 or not raw.endswith(b"\n"):
        raise StrictDataError(f"upstream full manifest digest/termination mismatch: {project.name}")
    try:
        lines = raw.decode("utf-8", errors="strict").splitlines()
    except UnicodeDecodeError as exc:
        raise StrictDataError("upstream full manifest is not UTF-8") from exc
    if len(lines) != expected_entries:
        raise StrictDataError(f"upstream full manifest entry count mismatch: {project.name}")
    declared: dict[str, str] = {}
    manifest_entries = []
    for line in lines:
        if len(line) < 67 or line[64:66] != "  ":
            raise StrictDataError("upstream full manifest line grammar mismatch")
        digest, relative = line[:64], line[66:]
        require_sha256(digest, "upstream manifest entry digest")
        if not safe_relative_path(relative) or relative in declared:
            raise StrictDataError("unsafe/duplicate upstream manifest path")
        declared[relative] = digest
        entry_raw, entry_fingerprint = read_stable(project / relative, max_bytes=500_000_000)
        if entry_fingerprint.sha256 != digest or len(entry_raw) != entry_fingerprint.size_bytes:
            raise StrictDataError(f"upstream full manifest entry mismatch: {relative}")
        manifest_entries.append(
            {"path": relative, "sha256": digest, "size_bytes": len(entry_raw)}
        )
    manifest_normalized = str(Path(manifest_relative).as_posix())
    live = {
        str(path.relative_to(project).as_posix())
        for path in project.rglob("*")
        if path.is_file() and not path.is_symlink() and str(path.relative_to(project).as_posix()) != manifest_normalized
    }
    symlinks_or_nonfiles = [
        path
        for path in project.rglob("*")
        if path.is_symlink() or (not path.is_dir() and not path.is_file())
    ]
    allowed_directories = set()
    for relative in (*declared, manifest_normalized):
        for parent in Path(relative).parents:
            normalized = str(parent.as_posix())
            if normalized != ".":
                allowed_directories.add(normalized)
    live_directories = {
        str(path.relative_to(project).as_posix())
        for path in project.rglob("*")
        if path.is_dir() and not path.is_symlink()
    }
    if (
        symlinks_or_nonfiles
        or live != set(declared)
        or live_directories != allowed_directories
    ):
        raise StrictDataError(
            f"upstream full inventory mismatch {project.name}; "
            f"missing={sorted(set(declared)-live)} extra={sorted(live-set(declared))}; "
            f"missing_dirs={sorted(allowed_directories-live_directories)} "
            f"extra_dirs={sorted(live_directories-allowed_directories)}"
        )
    return {
        "entry_count": len(declared),
        "inventory_exact_excluding_self": True,
        "entries": manifest_entries,
        "manifest_path": str((project / manifest_relative).relative_to(REPO)),
        "manifest_sha256": fingerprint.sha256,
    }


def verify_scoped_json_manifest(project: Path, expected_sha256: str) -> dict[str, Any]:
    path = project / "results/scoped_hash_manifest.json"
    raw, fingerprint = read_stable(path, max_bytes=1_000_000)
    if fingerprint.sha256 != expected_sha256:
        raise StrictDataError("upstream scoped manifest digest mismatch")
    value = canonical_pretty(raw, max_bytes=1_000_000, label="upstream scoped manifest")
    require_exact_keys(
        value,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        "upstream scoped manifest",
    )
    if (
        value["manifest_self_included"] is not False
        or type(value["entry_count"]) is not int
        or value["entry_count"] != len(value["entries"])
        or value["status"] != "PREFREEZE_CODE_RESULTS_PASS"
    ):
        raise StrictDataError("upstream scoped manifest header mismatch")
    declared = set()
    for entry in value["entries"]:
        require_exact_keys(entry, {"path", "sha256", "size_bytes"}, "scoped manifest entry")
        relative = entry["path"]
        if not safe_relative_path(relative) or relative in declared:
            raise StrictDataError("unsafe/duplicate scoped manifest path")
        declared.add(relative)
        raw_entry, observed = read_stable(project / relative, max_bytes=500_000_000)
        if observed.sha256 != entry["sha256"] or len(raw_entry) != entry["size_bytes"]:
            raise StrictDataError(f"scoped manifest entry mismatch: {relative}")
    live = set()
    live_directories = set()
    for root_name in ("code", "results"):
        for child in (project / root_name).rglob("*"):
            if child.is_symlink() or (not child.is_dir() and not child.is_file()):
                raise StrictDataError("upstream scoped inventory contains a special file")
            if child.is_file():
                relative = str(child.relative_to(project).as_posix())
                if relative != "results/scoped_hash_manifest.json":
                    live.add(relative)
            elif child.is_dir():
                live_directories.add(str(child.relative_to(project).as_posix()))
    allowed_directories = {"code", "results"}
    for relative in (*declared, "results/scoped_hash_manifest.json"):
        for parent in Path(relative).parents:
            normalized = str(parent.as_posix())
            if normalized != ".":
                allowed_directories.add(normalized)
    if live != declared or live_directories != allowed_directories - {"code", "results"}:
        raise StrictDataError(
            f"upstream scoped inventory mismatch; missing={sorted(declared-live)} "
            f"extra={sorted(live-declared)}; "
            f"missing_dirs={sorted((allowed_directories-{'code','results'})-live_directories)} "
            f"extra_dirs={sorted(live_directories-(allowed_directories-{'code','results'}))}"
        )
    return {
        "entry_count": len(declared),
        "inventory_exact_excluding_self": True,
        "manifest_path": str(path.relative_to(REPO)),
        "manifest_sha256": fingerprint.sha256,
    }


def verify_upstream_semantic_statuses() -> dict[str, Any]:
    paths = {
        "C55_certificate": C55 / "results/c55_certificate.json",
        "C55_check": C55 / "results/independent_check.json",
        "C56_certificate": C56 / "results/c56_certificate.json",
        "C56_check": C56 / "results/c56_check_report.json",
        "C57_certificate": C57 / "results/c57_certificate.json",
        "C57_check": C57 / "results/c57_check_report.json",
    }
    values: dict[str, dict[str, Any]] = {}
    fingerprints = {}
    for name, path in paths.items():
        raw, fingerprint = read_stable(path, max_bytes=4_000_000)
        value = canonical_pretty(raw, max_bytes=4_000_000, label=name)
        if type(value) is not dict:
            raise StrictDataError(f"{name} is not an object")
        values[name] = value
        fingerprints[name] = fingerprint

    c55 = values["C55_certificate"]
    c55_check = values["C55_check"]
    if (
        c55.get("schema") != "hcs-c55-certificate-v1"
        or c55.get("payload_sha256")
        != sha256_bytes(canonical_leaf_bytes(c55.get("payload")))
        or c55.get("payload", {}).get("artifact_status") != "RELEASE_CANDIDATE"
        or c55.get("payload", {}).get("material_passport", {}).get("verification_status")
        != "REPRODUCIBLE_EXACT_COMPUTATION"
        or c55_check.get("schema") != "hcs-c55-independent-check-v1"
        or c55_check.get("result") != "PASS"
        or c55_check.get("semantic_gate_count") != 13
        or c55_check.get("certificate_sha256") != fingerprints["C55_certificate"].sha256
        or c55_check.get("payload_sha256") != c55.get("payload_sha256")
    ):
        raise StrictDataError("C55 semantic release/check status mismatch")

    c56 = values["C56_certificate"]
    c56_check = values["C56_check"]
    if (
        c56.get("schema", {}).get("schema_id") != "hcs-c56-certificate-schema-v1"
        or c56.get("payload_sha256")
        != sha256_bytes(canonical_leaf_bytes(c56.get("payload")))
        or c56.get("payload", {}).get("theorem_gates", {}).get("final_status")
        != "PREFREEZE_CODE_RESULTS_PASS"
        or c56_check.get("schema") != "hcs-c56-independent-check-v1"
        or c56_check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        or c56_check.get("semantic_gate_count") != 10
        or len(c56_check.get("executed_gates", [])) != 10
        or c56_check.get("scalar_leaf_rebound", {}).get("rebound_mutations_rejected")
        != 2684
        or c56_check.get("certificate_sha256") != fingerprints["C56_certificate"].sha256
        or c56_check.get("payload_sha256") != c56.get("payload_sha256")
    ):
        raise StrictDataError("C56 semantic release/check status mismatch")

    c57 = values["C57_certificate"]
    c57_check = values["C57_check"]
    if (
        c57.get("schema_id") != "hcs-c57-certificate-v1"
        or c57.get("status") != "PREFREEZE_CODE_RESULTS_PASS"
        or c57.get("paper_status") != "PAPER_PENDING"
        or c57.get("payload_sha256")
        != sha256_bytes(canonical_leaf_bytes(c57.get("payload")))
        or c57.get("payload", {}).get("status_contract")
        != {
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "documentation_status": "PAPER_PENDING",
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "project_release_status": "PAPER_PENDING",
            "promotion_authorized": False,
        }
        or c57_check.get("schema_id") != "hcs-c57-independent-check-v1"
        or c57_check.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        or c57_check.get("executed_gates") != [f"G{index}" for index in range(8)]
        or c57_check.get("theorem_gate_count") != 8
        or c57_check.get("full_semantic_leaf_rebuild") is not True
        or c57_check.get("scalar_leaf_rebound", {}).get("rebound_mutations_rejected")
        != 535
        or c57_check.get("certificate_sha256") != fingerprints["C57_certificate"].sha256
        or c57_check.get("payload_sha256") != c57.get("payload_sha256")
    ):
        raise StrictDataError("C57 semantic release/check status mismatch")
    return {
        "C55": {
            "certificate_status": "RELEASE_CANDIDATE",
            "check_result": "PASS",
            "semantic_gate_count": 13,
        },
        "C56": {
            "certificate_status": "PREFREEZE_CODE_RESULTS_PASS",
            "check_result": "PASS_PREFREEZE_CODE_RESULTS",
            "semantic_gate_count": 10,
        },
        "C57": {
            "certificate_status": "PREFREEZE_CODE_RESULTS_PASS",
            "check_result": "PASS_PREFREEZE_CODE_RESULTS",
            "rebound_mutations_rejected": 535,
            "theorem_gate_count": 8,
        },
    }


def rebuild_g0_upstream_lock() -> dict[str, Any]:
    projects = {"C55": C55, "C56": C56, "C57": C57}
    for name, project in projects.items():
        release = UPSTREAM_PROJECT_RELEASES[name]
        relative = str(project.relative_to(REPO))
        if git("merge-base", "--is-ancestor", release, "HEAD", check=False).returncode:
            raise StrictDataError(f"frozen {name} release is not an ancestor of HEAD")
        if git("diff", "--quiet", release, "--", relative, check=False).returncode:
            raise StrictDataError(f"live/index {name} differs from its frozen release")
    # Extra file/blob anchors are checker-owned provenance controls and are
    # deliberately verified without being copied into the producer-shaped G0
    # payload below.
    for relative, (blob, digest) in sorted(UPSTREAM_FILES.items()):
        raw, fingerprint = read_stable(REPO / relative, max_bytes=10_000_000)
        if fingerprint.sha256 != digest:
            raise StrictDataError(f"upstream SHA mismatch: {relative}")
        tokens = git("ls-tree", UPSTREAM_RELEASE_COMMIT, "--", relative).stdout.decode().split()
        if len(tokens) != 4 or tokens[2] != blob or tokens[3] != relative:
            raise StrictDataError(f"upstream git blob mismatch: {relative}")
    full_manifests = [
        verify_full_sha_manifest(
            C55,
            "results/ARTIFACT_HASHES.sha256",
            "8b9a935bddb4aee04561860491eb982311b6776e250b41c8598336fe6bfc2fc9",
            47,
        ),
        verify_full_sha_manifest(
            C56,
            "FULL_PROJECT_HASHES.sha256",
            "26e3e4226cd1baea14543f14bac9ffd060ed8031741cb1ec0a38e22cd07487f4",
            46,
        ),
        verify_full_sha_manifest(
            C57,
            "FULL_PROJECT_HASHES.sha256",
            "140bbc3dcc723c533b62512dd2f21cd47bd32fc26a4e2cf7344a9aa070872745",
            64,
        ),
    ]
    scoped_manifests = [
        verify_scoped_json_manifest(
            C56, "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a"
        ),
        verify_scoped_json_manifest(
            C57, "864c05b18e0bdcafbc5b5e3206840a1b25afa355b9737ebcc9d1806e33fcec5d"
        ),
    ]
    statuses = verify_upstream_semantic_statuses()
    output_projects = {}
    for index, name in enumerate(("C55", "C56", "C57")):
        project = projects[name]
        certificate_path = project / f"results/{name.lower()}_certificate.json"
        certificate_raw, certificate_fingerprint = read_stable(
            certificate_path, max_bytes=4_000_000
        )
        certificate = canonical_pretty(
            certificate_raw, max_bytes=4_000_000, label=f"{name} certificate"
        )
        full = full_manifests[index]
        value = {
            "certificate_payload_sha256": certificate["payload_sha256"],
            "certificate_semantic_status": statuses[name]["certificate_status"],
            "certificate_sha256": certificate_fingerprint.sha256,
            "full_inventory_entries": full["entries"],
            "full_inventory_entry_count": full["entry_count"],
            "full_inventory_exact_live_rebind": True,
            "full_inventory_sha256": full["manifest_sha256"],
            "release_commit": UPSTREAM_PROJECT_RELEASES[name],
            "release_is_ancestor_of_HEAD": True,
            "tracked_subtree_unchanged": True,
        }
        if name in ("C56", "C57"):
            check_path = project / f"results/{name.lower()}_check_report.json"
            check_raw, check_fingerprint = read_stable(check_path, max_bytes=4_000_000)
            check = canonical_pretty(
                check_raw, max_bytes=4_000_000, label=f"{name} check report"
            )
            scoped_path = project / "results/scoped_hash_manifest.json"
            scoped_raw, scoped_fingerprint = read_stable(scoped_path, max_bytes=1_000_000)
            value.update(
                {
                    "check_report_result": check["result"],
                    "check_report_sha256": check_fingerprint.sha256,
                    "check_report_size_bytes": len(check_raw),
                    "scoped_manifest_sha256": scoped_fingerprint.sha256,
                    "scoped_manifest_size_bytes": len(scoped_raw),
                }
            )
        output_projects[name] = value
    return {
        "all_three_full_live_inventories_rebound": True,
        "upstream_projects": output_projects,
    }


def load_upstream_inputs() -> tuple[
    list[int], list[list[Any]], dict[str, Any], dict[str, list[int]]
]:
    raw, _ = read_stable(C56_CERTIFICATE, max_bytes=10_000_000)
    certificate = canonical_pretty(raw, max_bytes=10_000_000, label="C56 certificate")
    try:
        surface_rows = certificate["payload"]["surface"]["primitive_coefficients"]
        eliminant = certificate["payload"]["irreducibility"][
            "eliminant_coefficients_d_0_to_27"
        ]
    except (KeyError, TypeError) as exc:
        raise StrictDataError("C56 certificate lacks frozen surface/eliminant") from exc
    cubic = [
        [row["coefficient"], row["exponents_u0_to_u3"]] for row in surface_rows
    ]
    expected_cubic = [[coefficient, list(exponents)] for coefficient, exponents in CUBIC_TERMS]
    if not deep_exact(cubic, expected_cubic):
        raise StrictDataError("C56 cubic does not equal the checker-owned frozen cubic")
    if (
        type(eliminant) is not list
        or len(eliminant) != 28
        or any(type(value) is not int for value in eliminant)
    ):
        raise StrictDataError("C56 eliminant coefficient carrier is malformed")
    resolvers: dict[str, list[int]] = {}
    for name, expected_sha, expected_coefficient_sha in (
        (
            "delta",
            "4deead9914f31b0012afd91088339793330874a3b5156ceaeb1371fcb495f685",
            "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb",
        ),
        (
            "theta",
            "91181a525e0acb17e73d2e96fd4e7d5d7a25913784ef8ad9d3be59c430a4fadd",
            "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
        ),
    ):
        path = C57 / f"results/{name}_crt.json.gz"
        value, decompressed, fingerprint = strict_gzip_json(
            path,
            max_compressed_bytes=2_000_000,
            max_decompressed_bytes=10_000_000,
        )
        require_canonical_compact_json(decompressed)
        compressed, _ = read_stable(path, max_bytes=2_000_000)
        if fingerprint.sha256 != expected_sha or deterministic_gzip(decompressed) != compressed:
            raise StrictDataError(f"C58 upstream {name} resolver byte authority mismatch")
        if (
            type(value) is not dict
            or value.get("schema_id") != f"hcs-c57-{name}-crt-v1"
            or value.get("degree") != 36
            or value.get("coefficients_sha256") != expected_coefficient_sha
            or type(value.get("coefficients")) is not list
            or len(value["coefficients"]) != 37
            or any(type(coefficient) is not int for coefficient in value["coefficients"])
            or value["coefficients"][-1] != 1
            or sha256_bytes(canonical_leaf_bytes(value["coefficients"]))
            != expected_coefficient_sha
        ):
            raise StrictDataError(f"C58 upstream {name} resolver semantic authority mismatch")
        resolvers[name] = value["coefficients"]
    return eliminant, cubic, certificate, resolvers


def rebuild_source_contract() -> dict[str, Any]:
    children = list(CODE.iterdir())
    if any(path.is_symlink() or not path.is_file() for path in children):
        raise StrictDataError("C58 code inventory contains a non-regular entry")
    names = {path.name for path in children}
    if names != CODE_SOURCE_NAMES:
        raise StrictDataError(
            "C58 code inventory mismatch; "
            f"missing={sorted(CODE_SOURCE_NAMES - names)} "
            f"extra={sorted(names - CODE_SOURCE_NAMES)}"
        )
    if any(name == "__pycache__" or name.endswith((".pyc", ".pyo")) for name in names):
        raise StrictDataError("bytecode debris is forbidden in C58 code inventory")
    entries = []
    for path in sorted(children, key=lambda item: item.name):
        raw, fingerprint = read_stable(path, max_bytes=3_000_000)
        entries.append(
            {
                "path": f"code/{path.name}",
                "sha256": fingerprint.sha256,
                "size_bytes": len(raw),
            }
        )
    return {
        "entry_count": len(entries),
        "entries": entries,
        "exact_code_inventory": True,
        "exact_code_path_allowlist": [f"code/{name}" for name in sorted(CODE_SOURCE_NAMES)],
        "schema_id": "hcs-c58-exact-source-contract-v1",
        "self_reference_policy": "certificate/schema/check/manifest digests are excluded; immutable raw evidence is separately rebound",
    }


def validate_arithmetic_evidence(value: Any) -> dict[str, Any]:
    evidence = require_exact_keys(
        value,
        {
            "archimedean",
            "cubic_terms",
            "degree36_local_factors",
            "field_discriminant",
            "field_isomorphism",
            "local_prime_ideals",
            "macaulay",
            "maximal_order",
            "padic_factor_degrees",
            "reflection_witnesses",
            "schema_id",
            "wild_degree36_theta_authority",
        },
        "arithmetic evidence",
    )
    if evidence["schema_id"] != "hcs-c58-arithmetic-evidence-v1":
        raise StrictDataError("arithmetic evidence schema mismatch")
    if evidence["wild_degree36_theta_authority"] != WILD_THETA_AUTHORITY_EXPECTED:
        raise StrictDataError("raw wild theta36 authority carrier changed")
    expected_cubic = [[coefficient, list(exponents)] for coefficient, exponents in CUBIC_TERMS]
    if not deep_exact(evidence["cubic_terms"], expected_cubic):
        raise StrictDataError("arithmetic evidence cubic terms mismatch")
    require_exact_keys(
        evidence["macaulay"],
        {
            "denominator_decimal_newline_sha256",
            "divided_discriminant",
            "divided_discriminant_decimal_newline_sha256",
            "extraneous_shape",
            "factorization",
            "matrix_shape",
            "nonreduced_indices",
            "numerator_decimal_newline_sha256",
            "resultant_decimal_newline_sha256",
        },
        "macaulay evidence",
    )
    require_exact_keys(
        evidence["maximal_order"],
        {
            "integral_basis_canonical_sha256",
            "integral_basis_coefficients_low_to_high_as_num_den",
            "integral_basis_pari_text_sha256",
            "integral_basis_pari_text_size_bytes",
            "nfcertify_unresolved",
            "transformed_monic_polynomial_coefficients_low_to_high",
            "transformed_monic_polynomial_sha256",
        },
        "maximal-order evidence",
    )
    require_exact_keys(
        evidence["field_isomorphism"],
        {
            "orientation",
            "original_generator_image_canonical_sha256",
            "original_generator_image_common_denominator",
            "original_generator_image_numerators_low_to_high",
            "original_polynomial_degree",
        },
        "field-isomorphism evidence",
    )
    require_exact_keys(
        evidence["field_discriminant"],
        {
            "decimal_newline_sha256",
            "digits",
            "exponents_on_surface_bad_prime_envelope",
            "positive",
            "ramified_support",
            "surface_bad_prime_envelope",
            "value",
        },
        "field-discriminant evidence",
    )
    require_exact_keys(
        evidence["archimedean"],
        {
            "V20_signature",
            "V6_signature",
            "complex_conjugation_element_class_index",
            "complex_conjugation_subgroup_tom_index",
            "double_six_orbits_36",
            "field_signature",
            "line_orbits_27",
        },
        "archimedean evidence",
    )
    expected_prime_keys = {str(prime) for prime in DIRECT_PRIMES}
    require_exact_keys(evidence["local_prime_ideals"], expected_prime_keys, "local ideals")
    padic = evidence["padic_factor_degrees"]
    require_exact_keys(padic, expected_prime_keys, "line27 p-adic factors")
    expected_line27_factors = {
        "3": [[3, 1], [6, 1], [9, 2]],
        "5": [[1, 2], [5, 3], [10, 1]],
        "181": [[3, 1], [6, 1], [18, 1]],
        "997": [[3, 1], [6, 1], [18, 1]],
        "2346241": [[3, 1], [6, 1], [18, 1]],
    }
    degree36 = require_exact_keys(
        evidence["degree36_local_factors"],
        {"delta36", "theta36"},
        "degree36 local factors",
    )
    tame_prime_keys = {str(prime) for prime in C3_PRIMES}
    for resolver_name in ("delta36", "theta36"):
        require_exact_keys(
            degree36[resolver_name], tame_prime_keys, f"{resolver_name} tame local factors"
        )
        for prime in C3_PRIMES:
            record = require_exact_keys(
                degree36[resolver_name][str(prime)],
                {
                    "authority_bound_satisfied",
                    "authority_precision",
                    "authority_role",
                    "factor_krasner_bound_satisfied",
                    "factor_degree_multiplicities",
                    "local_rows",
                    "global_polynomial_discriminant_exponent",
                    "resolver_separation_bound_satisfied",
                    "stable_precisions",
                    "total_discriminant_exponent",
                    "twice_max_polynomial_discriminant_exponent",
                },
                f"{resolver_name}/{prime}",
            )
            factors = record["factor_degree_multiplicities"]
            if (
                type(factors) is not list
                or not factors
                or any(
                    type(row) is not list
                    or len(row) != 2
                    or any(type(item) is not int for item in row)
                    or row[0] <= 0
                    or row[1] <= 0
                    for row in factors
                )
            ):
                raise StrictDataError(f"{resolver_name} decomposition factors malformed at {prime}")
            if factors != [[3, 1], [6, 1], [9, 1], [18, 1]]:
                raise StrictDataError(f"{resolver_name} decomposition factors changed at {prime}")
            local_rows = record["local_rows"]
            if (
                record["stable_precisions"] != [20, 30, 40]
                or type(record["total_discriminant_exponent"]) is not int
                or type(local_rows) is not list
                or not local_rows
            ):
                raise StrictDataError(f"{resolver_name} tame local authority malformed at {prime}")
            for row in local_rows:
                require_exact_keys(
                    row,
                    {
                        "d",
                        "e",
                        "f",
                        "factor_degree",
                        "field_discriminant_contribution",
                        "mod_p_factor_exponent",
                        "mod_p_irreducible_factor_degree",
                        "polynomial_discriminant_exponent",
                    },
                    f"{resolver_name}/{prime} local row",
                )
                if any(type(row[key]) is not int for key in row):
                    raise StrictDataError(f"{resolver_name}/{prime} local row is not integral")
            polynomial_exponents = (
                [4, 20, 48, 204] if resolver_name == "delta36" else [2, 4, 6, 12]
            )
            reduction_degrees = (
                [1, 1, 1, 1] if resolver_name == "delta36" else [1, 2, 3, 6]
            )
            reduction_exponents = (
                [3, 6, 9, 18] if resolver_name == "delta36" else [3, 3, 3, 3]
            )
            expected_local_rows = [
                {"d": 2, "e": 3, "f": 1, "factor_degree": 3,
                 "field_discriminant_contribution": 2,
                 "mod_p_factor_exponent": reduction_exponents[0],
                 "mod_p_irreducible_factor_degree": reduction_degrees[0],
                 "polynomial_discriminant_exponent": polynomial_exponents[0]},
                {"d": 2, "e": 3, "f": 2, "factor_degree": 6,
                 "field_discriminant_contribution": 4,
                 "mod_p_factor_exponent": reduction_exponents[1],
                 "mod_p_irreducible_factor_degree": reduction_degrees[1],
                 "polynomial_discriminant_exponent": polynomial_exponents[1]},
                {"d": 2, "e": 3, "f": 3, "factor_degree": 9,
                 "field_discriminant_contribution": 6,
                 "mod_p_factor_exponent": reduction_exponents[2],
                 "mod_p_irreducible_factor_degree": reduction_degrees[2],
                 "polynomial_discriminant_exponent": polynomial_exponents[2]},
                {"d": 2, "e": 3, "f": 6, "factor_degree": 18,
                 "field_discriminant_contribution": 12,
                 "mod_p_factor_exponent": reduction_exponents[3],
                 "mod_p_irreducible_factor_degree": reduction_degrees[3],
                 "polynomial_discriminant_exponent": polynomial_exponents[3]},
            ]
            expected_role = (
                "BOUNDED_NON_RESULT_NONDEPENDENCY"
                if resolver_name == "delta36"
                else "KRASNER_CERTIFIED_AUTHORITY"
            )
            expected_bound = 840 if resolver_name == "delta36" else 24
            expected_satisfied = resolver_name == "theta36"
            if (
                local_rows != expected_local_rows
                or record["total_discriminant_exponent"] != 24
                or record["authority_precision"] != 40
                or record["global_polynomial_discriminant_exponent"] != expected_bound
                or record["twice_max_polynomial_discriminant_exponent"]
                != (408 if resolver_name == "delta36" else 24)
                or record["authority_bound_satisfied"] is not expected_satisfied
                or record["factor_krasner_bound_satisfied"] is not expected_satisfied
                or record["resolver_separation_bound_satisfied"] is not expected_satisfied
                or record["authority_role"] != expected_role
            ):
                raise StrictDataError(f"{resolver_name} tame local different rows changed at {prime}")
    for prime in DIRECT_PRIMES:
        rows = evidence["local_prime_ideals"][str(prime)]
        if type(rows) is not list or not rows:
            raise StrictDataError(f"empty local ideal carrier at {prime}")
        for index, row in enumerate(rows):
            require_exact_keys(
                row,
                {
                    "different_exponent",
                    "e",
                    "f",
                    "generator_coordinates",
                    "hnf_rows",
                    "prime_vector_complement",
                },
                f"local ideal {prime}/{index}",
            )
            for key in ("different_exponent", "e", "f"):
                require_int(row[key], f"local ideal {prime}/{index}/{key}")
            vector = row["generator_coordinates"]
            if type(vector) is not list or len(vector) != 27 or any(type(item) is not int for item in vector):
                raise StrictDataError(f"local generator vector shape mismatch at {prime}/{index}")
            for matrix_key in ("hnf_rows", "prime_vector_complement"):
                matrix = row[matrix_key]
                if (
                    type(matrix) is not list
                    or len(matrix) != 27
                    or any(type(line) is not list or len(line) != 27 for line in matrix)
                    or any(type(item) is not int for line in matrix for item in line)
                ):
                    raise StrictDataError(
                        f"local {matrix_key} shape mismatch at {prime}/{index}"
                    )
        factors = padic[str(prime)]
        if (
            type(factors) is not list
            or not factors
            or any(
                type(row) is not list
                or len(row) != 2
                or type(row[0]) is not int
                or type(row[1]) is not int
                or row[0] <= 0
                or row[1] <= 0
                for row in factors
            )
            or factors != sorted(factors)
        ):
            raise StrictDataError(f"p-adic factor-degree carrier malformed at {prime}")
        if factors != expected_line27_factors[str(prime)]:
            raise StrictDataError(f"line-field local degree carrier changed at {prime}")
    basis = evidence["maximal_order"]["integral_basis_coefficients_low_to_high_as_num_den"]
    if type(basis) is not list or len(basis) != 27:
        raise StrictDataError("integral basis does not have 27 elements")
    for row_index, row in enumerate(basis):
        if type(row) is not list or len(row) != 27:
            raise StrictDataError(f"integral basis row {row_index} has wrong length")
        for pair in row:
            if (
                type(pair) is not list
                or len(pair) != 2
                or any(type(item) is not int for item in pair)
                or pair[1] <= 0
                or math.gcd(pair[0], pair[1]) != 1
            ):
                raise StrictDataError("integral basis contains a non-normalized rational")
    transformed = evidence["maximal_order"][
        "transformed_monic_polynomial_coefficients_low_to_high"
    ]
    if (
        type(transformed) is not list
        or len(transformed) != 28
        or any(type(item) is not int for item in transformed)
        or transformed[-1] != 1
    ):
        raise StrictDataError("transformed polynomial carrier is malformed")
    for key in (
        "transformed_monic_polynomial_sha256",
        "integral_basis_canonical_sha256",
        "integral_basis_pari_text_sha256",
    ):
        require_sha256(evidence["maximal_order"][key], f"maximal order/{key}")
    if evidence["maximal_order"]["nfcertify_unresolved"] != []:
        raise StrictDataError("raw maximal-order carrier is not certified")
    isomorphism = evidence["field_isomorphism"]
    if isomorphism["orientation"] != (
        "original_C56_eliminant_generator_maps_to_polynomial_in_transformed_generator"
    ):
        raise StrictDataError("field-isomorphism orientation mismatch")
    numerators = isomorphism["original_generator_image_numerators_low_to_high"]
    denominator = require_int(
        isomorphism["original_generator_image_common_denominator"],
        "field-isomorphism denominator",
    )
    if (
        type(numerators) is not list
        or not 1 <= len(numerators) <= 27
        or any(type(item) is not int for item in numerators)
        or denominator <= 0
        or math.gcd(denominator, *numerators) != 1
        or isomorphism["original_polynomial_degree"] != 27
    ):
        raise StrictDataError("field-isomorphism coefficient carrier is noncanonical")
    require_sha256(
        isomorphism["original_generator_image_canonical_sha256"],
        "field-isomorphism digest",
    )
    discriminant = evidence["field_discriminant"]
    if (
        type(discriminant["value"]) is not int
        or discriminant["value"] <= 0
        or discriminant["surface_bad_prime_envelope"] != list(SUPPORT)
        or discriminant["ramified_support"] != list(SUPPORT[1:])
        or discriminant["exponents_on_surface_bad_prime_envelope"]
        != list(FIELD_DISCRIMINANT_EXPONENTS)
        or discriminant["positive"] is not True
        or discriminant["digits"] != len(str(discriminant["value"]))
        or discriminant["decimal_newline_sha256"]
        != sha256_bytes((str(discriminant["value"]) + "\n").encode("ascii"))
    ):
        raise StrictDataError("field-discriminant raw carrier is inconsistent")
    require_sha256(discriminant["decimal_newline_sha256"], "field discriminant digest")
    if type(evidence["reflection_witnesses"]) is not list or len(evidence["reflection_witnesses"]) != 3:
        raise StrictDataError("reflection witness count mismatch")
    reflection_keys = {
        "affine_chart",
        "chart_groebner_basis_lengths",
        "chart_groebner_basis_sha256",
        "chart_unit_ideals",
        "chart0_reduced_groebner_basis",
        "gradient_mod_prime",
        "hessian_determinant_mod_prime",
        "point_x0_to_x3",
        "prime",
        "total_space_quotient_mod_prime",
    }
    for row in evidence["reflection_witnesses"]:
        require_exact_keys(row, reflection_keys, "reflection witness")
        if (
            type(row["prime"]) is not int
            or row["affine_chart"] != 0
            or type(row["point_x0_to_x3"]) is not list
            or len(row["point_x0_to_x3"]) != 4
            or any(type(item) is not int for item in row["point_x0_to_x3"])
            or row["gradient_mod_prime"] != [0, 0, 0, 0]
            or type(row["chart_groebner_basis_sha256"]) is not list
            or len(row["chart_groebner_basis_sha256"]) != 4
            or any(type(item) is not str for item in row["chart_groebner_basis_sha256"])
            or type(row["chart_groebner_basis_lengths"]) is not list
            or len(row["chart_groebner_basis_lengths"]) != 4
            or any(type(item) is not int for item in row["chart_groebner_basis_lengths"])
            or type(row["chart_unit_ideals"]) is not list
            or len(row["chart_unit_ideals"]) != 4
            or any(type(item) is not bool for item in row["chart_unit_ideals"])
            or type(row["chart0_reduced_groebner_basis"]) is not list
        ):
            raise StrictDataError("reflection witness shape mismatch")
        for digest in row["chart_groebner_basis_sha256"]:
            require_sha256(digest, "reflection Groebner digest")
    if [row["prime"] for row in evidence["reflection_witnesses"]] != list(REFLECTION_PRIMES):
        raise StrictDataError("reflection witnesses are not in canonical prime order")
    return evidence


def validate_group_evidence(value: Any) -> dict[str, Any]:
    evidence = require_exact_keys(
        value,
        {
            "double_six_generators",
            "group_report",
            "line_generators",
            "picard_generators",
            "schema_id",
        },
        "group evidence",
    )
    if evidence["schema_id"] != "hcs-c58-group-evidence-v1":
        raise StrictDataError("group evidence schema mismatch")
    return evidence


def rebuild_artifact_contract(
    arithmetic_path: Path, group_path: Path
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    if arithmetic_path.name != ARTIFACT_NAMES[0] or group_path.name != ARTIFACT_NAMES[1]:
        raise StrictDataError("C58 evidence basenames are fixed")
    arithmetic, arithmetic_raw, arithmetic_fingerprint = strict_gzip_json(
        arithmetic_path,
        max_compressed_bytes=4_000_000,
        max_decompressed_bytes=8_000_000,
    )
    require_canonical_compact_json(arithmetic_raw)
    compressed_raw, _ = read_stable(arithmetic_path, max_bytes=4_000_000)
    if deterministic_gzip(arithmetic_raw) != compressed_raw:
        raise StrictDataError("arithmetic evidence gzip is not deterministic")
    arithmetic = validate_arithmetic_evidence(arithmetic)
    arithmetic_authority = ARTIFACT_BYTE_AUTHORITY[ARTIFACT_NAMES[0]]
    if (
        arithmetic_fingerprint.sha256 != arithmetic_authority["sha256"]
        or arithmetic_fingerprint.size_bytes != arithmetic_authority["size_bytes"]
        or sha256_bytes(arithmetic_raw) != arithmetic_authority["decompressed_sha256"]
        or len(arithmetic_raw) != arithmetic_authority["decompressed_size_bytes"]
    ):
        raise StrictDataError("arithmetic evidence byte authority changed")

    group_raw, group_fingerprint = read_stable(group_path, max_bytes=1_000_000)
    group = canonical_pretty(group_raw, max_bytes=1_000_000, label="group evidence")
    group = validate_group_evidence(group)
    group_authority = ARTIFACT_BYTE_AUTHORITY[ARTIFACT_NAMES[1]]
    if (
        group_fingerprint.sha256 != group_authority["sha256"]
        or group_fingerprint.size_bytes != group_authority["size_bytes"]
    ):
        raise StrictDataError("group evidence byte authority changed")
    contract = {
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
        "artifact_count": 2,
        "immutable_raw_evidence_carriers": True,
        "schema_id": "hcs-c58-artifact-contract-v1",
    }
    return contract, arithmetic, group


def compositions(total: int, length: int) -> tuple[tuple[int, ...], ...]:
    return tuple(row for row in product(range(total + 1), repeat=length) if sum(row) == total)


def macaulay_rows(terms: tuple[tuple[int, tuple[int, ...]], ...]):
    monomials = tuple(sorted(compositions(5, 4), reverse=True))
    index = {monomial: column for column, monomial in enumerate(monomials)}
    gradients = []
    for variable in range(4):
        gradient: dict[tuple[int, ...], int] = {}
        for coefficient, exponent in terms:
            if exponent[variable]:
                target = list(exponent)
                target[variable] -= 1
                key = tuple(target)
                gradient[key] = gradient.get(key, 0) + coefficient * exponent[variable]
        gradients.append(gradient)
    rows = []
    for alpha in monomials:
        variable = next(position for position, value in enumerate(alpha) if value >= 2)
        multiplier = list(alpha)
        multiplier[variable] -= 2
        row = [0] * len(monomials)
        for exponent, coefficient in gradients[variable].items():
            target = tuple(multiplier[i] + exponent[i] for i in range(4))
            row[index[target]] += coefficient
        rows.append(row)
    nonreduced = tuple(
        position
        for position, alpha in enumerate(monomials)
        if sum(value >= 2 for value in alpha) >= 2
    )
    minor = [[rows[i][j] for j in nonreduced] for i in nonreduced]
    if len(rows) != 56 or len(nonreduced) != 24:
        raise StrictDataError("checker Macaulay matrix dimensions changed")
    return rows, nonreduced, minor


def bareiss(values: list[list[int]]) -> int:
    matrix = [row[:] for row in values]
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise StrictDataError("Bareiss input is not a nonempty square matrix")
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if matrix[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size) if matrix[row][pivot_index]),
                None,
            )
            if swap is None:
                return 0
            matrix[pivot_index], matrix[swap] = matrix[swap], matrix[pivot_index]
            sign = -sign
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % previous:
                    raise StrictDataError("Bareiss division was not exact")
                matrix[row][column] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, size):
            matrix[row][pivot_index] = 0
    return sign * matrix[-1][-1]


def macaulay_replay(evidence: dict[str, Any]) -> dict[str, Any]:
    rows, nonreduced, minor = macaulay_rows(CUBIC_TERMS)
    numerator = bareiss(rows)
    denominator = bareiss(minor)
    if denominator == 0 or numerator % denominator:
        raise StrictDataError("Macaulay extraneous minor does not divide the determinant")
    resultant = numerator // denominator
    if resultant % (3**5):
        raise StrictDataError("cubic discriminant normalization by 3^5 is not integral")
    divided = resultant // (3**5)
    factorization = math.prod(prime**exponent for prime, exponent in SURFACE_FACTORIZATION)
    if divided != factorization:
        raise StrictDataError("surface discriminant factorization multiplication failed")
    expected = {
        "denominator_decimal_newline_sha256": sha256_bytes((str(denominator) + "\n").encode("ascii")),
        "divided_discriminant": divided,
        "divided_discriminant_decimal_newline_sha256": sha256_bytes(
            (str(divided) + "\n").encode("ascii")
        ),
        "extraneous_shape": [24, 24],
        "factorization": [[prime, exponent] for prime, exponent in SURFACE_FACTORIZATION],
        "matrix_shape": [56, 56],
        "nonreduced_indices": list(nonreduced),
        "numerator_decimal_newline_sha256": sha256_bytes((str(numerator) + "\n").encode("ascii")),
        "resultant_decimal_newline_sha256": sha256_bytes((str(resultant) + "\n").encode("ascii")),
    }
    if not deep_exact(evidence["macaulay"], expected):
        raise StrictDataError("raw Macaulay carrier disagrees with checker-owned Bareiss replay")
    return {
        **expected,
        "determinant_engine": "CHECKER_OWNED_PURE_PYTHON_BAREISS",
        "surface_bad_prime_envelope": list(SUPPORT),
        "surface_bad_prime_envelope_exhausted_by_exact_factorization": True,
    }


def evaluate_homogeneous(
    point: list[int], derivative_variables: tuple[int, ...] = ()
) -> int:
    value = 0
    for coefficient, exponent in CUBIC_TERMS:
        factor = coefficient
        remaining = list(exponent)
        valid = True
        for variable in derivative_variables:
            if remaining[variable] == 0:
                valid = False
                break
            factor *= remaining[variable]
            remaining[variable] -= 1
        if valid:
            factor *= math.prod(point[index] ** remaining[index] for index in range(4))
            value += factor
    return value


def determinant3(matrix: list[list[int]], modulus: int) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    ) % modulus


def solve_linear_mod_prime(
    matrix: list[list[int]], right_hand_side: list[int], prime: int
) -> list[int]:
    if (
        len(matrix) != len(right_hand_side)
        or any(len(row) != len(matrix) for row in matrix)
        or prime <= 2
    ):
        raise StrictDataError("malformed modular linear system")
    size = len(matrix)
    augmented = [
        [value % prime for value in row] + [right_hand_side[index] % prime]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise StrictDataError("singular modular Hessian in reflection lift")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse = pow(augmented[column][column], -1, prime)
        augmented[column] = [
            (value * inverse) % prime for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            multiplier = augmented[row][column]
            augmented[row] = [
                (left - multiplier * right) % prime
                for left, right in zip(augmented[row], augmented[column])
            ]
    solution = [augmented[row][-1] for row in range(size)]
    if any(
        sum(matrix[row][column] * solution[column] for column in range(size))
        % prime
        != right_hand_side[row] % prime
        for row in range(size)
    ):
        raise StrictDataError("modular reflection-lift solution did not rebound")
    return solution


def normalized_groebner_basis(prime: int, chart: int) -> tuple[list[Any], bool]:
    try:
        from sympy import groebner, symbols
    except ImportError as exc:
        raise StrictDataError("SymPy is required for reflection Groebner replay") from exc
    variables_all = symbols("x0:4")
    polynomial = sum(
        coefficient
        * math.prod(variables_all[index] ** exponent[index] for index in range(4))
        for coefficient, exponent in CUBIC_TERMS
    )
    gradients = [polynomial.diff(variable) for variable in variables_all]
    substitutions = {variables_all[index]: 0 for index in range(chart)}
    substitutions[variables_all[chart]] = 1
    remaining = variables_all[chart + 1 :]
    equations = [gradient.subs(substitutions) for gradient in gradients]
    if not remaining:
        unit = any(int(equation) % prime for equation in equations)
        basis = [[ [1, []] ]] if unit else []
        return basis, unit
    basis_object = groebner(
        equations,
        *remaining,
        modulus=prime,
        order="grevlex",
    )
    basis = []
    for polynomial_object in basis_object.polys:
        terms = [
            [int(coefficient) % prime, list(exponents)]
            for exponents, coefficient in polynomial_object.terms()
        ]
        basis.append(terms)
    unit = len(basis) == 1 and basis[0] == [[1, [0] * len(remaining)]]
    return basis, unit


def reflection_replay(evidence: dict[str, Any]) -> list[dict[str, Any]]:
    expected_rows = []
    for prime in REFLECTION_PRIMES:
        fixed = REFLECTION_WITNESSES[prime]
        point = fixed["point"]
        value = evaluate_homogeneous(point)
        gradient = [evaluate_homogeneous(point, (variable,)) % prime for variable in range(4)]
        hessian = [
            [evaluate_homogeneous(point, (left, right)) % prime for right in range(1, 4)]
            for left in range(1, 4)
        ]
        hessian_determinant = determinant3(hessian, prime)
        if value % prime or gradient != [0, 0, 0, 0]:
            raise StrictDataError(f"claimed reflection point is not singular modulo {prime}")
        quotient = (value // prime) % prime
        if hessian_determinant == 0 or quotient == 0:
            raise StrictDataError(f"reflection witness is not transverse ODP at {prime}")
        basis_hashes = []
        basis_lengths = []
        chart_bases = []
        unit_ideals = []
        for chart in range(4):
            basis, unit = normalized_groebner_basis(prime, chart)
            chart_bases.append(basis)
            basis_hashes.append(sha256_bytes(canonical_leaf_bytes(basis)))
            basis_lengths.append(len(basis))
            unit_ideals.append(unit)
        expected_chart_zero = []
        for variable_index in range(3):
            exponent = [0, 0, 0]
            exponent[variable_index] = 1
            expected_chart_zero.append(
                [
                    [1, exponent],
                    [(-point[variable_index + 1]) % prime, [0, 0, 0]],
                ]
            )
        expected_unit_bases = [
            [[[1, [0, 0]]]],
            [[[1, [0]]]],
            [[[1, []]]],
        ]
        if (
            chart_bases[0] != expected_chart_zero
            or chart_bases[1:] != expected_unit_bases
        ):
            raise StrictDataError(
                f"reflection Groebner bases do not define exactly the stated point at {prime}"
            )
        row = {
            "affine_chart": 0,
            "chart_groebner_basis_lengths": basis_lengths,
            "chart_groebner_basis_sha256": basis_hashes,
            "chart_unit_ideals": unit_ideals,
            "chart0_reduced_groebner_basis": expected_chart_zero,
            "gradient_mod_prime": gradient,
            "hessian_determinant_mod_prime": hessian_determinant,
            "point_x0_to_x3": point,
            "prime": prime,
            "total_space_quotient_mod_prime": quotient,
        }
        if hessian_determinant != fixed["hessian"] or quotient != fixed["quotient"]:
            raise StrictDataError(f"checker-owned reflection constants changed at {prime}")
        if unit_ideals != [False, True, True, True] or basis_lengths != [3, 1, 1, 1]:
            raise StrictDataError(f"reflection singular locus is not one reduced affine point at {prime}")
        expected_rows.append(row)
    if not deep_exact(evidence["reflection_witnesses"], expected_rows):
        raise StrictDataError("raw reflection witnesses disagree with independent replay")
    return expected_rows


def reflection_hensel_semantics(evidence: dict[str, Any]) -> dict[str, bool]:
    rows = evidence.get("reflection_witnesses")
    if type(rows) is not list or [row.get("prime") for row in rows] != list(
        REFLECTION_PRIMES
    ):
        raise StrictDataError("reflection Hensel replay lacks the exact prime carrier")
    all_odd = True
    all_unique = True
    all_hessian_units = True
    all_unique_lifts = True
    all_critical_values_congruent = True
    all_valuation_one = True
    for row in rows:
        prime = row["prime"]
        point = row["point_x0_to_x3"]
        all_odd = all_odd and prime % 2 == 1
        all_unique = all_unique and (
            row["chart_unit_ideals"] == [False, True, True, True]
            and row["chart_groebner_basis_lengths"] == [3, 1, 1, 1]
        )
        affine_gradient = [
            evaluate_homogeneous(point, (variable,)) for variable in range(1, 4)
        ]
        if any(value % prime for value in affine_gradient):
            raise StrictDataError("reflection affine gradient is not divisible by p")
        hessian = [
            [
                evaluate_homogeneous(point, (left, right)) % prime
                for right in range(1, 4)
            ]
            for left in range(1, 4)
        ]
        determinant = determinant3(hessian, prime)
        all_hessian_units = all_hessian_units and determinant != 0
        correction = solve_linear_mod_prime(
            hessian,
            [-(value // prime) for value in affine_gradient],
            prime,
        )
        lifted_point = [1] + [
            point[index + 1] + prime * correction[index] for index in range(3)
        ]
        modulus = prime * prime
        lifted_gradient = [
            evaluate_homogeneous(lifted_point, (variable,)) % modulus
            for variable in range(1, 4)
        ]
        all_unique_lifts = all_unique_lifts and lifted_gradient == [0, 0, 0]
        original_value = evaluate_homogeneous(point)
        lifted_value = evaluate_homogeneous(lifted_point)
        all_critical_values_congruent = all_critical_values_congruent and (
            lifted_value - original_value
        ) % modulus == 0
        all_valuation_one = all_valuation_one and (
            lifted_value % prime == 0 and lifted_value % modulus != 0
        )
    result = {
        "affine_hessian_units": all_hessian_units,
        "critical_points_hensel_lift_uniquely": all_unique_lifts,
        "critical_values_congruent_to_integer_witness_mod_p_squared": (
            all_critical_values_congruent
        ),
        "residue_characteristics_odd": all_odd,
        "smoothing_parameter_valuation_exactly_one": all_valuation_one,
        "unique_geometric_singular_point_each_prime": all_unique,
    }
    if set(result.values()) != {True}:
        raise StrictDataError("reflection Hensel/regular-total-space bridge failed")
    return result


def lattice_dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return left[0] * right[0] - sum(a * b for a, b in zip(left[1:], right[1:]))


def reflection_matrix(root: tuple[int, ...]) -> list[list[int]]:
    columns = []
    for column in range(7):
        basis = tuple(int(index == column) for index in range(7))
        pairing = lattice_dot(basis, root)
        columns.append([basis[index] + pairing * root[index] for index in range(7)])
    return [[columns[column][row] for column in range(7)] for row in range(7)]


def matrix_vector(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(7)) for row in range(7))


def labelled_carriers() -> dict[str, Any]:
    exceptional = []
    for index in range(6):
        vector = [0] * 7
        vector[index + 1] = 1
        exceptional.append(tuple(vector))
    roots = [
        tuple(exceptional[index][coordinate] - exceptional[index + 1][coordinate] for coordinate in range(7))
        for index in range(5)
    ]
    roots.append((1, -1, -1, -1, 0, 0, 0))
    lines = list(exceptional)
    for left, right in combinations(range(6), 2):
        vector = [1] + [0] * 6
        vector[left + 1] = vector[right + 1] = -1
        lines.append(tuple(vector))
    for omitted in range(6):
        vector = [2] + [-1] * 6
        vector[omitted + 1] = 0
        lines.append(tuple(vector))
    if len(lines) != 27 or len(set(lines)) != 27:
        raise StrictDataError("checker-owned Schlaefli line carrier is malformed")
    matrices = [reflection_matrix(root) for root in roots]
    line_index = {line: index for index, line in enumerate(lines)}
    line_generators_zero = [
        [line_index[matrix_vector(matrix, line)] for line in lines] for matrix in matrices
    ]
    incidence = [[lattice_dot(left, right) for right in lines] for left in lines]
    sixers = [
        frozenset(subset)
        for subset in combinations(range(27), 6)
        if all(incidence[left][right] == 0 for left, right in combinations(subset, 2))
    ]
    double_sixes = set()
    for first in sixers:
        second = frozenset(
            index
            for index in range(27)
            if index not in first
            and sum(incidence[index][other] for other in first) == 5
        )
        if len(second) != 6:
            raise StrictDataError("checker-owned sixer complement is malformed")
        double_sixes.add(frozenset((first, second)))
    configurations = sorted(
        double_sixes,
        key=lambda value: tuple(sorted(tuple(sorted(row)) for row in value)),
    )
    if len(sixers) != 72 or len(configurations) != 36:
        raise StrictDataError("checker-owned Schlaefli sixer counts changed")

    def act(permutation: list[int], value: Any) -> Any:
        if type(value) is int:
            return permutation[value]
        return frozenset(act(permutation, element) for element in value)

    double_index = {value: index for index, value in enumerate(configurations)}
    double_generators_zero = [
        [double_index[act(generator, value)] for value in configurations]
        for generator in line_generators_zero
    ]
    result = {
        "double_six_generators": [
            [value + 1 for value in generator] for generator in double_generators_zero
        ],
        "line_generators": [
            [value + 1 for value in generator] for generator in line_generators_zero
        ],
        "picard_generators": matrices,
    }
    result["canonical_sha256"] = {
        key: sha256_bytes(canonical_leaf_bytes(result[key]))
        for key in ("double_six_generators", "line_generators", "picard_generators")
    }
    return result


def run_group_replay(gap: Path) -> tuple[dict[str, Any], str]:
    script = CODE / "c58_checker_group.g"
    if script.is_symlink() or not script.is_file():
        raise StrictDataError("checker GAP helper is missing")
    completed = subprocess.run(
        [str(gap.resolve(strict=True)), "-q", str(script)],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=clean_environment(),
        check=True,
        timeout=180,
    )
    if completed.stderr:
        raise StrictDataError("checker GAP replay emitted stderr")
    if not completed.stdout.endswith(b"\n") or completed.stdout.count(b"\n") != 1:
        raise StrictDataError("checker GAP replay must emit exactly one line")
    raw = completed.stdout[:-1]
    report = strict_json_loads(raw, max_bytes=10_000_000)
    if type(report) is not dict or raw != canonical_leaf_bytes(report):
        raise StrictDataError("checker GAP replay is not canonical JSON")
    return report, sha256_bytes(raw)


def rational_vector_from_num_den(value: Any, label: str) -> list[Fraction]:
    if type(value) is not list or not value:
        raise StrictDataError(f"{label} is not a nonempty rational vector")
    result = []
    for index, pair in enumerate(value):
        if (
            type(pair) is not list
            or len(pair) != 2
            or any(type(item) is not int for item in pair)
            or pair[1] <= 0
            or math.gcd(pair[0], pair[1]) != 1
        ):
            raise StrictDataError(f"{label}/{index} is not a normalized rational")
        result.append(Fraction(pair[0], pair[1]))
    return result


def solve_two_layer_fraction_system(
    base: list[Fraction],
    wild: list[Fraction],
    deep: list[Fraction],
    target: list[Fraction],
) -> tuple[list[int], list[list[int]]]:
    if not (len(base) == len(wild) == len(deep) == len(target)):
        raise StrictDataError("deep-C3 filtration vectors have unequal lengths")
    right = [target[index] - base[index] for index in range(len(base))]
    candidates: set[tuple[Fraction, Fraction]] = set()
    for left, right_index in combinations(range(len(base)), 2):
        determinant = wild[left] * deep[right_index] - wild[right_index] * deep[left]
        if determinant:
            wild_layers = (
                right[left] * deep[right_index]
                - right[right_index] * deep[left]
            ) / determinant
            deep_layers = (
                wild[left] * right[right_index]
                - wild[right_index] * right[left]
            ) / determinant
            if all(
                base[index]
                + wild_layers * wild[index]
                + deep_layers * deep[index]
                == target[index]
                for index in range(len(base))
            ):
                candidates.add((wild_layers, deep_layers))
    if len(candidates) != 1:
        raise StrictDataError(
            f"deep-C3 filtration system has {len(candidates)} formal solutions"
        )
    formal_fraction = next(iter(candidates))
    if any(value.denominator != 1 for value in formal_fraction):
        raise StrictDataError("deep-C3 formal filtration solution is nonintegral")
    formal = [int(value) for value in formal_fraction]
    nonnegative = [formal] if all(value >= 0 for value in formal) else []
    return formal, nonnegative


def group_replay(
    evidence: dict[str, Any], gap: Path, degree36_authority: dict[str, Any]
) -> dict[str, Any]:
    labelled = labelled_carriers()
    for key in ("line_generators", "double_six_generators", "picard_generators"):
        if not deep_exact(evidence[key], labelled[key]):
            raise StrictDataError(f"group evidence {key} is not the frozen labelled carrier")
    report, report_sha = run_group_replay(gap)
    rich = require_exact_keys(
        evidence["group_report"],
        {
            "action_sha256",
            "complex_conjugation",
            "counts",
            "order_two_tom_profiles",
            "p3",
            "p5",
            "reflection",
            "status",
            "tame_C3",
            "tom_dual_action_exhaustion",
            "upstream_lock",
        },
        "producer rich group report",
    )
    # The fixed digest rebounds every rich-report leaf, while the checks below
    # independently project all theorem-bearing fields onto checker-owned GAP,
    # PARI and frozen labelled-carrier computations.  The producer report is
    # deliberately not required to equal the differently shaped GAP report.
    if sha256_bytes(canonical_leaf_bytes(rich)) != (
        "e4bfe21973624144c7a3f318f3015e3b49be22ac066b5383f5985acc2674f7f6"
    ):
        raise StrictDataError("producer rich group report byte authority changed")
    action_generators = report.get("action_generators")
    if type(action_generators) is not dict:
        raise StrictDataError("GAP report lacks labelled action generators")
    expected_action_generators = {
        "double_six_point_images": labelled["double_six_generators"],
        "line_point_images": labelled["line_generators"],
        "picard_matrices": labelled["picard_generators"],
    }
    if not deep_exact(action_generators, expected_action_generators):
        raise StrictDataError("GAP actions are abstractly correct but labels do not match C56/C57")
    expected_action_sha = labelled["canonical_sha256"]
    if not deep_exact(rich["action_sha256"], expected_action_sha):
        raise StrictDataError("producer action digests do not rebind the full labelled arrays")
    if rich["counts"] != {
        "double_sixes": 36,
        "line_action_faithful": True,
        "line_action_kernel_order": 1,
        "lines": 27,
        "sixers": 72,
        "weyl_order": 51840,
    } or rich["status"] != "PASS":
        raise StrictDataError("producer group report count/status projection mismatch")
    if report.get("actions") != {
        "double_six_action_bijective": True,
        "double_six_degree": 36,
        "line_degree": 27,
        "picard_action_bijective": True,
        "picard_lattice_rank": 7,
        "weyl_group_order": 51840,
    }:
        raise StrictDataError("W(E6) action identity mismatch")

    wild_theta_authority = degree36_authority.get(
        "wild_degree36_theta_authority"
    )
    if wild_theta_authority != WILD_THETA_AUTHORITY_EXPECTED:
        raise StrictDataError("wild group filters lack certified theta36 authority")

    def expanded_authority_degrees(prime: str) -> list[int]:
        return [
            degree
            for degree, count in wild_theta_authority["prime_records"][prime][
                "factor_degree_multiplicities"
            ]
            for _ in range(count)
        ]

    p3_target_36 = expanded_authority_degrees("3")
    p5_target_36 = expanded_authority_degrees("5")

    p3 = report.get("p3_filter")
    if type(p3) is not dict or set(p3) != {
        "all_tom_decomposition_pattern_hits",
        "deep_C3_exhaustion",
        "deep_C3_selected_action_by_inertia",
        "decomposition_candidates",
        "inertia_candidates",
        "valid_decomposition_inertia_pairs",
    }:
        raise StrictDataError("p=3 GAP filter shape mismatch")
    raw_deep_exhaustion = require_exact_keys(
        p3["deep_C3_exhaustion"],
        {
            "base_different_vector_num_den",
            "profiles",
            "selected_tom_index",
            "solution_variable_order",
            "target_different_vector_num_den",
            "wild_C3_squared_per_layer_contribution_num_den",
        },
        "p=3 exhaustive deep-C3 filter",
    )
    base_different = rational_vector_from_num_den(
        raw_deep_exhaustion["base_different_vector_num_den"],
        "p=3 base different",
    )
    target_different = rational_vector_from_num_den(
        raw_deep_exhaustion["target_different_vector_num_den"],
        "p=3 target different",
    )
    wild_contribution = rational_vector_from_num_den(
        raw_deep_exhaustion[
            "wild_C3_squared_per_layer_contribution_num_den"
        ],
        "p=3 wild-layer contribution",
    )
    expected_deep_profiles = [
        {
            "double_six_orbit_rle": [[3, 12]],
            "fixed_dimensions_V6_V20": [0, 8],
            "formal_integer_solution": [7, -18],
            "line_orbit_rle": [[3, 9]],
            "multiplicity": 2,
            "nonnegative_integer_solutions": [],
            "per_layer_different_contribution_num_den": [
                [1, 3],
                [2, 3],
                [1, 1],
                [1, 1],
            ],
            "tom_index": 6,
        },
        {
            "double_six_orbit_rle": [[1, 6], [3, 10]],
            "fixed_dimensions_V6_V20": [4, 10],
            "formal_integer_solution": [1, 6],
            "line_orbit_rle": [[1, 9], [3, 6]],
            "multiplicity": 1,
            "nonnegative_integer_solutions": [[1, 6]],
            "per_layer_different_contribution_num_den": [
                [0, 1],
                [0, 1],
                [1, 1],
                [1, 1],
            ],
            "tom_index": 7,
        },
        {
            "double_six_orbit_rle": [[1, 3], [3, 11]],
            "fixed_dimensions_V6_V20": [2, 6],
            "formal_integer_solution": [7, -18],
            "line_orbit_rle": [[3, 9]],
            "multiplicity": 1,
            "nonnegative_integer_solutions": [],
            "per_layer_different_contribution_num_den": [
                [1, 3],
                [2, 3],
                [1, 1],
                [1, 1],
            ],
            "tom_index": 8,
        },
    ]
    if (
        raw_deep_exhaustion["base_different_vector_num_den"]
        != [[2, 1], [5, 1], [8, 1], [8, 1]]
        or raw_deep_exhaustion["target_different_vector_num_den"]
        != [[3, 1], [7, 1], [18, 1], [18, 1]]
        or raw_deep_exhaustion[
            "wild_C3_squared_per_layer_contribution_num_den"
        ]
        != [[1, 1], [2, 1], [4, 1], [4, 1]]
        or raw_deep_exhaustion["solution_variable_order"]
        != ["wild_C3_squared_layers", "deep_C3_layers"]
        or raw_deep_exhaustion["profiles"] != expected_deep_profiles
        or raw_deep_exhaustion["selected_tom_index"] != 7
    ):
        raise StrictDataError("p=3 exhaustive deep-C3 profile carrier changed")
    for profile in raw_deep_exhaustion["profiles"]:
        deep_contribution = rational_vector_from_num_den(
            profile["per_layer_different_contribution_num_den"],
            f"p=3 deep profile ToM{profile['tom_index']}",
        )
        formal, nonnegative = solve_two_layer_fraction_system(
            base_different,
            wild_contribution,
            deep_contribution,
            target_different,
        )
        if (
            formal != profile["formal_integer_solution"]
            or nonnegative != profile["nonnegative_integer_solutions"]
        ):
            raise StrictDataError("p=3 deep-C3 Fraction solution did not rebound GAP")
    deep_action_rows = p3["deep_C3_selected_action_by_inertia"]
    if deep_action_rows != [
        {"inertia_tom_index": 140, "tame_action": "inversion"},
        {"inertia_tom_index": 142, "tame_action": "central"},
    ]:
        raise StrictDataError("selected deep-C3 tame actions changed")
    deep_c3_exhaustion = {
        **raw_deep_exhaustion,
        "selected_profile_tame_action_by_inertia_tom_index": {
            str(row["inertia_tom_index"]): row["tame_action"]
            for row in deep_action_rows
        },
    }
    serre_surviving_inertia_tom_indices = [
        row["inertia_tom_index"]
        for row in deep_action_rows
        if row["tame_action"] == "inversion"
    ]
    if serre_surviving_inertia_tom_indices != [140]:
        raise StrictDataError("Serre inversion did not select a unique p=3 inertia")
    expected_p3_all_hits = [
        {
            "id_group": [18, 4],
            "order": 18,
            "tame_quotient_cyclic": True,
            "tame_quotient_id_group": [2, 1],
            "tom_index": 140,
            "wild_sylow_3_id_group": [9, 2],
            "wild_sylow_3_normal": True,
        },
        {
            "id_group": [18, 3],
            "order": 18,
            "tame_quotient_cyclic": True,
            "tame_quotient_id_group": [2, 1],
            "tom_index": 142,
            "wild_sylow_3_id_group": [9, 2],
            "wild_sylow_3_normal": True,
        },
        {
            "id_group": [36, 10],
            "order": 36,
            "tame_quotient_cyclic": False,
            "tame_quotient_id_group": [4, 2],
            "tom_index": 206,
            "wild_sylow_3_id_group": [9, 2],
            "wild_sylow_3_normal": True,
        },
    ]
    for row in expected_p3_all_hits:
        row["decomposition_orbits_27"] = [3, 6, 9, 9]
        row["decomposition_orbits_36"] = p3_target_36
    def p3_deep_profile_summary(
        decomposition_tom_index: int, inertia_tom_index: int
    ) -> list[dict[str, Any]]:
        inversion_inertia = inertia_tom_index == 140
        return [
            {
                "central_action_multiplicity": 0,
                "inversion_action_multiplicity": 2 if inversion_inertia else 0,
                "multiplicity": 2,
                "normal_in_decomposition_multiplicity": (
                    2 if decomposition_tom_index == 140 else 0
                ),
                "normal_in_inertia_multiplicity": 2 if inversion_inertia else 0,
                "not_inertia_normal_multiplicity": 0 if inversion_inertia else 2,
                "tom_index": 6,
            },
            {
                "central_action_multiplicity": 0 if inversion_inertia else 1,
                "inversion_action_multiplicity": 1 if inversion_inertia else 0,
                "multiplicity": 1,
                "normal_in_decomposition_multiplicity": 1,
                "normal_in_inertia_multiplicity": 1,
                "not_inertia_normal_multiplicity": 0,
                "tom_index": 7,
            },
            {
                "central_action_multiplicity": 0,
                "inversion_action_multiplicity": 1,
                "multiplicity": 1,
                "normal_in_decomposition_multiplicity": 1,
                "normal_in_inertia_multiplicity": 1,
                "not_inertia_normal_multiplicity": 0,
                "tom_index": 8,
            },
        ]

    expected_p3_pairs = [
        {
            "deep_C3_profile_summary": p3_deep_profile_summary(140, 140),
            "deep_C3_subgroup_count": 4,
            "decomposition_tom_index": 140,
            "inertia_tom_index": 140,
            "residue_quotient_order": 1,
        },
        {
            "deep_C3_profile_summary": p3_deep_profile_summary(142, 142),
            "deep_C3_subgroup_count": 4,
            "decomposition_tom_index": 142,
            "inertia_tom_index": 142,
            "residue_quotient_order": 1,
        },
        {
            "deep_C3_profile_summary": p3_deep_profile_summary(206, 140),
            "deep_C3_subgroup_count": 4,
            "decomposition_tom_index": 206,
            "inertia_tom_index": 140,
            "residue_quotient_order": 2,
        },
        {
            "deep_C3_profile_summary": p3_deep_profile_summary(206, 142),
            "deep_C3_subgroup_count": 4,
            "decomposition_tom_index": 206,
            "inertia_tom_index": 142,
            "residue_quotient_order": 2,
        },
    ]
    if (
        p3["all_tom_decomposition_pattern_hits"] != expected_p3_all_hits
        or p3["valid_decomposition_inertia_pairs"] != expected_p3_pairs
    ):
        raise StrictDataError("p=3 all-ToM dual-action exhaustion changed")
    surviving_p3_pairs = [
        row
        for row in expected_p3_pairs
        if row["inertia_tom_index"] in serre_surviving_inertia_tom_indices
    ]
    deep_c3_normal_in_surviving_decomposition_groups = (
        [row["decomposition_tom_index"] for row in surviving_p3_pairs] == [140, 206]
        and all(
            next(
                profile
                for profile in row["deep_C3_profile_summary"]
                if profile["tom_index"] == 7
            )["normal_in_inertia_multiplicity"]
            == 1
            and next(
                profile
                for profile in row["deep_C3_profile_summary"]
                if profile["tom_index"] == 7
            )["normal_in_decomposition_multiplicity"]
            == 1
            for row in surviving_p3_pairs
        )
    )
    if not deep_c3_normal_in_surviving_decomposition_groups:
        raise StrictDataError("deep p=3 C3 is not normal in every surviving D")
    candidates = p3["inertia_candidates"]
    if type(candidates) is not list or [row.get("tom_index") for row in candidates] != [140, 142]:
        raise StrictDataError("p=3 dual-action filter did not leave exactly ToM 140/142")
    selected = next(
        row
        for row in candidates
        if row["tom_index"] == serre_surviving_inertia_tom_indices[0]
    )
    rejected = next(row for row in candidates if row is not selected)
    common_p3 = {
        "deep_id_group": [3, 1],
        "deep_orbits_27": [1] * 9 + [3] * 6,
        "fixed_dimensions_deep": [4, 10],
        "fixed_dimensions_inertia": [0, 3],
        "fixed_dimensions_wild": [0, 4],
        "inertia_orbits_27": [3, 6, 9, 9],
        "wild_id_group": [9, 2],
        "wild_orbits_27": [3, 3, 3, 9, 9],
    }
    for row in candidates:
        for key, value in common_p3.items():
            if not deep_exact(row.get(key), value):
                raise StrictDataError(f"p=3 candidate {row.get('tom_index')} failed {key}")
        if (
            row.get("deep_C3_profiles") != expected_deep_profiles
            or row.get("selected_deep_tom_index") != 7
            or row.get("selected_deep_tame_action")
            != ("inversion" if row.get("tom_index") == 140 else "central")
        ):
            raise StrictDataError("p=3 candidate preselected a deep C3 before exhaustion")
    if (
        selected.get("inertia_id_group") != [18, 4]
        or selected.get("central_deep_c3") is not False
        or rejected.get("inertia_id_group") != [18, 3]
        or rejected.get("central_deep_c3") is not True
    ):
        raise StrictDataError("p=3 candidates do not separate inversion from central action")
    decompositions = p3["decomposition_candidates"]
    if (
        type(decompositions) is not list
        or [row.get("tom_index") for row in decompositions] != [140, 142, 206]
        or [row.get("id_group") for row in decompositions]
        != [[18, 4], [18, 3], [36, 10]]
        or [row.get("contained_inertia") for row in decompositions]
        != [
            [{"inertia_tom_index": 140, "residue_quotient_order": 1}],
            [{"inertia_tom_index": 142, "residue_quotient_order": 1}],
            [
                {"inertia_tom_index": 140, "residue_quotient_order": 2},
                {"inertia_tom_index": 142, "residue_quotient_order": 2},
            ],
        ]
    ):
        raise StrictDataError("p=3 decomposition/inertia pair exhaustion changed")
    rich_p3 = require_exact_keys(
        rich["p3"],
        {
            "accepted_after_direct_and_serre_filters",
            "accepted_inertia_tom_index",
            "all_integral_discriminant_candidates",
            "all_tom_decomposition_pattern_hits",
            "central_competitor_tom_index",
            "decomposition_orders_not_resolved",
            "deep_C3_exhaustion",
            "deep_C3_normal_in_all_surviving_decomposition_groups",
            "deep_C3_pair_normal_multiplicities",
            "direct_pmaximal_27_target",
            "filtration_multiplicity_equation",
            "order_36_decomposition_tom_index",
            "p3_tame_quotient_filter_excludes_206_as_inertia",
            "rejected_non_C3_squared_wild",
            "serre_law",
            "valid_decomposition_inertia_pairs",
        },
        "producer p3 projection",
    )
    if (
        rich_p3["accepted_inertia_tom_index"] != 140
        or rich_p3["central_competitor_tom_index"] != 142
        or rich_p3["order_36_decomposition_tom_index"] != 206
        or rich_p3["decomposition_orders_not_resolved"] != [18, 36]
        or rich_p3["all_tom_decomposition_pattern_hits"]
        != [
            {key: value for key, value in row.items() if not key.startswith("decomposition_orbits_")}
            for row in expected_p3_all_hits
        ]
        or rich_p3["valid_decomposition_inertia_pairs"]
        != [
            [
                row["decomposition_tom_index"],
                row["inertia_tom_index"],
                row["residue_quotient_order"],
            ]
            for row in expected_p3_pairs
        ]
        or rich_p3["p3_tame_quotient_filter_excludes_206_as_inertia"] is not True
        or rich_p3["deep_C3_normal_in_all_surviving_decomposition_groups"] is not True
        or rich_p3["deep_C3_exhaustion"] != deep_c3_exhaustion
        or rich_p3["direct_pmaximal_27_target"]
        != [[3, 3, 1, 3], [6, 6, 1, 7], [9, 9, 1, 18], [9, 9, 1, 18]]
        or rich_p3["serre_law"]
        != {
            "central_competitor_rejected": True,
            "formula": "theta_i(s*tau*s^-1)=theta_0(s)^i*theta_i(tau)",
            "last_nonzero_grade": 7,
            "required_action": "inversion",
            "tame_character": -1,
        }
        or type(rich_p3["accepted_after_direct_and_serre_filters"]) is not list
        or [row.get("orders_P_I_D") for row in rich_p3["accepted_after_direct_and_serre_filters"]]
        != [[9, 18, 18], [9, 18, 36]]
        or type(rich_p3["all_integral_discriminant_candidates"]) is not list
        or [
            row.get("orders_P_I_D")
            for row in rich_p3["all_integral_discriminant_candidates"]
        ]
        != [[9, 18, 18], [9, 18, 18], [9, 18, 36], [9, 18, 36]]
        or type(rich_p3["rejected_non_C3_squared_wild"]) is not list
        or len(rich_p3["rejected_non_C3_squared_wild"]) != 2
        or rich_p3["filtration_multiplicity_equation"]
        != {
            "base_different_exponents": [2, 5, 8, 8],
            "layer_contributions": {
                "deep_C3_layers": [0, 0, 1, 1],
                "wild_C3_squared_layers": [1, 2, 4, 4],
            },
            "nonnegative_integer_solutions": [
                {"deep_C3_layers": 6, "wild_C3_squared_layers": 1}
            ],
            "search_box_inclusive_upper_bound": 19,
            "target_different_exponents": [3, 7, 18, 18],
            "unique": True,
        }
    ):
        raise StrictDataError("producer p=3 semantic projection disagrees with GAP/Serre replay")
    expected_rich_pair_normal_multiplicities = []
    profile_by_tom = {row["tom_index"]: row for row in expected_deep_profiles}
    for pair in expected_p3_pairs:
        rich_profiles = []
        for profile in pair["deep_C3_profile_summary"]:
            actions = []
            if profile["central_action_multiplicity"]:
                actions.append(["central", profile["central_action_multiplicity"]])
            if profile["inversion_action_multiplicity"]:
                actions.append(
                    ["inversion", profile["inversion_action_multiplicity"]]
                )
            if profile["not_inertia_normal_multiplicity"]:
                actions.append(["other", profile["not_inertia_normal_multiplicity"]])
            rich_profiles.append(
                {
                    "multiplicity": profile["multiplicity"],
                    "nonnegative_integer_solution_multiset": profile_by_tom[
                        profile["tom_index"]
                    ]["nonnegative_integer_solutions"],
                    "normal_in_decomposition_multiplicity": profile[
                        "normal_in_decomposition_multiplicity"
                    ],
                    "normal_in_inertia_multiplicity": profile[
                        "normal_in_inertia_multiplicity"
                    ],
                    "tame_actions": actions,
                    "tom_index": profile["tom_index"],
                }
            )
        expected_rich_pair_normal_multiplicities.append(
            {
                "decomposition_tom_index": pair["decomposition_tom_index"],
                "inertia_tom_index": pair["inertia_tom_index"],
                "orders_P_I_D": [
                    9,
                    18,
                    18 if pair["decomposition_tom_index"] in (140, 142) else 36,
                ],
                "profiles": rich_profiles,
                "simultaneous_conjugacy_orbit_size": 720,
            }
        )
    if (
        rich_p3["deep_C3_pair_normal_multiplicities"]
        != expected_rich_pair_normal_multiplicities
    ):
        raise StrictDataError("producer deep-C3 pair multiplicities disagree with GAP")

    p5 = report.get("p5_filter")
    expected_p5_all_hits = [
        {
            "id_group": [20, 3],
            "order": 20,
            "sylow_5_normal": True,
            "sylow_5_normalizer_order": 40,
            "tom_index": 147,
        },
        {
            "id_group": [60, 5],
            "order": 60,
            "sylow_5_normal": False,
            "sylow_5_normalizer_order": 40,
            "tom_index": 247,
        },
        {
            "id_group": [120, 34],
            "order": 120,
            "sylow_5_normal": False,
            "sylow_5_normalizer_order": 40,
            "tom_index": 295,
        },
    ]
    for row in expected_p5_all_hits:
        row["decomposition_orbits_27"] = [1, 1, 5, 5, 5, 10]
        row["decomposition_orbits_36"] = p5_target_36
    if (
        type(p5) is not dict
        or set(p5)
        != {
            "all_tom_decomposition_pattern_hits",
            "inertia_candidates",
            "valid_decomposition_inertia_pairs",
        }
        or p5.get("all_tom_decomposition_pattern_hits") != expected_p5_all_hits
        or p5.get("valid_decomposition_inertia_pairs")
        != [
            {
                "decomposition_tom_index": 147,
                "inertia_tom_index": 147,
                "residue_quotient_order": 1,
            }
        ]
        or type(p5.get("inertia_candidates")) is not list
        or len(p5["inertia_candidates"]) != 1
    ):
        raise StrictDataError("p=5 dual-action exhaustive filter mismatch")
    p5_selected = p5["inertia_candidates"][0]
    for key, value in {
        "fixed_dimensions_inertia": [2, 3],
        "fixed_dimensions_wild": [2, 4],
        "inertia_id_group": [20, 3],
        "inertia_orbits_27": [1, 1, 5, 5, 5, 10],
        "inertia_orbits_36": p5_target_36,
        "tom_index": 147,
        "wild_central": False,
        "wild_id_group": [5, 1],
        "wild_normal": True,
        "wild_orbits_27": [1, 1, 5, 5, 5, 5, 5],
    }.items():
        if not deep_exact(p5_selected.get(key), value):
            raise StrictDataError(f"p=5 selected inertia failed {key}")
    p5_local_summary = next(
        (
            row
            for row in degree36_authority.get("local_summaries", [])
            if row.get("prime") == 5
        ),
        None,
    )
    if (
        p5_selected.get("wild_normalizer_order") != 40
        or p5_selected.get("normalizer_order") != 40
        or type(p5_local_summary) is not dict
        or not p5_local_summary.get("rows_e_f_d")
        or any(row[1] != 1 for row in p5_local_summary["rows_e_f_d"])
    ):
        raise StrictDataError(
            "p=5 normal-wild normalizer/residue-degree filter is incomplete"
        )
    rich_p5 = require_exact_keys(
        rich["p5"],
        {
            "candidate",
            "dual_action_hit_counts_by_order",
            "all_tom_decomposition_pattern_hits",
            "inertia_and_decomposition_tom_index",
            "filtration_equation",
            "lattice_orders",
            "valid_decomposition_inertia_pairs",
            "wild_normalizer_filter_unique",
            "wild_normalizer_order",
        },
        "producer p5 projection",
    )
    p5_filtration_equation = {
        "base_different_vector_num_den": [
            [0, 1],
            [0, 1],
            [4, 1],
            [4, 1],
            [4, 1],
            [9, 1],
        ],
        "formal_integer_solution": 3,
        "nonnegative_integer_solutions": [3],
        "solution_variable": "wild_C5_layers",
        "target_different_vector_num_den": [
            [0, 1],
            [0, 1],
            [7, 1],
            [7, 1],
            [7, 1],
            [15, 1],
        ],
        "unique": True,
        "wild_C5_per_layer_contribution_num_den": [
            [0, 1],
            [0, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [2, 1],
        ],
    }
    p5_base = rational_vector_from_num_den(
        p5_filtration_equation["base_different_vector_num_den"], "p=5 base"
    )
    p5_target = rational_vector_from_num_den(
        p5_filtration_equation["target_different_vector_num_den"], "p=5 target"
    )
    p5_layer = rational_vector_from_num_den(
        p5_filtration_equation["wild_C5_per_layer_contribution_num_den"],
        "p=5 wild layer",
    )
    p5_solution_candidates = {
        (p5_target[index] - p5_base[index]) / p5_layer[index]
        for index in range(len(p5_base))
        if p5_layer[index]
    }
    if (
        any(
            p5_target[index] != p5_base[index]
            for index in range(len(p5_base))
            if not p5_layer[index]
        )
        or p5_solution_candidates != {Fraction(3)}
        or rich_p5["filtration_equation"] != p5_filtration_equation
    ):
        raise StrictDataError("producer p=5 filtration equation failed Fraction replay")
    if (
        rich_p5["dual_action_hit_counts_by_order"]
        != {"5": 0, "10": 0, "20": 1, "40": 0}
        or rich_p5["all_tom_decomposition_pattern_hits"]
        != [
            {key: value for key, value in row.items() if not key.startswith("decomposition_orbits_")}
            for row in expected_p5_all_hits
        ]
        or rich_p5["valid_decomposition_inertia_pairs"] != [[147, 147, 1]]
        or rich_p5["wild_normalizer_filter_unique"] is not True
        or rich_p5["inertia_and_decomposition_tom_index"] != 147
        or rich_p5["lattice_orders"] != {"5": 1, "10": 3, "20": 3, "40": 1}
        or rich_p5["wild_normalizer_order"] != 40
        or rich_p5["candidate"].get("lower_filtration_orders") != [20, 5, 5, 5, 1]
        or rich_p5["candidate"].get("orders_P_I_D") != [5, 20, 20]
        or rich_p5["candidate"].get("representation")
        != {
            "artin": [7, 29],
            "inertia_codimensions": [4, 17],
            "inertia_invariant_dimensions": [2, 3],
            "swan": [3, 12],
        }
    ):
        raise StrictDataError("producer p=5 semantic projection disagrees with GAP replay")

    order3 = report.get("order3_classes")
    order2 = report.get("order2_classes")
    if type(order3) is not list or [row.get("tom_index") for row in order3] != [6, 7, 8]:
        raise StrictDataError("order-3 class exhaustion mismatch")
    theta_tame_authority = degree36_authority.get(
        "degree36_local_factors", {}
    ).get("theta", {})
    if (
        set(theta_tame_authority) != {str(prime) for prime in C3_PRIMES}
        or {
            record.get("total_discriminant_exponent")
            for record in theta_tame_authority.values()
        }
        != {24}
    ):
        raise StrictDataError("tame theta36 local authority is incomplete")
    tame_degree_only_candidates = [
        row for row in order3 if row.get("orbits_27") == [3] * 9
    ]
    tame_selected_candidates = [
        row
        for row in tame_degree_only_candidates
        if 36 - len(row.get("orbits_36", [])) == 24
    ]
    if len(tame_degree_only_candidates) != 2 or len(tame_selected_candidates) != 1:
        raise StrictDataError("tame C3 local exponent does not select a unique ToM class")
    tame_selected = tame_selected_candidates[0]
    tame_competitor = next(
        row for row in tame_degree_only_candidates if row is not tame_selected
    )
    if (
        tame_selected["orbits_27"] != [3] * 9
        or tame_selected["orbits_36"] != [3] * 12
        or tame_selected["fixed_dimensions"] != [0, 8]
        or tame_competitor["orbits_27"] != [3] * 9
        or tame_competitor["orbits_36"] != [1] * 3 + [3] * 11
        or tame_competitor["fixed_dimensions"] != [2, 6]
    ):
        raise StrictDataError("tame C3 class separation mismatch")
    tame_pairs = report.get("tame_c3_dual_filter")
    if (
        type(tame_pairs) is not list
        or len(tame_pairs) != 3
        or [row.get("inertia_tom_index") for row in tame_pairs] != [6, 8, 6]
        or any(row.get("decomposition_tom_index") != 141 for row in tame_pairs)
        or any(row.get("decomposition_id_group") != [18, 5] for row in tame_pairs)
        or any(row.get("decomposition_order") != 18 for row in tame_pairs)
        or any(row.get("quotient_order") != 6 for row in tame_pairs)
        or any(row.get("decomposition_orbits_27") != [3, 6, 18] for row in tame_pairs)
        or any(row.get("decomposition_orbits_36") != [3, 6, 9, 18] for row in tame_pairs)
    ):
        raise StrictDataError("tame C3 inertia/decomposition pair exhaustion changed")
    if degree36_authority.get("degree36_precision_gate") != {
        "authoritative_resolver": "theta",
        "authority_precision": 40,
        "delta_authority_bound_satisfied": False,
        "delta_max_factor_polynomial_discriminant_exponent": 204,
        "delta_precision_exceeds_global_polynomial_discriminant_exponent": False,
        "delta_precision_exceeds_twice_max_factor_discriminant_exponent": False,
        "delta_global_polynomial_discriminant_exponent": 840,
        "delta_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
        "delta_twice_max_factor_discriminant_exponent": 408,
        "selection_uses_delta_as_authority": False,
        "theta_authority_bound_satisfied": True,
        "theta_max_factor_polynomial_discriminant_exponent": 12,
        "theta_precision_exceeds_global_polynomial_discriminant_exponent": True,
        "theta_precision_exceeds_twice_max_factor_discriminant_exponent": True,
        "theta_global_polynomial_discriminant_exponent": 24,
        "theta_role": "KRASNER_CERTIFIED_AUTHORITY",
        "theta_twice_max_factor_discriminant_exponent": 24,
    }:
        raise StrictDataError("tame C3 class selection lacks independent precision authority")
    theta_authority = degree36_authority.get("degree36_local_factors", {}).get("theta", {})
    delta_nonresult = degree36_authority.get("degree36_local_factors", {}).get("delta", {})
    if (
        set(theta_authority) != {str(prime) for prime in C3_PRIMES}
        or any(
            record.get("total_discriminant_exponent") != 24
            or record.get("authority_role") != "KRASNER_CERTIFIED_AUTHORITY"
            or record.get("authority_bound_satisfied") is not True
            for record in theta_authority.values()
        )
        or set(delta_nonresult) != {str(prime) for prime in C3_PRIMES}
        or any(
            record.get("authority_role") != "BOUNDED_NON_RESULT_NONDEPENDENCY"
            or record.get("authority_bound_satisfied") is not False
            for record in delta_nonresult.values()
        )
    ):
        raise StrictDataError("theta authority/delta nondependency firewall failed")
    selected_codimension_36 = 36 - len(tame_selected["orbits_36"])
    competitor_codimension_36 = 36 - len(tame_competitor["orbits_36"])
    if selected_codimension_36 != 24 or competitor_codimension_36 != 22:
        raise StrictDataError("degree-36 permutation conductors do not separate ToM 6/8")

    rich_tame = require_exact_keys(
        rich["tame_C3"],
        {
            "all_order_three_classes",
            "decomposition_filter",
            "degree_only_competitor",
            "degree_only_competitor_artin_V6_V20",
            "local_degree_36_selected",
            "selected_artin_V6_V20",
        },
        "producer tame C3 projection",
    )
    rich_filter = rich_tame["decomposition_filter"]
    require_exact_keys(
        rich_filter,
        {
            "all_inertia_classes",
            "decomposition_degree_carriers_unique_inertia",
            "degree_27_decomposition_orbits",
            "degree_36_decomposition_orbits",
            "degree_36_local_authority",
            "degree_36_local_discriminant_exponent",
            "degree_36_local_rows_target",
            "degree_36_local_rows_unique_inertia",
            "degree_only_surviving_inertia_classes",
            "delta36_role",
            "direct_degree_27_local_target",
            "selected_inertia_class",
            "selected_inertia_tom_index",
            "surviving_inertia_classes",
        },
        "producer tame decomposition filter",
    )
    if (
        rich_filter["decomposition_degree_carriers_unique_inertia"] is not False
        or rich_filter["degree_27_decomposition_orbits"] != [3, 6, 18]
        or rich_filter["degree_36_decomposition_orbits"] != [3, 6, 9, 18]
        or rich_filter["degree_36_local_authority"]
        != "theta36_KRASNER_CERTIFIED_AUTHORITY"
        or rich_filter["degree_36_local_discriminant_exponent"] != selected_codimension_36
        or rich_filter["degree_36_local_rows_target"]
        != [[3, 3, 1, 2], [6, 3, 2, 2], [9, 3, 3, 2], [18, 3, 6, 2]]
        or rich_filter["degree_36_local_rows_unique_inertia"] is not True
        or rich_filter["delta36_role"] != "BOUNDED_NON_RESULT_NONDEPENDENCY"
        or rich_filter["direct_degree_27_local_target"]
        != [[3, 3, 1, 2], [6, 3, 2, 2], [18, 3, 6, 2]]
        or rich_filter["selected_inertia_tom_index"] != 6
        or len(rich_filter["all_inertia_classes"]) != 3
        or len(rich_filter["degree_only_surviving_inertia_classes"]) != 2
        or len(rich_filter["surviving_inertia_classes"]) != 1
        or rich_tame["selected_artin_V6_V20"] != [6, 12]
        or rich_tame["degree_only_competitor_artin_V6_V20"] != [4, 14]
    ):
        raise StrictDataError("producer tame-C3 projection disagrees with GAP/PARI selection")
    if type(order2) is not list or [row.get("tom_index") for row in order2] != [2, 3, 4, 5]:
        raise StrictDataError("order-2 class exhaustion mismatch")
    reflection_candidates = [
        row
        for row in order2
        if row.get("orbits_27") == [1] * 15 + [2] * 6
        and row.get("orbits_36") == [1] * 16 + [2] * 10
        and row.get("fixed_dimensions") == [5, 15]
    ]
    field_signature = degree36_authority.get("field_signature")
    theta36_real_root_count = degree36_authority.get("theta36_real_root_count")
    if (
        type(field_signature) is not list
        or len(field_signature) != 2
        or any(type(value) is not int for value in field_signature)
        or type(theta36_real_root_count) is not int
    ):
        raise StrictDataError("PARI archimedean authority is absent from group replay")
    complex_candidates = [
        row
        for row in order2
        if row.get("orbits_27", []).count(1) == field_signature[0]
        and row.get("orbits_36", []).count(1) == theta36_real_root_count
    ]
    if len(reflection_candidates) != 1 or len(complex_candidates) != 1:
        raise StrictDataError("geometric/archimedean data do not select unique order-2 classes")
    reflection = reflection_candidates[0]
    complex_conjugation = complex_candidates[0]
    if (
        reflection["orbits_27"] != [1] * 15 + [2] * 6
        or reflection["fixed_dimensions"] != [5, 15]
        or complex_conjugation["orbits_27"] != [1] * 3 + [2] * 12
        or complex_conjugation["orbits_36"] != [1] * 4 + [2] * 16
        or complex_conjugation["fixed_dimensions"] != [3, 11]
    ):
        raise StrictDataError("reflection/complex-conjugation class mismatch")
    order2_character_map = report.get("order2_character_table_map")
    if type(order2_character_map) is not list or len(order2_character_map) != len(order2):
        raise StrictDataError("order-2 character-table map is missing")
    map_by_tom = {}
    character_map_keys = {
        "character_table_group_order",
        "character_table_name",
        "element_centralizer_order",
        "element_class_index",
        "element_class_matching_indices",
        "element_class_order",
        "element_class_size",
        "subgroup_generator_centralizer_order",
        "subgroup_normalizer_order",
        "subgroup_order",
        "subgroup_tom_index",
        "unique_order_and_class_size_match",
    }
    order2_by_tom = {row["tom_index"]: row for row in order2}
    for mapping in order2_character_map:
        require_exact_keys(mapping, character_map_keys, "order-2 character-table map")
        tom_index = mapping["subgroup_tom_index"]
        source_row = order2_by_tom.get(tom_index)
        if (
            tom_index in map_by_tom
            or source_row is None
            or mapping["character_table_group_order"] != 51840
            or mapping["character_table_name"] != "U4(2).2"
            or mapping["subgroup_order"] != 2
            or mapping["element_class_order"] != 2
            or mapping["subgroup_normalizer_order"] != source_row["normalizer_order"]
            or mapping["subgroup_generator_centralizer_order"]
            != source_row["normalizer_order"]
            or mapping["element_centralizer_order"] != source_row["normalizer_order"]
            or mapping["element_class_size"]
            != 51840 // source_row["normalizer_order"]
            or mapping["element_class_matching_indices"]
            != [mapping["element_class_index"]]
            or mapping["unique_order_and_class_size_match"] is not True
        ):
            raise StrictDataError("order-2 ToM/character-table derivation is inconsistent")
        map_by_tom[tom_index] = mapping
    if set(map_by_tom) != set(order2_by_tom):
        raise StrictDataError("order-2 ToM/character-table map is not exhaustive")

    def orbit_run_length(orbit_sizes: list[int]) -> list[list[int]]:
        if not orbit_sizes or orbit_sizes != sorted(orbit_sizes):
            raise StrictDataError("order-2 orbit carrier is not canonically sorted")
        result: list[list[int]] = []
        for size in orbit_sizes:
            if result and result[-1][0] == size:
                result[-1][1] += 1
            else:
                result.append([size, 1])
        return result

    order2_profiles = [
        {
            "character_table_element_class_index": map_by_tom[row["tom_index"]][
                "element_class_index"
            ],
            "double_six_orbit_rle": orbit_run_length(row["orbits_36"]),
            "element_class_size": map_by_tom[row["tom_index"]][
                "element_class_size"
            ],
            "fixed_dimensions_V6_V20": row["fixed_dimensions"],
            "line_orbit_rle": orbit_run_length(row["orbits_27"]),
            "normalizer_order": row["normalizer_order"],
            "tom_index": row["tom_index"],
        }
        for row in order2
    ]
    if order2_profiles != [
        {
            "character_table_element_class_index": 16,
            "double_six_orbit_rle": [[1, 16], [2, 10]],
            "element_class_size": 36,
            "fixed_dimensions_V6_V20": [5, 15],
            "line_orbit_rle": [[1, 15], [2, 6]],
            "normalizer_order": 1440,
            "tom_index": 2,
        },
        {
            "character_table_element_class_index": 2,
            "double_six_orbit_rle": [[1, 12], [2, 12]],
            "element_class_size": 45,
            "fixed_dimensions_V6_V20": [2, 12],
            "line_orbit_rle": [[1, 3], [2, 12]],
            "normalizer_order": 1152,
            "tom_index": 3,
        },
        {
            "character_table_element_class_index": 3,
            "double_six_orbit_rle": [[1, 8], [2, 14]],
            "element_class_size": 270,
            "fixed_dimensions_V6_V20": [4, 12],
            "line_orbit_rle": [[1, 7], [2, 10]],
            "normalizer_order": 192,
            "tom_index": 4,
        },
        {
            "character_table_element_class_index": 17,
            "double_six_orbit_rle": [[1, 4], [2, 16]],
            "element_class_size": 540,
            "fixed_dimensions_V6_V20": [3, 11],
            "line_orbit_rle": [[1, 3], [2, 12]],
            "normalizer_order": 96,
            "tom_index": 5,
        },
    ]:
        raise StrictDataError("exhaustive order-2 reflection/infinity profiles changed")
    if rich["order_two_tom_profiles"] != order2_profiles:
        raise StrictDataError("producer order-2 profiles disagree with exhaustive GAP scan")
    tom_exhaustion = require_exact_keys(
        rich["tom_dual_action_exhaustion"],
        {
            "complex_conjugation_character_match",
            "order_two_profiles_without_picard",
            "p3_all_tom_decomposition_pattern_hits",
            "p3_valid_decomposition_inertia_pairs",
            "p5_all_tom_decomposition_pattern_hits",
            "p5_valid_decomposition_inertia_pairs",
            "table_of_marks_class_count",
            "table_of_marks_name",
        },
        "producer all-ToM exhaustion",
    )
    complex_map = map_by_tom[complex_conjugation["tom_index"]]
    expected_complex_map = {
        key: complex_map[key]
        for key in (
            "character_table_group_order",
            "character_table_name",
            "element_centralizer_order",
            "element_class_index",
            "element_class_matching_indices",
            "element_class_order",
            "element_class_size",
            "subgroup_normalizer_order",
            "subgroup_order",
            "subgroup_tom_index",
            "unique_order_and_class_size_match",
        )
    }
    profiles_without_picard = [
        {
            key: value
            for key, value in profile.items()
            if key != "fixed_dimensions_V6_V20"
        }
        for profile in order2_profiles
    ]
    if (
        tom_exhaustion["table_of_marks_class_count"] != 350
        or tom_exhaustion["table_of_marks_name"] != "U4(2).2"
        or tom_exhaustion["order_two_profiles_without_picard"]
        != profiles_without_picard
        or tom_exhaustion["complex_conjugation_character_match"]
        != expected_complex_map
        or tom_exhaustion["p3_all_tom_decomposition_pattern_hits"]
        != rich_p3["all_tom_decomposition_pattern_hits"]
        or tom_exhaustion["p3_valid_decomposition_inertia_pairs"]
        != rich_p3["valid_decomposition_inertia_pairs"]
        or tom_exhaustion["p5_all_tom_decomposition_pattern_hits"]
        != rich_p5["all_tom_decomposition_pattern_hits"]
        or tom_exhaustion["p5_valid_decomposition_inertia_pairs"]
        != rich_p5["valid_decomposition_inertia_pairs"]
    ):
        raise StrictDataError("producer all-ToM exhaustion disagrees with GAP replay")
    complex_character_mapping = map_by_tom[complex_conjugation["tom_index"]]
    def rich_class_projection(row: dict[str, Any], order: int) -> dict[str, Any]:
        subgroup_class_size = 51840 // row["normalizer_order"]
        return {
            "class_size": subgroup_class_size * (2 if order == 3 else 1),
            "double_six_orbits": row["orbits_36"],
            "invariant_dimensions_V6_V20": row["fixed_dimensions"],
            "line_orbits": row["orbits_27"],
            "normalizer_order": row["normalizer_order"],
            "normalizer_realizes_inversion": True,
            "order": order,
            "subgroup_class_size": subgroup_class_size,
        }

    rich_order3 = sorted(
        rich_tame["all_order_three_classes"],
        key=lambda row: tuple(row["invariant_dimensions_V6_V20"]),
    )
    checker_order3 = sorted(
        (rich_class_projection(row, 3) for row in order3),
        key=lambda row: tuple(row["invariant_dimensions_V6_V20"]),
    )
    rich_infinity = require_exact_keys(
        rich["complex_conjugation"],
        {
            "V20_signature",
            "V6_signature",
            "character_table_match",
            "class_record",
            "element_class_index",
            "subgroup_tom_index",
        },
        "producer infinity projection",
    )
    if (
        rich_order3 != checker_order3
        or rich["reflection"] != rich_class_projection(reflection, 2)
        or rich_infinity["class_record"] != rich_class_projection(complex_conjugation, 2)
        or rich_infinity["V6_signature"] != [3, 3]
        or rich_infinity["V20_signature"] != [11, 9]
        or rich_infinity["character_table_match"] != expected_complex_map
        or rich_infinity["element_class_index"]
        != complex_character_mapping["element_class_index"]
        or rich_infinity["subgroup_tom_index"]
        != complex_character_mapping["subgroup_tom_index"]
    ):
        raise StrictDataError("producer conjugacy-class projection disagrees with checker GAP")
    if rich["upstream_lock"] != {
        "c56_carriers_deep_equal": True,
        "c56_certificate_sha256": UPSTREAM_FILES[
            "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json"
        ][1],
        "c57_carrier_sha256": "9925488d85758c933893a06a152a113fc2971071f60c249b438624cd532c681d",
        "c57_group_source_sha256": UPSTREAM_FILES[
            "henon_dynamics/henon_mu3_yukawa_minimal_brauer_jump/code/c57_group.py"
        ][1],
        "c57_import_carriers_immutable": True,
    }:
        raise StrictDataError("producer rich report upstream lock changed")
    return {
        "complex_conjugation": complex_conjugation,
        "complex_conjugation_character_mapping": complex_character_mapping,
        "decomposition_candidates_p3": decompositions,
        "gap_report_sha256": report_sha,
        "labelled_carrier_sha256": labelled["canonical_sha256"],
        "line_action_faithful": True,
        "p3_all_tom_decomposition_pattern_hits": [
            [row["tom_index"], row["order"], row["id_group"]]
            for row in expected_p3_all_hits
        ],
        "p3_rejected_central": rejected,
        "p3_selected": selected,
        "p3_tame_quotient_filter_excludes_206_as_inertia": True,
        "deep_C3_normal_in_all_surviving_decomposition_groups": (
            deep_c3_normal_in_surviving_decomposition_groups
        ),
        "p3_valid_decomposition_inertia_pairs": [
            [
                row["decomposition_tom_index"],
                row["inertia_tom_index"],
                row["residue_quotient_order"],
            ]
            for row in expected_p3_pairs
        ],
        "p5_all_tom_decomposition_pattern_hits": [
            [row["tom_index"], row["order"], row["id_group"]]
            for row in expected_p5_all_hits
        ],
        "p5_selected": p5_selected,
        "p5_filtration_equation": p5_filtration_equation,
        "p5_valid_decomposition_inertia_pairs": [[147, 147, 1]],
        "p5_wild_normalizer_filter_unique": True,
        "reflection": reflection,
        "deep_C3_exhaustion": deep_c3_exhaustion,
        "order2_profiles": order2_profiles,
        "tame_C3_competitor": tame_competitor,
        "tame_C3_dual_pair_candidates": tame_pairs,
        "tame_C3_selection_authority": {
            "competitor_degree36_conductor": competitor_codimension_36,
            "selected_degree36_conductor": selected_codimension_36,
            "selected_by_independent_local_exponent": 24,
        },
        "tame_C3_selected": tame_selected,
    }


def normalized_image_pairs(isomorphism: dict[str, Any]) -> list[list[int]]:
    denominator = isomorphism["original_generator_image_common_denominator"]
    result = []
    for numerator in isomorphism["original_generator_image_numerators_low_to_high"]:
        divisor = math.gcd(abs(numerator), denominator)
        result.append([numerator // divisor, denominator // divisor])
    while len(result) < 27:
        result.append([0, 1])
    return result


def pari_replay(
    evidence: dict[str, Any],
    original_coefficients: list[int],
    resolvers: dict[str, list[int]],
    pari_python: Path,
    scratch_parent: Path,
) -> tuple[dict[str, Any], str]:
    if (
        not scratch_parent.is_absolute()
        or not scratch_parent.is_dir()
        or scratch_parent.is_symlink()
        or scratch_parent.resolve(strict=True) != scratch_parent
    ):
        raise StrictDataError(
            "checker PARI scratch parent must be the verified real stage directory"
        )
    maximal = evidence["maximal_order"]
    isomorphism = evidence["field_isomorphism"]
    image_authority = {
        "common_denominator": isomorphism["original_generator_image_common_denominator"],
        "numerators_low_to_high": isomorphism[
            "original_generator_image_numerators_low_to_high"
        ],
    }
    if (
        isomorphism["original_generator_image_canonical_sha256"]
        != sha256_bytes(canonical_leaf_bytes(image_authority))
    ):
        raise StrictDataError("original-generator image digest mismatch")
    if (
        maximal["transformed_monic_polynomial_sha256"]
        != sha256_bytes(
            canonical_leaf_bytes(
                maximal["transformed_monic_polynomial_coefficients_low_to_high"]
            )
        )
        or maximal["integral_basis_canonical_sha256"]
        != sha256_bytes(
            canonical_leaf_bytes(
                maximal["integral_basis_coefficients_low_to_high_as_num_den"]
            )
        )
    ):
        raise StrictDataError("maximal-order carrier digest mismatch")
    local_records = [
        {
            "prime": prime,
            "prime_ideals": evidence["local_prime_ideals"][str(prime)],
        }
        for prime in DIRECT_PRIMES
    ]
    request = {
        "direct_primes": list(DIRECT_PRIMES),
        "degree36_resolvers": resolvers,
        "expected_degree36_local_factors": {
            "delta": evidence["degree36_local_factors"]["delta36"],
            "theta": evidence["degree36_local_factors"]["theta36"],
        },
        "expected_local_prime_ideals": local_records,
        "expected_padic_factor_degrees": evidence["padic_factor_degrees"],
        "integral_basis_coefficients_low_to_high_as_num_den": maximal[
            "integral_basis_coefficients_low_to_high_as_num_den"
        ],
        "original_generator_image_coefficients_low_to_high_as_num_den": normalized_image_pairs(
            isomorphism
        ),
        "original_polynomial_coefficients_low_to_high": original_coefficients,
        "schema_id": "hcs-c58-checker-pari-request-v1",
        "surface_bad_prime_envelope": list(SUPPORT),
        "transformed_monic_polynomial_coefficients_low_to_high": maximal[
            "transformed_monic_polynomial_coefficients_low_to_high"
        ],
    }
    with tempfile.TemporaryDirectory(
        prefix=".c58-checker-pari-", dir=scratch_parent
    ) as directory:
        scratch = Path(directory)
        if (
            scratch.parent != scratch_parent
            or scratch.is_symlink()
            or scratch.resolve(strict=True) != scratch
        ):
            raise StrictDataError("checker PARI scratch directory identity mismatch")
        request_path = scratch / "request.json"
        request_bytes = canonical_json_bytes(request)
        request_path.write_bytes(request_bytes)
        request_raw_before, request_fingerprint_before = read_stable(
            request_path, max_bytes=8_000_000
        )
        request_metadata_before = request_path.stat(follow_symlinks=False)
        if request_raw_before != request_bytes or request_metadata_before.st_nlink != 1:
            raise StrictDataError("checker PARI request initialization mismatch")
        report, digest = run_canonical_report(
            pari_python,
            CODE / "c58_checker_pari.py",
            [request_path],
            timeout=1800,
            max_stdout_bytes=5_000_000,
        )
        request_raw_after, request_fingerprint_after = read_stable(
            request_path, max_bytes=8_000_000
        )
        request_metadata_after = request_path.stat(follow_symlinks=False)
        request_identity_before = (
            request_metadata_before.st_dev,
            request_metadata_before.st_ino,
            request_metadata_before.st_nlink,
            request_metadata_before.st_size,
            request_metadata_before.st_mode,
            request_metadata_before.st_mtime_ns,
            request_metadata_before.st_ctime_ns,
        )
        request_identity_after = (
            request_metadata_after.st_dev,
            request_metadata_after.st_ino,
            request_metadata_after.st_nlink,
            request_metadata_after.st_size,
            request_metadata_after.st_mode,
            request_metadata_after.st_mtime_ns,
            request_metadata_after.st_ctime_ns,
        )
        if (
            request_raw_after != request_raw_before
            or request_fingerprint_after != request_fingerprint_before
            or request_identity_after != request_identity_before
        ):
            raise StrictDataError("checker PARI request changed across child replay")
    if (
        report.get("field_discriminant_decimal_newline_sha256")
        != evidence["field_discriminant"]["decimal_newline_sha256"]
        or report.get("field_discriminant_digits") != evidence["field_discriminant"]["digits"]
        or report.get("field_discriminant_exponents_on_surface_bad_prime_envelope")
        != evidence["field_discriminant"]["exponents_on_surface_bad_prime_envelope"]
        or report.get("field_discriminant_positive") is not True
        or report.get("basis_pari_text_sha256") != maximal["integral_basis_pari_text_sha256"]
        or report.get("basis_pari_text_size_bytes") != maximal["integral_basis_pari_text_size_bytes"]
        or report.get("nfcertify_unresolved") != []
        or report.get("generator_image_proves_oriented_field_identity") is not True
        or report.get("surface_bad_prime_envelope_isprime") != [True] * len(SUPPORT)
    ):
        raise StrictDataError("PARI report does not rebind maximal-order/field identity evidence")
    field_signature = report.get("field_signature")
    theta36_real_root_count = report.get("theta36_real_root_count")
    if (
        type(field_signature) is not list
        or len(field_signature) != 2
        or any(type(value) is not int or value < 0 for value in field_signature)
        or field_signature[0] + 2 * field_signature[1] != 27
        or field_signature != [3, 12]
        or type(theta36_real_root_count) is not int
        or not 0 <= theta36_real_root_count <= 36
        or theta36_real_root_count != 4
    ):
        raise StrictDataError("independent PARI archimedean counts are malformed")
    if report.get("wild_degree36_theta_authority") != WILD_THETA_AUTHORITY_EXPECTED:
        raise StrictDataError("wild theta36 precision authority replay changed")
    expected_rows = {
        3: [[3, 1, 3], [6, 1, 7], [9, 1, 18], [9, 1, 18]],
        5: [[1, 1, 0], [1, 1, 0], [5, 1, 7], [5, 1, 7], [5, 1, 7], [10, 1, 15]],
        181: [[3, 1, 2], [3, 2, 2], [3, 6, 2]],
        997: [[3, 1, 2], [3, 2, 2], [3, 6, 2]],
        2346241: [[3, 1, 2], [3, 2, 2], [3, 6, 2]],
    }
    observed_rows = {
        row["prime"]: row["rows_e_f_d"] for row in report.get("local_summaries", [])
    }
    if observed_rows != expected_rows:
        raise StrictDataError("independent PARI local rows do not match the theorem bundle")
    expected_factor_degrees = {
        "3": [[3, 1], [6, 1], [9, 2]],
        "5": [[1, 2], [5, 3], [10, 1]],
        "181": [[3, 1], [6, 1], [18, 1]],
        "997": [[3, 1], [6, 1], [18, 1]],
        "2346241": [[3, 1], [6, 1], [18, 1]],
    }
    if report.get("padic_factor_degrees") != expected_factor_degrees:
        raise StrictDataError("local Q_p factor degrees changed")
    expected_resolver_factors = {
        name: {
            "3": [[3, 1], [3, 1], [3, 1], [9, 1], [18, 1]],
            "5": [[1, 1], [5, 1], [10, 1], [10, 1], [10, 1]],
            "181": [[3, 1], [6, 1], [9, 1], [18, 1]],
            "997": [[3, 1], [6, 1], [9, 1], [18, 1]],
            "2346241": [[3, 1], [6, 1], [9, 1], [18, 1]],
        }
        for name in ("delta", "theta")
    }
    if report.get("degree36_factor_degrees") != expected_resolver_factors:
        raise StrictDataError("degree-36 dual resolver replay mismatch")
    expected_tame_local = {
        "delta": evidence["degree36_local_factors"]["delta36"],
        "theta": evidence["degree36_local_factors"]["theta36"],
    }
    if report.get("degree36_local_factors") != expected_tame_local:
        raise StrictDataError("degree-36 tame local rows disagree with evidence")
    if report.get("degree36_precision_gate") != {
        "authoritative_resolver": "theta",
        "authority_precision": 40,
        "delta_authority_bound_satisfied": False,
        "delta_max_factor_polynomial_discriminant_exponent": 204,
        "delta_precision_exceeds_global_polynomial_discriminant_exponent": False,
        "delta_precision_exceeds_twice_max_factor_discriminant_exponent": False,
        "delta_global_polynomial_discriminant_exponent": 840,
        "delta_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
        "delta_twice_max_factor_discriminant_exponent": 408,
        "selection_uses_delta_as_authority": False,
        "theta_authority_bound_satisfied": True,
        "theta_max_factor_polynomial_discriminant_exponent": 12,
        "theta_precision_exceeds_global_polynomial_discriminant_exponent": True,
        "theta_precision_exceeds_twice_max_factor_discriminant_exponent": True,
        "theta_global_polynomial_discriminant_exponent": 24,
        "theta_role": "KRASNER_CERTIFIED_AUTHORITY",
        "theta_twice_max_factor_discriminant_exponent": 24,
    }:
        raise StrictDataError("degree-36 precision/discriminant stability gate failed")
    expected_hensel = {
        name: {str(prime): [20, 30, 40] for prime in DIRECT_PRIMES}
        for name in ("delta", "theta")
    }
    if report.get("degree36_hensel_product_congruences") != expected_hensel:
        raise StrictDataError("degree-36 Hensel product congruence replay failed")
    return report, digest


def artin_from_filtration(
    dimension: int, group_orders: list[int], fixed_dimensions: list[int]
) -> tuple[int, int]:
    if len(group_orders) != len(fixed_dimensions) or not group_orders:
        raise StrictDataError("filtration character vectors have inconsistent lengths")
    inertia_order = group_orders[0]
    swan = sum(
        Fraction(order, inertia_order) * (dimension - fixed)
        for order, fixed in zip(group_orders[1:], fixed_dimensions[1:])
    )
    artin = Fraction(dimension - fixed_dimensions[0]) + swan
    if swan.denominator != 1 or artin.denominator != 1:
        raise StrictDataError("Artin/Swan conductor is not integral")
    return int(swan), int(artin)


def local_permutation_differents(
    orbit_sizes: list[int],
    refinement_codimensions: list[list[int]],
    layer_orders: list[int],
    inertia_order: int,
) -> list[int]:
    if any(len(row) != len(orbit_sizes) for row in refinement_codimensions):
        raise StrictDataError("orbit refinement vector length mismatch")
    values = []
    for orbit_index, orbit_size in enumerate(orbit_sizes):
        different = Fraction(orbit_size - 1)
        for codimensions, order in zip(refinement_codimensions, layer_orders):
            different += Fraction(order, inertia_order) * codimensions[orbit_index]
        if different.denominator != 1:
            raise StrictDataError("per-orbit different exponent is not integral")
        values.append(int(different))
    return values


def solve_filtration_layer_multiplicities(
    base: list[int],
    contributions: dict[str, list[int]],
    observed: list[int],
) -> dict[str, int]:
    if (
        len(base) != len(observed)
        or not contributions
        or any(len(row) != len(observed) for row in contributions.values())
        or any(type(value) is not int for value in base + observed)
    ):
        raise StrictDataError("filtration multiplicity system has inconsistent dimensions")
    names = sorted(contributions)
    upper_bound = max(observed, default=0) + 1
    solutions = []
    for counts in product(range(upper_bound + 1), repeat=len(names)):
        candidate = [
            base[index]
            + sum(
                counts[name_index] * contributions[name][index]
                for name_index, name in enumerate(names)
            )
            for index in range(len(base))
        ]
        if candidate == observed:
            solutions.append(dict(zip(names, counts)))
    if len(solutions) != 1:
        raise StrictDataError(
            f"filtration multiplicity system has {len(solutions)} solutions"
        )
    return solutions[0]


def decimal_guard(value: int) -> dict[str, Any]:
    text = str(value)
    return {
        "decimal_newline_sha256": sha256_bytes((text + "\n").encode("ascii")),
        "digits": len(text.lstrip("-")),
        "positive": value > 0,
    }


def character_and_global_replay(
    arithmetic: dict[str, Any], group: dict[str, Any], pari_report: dict[str, Any]
) -> dict[str, Any]:
    p3 = group["p3_selected"]
    p5 = group["p5_selected"]
    tame = group["tame_C3_selected"]
    reflection = group["reflection"]
    reflection_geometry = reflection_hensel_semantics(arithmetic)
    reflection_profile = next(
        (
            profile
            for profile in group["order2_profiles"]
            if profile["tom_index"] == reflection["tom_index"]
        ),
        None,
    )
    if reflection_profile is None or reflection_profile["tom_index"] != 2:
        raise StrictDataError("reflection geometry did not select ToM 2")
    reflection_picard_lefschetz_bridge = {
        **reflection_geometry,
        "all_order_two_profiles": group["order2_profiles"],
        "filtered_orders": [2, 1],
        "inertia_generator_action": "E6_ROOT_REFLECTION",
        "inertia_tame": reflection_geometry["residue_characteristics_odd"],
        "selected_inertia_tom_index": reflection_profile["tom_index"],
    }

    local_summaries = {
        row.get("prime"): row.get("rows_e_f_d")
        for row in pari_report.get("local_summaries", [])
        if type(row) is dict
    }
    if set(local_summaries) != set(DIRECT_PRIMES):
        raise StrictDataError("PARI local summaries are incomplete")

    def scaled_refinement(
        refinements: list[int], layer_order: int, inertia_order: int
    ) -> list[int]:
        values = [Fraction(layer_order * value, inertia_order) for value in refinements]
        if any(value.denominator != 1 for value in values):
            raise StrictDataError("filtration refinement contribution is nonintegral")
        return [int(value) for value in values]

    p3_observed_differents = [row[2] for row in local_summaries[3]]
    p3_base = [orbit_size - 1 for orbit_size in p3["inertia_orbits_27"]]
    p3_contributions = {
        "deep_C3_layers": scaled_refinement(
            p3["refinement_codimensions_deep"], 3, 18
        ),
        "wild_C3_squared_layers": scaled_refinement(
            p3["refinement_codimensions_wild"], 9, 18
        ),
    }
    p3_solution = solve_filtration_layer_multiplicities(
        p3_base, p3_contributions, p3_observed_differents
    )
    if p3_solution != {"deep_C3_layers": 6, "wild_C3_squared_layers": 1}:
        raise StrictDataError("p=3 filtration multiplicity solution changed")
    p3_orders = (
        [18]
        + [9] * p3_solution["wild_C3_squared_layers"]
        + [3] * p3_solution["deep_C3_layers"]
        + [1]
    )
    p3_fixed_6 = (
        [p3["fixed_dimensions_inertia"]]
        + [p3["fixed_dimensions_wild"]]
        * p3_solution["wild_C3_squared_layers"]
        + [p3["fixed_dimensions_deep"]] * p3_solution["deep_C3_layers"]
        + [[6, 20]]
    )
    p3_swan6, p3_artin6 = artin_from_filtration(
        6, p3_orders, [row[0] for row in p3_fixed_6]
    )
    p3_swan20, p3_artin20 = artin_from_filtration(
        20, p3_orders, [row[1] for row in p3_fixed_6]
    )
    p3_differents = local_permutation_differents(
        p3["inertia_orbits_27"],
        [p3["refinement_codimensions_wild"]]
        * p3_solution["wild_C3_squared_layers"]
        + [p3["refinement_codimensions_deep"]]
        * p3_solution["deep_C3_layers"],
        [9] * p3_solution["wild_C3_squared_layers"]
        + [3] * p3_solution["deep_C3_layers"],
        18,
    )
    if (
        [p3_swan6, p3_swan20] != [5, 18]
        or [p3_artin6, p3_artin20] != [11, 35]
        or p3_differents != p3_observed_differents
    ):
        raise StrictDataError("p=3 character/per-orbit different replay mismatch")

    p5_observed_differents = [row[2] for row in local_summaries[5]]
    p5_base = [orbit_size - 1 for orbit_size in p5["inertia_orbits_27"]]
    p5_contributions = {
        "wild_C5_layers": scaled_refinement(
            p5["refinement_codimensions_wild"], 5, 20
        )
    }
    p5_solution = solve_filtration_layer_multiplicities(
        p5_base, p5_contributions, p5_observed_differents
    )
    if p5_solution != {"wild_C5_layers": 3}:
        raise StrictDataError("p=5 filtration multiplicity solution changed")
    p5_orders = [20] + [5] * p5_solution["wild_C5_layers"] + [1]
    p5_fixed = (
        [p5["fixed_dimensions_inertia"]]
        + [p5["fixed_dimensions_wild"]] * p5_solution["wild_C5_layers"]
        + [[6, 20]]
    )
    p5_swan6, p5_artin6 = artin_from_filtration(6, p5_orders, [row[0] for row in p5_fixed])
    p5_swan20, p5_artin20 = artin_from_filtration(20, p5_orders, [row[1] for row in p5_fixed])
    p5_differents = local_permutation_differents(
        p5["inertia_orbits_27"],
        [p5["refinement_codimensions_wild"]] * p5_solution["wild_C5_layers"],
        [5] * p5_solution["wild_C5_layers"],
        20,
    )
    if (
        [p5_swan6, p5_swan20] != [3, 12]
        or [p5_artin6, p5_artin20] != [7, 29]
        or p5_differents != p5_observed_differents
    ):
        raise StrictDataError("p=5 character/per-orbit different replay mismatch")

    tame_swan6, tame_artin6 = artin_from_filtration(
        6, [3, 1], [tame["fixed_dimensions"][0], 6]
    )
    tame_swan20, tame_artin20 = artin_from_filtration(
        20, [3, 1], [tame["fixed_dimensions"][1], 20]
    )
    reflection_swan6, reflection_artin6 = artin_from_filtration(
        6, [2, 1], [reflection["fixed_dimensions"][0], 6]
    )
    reflection_swan20, reflection_artin20 = artin_from_filtration(
        20, [2, 1], [reflection["fixed_dimensions"][1], 20]
    )
    if (
        [tame_swan6, tame_swan20, tame_artin6, tame_artin20] != [0, 0, 6, 12]
        or [reflection_swan6, reflection_swan20, reflection_artin6, reflection_artin20]
        != [0, 0, 1, 5]
    ):
        raise StrictDataError("tame character conductors mismatch")

    # Serre, Local Fields IV.2 Prop. 9: theta_i(s tau s^-1) is
    # theta_0(s)^i theta_i(tau).  The nontrivial tame C2 has theta_0=-1
    # and the last nonzero graded quotient occurs at odd i=7.
    tame_character = -1
    last_break = 7
    required_multiplier = tame_character**last_break
    if required_multiplier != -1 or p3["central_deep_c3"] is not False:
        raise StrictDataError("Serre tame-character law did not force inversion at p=3")
    if group["p3_rejected_central"]["central_deep_c3"] is not True:
        raise StrictDataError("central p=3 control is not present")

    A = math.prod(C3_PRIMES)
    B = math.prod(REFLECTION_PRIMES)
    conductor6 = 3**p3_artin6 * 5**p5_artin6 * A**tame_artin6 * B**reflection_artin6
    conductor20 = 3**p3_artin20 * 5**p5_artin20 * A**tame_artin20 * B**reflection_artin20
    disc_e = math.prod(prime**exponent for prime, exponent in zip(SUPPORT, FIELD_DISCRIMINANT_EXPONENTS))
    if disc_e != arithmetic["field_discriminant"]["value"] or conductor6 * conductor20 != disc_e:
        raise StrictDataError("conductor-discriminant identity for E failed")
    if decimal_guard(disc_e)["decimal_newline_sha256"] != (
        "7548db5eb3f1c5549d80f6125521e9f3c7f965fb39b7198a8d28f93e8f78d6ca"
    ):
        raise StrictDataError("degree-27 discriminant decimal guard changed")
    if decimal_guard(conductor6)["decimal_newline_sha256"] != (
        "76366bcb4bf436efef17f39bff6820e6166ae8ba68afa50736169421e8a54ee3"
    ):
        raise StrictDataError("V6 conductor decimal guard changed")
    if decimal_guard(conductor20)["decimal_newline_sha256"] != (
        "c8477dde25a371207772ddd53a88df201696bbd2ff172c89f2861374c9d2c13d"
    ):
        raise StrictDataError("V20 conductor decimal guard changed")

    def normal_closure_exponent(group_orders: list[int]) -> int:
        numerator = 51840 * sum(order - 1 for order in group_orders)
        denominator = group_orders[0]
        if numerator % denominator:
            raise StrictDataError("normal-closure discriminant exponent is nonintegral")
        return numerator // denominator

    normal_exponents = {
        "p3": normal_closure_exponent(p3_orders),
        "p5": normal_closure_exponent(p5_orders),
        "tame_C3": normal_closure_exponent([3, 1]),
        "reflection_C2": normal_closure_exponent([2, 1]),
    }
    if normal_exponents != {
        "p3": 106560,
        "p5": 80352,
        "tame_C3": 34560,
        "reflection_C2": 25920,
    }:
        raise StrictDataError("normal-closure discriminant exponents changed")
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
        raise StrictDataError("normal-closure discriminant decimal guard changed")

    complex_conjugation = group["complex_conjugation"]
    complex_mapping = group["complex_conjugation_character_mapping"]
    field_signature = pari_report["field_signature"]
    theta36_real_root_count = pari_report["theta36_real_root_count"]
    line_fixed_count = complex_conjugation["orbits_27"].count(1)
    double_six_fixed_count = complex_conjugation["orbits_36"].count(1)
    if (
        line_fixed_count != field_signature[0]
        or double_six_fixed_count != theta36_real_root_count
    ):
        raise StrictDataError("archimedean fixed-point carriers do not cross-bind")
    v6_fixed, v20_fixed = complex_conjugation["fixed_dimensions"]
    archimedean_expected = {
        "V20_signature": [v20_fixed, 20 - v20_fixed],
        "V6_signature": [v6_fixed, 6 - v6_fixed],
        "complex_conjugation_element_class_index": complex_mapping[
            "element_class_index"
        ],
        "complex_conjugation_subgroup_tom_index": complex_mapping[
            "subgroup_tom_index"
        ],
        "double_six_orbits_36": complex_conjugation["orbits_36"],
        "field_signature": field_signature,
        "line_orbits_27": complex_conjugation["orbits_27"],
    }
    archimedean_authority_chain = {
        "character_table": complex_mapping["character_table_name"],
        "double_six_fixed_count": double_six_fixed_count,
        "element_centralizer_order": complex_mapping["element_centralizer_order"],
        "element_class_order": complex_mapping["element_class_order"],
        "element_class_size": complex_mapping["element_class_size"],
        "field_signature_from_nf": field_signature,
        "line_fixed_count": line_fixed_count,
        "matching_element_class_indices": complex_mapping[
            "element_class_matching_indices"
        ],
        "matching_order2_tom_indices": [complex_conjugation["tom_index"]],
        "selected_element_class_index": complex_mapping["element_class_index"],
        "selected_subgroup_tom_index": complex_mapping["subgroup_tom_index"],
        "theta36_real_root_count_from_polsturm": theta36_real_root_count,
    }
    if not deep_exact(arithmetic["archimedean"], archimedean_expected):
        raise StrictDataError("archimedean carrier/classification mismatch")
    if (
        pari_report["field_discriminant_exponents_on_surface_bad_prime_envelope"]
        != list(FIELD_DISCRIMINANT_EXPONENTS)
        or group.get("line_action_faithful") is not True
    ):
        raise StrictDataError("global field-order exponent vector did not survive character replay")
    ramified_support = [
        prime
        for prime, exponent in zip(SUPPORT, FIELD_DISCRIMINANT_EXPONENTS)
        if exponent
    ]
    if ramified_support != list(SUPPORT[1:]):
        raise StrictDataError("normal-closure ramified support derivation changed")
    return {
        "archimedean": archimedean_expected,
        "archimedean_authority_chain": archimedean_authority_chain,
        "conductors": {
            "V20": {"factorization_exponents": [35, 29, 12, 5], **decimal_guard(conductor20)},
            "V6": {"factorization_exponents": [11, 7, 6, 1], **decimal_guard(conductor6)},
            "A": A,
            "B": B,
        },
        "disc_E": {
            "factorization_exponents_on_surface_bad_prime_envelope": list(
                FIELD_DISCRIMINANT_EXPONENTS
            ),
            "p2_unramified": True,
            "ramified_support": list(SUPPORT[1:]),
            "surface_bad_prime_envelope": list(SUPPORT),
            **decimal_guard(disc_e),
        },
        "disc_K": {
            "factorization_exponents_by_type": normal_exponents,
            "p2_unramified_by_faithful_degree27_action": True,
            **disc_k_guard,
        },
        "local": {
            "p3": {
                "artin_V6_V20": [p3_artin6, p3_artin20],
                "filtered_group_orders": p3_orders,
                "per_orbit_different_exponents": p3_differents,
                "swan_V6_V20": [p3_swan6, p3_swan20],
                "filtration_multiplicity_solution": {
                    "deep_C3_layers": p3_solution["deep_C3_layers"],
                    "unique": True,
                    "wild_C3_squared_layers": p3_solution[
                        "wild_C3_squared_layers"
                    ],
                },
            },
            "p5": {
                "artin_V6_V20": [p5_artin6, p5_artin20],
                "filtered_group_orders": p5_orders,
                "per_orbit_different_exponents": p5_differents,
                "swan_V6_V20": [p5_swan6, p5_swan20],
                "filtration_multiplicity_solution": {
                    "unique": True,
                    "wild_C5_layers": p5_solution["wild_C5_layers"],
                },
            },
            "reflection_C2": {
                "artin_V6_V20": [reflection_artin6, reflection_artin20],
                "swan_V6_V20": [reflection_swan6, reflection_swan20],
            },
            "tame_C3": {
                "artin_V6_V20": [tame_artin6, tame_artin20],
                "swan_V6_V20": [tame_swan6, tame_swan20],
            },
        },
        "reflection_picard_lefschetz_bridge": (
            reflection_picard_lefschetz_bridge
        ),
        "serre_p3": {
            "central_candidate_rejected": True,
            "deep_break": last_break,
            "required_action": "inversion",
            "theta0_on_tame_C2": tame_character,
            "theta0_power_i": required_multiplier,
        },
        "normal_closure_ramified_support": ramified_support,
        "support_exhausted_by_exact_DiscE_and_faithful_action": True,
    }


def normalized_backends(
    pari_python: Path, flint_group_python: Path, gap: Path
) -> dict[str, Any]:
    python = python_preflight(pari_python, flint_group_python)
    gap_value = gap_preflight(gap)
    return {
        "FLINT_SYMPY": {
            "executable_sha256": python["flint_group"]["executable_sha256"],
            "executable_size_bytes": python["flint_group"]["executable_size_bytes"],
            "path_contract": "MINICONDA3_BIN_PYTHON3",
            "versions": python["flint_group"]["versions"],
        },
        "GAP_TOMLIB_SMALLGRP": {
            "ctbllib_version": gap_value["ctbllib_version"],
            "executable_sha256": gap_value["executable_sha256"],
            "executable_size_bytes": gap_value["executable_size_bytes"],
            "gap_version": gap_value["gap_version"],
            "path_contract": "USR_BIN_GAP",
            "smallgrp_version": gap_value["smallgrp_version"],
            "tomlib_version": gap_value["tomlib_version"],
        },
        "PARI": {
            "executable_sha256": python["pari"]["executable_sha256"],
            "executable_size_bytes": python["pari"]["executable_size_bytes"],
            "path_contract": "USR_BIN_PYTHON3",
            "versions": python["pari"]["versions"],
        },
    }


def expected_payload(
    *,
    source_contract: dict[str, Any],
    g0: dict[str, Any],
    artifact_contract: dict[str, Any],
    arithmetic: dict[str, Any],
    backends: dict[str, Any],
    macaulay: dict[str, Any],
    reflections: list[dict[str, Any]],
    pari_report: dict[str, Any],
    pari_report_sha256: str,
    producer_exact_report_sha256: dict[str, str],
    group: dict[str, Any],
    global_report: dict[str, Any],
) -> dict[str, Any]:
    require_sha256(pari_report_sha256, "checker PARI report digest")
    require_exact_keys(
        producer_exact_report_sha256,
        {"arithmetic", "group", "surface_bareiss", "surface_flint"},
        "producer exact-report digest map",
    )
    for name, digest in producer_exact_report_sha256.items():
        require_sha256(digest, f"producer exact report/{name}")
    conductor6 = global_report["conductors"]["V6"]
    conductor20 = global_report["conductors"]["V20"]
    disc_e = global_report["disc_E"]
    disc_k = global_report["disc_K"]
    payload = {
        "C58_source_contract": source_contract,
        "G0_upstream_source_lock": g0,
        "G1_bad_prime_exhaustion": {
            "all_surface_bad_prime_envelope_entries_proven_prime": (
                pari_report["surface_bad_prime_envelope_isprime"] == [True] * 9
            ),
            "divided_discriminant_decimal_newline_sha256": macaulay[
                "divided_discriminant_decimal_newline_sha256"
            ],
            "dual_exact_determinant_engines_agree": True,
            "factorization": macaulay["factorization"],
            "reflection_ODP_primes": list(REFLECTION_PRIMES),
            "reflection_chart0_reduced_point_bases_verified": True,
            "reflection_witnesses_sha256": sha256_bytes(
                canonical_leaf_bytes(reflections)
            ),
            "surface_bad_prime_envelope": list(SUPPORT),
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
            "ramified_support": list(SUPPORT[1:]),
        },
        "G3_dual_action_classification": {
            "decomposition_degrees_alone_leave_two_C3_classes": True,
            "delta36_role": "BOUNDED_NON_RESULT_NONDEPENDENCY",
            "full_labelled_action_arrays_bound": True,
            "p3_all_tom_decomposition_pattern_hits": group[
                "p3_all_tom_decomposition_pattern_hits"
            ],
            "p3_tame_quotient_filter_excludes_206_as_inertia": group[
                "p3_tame_quotient_filter_excludes_206_as_inertia"
            ],
            "p3_valid_decomposition_inertia_pairs": group[
                "p3_valid_decomposition_inertia_pairs"
            ],
            "p5_all_tom_decomposition_pattern_hits": group[
                "p5_all_tom_decomposition_pattern_hits"
            ],
            "p5_valid_decomposition_inertia_pairs": group[
                "p5_valid_decomposition_inertia_pairs"
            ],
            "p5_wild_normalizer_filter_unique": group[
                "p5_wild_normalizer_filter_unique"
            ],
            "tame_C3_selected_tom_index": group["tame_C3_selected"]["tom_index"],
            "tame_theta36_all_precision_factor_multiplybacks": (
                {
                    str(prime): pari_report[
                        "degree36_hensel_product_congruences"
                    ]["theta"][str(prime)]
                    for prime in C3_PRIMES
                }
                == {str(prime): [20, 30, 40] for prime in C3_PRIMES}
            ),
            "tame_theta36_authority_precision": 40,
            "tame_theta36_factor_krasner_bound_satisfied": True,
            "tame_theta36_global_polynomial_discriminant_exponent": 24,
            "tame_theta36_local_discriminant_exponent": 24,
            "tame_theta36_local_rows": [
                [3, 3, 1, 2],
                [6, 3, 2, 2],
                [9, 3, 3, 2],
                [18, 3, 6, 2],
            ],
            "tame_theta36_prime_scope": list(C3_PRIMES),
            "tame_theta36_resolver_separation_bound_satisfied": True,
            "tame_theta36_twice_max_polynomial_discriminant_exponent": 24,
            "tame_theta36_uniquely_selects_fixed_point_free_C3": True,
            "wild_degree36_theta_authority": {
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
            },
        },
        "G4_filtered_inertia": {
            "p3": {
                "deep_C3_exhaustion": group["deep_C3_exhaustion"],
                "deep_C3_normal_in_all_surviving_decomposition_groups": group[
                    "deep_C3_normal_in_all_surviving_decomposition_groups"
                ],
                "decomposition_orders_not_resolved": [18, 36],
                "filtered_orders": global_report["local"]["p3"]["filtered_group_orders"],
                "filtration_multiplicity_solution": global_report["local"]["p3"][
                    "filtration_multiplicity_solution"
                ],
                "inertia_tom_index": group["p3_selected"]["tom_index"],
                "serre_last_nonzero_grade": global_report["serre_p3"]["deep_break"],
                "serre_required_action": global_report["serre_p3"]["required_action"],
            },
            "p5": {
                "filtered_orders": global_report["local"]["p5"]["filtered_group_orders"],
                "filtration_equation": group["p5_filtration_equation"],
                "filtration_multiplicity_solution": global_report["local"]["p5"][
                    "filtration_multiplicity_solution"
                ],
                "inertia_and_decomposition_tom_index": group["p5_selected"]["tom_index"],
            },
            "reflection": {"filtered_orders": [2, 1]},
            "reflection_picard_lefschetz_bridge": global_report[
                "reflection_picard_lefschetz_bridge"
            ],
            "tame_C3": {
                "filtered_orders": [3, 1],
                "inertia_tom_index": group["tame_C3_selected"]["tom_index"],
            },
        },
        "G5_character_conductors": {
            "p3": {
                "artin_V6_V20": global_report["local"]["p3"]["artin_V6_V20"],
                "swan_V6_V20": global_report["local"]["p3"]["swan_V6_V20"],
            },
            "p5": {
                "artin_V6_V20": global_report["local"]["p5"]["artin_V6_V20"],
                "swan_V6_V20": global_report["local"]["p5"]["swan_V6_V20"],
            },
            "reflection_C2": global_report["local"]["reflection_C2"],
            "tame_C3": global_report["local"]["tame_C3"],
        },
        "G6_global_and_infinity": {
            "archimedean": global_report["archimedean"],
            "archimedean_authority_chain": global_report[
                "archimedean_authority_chain"
            ],
            "conductor_discriminant_identity_E": True,
            "conductors": {
                "V6": {
                    "factorization_exponents_3_5_A_B": [11, 7, 6, 1],
                    "decimal_newline_sha256": conductor6[
                        "decimal_newline_sha256"
                    ],
                    "digits": conductor6["digits"],
                    "positive": conductor6["positive"],
                },
                "V20": {
                    "factorization_exponents_3_5_A_B": [35, 29, 12, 5],
                    "decimal_newline_sha256": conductor20[
                        "decimal_newline_sha256"
                    ],
                    "digits": conductor20["digits"],
                    "positive": conductor20["positive"],
                },
            },
            "disc_E": {
                "exponents_on_surface_bad_prime_envelope": list(
                    FIELD_DISCRIMINANT_EXPONENTS
                ),
                "decimal_newline_sha256": disc_e["decimal_newline_sha256"],
                "digits": disc_e["digits"],
                "positive": disc_e["positive"],
            },
            "disc_K": {
                "factorization_exponents_by_type": disc_k[
                    "factorization_exponents_by_type"
                ],
                "decimal_newline_sha256": disc_k["decimal_newline_sha256"],
                "digits": disc_k["digits"],
                "positive": disc_k["positive"],
            },
            "p2_normal_closure_unramified_from_zero_permutation_discriminant_and_faithful_action": True,
            "normal_closure_ramified_support": global_report[
                "normal_closure_ramified_support"
            ],
            "support_exhausted_by_exact_DiscE_and_faithful_action": global_report[
                "support_exhausted_by_exact_DiscE_and_faithful_action"
            ],
        },
        "G7_replay_and_scope": {
            "all_evidence_and_source_snapshots_equal_before_after": True,
            "producer_exact_report_sha256": producer_exact_report_sha256,
            "raw_huge_CHANGE_excluded_from_formal_output": True,
            "runtime_and_absolute_paths_excluded": True,
        },
        "artifact_contract": artifact_contract,
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
            "local_epsilon_factors_claimed": False,
            "local_root_numbers_claimed": False,
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
    if tuple(sorted(payload)) != tuple(sorted(PAYLOAD_KEYS)):
        raise StrictDataError("checker expected payload key set changed")
    return payload


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
    raise StrictDataError("unsupported payload leaf type")


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(item) for item in value)
    if value is None or type(value) in (bool, int, str):
        return 1
    raise StrictDataError("unsupported payload leaf type")


def leaf_paths(value: Any, prefix: tuple[Any, ...] = ()):
    if type(value) is dict:
        for key in sorted(value):
            yield from leaf_paths(value[key], prefix + (key,))
    elif type(value) is list:
        for index, item in enumerate(value):
            yield from leaf_paths(item, prefix + (index,))
    elif value is None or type(value) in (bool, int, str):
        yield prefix
    else:
        raise StrictDataError("unsupported scalar during rebound sweep")


def mutate_leaf(value: Any) -> Any:
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "#"
    if value is None:
        return 0
    raise StrictDataError("unsupported mutation leaf")


def set_path(value: Any, path: tuple[Any, ...], replacement: Any) -> None:
    parent = value
    for component in path[:-1]:
        parent = parent[component]
    parent[path[-1]] = replacement


def schema_descriptor(payload: dict[str, Any]) -> dict[str, Any]:
    return {
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
        "payload_shape_sha256": sha256_bytes(canonical_leaf_bytes(shape_value(payload))),
        "payload_top_level_keys": sorted(payload),
        "schema_id": "hcs-c58-certificate-schema-v1",
        "unknown_fields_rejected_by_full_leaf_rebuild": True,
    }


def core_verify(
    envelope: Any,
    schema: Any,
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> None:
    require_exact_keys(
        envelope,
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
        "C58 certificate envelope",
    )
    require_exact_keys(schema, set(expected_schema), "C58 schema descriptor")
    if (
        envelope["schema_id"] != "hcs-c58-certificate-v1"
        or envelope["schema_descriptor_id"] != "hcs-c58-certificate-schema-v1"
        or envelope["schema_descriptor_id"] != schema["schema_id"]
        or envelope["status"] != "PREFREEZE_CODE_RESULTS_PASS"
        or envelope["paper_status"] != "PAPER_PENDING"
        or any(
            type(envelope[key]) is not str
            for key in (
                "schema_id",
                "schema_descriptor_id",
                "status",
                "paper_status",
                "schema_sha256",
                "canonical_schema_sha256",
                "payload_sha256",
            )
        )
    ):
        raise StrictDataError("C58 envelope identity/status mismatch")
    if (
        envelope["schema_sha256"] != sha256_bytes(canonical_json_bytes(schema, pretty=True))
        or envelope["canonical_schema_sha256"]
        != sha256_bytes(canonical_leaf_bytes(schema))
        or envelope["payload_sha256"]
        != sha256_bytes(canonical_leaf_bytes(envelope["payload"]))
    ):
        raise StrictDataError("C58 schema/payload digest binding mismatch")
    if not deep_exact(envelope["payload"], expected):
        raise StrictDataError("C58 full semantic payload rebuild mismatch")
    if not deep_exact(schema, expected_schema):
        raise StrictDataError("C58 schema descriptor rebuild mismatch")


def expect_core_rejection(
    envelope: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
    label: str,
) -> None:
    try:
        core_verify(envelope, schema, expected, expected_schema)
    except StrictDataError:
        return
    raise StrictDataError(f"actual C58 verifier accepted mutation: {label}")


def actual_verifier_rebound(
    certificate: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> dict[str, int]:
    payload_count = 0
    for path in leaf_paths(expected):
        mutant = deepcopy(certificate)
        original = mutant["payload"]
        for component in path:
            original = original[component]
        set_path(mutant["payload"], path, mutate_leaf(original))
        mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
        expect_core_rejection(mutant, schema, expected, expected_schema, f"payload:{path}")
        payload_count += 1

    schema_count = 0
    for path in leaf_paths(expected_schema):
        mutant_schema = deepcopy(schema)
        original = mutant_schema
        for component in path:
            original = original[component]
        set_path(mutant_schema, path, mutate_leaf(original))
        mutant = deepcopy(certificate)
        mutant["schema_sha256"] = sha256_bytes(
            canonical_json_bytes(mutant_schema, pretty=True)
        )
        mutant["canonical_schema_sha256"] = sha256_bytes(
            canonical_leaf_bytes(mutant_schema)
        )
        expect_core_rejection(
            mutant, mutant_schema, expected, expected_schema, f"schema:{path}"
        )
        schema_count += 1

    envelope_count = 0
    for key in (
        "canonical_schema_sha256",
        "paper_status",
        "payload_sha256",
        "schema_descriptor_id",
        "schema_id",
        "schema_sha256",
        "status",
    ):
        mutant = deepcopy(certificate)
        mutant[key] = mutate_leaf(mutant[key])
        expect_core_rejection(mutant, schema, expected, expected_schema, f"envelope:{key}")
        envelope_count += 1

    structural_mutants: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    extra = deepcopy(certificate)
    extra["unknown"] = False
    structural_mutants.append(("envelope-extra", extra, schema))
    missing = deepcopy(certificate)
    del missing["status"]
    structural_mutants.append(("envelope-missing", missing, schema))
    extra = deepcopy(certificate)
    extra["payload"]["unknown"] = False
    extra["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(extra["payload"]))
    structural_mutants.append(("payload-extra", extra, schema))
    missing = deepcopy(certificate)
    del missing["payload"]["status_contract"]
    missing["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(missing["payload"]))
    structural_mutants.append(("payload-missing", missing, schema))
    extra_schema = deepcopy(schema)
    extra_schema["unknown"] = False
    extra_certificate = deepcopy(certificate)
    extra_certificate["schema_sha256"] = sha256_bytes(
        canonical_json_bytes(extra_schema, pretty=True)
    )
    extra_certificate["canonical_schema_sha256"] = sha256_bytes(
        canonical_leaf_bytes(extra_schema)
    )
    structural_mutants.append(("schema-extra", extra_certificate, extra_schema))
    missing_schema = deepcopy(schema)
    del missing_schema["schema_id"]
    missing_certificate = deepcopy(certificate)
    missing_certificate["schema_sha256"] = sha256_bytes(
        canonical_json_bytes(missing_schema, pretty=True)
    )
    missing_certificate["canonical_schema_sha256"] = sha256_bytes(
        canonical_leaf_bytes(missing_schema)
    )
    structural_mutants.append(("schema-missing", missing_certificate, missing_schema))
    for label, mutant, mutant_schema in structural_mutants:
        expect_core_rejection(mutant, mutant_schema, expected, expected_schema, label)

    hostile_cases = []
    for label, path, replacement in (
        (
            "p3-five-order-three-layers",
            ("G4_filtered_inertia", "p3", "filtered_orders"),
            [18, 9] + [3] * 5 + [1],
        ),
        (
            "p3-seven-order-three-layers",
            ("G4_filtered_inertia", "p3", "filtered_orders"),
            [18, 9] + [3] * 7 + [1],
        ),
        (
            "p3-central-action",
            ("G4_filtered_inertia", "p3", "serre_required_action"),
            "central",
        ),
        (
            "tame-ToM8-substitution",
            ("G3_dual_action_classification", "tame_C3_selected_tom_index"),
            8,
        ),
        (
            "theta-local-row-mutation",
            (
                "G3_dual_action_classification",
                "tame_theta36_local_rows",
                0,
                3,
            ),
            3,
        ),
        (
            "false-unique-D18",
            ("G4_filtered_inertia", "p3", "decomposition_orders_not_resolved"),
            [18],
        ),
        (
            "false-unique-D36",
            ("G4_filtered_inertia", "p3", "decomposition_orders_not_resolved"),
            [36],
        ),
    ):
        mutant = deepcopy(certificate)
        set_path(mutant["payload"], path, replacement)
        mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
        hostile_cases.append((label, mutant))
    for label, mutant in hostile_cases:
        expect_core_rejection(mutant, schema, expected, expected_schema, label)

    type_confusions = 0
    for path, replacement in (
        (("status_contract", "promotion_authorized"), 0),
        (("G2_local_order_exact", "p2_field_discriminant_exponent"), True),
    ):
        mutant = deepcopy(certificate)
        set_path(mutant["payload"], path, replacement)
        mutant["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(mutant["payload"]))
        expect_core_rejection(mutant, schema, expected, expected_schema, f"type:{path}")
        type_confusions += 1
    return {
        "envelope_metadata_scalar_leaves": envelope_count,
        "explicit_bool_int_type_confusions": type_confusions,
        "hostile_semantic_mutations": len(hostile_cases),
        "payload_scalar_leaves": payload_count,
        "rebound_mutations_rejected": (
            payload_count
            + schema_count
            + envelope_count
            + len(structural_mutants)
            + len(hostile_cases)
            + type_confusions
        ),
        "schema_scalar_leaves": schema_count,
        "structural_mutations": len(structural_mutants),
    }


def literal_dict_key_audit() -> int:
    checked = 0
    for name in sorted(CODE_SOURCE_NAMES):
        if not name.endswith(".py"):
            continue
        raw, _ = read_stable(CODE / name, max_bytes=3_000_000)
        try:
            tree = ast.parse(raw.decode("utf-8", errors="strict"), filename=name)
        except (SyntaxError, UnicodeDecodeError) as exc:
            raise StrictDataError(f"C58 source parse failed: {name}") from exc
        for node in ast.walk(tree):
            if type(node) is ast.Dict:
                keys = [
                    key.value
                    for key in node.keys
                    if type(key) is ast.Constant and type(key.value) is str
                ]
                if len(keys) != len(set(keys)):
                    raise StrictDataError(f"duplicate literal dictionary key in {name}")
                checked += 1
    return checked


def strict_parser_cases() -> dict[str, int]:
    rejected = 0
    for raw in (
        b'{"a":1,"a":2}',
        b'{"a":-0}',
        b'{"a":01}',
        b'{"a":1.0}',
        b'{"a":NaN}',
        b"\xef\xbb\xbf{}",
        b'{"a":"\xff"}',
    ):
        try:
            strict_json_loads(raw, max_bytes=100)
        except StrictDataError:
            rejected += 1
        else:
            raise StrictDataError("strict parser accepted an invalid case")
    try:
        strict_json_loads(b'{"a":1}', max_bytes=3)
    except StrictDataError:
        rejected += 1
    else:
        raise StrictDataError("strict parser accepted oversized input")
    huge = b'{"a":' + b"9" * 100_000 + b"}"
    if type(strict_json_loads(huge, max_bytes=len(huge))["a"]) is not int:
        raise StrictDataError("100k-digit canonical integer was not accepted")
    return {
        "canonical_100k_digit_integer_accepted": 1,
        "invalid_cases_rejected": rejected,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--arithmetic-evidence", type=Path, required=True)
    parser.add_argument("--group-evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pari-python", type=Path, default=Path("/usr/bin/python3"))
    parser.add_argument(
        "--flint-group-python",
        type=Path,
        default=Path("/root/miniconda3/bin/python3"),
    )
    parser.add_argument("--gap", type=Path, default=Path("/usr/bin/gap"))
    arguments = parser.parse_args()
    fixed_basenames = {
        arguments.certificate: "c58_certificate.json",
        arguments.schema: "c58_schema.json",
        arguments.arithmetic_evidence: ARTIFACT_NAMES[0],
        arguments.group_evidence: ARTIFACT_NAMES[1],
        arguments.output: "c58_check_report.json",
    }
    if any(path.name != expected for path, expected in fixed_basenames.items()):
        raise StrictDataError("checker certificate/schema/evidence/output basenames are fixed")
    absolute_paths = [path.absolute() for path in fixed_basenames]
    shared_parent = absolute_paths[0].parent
    if (
        any(path.parent != shared_parent for path in absolute_paths)
        or not shared_parent.is_dir()
        or shared_parent.is_symlink()
        or shared_parent.resolve(strict=True) != shared_parent
    ):
        raise StrictDataError(
            "certificate/schema/evidence/output must share one real non-symlink parent"
        )
    protected = [arguments.certificate, arguments.schema]
    protected.extend(arguments.certificate.parent / name for name in ARTIFACT_NAMES)
    protected.extend(CODE.iterdir())
    protected.extend(REPO / relative for relative in UPSTREAM_FILES)
    (output,) = prepare_output_targets((arguments.output,), protected=protected)
    try:
        reject_optimized_python()
        certificate_raw, certificate_fingerprint = read_stable(
            arguments.certificate, max_bytes=5_000_000
        )
        schema_raw, schema_fingerprint = read_stable(arguments.schema, max_bytes=100_000)
        certificate = canonical_pretty(
            certificate_raw, max_bytes=5_000_000, label="C58 certificate"
        )
        schema = canonical_pretty(schema_raw, max_bytes=100_000, label="C58 schema")

        backends = normalized_backends(
            arguments.pari_python, arguments.flint_group_python, arguments.gap
        )
        source_before = rebuild_source_contract()
        g0 = rebuild_g0_upstream_lock()
        artifact_contract, arithmetic, group_evidence = rebuild_artifact_contract(
            arguments.arithmetic_evidence, arguments.group_evidence
        )
        original_coefficients, _, _, resolvers = load_upstream_inputs()
        macaulay = macaulay_replay(arithmetic)
        reflections = reflection_replay(arithmetic)
        pari_report, pari_report_sha256 = pari_replay(
            arithmetic,
            original_coefficients,
            resolvers,
            arguments.pari_python.resolve(strict=True),
            shared_parent,
        )
        group = group_replay(
            group_evidence,
            arguments.gap.resolve(strict=True),
            pari_report,
        )
        global_report = character_and_global_replay(arithmetic, group, pari_report)
        expected = expected_payload(
            source_contract=source_before,
            g0=g0,
            artifact_contract=artifact_contract,
            arithmetic=arithmetic,
            backends=backends,
            macaulay=macaulay,
            reflections=reflections,
            pari_report=pari_report,
            pari_report_sha256=pari_report_sha256,
            producer_exact_report_sha256=PRODUCER_EXACT_REPORT_SHA256,
            group=group,
            global_report=global_report,
        )
        expected_schema = schema_descriptor(expected)
        core_verify(certificate, schema, expected, expected_schema)
        rebound = actual_verifier_rebound(
            certificate, schema, expected, expected_schema
        )
        parser_report = strict_parser_cases()
        literal_nodes = literal_dict_key_audit()

        if not deep_exact(source_before, rebuild_source_contract()):
            raise StrictDataError("C58 code changed during checker replay")
        artifact_after, arithmetic_after, group_after = rebuild_artifact_contract(
            arguments.arithmetic_evidence, arguments.group_evidence
        )
        if (
            not deep_exact(artifact_contract, artifact_after)
            or not deep_exact(arithmetic, arithmetic_after)
            or not deep_exact(group_evidence, group_after)
        ):
            raise StrictDataError("C58 evidence changed during checker replay")
        certificate_raw_after, certificate_after = read_stable(
            arguments.certificate, max_bytes=5_000_000
        )
        schema_raw_after, schema_after = read_stable(arguments.schema, max_bytes=100_000)
        if (
            certificate_raw_after != certificate_raw
            or certificate_after != certificate_fingerprint
            or schema_raw_after != schema_raw
            or schema_after != schema_fingerprint
        ):
            raise StrictDataError("certificate/schema changed during checker replay")

        gate_keys = PAYLOAD_KEYS[1:9]
        report = {
            "certificate_sha256": certificate_fingerprint.sha256,
            "evidence_artifact_count": len(ARTIFACT_NAMES),
            "executed_gates": [f"G{index}" for index in range(8)],
            "full_semantic_leaf_rebuild": True,
            "gate_payload_sha256": {
                f"G{index}": sha256_bytes(canonical_leaf_bytes(expected[key]))
                for index, key in enumerate(gate_keys)
            },
            "independent_checker_does_not_import_or_call_producer_theorem_helpers": True,
            "independent_replay_summary_sha256": sha256_bytes(
                canonical_leaf_bytes(
                    {
                        "global": global_report,
                        "group": group,
                        "macaulay": macaulay,
                        "pari": pari_report,
                        "reflections": reflections,
                    }
                )
            ),
            "literal_dictionary_nodes_duplicate_key_checked": literal_nodes,
            "paper_status": "PAPER_PENDING",
            "payload_scalar_leaf_count": scalar_leaf_count(expected),
            "payload_sha256": certificate["payload_sha256"],
            "release_status": "PAPER_PENDING",
            "result": "PASS_PREFREEZE_CODE_RESULTS",
            "scalar_leaf_rebound": rebound,
            "schema_file_sha256": schema_fingerprint.sha256,
            "schema_id": "hcs-c58-independent-check-v1",
            "strict_parser_cases": parser_report,
            "theorem_gate_count": 8,
        }
        report_raw = canonical_json_bytes(report, pretty=True)
        # Final TOCTOU closure is intentionally adjacent to the only write.
        # Rebind code, all frozen upstream inventories/statuses, both raw
        # evidence carriers, and the certificate/schema bytes after every
        # expensive replay and after report construction.
        if not deep_exact(source_before, rebuild_source_contract()):
            raise StrictDataError("C58 code changed before report write")
        if not deep_exact(g0, rebuild_g0_upstream_lock()):
            raise StrictDataError("frozen C55-C57 authority changed before report write")
        final_artifacts, final_arithmetic, final_group = rebuild_artifact_contract(
            arguments.arithmetic_evidence, arguments.group_evidence
        )
        if (
            not deep_exact(artifact_contract, final_artifacts)
            or not deep_exact(arithmetic, final_arithmetic)
            or not deep_exact(group_evidence, final_group)
        ):
            raise StrictDataError("C58 evidence changed before report write")
        final_certificate_raw, final_certificate = read_stable(
            arguments.certificate, max_bytes=5_000_000
        )
        final_schema_raw, final_schema = read_stable(arguments.schema, max_bytes=100_000)
        if (
            final_certificate_raw != certificate_raw
            or final_certificate != certificate_fingerprint
            or final_schema_raw != schema_raw
            or final_schema != schema_fingerprint
        ):
            raise StrictDataError("certificate/schema changed before report write")
        atomic_write(output, report_raw)
    except BaseException:
        if output.exists() and output.is_file() and not output.is_symlink():
            output.unlink()
        raise
    print("C58 CHECK PASS PREFREEZE")
    print("theorem_gates=8")
    print(f"rebound_mutations={rebound['rebound_mutations_rejected']}")


if __name__ == "__main__":
    main()
