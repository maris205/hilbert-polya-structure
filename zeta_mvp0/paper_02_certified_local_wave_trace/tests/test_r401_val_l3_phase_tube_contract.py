from __future__ import annotations

import copy
import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

import pytest
from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "scripts/run_r401_val_l3_phase_tube_smoke.py"
CHECKER_PATH = ROOT / "scripts/check_r401_val_l3_phase_tube_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RUNNER = load_module("r401_val_l3_phase_tube_runner", RUNNER_PATH)
CHECKER = load_module("r401_val_l3_phase_tube_checker", CHECKER_PATH)


def refresh_tree_content_hash(tree: dict[str, object]) -> None:
    without_hash = dict(tree)
    without_hash.pop("content_sha256", None)
    tree["content_sha256"] = CHECKER.sha256_bytes(
        CHECKER.canonical_json_bytes(without_hash)
    )


@pytest.fixture(autouse=True)
def restore_arb_precision():
    previous = ctx.prec
    try:
        yield
    finally:
        ctx.prec = previous


def test_nonlicensing_status_and_independent_import_contract() -> None:
    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    checker_text = CHECKER_PATH.read_text(encoding="utf-8")
    assert RUNNER.ARTIFACT_STATUS == "DRAFT_NON_LICENSING"
    assert RUNNER.PASS_STATUS == "PASS_STATIC_COMPONENT_SMOKE"
    assert RUNNER.COMPONENT_SCOPE == "STATIC_ONLY"
    assert CHECKER.ARTIFACT_STATUS == "DRAFT_NON_LICENSING"
    assert CHECKER.PASS_STATUS == "PASS_STATIC_COMPONENT_SMOKE"
    assert CHECKER.COMPONENT_SCOPE == "STATIC_ONLY"
    assert "PASS_IMPLEMENTATION_SMOKE" not in runner_text
    assert "PASS_IMPLEMENTATION_SMOKE" not in checker_text
    assert "scientific_licensing_enabled" in runner_text
    assert "scientific_licensing_enabled" in checker_text
    assert "import run_r401_val_l3_phase_tube_smoke" not in checker_text
    assert "from run_r401_val_l3_phase_tube_smoke" not in checker_text
    assert "K_Qplus" not in runner_text
    assert "K_Qplus" not in checker_text


@pytest.mark.parametrize(
    "payload",
    [
        {"numerator": 1, "denominator": "2"},
        {"numerator": "1", "denominator": 2},
        {"numerator": "+1", "denominator": "2"},
        {"numerator": "01", "denominator": "2"},
        {"numerator": "2", "denominator": "4"},
        {"numerator": "1", "denominator": "-2"},
        {"numerator": "1", "denominator": "0"},
        {"numerator": "1", "denominator": "2", "float": 0.5},
    ],
)
def test_checker_rejects_noncanonical_fraction_coercions(payload: object) -> None:
    with pytest.raises(CHECKER.CheckError):
        CHECKER.parse_fraction_record(payload, "mutated")


def test_exact_interval_construction_contains_rational_boundaries() -> None:
    ctx.prec = 128
    lower = Fraction(-15, 1000)
    upper = Fraction(15, 1000)
    enclosure = RUNNER.interval_ball((lower, upper))
    assert enclosure.contains(RUNNER.point_ball(lower))
    assert enclosure.contains(RUNNER.point_ball(upper))
    squared = RUNNER.square_interval(enclosure)
    assert squared.lower() >= arb(0)
    assert squared.contains(RUNNER.point_ball(Fraction(225, 1_000_000)))


def test_outer_containment_gates_are_independently_recomputed() -> None:
    ctx.prec = 128
    production_model = RUNNER.build_model()
    independent_model = CHECKER.independent_model()
    record = RUNNER.outer_containment_gates(production_model, 128)
    checks = CHECKER.verify_outer_containment(
        record, independent_model, 128, "outer"
    )
    assert checks == 4
    assert record["gates"] == {
        "qminus_bound_lt_0.015": True,
        "qplus_bound_lt_0.18": True,
        "pplus_bound_lt_1.415": True,
        "theta_ceiling_18_lt_four_pi_over_0.69": True,
    }
    corrupted = copy.deepcopy(record)
    corrupted["values"]["qplus_bound"] = "0"
    with pytest.raises(CHECKER.CheckError, match="does not contain"):
        CHECKER.verify_outer_containment(
            corrupted, independent_model, 128, "outer"
        )


def test_section_boundary_roots_are_excluded_and_window_is_closed_cover() -> None:
    ctx.prec = 128
    epsilon = (Fraction(999, 10_000), Fraction(101, 1000))
    production_model = RUNNER.build_model()
    independent_model = CHECKER.independent_model()
    expected_counts = {
        "SECTION_LOW": {"ENERGY_EXCLUDED": 1},
        "SECTION_WINDOW": {"LANDING_CLOSED_WINDOW": 1},
        "SECTION_HIGH": {"ENERGY_EXCLUDED": 1},
    }
    for tree_id, root in RUNNER.SECTION_ROOTS.items():
        tree = RUNNER.build_tree(
            production_model,
            epsilon,
            bits=128,
            tree_id=tree_id,
            goal="SECTION_WINDOW_COVER",
            root_box=root,
        )
        replay = CHECKER.replay_tree(
            tree,
            epsilon,
            independent_model,
            tree_id,
            root,
        )
        assert replay["terminal_counts"] == expected_counts[tree_id]


def test_checker_rejects_decisive_interval_and_exact_split_mutations() -> None:
    ctx.prec = 128
    epsilon = (Fraction(0), Fraction(21, 10_000))
    root = {
        "qminus": (Fraction(-21, 1600), Fraction(-9, 800)),
        "qplus": (Fraction(-27, 200), Fraction(-9, 100)),
        "pminus": (Fraction(-9, 200), Fraction(-3, 100)),
        "pplus": (Fraction(-283, 200), Fraction(-849, 800)),
    }
    tree = RUNNER.build_tree(
        RUNNER.build_model(),
        epsilon,
        bits=128,
        tree_id="ANGLE_TEST",
        goal="ANGLE_COVER",
        root_box=root,
    )
    assert tree["node_count"] == 7
    replay = CHECKER.replay_tree(
        tree,
        epsilon,
        CHECKER.independent_model(),
        "ANGLE_TEST",
        root,
    )
    assert replay["terminal_counts"] == {
        "ENERGY_EXCLUDED": 2,
        "ANGLE_CERTIFIED": 2,
    }
    assert tree["internal_count"] == 3
    assert tree["terminal_count"] == 4
    assert tree["unresolved_count"] == 0
    assert tree["node_count"] == tree["internal_count"] + tree["terminal_count"]
    assert replay["content_sha256"] == tree["content_sha256"]
    extrema = tree["angle_extrema"]
    assert extrema["theta_numerator_definition"] == "omega_fast_times_N_plus"
    assert arb(extrema["minimum_D_plus_lower"]).lower() > 0
    assert arb(extrema["minimum_N_plus_lower"]).lower() > 0
    assert arb(extrema["minimum_theta_numerator_lower"]).lower() > 0
    assert arb(extrema["maximum_theta_dot_upper"]).upper() < 18

    content_hash_mutation = copy.deepcopy(tree)
    content_hash_mutation["content_sha256"] = "0" * 64
    with pytest.raises(CHECKER.CheckError, match="content hash mismatch"):
        CHECKER.replay_tree(
            content_hash_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )

    split_mutation = copy.deepcopy(tree)
    split_mutation["nodes"][0]["split_point"]["numerator"] = "-38"
    refresh_tree_content_hash(split_mutation)
    with pytest.raises(CHECKER.CheckError, match="split"):
        CHECKER.replay_tree(
            split_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )

    interval_mutation = copy.deepcopy(tree)
    terminal = next(
        node
        for node in interval_mutation["nodes"]
        if node["classification"] == "ANGLE_CERTIFIED"
    )
    terminal["decisive_intervals"]["theta_dot"] = "0"
    refresh_tree_content_hash(interval_mutation)
    with pytest.raises(CHECKER.CheckError, match="does not contain"):
        CHECKER.replay_tree(
            interval_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )

    integer_type_mutation = copy.deepcopy(tree)
    integer_type_mutation["node_count"] = float(tree["node_count"])
    refresh_tree_content_hash(integer_type_mutation)
    with pytest.raises(CHECKER.CheckError, match="exact JSON integer"):
        CHECKER.replay_tree(
            integer_type_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )

    bool_depth_mutation = copy.deepcopy(tree)
    bool_depth_mutation["nodes"][0]["depth"] = True
    refresh_tree_content_hash(bool_depth_mutation)
    with pytest.raises(CHECKER.CheckError, match="exact JSON integer"):
        CHECKER.replay_tree(
            bool_depth_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )

    count_type_mutation = copy.deepcopy(tree)
    terminal_name = next(iter(count_type_mutation["terminal_counts"]))
    count_type_mutation["terminal_counts"][terminal_name] = float(
        count_type_mutation["terminal_counts"][terminal_name]
    )
    refresh_tree_content_hash(count_type_mutation)
    with pytest.raises(CHECKER.CheckError, match="exact JSON integer"):
        CHECKER.replay_tree(
            count_type_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )

    extrema_mutation = copy.deepcopy(tree)
    extrema_mutation["angle_extrema"]["maximum_theta_dot_upper"] = "0"
    refresh_tree_content_hash(extrema_mutation)
    with pytest.raises(CHECKER.CheckError, match="does not contain"):
        CHECKER.replay_tree(
            extrema_mutation,
            epsilon,
            CHECKER.independent_model(),
            "ANGLE_TEST",
            root,
        )


def test_checker_rejects_duplicate_keys_nonfinite_json_and_source_tamper(
    tmp_path: Path,
) -> None:
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_bytes(b'{"schema_version":1,"schema_version":1}\n')
    with pytest.raises(CHECKER.CheckError, match="duplicate JSON key"):
        CHECKER.load_canonical_json(duplicate)

    nonfinite = tmp_path / "nonfinite.json"
    nonfinite.write_bytes(b'{"value":NaN}\n')
    with pytest.raises(CHECKER.CheckError, match="non-finite"):
        CHECKER.load_canonical_json(nonfinite)

    bindings = RUNNER.source_bindings()
    assert CHECKER.PLAN.name == "R401_VAL_L1_FINAL_PLAN_V2.json"
    assert bindings["l1_final_plan_sha256"] == CHECKER.sha256_file(CHECKER.PLAN)
    assert set(bindings["l1_release_chain_sha256"]) == {
        CHECKER.project_relative(path) for path in CHECKER.L1_RELEASE_CHAIN
    }
    assert len(bindings["l1_release_chain_sha256"]) == 5
    CHECKER.verify_source_bindings(bindings, "bindings")
    bindings = copy.deepcopy(bindings)
    release_path = CHECKER.project_relative(CHECKER.L1_RELEASE)
    bindings["l1_release_chain_sha256"][release_path] = "0" * 64
    with pytest.raises(CHECKER.CheckError, match="source binding"):
        CHECKER.verify_source_bindings(bindings, "bindings")


def test_manifest_rejects_path_tamper_before_filesystem_access(tmp_path: Path) -> None:
    proof_paths = [
        f"proof_{bits}_{slab}.json"
        for bits in CHECKER.PRECISIONS
        for slab in CHECKER.REPRESENTATIVE_SLABS
    ]
    summary = {"proofs": [{"path": path} for path in proof_paths]}
    files = [
        {"path": path, "sha256": "0" * 64, "size_bytes": 0}
        for path in [*proof_paths, "summary.json"]
    ]
    files[0]["path"] = "../proof_128_S000.json"
    manifest = {
        "schema_version": 1,
        "protocol_id": CHECKER.PROTOCOL_ID,
        "artifact_status": CHECKER.ARTIFACT_STATUS,
        "implementation_status": CHECKER.PASS_STATUS,
        "component_scope": CHECKER.COMPONENT_SCOPE,
        "composite_s0_passed": False,
        "scientific_licensing_enabled": False,
        "final_status": None,
        "files": files,
    }
    path = tmp_path / "manifest.json"
    path.write_bytes(CHECKER.canonical_json_bytes(manifest))
    with pytest.raises(CHECKER.CheckError, match="file set"):
        CHECKER.verify_manifest(path, summary)


def test_one_proof_schema_accounting_and_component_authority(tmp_path: Path) -> None:
    plan = RUNNER.load_plan()
    proof = RUNNER.run_one(128, "S000", plan["S000"])
    assert proof["artifact_status"] == "DRAFT_NON_LICENSING"
    assert proof["implementation_status"] == "PASS_STATIC_COMPONENT_SMOKE"
    assert proof["component_scope"] == "STATIC_ONLY"
    assert proof["composite_s0_passed"] is False
    assert proof["scientific_licensing_enabled"] is False
    assert proof["final_status"] is None
    counts = proof["counts"]
    assert counts["unresolved_count"] == 0
    assert counts["node_count"] == counts["internal_count"] + counts["terminal_count"]
    assert all(tree["unresolved_count"] == 0 for tree in proof["trees"])
    assert all(len(tree["content_sha256"]) == 64 for tree in proof["trees"])
    path = tmp_path / "proof_128_S000.json"
    path.write_bytes(RUNNER.canonical_json_bytes(proof))
    replay = CHECKER.verify_proof(
        path,
        expected_bits=128,
        expected_slab="S000",
        plan=CHECKER.load_plan(),
    )
    assert replay["unresolved_count"] == 0
    assert replay["node_count"] == counts["node_count"]
    assert replay["tree_content_sha256"] == {
        tree["tree_id"]: tree["content_sha256"] for tree in proof["trees"]
    }

    promoted = copy.deepcopy(proof)
    promoted["composite_s0_passed"] = True
    path.write_bytes(RUNNER.canonical_json_bytes(promoted))
    with pytest.raises(CHECKER.CheckError, match="composite status"):
        CHECKER.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=CHECKER.load_plan(),
        )


def test_caller_output_directory_must_be_empty(tmp_path: Path) -> None:
    occupied = tmp_path / "occupied"
    occupied.mkdir()
    (occupied / "user-data.txt").write_text("preserve", encoding="utf-8")
    with pytest.raises(FileExistsError, match="not empty"):
        RUNNER.prepare_output_directory(occupied)
    assert (occupied / "user-data.txt").read_text(encoding="utf-8") == "preserve"


def test_top_level_result_symlinks_fail_closed(tmp_path: Path) -> None:
    real_output = tmp_path / "real-output"
    real_output.mkdir()
    linked_output = tmp_path / "linked-output"
    linked_output.symlink_to(real_output, target_is_directory=True)
    assert RUNNER.main(["--output-dir", str(linked_output)]) == 1
    assert not any(real_output.iterdir())

    real_input = tmp_path / "real-input"
    real_input.mkdir()
    linked_input = tmp_path / "linked-input"
    linked_input.symlink_to(real_input, target_is_directory=True)
    assert CHECKER.main(["--input-dir", str(linked_input)]) == 1

    checker_target = tmp_path / "checker-target.json"
    checker_target.write_text("preserve\n", encoding="utf-8")
    checker_link = tmp_path / "checker-link.json"
    checker_link.symlink_to(checker_target)
    assert (
        CHECKER.main(
            [
                "--input-dir",
                str(real_input),
                "--output",
                str(checker_link),
            ]
        )
        == 1
    )
    assert checker_target.read_text(encoding="utf-8") == "preserve\n"
