from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_r401_val_l2_all_slabs_independent.py"
SPEC = importlib.util.spec_from_file_location("r401_val_l2_all_slabs_checker", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def dump_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(MODULE.canonical_json_bytes(payload))


def interval_text(value: tuple[Fraction, Fraction]) -> list[str]:
    return [MODULE.decimal_fraction_text(value[0]), MODULE.decimal_fraction_text(value[1])]


def box_text(box: dict[str, tuple[Fraction, Fraction]]) -> dict[str, list[str]]:
    return {coordinate: interval_text(box[coordinate]) for coordinate in MODULE.COORDINATES}


def synthetic_plan_record() -> dict[str, object]:
    return {
        "slab_id": "S000",
        "epsilon_lower": "0",
        "epsilon_upper": "0.0021",
        "center": {
            "q_slow": "0",
            "q_fast": "0.145",
            "p_slow": "0",
            "period": "0.665",
        },
        "root_radii": {
            "q_slow": "0.01",
            "q_fast": "0.015",
            "p_slow": "0.04",
            "period": "0.015",
        },
    }


def task_payload(
    *,
    node_id: str = "C0L",
    parent_id: str | None = None,
    depth: int = 0,
    box: dict[str, tuple[Fraction, Fraction]] | None = None,
) -> dict[str, object]:
    selected_box = box or {
        "q_slow": (Fraction(-1), Fraction(1)),
        "q_fast": (Fraction(49, 100), Fraction(51, 100)),
        "p_slow": (Fraction(-1), Fraction(1)),
        "period": (Fraction(-1), Fraction(1)),
    }
    return {
        "tree": {"precision_bits": 128, "slab_id": "S000"},
        "node_id": node_id,
        "parent_id": parent_id,
        "depth": depth,
        "epsilon": ["0", "0"],
        "box": box_text(selected_box),
        "run_config_sha256": "a" * 64,
        "evaluator_source_sha256": "b" * 64,
        "evaluator_binary_sha256": "c" * 64,
    }


def synthetic_return_transcript(*, excluded: bool = False) -> str:
    first = "[2,2]" if excluded else "[0,0]"
    k_first = "[-3,-1]" if excluded else "[-1,1]"
    selected = "0" if excluded else "-1"
    status = "RETURN_EXCLUDED" if excluded else "UNKNOWN"
    return "\n".join(
        [
            "energy_step_0_before=[0,1]",
            "energy_step_0_midpoint=[0.5,0.5]",
            "energy_step_0_residual=[0,0]",
            "energy_step_0_derivative=[1,1]",
            "energy_step_0_newton_raw=[0.5,0.5]",
            "energy_step_0_newton=[0.49,0.51]",
            "energy_step_0_intersects=1",
            "energy_step_0_after=[0.49,0.51]",
            "precision_bits=128",
            "epsilon=[0,0]",
            "reduced_box={[-1,1],[-1,1],[-1,1]}",
            "qplus_input=[0,1]",
            "energy_qplus=[0.49,0.51]",
            "energy_qplus_before=[0,1]",
            "energy_midpoint=[0.5,0.5]",
            "energy_midpoint_residual=[0,0]",
            "energy_derivative=[1,1]",
            "energy_newton=[0.49,0.51]",
            "energy_iterations=1",
            "energy_derivative_positive=1",
            "energy_has_candidate=1",
            "energy_exclusion_guard=1",
            "logical_margin=[2e-30,2e-30]",
            "newton_guard=[-1e-40,1e-40]",
            "X={[-1,1],[0.49,0.51],[-1,1],[-1,1]}",
            "x_bar={[0,0],[0.5,0.5],[0,0],[0,0]}",
            f"F_center={{{first},[0,0],[0,0],[0,0]}}",
            f"F_direct={{{first},[0,0],[0,0],[0,0]}}",
            "J={{[0,0],[0,0],[0,0],[0,0]},"
            "{[0,0],[0,0],[0,0],[0,0]},"
            "{[0,0],[0,0],[0,0],[0,0]},"
            "{[0,0],[0,0],[0,0],[0,0]}}",
            f"F_mean={{{first},[0,0],[0,0],[0,0]}}",
            "C={{[1,1],[0,0],[0,0],[0,0]},"
            "{[0,0],[1,1],[0,0],[0,0]},"
            "{[0,0],[0,0],[1,1],[0,0]},"
            "{[0,0],[0,0],[0,0],[1,1]}}",
            f"F_preconditioned={{{first},[0,0],[0,0],[0,0]}}",
            f"K={{{k_first},[0.49,0.51],[-1,1],[-1,1]}}",
            f"direct_component={selected}",
            f"mean_component={selected}",
            f"preconditioned_component={selected}",
            f"excluded={1 if excluded else 0}",
            "krawczyk_subset=0",
            f"status={status}",
            "",
        ]
    )


def synthetic_conflict_transcript() -> str:
    raw = synthetic_return_transcript()
    raw = raw.replace(
        "F_direct={[0,0],[0,0],[0,0],[0,0]}",
        "F_direct={[2,2],[0,0],[0,0],[0,0]}",
    )
    raw = raw.replace(
        "J={{[0,0],[0,0],[0,0],[0,0]},"
        "{[0,0],[0,0],[0,0],[0,0]},"
        "{[0,0],[0,0],[0,0],[0,0]},"
        "{[0,0],[0,0],[0,0],[0,0]}}",
        "J={{[1,1],[0,0],[0,0],[0,0]},"
        "{[0,0],[1,1],[0,0],[0,0]},"
        "{[0,0],[0,0],[1,1],[0,0]},"
        "{[0,0],[0,0],[0,0],[1,1]}}",
    )
    raw = raw.replace(
        "F_mean={[0,0],[0,0],[0,0],[0,0]}",
        "F_mean={[-1,1],[-0.01,0.01],[-1,1],[-1,1]}",
    )
    raw = raw.replace(
        "F_preconditioned={[0,0],[0,0],[0,0],[0,0]}",
        "F_preconditioned={[-1,1],[-0.01,0.01],[-1,1],[-1,1]}",
    )
    raw = raw.replace("K={[-1,1],[0.49,0.51],[-1,1],[-1,1]}", "K={[0,0],[0.5,0.5],[0,0],[0,0]}")
    raw = raw.replace("direct_component=-1", "direct_component=0")
    raw = raw.replace("excluded=0", "excluded=1")
    raw = raw.replace("krawczyk_subset=0", "krawczyk_subset=1")
    raw = raw.replace("status=UNKNOWN", "status=INVALID_EXCLUSION_UNIQUENESS_CONFLICT")
    return raw


def minimal_tree_payload(
    tree: object,
    *,
    internal: dict[str, object] | None = None,
) -> dict[str, object]:
    return {"tree": internal or tree.payload()}


def formal_status_whitelist() -> dict[str, object]:
    return {
        "excluded": [["ENERGY_EXCLUDED", 0], ["RETURN_EXCLUDED", 0]],
        "splittable": [
            ["ENERGY_DERIVATIVE_FAIL", 3],
            ["ENERGY_GUARD_FAIL", 3],
            ["FLOW_FAIL", 3],
            ["UNKNOWN", 2],
        ],
        "scientific_stop": [["ROOT_CANDIDATE", 4]],
        "invalid": [["INVALID_EXCLUSION_UNIQUENESS_CONFLICT", 5]],
    }


def make_formal_context_fixture(
    root: Path,
    *,
    include_run_config: bool = True,
) -> tuple[Path, Path, Path, dict[str, object], dict[str, object]]:
    """Create a complete synthetic freeze/run-config binding under ``root``."""

    input_hashes: dict[str, str] = {}
    for index, relative in enumerate(MODULE.MANDATORY_FROZEN_INPUTS):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if relative == "scripts/check_r401_val_l2_all_slabs_independent.py":
            path.write_bytes(SCRIPT.read_bytes())
        else:
            path.write_text(f"synthetic frozen input {index}\n", encoding="utf-8")
        input_hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()

    binary = root / "validated/capd_r401_local_complement_mp.synthetic"
    binary.write_bytes(b"synthetic evaluator binary\n")
    source_file = "validated/capd_r401_local_complement_mp.cpp"
    scheduler = {
        "policy": MODULE.EXPECTED_SCHEDULER_POLICY,
        "workers": 24,
        "node_timeout_seconds": 7200,
        "global_scientific_budget": None,
    }
    evaluator = {
        "source_file": source_file,
        "source_sha256": input_hashes[source_file],
        "binary_file": str(binary),
        "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest(),
        "capd_commit": MODULE.EXPECTED_CAPD_COMMIT,
        "capd_flags": [
            "-D__HAVE_MPFR__",
            "-frounding-math",
            "-lmpfr",
            "-lgmp",
        ],
        "status_returncode_whitelist": formal_status_whitelist(),
    }
    limits = {"max_depth": 48, "max_nodes": 20_000}
    freeze_payload: dict[str, object] = {
        "schema_version": 1,
        "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
        "status": "FROZEN_FOR_PRODUCTION",
        "scientific_licensing_enabled": True,
        "checker_mode": "INDEPENDENT_EXACT_RATIONAL_REPLAY",
        "checker_source_sha256": MODULE.sha256(SCRIPT),
        "matrix": [tree.payload() for tree in MODULE.exact_matrix()],
        "per_tree_limits": limits,
        "scheduler": scheduler,
        "logical_thresholds": dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS),
        "evaluator": evaluator,
        "input_hashes": input_hashes,
    }
    freeze = root / "R401_VAL_L2_A1_FREEZE.synthetic.json"
    dump_json(freeze, freeze_payload)
    output = root / "archive"
    if include_run_config:
        output.mkdir(parents=True, exist_ok=True)
        binding: dict[str, object] = {
            "schema_version": 1,
            "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
            "licensing": "FROZEN_PRODUCTION",
            "scientific_licensing_enabled": True,
            "l2_a1_freeze_sha256": MODULE.sha256(freeze),
            "matrix": [tree.payload() for tree in MODULE.exact_matrix()],
            "per_tree_limits": limits,
            "scheduler": scheduler,
            "evaluator": evaluator,
            "logical_thresholds": dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS),
            "input_hashes": input_hashes,
        }
        run_config = {
            "schema_version": 1,
            "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
            "licensing": "FROZEN_PRODUCTION",
            "producer_state": "FROZEN_GENERATION_INITIALIZED",
            "milestone_status": None,
            "theorem_status": None,
            "final_status": None,
            "binding": binding,
            "binding_sha256": MODULE.sha256_bytes(MODULE.canonical_json_bytes(binding)),
        }
        dump_json(output / "run_config.json", run_config)
    return output, freeze, binary, freeze_payload, evaluator


def test_checker_is_source_independent_of_scheduler_and_producer() -> None:
    syntax = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    imported = {
        alias.name
        for node in ast.walk(syntax)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    assert not any("run_r401_val_l2_all_slabs" in name for name in imported)
    assert not any("producer" in name or "scheduler" in name for name in imported)
    assert MODULE.CHECKER_MODE == "DRAFT_NON_LICENSING"


def test_strict_json_rejects_duplicate_keys_and_nonfinite_values() -> None:
    with pytest.raises(MODULE.StrictJSONError, match="DUPLICATE_JSON_KEY"):
        MODULE.strict_json_loads('{"tree": 1, "tree": 2}')
    with pytest.raises(MODULE.StrictJSONError, match="NONFINITE_JSON_CONSTANT"):
        MODULE.strict_json_loads('{"x": NaN}')


@pytest.mark.parametrize(
    "unsafe",
    ["../escape.json", "/absolute.json", "a/../../escape", "a\\b.json", ".hidden/x"],
)
def test_path_traversal_and_noncanonical_paths_are_hard_rejected(unsafe: str) -> None:
    with pytest.raises(MODULE.PathContractError):
        MODULE.safe_relative_path(unsafe)


def test_formal_gate_rejects_missing_freeze_before_any_promotion(tmp_path: Path) -> None:
    payload = MODULE.audit_archive(
        tmp_path / "archive",
        project_root=tmp_path,
        freeze_path=tmp_path / "missing-freeze.json",
    )
    assert payload["checker_status"] == "REJECT_DRAFT_NON_LICENSING"
    assert payload["milestone_status"] is None
    assert payload["theorem_status"] is None
    assert payload["final_status"] is None
    assert payload["promotion_authorized"] is False
    assert payload["failures"] == ["MISSING_FORMAL_FREEZE"]
    assert payload["provenance_bindings"] is None


def test_draft_or_incomplete_freeze_cannot_unlock_formal_gate(tmp_path: Path) -> None:
    freeze = tmp_path / "freeze.json"
    dump_json(
        freeze,
        {
            "schema_version": 1,
            "protocol_id": MODULE.DRAFT_PROTOCOL_ID,
            "status": "DRAFT",
            "scientific_licensing_enabled": False,
        },
    )
    with pytest.raises(MODULE.CheckerContractError, match="FORMAL_FREEZE"):
        MODULE.load_formal_context(tmp_path / "archive", freeze)


def test_formal_freeze_still_hard_rejects_missing_run_config(tmp_path: Path) -> None:
    output, freeze, _binary, _payload, _evaluator = make_formal_context_fixture(
        tmp_path,
        include_run_config=False,
    )
    with pytest.raises(MODULE.CheckerContractError, match="MISSING_SEALED_RUN_CONFIG"):
        MODULE.load_formal_context(output, freeze, tmp_path)


def test_formal_context_binds_binary_capd_scheduler_timeout_and_thresholds(
    tmp_path: Path,
) -> None:
    output, freeze, _binary, _payload, _evaluator = make_formal_context_fixture(
        tmp_path
    )
    context = MODULE.load_formal_context(output, freeze, tmp_path)
    assert context.evaluator_capd_commit == MODULE.EXPECTED_CAPD_COMMIT
    assert context.scheduler["workers"] == 24
    assert context.scheduler["node_timeout_seconds"] == 7200
    assert context.logical_thresholds == MODULE.EXPECTED_LOGICAL_THRESHOLDS


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("binary_bytes", "BINARY_HASH_MISMATCH"),
        ("capd_commit", "EVALUATOR_DIFFERS_FROM_FREEZE"),
        ("capd_flags", "EVALUATOR_DIFFERS_FROM_FREEZE"),
        ("scheduler_workers", "SCHEDULER_DIFFERS_FROM_FREEZE"),
        ("scheduler_timeout", "SCHEDULER_DIFFERS_FROM_FREEZE"),
        ("threshold", "THRESHOLDS_DIFFER_FROM_FREEZE"),
    ],
)
def test_formal_context_rejects_build_and_resource_mutation(
    tmp_path: Path,
    mutation: str,
    message: str,
) -> None:
    output, freeze, binary, _payload, _evaluator = make_formal_context_fixture(
        tmp_path
    )
    config_path = output / "run_config.json"
    config = MODULE.strict_json_load(config_path)
    binding = config["binding"]
    if mutation == "binary_bytes":
        binary.write_bytes(b"mutated evaluator binary\n")
    elif mutation == "capd_commit":
        binding["evaluator"]["capd_commit"] = "0" * 40
    elif mutation == "capd_flags":
        binding["evaluator"]["capd_flags"].remove("-frounding-math")
    elif mutation == "scheduler_workers":
        binding["scheduler"]["workers"] = 23
    elif mutation == "scheduler_timeout":
        binding["scheduler"]["node_timeout_seconds"] = 3600
    elif mutation == "threshold":
        binding["logical_thresholds"]["logical_margin_128"] = "1e-29"
    else:  # pragma: no cover - closed parametrization
        raise AssertionError(mutation)
    if mutation != "binary_bytes":
        config["binding_sha256"] = MODULE.sha256_bytes(
            MODULE.canonical_json_bytes(binding)
        )
        dump_json(config_path, config)
    with pytest.raises(MODULE.CheckerContractError, match=message):
        MODULE.load_formal_context(output, freeze, tmp_path)


def test_formal_context_rejects_symlinked_binary_before_resolution(
    tmp_path: Path,
) -> None:
    output, freeze, binary, _payload, _evaluator = make_formal_context_fixture(
        tmp_path
    )
    target = binary.with_suffix(".target")
    binary.rename(target)
    binary.symlink_to(target)
    with pytest.raises(MODULE.PathContractError, match="SYMLINK_REJECTED_EVALUATOR_BINARY"):
        MODULE.load_formal_context(output, freeze, tmp_path)


def test_original_cli_path_symlink_components_are_rejected(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    leaf = target / "freeze.json"
    leaf.write_text("{}\n", encoding="utf-8")
    leaf_link = tmp_path / "freeze-link.json"
    leaf_link.symlink_to(leaf)
    with pytest.raises(MODULE.PathContractError, match="SYMLINK_REJECTED"):
        MODULE.checked_lexical_path(leaf_link, label="FORMAL_FREEZE", require_file=True)

    parent_link = tmp_path / "linked-parent"
    parent_link.symlink_to(target, target_is_directory=True)
    with pytest.raises(MODULE.PathContractError, match="SYMLINK_REJECTED"):
        MODULE.checked_lexical_path(
            parent_link / "freeze.json",
            label="FORMAL_FREEZE",
            require_file=True,
        )


def test_exact_pair_paths_reject_missing_extra_symlink_and_identity_mismatch(
    tmp_path: Path,
) -> None:
    matrix = (MODULE.TreeKey(128, "S000"), MODULE.TreeKey(256, "S000"))
    for tree in matrix:
        dump_json(MODULE.expected_tree_path(tmp_path, tree), minimal_tree_payload(tree))
        dump_json(
            MODULE.expected_tree_manifest_path(tmp_path, tree),
            minimal_tree_payload(tree),
        )
    trees, manifests = MODULE.validate_exact_pair_paths(tmp_path, matrix)
    assert set(trees) == set(manifests) == set(matrix)

    missing = MODULE.expected_tree_path(tmp_path, matrix[-1])
    saved = missing.read_bytes()
    missing.unlink()
    with pytest.raises(MODULE.MatrixContractError, match="MISSING_EXTRA_SHARDS"):
        MODULE.validate_exact_pair_paths(tmp_path, matrix)
    missing.write_bytes(saved)

    extra = tmp_path / "trees/128/S000.copy.json"
    dump_json(extra, {})
    with pytest.raises(MODULE.MatrixContractError, match="MISSING_EXTRA_SHARDS"):
        MODULE.validate_exact_pair_paths(tmp_path, matrix)
    extra.unlink()

    target = MODULE.expected_tree_manifest_path(tmp_path, matrix[0])
    target.unlink()
    target.symlink_to(MODULE.expected_tree_manifest_path(tmp_path, matrix[1]))
    with pytest.raises(MODULE.PathContractError, match="SYMLINK"):
        MODULE.validate_exact_pair_paths(tmp_path, matrix)
    target.unlink()
    dump_json(target, minimal_tree_payload(matrix[0], internal=matrix[1].payload()))
    with pytest.raises(MODULE.MatrixContractError, match="IDENTITY_MISMATCH"):
        MODULE.validate_exact_pair_paths(tmp_path, matrix)


@pytest.mark.parametrize(
    ("status", "returncode", "expected"),
    [
        ("ENERGY_EXCLUDED", 0, "ENERGY_EXCLUDED"),
        ("RETURN_EXCLUDED", 0, "RETURN_EXCLUDED"),
        ("UNKNOWN", 2, "SPLIT"),
        ("ENERGY_DERIVATIVE_FAIL", 3, "SPLIT"),
        ("ENERGY_GUARD_FAIL", 3, "SPLIT"),
        ("FLOW_FAIL", 3, "SPLIT"),
        ("ROOT_CANDIDATE", 4, "SCIENTIFIC_STOP"),
        ("INVALID_EXCLUSION_UNIQUENESS_CONFLICT", 5, "INVALID"),
    ],
)
def test_status_returncode_whitelist_is_closed(
    status: str, returncode: int, expected: str
) -> None:
    assert MODULE.status_action(status, returncode, depth=0, max_depth=40) == expected
    with pytest.raises(MODULE.ProofObjectError, match="NOT_WHITELISTED"):
        MODULE.status_action(status, returncode + 10, depth=0, max_depth=40)


def test_status_parser_rejects_missing_or_duplicate_status() -> None:
    with pytest.raises(MODULE.ProofObjectError, match="MISSING_PROOF_FIELD"):
        MODULE.Transcript("precision_bits=128\n").scalar("status")
    with pytest.raises(MODULE.ProofObjectError, match="DUPLICATE_PROOF_FIELD"):
        MODULE.Transcript("status=UNKNOWN\nstatus=UNKNOWN\n").scalar("status")


def test_exact_energy_newton_replay_passes_and_detects_guard_mutation() -> None:
    transcript = MODULE.Transcript(synthetic_return_transcript())
    result = MODULE.verify_energy_proof(transcript, "UNKNOWN")
    assert result["step_count"] == 1
    assert result["empty_gap"] is None
    corrupted = synthetic_return_transcript().replace(
        "energy_step_0_newton=[0.49,0.51]",
        "energy_step_0_newton=[0.5001,0.5002]",
    )
    with pytest.raises(MODULE.ProofObjectError, match="NEWTON_REPLAY_NOT_ENCLOSED"):
        MODULE.verify_energy_proof(MODULE.Transcript(corrupted), "UNKNOWN")


def test_return_algebra_recomputes_mean_preconditioner_krawczyk_and_margin() -> None:
    result = MODULE.verify_return_proof(
        MODULE.Transcript(synthetic_return_transcript(excluded=True)),
        "RETURN_EXCLUDED",
    )
    assert result["selected_separation_margin"] == {"numerator": 2, "denominator": 1}
    assert result["independent_krawczyk_subset"] is False
    assert result["exclusion_uniqueness_conflict"] is False

    corrupted = synthetic_return_transcript(excluded=True).replace(
        "F_mean={[2,2]", "F_mean={[3,3]"
    )
    with pytest.raises(MODULE.ProofObjectError, match="F_MEAN_DOES_NOT_ENCLOSE"):
        MODULE.verify_return_proof(MODULE.Transcript(corrupted), "RETURN_EXCLUDED")


def test_return_algebra_independently_detects_exclusion_uniqueness_conflict() -> None:
    result = MODULE.verify_return_proof(
        MODULE.Transcript(synthetic_conflict_transcript()),
        "INVALID_EXCLUSION_UNIQUENESS_CONFLICT",
    )
    assert result["selected_separation_margin"] == {"numerator": 2, "denominator": 1}
    assert result["independent_krawczyk_subset"] is True
    assert result["exclusion_uniqueness_conflict"] is True


def make_shell_tree(*, split_first: bool = False) -> dict[str, object]:
    record = synthetic_plan_record()
    protected = MODULE.plan_root_box(record)
    shells = MODULE.expected_shells(protected)
    nodes: list[dict[str, object]] = []
    for node_id in sorted(shells):
        box = shells[node_id]
        if split_first and node_id == "C0L":
            coordinate, midpoint, left, right = MODULE.split_box(box)
            evaluator = {
                "evaluator_status": "UNKNOWN",
                "returncode": 2,
                "classification": "SPLIT",
                "split": {
                    "coordinate": coordinate,
                    "midpoint": MODULE.decimal_fraction_text(midpoint),
                    "children": ["C0L0", "C0L1"],
                },
            }
        else:
            evaluator = {
                "evaluator_status": "RETURN_EXCLUDED",
                "returncode": 0,
                "classification": "RETURN_EXCLUDED",
            }
        nodes.append(
            {
                "task": {
                    "tree": {"precision_bits": 128, "slab_id": "S000"},
                    "node_id": node_id,
                    "parent_id": None,
                    "depth": 0,
                    "epsilon": ["0", "0.0021"],
                    "box": box_text(box),
                },
                "evaluator_result": evaluator,
            }
        )
    if split_first:
        _, _, left, right = MODULE.split_box(shells["C0L"])
        for node_id, box in (("C0L0", left), ("C0L1", right)):
            nodes.append(
                {
                    "task": {
                        "tree": {"precision_bits": 128, "slab_id": "S000"},
                        "node_id": node_id,
                        "parent_id": "C0L",
                        "depth": 1,
                        "epsilon": ["0", "0.0021"],
                        "box": box_text(box),
                    },
                    "evaluator_result": {
                        "evaluator_status": "RETURN_EXCLUDED",
                        "returncode": 0,
                        "classification": "RETURN_EXCLUDED",
                    },
                }
            )
    nodes.sort(key=lambda node: (node["task"]["depth"], node["task"]["node_id"]))
    terminal_count = 9 if split_first else 8
    return {
        "tree": {"precision_bits": 128, "slab_id": "S000"},
        "epsilon": ["0", "0.0021"],
        "domain": {
            "big_box": box_text(MODULE.BIG_BOX),
            "protected_exact_plan_box": box_text(protected),
        },
        "per_tree_limits": {"max_depth": 40, "max_nodes": 20000},
        "evaluated_node_count": len(nodes),
        "terminal_counts": {"ENERGY_EXCLUDED": 0, "RETURN_EXCLUDED": terminal_count},
        "nodes": nodes,
    }


def test_exact_shell_cover_and_split_dag_replay_detects_geometry_mutation() -> None:
    tree = MODULE.TreeKey(128, "S000")
    payload = make_shell_tree(split_first=True)
    nodes = MODULE.verify_tree_structure(
        tree,
        payload,
        synthetic_plan_record(),
        max_depth=40,
        max_nodes=20_000,
    )
    assert len(nodes) == 10
    payload["nodes"][-1]["task"]["box"]["q_slow"][0] = "-0.123"
    with pytest.raises(MODULE.ProofObjectError, match="GEOMETRY_MISMATCH"):
        MODULE.verify_tree_structure(
            tree,
            payload,
            synthetic_plan_record(),
            max_depth=40,
            max_nodes=20_000,
        )


def test_tree_producer_cannot_preassign_milestone() -> None:
    tree = MODULE.TreeKey(128, "S000")
    payload = make_shell_tree()
    payload["milestone_status"] = "PASS_LOCAL_COMPLEMENT_ALL_SLABS"
    with pytest.raises(MODULE.ProofObjectError, match="PRODUCER_TREE_ASSIGNED"):
        MODULE.verify_tree_structure(
            tree,
            payload,
            synthetic_plan_record(),
            max_depth=40,
            max_nodes=20_000,
        )


def synthetic_context() -> object:
    return MODULE.FormalContext(
        freeze={},
        run_config={},
        freeze_sha256="f" * 64,
        run_config_sha256="a" * 64,
        max_depth=40,
        max_nodes=20_000,
        evaluator_source_sha256="b" * 64,
        evaluator_binary_sha256="c" * 64,
        evaluator_binary_file="/frozen/evaluator",
        evaluator_capd_commit=MODULE.EXPECTED_CAPD_COMMIT,
        evaluator_capd_flags=(
            "-D__HAVE_MPFR__",
            "-frounding-math",
            "-lmpfr",
            "-lgmp",
        ),
        scheduler={
            "policy": MODULE.EXPECTED_SCHEDULER_POLICY,
            "workers": 24,
            "node_timeout_seconds": 7200,
            "global_scientific_budget": None,
        },
        logical_thresholds=dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS),
    )


def test_node_record_requires_exact_argv_proof_object_and_hash(tmp_path: Path) -> None:
    tree = MODULE.TreeKey(128, "S000")
    task = task_payload()
    raw = synthetic_return_transcript()
    paths = MODULE.expected_raw_paths(tmp_path, tree, "C0L")
    paths["record"].parent.mkdir(parents=True)
    paths["stdout"].write_text(raw, encoding="utf-8")
    paths["stderr"].write_text("", encoding="utf-8")
    dump_json(paths["telemetry"], {"wall_seconds": 0.1})
    result = {
        "evaluator_status": "UNKNOWN",
        "returncode": 2,
        "classification": "SPLIT",
    }
    raw_binding = {
        "stdout_file": paths["stdout"].relative_to(tmp_path).as_posix(),
        "stdout_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "stderr_file": paths["stderr"].relative_to(tmp_path).as_posix(),
        "stderr_sha256": hashlib.sha256(b"").hexdigest(),
    }
    record = {
        "schema_version": 1,
        "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "task": task,
        "task_binding_sha256": MODULE.canonical_task_binding(task),
        "evaluator_result": result,
        "raw": raw_binding,
    }
    dump_json(paths["record"], record)
    node = {
        "task": task,
        "task_binding_sha256": MODULE.canonical_task_binding(task),
        "evaluator_result": result,
        "raw": raw_binding,
    }
    with pytest.raises(MODULE.ProofObjectError, match="MISSING_PROOF_OBJECT: invocation.argv"):
        MODULE.verify_node_record(tmp_path, tree, node, synthetic_context())

    argv = MODULE.exact_argv(task, "/frozen/evaluator")
    record["invocation"] = {
        "argv": argv,
        "argv_sha256": MODULE.sha256_bytes(MODULE.canonical_json_bytes(argv)),
    }
    node["invocation"] = json.loads(json.dumps(record["invocation"]))
    dump_json(paths["record"], record)
    replay = MODULE.verify_node_record(tmp_path, tree, node, synthetic_context())
    assert replay["status"] == "UNKNOWN"

    node["invocation"]["argv"][3] = "0.001"
    with pytest.raises(MODULE.ProofObjectError, match="TREE_RECORD_INVOCATION"):
        MODULE.verify_node_record(tmp_path, tree, node, synthetic_context())
    node["invocation"] = json.loads(json.dumps(record["invocation"]))

    record["invocation"]["argv"][2] = "0.001"
    dump_json(paths["record"], record)
    with pytest.raises(MODULE.ProofObjectError, match="EXACT_ARGV_MISMATCH"):
        MODULE.verify_node_record(tmp_path, tree, node, synthetic_context())


def test_tree_record_manifest_argv_binding_is_three_way_and_fail_closed(
    tmp_path: Path,
) -> None:
    tree = MODULE.TreeKey(128, "S000")
    task = task_payload()
    invocation = {
        "argv": MODULE.exact_argv(task, "/frozen/evaluator"),
    }
    invocation["argv_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(invocation["argv"])
    )
    paths = MODULE.expected_raw_paths(tmp_path, tree, "C0L")
    paths["record"].parent.mkdir(parents=True)
    record = {"invocation": invocation}
    dump_json(paths["record"], record)
    paths["stdout"].write_text("status=RETURN_EXCLUDED\n", encoding="utf-8")
    paths["stderr"].write_text("", encoding="utf-8")
    dump_json(paths["telemetry"], {})
    node = {"invocation": json.loads(json.dumps(invocation))}
    tree_payload = {"run_config_sha256": "a" * 64}
    tree_path = MODULE.expected_tree_path(tmp_path, tree)
    dump_json(tree_path, tree_payload)
    manifest = {
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "run_config_sha256": "a" * 64,
        "tree_file": tree_path.relative_to(tmp_path).as_posix(),
        "tree_sha256": MODULE.sha256(tree_path),
        "node_files": {
            "C0L": {
                "record_sha256": MODULE.sha256(paths["record"]),
                "stdout_sha256": MODULE.sha256(paths["stdout"]),
                "stderr_sha256": MODULE.sha256(paths["stderr"]),
                "argv_sha256": invocation["argv_sha256"],
            }
        },
    }
    MODULE.verify_tree_manifest(
        tmp_path,
        tree,
        tree_payload,
        manifest,
        {"C0L": node},
        synthetic_context(),
    )
    manifest["node_files"]["C0L"]["argv_sha256"] = "0" * 64
    with pytest.raises(MODULE.ProofObjectError, match="ARGV_BINDING_MISMATCH"):
        MODULE.verify_tree_manifest(
            tmp_path,
            tree,
            tree_payload,
            manifest,
            {"C0L": node},
            synthetic_context(),
        )


def test_raw_matrix_rejects_extra_node_summary_and_symlink(tmp_path: Path) -> None:
    tree = MODULE.TreeKey(128, "S000")
    paths = MODULE.expected_raw_paths(tmp_path, tree, "C0L")
    for key, path in paths.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}\n" if key in {"record", "telemetry"} else "", encoding="utf-8")
    MODULE.validate_raw_file_set(tmp_path, {tree: {"C0L"}})
    extra = paths["record"].parent / "record.copy.json"
    extra.write_text("{}\n", encoding="utf-8")
    with pytest.raises(MODULE.PathContractError, match="MISSING_EXTRA_RAW_OBJECTS"):
        MODULE.validate_raw_file_set(tmp_path, {tree: {"C0L"}})
    extra.unlink()
    paths["stderr"].unlink()
    paths["stderr"].symlink_to(paths["stdout"])
    with pytest.raises(MODULE.PathContractError, match="SYMLINK"):
        MODULE.validate_raw_file_set(tmp_path, {tree: {"C0L"}})


def test_aggregate_manifest_hash_dag_binds_exact_102_entries(tmp_path: Path) -> None:
    matrix = MODULE.exact_matrix()
    entries: list[dict[str, object]] = []
    manifests: dict[object, object] = {}
    for tree in matrix:
        path = MODULE.expected_tree_manifest_path(tmp_path, tree)
        dump_json(path, {"tree": tree.payload()})
        manifests[tree] = {"tree": tree.payload()}
        entries.append(
            {
                **tree.payload(),
                "tree_manifest_file": path.relative_to(tmp_path).as_posix(),
                "tree_manifest_sha256": MODULE.sha256(path),
            }
        )
    summary = {
        "schema_version": 1,
        "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "run_config_sha256": "a" * 64,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "tree_count": 102,
        "trees": entries,
    }
    summary_path = tmp_path / "aggregate_summary.json"
    dump_json(summary_path, summary)
    aggregate = {
        "schema_version": 1,
        "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "run_config_sha256": "a" * 64,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "aggregate_summary_file": "aggregate_summary.json",
        "aggregate_summary_sha256": MODULE.sha256(summary_path),
        "tree_manifests": entries,
    }
    dump_json(tmp_path / "aggregate_manifest.json", aggregate)
    MODULE.verify_aggregate_hash_dag(
        tmp_path,
        matrix,
        manifests,
        synthetic_context(),
    )
    dump_json(tmp_path / "run_config.json", {"synthetic": True})
    bindings = MODULE.build_archive_provenance_bindings(
        tmp_path,
        matrix,
        synthetic_context(),
    )
    assert bindings["freeze_sha256"] == "f" * 64
    assert bindings["run_config_sha256"] == "a" * 64
    assert bindings["aggregate_manifest_sha256"] == MODULE.sha256(
        tmp_path / "aggregate_manifest.json"
    )
    assert bindings["evaluator_binary_sha256"] == "c" * 64
    assert bindings["tree_manifest_root"]["entry_count"] == 102
    assert len(bindings["tree_manifest_root"]["sha256"]) == 64
    assert len(bindings["archive_generation_sha256"]) == 64
    aggregate["tree_manifests"][0]["tree_manifest_sha256"] = "0" * 64
    dump_json(tmp_path / "aggregate_manifest.json", aggregate)
    with pytest.raises(MODULE.ProofObjectError, match="LIST_MISMATCH"):
        MODULE.verify_aggregate_hash_dag(
            tmp_path,
            matrix,
            manifests,
            synthetic_context(),
        )


def test_aggregate_matrix_rejects_duplicate_summary_identity() -> None:
    entries = [tree.payload() for tree in MODULE.exact_matrix()]
    entries[-1] = dict(entries[0])
    with pytest.raises(MODULE.MatrixContractError, match="DUPLICATE_AGGREGATE_SUMMARY"):
        MODULE._matrix_payload(entries, "AGGREGATE_SUMMARY")


def test_authoritative_checker_outputs_are_write_once_per_generation(
    tmp_path: Path,
) -> None:
    target = tmp_path / "independent_checker.json"
    first = {
        "promotion_authorized": True,
        "provenance_bindings": {"archive_generation_sha256": "a" * 64},
    }
    MODULE.write_once_or_verify_json(target, first)
    MODULE.write_once_or_verify_json(target, first)
    original = target.read_bytes()
    changed = {
        "promotion_authorized": True,
        "provenance_bindings": {"archive_generation_sha256": "b" * 64},
    }
    with pytest.raises(MODULE.PathContractError, match="DIFFERENT_GENERATION"):
        MODULE.write_once_or_verify_json(target, changed)
    assert target.read_bytes() == original
