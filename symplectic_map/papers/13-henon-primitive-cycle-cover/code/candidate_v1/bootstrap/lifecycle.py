"""Durable one-shot claim and terminal-failure infrastructure."""

import hashlib
from pathlib import Path

from .canonical import (
    canonical_bytes,
    fsync_directory,
    read_regular_bytes,
    sha256_bytes,
    strict_canonical_load,
    write_json_exclusive,
)
from .constants import (
    CANDIDATE_ID,
    CANDIDATE_VERSION,
    CLAIM_RELATIVE,
    EXECUTION_STAGE_RELATIVE,
    OFFICIAL_RELATIVE,
    RAW_RESULT_RELATIVE,
    Q_STAGE_RELATIVE,
    R_STAGE_RELATIVE,
    RESULT_MANIFEST_RELATIVE,
    REGISTERED_RUN_ID,
    RUNTIME_RELATIVE,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
    TERMINAL_RELATIVE,
)


DIAGNOSTIC_TEXT_LIMIT = 4096
REGISTERED_ANTI_CLAIMS = [
    {
        "anti_claim_id": "AC1",
        "statement": "formal dynatomic period is not asserted equal to actual exact period on every special fiber",
    },
    {
        "anti_claim_id": "AC2",
        "statement": "primitive cover is not asserted everywhere embedded in Spec B_n",
    },
    {
        "anti_claim_id": "AC3",
        "statement": "normalization is not asserted to commute with a=0 without same-rank and nilpotent-exclusion proof",
    },
    {
        "anti_claim_id": "AC4",
        "statement": "no every-fiber smooth, reduced, or free-cyclic-torsor claim is made",
    },
    {
        "anti_claim_id": "AC5",
        "statement": "X_0^aff(n) is not asserted to be a projective compactification",
    },
    {
        "anti_claim_id": "AC6",
        "statement": "G_global is not asserted to be a subgroup of G_special; the specialization lower-bound direction is corrected",
    },
    {
        "anti_claim_id": "AC7",
        "statement": "non-base membership alone is not asserted to imply primitivity without the full S_r condition",
    },
    {
        "anti_claim_id": "AC8",
        "statement": "rho is a pointwise derivative-return trace, not a field trace or the determinant (-a)^n",
    },
    {
        "anti_claim_id": "AC9",
        "statement": "rank one does not assert that tau or rho lies outside K",
    },
    {
        "anti_claim_id": "AC10",
        "statement": "no extension to arbitrary generalized Henon maps is asserted",
    },
    {
        "anti_claim_id": "AC11",
        "statement": "a finite table, numerical roots, or a parameter scan is not treated as proof",
    },
    {
        "anti_claim_id": "AC12",
        "statement": "scalar rho primitivity, scalar quadratic tau primitivity, and formal trace-spectrum rigidity are not claimed new",
    },
]
REGISTERED_SAME_FAMILY_REVIEW_LIMITATION = {
    "correlated_error_risk_remains": True,
    "criteria_binding_available": False,
    "cross_model_review_performed": False,
    "model_family_count": 1,
    "statement": "The available review workflow uses one model family, has no cross-model review, and retains correlated-error risk.",
}
REGISTERED_COUNTER_VALUES = {
    "all_fibers_smooth_claim_count": 0,
    "arbitrary_henon_scope_claim_count": 0,
    "cross_track_scientific_read_count": 0,
    "d_n_grid_scan_count": 0,
    "definitions_only_shared_schema_count": 1,
    "derivative_field_trace_confusion_count": 0,
    "engine_acceptance_ledger_access_count": 0,
    "engine_review_document_access_count": 0,
    "engine_source_document_access_count": 0,
    "exact_engine_count": 2,
    "external_data_access_count": 0,
    "filesystem_read_outside_allowlist_count": 0,
    "filesystem_write_outside_allowlist_count": 0,
    "floating_field_count": 0,
    "formal_equals_actual_global_claim_count": 0,
    "interpolation_count": 0,
    "machine_source_proof_verdict_count": 0,
    "modulus_scan_count": 0,
    "neighbor_d_n_evaluation_count": 0,
    "network_access_count": 0,
    "numerical_root_solve_count": 0,
    "parameter_scan_count": 0,
    "post_result_retune_count": 0,
    "prime_scan_count": 0,
    "proof_audit_block_count": 3,
    "random_seed_count": 0,
    "registered_audit_count": 1,
    "registered_candidate_id_count": 1,
    "shared_arithmetic_helper_count": 0,
    "shared_schema_scientific_field_count": 0,
    "shared_scientific_implementation_count": 0,
    "stored_exploratory_value_count": 0,
    "third_engine_count": 0,
}
REGISTERED_ACCESS_COUNTERS = {
    "denied_cross_track_read_count": 0,
    "denied_dynamic_loader_count": 0,
    "denied_ledger_read_count": 0,
    "denied_network_count": 0,
    "denied_outside_read_count": 0,
    "denied_outside_write_count": 0,
    "denied_process_count": 0,
    "denied_review_read_count": 0,
    "denied_source_read_count": 0,
    "run_science_call_count": 1,
    "successful_outside_read_count": 0,
    "successful_outside_write_count": 0,
}


class CommittedTerminalDurabilityError(RuntimeError):
    """Exact terminal bytes exist, but the directory durability barrier failed."""

    terminal_committed = True


def _commit_terminal_once(project_root, terminal):
    terminal_path = project_root / TERMINAL_RELATIVE
    terminal_bytes = canonical_bytes(terminal)
    try:
        return write_json_exclusive(terminal_path, terminal)
    except BaseException as commit_error:
        committed = False
        try:
            committed = read_regular_bytes(terminal_path) == terminal_bytes
        except BaseException:
            committed = False
        if not committed:
            raise
        try:
            fsync_directory(terminal_path.parent)
        except BaseException as retry_error:
            error = CommittedTerminalDurabilityError(
                "exact terminal committed but directory durability could not be confirmed"
            )
            try:
                error.add_note("initial terminal commit error: " + repr(commit_error))
            except BaseException:
                pass
            raise error from retry_error
        return sha256_bytes(terminal_bytes)


def _json_exact(left, right):
    try:
        return canonical_bytes(left) == canonical_bytes(right)
    except (TypeError, ValueError):
        return False


def _stream_diagnostic(payload: bytes):
    if type(payload) is not bytes:
        raise TypeError("diagnostic stream must be bytes")
    clipped = payload[:DIAGNOSTIC_TEXT_LIMIT]
    expanded_text = clipped.decode("utf-8", errors="backslashreplace")
    text = expanded_text[:DIAGNOSTIC_TEXT_LIMIT]
    return {
        "byte_count": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "text": text,
        "truncated": len(payload) > len(clipped) or len(expanded_text) > len(text),
    }


def bounded_child_diagnostic(returncode, stdout, stderr, timed_out):
    if returncode is not None and type(returncode) is not int:
        raise TypeError("child return code")
    if type(timed_out) is not bool:
        raise TypeError("child timeout flag")
    if timed_out and returncode is not None:
        raise ValueError("timed-out child cannot have a return code")
    if not timed_out and returncode is None:
        raise ValueError("completed child requires a return code")
    diagnostic = {
        "returncode": returncode,
        "schema": "P13_BOUNDED_CHILD_DIAGNOSTIC_V1",
        "stderr": _stream_diagnostic(stderr),
        "stdout": _stream_diagnostic(stdout),
        "timed_out": timed_out,
    }
    validate_child_diagnostic(diagnostic)
    return diagnostic


def _is_sha256(value):
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _registered_capability_nonce(
    track,
    claim_sha256,
    runner_sha256,
    engine_sha256,
    fixture_sha256,
    definitions_sha256,
):
    if track not in {"Q", "R"} or any(
        not _is_sha256(value)
        for value in (
            claim_sha256,
            runner_sha256,
            engine_sha256,
            fixture_sha256,
            definitions_sha256,
        )
    ):
        raise ValueError("registered nonce inputs")
    material = "\0".join(
        (
            "P13_REGISTERED_CAPABILITY_NONCE_V1",
            track,
            claim_sha256,
            runner_sha256,
            engine_sha256,
            fixture_sha256,
            definitions_sha256,
        )
    ).encode("ascii")
    return sha256_bytes(material)[:32]


def _validate_stream_diagnostic(value):
    if type(value) is not dict or set(value) != {"byte_count", "sha256", "text", "truncated"}:
        raise ValueError("diagnostic stream keys")
    if type(value["byte_count"]) is not int or value["byte_count"] < 0:
        raise TypeError("diagnostic byte count")
    if not _is_sha256(value["sha256"]):
        raise ValueError("diagnostic stream hash")
    if type(value["text"]) is not str or len(value["text"]) > DIAGNOSTIC_TEXT_LIMIT:
        raise ValueError("diagnostic text bound")
    if type(value["truncated"]) is not bool:
        raise TypeError("diagnostic truncation flag")


def validate_child_diagnostic(value):
    if type(value) is not dict or set(value) != {"returncode", "schema", "stderr", "stdout", "timed_out"}:
        raise ValueError("child diagnostic keys")
    if value["schema"] != "P13_BOUNDED_CHILD_DIAGNOSTIC_V1":
        raise ValueError("child diagnostic schema")
    if type(value["timed_out"]) is not bool:
        raise TypeError("child timeout flag")
    if value["timed_out"]:
        if value["returncode"] is not None:
            raise ValueError("timed-out diagnostic return code")
    elif type(value["returncode"]) is not int:
        raise TypeError("completed diagnostic return code")
    _validate_stream_diagnostic(value["stdout"])
    _validate_stream_diagnostic(value["stderr"])


def build_claim(
    *,
    acceptance_ledger_sha256: str,
    code_manifest_sha256: str,
    code_tree_sha256: str,
    deployment_review_sha256: str,
    definitions_sha256: str,
    track_bindings: dict,
):
    required_tracks = {"Q", "R"}
    if type(track_bindings) is not dict or set(track_bindings) != required_tracks:
        raise ValueError("claim requires exactly Q and R bindings")
    for track in sorted(required_tracks):
        if set(track_bindings[track]) != {"engine_sha256", "fixture_sha256", "runner_sha256"}:
            raise ValueError("claim track binding keys")
        if any(not _is_sha256(value) for value in track_bindings[track].values()):
            raise ValueError("claim track hashes")
    hashes = (
        acceptance_ledger_sha256,
        code_manifest_sha256,
        code_tree_sha256,
        deployment_review_sha256,
        definitions_sha256,
    )
    if any(not _is_sha256(value) for value in hashes):
        raise ValueError("claim hashes")
    return {
        "acceptance_ledger_sha256": acceptance_ledger_sha256,
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "claim_state": "STARTED",
        "code_manifest_sha256": code_manifest_sha256,
        "code_tree_sha256": code_tree_sha256,
        "definitions_sha256": definitions_sha256,
        "deployment_review_sha256": deployment_review_sha256,
        "registered_audit_count": 1,
        "registered_candidate_id_count": 1,
        "rerun_budget_after_start": 0,
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_DURABLE_ONE_SHOT_CLAIM_V1",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "track_bindings": track_bindings,
    }


def _validate_claim_object(claim):
    required = {
        "acceptance_ledger_sha256",
        "candidate_id",
        "candidate_version",
        "claim_state",
        "code_manifest_sha256",
        "code_tree_sha256",
        "definitions_sha256",
        "deployment_review_sha256",
        "registered_audit_count",
        "registered_candidate_id_count",
        "rerun_budget_after_start",
        "run_id",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
        "track_bindings",
    }
    if type(claim) is not dict or set(claim) != required:
        raise ValueError("claim exact shape")
    rebuilt = build_claim(
        acceptance_ledger_sha256=claim["acceptance_ledger_sha256"],
        code_manifest_sha256=claim["code_manifest_sha256"],
        code_tree_sha256=claim["code_tree_sha256"],
        deployment_review_sha256=claim["deployment_review_sha256"],
        definitions_sha256=claim["definitions_sha256"],
        track_bindings=claim["track_bindings"],
    )
    if canonical_bytes(rebuilt) != canonical_bytes(claim):
        raise ValueError("claim fixed contract")


def _claim_receipt(project_root, claim, claim_payload):
    return {
        "claim": claim,
        "claim_bytes": claim_payload,
        "claim_sha256": sha256_bytes(claim_payload),
        "official": project_root / CLAIM_RELATIVE.parent,
    }


def create_claim(project_root: Path, claim: dict):
    runtime = project_root / RUNTIME_RELATIVE
    if runtime.exists() or runtime.is_symlink():
        raise RuntimeError("one-shot candidate runtime must be absent before claim")
    _validate_claim_object(claim)
    claim_payload = canonical_bytes(claim)
    receipt = _claim_receipt(project_root, claim, claim_payload)
    try:
        write_json_exclusive(project_root / CLAIM_RELATIVE, claim)
    except BaseException as exc:
        # A directory-fsync failure can occur after the exact claim file has
        # appeared.  From that instant the one-shot boundary is crossed, so it
        # must receive a terminal even though create_claim cannot return.
        committed = False
        try:
            committed = read_regular_bytes(project_root / CLAIM_RELATIVE) == claim_payload
        except BaseException:
            committed = False
        if committed:
            terminal_error = None
            try:
                terminalize_failure(
                    project_root,
                    receipt,
                    "CLAIM_COMMIT_" + type(exc).__name__.upper(),
                    None,
                )
            except BaseException as caught_terminal_error:
                terminal_error = caught_terminal_error
                try:
                    exc.add_note("claim-commit terminalization error: " + repr(terminal_error))
                except BaseException:
                    pass
            if isinstance(terminal_error, CommittedTerminalDurabilityError):
                raise terminal_error from exc
        raise
    return receipt


def load_claim_receipt(project_root: Path):
    """Reconstruct the immutable receipt for the sole externally created claim."""
    claim_payload = read_regular_bytes(project_root / CLAIM_RELATIVE)
    claim = strict_canonical_load(claim_payload)
    _validate_claim_object(claim)
    receipt = _claim_receipt(project_root, claim, claim_payload)
    if (project_root / TERMINAL_RELATIVE).exists() or (project_root / TERMINAL_RELATIVE).is_symlink():
        raise RuntimeError("one-shot terminal already exists")
    return receipt


def validate_claim_file(project_root: Path, expected_claim: dict):
    payload = read_regular_bytes(project_root / CLAIM_RELATIVE)
    if payload != canonical_bytes(expected_claim):
        raise RuntimeError("durable claim drift")
    return sha256_bytes(payload)


def terminalize_failure(
    project_root: Path,
    claim_receipt: dict,
    failure_code: str,
    child_diagnostic=None,
):
    if type(failure_code) is not str or not failure_code:
        raise ValueError("terminal failure code")
    if type(claim_receipt) is not dict or set(claim_receipt) != {
        "claim",
        "claim_bytes",
        "claim_sha256",
        "official",
    }:
        raise ValueError("claim receipt shape")
    claim = claim_receipt["claim"]
    claim_sha256 = claim_receipt["claim_sha256"]
    if claim_receipt["claim_bytes"] != canonical_bytes(claim):
        raise ValueError("claim receipt bytes")
    if sha256_bytes(claim_receipt["claim_bytes"]) != claim_sha256:
        raise ValueError("claim receipt hash")
    if child_diagnostic is not None:
        try:
            validate_child_diagnostic(child_diagnostic)
        except BaseException:
            child_diagnostic = None
            failure_code += "_INVALID_CHILD_DIAGNOSTIC"
    raw_path = project_root / RAW_RESULT_RELATIVE
    result_path = (
        RAW_RESULT_RELATIVE.as_posix()
        if raw_path.is_file() and not raw_path.is_symlink()
        else None
    )
    result_sha256 = None
    if raw_path.is_file() and not raw_path.is_symlink():
        result_sha256 = sha256_bytes(read_regular_bytes(raw_path))
    manifest_path = project_root / RESULT_MANIFEST_RELATIVE
    result_manifest_path = (
        RESULT_MANIFEST_RELATIVE.as_posix()
        if manifest_path.is_file() and not manifest_path.is_symlink()
        else None
    )
    result_manifest_sha256 = None
    if manifest_path.is_file() and not manifest_path.is_symlink():
        result_manifest_sha256 = sha256_bytes(read_regular_bytes(manifest_path))
    stage_pointers = {}
    for prefix, relative in (("q_stage", Q_STAGE_RELATIVE), ("r_stage", R_STAGE_RELATIVE)):
        path = project_root / relative
        stage_pointers[prefix + "_path"] = (
            relative.as_posix() if path.is_file() and not path.is_symlink() else None
        )
        stage_pointers[prefix + "_sha256"] = (
            sha256_bytes(read_regular_bytes(path))
            if path.is_file() and not path.is_symlink()
            else None
        )
    stage_path = project_root / EXECUTION_STAGE_RELATIVE
    execution_stage_path = (
        EXECUTION_STAGE_RELATIVE.as_posix()
        if stage_path.is_file() and not stage_path.is_symlink()
        else None
    )
    execution_stage_sha256 = None
    if stage_path.is_file() and not stage_path.is_symlink():
        execution_stage_sha256 = sha256_bytes(read_regular_bytes(stage_path))
    terminal = {
        "acceptance_ledger_sha256": claim["acceptance_ledger_sha256"],
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "child_diagnostic": child_diagnostic,
        "claim_sha256": claim_sha256,
        "code_manifest_sha256": claim["code_manifest_sha256"],
        "code_tree_sha256": claim["code_tree_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "deployment_review_sha256": claim["deployment_review_sha256"],
        "execution_stage_path": execution_stage_path,
        "execution_stage_sha256": execution_stage_sha256,
        "failure_code": failure_code,
        "registered_audit_count": 1,
        "q_stage_path": stage_pointers["q_stage_path"],
        "q_stage_sha256": stage_pointers["q_stage_sha256"],
        "r_stage_path": stage_pointers["r_stage_path"],
        "r_stage_sha256": stage_pointers["r_stage_sha256"],
        "result_path": result_path,
        "result_manifest_path": result_manifest_path,
        "result_manifest_sha256": result_manifest_sha256,
        "result_sha256": result_sha256,
        "rerun_permitted": False,
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_ONE_SHOT_TERMINAL_V1",
        "source_lock_sha256": claim["source_lock_sha256"],
        "source_review_sha256": claim["source_review_sha256"],
        "state": "REGISTERED_AUDIT_TERMINAL_FAIL",
    }
    _validate_terminal_object(terminal)
    return _commit_terminal_once(project_root, terminal)


def _validate_terminal_object(value):
    required = {
        "acceptance_ledger_sha256",
        "candidate_id",
        "candidate_version",
        "child_diagnostic",
        "claim_sha256",
        "code_manifest_sha256",
        "code_tree_sha256",
        "definitions_sha256",
        "deployment_review_sha256",
        "execution_stage_path",
        "execution_stage_sha256",
        "failure_code",
        "registered_audit_count",
        "q_stage_path",
        "q_stage_sha256",
        "r_stage_path",
        "r_stage_sha256",
        "result_path",
        "result_manifest_path",
        "result_manifest_sha256",
        "result_sha256",
        "rerun_permitted",
        "run_id",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
        "state",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError("terminal exact shape")
    fixed = {
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "registered_audit_count": 1,
        "rerun_permitted": False,
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_ONE_SHOT_TERMINAL_V1",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
    }
    if any(not _json_exact(value[key], expected) for key, expected in fixed.items()):
        raise ValueError("terminal fixed field")
    if value["state"] not in {"REGISTERED_AUDIT_TERMINAL_FAIL", "REGISTERED_AUDIT_SEALED"}:
        raise ValueError("terminal state")
    for key in (
        "acceptance_ledger_sha256",
        "claim_sha256",
        "code_manifest_sha256",
        "code_tree_sha256",
        "definitions_sha256",
        "deployment_review_sha256",
    ):
        if not _is_sha256(value[key]):
            raise ValueError("terminal hash: " + key)
    pointer_paths = {
        "execution_stage": EXECUTION_STAGE_RELATIVE.as_posix(),
        "q_stage": Q_STAGE_RELATIVE.as_posix(),
        "r_stage": R_STAGE_RELATIVE.as_posix(),
        "result": RAW_RESULT_RELATIVE.as_posix(),
        "result_manifest": RESULT_MANIFEST_RELATIVE.as_posix(),
    }
    for prefix, fixed_path in pointer_paths.items():
        path = value[prefix + "_path"]
        digest = value[prefix + "_sha256"]
        if path is not None and not _json_exact(path, fixed_path):
            raise ValueError("terminal pointer: " + prefix)
        if digest is not None and (not _is_sha256(digest) or path is None):
            raise ValueError("terminal pointer hash: " + prefix)
        if (path is None) != (digest is None):
            raise ValueError("terminal pointer nullability: " + prefix)
    if value["child_diagnostic"] is not None:
        validate_child_diagnostic(value["child_diagnostic"])
    if value["state"] == "REGISTERED_AUDIT_TERMINAL_FAIL":
        if type(value["failure_code"]) is not str or not value["failure_code"]:
            raise ValueError("terminal failure disposition")
    else:
        if value["failure_code"] is not None or value["child_diagnostic"] is not None:
            raise ValueError("sealed terminal failure fields")
        if value["result_path"] != RAW_RESULT_RELATIVE.as_posix() or not _is_sha256(value["result_sha256"]):
            raise ValueError("sealed terminal result pointer")
        if value["result_manifest_path"] != RESULT_MANIFEST_RELATIVE.as_posix() or not _is_sha256(value["result_manifest_sha256"]):
            raise ValueError("sealed terminal manifest pointer")
        if value["execution_stage_path"] != EXECUTION_STAGE_RELATIVE.as_posix() or not _is_sha256(value["execution_stage_sha256"]):
            raise ValueError("sealed terminal stage pointer")
        if value["q_stage_path"] != Q_STAGE_RELATIVE.as_posix() or not _is_sha256(value["q_stage_sha256"]):
            raise ValueError("sealed terminal Q-stage pointer")
        if value["r_stage_path"] != R_STAGE_RELATIVE.as_posix() or not _is_sha256(value["r_stage_sha256"]):
            raise ValueError("sealed terminal R-stage pointer")


def _decode_embedded_record(payload, prefix):
    text = payload[prefix + "_canonical_json"]
    digest = payload[prefix + "_sha256"]
    if type(text) is not str or not _is_sha256(digest):
        raise TypeError("registered embedded record type: " + prefix)
    try:
        record_bytes = text.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("registered embedded record ASCII: " + prefix) from exc
    if sha256_bytes(record_bytes) != digest:
        raise ValueError("registered embedded record hash: " + prefix)
    return strict_canonical_load(record_bytes)


def _validate_registered_capability(value, track, claim, envelope):
    required = {
        "candidate_id",
        "claim_sha256",
        "definitions_sha256",
        "engine_sha256",
        "fixture_sha256",
        "nonce",
        "purpose",
        "runner_sha256",
        "schema",
        "track",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError(track + " registered capability shape")
    binding = claim["track_bindings"][track]
    expected = {
        "candidate_id": CANDIDATE_ID,
        "claim_sha256": envelope["claim_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "engine_sha256": binding["engine_sha256"],
        "fixture_sha256": binding["fixture_sha256"],
        "purpose": "REGISTERED_R100",
        "runner_sha256": binding["runner_sha256"],
        "schema": "P13_TRACK_CAPABILITY_V1",
        "track": track,
    }
    if any(not _json_exact(value[key], expected_value) for key, expected_value in expected.items()):
        raise ValueError(track + " registered capability binding")
    expected_nonce = _registered_capability_nonce(
        track,
        value["claim_sha256"],
        value["runner_sha256"],
        value["engine_sha256"],
        value["fixture_sha256"],
        value["definitions_sha256"],
    )
    if not _json_exact(value["nonce"], expected_nonce):
        raise ValueError(track + " registered capability nonce")


def _validate_registered_envelope(value, track, claim, capability_bytes):
    required = {
        "access_counters",
        "access_log_canonical_json",
        "access_log_sha256",
        "candidate_id",
        "capability_sha256",
        "certificate_canonical_json",
        "certificate_sha256",
        "claim_sha256",
        "definitions_sha256",
        "engine_sha256",
        "fixture_sha256",
        "runner_sha256",
        "schema",
        "track",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError(track + " registered envelope shape")
    binding = claim["track_bindings"][track]
    expected = {
        "access_counters": REGISTERED_ACCESS_COUNTERS,
        "candidate_id": CANDIDATE_ID,
        "capability_sha256": sha256_bytes(capability_bytes),
        "claim_sha256": sha256_bytes(canonical_bytes(claim)),
        "definitions_sha256": claim["definitions_sha256"],
        "engine_sha256": binding["engine_sha256"],
        "fixture_sha256": binding["fixture_sha256"],
        "runner_sha256": binding["runner_sha256"],
        "schema": "P13_BOUNDED_EXACT_TRACK_ENVELOPE_V1",
        "track": track,
    }
    if any(not _json_exact(value[key], expected_value) for key, expected_value in expected.items()):
        raise ValueError(track + " registered envelope binding")
    access_bytes = value["access_log_canonical_json"].encode("ascii")
    if sha256_bytes(access_bytes) != value["access_log_sha256"]:
        raise ValueError(track + " access-log hash")
    access = strict_canonical_load(access_bytes)
    track_name = "track_q" if track == "Q" else "track_r"
    if not _json_exact(access, {
        "allowed_read_counts": {
            "code/candidate_v1/shared/definitions.json": 1,
            "code/candidate_v1/" + track_name + "/engine.py": 1,
            "code/candidate_v1/" + track_name + "/private_fixture.json": 1,
            "code/candidate_v1/" + track_name + "/runner.py": 0,
        },
        "purpose": "REGISTERED_R100",
        "schema": "P13_TRACK_ACCESS_LOG_V1",
        "track": track,
    }):
        raise ValueError(track + " access-log contract")
    certificate_bytes = value["certificate_canonical_json"].encode("ascii")
    if sha256_bytes(certificate_bytes) != value["certificate_sha256"]:
        raise ValueError(track + " certificate hash")
    certificate = strict_canonical_load(certificate_bytes)
    if track == "Q":
        from candidate_v1.track_q.runner import _validate_certificate

        _validate_certificate(certificate)
    else:
        from candidate_v1.track_r.runner import _rj_validate_certificate

        _rj_validate_certificate(certificate)
    return certificate


def _validate_registered_payload(payload, claim_receipt):
    required = {
        "adjudication_canonical_json",
        "adjudication_sha256",
        "anti_claims",
        "acceptance_ledger_canonical_json",
        "acceptance_ledger_sha256",
        "candidate_id",
        "claim_sha256",
        "code_manifest_sha256",
        "code_tree_sha256",
        "contract_presence_canonical_json",
        "contract_presence_sha256",
        "definitions_canonical_json",
        "definitions_sha256",
        "deployment_review_sha256",
        "q_capability_canonical_json",
        "q_capability_sha256",
        "q_envelope_canonical_json",
        "q_envelope_sha256",
        "r_capability_canonical_json",
        "r_capability_sha256",
        "r_envelope_canonical_json",
        "r_envelope_sha256",
        "registered_counters_canonical_json",
        "registered_counters_sha256",
        "run_id",
        "same_family_review_limitation",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
    }
    if type(payload) is not dict or set(payload) != required:
        raise ValueError("registered payload exact shape")
    fixed = {
        "acceptance_ledger_sha256": claim_receipt["claim"]["acceptance_ledger_sha256"],
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
    if any(not _json_exact(payload[key], expected) for key, expected in fixed.items()):
        raise ValueError("registered payload fixed field")
    decoded = {
        prefix: _decode_embedded_record(payload, prefix)
        for prefix in (
            "acceptance_ledger",
            "adjudication",
            "contract_presence",
            "definitions",
            "q_capability",
            "q_envelope",
            "r_capability",
            "r_envelope",
            "registered_counters",
        )
    }
    if not _json_exact(decoded["registered_counters"], REGISTERED_COUNTER_VALUES):
        raise ValueError("registered exact counter ledger")
    if not _json_exact(decoded["acceptance_ledger"].get("required_counter_values"), REGISTERED_COUNTER_VALUES):
        raise ValueError("embedded acceptance-ledger counters")
    q_capability_bytes = payload["q_capability_canonical_json"].encode("ascii")
    r_capability_bytes = payload["r_capability_canonical_json"].encode("ascii")
    q_certificate = _validate_registered_envelope(
        decoded["q_envelope"], "Q", claim_receipt["claim"], q_capability_bytes
    )
    r_certificate = _validate_registered_envelope(
        decoded["r_envelope"], "R", claim_receipt["claim"], r_capability_bytes
    )
    _validate_registered_capability(decoded["q_capability"], "Q", claim_receipt["claim"], decoded["q_envelope"])
    _validate_registered_capability(decoded["r_capability"], "R", claim_receipt["claim"], decoded["r_envelope"])
    if _json_exact(decoded["q_capability"]["nonce"], decoded["r_capability"]["nonce"]):
        raise ValueError("registered capability nonces must be track-distinct")
    from candidate_v1.adjudicator.adjudicate import adjudicate

    fresh_adjudication = adjudicate(
        q_certificate,
        r_certificate,
        decoded["acceptance_ledger"],
        decoded["registered_counters"],
        decoded["definitions"],
    )
    if not _json_exact(decoded["adjudication"], fresh_adjudication):
        raise ValueError("registered adjudication recomputation")
    if not _json_exact(decoded["contract_presence"], fresh_adjudication["contract_presence_records"]):
        raise ValueError("registered contract-presence cross-binding")
    forbidden = ("PROVED", "SOURCE" + "_LOCK_PASS")
    forbidden_authority_keys = {
        "machine_proof_authority",
        "machine_proof_claim",
        "machine_source_verdict",
        "proof_verdict",
        "source_verdict",
        "theorem_verdict",
    }
    pending = [payload, *decoded.values()]
    while pending:
        item = pending.pop()
        if type(item) is dict:
            for key in item:
                lowered = key.lower()
                if lowered in forbidden_authority_keys:
                    raise ValueError("registered payload proof-verdict field")
            pending.extend(item.keys())
            pending.extend(item.values())
        elif type(item) is list:
            pending.extend(item)
        elif type(item) is str and any(token in item for token in forbidden):
            raise ValueError("registered payload authority language")


def _seal_success(
    project_root,
    claim_receipt,
    payload,
    stage_receipt,
    final_preterminal_validator,
):
    live_claim_bytes = read_regular_bytes(project_root / CLAIM_RELATIVE)
    if (
        live_claim_bytes != claim_receipt["claim_bytes"]
        or sha256_bytes(live_claim_bytes) != claim_receipt["claim_sha256"]
    ):
        raise RuntimeError("durable claim drift before success seal")
    _validate_registered_payload(payload, claim_receipt)
    q_stage_bytes = read_regular_bytes(project_root / Q_STAGE_RELATIVE)
    r_stage_bytes = read_regular_bytes(project_root / R_STAGE_RELATIVE)
    if q_stage_bytes != payload["q_envelope_canonical_json"].encode("ascii"):
        raise RuntimeError("Q staged envelope/payload drift")
    if r_stage_bytes != payload["r_envelope_canonical_json"].encode("ascii"):
        raise RuntimeError("R staged envelope/payload drift")
    if sha256_bytes(q_stage_bytes) != payload["q_envelope_sha256"]:
        raise RuntimeError("Q staged envelope hash drift")
    if sha256_bytes(r_stage_bytes) != payload["r_envelope_sha256"]:
        raise RuntimeError("R staged envelope hash drift")
    if type(stage_receipt) is not dict or set(stage_receipt) != {
        "stage",
        "stage_bytes",
        "stage_sha256",
    }:
        raise ValueError("execution-stage receipt shape")
    expected_stage = _execution_stage_object(claim_receipt)
    expected_stage_bytes = canonical_bytes(expected_stage)
    if (
        not _json_exact(stage_receipt["stage"], expected_stage)
        or stage_receipt["stage_bytes"] != expected_stage_bytes
        or sha256_bytes(stage_receipt["stage_bytes"]) != stage_receipt["stage_sha256"]
    ):
        raise RuntimeError("execution-stage receipt drift")
    stage_bytes = read_regular_bytes(project_root / EXECUTION_STAGE_RELATIVE)
    if stage_bytes != stage_receipt["stage_bytes"]:
        raise RuntimeError("execution-stage contract drift before success seal")
    result_sha256 = write_json_exclusive(project_root / RAW_RESULT_RELATIVE, payload)
    stage_sha256 = stage_receipt["stage_sha256"]
    official = project_root / CLAIM_RELATIVE.parent
    before_manifest = {"durable_claim.json", "execution_started.json", "raw_result.json"}
    if {
        path.name for path in official.iterdir() if path.is_file() and not path.is_symlink()
    } != before_manifest or any(path.is_symlink() or not path.is_file() for path in official.iterdir()):
        raise RuntimeError("official pre-manifest inventory drift")
    embedded_prefixes = (
        "acceptance_ledger",
        "adjudication",
        "contract_presence",
        "definitions",
        "q_capability",
        "q_envelope",
        "r_capability",
        "r_envelope",
        "registered_counters",
    )
    entries = [
        {
            "kind": "PHYSICAL_FILE",
            "path": CLAIM_RELATIVE.as_posix(),
            "sha256": claim_receipt["claim_sha256"],
        },
        {
            "kind": "PHYSICAL_FILE",
            "path": EXECUTION_STAGE_RELATIVE.as_posix(),
            "sha256": stage_sha256,
        },
        {
            "kind": "PHYSICAL_FILE",
            "path": RAW_RESULT_RELATIVE.as_posix(),
            "sha256": result_sha256,
        },
        {
            "kind": "PHYSICAL_FILE",
            "path": Q_STAGE_RELATIVE.as_posix(),
            "sha256": sha256_bytes(q_stage_bytes),
        },
        {
            "kind": "PHYSICAL_FILE",
            "path": R_STAGE_RELATIVE.as_posix(),
            "sha256": sha256_bytes(r_stage_bytes),
        },
    ] + [
        {
            "kind": "EMBEDDED_CANONICAL_RECORD",
            "path": "embedded://raw_result/" + prefix,
            "sha256": payload[prefix + "_sha256"],
        }
        for prefix in embedded_prefixes
    ]
    entries = sorted(entries, key=lambda item: item["path"])
    result_manifest = {
        "candidate_id": CANDIDATE_ID,
        "claim_sha256": claim_receipt["claim_sha256"],
        "entries": entries,
        "entry_count": len(entries),
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_STRICT_RESULT_MANIFEST_V1",
        "status": "PRE_TERMINAL_CONTENT_SEALED",
    }
    _validate_result_manifest(project_root, result_manifest, payload, claim_receipt)
    result_manifest_sha256 = write_json_exclusive(
        project_root / RESULT_MANIFEST_RELATIVE, result_manifest
    )
    claim = claim_receipt["claim"]
    terminal = {
        "acceptance_ledger_sha256": claim["acceptance_ledger_sha256"],
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "child_diagnostic": None,
        "claim_sha256": claim_receipt["claim_sha256"],
        "code_manifest_sha256": claim["code_manifest_sha256"],
        "code_tree_sha256": claim["code_tree_sha256"],
        "definitions_sha256": claim["definitions_sha256"],
        "deployment_review_sha256": claim["deployment_review_sha256"],
        "execution_stage_path": EXECUTION_STAGE_RELATIVE.as_posix(),
        "execution_stage_sha256": stage_sha256,
        "failure_code": None,
        "registered_audit_count": 1,
        "q_stage_path": Q_STAGE_RELATIVE.as_posix(),
        "q_stage_sha256": sha256_bytes(q_stage_bytes),
        "r_stage_path": R_STAGE_RELATIVE.as_posix(),
        "r_stage_sha256": sha256_bytes(r_stage_bytes),
        "result_path": RAW_RESULT_RELATIVE.as_posix(),
        "result_manifest_path": RESULT_MANIFEST_RELATIVE.as_posix(),
        "result_manifest_sha256": result_manifest_sha256,
        "result_sha256": result_sha256,
        "rerun_permitted": False,
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_ONE_SHOT_TERMINAL_V1",
        "source_lock_sha256": claim["source_lock_sha256"],
        "source_review_sha256": claim["source_review_sha256"],
        "state": "REGISTERED_AUDIT_SEALED",
    }
    _validate_terminal_object(terminal)
    _validate_preterminal_runtime_tree(
        project_root, terminal, payload, claim_receipt, stage_receipt
    )
    final_inbound_receipt = final_preterminal_validator()
    claim = claim_receipt["claim"]
    expected_final_inbound_receipt = {
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
    if not _json_exact(final_inbound_receipt, expected_final_inbound_receipt):
        raise ValueError("final preterminal inbound validation receipt drift")
    _commit_terminal_once(project_root, terminal)
    return payload


def _validate_result_manifest(project_root, value, payload, claim_receipt):
    required = {
        "candidate_id",
        "claim_sha256",
        "entries",
        "entry_count",
        "run_id",
        "schema",
        "status",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError("result manifest exact shape")
    if not _json_exact(
        {key: value[key] for key in required - {"entries", "entry_count"}},
        {
            "candidate_id": CANDIDATE_ID,
            "claim_sha256": claim_receipt["claim_sha256"],
            "run_id": REGISTERED_RUN_ID,
            "schema": "P13_STRICT_RESULT_MANIFEST_V1",
            "status": "PRE_TERMINAL_CONTENT_SEALED",
        },
    ):
        raise ValueError("result manifest fixed fields")
    entries = value["entries"]
    if (
        type(entries) is not list
        or len(entries) != 14
        or type(value["entry_count"]) is not int
        or value["entry_count"] != 14
    ):
        raise ValueError("result manifest entry count")
    if entries != sorted(entries, key=lambda item: item.get("path", "")):
        raise ValueError("result manifest ordering")
    if len({item.get("path") for item in entries if type(item) is dict}) != len(entries):
        raise ValueError("result manifest duplicate path")
    observed = {}
    for entry in entries:
        if type(entry) is not dict or set(entry) != {"kind", "path", "sha256"}:
            raise ValueError("result manifest entry shape")
        if entry["kind"] not in {"PHYSICAL_FILE", "EMBEDDED_CANONICAL_RECORD"} or type(entry["path"]) is not str or not _is_sha256(entry["sha256"]):
            raise ValueError("result manifest entry leaf")
        observed[entry["path"]] = [entry["kind"], entry["sha256"]]
    expected = {
        CLAIM_RELATIVE.as_posix(): ["PHYSICAL_FILE", claim_receipt["claim_sha256"]],
        EXECUTION_STAGE_RELATIVE.as_posix(): [
            "PHYSICAL_FILE",
            sha256_bytes(read_regular_bytes(project_root / EXECUTION_STAGE_RELATIVE)),
        ],
        RAW_RESULT_RELATIVE.as_posix(): [
            "PHYSICAL_FILE",
            sha256_bytes(read_regular_bytes(project_root / RAW_RESULT_RELATIVE)),
        ],
        Q_STAGE_RELATIVE.as_posix(): [
            "PHYSICAL_FILE",
            sha256_bytes(read_regular_bytes(project_root / Q_STAGE_RELATIVE)),
        ],
        R_STAGE_RELATIVE.as_posix(): [
            "PHYSICAL_FILE",
            sha256_bytes(read_regular_bytes(project_root / R_STAGE_RELATIVE)),
        ],
    }
    for prefix in (
        "acceptance_ledger",
        "adjudication",
        "contract_presence",
        "definitions",
        "q_capability",
        "q_envelope",
        "r_capability",
        "r_envelope",
        "registered_counters",
    ):
        expected["embedded://raw_result/" + prefix] = [
            "EMBEDDED_CANONICAL_RECORD",
            payload[prefix + "_sha256"],
        ]
    if not _json_exact(observed, expected):
        raise ValueError("result manifest closure drift")


def _validate_preterminal_runtime_tree(
    project_root, terminal, payload, claim_receipt, stage_receipt
):
    runtime_root = project_root / RUNTIME_RELATIVE
    expected_files = {
        CLAIM_RELATIVE.as_posix(),
        EXECUTION_STAGE_RELATIVE.as_posix(),
        Q_STAGE_RELATIVE.as_posix(),
        R_STAGE_RELATIVE.as_posix(),
        RAW_RESULT_RELATIVE.as_posix(),
        RESULT_MANIFEST_RELATIVE.as_posix(),
    }
    observed_files = set()
    observed_directories = set()
    for path in runtime_root.rglob("*"):
        if path.is_symlink():
            raise RuntimeError("sealed runtime symlink")
        if path.is_file():
            observed_files.add(path.relative_to(project_root).as_posix())
        elif path.is_dir():
            observed_directories.add(path.relative_to(project_root).as_posix())
        else:
            raise RuntimeError("sealed runtime nonregular entry")
    if observed_files != expected_files:
        raise RuntimeError("preterminal runtime exact-six-file inventory drift")
    expected_directories = {
        OFFICIAL_RELATIVE.as_posix(),
        (RUNTIME_RELATIVE / "staging").as_posix(),
        (RUNTIME_RELATIVE / "staging/track_q").as_posix(),
        (RUNTIME_RELATIVE / "staging/track_r").as_posix(),
    }
    if observed_directories != expected_directories:
        raise RuntimeError("sealed runtime exact-directory inventory drift")
    if read_regular_bytes(project_root / CLAIM_RELATIVE) != claim_receipt["claim_bytes"]:
        raise RuntimeError("preterminal runtime claim drift")
    if read_regular_bytes(project_root / EXECUTION_STAGE_RELATIVE) != stage_receipt["stage_bytes"]:
        raise RuntimeError("preterminal execution-stage drift")
    raw_bytes = read_regular_bytes(project_root / RAW_RESULT_RELATIVE)
    if not _json_exact(strict_canonical_load(raw_bytes), payload) or sha256_bytes(raw_bytes) != terminal["result_sha256"]:
        raise RuntimeError("sealed runtime raw-result drift")
    q_bytes = read_regular_bytes(project_root / Q_STAGE_RELATIVE)
    r_bytes = read_regular_bytes(project_root / R_STAGE_RELATIVE)
    if (
        q_bytes != payload["q_envelope_canonical_json"].encode("ascii")
        or sha256_bytes(q_bytes) != terminal["q_stage_sha256"]
        or r_bytes != payload["r_envelope_canonical_json"].encode("ascii")
        or sha256_bytes(r_bytes) != terminal["r_stage_sha256"]
    ):
        raise RuntimeError("sealed runtime track-stage drift")
    manifest_bytes = read_regular_bytes(project_root / RESULT_MANIFEST_RELATIVE)
    manifest = strict_canonical_load(manifest_bytes)
    if sha256_bytes(manifest_bytes) != terminal["result_manifest_sha256"]:
        raise RuntimeError("sealed runtime manifest hash drift")
    _validate_result_manifest(project_root, manifest, payload, claim_receipt)


def _execution_stage_object(claim_receipt):
    return {
        "attempt": 1,
        "candidate_id": CANDIDATE_ID,
        "candidate_version": CANDIDATE_VERSION,
        "claim_path": CLAIM_RELATIVE.as_posix(),
        "claim_sha256": claim_receipt["claim_sha256"],
        "rerun_budget": 0,
        "run_id": REGISTERED_RUN_ID,
        "schema": "P13_EXECUTION_STAGE_V1",
        "state": "OPERATION_ENTERED",
    }


def run_after_claim(
    project_root: Path,
    claim_receipt: dict,
    operation,
    final_preterminal_validator=None,
):
    """Run exactly once; every post-claim exception receives a durable terminal."""
    if type(claim_receipt) is not dict or set(claim_receipt) != {
        "claim",
        "claim_bytes",
        "claim_sha256",
        "official",
    }:
        raise ValueError("claim receipt shape")
    if (
        claim_receipt["claim_bytes"] != canonical_bytes(claim_receipt["claim"])
        or sha256_bytes(claim_receipt["claim_bytes"]) != claim_receipt["claim_sha256"]
    ):
        raise ValueError("claim receipt integrity")
    terminal_path = project_root / TERMINAL_RELATIVE
    if terminal_path.exists() or terminal_path.is_symlink():
        raise RuntimeError("one-shot terminal already exists")
    try:
        if not callable(final_preterminal_validator):
            raise TypeError("final preterminal inbound validator callable required")
        live_payload = read_regular_bytes(project_root / CLAIM_RELATIVE)
        if live_payload != claim_receipt["claim_bytes"]:
            raise RuntimeError("durable claim drift after start")
        stage = _execution_stage_object(claim_receipt)
        stage_sha256 = write_json_exclusive(project_root / EXECUTION_STAGE_RELATIVE, stage)
        stage_bytes = canonical_bytes(stage)
        stage_receipt = {
            "stage": stage,
            "stage_bytes": stage_bytes,
            "stage_sha256": stage_sha256,
        }
        payload = operation()
        return _seal_success(
            project_root,
            claim_receipt,
            payload,
            stage_receipt,
            final_preterminal_validator,
        )
    except BaseException as exc:
        if isinstance(exc, CommittedTerminalDurabilityError):
            raise
        diagnostic_lookup_failed = False
        try:
            diagnostic = getattr(exc, "child_diagnostic", None)
        except BaseException:
            diagnostic = None
            diagnostic_lookup_failed = True
        failure_code = "POST_CLAIM_" + type(exc).__name__.upper()
        if diagnostic_lookup_failed:
            failure_code += "_INVALID_CHILD_DIAGNOSTIC"
        if diagnostic is not None:
            try:
                validate_child_diagnostic(diagnostic)
            except BaseException:
                diagnostic = None
                failure_code += "_INVALID_CHILD_DIAGNOSTIC"
        terminal_error = None
        try:
            terminalize_failure(
                project_root,
                claim_receipt,
                failure_code,
                diagnostic,
            )
        except BaseException as caught_terminal_error:
            terminal_error = caught_terminal_error
            try:
                exc.add_note("terminalization error: " + repr(terminal_error))
            except BaseException:
                pass
        if isinstance(terminal_error, CommittedTerminalDurabilityError):
            raise terminal_error from exc
        raise
