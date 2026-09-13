"""Hash-bound, science-free, append-only result-manifest analyzer."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


SOURCE_LOCK_SHA256 = "2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2"
SOURCE_REVIEW_SHA256 = "5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11"
PROOF_SHA256 = "36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9"


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("postrun duplicate JSON key")
        result[key] = value
    return result


def _reject(value):
    raise ValueError("postrun non-exact JSON number: " + value)


def _loads(data):
    return json.loads(
        data.decode("utf-8"),
        object_pairs_hook=_unique,
        parse_constant=_reject,
        parse_float=_reject,
    )


def _exact(value):
    if value is None or type(value) in (bool, int, str):
        return value
    if type(value) is list:
        return [_exact(item) for item in value]
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise TypeError("postrun non-string key")
        return {key: _exact(item) for key, item in value.items()}
    raise TypeError("postrun non-exact value")


def _canonical(value):
    return json.dumps(
        _exact(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def _read(path):
    before = path.lstat()
    if not path.is_file() or path.is_symlink():
        raise RuntimeError("postrun unsafe artifact")
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
    identity = lambda item: (
        item.st_dev,
        item.st_ino,
        item.st_mode,
        item.st_size,
        item.st_mtime_ns,
        item.st_ctime_ns,
    )
    if identity(before) != identity(opened) or identity(opened) != identity(after):
        raise RuntimeError("postrun unstable artifact")
    data = b"".join(chunks)
    if len(data) != before.st_size:
        raise RuntimeError("postrun short read")
    return data


def _canonical_artifact(path):
    data = _read(path)
    value = _loads(data)
    if data != _canonical(value):
        raise ValueError("postrun artifact is not canonical")
    return value, data, hashlib.sha256(data).hexdigest()


def _write_exclusive(path, data):
    descriptor = os.open(
        os.fspath(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600
    )
    try:
        offset = 0
        while offset < len(data):
            written = os.write(descriptor, data[offset:])
            if written < 1:
                raise OSError("postrun short write")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    directory = os.open(os.fspath(path.parent), os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def build_result_manifest(project_root):
    paths = {
        "durable_claim": project_root / "runtime/candidate_v1/official/durable_claim.json",
        "raw_result": project_root / "runtime/candidate_v1/official/raw_result.json",
        "terminal": project_root / "runtime/candidate_v1/official/terminal.json",
        "code_manifest": project_root / "preexecution/code_manifest.json",
        "deployment_review": project_root / "preexecution/INDEPENDENT_DEPLOYMENT_REVIEW.json",
        "result_review": project_root / "runtime/candidate_v1/review/INDEPENDENT_RESULT_REVIEW.json",
    }
    loaded = {}
    digests = {}
    for name, path in paths.items():
        value, _, digest = _canonical_artifact(path)
        loaded[name] = value
        digests[name] = digest
    claim = loaded["durable_claim"]
    result = loaded["raw_result"]
    terminal = loaded["terminal"]
    code_manifest = loaded["code_manifest"]
    review = loaded["result_review"]
    result_keys = {
        "audit",
        "candidate_id",
        "code_manifest_sha256",
        "code_tree_sha256",
        "contract_witnesses",
        "counters",
        "deployment_review_sha256",
        "durable_claim_sha256",
        "implementation_audit_status",
        "negative_controls",
        "nonclaims",
        "proof_sha256",
        "registered_coefficient_indices",
        "run_id",
        "schema",
        "source_lock_sha256",
        "source_review_sha256",
        "source_stage_diagnostic_disclosure",
        "track_artifacts",
        "track_certificates",
    }
    if type(result) is not dict or set(result) != result_keys:
        raise ValueError("postrun raw-result keys")
    if (result["schema"] != "HENON_PERIOD3_REGISTERED_EXACT_AUDIT_V1"
            or result["candidate_id"] != "henon_period3_residue_v1"
            or result["run_id"] != "R100"
            or result["registered_coefficient_indices"] != [8, 9]
            or type(result["counters"]) is not dict
            or type(result["counters"].get("registered_audit_count")) is not int
            or result["counters"]["registered_audit_count"] != 1):
        raise ValueError("postrun raw-result identity")
    if (type(claim) is not dict or claim.get("state") != "STARTED"
            or claim.get("run_id") != "R100"):
        raise ValueError("postrun durable-claim identity")
    if (type(terminal) is not dict
            or terminal.get("state") != "REGISTERED_AUDIT_COMPLETED_EXACT_AGREEMENT"
            or terminal.get("result_sha256") != digests["raw_result"]
            or terminal.get("claim_sha256") != digests["durable_claim"]
            or terminal.get("rerun_permitted") is not False):
        raise ValueError("postrun terminal binding")
    if (result["durable_claim_sha256"] != digests["durable_claim"]
            or result["code_manifest_sha256"] != digests["code_manifest"]
            or result["deployment_review_sha256"] != digests["deployment_review"]
            or result["source_lock_sha256"] != SOURCE_LOCK_SHA256
            or result["source_review_sha256"] != SOURCE_REVIEW_SHA256
            or result["proof_sha256"] != PROOF_SHA256):
        raise ValueError("postrun raw-result hash binding")
    analyzer_path = Path(__file__).absolute()
    analyzer_sha256 = hashlib.sha256(_read(analyzer_path)).hexdigest()
    if (type(code_manifest) is not dict
            or code_manifest.get("code_tree_sha256") != result["code_tree_sha256"]
            or type(code_manifest.get("code_files")) is not dict
            or code_manifest["code_files"].get("postrun_analyzer/analyze.py")
            != analyzer_sha256):
        raise ValueError("postrun analyzer is not bound by code manifest")
    review_keys = {
        "advisories",
        "blocking_findings",
        "candidate_id",
        "registered_execution_count_observed",
        "required_checks",
        "reviewed_artifacts",
        "reviewer_authored_candidate_code",
        "reviewer_relation",
        "schema",
        "verdict",
    }
    expected_artifacts = {
        "preexecution/INDEPENDENT_DEPLOYMENT_REVIEW.json": digests["deployment_review"],
        "preexecution/code_manifest.json": digests["code_manifest"],
        "runtime/candidate_v1/official/durable_claim.json": digests["durable_claim"],
        "runtime/candidate_v1/official/raw_result.json": digests["raw_result"],
        "runtime/candidate_v1/official/terminal.json": digests["terminal"],
    }
    required_checks = {
        "HASH_AND_CANONICAL_ARTIFACT_CLOSURE",
        "Q_R_CERTIFICATE_NAMESPACE_AND_AGREEMENT",
        "P1_P10_AND_NEGATIVE_CONTROL_COMPLETENESS",
        "COUNTERS_NONCLAIMS_AND_SCOPE",
        "NO_SECOND_SCIENTIFIC_EXECUTION",
    }
    if (type(review) is not dict or set(review) != review_keys
            or review["schema"] != "HENON_PERIOD3_INDEPENDENT_RESULT_REVIEW_V1"
            or review["candidate_id"] != "henon_period3_residue_v1"
            or review["reviewer_relation"] != "FRESH_INDEPENDENT_RESULT_ONLY"
            or review["reviewer_authored_candidate_code"] is not False
            or review["verdict"] != "RESULT_PASS"
            or type(review["registered_execution_count_observed"]) is not int
            or review["registered_execution_count_observed"] != 1
            or review["reviewed_artifacts"] != expected_artifacts
            or type(review["required_checks"]) is not dict
            or set(review["required_checks"]) != required_checks
            or any(review["required_checks"][key] != "PASS" for key in required_checks)
            or type(review["blocking_findings"]) is not list
            or review["blocking_findings"]
            or type(review["advisories"]) is not list):
        raise ValueError("postrun independent result review")
    return {
        "schema": "HENON_PERIOD3_APPEND_ONLY_RESULT_MANIFEST_V1",
        "candidate_id": "henon_period3_residue_v1",
        "run_id": "R100",
        "state": "SEALED_RESULT_PASS",
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "proof_sha256": PROOF_SHA256,
        "code_tree_sha256": result["code_tree_sha256"],
        "analyzer_sha256": analyzer_sha256,
        "artifact_sha256": {
            "durable_claim": digests["durable_claim"],
            "raw_result": digests["raw_result"],
            "terminal": digests["terminal"],
            "code_manifest": digests["code_manifest"],
            "deployment_review": digests["deployment_review"],
            "result_review": digests["result_review"],
        },
        "registered_execution_count": 1,
        "postrun_scientific_evaluation_count": 0,
    }


def main():
    if len(os.sys.argv) != 1:
        raise RuntimeError("postrun analyzer accepts no arguments")
    project_root = Path(__file__).absolute().parents[2]
    manifest = build_result_manifest(project_root)
    target = project_root / "runtime/candidate_v1/official/result_manifest.json"
    _write_exclusive(target, _canonical(manifest))


if __name__ == "__main__":
    main()
