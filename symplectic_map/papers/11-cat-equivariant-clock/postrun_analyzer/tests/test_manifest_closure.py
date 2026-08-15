from __future__ import annotations

import json
from pathlib import Path

import pytest

from equivariant_clock_postrun.constants import (
    ANALYZER_AUTHORITY_PREFIX,
    ANALYZER_FILES,
    ANALYZER_JUNIT_PATH,
    ANALYZER_REVIEW_PATH,
    BASE_RESULT_FILES,
    EXECUTION_TREE_FILES,
    FINAL_RESULT_FILES,
    IMMUTABLE_ARTIFACTS,
    PREWRITE_RESULT_FILES,
    REQUIRED_ANALYZER_TESTS,
)
from equivariant_clock_postrun.manifest import (
    build_manifest,
    validate_existing_manifest,
    write_manifest,
)
from equivariant_clock_postrun.protocol import (
    analyzer_tree_sha256,
    parse_analyzer_junit,
    pretty_json_bytes,
    result_inventory,
    sha256_file,
)
from equivariant_clock_postrun.review import analyzer_authority_payload


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def _copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())


def _junit_bytes() -> bytes:
    cases = "".join(
        f'<testcase classname="postrun" name="{name}"/>'
        for name in sorted(REQUIRED_ANALYZER_TESTS)
    )
    return (
        f'<testsuite tests="{len(REQUIRED_ANALYZER_TESTS)}" failures="0" '
        f'errors="0" skipped="0">{cases}</testsuite>\n'
    ).encode("utf-8")


def _isolated_project(tmp_path: Path) -> Path:
    project = tmp_path / "paper11"
    for relative in EXECUTION_TREE_FILES:
        _copy_file(PROJECT_ROOT / relative, project / relative)
    for relative in IMMUTABLE_ARTIFACTS:
        _copy_file(PROJECT_ROOT / relative, project / relative)
    for relative in ANALYZER_FILES:
        _copy_file(
            PROJECT_ROOT / "postrun_analyzer" / relative,
            project / "postrun_analyzer" / relative,
        )
    assert set(path.name for path in (project / "results").iterdir()) == set(
        BASE_RESULT_FILES
    )
    junit_path = project / ANALYZER_JUNIT_PATH
    junit_path.write_bytes(_junit_bytes())
    junit = parse_analyzer_junit(junit_path)
    assert junit["pass"] is True
    analyzer_sha = analyzer_tree_sha256(project)
    authority = analyzer_authority_payload(
        analyzer_sha256=analyzer_sha,
        analyzer_junit_sha256=junit["sha256"],
    )
    review_path = project / ANALYZER_REVIEW_PATH
    review_path.write_text(
        "# Independent isolated analyzer fixture\n\n"
        + ANALYZER_AUTHORITY_PREFIX
        + json.dumps(authority, sort_keys=True, separators=(",", ":"))
        + "\n",
        encoding="utf-8",
    )
    return project


def test_prewrite_inventory_rejects_missing_extra_and_symlink(tmp_path: Path):
    exact = _isolated_project(tmp_path / "exact")
    assert result_inventory(exact, PREWRITE_RESULT_FILES)["pass"] is True

    missing = _isolated_project(tmp_path / "missing")
    (missing / ANALYZER_REVIEW_PATH).unlink()
    assert result_inventory(missing, PREWRITE_RESULT_FILES)["pass"] is False

    extra = _isolated_project(tmp_path / "extra")
    (extra / "results/unexpected.txt").write_text("unexpected", encoding="utf-8")
    assert result_inventory(extra, PREWRITE_RESULT_FILES)["pass"] is False

    linked = _isolated_project(tmp_path / "linked")
    target = linked / ANALYZER_REVIEW_PATH
    external = linked / "external-review.md"
    external.write_bytes(target.read_bytes())
    target.unlink()
    target.symlink_to(external)
    assert result_inventory(linked, PREWRITE_RESULT_FILES)["pass"] is False


def test_manifest_prewrite_one_shot_final_closure_and_second_write_reject(
    tmp_path: Path,
):
    project = _isolated_project(tmp_path)
    payload = build_manifest(project)
    assert payload["pass"] is True
    assert payload["first_manifest_attempt"]["state"] == "FAILED_PREWRITE_NO_FILE"
    assert payload["execution_tree"]["role"] == "IMMUTABLE_REGISTERED_CANDIDATE_EXECUTION"
    assert payload["analyzer_tree"]["role"] == (
        "POSTRUN_VALIDATOR_ONLY_NO_CANDIDATE_AUTHORITY"
    )
    output = write_manifest(project)
    assert output == project / "results/result_manifest.json"
    closure = validate_existing_manifest(project)
    assert closure["pass"] is True
    assert closure["manifest_sha256"] == sha256_file(output)
    assert set(closure["observed_result_files"]) == set(FINAL_RESULT_FILES)
    assert build_manifest(project)["pass"] is False
    with pytest.raises(FileExistsError):
        write_manifest(project)


def test_manifest_rejects_changed_missing_extra_symlink_and_json_tampering(
    tmp_path: Path,
):
    attacks = (
        "changed",
        "missing",
        "extra",
        "symlink",
        "duplicate_key",
        "malformed",
        "unknown_key",
        "wrong_type",
        "tampered_semantics",
        "duplicate_file_record",
    )
    for attack in attacks:
        project = _isolated_project(tmp_path / attack)
        manifest_path = write_manifest(project)
        assert validate_existing_manifest(project)["pass"] is True
        if attack == "changed":
            result = project / "results/EXPERIMENT_RESULTS.json"
            result.write_bytes(result.read_bytes() + b" ")
        elif attack == "missing":
            (project / ANALYZER_REVIEW_PATH).unlink()
        elif attack == "extra":
            (project / "results/unexpected.txt").write_text("extra", encoding="utf-8")
        elif attack == "symlink":
            target = project / ANALYZER_REVIEW_PATH
            external = project / "external-review.md"
            external.write_bytes(target.read_bytes())
            target.unlink()
            target.symlink_to(external)
        elif attack == "duplicate_key":
            raw = manifest_path.read_bytes()
            manifest_path.write_bytes(b'{\n  "schema": "duplicate",\n' + raw[2:])
        elif attack == "malformed":
            manifest_path.write_bytes(b"{")
        else:
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            if attack == "unknown_key":
                payload["unexpected"] = False
            elif attack == "wrong_type":
                payload["registered_audit_count"] = True
            elif attack == "tampered_semantics":
                payload["execution_tree"]["sha256"] = "0" * 64
            else:
                payload["files"].append(payload["files"][0])
            manifest_path.write_bytes(pretty_json_bytes(payload))
        assert validate_existing_manifest(project)["pass"] is False, attack
