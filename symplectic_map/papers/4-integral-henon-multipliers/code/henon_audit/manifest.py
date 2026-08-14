"""Fail-closed final artifact and official-report linkage helpers."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

from .protocol import sha256_file

META_START = "<!-- HENON_AUDIT_META_V1"
META_END = "HENON_AUDIT_META_V1_END -->"
META_PATTERN = re.compile(
    rf"^{re.escape(META_START)}\s*\n(?P<payload>.*?)\n{re.escape(META_END)}\s*$",
    flags=re.MULTILINE | re.DOTALL,
)
HASH_PATTERN = re.compile(r"^[0-9a-f]{64}$")
CANDIDATE_ID = "integral_area_henon_multiplier_support_v1"

COMMON_META_FIELDS = {
    "schema_version",
    "artifact",
    "candidate_id",
    "official_full_run_status",
    "run_summary_sha256",
    "candidate_audit_sha256",
}
ARTIFACT_META_FIELDS = {
    "experiment_tracker": COMMON_META_FIELDS,
    "experiment_results": COMMON_META_FIELDS
    | {"candidate_executed", "must_run_failed"},
    "validation_report": COMMON_META_FIELDS
    | {"pytest_status", "pytest_xml_sha256"},
}
LEGACY_MACHINE_FIELD_PATTERN = re.compile(
    r"^[ \t]*(?:(?:>[ \t]*)|(?:(?:[-+*]|\d+[.)])[ \t]+))*"
    r"\*\*(?:Official full-run status|Run-summary SHA-256|"
    r"Candidate-audit SHA-256|Candidate executed|Must-run failed|"
    r"Pytest status|Pytest XML SHA-256):\*\*",
    flags=re.MULTILINE,
)


def collect_artifacts(project_root: Path, paths: Iterable[Path]) -> dict[str, dict[str, Any]]:
    """Hash an explicit artifact set and fail closed on missing files."""

    root = project_root.resolve()
    resolved = [path.resolve() for path in paths]
    missing = [str(path.relative_to(root)) for path in resolved if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"required final artifacts missing: {missing}")
    return {
        str(path.relative_to(root)): {
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
        for path in resolved
    }


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    duplicates: list[str] = []
    for key, value in pairs:
        if key in result:
            duplicates.append(key)
        result[key] = value
    if duplicates:
        raise ValueError(f"duplicate JSON metadata keys: {sorted(set(duplicates))}")
    return result


def render_audit_front_matter(metadata: dict[str, Any]) -> str:
    """Render the sole accepted machine-readable Markdown metadata block."""

    return (
        f"{META_START}\n"
        + json.dumps(metadata, indent=2, sort_keys=True)
        + f"\n{META_END}\n"
    )


def parse_audit_front_matter(path: Path, expected_artifact: str) -> dict[str, Any]:
    """Parse exactly one strict JSON front matter block and validate its schema."""

    if expected_artifact not in ARTIFACT_META_FIELDS:
        raise ValueError(f"unknown expected artifact schema: {expected_artifact}")
    text = path.read_text(encoding="utf-8")
    matches = list(META_PATTERN.finditer(text))
    if len(matches) != 1:
        raise ValueError(
            f"{path.name} must contain exactly one {META_START!r} block; found {len(matches)}"
        )
    if "PENDING_OFFICIAL_FULL_RUN" in text:
        raise ValueError(f"{path.name} retains PENDING_OFFICIAL_FULL_RUN")

    # Legacy bold status fields are forbidden rather than coexisting with the
    # JSON authority.  This prevents a stale human-visible FAIL field beside a
    # machine PASS block from becoming semantically ambiguous.
    body = text[: matches[0].start()] + text[matches[0].end() :]
    legacy_fields = LEGACY_MACHINE_FIELD_PATTERN.findall(body)
    if legacy_fields:
        raise ValueError(f"{path.name} contains forbidden legacy machine status fields")

    try:
        metadata = json.loads(
            matches[0].group("payload"), object_pairs_hook=_unique_json_object
        )
    except (json.JSONDecodeError, ValueError) as error:
        raise ValueError(f"invalid unique JSON metadata in {path.name}: {error}") from error
    if not isinstance(metadata, dict):
        raise ValueError(f"{path.name} metadata must be one JSON object")

    required = ARTIFACT_META_FIELDS[expected_artifact]
    actual = set(metadata)
    if actual != required:
        missing = sorted(required - actual)
        unknown = sorted(actual - required)
        raise ValueError(
            f"{path.name} metadata schema mismatch: missing={missing}, unknown={unknown}"
        )
    if metadata["schema_version"] != 1:
        raise ValueError(f"{path.name} has unknown schema_version")
    if metadata["artifact"] != expected_artifact:
        raise ValueError(f"{path.name} artifact kind conflicts with its role")
    if metadata["candidate_id"] != CANDIDATE_ID:
        raise ValueError(f"{path.name} has unknown candidate_id")
    if metadata["official_full_run_status"] != "PASS":
        raise ValueError(f"{path.name} has unknown or non-PASS official status")
    for field in ("run_summary_sha256", "candidate_audit_sha256"):
        if not isinstance(metadata[field], str) or not HASH_PATTERN.fullmatch(metadata[field]):
            raise ValueError(f"{path.name} has invalid {field}")

    if expected_artifact == "experiment_results":
        if metadata["candidate_executed"] is not True:
            raise ValueError("experiment_results must state candidate_executed=true")
        if type(metadata["must_run_failed"]) is not int or metadata["must_run_failed"] != 0:
            raise ValueError("experiment_results must state must_run_failed=0")
    elif expected_artifact == "validation_report":
        if metadata["pytest_status"] != "PASS":
            raise ValueError("validation_report has unknown or non-PASS pytest_status")
        if not isinstance(metadata["pytest_xml_sha256"], str) or not HASH_PATTERN.fullmatch(
            metadata["pytest_xml_sha256"]
        ):
            raise ValueError("validation_report has invalid pytest_xml_sha256")
    return metadata


def _parse_tracker_rows(text: str) -> dict[str, str]:
    """Parse every RNNN Markdown row, rejecting duplicates and unknown states."""

    rows: dict[str, str] = {}
    duplicates: list[str] = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.split("|")[1:-1]] if line.startswith("|") else []
        if not cells or not re.fullmatch(r"R\d+", cells[0]):
            continue
        if len(cells) != 4:
            raise ValueError(f"tracker run row must have exactly four cells: {line}")
        run_id, _purpose, status, _notes = cells
        if status not in {"PASS", "FAIL", "READY", "LOCKED"}:
            raise ValueError(f"tracker run {run_id} has unknown status {status!r}")
        if run_id in rows:
            duplicates.append(run_id)
        rows[run_id] = status
    if duplicates:
        raise ValueError(f"tracker contains duplicate run IDs: {sorted(set(duplicates))}")
    return rows


def validate_official_report_linkage(project_root: Path) -> dict[str, Any]:
    """Fail closed unless three unambiguous reports identify one passed run."""

    root = project_root.resolve()
    results = root / "results"
    run_summary_path = results / "run_summary.json"
    candidate_path = results / "candidate_multiplier_audit.json"
    pytest_path = results / "pytest.xml"
    tracker_path = root / "experiments" / "EXPERIMENT_TRACKER.md"
    experiment_results_path = results / "EXPERIMENT_RESULTS.md"
    validation_path = results / "VALIDATION_REPORT.md"

    required_paths = [
        run_summary_path,
        candidate_path,
        pytest_path,
        tracker_path,
        experiment_results_path,
        validation_path,
    ]
    missing = [str(path.relative_to(root)) for path in required_paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"official report linkage inputs missing: {missing}")

    summary = json.loads(run_summary_path.read_text(encoding="utf-8"))
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
    tracker_meta = parse_audit_front_matter(tracker_path, "experiment_tracker")
    experiment_meta = parse_audit_front_matter(
        experiment_results_path, "experiment_results"
    )
    validation_meta = parse_audit_front_matter(validation_path, "validation_report")

    run_hash = sha256_file(run_summary_path)
    candidate_hash = sha256_file(candidate_path)
    pytest_hash = sha256_file(pytest_path)
    expected_common = {
        "schema_version": 1,
        "candidate_id": CANDIDATE_ID,
        "official_full_run_status": "PASS",
        "run_summary_sha256": run_hash,
        "candidate_audit_sha256": candidate_hash,
    }
    metadata_records = {
        "tracker": tracker_meta,
        "experiment_results": experiment_meta,
        "validation_report": validation_meta,
    }
    checks: dict[str, bool] = {
        "summary_mode_full_exact_audit": summary.get("mode") == "full_exact_audit",
        "summary_status_pass": summary.get("status") == "PASS",
        "summary_candidate_executed": summary.get("candidate_executed") is True,
        "summary_no_must_run_failures": summary.get("must_run_failed") == 0,
        "candidate_id_consistent": summary.get("candidate_id")
        == candidate.get("candidate_id")
        == CANDIDATE_ID,
        "candidate_audit_pass": candidate.get("pass") is True,
        "all_metadata_link_the_same_exact_run": all(
            all(metadata.get(field) == value for field, value in expected_common.items())
            for metadata in metadata_records.values()
        ),
        "validation_links_exact_pytest_xml": validation_meta["pytest_xml_sha256"]
        == pytest_hash,
    }

    registry = summary.get("run_registry")
    if not isinstance(registry, list) or not registry:
        raise ValueError("run_summary run_registry must be a nonempty list")
    registry_ids: list[str] = []
    for item in registry:
        if not isinstance(item, dict) or set(item) != {"run_id", "status"}:
            raise ValueError("each run_registry record must contain exactly run_id and status")
        if not re.fullmatch(r"R\d+", str(item["run_id"])):
            raise ValueError(f"unknown run_registry run_id: {item['run_id']!r}")
        if item["status"] != "PASS":
            raise ValueError(f"run_registry {item['run_id']} has non-PASS or unknown status")
        registry_ids.append(item["run_id"])
    if len(registry_ids) != len(set(registry_ids)):
        raise ValueError("run_summary run_registry contains duplicate run IDs")

    tracker_rows = _parse_tracker_rows(tracker_path.read_text(encoding="utf-8"))
    required_run_ids = set(registry_ids)
    checks["tracker_run_id_set_exact"] = set(tracker_rows) == required_run_ids
    checks["tracker_marks_every_run_pass"] = all(
        tracker_rows.get(run_id) == "PASS" for run_id in required_run_ids
    )

    if not all(checks.values()):
        failed = sorted(name for name, passed in checks.items() if not passed)
        raise ValueError(f"official report linkage failed: {failed}")
    return {
        "status": "PASS",
        "metadata_schema": "HENON_AUDIT_META_V1",
        "run_summary_sha256": run_hash,
        "candidate_audit_sha256": candidate_hash,
        "pytest_xml_sha256": pytest_hash,
        "required_run_ids": sorted(required_run_ids),
        "checks": checks,
    }
