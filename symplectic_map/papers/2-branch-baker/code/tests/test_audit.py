from __future__ import annotations

import json
from pathlib import Path

import pytest

from branch_baker import audit, protocol
from branch_baker.model import MarkovBakerModel


def test_every_source_locked_seed_is_mechanically_rederived() -> None:
    lock = audit.load_source_lock()
    seeds = audit.validate_split_seeds(lock)
    assert seeds == {
        split: audit.derive_seed("pcf_markov_baker_v1", split)
        for split in audit.SPLITS
    }


def test_seed_drift_is_rejected(tmp_path: Path) -> None:
    lock = audit.load_source_lock()
    lock["split_seed_derivation"]["development"] += 1
    path = tmp_path / "tampered.json"
    path.write_text(json.dumps(lock), encoding="utf-8")
    with pytest.raises(audit.AuditConfigurationError, match="seed mismatch"):
        audit.validate_split_seeds(audit.load_source_lock(path))


def test_independent_parent_factor_audit_at_reduced_test_scale() -> None:
    result = audit.independent_parent_audit(
        digits=50,
        max_period=6,
        allow_reduced_precision=True,
    )

    assert result["reduced_precision_test_mode"] is True
    assert result["external_prime_or_zero_data_accessed"] is False
    assert result["frozen_scale_executed"] is False
    assert result["interpretation"] == (
        "high-precision consistency audit, not interval certification"
    )
    assert result["periodic_factor"]["symbolic_counts"] == [0, 4, 0, 8, 0, 16]
    assert result["periodic_factor"]["parent_expected_counts"] == [1, 3, 1, 7, 1, 15]
    assert result["periodic_factor"]["numerically_distinct_parent_counts"] == [
        1,
        3,
        1,
        7,
        1,
        15,
    ]
    assert result["periodic_factor"]["boundary_duplicate_counts"] == [
        0,
        1,
        0,
        1,
        0,
        1,
    ]
    assert result["consistency_passed"] is True
    assert result["thresholds"]["residual_target"] == "1e-75"
    assert result["frozen_protocol_passed"] is False
    assert result["passed"] is True


def test_reduced_precision_requires_an_explicit_test_label() -> None:
    with pytest.raises(audit.AuditConfigurationError, match="reduced precision"):
        audit.independent_parent_audit(digits=50, max_period=2)


def test_development_float_stress_is_seeded_and_per_step() -> None:
    first = audit.run_float_stress(
        MarkovBakerModel(), split="development", points=32, steps=16
    )
    second = audit.run_float_stress(
        MarkovBakerModel(), split="development", points=32, steps=16
    )

    assert first == second
    assert first["external_prime_or_zero_data_accessed"] is False
    assert first["gate"] == {
        "authorization": "development_open",
        "verified_before_sampling": True,
    }
    assert first["expected_checks"] == 512
    assert first["completed_checks"] == 512
    assert first["long_trajectory_reversal_claimed"] is False
    assert "at every step" in first["roundtrip_definition"]
    assert first["boundary_failures"] == 0
    assert first["edge_mismatches"] == 0
    assert first["max_roundtrip_error"] < 2e-13
    assert first["frozen_scale_executed"] is False
    assert first["frozen_protocol_passed"] is False
    assert first["passed"] is True


def test_locked_split_refuses_before_sampling(monkeypatch: pytest.MonkeyPatch) -> None:
    class BombModel:
        def sample(self, *_args: object, **_kwargs: object) -> list[object]:
            raise AssertionError("sampling happened before the split gate")

    access_log_calls: list[object] = []

    def locked(_split: str) -> None:
        raise protocol.ProtocolError("locked for test")

    monkeypatch.setattr(audit.protocol, "require_split", locked)
    monkeypatch.setattr(
        audit.protocol,
        "append_access_log",
        lambda *args: access_log_calls.append(args),
    )
    with pytest.raises(protocol.ProtocolError, match="locked for test"):
        audit.run_float_stress(
            BombModel(),  # type: ignore[arg-type]
            split="validation",
            points=1,
            steps=1,
        )
    assert access_log_calls == []
