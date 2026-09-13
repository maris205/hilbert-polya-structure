"""The sole inert-until-reviewed R100 parent transaction.

Safe preflight never calls this module's registered transaction.  The unique
entry fresh-gates the frozen package, creates the one claim, and hands it to
the one-shot lifecycle in the same process.
"""

from pathlib import Path

from candidate_v1.adjudicator.adjudicate import adjudicate
from candidate_v1.bootstrap.canonical import (
    canonical_bytes,
    read_regular_bytes,
    sha256_bytes,
    strict_canonical_load,
    write_bytes_exclusive,
)
from candidate_v1.bootstrap.constants import (
    ACCEPTANCE_LEDGER_RELATIVE,
    CANDIDATE_ID,
    CANDIDATE_VERSION,
    CLAIM_RELATIVE,
    CODE_MANIFEST_RELATIVE,
    DEFINITIONS_RELATIVE,
    DEPLOYMENT_REVIEW_RELATIVE,
    PREFLIGHT_RELATIVE,
    JUNIT_RELATIVE,
    Q_FIXTURE_RELATIVE,
    Q_ENGINE_RELATIVE,
    Q_RUNNER_RELATIVE,
    Q_STAGE_RELATIVE,
    R_FIXTURE_RELATIVE,
    R_ENGINE_RELATIVE,
    R_RUNNER_RELATIVE,
    RUNTIME_RELATIVE,
    R_STAGE_RELATIVE,
    REGISTERED_RUN_ID,
    REGISTERED_TRACK_TIMEOUT_SECONDS,
    SOURCE_LOCK_RELATIVE,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_RELATIVE,
    SOURCE_REVIEW_SHA256,
    TERMINAL_RELATIVE,
)
from candidate_v1.bootstrap.launcher import _registered_token, launch_registered_track
from candidate_v1.bootstrap.lifecycle import (
    REGISTERED_ANTI_CLAIMS,
    REGISTERED_SAME_FAMILY_REVIEW_LIMITATION,
    build_claim,
    create_claim,
    load_claim_receipt,
    run_after_claim,
    terminalize_failure,
)
from candidate_v1.bootstrap.manifest import (
    _code_files,
    _junit_record,
    _preflight_record,
    _validate_preflight_shape,
    code_tree_sha256,
)
from candidate_v1.bootstrap.preflight import collect_preflight


def _exact(left, right):
    try:
        return canonical_bytes(left) == canonical_bytes(right)
    except (TypeError, ValueError):
        return False


def _exact_keys(value, required, label):
    if type(value) is not dict or set(value) != set(required):
        raise ValueError("registered orchestrator shape: " + label)


def _read_bound_canonical(project_root, relative, expected_sha256):
    payload = read_regular_bytes(project_root / relative)
    if sha256_bytes(payload) != expected_sha256:
        raise RuntimeError(relative.as_posix() + " hash drift")
    return payload, strict_canonical_load(payload)


def _validate_code_manifest_live(project_root, value, claim):
    required = {
        "candidate_id",
        "code_file_count",
        "code_files",
        "code_tree_algorithm",
        "code_tree_sha256",
        "junit_sha256",
        "junit_record",
        "preflight_record",
        "preflight_sha256",
        "registered_audit_count_at_freeze",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
        "status",
    }
    _exact_keys(value, required, "code manifest")
    fixed = {
        "candidate_id": CANDIDATE_ID,
        "code_tree_algorithm": "sha256 of UTF-8 sorted path+NUL+file-sha256+LF records",
        "code_tree_sha256": claim["code_tree_sha256"],
        "registered_audit_count_at_freeze": 0,
        "schema": "P13_CODE_MANIFEST_V1",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "status": "CODE_FROZEN_FOR_INDEPENDENT_DEPLOYMENT_REVIEW",
    }
    if any(not _exact(value[key], expected) for key, expected in fixed.items()):
        raise RuntimeError("registered code-manifest fixed binding")
    fresh_files = _code_files(project_root)
    if (
        type(value["code_file_count"]) is not int
        or value["code_file_count"] != len(fresh_files)
        or not _exact(value["code_files"], fresh_files)
        or code_tree_sha256(project_root) != claim["code_tree_sha256"]
    ):
        raise RuntimeError("registered live code-tree drift")
    for key in ("junit_sha256", "preflight_sha256"):
        digest = value[key]
        if type(digest) is not str or len(digest) != 64 or any(
            character not in "0123456789abcdef" for character in digest
        ):
            raise ValueError("registered manifest digest: " + key)
    junit_record = _junit_record(
        read_regular_bytes(project_root / JUNIT_RELATIVE), claim["code_tree_sha256"]
    )
    preflight_bytes = read_regular_bytes(project_root / PREFLIGHT_RELATIVE)
    preflight_value = strict_canonical_load(preflight_bytes)
    preflight_record = _preflight_record(preflight_bytes, preflight_value)
    if not _exact(value["junit_record"], junit_record):
        raise RuntimeError("registered manifest nested JUnit record drift")
    if not _exact(value["preflight_record"], preflight_record):
        raise RuntimeError("registered manifest nested preflight record drift")
    return value


def _validate_deployment_review(value, claim, manifest):
    required = {
        "acceptance_ledger_sha256",
        "candidate_id",
        "candidate_version",
        "code_manifest_sha256",
        "code_tree_sha256",
        "definitions_sha256",
        "disposition",
        "implementation_author_is_reviewer",
        "preflight_sha256",
        "registered_audit_authorized_count",
        "registered_track_timeout_seconds",
        "reviewed_rows",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
    }
    _exact_keys(value, required, "deployment review")
    expected = {
        "acceptance_ledger_sha256": claim["acceptance_ledger_sha256"],
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "code_manifest_sha256": claim["code_manifest_sha256"],
        "code_tree_sha256": claim["code_tree_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "disposition": "DEPLOYMENT_PASS",
        "implementation_author_is_reviewer": False,
        "preflight_sha256": manifest["preflight_sha256"],
        "registered_audit_authorized_count": 1,
        "registered_track_timeout_seconds": REGISTERED_TRACK_TIMEOUT_SECONDS,
        "reviewed_rows": ["R020", "R021", "R022", "R023", "R024"],
        "schema": "P13_INDEPENDENT_DEPLOYMENT_REVIEW_V1",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
    }
    if not _exact(value, expected):
        raise RuntimeError("independent deployment-review contract drift")


def _validate_prelaunch_inputs(project_root, claim_receipt):
    claim = claim_receipt["claim"]
    if sha256_bytes(read_regular_bytes(project_root / SOURCE_LOCK_RELATIVE)) != SOURCE_LOCK_SHA256:
        raise RuntimeError("registered source-lock drift")
    if sha256_bytes(read_regular_bytes(project_root / SOURCE_REVIEW_RELATIVE)) != SOURCE_REVIEW_SHA256:
        raise RuntimeError("registered source-review drift")
    manifest_bytes, manifest = _read_bound_canonical(
        project_root, CODE_MANIFEST_RELATIVE, claim["code_manifest_sha256"]
    )
    _validate_code_manifest_live(project_root, manifest, claim)
    if sha256_bytes(manifest_bytes) != claim["code_manifest_sha256"]:
        raise RuntimeError("registered code-manifest receipt drift")
    preflight_bytes, preflight = _read_bound_canonical(
        project_root, PREFLIGHT_RELATIVE, manifest["preflight_sha256"]
    )
    boundary = preflight.get("development_execution_boundary")
    if (
        preflight.get("registered_audit_count") != 0
        or type(boundary) is not dict
        or boundary.get("top_level_run_science_call_count") != 0
        or boundary.get("scientific_child_engine_load_count") != 0
    ):
        raise RuntimeError("registered preflight development boundary drift")
    if sha256_bytes(preflight_bytes) != manifest["preflight_record"]["sha256"]:
        raise RuntimeError("registered preflight manifest cross-binding")
    review_bytes, review = _read_bound_canonical(
        project_root, DEPLOYMENT_REVIEW_RELATIVE, claim["deployment_review_sha256"]
    )
    if sha256_bytes(review_bytes) != claim["deployment_review_sha256"]:
        raise RuntimeError("registered deployment-review receipt drift")
    _validate_deployment_review(review, claim, manifest)
    ledger_bytes = read_regular_bytes(project_root / ACCEPTANCE_LEDGER_RELATIVE)
    if sha256_bytes(ledger_bytes) != claim["acceptance_ledger_sha256"]:
        raise RuntimeError("registered acceptance-ledger drift")
    definitions_bytes, definitions = _read_bound_canonical(
        project_root, DEFINITIONS_RELATIVE, claim["definitions_sha256"]
    )
    q_fixture_bytes = read_regular_bytes(project_root / Q_FIXTURE_RELATIVE)
    r_fixture_bytes = read_regular_bytes(project_root / R_FIXTURE_RELATIVE)
    if sha256_bytes(q_fixture_bytes) != claim["track_bindings"]["Q"]["fixture_sha256"]:
        raise RuntimeError("registered Q fixture drift")
    if sha256_bytes(r_fixture_bytes) != claim["track_bindings"]["R"]["fixture_sha256"]:
        raise RuntimeError("registered R fixture drift")
    return {
        "definitions": definitions,
        "definitions_bytes": definitions_bytes,
        "manifest": manifest,
        "manifest_bytes": manifest_bytes,
        "ledger_bytes": ledger_bytes,
        "q_fixture": strict_canonical_load(q_fixture_bytes),
        "r_fixture": strict_canonical_load(r_fixture_bytes),
        "static_audit": preflight["static_audit"],
        "inbound_snapshot": _capture_inbound_snapshot(project_root, claim_receipt, manifest),
    }


def _capture_inbound_snapshot(project_root, claim_receipt, manifest):
    relative_paths = (
        SOURCE_LOCK_RELATIVE,
        SOURCE_REVIEW_RELATIVE,
        CODE_MANIFEST_RELATIVE,
        JUNIT_RELATIVE,
        PREFLIGHT_RELATIVE,
        DEPLOYMENT_REVIEW_RELATIVE,
        ACCEPTANCE_LEDGER_RELATIVE,
        DEFINITIONS_RELATIVE,
        Q_RUNNER_RELATIVE,
        Q_ENGINE_RELATIVE,
        Q_FIXTURE_RELATIVE,
        R_RUNNER_RELATIVE,
        R_ENGINE_RELATIVE,
        R_FIXTURE_RELATIVE,
    )
    snapshot = {
        "claim_sha256": sha256_bytes(read_regular_bytes(project_root / CLAIM_RELATIVE)),
        "code_tree_sha256": code_tree_sha256(project_root),
        "file_sha256": {
            relative.as_posix(): sha256_bytes(read_regular_bytes(project_root / relative))
            for relative in relative_paths
        },
        "schema": "P13_REGISTERED_INBOUND_SNAPSHOT_V1",
    }
    if snapshot["claim_sha256"] != claim_receipt["claim_sha256"]:
        raise RuntimeError("registered snapshot claim drift")
    if snapshot["code_tree_sha256"] != claim_receipt["claim"]["code_tree_sha256"]:
        raise RuntimeError("registered snapshot code-tree drift")
    claim = claim_receipt["claim"]
    expected_file_sha256 = {
        SOURCE_LOCK_RELATIVE.as_posix(): SOURCE_LOCK_SHA256,
        SOURCE_REVIEW_RELATIVE.as_posix(): SOURCE_REVIEW_SHA256,
        CODE_MANIFEST_RELATIVE.as_posix(): claim["code_manifest_sha256"],
        JUNIT_RELATIVE.as_posix(): manifest["junit_sha256"],
        PREFLIGHT_RELATIVE.as_posix(): manifest["preflight_sha256"],
        DEPLOYMENT_REVIEW_RELATIVE.as_posix(): claim["deployment_review_sha256"],
        ACCEPTANCE_LEDGER_RELATIVE.as_posix(): claim["acceptance_ledger_sha256"],
        DEFINITIONS_RELATIVE.as_posix(): claim["definitions_sha256"],
        Q_RUNNER_RELATIVE.as_posix(): claim["track_bindings"]["Q"]["runner_sha256"],
        Q_ENGINE_RELATIVE.as_posix(): claim["track_bindings"]["Q"]["engine_sha256"],
        Q_FIXTURE_RELATIVE.as_posix(): claim["track_bindings"]["Q"]["fixture_sha256"],
        R_RUNNER_RELATIVE.as_posix(): claim["track_bindings"]["R"]["runner_sha256"],
        R_ENGINE_RELATIVE.as_posix(): claim["track_bindings"]["R"]["engine_sha256"],
        R_FIXTURE_RELATIVE.as_posix(): claim["track_bindings"]["R"]["fixture_sha256"],
    }
    if not _exact(snapshot["file_sha256"], expected_file_sha256):
        raise RuntimeError("registered snapshot claim-bound file drift")
    junit_record = _junit_record(
        read_regular_bytes(project_root / JUNIT_RELATIVE),
        snapshot["code_tree_sha256"],
    )
    preflight_bytes = read_regular_bytes(project_root / PREFLIGHT_RELATIVE)
    preflight = strict_canonical_load(preflight_bytes)
    _validate_preflight_shape(preflight)
    if not _exact(junit_record, manifest["junit_record"]):
        raise RuntimeError("registered snapshot nested JUnit record drift")
    if not _exact(_preflight_record(preflight_bytes, preflight), manifest["preflight_record"]):
        raise RuntimeError("registered snapshot nested preflight record drift")
    if snapshot["file_sha256"][JUNIT_RELATIVE.as_posix()] != manifest["junit_sha256"]:
        raise RuntimeError("registered snapshot JUnit drift")
    if snapshot["file_sha256"][PREFLIGHT_RELATIVE.as_posix()] != manifest["preflight_sha256"]:
        raise RuntimeError("registered snapshot preflight drift")
    return snapshot


def _verify_inbound_snapshot(project_root, claim_receipt, manifest, expected_snapshot, phase):
    observed = _capture_inbound_snapshot(project_root, claim_receipt, manifest)
    if not _exact(observed, expected_snapshot):
        raise RuntimeError("registered inbound drift after " + phase)


def _consume_final_inbound_guard(project_root, claim_receipt, guard):
    required = {"manifest_bytes", "snapshot_bytes", "state"}
    if type(guard) is not dict or set(guard) != required:
        raise ValueError("registered final-inbound guard shape")
    manifest_bytes = guard["manifest_bytes"]
    snapshot_bytes = guard["snapshot_bytes"]
    if (
        guard["state"] != "ARMED"
        or type(manifest_bytes) is not bytes
        or type(snapshot_bytes) is not bytes
    ):
        raise RuntimeError("registered final-inbound guard is not armed")
    claim = claim_receipt["claim"]
    if sha256_bytes(manifest_bytes) != claim["code_manifest_sha256"]:
        raise RuntimeError("registered final-inbound manifest receipt drift")
    if read_regular_bytes(project_root / CODE_MANIFEST_RELATIVE) != manifest_bytes:
        raise RuntimeError("registered final-inbound live manifest drift")
    manifest = strict_canonical_load(manifest_bytes)
    expected_snapshot = strict_canonical_load(snapshot_bytes)
    armed_receipt = {
        "manifest_bytes": manifest_bytes,
        "snapshot_bytes": snapshot_bytes,
        "state": "ARMED",
    }
    _verify_inbound_snapshot(
        project_root,
        claim_receipt,
        manifest,
        expected_snapshot,
        "final preterminal seal",
    )
    if (
        type(guard) is not dict
        or set(guard) != required
        or guard["state"] != armed_receipt["state"]
        or type(guard["manifest_bytes"]) is not bytes
        or guard["manifest_bytes"] != armed_receipt["manifest_bytes"]
        or type(guard["snapshot_bytes"]) is not bytes
        or guard["snapshot_bytes"] != armed_receipt["snapshot_bytes"]
    ):
        raise RuntimeError("registered final-inbound guard mutated during validation")
    guard["state"] = "CONSUMED"
    return {
        "acceptance_ledger_sha256": claim["acceptance_ledger_sha256"],
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "claim_sha256": claim_receipt["claim_sha256"],
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


def create_registered_claim_from_frozen(project_root: Path):
    """Fresh-gate and create the one claim in the unique registered process."""
    runtime = project_root / RUNTIME_RELATIVE
    if runtime.exists() or runtime.is_symlink():
        raise RuntimeError("registered runtime must be absent before fresh claim gate")
    if sha256_bytes(read_regular_bytes(project_root / SOURCE_LOCK_RELATIVE)) != SOURCE_LOCK_SHA256:
        raise RuntimeError("preclaim source-lock drift")
    if sha256_bytes(read_regular_bytes(project_root / SOURCE_REVIEW_RELATIVE)) != SOURCE_REVIEW_SHA256:
        raise RuntimeError("preclaim source-review drift")
    manifest_bytes = read_regular_bytes(project_root / CODE_MANIFEST_RELATIVE)
    manifest = strict_canonical_load(manifest_bytes)
    tree_sha256 = code_tree_sha256(project_root)
    provisional = {"code_tree_sha256": tree_sha256}
    _validate_code_manifest_live(project_root, manifest, provisional)
    junit_bytes = read_regular_bytes(project_root / JUNIT_RELATIVE)
    if sha256_bytes(junit_bytes) != manifest["junit_sha256"]:
        raise RuntimeError("preclaim JUnit hash drift")
    junit_record = _junit_record(junit_bytes, tree_sha256)
    if not _exact(junit_record, manifest["junit_record"]):
        raise RuntimeError("preclaim nested JUnit record drift")
    preflight_bytes = read_regular_bytes(project_root / PREFLIGHT_RELATIVE)
    preflight_record = _preflight_record(preflight_bytes, collect_preflight(project_root))
    if not _exact(preflight_record, manifest["preflight_record"]):
        raise RuntimeError("preclaim nested preflight record drift")
    if sha256_bytes(preflight_bytes) != manifest["preflight_sha256"]:
        raise RuntimeError("preclaim preflight hash drift")
    definitions_sha256 = sha256_bytes(read_regular_bytes(project_root / DEFINITIONS_RELATIVE))
    acceptance_ledger_sha256 = sha256_bytes(
        read_regular_bytes(project_root / ACCEPTANCE_LEDGER_RELATIVE)
    )
    track_bindings = {
        "Q": {
            "engine_sha256": sha256_bytes(read_regular_bytes(project_root / Q_ENGINE_RELATIVE)),
            "fixture_sha256": sha256_bytes(read_regular_bytes(project_root / Q_FIXTURE_RELATIVE)),
            "runner_sha256": sha256_bytes(read_regular_bytes(project_root / Q_RUNNER_RELATIVE)),
        },
        "R": {
            "engine_sha256": sha256_bytes(read_regular_bytes(project_root / R_ENGINE_RELATIVE)),
            "fixture_sha256": sha256_bytes(read_regular_bytes(project_root / R_FIXTURE_RELATIVE)),
            "runner_sha256": sha256_bytes(read_regular_bytes(project_root / R_RUNNER_RELATIVE)),
        },
    }
    deployment_review_bytes = read_regular_bytes(project_root / DEPLOYMENT_REVIEW_RELATIVE)
    deployment_review = strict_canonical_load(deployment_review_bytes)
    claim = build_claim(
        acceptance_ledger_sha256=acceptance_ledger_sha256,
        code_manifest_sha256=sha256_bytes(manifest_bytes),
        code_tree_sha256=tree_sha256,
        deployment_review_sha256=sha256_bytes(deployment_review_bytes),
        definitions_sha256=definitions_sha256,
        track_bindings=track_bindings,
    )
    _validate_deployment_review(deployment_review, claim, manifest)
    return create_claim(project_root, claim)


def _validate_access_counter_evidence(q_envelope, r_envelope):
    required = {
        "denied_cross_track_read_count",
        "denied_dynamic_loader_count",
        "denied_ledger_read_count",
        "denied_network_count",
        "denied_outside_read_count",
        "denied_outside_write_count",
        "denied_process_count",
        "denied_review_read_count",
        "denied_source_read_count",
        "run_science_call_count",
        "successful_outside_read_count",
        "successful_outside_write_count",
    }
    successful_outside_reads = 0
    successful_outside_writes = 0
    denied_outside_reads = 0
    denied_outside_writes = 0
    network_attempts = 0
    protected_reads = {"cross_track": 0, "ledger": 0, "review": 0, "source": 0}
    for track, envelope in (("Q", q_envelope), ("R", r_envelope)):
        counters = envelope["access_counters"]
        if type(counters) is not dict or set(counters) != required:
            raise ValueError(track + " registered access-counter shape")
        for key, value in counters.items():
            expected = 1 if key == "run_science_call_count" else 0
            if type(value) is not int or value != expected:
                raise RuntimeError(track + " registered access-counter evidence")
        successful_outside_reads += counters["successful_outside_read_count"]
        successful_outside_writes += counters["successful_outside_write_count"]
        denied_outside_reads += counters["denied_outside_read_count"]
        denied_outside_writes += counters["denied_outside_write_count"]
        network_attempts += counters["denied_network_count"]
        protected_reads["cross_track"] += counters["denied_cross_track_read_count"]
        protected_reads["ledger"] += counters["denied_ledger_read_count"]
        protected_reads["review"] += counters["denied_review_read_count"]
        protected_reads["source"] += counters["denied_source_read_count"]
        try:
            access_bytes = envelope["access_log_canonical_json"].encode("ascii")
        except (AttributeError, UnicodeEncodeError) as exc:
            raise ValueError(track + " registered access-log encoding") from exc
        if sha256_bytes(access_bytes) != envelope.get("access_log_sha256"):
            raise RuntimeError(track + " registered access-log hash evidence")
        access = strict_canonical_load(access_bytes)
        track_name = "track_q" if track == "Q" else "track_r"
        other_track_name = "track_r" if track == "Q" else "track_q"
        expected_access = {
            "allowed_read_counts": {
                "code/candidate_v1/shared/definitions.json": 1,
                "code/candidate_v1/" + track_name + "/engine.py": 1,
                "code/candidate_v1/" + track_name + "/private_fixture.json": 1,
                "code/candidate_v1/" + track_name + "/runner.py": 0,
            },
            "purpose": "REGISTERED_R100",
            "schema": "P13_TRACK_ACCESS_LOG_V1",
            "track": track,
        }
        if not _exact(access, expected_access):
            raise RuntimeError(track + " registered exact allowed-read evidence")
        for path, count in access["allowed_read_counts"].items():
            if type(count) is not int or count < 0:
                raise TypeError(track + " registered access-log count")
            protected_reads["cross_track"] += count if other_track_name in path else 0
            protected_reads["ledger"] += count if "acceptance_ledger" in path else 0
            protected_reads["review"] += count if "review" in path.lower() else 0
            protected_reads["source"] += count if "source_lock" in path.lower() else 0
    if any(protected_reads.values()):
        raise RuntimeError("registered protected-read evidence")
    return {
        "cross_track_scientific_read_count": protected_reads["cross_track"],
        "engine_acceptance_ledger_access_count": protected_reads["ledger"],
        "engine_review_document_access_count": protected_reads["review"],
        "engine_source_document_access_count": protected_reads["source"],
        "filesystem_read_outside_allowlist_count": successful_outside_reads + denied_outside_reads,
        "filesystem_write_outside_allowlist_count": successful_outside_writes + denied_outside_writes,
        "network_access_count": network_attempts,
    }


def _count_forbidden_authority_fields(*values):
    forbidden = {
        "machine_proof_authority",
        "machine_proof_claim",
        "machine_source_verdict",
        "proof_verdict",
        "source_verdict",
        "theorem_verdict",
    }
    count = 0
    pending = list(values)
    while pending:
        item = pending.pop()
        if type(item) is dict:
            count += sum(1 for key in item if key.lower() in forbidden)
            pending.extend(item.values())
        elif type(item) is list:
            pending.extend(item)
    return count


def _anti_claim_counter_evidence():
    expected_ids = ["AC" + str(index) for index in range(1, 13)]
    if [item.get("anti_claim_id") for item in REGISTERED_ANTI_CLAIMS] != expected_ids:
        raise RuntimeError("registered anti-claim scope evidence")
    return {
        "all_fibers_smooth_claim_count": 0,
        "arbitrary_henon_scope_claim_count": 0,
        "derivative_field_trace_confusion_count": 0,
        "formal_equals_actual_global_claim_count": 0,
    }


def _collect_registered_counters(
    static_audit,
    q_envelope,
    r_envelope,
    q_fixture,
    r_fixture,
    claim_receipt,
    definitions,
    ledger,
):
    access_evidence = _validate_access_counter_evidence(q_envelope, r_envelope)
    if (
        type(static_audit) is not dict
        or type(static_audit.get("exact_engine_count")) is not int
        or static_audit["exact_engine_count"] != 2
        or type(static_audit.get("definitions_only_shared_schema_count")) is not int
        or static_audit["definitions_only_shared_schema_count"] != 1
        or type(static_audit.get("shared_arithmetic_helper_count")) is not int
        or static_audit["shared_arithmetic_helper_count"] != 0
        or type(static_audit.get("shared_scientific_implementation_count")) is not int
        or static_audit["shared_scientific_implementation_count"] != 0
        or type(static_audit.get("shared_schema_scientific_field_count")) is not int
        or static_audit["shared_schema_scientific_field_count"] != 0
        or type(static_audit.get("third_engine_count")) is not int
        or static_audit["third_engine_count"] != 0
        or type(static_audit.get("exact_reviewed_schema_hash_count")) is not int
        or static_audit["exact_reviewed_schema_hash_count"] != 11
        or type(static_audit.get("registered_entry_file_count")) is not int
        or static_audit["registered_entry_file_count"] != 1
        or type(static_audit.get("registered_transaction_function_count")) is not int
        or static_audit["registered_transaction_function_count"] != 1
    ):
        raise RuntimeError("registered static counter evidence")
    engine_audits = static_audit.get("engine_audits")
    if type(engine_audits) is not dict or set(engine_audits) != {"Q", "R"}:
        raise RuntimeError("registered static engine inventory")
    if any(
        type(engine_audits[track].get(key)) is not int
        or engine_audits[track][key] != 0
        for track in ("Q", "R")
        for key in ("float_literal_count", "scan_loop_target_count")
    ):
        raise RuntimeError("registered exact/no-scan engine evidence")
    operation_counts = static_audit.get("closed_world_operation_counts")
    required_operation_counts = {
        "d_n_grid_scan_count",
        "interpolation_count",
        "modulus_scan_count",
        "neighbor_d_n_evaluation_count",
        "numerical_root_solve_count",
        "parameter_scan_count",
        "post_result_retune_count",
        "prime_scan_count",
        "random_seed_count",
        "stored_exploratory_value_count",
    }
    if (
        type(operation_counts) is not dict
        or set(operation_counts) != required_operation_counts
        or any(type(value) is not int or value != 0 for value in operation_counts.values())
    ):
        raise RuntimeError("registered static closed-world operation evidence")
    q_boundary = q_fixture.get("boundary")
    r_boundary = r_fixture.get("elimination_input")
    if (
        type(q_boundary) is not dict
        or type(r_boundary) is not dict
        or type(q_boundary.get("degree")) is not int
        or type(q_boundary.get("period")) is not int
        or type(r_boundary.get("degree")) is not int
        or type(r_boundary.get("cycle_length")) is not int
        or not _exact(
            [q_boundary["degree"], q_boundary["period"], r_boundary["degree"], r_boundary["cycle_length"]],
            [2, 2, 2, 2],
        )
    ):
        raise RuntimeError("registered fixed boundary evidence")
    if set(q_fixture.get("controls", {})) != {"N1", "N2", "N3", "N5", "N6", "N7", "N8"}:
        raise RuntimeError("registered Q fixed control inventory")
    if type(r_fixture.get("counter_inputs")) is not list or len(r_fixture["counter_inputs"]) != 7:
        raise RuntimeError("registered R fixed control inventory")
    claim = claim_receipt.get("claim") if type(claim_receipt) is dict else None
    if (
        type(claim) is not dict
        or type(claim.get("registered_audit_count")) is not int
        or claim["registered_audit_count"] != 1
        or type(claim.get("registered_candidate_id_count")) is not int
        or claim["registered_candidate_id_count"] != 1
        or not _exact(claim.get("candidate_id"), CANDIDATE_ID)
        or not _exact(claim.get("run_id"), REGISTERED_RUN_ID)
    ):
        raise RuntimeError("registered claim counter evidence")
    q_certificate = strict_canonical_load(
        q_envelope["certificate_canonical_json"].encode("ascii")
    )
    r_certificate = strict_canonical_load(
        r_envelope["certificate_canonical_json"].encode("ascii")
    )
    q_blocks = [
        q_certificate["controls"][control]["unsafe_inference"]
        for control in ("N1", "N2", "N3")
    ]
    r_blocks = [
        r_certificate["records"][control]["unsafe_step"]
        for control in ("N1", "N2", "N3")
    ]
    expected_blocks = [
        "REJECTED_FORMAL_TO_ACTUAL",
        "REJECTED_GENERIC_TO_ALL_FIBERS",
        "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY",
    ]
    if not _exact(q_blocks, expected_blocks) or not _exact(r_blocks, expected_blocks):
        raise RuntimeError("registered proof-audit block evidence")
    anti_claim_evidence = _anti_claim_counter_evidence()
    authority_field_count = _count_forbidden_authority_fields(
        claim,
        definitions,
        ledger,
        q_certificate,
        r_certificate,
        REGISTERED_ANTI_CLAIMS,
        REGISTERED_SAME_FAMILY_REVIEW_LIMITATION,
    )
    if type(authority_field_count) is not int or authority_field_count != 0:
        raise RuntimeError("registered machine-authority field evidence")
    counters = {
        "all_fibers_smooth_claim_count": anti_claim_evidence["all_fibers_smooth_claim_count"],
        "arbitrary_henon_scope_claim_count": anti_claim_evidence["arbitrary_henon_scope_claim_count"],
        "cross_track_scientific_read_count": access_evidence["cross_track_scientific_read_count"],
        "d_n_grid_scan_count": operation_counts["d_n_grid_scan_count"],
        "definitions_only_shared_schema_count": static_audit["definitions_only_shared_schema_count"],
        "derivative_field_trace_confusion_count": anti_claim_evidence["derivative_field_trace_confusion_count"],
        "engine_acceptance_ledger_access_count": access_evidence["engine_acceptance_ledger_access_count"],
        "engine_review_document_access_count": access_evidence["engine_review_document_access_count"],
        "engine_source_document_access_count": access_evidence["engine_source_document_access_count"],
        "exact_engine_count": static_audit["exact_engine_count"],
        "external_data_access_count": access_evidence["filesystem_read_outside_allowlist_count"] + access_evidence["network_access_count"],
        "filesystem_read_outside_allowlist_count": access_evidence["filesystem_read_outside_allowlist_count"],
        "filesystem_write_outside_allowlist_count": access_evidence["filesystem_write_outside_allowlist_count"],
        "floating_field_count": sum(engine_audits[track]["float_literal_count"] for track in ("Q", "R")),
        "formal_equals_actual_global_claim_count": anti_claim_evidence["formal_equals_actual_global_claim_count"],
        "interpolation_count": operation_counts["interpolation_count"],
        "machine_source_proof_verdict_count": authority_field_count,
        "modulus_scan_count": operation_counts["modulus_scan_count"],
        "neighbor_d_n_evaluation_count": operation_counts["neighbor_d_n_evaluation_count"],
        "network_access_count": access_evidence["network_access_count"],
        "numerical_root_solve_count": operation_counts["numerical_root_solve_count"],
        "parameter_scan_count": operation_counts["parameter_scan_count"],
        "post_result_retune_count": operation_counts["post_result_retune_count"],
        "prime_scan_count": operation_counts["prime_scan_count"],
        "proof_audit_block_count": len(q_blocks),
        "random_seed_count": operation_counts["random_seed_count"],
        "registered_audit_count": claim["registered_audit_count"],
        "registered_candidate_id_count": claim["registered_candidate_id_count"],
        "shared_arithmetic_helper_count": static_audit["shared_arithmetic_helper_count"],
        "shared_schema_scientific_field_count": static_audit["shared_schema_scientific_field_count"],
        "shared_scientific_implementation_count": static_audit["shared_scientific_implementation_count"],
        "stored_exploratory_value_count": operation_counts["stored_exploratory_value_count"],
        "third_engine_count": static_audit["third_engine_count"],
    }
    if any(type(value) is not int or value < 0 for value in counters.values()):
        raise TypeError("registered observed counter type")
    return counters


def _embedded_fields(prefix, payload_bytes):
    value = strict_canonical_load(payload_bytes)
    return {
        prefix + "_canonical_json": canonical_bytes(value).decode("ascii"),
        prefix + "_sha256": sha256_bytes(payload_bytes),
    }


def _registered_operation(project_root, claim_receipt, timeout_seconds, final_inbound_guard):
    if type(final_inbound_guard) is not dict or final_inbound_guard != {
        "manifest_bytes": None,
        "snapshot_bytes": None,
        "state": "UNSET",
    }:
        raise ValueError("registered final-inbound guard initial state")
    inputs = _validate_prelaunch_inputs(project_root, claim_receipt)
    manifest = inputs["manifest"]
    manifest_bytes = inputs["manifest_bytes"]
    snapshot_bytes = canonical_bytes(inputs["inbound_snapshot"])
    q_launch = launch_registered_track(
        project_root, "Q", claim_receipt, timeout_seconds=timeout_seconds
    )
    q_capability_bytes = q_launch["capability_bytes"]
    q_envelope_bytes = q_launch["envelope_bytes"]
    strict_canonical_load(q_envelope_bytes)
    q_stage_sha256 = sha256_bytes(q_envelope_bytes)
    write_bytes_exclusive(project_root / Q_STAGE_RELATIVE, q_envelope_bytes)
    if read_regular_bytes(project_root / Q_STAGE_RELATIVE) != q_envelope_bytes:
        raise RuntimeError("Q staged envelope seal drift")
    del q_capability_bytes
    del q_envelope_bytes
    del q_launch
    _verify_inbound_snapshot(
        project_root,
        claim_receipt,
        manifest,
        inputs["inbound_snapshot"],
        "Q seal",
    )

    r_launch = launch_registered_track(
        project_root, "R", claim_receipt, timeout_seconds=timeout_seconds
    )
    r_capability_bytes = r_launch["capability_bytes"]
    r_envelope_bytes = r_launch["envelope_bytes"]
    strict_canonical_load(r_envelope_bytes)
    r_stage_sha256 = sha256_bytes(r_envelope_bytes)
    write_bytes_exclusive(project_root / R_STAGE_RELATIVE, r_envelope_bytes)
    if read_regular_bytes(project_root / R_STAGE_RELATIVE) != r_envelope_bytes:
        raise RuntimeError("R staged envelope seal drift")
    del r_capability_bytes
    del r_envelope_bytes
    del r_launch
    _verify_inbound_snapshot(
        project_root,
        claim_receipt,
        manifest,
        inputs["inbound_snapshot"],
        "R seal",
    )

    live_q_envelope_bytes = read_regular_bytes(project_root / Q_STAGE_RELATIVE)
    live_r_envelope_bytes = read_regular_bytes(project_root / R_STAGE_RELATIVE)
    if (
        sha256_bytes(live_q_envelope_bytes) != q_stage_sha256
        or sha256_bytes(live_r_envelope_bytes) != r_stage_sha256
    ):
        raise RuntimeError("registered staged-envelope rehash drift")
    q_capability_bytes, q_capability = _registered_token(
        project_root, "Q", claim_receipt
    )
    r_capability_bytes, r_capability = _registered_token(
        project_root, "R", claim_receipt
    )
    q_envelope = strict_canonical_load(live_q_envelope_bytes)
    r_envelope = strict_canonical_load(live_r_envelope_bytes)
    if (
        q_envelope["capability_sha256"] != sha256_bytes(q_capability_bytes)
        or r_envelope["capability_sha256"] != sha256_bytes(r_capability_bytes)
        or q_capability["nonce"] == r_capability["nonce"]
    ):
        raise RuntimeError("registered staged-envelope capability rebind drift")
    q_certificate = strict_canonical_load(q_envelope["certificate_canonical_json"].encode("ascii"))
    r_certificate = strict_canonical_load(r_envelope["certificate_canonical_json"].encode("ascii"))
    ledger = strict_canonical_load(inputs["ledger_bytes"])
    counters = _collect_registered_counters(
        inputs["static_audit"],
        q_envelope,
        r_envelope,
        inputs["q_fixture"],
        inputs["r_fixture"],
        claim_receipt,
        inputs["definitions"],
        ledger,
    )
    adjudication = adjudicate(
        q_certificate,
        r_certificate,
        ledger,
        counters,
        inputs["definitions"],
    )
    adjudication_bytes = canonical_bytes(adjudication)
    contract_presence_bytes = canonical_bytes(adjudication["contract_presence_records"])
    counters_bytes = canonical_bytes(counters)
    payload = {
        "anti_claims": REGISTERED_ANTI_CLAIMS,
        "candidate_id": CANDIDATE_ID,
        "claim_sha256": claim_receipt["claim_sha256"],
        "code_manifest_sha256": claim_receipt["claim"]["code_manifest_sha256"],
        "code_tree_sha256": claim_receipt["claim"]["code_tree_sha256"],
        "definitions_sha256": claim_receipt["claim"]["definitions_sha256"],
        "deployment_review_sha256": claim_receipt["claim"]["deployment_review_sha256"],
        "run_id": REGISTERED_RUN_ID,
        "same_family_review_limitation": REGISTERED_SAME_FAMILY_REVIEW_LIMITATION,
        "schema": "P13_REGISTERED_AUDIT_PAYLOAD_V1",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
    }
    for prefix, payload_bytes in (
        ("acceptance_ledger", inputs["ledger_bytes"]),
        ("adjudication", adjudication_bytes),
        ("contract_presence", contract_presence_bytes),
        ("definitions", inputs["definitions_bytes"]),
        ("q_capability", q_capability_bytes),
        ("q_envelope", live_q_envelope_bytes),
        ("r_capability", r_capability_bytes),
        ("r_envelope", live_r_envelope_bytes),
        ("registered_counters", counters_bytes),
    ):
        payload.update(_embedded_fields(prefix, payload_bytes))
    if final_inbound_guard != {
        "manifest_bytes": None,
        "snapshot_bytes": None,
        "state": "UNSET",
    }:
        raise RuntimeError("registered final-inbound guard changed before arm")
    final_inbound_guard["manifest_bytes"] = manifest_bytes
    final_inbound_guard["snapshot_bytes"] = snapshot_bytes
    final_inbound_guard["state"] = "ARMED"
    return payload


def _validate_registered_api_inputs(project_root, timeout_seconds):
    if not isinstance(project_root, Path):
        raise TypeError("registered project root must be a Path")
    if not project_root.is_absolute():
        raise ValueError("registered project root must be absolute")
    if project_root.resolve(strict=True) != project_root:
        raise ValueError("registered project root must be canonical and non-symlinked")
    if (
        type(timeout_seconds) is not int
        or timeout_seconds != REGISTERED_TRACK_TIMEOUT_SECONDS
    ):
        raise ValueError("registered timeout must equal the frozen 30-second cap")


def execute_registered_once(
    project_root: Path,
    claim_receipt: dict,
    timeout_seconds=REGISTERED_TRACK_TIMEOUT_SECONDS,
):
    """Execute the sole authorized transaction; never called by safe tests."""
    _validate_registered_api_inputs(project_root, timeout_seconds)
    final_inbound_guard = {
        "manifest_bytes": None,
        "snapshot_bytes": None,
        "state": "UNSET",
    }

    def operation():
        return _registered_operation(
            project_root,
            claim_receipt,
            timeout_seconds,
            final_inbound_guard,
        )

    def final_preterminal_validator():
        return _consume_final_inbound_guard(
            project_root,
            claim_receipt,
            final_inbound_guard,
        )

    return run_after_claim(
        project_root,
        claim_receipt,
        operation,
        final_preterminal_validator,
    )


def run_registered_transaction(
    project_root: Path,
    timeout_seconds=REGISTERED_TRACK_TIMEOUT_SECONDS,
):
    """Fresh-gate, claim, and hand off with no uncovered post-claim gap."""
    _validate_registered_api_inputs(project_root, timeout_seconds)
    claim_receipt = None
    try:
        claim_receipt = create_registered_claim_from_frozen(project_root)
        return execute_registered_once(project_root, claim_receipt, timeout_seconds)
    except BaseException as original_error:
        terminal_path = project_root / TERMINAL_RELATIVE
        if terminal_path.exists() or terminal_path.is_symlink():
            raise
        if claim_receipt is None:
            claim_path = project_root / CLAIM_RELATIVE
            if claim_path.is_file() and not claim_path.is_symlink():
                try:
                    claim_receipt = load_claim_receipt(project_root)
                except BaseException as reconstruction_error:
                    try:
                        original_error.add_note(
                            "post-claim receipt reconstruction error: "
                            + repr(reconstruction_error)
                        )
                    except BaseException:
                        pass
        if claim_receipt is not None:
            try:
                terminalize_failure(
                    project_root,
                    claim_receipt,
                    "CLAIM_HANDOFF_" + type(original_error).__name__.upper(),
                    None,
                )
            except BaseException as terminal_error:
                try:
                    original_error.add_note(
                        "claim-handoff terminalization error: " + repr(terminal_error)
                    )
                except BaseException:
                    pass
                raise terminal_error from original_error
        raise
