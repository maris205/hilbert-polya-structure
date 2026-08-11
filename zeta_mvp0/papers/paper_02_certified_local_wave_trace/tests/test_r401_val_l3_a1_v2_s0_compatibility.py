from __future__ import annotations

import ast
import argparse
from copy import deepcopy
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import stat
import sys
import tempfile

import pytest


ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / "scripts/replay_r401_val_l3_s0_through_a1_v2_checkers.py"
CANONICAL_OUTPUT = (
    ROOT
    / "research/route_a_wave_trace/"
    "R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"
)


def load_adapter():
    spec = importlib.util.spec_from_file_location(
        "r401_l3_a1_v2_s0_adapter", ADAPTER_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_release_builder():
    path = ROOT / "scripts/build_r401_val_l3_a1_v2_release_provenance.py"
    spec = importlib.util.spec_from_file_location("r401_l3_a1_v2_release_for_s0", path)
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


def path_preimage(path: Path) -> tuple[object, ...]:
    try:
        info = os.lstat(path)
    except FileNotFoundError:
        return ("ABSENT",)
    raw_hash = digest(path) if stat.S_ISREG(info.st_mode) else None
    return (
        "PRESENT",
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
        raw_hash,
    )


def assert_preimage_unchanged(
    path: Path, expected: tuple[object, ...]
) -> None:
    assert path_preimage(path) == expected


@pytest.fixture(scope="module", autouse=True)
def live_canonical_role13_is_never_touched():
    before = path_preimage(CANONICAL_OUTPUT)
    yield before
    assert_preimage_unchanged(CANONICAL_OUTPUT, before)


def test_present_and_absent_preimage_guard_is_presence_agnostic(
    tmp_path: Path,
) -> None:
    present = tmp_path / "simulated-published-role13.json"
    present.write_bytes(b'{"published":true}\n')
    present.chmod(0o644)
    present_before = path_preimage(present)
    assert present_before[0] == "PRESENT"
    assert_preimage_unchanged(present, present_before)

    absent = tmp_path / "simulated-absent-role13.json"
    absent_before = path_preimage(absent)
    assert absent_before == ("ABSENT",)
    assert_preimage_unchanged(absent, absent_before)

    present.write_bytes(b'{"published":false}\n')
    with pytest.raises(AssertionError):
        assert_preimage_unchanged(present, present_before)

    source = Path(__file__).read_text(encoding="utf-8")
    forbidden_absence_assertion = "assert not " + "CANONICAL_OUTPUT.exists()"
    assert forbidden_absence_assertion not in source


@pytest.fixture(scope="module")
def compatibility_payload() -> dict[str, object]:
    before = control_digests()
    payload = ADAPTER.build_compatibility_object()
    assert control_digests() == before
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


def test_v2_source_bindings_are_exact_and_attempt1_paths_are_absent(
    compatibility_payload: dict[str, object],
) -> None:
    assert ADAPTER.COMPATIBILITY_SOURCE_ROLES == (
        "scripts/replay_r401_val_l3_s0_through_a1_v2_checkers.py",
        "research/route_a_wave_trace/R401_VAL_L3_A1_V2_PREFREEZE_DESIGN.md",
        "research/route_a_wave_trace/R401_VAL_L3_A1_V2_CHECKER_CONTRACT.md",
        "research/route_a_wave_trace/R401_VAL_L3_A1_V2_RELEASE_PROVENANCE_CONTRACT.md",
    )
    assert set(compatibility_payload["source_bindings"]) == set(
        ADAPTER.COMPATIBILITY_SOURCE_ROLES
    )
    assert ADAPTER.ROLE13_RELATIVE_PATH == Path(
        "research/route_a_wave_trace/"
        "R401_VAL_L3_A1_V2_S0_COMPATIBILITY_REPLAY.json"
    )
    source = ADAPTER_PATH.read_text(encoding="utf-8")
    for attempt1 in (
        "scripts/replay_r401_val_l3_s0_through_a1_checkers.py",
        "R401_VAL_L3_A1_PREFREEZE_DESIGN.md",
        "R401_VAL_L3_A1_CHECKER_CONTRACT.md",
        "R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md",
        "R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json",
    ):
        assert attempt1 not in source


def test_role11_count_lock_is_explicitly_unset_without_blocking_s0_edges() -> None:
    assert ADAPTER.EXPECTED_PREFREEZE_TEST_PASSED is None


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
            "check_output", "fork", "forkpty", "posix_spawn", "posix_spawnp",
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
    assert stat.S_IMODE(output.stat().st_mode) == 0o600
    assert output.stat().st_nlink == 1
    with pytest.raises(ADAPTER.CompatibilityError, match="exclusive temporary output"):
        ADAPTER._secure_exclusive_write(output, encoded)


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


def test_double_leading_slash_cannot_alias_reserved_or_project_paths() -> None:
    doubled_canonical = Path("/" + str(CANONICAL_OUTPUT))
    doubled_input = Path("/" + str(ADAPTER.CONTROL_PATHS["static_summary"]))

    with pytest.raises(argparse.ArgumentTypeError, match="root slash"):
        ADAPTER._output_argument(str(doubled_canonical))
    with pytest.raises(ADAPTER.CompatibilityError, match="non-canonical"):
        ADAPTER.InputSnapshot().capture(doubled_input, "double-root input")
    with pytest.raises(ADAPTER.CompatibilityError, match="non-canonical"):
        ADAPTER._canonical_absolute(doubled_canonical, "double-root canonical")


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


def publication_fixture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    payload: dict[str, object],
) -> tuple[Path, Path, Path, bytes, str, list[bytes]]:
    authority = tmp_path / "paper02-authority"
    canonical = authority / ADAPTER.ROLE13_RELATIVE_PATH
    canonical.parent.mkdir(parents=True)
    candidate = tmp_path / "role13-candidate.json"
    raw = ADAPTER.canonical_json_bytes(payload)
    candidate.write_bytes(raw)
    candidate.chmod(0o600)
    digest_value = hashlib.sha256(raw).hexdigest()
    live_values = [raw]

    monkeypatch.setattr(ADAPTER, "ROOT", authority)
    monkeypatch.setattr(ADAPTER, "CANONICAL_OUTPUT", canonical)

    def synthetic_live(root: Path) -> bytes:
        assert root == authority
        return live_values[0]

    monkeypatch.setattr(ADAPTER, "_live_compatibility_bytes", synthetic_live)
    return authority, candidate, canonical, raw, digest_value, live_values


def publication_worker(
    queue, candidate: str, digest_value: str, authority: str,
) -> None:
    try:
        receipt = ADAPTER.publish_compatibility_replay(
            candidate_value=candidate,
            expected_sha256=digest_value,
            authority_root_value=authority,
        )
        queue.put(("PASS", receipt))
    except BaseException as error:
        queue.put(("ERROR", type(error).__name__, str(error)))


def test_publication_constants_and_hook_vocabulary_are_frozen() -> None:
    assert ADAPTER.CANONICAL_OUTPUT == ROOT / ADAPTER.ROLE13_RELATIVE_PATH
    assert ADAPTER.PUBLICATION_HOOK_PHASES == {
        "AFTER_STAGE_WRITE",
        "AFTER_STAGE_FILE_FSYNC",
        "AFTER_STAGING_PARENT_FSYNC",
        "BEFORE_TERMINAL_REPLAY",
        "BEFORE_RENAME",
        "AFTER_RENAME",
        "AFTER_DESTINATION_FSYNC",
        "AFTER_PUBLICATION_PARENT_FSYNC",
        "AFTER_POSTPUBLICATION_REPLAY",
    }
    with pytest.raises(ADAPTER.CompatibilityError, match="unknown.*phase"):
        ADAPTER._publication_fault_hook("TYPO_PHASE")


def _captured_candidate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> tuple[Path, bytes]:
    candidate = tmp_path / "role13-verify.json"
    payload = deepcopy(compatibility_payload)
    monkeypatch.setattr(
        ADAPTER, "build_compatibility_object", lambda _snapshot=None: payload
    )
    ADAPTER.capture_compatibility_candidate(str(candidate))
    return candidate, candidate.read_bytes()


def test_exact5_self_verify_receipt_is_closed_and_non_authoritative(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
    live_canonical_role13_is_never_touched: tuple[object, ...],
) -> None:
    candidate, raw = _captured_candidate(
        tmp_path, monkeypatch, compatibility_payload
    )
    receipt = ADAPTER.verify_s0_compatibility_path(candidate)
    assert set(receipt) == ADAPTER.VERIFY_RECEIPT_KEYS
    assert len(receipt) == 5
    assert receipt == {
        "verification_status": "PASS_S0_COMPATIBILITY_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "promotion_authorized": False,
    }
    ADAPTER.validate_verify_receipt(receipt)
    assert_preimage_unchanged(
        CANONICAL_OUTPUT, live_canonical_role13_is_never_touched
    )


def test_role24_independent_verify_accepts_exact_role23_candidate_and_receipt_parity(
    compatibility_payload: dict[str, object],
    live_canonical_role13_is_never_touched: tuple[object, ...],
) -> None:
    release = load_release_builder()
    with tempfile.TemporaryDirectory(
        prefix="a416-role23-role24-", dir="/tmp"
    ) as directory:
        candidate = Path(directory) / "role13.json"
        ADAPTER._secure_exclusive_write(
            candidate, ADAPTER.canonical_json_bytes(compatibility_payload)
        )
        own = ADAPTER.verify_s0_compatibility_path(candidate)
        independent = release.verify_s0_compatibility_path(candidate)
        assert independent == own
        assert set(independent) == ADAPTER.VERIFY_RECEIPT_KEYS
        assert len(tuple(Path(directory).iterdir())) == 1
    assert_preimage_unchanged(
        CANONICAL_OUTPUT, live_canonical_role13_is_never_touched
    )


def test_live_replay_snapshot_pins_all_53_sealed_and_source_inputs() -> None:
    raw, snapshot = ADAPTER._live_compatibility_snapshot(ADAPTER.ROOT)
    assert snapshot.count == 53
    assert raw == ADAPTER.canonical_json_bytes(
        ADAPTER.strict_json_bytes(raw, "live role13 snapshot")
    )
    snapshot.assert_unchanged()


def test_self_verify_rejects_same_byte_source_generation_swap(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
    live_canonical_role13_is_never_touched: tuple[object, ...],
) -> None:
    candidate, raw = _captured_candidate(
        tmp_path, monkeypatch, compatibility_payload
    )
    watched = tmp_path / "synthetic-source.md"
    watched.write_bytes(b"same bytes\n")

    def swapped_generation(_root: Path):
        snapshot = ADAPTER.InputSnapshot()
        snapshot.capture(watched, "synthetic live source")
        replacement = tmp_path / "replacement-source.md"
        replacement.write_bytes(watched.read_bytes())
        os.replace(replacement, watched)
        return raw, snapshot

    monkeypatch.setattr(
        ADAPTER, "_live_compatibility_snapshot", swapped_generation
    )
    with pytest.raises(ADAPTER.CompatibilityError, match="TOCTOU mutation"):
        ADAPTER.verify_s0_compatibility_path(candidate)
    assert_preimage_unchanged(
        CANONICAL_OUTPUT, live_canonical_role13_is_never_touched
    )


@pytest.mark.parametrize(
    "mutation",
    (
        lambda value: value.pop("authority"),
        lambda value: value.__setitem__("extra", None),
        lambda value: value.__setitem__("verification_status", "PASS"),
        lambda value: value.__setitem__("authority", "ROLE23_ADAPTER_PUBLICATION_ONLY"),
        lambda value: value.__setitem__("candidate_sha256", "A" * 64),
        lambda value: value.__setitem__("candidate_sha256", "0" * 63),
        lambda value: value.__setitem__("size_bytes", True),
        lambda value: value.__setitem__("size_bytes", 0),
        lambda value: value.__setitem__("promotion_authorized", 0),
        lambda value: value.__setitem__("promotion_authorized", True),
    ),
)
def test_exact5_self_verify_receipt_rejects_key_literal_and_type_mutations(
    mutation,
) -> None:
    receipt = {
        "verification_status": "PASS_S0_COMPATIBILITY_VERIFY_ONLY",
        "authority": "NON_AUTHORITATIVE_VERIFY_ONLY",
        "candidate_sha256": "0" * 64,
        "size_bytes": 1,
        "promotion_authorized": False,
    }
    mutation(receipt)
    with pytest.raises(ADAPTER.CompatibilityError):
        ADAPTER.validate_verify_receipt(receipt)


def test_self_verify_rejects_same_byte_new_inode_swap_during_semantic_replay(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
    live_canonical_role13_is_never_touched: tuple[object, ...],
) -> None:
    candidate, raw = _captured_candidate(
        tmp_path, monkeypatch, compatibility_payload
    )
    original_live = ADAPTER._live_compatibility_snapshot

    def swap_candidate(root: Path):
        live, snapshot = original_live(root)
        replacement = candidate.with_name("replacement-role13.json")
        replacement.write_bytes(raw)
        replacement.chmod(0o600)
        os.replace(replacement, candidate)
        return live, snapshot

    monkeypatch.setattr(ADAPTER, "_live_compatibility_snapshot", swap_candidate)
    with pytest.raises(ADAPTER.CompatibilityError, match="generation changed"):
        ADAPTER.verify_s0_compatibility_path(candidate)
    assert_preimage_unchanged(
        CANONICAL_OUTPUT, live_canonical_role13_is_never_touched
    )


@pytest.mark.parametrize("kind", ("wrong_mode", "hardlink", "symlink", "fifo"))
def test_self_verify_candidate_reader_rejects_namespace_file_attacks_without_blocking(
    kind: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
    live_canonical_role13_is_never_touched: tuple[object, ...],
) -> None:
    candidate, raw = _captured_candidate(
        tmp_path, monkeypatch, compatibility_payload
    )
    if kind == "wrong_mode":
        candidate.chmod(0o644)
    elif kind == "hardlink":
        alias = candidate.with_name("hardlink-role13.json")
        os.link(candidate, alias)
    elif kind == "symlink":
        target = candidate.with_name("target-role13.json")
        candidate.rename(target)
        candidate.symlink_to(target)
    else:
        candidate.unlink()
        os.mkfifo(candidate, 0o600)
    with pytest.raises(ADAPTER.CompatibilityError):
        ADAPTER.verify_s0_compatibility_path(candidate)
    assert_preimage_unchanged(
        CANONICAL_OUTPUT, live_canonical_role13_is_never_touched
    )


def test_self_verify_rejects_noncompact_stale_and_lexical_alias_candidates(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
    live_canonical_role13_is_never_touched: tuple[object, ...],
) -> None:
    candidate, raw = _captured_candidate(
        tmp_path, monkeypatch, compatibility_payload
    )
    candidate.write_bytes(raw[:-1] + b" \n")
    with pytest.raises(ADAPTER.CompatibilityError, match="CJ_COMPACT_V1"):
        ADAPTER.verify_s0_compatibility_path(candidate)
    candidate.write_bytes(raw)
    monkeypatch.setattr(
        ADAPTER,
        "_live_compatibility_snapshot",
        lambda _root: (b"{}\n", ADAPTER.InputSnapshot()),
    )
    with pytest.raises(ADAPTER.CompatibilityError, match="differs from live"):
        ADAPTER.verify_s0_compatibility_path(candidate)
    with pytest.raises(ADAPTER.CompatibilityError, match="root slash|non-canonical"):
        ADAPTER.verify_s0_compatibility_path("/" + str(candidate))
    assert_preimage_unchanged(
        CANONICAL_OUTPUT, live_canonical_role13_is_never_touched
    )


def test_capture_receipt_is_closed_compact_and_non_authorizing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    output = tmp_path / "captured-role13.json"
    payload = deepcopy(compatibility_payload)
    monkeypatch.setattr(
        ADAPTER, "build_compatibility_object", lambda _snapshot=None: payload
    )
    receipt = ADAPTER.capture_compatibility_candidate(str(output))
    assert set(receipt) == {
        "schema_version", "protocol_id", "artifact_role", "artifact_status",
        "authority", "candidate_path", "candidate_sha256", "size_bytes",
        "mode", "nlink", "serializer", "scientific_licensing_enabled",
        "production_authorized", "scientific_dispatch_performed",
        "component_status", "milestone_status", "theorem_status", "final_status",
    }
    assert len(receipt) == 18
    raw = ADAPTER.canonical_json_bytes(payload)
    assert receipt == {
        "schema_version": 1,
        "protocol_id": ADAPTER.PROTOCOL_ID,
        "artifact_role": "TEMP_S0_COMPATIBILITY_CANDIDATE_RECEIPT",
        "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
        "authority": "NON_AUTHORITATIVE_CAPTURE_ONLY",
        "candidate_path": str(output),
        "candidate_sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "mode": "0600",
        "nlink": 1,
        "serializer": "CJ_COMPACT_V1",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    assert output.read_bytes() == raw
    assert stat.S_IMODE(output.stat().st_mode) == 0o600
    assert output.stat().st_nlink == 1
    assert ADAPTER.canonical_json_bytes(receipt).endswith(b"\n")


@pytest.mark.parametrize(
    "key,value",
    (
        ("schema_version", True),
        ("protocol_id", "R401-VAL-L3-A1-V2"),
        ("authority", "ROLE23_ADAPTER_PUBLICATION_ONLY"),
        ("candidate_path", "tmp/role13.json"),
        ("candidate_sha256", "A" * 64),
        ("size_bytes", True),
        ("mode", 0o600),
        ("scientific_licensing_enabled", True),
        ("component_status", "PASS"),
    ),
)
def test_capture_receipt_validator_rejects_literal_path_and_type_mutations(
    key: str, value: object,
) -> None:
    receipt = {
        "schema_version": 1,
        "protocol_id": ADAPTER.PROTOCOL_ID,
        "artifact_role": "TEMP_S0_COMPATIBILITY_CANDIDATE_RECEIPT",
        "artifact_status": "CAPTURED_VALIDATED_TEMP_ONLY",
        "authority": "NON_AUTHORITATIVE_CAPTURE_ONLY",
        "candidate_path": "/tmp/role13.json",
        "candidate_sha256": "0" * 64,
        "size_bytes": 1,
        "mode": "0600",
        "nlink": 1,
        "serializer": "CJ_COMPACT_V1",
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    receipt[key] = value
    with pytest.raises(ADAPTER.CompatibilityError):
        ADAPTER.validate_capture_receipt(receipt)


def test_publication_success_receipt_is_closed_write_once_and_non_authorizing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    before = ADAPTER._publication_file_identity(candidate.stat())
    receipt = ADAPTER.publish_compatibility_replay(
        candidate_value=str(candidate),
        expected_sha256=digest_value,
        authority_root_value=str(authority),
    )
    assert set(receipt) == {
        "schema_version", "protocol_id", "artifact_role", "artifact_status",
        "authority", "candidate_path", "canonical_path",
        "compatibility_sha256", "size_bytes", "mode", "nlink", "serializer",
        "publication_method", "independent_verification_performed",
        "scientific_licensing_enabled", "production_authorized",
        "scientific_dispatch_performed", "component_status", "milestone_status",
        "theorem_status", "final_status",
    }
    assert len(receipt) == 21
    assert receipt == {
        "schema_version": 1,
        "protocol_id": ADAPTER.PROTOCOL_ID,
        "artifact_role": "S0_COMPATIBILITY_PUBLICATION_RECEIPT",
        "artifact_status": "PUBLISHED_WRITE_ONCE_NON_LICENSING",
        "authority": "ROLE23_ADAPTER_PUBLICATION_ONLY",
        "candidate_path": str(candidate),
        "canonical_path": str(canonical),
        "compatibility_sha256": digest_value,
        "size_bytes": len(raw),
        "mode": "0644",
        "nlink": 1,
        "serializer": "CJ_COMPACT_V1",
        "publication_method": "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1",
        "independent_verification_performed": False,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    assert canonical.read_bytes() == candidate.read_bytes() == raw
    assert stat.S_IMODE(canonical.stat().st_mode) == 0o644
    assert canonical.stat().st_nlink == 1
    assert ADAPTER._publication_file_identity(candidate.stat()) == before
    assert not list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))
    with pytest.raises(ADAPTER.CompatibilityError, match="already exists"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate),
            expected_sha256=digest_value,
            authority_root_value=str(authority),
        )


@pytest.mark.parametrize(
    "key,value",
    (
        ("schema_version", True),
        ("artifact_status", "PUBLISHED"),
        ("authority", "ROLE24_RELEASE_PROVENANCE_PUBLICATION_ONLY"),
        ("candidate_path", "tmp/role13.json"),
        ("canonical_path", "/tmp//role13.json"),
        ("compatibility_sha256", "A" * 64),
        ("size_bytes", True),
        ("mode", 0o644),
        ("publication_method", "REPLACE"),
        ("independent_verification_performed", True),
        ("scientific_licensing_enabled", True),
        ("final_status", "PASS"),
    ),
)
def test_exact21_publication_receipt_validator_rejects_authority_mutations(
    key: str, value: object,
) -> None:
    receipt = {
        "schema_version": 1,
        "protocol_id": ADAPTER.PROTOCOL_ID,
        "artifact_role": "S0_COMPATIBILITY_PUBLICATION_RECEIPT",
        "artifact_status": "PUBLISHED_WRITE_ONCE_NON_LICENSING",
        "authority": "ROLE23_ADAPTER_PUBLICATION_ONLY",
        "candidate_path": "/tmp/candidate.json",
        "canonical_path": "/tmp/canonical.json",
        "compatibility_sha256": "0" * 64,
        "size_bytes": 1,
        "mode": "0644",
        "nlink": 1,
        "serializer": "CJ_COMPACT_V1",
        "publication_method": "SAME_PARENT_RENAMEAT2_NOREPLACE_FSYNC_V1",
        "independent_verification_performed": False,
        "scientific_licensing_enabled": False,
        "production_authorized": False,
        "scientific_dispatch_performed": False,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
    }
    receipt[key] = value
    with pytest.raises(ADAPTER.CompatibilityError):
        ADAPTER.validate_publication_receipt(receipt)


@pytest.mark.parametrize("kind", ("identical", "different", "directory", "symlink", "fifo"))
def test_publication_rejects_every_existing_destination_without_blocking(
    kind: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    if kind == "identical":
        canonical.write_bytes(raw)
    elif kind == "different":
        canonical.write_bytes(b"foreign\n")
    elif kind == "directory":
        canonical.mkdir()
    elif kind == "symlink":
        canonical.symlink_to(candidate)
    else:
        os.mkfifo(canonical, 0o644)
    before = os.lstat(canonical)
    with pytest.raises(ADAPTER.CompatibilityError, match="already exists"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate),
            expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    after = os.lstat(canonical)
    assert (after.st_dev, after.st_ino, after.st_mode) == (
        before.st_dev, before.st_ino, before.st_mode
    )
    assert candidate.read_bytes() == raw


@pytest.mark.parametrize(
    "raw,mode,match",
    (
        (b"", 0o600, "size outside"),
        (b"x" * (1024 * 1024 + 1), 0o600, "size outside"),
        (b"{}\n", 0o600, "missing"),
        (b'{"x": 1}\n', 0o600, "CJ_COMPACT"),
        (b"{}\n", 0o644, "mode 0600"),
    ),
)
def test_publication_rejects_size_schema_serializer_and_candidate_mode(
    raw: bytes,
    mode: int,
    match: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, _, _, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    candidate.write_bytes(raw)
    candidate.chmod(mode)
    with pytest.raises(ADAPTER.CompatibilityError, match=match):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate),
            expected_sha256=hashlib.sha256(raw).hexdigest(),
            authority_root_value=str(authority),
        )
    assert not canonical.exists()


def test_publication_rejects_symlink_hardlink_hash_path_and_authority_aliases(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    with pytest.raises(ADAPTER.CompatibilityError, match="expected.*SHA|lowercase"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256="A" * 64,
            authority_root_value=str(authority),
        )
    with pytest.raises(ADAPTER.CompatibilityError, match="differs from expected"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256="0" * 64,
            authority_root_value=str(authority),
        )
    with pytest.raises(ADAPTER.CompatibilityError, match="exact live"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority.parent),
        )
    with pytest.raises(ADAPTER.CompatibilityError, match="absolute|root slash"):
        ADAPTER.publish_compatibility_replay(
            candidate_value="relative.json", expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    hardlink = candidate.with_name("candidate-hardlink.json")
    os.link(candidate, hardlink)
    with pytest.raises(ADAPTER.CompatibilityError, match="hard-link"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    hardlink.unlink()
    target = candidate.with_name("candidate-target.json")
    candidate.rename(target)
    candidate.symlink_to(target)
    with pytest.raises(ADAPTER.CompatibilityError, match="regular file|replay failed"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert target.read_bytes() == raw
    assert not canonical.exists()


def test_stale_live_replay_and_same_byte_candidate_inode_swap_fail_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, live_values = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    live_values[0] = raw + b" "
    with pytest.raises(ADAPTER.CompatibilityError, match="stale"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert not canonical.exists()
    live_values[0] = raw

    def swap_candidate(phase: str) -> None:
        if phase == "BEFORE_RENAME":
            replacement = candidate.with_name("same-byte-new-inode.json")
            replacement.write_bytes(raw)
            replacement.chmod(0o600)
            os.replace(replacement, candidate)

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", swap_candidate)
    with pytest.raises(ADAPTER.CompatibilityError, match="candidate changed"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert candidate.read_bytes() == raw
    assert not canonical.exists()
    assert not list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))


def test_terminal_source_binding_drift_is_detected_before_rename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, live_values = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )

    def drift_source(phase: str) -> None:
        if phase == "BEFORE_RENAME":
            live_values[0] = raw + b"source-doc-drift"

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", drift_source)
    with pytest.raises(ADAPTER.CompatibilityError, match="changed at publication"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert not canonical.exists()
    assert candidate.read_bytes() == raw
    assert not list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))


def test_stage_name_collision_skips_and_never_touches_foreign_entry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    foreign_name = ADAPTER.PUBLICATION_STAGE_PREFIX + "0" * 32
    winner_name = ADAPTER.PUBLICATION_STAGE_PREFIX + "1" * 32
    foreign = canonical.parent / foreign_name
    foreign.write_bytes(b"foreign-stage\n")
    foreign.chmod(0o644)
    names = iter((foreign_name, winner_name))
    monkeypatch.setattr(ADAPTER, "_publication_stage_basename", lambda: next(names))
    receipt = ADAPTER.publish_compatibility_replay(
        candidate_value=str(candidate), expected_sha256=digest_value,
        authority_root_value=str(authority),
    )
    assert receipt["compatibility_sha256"] == digest_value
    assert canonical.read_bytes() == raw
    assert foreign.read_bytes() == b"foreign-stage\n"


def test_two_process_publication_has_exactly_one_winner_and_no_owned_residue(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    context = multiprocessing.get_context("fork")
    queue = context.Queue()
    processes = [
        context.Process(
            target=publication_worker,
            args=(queue, str(candidate), digest_value, str(authority)),
        )
        for _ in range(2)
    ]
    for process in processes:
        process.start()
    for process in processes:
        process.join(15)
        assert process.exitcode == 0
    results = [queue.get(timeout=2) for _ in processes]
    assert [item[0] for item in results].count("PASS") == 1
    assert [item[0] for item in results].count("ERROR") == 1
    error = next(item for item in results if item[0] == "ERROR")
    assert "already exists" in error[2] or "collided" in error[2]
    assert canonical.read_bytes() == candidate.read_bytes() == raw
    assert not list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))


def test_normal_pre_rename_error_cleans_only_owned_stage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )

    def ordinary_failure(phase: str) -> None:
        if phase == "BEFORE_TERMINAL_REPLAY":
            raise RuntimeError("ordinary injected failure")

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", ordinary_failure)
    with pytest.raises(RuntimeError, match="ordinary injected"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert not canonical.exists()
    assert candidate.read_bytes() == raw
    assert not list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))


def test_cleanup_inode_guard_never_unlinks_replacement_stage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    replacement: list[Path] = []

    def replace_stage(phase: str) -> None:
        if phase == "BEFORE_TERMINAL_REPLAY":
            stages = list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))
            assert len(stages) == 1
            stages[0].unlink()
            stages[0].write_bytes(b"foreign-replacement\n")
            stages[0].chmod(0o644)
            replacement.append(stages[0])

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", replace_stage)
    with pytest.raises(ADAPTER.CompatibilityError, match="refused to unlink"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert not canonical.exists()
    assert len(replacement) == 1
    assert replacement[0].read_bytes() == b"foreign-replacement\n"
    assert candidate.read_bytes() == raw


@pytest.mark.parametrize(
    "crash_phase",
    (
        "AFTER_STAGE_WRITE",
        "AFTER_STAGE_FILE_FSYNC",
        "AFTER_STAGING_PARENT_FSYNC",
        "BEFORE_TERMINAL_REPLAY",
        "BEFORE_RENAME",
    ),
)
def test_pre_rename_crash_residue_is_harmless_and_retry_uses_new_stage(
    crash_phase: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    original_hook = ADAPTER._publication_fault_hook

    def crash(phase: str) -> None:
        if phase == crash_phase:
            raise ADAPTER.SyntheticCompatibilityPublicationCrash(phase)
        original_hook(phase)

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", crash)
    with pytest.raises(ADAPTER.SyntheticCompatibilityPublicationCrash):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    residue = list(canonical.parent.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))
    assert len(residue) == 1
    assert residue[0].read_bytes() == raw
    assert stat.S_IMODE(residue[0].stat().st_mode) == 0o644
    assert not canonical.exists()
    assert candidate.read_bytes() == raw

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", original_hook)
    receipt = ADAPTER.publish_compatibility_replay(
        candidate_value=str(candidate), expected_sha256=digest_value,
        authority_root_value=str(authority),
    )
    assert receipt["compatibility_sha256"] == digest_value
    assert canonical.read_bytes() == raw
    assert residue[0].read_bytes() == raw


@pytest.mark.parametrize(
    "failure_phase",
    (
        "AFTER_RENAME",
        "AFTER_DESTINATION_FSYNC",
        "AFTER_PUBLICATION_PARENT_FSYNC",
        "AFTER_POSTPUBLICATION_REPLAY",
    ),
)
def test_post_rename_failure_never_rolls_back_and_retry_rejects(
    failure_phase: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    original_hook = ADAPTER._publication_fault_hook

    def fail(phase: str) -> None:
        if phase == failure_phase:
            raise RuntimeError(f"post-rename failure: {phase}")
        original_hook(phase)

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", fail)
    with pytest.raises(RuntimeError, match="post-rename failure"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert canonical.read_bytes() == candidate.read_bytes() == raw
    assert stat.S_IMODE(canonical.stat().st_mode) == 0o644
    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", original_hook)
    with pytest.raises(ADAPTER.CompatibilityError, match="already exists"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )


def test_pre_rename_parent_swap_is_detected_and_owned_stage_is_cleaned(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    parent = canonical.parent
    backup = parent.with_name(parent.name + ".swapped")

    def swap_parent(phase: str) -> None:
        if phase == "BEFORE_RENAME":
            parent.rename(backup)
            parent.mkdir()

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", swap_parent)
    with pytest.raises(ADAPTER.CompatibilityError, match="namespace changed"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert not canonical.exists()
    assert not (backup / canonical.name).exists()
    assert not list(backup.glob(ADAPTER.PUBLICATION_STAGE_PREFIX + "*"))
    assert candidate.read_bytes() == raw


@pytest.mark.parametrize("swap_phase", ("AFTER_RENAME", "AFTER_PUBLICATION_PARENT_FSYNC"))
def test_post_rename_parent_swap_preserves_pinned_canonical_without_misattribution(
    swap_phase: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    compatibility_payload: dict[str, object],
) -> None:
    authority, candidate, canonical, raw, digest_value, _ = publication_fixture(
        tmp_path, monkeypatch, compatibility_payload
    )
    parent = canonical.parent
    backup = parent.with_name(parent.name + ".postrename")
    original_hook = ADAPTER._publication_fault_hook

    def swap_parent(phase: str) -> None:
        if phase == swap_phase:
            parent.rename(backup)
            parent.mkdir()
        original_hook(phase)

    monkeypatch.setattr(ADAPTER, "_publication_fault_hook", swap_parent)
    with pytest.raises(ADAPTER.CompatibilityError, match="namespace changed"):
        ADAPTER.publish_compatibility_replay(
            candidate_value=str(candidate), expected_sha256=digest_value,
            authority_root_value=str(authority),
        )
    assert not canonical.exists()
    pinned_canonical = backup / canonical.name
    assert pinned_canonical.read_bytes() == raw
    assert stat.S_IMODE(pinned_canonical.stat().st_mode) == 0o644
    assert candidate.read_bytes() == raw


def test_capture_and_publication_cli_exact_compact_stdout_and_empty_stderr(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capfd: pytest.CaptureFixture[str],
    compatibility_payload: dict[str, object],
) -> None:
    output = tmp_path / "cli-candidate.json"
    payload = deepcopy(compatibility_payload)
    monkeypatch.setattr(
        ADAPTER, "build_compatibility_object", lambda _snapshot=None: payload
    )
    assert ADAPTER.main([
        "--capture-s0-compatibility", "--output", str(output)
    ]) == 0
    stdout, stderr = capfd.readouterr()
    assert stderr == ""
    capture_receipt = json.loads(stdout)
    assert len(capture_receipt) == 18
    assert stdout.encode("utf-8") == ADAPTER.canonical_json_bytes(capture_receipt)

    assert ADAPTER.main([
        "--verify-s0-compatibility", str(output)
    ]) == 0
    stdout, stderr = capfd.readouterr()
    assert stderr == ""
    verify_receipt = json.loads(stdout)
    assert set(verify_receipt) == ADAPTER.VERIFY_RECEIPT_KEYS
    assert stdout.encode("utf-8") == ADAPTER.canonical_json_bytes(verify_receipt)

    raw = output.read_bytes()
    digest_value = hashlib.sha256(raw).hexdigest()
    authority = tmp_path / "cli-authority"
    canonical = authority / ADAPTER.ROLE13_RELATIVE_PATH
    canonical.parent.mkdir(parents=True)
    monkeypatch.setattr(ADAPTER, "ROOT", authority)
    monkeypatch.setattr(ADAPTER, "CANONICAL_OUTPUT", canonical)
    monkeypatch.setattr(ADAPTER, "_live_compatibility_bytes", lambda root: raw)
    assert ADAPTER.main([
        "--publish-s0-compatibility",
        "--candidate", str(output),
        "--expected-sha256", digest_value,
        "--authority-root", str(authority),
    ]) == 0
    stdout, stderr = capfd.readouterr()
    assert stderr == ""
    publish_receipt = json.loads(stdout)
    assert len(publish_receipt) == 21
    assert stdout.encode("utf-8") == ADAPTER.canonical_json_bytes(publish_receipt)
    assert canonical.read_bytes() == raw


@pytest.mark.parametrize(
    "argv",
    (
        [],
        ["--capture-s0-compatibility", "--publish-s0-compatibility"],
        ["--capture-s0-compatibility", "--verify-s0-compatibility", "/tmp/x.json"],
        ["--publish-s0-compatibility", "--verify-s0-compatibility", "/tmp/x.json"],
        ["--verify-s0-compatibility", "/tmp/x.json", "--output", "/tmp/y.json"],
        ["--capture-s0-compatibility"],
        ["--capture-s0-compatibility", "--output", "/tmp/x.json", "--candidate", "/tmp/y.json"],
        ["--publish-s0-compatibility"],
        ["--publish-s0-compatibility", "--output", "/tmp/x.json"],
    ),
)
def test_cli_capture_publish_exact_xor_is_fail_closed(
    argv: list[str], capfd: pytest.CaptureFixture[str]
) -> None:
    assert ADAPTER.main(argv) == 1
    stdout, stderr = capfd.readouterr()
    assert stdout == ""
    assert stderr.startswith("ERROR: CompatibilityError:")


@pytest.mark.parametrize(
    "mutation",
    (
        lambda payload: payload["matrix"].__setitem__("authority", "SMUGGLED"),
        lambda payload: payload["source_bindings"].__setitem__("authority", "0" * 64),
        lambda payload: payload["role_sets"]["static_proof_entries"][0].__setitem__(
            "production_authorized", True
        ),
    ),
)
def test_recursive_closed_schemas_reject_authority_smuggling(
    compatibility_payload: dict[str, object], mutation,
) -> None:
    payload = deepcopy(compatibility_payload)
    mutation(payload)
    with pytest.raises(ADAPTER.CompatibilityError, match="mismatch|extra"):
        ADAPTER.validate_compatibility_output(payload)
