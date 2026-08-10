from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import types
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/run_r401_val_l3_a1_all_slabs.py"
BRANCH_RUNTIME = ROOT / "scripts/r401_val_l3_a1_branch_runtime.py"
PREFREEZE_DESIGN = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_DESIGN.md"
)
SCHEDULER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md"
)
PROTOCOL = ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md"
CHECKER_CONTRACT = (
    ROOT / "research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md"
)
RELEASE_CONTRACT = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md"
)
SPEC = importlib.util.spec_from_file_location("r401_val_l3_a1_scheduler", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def roots(tmp_path: Path) -> tuple[Path, Path]:
    output = tmp_path / "mock-generation"
    return output, MODULE.operational_root_for(output)


def initialize(tmp_path: Path) -> tuple[Path, Path, dict[str, object], str]:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    _, config_hash = MODULE.ensure_run_config(output, binding, resume=False)
    operational.mkdir()
    return output, operational, binding, config_hash


def write_canonical_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(MODULE.canonical_json_bytes(payload))


def formal_authority_fixture(tmp_path: Path) -> Path:
    authority = (tmp_path / "formal-authority").absolute()
    authority.mkdir(parents=True)
    for role, relative in MODULE.FORMAL_INPUT_ROLES:
        target = authority / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        source = ROOT / relative
        if source.is_file():
            shutil.copy2(source, target)
        elif relative.endswith(".json"):
            write_canonical_json(target, {"fixture_role": role})
        else:
            target.write_text(f"formal fixture role: {role}\n", encoding="utf-8")

    machine = authority / dict(MODULE.FORMAL_INPUT_ROLES)["machine_freeze"]
    write_canonical_json(
        machine,
        {
            "schema_version": 1,
            "protocol_id": MODULE.PROTOCOL_ID,
            "artifact_role": "MACHINE_FREEZE",
            "status": "FROZEN_FOR_PRODUCTION",
            "scientific_licensing_enabled": True,
            "component_status": None,
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
        },
    )
    review = authority / dict(MODULE.FORMAL_INPUT_ROLES)["prefreeze_review"]
    review.write_text(
        "Independent implementation fixture review\n"
        f"{MODULE.PREFREEZE_ACCEPT_LINE}\n",
        encoding="utf-8",
    )
    binary = authority / dict(MODULE.FORMAL_INPUT_ROLES)["branch_evaluator_binary"]
    binary.chmod(binary.stat().st_mode | 0o755)

    role_records = [
        MODULE.formal_role_binding(authority, role, relative)[0]
        for role, relative in MODULE.FORMAL_INPUT_ROLES
    ]
    roles = [item.payload() for item in role_records]
    machine_hash = next(
        item.sha256 for item in role_records if item.role == "machine_freeze"
    )
    freeze = {
        "schema_version": 1,
        "protocol_id": MODULE.PROTOCOL_ID,
        "artifact_role": "MAIN_FREEZE",
        "status": "FROZEN_FOR_PRODUCTION",
        "authority": "INDEPENDENT_PREFREEZE_REVIEW",
        "scientific_licensing_enabled": True,
        "matrix": MODULE.matrix_payload(),
        "matrix_id": MODULE.canonical_matrix_id(),
        "machine_freeze_sha256": machine_hash,
        "input_roles": roles,
        "claim_boundary": "formal fixture envelope; no evaluator dispatch",
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    write_canonical_json(
        authority / "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json",
        freeze,
    )
    return authority


def test_exact_matrix_and_matrix_id_are_canonical() -> None:
    matrix = MODULE.exact_matrix()
    assert len(matrix) == len(set(matrix)) == 102
    assert matrix == tuple(
        MODULE.CellKey(bits, f"S{index:03d}")
        for bits in (128, 256)
        for index in range(51)
    )
    assert matrix[0].label == "128:S000"
    assert matrix[50].label == "128:S050"
    assert matrix[51].label == "256:S000"
    assert matrix[-1].label == "256:S050"
    assert MODULE.canonical_matrix_id() == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(MODULE.matrix_payload())
    )
    assert len(MODULE.canonical_matrix_id()) == 64


@pytest.mark.parametrize(
    "raw",
    [
        '{"x":1,"x":1}',
        '{"x":NaN}',
        '{"x":Infinity}',
        '{"x":1e9999}',
    ],
)
def test_strict_json_rejects_duplicate_and_nonfinite_values(raw: str) -> None:
    with pytest.raises(MODULE.StrictJSONError):
        MODULE.strict_json_loads(raw)


def test_exact_json_equality_rejects_boolean_and_integral_float_aliases() -> None:
    assert not MODULE.exact_json_equal({"x": True}, {"x": 1})
    assert not MODULE.exact_json_equal({"x": 1.0}, {"x": 1})
    assert MODULE.exact_json_equal({"x": [1, None]}, {"x": [1, None]})


@pytest.mark.parametrize(
    "value",
    ["", "/absolute", "../escape", "a/../b", "./a", "a//b", "a\\b", "a/"],
)
def test_safe_relative_path_rejects_aliases(value: str) -> None:
    with pytest.raises(MODULE.PathContractError):
        MODULE.safe_relative_path(value)


def test_symlink_and_hardlink_controls_are_rejected(tmp_path: Path) -> None:
    target = tmp_path / "target.json"
    target.write_text("{}\n", encoding="utf-8")
    link = tmp_path / "link.json"
    link.symlink_to(target)
    with pytest.raises(MODULE.PathContractError):
        MODULE.strict_json_load(link)

    alias = tmp_path / "alias.json"
    os.link(target, alias)
    with pytest.raises(MODULE.PathContractError, match="hard-link"):
        MODULE.strict_json_load(target)


def test_staging_and_interrupted_names_are_exact() -> None:
    run_config_sha256 = "a" * 64
    for cell in MODULE.exact_matrix():
        name = MODULE.staging_basename(cell, run_config_sha256)
        assert MODULE.STAGING_BASENAME.fullmatch(name)
        assert name == f".{cell.slab_id}.tmp-aaaaaaaaaaaaaaaa-0"
    for invalid in (
        ".S051.tmp-aaaaaaaaaaaaaaaa-0",
        "S000.tmp-aaaaaaaaaaaaaaaa-0",
        ".S000.tmp-AAAAAAAAAAAAAAAA-0",
        ".S000.tmp-aaaaaaaaaaaaaaaa-00",
        ".S000.tmp-aaaaaaaaaaaaaaa-0",
        ".S000.tmp-aaaaaaaaaaaaaaaa-0.extra",
    ):
        assert MODULE.STAGING_BASENAME.fullmatch(invalid) is None
    with pytest.raises(MODULE.PathContractError):
        MODULE.staging_basename(MODULE.CellKey(128, "S000"), "a" * 63)


def test_static_and_branch_staging_namespace_matches_reviewed_design() -> None:
    template = ".{slab_id}.tmp-{generation_prefix_16hex}-{attempt_decimal}"
    assert template in PREFREEZE_DESIGN.read_text(encoding="utf-8")
    assert template in SCHEDULER_CONTRACT.read_text(encoding="utf-8")
    runtime_source = BRANCH_RUNTIME.read_text(encoding="utf-8")
    assert 'f".{task.slab_id}.tmp-{generation_prefix}-{attempt}"' in runtime_source
    cell = MODULE.CellKey(128, "S000")
    assert MODULE.staging_path(Path("/tmp/operational"), cell, "b" * 64, 7) == Path(
        "/tmp/operational/staging/static/128/.S000.tmp-bbbbbbbbbbbbbbbb-7"
    )


def test_candidate_role_map_counts_and_new_direct_bindings_are_consistent() -> None:
    release_text = RELEASE_CONTRACT.read_text(encoding="utf-8")
    input_section = release_text.split(
        "## 2. Exact 53-role main-freeze input map candidate", 1
    )[1].split("## 3. Main freeze edge", 1)[0]
    input_rows = re.findall(r"^\| (\d+) \| `([^`]+)` \| `([^`]+)` \|$", input_section, re.M)
    assert [int(index) for index, _role, _path in input_rows] == list(range(1, 54))
    roles = [role for _index, role, _path in input_rows]
    paths = [path for _index, _role, path in input_rows]
    assert len(roles) == len(set(roles)) == 53
    assert len(paths) == len(set(paths)) == 53
    direct_bindings = {
        "implementation_design_review": (
            "research/route_a_wave_trace/R401_VAL_L3_A1_DESIGN_REVIEW.md"
        ),
        "branch_runtime": "scripts/r401_val_l3_a1_branch_runtime.py",
        "test_static_evaluator": "tests/test_r401_val_l3_a1_static_cell.py",
        "test_s0_compatibility": "tests/test_r401_val_l3_a1_s0_compatibility.py",
    }
    table = {role: path for _index, role, path in input_rows}
    assert {role: table[role] for role in direct_bindings} == direct_bindings
    assert all((ROOT / path).is_file() for path in direct_bindings.values())

    release_section = release_text.split(
        "## 4. Exact 68-role release map candidate", 1
    )[1].split("## 5. Candidate exact release schema", 1)[0]
    release_rows = re.findall(
        r"^\| (\d+) \| `([^`]+)` \| `([^`]+)` \|$", release_section, re.M
    )
    assert [int(index) for index, _role, _path in release_rows] == list(range(55, 69))
    for path in (PROTOCOL, SCHEDULER_CONTRACT, CHECKER_CONTRACT, RELEASE_CONTRACT):
        text = path.read_text(encoding="utf-8")
        assert "53" in text and "68" in text


def test_mock_binding_is_sealed_nonlicensing_and_type_strict(tmp_path: Path) -> None:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    MODULE.validate_mock_binding(binding)
    assert binding["matrix_id"] == MODULE.canonical_matrix_id()
    assert binding["mock_only"] is True
    assert binding["production_authorized"] is False
    assert binding["scientific_licensing_enabled"] is False
    assert binding["main_freeze"] == {"path": None, "sha256": None}
    assert binding["milestone_status"] is None
    assert binding["theorem_status"] is None
    assert binding["final_status"] is None

    forged = dict(binding)
    forged["schema_version"] = True
    with pytest.raises(MODULE.StrictJSONError):
        MODULE.validate_mock_binding(forged)

    forged = json.loads(json.dumps(binding))
    forged["paths"]["extra"] = "/tmp/forged"
    with pytest.raises(MODULE.StrictJSONError, match="key set mismatch"):
        MODULE.validate_mock_binding(forged)

    forged = json.loads(json.dumps(binding))
    forged["paths"]["operational_root"] = 7
    with pytest.raises(MODULE.PathContractError):
        MODULE.validate_mock_binding(forged)

    forged = json.loads(json.dumps(binding))
    forged["limits"]["static"]["workers"] = 7
    with pytest.raises(MODULE.StrictJSONError, match="resource limits"):
        MODULE.validate_mock_binding(forged)


def test_run_config_is_write_once_and_resume_is_exact(tmp_path: Path) -> None:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    stored, first_hash = MODULE.ensure_run_config(output, binding, resume=False)
    before = MODULE.run_config_path(output).read_bytes()
    resumed, second_hash = MODULE.ensure_run_config(output, binding, resume=True)
    assert MODULE.exact_json_equal(stored, resumed)
    assert first_hash == second_hash
    assert MODULE.run_config_path(output).read_bytes() == before

    changed = json.loads(json.dumps(binding))
    changed["limits"]["static"]["workers"] = 7
    with pytest.raises(MODULE.StrictJSONError, match="resource limits"):
        MODULE.ensure_run_config(output, changed, resume=True)


def test_run_config_resume_rejects_semantically_equal_noncanonical_bytes(
    tmp_path: Path,
) -> None:
    output, operational = roots(tmp_path)
    binding = MODULE.build_mock_binding(output, operational)
    MODULE.ensure_run_config(output, binding, resume=False)
    target = MODULE.run_config_path(output)
    noncanonical = (json.dumps(binding, indent=2, sort_keys=False) + "\n").encode()
    assert noncanonical != MODULE.canonical_json_bytes(binding)
    target.write_bytes(noncanonical)
    before = target.read_bytes()
    with pytest.raises(MODULE.StrictJSONError, match="noncanonical JSON bytes"):
        MODULE.ensure_run_config(output, binding, resume=True)
    assert target.read_bytes() == before


def test_atomic_static_cell_and_manifest_contract(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S000")
    state, manifest = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "COMMITTED"
    directory = MODULE.static_cell_path(output, cell)
    assert {path.name for path in directory.iterdir()} == {"proof.json", "record.json"}
    assert not MODULE.staging_path(operational, cell, config_hash).exists()
    assert MODULE.static_manifest_path(output, cell).is_file()
    record = MODULE.strict_json_load(directory / "record.json")
    assert set(record) == {
        "schema_version",
        "protocol_id",
        "artifact_role",
        "artifact_status",
        "authority",
        "mock_only",
        "cell",
        "matrix_id",
        "main_freeze_sha256",
        "run_config_sha256",
        "scheduler_classification",
        "evaluator_status",
        "returncode",
        "evaluator_payload",
        "scientific_licensing_enabled",
        "claim_boundary",
        "component_status",
        "milestone_status",
        "theorem_status",
        "final_status",
    }
    assert record["main_freeze_sha256"] is None
    assert record["evaluator_payload"] == {
        "path": "proof.json",
        "sha256": MODULE.sha256(directory / "proof.json"),
        "size_bytes": (directory / "proof.json").stat().st_size,
    }
    assert set(manifest) == {
        "schema_version",
        "protocol_id",
        "artifact_role",
        "artifact_status",
        "authority",
        "mock_only",
        "cell",
        "matrix_id",
        "main_freeze_sha256",
        "run_config_sha256",
        "scheduler_classification",
        "evaluator_status",
        "files",
        "scientific_licensing_enabled",
        "claim_boundary",
        "component_status",
        "milestone_status",
        "theorem_status",
        "final_status",
    }
    assert manifest["main_freeze_sha256"] is None
    assert manifest["component_status"] is None
    assert manifest["milestone_status"] is None
    assert manifest["theorem_status"] is None
    assert manifest["final_status"] is None
    checked = MODULE.validate_static_manifest(
        output, cell, binding["matrix_id"], config_hash
    )
    assert MODULE.exact_json_equal(manifest, checked)


def test_committed_cell_resume_is_read_only(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(256, "S050")
    MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    directory = MODULE.static_cell_path(output, cell)
    manifest_path = MODULE.static_manifest_path(output, cell)
    before = {
        "proof": (directory / "proof.json").read_bytes(),
        "record": (directory / "record.json").read_bytes(),
        "manifest": manifest_path.read_bytes(),
    }
    state, _ = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "RESUMED_COMMITTED"
    assert (directory / "proof.json").read_bytes() == before["proof"]
    assert (directory / "record.json").read_bytes() == before["record"]
    assert manifest_path.read_bytes() == before["manifest"]


def test_manifestless_crash_recovers_without_rewriting_cell(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S025")
    with pytest.raises(MODULE.SyntheticCrash):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            cell,
            binding["matrix_id"],
            config_hash,
            fail_after_cell_rename=True,
        )
    directory = MODULE.static_cell_path(output, cell)
    assert directory.is_dir()
    assert not MODULE.static_manifest_path(output, cell).exists()
    proof_before = (directory / "proof.json").read_bytes()
    record_before = (directory / "record.json").read_bytes()

    state, manifest = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "RECOVERED_MANIFEST"
    assert manifest["mock_only"] is True
    assert (directory / "proof.json").read_bytes() == proof_before
    assert (directory / "record.json").read_bytes() == record_before


def test_corrupt_manifestless_cell_fails_without_overwrite(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S001")
    with pytest.raises(MODULE.SyntheticCrash):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            cell,
            binding["matrix_id"],
            config_hash,
            fail_after_cell_rename=True,
        )
    proof = MODULE.static_cell_path(output, cell) / "proof.json"
    proof.write_text('{"corrupt":true}\n', encoding="utf-8")
    corrupt = proof.read_bytes()
    with pytest.raises(MODULE.CorruptGeneration):
        MODULE.commit_mock_static_cell(
            output, operational, cell, binding["matrix_id"], config_hash
        )
    assert proof.read_bytes() == corrupt
    assert not MODULE.static_manifest_path(output, cell).exists()


def test_live_complete_staging_is_published_on_resume(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(256, "S002")
    stage = MODULE.staging_path(operational, cell, config_hash)
    MODULE.write_mock_stage(stage, cell, binding["matrix_id"], config_hash)
    assert stage.is_dir()
    state, _ = MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    assert state == "COMMITTED"
    assert not stage.exists()
    assert MODULE.static_manifest_path(output, cell).is_file()


def test_static_staging_scan_rejects_hidden_foreign_and_duplicate_owners(
    tmp_path: Path,
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    precision_root = operational / "staging/static/128"
    precision_root.mkdir(parents=True)
    invalid = precision_root / ".unexpected"
    invalid.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="invalid static staging"):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            MODULE.CellKey(128, "S000"),
            binding["matrix_id"],
            config_hash,
        )
    invalid.rmdir()

    foreign = precision_root / ".S000.tmp-ffffffffffffffff-0"
    foreign.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="foreign-generation"):
        MODULE.validate_static_staging_namespace(operational, config_hash)
    foreign.rmdir()

    first = precision_root / f".S000.tmp-{config_hash[:16]}-0"
    second = precision_root / f".S000.tmp-{config_hash[:16]}-1"
    second.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="noncanonical active"):
        MODULE.commit_mock_static_cell(
            output,
            operational,
            MODULE.CellKey(128, "S000"),
            binding["matrix_id"],
            config_hash,
        )
    second.rmdir()
    first.mkdir()
    second.mkdir()
    with pytest.raises(MODULE.CorruptGeneration, match="multiple active"):
        MODULE.validate_static_staging_namespace(operational, config_hash)


def test_cell_rename_flushes_staging_then_canonical_parent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S003")
    stage = MODULE.staging_path(operational, cell, config_hash)
    target = MODULE.static_cell_path(output, cell)
    events: list[tuple[str, Path, Path | None]] = []
    original_rename = MODULE.rename_directory_noreplace
    original_fsync = MODULE.fsync_directory

    def tracked_rename(source: Path, destination: Path) -> None:
        events.append(("rename", Path(source), Path(destination)))
        original_rename(source, destination)

    def tracked_fsync(path: Path) -> None:
        events.append(("fsync", Path(path), None))
        original_fsync(path)

    monkeypatch.setattr(MODULE, "rename_directory_noreplace", tracked_rename)
    monkeypatch.setattr(MODULE, "fsync_directory", tracked_fsync)
    MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    rename_index = events.index(("rename", stage, target))
    assert events[rename_index + 1] == ("fsync", stage.parent, None)
    assert events[rename_index + 2] == ("fsync", target.parent, None)


def test_whole_generation_quarantine_preserves_authoritative_and_operational(
    tmp_path: Path,
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    cell = MODULE.CellKey(128, "S000")
    MODULE.commit_mock_static_cell(
        output, operational, cell, binding["matrix_id"], config_hash
    )
    marker = operational / "telemetry.txt"
    marker.write_text("preserve me\n", encoding="utf-8")
    q_output, q_operational = MODULE.quarantine_incompatible_generation(
        output, "RUN_CONFIG_BINDING_MISMATCH"
    )
    assert not output.exists()
    assert not operational.exists()
    assert (q_output / "run_config.json").is_file()
    assert (q_output / "QUARANTINE_RECORD.json").is_file()
    assert q_operational is not None
    assert (q_operational / "telemetry.txt").read_text(encoding="utf-8") == "preserve me\n"
    record = MODULE.strict_json_load(q_output / "QUARANTINE_RECORD.json")
    assert record["reason"] == "RUN_CONFIG_BINDING_MISMATCH"
    assert record["operational_present"] is True
    assert MODULE.HEX_SHA256.fullmatch(record["transaction_journal_sha256"])
    assert record["milestone_status"] is None
    assert record["final_status"] is None
    assert not MODULE.quarantine_journal_path(output).exists()


@pytest.mark.parametrize("failure_point", sorted(MODULE.QUARANTINE_FAILURE_POINTS))
def test_quarantine_journal_recovers_every_durable_boundary(
    tmp_path: Path, failure_point: str
) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    MODULE.commit_mock_static_cell(
        output,
        operational,
        MODULE.CellKey(128, "S000"),
        binding["matrix_id"],
        config_hash,
    )
    marker = operational / "telemetry.txt"
    marker.write_text("recoverable\n", encoding="utf-8")
    with pytest.raises(MODULE.SyntheticQuarantineCrash):
        MODULE.quarantine_incompatible_generation(
            output,
            "BOUNDARY_TEST",
            fail_at=failure_point,
        )
    journal = MODULE.quarantine_journal_path(output)
    assert journal.is_file()
    q_output, q_operational = MODULE.recover_quarantine_transaction(output)
    assert not output.exists()
    assert not operational.exists()
    assert not journal.exists()
    assert q_operational is not None
    assert (q_output / "run_config.json").is_file()
    assert (q_output / "QUARANTINE_RECORD.json").is_file()
    assert (q_operational / "telemetry.txt").read_text(encoding="utf-8") == "recoverable\n"


def test_mock_resume_completes_pending_quarantine_then_fails_closed(
    tmp_path: Path,
) -> None:
    output, operational, _binding, _config_hash = initialize(tmp_path)
    with pytest.raises(MODULE.SyntheticQuarantineCrash):
        MODULE.quarantine_incompatible_generation(
            output,
            "RESUME_RECOVERY_TEST",
            fail_at="AFTER_AUTHORITATIVE_RENAME",
        )
    with pytest.raises(MODULE.RunBindingMismatch, match="quarantined generation"):
        MODULE.run_mock_static(output, 0, resume=True)
    q_output, q_operational = MODULE.quarantine_paths(output, 1)
    assert q_output.is_dir()
    assert q_operational.is_dir()
    assert (q_output / "QUARANTINE_RECORD.json").is_file()
    assert not MODULE.quarantine_journal_path(output).exists()


def test_mock_output_cannot_use_canonical_production_namespace() -> None:
    for path in (
        MODULE.CANONICAL_RESULT,
        MODULE.CANONICAL_RESULT / "child",
        MODULE.CANONICAL_OPERATIONAL,
        MODULE.CANONICAL_OPERATIONAL / "child",
    ):
        with pytest.raises(MODULE.PathContractError):
            MODULE.ensure_mock_output_allowed(path)


def test_production_and_initialize_only_fail_before_output_creation(tmp_path: Path) -> None:
    for mode in ("--production", "--initialize-only"):
        output = tmp_path / mode.removeprefix("--")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), mode, "--output", str(output)],
            text=True,
            capture_output=True,
            check=False,
        )
        assert completed.returncode == 1
        assert "production rejected" in completed.stderr
        assert not output.exists()


def test_formal_authority_exact_53_role_handshake_and_initialize_only(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-preflight-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    assert len(snapshot.input_roles) == 53
    assert tuple(item.role for item in snapshot.input_roles) == tuple(
        role for role, _ in MODULE.FORMAL_INPUT_ROLES
    )
    assert snapshot.main_freeze_sha256 == MODULE.sha256(snapshot.main_freeze_path)

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--initialize-only",
            "--authority-root",
            str(authority),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["artifact_status"] == "FORMAL_PREFLIGHT_ONLY"
    assert result["input_role_count"] == 53
    assert result["freeze_sha256"] == result["main_freeze_sha256"]
    assert result["production_authorized"] is False
    assert result["scientific_licensing_enabled"] is False
    assert {path.name for path in output.iterdir()} == {"run_config.json"}
    config = MODULE.strict_json_load(output / "run_config.json", require_canonical=True)
    assert config["preflight_only"] is True
    assert config["promotable"] is False
    assert config["production_authorized"] is False
    assert config["scientific_licensing_enabled"] is False
    assert config["freeze_sha256"] == config["main_freeze_sha256"]
    assert config["component_status"] is None
    assert not MODULE.operational_root_for(output).exists()


def test_formal_preflight_cannot_resume_promote_or_use_canonical_root(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-preflight-once").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    config, _ = MODULE.initialize_formal_preflight(snapshot, output)
    before = (output / "run_config.json").read_bytes()
    with pytest.raises(MODULE.RunBindingMismatch, match="cannot be resumed or promoted"):
        MODULE.initialize_formal_preflight(snapshot, output)
    assert (output / "run_config.json").read_bytes() == before
    promoted = dict(config)
    promoted["production_authorized"] = True
    with pytest.raises(MODULE.ProductionAuthorityError):
        MODULE.validate_formal_preflight_binding(promoted, snapshot, output)
    with pytest.raises(MODULE.PathContractError, match="canonical production"):
        MODULE.initialize_formal_preflight(snapshot, MODULE.CANONICAL_RESULT)

    rejected = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--production",
            "--execute-scientific-dispatch",
            "--authority-root",
            str(authority),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert rejected.returncode == 1
    assert "unconditionally disabled" in rejected.stderr
    assert (output / "run_config.json").read_bytes() == before


def test_formal_authority_rejects_role_reorder_and_decorated_review(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    freeze_path = authority / "research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json"
    freeze = MODULE.strict_json_load(freeze_path, require_canonical=True)
    freeze["input_roles"][0], freeze["input_roles"][1] = (
        freeze["input_roles"][1], freeze["input_roles"][0]
    )
    write_canonical_json(freeze_path, freeze)
    with pytest.raises(MODULE.ProductionAuthorityError, match="53-role"):
        MODULE.load_formal_authority(authority)

    authority = formal_authority_fixture(tmp_path / "second")
    review = authority / dict(MODULE.FORMAL_INPUT_ROLES)["prefreeze_review"]
    review.write_text(" Verdict: ACCEPT_FOR_FREEZE\n", encoding="utf-8")
    with pytest.raises(MODULE.ProductionAuthorityError):
        MODULE.load_formal_authority(authority)


@pytest.mark.parametrize(
    "extra",
    [
        "- Verdict: REJECT_FOR_FREEZE",
        "> Verdict: PENDING",
        "| Verdict | REJECT_FOR_FREEZE |",
        "**Verdict:** REJECT_FOR_FREEZE",
        "Verdict：PENDING",
        r"\Verdict: PENDING",
        "Verdict&#58; PENDING",
        "V&#101;rdict: PENDING",
        "V&#x65;rdict: PENDING",
        "Ver\u200bdict: PENDING",
        "Ver\ufe0fdict: PENDING",
        "Ver\u034fdict: PENDING",
        "V&#xFE0F;erdict: PENDING",
        "V&amp;#101;rdict: PENDING",
        "V&#101rdict: PENDING",
        "V&#x65rdict: PENDING",
        "V&#00101rdict: PENDING",
        "V&#x0065rdict: PENDING",
        "verdict = PENDING",
    ],
)
def test_formal_review_rejects_every_standalone_decorated_verdict(
    tmp_path: Path, extra: str
) -> None:
    authority = formal_authority_fixture(tmp_path)
    review = authority / dict(MODULE.FORMAL_INPUT_ROLES)["prefreeze_review"]
    review.write_text(
        f"{MODULE.PREFREEZE_ACCEPT_LINE}\n{extra}\n", encoding="utf-8"
    )
    with pytest.raises(MODULE.ProductionAuthorityError):
        MODULE.load_formal_authority(authority)


@pytest.mark.parametrize(
    "raw",
    [
        "relative/output",
        "/tmp/formal/../output",
        "//tmp/formal-output",
        "/tmp/formal-output/",
    ],
)
def test_formal_paths_reject_noncanonical_raw_spelling(raw: str) -> None:
    with pytest.raises(MODULE.PathContractError):
        MODULE.ensure_formal_preflight_output_allowed(raw, str(ROOT))


def test_formal_paths_reject_parent_symlinks(tmp_path: Path) -> None:
    real = tmp_path / "real"
    real.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    with pytest.raises(MODULE.PathContractError, match="symlink"):
        MODULE.ensure_formal_preflight_output_allowed(
            str(alias / "output"), str(ROOT)
        )
    authority = formal_authority_fixture(tmp_path / "fixture")
    authority_alias = tmp_path / "authority-alias"
    authority_alias.symlink_to(authority, target_is_directory=True)
    with pytest.raises(MODULE.PathContractError, match="symlink"):
        MODULE.load_formal_authority(str(authority_alias))


def test_formal_transaction_plans_are_exact_and_dispatch_stays_locked(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-transaction-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    cell = MODULE.CellKey(128, "S000")
    static_plan = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, cell
    )
    assert len(static_plan.argv) == len(static_plan.semantic_argv) == 26
    assert static_plan.argv[-2] == "--output"
    assert static_plan.semantic_argv[-1] == "<STAGING_PROOF_PATH>"
    assert tuple(
        path.name
        for path in (
            static_plan.proof_path,
            static_plan.stdout_path,
            static_plan.stderr_path,
            static_plan.record_path,
        )
    ) == ("proof.json", "stdout.txt", "stderr.txt", "record.json")
    called: list[str] = []
    with pytest.raises(MODULE.ProductionAuthorityError, match="unconditionally"):
        MODULE.dispatch_formal_static_transaction(
            static_plan, executor=lambda *_: called.append("static")
        )
    assert called == []

    branch_plan = MODULE.build_formal_branch_transaction_plan(
        snapshot, binding, run_hash, output, cell
    )
    assert branch_plan.task.argv()[0] == str(branch_plan.evaluator_binary_path)
    assert branch_plan.freeze_sha256 == branch_plan.main_freeze_sha256
    with pytest.raises(MODULE.ProductionAuthorityError, match="unconditionally"):
        MODULE.dispatch_formal_branch_transaction(
            branch_plan, transaction_runner=lambda *_: called.append("branch")
        )
    assert called == []


def test_formal_aggregate_candidates_are_null_authority_and_complete_only(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    entries = [
        {
            "cell": cell.payload(),
            "path": f"static/cell_manifests/{cell.precision_bits}/{cell.slab_id}.json",
            "sha256": MODULE.sha256_bytes(cell.label.encode("ascii")),
            "size_bytes": 1,
        }
        for cell in MODULE.exact_matrix()
    ]
    run_hash = "a" * 64
    summary, manifest = MODULE.build_formal_component_aggregate_candidates(
        "STATIC", snapshot, run_hash, entries
    )
    assert summary["status_counts"] == {"STATIC_CELL_CERTIFIED": 102}
    assert summary["scheduler_classification_counts"] == {
        "COMMITTED_EVALUATOR_RESULT": 102
    }
    assert summary["authority"] == manifest["authority"] == "PRODUCER_ONLY"
    assert summary["scientific_licensing_enabled"] is False
    assert summary["component_status"] is None
    assert summary["freeze_sha256"] == summary["main_freeze_sha256"]
    assert manifest["summary"]["sha256"] == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(summary)
    )
    with pytest.raises(MODULE.CorruptGeneration, match="102"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, entries[:-1]
        )

    wrong = [dict(item) for item in entries]
    wrong[1]["path"] = wrong[0]["path"]
    with pytest.raises(MODULE.CorruptGeneration, match="path/order"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, wrong
        )
    wrong = [dict(item) for item in entries]
    wrong[0]["path"] = "branch/cell_manifests/128/S000.json"
    with pytest.raises(MODULE.CorruptGeneration, match="path/order"):
        MODULE.build_formal_component_aggregate_candidates(
            "STATIC", snapshot, run_hash, wrong
        )


def replace_with_same_bytes(path: Path) -> None:
    replacement = path.with_name(path.name + ".replacement")
    replacement.write_bytes(path.read_bytes())
    replacement.chmod(path.stat().st_mode)
    os.replace(replacement, path)


def test_formal_snapshot_is_deeply_immutable_and_detects_same_byte_inode_swap(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    with pytest.raises(FrozenInstanceError):
        snapshot.input_roles[0].role = "forged"  # type: ignore[misc]
    assert isinstance(snapshot.main_freeze_raw, bytes)
    plan = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"]
    replace_with_same_bytes(plan)
    with pytest.raises(MODULE.ProductionAuthorityError, match="inode/image"):
        MODULE.revalidate_formal_snapshot(snapshot, ("l1_final_plan",))

    authority = formal_authority_fixture(tmp_path / "main")
    snapshot = MODULE.load_formal_authority(authority)
    replace_with_same_bytes(snapshot.main_freeze_path)
    with pytest.raises(MODULE.ProductionAuthorityError, match="main freeze inode"):
        MODULE.revalidate_formal_snapshot(snapshot, ("l1_final_plan",))


def test_formal_initialize_atomic_staging_failure_leaves_no_output(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    snapshot = MODULE.load_formal_authority(authority)
    for index, boundary in enumerate(
        ("AFTER_STAGE_DIR", "AFTER_CONFIG_FSYNC", "BEFORE_RENAME")
    ):
        output = (tmp_path / f"atomic-preflight-{index}").absolute()
        with pytest.raises(MODULE.SyntheticCrash):
            MODULE.initialize_formal_preflight(
                snapshot, output, _fail_at=boundary
            )
        assert not output.exists()
        assert not list(tmp_path.glob(f".{output.name}.formal-preflight-*"))


def test_formal_builders_reject_swapped_l1_images_before_parse_or_runtime_load(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-swap-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    cell = MODULE.CellKey(128, "S000")

    plan_path = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_final_plan"]
    replace_with_same_bytes(plan_path)
    with pytest.raises(MODULE.ProductionAuthorityError, match="l1_final_plan"):
        MODULE.build_formal_static_transaction_plan(
            snapshot, binding, run_hash, output, cell
        )

    authority = formal_authority_fixture(tmp_path / "branch")
    output = (tmp_path / "formal-branch-swap-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    summary = authority / dict(MODULE.FORMAL_INPUT_ROLES)["l1_summary"]
    replace_with_same_bytes(summary)
    MODULE._BRANCH_RUNTIME_MODULE = None
    with pytest.raises(MODULE.ProductionAuthorityError, match="l1_summary"):
        MODULE.build_formal_branch_transaction_plan(
            snapshot, binding, run_hash, output, cell
        )
    assert MODULE._BRANCH_RUNTIME_MODULE is None


def test_formal_static_dispatch_rehashes_evaluator_and_never_calls_executor(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "formal-evaluator-rehash").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    plan = MODULE.build_formal_static_transaction_plan(
        snapshot, binding, run_hash, output, MODULE.CellKey(128, "S000")
    )
    plan.evaluator_path.write_text("changed after plan\n", encoding="utf-8")
    called: list[bool] = []
    with pytest.raises(MODULE.ProductionAuthorityError, match="changed after plan"):
        MODULE.dispatch_formal_static_transaction(
            plan, executor=lambda *_: called.append(True)
        )
    assert called == []


def test_formal_branch_executes_captured_runtime_not_reopened_live_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "captured-runtime-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    runtime_role = next(
        item for item in snapshot.input_roles if item.role == "branch_runtime"
    )
    module_name = MODULE._formal_runtime_module_name(runtime_role.sha256)
    MODULE._FORMAL_BRANCH_RUNTIME_MODULES.pop(runtime_role.sha256, None)
    sys.modules.pop(module_name, None)
    marker = tmp_path / "runtime-side-effect"
    trap = tmp_path / "live-runtime-trap.py"
    trap.write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('opened')\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(MODULE, "BRANCH_RUNTIME_PATH", trap)
    monkeypatch.setattr(
        MODULE,
        "_load_branch_runtime",
        lambda: (_ for _ in ()).throw(AssertionError("mock loader called")),
    )
    plan = MODULE.build_formal_branch_transaction_plan(
        snapshot,
        binding,
        run_hash,
        output,
        MODULE.CellKey(128, "S000"),
    )
    assert plan.task.argv()[0] == str(plan.evaluator_binary_path)
    loaded = sys.modules[module_name]
    assert loaded.__formal_runtime_sha256__ == runtime_role.sha256
    assert loaded.__file__ == str(trap)
    assert not marker.exists()


def test_formal_branch_rejects_unbound_precached_runtime(
    tmp_path: Path,
) -> None:
    authority = formal_authority_fixture(tmp_path)
    output = (tmp_path / "precache-runtime-output").absolute()
    snapshot = MODULE.load_formal_authority(authority)
    binding, run_hash = MODULE.initialize_formal_preflight(snapshot, output)
    runtime_role = next(
        item for item in snapshot.input_roles if item.role == "branch_runtime"
    )
    name = MODULE._formal_runtime_module_name(runtime_role.sha256)
    MODULE._FORMAL_BRANCH_RUNTIME_MODULES.pop(runtime_role.sha256, None)
    previous = sys.modules.get(name)
    sys.modules[name] = types.ModuleType(name)
    try:
        with pytest.raises(MODULE.ProductionAuthorityError, match="pre-cached"):
            MODULE.build_formal_branch_transaction_plan(
                snapshot,
                binding,
                run_hash,
                output,
                MODULE.CellKey(128, "S000"),
            )
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous


def test_explicit_mock_initialize_and_cells_never_gain_authority(tmp_path: Path) -> None:
    output = tmp_path / "cli-mock"
    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--mock-only",
            "--initialize-only",
            "--mock-static-cells",
            "3",
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["artifact_status"] == "MOCK_ONLY_NON_LICENSING"
    assert payload["completed_cells"] == 3
    assert payload["production_authorized"] is False
    assert payload["component_status"] is None
    assert payload["milestone_status"] is None
    assert payload["theorem_status"] is None
    assert payload["final_status"] is None
    assert payload["aggregate_finalized"] is False
    assert payload["aggregate"] is None
    assert len(list((output / "static/cell_manifests").rglob("*.json"))) == 3
    assert not MODULE.static_aggregate_summary_path(output).exists()
    assert not MODULE.static_aggregate_manifest_path(output).exists()
    assert not MODULE.CANONICAL_RESULT.exists()


def test_full_mock_matrix_publishes_write_once_static_aggregate(tmp_path: Path) -> None:
    output = tmp_path / "full-static-mock"
    first = MODULE.run_mock_static(output, 102, resume=False)
    assert first["completed_cells"] == 102
    assert first["aggregate_finalized"] is True
    assert first["aggregate"]["state"] == "COMMITTED"
    summary_path = MODULE.static_aggregate_summary_path(output)
    manifest_path = MODULE.static_aggregate_manifest_path(output)
    summary_before = summary_path.read_bytes()
    manifest_before = manifest_path.read_bytes()
    summary = MODULE.strict_json_load(summary_path)
    manifest = MODULE.strict_json_load(manifest_path)
    assert summary["cell_count"] == 102
    assert summary["matrix"] == MODULE.matrix_payload()
    assert summary["main_freeze_sha256"] is None
    assert summary["component_status"] is None
    assert summary["theorem_status"] is None
    assert len(manifest["cell_manifests"]) == 102
    assert manifest["cell_manifests"][0]["cell"] == {
        "precision_bits": 128,
        "slab_id": "S000",
    }
    assert manifest["cell_manifests"][-1]["cell"] == {
        "precision_bits": 256,
        "slab_id": "S050",
    }
    assert manifest["ordered_cell_manifest_root"] == MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(manifest["cell_manifests"])
    )
    assert manifest["summary"] == {
        "path": "static/aggregate_summary.json",
        "sha256": MODULE.sha256(summary_path),
        "size_bytes": summary_path.stat().st_size,
    }

    resumed = MODULE.run_mock_static(output, 102, resume=True)
    assert resumed["aggregate"]["state"] == "RESUMED_COMMITTED"
    assert summary_path.read_bytes() == summary_before
    assert manifest_path.read_bytes() == manifest_before


def test_static_aggregate_rejects_live_stage_for_committed_cell(
    tmp_path: Path,
) -> None:
    output = tmp_path / "archive"
    first = MODULE.run_mock_static(output, 102, resume=False)
    assert first["aggregate_finalized"] is True
    config_hash = MODULE.sha256(MODULE.run_config_path(output))
    stage = MODULE.staging_path(
        MODULE.operational_root_for(output),
        MODULE.CellKey(128, "S000"),
        config_hash,
    )
    stage.mkdir(parents=True)
    with pytest.raises(MODULE.CorruptGeneration, match="live staging owners"):
        MODULE.run_mock_static(output, 102, resume=True)


def test_static_aggregate_rejects_extra_manifest_namespace(tmp_path: Path) -> None:
    output, operational, binding, config_hash = initialize(tmp_path)
    for cell in MODULE.exact_matrix():
        MODULE.commit_mock_static_cell(
            output, operational, cell, binding["matrix_id"], config_hash
        )
    extra = output / "static/cell_manifests/128/EXTRA.json"
    extra.write_text("{}\n", encoding="utf-8")
    with pytest.raises(MODULE.CorruptGeneration, match="namespace mismatch"):
        MODULE.finalize_static_mock_aggregate(
            output, binding["matrix_id"], config_hash
        )
    assert not MODULE.static_aggregate_summary_path(output).exists()
    assert not MODULE.static_aggregate_manifest_path(output).exists()


def test_static_aggregate_rejects_extra_cell_subtree(tmp_path: Path) -> None:
    output = tmp_path / "extra-cell-subtree"
    result = MODULE.run_mock_static(output, 102, resume=False)
    assert result["aggregate_finalized"] is True
    extra = output / "static/cells/128/EXTRA"
    extra.mkdir()
    (extra / "junk.json").write_text("{}\n", encoding="utf-8")
    run_config = MODULE.strict_json_load(
        MODULE.run_config_path(output), require_canonical=True
    )
    with pytest.raises(MODULE.CorruptGeneration, match="cell namespace mismatch"):
        MODULE.validate_static_mock_aggregate(
            output,
            run_config["matrix_id"],
            MODULE.sha256(MODULE.run_config_path(output)),
        )


def test_mock_cli_requires_explicit_action_and_resume(tmp_path: Path) -> None:
    output = tmp_path / "explicit"
    no_action = MODULE.main(["--mock-only", "--output", str(output)])
    assert no_action == 1
    assert not output.exists()

    assert MODULE.main(
        [
            "--mock-only",
            "--mock-static-cells",
            "1",
            "--output",
            str(output),
        ]
    ) == 0
    assert MODULE.main(
        [
            "--mock-only",
            "--mock-static-cells",
            "1",
            "--resume",
            "--output",
            str(output),
        ]
    ) == 0


def test_directory_publication_is_atomic_no_replace(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "destination"
    source.mkdir()
    destination.mkdir()
    marker = destination / "marker"
    marker.write_text("keep\n", encoding="utf-8")
    with pytest.raises(MODULE.CorruptGeneration, match="destination collision"):
        MODULE.rename_directory_noreplace(source, destination)
    assert source.is_dir()
    assert marker.read_text(encoding="utf-8") == "keep\n"


def test_strict_json_image_binds_parse_hash_and_size_to_one_snapshot(
    tmp_path: Path,
) -> None:
    path = tmp_path / "object.json"
    payload = {"authority": "PRODUCER_ONLY", "value": 1}
    raw = MODULE.canonical_json_bytes(payload)
    path.write_bytes(raw)
    parsed, captured, info = MODULE.strict_json_image(
        path, require_canonical=True
    )
    assert parsed == payload
    assert captured == raw
    assert MODULE.sha256_bytes(captured) == MODULE.file_binding(path)["sha256"]
    assert info.st_size == len(raw)
