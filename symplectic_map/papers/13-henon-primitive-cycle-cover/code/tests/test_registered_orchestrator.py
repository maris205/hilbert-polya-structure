from copy import deepcopy
import gc
import weakref

import pytest

from candidate_v1.bootstrap import lifecycle
from candidate_v1.bootstrap.canonical import (
    canonical_bytes,
    sha256_bytes,
    strict_canonical_load,
    write_bytes_exclusive,
)
from candidate_v1.bootstrap.constants import (
    CODE_MANIFEST_RELATIVE,
    Q_STAGE_RELATIVE,
    R_STAGE_RELATIVE,
    REGISTERED_TRACK_TIMEOUT_SECONDS,
    RUNTIME_RELATIVE,
    TERMINAL_RELATIVE,
)
from candidate_v1.orchestrator import registered
from tests.test_adjudicator_mutations import (
    TEST_MANIFEST_BYTES,
    _synthetic_registered_payload,
)


class _LaunchRecord(dict):
    __slots__ = ("__weakref__",)


def _final_inbound_receipt(receipt):
    claim = receipt["claim"]
    return {
        "acceptance_ledger_sha256": claim["acceptance_ledger_sha256"],
        "candidate_id": claim["candidate_id"],
        "candidate_version": claim["candidate_version"],
        "claim_sha256": receipt["claim_sha256"],
        "code_manifest_sha256": claim["code_manifest_sha256"],
        "code_tree_sha256": claim["code_tree_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "deployment_review_sha256": claim["deployment_review_sha256"],
        "run_id": claim["run_id"],
        "schema": "P13_FINAL_INBOUND_REVALIDATION_V1",
        "source_lock_sha256": claim["source_lock_sha256"],
        "source_review_sha256": claim["source_review_sha256"],
        "track_bindings": claim["track_bindings"],
    }


def test_registered_transaction_and_orchestration_are_science_free_and_one_shot(
    paper_root, tmp_path, monkeypatch
):
    payload, receipt = _synthetic_registered_payload(paper_root)

    operation_root = tmp_path / "orchestration"
    operation_root.mkdir()
    write_bytes_exclusive(
        operation_root / CODE_MANIFEST_RELATIVE,
        TEST_MANIFEST_BYTES,
    )
    test_manifest = strict_canonical_load(TEST_MANIFEST_BYTES)
    ledger = strict_canonical_load(payload["acceptance_ledger_canonical_json"].encode("ascii"))
    definitions = strict_canonical_load(payload["definitions_canonical_json"].encode("ascii"))
    q_envelope_bytes = payload["q_envelope_canonical_json"].encode("ascii")
    r_envelope_bytes = payload["r_envelope_canonical_json"].encode("ascii")
    q_capability_bytes = payload["q_capability_canonical_json"].encode("ascii")
    r_capability_bytes = payload["r_capability_canonical_json"].encode("ascii")
    launch_order = []
    verification_phases = []
    q_launch_reference = []

    def fake_inputs(project_root, claim_receipt):
        assert project_root == operation_root
        assert claim_receipt is receipt
        return {
            "definitions": definitions,
            "definitions_bytes": payload["definitions_canonical_json"].encode("ascii"),
            "inbound_snapshot": {"schema": "P13_TEST_SNAPSHOT"},
            "manifest": test_manifest,
            "manifest_bytes": TEST_MANIFEST_BYTES,
            "ledger_bytes": payload["acceptance_ledger_canonical_json"].encode("ascii"),
            "q_fixture": {
                "boundary": {"degree": 2, "period": 2},
                "controls": {key: {} for key in ("N1", "N2", "N3", "N5", "N6", "N7", "N8")},
            },
            "r_fixture": {
                "counter_inputs": [{"id": key} for key in ("N1", "N2", "N3", "N5", "N6", "N7", "N8")],
                "elimination_input": {"cycle_length": 2, "degree": 2},
            },
            "static_audit": {
                "closed_world_operation_counts": {
                    "d_n_grid_scan_count": 0,
                    "interpolation_count": 0,
                    "modulus_scan_count": 0,
                    "neighbor_d_n_evaluation_count": 0,
                    "numerical_root_solve_count": 0,
                    "parameter_scan_count": 0,
                    "post_result_retune_count": 0,
                    "prime_scan_count": 0,
                    "random_seed_count": 0,
                    "stored_exploratory_value_count": 0,
                },
                "definitions_only_shared_schema_count": 1,
                "engine_audits": {
                    "Q": {"float_literal_count": 0, "scan_loop_target_count": 0},
                    "R": {"float_literal_count": 0, "scan_loop_target_count": 0},
                },
                "exact_engine_count": 2,
                "exact_reviewed_schema_hash_count": 11,
                "registered_entry_file_count": 1,
                "registered_transaction_function_count": 1,
                "shared_arithmetic_helper_count": 0,
                "shared_schema_scientific_field_count": 0,
                "shared_scientific_implementation_count": 0,
                "third_engine_count": 0,
            },
        }

    def fake_launch(project_root, track, claim_receipt, timeout_seconds):
        assert project_root == operation_root
        assert claim_receipt is receipt
        assert timeout_seconds == REGISTERED_TRACK_TIMEOUT_SECONDS
        if track == "Q":
            assert not (operation_root / Q_STAGE_RELATIVE).exists()
            assert not (operation_root / R_STAGE_RELATIVE).exists()
            launch = _LaunchRecord(
                capability_bytes=q_capability_bytes,
                envelope_bytes=q_envelope_bytes,
            )
            q_launch_reference.append(weakref.ref(launch))
        else:
            assert track == "R"
            gc.collect()
            assert q_launch_reference[0]() is None
            assert (operation_root / Q_STAGE_RELATIVE).read_bytes() == q_envelope_bytes
            assert not (operation_root / R_STAGE_RELATIVE).exists()
            launch = _LaunchRecord(
                capability_bytes=r_capability_bytes,
                envelope_bytes=r_envelope_bytes,
            )
        launch_order.append(track)
        return launch

    def fake_verify(project_root, claim_receipt, manifest, snapshot, phase):
        assert project_root == operation_root
        assert claim_receipt is receipt
        assert snapshot == {"schema": "P13_TEST_SNAPSHOT"}
        if phase == "Q seal":
            assert (operation_root / Q_STAGE_RELATIVE).is_file()
            assert not (operation_root / R_STAGE_RELATIVE).exists()
        elif phase == "R seal":
            assert (operation_root / Q_STAGE_RELATIVE).is_file()
            assert (operation_root / R_STAGE_RELATIVE).is_file()
        elif phase == "final preterminal seal":
            assert (operation_root / Q_STAGE_RELATIVE).is_file()
            assert (operation_root / R_STAGE_RELATIVE).is_file()
        else:
            raise AssertionError("unexpected registered verification phase")
        verification_phases.append(phase)

    def fake_token(project_root, track, claim_receipt):
        assert project_root == operation_root and claim_receipt is receipt
        encoded = q_capability_bytes if track == "Q" else r_capability_bytes
        return encoded, strict_canonical_load(encoded)

    with monkeypatch.context() as local_patch:
        local_patch.setattr(registered, "_validate_prelaunch_inputs", fake_inputs)
        local_patch.setattr(registered, "launch_registered_track", fake_launch)
        local_patch.setattr(registered, "_verify_inbound_snapshot", fake_verify)
        local_patch.setattr(registered, "_registered_token", fake_token)
        final_inbound_guard = {
            "manifest_bytes": None,
            "snapshot_bytes": None,
            "state": "UNSET",
        }
        observed_payload = registered._registered_operation(
            operation_root,
            receipt,
            REGISTERED_TRACK_TIMEOUT_SECONDS,
            final_inbound_guard,
        )
        final_receipt = registered._consume_final_inbound_guard(
            operation_root,
            receipt,
            final_inbound_guard,
        )
    assert launch_order == ["Q", "R"]
    assert verification_phases == ["Q seal", "R seal", "final preterminal seal"]
    assert final_inbound_guard["state"] == "CONSUMED"
    assert final_receipt == _final_inbound_receipt(receipt)
    lifecycle._validate_registered_payload(observed_payload, receipt)
    observed_adjudication = strict_canonical_load(
        observed_payload["adjudication_canonical_json"].encode("ascii")
    )
    assert [
        record["contract_id"]
        for record in observed_adjudication["contract_presence_records"]
    ] == ledger["proof_contract_ids"]

    q_envelope = strict_canonical_load(q_envelope_bytes)
    r_envelope = strict_canonical_load(r_envelope_bytes)
    collected_inputs = fake_inputs(operation_root, receipt)
    for static_key in (
        "shared_schema_scientific_field_count",
        "third_engine_count",
    ):
        invalid_static = deepcopy(collected_inputs["static_audit"])
        invalid_static[static_key] = 99
        with pytest.raises(RuntimeError, match="registered static counter evidence"):
            registered._collect_registered_counters(
                invalid_static,
                q_envelope,
                r_envelope,
                collected_inputs["q_fixture"],
                collected_inputs["r_fixture"],
                receipt,
                definitions,
                ledger,
            )
    invalid_static = deepcopy(collected_inputs["static_audit"])
    invalid_static["closed_world_operation_counts"]["parameter_scan_count"] = 99
    with pytest.raises(RuntimeError, match="closed-world operation evidence"):
        registered._collect_registered_counters(
            invalid_static,
            q_envelope,
            r_envelope,
            collected_inputs["q_fixture"],
            collected_inputs["r_fixture"],
            receipt,
            definitions,
            ledger,
        )

    base_mutation_inputs = fake_inputs(operation_root, receipt)
    original_embedded_fields = registered._embedded_fields
    original_preterminal_validator = lifecycle._validate_preterminal_runtime_tree

    def run_final_inbound_mutation(case_name, mutate_during_seal):
        mutation_root = tmp_path / case_name
        mutation_root.mkdir()
        write_bytes_exclusive(mutation_root / CODE_MANIFEST_RELATIVE, TEST_MANIFEST_BYTES)
        marker_path = mutation_root / "synthetic-final-inbound.marker"
        original_marker = b"ORIGINAL_BOUND_INBOUND\n"
        write_bytes_exclusive(marker_path, original_marker)
        local_receipt = lifecycle.create_claim(mutation_root, receipt["claim"])
        marker_snapshot = {
            "marker_sha256": sha256_bytes(original_marker),
            "schema": "P13_TEST_FINAL_INBOUND_SNAPSHOT",
        }
        observed_phases = []

        def mutation_inputs(project_root, claim_receipt):
            assert project_root == mutation_root and claim_receipt is local_receipt
            result = dict(base_mutation_inputs)
            result["inbound_snapshot"] = marker_snapshot
            return result

        def mutation_launch(project_root, track, claim_receipt, timeout_seconds):
            assert project_root == mutation_root and claim_receipt is local_receipt
            assert timeout_seconds == REGISTERED_TRACK_TIMEOUT_SECONDS
            encoded_capability = (
                q_capability_bytes if track == "Q" else r_capability_bytes
            )
            encoded_envelope = q_envelope_bytes if track == "Q" else r_envelope_bytes
            return {
                "capability_bytes": encoded_capability,
                "envelope_bytes": encoded_envelope,
            }

        def mutation_token(project_root, track, claim_receipt):
            assert project_root == mutation_root and claim_receipt is local_receipt
            encoded = q_capability_bytes if track == "Q" else r_capability_bytes
            return encoded, strict_canonical_load(encoded)

        def mutation_verify(
            project_root,
            claim_receipt,
            manifest,
            expected_snapshot,
            phase,
        ):
            assert project_root == mutation_root and claim_receipt is local_receipt
            assert manifest == test_manifest
            assert expected_snapshot == marker_snapshot
            observed_phases.append(phase)
            if sha256_bytes(marker_path.read_bytes()) != expected_snapshot["marker_sha256"]:
                raise RuntimeError("synthetic final inbound marker drift")

        def mutate_after_adjudication(prefix, payload_bytes):
            fields = original_embedded_fields(prefix, payload_bytes)
            if prefix == "registered_counters" and not mutate_during_seal:
                marker_path.write_bytes(b"MUTATED_AFTER_ADJUDICATION\n")
            return fields

        def mutate_after_preterminal(*args):
            original_preterminal_validator(*args)
            marker_path.write_bytes(b"MUTATED_DURING_SEAL\n")

        with monkeypatch.context() as local_patch:
            local_patch.setattr(registered, "_validate_prelaunch_inputs", mutation_inputs)
            local_patch.setattr(registered, "launch_registered_track", mutation_launch)
            local_patch.setattr(registered, "_registered_token", mutation_token)
            local_patch.setattr(registered, "_verify_inbound_snapshot", mutation_verify)
            local_patch.setattr(registered, "_embedded_fields", mutate_after_adjudication)
            if mutate_during_seal:
                local_patch.setattr(
                    lifecycle,
                    "_validate_preterminal_runtime_tree",
                    mutate_after_preterminal,
                )
            with pytest.raises(RuntimeError, match="synthetic final inbound marker drift"):
                registered.execute_registered_once(mutation_root, local_receipt)
        terminal = strict_canonical_load(
            (mutation_root / TERMINAL_RELATIVE).read_bytes()
        )
        assert terminal["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"
        assert terminal["rerun_permitted"] is False
        assert observed_phases[:2] == ["Q seal", "R seal"]
        assert observed_phases[-1] == "final preterminal seal"

    run_final_inbound_mutation("stale-after-adjudication", False)
    run_final_inbound_mutation("stale-during-seal", True)

    normal_root = tmp_path / "normal-transaction"
    normal_root.mkdir()
    normal_operation_calls = []

    def create_normal_claim(project_root):
        return lifecycle.create_claim(project_root, receipt["claim"])

    def execute_normal(project_root, claim_receipt, timeout_seconds):
        def operation():
            normal_operation_calls.append(1)
            write_bytes_exclusive(
                project_root / Q_STAGE_RELATIVE,
                payload["q_envelope_canonical_json"].encode("ascii"),
            )
            write_bytes_exclusive(
                project_root / R_STAGE_RELATIVE,
                payload["r_envelope_canonical_json"].encode("ascii"),
            )
            return payload

        return lifecycle.run_after_claim(
            project_root,
            claim_receipt,
            operation,
            lambda: _final_inbound_receipt(claim_receipt),
        )

    with monkeypatch.context() as local_patch:
        local_patch.setattr(registered, "create_registered_claim_from_frozen", create_normal_claim)
        local_patch.setattr(registered, "execute_registered_once", execute_normal)
        assert registered.run_registered_transaction(normal_root) == payload
    assert normal_operation_calls == [1]
    assert strict_canonical_load((normal_root / TERMINAL_RELATIVE).read_bytes())["state"] == (
        "REGISTERED_AUDIT_SEALED"
    )

    handoff_root = tmp_path / "handoff-interrupt"
    handoff_root.mkdir()

    def claim_then_interrupt(project_root):
        lifecycle.create_claim(project_root, receipt["claim"])
        raise KeyboardInterrupt("injected CALL-to-STORE_FAST handoff signal")

    with monkeypatch.context() as local_patch:
        local_patch.setattr(registered, "create_registered_claim_from_frozen", claim_then_interrupt)
        with pytest.raises(KeyboardInterrupt):
            registered.run_registered_transaction(handoff_root)
    handoff_terminal = strict_canonical_load((handoff_root / TERMINAL_RELATIVE).read_bytes())
    assert handoff_terminal["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"
    assert handoff_terminal["failure_code"] == "CLAIM_HANDOFF_KEYBOARDINTERRUPT"

    assigned_handoff_root = tmp_path / "assigned-handoff-interrupt"
    assigned_handoff_root.mkdir()
    assigned_execute_calls = []

    def create_assigned_claim(project_root):
        return lifecycle.create_claim(project_root, receipt["claim"])

    def interrupt_before_lifecycle(project_root, claim_receipt, timeout_seconds):
        assigned_execute_calls.append(1)
        raise KeyboardInterrupt("injected receipt-to-lifecycle handoff signal")

    with monkeypatch.context() as local_patch:
        local_patch.setattr(
            registered, "create_registered_claim_from_frozen", create_assigned_claim
        )
        local_patch.setattr(
            registered, "execute_registered_once", interrupt_before_lifecycle
        )
        with pytest.raises(KeyboardInterrupt):
            registered.run_registered_transaction(assigned_handoff_root)
    assert assigned_execute_calls == [1]
    assigned_terminal = strict_canonical_load(
        (assigned_handoff_root / TERMINAL_RELATIVE).read_bytes()
    )
    assert assigned_terminal["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL"
    assert assigned_terminal["failure_code"] == "CLAIM_HANDOFF_KEYBOARDINTERRUPT"

    for timeout_seconds in (29, 31, True):
        invalid_root = tmp_path / ("invalid-timeout-" + str(timeout_seconds))
        invalid_root.mkdir()
        create_calls = []
        with monkeypatch.context() as local_patch:
            local_patch.setattr(
                registered,
                "create_registered_claim_from_frozen",
                lambda project_root: create_calls.append(project_root),
            )
            with pytest.raises(ValueError):
                registered.run_registered_transaction(invalid_root, timeout_seconds)
        assert create_calls == []
        assert not (invalid_root / RUNTIME_RELATIVE).exists()
