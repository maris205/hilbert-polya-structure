#!/usr/bin/env python3
"""Build the strict HCS-C57 PREFREEZE certificate from frozen exact inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any

from c57_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deterministic_gzip,
    deep_exact,
    read_stable,
    reject_optimized_python,
    regular_file,
    prepare_output_targets,
    require_canonical_compact_json,
    require_exact_keys,
    safe_relative_path,
    sha256_bytes,
    strict_gzip_json,
    strict_json_loads,
)
from c57_pipeline import (
    clean_environment,
    python_preflight,
    run_canonical_report,
    singular_preflight,
)


REPO = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
CODE = PROJECT / "code"
C56 = REPO / "henon_dynamics/henon_mu3_yukawa_line_field"
C56_CERTIFICATE = C56 / "results/c56_certificate.json"
C56_SCHEMA = C56 / "results/c56_schema.json"
C56_CHECK_REPORT = C56 / "results/c56_check_report.json"

IMPLEMENTATION_COMMIT = "b32402f1dd276a2684d3e849dae26150ebb595e1"
PROVENANCE_COMMIT = "6594400c577c4f59090174dc79b981ffbe8a50ac"
FINAL_REPAIR_COMMIT = "883cb727e57135a0b098a882d9995dd000df2bc0"
C56_CERTIFICATE_SHA256 = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
C56_PAYLOAD_SHA256 = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
C56_SCOPED_MANIFEST_SHA256 = "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a"
C56_CHECK_REPORT_SHA256 = "4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9"

ARTIFACTS = {
    "a12_crt_transcript.json.gz": (
        18_797_009,
        "5171ed975096c1cffed221e7eeec7a87d3afd2970ccd91c431b5283587f7a22f",
        40_146_042,
        "1189d4b015b2024fede11fbc4361575eccbddeed9c3ff6043cd34d16ec311fb2",
        25_000_000,
        50_000_000,
    ),
    "a12_table.json.gz": (
        15_817_606,
        "1034828fcfaad5262ea0388762947e78bf51f3986be642643dfdf5f66711e3f6",
        33_700_083,
        "9dd43ebbdd61873dae3f6437c160a0dfbc389934a62a38057b915955c117c3cc",
        40_000_000,
        40_000_000,
    ),
    "delta_crt.json.gz": (
        97_372,
        "4deead9914f31b0012afd91088339793330874a3b5156ceaeb1371fcb495f685",
        288_384,
        "61ead9febb5ee8295c75980b81ba1c73c2d9cdaebf9e87dd0d0e76da899999a9",
        1_000_000,
        1_000_000,
    ),
    "incidence_char0_witness.json.gz": (
        1_697_390,
        "4853641b143d3d7d0c2086fbee13f9d1f191bac960a989e8e85aede117cf8060",
        4_297_007,
        "2c42ac21f43e54870b030c71facff31b0b0b5a05da544b7455f960e47448a392",
        3_000_000,
        6_000_000,
    ),
    "theta_crt.json.gz": (
        50_282,
        "91181a525e0acb17e73d2e96fd4e7d5d7a25913784ef8ad9d3be59c430a4fadd",
        132_705,
        "5760dd3f4a1e07834f974e340f6cd488d9b793dab8efa0864505903cf9e1bcb3",
        1_000_000,
        1_000_000,
    ),
}

BRIDGE_PRIMES = (
    7,
    37,
    100000000000000000000000000000000000000000000012477,
)

CODE_SOURCE_FILES = (
    "README.md",
    "c57_a12_reconstruction.py",
    "c57_atomic_promote.py",
    "c57_checker.py",
    "c57_exact.py",
    "c57_flint_carrier_identity.py",
    "c57_group.py",
    "c57_hash_manifest.py",
    "c57_incidence_bridge.py",
    "c57_incidence_char0_verify.py",
    "c57_irreducibility.py",
    "c57_modular_resolvent.py",
    "c57_pipeline.py",
    "c57_producer.py",
    "c57_quartic_pivot.py",
    "c57_resolver_replay.py",
    "run_all.sh",
    "test_c57.py",
)


def c57_source_contract() -> dict[str, Any]:
    if len(CODE_SOURCE_FILES) != 18 or len(set(CODE_SOURCE_FILES)) != 18:
        raise StrictDataError("C57 source allowlist must contain 18 distinct names")
    children = list(CODE.iterdir())
    observed = {path.name for path in children}
    if len(observed) != len(children) or observed != set(CODE_SOURCE_FILES):
        raise StrictDataError(
            f"C57 code inventory mismatch; missing={sorted(set(CODE_SOURCE_FILES)-observed)}; "
            f"extra={sorted(observed-set(CODE_SOURCE_FILES))}"
        )
    entries = []
    for name in CODE_SOURCE_FILES:
        path = CODE / name
        raw, fingerprint = read_stable(path, max_bytes=2_000_000)
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": len(raw),
            }
        )
    return {
        "schema_id": "hcs-c57-exact-source-contract-v1",
        "entry_count": len(entries),
        "exact_code_inventory": True,
        "entries": entries,
        "self_reference_policy": "final certificate/schema/check/manifest digests are not embedded; immutable evidence inputs may be source-locked",
        "scoped_manifest_must_rebind_all_code_and_results_artifacts": True,
    }

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


def source_lock(flinterpreter: Path) -> dict[str, Any]:
    expected_files = {
        "henon_dynamics/henon_mu3_yukawa_line_field/code/c56_checker.py": (
            "05eaa9001c9138c4429c1d369d14dade96e9d09c",
            "83923b42662bb1368380271bf83476966dbd6c0522a78d7b0b86cafb1e1bfd63",
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json": (
            "d8c9faa272682bf9403605c59fcef09fcccbe000",
            C56_CERTIFICATE_SHA256,
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_check_report.json": (
            "e902189d1c66e33bdd5283389b1d512c909b67c1",
            C56_CHECK_REPORT_SHA256,
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_schema.json": (
            "01717e84a0efdb204d38ecd881a7827a7af01958",
            "adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504",
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/scoped_hash_manifest.json": (
            "e287006599be564b617ba92bf948b253a695bddd",
            C56_SCOPED_MANIFEST_SHA256,
        ),
    }
    ancestry = []
    for left, right, label in (
        (IMPLEMENTATION_COMMIT, PROVENANCE_COMMIT, "implementation_to_provenance"),
        (PROVENANCE_COMMIT, FINAL_REPAIR_COMMIT, "provenance_to_final_repair"),
        (FINAL_REPAIR_COMMIT, "HEAD", "final_repair_to_current_HEAD"),
    ):
        result = git("merge-base", "--is-ancestor", left, right, check=False)
        if result.returncode != 0 or result.stderr:
            raise StrictDataError(f"C56 ancestry failed: {label}")
        ancestry.append({"relation": label, "verified": True})
    c56_scope = "henon_dynamics/henon_mu3_yukawa_line_field"
    if git("diff", "--quiet", FINAL_REPAIR_COMMIT, "HEAD", "--", c56_scope, check=False).returncode != 0:
        raise StrictDataError("a descendant commit changed the frozen C56 subtree")
    if git("diff", "--quiet", FINAL_REPAIR_COMMIT, "--", c56_scope, check=False).returncode != 0:
        raise StrictDataError("the live/index C56 subtree differs from the final repair")

    committed = []
    for relative, (blob, expected_sha) in sorted(expected_files.items()):
        path = REPO / relative
        raw, fingerprint = read_stable(path, max_bytes=2_000_000)
        if fingerprint.sha256 != expected_sha:
            raise StrictDataError(f"C56 live source-lock mismatch: {relative}")
        for commit in (IMPLEMENTATION_COMMIT, PROVENANCE_COMMIT, FINAL_REPAIR_COMMIT):
            observed = git("ls-tree", commit, "--", relative).stdout.decode().strip().split()
            if len(observed) != 4 or observed[2] != blob or observed[3] != relative:
                raise StrictDataError(f"C56 committed blob mismatch: {commit}:{relative}")
        committed.append(
            {
                "path": relative,
                "git_blob_id": blob,
                "sha256": expected_sha,
                "size_bytes": len(raw),
                "identical_at_all_three_frozen_commits": True,
            }
        )

    manifest_raw, _ = read_stable(
        C56 / "results/scoped_hash_manifest.json", max_bytes=100_000
    )
    manifest = strict_json_loads(manifest_raw, max_bytes=100_000)
    require_exact_keys(
        manifest,
        {
            "entries",
            "entry_count",
            "manifest_self_included",
            "schema",
            "scope",
            "status",
        },
        "C56 scoped manifest",
    )
    if (
        manifest["schema"] != "hcs-c56-scoped-hash-manifest-v1"
        or manifest["status"] != "PREFREEZE_CODE_RESULTS_PASS"
        or manifest["manifest_self_included"] is not False
        or manifest["entry_count"] != 12
        or len(manifest["entries"]) != 12
    ):
        raise StrictDataError("C56 scoped manifest header changed")
    declared_inventory = set()
    for entry in manifest["entries"]:
        require_exact_keys(entry, {"path", "sha256", "size_bytes"}, "C56 manifest entry")
        relative = entry["path"]
        if not safe_relative_path(relative) or relative in declared_inventory:
            raise StrictDataError("unsafe or duplicate C56 scoped path")
        declared_inventory.add(relative)
        raw, fingerprint = read_stable(C56 / relative, max_bytes=2_000_000)
        if fingerprint.sha256 != entry["sha256"] or len(raw) != entry["size_bytes"]:
            raise StrictDataError(f"C56 scoped entry mismatch: {relative}")
    live_inventory = set()
    for root_name in ("code", "results"):
        root = C56 / root_name
        for path in root.rglob("*"):
            if path.is_symlink():
                raise StrictDataError("symlink forbidden in C56 scoped inventory")
            if path.is_dir():
                continue
            if not regular_file(path):
                raise StrictDataError("nonregular entry in C56 scoped inventory")
            live_inventory.add(path.relative_to(C56).as_posix())
    expected_live_inventory = declared_inventory | {"results/scoped_hash_manifest.json"}
    if live_inventory != expected_live_inventory:
        raise StrictDataError(
            f"C56 scoped live inventory mismatch; missing={sorted(expected_live_inventory-live_inventory)}; "
            f"extra={sorted(live_inventory-expected_live_inventory)}"
        )

    certificate_raw, _ = read_stable(C56_CERTIFICATE, max_bytes=2_000_000)
    envelope = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    if (
        envelope.get("payload_sha256") != C56_PAYLOAD_SHA256
        or sha256_bytes(canonical_leaf_bytes(envelope["payload"])) != C56_PAYLOAD_SHA256
    ):
        raise StrictDataError("C56 canonical payload digest mismatch")
    committed_report, committed_report_fingerprint = read_stable(
        C56_CHECK_REPORT, max_bytes=10_000
    )
    if committed_report_fingerprint.sha256 != C56_CHECK_REPORT_SHA256:
        raise StrictDataError("committed C56 checker report bytes changed")
    report = strict_json_loads(committed_report, max_bytes=10_000)
    require_exact_keys(
        report,
        {
            "W_E6_order",
            "certificate_sha256",
            "derived_rational_picard_rank",
            "executed_gates",
            "finite_L_degree_divisibility_gate",
            "four_prime_irreducibility",
            "index_two_kernel_order",
            "line_scheme_degree",
            "payload_sha256",
            "picard_fixed_rank",
            "result",
            "scalar_leaf_rebound",
            "schema",
            "schema_sha256",
            "semantic_gate_count",
            "target_cycle_count_outside_kernel",
            "tmp_hash_used_as_theorem_evidence",
            "written_Hochschild_Serre_rank_bridge_required",
        },
        "C56 committed check report",
    )
    if (
        report["result"] != "PASS_PREFREEZE_CODE_RESULTS"
        or report["semantic_gate_count"] != 10
        or report["scalar_leaf_rebound"].get("rebound_mutations_rejected") != 2684
    ):
        raise StrictDataError("C56 committed checker semantic counts changed")

    # Producer-side G0 is an actual fresh upstream replay, not a static hash
    # recital.  The independent C57 checker deliberately takes a different
    # route: it rebinds the frozen C56 manifest, certificate and committed
    # report without invoking this upstream executable a second time.
    with tempfile.TemporaryDirectory(prefix="c57-c56-replay-") as directory:
        fresh_output = Path(directory) / "c56_check_report.json"
        completed = subprocess.run(
            [
                str(flinterpreter.resolve(strict=True)),
                "-E",
                "-s",
                "-B",
                str(C56 / "code/c56_checker.py"),
                str(C56_CERTIFICATE),
                "--schema",
                str(C56_SCHEMA),
                "--output",
                str(fresh_output),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=clean_environment(),
            check=True,
            timeout=900,
        )
        if completed.stderr:
            raise StrictDataError("fresh C56 checker replay emitted stderr")
        expected_stdout = (
            b"C56 CHECK PASS PREFREEZE\n"
            b"semantic_gates=10\n"
            b"rebound_mutations=2684\n"
        )
        if completed.stdout != expected_stdout:
            raise StrictDataError("fresh C56 checker stdout contract changed")
        fresh_raw, fresh_fingerprint = read_stable(fresh_output, max_bytes=10_000)
        fresh_report = strict_json_loads(fresh_raw, max_bytes=10_000)
        if fresh_fingerprint.sha256 != C56_CHECK_REPORT_SHA256 or not deep_exact(
            fresh_report, report
        ):
            raise StrictDataError("fresh C56 checker replay differs from committed report")
    route_relative = "henon_dynamics/henon_mu3_yukawa_line_field/route_a_evaluation.yaml"
    route_raw, route_fingerprint = read_stable(REPO / route_relative, max_bytes=100_000)
    if route_fingerprint.sha256 != "cc17a14a3565165de2249bc5219f209b6546ffd91b583e75ac07bbba7730ca73":
        raise StrictDataError("C56 final route bytes changed")
    route_blobs = []
    for commit, expected_blob in (
        (IMPLEMENTATION_COMMIT, "993ce55e4b4b29d9c5470cf1c5a4dde90c3959e7"),
        (PROVENANCE_COMMIT, "fe569eb606451efb92bffcede93f3025070ed58d"),
        (FINAL_REPAIR_COMMIT, "cfdbc21b1613ade960570aec7eebd15c2da5ab8a"),
    ):
        observed = git("ls-tree", commit, "--", route_relative).stdout.decode().strip().split()
        if len(observed) != 4 or observed[2] != expected_blob:
            raise StrictDataError("C56 route provenance blob mismatch")
        route_blobs.append({"commit": commit, "git_blob_id": expected_blob})
    route_text = route_raw.decode("utf-8", errors="strict")
    for required_line in (
        "documentation_status: DOCS_FINAL_NO_MORE_EDITS",
        "code_results_status: PREFREEZE_CODE_RESULTS_PASS",
        "release_status: RELEASE_FROZEN",
    ):
        if required_line not in route_text.splitlines():
            raise StrictDataError("C56 final route layered status mismatch")
    archive_route_relative = (
        "henon_dynamics/henon_mu3_yukawa_line_field/evaluations/route_a/"
        "HCS-C56/20260815T000000Z.yaml"
    )
    archive_raw, archive_fingerprint = read_stable(
        REPO / archive_route_relative, max_bytes=100_000
    )
    archive_tree = git("ls-tree", FINAL_REPAIR_COMMIT, "--", archive_route_relative)
    archive_tokens = archive_tree.stdout.decode().strip().split()
    if (
        archive_raw != route_raw
        or archive_fingerprint.sha256 != route_fingerprint.sha256
        or len(archive_tokens) != 4
        or archive_tokens[2] != "cfdbc21b1613ade960570aec7eebd15c2da5ab8a"
    ):
        raise StrictDataError("C56 archived route does not equal the final root route")
    return {
        "implementation_commit": IMPLEMENTATION_COMMIT,
        "provenance_commit": PROVENANCE_COMMIT,
        "final_repair_commit": FINAL_REPAIR_COMMIT,
        "ancestry": ancestry,
        "certificate_sha256": C56_CERTIFICATE_SHA256,
        "payload_sha256": C56_PAYLOAD_SHA256,
        "scoped_manifest_sha256": C56_SCOPED_MANIFEST_SHA256,
        "committed_checker_report_sha256": C56_CHECK_REPORT_SHA256,
        "committed_checker_report_status": report["result"],
        "committed_checker_semantic_gates": report["semantic_gate_count"],
        "committed_checker_rebound_mutations": report["scalar_leaf_rebound"][
            "rebound_mutations_rejected"
        ],
        "committed_files": committed,
        "fresh_committed_checker_replayed_by_producer": True,
        "fresh_committed_checker_report_sha256": fresh_fingerprint.sha256,
        "final_route": {
            "path": route_relative,
            "sha256": route_fingerprint.sha256,
            "size_bytes": len(route_raw),
            "provenance_blob_chain": route_blobs,
            "documentation_status": "DOCS_FINAL_NO_MORE_EDITS",
            "code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "release_status": "RELEASE_FROZEN",
            "archived_copy_path": archive_route_relative,
            "archived_copy_byte_identical": True,
        },
        "current_HEAD_policy": "final repair is an ancestor and every imported C56 machine byte is independently rebound; later C57-only commits are permitted",
        "tracked_C56_subtree_unchanged_since_final_repair": True,
        "C56_code_and_results_exact_live_inventory_rebound": True,
        "C56_line_field_E_not_equal_splitting_field_K": True,
        "C56_line_field_E_non_Galois": True,
        "ordinary_S27_sign_argument_used": False,
    }


def artifacts(artifact_dir: Path) -> dict[str, Any]:
    if artifact_dir.is_symlink() or not artifact_dir.is_dir():
        raise StrictDataError("artifact directory must be a non-symlink directory")
    children = list(artifact_dir.iterdir())
    observed = {path.name for path in children}
    if len(observed) != len(children) or observed != set(ARTIFACTS):
        raise StrictDataError(
            f"artifact inventory mismatch; missing={sorted(set(ARTIFACTS)-observed)}; "
            f"extra={sorted(observed-set(ARTIFACTS))}"
        )
    result = {}
    for name, expected in sorted(ARTIFACTS.items()):
        path = artifact_dir / name
        if path.is_symlink() or not path.is_file():
            raise StrictDataError(f"artifact is not a regular non-symlink file: {name}")
        csize, csha, dsize, dsha, clim, dlim = expected
        value, raw, fingerprint = strict_gzip_json(
            path,
            max_compressed_bytes=clim,
            max_decompressed_bytes=dlim,
        )
        observed_values = (
            fingerprint.size_bytes,
            fingerprint.sha256,
            len(raw),
            sha256_bytes(raw),
        )
        if observed_values != (csize, csha, dsize, dsha):
            raise StrictDataError(f"artifact source-lock mismatch: {name}")
        require_canonical_compact_json(raw)
        compressed_raw, _ = read_stable(path, max_bytes=clim)
        if compressed_raw != deterministic_gzip(raw):
            raise StrictDataError(f"artifact gzip encoding is not deterministic: {name}")
        result[name] = {
            "path": f"results/{name}",
            "compressed_size_bytes": csize,
            "compressed_sha256": csha,
            "decompressed_size_bytes": dsize,
            "decompressed_sha256": dsha,
            "gzip_mtime": 0,
            "semantic_replay_required": True,
        }
    return result


def normalized_backends(pari_python: Path, flint_python: Path, singular: Path):
    python = python_preflight(pari_python, flint_python)
    singular_value = singular_preflight(singular)
    return {
        "PARI": {
            "path_contract": "USR_BIN_PYTHON3",
            "executable_sha256": python["pari"]["executable_sha256"],
            "executable_size_bytes": python["pari"]["executable_size_bytes"],
            "versions": python["pari"]["versions"],
        },
        "FLINT_SYMPY": {
            "path_contract": "MINICONDA3_BIN_PYTHON3",
            "executable_sha256": python["flint_group"]["executable_sha256"],
            "executable_size_bytes": python["flint_group"]["executable_size_bytes"],
            "versions": python["flint_group"]["versions"],
        },
        "SINGULAR": {
            "path_contract": "USR_BIN_SINGULAR",
            **{
                key: value
                for key, value in singular_value.items()
                if key != "resolved_executable"
            },
        },
    }


def _require_report_fields(
    report: dict[str, Any], expected: dict[str, Any], label: str
) -> None:
    if type(report) is not dict:
        raise StrictDataError(f"{label} report is not an object")
    for key, value in expected.items():
        if key not in report or not deep_exact(report[key], value):
            raise StrictDataError(
                f"{label} semantic mismatch at {key}: {report.get(key)!r}"
            )


def producer_exact_reports(
    artifact_dir: Path, pari_python: Path, flint_python: Path
) -> dict[str, Any]:
    """Run the producer's exact G1--G6 algorithms and bind their reports.

    These scripts are deliberately the producer call graph.  The independent
    checker must not import or invoke them; it reconstructs the same facts by
    separate in-checker algorithms.
    """

    def run(
        backend: Path,
        script_name: str,
        arguments: list[str | Path],
        *,
        timeout: int,
        max_stdout_bytes: int = 10_000_000,
    ) -> tuple[dict[str, Any], str]:
        return run_canonical_report(
            backend,
            CODE / script_name,
            arguments,
            timeout=timeout,
            max_stdout_bytes=max_stdout_bytes,
        )

    witness = artifact_dir / "incidence_char0_witness.json.gz"
    theta = artifact_dir / "theta_crt.json.gz"
    delta = artifact_dir / "delta_crt.json.gz"
    candidate = artifact_dir / "a12_table.json.gz"
    a12_transcript = artifact_dir / "a12_crt_transcript.json.gz"

    char0, char0_sha = run(
        flint_python,
        "c57_incidence_char0_verify.py",
        [witness, "--certificate", C56_CERTIFICATE],
        timeout=120,
    )
    _require_report_fields(
        char0,
        {
            "status": "PASS",
            "backend": {"implementation": "python-flint", "version": "0.9.0"},
            "degree_H": 10,
            "degree_Q": 17,
            "H_monic": True,
            "Q_monic": True,
            "H_divides_J": True,
            "g_equals_H_times_Q": True,
            "independent_monic_division_recovers_Q": True,
            "char0_common_factor_degree": 10,
            "char0_gcd_degree_lower_bound": 10,
            "diagonal_evaluation_nonzero": True,
            "diagonal_gcd_degree_zero_over_locked_field": True,
            "gcd_equality_requires_good_prime_rank_specialization_report": True,
            "H_text_sha256": "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f",
            "Q_text_sha256": "ebf57460f2349972e99ecd6a4739a1c0e11521a65201c72a0be6665d91038a47",
        },
        "G1 characteristic-zero incidence",
    )

    bridge_reports: dict[str, dict[str, Any]] = {}
    bridge_hashes: dict[str, str] = {}
    for prime in BRIDGE_PRIMES:
        report, report_sha = run(
            pari_python,
            "c57_incidence_bridge.py",
            [str(prime), "--witness", witness],
            timeout=900,
        )
        _require_report_fields(
            report,
            {
                "prime": prime,
                "prime_proven": True,
                "eliminant_leading_coefficient_nonzero": True,
                "all_shape_denominators_units": True,
                "g_squarefree_27_roots": True,
                "root_count": 27,
                "all_H_coefficient_denominators_units": True,
                "determinant_formula_equals_J": True,
                "meeting_count": 135,
                "line_degrees": [10] * 27,
                "gcd_degrees": [10] * 27,
                "gcd_root_sets_match_graph": True,
                "gcd_diagonal_avoided": True,
                "packaged_H_degree": 10,
                "packaged_H_monic": True,
                "packaged_H_mod_p_equals_monic_gcd_all_27": True,
                "rank_specialization_upper_bound_for_char0_gcd_degree": 10,
                "rank_specialization_direction": "degree_gcd_char0_le_degree_gcd_good_specialization",
                "sixer_count": 72,
                "double_six_count": 36,
                "double_six_delta_distinct_values": 36,
                "all_36_beta_nonzero": True,
                "meeting_graph_sha256": {
                    7: "aaea1ca9c2fa5e0976583f3b8ae13d35b344623e637730ac3f85526ea7f3df38",
                    37: "72939b3118f6cc1d149340363bdbcbded623d3a900ab6c326dd6e72700bfe347",
                    BRIDGE_PRIMES[2]: "bf482b36a1f066939319b072d56d78bd511b1967b94550c8d709374ad1367bb8",
                }[prime],
                "all_three_orbit_products_recomputed_independently": True,
                "orbit_products_bound_to_same_exact_graph_formula": True,
            },
            f"G1 incidence bridge p={prime}",
        )
        expected_oriented_count = 66 if prime == 7 else 72
        if report.get("oriented_sixer_distinct_values") != expected_oriented_count:
            raise StrictDataError(
                f"G1 incidence bridge p={prime} oriented-separator count changed"
            )
        bridge_reports[str(prime)] = report
        bridge_hashes[str(prime)] = report_sha

    group, group_sha = run(
        flint_python, "c57_group.py", [], timeout=600, max_stdout_bytes=2_000_000
    )
    _require_report_fields(
        group,
        {
            "status": "PASS",
            "W_E6_order": 51840,
            "stabilizer_order": 1440,
            "stabilizer_index": 36,
            "double_six_stabilizer_core_order": 1,
            "normalizer_order": 1440,
            "U_fixed_double_six_count": 1,
            "adjacent_S6_order": 720,
            "central_swap_order": 2,
            "central_swap_nontrivial": True,
            "central_swap_not_in_S6": True,
            "central_swap_exchanges_the_two_sixers": True,
            "generated_S6_times_C2_order": 1440,
            "generated_group_equals_enumerated_stabilizer": True,
            "H1_W_Pic_torsion": [],
            "H1_U_Pic_torsion": [2],
            "H1_W_Pic_smith_diagonal": [1, 1, 1, 1, 1, 1],
            "H1_U_Pic_smith_diagonal": [1, 1, 1, 1, 1, 2],
            "W_relation_rank": 36,
            "W_cocycle_kernel_rank": 6,
            "U_relation_rank": 36,
            "U_cocycle_kernel_rank": 6,
            "Pic_S6_invariant_basis": [
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1],
            ],
            "central_swap_on_h_E_columns": [[5, -2], [12, -5]],
            "anti_invariant_d0_in_h_E": [-2, 1],
            "Pic_S6_coboundary_lattice": "2 Z*d0",
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
        },
        "G2 group and Picard cohomology",
    )

    resolver_reports: dict[str, dict[str, Any]] = {}
    resolver_hashes: dict[str, str] = {}
    irreducibility_hashes: dict[str, str] = {}
    expected_resolvers = {
        "theta": (99, 4951, "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea"),
        "delta": (198, 9901, "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb"),
    }
    for kind, transcript in (("theta", theta), ("delta", delta)):
        replay, replay_sha = run(
            pari_python,
            "c57_resolver_replay.py",
            [kind, transcript],
            timeout=1800,
        )
        prime_count, modulus_digits, coefficient_sha = expected_resolvers[kind]
        _require_report_fields(
            replay,
            {
                "status": "PASS",
                "kind": kind,
                "candidate_input_used": False,
                "degree": 36,
                "prime_count": prime_count,
                "all_primes_proven_and_good": True,
                "oriented_sixer_distinct_values_at_separator": 72,
                "all_36_beta_nonzero_at_separator": True,
                "modulus_digits": modulus_digits,
                "modulus_exceeds_twice_uniform_bound": True,
                "coefficients_sha256": coefficient_sha,
            },
            f"G3 {kind} CRT replay",
        )
        irreducibility, irreducibility_sha = run(
            pari_python,
            "c57_irreducibility.py",
            [kind, transcript],
            timeout=600,
            max_stdout_bytes=2_000_000,
        )
        _require_report_fields(
            irreducibility,
            {
                "status": "PASS",
                "kind": kind,
                "resolver_coefficients_sha256": coefficient_sha,
                "proper_degree_intersection": [],
                "irreducible_over_Q": True,
                "separable_over_Q": True,
                "monic_degree_36": True,
                "primitive_Gauss_gate": True,
            },
            f"G3 {kind} irreducibility",
        )
        patterns = [record.get("factor_degrees") for record in irreducibility["records"]]
        if not deep_exact(patterns, [[1, 5, 5, 5, 10, 10], [9, 9, 9, 9]]):
            raise StrictDataError(f"G3 {kind} irreducibility factor patterns changed")
        resolver_reports[kind] = replay
        resolver_hashes[kind] = replay_sha
        irreducibility_hashes[kind] = irreducibility_sha

    reconstruction, reconstruction_sha = run(
        pari_python,
        "c57_a12_reconstruction.py",
        [candidate, a12_transcript],
        timeout=900,
    )
    _require_report_fields(
        reconstruction,
        {
            "status": "PASS",
            "shape": [13, 36],
            "fraction_count": 468,
            "prime_count": 1048,
            "modulus_digits": 100609,
            "carrier_table_sha256": "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1",
            "all_primes_proven": True,
            "prime_product_equals_modulus": True,
            "all_468_congruences_replayed": True,
            "all_468_height_bounds_replayed": True,
            "all_468_denominators_units": True,
            "stability_not_claimed_or_used": True,
        },
        "G5 A12 candidate-blind reconstruction",
    )
    carrier, carrier_sha = run(
        flint_python,
        "c57_flint_carrier_identity.py",
        [
            "--certificate",
            C56_CERTIFICATE,
            "--candidate",
            candidate,
            "--theta-transcript",
            theta,
        ],
        timeout=900,
    )
    _require_report_fields(
        carrier,
        {
            "status": "PASS",
            "carrier_table_sha256": "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1",
            "theta_coefficients_sha256": "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
            "carrier_degree": 12,
            "complement_degree": 15,
            "carrier_monic": True,
            "carrier_subtop_is_minus_theta_over_leading_g": True,
            "remainder_zero_count": 28,
            "forward_multiply_back_count": 28,
            "division_field_multiplication_count": 208,
            "forward_convolution_field_multiplication_count": 208,
            "complement_table_sha256": "b922484d59786a850fc8d13283366e2536c21eae56c5aaae1908b91bc7edbc0f",
        },
        "G5 exact carrier identity",
    )

    pivot, pivot_sha = run(
        pari_python,
        "c57_quartic_pivot.py",
        [
            "7",
            "--certificate",
            C56_CERTIFICATE,
            "--candidate",
            candidate,
            "--theta-transcript",
            theta,
        ],
        timeout=900,
    )
    _require_report_fields(
        pivot,
        {
            "status": "PASS",
            "prime": 7,
            "prime_proven": True,
            "matrix_shape": [60, 31],
            "normalization_monomial": [2, 2, 0, 0],
            "normalization_q0_value": 1,
            "normalization_q0_nonzero": True,
            "gauge_determinant": 31778526453059635681033276764499400992765201,
            "pivot_minor_rank": 30,
            "determinant_theta_coefficients_sha256": "1af5bfdc9b2f945094835fd81281305fb84dfc8208cb542874f2803420cd3a9e",
            "determinant_norm_mod_p": 3,
            "all_36_pivot_determinants_nonzero": True,
            "all_36_times_60_replay_zero": True,
            "all_36_R_theta_at_theta_D_zero": True,
            "theta_orbit_product_equals_R_theta": True,
            "carrier_line_count_per_double_six": 12,
            "all_12_carrier_lines_distinct_per_double_six": True,
            "u0_hyperplane_contains_no_carrier_line": True,
            "canonical_q_solution_sha256": "eb9e803e16f5623647843dd7636fe3d511af60f8f31c453ea6826cd3e4d25573",
        },
        "G6 determinant quartic",
    )

    return {
        "G1": {
            "char0_report_sha256": char0_sha,
            "bridge_report_sha256_by_prime": bridge_hashes,
        },
        "G2": {"group_report_sha256": group_sha},
        "G3": {
            "resolver_replay_report_sha256": resolver_hashes,
            "irreducibility_report_sha256": irreducibility_hashes,
        },
        "G4": {
            "orientation_separator_report_sha256": bridge_hashes["37"],
            "group_action_report_sha256": group_sha,
        },
        "G5": {
            "reconstruction_report_sha256": reconstruction_sha,
            "identity_report_sha256": carrier_sha,
        },
        "G6": {"pivot_report_sha256": pivot_sha},
        "G7": {
            "divisor_input_report_sha256": pivot_sha,
            "report_semantic_scope": [
                "carrier_line_count_per_double_six",
                "all_12_carrier_lines_distinct_per_double_six",
                "u0_hyperplane_contains_no_carrier_line",
                "normalization_q0_value",
                "normalization_q0_nonzero",
                "all_36_times_60_replay_zero",
            ],
            "machine_scope_is_divisor_inputs_not_class_map": True,
        },
    }


def build_payload(
    artifact_dir: Path,
    pari_python: Path,
    flint_python: Path,
    singular: Path,
) -> dict[str, Any]:
    backend_contract = normalized_backends(pari_python, flint_python, singular)
    source_contract = c57_source_contract()
    source = source_lock(flint_python)
    artifact_contract = artifacts(artifact_dir)
    exact_reports = producer_exact_reports(artifact_dir, pari_python, flint_python)
    if not deep_exact(source_contract, c57_source_contract()):
        raise StrictDataError("C57 code changed during exact producer replay")
    if not deep_exact(artifact_contract, artifacts(artifact_dir)):
        raise StrictDataError("C57 evidence changed during exact producer replay")
    return {
        "status_contract": {
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "documentation_status": "PAPER_PENDING",
            "project_release_status": "PAPER_PENDING",
            "promotion_authorized": False,
        },
        "backends": backend_contract,
        "C57_source_contract": source_contract,
        "G0_C56_source_lock": source,
        "artifact_contract": artifact_contract,
        "G1_exact_incidence": {
            "producer_exact_reports": exact_reports["G1"],
            "proof_class": "MACHINE_EXACT_PLUS_RANK_SPECIALIZATION_LEMMA",
            "formula": "J=-Da*Ab*Ac-Db*Dc*Aa",
            "H_text_sha256": "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f",
            "Q_text_sha256": "ebf57460f2349972e99ecd6a4739a1c0e11521a65201c72a0be6665d91038a47",
            "H_degree": 10,
            "Q_degree": 17,
            "H_divides_J_and_g_char0": True,
            "g_equals_H_times_Q_char0": True,
            "diagonal_gcd_degree": 0,
            "good_specialization_primes": list(BRIDGE_PRIMES),
            "all_good_specialization_primes_proven": True,
            "all_eliminant_leading_coefficients_nonzero": True,
            "all_shape_and_H_denominators_units": True,
            "all_specialized_eliminants_squarefree_with_27_roots": True,
            "determinant_formula_equals_divided_J_at_all_good_primes": True,
            "all_27_H_specializations_equal_monic_modular_gcd": True,
            "lower_bound_degree": 10,
            "upper_bound_degree": 10,
            "specialization_direction": "degree_gcd_char0_le_degree_gcd_good_specialization",
            "neighbours_per_line": 10,
            "unordered_edge_count": 135,
            "sixer_count": 72,
            "double_six_count": 36,
            "bridge_graph_sha256": {
                "7": "aaea1ca9c2fa5e0976583f3b8ae13d35b344623e637730ac3f85526ea7f3df38",
                "37": "72939b3118f6cc1d149340363bdbcbded623d3a900ab6c326dd6e72700bfe347",
                "100000000000000000000000000000000000000000000012477": "bf482b36a1f066939319b072d56d78bd511b1967b94550c8d709374ad1367bb8",
            },
            "numeric_residual_sorting_used": False,
        },
        "G2_group_and_H1": {
            "producer_exact_reports": exact_reports["G2"],
            "W_E6_order": 51840,
            "double_six_stabilizer_order": 1440,
            "double_six_stabilizer_index": 36,
            "double_six_stabilizer_core_order": 1,
            "double_six_stabilizer_normalizer_order": 1440,
            "U_fixed_double_six_count": 1,
            "stabilizer_structure": "S6 x C2",
            "oriented_stabilizer_order": 720,
            "central_swap_order": 2,
            "central_swap_nontrivial_and_not_in_S6": True,
            "central_swap_exchanges_sixers": True,
            "line_orbit_sizes": [12, 15],
            "H1_W_Pic_torsion": [],
            "H1_U_Pic_torsion": [2],
            "H1_W_Pic_smith_diagonal": [1, 1, 1, 1, 1, 1],
            "H1_U_Pic_smith_diagonal": [1, 1, 1, 1, 1, 2],
            "W_relation_rank": 36,
            "W_cocycle_kernel_rank": 6,
            "U_relation_rank": 36,
            "U_cocycle_kernel_rank": 6,
            "Pic_S6_invariant_basis": [[1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1]],
            "central_swap_on_h_E_columns": [[5, -2], [12, -5]],
            "anti_invariant_d0_in_h_E": [-2, 1],
            "Pic_S6_coboundary_lattice": "2 Z*d0",
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
            "global_minimality_proof_class": "LITERATURE_CLASSIFICATION_BRIDGE",
            "locator_required": True,
            "two_primary_case_split": {
                "Z_over_2": "H is contained in a conjugate of U1; index 36",
                "Z_over_2_squared": "H is contained in a conjugate of U3; index 720=36*20",
                "common_consequence": "36 divides [K intersect L:Q], and [K intersect L:Q] divides [L:Q] for every finite L/Q with nonzero 2-primary quotient",
                "degree_36_equality_consequence": "the subgroup is conjugate to U1",
                "degree_36_equality_field_consequence": "L=K intersect L=K^U1 (up to conjugate embedding)",
            },
            "machine_does_not_classify_all_two_primary_subgroups": True,
        },
        "G3_resolvers_and_fixed_field": {
            "producer_exact_reports": exact_reports["G3"],
            "theta_CRT_prime_count": 99,
            "theta_CRT_modulus_digits": 4951,
            "theta_coefficients_sha256": "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
            "delta_CRT_prime_count": 198,
            "delta_CRT_modulus_digits": 9901,
            "delta_required_height_digits": 9858,
            "delta_coefficients_sha256": "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb",
            "candidate_input_used": False,
            "all_CRT_primes_proven_and_orbit_products_replayed": True,
            "two_reduction_factor_patterns": [[1, 5, 5, 5, 10, 10], [9, 9, 9, 9]],
            "proper_factor_degree_intersection": [],
            "theta_and_delta_irreducible_degree": 36,
            "delta_is_primary_fixed_field_and_radicand_authority": True,
            "theta_is_auxiliary_primitive_for_G5": True,
            "same_D_fixed_field_bridge": "WRITTEN_STABILIZER_AND_SEPARATING_ORBIT_BRIDGE",
            "delta_equals_polynomial_in_theta_required": False,
            "ordinary_S27_sign_argument_used": False,
        },
        "G4_orientation_quadratic": {
            "producer_exact_reports": exact_reports["G4"],
            "beta_definition": "sum_A(alpha)-sum_B(alpha)",
            "delta_definition": "beta^2",
            "oriented_stabilizer_order": 720,
            "central_swap_beta_sign": -1,
            "oriented_sixer_separator_is_proven_good_prime": True,
            "oriented_sixer_separator_prime": 37,
            "oriented_sixer_distinct_values": 72,
            "double_six_delta_distinct_values": 36,
            "all_36_beta_nonzero": True,
            "quadratic_extension_bridge": "WRITTEN_STABILIZER_BRIDGE_K_S6_EQUALS_F_D_SQRT_DELTA",
        },
        "G5_degree_12_carrier": {
            "producer_exact_reports": exact_reports["G5"],
            "carrier_table_shape": [13, 36],
            "carrier_table_sha256": "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1",
            "original_candidate_source_sha256": "810ca69f08dae07b2978f6cc9d441638e6c79a8bcfd6a771c4a895f6b0d1b17d",
            "candidate_blind_CRT_prime_count": 1048,
            "candidate_blind_CRT_modulus_digits": 100609,
            "all_468_congruences_bounds_and_units_replayed": True,
            "stability_heuristic_used": False,
            "A_degree": 12,
            "B_degree": 15,
            "A_monic_and_subtop_minus_theta_over_leading_g": True,
            "division_field_multiplication_count": 208,
            "forward_convolution_field_multiplication_count": 208,
            "all_28_remainders_zero_and_forward_coefficients_equal": True,
            "complement_table_sha256": "b922484d59786a850fc8d13283366e2536c21eae56c5aaae1908b91bc7edbc0f",
            "authority": "EXACT_A12_TIMES_B15_EQUALS_G_IN_Q_THETA",
        },
        "G6_determinant_quartic_and_rank": {
            "producer_exact_reports": exact_reports["G6"],
            "matrix_shape": [60, 31],
            "normalization_monomial": [2, 2, 0, 0],
            "normalization_q0_value": 1,
            "normalization_q0_nonzero": True,
            "gauge_block_from_C56_cubic": [[75081586157, 0, 0, 0], [-28576620789, 75081586157, 0, 0], [-122000922135, 0, 75081586157, 0], [-5364921951, 0, 0, 75081586157]],
            "gauge_determinant": 31778526453059635681033276764499400992765201,
            "pivot_rows_zero_based": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 36, 37, 38, 48],
            "pivot_determinant_theta_coefficients_sha256": "1af5bfdc9b2f945094835fd81281305fb84dfc8208cb542874f2803420cd3a9e",
            "pivot_determinant_norm_mod_7": 3,
            "canonical_q_solution_sha256": "eb9e803e16f5623647843dd7636fe3d511af60f8f31c453ea6826cd3e4d25573",
            "all_36_theta_values_distinct_and_orbit_product_equal": True,
            "all_36_times_60_restriction_equations_zero": True,
            "rank_at_least_30_machine": True,
            "rank_at_most_30_and_kernel_existence_proof_class": "WRITTEN_HILBERT90_O4_GEOMETRIC_BRIDGE",
            "determinant_defined_Q_authority": True,
            "expanded_Q_required": False,
        },
        "G7_divisor_and_quaternion": {
            "producer_exact_reports": exact_reports["G7"],
            "carrier_line_count": 12,
            "all_12_carrier_lines_distinct": True,
            "normalization_q0_crossref_G6_value": 1,
            "Q_nonzero_mod_F_times_linear": True,
            "u0_hyperplane_contains_no_carrier_line": True,
            "quartic_divisor_H_degree": 12,
            "carrier_union_H_degree": 12,
            "multiplicity_at_least_one_on_each_carrier_line": True,
            "degree_exhaustion_no_residual_or_extra_multiplicity": True,
            "divisor_Q": "E+G",
            "oriented_divisor_D": "E-2H0",
            "divisor_f_for_f_equals_Q_over_u0_fourth": "E+G-4H0",
            "norm_D_equals_divisor_f": True,
            "norm_divisor_bridge_proof_class": "WRITTEN_EXACT_RESTRICTION_AND_DEGREE_EXHAUSTION",
            "cyclic_algebra": "(F_D_prime/F_D,Q/u0^4)",
            "quaternion": "(delta,Q/u0^4)",
            "cyclic_and_quaternion_presentations_identified": True,
            "unramifiedness_proof_class": "WRITTEN_CYCLIC_NORM_DIVISOR_CRITERION",
            "unramified": True,
            "unramifiedness_does_not_imply_nonzero": True,
            "Pic_S6_coordinates": {
                "basis": ["h", "eSigma"],
                "hyperplane_H0": [3, -1],
                "anti_invariant_d0": [-2, 1],
                "oriented_divisor_D": [-6, 3],
            },
            "central_swap_d0_sign": -1,
            "kernel_one_plus_central_swap_on_Pic_S6": "Z*d0",
            "central_swap_minus_one_image_on_Pic_S6": "2 Z*d0",
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
            "Hochschild_Serre_Brbar_and_H3_hypotheses_required": True,
            "cyclic_class_nonzero_proof_class": "WRITTEN_CLASS_MAP_BRIDGE_REQUIRED",
            "machine_does_not_claim_Hochschild_Serre_class_map": True,
            "written_conclusion_Br_quotient": "Z/2 generated by (delta,Q/u0^4)",
        },
        "nonresults_firewall": {
            "pari_direct_incidence_factor_lane": {
                "status": "TIMEOUT_NON_RESULT",
                "certificate_dependency": False,
                "noninput": True,
            },
            "expanded_quartic_lane": {
                "status": "BOUNDED_NON_RESULT",
                "certificate_dependency": False,
                "noninput": True,
            },
            "delta_as_polynomial_in_theta_lane": {
                "status": "BOUNDED_NON_RESULT",
                "certificate_dependency": False,
                "noninput": True,
            },
        },
        "scope_firewall": {
            "general_degree_36_resolvent_novelty_claimed": False,
            "delta_equals_polynomial_in_theta_claimed": False,
            "expanded_quartic_coefficients_claimed": False,
            "local_quaternion_evaluation_claimed": False,
            "rational_points_claimed": False,
            "absence_of_rational_points_claimed": False,
            "Hasse_failure_claimed": False,
            "weak_approximation_claimed": False,
            "Brauer_Manin_obstruction_claimed": False,
            "full_local_inertia_claimed": False,
            "Artin_conductors_claimed": False,
            "bad_Euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "stable_rationality_novelty_claimed": False,
            "stable_irrationality_claimed": False,
            "surface_rationality_claimed": False,
            "arbitrary_cubic_surfaces_theorem_claimed": False,
            "later_batch_theorem_claimed": False,
            "all_Yukawa_or_Henon_surfaces_theorem_claimed": False,
            "motives_claimed": False,
            "VHS_realization_claimed": False,
            "Calabi_Yau_realization_claimed": False,
            "automorphy_claimed": False,
            "dynamics_claimed": False,
            "Riemann_Hypothesis_claimed": False,
            "Hilbert_Polya_operator_claimed": False,
            "local_Picard_Artin_package_claimed": False,
            "temporary_digest_accepted_as_release_provenance": False,
            "paper_complete_claimed": False,
            "release_claimed": False,
        },
        "documentation_contract": {
            "status": "PAPER_PENDING",
            "root_document_bytes_are_machine_certificate_inputs": False,
            "paper_bytes_are_machine_certificate_inputs": False,
            "later_document_and_paper_freeze_requires_external_full_project_manifest": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-output", type=Path, required=True)
    parser.add_argument("--pari-python", type=Path, default=Path("/usr/bin/python3"))
    parser.add_argument(
        "--flint-group-python", type=Path, default=Path("/root/miniconda3/bin/python3")
    )
    parser.add_argument("--singular", type=Path, default=Path("/usr/bin/Singular"))
    arguments = parser.parse_args()
    if arguments.output.name != "c57_certificate.json" or arguments.schema_output.name != "c57_schema.json":
        raise StrictDataError("producer output basenames are fixed")
    protected = [arguments.artifact_dir / name for name in ARTIFACTS]
    protected.extend(path for path in CODE.iterdir() if path.is_file())
    protected.extend(
        (
            C56_CERTIFICATE,
            C56_SCHEMA,
            C56_CHECK_REPORT,
            C56 / "results/scoped_hash_manifest.json",
            C56 / "route_a_evaluation.yaml",
            C56 / "evaluations/route_a/HCS-C56/20260815T000000Z.yaml",
        )
    )
    outputs = prepare_output_targets(
        (arguments.output, arguments.schema_output), protected=protected
    )
    try:
        reject_optimized_python()
        sys.set_int_max_str_digits(0)
        payload = build_payload(
            arguments.artifact_dir,
            arguments.pari_python,
            arguments.flint_group_python,
            arguments.singular,
        )
        shape = shape_value(payload)
        schema = {
            "schema_id": "hcs-c57-certificate-schema-v1",
            "max_certificate_bytes": 2_000_000,
            "payload_top_level_keys": sorted(payload),
            "payload_shape_sha256": sha256_bytes(canonical_leaf_bytes(shape)),
            "payload_scalar_leaf_count": scalar_leaf_count(payload),
            "unknown_fields_rejected_by_full_leaf_rebuild": True,
            "duplicate_keys_rejected": True,
            "floats_rejected": True,
            "booleans_rejected_in_integer_slots": True,
            "noncanonical_integers_rejected": True,
            "non_UTF8_rejected": True,
            "oversized_input_rejected": True,
            "optimized_python_rejected": True,
            "gzip_mtime_zero_and_deterministic_recompression_required": True,
        }
        schema_raw = canonical_json_bytes(schema, pretty=True)
        envelope = {
            "schema_id": "hcs-c57-certificate-v1",
            "schema_descriptor_id": "hcs-c57-certificate-schema-v1",
            "schema_sha256": sha256_bytes(schema_raw),
            "canonical_schema_sha256": sha256_bytes(canonical_leaf_bytes(schema)),
            "status": "PREFREEZE_CODE_RESULTS_PASS",
            "paper_status": "PAPER_PENDING",
            "payload_sha256": sha256_bytes(canonical_leaf_bytes(payload)),
            "payload": payload,
        }
        raw = canonical_json_bytes(envelope, pretty=True)
        if len(raw) > 2_000_000 or len(schema_raw) > 100_000:
            raise StrictDataError("generated certificate or schema exceeds its byte ceiling")
        atomic_write(outputs[1], schema_raw)
        # The certificate is the commit marker and is therefore published last.
        atomic_write(outputs[0], raw)
    except BaseException:
        for output in outputs:
            if output.exists() and output.is_file() and not output.is_symlink():
                output.unlink()
        raise
    print("HCS-C57 PRODUCER PASS PREFREEZE")
    print(f"certificate_sha256={hashlib.sha256(raw).hexdigest()}")
    print(f"payload_sha256={envelope['payload_sha256']}")


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


if __name__ == "__main__":
    main()
