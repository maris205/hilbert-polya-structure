from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from branch_baker import protocol


def test_source_lock_hash_and_seed_rule() -> None:
    lock = json.loads(protocol.SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
    assert lock["lock_version"] == 2
    rule = lock["split_seed_derivation"]
    for split in ("development", "validation", "test"):
        digest = hashlib.sha256(
            f"pcf_markov_baker_v1:{split}".encode("utf-8")
        ).digest()
        assert rule[split] == int.from_bytes(digest[:8], "big")


def test_source_lock_checksum_file() -> None:
    checksum_path = protocol.EXPERIMENTS_ROOT / "SOURCE_LOCK.sha256"
    expected = checksum_path.read_text(encoding="utf-8").split()[0]
    assert protocol.sha256_file(protocol.SOURCE_LOCK_PATH) == expected


def test_validation_and_test_default_to_locked(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setattr(protocol, "VALIDATION_UNLOCK_PATH", tmp_path / "missing-v.json")
    monkeypatch.setattr(protocol, "TEST_UNLOCK_PATH", tmp_path / "missing-t.json")
    protocol.require_split("development")
    with pytest.raises(protocol.ProtocolError, match="Validation is locked"):
        protocol.require_split("validation")
    with pytest.raises(protocol.ProtocolError, match="Sealed test is locked"):
        protocol.require_split("test")


def test_write_json_new_refuses_overwrite(tmp_path: Path) -> None:
    target = tmp_path / "artifact.json"
    protocol.write_json_new(target, {"a": 1})
    with pytest.raises(protocol.ProtocolError, match="Refusing to overwrite"):
        protocol.write_json_new(target, {"a": 2})


def test_validation_unlock_rejects_incomplete_or_extra_artifact_sets() -> None:
    with pytest.raises(protocol.ProtocolError, match="frozen whitelist"):
        protocol.build_validation_unlock(
            [protocol.CODE_ROOT / "README.md"], "2026-08-13T00:00:00+00:00"
        )
    required = [
        protocol.PROJECT_ROOT / relative
        for relative in protocol.REQUIRED_DEVELOPMENT_ARTIFACTS
    ]
    with pytest.raises(protocol.ProtocolError, match="frozen whitelist"):
        protocol.build_validation_unlock(
            required + [protocol.CODE_ROOT / "README.md"],
            "2026-08-13T00:00:00+00:00",
        )


def test_validation_manifest_rejects_arbitrary_hash_keys(
    monkeypatch, tmp_path: Path
) -> None:
    marker = {
        "candidate_id": "pcf_markov_baker_v1",
        "source_lock_sha256": protocol.sha256_file(protocol.SOURCE_LOCK_PATH),
        "code_tree_sha256": protocol.code_tree_sha256(),
        "analysis_sha256": protocol.analysis_script_sha256(),
        "development_artifacts": {"code/README.md": protocol.sha256_file(protocol.CODE_ROOT / "README.md")},
    }
    path = tmp_path / "validation_unlock.json"
    path.write_text(json.dumps(marker), encoding="utf-8")
    monkeypatch.setattr(protocol, "VALIDATION_UNLOCK_PATH", path)
    with pytest.raises(protocol.ProtocolError, match="artifact keys"):
        protocol.verify_validation_unlock()


def test_validation_unlock_requires_explicit_preaccess_false(
    monkeypatch, tmp_path: Path
) -> None:
    marker = {
        "candidate_id": "pcf_markov_baker_v1",
        "source_lock_sha256": protocol.sha256_file(protocol.SOURCE_LOCK_PATH),
        "code_tree_sha256": protocol.code_tree_sha256(),
        "analysis_sha256": protocol.analysis_script_sha256(),
        "development_artifacts": {
            relative: "0" * 64
            for relative in protocol.REQUIRED_DEVELOPMENT_ARTIFACTS
        },
        "validation_accessed_before_unlock": True,
        "test_accessed_before_unlock": False,
    }
    path = tmp_path / "validation_unlock.json"
    path.write_text(json.dumps(marker), encoding="utf-8")
    monkeypatch.setattr(protocol, "VALIDATION_UNLOCK_PATH", path)
    monkeypatch.setattr(protocol, "verify_hash_map", lambda _entries: None)
    with pytest.raises(protocol.ProtocolError, match="explicitly record"):
        protocol.verify_validation_unlock()


def test_static_isolation_scope_contains_no_forbidden_token() -> None:
    lock = json.loads(protocol.SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
    forbidden = lock["static_isolation_forbidden_tokens"]
    exempt = {
        "code/tests/test_protocol.py",
    }
    violations: list[str] = []
    for path in protocol.CODE_ROOT.rglob("*.py"):
        relative = path.relative_to(protocol.PROJECT_ROOT).as_posix()
        if relative in exempt:
            continue
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text:
                violations.append(f"{relative}:{token}")
    assert violations == []
