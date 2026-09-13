#!/usr/bin/env python3
"""Generate the immutable batch closeout for Round 10 Stage 4.5 Round 2.

This is an audit-side packager.  It never edits a manuscript, bibliography,
canonical artifact, result, Route state, README, or pipeline-state file.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
ARS_ROOT = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/"
    "skills/academic-research-suite/ars"
)
LOCK_PATH = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
AUTH_PATH = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"
VALIDATOR_PATH = ROOT / "tools/audit_round10_stage4_5_round2.rb"
FINAL_INDEPENDENT_REVIEW_PATH = (
    ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_INDEPENDENT_REPLAY.json"
)

EXPECTED_LOCK_SHA = "11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0"
EXPECTED_AUTH_SHA = "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60"
EXPECTED_VALIDATOR_CHECKS = 89
EXPECTED_FINAL_INDEPENDENT_REVIEW_STATUS = "PASS_FINAL_INDEPENDENT_REPLAY"
EXPECTED_FINAL_INDEPENDENT_REVIEW_SHA = "2596f8caa15c91a04f7bb33d69bbc231f0e2154df6d6bc01f1e1db50d304094f"
EXPECTED_FINAL_INDEPENDENT_REVIEW_SCHEMA = "round10-stage4.5-round2-final-independent-replay/1.0"
EXPECTED_FINAL_INDEPENDENT_REVIEW_KEYS = {
    "aggregate",
    "authority",
    "findings",
    "generated_at_utc",
    "input_lock",
    "papers",
    "protected_boundary_replay",
    "root_replay",
    "route_boundary",
    "schema_version",
    "scientific_integrity_batch_verdict",
    "status",
    "validator",
}
EXPECTED_ROUTE_BOUNDARY = {
    "formal_route_a_tuples": "0/5",
    "positive_arithmetic_A2": "0/5",
    "A3": "0/5",
    "A4": "0/5",
    "route_b_invocations": "0/5",
}
EXPECTED_CLAIM_VERDICT_COUNTS = {
    "MAJOR_DISTORTION": 13,
    "UNVERIFIABLE": 98,
    "VERIFIED": 686,
}
EXPECTED_PAPER_CLAIM_VERDICTS = {
    "P29": {"MAJOR_DISTORTION": 2, "UNVERIFIABLE": 20, "VERIFIED": 67},
    "P30": {"MAJOR_DISTORTION": 7, "UNVERIFIABLE": 4, "VERIFIED": 96},
    "P31": {"MAJOR_DISTORTION": 2, "UNVERIFIABLE": 6, "VERIFIED": 119},
    "P32": {"MAJOR_DISTORTION": 2, "UNVERIFIABLE": 6, "VERIFIED": 90},
    "P33": {"UNVERIFIABLE": 62, "VERIFIED": 314},
}
EXPECTED_PAPER_ORIGINALITY = {
    "P29": {"body": [62, 77], "changed": [49, 49]},
    "P30": {"body": [67, 82], "changed": [54, 54]},
    "P31": {"body": [50, 63], "changed": [30, 30]},
    "P32": {"body": [52, 77], "changed": [35, 35]},
    "P33": {"body": [38, 72], "changed": [38, 38]},
}
EXPECTED_NONVERIFIED_CLAIM_ANCHORS = {
    "P30": {
        "P30-S45R2-E1-001": "B0004",
        "P30-S45R2-E1-047": "B0057",
        "P30-S45R2-E1-049": "B0060",
        "P30-S45R2-E1-050": "B0061",
        "P30-S45R2-E1-051": "B0062",
        "P30-S45R2-E1-053": "B0065",
        "P30-S45R2-E1-083": "B0096",
        "P30-S45R2-E1-092": "B0106",
        "P30-S45R2-E1-094": "B0108",
        "P30-S45R2-E1-106": "B0124",
        "P30-S45R2-E1-107": "B0125",
    },
    "P31": {
        "P31-S45R2-E1-008": "B0016",
        "P31-S45R2-E1-067": "B0030",
        "P31-S45R2-E1-077": "B0112",
        "P31-S45R2-E1-079": "B0037",
        "P31-S45R2-E1-080": "B0038",
        "P31-S45R2-E1-108": "B0079",
        "P31-S45R2-E1-125": "B0105",
        "P31-S45R2-E1-126": "B0107",
    },
}

REQUEST_JSON = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.json"
REQUEST_MD = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.md"
FINAL_AUDIT_JSON = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_AUDIT.json"
FINAL_REPORT_MD = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_INTEGRITY_REPORT.md"
CHECKPOINT_MD = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_MANDATORY_CHECKPOINT.md"
RECEIPT_JSON = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_VALIDATION_RECEIPT.json"


PAPERS: dict[str, dict[str, Any]] = {
    "P29": {
        "number": 29,
        "slug": "29-bianchi-ideal-owner-refinement",
        "title": "Bianchi ideal-owner refinement",
        "draft": "stage4_prime_revision_round3.tex",
        "block_manifest": "stage4_prime_revision_round3.block-manifest.json",
        "targets": [
            "B0004", "B0006", "B0040", "B0048", "B0049", "B0051", "B0055",
            "B0075", "B0076", "B0080", "B0084", "B0087", "B0089", "B0090",
            "B0091", "B0100", "B0103", "B0107", "B0108", "B0109",
        ],
        "target_issue": {
            "B0006": ["P29-S45R2-I01-TRANSLATED-ABSTRACT-STATUS"],
        },
        "default_issue": ["P29-S45R2-I03-LOCAL-EVIDENCE-ANCHOR"],
        "successor": "stage4_prime_revision_round4.tex",
        "issue_count": 2,
        "strategy": (
            "Apply the already proposed exact B0006 status correction.  In the remaining listed "
            "blocks, retain verified components but narrow or remove only components whose raw "
            "carrier is absent; do not turn absence into a mathematical negative result."
        ),
    },
    "P30": {
        "number": 30,
        "slug": "30-three-disk-nonconstant-roof-determinant",
        "title": "Three-disk nonconstant-roof determinant",
        "draft": "stage4_prime_revision_round3.tex",
        "block_manifest": "stage4_prime_revision_round3.block-manifest.json",
        "targets": [
            "B0004", "B0057", "B0060", "B0061", "B0062", "B0065", "B0096",
            "B0106", "B0108", "B0124", "B0125",
        ],
        "target_issue": {
            "B0004": ["P30-LIVSIC-PASSAGE"],
            "B0057": ["P30-LIVSIC-PASSAGE"],
            "B0060": ["P30-CORRECTION-RELATION"],
            "B0061": ["P30-REVIEW-ROLE-ENUMERATION"],
            "B0062": ["P30-CORRECTION-RELATION"],
            "B0065": ["P30-CORRECTION-RELATION"],
            "B0096": ["P30-LIVSIC-PASSAGE"],
            "B0106": ["P30-CORRECTION-RELATION"],
            "B0108": ["P30-STALE-SEARCH-STATUS"],
            "B0124": ["P30-AI-METADATA-CARRIER"],
            "B0125": ["P30-STALE-STAGE4-5-RERUN-STATUS"],
        },
        "default_issue": [],
        "successor": "stage4_prime_revision_round4.tex",
        "issue_count": 6,
        "strategy": (
            "Correct only the P30-S02 companion relation to DOI 10.1063/1.457672, preserve "
            "P30-C01 -> P30-S01 and P30-C02 -> P30-S03, correct B0061's false four-role "
            "enumeration without inventing a review role, reconcile the stale search-status and "
            "fresh-rerun-status sentences, and conservatively narrow the unsupported Livsic and "
            "AI-history clauses."
        ),
    },
    "P31": {
        "number": 31,
        "slug": "31-level11-conjugacy-owner-ledger",
        "title": "Level-11 conjugacy-owner ledger",
        "draft": "stage4_prime_revision_round3.tex",
        "block_manifest": "stage4_prime_revision_round3.block-manifest.json",
        "targets": [
            "B0016", "B0030", "B0112", "B0037", "B0038", "B0079", "B0105", "B0107",
        ],
        "target_issue": {
            "B0016": ["P31-S23-S24-PASSAGES"],
            "B0030": ["P31-OVERBROAD-LITERATURE-NEGATIVE"],
            "B0112": ["P31-S23-S24-PASSAGES"],
            "B0037": ["P31-S23-S24-PASSAGES"],
            "B0038": ["P31-S23-S24-PASSAGES"],
            "B0079": ["P31-STALE-READER-MANIFEST"],
            "B0105": ["P31-STALE-READER-MANIFEST"],
            "B0107": ["P31-AI-METADATA-CARRIER"],
        },
        "default_issue": [],
        "successor": "stage4_prime_revision_round4.tex",
        "issue_count": 4,
        "strategy": (
            "Treat P31-S23/P31-S24 as metadata-only unless an exact original passage is already "
            "bound; narrow or remove their substantive method-pattern transfers in the four "
            "affected prose blocks, narrow the overbroad literature-negative claim to the admitted "
            "project-use boundary, correct the two claims relying on the stale reader manifest, "
            "and narrow the AI-history clause to locked metadata."
        ),
    },
    "P32": {
        "number": 32,
        "slug": "32-homology-cover-renormalization-uniformity",
        "title": "Homology-cover renormalization uniformity",
        "draft": "stage4_prime_revision_round3.tex",
        "block_manifest": "stage4_prime_revision_round3.block-manifest.json",
        "targets": ["B0007", "B0018", "B0112", "B0121", "B0127", "B0128", "B0138"],
        "target_issue": {
            "B0007": ["P32-S45R2-I01-TRANSLATED-ABSTRACT-STATUS"],
            "B0018": ["P32-S45R2-I04-CW-EXCERPT-BINDING"],
        },
        "default_issue": ["P32-S45R2-I03-LOCAL-EVIDENCE-ANCHOR"],
        "successor": "stage4_prime_revision_round4.tex",
        "issue_count": 3,
        "strategy": (
            "Apply the already proposed exact B0007 status correction; keep CW01--CW04 "
            "unverifiable and narrow B0018 to metadata-only; in the remaining blocks remove only "
            "the components lacking raw activity/author/provenance carriers."
        ),
    },
    "P33": {
        "number": 33,
        "slug": "33-bolza-control-matched-census",
        "title": "Bolza control-matched census",
        "draft": "stage4_prime_revision_round2.tex",
        "block_manifest": "stage4_prime_revision_round2.block-manifest.json",
        "targets": [
            "B0007", "B0015", "B0025", "B0026", "B0027", "B0029", "B0030",
            "B0032", "B0033", "B0036", "B0037", "B0044", "B0061", "B0062",
            "B0067", "B0072", "B0077", "B0091", "B0108", "B0124",
        ],
        "target_issue": {
            **{key: ["IL-SERIOUS-1"] for key in [
                "B0015", "B0025", "B0026", "B0027", "B0029", "B0030", "B0032",
                "B0033", "B0036", "B0037", "B0044", "B0067", "B0077", "B0091",
            ]},
            **{key: ["IL-MEDIUM-1"] for key in [
                "B0007", "B0061", "B0062", "B0072", "B0108", "B0124",
            ]},
        },
        "default_issue": [],
        "successor": "stage4_prime_revision_round3.tex",
        "issue_count": 2,
        "strategy": (
            "Use the conservative no-new-execution branch: narrow or remove every source-dependent "
            "claim lacking an original passage, and remove evidentiary interpretation of the 14/14 "
            "same-lineage synthetic harness while preserving its diagnostic/non-scientific record."
        ),
    },
}


READONLY_FILES = [
    "README.md",
    *[f"papers/{cfg['slug']}/README.md" for cfg in PAPERS.values()],
    *[f"papers/{cfg['slug']}/notes/pipeline_state.md" for cfg in PAPERS.values()],
    *[f"papers/{cfg['slug']}/paper/README.md" for cfg in PAPERS.values()],
]


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def artifact(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha_bytes(raw), "bytes": len(raw)}


def pending_artifact(path: Path, raw: bytes) -> dict[str, Any]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha_bytes(raw), "bytes": len(raw)}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def atomic_write(path: Path, raw: bytes) -> None:
    fd, temp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
        os.replace(temp_name, path)
    except BaseException:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
        raise


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def replay_root_validator() -> dict[str, Any]:
    command = ["ruby", str(VALIDATOR_PATH)]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    combined = completed.stdout + b"\n" + completed.stderr
    match = re.search(rb"Checks passed:\s*(\d+)", combined)
    checks = int(match.group(1)) if match else -1
    marker = b"ROUND10_STAGE4_5_ROUND2_AUDIT_PASS"
    if completed.returncode != 0 or checks != EXPECTED_VALIDATOR_CHECKS or marker not in combined:
        tail = combined[-4000:].decode("utf-8", errors="replace")
        raise RuntimeError(
            "root validator did not pass exactly "
            f"(exit={completed.returncode}, checks={checks}, marker={marker in combined}):\n{tail}"
        )
    return {
        "validator": artifact(VALIDATOR_PATH),
        "command": "ruby tools/audit_round10_stage4_5_round2.rb",
        "exit_code": completed.returncode,
        "checks_passed": checks,
        "terminal_marker": marker.decode("ascii"),
        "stdout_sha256": sha_bytes(completed.stdout),
        "stdout_bytes": len(completed.stdout),
        "stderr_sha256": sha_bytes(completed.stderr),
        "stderr_bytes": len(completed.stderr),
    }


def require_workspace_file(path: Path, label: str) -> Path:
    try:
        relative = path.relative_to(ROOT)
    except ValueError as exc:
        raise RuntimeError(f"{label} escapes the workspace: {path}") from exc
    if any(part in {"", ".", ".."} for part in relative.parts):
        raise RuntimeError(f"{label} contains a non-canonical path component: {path}")
    cursor = ROOT
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            raise RuntimeError(f"{label} contains a symlink component: {cursor}")
    if not path.is_file():
        raise RuntimeError(f"{label} is not a regular file: {path}")
    return path


def exact_artifact(path: Path, label: str) -> dict[str, Any]:
    return artifact(require_workspace_file(path, label))


def manifest_path_for_independent_replay(notes: Path, paper_id: str) -> Path:
    candidates = [
        notes / "stage4_5_round2_output_manifest.json",
        notes / "stage4_5_round2_package_manifest.json",
    ]
    existing = [path for path in candidates if path.exists() or path.is_symlink()]
    if len(existing) != 1:
        raise RuntimeError(
            f"{paper_id} must have exactly one controlling Round-2 manifest, got "
            f"{[path.name for path in existing]}"
        )
    return require_workspace_file(existing[0], f"{paper_id} controlling manifest")


def normalized_component_verdict(value: str) -> str:
    if value == "MAJOR_DISTORTION" or value.startswith("CONTRADICT") or value.startswith("MAJOR_DISTORTION"):
        return "MAJOR_DISTORTION"
    if value.startswith("UNVERIFIABLE"):
        return "UNVERIFIABLE"
    if value.startswith("MINOR_DISTORTION"):
        return "MINOR_DISTORTION"
    if value == "VERIFIED" or value.startswith("VERIFIED") or value.startswith("EXACT_SURFACE_PRESENT"):
        return "VERIFIED"
    raise RuntimeError(f"unknown component-semantic verdict: {value}")


def catalog_dependencies(catalog: dict[str, Any], paper_id: str) -> list[dict[str, Any]]:
    dependencies = list(catalog.get("dependencies", []))
    if not dependencies:
        raise RuntimeError(f"{paper_id} dependency catalog is empty")
    known_ids = {row.get("evidence_row_id") for row in dependencies}
    for row in catalog.get("missing_dependencies", []):
        if row.get("evidence_row_id") not in known_ids:
            dependencies.append(row)
            known_ids.add(row.get("evidence_row_id"))
    row_ids = [row.get("evidence_row_id") for row in dependencies]
    if None in row_ids or len(row_ids) != len(set(row_ids)):
        raise RuntimeError(f"{paper_id} dependency catalog has absent/duplicate evidence-row IDs")
    return dependencies


def independent_paper_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for paper_id, cfg in PAPERS.items():
        notes = ROOT / "papers" / cfg["slug"] / "notes"
        registry_path = require_workspace_file(
            notes / "stage4_5_round2_claim_registry.json", f"{paper_id} claim registry"
        )
        evidence_path = require_workspace_file(
            notes / "stage4_5_round2_evidence_rows.json", f"{paper_id} evidence rows"
        )
        report_path = require_workspace_file(
            notes / "stage4_5_round2_integrity_report.json", f"{paper_id} integrity report"
        )
        manifest_path = manifest_path_for_independent_replay(notes, paper_id)
        registry = load_json(registry_path)
        evidence = load_json(evidence_path)
        report = load_json(report_path)
        if not isinstance(evidence, list) or not evidence:
            raise RuntimeError(f"{paper_id} evidence rows are empty or not an array")
        claims = registry.get("claims")
        if not isinstance(claims, list) or not claims:
            raise RuntimeError(f"{paper_id} registry claims are empty or not an array")
        registry_claim_ids = [row.get("claim_id") for row in claims]
        if None in registry_claim_ids or len(registry_claim_ids) != len(set(registry_claim_ids)):
            raise RuntimeError(f"{paper_id} registry claim IDs are absent or duplicated")
        evidence_row_ids = [row.get("row_id") for row in evidence]
        if None in evidence_row_ids or len(evidence_row_ids) != len(set(evidence_row_ids)):
            raise RuntimeError(f"{paper_id} EVR row IDs are absent or duplicated")
        evidence_claim_ids = {row.get("claim", {}).get("claim_id") for row in evidence}
        if None in evidence_claim_ids:
            raise RuntimeError(f"{paper_id} EVR contains an absent claim ID")
        if evidence_claim_ids != set(registry_claim_ids):
            raise RuntimeError(
                f"{paper_id} registry/EVR claim populations differ: "
                f"{sorted(set(registry_claim_ids) - evidence_claim_ids)} missing from EVR; "
                f"{sorted(evidence_claim_ids - set(registry_claim_ids))} unknown in EVR"
            )
        claim_counts = count_claim_verdicts(evidence)
        if claim_counts != EXPECTED_PAPER_CLAIM_VERDICTS[paper_id]:
            raise RuntimeError(
                f"{paper_id} independent claim verdicts: {claim_counts} != "
                f"{EXPECTED_PAPER_CLAIM_VERDICTS[paper_id]}"
            )
        evr_counts = dict(sorted(Counter(row["verdict"] for row in evidence).items()))
        report_verdict = report.get("verdict", report.get("integrity_verdict"))
        if not str(report_verdict).startswith("FAIL") or report.get("stage5_started") is not False:
            raise RuntimeError(f"{paper_id} independent package is not fail-closed")
        phase_a = report["phases"]["A_references"]
        phase_b = report["phases"]["B_citation_contexts"]
        phase_d = report["phases"]["D_originality"]
        originality = {
            "body": [
                phase_d.get("body_successful", int(str(phase_d.get("body", "0/0")).split("/")[0])),
                phase_d.get("body_denominator", int(str(phase_d.get("body", "0/0")).split("/")[-1])),
            ],
            "changed": [
                phase_d.get("changed_successful", int(str(phase_d.get("changed_body", "0/0")).split("/")[0])),
                phase_d.get("changed_denominator", int(str(phase_d.get("changed_body", "0/0")).split("/")[-1])),
            ],
        }
        if originality != EXPECTED_PAPER_ORIGINALITY[paper_id]:
            raise RuntimeError(
                f"{paper_id} independent originality: {originality} != "
                f"{EXPECTED_PAPER_ORIGINALITY[paper_id]}"
            )

        catalog_descriptor: dict[str, Any] | None = None
        component_count: int | None = None
        component_counts: dict[str, int] | None = None
        if paper_id != "P33":
            catalog_path = require_workspace_file(
                notes / "stage4_5_round2_local_claim_dependency_catalog.json",
                f"{paper_id} dependency catalog",
            )
            catalog = load_json(catalog_path)
            dependencies = catalog_dependencies(catalog, paper_id)
            component_count = len(dependencies)
            component_counts = dict(
                sorted(
                    Counter(
                        normalized_component_verdict(row["component_semantic_verdict"])
                        for row in dependencies
                    ).items()
                )
            )
            catalog_descriptor = exact_artifact(catalog_path, f"{paper_id} dependency catalog")
        elif (notes / "stage4_5_round2_local_claim_dependency_catalog.json").exists():
            raise RuntimeError("P33 unexpectedly acquired a local dependency catalog")

        rows.append(
            {
                "paper_id": paper_id,
                "scientific_integrity_verdict": report_verdict,
                "stage5_started": False,
                "controlling_manifest": exact_artifact(manifest_path, f"{paper_id} controlling manifest"),
                "dependency_catalog": catalog_descriptor,
                "evidence_rows": exact_artifact(evidence_path, f"{paper_id} evidence rows"),
                "claim_registry": exact_artifact(registry_path, f"{paper_id} claim registry"),
                "integrity_report": exact_artifact(report_path, f"{paper_id} integrity report"),
                "denominators": {
                    "references": phase_a["registered"],
                    "citation_contexts": phase_b["registered"],
                    "registered_claims": len(registry["claims"]),
                    "evidence_rows": len(evidence),
                    "dependency_components": component_count,
                    "claim_verdict_counts": claim_counts,
                    "component_verdict_counts": component_counts,
                    "evr_verdict_counts": evr_counts,
                    "originality": originality,
                },
            }
        )
    return rows


def descriptor_rows(value: Any, rows: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    if rows is None:
        rows = []
    if isinstance(value, dict):
        path_value = value.get("path", value.get("repo_path"))
        if (
            isinstance(path_value, str)
            and isinstance(value.get("sha256"), str)
            and isinstance(value.get("bytes"), int)
        ):
            rows.append({"path": path_value, "sha256": value["sha256"], "bytes": value["bytes"]})
        for child in value.values():
            descriptor_rows(child, rows)
    elif isinstance(value, list):
        for child in value:
            descriptor_rows(child, rows)
    return rows


def verify_locked_descriptor(row: dict[str, Any], label: str) -> dict[str, Any]:
    path = require_workspace_file(ROOT / row["path"], label)
    observed = exact_artifact(path, label)
    if observed != row:
        raise RuntimeError(f"{label} does not match the frozen input-lock descriptor")
    return observed


def science_tree_digest(path: Path) -> tuple[str, int]:
    if path.is_symlink() or not path.is_dir():
        raise RuntimeError(f"unsafe/missing protected science tree: {path}")
    rows: list[tuple[str, str]] = []
    for current, directories, filenames in os.walk(path, followlinks=False):
        current_path = Path(current)
        for name in directories:
            if (current_path / name).is_symlink():
                raise RuntimeError(f"symlink in protected science tree: {current_path / name}")
        for name in filenames:
            child = current_path / name
            require_workspace_file(child, "protected science-tree file")
            rows.append((child.relative_to(ROOT).as_posix(), sha_bytes(child.read_bytes())))
    raw = "".join(f"{digest}  {name}\n" for name, digest in sorted(rows)).encode("utf-8")
    return sha_bytes(raw), len(rows)


def protected_boundary_replay() -> dict[str, Any]:
    lock = load_json(require_workspace_file(LOCK_PATH, "input lock"))
    unique_rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str, int]] = set()
    for row in descriptor_rows(lock):
        key = (row["path"], row["sha256"], row["bytes"])
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)
    if len(unique_rows) != 119:
        raise RuntimeError(f"independent lock binding denominator: {len(unique_rows)} != 119")
    for index, row in enumerate(unique_rows, start=1):
        verify_locked_descriptor(row, f"locked artifact {index}/119")

    canonical: list[dict[str, Any]] = []
    trees: list[dict[str, Any]] = []
    for paper in lock["papers"]:
        paper_id = paper["paper_id"]
        for row in paper["protected_canonical_files"]:
            canonical.append(
                {"paper_id": paper_id, "artifact": verify_locked_descriptor(row, f"{paper_id} canonical")}
            )
        for tree in paper["science_trees"]:
            digest, file_count = science_tree_digest(ROOT / tree["path"])
            if digest != tree["sha256"] or file_count != len(tree["files"]):
                raise RuntimeError(f"{paper_id} science-tree digest/count drift: {tree['path']}")
            trees.append(
                {
                    "paper_id": paper_id,
                    "path": tree["path"],
                    "sha256": digest,
                    "file_count": file_count,
                }
            )
    if len(trees) != 15:
        raise RuntimeError(f"independent science-tree denominator: {len(trees)} != 15")
    return {
        "locked_file_bindings_replayed": len(unique_rows),
        "protected_canonical_files": canonical,
        "science_trees": trees,
        "read_only_files": [
            exact_artifact(ROOT / name, f"read-only boundary {name}") for name in READONLY_FILES
        ],
        "changed_protected_files": 0,
    }


def independent_aggregate(papers: list[dict[str, Any]]) -> dict[str, Any]:
    claim_counts: Counter[str] = Counter()
    component_counts: Counter[str] = Counter()
    evr_counts: Counter[str] = Counter()
    for paper in papers:
        denominators = paper["denominators"]
        claim_counts.update(denominators["claim_verdict_counts"])
        if denominators["component_verdict_counts"] is not None:
            component_counts.update(denominators["component_verdict_counts"])
        evr_counts.update(denominators["evr_verdict_counts"])
    aggregate = {
        "papers_total": len(papers),
        "papers_passed": 0,
        "papers_failed": len(papers),
        "references": sum(row["denominators"]["references"] for row in papers),
        "citation_contexts": sum(row["denominators"]["citation_contexts"] for row in papers),
        "registered_claims": sum(row["denominators"]["registered_claims"] for row in papers),
        "evidence_rows": sum(row["denominators"]["evidence_rows"] for row in papers),
        "dependency_components_p29_to_p32": sum(
            row["denominators"]["dependency_components"] or 0 for row in papers
        ),
        "claim_verdict_counts": dict(sorted(claim_counts.items())),
        "component_verdict_counts_p29_to_p32": dict(sorted(component_counts.items())),
        "evr_verdict_counts": dict(sorted(evr_counts.items())),
    }
    fixed = {
        "papers_total": 5,
        "papers_passed": 0,
        "papers_failed": 5,
        "references": 126,
        "citation_contexts": 156,
        "registered_claims": 797,
        "claim_verdict_counts": EXPECTED_CLAIM_VERDICT_COUNTS,
    }
    for key, expected in fixed.items():
        if aggregate[key] != expected:
            raise RuntimeError(f"independent aggregate {key}: {aggregate[key]} != {expected}")
    return aggregate


def validate_final_independent_review(independent_path: Path) -> dict[str, Any]:
    if independent_path != FINAL_INDEPENDENT_REVIEW_PATH:
        raise RuntimeError(
            f"independent review must be {FINAL_INDEPENDENT_REVIEW_PATH.name}"
        )
    independent_path = require_workspace_file(independent_path, "final independent replay")
    descriptor = artifact(independent_path)
    if descriptor["sha256"] != EXPECTED_FINAL_INDEPENDENT_REVIEW_SHA:
        raise RuntimeError(
            "final independent-review SHA is not the frozen expected digest: "
            f"{descriptor['sha256']} != {EXPECTED_FINAL_INDEPENDENT_REVIEW_SHA}"
        )
    if sha_bytes(LOCK_PATH.read_bytes()) != EXPECTED_LOCK_SHA:
        raise RuntimeError("input lock drift before independent-review replay")
    if sha_bytes(AUTH_PATH.read_bytes()) != EXPECTED_AUTH_SHA:
        raise RuntimeError("authorization receipt drift before independent-review replay")
    independent = load_json(independent_path)
    if set(independent) != EXPECTED_FINAL_INDEPENDENT_REVIEW_KEYS:
        raise RuntimeError(
            "independent review top-level keys are not exact: "
            f"{sorted(independent)} != {sorted(EXPECTED_FINAL_INDEPENDENT_REVIEW_KEYS)}"
        )
    if independent.get("schema_version") != EXPECTED_FINAL_INDEPENDENT_REVIEW_SCHEMA:
        raise RuntimeError("independent review schema is not exact")
    status = independent.get("status")
    if status != EXPECTED_FINAL_INDEPENDENT_REVIEW_STATUS:
        raise RuntimeError(
            "independent review status is not exact PASS: "
            f"{status!r} != {EXPECTED_FINAL_INDEPENDENT_REVIEW_STATUS!r}"
        )
    if independent.get("scientific_integrity_batch_verdict") != "FAIL_0_OF_5_ELIGIBLE_FOR_STAGE5":
        raise RuntimeError("independent review does not preserve the five-paper fail-closed verdict")
    required_descriptors = {
        "validator": artifact(VALIDATOR_PATH),
        "authority": artifact(AUTH_PATH),
        "input_lock": artifact(LOCK_PATH),
    }
    for key, expected in required_descriptors.items():
        if independent.get(key) != expected:
            raise RuntimeError(f"independent review {key} descriptor does not match current bytes")
    expected_papers = independent_paper_rows()
    if independent.get("papers") != expected_papers:
        raise RuntimeError("independent review paper descriptors/denominators do not replay exactly")
    expected_aggregate = independent_aggregate(expected_papers)
    if independent.get("aggregate") != expected_aggregate:
        raise RuntimeError("independent review aggregate does not replay exactly")
    lock = load_json(LOCK_PATH)
    if lock.get("aggregate_route_boundary") != EXPECTED_ROUTE_BOUNDARY:
        raise RuntimeError("input-lock Route boundary drift")
    if independent.get("route_boundary") != EXPECTED_ROUTE_BOUNDARY:
        raise RuntimeError("independent review Route boundary is not exact")
    expected_protected = protected_boundary_replay()
    if independent.get("protected_boundary_replay") != expected_protected:
        raise RuntimeError("independent review protected-boundary replay does not match current bytes")
    expected_root_replay = {
        "checks_passed": EXPECTED_VALIDATOR_CHECKS,
        "terminal_marker": "ROUND10_STAGE4_5_ROUND2_AUDIT_PASS",
        "findings": [],
    }
    if independent.get("root_replay") != expected_root_replay:
        raise RuntimeError("independent review root-replay summary is not exact")
    if independent.get("findings") != []:
        raise RuntimeError("independent review contains unresolved package-coherence findings")
    return independent


def import_block_parser():
    path = ARS_ROOT / "scripts/_block_parser.py"
    spec = importlib.util.spec_from_file_location("ars_block_parser_round10_closeout", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load ARS block parser")
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def utf8_offset(text: str, character_offset: int) -> int:
    return len(text[:character_offset].encode("utf-8"))


def block_targets(cfg: dict[str, Any], parser: Any) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    notes = ROOT / "papers" / cfg["slug"] / "notes"
    draft_path = notes / cfg["draft"]
    manifest_path = notes / cfg["block_manifest"]
    raw = draft_path.read_bytes()
    text = raw.decode("utf-8")
    parsed = parser.parse_document(text)
    by_id = parsed.block_by_id()
    manifest = load_json(manifest_path)
    manifest_by_id = {row["block_id"]: row for row in manifest["blocks"]}
    if len(cfg["targets"]) != len(set(cfg["targets"])):
        raise RuntimeError(f"{cfg['slug']} has duplicate correction targets")
    targets: list[dict[str, Any]] = []
    previous_marker_start = -1
    for block_id in cfg["targets"]:
        block = by_id[block_id]
        if block.marker_span[0] <= previous_marker_start:
            raise RuntimeError(f"{cfg['slug']} correction targets are not in physical draft order")
        previous_marker_start = block.marker_span[0]
        manifest_row = manifest_by_id[block_id]
        normalized_raw = block.normalized_text.encode("utf-8")
        normalized_sha = sha_bytes(normalized_raw)
        if normalized_sha[:12] != block.norm_hash or manifest_row["old_hash"] != block.norm_hash:
            raise RuntimeError(f"{cfg['slug']} {block_id} block-manifest mismatch")
        marker_start = block.marker_span[0]
        full_end = block.span[1]
        marked_raw = text[marker_start:full_end].encode("utf-8")
        content_raw = text[block.span[0]:block.span[1]].encode("utf-8")
        start_line = text[: block.span[0]].count("\n") + 1
        end_line = text[: block.span[1]].count("\n")
        finding_ids = cfg["target_issue"].get(block_id, cfg["default_issue"])
        if not finding_ids:
            raise RuntimeError(f"{cfg['slug']} {block_id} has no explicit blocking finding")
        targets.append(
            {
                "block_id": block_id,
                "finding_ids": finding_ids,
                "allowed_operations": ["replace_block"],
                "hash_semantics": (
                    "UTF-8; CRLF/LF normalized to LF; marker excluded; leading/trailing blank "
                    "lines stripped; intra-line whitespace preserved"
                ),
                "expected_current_normalized_content_sha256": normalized_sha,
                "expected_current_normalized_content_bytes": len(normalized_raw),
                "manifest_old_hash_prefix_12": block.norm_hash,
                "expected_current_marked_block_sha256": sha_bytes(marked_raw),
                "expected_current_marked_block_bytes": len(marked_raw),
                "expected_current_raw_content_sha256": sha_bytes(content_raw),
                "expected_current_raw_content_bytes": len(content_raw),
                "content_utf8_span_end_exclusive": {
                    "start": utf8_offset(text, block.span[0]),
                    "end": utf8_offset(text, block.span[1]),
                },
                "line_span_1_based_inclusive": {"start": start_line, "end": end_line},
            }
        )
    return artifact(draft_path), artifact(manifest_path), targets


def extract_bib_entry(raw: bytes, key: str) -> bytes:
    match = re.search(rb"@[A-Za-z]+\s*\{" + re.escape(key.encode("ascii")) + rb"\s*,", raw, re.I)
    if match is None:
        raise RuntimeError(f"BibTeX key missing: {key}")
    depth = 0
    opened = False
    for index in range(match.start(), len(raw)):
        if raw[index] == ord("{"):
            depth += 1
            opened = True
        elif raw[index] == ord("}"):
            depth -= 1
            if opened and depth == 0:
                return raw[match.start() : index + 1]
    raise RuntimeError(f"unterminated BibTeX entry: {key}")


def count_claim_verdicts(evidence: list[dict[str, Any]]) -> dict[str, int]:
    by_claim: dict[str, set[str]] = defaultdict(set)
    for row in evidence:
        by_claim[row["claim"]["claim_id"]].add(row["verdict"])
    mixed = {key: values for key, values in by_claim.items() if len(values) != 1}
    if mixed:
        raise RuntimeError(f"mixed shared-EVR verdicts: {mixed}")
    return dict(sorted(Counter(next(iter(values)) for values in by_claim.values()).items()))


def verdict_triplet(counts: dict[str, int]) -> str:
    return (
        f"{counts.get('VERIFIED', 0)}/"
        f"{counts.get('UNVERIFIABLE', 0)}/"
        f"{counts.get('MAJOR_DISTORTION', 0)}"
    )


def claim_verdict_map(evidence: list[dict[str, Any]]) -> dict[str, str]:
    by_claim: dict[str, set[str]] = defaultdict(set)
    for row in evidence:
        by_claim[row["claim"]["claim_id"]].add(row["verdict"])
    mixed = {key: values for key, values in by_claim.items() if len(values) != 1}
    if mixed:
        raise RuntimeError(f"mixed shared-EVR verdicts: {mixed}")
    return {key: next(iter(values)) for key, values in by_claim.items()}


def validate_semantic_correction_scope(
    paper_id: str,
    cfg: dict[str, Any],
    proposal: Path,
) -> None:
    """Fail closed on the two packages whose semantic attribution was rebuilt."""
    if paper_id not in {"P30", "P31"}:
        return
    notes = ROOT / "papers" / cfg["slug"] / "notes"
    registry = load_json(notes / "stage4_5_round2_claim_registry.json")
    evidence = load_json(notes / "stage4_5_round2_evidence_rows.json")
    verdicts = claim_verdict_map(evidence)
    nonverified_ids = {claim_id for claim_id, verdict in verdicts.items() if verdict != "VERIFIED"}
    registry_by_id = {row["claim_id"]: row for row in registry["claims"]}
    if not nonverified_ids <= registry_by_id.keys():
        raise RuntimeError(f"{paper_id} non-VERIFIED evidence claim is absent from registry")
    expected_anchor_map = EXPECTED_NONVERIFIED_CLAIM_ANCHORS[paper_id]
    if nonverified_ids != set(expected_anchor_map):
        raise RuntimeError(f"{paper_id} non-VERIFIED claim IDs differ from the frozen exact map")
    for claim_id, expected_anchor in expected_anchor_map.items():
        observed_anchors = registry_by_id[claim_id].get("writer_anchors", [])
        if observed_anchors != [expected_anchor]:
            raise RuntimeError(
                f"{paper_id} {claim_id} writer anchor: {observed_anchors} != {[expected_anchor]}"
            )
    nonverified_anchors = set(expected_anchor_map.values())
    if nonverified_anchors != set(cfg["targets"]):
        raise RuntimeError(
            f"{paper_id} correction targets do not equal non-VERIFIED writer anchors: "
            f"{sorted(nonverified_anchors)} != {sorted(cfg['targets'])}"
        )

    request_findings = {
        finding_id
        for block_id in cfg["targets"]
        for finding_id in cfg["target_issue"].get(block_id, cfg["default_issue"])
    }
    proposal_json = load_json(proposal)
    proposal_rows = proposal_json.get("blocking_findings", [])
    proposal_findings = {row.get("finding_id") for row in proposal_rows}
    if (
        proposal_findings != request_findings
        or len(proposal_rows) != cfg["issue_count"]
        or len(proposal_findings) != len(proposal_rows)
    ):
        raise RuntimeError(
            f"{paper_id} controlling proposal finding set/count does not match request scope"
        )
    proposal_claims = {
        claim_id for row in proposal_rows for claim_id in row.get("affected_claim_ids", [])
    }
    if proposal_claims != nonverified_ids:
        raise RuntimeError(
            f"{paper_id} controlling proposal claims do not equal non-VERIFIED claim set"
        )

    claims_by_finding = {
        row["finding_id"]: set(row.get("affected_claim_ids", [])) for row in proposal_rows
    }
    flattened_proposal_claims = [
        claim_id for row in proposal_rows for claim_id in row.get("affected_claim_ids", [])
    ]
    if len(flattened_proposal_claims) != len(set(flattened_proposal_claims)):
        raise RuntimeError(f"{paper_id} proposal repeats a claim across blocking findings")
    expected_claims_by_finding: dict[str, set[str]] = defaultdict(set)
    for claim_id, block_id in expected_anchor_map.items():
        for finding_id in cfg["target_issue"].get(block_id, cfg["default_issue"]):
            expected_claims_by_finding[finding_id].add(claim_id)
    if claims_by_finding != dict(expected_claims_by_finding):
        raise RuntimeError(
            f"{paper_id} proposal claim-to-finding mapping is not exact: "
            f"{claims_by_finding} != {dict(expected_claims_by_finding)}"
        )


def paper_summary(paper_id: str, cfg: dict[str, Any]) -> dict[str, Any]:
    notes = ROOT / "papers" / cfg["slug"] / "notes"
    registry_path = notes / "stage4_5_round2_claim_registry.json"
    evidence_path = notes / "stage4_5_round2_evidence_rows.json"
    integrity_path = notes / "stage4_5_round2_integrity_report.json"
    compliance_path = notes / "stage4_5_round2_compliance_report.json"
    registry = load_json(registry_path)
    evidence = load_json(evidence_path)
    report = load_json(integrity_path)
    verdict = report.get("verdict", report.get("integrity_verdict"))
    if not str(verdict).startswith("FAIL") or report.get("stage5_started") is not False:
        raise RuntimeError(f"{paper_id} is not a fail-closed Stage-4.5 package")
    manifest_name = (
        "stage4_5_round2_package_manifest.json"
        if (notes / "stage4_5_round2_package_manifest.json").exists()
        else "stage4_5_round2_output_manifest.json"
    )
    phase_a = report["phases"]["A_references"]
    phase_b = report["phases"]["B_citation_contexts"]
    phase_d = report["phases"]["D_originality"]
    body_success = phase_d.get("body_successful", int(str(phase_d.get("body", "0/0")).split("/")[0]))
    body_total = phase_d.get("body_denominator", int(str(phase_d.get("body", "0/0")).split("/")[-1]))
    changed_success = phase_d.get("changed_successful", int(str(phase_d.get("changed_body", "0/0")).split("/")[0]))
    changed_total = phase_d.get("changed_denominator", int(str(phase_d.get("changed_body", "0/0")).split("/")[-1]))
    observed_originality = {
        "body": [body_success, body_total],
        "changed": [changed_success, changed_total],
    }
    if observed_originality != EXPECTED_PAPER_ORIGINALITY[paper_id]:
        raise RuntimeError(
            f"{paper_id} originality denominators: {observed_originality} != "
            f"{EXPECTED_PAPER_ORIGINALITY[paper_id]}"
        )
    evidence_counts = dict(sorted(Counter(row["verdict"] for row in evidence).items()))
    claim_counts = count_claim_verdicts(evidence)
    if claim_counts != EXPECTED_PAPER_CLAIM_VERDICTS[paper_id]:
        raise RuntimeError(
            f"{paper_id} claim verdict counts: {claim_counts} != "
            f"{EXPECTED_PAPER_CLAIM_VERDICTS[paper_id]}"
        )
    summary: dict[str, Any] = {
        "paper_id": paper_id,
        "paper_number": cfg["number"],
        "title": cfg["title"],
        "verdict": verdict,
        "stage5_started": False,
        "references": phase_a["registered"],
        "citation_contexts": phase_b["registered"],
        "registered_claims": len(registry["claims"]),
        "claim_overall_verdict_counts": claim_counts,
        "evidence_rows": len(evidence),
        "shared_evr_verdict_counts": evidence_counts,
        "originality": {
            "successful_body_paragraphs": body_success,
            "body_paragraphs": body_total,
            "successful_changed_paragraphs": changed_success,
            "changed_paragraphs": changed_total,
        },
        "draft": artifact(notes / cfg["draft"]),
        "registry": artifact(registry_path),
        "evidence_rows_artifact": artifact(evidence_path),
        "integrity_report": artifact(integrity_path),
        "compliance_report": artifact(compliance_path),
        "manifest": artifact(notes / manifest_name),
    }
    catalog_path = notes / "stage4_5_round2_local_claim_dependency_catalog.json"
    if catalog_path.exists():
        catalog = load_json(catalog_path)
        if "dependency_count" in catalog:
            component_count = catalog["dependency_count"]
        else:
            component_count = catalog["dependency_component_count"]
        summary["dependency_catalog"] = artifact(catalog_path)
        summary["cataloged_components"] = component_count
        summary["component_semantic_verdict_counts"] = catalog["component_semantic_verdict_counts"]
    return summary


def normalized_component_counts(paper_summaries: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for summary in paper_summaries:
        for value, number in summary.get("component_semantic_verdict_counts", {}).items():
            if value == "MAJOR_DISTORTION" or value.startswith("CONTRADICT") or value.startswith("MAJOR_DISTORTION"):
                counts["MAJOR_DISTORTION"] += number
            elif value.startswith("UNVERIFIABLE"):
                counts["UNVERIFIABLE"] += number
            elif value == "VERIFIED" or value.startswith("VERIFIED") or value.startswith("EXACT_SURFACE_PRESENT"):
                counts["VERIFIED"] += number
            else:
                raise RuntimeError(f"unknown component-semantic verdict: {value}")
    return dict(sorted(counts.items()))


def aggregate_summary(summaries: list[dict[str, Any]]) -> dict[str, Any]:
    aggregate_claim_counts: Counter[str] = Counter()
    aggregate_evr_counts: Counter[str] = Counter()
    for summary in summaries:
        aggregate_claim_counts.update(summary["claim_overall_verdict_counts"])
        aggregate_evr_counts.update(summary["shared_evr_verdict_counts"])
    aggregate = {
        "papers_passed": 0,
        "papers_failed": 5,
        "papers_total": 5,
        "references": sum(row["references"] for row in summaries),
        "citation_contexts": sum(row["citation_contexts"] for row in summaries),
        "registered_claims": sum(row["registered_claims"] for row in summaries),
        "claim_overall_verdict_counts": dict(sorted(aggregate_claim_counts.items())),
        "evidence_rows": sum(row["evidence_rows"] for row in summaries),
        "shared_evr_verdict_counts": dict(sorted(aggregate_evr_counts.items())),
        "cataloged_components_p29_to_p32": sum(
            row.get("cataloged_components", 0) for row in summaries
        ),
        "normalized_component_semantic_verdict_counts_p29_to_p32": normalized_component_counts(
            summaries
        ),
        "originality_successful_body_paragraphs": sum(
            row["originality"]["successful_body_paragraphs"] for row in summaries
        ),
        "originality_body_paragraphs": sum(
            row["originality"]["body_paragraphs"] for row in summaries
        ),
        "changed_paragraphs_successful": sum(
            row["originality"]["successful_changed_paragraphs"] for row in summaries
        ),
        "changed_paragraphs_total": sum(
            row["originality"]["changed_paragraphs"] for row in summaries
        ),
    }
    expected = {
        "references": 126,
        "citation_contexts": 156,
        "registered_claims": 797,
        "originality_successful_body_paragraphs": 269,
        "originality_body_paragraphs": 371,
        "changed_paragraphs_successful": 206,
        "changed_paragraphs_total": 206,
    }
    for key, value in expected.items():
        if aggregate[key] != value:
            raise RuntimeError(f"aggregate {key}: {aggregate[key]} != {value}")
    if aggregate["claim_overall_verdict_counts"] != EXPECTED_CLAIM_VERDICT_COUNTS:
        raise RuntimeError(
            "aggregate claim verdicts: "
            f"{aggregate['claim_overall_verdict_counts']} != {EXPECTED_CLAIM_VERDICT_COUNTS}"
        )
    return aggregate


def build_request(stamp: str) -> dict[str, Any]:
    parser = import_block_parser()
    papers: list[dict[str, Any]] = []
    total_targets = 0
    for paper_id, cfg in PAPERS.items():
        draft, block_manifest, targets = block_targets(cfg, parser)
        total_targets += len(targets)
        notes = ROOT / "papers" / cfg["slug"] / "notes"
        proposal_candidates = [
            notes / "stage4_5_round2_correction_list.json",
            notes / "stage4_5_round2_correction_proposal.json",
            notes / "stage4_5_round2_integrity_correction_list.json",
        ]
        proposal = next(path for path in proposal_candidates if path.exists())
        validate_semantic_correction_scope(paper_id, cfg, proposal)
        papers.append(
            {
                "paper_id": paper_id,
                "paper_number": cfg["number"],
                "base_draft": draft,
                "base_block_manifest": block_manifest,
                "stage4_5_blocker_source": artifact(proposal),
                "issue_count": cfg["issue_count"],
                "chosen_branch": "CONSERVATIVE_NARROWING_NO_NEW_SCIENTIFIC_EXECUTION",
                "strategy": cfg["strategy"],
                "proposed_successor_draft": f"papers/{cfg['slug']}/notes/{cfg['successor']}",
                "targets": targets,
                "target_count": len(targets),
            }
        )
    if total_targets != 66:
        raise RuntimeError(f"expected 66 replace_block targets, got {total_targets}")

    p30_notes = ROOT / "papers" / PAPERS["P30"]["slug"] / "notes"
    bib_path = p30_notes / "stage4_prime_references_round2.bib"
    bib_raw = bib_path.read_bytes()
    entry = extract_bib_entry(bib_raw, "P30-S02")
    if b"10.1063/1.457669" not in entry:
        raise RuntimeError("P30-S02 current companion DOI surface absent")
    return {
        "schema_version": "round10-stage4.5-round2-exact-correction-authorization-request/1.0",
        "generated_at_utc": stamp,
        "status": "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION_NOT_AUTHORIZED_NOT_APPLIED",
        "current_authority": artifact(AUTH_PATH),
        "current_input_lock": artifact(LOCK_PATH),
        "decision_rule": (
            "A short unqualified author reply of 确认 after presentation of this request's exact "
            "SHA-256 authorizes only the operations listed here."
        ),
        "selected_execution_branch": "FAST_CONSERVATIVE_NARROWING",
        "aggregate": {
            "blocking_issue_count": sum(cfg["issue_count"] for cfg in PAPERS.values()),
            "replace_block_targets": total_targets,
            "unique_replace_block_targets_within_each_draft": total_targets,
            "bibliography_entry_replacements": 1,
            "new_scientific_executions": 0,
            "canonical_promotions": 0,
        },
        "papers": papers,
        "bibliography_operation": {
            "paper_id": "P30",
            "path": bib_path.relative_to(ROOT).as_posix(),
            "base_artifact": artifact(bib_path),
            "entry_key": "P30-S02",
            "allowed_operation": "replace_bib_entry_in_successor_only",
            "expected_current_entry_sha256": sha_bytes(entry),
            "expected_current_entry_bytes": len(entry),
            "exact_field_change": {
                "field": "note",
                "old_companion_doi": "10.1063/1.457669",
                "new_companion_doi": "10.1063/1.457672",
            },
            "preserve_relations": [
                "P30-C01 update-to P30-S01 (10.1063/1.456017)",
                "P30-C02 update-to P30-S03 (10.1063/1.456019)",
            ],
            "proposed_successor": (
                "papers/30-three-disk-nonconstant-roof-determinant/notes/"
                "stage4_prime_references_round3.bib"
            ),
        },
        "allowed_derived_operations": {
            "revision": (
                "Emit only the named successor drafts/Bib and their exact patch, block-manifest, "
                "apply-report, traceability, and isolated-build receipts under each paper's notes directory."
            ),
            "matrices": [
                "P30: stage4_prime_claim_passage_matrix_round3.json",
                "P31: stage4_prime_method_passage_matrix_round3.json",
                "P32: stage4_prime_claim_passage_matrix_round4.json",
                "P33: stage4_prime_claim_passage_matrix_round3.json",
            ],
            "versioned_reader_manifests": [
                "P31: stage4_prime_reader_artifact_manifest_round3.json",
            ],
            "fresh_integrity_audit": (
                "After correction, generate a new Stage 4.5 Round 3 audit package for P29--P33 "
                "and stop at its mandatory checkpoint."
            ),
            "isolated_preview_build": True,
        },
        "mandatory_stop_conditions": [
            "Any base-draft, block-manifest, normalized-block, marked-block, Bib, or blocker-source hash mismatch.",
            "Any need to edit a block or bibliography entry not listed in this request.",
            "Any scientific value/result change, new execution, claim strengthening, Route change, or initial-system change.",
            "Any request to overwrite the locked Round-2 input rather than emit a named successor.",
            "Any failed official validator, independent replay, or isolated build.",
        ],
        "explicitly_forbidden": {
            "canonical_or_submission_promotion": True,
            "code_experiment_or_result_refresh": True,
            "route_a_or_route_b_mutation": True,
            "initial_dynamical_system_mutation": True,
            "readme_or_pipeline_status_mutation": True,
            "git_commit_push_or_sync": True,
            "stage5_or_stage6_entry": True,
            "unlisted_collateral_edit": True,
            "claim_strengthening": True,
            "invented_source_passage_or_user_metadata": True,
        },
        "authorization_effect_if_confirmed": (
            "Authorize the 66 exact replace_block operations, the one exact P30-S02 successor-Bib "
            "entry correction, the named notes-side derived outputs, isolated previews, and a fresh "
            "Stage 4.5 Round 3 audit; nothing else."
        ),
    }


def build_closeout(stamp: str, independent_path: Path) -> None:
    if sha_bytes(LOCK_PATH.read_bytes()) != EXPECTED_LOCK_SHA:
        raise RuntimeError("input lock drift")
    if sha_bytes(AUTH_PATH.read_bytes()) != EXPECTED_AUTH_SHA:
        raise RuntimeError("authorization receipt drift")
    validate_final_independent_review(independent_path)

    root_replay = replay_root_validator()
    request = build_request(stamp)
    summaries = [paper_summary(paper_id, cfg) for paper_id, cfg in PAPERS.items()]
    request_raw = json_bytes(request)
    request_desc = {
        "path": REQUEST_JSON.relative_to(ROOT).as_posix(),
        "sha256": sha_bytes(request_raw),
        "bytes": len(request_raw),
    }
    request_md = f"""# Round 10 Papers 29--33 — exact correction authorization request

Status: **AWAITING EXPLICIT AUTHOR CONFIRMATION; nothing has been applied.**

Machine request: `{request_desc['path']}`  
SHA-256: `{request_desc['sha256']}`  
Bytes: `{request_desc['bytes']}`

The selected fast branch is conservative: where a raw source/activity carrier is absent, narrow or
remove only the unsupported component.  It does not invent a passage, run a new scientific
experiment, or strengthen a claim.

| Paper | Blocking issues | Exact `replace_block` targets | Additional operation |
|---|---:|---:|---|
| P29 | 2 | 20 | none |
| P30 | 6 | 11 | one successor-only `P30-S02` Bib entry correction |
| P31 | 4 | 8 | none |
| P32 | 3 | 7 | none |
| P33 | 2 | 20 | none; remove evidentiary interpretation of same-lineage 14/14 |

Total: **17 blocking issues, 66 exact block replacements, one exact Bib-entry correction**.  Every
target's current draft hash, normalized full-content SHA-256, marked-block SHA-256, byte span, and
allowed operation are in the machine request.  A mismatch or any unlisted target stops execution.

If confirmed, the work emits successor notes-side drafts and derived audit artifacts, performs
isolated preview builds, then runs a fresh Stage 4.5 Round 3 and stops.  Canonical files, scientific
results, the two route evaluators, initial dynamical systems, README/status files, Git, Stage 5, and
Stage 6 remain outside scope.

## Confirmation

Per the author's standing preference for short confirmations, the next unqualified reply
**`确认`** binds the exact machine-request SHA-256 above and authorizes only that request.
"""
    request_md_raw = request_md.encode("utf-8")
    aggregate = aggregate_summary(summaries)

    final_audit = {
        "schema_version": "round10-stage4.5-round2-batch-final-audit/1.0",
        "generated_at_utc": stamp,
        "status": "PASS_AUDIT_PACKAGE_COHERENT_WITH_FIVE_BLOCKING_FAIL_VERDICTS",
        "scientific_integrity_batch_verdict": "FAIL_0_OF_5_ELIGIBLE_FOR_STAGE5",
        "authority": artifact(AUTH_PATH),
        "input_lock": artifact(LOCK_PATH),
        "independent_review": artifact(independent_path),
        "root_replay": {
            **root_replay,
            "semantics": "The package replay passes; all five scientific-integrity dispositions remain FAIL.",
        },
        "aggregate": aggregate,
        "papers": summaries,
        "route_boundary": {
            "formal_route_a_tuples": "0/5",
            "positive_arithmetic_A2": "0/5",
            "A3": "0/5",
            "A4": "0/5",
            "route_b_invocations": "0/5",
        },
        "frozen_initial_systems": {
            "P29": "unit-speed level-(3) Gaussian Bianchi geodesic-flow owner proposal",
            "P30": "physical no-eclipse equilateral three-disk flow at d=6a, with separate unit-roof symbolic calibrator",
            "P31": "positive time change of the Gamma_0(11) geodesic flow",
            "P32": "pure genus-two homology-cover tower with fixed 1/N time and 1/N^3 log-product normalization",
            "P33": "frozen Bolza b=1/2 magnetic precursor with genus-two geodesic control",
        },
        "read_only_boundaries": {name: sha_bytes((ROOT / name).read_bytes()) for name in READONLY_FILES},
        "correction_authorization_request": request_desc,
        "correction_authorization_request_human": pending_artifact(REQUEST_MD, request_md_raw),
        "stage5_started": False,
        "stage5_authorized": False,
        "canonical_promotion_performed": False,
        "git_operation_performed": False,
    }
    rows = {row["paper_id"]: row for row in summaries}
    report_md = f"""# Round 10 Papers 29--33 — Stage 4.5 Round 2 final-integrity report

Date: **{stamp[:10]}**  
ARS mode: **Stage 4.5 / Mode 2 final verification**  
Batch scientific-integrity verdict: **0/5 PASS; five fail-closed correction checkpoints**  
Audit-package replay: **PASS (89/89 checks)**  
Stage 5: **not started and not authorized**

## Outcome

The audit packages are structurally coherent and independently replayable, but none of the five
papers is eligible to enter Stage 5.  `PASS` here applies only to the audit machinery; the controlling
per-paper decisions remain `FAIL` or `FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED`.  These findings do not
say the underlying mathematics is false.  They identify unsupported, contradictory, or
same-lineage-evidence surfaces that must be corrected first.

| Paper | Refs / contexts | Claims (V/U/MD) | Evidence rows (V/U/MD) | Main blocker | Verdict |
|---|---:|---:|---:|---|---|
| P29 | {rows['P29']['references']} / {rows['P29']['citation_contexts']} | {verdict_triplet(rows['P29']['claim_overall_verdict_counts'])} | {verdict_triplet(rows['P29']['shared_evr_verdict_counts'])} | translated status contradiction; 20 compound claims with missing raw components | FAIL |
| P30 | {rows['P30']['references']} / {rows['P30']['citation_contexts']} | {verdict_triplet(rows['P30']['claim_overall_verdict_counts'])} | {verdict_triplet(rows['P30']['shared_evr_verdict_counts'])} | wrong correction relation; false review-role enumeration; Livsic passage; stale search/rerun status; AI metadata | FAIL |
| P31 | {rows['P31']['references']} / {rows['P31']['citation_contexts']} | {verdict_triplet(rows['P31']['claim_overall_verdict_counts'])} | {verdict_triplet(rows['P31']['shared_evr_verdict_counts'])} | P31-S23/S24 passages; overbroad literature negative; stale reader manifest; AI metadata | FAIL |
| P32 | {rows['P32']['references']} / {rows['P32']['citation_contexts']} | {verdict_triplet(rows['P32']['claim_overall_verdict_counts'])} | {verdict_triplet(rows['P32']['shared_evr_verdict_counts'])} | translated status; five local raw gaps; CW01--CW04 excerpt binding | FAIL |
| P33 | {rows['P33']['references']} / {rows['P33']['citation_contexts']} | {verdict_triplet(rows['P33']['claim_overall_verdict_counts'])} | {verdict_triplet(rows['P33']['shared_evr_verdict_counts'])} | 48 passage gaps; same-lineage synthetic oracle/harness | FAIL |

Totals: **{aggregate['references']} references, {aggregate['citation_contexts']} citation contexts,
{aggregate['registered_claims']} registered claims, and {aggregate['evidence_rows']:,} shared
evidence rows**.  Claim-level outcomes are
**{aggregate['claim_overall_verdict_counts'].get('VERIFIED', 0)} VERIFIED /
{aggregate['claim_overall_verdict_counts'].get('UNVERIFIABLE', 0)} UNVERIFIABLE /
{aggregate['claim_overall_verdict_counts'].get('MAJOR_DISTORTION', 0)} MAJOR_DISTORTION**;
shared EVRs are **{verdict_triplet(aggregate['shared_evr_verdict_counts'])}**.  For P29--P32,
{aggregate['cataloged_components_p29_to_p32']} dependency components were independently cataloged:
**{verdict_triplet(aggregate['normalized_component_semantic_verdict_counts_p29_to_p32'])}**.
Component, claim, and shared-EVR denominators are deliberately distinct:
Schema-5 propagates a compound claim's weakest verdict to every row sharing its claim ID without
reclassifying every supported component as defective.

The originality pass records
**{aggregate['originality_successful_body_paragraphs']}/{aggregate['originality_body_paragraphs']}**
successful body-paragraph searches and
**{aggregate['changed_paragraphs_successful']}/{aggregate['changed_paragraphs_total']}** changed
paragraphs covered.  These are audit/bookkeeping totals, not pooled scientific samples or new
experiments.  Preview-page and E6-operation totals are intentionally omitted from this batch
summary because they are not scientific outcomes and are already preserved in their per-paper receipts.

## Paper-level correction direction

- **P29:** correct B0006's translated locator-status sentence; conservatively narrow the unsupported
  components in the 20 affected compound claims.  The earlier fixed-preamble persistence defect is
  corrected in the audit artifacts; no claim was promoted merely because an audit report described it.
- **P30:** bind P30-S02 to correction DOI `10.1063/1.457672`, preserve the separate C01/C02
  relations, correct B0061's role enumeration against the actual review records, narrow the
  unsupported Livsic attribution in B0004/B0057/B0096, reconcile B0108 with the already frozen
  dated search replay, narrow B0124 to locked AI metadata, and correct B0125's now-false statement
  that this exact Round-3 draft has not received Stage 4.5 replay.
- **P31:** treat P31-S23/P31-S24 as metadata-only wherever no original passage is bound, narrowing
  four affected prose blocks; narrow the overbroad literature-negative claim to the admitted
  project-use boundary; correct B0079/B0105's reliance on a stale reader manifest; and narrow the
  AI-history disclosure to locked metadata.
- **P32:** correct B0007's translated status, keep CW01--CW04 explicitly unverifiable, and narrow
  the five local compound claims whose raw activity/author/provenance component is absent.
- **P33:** narrow all 48 source-dependent contexts that lack passage evidence.  For Mode 4, take the
  no-new-execution branch and remove evidentiary interpretation of the same-lineage 14/14 synthetic
  harness while preserving it as a diagnostic record.

The exact next-scope request is [{REQUEST_MD.name}]({REQUEST_MD.name}); its machine form binds 66
normalized blocks plus the single P30-S02 Bib entry by full SHA-256.  No repair has yet been applied.

## Route-A correspondence and frozen systems

Stage 4.5 is an integrity gate, not a Route-A coordinate.  Under
[`skills/route-a-evaluator.md`](skills/route-a-evaluator.md), formal Route-A tuples remain **0/5**,
positive-arithmetic A2 remains **0/5**, and A3/A4 remain **0/5**.  Under
[`skills/route-b-evaluator.md`](skills/route-b-evaluator.md), Route-B invocations remain **0/5**.

The five initial systems remain frozen: the level-(3) Gaussian Bianchi flow; the physical
three-disk flow at `d=6a` plus its separate symbolic calibrator; the positive Level-11 time change;
the pure genus-two homology-cover tower; and the Bolza `b=1/2` magnetic precursor with geodesic
control.  This audit makes no new dynamical-system test and changes no initial restriction.

## Independent replay and boundaries

[`tools/audit_round10_stage4_5_round2.rb`](tools/audit_round10_stage4_5_round2.rb) recomputed the
119 locked file bindings, 15 science-tree hashes, all registered claim spans, official coverage,
evidence and Schema-12 checks, catalog-to-EVR joins, raw UTF-8 spans, transitive lock chains, P30's
fresh authorized Crossref provenance, per-paper FAIL blockers, Route state, and Stage-5 closure.

```text
Checks passed: 89
ROUND10_STAGE4_5_ROUND2_AUDIT_PASS
```

The machine-readable batch audit is `{FINAL_AUDIT_JSON.name}`.  Manuscripts, bibliographies,
canonical PDFs, code/experiments/results, Route evaluators, initial-system definitions,
README/status files, and Git were not changed by this closeout.
"""
    checkpoint_md = f"""# Round 10 Stage 4.5 Round 2 — mandatory checkpoint

Status: **STOPPED FAIL-CLOSED AT STAGE 4.5**.

- Five audit packages are coherent and independently replayed; scientific-integrity result is `0/5 PASS`.
- Stage 5 is not started and not authorized.
- No manuscript/Bib correction, canonical promotion, scientific execution/result refresh, Route or initial-system change, README/status change, or Git operation occurred in this closeout.
- Exact proposed next scope: `{REQUEST_JSON.name}` SHA-256 `{request_desc['sha256']}`.
- The next unqualified author reply `确认` authorizes only that exact request: 66 `replace_block` targets, one P30-S02 successor-Bib correction, named notes-side descendants, isolated previews, and a fresh Stage 4.5 Round 3.
- Any hash mismatch, unlisted target, scientific-value change, failed validation, or scope expansion must stop for renewed author direction.
"""
    report_raw = report_md.encode("utf-8")
    checkpoint_raw = checkpoint_md.encode("utf-8")
    final_audit["batch_report"] = pending_artifact(FINAL_REPORT_MD, report_raw)
    final_audit["mandatory_checkpoint"] = pending_artifact(CHECKPOINT_MD, checkpoint_raw)
    final_audit_raw = json_bytes(final_audit)
    atomic_write(REQUEST_JSON, request_raw)
    atomic_write(REQUEST_MD, request_md_raw)
    atomic_write(FINAL_AUDIT_JSON, final_audit_raw)
    atomic_write(FINAL_REPORT_MD, report_raw)
    atomic_write(CHECKPOINT_MD, checkpoint_raw)


def validate_closeout_for_receipt(independent_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    audit = load_json(FINAL_AUDIT_JSON)
    if audit.get("status") != "PASS_AUDIT_PACKAGE_COHERENT_WITH_FIVE_BLOCKING_FAIL_VERDICTS":
        raise RuntimeError("final audit status is not exact")
    if audit.get("scientific_integrity_batch_verdict") != "FAIL_0_OF_5_ELIGIBLE_FOR_STAGE5":
        raise RuntimeError("final audit scientific-integrity verdict drift")
    for key in [
        "stage5_started",
        "stage5_authorized",
        "canonical_promotion_performed",
        "git_operation_performed",
    ]:
        if audit.get(key) is not False:
            raise RuntimeError(f"final audit boundary {key} is not false")

    descriptor_checks = [
        (audit.get("authority"), AUTH_PATH, "authority"),
        (audit.get("input_lock"), LOCK_PATH, "input lock"),
        (audit.get("independent_review"), independent_path, "independent review"),
        (audit.get("correction_authorization_request"), REQUEST_JSON, "machine request"),
        (audit.get("correction_authorization_request_human"), REQUEST_MD, "human request"),
        (audit.get("batch_report"), FINAL_REPORT_MD, "batch report"),
        (audit.get("mandatory_checkpoint"), CHECKPOINT_MD, "mandatory checkpoint"),
    ]
    for expected, path, label in descriptor_checks:
        if expected != artifact(path):
            raise RuntimeError(f"{label} descriptor changed between artifacts and receipt")

    request = load_json(REQUEST_JSON)
    expected_request = build_request(request.get("generated_at_utc", ""))
    if request != expected_request:
        raise RuntimeError("machine correction request does not replay exactly")

    summaries = [paper_summary(paper_id, cfg) for paper_id, cfg in PAPERS.items()]
    aggregate = aggregate_summary(summaries)
    if audit.get("papers") != summaries or audit.get("aggregate") != aggregate:
        raise RuntimeError("final audit paper summaries or aggregate do not replay exactly")
    expected_route = {
        "formal_route_a_tuples": "0/5",
        "positive_arithmetic_A2": "0/5",
        "A3": "0/5",
        "A4": "0/5",
        "route_b_invocations": "0/5",
    }
    if audit.get("route_boundary") != expected_route:
        raise RuntimeError("final audit Route boundary drift")
    current_read_only = {name: sha_bytes((ROOT / name).read_bytes()) for name in READONLY_FILES}
    if audit.get("read_only_boundaries") != current_read_only:
        raise RuntimeError("final audit read-only boundaries drift")

    root_replay = replay_root_validator()
    stored_replay = {
        key: value for key, value in audit.get("root_replay", {}).items() if key != "semantics"
    }
    if stored_replay != root_replay:
        raise RuntimeError("root-validator replay changed between artifacts and receipt")
    return audit, root_replay


def build_receipt(stamp: str, independent_path: Path) -> None:
    required = [REQUEST_JSON, REQUEST_MD, FINAL_AUDIT_JSON, FINAL_REPORT_MD, CHECKPOINT_MD]
    if any(not path.exists() for path in required):
        raise RuntimeError("closeout artifacts are incomplete")
    validate_final_independent_review(independent_path)
    audit, root_replay = validate_closeout_for_receipt(independent_path)
    receipt = {
        "schema_version": "round10-stage4.5-round2-batch-validation-receipt/1.0",
        "generated_at_utc": stamp,
        "status": "PASS_AUDIT_PACKAGE_COHERENT_WITH_FIVE_FAIL_VERDICTS",
        "scientific_integrity_batch_verdict": "FAIL_0_OF_5_ELIGIBLE_FOR_STAGE5",
        "authority": artifact(AUTH_PATH),
        "input_lock": artifact(LOCK_PATH),
        "final_audit": artifact(FINAL_AUDIT_JSON),
        "batch_report": artifact(FINAL_REPORT_MD),
        "mandatory_checkpoint": artifact(CHECKPOINT_MD),
        "correction_authorization_request": artifact(REQUEST_JSON),
        "correction_authorization_request_human": artifact(REQUEST_MD),
        "independent_review": artifact(independent_path),
        "independent_validator": {
            **root_replay,
        },
        "aggregate": audit["aggregate"],
        "route_boundary": audit["route_boundary"],
        "read_only_boundaries": audit["read_only_boundaries"],
        "stage5_started": False,
        "stage5_authorized": False,
        "canonical_promotion_performed": False,
        "git_operation_performed": False,
    }
    atomic_write(RECEIPT_JSON, json_bytes(receipt))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["artifacts", "receipt"])
    parser.add_argument("--independent-review", required=True, type=Path)
    args = parser.parse_args()
    # Normalize lexical ``..`` without dereferencing symlinks; the strict
    # workspace-file check below must see and reject every symlink component.
    independent_path = Path(os.path.abspath(args.independent_review))
    require_workspace_file(independent_path, "final independent replay")
    stamp = utc_now()
    if args.mode == "artifacts":
        for path in [REQUEST_JSON, REQUEST_MD, FINAL_AUDIT_JSON, FINAL_REPORT_MD, CHECKPOINT_MD, RECEIPT_JSON]:
            if path.exists():
                raise RuntimeError(f"refusing to overwrite existing closeout artifact: {path.name}")
        build_closeout(stamp, independent_path)
        build_receipt(utc_now(), independent_path)
    else:
        if RECEIPT_JSON.exists():
            raise RuntimeError(f"refusing to overwrite existing receipt: {RECEIPT_JSON.name}")
        build_receipt(stamp, independent_path)


if __name__ == "__main__":
    main()
