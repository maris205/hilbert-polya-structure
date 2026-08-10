from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
BUILDER_SOURCE = ROOT / "scripts/build_r401_val_l3_a1_release_provenance.py"
COMPOSITE_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_composite_independent.py"
COMPOSITE_TEST_SOURCE = ROOT / "tests/test_r401_val_l3_a1_composite_contract.py"


def load(path: Path, name: str):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


R = load(BUILDER_SOURCE, "l3_a1_release")
C = load(COMPOSITE_SOURCE, "l3_a1_composite_for_release")
CT = load(COMPOSITE_TEST_SOURCE, "l3_a1_composite_fixture")


def write_json(path: Path, payload: Any) -> bytes:
    raw = R.canonical_json_bytes(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return raw


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def build_result(project: Path) -> Path:
    result = project / R.RESULT_RELATIVE
    result.mkdir(parents=True)
    _, run_raw = CT.mock_run_config(result)
    run_hash = sha(run_raw)
    CT.make_component(result, "static", run_hash)
    CT.make_component(result, "branch", run_hash)
    static_chain, _, _ = C.validate_component_chain(result, "static", run_hash)
    branch_chain, _, _ = C.validate_component_chain(result, "branch", run_hash)
    summary, manifest = C.expected_composite_controls(
        result, run_hash, static_chain, branch_chain
    )
    CT.write_json(result / "composite_summary.json", summary)
    CT.write_json(result / "composite_manifest.json", manifest)
    checker = C.run_checker(result)
    CT.write_json(result / "independent_checker.json", checker)
    postcheck = C.run_postcheck(result)
    CT.write_json(result / "POSTCHECK_STATUS.json", postcheck)
    report = (
        "Status: PASS_MOCK_PROVENANCE_REPLAY\n"
        "milestone_status = null\n"
        "theorem_status = null\n"
        "final_status = null\n"
        f"Claim boundary: {R.MOCK_CLAIM_BOUNDARY}\n"
    )
    (result / "R401_VAL_L3_A1_REPORT.md").write_text(report, encoding="utf-8")
    return result


def populate_inputs(project: Path) -> None:
    for role, relative in R.INPUT_ROLES:
        path = project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        source = ROOT / relative
        if source.is_file():
            path.write_bytes(source.read_bytes())
        elif relative.endswith(".json"):
            write_json(path, {"role": role, "mock_only": True})
        elif role == "branch_evaluator_binary":
            path.write_bytes(b"MOCK BINARY - NEVER EXECUTED\n")
        else:
            path.write_text(f"mock input role: {role}\n", encoding="utf-8")


def publish_mock_freeze(project: Path) -> dict[str, Any]:
    input_roles = [R.role_binding(project, role, relative) for role, relative in R.INPUT_ROLES]
    machine_hash = next(item["sha256"] for item in input_roles if item["role"] == "machine_freeze")
    payload = {
        "schema_version": 1,
        "protocol_id": R.PROTOCOL_ID,
        "artifact_role": "MOCK_MAIN_FREEZE",
        "artifact_status": "MOCK_ONLY_NON_LICENSING",
        "authority": "ENGINEERING_TEST_ONLY",
        "mock_only": True,
        "scientific_licensing_enabled": False,
        "matrix": R.matrix_payload(),
        "matrix_id": R.matrix_id(),
        "machine_freeze_sha256": machine_hash,
        "input_roles": input_roles,
        "claim_boundary": R.MOCK_CLAIM_BOUNDARY,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    write_json(project / R.MAIN_FREEZE_RELATIVE, payload)
    return payload


def release_fixture(tmp_path: Path) -> Path:
    project = tmp_path / "project"
    project.mkdir()
    populate_inputs(project)
    build_result(project)
    publish_mock_freeze(project)
    return project


def rewrite(path: Path, mutator) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    mutator(payload)
    write_json(path, payload)


def test_build_and_verify_exact_68_role_mock_release(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    released = R.build_release(project)
    assert released["release_status"] == R.MOCK_RELEASE_STATUS
    assert released["scientific_licensing_enabled"] is False
    assert released["milestone_status"] is None
    assert released["theorem_status"] is None
    assert released["final_status"] is None
    assert len(released["roles"]) == 68
    assert [item["role"] for item in released["roles"]] == [
        *[role for role, _ in R.INPUT_ROLES],
        "main_freeze",
        *[role for role, _ in R.DOWNSTREAM_ROLES],
    ]
    before = (project / R.RESULT_RELATIVE / R.RELEASE_NAME).read_bytes()
    verified = R.verify_release(project)
    assert verified == released
    assert (project / R.RESULT_RELATIVE / R.RELEASE_NAME).read_bytes() == before


def test_identical_build_is_idempotent(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    first = R.build_release(project)
    path = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    before = (path.read_bytes(), path.stat().st_mtime_ns)
    second = R.build_release(project)
    assert second == first
    assert (path.read_bytes(), path.stat().st_mtime_ns) == before


def test_missing_main_freeze_input_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    (project / R.INPUT_ROLES[0][1]).unlink()
    with pytest.raises((R.ReleaseError, FileNotFoundError)):
        R.build_expected_release(project)


def test_changed_input_after_freeze_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.INPUT_ROLES[5][1]
    path.write_text("changed after mock freeze\n", encoding="utf-8")
    with pytest.raises(R.ReleaseError, match="53-role"):
        R.build_expected_release(project)


def test_downstream_manifest_mutation_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "branch/cell_manifests/128/S000.json"
    rewrite(path, lambda payload: payload.__setitem__("evaluator_status", "FORGED"))
    with pytest.raises(R.ReleaseError, match="canonical|hash mismatch|key set"):
        R.build_expected_release(project)


def test_nominal_formal_freeze_is_fail_closed(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.MAIN_FREEZE_RELATIVE
    rewrite(path, lambda payload: payload.__setitem__("mock_only", False))
    with pytest.raises(R.ReleaseError, match="not implemented"):
        R.build_expected_release(project)


def test_report_authority_mutation_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "R401_VAL_L3_A1_REPORT.md"
    path.write_text(path.read_text(encoding="utf-8") + "theorem_status = PASS\n", encoding="utf-8")
    with pytest.raises(R.ReleaseError, match="authority block"):
        R.build_expected_release(project)


def test_duplicate_key_in_json_role_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / "research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
    path.write_text('{"x":1,"x":2}\n', encoding="utf-8")
    with pytest.raises(R.StrictJSONError, match="duplicate"):
        R.build_expected_release(project)


def test_symlinked_input_role_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.INPUT_ROLES[0][1]
    saved = project / "saved.md"
    path.rename(saved)
    path.symlink_to(saved)
    with pytest.raises((R.PathContractError, OSError)):
        R.build_expected_release(project)


def test_different_existing_release_is_never_overwritten(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    path.write_bytes(b'{"foreign":true}\n')
    before = path.read_bytes()
    with pytest.raises(R.ReleaseError, match="different release"):
        R.build_release(project)
    assert path.read_bytes() == before


def test_verify_only_rejects_noncanonical_release_bytes(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    released = R.build_release(project)
    path = project / R.RESULT_RELATIVE / R.RELEASE_NAME
    path.write_text(json.dumps(released, indent=2) + "\n", encoding="utf-8")
    with pytest.raises(R.StrictJSONError, match="not canonical"):
        R.verify_release(project)


def test_composite_checker_claim_mutation_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    result = project / R.RESULT_RELATIVE
    checker_path = result / "independent_checker.json"
    rewrite(
        checker_path,
        lambda payload: payload.__setitem__("claim_boundary", "FORGED THEOREM AUTHORITY"),
    )
    checker_hash = sha(checker_path.read_bytes())
    rewrite(
        result / "POSTCHECK_STATUS.json",
        lambda payload: payload.__setitem__("checker_sha256", checker_hash),
    )
    with pytest.raises(R.ReleaseError, match="composite checker authority"):
        R.build_expected_release(project)


def test_nested_composite_postcheck_authority_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "POSTCHECK_STATUS.json"
    rewrite(
        path,
        lambda payload: payload["bound_artifacts"].__setitem__(
            "theorem_status", "RH_PROVED"
        ),
    )
    with pytest.raises(R.ReleaseError, match="nested authority|artifact bindings"):
        R.build_expected_release(project)


def test_frozen_release_builder_must_match_executing_source(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    (project / "scripts/build_r401_val_l3_a1_release_provenance.py").write_text(
        "# coherent but foreign release builder\n", encoding="utf-8"
    )
    publish_mock_freeze(project)
    with pytest.raises(R.ReleaseError, match="executing source"):
        R.build_expected_release(project)


def test_frozen_protocol_must_match_checker_source_binding(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    (project / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md").write_text(
        "FORGED ALTERNATE PROTOCOL\n", encoding="utf-8"
    )
    publish_mock_freeze(project)
    with pytest.raises(R.ReleaseError, match="executing source"):
        R.build_expected_release(project)


def test_hidden_component_authority_file_is_rejected(tmp_path: Path) -> None:
    project = release_fixture(tmp_path)
    path = project / R.RESULT_RELATIVE / "static/.hidden-authority.json"
    write_json(path, {"theorem_status": "FORGED"})
    with pytest.raises(R.PathContractError, match="namespace mismatch"):
        R.build_expected_release(project)


def test_late_authoritative_extra_prevents_success(tmp_path: Path, monkeypatch) -> None:
    project = release_fixture(tmp_path)
    original = R.write_once

    def publish_then_add_extra(path: Path, raw: bytes) -> None:
        original(path, raw)
        (path.parent / ".late-authority-extra").write_text(
            "late extra\n", encoding="utf-8"
        )

    monkeypatch.setattr(R, "write_once", publish_then_add_extra)
    with pytest.raises(R.PathContractError, match="namespace mismatch"):
        R.build_release(project)


def test_release_source_has_no_component_imports() -> None:
    text = BUILDER_SOURCE.read_text(encoding="utf-8")
    assert "import run_r401" not in text
    assert "import check_r401" not in text
    assert "subprocess" not in text
