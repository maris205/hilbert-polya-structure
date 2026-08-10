from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/check_r401_val_l3_a1_composite_independent.py"


def load_module():
    specification = importlib.util.spec_from_file_location("l3_a1_composite", SOURCE)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


M = load_module()


def write_json(path: Path, payload: Any) -> bytes:
    raw = M.canonical_json_bytes(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return raw


def write_branch_json(path: Path, payload: Any) -> bytes:
    raw = M.branch_transaction_json_bytes(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return raw


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def mock_run_config(result: Path) -> tuple[dict[str, Any], bytes]:
    payload = {
        "schema_version": 1,
        "protocol_id": M.PROTOCOL_ID,
        "artifact_role": "RUN_CONFIG",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "production_authorized": False,
        "scientific_licensing_enabled": False,
        "matrix": M.matrix_payload(),
        "matrix_id": M.matrix_id(),
        "scheduler_policy": M.SCHEDULER_POLICY,
        "limits": M.candidate_limits(),
        "paths": {
            "authoritative_root": str(result),
            "operational_root": str(result) + ".operational",
        },
        "main_freeze": {"path": None, "sha256": None},
        "machine_freeze": {"path": None, "sha256": None},
        "prefreeze_review": {"path": None, "sha256": None, "accepted": False},
        "source_bindings": M.expected_scheduler_sources(),
        "claim_boundary": M.SCHEDULER_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    return payload, write_json(result / "run_config.json", payload)


def make_component(result: Path, name: str, run_hash: str) -> None:
    entries: list[dict[str, Any]] = []
    for cell in M.matrix_payload():
        relative = Path(name) / "cell_manifests" / str(cell["precision_bits"]) / f"{cell['slab_id']}.json"
        cell_root = result / name / "cells" / str(cell["precision_bits"]) / cell["slab_id"]
        if name == "static":
            proof_raw = write_json(
                cell_root / "proof.json",
                {"cell": cell, "mock_only": True, "kind": "static-proof"},
            )
            record_raw = write_json(
                cell_root / "record.json",
                {"cell": cell, "mock_only": True, "kind": "static-record"},
            )
            files: dict[str, Any] = {
                "proof.json": {"sha256": digest(proof_raw), "size_bytes": len(proof_raw)},
                "record.json": {"sha256": digest(record_raw), "size_bytes": len(record_raw)},
            }
        else:
            stdout_raw = f"mock branch {cell['precision_bits']} {cell['slab_id']}\n".encode()
            stderr_raw = b""
            (cell_root / "stdout.txt").parent.mkdir(parents=True, exist_ok=True)
            (cell_root / "stdout.txt").write_bytes(stdout_raw)
            (cell_root / "stderr.txt").write_bytes(stderr_raw)
            record_raw = write_branch_json(
                cell_root / "record.json",
                {"cell": cell, "mock_only": True, "kind": "branch-record"},
            )
            files = {
                (Path(name) / "cells" / str(cell["precision_bits"]) / cell["slab_id"] / "record.json").as_posix(): digest(record_raw),
                (Path(name) / "cells" / str(cell["precision_bits"]) / cell["slab_id"] / "stderr.txt").as_posix(): digest(stderr_raw),
                (Path(name) / "cells" / str(cell["precision_bits"]) / cell["slab_id"] / "stdout.txt").as_posix(): digest(stdout_raw),
            }
        if name == "static":
            cell_manifest = {
                "schema_version": 1,
                "protocol_id": M.PROTOCOL_ID,
                "artifact_role": "MOCK_STATIC_CELL_MANIFEST",
                "artifact_status": "MOCK_ONLY_NON_LICENSING",
                "authority": "PRODUCER_ONLY",
                "mock_only": True,
                "cell": cell,
                "matrix_id": M.matrix_id(),
                "main_freeze_sha256": None,
                "run_config_sha256": run_hash,
                "scheduler_classification": "COMMITTED_EVALUATOR_RESULT",
                "evaluator_status": "STATIC_CELL_CERTIFIED",
                "files": files,
                "scientific_licensing_enabled": False,
                "claim_boundary": M.SCHEDULER_MOCK_CLAIM_BOUNDARY,
                "component_status": None,
                "milestone_status": None,
                "theorem_status": None,
                "final_status": None,
            }
            raw = write_json(result / relative, cell_manifest)
        else:
            cell_manifest = {
                "schema_version": 1,
                "protocol_id": M.PROTOCOL_ID,
                "artifact_role": "BRANCH_CELL_MANIFEST",
                "authority": "PRODUCER_ONLY",
                "budgets": M.BRANCH_CELL_BUDGETS,
                "cell_identity": cell,
                "claim_boundary": M.BRANCH_CELL_CLAIM_BOUNDARY,
                "component_status": None,
                "files": files,
                "final_status": None,
                "freeze_sha256": digest(b"mock branch freeze\n"),
                "matrix_id": M.matrix_id(),
                "milestone_status": None,
                "run_config_sha256": run_hash,
                "scientific_licensing_enabled": False,
                "task_binding_sha256": digest(
                    M.canonical_json_bytes({"cell": cell, "mock_only": True})
                ),
                "theorem_status": None,
            }
            raw = write_branch_json(result / relative, cell_manifest)
        entries.append(
            {
                "cell": cell,
                "path": relative.as_posix(),
                "sha256": digest(raw),
                "size_bytes": len(raw),
            }
        )
    root = digest(M.canonical_json_bytes(entries))
    mock_evaluator = None
    if name == "branch":
        evaluator_path = M.MOCK_BRANCH_EVALUATOR
        evaluator_raw = evaluator_path.read_bytes()
        mock_evaluator = {"path": str(evaluator_path), "sha256": digest(evaluator_raw)}
    summary = {
        "schema_version": 1,
        "protocol_id": M.PROTOCOL_ID,
        "artifact_role": f"MOCK_{name.upper()}_AGGREGATE_SUMMARY",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": M.matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_hash,
        "matrix": M.matrix_payload(),
        "cell_count": 102,
        "ordered_cell_manifest_root": root,
        "status_counts": {f"{name.upper()}_CELL_CERTIFIED": 102},
        "scheduler_classification_counts": {"COMMITTED_EVALUATOR_RESULT": 102},
        "scientific_licensing_enabled": False,
        "claim_boundary": M.SCHEDULER_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    if mock_evaluator is not None:
        summary["mock_evaluator"] = mock_evaluator
    summary_path = result / name / "aggregate_summary.json"
    summary_raw = write_json(summary_path, summary)
    manifest = {
        "schema_version": 1,
        "protocol_id": M.PROTOCOL_ID,
        "artifact_role": f"MOCK_{name.upper()}_AGGREGATE_MANIFEST",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "PRODUCER_ONLY",
        "mock_only": True,
        "matrix_id": M.matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_hash,
        "ordered_cell_manifest_root": root,
        "cell_manifests": entries,
        "summary": {
            "path": f"{name}/aggregate_summary.json",
            "sha256": digest(summary_raw),
            "size_bytes": len(summary_raw),
        },
        "scientific_licensing_enabled": False,
        "claim_boundary": M.SCHEDULER_MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    if mock_evaluator is not None:
        manifest["mock_evaluator"] = mock_evaluator
    manifest_raw = write_json(result / name / "aggregate_manifest.json", manifest)
    semantics = M.expected_component_semantics(name, root, mock_evaluator)
    if name == "static":
        diagnostics = semantics["diagnostics"]
    else:
        diagnostics = {
            "archive_transcripts_are_synthetic": True,
            "artifact_status": "MOCK_ONLY_NON_LICENSING",
            "maximum_rslow_sq_upper": "0/1",
            "minimum_margin_sq_lower": "1/625",
            "mock_only": True,
            "ordered_cell_manifest_root": root,
            "production_dispatch_observed": False,
            "scientific_flow_replay_performed": False,
            "synthetic_tube_implication_replay_performed": True,
        }
    checker = {
        "schema_version": 1,
        "protocol_id": M.PROTOCOL_ID,
        "artifact_role": f"{name.upper()}_INDEPENDENT_CHECKER",
        "authority": "INDEPENDENT_CHECKER",
        "checker_status": M.MOCK_CHECKER_STATUS,
        "component_status": None,
        "scientific_licensing_enabled": False,
        "passed": True,
        "matrix_id": M.matrix_id(),
        "main_freeze_sha256": None,
        "run_config_sha256": run_hash,
        "component_aggregate_summary_sha256": digest(summary_raw),
        "component_aggregate_manifest_sha256": digest(manifest_raw),
        "replay_counts": semantics["replay_counts"],
        "cross_precision": semantics["cross_precision"],
        "diagnostics": diagnostics,
        "failures": [],
        "source_bindings": semantics["source_bindings"],
        "claim_boundary": semantics["claim_boundary"],
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    checker_raw = write_json(result / f"independent_{name}_checker.json", checker)
    checker_source = M.STATIC_CHECKER_SOURCE if name == "static" else M.BRANCH_CHECKER_SOURCE
    checker_source_raw = checker_source.read_bytes()
    postcheck = {
        "schema_version": 1,
        "protocol_id": M.PROTOCOL_ID,
        "artifact_role": f"{name.upper()}_POSTCHECK",
        "authority": "POSTCHECK_ONLY",
        "postcheck_status": M.MOCK_POSTCHECK_STATUS,
        "passed": True,
        "checker_path": f"independent_{name}_checker.json",
        "checker_sha256": digest(checker_raw),
        "main_freeze_sha256": None,
        "run_config_sha256": run_hash,
        "bound_artifacts": {
            "aggregate_manifest": {
                "path": f"{name}/aggregate_manifest.json",
                "sha256": digest(manifest_raw),
            },
            "aggregate_summary": {
                "path": f"{name}/aggregate_summary.json",
                "sha256": digest(summary_raw),
            },
            "checker_source": {
                "path": checker_source.relative_to(M.ROOT).as_posix(),
                "sha256": digest(checker_source_raw),
            },
        },
        "replay_counts": semantics["replay_counts"],
        "failures": [],
        "claim_boundary": semantics["postcheck_claim_boundary"],
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    write_json(result / f"{name.upper()}_POSTCHECK_STATUS.json", postcheck)


def complete_fixture(tmp_path: Path) -> Path:
    result = tmp_path / "result"
    result.mkdir()
    _, run_raw = mock_run_config(result)
    run_hash = digest(run_raw)
    make_component(result, "static", run_hash)
    make_component(result, "branch", run_hash)
    static_chain, _, _ = M.validate_component_chain(result, "static", run_hash)
    branch_chain, _, _ = M.validate_component_chain(result, "branch", run_hash)
    summary, manifest = M.expected_composite_controls(
        result, run_hash, static_chain, branch_chain
    )
    write_json(result / "composite_summary.json", summary)
    write_json(result / "composite_manifest.json", manifest)
    return result


def rewrite(path: Path, mutator) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    mutator(payload)
    write_json(path, payload)


def coherently_rebind_component_after_cell_change(
    result: Path, name: str, entry_index: int
) -> dict[str, Any]:
    aggregate_manifest_path = result / name / "aggregate_manifest.json"
    aggregate_summary_path = result / name / "aggregate_summary.json"
    aggregate_manifest = json.loads(aggregate_manifest_path.read_text(encoding="utf-8"))
    entry = aggregate_manifest["cell_manifests"][entry_index]
    changed_manifest = result / entry["path"]
    changed_raw = changed_manifest.read_bytes()
    entry["sha256"] = digest(changed_raw)
    entry["size_bytes"] = len(changed_raw)
    ordered_root = digest(M.canonical_json_bytes(aggregate_manifest["cell_manifests"]))
    aggregate_manifest["ordered_cell_manifest_root"] = ordered_root
    aggregate_summary = json.loads(aggregate_summary_path.read_text(encoding="utf-8"))
    aggregate_summary["ordered_cell_manifest_root"] = ordered_root
    summary_raw = write_json(aggregate_summary_path, aggregate_summary)
    aggregate_manifest["summary"]["sha256"] = digest(summary_raw)
    aggregate_manifest["summary"]["size_bytes"] = len(summary_raw)
    manifest_raw = write_json(aggregate_manifest_path, aggregate_manifest)

    checker_path = result / f"independent_{name}_checker.json"
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    checker["component_aggregate_summary_sha256"] = digest(summary_raw)
    checker["component_aggregate_manifest_sha256"] = digest(manifest_raw)
    checker["diagnostics"]["ordered_cell_manifest_root"] = ordered_root
    checker_raw = write_json(checker_path, checker)
    postcheck_path = result / f"{name.upper()}_POSTCHECK_STATUS.json"
    postcheck = json.loads(postcheck_path.read_text(encoding="utf-8"))
    postcheck["checker_sha256"] = digest(checker_raw)
    postcheck["bound_artifacts"]["aggregate_summary"]["sha256"] = digest(summary_raw)
    postcheck["bound_artifacts"]["aggregate_manifest"]["sha256"] = digest(manifest_raw)
    postcheck_raw = write_json(postcheck_path, postcheck)
    return {
        "aggregate_summary": {
            "path": f"{name}/aggregate_summary.json", "sha256": digest(summary_raw)
        },
        "aggregate_manifest": {
            "path": f"{name}/aggregate_manifest.json", "sha256": digest(manifest_raw)
        },
        "checker": {
            "path": f"independent_{name}_checker.json", "sha256": digest(checker_raw)
        },
        "postcheck": {
            "path": f"{name.upper()}_POSTCHECK_STATUS.json", "sha256": digest(postcheck_raw)
        },
        "ordered_cell_manifest_root": ordered_root,
    }


def current_component_chain(result: Path, name: str) -> dict[str, Any]:
    summary_raw = (result / name / "aggregate_summary.json").read_bytes()
    manifest_raw = (result / name / "aggregate_manifest.json").read_bytes()
    checker_raw = (result / f"independent_{name}_checker.json").read_bytes()
    postcheck_raw = (result / f"{name.upper()}_POSTCHECK_STATUS.json").read_bytes()
    summary = json.loads(summary_raw)
    return {
        "aggregate_summary": {
            "path": f"{name}/aggregate_summary.json", "sha256": digest(summary_raw)
        },
        "aggregate_manifest": {
            "path": f"{name}/aggregate_manifest.json", "sha256": digest(manifest_raw)
        },
        "checker": {
            "path": f"independent_{name}_checker.json", "sha256": digest(checker_raw)
        },
        "postcheck": {
            "path": f"{name.upper()}_POSTCHECK_STATUS.json", "sha256": digest(postcheck_raw)
        },
        "ordered_cell_manifest_root": summary["ordered_cell_manifest_root"],
    }


def test_complete_204_cell_mock_chain_and_postcheck(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    checked = M.run_checker(result)
    assert checked["checker_status"] == M.MOCK_CHECKER_STATUS
    assert checked["replay_counts"] == {
        "static_cells": 102,
        "branch_cells": 102,
        "component_chains": 2,
    }
    assert checked["scientific_licensing_enabled"] is False
    assert checked["component_status"] is None
    assert checked["milestone_status"] is None
    assert checked["theorem_status"] is None
    assert checked["final_status"] is None
    write_json(result / "independent_checker.json", checked)
    postcheck = M.run_postcheck(result)
    assert postcheck["postcheck_status"] == M.MOCK_POSTCHECK_STATUS
    assert postcheck["theorem_status"] is None


def test_manifest_byte_mutation_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "branch/cell_manifests/128/S000.json"
    rewrite(path, lambda payload: payload.__setitem__("evaluator_status", "FORGED"))
    with pytest.raises(M.CompositeCheckError, match="hash mismatch"):
        M.run_checker(result)


def test_coherently_rebound_cell_theorem_status_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    cell_path = result / "static/cell_manifests/128/S000.json"
    rewrite(
        cell_path,
        lambda payload: payload.__setitem__("theorem_status", "PASS_FORGED_CELL_THEOREM"),
    )
    static_chain = coherently_rebind_component_after_cell_change(result, "static", 0)
    run_raw = (result / "run_config.json").read_bytes()
    branch_chain, _, _ = M.validate_component_chain(result, "branch", digest(run_raw))
    summary, manifest = M.expected_composite_controls(
        result, digest(run_raw), static_chain, branch_chain
    )
    write_json(result / "composite_summary.json", summary)
    write_json(result / "composite_manifest.json", manifest)
    with pytest.raises(M.CompositeCheckError, match="unauthorised static cell"):
        M.run_checker(result)


def test_coherently_rebound_payload_theorem_status_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    proof_path = result / "static/cells/128/S000/proof.json"
    rewrite(
        proof_path,
        lambda payload: payload.__setitem__("theorem_status", "PASS_FORGED_PAYLOAD"),
    )
    proof_raw = proof_path.read_bytes()
    manifest_path = result / "static/cell_manifests/128/S000.json"
    rewrite(
        manifest_path,
        lambda payload: payload["files"]["proof.json"].update(
            {"sha256": digest(proof_raw), "size_bytes": len(proof_raw)}
        ),
    )
    static_chain = coherently_rebind_component_after_cell_change(result, "static", 0)
    run_raw = (result / "run_config.json").read_bytes()
    branch_chain, _, _ = M.validate_component_chain(result, "branch", digest(run_raw))
    summary, manifest = M.expected_composite_controls(
        result, digest(run_raw), static_chain, branch_chain
    )
    write_json(result / "composite_summary.json", summary)
    write_json(result / "composite_manifest.json", manifest)
    with pytest.raises(M.CompositeCheckError, match="unauthorised static proof"):
        M.run_checker(result)


def test_component_scientific_status_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "independent_static_checker.json"
    rewrite(path, lambda payload: payload.__setitem__("component_status", "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"))
    checker_raw = path.read_bytes()
    postcheck_path = result / "STATIC_POSTCHECK_STATUS.json"
    rewrite(postcheck_path, lambda payload: payload.__setitem__("checker_sha256", digest(checker_raw)))
    with pytest.raises(M.CompositeCheckError, match="unauthorised"):
        M.run_checker(result)


def test_coherently_rebound_negative_branch_margin_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    checker_path = result / "independent_branch_checker.json"
    rewrite(
        checker_path,
        lambda payload: payload["diagnostics"].__setitem__(
            "minimum_margin_sq_lower", "-999/1"
        ),
    )
    checker_raw = checker_path.read_bytes()
    rewrite(
        result / "BRANCH_POSTCHECK_STATUS.json",
        lambda payload: payload.__setitem__("checker_sha256", digest(checker_raw)),
    )
    run_raw = (result / "run_config.json").read_bytes()
    summary, manifest = M.expected_composite_controls(
        result,
        digest(run_raw),
        current_component_chain(result, "static"),
        current_component_chain(result, "branch"),
    )
    write_json(result / "composite_summary.json", summary)
    write_json(result / "composite_manifest.json", manifest)
    with pytest.raises(M.CompositeCheckError, match="branch checker diagnostics"):
        M.run_checker(result)


def test_float_precision_alias_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "static/aggregate_manifest.json"
    rewrite(path, lambda payload: payload["cell_manifests"][0]["cell"].__setitem__("precision_bits", 128.0))
    with pytest.raises(M.CompositeCheckError, match="order mismatch"):
        M.run_checker(result)


def test_noncanonical_json_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "branch/aggregate_summary.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    with pytest.raises(M.StrictJSONError, match="not canonical"):
        M.run_checker(result)


def test_duplicate_json_key_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "composite_summary.json"
    path.write_text('{"schema_version":1,"schema_version":1}\n', encoding="utf-8")
    with pytest.raises(M.StrictJSONError, match="duplicate"):
        M.run_checker(result)


def test_symlinked_cell_manifest_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "static/cell_manifests/128/S001.json"
    target = result / "saved.json"
    path.rename(target)
    path.symlink_to(target)
    with pytest.raises((M.PathContractError, OSError)):
        M.run_checker(result)


def test_formal_or_nominally_licensed_run_config_stays_fail_closed(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "run_config.json"
    rewrite(path, lambda payload: payload.__setitem__("mock_only", False))
    with pytest.raises(M.CompositeCheckError, match="mock"):
        M.run_checker(result)


def test_write_once_refuses_overwrite(tmp_path: Path) -> None:
    path = tmp_path / "checker.json"
    M.write_once(path, b"{}\n")
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        M.write_once(path, b'{"changed":true}\n')
    assert path.read_bytes() == before


def test_composite_generation_binding_mutation_is_rejected(tmp_path: Path) -> None:
    result = complete_fixture(tmp_path)
    path = result / "composite_manifest.json"
    rewrite(path, lambda payload: payload.__setitem__("archive_generation_sha256", "0" * 64))
    with pytest.raises(M.CompositeCheckError, match="manifest mismatch"):
        M.run_checker(result)
