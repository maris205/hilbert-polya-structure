from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
PACKAGER_PATH = ROOT / "scripts/build_r401_val_l3_s0_composite.py"
CHECKER_PATH = ROOT / "scripts/check_r401_val_l3_s0_composite_independent.py"
STATIC_DIR = ROOT / "results/r401_val_l3_phase_tube_smoke"
BRANCH_DIR = ROOT / "results/r401_val_l3_branch_tube_smoke"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PACKAGER = load(PACKAGER_PATH, "r401_l3_composite_packager")
CHECKER = load(CHECKER_PATH, "r401_l3_composite_checker")


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_composite_sources_have_isolated_authority_and_no_checker_import() -> None:
    packager = PACKAGER_PATH.read_text(encoding="utf-8")
    checker = CHECKER_PATH.read_text(encoding="utf-8")
    assert "from build_r401_val_l3_s0_composite import" not in checker
    assert "import build_r401_val_l3_s0_composite" not in checker
    for text in (packager, checker):
        assert 'IMPLEMENTATION_STATUS = "PASS_IMPLEMENTATION_SMOKE"' in text
        assert 'COMPONENT_SCOPE = "COMPOSITE_S0"' in text
        assert '"scientific_licensing_enabled": False' in text
        assert '"milestone_status": None' in text
        assert '"theorem_status": None' in text
        assert '"final_status": None' in text
        assert "A416_EXPERIMENT_TRACKER.md" not in text
        assert "A416_PHASE_FLOWBOX_DERIVATION.md" in text
        assert "R401_VAL_L3_PHASE_TUBE_PROTOCOL_DRAFT.md" in text
        assert "A416_EXPERIMENT_PLAN.md" in text
    assert "refusing to reuse composite output" in packager
    assert "refusing to overwrite checker result" in checker


def test_canonical_components_replay_to_the_same_exact_six_pairs() -> None:
    static_component, static = PACKAGER.validate_static_component(STATIC_DIR)
    branch_component, branch, branch_manifest = PACKAGER.validate_branch_component(
        BRANCH_DIR
    )
    expected = {
        (bits, slab)
        for bits in (128, 256)
        for slab in ("S000", "S025", "S050")
    }
    assert set(static) == expected
    assert set(branch) == expected
    assert len(branch_manifest) == 26
    assert static_component["component_status"] == "PASS_STATIC_COMPONENT_SMOKE"
    assert static_component["component_scope"] == "STATIC_ONLY"
    assert branch_component["component_status"] == (
        "PASS_NON_LICENSING_BRANCH_TUBE_SMOKE"
    )
    assert static_component["composite_s0_passed"] is False
    assert branch_component["composite_s0_passed"] is False
    assert static_component["scientific_licensing_enabled"] is False
    assert branch_component["scientific_licensing_enabled"] is False


def test_temp_composite_packager_and_no_import_checker_pass_write_once(
    tmp_path: Path,
) -> None:
    output = tmp_path / "composite"
    summary = PACKAGER.build_composite(STATIC_DIR, BRANCH_DIR, output)
    assert summary["component_scope"] == "COMPOSITE_S0"
    assert summary["composite_s0_passed"] is True
    assert summary["implementation_status"] == "PASS_IMPLEMENTATION_SMOKE"
    assert summary["milestone_status"] is None
    assert summary["theorem_status"] is None
    assert summary["final_status"] is None
    assert len(summary["cells"]) == 6
    assert {path.name for path in output.iterdir()} == {
        "summary.json",
        "manifest.json",
        "R401_VAL_L3_S0_COMPOSITE_REPORT.md",
    }
    assert CHECKER.main(["--input-dir", str(output)]) == 0
    checked = json.loads(
        (output / "independent_checker.json").read_text(encoding="utf-8")
    )
    assert checked["checker_status"] == "PASS"
    assert checked["cell_replay_count"] == 6
    assert checked["failures"] == []
    assert checked["implementation_status"] == "PASS_IMPLEMENTATION_SMOKE"
    assert checked["composite_s0_passed"] is True
    assert checked["final_status"] is None
    assert CHECKER.main(["--input-dir", str(output)]) == 1
    with pytest.raises(FileExistsError, match="refusing to reuse"):
        PACKAGER.build_composite(STATIC_DIR, BRANCH_DIR, output)


def test_checker_rejects_forged_composite_cell_even_before_manifest_replay(
    tmp_path: Path,
) -> None:
    output = tmp_path / "composite"
    PACKAGER.build_composite(STATIC_DIR, BRANCH_DIR, output)
    summary_path = output / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["cells"][0]["branch"]["solution_piece_count"] += 1
    write_json(summary_path, summary)
    with pytest.raises(ValueError, match="cells do not independently reconstruct"):
        CHECKER.verify_composite(output, STATIC_DIR, BRANCH_DIR)


def test_packager_rejects_branch_manifest_with_provenance_subtracted(
    tmp_path: Path,
) -> None:
    branch_copy = tmp_path / "branch"
    shutil.copytree(BRANCH_DIR, branch_copy)
    manifest_path = branch_copy / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    removed = next(
        name
        for name in manifest["files"]
        if name.endswith("/capd_r401_phase_branch_tube_mp")
    )
    del manifest["files"][removed]
    write_json(manifest_path, manifest)
    checker_path = branch_copy / "independent_checker.json"
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    checker["manifest_file_count"] = 25
    write_json(checker_path, checker)
    with pytest.raises(ValueError, match="exact frozen 26-file set"):
        PACKAGER.validate_branch_component(branch_copy)


def test_strict_json_and_symlink_gates_fail_closed(tmp_path: Path) -> None:
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"x": 1, "x": 2}\n', encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate JSON key"):
        CHECKER.strict_json(duplicate)

    overflowing = tmp_path / "overflowing.json"
    overflowing.write_text('{"x": 1e400}\n', encoding="utf-8")
    with pytest.raises(ValueError, match="non-finite JSON float"):
        CHECKER.strict_json(overflowing)

    target = tmp_path / "target"
    target.mkdir()
    linked_output = tmp_path / "linked-output"
    linked_output.symlink_to(target, target_is_directory=True)
    with pytest.raises(FileExistsError, match="refusing to reuse"):
        PACKAGER.build_composite(STATIC_DIR, BRANCH_DIR, linked_output)


@pytest.mark.parametrize(
    "mutation,match",
    (
        (lambda summary: summary.__setitem__("schema_version", True), "schema_version"),
        (
            lambda summary: summary["matrix"]["precisions"].__setitem__(0, 128.0),
            "composite matrix",
        ),
        (
            lambda summary: summary["matrix"].__setitem__("cell_count", 6.0),
            "composite matrix",
        ),
        (
            lambda summary: summary["cells"][0]["branch"].__setitem__(
                "solution_piece_count",
                float(summary["cells"][0]["branch"]["solution_piece_count"]),
            ),
            "cells do not independently reconstruct",
        ),
    ),
)
def test_checker_rejects_bool_int_and_int_float_json_aliases(
    tmp_path: Path,
    mutation,
    match: str,
) -> None:
    output = tmp_path / "composite"
    PACKAGER.build_composite(STATIC_DIR, BRANCH_DIR, output)
    summary_path = output / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    mutation(summary)
    write_json(summary_path, summary)
    with pytest.raises(ValueError, match=match):
        CHECKER.verify_composite(output, STATIC_DIR, BRANCH_DIR)


@pytest.mark.parametrize(
    "field,value,match",
    (
        ("schema_version", True, "schema version"),
        ("matrix_precision", 128.0, "static 3x2 matrix"),
    ),
)
def test_packager_rejects_static_component_numeric_type_aliases(
    tmp_path: Path,
    field: str,
    value: object,
    match: str,
) -> None:
    static_copy = tmp_path / "static"
    shutil.copytree(STATIC_DIR, static_copy)
    summary_path = static_copy / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if field == "matrix_precision":
        summary["matrix"]["precisions"][0] = value
    else:
        summary[field] = value
    write_json(summary_path, summary)
    with pytest.raises(ValueError, match=match):
        PACKAGER.validate_static_component(static_copy)


def test_recursive_exact_json_equality_rejects_python_numeric_aliases() -> None:
    for module in (PACKAGER, CHECKER):
        assert module.exact_json_equal(1, 1)
        assert not module.exact_json_equal(1, True)
        assert not module.exact_json_equal(1, 1.0)
        assert not module.exact_json_equal(
            {"precisions": [128, 256]},
            {"precisions": [128.0, 256]},
        )


def test_packager_manifest_binds_exact_sources_docs_and_component_controls(
    tmp_path: Path,
) -> None:
    output = tmp_path / "composite"
    PACKAGER.build_composite(STATIC_DIR, BRANCH_DIR, output)
    summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert summary["source_bindings"] == PACKAGER.source_bindings()
    assert len(manifest["component_files"]) == 6
    assert {
        (record["component"], record["path"])
        for record in manifest["component_files"]
    } == {
        (component, name)
        for component in ("static", "branch")
        for name in ("summary.json", "manifest.json", "independent_checker.json")
    }
    for record in manifest["files"]:
        path = (
            output / record["path"]
            if record["scope"] == "OUTPUT"
            else ROOT / record["path"]
        )
        assert record["sha256"] == sha256(path)
        assert record["size_bytes"] == path.stat().st_size
