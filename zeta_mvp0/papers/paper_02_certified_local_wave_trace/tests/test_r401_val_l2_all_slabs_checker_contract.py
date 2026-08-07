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
        elif relative == MODULE.MACHINE_FREEZE_RELATIVE:
            dump_json(
                path,
                {
                    "schema_version": 1,
                    "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
                    "status": "FROZEN_FOR_PRODUCTION",
                    "scientific_licensing_enabled": True,
                    "machine_requirements": dict(
                        MODULE.EXPECTED_MACHINE_REQUIREMENTS
                    ),
                },
            )
        elif relative == MODULE.PREFREEZE_REVIEW_RELATIVE:
            path.write_text(
                "# Independent prefreeze review\n\n"
                f"{MODULE.PREFREEZE_ACCEPT_LINE}\n",
                encoding="utf-8",
            )
        elif relative in {MODULE.S0_REPLAY_RELATIVE, MODULE.S0_ADAPTER_RELATIVE}:
            path.write_bytes((ROOT / relative).read_bytes())
        else:
            path.write_text(f"synthetic frozen input {index}\n", encoding="utf-8")
        input_hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()

    for relative in (
        f"{MODULE.S0_RESULT_RELATIVE}/RELEASE_PROVENANCE.json",
        f"{MODULE.S0_RESULT_RELATIVE}/manifest.json",
        f"{MODULE.S0_RESULT_RELATIVE}/POSTCHECK_STATUS.json",
    ):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / relative).read_bytes())

    binary = root / "validated/capd_r401_local_complement_mp.synthetic"
    binary.write_bytes(b"synthetic evaluator binary\n")
    source_file = "validated/capd_r401_local_complement_mp.cpp"
    scheduler = {
        "policy": MODULE.EXPECTED_SCHEDULER_POLICY,
        "workers": 24,
        "node_timeout_seconds": 7200,
        "global_scientific_budget": None,
        "max_inflight_per_tree": 1,
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
        "machine_requirements": dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
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
            "machine_requirements": dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
            "machine_freeze_sha256": input_hashes[MODULE.MACHINE_FREEZE_RELATIVE],
            "evaluator": evaluator,
            "logical_thresholds": dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS),
            "input_hashes": input_hashes,
        }
        run_config = {
            "schema_version": 1,
            "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
            "licensing": "FROZEN_PRODUCTION",
            "scientific_licensing_enabled": True,
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
    assert MODULE.CHECKER_MODE == "INDEPENDENT_EXACT_RATIONAL_REPLAY"


def test_mandatory_hash_dag_covers_formal_machine_review_and_upstream_l1() -> None:
    assert set(MODULE.MANDATORY_FROZEN_INPUTS).issuperset(
        {
            "scripts/check_r401_val_l2_all_slabs_independent.py",
            "scripts/run_r401_val_l2_all_slabs.py",
            "validated/capd_r401_local_complement_mp.cpp",
            "validated/CAPD_DEPENDENCY.md",
            "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json",
            "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md",
            MODULE.MACHINE_FREEZE_RELATIVE,
            "research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md",
            "results/r401_val_l1_branch/RELEASE_PROVENANCE.json",
            "results/r401_val_l1_branch/summary.json",
            "results/r401_val_l1_branch/manifest.json",
            "results/r401_val_l1_branch/independent_checker.json",
            "results/r401_val_l1_branch/POSTCHECK_STATUS.json",
        }
    )


def test_prefreeze_review_gate_accepts_one_exact_declaration(tmp_path: Path) -> None:
    path = tmp_path / MODULE.PREFREEZE_REVIEW_RELATIVE
    path.parent.mkdir(parents=True)
    path.write_text(
        "# Independent review\n\n"
        f"{MODULE.PREFREEZE_ACCEPT_LINE}\n\n"
        "The remainder is explanatory text.\n",
        encoding="utf-8",
    )
    hashes = {MODULE.PREFREEZE_REVIEW_RELATIVE: MODULE.sha256(path)}
    assert MODULE.validate_prefreeze_review(tmp_path, hashes) == MODULE.sha256(path)


@pytest.mark.parametrize(
    "content",
    [
        "Verdict: PENDING\n",
        "No verdict declaration is present.\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict: ACCEPT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict: PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE \n",
        " Verdict: ACCEPT_FOR_FREEZE\n",
        "verdict: ACCEPT_FOR_FREEZE\n",
        "Verdict : ACCEPT_FOR_FREEZE\n",
        "Verdict=ACCEPT_FOR_FREEZE\n",
        "Verdict - ACCEPT_FOR_FREEZE\n",
        "Verdict: ACCEPT FOR FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict=PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE\n- Verdict: REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\n> Verdict: PENDING\n",
        "Verdict: ACCEPT_FOR_FREEZE\n**Verdict:** REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\n| Verdict | REJECT_FOR_FREEZE |\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict - REJECT_FOR_FREEZE\n",
        "Verdict: ACCEPT_FOR_FREEZE\nVerdict：PENDING\n",
    ],
)
def test_prefreeze_review_gate_rejects_pending_missing_duplicate_or_near_match(
    tmp_path: Path,
    content: str,
) -> None:
    path = tmp_path / MODULE.PREFREEZE_REVIEW_RELATIVE
    path.parent.mkdir(parents=True)
    path.write_text(content, encoding="utf-8")
    hashes = {MODULE.PREFREEZE_REVIEW_RELATIVE: MODULE.sha256(path)}
    with pytest.raises(
        MODULE.CheckerContractError,
        match="PREFREEZE_REVIEW_NOT_EXACTLY_ACCEPTED",
    ):
        MODULE.validate_prefreeze_review(tmp_path, hashes)


def test_prefreeze_review_gate_rejects_missing_file(tmp_path: Path) -> None:
    with pytest.raises(MODULE.PathContractError, match="MISSING_REGULAR_FILE"):
        MODULE.validate_prefreeze_review(
            tmp_path,
            {MODULE.PREFREEZE_REVIEW_RELATIVE: "0" * 64},
        )


def test_prefreeze_review_gate_replays_actual_file_hash(tmp_path: Path) -> None:
    path = tmp_path / MODULE.PREFREEZE_REVIEW_RELATIVE
    path.parent.mkdir(parents=True)
    path.write_text(f"{MODULE.PREFREEZE_ACCEPT_LINE}\n", encoding="utf-8")
    with pytest.raises(
        MODULE.CheckerContractError,
        match="PREFREEZE_REVIEW_INPUT_HASH_MISMATCH",
    ):
        MODULE.validate_prefreeze_review(
            tmp_path,
            {MODULE.PREFREEZE_REVIEW_RELATIVE: "0" * 64},
        )


def test_strict_json_rejects_duplicate_keys_and_nonfinite_values() -> None:
    with pytest.raises(MODULE.StrictJSONError, match="DUPLICATE_JSON_KEY"):
        MODULE.strict_json_loads('{"tree": 1, "tree": 2}')
    with pytest.raises(MODULE.StrictJSONError, match="NONFINITE_JSON_CONSTANT"):
        MODULE.strict_json_loads('{"x": NaN}')
    with pytest.raises(MODULE.StrictJSONError, match="NONFINITE_JSON_NUMBER"):
        MODULE.strict_json_loads('{"x": 1e400}')


@pytest.mark.parametrize(
    "unsafe",
    [
        "../escape.json",
        "/absolute.json",
        "a/../../escape",
        "a\\b.json",
        ".hidden/x",
        "./a.json",
        "a//b.json",
        "a/",
    ],
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
    assert payload["checker_status"] == "REJECT_FORMAL_PRECONDITION"
    assert type(payload["schema_version"]) is int
    assert payload["schema_version"] == MODULE.SCHEMA_VERSION
    assert payload["milestone_status"] is None
    assert payload["theorem_status"] is None
    assert payload["final_status"] is None
    assert payload["promotion_authorized"] is False
    assert payload["failures"] == ["MISSING_FORMAL_FREEZE"]
    assert payload["provenance_bindings"] is None


@pytest.mark.parametrize(
    ("field", "value"),
    [("precision_bits", 128.0), ("precision_bits", True), ("slab_id", 0)],
)
def test_exact_matrix_rejects_coercible_identity_types(
    field: str,
    value: object,
) -> None:
    matrix = [tree.payload() for tree in MODULE.exact_matrix()]
    matrix[0][field] = value
    with pytest.raises(MODULE.MatrixContractError, match="MALFORMED_FREEZE_MATRIX_ENTRY"):
        MODULE._matrix_payload(matrix, "FREEZE")


def test_draft_or_incomplete_freeze_cannot_unlock_formal_gate(tmp_path: Path) -> None:
    freeze = tmp_path / "freeze.json"
    dump_json(
        freeze,
        {
            "schema_version": 1,
            "protocol_id": "R401-VAL-L2-A1-DRAFT",
            "status": "DRAFT",
            "scientific_licensing_enabled": False,
        },
    )
    with pytest.raises(MODULE.CheckerContractError, match="FORMAL_FREEZE"):
        MODULE.load_formal_context(tmp_path / "archive", freeze)


def test_checker_mandatory_frozen_input_tuple_is_exact_complete_17_chain() -> None:
    expected = (
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
    assert MODULE.MANDATORY_FROZEN_INPUTS == expected


@pytest.mark.parametrize("missing", MODULE.MANDATORY_FROZEN_INPUTS)
def test_checker_rejects_each_missing_mandatory_input_hash(
    tmp_path: Path,
    missing: str,
) -> None:
    output, freeze, _binary, payload, _evaluator = make_formal_context_fixture(
        tmp_path
    )
    del payload["input_hashes"][missing]
    dump_json(freeze, payload)
    with pytest.raises(
        MODULE.CheckerContractError,
        match="MISSING_MANDATORY_INPUT_HASHES",
    ):
        MODULE.load_formal_context(output, freeze, tmp_path)


@pytest.mark.parametrize(
    "mutation",
    ("checker_hash", "manifest_checks", "status_counts", "tree_counts", "s0_hash"),
)
def test_checker_rejects_forged_public_s0_replay_semantics(
    tmp_path: Path,
    mutation: str,
) -> None:
    output, freeze, _binary, payload, _evaluator = make_formal_context_fixture(
        tmp_path
    )
    replay_path = tmp_path / MODULE.S0_REPLAY_RELATIVE
    replay = MODULE.strict_json_load(replay_path)
    if mutation == "checker_hash":
        replay["checker_source_sha256"] = "0" * 64
    elif mutation == "manifest_checks":
        replay["manifest_hash_checks"] = 1
    elif mutation == "status_counts":
        replay["status_counts"] = {"UNKNOWN": 3016}
    elif mutation == "tree_counts":
        replay["tree_counts"][0]["node_count"] = 485
    elif mutation == "s0_hash":
        replay["s0_release_provenance_sha256"] = "0" * 64
    else:  # pragma: no cover - closed parametrization
        raise AssertionError(mutation)
    dump_json(replay_path, replay)
    payload["input_hashes"][MODULE.S0_REPLAY_RELATIVE] = MODULE.sha256(replay_path)
    dump_json(freeze, payload)
    with pytest.raises(
        MODULE.CheckerContractError,
        match="PUBLIC_S0_COMPATIBILITY_REPLAY",
    ):
        MODULE.load_formal_context(output, freeze, tmp_path)


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
    assert context.scheduler["max_inflight_per_tree"] == 1
    assert context.logical_thresholds == MODULE.EXPECTED_LOGICAL_THRESHOLDS
    assert context.machine_requirements == MODULE.EXPECTED_MACHINE_REQUIREMENTS
    assert context.machine_freeze_sha256 == MODULE.sha256(
        tmp_path / MODULE.MACHINE_FREEZE_RELATIVE
    )
    assert context.prefreeze_review_sha256 == MODULE.sha256(
        tmp_path / MODULE.PREFREEZE_REVIEW_RELATIVE
    )


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("cpu_logical", 31),
        ("memory_limit_bytes", 64_424_509_439),
        ("min_launch_free_bytes", 107_374_182_399),
        ("operational_pause_below_free_bytes", 107_374_182_400),
    ],
)
def test_machine_freeze_requires_exact_resource_contract(
    tmp_path: Path,
    key: str,
    value: int,
) -> None:
    _output, _freeze, _binary, freeze_payload, _evaluator = (
        make_formal_context_fixture(tmp_path)
    )
    path = tmp_path / MODULE.MACHINE_FREEZE_RELATIVE
    machine = MODULE.strict_json_load(path)
    machine["machine_requirements"][key] = value
    dump_json(path, machine)
    hashes = dict(freeze_payload["input_hashes"])
    hashes[MODULE.MACHINE_FREEZE_RELATIVE] = MODULE.sha256(path)
    with pytest.raises(
        MODULE.CheckerContractError,
        match="MACHINE_FREEZE_NAMESPACE_OR_RESOURCE_MISMATCH",
    ):
        MODULE.validate_machine_freeze(
            tmp_path,
            hashes,
            MODULE.EXPECTED_MACHINE_REQUIREMENTS,
        )


def test_machine_freeze_hash_is_replayed_from_actual_bytes(tmp_path: Path) -> None:
    _output, _freeze, _binary, freeze_payload, _evaluator = (
        make_formal_context_fixture(tmp_path)
    )
    path = tmp_path / MODULE.MACHINE_FREEZE_RELATIVE
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(
        MODULE.CheckerContractError,
        match="MACHINE_FREEZE_INPUT_HASH_MISMATCH",
    ):
        MODULE.validate_machine_freeze(
            tmp_path,
            freeze_payload["input_hashes"],
            MODULE.EXPECTED_MACHINE_REQUIREMENTS,
        )


def test_freeze_rejects_more_than_one_inflight_node_per_tree(tmp_path: Path) -> None:
    output, freeze, _binary, freeze_payload, _evaluator = (
        make_formal_context_fixture(tmp_path)
    )
    freeze_payload["scheduler"]["max_inflight_per_tree"] = 2
    dump_json(freeze, freeze_payload)
    with pytest.raises(
        MODULE.CheckerContractError,
        match="INVALID_FROZEN_SCHEDULER_CONTRACT",
    ):
        MODULE.load_formal_context(output, freeze, tmp_path)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("machine_requirements", {}, "MACHINE_REQUIREMENTS_DIFFER"),
        ("machine_freeze_sha256", "0" * 64, "MACHINE_FREEZE_HASH_MISMATCH"),
    ],
)
def test_run_config_directly_binds_machine_contract(
    tmp_path: Path,
    field: str,
    value: object,
    message: str,
) -> None:
    output, freeze, _binary, _freeze_payload, _evaluator = (
        make_formal_context_fixture(tmp_path)
    )
    path = output / "run_config.json"
    config = MODULE.strict_json_load(path)
    config["binding"][field] = value
    config["binding_sha256"] = MODULE.sha256_bytes(
        MODULE.canonical_json_bytes(config["binding"])
    )
    dump_json(path, config)
    with pytest.raises(MODULE.CheckerContractError, match=message):
        MODULE.load_formal_context(output, freeze, tmp_path)


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
        "schema_version": 1,
        "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": MODULE.EXPECTED_PRODUCER_STATES["tree"],
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
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
    with pytest.raises(MODULE.ProofObjectError, match="PRODUCER_TREE.*ASSIGNED"):
        MODULE.verify_tree_structure(
            tree,
            payload,
            synthetic_plan_record(),
            max_depth=40,
            max_nodes=20_000,
        )


def test_tree_terminal_counts_reject_integral_float_alias() -> None:
    tree = MODULE.TreeKey(128, "S000")
    payload = make_shell_tree()
    payload["terminal_counts"]["RETURN_EXCLUDED"] = 8.0
    with pytest.raises(MODULE.ProofObjectError, match="TERMINAL_COUNT_MISMATCH"):
        MODULE.verify_tree_structure(
            tree,
            payload,
            synthetic_plan_record(),
            max_depth=40,
            max_nodes=20_000,
        )


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("protocol_id", "R401-VAL-L2-A1-DRAFT", "NAMESPACE_OR_LICENSE"),
        ("licensing", "DRAFT_NONE", "NAMESPACE_OR_LICENSE"),
        ("scientific_licensing_enabled", False, "NAMESPACE_OR_LICENSE"),
        ("producer_state", "DRAFT_TREE_COMMITTED", "PRODUCER_STATE"),
        ("theorem_status", "PASS_LOCAL_COMPLEMENT_ALL_SLABS", "ASSIGNED_SCIENTIFIC"),
    ],
)
def test_formal_tree_namespace_license_state_and_authority_are_closed(
    field: str,
    value: object,
    message: str,
) -> None:
    tree = MODULE.TreeKey(128, "S000")
    payload = make_shell_tree()
    payload[field] = value
    with pytest.raises(MODULE.ProofObjectError, match=message):
        MODULE.verify_tree_structure(
            tree,
            payload,
            synthetic_plan_record(),
            max_depth=40,
            max_nodes=20_000,
        )


def test_formal_tree_must_explicitly_carry_all_three_null_statuses() -> None:
    tree = MODULE.TreeKey(128, "S000")
    payload = make_shell_tree()
    del payload["final_status"]
    with pytest.raises(MODULE.ProofObjectError, match="ASSIGNED_SCIENTIFIC"):
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
            "max_inflight_per_tree": 1,
        },
        logical_thresholds=dict(MODULE.EXPECTED_LOGICAL_THRESHOLDS),
        machine_requirements=dict(MODULE.EXPECTED_MACHINE_REQUIREMENTS),
        machine_freeze_sha256="d" * 64,
        prefreeze_review_sha256="e" * 64,
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
        "scientific_licensing_enabled": True,
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
        "schema_version": 1,
        "protocol_id": MODULE.FORMAL_PROTOCOL_ID,
        "licensing": "FROZEN_PRODUCTION",
        "scientific_licensing_enabled": True,
        "producer_state": MODULE.EXPECTED_PRODUCER_STATES["tree_manifest"],
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
    manifest["producer_state"] = "DRAFT_TREE_COMMITTED"
    with pytest.raises(MODULE.ProofObjectError, match="PRODUCER_STATE_MISMATCH"):
        MODULE.verify_tree_manifest(
            tmp_path,
            tree,
            tree_payload,
            manifest,
            {"C0L": node},
            synthetic_context(),
        )
    manifest["producer_state"] = MODULE.EXPECTED_PRODUCER_STATES["tree_manifest"]
    saved_node_files = manifest["node_files"]
    manifest["node_files"] = {}
    with pytest.raises(MODULE.ProofObjectError, match="NODE_SET_MISMATCH"):
        MODULE.verify_tree_manifest(
            tmp_path,
            tree,
            tree_payload,
            manifest,
            {"C0L": node},
            synthetic_context(),
        )
    manifest["node_files"] = saved_node_files
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


def test_raw_matrix_ignores_only_canonical_interrupted_node_staging(
    tmp_path: Path,
) -> None:
    tree = MODULE.TreeKey(128, "S000")
    paths = MODULE.expected_raw_paths(tmp_path, tree, "C0L")
    for key, path in paths.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}\n" if key in {"record", "telemetry"} else "", encoding="utf-8")

    interrupted = tmp_path / "raw/128/S000/.C0L0.tmp-1234-deadbeef"
    interrupted.mkdir()
    (interrupted / "record.json").write_text('{"partial":true}\n', encoding="utf-8")
    (interrupted / "stdout.txt").write_text("partial", encoding="utf-8")
    MODULE.validate_raw_file_set(tmp_path, {tree: {"C0L"}})

    malformed = tmp_path / "raw/128/S000/.not-a-node.tmp-deadbeef"
    malformed.mkdir()
    with pytest.raises(MODULE.PathContractError, match="HIDDEN_AUTHORITATIVE_PATH"):
        MODULE.validate_raw_file_set(tmp_path, {tree: {"C0L"}})


def test_exact_matrix_scan_ignores_only_canonical_interrupted_file_staging(
    tmp_path: Path,
) -> None:
    root = tmp_path / "trees"
    staging = root / "128/.S000.json.tmp-1234-deadbeef"
    staging.parent.mkdir(parents=True)
    staging.write_text("partial", encoding="utf-8")
    MODULE.scan_exact_json_paths(root, ())

    malformed = root / "128/.S000.copy.json.tmp-1234-deadbeef"
    malformed.write_text("partial", encoding="utf-8")
    with pytest.raises(MODULE.PathContractError, match="HIDDEN_AUTHORITATIVE_PATH"):
        MODULE.scan_exact_json_paths(root, ())


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
        "scientific_licensing_enabled": True,
        "producer_state": MODULE.EXPECTED_PRODUCER_STATES["aggregate_summary"],
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
        "scientific_licensing_enabled": True,
        "producer_state": MODULE.EXPECTED_PRODUCER_STATES["aggregate_manifest"],
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
    summary["tree_count"] = 102.0
    dump_json(summary_path, summary)
    aggregate["aggregate_summary_sha256"] = MODULE.sha256(summary_path)
    dump_json(tmp_path / "aggregate_manifest.json", aggregate)
    with pytest.raises(
        MODULE.MatrixContractError,
        match="AGGREGATE_SUMMARY_TREE_COUNT_MISMATCH",
    ):
        MODULE.verify_aggregate_hash_dag(
            tmp_path,
            matrix,
            manifests,
            synthetic_context(),
        )
    summary["tree_count"] = 102
    dump_json(summary_path, summary)
    aggregate["aggregate_summary_sha256"] = MODULE.sha256(summary_path)
    dump_json(tmp_path / "aggregate_manifest.json", aggregate)
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


def test_write_once_publication_cannot_overwrite_a_racing_generation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = tmp_path / "POSTCHECK_STATUS.json"
    requested = {"archive_generation_sha256": "a" * 64}
    competing = {"archive_generation_sha256": "b" * 64}

    def racing_link(
        _source: str,
        _destination: str,
        *args: object,
        **kwargs: object,
    ) -> None:
        target.write_bytes(MODULE.canonical_json_bytes(competing))
        raise FileExistsError

    monkeypatch.setattr(MODULE.os, "link", racing_link)
    with pytest.raises(MODULE.PathContractError, match="DIFFERENT_GENERATION"):
        MODULE.write_once_or_verify_json(target, requested)
    assert target.read_bytes() == MODULE.canonical_json_bytes(competing)
    assert not list(tmp_path.glob(".*.seal-*"))


def test_write_once_rejects_preexisting_hardlink_alias(tmp_path: Path) -> None:
    target = tmp_path / "independent_checker.json"
    payload = {"archive_generation_sha256": "a" * 64}
    MODULE.write_once_or_verify_json(target, payload)
    alias = tmp_path / "checker-alias.json"
    alias.hardlink_to(target)
    with pytest.raises(MODULE.PathContractError, match="HARDLINK_ALIAS"):
        MODULE.write_once_or_verify_json(target, payload)


def test_write_once_links_open_inode_not_replaced_temp_name(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = tmp_path / "independent_checker.json"
    requested = {"archive_generation_sha256": "a" * 64}
    real_link = MODULE.os.link
    attacked = False

    def racing_link(
        source: str,
        destination: str,
        *args: object,
        **kwargs: object,
    ) -> None:
        nonlocal attacked
        temporary = list(tmp_path.glob(".independent_checker.json.seal-*"))
        assert len(temporary) == 1
        temporary[0].unlink()
        temporary[0].write_bytes(b"ATTACKER BYTES")
        attacked = True
        real_link(source, destination, *args, **kwargs)

    monkeypatch.setattr(MODULE.os, "link", racing_link)
    with pytest.raises(MODULE.PathContractError, match="PUBLICATION_LINK_FAILURE"):
        MODULE.write_once_or_verify_json(target, requested)
    assert attacked
    assert not target.exists()
