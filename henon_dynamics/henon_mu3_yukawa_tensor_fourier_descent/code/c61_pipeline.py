#!/usr/bin/env python3
"""Backend preflights and deterministic subprocess-report parsing for C61."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Any, Sequence

from c61_exact import (
    StrictDataError,
    canonical_leaf_bytes,
    canonical_json_bytes,
    deep_exact,
    read_stable,
    reject_optimized_python,
    sha256_bytes,
    strict_json_loads,
)


CODE_DIR = Path(__file__).resolve().parent
PROJECT = CODE_DIR.parent
RESULTS = PROJECT / "results"
STAGE_PATTERN = re.compile(r"^\.c61-stage-[A-Za-z0-9]{8}$")

EXPECTED_RELEASE_SOURCE_NAMES = (
    "c61_group.py",
    "c61_checker_group.g",
    "c61_resolvent.py",
    "c61_checker_resolvent.py",
    "c61_producer.py",
    "c61_checker.py",
)
EXPECTED_COMPONENT_SOURCE_NAMES = EXPECTED_RELEASE_SOURCE_NAMES[:4]
EXPECTED_COMPONENT_EVIDENCE_NAMES = (
    "c61_group_evidence.json",
    "c61_resolvent_evidence.json",
)
FROZEN_COMPONENT_SOURCE_HASHES = {
    "c61_group.py": (
        "64dfabdec2cf5767e4022c21a0ad7385efaa191df209c739ab7e015c46a83b5f"
    ),
    "c61_checker_group.g": (
        "4fc377dc16f5b4ebec68767709d1e3e5e2a137b6694567f0b42cb9d88406862e"
    ),
    "c61_resolvent.py": (
        "1c6e18ba4533908ef327cbc574e9d3b8268d1d0f2c9adf6ab2a9d6e86ae40c20"
    ),
    "c61_checker_resolvent.py": (
        "f247dfdf393499c6a41df3dfa34815c1f4557781ec604639da47b921e90c9f6a"
    ),
}
FROZEN_COMPONENT_EVIDENCE_HASHES = {
    "c61_group_evidence.json": (
        "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9"
    ),
    "c61_resolvent_evidence.json": (
        "1be0f9ac4e05ee7a747d39c546502d59dc29bb1407932e14875b61a3b82afe0f"
    ),
}
# Both independent source owners froze these exact bytes after the shared
# fixture and actual producer/checker CLI lifecycle passed.
RELEASE_SOURCE_LATCH_STATUS = "SOURCE_STABLE"
FROZEN_RELEASE_SOURCE_HASHES: dict[str, str] | None = {
    **FROZEN_COMPONENT_SOURCE_HASHES,
    "c61_producer.py": (
        "dadf8899f2fe82b65131a43ffbe438602db79a12654489b34d35ae8a6ee83d99"
    ),
    "c61_checker.py": (
        "571de05ce06cf98c1acb6809800cf5f212755ce91c5d2f8eb5733eb1aa708887"
    ),
}
FROZEN_RUNTIME_REPORT_CONTRACT: dict[str, Any] | None = {
    "stage_file_names": (
        "c61_certificate.json",
        "c61_check_report.json",
        "c61_group_evidence.json",
        "c61_resolvent_evidence.json",
        "c61_schema.json",
    ),
    "source_paths": (
        "code/README.md",
        "code/c61_atomic_promote.py",
        "code/c61_checker.py",
        "code/c61_checker_group.g",
        "code/c61_checker_resolvent.py",
        "code/c61_exact.py",
        "code/c61_group.py",
        "code/c61_hash_manifest.py",
        "code/c61_pipeline.py",
        "code/c61_producer.py",
        "code/c61_resolvent.py",
        "code/run_all.sh",
        "code/test_c61.py",
    ),
    "report_root_keys": (
        "backend_contract",
        "certificate",
        "child_snapshot_rebind_checks",
        "component_validation",
        "evidence",
        "evidence_rebound",
        "executed_gates",
        "full_semantic_leaf_rebuild",
        "g0_released_authority_sha256",
        "gate_payload_sha256",
        "independent_check_report_policy",
        "independent_checker_does_not_import_or_call_producer_theorem_helpers",
        "paper_status",
        "payload_scalar_leaf_count",
        "payload_shape_sha256",
        "promotion_authorized",
        "release_status",
        "result",
        "scalar_leaf_rebound",
        "schema_file",
        "schema_id",
        "source_architecture_audit",
        "source_contract_sha256",
        "source_evidence_authority_stable_before_after_every_child",
        "status",
        "strict_parser_cases",
    ),
    "root_static": {
        "child_snapshot_rebind_checks": 65,
        "executed_gates": ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7"],
        "full_semantic_leaf_rebuild": True,
        "independent_check_report_policy": (
            "REPORT_HAS_NO_SELF_HASH_AND_IS_NOT_A_CERTIFICATE_INPUT"
        ),
        "independent_checker_does_not_import_or_call_producer_theorem_helpers": True,
        "paper_status": "PAPER_BLOCKED_ON_POST_MACHINE_FORMAL_PASS",
        "payload_scalar_leaf_count": 19_078,
        "payload_shape_sha256": (
            "6b771a2b8b0a1b313937654c957bc5b3f9f9cdc8dc496d4ae99987f5b2a0ed52"
        ),
        "promotion_authorized": False,
        "release_status": "NOT_RELEASED",
        "result": "PASS_PREFREEZE_CODE_RESULTS",
        "schema_id": "hcs-c61-independent-check-report-v1",
        "source_evidence_authority_stable_before_after_every_child": True,
        "status": "PREFREEZE_CODE_RESULTS_PASS",
    },
    "backend_contract": {
        "gap": {
            "ctbllib_version": "1.3.1",
            "executable_sha256": (
                "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3"
            ),
            "executable_size_bytes": 1_942,
            "gap_version": "4.11.1",
            "resolved_executable": "/usr/bin/gap",
            "smallgrp_version": "1.4.1",
            "tomlib_version": "1.2.9",
        },
        "math_python": {
            "executable_sha256": (
                "9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
            ),
            "executable_size_bytes": 30_626_264,
            "resolved_executable": "/root/miniconda3/bin/python3.12",
            "versions": {
                "backend": "FLINT_SYMPY_NETWORKX",
                "flint": "0.9.0",
                "jsonschema": "4.25.0",
                "networkx": "3.5",
                "python": [3, 12, 3],
                "sympy": "1.14.0",
            },
        },
        "pari_dependency": False,
        "schema_id": "hcs-c61-backend-contract-v1",
        "singular_dependency": False,
        "two_run_deterministic": True,
    },
    "component_validation": {
        "group": {
            "gap_projection_sha256": (
                "ebd3c174ecc76cb26792dfd24e547a59148f1d13e7a59d4f74a53f8bfb8c860b"
            ),
            "group_source_validator_status": "PASS",
            "two_gap_runs_equal": True,
        },
        "resolver": {
            "candidate_payload_sha256": (
                "5202a2949d0cf3e0777b6ad05708b48a1322a8247a9140b8c85f68964d6f8713"
            ),
            "checker_status": "PASS",
            "evidence_payload_sha256": (
                "956f99f419e08f78d7b8c3304e840a90ca50ac7271635b5e46d9ba5c9c391918"
            ),
            "release_status": "NOT_RELEASED",
            "resolver_component_status": "RESOLVER_COMPONENT_PASS",
            "schema_id": "hcs-c61-resolvent-final-check-v1",
        },
    },
    "evidence": {
        "group_projection_sha256": (
            "ebd3c174ecc76cb26792dfd24e547a59148f1d13e7a59d4f74a53f8bfb8c860b"
        ),
        "group_sha256": (
            "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9"
        ),
        "group_size_bytes": 1_165_113,
        "resolver_payload_sha256": (
            "956f99f419e08f78d7b8c3304e840a90ca50ac7271635b5e46d9ba5c9c391918"
        ),
        "resolver_sha256": (
            "1be0f9ac4e05ee7a747d39c546502d59dc29bb1407932e14875b61a3b82afe0f"
        ),
        "resolver_size_bytes": 594_163,
    },
    "evidence_rebound": {
        "actual_group_verifier_mutation_families": [
            "group_schema_status_firewall",
            "group_source_authority_rebind",
            "group_tensor_row_semantics",
            "group_mixed_160_12_8_atlas",
            "group_raw_global_local_inputs",
            "group_scope_false_leaf",
        ],
        "actual_group_verifier_mutations_rejected": 6,
        "actual_resolver_verifier_mutation_families": [
            "resolver_schema_payload",
            "resolver_marker_fourier_carrier",
            "resolver_type3_Tplus_diamond",
            "resolver_global_local_ideal_law",
        ],
        "actual_resolver_verifier_mutations_rejected": 4,
        "additional_artifact_hostile_families": [
            "group_artifact_contract",
            "resolver_artifact_contract",
        ],
        "additional_artifact_hostile_rebounds_rejected": 2,
        "self_consistent_evidence_rebound_mutations_rejected": 10,
        "total_evidence_and_artifact_rebounds_rejected": 12,
    },
    "scalar_leaf_rebound": {
        "payload_type_mutations_rejected": 19_078,
        "payload_value_mutations_rejected": 19_078,
        "root_type_mutations_rejected": 2,
        "root_value_mutations_rejected": 2,
        "schema_type_mutations_rejected": 29,
        "schema_value_mutations_rejected": 29,
        "structural_mutations_rejected": 14,
        "total_certificate_mutations_rejected": 38_232,
        "type_mutations_rejected": 19_109,
        "value_mutations_rejected": 19_109,
    },
    "schema_file_static": {
        "compact_embedded_schema_sha256": (
            "729b65e2a3b4ab9b3aae3930908aac94e5f9aefeee93b8032d6bf9b50067515e"
        ),
        "descriptor_sha256": (
            "729b65e2a3b4ab9b3aae3930908aac94e5f9aefeee93b8032d6bf9b50067515e"
        ),
        "parsed_deep_equal_embedded_schema": True,
        "path": "results/c61_schema.json",
        "sha256": (
            "a446d693742a327dd0b1edd3ad5da97a50dc76cc0f1f7e171096df341ad10e76"
        ),
        "size_bytes": 1_015,
    },
    "source_architecture_audit": {
        "certificate_producer_opaque_stable_cryptographic_read_only": True,
        "certificate_producer_source_not_decoded_or_parsed": True,
        "checker_exact_local_import_set": True,
        "checker_forbidden_component_or_certificate_producer_imports_absent": True,
        "checker_literal_dictionary_nodes_checked": 77,
        "dynamic_execution_absent": True,
        "promotable_source_tmp_literals_absent": True,
    },
    "strict_parser_cases": {
        "canonical_100k_digit_integer_accepted": 1,
        "invalid_or_noncanonical_cases_rejected": 15,
    },
    "gate_payload_sha256_static": {
        "G0": "41712f83134e5b3843ff14113cdee3928b134496be393d519f9b8167c34a8b54",
        "G1": "4aa676be3c5351e00a366c46d0a5636366bf47b136b6bf3f02db6642e99196ca",
        "G2": "cc4e385d7f7ed3692992a82df92835d6de588c3329154c8e2feed3a251cf6714",
        "G3": "6a846143157b7f54eb051c865e25b71b3a4910442c738c5421740c6846b6f66b",
        "G4": "b81d356297e0d690947eb424821437e9b84ad1071a7d7fa7e74d0dd39bfc93a3",
        "G5": "4188373ff8c1de3fe667800d73c5441361c5cac0dc03892a9b75fddd566c17ea",
        "G6": "eda0932449293e6c586cfbcb8a519e6b4dae30408c452b505a85af750e9898f8",
    },
}

FORMAL_MARKDOWN_NAMES = (
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
P60_RELEASE_AUTHORITY = {
    "commit": "fe1217810b72840619efdf40a2af31b8b80d96f6",
    "tree": "22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a",
    "released_batch_sha256": (
        "d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5"
    ),
    "released_batch_size_bytes": 34_176,
}
C61_TARGET_LOCK_AUTHORITY = {
    "formal_root13_aggregate_sha256": (
        "c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28"
    ),
    "route_sha256": "c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b",
    "batch_sha256": "13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814",
    "exact15_ledger_sha256": (
        "61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5"
    ),
    "exact15_total_bytes": 199_565,
    "exact15_line_count": 5_094,
    "protected_guard_sha256": (
        "24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead"
    ),
}
BATCH_REPOSITORY_RELATIVE = "henon_dynamics/BATCH_PLAN_C57_C61.md"

EXPECTED_BACKENDS = {
    "math": {
        "python": [3, 12, 3],
        "flint": "0.9.0",
        "sympy": "1.14.0",
        "networkx": "3.5",
        "jsonschema": "4.25.0",
        "executable_sha256": "9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101",
        "executable_size_bytes": 30626264,
    },
}
EXPECTED_GAP = {
    "resolved_executable": "/usr/bin/gap",
    "executable_sha256": "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3",
    "executable_size_bytes": 1942,
    "gap_version": "4.11.1",
    "tomlib_version": "1.2.9",
    "smallgrp_version": "1.4.1",
    "ctbllib_version": "1.3.1",
}


def require_frozen_release_sources() -> dict[str, str]:
    """Reject every runner invocation until all six source seals are installed."""

    frozen = FROZEN_RELEASE_SOURCE_HASHES
    if frozen is None:
        raise StrictDataError(
            "C61 component/main source hashes are not frozen; "
            "TARGET_LOCKED implementation cannot replay or refresh"
        )
    if set(frozen) != set(EXPECTED_RELEASE_SOURCE_NAMES):
        raise StrictDataError("C61 frozen source latch has the wrong exact-six keys")
    if any(
        frozen[name] != FROZEN_COMPONENT_SOURCE_HASHES[name]
        for name in EXPECTED_COMPONENT_SOURCE_NAMES
    ):
        raise StrictDataError("C61 release source latch disagrees with component freeze")
    observed: dict[str, str] = {}
    for name in EXPECTED_RELEASE_SOURCE_NAMES:
        path = CODE_DIR / name
        metadata = path.lstat()
        if (
            path.is_symlink()
            or not stat.S_ISREG(metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode) != 0o644
            or metadata.st_nlink != 1
        ):
            raise StrictDataError(
                f"C61 frozen source must be mode-0644 link-count-one: {name}"
            )
        raw, _ = read_stable(path, max_bytes=8_000_000)
        digest = sha256_bytes(raw)
        if digest != frozen[name]:
            raise StrictDataError(f"C61 frozen source hash drift: {name}")
        observed[name] = digest
    return observed


def _locked_regular_bytes(
    path: Path,
    label: str,
    *,
    max_bytes: int,
    expected_mode: int = 0o644,
) -> bytes:
    """Read one mode-bound, link-count-one authority leaf without path drift."""

    metadata = path.lstat()
    if (
        path.is_symlink()
        or not stat.S_ISREG(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != expected_mode
        or metadata.st_nlink != 1
    ):
        raise StrictDataError(
            f"{label} must be one mode-{expected_mode:04o} "
            "link-count-one regular file"
        )
    raw, fingerprint = read_stable(path, max_bytes=max_bytes)
    after = path.lstat()
    before_seal = (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_nlink,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )
    after_seal = (
        after.st_dev,
        after.st_ino,
        after.st_mode,
        after.st_nlink,
        after.st_size,
        after.st_mtime_ns,
        after.st_ctime_ns,
    )
    if before_seal != after_seal or fingerprint.size_bytes != len(raw):
        raise StrictDataError(f"{label} changed while being read")
    return raw


def require_frozen_components() -> dict[str, dict[str, str]]:
    """Bind the independently adjudicated component layer before main freeze."""

    if set(FROZEN_COMPONENT_SOURCE_HASHES) != set(EXPECTED_COMPONENT_SOURCE_NAMES):
        raise StrictDataError("C61 frozen component source latch has wrong keys")
    if set(FROZEN_COMPONENT_EVIDENCE_HASHES) != set(
        EXPECTED_COMPONENT_EVIDENCE_NAMES
    ):
        raise StrictDataError("C61 frozen component evidence latch has wrong keys")
    observed_sources: dict[str, str] = {}
    for name in EXPECTED_COMPONENT_SOURCE_NAMES:
        raw = _locked_regular_bytes(
            CODE_DIR / name,
            f"C61 frozen component source {name}",
            max_bytes=8_000_000,
        )
        digest = sha256_bytes(raw)
        if digest != FROZEN_COMPONENT_SOURCE_HASHES[name]:
            raise StrictDataError(f"C61 frozen component source hash drift: {name}")
        observed_sources[name] = digest
    observed_evidence: dict[str, str] = {}
    for name in EXPECTED_COMPONENT_EVIDENCE_NAMES:
        raw = _locked_regular_bytes(
            RESULTS / name,
            f"C61 frozen component evidence {name}",
            max_bytes=30_000_000,
        )
        digest = sha256_bytes(raw)
        if digest != FROZEN_COMPONENT_EVIDENCE_HASHES[name]:
            raise StrictDataError(f"C61 frozen component evidence hash drift: {name}")
        observed_evidence[name] = digest
    return {"sources": observed_sources, "evidence": observed_evidence}


def _git_stdout(repository: Path, arguments: Sequence[str], label: str) -> bytes:
    completed = subprocess.run(
        ["/usr/bin/git", "-C", str(repository), *arguments],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={"PATH": "/usr/bin:/bin", "LC_ALL": "C"},
        cwd="/",
        check=True,
        timeout=60,
    )
    if completed.stderr or len(completed.stdout) > 1_000_000:
        raise StrictDataError(f"{label} emitted invalid output")
    return completed.stdout


def require_authority_layers(
    *, repository: Path | None = None, project: Path | None = None
) -> dict[str, Any]:
    """Bind immutable released P60 separately from installed C61 target bytes.

    This intentionally does not grant a generic dirty-worktree allowance.
    The exact pre-I61 porcelain state has a separate one-time hostile audit;
    later exact code/results inventories are enforced by their own source and
    manifest gates.
    """

    selected_project = PROJECT if project is None else project.absolute()
    selected_repository = (
        selected_project.parents[1]
        if repository is None
        else repository.absolute()
    )
    dynamics = selected_project.parent
    if (
        selected_project.name != "henon_mu3_yukawa_tensor_fourier_descent"
        or dynamics.name != "henon_dynamics"
        or selected_repository != dynamics.parent
        or selected_project.is_symlink()
        or dynamics.is_symlink()
        or selected_repository.is_symlink()
        or selected_project.resolve(strict=True) != selected_project
        or dynamics.resolve(strict=True) != dynamics
        or selected_repository.resolve(strict=True) != selected_repository
    ):
        raise StrictDataError("C61 authority roots are not canonical real paths")

    head = _git_stdout(
        selected_repository, ["rev-parse", "HEAD"], "P60 HEAD lookup"
    ).decode("ascii", errors="strict").strip()
    tree = _git_stdout(
        selected_repository,
        ["rev-parse", "HEAD^{tree}"],
        "P60 tree lookup",
    ).decode("ascii", errors="strict").strip()
    if head != P60_RELEASE_AUTHORITY["commit"] or tree != P60_RELEASE_AUTHORITY["tree"]:
        raise StrictDataError("immutable released P60 HEAD/tree identity mismatch")
    released_batch = _git_stdout(
        selected_repository,
        [
            "show",
            f"{P60_RELEASE_AUTHORITY['commit']}:{BATCH_REPOSITORY_RELATIVE}",
        ],
        "released P60 Batch blob lookup",
    )
    if (
        sha256_bytes(released_batch)
        != P60_RELEASE_AUTHORITY["released_batch_sha256"]
        or len(released_batch)
        != P60_RELEASE_AUTHORITY["released_batch_size_bytes"]
    ):
        raise StrictDataError("immutable released P60 Batch blob mismatch")

    observed_markdown = {path.name for path in selected_project.glob("*.md")}
    if observed_markdown != set(FORMAL_MARKDOWN_NAMES):
        raise StrictDataError("installed C61 target must have exactly 13 root Markdown files")
    formal_rows: list[bytes] = []
    exact15: list[tuple[str, bytes]] = []
    for name in sorted(FORMAL_MARKDOWN_NAMES):
        raw = _locked_regular_bytes(
            selected_project / name, f"C61 formal target {name}", max_bytes=2_000_000
        )
        digest = sha256_bytes(raw)
        formal_rows.append(f"{digest}  {name}\n".encode("ascii"))
        exact15.append((f"{selected_project.name}/{name}", raw))
    formal_aggregate = sha256_bytes(b"".join(formal_rows))

    route_raw = _locked_regular_bytes(
        selected_project / "route_a_evaluation.yaml",
        "C61 target Route",
        max_bytes=1_000_000,
    )
    batch_path = dynamics / "BATCH_PLAN_C57_C61.md"
    batch_raw = _locked_regular_bytes(
        batch_path, "installed C61 target-lock Batch", max_bytes=1_000_000
    )
    guard_raw = _locked_regular_bytes(
        dynamics / "codex_prompt.md", "protected guard", max_bytes=1_000_000
    )
    exact15.extend(
        (
            ("BATCH_PLAN_C57_C61.md", batch_raw),
            (f"{selected_project.name}/route_a_evaluation.yaml", route_raw),
        )
    )
    exact15.sort(key=lambda item: item[0])
    exact15_ledger = b"".join(
        f"{sha256_bytes(raw)}  {relative}\n".encode("ascii")
        for relative, raw in exact15
    )
    target = C61_TARGET_LOCK_AUTHORITY
    if (
        formal_aggregate != target["formal_root13_aggregate_sha256"]
        or sha256_bytes(route_raw) != target["route_sha256"]
        or sha256_bytes(batch_raw) != target["batch_sha256"]
        or sha256_bytes(exact15_ledger) != target["exact15_ledger_sha256"]
        or sum(len(raw) for _, raw in exact15) != target["exact15_total_bytes"]
        or sum(raw.count(b"\n") for _, raw in exact15)
        != target["exact15_line_count"]
        or sha256_bytes(guard_raw) != target["protected_guard_sha256"]
    ):
        raise StrictDataError("installed C61 target-lock/guard bytes mismatch")
    return {
        "immutable_released_p60": dict(P60_RELEASE_AUTHORITY),
        "installed_c61_target_lock": dict(C61_TARGET_LOCK_AUTHORITY),
    }


def executable(path: Path, label: str) -> Path:
    resolved = path.resolve(strict=True)
    metadata = resolved.stat()
    if not stat.S_ISREG(metadata.st_mode) or not os.access(resolved, os.X_OK):
        raise StrictDataError(f"{label} backend is not an executable regular file")
    return resolved


def clean_environment() -> dict[str, str]:
    # Reject hostile optimization at the orchestration boundary.  Never erase
    # it and continue, since doing that would turn a requested unsafe run into
    # an apparently valid one.
    reject_optimized_python()
    return {
        "PATH": "/usr/bin:/bin",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "TZ": "UTC",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONNOUSERSITE": "1",
    }


def python_preflight(math_python: Path) -> dict[str, Any]:
    math_backend = executable(math_python, "FLINT/SymPy/NetworkX")
    snippets = {
        "math": (
            math_backend,
            "import importlib.metadata,json,sys,flint,sympy,networkx,jsonschema; "
            "assert not sys.flags.optimize; "
            "print(json.dumps({'backend':'FLINT_SYMPY_NETWORKX',"
            "'python':list(sys.version_info[:3]),"
            "'flint':getattr(flint,'__version__','unknown'),"
            "'sympy':sympy.__version__,'networkx':networkx.__version__,"
            "'jsonschema':importlib.metadata.version('jsonschema')},sort_keys=True,separators=(',',':')))",
        ),
    }
    result = {}
    for key, (binary, source) in snippets.items():
        binary_raw, binary_fingerprint = read_stable(binary, max_bytes=40_000_000)
        completed_runs = [
            subprocess.run(
                [str(binary), "-s", "-B", "-c", source],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=clean_environment(),
                cwd="/",
                check=True,
                timeout=60,
            )
            for _ in range(2)
        ]
        if any(completed.stderr for completed in completed_runs):
            raise StrictDataError(f"{key} backend preflight emitted stderr")
        if completed_runs[0].stdout != completed_runs[1].stdout:
            raise StrictDataError(f"{key} backend preflight is nondeterministic")
        completed = completed_runs[0]
        value = strict_json_loads(completed.stdout.strip(), max_bytes=10_000)
        expected_versions = {
            "backend": "FLINT_SYMPY_NETWORKX",
            **{
                name: expected
                for name, expected in EXPECTED_BACKENDS[key].items()
                if not name.startswith("executable_")
            },
        }
        if value != expected_versions:
            raise StrictDataError(f"unsupported {key} backend versions: {value}")
        if (
            sha256_bytes(binary_raw) != EXPECTED_BACKENDS[key]["executable_sha256"]
            or binary_fingerprint.size_bytes
            != EXPECTED_BACKENDS[key]["executable_size_bytes"]
        ):
            raise StrictDataError(f"unsupported {key} Python executable bytes")
        result[key] = {
            "resolved_executable": str(binary),
            "versions": value,
            "executable_sha256": sha256_bytes(binary_raw),
            "executable_size_bytes": binary_fingerprint.size_bytes,
        }
    return result


def gap_preflight(gap_path: Path) -> dict[str, Any]:
    gap = executable(gap_path, "GAP")
    raw, fingerprint = read_stable(gap, max_bytes=1_000_000)
    source = (
        'Print(GAPInfo.Version,"|",PackageInfo("TomLib")[1].Version,"|",'
        'PackageInfo("SmallGrp")[1].Version,"|",'
        'PackageInfo("ctbllib")[1].Version,"\\n"); QUIT;'
    )
    completed_runs = [
        subprocess.run(
            [str(gap), "-q", "-c", source],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=clean_environment(),
            cwd="/",
            check=True,
            timeout=60,
        )
        for _ in range(2)
    ]
    if any(completed.stderr for completed in completed_runs):
        raise StrictDataError("GAP preflight emitted stderr")
    if completed_runs[0].stdout != completed_runs[1].stdout:
        raise StrictDataError("GAP preflight is nondeterministic")
    try:
        fields = completed_runs[0].stdout.decode("ascii", errors="strict").strip().split("|")
    except UnicodeDecodeError as exc:
        raise StrictDataError("GAP preflight output is malformed") from exc
    if len(fields) != 4:
        raise StrictDataError("GAP preflight output has the wrong field count")
    observed = {
        "resolved_executable": str(gap),
        "executable_sha256": sha256_bytes(raw),
        "executable_size_bytes": fingerprint.size_bytes,
        "gap_version": fields[0],
        "tomlib_version": fields[1],
        "smallgrp_version": fields[2],
        "ctbllib_version": fields[3],
    }
    if observed != EXPECTED_GAP:
        raise StrictDataError(f"unsupported GAP backend: {observed}")
    return observed


def run_canonical_report(
    python: Path,
    script: Path,
    arguments: Sequence[str | Path],
    *,
    timeout: int,
    max_stdout_bytes: int = 10_000_000,
) -> tuple[dict[str, Any], str]:
    binary = executable(python, "Python")
    if not script.is_file() or script.is_symlink():
        raise StrictDataError(f"report script must be a regular non-symlink file: {script}")
    completed = subprocess.run(
        [str(binary), "-s", "-B", str(script), *(str(value) for value in arguments)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=clean_environment(),
        check=True,
        timeout=timeout,
    )
    if completed.stderr:
        raise StrictDataError(f"report script emitted stderr: {script.name}")
    if len(completed.stdout) > max_stdout_bytes:
        raise StrictDataError(f"report stdout exceeds limit: {script.name}")
    lines = completed.stdout.splitlines()
    json_lines = [line for line in lines if line.startswith(b"{") and line.endswith(b"}")]
    if len(json_lines) != 1:
        raise StrictDataError(f"report must have exactly one JSON line: {script.name}")
    raw = json_lines[0]
    report = strict_json_loads(raw, max_bytes=max_stdout_bytes)
    if type(report) is not dict:
        raise StrictDataError("canonical report must be an object")
    canonical = json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    if raw != canonical:
        raise StrictDataError(f"report JSON line is not canonical: {script.name}")
    declared = [line.split(b" ", 1)[1].decode() for line in lines if line.startswith(b"report_sha256 ")]
    actual = hashlib.sha256(raw).hexdigest()
    if declared != [actual]:
        raise StrictDataError(f"canonical report digest line mismatch: {script.name}")
    permitted_progress = {
        line
        for line in lines
        if line.startswith(b"division_step ")
    }
    unexplained = [
        line
        for line in lines
        if line not in permitted_progress
        and line != raw
        and not line.startswith(b"report_sha256 ")
    ]
    if unexplained:
        raise StrictDataError(f"unexpected report stdout line: {script.name}")
    return report, actual


def _canonical_pretty_object(path: Path, *, max_bytes: int, label: str) -> dict[str, Any]:
    metadata = path.lstat()
    if (
        path.is_symlink()
        or not stat.S_ISREG(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != 0o644
        or metadata.st_nlink != 1
    ):
        raise StrictDataError(f"{label} must be one mode-0644 link-count-one regular file")
    raw, _ = read_stable(path, max_bytes=max_bytes)
    value = strict_json_loads(raw, max_bytes=max_bytes)
    if type(value) is not dict or raw != canonical_json_bytes(value, pretty=True):
        raise StrictDataError(f"{label} is not one canonical pretty JSON object")
    return value


def verify_runtime_report(stage_dir: Path) -> dict[str, Any]:
    """Rebind the frozen report contract to one exact active-stage snapshot."""

    contract = FROZEN_RUNTIME_REPORT_CONTRACT
    if contract is None:
        raise StrictDataError("C61 runtime-report contract is not frozen")

    def metadata_seal(metadata: os.stat_result) -> tuple[int, ...]:
        return (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_nlink,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )

    def canonical_pretty(raw: bytes, label: str) -> dict[str, Any]:
        value = strict_json_loads(raw, max_bytes=len(raw))
        if type(value) is not dict or raw != canonical_json_bytes(value, pretty=True):
            raise StrictDataError(f"{label} is not one canonical pretty JSON object")
        return value

    def scalar_leaf_count(value: Any) -> int:
        if type(value) is dict:
            return sum(scalar_leaf_count(child) for child in value.values())
        if type(value) is list:
            return sum(scalar_leaf_count(child) for child in value)
        if type(value) in (str, int, bool) or value is None:
            return 1
        raise StrictDataError("C61 runtime document contains a forbidden scalar type")

    if (
        not stage_dir.is_absolute()
        or stage_dir != stage_dir.absolute()
        or stage_dir.parent != RESULTS
        or STAGE_PATTERN.fullmatch(stage_dir.name) is None
        or RESULTS.is_symlink()
        or RESULTS.resolve(strict=True) != RESULTS
        or stage_dir.is_symlink()
        or stage_dir.resolve(strict=True) != stage_dir
    ):
        raise StrictDataError("C61 runtime stage is not one canonical direct results child")
    stage_metadata = stage_dir.lstat()
    if (
        not stat.S_ISDIR(stage_metadata.st_mode)
        or stat.S_IMODE(stage_metadata.st_mode) != 0o700
        or stage_metadata.st_nlink != 2
    ):
        raise StrictDataError("C61 runtime stage must be mode-0700/link-count-two")
    stage_seal = metadata_seal(stage_metadata)
    expected_names = tuple(contract["stage_file_names"])
    observed_names = tuple(sorted(path.name for path in stage_dir.iterdir()))
    if observed_names != expected_names:
        raise StrictDataError("C61 runtime stage has the wrong exact-five inventory")

    limits = {
        "c61_certificate.json": 12_000_000,
        "c61_check_report.json": 2_000_000,
        "c61_group_evidence.json": 30_000_000,
        "c61_resolvent_evidence.json": 30_000_000,
        "c61_schema.json": 200_000,
    }
    stage_raw = {
        name: _locked_regular_bytes(
            stage_dir / name,
            f"C61 runtime {name}",
            max_bytes=limits[name],
        )
        for name in expected_names
    }
    certificate = canonical_pretty(
        stage_raw["c61_certificate.json"], "C61 runtime certificate"
    )
    report = canonical_pretty(
        stage_raw["c61_check_report.json"], "C61 runtime check report"
    )
    sidecar_schema = canonical_pretty(
        stage_raw["c61_schema.json"], "C61 runtime schema"
    )

    if tuple(report) != tuple(contract["report_root_keys"]):
        raise StrictDataError("C61 runtime report has the wrong exact root keys")
    for key, expected in contract["root_static"].items():
        if not deep_exact(report[key], expected):
            raise StrictDataError(f"C61 runtime report static root mismatch: {key}")
    for key in (
        "backend_contract",
        "component_validation",
        "evidence_rebound",
        "scalar_leaf_rebound",
        "source_architecture_audit",
        "strict_parser_cases",
    ):
        if not deep_exact(report[key], contract[key]):
            raise StrictDataError(f"C61 runtime report frozen section mismatch: {key}")

    if tuple(certificate) != ("payload", "payload_sha256", "schema", "schema_sha256"):
        raise StrictDataError("C61 runtime certificate has the wrong exact root keys")
    payload = certificate["payload"]
    embedded_schema = certificate["schema"]
    if type(payload) is not dict or type(embedded_schema) is not dict:
        raise StrictDataError("C61 runtime certificate payload/schema is not an object")
    payload_sha256 = sha256_bytes(canonical_leaf_bytes(payload))
    schema_sha256 = sha256_bytes(canonical_leaf_bytes(embedded_schema))
    if (
        certificate["payload_sha256"] != payload_sha256
        or certificate["schema_sha256"] != schema_sha256
        or not deep_exact(sidecar_schema, embedded_schema)
    ):
        raise StrictDataError("C61 runtime certificate/schema digest contract mismatch")
    certificate_expected = {
        "path": "results/c61_certificate.json",
        "payload_sha256": payload_sha256,
        "sha256": sha256_bytes(stage_raw["c61_certificate.json"]),
        "size_bytes": len(stage_raw["c61_certificate.json"]),
    }
    if not deep_exact(report["certificate"], certificate_expected):
        raise StrictDataError("C61 runtime certificate report seal mismatch")
    schema_expected = {
        "compact_embedded_schema_sha256": schema_sha256,
        "descriptor_sha256": schema_sha256,
        "parsed_deep_equal_embedded_schema": True,
        "path": "results/c61_schema.json",
        "sha256": sha256_bytes(stage_raw["c61_schema.json"]),
        "size_bytes": len(stage_raw["c61_schema.json"]),
    }
    if (
        not deep_exact(report["schema_file"], schema_expected)
        or not deep_exact(schema_expected, contract["schema_file_static"])
        or scalar_leaf_count(embedded_schema) != 29
    ):
        raise StrictDataError("C61 runtime schema report seal mismatch")

    evidence_expected = contract["evidence"]
    if (
        not deep_exact(report["evidence"], evidence_expected)
        or sha256_bytes(stage_raw["c61_group_evidence.json"])
        != evidence_expected["group_sha256"]
        or len(stage_raw["c61_group_evidence.json"])
        != evidence_expected["group_size_bytes"]
        or sha256_bytes(stage_raw["c61_resolvent_evidence.json"])
        != evidence_expected["resolver_sha256"]
        or len(stage_raw["c61_resolvent_evidence.json"])
        != evidence_expected["resolver_size_bytes"]
    ):
        raise StrictDataError("C61 runtime component evidence seal mismatch")

    source_contract = payload.get("source_contract")
    if type(source_contract) is not dict or set(source_contract) != {
        "entries",
        "entry_count",
        "exact_code_inventory",
        "exact_code_path_allowlist",
        "mode_policy",
        "schema_id",
        "self_reference_policy",
    }:
        raise StrictDataError("C61 runtime source contract has the wrong exact shape")
    source_paths = tuple(contract["source_paths"])
    if (
        source_contract["entry_count"] != 13
        or source_contract["exact_code_inventory"] is not True
        or source_contract["exact_code_path_allowlist"] != list(source_paths)
        or source_contract["mode_policy"]
        != "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644"
        or source_contract["schema_id"] != "hcs-c61-source-contract-v1"
        or source_contract["self_reference_policy"]
        != "CERTIFICATE_BINDS_ALL_13_SOURCE_BYTES_CHECK_REPORT_LATER_BINDS_CERTIFICATE"
        or type(source_contract["entries"]) is not list
        or len(source_contract["entries"]) != 13
    ):
        raise StrictDataError("C61 runtime source contract policy mismatch")
    expected_code_names = tuple(path.removeprefix("code/") for path in source_paths)
    code_metadata = CODE_DIR.lstat()
    if (
        CODE_DIR.is_symlink()
        or not stat.S_ISDIR(code_metadata.st_mode)
        or tuple(sorted(path.name for path in CODE_DIR.iterdir()))
        != expected_code_names
    ):
        raise StrictDataError("C61 runtime source directory inventory mismatch")
    code_seal = metadata_seal(code_metadata)
    source_seals: dict[str, tuple[int, ...]] = {}
    for expected_relative, entry in zip(source_paths, source_contract["entries"]):
        if type(entry) is not dict or set(entry) != {
            "mode_octal",
            "path",
            "sha256",
            "size_bytes",
        }:
            raise StrictDataError("C61 runtime source entry has the wrong exact keys")
        expected_mode = 0o755 if expected_relative == "code/run_all.sh" else 0o644
        path = PROJECT / expected_relative
        before = path.lstat()
        source_seals[expected_relative] = metadata_seal(before)
        raw = _locked_regular_bytes(
            path,
            f"C61 runtime source {expected_relative}",
            max_bytes=8_000_000,
            expected_mode=expected_mode,
        )
        expected_entry = {
            "mode_octal": f"{expected_mode:04o}",
            "path": expected_relative,
            "sha256": sha256_bytes(raw),
            "size_bytes": len(raw),
        }
        if not deep_exact(entry, expected_entry):
            raise StrictDataError(f"C61 runtime source entry mismatch: {expected_relative}")
    if (
        metadata_seal(CODE_DIR.lstat()) != code_seal
        or tuple(sorted(path.name for path in CODE_DIR.iterdir()))
        != expected_code_names
        or any(
            metadata_seal((PROJECT / relative).lstat()) != before
            for relative, before in source_seals.items()
        )
    ):
        raise StrictDataError("C61 runtime source inventory changed during rebound")
    source_sha256 = sha256_bytes(canonical_leaf_bytes(source_contract))
    if report["source_contract_sha256"] != source_sha256:
        raise StrictDataError("C61 runtime source-contract digest mismatch")

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
    try:
        gate_hashes = {
            f"G{index}": sha256_bytes(canonical_leaf_bytes(payload[key]))
            for index, key in enumerate(gate_keys)
        }
    except KeyError as error:
        raise StrictDataError("C61 runtime payload lacks a semantic gate") from error
    if (
        not deep_exact(report["gate_payload_sha256"], gate_hashes)
        or any(
            gate_hashes[key] != value
            for key, value in contract["gate_payload_sha256_static"].items()
        )
        or report["g0_released_authority_sha256"] != gate_hashes["G0"]
        or scalar_leaf_count(payload) != report["payload_scalar_leaf_count"]
    ):
        raise StrictDataError("C61 runtime semantic-gate/payload report mismatch")

    scalar = report["scalar_leaf_rebound"]
    evidence_rebound = report["evidence_rebound"]
    if (
        scalar["value_mutations_rejected"]
        != scalar["payload_value_mutations_rejected"]
        + scalar["schema_value_mutations_rejected"]
        + scalar["root_value_mutations_rejected"]
        or scalar["type_mutations_rejected"]
        != scalar["payload_type_mutations_rejected"]
        + scalar["schema_type_mutations_rejected"]
        + scalar["root_type_mutations_rejected"]
        or scalar["total_certificate_mutations_rejected"]
        != scalar["value_mutations_rejected"]
        + scalar["type_mutations_rejected"]
        + scalar["structural_mutations_rejected"]
        or evidence_rebound["self_consistent_evidence_rebound_mutations_rejected"]
        != evidence_rebound["actual_group_verifier_mutations_rejected"]
        + evidence_rebound["actual_resolver_verifier_mutations_rejected"]
        or evidence_rebound["total_evidence_and_artifact_rebounds_rejected"]
        != evidence_rebound["self_consistent_evidence_rebound_mutations_rejected"]
        + evidence_rebound["additional_artifact_hostile_rebounds_rejected"]
    ):
        raise StrictDataError("C61 runtime hostile-counter arithmetic mismatch")

    if (
        metadata_seal(stage_dir.lstat()) != stage_seal
        or tuple(sorted(path.name for path in stage_dir.iterdir())) != expected_names
    ):
        raise StrictDataError("C61 runtime stage changed during report rebound")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--verify-runtime-report", action="store_true")
    parser.add_argument("--stage-dir", type=Path)
    parser.add_argument(
        "--math-python",
        type=Path,
        default=Path("/root/miniconda3/bin/python3"),
    )
    parser.add_argument("--gap", type=Path, default=Path("/usr/bin/gap"))
    arguments = parser.parse_args()
    reject_optimized_python()
    require_authority_layers()
    require_frozen_components()
    require_frozen_release_sources()
    if arguments.verify_runtime_report:
        if arguments.stage_dir is None:
            parser.error("--verify-runtime-report requires --stage-dir")
        verify_runtime_report(arguments.stage_dir)
        print("C61 runtime G7/rebound counters PASS")
        return 0
    if arguments.stage_dir is not None:
        parser.error("--stage-dir is accepted only with --verify-runtime-report")
    value = {
        "python": python_preflight(arguments.math_python),
        "gap": gap_preflight(arguments.gap),
    }
    sys.stdout.buffer.write(canonical_json_bytes(value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
