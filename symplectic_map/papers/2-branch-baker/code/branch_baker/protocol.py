"""Hash-bound split access and reproducibility helpers."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CODE_ROOT = PROJECT_ROOT / "code"
EXPERIMENTS_ROOT = PROJECT_ROOT / "experiments"
RESULTS_ROOT = PROJECT_ROOT / "results"
SOURCE_LOCK_PATH = EXPERIMENTS_ROOT / "source_lock.json"
VALIDATION_UNLOCK_PATH = EXPERIMENTS_ROOT / "validation_unlock.json"
VERIFICATION_MANIFEST_PATH = EXPERIMENTS_ROOT / "verification_manifest.json"
TEST_UNLOCK_PATH = EXPERIMENTS_ROOT / "test_unlock.json"
ACCESS_LOG_PATH = EXPERIMENTS_ROOT / "test_access_log.md"
REQUIRED_DEVELOPMENT_ARTIFACTS = (
    "results/analysis_development.json",
    "results/exact_preflight.json",
    "results/float_stress_development.json",
    "results/ledger.json",
    "results/parent_audit.json",
    "results/pytest_development.xml",
)
REQUIRED_VALIDATION_ARTIFACTS = (
    "results/analysis_validation.json",
    "results/float_stress_validation.json",
)


class ProtocolError(RuntimeError):
    """Raised when a frozen access or hash condition is violated."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_tree_hash(paths: Iterable[Path], base: Path = PROJECT_ROOT) -> str:
    """Hash relative names and bytes, making additions/removals detectable."""

    digest = hashlib.sha256()
    resolved = sorted({Path(path).resolve() for path in paths})
    for path in resolved:
        if not path.is_file():
            raise ProtocolError(f"Cannot hash missing artifact: {path}")
        try:
            relative = path.relative_to(base.resolve()).as_posix()
        except ValueError as exc:
            raise ProtocolError(f"Artifact lies outside project root: {path}") from exc
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(sha256_file(path)))
        digest.update(b"\0")
    return digest.hexdigest()


def frozen_code_files() -> list[Path]:
    files = [
        path
        for path in CODE_ROOT.rglob("*.py")
        if "__pycache__" not in path.parts
    ]
    files.extend(
        [
            PROJECT_ROOT / "pyproject.toml",
            EXPERIMENTS_ROOT / "EXPERIMENT_PLAN.md",
            SOURCE_LOCK_PATH,
            PROJECT_ROOT / "PROOF_PACKAGE.md",
        ]
    )
    return sorted(files)


def code_tree_sha256() -> str:
    return canonical_tree_hash(frozen_code_files())


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ProtocolError(f"Expected JSON object at {path}")
    return value


def write_json_new(path: Path, payload: Mapping) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(serialized)
    except FileExistsError as exc:
        raise ProtocolError(f"Refusing to overwrite frozen artifact: {path}") from exc


def file_hash_map(paths: Iterable[Path]) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(Path(item).resolve() for item in paths):
        if not path.is_file():
            raise ProtocolError(f"Required artifact does not exist: {path}")
        try:
            relative = path.relative_to(PROJECT_ROOT).as_posix()
        except ValueError as exc:
            raise ProtocolError(f"Artifact lies outside project root: {path}") from exc
        result[relative] = sha256_file(path)
    return result


def _require_exact_artifact_set(
    paths: Iterable[Path], required_relative: tuple[str, ...], stage: str
) -> list[Path]:
    resolved = sorted({Path(path).resolve() for path in paths})
    required = sorted((PROJECT_ROOT / relative).resolve() for relative in required_relative)
    if resolved != required:
        supplied_names = []
        for path in resolved:
            try:
                supplied_names.append(path.relative_to(PROJECT_ROOT).as_posix())
            except ValueError:
                supplied_names.append(str(path))
        raise ProtocolError(
            f"{stage} artifact set must equal the frozen whitelist; "
            f"required={list(required_relative)!r}, supplied={supplied_names!r}"
        )
    return resolved


def _verify_exact_hash_keys(
    entries: Mapping[str, str], required_relative: tuple[str, ...], stage: str
) -> None:
    if set(entries) != set(required_relative):
        raise ProtocolError(
            f"{stage} marker artifact keys differ from the frozen whitelist"
        )


def verify_hash_map(entries: Mapping[str, str]) -> None:
    for relative, expected in entries.items():
        path = PROJECT_ROOT / relative
        if not path.is_file():
            raise ProtocolError(f"Frozen artifact disappeared: {relative}")
        actual = sha256_file(path)
        if actual != expected:
            raise ProtocolError(
                f"Frozen artifact drifted: {relative}; expected {expected}, got {actual}"
            )


def analysis_script_sha256() -> str:
    path = CODE_ROOT / "scripts" / "analyze_carrier.py"
    if not path.is_file():
        raise ProtocolError("Analysis script is not implemented")
    return sha256_file(path)


def build_validation_unlock(
    development_artifacts: Iterable[Path], created_utc: str
) -> dict:
    """Build, but do not write, the validation unlock declaration."""

    frozen_artifacts = _require_exact_artifact_set(
        development_artifacts,
        REQUIRED_DEVELOPMENT_ARTIFACTS,
        "development",
    )
    return {
        "candidate_id": "pcf_markov_baker_v1",
        "created_utc": created_utc,
        "source_lock_sha256": sha256_file(SOURCE_LOCK_PATH),
        "code_tree_sha256": code_tree_sha256(),
        "analysis_sha256": analysis_script_sha256(),
        "development_artifacts": file_hash_map(frozen_artifacts),
        "validation_accessed_before_unlock": False,
        "test_accessed_before_unlock": False,
    }


def _verify_common_marker(marker: Mapping) -> None:
    if marker.get("candidate_id") != "pcf_markov_baker_v1":
        raise ProtocolError("Unlock marker has the wrong candidate id")
    if marker.get("source_lock_sha256") != sha256_file(SOURCE_LOCK_PATH):
        raise ProtocolError("Source lock changed after split unlock")
    if marker.get("code_tree_sha256") != code_tree_sha256():
        raise ProtocolError("Code tree changed after split unlock")
    if marker.get("analysis_sha256") != analysis_script_sha256():
        raise ProtocolError("Analysis code changed after split unlock")
    artifacts = marker.get("development_artifacts")
    if not isinstance(artifacts, dict) or not artifacts:
        raise ProtocolError("Unlock marker has no development artifact hashes")
    _verify_exact_hash_keys(
        artifacts, REQUIRED_DEVELOPMENT_ARTIFACTS, "development"
    )
    verify_hash_map(artifacts)


def verify_validation_unlock() -> dict:
    if not VALIDATION_UNLOCK_PATH.is_file():
        raise ProtocolError("Validation is locked: validation_unlock.json is absent")
    marker = load_json(VALIDATION_UNLOCK_PATH)
    _verify_common_marker(marker)
    for field in (
        "validation_accessed_before_unlock",
        "test_accessed_before_unlock",
    ):
        if marker.get(field) is not False:
            raise ProtocolError(f"Validation unlock must explicitly record {field}=false")
    return marker


def build_verification_manifest(
    validation_artifacts: Iterable[Path], created_utc: str
) -> dict:
    validation_unlock = verify_validation_unlock()
    frozen_validation = _require_exact_artifact_set(
        validation_artifacts,
        REQUIRED_VALIDATION_ARTIFACTS,
        "validation",
    )
    return {
        "candidate_id": "pcf_markov_baker_v1",
        "created_utc": created_utc,
        "source_lock_sha256": sha256_file(SOURCE_LOCK_PATH),
        "code_tree_sha256": code_tree_sha256(),
        "analysis_sha256": analysis_script_sha256(),
        "development_artifacts": dict(validation_unlock["development_artifacts"]),
        "validation_artifacts": file_hash_map(frozen_validation),
        "test_accessed_before_manifest": False,
    }


def verify_verification_manifest() -> dict:
    if not VERIFICATION_MANIFEST_PATH.is_file():
        raise ProtocolError("Verification manifest is absent")
    manifest = load_json(VERIFICATION_MANIFEST_PATH)
    _verify_common_marker(manifest)
    if manifest.get("test_accessed_before_manifest") is not False:
        raise ProtocolError(
            "Verification manifest must explicitly record "
            "test_accessed_before_manifest=false"
        )
    validation = manifest.get("validation_artifacts")
    if not isinstance(validation, dict) or not validation:
        raise ProtocolError("Verification manifest has no validation artifacts")
    _verify_exact_hash_keys(validation, REQUIRED_VALIDATION_ARTIFACTS, "validation")
    verify_hash_map(validation)
    return manifest


def build_test_unlock(created_utc: str) -> dict:
    manifest = verify_verification_manifest()
    return {
        "candidate_id": "pcf_markov_baker_v1",
        "created_utc": created_utc,
        "source_lock_sha256": manifest["source_lock_sha256"],
        "code_tree_sha256": manifest["code_tree_sha256"],
        "analysis_sha256": manifest["analysis_sha256"],
        "development_artifacts": dict(manifest["development_artifacts"]),
        "validation_artifacts": dict(manifest["validation_artifacts"]),
        "verification_manifest_sha256": sha256_file(VERIFICATION_MANIFEST_PATH),
        "test_accessed_before_unlock": False,
    }


def verify_test_unlock() -> dict:
    if not TEST_UNLOCK_PATH.is_file():
        raise ProtocolError("Sealed test is locked: test_unlock.json is absent")
    marker = load_json(TEST_UNLOCK_PATH)
    _verify_common_marker(marker)
    if marker.get("test_accessed_before_unlock") is not False:
        raise ProtocolError(
            "Test unlock must explicitly record test_accessed_before_unlock=false"
        )
    validation = marker.get("validation_artifacts")
    if not isinstance(validation, dict) or not validation:
        raise ProtocolError("Test marker has no validation artifact hashes")
    _verify_exact_hash_keys(validation, REQUIRED_VALIDATION_ARTIFACTS, "validation")
    verify_hash_map(validation)
    manifest_hash = marker.get("verification_manifest_sha256")
    if manifest_hash != sha256_file(VERIFICATION_MANIFEST_PATH):
        raise ProtocolError("Verification manifest changed after test unlock")
    verify_verification_manifest()
    return marker


def require_split(split: str) -> None:
    if split == "development":
        return
    if split == "validation":
        verify_validation_unlock()
        return
    if split == "test":
        verify_test_unlock()
        return
    raise ProtocolError(f"Unknown split: {split}")


def append_access_log(
    utc_time: str, split: str, action: str, authorization: str, result: str
) -> None:
    if split not in {"validation", "test"}:
        return
    line = f"| {utc_time} | {split} | {action} | {authorization} | {result} |\n"
    with ACCESS_LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(line)
