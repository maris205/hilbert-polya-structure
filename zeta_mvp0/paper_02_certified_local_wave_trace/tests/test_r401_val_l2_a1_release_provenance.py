from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/build_r401_val_l2_a1_release_provenance.py"
SPEC = importlib.util.spec_from_file_location("r401_val_l2_a1_release", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def dump_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(MODULE.canonical_json_bytes(payload))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha(path: Path) -> str:
    return MODULE.sha256_bytes(path.read_bytes())


def make_release_fixture(tmp_path: Path) -> Path:
    project = tmp_path / "paper"
    project.mkdir()
    result = project.joinpath(*MODULE.RESULT_RELATIVE.parts)
    result.mkdir(parents=True)

    protocol = project / MODULE.FORMAL_PROTOCOL
    write(protocol, "# Protocol\n\nProtocol ID: `R401-VAL-L2-A1`\n")
    review = project / MODULE.PREFREEZE_REVIEW
    write(review, "# Independent review\n\nVerdict: ACCEPT_FOR_FREEZE\n")
    s0 = project / MODULE.S0_REPLAY

    # Copy the exact executing implementation so the runtime/freeze source
    # identity check is exercised in every happy-path test.
    release_builder = project / MODULE.RELEASE_BUILDER
    release_builder.parent.mkdir(parents=True, exist_ok=True)
    release_builder.write_bytes(SCRIPT.read_bytes())
    contract = project / MODULE.RELEASE_CONTRACT_DOC
    contract.parent.mkdir(parents=True, exist_ok=True)
    contract.write_bytes((ROOT / MODULE.RELEASE_CONTRACT_DOC).read_bytes())
    for relative in (
        MODULE.PRODUCER,
        MODULE.CHECKER,
        MODULE.S0_ADAPTER,
        MODULE.EVALUATOR_SOURCE,
    ):
        write(project / relative, f"synthetic bytes for {relative}\n")
    for relative in MODULE.REQUIRED_MAIN_FREEZE_HASHES:
        target = project / relative
        if not target.exists():
            if target.suffix == ".json":
                dump_json(target, {"synthetic_frozen_input": relative})
            else:
                write(target, f"synthetic frozen input for {relative}\n")
    for relative in MODULE.S0_REPLAY_HASH_FILES.values():
        target = project / relative
        if not target.exists():
            dump_json(target, {"synthetic_s0_evidence": relative})
    dump_json(s0, MODULE.expected_s0_replay_payload(project))

    binary = project / "validated/bin/capd_r401_local_complement_mp_a1"
    binary.parent.mkdir(parents=True, exist_ok=True)
    binary.write_bytes(b"synthetic evaluator binary\n")
    evaluator = {
        "source_file": MODULE.EVALUATOR_SOURCE,
        "source_sha256": sha(project / MODULE.EVALUATOR_SOURCE),
        "binary_file": str(binary),
        "binary_sha256": sha(binary),
        "capd_commit": MODULE.EXPECTED_CAPD_COMMIT,
        "capd_flags": ["-frounding-math", "-D__HAVE_MPFR__", "-lmpfr", "-lgmp"],
        "status_returncode_whitelist": MODULE.EXPECTED_STATUS_RETURNCODE_WHITELIST,
    }
    machine = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "status": "FROZEN_FOR_PRODUCTION",
        "scientific_licensing_enabled": True,
        "machine_requirements": dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
        "evaluator": evaluator,
    }
    dump_json(project / MODULE.MACHINE_FREEZE, machine)

    input_hashes = {
        relative: sha(project / relative)
        for relative in MODULE.REQUIRED_MAIN_FREEZE_HASHES
    }
    scheduler = dict(MODULE.EXPECTED_SCHEDULER)
    thresholds = dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS)
    main_freeze = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "status": "FROZEN_FOR_PRODUCTION",
        "scientific_licensing_enabled": True,
        "checker_mode": MODULE.CHECKER_MODE,
        "matrix": MODULE.expected_matrix(),
        "input_hashes": input_hashes,
        "checker_source_sha256": input_hashes[MODULE.CHECKER],
        "evaluator": evaluator,
        "machine_requirements": dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
        "per_tree_limits": dict(MODULE.EXPECTED_PER_TREE_LIMITS),
        "scheduler": scheduler,
        "logical_thresholds": thresholds,
    }
    dump_json(project / MODULE.MAIN_FREEZE, main_freeze)

    binding = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "l2_a1_freeze_sha256": sha(project / MODULE.MAIN_FREEZE),
        "matrix": MODULE.expected_matrix(),
        "input_hashes": input_hashes,
        "evaluator": evaluator,
        "machine_requirements": dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
        "machine_freeze_sha256": sha(project / MODULE.MACHINE_FREEZE),
        "per_tree_limits": dict(MODULE.EXPECTED_PER_TREE_LIMITS),
        "scheduler": scheduler,
        "logical_thresholds": thresholds,
    }
    run_config = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_GENERATION_INITIALIZED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "binding": binding,
        "binding_sha256": MODULE.sha256_bytes(MODULE.canonical_json_bytes(binding)),
    }
    dump_json(project / MODULE.RUN_CONFIG, run_config)
    run_hash = sha(project / MODULE.RUN_CONFIG)

    entries: list[dict[str, object]] = []
    for identity in MODULE.expected_matrix():
        tree_relative = f"trees/{identity['precision_bits']}/{identity['slab_id']}.json"
        tree_path = result / tree_relative
        dump_json(
            tree_path,
            {
                "schema_version": 1,
                "protocol_id": MODULE.PROTOCOL_ID,
                "licensing": "FROZEN_PRODUCTION",
                "scientific_licensing_enabled": True,
                "producer_state": "FROZEN_TREE_ARCHIVED",
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
                "tree": identity,
                "run_config_sha256": run_hash,
                "evaluated_node_count": 1,
                "terminal_counts": {
                    "ENERGY_EXCLUDED": 0,
                    "RETURN_EXCLUDED": 1,
                },
                "nodes": [
                    {
                        "evaluator_result": {
                            "classification": "RETURN_EXCLUDED",
                        }
                    }
                ],
            },
        )
        relative = (
            f"tree_manifests/{identity['precision_bits']}/{identity['slab_id']}.json"
        )
        tree_manifest = result / relative
        dump_json(
            tree_manifest,
            {
                "schema_version": 1,
                "protocol_id": MODULE.PROTOCOL_ID,
                "licensing": "FROZEN_PRODUCTION",
                "scientific_licensing_enabled": True,
                "producer_state": "FROZEN_TREE_COMMITTED",
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
                "tree": identity,
                "run_config_sha256": run_hash,
                "tree_file": tree_relative,
                "tree_sha256": sha(tree_path),
                "node_files": {},
            },
        )
        entries.append(
            {
                **identity,
                "tree_manifest_file": relative,
                "tree_manifest_sha256": sha(tree_manifest),
            }
        )
    summary = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_ALL_TREES_ARCHIVED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "run_config_sha256": run_hash,
        "tree_count": 102,
        "trees": entries,
    }
    dump_json(project / MODULE.AGGREGATE_SUMMARY, summary)
    manifest = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": "FROZEN_AGGREGATE_COMMITTED",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "run_config_sha256": run_hash,
        "aggregate_summary_file": "aggregate_summary.json",
        "aggregate_summary_sha256": sha(project / MODULE.AGGREGATE_SUMMARY),
        "tree_manifests": entries,
    }
    dump_json(project / MODULE.AGGREGATE_MANIFEST, manifest)

    tree_root = {
        "algorithm": "sha256_canonical_json_ordered_manifest_entries_v1",
        "entry_count": 102,
        "sha256": MODULE.sha256_bytes(MODULE.canonical_json_bytes(entries)),
    }
    provenance = {
        "freeze_sha256": sha(project / MODULE.MAIN_FREEZE),
        "run_config_file": "run_config.json",
        "run_config_sha256": run_hash,
        "aggregate_summary_file": "aggregate_summary.json",
        "aggregate_summary_sha256": sha(project / MODULE.AGGREGATE_SUMMARY),
        "aggregate_manifest_file": "aggregate_manifest.json",
        "aggregate_manifest_sha256": sha(project / MODULE.AGGREGATE_MANIFEST),
        "evaluator_source_sha256": sha(project / MODULE.EVALUATOR_SOURCE),
        "evaluator_binary_file": str(binary),
        "evaluator_binary_sha256": sha(binary),
        "capd_commit": evaluator["capd_commit"],
        "capd_flags": evaluator["capd_flags"],
        "scheduler": scheduler,
        "logical_thresholds": thresholds,
        "machine_freeze_file": MODULE.MACHINE_FREEZE,
        "machine_freeze_sha256": sha(project / MODULE.MACHINE_FREEZE),
        "machine_requirements": machine["machine_requirements"],
        "prefreeze_review_file": MODULE.PREFREEZE_REVIEW,
        "prefreeze_review_sha256": sha(project / MODULE.PREFREEZE_REVIEW),
        "tree_manifest_root": tree_root,
    }
    provenance["archive_generation_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(provenance)
    )
    checker = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "checker_mode": MODULE.CHECKER_MODE,
        "checker_status": MODULE.CHECKER_STATUS,
        "milestone_status": MODULE.PASS_STATUS,
        "theorem_status": MODULE.PASS_STATUS,
        "final_status": None,
        "promotion_authorized": True,
        "aggregate_checks": 1,
        "failure_count": 0,
        "failures": [],
        "tree_stats": [
            {
                **identity,
                "node_count": 1,
                "energy_excluded": 0,
                "return_excluded": 1,
                "split_nodes": 0,
            }
            for identity in MODULE.expected_matrix()
        ],
        "l1_protected_box_replay": {
            key: sha(project / relative)
            for key, relative in MODULE.L1_REPLAY_FILES.items()
        } | {
            "minimum_krawczyk_to_plan_boundary_margin": {
                "numerator": 1,
                "denominator": 1,
            },
        },
        "checker_source_sha256": sha(project / MODULE.CHECKER),
        "provenance_bindings": provenance,
        "claim_boundary": MODULE.CHECKER_CLAIM_BOUNDARY,
    }
    dump_json(project / MODULE.INDEPENDENT_CHECKER, checker)
    postcheck = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "checker_mode": MODULE.CHECKER_MODE,
        "checker_status": MODULE.CHECKER_STATUS,
        "milestone_status": MODULE.PASS_STATUS,
        "theorem_status": MODULE.PASS_STATUS,
        "final_status": None,
        "promotion_authorized": True,
        "checker_file": "independent_checker.json",
        "checker_sha256": sha(project / MODULE.INDEPENDENT_CHECKER),
        "archive_generation_sha256": provenance["archive_generation_sha256"],
        "provenance_bindings_sha256": MODULE.sha256_bytes(
            MODULE.canonical_json_bytes(provenance)
        ),
    }
    dump_json(project / MODULE.POSTCHECK, postcheck)

    accepted = (
        f"Protocol: `{MODULE.PROTOCOL_ID}`\n\n"
        f"Status: {MODULE.PASS_STATUS}\n"
        f"milestone_status = {MODULE.PASS_STATUS}\n"
        f"theorem_status = {MODULE.PASS_STATUS}\n"
        "final_status = null\n"
        f"{MODULE.MARKDOWN_CLAIM_BOUNDARY}\n"
    )
    write(project / MODULE.A415_CERTIFICATE, "# A4.15 certificate\n\n" + accepted)
    write(project / MODULE.PRODUCTION_REPORT, "# Production report\n\n" + accepted)
    return project


def rewrite_json(path: Path, mutate: object) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert callable(mutate)
    mutate(payload)
    dump_json(path, payload)


def rebind_tampered_s0(project: Path, payload: dict[str, object]) -> None:
    """Write S0 evidence and rebind only its main-freeze input edge."""

    s0_path = project / MODULE.S0_REPLAY
    dump_json(s0_path, payload)
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    freeze["input_hashes"][MODULE.S0_REPLAY] = sha(s0_path)
    dump_json(freeze_path, freeze)


def test_release_builder_mandatory_input_tuple_is_exact_complete_17_chain() -> None:
    assert MODULE.REQUIRED_MAIN_FREEZE_HASHES == (
        "scripts/check_r401_val_l2_all_slabs_independent.py",
        "scripts/run_r401_val_l2_all_slabs.py",
        "validated/capd_r401_local_complement_mp.cpp",
        "validated/CAPD_DEPENDENCY.md",
        "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
        "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md",
        "research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json",
        "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md",
        "research/route_a_wave_trace/R401_VAL_L2_A1_S0_COMPATIBILITY_REPLAY.json",
        "scripts/replay_r401_val_l2_s0_through_a1_checker.py",
        "scripts/build_r401_val_l2_a1_release_provenance.py",
        "research/route_a_wave_trace/R401_VAL_L2_A1_RELEASE_PROVENANCE_CONTRACT.md",
        "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
        "results/r401_val_l1_branch/summary.json",
        "results/r401_val_l1_branch/manifest.json",
        "results/r401_val_l1_branch/independent_checker.json",
        "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
    )


def test_build_is_deterministic_idempotent_and_verify_only_is_read_only(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    first = MODULE.build_release(project)
    release = MODULE.release_path(project)
    before = release.read_bytes()
    second = MODULE.build_release(project)
    verified = MODULE.verify_release(project)
    assert first == second == verified
    assert release.read_bytes() == before
    assert first["tree_manifest_root"]["entry_count"] == 102
    assert len(first["archive_generation_sha256"]) == 64
    assert len(first["artifact_roles"]) == 19
    assert set(first["files"]) == set(first["artifact_roles"].values())
    assert MODULE.RELEASE_NAME not in first["files"]


def test_duplicate_json_key_is_rejected_before_release(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.POSTCHECK
    target.write_text(
        '{"protocol_id":"R401-VAL-L2-A1","protocol_id":"forged"}\n',
        encoding="utf-8",
    )
    with pytest.raises(MODULE.StrictJSONError, match="DUPLICATE_JSON_KEY"):
        MODULE.build_release(project)


def test_duplicate_tree_manifest_key_is_rejected_even_with_coherent_hashes(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    target = (
        project
        / MODULE.RESULT_RELATIVE.as_posix()
        / "tree_manifests/128/S000.json"
    )
    raw = target.read_text(encoding="utf-8")
    needle = f'  "protocol_id": "{MODULE.PROTOCOL_ID}",\n'
    assert raw.count(needle) == 1
    target.write_text(raw.replace(needle, needle + needle), encoding="utf-8")

    # Rebind every public digest that the old hash-only implementation used.
    # The malformed manifest must still be rejected on its bytes.
    summary_path = project / MODULE.AGGREGATE_SUMMARY
    manifest_path = project / MODULE.AGGREGATE_MANIFEST
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["trees"][0]["tree_manifest_sha256"] = sha(target)
    dump_json(summary_path, summary)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["tree_manifests"] = summary["trees"]
    manifest["aggregate_summary_sha256"] = sha(summary_path)
    dump_json(manifest_path, manifest)

    checker_path = project / MODULE.INDEPENDENT_CHECKER
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    bindings = checker["provenance_bindings"]
    bindings["aggregate_summary_sha256"] = sha(summary_path)
    bindings["aggregate_manifest_sha256"] = sha(manifest_path)
    bindings["tree_manifest_root"] = {
        "algorithm": "sha256_canonical_json_ordered_manifest_entries_v1",
        "entry_count": 102,
        "sha256": MODULE.sha256_bytes(
            MODULE.canonical_json_bytes(summary["trees"])
        ),
    }
    without_generation = dict(bindings)
    without_generation.pop("archive_generation_sha256")
    bindings["archive_generation_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(without_generation)
    )
    dump_json(checker_path, checker)

    postcheck_path = project / MODULE.POSTCHECK
    postcheck = json.loads(postcheck_path.read_text(encoding="utf-8"))
    postcheck["checker_sha256"] = sha(checker_path)
    postcheck["archive_generation_sha256"] = bindings[
        "archive_generation_sha256"
    ]
    postcheck["provenance_bindings_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(bindings)
    )
    dump_json(postcheck_path, postcheck)

    with pytest.raises(MODULE.StrictJSONError, match="DUPLICATE_JSON_KEY"):
        MODULE.build_release(project)


def test_exponent_overflow_is_rejected_as_nonfinite_json(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.POSTCHECK
    raw = target.read_text(encoding="utf-8")
    assert raw.endswith("}\n")
    target.write_text(raw[:-2] + ',\n  "overflow": 1e400\n}\n', encoding="utf-8")
    with pytest.raises(MODULE.StrictJSONError, match="NONFINITE_JSON_NUMBER"):
        MODULE.build_release(project)


def test_schema_boolean_cannot_impersonate_integer_version(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.POSTCHECK
    rewrite_json(target, lambda payload: payload.__setitem__("schema_version", True))
    with pytest.raises(MODULE.StatusContractError, match="NAMESPACE_MISMATCH"):
        MODULE.build_release(project)


def test_integral_float_cannot_impersonate_manifest_precision(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    summary_path = project / MODULE.AGGREGATE_SUMMARY
    manifest_path = project / MODULE.AGGREGATE_MANIFEST
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["trees"][0]["precision_bits"] = 128.0
    dump_json(summary_path, summary)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["tree_manifests"] = summary["trees"]
    manifest["aggregate_summary_sha256"] = sha(summary_path)
    dump_json(manifest_path, manifest)

    checker_path = project / MODULE.INDEPENDENT_CHECKER
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    bindings = checker["provenance_bindings"]
    bindings["aggregate_summary_sha256"] = sha(summary_path)
    bindings["aggregate_manifest_sha256"] = sha(manifest_path)
    bindings["tree_manifest_root"] = {
        "algorithm": "sha256_canonical_json_ordered_manifest_entries_v1",
        "entry_count": 102,
        "sha256": MODULE.sha256_bytes(
            MODULE.canonical_json_bytes(summary["trees"])
        ),
    }
    without_generation = dict(bindings)
    without_generation.pop("archive_generation_sha256")
    bindings["archive_generation_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(without_generation)
    )
    dump_json(checker_path, checker)
    postcheck_path = project / MODULE.POSTCHECK
    postcheck = json.loads(postcheck_path.read_text(encoding="utf-8"))
    postcheck["checker_sha256"] = sha(checker_path)
    postcheck["archive_generation_sha256"] = bindings[
        "archive_generation_sha256"
    ]
    postcheck["provenance_bindings_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(bindings)
    )
    dump_json(postcheck_path, postcheck)

    with pytest.raises(
        MODULE.GenerationContractError,
        match="IDENTITY_TYPE_OR_VALUE_MISMATCH",
    ):
        MODULE.build_release(project)


def test_symlinked_tree_manifest_is_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = (
        project
        / MODULE.RESULT_RELATIVE.as_posix()
        / "tree_manifests/128/S000.json"
    )
    other = target.with_name("S001.json")
    target.unlink()
    target.symlink_to(other)
    with pytest.raises(MODULE.PathContractError, match="SYMLINK_REJECTED"):
        MODULE.build_release(project)


def test_aggregate_path_traversal_is_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    summary_path = project / MODULE.AGGREGATE_SUMMARY
    manifest_path = project / MODULE.AGGREGATE_MANIFEST
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    summary["trees"][0]["tree_manifest_file"] = "../escape.json"
    manifest["tree_manifests"] = summary["trees"]
    dump_json(summary_path, summary)
    manifest["aggregate_summary_sha256"] = sha(summary_path)
    dump_json(manifest_path, manifest)
    with pytest.raises(MODULE.PathContractError, match="PATH_TRAVERSAL"):
        MODULE.build_release(project)


def test_duplicate_or_reordered_tree_identity_is_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    summary_path = project / MODULE.AGGREGATE_SUMMARY
    manifest_path = project / MODULE.AGGREGATE_MANIFEST
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    summary["trees"][1] = dict(summary["trees"][0])
    manifest["tree_manifests"] = summary["trees"]
    dump_json(summary_path, summary)
    manifest["aggregate_summary_sha256"] = sha(summary_path)
    dump_json(manifest_path, manifest)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="DUPLICATE_TREE_IDENTITY|IDENTITY_TYPE_OR_VALUE_MISMATCH",
    ):
        MODULE.build_release(project)


def test_checker_status_mismatch_cannot_be_released(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    checker_path = project / MODULE.INDEPENDENT_CHECKER
    rewrite_json(
        checker_path,
        lambda payload: payload.__setitem__("checker_status", "FAIL_INDEPENDENT_CHECKER"),
    )
    with pytest.raises(MODULE.StatusContractError, match="STATUS_MISMATCH"):
        MODULE.build_release(project)


def test_archive_generation_is_independently_recomputed(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    checker_path = project / MODULE.INDEPENDENT_CHECKER
    postcheck_path = project / MODULE.POSTCHECK
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    checker["provenance_bindings"]["archive_generation_sha256"] = "0" * 64
    dump_json(checker_path, checker)
    postcheck = json.loads(postcheck_path.read_text(encoding="utf-8"))
    postcheck["checker_sha256"] = sha(checker_path)
    postcheck["archive_generation_sha256"] = "0" * 64
    postcheck["provenance_bindings_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(checker["provenance_bindings"])
    )
    dump_json(postcheck_path, postcheck)
    with pytest.raises(
        MODULE.GenerationContractError, match="ARCHIVE_GENERATION_SHA256_MISMATCH"
    ):
        MODULE.build_release(project)


def test_existing_release_cannot_be_overwritten_by_different_generation(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    MODULE.build_release(project)
    release = MODULE.release_path(project)
    original = release.read_bytes()
    report = project / MODULE.PRODUCTION_REPORT
    report.write_text(report.read_text(encoding="utf-8") + "new generation bytes\n")
    with pytest.raises(
        MODULE.GenerationContractError,
        match="RELEASE_ALREADY_BOUND_TO_DIFFERENT_GENERATION",
    ):
        MODULE.build_release(project)
    assert release.read_bytes() == original


@pytest.mark.parametrize("relative", [MODULE.A415_CERTIFICATE, MODULE.PRODUCTION_REPORT])
def test_contradictory_markdown_status_declarations_are_rejected(
    tmp_path: Path,
    relative: str,
) -> None:
    project = make_release_fixture(tmp_path)
    target = project / relative
    target.write_text(
        target.read_text(encoding="utf-8")
        + "Status: FAIL_INDEPENDENT_CHECKER\n"
        + "final_status = PASS_GLOBAL\n",
        encoding="utf-8",
    )
    with pytest.raises(
        MODULE.StatusContractError,
        match="STATUS_BLOCK_NOT_EXACT_OR_CONTRADICTORY",
    ):
        MODULE.build_release(project)


def test_additional_named_status_declarations_are_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.PRODUCTION_REPORT
    target.write_text(
        target.read_text(encoding="utf-8")
        + "release_status = FAIL_GLOBAL\n"
        + "checker_status = FAIL_INDEPENDENT_CHECKER\n",
        encoding="utf-8",
    )
    with pytest.raises(
        MODULE.StatusContractError,
        match="STATUS_BLOCK_NOT_EXACT_OR_CONTRADICTORY",
    ):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "declaration",
    [
        "- release_status = FAIL_GLOBAL",
        "> final_status = PASS_GLOBAL",
        "**Status:** FAIL_GLOBAL",
        "- Claim boundary: GLOBAL CLAIM",
        "| release_status | FAIL_GLOBAL |",
        "Status - FAIL_GLOBAL",
        "Status：FAIL_GLOBAL",
        "Claim boundary — GLOBAL CLAIM",
        r"Status\: FAIL_GLOBAL",
        r"final_status\= PASS_GLOBAL",
        "Status&#58; FAIL_GLOBAL",
        "release_status&#61; FAIL_GLOBAL",
        "promotion_authorized&#58; true",
        "Claim boundary&#58; GLOBAL CLAIM",
        "Status has been discussed without punctuation",
        "release_status",
    ],
)
def test_markdown_decorated_authority_declarations_are_rejected(
    tmp_path: Path,
    declaration: str,
) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.PRODUCTION_REPORT
    target.write_text(
        target.read_text(encoding="utf-8") + declaration + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        MODULE.StatusContractError,
        match="STATUS_BLOCK_NOT_EXACT_OR_CONTRADICTORY",
    ):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "declaration",
    [
        "- Verdict: REJECT_FOR_FREEZE",
        "> Verdict: PENDING",
        "**Verdict:** REJECT_FOR_FREEZE",
        "| Verdict | REJECT_FOR_FREEZE |",
        "Verdict - PENDING",
        "Verdict：REJECT_FOR_FREEZE",
        r"Verdict\: REJECT_FOR_FREEZE",
        r"Verdict\= PENDING",
        "Verdict&#58; REJECT_FOR_FREEZE",
        "Verdict",
    ],
)
def test_prefreeze_markdown_decorated_verdicts_are_rejected(
    tmp_path: Path,
    declaration: str,
) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.PREFREEZE_REVIEW
    target.write_text(
        target.read_text(encoding="utf-8") + declaration + "\n",
        encoding="utf-8",
    )
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    freeze["input_hashes"][MODULE.PREFREEZE_REVIEW] = sha(target)
    dump_json(freeze_path, freeze)
    with pytest.raises(
        MODULE.StatusContractError,
        match="PREFREEZE_REVIEW_NOT_EXACTLY_ACCEPTED",
    ):
        MODULE.build_release(project)


def test_additional_json_status_declaration_is_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.POSTCHECK
    rewrite_json(
        target,
        lambda payload: payload.__setitem__("release_status", "FAIL_GLOBAL"),
    )
    with pytest.raises(
        MODULE.StatusContractError,
        match="UNEXPECTED_AUTHORITY_FIELD|POSTCHECK_KEY_SET_MISMATCH",
    ):
        MODULE.build_release(project)


def test_nested_json_status_metadata_is_rejected_by_exact_schema(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.POSTCHECK
    rewrite_json(
        target,
        lambda payload: payload.__setitem__(
            "metadata", {"release_status": "FAIL_GLOBAL"}
        ),
    )
    with pytest.raises(MODULE.StatusContractError, match="POSTCHECK_KEY_SET_MISMATCH"):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "mutation",
    [
        "float_precision",
        "nested_status",
        "l1_authorized",
        "l1_hash",
        "valid_count_disagrees_with_tree",
    ],
)
def test_checker_nested_diagnostics_use_exact_schema(
    tmp_path: Path,
    mutation: str,
) -> None:
    project = make_release_fixture(tmp_path)
    checker_path = project / MODULE.INDEPENDENT_CHECKER
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    if mutation == "float_precision":
        checker["tree_stats"][0]["precision_bits"] = 128.0
    elif mutation == "nested_status":
        checker["tree_stats"][0]["release_status"] = "FAIL_GLOBAL"
    elif mutation == "l1_authorized":
        checker["l1_protected_box_replay"]["authorized"] = False
    elif mutation == "l1_hash":
        checker["l1_protected_box_replay"]["summary_sha256"] = "0" * 64
    else:
        checker["tree_stats"][0]["node_count"] = 2
        checker["tree_stats"][0]["return_excluded"] = 2
    dump_json(checker_path, checker)
    postcheck_path = project / MODULE.POSTCHECK
    postcheck = json.loads(postcheck_path.read_text(encoding="utf-8"))
    postcheck["checker_sha256"] = sha(checker_path)
    dump_json(postcheck_path, postcheck)
    with pytest.raises(
        (MODULE.StatusContractError, MODULE.GenerationContractError),
        match="TREE_STATS|NESTED_AUTHORITY|L1_REPLAY",
    ):
        MODULE.build_release(project)


def test_checker_tree_stats_recomputation_rejects_non_scalar_tree_classification(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    tree = (
        project
        / MODULE.RESULT_RELATIVE.as_posix()
        / "trees/128/S000.json"
    )
    rewrite_json(
        tree,
        lambda payload: payload["nodes"][0]["evaluator_result"].__setitem__(
            "classification", []
        ),
    )
    with pytest.raises(
        MODULE.StatusContractError,
        match="TREE_STATS_PAYLOAD_CLASSIFICATION_MISMATCH",
    ):
        MODULE.build_release(project)


@pytest.mark.parametrize("unsafe", ["./a.json", "a//b.json", "a/"])
def test_path_normalization_aliases_are_rejected(unsafe: str) -> None:
    with pytest.raises(MODULE.PathContractError, match="NONCANONICAL_PATH"):
        MODULE.safe_relative_path(unsafe)


def test_semantic_gate_and_hash_use_the_same_byte_snapshot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    project = make_release_fixture(tmp_path)
    target = project / MODULE.A415_CERTIFICATE
    real_sha256 = MODULE.sha256
    swapped = False

    def racing_sha256(path: Path) -> str:
        nonlocal swapped
        if Path(path) == target and not swapped:
            swapped = True
            target.write_text(
                "Status: FAIL_GLOBAL\nfinal_status = PASS_GLOBAL\n",
                encoding="utf-8",
            )
        return real_sha256(path)

    monkeypatch.setattr(MODULE, "sha256", racing_sha256)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="INPUT_CHANGED_DURING_RELEASE_BUILD|RELEASE_FILE_HASH_MISMATCH",
    ):
        MODULE.build_release(project)
    assert swapped


def test_publication_links_open_inode_not_mutable_temp_name(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    project = make_release_fixture(tmp_path)
    real_link = MODULE.os.link
    attacked = False

    def racing_link(source: str, destination: str, *args: object, **kwargs: object) -> None:
        nonlocal attacked
        result_dir = project.joinpath(*MODULE.RESULT_RELATIVE.parts)
        temporary = list(result_dir.glob(f".{MODULE.RELEASE_NAME}.seal-*"))
        assert len(temporary) == 1
        temporary[0].unlink()
        temporary[0].write_bytes(b"ATTACKER BYTES")
        attacked = True
        real_link(source, destination, *args, **kwargs)

    monkeypatch.setattr(MODULE.os, "link", racing_link)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="RELEASE_PUBLICATION_SOURCE_OR_LINK_FAILURE",
    ):
        MODULE.build_release(project)
    assert attacked
    assert not MODULE.release_path(project).exists()


def test_release_exact_set_and_path_traversal_are_checked_read_only(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    MODULE.build_release(project)
    release = MODULE.release_path(project)
    payload = json.loads(release.read_text(encoding="utf-8"))
    old = payload["artifact_roles"]["production_report"]
    payload["artifact_roles"]["production_report"] = "../escape.md"
    payload["files"]["../escape.md"] = payload["files"].pop(old)
    dump_json(release, payload)
    with pytest.raises(MODULE.PathContractError, match="PATH_TRAVERSAL"):
        MODULE.verify_release(project)


def test_aggregate_manifest_float_alias_cannot_equal_summary_integer(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    manifest_path = project / MODULE.AGGREGATE_MANIFEST
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["tree_manifests"][0]["precision_bits"] = 128.0
    dump_json(manifest_path, manifest)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="AGGREGATE_TREE_MANIFEST_LIST_MISMATCH",
    ):
        MODULE.build_release(project)


def test_verify_rejects_semantically_equal_noncanonical_release_bytes(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    MODULE.build_release(project)
    release = MODULE.release_path(project)
    payload = json.loads(release.read_text(encoding="utf-8"))
    release.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    with pytest.raises(
        MODULE.GenerationContractError,
        match="RELEASE_NONCANONICAL_BYTES",
    ):
        MODULE.verify_release(project)


def test_release_self_hash_and_extra_hash_are_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    MODULE.build_release(project)
    release = MODULE.release_path(project)
    original = json.loads(release.read_text(encoding="utf-8"))

    extra = json.loads(json.dumps(original))
    extra["files"]["extra.txt"] = "0" * 64
    dump_json(release, extra)
    with pytest.raises(
        MODULE.GenerationContractError, match="RELEASE_FILE_HASH_EXACT_SET_MISMATCH"
    ):
        MODULE.verify_release(project)

    self_bound = json.loads(json.dumps(original))
    old = self_bound["artifact_roles"]["production_report"]
    own_path = f"{MODULE.RESULT_RELATIVE.as_posix()}/{MODULE.RELEASE_NAME}"
    self_bound["artifact_roles"]["production_report"] = own_path
    self_bound["files"][own_path] = self_bound["files"].pop(old)
    dump_json(release, self_bound)
    with pytest.raises(
        MODULE.GenerationContractError, match="MUST_NOT_HASH_ITSELF"
    ):
        MODULE.verify_release(project)


def test_preexisting_release_hardlink_alias_is_rejected(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    MODULE.build_release(project)
    release = MODULE.release_path(project)
    alias = release.with_name("release-alias.json")
    alias.hardlink_to(release)
    with pytest.raises(MODULE.PathContractError, match="HARDLINK_ALIAS"):
        MODULE.build_release(project)
    with pytest.raises(MODULE.PathContractError, match="HARDLINK_ALIAS"):
        MODULE.verify_release(project)


@pytest.mark.parametrize("missing", MODULE.REQUIRED_MAIN_FREEZE_HASHES)
def test_main_freeze_must_bind_every_complete_17_chain_input(
    tmp_path: Path,
    missing: str,
) -> None:
    project = make_release_fixture(tmp_path)
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    del freeze["input_hashes"][missing]
    dump_json(freeze_path, freeze)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="MAIN_FREEZE_MISSING_RELEASE_INPUT_HASHES",
    ):
        MODULE.build_release(project)


def test_main_freeze_checker_hash_must_equal_checker_input_hash(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    freeze["checker_source_sha256"] = "0" * 64
    dump_json(freeze_path, freeze)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="MAIN_FREEZE_CHECKER_HASH_DAG_MISMATCH",
    ):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "mutation",
    [
        "extra_key",
        "missing_key",
        "checker_hash",
        "adapter_hash",
        "release_hash",
        "manifest_hash",
        "postcheck_hash",
        "protocol_id",
        "status",
        "source_release",
        "claim_boundary",
        "tree_count",
        "tree_count_boolean",
        "node_count",
        "manifest_hash_checks",
        "status_counts",
        "status_counts_extra_key",
        "tree_counts_order",
        "tree_counts_length",
        "tree_counts_extra_key",
        "tree_counts_float_precision",
        "tree_counts_node_count",
        "tree_counts_status_count",
        "tree_counts_status_extra_key",
    ],
)
def test_s0_replay_exact_schema_hashes_and_semantics_reject_tampering(
    tmp_path: Path,
    mutation: str,
) -> None:
    project = make_release_fixture(tmp_path)
    s0_path = project / MODULE.S0_REPLAY
    s0 = json.loads(s0_path.read_text(encoding="utf-8"))
    if mutation == "extra_key":
        s0["metadata"] = {}
    elif mutation == "missing_key":
        del s0["claim_boundary"]
    elif mutation == "checker_hash":
        s0["checker_source_sha256"] = "0" * 64
    elif mutation == "adapter_hash":
        s0["adapter_source_sha256"] = "0" * 64
    elif mutation == "release_hash":
        s0["s0_release_provenance_sha256"] = "0" * 64
    elif mutation == "manifest_hash":
        s0["s0_manifest_sha256"] = "0" * 64
    elif mutation == "postcheck_hash":
        s0["s0_postcheck_sha256"] = "0" * 64
    elif mutation == "protocol_id":
        s0["protocol_id"] = "R401-VAL-L2-S0"
    elif mutation == "status":
        s0["status"] = "PENDING"
    elif mutation == "source_release":
        s0["source_release"] = "R401-VAL-L2-A1"
    elif mutation == "claim_boundary":
        s0["claim_boundary"] = "held-out A1 replay"
    elif mutation == "tree_count":
        s0["tree_count"] = 7
    elif mutation == "tree_count_boolean":
        s0["tree_count"] = True
    elif mutation == "node_count":
        s0["node_count"] = 3_017
    elif mutation == "manifest_hash_checks":
        s0["manifest_hash_checks"] = 6_054
    elif mutation == "status_counts":
        s0["status_counts"]["UNKNOWN"] = 1_483
    elif mutation == "status_counts_extra_key":
        s0["status_counts"]["ROOT_CANDIDATE"] = 0
    elif mutation == "tree_counts_order":
        s0["tree_counts"][0], s0["tree_counts"][1] = (
            s0["tree_counts"][1],
            s0["tree_counts"][0],
        )
    elif mutation == "tree_counts_length":
        s0["tree_counts"].pop()
    elif mutation == "tree_counts_extra_key":
        s0["tree_counts"][0]["metadata"] = {}
    elif mutation == "tree_counts_float_precision":
        s0["tree_counts"][0]["precision_bits"] = 128.0
    elif mutation == "tree_counts_node_count":
        s0["tree_counts"][0]["node_count"] = 487
    elif mutation == "tree_counts_status_count":
        s0["tree_counts"][0]["status_counts"]["UNKNOWN"] = 240
    else:
        s0["tree_counts"][0]["status_counts"]["ROOT_CANDIDATE"] = 0
    rebind_tampered_s0(project, s0)
    with pytest.raises(
        (MODULE.StatusContractError, MODULE.GenerationContractError),
        match="S0_REPLAY",
    ):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "field",
    [
        "checker_source_sha256",
        "adapter_source_sha256",
        "s0_release_provenance_sha256",
        "s0_manifest_sha256",
        "s0_postcheck_sha256",
    ],
)
def test_s0_replay_hashes_are_bound_to_actual_same_snapshot_files(
    tmp_path: Path,
    field: str,
) -> None:
    project = make_release_fixture(tmp_path)
    relative = MODULE.S0_REPLAY_HASH_FILES[field]
    target = project / relative
    if field in {"checker_source_sha256", "adapter_source_sha256"}:
        target.write_bytes(target.read_bytes() + b"# tamper\n")
        freeze_path = project / MODULE.MAIN_FREEZE
        freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
        freeze["input_hashes"][relative] = sha(target)
        if field == "checker_source_sha256":
            freeze["checker_source_sha256"] = sha(target)
        dump_json(freeze_path, freeze)
    else:
        payload = json.loads(target.read_text(encoding="utf-8"))
        payload["tamper"] = True
        dump_json(target, payload)
    with pytest.raises(
        MODULE.StatusContractError,
        match="S0_REPLAY_HASH_MISMATCH",
    ):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "mutation, expected",
    [
        ("extra_key", "EVALUATOR_KEY_SET"),
        ("missing_key", "EVALUATOR_KEY_SET"),
        ("wrong_commit", "EVALUATOR_CAPD_BINDING"),
        ("wrong_whitelist", "EVALUATOR_WHITELIST"),
    ],
)
def test_main_freeze_evaluator_has_exact_producer_schema(
    tmp_path: Path,
    mutation: str,
    expected: str,
) -> None:
    project = make_release_fixture(tmp_path)
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    evaluator = freeze["evaluator"]
    if mutation == "extra_key":
        evaluator["binary_size_bytes"] = 1
    elif mutation == "missing_key":
        del evaluator["status_returncode_whitelist"]
    elif mutation == "wrong_commit":
        evaluator["capd_commit"] = "0" * 40
    else:
        evaluator["status_returncode_whitelist"]["invalid"] = []
    dump_json(freeze_path, freeze)
    with pytest.raises(MODULE.GenerationContractError, match=expected):
        MODULE.build_release(project)


@pytest.mark.parametrize(
    "mutation, expected",
    [
        ("extra_key", "BINDING_KEY_SET"),
        ("boolean_schema", "BINDING_NAMESPACE_OR_LICENSE"),
        ("wrong_license", "BINDING_NAMESPACE_OR_LICENSE"),
        ("evaluator_drift", "EVALUATOR_DIFFERS_FROM_FREEZE"),
    ],
)
def test_run_config_binding_uses_exact_runner_schema_and_frozen_evaluator(
    tmp_path: Path,
    mutation: str,
    expected: str,
) -> None:
    project = make_release_fixture(tmp_path)
    run_path = project / MODULE.RUN_CONFIG
    run = json.loads(run_path.read_text(encoding="utf-8"))
    binding = run["binding"]
    if mutation == "extra_key":
        binding["metadata"] = {}
    elif mutation == "boolean_schema":
        binding["schema_version"] = True
    elif mutation == "wrong_license":
        binding["licensing"] = "TEST_ONLY"
    else:
        binding["evaluator"]["capd_commit"] = "0" * 40
    run["binding_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(binding)
    )
    dump_json(run_path, run)
    with pytest.raises(
        (MODULE.GenerationContractError, MODULE.StatusContractError),
        match=expected,
    ):
        MODULE.build_release(project)


def test_every_extra_main_freeze_input_hash_is_replayed(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    extra = project / "research/extra-frozen-input.txt"
    write(extra, "actual bytes\n")
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    freeze["input_hashes"]["research/extra-frozen-input.txt"] = "0" * 64
    dump_json(freeze_path, freeze)
    with pytest.raises(
        MODULE.GenerationContractError,
        match="MAIN_FREEZE_INPUT_HASH_MISMATCH",
    ):
        MODULE.build_release(project)


def test_every_extra_json_freeze_input_is_strictly_parsed(tmp_path: Path) -> None:
    project = make_release_fixture(tmp_path)
    extra = project / "research/extra-frozen-input.json"
    extra.parent.mkdir(parents=True, exist_ok=True)
    extra.write_text('{"x":1,"x":2}\n', encoding="utf-8")
    freeze_path = project / MODULE.MAIN_FREEZE
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    freeze["input_hashes"]["research/extra-frozen-input.json"] = sha(extra)
    dump_json(freeze_path, freeze)
    with pytest.raises(MODULE.StrictJSONError, match="DUPLICATE_JSON_KEY"):
        MODULE.build_release(project)


def test_evaluator_absolute_path_normalization_alias_is_rejected(
    tmp_path: Path,
) -> None:
    project = make_release_fixture(tmp_path)
    machine_path = project / MODULE.MACHINE_FREEZE
    main_path = project / MODULE.MAIN_FREEZE
    machine = json.loads(machine_path.read_text(encoding="utf-8"))
    main = json.loads(main_path.read_text(encoding="utf-8"))
    canonical = main["evaluator"]["binary_file"]
    aliased = str(Path(canonical).parent / ".." / Path(canonical).parent.name / Path(canonical).name)
    assert aliased != canonical and "/../" in aliased
    machine["evaluator"]["binary_file"] = aliased
    main["evaluator"]["binary_file"] = aliased
    dump_json(machine_path, machine)
    main["input_hashes"][MODULE.MACHINE_FREEZE] = sha(machine_path)
    dump_json(main_path, main)
    with pytest.raises(
        MODULE.PathContractError,
        match="BINARY_NOT_ABSOLUTE|BINARY_NOT_CANONICAL",
    ):
        MODULE.build_release(project)
