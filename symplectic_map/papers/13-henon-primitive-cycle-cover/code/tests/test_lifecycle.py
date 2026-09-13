from copy import deepcopy
import json
import os
import shutil

import pytest
from jsonschema import Draft202012Validator

from candidate_v1.bootstrap import canonical, lifecycle
from candidate_v1.bootstrap.canonical import (
    canonical_bytes,
    strict_canonical_load,
    write_bytes_exclusive,
    write_json_exclusive,
)
from candidate_v1.bootstrap.constants import (
    CANDIDATE_ID,
    CANDIDATE_VERSION,
    CLAIM_RELATIVE,
    EXECUTION_STAGE_RELATIVE,
    RAW_RESULT_RELATIVE,
    Q_STAGE_RELATIVE,
    R_STAGE_RELATIVE,
    RESULT_MANIFEST_RELATIVE,
    REGISTERED_RUN_ID,
    TERMINAL_RELATIVE,
)


HEX_A = "a" * 64
HEX_B = "b" * 64
HEX_C = "c" * 64
HEX_D = "d" * 64
HEX_E = "e" * 64


def _claim():
    return lifecycle.build_claim(
        acceptance_ledger_sha256=HEX_E,
        code_manifest_sha256=HEX_A,
        code_tree_sha256=HEX_B,
        deployment_review_sha256=HEX_C,
        definitions_sha256=HEX_D,
        track_bindings={
            "Q": {"engine_sha256": HEX_A, "fixture_sha256": HEX_B, "runner_sha256": HEX_C},
            "R": {"engine_sha256": HEX_D, "fixture_sha256": HEX_E, "runner_sha256": HEX_A},
        },
    )


def _terminal(root):
    return strict_canonical_load((root / TERMINAL_RELATIVE).read_bytes())


def _payload(receipt):
    records = {
        "acceptance_ledger": {"schema": "P13_TEST_LEDGER"},
        "adjudication": {"schema": "P13_TEST_ADJUDICATION_RECORD"},
        "contract_presence": [
            {"contract_id": "P" + str(index), "record_class": "DEFINITION_PRESENCE_RECORD"}
            for index in range(1, 13)
        ],
        "definitions": {"schema": "P13_TEST_DEFINITIONS"},
        "q_capability": {"schema": "P13_TEST_Q_CAPABILITY"},
        "q_envelope": {"schema": "P13_TEST_Q_ENVELOPE"},
        "r_capability": {"schema": "P13_TEST_R_CAPABILITY"},
        "r_envelope": {"schema": "P13_TEST_R_ENVELOPE"},
        "registered_counters": {"registered_audit_count": 1},
    }
    payload = {
        "anti_claims": lifecycle.REGISTERED_ANTI_CLAIMS,
        "candidate_id": "henon_primitive_cycle_cover_v1",
        "claim_sha256": receipt["claim_sha256"],
        "run_id": "R100",
        "same_family_review_limitation": lifecycle.REGISTERED_SAME_FAMILY_REVIEW_LIMITATION,
        "schema": "P13_REGISTERED_AUDIT_PAYLOAD_V1",
    }
    for prefix, value in records.items():
        encoded = canonical_bytes(value)
        payload[prefix + "_canonical_json"] = encoded.decode("ascii")
        payload[prefix + "_sha256"] = canonical.sha256_bytes(encoded)
    return payload


def _write_fake_stages(root, payload):
    write_bytes_exclusive(
        root / Q_STAGE_RELATIVE, payload["q_envelope_canonical_json"].encode("ascii")
    )
    write_bytes_exclusive(
        root / R_STAGE_RELATIVE, payload["r_envelope_canonical_json"].encode("ascii")
    )


def _final_inbound_receipt(receipt):
    claim = receipt["claim"]
    return {
        "acceptance_ledger_sha256": claim["acceptance_ledger_sha256"],
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "claim_sha256": receipt["claim_sha256"],
        "code_manifest_sha256": claim["code_manifest_sha256"],
        "code_tree_sha256": claim["code_tree_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "deployment_review_sha256": claim["deployment_review_sha256"],
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_FINAL_INBOUND_REVALIDATION_V1",
        "source_lock_sha256": claim["source_lock_sha256"],
        "source_review_sha256": claim["source_review_sha256"],
        "track_bindings": claim["track_bindings"],
    }


def _final_inbound_validator(receipt):
    return lambda: _final_inbound_receipt(receipt)


def test_science_boundary_before_after_and_single_operation_call(
    paper_root, tmp_path, monkeypatch
):
    missing_root = tmp_path / "missing-final-validator"
    missing_receipt = lifecycle.create_claim(missing_root, _claim())
    missing_operation_calls = []
    with pytest.raises(TypeError, match="validator callable required"):
        lifecycle.run_after_claim(
            missing_root,
            missing_receipt,
            lambda: missing_operation_calls.append(1),
        )
    assert missing_operation_calls == []
    assert _terminal(missing_root)["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"

    early_root = tmp_path / "early"
    early_receipt = lifecycle.create_claim(early_root, _claim())
    with pytest.raises(ValueError):
        lifecycle.run_after_claim(
            early_root,
            early_receipt,
            lambda: "bare early return",
            _final_inbound_validator(early_receipt),
        )
    assert _terminal(early_root)["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"

    sealed_root = tmp_path / "sealed"
    calls = []
    receipt = lifecycle.create_claim(sealed_root, _claim())
    assert calls == []

    def operation():
        calls.append("entered")
        payload = _payload(receipt)
        _write_fake_stages(sealed_root, payload)
        return payload

    with monkeypatch.context() as local_patch:
        local_patch.setattr(lifecycle, "_validate_registered_payload", lambda payload, claim_receipt: None)
        assert lifecycle.run_after_claim(
            sealed_root,
            receipt,
            operation,
            _final_inbound_validator(receipt),
        ) == _payload(receipt)
    assert calls == ["entered"]
    stage = strict_canonical_load((sealed_root / EXECUTION_STAGE_RELATIVE).read_bytes())
    assert stage["state"] == "OPERATION_ENTERED" and stage["rerun_budget"] == 0
    assert _terminal(sealed_root)["state"] == "REGISTERED_AUDIT_SEALED"
    manifest = strict_canonical_load((sealed_root / RESULT_MANIFEST_RELATIVE).read_bytes())
    assert manifest["entry_count"] == 14
    assert _terminal(sealed_root)["result_manifest_sha256"] == canonical.sha256_bytes(
        (sealed_root / RESULT_MANIFEST_RELATIVE).read_bytes()
    )
    with pytest.raises(RuntimeError):
        lifecycle.run_after_claim(
            sealed_root,
            receipt,
            operation,
            _final_inbound_validator(receipt),
        )
    assert calls == ["entered"]
    assert _terminal(sealed_root)["rerun_permitted"] is False

    result_manifest_schema = json.loads(
        (
            paper_root
            / "code/candidate_v1/shared/result_manifest.schema.json"
        ).read_text(encoding="utf-8")
    )
    manifest_mutations = []
    missing_entry = deepcopy(manifest)
    missing_entry["entries"].pop()
    missing_entry["entry_count"] -= 1
    manifest_mutations.append((missing_entry, True))
    extra_entry = deepcopy(manifest)
    extra_entry["entries"].append(deepcopy(extra_entry["entries"][-1]))
    extra_entry["entry_count"] += 1
    manifest_mutations.append((extra_entry, True))
    stale_hash = deepcopy(manifest)
    stale_hash["entries"][0]["sha256"] = "0" * 64
    manifest_mutations.append((stale_hash, False))
    for changed_manifest, schema_must_reject in manifest_mutations:
        with pytest.raises(ValueError):
            lifecycle._validate_result_manifest(
                sealed_root, changed_manifest, _payload(receipt), receipt
            )
        if schema_must_reject:
            assert list(
                Draft202012Validator(result_manifest_schema).iter_errors(changed_manifest)
            )

    symlink_root = tmp_path / "manifest-symlink"
    shutil.copytree(sealed_root, symlink_root)
    staged_q = symlink_root / Q_STAGE_RELATIVE
    replacement = symlink_root / "q-envelope-replacement.json"
    replacement.write_bytes(staged_q.read_bytes())
    staged_q.unlink()
    staged_q.symlink_to(replacement)
    with pytest.raises(ValueError):
        lifecycle._validate_result_manifest(
            symlink_root, manifest, _payload(receipt), receipt
        )

    terminal_schema = json.loads(
        (paper_root / "code/candidate_v1/shared/terminal.schema.json").read_text(
            encoding="utf-8"
        )
    )
    pointer_drift = deepcopy(_terminal(sealed_root))
    pointer_drift["q_stage_sha256"] = None
    with pytest.raises(ValueError, match="pointer nullability"):
        lifecycle._validate_terminal_object(pointer_drift)
    assert list(Draft202012Validator(terminal_schema).iter_errors(pointer_drift))

    tamper_root = tmp_path / "tamper"
    tamper_receipt = lifecycle.create_claim(tamper_root, _claim())

    def tamper_operation():
        payload = _payload(tamper_receipt)
        _write_fake_stages(tamper_root, payload)
        (tamper_root / EXECUTION_STAGE_RELATIVE).write_bytes(b'{"schema":"ATTACKED"}\n')
        return payload

    with monkeypatch.context() as local_patch:
        local_patch.setattr(lifecycle, "_validate_registered_payload", lambda payload, claim_receipt: None)
        with pytest.raises(RuntimeError):
            lifecycle.run_after_claim(
                tamper_root,
                tamper_receipt,
                tamper_operation,
                _final_inbound_validator(tamper_receipt),
            )
    assert _terminal(tamper_root)["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"

    mutated_guard_root = tmp_path / "mutated-final-validator"
    mutated_guard_receipt = lifecycle.create_claim(mutated_guard_root, _claim())

    def mutated_guard_operation():
        payload = _payload(mutated_guard_receipt)
        _write_fake_stages(mutated_guard_root, payload)
        return payload

    def mutated_guard_validator():
        receipt_value = _final_inbound_receipt(mutated_guard_receipt)
        receipt_value["candidate_version"] = True
        return receipt_value

    with monkeypatch.context() as local_patch:
        local_patch.setattr(lifecycle, "_validate_registered_payload", lambda payload, claim_receipt: None)
        with pytest.raises(ValueError, match="validation receipt drift"):
            lifecycle.run_after_claim(
                mutated_guard_root,
                mutated_guard_receipt,
                mutated_guard_operation,
                mutated_guard_validator,
            )
    assert _terminal(mutated_guard_root)["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"

    retry_root = tmp_path / "terminal-retry"
    retry_receipt = lifecycle.create_claim(retry_root, _claim())
    original_write = lifecycle.write_json_exclusive
    injected = []

    def one_postcommit_failure(path, value):
        digest = original_write(path, value)
        if path == retry_root / TERMINAL_RELATIVE and not injected:
            injected.append(True)
            raise OSError("injected postcommit directory barrier")
        return digest

    def retry_operation():
        payload = _payload(retry_receipt)
        _write_fake_stages(retry_root, payload)
        return payload

    with monkeypatch.context() as local_patch:
        local_patch.setattr(lifecycle, "_validate_registered_payload", lambda payload, claim_receipt: None)
        local_patch.setattr(lifecycle, "write_json_exclusive", one_postcommit_failure)
        assert lifecycle.run_after_claim(
            retry_root,
            retry_receipt,
            retry_operation,
            _final_inbound_validator(retry_receipt),
        ) == _payload(retry_receipt)
    assert _terminal(retry_root)["state"] == "REGISTERED_AUDIT_SEALED"

    persistent_root = tmp_path / "terminal-persistent"
    persistent_receipt = lifecycle.create_claim(persistent_root, _claim())

    def persistent_postcommit_failure(path, value):
        digest = original_write(path, value)
        if path == persistent_root / TERMINAL_RELATIVE:
            raise OSError("persistent postcommit directory barrier")
        return digest

    def persistent_operation():
        payload = _payload(persistent_receipt)
        _write_fake_stages(persistent_root, payload)
        return payload

    with monkeypatch.context() as local_patch:
        local_patch.setattr(lifecycle, "_validate_registered_payload", lambda payload, claim_receipt: None)
        local_patch.setattr(lifecycle, "write_json_exclusive", persistent_postcommit_failure)
        local_patch.setattr(lifecycle, "fsync_directory", lambda directory: (_ for _ in ()).throw(OSError("persistent fsync")))
        with pytest.raises(lifecycle.CommittedTerminalDurabilityError):
            lifecycle.run_after_claim(
                persistent_root,
                persistent_receipt,
                persistent_operation,
                _final_inbound_validator(persistent_receipt),
            )
    assert _terminal(persistent_root)["state"] == "REGISTERED_AUDIT_SEALED"


def test_post_claim_exception_writes_terminal_and_forbids_retry(tmp_path, monkeypatch):
    receipt = lifecycle.create_claim(tmp_path, _claim())
    diagnostic = lifecycle.bounded_child_diagnostic(9, b"partial", b"failure", False)
    calls = []

    class ChildFailure(RuntimeError):
        def __init__(self):
            super().__init__("child failed")
            self.child_diagnostic = diagnostic

    def operation():
        calls.append(1)
        raise ChildFailure()

    with pytest.raises(ChildFailure):
        lifecycle.run_after_claim(
            tmp_path,
            receipt,
            operation,
            _final_inbound_validator(receipt),
        )
    terminal = _terminal(tmp_path)
    assert terminal["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"
    assert terminal["child_diagnostic"] == diagnostic
    assert terminal["execution_stage_path"] == EXECUTION_STAGE_RELATIVE.as_posix()
    terminal_before = (tmp_path / TERMINAL_RELATIVE).read_bytes()
    with pytest.raises(RuntimeError):
        lifecycle.run_after_claim(
            tmp_path,
            receipt,
            operation,
            _final_inbound_validator(receipt),
        )
    assert calls == [1]
    assert (tmp_path / TERMINAL_RELATIVE).read_bytes() == terminal_before

    persistent_root = tmp_path / "persistent-operation-failure"
    persistent_receipt = lifecycle.create_claim(persistent_root, _claim())
    persistent_calls = []
    original_write = lifecycle.write_json_exclusive

    def persistent_terminal_commit_failure(path, value):
        digest = original_write(path, value)
        if path == persistent_root / TERMINAL_RELATIVE:
            raise OSError("persistent operation-failure terminal barrier")
        return digest

    def persistent_failing_operation():
        persistent_calls.append(1)
        raise ChildFailure()

    with monkeypatch.context() as local_patch:
        local_patch.setattr(lifecycle, "write_json_exclusive", persistent_terminal_commit_failure)
        local_patch.setattr(
            lifecycle,
            "fsync_directory",
            lambda directory: (_ for _ in ()).throw(OSError("persistent terminal fsync")),
        )
        with pytest.raises(lifecycle.CommittedTerminalDurabilityError) as captured:
            lifecycle.run_after_claim(
                persistent_root,
                persistent_receipt,
                persistent_failing_operation,
                _final_inbound_validator(persistent_receipt),
            )
    assert persistent_calls == [1]
    assert isinstance(captured.value.__cause__, ChildFailure)
    persistent_terminal_bytes = (persistent_root / TERMINAL_RELATIVE).read_bytes()
    assert strict_canonical_load(persistent_terminal_bytes)["state"] == (
        "REGISTERED_AUDIT_TERMINAL_FAIL"
    )
    with pytest.raises(RuntimeError):
        lifecycle.run_after_claim(
            persistent_root,
            persistent_receipt,
            persistent_failing_operation,
            _final_inbound_validator(persistent_receipt),
        )
    assert persistent_calls == [1]
    assert (persistent_root / TERMINAL_RELATIVE).read_bytes() == persistent_terminal_bytes


def test_post_claim_drift_raw_pointer_and_evil_diagnostic_getter_terminalize(tmp_path):
    drift_root = tmp_path / "drift"
    receipt = lifecycle.create_claim(drift_root, _claim())
    (drift_root / CLAIM_RELATIVE).write_bytes(b"{}\n")
    called = []
    with pytest.raises(RuntimeError):
        lifecycle.run_after_claim(
            drift_root,
            receipt,
            lambda: called.append(1),
            _final_inbound_validator(receipt),
        )
    assert called == []
    assert "DURABLE CLAIM DRIFT" not in _terminal(drift_root)["failure_code"]
    assert _terminal(drift_root)["claim_sha256"] == receipt["claim_sha256"]

    raw_root = tmp_path / "raw"
    raw_receipt = lifecycle.create_claim(raw_root, _claim())

    class EvilDiagnostic(RuntimeError):
        @property
        def child_diagnostic(self):
            raise LookupError("getter attack")

    def raw_then_fail():
        write_json_exclusive(raw_root / RAW_RESULT_RELATIVE, {"partial": True})
        raise EvilDiagnostic("after raw")

    with pytest.raises(EvilDiagnostic):
        lifecycle.run_after_claim(
            raw_root,
            raw_receipt,
            raw_then_fail,
            _final_inbound_validator(raw_receipt),
        )
    terminal = _terminal(raw_root)
    assert terminal["child_diagnostic"] is None
    assert terminal["failure_code"].endswith("_INVALID_CHILD_DIAGNOSTIC")
    assert terminal["result_path"] == RAW_RESULT_RELATIVE.as_posix()
    assert len(terminal["result_sha256"]) == 64


def test_claim_commit_fsync_failure_is_terminal_after_boundary_crossing(tmp_path, monkeypatch):
    original_directory_fsync = canonical.fsync_directory
    claim_path = tmp_path / CLAIM_RELATIVE

    def fail_directory_fsync(_directory):
        if claim_path.is_file():
            raise OSError("injected directory fsync failure")
        return original_directory_fsync(_directory)

    with monkeypatch.context() as local_patch:
        local_patch.setattr(canonical, "fsync_directory", fail_directory_fsync)
        with pytest.raises(OSError):
            lifecycle.create_claim(tmp_path, _claim())
    assert (tmp_path / CLAIM_RELATIVE).is_file()
    assert (tmp_path / TERMINAL_RELATIVE).is_file()
    terminal = _terminal(tmp_path)
    assert terminal["failure_code"] == "CLAIM_COMMIT_OSERROR"
    assert terminal["rerun_permitted"] is False


def test_diagnostic_and_symlink_guards_are_bounded(tmp_path, monkeypatch):
    payload = b"\xff" * 5000
    stream = lifecycle._stream_diagnostic(payload)
    assert stream["byte_count"] == 5000
    assert len(stream["text"]) == lifecycle.DIAGNOSTIC_TEXT_LIMIT
    assert stream["truncated"] is True
    diagnostic = lifecycle.bounded_child_diagnostic(None, payload, b"", True)
    lifecycle.validate_child_diagnostic(diagnostic)

    real = tmp_path / "real"
    real.mkdir()
    link = tmp_path / "link"
    link.symlink_to(real, target_is_directory=True)
    with pytest.raises(ValueError):
        canonical.write_bytes_exclusive(link / "escape.json", b"{}\n")
    assert not (real / "escape.json").exists()

    durability_root = tmp_path / "durability-order"
    durability_root.mkdir()
    target = durability_root / "runtime/candidate_v1/official/record.json"
    original_fsync_directory = canonical.fsync_directory
    observed_barriers = []

    def record_directory_barrier(directory):
        observed_barriers.append(directory)
        return original_fsync_directory(directory)

    with monkeypatch.context() as local_patch:
        local_patch.setattr(canonical, "fsync_directory", record_directory_barrier)
        canonical.write_bytes_exclusive(target, b"{}\n")
    assert observed_barriers == [
        durability_root,
        durability_root / "runtime",
        durability_root / "runtime/candidate_v1",
        durability_root / "runtime/candidate_v1/official",
    ]

    cleanup_root = tmp_path / "partial-cleanup-order"
    cleanup_root.mkdir()
    cleanup_target = cleanup_root / "runtime/candidate_v1/official/partial.json"
    cleanup_barriers = []

    def record_cleanup_barrier(directory):
        cleanup_barriers.append(directory)
        return original_fsync_directory(directory)

    with monkeypatch.context() as local_patch:
        local_patch.setattr(canonical, "fsync_directory", record_cleanup_barrier)
        local_patch.setattr(
            canonical.os,
            "write",
            lambda descriptor, payload: (_ for _ in ()).throw(OSError("injected partial write")),
        )
        with pytest.raises(OSError, match="injected partial write"):
            canonical.write_bytes_exclusive(cleanup_target, b"{}\n")
    assert not cleanup_target.exists()
    assert cleanup_barriers == [
        cleanup_root,
        cleanup_root / "runtime",
        cleanup_root / "runtime/candidate_v1",
        cleanup_root / "runtime/candidate_v1/official",
    ]
