from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
CHECKER_SOURCE = ROOT / "scripts/check_r401_val_l3_a1_static_independent.py"
S0_PROOF = ROOT / "results/r401_val_l3_phase_tube_smoke/proof_128_S000.json"


def load_checker():
    name = "check_r401_val_l3_a1_static_independent_tested"
    spec = importlib.util.spec_from_file_location(name, CHECKER_SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def checker():
    return load_checker()


@pytest.fixture()
def formal_context(checker):
    return checker.FormalStaticContext(
        matrix_id="1" * 64,
        freeze_sha256="2" * 64,
        run_config_sha256="3" * 64,
        max_depth=24,
        max_nodes_per_tree=250000,
        max_nodes_per_cell=1000000,
    )


def build_formal_s0_adapter_proof(checker, context) -> dict:
    source = json.loads(S0_PROOF.read_text(encoding="utf-8"))
    tree_by_id = {tree["tree_id"]: tree for tree in source["trees"]}
    formal_trees = [
        tree_by_id[tree_id]
        for tree_id in ("ANGLE", "SECTION_LOW", "SECTION_HIGH", "SECTION_WINDOW")
    ]
    plan = checker.load_plan()
    record = plan["S000"]
    counts = dict(source["counts"])
    counts["maximum_depth"] = max(tree["maximum_depth"] for tree in formal_trees)
    payload = {
        "schema_version": 1,
        "protocol_id": "R401-VAL-L3-A1",
        "artifact_role": "STATIC_CELL_PROOF",
        "authority": "PRODUCER_ONLY",
        "scientific_licensing_enabled": False,
        "matrix_id": context.matrix_id,
        "freeze_sha256": context.freeze_sha256,
        "run_config_sha256": context.run_config_sha256,
        "component_status": None,
        "milestone_status": None,
        "theorem_status": None,
        "final_status": None,
        "evaluator_status": "STATIC_CELL_CERTIFIED",
        "slab_id": "S000",
        "precision_bits": 128,
        "epsilon": source["epsilon"],
        "period_window": source["period_window"],
        "input_echo": {
            "slab_id": "S000",
            "precision_bits": 128,
            "epsilon_lower": record["epsilon_lower"],
            "epsilon_upper": record["epsilon_upper"],
            "matrix_id": context.matrix_id,
            "freeze_sha256": context.freeze_sha256,
            "run_config_sha256": context.run_config_sha256,
            "plan_record_sha256": checker.plan_record_sha256(record),
            "max_depth": context.max_depth,
            "max_nodes_per_tree": context.max_nodes_per_tree,
            "max_nodes_per_cell": context.max_nodes_per_cell,
        },
        "claim_boundary": checker.CELL_CLAIM_BOUNDARY,
        "proof_complete": True,
        "outer_containment": source["outer_containment"],
        "trees": formal_trees,
        "counts": counts,
        "source_bindings": checker.expected_source_bindings(record),
        "proof_content_hash_definition": (
            "sha256(canonical_json(proof_without_proof_content_sha256))"
        ),
    }
    payload["proof_content_sha256"] = checker.sha256_bytes(
        checker.canonical_json_bytes(payload)
    )
    return payload


def write_payload(checker, path: Path, payload: dict) -> None:
    path.write_bytes(checker.canonical_json_bytes(payload))


def test_checker_source_is_independent() -> None:
    source = CHECKER_SOURCE.read_text(encoding="utf-8")
    assert "import evaluate_r401_val_l3_a1_static_cell" not in source
    assert "import run_r401_val_l3_a1_all_slabs" not in source
    assert "run_r401_val_l3_phase_tube_smoke" not in source


def test_checker_role_and_tree_order_match_formal_contract(checker) -> None:
    assert checker.CHECKER_ROLE == "STATIC_INDEPENDENT_CHECKER"
    assert tuple(checker.SECTION_ROOTS) == (
        "SECTION_LOW",
        "SECTION_HIGH",
        "SECTION_WINDOW",
    )


def test_checker_plan_semantics_and_binding_share_one_pinned_snapshot(
    checker, monkeypatch: pytest.MonkeyPatch
) -> None:
    original_read = checker.read_pinned_regular_bytes
    accepted_raw = original_read(checker.PLAN)
    mutated = json.loads(accepted_raw)
    mutated["slabs"][0]["epsilon_lower"] = "0.0001"
    later_raw = checker.canonical_json_bytes(mutated)
    plan_reads = 0

    def staged_read(path: Path) -> bytes:
        nonlocal plan_reads
        if path == checker.PLAN:
            plan_reads += 1
            return accepted_raw if plan_reads == 1 else later_raw
        return original_read(path)

    monkeypatch.setattr(checker, "read_pinned_regular_bytes", staged_read)
    record = checker.load_plan()["S000"]
    bindings = checker.expected_source_bindings(record)

    assert plan_reads == 1
    assert record["epsilon_lower"] == "0.0000"
    assert bindings["l1_final_plan_sha256"] == checker.sha256_bytes(accepted_raw)


def test_checker_rejects_lexical_dotdot_proof_path(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    (tmp_path / "sub").mkdir()
    alias = tmp_path / "sub" / ".." / "proof.json"
    with pytest.raises(checker.CheckError, match="dot or empty"):
        checker.verify_proof(
            alias,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_checker_cli_rejects_path_aliases(checker) -> None:
    for value in ("//tmp/proof.json", "/tmp//proof.json", "/tmp/../proof.json"):
        with pytest.raises(Exception):
            checker.canonical_absolute_argument(value)


def test_checker_upstream_replay_rejects_extra_authority_field(
    checker, monkeypatch: pytest.MonkeyPatch
) -> None:
    payloads = {
        path: checker.load_strict_json_object_with_raw(path)[0]
        for path in (
            checker.L1_SUMMARY,
            checker.L1_MANIFEST,
            checker.L1_CHECKER,
            checker.L1_POSTCHECK,
            checker.L1_RELEASE,
        )
    }
    payloads[checker.L1_SUMMARY] = dict(payloads[checker.L1_SUMMARY])
    payloads[checker.L1_SUMMARY]["theorem_status"] = "FORGED_UNAUTHORIZED"
    monkeypatch.setattr(
        checker,
        "load_strict_json_object_with_raw",
        lambda path: (payloads[path], checker.canonical_json_bytes(payloads[path])),
    )
    with pytest.raises(checker.CheckError, match="keys differ"):
        checker.independently_validate_l1_release_chain()


def test_independent_replay_accepts_read_only_s0_math_adapter(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    result = checker.verify_proof(
        path,
        expected_bits=128,
        expected_slab="S000",
        plan=checker.load_plan(),
        context=formal_context,
    )
    assert result["node_count"] == 13794
    assert result["unresolved_count"] == 0
    assert result["maximum_depth"] == 14
    assert result["interval_checks"] > result["node_count"]


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("schema_version", True),
        ("precision_bits", 128.0),
        ("evaluator_status", "STATIC_UNRESOLVED_DEPTH"),
        ("scientific_licensing_enabled", True),
        ("component_status", "PASS_STATIC_PHASE_ANCHOR_ALL_SLABS"),
        ("milestone_status", "PASS_LOCAL_PHASE_TUBE_ALL_SLABS"),
        ("final_status", "PASS_GLOBAL"),
    ],
)
def test_header_authority_and_type_mutations_fail_before_science(
    checker, formal_context, tmp_path: Path, key: str, value: object
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    payload[key] = value
    without_hash = dict(payload)
    without_hash.pop("proof_content_sha256")
    payload["proof_content_sha256"] = checker.sha256_bytes(
        checker.canonical_json_bytes(without_hash)
    )
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_content_hash_mutation_is_rejected(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    payload["proof_content_sha256"] = "0" * 64
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    with pytest.raises(checker.CheckError, match="proof content hash"):
        checker.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_recomputed_proof_cannot_exceed_frozen_resource_caps(checker, tmp_path: Path) -> None:
    context = checker.FormalStaticContext(
        matrix_id="1" * 64,
        freeze_sha256="2" * 64,
        run_config_sha256="3" * 64,
        max_depth=24,
        max_nodes_per_tree=100,
        max_nodes_per_cell=100,
    )
    payload = build_formal_s0_adapter_proof(checker, context)
    path = tmp_path / "proof.json"
    write_payload(checker, path, payload)
    with pytest.raises(checker.CheckError, match="node count exceeds"):
        checker.verify_proof(
            path,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=context,
        )


def test_proof_leaf_and_parent_aliases_are_rejected(
    checker, formal_context, tmp_path: Path
) -> None:
    payload = build_formal_s0_adapter_proof(checker, formal_context)
    real_parent = tmp_path / "real"
    real_parent.mkdir()
    real_proof = real_parent / "proof.json"
    write_payload(checker, real_proof, payload)

    leaf_alias = tmp_path / "proof-link.json"
    leaf_alias.symlink_to(real_proof)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            leaf_alias,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )

    parent_alias = tmp_path / "parent-link"
    parent_alias.symlink_to(real_parent, target_is_directory=True)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            parent_alias / "proof.json",
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )

    hard_alias = tmp_path / "proof-hard.json"
    hard_alias.hardlink_to(real_proof)
    with pytest.raises(checker.CheckError):
        checker.verify_proof(
            hard_alias,
            expected_bits=128,
            expected_slab="S000",
            plan=checker.load_plan(),
            context=formal_context,
        )


def test_context_rejects_boolean_and_integral_float_aliases(checker) -> None:
    for bad_depth in (True, 24.0):
        context = checker.FormalStaticContext(
            matrix_id="1" * 64,
            freeze_sha256="2" * 64,
            run_config_sha256="3" * 64,
            max_depth=bad_depth,
            max_nodes_per_tree=250000,
            max_nodes_per_cell=1000000,
        )
        with pytest.raises(checker.CheckError):
            checker.validate_formal_context(context)


@pytest.mark.parametrize(
    "raw",
    ['{"x":1,"x":2}\n', '{"x":NaN}\n', '{"x":1e400}\n'],
)
def test_strict_loader_rejects_duplicate_and_nonfinite(
    checker, tmp_path: Path, raw: str
) -> None:
    path = tmp_path / "bad.json"
    path.write_text(raw, encoding="utf-8")
    with pytest.raises(checker.CheckError):
        checker.load_canonical_json(path)


def test_write_once_rejects_existing_checker(checker, tmp_path: Path) -> None:
    output = tmp_path / "independent_static_checker.json"
    checker.write_once(output, b"{}\n")
    with pytest.raises(FileExistsError):
        checker.write_once(output, b"different\n")
