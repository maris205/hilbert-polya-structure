from __future__ import annotations

import ast
import argparse
from copy import deepcopy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / "scripts/replay_r401_val_l3_s0_through_a1_checkers.py"
CANONICAL_OUTPUT = (
    ROOT
    / "research/route_a_wave_trace/"
    "R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json"
)


def load_adapter():
    spec = importlib.util.spec_from_file_location("r401_l3_a1_s0_adapter", ADAPTER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ADAPTER = load_adapter()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def control_digests() -> dict[str, str]:
    return {role: digest(path) for role, path in ADAPTER.CONTROL_PATHS.items()}


def strict_load(path: Path) -> dict[str, object]:
    return ADAPTER.strict_json_bytes(path.read_bytes(), str(path))


@pytest.fixture(scope="module")
def compatibility_payload() -> dict[str, object]:
    assert not CANONICAL_OUTPUT.exists()
    before = control_digests()
    payload = ADAPTER.build_compatibility_object()
    assert control_digests() == before
    assert not CANONICAL_OUTPUT.exists()
    return payload


def test_canonical_s0_replays_to_exact_non_authoritative_object(
    compatibility_payload: dict[str, object],
) -> None:
    payload = compatibility_payload
    assert set(payload) == {
        "schema_version", "protocol_id", "artifact_role", "artifact_status",
        "source_protocols", "matrix", "static_facts", "branch_facts",
        "composite_facts", "control_hashes", "role_sets", "source_bindings",
        "replay_status", "failures", "claim_boundary", "milestone_status",
        "theorem_status", "final_status",
    }
    assert len(payload) == 18
    assert payload["schema_version"] == 1
    assert type(payload["schema_version"]) is int
    assert payload["artifact_status"] == "NON_LICENSING"
    assert payload["replay_status"] == "PASS_S0_COMPATIBILITY_REPLAY"
    assert payload["failures"] == []
    for key in ("milestone_status", "theorem_status", "final_status"):
        assert payload[key] is None
    assert payload["source_protocols"] == {
        "static": "R401-VAL-L3-PHASE-TUBE-SMOKE-DRAFT",
        "branch": "R401-VAL-L3-BT-S0",
        "composite": "R401-VAL-L3-S0-COMPOSITE-DRAFT",
    }
    assert payload["matrix"] == {
        "precisions": [128, 256],
        "slabs": ["S000", "S025", "S050"],
        "cell_count": 6,
    }
    assert payload["static_facts"] == ADAPTER.STATIC_FACTS
    assert payload["branch_facts"] == ADAPTER.BRANCH_FACTS
    assert payload["composite_facts"] == ADAPTER.COMPOSITE_FACTS
    assert payload["control_hashes"] == ADAPTER.CONTROL_HASHES
    inventory = payload["role_sets"]
    assert [(item["precision_bits"], item["slab_id"]) for item in inventory["static_proof_entries"]] == [
        (128, "S000"), (128, "S025"), (128, "S050"),
        (256, "S000"), (256, "S025"), (256, "S050"),
    ]
    assert all(
        set(item) == ADAPTER.STATIC_ENTRY_KEYS
        for item in inventory["static_proof_entries"]
    )
    assert inventory["branch_manifest_roles"] == list(ADAPTER.BRANCH_ROLE_PATHS)
    assert len(inventory["branch_manifest_roles"]) == 26
    assert inventory["composite_manifest_roles"] == [
        {"scope": scope, "path": path}
        for scope, path in ADAPTER.COMPOSITE_FILE_ROLES
    ]
    assert inventory["composite_component_roles"] == [
        {"component": component, "path": path}
        for component, path in ADAPTER.COMPOSITE_COMPONENT_ROLES
    ]
    assert set(payload["source_bindings"]) == set(ADAPTER.COMPATIBILITY_SOURCE_ROLES)
    for role, bound_hash in payload["source_bindings"].items():
        assert bound_hash == digest(ROOT / role)
    assert payload["source_bindings"][ADAPTER.COMPATIBILITY_SOURCE_ROLES[0]] == digest(
        ADAPTER_PATH
    )
    ADAPTER.validate_compatibility_output(payload)


def test_adapter_source_has_no_evaluator_or_checker_dispatch_path() -> None:
    source = ADAPTER_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported_roots = {
        alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        (node.module or "").split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    assert "subprocess" not in imported_roots
    assert "importlib" not in imported_roots
    assert "evaluate_r401_val_l3_a1_static_cell" not in source
    forbidden_calls = {
        (node.func.value.id, node.func.attr)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id in {"os", "subprocess"}
        and node.func.attr in {
            "system", "popen", "spawnl", "spawnle", "spawnlp", "spawnlpe",
            "spawnv", "spawnve", "spawnvp", "spawnvpe", "execv", "execve",
            "execvp", "execvpe", "run", "Popen", "call", "check_call",
            "check_output",
        }
    }
    assert forbidden_calls == set()


def test_optional_output_is_temporary_exclusive_and_never_canonical(
    tmp_path: Path, compatibility_payload: dict[str, object]
) -> None:
    output = tmp_path / "compatibility.json"
    encoded = ADAPTER.canonical_json_bytes(compatibility_payload)
    ADAPTER._secure_exclusive_write(output, encoded)
    assert output.read_bytes() == encoded
    with pytest.raises(ADAPTER.CompatibilityError, match="exclusive temporary output"):
        ADAPTER._secure_exclusive_write(output, encoded)
    with pytest.raises(ADAPTER.CompatibilityError, match="canonical compatibility"):
        ADAPTER._secure_exclusive_write(CANONICAL_OUTPUT, encoded)
    assert not CANONICAL_OUTPUT.exists()


@pytest.mark.parametrize(
    "raw",
    (
        "//root/a416-compatibility.json",
        "///tmp/a416-compatibility.json",
        "/tmp//a416-compatibility.json",
    ),
)
def test_noncanonical_root_and_repeated_slashes_are_rejected(raw: str) -> None:
    with pytest.raises(argparse.ArgumentTypeError, match="root slash|non-canonical"):
        ADAPTER._output_argument(raw)


def test_double_root_path_object_is_rejected_before_secure_io() -> None:
    with pytest.raises(ADAPTER.CompatibilityError, match="non-canonical"):
        ADAPTER._canonical_absolute(Path("//root/a416.json"), "synthetic path")


def test_double_leading_slash_cannot_alias_reserved_or_project_paths(
    compatibility_payload: dict[str, object],
) -> None:
    encoded = ADAPTER.canonical_json_bytes(compatibility_payload)
    doubled_canonical = Path("/" + str(CANONICAL_OUTPUT))
    doubled_input = Path("/" + str(ADAPTER.CONTROL_PATHS["static_summary"]))

    with pytest.raises(argparse.ArgumentTypeError, match="root slash"):
        ADAPTER._output_argument(str(doubled_canonical))
    with pytest.raises(ADAPTER.CompatibilityError, match="non-canonical"):
        ADAPTER.InputSnapshot().capture(doubled_input, "double-root input")
    with pytest.raises(ADAPTER.CompatibilityError, match="non-canonical"):
        ADAPTER._secure_exclusive_write(doubled_canonical, encoded)
    assert not CANONICAL_OUTPUT.exists()


def test_single_root_temporary_output_argument_remains_accepted(tmp_path: Path) -> None:
    output = tmp_path / "outside-project.json"
    assert ADAPTER._output_argument(str(output)) == output


@pytest.mark.parametrize(
    "raw,match",
    (
        (b'{"x":1,"x":2}\n', "duplicate JSON key"),
        (b'{"x":NaN}\n', "non-finite JSON constant"),
        (b'{"x":Infinity}\n', "non-finite JSON constant"),
        (b'{"x":1e400}\n', "non-finite JSON float"),
        (b'[1,2,3]\n', "top-level object"),
    ),
)
def test_strict_json_rejects_duplicates_nonfinite_and_wrong_root(
    raw: bytes, match: str
) -> None:
    with pytest.raises(ADAPTER.CompatibilityError, match=match):
        ADAPTER.strict_json_bytes(raw, "synthetic")


@pytest.mark.parametrize(
    "mutation,match",
    (
        (lambda value: value.__setitem__("unexpected", None), "extra"),
        (lambda value: value.pop("failures"), "missing"),
        (lambda value: value.__setitem__("schema_version", True), "schema_version"),
        (lambda value: value["static_facts"].__setitem__("node_count", 84172.0),
         "static facts"),
        (lambda value: value.__setitem__("failures", {}), "failures"),
        (lambda value: value.__setitem__("final_status", "PASS"), "final_status"),
    ),
)
def test_exact_contract_output_schema_and_types_reject_mutations(
    compatibility_payload: dict[str, object], mutation, match: str
) -> None:
    payload = deepcopy(compatibility_payload)
    mutation(payload)
    with pytest.raises(ADAPTER.CompatibilityError, match=match):
        ADAPTER.validate_compatibility_output(payload)


@pytest.mark.parametrize(
    "mutation,match",
    (
        (lambda value: value["matrix"].__setitem__("proof_count", True),
         "static matrix"),
        (lambda value: value["proofs"][0].__setitem__("precision_bits", 128.0),
         "exact integer"),
        (lambda value: value["proofs"][0].__setitem__("node_count", 13794.0),
         "exact integer"),
    ),
)
def test_static_shape_rejects_boolean_integer_and_float_integer_aliases(
    mutation, match: str
) -> None:
    summary = strict_load(ADAPTER.CONTROL_PATHS["static_summary"])
    mutation(summary)
    with pytest.raises(ADAPTER.CompatibilityError, match=match):
        ADAPTER.validate_static_summary_shape(summary)


def test_closed_schemas_status_ownership_and_null_authority_fail_closed() -> None:
    static = strict_load(ADAPTER.CONTROL_PATHS["static_summary"])
    static["unexpected"] = None
    with pytest.raises(ADAPTER.CompatibilityError, match="extra"):
        ADAPTER.validate_static_summary_shape(static)

    static = strict_load(ADAPTER.CONTROL_PATHS["static_summary"])
    static["implementation_status"] = "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"
    with pytest.raises(ADAPTER.CompatibilityError, match="implementation_status"):
        ADAPTER.validate_static_summary_shape(static)

    branch = strict_load(ADAPTER.CONTROL_PATHS["branch_summary"])
    branch["milestone_status"] = "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"
    with pytest.raises(ADAPTER.CompatibilityError, match="milestone_status"):
        ADAPTER.branch_common(branch, "branch summary")

    composite = strict_load(ADAPTER.CONTROL_PATHS["composite_summary"])
    composite["theorem_status"] = "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"
    with pytest.raises(ADAPTER.CompatibilityError, match="theorem_status"):
        ADAPTER.composite_common(composite, "composite summary")


def test_static_six_proof_order_missing_and_extra_are_rejected() -> None:
    summary = strict_load(ADAPTER.CONTROL_PATHS["static_summary"])
    summary["proofs"][0], summary["proofs"][1] = (
        summary["proofs"][1], summary["proofs"][0]
    )
    with pytest.raises(ADAPTER.CompatibilityError, match="order/identity"):
        ADAPTER.validate_static_summary_shape(summary)

    summary = strict_load(ADAPTER.CONTROL_PATHS["static_summary"])
    summary["proofs"].pop()
    with pytest.raises(ADAPTER.CompatibilityError, match="exactly six"):
        ADAPTER.validate_static_summary_shape(summary)

    summary = strict_load(ADAPTER.CONTROL_PATHS["static_summary"])
    summary["proofs"].append(deepcopy(summary["proofs"][-1]))
    with pytest.raises(ADAPTER.CompatibilityError, match="exactly six"):
        ADAPTER.validate_static_summary_shape(summary)


def test_branch_exact_26_roles_reject_subtraction_addition_and_alias() -> None:
    canonical = strict_load(ADAPTER.CONTROL_PATHS["branch_manifest"])
    mutations = []
    removed = deepcopy(canonical)
    removed["files"].pop(next(iter(removed["files"])))
    mutations.append(removed)
    added = deepcopy(canonical)
    added["files"][str(ROOT / "unexpected.txt")] = "0" * 64
    mutations.append(added)
    aliased = deepcopy(canonical)
    old = next(iter(aliased["files"]))
    value = aliased["files"].pop(old)
    aliased["files"][old.replace("/results/", "/results/./", 1)] = value
    mutations.append(aliased)
    for payload in mutations:
        with pytest.raises(ADAPTER.CompatibilityError, match="26 roles|26-role"):
            ADAPTER.validate_branch_manifest_shape(payload, ADAPTER.InputSnapshot())


def test_composite_roles_counts_and_status_types_are_closed() -> None:
    snapshot = ADAPTER.InputSnapshot()
    controls = ADAPTER._capture_controls(snapshot)
    manifest = strict_load(ADAPTER.CONTROL_PATHS["composite_manifest"])
    manifest["files"][0], manifest["files"][1] = (
        manifest["files"][1], manifest["files"][0]
    )
    with pytest.raises(ADAPTER.CompatibilityError, match="role/order"):
        ADAPTER.validate_composite_manifest_shape(manifest, controls, snapshot)

    checker = strict_load(ADAPTER.CONTROL_PATHS["composite_checker"])
    checker["manifest_binding_count"] = 18.0
    source = snapshot.capture(
        ROOT / "scripts/check_r401_val_l3_s0_composite_independent.py",
        "checker source",
    )
    with pytest.raises(ADAPTER.CompatibilityError, match="exact integer"):
        ADAPTER.validate_composite_checker_shape(checker, source)


def test_path_alias_symlink_leaf_parent_and_hardlink_fail_closed(
    tmp_path: Path,
) -> None:
    target = tmp_path / "target.json"
    target.write_text('{"ok":true}\n', encoding="utf-8")
    with pytest.raises(ADAPTER.CompatibilityError, match="normalized|dot"):
        ADAPTER.InputSnapshot().capture(
            tmp_path / "subdir" / ".." / "target.json", "path alias"
        )

    leaf_link = tmp_path / "leaf-link.json"
    leaf_link.symlink_to(target)
    with pytest.raises(ADAPTER.CompatibilityError, match="secure open failed"):
        ADAPTER.InputSnapshot().capture(leaf_link, "leaf symlink")

    real_parent = tmp_path / "real-parent"
    real_parent.mkdir()
    inside = real_parent / "inside.json"
    inside.write_text('{"ok":true}\n', encoding="utf-8")
    parent_link = tmp_path / "parent-link"
    parent_link.symlink_to(real_parent, target_is_directory=True)
    with pytest.raises(ADAPTER.CompatibilityError, match="secure open failed"):
        ADAPTER.InputSnapshot().capture(parent_link / "inside.json", "parent symlink")

    hard_link = tmp_path / "hard-link.json"
    os.link(target, hard_link)
    with pytest.raises(ADAPTER.CompatibilityError, match="hard-link alias"):
        ADAPTER.InputSnapshot().capture(target, "hard link source")


def test_snapshot_detects_toctou_mutation(tmp_path: Path) -> None:
    path = tmp_path / "mutable.json"
    path.write_text('{"value":1}\n', encoding="utf-8")
    snapshot = ADAPTER.InputSnapshot()
    snapshot.capture(path, "mutable input")
    path.write_text('{"value":2}\n', encoding="utf-8")
    with pytest.raises(ADAPTER.CompatibilityError, match="TOCTOU mutation"):
        snapshot.assert_unchanged()


def test_wrong_hardcoded_control_digest_fails_before_compatibility(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(ADAPTER.CONTROL_HASHES, "static_summary", "0" * 64)
    with pytest.raises(ADAPTER.CompatibilityError, match="sealed S0 hash"):
        ADAPTER._capture_controls(ADAPTER.InputSnapshot())


def test_canonical_replay_path_remains_absent_after_all_focused_checks() -> None:
    assert not CANONICAL_OUTPUT.exists()
