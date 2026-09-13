"""Capability-gated Track-Q process entry point."""

import hashlib
import json
import os
from pathlib import Path


def _q_unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Q duplicate JSON key")
        result[key] = value
    return result


def _q_reject_constant(value):
    raise ValueError("Q non-finite JSON value: " + value)


def _q_reject_float(value):
    raise ValueError("Q floating JSON value: " + value)


def _q_strict_load(data):
    return json.loads(
        data.decode("utf-8"),
        object_pairs_hook=_q_unique_object,
        parse_constant=_q_reject_constant,
        parse_float=_q_reject_float,
    )


def _q_exact_json(value):
    if value is None or type(value) in (bool, int, str):
        return value
    if type(value) is list:
        return [_q_exact_json(item) for item in value]
    if type(value) is tuple:
        return [_q_exact_json(item) for item in value]
    if type(value) is dict:
        result = {}
        for key, item in value.items():
            if type(key) is not str or key in result:
                raise TypeError("Q canonical JSON key")
            result[key] = _q_exact_json(item)
        return result
    raise TypeError("Q non-exact evidence type: " + type(value).__name__)


def _q_canonical(value):
    return json.dumps(
        _q_exact_json(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def _q_absolute(path):
    return Path(os.path.abspath(os.fspath(path)))


def _q_reject_symlink_components(path):
    absolute = _q_absolute(path)
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        if current.exists() and current.is_symlink():
            raise RuntimeError("Q symlink path component")


def _q_read_regular(path):
    _q_reject_symlink_components(path)
    before = path.lstat()
    if not path.is_file() or path.is_symlink():
        raise RuntimeError("Q read target is not a regular non-symlink file")
    descriptor = os.open(os.fspath(path), os.O_RDONLY | os.O_NOFOLLOW)
    try:
        chunks = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        opened = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    after = path.lstat()
    identity_before = (
        before.st_dev, before.st_ino, before.st_mode, before.st_size,
        before.st_mtime_ns, before.st_ctime_ns,
    )
    identity_opened = (
        opened.st_dev, opened.st_ino, opened.st_mode, opened.st_size,
        opened.st_mtime_ns, opened.st_ctime_ns,
    )
    identity_after = (
        after.st_dev, after.st_ino, after.st_mode, after.st_size,
        after.st_mtime_ns, after.st_ctime_ns,
    )
    if identity_before != identity_opened or identity_opened != identity_after:
        raise RuntimeError("Q unstable file read")
    data = b"".join(chunks)
    if len(data) != before.st_size:
        raise RuntimeError("Q short file read")
    return data


def _q_write_exclusive(path, data):
    _q_reject_symlink_components(path.parent)
    descriptor = os.open(
        os.fspath(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600
    )
    try:
        offset = 0
        while offset < len(data):
            written = os.write(descriptor, data[offset:])
            if written < 1:
                raise OSError("Q short write")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    directory = os.open(os.fspath(path.parent), os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def _q_digest_token(value):
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _q_parse_capability(token):
    try:
        text = token.decode("ascii")
    except UnicodeDecodeError as exc:
        raise RuntimeError("Q capability is not ASCII") from exc
    parts = text.rstrip("\n").split(":")
    if (not text.endswith("\n") or len(parts) != 5
            or parts[0] != "HENON_PERIOD3_TRACK_Q_START_V1"
            or any(not _q_digest_token(value) for value in parts[1:])):
        raise RuntimeError("Q launch capability invalid")
    return {
        "claim_sha256": parts[1],
        "runner_sha256": parts[2],
        "engine_sha256": parts[3],
        "definitions_sha256": parts[4],
    }


def _q_path_label(project_root, path):
    absolute = _q_absolute(path)
    try:
        return absolute.relative_to(project_root).as_posix()
    except ValueError:
        return absolute.as_posix()


def _q_increment(table, key):
    table[key] = table.get(key, 0) + 1


def _q_install_audit_guard(project_root, allowed_reads, allowed_writes, allowed_directories):
    absolute_reads = {_q_absolute(path): _q_path_label(project_root, path) for path in allowed_reads}
    absolute_writes = {_q_absolute(path): _q_path_label(project_root, path) for path in allowed_writes}
    absolute_directories = {
        _q_absolute(path): _q_path_label(project_root, path) for path in allowed_directories
    }
    state = {
        "read_counts": {},
        "write_counts": {},
        "directory_counts": {},
        "import_counts": {},
        "read_outside_allowlist_count": 0,
        "write_outside_allowlist_count": 0,
        "network_access_count": 0,
        "process_access_count": 0,
        "dynamic_loader_access_count": 0,
    }
    write_mask = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
    forbidden_os_events = {
        "os.chdir", "os.chmod", "os.chown", "os.exec", "os.fork", "os.kill",
        "os.link", "os.mkdir", "os.posix_spawn", "os.remove", "os.rename",
        "os.rmdir", "os.spawn", "os.symlink", "os.system", "os.truncate",
    }

    def audit(event, arguments):
        if event == "open":
            raw_path = arguments[0]
            if not isinstance(raw_path, (str, bytes, os.PathLike)):
                state["read_outside_allowlist_count"] += 1
                raise PermissionError("Q non-path open forbidden")
            absolute = _q_absolute(raw_path)
            flags = arguments[2] if len(arguments) > 2 and type(arguments[2]) is int else 0
            if flags & os.O_DIRECTORY:
                if absolute not in absolute_directories:
                    state["read_outside_allowlist_count"] += 1
                    raise PermissionError("Q directory open outside allowlist")
                _q_increment(state["directory_counts"], absolute_directories[absolute])
            elif flags & write_mask:
                if absolute not in absolute_writes:
                    state["write_outside_allowlist_count"] += 1
                    raise PermissionError("Q write outside allowlist")
                _q_increment(state["write_counts"], absolute_writes[absolute])
            else:
                if absolute not in absolute_reads:
                    state["read_outside_allowlist_count"] += 1
                    raise PermissionError("Q read outside allowlist")
                _q_increment(state["read_counts"], absolute_reads[absolute])
            return
        if event in {"os.listdir", "os.scandir"}:
            absolute = _q_absolute(arguments[0])
            if absolute not in absolute_directories:
                state["read_outside_allowlist_count"] += 1
                raise PermissionError("Q directory scan outside allowlist")
            _q_increment(state["directory_counts"], absolute_directories[absolute])
            return
        if event == "import":
            module_name = arguments[0]
            if module_name != "engine":
                state["dynamic_loader_access_count"] += 1
                raise PermissionError("Q unexpected post-capability import")
            _q_increment(state["import_counts"], module_name)
            return
        if event in forbidden_os_events or event.startswith(("subprocess.", "pty.")):
            state["process_access_count"] += 1
            raise PermissionError("Q process capability forbidden")
        if event.startswith(("socket.", "urllib.", "http.client")):
            state["network_access_count"] += 1
            raise PermissionError("Q network capability forbidden")
        if event.startswith(("ctypes.", "importlib.")):
            state["dynamic_loader_access_count"] += 1
            raise PermissionError("Q dynamic loader capability forbidden")

    os.sys.addaudithook(audit)
    return state


def _q_count_records(table):
    return [{"count": table[path], "path": path} for path in sorted(table)]


def _q_write_access_log(path, project_root, state, token_fields, allowed_reads, allowed_writes):
    descriptor = os.open(
        os.fspath(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600
    )
    try:
        record = {
            "schema": "HENON_PERIOD3_TRACK_Q_PROVENANCE_ACCESS_LOG_V1",
            "claim_sha256": token_fields["claim_sha256"],
            "allowlisted_reads": sorted(_q_path_label(project_root, item) for item in allowed_reads),
            "allowlisted_writes": sorted(_q_path_label(project_root, item) for item in allowed_writes),
            "observed_reads": _q_count_records(state["read_counts"]),
            "observed_writes": _q_count_records(state["write_counts"]),
            "observed_directories": _q_count_records(state["directory_counts"]),
            "observed_imports": _q_count_records(state["import_counts"]),
            "read_outside_allowlist_count": state["read_outside_allowlist_count"],
            "write_outside_allowlist_count": state["write_outside_allowlist_count"],
            "network_access_count": state["network_access_count"],
            "process_access_count": state["process_access_count"],
            "dynamic_loader_access_count": state["dynamic_loader_access_count"],
            "source_document_access_count": 0,
            "acceptance_ledger_access_count": 0,
            "historical_result_access_count": 0,
            "cross_track_scientific_read_count": 0,
        }
        data = _q_canonical(record)
        offset = 0
        while offset < len(data):
            written = os.write(descriptor, data[offset:])
            if written < 1:
                raise OSError("Q short access-log write")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    directory = os.open(os.fspath(path.parent), os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def _q_validate_definitions(value):
    required = {
        "allowed_task_ids",
        "candidate_id",
        "category",
        "cyclic_orientation",
        "exact_serialization",
        "family",
        "formal_period_convention",
        "nonclaim_tags",
        "output_field_names",
        "registered_coefficient_indices",
        "schema",
        "symbol_names",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError("Q definitions keys")
    if value["schema"] != "HENON_PERIOD3_DEFINITIONS_ONLY_V1":
        raise ValueError("Q definitions schema")
    if value["candidate_id"] != "henon_period3_residue_v1":
        raise ValueError("Q candidate")
    if value["registered_coefficient_indices"] != [8, 9] or any(
        type(item) is not int for item in value["registered_coefficient_indices"]
    ):
        raise ValueError("Q registered tuple")
    if value["category"].get("characteristic") != 0 or type(
        value["category"].get("characteristic")
    ) is not int:
        raise ValueError("Q characteristic")


def _q_validate_claim(value):
    required = {
        "candidate_id",
        "code_manifest_sha256",
        "code_tree_sha256",
        "definitions_sha256",
        "deployment_review_sha256",
        "preflight_sha256",
        "proof_sha256",
        "registered_audit_count",
        "registered_candidate_id_count",
        "registered_coefficient_indices",
        "rerun_budget_after_start",
        "result_path",
        "run_id",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
        "state",
        "terminal_failure_rule",
        "terminal_path",
    }
    if type(value) is not dict or set(value) != required:
        raise ValueError("Q durable claim keys")
    if (value["schema"] != "HENON_PERIOD3_DURABLE_REGISTERED_CLAIM_V1"
            or value["candidate_id"] != "henon_period3_residue_v1"
            or value["run_id"] != "R100"
            or value["state"] != "STARTED"):
        raise ValueError("Q durable claim identity")
    if value["registered_coefficient_indices"] != [8, 9] or any(
        type(item) is not int for item in value["registered_coefficient_indices"]
    ):
        raise ValueError("Q durable claim tuple")
    if (type(value["registered_audit_count"]) is not int
            or value["registered_audit_count"] != 1
            or type(value["registered_candidate_id_count"]) is not int
            or value["registered_candidate_id_count"] != 1
            or type(value["rerun_budget_after_start"]) is not int
            or value["rerun_budget_after_start"] != 0):
        raise ValueError("Q durable claim counters")
    for key in (
        "code_manifest_sha256",
        "code_tree_sha256",
        "definitions_sha256",
        "deployment_review_sha256",
        "preflight_sha256",
        "proof_sha256",
        "source_lock_sha256",
        "source_review_sha256",
    ):
        if not _q_digest_token(value[key]):
            raise ValueError("Q durable claim digest")


def _q_capability():
    try:
        token = os.read(3, 400)
    except OSError as exc:
        raise RuntimeError("Q launch capability missing") from exc
    finally:
        try:
            os.close(3)
        except OSError:
            pass
    return _q_parse_capability(token)


def main():
    if len(os.sys.argv) != 1:
        raise RuntimeError("Q runner accepts no arguments")
    token_fields = _q_capability()
    runner_path = Path(__file__).absolute()
    project_root = runner_path.parents[3]
    definitions_path = project_root / "code/candidate_v1/shared/definitions.json"
    claim_path = project_root / "runtime/candidate_v1/official/durable_claim.json"
    engine_path = runner_path.parent / "engine.py"
    stage = project_root / "runtime/candidate_v1/staging/track_q"
    witness_path = stage / "private_witness.json"
    envelope_path = stage / "sealed_envelope.json"
    access_path = stage / "access_log.json"
    allowed_reads = {claim_path, definitions_path, engine_path, runner_path}
    allowed_writes = {witness_path, envelope_path, access_path}
    audit_state = _q_install_audit_guard(
        project_root,
        allowed_reads,
        allowed_writes,
        {stage, runner_path.parent},
    )
    if not stage.is_dir() or stage.is_symlink() or list(stage.iterdir()):
        raise RuntimeError("Q staging directory is not fresh")
    claim_bytes = _q_read_regular(claim_path)
    claim = _q_strict_load(claim_bytes)
    if claim_bytes != _q_canonical(claim):
        raise ValueError("Q durable claim is not canonical")
    _q_validate_claim(claim)
    if hashlib.sha256(claim_bytes).hexdigest() != token_fields["claim_sha256"]:
        raise RuntimeError("Q capability claim digest mismatch")
    runner_bytes = _q_read_regular(runner_path)
    if hashlib.sha256(runner_bytes).hexdigest() != token_fields["runner_sha256"]:
        raise RuntimeError("Q runner digest mismatch")
    engine_bytes = _q_read_regular(engine_path)
    if hashlib.sha256(engine_bytes).hexdigest() != token_fields["engine_sha256"]:
        raise RuntimeError("Q engine digest mismatch")
    definition_bytes = _q_read_regular(definitions_path)
    if hashlib.sha256(definition_bytes).hexdigest() != token_fields["definitions_sha256"]:
        raise RuntimeError("Q definitions digest mismatch")
    if claim["definitions_sha256"] != token_fields["definitions_sha256"]:
        raise RuntimeError("Q claim definitions digest mismatch")
    definitions = _q_strict_load(definition_bytes)
    _q_validate_definitions(definitions)
    os.sys.path.insert(0, os.fspath(runner_path.parent))
    from engine import run_science

    science = run_science(definitions)
    witness_bytes = _q_canonical(science["private_witness"])
    _q_write_exclusive(witness_path, witness_bytes)
    witness_sha256 = hashlib.sha256(witness_bytes).hexdigest()
    envelope = {
        "schema": "HENON_PERIOD3_TRACK_OUTPUT_V1",
        "candidate_id": "henon_period3_residue_v1",
        "track": "Q",
        "definitions_sha256": hashlib.sha256(definition_bytes).hexdigest(),
        "private_witness_sha256": witness_sha256,
        "quartic": science["public_quartic"],
        "coefficient_diagnostics": science["public_coefficient_diagnostics"],
    }
    envelope_bytes = _q_canonical(envelope)
    _q_write_exclusive(envelope_path, envelope_bytes)
    _q_write_access_log(
        access_path,
        project_root,
        audit_state,
        token_fields,
        allowed_reads,
        allowed_writes,
    )


if __name__ == "__main__":
    main()
