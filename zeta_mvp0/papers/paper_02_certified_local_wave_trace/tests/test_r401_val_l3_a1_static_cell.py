from __future__ import annotations

import importlib.util
import json
import sys
from argparse import Namespace
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/evaluate_r401_val_l3_a1_static_cell.py"


def load_module():
    name = "evaluate_r401_val_l3_a1_static_cell_tested"
    spec = importlib.util.spec_from_file_location(name, SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def module():
    return load_module()


def frozen_argv(module, output: Path, **overrides: object) -> list[str]:
    plan_record = module.load_plan()["S000"]
    values: dict[str, object] = {
        "slab_id": "S000",
        "precision_bits": 128,
        "epsilon_lower": "0.0000",
        "epsilon_upper": "0.0021",
        "matrix_id": "1" * 64,
        "freeze_sha256": "2" * 64,
        "run_config_sha256": "3" * 64,
        "plan_record_sha256": module.plan_record_sha256(plan_record),
        "max_depth": 24,
        "max_nodes_per_tree": 250000,
        "max_nodes_per_cell": 1000000,
        "output": str(output),
    }
    values.update(overrides)
    return [
        "--slab-id",
        str(values["slab_id"]),
        "--precision-bits",
        str(values["precision_bits"]),
        "--epsilon-lower",
        str(values["epsilon_lower"]),
        "--epsilon-upper",
        str(values["epsilon_upper"]),
        "--matrix-id",
        str(values["matrix_id"]),
        "--freeze-sha256",
        str(values["freeze_sha256"]),
        "--run-config-sha256",
        str(values["run_config_sha256"]),
        "--plan-record-sha256",
        str(values["plan_record_sha256"]),
        "--max-depth",
        str(values["max_depth"]),
        "--max-nodes-per-tree",
        str(values["max_nodes_per_tree"]),
        "--max-nodes-per-cell",
        str(values["max_nodes_per_cell"]),
        "--output",
        str(values["output"]),
    ]


def test_source_is_one_cell_producer_without_s0_import_or_telemetry() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    assert "run_r401_val_l3_phase_tube_smoke" not in source
    assert "REPRESENTATIVE_SLABS" not in source
    assert "wall_seconds" not in source
    assert "time.monotonic" not in source
    assert 'PROTOCOL_ID = "R401-VAL-L3-A1"' in source
    assert "scientific_licensing_enabled" in source


@pytest.mark.parametrize(
    "raw",
    [
        '{"x":1,"x":2}',
        '{"x":NaN}',
        '{"x":Infinity}',
        '{"x":1e400}',
    ],
)
def test_strict_json_rejects_duplicate_and_nonfinite(module, tmp_path: Path, raw: str) -> None:
    path = tmp_path / "bad.json"
    path.write_text(raw, encoding="utf-8")
    with pytest.raises(module.StaticCellContractError):
        module.strict_json_load(path)


def test_exact_plan_matrix_and_frozen_input_binding(module, tmp_path: Path) -> None:
    plan = module.load_plan()
    assert list(plan) == [f"S{index:03d}" for index in range(51)]
    parent = tmp_path / "stage"
    parent.mkdir()
    args = module.parse_args(frozen_argv(module, (parent / "proof.json").absolute()))
    cell, record = module.validate_frozen_input(args)
    assert cell.slab_id == "S000"
    assert type(cell.precision_bits) is int and cell.precision_bits == 128
    assert cell.plan_record_sha256 == module.plan_record_sha256(record)


def test_plan_semantics_and_binding_share_one_pinned_snapshot(
    module, monkeypatch: pytest.MonkeyPatch
) -> None:
    original_read = module.read_pinned_regular_bytes
    accepted_raw = original_read(module.PLAN)
    mutated = json.loads(accepted_raw)
    mutated["slabs"][0]["epsilon_lower"] = "0.0001"
    later_raw = module.canonical_json_bytes(mutated)
    plan_reads = 0

    def staged_read(path: Path) -> bytes:
        nonlocal plan_reads
        if path == module.PLAN:
            plan_reads += 1
            return accepted_raw if plan_reads == 1 else later_raw
        return original_read(path)

    monkeypatch.setattr(module, "read_pinned_regular_bytes", staged_read)
    record = module.load_plan()["S000"]
    bindings = module.source_bindings(record)

    assert plan_reads == 1
    assert record["epsilon_lower"] == "0.0000"
    assert bindings["l1_final_plan_sha256"] == module.sha256_bytes(accepted_raw)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("slab_id", "S051"),
        ("epsilon_lower", "0"),
        ("epsilon_upper", "0.0022"),
        ("matrix_id", "A" * 64),
        ("plan_record_sha256", "0" * 64),
        ("max_depth", 0),
        ("max_nodes_per_tree", -1),
        ("max_nodes_per_cell", 100),
    ],
)
def test_frozen_input_mutations_fail_closed(
    module, tmp_path: Path, field: str, value: object
) -> None:
    parent = tmp_path / "stage"
    parent.mkdir()
    args = module.parse_args(frozen_argv(module, (parent / "proof.json").absolute()))
    setattr(args, field, value)
    with pytest.raises(module.StaticCellContractError):
        module.validate_frozen_input(args)


def test_cell_budget_distinguishes_tree_cell_and_depth(module) -> None:
    budget = module.CellBudget(max_depth=2, max_nodes_per_tree=2, max_nodes_per_cell=3)
    budget.consume(tree_id="ANGLE", tree_nodes=0, depth=0)
    budget.consume(tree_id="ANGLE", tree_nodes=1, depth=1)
    with pytest.raises(module.StaticCellLimit) as tree_error:
        budget.consume(tree_id="ANGLE", tree_nodes=2, depth=2)
    assert tree_error.value.status == "STATIC_UNRESOLVED_NODE_BUDGET"
    assert tree_error.value.details["scope"] == "tree"

    cell_budget = module.CellBudget(
        max_depth=2, max_nodes_per_tree=10, max_nodes_per_cell=1
    )
    cell_budget.consume(tree_id="ANGLE", tree_nodes=0, depth=0)
    with pytest.raises(module.StaticCellLimit) as cell_error:
        cell_budget.consume(tree_id="SECTION_LOW", tree_nodes=0, depth=0)
    assert cell_error.value.details["scope"] == "cell"

    depth_budget = module.CellBudget(
        max_depth=1, max_nodes_per_tree=10, max_nodes_per_cell=10
    )
    with pytest.raises(module.StaticCellLimit) as depth_error:
        depth_budget.consume(tree_id="ANGLE", tree_nodes=0, depth=2)
    assert depth_error.value.status == "STATIC_UNRESOLVED_DEPTH"


def test_write_once_rejects_overwrite_and_symlink_parent(module, tmp_path: Path) -> None:
    parent = tmp_path / "stage"
    parent.mkdir()
    output = parent / "proof.json"
    module.write_once(output, b"{}\n")
    with pytest.raises(FileExistsError):
        module.write_once(output, b"different\n")
    target = tmp_path / "target"
    target.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(target, target_is_directory=True)
    with pytest.raises(module.StaticCellContractError):
        module.write_once(alias / "proof.json", b"{}\n")


def test_mock_only_cli_pass_is_canonical_and_write_once(
    module, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    parent = tmp_path / "stage"
    parent.mkdir()
    output = (parent / "proof.json").absolute()

    def fake_evaluate(cell, _record):
        payload = module.common_payload(cell, module.PASS_STATUS)
        payload.update(
            {
                "proof_complete": True,
                "outer_containment": {"all_pass": True},
                "trees": [],
                "counts": {
                    "tree_count": 0,
                    "node_count": 0,
                    "internal_count": 0,
                    "terminal_count": 0,
                    "unresolved_count": 0,
                    "maximum_depth": 0,
                },
                "source_bindings": {},
                "proof_content_hash_definition": (
                    "sha256(canonical_json(proof_without_proof_content_sha256))"
                ),
            }
        )
        payload["proof_content_sha256"] = module.sha256_bytes(
            module.canonical_json_bytes(payload)
        )
        return payload

    monkeypatch.setattr(module, "evaluate_cell", fake_evaluate)
    argv = frozen_argv(module, output)
    assert module.main(argv) == 0
    raw = output.read_bytes()
    payload = json.loads(raw)
    assert raw == module.canonical_json_bytes(payload)
    assert payload["evaluator_status"] == "STATIC_CELL_CERTIFIED"
    assert payload["authority"] == "PRODUCER_ONLY"
    assert payload["scientific_licensing_enabled"] is False
    assert payload["component_status"] is None
    assert payload["milestone_status"] is None
    assert payload["theorem_status"] is None
    assert payload["final_status"] is None
    assert module.main(argv) == 5
    assert output.read_bytes() == raw


def test_mock_limit_maps_only_to_unresolved_exit_two(
    module, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    parent = tmp_path / "stage"
    parent.mkdir()
    output = (parent / "proof.json").absolute()

    def fake_limit(_cell, _record):
        raise module.StaticCellLimit(
            "STATIC_UNRESOLVED_NODE_BUDGET",
            {"scope": "cell", "limit": 1, "consumed_before_node": 1},
        )

    monkeypatch.setattr(module, "evaluate_cell", fake_limit)
    assert module.main(frozen_argv(module, output)) == 2
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["evaluator_status"] == "STATIC_UNRESOLVED_NODE_BUDGET"
    assert payload["proof_complete"] is False
    assert payload["component_status"] is None
    assert payload["final_status"] is None


def test_invalid_echo_returns_contract_code_without_artifact(module, tmp_path: Path) -> None:
    parent = tmp_path / "stage"
    parent.mkdir()
    output = (parent / "proof.json").absolute()
    argv = frozen_argv(module, output, epsilon_upper="0.0022")
    assert module.main(argv) == 5
    assert not output.exists()


def test_common_payload_has_exact_non_authority_boundary(module, tmp_path: Path) -> None:
    cell = module.FrozenStaticInput(
        slab_id="S000",
        precision_bits=128,
        epsilon_lower="0.0000",
        epsilon_upper="0.0021",
        matrix_id="1" * 64,
        freeze_sha256="2" * 64,
        run_config_sha256="3" * 64,
        plan_record_sha256="4" * 64,
        max_depth=24,
        max_nodes_per_tree=250000,
        max_nodes_per_cell=1000000,
        output=tmp_path / "proof.json",
    )
    payload = module.common_payload(cell, "STATIC_UNRESOLVED_DEPTH")
    assert set(
        key
        for key in payload
        if key in {"component_status", "milestone_status", "theorem_status", "final_status"}
    ) == {"component_status", "milestone_status", "theorem_status", "final_status"}
    assert all(
        payload[key] is None
        for key in ("component_status", "milestone_status", "theorem_status", "final_status")
    )
    assert "Hilbert-Polya" in payload["claim_boundary"]


def test_namespace_tables_are_closed(module) -> None:
    assert module.PASS_STATUS == "STATIC_CELL_CERTIFIED"
    assert module.PROTOCOL_ID == "R401-VAL-L3-A1"
    assert module.ARTIFACT_ROLE == "STATIC_CELL_PROOF"
    assert module.AUTHORITY == "PRODUCER_ONLY"


def test_formal_tree_order_matches_protocol(module) -> None:
    assert tuple(module.SECTION_ROOTS) == (
        "SECTION_LOW",
        "SECTION_HIGH",
        "SECTION_WINDOW",
    )


def test_upstream_l1_replay_rejects_extra_authority_field(
    module, monkeypatch: pytest.MonkeyPatch
) -> None:
    payloads = {
        path: module.strict_json_image(path)[0]
        for path in (
            module.L1_SUMMARY,
            module.L1_MANIFEST,
            module.L1_CHECKER,
            module.L1_POSTCHECK,
            module.L1_RELEASE,
        )
    }
    payloads[module.L1_SUMMARY] = dict(payloads[module.L1_SUMMARY])
    payloads[module.L1_SUMMARY]["theorem_status"] = "FORGED_UNAUTHORIZED"
    monkeypatch.setattr(
        module,
        "strict_json_image",
        lambda path: (payloads[path], module.canonical_json_bytes(payloads[path])),
    )
    with pytest.raises(module.StaticCellContractError, match="schema mismatch"):
        module.validate_l1_release_chain()


@pytest.mark.parametrize("value", ["+128", "0128", "128.0", "129"])
def test_precision_cli_rejects_noncanonical_aliases(module, value: str) -> None:
    with pytest.raises(Exception):
        module.canonical_precision(value)


@pytest.mark.parametrize("value", ["0", "-1", "+1", "01", "1.0"])
def test_positive_integer_cli_rejects_noncanonical_aliases(module, value: str) -> None:
    with pytest.raises(Exception):
        module.canonical_positive_int(value)


@pytest.mark.parametrize(
    "value",
    ["relative/proof.json", "/tmp//stage/proof.json", "/tmp/../proof.json"],
)
def test_output_cli_rejects_lexical_aliases(module, value: str) -> None:
    with pytest.raises(Exception):
        module.lexical_absolute_output(value)
