from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from equivariant_clock_postrun.audit import (
    first_attempt_reproduction,
    reproduce_legacy_k005,
    validate_corrected_k005,
    validate_execution_chain,
    validate_immutable_artifacts,
    validate_immutable_execution_tree,
)
from equivariant_clock_postrun.constants import (
    ANALYZER_AUTHORITY_PREFIX,
    ANALYZER_FILES,
    EXECUTION_TREE_SHA256,
    IMMUTABLE_ARTIFACTS,
)
from equivariant_clock_postrun.protocol import (
    analyzer_tree_sha256,
    execution_tree_sha256,
    load_exact_json,
    sha256_file,
    strict_json_loads,
)
from equivariant_clock_postrun.review import (
    analyzer_authority_payload,
    parse_analyzer_authority_text,
    validate_execution_authorities,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def _copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())


def _copy_analyzer_tree(target_project: Path) -> None:
    for relative in sorted(ANALYZER_FILES):
        _copy_file(
            PROJECT_ROOT / "postrun_analyzer" / relative,
            target_project / "postrun_analyzer" / relative,
        )


def _rows() -> list[dict]:
    payload = load_exact_json(PROJECT_ROOT / "results/EXPERIMENT_RESULTS.json")
    return payload["audit"]["arithmetic_modulus_records"]


def test_analyzer_import_is_science_free_and_execution_tree_is_immutable():
    assert not any(
        name == "equivariant_clock" or name.startswith("equivariant_clock.")
        for name in sys.modules
    )
    before = {
        relative: sha256_file(PROJECT_ROOT / relative)
        for relative in IMMUTABLE_ARTIFACTS
    }
    assert execution_tree_sha256(PROJECT_ROOT) == EXECUTION_TREE_SHA256
    assert validate_immutable_execution_tree(PROJECT_ROOT)["pass"] is True
    assert validate_immutable_artifacts(PROJECT_ROOT)["pass"] is True
    after = {
        relative: sha256_file(PROJECT_ROOT / relative)
        for relative in IMMUTABLE_ARTIFACTS
    }
    assert before == after
    assert not any(
        name == "equivariant_clock" or name.startswith("equivariant_clock.")
        for name in sys.modules
    )


def test_exact_legacy_k005_failure_is_reproduced_without_artifact_mutation():
    result_path = PROJECT_ROOT / "results/EXPERIMENT_RESULTS.json"
    before = sha256_file(result_path)
    rows = _rows()
    assert reproduce_legacy_k005(rows) is False
    reproduction = first_attempt_reproduction(PROJECT_ROOT)
    assert reproduction["pass"] is True
    assert reproduction["historical_attempt"]["failure_code"] == (
        "CONTROLS_NOT_EXACT_RECOMPUTED_TRUE"
    )
    assert reproduction["historical_attempt"]["manifest_created"] is False
    assert reproduction["legacy_k005_value"] is False
    assert reproduction["corrected_k005"]["pass"] is True
    assert before == sha256_file(result_path)
    assert not (PROJECT_ROOT / "results/result_manifest.json").exists()


def test_corrected_k005_requires_singleton_json_lists_and_detects_tampering():
    rows = _rows()
    passing = validate_corrected_k005(rows)
    assert passing["pass"] is True
    assert passing["record_count"] == 174
    attacks = []
    for mutation in ("tuple", "empty", "extra", "wrong", "bad_expected"):
        changed = json.loads(json.dumps(rows))
        record = changed[0]["enumeration_engine"]["g_permutation"][
            "unique_fixing_translation_by_iterate"
        ][0]
        if mutation == "tuple":
            record["fixing_group_elements"] = tuple(record["fixing_group_elements"])
        elif mutation == "empty":
            record["fixing_group_elements"] = []
        elif mutation == "extra":
            record["fixing_group_elements"].append(record["expected_a_inverse_power"])
        elif mutation == "wrong":
            record["fixing_group_elements"] = [[[0, 0], [0, 0]]]
        else:
            record["expected_a_inverse_power"] = "not-a-matrix"
        attacks.append(validate_corrected_k005(changed)["pass"])
    assert attacks == [False, False, False, False, False]


def test_strict_json_rejects_duplicate_float_constant_and_trailing_data():
    assert strict_json_loads('{"a":1,"b":[true,false,null]}') == {
        "a": 1,
        "b": [True, False, None],
    }
    for text in (
        '{"a":1,"a":1}',
        '{"a":1.0}',
        '{"a":NaN}',
        '{"a":Infinity}',
        '{"a":1} trailing',
    ):
        with pytest.raises((json.JSONDecodeError, ValueError, TypeError)):
            strict_json_loads(text)


def test_analyzer_review_authority_is_canonical_duplicate_and_stale_closed():
    analyzer_sha = "a" * 64
    junit_sha = "b" * 64
    payload = analyzer_authority_payload(
        analyzer_sha256=analyzer_sha, analyzer_junit_sha256=junit_sha
    )
    marker = ANALYZER_AUTHORITY_PREFIX + json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    )
    assert parse_analyzer_authority_text(
        marker,
        expected_analyzer_sha256=analyzer_sha,
        expected_junit_sha256=junit_sha,
    )["pass"] is True
    assert parse_analyzer_authority_text(
        marker + "\n" + marker,
        expected_analyzer_sha256=analyzer_sha,
        expected_junit_sha256=junit_sha,
    )["pass"] is False
    assert parse_analyzer_authority_text(
        marker,
        expected_analyzer_sha256="c" * 64,
        expected_junit_sha256=junit_sha,
    )["pass"] is False
    assert parse_analyzer_authority_text(
        marker,
        expected_analyzer_sha256=analyzer_sha,
        expected_junit_sha256="d" * 64,
    )["pass"] is False
    noncanonical = ANALYZER_AUTHORITY_PREFIX + json.dumps(payload, sort_keys=False)
    assert parse_analyzer_authority_text(
        noncanonical,
        expected_analyzer_sha256=analyzer_sha,
        expected_junit_sha256=junit_sha,
    )["pass"] is False


def test_analyzer_tree_inventory_rejects_extra_and_symlink(tmp_path: Path):
    project = tmp_path / "exact"
    _copy_analyzer_tree(project)
    assert analyzer_tree_sha256(project)
    extra = project / "postrun_analyzer/unreviewed.py"
    extra.write_text("pass\n", encoding="utf-8")
    with pytest.raises(RuntimeError):
        analyzer_tree_sha256(project)

    project = tmp_path / "symlink"
    _copy_analyzer_tree(project)
    target = project / "postrun_analyzer/README.md"
    external = project / "external-readme.md"
    external.write_bytes(target.read_bytes())
    target.unlink()
    target.symlink_to(external)
    with pytest.raises(RuntimeError):
        analyzer_tree_sha256(project)


def test_immutable_chain_and_result_authorities_are_exact():
    chain = validate_execution_chain(PROJECT_ROOT)
    authorities = validate_execution_authorities(PROJECT_ROOT)
    assert chain["pass"] is True
    assert chain["result_semantics"]["corrected_k005"]["pass"] is True
    assert authorities["pass"] is True
    assert authorities["records"]["deployment_review"]["authority"]["verdict"] == (
        "DEPLOYMENT_PASS"
    )
    assert authorities["records"]["result_review"]["authority"]["verdict"] == (
        "RESULT_PASS"
    )
